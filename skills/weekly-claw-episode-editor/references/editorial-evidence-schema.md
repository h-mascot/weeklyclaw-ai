# Editorial evidence schema

`editorial_evidence.py` checks a small, episode-local evidence plan. The plan
is a structural receipt for review preparation; it is not an editorial,
listening, native-playback or release approval.

The plan uses half-open integer frame ranges: `[start, end)` includes `start`
and excludes `end`. `programme_frames` is the complete programme length. Every
retained segment names a source and an explicit source range. An insert is an
ordinary retained segment with `kind: "insert"`, but its `source_id` must be a
separate source ID. Removed material is represented by omission and may not be
bridged by a fabricated continuous source range.

Rates are rational `{ "num": 24, "den": 1 }` (the aliases `numerator` and
`denominator` are accepted). If rates are omitted, the validator supports only
the explicit rate-1 map, so source and programme durations must be equal. It
does not infer offsets across edits.

The native geometry profile `native-evidence-2026-10-04.1` uses the same
evidence boundary. Its `group_states` list declares each currently visible
group roster and one integer `[x, y, width, height]` viewport per member. Each
state must cover the full landscape canvas with contiguous full-height
side-by-side tiles; a two-person state may omit a participant who is absent in
that state. A row may use `transform` when its native transform ID differs from
the participant ID. Each declared transform must scale its portrait picture to
the full viewport. Source-limited enlargement is permitted only on that
individual transform with a hashed `review_evidence` object and a nonempty
`limitation_reason`; a general `approved` flag cannot grant enlargement.

## Minimal example

```json
{
  "validator_anchor": {
    "name": "editorial_evidence",
    "version": "2026-10-04.1",
    "project_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "project": { "path": "episode.kdenlive", "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" },
  "programme_rate": { "num": 24, "den": 1 },
  "programme_frames": 144,
  "sources": [
    { "id": "camera-a", "path": "camera-a.mp4", "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "rate": { "num": 24, "den": 1 } },
    { "id": "prior-quote", "path": "prior-quote.mp4", "sha256": "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc", "rate": { "num": 24, "den": 1 } }
  ],
  "source_to_programme": [
    { "kind": "source", "source_id": "camera-a", "programme_start": 0, "programme_end": 96, "source_start": 1200, "source_end": 1296 },
    { "kind": "insert", "source_id": "prior-quote", "programme_start": 96, "programme_end": 120, "source_start": 400, "source_end": 424 },
    { "kind": "source", "source_id": "camera-a", "programme_start": 120, "programme_end": 144, "source_start": 1320, "source_end": 1344 }
  ],
  "cues": [
    { "id": "topic-cue", "source_id": "camera-a", "source_start": 1210, "source_end": 1230 }
  ],
  "graphics": [
    { "id": "topic-card", "cue_id": "topic-cue", "onset_programme_frame": 31,
      "display_end_programme_frame": 60,
      "asset": { "path": "topic-card.png", "sha256": "9999999999999999999999999999999999999999999999999999999999999999" } }
  ],
  "solos": [
    {
      "id": "speaker-a-solo-1",
      "declared_speaker": "speaker-a",
      "actual_speaker": "speaker-a",
      "programme_start": 10,
      "programme_end": 90,
      "sustained_contribution_rationale": "A connected explanation continues across the retained solo range.",
      "transcript_evidence": { "path": "speaker-a.txt", "sha256": "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd", "source_id": "camera-a", "source_start": 1210, "source_end": 1290 },
      "audio_evidence": { "path": "speaker-a.wav", "sha256": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "source_id": "camera-a", "source_start": 1210, "source_end": 1290 }
    }
  ],
  "programme_marks": [
    {
      "id": "weeklyclaw-mark",
      "track": "programme-mark",
      "programme_start": 0,
      "programme_end": 144,
      "position": "global-bottom-left",
      "backing_plate": false,
      "asset": { "path": "weeklyclaw-mark.png", "sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff" }
    }
  ]
}
```

The graphic asset hash and its display end are required. The cue range is also
half-open: if the mapped cue ends at exclusive programme frame `31`, onset
frame `31` is the first frame after the completed cue and is valid; frame `30`
is premature.

A native geometry group state has the following compact shape:

```json
{
  "profile": "native-evidence-2026-10-04.1",
  "canvas": [1920, 1080],
  "group_states": [{
    "id": "current-group",
    "members": ["speaker-a", "speaker-b"],
    "viewports": [
      { "member": "speaker-a", "transform": "speaker-a-group", "viewport": [0, 0, 960, 1080] },
      { "member": "speaker-b", "transform": "speaker-b-group", "viewport": [960, 0, 960, 1080] }
    ]
  }],
  "transforms": [
    { "id": "speaker-a-group", "crop": [600, 675, 0, 0], "scale": [960, 1080],
      "source_limited_enlargement": {
        "review_evidence": { "path": "scale-review.md", "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" },
        "limitation_reason": "The verified source is portrait-safe only at this crop; the review records the resulting detail limitation."
      } },
    { "id": "speaker-b-group", "crop": [960, 1080, 0, 0], "scale": [960, 1080] }
  ]
}
```

The native helper still returns `CHECKED_SUBSET_PENDING_REVIEW` on success.
It requires actual native XML bindings, source and sample hashes, and review
measurements, but it does not certify native effect semantics, creative intent,
perceptual quality, listening, privacy or release.

The example hashes are placeholders; an actual plan must contain hashes of the
exact local files. The project hash is repeated in `validator_anchor` so a
report cannot be detached from the project it describes. Reports are created
with exclusive file creation and include the plan and validator hashes when
invoked through the command line.

Each solo declaration includes a programme interval. Its transcript and audio
evidence records each carry their own hash plus `source_id` and a source
half-open range that maps across the declared solo interval; a matching speaker
label alone is insufficient. A graphic carries its hashed asset and a
`display_end_programme_frame` as well as its onset.

The checker verifies source/programme continuity, explicit durations and rates,
evidence hashes, speaker declaration versus supplied evidence labels and
coverage, cue completion ordering, and one transparent full-length global mark
declaration.
It cannot establish that the speaker is actually speaking, that a cue is
semantically complete, that an overlay is correctly timed in the native
editor, or that an alpha mark survives compositing and encoded playback. Those
claims require native playback, visual inspection and listening review.
