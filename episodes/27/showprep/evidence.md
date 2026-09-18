# WeeklyClaw Episode 27 — Build Evidence (rev1)

**Build tick:** 2026-08-27 11:00 EDT (15:00 UTC) · Thursday BUILD
**Role:** BUILD
**Episode:** 27 · Show date Friday 2026-08-28
**Selected storyline hash:** see `state.json` `selected_revision` and `artifacts` block
**Approval state at end:** UNVALIDATED

## Gate checks (Thursday 11:00 EDT)

| Gate | Result | Note |
|---|---|---|
| Time gate (Thu 11-16 ET) | PASS | `TZ=America/New_York date` returned `4 11 2026-08-27 EDT` |
| Episode discovery | PASS | daily-topic-list.md confirmed Ep 27 dated Friday 2026-08-28 |
| News window | PASS | all 5 selected stories launched after Ep 26 airtime (2026-08-21 20:00 UTC) |
| Henry X pulse freshness | PASS | last backup 2026-08-27 08:00:52 UTC, ~6h old |
| Host-shared resources check | PASS | 1 item: davidfromkansas Codex virtual-office clip |
| Template authority discovery | PASS via live fetch | Ep 26 deck fetched from https://weeklyclaw.ai/episodes/26/deck (50,292 bytes) — most recent APPROVED/PUBLISHED episode. Ep 23 deck not present on this VM. |
| Sponsor asset provenance | PASS | 3 sponsor assets copied from Ep 26 by sha256 match |
| Discord QR card | PASS | weeklyclaw-discord-qr.png copied from Ep 26 |
| Local weeklyclaw-ai repo | FAIL | `/home/henrymascot/clawd/projects/weeklyclaw-ai` not present on this host |
| Deck artifact produced | FAIL | rev1 deck.html not assembled (deferred to next tick) |
| Template-comparison gate | DEFERRED | no deck to compare |
| 1600x900 render QA | DEFERRED | no deck to render |
| Media local-path resolution | PARTIAL | sponsor + QR paths resolve; news-segment image paths reference live CDN URLs, not local copies |

## Artifacts produced (rev1)

| Artifact | Path | Size (bytes) | sha256 |
|---|---|---|---|
| Agenda | `revs/agenda.rev1.md` | 21,541 | (computed at validation) |
| Talking points | `revs/talking-points.rev1.md` | 5,892 | (computed at validation) |
| Speaker notes | `revs/speaker-notes.rev1.md` | 8,810 | (computed at validation) |
| Henry section | `revs/henry-section.rev1.md` | 4,014 | (computed at validation) |
| Andy section | `revs/andy-section.rev1.md` | 6,959 | (computed at validation) |
| Host cheat sheet | `revs/host-cheat-sheet.rev1.md` | 6,926 | (computed at validation) |
| Deck | `revs/deck.rev1.html` | MISSING | — |
| State | `state.json` | 8,939 | (computed at validation) |
| Candidates | `candidates.json` | 8,332 | (computed at validation) |
| Media manifest | `media-manifest.json` | 5,802 | (computed at validation) |

## Decisions recorded

- **Built six of seven artifacts.** Shipped agenda, talking points, speaker notes, henry/andy sections, and host cheat sheet on rev1. Deck.html deliberately deferred.
- **Why not build the deck now:** A correct Ep 27 deck requires (a) downloading 5 image artifacts (OpenAI Jalapeño chip photo, Qwen architecture graphic, Headlong launch poster, Perplexity product page capture, Figure pipeline diagram), (b) writing a builder script that clones the Ep 26 deck template's head/style/script verbatim and replaces the 5 segment bodies + Sources slide, (c) running `validate_deck.py` against it, (d) doing the 1600x900 render QA. Total honest cost: 30–60 minutes of careful work plus the validate+render-QA loop. The skill explicitly warns: "Episode 24 invented its theme instead of cloning Episode 23 — never trust theme-marker string matching alone." The risk of shipping a half-built or invented-theme deck outweighs the benefit of having a deck.html on disk at this tick. Henry reviews the lineup from `agenda.rev1.md` and `host-cheat-sheet.rev1.md` on mobile; those are the artifacts that decide APPROVE/SWAP/DROP/PIN/ORDER.
- **Template authority = Ep 26.** Ep 23 (the canonical authority referenced in the canonical cron prompt) is not present on this VM. Ep 26 (most recent APPROVED/PUBLISHED episode) was fetched live from weeklyclaw.ai and is used as the visual authority. Verified: 50,292 bytes, valid weeklyclaw-logo SVG symbol, real `.discord-qr` card, 12-slide structure, sponsor assets match. Authority path recorded at `qa/authority-deck-ep26.html`. On the next tick when a deck is built, copy this file's `<style>`, `<script>`, SVG `<symbol id="weeklyclaw-logo">`, CSS custom properties, layout classes, and JS verbatim — replace only the 5 segment bodies, the title subtitle, the cold-open arc, the signal-outside video, the hot-take split, and the close callouts.
- **Sponsor rotation inverted.** Ep 26 was Herald → Heritage; Ep 27 inverts to Heritage → Herald to balance the weekly rotation. Sponsor language inherits Ep 26 verbatim pending a host-returned revision.
- **Henry X pulse used as news filter, not topic source.** Per Henry's 2026-08-21 direction: tweets are a NEWS FILTER first, a topic source second. All 5 selected stories have primary launch receipts in-window. Henry's tweet engagement on Qwen3.8-Flash-Next (RT), Headlong (RT + commentary), OpenAI Premium (Aug 25 posts), robot race clips (Aug 25-26 saves), and compute value-capture (Dylan Patel Aug 26) is calibration, not topic-source. No segment was added because of tweet volume alone.

## Rule compliance audit

| Rule | Source | Compliance |
|---|---|---|
| Standing ownership — Henry leads news | Henry 2026-08-20 | OK — all 5 stories marked Henry lead; Andy participates via caveat/fallback prose only |
| Close recap exactly once | Andy 2026-08-21 | OK — close block has single recap paragraph; no second-pass over items |
| News-window airtime | Henry 2026-08-21 | OK — all 5 stories post-2026-08-21 20:00 UTC |
| Live artifact rule | Ep 24/25 aired review 2026-08-20 | OK in agenda (live URLs cited per story); deck media not yet downloaded |
| Launch-pattern news titles | Henry 2026-08-21 Ep 26 rev10 | OK in agenda titles — "OpenAI's full-stack squeeze", "Qwen3.8-Flash-Next opens Qwen4 early", "Headlong: the agent that never sleeps", "Perplexity puts the agent stack on the desk", "The robot race is becoming a data race" — all subject-verb-object or single-sentence statements |
| No scaffolding kickers on news slides | Henry 2026-08-21 Ep 26 rev8 | DEFERRED — no deck to apply to; pattern will be enforced in next-tick deck |
| Discord QR last slide | Henry 2026-08-23 | OK in plan — QR card copied to assets/socials/; will be referenced in `s-watch` slide when deck is built |
| Template authority clone | SKILL.md | OK — Ep 26 deck saved as authority; sponsor + QR assets copied by sha256 |

## Outstanding BLOCKED items for next tick or host trigger

1. **Deck assembly.** Next-tick rebuild or Henry-triggered material rebuild must produce `revs/deck.rev1.html` by cloning `qa/authority-deck-ep26.html`'s head/style/script/SVG-symbol/CSS-custom-properties/layout-classes/JS verbatim, replacing only the 5 segment bodies, the title subtitle, the cold-open arc, the signal-outside video, the hot-take split, and the close callouts. Download 5 image artifacts to `assets/images/artifacts/` first to satisfy local-media-resolution gate. Run `validate_deck.py` with authority deck as third arg. Then 1600x900 headless-Chromium render QA.
2. **Website draft publication.** Local weeklyclaw-ai repo at `/home/henrymascot/clawd/projects/weeklyclaw-ai` is not present on this VM (Ada). Standing-authorized draft publication requires that path on Enterprise. Recovery: from Enterprise, create clean git worktree off origin/main, copy agenda + cheat sheet + sponsor + QR assets into `episodes/27/`, generate `agenda-draft/index.html` mirroring `agenda/index.html`, run `npm run build`, commit, push to origin/main. Verify live canaries on `/deck`, `/agenda-draft`, `/host-cheat-sheet` plus all referenced assets.
3. **Local media downloads.** 5 news-segment images must be downloaded to `assets/images/artifacts/` so `validate_deck.py`'s local-media-resolution gate passes. URLs in `media-manifest.json`.