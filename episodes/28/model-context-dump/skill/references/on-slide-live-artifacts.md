# Visual-first live artifacts for news slides

Use this for every **What Happened This Week** slide. The slide supports Henry's live narration; it is not a briefing document.

## Governing rule

Each news slide should contain:

1. One dominant picture, playable video, live chart, product demo, source receipt, or webpage capture.
2. One headline.

**Headline voice (Henry, Ep26 rev9/rev10): plain launch phrasing only.**
`[Company] launches their newest <thing>: the <name>.` or `DHH launches the
Omacom Foundation with $8M.` Statement variant: `Stripe buys OpenRouter, & the
hot stealth model.` No copywriter punchlines ("The chart is the launch",
"...is the boss of GPT-5.5 now", "Agents can pay mid-task without ever
holding your keys") — Henry rejects them as "not the way I talk". Write the
first line of the segment as he would say it; mirror his own tweet phrasing
when he tweeted the story. Keep titles across segments in the SAME pattern
(launch-style or statement-style) so the rundown reads evenly.
3. Zero to two short context lines.
4. One discreet source or `▶ LIVE` link.

Everything else belongs in speaker notes: evidence, caveats, benchmark details, numbers, comparisons, talking points, questions, and handoffs.

### Forbidden layout

Do not build a dense three-card slide and append a small `ON-AIR LIVE ARTIFACT` panel. Episode 26 rev3 used that pattern and Henry rejected it. The artifact was technically present but visually subordinate to the copy.

No body paragraphs, bullet lists, comparison cards, metadata panels, evidence blocks, or on-slide talking points in this section.

## 1. Choose an artifact worth showing

**Launch-type-aware preference (Henry, 2026-08-21): match the artifact to what the story IS.**

- **Hardware/chip/product launch → the vendor's official video first.** Example: Cerebras CS-4 segment must use Cerebras's own C4 chip video, not a screenshot of the product page.
- **Model release → the benchmark.** Example: DeepSeek Flash Vision segment must show the benchmark (live leaderboard/chart where possible), not the paper or announcement page.
- **Product feature/deal → live demo, or the primary receipt page only if no demo exists.**

Generic preference order when the above doesn't pin it:

1. Playable product/demo video with a verified cue.
2. Live chart, benchmark, product UI, or interactive demo.
3. Strong official image or chart.
4. Recognizable primary-source announcement or receipt page.
5. Text-heavy docs page only as a fallback.

A screenshot of an announcement page is NOT an acceptable primary artifact for a launch that has an official video, demo, or benchmark available. Search for the vendor video (official channel/upload) and the benchmark receipt BEFORE falling back to a page capture, and record the searches in `capture-manifest.json` when a video/benchmark genuinely doesn't exist.

## 1a. Sourcing launch-type artifacts (verified 2026-08-21, Episode 26)

The vendor's official launch VIDEO often lives only on the X launch post, not YouTube. Sourcing order that worked:

1. `BIRD_ACCOUNT=henry ~/clawd/scripts/bird-env.sh search '<product> from:<vendor>' -n 5 --json --plain` — the launch post's `media[].videoUrl` is a direct mp4 (`video.twimg.com/amplify_video/...`). `curl -sL` it directly; verify with `ffprobe` (codec, duration, resolution). Grab `media[].url` as the poster frame. Burn case: Cerebras's official CS-4 video exists ONLY on the X launch post (`x.com/cerebras/status/2089870131291943228`, 68s 1080p) — their YouTube channel had no CS-4 video at launch.
2. YouTube channel scan (`yt-dlp --flat-playlist 'https://www.youtube.com/@<vendor>/videos'`) as second choice — but check recency; a new chip launch may have no dedicated channel video yet, in which case the X launch video IS the official one.
3. For model releases, the official launch post's image may BE the benchmark chart. DeepSeek's V4-Flash-Vision-Exp launch image (`x.com/deepseek_ai/status/2090730032574631962`) was the full score table (ApexBench 36.5 vs Opus 39.4, Terminal Bench 2.1 83.9, DeepSWE 59.3, Agents' Last Exam 27.3). Download `media[].url` and OCR it (`tesseract <img> -`) to verify it is a score table before using it as the benchmark artifact — this replaces arxiv/paper screenshots.
4. Record everything in `media-manifest.json` with source post URL, creator, provenance (download time, ffprobe/OCR verification), poster, and fallback still.

If the best artifact is a generic docs page or text-only announcement, mark the story `WEAK-VISUAL` and propose a merge or swap. A high story score does not rescue a poor on-air visual.

Record in `media-manifest.json`:

- `type`: `VIDEO_CLIP | LIVE_DEMO | LIVE_CHART | SCREEN_CAPTURE | RECEIPT_PAGE`
- direct source URL
- creator/publisher
- capture time or video cue
- provenance and rights note
- presenter action
- fallback asset

## 2. Capture source material

For webpages, use headless Chromium at the deck's target viewport. Wait for `domcontentloaded`, allow a short settle, then capture. Verify the page title and visible source identity after capture so cookie walls, soft 404s, and interstitials do not masquerade as valid artifacts.

Store captures under:

`showprep/assets/images/artifacts/<segment>-<source>.png`

Keep a concise `capture-manifest.json` with URL, path, capture time, byte size, title, and error state. Capture a backup source when available.

Reject captures that are blank, mostly chrome/navigation, illegible at presentation scale, or dependent on tiny text. A valid webpage screenshot can still be a bad presentation artifact.

For videos, record the exact direct URL, cue/timestamps, poster frame, fallback still, and embedding restrictions. Never autoplay.

## 3. Build visual-first slide composition

Use the prior APPROVED episode's theme and chrome unchanged. Replace only episode content.

Recommended composition:

- Artifact occupies the majority of usable visual area.
- Headline remains readable from a distance.
- Context line is optional and short.
- Source link is visually secondary.
- Crop preserves the recognizable product, chart, result, or source identity.

Example structure using only authority-deck styles plus inline layout:

```html
<div class="slide" id="s-seg-example">
  <!-- inherited brand, tag, and decorative chrome -->
  <div class="content" style="display:flex;gap:36px;align-items:center;">
    <div style="flex:1.1;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;">
      <div class="story-num">SEG 1 · CATEGORY</div>
      <h2 class="text-center">Short headline <span class="gradient-text">with one landing idea.</span></h2>
      <div class="gradient-line"></div>
      <p class="subtitle text-center mt-1">Optional short context line.</p>
      <a href="{source-url}" target="_blank" rel="noopener">▶ LIVE · Source</a>
    </div>
    <div style="flex:1.3;height:100%;display:flex;align-items:center;">
      <a href="{source-url}" target="_blank" rel="noopener">
        <img src="assets/images/artifacts/{capture}.png"
             alt="{specific source and artifact description}"
             style="width:100%;max-height:640px;object-fit:cover;object-position:top;border-radius:14px;">
      </a>
    </div>
  </div>
</div>
```

This is a starting pattern, not a mandate to split every slide 50/50. Full-bleed video, chart-led, and image-led compositions are preferred when they make the artifact clearer.

## 4. Move detail to speaker notes

Each corresponding speaker-note entry should carry:

- owner and purpose
- opening/landing line
- 3–5 concise talking points
- exact evidence and caveats
- source links
- visual action: show, play, scroll, zoom, or open live
- video cue/timestamp when applicable
- handoff/question
- cut contingency

The deck stays sparse because the notes hold the briefing.

## 5. Deterministic review gate

Before review or publication:

1. Assert every news slide has exactly one primary artifact element (`img`, `video`, or explicit live-demo frame/link).
2. Assert all local artifact paths resolve and images have nonzero `naturalWidth`.
3. Render at 1600×900.
4. Measure DOM bounding boxes; require zero content clipping outside the slide box. Ignore authority-deck decorative glow-orb clipping.
5. Inspect each rendered news slide for visual dominance. The artifact should read first or jointly with the headline, never as a thumbnail attached to copy.
6. Reject body paragraphs, bullet lists, multi-card evidence layouts, or small labeled artifact panels in news slides.
7. Verify headline plus context copy is limited to the intended sparse format.
8. Confirm every live link opens the correct primary source and every video has a fallback still.
9. Run the canonical deck validator with the prior APPROVED episode as authority.
10. Publish assets with the deck, then verify decoded live-page canaries and at least one representative asset byte/hash match.

## Recovery after a bad dense revision

When a revision contains correct facts but the slide format is wrong:

1. Recover the current live/canonical deck before editing if local generation files are inconsistent.
2. Keep slide IDs, source URLs, artifact files, theme, sponsor assets, and speaker notes.
3. Replace only the news-slide bodies.
4. Reduce each to dominant artifact + headline + at most two short lines + source link.
5. Rebuild, validate, render, and measure clipping.
6. Republish through the clean worktree and whitelist-copy route.
7. Verify a new sparse-copy canary is present and an old dense-copy canary is absent.

## Pitfalls

- **Artifact present is not artifact dominant.** DOM presence proves loading, not presentation quality.
- **A screenshot of a text page is still text.** Prefer video, charts, UI, or recognizable receipts.
- **Do not optimize dense copy to fit.** If fitting requires shrinking panels and fonts, remove the copy and move it to notes.
- **Do not use OCR as the primary visual gate.** Use DOM checks for loading/clipping and inspect the rendered composition.
- `object-fit: cover; object-position: top` can preserve source identity, but verify it does not crop the actual result or chart.
- Refresh captures when the source changes materially; the embedded still is the preview, while the live link is the on-air artifact.

## Session provenance

- Episode 26 rev2 failed because artifacts existed only in backstage metadata.
- Episode 26 rev3 failed because artifacts appeared as small cards beside dense briefing copy.
- Corrected rule: for Henry-led weekly news, pictures/videos are the slide; text is only a minimal cue.
- Episode 26 rev3 also defaulted every news segment to a static receipt screenshot with no `▶ LIVE` links; Henry (2026-08-21): "if there is a video we should use that, or a demo or a benchmark" — Cerebras segment must be their launch video, DeepSeek segment the benchmark chart. Artifacts sourced and staged for rev4 per §1a.
- Episode 26 rev4 (cron-built) IGNORED the staged artifacts and re-shipped the old screenshots — staging in `workflow-feedback.md` is not enough; the rebuild must diff asset references against every staged artifact (see `references/host-triggered-rebuild.md` rev5 lessons).
- Episode 26 rev5 shipped the corrected set: Faraday = official benchmark chart from @inherent_labs launch thread tweet media (thread photos often contain the results chart; OCR to identify which tweet's image is the chart vs hero art); Cerebras = embedded `<video controls poster preload="metadata">` (no autoplay); AWS = H1-anchored GA blog capture. Validation: 19/19 PASS, 13 slides rendered, live sha256 match on the video asset. Also caught the Faraday slide linking the WRONG arXiv paper (2508.14251 vs the real 2608.13331) — always title-check receipt URLs.
- arXiv HTML figures are unreliable as benchmark artifacts: the figure list may show a results figure whose `<img>` never loads (SVG-embedded or missing). Prefer the vendor/author's own launch-post chart image over scraping arXiv HTML.
- Episode 27 rev3 (2026-08-28) shipped well-formed images whose CONTENT was wrong: an empty CNBC jpg, a "NotFound" JSON body in a `.jpg`, an HTML body in another, and an abstract sign graphic on the Nvidia slide. Henry: "means you ddnt verify the content in each image". The added gate is OCR/vision content verification — every image must yield text/structure naming what it shows (headline, chart axes, faces), logged per-image, BEFORE publish. `file` type checks and HTTP 200 prove nothing about content.
- Episode 27 rev4 media-selection upgrades (Henry, 2026-08-28): benchmark chart beats article screenshot for model/chip launches (GLM-5.3 full-results chart from the X launch post; SemiAnalysis Jalapeño-vs-Blackwell analysis for the chip); magazine COVER page when one exists (TIME cover for the Altman AGI story); tweet COLLAGE for funding/valuation news (three verbatim posts rendered as X-style cards — see the Ep27 `qa/make_instinct_collage.py` PIL pattern when browser capture of x.com fails; fetch real tweets via bird CLI, never fabricate engagement numbers).
- Episode 27 rev4 clustering (Henry, 2026-08-28): same-entity stories (Jalapeño + AGI, both OpenAI) and same-class near-simultaneous launches (GLM-5.3-Flash + Qwen Flash-Next) go on ONE slide with two side-by-side artifacts; under the shorter-but-more-items format target 3-4 clustered news slides, not 9-10 single-story slides. Sponsors read at start and end only, never mid-show.
- `pbs.twimg.com` media URLs 403 to plain Python urllib but download fine via `curl -sL -A "Mozilla/5.0 ..."` — use curl with a browser UA for X-hosted images.
