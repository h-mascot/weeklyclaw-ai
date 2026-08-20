# WeeklyClaw #26 — Host cheat sheet (one page)

**Show date:** Friday, August 21, 2026 · 4:00 PM ET
**Hosts:** [Henry](tg://user?id=855505513) and [Andy](tg://user?id=7615999206)
**Planned runtime:** ~40:00 · Hard stop: 45:00
**Sponsor order:** Herald Labs (post-cold-open) · Heritage Telecom (pre-One to Watch)

## Run of show

| Beat | Owner | Time |
|------|-------|------|
| Cold open | Both | 2:00 |
| Herald Labs sponsor | Andy | 0:30 |
| The map | Henry | 1:00 |
| S1 Qwen open | Henry lead, Andy caveat | ~5:00 |
| S2 Faraday | Andy lead, Henry recap | ~5:30 |
| S3 Speed tier | Henry lead, Andy DFlash 2 | ~5:30 |
| Signal From Outside (Garry Tan) | Andy | ~7:00 |
| S4 Stripe-OpenRouter | Andy lead, Henry recap | ~5:00 |
| S5 AgentCore payments | Henry lead, Andy BNB | ~5:00 |
| Hot Take (provenance) | Henry anchor, Andy steelman | ~3:00 |
| Heritage Telecom sponsor | Henry | 0:30 |
| One to Watch | Andy | 1:00 |
| Outro | Andy | 0:30 |

## Cut order if running long

1. Drop the 10T+ tokens stat in S4.
2. Collapse the AWS/BNB split in S5 to one card.
3. Drop the DFlash 2 software side in S3.
4. Never cut Signal From Outside, the cold open, S1, or S2.

## Henry's talking-point anchors (full text in henry-section.rev1.md)

- **Cold open (optional landing line):** "Here's the frame: speed, routing, payments, supervision, and licensing thresholds are no longer features — they are the moat."
- **S1 question:** "If the weights are downloadable but require five terabytes, serious inference infrastructure, and a separate license once your AI assistant reaches $50 million, did frontier capability become open — or merely inspectable?"
- **S2 question:** "If a 27B supervisor can direct a model two orders of magnitude larger, should we spend the next dollar on a smarter worker — or on training the judgment that decides what the worker should do?"
- **S3 question:** "If an agent gets 30 times more tokens in the same minute, should we make the answer arrive faster — or spend the entire gain on more checking before anyone sees it?"
- **S5 question:** "When an agent can pay for the next API call without asking, which layer should own the veto — the model, the workflow, the wallet, or a policy the agent cannot rewrite?"
- **Hot Take anchor:** "Detection is not authorship. The model becomes the new plausible deniability. The defensible posture is signed receipts — content-keyed, hash-chained — not a watermark guess."
- **Hot Take close:** "What decision is the detector safe enough to make?"

## Andy's complete fallback talk tracks (full text in andy-section.rev1.md)

- **Cold open (verbatim):** "It is Friday, August 21. The models barely moved this week. The layer beneath them did."
- **Herald Labs (verbatim):** "This episode is brought to you by Herald Labs — an applied AI product lab where humans and agents build together. Their product Entity is mission control for agent teams, and they run hacker houses worldwide. Find them at labs.theherald.co. Back to the operating layer."
- **S2 lead:** "Inherent's Faraday is post-trained on Qwen3.6-27B and builds a scientific agent that can call GPT-5.5 Codex as a coding worker, rather than encoding scientific workflow in a large hand-built multiagent harness. The training corpus is Replica: 310 figure-replication tasks across 100 machine learning and AI-for-science papers, 242 training, 68 test. Each agent receives a paper with one results figure redacted, a 60-minute deadline, internet access, and 1/7 of an H200 GPU."
- **Signal From Outside (verbatim):** "This week's outside signal is Garry Tan at YC Startup School 2026, 'Own Your Intelligence.' Published August 6. Forty-two minutes. The argument: we are entering the era of personal AGI. Personal AGI runs on your own infrastructure, compounds personal knowledge, and dramatically increases individual ability to build."
- **S4 lead:** "Both companies posted on August 19. Stripe's newsroom announcement says it has agreed to acquire OpenRouter to help businesses optimize token routing and usage. Stripe describes a gateway that routes across 400+ models from more than 80 providers. OpenRouter's same-day post says it is 'joining Stripe,' commits to 'same mission, same name, same product, same roadmap,' and writes down the neutrality promise: 'routing decisions will remain driven by one thing: what's best for you, the user.'"
- **Hot Take steelman:** "The opposition runs like this. 'Schools need any signal. Newsrooms need any signal. Even a probabilistic watermark is better than nothing. Waiting for a perfect detector leaves the public unprotected.' That is half right and half wrong. Half right because any signal beats the vacuum the public operates in today. Half wrong because a probabilistic signal used as if it were deterministic attribution creates false confidence. The resolution is not to suppress the detector. It is to scope it: watermarks belong in triage pipelines that route questionable artifacts to a reviewer, not in courtrooms that treat 'Claude likely processed this' as authorship. The production layer fix is signed receipts — identity, authorization, timestamp — that do not depend on which sampler touched the text."
- **Heritage Telecom (verbatim):** "Heritage Telecom keeps the lights on while we keep the operating layer honest. Independent infrastructure for independent voices. Independent. Reliable. Quietly essential. Back to One to Watch."
- **One to Watch:** "One to watch for next Friday: Stripe–OpenRouter closing conditions. If the deal closes before August 28, gateway and wallet ship as one company. If the close slips, the test shifts to whether the OpenRouter catalog and pricing stay stable through the regulatory tail."
- **Outro:** "That's WeeklyClaw twenty-six. Discord on screen for live chat, scan to join Friends of the Crustacean. Follow at weeklyclaw.ai. Next show Friday August twenty-eight, four PM ET. See you then."

## Authoritative commands

- `APPROVE` — flip `approval_state` to APPROVED.
- `SWAP <slot> <candidate>` — replace a segment with a bench candidate.
- `DROP <slot>` — remove a segment.
- `PIN <candidate>` — never displace a story.
- `ORDER <slots>` — reorder segments.

## Files (this episode, all under `episodes/26/showprep/`)

- `state.json` — selection, scores, sponsor order, signal video, asset provenance.
- `revs/agenda.rev1.md` — full agenda.
- `revs/deck.rev1.html` — full deck.
- `revs/speaker-notes.rev1.md` — slide-by-slide notes.
- `revs/talking-points.rev1.md` — one-page numbers and caveat ladder.
- `revs/henry-section.rev1.md` — Henry's on-air material.
- `revs/andy-section.rev1.md` — Andy's fallback talk tracks.
- `revs/host-cheat-sheet.rev1.md` — this file.
- `sources/s1-qwen-open.md`, `sources/s2-faraday-judgment.md`, `sources/s3-speed-tier.md`, `sources/s4-stripe-openrouter.md`, `sources/s5-agent-payments.md`, `sources/hot-take-provenance.md`, `sources/signal-outside.md`, `sources/henry-x-pulse.md`, `sources/host-shared-resources.md`.