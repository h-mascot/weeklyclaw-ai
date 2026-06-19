# WeeklyClaw.ai

Official landing page for **The Weekly Claw**, OpenClaw's weekly community show.

## Published Weekly Claw slide routes

SuperAda Weekly Claw changelog decks are mirrored into short WeeklyClaw.ai paths:

- `/changelog/` lists every mirrored changelog deck.
- `/w11/changelog/` and `/w11/`
- `/w12/changelog/` and `/w12/`
- `/w13/changelog/` and `/w13/`
- `/w14/changelog/` and `/w14/`
- `/w15/changelog/` and `/w15/`
- `/w16/changelog/` and `/w16/`
- `/w17/changelog/` and `/w17/`
- `/w18/changelog/` and `/w18/`

`/wN/` is a static redirect page to `/wN/changelog/`. Slide JPGs are copied beside each changelog deck so the archived HTML remains self-contained. The homepage should not send Weekly Claw slide traffic back to SuperAda; it presents **Main slides** and **Changelog** links on WeeklyClaw.ai.


## Main slide routes

Recent MascotM3 main decks are hosted directly under WeeklyClaw.ai:

- `/episodes/10/deck.html`
- `/episodes/12/deck.html`
- `/episodes/13/deck.html`
- `/episodes/14/deck.html`
- `/episodes/15/deck.html`

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
