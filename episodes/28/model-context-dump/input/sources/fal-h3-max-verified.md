# C3 — fal launches H3 Max ("Fals H3 Max" in Henry's message) · verified 2026-09-04 ~01:45 UTC

## Primary receipts
- PRNewswire launch release (Sep 1, 2026, 11:10 ET): https://www.prnewswire.com/news-releases/fal-launches-h3-max-a-new-post-trained-video-model-with-frontier-quality-and-faster-than-real-time-generation-302866462.html — full extract: `sources/fal-h3-max.md` (cache copy).
- fal X pricing extension post: https://x.com/fal/status/2094834516854788528
- fal model page: https://fal.ai/models/minimax/h3-max

## Key facts (from the release)
- H3 Max = post-trained MiniMax H3 (open weights) + fal co-designed inference engine; "fal the original creator of H3 Max."
- Speed: ~5s video in ~3s wall time; ~35x throughput of official MiniMax H3 endpoint; avg ~15x faster than comparable-quality models (fal testing).
- Independent leaderboards (as of Aug 26, 2026): #1 Design Arena Image-to-Video (Elo 1,341 vs official H3 1,333; ahead of Seedance 2.5, FLUX.3, Gemini Omni Flash); #1 Artificial Analysis I2V-with-Audio (Elo 1,201, 2,177 samples; ahead of Seedance 2.0, MiniMax H3, Gemini Omni Flash, Grok Imagine 1.5, Veo 3.1, Kling 3.0).
- Internal: #1 vs 12 leading video models in head-to-head human preference (overall, prompt understanding, aesthetics).
- Pricing: 50% off first week; extended through Sep 7 at 75% off t2v/i2v ($0.0125/s @480p, $0.02/s @768p promo; $0.08/s durable list at 768p per third-party cost comparison).

## Corroboration
- MiniMax H3 team quote in release (partnership confirmation).
- Third-party cost analysis: https://omidsaffari.com/blog/real-time-ai-video-api-cost-comparison-2026
- Kie.ai explainer: https://kie.ai/blog/what-is-minimax-h3-max

## Caveats
- Speed claims are fal's own testing except the two independent leaderboards.
- Leaderboard ranks dated Aug 26; can move.
- MiniMax open-sourced H3 weights (33B omni-modal, ≤15s @2K) — community LoRAs shipped within 48h (Thursdai.news). H3 Max itself is fal's post-trained variant.
