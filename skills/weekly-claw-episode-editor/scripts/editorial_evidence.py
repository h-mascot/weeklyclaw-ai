#!/usr/bin/env python3
"""Validate bounded editorial evidence and frame-map structure.

This is a fail-closed structural check.  It does not listen to audio, decide
whether a contribution is editorially good, interpret native effects, or
certify that a baked mark appears in encoded playback.
"""
import argparse
import hashlib
import json
import math
import re
from fractions import Fraction
from pathlib import Path

from PIL import Image


VERSION = '2026-10-04.1'
PROFILE = 'editorial-evidence-2026-10-04.1'
SHA256 = re.compile(r'^[0-9a-f]{64}$')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def _integer(value, label, errors):
    if type(value) is not int:
        errors.append(label + ': explicit integer required')
        return None
    return value


def _rate(value, label, errors):
    """Read a rational frame rate without silently guessing an edit rate."""
    if value is None:
        return Fraction(1, 1)
    if isinstance(value, (list, tuple)) and len(value) == 2:
        numerator, denominator = value
    elif isinstance(value, dict):
        numerator = value.get('numerator', value.get('num'))
        denominator = value.get('denominator', value.get('den'))
    else:
        errors.append(label + ': rate must be a numerator/denominator pair')
        return None
    if type(numerator) is not int or type(denominator) is not int or numerator <= 0 or denominator <= 0:
        errors.append(label + ': rate numerator and denominator must be positive integers')
        return None
    return Fraction(numerator, denominator)


def _path(root, item):
    value = item.get('path') if isinstance(item, dict) else None
    if not isinstance(value, str) or not value:
        return None
    path = Path(value)
    return path if path.is_absolute() else root / path


def _hash_evidence(root, item, label, errors, verified=None):
    """Verify a path/hash record and return its decoded path, if valid."""
    if verified is None:
        verified = set()
    if not isinstance(item, dict):
        errors.append(label + ': hashed evidence object required')
        return None
    path = _path(root, item)
    digest = item.get('sha256')
    if path is None or not isinstance(digest, str) or not SHA256.fullmatch(digest):
        errors.append(label + ': path and lowercase SHA-256 required')
        return None
    key = (str(path), digest)
    if key in verified:
        return path
    verified.add(key)
    try:
        if not path.is_file() or sha(path) != digest:
            errors.append(label + ': missing or changed evidence')
            return None
    except (OSError, TypeError, ValueError):
        errors.append(label + ': unreadable evidence')
        return None
    return path


def _walk_hashes(root, value, label, errors, verified):
    """Check every explicit path/hash object, including nested evidence."""
    if isinstance(value, dict):
        has_path = 'path' in value
        has_hash = 'sha256' in value
        if has_path or has_hash:
            if has_path and has_hash:
                _hash_evidence(root, value, label, errors, verified)
            else:
                errors.append(label + ': path and sha256 must be supplied together')
        for key, child in value.items():
            if key not in ('path', 'sha256'):
                _walk_hashes(root, child, label + '.' + str(key), errors, verified)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk_hashes(root, child, label + '[' + str(index) + ']', errors, verified)


def _record_range(record, start_keys, end_keys, label, errors):
    if not isinstance(record, dict):
        errors.append(label + ': object required')
        return None
    start = next((record.get(key) for key in start_keys if key in record), None)
    end = next((record.get(key) for key in end_keys if key in record), None)
    if start is None and isinstance(record.get('range'), list) and len(record['range']) == 2:
        start, end = record['range']
    start = _integer(start, label + '.start', errors)
    end = _integer(end, label + '.end', errors)
    if start is None or end is None:
        return None
    if start < 0 or end <= start:
        errors.append(label + ': half-open range must satisfy 0 <= start < end')
        return None
    return start, end


def _normalise_segments(data, source_by_id, programme_rate, errors):
    raw = data.get('source_to_programme', data.get('timeline', data.get('segments')))
    if not isinstance(raw, list) or not raw:
        errors.append('source_to_programme: nonempty half-open segment list required')
        return [], None
    segments = []
    cursor = 0
    source_ranges = {}
    insert_ids = set()
    source_segment_ids = set()
    for index, item in enumerate(raw):
        label = 'source_to_programme[' + str(index) + ']'
        if not isinstance(item, dict):
            errors.append(label + ': object required')
            continue
        kind = item.get('kind', 'source')
        if kind not in ('source', 'insert'):
            errors.append(label + ': removed/cut/gap segments cannot fabricate a source mapping')
            continue
        source_id = item.get('source_id')
        if not isinstance(source_id, str) or not source_id:
            errors.append(label + ': source_id required for every retained segment')
            continue
        if source_id not in source_by_id:
            errors.append(label + ': unknown source_id ' + repr(source_id))
            continue
        programme_range = _record_range(item, ('programme_start', 'programme_in'),
                                        ('programme_end', 'programme_out'), label + '.programme', errors)
        source_range = _record_range(item, ('source_start', 'source_in'),
                                     ('source_end', 'source_out'), label + '.source', errors)
        if programme_range is None or source_range is None:
            continue
        programme_start, programme_end = programme_range
        source_start, source_end = source_range
        if programme_start != cursor:
            errors.append(label + ': programme ranges must be contiguous from frame zero')
        cursor = programme_end
        if item.get('removed_ranges') or item.get('cut_ranges') or item.get('removed_source_ranges'):
            errors.append(label + ': source range cannot claim continuity through removed material')
        rate = programme_rate
        if item.get('rate', item.get('frame_rate')) is not None:
            rate = _rate(item.get('rate', item.get('frame_rate')), label + '.rate', errors) or rate
        source_rate = _rate(source_by_id[source_id].get('rate'), source_id + '.rate', errors)
        if source_rate is None:
            source_rate = Fraction(1, 1)
        mapping_rate = rate
        if item.get('source_rate') is not None:
            source_rate = _rate(item.get('source_rate'), label + '.source_rate', errors) or source_rate
        if item.get('programme_rate') is not None:
            mapping_rate = _rate(item.get('programme_rate'), label + '.programme_rate', errors) or mapping_rate
        # Explicit frame rates make duration conversion deterministic.  With no
        # rates this is deliberately the rate-1 map; no time offset is guessed.
        source_duration = source_end - source_start
        programme_duration = programme_end - programme_start
        declared_source_duration = source_by_id[source_id].get('duration_frames')
        if declared_source_duration is not None and source_end > declared_source_duration:
            errors.append(label + ': source range exceeds declared source duration')
        if source_duration * mapping_rate != programme_duration * source_rate:
            errors.append(label + ': source/programme durations do not match the explicit rational rate')
        previous = source_ranges.setdefault(source_id, [])
        if any(source_start < old_end and source_end > old_start for old_start, old_end in previous):
            errors.append(label + ': overlapping source range would fabricate mapping through a cut')
        previous.append((source_start, source_end))
        if kind == 'insert':
            insert_ids.add(source_id)
        else:
            source_segment_ids.add(source_id)
        segments.append({
            'kind': kind,
            'source_id': source_id,
            'programme_start': programme_start,
            'programme_end': programme_end,
            'source_start': source_start,
            'source_end': source_end,
            'programme_rate': mapping_rate,
            'source_rate': source_rate,
        })
    if insert_ids & source_segment_ids:
        errors.append('source_to_programme: inserts must use source IDs separate from camera/source segments')
    total = data.get('programme_frames', data.get('programme_duration'))
    if total is None:
        errors.append('programme_frames: explicit total programme frame count required')
    else:
        total = _integer(total, 'programme_frames', errors)
        if total is not None and (total <= 0 or cursor != total):
            errors.append('source_to_programme: contiguous ranges do not cover programme_frames')
    return segments, total


def _check_removed_ranges(data, segments, errors):
    removals = data.get('removed_source_ranges', data.get('cut_ranges', data.get('removed_ranges', [])))
    if removals is None:
        return
    if not isinstance(removals, list):
        errors.append('removed_source_ranges: list required')
        return
    for index, removal in enumerate(removals):
        label = 'removed_source_ranges[' + str(index) + ']'
        if not isinstance(removal, dict):
            errors.append(label + ': object required')
            continue
        source_id = removal.get('source_id')
        bounds = _record_range(removal, ('source_start', 'start', 'source_in'),
                               ('source_end', 'end', 'source_out'), label, errors)
        if not isinstance(source_id, str) or bounds is None:
            errors.append(label + ': source_id and source half-open range required')
            continue
        start, end = bounds
        for segment in segments:
            if segment['source_id'] == source_id and start < segment['source_end'] and end > segment['source_start']:
                errors.append(label + ': removal overlaps a declared retained mapping')


def _coverage_record(record, label, errors):
    if not isinstance(record, dict):
        errors.append(label + ': evidence coverage object required')
        return
    source_id = record.get('source_id', record.get('source'))
    if not isinstance(source_id, str) or not source_id:
        errors.append(label + ': evidence source_id required')
    bounds = _record_range(record, ('source_start', 'source_in'),
                           ('source_end', 'source_out'), label, errors)
    if bounds is None:
        coverage = record.get('source_range', record.get('coverage'))
        if isinstance(coverage, dict):
            bounds = _record_range(coverage, ('source_start', 'source_in', 'start'),
                                   ('source_end', 'source_out', 'end'), label + '.coverage', errors)
        elif isinstance(coverage, list) and len(coverage) == 2:
            bounds = _record_range({'range': coverage}, ('source_start',), ('source_end',),
                                   label + '.coverage', errors)
        else:
            errors.append(label + ': source range/coverage required')
    if bounds is not None and bounds[1] <= bounds[0]:
        errors.append(label + ': evidence coverage must be nonempty')
    return source_id, bounds


def _check_solos(data, root, programme_frames, source_by_id, segments, errors, verified):
    solos = data.get('solos', data.get('solo_evidence', []))
    if solos is None:
        return
    if not isinstance(solos, list):
        errors.append('solos: list required')
        return
    for index, solo in enumerate(solos):
        label = 'solos[' + str(index) + ']'
        if not isinstance(solo, dict):
            errors.append(label + ': object required')
            continue
        declared = solo.get('declared_speaker')
        actual = solo.get('actual_speaker')
        if not isinstance(declared, str) or not declared.strip():
            errors.append(label + ': declared_speaker required')
        if not isinstance(actual, str) or not actual.strip():
            errors.append(label + ': actual_speaker required')
        elif actual != declared:
            errors.append(label + ': actual speaker does not match declared speaker')
        rationale = solo.get('sustained_contribution_rationale')
        if rationale is None and isinstance(solo.get('sustained_contribution'), dict):
            rationale = solo['sustained_contribution'].get('rationale')
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(label + ': sustained contribution rationale required')
        programme_range = _record_range(solo, ('programme_start', 'programme_in'),
                                        ('programme_end', 'programme_out'), label + '.programme', errors)
        if programme_range is not None and programme_frames is not None:
            if programme_range[1] > programme_frames:
                errors.append(label + ': programme interval exceeds programme_frames')
        for key in ('transcript_evidence', 'audio_evidence'):
            evidence = solo.get(key)
            if not isinstance(evidence, (dict, list)) or not evidence:
                errors.append(label + ': ' + key + ' required')
            else:
                _walk_hashes(root, evidence, label + '.' + key, errors, verified)
                records = evidence if isinstance(evidence, list) else [evidence]
                for record_index, record in enumerate(records):
                    evidence_label = label + '.' + key + '[' + str(record_index) + ']'
                    coverage = _coverage_record(record, evidence_label, errors)
                    if isinstance(record, dict):
                        _hash_evidence(root, record, evidence_label, errors, verified)
                    if coverage is not None:
                        source_id, source_range = coverage
                        if source_id not in source_by_id:
                            errors.append(evidence_label + ': unknown evidence source_id')
                        elif source_range is not None and programme_range is not None:
                            source_start, source_end = source_range
                            mapped = []
                            for segment in segments:
                                if (segment['source_id'] == source_id and
                                        segment['source_start'] <= source_start and
                                        source_end <= segment['source_end']):
                                    first = Fraction(segment['programme_start'], 1) + Fraction(
                                        source_start - segment['source_start'], 1) * segment['programme_rate'] / segment['source_rate']
                                    last = Fraction(segment['programme_start'], 1) + Fraction(
                                        source_end - segment['source_start'], 1) * segment['programme_rate'] / segment['source_rate']
                                    if first.denominator == 1 and last.denominator == 1:
                                        mapped.append((first.numerator, last.numerator))
                            if not any(first <= programme_range[0] and last >= programme_range[1]
                                       for first, last in mapped):
                                errors.append(evidence_label + ': source coverage does not cover the declared solo programme interval')


def _map_cue_end(cue, segments, errors, label):
    if not isinstance(cue, dict):
        errors.append(label + ': cue object required')
        return None
    source_id = cue.get('source_id')
    bounds = _record_range(cue, ('source_start', 'source_in'), ('source_end', 'source_out'), label, errors)
    if not isinstance(source_id, str) or bounds is None:
        errors.append(label + ': source_id and source completion range required')
        return None
    start, end = bounds
    matches = [s for s in segments if s['source_id'] == source_id and
               s['source_start'] <= start and end <= s['source_end']]
    if len(matches) != 1:
        errors.append(label + ': cue is removed or crosses a cut; no fabricated programme mapping')
        return None
    segment = matches[0]
    mapped = Fraction(segment['programme_start'], 1) + Fraction(
        end - segment['source_start'], 1) * segment['programme_rate'] / segment['source_rate']
    if mapped.denominator != 1:
        errors.append(label + ': cue completion does not land on an integer programme frame')
        return None
    return mapped.numerator


def _check_graphics(data, root, programme_frames, segments, errors, verified):
    graphics = data.get('graphics', data.get('graphic_overlays', []))
    if graphics is None:
        return
    if not isinstance(graphics, list):
        errors.append('graphics: list required')
        return
    cues = data.get('cues', data.get('speech_cues', []))
    if not isinstance(cues, list):
        errors.append('cues: list required when graphics are declared')
        return
    cue_by_id = {cue.get('id'): cue for cue in cues if isinstance(cue, dict) and isinstance(cue.get('id'), str)}
    for index, graphic in enumerate(graphics):
        label = 'graphics[' + str(index) + ']'
        if not isinstance(graphic, dict):
            errors.append(label + ': object required')
            continue
        cue_id = graphic.get('cue_id', graphic.get('relevant_cue_id'))
        cue = cue_by_id.get(cue_id)
        if cue is None:
            errors.append(label + ': relevant cue_id required')
            continue
        completed = _map_cue_end(cue, segments, errors, label + '.cue')
        onset = graphic.get('onset_programme_frame', graphic.get('programme_start'))
        onset = _integer(onset, label + '.onset_programme_frame', errors)
        if completed is not None and onset is not None and onset < completed:
            errors.append(label + ': graphic onset must be at or after the first frame after completed cue')
        declared = graphic.get('cue_completed_programme_frame')
        if declared is not None and declared != completed:
            errors.append(label + ': declared cue completion does not match source mapping')
        if onset is not None and programme_frames is not None and onset >= programme_frames:
            errors.append(label + ': graphic onset must be inside the programme')
        display_end = graphic.get('display_end_programme_frame', graphic.get('display_end', graphic.get('programme_end')))
        display_end = _integer(display_end, label + '.display_end_programme_frame', errors)
        if onset is not None and display_end is not None and display_end <= onset:
            errors.append(label + ': graphic display range must be nonempty')
        if display_end is not None and programme_frames is not None and display_end > programme_frames:
            errors.append(label + ': graphic display end exceeds programme_frames')
        asset = graphic.get('asset', graphic.get('asset_evidence'))
        _hash_evidence(root, asset, label + '.asset', errors, verified)


def _alpha_is_transparent(path):
    with Image.open(path) as image:
        image.load()
        if 'A' not in image.getbands() and 'transparency' not in image.info:
            return False
        alpha = image.convert('RGBA').getchannel('A')
        low, high = alpha.getextrema()
        return low == 0 and high > 0


def _check_marks(data, root, programme_frames, errors, verified):
    marks = data.get('programme_marks', data.get('program_marks'))
    if not isinstance(marks, list) or not marks:
        errors.append('programme_marks: one full-length programme mark declaration required')
        return
    if len(marks) != 1:
        errors.append('programme_marks: duplicate declared programme marks are rejected')
    for index, mark in enumerate(marks):
        label = 'programme_marks[' + str(index) + ']'
        if not isinstance(mark, dict):
            errors.append(label + ': object required')
            continue
        if mark.get('backing_plate') or mark.get('has_backing_plate') or mark.get('backing_plate_asset'):
            errors.append(label + ': backing plate is not permitted')
        position = mark.get('position')
        if isinstance(position, dict):
            scope, anchor = position.get('scope'), position.get('anchor')
        else:
            scope, anchor = mark.get('scope'), mark.get('anchor')
            if position == 'global-bottom-left':
                scope, anchor = 'global', 'bottom-left'
        if scope != 'global' or anchor != 'bottom-left':
            errors.append(label + ': mark must be fixed at global bottom-left')
        if mark.get('track') not in ('programme-mark', 'programme_marks'):
            errors.append(label + ': mark must be on the programme-mark track')
        if mark.get('keyframes') or mark.get('positions'):
            errors.append(label + ': moving mark declarations are not fixed-global-bottom-left')
        start = mark.get('programme_start', mark.get('start'))
        end = mark.get('programme_end', mark.get('end'))
        start = _integer(start, label + '.start', errors)
        end = _integer(end, label + '.end', errors)
        if start is not None and end is not None and (start != 0 or programme_frames is None or end != programme_frames):
            errors.append(label + ': mark must cover the complete [0, programme_frames) programme')
        asset = mark.get('asset', mark.get('asset_evidence'))
        path = _hash_evidence(root, asset, label + '.asset', errors, verified)
        if path is not None:
            try:
                if not _alpha_is_transparent(path):
                    errors.append(label + ': asset must contain a genuinely transparent alpha channel')
            except (OSError, ValueError, IndexError):
                errors.append(label + ': asset is not a decodable image with alpha')


def check(data, root):
    """Return a structured result for valid and malformed plans alike."""
    root = Path(root)
    errors = []
    verified = set()
    segments = []
    programme_frames = None
    try:
        if not isinstance(data, dict):
            return {'status': 'FAILED', 'errors': ['plan: object required'], 'limits': _limits()}
        anchor = data.get('validator_anchor', data.get('validator'))
        if not isinstance(anchor, dict):
            errors.append('validator_anchor: version and project hash required')
        else:
            if anchor.get('name') not in (None, 'editorial_evidence'):
                errors.append('validator_anchor: unsupported validator name')
            if anchor.get('version') != VERSION:
                errors.append('validator_anchor: unsupported validator version')
            anchor_hash = anchor.get('project_sha256', anchor.get('project_hash'))
            if not isinstance(anchor_hash, str) or not SHA256.fullmatch(anchor_hash):
                errors.append('validator_anchor: project SHA-256 required')
        project = data.get('project')
        project_path = _hash_evidence(root, project, 'project', errors, verified)
        if isinstance(anchor, dict) and isinstance(project, dict):
            anchor_hash = anchor.get('project_sha256', anchor.get('project_hash'))
            if anchor_hash != project.get('sha256'):
                errors.append('validator_anchor: project hash does not match project evidence')
        _walk_hashes(root, data, 'plan', errors, verified)

        sources = data.get('sources')
        source_by_id = {}
        if not isinstance(sources, list) or not sources:
            errors.append('sources: nonempty source roster required')
        else:
            for index, source in enumerate(sources):
                label = 'sources[' + str(index) + ']'
                if not isinstance(source, dict):
                    errors.append(label + ': object required')
                    continue
                source_id = source.get('id')
                if not isinstance(source_id, str) or not source_id:
                    errors.append(label + ': id required')
                elif source_id in source_by_id:
                    errors.append(label + ': duplicate source id')
                else:
                    source_by_id[source_id] = source
                _hash_evidence(root, source, label, errors, verified)
                if source.get('duration_frames') is not None:
                    duration = _integer(source.get('duration_frames'), label + '.duration_frames', errors)
                    if duration is not None and duration <= 0:
                        errors.append(label + ': duration_frames must be positive')
        programme_rate = _rate(data.get('programme_rate', data.get('programme_fps')),
                               'programme_rate', errors)
        if programme_rate is None:
            programme_rate = Fraction(1, 1)
        segments, programme_frames = _normalise_segments(data, source_by_id, programme_rate, errors)
        _check_removed_ranges(data, segments, errors)
        _check_solos(data, root, programme_frames, source_by_id, segments, errors, verified)
        _check_graphics(data, root, programme_frames, segments, errors, verified)
        _check_marks(data, root, programme_frames, errors, verified)
    except Exception as exc:  # malformed plans must produce a report, never a traceback
        errors.append('malformed_plan:' + type(exc).__name__ + ': ' + str(exc))
    return {
        'status': 'FAILED' if errors else 'CHECKED_SUBSET_PENDING_REVIEW',
        'errors': errors,
        'validator_version': VERSION,
        'profile': PROFILE,
        'limits': _limits(),
    }


def _limits():
    return ('Structural declarations and exact path/hash checks only. Verify actual source speech, '
            'native effect semantics, complete encoded playback, listening, baked mark pixels and '
            'human editorial quality separately. Never a creative, perceptual or release PASS.')


def write_report(path, report):
    with Path(path).open('x') as stream:
        stream.write(json.dumps(report, indent=2, allow_nan=False) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('plan')
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    plan_path = Path(args.plan)
    try:
        plan = json.loads(plan_path.read_text())
        report = check(plan, plan_path.parent)
    except Exception as exc:
        report = {'status': 'FAILED', 'errors': ['malformed_plan:' + type(exc).__name__ + ': ' + str(exc)],
                  'validator_version': VERSION, 'profile': PROFILE, 'limits': _limits()}
    try:
        report['plan_sha256'] = sha(plan_path)
    except (OSError, TypeError, ValueError):
        report['plan_sha256'] = None
    report['validator_sha256'] = sha(Path(__file__))
    write_report(args.report, report)
    print(report['status'])
    raise SystemExit(bool(report['errors']))
