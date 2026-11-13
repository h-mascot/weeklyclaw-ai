"""Weekly Claw camera/section-note preflight, shared by previews and renders.

This verifies measurable inputs, not taste, listening, or publication approval.
"""
import argparse
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

QUALITY_VERSION = '2026-09-12.1'
CAMERA_BOX = [240, 0, 1440, 810]


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024**2), b''):
            digest.update(chunk)
    return digest.hexdigest()


def dimensions(values, count, name):
    if not isinstance(values, list) or len(values) != count or any(type(v) is not int for v in values):
        raise ValueError(name + ' requires explicit integer dimensions')
    return values


def camera_filter(transform, source_size, color=None):
    """Build the actual filter only after validating crop, pixel scale and padding."""
    w, h, x, y = dimensions(transform['crop'], 4, 'crop')
    sw, sh = dimensions(transform['scale'], 2, 'scale')
    source_w, source_h = source_size
    if min(w, h, sw, sh) <= 0 or min(x, y) < 0 or x + w > source_w or y + h > source_h:
        raise ValueError('camera crop outside source or invalid dimensions')
    if any(v % 2 for v in (w, h, x, y, sw, sh)):
        raise ValueError('camera dimensions and offsets must be even for yuv420p')
    if sw > w or sh > h:
        raise ValueError('camera transform enlarges source pixels; use native/downscaled picture with padding')
    if abs(sw / w - sh / h) > 0.001:
        raise ValueError('camera transform distorts aspect ratio')
    filters = [f'crop={w}:{h}:{x}:{y}']
    if (sw, sh) != (w, h):
        filters.append(f'scale={sw}:{sh}:flags=lanczos')
    if color:
        bounds = {'gamma': (0.5, 2), 'contrast': (0.5, 2), 'brightness': (-0.2, 0.2), 'saturation': (0.5, 1.5)}
        if set(color) - set(bounds):
            raise ValueError('unsupported colour operation; explicitly review a new processing path')
        for key, value in color.items():
            if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
                raise ValueError('invalid colour value')
            if not bounds[key][0] <= value <= bounds[key][1]:
                raise ValueError('colour adjustment outside conservative review range')
        filters.append('eq=' + ':'.join(f'{key}={color[key]}' for key in sorted(color)))
    if 'pad' in transform:
        pw, ph, px, py = dimensions(transform['pad'], 4, 'pad')
        if min(px, py) < 0 or px + sw > pw or py + sh > ph or any(v % 2 for v in (pw, ph, px, py)):
            raise ValueError('invalid camera padding')
        filters.append(f'pad={pw}:{ph}:{px}:{py}:0x0f2c25')
    return ','.join(filters) + ',setsar=1,setpts=PTS-STARTPTS'


def validate_plan(plan, source_sizes):
    errors = []
    if not source_sizes:
        errors.append('nonempty independent camera roster required')
    if (plan.get('width'), plan.get('height')) != (1920, 1080):
        errors.append('delivery canvas must be 1920x1080 for this profile')
    for mode in ('solo', 'group'):
        transforms = plan.get('framing', {}).get(mode, {})
        if set(transforms) != set(source_sizes):
            errors.append(mode + ': camera source/transform roster mismatch')
        for person, transform in transforms.items():
            try:
                camera_filter(transform, source_sizes[person])
                output_size = transform.get('pad', transform['scale'])[:2]
                if output_size != ([1920, 1080] if mode == 'solo' else [960, 1080]):
                    raise ValueError('camera tile does not fit the solo/group delivery layout')
            except (ValueError, KeyError, TypeError) as error:
                errors.append(f'{mode}/{person}: {error}')
    if not plan.get('blocks'):
        errors.append('nonempty layout plan required')
    for block in plan.get('blocks', []):
        layout = block.get('layout')
        if layout == 'group' and set(block.get('participants', [])) != set(source_sizes):
            errors.append(block['id'] + ': group participants do not match camera roster')
        elif layout in source_sizes and block.get('participants') != [layout]:
            errors.append(block['id'] + ': solo participant does not match camera')
        elif layout not in ('group', *source_sizes) and not block.get('screen') and not block.get('card'):
            errors.append(block['id'] + ': unrecognized camera/layout block')
        card = block.get('card')
        # A source evidence asset is distinct from an information/fact-check note.
        if card and card.get('kind') != 'source_evidence':
            footer = block.get('footer')
            if not footer or block.get('layout') not in ('group', *source_sizes):
                errors.append(block['id'] + ': information note must retain live cameras and section footer')
            elif footer.get('camera_box') != CAMERA_BOX:
                errors.append(block['id'] + ': footer must reserve the established camera area')
            elif footer.get('displayed_text', '').split() != card.get('text', '').split():
                errors.append(block['id'] + ': footer wording changed')
    return errors


def contained(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('quality evidence/assets must use episode-relative paths')
    target = (root / path).resolve()
    if root.resolve() not in target.parents:
        raise ValueError('quality evidence/assets must stay inside the episode')
    return target


def footer_geometry(path):
    """Verify decoded RGBA geometry, not just a claimed PNG filename/hash.

    Word accuracy still requires the shared deterministic generator and visual QA.
    ffmpeg is already required on render hosts; Pillow is only needed to make assets.
    """
    data = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height,pix_fmt', '-of', 'json', str(path)]))['streams'][0]
    if (data['width'], data['height'], data['pix_fmt']) != (1920, 1080, 'rgba'):
        raise ValueError('footer must be the full-canvas RGBA section asset')
    result = subprocess.run(['ffmpeg', '-v', 'info', '-nostdin', '-i', str(path),
        '-vf', 'alphaextract,bbox=min_val=1', '-frames:v', '1', '-f', 'null', '-'],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    bounds = re.search(r'x1:(\d+) x2:(\d+) y1:(\d+) y2:(\d+)', result.stderr)
    if not bounds or tuple(map(int, bounds.groups())) != (180, 1820, 825, 1035):
        raise ValueError('footer alpha must stay in the established section panel; full-page/opaque assets rejected')


def preflight(plan_path, report_path=None):
    plan_path = Path(plan_path)
    root = plan_path.parent
    plan = json.loads(plan_path.read_text())
    contract = plan.get('quality_contract', {})
    if contract.get('version') != QUALITY_VERSION:
        raise ValueError('missing/current quality profile not recorded')
    baseline = contract.get('baseline_master_sha256', '')
    if len(baseline) != 64 or any(c not in '0123456789abcdef' for c in baseline):
        raise ValueError('approved visual baseline SHA-256 required; not approval for this new master')
    evidence = contract['review_evidence']
    if not evidence:
        raise ValueError('matched-size source/framing/colour review evidence required')
    for item in evidence:
        if sha(contained(root, item['path'])) != item['sha256']:
            raise ValueError('quality review evidence hash mismatch')
    rows = json.loads((root / 'ingest-state.json').read_text())['rows']
    sources, sizes = {}, {}
    for person, name in contract['camera_sources'].items():
        if Path(name).name != name:
            raise ValueError('camera source must be a filename in the episode sources directory')
        row = next(r for r in rows if r['participant'] == person and r['kind'] == 'aligned_camera'
                   and Path(r['local_path']).name == name)
        source = root / 'sources' / name
        if row['state'] != 'VERIFIED' or sha(source) != row['sha256']:
            raise ValueError('camera is not the verified independent source')
        media = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height', '-of', 'json', str(source)]))['streams'][0]
        sizes[person] = (media['width'], media['height'])
        sources[person] = row['sha256']
    errors = validate_plan(plan, sizes)
    if set(contract.get('color', {})) != set(sizes):
        errors.append('every camera needs an explicit reviewed colour decision, including no change')
    for mode in ('solo', 'group'):
        for person, transform in plan.get('framing', {}).get(mode, {}).items():
            try:
                camera_filter(transform, sizes[person], contract.get('color', {}).get(person))
            except (ValueError, KeyError, TypeError) as error:
                errors.append(f'{mode}/{person}: {error}')
    for block in plan.get('blocks', []):
        if block.get('footer'):
            asset = contained(root, block['footer']['asset'])
            if sha(asset) != block['footer']['sha256']:
                errors.append(block['id'] + ': footer asset changed')
            try:
                footer_geometry(asset)
            except (ValueError, KeyError, IndexError, subprocess.CalledProcessError) as error:
                errors.append(block['id'] + ': invalid section footer: ' + str(error))
    report = {'quality_version': QUALITY_VERSION, 'plan_sha256': sha(plan_path),
              'validator_sha256': sha(Path(__file__)), 'source_sha256': sources,
              'review_evidence': evidence, 'errors': errors, 'passed': not errors,
              'limits': 'Input/geometry proof only; requires exact-master visual/audio/media QA. Not publication approval.'}
    if report_path:
        Path(report_path).write_text(json.dumps(report, indent=2) + '\n')
    if errors:
        raise ValueError('\n'.join(errors))
    return plan, sizes, report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('plan')
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    preflight(args.plan, args.report)
    print('PASS: source, native camera scale, reviewed colour and section-footer preflight')
