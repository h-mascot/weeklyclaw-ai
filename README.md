# WeeklyClaw.ai

Official landing page for **The Weekly Claw**, OpenClaw's weekly community show.

## Local check

```bash
npm run build
python3 -m http.server 4173
```

The site is static HTML. Episode decks and agenda notes live under `episodes/`.

## Deployment

Production is hosted on Vercel and connected to this GitHub repo. Pushes to `main` auto-deploy to production; pull requests should receive preview deployments once Vercel Git integration is active.
