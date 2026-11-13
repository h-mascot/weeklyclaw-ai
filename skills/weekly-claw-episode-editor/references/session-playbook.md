# Session-derived editing playbook — 2026-10-04.1

## Contents

1. Ingest paths
2. Editorial rescue
3. Multicamera language
4. Audio correction
5. Source visuals and corrections
6. Outro and delivery
7. Failure patterns

## 1. Ingest paths

### Riverside

Download independent aligned CFR video for every participant, every split or reconnect, all screen shares, and raw WAV audio. Riverside may split one participant across several track entries. An absent WAV does not make an aligned MP4 unusable; inspect embedded audio.

Riverside export generation and browser transfer are separate phases. For every required source:

1. Record the exact take, participant, track ID, format, duration, and resolution in `work/<episode>/ingest-state.json` as `DISCOVERED`.
2. Request the export and mark it `GENERATING`.
3. Poll the exact recording page every 30–60 seconds. When generation completes, mark it `READY_TO_DOWNLOAD`, invoke the download action again when required, and mark it `DOWNLOADING`.
4. Observe the local file every 10–30 seconds until no temporary download extension remains and its size is stable across two checks.
5. Probe it with `ffprobe`, compare duration and streams with the Riverside inventory, compute SHA-256, move it into immutable episode source storage, and mark it `VERIFIED`.
6. Reconcile `verified_required_files == required_files` and explicitly verify every expected participant before transcription or editing.

Queue generation for independent files when useful, but collect and verify every result. A toast saying the file is being generated, a `Ready` track badge, a completed generation request, or an active `.crdownload` proves neither local presence nor completeness.

While generation or transfer advances, keep waiting. After 15 minutes with no observable progress, refresh and retry the exact failed step. Only a fresh page plus three documented failed recovery attempts can convert a source to a blocker. Authentication, an actually missing/failed track, or a repeatedly non-progressing export may block; normal generation latency may not.

Create a manifest before editing:

| participant | kind | track ID | timeline start | duration | media spec | path |
|---|---|---|---:|---:|---|---|

Use aligned CFR files for shared timeline video. Map raw WAVs to their recording offsets before active-speaker analysis or mixing.

### OBS or desktop capture

Identify regions for screen, cameras, stage, navigation, audience, and chat. Preserve the original composite. Build deliberate 16:9 crops instead of publishing a nonstandard desktop canvas.

Use:

- presentation plus participant rail for slides or demos
- full-screen desktop/browser when the source itself is the subject
- full-frame participant group composition for discussion

Exclude navigation, audience, and chat unless editorially relevant.

### Optional Discord capture

Check `work/<episode>/` for locally saved Discord or desktop recordings. Their absence is normal and must not stop ingest, planning, or rendering.

When a relevant capture exists:

- map each usable excerpt to the exact discussion interval
- show only when it clarifies or substantiates what the speakers are discussing
- crop tightly to the relevant message or thread; never publish raw scrolling
- keep the excerpt readable, normally for 5–10 seconds
- hide unrelated or private usernames, avatars, server/channel names, notifications, DMs, and messages
- recreate a clean excerpt card when safe cropping cannot remove private material
- return to speakers after the evidence has served its purpose

Do not infer that all visible Discord content is cleared for publication.

## 2. Editorial rescue

Transcribe first. A bad live experience can still contain a strong episode.

Mark:

- failed setup and pre-show
- first clean introduction
- repeated starts
- audio/device troubleshooting
- guest arrivals and departures
- accidental stage endings
- coherent recovery sections
- natural closing
- post-show production talk

Write keep/remove source intervals with reasons and one versioned piecewise source-to-programme map, including insertions and frame semantics. Derive cameras, raw audio, captions, context images, footers, chapters and ending from that map. For an archival quotation, retrieve the real earlier excerpt and place it at the verified conversational cue with only the requested archival treatment.

Begin at the first clean formal welcome after setup, webcam discussion, delays and repeated starts. Preserve actual words; use a cold open only when the current editorial brief calls for one.

## 3. Multicamera language

Follow [editorial-direction.md](editorial-direction.md): group-first for conversation, opening, handoffs and reactions. Take a full-width solo only for a sustained contribution by the verified actual speaker. Audit every solo against speech/context and isolated microphones. Energy and elapsed duration can locate candidates, but neither authorizes a cut; do not impose a solo quota.

Use a full-frame horizontal arrangement of portrait participant panels, or readable main evidence with a rail of the participants actually present. Do not retain an absent guest as a frozen/borrowed frame. Source visuals enter after their spoken introduction and remain only while relevant and readable; a fixed screen timer is not editorial authority.

Normalize participant framing before rendering group layouts:

- Use per-camera crop, scale, and vertical offset; never assume one transform
  suits every camera.
- At 1920×1080, aim to place participant eye lines within roughly 30–50 px
  vertically in a two-up or grid, unless an intentional composition justifies
  an exception.
- Keep face heights visually comparable, normally within about 15%, with
  consistent headroom and no clipped crowns or chins.
- Base alignment on neutral sampled frames, then check movement, laughter, and
  posture changes so the crop remains safe throughout the block.
- Store the transforms in the layout plan or render configuration so the
  framing is reproducible and cache invalidation can detect changes.

Store the plan and shared time map in machine-readable form. Review the storyboard, then actual native moving proof of every layout/source graphic, transform and relevant motion extreme before full render. Cache by exact source range, map revision, layout, renderer and assets; changed inputs invalidate the block.

## 4. Audio correction

### General mix

Prefer isolated participant audio and verify offsets. Diagnose mic handling, room reflections and duplicate-track bleed separately; do not assume every reported echo has one cause. Compare level-matched original, repair and final-mix samples. Measure final encoded loudness/true peak and record actual listening separately.

Improve quiet guest audibility and caption every intelligible contribution, including brief meaningful reactions. Keep uncertain words unresolved; retain substantive answers. Remove an empty invitation/decline exchange only after actual audition establishes a natural join and intact meaning. If unavailable or forced, retain it. A transcript or silence boundary is insufficient.

### Named unwanted voice

Required order:

1. Record exact user-stated interval.
2. Identify the one speaker to retain.
3. Add failing regression for full interval and identity.
4. Create speaker-targeted retained track.
5. Optionally apply high-quality voice isolation for room noise.
6. Loudness-match neighboring dialogue.
7. Insert with 50 ms crossfades.
8. Export A/B clips.
9. Transcribe retained dialogue.
10. Listen and inspect waveform/spectrogram.

Do not trust generic “baby voice removed” prompts or a JSON `dialogue_retained` field. Separation artifacts may contain the main host rather than the unwanted person.

## 5. Source visuals and corrections

Resolve quoted posts back to original status IDs. Use primary articles, product pages, charts, event pages, and demos. Keep account, date, title, byline, and relevant claim readable.

Use readable evidence treatment:

- source first
- full-screen evidence or a large source with the actual participants at the side
- tight readable crop
- speaker/group inset only when useful and supported by the current camera direction
- no synthetic quotation cards

Fact-check proper nouns, company roles, attribution, dates, statistics, and scope. Preserve qualifiers such as “announced,” “alleged,” “gateway sample,” or “founder claim.” Add concise correction cards for substantive spoken errors.

Tone: make source notes helpful, not combative. Prefer “Sanders’ AI pause proposal” and its verified link to a blunt “no ban” label. Where the spoken claim needs a factual distinction, state that distinction neutrally; a source link must not conceal a material correction. Never retrofit a newly expressed style preference into an approved video without authorization.

Follow the authentic-evidence/designed-explanation/GPT-artwork distinction in [editorial-direction.md](editorial-direction.md). Use original benchmark charts with axes, legends, units, dates and qualifiers intact; actual launch motion when requested; and real icons/canonical fonts for designed comparisons. Merge related cards when a readable table serves them. Do not treat a still, related chart or profile/CTA fallback as fulfillment of a requested clip, exact chart or historical scroll. Check complete transformed diagrams, source edges and host-rail fit throughout native motion at delivery/mobile sizes.

## 6. Outro and delivery

Preserve the established original ending picture and sound with hashes and provenance. For an authorized new/update capture, verify the canonical `weeklyclaw.ai` destination and actual branding rather than reconstructing it or accepting an unchecked typed domain. Preserve identity and labels. Clip-specific vertical endings and verified social icons/links are covered in [editorial-direction.md](editorial-direction.md).

The full-episode default is a 10-second end card with the established music beginning 3 seconds before the picture transition. Preserve a specifically approved original timing. Match the requested deliverable's canvas/frame rate, yuv420p, BT.709 and 48 kHz audio; verify picture and sound in the exact final file and remove internal review stamps.

Write a report with immutable input paths, output path, EDL, repair intervals, retained speakers, source visuals, correction cards, outro assets, and verification evidence.

## 7. Failure patterns

- Composite-only edit omitted a valid participant track.
- Slides-only treatment removed speakers and reactions.
- Generated portrait changed a real person’s identity.
- Cross-episode portrait substitution mislabeled hosts.
- Forced width/height distorted portrait aspect ratio.
- One shared group crop left participant eye lines, face scale, or headroom
  visibly mismatched.
- Generic voice isolation retained every human voice.
- Cleanup covered the wrong timestamp or wrong episode.
- Self-authored cleanup report passed without perceptual proof.
- Later render dropped an outro present in an earlier pipeline.
- Source-visual render changed frame count by one tail frame.
- Reused render blocks survived changed source inputs.
- Raw Discord footage exposed unrelated or private chat.
- Public upload occurred before fact-check and final-master selection.
- Scheduled run stopped after requesting Riverside generation but before collecting the generated files.
- A growing temporary browser download was mistaken for a terminal source blocker.

Prevent each failure with exact source paths, machine-readable plans, targeted tests, visual/perceptual review, immutable versions, and Unlisted review.
