# WeeklyClaw.ai

Official landing page for **The Weekly Claw**, OpenClaw's weekly community show.

## Published Weekly Claw slide routes

Weekly Claw changelog decks are published into short WeeklyClaw.ai paths:

- `/changelog/` lists every changelog/DX deck.
- `/w11/changelog/` and `/w11/`
- `/w12/changelog/` and `/w12/`
- `/w13/changelog/` and `/w13/`
- `/w14/changelog/` and `/w14/`
- `/w15/changelog/` and `/w15/`
- `/w16/changelog/` and `/w16/`
- `/w17/changelog/` and `/w17/`
- `/w18/changelog/` and `/w18/`
- `/w19/changelog/` and `/w19/`

`/wN/` is a static redirect page to `/wN/changelog/`. Slide JPGs are copied beside each changelog deck so each route remains self-contained. The homepage presents clear **Episode deck** and **Changelog/DX deck** links on WeeklyClaw.ai without duplicate host-deck CTAs.


## Main slide routes

Recent Weekly Claw main show decks are hosted directly under WeeklyClaw.ai:

- `/episodes/10/deck.html`
- `/episodes/11/deck.html`
- `/episodes/12/deck.html`
- `/episodes/13/deck.html`
- `/episodes/14/deck.html`
- `/episodes/15/deck.html`
- `/episodes/18/deck.html`
- `/episodes/19/deck.html`
- `/episodes/20/deck.html` and `/episodes/20/agenda/`
- `/episodes/21/deck.html`, `/episodes/21/agenda/`, and `/episodes/21/host-cheat-sheet/`

Episode 19 also keeps an internal host cue deck at `/episodes/19/host.html`, but the public UI links to the main room deck and the changelog deck only. Episode 21 is the current latest episode packet.

## Local check

```bash
npm run build
python3 -m http.server 4173
```

The site is static HTML with one Vercel serverless function at `/api/feedback`. Episode decks and agenda notes live under `episodes/`. Changelog decks live under `w*/changelog/`.

## Feedback submissions

`/feedback` posts JSON to `/api/feedback`. The serverless function creates a private GitHub issue in `h-mascot/weeklyclaw-feedback` using these environment variables:

- `WEEKLYCLAW_GITHUB_TOKEN` — GitHub token with private repo issue-write access.
- `WEEKLYCLAW_FEEDBACK_REPO` — optional override; defaults to `h-mascot/weeklyclaw-feedback`.

## Deployment

Production is hosted on Vercel and connected to this GitHub repo. Pushes to `main` auto-deploy to production; pull requests should receive preview deployments once Vercel Git integration is active.

## Contributor workflow

Edit via pull requests or direct commits to `main` if you have write access. Vercel auto-deploys the Git-connected project.
