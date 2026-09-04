# WeeklyClaw Guest Intelligence

Use when Henry asks for a recurring guest pipeline tied to current AI news. This is separate from ordinary topic intake: every accepted item must identify a plausible person or concrete team role who can explain a timely development on air.

## Trigger pattern

Treat news as an invitation trigger when it creates a clear audience question that the source team can answer. Strong examples:

- blockbuster model or product release
- founder or lead researcher becomes newsworthy
- breakout open-source project or benchmark result
- major strategy, funding, policy, or ecosystem shift
- public appearance or interview that reveals a timely angle

Kimi shipping a major model and DeepSeek founder Liang Wenfeng entering the news cycle are canonical patterns. A company mention alone is not a guest lead.

## Weekly scan

1. Search official company/lab channels and credible independent reporting in English and Chinese.
2. Cover established labs and fresh breakouts. Baseline watchlist: Moonshot AI/Kimi, DeepSeek, Alibaba/Qwen, Zhipu/GLM, MiniMax, Baidu/ERNIE, ByteDance/Doubao/Seed, Tencent/Hunyuan, Huawei/Pangu, 01.AI, and StepFun.
3. Prefer developments from the last seven days.
4. Verify the event against a primary source when possible. Label vendor claims and rumor-only reporting.
5. Convert each event into a named person or concrete role, a specific `why now`, and a WeeklyClaw conversation angle. Prefer a hands-on builder or operator over the most famous executive.
6. For each strong event, map 2–5 plausible speakers internally before selecting the best-matched candidate. Do not expose the full internal list unless requested.
7. Score candidates out of 15: trigger recency/significance (0–3), direct builder credibility (0–3), practical operator insight (0–3), useful on-air conversation potential (0–3), and access or relationship plausibility (0–3). Append only candidates scoring at least 10/15, maximum five per run.
8. Deduplicate by person, company/team, and underlying news hook. A new article, benchmark recap, or different spokesperson around the same release is not a new lead. If the sheet already contains that hook, skip it rather than changing the angle to manufacture novelty.
9. Use relationship context only when a private relationship lookup returns evidence. If that route is unavailable, say it was not checked and make no relationship claim; public contact routes may still inform the access score.

## Guest ledger

Canonical workspace artifact:

- Spreadsheet: `Weekclaw Feedback`
- Spreadsheet ID: `147RhKY4B10HrqTltdzuoleFEos9t7-Zyk2O0V_7bxt0`
- Tab: `Guests`

Columns:

`Guest / target | Organization | Why now | Trigger pattern | Suggested WeeklyClaw angle | Outreach owner | Status | Source / notes | Added`

Defaults for scanner-added rows:

- `Outreach owner`: `Jim`
- `Status`: `Candidate`
- `Added`: current ISO date
- `Source / notes`: primary-source URL plus any material independent receipt

Never clear or rewrite existing rows. Append only accepted, deduplicated candidates.

## Google Sheets write path

Use the Sheets API with the existing spreadsheet when Drive-file operations are unavailable or unnecessary. Creating a fresh spreadsheet with Sheets scope does not prove it lives in the requested Drive folder. A tab added to an existing spreadsheet already in that folder preserves placement without requiring a Drive move.

For the current Workspace helper:

- library: `~/enterprise-home/Skills/google-workspace/scripts/workspace-lib`
- auth subject: `henry@curacel.ai`
- scope: `https://www.googleapis.com/auth/spreadsheets`

After every write:

1. Read back the appended range through the authenticated Sheets API and verify name, organization, Jim ownership, source URL, and date. API success without readback is incomplete.
2. Fetch spreadsheet metadata and confirm the `Guests` tab's current numeric `sheetId`. Address writes by the tab title (`Guests!A:I`), not by a copied URL's `gid`, because shared URLs can carry a stale or different tab ID.
3. Build the operator link from the verified metadata: `https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=<GUESTS_SHEET_ID>`.
4. Treat unauthenticated CSV/export access as a separate sharing check. An HTML login/error response does not invalidate an authenticated API write; report the link as private or unverified rather than claiming public verification.
5. Persist a compact local receipt containing pre-write row count, appended count, updated range, post-write row count, and read-back rows.

## Delivery

- Fresh candidates: compact bullet per guest with score, organization, why now, interview angle, and source. End with `Jim: outreach candidates are in the Guests sheet.`
- No qualifying lead: `No fresh China guest candidate cleared the 10/15 bar this week.`
- Blocked: one terse line naming failed stage and evidence.

Report research-channel degradation precisely: name the unavailable channel and continue with materially different primary and secondary routes. Do not harden a transient setup or quota failure into a general claim that the tool does not work.

Do not contact guests, make commitments, or launch outreach. The scan prepares Jim's queue; outreach remains human-controlled unless separately authorized.
