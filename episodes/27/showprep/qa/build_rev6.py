#!/usr/bin/env python3
"""Ep27 rev6: 'What Happened This Week' becomes a 2x3 / 2x2 story GRID.
Henry (Telegram 2026-08-28): 'i dont want us to have one story per slide.. we
should have 4-6 / 2 rows, 3 cols or something. nvidia thumb: just the co logos.
glm remove news article. dont put 2 images — merge into a collage.'
Five single/cluster seg slides → two grid slides (6 stories + 3 stories).
"""
import re
from pathlib import Path

ROOT = Path("/home/henrymascot/weeklyclaw/episodes/27/showprep")
deck = (ROOT / "revs/deck.rev5.html").read_text()

def slide_block(sid):
    m = re.search(rf'<div class="slide" id="{sid}">.*?\n</div>\n\n\n?', deck, re.S)
    assert m, f"slide not found: {sid}"
    return m.group(0)

# remove the five old seg slides
for sid in ["s-seg-nvidia-hf", "s-seg-models-flash", "s-seg-openai-cluster",
            "s-seg-instinct-raise", "s-seg-robot-cluster"]:
    deck = deck.replace(slide_block(sid), "")
assert "s-seg-nvidia-hf" not in deck

GRID_CSS = """
<style>
.story-grid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:18px;flex:1;min-height:0;margin-top:16px;}
.story-grid.cols-2{grid-template-columns:repeat(2,1fr);}
.story-card{display:flex;flex-direction:column;background:rgba(255,255,255,.03);border:1.5px solid var(--border-subtle);border-radius:16px;overflow:hidden;min-height:0;transition:border-color .2s;}
.story-card:hover{border-color:var(--accent);}
.story-card .thumb{height:150px;min-height:110px;overflow:hidden;position:relative;background:#0d1117;}
.story-card a.thumb{position:relative;}
.story-card .thumb img{width:100%;height:100%;object-fit:cover;object-position:top;}
.story-card .thumb .glyph{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:3.2rem;font-weight:800;}
.story-card .meta{padding:12px 16px 14px;display:flex;flex-direction:column;gap:4px;min-height:0;}
.story-card .meta h3{font-size:1.06rem;line-height:1.25;margin:0;color:var(--text);}
.story-card .meta p{font-size:.82rem;line-height:1.35;margin:0;color:var(--muted);}
.story-card .meta a{font-family:var(--mono);font-size:.72rem;color:var(--accent);text-decoration:none;margin-top:2px;}
</style>
"""

# insert grid css before the closing </head> (or before first slide-container style block end)
assert "</head>" in deck
deck = deck.replace("</head>", GRID_CSS + "</head>", 1)

def grid_slide(sid, tag_label, h2_title, h2_grad, subtitle, cards):
    cells = []
    for c in cards:
        if c.get("img"):
            media = f'<img src="{c["img"]}" alt="{c.get("alt","")}">'
        else:
            media = f'<div class="glyph" style="color:{c.get("color","#8b949e")};">{c.get("glyph","")}</div>'
        link = f'<a href="{c["url"]}" target="_blank" rel="noopener">{c["label"]}</a>' if c.get("url") else ""
        cells.append(f'''      <div class="story-card">
        <a class="thumb" href="{c.get('url','#')}" target="_blank" rel="noopener" style="display:block;height:100%;">{media}</a>
        <div class="meta"><h3>{c["title"]}</h3><p>{c["sub"]}</p>{link}</div>
      </div>''')
    return f'''<div class="slide" id="{sid}">
  <div class="slide-brand"><svg><use href="#weeklyclaw-logo"/></svg> Weekly Claw #27</div><div class="slide-tag">{tag_label}</div>
  <div class="glow-orb orb-green" style="width:380px;height:380px;top:-100px;right:-90px;"></div>
  <div class="content">
    <div>
      <div class="part-label">What happened this week &middot; part {sid.endswith('a') and '1' or '2'}</div>
      <h2>{h2_title} <span class="gradient-text">{h2_grad}</span></h2>
      <div class="gradient-line"></div>
      <p class="subtitle mt-1" style="max-width:1000px;">{subtitle}</p>
    </div>
    <div class="story-grid">
{chr(10).join(cells)}
    </div>
  </div>
</div>

'''

CARDS_A = [
    dict(img="assets/images/artifacts/s-nvidia-hf-cologo.png", alt="Nvidia acquires Hugging Face",
         title="Nvidia is buying Hugging Face.", sub="$12.9B reported, unconfirmed. The GPU vendor would own the model commons.",
         url="https://www.cnbc.com/2026/08/27/nvidia-hugging-face-acquisition.html", label="cnbc.com"),
    dict(img="assets/images/artifacts/s-glm53-full-results.jpg", alt="GLM-5.3 full benchmark results",
         title="Ox Alpha is GLM-5.3-Flash.", sub="Serving ~100T tokens/day on ~100K Chinese GPUs (Zhipu-reported). Benchmarks over press.",
         url="https://x.com/ZixuanLi_/status/2088135213930905623", label="benchmarks (x.com)"),
    dict(img="assets/images/artifacts/s-jalapeno-semi.png", alt="OpenAI Jalapeno vs Nvidia Blackwell analysis",
         title="OpenAI ships Jalape&ntilde;o.", sub="First custom inference chip; vendor-reported wins vs Blackwell on perf/watt.",
         url="https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia", label="semianalysis"),
    dict(img="assets/images/artifacts/s-openai-time-cover.png", alt="TIME cover story on OpenAI reboot",
         title="OpenAI says AGI by December.", sub="Altman in TIME: internal system he'd call AGI by end of 2026 — his definition.",
         url="https://time.com/article/2026/08/26/openai-sam-altman-interview/", label="time.com"),
    dict(img="assets/images/artifacts/s-instinct-collage.png", alt="Posts about Instinct raise",
         title="Instinct raised at $2.5B.", sub="$250M new at a $2.5B valuation, four months old. Agent capital is hot.",
         url="https://techcrunch.com/2026/08/27/instinct-ai-valuation-2-5b/", label="techcrunch"),
    dict(img="assets/images/artifacts/s5-figure-pipeline.png", alt="Figure Index data pipeline",
         title="Figure launches Index.", sub="16M videos, 44K creators, $15M paid out. Robots are a data business.",
         url="https://www.figure.ai/", label="figure.ai"),
]

CARDS_B = [
    dict(img="assets/images/artifacts/s2-qwen-architecture.png", alt="Qwen Flash-Next architecture",
         title="Qwen opens Flash-Next.", sub="Qwen4-preview architecture ungated: 125B params, 6B active, 250K context.",
         url="https://qwen.ai/blog?id=qwen3.8-flash-next", label="qwen.ai"),
    dict(img="assets/images/artifacts/s3-headlong-loop.svg", alt="Headlong always-on loop",
         title="Laude ships Headlong.", sub="The agent that never sleeps — fixed a recall bug in 48 min, no human in the loop.",
         url="https://www.laude.org/updates/headlong-a-microharness", label="laude.org"),
    dict(img="assets/images/artifacts/s4-portable-computer.png", alt="Perplexity Portable Computer",
         title="Perplexity puts the stack on the desk.", sub="Portable Computer runs model, harness, sandbox locally on DGX Spark.",
         url="https://www.perplexity.ai/", label="perplexity.ai"),
]

grid_a = grid_slide("s-seg-grid-a", "WHAT HAPPENED THIS WEEK", "Consolidation, sovereign compute,", "agent capital.",
                    "Six moves that defined the week. Each card links to the primary source.", CARDS_A)
grid_b = grid_slide("s-seg-grid-b", "WHAT HAPPENED THIS WEEK", "The operating layer", "ships.",
                    "Open weights, always-on agents, local-first stacks — the deployment story.", CARDS_B)

# insert grids before the Heritage sponsor slide
anchor = '<div class="slide" id="s-sponsor-heritage">'
deck = deck.replace(anchor, grid_a + grid_b + anchor, 1)
for canary in ['id="s-seg-grid-a"', 'id="s-seg-grid-b"', 's-nvidia-hf-cologo.png', 'story-grid']:
    assert canary in deck, canary
# slideTotal 13 -> 10
deck = deck.replace('<span id="slideTotal">13</span>', '<span id="slideTotal">10</span>')
assert '<span id="slideTotal">10</span>' in deck
# nav chrome intact
for chrome in ['id="navDots"', 'class="slide-container"']:
    assert chrome in deck, chrome

out = ROOT / "revs/deck.rev6.html"
out.write_text(deck)
print(f"wrote {out} ({len(deck)} bytes)")
ids = re.findall(r'<div class="slide" id="(s-[a-z-]+)"', deck)
print(len(ids), ids)
