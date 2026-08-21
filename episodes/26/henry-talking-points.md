# WeeklyClaw #26 — Henry section (rev6)

Five news segments. Henry leads all five. Cut S5 first if running long.

## s-cold-open (2:00) — Henry

- "It is Friday, August 21. The models barely moved this week. The layer beneath them did."
- Frame: speed, routing, payments, supervised judgment, and the launch-as-chart are the new product surface.
- Handoff (Andy): "Five stories tonight, no benchmark parade. Sponsor first."

## s-seg-faraday (S1, 5:30) — Henry (lead)

- Bullet 1: "Inherent's Faraday, post-trained on Qwen3.6-27B, builds a scientific agent that can call GPT-5.5 Codex as a coding worker."
- Bullet 2: Replica corpus — 310 figure-replication tasks, 242 training, 68 test; 60-minute deadline, 1/7 H200 GPU, internet access.
- Bullet 3: Beats Claude Opus 4.8 and GPT-5.5 on 60% of held-out AI-for-science tasks; +6% over Claude, +8% over Codex; 29/41 human preference.
- Bullet 4: Five ordinary tools plus resumable Codex CLI wrapper. Can reset or parallelize coding-agent sessions. Long-horizon GRPO with per-task rubrics, three judge samples, turn-level credit assignment.
- Landing line (optional): "The 27B does not outperform the frontier model alone — it outperforms it by calling it."
- Handoff (Andy): "Segment two: if the worker is GPT-5.5 and the judge is the same GPT-5.5, who is the audience for the chart?"
- Cut contingency: drop the human study line if running long.

## s-seg-speed (S2, 5:00) — Henry (lead)

- Bullet 1: "Agent intelligence is now constrained by wall-clock time as much as model quality."
- Bullet 2: CS-4 — three WSE-3 Turbo wafers, 750 PFLOPS, 129.6 PB/s memory bandwidth, 7.2 Tb/s I/O, two-microsecond wafer-to-wafer latency.
- Bullet 3: 4,400+ tok/s/user on GPT-OSS-120B, up to 30× production GPU, up to 10× CS-3 throughput per watt. All vendor-reported.
- Bullet 4: Inco DFlash 2 — selector + local convolution, lossless rejection sampling. 4.80 accepted tokens vs 4.28 MTP, 2.7–3.4× SGLang throughput.
- Landing line: "Hardware scale and software drafting, same wall-clock budget. Pick your poison."
- Handoff (Andy): "Segment three: the gateway and the wallet are now one company. The same week, an unattributed ghost mounts the same rail."
- Cut contingency: drop the DFlash 2 software side if running long.

## s-seg-stripe-openrouter (S3, 4:30) — Henry (lead)

- Bullet 1: "Both companies posted on August 19. Stripe's newsroom says it has agreed to acquire OpenRouter."
- Bullet 2: 400+ models, 80+ providers, 10T+ tokens/day, 10M devs, 10× annual inference growth, 414 catalog entries at verification.
- Bullet 3: "joining Stripe, same mission, same name, same product, same roadmap." Neutrality promise written down before the deal closes.
- Bullet 4: Bloomberg's >$7B figure is anonymous-sourced. Deal signed, not closed.
- Bullet 5: Ox Alpha — free, 1M context, mandatory max reasoning, 80% on ten DeepSWE tasks vs 65% (Fable) and 52% (Sol). Ten tasks; signal not score.
- Landing line: "The router got bought. The same week, an unattributed frontier-class ghost showed up on the same rail."
- Handoff (Andy): "Segment five: DeepSeek posted a chart and called it a launch. What did the chart actually prove?"
- Cut contingency: drop the 10T+ tokens stat first; collapse the side-by-side into a single beat.

## s-seg-deepseek (S5, 4:30) — Henry (lead)

- Bullet 1: "DeepSeek shipped a chart. The chart is the launch."
- Bullet 2: ApexBench 36.5, Agents' Last Exam 27.3 > Opus 25.7, Terminal Bench 2.1 83.9, DeepSWE 59.3 — all vendor-reported.
- Bullet 3: No paper, no API, no separate demo. Compare to Faraday (paper-first) and Cerebras (video-first). DeepSeek chose the chart.
- Bullet 4: Read the chart where DeepSeek is ahead — Agents' Last Exam, Terminal Bench 2.1, DeepSWE — and where it trails — ApexBench vs Opus 4.0.
- Landing line: "The benchmark is the receipt. That's a more honest product surface than a paper, or a less honest one. Either way, it's the new default."
- Handoff (Andy): "Segment four: if the launch is the chart, where does the spend boundary live — AgentCore or onchain?"
- Cut contingency: drop the ApexBench 36.5 vs Opus 39.4 row if running long; keep the Agents' Last Exam 27.3 > Opus 25.7 line as the strongest forward claim.

## s-seg-agent-payments (S4, 5:00) — Henry (lead)

- Bullet 1: "AWS Bedrock AgentCore Payments moved from May preview to GA on August 18."
- Bullet 2: x402 + Stripe/Tempo MPP. Coinbase and Stripe Privy stablecoin wallets. Identity Secrets Manager holds raw developer credentials.
- Bullet 3: Each payment session enforces a maximum amount and expiry below the agent loop. x402 `upto` ceilings for metered usage.
- Bullet 4: BNB Agent Studio v2 ships Altana wallet — scoped session keys, onchain limits, revocable without giving the agent the key.
- Landing line: "Two distinct designs. AWS treats the boundary as managed logs and policy; BNB writes it onchain and lets the builder keep the keys."
- Handoff (Andy): "And that's why Signal From Outside lands after the operating layer, not in the middle of it."
- Cut contingency: collapse AWS/BNB split into one card.

## s-signal-outside (7:00) — Henry (light, mostly Andy)

- Bullet 1: "Garry Tan at YC Startup School 2026, 'Own Your Intelligence,' published August 6."
- Bullet 2: Personal AGI runs on your own infrastructure; compounds personal knowledge over time.
- Bullet 3: Pair it with the operating-layer thesis — if the agent runs on someone else's infrastructure, the operator is not the user.
- Handoff (Andy): "Hot Take."

## s-hot-take (3:00) — Henry (anchor)

- Bullet 1: Anthropic text watermark — changes the source of randomness in low-stakes word choices.
- Bullet 2: Positive result means Claude likely processed some of the content — not that Claude authored it. Translation is more markable.
- Bullet 3: Detector API "coming soon." C2PA file credentials are a separate path.
- Landing line: "Watermarks belong in triage pipelines, not courtrooms. The production-layer fix is signed receipts."
- Handoff (Andy): "Heritage sponsor."

## s-sponsor-heritage (0:30) — Henry

- "Heritage Telecom keeps the lights on while we keep the operating layer honest. Independent. Reliable. Quietly essential. Back to One to Watch."
