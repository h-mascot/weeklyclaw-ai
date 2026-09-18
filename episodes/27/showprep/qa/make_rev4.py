#!/usr/bin/env python3
"""Derive rev4 from rev3: cluster 9 news segments into 4, sponsors start+end only,
swap artifacts to benchmarks/cover/collage, add Signal video (Dwarkesh/Dylan)."""
import re, sys

SRC = '/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/deck.rev3.html'
DST = '/home/henrymascot/weeklyclaw/episodes/27/showprep/revs/deck.rev4.html'

src = open(SRC).read()

# --- extract slide blocks ---
def slides(t):
    out = {}
    for m in re.finditer(r'<div class="slide[^"]*" id="(s-[^"]+)">(.*?)\n</div>\n\n', t, re.S):
        out[m.group(1)] = m.group(0)
    return out

S = slides(src)
need = ['s-title','s-cold-open','s-seg-nvidia-hf','s-seg-glm-flash','s-sponsor-heritage','s-seg-openai-stack',
        's-seg-instinct-raise','s-seg-openai-agi','s-seg-qwen-flash-next','s-seg-headlong','s-seg-portable-computer',
        's-seg-robot-data','s-signal-outside','s-hot-take','s-sponsor-herald','s-watch','s-sources']
missing = [k for k in need if k not in S]
if missing: sys.exit(f'missing slides: {missing}')

A = 'assets/images/artifacts/'

def seg(sid, tag, title, sub, img, imgalt, link, linklabel, extra_img=None, extra_alt=None):
    two = ''
    if extra_img:
        two = f'''
    <div class="artifact-duo">
      <figure class="artifact"><img src="{img}" alt="{imgalt}"><figcaption>{imgalt}</figcaption></figure>
      <figure class="artifact"><img src="{extra_img}" alt="{extra_alt}"><figcaption>{extra_alt}</figcaption></figure>
    </div>'''
    else:
        two = f'''
    <figure class="artifact"><img src="{img}" alt="{imgalt}"><figcaption>{imgalt}</figcaption></figure>'''
    return f'''<div class="slide" id="{sid}">
  <div class="content">
    <div class="slide-tag">WHAT HAPPENED THIS WEEK</div>
    <h2>{title}</h2>
    <p class="slide-sub">{sub}</p>
    <a class="live-link" href="{link}" target="_blank">&#9654; {linklabel}</a>
{two}
  </div>
</div>

'''

# Cluster 1: Nvidia buys Hugging Face (deal — receipt visual already good)
seg1 = seg('s-seg-nvidia-hf', '', 'Nvidia is buying Hugging Face.',
    'Reported $12.9B — unconfirmed. Consolidation of the open-source layer.',
    f'{A}s5-nvidia-hf-deal.png', 'Nvidia–Hugging Face deal coverage',
    'https://www.cnbc.com/2026/08/27/nvidia-hugging-face.html', 'CNBC coverage')

# Cluster 2: GLM-5.3-Flash + Qwen Flash-Next — benchmarks, Henry's own chart
seg2 = seg('s-seg-models-flash', '', 'GLM-5.3-Flash and Qwen Flash-Next land the flash-class upgrades.',
    'Sovereign compute meets open weights — benchmarks over press.',
    f'{A}s-glm53-full-results.jpg', 'GLM-5.3 full benchmark results',
    'https://x.com/ZixuanLi_/status/2088135213930905623', 'GLM-5.3 benchmarks on X',
    extra_img=f'{A}s2-glm-flash-ox-alpha.png', extra_alt='Zhipu shares jump on Ox Alpha reveal')

# Cluster 3: OpenAI — Jalapeño + AGI claim, TIME cover
seg3 = seg('s-seg-openai-cluster', '', 'OpenAI ships Jalapeño and says AGI by December.',
    'First custom chip beats Blackwell on perf/watt; Altman tells TIME an internal AGI lands this year.',
    f'{A}s-jalapeno-semi.png', 'Jalapeño vs Blackwell benchmark analysis',
    'https://time.com/article/2026/08/26/openai-sam-altman-interview/', 'TIME: Inside OpenAI\u2019s Reboot',
    extra_img=f'{A}s-openai-time-cover.png', extra_alt='TIME cover story — Sam Altman')

# Cluster 4: Instinct raise — tweet collage
seg4 = seg('s-seg-instinct-raise', '', 'Instinct raises at $2.5B in four months.',
    '$250M Series B co-led by Index and Benchmark. The reaction was the story.',
    f'{A}s-instinct-collage.png', 'X reaction collage to the Instinct raise',
    'https://techcrunch.com/2026/08/28/instinct-ai-2-5b-valuation/', 'TechCrunch report')

# Robots cluster: Figure + World Humanoid Robot Games
seg5 = seg('s-seg-robot-cluster', '', 'Figure launches Index while Beijing hosts the robot games.',
    '2,056 robots, 666 teams, 51 events — the robot race is a data race.',
    f'{A}s-robot-games.png', 'World Humanoid Robot Games, Beijing 2026',
    'https://en.wikipedia.org/wiki/World_Humanoid_Robot_Games', 'Robot Games coverage',
    extra_img=f'{A}s5-figure-pipeline.png', extra_alt='Figure Index data pipeline')

# Signal From Outside: Dwarkesh x Dylan Patel
seg6 = f'''<div class="slide" id="s-signal-outside">
  <div class="content">
    <div class="slide-tag">03 / SIGNAL FROM OUTSIDE</div>
    <h2>Two labs will soon control most of the world\u2019s compute.</h2>
    <p class="slide-sub">Dwarkesh x Dylan Patel \u00b7 1:16:53</p>
    <a class="live-link" href="https://youtu.be/aV26V1UvkJw" target="_blank">&#9654; Watch on YouTube</a>
    <figure class="artifact"><img src="{A}s-dwarkesh-dylan.png" alt="Dwarkesh Podcast with Dylan Patel"><figcaption>Dwarkesh Podcast \u2014 Dylan Patel</figcaption></figure>
  </div>
</div>

'''

# --- assemble ---
head = src[:src.find('<div class="slide-container">') + len('<div class="slide-container">')]
tail_match = re.search(r'</div>\n\n<script>.*?</script>', src, re.S)
tail = tail_match.group(0)

order = [S['s-title'], S['s-cold-open'], seg1, seg2, seg3, seg4, seg5,
         S['s-sponsor-heritage'], seg6, S['s-hot-take'], S['s-sponsor-herald'], S['s-watch'], S['s-sources']]

out = head + '\n\n' + '\n'.join(order) + '\n' + tail
out = out.replace('<span id="slideTotal">17</span>', '<span id="slideTotal">13</span>')
open(DST, 'w').write(out)
print('rev4 written', len(out), 'bytes')
ids = re.findall(r'<div class="slide[^"]*" id="(s-[^"]+)"', out)
print('slides:', len(ids), ids)
