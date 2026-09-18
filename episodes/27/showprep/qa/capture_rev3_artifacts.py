#!/usr/bin/env python3
"""Ep27 rev3 artifact capture for 4 new stories (Nvidia-HF, GLM-5.3-Flash, Instinct, OpenAI AGI)."""
import asyncio, pathlib
from playwright.async_api import async_playwright

OUT = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/assets/images/artifacts')

TARGETS = [
    ('s2-glm-flash-ox-alpha.png', 'https://wccftech.com/zhipu-z-ai-unmasks-the-mystery-ox-alpha-model-as-glm-5-3-flash-revealing-that-it-was-run-entirely-on-chinese-gpus-while-serving-100-trillion-tokens-day/', 'body'),
    ('s4-instinct-raise.png', 'https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/', 'article'),
    ('s5b-openai-agi-time.png', 'https://the-decoder.com/sam-altman-says-openai-will-have-agi-by-the-end-of-2026-if-you-accept-his-definition/', 'body'),
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True, args=['--no-sandbox'], executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': 1280, 'height': 1000})
        for fname, url, sel in TARGETS:
            try:
                await pg.goto(url, wait_until='domcontentloaded', timeout=45000)
                await pg.wait_for_timeout(2500)
                try:
                    el = pg.locator(sel).first
                    await el.screenshot(path=str(OUT / fname), timeout=30000)
                except Exception:
                    await pg.screenshot(path=str(OUT / fname), full_page=False)
                sz = (OUT / fname).stat().st_size
                print(fname, 'OK' if sz > 20000 else f'SMALL({sz})')
            except Exception as e:
                print(fname, 'FAIL', str(e)[:160])
        await b.close()

asyncio.run(main())
