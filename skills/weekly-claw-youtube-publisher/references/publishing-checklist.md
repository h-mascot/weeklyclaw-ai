# YouTube Studio publishing checklist

Operate against the video ID and exact source path recorded in the release manifest.

## Details

- New upload; never replace an existing video.
- Target YouTube channel identity is recorded before upload as an exact tuple: display name, handle, and immutable channel ID. For Weekly Claw the default tuple is `Weeklyclaw` / `@WeeklyClaw` / `UCa0Mxn9vyx6NnU-aBgRcRvg` unless the release manifest names an approved replacement.
- Before file selection, read back the active Studio channel header/account switcher and verify it matches the tuple exactly. A signed-in Google account, avatar, or prior channel name is not proof. If it differs, switch channels and verify again; otherwise stop with `YOUTUBE_CHANNEL_IDENTITY_BLOCKED`.
- A single video cannot be transferred between separate YouTube channels. If a post-upload audit finds the wrong channel, preserve the wrong-channel video ID, mark `WRONG_YOUTUBE_CHANNEL`, and require an explicit recovery decision; the normal fix is a new upload to the verified target channel. Whole-channel Brand Account transfer is a different operation with destination-replacement/deletion risk.
- Exact master filename and expected runtime.
- Exact independently QA-passed and user-approved thumbnail path and SHA-256.
- Record separate `thumbnail_headline` (short artwork text) and `episode_title` (full canonical listing title) values. A thumbnail-wording revision or candidate approval changes only `thumbnail_headline`; retain `episode_title` unless the user explicitly changes the listing title. This adds no approval step.
- `thumbnail_headline` is concise, readable, supported by the episode, and rendered exactly on the selected artwork; assess the hook as well as visual execution.
- `episode_title` complements the artwork and accurately represents the episode. Follow the title-development workflow and record its evidence and selection rationale; keep the listing under 100 characters, follow established episode numbering where appropriate, and preserve an explicit exact user-supplied episode-title override.
- Description contains verified summary, chapters, canonical links, sponsors, and focused hashtags.
- Custom 1280×720 thumbnail selected from three independently QA-passed candidates; confirm the exact approved asset actually renders on the YouTube listing.
- `Weekly Claw — Full Episodes` playlist when available.
- Audience: not made for kids unless episode evidence says otherwise.
- Age restriction: no unless required.
- Show title, description, chapters, thumbnail, and listing preview for review before Public unless the current request already grants exact publication approval.

## Disclosures and advanced settings

- Paid promotion: enable when sponsors, product placement, endorsements, or other paid relationships are present.
- Altered/synthetic content: answer from the video’s actual content, not from the thumbnail workflow.
- Tags: accurate and non-spammy.
- Language: English unless evidence says otherwise.
- Caption certification: select the accurate option.
- Recording date/location: add only when verified and useful.
- Licence: Standard YouTube licence unless instructed otherwise.
- Embedding: on.
- Shorts remixing: follow channel default unless instructed.
- Category: Science & Technology for normal Weekly Claw episodes.
- Comments: on with channel-default moderation unless instructed.

## Video elements and checks

- Upload matching captions and confirm Published state.
- Add end screen/cards only when appropriate source targets are known.
- Wait for copyright/ad-suitability checks when shown.
- Confirm SD and HD processing.
- Play the opening, every corrected/source-visual passage, repaired audio interval, guest segment, and outro from the uploaded copy.
- After upload, verify the Studio channel and watch-page channel both match the recorded target tuple. A mismatch is `WRONG_YOUTUBE_CHANNEL`: stop promotion, do not claim success, and preserve the video ID for an explicit recovery decision.
- After saving metadata, reopen Studio and the watch page and read back `episode_title` against its full recorded value before any publication. Verify `thumbnail_headline` separately on the rendered custom thumbnail.

## Visibility

- Initial state: Unlisted.
- Thumbnail approval does not authorize upload or publication.
- Public only with explicit complete-release authorization for the exact episode, video ID, canonical title, approved thumbnail SHA-256, and listed website surfaces.
- Never Schedule or Premiere without separate authorization.
- Before changing Public state, preflight access, current state, asset targets, cache/build behavior, verification route, and safe rollback for every required surface.
- Stop before public change if the YouTube channel grid/watch page or canonical website homepage/archive/episode surfaces cannot all be updated and verified.
- After status change, save and verify in Studio, the public channel grid, and the public watch page.
- Recheck visibility outside the edit dialog and authenticated Studio session.
- Inventory duplicate episode uploads after publication and keep superseded copies Unlisted.

## Complete release reconciliation

- YouTube custom thumbnail matches the approved asset.
- YouTube Studio, channel grid, and watch page all show the same intended display name, handle, and channel ID recorded in the release manifest.
- YouTube public channel grid shows the exact canonical title and approved thumbnail.
- YouTube public watch page shows the exact canonical title, approved thumbnail, Public playback, and expected video ID.
- Canonical `weeklyclaw.ai` homepage shows the exact canonical title, approved thumbnail, and correct public watch URL.
- Canonical archive shows the exact canonical title, approved thumbnail, and correct public watch URL.
- Canonical episode page shows the exact canonical title, approved thumbnail, and correct public watch URL.
- Title matches character-for-character across Studio, channel grid, watch page, homepage, archive, episode page, and release manifest.
- Record URL, observed title, thumbnail proof, status, verifier, and verification time for every surface.
- If any post-change check fails, mark `PARTIAL_RELEASE_BLOCKED`, stop promotion, and execute the pre-approved safe rollback where possible.
- Declare `PUBLIC_VERIFIED` only when every row passes.
