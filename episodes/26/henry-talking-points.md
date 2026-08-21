# WeeklyClaw #26 — Henry section (own slides + shared transitions only)

Henry's on-air material is concise bullets, an optional line, and a handoff cue. He does not read a word-for-word script.

## Cold open (shared with Andy)

- Optional landing line: "Here's the frame: speed, routing, payments, supervision, and licensing thresholds are no longer features — they are the moat. Andy, which work should leave the machine now?"
- Handoff: Andy → Herald Labs sponsor.

## s-the-map

- Five-card deployment chain: license thresholds, supervisory judgment, wall-clock budget, gateway ownership, spend boundary.
- Cut order: Segment 4 first, then 5, then the hardware side of 3. Signal From Outside stays. Cold open stays. S1 and S2 untouchable.
- Handoff: "Start with the lab that shipped a 4.89 terabyte checkpoint and a $50 million license cliff in the same release."

## s-seg-qwen-open (Henry lead, Andy caveat)

- 2.446T BF16 parameters; 95B active per token; 92 layers; 512 routed experts.
- 262,144 native context extensible to ~1.01M.
- Repository is ungated, 224 files, ~4.89 TB; 6,381 downloads and 950 likes at retrieval.
- The downloadable release is text-only with mandatory reasoning.
- Hosted Qwen3.8-Max adds vision, non-thinking, tools, default 1M context.
- Threshold A (100M MAU or $20M monthly revenue): prominent model naming.
- Threshold B ($50M revenue in any consecutive 12-month period for model-service or AI work-assistant companies): separate Qwen license.
- OpenRouter lists the route at $2 input / $6 output per M tokens, mandatory reasoning.
- Caveat: vendor-run benchmarks, custom license, no Apache 2.0.
- Optional landing line: "A 4.89 terabyte checkpoint can be inspectable and modifiable yet still economically centralized."
- Question: "If the weights are downloadable but require five terabytes, serious inference infrastructure, and a separate license once your AI assistant reaches $50 million, did frontier capability become open — or merely inspectable?"
- Handoff (to Andy caveat): "And the license cliff."

## s-seg-faraday (Henry lead, Andy support)

- 27B supervisor, post-trained on Qwen3.6-27B, calls GPT-5.5 Codex as a coding worker.
- Replica: 310 tasks across 100 ML/AI-for-science papers; 242 train / 68 test.
- Each agent: 60 minutes, internet, 1/7 H200 GPU.
- Beats Claude Opus 4.8 and GPT-5.5 on 60% of held-out AI-for-science tasks; +6% Claude / +8% Codex on test split.
- Human experts preferred Faraday in 29 of 41 selected rollouts.
- Same Codex model serves as rubric judge.
- Caveat: author-run, no public weights, selected human study.
- Henry recap beats: small model + judgment + the same Codex judge — the comparison is not "27B vs frontier."
- Optional landing line: "If that transfer holds beyond one author-built benchmark, model routing becomes an org chart rather than a leaderboard."
- Question: "If a 27B supervisor can direct a model two orders of magnitude larger, should we spend the next dollar on a smarter worker — or on training the judgment that decides what the worker should do?"
- Handoff: "After the break: Signal From Outside."

## s-seg-speed (Henry lead, Andy DFlash 2)

- CS-4: three WSE-3 Turbo wafers, 750 PFLOPS, 129.6 PB/s memory bandwidth, 7.2 Tb/s I/O, 2 μs wafer-to-wafer latency.
- Cerebras claims >4,400 tok/s/user on GPT-OSS-120B, up to 30× production GPU, up to 10× CS-3/W. First shipments this quarter.
- DFlash 2: selector + local convolution; Qwen3.8-27B drafter 4.80 accepted tokens vs 4.28 native MTP.
- 2.7–3.4× SGLang throughput vs autoregressive; 16–25% more accepted output per verification pass at ~1% extra cycle latency.
- Drafter weights live on HF under Apache 2.0; vLLM + llama.cpp PRs open.
- Henry M5 128 GB Mac Pro: 76.8 tok/s, configuration-specific, host testimony.
- Caveat: vendor-reported throughout.
- Optional landing line: "A faster run can spend the same wall-clock budget on deeper search, verification, or parallel work."
- Question: "If an agent gets 30 times more tokens in the same minute, should we make the answer arrive faster — or spend the entire gain on more checking before anyone sees it?"
- Handoff: Andy opens Signal From Outside.

## s-seg-agent-payments (Henry lead, Andy BNB)

- AWS AgentCore Payments: preview → GA on 2026-08-18.
- Agents discover and pay via x402 or Stripe/Tempo MPP.
- Coinbase + Stripe Privy stablecoin wallets; raw credentials in AgentCore Identity Secrets Manager; short-lived tokens instruct wallet ops.
- Per-session max spend + expiry below the agent loop; x402 `upto` for metered usage.
- CloudWatch logs, spans, dashboards.
- BNB Altana: scoped session keys carry spending limits, allowlists, time bounds registered onchain; revocable without giving the agent the private key.
- Two designs: AWS = managed logs + policy; BNB = onchain permissions + self-custody.
- Caveat: no transaction attempted, no wallet funded; BNB onchain claims not independently audited.
- Optional landing line: "Probabilistic reasoning proposes a purchase; deterministic infrastructure decides whether money can move."
- Question: "When an agent can pay for the next API call without asking, which layer should own the veto — the model, the workflow, the wallet, or a policy the agent cannot rewrite?"
- Handoff: "Hot take: same question, different artifact."

## s-hot-take (Henry anchor, Andy steelman)

- Anthropic watermark changes the source of randomness in low-stakes word choices.
- Long passages get statistically consistent with a secret key.
- Exact facts, code, proofreading, heavy edits leave little room for a mark.
- Translation is more markable because Claude chooses every word.
- Positive result = Claude likely processed some of the content, not that Claude authored it.
- Detector API: "coming soon"; no false-positive curve published.
- C2PA file credentials are a separate path.
- Henry's three-beat close:
  1. Detection is not authorship.
  2. The model becomes the new plausible deniability.
  3. The defensible posture is signed receipts — content-keyed, hash-chained — not a watermark guess.
- Optional landing line: "What decision is the detector safe enough to make?"
- Handoff: "Andy, that's the operating layer beneath the watermark."

## s-sponsor-heritage (Henry owns)

- "Heritage Telecom keeps the lights on while we keep the operating layer honest. Independent infrastructure for independent voices. Independent. Reliable. Quietly essential. Back to One to Watch."

## Notes for Henry across the show

- "Henry says" is the rule for vendor-reported figures, author-run benchmarks, and host testimony. Always attach the source tier.
- S1 license thresholds are the segment's editorial core — name them both before any benchmark number.
- S3 should always read as wall-clock budget, not tokens-per-second vanity.
- S5's most quotable line is the AWS receipt's three-times-read sentence: "the model never holds the key."
- Hot Take's production-layer fix (signed receipts) is the segment's defensible landing — hold it regardless of the steelman's pushback.