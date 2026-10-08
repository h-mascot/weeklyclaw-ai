# Weekly Claw #33 — Show Agenda (rev1)

- **Air:** Friday, October 9, 2026, 16:00 ET / 21:00 UK · **Target runtime:** 32:00 (hard stop 45:00)
- **Ownership:** Henry leads ALL "What Happened This Week" segments (grids A+B, SFO bridge, hot-take proposition, One to Watch). Andy: cold open, both sponsor reads, hot-take steelman, and his ONE recap at the close (no recap-of-recap).
- **Sponsor order:** 1) Herald Labs (after cold open) → 2) Heritage Telecom (before close). Rotation inverted from #32.
- **Signal From Outside (locked per contract):** Theo, **"I love Ultrafast (it's unusable)"** — `pJljViiUEPw`, Oct 6, 28:17, 128,624 views. Manual open only. Cues spot-check before air.
- **Show rules in force:** five stories is a target not a quota (8 cards, 2 grids) · no autoplay · verified provenance/caveats on every card · Andy material has complete fallback prose · hot take does not repeat any grid proposition · no alternating dialogue forced.

| # | Segment | Owner | Budget | Beats |
|---|---|---|---|---|
| 1 | Cold open | Andy | 0:45 | 3 hooks + episode frame |
| 2 | Sponsor: Herald Labs | Andy | 1:30 | read |
| 3 | What Happened · Grid A — "The trillion-parameter open-weight promise" | Henry | 8:00 | 4 cards × ~2:00: Mistral Large 4 → Beam → 722 manuscripts → math reception |
| 4 | Signal From Outside | Andy intro → Henry bridge | 6:00 | Theo Ultrafast; Henry's token-per-task discipline |
| 5 | What Happened · Grid B — "Agents get graded, routed, and locked down" | Henry | 8:00 | 4 cards × ~2:00: ThinkingBox → ReviewBench → Grok Bot routing → Apple FDA |
| 6 | Hot take | Henry prop · Andy steel | 4:00 | "The free-compute era ended on schedule — and that's healthy." |
| 7 | Sponsor: Heritage Telecom | Andy | 1:30 | read |
| 8 | One to Watch + close | Henry watch → Andy recap | 2:15 | Alibaba/DeepSeek Oct 10 deadline + Discord QR → Andy's single recap |

**Card beats (Henry, grid A)**

1. **Mistral Large 4** — 1T total / 52B active, natively multimodal (Mistral's post). Public-preview API now at $1.36/M in, $4.18/M out — matches AA exactly. AA independent index: 38, above the 26 median — and "very verbose" (200M eval tokens vs 81M median). "Le Chonk" is Mistral's own name. **Weights NOT out**: "weights drop end of this month" while red-teaming runs. "Surpassing frontier closed models" is Mistral's claim; 38 is the independent number. The gap is the beat.
2. **Reflection Beam** — 501B total / 23B active sparse MoE, agentic coding focus (Reflection, Oct 5). **Weights NOT out**: "weights, technical report, model card… later this month"; early access is a select group. The DeepSWE/HLE/Terminal-Bench chart is Reflection's own. Caveat ON AIR: self-reported, weights pending, independent runs after weights land. Both grid-A leads are promises — that's the honest frame, not "open weights shipped".
3. **OpenAI 722 manuscripts** — `github.com/openai/math`: 722 papers, 372 result families, 235 with Lean formalizations, Apache-2.0. Zero peer review. One-night dump from a secret internal frontier model.
4. **Math reception** — Williams–Alman (arXiv 2610.06783): deterministic 3SUM in n^1.9992 and APSP in n^2.9995 — humans refuting 50-year conjectures the same week. Aaronson's "Mathocalypse" and Tao's "Math 2.0" — **ON AIR: open before quoting** (Aaronson post is Cloudflare-gated; quote only after manual open). Name-drop C1: Muse Spark's six papers incl. five open problems, plain chat, no scaffold.

**Card beats (Henry, grid B)**

5. **ThinkingBox** — Microsoft + HF ship a stateful-reliability benchmark: grades the records agents leave, not their sentences. Receipt: 121,680 valid trials across 12 models, 79,853 failed — two-thirds. Paper 2608.19741.
6. **ReviewBench** — GitHub ships an open AI-code-review benchmark from 103.9M PRs; leaderboard live with grounded/augmented precision+recall.
7. **Grok Bot routing** — Musk, Oct 7: "Going forward, @SpaceX will use the best back end model for any given task, including Claude Opus 5.5, MidJourney, Suno… Whatever is most likely to give you the best outcome." 106.1K likes. The harness-wins beat: the loudest model-lock founder concedes routing to the best model. Tie to Henry's standing call.
8. **Apple FDA** — Apple Developer News Oct 2: full-disk-access apps face per-app user prompts; silent paths close. Apple's own text blames autonomous agents reading everything. The agent boom now sets desktop OS threat models.

**Hot take (C11)** — Henry: Gemini's free tier quietly drops to Flash-Lite on air day; OpenAI halves Pro 200 limits Oct 30; "With 6.1 you get 2.5x more usage on the new 10x plan." Subsidized-compute era ends; builders who learned on subsidies face real unit economics — healthy. Andy steelman: subsidies built the hobbyist pipeline; ending it mid-flight kicks the ladder; Flash-Lite free tier is a downgrade disguised as a tier. Mind-changer: if free-tier retention holds after Oct 9, the subsidy was never load-bearing. **Caveat on air:** tier changes rest on 9to5Google + OpenAI help-center pages; no vendor-dated primary.

**One to Watch (C32)** — Alibaba retires every third-party model from Model Studio **Oct 10 — the day after we air.** DashScope migrations break Saturday. Irony: DeepSeek-V4.1-Flash is served on rival Qwen's consumer platform while Alibaba delists everyone else's.

**SFO cues (Theo, spot-check before air)** — manual open `youtube.com/watch?v=pJljViiUEPw`:
- 0:00–0:40 — live Astra app edit in real time ("make it light mode and funnier" → updates as he types).
- 1:00–1:17 — the receipts: Astra $50/M output tokens; Ultrafast $300/M; long-context $450/M. "These bills are actually insane."
- ~2:40–3:10 — Graptile/T-Rex sponsor bridge (skip or fold into the graded-agents frame).
- Later: rate-limit burn + verdict — **open before air and re-locate timestamps** (auto-caption times drift).

**Henry bridge into SFO:** his Oct 8 post quoting token-use comparisons (Haiku 5.5 max ~162K output tokens/task vs GPT-6 Luna max ~50K) — Theo's "tokens per second is meaningless" thesis, with Henry's own per-task data as the receipt.

**Andy fallback prose (if video fails):** complete paraphrase lives in `andy-section.rev1.md`; poster on deck is the fallback visual; never autoplay.
