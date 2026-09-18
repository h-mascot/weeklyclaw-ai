# WeeklyClaw Episode 27 — Henry Section (rev1)

**Owner:** Henry Mascot · **Section format:** concise talking points, one optional landing line per segment, handoff cue.

## Cold open

- "The operating layer grew a backbone this week."
- Five stories, one debate, the question of who decides what an agent is interested in.
- Land Story 1 (OpenAI) without previewing the rest.

**Handoff:** Andy opens Story 1.

## Story 1 · OpenAI's full-stack squeeze · 6:30

- OpenAI just stacked chip + model + harness + business seat. Named the price: $100/user/year Premium.
- Jalapeño: 1.5–1.9x more work per watt, 1.7–3.6x lower end-to-end latency. Vendor-reported, normalized by published package TDP.
- 5x Standard usage. No five-hour cap.
- NVIDIA Groq 3 LPX in production 2026-08-24 — the rival is real.

**Henry line (optional):** "Vertical integration is back. The question is whether it's a moat or a funeral."

**Handoff:** "Andy, the OpenAI stack is one answer. Qwen just opened a different one."

## Story 2 · Qwen3.8-Flash-Next opens Qwen4 early · 6:00

- 125B main + 51B n-gram embeddings + 6B active/token. 262K native context, 1M with YaRN.
- Gated DeltaNet + Qwen Sparse Attention + four-branch Gated Residual + host-offloadable n-gram embedding table.
- Weights public 2026-08-26. Training cost reported ~1/9 of Qwen3.7-Plus.
- QwenCloud API is "coming soon." Vendor benchmark.

**Henry line (optional):** "Qwen4 isn't out yet. The preview architecture is the play."

**Handoff:** "Henry, this is what long-context agents are made of. Who decides what they do with it?"

## Story 3 · Headlong: the agent that never sleeps · 5:30

- Sub-10K-line Bash microharness, Apache 2.0. Append-only thought DAG crosses Slack, Telegram, web.
- Internal agent Audel: 50+ commits pulled into main. One autonomous fix, 48 minutes, timestamped.
- Cost $1–$2/hour background. Stopped its own service three times. Self-delegation died on day one.

**Henry line (optional):** "The first coworker who decides what matters. Also the first to dismantle its own chair while sitting on it."

**Handoff:** "Henry, that's an agent on a server. Perplexity just put one on the desk."

## Story 4 · Perplexity puts the agent stack on the desk · 5:00

- Portable Computer on DGX Spark. Model + harness + orchestrator + trajectory + sandbox + tools. Cloud calls gated by approval.
- Linux RTX support requires 24GB VRAM. Windows in September.
- "Zero token cost" still leaves hardware, electricity, subscription. Self-authored bench.

**Henry line (optional):** "If the agent lives on your desk, the cloud becomes the guest, not the landlord."

**Handoff:** "The robots are chasing a different prize."

## Story 5 · The robot race is becoming a data race · 5:30

- Figure Index: 16M uploaded videos, 264K app downloads, 44K weekly active creators, 30 min new video/sec, $15M paid out.
- Beijing World Humanoid Robot Games same week — sprinting, falling, overheating.
- Figure plans >$1B on data + compute in next 12 months.

**Henry line (optional):** "The robots sprinting and falling are the demo. The 16 million videos are the company."

**Handoff:** "Now the part where we fight about it."

## Hot take · 3:00

- Proposition: "The last open moat is the deployment layer. Whoever can re-deploy the model without phoning home owns the upgrade cycle."
- Reason: Qwen dropped ungated same-day. Headlong shipped Apache 2.0. Perplexity put the agent on the desk. Bottleneck is no longer access.
- What would change his mind: open-weight models losing production-agent share to closed APIs in two quarters.

**Handoff:** "That's the take. Time for the second sponsor read."

## Close · One to watch

- Jalapeño production qualification. Year-end deployment is the question.
- Qwen3.8-Flash-Next SGLang day-zero stability. QwenCloud API going from "coming soon" to live.
- Local-AI lane (Portable Computer, DGX Spark) needs a hardware-cost receipt. "Zero token cost" is a slogan.

**Handoff:** None — end of show.