# TASK: Rebuild WeeklyClaw Episode 28 deck (variant build — model comparison)

You are rebuilding the WeeklyClaw Episode 28 presentation deck from an APPROVED baseline. This is a controlled model-comparison rebuild: the story set, facts, figures, quotes, dates, URLs, ordering, ownership, sponsors, and slide structure are FROZEN. Your job is to produce the same deck — same 11 slides, same stories, same data — exercising your own composition ability within the frozen contract.

## HARD RULES (violation = failed build)

1. **Same data.** Every fact, number, quote, date, company name, model name, price, benchmark figure, and URL in `input/deck.rev3.html` and `input/agenda.rev3.md` must be preserved exactly where its story appears. Do not add stories, do not drop stories, do not re-score, do not re-research. The story set is: A1 Nvidia–Hugging Face ($13B definitive agreement), A2 Anthropic Fable 5.1 + Mythos 5.1, A3 OpenClaw 2.0, A4 Qwen3.8-Max-0902, B1 NYC student-AI moratorium, B2 Visko Orbis 1.0, B3 OpenAI GPT-6 Astra, B4 AI-sentience poll (Henry's post), C1 Gemini 3.8 Flash + Flash Cyber, C2 Muse Spark 1.3, C3 fal H3 Max, C4 independent-receipts card. 12 cards across 3 news grids, 11 slides total.
2. **Template authority is `input/authority-deck-ep23.html`** (Episode 23 approved deck). Clone its complete `<style>` block, `<script>` block, SVG `<symbol>`/`<defs>` (including `<symbol id="weeklyclaw-logo">`), CSS custom properties, layout classes, and navigation/fullscreen/scroll/swipe JS **verbatim**. (sha256 of the authority file: 3548178052bb0c8e151b61ca230930885af8b7b3016072de1bfaa38aea598785.) Replace episode-specific content only. Do NOT invent new CSS class systems, SVG symbols, brand marks, or logo paths. The baseline `input/deck.rev3.html` is already a valid instance of this template — you may treat it as the structural reference and improve only composition, spacing, hierarchy, and polish within the same class vocabulary.
3. **Image assets:** every image the deck references lives under `input/assets/` (artifacts, sponsors, socials). Reuse the SAME files. Do not generate, fetch, or substitute images. Sponsor marks must resolve to `input/assets/sponsors/` files.
4. **What you SHOULD exercise (the point of this run):** composition quality — visual hierarchy of each slide, artifact dominance on news slides, headline typography, grid rhythm, spacing, alignment, consistent card anatomy, clean Sources slide, no overlaps, no text clipping at 1600x900. You may adjust inline styles, flex ratios, font sizes within the template's scale, and card ordering nuances WITHIN a grid as long as every story, its headline facts, and its links survive intact.
5. **News slides are visual prompts, not briefing documents:** headline + zero-to-two short context lines + dominant image + small LIVE link. Details live in speaker notes (`input/speaker-notes.rev3.md`), which you copy through unchanged.
6. **Structure to reproduce exactly (11 slides):**
   - s-title — title slide
   - s-cold-open — "The agreement landed. The models answered."
   - s-sponsor-herald — Herald Labs sponsor read
   - s-seg-grid-a — What Happened This Week part 1 (A1–A4)
   - s-seg-grid-b — part 2 "Then the world pushed back." (B1–B4)
   - s-seg-grid-c — part 3 "The launch pedal stayed down." (C1–C4)
   - s-signal-outside — Signal From Outside
   - s-hot-take — Hot Take
   - s-sponsor-heritage — Heritage Telecom sponsor read
   - s-close — close + Discord QR (assets/socials/weeklyclaw-discord-qr.png, link https://weeklyclaw.ai/discord)
   - s-sources — Sources appendix (all receipt links incl. C1–C3 blocks)
   Stable slide IDs must match this list. Keep `slideTotal` = 11 and the nav chrome (`navDots`, `slideNum`/`slideTotal`, `kb-hint`, `.slide-container`) functional.
7. **Ownership:** What Happened This Week segments are Henry-led. Sponsor order: Herald first (after cold open), Heritage last (before close).
8. **No fabricated content.** If something in the baseline looks wrong, preserve it anyway — this is a same-data rebuild; note observations in `output/BUILD_NOTES.md` instead of changing facts.

## OUTPUT CONTRACT

Write to `output/` (do not touch `input/`):
- `output/deck.html` — the rebuilt deck (single self-contained HTML, relative asset paths as in baseline)
- `output/BUILD_NOTES.md` — what you changed compositionally vs baseline, observations, and any lint concerns
- Optional but appreciated: `output/structure-check.txt` — output of the validation below

## VALIDATION (run before declaring done)

```bash
python3 input/validate_deck.py output/deck.html input/speaker-notes.rev3.md input/authority-deck-ep23.html
```
Exit 0 = PASS (14 checks incl. template-authority gates). Fix and re-run until PASS.

Then a quick structural self-check: parse slide IDs from output/deck.html, confirm the 11 IDs above, in order, unique.

## CONTEXT FILES (read in this order)

1. `input/deck.rev3.html` — baseline deck (structure + content source of truth)
2. `input/authority-deck-ep23.html` — template authority (CSS/SVG/JS verbatim)
3. `input/agenda.rev3.md` — canonical editorial agenda
4. `input/speaker-notes.rev3.md` — speaker notes (copy through)
5. `input/media-manifest.json` — every media asset + provenance
6. `input/candidates.md` / `input/candidates.json` — story scoring ledger
7. `input/evidence.md`, `input/state.json` — verification receipts
8. `input/sources/*.md` — primary-source extracts for every story
9. `input/contracts/*.md` — template-authority, live-artifact, deck-contract recipes
10. `input/workspace-template.md`, `input/agenda-template.md` — agenda structure rules

When done, reply with exactly: `BUILD DONE validator=<PASS|FAIL> slides=<N>` plus a 5-line summary.
