#!/usr/bin/env python3
"""Ep27 rev3 artifact capture, attempt 2: dismiss consent walls, fallback sources."""
import asyncio, pathlib
from playwright.async_api import async_playwright

OUT = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/assets/images/artifacts')

CONSENT_TEXTS = ['Consent', 'I Agree', 'Accept', 'Agree', 'Accept all', 'Got it']

async def try_consent(pg):
    for t in CONSENT_TEXTS:
        try:
            btn = pg.get_by_role('button', name=t, exact=False).first
            if await btn.count() and await btn.is_visible():
                await btn.click(timeout=3000)
                await pg.wait_for_timeout(1200)
                return t
        except Exception:
            continue
    # common one-off selectors
    for sel in ['button:has-text("Consent")', '#onetrust-accept-btn-handler', 'button:has-text("Accept All")', 'button[title="Consent"]']:
        try:
            el = pg.locator(sel).first
            if await el.count() and await el.is_visible():
                await el.click(timeout=2500)
                await pg.wait_for_timeout(1200)
                return sel
        except Exception:
            continue
    return None

async def clip(pg, sel, fname, top_clip=None):
    el = pg.locator(sel).first
    box = await el.bounding_box()
    await pg.screenshot(path=str(OUT / fname), clip={'x': 0, 'y': 0, 'width': 1280, 'height': min(top_clip or 900, box['height'] if box else 900)})
    return (OUT / fname).stat().st_size

JOBS = [
    # (fname, url, selector, clip_height)
    ('s2-glm-flash-ox-alpha.png', 'https://www.scmp.com/tech/big-tech/article/3365433/zhipu-ai-shares-jump-viral-ox-alpha-model-revealed-glm-53-flash-chinese-chips', 'body', 880),
    ('s4-instinct-raise.png', 'https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/', 'article', 950),
    ('s5b-openai-agi-time.png', 'https://the-decoder.com/sam-altman-says-openai-will-have-agi-by-the-end-of-2026-if-you-accept-his-definition/', 'body', 850),
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, args=['--no-sandbox'], executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': 1280, 'height': 1000})
        for fname, url, sel, ch in JOBS:
            try:
                await pg.goto(url, wait_until='domcontentloaded', timeout=45000)
                await pg.wait_for_timeout(2000)
                dismissed = await try_consent(pg)
                await pg.wait_for_timeout(1500)
                sz = await clip(pg, sel, fname, ch)
                print(fname, 'consent=', dismissed, 'size=', sz)
            except Exception as e:
                print(fname, 'FAIL', str(e)[:160])
        await b.close()

asyncio.run(main())
