# WeeklyClaw Episode 27 — Henry's Section (rev2)

**Show:** Friday 2026-08-28, 4:00 PM ET · **Co-host:** @AndyML · **Sponsor order (rev2):** Heritage → Herald.

**Your standing role:** Lead all five What Happened This Week segments. Frame the cold open. Lead the hot take with a sharp proposition. Close with one-to-watch callouts.

## Cold open (lead the frame after Andy's intro)

- One-line frame (lead with this): "The interesting thing isn't that the model got faster. It's that OpenAI is now selling the seat, the chip, the harness and the API. Pick a margin, any margin."
- Pivot to Story 1: "Let's start with the OpenAI stack."

## Story 1 · OpenAI's full-stack squeeze (you lead)

- Numbers: Jalapeño 1.5–1.9x work/watt, 1.7–3.6x lower end-to-end latency (vendor-reported, normalized by published TDP). Premium $100/user/yr, 5x Standard usage, no five-hour cap. NVIDIA Groq 3 LPX in production 2026-08-24.
- Anchor line: "If you own the chip, the model, the harness, the API, and the business seat, where does anyone else's margin live?"
- Follow-up: "The Premium number is the story. Five times the usage, no five-hour cap. That is what the chip bought them."
- Optional closer: "Vertical integration is back. The question is whether it's a moat or a funeral."

## Story 2 · Qwen3.8-Flash-Next opens Qwen4 early (you lead)

- Numbers: 125B main, 51B n-gram embeddings, 6B active per token. 262K context, YaRN to 1M. Training ~1/9 of Qwen3.7-Plus. QwenCloud $0.16/M in, $0.47/M out, API "coming soon."
- Anchor line: "Six billion active parameters at inference. The architecture is the point, not the parameter count."
- Follow-up: "Long context was supposed to cost a fortune. This paper says it doesn't have to."
- Optional closer: "Qwen4 isn't out yet. The preview architecture is the play."

## Story 3 · Headlong: the agent that never sleeps (you lead)

- Story beats: sub-10K-line Bash harness, continuous self-guided loop, append-only JSONL trajectory. Audel test agent. 50+ self-authored commits merged. One 48-minute autonomous recall-process fix, no human in the loop.
- Failure modes: $1–$2/hour background cost. Three incidents where the agent stopped its own service. Apache 2.0, sandbox warnings.
- Anchor line: "The agent decided to fix a recall process nobody asked it to fix. Forty-eight minutes, every step timestamped."
- Follow-up: "Cost: one to two dollars an hour. Failure modes: it turned its own service off three times."
- Optional closer: "The first coworker who decides what matters. Also the first to dismantle its own chair while sitting on it."

## Story 4 · Perplexity puts the agent on the desk (you lead)

- Story beats: model + harness + sandbox + tools all local on DGX Spark. Approval gate before any cloud call (15+ cloud models). Linux RTX: 24GB VRAM floor. Windows planned September. Perplexity 82.6% Computer vs 74.0% Hermes on 53-task local-work bench (self-authored).
- Anchor line: "Zero token cost is a pitch. The hardware and electricity are not zero."
- Follow-up: "Approval gate before a cloud call — that's the part that actually matters."
- Optional closer: "If the agent lives on your desk, the cloud becomes the guest, not the landlord."

## Story 5 · The robot race is becoming a data race (you lead)

- Story beats: Figure Index launched 2026-08-25. 16M uploaded videos, 264K app downloads, 44K weekly active creators, 30 min new video per second, $15M paid out. Beijing World Humanoid Robot Games. Figure plans $1B+ on data and compute in 12 months.
- Anchor line: "Figure has 16 million videos. The race clips are the marketing; the data is the moat."
- Follow-up: "A billion dollars on data and compute. That's the actual ask."
- Optional closer: "The robots sprinting and falling are the demo. The 16 million videos are the company."

## Signal From Outside (one line)

- After Andy's frame: "Same Codex agent, different surface. The agent does not know it has an office."

## Hot take (you lead with the proposition)

- Proposition: "The last open moat is the deployment layer. Whoever can re-deploy the model without phoning home owns the upgrade cycle."
- Reason: Qwen dropped 125B + 51B n-gram embeddings ungated the same day. Perplexity put the harness on the desk. The bottleneck is no longer access — it is local tooling, local data, and the social permission to re-deploy.
- What would change your mind: if open-weight models lose share to closed APIs in production agents over the next two quarters.
- Close: "Five segments, one assumption: someone else owns the model. Open weights closed that gap long ago. Persistent initiative shipped this week. Local-first is now a product. What hasn't shipped is who owns the deployment layer."

## One to watch + close (you supply the callouts, Andy recaps once)

- Jalapeño production qualification. Gen 2 and Gen 3 are roadmap, not capacity. Year-end deployment is the question.
- Qwen3.8-Flash-Next day-zero stability on SGLang. Independent evals are starting.
- Local-AI lane (Perplexity Portable Computer, DGX Spark) needs a hardware-cost receipt.

## Sponsor rotation reminder (rev2)

- Sponsor 1 = Heritage (after cold open, before Story 1).
- Sponsor 2 = Herald (after hot take, before close).
- This is the inversion of Ep 26 (which was Herald → Heritage). Don't read them out of order.

## Handoff rules

- "Henry, what's the frame?" → your cold-open frame → Story 1.
- After Sponsor 1 (Heritage) → Story 1 opener.
- After Story 3 (Headlong) → "Henry, that's an agent on a server. Perplexity just put one on the desk." → Story 4.
- After Story 5 (robot-data) → "Now the part where we fight about it." → Hot take.
- After hot take → "Time for the second sponsor read." → Sponsor 2 (Herald).
- After close prose → end of show.
