# Aired-video vs deck comparison (What Happened This Week review)

Use this reference when Henry asks to compare the slides *as aired on video* (not the deck files), e.g. "compare what happened this week across episodes 24/25/26," or when verifying whether a built lineup matches the show's established on-air pattern.

## Why this exists

The aired video is the editorial ground truth. The final deck revision and the aired video usually match, but the agenda's early revisions do NOT (Episode 24: agenda rev1 listed different segments than final deck rev3 / the aired video). Always compare against the **latest deck revision** and, when asked about "the video," against the published video itself — the on-air visual treatment (live walkthroughs, charts, X panels) often differs from the deck even when segment identity matches.

## Episode video discovery

- WeeklyClaw channel: `youtube.com/@WeeklyClaw` (channel id `UCa0Mxn9vyx6NnU-aBgRcRvg`).
- Enumerate recent uploads without auth via the RSS feed:
  `https://www.youtube.com/feeds/videos.xml?channel_id=UCa0Mxn9vyx6NnU-aBgRcRvg`
  (8 most recent entries with title + video id + published date. Parse `<entry>` blocks; the `<link href>` regex needs the *first* href in each entry.)
- Published titles do not always carry episode numbers — match by published date (episode N airs Friday; video appears within ~1 day).

## Download recipe (yt-dlp 403 workaround)

Default yt-dlp clients (web/android_vr) hit `HTTP 403 Forbidden` on googlevideo URLs for this channel (SABR/PO-token enforcement, yt-dlp issue #12482). Working invocation:

```bash
yt-dlp --extractor-args "youtube:player_client=android" -f 18 --no-progress -o "wc-ep<N>.%(ext)s" "https://www.youtube.com/watch?v=<id>"
```

- Format 18 (360p mp4, muxed audio) is sufficient for slide identification and is small (~70 MB for ~50 min). Formats 134/136 etc. also work with the android client if higher res is needed.
- `player_client=android` is the key flag; without it every format 403s.

## Slide-identification pipeline (no vision model required)

1. **Triage frames:** `ffmpeg -i video.mp4 -vf fps=1/20,scale=640:-1 triage/t%04d.jpg` (one frame / 20 s).
2. **Dedupe:** perceptual aHash (16x16, mean threshold) per frame; keep frames with Hamming distance > 28 from all kept representatives → distinct on-screen views.
3. **News-block location:** OCR (tesseract) the representatives with preprocessing: convert to grayscale, `ImageOps.autocontrast(cutoff=2)`, upscale 2.5-3x LANCZOS, crop to top ~50%. All-caps slide titles (e.g. "FOUR BEATS. ONE SHIFT.", "FIVE SEGMENTS. ONE OPERATING LAYER.") mark the news intro.
4. **Dense scan:** once the news intro timestamp is found, extract frames every 10 s across the news section at full res and OCR each; segment slides surface as ALL-CAPS phrases, product names, and benchmark labels (LiveBench, SWE-bench Pro, Terminal Bench, model names).
5. **Hard OCR truths:** thresholding destroys the cream-on-teal theme — do NOT binarize. autocontrast + upscale is the reliable path. PSM 11 for sparse title text, PSM 3/6 for body.
6. **Deliverable:** contact sheets per episode (PIL, ~900px wide frames with timestamp bars) sent as media, plus a written pattern comparison (segments aired vs planned lineup).

## Editorial pattern check (what to compare)

Against the last two aired episodes, check the planned lineup for:
- **Mix balance:** ≥2 model-capability segments, ≥1 infra/economics beat; flag if 3+ of 5 segments share one thesis (e.g. Episode 26 draft ran Stripe-OpenRouter + AWS payments + Qwen license cliff = three money-rails segments — EP24/25 never aired two segments on one thesis).
- **Category continuity:** security/agent-safety beat aired in EP24 (twice); its absence in a planned lineup is a gap worth surfacing.
- **Duplicate-thesis merge:** if the candidate intake itself says two stories "pair," they probably should not air as two full 5-minute segments.
- Bench alternatives: pull non-selected candidates (daily-topic-list.md, `SUPPORTING COLOR` / `HOLD` rows) with scores ≥7.5 as promotion options and offer concrete commands (`MERGE 4 5`, `SWAP 5 <slug>`).

## Caveats

- OCR identifies segment identity reliably; exact on-screen wording is less reliable. Label confidence accordingly.
- Episode recordings may also exist in `~/weeklyclaw/recordings/` (audio inventory) but recent episodes (24+) were not locally recorded; the YouTube channel is the source of truth for aired video.
