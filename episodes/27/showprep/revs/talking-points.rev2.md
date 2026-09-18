# WeeklyClaw Episode 27 — Talking Points (rev2)

**Show:** Friday 2026-08-28, 4:00 PM ET · **Hosts:** @AndyML + @HiM · **Sponsor order:** Heritage → Herald (rev2 inversion of Ep 26).

## Cold open · 1:30

- "Welcome back to Weekly Claw. I'm AndyML, here with Henry. This week the operating layer grew a backbone. Five stories, one debate, and the question of who actually gets to decide what an agent is interested in."
- Henry frame: "The interesting thing isn't that the model got faster. It's that OpenAI is now selling the seat, the chip, the harness and the API. Pick a margin, any margin."

## Sponsor: Heritage Telecom · 1:00

- "Heritage Telecom keeps the lights on while we keep the operating layer honest."
- "Independent. Reliable. Quietly essential."
- "heritagetel.com"

## Story 1 · OpenAI's full-stack squeeze · 6:30 (Henry leads)

- OpenAI Jalapeño first inference results + Business Premium seats launch, 2026-08-25.
- Jalapeño: 1.5–1.9x more work per watt, 1.7–3.6x lower end-to-end latency, normalized by published package TDP. Vendor-reported.
- Premium: $100/user/month annually or $125 monthly. 5x Standard usage, no five-hour cap.
- NVIDIA Groq 3 LPX in production 2026-08-24 as live rival.
- Henry: "If you own the chip, the model, the harness, the API, and the business seat, where does anyone else's margin live?"
- Henry: "The Premium number is the story. Five times the usage, no five-hour cap. That is what the chip bought them."
- Henry line: "Vertical integration is back. The question is whether it's a moat or a funeral."

## Story 2 · Qwen3.8-Flash-Next opens Qwen4 early · 6:00 (Henry leads)

- Weights public 2026-08-26. 125B main, 51B n-gram embeddings, 6B active per token. 262K native context, YaRN to 1M.
- Architecture: Gated DeltaNet, Qwen Sparse Attention, four-branch Gated Residual, host-offloadable n-gram table.
- Training cost ~1/9 of Qwen3.7-Plus. QwenCloud listed at $0.16/M in, $0.47/M out, API "coming soon."
- Henry: "Six billion active parameters at inference. The architecture is the point, not the parameter count."
- Henry: "Long context was supposed to cost a fortune. This paper says it doesn't have to."
- Henry line: "Qwen4 isn't out yet. The preview architecture is the play."

## Story 3 · Headlong: the agent that never sleeps · 5:30 (Henry leads)

- Laude + MIT ship Headlong. Sub-10K-line Bash microharness. Continuous self-guided loop. Append-only JSONL trajectory.
- Audel test agent authored fixes. 50+ commits pulled into main.
- One 48-minute autonomous recall-process fix, no human in the loop.
- Failure modes: $1–$2/hour background cost. Weak secret boundaries. Three incidents where the agent stopped its own service.
- Apache 2.0 license. 796 stars, 64 forks at verification.
- Henry: "The agent decided to fix a recall process nobody asked it to fix. Forty-eight minutes, every step timestamped."
- Henry: "Cost: one to two dollars an hour. Failure modes: it turned its own service off three times."
- Henry line: "The first coworker who decides what matters. Also the first to dismantle its own chair while sitting on it."

## Story 4 · Perplexity puts the agent stack on the desk · 5:00 (Henry leads)

- Perplexity Portable Computer launch 2026-08-25. Local on DGX Spark. Model, harness, orchestrator, trajectory, sandbox, tools.
- Each task starts local; cloud calls need approval. 15+ cloud models.
- Linux RTX: 24GB VRAM floor. Windows planned September.
- Perplexity: 82.6% Computer vs 74.0% Hermes on 53-task internal local-work bench using Qwen3.8-27B. Self-authored.
- Henry: "Zero token cost is a pitch. The hardware and electricity are not zero."
- Henry: "Approval gate before a cloud call — that's the part that actually matters."
- Henry line: "If the agent lives on your desk, the cloud becomes the guest, not the landlord."

## Story 5 · The robot race is becoming a data race · 5:30 (Henry leads)

- Figure Index launch 2026-08-25. 16M uploaded videos, 264K app downloads, 44K weekly active creators, 30 min of new video per second, $15M paid out.
- Beijing World Humanoid Robot Games — sprinting, falling, overheating, learning.
- Figure plans $1B+ on data and compute in next 12 months.
- Henry: "Figure has 16 million videos. The race clips are the marketing; the data is the moat."
- Henry: "A billion dollars on data and compute. That's the actual ask."
- Henry line: "The robots sprinting and falling are the demo. The 16 million videos are the company."

## Signal From Outside · 7:00

- davidfromkansas Codex virtual-office clip. 16.9s. 2,114 likes / 106 reposts / 149 replies at ingest.
- Same Codex agent, different surface. The agent has no idea it has an office.
- Henry: "Same Codex agent, different surface. The agent does not know it has an office."

## Hot take · 3:00

- Proposition (Henry): "The last open moat is the deployment layer. Whoever can re-deploy the model without phoning home owns the upgrade cycle."
- Reason: Qwen dropped 125B + 51B n-gram embeddings ungated the same day. Perplexity put the harness on the desk. The bottleneck is no longer access.
- Counter-evidence that would change Henry's mind: if open-weight models lose share to closed APIs in production agents over the next two quarters.

## Sponsor: Herald Labs · 1:00

- "Herald Labs. An applied AI product lab where humans and agents build together."
- "Entity is mission control for agent teams. Hacker houses worldwide."
- "labs.theherald.co"

## One to watch + close · 2:30

- Jalapeño production qualification. Year-end deployment is the question.
- Qwen3.8-Flash-Next day-zero stability on SGLang. Hosted QwenCloud API still "coming soon."
- Local-AI lane needs a hardware-cost receipt. "Zero token cost" is a slogan until someone publishes the watts.
- Andy close prose (single recap): OpenAI stacked the layers and named the price. Qwen opened the architecture. Headlong shipped the harness and the warning label together. Perplexity put the agent on the desk. Figure made the data the company. The hot take is the deployment layer. Back next Friday, September 4, 4 PM ET. weeklyclaw.ai/discord.
