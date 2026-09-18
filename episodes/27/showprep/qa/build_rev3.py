#!/usr/bin/env python3
"""Ep27 rev3: 9 news segments, compressed. Surgical edit of deck.rev2.html."""
import re, pathlib

REV = pathlib.Path('/home/henrymascot/weeklyclaw/episodes/27/showprep/revs')
src = (REV / 'deck.rev2.html').read_text()

def swap(old, new):
    global src
    assert old in src, 'MISSING: ' + old[:60]
    src = src.replace(old, new)

# 1. Title slide
swap('''      The agent owns the loop.<br/>OpenAI stacked chip, model, harness and business seat into one vertically aligned machine; Qwen opened a Qwen4-preview architecture the same day; Headlong shipped the harness and the warning label together; Perplexity put the whole agent stack on the desk and made cloud calls an opt-in; Figure turned the robot race into a data race.''',
     '''      The agent owns the loop.<br/>Nvidia moved to buy the open-weights commons; Zhipu unmasked Ox Alpha as GLM-5.3-Flash serving 100T tokens a day on Chinese chips; OpenAI stacked chip, model, seat and said AGI by December; a four-month-old assistant raised at $2.5B. Nine stories, less time on each, more of the week.''')
swap('~38 min &middot; five segments &middot; built to be clipped',
     '~40 min &middot; nine stories &middot; faster cuts &middot; built to be clipped')

# 2. Cold open
swap('The models barely moved. The layer beneath them did &mdash; chip, model, harness, business seat, deployment surface, and the data feeding physical autonomy. The moat is no longer the model. It is the operating layer.',
     'Nine stories, one frame: the consolidation race. Chips buying commons, stealth models on domestic silicon, four-month-old agents at $2.5B, AGI dates with footnotes. The moat is no longer the model. It is the operating layer.')
swap('<div class="arc-label">Stacking</div>', '<div class="arc-label">Consolidation</div>')
swap('<div class="arc-label">Autonomy</div>', '<div class="arc-label">Sovereign compute</div>')
swap('<div class="arc-label">Locality</div>', '<div class="arc-label">Agent capital</div>')
swap('<div class="arc-label">Physical data</div>', '<div class="arc-label">AGI claims</div>')
swap('<div class="arc-label">Governance</div>', '<div class="arc-label">Operating layer</div>')
swap('''      <div class="hook"><span class="hook-num gradient-text">&#9881;</span><span class="hook-text">OpenAI stacked <span class="orange">chip, model, harness, business seat</span>; Premium removes the five-hour cap and sells five times the usage.</span></div>
      <div class="hook"><span class="hook-num gradient-text">&#9889;</span><span class="hook-text">Qwen opened the <span class="orange">Qwen4-preview architecture</span> ungated; 125B main, 51B n-gram embeddings, 6B active per token.</span></div>
      <div class="hook"><span class="hook-num gradient-text">&#128176;</span><span class="hook-text">Headlong shipped the harness and the <span class="orange">warning label</span>; $1&ndash;$2/hour background cost, three incidents where the agent stopped its own service.</span></div>''',
     '''      <div class="hook"><span class="hook-num gradient-text">&#127793;</span><span class="hook-text">Nvidia is buying <span class="orange">Hugging Face for $12.9B</span>; the GPU vendor would own the open-weights commons.</span></div>
      <div class="hook"><span class="hook-num gradient-text">&#128052;</span><span class="hook-text">Ox Alpha was <span class="orange">GLM-5.3-Flash</span>: 100 trillion tokens a day served on 100% Chinese chips.</span></div>
      <div class="hook"><span class="hook-num gradient-text">&#128176;</span><span class="hook-text">Altman says OpenAI has <span class="orange">AGI internally by year-end</span>; Mark Chen calls it 80% of the way there.</span></div>''')

(REV / 'deck.rev3.html').write_text(src)
print('deck.rev3.html written:', len(src), 'bytes')
print('slides:', re.findall(r'id="(s-[^"]+)"', src))
