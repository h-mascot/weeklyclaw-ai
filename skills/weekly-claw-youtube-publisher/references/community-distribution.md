# Community distribution

Distribution is a post-publication phase owned by the existing authorized release owner. Do not create duplicate schedulers or override current pause and ownership directives. Verify the exact approved YouTube ID, channel, and matching public website release before proceeding. Human gates for one destination do not block independently authorized work elsewhere.

Read the release manifest, private destination ledger, current rules, delivery state and recent messages before each send. Resolve the current actor, destination, permissions, topic fit and approved content. Discovery is not permission. Do not join communities, accept terms, send DMs, or bypass access restrictions. Record skips and genuine permission gates. Do not mass-post automatically.

Use a verified, authorized transport supplied by the operator; inspect its behavior and exact episode selection first. Keep credentials, destination identifiers, state and private routing details outside this public bundle. On uncertain response inspect destination history before retrying. Record exact episode/master/YouTube-ID binding, sender, time, message ID and preview in the private release manifest. Retry only failed destinations with bounded backoff; never reset receipts or force duplicates.

## WhatsApp thumbnail gate — mandatory

For each authorized WhatsApp group, the delivered announcement must visibly include the exact release-approved episode thumbnail plus the canonical title and YouTube link. Use the approved thumbnail path/SHA-256 in the release manifest; never invent a cover, use a stale YouTube thumbnail, or request approval again for unchanged approved artwork.

1. Verify the exact account/group and check existing messages/receipts before composing. If the episode was already sent, preserve its message ID; a missing preview is not permission to resend or delete it. Record `SENT_THUMBNAIL_MISSING` or `SENT_THUMBNAIL_UNVERIFIED`, not full delivery PASS. Repair existing posts only within an explicit correction request.
2. Prefer a native link preview using the canonical watch URL. Verify the composer shows the correct episode artwork before sending through the authenticated Codex browser. For a transport that exposes preview metadata, inspect its documented capability first; the existing bridge has a `/send-preview` path with thumbnail data, but its availability and rendered result must be verified, not inferred from a success response. Do not assume generic Beeper text sends create previews.
3. If a correct link preview cannot be prepared, use the exact approved thumbnail as a PHOTO attachment with the approved title, blank line and single YouTube watch URL in its caption. This image-plus-caption fallback is part of future authorized WhatsApp episode distribution; it is not a second announcement or an attachment sent after a text-only post. Inspect the image composer before sending. Use a verified media-capable route; never invent API fields or substitute a document attachment. If neither preview nor photo composition is available, stop before sending with `WHATSAPP_THUMBNAIL_DELIVERY_BLOCKED`.
4. After one send, inspect that exact message in the destination WhatsApp conversation and confirm visible correct artwork, readable caption/title, exact video link and sender. Record message ID, mode (`LINK_PREVIEW` or `PHOTO_CAPTION`), approved thumbnail SHA-256, and narrowly scoped visual evidence in the release manifest. A text receipt, local image or HTTP success is insufficient. If artwork is absent/unobservable, retain the sent receipt and visual-failure status; never automatically retry the send. Verify each group separately.

Visual proof covers the inspected WhatsApp client, not a guarantee about every recipient's settings or client. Never claim an actual thumbnail repair from a skill edit alone.

## Message and routing

Use the approved episode title, blank line and a single canonical YouTube watch URL unless the destination requires a separately approved format. Check current rules and topic fit, disclose affiliation as required, and stop for organizer approval when required. WhatsApp requires the visual gate above; other platforms need their own preview checks. Preserve the existing private destination ledger as the source for route and permission evidence.
