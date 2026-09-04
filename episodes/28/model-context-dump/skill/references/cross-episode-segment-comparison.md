# Cross-episode segment comparison on request (deterministic, vision-optional)

Henry may ask to compare "What Happened This Week" (news) segments across episodes, e.g. "go to last week's episode and the week before, screenshot my segment, compare with the new one and see if the right things are there." Recipe verified on Episodes 24/25/26, 2026-08-20.

## 1. Locate the latest deck revisions

Root `episodes/<N>/deck.html` does NOT exist for every episode (Episode 24-26 kept decks only under `showprep/revs/`). Find the latest revision deterministically:

    latest=$(ls episodes/<N>/showprep/revs/deck.rev*.html | sed 's/.*rev\([0-9]*\)\.html/\1 &/' | sort -n | tail -1 | cut -d' ' -f2)

Segment titles per episode come from `showprep/revs/agenda.rev<N>.md` (`## Segment N — ...` headings) and scores from `showprep/state.json` (`scores`). Episode dates from `state.json` `show_date_ny`.

## 2. Identify news-slide IDs

Slide IDs vary per episode (EP24: `s-news-intro`, `s-seg-weathernext`, `s-seg-models`; EP25: `s-news-intro`, `s-seg-1`..`s-seg-5`; EP26: `s-the-map`, `s-seg-qwen-open`, ...). Grep the deck:

    grep -oE 'id="(s-[a-z0-9-]+)"' "$latest" | grep -iE 'seg|news|map'

## 3. Screenshot specific slides at 1600x900

The decks' navigation JS honors `location.hash` at load (verified in the deck `<script>`), so headless Chrome with a hash lands on the exact slide:

    google-chrome --headless=new --disable-gpu --hide-scrollbars --window-size=1600,900 --screenshot=<out.png> --virtual-time-budget=4000 "file://<deck.html>#<slide-id>"

Runs headless on the Ada gateway host. Output to e.g. `showprep-qa/ep<N>-news-compare/`.

## 4. Verify slide identity WITHOUT vision (fallback when vision pipeline is down)

Vision (vision_analyze) can be unavailable or misrouted (e.g. aux model 404 against a Gemini-style endpoint). Deterministic verification chain that fully substitutes:

1. **Text extraction**: decks use `<div class="slide" id="...">`, NOT `<section>`. A `<section>`-based regex silently returns NOT FOUND for every slide. Slice from `id="<slide-id>"` to the next `class="slide"`, then pull the first `h1/h2` or title-class text.
2. **Hash support check**: confirm `location.hash` handling exists in the deck `<script>` so the screenshot actually shows the requested slide.
3. **Render sanity**: PIL per-file check — size is 1600x900, contrast (max-min grayscale over a downsample) > 100, md5 distinct across files (catches all-same-slide renders).

## 5. Contact sheet for delivery

Assemble a labeled vertical contact sheet (PIL): each row = label bar (brand color, e.g. `#2a7e6b`) + 1100px-wide slide. Deliver via `MEDIA:<path>` plus individual PNG paths. Henry reviews on mobile — the single sheet is the deliverable, not filesystem paths.

## 6. Editorial comparison output

Report per-episode segment lists (verified from agenda + state.json, not memory), then a judgment on continuity: pattern consistency (model releases / harness-economics / one infra-hardware beat is the historical shape), thematic drift (e.g. EP26 leaned 3-of-5 money-rails stories vs 24/25's capability/infra balance), and any contract violations found (e.g. EP26 rev1 marked S2/S4 "Andy lead" against the standing Henry-leads-news rule).
