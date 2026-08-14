# WeeklyClaw #25 — Andy's segment deep-dive

Andy owns: **Segment 1 (DeepSeek ships the model, harness, and API dialect)**, **Segment 4 (Writer cuts agent cost in the harness)**, **Segment 5 (OpenAI Computer History + Drive ambient context)**.
Andy co-leads: Signal From Outside, Hot Take, One to Watch.

## Segment 1 — DeepSeek ships the model, the harness, and the API dialect (lead)

**Frame:** The model lab owns the whole stack. Weights, harness, and API dialect — one lab, same news cycle, MIT.

**Anchor numbers:**
- **1.65T params**, **66 safetensor shards** on Hugging Face
- **1,048,576 context / 384,000 completion** tokens
- **OpenRouter Artificial Analysis index 53** (independent)
- **805 GitHub stars** on DeepSeek Harness at retrieval

**On-air script (5 minutes target):**

> DeepSeek-V4-Pro-0813 reached GA on August 13. One lab, MIT license, three things at once: a model checkpoint, a harness, and an API dialect. Start with the model: one-point-six-five-T params, sixty-six safetensor shards live on Hugging Face under deepseek-ai/DeepSeek-V4-Pro-0813, and OpenRouter independently exposes it at one-million-forty-eight-thousand-five-seventy-six context and three-eighty-four-K completion. Artificial Analysis index fifty-three on the independent scale. Then the dialect: the API keeps the deepseek-v4-pro name and accepts OpenAI Responses and Anthropic Messages formats, so OpenClaw, Claude Code, and Codex clients connect without rewrites — same tool calls, same reasoning effort levels, one-click Codex route. And then the harness: the MIT-licensed DeepSeek Harness, everything-is-a-plugin TypeScript, with skills, MCP, persistent shells, subagents, jobs, scheduling, workflows, compaction, terminal, web, and Ralph tooling. The npm family @deepseek-ai/dsh ships an executable CLI. Eight-oh-five GitHub stars at retrieval. Developer preview — compatibility may break.
>
> Benchmarks DeepSeek reported: Terminal Bench two-point-one eighty-seven point nine, NL2Repo sixty-one point five, DeepSWE sixty-two point seven, Toolathlon-Verified seventy-four point one. None independently reproduced. OpenRouter Artificial Analysis index fifty-three is independent but not a harness-matched run. The headline is not the benchmark number — it is that DeepSeek shipped weights, harness, and Open Responses + Anthropic Messages dialect on the same day, all under MIT. That is the model lab owning the operating layer.

Delivery notes:
- Lead with "three things at once" — that is the segment thesis.
- Don't editorialise about Chinese open-source strategy; stay on the integration story.
- Cite the npm package by name once and read the GitHub URL out loud.

**Handoff to Henry:** *"Henry, when the model lab ships the harness and the API dialect together, who decides what the operating layer looks like?"*

---

## Segment 4 — Writer cuts agent cost in the harness (lead)

**Frame:** The harness rewrites the bill. Same model, forty percent cheaper because the harness stops rebuying context and failure.

**Anchor numbers (memorize):**
- **33–61%** cost reduction across six tested models
- **82%** quality per dollar improvement
- **44%** faster completion at parity
- **52% / 48% / 10%** with Palmyra X6 (cost / speed / quality)
- **~$0.12** per finished task
- **7,876 / 7,886** cache read rate (byte-stable prefix)
- **n=22 prompts, 6 models, r=0.99**
- **8 hours** write-ahead recovery objective

**On-air script (5 minutes target):**

> The harness rewrites the bill. Writer's updated harness made six tested models thirty-three to sixty-one percent cheaper, raised quality per dollar eighty-two percent, and averaged forty-four percent faster completion at parity. Paired with Palmyra X6 — GLM-5.2 base, one-million context, two dollars in, eight dollars out per million tokens — they report fifty-two percent lower cost, forty-eight percent faster work, ten percent higher quality at ~twelve cents per finished task.
>
> Six ladder rows. Stable prompt prefix — cache read seven-thousand-eight-seventy-six out of seven-thousand-eight-eighty-six. Typed compaction at eighty percent budget — auto-summary and offload. Context offload to durable store — resumable from disk. Zero-token suspension — no idle billing. Bounded retries and failure routing — avoid repeated error loops. Write-ahead recovery — up to eight hours on a single task.
>
> Writer-run, n-twenty-two prompts, six models. The harness-leverage r-zero-point-nine-nine result spans only six models; the cost and quality figures are directional, not a general benchmark. Independent workload test was not performed in this build. Quote: if the same model becomes forty percent cheaper because the harness stops rebuying context and failure, should AI budgets be owned by model procurement — or systems engineering? Sources: writer.com — Aug roundup, writer.com/engineering — harness research, dev.writer.com — Palmyra X6, VentureBeat corroboration.

Delivery notes:
- Read the six rows in order; don't skip.
- Quote lands on the budget-ownership framing.
- Don't extrapolate Writer's results across all harnesses.

**Handoff to Henry:** *"Henry, if the same model becomes forty percent cheaper in the harness, what does that do to AI capex plans?"*

---

## Segment 5 — OpenAI Computer History + Drive ambient context (lead)

**Frame:** Your agent is now watching your workday.

**On-air script (5 minutes target):**

> Your agent is now watching your workday. On August thirteen, OpenAI shipped Computer History for macOS — interaction events from selected apps and sites, not screenshots, screen recordings, microphone, or system audio. Off by default. Inclusion lists for apps and sites. Pause. Timeline inspection. Deletion. Business and Enterprise admin enablement with individual opt-in. Rollout: Pro, Business, and Enterprise outside the EEA, the UK, and Switzerland first.
>
> Right card — Google Drive in Library. Connected Drive files and folders are browsable in Library. Keep Docs, Sheets, and Slides beside a conversation. Work across a selected folder; update the source file where authorized. Shared Drives and some collaboration features not yet included. Builds on Chronicle with reduced token use and more privacy controls.
>
> Off by default, admin and user opt-in, no screenshot or audio capture. OpenAI's framing is interaction events, not screen recording. This run did not inspect local event files, server-side retention behavior, deletion completeness, cross-workspace leakage, or real recall quality. Quote: when your agent remembers the workday and can edit the source files, is the product finally useful because it knows enough — or finally dangerous for the same reason? Sources: help.openai.com — release notes, OpenAI official X — status twenty-zero-eight-seven-nine-nine-six-four-nine-six-zero-eight-eight-two-nine-seven-seven-four-six.

Delivery notes:
- Lead with "interaction events, not screenshots, not screen recordings, not microphone, not system audio" — be precise about what is and isn't captured.
- Read the source X status number once if it lands cleanly; otherwise just say "OpenAI's official X post."

**Handoff to Henry:** *"Henry, when an agent remembers the workday and can edit the source files, who owns the audit trail?"*

---

## Signal From Outside (anchor)

> Signal From Outside. Tim Hwang, Mihai Criveti, Olivia Buzek, and Akash Srivastava on IBM's Mixture of Experts podcast, episode titled "Agent control planes and OpenAI model solves Erdős." ~46 minutes, published May twenty-nine. The first seventeen minutes are the operating-layer conversation we have been trying to have since Episode twenty-two — observability, policy, kill switches, agentic control planes. The second half covers OpenAI's unit-distance result on the Erdős-seventy-eight puzzle and METR's rogue-agent findings. Timestamps on screen: zero-zero introduction, one-oh-three agentic control plane, seventeen-forty-eight Astra unit-distance result, thirty-three-thirty-four METR rogue-agent study. No autoplay — clickable source link only. Poster is the verified YouTube thumbnail.

Delivery notes:
- This is a permanent anchor — never cut, even if running long.
- Land the title in full once: "Agent control planes and OpenAI model solves Erdős."
- Read the four timestamps so listeners can scrub to them on YouTube.

---

## Hot Take (co-lead)

Read the three findings in order, then the quote, then the alert-card questions. See Henry's section for the lead-in copy.

---

## Sponsor reads (Andy)

**Herald Labs (30s):** This episode is brought to you by Herald Labs — an applied AI product lab where humans and agents build together. Their product Entity is mission control for agent teams, and they run hacker houses worldwide. Find them at labs.theherald.co.

---

## Risk register (what to avoid on air)

- Don't characterise DeepSeek's MIT license as "fully open" — it is MIT for the harness and a separate MIT-like license for the model; the dialect is API-level.
- Don't claim 805 stars is "verified adoption" — it is a snapshot at retrieval.
- Don't generalise Writer's r=0.99 across models beyond the six tested.
- Don't claim OpenAI's Computer History is "always on" — it is opt-in, off by default, with explicit admin/user gating.
- Don't speculate about Anthropic's multiagent swarm being "rogue" — the paper documents dynamics, not intent.