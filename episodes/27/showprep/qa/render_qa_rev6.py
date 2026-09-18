#!/usr/bin/env python3
"""Render QA for rev6 grids: overflow + canaries + grid layout assertions."""
import asyncio, json, pathlib, re, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep')
OUT = ROOT / 'qa/render-1600x900-rev6'
OUT.mkdir(parents=True, exist_ok=True)

CANARIES = [
    ('s-cold-open', 'eight stories'),
    ('s-seg-grid-a', 'Hugging Face'),
    ('s-seg-grid-b', 'Flash-Next'),
    ('s-signal-outside', 'OpenClaw Went Viral'),
    ('s-hot-take', 'bad for open source'),
    ('s-watch', 'September 4'),
    ('s-sources', 'cnbc'),
]

async def main():
    fails = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={'width': 1600, 'height': 900})
        await page.goto(f'file://{ROOT / "revs/deck.rev6.html"}')
        await page.wait_for_timeout(1500)
        slides = await page.evaluate("() => Array.from(document.querySelectorAll('.slide')).map(s => s.id)")
        print('slides:', len(slides), slides)
        total = await page.evaluate("() => document.getElementById('slideTotal') && document.getElementById('slideTotal').textContent")
        dots = await page.evaluate("() => document.getElementById('navDots') ? document.getElementById('navDots').children.length : -1")
        print('slideTotal:', total, 'navDots:', dots)
        if int(total) != len(slides) or dots != len(slides):
            fails.append({'check': 'nav parity', 'total': total, 'dots': dots, 'slides': len(slides)})
        for i, sid in enumerate(slides):
            await page.evaluate(f"() => document.querySelectorAll('.slide').forEach((s,j)=>s.classList.toggle('active', j==={i}))")
            await page.wait_for_timeout(250)
            # overflow check on slide content
            ov = await page.evaluate(f"""() => {{
                const s = document.querySelectorAll('.slide')[{i}];
                const c = s.querySelector('.content') || s;
                return {{sh: c.scrollHeight, ch: c.clientHeight, body: document.documentElement.scrollHeight}};
            }}""")
            if ov['sh'] - ov['ch'] > 6:
                fails.append({'slide': sid, 'overflow': ov['sh'] - ov['ch']})
            await page.screenshot(path=str(OUT / f'{i+1:02d}-{sid}.png'))
        # canaries
        html = (ROOT / 'revs/deck.rev6.html').read_text()
        for sid, canary in CANARIES:
            i = html.find(f'id="{sid}"')
            i2 = html.find('<div class="slide" id="s-', i + 10)
            seg = html[i:i2 if i2 > 0 else len(html)]
            if canary.lower() not in seg.lower():
                fails.append({'slide': sid, 'canary_missing': canary})
        # grid assertions
        for sid, cols, rows in [('s-seg-grid-a', 2, 2), ('s-seg-grid-b', 2, 2)]:
            g = await page.evaluate(f"""() => {{
                const s = document.getElementById('{sid}');
                const grid = s.querySelector('.story-grid');
                if (!grid) return null;
                const cs = getComputedStyle(grid);
                const cards = grid.querySelectorAll('.story-card');
                const r1 = grid.getBoundingClientRect(); 
                return {{cols: cs.gridTemplateColumns.split(' ').length, cards: cards.length, visible: r1.width > 0}};
            }}""")
            print(sid, 'grid:', json.dumps(g))
            if not g or g['cards'] != 4 or g['cols'] != 2 or not g['visible']:
                fails.append({'slide': sid, 'grid_broken': g})
        await browser.close()
    if fails:
        print(json.dumps(fails, indent=2)); sys.exit(1)
    print('=== RENDER-QA PASS (rev6) ===')

asyncio.run(main())
