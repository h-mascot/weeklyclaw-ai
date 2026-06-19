# WeeklyClaw.ai

Official landing page for **The Weekly Claw**, OpenClaw's weekly community show.

## Published Weekly Claw slide routes

SuperAda Weekly Claw changelog decks are mirrored into short WeeklyClaw.ai paths:

- `/w11/changelog/` and `/w11/`
- `/w12/changelog/` and `/w12/`
- `/w13/changelog/` and `/w13/`
- `/w14/changelog/` and `/w14/`
- `/w15/changelog/` and `/w15/`
- `/w16/changelog/` and `/w16/`
- `/w17/changelog/` and `/w17/`
- `/w18/changelog/` and `/w18/`

`/wN/` is a static redirect page to `/wN/changelog/`. Slide JPGs are copied beside each changelog deck so the archived HTML remains self-contained.

## Local check

```bash
npm run build
python3 -m http.server 4173
```

The site is static HTML. Episode decks and agenda notes live under `episodes/`. Changelog decks live under `w*/changelog/`.

## Deployment

Production is hosted on Vercel and connected to this GitHub repo. Pushes to `main` auto-deploy to production; pull requests should receive preview deployments once Vercel Git integration is active.

## Contributor workflow

Edit via pull requests or direct commits to `main` if you have write access. Vercel auto-deploys the Git-connected project.
