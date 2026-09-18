#!/usr/bin/env python3
"""Nvidia x HF co-logo card v2 — cropped wordmark strip + HF face, no white box."""
from PIL import Image, ImageDraw, ImageFont

# nv2.svg renders as white square with wordmark strip; crop the strip
nv_full = Image.open("/tmp/nv.png").convert("RGBA")  # 440x440 render of nv2
w, h = nv_full.size
# strip is the #c4d64d band in the middle ~ y 38%-60% of viewBox 192.756 (72.9-119.8)
box = (0, int(h * 0.375), w, int(h * 0.625))
nv_strip = nv_full.crop(box)
# upscale strip
nv_strip = nv_strip.resize((760, int(nv_strip.height * 760 / nv_strip.width)))

hf = Image.open("/tmp/hf.png").convert("RGBA").resize((420, 420))

W, H = 1280, 720
bg = Image.new("RGB", (W, H), "#0d1117")
d = ImageDraw.Draw(bg)
d.rectangle([0, 0, W, 6], fill="#76b900")
d.rectangle([0, H - 6, W, H], fill="#ffd21e")

# center-left: nvidia strip; right: HF face
bg.paste(nv_strip, (110, 310), nv_strip)
bg.paste(hf, (760, 150), hf)

d.line([(660, 200), (660, 540)], fill="#30363d", width=3)
try:
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
except Exception:
    f = ImageFont.load_default()
d.text((588, 350), "acquires", font=f, fill="#8b949e")

out = "/home/henrymascot/weeklyclaw/episodes/27/showprep/assets/images/artifacts/s-nvidia-hf-cologo.png"
bg.save(out)
print("saved", out)
