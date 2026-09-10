# WeeklyClaw Episode 29 — Henry section

Concise talking points, optional lines, and handoff cues. Full research + caveats + Andy prose live in `agenda.md` and `speaker-notes.md`. Every What Happened This Week card is Henry-led; the Hot Take is a debate; Signal From Outside is Andy-led.

**Show:** Friday 2026-09-11, 4:00 PM ET
**Target runtime:** 32–38 minutes (scripted total 32:00)

---

## Cold open · 1:30 · `s-cold-open`

**Talking points:**
- "Agents left the chat" is not a slogan; it is where the receipts landed.
- Not every "AGI moment" is a proof. OpenAI's Navier–Stokes is a claim under review.
- Half the timeline is arguing about the argument; we save that for the hot take.

**Optional line:** "The models moved. The boundaries moved. The argument about the argument moved even faster."

**Handoff:** "Heritage first, then I open Grid A."

---

## Sponsor: Heritage Telecom · 1:00 · `s-sponsor-heritage`

**Owner:** Henry.

**Talk track:** "This episode is brought to you by Heritage Telecom. While the AI industry keeps bundling your chips, your models, and your monthly seat, Heritage does the thing it is actually good at: UCaaS and VoIP phone service for businesses that just need their calls to work. Independent, boring reliability, zero telemetry. Find them at heritagetel.com."

**Handoff:** "Grid A: agents left the chat."

---

## Grid A · What Happened This Week · 8:00 · `s-seg-grid-a`

Walk left→right, top→bottom. One dominant artifact per card. Details live in `speaker-notes.md`.

### A1 · OpenAI's 10,000-agent Navier–Stokes claim · 2:00

**Talking points:**
- 10,000 agents. 88 hours. 130 billion output tokens. 165-page paper. Public Lean 4 repo.
- CLAIMED — expert review pending. Nature reported the announcement; Nature does not verify the proof.
- Read the Lean repo like an audit trail. One commit on 2026-09-08, Apache-2.0, publicly diff-able.
- Sibling receipt: MIT's quantum-lab case study — Sol + Codex + six-qubit chip, closed-loop measurement.

**Optional line:** "It is not that AI did math. It is that AI wrote enough proof-attempt code that a person can now read it before the model writes ten thousand more."

**Handoff:** "Henry, if the proof holds the ceiling moves. If the workflow holds the floor moves. Which one changes more?"

### A2 · Meta launches Muse behind a Sentinel and a cloud VM · 2:00

**Talking points:**
- US launch on iOS/Android/web/WhatsApp, 2026-09-08. Personal agent powered by Muse Spark.
- Each user gets an isolated Linux cloud VM. Credentials outside the harness. Sentinel model can veto, agent cannot override.
- Reuters ran adverse internal tests before launch and reported stalls and unauthorized data exposure. Meta says it hardened; up to $300K bug bounty. No public independent audit yet.
- "The Sentinel is the product. The chat is not."

**Optional line:** "The agent moved from a chat window into a cloud computer."

**Handoff:** "The agent moved into a VM. Now the humanoid moved into a factory."

### A3 · XPENG IRON production line · 2:00

**Talking points:**
- Line commissioned. XPENG says 80%+ core-process automation.
- First assembled humanoid walked off under its own control.
- Year-end mass-production target; external customer deliveries in 2027.
- CnEVPost confirms commissioning; explicitly says this is production-line manufacturing, not mass production.
- Capacity and price undisclosed. "World's first" is XPENG's framing.

**Optional line:** "The interesting frame is not the humanoid. It is the assembly line."

**Handoff:** "Physical side of agents leaving the chat. Now the biological side."

### A4 · DeepMind AlphaGenome Atlas · 2:00

**Talking points:**
- 9 billion pre-computed single-letter DNA-change predictions. ~1 PB total. Portal + API + Antigravity skill.
- New AlphaGenome Variant Impact score spans coding and non-coding regions.
- Nature reports the launch and calls the outputs predictions. Launch-team results include partner-reported 22% more non-coding associations in a UK Biobank analysis.
- PREDICTION — NOT CLINICAL EVIDENCE. Not approved for clinical use.

**Optional line:** "You don't need a bigger model. You need to spend the compute once and let every lab query the answer."

**Handoff:** "Grid A: agents left the chat. Grid B: the walls around them became products."

---

## Grid B · What Happened This Week · 8:00 · `s-seg-grid-b`

### B1 · DeepSeek V4.1-Flash · 2:00

**Talking points:**
- 552B multimodal MoE, Causal Encoder–Decoder, 8B active input / 16B active output. MIT-licensed weights live; `deepseek-flash` API live.
- Vendor-reported: ≈1/4 HBM, ≈1/8 SSD cache vs prior V4-Flash. Treat the official benchmark table as a mixed task-level comparison, not a single quality or cost ratio.
- HF repo verified: created 2026-09-10 02:17 UTC, 1M positions, 384 experts, native vision, MIT, no gate, 48 shards.
- On 2026-09-14 V4-Pro API traffic is scheduled to migrate to V4.1-Flash.
- All performance/efficiency numbers are vendor-reported. Wait for independent runs.

**Optional line:** "The launch is not the leaderboard. The launch is the cache."

**Handoff:** "The boundary this week was cache. The next boundary is capital."

### B2 · Mistral €3B Series D · 2:00

**Talking points:**
- Samsung led. EQT and PSG co-led. ASML on the record. €3B round at ≥ €21B post.
- Nearly doubled valuation from €11.7B Series C. Quartz independent confirmation.
- Company framing: sovereign frontier research + owned and rented compute + international reach + 125+ enterprise customers.
- "Largest European tech equity round" is Mistral's characterization.
- Tension: strategic Samsung/ASML backing funds a European alternative; scale still depends on global chip supply.

**Optional line:** "Sovereignty is now a capital expense."

**Handoff:** "From strategic capital to strategic peace treaties. Suno just signed with the labels that sued them."

### B3 · Suno v6 with former plaintiffs · 2:00

**Talking points:**
- v6, v6-wild, free v6-mini. Partners: Warner Music Group, BMG, Believe.
- From-scratch training with licensed partner music + user data. Reuters/Axios/The Verge corroboration.
- Feature layer: local edits, mashups, sampling, lyric replacement, text/audio/image/video-to-song.
- Prior models will be retired. Warner and BMG were plaintiffs/adjacent-to-plaintiffs; now development partners.
- Dataset scope, artist compensation, and opt-in artist product terms are undisclosed. Litigation continues elsewhere.

**Optional line:** "This is not a settlement. This is a licensing product."

**Handoff:** "That is the media boundary. Now the labor boundary — Andy, the Economist has the first honest number."

### B4 · AI jobs boom (with Stanford asterisk) · 2:00

**Talking points:**
- Economist estimate: ≈1M US AI-linked jobs created vs ≈200K AI-attributed layoffs since mid-2023.
- Burning Glass: about 1% of professional jobs are AI-specific. LinkedIn: ~640K new AI-specific jobs 2023–25.
- Stanford SIEPR independently finds aggregate effects small so far but flags weaker entry-level hiring in AI-exposed occupations.
- Goldman expects displacement risk to rise as adoption spreads.
- Estimates. Not a census. Not proof the long-run balance stays positive.

**Optional line:** "Nobody has to lose their job for someone else's argument to be right."

**Handoff:** "Now the video anchor — an agent that keeps working while you interrupt it."

---

## Signal From Outside · 6:00 · `s-signal-outside`

**Owner:** Andy leads (permanent anchor). Henry adds operator take after Andy walks the demo.

**Henry's operator take (after Andy runs the beats):**
- The win is not better speech. It is keeping conversation and execution alive at the same time.
- Two loops — live dialogue Cerebellum, async work Brain — is closer to how a human collaborator handles interruption.
- Apache-2.0 weights, runnable two-GPU config, active GitHub pushes. Reproduce, don't repost.
- Author-reported Pass@1 is 0.400. The dataset link says "coming soon" while the abstract says data is released. Both flags on air.

**Optional line:** "The voice agent stopped being a demo the moment it stopped waiting for you to finish."

**Handoff:** "That is where the research is. Now the argument about the argument."

---

## Hot Take · 4:00 · `s-hot-take`

**Motion:** "AI safety is becoming a religion with a business model."

**Henry side — challenging doomer incentive structures:**
- Anthropic's public claims scaled with IPO timing. Coxon's resignation post crossed ~120M views on X in a day. That velocity is not neutral.
- The Effort's Sep-4 report documents $3.3M in FLI-linked grants to religious NGOs, including $200K to The Gospel Coalition and $125K to Faith Matters. The ledgers are inspectable. "Coordinated propaganda" is The Effort's interpretation; the payments are real.
- Cal Newport's Sep-10 NYT column names the Yudkowsky-lineage rationalists specifically.
- What would change Henry's mind: a serious safety org publishing budget, funding sources, and a policy that measures capability harm rather than movement growth.

**What Henry does not do on-air:**
- Repeat unattributed conspiracy claims from the X stream.
- Treat engagement velocity as evidence of coordination.
- Attribute private motives to specific researchers.

**Optional line:** "You do not get to demand a global capability pause and also expect no one to check the collection plate."

**Handoff:** "One rebuttal each. Then Andy takes Herald."

---

## Sponsor: Herald Labs · 1:00 · `s-sponsor-herald`

**Owner:** Andy. Henry silent unless prompted for a beat about Entity.

---

## One to Watch + close · 2:30 · `s-watch`

**Talking points:**
- The migration: 2026-09-14 — DeepSeek moves V4-Pro traffic onto V4.1-Flash. Deployment receipt.
- The audit: first independent mathematician who publicly checks the OpenAI Navier–Stokes Lean formalization.
- The line: XPENG's next monthly disclosure — is there a monthly capacity number behind "commissioned"?

**Optional line:** "Three receipts to check. Same time next Friday."

**Close (Andy delivers the recap):** Andy owns the one-time recap. Do not repeat the recap; do not add a second recap in the sign-off.

---

## Cut order Henry should know

1. Compress A4 (drop AVI-score sub-beat).
2. Compress B4 (drop Stanford entry-level side quote).
3. Compress Signal (skip demo cue; go to architecture beat).
4. Compress A3 (drop 2027 external-delivery timeline).
5. Never cut Signal From Outside or Hot Take entirely.

---

## Pin discipline

- Do not promote OpenAI Navier–Stokes to "settled proof."
- Do not repeat "world's first" on XPENG without attribution.
- Do not describe AlphaGenome outputs as clinical.
- Do not repeat DeepSeek benchmark or cache figures without the vendor-reported label.
- Do not launder Coxon's testimony into fact on-air.
