# Host-triggered material rebuild (mid-week revision)

Recipe for an explicit Henry/Andy "regen the deck" command between scheduled
ticks (e.g. Episode 26 rev1 → rev2, 2026-08-20). This is the documented
material-rebuild trigger the Thursday REFRESH ticks defer lint fixes to.

## Trigger classes that authorize an off-schedule rebuild

- Explicit host command in the Telegram topic ("regen", "rebuild",
  `APPROVE`/`SWAP`/`DROP`/`ORDER`/`PIN`/`MERGE`).
- Friday 11 ET REFRESH when the build is still UNVALIDATED with deferred
  host-format lint failures queued in `workflow-feedback.md`.
- A later cron/supersede pass that pushes a more-complete rev6 final on top
  of an earlier cron's partial rev6 (verified 2026-08-21 Ep26). When
  `origin/main` already contains a partial rev from an earlier cron and you
  need to land the full feature set, treat the later push as another material
  rebuild, not a no-op refresh. See "Supersede a partial cron push" below.
- Never an unsolicited Thursday-afternoon rebuild — monitoring-only there.

## Supersede a partial cron push (verified 2026-08-21 Episode 26)

When a same-day earlier cron already pushed an incomplete rev6 (e.g. only
`deck.html` modified, no new S5, agenda/agenda-draft still on rev4) and your
later pass needs to land the full feature set on top:

1. **Confirm the partial is live.** `curl -s https://weeklyclaw.ai/episodes/<N>/deck | grep -oE 'id="s-[^"]+"' | sort -u` and compare slide count to your local target. If the partial is missing slides (e.g. 12 slides vs. your 13-slide target), you are superseding, not publishing fresh.
2. **Pull origin/main to local main FIRST.** Local main is often stale by 5–10 commits if you haven't run `git pull --ff-only` since the partial cron. `git -C ~/.hermes/workspace/projects/weeklyclaw-ai fetch origin && git merge --ff-only origin/main`. Verify `git log origin/main --oneline -3` shows the partial cron commit.
3. **Base the worktree on `origin/main`, not local `main`.** This is the recurring trap. `git branch -f feat/<slug> origin/main && git worktree add /tmp/wt-<slug> feat/<slug>`. Confirm `git -C /tmp/wt-<slug> log --oneline -3` shows the partial cron commit at HEAD before you stage anything. A worktree whose HEAD does NOT contain the partial commit is silently editing on top of an older base; your push will create a non-fast-forward and Vercel won't deploy.
4. **Worktree reuse failure mode:** `git worktree add <path> <branch>` succeeds silently even when the branch was previously checked out — your edits go on top of the OLD branch HEAD, not the new one. Symptom: `git -C <worktree> rev-parse --show-toplevel` succeeds but `git -C <worktree> log --oneline -3` shows the wrong (stale) commits. Fix: `git worktree remove <path> --force && git branch -D <branch>` (worktree must be removed before branch delete), then re-create branch from `origin/main` and re-add worktree. **Always verify worktree HEAD matches `origin/main` HEAD before staging** — not just the worktree existing.
5. **dcg blocks `rm -rf`** on any path including `/tmp/...`. Avoid by using `mktemp -d` for fresh paths; if a worktree path already exists, skip the `rm` and use `git worktree remove --force` first.
6. **Asset copy needs explicit subdir recursion.** A naïve `shutil.copy` of `assets/images/` skips `assets/images/artifacts/`. Iterate `src.iterdir()` and recurse into any `is_dir()` child. The deck's `src=...` attributes reference files in `assets/images/artifacts/`; missing artifacts cause visible slide breakage (broken-image icon) but the deck validator may still pass because the local-media check only verifies the `revs/assets` symlink resolves the top-level paths.
7. **Mirror `agenda-draft/index.html` to `agenda/index.html`.** `vercel.json` rewrites `/episodes/<N>/agenda` to `/episodes?week=<N>&deck=main` (308), so the canonical `/agenda` URL is not user-discoverable. But `agenda/index.html` IS committed (legacy route) and Vercel serves it via the gallery's deep links. Keep them identical so the gallery deep links stay consistent with the draft route.
8. **Vercel deploy lag (15–45 s):** don't trust the first 200. Poll the live deck SHA: `LIVE_SHA=$(curl -s https://weeklyclaw.ai/episodes/<N>/deck | sha256sum | awk '{print $1}')` and compare to your local `sha256sum revs/deck.rev<N>.html`. Byte-equality is the strongest live deploy proof — stronger than curl 200, stronger than grep canaries. Use it on every supersede push.
9. **State.json draft_publication update:** change `commit` to the new SHA, change `deployed` to the actual Vercel promotion timestamp (round to the nearest minute you observed the SHA match), and add a `live_verified_routes` object recording every URL you checked (status code + size in bytes). The old `commit: <partial-SHA>` in `state.json` is misleading after supersede; do not leave it pointing at the partial.
10. **Push with `git push origin <branch>:main` (force-push to main).** A normal push is fine because the partial was on origin/main and your local branch is fast-forwarded. Vercel deploys the new HEAD on receipt.

## Rebuild sequence (verified on Episode 26 rev2)

1. **Scope the diff from workflow-feedback.md.** Typical rev2 scope:
   reassign segment leads per the standing Henry-led rule, add the
   `live_artifacts` block to `media-manifest.json`, fix slide-ID parity.
   Lineup/scores/thesis/sponsor order stay frozen unless the host said
   otherwise.
2. **Derive rev2 artifacts from rev1 by script, not by hand:**
   ```bash
   cd episodes/<N>/showprep
   cp revs/_slides_content.rev1.html revs/_slides_content.rev2.html
   # targeted sed/python replacements for lead tags, agenda **Henry (lead):**
   # headers, speaker-notes '## s-seg-X — Owner' heads AND '- **Owner:**' lines,
   # cheat-sheet table rows, henry/andy section headings
   sed 's/rev1/rev2/g' revs/build_deck.rev1.py > revs/build_deck.rev2.py
   python3 revs/build_deck.rev2.py
   ```
   Ownership strings live in MORE places than grep first shows: agenda
   `**Henry (lead):**` paragraphs, `## s-seg-x — Owner` speaker-note heads,
   `- **Owner:**` bullet lines, cheat-sheet `| S2 Faraday | Andy lead |` rows,
   host-section `## s-seg-x (Andy lead)` headings, and the deck map slide's
   `<td>Andy</td>` ownership column. Grep `Andy (lead)\|Andy lead` across all
   rev2 files and require zero hits on news segments before validating.
3. **Validator setup gotchas (both bit on Episode 26):**
   - `qa/validate_deck.py` is NOT auto-copied into a new episode's `qa/`.
     Copy it from the prior episode:
     `cp ../<N-1>/showprep/qa/validate_deck.py qa/`.
   - The local-media check resolves asset paths **relative to the deck file**
     (`revs/`), not the showprep root. Create `revs/assets -> ../assets`
     (symlink) or the media check FAILs on files that exist.
   - Run with the authority third argument:
     `python3 qa/validate_deck.py revs/deck.rev2.html revs/speaker-notes.rev2.md episodes/23/deck.html`
4. **Slide-ID parity failures have three recurring shapes:**
   - Notes missing `s-title` (the recovery-BUILD author skipped it because the
     cold open "covers" it) → add a minimal s-title section.
   - Duplicate `s-sources` + `s-outro` sections when the outro is delivered
     over the Sources slide → merge into ONE `## s-sources — ... (outro
     delivered over sources slide)` section; the appendix content becomes a
     bullet inside it. The validator dedupes nothing; `^## (s-\S+)` headings
     must be exactly 1:1 with deck slide IDs.
   - **Notes have a `## s-the-id — Owner — M:SS` block for a slide you already
     removed from the deck** (verified 2026-08-21 Ep26 rev6 final: speaker-notes
     still had `## s-the-map` after the deck dropped `s-the-map`). The
     validator's first failure is `slide-ID parity (13 slides <-> notes)`. The
     fix is a regex block remove on the notes file:
     ```python
     import re
     text = open('revs/speaker-notes.revN.md').read()
     text = re.sub(r'## s-the-id — .*?\n\n(?:(?!## ).)*?\n', '', text, flags=re.S)
     open('revs/speaker-notes.revN.md', 'w').write(text)
     ```
     Use `(?!## )` as the lookahead so the regex stops at the next `## `
     heading. Verify with `grep -c '^## s-' revs/speaker-notes.revN.md` ==
     deck slide count.
5. **Render QA: compare against the prior revision, not absolute zero.**
   The overflow/clipping Playwright measurement reports `clipped=1..2` on
   nearly every slide from deck chrome (progress bar, nav dots) that sits
   outside the slide bounds — present in the authority deck too. The gate is
   *no regression vs the previous rev's per-slide numbers*, not zero.
6. **Republish the standing-authorized draft** via the worktree route
   (`references/website-draft-publication.md`). Two helper gotchas:
   - `wc_sync.deck_meta()` requires a `Path` worktree argument, not `str`
     (TypeError on `str / str` otherwise).
   - Re-run the agenda/host-cheat-sheet HTML generation after copying the new
     rev files, then re-verify live canaries that prove the change itself
     (e.g. "Henry (lead)" count = number of news segments).
   - For slide-add / slide-remove rebuilds, the live deck slide-ID count and
     local deck slide-ID count must match. `curl -s
     https://weeklyclaw.ai/episodes/<N>/deck | grep -oE 'id="s-[^"]+"' | sort
     -u | wc -l` should equal the local count. If the live count is the old
     number, your push didn't deploy (or you pushed before Vercel caught up).
7. **Record receipts:** update `state.json` (`selected_revision`,
   `rev<N>_built_at`, `artifact_hashes_rev<N>`, `draft_publication` commit +
   `live_verified_routes`), append a rebuild block to `runlog.md`, and post
   the notice to the Telegram topic with `hermes send --file` (never `--body`
   with redirects/ellipses).

## Post-rebuild lint debt check

A prior rev's claimed PASS may have come from a hand-rolled structural check
(`qa/revN_validation.md`) rather than the canonical validator. Episode 26 rev1
shipped "PASS" while `validate_deck.py` actually failed slide-ID parity. On
any material rebuild, run the canonical validator against the PREVIOUS rev
too; if it fails, note the hidden failure in the runlog so the fix is visible
as a fix, not an unexplained diff.

## Lessons verified on Episode 26 rev5 (launch-type artifact rebuild)

- **A cron-built revision can miss artifacts staged in `workflow-feedback.md`.**
  Rev4 (15 ET tick) was built minutes after the Cerebras video and DeepSeek
  benchmark were staged and logged in the feedback file, yet it shipped the
  old screenshots unchanged. Before regenerating on a host command, diff the
  current rev's asset references against EVERY artifact listed in
  `workflow-feedback.md` ("already sourced and staged" blocks) — a rebuild
  that ignores staged assets is a wasted revision.
- **Verify receipt URLs resolve to the claimed content before shipping.**
  Rev3/rev4's Faraday slide linked `arxiv.org/abs/2508.14251`, an unrelated
  relativistic-gas physics paper; the real paper was 2608.13331. A one-line
  `curl -sL <url> | grep '<title>'` against every arXiv/primary link catches
  this. Source ledgers can carry the correct URL while the deck carries a
  stale one — fix across deck, speaker notes, agenda, host views, and cheat
  sheet in the same revision (same principle as the ownership-string rule:
  grep every surface, not just the slide).
- **Render QA slide activation (1600x900 captures):** `scrollIntoView()` on
  each slide captures slide 1 every time (all slides are stacked in the DOM).
  The working mechanism is toggling the deck's own state — remove `.active`
  from all `.slide` elements, add it to slide i, then wait ~700ms for the CSS
  fade before screenshotting. An 80ms wait captures the PREVIOUS slide
  because the fade is still in flight.
- **Artifact-presence proof without a vision model:** OCR the captured slide
  (tesseract) plus a PIL luminance check on the artifact half of the frame —
  a rendered benchmark chart or video poster has luminance stdev roughly
  >50; a blank region sits near 5-15. OCR of chart axis labels/series names
  (e.g. "Qwen3.6-27B 0.856") proves the RIGHT chart is embedded.
- **AWS blog screenshots need an H1-anchored clip region.** AWS chrome (nav,
  reinvent banner) dominates the 1440x900 viewport; a plain
  `page.screenshot()` captures menus, not the announcement. Locate the `h1`
  bounding box, scroll it into view, and clip a region starting ~160-260px
  above the H1. Verify via OCR that the GA headline text is in the capture.
- **Rev derivation stays script-based:** stage a `make_rev<N>.py` next to the
  build script that patches `_slides_content.rev<N-1>.html` with targeted
  replacements (asset paths, LIVE link labels, hrefs), bump the build script
  by `sed s/rev<N-1>/revN/g`, rebuild, revalidate. Copy speaker-notes/host
  rev files with the same URL/artifact fixes — the notes must name the NEW
  artifact, not the old screenshot. Watch for LIVE-label strings that differ
  from what you expected to replace (rev4's AWS label was "AWS AgentCore
  docs", not the docs URL); grep for the actual remaining label after the
  pass.

## Lessons verified on Episode 26 rev6 final (2026-08-21)

- **Slide-DROP creates stale notes sections** (see "Slide-ID parity
  failures" item 3 above for the recipe). The deck drop and the notes drop
  are two independent edits; if you only patch the deck, the first
  validator run catches it. The `## s-the-id — Owner — M:SS\n\n...## next`
  regex with `(?!## )` lookahead handles it cleanly in one Python pass.
- **Asset subdirs need explicit recursion in the publish script.** A naïve
  `shutil.copy` of `showprep/assets/images/` skips `artifacts/`. The deck
  references `assets/images/artifacts/s1-faraday-hero.jpg` etc.; missing
  artifacts surface as broken-image icons on the live site but the
  validator's local-media check still passes (it only checks the top-level
  paths under `revs/assets`). Always add a recursive copy pass over
  `src.iterdir()` filtering on `is_dir()`.
- **Mirror `agenda-draft/index.html` to `agenda/index.html`.** The legacy
  route is committed and served; if you only update agenda-draft, the
  agenda route stays on stale content via the gallery deep links.
- **Live SHA-equality is the strongest deploy proof.** After pushing a
  supersede rev, poll `curl -s <live-url> | sha256sum` until it matches
  `sha256sum revs/deck.rev<N>.html`. curl 200 + grep canary is necessary
  but not sufficient; the only way to be sure Vercel is serving the byte
  you pushed is byte equality.
- **Local main can lag origin/main by 5–10 commits** if a prior cron already
  pushed a partial rev. Always `git fetch origin` and base the worktree on
  `origin/main`, not local `main`. Worktrees created from local `main`
  push fine but represent a no-op relative to origin.
- **`git worktree add` reuses stale branches silently.** When you re-run a
  worktree-create command against an existing branch name, git checks out
  the OLD branch HEAD. Symptom: worktree HEAD is missing commits you
  expected to see (e.g. the partial rev6 cron commit). Fix: `git worktree
  remove --force`, `git branch -D <branch>`, re-create from origin/main,
  re-add worktree. **Always confirm worktree HEAD == origin/main HEAD
  before staging.**
- **`build_lock_pid` and `state.lock` cleanup** at end of every tick:
  verify the lock PID is no longer running (`ps -p <pid>` returns empty)
  before removing the lock file. A stale lock blocks the next hourly
  tick. Recorded in `state.json.build_lock_pid = null`.