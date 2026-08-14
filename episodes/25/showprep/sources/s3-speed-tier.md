# S3 — Gemini 3.7 Flash + OpenAI Ultrafast: speed becomes a product tier

**Candidate:** C25 + C28 — Gemini 3.7 Flash Pareto time-frontier (Aug 13) + OpenAI Ultrafast preview on GPT-5.6 Sol (Aug 13)
**Score:** 9.7 (merged; C25 alone 9.9, C28 alone 9.5)
**Owner:** Henry (lead)

## Story

Two vendors shipped the same idea on the same day: useful work per second is now a service-level choice. Google's Gemini 3.7 Flash reached the intelligence-vs-time Pareto frontier at ~340 output tokens/sec independently (Artificial Analysis). OpenAI launched Ultrafast on GPT-5.6 Sol at up to 750 output tokens/sec behind a Cerebras route — a select-customer waitlist with capacity-gated expansion.

## Numbers

**Gemini 3.7 Flash (Aug 13):**
- 1,048,576-token multimodal input / 65,536 output
- Pricing: **$0.75 / $3.75** per M tok through Dec 31, then **$1.50 / $7.50**
- Independent: AA Intelligence Index **56**, ~340 tok/s, AutomationBench-AA **62.7%**, AA-AnalystAgent pass^5 **60%**
- Day-one distribution: VS Code, CLI, cloud agent, app, JetBrains, Xcode, Eclipse via GitHub Copilot

**OpenAI Ultrafast (Aug 13, limited preview):**
- Up to **14×** Standard speed
- Up to **750 output tok/s** on the same GPT-5.6 Sol weights
- Cerebras-backed route
- Price undisclosed

## Vendor-reported vs independent

- Flash: AA Intelligence 56, AutomationBench-AA 62.7%, AA-AnalystAgent pass^5 60%, ~340 tok/s are independent. Vendor-reported for the rest.
- Ultrafast: throughput self-reported; no matched independent run; no public Ultrafast SLA; price undisclosed — do not infer from Standard or Fast tiers.

## Caveats

- Do not claim a fixed Ultrafast latency floor — OpenAI disclosure is throughput-only.
- The 14× multiplier is "up to" — ceiling, not baseline.
- Cerebras supply is capacity-gated; expansion pacing is OpenAI-controlled.

## Sources

- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
- https://artificialanalysis.ai/articles/gemini-3-7-time-frontier
- https://openai.com/index/previewing-ultrafast/
- https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash
- https://github.blog/changelog/2026-08-13-gemini-3-7-flash-is-now-available-in-github-copilot/