# Episode 25 — Build runlog

**Date:** Friday, August 14, 2026 · 11:00 EDT (15:00 UTC)
**Role:** BUILD
**Lock PID:** 2348570
**Target runtime:** 32–38 min (planned ~35:00) · hard stop 45 min
**Show date:** Friday, August 14, 2026 · 4:00 PM ET

## Cron decisions

- Episode 25 BUILD activated after confirming:
  - `date` returned `Fri Aug 14 15:01:37 UTC 2026`.
  - `episodes/25/daily-topic-list.md` present (138,836 bytes, mtime 2026-08-14 13:04:30 UTC, 665 lines).
  - `episodes/25/showprep/` did not exist at cron start.
- Episode 24 state inspected and confirmed frozen on 2026-08-07 (`approval_state: UNVALIDATED`); treated as stale context for the new build, except for: (a) approved sponsor assets and signal poster, copied verbatim, (b) authority deck `/home/henrymascot/weeklyclaw/episodes/23/deck.html` used as the template-authority baseline.
- No active host approvals/pins found for Episode 25 via `lcm_grep` query `weeklyclaw friday show prep OR episode 25` (current-session only; no external host-shared resources discovered).

## Selection (5 segments + Hot Take + Signal From Outside)

| ID | Title | Owner | Score |
|----|-------|-------|-------|
| S1 | DeepSeek ships the model, the harness, and the API dialect | Andy | 9.9 |
| S2 | GLM-5.3 cyber via post-training; weights delayed two weeks | Henry | 9.8 |
| S3 | Gemini 3.7 Flash + Ultrafast: speed becomes a product tier | Henry | 9.7 |
| S4 | Writer cuts agent cost in the harness, not the model alone | Andy | 9.6 |
| S5 | OpenAI Computer History + Drive ambient context | Andy | 9.8 |
| HOT | Hot Take: Anthropic multiagent patterns (late discovery 2026-08-12) | Henry / Andy | N/A |
| SIGNAL | Signal From Outside: IBM Mixture of Experts (wVdivlahcm0) | Andy | anchor |

Thesis: **The model is no longer the product — the operating layer is.**

Arc: model + harness + dialect → cyber release gate → speed as a tier → harness cost cuts → ambient work context.

## Asset provenance

- All six sponsor assets copied verbatim from Episode 24 (`/home/henrymascot/weeklyclaw/episodes/24/showprep/assets/sponsors/`); SHA256 hashes verified byte-for-byte against Ep 24 source.
- Signal poster `signal-outside-poster.jpg` copied from Episode 24 (permanent weekly anchor).
- Discord QR `weeklyclaw-discord-qr.png` copied from Episode 24.
- No invented logos, no invented SVG symbols, no invented CSS — the deck's `<style>`, `<svg><defs>`, and `<script>` blocks are extracted verbatim from the Episode 23 authority deck.

## Validation evidence

- Validator: `/home/henrymascot/.hermes/skills/operations/weeklyclaw-show-prep/scripts/validate_deck.py` (skill canonical), copied to `/home/henrymascot/weeklyclaw/episodes/25/showprep/qa/validate_deck.py`.
- Authority comparison passed: CSS custom properties (15), SVG symbols (`weeklyclaw-logo`), layout classes (16), sponsor asset provenance, deck size 60,732 bytes vs authority 74,261 bytes.
- JS syntax: `node --check -` PASS.
- Slide-ID parity: 14 slides in deck ↔ 14 slide IDs in speaker notes.
- Source links: 22 clickable (one duplicate href counts once).
- Local media: 6 paths resolved (`assets/sponsors/herald-labs-icon.svg` × 2, `assets/sponsors/heritage-telecom-mark-256.png`, `assets/sponsors/heritage-telecom-logo-horizontal-1200.jpg`, `assets/images/signal-outside-poster.jpg`, `assets/socials/weeklyclaw-discord-qr.png`).
- Visual render: 14 PNGs at 1600x900 produced via Playwright + chromium; all non-blank (min 269,082 bytes, max 506,010 bytes), color extrema within expected cream-paper + ink ranges.

## Artifacts produced

- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/deck.rev1.html` (60,732 bytes)
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/speaker-notes.rev1.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/agenda.rev1.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/talking-points.rev1.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/henry-section.rev1.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/andy-section.rev1.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/host-cheat-sheet.rev1.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/_slides_content.html` (slide body source)
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/revs/build_deck.py` (build script)
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/state.json` (state)
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/state.lock` (PID 2348570)
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/sources/s1-deepseek.md` ... `s5-openai-ambient.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/sources/hot-take-multiagent.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/sources/signal-outside.md`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/qa/validate_deck.py`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/qa/render_deck.py`
- `/home/henrymascot/weeklyclaw/episodes/25/showprep/qa/render-1600x900/*.png` (14 slides)

## Posture

- `approval_state: UNVALIDATED` (unchanged).
- No root artifacts overwritten at the episode-level (`/home/henrymascot/weeklyclaw/episodes/25/`); the showprep/revs/ artifacts are isolated to the build workspace.
- No Discord lifecycle post executed (still UNVALIDATED).
- No Telegram handoff message emitted (still UNVALIDATED).
- No cron definition modified.
- No host-shared resource was approved in this session; selection derived from the populated daily intake.

## Next actions (held pending Henry or Andy approval)

1. Henry or Andy approves via Telegram topic `-1004370723812:17` to flip `approval_state` from `UNVALIDATED` to `APPROVED`.
2. Promote `revs/deck.rev1.html` and `revs/speaker-notes.rev1.md` to the root `episodes/25/` if approved.
3. Emit the Discord lifecycle post (template in `references/post-freeze-verification-and-handoff.md`).
4. Emit the Telegram handoff summary.
5. Publish the show draft website (template in `references/website-draft-publication.md`).

## Pitfalls / known limitations

- This build did not independently verify any DeepSeek, Z.ai, Google, OpenAI, or Writer benchmark.
- The harness-leverage r=0.99 result spans only six models; Writer's figures are directional.
- Ultrafast price and SLA are undisclosed.
- OpenAI Computer History + Drive framing is OpenAI's own; this build did not inspect local event files, server-side retention, deletion completeness, cross-workspace leakage, or real recall quality.
- Anthropic multiagent paper is Anthropic's own research; not independently replicated at retrieval.
- The cvd.z.ai ledger counts are Z.ai's own audit queue; "embargo" is Z.ai's disclosure framing.