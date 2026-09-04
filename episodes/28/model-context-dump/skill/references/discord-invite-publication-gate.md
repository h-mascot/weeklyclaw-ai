# Discord invite publication gate

Recipe verified live 2026-08-21 on `~/.hermes/scripts/weeklyclaw-beeper-promo.py`,
after the same expired invite (`SPYQRuAdS`) was published to both Crustacean chats
on Aug 14 AND Aug 21 — the second time despite the Aug 16 SEV-2 postmortem.

## Why it recurred

The Aug 16 postmortem's fix landed as a NEW cron
(`weeklyclaw-discord-invite-rotation`, rotating `weeklyclaw.ai/discord` weekly)
but nobody rewired the EXISTING publishing script that still carried the invite
hardcoded. This is the same class as the "rule patched into SKILL.md does not
reach the job" trap: when a fix changes the canonical source of a link, grep
EVERY consumer of the old link — scripts, cron prompts in `jobs.json`, episode
artifacts, chat templates — not just the surface that reported the failure.

## The gate (fail closed)

At send time, resolve and validate; never trust a stored invite:

1. **Resolve canonical route without following redirects.**
   Python urllib follows redirects by default, which silently lands you on
   `discord.com/invite` and blows past the Location you need. Use a no-redirect
   opener:

   ```python
   class NoRedirect(urllib.request.HTTPRedirectHandler):
       def redirect_request(self, req, fp, code, msg, headers, newurl):
           return None

   OPENER = urllib.request.build_opener(NoRedirect)
   # HEAD https://weeklyclaw.ai/discord -> expect 307; read Location header
   # (the HTTPError raised for 3xx carries .code and .headers when the
   # no-redirect handler returns None — catch it, don't re-raise unless 2xx/4xx)
   ```

   Shell equivalent: `curl -sI https://weeklyclaw.ai/discord | grep -i '^location'`.

2. **Extract the code** from Location with `discord\.gg/([A-Za-z0-9-]+)`.

3. **Validate via the invite API, not the landing page.**
   `GET https://discord.com/api/v10/invites/<code>?with_expiration=true`
   - Landing-page HTTP 200 proves NOTHING — Discord serves the generic web
     shell for dead invites. This false validation caused the original SEV-2.
   - Require: HTTP 200, `guild.id == 1532061180569587975` (Weeklyclaw),
     `expires_at` present, remaining lifetime > 24h (publishing window).
   - Any miss = RuntimeError, no send, no fallback link. Dead link > wrong link.

4. **Discord's API 403s Python's default urllib User-Agent.** Send
   `User-Agent: weeklyclaw-promo-gate/1.0` (any custom string) on every request
   to both weeklyclaw.ai and discord.com.

5. **Assemble the message from the resolved URL at runtime.** Keep no invite
   literal in the script. Record the resolved `invite_code` in the run state
   receipt for audit.

## Event deep-link caveat

The canonical route loses `?event=<id>` (no event API hook to resolve it).
If the event deep-link matters, an authorized human must supply the event ID
weekly; never synthesize or reuse one from session history.

## Consumers to sweep when the invite source changes

- `~/.hermes/scripts/weeklyclaw-beeper-promo.py` (Beeper Discord promo)
- `weeklyclaw-discord-invite-rotation` cron prompt in `~/.hermes/cron/jobs.json`
- Website `vercel.json` `/discord` destination (owned by the rotation cron)
- Episode artifacts and social templates that embed `discord.gg/...` literals
- Verify with: `grep -rn "discord.gg/" ~/.hermes/scripts/ ~/weeklyclaw/ | grep -v output/`
