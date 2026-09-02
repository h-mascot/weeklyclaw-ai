# WeeklyClaw Episode 27 — Host Cheat Sheet (rev2)

**Show:** Friday 2026-08-28, 4:00 PM ET · **Hosts:** @AndyML + @HiM · **Sponsor order:** Heritage → Herald (rev2 inversion of Ep 26).
**Deck:** `deck.rev2.html` · 13 slides · render at 1600x900 · validate via `validate_deck.py` against Ep 26 authority.
**Hard stop:** 45:00.

## Runtime map

| # | Section            | Slide ID              | Time   | Lead    |
|---|--------------------|-----------------------|--------|---------|
| 1 | Cold open          | `s-cold-open`         | 1:30   | Andy→H  |
| 2 | Sponsor 1 (Heritage) | `s-sponsor-heritage` | 1:00   | Heritage|
| 3 | Story 1 · OpenAI   | `s-seg-openai-stack`  | 6:30   | Henry   |
| 4 | Story 2 · Qwen     | `s-seg-qwen-flash-next` | 6:00 | Henry   |
| 5 | Story 3 · Headlong | `s-seg-headlong`      | 5:30   | Henry   |
| 6 | Story 4 · Perplexity | `s-seg-portable-computer` | 5:00 | Henry |
| 7 | Story 5 · Robot data | `s-seg-robot-data`  | 5:30   | Henry   |
| 8 | Signal From Outside | `s-signal-outside`  | 7:00   | Andy→H  |
| 9 | Hot take          | `s-hot-take`          | 3:00   | Henry   |
| 10| Sponsor 2 (Herald) | `s-sponsor-herald`   | 1:00   | Herald  |
| 11| One to watch + close| `s-watch`            | 2:30   | Andy→H  |
| 12| Title card         | `s-title`             | n/a    | Visual  |
| 13| Sources / Links    | `s-sources`           | n/a    | Visual  |

Total scripted ≈ 44:30; hard stop 45:00.

## ASCII runtime bars (rev2 — corrected sponsor order)

```
Cold open    [█]                           1:30
Heritage     [█]                           1:00   ← opens Ep 27
Story 1      [██████]                      6:30   Henry leads
Story 2      [██████]                      6:00   Henry leads
Story 3      [█████]                       5:30   Henry leads (MANDATORY)
Story 4      [█████]                       5:00   Henry leads
Story 5      [█████]                       5:30   Henry leads
Signal out   [███████]                     7:00
Hot take     [███]                         3:00   Henry leads
Herald       [█]                           1:00   ← closes Ep 27
Close        [██]                          2:30
             [0─────10─────20─────30─────40─────45] min
```

## Ownership & rules

1. **Henry leads** every What Happened This Week segment (Story 1–5). Andy carries the fallback prose and handoffs.
2. **Never cut:** Stories 1, 2, 3. Heritage sponsor read. Henry segment lead on any news segment.
3. **Recap rule (Andy):** the close below recaps the episode exactly once. Do not re-recap items already covered in the close during host banter after Herald or in the Discord follow-up post. The recap is the recap.
4. **Sponsor rotation:** Ep 27 = Heritage → Herald (inverted vs Ep 26). Sponsor 1 opens after cold open; Sponsor 2 closes before the recap.
5. **News-window rule:** every selected story's primary launch receipt landed after Ep 26 airtime (2026-08-21 20:00 UTC).

## Handoff cues

- After cold open: "Henry, what's the frame?" → Henry line → Heritage sponsor.
- After Heritage: "Henry, let's start with the OpenAI stack." → Story 1.
- After Story 3: "Henry, that's an agent on a server. Perplexity just put one on the desk." → Story 4.
- After Story 5: "Now the part where we fight about it." → Hot take.
- After Signal From Outside: "Henry, signal absorbed. Time for the fight." → Hot take.
- After hot take: "Time for the second sponsor read." → Herald sponsor.
- After Herald sponsor: close prose. End of show.

## Cut priority (in order)

1. Signal From Outside: 7:00 → 6:00 (compress).
2. Story 5 (robot-data): 5:30 → 4:30 (compress).
3. Story 4 (Portable Computer): 5:00 → 4:30 (compress).
4. Story 3 Headlong: MANDATORY. Never cut.

## Close recap prose (Andy, single pass — never repeat)

"That's the show. Five stories, one fight. OpenAI stacked the layers and named the price. Qwen opened the architecture. Headlong shipped the harness and the warning label together. Perplexity put the agent on the desk. Figure made the data the company. The hot take is the deployment layer. Back next Friday, September 4, 4 PM ET. Scan the QR or visit weeklyclaw.ai/discord — invite rotates, so always use the site link."

## Standing actions (cron carries forward)

- **Website draft:** `/home/henrymascot/clawd/projects/weeklyclaw-ai` is not present on this host. Standing-authorized draft publication deferred. Next-tick recovery: copy Ep 26 sponsor/QR assets + rev2 deck/agenda/cheat-sheet to that path, `npm run build`, commit, push, verify canary.
- **Discord post:** standing-authorized after close prose. Use the rotating invite at weeklyclaw.ai/discord.
- **Media manifest:** `media-manifest.json` is the audit log. Every claim must trace back to a `media-manifest.json` entry.

## Rev2 vs rev1 (what changed)

- Sponsor order: rev1 had Herald first (bug); rev2 inverts to Heritage first per the standing rotation rule.
- Slide IDs renumbered: rev2 has `s-sponsor-heritage` (slide 3) before any `s-seg-*` slide; `s-sponsor-herald` (slide 11) sits between hot take and close.
- All host-facing artifacts (agenda, talking-points, henry-section, andy-section, host-cheat-sheet, speaker-notes) updated to match.
- Title card sponsor logo row updated: Heritage first, Herald second.
- Sources slide reorganized: S4/S5 + Signal + Hot Take on the right; S1/S2/S3 on the left.
