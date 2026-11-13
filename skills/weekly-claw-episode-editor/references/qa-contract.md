# Final-master QA contract — 2026-10-04.1

## Required artifacts

- current [requirement/capability ledger](run-contract.md), including independent source-universe reconciliation and exact-master completion decision
- source manifest
- complete transcript or matching captions
- source-time EDL with keep/remove reasons and versioned source-to-programme map
- machine-readable layout plan
- reconciled presentation-coverage inventory with source/spoken-cue/programme bindings, expected/included/excluded/unresolved counts, exclusion evidence and exact-master visual proof
- current [editorial evidence plan and subset check](editorial-evidence-schema.md), with actual speech/native review recorded separately
- storyboard/contact sheet
- focused regression tests
- A/B audio clips for every repair
- primary-source list and correction map
- render report
- media-audit report

## Structural assertions

- Output path identifies exact episode and revision.
- QA reports and approvals identify the exact master SHA-256; an earlier episode or revision cannot supply a later candidate's approval.
- Expected duration equals EDL duration plus explicit intro/outro additions within one frame or documented mux tolerance.
- Every expected participant has group coverage while present. Each solo has sustained actual-speaker evidence; no solo quota applies.
- Every screen or primary-source asset maps to an explicit interval beginning after its completed spoken-topic introduction.
- Every relevant slide/chart and meaningful screen/demo interval in retained discussion is accounted for and included. Reconcile the source inventory with the plan and exact final encoded master, not just the subset chosen for a storyboard. An editor's preference, time budget or written omission reason cannot waive relevant coverage. Only a scoped user instruction/acceptance can authorize a relevant omission or fallback; preserve its exact scope and report the limitation rather than an unqualified coverage PASS.
- Every Discord excerpt maps to a relevant discussion interval and passes a privacy crop/redaction review.
- Every correction card maps to a transcript timestamp and authoritative source.
- Outro exists in the exact final master, not only an upstream version.
- Cameras, captions, audio, graphics, footers, archive, chapters and ending share the current time map. Missing requested motion, exact evidence or historical scroll remains disclosed as missing/fallback.

## Video assertions

- 1920×1080 square pixels and 16:9 display.
- Constant intended frame rate.
- H.264 High profile.
- For a 1080p YouTube upload master, record average video bitrate and satisfy the publisher's existing 4,000 kbps release gate. Probe the final candidate; compliant upstream blocks alone do not pass it.
- yuv420p with BT.709 primaries, transfer, and matrix.
- No black/broken frames at opening, joins, sampled intervals, or closing.
- Full-frame group panels use deliberate per-participant
  framing: eye lines are normally within 30–50 px vertically at 1080p, face
  heights are visually comparable (about 15% tolerance), headroom is
  consistent, crops follow actual face/eye positions rather than geometric
  center by default, and crowns/chins are not clipped. Document intentional or
  source-limited exceptions with hashed actual-preview review. Preserve requested
  frame fill; no decorative bands, solo side padding or universal enlargement factor.
- Frame count and duration agree within one frame.
- Newly rendered and reused blocks have probed frame counts; moving-demo blocks preserve source-time motion through frame-rate conversion and overlays.
- Every source graphic and changed native transform has moving proof, including complete diagram content, rail fit and pan/zoom extrema.
- Unchanged video elementary stream matches its comparison hash when audio-only repair is claimed.
  Compare hashes produced with the same extraction/representation, never a whole-file hash against an elementary-stream hash.

## Audio assertions

- 48 kHz final sample rate.
- Mono or stereo as intended; no accidental channel drop.
- Dialogue targets -16 to -14 LUFS and must remain between -18 and -12 LUFS unless documented otherwise.
- True peak targets no higher than -1.5 dBTP and must remain at or below -0.1 dBTP unless documented.
  Measure these on audio decoded from the final encoded candidate, not only upstream PCM.
- No clicks or level jumps at repair boundaries.
- Named retained speaker remains intelligible throughout full repaired interval.
- Unwanted voice is checked perceptually and with waveform/speaker evidence.
- Outro music starts and fades at specified timestamps.

## Editorial assertions

- Opening starts cleanly and establishes episode.
- Technical failures, restarts, apologies, and post-show talk are removed unless editorially useful.
- Topic transitions remain coherent after cuts.
- Slides, articles, and posts are readable.
- Every required presentation row has exact-master onset/content/exit evidence; moving material has multiple playback/frame observations demonstrating its meaningful action. Zero source visuals, missing inventory rows, token representative cards or stills substituted for required motion fail editorial coverage, even when the technical audit passes. Genuine exclusions for duplicate/setup/removed discussion/private or unusable content need source evidence; unresolved relevant content holds editorial completion and upload.
- Correction text retains literal glyphs and leaves mouths/chins unobscured. One alpha-transparent stacked programme mark stays at a fixed global bottom-left position across every layout, source image, archive and outro with no plate. Prevent duplicate baked programme overlays while preserving authentic source logos and original ending artwork. Names/verified handles remain tile-local without moving the global mark; confirm current guest identity and never guess a handle.
- Optional Discord material is omitted without blocking when absent; when used, only relevant privacy-safe excerpts appear.
- Group scenes are the conversational default; full-width solos are supported sustained actual-speaker contributions.
- Group framing remains balanced during neutral posture, movement, and
  laughter; no participant appears accidentally higher, lower, larger, or more
  tightly cropped than the others.
- Proper nouns and source attribution are fact-checked.
- Captions match final timeline.
- Caption cues crossing cuts contain no removed setup dialogue; uncertain ASR words are checked audibly rather than guessed.
- Meaningful guest speech and reactions remain; caption all intelligible contributions. Invitation/decline cuts need actual naturalness audition or remain uncut.
- Original ending picture and music survive the exact final file; canonical links are verified and internal review stamps removed. Vertical clips use their scoped ending/aspect checks from [editorial-direction.md](editorial-direction.md).

## Execution proof

1. Run focused tests.
2. Run `scripts/media_audit.py` with `--full-decode`.
3. Before the long render, deliver/review actual native moving proof for every layout/source graphic and changed transform; after render inspect the exact final artifact.
4. Review every junction and repaired interval.
5. Run Codex review.
6. Read and adjudicate findings even when a review helper exits zero or prints a clean footer; record accepted/rejected findings.
7. Complete Jeff Dean review.
8. Complete Luke W + Ryan Singer review for visual changes.

Before any final/DONE/COMPLETE claim, reconcile every applicable requirement from the loaded current editor references and this contract under [run-contract.md](run-contract.md). `next_actions: []`, a successful tool/worker exit, planned-shot coverage, and self-declared PASS flags do not clear missing rows or pending caption-word/listening checks.

Do not call an episode final while required assertions lack evidence. An explicitly accepted perceptual limitation must be recorded with its scope and remaining uncertainty; acceptance is not a technical or listening PASS.

Record technical and perceptual results separately. Neither a transcript nor a
waveform/loudness/decode result proves listening. When no audio-capable reviewer
is available, supply exact-master playback samples and leave the audible checks
pending until reviewed or explicitly accepted by Henry with the scope recorded.
