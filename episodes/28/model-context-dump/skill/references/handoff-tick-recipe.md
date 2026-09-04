# Friday 16:00 ET HANDOFF tick recipe

Use this on the **HANDOFF** role (Friday 16:00–16:59 ET). The HANDOFF is
read-only: it does not regenerate the deck, does not post the review
card, and does not post the 2 PM reminder (that fires at Friday 14:00,
not 16:00). Its job is to deliver a compact, read-only summary of where
the show package stands at air time so the cron contract is satisfied
without mutating anything.

## What HANDOFF is NOT

- Not a regeneration tick. Do not run Cursor, do not bump `selected_revision`,
  do not edit `revs/*`, do not push to the website repo, do not touch
  root artifacts (`episodes/<N>/{agenda.md,deck.html,…}`).
- Not a review-card delivery. The last review card is the one posted at
  the most recent BUILD/REFRESH; HANDOFF does not repost it.
- Not a reminder slot. The 2 PM reminder is Friday 14:00 ET only.
  HANDOFF is 16:00 ET, two hours after the reminder.
- Not an approval solicitation. The show is starting. Hosts and viewers
  are entering live. The only valid host action at this point is
  `APPROVE` (or `SWAP` / `DROP` / `PIN` / `ORDER` against a still-UNVALIDATED
  lineup), which the publication runbook will pick up on Monday.

## Inputs to inspect

1. `episodes/<N>/showprep/` directory — `ls -la` to confirm no new files
   since the 13:00 ET REFRESH (or since the last host-triggered rebuild).
2. `episodes/<N>/showprep/workflow-feedback.md` — last mtime; if
   unchanged since the last successful tick, no new host directive.
3. `episodes/<N>/showprep/state.json` — read `approval_state`,
   `selected_revision`, `selected_revision_paths`, and the latest
   `artifact_hashes_rev<N>` block.
4. `episodes/<N>/showprep/revs/` — confirm the highest `*.rev<N>.{html,md,py}`
   exists and matches `state.json.selected_revision`. The
   `selected_revision_paths` block may lag reality (the FREEZE drift
   recipe in `no-change-refresh-recipe.md` covers this); the truth is
   the highest rev on disk, not the path string in state.json.
5. `https://weeklyclaw.ai/episodes/<N>/deck` —
   `curl -s | sha256sum` and compare against the local
   `revs/deck.rev<N>.html` SHA-256. SHA-equal is the strongest deploy
   proof. Do not skip this even on a HANDOFF tick.
6. `/agenda-draft` and `/host-cheat-sheet` — 200 OK canary only at
   HANDOFF (full byte-check is reserved for BUILD/REFRESH).
7. Telegram topic — not polled at HANDOFF. If the show is starting,
   hosts are in the venue/Studio, not sending approval commands.

## Locking

- Do not acquire `showprep/state.lock` at HANDOFF. There are no writes
  to coordinate. If a stale lock exists from a prior interrupted run,
  verify the PID is dead (`ps -p <pid>`) and remove it; record the
  reason in `runlog.md` as part of the HANDOFF block.
- Always confirm no lock survives the tick before returning.

## runlog.md append block

```markdown
## YYYY-MM-DD 16:00 EDT — HANDOFF tick (NN-YYYY-MM-DD-16)

- Gate: `TZ=America/New_York date '+%u %H %Y-%m-%d %Z'` → `5 16 YYYY-MM-DD EDT` → Friday 16:00 ET → role = HANDOFF.
- Tick ID: `<tick-id>`.
- Lock: none held on entry; no lock acquired (read-only role).
- Inputs inspected since last successful tick (HH:00 ET):
  - `episodes/<N>/showprep/` directory mtime: no new files since …
  - `workflow-feedback.md` mtime: unchanged → no new host directive.
  - `revs/*` mtimes: all ≤ last successful tick; highest rev on disk = <N>.
  - `state.json.selected_revision` = <N>; `selected_revision_paths` may
    point at a prior rev (drift — see FREEZE recipe; truth is disk rev).
  - `https://weeklyclaw.ai/episodes/<N>/deck` SHA-256 = local
    `revs/deck.rev<N>.html` SHA-256 → EQUAL (live deploy current).
  - `/agenda-draft` and `/host-cheat-sheet` → 200 OK.
- HANDOFF summary (read-only, no regeneration):
  - State: UNVALIDATED | APPROVED.
  - Done: five news segments (S1…S5) + Signal From Outside + Hot Take +
    Herald/Heritage sponsor rotation (Herald first per Ep<N-1> inversion).
    Seven-artifact contract met: agenda/deck/speaker-notes/talking-points/
    henry-section/andy-section/host-cheat-sheet at rev<N>.
  - Now: show begins 4:00 PM ET. Hosts and viewers enter live.
  - Blocker: no host approval received during 11–16 ET windows.
  - Next: post-show on Monday, root promotion to `episodes/<N>/{agenda.md,
    deck.html, henry-talking-points.md, host-cheat-sheet.md}` if APPROVED;
    otherwise BUILD for the next episode at Thursday 11:00 ET next week.
  - Final paths: `episodes/<N>/showprep/revs/*.rev<N>.*` plus
    `https://weeklyclaw.ai/episodes/<N>/{deck,agenda-draft,host-cheat-sheet}`.
  - Approval: UNVALIDATED. No late story. No changes since 13:00 ET REFRESH.
```

## Wire output (final response)

Per `[CRON_OUTPUT_CONTRACT_V1]`: max 6 short bullets and 700 characters.
Lead with status and action. For HANDOFF the pattern is:

```text
State: <UNVALIDATED|APPROVED> rev<N> live (SHA-equal local↔weeklyclaw.ai).
Done: <one-line package summary, e.g. "5 news + Signal + Hot Take, 7-artifact contract met, Herald/Heritage rotation applied">.
Now: show begins 4:00 PM ET.
Blocker: <no host approval | none>.
Next: <post-show Monday root promotion if APPROVED, else Ep<N+1> BUILD at Thursday 11 ET>.
Final paths: <revs/*.rev<N>.* + weeklyclaw.ai URLs>.
No late story; no changes since <last successful tick>.
```

For a HANDOFF where nothing has changed since the 13:00 ET REFRESH and
state is UNVALIDATED, the shorter form is acceptable:

```text
OK · WeeklyClaw Episode <N> Friday show prep · no action (HANDOFF tick 16:00 EDT, rev<N> live SHA-equal, no host feedback during 11–16 ET windows; show begins at 4:00 PM ET).
```

## Common traps

- **Treating 16:00 as a FREEZE recap.** FREEZE is 15:00. HANDOFF at 16:00
  is its own role and is read-only; do not re-emit the FREEZE block.
- **Posting the 2 PM reminder at 16:00.** Reminder fires at Friday 14:00
  ET only. A 16:00 reminder is late, redundant, and breaks the
  "one reminder per show" contract.
- **Re-running the FREEZE drift reconciliation at HANDOFF.** The
  `selected_revision_paths` block may point at rev6 while the truth on
  disk is rev10, but HANDOFF is not the place to rewrite `state.json`.
  If drift is detected at 16:00, record it in the HANDOFF block as a
  note for the post-show Monday publication run; do not patch
  `state.json` mid-HANDOFF.
- **Skipping the live SHA-equal check.** The FREEZE tick already did
  it; HANDOFF should re-do it in one curl + sha256sum because the
  15:00–16:00 window is the highest-risk time for an unscheduled
  website edit (hosts sometimes tweak the site directly right before
  air). SHA-equal at 16:00 is the deploy proof the post-show Monday
  publication run relies on.
- **Sending a Telegram message at HANDOFF.** The show is starting;
  hosts are not at their desks. Do not post a reminder, do not post a
  status update. The wire output goes to the cron delivery channel,
  not the WeeklyClaw Telegram topic.

## Relationship to other recipes

- `no-change-refresh-recipe.md` covers REFRESH (Thursday 12–16, Friday
  11–14) and the FREEZE (Friday 15) drift reconciliation. This file
  covers the HANDOFF (Friday 16) read-only summary.
- `post-freeze-verification-and-handoff.md` covers *post-freeze* edits
  — late fact-checks, asset corrections, presenter complaints. HANDOFF
  is the no-edit close-out; post-freeze verification is the response
  when something still needs to change after the 15:00 FREEZE.
- `publication-runbook.md` covers the Monday post-show root promotion
  triggered by an APPROVED state. HANDOFF sets up the receipt that
  publication-runbook relies on; it does not run the promotion.
