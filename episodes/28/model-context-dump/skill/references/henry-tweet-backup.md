# Henry tweet backup pipeline (topic source for show prep)

**Canonical data:** `~/weeklyclaw/sources/henry-tweets/`
- `all.jsonl` — append-only canonical store, one tweet object per line
- `YYYY-MM-DD.jsonl` — per-day index files keyed by tweet `createdAt` (UTC)
- `state.json` — `{seen_ids: [...], last_run_utc, last_new_count}` dedup state

**Producer:** Hermes script-only cron `henry-tweets-daily-backup` (job `12c370604fd7`), every 4h, `deliver=local`, silent on success (empty stdout), alerts on failure. Script: `~/.hermes/scripts/henry-tweets-backup.py` — scheduler requires it at that path under `~/.hermes/scripts/`, so the skill never relocates it without updating the cron job too.

## How the script works
1. Runs `BIRD_ACCOUNT=henry ~/clawd/scripts/bird-env.sh user-tweets iAmHenryMascot -n 200 --json`
2. Parses the JSON array with `json.JSONDecoder().raw_decode()` starting at the first `[` in stdout
3. Dedupes against `state.json` seen_ids, appends new rows to `all.jsonl` + the correct day file, updates state
4. Exits 0 with empty stdout when nothing new (silent); prints `henry-tweets-backup FAILED: <reason>` and exits 1 on error

## Bird CLI parsing quirks (learned 2026-08-21)
- bird prefixes info lines (`ℹ️ Looking up...`) before the JSON; strip by finding the first `[`.
- bird can emit trailing content after the array (strict `json.loads` fails with "Extra data"). Always use `raw_decode` and ignore the tail.
- Auth is account-scoped: `BIRD_ACCOUNT=henry` env selects the henry cookie jar. If cookies expire, the script fails loudly — that is the alert path, do not silence it.

## How show prep consumes it
Before scoring candidates, read the last 7 day files. Henry's own posts and quote-commentary are an **editorial priority signal**: any news he tweeted about gets scored as important, ordered by recency and engagement (direct posts/quote-commentary > bare RTs). Staleness check: if `state.json.last_run_utc` is older than 24h, fall back to a live bird scan and record `HENRY_X_PULSE_INCOMPLETE` in `showprep/sources/henry-x-pulse.md` if that also fails.

## Dedup against prior episodes
A topic Henry tweeted about that already aired on a prior episode does not re-qualify unless there is a genuinely new development. Precedent: Qwen3.8-27B (Apache-2.0) aired Episode 25; Qwen3.8-2.4T-A95B (Max-class MoE, custom license) was a distinct new release and qualified for Episode 26 S1. Same-family releases need artifact-level differentiation (size, license, capability), not just a new tweet.

## Deep backfill: the 200-tweet window is only ~6 days (learned 2026-08-21)
At Henry's volume (~35–50 posts/day), one `user-tweets -n 200` call only reaches back ~6 days. Analyzing an episode older than that requires cursor pagination: run `user-tweets ... --json --plain`, parse the `{tweets: [...], nextCursor: ...}` object (an object, not the bare array the cron script sees), then loop with `--cursor <nextCursor>` (sleep ~1.5s between pages, max ~10–12 pages ≈ 1,500 tweets) until the oldest `createdAt` precedes the target window. Merge pages into the canonical store with the same dedup/append recipe as the cron script (append unseen to `all.jsonl` + per-day files, update `state.json.seen_ids`) so the backfill does not desync the cron's seen set. Verified: 589 tweets spanning Aug 4–21 after two cursor pages.

## Verification recipe (after any change to the pipeline)
1. Run the script twice directly: first run may ingest, second run must exit 0 silent (idempotent).
2. Force-run the cron once (`cronjob action=run`) and confirm `last_status=ok`, `last_delivery_error=null`.
3. Check day files exist for each distinct `createdAt` date present in `all.jsonl`.
