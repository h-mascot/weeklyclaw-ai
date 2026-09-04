# WeeklyClaw website draft publication route

How to publish a draft deck to weeklyclaw.ai during BUILD, and how the
full listing works on APPROVE.

## Repositories

- **Website repo:** `~/clawd/projects/weeklyclaw-ai`
- **Remote:** `https://github.com/h-mascot/weeklyclaw-ai.git` (branch `main`)
- **Hosting:** Vercel, auto-deploys on push to main
- **Workspace archive (showprep source):** `~/weeklyclaw`

## Draft publication (BUILD tick, standing authority)

On every BUILD that produces a passing seven-artifact package:

1. Create a clean git worktree off `origin/main` with a unique branch:
   ```bash
   repo=~/clawd/projects/weeklyclaw-ai
   git -C "$repo" fetch origin
   worktree=$(mktemp -d /tmp/weeklyclaw-draft-publish-XXXXXX)
   branch="ada/draft-publication-$(date +%s)"
   git -C "$repo" worktree add -b "$branch" "$worktree" origin/main
   test "$(git -C "$worktree" rev-parse --show-toplevel)" = "$worktree"
   ```
   Keep using `git -C "$worktree"` for every build-adjacent git command. Do not rely on the tool call's `workdir` or on a shell variable that is never used by later commands. A clean worktree does nothing if `npm` and `git` still run in the dirty canonical checkout.

2. Copy only the selected revision artifacts into `episodes/<N>/`:
   - `deck.rev<N>.html` → `episodes/<N>/deck.html`
   - `agenda.rev<N>.md` → `episodes/<N>/agenda.md`
   - `henry-section.rev<N>.md` → `episodes/<N>/henry-talking-points.md`
   - `host-cheat-sheet.rev<N>.md` → `episodes/<N>/host-cheat-sheet.md`
   - only assets referenced by the public deck/host pages → `episodes/<N>/assets/`

   Never copy or stage `showprep/`, QA renders, source ledgers, state locks, or unrelated intake files. Stage an explicit whitelist, not `git add episodes/<N>/`.

3. Generate the agenda and host HTML pages using the sync script's helpers, then duplicate the generated agenda page to the non-redirected draft route. Run the helper with `python3 -B` (or `PYTHONDONTWRITEBYTECODE=1`) so importing the sync module does not leave an untracked `scripts/__pycache__/` that blocks clean worktree removal:
   ```python
   # Invoke this helper as: python3 -B <helper-script.py>
   import importlib.util
   from pathlib import Path
   spec = importlib.util.spec_from_file_location("wc_sync", "<worktree>/scripts/sync-weeklyclaw-archive.py")
   wc_sync = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(wc_sync)
   meta = wc_sync.deck_meta("<worktree>", <N>)
   wc_sync.write_agenda_html("<worktree>", <N>, meta)
   wc_sync.write_markdown_page("<worktree>", <N>, "host-cheat-sheet.md", "host-cheat-sheet", "Host Cheat Sheet", meta)
   episode = Path("<worktree>") / "episodes" / str(<N>)
   direct = episode / "agenda-draft"
   direct.mkdir(exist_ok=True)
   (direct / "index.html").write_bytes((episode / "agenda" / "index.html").read_bytes())
   ```

   `/episodes/<N>/agenda` is intentionally redirected to `/episodes?week=<N>&deck=main`. An unapproved draft is absent from the gallery, so that redirect is not a usable draft-agenda handoff. Use `/episodes/<N>/agenda-draft` until approval.

4. Validate, assert repository identity again, stage exact paths, and push:
   ```bash
   (cd "$worktree" && npm run build)
   test "$(git -C "$worktree" rev-parse --show-toplevel)" = "$worktree"
   git -C "$worktree" add \
     "episodes/<N>/deck.html" \
     "episodes/<N>/agenda.md" \
     "episodes/<N>/agenda/index.html" \
     "episodes/<N>/agenda-draft/index.html" \
     "episodes/<N>/henry-talking-points.md" \
     "episodes/<N>/host-cheat-sheet.md" \
     "episodes/<N>/host-cheat-sheet/index.html" \
     "episodes/<N>/assets/<exact-referenced-asset-1>" \
     "episodes/<N>/assets/<exact-referenced-asset-2>"
   git -C "$worktree" diff --cached --name-only
   git -C "$worktree" commit -m "feat: publish Weekly Claw episode <N> draft deck and agenda"
   git -C "$worktree" push origin HEAD:main
   ```
   Inspect the staged-name list before commit. It must contain only the intended public episode packet. On a repeat draft publication, files already identical to `origin/main` will not appear in the staged list; that is expected. Require the changed-file set to be a subset of the whitelist, not an exact match to every copied path.

5. Verify live after Vercel deploy, using decoded content canaries rather than headers alone:
   ```bash
   curl -fsS "https://weeklyclaw.ai/episodes/<N>/deck" | grep '<episode-specific-canary>'
   curl -fsS "https://weeklyclaw.ai/episodes/<N>/agenda-draft" | grep '<agenda-specific-canary>'
   curl -fsS "https://weeklyclaw.ai/episodes/<N>/host-cheat-sheet" | grep '<host-doc-canary>'
   curl -fsS "https://weeklyclaw.ai/episodes/<N>/assets/<asset>" -o /tmp/weeklyclaw-live-asset
   sha256sum /tmp/weeklyclaw-live-asset "<local-asset>"
   ```
   Poll with a bounded retry loop while Vercel deploys; do not treat the first stale response as final. Choose canaries that prove the material correction itself, not generic episode text. For changed binary assets, require matching byte length and SHA-256. For ordered edits such as sponsor rotation, verify both sponsor canaries and assert that the first sponsor's byte/DOM position precedes the second sponsor's position on the deck, agenda, and host cheat sheet.

6. Prove `origin/main` points to the pushed commit, sync the canonical checkout only if doing so preserves its unrelated dirty state, then remove the temporary worktree. Never reset or clean the canonical checkout as part of draft publication. A helper import should not create bytecode when step 3 uses `python3 -B`; if any generated untracked file still appears, inspect it before cleanup. Remove only the temporary worktree and its temporary branch. Report the canonical checkout's pre-existing dirty state as preserved, not as publication drift.

7. Include all three mobile-friendly links in the BUILD message:
   - `https://weeklyclaw.ai/episodes/<N>/deck`
   - `https://weeklyclaw.ai/episodes/<N>/agenda-draft`
   - `https://weeklyclaw.ai/episodes/<N>/host-cheat-sheet`

## What NOT to touch during draft publication

- **`episodes/index.html`** — the episode gallery. Adding a card here
  without updating the homepage breaks `validate.mjs` (see below).
- **`index.html`** — the homepage. The featured episode and archive grid
  are updated atomically by the sync script on APPROVE.
- **`scripts/validate.mjs`** — the validator. The sync script updates it
  on full publication.

Draft publication is deck + assets + agenda pages only. The gallery and
homepage listing is the approval-to-publication step.

## Validator constraints (validate.mjs)

The site's `npm run build` runs `scripts/validate.mjs`, which enforces:

1. **Homepage/gallery consistency:** the homepage's newest 6
   `episode-week` spans must match the episodes gallery's newest 6
   `week-number` spans (sorted descending). Adding a card to one without
   the other fails the build.

2. **Required files:** specific deck/agenda paths per episode are
   hardcoded. New episodes must be added to the `required` array (the
   sync script does this via `update_validate()`).

3. **Content canaries:** homepage must contain specific copy strings
   (titles, sponsor names, links). Gallery must contain specific YouTube
   video IDs for episodes with published videos.

4. **No public `.html` URLs:** pages must not expose `.html` extensions
   in href/src/action/data-url attributes (clean URLs only).

5. **No forbidden nav items:** desktop/mobile/footer nav must not contain
   newsletter, X, YouTube, or other removed links.

6. **Deck sanity:** every episode deck must contain "Weekly" or "OpenClaw".

## Full publication (APPROVE trigger)

On Henry/Andy APPROVE, the publication runbook
(`references/publication-runbook.md`) takes over. The sync script
(`scripts/sync-weeklyclaw-archive.py`) handles:

- Copying all episode files from the workspace archive into the repo
- `update_homepage()` — updates featured episode number, title, date,
  description, CTA, and archive grid card
- `update_episodes_index()` — updates the gallery card, archive count,
  and YouTube video wiring
- `update_validate()` — adds the new episode to the required-files list
  and updates canary references
- Downloading YouTube thumbnails for published videos
- Writing agenda and host-cheat-sheet HTML pages

Run it with:
```bash
python3 scripts/sync-weeklyclaw-archive.py --commit --push
```

The sync script is the atomic path: it updates gallery + homepage +
validator together, so the build passes on first try.

## Vercel clean URL behavior

`vercel.json` has `"cleanUrls": true`, so:
- `/episodes/24/deck.html` redirects (308) to `/episodes/24/deck`
- The clean URL is the canonical public URL
- Always verify using the clean URL, not the `.html` extension

## Vercel redirects

- `/discord` → Discord invite
- `/weeklyclaw-archive` → `/episodes`
- `/episodes/:N/agenda` and `/episodes/:N/agenda.md` → `/episodes?week=:N&deck=main`
- Because draft episodes are deliberately absent from the gallery until approval, `/episodes/:N/agenda` can return 200 after redirect while still failing the user's agenda-discovery need. Publish and verify `/episodes/:N/agenda-draft` as the direct review route; retire or stop advertising it after the approved episode enters the gallery.
