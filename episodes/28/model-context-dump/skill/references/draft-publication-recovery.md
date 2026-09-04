# Website draft publication: recovery and runtime pitfalls

This is the appendix to `references/website-draft-publication.md`. Read it
when the BUILD passed but `/episodes/<N>/deck`, `/agenda-draft`, or
`/host-cheat-sheet` returns 404 on the first REFRESH after BUILD, or when a
shell-quoting issue blocks the Telegram notification.

## When to use this

The first REFRESH tick after a BUILD that produced a passing package
**must** verify the standing-authorized draft is live BEFORE claiming "no
action":

```bash
for url in /deck /agenda-draft /host-cheat-sheet; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "https://weeklyclaw.ai/episodes/<N>$url")
  if [ "$code" != "200" ]; then missing="$missing $url"; fi
done
```

If any URL is missing, the BUILD skipped the standing-authorized publication.
The seven-artifact gate (`validate_deck.py` + render QA + slide-ID parity +
template-authority comparison) is independent of the website push, so a BUILD
can pass locally without ever touching `weeklyclaw.ai`. Verified on Episode 26
Thursday 12 ET BUILD (rev1 PASS) and Thursday 14 ET REFRESH (repair).

## Recovery recipe (4 steps)

1. **Re-run the standing-authorized publication route** from
   `references/website-draft-publication.md` (worktree → whitelist copy →
   `python3 -B` helper for agenda/host pages → `npm run build` → commit →
   push to `origin/main`). The recovery path is identical to the BUILD path;
   only the trigger is different.

2. **Wait for Vercel deploy to settle.** Poll `curl -s -o /dev/null -w '%{http_code}'
   https://weeklyclaw.ai/episodes/<N>/deck` in a bounded retry loop (4s
   sleep, up to ~10 ticks). Do NOT trust the first 200 if it appears
   immediately — Vercel may serve the previous build for ~10s after push.

3. **Verify with decoded content canaries, not headers alone.** Headers
   alone prove Vercel is up, not that your push landed. Required canaries:
   - Deck: `Episode 26`, `weeklyclaw-logo`, every segment's primary source
     term (Qwen / Faraday / Cerebras / Stripe / AgentCore / Garry Tan).
   - Agenda-draft: show date in long form (`August 21, 2026`), every
     segment headline term.
   - Host-cheat-sheet: at least two story terms + the video title.
   - All referenced assets (`assets/images/...`, `assets/sponsors/...`)
     must return HTTP 200; pick one binary asset and byte/SHA-match it
     against the local rev.

4. **Prove sponsor order with byte offsets.** Sponsor rotation is a weekly
   inversion rule, not a permanent Herald-first layout. On a Herald-first
   week:
   ```bash
   curl -fsS "https://weeklyclaw.ai/episodes/<N>/deck" -o /tmp/deck.html
   herald=$(grep -b -o 'Herald Labs' /tmp/deck.html | head -1 | cut -d: -f1)
   heritage=$(grep -b -o 'Heritage Telecom' /tmp/deck.html | head -1 | cut -d: -f1)
   test "$herald" -lt "$heritage"
   ```
   Mirror the assertion for Heritage-first weeks. Record both offsets in
   `state.json.draft_publication.live_canaries.sponsor_order_check`.

## State and runlog receipts (required)

Update `state.json` with a `draft_publication` block containing:

- `status: "PUBLISHED"`
- `published_at_utc` (ISO with ET offset)
- `tick_id` (e.g., `26-2026-08-21-14`)
- `role: "REFRESH"` when the publication happened on a repair tick
- `trigger` text describing why the BUILD did not publish (so the next
  reader sees the recovery story in one glance)
- `git.commit_sha` and `git.remote_head_after_push`
- `git.staged_files` exact whitelist + `staged_unrelated_count: 0`
- `validator.npm_run_build` PASS output
- `live_canaries` with deck/agenda-draft/host-cheat-sheet URLs, HTTP
  codes, term-match counts, asset HTTP codes, asset SHA-256 match
  booleans, and the sponsor-order check
- `approval_state_after: "UNVALIDATED"` — preserve editorial approval
  state even after the draft is published; "live as draft" and
  "approved" are separate

Append a `## YYYY-MM-DD HH:00 EDT — REFRESH tick (<tick-id>)` block to
`runlog.md` that records the eight required inputs from the skill's
REFRESH-tick template PLUS the recovery narrative.

## `hermes send` dcg gotchas (WeeklyClaw Telegram topic)

Sending the BUILD/REVIEW card to the originating WeeklyClaw Telegram topic
(`-1004370723812:17`) reliably trips `core.filesystem:redirect-truncate-root-home`
with two patterns, even when no actual file redirect exists:

1. Trailing shell syntax inside the same argument string (`... 2>&1`,
   `... | tail -10`, `... > /tmp/foo`). The dcg rule sees the redirect
   token and refuses.
2. Three-character ellipsis `...` anywhere in `--body`. The dcg rule
   treats `...` as a glob/redirect and blocks the send.

Workaround for both: write the body to a temp file with `write_file`, then
send via the `--file` form. The `--file` path is the only safe route for
multi-line WeeklyClaw review cards containing the exact
`APPROVE` / `SWAP` / `DROP` / `PIN` / `ORDER` command list.

```bash
# 1) write body to /tmp/weeklyclaw-ep26-draft-notice.txt with write_file
# 2) send via:
hermes send --to telegram:-1004370723812:17 \
  --subject "Weekly Claw Episode 26 — DRAFT LIVE on weeklyclaw.ai" \
  --file /tmp/weeklyclaw-ep26-draft-notice.txt
# exit 0 = sent
```

Verified on Episode 26: both `--body "..." 2>&1` forms were BLOCKED; the
`--file` form returned `sent`. Do not retry the `--body` form repeatedly;
it will not pass.

## Reminder rule (no change)

This appendix does NOT change the 2 PM ET reminder rule. The reminder slot
is **Friday 14:00 ET only**, not BUILD-relative. Thursday REFRESH ticks
never send the broadcast reminder regardless of approval state. Verified
on Episode 26 Thursday 14 ET — no reminder posted.

## See also

- `references/website-draft-publication.md` — the canonical BUILD-time
  publication recipe (worktree creation, whitelist copy, agenda/host page
  generation, `npm run build`, push, canary verification).
- `references/no-change-refresh-recipe.md` — the OK no-action wire
  output contract for clean ticks; the recovery flow above deliberately
  deviates from "no action" because the standing-authorized draft is
  missing.