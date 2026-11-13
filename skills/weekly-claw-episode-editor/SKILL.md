---
name: weekly-claw-episode-editor
description: Turn raw Weekly Claw Riverside, OBS, desktop, or previously edited recordings into a coherent, branded episode master. Use for independent-track ingest, transcript-led editing, group-first multicamera layouts, source visuals, targeted audio repair, captions, established endings and exact-master verification before publishing.
---

# Weekly Claw Episode Editor

Produce one immutable-source, reproducible edit and a machine-checked final master. Keep editing separate from YouTube publishing.

## Production direction — 2026-10-04.1

Before editorial planning, read [references/editorial-direction.md](references/editorial-direction.md) for group-first coverage, full-frame crops, spoken-cue visuals, the global transparent mark, truthful captions and clip-specific direction. Apply its interview-format acceptance check before the long render and to the exact final master. Use [references/native-quality-profile.md](references/native-quality-profile.md) for native render evidence. Episode identities, values and exceptions remain in that episode's ledger. The document version does not establish that a running task has reloaded it.

## Start

1. Resolve the exact episode and source paths. Never infer “first,” “other,” or “latest” from nearby context.
2. Create `tasks/todo.md`, `tasks/lessons.md`, `work/<episode>/`, and `outputs/` when absent.
3. Preserve source media and rollback masters while editing or correcting an unaccepted episode. Use new versioned or `editorial-review` output names. Apply the cleanup policy below as intermediate work becomes obsolete and after the exact YouTube upload is accepted.
4. Read [references/session-playbook.md](references/session-playbook.md) for ingest, editorial, layout, audio, visual, and outro rules.
5. Read [references/qa-contract.md](references/qa-contract.md) before designing tests or declaring completion.
   For alignment, render caches, moving demos, corrections, captions, or final audio QA, also read [references/render-integrity.md](references/render-integrity.md).
6. Before camera/layout/colour work, read [references/production-quality.md](references/production-quality.md). Compare the approved baseline with current editorial direction, assess this recording's cameras, and choose the actual preflight branch from [references/native-quality-profile.md](references/native-quality-profile.md): the legacy FFmpeg helper certifies only its strict historical graph; current native compositions use the reviewed native-effect mapping, current profile evidence checks and moving proof. Hold the long render until mapping and proof are reviewed; the subset checker alone is not a render PASS. Information notes retain the established section footer. This applies to scheduled runs too.
7. Before execution, read [references/run-contract.md](references/run-contract.md), create or reconcile the episode's requirement and capability ledger, and preserve current skill/reference hashes. Use it at every phase transition and before any completion, handoff or cleanup claim. A plan-only audit or empty `next_actions` list cannot establish completion.
8. Start or reuse the one run-scoped progress manager described in [references/progress-manager.md](references/progress-manager.md). Record its native automation ID and exact next action in `work/<episode>/progress-manager.json` before the first material browser, render, or publishing-preparation step.

All Riverside and publishing web actions must use only the Codex app's built-in
authenticated browser. Do not open Riverside in Chrome, Playwright, or any
external browser session; do not substitute another browser when a transfer or
page is blocked. Record the exact Codex-browser recovery action instead.

## Dependency-aware continuation and project ownership

Use the existing authorized project owner and progress manager; do not duplicate work or create a second scheduler. Verify live recording inventory before concluding that no recording is actionable. Record unavailable discovery as blocked, with evidence and a recovery action. Block only the stage dependent on an unavailable capability; continue independent authorized editing, rendering and QA. Preserve resumable state and never guess an episode identity.

## Post-stream live-replay privacy guard

Check live-replay privacy as an independent task, not a pre-edit prerequisite.
When YouTube access is available, open Studio in the same Codex browser and inspect the target channel's
`Live` tab. A completed replay is a separate object from the edited episode
master. For the current episode, identify a row that is explicitly `Streamed`
and titled `Weekly Claw - Episode <N>, Live`; verify the target channel tuple,
episode number, stream date, runtime, and video ID against the current run.
Only at least sixty minutes after the verified stream end, when that exact
replay is `Public`, change only the replay to `Unlisted`, save,
and read the visibility back from Studio and the watch URL. Never change an
upcoming/scheduled stream, an unrelated episode, an already-Unlisted replay, or
the edited master. Record the before/after visibility, exact ID, channel tuple,
and verification time in `work/<episode>/live-replay-privacy.json` and in the
release manifest when one exists. If the channel, episode association, or
account cannot be verified, stop before changing visibility and report the
precise human choice needed for that visibility change. Continue independent
ingest, editing, QA, and preparation while that check is pending.

## Run-scoped progress manager

Every material run has one heartbeat supervising the canonical owner's processes and the
durable episode state. The manager checks all phases—not just Riverside ingest—
and performs the smallest safe recovery when progress stops. It must reconcile
the live process, filesystem, and current page before relaunching anything, and
must never start a second worker for the same episode. Reuse an existing live
manager for the exact episode/worktree instead of creating a duplicate on a
continuation or poll.

Use exactly one native Codex heartbeat as the project manager, attached to the
canonical pinned **🎬 Weekly Claw** task identified above. A standalone project cron is not a
manager: each cron tick starts a fresh conversation and must not be used for
this control plane. On every tick, resume and steer the same manager thread;
never create a new manager thread for a poll, continuation, recovery, or
episode. This single combined heartbeat handles Friday due checks and progress
supervision. It may resume transfers/renders, refresh the exact recording,
retry one failed block, reconcile state, or resume authorized work in this same
task. The heartbeat grants no new publication authority: the canonical owner
may execute only already-authorized actions after all applicable gates pass.
Never bypass a human gate or infer acceptance of platform terms.

Apply the lean-runner attributes: one owner, one worker per resource key,
resume-first continuity, compact delta-first state, immutable receipts, and
bounded repair attempts. Treat process existence, timestamp churn, and receipt
appends as liveness only; semantic gate/count changes are progress. A separate
observer may report state but never mutate or restart the run. Preserve every
failed attempt and do not launch a second manager when the canonical owner is
live or resumable.

Keep compact delta-first checks and the existing phase cadences. A growing
transfer or active render is progress. After 15 minutes without progress,
document one smallest recovery; after three failed recovery attempts and a
fresh view, stop only for an authentication/CAPTCHA gate, missing/failed
required source, repeatedly non-progressing export/render, or an explicit human
approval/irreversible choice. Worker exits, transient tool errors, failing
tests, stale caches, and parent-session ceilings are recoverable states. On an
external ceiling, record `INTERRUPTED_INCOMPLETE` plus the exact next action.

When the run reaches `DONE`, or every remaining action depends on a genuine
unresolved gate, write the corresponding run state. Keep the combined scheduler
ACTIVE for future Friday triggers, making quiet no-ops when nothing is due or
actionable; do not keep retrying a genuinely gated stage. Keep the complete
state schema and recovery evidence in [references/progress-manager.md](references/progress-manager.md).

## Build evidence before editing

- Inventory every camera, screen share, raw audio track, transcript, export, and previous master.
- For Riverside, use only the Codex built-in browser to retrieve all aligned CFR camera tracks, every split/reconnected participant track, all screen shares, and raw WAVs. Do not treat the composite export as the complete source set, and never fall back to Chrome, Playwright, or another external browser.
- Treat Riverside exports as a two-phase operation: request generation, then return to download the generated file. A `Ready` badge, generation request, toast, or queued browser download is not a completed source.
- Maintain `work/<episode>/ingest-state.json` with one row per required file and the states `DISCOVERED`, `GENERATING`, `READY_TO_DOWNLOAD`, `DOWNLOADING`, and `VERIFIED`. Record the recording/take, participant, track ID, requested format, expected duration, local path, size, and SHA-256.
- Poll Riverside generation about every 30–60 seconds and active local transfers about every 10–30 seconds while progress continues. When generation finishes, mark the row `READY_TO_DOWNLOAD`, click the download action again if Riverside requires it, and then mark it `DOWNLOADING`. Do not end a scheduled run merely because Riverside says a file will be ready in a few minutes.
- Accept a download only after its temporary extension is gone, its size is stable, `ffprobe` succeeds, duration/media properties match the Riverside inventory, and SHA-256 is recorded. Reconcile the local verified count against the required-file count before editing.
- If progress stalls for 15 minutes, refresh the recording, re-open the exact track, and retry the smallest failed generation/download step. Riverside may attach a `variant="upgrade"` or promotional marker in the DOM while the visible download control remains actionable; never classify that marker alone as an entitlement blocker. Click one exact visible option, monitor the local transfer through completion, and reconcile the resulting file before deciding. Report a blocker only after three documented recovery attempts and a fresh Riverside view proves a missing/failed track, authentication gate, or non-progressing export. Temporary generation or an active growing transfer is not a blocker.
- Treat a browser download event as transport evidence only, not proof of source identity or completion. If a hidden-tab attempt times out while a visible foreground Codex tab shows the exact Riverside row and a growing `.crdownload`, preserve that transfer and do not restart it. Reconcile the completed file to the exact participant/track/duration/resolution row; aligned exports may contain leading black or padding, so inspect per-stream start and duration, `blackdetect`, and sampled active frames before accepting. Record the unchanged file, container and active coverage, size, SHA-256, and exact row evidence. A visible-tab correlation is a proven recovery path for the run, not proof of root cause or permission internals.
- If the hidden attempt produced no transfer, reopen the exact recording in a visible foreground Codex tab, re-resolve the exact row, register the documented download listener before clicking one exact visible option, and observe the filesystem; never bypass an access restriction. Scope every state transition and receipt to its exact `row_id`, and compute `verified_file_count` from per-file path, size, and SHA-256 validation rather than trusting a copied or stale aggregate.
- Check `work/<episode>/` for optional local supporting captures such as Discord. Use them only when editorially relevant; absence must never block the edit.
- Write a source manifest with participant, track ID, path, duration, frame rate, resolution, audio format, and timeline alignment.
- Probe each stream's actual coverage; a long screen-share video can have an audio stream that ends much earlier. Verify raw-WAV offsets against aligned camera audio near the start, middle, and end before mixing.
- Enumerate expected participants and actual presence intervals. Verify group coverage; require a solo only where a sustained contribution and direct speaker evidence justify it.
- Transcribe the complete recording locally when a matching transcript is unavailable.
- Review transcript and sampled video end to end. Identify clean opening, recoverable discussion, technical failures, accidental endings, restarts, and post-show talk.

## Plan before rendering

- Write an EDL in original source time with explicit keep/remove reasons and one shared source-to-programme map for every trim and insertion.
- Decide whether the recording supports a full episode or only focused clips. Do not force a broken full episode.
- Write a machine-readable layout plan. Include source start/end, layout, visible participants, screen source, and duration for every block.
- Define reproducible per-participant framing transforms for group layouts.
  Normalize eye line, face scale, and headroom instead of applying one identical
  crop to cameras with different compositions. Choose each tile crop from the
  actual face/eye position, not geometric center by default; reject crops that
  clip a face, crown, chin, or meaningful gesture.
- Default to full-frame group views. Use a full-width solo only for a sustained, verified actual-speaker contribution; no automatic energy or duration threshold decides it. Follow the framing and reviewed source-quality tradeoffs in [references/editorial-direction.md](references/editorial-direction.md).
- If a retained interval has live audio but a verified technical outage affects all participant video, use only a clearly labeled static fallback from approved real episode frames with a small audio indicator. Preserve original audio/timing and record the source frame, interval, fallback hash and rendered proof; do not imply live motion. This does not apply when a guest leaves the camera: use the remaining real participants, never a frozen or borrowed guest image.
- For source material, use full-screen readable evidence or a large source with participant rail. Never reduce slides or articles to unreadable decoration.
- Sponsor ads are an explicit exception to the participant-rail default: start each ad with its actual moving video full-screen, not embedded in a slide or surrounded by hosts. Follow the sponsor playback instructions in `references/editorial-direction.md`.
- Treat Discord as supporting evidence, not ambient footage. Show only relevant excerpts at matching discussion moments; tightly crop or recreate them and conceal unrelated/private usernames, avatars, servers, channels, notifications, DMs, and messages.
- Preserve relevant presentation coverage throughout retained discussion. Do not independently omit a slide, chart, screen scroll or demo to simplify the edit, save render time, or keep the hosts on screen. A written editorial reason alone does not authorize dropping relevant material; a few representative inserts do not fulfil the presentation. Only an explicit user instruction covering that omission changes the requirement.
- Maintain `work/<episode>/presentation-coverage.json` with one row per distinct relevant slide/chart and meaningful screen/demo interval. Bind source ID/path/hash and source time, spoken cue, mapped programme interval, intended still/motion treatment, disposition and exact-master verification. Exclude duplicates, setup/dead time, material outside retained discussion, or private/unusable content only with an evidence-based reason; such exclusions must not conceal a missing relevant visual.
- Reconcile every inventory row with the layout plan before the long render. If required material is missing, unsafe or unusable, continue independent work and recover or prepare a privacy-safe equivalent from authentic evidence. Record any unresolved gap as incomplete; do not silently replace it with talking heads, an unrelated still, or generated evidence. A scoped fallback or omission needs the user's explicit acceptance before editorial completion or upload.
- Use the storyboard to plan, then deliver actual native moving proof of every layout/source graphic, changed transform, motion extreme and join before the long render.

## Repair audio deliberately

- Mix from independent participant audio when available. Preserve sync and normalize dialogue consistently.
- Target natural YouTube dialogue near -16 to -14 LUFS with true peak at or below -1.5 dBTP unless the source requires a documented exception.
- Treat human background speech as a speaker-separation problem. Generic denoise or voice isolation preserves all human voices.
- Encode the exact reported interval and retained speaker in a failing regression before repair.
- Use speaker-targeted separation for the retained person, then optional voice isolation for room noise.
- Export original/cleaned A/B clips. Verify transcript retention, waveform behavior, boundary transitions, and perceptual result.
- Replace only the damaged interval with roughly 50 ms crossfades. Preserve unaffected video bit-for-bit when possible.

## Add evidence and finish

- Fact-check names, roles, companies, dates, attribution, statistics, and qualifiers against primary sources.
- Show original posts, articles, charts, launch pages, or demos when they materially support discussion.
- Use correction cards for substantive spoken errors. Keep original source IDs and pages beside edit crops.
- Keep notes helpful, neutral and source-led, not adversarial. Prefer a concise label such as “Sanders’ AI pause proposal” with the verified source link over “no ban” or gotcha wording. When a material distinction needs correction, explain it calmly and precisely; do not suppress the distinction. Henry's 2026-09-05 preference applies to future edits, not retroactive changes to an approved master.
- Use authentic benchmark/source evidence and polished GPT Image supporting artwork with actual icons/fonts as distinguished in [references/editorial-direction.md](references/editorial-direction.md). Anchor every context-image onset after its spoken introduction and inspect the full transformed content, including motion, at delivery and mobile sizes.
- Preserve the established original closing picture and music; verify canonical destinations before any requested link update.
- Use one alpha-transparent stacked Weekly Claw programme mark fixed at the global bottom-left across cameras, context images, archive and outro, with no plate or tile-relative movement. Prevent baked duplicate programme marks while preserving authentic source logos. Follow [references/editorial-direction.md](references/editorial-direction.md); preserve approved previous masters.
- Place participant names as tile-local white labels right-aligned within each active participant tile on a shared name baseline, with consistent inset, font, size and contrast. Use canonical host labels `AndyML` and `HiM`; confirm every guest's current name and presence from episode evidence. Henry’s standing host-handle defaults are `AndyML → @alauppe` and `HiM → @Iamhenrymascot`; use them unless Henry corrects them. Canonical spelling check before render: Andy’s handle is `@alauppe` (a-l-a-u-p-p-e); the transposition `@aluappe` is a known error that shipped on E36 and must never be rendered. Add a guest handle only when Henry supplies it for that episode. Render supplied handles smaller directly beneath the corresponding name. Keep labels clear of faces, footers, source visuals and the fixed global mark; label only visibly present participants.
- When branding or name treatment changes, require actual-render previews at representative solo, two-up, three-up, screen-share, and outro states plus a mobile-size legibility check. A still mockup is a review aid, not evidence that the final render is correct.
- Default outro: 10 seconds, with music beginning 3 seconds before the end card and fading through it.
- Keep source analysis, EDL, layouts, audio repair, visual overlays, outro, render, and QA as separate stages.
- Render resumable independent blocks, concatenate them, then mux verified audio.
- Apply the publisher's master encode standard before the final encode. Preserve compliant block video through concat when possible; measure the exact upload master's video bitrate instead of assuming block quality survived muxing.

## Cleanup and accepted-upload retention

Where the current operator has applicable authorization for routine cleanup, remove obsolete generated proof packages, duplicate intermediate media and superseded temporary projects once their useful edit JSON, settings and failure evidence are saved and a usable current project/master remains. Do not accumulate a full portable copy of the source set for every proof. Confirm file identity, dependencies and actual free space; scope deletion to this run.

Only where existing authorization covers deletion, delete this episode's local raw recordings and source copies after the exact corrected YouTube upload has completed processing, its account/visibility/picture/audio/ending have been verified, and YouTube's checks pass. Henry clarified on 2026-10-28 that “accepted on YouTube” means “After YouTube checks pass”; a separate personal editorial approval is not required for this cleanup. Transfer completion or a processing badge alone is insufficient, and a candidate already known to be missing content must be corrected before cleanup. Confirm that applicable deletion authority covers the exact scope before acting.

Keep the accepted master, thumbnail, captions, metadata, transcript/EDL/edit JSON, source hashes/IDs and release/QA receipts. Audit packaged `.tsrct` media and downloaded copies as well as loose sources so hidden raw duplicates do not remain accidentally; retain only dependencies still needed for an authorized unfinished destination. Record deleted paths, acceptance evidence, space recovered and any resulting source-relink limitations. This policy supersedes blanket source/prior-master retention after acceptance; it does not authorize deleting remote Riverside recordings or YouTube objects.

## Spotify podcast delivery

When Spotify delivery is requested, use only the Codex app's authenticated in-app
Browser and the existing Weekly Claw show. Treat the Creator Studio catalogue as
the source of truth for duplicate checks: inspect the current rows and match the
episode number, title, runtime, format, and status before creating a new item.
Never create a replacement show or silently duplicate an existing episode.

### Spotify email-code login

Use the authorized existing session and verify the intended show before upload. If signed out, use the approved account and supported sign-in flow. Retrieve only the fresh code for the current attempt through an authorized mailbox; verify its sender, recipient, timestamp and purpose. Enter it only into the official login form. Never save codes or message bodies. Record any access failure and use supported recovery; do not sign out a working session to test.

After code submission, verify the existing Weekly Claw show and episode
catalogue. Preserve the authenticated tab for continuation. Do not sign out a
working session merely to test this procedure.

For long video masters, prefer a verified audio upload when the video path is
slow or unreliable. Extract a new, versioned MP3 from the exact approved master
with ffmpeg (normally 128 kbps, preserving the full runtime), then verify it with
ffprobe, stable file size, duration, stream metadata, and SHA-256 before opening
the Spotify upload flow. Do not upload a render preview, wrapper, or stale
revision. Keep the source video and extracted audio immutable.

Upload one episode at a time. Wait for Spotify's upload completion and inspect
the details page before entering title and description. Publish only when the
episode metadata is complete and the user has authorized publication; verify the
success dialog and then re-read the catalogue row as `Published`. A successful
upload, a saved draft, and a published episode are separate states.

If a large MP4 upload stalls, cancel only that in-progress upload, preserve the
failure evidence, extract audio from the same verified master, and retry once as
audio. Do not start parallel retries or create another show. If Spotify's public
show page lags behind Creator Studio, record the exact missing titles and treat
that as propagation pending—not as proof that the upload failed. Leave unrelated
empty drafts unchanged unless the user explicitly authorizes deletion.

For each delivery, record the source master, extracted-audio path/hash when used,
Spotify episode ID, format, runtime, metadata, Creator Studio status, public URL,
and any propagation or authentication blocker in the episode release manifest.

## Verify

Run:

```bash
python3 scripts/media_audit.py <final-master> \
  --width 1920 --height 1080 --sample-rate 48000 \
  --full-decode --report work/<episode>/media-audit.json
```

Add `--compare-video <source-or-prior-master>` when video should remain unchanged.

Also:

- Run focused regressions for EDL duration, all participants, correction cards, audio windows, outro, and frame/timestamp continuity.
- Review opening, closing, regular samples, every edit junction, and every repaired interval. In representative group frames, verify that participant eye lines, face scale, and headroom feel deliberately aligned.
- Verify full decode, runtime, constant frame rate, BT.709 metadata, audio channel layout, loudness, captions, and output filename.
- Reject self-declared JSON flags as proof. Test rendered media.
- Verify every required presentation row in the exact final encoded master: inspect onset, readable content and exit; sample multiple times through moving material to establish genuine motion and meaningful action. Bind programme timestamps and actual frames/playback evidence to the master SHA-256. Reconcile expected, included, excluded and unresolved counts; missing rows or unsupported omissions fail editorial coverage and hold upload. Technical decode, an earlier proof, or a handful of source cards cannot pass this check.
- Bind QA and approval to the exact episode, revision, and master SHA-256. Keep technical checks and perceptual listening separate; an unavailable listening capability leaves that review pending with exact-master playback samples.
- Run Codex review after focused tests. Resolve or explicitly reject each finding.

## Handoff

Reconcile the requirement ledger under [references/run-contract.md](references/run-contract.md) against the exact master before reporting completion. Report final path/hash, runtime, streams, EDL summary, source and presentation coverage counts, layout coverage, audio treatment, corrections, caption-word and listening status, outro, test results, full-decode result, and every failed, pending or scoped-exception requirement.

When upload is requested, pass only the exact verified master, mapped cues, reconciled presentation-coverage inventory and exact-master visual evidence, plus unresolved limitations to [$weekly-claw-youtube-publisher](../weekly-claw-youtube-publisher/SKILL.md), which routes to the [thumbnail skill](../thumbnail-skill/SKILL.md). Missing required presentation coverage remains incomplete and cannot be cleared by technical QA or upload authority. Review uploads remain Unlisted until the current request explicitly authorizes Public publication for the exact release. For vertical clips and their ending, use [editorial-direction.md](references/editorial-direction.md); accompanying posts route to the installed `write-podcast-clip-posts` skill.

For scheduled runs, do not return a terminal report while any required ingest row is `GENERATING`, `READY_TO_DOWNLOAD`, or `DOWNLOADING`. Continue the reversible wait/retry loop while progress is observable. If an external execution ceiling interrupts the run, leave exact per-file state and the next browser action in `ingest-state.json` and report the run as interrupted/incomplete, never as a completed or user-blocked edit.

## Maintaining the shared skill

Compare installed and canonical versions before changes; preserve newer rules and prior versions.
