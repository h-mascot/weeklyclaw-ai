"""Render Episode 25 deck slides to PNG screenshots at 1600x900 for visual QA.
Uses Playwright to drive the deck's own arrow-key navigation.
"""
import os
import re
from playwright.sync_api import sync_playwright

WORKSPACE = '/home/henrymascot/weeklyclaw/episodes/25/showprep'
DECK = os.path.join(WORKSPACE, 'revs/deck.rev1.html')
OUT_DIR = os.path.join(WORKSPACE, 'qa/render-1600x900')
os.makedirs(OUT_DIR, exist_ok=True)

# Clean prior renders
for f in os.listdir(OUT_DIR):
    if f.endswith('.png'):
        os.remove(os.path.join(OUT_DIR, f))

with open(DECK) as f:
    html = f.read()
slide_ids = re.findall(r'<div class="slide[^"]*" id="(s-[^"]+)"', html)
print(f"Rendering {len(slide_ids)} slides at 1600x900 -> {OUT_DIR}")

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True, args=['--no-sandbox'])
    context = browser.new_context(viewport={'width': 1600, 'height': 900})
    page = context.new_page()
    page.goto('file://' + DECK, wait_until='networkidle')
    page.wait_for_timeout(800)

    for i, sid in enumerate(slide_ids):
        # Always start at first slide then walk forward — but using the
        # script's navigation, we can just press ArrowRight i times from index 0.
        # But we cannot "reset" mid-loop. So we use location.hash, which the
        # script honours on initial load, and for subsequent slides we click
        # the corresponding nav-dot via JS.
        # Simplest robust approach: navigate from current by clicking nav dots.
        page.evaluate(f"""
            const target = document.getElementById('{sid}');
            const dots = document.querySelectorAll('.nav-dot');
            const slides = document.querySelectorAll('.slide');
            const idx = Array.prototype.indexOf.call(slides, target);
            dots[idx].click();
        """)
        page.wait_for_timeout(200)
        out_png = os.path.join(OUT_DIR, f'{i+1:02d}-{sid}.png')
        page.screenshot(path=out_png, full_page=False)
        print(f"  {i+1:02d} {sid} -> {out_png}")
    browser.close()

# Validate non-empty
print("--- PNG inventory ---")
for f in sorted(os.listdir(OUT_DIR)):
    if f.endswith('.png'):
        size = os.path.getsize(os.path.join(OUT_DIR, f))
        print(f"  {f}: {size} bytes")
        assert size > 5000, f"PNG too small: {f}"
print("=== VISUAL RENDER COMPLETE ===")