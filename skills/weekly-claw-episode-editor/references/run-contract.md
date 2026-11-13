# Required execution and evidence

Use `work/<episode>/skill-use-ledger.json` to index requirements, capabilities and immutable receipts. Reconcile existing evidence before resuming; do not repeat completed deliveries from a stale next action. The ledger supplements source/edit/QA/release records. It never grants publication authority.

## Establish the complete requirement set

Record exact episode or verified recording/take, revision, host, deliverable, current directions and applicable existing authority. Load each required reference before its stage and record its actual path/hash/read time. Read the publisher encode rules before final encoding and its operational/thumbnail skills before those requested stages.

Create a requirement row for **every applicable directive** in the entrypoint, current references, QA contract and episode instructions, with source document/hash, section and requirement text. The gate's mandatory IDs below are a minimum, not the complete checklist. Expand them into actual obligations; one phase-level PASS cannot replace separate requirements. Conditional inapplicability needs evidence, not absence from the plan. New directions or changed sources reopen affected proof/QA.

Cover scope/dependencies; complete ingest and source/transcript review; EDL/shared time map; participant/layout/privacy plans; selected native/legacy render path and moving proof; audio offsets/mix/repairs/listening; factual corrections and full presentation motion; branding/original ending; caption words/timing; reproducible exact-master QA; independent review/adjudication; and requested publisher handoff/delivery/cleanup.

## Build coverage from sources, then plan

Build the source-visual universe from the complete recording, every screen-share source and complete transcript **before** the EDL/storyboard. Review end to end using the actual transcript and video, retaining truthful coverage/method evidence. Include spoken slide/demo cues and private/setup material. A planned-insert list cannot define what is required.

Give each relevant slide/chart and meaningful screen/demo interval a stable ID; carry it through source inventory, EDL/layout, presentation coverage and exact-master evidence. Reconcile included, excluded, accepted-exception and unresolved IDs. Verify onset, readable content, meaningful motion and exit in the encoded master. Recover missing required visuals through ordinary authorized editing. An independent review must compare original source IDs and the full requirement set against final evidence, including items absent from the plan. A subset checker certifies only its declared subset.

## Verify capabilities; continue authorized work

Use small reversible real probes, recording host/time, observed result, evidence and affected stage. Skill folders, executable paths, old receipts and queued operations do not prove capability. Test current media inspection/transcript coverage; a short render through the selected supported editor/effects; actual fonts/brand/outro assets at delivery/mobile sizes; and an audio-capable reviewer receiving exact-master samples. Use current permitted Codex browser discovery/download and publisher account/image-generation probes when their stages need them.

Discover the supported current interface before calling an absent remembered path a blocker. Preserve failures, apply bounded supported recovery, continue independent phases and block only dependent requirements. Do not bypass access restrictions. Measurements/ASR/transcripts cannot establish listening, caption words, audible sync or natural cuts; those need actual audio-capable review with hashed samples, observations and coverage.

Ingest, source review, normal editorial choices, required visual restoration, captions preparation, QA, reversible corrections and recovery proceed under existing edit authority. Do not repeatedly ask permission for a mandatory phase or ask Henry to waive it because execution is inconvenient. Prepare concrete evidence before raising a substantive unresolved creative choice or optional omission/fallback. Reuse explicit accepted scope; preserve requested-editor, exact-thumbnail/release, account/platform and external-action boundaries. Edit authority alone does not grant Public publication, community sends, or account/feed changes.

## Gate input and invocation

Run the shared gate before completion/handoff, and again after affected inputs change:

```bash
python3 <editor-skill>/scripts/completion_gate.py work/<episode>/skill-use-ledger.json \
  --report work/<episode>/completion-gate-r<N>.json
```

The publisher adapter adds `--require-asset thumbnail`. Python callers use `check(ledger, episode_root, required_assets=('master', 'captions', 'source_manifest', 'thumbnail'))`. Relative paths resolve from the ledger's directory. File references are `{path, sha256}`; actual nonempty bytes must match. Durations/intervals use finite seconds and positive half-open `[start, end)` ranges; proof observations include the exit boundary.

Ledger schema `schema_version: weekly-claw-evidence-1`:

| Field | Required content |
| --- | --- |
| `episode_id`, `revision`, `assets` | Exact identity; hashed `master`, `captions`, JSON `source_manifest`, and requested `thumbnail`. Manifest `sources` rows contain `id`, `path`, `sha256`, `duration`, and actual `kind` (`camera`, `audio`, `screen`, `composite`, `archive`, `other`). Screens must have item IDs, including an explicit full-source excluded item when no relevant content exists. |
| `requirement_set` | Hashed JSON with `documents` (`id`, path/hash) and `requirements` (`id`, `document_id`, `section`, `requirement`, `master_bound`; optional `conditional`, `review_kind`, `required_intervals`). |
| `requirements` | Exact same ID set. Each row has `status`, hashed `evidence` list, current `master_sha256` when master-bound, and actual `review` receipt when required. Rows and reviews carry `bindings`: current hashes of `requirement_set`, `source_manifest`, `source_universe`, plus `master` when master-bound; `captions_words`/`independent_review` also bind `captions`. Definitions can name further `asset_bindings`. Pending/failed/missing rows refuse completion. |
| `capabilities` | IDs `media_inspection`, `source_transcript`, `native_render` (the selected render path), `brand_assets`, `audio_review`; each has `status: VERIFIED`, actual `probe`, `host`, `observed_at`, hashed `evidence`. |
| `source_universe` | Hashed JSON anchored by `source_manifest_sha256`; `sources` have exact source IDs, gap-free `reviewed_intervals`, hashed review `evidence` and expected `item_ids`; `items` reconcile those IDs. |

Mandatory requirement IDs are `capability_preflight`, `source_inventory`, `source_review`, `source_coverage`, `edl_time_map`, `native_proof`, `audio_listening`, `captions_words`, `master_technical`, `master_visual`, `outro`, `independent_review`.

An included universe item contains `id`, `source_id`, `source_interval`, `kind` (`static`/`motion`), `treatment`, `disposition: included`, `programme_interval`, current `master_sha256`, and at least three hashed `proof` observations with distinct `programme_time` at onset/content/exit. Required motion cannot use static treatment or shrink its source duration: source/programme spans must match within one actual master frame. The gate probes the actual master duration/frame rate with ffprobe rather than trusting a declared runtime. An excluded item needs reason (`duplicate`, `setup`, `removed_discussion`, `private`, `unusable`), explanation and hashed evidence; an unresolved relevant visual remains incomplete.

Actual review receipts contain `kind`, `result: PASS`, exact `master_sha256`, `reviewer`, `method`, `observations`, `observed_at`. `audio_listening` uses kind `listening`; `captions_words` uses `caption_words`: both require expected `required_intervals` covering the actual full master and covering observed `programme_intervals` in the receipt. Shrinking declared review spans cannot clear the gate. `independent_review` uses `requirements_reconciliation`, naming **all** `requirement_ids` and `source_item_ids` inspected.

`NOT_APPLICABLE` is allowed only for a conditional nonmandatory requirement with reason/evidence. `ACCEPTED_EXCEPTION` or universe `accepted_exception` needs a hashed acceptance JSON: `actor: Henry`, direct source/turn reference in `source`, exact `instruction`, `observed_at`, `episode_id`, current `master_sha256`, scoped `requirement_ids`, and `limitations`. A requirement acceptance carries the same current `bindings` as its row. A source-item exception uses ID `source_item:<id>` and binds `master`, `requirement_set`, `source_manifest`, plus `source_item`: SHA-256 of canonical sorted compact JSON for the item excluding its `acceptance` reference. This avoids a circular universe/acceptance hash.

## Completion and accepted cleanup

The gate returns `INCOMPLETE`, `EVIDENCE_COMPLETE`, or `EVIDENCE_COMPLETE_WITH_EXCEPTIONS`. Preserve exceptions/limitations; they never become listening/technical PASS or an unqualified “100%” claim. File/hash reconciliation cannot prove truthful observations or media quality: current native/media/perceptual checks still apply. A filename, process exit, upload badge, `next_actions: []`, or self-declared COMPLETE cannot replace evidence. Restore concrete next actions for pending requirements; report technical, visual, caption-word, listening and release states separately.

Keep Henry's existing raw-source cleanup authority after the exact corrected YouTube upload passes checks and its listed account/visibility/picture/audio/ending conditions are actually verified. No additional personal approval is required. Before deletion retain master/captions/metadata/EDL/edit JSON, source IDs/hashes and QA/release receipts. A missing-content candidate or processing badge cannot trigger cleanup.

After authorized deletion, `source_cleanup` may reference a hashed JSON receipt bound to `episode_id`/`master_sha256`. It contains `acceptance_checks` IDs `account`, `visibility`, `picture`, `audio`, `ending`, `youtube_checks`, each with PASS, actual observations/time and hashed evidence. `deleted_sources` records exact source `id`/path/hash and a hashed retained `verification` JSON with `id`, original `sha256`, positive `bytes`, `verified_at`, and hashed `probe` JSON containing actual ffprobe streams/duration. This preserves completed ingest without forcing re-download; missing evidence keeps the affected claim incomplete.
