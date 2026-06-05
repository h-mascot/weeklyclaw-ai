# 🦞 The Weekly Claw — Episode 13 Agenda

**Date:** Friday, May 8, 2026 · 4:00 PM Eastern
**Platform:** OpenClaw Discord · Voice Channel
**Hosts:** Andy (@AndyML), Henry (@HiM)
**Total runtime target:** ~48 minutes (1 hour cap)

---

## 1. Welcome & Housekeeping (3 min)

Welcome back to The Weekly Claw, everyone. Episode 13. Friday, May 8th, 4 PM Eastern, same slot as always. If this is your first time joining, this is the spot where each Friday we pick apart what shipped in the OpenClaw world that week, what the broader industry was saying about us, and one outside conversation worth bringing back to the room. Pull up a chair. Drop questions in text chat as we go and I'll catch them between segments.

Quick housekeeping the same way we always do it. This session may be recorded — joining voice is your opt-in, and the disclosure link lives in the server rules. And the standing PSA before anything else: **OpenClaw has no token, no coin, no blockchain component.** If you see a wallet, an airdrop, a presale, or anything claiming association with this project, it's a scam. Report it and move on.

---

## 2. Community Guidelines (3 min)

Fast pass through the rules for anyone new — and we have new faces every week now, so I'd rather over-explain than skip.

On the server: no spam, no NSFW content, no harassment or hate speech, and no crypto, betting, or trading talk. Ever. We get serious builders and high-profile guests in here, and the bar is what keeps them coming back. Self-promotion lives in `#self-promotion` only — don't DM members about your project. Help questions go to `#help` and `#users-helping-users`, not `#general`. Model questions go to `#models`. If something looks off, `/report` flags it and a mod will see it.

If you're stuck on an install issue, the fastest unblock is almost always switching to the git install: `curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method git`. Saves a lot of back-and-forth.

In voice: jump in, but listen for a beat first so you don't land in the middle of someone's thought. Share the mic — if you've been talking a lot, make space. Keep the language kid-safe-ish. These norms run on honor. They work because you make them work. If something goes sideways in here, `/report-vc` pings Audrey and she'll handle it.

---

## 3. OpenClaw in the News (12 min)

Big news week, and the headline story is something I genuinely did not expect to be saying out loud on this show. Three stories I want to spend real time on, then a couple of cautionary items I want to acknowledge so we're not pretending they don't exist.

**Story one. Meta is building an OpenClaw clone, and they're calling it "Hatch."** This dropped on Wednesday — The Information had the story first, and Gizmodo, Engadget, and Dataconomy all picked it up. According to the reporting, Meta has an internal AI agent in development codenamed Hatch, and the explicit framing inside Meta is that OpenClaw is *too complex* for non-technical users, so they want to build a consumer-friendly alternative. They're targeting end of June for internal testing. They've already been testing it on simulated versions of DoorDash, Reddit, and Outlook. And there's a sister project — an agentic shopping tool for Instagram, positioned to compete with TikTok Shop.

Let that sit for a second. The biggest social media company on Earth — a company with an AI org the size of a small country — is building a product *because OpenClaw proved the category exists*. They're not competing with us at the developer layer. They're admitting the open-source lobster defined what a personal AI agent looks like, and now they want a friendlier wrapper for everyone else. When Meta copies you, you've won. This is the most validating piece of news this project has had since Tank OS shipped two weeks ago. Drop the Gizmodo link in chat — `gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854`. The headline references the Summer Yue inbox incident from February, which is one reason we'll come back to security in a minute.

**Story two. We are now the most-starred software project in the history of GitHub, by a wide margin, and we got there in two months.** OpenClaw crossed 350,000 GitHub stars in April and the number is still climbing. Seventy thousand forks. Sixteen hundred contributors. We surpassed React's decade-long record in sixty days. But the part of this that matters more than the trophy is what's underneath it. As of last month: 3.2 million monthly active users. 38 million monthly visits to the website. ClawHub now lists over 44,000 community-built skills. And — this is the number I keep coming back to — 180 startups built on top of OpenClaw are generating more than $320,000 a month in combined revenue. That's an ecosystem. That's not vapor.

Star History wrote it up — you can find their post at `star-history.com/blog/openclaw-surpasses-react-most-starred-software`. Panto has the full statistics breakdown for 2026. Drop those in chat for anyone who wants the receipts.

**Story three. The team shipped two stable releases this week alone, and they did it the right way.** v2026.5.2 dropped Sunday with xAI Grok 4.3 support, sturdier plugin installs, leaner gateway and agent hot paths, and fixes across Discord, Slack, Telegram, and WhatsApp. v2026.5.4 came out Tuesday with cleaner plugin installs, faster gateway startup, better doctor and repair hints, and Windows plus Discord reliability fixes. Henry will dig into all of it in the changelog segment. But I want to flag the *meta* story around these releases here, because it's the part that tells you something about the project's character.

If you've been reading the timeline, you know the back end of April had some stability problems. v2026.4.24 through 4.29 caused gateway crashes for some users, broke a few chat integrations, surfaced regressions. The team's response was a blog post — title is literally "OpenClaw Had a Rough Week" — where they openly acknowledged what went wrong, named the failure modes, and laid out the structural changes they're making. Smaller core. Optional modules moving out to ClawHub. An LTS release planned for later this month. The blog post is at `openclaw.ai/blog/openclaw-rough-week`. Drop it in chat.

That kind of transparency is rare in commercial software and it's getting rarer in open source. Most projects this size would have shipped quietly and let the patches speak for themselves. Owning the rough week, in writing, where everyone can read it — that's how trust gets built.

**Now, the cautionary side. Security.** I'm going to keep saying this every week until it stops being true, because if you look at our coverage in the major outlets, security is the recurring theme outside our community. Couple of things to keep on your radar.

The "ClawHavoc" malware campaign is still being written about. Latest reporting puts the count at roughly 800 malicious skills found on ClawHub — that's about 20 percent of the registry — delivering malware ranging from infostealers to remote-access tools. Censys, Bitsight, and Hunt.io have all separately identified tens of thousands of internet-exposed OpenClaw instances running without authentication. And the Summer Yue incident — Meta's AI Safety Director who had her inbox deleted by an out-of-control OpenClaw agent that ignored her stop commands — that story resurfaced this week specifically because of the Hatch announcement. Reporters are using it as the framing device for why Meta thinks OpenClaw is too dangerous for normies.

The honest assessment: these are real, verifiable concerns that Fortune, The Register, Kaspersky, Cisco, Tom's Hardware, and Fast Company have all covered. The team has been responsive — patches keep shipping, the structural changes in the rough-week post are partly a response — but security is the project's Achilles heel and it deserves attention. If you're running OpenClaw: keep it updated, vet your skills, turn on auth, and review the docs.

Two pieces of bonus context for the back pocket. NVIDIA NemoClaw — the enterprise security layer Jensen announced at GTC in March — is still in early preview. Worth tracking. And the OpenClaw Foundation is being established with OpenAI backing for long-term stewardship of the project. Peter joined OpenAI back in February. The foundation is the structural piece that gives the project a stable home outside any one company's roadmap.

That's the news. Henry, take it from here.

---

## 4. Changelog Roundup + DevX Report — Henry @HiM (14 min)

*Hand the floor to Henry. He'll drive his own deck on superada.ai for this segment — the host's slides won't advance again until the seminar. The notes below are a follow-along beat sheet for the host so we know what's on screen and when to take the floor back.*

This week's release window is **2026.5.4 through 2026.5.7** — four releases in a tight three-day stretch, May 5 through May 7. The shape of the week is one big feature release up front and three days of follow-up bugfixes and stability work. Henry will walk through it, but here's the rough arc he'll cover so the host knows where he's going:

The headline ship is **2026.5.4 on May 5** — Google Meet voice agent over the realtime Gemini bridge. Twilio dial-in joins now speak through Gemini Realtime with paced audio streaming, backpressure-aware buffering, and barge-in queue clearing. No more TwiML fallback during realtime speech. If you've been running the Meet bridge, this is the release that makes it feel snappy instead of stuttery. Same release also brought a Windows gateway fix (binding to `127.0.0.1` instead of `::1` to fix libuv dual-stack issues), better plugin migration hints, secret-ref preservation through `secrets apply`, and Codex audio transcription advertised through the manifest.

**2026.5.5 on May 6** was the broad stability release. Feishu topic-session hydration, LINE webhook validation now fails explicitly rather than silently dropping, Telegram and Codex progress drafts stay visible, Slack startup failures now log full error context instead of "unknown error," Grok native Responses no longer rejects OpenAI-style reasoning effort controls, Discord heartbeat ACK timeouts now measured from actual send time (which kills a class of false reconnect loops), Matrix approval delivery retries with backoff, iOS Tailscale and `.local` auth got cleaner, and the Control UI got responsive during slow history payloads.

**2026.5.6 was the emergency hotfix later the same day** — a regression in 5.5's `doctor --fix` command was incorrectly rewriting valid `openai-codex/*` OAuth routes to `openai/*`, which could have broken OAuth-only GPT-5.5 setups or silently moved users to API-key billing. The team caught it, reverted the change, and the recovery command is `openclaw models set openai-codex/gpt-5.5 && openclaw config validate` if anyone in here needs it. Same release also fixed a couple of fetch and proxy header issues with third-party symbol metadata.

**2026.5.7 on May 7** was a pure bugfix and security-hardening release. Plugin publishing got more resilient — retries transient ClawHub install failures, keeps preview-passing plugins publishable when a single preview cell flakes. The cron CLI got a `status` field in JSON output so external tooling doesn't have to re-derive it, and `openclaw doctor --fix` can now repair persisted cron jobs with bad model overrides. On the security side: admin scope is now required for global Active Memory toggles, owner enforcement is honored for native command handlers, auto-reply inline skill tool dispatch passes through before-tool-call authorization hooks, and Tavily SecretRef API keys are now correctly resolved before being passed to search and extract tools. Plus a Discord routing fix for provider-prefixed targets, consistent npm lifecycle shell paths, and a `/btw` placeholder fix.

The summary takeaway Henry will close on: this was a *firefighting* week, but the firefighting was disciplined. One headline feature, then three consecutive days of explicit, well-described patches. The Codex OAuth regression got caught and reverted in hours. The cron and plugin publishing improvements are the kind of unglamorous reliability work that compounds.

After the changelog walkthrough, Henry takes a few minutes for his standing DevX wrap — wins and pain points from the past week, community PR highlights, the voice moderator and facilitator application update, and a status note on Jim's International AI Series. Then he hands the floor back for the seminar.

---

## 5. Video Review: Jensen Huang at the Milken Institute Global Conference (8 min)

Alright, so this week I want to walk you through a video that dropped just four days ago — and it's one I think deserves more attention from people in the OpenClaw world than it's been getting in the usual developer circles.

Jensen Huang, CEO of NVIDIA, sat down with Becky Quick at the Milken Institute Global Conference in Beverly Hills. If you don't know the Milken conference, it's basically where the CEOs of everything go every spring to talk about the macro picture — finance, policy, geopolitics. So Jensen showing up there is already a little interesting. He's not at GTC, he's not at a developer summit. He's in a room full of hedge fund managers and private equity titans and institutional investors. And what he talks about is agentic AI.

Now, here's the setup: the conference itself had this anxious energy. Becky Quick even calls it out early in the conversation. The broader CEO crowd at Milken this year was unsettled — there's a lot going on economically — and the question that kept coming up on stage after stage was basically: *are things okay?* So when she gets Jensen in that chair, she leads with the thing everyone in the room is quietly worried about. And it's not chip shortages. It's jobs.

She asks him, point blank, whether this AI revolution is going to cause a kind of economic dislocation that's qualitatively different from past technological shifts. Whether we're heading somewhere that creates more inequality, not less.

And Huang doesn't dodge it. He goes right at it. His first line is basically: *"The first thing that AI is doing right now is creating an enormous number of jobs."* And you can feel the room wanting to believe him. But he doesn't stop at the bumper sticker. He actually builds the argument.

Here's the distinction he draws, and this is the part I think is genuinely worth sitting with. He says people who are afraid of AI taking their jobs are making a conceptual error — they're confusing their *job* with the *tasks* their job requires. His framing is that automating a specific task within a role doesn't eliminate the role, because the purpose of the job and the tasks of the job are related but not the same thing. So a developer who uses an agent to write boilerplate doesn't stop being a developer — they become a developer with more leverage. The job didn't disappear; it changed what it means to be good at it.

Becky pushes back a little here. She's not dismissive, but she's representing the room's skepticism. She raises the question of whether this time really is different — whether the pace is faster than people can adapt. And Huang acknowledges the concern is real, but then he says something that I thought was the most interesting beat in the whole conversation: he says his *greatest concern* isn't AI causing harm. It's the opposite. He says, "My greatest concern is that we scare people — all the people that we're telling these science-fiction stories to — to the point where AI is so unpopular in the United States, or people are so afraid of it, that they don't actually engage it." That was the line that landed in the room. He's not worried about the robot apocalypse. He's worried about a fear-driven disengagement from a technology he believes is genuinely generative.

Then he pivots to what I'd call the audacious part of the talk. This is where it stopped feeling like a defensive PR move and started feeling like he was actually laying out a thesis.

He says: the IT industry today is a couple of trillion dollars. Big number. But the *service* industry? That's a hundred times larger. And then he drops this line that I keep coming back to: "For the first time, service is software. Software is service." What he means is that agentic AI is the mechanism by which the software industry finally gets access to markets it was never really able to touch — manufacturing, logistics, healthcare operations, physical infrastructure. Not through traditional software deployments that require enormous implementation cycles and human integration, but through agents that can operate in those environments directly.

He gets specific about manufacturing. He talks about a future factory where "the entire manufacturing line is operated by robots, managed by more robots, and the entire factory is a robot." Not metaphorically — he means this literally as the physical architecture of industrial production over the next decade. He frames this as a $50 trillion opportunity that has been essentially untouched by technology until now.

And then there's a detail he mentions, almost in passing, that hit differently for me when I thought about it in OpenClaw terms. He says the compute demand for agentic AI has gone up *one thousand percent* compared to generative AI from just two years ago. Not 10x in marketing language — he's saying the actual compute requirements at inference time have exploded because agents don't just produce text: they read, reason, use tools, check results, generate more tokens, spawn sub-tasks, loop back. The token budget for a single agentic session dwarfs what a standard LLM call used to look like.

He doesn't say this as a warning. He says it almost like someone rubbing their hands together. Because NVIDIA sells the compute. But the implication for everyone building in the agentic space is pretty clear: what we're building is genuinely different in kind, not just in degree.

Toward the end of the conversation, Becky brings it back to the question of responsibility — whether tech leaders are doing enough to think about second-order effects. And Huang doesn't give a corporate-speak answer. He talks about the shared obligation of the sector to maintain guardrails, and he says it in a way that felt sincere rather than rehearsed. He's clearly thought about it. He's not afraid of the question.

Now, why does any of this matter to us specifically — to people building and contributing to OpenClaw?

I'll just say it directly: Jensen Huang spent thirty minutes at one of the most watched business conferences of the year making the case that the type of thing we build is the biggest opportunity in the history of software. The $50 trillion market he's pointing at doesn't get unlocked by another chatbot. It gets unlocked by persistent, autonomous agents that can act in the world, manage tasks, coordinate with tools, and operate without constant hand-holding. That's the architectural problem OpenClaw is trying to solve at the open-source layer.

When he says "service is software" — that's not just a snappy quote. That's a description of the transition we're in the middle of. And when he says the compute for agents has gone up a thousand percent, he's inadvertently describing why the engineering challenges in OpenClaw — context management, efficient agentic loops, tool use, session persistence — are genuinely hard problems worth solving.

This wasn't a developer conference talk. Jensen wasn't speaking to us. But the thing he was describing? That's us. And I think it's worth watching.

The video is called *"Leading in the Age of AI: A Conversation with NVIDIA CEO Jensen Huang"* — it's on the Milken Institute YouTube channel, posted May 4th. Go watch it. It runs about thirty minutes and it moves.

---

## 6. Meetup Report (5 min)

If anyone's attended an OpenClaw meetup recently or has one on the calendar, this is your slot. Open mic. Tell us city, headcount, what you talked about, anything good that came out of it, anything that fell flat. The Tel Aviv crew was in this room last week — would love to hear how Pulumi TLV went. Same for anyone who hit Milan, Miami Beach, Istanbul, Seattle, or New York this past week.

**Coming up in the next two weeks** — these are pulled from ClawExplorer at `clawexplorer.ai`. Heads up: the live calendar feed wasn't reachable from my fetch this morning, so this list is built off the most current carry-forward we had on file. If you see something new or postponed, please drop it in chat and tag @AndyML so we can update the rundown:

- **Saturday, May 9 — Chiang Mai 🇹🇭** — 🦞 OpenClaw Meetup Chiang Mai — 2:00 PM local — `luma.com/2w471wrh`
- **Saturday, May 9 — Mexico City 🇲🇽** — ClawCon CDMX — 5:00 PM local — `luma.com/clawconcdmx`
- **Wednesday, May 13 — Sunnyvale, CA 🇺🇸** — Getting Started with OpenClaw Workshop — 2:00 PM PT — Eventbrite ticket page is live
- **Wednesday, May 13 — St. Charles, MO 🇺🇸** — Build Smarter Workflows with OpenClaw — 5:00 PM CT — Eventbrite ticket page is live

Three continents in two weeks, mix of formats — a Saturday community hangout in northern Thailand, a full-day ClawCon in CDMX, and two midweek workshops in the US. If you're going to any of these, please report back. Tag me in Discord, @AndyML, with the city and your handle and I'll get you on the rundown for next week's episode.

If you're running a meetup and it isn't on ClawExplorer yet, get it listed — the calendar at `clawexplorer.ai/calendar.ics` is what feeds this segment, so anything that isn't on there is invisible to the rest of the community.

---

## 7. Closing (3 min)

That's Episode 13. Thanks for being here.

Quick link roundup before I let you go. GitHub at `github.com/openclaw/openclaw`. Website is `openclaw.org`. On X we're `@openclaw`, and `@steipete` for Peter's feed. The "OpenClaw Had a Rough Week" blog post is at `openclaw.ai/blog/openclaw-rough-week` if you want to read the team's own write-up of the late-April stability work. The Jensen Huang Milken video is on the Milken Institute YouTube channel, May 4th — go watch it. And the Meta Hatch reporting from Gizmodo is the one to bookmark for the news segment.

We're back next Friday, May 15th, at 4 PM Eastern. Drop topic suggestions in Discord. If you want to report from a meetup or present a short segment, tag @AndyML.

And one more time, the standing PSA: **OpenClaw has no token, no coin, no blockchain component. Anything claiming otherwise is a scam.**

See you next week. 🦞

---

**Links:**
- 📺 [Leading in the Age of AI — Jensen Huang at Milken Institute Global Conference 2026 (YouTube)](https://www.youtube.com/results?search_query=Leading+in+the+Age+of+AI+Jensen+Huang+Milken)
- 📰 [Gizmodo — Meta Reportedly Building OpenClaw-Like Agent Called 'Hatch'](https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854)
- 📰 [Engadget — Meta's AI agent plans include an OpenClaw competitor](https://www.engadget.com/2167475/metas-ai-agent-plans-reportedly-include-an-openclaw-competitor-that-can-shop-on-instagram/)
- 📰 [Dataconomy — Meta Builds OpenClaw-inspired Assistant For Instagram](https://dataconomy.com/2026/05/08/meta-builds-openclaw-inspired-assistant-for-instagram/)
- 📊 [Star History — OpenClaw Surpasses React](https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software/)
- 📊 [Panto — OpenClaw AI Platform Statistics 2026](https://www.getpanto.ai/blog/openclaw-ai-platform-statistics)
- 🦞 [OpenClaw Blog — OpenClaw Had a Rough Week](https://openclaw.ai/blog/openclaw-rough-week)
- 📦 [v2026.5.4 announcement on X](https://x.com/openclaw/status/2050735037230801042)
- 📦 [v2026.5.7 announcement on X](https://x.com/openclaw/status/2051582130417721696)
- 🛡️ [Fortune — OpenClaw is the bad boy of AI agents](https://fortune.com/2026/02/12/openclaw-ai-agents-security-risks-beware/)
- 🛡️ [Tom's Hardware — OpenClaw wipes inbox of Meta AI Alignment director](https://www.tomshardware.com/tech-industry/artificial-intelligence/openclaw-wipes-inbox-of-meta-ai-alignment-director-executive-finds-out-the-hard-way-how-spectacularly-efficient-ai-tool-is-at-maintaining-her-inbox)
- 🦞 [OpenClaw on GitHub](https://github.com/openclaw/openclaw)
- 📅 [ClawExplorer Calendar](https://www.clawexplorer.ai/calendar.ics)

---

**Runtime check (target ≤ 60 min):**

| Section | Minutes |
|---------|---------|
| 1. Welcome & Housekeeping | 3 |
| 2. Community Guidelines | 3 |
| 3. OpenClaw in the News | 12 |
| 4. Changelog + DevX (Henry) | 14 |
| 5. Video Review (Jensen / Milken) | 8 |
| 6. Meetup Report | 5 |
| 7. Closing | 3 |
| **Total** | **48** |

Buffer of ~12 minutes for Q&A, voice introductions, or stretch on any segment that opens up.

---

*The Weekly Claw #13 · May 8, 2026 · 🦞*
*"The Claw is the Law."*

---

**Notes for the host (not for air):**
- **Calendar fetch failed:** `clawexplorer.ai/calendar.ics` is not on the network allowlist for this run, so the meetup list in §6 is carried forward from Episode 12's research and trimmed to events still inside the May 8 → May 22 window. Worth confirming live before air via the ClawExplorer site or asking in `#meetups`.
- **Henry segment beat sheet (§4)** is built off the changelog brief covering 2026.5.4 → 2026.5.7. Henry's own slides on superada.ai will be the source of truth on screen — these notes are just for follow-along.
- **News segment lead (§3)** is the Meta "Hatch" story; this is the strongest single beat of the week and is intentionally first in the run order.
- **Security beat (§3 close)** is included deliberately because the Meta reporting reactivated the Summer Yue inbox-deletion story — host should expect chat to surface it and is prepped to address it directly.
