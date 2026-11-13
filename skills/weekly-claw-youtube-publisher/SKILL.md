---
name: weekly-claw-youtube-publisher
description: "Finish and distribute a Weekly Claw episode end to end from a supplied video or project: verify the editorial master, create and approve the thumbnail, upload and review YouTube Unlisted, prepare and publish the exact full episode on X and Bilibili when each account is ready, update weeklyclaw.ai, and reconcile every approved surface. Use for Weekly Claw episode finishing, YouTube/X/Bilibili packaging, uploads, posts, re-uploads, corrections, publication, distribution, or release QA."
---

# Weekly Claw Multiplatform Publisher

## Full-episode handoff — 2026-10-04.1

For full-episode work read [references/full-episode-handoff.md](references/full-episode-handoff.md) before inventory or upload. A Short or proof montage cannot fulfil a full-episode review request. Read the [editor's current direction](../weekly-claw-episode-editor/references/editorial-direction.md) when reconciling its QA and disclosed omissions. This handoff does not authorize publication or replace missing operating references.

Before selecting a full-episode upload file, require the editor's reconciled presentation-coverage inventory and actual visual evidence bound to that exact master SHA-256, under its [final-master QA contract](../weekly-claw-episode-editor/references/qa-contract.md). Every relevant slide/chart and meaningful screen/demo interval in retained discussion must be accounted for; inspect representative actual-master evidence across the presentation and every flagged gap. Missing rows, unsupported omissions or stills substituted for required motion hold upload even when decode, audio, thumbnails and platform checks pass. An editor's written omission reason or an Unlisted upload request does not waive required coverage. Reuse an explicit user-accepted scoped exception when one exists; keep its limitation visible and continue independent preparation while a genuine gap is resolved.

## Community ownership override — 2026-09-05

WhatsApp delivery requires a visually verified correct episode thumbnail: use a native link preview or the approved thumbnail as a photo with title/link caption. Text-only delivery is not complete. Apply the mandatory WhatsApp gate in the community reference below before sending.

Community distribution is a post-publication phase of this release workflow. Read [references/community-distribution.md](references/community-distribution.md) and preserve the existing authorized owner, account-bound approval gates and delivery receipts.

Turn a supplied episode into one verified release. Do not equate “rendered,” “uploaded,” and “published”; each is a separate gated state.

## Inputs and evidence

Require a video or project path. Accept optional episode number, guest names, transcript, known defect intervals, context URLs, and requested visibility.

Create or update `work/publishing/<episode>/release-manifest.md` from [references/release-manifest.md](references/release-manifest.md). Record facts and proof there throughout the run. Never trust a filename such as `final` without inspection.

Track `thumbnail_headline` (short artwork text) and `episode_title` (full canonical listing title) separately in the title rationale or release record. A user revision or approval of thumbnail wording changes `thumbnail_headline` only; preserve `episode_title` unless the user explicitly changes the listing title. Continue under the existing task authority; this distinction adds no approval step. An explicit exact episode-title instruction overrides the usual topic and numbering format.

Read:

- [references/editorial-qa.md](references/editorial-qa.md) before modifying media.
- [references/weeklyclaw-brand.md](references/weeklyclaw-brand.md) before thumbnail or outro work.
- [references/publishing-checklist.md](references/publishing-checklist.md) before operating YouTube Studio.
- [references/distribution-checklist.md](references/distribution-checklist.md) before operating X or Bilibili.
- `work/publishing/platform-rollout.md` before staging any non-YouTube destination.
- The saved `thumbnail-skill` and its required references before thumbnail work. Its workflow is a required stage, not optional guidance.

## Safety contract

- Keep source media immutable. Write versioned outputs.
- Never overwrite or delete an existing YouTube upload.
- Upload a new copy as **Unlisted** first.
- Never choose Public, Schedule, Premiere, or private sharing without explicit authorization in the current request.
- Treat “publish” as approval only when the exact episode, video ID, approved thumbnail, canonical title, and complete multi-surface release scope are unambiguous.
- If material media, metadata, thumbnail, captions, or checks change after approval, return to Unlisted review.
- Default to exact photographs for real people. Never generate or alter a person’s likeness without explicit authorization.
- Keep superseded copies Unlisted unless deletion is explicitly requested.
- Keep thumbnail approval distinct from complete-release approval. Neither implies the other.
- A direct, explicit acceptance of a known editorial defect in an exact thumbnail is `REVIEWED_WITH_USER_ACCEPTED_EXCEPTION`, not an independent QA PASS. Record the failed criterion, candidate hash and acceptance text/scope; all non-waived criteria still require evidence. This scoped acceptance satisfies the editorial thumbnail gate for that candidate wherever this skill or its references otherwise say “QA-passed”. It does not waive channel/account identity, factual integrity or release-surface authorization, and does not apply to future candidates. Reuse valid recorded approval; do not request it again merely because a session resumed.
- Treat X posts and Bilibili final submissions as public publication. Never trigger either from thumbnail approval or YouTube-upload approval alone.
- Verify the exact destination actor before every upload, draft, or post. Never publish from a substitute account.
- **YouTube channel identity gate (mandatory):** record the intended channel's exact display name, handle, and immutable channel ID in the release manifest before opening the upload flow. Read back the active Studio channel header/account switcher and verify all three fields before selecting the local file or triggering an upload; a signed-in Google account name, avatar, or remembered channel is not proof. For Weekly Claw the default tuple is `Weeklyclaw` / `@WeeklyClaw` / `UCa0Mxn9vyx6NnU-aBgRcRvg` unless the manifest explicitly records an approved replacement. If the active channel differs or the target is unavailable, stop with `YOUTUBE_CHANNEL_IDENTITY_BLOCKED` before any upload. After upload, verify the same tuple in Studio and on the watch page; a mismatch is `WRONG_YOUTUBE_CHANNEL`, not a successful release.
- A non-default YouTube channel tuple requires an explicit approval record containing approval text, time, and scope bound to that tuple; never accept an alternative because it is available in the account switcher.
- Before every destination write, check the release manifest, published inventory, and draft/media library for the same episode and master hash. Resume matching drafts; never create a duplicate silently.
- Prefer the exact verified full master on X and Bilibili. If current entitlement or conformance blocks it, stop with the precise blocker; never silently substitute a clip, transcode, dub, or localized edit.
- Do not begin the public release when any approved release surface cannot be updated and verified. Preflight access and rollback first.
- **Bilibili title gate (mandatory):** the approved manifest title—not the media filename—is the sole title authority. For every new upload or resumed draft, explicitly write that exact title into the editable Bilibili title field. A value visible before Save or Submit is not proof: save, reopen the remote draft/editor, and read back the exact title before submission. If it reverts to the filename, record `TITLE_PERSISTENCE_FAILED`, preserve the one existing draft/BV, and stop—do not submit, re-submit, or advance another episode through that UI path. Independently open the public BV page to confirm the rendered title. A completed transfer, Creator Center card, auto-filled filename, or saved draft never satisfies this gate.
- **Bilibili cover gate (mandatory):** use the exact independently QA-passed, user-approved Weekly Claw thumbnail as the Bilibili cover for every episode. Treat the approved thumbnail binding in the release manifest (path and SHA-256) as authorization to attach that cover; do not ask again per episode. Read back or visually verify the rendered cover before submission. If the current browser surface cannot supply the local file, preserve the draft and report that specific file-picker capability gate—never substitute a generated, auto-selected, or filename-derived cover.
- **Handoff:** Route account-bound work to the authorized owner and verified local browser session; use one idempotent handoff and record its result.
- **Transport:** Use the existing authorized local handoff and receipt mechanism; do not duplicate queued or completed work.

## Stage 1: Inventory and identify the candidate

1. Resolve the exact requested path.
2. Inventory sibling masters, edit plans, transcripts, captions, raw participant tracks, thumbnails, source assets, and prior upload IDs.
3. Probe every plausible master for size, duration, codecs, dimensions, frame rate, channels, sample rate, and average video bitrate; apply the master encode standard below.
4. Match episode number, participants, runtime, edit state, outro, and audio state. Record why one file is the candidate and why the others are superseded.
5. Enumerate every usable participant track. Require visible coverage for each participant in at least one focused scene and one all-present scene.

Stop if the episode identity, candidate master, or required participant coverage is ambiguous.

## Master encode standard

The August 26 production review established a Weekly Claw release gate of at least **4,000 kbps average video bitrate for 1080p YouTube masters**. Restore this check at the final encode and upload boundary; it is a house delivery standard, not proof of visual quality or a guarantee about YouTube's transcode bitrate.

- Preserve compliant block video with `-c copy` when concat parameters match. Avoid accidentally replacing roughly 6 Mbps blocks with a fixed 2–3 Mbps final encode.
- When re-encoding is required, start from the best verified original blocks/intermediate. The existing recipe is `libx264 -preset slow -crf 17 -maxrate 10M -bufsize 16M -pix_fmt yuv420p`, H.264 High profile and AAC-LC at 256 kbps or higher. CRF does not guarantee a bitrate floor; measure the output. If it misses the house gate, the existing target-bitrate alternative is `-b:v 8M -maxrate 10M -bufsize 16M`, followed by another measurement.
- Record the exact final path/SHA-256, encode command, average video bitrate and visual QA in the release manifest. Use the video stream bitrate, not total container bitrate; if unavailable, measure video packet bytes over duration rather than treating unknown as a pass.
- A sub-4 Mbps 1080p candidate requires a new verified render from the best source before upload. Inflating a previously degraded master cannot restore detail. Review source cards, faces, motion and joins in the actual candidate as well as its bitrate.

## Stage 2: Inspect, transcribe, and fact-check

1. Inspect the complete timeline through playback, contact sheets, waveform, and transcript; closely review the opening, speaker transitions, every known defect interval, source-reference passages, guest segments, and ending.
2. Reuse a transcript only when it matches the candidate. Otherwise transcribe the candidate locally.
3. Search the project and `weeklyclaw.ai` for matching show notes, prior metadata, speaker references, sponsor context, and episode pages. Use them to enrich—not override—the candidate and transcript.
4. Extract claims and references: people, roles, companies, products, models, benchmarks, prices, dates, tweets, articles, charts, events, and quoted language.
5. Verify material claims against original or authoritative sources. Preserve qualifiers such as reported, announced, sampled, alleged, open-weight, or scheduled.
6. Build a timestamped edit sheet with verdicts: correct, correction required, qualification required, source visual, or unresolved.
7. Prefer the original tweet, article, chart, filing, launch page, or video. Resolve X reply chains to original status IDs. Keep source account, date, headline, and material passage legible.
8. Put every on-screen source and correction into a `SOURCES & CORRECTIONS` description block.

Do not reinforce an unresolved claim with decorative B-roll or a synthetic quote card.

## Stage 3: Build the editorial master

1. Add readable source visuals wherever the discussion references material that can be shown.
2. Cover every occurrence of an incorrect spoken claim. Use a correction card, cut, or pickup; a single card is insufficient when the error repeats later.
3. For article treatment, show the title/byline first and scroll only when the evidence develops down the page. For threads, show posts chronologically.
4. For unwanted background speech, encode the user’s exact interval and retained speaker identity before processing. Use speaker-targeted separation; generic denoise or voice isolation cannot distinguish two people.
5. Crossfade bounded audio repairs and verify the retained speaker with transcription, loudness, waveform comparison, and listening samples.
6. Preserve the authorized recurring original ending image and music. Verify its actual canonical website/social links, visual duration, music overlap and global transparent programme mark in the exact rendered master; do not silently regenerate the ending or substitute an unverified domain.
7. Preserve constant delivery timing, color metadata, audio format, and intended runtime.

Run the applicable checks in [references/editorial-qa.md](references/editorial-qa.md). The exact file that passes becomes the release candidate.

## Stage 4: Create and approve the thumbnail

Invoke the saved `thumbnail-skill`; complete every step and its required QA record. This publisher safety contract controls wherever the thumbnail skill is more permissive, including its explicitly scoped user-accepted-exception rule.

1. Ground the brief in the exact release candidate, transcript/topic, complete participant list, verified current-episode participant frames, existing brand assets, and most recently approved Weekly Claw thumbnail. Follow the thumbnail skill's approved identity lock: user-designated authoritative cards govern Andy/Henry facial anatomy; hashed real cross-episode photographs support it; current-episode footage establishes participants, clothing and removable equipment. These approved references are not an unapproved fallback. For guests without an approved identity pack, use verified current-episode frames. Record each source and approval scope; do not promote generated candidates to likeness evidence or describe the approved cards as raw photographs when their provenance does not establish that.
2. Follow [thumbnail title development](../thumbnail-skill/references/title-development.md): develop distinct, evidence-backed listing-title and thumbnail-hook pairs; compare their viewer appeal and fidelity, and record the chosen pair and rationale.
3. Define one visual idea and an episode-specific palette. Use the official claw-before-`WEEKLY` mark, add the standalone claw icon in the bottom-left safe margin for every new round, and use a contained episode badge. Keep approved files immutable. For recurring two-host episodes, require both current-episode hosts side by side at comparable visual weight in one continuous simple scene; do not substitute separate webcam cards, a split portrait wall, or participants flanking a central copy card.
4. Generate three distinct 16:9 candidates for the initial concept and every revision round. Keep participants and brand anchors fixed; test distinct well-grounded hooks where appropriate while varying meaningful composition choices such as crop, spacing, hierarchy, and title placement; trivial colour swaps do not count. Use GPT Image 2 as the final shared-scene generation pass for all three base images, grounded in the approved identity-card and real-camera reference hierarchy, current-episode context and explicit real-person authorization. Generate without text/logo/badge, then apply exact typography and branding deterministically. Do not stop at webcam crops, feathered source composites, or generated backgrounds behind separate cards. Faces must remain natural, flattering, large, recognisable, and free of distracting eyeglass reflections.
5. Keep the current-episode faces dominant, place `thumbnail_headline` over the lower third or clean negative space, and use a quiet tonal or restrained studio-gradient background. Follow the simple All-In podcast grammar: no prop or one simple supporting object; reject a separate half-canvas text panel, elaborate literal environments, dense machinery, and busy scene-building.
6. Run mandatory independent QA before showing previews. A reviewer other than the maker must compare all three candidates with the approved identity cards and verified real-camera references, episode footage, participant list, and most recently approved thumbnail (for style only); inspect each at 1280×720 and 160×90; and explicitly pass or reject the All-In composition, source grounding, participant count/coverage, each likeness, side-by-side scale and spacing, clean eyeglass lenses, each candidate’s exact recorded `thumbnail_headline` wording, claw/logo order, accent colour, badge containment, meaningful A/B/C variation, and mobile readability.
7. Regenerate rejected candidates unless the exact known defect has the scoped user acceptance recorded above. Record the reviewer, all candidate paths and SHA-256 values, comparison sources, dimensions, and itemised pass/fail result in the release manifest.
8. Show only three QA-passed previews labelled A/B/C and stop. Do not upload, alter YouTube, update the website, change video metadata, or publish any asset until the user explicitly selects and approves one exact thumbnail candidate.
9. Bind approval text and time to the exact thumbnail path and SHA-256. Any thumbnail change invalidates approval and repeats independent QA and user approval.

## Stage 5: Create the YouTube package

1. Draft title, description, chapters, tags, captions, thumbnail, and playlist from the release candidate—not an earlier transcript or cut.
2. `episode_title`: use the selected, episode-grounded title from Stage 4 and pair it with a complementary `thumbnail_headline`. Use a topic stack only when it improves the title, rather than as a mandatory formula. Keep the title under 100 characters and retain established Weekly Claw episode numbering where appropriate. Honour an explicit exact user-supplied episode title.
3. Description: concise hook, accurate guest/host context, chapters, `SOURCES & CORRECTIONS`, canonical links, verified sponsors, and 3–6 focused hashtags.
4. Chapters: start at `0:00`; verify transitions against the final rendered timeline.
5. Playlist: use `Weekly Claw — Full Episodes` when available. Create nothing new without authorization.
6. Captions: generate or retime from the release candidate and verify names and corrections.
7. Use only the exact independently QA-passed and user-approved thumbnail from Stage 4.

Record candidate title/hook pairs, episode evidence, selection rationale, separate final `thumbnail_headline` and `episode_title` values, and title character count in `work/publishing/<episode>/title-rationale.md` or the release manifest. Record any external comparisons actually used without inferring performance.

Record the proposed package. Show it before any Public change; show it before upload as well when the user requested pre-upload review.

## Stage 6: Upload Unlisted

1. Read and invoke the in-app Browser control skill before operating YouTube Studio.
2. Resolve the target channel identity tuple from the release manifest before selecting a file: exact display name, exact handle, and immutable channel ID. For Weekly Claw the expected tuple is `Weeklyclaw` / `@WeeklyClaw` / `UCa0Mxn9vyx6NnU-aBgRcRvg` unless the current manifest explicitly records an approved replacement.
3. Open Studio in the authenticated browser and verify the active channel header/account switcher shows that exact tuple. Read it back from the visible UI or the channel page; a Google account name, avatar, or remembered prior session is not sufficient. If the active channel differs, switch to the target and verify again. If the target is unavailable, stop before file selection and record `YOUTUBE_CHANNEL_IDENTITY_BLOCKED`.
4. Only after the identity gate passes, create a new upload from the exact release candidate.
5. Set **Unlisted** before completing the flow.
6. Apply every applicable item in [references/publishing-checklist.md](references/publishing-checklist.md).
7. Upload the exact approved thumbnail and matching captions. Verify the custom thumbnail rendered on the listing; a local asset alone is not proof.
8. Wait for upload, checks, and HD processing as practical.
9. Record the YouTube video ID, review URL, exact local source path, runtime, thumbnail path, metadata revision, visibility, and the verified target channel tuple in the release manifest.

If a video is discovered on the wrong channel after upload, do not claim the release, do not silently delete or change visibility, and do not assume a single-video transfer exists. Preserve the video ID and evidence, mark `WRONG_YOUTUBE_CHANNEL`, and stop for an explicit recovery decision. YouTube's normal recovery is a fresh upload to the verified target channel; channel-transfer tooling moves an entire Brand Account/channel and can replace or delete the destination channel, so it is not a substitute for moving one episode.

Before any upload or public transition, run the channel-gate preflight verifier at `scripts/verify_youtube_channel_gate.py` (or an equivalent machine-check) against the manifest and the exact visible channel readback. The verifier must fail closed for a missing tuple, a pre-upload mismatch (`YOUTUBE_CHANNEL_IDENTITY_BLOCKED`), a post-upload mismatch (`WRONG_YOUTUBE_CHANNEL`), or a contradictory `PUBLIC_VERIFIED` status.

## Stage 7: Review the actual Unlisted listing

Open Studio and the watch page. Verify:

- exact target channel display name, handle, and channel ID on both Studio and the watch page; if any differs, mark `WRONG_YOUTUBE_CHANNEL`, stop promotion, and do not claim the upload as a Weekly Claw release
- exact source filename and expected runtime
- saved `episode_title` matches its full recorded value character-for-character after saving and reopening Studio and on the watch page; verify `thumbnail_headline` separately on the rendered thumbnail before any publication
- full description, chapter navigation, thumbnail, captions, playlist, and audience
- paid-promotion and altered-content answers
- copyright and Community Guidelines checks
- Unlisted badge and watch-page playback
- opening, correction/source-visual passages, repaired audio interval, guest coverage, and outro

Show the final YouTube preview. Record the exact canonical title and approved thumbnail SHA-256. Stop at Unlisted unless the user explicitly authorizes the complete multi-surface release for this exact video ID, title, and thumbnail.

## Stage 8: Stage X and Bilibili distribution

Read [references/distribution-checklist.md](references/distribution-checklist.md) and the rollout matrix. A destination may be staged only when its exact actor and required entitlement are verified. Keep all staged assets unpublished.

1. Build one destination ledger from the exact master path/SHA-256, approved thumbnail path/SHA-256, captions, canonical title, source manifest, and QA report.
2. For X, keep the canonical editorial master unchanged and create a versioned platform wrapper that holds the exact approved episode thumbnail visibly for approximately five seconds before frame zero of the complete master. Add no intro music unless separately approved. Record the wrapper path/SHA-256 and source master/thumbnail hashes. Media QA must prove the opening card is present, correctly timed, uncropped, and legible at desktop and mobile sizes, then prove the complete programme follows without unintended content or A/V changes. Recheck current official duration, file-size, codec, resolution, and entitlement limits against the wrapper. Verify the authenticated account is exactly `@weeklyclaw`; if it is not, stop before media upload or post creation. Draft concise episode-specific copy and record its revision. Normal compose is immediately public, so do not attach media or press Post before complete-release approval. If Media Studio is available, an unpublished media upload may be staged after duplicate and entitlement checks; record its media ID. Use the wrapper hash for X duplicate/idempotency checks.
3. For Bilibili, verify Creator Center is authenticated as `Weeklyclaw` and read back the approved account ID recorded in the release manifest unless the manifest explicitly names a newly approved replacement. Search both published submissions and drafts for the episode/title/master. Resume a matching draft before considering a new upload.
4. Resolve Bilibili's title from the same manifest-approved canonical title contract used for YouTube; when an approved Chinese-first bilingual variant exists, that exact variant is the Bilibili submitted title. The media filename is never title authority. After the upload starts, explicitly replace the Bilibili title field with the approved submitted title even when the form appears to auto-fill it, then read back the field value and character count before submission. If the current UI limit requires condensation, preserve the canonical claim, record the approved variant in the release manifest, and do not improvise from the filename or secondary topics. Upload the exact full master and approved thumbnail to an unpublished Bilibili draft when the live form accepts them. Apply the complete description, chapters, tags, category, creation declaration, captions when supported, and all sponsorship/commercial disclosures. Do not invent a Chinese dub or silently remove material.
   The approved Weekly Claw thumbnail is the required Bilibili cover automatically; attach and verify it without requesting a separate per-episode cover decision.
5. Stop at any Bilibili login, QR, bound-phone, real-name, CAPTCHA, or SMS gate. Never guess a code or claim verification. For the bound-phone SMS flow, report the displayed action and wait for the account holder; do not select `I sent it` until the user confirms the real phone action is complete.
6. Record X copy/media identity and Bilibili draft/submission identity in the same release manifest. A local package or completed file transfer is not a published destination.

## Stage 9: Publish and reconcile every surface

1. Preflight the complete release before changing public state: exact YouTube video ID, exact target YouTube channel tuple (display name, handle, channel ID), canonical title, approved thumbnail path/SHA-256, X copy and media ID/path/hash, Bilibili actor/title/draft ID, every approved website target, permissions, platform checks, and a safe rollback for each mutable surface.
2. Stop if any approved destination is absent, ambiguous, logged out, attached to the wrong actor, blocked by entitlement/verification, stale, duplicated, or unverifiable. Do not make YouTube Public while another destination included in the requested release is still blocked.
3. Show the final release manifest and require explicit complete-release approval for the exact YouTube ID, canonical title, approved thumbnail SHA-256, X post copy/media, Bilibili submitted title/draft ID, and complete surface list.
4. Publish the approved thumbnail asset and canonical title/link to the website homepage, archive, and episode page; verify staged outputs before public promotion.
5. Change the exact YouTube upload from Unlisted to Public. Do not Schedule or Premiere. Save and reopen Studio.
6. Post the approved copy and full video from exactly `@weeklyclaw`. Verify the public X URL, actor, text, media duration, thumbnail/frame, and playback. Do not create replies or a thread unless they were included in the approval.
7. Submit the approved Bilibili draft from exactly the verified Weeklyclaw UID. Complete only user-performed verification gates, then open the public BV as a viewer and independently compare its rendered title with the manifest-approved Bilibili submitted title before advancing to another episode. Also verify the BV/AV ID, public URL, actor, thumbnail, duration, disclosures, and playback. A correct filename, draft field, or Creator Center card is not public-title proof.
8. Verify the YouTube target channel grid/watch page and canonical website homepage/archive/episode page. Compare channel identity, titles, and rendered thumbnails against the approved release package.
9. Inventory same-episode uploads/posts on every destination. Confirm superseded copies remain unchanged and no duplicate was created.
10. Record each URL/ID, observed title or copy, media proof, visibility, verifier, and verification time. Advance to `PUBLIC_VERIFIED` only when every surface included in the approved release passes.
11. If a surface fails after public changes begin, stop promotion, mark `PARTIAL_RELEASE_BLOCKED`, preserve evidence, and execute only pre-approved safe rollback actions. Never call a partial release complete.

## Cleanup after upload acceptance

Apply the editor skill's [cleanup and accepted-upload retention policy](../weekly-claw-episode-editor/SKILL.md#cleanup-and-accepted-upload-retention) only within applicable deletion authorization. Raw cleanup additionally requires the exact corrected upload to finish processing, verification of account, visibility, picture, audio and ending, and passing YouTube checks. Keep the master, thumbnail, captions, metadata, edit recipe, release/QA evidence and dependencies for unfinished authorized destinations. Record acceptance evidence and deleted paths; never extend local cleanup to remote recordings or YouTube objects.

## Final report

Report:

- final master path and technical summary
- tests and review evidence
- title, chapter count, thumbnail path, captions, playlist, and key settings
- thumbnail grounding, independent QA, exact approval, and SHA-256
- review/public URL and exact visibility
- YouTube custom thumbnail, public channel-grid, and public watch-page proof
- canonical website homepage, archive, and episode-page proof
- X account, post URL, exact copy, media duration, and playback proof
- Bilibili UID, BV/AV ID, public URL, submitted title, disclosures, duration, and playback proof
- exact title-consistency result across every surface
- completed release-manifest status and remaining failed rows
- copyright, Community Guidelines, and processing status
- superseded upload IDs and their unchanged visibility
- unresolved editorial or platform issues

Never claim “final” from intent, a local thumbnail, a Studio save, or one public page. Claim it only from a completed `PUBLIC_VERIFIED` release manifest with every surface included in the approved release verified.

## Maintaining the shared skill

Compare installed and canonical versions before changes; preserve newer rules and prior versions.
