# Friday show-prep control-plane findings

Use this reference when changing the scheduled Friday workflow, recovering a missed build, or reconciling prompt/skill drift.

## Scheduler and New York gate

Canonical schedule: `0 15-21 * * 4,5` UTC (Thursday + Friday, effective 2026-08-20 — deck production moved to Thursday per Henry; Friday ticks are a light late-news check). During EDT, 15–21 UTC maps to 11:00–17:00 ET. Gate accepts 11–16; 17 returns exact `NO_REPLY` with zero writes. During EST, the same UTC window maps to 10:00–16:00 ET; gate rejects 10 and accepts 11–16. The UTC superset plus the New York gate is deliberate. Do not replace it with a fixed current UTC offset.

## Build day semantics

- Thursday 11 ET tick is the production BUILD for the episode airing the NEXT day (Friday 4 PM ET). Episode discovery resolves N against that upcoming Friday show date, not today's date.
- Thursday 12–15 ET ticks are ordinary REFRESH (feedback + developments only).
- Friday 11–14 ET ticks are late-news REFRESH, additive-first: prefer ADD (new segment, bench promotion, One To Watch upgrade) over rewriting the lineup. Replacement still requires >=9.0, +0.5 over the lowest unpinned story, and explicit re-approval after any host approval.
- Friday 15 ET FREEZE and 16 ET HANDOFF are unchanged.
- Missed-BUILD recovery window is now the first qualifying tick Thursday or Friday 11:00–14:00 ET.

## One procedural source

The skill is the canonical procedure. Keep the cron prompt thin: mission, schedule/gate, workspace, attached skill/template, Telegram identities, boundaries, and completion receipt. Duplicating the research, media, Cursor, freeze, and validation contracts in both prompt and skill causes drift.

## Missed-BUILD recovery

- Any Thursday or Friday 11:00–14:00 ET tick without valid same-week state performs full BUILD.
- At Friday 15:00 without valid state: perform a bounded abbreviated build-and-freeze only if evidence and artifacts can pass; otherwise deliver BLOCKED.
- At 16:00 without a usable package: read-only BLOCKED handoff.
- Lock expiry must be shorter than hourly cadence. Use a heartbeat for long Cursor work so a healthy run is not mistaken for stale.

## Editorial authority and artifacts

The agenda is the canonical editorial source. Complete it from the agenda template before rendering. The complete package is seven artifacts:

1. agenda
2. deck
3. speaker notes
4. consolidated talking points
5. Henry view
6. Andy view
7. host cheat sheet

Cursor derives the six presentation/host views from the staged agenda. Success requires all seven to exist, read back, and share revision/story-set identity. Exit 0 is not success.

## Permanent weekly video anchor

Signal From Outside is an every-week anchor, not an optional rotating block. Pull the dated video-research talk-track from the authorized share, verify the source and media, then integrate its spoken narrative directly into the agenda. Optional rotation is Tool Fight, Builder Demo, or Audience Question. Cut/compress the optional block before the video anchor.

## Story count and clustering

- Five is a ceiling/target, not a padding quota.
- Automatically select only clusters clearing the evidence and quality floor.
- If only three or four qualify, air fewer and show the bench.
- Rescore a merged cluster as one editorial unit; preserve constituent scores.
- Each constituent belongs to one selected cluster unless an explicit cross-reference explains the overlap.

## Host authority

- Henry user ID `855505513` and Andy user ID `7615999206`: lineup approval, swap/drop/pin/order, root promotion, and website publication.
- Andy additionally has workflow, production, video-cue, ownership, and section-content authority inside drafts.
- Other senders cannot approve or promote; ignore and log commands.

## Freeze interpretation

Recommended standing interpretation: watch until showtime, mutate until 3 PM.

- 11: BUILD
- 12–14: mutable REFRESH
- 15: final verification and FREEZE
- 15–16: breaking-news monitoring; exceptional items produce proposal-only alerts, no artifact mutation
- 16: read-only HANDOFF

If unvalidated at freeze, root artifacts remain untouched. Handoff names exact usable revision paths and labels them UNVALIDATED.

## Deterministic validators

Before review-card delivery and again before promotion, mechanically check:

- **prior-episode template authority**: the deck's visual template must be cloned from the prior APPROVED episode (discovered by scanning `showprep/state.json` for the highest `approval_state: APPROVED`), not invented. Run `validate_deck.py` with the authority deck as the third argument. See `references/prior-episode-template-authority.md`.
- talk-track structure: host-specific format (Henry bullets/optional line/handoff; Andy fallback prose/handoff). No duplicate bullets inside Andy's fallback prose
- Hot Take / news non-duplication: the Hot Take proposition, framing, and question must differ from every What Happened This Week segment
- finished host-document precedence: if a finished, ordered host document exists, its picks override raw candidate scoring; verify and record the authoritative path
- corroboration retry: every exclusion after a failed first corroboration search must show at least one retried query with materially different terms, entity names, date ranges, or source types
- cluster exclusivity and post-merge scoring
- artifact paths: no stale staging `output/` references in promoted files
- seven-artifact manifest and shared revision/story hash
- deck/notes slide ID count, order, uniqueness
- local media resolution, external verification receipt, cue/fallback, no autoplay
- canonical theme markers/hash and real `weeklyclaw-logo` SVG symbol (not the invented `claw-mark` string)
- sponsor-asset provenance: every `assets/sponsors/` file matches the prior-episode sponsor asset by sha256
- invented-logo rejection: no `<symbol>` or inline SVG drawing a claw/logo/brand mark absent from the authority deck
- 1600x900 render QA: no clipping, overlap, or report-like density
- runtime from word count plus clip/demo durations, under 45 minutes
- evidence/runlog completeness

## Degraded mode

If all Cursor routes fail, never disappear. Deliver the verified agenda and any valid notes/cheat-sheet artifacts, mark the deck BLOCKED, preserve evidence, and name the exact missing contract.