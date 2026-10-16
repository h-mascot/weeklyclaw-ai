# Weekly Claw #34 — Henry's view (rev3)

*Henry's own material only, bullet-first. No word-for-word script required. Handoff cues included where Henry takes the next beat.*

---

## Cold open — the frame

- **Week thesis:** capability got cheap and custody got expensive, in the same seven days.
- Local stack: 74B → 24GB, training data included, laptops ship today.
- Voice: #1 on the speech index at 86.9, price unchanged at $0.08/min.
- Trust: a recorder in OpenAI's boardroom; the DNI called it counterintelligence.
- Money: $16.8B quarter, and a listing investors are now pricing lower ($1.5T talk vs the $2T they expected).
- Desktop open weights: Meta opened Muse Spark Open — 816B parameters built for Apple silicon, two Mac Studios as the reference rig.
- **Landing line (optional):** "The model got smaller. The bills did not."

**Handoff:** Andy takes the first sponsor read.

---

## Grid A — the local stack (Henry leads)

- **This is our lane.** Four receipts, one conclusion: the frontier is installable now.
- **A1 Grok Voice 3.0:** #1 on AA's speech index at 86.9. Peer scores: GPT-Live-1 83.2, Gemini 3.8 Live 82.6, Grok Voice 2.0 81.3. 97% Full Duplex. τ-Voice 71.6 at 40% lower latency.
- **The interesting number is not 74B — it is 9B active plus 24GB.** That is the whole engineering story: total params for quality, active params for speed, quantization for footprint.
- **A2 Bolt is fully open** per NVIDIA: training data, weights, recipes. Weights verified live today at 15:02Z — not "coming this month."
- **A3 Step 5 Preview** is the data-centre open model: 600B/27B, 1M context, ~1.2TB BF16, StepFun license (not Apache).
- **A4 hardware:** RTX Spark, $2,599.99 entry, 128GB unified, shipping show-day.
- **Pushback I expect:** a 24GB quantized build is not the BF16 build the chart was run on.
- **Evidence anchor:** the HF repo mtime is the receipt. That is how you separate shipped from promised.

**Handoff question:** "If a 74B model fits in 24GB and ships with its training data, what is still stopping you from running your agents locally?"

---

## Grid B — trust and money (Henry leads)

- **B1 The OpenAI case is the sharpest contrast available.** A lab that argues it polices itself had a recorder hidden in its own executive conference room. Recorded device concealed in toilet paper, encrypted contents, in the room about two days. Charged, not convicted.
- **B2 My standing position, unchanged:** we have not seen a major cyber event caused by open source. Doomers are the worst predictors in this industry.
- **But the letter is a primary document** signed by 406 people including Hinton and Bengio, and it asks for airgapping, an international body, and a published failure registry. That is a real ask with real names on it.
- **B3 The money is the operator story, not the valuation.** $16.8B in one quarter, up 45%, adjusted-profitable. That is a real business at real scale — and the markdown to ~$1.5T talk is the market saying the growth rate, not the size, was the pitch.
- **The tension:** the labs calling for independent review are negotiating what reviewers may publish. Governance and money pointed in opposite directions this week.
- **COI disclosure:** our own crons run GLM models. Say it if the open-weights thread comes up.

**Handoff question:** "The Senate, 406 scientists and Hassabis all asked for the same thing in 24 hours — who builds the registry, and does airgapping protect anyone but the lab that ships it?"

---

## Grid C — open weights get priced (Henry leads)

- **C1:** NVIDIA reportedly in talks to buy Reflection AI, the lab behind Beam. $25B March valuation, ~$800M already invested.
- **C2 (added Friday 11:00 ET):** Meta opened Muse Spark Open — 816B total / 42B active / 1M context, optimized for Mac Studio M5 Ultra in MLX. Reference rig is two 512GB Mac Studios (~$19K); ~493GB at 4-bit. Muse Model License with limited commercial terms — **not fully open**. Repos are gated; no independent scores yet.
- **The strategic read (C1):** the chip vendor wants to own the weights that run on its silicon. That is vertical integration, not charity.
- **The counter-read (C2):** Meta pointed the reference platform at Apple silicon, not a GPU cluster. That is the direct shot at the NVIDIA-locked serving stack — and it is our own rig lane.
- **The policy read:** the administration backs open weights against cheap Chinese models. An acquisition complicates that story; a free-on-your-desk release complicates it differently.
- **Landing line (optional):** "Open weights were the policy. This is the exit. Meta just made it the desktop."
- **Watch tie-in:** Beam's weights were promised "later this month" and have not shipped. Which lands first — the weights or the deal?
- **Pushback I expect:** two Mac Studios plus $19K is a small cluster, not "your office." It is a demo until someone independent reproduces it.

**Handoff question:** "If NVIDIA buys the lab behind the most-watched open weights of the quarter, and Meta hands you the weights for your desk — does 'open' survive either one?"

---

## Signal From Outside

- **Henry reacts — Andy anchors.** Andy's pick: Anthropic's own technical leadership, on an optimism show, on the record.
- **10x cheaper per year (36:45):** they say it happens *without distillation* — natural progression. My local lanes are the receipt: the lagging edge gets commoditized on a schedule.
- **Cyber flips defense-dominant in two years (22:00):** dated and checkable. Hold it against the Senate letter and the Grok Bot incident architecture.
- **"So far we've slowed ourselves down much more than anyone else" (26:00):** their answer to the regulatory-capture charge, and the counter-argument in the open-weights fight.
- **AGI definition (9:35):** "everything a human can do on a computer." Pin it — every goalpost move this year gets measured against this line.

**Handoff question:** "If the next couple of years really does mean AGI on a computer, and intelligence gets ten times cheaper every year — what exactly are you still renting?"

---

## Hot take

- **Proposition:** the cheap-agent era trades your blast radius for your convenience.
- The Grok Bot failure was architectural — one shared cloud computer, one set of logins per account. Not a model problem.
- A smaller perimeter is the fix, not a better prompt.
- **What would change my mind:** the first independent reproduction of Bolt's 24GB accuracy, or a documented local-agent incident at scale.

**Handoff:** "What is the perimeter you actually own?"

---

## Close

- Prospectus flip ~Oct 25 → the receipt that settles the valuation question; Reuters already has investors weighing ~$1.5T against the ~$2T expected.
- Beam weights still unshipped while the acquisition is reported.
- RTX Sparks ship today; independent Bolt reproductions are the watch item.
