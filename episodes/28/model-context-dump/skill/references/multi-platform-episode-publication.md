# WeeklyClaw multi-platform episode publication

Use after Henry or Andy explicitly authorizes publishing a finished WeeklyClaw episode. Public completion means the full episode is published and verified on **YouTube, X, and Bilibili**, not YouTube alone.

## Platform owner and identity gates

- Run authenticated upload work on **Geordi**, which owns the browser sessions and large source file.
- YouTube: verify the authenticated channel is WeeklyClaw before upload or metadata writes.
- X: open the account menu and require visible identity evidence for `@weeklyclaw`. A menu reading `Log out @weeklyclaw` is sufficient session evidence. Profile tabs, browser-profile names, or another account in the switcher are not.
- Bilibili: require the WeeklyClaw creator account/session before upload.
- Stop at password, passkey, 2FA, SMS-send, or payment prompts. Henry handles secrets and sends verification messages. Resume only after he confirms the challenge step.

### Operable-session provenance gate

Account proof must come from the **exact browser instance the agent can operate for the write**, not from a screenshot, another device, another Chrome user-data directory, or a previous receipt.

1. Record target host, browser/profile or user-data directory, platform URL, visible account identity, and verification time immediately before each external write.
2. Treat Henry's statement or screenshot that an account is logged in as evidence that a usable session exists somewhere, not proof that the connected automation target owns it. Locate and verify that same session before publishing.
3. Cookie-domain presence, browser-profile labels, saved tabs, and account-switcher entries are discovery clues only. They do not prove the active account or a valid session.
4. If visible account identity differs from the required account, make no post/upload. Report both identities and the exact action needed: open or switch the required account in the operable target browser.
5. If Bilibili redirects to login, preserve any existing server/browser draft and stop at authentication. Do not duplicate the upload while trying alternate profiles.
6. After switching profiles or restoring auth, repeat visible identity proof. Never carry identity evidence from one browser instance into another.

## Release package

Use one canonical release package for all three platforms:

- final show-only video, scrubbed to remove pre-show, dead air, and overrun recording;
- final title, description, topic bullets, chapters/timestamps, tags, thumbnail, episode number, and publication date;
- source-file fingerprint, duration, dimensions, codec, and byte size;
- canonical slides/deck URL.

Record these in the episode release receipt before any public write. Platform-specific shortening or localization may change presentation, not facts, chapter order, episode identity, or source video.

## Two-phase workflow

### 1. Prepare

1. Inspect source duration and size before choosing upload route.
2. Stage metadata and thumbnail on all three platforms.
3. Confirm account identity on every platform.
4. Record blockers without discarding successful uploads. Resume idempotently rather than starting duplicate uploads.
5. Keep downstream Discord/link-thread distribution disabled until required public URLs exist.

### 2. Publish and verify

#### YouTube

- Upload full episode using the authenticated WeeklyClaw route.
- Apply canonical title, description, chapters, tags, and thumbnail.
- Verify public watch URL returns the expected episode title/channel and playable video.
- Record video ID and URL.

#### X

- Publish the **full native video** from the `@weeklyclaw` authenticated browser session.
- Do not use Typefully when video exceeds its supported upload envelope. Known WeeklyClaw limit observed in production: **10 minutes / 512 MB**. Inspect current artifact first; a 48:33 / 985 MB episode requires native X upload.
- Main post pattern:
  1. `POD UP` opening.
  2. Tight episode/topic summary plus chapters when they fit.
  3. Native video attached.
  4. No external URL in main post.
- Reply chain after main post is live:
  1. YouTube URL.
  2. Bilibili URL.
  3. WeeklyClaw slides/deck URL.
- Verify the post appears on `@weeklyclaw`, contains native video, and has a canonical status URL. Record post ID/URL.
- Enforce a single X writer. If native X publication owns the release, disable or deduplicate any Typefully/cron top-level post for the same episode.

#### Bilibili

- Upload the full episode; apply title, description, tags/category, thumbnail, and any required disclosure fields.
- Preserve completed upload/metadata state across verification challenges.
- If final publication requires SMS or account verification, report exact on-screen instruction with masked phone evidence. Henry sends the code/message; never handle his secret or claim publication before the confirmation completes.
- After confirmation, verify the public Bilibili video page shows the expected title/account and playable episode. Record BV/AV ID and URL.

## Completion and downstream distribution

Track per-platform states independently:

- `not_started`
- `uploading`
- `metadata_ready`
- `verification_required`
- `processing`
- `published_unverified`
- `verified`
- `blocked`

Release is **COMPLETE** only when YouTube, X, and Bilibili are all `verified`. Partial publication is valid progress, not completion.

After all three URLs verify:

1. Publish X reply chain in the required order, skipping any reply already present.
2. Publish Discord/community announcement containing YouTube, X, Bilibili, and slides links.
3. Update release receipt with URLs, IDs, timestamps, account identity receipts, source fingerprint, and verification evidence.
4. Re-read every public URL. Link presence alone is not proof; title/account/video identity must match.

If one platform remains blocked, keep retry state and report only the current human action. Do not create duplicate uploads, posts, replies, or announcements on retries.

## Failure rules

- YouTube live alone is not release completion.
- Upload progress or filled metadata is not publication.
- Publish-button success is not verification.
- Do not substitute a YouTube link post for full native X video unless Henry explicitly changes the distribution format.
- Do not compress or truncate the master solely to fit Typefully when native X supports the required full episode route.
- Never restart a large upload before checking whether the prior upload draft can resume.
- Never fire downstream distribution with placeholder or unverified URLs.
