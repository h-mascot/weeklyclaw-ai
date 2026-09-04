# WeeklyClaw approval-to-publication runbook

Use when Henry (`855505513`) or Andy (`7615999206`) approves a lineup, requests canonical promotion, or says to publish.

## Authority

- Either host may approve/reselect lineup, trigger root promotion, and authorize WeeklyClaw website publication.
- Treat this as durable role authority, not an episode-specific exception.
- Other senders cannot approve or promote.

## Completion sequence

1. Read current approval state, selected revision, validation receipts, and asset manifest.
2. Record approver identity and exact instruction.
3. Back up pre-existing canonical root artifacts.
4. Promote approved agenda, deck, host notes, cheat sheet, media manifest, and every deck-relative local asset.
5. Recompute canonical hashes and mark promotion complete.
6. If instruction includes `publish`, run canonical website sync/deploy, then publish the finished episode across YouTube, native X video, and Bilibili using `multi-platform-episode-publication.md`. Do not stop after state mutation, root promotion, website deployment, or YouTube-only publication.
7. Verify live result:
   - homepage/episode index contains current episode canary;
   - direct deck URL returns success and contains title, stable slide anchor, and expected asset references;
   - representative local images/videos return success with correct content types;
   - deployed deck identity matches promoted candidate by hash where byte-for-byte retrieval permits it;
   - YouTube, X, and Bilibili each expose a public URL with matching episode title/account and playable full video;
   - X main post is native video from `@weeklyclaw`, has no external URL, and its deduplicated reply chain contains YouTube, Bilibili, then slides;
   - downstream Discord/community announcement contains all four links: YouTube, X, Bilibili, and slides.
8. Append authority, promoted files, hashes, deployment identity, three platform URLs/IDs, account-identity receipts, source fingerprint, downstream announcement receipts, checks, and gaps to state/run log.
9. Return direct openable YouTube, X, Bilibili, deck, and episode links. Keep response terse.

## Publication asset closure

Static-site sync scripts often stage only agenda/deck defaults. Before push, inspect all relative `src`, poster, QR, sponsor, image, and video references. Add their containing paths to the site's public/staged path allowlist. Validate at least one URL from each material media class.

## Failure semantics

- Deploy command success without content canaries is unverified.
- Live deck with missing local media is failed publication.
- Approval state `APPROVED` without requested publication is partial progress.
- If one scraper/browser backend is unavailable, use direct HTTP status/content checks or another browser path; record evidence, not a durable negative claim about the failed tool.