# Weekly Claw #35 — Henry Section (rev2)

**You lead:** cold-open frame share, all three news grids, One To Watch, hot-take proposition, final verdict share.
**Host note:** the video anchor does not air this week (Andy drop + Henry scope note, Oct 23) — Grid C hands straight to the hot take.
**Andy owns:** cold-open opener, sponsor reads, hot-take steelman, the single close recap.

---

## Cold open (your half, after Andy's hooks)

One line to land the arc: "The open lane had its best benchmark week of the year — and its worst week for places to run it." Then let the arc strip carry the eye.

## Grid A — open models won the benchmark, lost the catalogue (3:30–11:00)

**A1 DeepSeek V4.1-Flash-1017 — your lead card.**

Receipts: HF repo created 2026-10-17T02:40:38Z, MIT, ungated, image-text-to-text, 1M context. Model-card bench table (their own run):

| Benchmark | 1017 | DS-V4.1-Flash | K3 | GLM-5.3 | GPT-5.6 Sol | Opus 5 |
|---|---|---|---|---|---|---|
| HLE w/o tools | 42.6 | 44.01 | 33.2 | 35.4 | 40.5 | 50.3 |
| Terminal-Bench 4.0 | **42.3** | 31.2 | 12.6 | 37.9 | 39.9 | 51.8 |
| DeepSWE v1.1 | 77.0 | 74.2 | 67.5 | 68.9 | 72.0 | 74.0 |
| ProgramBench | 29.1 | 26.3 | 20.3 | 25.9 | 30.0 | 28.0 |

Story to tell: 1017 is the first open release to clear GPT-5.6 Sol on an agentic benchmark — Terminal-Bench 4.0, Claude Code harness, 42.3 vs 39.9 — while Opus 5 still holds 51.8. Say "vendor-run" once. Note the odd engineering: no Jinja chat template; prompts go through a Python `encoding/` reference implementation, and DeepSeek shipped `deepseek-recipe` (Rust + Python bindings) to handle it. Also their own table shows the HLE-without-tools regression vs V4.1-Flash — honest card, that's why it's credible.

Your operator lane (say it as experience, not benchmark): you've been running the 1017 build on 2× DGX Spark since the repo dropped — the question moved from "can I run the frontier" to "where am I allowed to."

**A1b Search & Fetch APIs.** Changelog 10-17: `POST /v1/tools/search`, `POST /v1/tools/fetch`, bearer auth, $0.75 per 1K successful calls each; failures and empty results free; QPS 100/25 account-level; free inside DeepSeek Harness, Claude Code, Codex until 2026-11-01 00:00 Beijing. Fetch returns Markdown. Price anchor: they claim ~6× under Brave Search's $5.00/1K. If asked "why care" — it's the same play as their model pricing: commoditize the layer above the weights.

**A2 MiniMax M3.1 Flash.** Blog 10-19. The reveal: "Space Bunny," the deployment that "processed more than 200 trillion tokens while operating anonymously," was an early version of M3.1 Flash. Vendor figures: DeepSWE v1.1 73.7%, CyberGym 82%, OSWorld V2 61.7, BankerToolBench 76.2, AutomationBench-AA top among Chinese models; 200+ TPS output; $0.15/$0.60/$0.015 pricing. **Weights "will be released later" — flag it; this is a service launch wearing open-model language.** First cut if tight.

**A3 DHS exclusion.** Federal Register 2026-21447, published 10/20/2026, Homeland Security: exclusion and removal of DeepSeek products from federal civilian executive-branch IT and procurements. Reuters/Verge reported 10-19. The line that matters to your audience: it's transitive — vendors into federal systems now have to show no DeepSeek anywhere in the dependency chain, including inference routing. Four days from best-bench-of-the-week to federal eviction.

**A4 Google Cloud.** Oct 21, both directions at once: GPT-6 Astra / GPT-6.1 Sol / GPT-6.1 Luna into Model Garden (private preview, Marketplace single-invoice), and a same-day deprecation notice retiring all managed open-model endpoints on Gemini Enterprise Agent Platform — sixteen models across DeepSeek, Qwen, Kimi, GLM, Llama, MiniMax, gpt-oss. Self-deploy on GKE/Vertex still allowed — it's a managed-service retreat, not a ban. Tie-off: the hyperscaler that hosted the open lane is now selling the closed one on invoice.

## Grid B — the compute bill and the moat under it (11:00–18:00)

**B1 Anthropic draft S-1.** Nothing is filed; figures are from the confidential draft reviewed by WSJ/Reuters — say that. The numbers: H1-2026 revenue **$16.3B** (from $1.1B a year ago); net loss **$80.7B**, ~$72B of it non-cash convertible-note accounting; actual H1 infra spend ~**$9B** (v $7.3B for all of 2025); possible future compute commitments up to **$750B**, non-cancellable chunks: Google $111B, AWS $110B, Microsoft $31B; ~**20% of revenue from two customers**; investors at the Oct 14 pre-IPO meeting weighed ~$1.5T against ~$2T expected for the November listing.

Two-beat frame: (1) the loss is mostly paper — the accounting converts, the commitments don't; (2) $9B of real burn has to be earned while three of your four biggest suppliers are competitors and a fifth of revenue rides on two customers. That's the IPO story in one breath.

**B2 the CUDA moat, attacked at three layers.** Framework layer: Amazon's **TorchNeuron** (Apache-2.0; `.to('neuron')`; Amazon claims 89% of top-100 text-gen architectures work vs 46% under Optimum Neuron) and Google's **TorchTPU** (open source, `torch.device("tpu")`, co-developed with Meta, native vLLM/SGLang at Meta, Apache-2.0). Capital layer: **Tenstorrent Series E $1.5B at $6.2B**, led by Trace Capital and Innovation X, with ARK, Fidelity, Morgan Stanley, SanDisk, Tether. Demand layer: Reuters — ByteDance, Alibaba, Tencent ordered **3M+ RTX PRO 5500s at ~$11,400 each ($35B+)**, total Chinese orders above 6M against planned production, one source says Nvidia may fill only 5–10%.

**B2b (reported, single-source):** The Information says Huawei engineers are stationed inside DeepSeek co-designing future AI chips. Corroborated only as a headline (DigiTimes/Techmeme). Say "reported," move on.

Synthesis line to land: the compute story and the open story are one story — the closed labs' $750B ceiling is why cheap open weights matter, and the CUDA stack loosening is why running them anywhere is finally plausible.

## Grid C — agents went to war, and the keyring got hit (18:00–22:00)

**C1 the attacker's unit economics.** Reuters exclusive (read via WHBL; original 401s to curl) + NorForge's own post: Chinese-speaking operator pointed Cairn agents at 1,200+ e-commerce sites from Sep 25; **100+ companies breached** — Deere, SharkNinja, Cummins among them; typical successful intrusion ≈ **23 hours of autonomous probing**; total campaign cost "a few thousand dollars" of tokens. "On the order of $50 a breach" is **our arithmetic** — attribute it as such, once. NorForge watched via 20+ exposed Cairn panels. Same day: The Intercept published ARCYVER procurement docs for **ECHOTRIBBLE** — self-directing, self-propagating offensive agents, "minimal oversight," whitepaper-phase only.

**C1b the callback (don't skip):** the Cairn worker string was `claudecode_deepseek-v4.1` — the same model family DHS excluded from federal IT hours later. Attackers don't care about procurement rules; they care about price per task.

**C2 supply chain.** GitHub issue 47826: attackers stole **GitHub CLI OAuth tokens from three LiteLLM maintainers**, built 1.107.0 from the lookalike `Berri-AI/litellm` repo, shipped **`cook.pth` credential stealer + `sitecustomize` RCE loader with an hourly backdoor**. PyPI removed the release; Docker `latest`/`main-stable` pulled same day. Railway, Oct 21: third party "may have accessed encrypted environment variables and, for some of them, obtained the decrypted contents"; **all deployments paused**; upstream AI providers asked to revoke every Railway-originated key; the campaign is "part of a series of attacks recently targeting platform companies with the aim of compromising AI inference providers." That sentence is the thesis of the segment — read it as written.

**C2b why it lands:** OpenCode (Oct 18), LiteLLM and Railway (Oct 21) — three supply-chain hits in seven days, all aimed at the same asset: the inference keyring.

**C3 the defense side.** xAI engineering, Oct 20: **IncidentWatch** scans the support queue every 5 minutes (15-min lookback) and alerts on spike; **IncidentSweep** flags incident-affected tickets, parks uncertain ones, closes the batch only after a human approves — Sept 18 incident: 204 tickets cleared in ~10 minutes with one engineer at the gate. Vendor-reported numbers. Tension line: offense is autonomous and cheap; defense is autonomous and gated — the gap between those postures is the operational argument of the year.

## One To Watch (32:30 onward)

Three dated tripwires, in order:

1. **The filing** — Anthropic's prospectus expected public ~**Oct 25**. Everything we aired is draft-stage; watch whether the $750B ceiling survives the public version.
2. **The promised weights** — Mistral Large 4 (public preview, ~1T total / 49B active, weights promised end of October) and MiniMax M3.1 Flash ("later"). Two dated promises; hold them to it on-air next week.
3. **The free window** — DeepSeek Search/Fetch free inside Claude Code, Codex, DeepSeek Harness until **Nov 1, 00:00 Beijing**. Then $0.75/1K. Check your harness call volume before the meter starts.

## Hot take — your proposition (22:00–26:00)

"Taste is the last moat." If a 2.5B-active open model writes production code and a $0.15/M API clears your ticket queue, the scarce input is judgment about what to build and what to throw away. Supporting color: dev-tools money already moved from editors to review, evals and observability — the places where judgment gets recorded. Andy steelmans accountability; your rebuttal closes on "own the consequences, not just the idea." Mind-changer to concede if he lands it: a documented taste-led non-engineer team shipping and keeping production for a year with no engineer on pager.

## Standing rules for your mic

- Every caveat in the notes is a say-on-air caveat — vendor benches, draft S-1, single-source Huawei, vendor-reported xAI numbers.
- One recap only, Andy's, at the close. You hand him the watch items and stay quiet.
- If time collapses: cut order is A2 → C3 → B2b → drop the free-window watch card. Never cut sponsors or the close.
