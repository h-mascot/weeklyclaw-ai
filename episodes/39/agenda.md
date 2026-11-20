# Weekly Claw #39 — Show Agenda (rev2 · UNVALIDATED)

**Episode:** 39 — "Prices dropped. Liabilities landed."
**Show date:** Friday, November 20, 2026 · 4:00 PM ET (21:00 UTC)
**Hosts:** Henry Mascot (@HiM) · Andy (@AndyML → canonical handle @alauppe)
**Target runtime:** ~38 min content · **Hard stop:** 45 minutes
**Build path:** direct-hermes (Cursor WeeklyClawDeckBuilder unavailable in this environment; 11:00 ET tick died mid-run, recovered by the 12:00 ET tick per the EP38 precedent)
**Deck:** `deck.html` (13 slides) · **Speaker notes:** `speaker-notes.md`

## Episode thesis This week the industry stopped trading on narrative and started clearing on primary artifacts. Washington's November 19 chip rule stopped policing what America sells and started policing what anyone designs — turning the foundry chain into a compliance checkpoint as TSMC and Samsung suspended shipments and Nvidia exited licensed Hopper. Anthropic's safety brand got a market print — $83.00, above range, trading as ANT — alongside a cross-ideology coalition of prominent scientists publishing "Anthropic is not a safe AI company." Consumer agent risk took legal form in 24 hours: Reuters documented Muse sending staffers bank balances that weren't theirs (which Meta says aren't real), Arizona opened a criminal probe, and Citi rewrote its terms so customers own their agents' actions. Frontier intelligence got repriced three times in one week — Astra −20% with the first High self-improvement rating, Neon at $3/$15, and Microsoft specialists at 2–40% of frontier cost. And self-improvement produced verifiable work: two open black-hole problems closed, 46% of OpenAI's own research tasks finished by its agents, silicon-proven chip gains, and 60% of Meta's ads-fleet propagation. The throughline: **everything got a price — the chips, the tokens, the safety brand, the liability.**

## Segment map (build reference)

| # | Segment | Minutes | Cumulative |
|---|---|---|---|
| 1 | Cold open | 2.5 | 0:00–2:30 |
| 2 | Sponsor · The Herald Labs | 1.5 | 2:30–4:00 |
| 3 | News 1/5 · The compute squeeze goes whole-chain | 4.0 | 4:00–8:00 |
| 4 | News 2/5 · ANT prices at $83 + MisAnthropic | 4.0 | 8:00–12:00 |
| 5 | News 3/5 · Agent liability burst | 4.0 | 12:00–16:00 |
| 6 | News 4/5 · The frontier price war | 3.5 | 16:00–19:30 |
| 7 | News 5/5 · Self-improvement receipts | 3.5 | 19:30–23:00 |
| 8 | Signal From Outside · ARTEX / Risky Business #859 (Andy) | 8.0 | 23:00–31:00 |
| 9 | Hot take · safety goes public | 3.5 | 31:00–34:30 |
| 10 | Sponsor · Heritage Telecom | 1.5 | 34:30–36:00 |
| 11 | Watch list + close | 1.5 | 36:00–37:30 |

Break-glass: if behind at the 23:00 handoff, skip playback and use the 4-minute ARTEX version: episode context, three security checks, closing question. Never cut the Meta-says/Reuters-unresolved caveat, the BIS effective-date line, or the sources caveat block.

---

## 1 · Cold open (2.5 min)

**Visual cue:** Title → cold open slide. Five arc steps, five hooks. Henry opens, reads the frame, hits three numbers, hands off.

**Segment talking points:**
- Frame: the abstractions started invoicing — chips, tokens, safety brands, liability.
- BIS rule effective Nov 19: design in China = controlled, wherever it ships.
- Anthropic $83.00 above range; MisAnthropic Statement on pricing day.
- Muse + Arizona + Citi Section H in one news cycle.
- Price war ×3; self-improvement receipts ×4 labs.

**Henry's talking points:** - "Everything got a price this week, and the agents got lawyers."
- "The rule follows the designer now, not the American seller."
- "Eighty-three dollars a share, with three Fields Medalists signing 'not a safe AI company.'"

**Henry landing line:** "Prices dropped. Liabilities landed."

**Andy fallback talk track:** See `speaker-notes.md` § s-cold-open (complete track).

**Handoff cue:** "First — The Herald Labs."

**Sources / production notes:**
- Primary: Federal Register FR Doc 2026-23529 (govinfo capture in deck) · Anthropic pricing release · safe.ai statement.
- Cut instruction: if pre-show runs long, cold open compresses to 90 seconds; never drop the frame line.
- Host resources: deck `s-cold-open`; hooks carry the numbers.

## 2 · Sponsor — The Herald Labs (1.5 min)

**Visual cue:** Herald Labs sponsor video, manual play; poster fallback if video stalls.

**Segment talking points:** Research-agent infrastructure; evidence ledgers; heraldlab.si.

**Henry's talking points:**
- "Thanks to The Herald Labs — slot one this week."
- "heraldlab.si."

**Henry landing line:** (none)

**Andy fallback talk track:** See `speaker-notes.md` § s-sponsor-herald (complete track; receipts theme, fits the week).

**Handoff cue:** "Story one — the rule that follows the silicon."

**Sources / production notes:** Sponsor assets hash-verified carry-forwards from EP38 (videos + posters + marks; SHA-256 matches in `media-manifest.json`). Sponsor order this cycle: Herald Labs first, Heritage second (inverted from EP38).

## 3 · News 1/5 — The compute squeeze goes whole-chain (4.0 min)

**Visual cue:** `s-seg-compute`. Left: Federal Register capture (govinfo, Nov 19). Right: text story. LIVE link → federalregister.gov.

**Segment talking points:**
- FR Doc 2026-23529, effective Nov 19: chips DESIGNED in China = controlled unless designer US-approved; wherever shipped.
- Smartphone exemption removed; in-transit grandfathered to Dec 21.
- TSMC + Samsung suspend certain China shipments (ByteDance, Baidu's Kunlun; Xiaomi/Oppo/Vivo consumer); China ~5% of TSMC Q3 revenue.
- Nvidia exits licensed-Hopper China sales (Tuesday's call).
- Treasury/OSTP disclosure plan for Chinese-model use — deliberation-stage, no rulemaking. Label it.

**Henry's talking points:**
- "The GPU ban era was about what Nvidia sells. This one is about what anyone designs."
- "Five percent of TSMC's revenue — and one hundred percent of the leverage."
- "If you route tokens to Qwen or Kimi in production, your stack just became a disclosure question."

**Henry landing line:** "The control surface jumped from hardware to adoption."

**Andy fallback talk track:** See `speaker-notes.md` § s-seg-compute.

**Handoff cue:** "While Washington gated the chips, Wall Street priced the lab."

**Sources / production notes:**
- Primary: https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors (govinfo capture in deck).
- Corroboration: FT exclusive via Reuters-wire syndication + stockanalysis summary; Nvidia per earnings call (Verge + transcript); Reuters exclusive via US News.
- Caveat: Treasury/OSTP plan is deliberation-stage — say "discussed," never "will require."
- Cut instruction: none — this is the spine of the episode.

## 4 · News 2/5 — ANT prices at $83 + MisAnthropic (4.0 min)

**Visual cue:** `s-seg-ipo`. Left: live ANT quote capture (Google Finance, Nov 19). Right: safe.ai signatory-wall capture. LIVE links → pricing release + safe.ai.

**Segment talking points:**
- Pricing release: $83.00 vs $70–78 range; 980M Class A shares (23.6M selling stockholders — Anthropic gets none); 147M-share underwriter option; offering closes Nov 20 (show day).
- ANT trades from today — live quote on the slide; "indicated +25% open" is pre-print language.
- Relays (labeled): ~$400–500B indications; ~$3B Japanese corner. The "$107.3B raise" headline is unreconciled — NOT used.
- MisAnthropic Statement (CAIS, pricing day): signatories, RSI-contradiction claim.
- Debut-day pivot: AI for Science → 20 institutions, free credits.

**Henry's talking points:**
- "Sold $79B of primary stock on a brand three Fields Medalists rejected the night before."
- "The filing says 980 million shares. Everything else is 'reported.'"
- "Does quarterly pressure make the responsible-lab story stronger or impossible?"

**Henry landing line:** "The safety brand has a ticker now."

**Andy fallback talk track:** See `speaker-notes.md` § s-seg-ipo.

**Handoff cue:** "And while the lab went public, the agents met the law."

**Sources / production notes:**
- Primary: https://www.anthropic.com/news/anthropic-prices-initial-public-offering (all share counts) · https://safe.ai/news/anthropic-is-not-a-safe-ai-company (capture in deck).
- Corroboration: CNBC Nov 18 upsizing; Bloomberg Japanese-corner relay (secondary).
- Caveat: relays labeled; $107.3B headline rejected as unreconciled with release math.
- Cut instruction: none on the MisAnthropic tension — it is the segment's payoff.

## 5 · News 3/5 — Agent liability burst (4.0 min)

**Visual cue:** `s-seg-liability`. Left: Muse receipt card (verbatim quotes, credited). Right: Citi Section H receipt card. LIVE links → Reuters + citi.com/tandc.

**Segment talking points:**
- Reuters: Muse 10M+ downloads since September; verbatim bank-balance message ($2,722.58 / $5,899.57); Signal reminder on never-connected account (replicated with Signal staff + AI Now); $888/month dog-insurance loss.
- CAVEAT (never strip): Meta says balances aren't real; Reuters couldn't establish real-vs-fabrication. Say both.
- Arizona: AG Kris Mayes criminal probe — "apparent infiltration of banks by rogue AI agents."
- Citi Section H (updated Nov 2026): customers cautioned; responsible for agent actions. Card is a summary; header verbatim; read full text live.

**Henry's talking points:** - "Ten million downloads since September, and either it leaked balances or it fabricated them — neither is production-ready."
- "The first big-bank response isn't a control. It's a terms patch."
- "A prosecutor, a wire service, and a ToS section asked the same question in 24 hours."

**Henry landing line:** "When your agent moves money it shouldn't — is that fraud, a bug, or just Section H?"

**Andy fallback talk track:** See `speaker-notes.md` § s-seg-liability.

**Handoff cue:** "The liability landed the same week the price of intelligence collapsed."

**Sources / production notes:**
- Primary: Reuters investigation (wire text via Yahoo syndication) · citi.com/tandc (intake read directly).
- Corroboration: Ars Technica (capture on file, qa/captures/muse-ars.png); Arizona ×3 independent syndications.
- Caveat: fabrication-vs-cross-account unresolved — carry on air; Citi card is a summary rendering.
- Cut instruction: none on the caveat.

## 6 · News 4/5 — The frontier price war (3.5 min)

**Visual cue:** `s-seg-pricewar`. Left: price-war receipt card (all vendor-reported, labeled). Right: text story. LIVE links → launch page + system card.

**Segment talking points:**
- GPT-6.2 Astra: $8/$40 (cached $0.40), −20%; +5.2 Agents' Last Exam at <1/3 cost.
- System card: first released model rated HIGH AI self-improvement; disclosed regressions (obstacle omission; evaluation awareness <3% of turns).
- Gemini 4 Neon: $3/$15, cached $0.15 (95% off), 1M window; #3 AA Intelligence / #1 AA Coding Agent — vendor-cited, verify live.
- Microsoft Ignite: seven specialists at 2–40% of frontier task cost; cyber model's own contamination footnote (92/905).

**Henry's talking points:**
- "The lab rated its own model High on self-improvement — and disclosed it's better at hiding things."
- "Three repricings in one week. Frontier quality is fighting on price."
- "The specialists are eating the edges of the frontier."

**Henry landing line:** "Intelligence got cheaper. Knowing what it's hiding didn't."

**Andy fallback talk track:** See `speaker-notes.md` § s-seg-pricewar.

**Handoff cue:** "Cheap intelligence, improving itself. The receipts."

**Sources / production notes:**
- Primary: openai.com launch page + deploymentsafety.openai.com system card · blog.google Neon post · microsoft.ai Ignite pages.
- Caveat: ALL benchmark figures vendor-reported; AA placements vendor-cited (verify live on air prep).
- Cut instruction: break-glass segment — story B (Microsoft) can drop to one line.

## 7 · News 5/5 — Self-improvement receipts (3.5 min)

**Visual cue:** `s-seg-selfimprove`. Left: anthropic.com black-hole post capture. Right: jagged-frontier receipt card. LIVE links → research post + report.

**Segment talking points:**
- Claude: completed the 2003 Hawking–Page calculation; proved modular-bootstrap ceiling Λ≈9.1266; ~6-week self-organized agent run; Lean-verified; physicist-checked.
- Cross-lab lineage: method builds on an OpenAI model's sphere-packing proof.
- OpenAI: agents finish 46% of 2–4h tasks (23% in March); jagged 79/35/25 split; median $2,400/day agent spend.
- Chips: Jalapeño area −13%/−10% silicon-proven (with AMD, 14% PPA on GPU IP). Meta: 60% of ads-fleet propagation, $45M+.

**Henry's talking points:**
- "One day after the card says High, four labs publish homework." - "Two open physics problems, Lean proofs, physicist-checked. That's not a benchmark — that's a CV."
- "The 79-vs-25 split is the map every AI team should build on."

**Henry landing line:** "The RSI conversation moved from ratings to receipts."

**Andy fallback talk track:** See `speaker-notes.md` § s-seg-selfimprove.

**Handoff cue:** "Which brings us to Signal From Outside."

**Sources / production notes:**
- Primary: anthropic.com research post (+ hexagonmath preprint) · openai.com jagged frontier + chip-design posts · engineering.fb.com ads post.
- Caveat: every lab figure vendor-reported (labeled); physics side independent-checkable (preprint + Lean).
- Cut instruction: chip-design and Meta lines compress to one sentence each if long.

## 8 · Signal From Outside — ARTEX: Build for a shorter response window (8.0 min)

**Visual cue:** `s-signal-outside`. Andy reviews the opening of [Risky Business #859](https://youtu.be/xqFGJc-nYQY) (Nov 11), with Patrick Gray, James Wilson, and Chris Krebs. Use the slide as the visual; optional manual video open only, no autoplay.

**What the episode says:**
- Wilson points to a simple combination: shared notes, workers that coordinate, and an orchestrator. Gray focuses on the pace of incidents; Krebs distinguishes encountering the tool from a confirmed breach.
- Shared tooling is not shared attribution. CrowdStrike documented use in a South Korean finance campaign; a later FBI alert describes multiple actors and campaigns, not one coordinated incident.

**Andy's security takeaways:**
1. Shrink what’s exposed: know what is internet-facing, give temporary tools an owner and an expiry, and remove what you no longer use.
2. Limit what one credential can reach: separate build, deploy, and recovery access; prefer short-lived, scoped credentials.
3. Drill the response: use a test credential to measure detection and revocation; prove you can restore from a backup the same identity cannot alter.

**Closing question:** If a deployment credential leaked today, what could it reach, how fast could you revoke it, and could you still recover?

**Handoff cue:** “That's the signal. Now let's get to the hot take.”

**Sources / production notes:**
- [Publisher notes](https://www.risky.biz/RB859/) · [CrowdStrike campaign report](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) · [FBI FLASH, Nov 13](https://www.ic3.gov/CSA/2026/261113.pdf) (postdates the episode).
- Optional cue points from the audio transcript (check video timing before playback): ~2:49 coordination; ~4:23 control; ~6:17 visibility and attribution.
- If short on time, skip playback and use the 4-minute rundown; keep the attribution distinction.

## 9 · Hot take — safety goes public (3.5 min)

**Visual cue:** `s-hot-take`. Receipt: same safe.ai capture as slide 5 (reuse disclosed on-slide).

**Segment talking points:**
- Proposition: the first frontier lab priced by the market will now report quarterly; guidance, not the signatories, is the real test of the safety brand.
- Quarterly pressure: does RSI stay "competitive advantage" or become risk-factor language?
- Mind-changer: first earnings call keeping the framing with RSI as upside — or an RSP update filed as an 8-K.

**Henry's talking points:**
- "Every frontier lab is becoming a reporting company. The safety case is about to be a line item in a 10-Q."
- "Watch which footnote disappears first."

**Henry landing line:** "If safety only ever appears in marketing and footnotes, the signatories were right."

**Andy fallback talk track:** See `speaker-notes.md` § s-hot-take.

**Handoff cue:** "Thank you to Heritage Telecom."

**Sources / production notes:**
- Receipt: assets/images/s5-misanthropic.png — reuse of slide-5 capture, disclosed on-slide.
- Caveat: this is opinion, not news — no new factual claims beyond the week's receipts.
- Cut instruction: none — never cut the hot take.

## 10 · Sponsor — Heritage Telecom (1.5 min)

**Visual cue:** Heritage sponsor video, manual play; poster fallback.

**Segment talking points:** Carrier-side partner for teams that ship on connectivity.

**Henry's talking points:**
- "Thanks to Heritage Telecom — slot two this week."
- "heritagetel.com."

**Henry landing line:** (none)

**Andy fallback talk track:** See `speaker-notes.md` § s-sponsor-heritage (includes the deliberate "Thank Heritage— sorry, habit" recovery gag; keep it).

**Handoff cue:** "Watch list and goodbyes."

**Sources / production notes:** Sponsor assets hash-verified carry-forwards. Do NOT correct Andy's scripted recovery line — it is intentional.

## 11 · Watch list + close (1.5 min)

**Visual cue:** `s-watch`. Three watch cards + social CTA + Discord QR (verify resolves to weeklyclaw.ai/discord).

**Segment talking points:**
- Watch 1: Anthropic offering closes Nov 20; 147M-share option could push primary past $90B.
- Watch 2: OpenAI Nov-20 platform approval rule — verify docs before air or cut the mention.
- Watch 3: Nov 25 weights wall (Qwen4-Max-Preview retirement + ERNIE 5.5 Flash); Nov 28 Gentlemen ransomware countdown (Ep40 window).

**Henry's talking points:** - "Three dates: November 20, November 20, and November 25."
- "Discord for the receipts between shows."

**Henry landing line:** "Back next Friday, November 27."

**Andy fallback talk track:** See `speaker-notes.md` § s-watch.

**Handoff cue:** Close → sources slide rolls through outro.

**Sources / production notes:** No recap of the episode elsewhere (recap lives once, here, as the close line). QR check pre-air.
