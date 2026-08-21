# Henry — Week 26 prep (rev4)

## Cold open · 2:00

- "Here's the frame: speed, routing, payments, and supervised judgment are no longer features — they are the moat. Andy, which work should leave the machine now?"
- "Start with the lab that shipped a 4.89 terabyte checkpoint and a $50M license cliff in the same release." → revise to "Start with the lab that trained a 27B supervisor to direct GPT-5.5." (Qwen off this week's lineup per Henry's standing rule.)
- "Four stories tonight" not five.

## Map · 1:00

- "The map is the deployment chain: supervisory judgment, wall-clock budget, gateway ownership plus an unattributed ghost, spend boundary. Qwen's Max-class checkpoint aired on Episode 25, so it is off this week's lineup by Henry's standing rule. If we run long, Segment three compresses first. Signal From Outside stays. Segments one and two are untouchable."

## S1 — Faraday · ~5:30 (lead)

- "Inherent's Faraday, post-trained on Qwen3.6-27B, builds a scientific agent that can call GPT-5.5 Codex as a coding worker rather than encoding scientific workflow in a large hand-built multiagent harness."
- 310 figure-replication tasks across 100 ML and AI-for-science papers. 242 training, 68 test.
- Each agent: one figure redacted, 60 minutes, internet, 1/7 H200.
- Faraday uses five ordinary tools plus a resumable Codex CLI wrapper. Can reset or parallelize coding-agent sessions.
- Long-horizon GRPO + per-task rubrics + three judge samples + turn-level credit assignment.
- Faraday beats Claude Opus 4.8 and GPT-5.5 on 60% of held-out AI-for-science tasks. Averages 6% above Claude, 8% above Codex on the test split.
- Human experts preferred Faraday over both in 29 of 41 selected rollouts.
- Same Codex model serves as the rubric judge. The 27B does not outperform the frontier model alone — it outperforms it by calling it.
- "If a 27B supervisor can direct a model two orders of magnitude larger, should we spend the next dollar on a smarter worker — or on training the judgment that decides what the worker should do?"
- Sources: arxiv.org/abs/2608.13331 · arxiv.org/html/2608.13331v1 · x.com/inherent_labs/status/2088290794092298655
- Caveat: author-run; selected human study; no public weights, training code, or Replica dataset.

## S2 — Speed · ~5:30 (lead)

- "Agent intelligence is now constrained by wall-clock time as much as model quality."
- CS-4 = three WSE-3 Turbo wafers. 750 PFLOPS. 129.6 PB/s. 7.2 Tb/s I/O. 2 µs wafer-to-wafer. 4,400+ tok/s/user on GPT-OSS-120B. 30× GPU. 10× CS-3 per watt. First shipments this quarter. **Vendor-reported.**
- DFlash 2: selector + local convolution. Lossless rejection sampling. 4.80 accepted vs 4.28 MTP vs 3.62 DSpark. 2.7–3.4× SGLang throughput. 16–25% more accepted output per verification pass for ~1% extra cycle latency. Apache 2.0. vLLM and llama.cpp PRs still open.
- M5 128 GB Mac Pro: 76.8 tok/s. Configuration-specific.
- "If an agent gets 30 times more tokens in the same minute, should we make the answer arrive faster — or spend the entire gain on more checking before anyone sees it?"
- Sources: cerebras.ai/cs4 · investors.cerebras.ai · x.com/cerebras/status/2089870131291943228 · inco.ai/blog/dflash2 · huggingface.co/incoai/Qwen3.8-27B-DFlash2 · github.com/vllm-project/vllm/pull/52816 · github.com/ggml-org/llama.cpp/pull/27342
- Caveat: all speed numbers vendor-reported or configuration-specific.

## S3 — Stripe–OpenRouter + Ox Alpha · ~5:00 (lead)

- "Both companies posted on August 19. Stripe's newsroom announcement says it has agreed to acquire OpenRouter to help businesses optimize token routing and usage."
- Stripe describes a gateway that routes across 400+ models from more than 80 providers.
- OpenRouter's same-day post: "joining Stripe," "same mission, same name, same product, same roadmap." Quote the neutrality line verbatim on air.
- 10T+ tokens/day. 10M devs. 10× annual growth. Live API returned 414 catalog entries.
- "Then on August 20 — the same week the router sells — an unattributed ghost shows up on the same rail." Ben Davis reported 80%+ on ten DeepSWE tasks vs 65% Fable / 52% GPT-5.6 Sol. Variance caveat.
- On-air: "unattributed, unverified, ten tasks, take the 80% as signal not score."
- Bloomberg >$7B figure remains anonymous-sourced. Deal signed, not closed — "subject to customary closing conditions. We expect to close in the coming weeks."
- "OpenRouter wrote down 'routing decisions remain driven by what's best for the user' before the deal even closes — what would have to happen for us to say that promise failed?"
- Sources: stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter · openrouter.ai/blog/announcements/openrouter-is-joining-stripe · openrouter.ai/api/v1/models · bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion · openrouter.ai/stealth/ox-alpha · x.com/davis7/status/2090655207831298095
- Caveat: signed, not closed; price undisclosed; terms undisclosed; do not generalize "400+ models from 80+ providers" beyond announcement copy.

## S4 — AgentCore Payments · ~5:00 (lead)

- "AWS Bedrock AgentCore Payments moved from May preview to GA on August 18."
- Agents can discover and pay for APIs, MCP servers, inference, and content through x402 or Stripe and Tempo's MPP.
- Coinbase and Stripe Privy provide stablecoin wallets; raw developer credentials stay in AgentCore Identity Secrets Manager.
- Short-lived tokens. Each session enforces max amount and expiry below the agent loop.
- x402 `upto` ceilings. CloudWatch logs and dashboards.
- BNB alternative: Agent Studio v2 ships Altana wallet with scoped session keys, onchain spending limits, allowlists, time bounds; revocable without giving the agent the private key.
- "When an agent can pay for the next API call without asking, which layer should own the veto — the model, the workflow, the wallet, or a policy the agent cannot rewrite?"
- Sources: aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale · aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga · docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html · github.com/awslabs/agentcore-samples/tree/main/01-features/08-agents-that-transact · bnbchain.org/en/blog/altana-in-bnb-agent-studio-agents-with-limits-you-set
- Caveat: no transaction attempted, no wallet funded; BNB onchain permission claims not independently audited; stablecoin + protocol risks remain.

## Hot Take · ~3:00 (anchor)

- "Hot take, not the news. Anthropic's text watermark changes the source of randomness in low-stakes word choices."
- Long passages get statistically consistent with a secret key.
- Facts, code, proofreading, heavy edits leave little room for a mark.
- Translation is more markable.
- A positive result means Claude likely processed some of the content — not that Claude authored it.
- Detector API "coming soon"; no false-positive curve published.
- "What decision is the detector safe enough to make?"
- Sources: anthropic.com/news/claude-text-watermark · nature.com/articles/s41586-024-08025-4 · digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content

## Heritage Telecom sponsor · 0:30

- "Heritage Telecom keeps the lights on while we keep the operating layer honest."
- "Independent. Reliable. Quietly essential."

## What changed rev3 → rev4

- DROP S1 Qwen (aired pre-show 8/14). Henry standing rule.
- PIN Ox Alpha into S3.
- Renumbered 1–4; cold-open hook reframed; cut order re-prioritized.