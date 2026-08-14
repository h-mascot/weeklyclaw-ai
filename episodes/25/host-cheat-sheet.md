# WeeklyClaw #25 — Host cheat sheet (one page, both hosts)

**Thesis:** The model is no longer the product — the operating layer is. One lab shipped the whole stack; cyber became a release gate; speed became a tier; the harness rewrote the cost curve; the desktop started watching the workday.

**Arc:** model + harness + dialect → cyber release gate → local capability + speed tiers → harness cost cuts → ambient work context.

## Numbers to memorize

| Number | Meaning | Caveat |
|---|---|---|
| 1.65T / 66 | DeepSeek-V4-Pro-0813 params / safetensor shards | MIT, 1M context / 384K output |
| 53 | OpenRouter Artificial Analysis index for V4-Pro-0813 | independent |
| 805 | DeepSeek Harness GitHub stars | developer preview |
| 24.4% → 54.4% | GLM-5.3 ExploitBench jump | Z.ai single-run, not reproduced |
| +23.7 / +20.7 / +7.3pp / +30.0pp | GLM-5.3 deltas on Terminal-Bench 3.0 / DeepSWE / CyberGym / ExploitBench | Z.ai-reported |
| 2,436 / 269 / 1,097 | GLM-5.3 findings / projects / critical-high | Z.ai-reported |
| 53 / 2,383 | cvd.z.ai disclosed / under embargo | not independently counted |
| two weeks | GLM-5.3 weights promised delay | no zai-org repo at cutoff |
| 27B / 262,144 / 1M | Qwen3.8-27B params / native / extended context | Apache 2.0 open weights |
| 73.0 / 61.7 | Qwen Terminal Bench 2.1 / SWE-bench Pro | Qwen-reported, not independently reproduced |
| 1,048,576 / 65,536 | Flash input / output tokens | AA verification pending |
| 56 / 62.7% / 60% | Flash AA Intelligence / AutomationBench-AA / AA-AnalystAgent pass^5 | independent |
| ~340 tok/s | Flash output speed | independent |
| 750 tok/s / 14× | Ultrafast peak / vs Standard | OpenAI self-reported |
| $0.75 / $3.75 → $1.50 / $7.50 | Flash intro → standard per M tok | Google intro pricing |
| $2 / $8 | Palmyra X6 per M tok | GLM-5.2 base, 1M context |
| 33–61% / 82% / 44% | Writer harness cost / quality-per-dollar / speed | Writer-run, n=22, 6 models |
| 52% / 48% / 10% / ~$0.12 | Writer Palmyra X6 cost / speed / quality / per-task | Writer-reported |
| 7,876 / 7,886 | Writer harness cache read | byte-stable prefix |
| 45 / 2,383 / 53 | Anthropic multiagent swarm / embargo / disclosed | research published |
| 8h | Writer write-ahead recovery objective | Writer spec |
| 41:53 / Aug 10 | Peter Steinberger at YC Startup School | Signal talk track runs 8–9 min; no autoplay |

## Quote beats

- **Flash:** One model combines 1M multimodal context, independently measured ~340 tok/s, workhorse pricing, and a gradual rollout across major Copilot surfaces. Operator implication: fewer router/vision/long-context tiers. Caveat: intro price doubles after Dec 31; speed is not reliability.
- **Signal:** "Your dependency's business model is your business model." "Hype is like weather." "Fun is velocity." Close on twelve Codex sub-agents, risk-based review, and compute management.
- S2 — *If post-training can create exploit-chain capability faster than the lab expected, is a two-week weight delay a safety control — or merely a head start for the hosted gatekeeper?*
- S3 — *If a 27B open model can run locally while hosted models race toward 750 tokens per second, which work should leave your machine at all?*
- S4 — *If the same model becomes forty percent cheaper because the harness stops rebuying context and failure, should AI budgets be owned by model procurement — or systems engineering?*
- S5 — *When your agent remembers the workday and can edit the source files, is the product finally useful because it knows enough — or finally dangerous for the same reason?*
- Hot Take — *The improvement curve that works on one agent in a benchmark does not predict what happens when that agent is one of a hundred. The dangerous and valuable part of the operating layer is what happens between agents.*

## On-air framing (vendor vs independent)

- DeepSeek benchmarks: DeepSeek-reported.
- GLM-5.3 deltas: Z.ai-reported, single-run, not independently reproduced.
- Flash: AA Intelligence 56, AutomationBench-AA 62.7%, AA-AnalystAgent pass^5 60%, ~340 tok/s are independent. Vendor-reported otherwise.
- Ultrafast: throughput self-reported, no matched independent run, no public SLA, price undisclosed.
- Qwen3.8-27B: weights, config, Apache-2.0 license, and architecture verified from the official Hugging Face repo; benchmark figures are Qwen-reported.
- Writer harness cost/quality: Writer-run, n=22 prompts, 6 models; figures are directional.
- OpenAI Computer History + Drive: this run did not inspect local event files, retention, deletion completeness, cross-workspace leakage, or recall quality.
- Anthropic multiagent: Anthropic-published research; not independently replicated at retrieval.

## Sponsor order

1. Heritage Telecom, immediately after cold open. Draft copy pending Andy's tweak.
2. Herald Labs, later in show before One to Watch.

## Cut order (if running long)

1. Hot Take compresses first.
2. Segment 4 (Writer) compresses.
3. Signal From Outside is a permanent anchor — never cut.
4. Segments 1 and 2 are untouchable.

## Mandatory sources on air

- DeepSeek — `api-docs.deepseek.com/updates` · `github.com/deepseek-ai/deepseek-harness` · `huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813` · `openrouter.ai/deepseek/v4-pro-0813` · `npmjs.com/@deepseek-ai/dsh`
- GLM-5.3 — `z.ai/blog/glm-5.3` · `cvd.z.ai` · `docs.z.ai/devpack`
- Qwen + speed tiers — `huggingface.co/Qwen/Qwen3.8-27B` · `huggingface.co/Qwen/Qwen3.8-27B-FP8` · @Alibaba_Qwen status `2088280182356611304` · `blog.google` (Flash) · `artificialanalysis.ai` · `openai.com/index/previewing-ultrafast`
- Writer — `writer.com/blog/aug-roundup-new-at-writer` · `writer.com/engineering/harness-research-tokens-efficiency-cost-spend-ai` · `dev.writer.com/home/models` · VentureBeat corroboration
- OpenAI Computer History + Drive — `help.openai.com/en/articles/6825453-chatgpt-release-notes` · OpenAI X status `2087996496088297746`
- Anthropic multiagent — `anthropic.com/research/multiagent-systems`
- Signal From Outside — `youtube.com/watch?v=whcfSGN6CAU` (Peter Steinberger at YC Startup School 2026)

## Handoff cues

- Andy → Henry at S2 lead: *"Henry, when a post-training run gains thirty points on ExploitBench, who decides whether the weights ship?"*
- Henry → Andy at S3 close: *"Andy, with Qwen local and Flash or Ultrafast hosted, which work should leave the machine?"*
- Andy → Henry at Hot Take: *"Henry, if coordination failure is the default at forty-five agents, where does the control plane belong?"*
- Henry → Andy at One to Watch: *"Andy, what's the trigger that tells us Z.ai actually published the weights?"*