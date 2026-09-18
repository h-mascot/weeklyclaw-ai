# Ep 27 rev2 — Evidence (12:00 EDT REFRESH tick, 2026-08-27)

**Tick:** 27-2026-08-27-12 (REFRESH)
**Operator:** Ada (cron)
**Host:** Henry (awaiting APPROVE in Telegram review card)
**Selected revision:** rev2 (supersedes rev1)

## What this REFRESH tick delivered

1. **Sponsor rotation corrected** (Heritage → Herald, inverting Ep 26's Herald → Heritage). Rev1 had shipped Herald-first by mistake; rev2 fixes it across all 6 host-facing artifacts and the deck.
2. **Deck.rev2.html produced**: 13 slides, 48,570 bytes, cloned from Ep 26 authority head/style/SVG/script verbatim with new slide bodies.
3. **Validate_deck.py against Ep 26 authority**: ALL CHECKS PASSED.
4. **Playwright render-QA at 1600x900**: 13/13 PASS — no overflow, no scroll-overflow, no element overlaps; sponsor order verified Heritage@2 Herald@10.
5. **5 news-segment images downloaded**: s1-jalapeno-chip.jpg, s2-qwen-architecture.png, s3-headlong-loop.svg, s4-portable-computer.png (Chrome screenshot, Cloudflare fallback), s5-figure-pipeline.png.

## Validator evidence (verbatim from qa/validate_deck.py)

```
PASS: slide-ID parity (13 slides <-> notes)
PASS: JS syntax (node --check -)
PASS: no autoplay
PASS: 19 clickable source links
PASS: final Sources slide present
PASS: close-slide Discord QR (assets/socials/weeklyclaw-discord-qr.png -> weeklyclaw.ai/discord)
PASS: theme markers: ['cream_paper', 'teal_cyan', 'weeklyclaw_logo_symbol', 'barlow_condensed', 'ibm_plex_mono']
PASS: 10 local media paths resolved
PASS: segment IDs found: ['openai-stack', 'qwen-flash-next', 'headlong', 'portable-computer', 'robot-data']
PASS: CSS custom properties match authority deck (15 checked)
PASS: SVG symbols match authority deck (['weeklyclaw-logo'])
PASS: no invented brand/logo symbols
PASS: core layout classes present (16 checked)
PASS: 3 sponsor assets resolved and provenance-checked
PASS: deck size 48558 bytes (authority: 50282 bytes)
=== ALL CHECKS PASSED ===
```

## Render-QA evidence (verbatim from qa/render_qa_rev2.py)

```
NEW_DECK_SLIDES=13 ids=['s-title', 's-cold-open', 's-sponsor-heritage', 's-seg-openai-stack', 's-seg-qwen-flash-next', 's-seg-headlong', 's-seg-portable-computer', 's-seg-robot-data', 's-signal-outside', 's-hot-take', 's-sponsor-herald', 's-watch', 's-sources']
NEW_RENDER_QA PASS bad_slides=0
  [s-title                         ] ok
  [s-cold-open                     ] ok
  [s-sponsor-heritage              ] ok
  [s-seg-openai-stack              ] ok
  [s-seg-qwen-flash-next           ] ok
  [s-seg-headlong                  ] ok
  [s-seg-portable-computer         ] ok
  [s-seg-robot-data                ] ok
  [s-signal-outside                ] ok
  [s-hot-take                      ] ok
  [s-sponsor-herald                ] ok
  [s-watch                         ] ok
  [s-sources                       ] ok
SPONSOR_ORDER_OK: heritage@2 herald@10
=== RENDER-QA PASS (rev2) ===
```

13 PNG screenshots at qa/render-1600x900-rev2/, all 1600x900, all RGB color span ≥ 657.

## Slide ID set (Ep 27 rev2 vs Ep 26 authority)

| Slot | Ep 27 rev2 | Ep 26 authority |
|------|-----------|-----------------|
| 1    | s-title   | s-title |
| 2    | s-cold-open | s-cold-open |
| 3    | **s-sponsor-heritage** | s-sponsor-herald (Ep 27 inverts sponsor rotation) |
| 4    | s-seg-openai-stack | s-seg-faraday |
| 5    | s-seg-qwen-flash-next | s-seg-speed |
| 6    | s-seg-headlong | s-seg-stripe-openrouter |
| 7    | s-seg-portable-computer | s-seg-deepseek |
| 8    | s-seg-robot-data | s-seg-agent-payments |
| 9    | s-signal-outside | s-signal-outside |
| 10   | s-hot-take | s-hot-take |
| 11   | **s-sponsor-herald** | s-sponsor-heritage |
| 12   | s-watch | s-watch |
| 13   | s-sources | s-sources |

Slide-ID parity: 13 new ↔ 13 Ep 26. Sponsor slots swapped in correct order. Five segment IDs replaced with Ep 27 story names.

## Standing rules applied

- standing-ownership-henry-news-2026-08-20: all 5 segments are Henry-led.
- close-recap-once-andy-2026-08-21: Andy's close prose recaps once, never re-recaps.
- news-window-airtime-2026-08-21: every selected story's primary launch receipt landed after Ep 26 airtime (2026-08-21 20:00 UTC).
- live-artifact-rule-2026-08-21: every news slide has a clickable live URL.
- launch-pattern-news-titles-2026-08-21: titles are launch-publisher-formatted (not editorialized).
- no-scaffolding-kickers-on-news-slides-2026-08-21: no "Story 1:" kicker labels on news segments.
- discord-qr-last-slide-2026-08-23: QR card is on the close slide, anchored to weeklyclaw.ai/discord (rotating invite route).
- template-authority-clone-prior-approved: deck head/SVG/script cloned from Ep 26 authority verbatim; no invented theme.

## Awaiting human action

- Telegram review card sent to topic `-1004370723812:17` at 2026-08-27 16:13 EDT.
- Henry's APPROVE/SWAP/DROP/PIN/ORDER reply in the Telegram review card.
- Standing-authorized draft publication: **COMPLETE** (commit `46a4c1b` pushed to `origin/main`, all three URLs HTTP 200, sponsor-order byte check PASS, asset SHA-256 byte-match verified on s1-jalapeno-chip.jpg).
- After APPROVE, the publication runbook (`scripts/sync-weeklyclaw-archive.py --commit --push`) handles the gallery + homepage atomic update. This REFRESH tick deliberately did NOT touch `episodes/index.html` or `index.html` per the skill's draft-vs-full-publication separation.
