# Native production profile — 2026-10-04.1

Use with [editorial-direction.md](editorial-direction.md), [production-quality.md](production-quality.md), [qa-contract.md](qa-contract.md) and [render-integrity.md](render-integrity.md). This is the current document profile; file presence is not runtime reload evidence, episode approval or publishing authority.

## Entrypoint and stage selection

1. Identify the requested deliverable: full landscape episode, proof montage, or vertical Short. A proof or Short never satisfies a full-episode request. Record episode, revision, aspect, complete programme duration, native editor and renderer versions, exact project hash, source inventory/hash, and user constraints.
2. Run scripts/dependency_audit.py on the linked package before claiming the full workflow is available. It inventories local Markdown links and declared runtime prerequisites, not creative/media PASS. Verify actual transferred bytes, including the thumbnail bundle, and obtain missing dependencies from their owner; block only dependent operations.
3. Follow the editor's stage-specific reference routing. Load publisher requirements before final encode and its operational references/thumbnail skill before their stages. Preserve authentication, channel identity, approval, duplicate and distribution gates.
4. Record the actual approved prior master hash plus matched-size comparison samples. A missing baseline remains an explicit unresolved dependency; do not invent a hash or use a new unapproved preview as the approved baseline. Ask for a scoped decision if it cannot be recovered. Baseline style comparison is never approval for a new edit.
5. Choose one actual native production path. For requested Kdenlive, use editable camera, audio, text and source tracks and Kdenlive/MLT native effects and render. External tools may inspect/probe/hash/extract evidence or generate a source asset, but must not secretly replace requested native editing with a flattened external master. A project filename or XML file alone does not establish native render proof.

## Geometry and source-quality decision

Use aspect-preserving transforms from the highest-resolution verified originals. Landscape group compositions use full-height portrait panels across the frame, with matched heads and no decorative top/bottom bands. Full-width solos require sustained actual-speaker evidence. Do not replace these directions with smaller padded strips or wide room views; follow [editorial-direction.md](editorial-direction.md).

The current `native-evidence-2026-10-04.1` profile permits source-limited enlargement only with an explicit hashed review exception for the exact fill transform and its disclosed quality tradeoff. Prefer original detail, compare native proof at matched display sizes and retain face/gesture safety. No universal scale factor applies. Do not distort, reconstruct faces, heavily sharpen or use blurred filler to disguise a limitation; more bitrate cannot recover absent detail. The older native/legacy profiles remain distinct and strict.

For each group state, measure on real native-rendered frames at delivery size:
- viewport top/bottom and participant crown, eye midpoint and chin in pixels
- headroom = crown minus viewport top; normalize by viewport height when heights differ
- face height = chin minus crown; compare max/min, normally ≤1.15
- eye-line spread, normally ≤50 px at 1080p (30 px is the tighter end of the existing 30–50 px guidance)
- headroom spread: use a declared episode-specific tolerance chosen from the reviewed proof; there was no inherited fixed numerical headroom tolerance
- left/right face and meaningful gesture envelope; reject any clipped face, crown, chin or required gesture

Measure neutral and movement/laughter/posture frames near early, middle and late sections for every applied crop. Sampling is not complete motion clearance: inspect affected intervals or use a documented dense scan plus close review of extrema. Record source limitations and reviewer/user disposition; never relax tolerances silently. Tune per-camera crops and common apparent face scale while retaining frame fill; any source-limited enlargement needs the specific reviewed exception above.

The portable footer helper preserves the established panel and type sizes. On non-macOS systems set WEEKLYCLAW_FOOTER_FONT_REGULAR and WEEKLYCLAW_FOOTER_FONT_BOLD to explicit available font files; it records their hashes beside the output. Any substitute requires actual-render and mobile comparison. Never silently substitute fonts or redesign the established section panel.

## Native graph proof

The legacy quality_gate.py builds a specific strict FFmpeg two-up graph with fixed footer camera box and green pad. Keep its profile and historical receipts distinct; it cannot certify current native full-frame layouts or enlargement exceptions. Do not fabricate a legacy plan to obtain PASS while rendering another graph.

Use scripts/native_geometry_evidence.py for the narrow checks it actually supports: source crop/scale bounds, aspect, viewport fit, matched eye/face/headroom measurements, hashes of native project/proof images, and exact XML property bindings. Each transform must cite the actual native effect property and owner, with an explicit conversion explanation. Unsupported/keyframed native semantics need a reviewed adapter or manual native effect inspection; XML equality alone does not prove that a proposed transform models MLT semantics. Record native adapter/manual review as pending until verified. This script deliberately returns CHECKED_SUBSET_PENDING_REVIEW, never release PASS.

Use the [editorial evidence schema](editorial-evidence-schema.md) for current group-state and enlargement-review fields and for the shared frame map, cue, solo and mark plan. Run `python3 scripts/editorial_evidence.py <plan.json> --report <new-report.json>` before the native proof: it checks declared mapping, cue ordering, hashed shot evidence and transparent global-mark coverage. Read its limits and inspect actual speech/native output separately; matching declarations are not perceptual verification.

Bind proof receipts to the exact native project and all source/asset hashes, renderer version/settings, inclusive/exclusive frame semantics, and output hash. Changes invalidate affected proof/cache. Inspect actual project effect settings, then actual moving output. Native editor UI screenshots, render queue evidence and a reopened editable project supplement, not replace, encoded-media tests.

## Privacy and evidence

Treat every desktop/screenshare interval as public evidence, private/setup, or unresolved before use. Full-frame private history, tabs, DMs, notifications, account details and unrelated chat must be excluded, not merely made less prominent. Inspect full encoded frames including transitions/edge frames. Use verified clean source visuals instead; if redaction is appropriate, verify every affected frame. Absence of private content in a Short says nothing about the full episode.

Use genuine primary-source captures or faithful deterministic typesetting with original URL, retrieval date, asset hash, exact labels/units/effort/version and timeline interval. Preserve vendor attribution and methodological qualifiers. Never present generated imagery as an authentic source screenshot or benchmark chart; numeric comparisons require verified values and deterministic typesetting. Inspect source text at native and mobile sizes. Cover every retained occurrence of a substantive error, keep corrections neutral and in the established footer with live speakers, and keep readable full-screen source evidence distinct from an information note.

Retain the current episode's fact-check and correction ledger, including unresolved claims and source limitations; partial/secondary verification is not independent proof. Canonical host labels stay AndyML and HiM. Verify the guest's current identity and do not inherit another episode's name or guess a handle. Resolve ambiguous ASR words audibly or leave them unresolved.

## Audio, captions and ending

Inventory raw WAVs and aligned video separately. Verify raw offset sign and drift against embedded audio at start/middle/end; filename agreement is insufficient. Do not sum every live mic indiscriminately where it produces bleed or doubles speech. Use bounded native gain/mute/duck/crossfade decisions while preserving speech and natural overlap. Keep repair A/B samples and final mix evidence.

Target dialogue −16 to −14 LUFS and true peak ≤−1.5 dBTP on the final encoded audio, with usable encoding margin. Historical broad limits (−18 to −12, ≤−0.1) are not the production target. Measure the final candidate and document exceptions; never round a borderline peak into compliance. The media audit's ebur128 parser is a coarse one-decimal screen; its additional 8× SoX/float64 estimate retains precision and its interpolation limitation. Missing measurement support leaves that check blocked, not silently rounded to PASS.

Retiming captions from EDL is only structural correctness. Check actual words, pace, cut-spanning cues, reading time and native overlay safety against the final timeline. Transcripts, correlation, waveforms and loudness cannot prove perceptual sync/listening. Record who actually listened, exact hash and coverage. Leave listening/word timing pending if unavailable; supply exact-master playback samples, not an invented PASS.

Preserve the authorized original outro hero and music with hashes and original provenance. Verify the depicted/clickable domain against the confirmed canonical weeklyclaw.ai source; do not silently substitute a redesign, unrelated .com site or a reconstructed portrait. If the supplied original conflicts with live branding, surface that specific conflict. Default remains 10-second card, music starting 3 seconds before it, clean fade; verify exact native and final-render intervals.

## Stop costly mistakes before the full encode

Deliver a short native moving proof covering opening, every layout and individual source graphic, all visible faces during motion, every changed transform/boundary and the original outro/music. Inspect full diagrams, rail boundaries and pan/zoom extrema, plus the fixed transparent global mark in every state. Compare source-sized frames and actual effects. Clear represented geometry, text, privacy and technical mix defects before the long render. A montage clears only represented states; it does not certify omitted programme or listening.

Render full-length only from the verified project snapshot. Record expected frame count from EDL and explicit additions; never reuse a proof-only index as the full concat. After encoding run media_audit.py --full-decode with exact dimensions, fps, duration, audio channels and strict current peak threshold. Verify final whole-file hash separately from elementary-stream hashes; they are not interchangeable. Inspect all junctions, beginning/end, changed shots, full privacy-sensitive intervals, captions, and audio. A complete decode does not prove no freezes, correct facts, privacy or listening.

Preserve the 4,000 kbps average-video house gate for 1080p upload until explicitly revised. CRF alone does not guarantee it; bitrate padding cannot restore detail. Measure video packet bytes/duration if stream bitrate is absent. Use the best original/intermediate and compare a moving source/benchmark excerpt before choosing encode settings. The audit records the bitrate method; if metadata and packet measurement fail, keep the gate unknown/failed. Audit the requested deliverable's aspect; full-episode routing remains landscape and vertical clips remain separate.

## Handoff

Use separate statuses: EDITABLE_PROJECT, PROOF_REVIEW, FULL_MASTER_TECHNICALLY_CHECKED, PERCEPTUAL_REVIEW_PENDING, FULL_MASTER_REVIEW_READY, UNLISTED_FULL_EPISODE_REVIEW, RELEASE_APPROVED, PUBLIC_VERIFIED. Include explicit failed/pending gates rather than promoting status by filename. A user acceptance of a disclosed limitation is a scoped acceptance, not a technical/perceptual PASS.

Send the publisher the full landscape programme hash/runtime, sources, QA, captions, chapters, exact thumbnail approval and intended visibility. Verify YouTube channel tuple, full runtime and playback after Unlisted upload. Do not substitute Shorts or proof reel. Unlisted upload is neither public-release approval nor proof of final playback quality; preserve all publisher release gates.

## Continuation and deployment evidence

Reconcile current immutable receipts against progress/scheduler/rollout prose before resuming. A later exact completion receipt supersedes stale pending rows; do not repeat sends, account recovery or source ingestion because an older next_action says pending. Recheck current platform state where the next authorized action needs it. Keep manifests distinct by host, recording/take and exact files; counts from separate source workflows are not interchangeable.

Maintain one canonical owner with no duplicate manager. Honor current verified owner instructions for a single episode worker without creating a new owner/scheduler on every wake. Distinguish a completed or gated episode run from a dispatcher that has future authorized work. Installing these skills makes no scheduler, cron, job or account changes.

Preserve the written 4 Mbps house gate when reconciling deployed validators. Back up affected files, preserve unrelated newer work, and verify which exact verifier hash each runtime consumes. Missing dependencies or unresolved version conflicts block only their affected step.

Distinguish actual approved master pixels, later verified standing directions and unapproved previews. A prior master's treatment does not override the current group-first/full-frame/global-mark direction, and a recommendation does not approve a candidate. Preserve the approved baseline and confirm the latest relevant reference instead of freezing one episode as permanent style authority.

If the supplied original outro's domain conflicts with a current owner request or installed canonical branding, preserve the authorized original, verify the actual conflict and ask the specific choice. Do not silently rebuild the ending or adopt a different domain from stale context.

Before podcast backfill or feed changes, verify current existing-show/feed identity and duplicate risk. Historical sign-in blockers can be superseded by later successful access. Do not create a replacement show or switch a feed without current authority and verified destination identity.
