#!/usr/bin/env python3
"""Ep27 rev3 part 2: insert 4 new segment slides + compress subtitles + sources."""

import pathlib

REV = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/revs')
src = (REV / 'deck.rev3.html').read_text()

def swap(old, new):
    global src
    assert old in src, 'MISSING: ' + old[:70]
    src = src.replace(old, new, 1)

def seg(sid, orb, orbpos, title_grad, subtitle, link_label, link_url, img, img_alt, img_link):
    return f'''<div class="slide" id="{sid}">
  <div class="slide-brand"><svg><use href="#weeklyclaw-logo"/></svg> Weekly Claw #27</div><div class="slide-tag">WHAT HAPPENED THIS WEEK</div>
  <div class="glow-orb {orb}" style="width:380px;height:380px;{orbpos}"></div>
  <div class="content" style="display:flex;flex-direction:row;gap:36px;align-items:center;">
    <div style="flex:1.1;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;">
      <h2 class="text-center">{title_grad}</h2>
      <div class="gradient-line"></div>
      <p class="subtitle text-center mt-1" style="max-width:780px;">{subtitle}</p>
      <a href="{link_url}" target="_blank" rel="noopener" style="margin-top:18px;display:inline-flex;align-items:center;gap:8px;padding:10px 24px;border:2px solid var(--accent);border-radius:999px;font-family:var(--mono);font-size:.95rem;color:var(--accent);text-decoration:none;background:rgba(255,255,255,.03);">&#9654; LIVE &middot; {link_label}</a>
    </div>
    <div style="flex:1.3;height:100%;display:flex;align-items:center;justify-content:center;">
      <a href="{img_link}" target="_blank" rel="noopener"><img src="{img}" alt="{img_alt}" style="width:100%;max-height:640px;object-fit:cover;object-position:top;border-radius:14px;border:3px solid var(--border-subtle);box-shadow:0 20px 60px rgba(0,0,0,.35);"></a>
    </div>
  </div>
</div>

'''

CNBC = 'https://www.cnbc.com/2026/08/27/nvidia-hugging-face-acquisition.html'
SCMP = 'https://www.scmp.com/tech/big-tech/article/3365433/zhipu-ai-shares-jump-viral-ox-alpha-model-revealed-glm-53-flash-chinese-chips'
WCCF = 'https://wccftech.com/zhipu-z-ai-unmasks-the-mystery-ox-alpha-model-as-glm-5-3-flash-revealing-that-it-was-run-entirely-on-chinese-gpus-while-serving-100-trillion-tokens-day/'
TC = 'https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/'
DEC = 'https://the-decoder.com/sam-altman-says-openai-will-have-agi-by-the-end-of-2026-if-you-accept-his-definition/'
FEL = 'https://felloai.com/openai-agi-2026/'

nvidia_hf = seg('s-seg-nvidia-hf', 'orb-green', 'top:-100px;right:-90px;',
    'Nvidia is buying <span class="gradient-text">Hugging Face.</span>',
    '$12.9B reported &middot; deal not confirmed by either side &middot; the GPU vendor would own the model commons',
    'CNBC report (cnbc.com)', CNBC,
    'assets/images/artifacts/s5-nvidia-hf-deal.png',
    'Nvidia to acquire Hugging Face for 12.9 billion dollars, report', CNBC)

glm_flash = seg('s-seg-glm-flash', 'orb-red', 'bottom:-100px;left:-90px;',
    'Ox Alpha was GLM-5.3-Flash <span class="gradient-text">on Chinese chips.</span>',
    '100T tokens/day &middot; ~100,000 domestic GPUs &middot; $0.15 in / $0.50 out per M',
    'SCMP reveal coverage (scmp.com)', SCMP,
    'assets/images/artifacts/s2-glm-flash-ox-alpha.png',
    'Zhipu AI shares jump as viral Ox Alpha model revealed as GLM-5.3-Flash on Chinese chips', WCCF)

instinct = seg('s-seg-instinct-raise', 'orb-purple', 'top:-100px;left:-90px;',
    'Instinct raised at <span class="gradient-text">$2.5 billion.</span>',
    'Four months old &middot; $250M round co-led by Index and Benchmark &middot; up 5x in weeks',
    'TechCrunch round coverage (techcrunch.com)', TC,
    'assets/images/artifacts/s4-instinct-raise.png',
    'Instinct AI assistant valuation rockets to 2.5 billion in weeks', TC)

agi = seg('s-seg-openai-agi', 'orb-orange', 'bottom:-100px;right:-90px;',
    'OpenAI says it will have <span class="gradient-text">AGI by December.</span>',
    'Altman in TIME: internal AGI by end of 2026 &middot; Mark Chen: &ldquo;80% of the way&rdquo; &middot; definition is the footnote',
    'The Decoder on the TIME interview (the-decoder.com)', DEC,
    'assets/images/artifacts/s5b-openai-agi-time.png',
    'OpenAI AGI in 2026: what Altman actually promised', FEL)

# Insert Nvidia-HF + GLM before first sponsor slide
anchor = '<div class="slide" id="s-sponsor-heritage">'
swap(anchor, nvidia_hf + glm_flash + anchor)

# Insert Instinct + AGI after the openai-stack slide, before qwen slide
anchor2 = '<div class="slide" id="s-seg-qwen-flash-next">'
swap(anchor2, instinct + agi + anchor2)

# Compress existing subtitles
swap('Jalapeño first inference results &middot; Premium at $100/user/yr, 5x usage, no five-hour cap',
     'Jalape&ntilde;o first results &middot; Premium: 5x usage, no five-hour cap')
swap('125B main &middot; 51B n-gram embeddings &middot; 6B active &middot; 262K context, YaRN to 1M',
     '125B + 51B n-gram &middot; 6B active &middot; 262K context, YaRN to 1M')
swap('Sub-10K-line Bash harness &middot; continuous self-guided loop &middot; $1&ndash;$2/hour background cost',
     'Bash microharness &middot; always-on loop &middot; $1&ndash;$2/hour to run')
swap('Model, harness, sandbox, tools all local on DGX Spark &middot; cloud calls need approval',
     'Whole agent stack local on DGX Spark &middot; cloud calls need approval')
swap('16M uploaded videos &middot; 44K weekly active creators &middot; $15M paid out &middot; $1B+ planned for data',
     '16M videos &middot; 44K creators &middot; $15M paid &middot; $1B+ planned for data')

# Sources slide: S1 nvidia-hf block, relabel old tags
swap('<span class="tag tag-red">S1 &middot; OPENAI STACK</span>',
     '<span class="tag tag-green">S1 &middot; NVIDIA &times; HUGGING FACE</span>\n        <div class="src-links" style="justify-content:flex-start;margin-top:8px;">\n          <a href="' + CNBC + '" target="_blank" rel="noopener">cnbc.com: Nvidia to buy Hugging Face for $12.9B</a>\n          <a href="https://arstechnica.com/ai/2026/08/report-nvidia-to-acquire-ai-model-repository-hugging-face-for-13-billion/" target="_blank" rel="noopener">arstechnica.com: Nvidia to acquire Hugging Face</a>\n        </div>\n        <span class="tag tag-red mt-2">S2 &middot; OPENAI STACK</span>')
swap('<span class="tag tag-blue mt-2">S2 &middot; QWEN FLASH-NEXT</span>',
     '<span class="tag tag-blue mt-2">S3 &middot; QWEN FLASH-NEXT</span>')
swap('<span class="tag tag-green mt-2">S3 &middot; HEADLONG</span>',
     '<span class="tag tag-green mt-2">S4 &middot; HEADLONG</span>')
swap('<span class="tag tag-yellow">S4 &middot; PERPLEXITY PORTABLE COMPUTER</span>',
     '<span class="tag tag-yellow">S5 &middot; PERPLEXITY PORTABLE COMPUTER</span>')
swap('<span class="tag tag-purple mt-2">S5 &middot; FIGURE INDEX</span>',
     '<span class="tag tag-purple mt-2">S6 &middot; FIGURE INDEX</span>\n        <span class="tag tag-red mt-2">S7 &middot; GLM-5.3-FLASH / OX ALPHA</span>\n        <div class="src-links" style="justify-content:flex-start;margin-top:8px;">\n          <a href="' + SCMP + '" target="_blank" rel="noopener">scmp.com: Ox Alpha revealed as GLM-5.3-Flash</a>\n          <a href="' + WCCF + '" target="_blank" rel="noopener">wccftech.com: GLM-5.3-Flash on Chinese GPUs</a>\n        </div>\n        <span class="tag tag-blue mt-2">S8 &middot; INSTINCT RAISE</span>\n        <div class="src-links" style="justify-content:flex-start;margin-top:8px;">\n          <a href="' + TC + '" target="_blank" rel="noopener">techcrunch.com: Instinct raises at $2.5B valuation</a>\n        </div>\n        <span class="tag tag-purple mt-2">S9 &middot; OPENAI AGI CLAIM</span>\n        <div class="src-links" style="justify-content:flex-start;margin-top:8px;">\n          <a href="' + DEC + '" target="_blank" rel="noopener">the-decoder.com: Altman AGI by end of 2026</a>\n          <a href="' + FEL + '" target="_blank" rel="noopener">felloai.com: what Altman actually promised</a>\n        </div>')

# Sources note + verified date
swap('Vendor-reported claims are labeled on each slide (OpenAI work-per-watt normalized by published TDP; Qwen benchmark vendor-run; Perplexity 82.6% vs 74.0% self-authored; Figure scale figures company-reported). The hosted QwenCloud API is &ldquo;coming soon.&rdquo;',
     'Vendor-reported claims are labeled on each slide (OpenAI work-per-watt by published TDP; Qwen benchmark vendor-run; Perplexity 82.6% vs 74.0% self-authored; Figure scale company-reported; Nvidia&times;HF price press-reported, unconfirmed; GLM-5.3-Flash scale Zhipu-reported; AGI date is Altman&rsquo;s own definition, not independently validated). The hosted QwenCloud API is &ldquo;coming soon.&rdquo;')
swap('Every claim, one click &middot; verified 2026-08-27', 'Every claim, one click &middot; verified 2026-08-28')

(REV / 'deck.rev3.html').write_text(src)
import re
print('deck.rev3.html:', len(src), 'bytes')
print('slides:', re.findall(r'id="(s-[^"]+)"', src))
