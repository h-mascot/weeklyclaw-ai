# WeeklyClaw Episode 32 speaker notes rev2

**Runtime:** 35:00 + 3:00 buffer = 38:00 ceiling; 45:00 hard stop. Title is included in cold open; Sources is included in close.  
**Revision:** rev2 · local review draft. Exactly one entry per stable slide ID, in deck order.  
**Core question:** Which part of the agent stack would you change this week?

## s-title

**Owner:** Producer advances; Andy begins on next frame

**Purpose:** Identify Episode 32 without using a separate introduction slot.

**Opening line or optional landing line:** No spoken title read; advance to the cold open as the camera goes live.

**Talking points:**
- Confirm Episode 32 and the October 2 show date
- Show the unchanged show branding
- Start the master clock at the first on-air word; advance immediately

**Evidence/caveat:** Title is branding, not evidence for a story claim. It adds no independent runtime.

**Question or handoff:** Andy opens with the core builder-decision question on s-cold-open.

**Visual cue:** Title frame only; no video playback.

**Source links:**
- Program Topics reference: https://docs.google.com/spreadsheets/d/16xAvCzRGA8XlWvihdSBcipw0wARzVZT9YysXzM0eFM8/edit

**Target time:** 0:00 additional; contained in the 00:00–00:45 cold-open window.

**Cut contingency:** Advance immediately; never delay news for a title explanation.

## s-cold-open

**Owner:** Andy opens; Henry gives concise hooks

**Purpose:** Get to the practical question before the first sponsor and news by 02:15.

**Opening line or optional landing line:** OpenAI has a new Sol model, Dots, and a Decisions API. Google has Gemini 4 Argon, with restricted initial access. We are going to work through what each changes for someone building with agents, from the model bill to the runtime boundary. Henry, the question for the show is simple: which part of the agent stack would you change this week?

**Talking points:**
- Model choice: measure the cost of a completed task, including retries and review
- Deployment choice: decide what the agent can reach and what a human must approve
- Optional Henry line: Start with the change you can test this week.

**Evidence/caveat:** Do not restore the unsupported Astra-deception claim or infer a causal timeline between product launches and investigations.

**Question or handoff:** Andy takes the Heritage read; Henry starts Sol on Grid A at 02:15.

**Visual cue:** Cold-open frame with the builder question. No playback; title time is included here.

**Source links:**
- [OpenAI DevDay announcements](https://openai.com/index/devday-2026-recap/)
- [Google Argon announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

**Target time:** 0:45, 00:00–00:45 including title.

**Cut contingency:** Use Andy’s question and one Henry point; start Heritage on time.

## s-sponsor-heritage

**Owner:** Andy

**Purpose:** Deliver the first approved sponsor read before the news.

**Opening line or optional landing line:** “Weekly Claw is brought to you by Heritage Telecom: UCaaS and VoIP for businesses that just need their calls to work. Independent, boring reliability, zero telemetry. Independently reliable. Quietly essential. Heritagetel.com.”

**Talking points:**
- Read the approved copy once, verbatim
- Keep the sponsor’s UCaaS/VoIP product wording
- Use only cleared sponsor assets for the balance of the 90-second window

**Evidence/caveat:** Approved rev1 wording is preserved. Unverified-claim checks are confined to producer review; do not improvise factual additions.

**Question or handoff:** Henry starts Sol on Grid A at 02:15, without another introduction.

**Visual cue:** Heritage sponsor frame and original sponsor mark.

**Source links:**
- Approved text source: agenda.rev1.md, Heritage Telecom read
- Sponsor destination named in approved read: https://heritagetel.com/

**Target time:** 1:30, 00:45–02:15.

**Cut contingency:** Keep the approved read and contractual window; producer may adjust only the cleared bumper/asset timing.

## s-seg-grid-a

**Owner:** Henry leads every card; Andy supports with full per-card fallback prose in agenda/Andy view

**Purpose:** Use four compact stories to identify a specific builder decision, not rank the whole market.

**Opening line or optional landing line:** What would you move first if the quality survives your own regression set?

**Talking points:**
- Card 1 / 3:00 / OpenAI launches GPT-6.1 Sol: OpenAI lists standard API prices of $2 input, $0.10 cached input, and $10 output per million tokens. Operator question: What would you move first if the quality survives your own regression set?
- Card 2 / 2:00 / OpenAI introduces Dots: OpenAI describes Dots as always-on agents with their own cloud computer and connected-app access. Operator question: What is the first job you would trust it to keep working on after you close the laptop?
- Card 3 / 2:00 / OpenAI previews the Decisions API: The Decisions API uses Luna to answer user-defined questions with finite predefined answers. Operator question: Where does a small decision API fit better than another open-ended agent turn?
- Card 4 / 3:00 / Google introduces Gemini 4 Argon: Google’s launch table reports 77.9% for Argon on DeepSWE v1.1; it also shows trade-offs, including 55.0% on FrontierSWE v2 against Astra’s 65.5%. Operator question: Which row resembles the work you actually need done?

**Evidence/caveat:** Sol price ratios are token prices; its exact community-only scores are not primary-verified. Dots has plan/region/admin limits. Decisions is a finite-choice Luna preview; the 150 ms/request versus 1.6 s/request labels come from a vendor demonstration shown at 15× real time, not a universal benchmark. Argon’s 1M is output; Google’s table mixes provenance and includes weaker results. Do not splice vendor charts into an unqualified ranking.

**Question or handoff:** Advance to Grid B; Henry starts Anthropic’s GLM-5.3 evaluation at card 1.

**Visual cue:** Two-by-two grid, exactly four cards: Sol / Dots / Decisions / Argon. Walk left to right, top to bottom. Sol card: labeled WeeklyClaw transcription of primary-source benchmark deltas, DeepSWE high +6.4 pp over prior Sol best, AutomationBench medium +2.2 pp over Opus 5.5, OSWorld offline max −2.1 pp versus Astra max; full OpenAI source linked. Argon card: exact original vendor-table header and all four agentic-coding rows, DeepSWE, FrontierSWE, Vibe Code, Terminal-bench; full original table available in the enlarged view. Enlarge these artifacts for legibility; do not describe Sol as a vendor chart or Argon as a reconstruction. The official DevDay keynote is 53:34 but has no verified cue. Dots cue 00:50–01:10, pause at 01:05 on Jojo’s Computer; Decisions cue 00:05–00:25, pause at 00:10, preserving “Shown 15x realtime”. Both clips take 20 seconds within their two-minute cards. Exact-time frames are verified; browser/audio playback remains pending. No autoplay. Exact per-card visual/provenance instructions are in the agenda.

**Source links:**
- [OpenAI Sol launch](https://openai.com/index/introducing-gpt-6-1-sol/)
- [Community chart provenance](https://community.openai.com/t/gpt-6-1-sol-in-the-api-a-meaningful-step-up-in-cost-performance/1402388)
- [DevDay keynote, official OpenAI channel, 53:34](https://www.youtube.com/watch?v=Fls_onRviPM)
- [OpenAI Dots launch](https://openai.com/index/introducing-dots/)
- [Official OpenAI Dots launch video, 2:28](https://x.com/OpenAI/status/2104984504133918973)
- [DevDay availability details](https://openai.com/index/devday-2026-recap/)
- [OpenAI DevDay recap, Decisions API section](https://openai.com/index/devday-2026-recap/)
- [Official OpenAI Developers Decisions demo](https://x.com/OpenAIDevs/status/2105003318917697873)
- [Google Argon launch and original table](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [DeepMind evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon/)

**Target time:** 10:00, 02:15–12:15. Card splits: 3:00, 2:00, 2:00, 3:00.

**Cut contingency:** Cut extra examples and secondary metrics, not attribution or legal status. Keep the four cards in order; use the agenda’s per-card cut instructions.

## s-seg-grid-b

**Owner:** Henry leads every card; Andy supports with full per-card fallback prose in agenda/Andy view

**Purpose:** Use four compact stories to identify a specific builder decision, not rank the whole market.

**Opening line or optional landing line:** What does this test tell the person deciding which tools the agent can reach?

**Talking points:**
- Card 1 / 2:00 / Anthropic evaluates GLM-5.3 cyber capabilities: Anthropic reports GLM-5.3 succeeding in 50 of 410 ExploitBench attempts versus 56 of 410 for Mythos Preview. Operator question: What does this test tell the person deciding which tools the agent can reach?
- Card 2 / 2:00 / OpenClaw previews Enterprise: The public September 29 announcement makes the preview available for self-hosted internal pilots. Operator question: What would you need to see in a pilot before giving this access to a real business workflow?
- Card 3 / 2:30 / NVIDIA adds agent runtime controls: NVIDIA presents OpenShell runtime controls and Sentry monitoring in its open agent safety platform. Operator question: Show me the blocked action and the evidence an operator gets afterward.
- Card 4 / 2:30 / AI agents face regulatory and legal scrutiny: AP reported agency confirmation of the FTC probe on September 30; this is not evidence of the probe’s opening date. Operator question: What do we know from the record, and what is still only being alleged?

**Evidence/caveat:** Anthropic is a competing evaluator; 50/410 and 56/410 are sandbox end-to-end successes, unlike CAISI partial-credit scoring. OCE preview is available for self-hosted internal pilots; disclose adjacent tooling. NVIDIA performance is vendor-reported; its 5:29 official demo has no verified excerpt. FTC confirmation is dated September 30, not a proven opening date. METR testimony describes limited-scope voluntary work. LASST allegations are not findings; complaint not retrieved.

**Question or handoff:** Andy takes Signal From Outside on the next frame; no extra news recap.

**Visual cue:** Two-by-two grid, exactly four cards: GLM evaluation / OpenClaw Enterprise / NVIDIA OpenShell + Sentry / accountability. Use labeled benchmark counts, official OCE material, NVIDIA runtime diagram or verified poster, and correctly identified legal receipts. No autoplay. Poster identity does not verify an excerpt. Preserve visible metric/status qualifiers.

**Source links:**
- [Anthropic GLM-5.3 study](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)
- [NIST CAISI evaluation for methodology contrast](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities)
- [OpenClaw Enterprise public announcement, September 29](https://openclaw.ai/blog/openclaw-enterprise)
- [NVIDIA open agent safety platform announcement](https://nvidianews.nvidia.com/news/open-agent-safety-platform)
- [NVIDIA OpenShell developer explanation](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/)
- [Official NVIDIA Developer OpenShell demo, 5:29](https://www.youtube.com/watch?v=GYYP-eW58ug)
- [AP report with FTC agency confirmation](https://apnews.com/article/89ac416717adbfb1d72f2d85e6ce83d1)
- [Senate September 30 hearing](https://www.hsgac.senate.gov/subcommittees/dmdcc/hearings/rogue-ai-securing-the-homeland-against-ai-agent-attacks/)
- [METR published testimony and scope](https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/)
- [Axios report on LASST allegations](https://www.axios.com/2026/09/29/openai-sued-hugging-face-breach)

**Target time:** 9:00, 12:15–21:15. Card splits: 2:00, 2:00, 2:30, 2:30.

**Cut contingency:** Cut extra examples and secondary metrics, not attribution or legal status. Keep the four cards in order; use the agenda’s per-card cut instructions.

## s-signal-outside

**Owner:** Andy leads; Henry answers operator questions

**Purpose:** Use the selected outside source to examine workload-specific routing and total subagent cost without inventing the creator’s argument.

**Opening line or optional landing line:** Theo’s September 29 Sonnet 5.5 review gives us a useful contradiction: he likes the model but does not want it as his daily driver. His case turns on cached-token economics and using Sonnet as a subagent. Let’s look at the argument, then ask whether it fits our own work.

**Talking points:**
- 0:00–0:25 Andy identifies Theo’s Sonnet 5.5 argument
- Source 00:30–01:29 / segment 00:25–01:24: favorable review without an obvious primary-model case; react 01:24–01:56
- Source 07:29–08:23 / segment 01:56–02:50: cached-token economics; react 02:50–03:30
- Source 29:51–31:06 / segment 03:30–04:45: Sonnet as an Opus-called investigative subagent
- 04:45–06:00 Henry proposes a falsifiable workload test; Andy preserves practitioner/hypothesis caveats and hands off

**Evidence/caveat:** PENDING PLAYBACK: the three source-video windows are measured from the recovered timestamped transcript, not yet audio/video spot-checked. Theo - t3.gg, September 29, 2026, duration 31:46. Verified subject: Sonnet 5.5; GPT-6 Sol is a comparison target, with “Soul” preserved as an auto-caption spelling in the source. The selected windows are 00:30–01:29 (59 seconds), 07:29–08:23 (54 seconds), and 29:51–31:06 (75 seconds): 3:08 playback plus 2:52 host setup/reaction = 6:00. Source timestamps and elapsed segment-clock labels are kept separate. Spot-check spoken boundaries, factual context, sound, and playback before air; do not label these host-approved or independently replicated. Keep the source title/creator visible. Manual start only; no autoplay. If playback fails, hold the verified poster and Andy reads the corresponding fallback paraphrase, then takes the same reaction question; do not invent a replacement clip. If using a local trim, stage it with source/cue provenance and confirm the permitted use scope. A public video or thumbnail is not blanket permission to rehost it. Cut additional discussion before dropping the permanent anchor.

**Question or handoff:** Andy reads the incident-reporting motion; Henry takes the proposed affirmative opening.

**Visual cue:** Verified Theo source poster linked to the 31:46 video. Three transcript-derived source windows are selected; playback/audio spot-check is pending. Manual start, no autoplay. Source timestamps and elapsed segment time are explicitly labeled. Use the prepared paraphrase if playback fails.

**Source links:**
- [Theo video, September 29, Sonnet 5.5 review](https://www.youtube.com/watch?v=8WbW_n95wc4)

**Target time:** 6:00, 21:15–27:15.

**Cut contingency:** Shorten middle host answers, preserving the permanent anchor. Spot-check the selected source cues before air; if playback fails, use the verified poster and matching fallback paraphrases. Do not fake a clip or independent test result.

## s-hot-take

**Owner:** Proposed assignment: Henry affirmative; Andy countercase

**Purpose:** Debate a concrete prospective publication duty, separate from the factual news card.

**Opening line or optional landing line:** Andy reads the motion: Agent vendors should be required to publish incident reports.

**Talking points:**
- Henry’s proposed case: customers need useful warnings and shared lessons; scope the rule to material incidents
- Andy’s proposed case: protect victims, avoid enabling exploits, and account for small-team recovery/compliance burden
- Henry rebuttal: thresholds and delayed technical detail can preserve useful disclosure
- Andy rebuttal: even a summary may identify a customer; require a workable redaction/review process
- Each names a mind-changer; Henry lands one sentence and hands off

**Evidence/caveat:** These are proposed debate assignments, not statements of Henry’s or Andy’s existing beliefs. Confirm the sides before air. The news card established the status of investigations, testimony, and allegations. This debate is about a prospective publication duty: who must disclose what, to whom, and when. Do not re-tell those news events or use them to imply a legal finding. Clock: motion/setup 0:15; Henry affirmative 0:45; Andy countercase 0:55; Henry rebuttal 0:40; Andy rebuttal/mind-changer 0:50; Henry mind-changer/closer 0:35 = 4:00.

**Question or handoff:** Henry lands one final sentence; Andy takes the Herald Labs read. Do not revisit the news chronology.

**Visual cue:** Show the motion prominently. No incident montage or re-run of the accountability sources; this is a policy debate, not new reporting.

**Source links:**
- The motion is an original discussion proposal, not a quote or a claimed legal requirement
- [Scope reference only, METR published testimony](https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/)

**Target time:** 4:00, 27:15–31:15.

**Cut contingency:** Shorten opening cases, retaining one rebuttal and mind-changer per side. Do not pad by recapping news.

## s-sponsor-herald

**Owner:** Andy

**Purpose:** Deliver the second approved sponsor read after the debate and before the close.

**Opening line or optional landing line:** “Before we close — Weekly Claw is also brought to you by Herald Labs — an applied AI product lab where humans and agents build together. Entity is mission control for agent teams, and they run hacker houses worldwide. Build with humans. Ship with agents. That’s labs.theherald.co.”

**Talking points:**
- Read the approved copy once, verbatim
- Use the supplied sponsor identity and product wording
- Hand to Henry’s single watch after the 90-second window

**Evidence/caveat:** Approved rev1 wording is preserved. Unverified-claim checks are confined to producer review; no new factual claims are added.

**Question or handoff:** Henry takes s-watch; Andy waits until s-sources to recap.

**Visual cue:** Herald sponsor frame and original sponsor mark.

**Source links:**
- Approved text source: agenda.rev1.md, Herald Labs read
- Sponsor destination named in approved read: https://labs.theherald.co/

**Target time:** 1:30, 31:15–32:45.

**Cut contingency:** Keep the approved read and contractual window; producer controls only cleared bumper/asset timing.

## s-watch

**Owner:** Henry

**Purpose:** Leave viewers with one specific future evidence test, not a scattershot news list.

**Opening line or optional landing line:** I want to see the same boundary hold when someone outside the vendor repeats the test.

**Talking points:**
- One watch: an independent, repeatable test of an agent runtime boundary
- Proposed test: attempt a harmless, policy-denied action in a disposable test environment and record allow/deny behavior, logs, and recovery
- Require enough configuration and procedure detail for another operator to reproduce it; a vendor demo alone does not meet that bar
- No result is established yet; do not imply WeeklyClaw or anyone else has already run the test

**Evidence/caveat:** This is a proposed watch/test, not an observed result or a claim that any named product failed. Run only in an authorized disposable environment with harmless actions.

**Question or handoff:** Advance to s-sources. Andy gives the single closing recap while the source links and WeeklyClaw Discord QR remain visible.

**Visual cue:** One watch frame: independent, repeatable runtime-boundary test. Avoid implying a completed test with a result graphic.

**Source links:**
- [NVIDIA OpenShell runtime controls, context for test](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/)
- [OpenClaw Enterprise pilot announcement, context for test](https://openclaw.ai/blog/openclaw-enterprise)

**Target time:** 1:15, 32:45–34:00; part of the combined 2:15 watch/close.

**Cut contingency:** Keep the one test and handoff; do not bring back discarded closing stories.

## s-sources

**Owner:** Andy closes; producer holds final frame

**Purpose:** Deliver the only closing recap while viewers can use source links and the Discord QR.

**Opening line or optional landing line:** Our answer this week is to test one change at a time: choose a model for a measured workload, define the responsibility you are delegating, and verify the boundary before expanding access. We also put a separate policy question on the table: what should vendors have to disclose after an incident? The sources are on screen. Tell us in the WeeklyClaw Discord which part of your agent stack you would change this week, and what evidence you would want first. Use the QR code or weeklyclaw.ai/discord. We’ll be back Friday, October 9 at 4 PM Eastern. Thanks for watching.

**Talking points:**
- Andy reads/paraphrases the single closing paragraph once
- Keep the source links available without reading the entire bibliography aloud
- Invite the viewer’s builder decision through the WeeklyClaw Discord QR/vanity route
- Next-show line remains Friday, October 9, 4 PM Eastern

**Evidence/caveat:** This is the on-air closing frame, not a separate post-show read. QR pixels and redirect/guild identity need integration QA; the textual URL alone does not verify the image.

**Question or handoff:** End after the sign-off; no second recap from either host.

**Visual cue:** Final Sources/Links frame with WeeklyClaw Discord QR. Hold through the sign-off; QR should use the verified asset and route https://weeklyclaw.ai/discord.

**Source links:**
- https://openai.com/index/introducing-gpt-6-1-sol/
- https://community.openai.com/t/gpt-6-1-sol-in-the-api-a-meaningful-step-up-in-cost-performance/1402388
- https://openai.com/index/introducing-dots/
- https://x.com/OpenAI/status/2104984504133918973
- https://x.com/OpenAIDevs/status/2105003318917697873
- https://openai.com/index/devday-2026-recap/
- https://www.youtube.com/watch?v=Fls_onRviPM
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- https://deepmind.google/models/evals-methodology/gemini-4-argon/
- https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
- https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
- https://openclaw.ai/blog/openclaw-enterprise
- https://nvidianews.nvidia.com/news/open-agent-safety-platform
- https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/
- https://www.youtube.com/watch?v=GYYP-eW58ug
- https://apnews.com/article/89ac416717adbfb1d72f2d85e6ce83d1
- https://www.hsgac.senate.gov/subcommittees/dmdcc/hearings/rogue-ai-securing-the-homeland-against-ai-agent-attacks/
- https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/
- https://www.axios.com/2026/09/29/openai-sued-hugging-face-breach
- https://www.youtube.com/watch?v=8WbW_n95wc4
- WeeklyClaw Discord: https://weeklyclaw.ai/discord
- Program Topics: https://docs.google.com/spreadsheets/d/16xAvCzRGA8XlWvihdSBcipw0wARzVZT9YysXzM0eFM8/edit

**Target time:** 1:00, 34:00–35:00; contained in watch/close. No additional Sources runtime.

**Cut contingency:** Give the brief recap, Discord invitation, and sign-off once. Skip link-by-link narration.

# Producer review only

- **Local draft only.** Revision rev2 does not authorize promotion, site publication, or edits to the original package. Approval remains UNVALIDATED pending integrated deck/document/media QA and host approval.
- **SFO playback spot-check remains open.** Timestamped transcript now supports three source windows and the actual Sonnet/cache/subagent argument. Verify spoken boundaries and playback before air. Selected cues are 00:30–01:29, 07:29–08:23, and 29:51–31:06, totaling 3:08 inside the 6:00 slot. They are transcript-derived, not pre-approved or independently replicated. Keep source cues separate from segment-clock timings; use the verified poster and prepared paraphrases if playback fails.
- **Video playback holds.** Dots 00:50–01:10, pause 01:05; Decisions 00:05–00:25, pause 00:10: official media and exact-time frames are verified, but browser/audio playback is not. Retain the Decisions “Shown 15x realtime” label and qualify its numbers as a vendor demo. NVIDIA Developer demo is verified as 5:29, but the excerpt is unverified. OpenAI’s official keynote is 53:34, with no verified excerpt. Use still/source-link fallbacks; no autoplay or guessed timestamps. Verify any local trim and usage rights before relying on playback.
- **Sponsor copy is preserved exactly from rev1.** The claims “zero telemetry” and “hacker houses worldwide” are not independently substantiated in this pass. Ask the producer/sponsor owner to clear them; do not silently rewrite approved copy. Both slots retain 90-second windows. The supplied reads are shorter than 90 seconds of ordinary speech; confirm the approved bumper/asset plan for the remaining slot time rather than adding claims or repeating the copy.
- **Host approval.** Confirm the proposed Hot Take side assignments. Confirm the precise adjacent-tooling relationship before expanding the existing disclosure. No host opinions, test results, or sponsor approvals have been invented.
- **Legal/source precision.** FTC confirmation on September 30 does not establish the probe’s opening date or motivation. Hearing testimony is scoped; LASST allegations are not findings. The primary LASST complaint remains unavailable in this package.
- **Model provenance.** Google’s table is original vendor evidence with mixed methodologies. Sol exact community-only scores are not primary-verified; do not merge charts into one ranking. Anthropic runs the GLM comparison and has a competitor conflict. CAISI uses a different ExploitBench metric. Keep these qualifications in spoken material.
- **Visual integration remains a parent QA gate.** Confirm the two four-card grids, readable benchmarks, verified source identities, all ten stable slide IDs, media paths, manual playback, and final-frame QR. QR must decode to the WeeklyClaw route and resolve to the correct community; a nearby href alone is insufficient proof.
- **Program Topics reference:** https://docs.google.com/spreadsheets/d/16xAvCzRGA8XlWvihdSBcipw0wARzVZT9YysXzM0eFM8/edit. This local-only revision includes the reference; it does not claim the external sheet has been synced or changed.

<!-- Episode 32 | revision rev2 | story-set-sha256 cee5cc422124f17a4b9d99326a790763ea58321c2dc545cf5aaea30d9ef6029d -->
