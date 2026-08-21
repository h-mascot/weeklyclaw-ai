# WeeklyClaw #26 — Host cheat sheet (rev6)

Use this on screen while live. Owner, segment, time, opening line, must-say, must-not-say, sources, slide.

Revision: rev6 — DROP s-the-map. MOVE Signal From Outside to after news block. REBUILD s-seg-stripe-openrouter: title on top + Stripe + Ox Alpha side by side. ADD S5 DeepSeek Flash Vision. Renumbered 1–5.

| Time | Owner | Slide | Segment | Opening line | Must-say | Must-not-say | Sources |
|------|-------|-------|---------|--------------|----------|--------------|---------|
| 0:00 | Both | s-title | Title | "Welcome to WeeklyClaw, episode twenty-six." | number, date | model names | — |
| 0:30 | Both | s-cold-open | Cold open | "It is Friday, August 21. The models barely moved this week. The layer beneath them did." | "speed, routing, payments, supervision, and the launch-as-chart are the new product surface" | "Qwen" | — |
| 2:30 | Andy | s-sponsor-herald | Sponsor | "Brought to you by Herald Labs — an applied AI product lab where humans and agents build together." | "Entity is mission control for agent teams" | product claims | labs.theherald.co |
| 3:00 | Henry | s-seg-faraday | S1 | "Inherent's Faraday, post-trained on Qwen3.6-27B, builds a scientific agent that can call GPT-5.5 Codex as a coding worker rather than encoding scientific workflow in a large hand-built multiagent harness." | "60% wins · 6% above Claude · 8% above Codex · 29/41 human preference · Codex also judges" | "no public weights" | arxiv 2608.13331 |
| 8:30 | Henry | s-seg-speed | S2 | "Agent intelligence is now constrained by wall-clock time as much as model quality." | "Cerebras CS-4 + Inco DFlash 2 · hardware scale + software drafting · 76.8 tok/s on M5" | "neutral benchmark" | cerebras.ai/cs4 · inco.ai/blog/dflash2 |
| 13:30 | Henry | s-seg-stripe-openrouter | S3 + Ox Alpha | "Both companies posted on August 19. Stripe's newsroom announcement says it has agreed to acquire OpenRouter." | "400+ models · 10T+ tokens/day · 10M devs · 10× growth · 414 catalog entries · 'same mission, same name, same product, same roadmap' · Ox Alpha: free, 1M context, mandatory max reasoning · 10 DeepSWE tasks" | "deal closed" · "Ox Alpha owned" | stripe newsroom · openrouter is joining stripe · ox-alpha · bloomberg |
| 18:00 | Henry | s-seg-deepseek | S5 DeepSeek | "DeepSeek shipped a chart. The chart is the launch." | "ApexBench 36.5 · Agents Last Exam 27.3 > Opus 25.7 · Terminal Bench 2.1 83.9 · DeepSWE 59.3 · vendor-reported" | "audit" · "guarantee" | x.com/deepseek_ai/status/2090730032574631962 |
| 22:30 | Henry | s-seg-agent-payments | S4 | "AWS Bedrock AgentCore Payments moved from May preview to GA on August 18." | "x402 + Stripe/Tempo MPP · Coinbase/Stripe Privy wallets · session caps · Altana wallet onchain" | "audited at scale" | aws.amazon.com/blog/agentcore-payments-ga · bnb altana blog |
| 27:30 | Andy | s-signal-outside | Signal | "This week's outside signal is Garry Tan at YC Startup School 2026, 'Own Your Intelligence.'" | "personal AGI runs on your own infrastructure" | "AGI achieved" | youtube eRrc1pUY5oU |
| 34:30 | Both | s-hot-take | Hot Take | "Hot take, not the news. Anthropic's text watermark changes the source of randomness in low-stakes word choices." | "involvement ≠ authorship · signed receipts over watermark guesses" | "watermark is authorship proof" | anthropic text watermark |
| 37:30 | Henry | s-sponsor-heritage | Sponsor | "Heritage Telecom keeps the lights on while we keep the operating layer honest." | — | — | — |
| 38:00 | Andy | s-watch | One to Watch | "One to watch for next Friday: Stripe–OpenRouter closing conditions, DeepSeek chart-as-launch follow-ons, and whether anyone ever names Ox Alpha." | "three watches: Stripe newsroom · OpenRouter changelog · independent neutrality measurement · Ox Alpha attribution · DeepSeek API/method release" | predictions | — |
| 38:30 | Andy | s-sources | Outro | "That's WeeklyClaw twenty-six." | "Friends of the Crustacean · next show 8/28" | — | weeklyclaw.ai |

## Cut order (if running long)

1. Compress S5 (DeepSeek) first: drop the ApexBench 36.5 vs Opus 39.4 row, keep the Agents' Last Exam 27.3 > Opus 25.7 line.
2. Compress S3 (Stripe + Ox Alpha) second: collapse the side-by-side into a single beat.
3. Compress S4 (AgentCore) third: collapse AWS/BNB split.
4. Compress S2 (speed) fourth: drop DFlash 2 software side.
5. Never cut Signal From Outside.
6. Never cut cold open.

## Standing rules (rev6)

- "What Happened This Week" segments are always Henry-led. rev6 confirms Henry leads all five.
- Sponsor rotation: Episode 26 inverts Episode 25's order. Herald (2:30) → Heritage (37:30).
- Live link opens at host cue, never on slide load.
- Vendor-reported numbers labeled on air: "vendor-reported", "configuration-specific", "anonymous-sourced".
- Ox Alpha is unattributed and unverified — on-air: "unattributed, unverified, ten tasks, take the 80% as signal not score."
- DeepSeek chart numbers are vendor-reported from a single launch post — on-air: "vendor-reported, single launch post, configuration-specific. No independent rerun."
