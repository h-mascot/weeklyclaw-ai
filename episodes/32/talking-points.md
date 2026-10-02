# WeeklyClaw Episode 32 consolidated talking points

**Revision:** rev2 · local review draft  
**Runtime:** 35:00 + 3:00 buffer = 38:00 ceiling; 45:00 hard stop  
**Core question:** Which part of the agent stack would you change this week?

This is the shared, on-air-focused view of the canonical agenda. News remains Henry-led; Andy’s prose is a safety net. Evidence/caveat and visual details remain in the agenda and slide notes.

## Cold open · 0:45 · s-cold-open

**Andy:** OpenAI has a new Sol model, Dots, and a Decisions API. Google has Gemini 4 Argon, with restricted initial access. We are going to work through what each changes for someone building with agents, from the model bill to the runtime boundary. Henry, the question for the show is simple: which part of the agent stack would you change this week?

**Henry talking points:**
- Model choice: measure the cost of a completed task, including retries and review
- Deployment choice: decide what the agent can reach and what a human must approve

**Henry line (optional):** Start with the change you can test this week.

**Handoff cue:** Andy takes the Heritage read; Henry starts Sol on Grid A at 02:15.

## Heritage Telecom · 1:30 · s-sponsor-heritage

**Andy:** “Weekly Claw is brought to you by Heritage Telecom: UCaaS and VoIP for businesses that just need their calls to work. Independent, boring reliability, zero telemetry. Independently reliable. Quietly essential. Heritagetel.com.”

**Handoff cue:** Henry starts Sol at 02:15.

## Story 1 · OpenAI launches GPT-6.1 Sol · 3:00 (Grid 1, slide `s-seg-grid-a` card 1)

*02:15–05:15 · Henry leads.*

**Henry talking points:**
- Start with one workload you already measure; hold the harness, success criteria, and review burden fixed
- One-fifth refers to Astra’s standard input/output token prices; retries and extra reasoning can change task economics
- Label the Sol card as a WeeklyClaw transcription of primary-source benchmark deltas; do not splice it into Google’s table

**Henry line (optional):** What would you move first if the quality survives your own regression set?

**Andy fallback talk track:** The practical reason to try Sol is the new cost point. OpenAI lists it at two dollars per million input tokens and ten dollars per million output tokens, with cached input at ten cents. Its launch evaluation also reports an improvement over the previous Sol on DeepSWE. Those are OpenAI’s results, and the production setup can differ. For a builder, I would pick a workflow with an answer we can actually check, run the same tasks through both configurations, and count failed attempts and human cleanup as part of the bill. A cheaper model that takes three tries may still be the wrong route. Henry, which workload would you put into that comparison first, and what result would make you keep the old route? That gives us a concrete model decision. Next, Dots changes who keeps the work moving.

**Handoff cue:** Henry moves to Grid A card 2: Dots and the responsibilities that persist between prompts.

**Evidence guardrail:** Research/API evaluation; competitor scores come from public reports. Sol launch availability is Work, Codex and API, not yet Chat. No precise keynote cue is verified. Community-only exact scores are not used in the primary-source delta scorecard.

**Visual cue (not read on air):** Show the clearly labeled WeeklyClaw transcription of primary-source benchmark deltas at card 1: DeepSWE high +6.4 pp over the prior Sol best; AutomationBench medium +2.2 pp over Opus 5.5; OSWorld offline max −2.1 pp versus Astra max. This is a source-cited rendered scorecard, not a vendor chart or the community repost. Keep the full OpenAI launch-source link. Enlarge it if labels are illegible; do not merge the deltas into Google’s comparison.

**Primary source:** https://openai.com/index/introducing-gpt-6-1-sol/

## Story 2 · OpenAI introduces Dots · 2:00 (Grid 1, slide `s-seg-grid-a` card 2)

*05:15–07:15 · Henry leads.*

**Henry talking points:**
- Choose one recurring job with a clear stopping condition and owner
- Separate read-only investigation, drafting, and external action when setting permissions
- Ask how the operator notices a wrong assumption or stops work; launch capability is not an observed reliability result

**Henry line (optional):** What is the first job you would trust it to keep working on after you close the laptop?

**Andy fallback talk track:** Dots is the persistent-assistant part of this launch. OpenAI says it has its own cloud computer and can use connected apps to keep working on a goal. Availability depends on your plan and market, and enterprise use also depends on the workspace administrator. The useful first assignment should have a boundary you can explain: investigate a class of bugs, for example, and bring back changes for review. That is our proposed test case, not a claim that this release has passed it. I would want to know when it asks, what it records, and how I stop it. Henry, which ongoing job has enough value to try this, and where would you require a human decision? Now let’s look at a much narrower piece of the same stack: choosing the next action from a fixed set.

**Handoff cue:** Henry moves to Grid A card 3: Decisions API.

**Evidence guardrail:** Vendor-described product behavior, not a WeeklyClaw reliability test. Pro/Business Premium access is market-limited; Enterprise/Edu/Healthcare beta requires admin enablement. Keep highly consequential actions outside any on-air demonstration.

**Visual cue (not read on air):** Official OpenAI Dots video: manually play 00:50–01:10 (20 seconds), pausing at 01:05 on Jojo’s Computer browsing a wedding-cake site. Exact-time frames were decoded; browser/audio playback remains a pre-air check. Fallback: the verified 01:05 frame, source-linked. The clip is inside this card’s 2:00, not extra time. No autoplay or live connected-account action.

**Primary source:** https://openai.com/index/introducing-dots/

## Story 3 · OpenAI previews the Decisions API · 2:00 (Grid 1, slide `s-seg-grid-a` card 3)

*07:15–09:15 · Henry leads.*

**Henry talking points:**
- Find a decision that genuinely has a small, known set of valid outcomes
- Test wrong-route behavior and ambiguous inputs, not just clean examples
- A constrained answer format does not prove the chosen action is correct or authorized; demo labels are vendor-reported

**Henry line (optional):** Where does a small decision API fit better than another open-ended agent turn?

**Andy fallback talk track:** The Decisions API narrows the job. You provide the context, define a question, and give it a finite set of answers. OpenAI says Luna powers that decision, with classification and routing among the intended uses. It was announced as a limited preview. The demo compares Decisions with Responses and labels the screen as shown at fifteen times real time. Its latency figures describe that vendor demonstration, with setup details we do not have. For a workflow that only needs to choose between a few next steps, this could be a useful component to test. The work is defining those choices well and deciding what happens when none is safe. Henry, where would you try this first, and what would your fallback be for an ambiguous request? Keep that test in mind as we turn to Google’s much broader capability claims.

**Handoff cue:** Henry moves to Grid A card 4: Gemini 4 Argon and its benchmark/access limits.

**Evidence guardrail:** Limited preview in the September 29 announcement. The vendor demonstration’s conditions, region, and concurrency are undisclosed in the verified material. Its 150 ms/request versus 1.6 s/request is not an independent benchmark or universal latency guarantee. Keep “Shown 15x realtime” visible. No independent accuracy or cost comparison is established.

**Visual cue (not read on air):** Official OpenAI Developers demo: manually play 00:05–00:25 (20 seconds), pausing at 00:10. Preserve the “Shown 15x realtime” label. At 00:10 it displays 10,000/10,000 Decisions versus 2,000/10,000 Responses, 150 ms/request versus 1.6 s/request, and the vendor claim of about 10× faster decisions. Exact-time frames were decoded; browser/audio playback remains a pre-air check. Fallback: verified 00:10 frame linked to the original X post. The 20 seconds is inside this card’s 2:00. No autoplay.

**Primary source:** https://openai.com/index/devday-2026-recap/

## Story 4 · Google introduces Gemini 4 Argon · 3:00 (Grid 1, slide `s-seg-grid-a` card 4)

*09:15–12:15 · Henry leads.*

**Henry talking points:**
- The card shows the original vendor-table header and four agentic-coding rows; enlarge to the full table and pick one relevant row plus one where Argon trails
- The table mixes evaluation provenance and harnesses; do not turn it into a universal model ranking
- Access is part of the builder decision: qualify the rollout before recommending a migration

**Henry line (optional):** Which row resembles the work you actually need done?

**Andy fallback talk track:** Google’s own table is the right starting point for Argon. It reports 77.9 percent on DeepSWE, but it also shows places where Argon trails, including FrontierSWE. The evaluations do not all share one harness or one source, so a row is a clue about what to test rather than a guarantee for our workload. There is also a rollout constraint: the first access goes through Fairwind to trusted cyber defenders and testers. And the million-token number in this announcement refers to output. Henry, which result would make you spend time evaluating this, and can the team you are advising actually get access? That finishes our first grid. The second begins with evidence about what capable models can do in a very different setting.

**Handoff cue:** Advance to Grid B; Henry starts Anthropic’s GLM-5.3 evaluation at card 1.

**Evidence guardrail:** Google launch comparison, mixed-source evaluations. DeepSWE uses Google-run mini-swe-agent for Argon and external rival results; OSWorld is offline partial score and is not interchangeable with OpenAI’s comparison. Introductory API rates are $2/$10 input/output per million, later $4/$20, only if price is needed. No official Argon demo video was verified in this evidence pass.

**Visual cue (not read on air):** The card uses the exact original Google vendor-table header plus all four agentic-coding rows: DeepSWE, FrontierSWE, Vibe Code, and Terminal-bench. This is a faithful crop, not a reconstructed table. The complete original table is available in the enlarged view through the full-table link. Open that view for legibility or broader comparisons; preserve model headers and relevant methodology qualifications.

**Primary source:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

## Story 5 · Anthropic evaluates GLM-5.3 cyber capabilities · 2:00 (Grid 2, slide `s-seg-grid-b` card 1)

*12:15–14:15 · Henry leads.*

**Henry talking points:**
- Read the numerator and denominator; avoid “nearly equal” as a blanket capability ranking
- Separate capability tests from safeguard tests and real deployment outcomes
- CAISI’s 61.1% is partial-credit, best-of-three scoring; it cannot be compared directly to 50/410

**Henry line (optional):** What does this test tell the person deciding which tools the agent can reach?

**Andy fallback talk track:** Anthropic tested GLM-5.3 against its own models on cyber tasks. In the ExploitBench result we are showing, GLM completed 50 of 410 attempts and Mythos Preview completed 56. That is a specific end-to-end metric in an offline sandbox. Anthropic ran it, it competes with Z.ai, and Claude’s safeguards were disabled for the capability test. It tells us something important about capability under those conditions, but it does not give a failure rate for a deployed product. There is also a CAISI evaluation with a different scoring method; putting those percentages side by side would mislead people. Henry, what operational precaution follows from this result before we have any production incident rate? That takes us to the control plane where those precautions have to be implemented.

**Handoff cue:** Henry moves to Grid B card 2: OpenClaw Enterprise.

**Evidence guardrail:** The separate safeguard study measures attempted remote-target connection, not a successful exploit. Do not read the 64/92/100% connection figures as attack success. Prefill/abliteration unavailable through the Claude API is not a tested zero. No Henry-supplied GLM benchmark was recovered in the staged evidence; do not invent his result.

**Visual cue (not read on air):** Use a faithful labeled scorecard with 50/410 and 56/410 if the original Anthropic figure cannot be retrieved. Mark it as a rendered scorecard, not an original screenshot. The evaluator, metric, denominator, and sandbox condition must remain legible.

**Primary source:** https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities

## Story 6 · OpenClaw previews Enterprise · 2:00 (Grid 2, slide `s-seg-grid-b` card 2)

*14:15–16:15 · Henry leads.*

**Henry talking points:**
- Disclose the adjacent-tooling connection; assess the deployment problem on its merits
- Ask where permissions are enforced and whether model, harness, and sandbox can be changed independently
- Preview available for self-hosted internal pilots: do not call it private-only or production-ready

**Henry line (optional):** What would you need to see in a pilot before giving this access to a real business workflow?

**Andy fallback talk track:** Quick disclosure: WeeklyClaw runs adjacent tooling, so there is a connection to keep in mind as we discuss this. OpenClaw’s September 29 post says the Enterprise preview is available for self-hosted internal pilots. It is being developed in public ahead of a 1.0 release. The proposed value is a place to manage persistent agents with clearer tenancy, permissions, sandboxing, and auditability, while retaining choices about the components underneath. That is relevant to any team trying to move from a useful personal agent to a controlled internal service. It is still a pilot decision, and the product description is not evidence that every security boundary has been independently tested. Henry, what would your smallest useful pilot be, and which boundary would you test before expanding it? NVIDIA is addressing another part of that boundary at runtime.

**Handoff cue:** Henry moves to Grid B card 3: NVIDIA OpenShell and Sentry.

**Evidence guardrail:** The preview is accessible for self-hosted internal pilots; “internal pilots only” must not imply a closed private rollout. Vendor-described controls are not an independent security assessment. Keep the WeeklyClaw adjacent-tooling disclosure; producer must confirm any more specific relationship before elaborating.

**Visual cue (not read on air):** Use the official OCE product/architecture material linked to the September 29 post; a source-linked launch capture is the fallback. Do not call a conceptual illustration a live deployment or imply a security audit.

**Primary source:** https://openclaw.ai/blog/openclaw-enterprise

## Story 7 · NVIDIA adds agent runtime controls · 2:30 (Grid 2, slide `s-seg-grid-b` card 3)

*16:15–18:45 · Henry leads.*

**Henry talking points:**
- Point to the enforcement boundary in the architecture; a model instruction alone is not a tested boundary
- Ask which resources and outbound actions policy can restrict, and what happens when a request is denied
- Keep Sentry monitoring separate from proof that every harmful action is detected or prevented

**Henry line (optional):** Show me the blocked action and the evidence an operator gets afterward.

**Andy fallback talk track:** NVIDIA’s announcement puts runtime controls and monitoring around agent behavior. OpenShell is the runtime-control piece we can inspect through the developer material, while Sentry belongs to the broader monitoring story. The useful question is where a decision becomes enforceable: can a process reach a resource, can it use a credential, and what happens if it tries to go outside policy? The official demo is useful for seeing the intended workflow, but a vendor demo does not establish resistance to every bypass. The same applies to NVIDIA’s response-speed claims. Henry, which denied action would you reproduce in a test environment, and what would convince you the restriction held? We will come back to that as our one thing to watch. First, there are three different kinds of external scrutiny to distinguish.

**Handoff cue:** Henry moves to Grid B card 4: FTC confirmation, Senate hearing, and lawsuit allegations.

**Evidence guardrail:** Do not invent an excerpt, quote, tested stop time, or production safety outcome. A verified poster proves video identity, not a particular demo event. Keep vendor latency claims attributed if used; omit the number if it is not needed.

**Visual cue (not read on air):** Prefer the official OpenShell runtime diagram and NVIDIA Developer demo. Verified video identity: GYYP-eW58ug, NVIDIA Developer, 5:29. No playback excerpt is cleared until start/end cues are verified; use the verified poster or architecture still as fallback. Manual start only, no autoplay.

**Primary source:** https://nvidianews.nvidia.com/news/open-agent-safety-platform

## Story 8 · AI agents face regulatory and legal scrutiny · 2:30 (Grid 2, slide `s-seg-grid-b` card 4)

*18:45–21:15 · Henry leads.*

**Henry talking points:**
- Keep three statuses distinct: confirmed investigation, hearing/testimony, and allegations in a reported lawsuit
- Ask what evidence operators should preserve so a specific incident can be reconstructed
- Leave the mandatory-publication policy fight for Hot Take; this card establishes the record only

**Henry line (optional):** What do we know from the record, and what is still only being alleged?

**Andy fallback talk track:** These are three separate developments. AP says the FTC confirmed its probe on September 30. That tells us when the confirmation was reported, not when the investigation began. The Senate also held a hearing on rogue AI agents. In its published testimony material, METR describes limited-scope voluntary engagement; that should not be presented as a security audit of everything a company does. And reporting on the LASST lawsuit describes allegations about the Hugging Face breach. A filed allegation is not a court finding, and we do not have the primary complaint in this package. Henry, what records should a builder preserve today so that an incident can be investigated properly? That is the factual status of the scrutiny. Before our separate policy debate, Andy takes the outside video.

**Handoff cue:** Andy takes Signal From Outside on the next frame; no extra news recap.

**Evidence guardrail:** No claim that the FTC opened the probe on September 30, that any proceeding was a reaction to an Accord, or that the sequence proves causation. Do not repeat the old “within 48 hours” framing. Avoid personal-attendance claims unless independently verified. LASST complaint not retrieved; Axios is reporting on allegations, not a ruling.

**Visual cue (not read on air):** Show clearly labeled source material: AP confirmation, the Senate hearing page, and reported lawsuit status. Do not use an arrest/courtroom image to imply a judgment. Keep the three statuses visible in the presenter’s notes even when one receipt is on screen.

**Primary source:** https://apnews.com/article/89ac416717adbfb1d72f2d85e6ce83d1

## Signal From Outside / weekly video review · 6:00

*Slide `s-signal-outside` · 21:15–27:15 · Andy leads. [Theo — OpenAI should be scared of this one](https://www.youtube.com/watch?v=8WbW_n95wc4), September 29, 2026, 31:46; Sonnet 5.5 review.*

**Henry talking points:**
- Theo likes Sonnet 5.5 but argues against choosing it as the everyday primary model; his introduction compares it with GPT-6 Sol
- His pricing caveat is about cache-heavy coding workloads; do not turn his figures or usage into a universal cost result
- His concrete niche is Sonnet handling investigative subagent work called by Opus; the claimed benefit remains his practitioner hypothesis
- Name one task and a result that would disprove the routing choice; count retries, coordination, and human review

**Henry line (optional):** Which route wins after we count retries and review?

**Andy fallback talk track / 0:00–0:25 open:** Theo’s September 29 Sonnet 5.5 review gives us a useful contradiction: he likes the model but does not want it as his daily driver. His case turns on cached-token economics and using Sonnet as a subagent. Let’s look at the argument, then ask whether it fits our own work.

**Manual source cue 00:30–01:29 (59s) · segment clock 00:25–01:24: A good model without a clear primary-model case.** Transcript-derived; PENDING PLAYBACK / pre-air spot-check.

**Andy fallback if playback fails:** Theo says Sonnet 5.5 impressed him, even though the comparison he is discussing does not make an obvious case for it. He positions it against GPT-6 Sol. This is his assessment, not our benchmark conclusion.

**01:24–01:56 · React after cue 1 — Andy fallback:** That is a useful distinction: a model can be impressive without becoming the one you choose for every task. Theo is comparing it with GPT-6 Sol here; this is a Sonnet review, not a review of the GPT-6.1 Sol launch. Henry, what specific job would make you try a model even if you would not switch your primary route?

**Manual source cue 07:29–08:23 (54s) · segment clock 01:56–02:50: Cached-token costs qualify the headline price.** Transcript-derived; PENDING PLAYBACK / pre-air spot-check.

**Andy fallback if playback fails:** Theo questions the per-task saving claim and explains why cache reads and writes matter for his day-to-day agentic coding. His point is that input and output sticker prices alone can give the wrong impression of the bill.

**02:50–03:30 · React after cue 2 — Andy fallback:** The question is which tokens your workflow actually spends money on. Theo says cache activity is a big part of his coding work, so the headline input and output prices leave out something important. We should treat that as his workload evidence. Henry, would cache reads, retries, or human review be the bigger cost in the job you just picked?

**Manual source cue 29:51–31:06 (75s) · segment clock 03:30–04:45: Sonnet as an Opus-called investigative subagent.** Transcript-derived; PENDING PLAYBACK / pre-air spot-check.

**Andy fallback if playback fails:** Theo sees value in letting Opus call Sonnet for codebase investigation and checking a hunch. He expects that routing to make Opus feel faster and get work done somewhat more cheaply; he is proposing a useful role, not reporting an independent replication.

**04:45–06:00 · React after cue 3 and hand off — Andy fallback:** Here is his specific recommendation: keep Opus in charge and let it call Sonnet for bounded investigative work. The important qualifier is that he is predicting a benefit from routing it well. We have not independently reproduced that result. Henry, choose one investigation you would delegate that way, and tell us what would make you abandon it. For a useful comparison, I would hold the task and acceptance criteria fixed, count the coordinator and worker calls, and include failed attempts and the time a person spends checking the answer. That would tell us whether the cheaper worker really improved the route. Now we will leave model selection and take a different question: should agent vendors be required to publish incident reports?

**Handoff cue:** Andy reads the incident-reporting motion; Henry takes the proposed affirmative opening.

### Sources and production notes (not read on air)

PENDING PLAYBACK: the three source-video windows are measured from the recovered timestamped transcript, not yet audio/video spot-checked. Theo - t3.gg, September 29, 2026, duration 31:46. Verified subject: Sonnet 5.5; GPT-6 Sol is a comparison target, with “Soul” preserved as an auto-caption spelling in the source. The selected windows are 00:30–01:29 (59 seconds), 07:29–08:23 (54 seconds), and 29:51–31:06 (75 seconds): 3:08 playback plus 2:52 host setup/reaction = 6:00. Source timestamps and elapsed segment-clock labels are kept separate. Spot-check spoken boundaries, factual context, sound, and playback before air; do not label these host-approved or independently replicated. Keep the source title/creator visible. Manual start only; no autoplay. If playback fails, hold the verified poster and Andy reads the corresponding fallback paraphrase, then takes the same reaction question; do not invent a replacement clip. If using a local trim, stage it with source/cue provenance and confirm the permitted use scope. A public video or thumbnail is not blanket permission to rehost it. Cut additional discussion before dropping the permanent anchor.

- Source: https://www.youtube.com/watch?v=8WbW_n95wc4
- Fallback visual: verified Theo video poster linked to the source. Poster fallback is distinct from the transcript-derived excerpt; source playback still needs a spot-check.
- Cut: shorten the middle discussion answers first; retain the outside-source identification, workload question, and handoff. Keep the three transcript-derived source windows and spot-check them before air.

## Hot take / debate · 4:00

**Motion:** Agent vendors should be required to publish incident reports

*Slide `s-hot-take` · 27:15–31:15. Proposed debate assignments only; hosts may reverse or decline them before air.*

**Do not repeat news:** Debate a future disclosure duty, reporting thresholds, redaction, and burden. Do not recap the investigations, hearing, or lawsuit.

**Henry talking points:**
- PROPOSED AFFIRMATIVE opening: customers cannot price operational risk when important failures remain private
- Proposed rule: publish material incidents, impact, failure category, and remediation; defer exploit-enabling detail until safe
- Rebuttal: a scoped threshold and delayed technical details can reduce burden and protect customers without leaving everyone blind
- Mind-changer: credible evidence that confidential reporting produces equally useful, independently checked public lessons fast enough

**Henry line (optional):** If we cannot publish the exploit, can we still publish enough for another operator to avoid the same failure?

**Andy fallback countercase:** I’ll take the other side for this debate. A blanket publication mandate can create a new security and privacy problem. An incident report can expose a customer, reveal how to repeat an attack, or force a small team to spend its recovery time on legal review. I would start with prompt reporting to affected customers and an appropriate confidential reviewer, then publish lessons when the danger is contained. Henry, who decides what counts as material, and how do we keep that rule from rewarding large vendors that have bigger compliance teams?

**Andy fallback rebuttal and mind-changer:** Your delayed-detail proposal helps, but even a short report can identify a customer or reveal that a particular defense failed. The rule needs a responsible decision-maker for redaction, a way to challenge secrecy, and a deadline that reflects the actual risk. I would change my mind if a narrow reporting standard showed that it gives customers useful warning without exposing victims or distracting small teams from fixing the problem. What would change your mind about requiring public reports?

**Handoff cue:** Henry lands one final sentence; Andy takes the Herald Labs read. Do not revisit the news chronology.

### Production notes (not read on air)

These are proposed debate assignments, not statements of Henry’s or Andy’s existing beliefs. Confirm the sides before air. The news card established the status of investigations, testimony, and allegations. This debate is about a prospective publication duty: who must disclose what, to whom, and when. Do not re-tell those news events or use them to imply a legal finding. Clock: motion/setup 0:15; Henry affirmative 0:45; Andy countercase 0:55; Henry rebuttal 0:40; Andy rebuttal/mind-changer 0:50; Henry mind-changer/closer 0:35 = 4:00.

- Cut: shorten opening cases first; retain one rebuttal and one mind-changer per side. No new alleged incident is needed to make the motion arguable.

## Herald Labs · 1:30 · s-sponsor-herald

**Andy:** “Before we close — Weekly Claw is also brought to you by Herald Labs — an applied AI product lab where humans and agents build together. Entity is mission control for agent teams, and they run hacker houses worldwide. Build with humans. Ship with agents. That’s labs.theherald.co.”

**Handoff cue:** Henry takes the one watch; Andy closes after the advance to `s-sources`.

## One to watch and close · 2:15

**Henry talking points / s-watch / 1:15:**
- One watch: an independent, repeatable test of an agent runtime boundary
- Proposed test: attempt a harmless, policy-denied action in a disposable test environment and record allow/deny behavior, logs, and recovery
- Require enough configuration and procedure detail for another operator to reproduce it; a vendor demo alone does not meet that bar
- No result is established yet; do not imply WeeklyClaw or anyone else has already run the test

**Henry line (optional):** I want to see the same boundary hold when someone outside the vendor repeats the test.

**Handoff cue:** Advance to s-sources. Andy gives the single closing recap while the source links and WeeklyClaw Discord QR remain visible.

**Andy fallback / s-sources / 1:00 / only closing recap:** Our answer this week is to test one change at a time: choose a model for a measured workload, define the responsibility you are delegating, and verify the boundary before expanding access. We also put a separate policy question on the table: what should vendors have to disclose after an incident? The sources are on screen. Tell us in the WeeklyClaw Discord which part of your agent stack you would change this week, and what evidence you would want first. Use the QR code or weeklyclaw.ai/discord. We’ll be back Friday, October 9 at 4 PM Eastern. Thanks for watching.

**End cue:** Keep `s-sources` and the Discord QR visible. Do not add a second recap.

## Producer references (not read on air)

- Program Topics: https://docs.google.com/spreadsheets/d/16xAvCzRGA8XlWvihdSBcipw0wARzVZT9YysXzM0eFM8/edit
- Canonical approval, sponsor-claim checks, source caveats, and runtime proof: agenda.rev2.md
- SFO transcript-derived cues remain pending playback spot-check; NVIDIA excerpt cues are unverified. Dots/Decisions official media frames are verified, with browser/audio playback pending
- Local revision only; no publication or external-sheet synchronization is asserted

<!-- Episode 32 | revision rev2 | story-set-sha256 cee5cc422124f17a4b9d99326a790763ea58321c2dc545cf5aaea30d9ef6029d -->
