# Release manifest template

Create `work/publishing/<episode>/release-manifest.md`. Keep one manifest per YouTube candidate.

```markdown
# Weekly Claw <episode> release manifest

Status: INVENTORY | EDITORIAL_REVIEW | MASTER_VERIFIED | THUMBNAIL_QA | THUMBNAIL_APPROVED | UNLISTED_REVIEW | DISTRIBUTION_STAGED | RELEASE_APPROVED | PARTIAL_RELEASE_BLOCKED | PUBLIC_VERIFIED

## Identity

- Episode:
- Guest(s):
- Requested input:
- Release candidate:
- Candidate SHA-256:
- Superseded local masters:

## Master proof

- Duration:
- Video:
- Audio:
- Participants and coverage:
- Fact-check/edit sheet:
- Source-visual map:
- Audio repair intervals and retained speaker:
- Outro visual/music proof:
- Focused tests:
- Full decode:
- Human review:

## YouTube package

- Topic ledger / title rationale:
- Canonical thumbnail title (2–5 words):
- Expanded listing title:
- Five-current-episode All-In comparison record:
- Thumbnail/listing lead-story identity check:
- Description revision:
- Chapter count:
- Captions:
- Thumbnail:
- Playlist:
- Audience/category/language:
- Paid promotion:
- Altered content:

## Master encode evidence

- Exact candidate path and SHA-256:
- Encode/concat command and input identity:
- Average video bitrate (video stream, kbps) and measurement method:
- 1080p 4,000 kbps house gate result:
- Final encoded AAC loudness/true peak:
- Technical QA receipt:
- Perceptual reviewer, coverage, result or explicit scoped acceptance:

## YouTube channel identity gate

- Intended display name:
- Intended handle:
- Intended immutable channel ID:
- Approved replacement authorization text (required when not the default tuple):
- Approved replacement authorization time and scope:
- Pre-upload Studio channel readback (display name / handle / channel ID / time):
- Post-upload Studio channel readback (display name / handle / channel ID / time):
- Post-upload watch-page channel readback (display name / handle / channel ID / time):
- Gate result: `PASS` | `YOUTUBE_CHANNEL_IDENTITY_BLOCKED` | `WRONG_YOUTUBE_CHANNEL`

## Thumbnail gate

- Topic/footage grounding:
- Participant list and verified references:
- Most recently approved thumbnail compared:
- Canonical title / visual idea / palette:
- AI generation method and real-person authorization:
- Candidate A/B/C paths:
- Candidate A/B/C SHA-256 values:
- Dimensions:
- Thumbnail maker:
- Independent reviewer:
- Independent QA record:
  - Source-footage grounding:
  - Participant count and coverage:
  - Each likeness quality:
  - Side-by-side face scale and spacing:
  - Clean eyeglass lenses:
  - Exact canonical-title wording:
  - Claw-before-WEEKLY mark order:
  - Themed accent colour:
  - Badge containment:
  - Meaningful A/B/C variation:
  - Adjacent-episode variation:
  - 1280×720 inspection:
  - 160×90 readability:
- Exact user thumbnail approval text:
- Thumbnail approval time:

## Upload

- YouTube video ID:
- Target channel tuple (display name / handle / immutable channel ID):
- Review URL:
- Exact uploaded source path:
- Uploaded runtime:
- Initial visibility:
- Copyright check:
- Community Guidelines check:
- HD processing:
- Final preview reviewed:

## X package

- Required account:
- Authenticated account:
- Native entitlement and observed limits:
- Candidate copy and revision:
- Candidate media path/SHA-256:
- Media Studio ID/state, if staged:
- Duplicate search evidence:
- Post ID / URL:
- Account/text/duration/playback verification:

## Bilibili package

- Required account / UID:
- Authenticated account / UID:
- Duplicate published/draft search evidence:
- Draft ID / upload receipt:
- Exact media path/SHA-256:
- Canonical title:
- Submitted title and live limit:
- Description/chapters/tags/category:
- Creation and commercial disclosures:
- Captions/localization state:
- Authentication/SMS/review blocker:
- BV/AV ID / public URL:
- Account/title/thumbnail/duration/playback verification:

## Publication

- Exact complete-release approval text:
- Approved video ID / title / thumbnail SHA-256:
- Approved release surfaces, including X/Bilibili:
- Approval time:
- Preflight and rollback:
- Final visibility:
- Public URL:
- External watch-page verification:
- Superseded upload IDs and visibility:
- Remaining issues:

## Surface reconciliation

| Surface | URL/target | Observed title/copy | Approved thumbnail proof | Visibility/status | Verifier | Verified at | Pass |
|---|---|---|---|---|---|---|---|
| YouTube custom thumbnail | | | | | | | |
| YouTube public channel grid | | | | | | | |
| YouTube public watch page | | | | | | | |
| weeklyclaw.ai homepage | | | | | | | |
| weeklyclaw.ai archive | | | | | | | |
| weeklyclaw.ai episode page | | | | | | | |
| X `@weeklyclaw` | | | | | | | |
| Bilibili `Weeklyclaw` | | | | | | | |

- Character-for-character expanded listing-title consistency across publishing surfaces:
- Thumbnail-title/listing-prefix consistency:
- Approved-thumbnail consistency:
- Release status justification:
```

Advance status only when every field required by that stage has evidence. `PUBLIC_VERIFIED` requires every surface row to pass; any failed or unverifiable row after public changes begin requires `PARTIAL_RELEASE_BLOCKED`.
