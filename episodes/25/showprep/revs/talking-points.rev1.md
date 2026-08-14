# WeeklyClaw #25 — Talking points (one page, both hosts)

## Thesis

**The model is no longer the product — the operating layer is.** DeepSeek shipped weights, harness, and API dialect together. Z.ai delayed its own weights after a post-training run gained exploit-chain capability. Speed became a service tier. The harness rewrote the cost curve. The desktop started watching the workday.

## Arc

model + harness + dialect → cyber release gate → speed as a tier → harness cost cuts → ambient work context.

## Numbers to memorize

| Number | Meaning | Caveat |
|---|---|---|
| 1.65T / 66 shards | DeepSeek-V4-Pro-0813 params / safetensor shards | MIT, 1M context / 384K output |
| 53 | OpenRouter Artificial Analysis index for V4-Pro-0813 | independent, not harness-matched |
| 805 | GitHub stars on DeepSeek Harness at retrieval | developer preview |
| 24.4% → 54.4% | GLM-5.3 ExploitBench jump | Z.ai single-run, not reproduced |
| +23.7 / +20.7 / +7.3pp / +30.0pp | GLM-5.3 deltas vs GLM-5.2 on Terminal-Bench 3.0 / DeepSWE / CyberGym / ExploitBench | Z.ai-reported, single-run |
| 2,436 / 269 / 1,097 | GLM-5.3 findings / projects audited / critical-high | Z.ai-reported |
| 53 / 2,383 | cvd.z.ai disclosed / under embargo at retrieval | not independently counted |
| two weeks | GLM-5.3 weights promised delay | no zai-org GLM-5.3 repo at cutoff |
| 1,048,576 / 65,536 | Flash input / output tokens | independent AA verification pending |
| 56 / 62.7% / 60% | Flash AA Intelligence / AutomationBench-AA / AA-AnalystAgent pass^5 | independent |
| ~340 tok/s | Flash independent output speed | independent |
| 750 tok/s / 14× | Ultrafast peak / vs Standard | OpenAI self-reported, no matched independent run |
| $0.75 / $3.75 → $1.50 / $7.50 | Flash intro through Dec 31, then standard | Google intro pricing |
| $2 / $8 | Palmyra X6 per M tok | GLM-5.2 base, 1M context |
| 33–61% / 82% / 44% | Writer harness cost / quality-per-dollar / speed | Writer-run, n=22, 6 models |
| 52% / 48% / 10% / ~$0.12 | Writer Palmyra X6 cost / speed / quality / per-task | Writer-reported |
| 7,876 / 7,886 | Writer harness cache read | byte-stable prefix |
| 45 / 2,383 → 53 disclosed | Anthropic multiagent swarm / embargo vs disclosed counts | research published |
| 8h | Writer write-ahead recovery objective | Writer product spec |
| ~46 min / May 29 | IBM Mixture of Experts podcast (Signal From Outside) | permanent anchor, no autoplay |

## Frame hooks (verbatim)

1. **DeepSeek** — `DeepSeek-V4-Pro-0813 went GA with 1M context, 384K output, Responses + Anthropic API dialects, and an MIT harness published the same day.`
2. **Z.ai** — `Z.ai delayed GLM-5.3 weights two weeks after the same post-training pushed ExploitBench from 24.4% to 54.4%.`
3. **Speed tier** — `OpenAI's Ultrafast promises up to 750 output tokens/sec on GPT-5.6 Sol; Google shipped Gemini 3.7 Flash at ~340 tok/s on the same day.`

## Quote beats

- S2 — *If post-training can create exploit-chain capability faster than the lab expected, is a two-week weight delay a safety control — or merely a head start for the hosted gatekeeper?*
- S3 — *If the same frontier model can answer at 750 tokens per second, do agents become real-time collaborators — or do we just create much faster loops that fail before humans can intervene?*
- S4 — *If the same model becomes forty percent cheaper because the harness stops rebuying context and failure, should AI budgets be owned by model procurement — or systems engineering?*
- S5 — *When your agent remembers the workday and can edit the source files, is the product finally useful because it knows enough — or finally dangerous for the same reason?*
- Hot Take — *The improvement curve that works on one agent in a benchmark does not predict what happens when that agent is one of a hundred. The dangerous and valuable part of the operating layer is what happens between agents.*

## Vendor-reported vs independent (on-air framing)

- DeepSeek benchmarks: DeepSeek-reported.
- GLM-5.3 deltas: Z.ai-reported, single-run, not independently reproduced.
- Flash: AA Intelligence 56, AutomationBench-AA 62.7%, AA-AnalystAgent pass^5 60%, ~340 tok/s are independent. Vendor-reported otherwise.
- Ultrafast: throughput self-reported, no matched independent run, no public SLA, price undisclosed.
- Writer harness cost/quality: Writer-run, n=22 prompts, 6 models; figures are directional.
- OpenAI Computer History + Drive: this run did not inspect local event files, retention, deletion completeness, cross-workspace leakage, or recall quality.
- Anthropic multiagent: Anthropic-published research; not independently replicated at retrieval.

## Cut order (if running long)

1. Hot Take compresses first.
2. Segment 4 (Writer) compresses.
3. Signal From Outside is a permanent anchor — never cut.
4. Segments 1 and 2 are untouchable.

## Sources (must read on air)

- DeepSeek — `api-docs.deepseek.com/updates` · `github.com/deepseek-ai/deepseek-harness` · `huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813` · `openrouter.ai/deepseek/v4-pro-0813` · `npmjs.com/@deepseek-ai/dsh`
- GLM-5.3 — `z.ai/blog/glm-5.3` · `cvd.z.ai` · `docs.z.ai/devpack` · `huggingface.co/zai-org` (5.3 not yet present)
- Speed tier — `blog.google` (Flash) · `artificialanalysis.ai` (time chart) · `openai.com/index/previewing-ultrafast` · `ai.google.dev/gemini-api/docs/models/gemini-3.7-flash` · `github.blog` (Copilot rollout)
- Writer — `writer.com/blog/aug-roundup-new-at-writer` · `writer.com/engineering/harness-research-tokens-efficiency-cost-spend-ai` · `dev.writer.com/home/models` · VentureBeat corroboration
- OpenAI Computer History + Drive — `help.openai.com/en/articles/6825453-chatgpt-release-notes` · OpenAI X status `2087996496088297746`
- Anthropic multiagent — `anthropic.com/research/multiagent-systems`
- Signal From Outside — `youtube.com/watch?v=wVdivlahcm0` (IBM Mixture of Experts)