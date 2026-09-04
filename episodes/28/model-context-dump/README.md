# Episode 28 — Model Build Context Dump

**Purpose:** the complete, sanitized input bundle used to task a model with rebuilding the WeeklyClaw Episode 28 deck. Published so any model (or human) can attempt the same build and be compared like-for-like against the baseline and the Codex `gpt-5.6-sol` xhigh variant.

## What happened here

- The live baseline is `input/deck.rev3.html` (11 slides), built by Ada (glm5.3, reasoning max) on 2026-09-04 after Henry flagged three missed launches (Gemini 3.8 Flash + Flash Cyber, Muse Spark 1.3, fal H3 Max) — rev3 added the third news grid `s-seg-grid-c`.
- A parallel variant was generated with Codex `gpt-5.6-sol` at `model_reasoning_effort=xhigh` from this exact bundle. Its output lands in `output/` when the run completes; `BUILD_NOTES.md` records what it changed.
- The task contract is `PROMPT.md` — same data, same 11 slides, same stories/links/assets; the model exercises composition only, inside the frozen Episode-23 template authority.

## Bundle map

- `PROMPT.md` — the exact task prompt given to the variant model
- `input/deck.rev3.html` — baseline deck (content + structure source of truth)
- `input/authority-deck-ep23.html` — approved Episode 23 deck, the verbatim template authority (CSS/SVG/JS)
- `input/agenda.rev3.md`, `talking-points.rev3.md`, `speaker-notes.rev3.md`, `henry-section.rev3.md`, `andy-section.rev3.md`, `host-cheat-sheet.rev3.md` — the seven-artifact editorial package
- `input/candidates.md|.json` — story scoring ledger for the week
- `input/evidence.md`, `input/state.json` — verification receipts (paths sanitized)
- `input/sources/*.md` — primary-source extracts for every story
- `input/media-manifest.json` + `input/assets/` — every image the deck references, with provenance
- `input/contracts/*.md` — template-authority, on-slide-live-artifacts, deck-contract recipes
- `input/workspace-template.md`, `input/agenda-template.md` — agenda structure rules
- `input/validate_deck.py` — the 14-check validator (base 8 + 6 template-authority gates)

## Scoring a variant

1. `python3 input/validate_deck.py <deck.html> input/speaker-notes.rev3.md input/authority-deck-ep23.html` → exit 0
2. Render at 1600x900, check every slide: no overlap, no clipping, artifact dominance on news slides
3. Content parity: all 12 story cards present, every fact/URL intact, sponsor order Herald→Heritage, Discord QR on close slide
4. Subjective: composition quality vs `input/deck.rev3.html`

Note: paths inside receipts were sanitized (`/home/henrymascot` → `~`) for publication; the bytes of deck/artifact files are untouched.
