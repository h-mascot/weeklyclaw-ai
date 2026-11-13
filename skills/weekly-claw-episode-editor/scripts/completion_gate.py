#!/usr/bin/env python3
"""Fail closed on incomplete, stale or unreconciled episode evidence; never publish."""
import argparse
import hashlib
import json
import math
import subprocess
from pathlib import Path

VERSION = 'weekly-claw-evidence-1'
REQUIRED = {'capability_preflight', 'source_inventory', 'source_review', 'source_coverage', 'edl_time_map',
            'native_proof', 'audio_listening', 'captions_words', 'master_technical',
            'master_visual', 'outro', 'independent_review'}
REVIEW_KINDS = {'audio_listening': 'listening', 'captions_words': 'caption_words',
                'independent_review': 'requirements_reconciliation'}
LIMITS = ('File/hash, coverage and review-receipt reconciliation only. Cannot establish '
          'truthfulness of observations, perceptual quality or publication authority. '
          'Existing exact-master media/native/editorial review remains required.')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def interval(value):
    if (not isinstance(value, list) or len(value) != 2 or
            any(isinstance(n, bool) or not isinstance(n, (int, float)) or
                not math.isfinite(n) for n in value) or not 0 <= value[0] < value[1]):
        raise ValueError('positive half-open interval required')
    return value


def covers(observed, expected):
    spans = sorted(interval(v) for v in observed)
    for begin, end in map(interval, expected):
        cursor = begin
        for left, right in spans:
            if right <= cursor:
                continue
            if left > cursor + 1e-6:
                break
            cursor = max(cursor, right)
            if cursor >= end - 1e-6:
                break
        if cursor < end - 1e-6:
            return False
    return True


def check(ledger, root, required_assets=('master', 'captions', 'source_manifest')):
    """Return an evidence decision; resolve relative paths against the episode root."""
    root = Path(root).resolve()
    errors, exceptions, assets = [], [], {}

    def require(condition, message):
        if not condition:
            errors.append(message)

    def file(ref, label, parse=False):
        if not isinstance(ref, dict) or not ref.get('path') or not ref.get('sha256'):
            errors.append(label + ': path and SHA-256 required')
            return None
        try:
            path = root / ref['path']
            require(path.is_file() and path.stat().st_size > 0, label + ': nonempty file required')
            if not path.is_file():
                return None
            if sha(path) != ref['sha256']:
                errors.append(label + ': hash mismatch')
                return None
            return json.loads(path.read_text()) if parse else path
        except (OSError, ValueError, TypeError) as exc:
            errors.append(label + ': ' + str(exc))
            return None

    def evidence(refs, label):
        require(isinstance(refs, list) and bool(refs), label + ': actual evidence required')
        for i, ref in enumerate(refs if isinstance(refs, list) else []):
            file(ref, label + '[' + str(i) + ']')

    def roster(rows, label):
        require(isinstance(rows, list), label + ': list required')
        result = {}
        for row in rows if isinstance(rows, list) else []:
            if not isinstance(row, dict) or not isinstance(row.get('id'), str) or not row['id']:
                errors.append(label + ': every row needs an ID')
                continue
            require(row['id'] not in result, label + ': duplicate ID ' + row['id'])
            result[row['id']] = row
        return result

    def accepted(ref, label, scope, bindings):
        receipt = file(ref, label, parse=True)
        if not isinstance(receipt, dict):
            return
        require(all(value and receipt.get('bindings', {}).get(key) == value for key, value in bindings.items()), label + ': stale acceptance input bindings')
        require(receipt.get('actor') == 'Henry', label + ': explicit Henry acceptance required')
        for key in ['source', 'instruction', 'limitations', 'observed_at']:
            require(bool(receipt.get(key)), label + ': ' + key + ' required')
        require(receipt.get('episode_id') == ledger.get('episode_id'), label + ': episode mismatch')
        require(receipt.get('master_sha256') == master, label + ': master mismatch')
        require(scope in receipt.get('requirement_ids', []), label + ': exact scope missing')
        exceptions.append({'id': scope, 'acceptance': ref, 'limitations': receipt.get('limitations')})

    try:
        if not isinstance(ledger, dict):
            raise ValueError('ledger object required')
        require(ledger.get('schema_version') == VERSION, 'unsupported evidence schema')
        require(bool(ledger.get('episode_id')) and bool(ledger.get('revision')), 'episode/revision required')
        capabilities = roster(ledger.get('capabilities'), 'capabilities')
        for name in ['media_inspection', 'source_transcript', 'native_render', 'brand_assets', 'audio_review']:
            capability = capabilities.get(name, {})
            require(capability.get('status') == 'VERIFIED' and all(capability.get(k) for k in ['probe', 'host', 'observed_at']), 'capability.' + name + ': actual successful probe required')
            evidence(capability.get('evidence'), 'capability.' + name + '.evidence')
        for name in set(required_assets) | {'master', 'captions', 'source_manifest'}:
            ref = ledger.get('assets', {}).get(name)
            if file(ref, 'asset.' + name):
                assets[name] = ref
        master = assets.get('master', {}).get('sha256')
        master_duration = None
        frame_tolerance = 1e-6
        if 'master' in assets:
            try:
                actual_probe = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,avg_frame_rate', '-of', 'json', str(root / assets['master']['path'])], stderr=subprocess.PIPE, text=True, timeout=30))
                master_duration = float(actual_probe['format']['duration'])
                interval([0, master_duration])
                video = next(stream for stream in actual_probe['streams'] if stream.get('codec_type') == 'video')
                numerator, denominator = map(float, video['avg_frame_rate'].split('/'))
                frame_tolerance = denominator / numerator + 1e-6
            except (OSError, ValueError, KeyError, StopIteration, ZeroDivisionError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
                errors.append('master: actual media duration/frame rate unavailable: ' + str(exc))
        manifest = file(ledger.get('assets', {}).get('source_manifest'), 'source_manifest', parse=True) or {}
        sources = roster(manifest.get('sources'), 'source_manifest.sources')
        require(bool(sources), 'source_manifest: required sources missing')
        cleanup = None
        for name, source in sources.items():
            if (root / source.get('path', '')).is_file():
                file(source, 'source.' + name)
                continue
            # Proper accepted-upload cleanup must not force a new source download.
            if cleanup is None:
                cleanup = file(ledger.get('source_cleanup'), 'source_cleanup', parse=True) or {}
                require(cleanup.get('episode_id') == ledger.get('episode_id') and cleanup.get('master_sha256') == master and bool(master), 'source_cleanup: episode/master mismatch')
                checks = roster(cleanup.get('acceptance_checks'), 'source_cleanup.acceptance_checks')
                for check_id in ['account', 'visibility', 'picture', 'audio', 'ending', 'youtube_checks']:
                    receipt = checks.get(check_id, {})
                    require(receipt.get('result') == 'PASS' and all(receipt.get(k) for k in ['observed_at', 'observations']), 'source_cleanup.' + check_id + ': acceptance evidence missing')
                    evidence(receipt.get('evidence'), 'source_cleanup.' + check_id)
            deleted = roster(cleanup.get('deleted_sources'), 'source_cleanup.deleted_sources').get(name, {})
            require(deleted.get('path') == source.get('path') and deleted.get('sha256') == source.get('sha256'), 'source.' + name + ': missing without accepted-cleanup identity')
            verification = file(deleted.get('verification'), 'source.' + name + '.retained_verification', parse=True) or {}
            require(verification.get('id') == name and verification.get('sha256') == source.get('sha256') and isinstance(verification.get('bytes'), int) and verification['bytes'] > 0 and bool(verification.get('verified_at')), 'source.' + name + ': retained ingest identity missing')
            probe = file(verification.get('probe'), 'source.' + name + '.retained_probe', parse=True) or {}
            require(bool(probe.get('streams')) and float(probe.get('format', {}).get('duration', 0)) > 0, 'source.' + name + ': retained media probe missing')

        spec = file(ledger.get('requirement_set'), 'requirement_set', parse=True) or {}
        documents = roster(spec.get('documents'), 'requirement_set.documents')
        for name, doc in documents.items():
            file(doc, 'document.' + name)
        definitions = roster(spec.get('requirements'), 'requirement_set.requirements')
        require(REQUIRED <= definitions.keys(), 'requirement_set: mandatory requirements missing: ' + ','.join(sorted(REQUIRED - definitions.keys())))
        rows = roster(ledger.get('requirements'), 'requirements')
        require(rows.keys() == definitions.keys(), 'requirements: missing or extra requirement IDs')

        universe = file(ledger.get('source_universe'), 'source_universe', parse=True) or {}
        require(universe.get('source_manifest_sha256') == assets.get('source_manifest', {}).get('sha256'), 'source_universe: source manifest mismatch')
        reviewed = roster(universe.get('sources'), 'source_universe.sources')
        require(reviewed.keys() == sources.keys(), 'source_universe: missing or extra source IDs')
        expected_items = set()
        for name, source in sources.items():
            duration = source.get('duration')
            bounds = interval([0, duration])
            review = reviewed.get(name, {})
            require(covers(review.get('reviewed_intervals', []), [bounds]), 'source.' + name + ': unreviewed source interval')
            evidence(review.get('evidence'), 'source.' + name + '.review')
            require(source.get('kind') in ['camera', 'audio', 'screen', 'composite', 'archive', 'other'], 'source.' + name + ': actual source kind required')
            item_ids = review.get('item_ids', [])
            if source.get('kind') == 'screen':
                require(bool(item_ids), 'source.' + name + ': screen item inventory or explicit source exclusion required')
            require(isinstance(item_ids, list) and len(item_ids) == len(set(item_ids)), 'source.' + name + ': invalid item IDs')
            require(not expected_items.intersection(item_ids), 'source.' + name + ': item ID assigned to multiple sources')
            expected_items.update(item_ids)
        items = roster(universe.get('items'), 'source_universe.items')
        require(items.keys() == expected_items, 'source_universe: missing or extra source item IDs')
        for name, item in items.items():
            prefix = 'source_item.' + name
            source_id = item.get('source_id')
            require(source_id in sources, prefix + ': source missing')
            left, right = interval(item.get('source_interval'))
            require(source_id in sources and right <= sources[source_id].get('duration', 0), prefix + ': source bounds invalid')
            require(name in reviewed.get(source_id, {}).get('item_ids', []), prefix + ': wrong source item roster')
            require(item.get('kind') in ['static', 'motion'], prefix + ': actual static/motion kind required')
            disposition = item.get('disposition')
            if disposition == 'included':
                start, end = interval(item.get('programme_interval'))
                require(item.get('master_sha256') == master, prefix + ': stale master')
                require(master_duration is not None and end <= master_duration + frame_tolerance, prefix + ': programme bounds exceed actual master')
                proof = item.get('proof', [])
                evidence(proof, prefix + '.proof')
                times = [p.get('programme_time') for p in proof]
                require(len(set(times)) >= 3 and all(isinstance(t, (int, float)) and not isinstance(t, bool) and start <= t <= end for t in times) and abs(min(times) - start) <= 1e-6 and abs(max(times) - end) <= 1e-6, prefix + ': onset/content/exit observations required')
                require(item.get('treatment') in ['static', 'motion'], prefix + ': static/motion treatment required')
                if item.get('kind') == 'motion':
                    require(item.get('treatment') == 'motion', prefix + ': required motion replaced with still')
                    require(abs((right - left) - (end - start)) <= frame_tolerance, prefix + ': motion duration does not preserve source time')
            elif disposition == 'excluded':
                require(item.get('reason') in ['duplicate', 'setup', 'removed_discussion', 'private', 'unusable'], prefix + ': unsupported exclusion')
                evidence(item.get('evidence'), prefix + '.exclusion')
                require(bool(item.get('explanation')), prefix + ': exclusion explanation required')
            elif disposition == 'accepted_exception':
                accepted(item.get('acceptance'), prefix + '.acceptance', 'source_item:' + name, {'master': master, 'requirement_set': ledger.get('requirement_set', {}).get('sha256'), 'source_manifest': assets.get('source_manifest', {}).get('sha256'), 'source_item': hashlib.sha256(json.dumps({k: v for k, v in item.items() if k != 'acceptance'}, sort_keys=True, separators=(',', ':')).encode()).hexdigest()})
            else:
                errors.append(prefix + ': unresolved coverage')

        for name, definition in definitions.items():
            row = rows.get(name, {})
            prefix = 'requirement.' + name
            require(definition.get('document_id') in documents and bool(definition.get('section')) and bool(definition.get('requirement')), prefix + ': source locator required')
            required_bindings = {'requirement_set': ledger.get('requirement_set', {}).get('sha256'),
                                 'source_manifest': assets.get('source_manifest', {}).get('sha256'),
                                 'source_universe': ledger.get('source_universe', {}).get('sha256')}
            if definition.get('master_bound') or name in REVIEW_KINDS or name in {'master_technical', 'master_visual', 'outro', 'source_coverage'}:
                required_bindings['master'] = master
            if name in {'captions_words', 'independent_review'}:
                required_bindings['captions'] = assets.get('captions', {}).get('sha256')
            for asset_name in definition.get('asset_bindings', []):
                required_bindings[asset_name] = assets.get(asset_name, {}).get('sha256')
            require(all(value and row.get('bindings', {}).get(key) == value for key, value in required_bindings.items()), prefix + ': stale input bindings')
            status = row.get('status')
            if status == 'ACCEPTED_EXCEPTION':
                accepted(row.get('acceptance'), prefix + '.acceptance', name, required_bindings)
                continue
            if status == 'NOT_APPLICABLE':
                require(name not in REQUIRED and definition.get('conditional') is True and bool(row.get('reason')), prefix + ': inapplicability unsupported')
                evidence(row.get('evidence'), prefix + '.applicability')
                continue
            require(status == 'VERIFIED', prefix + ': pending, failed or missing evidence')
            evidence(row.get('evidence'), prefix + '.evidence')
            if definition.get('master_bound') or name in REVIEW_KINDS or name in {'master_technical', 'master_visual', 'outro', 'source_coverage'}:
                require(row.get('master_sha256') == master and bool(master), prefix + ': stale master')
            kind = REVIEW_KINDS.get(name, definition.get('review_kind'))
            if kind:
                review = file(row.get('review'), prefix + '.review', parse=True) or {}
                require(all(value and review.get('bindings', {}).get(key) == value for key, value in required_bindings.items()), prefix + ': stale review input bindings')
                require(review.get('kind') == kind and review.get('result') == 'PASS', prefix + ': actual review incomplete')
                require(review.get('master_sha256') == master and bool(master), prefix + ': review master mismatch')
                require(all(review.get(k) for k in ['reviewer', 'method', 'observations', 'observed_at']), prefix + ': actual review observations required')
                if name in {'audio_listening', 'captions_words'}:
                    expected = definition.get('required_intervals', [])
                    require(master_duration is not None and bool(expected) and covers(expected, [[0, master_duration]]), prefix + ': expected review span does not cover actual master')
                    require(bool(expected) and covers(review.get('programme_intervals', []), expected), prefix + ': review coverage incomplete')
                if name == 'independent_review':
                    require(set(review.get('requirement_ids', [])) == definitions.keys(), prefix + ': review did not reconcile all requirements')
                    require(set(review.get('source_item_ids', [])) == items.keys(), prefix + ': review did not reconcile all source items')
        require(bool(documents), 'requirement_set: current directive documents missing')
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        errors.append('malformed evidence: ' + str(exc))
    return {'schema_version': VERSION,
            'status': 'INCOMPLETE' if errors else 'EVIDENCE_COMPLETE_WITH_EXCEPTIONS' if exceptions else 'EVIDENCE_COMPLETE',
            'errors': errors, 'accepted_exceptions': exceptions, 'assets': assets, 'master_duration': locals().get('master_duration'),
            'requirement_set': ledger.get('requirement_set') if isinstance(ledger, dict) else None,
            'source_universe': ledger.get('source_universe') if isinstance(ledger, dict) else None,
            'limits': LIMITS}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ledger', type=Path)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--require-asset', action='append', default=[])
    args = parser.parse_args()
    try:
        result = check(json.loads(args.ledger.read_text()), args.ledger.parent,
                       ('master', 'captions', 'source_manifest', *args.require_asset))
        result['ledger_sha256'] = sha(args.ledger)
    except (OSError, ValueError) as exc:
        result = {'status': 'INCOMPLETE', 'errors': [str(exc)], 'limits': LIMITS}
    result['validator_sha256'] = sha(__file__)
    with args.report.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(result['status'])
    return int(result['status'] == 'INCOMPLETE')


if __name__ == '__main__':
    raise SystemExit(main())
