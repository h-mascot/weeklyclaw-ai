# Weekly Claw #37 — Friday, November 6, 2026 — 4:00 PM ET

**Revision:** 4 (immutable once written; any change = new revision file)
**Runtime plan:** 34 min content, hard stop 45
**Lineup:** 12 slides · 4 clustered news slides (8 stories) · 1 video anchor · 1 hot take
**News window:** 2026-10-30 20:00 UTC → 2026-11-05 19:30 UTC (EP36 aired Fri Oct 30, 16:00 ET)
**Approval state:** awaiting lineup review by Henry (Telegram 855505513) or Andy (7615999206)
**Revision 4 (Fri REFRESH, additive):** no story swap, no promotion. (a) Hot-take arc extension now carries the IPO pushback with two independent press receipts — Reuters and the Wall Street Journal report investors balking at the $1.5T valuation, one reportedly floating $1T, October revenue absent from the updated S-1, and the ~Nov 10 roadshow start at risk. (b) Close card 2 sharpened to match. (c) Cold-open hook count corrected to five in the talking points (agenda and speaker notes already had five). Deck markup unchanged — `deck.rev4.html` is byte-identical to `deck.rev3.html`.

## Frame

One week of agent-era plumbing: OpenAI rebuilt Git for agent-scale traffic and then bought the tooling around it, Meta bought the multi-agent workspace, one open frontier checkpoint actually shipped its weights, two practitioners fought over what "reading weights" means, and a $1.2M model run produced 948 working root exploits. The throughline: the layer agents run on is being consolidated, priced, and attacked — all in five days.

Cold-open promise (on air): "The agents got a landlord, a lawyer, and a bug bounty — in the same week."

## Segment order and timings

1. **Title** — 0:00–0:20
2. **Cold open** — 0:20–2:20 (2 min): five hooks — Pando/Pierre + Conductor, Kimi weights, weight space, 948 exploits + prompt adware, Anthropic commitments
3. **Sponsor · The Herald Labs** — 2:20–3:20 (1 min, slot 1, inverted from EP36)
4. **S1 · What happened this week · agent-era code stack** — 3:20–8:20 (5 min)
5. **S2 · What happened this week · open weights** — 8:20–12:20 (4 min)
6. **S3 · What happened this week · weight space** — 12:20–16:20 (4 min)
7. **S4 · What happened this week · agent security** — 16:20–21:20 (5 min)
8. **Signal From Outside · Factory, "Your AI Agents Shouldn't Care Where They Run"** — 21:20–27:20 (6 min)
9. **Hot take · Anthropic's $895.4B of purchase commitments** — 27:20–31:20 (4 min)
10. **Sponsor · Heritage Telecom** — 31:20–32:20 (1 min, slot 2)
11. **Close · One to watch + Discord** — 32:20–34:20 (2 min)
12. **Sources & Links** — non-air reference, shown at end

## S1 — Agent-era code stack (C76 + C80)

**Lead:** Henry. Andy supports with caveat/fallback prose only.

Headline: **OpenAI rebuilt Git for its agents, then bought the tooling around it.**
- **Pando** (openai.com, Nov 2): Rust Git backend for agent-scale monorepos; ~1PB/day; median push latency cut ~5x; reliability had fallen below 90% under Codex concurrency; built with Codex in 10 weeks; unmodified Git protocol. HN thread 269 pts, submitted 2026-11-02T23:47Z.
- **Pierre** (openai.com, Nov 4): OpenAI acquires Pierre Computer Company — Code Storage plus the Trees/Diffs libraries Codex already ships; post explicitly continues the Pando thread; open-source projects stay open; close pending conditions.
- **Conductor → Meta** (TechCrunch 1:10 PM PST Nov 4; conductor.build changelog): workspace for deploying teams of agents on one project; Conductor cloud shuts down **Nov 20**.
- Caveat on air: sxz.io notes two described Pando client features live in OpenAI's Git fork, not upstream Git.

## S2 — Open weights (C79)

**Lead:** Henry. Andy supports with caveat/fallback prose only.

Headline: **One frontier checkpoint actually shipped its weights.**
- **Kimi K3.1 Pro** (HF, Nov 4): ungated; 2.8T total / 104B active; 1M context; MXFP4 QAT; MoonViT-V2 vision; Gated MLA→Gated DSA swap on 24 layers vs K3 (69 KDA + 24 Gated DSA row on the card); 11,658 downloads / 754 likes at check; vLLM day-0; Huawei serves via vLLM-Ascend + SGLang on Atlas A3 / Ascend 950.
- **ERNIE-5.5-Flash-Base** (Baidu, Nov 5): 280B total / 14B active base checkpoint; 33.5T tokens; 1M-token fine-tune context; FP8+BF16; custom ERNIE license v1.0 — **not Apache**.
- **Tencent Hy4** (Nov 4): first vision + first computer use, CLI+GUI, Blender/CAD-trained; live on Tencent Cloud + OpenRouter at $0.834/$2.501 per M — **weights not posted**, only Hy4-preview. Label "API now, weights pending" on air.
- Bench context (not a slide): Ricursive Ripple-65B Preview, Apache-2.0, Terminal-Bench 2.1 80.52.

## S3 — Weight space (C75)

**Lead:** Henry. Andy supports with caveat/fallback prose only.

Headline: **Qwen 3.8 27B read its own weights well enough to name the game.**
- **Willison** (Nov 3): on a laptop, Qwen 3.8 27B names 3 of 4 games from raw policy weights; his own caveat — "some of the wider commentary… does not feel justified."
- **Sparks claim** (Nov 2): GPT-6 Astra reads small nets' weights; writes game-playing nets beating PPO-100M; fixes Qwen3.5-0.8B MATH-500 7.9→48.1 by editing 0.016% of weights.
- **Honnibal** (Nov 3, "…post is misleading"): only toy nets are read weight-only; the Qwen/Go results lean on Python programs and up to 50 passes.
- Framing on air: claim vs rebuttal, explicitly labelled. Not a verdict.

## S4 — Agent security (C82)

**Lead:** Henry. Andy supports with caveat/fallback prose only.

Headline: **A $1.2M model run produced 948 working root exploits.**
- **OpenAI "A thousand fewer paths to root"** (Nov 4, via THN): 30-hour pipeline; 2,308 candidate kernel findings → 1,724 dynamically reproduced → **948 working local-privesc exploits**, each with a patch; novel techniques include kernel object spraying, page grooming, five data-only privesc paths; OpenAI's line: an unpatched low-priv account is "functionally equivalent to root" for a well-resourced actor. Label exploit counts OpenAI-reported.
- **GPT-6 Cyber launch** (openai.com, Nov 5): OpenAI named the model behind the 948 run. ExploitGym 48.5% vs 32.1% for GPT-5.6 Cyber; out-of-scope-service avoidance 99.93% without the deployment prompt and 100% with it; 81 previously unknown high-severity Firefox bugs, Mozilla fixes in MFSA2026-118; classified Critical under the Preparedness Framework. API and Codex access is Daybreak Red customers only. Label OpenAI-reported.
- **Check Point "prompt adware"** (Nov 3): Haiou jailbreak bundle targets Codex; installs Skills and rewrites Codex config so ads for the author's paid LLM gateway are injected into later agent responses. Seen alongside Cobalt Strike, VulnClaw and Ladon. Broader risk: gateways snooping data, stealing cloud keys, injecting tool calls.

## Signal From Outside — Factory, Nikhil Harithas (permanent anchor)

- Title: **"Your AI Agents Shouldn't Care Where They Run"** · AI Engineer · video `XIHZpZtYCzo`
- Published 2026-11-03T01:00:22-08:00 · 17:13 · 5,085 views at verification · poster `assets/images/sfo37-factory-relay.jpg`
- Verified: transcript saved at `sources/transcript-XIHZpZtYCzo.txt` (489 lines); cues read against transcript, **spot-check before air** (auto-captions can drift by seconds).
- Cue beats (manual open only, never autoplay):
  - 2:44–3:34 — "agents can't just keep borrowing your identity… they're basically slightly non-deterministic applications"
  - 5:42–6:40 — control plane, compute gateway and relay
  - 9:34–10:26 — bring your own key, stays inside the VPC, blast radius contained
  - 11:21–11:36 — plans to open source the compute layer; "the abstractions have nothing to do with Factory"
  - 12:24–12:37 — snapshots and forking for fleets and swarms
  - 14:22–15:45 — the hard parts: bookkeeping, AWS microVM 8-hour session cap, snapshot/rehydrate for multi-day missions
  - 16:44–17:05 — "agents shouldn't care where they run"
- Selection reason on air: it is the operational counterweight to S1 — the labs are consolidating the layer, while a 17-minute practitioner talk shows what it actually costs to make agents run where a customer's security team says they must.

## Hot take — Anthropic's commitments (C77, receipts only)

- Proposition: **The revenue is the headline. The commitments are the story.**
- Receipts (vendor-filed, EDGAR accession 0001628280-26-068676, filed 2026-11-02T14:24Z): Q3 revenue **$16,956M** (+46.7% QoQ); nine-month **$33,242M**; purchase commitments **$895.4B** vs **$447.5B**; nine-month compute $18,808M. Ratio ~13x annualized revenue.
- Arc extension, bench-grade only: TeraWulf/Google credit backstop for a $19B Anthropic lease (Nov 4); Nasdaq "ANT" IPO pending. IPO pushback — Reuters and the Wall Street Journal report prospective investors balking at the $1.5T valuation, with one reportedly floating $1T; October revenue is absent from the updated S-1 and the roadshow's ~Nov 10 start is at risk. Read via The Decoder's rendering (Reuters itself is bot-walled to us) — attribute as "press reports", never as a filing.
- Non-duplication check: no news slide carries Anthropic; this is the only airing of the S-1/A numbers.

## Bench (recorded, not promoted)

- C74 Apple opens Siri AI developer access (App Intents + skills, iOS 27.3 Developer Preview) — strong, held for next week; official Apple docs only, spring submission gate/terms TBD, EU unavailable.
- C78 Sovereign stacks (IndiaAI EKA-1 / Dhīr 2B·5B; DeepSeek V5 reportedly Ascend-950-native) — the Ascend leg stays labelled unconfirmed.
- C81 ChatGPT search ≈20% of Google's volume, 1B→1.2B weekly users in 60 days — single-source on-record, methodology undisclosed.
- C83 Midterms: ~$187M AI ads, ~90% undisclosed; OpenAI National Community Compact (Nov 5) — Henry-angle low, keep for the next political cycle tick.
- Watch-only: Qwen 4 "next week" per Alibaba CTO; Gemini 4 Carbon tops AA Intelligence Index (JS-rendered scores unverified); fal at $16B per Bloomberg; Claude Marketplace 25+ partner agents; GPT-5.6 Cyber in AWS GovCloud.

## Sponsor slots

- Slot 1: The Herald Labs (`assets/videos/herald-labs-ad.mp4`, poster `assets/images/herald-labs-ad-poster.jpg`, heraldlab.si)
- Slot 2: Heritage Telecom (`assets/videos/heritage-telecom-ad.mp4`, poster `assets/images/heritage-telecom-ad-poster.jpg`, heritagetel.com)

## Close

- One to watch, three cards: (1) Conductor cloud shutdown Nov 20 — where do those teams land; (2) Anthropic's roadshow around Nov 10 — now at risk: press reports say investors are pushing back on the $1.5T valuation and October revenue is missing from the updated S-1, so does the $895.4B survive diligence; (3) Kimi K3.1 Pro real-world adoption vs Ripple-65B economics.
- Discord QR to `https://weeklyclaw.ai/discord` on the close slide; recap appears **once**, on this slide, and is never repeated in the cheat sheet or end copy.

## Caveats carried on air

- All Anthropic figures vendor-filed.
- Exploit counts OpenAI-reported.
- Hy4 weights pending; ERNIE licence is custom, not Apache.
- Weight-space claims contested — claim vs rebuttal, not settled.
- SFO cues creator/auto-caption timestamps — spot-check before air.
- Pando client-feature caveat per sxz.io.
