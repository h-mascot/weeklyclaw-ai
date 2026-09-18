#!/usr/bin/env python3
"""Render authentic Instinct tweets (fetched via bird) as a 1280x850 collage card."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 850
BG = (21, 24, 28)
CARD = (28, 32, 38)
TXT = (233, 236, 239)
SUB = (140, 148, 158)
ACC = (42, 126, 107)

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f_name = ImageFont.truetype(FB, 26)
f_handle = ImageFont.truetype(F, 22)
f_body = ImageFont.truetype(F, 24)
f_meta = ImageFont.truetype(F, 20)

tweets = [
    {"name": "Evan Kirstel", "handle": "@EvanKirstel", "text": "Instinct, the AI app that went viral this summer, raised $350M at a $2.5B valuation. Consumer AI valuations are getting priced like the winner is already picked. Retention numbers would be nice before the next round.", "meta": "2:28 PM · Aug 28, 2026 · 2K views"},
    {"name": "Gen AI Spotlight", "handle": "@GenAISpotlight", "text": "Viral Assistant Startup Instinct Hits $2.5B Valuation on $250M Series B — one-year-old consumer AI assistant founded by 23-year-old Noah Shinn. Round co-led by Index Ventures and Benchmark, total raised $350M.", "meta": "1:05 PM · Aug 28, 2026"},
    {"name": "Vladimir Budejicky", "handle": "@budejicky", "text": "Viral AI startup Instinct has raised $350M at a $2.5B valuation, via TechCrunch.", "meta": "12:42 PM · Aug 28, 2026"},
]

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# X-style header strip
d.rectangle([0, 0, W, 70], fill=(25, 28, 33))
d.text((40, 22), "Posts about Instinct's raise — X, Aug 28 2026", font=f_name, fill=TXT)

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

y = 100
for t in tweets:
    ch = 30
    lines = wrap(t["text"], f_body, W - 120 - 20)
    cardh = 70 + len(lines) * 32 + 40
    d.rounded_rectangle([30, y, W - 30, y + cardh], 14, fill=CARD)
    # avatar circle
    d.ellipse([55, y + 20, 100, y + 65], fill=(50, 56, 64))
    d.text((70, y + 33), t["name"][0], font=f_name, fill=(200, 205, 210))
    d.text((115, y + 18), t["name"], font=f_name, fill=TXT)
    d.text((115 + d.textlength(t["name"], font=f_name) + 12, y + 22), t["handle"], font=f_handle, fill=SUB)
    ty = y + 62
    for ln in lines:
        d.text((55, ty), ln, font=f_body, fill=TXT); ty += 32
    d.text((55, ty + 6), t["meta"], font=f_meta, fill=SUB)
    y += cardh + 18

img.save("/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/assets/images/artifacts/s-instinct-collage.png")
print("collage saved", img.size)
