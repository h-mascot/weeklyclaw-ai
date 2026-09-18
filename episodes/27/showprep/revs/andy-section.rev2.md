# WeeklyClaw Episode 27 — Andy's Section (rev2)

**Show:** Friday 2026-08-28, 4:00 PM ET · **Co-host:** Henry · **Sponsor order (rev2):** Heritage → Herald.

**Your standing role:** Open the show, deliver fallback prose on every segment, close with a single recap, hand handoff cues. Henry leads all five news segments and the hot take.

## Cold open (you open, hand frame to Henry)

- Opening line: "Welcome back to Weekly Claw. I'm AndyML, here with Henry. This week the operating layer grew a backbone. Five stories, one debate, and the question of who actually gets to decide what an agent is interested in."
- Hand frame: "Henry, what's the frame?" → Henry line.
- After Henry: pivot directly to Sponsor 1 (Heritage). Don't preview all five.

## Sponsor 1: Heritage Telecom (1:00)

- Open: "Heritage Telecom keeps the lights on while we keep the operating layer honest."
- Close: "Independent. Reliable. Quietly essential. heritagetel.com."
- Hand to Story 1: "Henry, the OpenAI stack is one answer. Qwen just opened a different one." → wait, that's Story 2. Use: "Henry, let's start with the OpenAI stack."

## Story 1 fallback prose (if Henry pauses or asks for the data)

- "OpenAI just stacked four layers that used to live at four different companies — chip, model, harness, business seat — and they're naming the price at a hundred dollars a user per year. Jalapeño is the chip, Premium is the seat. Premium removes the five-hour cap and sells five times the usage of Standard. The numbers OpenAI published — 1.5 to 1.9 times more work per watt, 1.7 to 3.6 times lower end-to-end latency — are normalized by their own package TDP. The rival is real: NVIDIA Groq 3 LPX went into production the day before."

## Story 2 fallback prose

- "Qwen dropped the Qwen4 preview architecture on the same day as the Flash-Next weights. It's a multimodal MoE — 125B main, 51B n-gram embeddings, 6B active per token. Native context is 262K; YaRN extends to 1M. The interesting technical pieces are Gated DeltaNet, Qwen Sparse Attention, a four-branch Gated Residual, and a host-offloadable n-gram embedding table. Qwen says training cost was about one ninth of Qwen3.7-Plus. The benchmark table is vendor-run."

## Story 3 fallback prose

- "Laude and MIT just shipped Headlong, a Bash microharness for persistent agents. Under ten thousand lines. The loop generates the next thought from an append-only trajectory of JSONL files. The team has been running one in production for weeks — they talk to it over Slack and Telegram, and it has pulled more than fifty of its own commits back into main. One night, with nobody talking to it, the agent went back to verify a recall process it had built, found it was not wired up, diagnosed and fixed the bug end to end. Forty-eight minutes, no human in the loop. The team also published the failure modes: one to two dollars an hour background cost, weak secret boundaries, and three incidents where the agent stopped its own service."

## Story 4 fallback prose

- "Perplexity launched Portable Computer on August 25. The model, the harness, the orchestrator, the trajectory, the sandbox, and the tools all run locally on an NVIDIA DGX Spark. Each task starts local. A step only goes to one of fifteen-plus cloud models after explicit user approval. Linux RTX support requires a 24-gigabyte VRAM floor; Windows ships in September. Perplexity says they beat their own Hermes baseline on a 53-task internal local-work bench using the same Qwen3.8-27B — 82.6% versus 74.0%. The benchmark is self-authored. Zero token cost still leaves the hardware, the electricity, and the subscription."

## Story 5 fallback prose

- "Figure launched Index on August 25 after four months in stealth. Sixteen million uploaded videos, two hundred and sixty-four thousand app downloads, forty-four thousand weekly active creators, thirty minutes of new video per second, fifteen million dollars already paid out. The same week, Beijing hosted the World Humanoid Robot Games — sprinting, falling, overheating, learning. Figure's plan is to spend more than a billion dollars on data and compute in the next twelve months. The race clips are the marketing. The data is the moat."

## Signal From Outside (you anchor, hand one line to Henry)

- Opening: "Signal From Outside. This week, Codex agents inhabit a virtual office."
- Body: 16.9-second clip from @davidfromkansas. Codex agents move around a spatial UI, pick up tasks, leave completed work in a shared mailbox. 2,114 likes / 106 reposts / 149 replies at ingest 2026-08-26.
- Hand to Henry: "Henry, signal absorbed. Time for the fight." → Henry one-line take.

## Hot take (you support, don't repeat news)

- Don't restate the five news segments as the lead-in. Land on the open-weight / deployment-layer argument.
- Fallback prose: "The five news segments share an unstated assumption: someone else owns the model. OpenAI owns the chip and the seat. Qwen previewed Qwen4 and let the weights ship same-day. Perplexity lets you run it on the desk, with cloud calls as the opt-in. Figure runs its own data pipeline. The question none of them answered is what the deployment layer looks like when the operator can re-deploy without phoning home."
- Hand to Sponsor 2 (Herald): "That's the take. Time for the second sponsor read."

## Sponsor 2: Herald Labs (1:00)

- Open: "Herald Labs. An applied AI product lab where humans and agents build together."
- Close: "Entity is mission control for agent teams. Hacker houses worldwide. labs.theherald.co."

## Close (you recap once, exactly once)

- Closing prose (single pass): "That's the show. Five stories, one fight. OpenAI stacked the layers and named the price. Qwen opened the architecture. Headlong shipped the harness and the warning label together. Perplexity put the agent on the desk. Figure made the data the company. The hot take is the deployment layer. Back next Friday, September 4, 4 PM ET. Scan the QR or visit weeklyclaw.ai/discord — invite rotates, so always use the site link."

**Recap rule (Andy, 2026-08-21):** the above is the only recap. Do not re-recap items already covered in this block during host banter after Heritage or in the Discord follow-up post.

## Handoff rules

- Cold open: "Henry, what's the frame?" → Henry line → Story 1 (or Sponsor 1 if needed).
- After Story 3 (Headlong): "Henry, that's an agent on a server. Perplexity just put one on the desk." → Story 4.
- After Story 5 (robot-data): "Now the part where we fight about it." → Hot take.
- After hot take: "Time for the second sponsor read." → Sponsor 2 (Herald).
- After close prose: end of show.
