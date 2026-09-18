#!/usr/bin/env python3
"""Ep27 rev5: hot-take rebuild — abstract 'deployment layer' take becomes a
concrete two-sided fight (Andy feedback 2026-08-28: 'tool fight lands when the
topics are important… Nvidia buys huggingface - good for open source or bad')."""
import re, sys
from pathlib import Path

ROOT = Path("/home/henrymascot/weeklyclaw/episodes/27/showprep")
deck = (ROOT / "revs/deck.rev4.html").read_text()

# ---- extract the whole s-hot-take slide block and rebuild it ----
m = re.search(r'<div class="slide" id="s-hot-take">.*?\n</div>\n\n\n?(?=<div class="slide" id="s-sponsor-herald">)', deck, re.S)
assert m, "s-hot-take block not found"
old_block = m.group(0)

src_links = re.search(r'(<div class="src-links">.*?</div>)', old_block, re.S)
assert src_links, "src-links not found in hot-take block"

new_block = '''<div class="slide" id="s-hot-take">
  <div class="slide-brand"><svg><use href="#weeklyclaw-logo"/></svg> Weekly Claw #27</div><div class="slide-tag">04 / HOT TAKE &middot; 3 MIN</div>
  <div class="glow-orb orb-red" style="width:480px;height:480px;top:-140px;left:-120px;"></div>
  <div class="content">
    <div class="part-label">Hot take &middot; the fight &middot; two sides, one verdict</div>
    <h2 class="text-center">Nvidia buying Hugging Face is <span class="gradient-text">bad for open source.</span></h2>
    <div class="gradient-line"></div>
    <p class="subtitle text-center mt-1" style="max-width:900px;">The motion. Twelve point nine billion dollars, still unconfirmed, for the hub where the open-weights world ships. Henry argues it is bad for open source. Andy argues it is good. Two minutes each, then the verdict.</p>
    <div class="mt-3 two-col">
      <div class="card">
        <span class="tag tag-red">HENRY &middot; BAD FOR OPEN SOURCE</span>
        <h3 class="mt-1">The commons gets a landlord.</h3>
        <p class="muted">The biggest GPU vendor now owns the hub its own competitors ship on. Every neutral surface &mdash; model hosting, benchmarks, Spaces &mdash; now has an owner with a dog in the fight.</p>
        <ul class="bullet-list mt-2">
          <li><strong>Conflict of interest:</strong> the referee sells jerseys</li>
          <li><strong>Microsoft-GitHub precedent:</strong> openness survives, neutrality does not</li>
          <li><strong>The rent:</strong> terms of service beat licenses when the hub is single</li>
        </ul>
      </div>
      <div class="card card-glow">
        <span class="tag tag-blue">ANDY &middot; GOOD FOR OPEN SOURCE</span>
        <h3 class="mt-1">Validation, not capture.</h3>
        <p class="muted">Nobody pays twelve point nine billion for a charity. Open source just got priced as the strategic layer of AI &mdash; and Nvidia sells GPUs to everyone, so walling the garden shrinks its own market.</p>
        <ul class="bullet-list mt-2">
          <li><strong>Capital:</strong> the commons stops living donation to donation</li>
          <li><strong>Incentive:</strong> locking HF hurts Nvidia&rsquo;s own TAM</li>
          <li><strong>Fork discipline:</strong> open weights cannot be unshipped</li>
        </ul>
      </div>
    </div>
    <div class="quote-block mt-3">"The question is not whether the hub stays open. It is who sets the rent &mdash; and that is why your right to re-deploy is the moat that is still open."</div>
    ''' + src_links.group(1) + '''
  </div>
</div>

'''

deck5 = deck.replace(old_block, new_block)
assert deck5 != deck
# canaries
for canary in ["Nvidia buying Hugging Face is", "bad for open source", "HENRY &middot; BAD FOR OPEN SOURCE", "ANDY &middot; GOOD FOR OPEN SOURCE", "The commons gets a landlord", "Validation, not capture"]:
    assert canary in deck5, f"missing canary: {canary}"
# nav chrome still intact
for chrome in ['id="navDots"', 'class="slide-container"', 'id="slideTotal"']:
    assert chrome in deck5, f"nav chrome dropped: {chrome}"

out = ROOT / "revs/deck.rev5.html"
out.write_text(deck5)
print(f"wrote {out} ({len(deck5)} bytes)")

# ---- speaker notes: replace the s-hot-take section ----
notes = (ROOT / "revs/speaker-notes.rev4.md").read_text()
nm = re.search(r"(## s-hot-take .*?)(?=## s-sponsor-herald)", notes, re.S)
assert nm, "notes s-hot-take section not found"

new_notes_section = '''## s-hot-take · Hot take: the fight · 3:00

- **Owner:** Henry (BAD) vs Andy (GOOD) — a real two-sided debate, not a monologue.
- **Motion:** "Nvidia buying Hugging Face is bad for open source." Twelve point nine billion dollars, unconfirmed (CNBC citing The Information). The fight lands because the stakes are real: the hub where the open-weights world ships changing hands.
- **Opening line (Henry):** "Motion: Nvidia buying Hugging Face is bad for open source. I'm arguing bad. Andy's got the hard side."
- **Henry's case (BAD):**
  - The referee sells jerseys: the biggest GPU vendor now owns the hub its competitors ship on. Model hosting, the Open LLM Leaderboard, Spaces — every neutral surface now has an owner with a dog in the fight.
  - Microsoft-GitHub precedent: GitHub stayed open after the acquisition; its neutrality did not. Copilot happened. Expect the HF equivalent.
  - Terms of service beat licenses when the hub is single. The weights stay Apache, but the hosting, the ranking, the distribution rent all run through one landlord.
- **Andy's case (GOOD):**
  - Validation: nobody pays $12.9B for a charity. Open source just got priced as the strategic layer of AI — that pulls talent, funding, and enterprise budgets toward open, not away.
  - Incentive alignment: Nvidia sells GPUs to everyone. Walling the HF garden shrinks its own market; openness is the TAM.
  - Fork discipline: open weights cannot be unshipped. The community forked when licenses tightened before; the landlord knows it, and that disciplines the rent.
- **Rebuttals (one each, ~20s):** Henry: "TAM arguments didn't stop platform taxes before — cloud vendors all sell to everyone." Andy: "GitHub's Copilot didn't kill open source; it funded it."
- **Closer (Henry):** "Either way, this is the week's real lesson in miniature: the question is never whether the hub stays open — it's who sets the rent. That's why your right to re-deploy without phoning home is the moat that's still open."
- **What would change their minds:** Henry flips if Nvidia keeps HF neutrally governed (independent board, no preferential placement) for four quarters. Andy flips if HF terms change or competitor models get deprioritized within a year.
- **Visual cue:** two-card fight layout (HENRY · BAD / ANDY · GOOD), motion in the H2, verdict quote at the bottom.
- **Handoff cue:** "That's the fight. Second sponsor read."
- **Source links:** cnbc.com/nvidia-hugging-face-acquisition; theinformation.com.
- **Target time:** 31:15 — 34:15
- **Cut contingency:** drop rebuttals, keep motion + one case each + closer (~2:00).

'''

notes5 = notes.replace(nm.group(1), new_notes_section)
assert notes5 != notes
(ROOT / "revs/speaker-notes.rev5.md").write_text(notes5)
print("wrote speaker-notes.rev5.md")
