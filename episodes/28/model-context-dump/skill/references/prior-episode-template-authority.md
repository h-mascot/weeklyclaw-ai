# Prior-episode template authority and render-QA gates

This reference defines the deterministic gates that prevent a build from
inventing its own visual theme, logo, or layout instead of cloning the prior
APPROVED episode deck. Episode 24's BUILD ignored the Episode 23 template and
produced an invented inline `<symbol id="claw-mark">` SVG, an invented
`brand-mark`/`claw-text` CSS class system, sponsor `<img>` refs to non-existent
files, and a stripped 37 KB deck. These gates would have caught all of it.

## 1. Discover the template authority

At BUILD (or any material deck rebuild), discover the prior APPROVED episode:

```python
import json, os, glob

def find_template_authority(workspace="~/weeklyclaw"):
    """Return (episode_number, deck_path, sha256) for the highest APPROVED
    episode with a non-empty root deck.html."""
    best = None
    for state_path in sorted(
        glob.glob(f"{workspace}/episodes/*/showprep/state.json")
    ):
        try:
            with open(state_path) as f:
                state = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            continue
        if state.get("approval_state") != "APPROVED":
            continue
        ep = state.get("episode")
        if not isinstance(ep, int):
            continue
        deck_path = f"{workspace}/episodes/{ep}/deck.html"
        if not os.path.exists(deck_path) or os.path.getsize(deck_path) == 0:
            continue
        if best is None or ep > best[0]:
            import hashlib
            h = hashlib.sha256(open(deck_path, "rb").read()).hexdigest()
            best = (ep, deck_path, h)
    return best  # (ep, path, sha256) or None
```

As of this reference: Episode 23, sha256
`3548178052bb0c8e151b61ca230930885af8b7b3016072de1bfaa38aea598785`.

Henry may explicitly name a replacement. Absent that, the prior APPROVED
episode is the authority.

## 2. Run the template-comparison validator

The upgraded `scripts/validate_deck.py` accepts the authority deck as an
optional third argument:

```bash
python3 scripts/validate_deck.py \
  episodes/<N>/showprep/revs/deck.rev1.html \
  episodes/<N>/showprep/revs/speaker-notes.rev1.md \
  episodes/<AUTHORITY_EP>/deck.html
```

When the authority deck is provided, these gates run:

- **CSS custom-property parity** (check 9): all theme-defining custom
  properties (`--site-paper`, `--claw-red`, `--display`, `--mono`, etc.) must
  have the same value in the new deck as in the authority deck. Value drift
  means the builder invented its own palette.
- **SVG symbol parity** (check 10): every `<symbol>` in the authority deck must
  be present in the new deck. The `weeklyclaw-logo` symbol's `viewBox` must
  match exactly.
- **Invented-logo rejection** (check 11): any `<symbol>` in the new deck whose
  ID contains a brand keyword (`claw`, `logo`, `brand`, `mark`, `icon`, `wc`)
  but is NOT in the authority deck is an invention and fails the build. Inline
  SVG blocks with `claw`/`brand-mark` class that are not `<use>` references to
  the authority symbol also fail.
- **Layout-class coverage** (check 12): core layout classes defined in the
  authority deck's CSS (`slide`, `content`, `card`, `part-label`, `story-num`,
  `claw-bg`, `glow-orb`, `logo-row`, `bullet-list`, etc.) must be present in
  the new deck. Missing classes mean the builder invented a new layout system.
- **Sponsor-asset provenance** (check 13): every `assets/sponsors/` file
  referenced in the deck must exist on disk and, if present in the authority
  episode, must match by sha256. Sponsor marks are real brand assets.
- **Deck size sanity** (check 14): if the new deck is less than 55% of the
  authority deck's byte size, the builder likely stripped layout, CSS, or
  assets. Episode 24 was 37 KB vs Episode 23's 74 KB (50%).

Exit 0 = PASS. Non-zero = first failed gate.

### Exact reference values (Episode 23 authority)

When the validator reports a mismatch, these are the exact values the new
deck must carry. A rebuilder should not have to re-derive them from the
authority deck.

**`weeklyclaw-logo` SVG symbol (copy verbatim):**

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="weeklyclaw-logo" viewBox="0 0 64 64">
      <rect x="2" y="2" width="60" height="60" rx="12" fill="#f2eadb" stroke="#2f2923" stroke-width="3"></rect>
      <path d="M12 19 16 9M21 19 25 9M30 19 34 9" fill="none" stroke="#2d8472" stroke-width="4" stroke-linecap="round"></path>
      <path d="m13 27 8 25 11-18 10 18 9-25" fill="none" stroke="#211c18" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"></path>
    </symbol>
  </defs>
</svg>
```

Every slide brands via `<use href="#weeklyclaw-logo"/>`. The invented
`<symbol id="claw-mark">` (abstract arch `M16 50 C 16 36...`) is the
canonical rejection case.

**Type scale (Episode 23, MUST match exactly):**

| Token        | Required CSS                                                     |
|--------------|------------------------------------------------------------------|
| `h1,h2,h3`   | `font-family:var(--display); font-weight:800; letter-spacing:-.025em;` |
| `h1,h2`      | `text-transform:uppercase;`                                      |
| `h1`         | `font-size:4rem; line-height:.92; margin-bottom:16px;`          |
| `h2`         | `font-size:2.55rem; line-height:.96; margin-bottom:12px;`       |
| `h3`         | `font-size:1.35rem; line-height:1; margin-bottom:8px;`          |
| `.subtitle`  | `font-size:1.15rem; line-height:1.5; max-width:820px;`          |
| `.card p,.card li` | `font-size:0.95rem; line-height:1.45;` (display font, NOT mono) |

Episode 24 rev1 shrunk these (h1→3.4rem, h2→2.05rem, h3→1.25rem) and
switched `.card p` to `font-family:var(--mono)`, producing the
"report-like" density. Verify with:
`grep -c 'font-size:4rem' deck.html` ≥ 1;
`grep -c 'font-size:2.55rem' deck.html` ≥ 1.

**Must-present CSS classes (defined AND used):**

`.slide`, `.content`, `.card`, `.card-glow`, `.tag`+variants, `.pill`+variants,
`.quote-block`+variants, `.bullet-list`, `.two-col`, `.three-col`, `.split`,
`.hook`/`.hook-num`/`.hook-text`, `.part-label`, `.story-num`, `.slide-brand`,
`.slide-tag`, `.sponsor-lockup`+`.herald`/`.heritage`, `.sponsor-logo-chip`,
`.channel-chip`, `.logo-row`, `.discord-qr`, `.social-cta`, `.glow-orb`+`.orb-*`,
`.claw-bg`, `.arc-wrap`/`.arc-step`/`.arc-num`/`.arc-label`,
`.ladder`/`.ladder-row`/`.ladder-track`/`.ladder-fill`/`.ladder-val`,
`.event-row`/`.event-date`, `table.cmp`, `.src-links`, `.src-note`, `.stamp`,
`.alert-card`, `.warn-card`, `.gradient-line`+`.wide`, `.gradient-text`.

**Must-absent classes (rev1 inventions to reject):**

`.metric`, `.metric-label`, `.kicker`, `.eyebrow`, `.lower-third`, `.badge-warn`,
`.badge-soft`, `.source-link`, `.source-pill`, `.source-row`, `.thumb`,
`.fullscreen-btn`, `.four-col`, `.brand-mark`, `.claw`, `.claw-text`, `.mt-4`.

**Controls parity (check 15, navigation behavior):**

The authority deck's keyboard handler binds ArrowRight/Space/PageDown (next),
ArrowLeft/PageUp (prev), **Home** (first), **End** (last), **F** (fullscreen).
It also implements hash deep-linking: `history.replaceState(null,'',`+
`'#'+slides[current].id)` on nav, plus `location.hash` read on load. The
slide-counter uses two spans (`<span id="slideNum">N</span> / <span`+
` id="slideTotal">M</span>`), not a static text node. Episode 24 rev1 dropped
Home/End/PageDown/PageUp and hash deep-linking, and added a standalone
`.fullscreen-btn` element the authority deck does not have. Verify:
`grep -c "'Home'" deck.html` = 1;
`grep -c 'replaceState' deck.html` ≥ 1;
`grep -c 'location.hash' deck.html` ≥ 1;
`grep -c 'fullscreen-btn' deck.html` = 0.

## 3. Render-QA gate (1600x900 headless Chromium)

After the structural validator passes, render both the authority deck and the
new deck at 1600x900 and check for visual consistency, clipping, overlap, and
report-like density. This is a visual comparison, not just a structural check.

### Revision-explicit runner gate

A render can pass while proving the wrong deck. Before execution, inspect the
renderer for hardcoded `deck.rev1.html` or `qa/render-1600x900` paths. The
runner must accept the selected deck revision and output directory as explicit
arguments, resolve both to absolute paths, and print them before rendering.
Afterward, assert all of the following against the selected revision:

- rendered slide count equals the unique `.slide` ID count,
- rendered filenames preserve the selected revision's slide order,
- content canaries from the material change are present in both the HTML and
  the relevant screenshot,
- ordered canaries such as rotating sponsors appear in the expected DOM and
  screenshot order,
- the evidence receipt names the exact input deck path and output directory.

Never accept PNG count/nonblank checks alone. A stale hardcoded renderer can
produce a perfect 14-slide report from rev1 while rev3 is the artifact being
published. If the runner ignores supplied arguments, fix the runner first,
then rerun QA and visually inspect every materially changed slide.

### Working CDP measurement recipe (validated)

This produces exact per-slide overflow numbers at 1600x900 and is the recipe
used to confirm both Episode 23 and the Episode 24 rebuild. It does not rely
on Puppeteer; it drives Chrome's CDP socket directly with `websocket-client`.

```bash
# 1. Serve the workspace so relative asset paths resolve.
cd ~/weeklyclaw
python3 -m http.server <PORT> --bind 127.0.0.1 &

# 2. Launch headless Chrome with remote debugging + origin allow.
google-chrome --headless=new --disable-gpu --no-sandbox \
  --remote-debugging-port=9222 --remote-allow-origins=* \
  --window-size=1600,900 about:blank &
```

Then from Python (`websocket-client`):

```python
import json, time, urllib.request, websocket

targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read())
ws = websocket.create_connection(
    next(t for t in targets if t["type"]=="page")["webSocketDebuggerUrl"],
    origin="http://127.0.0.1:9222")

mid=[0]
def call(method, params=None):
    mid[0]+=1
    ws.send(json.dumps({"id":mid[0],"method":method,"params":params or {}}))
    while True:
        r=json.loads(ws.recv())
        if r.get("id")==mid[0]: return r

# Navigate, set exact viewport, measure each slide in isolation.
call("Page.enable")
call("Page.navigate",{"url":f"http://127.0.0.1:{PORT}/{deck_path}"})
time.sleep(2.5)
call("Emulation.setDeviceMetricsOverride",
     {"width":1600,"height":900,"deviceScaleFactor":1,"mobile":False})
time.sleep(0.8)

JS = """
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var out=[];
  slides.forEach(function(s,i){
    slides.forEach(function(x){x.classList.remove('active');});
    s.classList.add('active');
    var content=s.querySelector('.content');
    out.push({id:s.id, idx:i,
              slideClientH:s.clientHeight, slideScrollH:s.scrollHeight,
              contentClientH:content?content.clientHeight:0,
              contentScrollH:content?content.scrollHeight:0});
  });
  slides[0].classList.add('active');
  return JSON.stringify(out);
})()
"""
result = call("Runtime.evaluate",{"expression":JS,"returnByValue":True})
for s in json.loads(result["result"]["result"]["value"]):
    overV = s["contentScrollH"] - s["contentClientH"]
    flag = f"CLIP +{overV}" if overV > 2 else "ok"
    print(f"  [{s['idx']:2d}] {s['id']:32s} {flag}")
```

**Pass criterion:** for every slide, `content.scrollHeight ≤`+
` content.clientHeight + 2px`. Decorative bleed (`.glow-orb`, `.claw-bg`)
may extend the slide's own `scrollHeight` beyond `clientHeight`; that is
intentional and clipped by `overflow:hidden`, so judge by
`.content.scrollHeight`, not `.slide.scrollHeight`.

### Playwright alternative (simpler setup, adds overlap detection)

The CDP recipe above checks scroll overflow only. Playwright gives the same
scroll check **plus** deterministic element-level overlap detection in a
single run, and does not require a raw websocket or a local HTTP server
(it loads the deck via `file://` URI). When Playwright is available, prefer
it for render QA.

```python
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

DECK = Path('revs/deck.rev1.html').resolve().as_uri()
OUT  = Path('qa/render-1600x900'); OUT.mkdir(parents=True, exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        page = await browser.new_page(viewport={'width': 1600, 'height': 900})
        await page.goto(DECK, wait_until='networkidle')
        ids = await page.eval_on_selector_all('.slide', 'els=>els.map(e=>e.id)')
        results = []
        for i, sid in enumerate(ids):
            # Activate slide i only (disable CSS transitions first so the
            # 0.45s opacity fade doesn't leave the previous slide visible
            # during the screenshot — a common false-positive source).
            await page.evaluate(
                '(i)=>{document.querySelectorAll(".slide")'
                '.forEach(e=>e.style.transition="none");'
                'document.querySelectorAll(".slide")'
                '.forEach((e,j)=>e.classList.toggle("active",i===j))}', i)
            await page.wait_for_timeout(80)
            r = await page.evaluate('''(sid)=>{
                const s=document.getElementById(sid), c=s.querySelector('.content');
                const cr=c.getBoundingClientRect();
                const els=[...c.querySelectorAll(
                  'h1,h2,h3,p,li,a,img,table,.card,.quote-block')];
                let overlaps=0;
                for(let i=0;i<els.length;i++){let a=els[i].getBoundingClientRect();
                  for(let j=i+1;j<els.length;j++){let b=els[j].getBoundingClientRect();
                    if(a.width&&a.height&&b.width&&b.height&&
                       a.left<b.right-2&&a.right>b.left+2&&
                       a.top<b.bottom-2&&a.bottom>b.top+2&&
                       !els[i].contains(els[j])&&!els[j].contains(els[i])) overlaps++;}}
                return {id:sid,
                        overflow: cr.top<42||cr.bottom>840||cr.left<30||cr.right>1570,
                        scrollOverflow: c.scrollHeight>c.clientHeight+2||
                                        c.scrollWidth>c.clientWidth+2,
                        overlaps: overlaps};}''', sid)
            await page.screenshot(path=str(OUT / f'{i+1:02d}-{sid}.png'))
            results.append(r)
        await browser.close()
        bad = [r for r in results if r['overflow'] or r['scrollOverflow'] or r['overlaps']]
        print('RENDER_QA', 'PASS' if not bad else 'FAIL', 'bad_slides=', len(bad))
        if bad: print(json.dumps(bad, indent=2))

asyncio.run(main())
```

**Pass criterion (Playwright):** zero bad slides — every slide has no content
overflow, no scroll overflow, and zero pairwise element overlaps. The margin
thresholds (top≥42, bottom≤840, left≥30, right≤1570) leave room for the fixed
progress-bar/nav-dots/kb-hint/slide-counter chrome.

**Transition-disable note:** the `.slide` CSS has a `0.45s` opacity transition.
If you activate slide *N* and screenshot before the transition completes, the
previous slide (*N-1*) is still partially visible at `opacity>0`, producing a
false "double-exposure" in both screenshots and the overlap check. Always set
`e.style.transition='none'` before toggling `.active`, or wait ≥ 500ms after
activation.

**Chromium path:** under snap environments, pass
`executable_path='/snap/bin/chromium'` to `p.chromium.launch()`. The
`--no-sandbox` flag is required for headless CI/snap and is safe for local
render-only QA.

### Prerequisites

Chromium/Chrome is available at `/usr/bin/google-chrome`,
`/usr/bin/chromium-browser`, or `/snap/bin/chromium`. `websocket-client`
is supplied by `pip install websocket-client` or
`uv run --with websocket-client`. Node v22 at `/usr/bin/node` for the
deck's inline JS (not needed for the CDP measurement itself).

### Visual checks

For each rendered slide, confirm:

1. **No text clipping**: no text element has its bounding box extending beyond
   the slide's content area (check `overflow: hidden` is not hiding content).
2. **No element overlap**: cards, images, text blocks, and sponsor logos do not
   visually overlap in ways the authority deck does not.
3. **No report-like density**: the slide does not look like a text-dense report
   or bibliography. The authority deck uses spacious editorial cards with
   large display type. A slide with > 8 paragraphs or > 15 bullet items is
   report-like.
4. **Visual consistency with authority**: the title slide's logo placement,
   gradient treatment, card styling, and part-label/story-num markers match
   the authority deck's visual language.

### Automated density heuristic

```python
# After rendering, run a simple text-density check on each slide screenshot
# using PIL to count text pixels. A slide with > 35% text coverage (excluding
# background grid) is report-like and fails.
from PIL import Image
import sys

def text_density_pct(png_path):
    img = Image.open(png_path).convert('L')
    pixels = list(img.getdata())
    dark = sum(1 for p in pixels if p < 128)  # text-ish pixels
    return dark / len(pixels) * 100

for slide in sys.argv[1:]:
    pct = text_density_pct(slide)
    status = "FAIL" if pct > 35 else "OK"
    print(f"{status}: {slide} text density {pct:.1f}%")
```

## 4. Stage the authority deck for the Cursor builder

When staging the Cursor run directory on Enterprise, copy the authority deck
as `input/template-authority-deck.html` and its `assets/sponsors/` directory
into `input/assets/sponsors/`. The builder instruction must say:

> Clone `input/template-authority-deck.html` as the verbatim visual and layout
> template. Copy its full `<style>`, `<script>`, SVG `<symbol>`/`<defs>`, CSS
> custom properties, and all layout classes. Replace episode-specific content
> (titles, story copy, metrics, links, media `src`) only. Do not invent new
> CSS class systems, SVG symbols, brand marks, or logo paths. Use
> `<use href="#weeklyclaw-logo"/>` for the WeeklyClaw logo. Copy sponsor
> assets from `input/assets/sponsors/` and reference them with relative paths.

## 5. Evidence to record

In `evidence.md` and `runlog.md`, record:

- Template authority episode number, path, and sha256.
- Template-comparison validator result (exit code, per-check pass/fail).
- Render-QA result: slides rendered, any clipping/overlap/density flags.
- Sponsor-asset provenance: each sponsor file's sha256 match against the
  authority episode.
- Deck size comparison: new deck bytes vs authority deck bytes.

## 6. The Episode 24 failure (what these gates catch)

Episode 24's BUILD (2026-08-07) would have failed at:

- **Check 11 (invented-logo rejection)**: EP24 defined
  `<symbol id="claw-mark">` which is not in EP23's symbol set. The old
  `validate_deck.py` looked for the string `claw-mark` and passed, but the
  upgraded validator sees `claw-mark` as an invented brand symbol.
- **Check 12 (layout-class coverage)**: EP24 invented `brand-mark`,
  `claw-text`, `eyebrow`, `metric`, `metric-label` classes not present in
  EP23. Core EP23 classes (`claw-bg`, `glow-orb`, `story-num`) are absent.
- **Check 13 (sponsor-asset provenance)**: EP24 references
  `assets/sponsors/herald-labs-icon.svg` and
  `assets/sponsors/heritage-telecom-logo-horizontal-1200.jpg` but the
  `assets/sponsors/` directory does not exist in the EP24 showprep tree.
- **Check 14 (deck size sanity)**: EP24 is 37,332 bytes vs EP23's 74,309
  bytes (50.2%), below the 55% threshold.
- **Check 6 (theme markers, fixed)**: EP23 uses `weeklyclaw-logo` (the real
  symbol), not `claw-mark`. The old validator's `claw-mark` check would have
  FAILED on the correct EP23 deck while PASSING the incorrect EP24 deck.

### Why checks 9–15 exist: the validator-substring trap

The Episode 24 BUILD passed the *old* `validate_deck.py` because that
validator's theme-marker check looked for the substring `claw-mark`, which
the invented EP24 deck contained and the real EP23 deck did not (EP23 uses
`weeklyclaw-logo`). A substring marker that happens to match the invention
while failing the authority is the failure mode checks 9–15 are designed to
close: instead of matching strings, they compare the new deck's SVG symbols,
CSS custom properties, and layout classes against the authority deck
*structurally*. Any future "theme marker" check must assert the *authority's
symbol ID is present and identical*, never merely that *some* claw-flavored
token is present.

### Live-deck byte-equality check

Before declaring a rebuild done, fetch the public deck and confirm it is
byte-identical to the canonical revision you intend. The Episode 24 rev1
deck at `weeklyclaw.ai/episodes/24/deck` was confirmed byte-identical
(37,332 bytes, same `claw-mark` symbol, same 12 slide ids) to the local
`episodes/24/showprep/revs/deck.rev1.html`. `web_extract` may fail with a
credits error; fall back to `curl -sL <url>` and grep for the symbol id /
slide ids / byte length. This catches the case where a rebuild was staged
locally but the live site still serves the rejected deck (or vice versa).
