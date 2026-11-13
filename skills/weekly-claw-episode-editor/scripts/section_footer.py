"""Established E28/E29 Weekly Claw footer; source-verified literal typography."""
from pathlib import Path
import os
import json
import hashlib
from urllib.parse import urlparse
from PIL import Image, ImageDraw, ImageFont

SIZE = (1920, 1080)
PANEL = (180, 825, 1820, 1035)
FONTS = Path('/System/Library/Fonts/Supplemental')


def font(size, bold=False):
    key = 'WEEKLYCLAW_FOOTER_FONT_BOLD' if bold else 'WEEKLYCLAW_FOOTER_FONT_REGULAR'
    path = Path(os.environ.get(key, str(FONTS / ('Arial Bold.ttf' if bold else 'Arial.ttf'))))
    if not path.is_file():
        raise FileNotFoundError(f'Footer font missing: {path}. Set {key} explicitly and review native/mobile geometry; no silent font substitution.')
    return ImageFont.truetype(str(path), size)


def wrapped(draw, value, face, width):
    lines = []
    for paragraph in value.split('\n'):
        line = ''
        for word in paragraph.split():
            candidate = f'{line} {word}'.strip()
            if draw.textlength(candidate, font=face) <= width:
                line = candidate
            else:
                if not line or draw.textlength(word, font=face) > width:
                    raise ValueError('Unbreakable footer text exceeds width')
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def text(draw, position, value, size, fill, bold=False, width=None):
    face = font(size, bold)
    bounds = draw.textbbox(position, value, font=face, anchor='lt')
    if bounds[0] < 0 or bounds[1] < 0 or bounds[2] > SIZE[0] or bounds[3] > SIZE[1]:
        raise ValueError('Footer text outside canvas')
    if width is not None and draw.textlength(value, font=face) > width:
        raise ValueError('Footer text exceeds allocated width')
    draw.text(position, value, font=face, fill=fill, anchor='lt')


def render_correction_card(correction, output_path):
    image = Image.new('RGBA', SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(PANEL, radius=24, fill='#163D35')
    draw.rounded_rectangle((202, 849, 208, 1011), radius=3, fill='#83CFB6')
    url = correction.get('url')
    host = urlparse(url if '://' in url else 'https://' + url).netloc.removeprefix('www.') if url else 'WEEKLY CLAW · EDITORIAL NOTE'
    host_width = draw.textlength(host, font=font(25))
    text(draw, (234, 850), str(correction['title']), 25, '#83CFB6', bold=True, width=850)
    text(draw, (round(1775 - host_width), 852), host, 25, '#B2C9BD', width=650)
    lines = wrapped(draw, str(correction['text']), font(36), 1540)
    if len(lines) > 2:
        raise ValueError('Footer exceeds two lines; reflow or split in time, never silently truncate')
    for index, line in enumerate(lines):
        text(draw, (234, 904 + index * 47), line, 36, '#F5F2E9', width=1540)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format='PNG', optimize=True)
    fonts = {}
    for label, bold in [('regular', False), ('bold', True)]:
        fp = Path(font(25, bold).path)
        fonts[label] = {'path': str(fp), 'sha256': hashlib.sha256(fp.read_bytes()).hexdigest()}
    receipt = {'output_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'fonts': fonts, 'panel': PANEL, 'canvas': SIZE, 'review_status': 'NATIVE_AND_MOBILE_VISUAL_REVIEW_REQUIRED'}
    path.with_suffix(path.suffix + '.fonts.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return path
