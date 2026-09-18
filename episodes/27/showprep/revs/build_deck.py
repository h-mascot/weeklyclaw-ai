#!/usr/bin/env python3
"""Ep 27 deck builder. Clones Ep 26 authority deck verbatim and swaps
slide bodies, title card, and slide count. Run from /home/henrymascot/weeklyclaw/episodes/27/showprep/revs/."""
import sys, re, pathlib, subprocess

ROOT = pathlib.Path("/home/henrymascot/weeklyclaw/episodes/27/showprep")
AUTHORITY = ROOT / "qa" / "authority-deck-ep26.html"
SLIDES = ROOT / "revs" / "_slides_content.rev2.html"
OUT = ROOT / "revs" / "deck.rev2.html"

auth = AUTHORITY.read_text(encoding="utf-8")

# Locate the start of <div class="slide" and the end of <script>.
# Replace everything between those two anchors with the new slides + script.
slide_start = auth.index('<div class="slide')
script_start_marker = "</script>"
script_close_idx = auth.rindex(script_start_marker) + len(script_start_marker)
# script_start_marker is "<\/script>". We want the open <script> tag — find the last <script> tag before that.
script_open = auth.rfind("<script>", 0, script_close_idx - len(script_start_marker))

# Extract head + chrome (everything before slide_start) and trailing HTML (everything after script_close_idx).
head_block = auth[:slide_start]
tail_block = auth[script_close_idx:]  # </script>...</body></html>

# Read new slides + new <script>.
new_body = SLIDES.read_text(encoding="utf-8")
# The new_body ends with </div> + <script>...</script></body></html>.
# We want everything up to (but not including) the closing </div> of slide-container, then our script.
# Our slides file ends with `</div>\n<script>...</script>\n</body>\n</html>`.
# We need to splice head_block + slide_divs + tail_block. The slide_divs end with the closing </div> of slide-container (right before <script>).
script_open_in_new = new_body.index("<script>")
slide_divs = new_body[:script_open_in_new]  # includes the </div> that closes slide-container
# Re-extract the script block from new_body:
m = re.search(r"<script>(.*?)</script>", new_body, re.DOTALL)
assert m, "no <script> in new slides file"
script_block = m.group(0)  # include the <script>...</script>

# Assemble
deck = head_block + slide_divs + script_block + tail_block

# Sanity: must contain weeklyclaw-logo symbol, must NOT contain invented claw-mark
assert 'id="weeklyclaw-logo"' in deck, "weeklyclaw-logo symbol missing"
assert 'id="claw-mark"' not in deck, "invented claw-mark symbol present"

# Update the slide counter to reflect new total (script computes it dynamically; no static edit needed).
# But the <title> should say Ep 27:
deck = deck.replace(
    "<title>Weekly Claw #26 &mdash; August 21, 2026</title>",
    "<title>Weekly Claw #27 &mdash; August 28, 2026</title>",
)

# Update all #26 → #27 references that are decorative (slide brand labels etc.)
deck = deck.replace("Weekly Claw #26", "Weekly Claw #27")
deck = deck.replace("Episode 26 &middot;", "Episode 27 &middot;")

OUT.write_text(deck, encoding="utf-8")
size = OUT.stat().st_size
print(f"WROTE {OUT} size={size}")

# node --check the inline script
script_only = re.search(r"<script>(.*?)</script>", deck, re.DOTALL).group(1)
node_check = subprocess.run(["node", "--check", "-"], input=script_only, capture_output=True, text=True)
if node_check.returncode != 0:
    print("NODE_CHECK_FAIL:", node_check.stderr)
    sys.exit(1)
print("NODE_CHECK_PASS")

# Slide ID count
slide_ids = re.findall(r'<div class="slide[^"]*" id="([^"]+)"', deck)
print(f"SLIDE_COUNT={len(slide_ids)}")
print(f"SLIDE_IDS={slide_ids}")
