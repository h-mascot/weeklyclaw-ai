# Weekly Claw #36 — Agenda (rev2)

**Air:** Friday, October 30, 2026 · 16:00 ET (YouTube live) · Target 32–38 min (37:15 scripted), hard stop 45:00
**Hosts:** Henry Mascot (@HiM) · Andy (@AndyML)
**Studio deck:** 11 slides · three story grids · permanent Signal From Outside anchor

## Episode thesis

Wall Street became AI's landlord — and the numbers started lying. One week fused the money story and the trust story: banks securitized the chips ($63B SPV, ~$40B GPU lease), Meta filed ~$95B of equity paper hours after its Q3 beat, Anthropic's S-1 priced the era ($16.3B half-year revenue against a mostly-paper $80.7B loss) — while Grok and GPT picked opposite parties in ~500 races, ARC Prize showed a 37-point harness swing on the same model, an unreleased Claude chained 62 CVEs into a working browser exploit, and token efficiency became a product axis just as the token bill's unit economics collapsed.

## Run order

| Time | Segment | Slide | Lead |
|------|---------|-------|------|
| 0:00 | Show open + welcome | s-title | Andy |
| 0:40 | Cold open: the five hooks + episode arc | s-cold-open | Henry |
| 3:30 | **Sponsor 1: Heritage Telecom** | s-sponsor-heritage | Andy |
| 4:45 | Grid A — The money wall: SPV, Meta raise, S-1, earnings | s-seg-grid-a | Henry |
| 11:45 | Grid B — The trust cracks: model politics, ARC harness, Carbon #1 | s-seg-grid-b | Henry |
| 18:15 | Grid C — Agents go professional: Genie 4, red team, token efficiency | s-seg-grid-c | Henry |
| 24:30 | Signal From Outside: Jack Wotherspoon (Google DeepMind) — build your own team of managed agents | s-signal-outside | Andy |
| 30:30 | Hot take: "Stop asking which model is best. Start asking who owns your harness." | s-hot-take | Both |
| 33:30 | **Sponsor 2: Herald Labs** | s-sponsor-herald | Andy |
| 34:30 | One to watch: IPO window, Meta ATM, election-through-models | s-watch | Andy |
| 36:45 | Recap + sign-off | s-watch → s-sources | Andy |

**Note:** Exactly one recap, Andy-led, before the sources scroll. No recap of the recap.

## Stories covered

- **A1 · Broadcom/banks $63B SPV** — BofA, Blackstone, Citi, Morgan Stanley form an SPV to buy XPUs leased to Anthropic; Broadcom backstops residuals. Paired with SpaceX–Apollo ~$40B GPU lease. *(Primary: Broadcom IR release.)*
- **A2 · Meta ~$95B financing** — $22.5B forward + $12.5B mandatory convertible preferred now; ~$60B ATM planned, not raised. *(Primary: SEC FWP + 424B5.)*
- **A3 · Anthropic S-1** — $16.3B H1 revenue; $80.7B net loss (~$72.4B non-cash); $693M operating loss; $112.4B cash; Nasdaq ANT. *(Primary: SEC EDGAR.)*
- **A4 · Q3 earnings wall** — Alphabet Cloud $30.7B (+103%), capex $51.4B, FCF −$9.1B; Microsoft $10B/qtr OpenAI revenue; Samsung KRW 107.4T. *(Primary: Alphabet PDF, MSFT 10-Q, Samsung newsroom.)*
- **B1 · Model politics (Convovo)** — Grok → R 92%, GPT → D 97%, agreement <10% under its methodology. *(Primary: convovo.ai/ballot + TechCrunch.)*
- **B2 · ARC harness effect** — 99.9% provider adapter vs 62.7% neutral harness; arXiv companion. *(Primary: arcprize.org + arXiv 2610.04433.)*
- **B3 · Gemini 4 Carbon** — AA v5.0 #1 at 59.4; second Gemini 4 frontier in a month. *(Primary: blog.google + AA.)*
- **C1 · Genie 4** — real-time world model, native audio, mid-sim steering. *(Primary: deepmind.google.)*
- **C2 · Models that hack** — Anthropic red team: unreleased Claude chains 62 CVEs into Chrome RCE + 4 more chains; Cipher finds 4 EPICS zero-days in 3h49m. *(Primary: anthropic.com + causalsecurity.)*
- **C3 · Token efficiency as product axis** — Copilot Fusion GA (AA: $5.59 vs $11.42/task); Particle-1 token-frugal RL. *(Primary: github.blog + AA + particle.ai.)*
- **SFO · Jack Wotherspoon (Google DeepMind) — "Build Your Own Team of Managed Agents"** — coding agents in cloud sandboxes from one API call: Interactions API, Antigravity harness, shared environments, uploaded skills + AGENTS.md, secrets proxy, triggers, multi-agent workflows; SEC-filing researcher → quant agent → report demo. *(YouTube Y_p3y6zP5QE, creator-chapter cues, manual open. Presenter Andy — host override 2026-10-30.)*

**Context-only (sources slide, not decked):** Texas AG v. OpenAI/Altman (filed Oct 28).

## Editorial caveats carried on air

- Convovo: one studio's methodology — API, forced choice; not consumer apps; not a universal model property.
- ARC: 99.9% is a provider-adapter-harness score, never a naked model score.
- Anthropic red team: vendor-reported, unreleased internal model, authorized research with coordinated disclosure.
- Meta: ~$60B ATM is planned, not raised.
- Leaderboards: AA-measured, dated captures.
- Managed agents: vendor demo — Google showing Google; chapter cues spot-checked on open.
- Genie session length: vendor-briefed. Particle-1: vendor-reported.

## Production notes

- All grid card thumbnails link their primary receipts; every claim resolves to the sources slide.
- SFO is manual-open only; no autoplay; fallback still = poster; presenter Andy this episode (host override 2026-10-30); no in-video sponsor read in chapters — verify on open.
- Sponsor rotation this episode: Heritage (slot 1) → Herald Labs (slot 2).
- Program Topics sheet: Episode 36 tab synced 2026-10-29 (C39–C58, direct API + readback verified).
- Build trail: `episodes/36/showprep/revs/` rev2; validator authority EP35 rev4; website draft publish on pass.
