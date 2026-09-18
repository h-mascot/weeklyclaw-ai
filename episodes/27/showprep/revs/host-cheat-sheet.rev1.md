# WeeklyClaw Episode 27 — Host Cheat Sheet (rev1)

**Show date:** Friday 2026-08-28 · 4:00 PM ET · Hosts: Henry + Andy
**Run:** ~38–44 min scripted · hard stop 45:00

## Runtime at a glance

```
Cold open          [████]                1:30
Herald sponsor     [██]                  1:00
Story 1 OpenAI     [████████████]        6:30   ← Henry lead
Story 2 Qwen       [████████████]        6:00   ← Henry lead
Story 3 Headlong   [██████████]          5:30   ← Henry lead
Story 4 Portable   [██████████]          5:00   ← Henry lead
Story 5 Robot data [██████████]          5:30   ← Henry lead
Signal Outside     [██████████████]      7:00   ← permanent anchor
Hot take           [██████]              3:00
Heritage sponsor   [█]                   0:45
Close + recap      [████]                2:30
                  ────────────
Total scripted                            ~44:15  (hard stop 45:00)
```

## One-line segment summaries (host key card)

| # | Segment           | Owner   | Core claim                                | Live artifact                                 | Time |
|---| |---|---|---|---|---|
| 1 | OpenAI stack      | Henry   | Owned silicon + Premium seat = vertical margin | openai.com/index/jalapeno-first-results         | 6:30 |
| 2 | Qwen Flash-Next   | Henry   | 6B-active MoE previewing Qwen4 architecture  | qwen.ai/blog?id=qwen3.8-flash-next             | 6:00 |
| 3 | Headlong          | Henry   | Agent decides its own next wake-up           | laude.org/updates/headlong                     | 5:30 |
| 4 | Perplexity PC     | Henry   | Local-first agent stack; cloud gated        | perplexity.ai/hub/products/portable-computer   | 5:00 |
| 5 | Figure Index      | Henry   | Physical-world data is the moat             | figure.ai/news/introducing-index               | 5:30 |
|   | Signal Outside    | Andy    | Codex wrapper → spatial surface             | x.com/davidfromkansas/status/2092245009810493916 | 7:00 |
|   | Hot take          | Henry   | Deployment layer is the open moat          | (no live artifact)                              | 3:00 |

## Cut order if running long

1. **Compress Signal From Outside 7:00 → 6:00.** Drop the second clip cue.
2. **Compress Story 5 (Figure) 5:30 → 4:30.** Cut the Beijing event recap paragraph.
3. **Compress Story 4 (Portable Computer) 5:00 → 4:30.** Drop the DX Spark hardware-floor detail.
4. **Compress Hot take 3:00 → 2:00.** Drop "what would change his mind" line.
5. **NEVER cut:** Stories 1, 2, 3. Herald sponsor read. Henry segment lead on any news segment.

## Henry-only key phrases (do not script verbatim)

- **Story 1:** "Vertical integration is back. The question is whether it's a moat or a funeral."
- **Story 2:** "Qwen4 isn't out yet. The preview architecture is the play."
- **Story 3:** "The first coworker who decides what matters. Also the first to dismantle its own chair while sitting on it."
- **Story 4:** "If the agent lives on your desk, the cloud becomes the guest, not the landlord."
- **Story 5:** "The robots sprinting and falling are the demo. The 16 million videos are the company."
- **Hot take:** "The last open moat is the deployment layer."

## Live artifacts — clickable URLs only

```
S1 OpenAI Jalapeño:
  https://openai.com/index/jalapeno-first-results/
  https://openai.com/index/premium-seats-chatgpt-business/
  https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Groq-3-LPX-Now-in-Full-Production-With-World-Class-Speed-for-Agentic-AI/default.aspx

S2 Qwen3.8-Flash-Next:
  https://qwen.ai/blog?id=qwen3.8-flash-next
  https://huggingface.co/Qwen/Qwen3.8-Flash-Next
  https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next

S3 Headlong:
  https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents
  https://github.com/laude-institute/headlong

S4 Perplexity Portable Computer:
  https://www.perplexity.ai/hub/products/portable-computer
  https://perplexity.ai/hub/blog/a-local-first-agent-for-private-and-cost-effective-knowledge-work
  https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs

S5 Figure Index + Robot Games:
  https://www.figure.ai/news/introducing-index
  https://arstechnica.com/ai/2026/08/world-humanoid-robot-games-show-runners-breaking-records-bursting-into-flames/
  https://www.euronews.com/video/2026/08/24/beijing-robot-games-humanoids-take-on-sprints-football-and-tai-chi

Signal From Outside:
  https://x.com/davidfromkansas/status/2092245009810493916 (16.9s demo · 2,114 likes)

Discord (close):
  https://weeklyclaw.ai/discord (rotating invite route — never hardcode discord.gg)
```

## Handoff cues (Henry → Andy)

- After Herald sponsor: "Henry, the OpenAI stack is one answer. Qwen just opened a different one."
- After S1 → S2: Andy asks "Is this what long-context agents are made of?"
- After S2 → S3: Andy asks "Who decides what they do with it?"
- After S3 → S4: Andy asks "Henry, that's an agent on a server. Perplexity just put one on the desk."
- After S4 → S5: Andy asks "The robots are chasing a different prize."
- After S5 → Signal: Andy asks "Now the part where we fight about it."
- After Signal: Henry line, then Andy opens Heritage.

## Recap rule (Andy, 2026-08-21)

The close block above recaps the episode exactly ONCE. Do not re-recap items already covered in the close during host banter after Heritage or in the Discord follow-up post. The recap is the recap.

## Known gaps before showtime

- **Deck:** BUILD did not produce a 12-slide deck.html with verified local media assets (5 image artifacts + 2 video clips). The Ep 26 deck template is in `qa/authority-deck-ep26.html` for next-tick regeneration.
- **Website draft:** `/home/henrymascot/clawd/projects/weeklyclaw-ai` is not present on this host. Standing-authorized draft publication deferred. Next-tick recovery: copy Ep 26 sponsor/QR assets (already on disk) + agenda + cheat sheet to that path, `npm run build`, commit, push.
- **Henry X pulse:** fresh as of 2026-08-27 08:00 UTC (6h ago). Henry engaged with Qwen3.8-Flash-Next (RT Aug 26), Headlong (RT Aug 25), OpenAI Premium/Jalapeño (Aug 25 quotes), robot race clips (Aug 25-26), Dylan Patel compute value-capture (Aug 26). No override.

## APPROVE / SWAP / DROP / PIN / ORDER commands

Reply in this Telegram topic with exactly one of:

- `APPROVE` — lock the lineup as-is, promote at FREEZE.
- `SWAP <slot> <candidate>` — replace Story N with bench candidate.
- `DROP <slot>` — remove Story N from the lineup.
- `PIN <candidate>` — pin Story N against any auto-replacement.
- `ORDER <n1,n2,n3,n4,n5>` — re-sequence the five news segments.