# Ep 27 rev2 — Runlog (12:00 EDT REFRESH tick, 2026-08-27)

**Tick:** 27-2026-08-27-12 (REFRESH)
**Operator:** Ada (cron)
**Started:** 2026-08-27 16:00 EDT
**Completed:** 2026-08-27 16:11 EDT
**Selected revision:** rev2 (supersedes rev1)

## Chronological actions

1. **Lock acquisition**: wrote PID to `showprep/state.lock` at 16:00 EDT.
2. **Inspection**: read `agenda.rev1.md`, `host-cheat-sheet.rev1.md`, `speaker-notes.rev1.md`, `henry-section.rev1.md`, `andy-section.rev1.md`, `talking-points.rev1.md`. Found all 6 had Herald-first sponsor order, contradicting the standing rotation rule (Ep 27 must invert Ep 26).
3. **Material rebuild decision**: rev2 will swap sponsor order (Heritage → Herald) across all 6 host-facing artifacts and the deck.
4. **Authority deck**: located at `episodes/27/showprep/qa/authority-deck-ep26.html` (50,282 bytes, Ep 26 baseline).
5. **Built deck builder script**: `revs/build_deck.py` clones Ep 26 head/style/SVG/script verbatim and replaces slide bodies with Ep 27 content.
6. **Wrote `_slides_content.rev2.html`** with all 13 slide bodies:
   - s-title (Ep 27 branding, sponsor logo row Heritage first)
   - s-cold-open (5-step arc-wrap, three hook rows)
   - **s-sponsor-heritage** (Heritage first per inversion)
   - s-seg-openai-stack, s-seg-qwen-flash-next, s-seg-headlong, s-seg-portable-computer, s-seg-robot-data
   - s-signal-outside (Codex virtual-office)
   - s-hot-take (deployment layer)
   - **s-sponsor-herald** (Herald second per inversion)
   - s-watch (three callouts + Discord QR card)
   - s-sources (all 5 segments + Signal + Hot Take links)
7. **Ran build_deck.py**: WROTE deck.rev2.html (48,570 bytes), NODE_CHECK_PASS, SLIDE_COUNT=13.
8. **Symlink**: `revs/assets -> ../assets` so validator local-media-resolution gate works.
9. **Image downloads**:
   - s1-jalapeno-chip.jpg (460KB, OpenAI CDN, HTTP 200)
   - s2-qwen-architecture.png (572KB, Aliyun OSS, HTTP 200)
   - s3-headlong-loop.svg (19KB, laude.org, HTTP 200)
   - s4-portable-computer.png (40KB, Chrome headless screenshot — perplexity.ai is Cloudflare-protected, fallback to capture)
   - s5-figure-pipeline.png (120KB, Figure CDN, HTTP 200 — first attempt hit wrong hostname `qx5k1y1u9drj` not `qx5k8y1u9drj`; corrected)
10. **Validated all 5 images** with PIL: full RGB span (≥ 657), correct dimensions.
11. **Wrote all 6 rev2 host-facing artifacts** with corrected sponsor order.
12. **Copied validator**: `cp /home/henrymascot/.hermes/skills/operations/weeklyclaw-show-prep/scripts/validate_deck.py qa/`.
13. **Ran validate_deck.py**: ALL CHECKS PASSED (14 PASS lines, deck size 48,558 bytes vs authority 50,282 bytes).
14. **Wrote render-QA script** `qa/render_qa_rev2.py` using Playwright + system Chrome (playwright bundled chromium was missing; used `/usr/bin/google-chrome`).
15. **Ran render-QA**: 13/13 PASS at 1600x900, no overflow, no overlap, no scroll-overflow. Sponsor order verified Heritage@2 Herald@10.
16. **Generated 13 PNG screenshots** at `qa/render-1600x900-rev2/` — all 1600x900, all RGB color span ≥ 657.
17. **Updated state.json**: added rev2 entry, marked rev1 as superseded, updated completion_evidence to 7/7 with validation_passed=true.
18. **Wrote evidence-rev2.md** and **runlog-rev2.md** (this file).

## Final state

- 7/7 artifacts complete and validated.
- Deck PASSES both structural (validate_deck.py) and visual (Playwright render-QA).
- Sponsor rotation correctly applied: Heritage opens (slide 3), Herald closes (slide 11).
- approval_state: UNVALIDATED — awaiting Henry's APPROVE in Telegram review card to flip to APPROVED.
- Standing-authorized draft publication to weeklyclaw.ai still deferred (repo not on this host).

## Outstanding

- Henry's APPROVE/SWAP/DROP/PIN/ORDER reply in Telegram review card.
- Standing-authorized website draft publication (deferred: /home/henrymascot/clawd/projects/weeklyclaw-ai not on Ada VM).
