---
name: weeklyclaw-show-prep
description: "Use for scheduled WeeklyClaw live-show preparation."
version: 2.0.0
metadata:
  emoji: "🦞"
  category: operations
---

# WeeklyClaw Show Prep

Prepare a Friday WeeklyClaw episode as a reviewable, reversible draft. This skill covers discovery, source verification, story selection, agenda/deck/notes generation, validation, review-card delivery, refreshes, freeze, and handoff. It does not publish publicly or overwrite canonical episode files before approval.

## Scope and boundaries

- Workspace: `~/weeklyclaw`.
- Work only under `episodes/<N>/showprep/` until approval. Read prior episodes; never modify them.
- Never touch the separate SuperAda/OpenClaw changelog workspace.
- No public YouTube, X, Bilibili, Discord (outside lifecycle authority), guest, sponsor, purchase, or production write without explicit approval.
- When Henry or Andy explicitly authorizes episode publication, completion covers the full episode on **YouTube, native X video, and Bilibili**. Follow `references/multi-platform-episode-publication.md`; YouTube-only publication is partial progress.
- **Website draft publication is a standing authorized action**: on every BUILD that produces a passing package, publish the deck draft to the WeeklyClaw website repo (`~/clawd/projects/weeklyclaw-ai`) under `episodes/<N>/`. This is an internal deploy to a site Henry controls, not an external publication.
- Never modify the cron definition from the show-prep job.

## Draft publication to weeklyclaw.ai (standing authority)

On every BUILD with a passing seven-artifact package:

1. Create a clean git worktree off `origin/main` of the website repo. Before any build, staging, commit, or push, assert that `git rev-parse --show-toplevel` equals the new worktree path. Use `git -C "$worktree" ...` or `cd "$worktree"` inside the same shell command; setting the tool's working directory to the canonical checkout is not enough.
2. Copy only the current deck revision, agenda, host docs, and referenced assets into `episodes/<N>/`. Stage an explicit whitelist; never run `git add episodes/<N>/` from a dirty canonical checkout, because it can publish the private `showprep/` tree and unrelated untracked files.
3. Generate both the canonical archive-compatible agenda page and a directly accessible draft route at `episodes/<N>/agenda-draft/index.html`. The site's `/episodes/<N>/agenda` redirect points to the gallery, where an unapproved draft is intentionally absent, so it is not a discoverable draft-agenda link.
4. Run `npm run build` from the asserted worktree.
5. Commit and push to `origin/main`. Vercel auto-deploys.
6. Verify the exact live deck, agenda-draft, host-cheat-sheet, and representative asset URLs with HTTP 200 plus decoded content canaries. For ordered content such as sponsor slots, prove both canaries and their byte/DOM order (record the byte offset of each sponsor's first occurrence; assert Herald byte offset < Heritage byte offset on a Herald-first week, the reverse on a Heritage-first week).
7. Include clickable links for `https://weeklyclaw.ai/episodes/<N>/deck`, `https://weeklyclaw.ai/episodes/<N>/agenda-draft`, and `https://weeklyclaw.ai/episodes/<N>/host-cheat-sheet` in the BUILD message to this Telegram topic.
8. **HARD GATE (Henry, 2026-08-28): every weekly-content message — BUILD review card, material-rev report, FREEZE, HANDOFF, draft-publication report — MUST also include the WeeklyClaw Program Topics spreadsheet link** (sync it first if the lineup changed: append candidates to `episodes/<N>/daily-topic-list.md` matching the `- **Score:**` block format with `^### Candidate \d+` headings, run `python3 scripts/weeklyclaw-program-sheet.py`, verify via the public CSV export). Sheet: https://docs.google.com/spreadsheets/d/16xAvCzRGA8XlWvihdSBcipw0wARzVZT9YysXzM0eFM8/edit . A content delivery without the sheet link is an incomplete delivery.

On material deck rebuilds (new revision from REFRESH/FREEZE), republish using the same route.

On Henry/Andy APPROVE, the [publication runbook](references/publication-runbook.md) takes over: promote canonical root artifacts, update the episode gallery card from "Draft" to the final state, update the homepage featured episode, run the full sync script, and verify live URLs with content canaries.

**Draft-publication self-check on every REFRESH tick after BUILD.** Standing-authorized website publication is part of the BUILD contract, not optional. On the first REFRESH tick after a BUILD that produced a passing package, BEFORE claiming "no action," run this check:

```bash
for url in /deck /agenda-draft /host-cheat-sheet; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "https://weeklyclaw.ai/episodes/<N>$url")
  if [ "$code" != "200" ]; then missing="$missing $url"; fi
done
```

If any URL is missing, the BUILD skipped the standing-authorized draft publication. Repair it during this REFRESH tick (worktree → whitelist copy → agenda/host page generation → `npm run build` → commit → push → live canary verification) and record the recovery in `state.json.draft_publication` and `runlog.md`. Do NOT silently emit "no action" when the standing-authorized draft is missing — that is a contract failure, not a clean tick. Verified on Episode 26 Thursday 14 ET REFRESH after the 12 ET BUILD shipped rev1 PASS without pushing.

## Authoritative deck template (prior APPROVED episode)

- The canonical visual/layout template for a new episode is the **prior APPROVED episode deck**, discovered at BUILD by scanning `episodes/*/showprep/state.json` for the highest episode whose `approval_state` is `APPROVED` with a non-empty root `episodes/<N>/deck.html`. Record the authority path, episode number, and sha256 in evidence.md. As of this skill the authority is Episode 23: `~/weeklyclaw/episodes/23/deck.html` (sha256 `3548178052bb0c8e151b61ca230930885af8b7b3016072de1bfaa38aea598785`). Henry may explicitly name a replacement; absent that instruction, use the prior APPROVED episode.
- Copy the authority deck's full `<style>` block, `<script>` block, SVG `<symbol>`/`<defs>` (including the real `<symbol id="weeklyclaw-logo">`), CSS custom properties, layout classes, and navigation/fullscreen JS **verbatim**. Replace episode-specific content only. Do not invent new CSS class systems, new SVG symbols, new brand marks, or new logo paths.
- The WeeklyClaw logo is the `<symbol id="weeklyclaw-logo">` SVG inside the authority deck, referenced via `<use href="#weeklyclaw-logo"/>`. Any `<symbol>`, `<path>`, or inline SVG that draws a claw/logo/brand mark not present in the authority deck is an invention and fails the build.
- Do NOT use `~/clawd/projects/weeklyclaw-ai/episodes/22/deck-website-theme.html` as a template. That file is the former dark/neon theme Henry explicitly rejected during Episode 23 prep. It is retained for history only.
- Copy the prior episode's `assets/sponsors/` directory into the new showprep asset tree verbatim. Every sponsor `<img>` `src` must resolve to a file on disk whose sha256 matches the prior-episode sponsor asset. Sponsor marks are real brand assets, not invented inline icons.
- Theme traits inherited from Episode 23: light cream paper background (`--site-paper`), fine grid, teal/cyan accents (`--claw-red: #2a7e6b`), Barlow Condensed display type, IBM Plex Mono utility type, rounded editorial cards, the real `weeklyclaw-logo` SVG symbol, `claw-bg` background watermark, `glow-orb` accents, and `part-label`/`story-num` section markers.
- Read `references/prior-episode-template-authority.md` for the full deterministic template-comparison and render-QA gate recipe before any BUILD or material deck rebuild.

## Time gate and roles

Run the New York gate first:

```bash
TZ=America/New_York date '+%u %H %Y-%m-%d %Z'
```

Continue only on Thursday (4) or Friday (5) during hours 11–16 ET:

- Thursday 11: BUILD: discover the episode for TOMORROW's Friday show, research, select stories, build the full draft package a day early.
- Thursday 12–15: REFRESH: inspect only changes since the last successful tick and apply explicit feedback.
- Friday 11–14: REFRESH (late-news check): additive-first — verify developments since the last successful tick; prefer ADD (new segment, bench promotion, One To Watch upgrade) over rewriting the built lineup; never silently swap an approved or pinned story.
- Friday 15: FREEZE: final verification and lock current package; late stories become One To Watch unless exceptional.
- Friday 16: HANDOFF: read-only, maximum 12 lines, no regeneration.

Outside that window, return exactly `NO_REPLY` without taking a lock or changing files.

## Episode discovery and locking

1. Determine the active Friday episode from show dates, never by adding one to the highest existing directory. On the Thursday BUILD tick, the target show date is TOMORROW's New York Friday; on Friday ticks it is today. Inspect numeric episode `showprep/state.json`, `daily-topic-list.md`, and `agenda.md` for `show_date_ny` or `Show date`. If an episode is dated for the target show date, resume it. Otherwise choose exactly one more than the highest episode whose show date is earlier than that Friday. A pre-existing directory created by daily intelligence is the upcoming episode intake, not evidence to skip another number.
2. If today's New York date already exists in `showprep/state.json`, resume that episode. Never assign a second episode for the same show date.
3. Recovery bootstrap: any Thursday or Friday 11:00–14:00 tick without valid same-week state performs full BUILD. At Friday 15:00 without state, do a bounded abbreviated build-and-freeze only if it can pass; otherwise deliver BLOCKED. At Friday 16:00 without a usable package, deliver a read-only BLOCKED handoff.
4. Cross-check the selected episode's intended show date and the prior agenda's stated next-show date. If evidence disagrees with today, record a concise BLOCKED card instead of guessing.
5. Acquire `showprep/state.lock` atomically before writes. Lock expiry must be shorter than the hourly cadence; heartbeat long Cursor runs so healthy work remains fresh. A fresh lock means quiet exit. Recover stale locks and record why.
6. Make reruns idempotent by using a tick ID `<episode>-<NY date>-<NY hour>` and checking persisted state before duplicating artifacts or messages.
7. Remove the lock after the run, including blocked or failed paths where safe.

## Research and story selection

- Before scoring the raw candidate pool, check the active episode for a finished, ordered host document: talking-points file, run-of-show, host agenda, or equivalent. If one exists, it is authoritative for selection, order, lines, questions, and ownership. Use it directly. Score the raw pool only to fill gaps the host did not cover, or when no finished host document exists. Record the authoritative path and any gap-filling decisions.
- Treat the week's verified daily program-intelligence output as a raw candidate pool subordinate to a finished host document. When no finished host document exists, prefer that pool and add only a focused gap sweep of primary sources and credible independent reporting.
- Before research or drafting, inspect the originating WeeklyClaw Telegram topic and active episode files for links, posts, videos, demos, screenshots, or documents shared by Henry or Andy. Host-shared resources are authoritative editorial inputs: preserve every exact URL in a dedicated `sources/host-shared-resources.md` ledger, associate each with its segment, retrieve/read it where tooling permits, and carry it into the agenda's `Sources and production notes`, slide-by-slide speaker notes, and a clickable deck Sources/Host Resources appendix. Never silently replace, omit, or "improve away" a host-shared link. Host-shared resources do not waive fact-checking: classify official/primary sources separately from community commentary, corroborate material factual claims, and label unresolved claims.
- For each selected topic, find equivalent presenter resources even when hosts supplied none: at least one primary/official receipt plus one useful visual, demo, video, or credible practitioner discussion when available. Record direct URL, creator/account, what it demonstrates, source tier, retrieval result, presenter use, cue/timestamp for video, and fallback. If no useful equivalent exists after materially different searches, record the failed searches rather than inventing one.
- Keep a source ledger per story with URL, retrieval time, source tier, claims, caveats, and verification status.
- Score candidates 0–10 using consequence/industry shift (25%), Henry/operator angle (20%), evidence quality (20%), novelty (15%), narrative connection (10%), and clip-ability (10%).
- Target up to five segments at >=8.5. Five is a target, not a padding quota. If only three or four qualify, select those, enlarge the bench, and state the shorter lineup on the review card. A lower-scoring story remains bench-only unless Henry explicitly promotes it.
- **Henry's X signal is a NEWS FILTER first, a topic source second (Henry, 2026-08-21: "The idea is not to use all tweets but only breaking news topics for the week").** Before scoring, read the tweet backup at `~/weeklyclaw/sources/henry-tweets/` (per-day `YYYY-MM-DD.jsonl`, canonical `all.jsonl`, refreshed every 4h by the `henry-tweets-daily-backup` cron, job `12c370604fd7`). From his week's tweets, extract only launch-grade news (new model/chip/product releases, first-ever facts, confirmed deals) that broke inside the episode window; his topic volume, opinion posts, and engagement counts calibrate ordering and the Henry-section, but NEVER add a segment for a topic he tweeted heavily if the underlying launch is not this-week news (Qwen3.8-27B, Grok Bot, GLM-5.3, Ultrafast were all correctly excluded from Episode 26 despite heavy tweeting). Direct posts/quote commentary outrank bare reposts for ordering only. On backup staleness (>24h), fall back to `BIRD_ACCOUNT=henry ~/clawd/scripts/bird-env.sh user-tweets iAmHenryMascot -n 40 --json` and mark `HENRY_X_PULSE_INCOMPLETE` on failure.
- **Episode news window = previous episode AIRTIME, not the last daily-intake completion (Henry, 2026-08-21: "did anything happen on it this week?").** A story qualifies for episode N only if its primary launch receipt landed AFTER episode N-1 aired (Friday 16:00 ET / 20:00 UTC). The daily-intelligence freshness cutoff is the Friday ~09:05 EDT intake completion, which finishes pre-show — so a Friday-morning launch (e.g. Qwen3.8-2.4T posted Aug 14 15:02 UTC, ~5h before Episode 25 aired) wrongly gets promoted as next-episode news. When scoring a candidate, compare its launch timestamp against the PRIOR EPISODE'S AIRTIME, not against the last intake cursor. Follow-on developments of an aired story (community quants, demand metrics, new variant routes) are supporting color at most, never a fresh segment.
- Deduplicate against the week's lists and the last three aired editions, INCLUDING Henry's tweeted topics already covered on a prior episode — a follow-on development is news, a re-tread of last week's release is not (e.g. Qwen3.8-27B weights aired on Episode 25; only a genuinely new release qualifies again). Merge related developments when they share an entity or causal thread and can land cleanly in about five minutes; each cluster names its umbrella thesis, sub-stories, narrative order, shared landing line, and one host question, rescored as one editorial unit while preserving constituent scores. Each constituent belongs to one selected cluster unless an explicit cross-reference explains the overlap.
- Treat release ecosystems as evidence layers, not separate filler stories: Hugging Face model cards, files, licenses, quantizations, demos, and deployment recipes should deepen the relevant model-launch cluster unless they create a materially different audience takeaway.
- Require two independent receipts for aired factual claims where possible. If the first corroboration search fails, retry with materially different terms, entity names, date ranges, and source types before excluding the claim; record the retries and result. Label vendor-reported figures. Never turn a secondary comparison into a primary receipt.
- For video/image launches, find official playable examples and record creator, direct URL, cue/timestamps, poster/fallback, provenance, and embedding/rights status. For language/reasoning model comparisons, build sourced tables covering architecture/active parameters, context, modality, license/weights, benchmark source, API price, quantization, hardware/runtime claims, and caveats; unknown cells stay unknown.
- Sequence by a named narrative arc, not raw score order. Mark the first optional cut.

## Draft package

Create only under `episodes/<N>/showprep/`:

- `state.json`, `candidates.json`, `candidates.md`
- `sources/<slug>.md`
- `revs/agenda.rev<N>.md`, `deck.rev<N>.html`, `talking-points.rev<N>.md`, `speaker-notes.rev<N>.md`, `henry-section.rev<N>.md`, `andy-section.rev<N>.md`, `host-cheat-sheet.rev<N>.md`
- `assets/images/`, `assets/videos/`, `media-manifest.json`
- `workflow-feedback.md`, `evidence.md`, append-only `runlog.md`
- A concise review card with exact commands: `APPROVE`, `SWAP <slot> <candidate>`, `DROP <slot>`, `PIN <candidate>`, `ORDER ...`, or free text.

## Agenda talk-track contract

- **Standing ownership rule (Henry, 2026-08-20): What Happened This Week segments are ALWAYS Henry-led.** Never assign Andy the lead on a news segment and never rotate/flip segment leads between rebuilds. Andy participates via caveat, support angle, or fallback prose only, unless Henry explicitly assigns him a lead for a specific segment in that episode. The rule is recorded in `template.md`, the cron prompt, and here; a revision that marks a What Happened This Week segment "Andy lead" (Episode 26 rev1 did exactly this on S2/S4) fails host-format lint and must be reassigned at the next revision.

- **Close recap rule (Andy, 2026-08-21): recap the episode exactly ONCE at the end of the show; never recap the recap.** Applies to close scripts, host cheat sheets, and any end-of-show copy drafted from the show. A close section that re-summarizes items already covered in the recap, or a cheat sheet whose end-of-show block repeats the recap, fails host-format lint. Recorded in `template.md`, `templates/agenda-template.md`, the cron prompt, and here.

- Read `~/weeklyclaw/template.md` before generating any agenda revision. The packaged baseline is `templates/agenda-template.md`; if the workspace copy is absent or intentionally refreshed, seed/reconcile it from that template rather than inventing a new structure.
- Match each host's working style. Henry gets concise segment/talking-point bullets, an optional landing line, and a handoff cue. Never force a word-for-word Henry script.
- Andy gets a complete natural fallback talk track wherever he participates, followed by the handoff cue. It is a safety net he may paraphrase, not a requirement to read verbatim.
- General segment bullets may precede the host material. Do not duplicate them verbatim in Andy's fallback prose, and do not force rigid alternating-speaker dialogue where the run of show does not need it.
- Integrate verified facts, caveats, transitions, host questions, landing lines, and video talk content into the appropriate bullets or Andy fallback prose.
- Video research should contribute its talk content directly to the relevant section. If it lacks a usable talk-track, write one from verified evidence rather than assuming it exists.
- Keep target runtime at 32–38 minutes and hard stop at 45 minutes. Signal From Outside is the permanent weekly video-review anchor; cut or compress the optional rotating block first.

Use the authoritative deck template described above (prior APPROVED episode). The default shape is cold open, first sponsor read, up to five story segments, **Signal From Outside / weekly video review**, one optional rotating block, hot take, second sponsor read, close, and a non-air build reference. **Sponsor position is a weekly rotation, not a permanent Herald-first layout:** inspect the prior aired/approved episode's two sponsor slots and invert them for the current episode unless Henry or Andy specifies a different order. Apply the same order to the deck, agenda, speaker notes, talking points, Henry view, Andy view, and host cheat sheet, while preserving the latest approved sponsor language until a host returns revised copy. Reserve Hot Take before drafting news and verify that its proposition, framing, and question do not repeat a news segment; replace or omit it if they do. Signal From Outside is a permanent weekly anchor, not part of the rotation. The optional rotating block may be Tool Fight, Builder Demo, or Audience Question. Target 32–38 minutes and a 45-minute hard stop; cut or compress the optional rotating block before cutting the video anchor.

## Mandatory build route (Cursor) and the documented direct-Hermes alternative

The default route is to run Cursor on Enterprise, which derives the six
presentation/host views from the immutable agenda revision. Stage a bounded
run directory at:

`~ent/Services/WeeklyClawDeckBuilder/runs/<show-date>-ep<N>/`

Copy only the canonical agenda revision, source receipts, media manifest, authoritative theme, and required prior references into `input/`. Record the agenda revision/story-set hash before Cursor starts. Run non-interactively with:

```text
--print --output-format json --model <exact-id> --force --trust
```

Try exactly this order:

1. `kimi-k3-high`
2. `claude-opus-5-high`
3. `gpt-5.6-sol-high`

A model is not successful because Cursor exited 0. It must create every required derived artifact, produce valid HTML, preserve source/visual sections, and pass local readback/validation. If a model hangs or returns a partial set, record the attempted model, exit/timeout, produced artifact list, hashes when available, and precise fallback reason before moving to the next route. Never call partial output a success. If every route fails, deliver the verified agenda and any valid notes/cheat-sheet artifacts, mark the deck BLOCKED, preserve evidence, and name the exact missing contract instead of disappearing.

The complete package contract is seven artifacts: canonical agenda, deck, speaker notes, consolidated talking points, Henry view, Andy view, and host cheat sheet. Cursor must produce the six derived artifacts and a receipt binding them to the staged agenda revision/story-set hash. A route passes only when all seven exist, read back, and agree on revision/story identity; any missing or invalid artifact triggers fallback.

### Direct-Hermes build path (documented alternative)

When ALL of these are true, the seven-artifact package can be authored
directly in Hermes in a single 11:00 BUILD tick without invoking Cursor:

- The deck is ≤ 14 slides with a clear linear arc and uses the prior APPROVED episode's deck as the verbatim template (cream paper, teal-cyan, Barlow Condensed + IBM Plex Mono, real `weeklyclaw-logo` SVG symbol).
- The full package fits in one context window (deck HTML ≤ ~40 KB;
  total package ≤ ~140 KB across all seven files).
- No required visual asset is missing (posters retrievable via
  `yt-dlp --write-thumbnail --convert-thumbnails jpg`; sponsor marks
  copyable from the prior episode's `revs/assets/sponsors/`).

See `references/direct-hermes-build-path.md` for the full recipe, including
the dcg shell-parser workarounds and the `validate_deck.py` invocation. That
reference also documents the recovery BUILD pattern (verified on Episode 26
from a non-existent prior `showprep/` directory), the Henry X pulse
placeholder when X CLIs lack cookies, and the render-script divergence between
the per-frame screenshot-only QA pass and the full Playwright overlap-detection
QA pass required before APPROVE-triggered publication.

## Multimedia and notes contract

- **What Happened This Week slides are visual prompts, not briefing documents.** Use one dominant picture, video, demo, chart, or live webpage per story. On-slide copy is limited to a headline plus zero to two short context lines. No body paragraphs, bullet lists, comparison cards, metadata panels, evidence blocks, or talking points. Put details, caveats, citations, numbers, and presenter guidance in speaker notes.
- Every major story needs a verified visual cue where available: primary-source screenshot, official image, chart, UI, clip cue, or explicit fallback still.
- **Live-artifact rule (EP24/EP25 aired-video review, corrected 2026-08-21): on air the deck is a beat marker; the show is the artifact, and the artifact must dominate the slide.** Each news slide embeds a large real capture or playable video from the primary source plus a discreet `▶ LIVE` link for on-air screen share. Do not put the artifact inside a small "ON-AIR LIVE ARTIFACT" card beside dense copy. Tag artifact `type` in `media-manifest.json` (`LIVE_DEMO | LIVE_CHART | RECEIPT_PAGE | SCREEN_CAPTURE | VIDEO_CLIP`); prefer live over static. Docs-page/text-only artifacts are `WEAK-VISUAL`: propose merge/swap. Capture provenance (URL, UTC time, title verified), use relative paths, no autoplay.
- **Launch-type-aware artifact matching (Henry, 2026-08-21: "if there is a video we should use that, or a demo or a benchmark").** Match the artifact to what the story IS: hardware/chip/product launch → the vendor's official launch video; model release → the benchmark (live leaderboard/chart where possible); feature/deal → live demo, receipt page only as fallback. A receipt-page screenshot is NOT acceptable when an official video, demo, or benchmark exists — search for them BEFORE defaulting to a page capture. Episode 26 rev3 shipped static screenshots on all five news segments and dropped the `▶ LIVE` links; both were violations. See `references/on-slide-live-artifacts.md` §1 for the full preference order and the sourcing recipe (vendor launch videos often live only on the X launch post; launch-post images may BE the benchmark chart — OCR to verify).
- **Media selection hard gates (Henry, 2026-08-28, Ep27 rev3 review — "benchmarks are more important to us than news").** Priority order for every news-slide image: (1) **benchmark/chart comparing the model or chip against peers** — beats ANY article screenshot for model and chip launches, including Jalapeño-style chip launches ("there are some cool graphs of the chip vs others"); (2) **magazine COVER page** when the story involves one (TIME cover for Altman AGI: "pattern match for future, if it involves a cover, use that; if theres a high profile personality use them"); (3) **collage of multiple high-profile tweets** for funding/valuation/raise news — "multiple high profile tweets in a collage is prolly better than one screenshot of an article"; (4) official demo video/graphs. Article-headline screenshots are the LAST resort. For Chinese/open models, CHECK HENRY'S OWN TWEETS FIRST — he runs internal benchmarks and posts the charts (GLM-5.3 full results; "Deepseek v4 flash > Qwen 3.8 27b on my internal benchmark"); his benchmark artifact is a first-class slide asset when it covers the story. He explicitly flagged a missed instance: "I made a benchmark for this earlier in the week you should have used that."
- **Vision-verify image CONTENT, not just presence (Henry, 2026-08-28: "the attached images in some of them is super weird.. nvidia acquisition is some weird sign, means you ddnt verify the content in each image").** Every slide image gets a vision check that names what is actually IN the image (headline text, chart axes, faces) and confirms it matches the story. A valid PNG of a "NotFound" JSON response, a consent-wall remnant, or an abstract sign/logo is a FAILURE even though the file is a well-formed image. Log per-image verdict in the runlog before publishing.
- **Cluster same-entity / same-class news onto one slide (Henry, 2026-08-28).** Two news items about the same entity (Jalapeño + Altman AGI claim, both OpenAI) go on ONE slide. Models launched close together in the same class (GLM-5.3-Flash + Qwen Flash-Next) go on ONE slide. Under the shorter-but-more-items format ("now that we are doing shorter but more items"), target 3-4 clustered news slides instead of 9-10 single-story slides — "cluster things that are related or easily transitionable per slide."
- **Sponsor slots: beginning and end of show only (Henry, 2026-08-28: "for the sponsors, lets leave them in the beginning of the show and at the end").** No mid-show sponsor slides. The two reads stay first (after cold open) and last (before close). Rotation of WHICH sponsor leads still applies; the POSITION is fixed.
- **No internal scaffolding labels on news slides (Henry, 2026-08-21, Ep26 rev8: "The titles of these aren't the way I talk").** What Happened This Week slides must NOT carry the `story-num` kicker line (`SEG 1 · SUPERVISORY JUDGEMENT` etc.) or the owner segment tag (`S1 · HENRY`); replace the `slide-tag` content with `WHAT HAPPENED THIS WEEK` and delete the kicker div. The h2 headline IS the voice — anything that reads like run-of-show scaffolding (SEG N, S#, owner, theme codename) stays in speaker notes, not on the slide. Numbered tags on non-news slides (cold open, `03 / SIGNAL FROM OUTSIDE`, hot take, close) are unaffected.
- **News-slide h2 titles use plain launch phrasing, not editorial punchlines (Henry, 2026-08-21, Ep26 rev9→rev10: "The titles of these aren't the way I talk … keep it simple").** Two verified patterns: (a) **launch pattern** — `[Company] launches [their newest <thing>]: the [name].` / `DHH launches the Omacom Foundation with $8M.` — subject-verb-object, the launch IS the headline; (b) **statement pattern** — `Stripe buys OpenRouter, & the hot stealth model.` — one plain sentence, may name two related entities. NEVER slogan/copywriter constructions ("the chart is the launch", "Agents can pay mid-task without ever holding your keys", "A 27B model is the boss of GPT-5.5 now"). Write titles the way Henry would SAY the first line of the segment. When a host tweets about the story, mirror his tweet's plain phrasing (his Faraday RT: "a 27B model can beat GPT-5.5 … by learning when and how to use GPT-5.5 as a tool").
- **Henry-supplied artifact images (Telegram reply "Use this for X image").** The image lands at `~/.hermes/cache/images/img_*.jpg`. Identify content via tesseract OCR when vision_analyze is unavailable (usage charts OCR cleanly: model names + token totals). Copy to `assets/images/artifacts/sN-<slug>.<ext>` as the canonical asset — never reference the cache path — then update slide src/alt/caption, bump rev, and record provenance in `media-manifest.json` (source = Henry-supplied Telegram image, verbatim instruction, OCR'd values; the chart data is the receipt). Publish asset + deck in the same commit and verify the live asset sha256 matches local.
- Never fabricate screenshots, quotes, charts, or media. Video cues need source URL, start/end or cue, poster/fallback, clickable link, and no autoplay.
- Every story slide exposes a clickable source link. Add a final Sources/Links slide.
- **Close-slide Discord QR (Henry, 2026-08-23): the LAST slide must include a QR code that leads to the WeeklyClaw Discord.** Use the authority deck's `.discord-qr` card verbatim: local image `assets/socials/weeklyclaw-discord-qr.png` (copy it from the prior episode's showprep `assets/socials/`), anchored to `https://weeklyclaw.ai/discord` — the rotating invite route, never a hardcoded `discord.gg/<code>` (invites expire ~30 days; see the invite-link publication gate). `validate_deck.py` check 5b fails the build if the QR card, link target, or image file is missing.
- Store local media under the showprep asset directories and resolve every local path before promotion.
- Give slides stable IDs. Speaker notes must have exactly one entry per slide, and every entry must include owner, purpose, opening line or optional landing line, 3–5 talking points, evidence/caveat, question or handoff, visual cue, source links, target time, and cut contingency. Henry's view stays bullet-first; Andy's view carries complete fallback prose.
- Henry and Andy views contain only their sections plus shared transitions. Tag each host only where they have an actionable review.

## Verification gates

Before reporting a draft as ready:

1. Read back every required file and verify non-empty content.
2. Parse JSON with `python3 -m json.tool`.
3. Run `python3 scripts/validate_deck.py <deck.html> <speaker-notes.md> [authority-deck.html]`.
   With no third argument it runs the base 8 checks: slide-ID parity, JS syntax
   via `node --check -`, autoplay detection (allowing "do NOT autoplay" prose),
   ≥ 10 clickable source links, final Sources slide, canonical theme markers
   (now requiring the real `weeklyclaw-logo` symbol, not the `claw-mark` string),
   local media resolution, and segment-ID discovery. When the authority deck is
   supplied as the third argument, 6 additional template-authority gates run:
   CSS custom-property parity, SVG symbol parity, invented-logo rejection,
   layout-class coverage, sponsor-asset provenance, and deck-size sanity.
   Always pass the prior APPROVED episode's `deck.html` as the third argument
   on BUILD and material rebuilds. Exit 0 = PASS.
4. Parse slide IDs from the deck and note headings; assert equal order,
   count, and uniqueness.
5. Resolve every local media path and record external-link verification in `media-manifest.json`.
6. Hash the candidate set and revision artifacts. Put hashes and model attempts in `state.json`/`evidence.md`.
7. Record gate time, inputs, candidate/source counts, story hash, artifacts, validation, approval state, and delivery purpose in `evidence.md` and `runlog.md`.
8. Run deterministic lints before review-card delivery and again before promotion: host-format structure (Henry bullets/optional line/handoff; Andy fallback prose/handoff); Hot Take/news non-duplication; cluster exclusivity/post-merge score; no staging `output/` paths in promoted files; seven-artifact manifest and shared revision/story hash; deck/notes slide-ID parity; media/cue/fallback/no-autoplay; canonical theme markers/hash; runtime target 32–38 and hard stop under 45 minutes; **template-authority comparison** (the new deck's `<style>` block, SVG `<symbol>`/`<defs>`, CSS custom properties, layout classes, and JS must derive from the prior APPROVED episode deck, not be invented); **invented-logo rejection** (no `<symbol>`, `<path>`, or inline SVG drawing a claw/logo/brand mark absent from the authority deck); **sponsor-asset provenance** (every `assets/sponsors/` file resolves and matches a prior-episode sponsor asset by sha256); and **1600x900 render QA** (render both the authority deck and the new deck at 1600x900 via headless Chromium, confirm no text clipping, no element overlap, no report-like text density, and visual consistency with the authority deck's layout). See `references/prior-episode-template-authority.md` for the exact gate recipe.
9. Treat any lint failure or missing evidence receipt as a failed package, not a warning.
10. Do not promote to root `agenda.md`, `deck.html`, `henry-talking-points.md`, or `host-cheat-sheet.md` unless state is explicitly approved by Henry or Andy. Back up existing root artifacts before promotion.
11. If an authorized instruction includes `publish`, continue through website sync/deploy and live verification; changing approval state or promoting root files alone is not completion.
12. Before website publication, trace every deck-relative media path and include those files in the staged/public artifact set. A live deck with missing local media is a failed publication.
13. After publication, verify the user-facing page with content canaries and representative local media URLs, not only deploy-command success.
14. After any post-freeze fact-check or asset correction, search every public and host-facing artifact for superseded wording, compare canonical files with generator output byte-for-byte, copy in the authoritative direction, include newly referenced assets, recompute receipts/state hashes, and verify the exact public URLs return canonical bytes.

## Refresh, freeze, authority, and handoff

### Host-feedback delegation and thread availability

When Henry or Andy sends a screenshot/list of several independent review tasks and explicitly asks for subagents:

1. Translate each item into one bounded worker brief with episode, current revision, source paths, read/write authority, and required receipts.
2. Dispatch every requested worker in background mode. Keep the originating Telegram thread available for normal conversation; do not block, wait, or poll in-thread.
3. If the user says all work should be handled by subagents, the coordinator must not begin a competing implementation. Coordinator only routes, resolves conflicts, verifies receipts, and synthesizes the final revision.
4. Use read-only scouts for discovery/research/audit and exactly one implementation owner for artifact writes. Never let multiple workers edit the same revision files.
5. If runtime concurrency is lower than requested worker count, queue remaining briefs or use an approved independent worker route. State the constraint plainly; do not silently reduce team size or make the coordinator an unrequested substitute worker.
6. Treat reply-to text, attached documents, and screenshots as one instruction packet. Preserve supersession language such as “disregard the last talk track; use this instead.” Hermes session JSONL may retain only the reply caption while omitting the original message's file metadata. Before declaring the replacement payload missing, search the underlying Telegram/Beeper archive for the exact quoted phrase, inspect the original message object, resolve any `mxc://` attachment through the supported asset API, and verify filename/size/hash. If the original channel archive and accessible asset stores still do not yield the replacement, stop that workstream as BLOCKED rather than retaining superseded copy. Use the `cross-agent-memory-retrieval` skill's `references/reply-linked-attachment-recovery.md` recipe.
7. Worker completion is not package completion. Read back changes, reconcile all seven artifacts, validate, render-check, update state/evidence, and only then publish the standing-authorized website draft.
8. If any worker exceeds five minutes, post one compact progress block per worker every five minutes until all finish. Use an ASCII bar, label percentages as estimated unless measured, and include `Done` plus `Left`. Completed workers stay visible at 100% while others run.
9. Never use a progress card as the final delivery. A worker marked 100% is not delivered until the coordinator surfaces the requested payload in-thread: direct mobile-openable sheet/link, substantive answer, edited artifact, or explicit blocker. Do not make Henry or Andy ask “where is it?” after reporting completion.
10. When a host supplies a replacement talk-track document, follow `references/host-supplied-talk-track-replacement.md`: preserve the full script, close every stale-reference surface, rebuild, validate, render, republish the website draft, and deliver the actual links/results.

See `references/host-feedback-parallel-execution.md` for routing and receipt templates.

- Henry user ID `855505513` and Andy user ID `7615999206` may each issue lineup `APPROVE`, `SWAP`, `DROP`, `PIN`, `ORDER`, trigger root promotion, and authorize website publication.
- Andy may also change workflow, production, video cues, ownership, and section content inside drafts; record changes in `workflow-feedback.md`. Other senders cannot approve/promote; ignore and log those commands.
- Refresh only developments since the last successful tick and explicit feedback. No-change refreshes return `NO_REPLY` while still recording successful source cursor/tick evidence.
- Refresh tick evidence path: on every REFRESH tick, append a `## YYYY-MM-DD HH:00 EDT — REFRESH tick (<tick-id>)` block to `runlog.md` that records (1) gate time and tick ID, (2) lock state on entry, (3) inputs inspected since the last successful tick (showprep directory mtime, workflow-feedback.md, host Telegram topic), (4) story-set unchanged or swap proposed, (5) hash readback of all seven rev artifacts against `state.json` artifact_hashes (no drift = no rebuild), (6) finding on any new >=9.0 candidate, (7) approval state, (8) pending human action. Treat the wire-output as `OK · WeeklyClaw Episode <N> Friday show prep · no action (REFRESH tick HH:00 EDT, ...)` so the cron output contract is satisfied without producing a fresh review card.
- Two-hour reminder rule: the canonical cron prompt allows one reminder at 2 PM ET FRIDAY (= 14:00 ET / 14:00 EDT during summer) if the package is still UNVALIDATED. Thursday BUILD and Thursday refreshes do not send reminders. Do not repost the full review card; a single short pointer to the review-card artifact paths and the exact APPROVE/SWAP/DROP/PIN/ORDER commands is enough. Do not send a reminder at 12:00 — the BUILD review card is already in the same Telegram topic. **Do not confuse "two hours after BUILD" with "2 PM ET": BUILD is at 11:00 ET, so the literal 2 PM ET reminder fires at 14:00 ET, not 13:00 ET. The 13:00 tick is a plain no-change REFRESH, not a reminder slot. Computing "BUILD + 2h = 13:00" is a common mistake — pin the reminder to the literal 14:00 ET hour.** When in doubt, read the canonical cron prompt (`~/weeklyclaw/council/current-friday-cron-prompt.md`) — the skill text and cron prompt are authoritative; ad-hoc interpretations of "two-hour reminder" are not.
- Before 3 PM, propose a replacement only if it is verified, scores >=9.0, and beats the lowest unpinned story by >=0.5. Never silently swap an approved or pinned story.
- Standing interpretation: watch until showtime, mutate until 3 PM. At freeze, state APPROVED or UNVALIDATED, final revision, paths, verification time, unresolved claims, cut order, and remaining human actions. From freeze to handoff, exceptional news may trigger proposal-only alerts; do not mutate artifacts.
- **Coverage-gap check at FREEZE (Henry-approved 2026-08-21).** Before locking, match the episode window's Henry tweets (`sources/henry-tweets/all.jsonl`, originals weighted over RTs, garble-variant regexes per `references/tweet-vs-aired-overlap.md`) against the selected lineup. Any breaking-news topic with >=5 tweets and zero segment presence gets one flag line in the FREEZE message for host decision — flagged, never auto-added. Apply the airtime news-window and launch filters first; tweet volume alone never qualifies a topic, and Henry's lived/first-hand material belongs in the Henry section, not the news rundown. Burn case: Episode 25's Grok Bot had 36 tweets (including Henry's top-engaged original of the window) and got one passing mention at 26:47.
- If unvalidated at freeze, leave root artifacts byte-identical. Handoff names exact usable `revs/` paths and labels them UNVALIDATED.
- Handoff is read-only and maximum 12 lines: State, Done, Now, Blocker, Next, final paths, approval, late story.

## Pre-show community promo (X + Discord)

Before each Friday show, post the promo with the Discord event link so viewers can join. The X post and Discord Beeper post are separate delivery paths with different blockers:

### X post via Typefully

- Use the WeeklyClaw Typefully key (`~/clawd/secrets/typefully.json` → `weeklyclaw_key`), social set 322715.
- **The `publish_at: "now"` 403 fires on any draft containing a URL.** Workaround: create the draft (POST), then PATCH it with a future ISO timestamp 2-3 min ahead: `PATCH /v2/social-sets/322715/drafts/{id}` with `{"publish_at": "2026-08-07T19:46:14Z"}`. Typefully's internal scheduler publishes within ~4 min.
- Poll `GET /v2/social-sets/322715/drafts/{id}` until `publish_state` is `"finished"` and `x_published_url` is non-null.
- Do NOT fall back to Bird CLI for WeeklyClaw (auth tokens are stale; Typefully is the sole write surface).

### Discord via Beeper (multi-target broadcast)

- The Beeper skill is user-owned (`hermes curator adopt beeper` to enable curation). Chat IDs for Friends of the Crustacean:
  - `#shell-society`: `!gXx0enjFRfVVGFs2JAat:beeper.local`
  - `#general`: `!vY1OnTVkdVacHw6qAvsB:beeper.local`
- POST to `/v1/chats/{chatID}/messages` with `{"text": "..."}`. The API returns `pendingMessageID` only.
- **Verify delivery** by re-fetching recent messages after 3-5s and matching normalized text (Beeper stores messages as HTML: `\n`→`<br>`, URLs→`<a href>`, entities escaped). See Beeper skill's HTML normalization section.
- The recurring cron `weeklyclaw-beeper-community-promo` (script: `~/.hermes/scripts/weeklyclaw-beeper-promo.py`) handles this deterministically every Friday, gated to show time, with date+content dedup.
- **Invite-link publication gate (SEV-2 recurrence, fixed 2026-08-21).** NEVER hardcode a `discord.gg/<code>` (or `?event=`) link in any promo/post script. Discord invites expire in ~30 days; the promo script shipped the dead Aug 7 invite (`SPYQRuAdS`, expired Aug 9) on Aug 14 AND Aug 21 even after the Aug 16 postmortem, because the fix landed in the `weeklyclaw-discord-invite-rotation` cron (which rotates `weeklyclaw.ai/discord`) but never rewired the publishing script. Contract now embedded in the script and required for any future link-posting automation:
  1. At runtime, resolve `https://weeklyclaw.ai/discord` WITHOUT following redirects (custom `HTTPRedirectHandler` returning `None`, or `curl -sI` and read `Location`). Vercel serves a 307 to the current invite.
  2. Validate the extracted code via `GET https://discord.com/api/v10/invites/<code>?with_expiration=true`. Require HTTP 200 from the API — a 200 from the `discord.com/invite` landing page proves nothing (Discord serves the generic web shell for dead invites; this false-validation pattern caused the original SEV-2).
  3. Assert `guild.id == 1532061180569587975` (Weeklyclaw) and expiry >24h out. Any failure = fail closed, no fallback link, alert.
  4. Discord's API 403s Python's default urllib User-Agent — send a custom UA on every request.
  Caveat: this route loses the `?event=<id>` deep-link (no event API hook). If the event link matters, an authorized person must supply the event ID weekly; do not synthesize one.

### Structural mid-review edits (slide removal, reorder, layout rebuild)
Verified on Episode 26 rev5→rev6 (2026-08-21). Henry sends a slide screenshot
plus terse multi-part commands: remove a slide, move Signal From Outside after
all news segments, rebuild the Stripe slide as title-on-top with two artifact
images side by side. Full recipe:

1. Read the screenshot via tesseract OCR to identify which slide (image
   contains segment titles/headers). Do not guess from context.
2. Write `revs/make_rev<N>.py` operating on the previous deck with regex
   block moves: `<div class="slide" id="X">.*?\n</div>\n\n` spans are the
   unit of move/remove. Extract → remove → reinsert at the new anchor.
3. Speaker-notes parity: removing a slide requires deleting its `## s-x`
   notes section AND folding operational content (cut order, pin
   directives) into the cold-open notes section.
4. Regenerate all five derived md files (agenda, talking-points,
   henry-section, andy-section, host-cheat-sheet) from the prior rev even
   when unchanged, so the rev numbering stays coherent.
5. Layout verification via Playwright `getBoundingClientRect` on the
   rebuilt slide: title.y + title.height < each image.y (title on top),
   img[0].x + img[0].width < img[1].x (side by side), equal widths.
6. Republish the website draft; remember newly-referenced assets (a
   previously-unpublished artifact image must join the git whitelist).
7. Deliver a rendered PNG of the rebuilt slide in the Telegram reply.

## References

- Read `references/host-supplied-talk-track-replacement.md` whenever

- Read `references/host-supplied-talk-track-replacement.md` whenever Henry or Andy supersedes an existing video/talk track with a document, attachment, or reply-linked script. It defines authority recovery, verbatim preservation, cross-artifact replacement closure, stale-reference checks, rebuild/render/publication gates, and actual-result delivery.
- Read `references/host-shared-resources.md` before drafting or when any host shares links, posts, videos, or demos in the WeeklyClaw Telegram topic. It defines the retrieval technique (bird/yt-dlp/curl), the three-tier classification (official/primary, practitioner/hands-on, community/discussion), the four output artifacts (source ledger, agenda production notes, deck Host Resources slide, speaker-notes appendix), the equivalent-resource finding workflow for topics where no host link was shared, and the reusable CSS/slide template for the resources card.
- Read `references/prior-episode-template-authority.md` before any BUILD or material deck rebuild. It defines how to discover the prior APPROVED episode as the verbatim visual template, the deterministic template-comparison gate (CSS/SVG/layout-marker parity), the invented-logo rejection rule, sponsor-asset provenance check, the 1600x900 headless-Chromium render-QA recipe, and — for rebuilds after a theme regression — the exact reference values (logo SVG paths, type scale, must-present/must-absent class lists, controls-parity greps) and the working CDP per-slide overflow measurement recipe.
- Read `references/cursor-deck-contract.md` for the exact fallback evidence and validation recipe.
- Read `references/direct-hermes-build-path.md` for the documented alternative to the mandatory Cursor route: when the package is small (≤ 14 slides, ≤ ~140 KB total) and the author can produce canonical-theme HTML by hand, the seven-artifact package can be authored in Hermes in a single 11:00 BUILD tick and pass every gate. Includes the dcg shell-parser gotchas, `node --check -` pattern, lock-release protocol, and the validate_deck.py script invocation.
- Read `references/friday-show-prep-control-plane.md` before changing scheduler behavior, recovery, authority, artifact contracts, freeze semantics, or validators.
- Read `references/schedule-change-runbook.md` whenever the show-prep schedule itself changes (build day, tick hours, check frequency): the change must land in the cron registry, the canonical cron prompt, SKILL.md, and the support references together, or the gate and prompt drift apart. Covers BUILD-day vs show-day decoupling, reminder-slot pinning, and the verification checklist.
- Read `references/post-freeze-verification-and-handoff.md` after late fact-checks, asset corrections, presenter-link requests, or reports of deck slowness.
- Read `references/handoff-tick-recipe.md` on the Friday 16:00 ET HANDOFF tick: read-only, no regeneration, no Telegram post, 12-line summary format, live SHA-equal re-check at showtime.
- Read `references/publication-runbook.md` whenever Henry or Andy approves, requests canonical promotion, or says to publish; it defines authority, asset closure, live canaries, and completion evidence.
- Read `references/multi-platform-episode-publication.md` for every authorized finished-episode release. It defines Geordi account-identity gates, the common release package, full native X upload and reply-chain pattern, Bilibili verification handling, per-platform retry states, deduplication, and the three-URL completion contract.
- Read `references/late-visual-asset-and-qr-edits.md` before post-freeze sponsor-logo, social-link, or QR-code edits; it covers concurrent-edit preservation, authoritative-direction sync, and rendered QR decode proof.
- Read `references/website-draft-publication.md` before any BUILD or first REFRESH after a BUILD. It defines the git worktree route, what to copy, what NOT to touch (gallery/homepage), the `validate.mjs` constraints that block naive card additions, the sponsor-order byte-offset check, the missing-publication recovery recipe, and the full sync script path for APPROVE-triggered listing. This is the standing-authorized publication recipe, not a one-off.
- Read `references/draft-publication-recovery.md` when a BUILD passed locally but the standing-authorized draft is not live on `weeklyclaw.ai` (404 on `/deck`, `/agenda-draft`, or `/host-cheat-sheet`), or when `hermes send` to the WeeklyClaw Telegram topic is BLOCKED by dcg. It codifies the recovery recipe, the required `state.json.draft_publication` + `runlog.md` receipts, the `hermes send --file` workaround for the dcg `redirect-truncate-root-home` false-positive, and the sponsor-order byte-offset check.
- Read `references/on-slide-live-artifacts.md` before any BUILD or material news-slide rebuild. It defines the corrected visual-first contract: one dominant picture/video/live artifact, headline, zero to two short context lines, details moved to speaker notes, source capture/provenance, sparse-layout recovery, DOM/render gates, and website asset verification. The former small `ON-AIR LIVE ARTIFACT` panel beside dense copy is explicitly rejected.
- Read `references/cross-episode-segment-comparison.md` when Henry asks to compare news segments across episodes or screenshot specific slides from prior decks: latest-rev discovery, per-episode slide-ID variance, hash-targeted headless-Chrome screenshots at 1600x900, the vision-free slide-identity verification chain (`<div>` not `<section>`), PIL contact-sheet delivery, and the editorial-continuity comparison output.
- Read `references/aired-video-comparison.md` when Henry says "compare the slides in the video" (aired YouTube video, not the deck files) or asks to check a planned lineup against what actually aired. It defines the channel RSS discovery route, the yt-dlp `player_client=android` 403 workaround, the OCR-based slide-identification pipeline (aHash dedupe → dense scan → tesseract, no vision model needed, never binarize the cream-on-teal theme), and the editorial pattern checks (mix balance, duplicate-thesis merge, category gaps). Aired video is the editorial ground truth: early agenda revisions do NOT match it (EP24 agenda rev1 ≠ final deck rev3 ≠ nothing), and on-air visuals often diverge from the deck even when segment identity matches. Henry's confirmed takeaway from the EP24/25 review (2026-08-20): "live artifact is the right insight" — when presenting comparison findings, lead with the live-artifact observation, not secondary pattern-gap observations.
- Read `references/host-triggered-rebuild.md` whenever Henry or Andy explicitly commands a deck regeneration/material rebuild between scheduled ticks (or the Friday 11 ET REFRESH acts on deferred lint debt). It defines the authorized trigger classes, the rev-derivation-by-script sequence, the validator setup gotchas (copy `qa/validate_deck.py` from the prior episode; `revs/assets` symlink for relative media resolution), the two recurring slide-ID parity failure shapes (missing `s-title`, duplicate `s-sources`/`s-outro`), the regression-vs-prior-rev render-QA gate, and the republish + receipt contract. Verified on Episode 26 rev1 → rev2.
- Read `references/rolling-candidate-intake.md` for the daily (non-Friday) candidate-intake cron: the multi-tool source-verification toolchain (bird → Exa → Jina Reader fallback → HF API → gh API), mandatory Henry X pulse calibration via `@iAmHenryMascot`, candidate-block structure, evidence-discipline labels, editorial-thread synthesis, explicit non-candidate ledger, and sheet-sync step. The Sheet is an audit ledger, not a voting gate; clear evidence-led selections proceed without asking Henry to vote.
- Read `references/guest-intelligence.md` when building or operating a news-triggered guest pipeline. It defines the weekly Chinese AI ecosystem scan, 10/15 scorecard, internal 2–5-speaker mapping, named-person/concrete-role requirement, Jim-owned Guests ledger schema, underlying-hook deduplication, evidence-only relationship notes, Sheets-only write path when Drive placement cannot be changed, authenticated row readback, and current Guests-tab `gid` verification.
- Read `references/no-change-refresh-recipe.md` on every REFRESH tick that finds no host feedback and no drift: it codifies the input-inspection list, the `runlog.md` evidence block template, the `OK · <job> · no action` wire output, and the 14:00 ET 2 PM reminder posting recipe (and the BUILD+2h vs. literal 2 PM ET trap).
- Read `references/weeklyclaw-x-news-drafts-notes.md` for the parallel x-news-drafts cron (`8db1b4ad59f7`): Typefully v2 API gotchas, media-guard recipe, working non-Polymarket news sources, gap-priority override, and combined-queue dedup pattern.
- Read `references/henry-tweet-backup.md` for the Henry tweet backup pipeline that feeds story selection: canonical `~/weeklyclaw/sources/henry-tweets/` store, the `henry-tweets-daily-backup` script-only cron (every 4h, silent on success), bird-CLI JSON parsing quirks (`raw_decode` from first `[`; info-line prefix; trailing data), cursor-pagination deep backfill when the 200-tweet window (~6 days at Henry's volume) doesn't reach the target episode, staleness fallback, the prior-episode tweet dedup rule, and the post-change verification recipe.
- Read `references/tweet-vs-aired-overlap.md` when Henry asks to compare his tweets against what actually aired on an episode: aired-transcript ground truth (yt-dlp channel discovery, auto-caption garble variants like "queen"=Qwen and "Glockbot"=Grok Bot), tweet-window construction (prior episode airtime boundary, 20:00 UTC), the topic-matrix + engagement method, the news-grade lineup filter, the FREEZE coverage-gap step, and the bidirectional coverage-gap findings from Ep24/Ep25.
- Use `templates/agenda-template.md` as the packaged agenda baseline; reconcile the workspace `template.md` against it.
- Read `references/beehiiv-newsletter.md` before any WeeklyClaw newsletter/Beehiiv work (Monday written-roundup edition): publication facts, credential location (Vaultwarden), sending-domain check, and the draft-then-approve send contract.
- Read `references/thumbnail-host-likeness-rules.md` before any WeeklyClaw thumbnail generation, QA, or regen request. It defines the verified Andy/Henry identity mapping and placement, the ground-truth card reference assets on Enterprise (card wins on any conflict), the "broad-but-generic chiselled bald podcast man" rejection criteria, Andy's positive soft-tissue likeness markers, the geometry+soft-tissue dual QA gate, and the Nano Banana Pro generation route.
- Read the existing `scheduled-intelligence-sync` skill for source/date normalization, atomic state promotion, and artifact-hash discipline.

## Pitfalls

- **Artifact present is not artifact dominant.** Do not treat a loaded image, screenshot thumbnail, or small labeled artifact card as compliance. For What Happened This Week, the picture/video/live artifact must visually dominate; on-slide copy stays at headline plus zero to two short lines. If layout pressure leads to shrinking the artifact or fitting dense prose, delete the prose and move it to speaker notes. Use `references/on-slide-live-artifacts.md`.
- **Logged in somewhere is not logged in on the operable target.** A user screenshot, cookie-domain presence, Chrome profile name, saved tab, or prior receipt cannot authorize a write from another browser instance. Immediately before X/Bilibili publication, prove the required account in the exact connected host + browser/profile that will perform the write. If identities differ, stop without posting, name both identities, and ask for the required account to be opened there. See `references/multi-platform-episode-publication.md`.
- **Episode 24 invented its theme instead of cloning Episode 23.** The BUILD produced a 37 KB deck (vs the 74 KB Episode 23 authority) with an invented inline `<symbol id="claw-mark">` SVG, an invented `brand-mark`/`claw-text` CSS class system, sponsor `<img>` refs to non-existent asset files, and a stripped layout. The old `validate_deck.py` passed it because its theme marker looked for the string `claw-mark`, which the invented deck contained and the real Episode 23 deck did not (Episode 23 uses `weeklyclaw-logo`). Always run the template-authority comparison and render-QA gates from `references/prior-episode-template-authority.md`. Never trust theme-marker string matching alone.
- **The `episodes/22/deck-website-theme.html` file is the rejected dark theme, not the canonical template.** Earlier skill text called it the authoritative website theme. It uses `--bg-dark:#0a0a0a`, Inter/JetBrains Mono fonts, and a red/orange gradient. Henry rejected it during Episode 23 prep and it must never be used as a template again. The canonical template is the prior APPROVED episode deck (currently Episode 23).
- Do not report model success from process exit alone. Artifact completeness plus readback is the contract.
- Do not overwrite canonical episode artifacts while approval is UNVALIDATED.
- Do not claim independent corroboration when the packet contains only an official source and a secondary mention.
- Do not treat a visual placeholder or textual metric card as a verified screenshot. Mark the fallback honestly.
- Do not regenerate the deck at the 4 PM handoff tick.
- Do not let a broad news scan replace the verified daily candidate pool and focused primary-source sweep.
- Do not deliver show prep as raw filesystem paths Henry can't open on mobile. Provide an accessible link (Entity hosted URL, Caddy friendly URL, or shared link) alongside file paths. Henry consuming on mobile cannot open `~/weeklyclaw/...`.
- Do not leave show recordings untrimmed before upload. At least one WeeklyClaw recording ran all night; others rolled past the show end. Pre-upload scrubbing to show-only content is a required step.
- Do not collapse official leaderboard results, organizer-verified public-set runs, and vendor alternative-harness results into one benchmark number.
- Do not infer that a security product fixed or answered a nearby incident without a primary-source causal statement.
- Do not generalize a hardware verdict from full/unpruned weights to pruned or expert-reduced derivatives; name the exact artifact and quality caveats.
- Do not claim canonical/generator parity from matching filenames. Prove byte equality, asset resolution, updated receipt hashes, and public-byte readback.
- **state.json can lag behind `revs/` and the live website between BUILD and FREEZE.** Revisions authored outside the cron (Henry's manual edit, a non-Cursor rebuild, a talk-track-only refresh where slide markup is unchanged but `_slides_content.rev<N>.html` is) leave `state.json` pointing at the previous revision while rev files and the live site already moved. The FREEZE tick must reconcile this: recompute the highest existing revision, compare to `state.json` `selected_revision` + `artifacts.*`, promote state.json to match, re-run the validator on the promoted rev, and byte-check the live `weeklyclaw.ai/episodes/<N>/deck` URL against the local rev file before locking. See `references/no-change-refresh-recipe.md` § "FREEZE drift reconciliation" for the full recipe.
- If presentation feels slow, check host contention before rewriting deck code; report load and ask before terminating processes.
- **Henry asks "which skill/tool generates this?" — answer precisely.** The deck is generated by Cursor Agent on Enterprise (model route `kimi-k3-high` → `claude-opus-5-high` → `gpt-5.6-sol-high`), orchestrated by the `weeklyclaw-friday-show-prep` cron following this skill. Similarly, when Henry assumes topics come "from the spreadsheet": the Sheet is an audit ledger only; the topic source is the verified daily candidate-intelligence pool plus Henry's X pulse, scored 0–10. State the actual source chain plainly; don't let a wrong mental model of the pipeline stand.
- **Do not leave a `state.lock` file behind at the end of a tick.** If a stale
  lock is present (PID not running, prior session interrupted), verify with
  `ps -p <pid>` and remove it; record the reason in `runlog.md`. A lock
  held across an interrupted run will block the next hourly tick and force
  it into a no-op recovery. Always `rm` the lock on every exit path —
  success, failure, blocked, validation-fail.
- The skill says "no-change refreshes return NO_REPLY", but the cron output
  contract (`[CRON_OUTPUT_CONTRACT_V1]`) wraps every tick and demands a
  compact line. Honor the cron contract: emit
  `OK · WeeklyClaw Episode <N> Friday show prep · no action (REFRESH tick HH:00 EDT, ...)`
  even when nothing changed. Do not silently return NO_REPLY from a
  scheduled tick — the orchestrator treats that as a delivery failure.
  NO_REPLY is the rule for non-Friday hours (no gate pass), not for
  in-window no-change REFRESH ticks.
- Do not interpret "two-hour reminder" as "two hours after BUILD" (13:00).
  The canonical cron prompt's "one reminder at 2 PM ET" means 14:00 ET on
  SHOW DAY (Friday), always. Since the 2026-08-20 Thursday-BUILD move,
  "BUILD day + 3h = Thursday 14:00" is equally wrong — Thursday 14:00 is a
  plain no-change REFRESH. Pin reminders to (show day, literal hour), never
  to BUILD-relative offsets. The 13:00 ET tick is a no-change REFRESH that
  appends a tick block to `runlog.md` and emits the OK no-action line. Save
  the reminder for 14:00 ET and verify state is still UNVALIDATED before
  posting.
- On every no-change REFRESH, still inspect: (a) `episodes/<N>/showprep/`
  directory mtime for new files, (b) `workflow-feedback.md` for new
  authoritative-host entries, (c) the originating Telegram topic via
  `hermes send --list telegram` and recent message reads if reachable,
  (d) all seven `revs/` artifact hashes — SHA-256 each file. If
  `state.json` carries an `artifact_hashes` block, compare against
  it directly; if only `artifacts` paths + `validation` receipt are
  stored (Episode 25+ pattern), assert non-empty + size-stable
  vs the BUILD-time `validation` block. Either way, no drift = no
  rebuild. Skip the broadcast Telegram reminder at 13:00.
- When posting any reminder message to the originating Telegram topic
  (chat_id `-1004370723812`, thread `17` for `weeklyclaw-friday-show-prep`),
  use `hermes send --to telegram:-1004370723812:17 --subject "<subject>" --file <path>`
  with the exact review-card artifact paths and the
  `APPROVE`/`SWAP`/`DROP`/`PIN`/`ORDER` command list. Never post the
  reminder at any hour other than 14:00 ET unless state changed.
- **Do not treat tweet volume as news-worthiness.** When proposing a weekly lineup from Henry's tweets, filter to breaking-news launches inside the episode window FIRST; then order by engagement. Presenting last-week's launches (already-aired topics) or non-launch opinion threads (e.g. Anthropic criticism, Merge product launches Henry dismissed) as news segments gets corrected by Henry. His lived/first-hand material (local benchmarks, harness setups) belongs in the Henry section, not the news rundown. Verified on Episode 26 lineup review, 2026-08-21.
- **Host-supplied product/model/version names are not verified naming.** Henry will say "Qwen 2.8 Max" from memory; the official @Alibaba_Qwen account says "Qwen3.8-Max" and "Qwen3.8-27B". When a host supplies a product, model, company, or version name from memory, treat it as a lead, not a verified fact. Retrieve the official source and use the official naming in the deck, agenda, and slides. Preserve the host's original wording in the source ledger with a correction note so the discrepancy is visible. This applies to company names (acquired vs acquirer), model version strings, release dates, and feature naming.
- **Mid-review full-segment replacement (Ep26 rev10: AWS AgentCore → DHH Omacom Foundation, 2026-08-21).** Henry replaces a whole segment by sending a tweet/launch link: "replace the last amazon news with launch of Omarchy by DHH <URL>". This is a material rebuild: (1) fetch the launch tweet first — X read routes may 401; fall back to the linked vendor post via plain `curl -sL` + tag-strip (firecrawl credits can be exhausted), then corroborate with search results; (2) rewrite the slide (launch-pattern title, `▶ LIVE` link to the host's tweet, artifact = official announcement page/benchmark, not a screenshot if a stronger type exists), speaker notes, and ALL surfaces; (3) **closure sweep: grep the deck (including the Sources slide) for the removed story's entity name and swap every source link** — AgentCore links survived rev10's first push and needed a fix commit; (4) republish and byte-verify. Title-check every new receipt URL.
- **Tone passes are Henry-section-only.** When Henry asks for anti-slop / tone work on titles ("just my section not the whole slides"), edit only What Happened This Week slide h2s and Henry-owned slides. Andy's sections, sponsor slides, Signal From Outside, and the cold open stay byte-identical. Verify with a diff scoped to the changed slide IDs.
- **Henry changes the lineup mid-build.** He will send a completely different set of topics via Telegram while the deck is being built or reviewed. This is not an error in the process; it is Henry adjusting in real time. When this happens: keep the template (CSS, SVG, chrome, script) from the authority deck unchanged, rebuild only the content slides with the new topics, research the new topics with source verification (no fabrication), and republish. Do not argue about the prior lineup. Do not try to preserve old segments. The deck template is immutable across lineup changes; only slide content moves.
- **execute_code calls are isolated.** Each `execute_code` invocation starts fresh; variables and string literals from one call do not persist to the next. When building a large deck HTML (50+ KB), do not attempt to build it across multiple execute_code calls. Instead: (1) write the content slides to a file via `write_file`, (2) write a small Python builder script via `write_file` that reads the authority deck, extracts the head/CSS/SVG/chrome/script blocks, reads the content slides file, and assembles the full deck, (3) run the builder via `terminal`. This is the reliable pattern for any deck rebuild or generation that exceeds what a single write_file can handle.
- Do not interpret "make changes to the agenda" as edits to a single file. **The agenda is produced by TWO workspace files, and host feedback must be routed to the correct one:** format/structure changes (Henry bullets vs Andy prose, section layout, speaker alternation, handoff-cue pattern) → edit `~/weeklyclaw/template.md`; selection/scoring/workflow changes (host-document precedence, hot-take-before-news ordering, source-retry policy, reminder timing, runtime targets) → edit `~/weeklyclaw/council/current-friday-cron-prompt.md`. Runtime targets (32–38 min scripted, 45 hard stop) must be unified across BOTH files — if they disagree, the BUILD produces inconsistent guidance. When a host asks to "review the prompt" or "see the agenda prompt," show them BOTH files — the cron prompt alone does not control agenda output, and template.md alone does not control story selection.
- **Draft deployment and editorial approval are separate states.** A passing BUILD or material rebuild may be live at `/episodes/<N>/deck`, `/agenda-draft`, and `/host-cheat-sheet` while `approval_state` correctly remains `UNVALIDATED`. Record both facts explicitly: preserve editorial approval as UNVALIDATED, but add/update a draft-publication receipt with pushed commit, deploy time, live canaries, and changed-asset hashes. Do not leave a later runlog/state claim saying “not deployed” after the standing-authorized draft route has been verified live. Repeat draft updates may stage only the subset that changed because unchanged whitelisted assets already match `origin/main`; that is not a missing-file failure. See `references/website-draft-publication.md`.
- **Website validator enforces homepage/gallery consistency.** The site's
  `validate.mjs` asserts the homepage's newest 6 `episode-week` cards
  match the episodes gallery's newest 6 `week-number` cards. Adding a new
  episode card to `episodes/index.html` WITHOUT also adding it to the
  homepage `index.html` breaks `npm run build`. For draft publication,
  push the deck + assets + agenda to `episodes/<N>/` only — do NOT touch
  the gallery or homepage. The full gallery listing, homepage featured
  episode, and archive count update happen atomically via the sync script
  (`sync-weeklyclaw-archive.py`) on APPROVE. See
  `references/website-draft-publication.md` for the full route and
  validator constraints.
- **`hermes send` body quoting triggers dcg false-positive `redirect-truncate`.** Two
  patterns reliably trip the `core.filesystem:redirect-truncate-root-home` rule even
  when no actual redirect is in the command: (1) trailing shell redirect syntax
  (`2>&1`, `| tail -10`, `> /tmp/...`) inside the same quoted body, (2) the
  three-character ellipsis (`...`) anywhere in the `--body` argument. The rule
  treats both as if they were file truncations and BLOCKS the send. Workaround
  for both: write the message body to `/tmp/<short>.txt` via `write_file` and send
  with `hermes send --to telegram:<chat>:<thread> --subject "..." --file
  /tmp/<short>.txt`. The `--file` form is the only safe way to send multi-line
  WeeklyClaw review-card bodies with the exact `APPROVE` / `SWAP` / `DROP` /
  `PIN` / `ORDER` command list to topic `-1004370723812:17`. Verified on Episode
  26 — first attempt with `--body "..." 2>&1` was blocked; second attempt with
  `--body "..." 2>&1` was blocked; third attempt with `--file /tmp/notice.txt`
  returned `sent`.
- **BUILD can pass without publishing the standing-authorized draft.** The
  seven-artifact gate (`validate_deck.py`, 1600x900 render, slide-ID parity,
  template-authority comparison) is independent of the website draft push. A
  BUILD that produces a passing package may still skip the worktree → commit →
  push → live-canary sequence if it focuses on artifact completeness and never
  gets to the publication contract. Episode 26 12 ET BUILD shipped rev1 PASS and
  never touched `/episodes/26/` on `weeklyclaw.ai`; the 14 ET REFRESH discovered
  the gap with a `curl -I` to `/episodes/26/deck` returning 404, repaired the
  publication, and recorded the recovery in `state.json.draft_publication` plus
  `runlog.md`. The repair must include (a) commit SHA pushed to `origin/main`,
  (b) `npm run build` PASS receipt, (c) live canary counts on the three URLs
  plus all referenced assets, (d) sponsor-order byte-offset proof, (e)
  `approval_state_after: UNVALIDATED` so editorial approval stays pending. Do
  not skip this self-check on subsequent REFRESH ticks just because the BUILD
  succeeded.
- **A passing BUILD can still ship known lint failures (e.g. host-ownership rule).**
  A seven-artifact PASS does not guarantee all rule lints were clean at author
  time. `workflow-feedback.md` directives recorded before or between
  revisions are authoritative: if it says `S2/S4 must be reassigned to Henry
  lead at the next revision` and the current rev still marks them `Andy (lead)`,
  that is a deferred fix, not a clean state. Thursday afternoon REFRESH ticks
  must log the deferred-to-rev2 item in `runlog.md`, NOT auto-trigger an
  unscheduled rebuild. Unsolicited rebuilds during a Thursday 12–16 ET REFRESH
  window (a) introduce changes the host has not reviewed, (b) risk drift on
  the published weeklyclaw.ai draft from a still-UNVALIDATED revision, and
  (c) bypass the standing host-approval gate. The fix lands on the next
  material rebuild trigger: an explicit host `APPROVE` / `SWAP` / `DROP` /
  `ORDER` command, the Friday 11 ET REFRESH if the build is still UNVALIDATED,
  or a documented host-side escalation. Verified on Episode 26 Thursday 15 ET
  REFRESH (rev1 still carries the S2/S4 `Andy lead` lint failure noted in
  `workflow-feedback.md`; deferred to next material rebuild, recorded in the
  `## 2026-08-20 15:00 EDT — REFRESH tick` block of `runlog.md`).
- **A hand-rolled "PASS" receipt is not the canonical validator's PASS.**
  Episode 26 rev1 shipped with a `qa/rev1_validation.md` claiming PASS from a
  structural checklist, while the canonical `qa/validate_deck.py` actually
  FAILED slide-ID parity (duplicate `s-sources`/`s-outro` notes sections,
  missing `s-title` entry). Discovered only when the rev2 rebuild ran the
  canonical validator. On any material rebuild, also run the canonical
  validator against the PREVIOUS revision; if it fails, record the hidden
  failure in `runlog.md` so the fix reads as a fix, not an unexplained diff.
  See `references/host-triggered-rebuild.md` for the full rebuild recipe and
  the validator setup gotchas (validator not auto-copied into new episodes'
  `qa/`; local-media check resolves relative to the deck file, requiring the
  `revs/assets -> ../assets` symlink).
- **Ownership strings live in more artifact surfaces than grep first shows.**
  Reassigning a segment lead touches: agenda `**Henry (lead):**` paragraphs,
  speaker-note `## s-seg-x — Owner` heads AND their `- **Owner:**` bullets,
  cheat-sheet `| S2 Faraday | Andy lead |` rows, host-section
  `## s-seg-x (Andy lead)` headings, talking-points labels, and the deck map
  slide's `<td>Andy</td>` ownership column. Grep
  `Andy (lead)\|Andy lead` across ALL rev files and require zero hits on news
  segments before validating; per-file spot fixes leave stragglers.
- **A host rule acknowledged in chat is not a rule recorded in the control plane.** When Henry or Andy states a durable editorial rule mid-review (e.g. Andy's 2026-08-21 "one recap at the end, never recap the recap") and any agent replies "noted and saved", that acknowledgment changes nothing until the rule is written into the layers that generate output. Verified 2026-08-22: the recap rule existed in ZERO layers (SKILL.md, cron prompt, template.md, agenda-template, jobs.json) a full day after the acknowledgment, and would have been dropped by the next BUILD. When a host gives a durable editorial rule: (1) grep every layer for any existing wording, (2) patch ALL layers in the same pass — workspace `template.md`, packaged `templates/agenda-template.md`, `council/current-friday-cron-prompt.md`, this SKILL.md, and the job prompt inside `~/.hermes/cron/jobs.json` — (3) verify with a final grep across all five plus a jobs.json reload. A rule that lives only in memory or a chat acknowledgment is a rule the next tick does not have. Also record host directives in the episode's `workflow-feedback.md` with date, verbatim quote, and the command for the next tick.
- **A rule patched into SKILL.md does not reach the job that reads a
  reference file or a separate cron prompt.** The 2026-08-21 airtime
  news-window rule was written into SKILL.md but the daily-intelligence cron
  executes `references/rolling-candidate-intake.md`, whose line "prior intake
  completion timestamp as the cutoff" still governed — so Qwen3.8-2.4T
  (launched pre-airtime) kept qualifying as next-episode news. WeeklyClaw
  rules live in up to FOUR layers that can drift independently: SKILL.md,
  the relevant `references/` file, `council/current-friday-cron-prompt.md`,
  and the stored cron prompt inside `~/.hermes/cron/jobs.json`. When patching
  an editorial rule, grep every layer for the old wording before calling it
  done, and patch `jobs.json` by loading it, editing the target job's
  `prompt` field, dumping back with `json.dump(..., indent=2)`, then
  re-loading to verify — never by string-replacing the raw file. The
  no_agent wrapper (`~/.hermes/scripts/bounded-reasoning-cron.py`) clones the
  job record from `jobs.json` at run time, so an edit to jobs.json takes
  effect on the next tick without a scheduler restart.
- **Before asserting "no prior comment exists," read the episode's
  `workflow-feedback.md` end to end.** When Henry asks "haven't I already
  commented on this?", that file is the authoritative record of host
  directives — pins, drops, rules — and `state.json`'s `pins` array is a
  separate, smaller record. Answer from those files, then append the new
  directive there (with date, verbatim quote, and the command for the next
  tick) so the next session finds it in one place.
- **A staged artifact is not a shipped artifact.** Recording a sourced
  video/benchmark in `workflow-feedback.md` and `media-manifest.json` does
  nothing until a revision's slide actually references it. Episode 26: the
  Cerebras launch video and DeepSeek benchmark were staged and logged at
  ~15:10 ET; the 15 ET cron tick built rev4 minutes later and re-shipped the
  old screenshots. On any host-triggered regen, FIRST grep the current deck
  for every staged asset filename and the old asset filenames; a rebuild
  that swaps neither is a wasted revision. Full rev5 recipe (script-based
  rev derivation, wrong-arxiv-URL title-check, slide-activation render QA,
  vision-free artifact proof, AWS H1-anchored captures) is in
  `references/host-triggered-rebuild.md` § "Lessons verified on Episode 26
  rev5".
- **Title-check every receipt URL on the slide, not just in the source
  ledger.** Episode 26 rev3/rev4 linked the Faraday segment to
  `arxiv.org/abs/2508.14251` — an unrelated relativistic-gas physics paper —
  while the source ledger carried the correct 2608.13331. `curl -sL <url> |
  grep '<title>'` on each slide's LIVE link catches this in seconds. When
  found, fix across deck, speaker notes, agenda, host views, and cheat sheet
  in the same revision.
- **Slide-deck render QA: activate slides via the deck's own `.active` class,
  not `scrollIntoView()`.** All slides sit stacked in the DOM; scrolling
  captures slide 1 every time. Remove `.active` from all `.slide` elements,
  add it to the target, wait ~700ms for the CSS fade (an 80ms wait captures
  the PREVIOUS slide), then screenshot.
- **Structural mid-review edits arrive as a screenshot + terse multi-part
  commands (Henry, 2026-08-21 Episode 26 rev6).** Pattern: one slide
  screenshot plus instructions like "remove this slide", "put everything that
  happened this week together not split", "move X after the news segments",
  "split A and B", "title on top, two images side by side". These are
  host-triggered material rebuilds: bump the rev via a `make_rev<N>.py`
  script (regex-based block moves, not manual edits), and watch three
  couplings: (1) removing a slide breaks speaker-notes slide-ID parity —
  delete the notes section AND fold its operational content (cut order,
  pins) into the cold-open notes so nothing is lost; (2) a rebuilt slide may
  reference an asset never published before (e.g. `s4-stripe-newsroom.png`)
  — add it to the website draft whitelist; (3) renumbering is
  self-adjusting via the slide counter, but part labels (`03 / SIGNAL...`)
  should be sanity-checked. Reorder rules seen so far: Signal From Outside
  goes AFTER all news segments; a segment-map/overview slide before the
  segments is removable. Verify layout programmatically (getBoundingClientRect:
  title above both images, image lefts disjoint = side by side), republish
  the draft, and deliver a rendered screenshot of the rebuilt slide.

- **Superseding a partial cron push (verified 2026-08-21 Ep26 rev6 final).**
  When an earlier same-day cron already pushed a partial rev (e.g. only
  `deck.html` modified, no S5, agenda still on prior rev) and you need to
  land the full feature set on top, treat it as another material rebuild,
  not a no-op refresh. Four traps:
  1. **Local main is stale.** `git fetch origin && git merge --ff-only
     origin/main` first; verify `git log origin/main --oneline -3` shows
     the partial cron commit at HEAD.
  2. **`git worktree add` reuses stale branches silently.** Re-creating a
     worktree against an existing branch name checks out the OLD branch
     HEAD, not origin/main. Verify `git -C <worktree> log --oneline -3`
     shows the partial cron commit BEFORE staging; if not, `git worktree
     remove --force`, `git branch -D <branch>`, re-create from origin/main.
  3. **Asset subdirs need recursive copy.** A naïve `shutil.copy` of
     `assets/images/` skips `assets/images/artifacts/`. Iterate
     `src.iterdir()` and recurse into any `is_dir()` child. The deck's
     `src=...` attributes reference files in artifacts/; missing artifacts
     surface as broken-image icons but the validator's local-media check
     still passes (it only checks top-level paths under `revs/assets`).
  4. **Mirror `agenda-draft/index.html` to `agenda/index.html`.** The
     legacy route is committed and served; if you only update
     agenda-draft, gallery deep links stay on stale content.
  See `references/host-triggered-rebuild.md` § "Supersede a partial cron
  push" for the full sequence.

- **Scope post-edit assertions to the elements you changed, never to whole-file grep patterns.** Editing Ep26 rev8 (removing SEG kickers + S-tags), an assertion `'S5 &middot;' not in t` kept failing — the remaining matches were `tag tag-red` spans on the Sources slide, which legitimately keep their labels. Over-broad assertions (`'S1 &middot;'`, generic `'S5'`) produce false-failure loops; assert on exact full strings like `slide-tag">WHAT HAPPENED THIS WEEK` count == 5 and `story-num">SEG` absent instead.
- **Slides are `<div class="slide" id="...">`, not `<section>`; regex block edits must match the actual container.** A `<section[^>]*id="X">` pattern matched nothing and silently reported zero replacements. Use `<div[^>]*id="X"` and verify the subn() replacement counts are non-zero before asserting success. Note also some slides exist in the deck but are hidden (e.g. `s-seg-deepseek` display:none) — apply label edits to them anyway for consistency.
- **Live SHA-equality is the strongest deploy proof.** After pushing any
  rev (full or supersede), poll `curl -s <live-url> | sha256sum` until it
  equals `sha256sum revs/deck.rev<N>.html`. curl 200 + grep canary is
  necessary but not sufficient; the only way to be sure Vercel is serving
  the bytes you pushed is byte equality. Live SHA-equality proves (a) Vercel
  deployed, (b) the deployed SHA matches the local one, (c) no
  CDN/proxy/cache returned stale content.

- **A fix that changes a canonical link must sweep every consumer, not just the surface that failed.** The Aug 16 SEV-2 fix created the invite-rotation cron but left the hardcoded invite in `weeklyclaw-beeper-promo.py`, which republished the dead link on Aug 21. Publishing scripts resolve `weeklyclaw.ai/discord` at runtime through the invite-API gate; no `discord.gg` literal may live in any script. See `references/discord-invite-publication-gate.md`.

- **Worktree dance requires pre-flight HEAD verification.** After
  `git worktree add`, run `git -C <worktree> rev-parse HEAD` and
  `git rev-parse origin/main` and assert equality before staging anything.
  Two failure modes: (a) stale branch (above pitfall), (b) the tool call's
  `workdir` was set to the canonical checkout, not the worktree, so
  subsequent `terminal` calls run `git add` and `git commit` against the
  dirty canonical repo (with untracked `episodes/<N>/` directories from
  prior crons). Always use `git -C <worktree>` or `cd <worktree>` inside the
  same shell command; don't trust the `workdir` parameter alone.

- **CSS present is not element present; vision reads can hallucinate
  (Ep26 rev11, 2026-08-23).** The Ep26 rebuild chain (rev1–rev10) inherited
  the `.discord-qr` CSS from the authority deck while dropping the
  `<a class="discord-qr">` element — a class-name grep returned 4 hits (all
  in `<style>`), so grep "verification" passed while the live deck had no
  QR at all, and no validator gate checked for it. Verify ELEMENTS
  (`<a class="discord-qr"` + child `<img src>`), never bare class names;
  `validate_deck.py` check 5b now enforces this for the QR card. During the
  rev11 render QA, the vision tool confidently described a QR card in a
  render whose img had `naturalWidth: 0` (broken relative path — QA renders
  must run from inside `revs/` where the `assets/` symlink resolves).
  Proof chain for rendered-slide evidence: (1) DOM `img.naturalWidth > 0`,
  (2) programmatic decode of the screenshot — `zxingcpp.read_barcodes`
  (pip `zxing-cpp`) decodes a browser-scaled QR from the full 1600×900
  render where `cv2.QRCodeDetector` returns empty, (3) vision only for
  layout/clipping inspection. Snap Chromium cannot `--screenshot` to
  `/tmp` (AppArmor); write QA screenshots under `$HOME`. Full recipe in
  `references/late-visual-asset-and-qr-edits.md` § "QR decode toolchain".

- **A reassembly rebuild can silently drop nav chrome and the slide-container wrapper (Ep27 rev2/rev3, found 2026-08-28 as "slides arent scrolling").** When a new deck is assembled from content pieces rather than cloned slide-by-slide from the authority, the `slide-counter`/`slideNum`/`slideTotal`, `nav-dots`/`navDots`, `kb-hint` elements AND the `.slide-container` wrapper can vanish. The nav script then crashes on load (`slideTotalEl.textContent` on null), so the deck has NO working navigation — keyboard included — while validate_deck.py still passes (it checks CSS/SVG/symbols, not runtime chrome elements). Guard after every rebuild: grep the deck HTML for `id="navDots"`, `id="slideTotal"`, and `class="slide-container"`, and in the live browser assert `document.getElementById('slideTotal')` exists and an ArrowRight keydown advances the active slide. Also remember decks built before 2026-08-28 were keyboard-only (no wheel/touch handlers) — unusable on mobile; the Ep27 fix added wheel + touch-swipe handlers (650ms lock) and the kb-hint now reads "arrows · scroll/swipe · F".

- **Never hand-roll new slide markup in a cluster rebuild — clone the prior rev's per-slide block structure (Ep27 rev4, 2026-08-28).** First attempt wrote simplified `<figure class="artifact">` markup that passed validate_deck.py but FAILED render-QA overflow on every rebuilt slide, because it skipped the real structure: `slide-brand` div, `glow-orb`, `content` flex row (`flex:1.1` text column / `flex:1.3` image column), inline-styled LIVE pill link, and inline-styled `img` with `max-height` + `object-fit:cover`. Correct pattern: extract a known-good slide block from the prior rev with the regex unit `<div class="slide" id="X">.*?\n</div>\n\n`, then substitute only h2/sub/link/img hrefs/srcs inside it. Two images side-by-side = two `flex:1` children inside the image column. When sed-cloning the render-QA script for a new rev, also update its CANARIES slide-ID list — renamed/clustered slides will otherwise fail canary checks that no longer exist.

- **Tweet-collage fallback when browser capture of x.com fails (Ep27 rev4, 2026-08-28).** x.com may network-error (`chrome-error://chromewebdata/`) or hang CDP screenshot calls. Fallback: fetch the real tweets via `BIRD_ACCOUNT=henry ~/clawd/scripts/bird-env.sh read <id> --json --plain` (author, text, likes), then render authentic-content cards into one collage with PIL (dark bg, rounded cards, avatar circle, name/handle/body/meta lines — see `qa/make_instinct_collage.py` in the Ep27 workspace as the pattern). OCR the collage to verify text, and label it in media-manifest as a rendered collage of verbatim tweets — never fabricate engagement numbers.

- **Episode critique/feedback reports NEVER go to Discord #episodes (Henry, 2026-09-02: "Don't post this in episodes anymore post it here").** Post-episode audits, Geordi notes, lighting/production critique, and Monday feedback summaries belong in the WeeklyClaw Telegram ops thread (`telegram:-1004370723812:337`), not in any WeeklyClaw Discord channel. Discord stays read-only for feedback gathering (engagement metrics, comments). The Monday feedback cron (`b6515f9eb5d9`) was retargeted 2026-09-02 after its prompt's "post them to the WeeklyClaw Discord channel" step leaked critique into #episodes. The episode-publisher cron is exempt: actual episode RELEASE posts to #episodes/#announcements remain its job.
- **daily-topic-list candidate blocks have a strict parser contract (Ep27 rev4 sheet sync, 2026-08-28).** `scripts/weeklyclaw-program-sheet.py` parses `^### Candidate \d+ <title>` headings (a bare `### Candidate 11` with the title only in a `- **Title:**` bullet is SILENTLY skipped) and hard-fails (`RuntimeError: missing fields`) unless the block carries `- **Tier:**`, `- **Sub-stories:**`, `- **Why discuss:**`, `- **Suggested host question:**`, `- **Visual plan:**`, `- **Media URLs:**`, `- **Status:**`, `- **Sources:**`. Copy the full field set from an existing candidate when appending. Also: the public CSV export URL returns 0 bytes unless fetched with `curl -sL -A "Mozilla/5.0"` (redirect + UA required); a plain `curl -s` grep shows a false "row missing".
