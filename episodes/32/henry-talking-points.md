# WeeklyClaw Episode 32 Henry section

**Revision:** rev2 · local review draft  
**Clock:** 35:00 + 3:00 buffer = 38:00 ceiling; 45:00 hard stop  
**Your role:** Lead all eight news cards, answer Andy in SFO, take the proposed affirmative in Hot Take, and give one watch. Andy handles both sponsors and the single recap on `s-sources`.

**Core question:** Which part of the agent stack would you change this week?

## Cold open · 0:45 shared · s-cold-open

- Model choice: measure the cost of a completed task, including retries and review
- Deployment choice: decide what the agent can reach and what a human must approve

**Optional line:** Start with the change you can test this week.

**Handoff:** Andy takes the Heritage read; Henry starts Sol on Grid A at 02:15.

## Story 1 · OpenAI launches GPT-6.1 Sol · 3:00 (Grid 1, slide `s-seg-grid-a` card 1)

*02:15–05:15 · Henry leads.*

**Henry talking points:**
- Start with one workload you already measure; hold the harness, success criteria, and review burden fixed
- One-fifth refers to Astra’s standard input/output token prices; retries and extra reasoning can change task economics
- Label the Sol card as a WeeklyClaw transcription of primary-source benchmark deltas; do not splice it into Google’s table

**Henry line (optional):** What would you move first if the quality survives your own regression set?

**Handoff cue:** Henry moves to Grid A card 2: Dots and the responsibilities that persist between prompts.

**Evidence/caveat:** Research/API evaluation; competitor scores come from public reports. Sol launch availability is Work, Codex and API, not yet Chat. No precise keynote cue is verified. Community-only exact scores are not used in the primary-source delta scorecard.

**Visual cue:** Show the clearly labeled WeeklyClaw transcription of primary-source benchmark deltas at card 1: DeepSWE high +6.4 pp over the prior Sol best; AutomationBench medium +2.2 pp over Opus 5.5; OSWorld offline max −2.1 pp versus Astra max. This is a source-cited rendered scorecard, not a vendor chart or the community repost. Keep the full OpenAI launch-source link. Enlarge it if labels are illegible; do not merge the deltas into Google’s comparison.

**Sources:**
- [OpenAI Sol launch](https://openai.com/index/introducing-gpt-6-1-sol/)
- [Community chart provenance](https://community.openai.com/t/gpt-6-1-sol-in-the-api-a-meaningful-step-up-in-cost-performance/1402388)
- [DevDay keynote, official OpenAI channel, 53:34](https://www.youtube.com/watch?v=Fls_onRviPM)

**Cut:** Cut the second benchmark example and the optional follow-up. Keep price scope, vendor attribution, and the one workload question.

## Story 2 · OpenAI introduces Dots · 2:00 (Grid 1, slide `s-seg-grid-a` card 2)

*05:15–07:15 · Henry leads.*

**Henry talking points:**
- Choose one recurring job with a clear stopping condition and owner
- Separate read-only investigation, drafting, and external action when setting permissions
- Ask how the operator notices a wrong assumption or stops work; launch capability is not an observed reliability result

**Henry line (optional):** What is the first job you would trust it to keep working on after you close the laptop?

**Handoff cue:** Henry moves to Grid A card 3: Decisions API.

**Evidence/caveat:** Vendor-described product behavior, not a WeeklyClaw reliability test. Pro/Business Premium access is market-limited; Enterprise/Edu/Healthcare beta requires admin enablement. Keep highly consequential actions outside any on-air demonstration.

**Visual cue:** Official OpenAI Dots video: manually play 00:50–01:10 (20 seconds), pausing at 01:05 on Jojo’s Computer browsing a wedding-cake site. Exact-time frames were decoded; browser/audio playback remains a pre-air check. Fallback: the verified 01:05 frame, source-linked. The clip is inside this card’s 2:00, not extra time. No autoplay or live connected-account action.

**Sources:**
- [OpenAI Dots launch](https://openai.com/index/introducing-dots/)
- [Official OpenAI Dots launch video, 2:28](https://x.com/OpenAI/status/2104984504133918973)
- [DevDay availability details](https://openai.com/index/devday-2026-recap/)

**Cut:** Cut the second hypothetical workflow. Keep one responsibility, one approval boundary, and the availability caveat.

## Story 3 · OpenAI previews the Decisions API · 2:00 (Grid 1, slide `s-seg-grid-a` card 3)

*07:15–09:15 · Henry leads.*

**Henry talking points:**
- Find a decision that genuinely has a small, known set of valid outcomes
- Test wrong-route behavior and ambiguous inputs, not just clean examples
- A constrained answer format does not prove the chosen action is correct or authorized; demo labels are vendor-reported

**Henry line (optional):** Where does a small decision API fit better than another open-ended agent turn?

**Handoff cue:** Henry moves to Grid A card 4: Gemini 4 Argon and its benchmark/access limits.

**Evidence/caveat:** Limited preview in the September 29 announcement. The vendor demonstration’s conditions, region, and concurrency are undisclosed in the verified material. Its 150 ms/request versus 1.6 s/request is not an independent benchmark or universal latency guarantee. Keep “Shown 15x realtime” visible. No independent accuracy or cost comparison is established.

**Visual cue:** Official OpenAI Developers demo: manually play 00:05–00:25 (20 seconds), pausing at 00:10. Preserve the “Shown 15x realtime” label. At 00:10 it displays 10,000/10,000 Decisions versus 2,000/10,000 Responses, 150 ms/request versus 1.6 s/request, and the vendor claim of about 10× faster decisions. Exact-time frames were decoded; browser/audio playback remains a pre-air check. Fallback: verified 00:10 frame linked to the original X post. The 20 seconds is inside this card’s 2:00. No autoplay.

**Sources:**
- [OpenAI DevDay recap, Decisions API section](https://openai.com/index/devday-2026-recap/)
- [Official OpenAI Developers Decisions demo](https://x.com/OpenAIDevs/status/2105003318917697873)

**Cut:** Cut the extra routing example. Keep finite choices, limited-preview status, and the ambiguity question.

## Story 4 · Google introduces Gemini 4 Argon · 3:00 (Grid 1, slide `s-seg-grid-a` card 4)

*09:15–12:15 · Henry leads.*

**Henry talking points:**
- The card shows the original vendor-table header and four agentic-coding rows; enlarge to the full table and pick one relevant row plus one where Argon trails
- The table mixes evaluation provenance and harnesses; do not turn it into a universal model ranking
- Access is part of the builder decision: qualify the rollout before recommending a migration

**Henry line (optional):** Which row resembles the work you actually need done?

**Handoff cue:** Advance to Grid B; Henry starts Anthropic’s GLM-5.3 evaluation at card 1.

**Evidence/caveat:** Google launch comparison, mixed-source evaluations. DeepSWE uses Google-run mini-swe-agent for Argon and external rival results; OSWorld is offline partial score and is not interchangeable with OpenAI’s comparison. Introductory API rates are $2/$10 input/output per million, later $4/$20, only if price is needed. No official Argon demo video was verified in this evidence pass.

**Visual cue:** The card uses the exact original Google vendor-table header plus all four agentic-coding rows: DeepSWE, FrontierSWE, Vibe Code, and Terminal-bench. This is a faithful crop, not a reconstructed table. The complete original table is available in the enlarged view through the full-table link. Open that view for legibility or broader comparisons; preserve model headers and relevant methodology qualifications.

**Sources:**
- [Google Argon launch and original table](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [DeepMind evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon/)

**Cut:** Cut additional benchmark rows and pricing detail. Keep a relevant result, a counterexample, mixed-source caveat, and restricted access.

## Story 5 · Anthropic evaluates GLM-5.3 cyber capabilities · 2:00 (Grid 2, slide `s-seg-grid-b` card 1)

*12:15–14:15 · Henry leads.*

**Henry talking points:**
- Read the numerator and denominator; avoid “nearly equal” as a blanket capability ranking
- Separate capability tests from safeguard tests and real deployment outcomes
- CAISI’s 61.1% is partial-credit, best-of-three scoring; it cannot be compared directly to 50/410

**Henry line (optional):** What does this test tell the person deciding which tools the agent can reach?

**Handoff cue:** Henry moves to Grid B card 2: OpenClaw Enterprise.

**Evidence/caveat:** The separate safeguard study measures attempted remote-target connection, not a successful exploit. Do not read the 64/92/100% connection figures as attack success. Prefill/abliteration unavailable through the Claude API is not a tested zero. No Henry-supplied GLM benchmark was recovered in the staged evidence; do not invent his result.

**Visual cue:** Use a faithful labeled scorecard with 50/410 and 56/410 if the original Anthropic figure cannot be retrieved. Mark it as a rendered scorecard, not an original screenshot. The evaluator, metric, denominator, and sandbox condition must remain legible.

**Sources:**
- [Anthropic GLM-5.3 study](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)
- [NIST CAISI evaluation for methodology contrast](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities)

**Cut:** Cut the secondary binary-exploitation and safeguard experiments. Keep 50/410 versus 56/410, evaluator conflict, sandbox conditions, and metric distinction.

## Story 6 · OpenClaw previews Enterprise · 2:00 (Grid 2, slide `s-seg-grid-b` card 2)

*14:15–16:15 · Henry leads.*

**Henry talking points:**
- Disclose the adjacent-tooling connection; assess the deployment problem on its merits
- Ask where permissions are enforced and whether model, harness, and sandbox can be changed independently
- Preview available for self-hosted internal pilots: do not call it private-only or production-ready

**Henry line (optional):** What would you need to see in a pilot before giving this access to a real business workflow?

**Handoff cue:** Henry moves to Grid B card 3: NVIDIA OpenShell and Sentry.

**Evidence/caveat:** The preview is accessible for self-hosted internal pilots; “internal pilots only” must not imply a closed private rollout. Vendor-described controls are not an independent security assessment. Keep the WeeklyClaw adjacent-tooling disclosure; producer must confirm any more specific relationship before elaborating.

**Visual cue:** Use the official OCE product/architecture material linked to the September 29 post; a source-linked launch capture is the fallback. Do not call a conceptual illustration a live deployment or imply a security audit.

**Sources:**
- [OpenClaw Enterprise public announcement, September 29](https://openclaw.ai/blog/openclaw-enterprise)

**Cut:** Cut the origin story and extra feature list. Keep public-preview maturity, one pilot question, and the connection disclosure.

## Story 7 · NVIDIA adds agent runtime controls · 2:30 (Grid 2, slide `s-seg-grid-b` card 3)

*16:15–18:45 · Henry leads.*

**Henry talking points:**
- Point to the enforcement boundary in the architecture; a model instruction alone is not a tested boundary
- Ask which resources and outbound actions policy can restrict, and what happens when a request is denied
- Keep Sentry monitoring separate from proof that every harmful action is detected or prevented

**Henry line (optional):** Show me the blocked action and the evidence an operator gets afterward.

**Handoff cue:** Henry moves to Grid B card 4: FTC confirmation, Senate hearing, and lawsuit allegations.

**Evidence/caveat:** Do not invent an excerpt, quote, tested stop time, or production safety outcome. A verified poster proves video identity, not a particular demo event. Keep vendor latency claims attributed if used; omit the number if it is not needed.

**Visual cue:** Prefer the official OpenShell runtime diagram and NVIDIA Developer demo. Verified video identity: GYYP-eW58ug, NVIDIA Developer, 5:29. No playback excerpt is cleared until start/end cues are verified; use the verified poster or architecture still as fallback. Manual start only, no autoplay.

**Sources:**
- [NVIDIA open agent safety platform announcement](https://nvidianews.nvidia.com/news/open-agent-safety-platform)
- [NVIDIA OpenShell developer explanation](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/)
- [Official NVIDIA Developer OpenShell demo, 5:29](https://www.youtube.com/watch?v=GYYP-eW58ug)

**Cut:** Use the architecture still instead of playback; cut the second implementation question. Never turn an unverified cue into an improvised demonstration.

## Story 8 · AI agents face regulatory and legal scrutiny · 2:30 (Grid 2, slide `s-seg-grid-b` card 4)

*18:45–21:15 · Henry leads.*

**Henry talking points:**
- Keep three statuses distinct: confirmed investigation, hearing/testimony, and allegations in a reported lawsuit
- Ask what evidence operators should preserve so a specific incident can be reconstructed
- Leave the mandatory-publication policy fight for Hot Take; this card establishes the record only

**Henry line (optional):** What do we know from the record, and what is still only being alleged?

**Handoff cue:** Andy takes Signal From Outside on the next frame; no extra news recap.

**Evidence/caveat:** No claim that the FTC opened the probe on September 30, that any proceeding was a reaction to an Accord, or that the sequence proves causation. Do not repeat the old “within 48 hours” framing. Avoid personal-attendance claims unless independently verified. LASST complaint not retrieved; Axios is reporting on allegations, not a ruling.

**Visual cue:** Show clearly labeled source material: AP confirmation, the Senate hearing page, and reported lawsuit status. Do not use an arrest/courtroom image to imply a judgment. Keep the three statuses visible in the presenter’s notes even when one receipt is on screen.

**Sources:**
- [AP report with FTC agency confirmation](https://apnews.com/article/89ac416717adbfb1d72f2d85e6ce83d1)
- [Senate September 30 hearing](https://www.hsgac.senate.gov/subcommittees/dmdcc/hearings/rogue-ai-securing-the-homeland-against-ai-agent-attacks/)
- [METR published testimony and scope](https://metr.org/blog/2026-09-30-chris-painter-senate-testimony/)
- [Axios report on LASST allegations](https://www.axios.com/2026/09/29/openai-sued-hugging-face-breach)

**Cut:** Cut extra hearing detail and names. Preserve the three legal/evidentiary statuses and the complaint limitation.

## Signal From Outside / weekly video review · 6:00

*Slide `s-signal-outside` · 21:15–27:15 · Andy leads. [Theo — OpenAI should be scared of this one](https://www.youtube.com/watch?v=8WbW_n95wc4), September 29, 2026, 31:46; Sonnet 5.5 review.*

**Henry talking points:**
- Theo likes Sonnet 5.5 but argues against choosing it as the everyday primary model; his introduction compares it with GPT-6 Sol
- His pricing caveat is about cache-heavy coding workloads; do not turn his figures or usage into a universal cost result
- His concrete niche is Sonnet handling investigative subagent work called by Opus; the claimed benefit remains his practitioner hypothesis
- Name one task and a result that would disprove the routing choice; count retries, coordination, and human review

**Henry line (optional):** Which route wins after we count retries and review?

**Manual source cue 00:30–01:29 (59s) · segment clock 00:25–01:24: A good model without a clear primary-model case.** Transcript-derived; PENDING PLAYBACK / pre-air spot-check.

**Manual source cue 07:29–08:23 (54s) · segment clock 01:56–02:50: Cached-token costs qualify the headline price.** Transcript-derived; PENDING PLAYBACK / pre-air spot-check.

**Manual source cue 29:51–31:06 (75s) · segment clock 03:30–04:45: Sonnet as an Opus-called investigative subagent.** Transcript-derived; PENDING PLAYBACK / pre-air spot-check.

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

**Handoff cue:** Henry lands one final sentence; Andy takes the Herald Labs read. Do not revisit the news chronology.

### Production notes (not read on air)

These are proposed debate assignments, not statements of Henry’s or Andy’s existing beliefs. Confirm the sides before air. The news card established the status of investigations, testimony, and allegations. This debate is about a prospective publication duty: who must disclose what, to whom, and when. Do not re-tell those news events or use them to imply a legal finding. Clock: motion/setup 0:15; Henry affirmative 0:45; Andy countercase 0:55; Henry rebuttal 0:40; Andy rebuttal/mind-changer 0:50; Henry mind-changer/closer 0:35 = 4:00.

- Cut: shorten opening cases first; retain one rebuttal and one mind-changer per side. No new alleged incident is needed to make the motion arguable.

## One to watch · 1:15 · s-watch

*32:45–34:00, after Andy’s Herald read.*

- One watch: an independent, repeatable test of an agent runtime boundary
- Proposed test: attempt a harmless, policy-denied action in a disposable test environment and record allow/deny behavior, logs, and recovery
- Require enough configuration and procedure detail for another operator to reproduce it; a vendor demo alone does not meet that bar
- No result is established yet; do not imply WeeklyClaw or anyone else has already run the test

**Optional line:** I want to see the same boundary hold when someone outside the vendor repeats the test.

**Handoff cue:** Advance to s-sources. Andy gives the single closing recap while the source links and WeeklyClaw Discord QR remain visible.

## Producer review for Henry (not read on air)

- Confirm the proposed debate side and the adjacent-tooling disclosure
- SFO cues are transcript-derived and pending playback; NVIDIA excerpt cues are still unverified. Dots/Decisions exact-time frames are verified, with playback/audio checks pending
- On `s-sources`, leave Andy the only recap; no second Henry summary
- Program Topics: https://docs.google.com/spreadsheets/d/16xAvCzRGA8XlWvihdSBcipw0wARzVZT9YysXzM0eFM8/edit

<!-- Episode 32 | revision rev2 | story-set-sha256 cee5cc422124f17a4b9d99326a790763ea58321c2dc545cf5aaea30d9ef6029d -->
