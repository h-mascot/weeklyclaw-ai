# Rolling Candidate Intake (daily, non-Friday)

The daily intake cron feeds the candidate pool that the Friday show-prep pipeline consumes. It runs **outside** the Friday 11–16 ET time gate — it is a scheduled-intelligence-sync task, not a show-prep build. Its output is appended to `episodes/<N>/daily-topic-list.md` and synced to the public programming sheet via `scripts/weeklyclaw-program-sheet.js`.

## Post-show episode rollover

Daily intake must advance to the next episode after the prior show airs; do not keep appending Saturday findings to Friday's frozen episode.

1. Read every dated numeric episode from `showprep/state.json`, `daily-topic-list.md`, and `agenda.md`. Choose the smallest episode whose show date is on or after today's New York date.
2. If none exists, confirm the latest dated episode actually aired using the live WeeklyClaw site, video index, or another canonical publication surface. Then advance exactly one episode beyond that aired show. Do not infer the next episode from the highest directory alone.
3. Derive the new show date from the verified recurring schedule and latest aired date. Record the evidence and date derivation in the run report.
4. Create only `episodes/<N>/daily-topic-list.md` with the new show date and lineage. Do not create an agenda or `showprep/` package during daily intake. If no canonical agenda exists, report `agenda additions: 0`.
5. Bind the Sheet write explicitly with `WEEKLYCLAW_EPISODE=<N>`. The writer may create the new `Episode <N>` tab, but it must not rewrite prior tabs.

This rollover is an intake-state transition, not Friday show prep. The Friday BUILD later resumes the pre-created upcoming episode directory instead of skipping another number.

## Source-verification toolchain

Use multiple independent tools in parallel; never rely on a single source for a fresh launch claim.

| Signal type | Tool | Notes |
|---|---|---|
| X/Twitter primary posts | `~/clawd/scripts/bird-env.sh read <url> --plain` | Gives likes/RTs for engagement signal, full text, QT chains |
| Broad web discovery | Exa search via `mcporter call 'exa.web_search_exa(query: "...", numResults: N)'` | Best for finding primary blog posts, HF cards, GitHub repos |
| Quick web lookup | `web_search` | DuckDuckGo-backed; can time out, have Exa as fallback |
| Primary blog/article full text | Jina Reader: `curl -sS 'https://r.jina.ai/<url>'` | **Fallback when `web_extract` fails** (e.g., firecrawl credit exhaustion). Returns clean markdown. |
| Hugging Face model verification | `curl -sS 'https://huggingface.co/api/models/<org>/<model>'` | Machine-readable: downloads, likes, tags, siblings, timestamps, license. Prefer this over scraping bot-protected HF pages. |
| GitHub release verification | `gh api repos/<org>/<repo>/releases/tags/<tag>` | Full release body, publish timestamp, tag confirmation. Prefer over scraping GitHub HTML. |

### Jina Reader fallback pattern

`web_extract` (firecrawl-backed) can fail with "Payment Required: Insufficient credits." When it does, pivot to Jina Reader for primary blog/article content:

```bash
curl -sS 'https://r.jina.ai/https://www.example.com/blog/post' -o /tmp/article.md
```

This returned clean markdown of the Not Diamond Code launch blog when firecrawl was exhausted. Jina Reader is a free, unauthenticated fallback for extracting article body text.

### Multi-surface ecosystem launch verification

When one vendor ships a model, API update, harness/runtime, and packages together, score and write them as **one ecosystem cluster** when they share the same operator takeaway. Do not manufacture separate model, harness, and package rows.

Verify each surface with its native machine-readable source:

- **Model artifact:** Hugging Face API for exact checkpoint ID, `createdAt`, `lastModified`, license, parameter metadata, and actual weight shards.
- **API state:** first-party changelog/pricing/docs for model alias, context/output limits, supported protocols, effort controls, and effective-date pricing.
- **Harness/runtime:** GitHub REST for repository creation/publication timing, license, commit/tree contents, and preview/stability warnings. A repository becoming public today may contain older internal commits; distinguish public availability from code authorship dates.
- **Runnable distribution:** npm/PyPI registry metadata for exact package name, version, publication timestamp, executable entry point, and dependency surface.
- **Hosted availability:** provider catalog API for the live route, limits, modalities, prices, and supported parameters.
- **Launch clock:** official social/company receipt for the public-launch timestamp and exact announcement wording.

Keep evidence planes separate. A hosted provider's catalog or composite score verifies availability or an independent measurement, not the vendor's harness-specific benchmark. A runnable release candidate proves installability, not stability. Put preview warnings, compatibility-break risk, and unexecuted local tests in `Evidence pulled` and `Status`.

## X coverage completion gate

Do not treat failure of the generic `twitter` CLI as proof that the WeeklyClaw X source is unavailable. The canonical read route is `~/clawd/scripts/bird-env.sh`; exercise that route independently before marking social coverage incomplete.

1. Run a bounded authenticated home/search pass through `bird-env.sh` and retrieve direct post URLs for accepted leads.
2. If a direct single-post read verb is unavailable or rejected by a read-only safety wrapper, use the official account's `user-tweets` timeline or bounded `search` route and match the exact stable post ID. This verifies that post only; it does not prove timeline completeness.
3. If the canonical wrapper fails across its read routes, record its exact read error in the run report and preserve X coverage as `INCOMPLETE`; do not report zero findings.
4. Search-engine or Exa results containing X URLs can verify individual, artifact-backed posts, but they do not prove a complete feed scan.
5. Never let an unavailable social feed block primary artifact verification through official blogs, GitHub, Hugging Face, registries, or release APIs. Accept candidates only when those receipts independently clear the evidence gate, and disclose the social coverage gap.

This gate prevents a generic-client credential state from silently downgrading a source route that has its own managed credentials.

## Henry X pulse calibration

Every daily intake and Friday BUILD must scan Henry's recent public X timeline in addition to the general internet/X sweep:

```bash
BIRD_ACCOUNT=henry ~/clawd/scripts/bird-env.sh user-tweets iAmHenryMascot -n 40 --json
```

Use the latest seven days, with extra weight on the current 24–48 hours. This is an editorial-priority signal, not factual proof.

- Direct posts and quote-post commentary are stronger signals than bare reposts.
- Repeated attention to the same launch/cluster is stronger than a single interaction.
- Preserve the exact post URL and quoted primary source where available.
- Calibrate `Henry/operator angle`, ordering, merge decisions, and host questions from this pulse.
- Verify every factual claim against primary artifacts before airing it. Henry's timeline can tell us what matters to him; it cannot turn a rumor into a release.
- If Bird fails, record `HENRY_X_PULSE_INCOMPLETE` with the exact error and continue with primary-source research. Do not pretend the pulse was scanned.
- The programming Sheet remains a candidate ledger and audit trail. It is not a voting gate. Do not ask Henry to vote on Sheet rows when the X pulse plus evidence-led scoring produces a clear lineup. Escalate only genuine close calls, unsupported claims, or material post-approval swaps.

### Watch-state transition refresh

A countdown, notify page, livestream, or promised future weight release is not
an artifact. Keep it in the watch ledger until the exact official model/API/
package endpoint becomes public and inspectable. On every material Friday
refresh, re-query the native machine-readable endpoint for watched launches,
not just the search index. When the artifact flips live during the show-prep
window:

1. capture the official launch clock and artifact/API timestamps separately,
2. verify public/gated state, exact model ID, license, config, weight variants,
   and runtime compatibility from native APIs/model cards,
3. replace or explicitly supersede the stale watch disposition so the current
   ledger does not simultaneously say “unreleased” and “promoted,”
4. merge into an existing causal segment when that preserves the five-story
   shape; do not add a sixth segment merely because the release was late,
5. label model-card benchmark tables vendor-reported until independently run.

Prediction velocity never clears the evidence gate, but a live official
artifact can legitimately change the lineup minutes later.

## Candidate intake structure

Each daily intake section in `daily-topic-list.md` follows this shape:

```markdown
## YYYY-MM-DD — rolling candidate intake (freshness-verified, HH:MM TZ)

**Editorial thread note (not a candidate itself):** [When 2+ fresh stories converge
on one thesis, name the thread and recommend a synthesized beat, not N segments.]

**Rule:** [What's frozen/aired, what's supporting color, what's a repeat to avoid.]

### Candidate N — [Headline that states the operator-relevant claim]

- **Score:** N.N (consequence × .25 + operator × .20 + evidence × .20 + novelty × .15 + narrative × .10 + clip × .10 = raw, [held/discounted for reason])
- **Source tier:** [Primary + corroboration description]
- **Sources:** [URLs, one per line, dot-separated with ` · `]
- **Sub-stories:** [Full factual summary with numbers, named entities, and what the primary source claims]
- **Evidence pulled:** [What was actually fetched and verified, which API/CLI confirmed it, and what remains vendor-reported or unverified]
- **Why discuss:** [Operator-relevant framing, connection to prior episode thesis]
- **Suggested host question:** ["One sharp question in quotes"]
- **Visual plan:** [Slide/asset direction with explicit vendor-reported labels]
- **Media URLs:** [1–3 primary URLs for on-air use]
- **Status:** CANDIDATE — [freshness verdict, evidence caveats]
```

## Evidence-discipline labels

Every performance/benchmark figure gets one of these labels inline:

- **`vendor-reported`** — claimed by the launching org in their own blog/card/notes, no independent reproduction cited.
- **`author-reported`** — claimed in release notes or repo README by the authors.
- **`company-reported`** — claimed in a press release.
- **`single-source`** — only one source found; needs corroboration before air.
- **`sourced claim, not a measured fact`** — cited by a secondary source attributing an unnamed primary study; locate the study before stating as fact on air.

When the show's own operator stack has a COI (e.g., covering Hermes Agent while running on Hermes), flag it explicitly in both the candidate's Source tier and its Visual plan.

## Editorial thread synthesis

When 3+ independent fresh stories in the same week converge on one thesis, do not run them as separate segments. Instead:

1. Write a one-paragraph **editorial thread note** at the top of the daily intake section.
2. Name the thesis and list which candidates reinforce it from which angles.
3. Recommend "one synthesized cold-open or hot-take beat, not N separate segments."
4. Cross-reference candidate numbers so the Friday build can pick up the thread.

Example (2026-08-05): Orchard (trains-in-harness), Microsoft Agent Framework Harness GA (harness-as-product), LFM2.5-2.6B (post-trained-in-harness), Not Diamond Code (routes-between-models-per-step), and Z-Agent OSWorld 90.2% ("the harness did it") all converged on "the harness is the headline, not the model."

## Explicit non-candidate ledger

End each daily intake with a **supporting color and explicit non-candidates** subsection. For each evaluated-but-held item:

- Name the item, date, and primary source.
- State the **reason** it's held (repeats aired coverage, single-source, supporting color only, territory-limited license, etc.).
- State the **disposition**: "hold as supporting color," "not a standalone candidate," "fold into synthesized beat."
- Be explicit about what it repeats from which prior episode.

This prevents future reruns from re-evaluating the same items from scratch and duplicating candidates.

## Pre-write editorial gate

Run this gate after research/model critique and before appending candidate blocks:

1. Search the complete canonical `episodes/<N>/daily-topic-list.md` for the company, model family, product, and editorial angle, not just the proposed headline.
2. Read every explicit `Rule:` / frozen-coverage note in the file. A technically fresh announcement can still be cluster color when it extends an aired pricing, model, or harness story.
3. Resolve conditional reviewer advice with tools. For example, if a review says “standalone only if no GPT/OpenAI item exists,” search the ledger and make the binary decision; do not carry the condition into the write.
4. Prefer one strong standalone plus explicit update color over manufacturing a second or third candidate to fill a quota.
5. Record demotions in the non-candidate/supporting-color ledger so the Friday build understands why the item was not promoted.

For a requested three-pass review, use the passes operationally: **Pass 1** critiques the proposed selection and scores; **Pass 2** executes freshness, duplicate, source, and rollout checks; **Pass 3** states the corrected standalone/color/skip decision. Only the Pass 3 decision is written to the candidate ledger.

## Sheet sync

After appending to `daily-topic-list.md`, sync to the public programming sheet:

```bash
cd ~/weeklyclaw && WEEKLYCLAW_EPISODE=<ACTIVE_EPISODE> node scripts/weeklyclaw-program-sheet.js
```

Pass `WEEKLYCLAW_EPISODE` explicitly. This binds the write to the episode selected and evidenced by the current run instead of asking the writer to rediscover it.

The parser treats **every `###` heading as a Sheet candidate row**, not only headings beginning with `Candidate`. Therefore:

- Use `### Candidate N — ...` only for promoted clusters.
- Use `####` headings inside supporting-color, resurfaced, watch, and rejection ledgers.
- Before sync, confirm every promoted block has the exact single-line fields the parser reads: `Score`, `Source tier`, `Sources`, `Sub-stories`, `Evidence pulled`, `Why discuss`, `Suggested host question`, `Visual plan`, `Media URLs`, and `Status`.

The script parses those candidate blocks and their `- **Label:**` fields, writes rows to the active episode tab, and returns a JSON receipt with the spreadsheet URL. Treat the Sheet as a durable record, not a ballot. Selection should proceed from evidence-led scoring calibrated by the Henry X pulse; do not block the show waiting for spreadsheet votes.

Do not block pre-emptively because a generic Hermes Google-token probe reports no token. The canonical writer uses the Enterprise `workspace-lib` credential route for `henry@curacel.ai`; run the canonical sync command and treat its real result as authoritative. A setup probe is diagnostic context, not a substitute for exercising the production path.

Verification has two layers:

1. **Write receipt:** require `"ok": true`, the correct `activeEpisode`, the exact `updatedTab`, and a tab list containing that exact tab.
2. **Row readback:** query the active tab through the Sheets API using the same `workspace-lib` auth route as the writer. Verify one header plus exactly the expected candidate rows, and check each row's title, score, source, status, and evidence canary. A tab-list receipt proves the write path completed, not that the intended rows parsed correctly.

Save the write receipt and readback under `output/program-intelligence/`. If the active episode has no canonical agenda yet, do not invent one during daily intake: report `agenda adds: 0` and carry `ADD TO AGENDA` as a recommendation in the candidate status for Friday show prep.

## Run report and wire-output discipline

Before research, create or update `output/program-intelligence/YYYY-MM-DD-run.md`. Keep detailed discovery, freshness decisions, caveats, rejection rationale, local-write evidence, and the final Sheet/readback receipt there as the run proceeds.

The scheduled job's delivered response is only a wire receipt, not the report body. Follow the active cron contract exactly; for the current program-intelligence job this means plain text, at most 500 characters and five bullets, naming episode, new-cluster count, actual agenda-add count, updated tab, report path, and Sheet URL. Validate the character count before returning.

## Freshness vs. resurfaced

Use the **prior intake completion timestamp** from its receipt/run artifact as the cutoff, not midnight, the previous intake's start time, or the date heading alone.

**Episode-assignment boundary = prior episode AIRTIME (Henry, 2026-08-21).** The intra-week intake cursor above decides what is *new since the last pass*; it must never decide which *episode* a story belongs to. A story qualifies for episode N only if its primary launch receipt landed AFTER episode N-1 aired (Friday 16:00 ET / 20:00 UTC). The Friday-morning intake completes pre-show, so a launch between that intake and airtime (e.g. Qwen3.8-2.4T posted 2026-08-14 15:02 UTC, ~5h before Episode 25 aired) belongs to the episode airing THAT day, not the next one. When the intake run happens on a show day before airtime, treat pre-airtime launches as same-day episode material and post-airtime launches as next-episode material. Follow-on developments of an already-aired story (community quants, demand metrics, variant routes) are supporting color, never a fresh segment for the next episode.

- **Fresh:** primary artifact published or materially updated after the prior intake completed. CANDIDATE, subject to the duplicate/editorial gate above.
- **Resurfaced:** real primary source but `published_time` predates the prior intake completion cutoff. Note in a "Resurfaced / late-discovery ledger" subsection, not as a new candidate. Do not relabel resurfaced material as new.
- **Update to aired material:** an incremental update to something already covered in a frozen/aired episode. Note as "not repeated as a new topic" or fresh cluster/update color.
- **Boundary case:** when a source lands during the previous intake window but was missed, classify it as late discovery unless the previous receipt explicitly left the scan open for it.

### Multi-clock launch verification

A release can have several legitimate timestamps. Record them separately instead of forcing one date onto the whole cluster:

1. **Artifact clock:** repository/model/package creation and file-upload timestamps.
2. **Public-launch clock:** canonical launch post, company announcement, or official social receipt.
3. **Availability clock:** API/catalog/download route becomes usable.
4. **Documentation clock:** docs or changelog last-modified time.

Use the clock that matches the claim:

- Pre-staged weights or packages do not make a later official public launch stale. If the public-launch clock clears the cutoff and the artifacts are live, accept the cluster as a fresh public launch while stating that files were staged earlier.
- Early press or wire coverage before the cutoff does not make a later first-party launch receipt stale. For a `public launch` claim, use the launching actor's canonical page or official social receipt; record the earlier coverage separately. Do not use this rule to revive a product whose own official launch already predates the cutoff.
- A fresh documentation `Last-Modified` header does not create a new launch when the capability's public-launch and availability clocks predate the cutoff. Treat substantive doc changes as technical update color unless they change deployability or policy.
- A vendor index, search card, or research listing may show today's date while the canonical article body and publication metadata are older. Classify from the canonical article and record the discrepancy as `index-date mismatch`; never promote the listing date.
- A launch article without a live availability route verifies announcement only. Keep `ANNOUNCED`, `ARTIFACT_LIVE`, and `DEPLOYABLE` separate.
- For promised weights or packages, bound negative evidence to the exact surfaces and retrieval time: inspect the canonical organization inventory plus at least one relevant distribution/catalog API, then write `not observed in the checked surfaces`, not a universal claim that the artifact does not exist.
- When clocks disagree, put exact timestamps and the resulting classification in `Evidence pulled`; do not hide the discrepancy.

### Product-boundary verification for persistent agent systems

For products marketed as teams of agents or digital coworkers, verify the security and operating boundary from first-party docs, not the product metaphor:

- Determine whether agents receive separate computers, screens, sessions, credentials, filesystems, and permission scopes, or merely separate names/threads on one user-scoped machine.
- Check whether credentials, browser sessions, files, routines, connectors, and local-computer permissions are shared across the roster.
- Read approval, storage, privacy-mode, reset/delete, and administrator-control documentation.
- State the blast-radius implication plainly. “Multiple agents” is not “multiple security boundaries” unless the product proves isolation.
- Keep internal use cases and early-user praise labeled company/community-reported until a controlled end-to-end task or independent audit exists.
