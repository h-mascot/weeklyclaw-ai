"""Build Episode 25 deck by cloning the canonical Episode 23 authority deck
(style block, SVG <symbol>, slide chrome, script) verbatim and inserting the
Episode 25 content slides. No invented CSS, no invented SVG, no invented
logo. Per references/prior-episode-template-authority.md.
"""
import os
import re

WORKSPACE = '/home/henrymascot/weeklyclaw/episodes/25/showprep'
AUTHORITY = '/home/henrymascot/weeklyclaw/episodes/23/deck.html'
CONTENT = os.path.join(WORKSPACE, 'revs/_slides_content.html')
OUT = os.path.join(WORKSPACE, 'revs/deck.rev1.html')

with open(AUTHORITY) as f:
    authority = f.read()
with open(CONTENT) as f:
    content = f.read()

# Extract blocks from authority deck (verbatim, no edits)
style_match = re.search(r'<style>(.*?)</style>', authority, re.DOTALL)
svg_match = re.search(r'(<svg width="0" height="0"[^>]*>\s*<defs>.*?</defs>\s*</svg>)', authority, re.DOTALL)
script_match = re.search(r'<script>(.*?)</script>', authority, re.DOTALL)

assert style_match, 'no <style> block in authority deck'
assert svg_match, 'no <symbol> SVG in authority deck'
assert script_match, 'no <script> block in authority deck'

style = style_match.group(1)
svg_defs = svg_match.group(1)
script = script_match.group(1)

# Count slides in content
slide_count = len(re.findall(r'<div class="slide"', content))
slide_ids = re.findall(r'id="(s-[^"]+)"', content)
print(f"Content slides: {slide_count} | IDs: {slide_ids}")

# Update slideTotal in script (replace the literal '18' that Episode 23 used)
# Actually, the script computes total dynamically from querySelectorAll, so no literal patch needed.
# But the placeholder slideTotalEl in HTML chrome is set by script, not literal. Safe.

# Extract chrome: progress bar, counter, nav dots, kb-hint, slide-container wrapper
# We do NOT include any <div class="slide ..."> from authority — only chrome blocks.
chrome_pattern = re.compile(
    r'(<div class="progress-bar"[^>]*></div>\s*'
    r'<div class="slide-counter">.*?</div>\s*'
    r'<div class="nav-dots"[^>]*></div>\s*'
    r'<div class="kb-hint">.*?</div>\s*'
    r'<div class="slide-container">\s*)',
    re.DOTALL,
)
chrome_m = chrome_pattern.search(authority)
assert chrome_m, 'could not find chrome blocks in authority deck'
chrome = chrome_m.group(1)

# Assemble the deck
deck = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Weekly Claw #25 &mdash; August 14, 2026</title>
<style>{style}</style>
</head>
<body>
{svg_defs}

{chrome}
{content}
</div>
<script>{script}</script>
</body>
</html>
"""

# Replace the title-block episode number in body (slide-brand svg paths untouched).
# The content slides themselves carry "Weekly Claw #25" branding inline.

with open(OUT, 'w') as f:
    f.write(deck)

print(f"Wrote {OUT} | bytes={len(deck)}")
slide_ids_out = sorted(set(re.findall(r'id="(s-[^"]+)"', deck)))
print(f"Slide IDs in output: {slide_ids_out}")
print(f"weeklyclaw-logo symbol present: {'#weeklyclaw-logo' in deck}")
print(f"claw-mark string absent (should be False): {'claw-mark' in deck}")