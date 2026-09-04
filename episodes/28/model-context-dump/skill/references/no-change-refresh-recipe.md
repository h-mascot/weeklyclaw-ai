# No-change REFRESH tick recipe

Use this on every REFRESH tick that finds no host feedback, no new
candidate, and no drift between `revs/` artifacts and `state.json`
`artifact_hashes`. The skill says "no-change refreshes return NO_REPLY";
the cron output contract says emit `OK · <job> · no action`. Honor the
contract. NO_REPLY is for out-of-window ticks, not in-window no-changes.

## Inputs to inspect every tick

1. `episodes/<N>/showprep/` directory — `find -newer <state.json> -type f`
2. `episodes/<N>/showprep/workflow-feedback.md` — append-only host log
3. `episodes/<N>/showprep/revs/*` — mtimes should all be ≤ BUILD time once stable
4. `episodes/<N>/showprep/state.json` `artifact_hashes` — recompute SHA-256 of each `revs/*` and assert equality
5. Originating Telegram topic — read via `hermes send --list telegram` or chat history. No new direct host message from `855505513` or `7615999206` since last successful tick = no feedback to apply.

## Tick ID

`<episode>-<NY date>-<NY hour>` (e.g. `24-2026-08-07-13`).

## Locking

- Skip lock acquisition for no-change REFRESH ticks — there are no writes
  to coordinate. If a lock is present from a prior interrupted run,
  verify the PID is dead (`ps -p <pid>`) and remove it; record the reason
  in `runlog.md`.
- Always `rm showprep/state.lock` on every exit path before returning,
  including no-change refreshes.

## runlog.md append block

```markdown
## YYYY-MM-DD HH:00 EDT — REFRESH tick (<episode>-YYYY-MM-DD-HH)

- Gate: `TZ=America/New_York date '+%u %H %Y-%m-%d %Z'` → `4|5 HH YYYY-MM-DD EDT` → Thursday/Friday HH:00 EDT → REFRESH. (Thursday 12–15 and Friday 11–14 are both REFRESH slots since the 2026-08-20 Thursday-BUILD move; the gate weekday digit is 4 on Thursday, 5 on Friday.)
- Role: REFRESH. Tick ID: `<tick-id>`.
- Lock: none held on entry; no fresh lock needed for a no-change refresh tick.
- Inputs inspected since last successful tick (<HH-1>:00 EDT):
  - `episodes/<N>/showprep/` directory mtime — no new files since ...
  - `workflow-feedback.md` — last entry <date> (<host>: <instruction>)
  - `revs/*` mtimes — all ≤ BUILD time
  - Telegram topic — no new host message from 855505513 / 7615999206
- Story-set unchanged: S1 ... · S2 ... · ... · S5 ...
- Artifact hash readback: SHA-256 recomputed for each of the seven
  rev1 artifacts. Comparison surface depends on what BUILD stored in
  `state.json`: if `artifact_hashes` is present, compare against it
  directly; if only `artifacts` paths + `validation` receipt (current
  Episode 25+ pattern) are recorded, assert non-empty + size-stable
  vs the BUILD-time `validation` block. The point is to prove no
  drift since BUILD. Local short-hash readback:
  agenda <short> · deck <short> · speaker-notes <short> · talking-points
  <short> · henry-section <short> · andy-section <short> · host-cheat-sheet <short>.
- No new ≥9.0 candidate surfaced this hour that beats the lowest
  unpinned selected story by ≥0.5; no proposed swap.
- 2-hour reminder status: canonical 2 PM ET reminder fires at 14:00 EDT;
  this tick is HH:00, not the reminder slot. No reminder posted.
- Approval: UNVALIDATED. Root artifacts NOT overwritten. Discord
  lifecycle post NOT executed.
- Pending human action: Henry / Andy `APPROVE` / `SWAP` / `DROP` /
  `PIN` / `ORDER` via Telegram @Henry (id 855505513) / @Andy (id 7615999206).
- Cron definition: NOT modified.
```

## Wire output (final response)

```text
OK · WeeklyClaw Episode <N> Friday show prep · no action (REFRESH tick HH:00 EDT, no host feedback, no new candidate, all 7 rev1 artifacts hash-stable, lineup UNVALIDATED, <next reminder or action> pending)
```

The wire-output line MUST start with `OK ·` or `FAIL ·` per
`[CRON_OUTPUT_CONTRACT_V1]`. The narrative above is the `runlog.md`
appended evidence, not the wire output.

## 2 PM reminder (only) — when UNVALIDATED at 14:00 ET FRIDAY

Reminder fires only on the Friday 14:00 ET tick. Thursday 14:00 is a plain
no-change REFRESH despite being "BUILD day + 3h" — never post a reminder on
Thursday. If `state.json` `approval_state == UNVALIDATED` and the tick is
Friday `*-14` (14:00 ET), post a single short reminder to the originating
Telegram topic:

```bash
hermes send --to "telegram:-1004370723812:17" \
  --subject "[WeeklyClaw Ep <N>] 2 PM reminder" \
  --file /tmp/weeklyclaw-ep<N>-reminder.md
```

Where `/tmp/weeklyclaw-ep<N>-reminder.md` is a one-screen pointer:

```markdown
📍 WeeklyClaw Ep <N> draft is still UNVALIDATED (2 PM ET reminder).

Review card: `episodes/<N>/showprep/review-card.md`
Artifacts:   `episodes/<N>/showprep/revs/` (rev1)
Commands:    `APPROVE` · `SWAP <slot> <candidate>` · `DROP <slot>` · `PIN <candidate>` · `ORDER ...` · free text
Deadline:    3 PM ET FREEZE
Pinned:      S3 (Andy, 2026-08-06)
```

Do NOT post the full review card. Do NOT post at any hour other than
14:00 ET unless state changed materially. Do NOT post when
`approval_state == APPROVED`.

## Common traps

- "BUILD + 2h = 13:00" is wrong; the reminder is at 14:00 ET Friday. Since
  the Thursday-BUILD move, "BUILD day + 3h = Thursday 14:00" is ALSO wrong —
  Thursday 14:00 is a plain no-change REFRESH, not a reminder slot.
- Treating `NO_REPLY` as the correct wire output for an in-window
  no-change refresh breaks the cron delivery contract.
- Skipping the `revs/*` hash readback because "nothing changed" — the
  whole point of the tick is to prove no drift.
- Locking the workspace for a no-change refresh — there are no writes
  to coordinate, so lock acquisition just adds noise and can wedge the
  next tick if cleanup is sloppy.

## FREEZE drift reconciliation (Episode 25 lesson)

`state.json` can lag behind reality even when the BUILD itself was clean.
Two common drift patterns seen in the wild:

1. **Revision-number drift.** `state.json` `selected_revision` and
   `artifacts.*` paths still point at rev3, but rev4 was authored
   outside the cron (Henry's manual edit, a parallel rebuild from a
   non-Cursor path, or a Talk-Track-only refresh that bumped the
   `_slides_content` file but kept the deck HTML hash stable because
   the slide markup didn't move). The website repo already has rev4
   bytes deployed, but local state still says rev3.
2. **Website parity drift.** Local `revs/deck.rev<N>.html` differs
   from `https://weeklyclaw.ai/episodes/<N>/deck` because the standing
   website publish ran before the latest local edit, or because the
   git worktree commit/push was incomplete.

The FREEZE tick (15:00 ET) is the last chance to catch either before
delivering the freeze summary. Reconciliation steps, in order:

1. **Recompute the highest existing revision.** `ls
   episodes/<N>/showprep/revs/*.{md,html,py} | sort -V` — pick the
   max revision suffix. That is the candidate canonical revision.
2. **Compare to `state.json` `selected_revision` and `artifacts.*`.**
   If they already match, no action. If they don't, the cron (or the
   human who edited revs out-of-band) forgot to update `state.json`.
3. **Promote `state.json` to the highest rev** by patching
   `selected_revision` and every `artifacts.*` path to use that rev
   suffix. Re-validate with `python3 -m json.tool state.json`. Record
   the promotion in `runlog.md` under the FREEZE tick block:
   "Drift detected and reconciled: state.json promoted rev3→rev4
   (artifacts paths rewired, JSON re-validated)."
4. **Re-run the validator** on the promoted revision
   (`python3 qa/validate_deck.py revs/deck.rev<N>.html
   revs/speaker-notes.rev<N>.md <prior-approved-ep>/deck.html`) before
   locking. Exit 0 required.
5. **Byte-check the live website** against the promoted local files:
   ```bash
   curl -sL "https://weeklyclaw.ai/episodes/<N>/deck" | sha256sum
   curl -sL "https://weeklyclaw.ai/episodes/<N>/agenda-draft/index.html" | sha256sum
   curl -sL "https://weeklyclaw.ai/episodes/<N>/host-cheat-sheet" | sha256sum
   ```
   Compare each returned SHA-256 against the local rev file. A
   mismatch means a standing website publish failed or a manual
   website edit landed out-of-band — re-run the standing website
   publish route from `references/website-draft-publication.md` and
   re-verify, or BLOCK the FREEZE if the publish route is unreachable
   from the cron context.
6. **Do not promote root artifacts.** Root artifacts at
   `episodes/<N>/` stay byte-identical until Henry or Andy approves.
   The drift reconciliation only touches `state.json` + `revs/` + the
   live website — not the canonical root.

If the cron cannot reach the prior APPROVED episode's deck for the
validator third argument (e.g., remote authority file not present in
the cron workdir), fall back to the base 8 checks and record the
limitation in the FREEZE block.

The FREEZE wire-output summary should name the **promoted** revision
in the lineup/receipt lines, not the `state.json` value the cron read
on entry.