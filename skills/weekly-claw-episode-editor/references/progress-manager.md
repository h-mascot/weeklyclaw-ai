# Run-scoped progress manager

Use one authorized project owner and one durable progress manager per run. Reuse an existing manager, preserve state, and do not create duplicate workers or schedulers. Verify live recording inventory before claiming no actionable recording; document blocked discovery and recovery. Use bounded polling for active operations and preserve incomplete work.

## Durable state

Create `work/<episode>/progress-manager.json` before the first browser or render
action. Keep the ingest ledger as the source of truth for files; the manager file
records the control plane:

```json
{
  "schema_version": 1,
  "episode": "27",
  "manager_kind": "heartbeat",
  "manager_id": "weekly-claw-progress-manager",
  "status": "ACTIVE",
  "phase": "INGEST",
  "started_at": "<UTC ISO-8601>",
  "last_check_at": "<UTC ISO-8601>",
  "last_progress_at": "<UTC ISO-8601>",
  "next_action": "<one exact reversible action>",
  "recovery_attempts": [],
  "stop_reason": null
}
```

Use `DONE`, `BLOCKED`, or `INTERRUPTED_INCOMPLETE` for terminal states. Each
recovery attempt records a timestamp, observed condition, smallest attempted
action, result, and fresh evidence path. Write state atomically and reread it
after each transition.

## Start and reuse rules

1. At the first material step, inspect `progress-manager.json` and the active
   automation list. Exactly one native Codex heartbeat owns this control plane
   and is attached to the pinned **🎬 Weekly Claw** task identified above.
   Resume and steer that same thread on every poll or continuation. Never
   create a fresh manager thread merely because a tick, session, or worker
   ended.
2. All Riverside and publishing web actions use only the Codex app's built-in
   authenticated browser. Chrome, Playwright, and external browser sessions
   are prohibited, including as a fallback for a blocked transfer.
3. A project cron is not an acceptable manager because each tick starts a
   fresh conversation. Do not create per-episode managers or fallback cron
   copies. Record the canonical heartbeat ID, target thread, cadence, worktree,
   and owner in `progress-manager.json`; this heartbeat is both the weekly
   dispatcher and the run supervisor. Keep due-date claims separate from
   verified episode completion.
4. Apply resume-first continuity and lean bounded execution: one owner, one
   worker per conflicting resource key, compact delta-first checks, immutable
   receipts, and bounded repair attempts. A separate observer may report but
   never mutate or restart the run. The heartbeat supervises processes owned by
   the same canonical task. It checks the worker/process identity before relaunching
   and never starts a second worker
   while the recorded one is alive. A stale completion notice is history, not a
   reason to regress state or duplicate work.
5. The manager covers every phase—Riverside ingest, transcript/EDL, render,
   media QA, thumbnail archive, and gated handoff—not only downloads. It may
   perform safe, reversible recovery and continue the owner's authorized work.
   The heartbeat grants no new authority to upload or publish; the owner must
   satisfy all exact-package approvals, actor checks, and duplicate checks.
   Never bypass an approval or infer acceptance of platform terms.

## Dependency-scoped blockers

Track `stage_blockers` separately from run status. Each entry records stage,
status, observed evidence, exact recovery, and what depends on it. An unavailable
YouTube account holds YouTube upload/visibility checks, not Riverside ingest,
editing, local QA, captions, thumbnail work, or release-copy preparation.
Approval pending likewise does not stop unrelated safe preparation.
Maintain ACTIVE and choose an actionable `next_action` while independent work
remains. Missing source tracks still prevent final editing/QA claims requiring
those sources; inventory and recover other tracks without silently omitting anyone.

## Check and recover

On each tick, read compact deltas first: current phase, state hashes, active
process/transfer IDs, temporary-file sizes, `last_progress_at`, and the exact
next action. Use the phase cadence (generation 30–60 seconds, active transfers
10–30 seconds, render/QA according to observed progress) and emit terse healthy
status unless a transition or failure needs detail.

If progress is observable, wait and keep checking. If a phase has made no
progress for 15 minutes, do the smallest compatible recovery in this order:

1. Reconcile durable state with the live process, filesystem, and current
   Riverside/page state; do not trust a stale self-report.
2. Resume the existing transfer/render if its process and partial output are
   healthy.
3. Refresh and reopen only the exact recording/track or rerun only the failed
   block. Preserve verified artifacts and receipts.
4. Record the result and reread state before deciding whether another attempt is
   needed.

A browser download event is transport evidence only. If a hidden-tab attempt
times out while a visible foreground Codex tab shows the exact Riverside row and
a growing `.crdownload`, preserve that transfer and do not restart it. Reconcile
the completed file to the exact participant/track/duration/resolution row;
aligned exports may contain leading black or padding, so inspect per-stream
start and duration, `blackdetect`, and sampled active frames before accepting.
Record the unchanged file, container and active coverage, size, SHA-256, and
exact row evidence. A visible-tab correlation is a proven recovery path for the
run, not proof of root cause or permission internals.

If the hidden attempt produced no transfer, reopen the exact recording in a
visible foreground Codex tab, re-resolve the exact row, register the documented
download listener before clicking one exact visible option, and observe the
filesystem; never bypass an access restriction. Scope every state transition
and receipt to its exact `row_id`, and compute `verified_file_count` from
per-file path, size, and SHA-256 validation rather than trusting a copied or
stale aggregate.

After three documented recovery attempts, a fresh view may classify the affected stage as
`BLOCKED` only for an authentication/CAPTCHA gate, a missing or failed required
source, a repeatedly non-progressing export/render, or a human approval or
irreversible choice. A worker exit, transient tool error, failing test, stale
cache, or parent-session ceiling is recoverable work: salvage the artifacts,
repair or relaunch the bounded phase, and continue. If an external ceiling ends
the run, record `INTERRUPTED_INCOMPLETE` and the exact next browser/terminal
action; do not call it blocked or complete.

## Stop and hand off

Editor/QA success does not end remaining authorized preparation or distribution.
At a human gate, record the affected stage and continue independent work.
Pause an individual run when it has no actionable independent work. The combined
heartbeat stays ACTIVE for future weekly triggers; quiet no-op when no run,
valid unclaimed inbox request, or Friday trigger is actionable. Record DONE only for verified
completion; otherwise retain the exact unresolved gate and completed artifacts.
On interruption, remain resumable with the next action in the manager file and
episode memory. Never create a second heartbeat for a new episode.
