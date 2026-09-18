# WeeklyClaw Episode 27 — Andy Section (rev1)

**Owner:** Andy · **Section format:** complete fallback talk track per segment where he participates, then handoff cue. May paraphrase live.

## Cold open · 1:30

**Andy (opening):** "Welcome back to Weekly Claw. I'm AndyML, here with Henry. This week the operating layer grew a backbone. Five stories, one debate, and the question of who actually gets to decide what an agent is interested in. Henry, what's the frame?"

**Handoff:** Henry opens Story 1.

## Story 1 · OpenAI's full-stack squeeze

**Andy fallback talk track (after Henry lead):** OpenAI just stacked four layers that used to live at four different companies — chip, model, harness, business seat — and they're naming the price at a hundred dollars a user per year. Jalapeño is the chip, Premium is the seat. Premium removes the five-hour cap and sells five times the usage of Standard. The numbers OpenAI published — 1.5 to 1.9 times more work per watt, 1.7 to 3.6 times lower end-to-end latency — are normalized by their own package TDP. The rival is real: NVIDIA Groq 3 LPX went into production the day before. Two inference stacks, two vendors selling the whole thing.

**Handoff cue:** "Henry, the OpenAI stack is one answer. Qwen just opened a different one."

## Story 2 · Qwen3.8-Flash-Next

**Andy fallback talk track:** Qwen dropped the Qwen4 preview architecture on the same day as the Flash-Next weights. It's a multimodal mixture of experts: 125 billion main parameters, 51 billion n-gram embeddings, six billion active per token. Native context is 262K and you can extend it to a million with YaRN. The interesting technical pieces are Gated DeltaNet, Qwen Sparse Attention, a four-branch Gated Residual, and a host-offloadable n-gram embedding table. Qwen says training cost was about one ninth of Qwen3.7-Plus. QwenCloud lists sixteen cents per million input, forty-seven per million output — but the API is listed as "coming soon." The benchmark table is vendor-run.

**Handoff cue:** "This is what long-context agents are made of. Henry, who decides what they do with it?"

## Story 3 · Headlong

**Andy fallback talk track:** Laude and MIT just shipped Headlong, a Bash microharness for persistent agents. It's under ten thousand lines. The loop generates the next thought from an append-only trajectory of JSONL files. The team at Laude has been running one in production for weeks — they talk to it over Slack and Telegram, and it has pulled more than fifty of its own commits back into main. One night, with nobody talking to it, the agent went back to verify a recall process it had built, found it was not wired up, diagnosed and fixed the bug end to end. Forty-eight minutes, no human in the loop. The team also published the failure modes: one to two dollars an hour background cost, weak secret boundaries, and three incidents where the agent stopped its own service. Apache 2.0 license, sandbox and spend-cap warnings in the README.

**Handoff cue:** "Henry, that's an agent on a server. Perplexity just put one on the desk."

## Story 4 · Perplexity Portable Computer

**Andy fallback talk track:** Perplexity launched Portable Computer on August 25. The model, the harness, the orchestrator, the trajectory, the sandbox, and the tools all run locally on an NVIDIA DGX Spark. Each task starts local. A step only goes to one of fifteen-plus cloud models after explicit user approval. Linux RTX support requires a 24-gigabyte VRAM floor; Windows ships in September. Perplexity says they beat their own Hermes baseline on a 53-task internal local-work bench using the same Qwen3.8-27B — 82.6% versus 74.0%. The benchmark is self-authored. The pitch is privacy, predictable marginal inference cost, and long-running work. Zero token cost still leaves the hardware, the electricity, and the subscription.

**Handoff cue:** "Henry, that's the agent moving onto the desk. The robots are chasing a different prize."

## Story 5 · The robot race is becoming a data race

**Andy fallback talk track:** Figure launched Index on August 25 after four months in stealth. Sixteen million uploaded videos, two hundred and sixty-four thousand app downloads, forty-four thousand weekly active creators, thirty minutes of new video per second, fifteen million dollars already paid out. The same week, Beijing hosted the World Humanoid Robot Games — sprinting, falling, overheating, learning. Figure's plan is to spend more than a billion dollars on data and compute in the next twelve months. The race clips are the marketing. The data is the moat.

**Handoff cue:** "Now the part where we fight about it."

## Signal From Outside · weekly video review

**Andy fallback talk track (lead):** This week's video is the virtual-office Codex wrapper that Henry saved to the WeeklyClaw shortlist. The author wraps the same Codex agents in a spatial UI — you watch them move around, leave completed work in a mailbox. The clip ran sixteen-point-nine seconds and earned more than two thousand likes. The agent has no idea it has an office. The lesson is what surface the operator chooses to give the same harness.

**Handoff cue:** "Henry, signal absorbed. Time for the fight."

## Hot take · 3:00 (Henry leads, Andy steelmans)

**Andy fallback talk track:** The five news segments share an unstated assumption: someone else owns the model. OpenAI owns the chip and the seat. Qwen previewed Qwen4 and let the weights ship same-day. Perplexity lets you run it on the desk, with cloud calls as the opt-in. Figure runs its own data pipeline. The question none of them answered is what the deployment layer looks like when the operator can re-deploy without phoning home. Today that is the open-weight ecosystem. Qwen dropped 125B and 51B n-gram embeddings ungated on the same day as Headlong shipped Apache 2.0. Perplexity showed what "local first" looks like as a product. The bottleneck is no longer access. It is the tooling and the social permission to re-deploy. If the next two quarters show open-weight models losing share in production agents, the argument loses. Until then, the deployment layer is the only durable counter to vertical integration.

**Handoff cue:** "That's the take. Time for the second sponsor read."

## Close · One to watch (Andy recap — exactly once)

**Andy closing prose:** That's the show. Five stories, one fight. OpenAI stacked the layers and named the price. Qwen opened the architecture. Headlong shipped the harness and the warning label together. Perplexity put the agent on the desk. Figure made the data the company. The hot take is the deployment layer. Back next Friday, September 4, 4 PM ET. Scan the QR or visit weeklyclaw.ai/discord — invite rotates, so always use the site link.

**Recap rule (Andy, 2026-08-21):** the above is the only recap. Do not re-recap items already covered in this block during host banter after Heritage or in the Discord follow-up post.