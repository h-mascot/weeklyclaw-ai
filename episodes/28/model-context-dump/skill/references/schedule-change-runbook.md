# Show-prep schedule-change runbook (2026-08-20 Thursday move)

Use this whenever Henry or Andy changes WHEN the show-prep pipeline runs
(build day, tick hours, check frequency) — the class of change made on
2026-08-20 when deck production moved from Friday to Thursday with Friday
kept as a light late-news check.

## Why a dedicated runbook

The schedule is enforced in FOUR places plus the cron registry. Changing
only the cron expr produces a pipeline whose gate rejects its own ticks
(or accepts ticks the prompt no longer defines). Every surface must move
together, in one session, with readback.

## The change surfaces (all must agree)

1. **Cron registry** — `cronjob` tool `action=update` with the new
   `schedule` expr. Never hand-edit `~/.hermes/cron/jobs.json` (the show-prep
   prompt itself forbids the cron editing its own definition; the change
   must come from the Ada/control-plane side). Verify with a fresh
   `cronjob action=list` (or a readback of jobs.json): check `schedule`,
   `next_run_at`, `enabled`.
2. **Canonical cron prompt** —
   `~/weeklyclaw/council/current-friday-cron-prompt.md`:
   mission line, DST-SAFE TIME GATE (weekday digits + hour→role map),
   EPISODE DISCOVERY (BUILD-day vs show-day semantics), BREAKING-NEWS
   POLICY, missed-BUILD recovery window.
3. **Skill SKILL.md** — `weeklyclaw-show-prep` "Time gate and roles",
   "Episode discovery and locking" recovery bootstrap, reminder rule.
4. **Support references** — `references/friday-show-prep-control-plane.md`
   (scheduler section + build-day semantics) and
   `references/no-change-refresh-recipe.md` (gate line, reminder slot,
   traps). Grep every reference for stale weekday/hour assumptions after
   the main edits: the no-change recipe's runlog block hard-coded
   `→ 5 HH ... Friday` and would have logged wrong gate evidence forever.

## Semantics that move with the schedule (the subtle part)

- **BUILD-day vs show-day decoupling.** When BUILD runs the day before
  the show, episode discovery must resolve N against TOMORROW's show
  date, not today. The old rule "if an episode is dated for today, resume
  it" silently breaks: on Thursday nothing is dated for today, so the
  naive rule would skip ahead an episode. Encode the target-date rule in
  BOTH the cron prompt's EPISODE DISCOVERY and the skill's episode
  discovery step 1.
- **Reminder slots stay pinned to literal clock hours on show day.**
  The 2 PM ET reminder is a FRIDAY 14:00 concept. After moving BUILD to
  Thursday, "BUILD + 3h = Thursday 14:00" must NOT become a reminder —
  the trap generalizes: pin reminders to (show-day, literal hour), never
  to BUILD-relative offsets.
- **Late-news ticks become additive-first.** Henry's 2026-08-20 framing:
  Friday checks exist to "check if there's any Friday news worth adding
  and adding it". Encode: prefer ADD (new segment, bench promotion, One
  To Watch upgrade) over rewriting the built lineup; replacement still
  needs the >=9.0 / +0.5 bar and explicit re-approval after any host
  approval; never silently swap an approved or pinned story.
- **DST safety.** Keep the UTC-hours superset + `TZ=America/New_York`
  gate pattern; extend the gate's weekday set (e.g. `4|5`), never replace
  the gate with a fixed UTC offset. Validate the expr for BOTH EDT and
  EST mappings (15–21 UTC = 11–17 ET in EDT, 10–16 ET in EST — gate
  rejects the 10 and the 17).
- **"One or two checks" vs hourly default.** Henry may say "one or two
  crons" loosely. Default kept: hourly in-window ticks that are silent on
  no-change (each tick costs one compact `OK ·` line only). Surface the
  knob in the reply rather than pre-trimming: offer the exact reduced
  schedule (e.g. Friday 12:00 + 14:00) if he wants literal two.

## Verification checklist after the change

1. `cronjob action=list` shows the new expr, correct `next_run_at`
   (convert to ET and sanity-check it lands in an intended role slot),
   `enabled: true`.
2. Readback-grep the cron prompt AND skill AND both references for the
   OLD schedule tokens (`* * 5`-style weekday, "Friday 11=BUILD",
   "same-day state") — zero stale hits.
3. Simulate the gate for the next fire time:
   `TZ=America/New_York date -d '<next_run>' '+%u %H'` and confirm the
   weekday/hour pair maps to the intended role in the new prompt text.
4. Confirm the first BUILD tick's target episode exists per the new
   discovery rule (state.json dated for the UPCOMING Friday, not today).

## Editing an inline cron prompt (jobs.json) — the fifth surface

The Friday job delegates to `council/current-friday-cron-prompt.md`, so
editing that file is enough for it. But the daily-intelligence job
(`weeklyclaw-daily-program-intelligence`, `1caf9a7a43fa`) carries its full
prompt INLINE in `~/.hermes/cron/jobs.json` and runs via the no_agent
wrapper (`~/.hermes/scripts/bounded-reasoning-cron.py`), which clones the
job record from `jobs.json` at run time — so a jobs.json edit takes effect
on the next tick with no scheduler restart. When an editorial rule (not a
schedule) must reach a stored prompt, the safe procedure (verified
2026-08-21, airtime news-window rule):

1. Read the job's prompt out of `jobs.json` (stored key is `id`, not
   `job_id`).
2. Patch the text in a temp file FIRST and diff it — a careless
   find/replace can clobber the first half of a neighboring bullet.
3. Back up `jobs.json`, then `json.load` → replace the target job's
   `prompt` → `json.dump(..., indent=2)` → re-load and assert BOTH the new
   rule and a sentinel phrase from an untouched section are present. Never
   string-replace the raw file; `hermes cron` has no show/edit-prompt
   subcommand.
4. Verify `hermes cron list` still renders the job.

Note: hand-editing jobs.json for PROMPT content is fine from the Ada
control-plane side; the "never hand-edit jobs.json" rule above applies to
schedule/definition changes, which go through `cronjob action=update`.

## Recorded instance

2026-08-20: `b75dfa1780c9` moved `0 15-21 * * 5` → `0 15-21 * * 4,5`.
First run same day 15:00 UTC (Thursday 11 ET BUILD) for the Friday
2026-08-21 episode. Edits: cron expr; prompt mission/gate/discovery/
recovery/breaking-news sections; skill time-gate, discovery, reminder
rule; control-plane scheduler + new "Build day semantics" section;
no-change recipe gate line, reminder header, traps. Skill version
bumped 1.7.6 → 1.8.0.
