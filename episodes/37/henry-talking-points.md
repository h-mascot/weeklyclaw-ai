# Weekly Claw #37 — Henry's section view (rev4)

Deck: revs/deck.rev4.html · 12 slides · show Fri 2026-11-06 16:00 ET.
You lead cold open, S1, S2, S3, S4, the hot take, the Heritage Telecom read and the Discord CTA. Andy presents Signal From Outside, reads Herald Labs, carries the support/caveat prose, rebuts on the hot take and closes. Bullets below are your speaking order; the prose after each block is the landing line, say it close to as written.

## Title → Cold open (0:00–2:20)

- "Five days, and the layer agents run on got consolidated, priced and attacked."
- "OpenAI rebuilt Git for its own agents, then bought the tooling around it. Meta bought the workspace. Kimi put 2.8 trillion parameters on Hugging Face with no gate."
- "Two practitioners fought over what reading a model's weights even means, and a $1.2M model run produced 948 working root exploits."
- Point at the four chips as you say them: code stack, open weights, weight space, agent security.

Landing line: "The agents got a landlord, a lawyer, and a bug bounty — and we have receipts for all three."

## S1 — Agent-era code stack (3:20–8:20)

- Pando: ~1PB/day, median push latency down ~5x, and reliability that had fallen below 90% under Codex concurrency. Say the number, then the number after it.
- Built with Codex in 10 weeks, unmodified Git protocol — the interesting part is that the protocol did not change, the storage did.
- Two days later: OpenAI buys Pierre. Same day: Meta buys Conductor. Name the same-day coincidence out loud.
- Conductor cloud goes dark November 20. Two weeks. That is the part the audience can act on.
- If Andy raises the sxz.io note: concede it plainly — two described client features are OpenAI-fork-only — and keep the 1PB/day and reliability figures, which are the post's own.

Landing line: "The code stack for agents just got a landlord, and the tenant list is being rewritten."

Handoff: "Now the weights — because one of these actually shipped."

## S2 — Open weights (8:20–12:20)

- Kimi K3.1 Pro: 2.8T total, 104B active, 1M context, ungated. Those four facts in that order.
- The engineering detail worth one sentence: MXFP4 QAT, MoonViT-V2 vision, and a gated attention swap on 24 layers versus K3.
- Day-0 serving exists — vLLM, plus Huawei on Atlas A3 and Ascend 950. That is what makes it a build story rather than a leaderboard story.
- ERNIE-5.5-Flash-Base next day: 280B/14B-active, 33.5T tokens, custom licence. Say "custom licence" before anyone assumes Apache.
- Hy4: vision and computer use, API-only, weights pending. Do not imply open weights.

Landing line: "One frontier checkpoint shipped ungated, one shipped under a custom licence, and one is still an API."

Handoff: "And if weights are a program, this next story is about what happens when a model reads them."

## S3 — Weight space (12:20–16:20)

- Willison's replication: Qwen 3.8 27B, laptop, 3 of 4 games from raw policy weights.
- Read his own caveat in his words — "some of the wider commentary… does not feel justified." That sentence is the segment.
- Honnibal's rebuttal: only toy nets are read weight-only; the Qwen and Go results lean on Python programs, up to 50 passes.
- Sparks claim as a claim: Astra editing 0.016% of weights to move MATH-500 from 7.9 to 48.1.
- Do not pick a winner. Name what would settle it: an independent run with the programs removed.

Landing line: "Claim, rebuttal, no referee. That is where this one sits tonight."

Handoff: "Which is a nice segue into the other side of this week: the receipts about what these systems can actually do."

## S4 — Agent security (16:20–21:20)

- 948 exploits, each with a patch. Then the funnel: 2,308 candidates, 1,724 reproduced, 948 working.
- The cost line: $1.2M of API in a 30-hour run. That number is the story, not the exploit count.
- Name the model: it shipped Nov 5 as GPT-6 Cyber. ExploitGym 48.5% against GPT-5.6 Cyber's 32.1%, plus 81 previously unknown Firefox bugs Mozilla has now fixed. Say it as OpenAI-reported, not as an independent run.
- Techniques worth naming: kernel object spraying, page grooming, five data-only paths.
- OpenAI's framing to quote: an unpatched low-priv account is functionally equivalent to root for a well-resourced actor.
- Prompt adware: a jailbreak bundle that installs Skills and rewrites Codex config so ads land in later agent responses. Seen next to Cobalt Strike, VulnClaw, Ladon.
- Label both: exploit counts OpenAI-reported, adware from Check Point's research.

Landing line: "The same week the layer got a landlord, it also got a bug bounty."

Handoff: "And that is the perfect place to leave the news and look outside."

## Hot take (27:20–31:20)

- Lead with the split: "Revenue is the headline. The commitments are the story."
- Q3 revenue $16,956M, up 46.7% quarter on quarter. Nine months: $33,242M.
- Purchase commitments $895.4B, against $447.5B the prior period. Nine-month compute spend $18,808M.
- Do the arithmetic on air: roughly 13x annualized revenue, signed before the roadshow.
- Your proposition: nobody signs $895.4B of compute by accident. It is a demand forecast — and if it is even 20% wrong, the balance sheet that absorbs it is not Anthropic's.
- Your falsifier: a disclosed schedule where the $895.4B steps up only after revenue clears a stated threshold.
- The timing beat, if you want it: the roadshow is reportedly around November 10, and press reports say investors are already pushing back on a $1.5 trillion valuation — one reportedly floated a trillion. Say "press reports", never "the filing says". It is the cleanest proof that the commitments are being priced before the money arrives.
- Then hand to Andy for the allocation argument, and do not restate his point after him.
- Say "unaudited, vendor-filed" once, early.

Landing line: "Thirteen times annualized revenue, signed before the roadshow. If compute demand flattens, the people holding the leases find out first."

## Sponsor 2 — Heritage Telecom (31:20–32:20) — you read it

Read off the slide, clean, no recap, no callback to the news:

"Heritage Telecom runs the connectivity behind a lot of the infrastructure we just talked about — the links that keep agent traffic inside a region and off the public internet. heritagetel.com."

Then hand straight to Andy: "One to watch before we go."

## Close (32:20–34:20)

- Andy runs One to Watch and speaks the single recap. You add one line only if he leaves the Anthropic card unqualified: "roadshow reportedly around November 10, and press reports say investors are balking at the $1.5 trillion valuation — so it may slip. No priced offering yet; the S-1/A is the only filing."
- You take the Discord call to action: QR on screen, weeklyclaw.ai/discord.
- Recap lives here, once. Not in the cheat sheet, not in either sponsor read, not in the sign-off. Do not repeat it after Andy.
- Sign-off: "See you next Friday." Next episode November 13, 4 PM ET.

## Never say on air

- That the show's identity has broadened. Justify by viewer stakes instead.
- Any Anthropic figure without "unaudited, vendor-filed".
- Any exploit count without "OpenAI-reported".
- "Open weights" for Hy4.
- "Apache" for ERNIE.
- A verdict on weight space.
