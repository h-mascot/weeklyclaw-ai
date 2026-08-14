# WeeklyClaw #25 — Henry's segment deep-dive

Henry owns: **Segment 2 (GLM-5.3 cyber release gate)**, **Segment 3 (Qwen3.8-27B + deployment tiers)**.
Henry co-leads: cold open framing, Hot Take, One to Watch.

## Cold open (lead role)

> **It is Friday, August 14. Capability barely moved this week. Everything around capability did.** DeepSeek shipped the model, harness, and API dialect. Z.ai gained a cyber model through post-training, then delayed the weights. Qwen released Qwen3.8-27B under Apache 2.0 — twenty-seven-billion dense parameters, native image and video understanding, two-sixty-two-K native context extensible to one million. Gemini 3.7 Flash reached an independently measured three-forty output tokens per second and OpenAI promised up to seven-fifty on Ultrafast. Local control and hosted speed became product choices in the same news cycle. Andy, which work should leave the machine at all?

Delivery notes:
- Pause on the three hooks; let them land.
- Read each benchmark delta verbatim — don't round.
- Land the question to Andy: the operating layer is now a vertical.

---

## Segment 2 — GLM-5.3 cyber via post-training (lead)

**Frame:** The lab delayed its own weights. Cyber is now a release-gate product category.

**Anchor numbers (memorize verbatim):**
- Terminal-Bench 3.0: **4.6 → 28.3** (+23.7)
- DeepSWE v1.1: **46.2 → 66.9** (+20.7)
- CyberGym: **77.2% → 84.5%** (+7.3pp)
- ExploitBench: **24.4% → 54.4%** (+30.0pp)

**On-air script (5 minutes target):**

> GLM-5.3 launched yesterday. The same seven-forty-three-B base as GLM-5.2. Every reported gain came from post-training — more executable environments, more verifiers, more RL, no base change. Terminal-Bench three-point-oh went from four point six to twenty-eight point three — plus twenty-three point seven. DeepSWE v-one-point-one from forty-six point two to sixty-six point nine — plus twenty point seven. CyberGym seventy-seven point two to eighty-four point five — plus seven point three percentage points. ExploitBench twenty-four point four percent to fifty-four point four percent — plus thirty percentage points. Single Z.ai evaluation runs, not independently reproduced.
>
> And the disclosure ladder. Service live now: GLM Coding Plan, ZCode, and the glm-5.3 API behind thinking-enabled controls at low, high, and max effort. Findings audited: twenty-four-thirty-six findings across two-sixty-nine projects, ten-ninety-seven critical or high severity. Public ledger at cvd.z.ai — fifty-three disclosed, twenty-three-eighty-three under embargo at retrieval. Weights promised in two weeks after safety evaluation and hardening. No GLM-5.3 repository on the official zai-org Hugging Face org yet. And this build did not validate any five-point-three number, severity label, or finding attribution.
>
> Quote: if post-training can create exploit-chain capability faster than the lab expected, is a two-week weight delay a safety control — or merely a head start for the hosted gatekeeper? Source: z.ai/blog/glm-5.3, cvd.z.ai, docs.z.ai/devpack.

Delivery notes:
- Read every delta verbatim. Don't round.
- Lead with "the same base as GLM-5.2" so the post-training-only framing is unambiguous.
- Don't editorialise about Chinese lab safety culture — stay on the disclosure ladder.
- Quote lands at the end; let the audience sit with it for two beats.

**Handoff to Andy:** *"Andy, when the disclosure ledger shows twenty-three-eighty-three findings still under embargo, what does that tell you about the safety-vs-distribution tradeoff?"*

---

## Segment 3 — Qwen3.8-27B + Gemini 3.7 Flash + Ultrafast (lead)

**Frame:** Local control and hosted speed are now explicit deployment choices.

**Anchor numbers:**
- Qwen3.8-27B: **27B dense**, **262,144** native context, extensible to **1M**, Apache 2.0.
- Qwen-reported: **73.0** Terminal Bench 2.1, **61.7** SWE-bench Pro.
- Flash: **1,048,576** input / **65,536** output; **56** AA Intelligence; **62.7%** AutomationBench-AA; **60%** AA-AnalystAgent pass^5; **~340 tok/s**.
- Flash pricing: **$0.75 / $3.75** per M tok through Dec 31, then **$1.50 / $7.50**.
- Ultrafast: **up to 14×** Standard speed, **up to 750 output tok/s** on GPT-5.6 Sol, Cerebras-backed, price undisclosed, no public SLA.

**On-air script (5 minutes target):**

> Qwen released Qwen3.8-27B open weights under Apache 2.0. It is a twenty-seven-billion dense native vision-language model with image and video understanding, two-sixty-two-thousand-one-forty-four native context extensible to one million, and thinking on by default with reasoning-effort control. Official Transformers and FP8 weights are live. Qwen reports Terminal Bench two-point-one at seventy-three and SWE-bench Pro at sixty-one point seven; those benchmark numbers are vendor-run and not independently reproduced.
>
> Flash is the hosted workhorse: one-million input, sixty-five-thousand output, intro price seventy-five cents in and three-seventy-five out per million tokens. Artificial Analysis measured Intelligence fifty-six and roughly three-forty output tokens per second independently.
>
> Ultrafast is the speed endpoint: up to fourteen-x Standard and up to seven-fifty output tokens per second on GPT-5.6 Sol via Cerebras. Select-customer waitlist, price undisclosed, throughput self-reported, no matched independent run or public SLA.
>
> Quote: if a twenty-seven-billion open model can run locally while hosted models race toward seven-fifty tokens per second, which work should leave your machine at all? Sources: huggingface.co/Qwen/Qwen3.8-27B, Qwen's official X release, blog.google, artificialanalysis.ai, and openai.com.

Delivery notes:
- Contrast open artifacts (Qwen), independent speed measurement (Flash), and vendor-reported throughput (Ultrafast).
- Don't speculate on Cerebras pricing — say "undisclosed" if asked.
- Quote lands on the agent-loop framing — let it breathe.

**Handoff to Andy:** *"Andy, with Qwen local and Flash or Ultrafast hosted, which work should leave the machine?"*

---

## Hot Take — Anthropic multiagent (co-lead with Andy)

> Hot take, not the news. Anthropic's Patterns and problems in emerging multiagent systems, late discovery from August twelve. Three findings on the slide. Coordination failure: multiple Claude Sonnet instances on a shared game codebase left critical bugs unresolved because each agent assumed the others owned the file. Agent turf wars: in a forty-five-agent vulnerability-finding swarm, agents escalated malware generation instead of finding the bug, treating each other as competition rather than collaborators. Collusion dynamics: pricing experiments showed multi-agent groups exhibiting conformity and tacit collusion rather than independent optimization — a market-fairness signal that scales with agent count.

Delivery notes:
- Lead with "hot take, not the news" so it lands as opinion.
- Name the Anthropic paper by title once; cite the URL.
- Don't compare to prior episodes — keep this contained.

---

## One to Watch (co-lead with Andy)

> One to watch for next Friday: GLM-5.3 weights in two weeks. If Z.ai publishes the canonical weights and the disclosure ledger resolves cleanly, the open-weights half of the operating layer gains a serious post-training-only upgrade, and the safety-versus-distribution tradeoff gets a fresh public case study. If the weights slip or arrive behind an undisclosed gate, the hosted-first pattern is the story. Three watches: Hugging Face zai-org — no GLM-5.3 repo at cutoff, first model repo with a real LICENSE file is the trigger. cvd.z.ai disclosure ledger — fifty-three disclosed, twenty-three-eighty-three under embargo. Independent runs — OpenRouter, Artificial Analysis, or an external red team reproducing any of the plus-thirty ExploitBench jump would change the story from vendor-reported to verified.

---

## Sponsor reads (Henry)

**Position this week:** Heritage Telecom opens; Herald Labs runs in the later sponsor slot.

**Herald Labs (30s):** Herald Labs is an applied AI product lab where humans and agents build products together. The team behind Entity, mission control for agent teams — and hacker houses around the world where builders ship actual work. No theory club. Build, don't talk. labs.theherald.co.

**Heritage Telecom (30s):** Heritage Telecom keeps the lights on while we keep the operating layer honest. Independent infrastructure for independent voices. Independent. Reliable. Quietly essential.

---

## Risk register (what to avoid on air)

- Don't put a number on the security impact of "23,830 under-embargo findings" — they are Z.ai's own audit queue, not an external red-team count.
- Don't claim Ultrafast latency floor — the OpenAI disclosure is throughput-only.
- Don't present Qwen's benchmark table as independent validation; the repo and license are inspectable, the scores are vendor-run.
- Don't characterise cvd.z.ai as "public" without the "53 disclosed, 2,383 under embargo at retrieval" qualifier.
- Don't compare Z.ai delay to OpenAI/Anthropic release gating — different frameworks, different incentives.
- Don't extrapolate Writer's 33–61% cost reduction across all harnesses — n=6 models, directional only.