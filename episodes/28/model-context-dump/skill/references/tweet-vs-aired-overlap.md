# Tweet-vs-aired overlap analysis (Henry's X pulse vs actual show)

Use when Henry asks to compare his tweets against what actually aired on an episode — the editorial ground truth is the **aired YouTube transcript**, never the deck, agenda, or candidate files (agenda rev1 ≠ final deck rev ≠ what aired; see `references/aired-video-comparison.md` for the same principle on the visual side).

Also use this pipeline when Henry asks for a **proposed weekly lineup from his tweets**. Two rules govern lineup proposals (both Henry corrections, 2026-08-21):

- **News-grade filter:** "The idea is not to use all tweets but only breaking news topics for the week." Extract launch-grade news only (new model/chip/product releases, first-ever facts, confirmed deals). Tweet volume is NOT a selection signal — Qwen3.8-27B, Grok Bot, GLM-5.3, and Ultrafast were all excluded from Episode 26 despite 20–50 tweets each because their launches were Ep25-window news. Opinion threads (e.g. Anthropic criticism) are not launches. Henry's first-hand lived material (local benchmarks, DGX/M5 tok/s results, harness setups) is Henry-section content, not a news segment.
- **Episode news window = previous episode AIRTIME.** A story qualifies for episode N only if its launch receipt landed after episode N-1 aired (Friday 16:00 ET / 20:00 UTC) — not after the last daily-intake completion, which finishes pre-show. Burned example: Qwen3.8-2.4T-A95B posted Aug 14 15:02 UTC, ~5h before Episode 25 aired, and was wrongly slotted as Episode 26's S1 lead until Henry asked "did anything happen on it this week?" — it hadn't; only follow-on community quants.

## Pipeline (verified 2026-08-21 on Episodes 24/25)

1. **Find the aired video.** `yt-dlp 'ytsearch20:Weekly Claw Episode <N>' --flat-playlist --print '%(id)s\t%(title)s\t%(channel)s'` and confirm the channel "Weeklyclaw" (channel id `UCa0Mxn9vyx6NnU-aBgRcRvg`; listing `/videos` is the reliable route). Beware: episode numbering on YouTube titles may not match internal episode numbers — the "Episode 25" search result `54jD7eZmIYg` was actually the Aug 14 show; cross-check upload date and chapter list against `showprep/state.json` `show_date_ny`.
2. **Get the transcript.** `~/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py <id> --timestamps` → JSON with `timestamped_text`. Auto-captions only; **garbled terms are guaranteed**: "queen"=Qwen, "Kimmy"=Kimi, "Glockbot"/"Glock bot"=Grok Bot, "deep sw"=DeepSeek, "Glock"=Grok. Topic regexes must include the garble variants or mentions undercount to zero.
3. **Build the tweet window.** Episode N's window = [prior episode's show date, this show date), both at 20:00 UTC (16:00 ET Friday). Pull from `~/weeklyclaw/sources/henry-tweets/all.jsonl`; if the window predates the backup's coverage, run the deep backfill pagination first (see `references/henry-tweet-backup.md` § Deep backfill).
4. **Topic matrix.** Define ~20 topics from the episode's `candidates.md`/`sources/` plus anticipated misses; count (a) tweets matching each topic regex (include quoted-tweet text — RTs carry the signal too), (b) transcript mentions. Flag both directions: `tweets ≥3 & show = 0` (tweeted, not aired) and `show ≥3 & tweets = 0` (aired, not tweeted).
5. **Engagement layer.** Sort original posts (non-`RT @`) by likes+RTs to find Henry's top-engaged originals; a top-engaged original with no segment is the strongest miss signal.
6. **Report shape:** compact `topic / tweets / show-mentions` matrix, then findings ranked: biggest misses (Henry-owned signal that got no airtime), reverse gaps (show-only topics, i.e. Ada/Andy-sourced), and lean-direction mismatches (show leaned harder than the feed did).

## Verified findings (Ep24/Ep25, 2026-08-21)
- Core overlap is strong and bidirectional — every major segment maps to same-week heavy tweeting.
- **Ep25 biggest miss: Grok Bot** — 36 tweets including Henry's top-engaged original of the whole period (76 likes), one passing show mention.
- **Second miss: Gemini 3.7 Flash** — 9 tweets, zero coverage.
- Reverse gaps (show-only): WeatherNext + YC QM (Ep24), Writer (Ep25) — came from candidate/host-resources, not the feed.
- Ep24 show leaned harder than the feed on AMD/Taalas (12 vs 1) and Cloudflare OS (7 vs 1).

## Follow-up
Henry approved wiring a **coverage-gap step** into Friday prep (2026-08-21): before FREEZE, run the tweet-vs-lineup match for the episode window. Any breaking-news topic with ≥5 tweets (originals weighted over RTs) and zero segment presence gets flagged in the FREEZE message as a coverage gap for host decision — flagged, not auto-added. Ep25 burn case: Grok Bot had 36 tweets and got one passing mention. Guard: tweet volume alone never qualifies a topic — apply the news-window and launch filters first, and keep Henry's lived material in the Henry section, not the news rundown.

## Pitfalls
- Do not use the deck or agenda as "what aired" — use the transcript.
- Do not count bare regex hits as segment coverage; read surrounding context ("Kimmy" appears inside a DeepSeek comparison, Grok Bot got one passing mention at 26:47).
- `x_search` tool may be out of credits — the whole pipeline runs on local backup + yt-dlp, no X API needed.
