# WeeklyClaw #26 — Andy section (rev6)

Andy handles: Herald sponsor (0:30), the agent-payments caveat (BNB), Signal From Outside (anchor, 7:00), One to Watch, Sources. Andy also provides caveat prose for Henry-led news segments.

## s-sponsor-herald (0:30) — Andy

- "This episode is brought to you by Herald Labs — an applied AI product lab where humans and agents build together. Their product Entity is mission control for agent teams, and they run hacker houses worldwide. Find them at labs.theherald.co. Back to the operating layer."

## s-seg-faraday (S1, 5:30) — Andy (caveat)

- **Fallback prose (use only if Henry loses his place):**
  "The interesting caveat is the human study was author-selected — they sampled the cases where the automated judge saw a strong Faraday advantage. The same Codex model serves as the rubric judge. So the 27B is not outperforming the frontier; it is outperforming it by calling it. No public weights, training code, or Replica dataset. The number to remember: 60% wins, 6% above Claude, 8% above Codex, 29/41 human preference."
- **Caveat to add on air:** "Author-selected, not a neutral comparison."

## s-seg-speed (S2, 5:00) — Andy (DFlash 2)

- **Fallback prose (use only if Henry loses his place):**
  "Inco attacks the same wall-clock budget in decoding software. DFlash 2 uses a selector plus local convolution to improve parallel speculative drafts while preserving the target model's output under lossless rejection sampling. The released Qwen3.8-27B drafter averages 4.80 accepted tokens vs 4.28 for native MTP and 3.62 for community DSpark. Inco reports 2.7 to 3.4× autoregressive throughput in SGLang and 16 to 25% more accepted output per verification pass for roughly 1% extra cycle latency. The drafter weights are live on Hugging Face under Apache 2.0. The vLLM and llama.cpp integration PRs are still open."
- **Caveat:** "All numbers are vendor-reported; the PRs are unmerged; no matched independent rerun."

## s-seg-stripe-openrouter (S3, 4:30) — Andy (Ox Alpha)

- **Fallback prose (use only if Henry loses his place):**
  "Then on August 20 — the same week the router sells — an unattributed ghost shows up on the same rail. OpenRouter quietly mounted a free stealth/ox-alpha route with 1M context, 131,072 max output, text/image/video input, and mandatory max reasoning. Ben Davis posted over 80% on only ten DeepSWE tasks versus 65% for Fable and 52% for GPT-5.6 Sol, with an explicit variance warning. No developer identity, no model card, no full benchmark run, no stable availability commitment. The router got bought, and an unattributed frontier-class ghost showed up the same week. OpenRouter wrote down 'routing decisions remain driven by what's best for the user' before the deal even closes. What would have to happen for us to say that promise failed?"
- **Caveat:** "Unattributed, unverified, ten tasks. Take the 80% as signal, not score."

## s-seg-deepseek (S5, 4:30) — Andy (caveat)

- **Fallback prose (use only if Henry loses his place):**
  "DeepSeek didn't drop a paper this week. They dropped a chart. The chart shows ApexBench 36.5, Agents' Last Exam 27.3, Terminal Bench 2.1 at 83.9, DeepSWE 59.3. All vendor-reported from a single launch post. The point isn't the numbers — it's that the launch was the chart, not the API, not the paper. Compare that to Faraday in segment one, where the chart lived inside the paper. And to Cerebras in segment two, where the chip was the artifact. DeepSeek chose a third route: the benchmark table is the product. That's the new product surface — and it's why the chart is also the audit trail."
- **Caveat:** "Vendor-reported, single launch post, configuration-specific. No independent rerun."

## s-seg-agent-payments (S4, 5:00) — Andy (BNB)

- **Fallback prose (use only if Henry loses his place):**
  "BNB's alternative: Agent Studio v2 ships an Altana wallet where scoped session keys carry spending limits, allowlists, and time bounds registered onchain, revocable without giving the agent the private key. Two distinct designs. AWS treats the boundary as managed logs and policy; BNB writes it onchain and lets the builder keep the keys. The most important sentence in the AWS receipt: 'the model never holds the key.'"
- **Caveat:** "Neither design has been independently audited at scale."

## s-signal-outside (7:00) — Andy (anchor)

- **Full fallback prose (anchor):**
  "This week's outside signal is Garry Tan at YC Startup School 2026, 'Own Your Intelligence.' Published August 6. The argument is that we are entering the era of personal AGI: AI agents that run on your own infrastructure, compound personal knowledge over time, and dramatically increase individual ability to build. Tan is YC's president and CEO; the talk is 42 minutes. Pair his 'agents on your own infrastructure' framing with the show's 'operating layer became the company' thesis and you get the same answer from two angles. If the agent runs on someone else's infrastructure, the operator is not the user. Fallback is the verified YouTube maxresdefault thumbnail. Source: youtube.com/watch?v=eRrc1pUY5oU and ycombinator.com/library/WX-garry-tan-own-your-intelligence."

## s-hot-take (3:00) — Andy (steelman)

- **Steelman prose:**
  "The opposition: any signal beats the vacuum the public operates in today. Schools need something. Newsrooms need something. Even a probabilistic watermark is better than nothing. The resolution is scope: watermarks belong in triage pipelines that route questionable artifacts to a reviewer, not in courtrooms that treat 'Claude likely processed this' as authorship."

## s-watch (1:00) — Andy

- **Full prose:**
  "One to watch for next Friday: Stripe–OpenRouter closing conditions, DeepSeek chart-as-launch follow-ons, and whether anyone ever names Ox Alpha. If Stripe–OpenRouter closes before August 28, the gateway and the wallet ship as one company and the neutrality promise becomes a one-quarter-old commitment under audit. If DeepSeek ships an API, a paper, or a model card behind the chart, the launch-as-chart rule either firms up or quietly dissolves. Three watches: the Stripe newsroom index for a closing announcement; the OpenRouter changelog for any model-routing behavior change; any independent measurement of routing neutrality post-close; the DeepSeek repo/API for a follow-up release; and any independent naming or measurement of Ox Alpha."

## s-sources (0:30) — Andy

- "That's WeeklyClaw twenty-six. Discord on screen for live chat, scan to join Friends of the Crustacean. Follow at weeklyclaw.ai. Next show Friday August twenty-eight, four PM ET. See you then."
