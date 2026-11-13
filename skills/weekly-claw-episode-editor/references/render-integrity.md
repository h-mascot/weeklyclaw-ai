# Render integrity — 2026-10-04.1

Read this when aligning independent tracks, revising an EDL, repairing a render,
or validating the final master. Historical paths, account blockers, and episode-specific approvals
are evidence to recheck, not defaults for a new episode.

## Source alignment and editorial recovery

- Derive the expected participant roster from recording/session evidence, not
  only the files already downloaded. Account for delayed arrivals, departures
  and reconnects; do not show empty tiles outside actual participant presence.
- Wait for browser transfers or cloud-file hydration to finish before declaring
  a source corrupt. A growing MP4 can temporarily lack its `moov` atom; require
  stable, fully local bytes and a fresh probe before classifying that failure.
- Probe audio and video separately, including stream start/end and decoded
  samples at the requested interval. An audio stream listed by `ffprobe` may
  end long before its screen-share video. Zero decoded samples are missing
  coverage, not proof that a demo has a silent soundtrack.
- Map raw WAV time to the aligned CFR timeline explicitly. If raw audio begins
  `d` seconds into that timeline, aligned time `t` maps to raw time `t - d`.
  Verify the sign and offset against embedded camera audio near the beginning,
  middle, and end; do not assume matching filenames or durations establish sync.
- Mark each screen interval as static evidence, moving demo, or private/setup
  footage. Inspect the original motion before deleting a passage labelled
  “failed playback” by the transcript: the local recording can contain a good
  demo even when a participant reports it hanging. Recover the useful picture
  independently of unwanted troubleshooting dialogue, with an explicit audio
  choice and source-time mapping.
- Seek moving demos from their mapped source start. A first-frame trim plus
  clone/pad destroys motion. Use original public demo media where suitable and
  verified; preserve attribution and do not imply its audio came from a track
  with no coverage.
- Maintain one versioned piecewise source-to-programme map with source/take,
  source and programme intervals, frame semantics and input hashes. When the EDL
  changes, retime cameras, captions, chapters, source cards, footers, archive,
  audio and ending from it. Inspect cues straddling every cut: an excluded setup phrase
  can survive as a tiny boundary cue. Correct grounded spellings while keeping
  captions faithful to speech; uncertain words need audible review.
- Check subtitle timing against speech as well as file validity. Forcing cues
  into non-overlap can accumulate seconds of delay, while broad merging can
  create unreadable walls of text. Preserve timing and readable cue lengths;
  validate the muxed subtitle track and confirm subtitles cannot truncate the
  video at the last cue (for example through an unintended `-shortest`).

## Render cache and timing

- Reuse a block only when its current source hashes, source range, layout,
  renderer/configuration, overlays and brand assets match. An old receipt's
  input fingerprint is not a fresh comparison.
- Derive each camera tile crop from the actual face/eye position and gesture
  envelope, not geometric center by default. Reject a crop that clips a face,
  crown, chin, or meaningful movement even when its dimensions are valid.
- Require the cached file to exist, match its recorded output hash, and probe
  to the expected frame count, dimensions and frame rate. A missing file is a
  cache miss; recover from verified alternatives or rerender that block.
- Probe newly rendered blocks before writing success receipts. FFmpeg can exit
  successfully at early EOF while producing fewer frames than planned.
- Keep preview/limited-run indexes separate from the canonical full index and
  concat list. Promote a complete, validated set together, including the outro;
  do not leave a subset index beside an old full concat list.
- Test native frame-rate conversion through the actual overlay graph. The E28
  25-to-24 fps path lost one terminal frame; a motion-only
  `fps=24:eof_action=pass` fixed that path. Verify both exact frame count and
  changing pixels before using the same fix elsewhere. A freeze or fabricated
  success count is not a timing repair.
- Compare hashes of the same representation: whole MP4, video packets and
  Annex-B elementary video are different identities. For an audio-only change,
  extract both video streams using the same command and compare those hashes.

## Source cards and corrections

- Use native-resolution evidence or faithful, source-verified typesetting.
  Enlarging a small screenshot cannot recover its table cells. Inspect the
  smallest meaningful labels at final delivery and mobile sizes.
- Prefer independent local Riverside tracks over a compressed live-preview
  capture when both exist. Increasing output bitrate, scaling tiny OBS camera
  tiles or sharpening cannot restore absent source detail. Verify a short
  moving sample before committing an entire episode to enhancement.
- Use the established Weekly Claw correction design with literal text
  rendering. With FFmpeg drawtext, disable expansion for literal text or render
  verified typography to an image; percent signs must survive in encoded pixels.
- Reserve picture space above correction panels. A safe-margin rectangle can
  still cover a leaning host's mouth or chin; check actual moving frames.
  Keep one alpha-transparent stacked programme mark fixed to the global
  bottom-left across cameras, sources, archive and outro, with no plate or
  rail-relative movement. Prevent duplicate baked programme overlays without
  deleting authentic source logos or original ending artwork. Verify actual
  alpha and every composed state. Participant names and supplied handles remain
  tile-local; confirm guest identity and never guess a handle. Their baseline
  must not move the global mark. Preserve approved previous masters.
- Map the completed spoken-topic cue before each visual onset and inspect its
  final encoded position. Preserve authentic chart axes, legends, timeframe,
  units and qualifiers. Fit complete diagrams in the source region throughout
  native motion, including pan/zoom extrema, without covering the host rail.
- Remove only the correction Henry identified. Preserve other material
  qualifications, and cover repeated occurrences of a mistaken claim.
- A full fact-check requires a timestamped ledger of material claims across
  the complete retained transcript. A few representative topic checks are a
  partial review; label remaining coverage and unresolved claims explicitly.

## Final audio and honest QA

- Measure loudness and oversampled true peak on the final encoded AAC decoded
  from the exact candidate. Upstream PCM or sample-peak checks do not establish
  the encoded result: E28 required a new audio revision after AAC overshoot.
- For repairs, export level-matched original, cleaned isolated track and actual
  final-mix samples, with source and master timestamps. This separates noise
  treatment from a simple gain difference. Preserve earlier revisions.
- Audition proposed invitation/decline joins for naturalness and retained meaning.
  If that listening is unavailable or the join is forced, retain the exchange.
  Keep substantive guest speech; caption verified words and flag uncertainty.
- Transcription, waveform inspection, full decode and loudness measurements
  are technical evidence, not listening. Record the reviewer and audible
  checks for intelligibility, timbre, clicks, transitions, unwanted voices and
  sync. If audio input is unavailable, leave perceptual QA pending and provide
  short exact-master playback samples; an explicit user acceptance records
  precisely that acceptance, not an invented independent PASS.
- Read review findings even when the helper exits zero or prints a clean
  footer. Resolve or explicitly reject actionable findings with evidence.
  Recovery-code defects do not themselves prove an already verified master is
  corrupt; rerender affected media only when the evidence requires it.
- Pass the current candidate explicitly to QA and verify the manifest binding.
  An old default fixture/master or stale episode label is not the current
  release's result. Separate test-collection/tooling failures from media
  failures; when maintaining the pipeline, fix its supported test entry point
  instead of depending indefinitely on an undocumented local override.
- A bounded native patch and packet-preserving assembly still require exact
  final-master hash, full decode, packet/timestamp continuity and changed-boundary
  review. Compare source glitches against original media before blaming a render.
  Report sampled visual/privacy coverage separately from full-file technical checks.

## Resuming after a historical blocker

Reopen the exact recording, account and control before carrying an old download,
authentication or entitlement blocker forward. A previous upgrade marker or
account state may no longer apply. Preserve the failed receipt, record the
fresh observation that supersedes it, and resume the existing verified work.
Use the current Codex-browser and single-manager rules in `SKILL.md`.
