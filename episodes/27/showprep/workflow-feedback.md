# WeeklyClaw Episode 27 — Workflow Feedback (rev2)

## 2026-08-27 12:00 EDT — REFRESH tick — material rebuild to rev2

The Thursday 12:00 EDT REFRESH tick produced a material rebuild (rev1 → rev2).
Justified by the deferred lint debt noted in rev1's workflow-feedback: the
11:00 BUILD shipped a Herald-first sponsor order that violated the standing
weekly rotation rule (Ep 27 must invert Ep 26, i.e., Heritage → Herald). Rev1
also did not produce deck.html. The skill's no-change-refresh recipe says
unsolicited REFRESH rebuilds are normally suppressed, but a sponsor-order
inversion on a draft that would ship to weeklyclaw.ai is a larger drift than
waiting for the next host trigger — the fix had to land before the standing
draft publication, otherwise the live draft would have been Herald-first.

Rev2 fix list (all verified):

- Sponsor rotation corrected across all 6 host-facing artifacts and the
  deck. **Heritage opens** (slide 3, after cold open); **Herald closes**
  (slide 11, after hot take).
- Deck.rev2.html produced (13 slides, 48,570 B) by cloning Ep 26 authority
  head/SVG/script verbatim. No invented theme (Ep 24 lesson applied).
- 5 news-segment images downloaded and validated:
  - s1-jalapeno-chip.jpg (OpenAI CDN)
  - s2-qwen-architecture.png (Aliyun OSS)
  - s3-headlong-loop.svg (laude.org)
  - s4-portable-computer.png (headless Chrome screenshot — perplexity.ai
    is Cloudflare-protected; LIVE link in deck still points to product page)
  - s5-figure-pipeline.png (Figure CDN)
- Validate_deck.py against Ep 26 authority: ALL CHECKS PASSED (14/14).
- Playwright render-QA at 1600x900: 13/13 PASS — no overflow, no overlap,
  no scroll-overflow.
- Standing-authorized draft publication: SUCCESS.
  - Worktree on Enterprise, branch `ada/draft-publication-1787847347`.
  - Commit `46a4c1b` pushed to `origin/main`.
  - Vercel deploy verified: 3 URLs HTTP 200 (deck / agenda-draft / host-cheat-sheet).
  - Sponsor-order byte check on live deck: Heritage@19682 < Herald@19862.
  - Asset SHA-256 byte-match verified on s1-jalapeno-chip.jpg.

## 2026-08-27 12:00 EDT — Outstanding / awaiting host

- Telegram review card sent to topic `-1004370723812:17`.
- Awaiting Henry's APPROVE / SWAP / DROP / PIN / ORDER reply.
- After APPROVE, the publication runbook promotes Ep 27 to gallery +
  homepage via `scripts/sync-weeklyclaw-archive.py --commit --push`.

## Standing rules (still applied)

- Henry leads every What Happened This Week segment.
- Close recap exactly once; never recap the recap.
- News-window = previous episode airtime (2026-08-21 20:00 UTC).
- Launch-pattern news titles (subject-verb-object).
- Discord QR on the last slide, anchored to weeklyclaw.ai/discord (rotating
  invite route).
- Sponsor rotation inverted vs Ep 26: Heritage → Herald.
- Template authority = Ep 26 (live-fetched).

## Host reply commands

Reply in originating Telegram topic with exactly one of:

- `APPROVE` — lock the lineup as-is, promote at FREEZE.
- `SWAP <slot> <candidate>` — replace Story N with bench candidate.
- `DROP <slot>` — remove Story N from the lineup.
- `PIN <candidate>` — pin Story N against any auto-replacement.
- `ORDER <n1,n2,n3,n4,n5>` — re-sequence the five news segments.

Free-text edits are also accepted; ambiguous changes will be confirmed before applying.
