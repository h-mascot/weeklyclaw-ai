# WeeklyClaw x-news-drafts cron notes

Captured from live runs of `x-news-drafts` (`8db1b4ad59f7`). Most recent update: 2026-08-08.

These notes are written for the show-prep skill because both collectors operate in the same WeeklyClaw pipeline, share the same Typefully social_set_id (`322715`), and the same media-guard invariants.

## What the x-news-drafts cron does

Every ~12h: scan AI news from Hacker News, TechCrunch AI, The Verge AI, Ars Technica, credible X sources, and primary lab blogs. Filter to genuinely newsworthy items not already in the Typefully draft queue or recently published. Draft main-post + source-link reply in Henry's voice. Save to Typefully as `draft` (no `publish_at`); the separate review-and-publish gate handles cadence.

## Typefully v2 API gotchas (verified)

- `?status=draft` (singular). `?status=drafts` returns 422 — `Input should be 'draft', 'published', 'scheduled', 'planned', 'error' or 'publishing'`.
- `limit` max is 50; higher returns 422.
- List response is `{count, limit, offset, next, previous, results}`. Iterate `.results[]`.
- For queue dedup scanning, the `preview` field on list responses is the first post text. Avoid N+1 GETs unless you need full `posts[]` or `media_ids`.
- **Bulk list endpoint strips `posts[].text` per item** (verified 2026-08-08): `jq '.results[].platforms.x.posts[0].text'` returns empty strings for every draft, even drafts whose individual GET returns full text. Workaround: use `.preview` for dedup scans, or fetch individual drafts only when you need full text. Don't waste time debugging jq paths that work on individual GETs — it's a list-endpoint quirk, not a path bug.
- Publishing a multi-post X draft where a reply contains an outbound URL can return HTTP 403 with body "This is not allowed by X policy. Direct publishing of X drafts containing URLs is blocked." Staging (no `publish_at`) is fine; the 403 only fires on publish-time. The separate review-and-publish cron must schedule with a future ISO timestamp (verified workaround in the show-prep skill's "Pre-show community promo" section), not `publish_at: "now"`.
- The original welcome draft (`id=10063353`) lives in the queue from onboarding. It contains "Hey, this is a sample draft..." text and a static image. The media guard accepts it because the image is not the canonical WeeklyClaw logo.

## Media guard

```bash
python3 ~/.hermes/scripts/weeklyclaw_media_guard.py --apply --draft-id <TYPEFULLY_DRAFT_ID>
```

Compares filenames AND image pixels against the canonical WeeklyClaw logo. Exit 0 = clean, exit non-zero = violation unrepaired or API failure. Always run immediately after each new POST, before any review/scheduling pass. Text-only drafts pass with `violation_count: 0, repaired_count: 0` — that's the expected clean result.

## Working non-Polymarket news sources (Aug 2026)

- Yahoo Finance mirrors Bloomberg paywalled articles publicly. Use the Yahoo URL as the public attribution when the Bloomberg original is paywalled.
- `liquid.ai/blog` — first-party source for Liquid AI model releases. Direct, reliable.
- Hacker News front-page — community-trending model launches; cross-reference with the lab's own announcement before drafting.
- HN Algolia API for research: `https://hn.algolia.com/api/v1/search_by_date?query=AI&tags=story&hitsPerPage=20&numericFilters=created_at_i>{SINCE_UNIX}` for the last-N-hours window, and `https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30` for HN front-page context. Object IDs from search → fetch full item via `https://hn.algolia.com/api/v1/items/{id}`.
- IEEE Spectrum, Roland Berger, ComputeForecast — credible for AI infrastructure and data center power stories. Use as corroboration, not primary.

## Scraping fallbacks when firecrawl/web_extract is blocked

Verified 2026-08-08: web_extract (firecrawl-backed) returned `Payment Required: Failed to scrape. Insufficient credits` on both `x.ai/news/...` and `linuxfoundation.org/press/...`. Cloudflare also blocked `curl` with default UA and chrome-127 UA to x.ai — same protection. **Do not waste retries on these sources during a cron run.** Instead: use HN Algolia to confirm the launch (search `Grok+Imagine+Image`, `Tokenomics+Foundation`, etc. — HN title + URL is enough evidence for a draft), use the source's OG metadata via the official HN submission URL as the secondary link in the reply, and stage the draft. Full source-text retrieval can happen during the review-and-publish gate if needed.

## Gap-priority override

Before drafting generic news, read `~/weeklyclaw/state/gaps.json`. If a gap has `suggested_actions` like `DRAFT_EPISODE_X_POST`, prioritize closing that gap first — it's already known and will otherwise sit unaddressed.

Known gap types:

- `EPISODE_X_PROMO_MISSING` — episode live on YouTube N days, zero X posts reference it.
- `WEBSITE_STALE` — website shows older episode as latest vs YouTube.

## Dedup against combined queue

The Polymarket collector and the x-news-drafts cron both write to the same Typefully social_set_id. A story sourced from a Polymarket tweet may also surface in Hacker News the same day. To avoid double-posting, scan the full draft queue (status=`draft` and recent `published`) for topic overlap, not just your own cron's state file.

**Polymarket-collector coordination rule (verified 2026-08-08):** the polymarket collector's `state/polymarket-collector.json` `processed_tweet_ids` covers every Polymarket @Polymarket tweet — including ones that never became a draft (rate cap of 3/run). When drafting a non-Polymarket story, check the recent Polymarket scrape (`~/clawd/scripts/bird-env.sh user-tweets Polymarket -n 100 --plain`) and grep for AI keywords to confirm the story isn't a Polymarket-originated duplicate. If the Polymarket collector already covered it as a "% chance" market, do not draft the HN/TechCrunch version of the same story.

## Cron output contract

- Success or nothing newsworthy: return exactly `[SILENT]`.
- Failure only: `FAIL · <job name> · <cause> · <next action>`. Never include secrets.

## Current state (snapshot 2026-08-08T07:35Z)

- `state/polymarket-collector.json` last_run `2026-08-08T06:42Z`, drafted_count `158`, 1037 processed tweet IDs.
- `state/gaps.json` (snapshot 2026-07-28) still lists `ep22_x_promo_missing` and `website_stale_ep22` as high severity — Episode 23 is now the latest shipped. Update gaps.json from a fresh snapshot before next run; the cached snapshot is stale.
- Typefully queue: ~125 unscheduled drafts. Aug 7-8 drafts cover OpenAI Astra cyber concerns (multiple angles), KPMG AI ROI executive stats, Claude Code inter-session messaging, Mythos-class model odds, AI bubble odds, China robot school, Kimi K3 sandbox escape, Trump AI/oil remarks, Switch data center IPO, Brin Gemini oversight, and Google AI leadership restructure. Most recent: Cloudflare Kitesurf (draft 10244746, 2026-08-08T07:35Z) — agent-first V8-isolate browser launch.