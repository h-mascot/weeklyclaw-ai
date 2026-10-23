# Weekly Claw #35 — Host Cheat Sheet (rev2)

**Air:** Friday, October 23, 2026 · 4:00 PM ET · hard stop 45:00
**Deck:** `episodes/35/showprep/revs/deck.rev2.html` · 10 slides · EP23 authority styling
**Rev2:** video anchor dropped by host order (Andy + Henry, Oct 23) — run is 31:00 scripted.
**Thesis:** Open weights won the benchmark. Then they lost the building.

## Slide map

| # | Slide | Owner | Clock | One-glance note |
|---|-------|-------|-------|-----------------|
| 1 | s-title | hold | pre | Thesis + sponsors, Herald first |
| 2 | s-cold-open | Andy→Henry | 0:00–2:00 | 5 hooks, arc strip |
| 3 | s-sponsor-herald | Andy | 2:00–3:30 | Approved copy only |
| 4 | s-seg-grid-a | **Henry** | 3:30–11:00 | DeepSeek bench / MiniMax / DHS / Google |
| 5 | s-seg-grid-b | **Henry** | 11:00–18:00 | Anthropic S-1 / CUDA moat |
| 6 | s-seg-grid-c | **Henry** | 18:00–22:00 | Cairn / LiteLLM+Railway / xAI defense |
| 7 | s-hot-take | both | 22:00–26:00 | Taste vs accountability |
| 8 | s-sponsor-heritage | Andy | 26:00–27:30 | Approved copy only |
| 9 | s-watch | Henry→Andy | 27:30–31:00 | 3 watches · **Andy's single recap** |
| 10 | s-sources | non-air | — | Receipts; copy for the show notes |

## Cold open — Andy's 5 hooks (0:00–2:00)

1. Open model beats GPT-5.6 Sol on Terminal-Bench 4.0 (42.3 v 39.9; Opus 5 at 51.8)
2. DHS evicts DeepSeek from all federal civilian IT (notice 2026-21447)
3. Anthropic draft S-1: $16.3B revenue, $80.7B loss, $750B compute ceiling
4. CUDA moat attacked at three layers in one week (TorchNeuron / TorchTPU / Tenstorrent $1.5B)
5. Agents breach 100+ companies for ~$50 a breach; LiteLLM wheel ships a key stealer

**Handoff line (Andy):** "Every week we tell you the frontier moved…" → sponsor → Grid A.

## Grid A — Henry (3:30–11:00)

- **A1 DeepSeek V4.1-Flash-1017.** MIT, ungated, 1M context, repo live 10-17. TB4.0 **42.3** (Sol 39.9, GLM-5.3 37.9, Opus 5 51.8). Search & Fetch API: $0.75/1K, free in Claude Code/Codex until Nov 1.
- **A2 MiniMax M3.1 Flash.** Blog 10-19. Space Bunny = early version, 200T tokens processed anonymously. DeepSWE 73.7%, $0.15/$0.60 pricing. **Weights "later" — say so.**
- **A3 DHS exclusion.** Federal Register 2026-21447, 10/20. Vendors carry the transitive burden.
- **A4 Google Cloud swap.** GPT-6 family into Model Garden; same-day retirement of 16 managed open models.
- *Cut order: A2 first, then fold A1b into A1.*
- Caveat to say on air: DeepSeek/MiniMax benches are vendor-run; no independent reproduction yet.

## Grid B — Henry (11:00–18:00)

- **B1 Anthropic S-1 (draft).** H1 rev **$16.3B** (v $1.1B YoY); loss **$80.7B** but ~$72B is non-cash note accounting; real infra burn ~**$9B**; ceiling **$750B** (Google $111B, AWS $110B, MSFT $31B); 2 customers = ~20% of revenue.
- Framing: the loss is mostly paper; the commitments are not.
- **B2 moat.** TorchNeuron (`.to('neuron')`, 89% v 46% vendor claim) + TorchTPU (Apache-2.0, native vLLM/SGLang at Meta) + Tenstorrent **$1.5B @ $6.2B** + Reuters: 3M+ RTX PRO 5500 orders from ByteDance/Alibaba/Tencent (~$35B+, maybe 5–10% filled).
- **B2b reported only:** The Information says Huawei engineers inside DeepSeek co-designing chips. Single source, paywalled — say "reported."
- *Cut order: B2b first, then fold order-book into B2 one-liner.*
- Caveat: S-1 numbers are from a confidential draft reviewed by wires; nothing filed.

## Grid C — Henry (18:00–22:00)

- **C1 Cairn campaign.** Reuters+NorForge: 1,200+ sites, 100+ breached (Deere, SharkNinja, Cummins), ~23h autonomous probing per success, "a few thousand dollars" of tokens → on the order of $50/breach (our arithmetic — say "on the order of"). Same day: ARCYBER ECHOTRIBBLE procurement docs (whitepaper-phase).
- **C1b callback:** worker string was `claudecode_deepseek-v4.1` — the same model DHS excluded.
- **C2 supply chain.** LiteLLM 1.107.0 built from lookalike repo by GitHub CLI token theft from 3 maintainers; `cook.pth` stealer + `sitecustomize` hourly backdoor; PyPI+Docker pulled same day. Railway (10-21): encrypted env vars accessed, some decrypted; all deployments paused; "series of attacks targeting platform companies to compromise AI inference providers."
- **C3 defense.** xAI IncidentWatch (5-min scans) + IncidentSweep (batch close, human gate): 204 tickets in ~10 min, Sept 18 incident. Vendor-reported.
- *Cut order: C3 first, then fold C1b into C1.*
- Caveat: Reuters couldn't establish data exfiltration; Railway final report pending.

## Hot take (22:00–26:00)

- **Henry:** taste is the last moat — scarcity moved from writing code to judging what to build. Dev-tools money already moved to review/evals/observability.
- **Andy steelman:** accountability compounds, taste doesn't. Who holds keys, who carries pager. $50-a-breach is a staffing gap, not aesthetics; LiteLLM survivors were saved by a rotated key.
- **Verdict:** taste gets you there; accountability keeps you in business. Only one is cheap to hire.
- Mind-changer: a taste-led non-engineer team running production for a year, no engineer on pager.

## Watch + close (27:30–31:00) — recap ONCE, Andy

1. Anthropic prospectus expected public ~**Oct 25** — watch the $750B ceiling.
2. Promised weights: Mistral Large 4 (end of Oct) and MiniMax M3.1 Flash ("later").
3. DeepSeek Search/Fetch free window ends **Nov 1** — check harness volume.
- **Andy closes: one recap pass, then next show Friday Oct 30 4 PM ET + follow CTA. Never recap the recap.**

## Always

- News segments are Henry-led, always.
- Exactly one recap, end of show, Andy.
- Every caveat printed in the notes is a say-on-air caveat.
- Sources slide is the receipt backstop; manual-open paywalls: WSJ, The Information, Reuters (via WHBL).
