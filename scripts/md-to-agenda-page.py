#!/usr/bin/env python3
"""Generate a static agenda.html page from an episode's agenda.md."""
import html
import re
import sys
from pathlib import Path


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r'`(.*?)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
    return s


def gen(md_path: str, out_path: str, title: str, badge: str) -> None:
    md = Path(md_path).read_text()
    out = []
    for line in md.splitlines():
        if line.startswith('# '):
            out.append(f'<h1>{inline(line[2:])}</h1>')
        elif line.startswith('## '):
            out.append(f'<h2>{inline(line[3:])}</h2>')
        elif line.startswith('- '):
            out.append(f'<li>{inline(line[2:])}</li>')
        elif line.strip() == '':
            out.append('')
        else:
            out.append(f'<p>{inline(line)}</p>')
    body = '\n'.join(out)
    body = re.sub(
        r'(<li>.*?</li>)(\n<li>.*?</li>)*',
        lambda m: '<ul>\n' + m.group(0) + '\n</ul>',
        body,
        flags=re.S,
    )
    page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>body{{margin:0;background:#fffdf8;color:#101418;font:16px/1.6 Georgia,serif}}main{{max-width:820px;margin:0 auto;padding:48px 24px 80px}}h1{{font-size:1.7rem}}h2{{font-size:1.1rem;margin:2rem 0 .5rem;border-bottom:2px solid #e5e0d5;padding-bottom:.3rem;color:#0b3c42}}ul{{padding-left:1.3rem}}code{{font-family:ui-monospace,monospace;font-size:.85em;background:#f1ede2;padding:1px 5px;border-radius:4px}}</style>
</head><body><main><span style="display:inline-block;font:700 11px/1 ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:#6b7280;border-radius:999px;padding:6px 12px;margin-bottom:20px">{html.escape(badge)}</span>
{body}
</main></body></html>'''
    Path(out_path).write_text(page)
    print('wrote', out_path)


if __name__ == '__main__':
    md_path, out_path, title, badge = sys.argv[1:5]
    gen(md_path, out_path, title, badge)
