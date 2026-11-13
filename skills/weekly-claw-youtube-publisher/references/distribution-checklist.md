# X and Bilibili distribution checklist

Use the live platform UI and current official documentation as the authority. Platform limits change; record the observed limits and account entitlement in the release manifest for every episode.

## Shared idempotency and approval gate

- Resolve the exact master path/SHA-256, approved thumbnail path/SHA-256, captions, canonical title, episode number, and YouTube ID before any destination write.
- Search published inventory and unpublished drafts/media for the episode number, canonical lead, and any recorded remote ID. Resume a matching draft. Never upload a second copy merely because the first draft is hard to find.
- Record destination actor, master hash, remote draft/media ID, submitted title/copy revision, visibility, and verification URL/time.
- Stage only unpublished artifacts before complete-release approval. Treat X compose and Bilibili final submission as public actions.
- Require approval to enumerate the exact X copy/media and Bilibili title/draft ID along with the YouTube ID, canonical title, thumbnail SHA-256, and complete surface list.

## X

- Required actor: `@weeklyclaw`. Read the visible profile/account identity immediately before upload and again before Post. If another account is active, stop unless the exact required account is explicitly available for a safe switch; reverify after switching.
- Recheck [X longer-video limits](https://help.x.com/en/using-x/premium-longer-videos), [X Premium entitlements](https://help.x.com/en/using-x/x-premium), and [Media Studio specifications](https://help.x.com/en/using-x/media-studio-faqs). When official pages disagree, obey the stricter applicable limit and the live account UI.
- Use a versioned H.264/AAC X wrapper, leaving the canonical master unchanged: hold the exact approved thumbnail for approximately five seconds, then play the complete master from frame zero. Add no intro music unless separately approved. Record master, thumbnail, and wrapper SHA-256 values; verify card duration, full-frame legibility at desktop/mobile sizes, clean transition, complete runtime, streams, decode, and playback before upload. Use the wrapper hash for X duplicate/idempotency checks. No Premium/full-video entitlement means stop; do not silently create an excerpt.
- Keep copy concise and episode-specific. Verify character count locally and record the exact line breaks.
- Normal x.com compose publishes immediately. Do not attach/upload through compose before complete-release approval. When the verified account has Media Studio, an unpublished library upload may be staged and must record its media ID, processing state, metadata, subtitle, and custom-thumbnail state.
- Before Post, search `from:weeklyclaw` for the episode number, title lead, and distinctive copy phrase. After Post, verify the exact public URL, `@weeklyclaw`, text, media duration, audio/video playback, and absence of accidental replies or duplicate posts.
- Do not route through Typefully unless explicitly requested and its credential can read the exact social set. Typefully limits are not evidence of native X entitlement.

## Bilibili

- Required actor: account name `Weeklyclaw`, expected account ID recorded in the release manifest. Verify both in Creator Center or the authenticated owner view before a file upload or final submission. A login page is a blocker, not permission to use another account.
- Search Creator Center published submissions and drafts for the episode number, canonical lead, submitted-title variant, and recorded draft ID. Resume the existing matching draft before uploading again.
- Prefer the full exact master and approved thumbnail. If the live form requires a conforming derivative, preserve the complete programme, create a versioned derivative, run media QA, and record both hashes and the platform reason; never substitute a clip or dub silently.
- Resolve the Bilibili submitted title from the same release-manifest-approved canonical title contract used for YouTube. Use the exact approved Chinese-first bilingual variant when one exists. Never treat the media filename or Bilibili auto-fill as title authority. Recheck the live title limit (the verified 2026-08-09 form enforced 80 characters); if condensation is required, preserve the canonical claim and record the approved variant. After upload begins, explicitly replace the title field, then read back the exact value and character count before submission.
- Apply the full description, 12-style chapter list, relevant English/Chinese tags, suitable technology category, creation declaration, captions when supported, and sponsorship/commercial disclosure. Do not claim original reporting beyond the episode's sourced discussion.
- A completed transfer (`上传完成`) is only a draft-state receipt. Record upload bytes, filename, draft state, and form readback before final submission.
- Stop at login, QR, CAPTCHA, real-name, bound-phone, or SMS verification. Never expose or guess codes. For a displayed send-from-bound-phone action, quote only the minimum required instruction privately to the user and wait; do not select `我已发送` until the user confirms the real action.
- After final submission, open the public BV as a viewer and independently compare the rendered title with the manifest-approved Bilibili submitted title before advancing to the next episode. Verify the BV/AV ID, public URL, account name/UID, thumbnail, duration, description/disclosures, processing/review status, and playable video. A correct filename, draft field, or Creator Center card is not public-title proof. If Bilibili keeps the submission under review, record `SUBMITTED_UNDER_REVIEW`; do not claim it is public.
