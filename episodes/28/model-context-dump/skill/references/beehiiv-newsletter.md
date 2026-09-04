# WeeklyClaw Beehiiv newsletter (Monday edition)

As of 2026-08-20. Henry wants the acquired Beehiiv list resumed: **Monday send, previous week's episode content as a written roundup + the video of the week** (fresh YouTube episode link).

## Publication facts (verified 2026-08-20)

- Publication: `https://weeklyclaw.beehiiv.com/` (~2k subscribers, acquired from Jordy bundle with @weeklyclaw X handle + domain).
- Signup form already live on weeklyclaw.ai: POSTs to `https://weeklyclaw.beehiiv.com/create` (see beeper skill's `weeklyclaw-beehiiv-website-handoff.md` reference for full form shape).
- Archive page returns 404 → list is dormant, zero posts sent since acquisition. First edition covers Episode 25.
- Jordy's last handover note: "you now have X, Beehiiv, email — just need to configure sending domain." Sending-domain configuration was never confirmed. **Before the first send, verify the sending domain is configured; a generic beehiiv-domain send to 2k people looks cheap — surface to Henry if unconfigured.**

## Credential location

- The Beehiiv API key from the handover was stored in **Vaultwarden** on 2026-07-18 (SuperADA message, Beeper archive). It is NOT in `~/clawd/secrets/`.
- Automated retrieval requires the vault unlocked (`bw`); if locked, ask Henry rather than hunting for the key elsewhere.
- Beehiiv API is server-side only; never put the key in client-side site code.

## Planned Monday pipeline (pending key + build)

1. Cron fires Monday morning UK after each Friday episode publication.
2. Pull that episode's approved agenda/talking points from `episodes/<N>/`, write compact written roundup.
3. Video of the week = fresh YouTube episode link.
4. Create as DRAFT in Beehiiv via API; post preview to the WeeklyClaw Telegram topic.
5. Henry APPROVE → schedule/send. First contact with a 2k dormant list is an external send: **always draft + approval, never auto-send.**

## Pitfalls

- The beeper skill (which holds the Beehiiv handoff references) is user-owned; do not edit it. Read its `references/weeklyclaw-beehiiv-website-handoff.md` and `weeklyclaw-beehiiv-readonly-investigation.md` for form fields, evidence-extraction, and secret-redaction rules.
- Do not treat the public asset UUID `26693d98-...` as the API `pub_...` publication id; the real publication id must come from the Beehiiv API once the key is available.
- "Beehiiv" and "beehive" are spelled interchangeably by Henry and Jordy — search both spellings in any Beeper/message evidence hunt.
