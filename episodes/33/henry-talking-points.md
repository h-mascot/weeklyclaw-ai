# Episode 33 — Henry's Sections

Everything Henry owns on air: Grid A, the SFO bridge, Grid B, the hot-take proposition, and One to Watch.

## Grid A — "The trillion-parameter open-weight promise" (8:00)

**Card 1 — Mistral Large 4 "Le Chonk"**
- Numbers: 1T total, 52B active, natively multimodal. Preview API: $1.36/M in, $4.18/M out — Mistral's page and Artificial Analysis agree. AA Intelligence Index 38 (median 26). Verbosity: 200M eval output tokens vs 81M median — "very verbose" per AA. Weights: end of October, red-teaming until then.
- Landing line: "Mistral says it surpasses frontier closed models. The independent index says 38 against a median of 26. Both things are on the same page — that's not a dunk, that's a preview."
- If asked about the name: "Le Chonk is Mistral's own name for it — 'unofficially ML4, very officially: le Chonk.'"

**Card 2 — Reflection Beam**
- Numbers: 501B total, 23B active, sparse MoE, built for agentic coding. Announced Oct 5. Weights + tech report + model card "later this month"; early access is invite-only.
- Landing line: "Second trillion-scale preview in one week, and the benchmark chart on screen is Reflection's own. I'll run it the day weights land — until then this is a promise with a logo on it."

**Card 3 — OpenAI 722 manuscripts**
- Numbers: 722 papers, 372 result families, 235 with Lean formalizations, Apache-2.0, zero peer review. One-night dump. Includes a solution to the Unitary Synthesis Problem (posed by Aaronson and Kuperberg, 2007).
- Landing line: "The largest math drop in history, unrefereed, under an open license, from a model OpenAI still hasn't named. Peer review just got a volume problem."

**Card 4 — The math reception**
- Numbers: Williams–Alman, arXiv 2610.06783, submitted Oct 5: deterministic 3SUM in n^1.9992, APSP in n^2.9995 — refutes the 3SUM and APSP hypotheses. Human authors. Same week.
- ON AIR ACTION: open scottaaronson.blog/?p=9137 manually BEFORE quoting Aaronson; Tao's thread per curator receipt — both Cloudflare-gated/unverified this build.
- Muse Spark name-drop (one line): "And in plain chat, no scaffold — Muse Spark co-authored six papers this month, five of them solving open problems."
- Landing line: "The 722 needed an answer, and the field answered the same week — with a refutation of fifty-year-old conjectures, typed by humans."

## SFO bridge (after Theo's clip, ~40s)
- "Theo's whole point is tokens-per-second is a meaningless metric — and he's right, because the bill doesn't read tokens per second. It reads tokens per task. My own numbers this week: Haiku 5.5 maxes around 162K output tokens per task; GPT-6 Luna around 50K. Same job, three times the tokens, three times the bill. Ultrafast is the same tax with a nicer interface. The harness is the product. The model is a line item."

## Grid B — "Agents get graded, routed, and locked down" (8:00)

**Card 5 — ThinkingBox**
- Numbers: 121,680 valid trials, 12 models, 79,853 failed — two-thirds. Microsoft + Hugging Face; paper 2608.19741.
- Quote: "An agent can sound correct while leaving the wrong value, changing the wrong record, or creating an extra side effect. Only the records it leaves behind settle the question."
- Landing line: "Grading the database, not the demo. Twenty times in a row is the actual bar."

**Card 6 — ReviewBench**
- Numbers: 103.9M pull requests, live leaderboard, grounded and augmented precision/recall, research preview, submissions open.
- Landing line: "Two agent benchmarks shipped the same week — the measurement layer is being built in public, right on schedule."

**Card 7 — Grok Bot routing**
- Verbatim: "Going forward, @SpaceX will use the best back end model for any given task, including Claude Opus 5.5, MidJourney, Suno and other leading APIs. Whatever is most likely to give you the best outcome." Oct 7. 106.1K likes.
- Landing line: "The loudest model-lock founder just conceded the harness wins. Route to the best model per task — that's been this show's benchmarking thesis since episode one."

**Card 8 — Apple Full Disk Access**
- Numbers: Oct 2 developer update; per-app user prompts replace silent FDA paths; Apple's own text cites autonomous agents sidestepping controls.
- Landing line: "When Apple writes OS policy because of your industry, your industry arrived. Agents are now a threat model — treat them like one."

## Hot take proposition (2:00)
- "The free-compute era ended on schedule — and that's healthy. Tomorrow, Gemini's free tier locks to 3.5 Flash-Lite. October 30, OpenAI halves Pro 200 — 20x to 10x Plus on Work and Codex, GPT-6 Pro chat from 200 to 100 a week — same $200. My line: with 6.1 you get 2.5x more usage on the new 10x plan. Prices are finally telling the truth about inference. Everyone who learned on subsidies now has to build unit economics that survive contact with a real bill. That's not the apocalypse; that's graduation."

## One to Watch (1:15)
- "Tomorrow — October 10 — Alibaba retires every third-party model from Model Studio. 100-plus models, four waves, 60-plus snapshots. DashScope migrations break Saturday morning. The irony writes itself: DeepSeek-V4.1-Flash is now served on rival Qwen's consumer platform while Alibaba delists everyone else's. Platform neutrality, one direction only. And set a reminder for the free tier: if retention holds after tomorrow's Flash-Lite lock, the subsidy was never load-bearing."

## Sourcing notes for Henry
- Mistral facts: mistral.ai/news/mistral-large-4 + artificialanalysis.ai/models/mistral-large-4 (both opened this build).
- Beam: reflection.ai/beam (self-reported chart on screen).
- 722: github.com/openai/math. Williams–Alman: arxiv.org/abs/2610.06783.
- ThinkingBox: huggingface.co/blog/microsoft/thinkingbox + arxiv.org/abs/2608.19741.
- Musk post: x.com/elonmusk/status/2107724314451878104 (verbatim verified 2026-10-08).
- Apple: developer.apple.com/news/?id=101stbvu.
- Tier changes: 9to5google.com/2026/10/03/gemini-model-limits-oct-26/ + help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers.
- DashScope: therouter.ai Oct-2026 sunset guide + nfero.com listing.
