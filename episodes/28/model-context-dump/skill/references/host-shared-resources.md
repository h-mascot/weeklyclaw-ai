# Host-shared resources workflow

Henry and Andy share links, posts, videos, demos, and screenshots in the WeeklyClaw Telegram topic while the episode is being prepared or reviewed. These are authoritative editorial inputs — preserve them, don't silently replace them. This reference defines the retrieval, classification, insertion, and fact-checking technique.

## When this runs

- **BUILD tick**: before drafting, scan the originating Telegram topic + active episode files for host-shared resources.
- **Mid-build lineup changes**: when Henry sends new topics (he does this regularly), check for accompanying links in the same message thread.
- **Any host message containing URLs**: treat as host-shared resources for the relevant segment.

## Retrieval

1. Collect every URL Henry or Andy shared, grouped by the topic/segment they attached it to (or infer from URL content when no label was given).
2. Retrieve each resource where tooling permits:
   - **X/Twitter posts**: `bird read <url> --plain` via `~/clawd/scripts/bird-env.sh`. Captures author, text, media URLs, date, engagement counts.
   - **YouTube videos**: `yt-dlp --print '%(title)s | %(channel)s | %(duration_string)s' <url>`. Captures title, channel, runtime. Use `--write-thumbnail --convert-thumbnails jpg` when a poster is needed.
   - **Web pages**: `curl -sS -o /dev/null -w '%{http_code} %{url_effective}' <url>` for reachability; `web_extract` for content.
3. Record the retrieval result (content, metadata, HTTP status, timestamp) in `sources/host-shared-resources.md`.

## Classification tiers

Classify each resource so fact-checking is applied correctly:

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Official/primary** | Official account post (@Alibaba_Qwen, @Cloudflare, @ycombinator, @elonmusk, @finkd), official blog post, product launch page, Nature paper | Primary launch receipt. Still corroborate material numerical/causal claims. |
| **Practitioner/hands-on** | Henry's own post testing a product (@iAmHenryMascot with BB + Liquid), Andy's pinned candidate | Presenter experience. High editorial value; quote as host experience, not independent proof. |
| **Community/discussion** | Non-official X post (@ns123abc, @niccruzpatane, @_can1357), review video (Theo - t3.gg) | Supporting visual/discussion receipt. Use as talking-point fuel and on-screen visual; label as community signal. Do not convert into benchmark proof. |

## Output artifacts

Every host-shared resource must appear in three places:

### 1. Source ledger: `sources/host-shared-resources.md`

One section per topic with:
- Exact URL
- Retrieved metadata (author, title, date, runtime if video)
- Classification tier
- What it demonstrates / presenter use
- Caveats

### 2. Agenda production notes

Under each segment's `### Sources and production notes (not read on air)`, add a `Host-shared resources` subsection listing the exact URLs. Also add a consolidated `## Host-shared resources and show links` section before the Build reference with all links grouped by topic.

### 3. Deck slide: `s-host-resources`

Insert a clickable resources slide as the penultimate slide (before Sources). Use this structure:

```html
<!-- CSS (add before </style>) -->
.resource-list{display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%;max-width:1120px;text-align:left;}
.resource-item{display:block;background:rgba(255,255,255,.04);border:1px solid var(--border-subtle,rgba(255,255,255,.12));border-radius:10px;padding:10px 12px;color:var(--text-primary,#eee);text-decoration:none;font-size:.78rem;line-height:1.3;overflow-wrap:anywhere;}
.resource-item:hover{border-color:var(--claw-red,#e74c3c);}
.resource-item strong{color:var(--claw-orange,#e67e22);display:block;margin-bottom:2px;}

<!-- Slide (insert before final </div>\n<script>) -->
<div class="slide" id="s-host-resources">
  <div class="slide-brand"><svg><use href="#weeklyclaw-logo"/></svg> Weekly Claw #<N></div>
  <div class="slide-tag">HOST RESOURCES</div>
  <div class="content">
    <div class="part-label">Links Henry shared for this episode</div>
    <h2 class="text-center">Primary demos, posts, <span class="gradient-text">and discussion receipts.</span></h2>
    <div class="gradient-line"></div>
    <div class="resource-list mt-2">
      <a class="resource-item" href="URL" target="_blank"><strong>TOPIC</strong>description</a>
      ...
    </div>
  </div>
</div>
```

### 4. Speaker notes appendix

Add a `## Host resource appendix` to `speaker-notes.rev<N>.md` pointing to the ledger file and the deck slide.

## Equivalent-resource finding (when hosts supplied nothing)

For each selected topic where no host link exists, find:
- At least one **primary/official receipt** (official blog, repo, paper, announcement post)
- One useful **visual/demo/discussion** (screenshot, UI, chart, practitioner video, credible community post)

Record creator, direct URL, source tier, what it demonstrates, presenter use, video cue/timestamp + fallback, and retrieval result. If materially different searches all fail, record the failed queries — never fabricate a resource.

## Publication

The host-resources slide, agenda section, source ledger, and speaker-notes appendix all publish with the draft via the standard worktree route. No special handling needed — they live under `episodes/<N>/` and pass `validate.mjs` because they don't touch the gallery or homepage.

## Episode 24 receipt (2026-08-07)

Henry supplied 14 links across 5 topics (AMD/Taalas, Terafab, Security, Models, Harnesses). All 14 were retrieved, classified, and inserted into the deck + agenda + notes + ledger. One naming correction surfaced: Henry said "Qwen 2.8 Max" — the official @Alibaba_Qwen post says "Qwen3.8-Max" and "Qwen3.8-27B". The ledger preserves Henry's wording with a correction note; the deck and agenda use the verified official naming.
