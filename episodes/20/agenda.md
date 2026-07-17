# 🦞 Weekly Claw — Episode 20 Rundown

**Date:** Friday, July 10, 2026 · 4:00 PM ET
**A live builder show about AI, agents, devtools, startups, and the weird edge of software.**
**Host:** Andy (@AndyML) · **Featuring:** @HiM · possible guest builder
**Target runtime:** ~43 min (~48 with a guest) · built to be clipped

---

## Cold Open — The Frame (2 min)

Welcome to Weekly Claw. The last seven days might be the most important week in AI all year, so I'm not going to waste the top of the show — here's what actually mattered. Two frontier models launched in a single day. The cost of running an agent just fell off a cliff. And the first fully autonomous AI ransomware showed up in the wild. That's the episode. Let's get into it.

---

## What Happened This Week (14 min)

**The headline: this wasn't a launch, it was a pile-up — maybe the biggest 72 hours in AI model history.** Run the tape. July 8th, OpenAI drops **GPT-Live** — a full-duplex voice model that listens and talks at the same time, backchannels "mhmm" at you like a person, and hands off to a frontier model when it needs to actually think. Same day, **Cognition ships SWE-1.7**, their best coding model yet, running in Devin at a thousand tokens a second on Cerebras — frontier-class agentic coding at a fraction of the cost. **Perplexity's** in the mix too, rolling out local-cloud routing on Perplexity Computer that keeps your sensitive stuff on-device and ships the heavy lifting to the cloud automatically. And then July 9th is the real earthquake: **GPT-5.6** in three tiers — Sol, Terra, Luna — with ChatGPT and Codex folded into one super app, and hours later **xAI's Grok 4.5** at two dollars a million tokens, which Cursor's CEO instantly made his daily driver at roughly a quarter of Opus 4.8's token count.

The takeaway — and it's the theme of the whole episode: the cost of intelligence just collapsed, and it's coming from everywhere at once. Voice, coding, routing, frontier — four different fronts in three days. What was expensive six months ago is commodity infrastructure now, and that changes what's worth building. (And if OpenClaw's your harness — it already wired up the full GPT-5.6 family, day one.)

**Second: Claude Cowork went mobile and web.** Anthropic made Cowork sessions run remotely — start a task on your laptop, close the lid, check it from your phone, and scheduled tasks run when nothing's even online. That's the real shift: from "AI tool you sit in front of" to "AI teammate working in the background." They doubled usage limits through August 5th to get you hooked. Watch this pattern — async agents are becoming the default, not the novelty.

**Third: Cursor had an absurd week.** They launched Automations — coding agents that trigger themselves off repo changes, Slack messages, or a timer. Code review, security audits, incident response, all running with nobody pressing a button. They shipped an iOS app. And Bloomberg says revenue doubled to over two billion dollars in three months, sixty-billion valuation. Devtools just became always-on infrastructure, and the money says it's real.

**Fourth, and this one's strategic: Chinese models now run up to 46% of US enterprise API tokens.** CNBC's investigation — up from about four and a half percent a year ago. DeepSeek V4 Flash is fourteen cents per million tokens against GPT-5.5's five dollars. Coinbase runs twelve hundred agents on Chinese models and halved its bill. The House Committee opened a probe. Your model choice is now a strategic and political decision, not just a technical one.

**And the one that should scare you a little: JADEPUFFER.** Sysdig documented the first fully autonomous AI ransomware attack. An LLM agent exploited a vulnerability, moved laterally, escalated privileges, encrypted over thirteen hundred configs, and demanded ransom — all on its own, fixing its own failed steps in real time. This is not a demo. If you build agents, that's your threat model now. The age of agentic attackers is officially here.

---

## Hot Takes / Debate (7 min)

Alright, takes. Two big ones this week.

**Take one: the frontier-model moat is basically gone.** When Grok 4.5 lands at two dollars and DeepSeek's at fourteen cents and Cursor's CEO swaps daily drivers in an afternoon — the model isn't the moat anymore. The moat is moving up the stack: the harness, the routing, the workflows, the distribution. My prediction: within a year, "which model" becomes a config setting most builders barely think about, and the companies that win are the ones that own the layer *above* the model, not the model itself. If you're betting your product on having access to the single best model, I think you're betting on the wrong thing.

**Take two, the spicy one: are you actually going to run DeepSeek in production?** Because the cost math says yes and the politics say maybe not. I think most builders quietly will, congressional probe or not — the price gap is too big to ignore for background agent work where the data isn't sensitive. But I'd bet we see the first "company got burned running Chinese models" headline within a couple months, and then everyone pretends they were always careful about it. Where do you land — pragmatist or hard no? Drop it in chat, I want the disagreement.

---

## Tool Fight — Grok 4.5 vs the Frontier for Agent Work (6 min)

So let's actually put yesterday's launches in the ring, because this is the question everyone's going to be arguing about all weekend: what's your agent daily driver now — Grok 4.5, GPT-5.6, or Claude Opus 4.8?

Here's my read. On raw cost-per-outcome, Grok 4.5 is the story — two bucks a million and, if the token-efficiency claims hold, roughly a quarter of the tokens Opus burns for the same job. For long-running agent loops where you're paying per step, that compounds fast; the Cursor endorsement isn't nothing. GPT-5.6 Luna is the sleeper — a dollar in, and now it lives inside a merged Codex-plus-ChatGPT app, so the distribution is brutal. And Opus 4.8 is still, for my money, the best when the task needs judgment and long-horizon coherence — but it's now the premium option you reach for deliberately, not the default you leave running.

The real move, though — and this is what the smart teams are already doing — isn't picking one. It's routing: cheap fast model for the ninety percent of agent steps that are grunt work, frontier model for the ten percent that actually need taste. Which, funny enough, is exactly what the guy in our next segment spends twenty minutes arguing. So let's go there.

---

## Signal From Outside — Jensen Huang on Open Agent Systems (7 min)

The one video worth your time this week dropped two days ago: Jensen Huang, NVIDIA's CEO, sitting down with Harrison Chase from LangChain. Title's "Why companies need open agent systems." Sounds like an all-hands snoozer. It is not — it's the sharpest framing I've heard of exactly the thing we were just talking about.

Chase asks what changed in the last six months to make AI actually *useful*. And Jensen's answer isn't about the models — it's about what he calls the **harness**. The scaffolding around the model: tools, memory, domain context, the learning loop. AI got useful, he says, when people stopped treating it as raw capability and started wrapping it in a harness they own and control. That's agent frameworks. That's the whole game.

Then he gets to model selection, and it's the same take I just gave in the tool fight — start with the frontier model to find the ceiling of what's possible in your domain, then build **specialized sub-agents** for your critical workflows, and *that's* where cheap open-weight models shine because you can fine-tune them and run them yourself. His line is that when intelligence is cheap, you use *more* of it — more agents in parallel, bigger search, faster iteration. Which is precisely the world yesterday's launches just dropped us into.

The part that stuck with me: he says most companies treat agents like a software-procurement decision when it's actually a strategy decision — that a company is "a collection of proprietary, super-important workflows," and whoever encodes those into agent systems on infrastructure they control wins. He and Chase announce a Deep Agents plus OpenShell reference architecture to go do exactly that. And he throws in, without hedging, that more AI means more jobs — the AI-native roles just aren't invented yet.

Why I'm showing you this: it's a CEO of a three-trillion-dollar company describing the open-harness, route-between-models, own-your-infrastructure playbook as *the* winning architecture. That's not fringe anymore. It's the consensus forming in real time. Video's linked — the Nemotron and LangChain middle section gets usefully technical if you want to go deeper.

---

## Close — One To Watch + Where To Follow (2 min)

One thing to watch next week: the next shoe. Two frontier models launched in a day, so keep an eye on how Anthropic responds and whether that House probe on Chinese models turns into anything real — that's the story with legs.

If you want to travel for something: the AGI Summit is at the Palace of Fine Arts in San Francisco July 18–19, and there's a sharp little "Loop Engineering" night at Frontier Labs in SF on the 14th if last week's Steinberger talk landed for you.

And the housekeeping that actually matters now: this show lives on **X** first — that's where the clips and the live takes go, so follow the show and follow me, **@AndyML**. Full episodes and highlights land on **YouTube**, and everything's archived with sources at **weeklyclaw.ai**.

Next episode is Friday, July 17th, 4 PM ET. New format, same time. We follow the excitement — see you then.

---

*Weekly Claw #20 · July 10, 2026 · 🦞*
*"Follow the excitement."*
