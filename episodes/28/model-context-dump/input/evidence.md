# Episode 28 build evidence

## Build identity

- **Episode:** 28
- **Show date:** Friday 2026-09-04, 4:00 PM ET / America-New_York
- **Tick:** `28-2026-09-03-12`
- **Build kind:** recovery-bootstrap-full-build; Thursday 11:00 BUILD was absent, so the 12:00 tick built from the active episode intake.
- **News window:** 2026-08-28 20:00 UTC through 2026-09-03 16:00 UTC.
- **Approval:** `UNVALIDATED`; root episode artifacts were not promoted.

## Template authority

- Prior APPROVED authority required by the active WeeklyClaw skill: `~/clawd/projects/weeklyclaw-ai/episodes/23/deck.html`
- Authority SHA-256: `3548178052bb0c8e151b61ca230930885af8b7b3016072de1bfaa38aea598785`
- Grid-format assembly reference: `~/weeklyclaw/episodes/27/showprep/revs/deck.rev6.html`
- Grid reference SHA-256: `19060492b959a454d886651559c6085c8b90e19ed2b55ac47f7fa656afb94275`
- Recent formal comparison copy: `~/weeklyclaw/episodes/27/showprep/qa/authority-deck-ep26.html`
- Recent formal comparison SHA-256: `7abef203065eebdf11ac9202ad558f16c4943398145db7df3e0210d8621ae4c7`
- The selected deck preserves the grid reference’s full CSS/SVG/chrome/script and was run through the canonical validator against both the documented Episode 23 authority and the Episode 26 grid authority. Both passed CSS custom-property parity, SVG symbol parity, core layout coverage, sponsor provenance, and size sanity.

## Candidate and research evidence

- Henry X archive: `sources/henry-tweets/all.jsonl`, 1,002 records; window contained 194 records, 108 originals and 86 retweets.
- Scoring rubric: consequence 25%, Henry/operator angle 20%, evidence 20%, novelty 15%, narrative 10%, clip-ability 10%.
- Selected set: A1 Nvidia/Hugging Face agreement, A2 Fable/Mythos 5.1, A3 OpenClaw 2.0, A4 Qwen3.8-Max-0902, B1 NYC moratorium, B2 Orbis 1.0, B3 ChatGPT teaser, B4 sentience sentiment.
- `story_set_hash`: `d5ce0c75ab19089994e5a96916e418720beea67bb8f5580a8b14ecb34318b38d`
- B4 is explicitly sentiment-only and first cut; B3 is explicitly teaser-only. Neither is presented as settled evidence.

## Material corrections made during build

1. **Nvidia/Hugging Face status:** initial inherited wording said “deal closed.” Web search and The Register receipt establish a signed definitive agreement expected to close in H1 2027 pending regulatory approvals and other closing conditions. All deck, agenda, notes, candidates, state, and source-ledger surfaces now say agreement/signing/expected close.
2. **The Register receipt:** initial URL returned 404. Resolved article URL is `https://www.theregister.com/ai-and-ml/2026/09/03/nvidia-buys-hugging-face-for-129b-promises-not-to-squeeze-too-hard/5294208`; direct title check returned 200 with the correct article title.
3. **Orbis receipt:** initial link was Henry’s retweet. Original Visko launch receipt is `https://x.com/viskoai/status/2094817592754291173`; direct title check confirms “Today, we are introducing Orbis 1.0...” and this URL is used across the package.
4. **Qwen visual:** the first `t-qwen-max` file was a misassigned Nvidia-regulator render. It was replaced with a fresh Qwen prompt, multimodal-checked, then copied into the stable artifact path.
5. **Image containers:** Gemini returned JPEG bytes under `.png` names. All eight banners were staged, PIL-verified, and normalized to real RGB PNG files at 1856x576 before deck QA.
6. **Teaser receipt:** malformed `2095531036293599499` was replaced with the verified official `https://x.com/ChatGPT/status/2095527989077557738`.

## Required artifact hashes

- `revs/agenda.rev1.md` — `b21eb12b86ceb9342e151682e5b037be1817555c33c36c51c2d1a485258d7b22`
- `revs/deck.rev1.html` — `68f0216faa0ca21a1246be270b2ce47330539440da6461bd66529b540b61105d`
- `revs/speaker-notes.rev1.md` — `8b673e727c22b0a717f0bd562f7f283eb35c88fb6ee465a5f9633ce15b49af1f`
- `revs/talking-points.rev1.md` — `618c20a7dfc5c7672451dd94eef603ab913d418099857fe68944dc2ab5ab4d08`
- `revs/henry-section.rev1.md` — `e6f39c6e1a3943067849a72b3e520ffbc1911c585ebf960c0356f3e28032de55`
- `revs/andy-section.rev1.md` — `ceb00049bb8dc84cef0b0fb8ae2ec7ef2873d3bd85c8b542e6ad885cb8de6e61`
- `revs/host-cheat-sheet.rev1.md` — `7ccddc75bd6d8ae08df4552259bb3428697ef439985e8e07e61eed4d7cc64927`
- `candidates.json` — `0bb90ff832a562d3ef60e192b37f7829e696ff1bad77cb5b19755a88a07e4e5d`
- `media-manifest.json` — `6d361e07da52984e6d59df8c26a2c08155e1bc6ef4f354b4a1c040e82a2b9603`
- `sources/ledger.md` — `f212ff362214538414636a013fda5e0dea24786fb26b8d0187de764baf6583e5`
- `sources/capture-manifest.json` — `f8caf626d708a1e71236fcd77fd7327bbe0b838189abfbd44a1d33e32d187d5c`

## Canonical validation

Command:

```text
python3 ~/.hermes/skills/operations/weeklyclaw-show-prep/scripts/validate_deck.py revs/deck.rev1.html revs/speaker-notes.rev1.md ~/clawd/projects/weeklyclaw-ai/episodes/23/deck.html
```

Result: **PASS**.

- 10 slides, exact speaker-notes parity.
- Inline JavaScript `node --check -`: PASS.
- No autoplay: PASS.
- 27 clickable source links: PASS.
- Final `s-sources`: PASS.
- Close QR points to `https://weeklyclaw.ai/discord`: PASS.
- 14 local media paths resolve: PASS.
- CSS custom properties, SVG symbol, core layout, sponsor provenance, and size gates: PASS.
- The same validator against the Episode 26 grid authority also returned **PASS**.

## Render and browser QA

- Runner: `qa/render_qa.py`, explicit deck and output arguments.
- Output: `qa/render-1600x900/rev1/`.
- Rendered slides: 10/10 at 1600x900.
- DOM result: **PASS**; zero viewport overflow, zero scroll overflow, zero detected overlaps, zero unloaded images, one active slide at a time.
- Grid result: both news slides have four children, two computed rows, and two computed columns.
- Multimodal contact-sheet inspection: no blank slides, clipping, overlap, broken images, unreadable layout, or wrong sponsor order. Sources slide was dense but organized for an appendix.
- Browser smoke test: `slideTotal=10`; ArrowRight moved `s-title` to `s-cold-open`; hash updated to `#s-cold-open`; End reached `s-sources`; Home returned to `s-title`.
- QR screenshot decode with OpenCV: `https://weeklyclaw.ai/discord`.
- Render receipt: `qa/render-1600x900/rev1/render-receipt.json`.

## Source URL QA

- Receipt: `qa/source-link-check.json`.
- 27 unique URLs inspected.
- 22 direct title/status checks passed; Anthropic system card returned HTTP 200 without a title tag and is marked primary-page pass; YouTube metadata was separately verified with yt-dlp.
- Direct rate-limit/blocked routes are recorded, not hidden: VentureBeat 429, DataCamp 403, Reuters 401, and YouTube direct HTML without a title tag. Their source roles have independent receipts in the ledger.

## Media QA

- Eight banners: PIL decode PASS, RGB PNG, 1856x576.
- Banner content: each has a per-image multimodal description in `media-manifest.json`; Qwen was rerolled after the misassignment was detected.
- Signal poster: PIL decode PASS, JPEG 1280x720; YouTube title/creator/public availability/duration 3,602 seconds verified by yt-dlp.
- Sponsors and QR: copied byte-for-byte from Episode 27; hashes in `media-manifest.json` match source assets.

## Draft publication

- Clean publication worktree: `/tmp/weeklyclaw-draft-publish-69VrGR`; removed after verification.
- `npm run build`: PASS. Pushed commit `489c0bae98a476e24375364fc87f90206a77a4c8` to `origin/main`.
- Staged scope: 20 explicit files under `episodes/28/`; no showprep, QA renders, gallery, homepage, or validator changes.
- Live deck: HTTP 200, 48,796 bytes, SHA-256 `68f0216faa0ca21a1246be270b2ce47330539440da6461bd66529b540b61105d`, exact local equality.
- Live agenda-draft: HTTP 200, exact local equality, SHA-256 `86e0e7c262031f05ce681e91e4290bc5793f553fe6a0ec2b9d0c8ff6e6f3167a`.
- Live host-cheat-sheet: HTTP 200, exact local equality, SHA-256 `d3173f2c7ea00c482907a8c42bef0a7bdab043a53a0072c105a395f83dbd5125`.
- All 13 unique referenced assets: HTTP 200 and byte/hash equal to clean-worktree sources.
- Sponsor order on all three public pages: Herald before Heritage. Offsets deck 21349/21530, agenda 4840/32310, host sheet 2153/2614.
- Receipt: `qa/live-draft-receipt.json`.

## Review-card delivery

- BUILD card sent to `telegram:-1004370723812:17` with `hermes send --file`; command returned `sent`.
- Card included deck, agenda-draft, host-cheat-sheet, exact review commands, and the Program Topics spreadsheet link.
- Hermes exposes no outgoing Telegram read operation on this host, so the receipt is explicitly a send ACK rather than fabricated recipient-side readback.

## Remaining human action

- Review the UNVALIDATED package and issue `APPROVE`, `SWAP <slot> <candidate>`, `DROP <slot>`, `PIN <candidate>`, `ORDER <n1,n2,n3,n4,n5>`, or free-text feedback.
- No root episode artifact promotion has occurred. The public draft is live, but editorial approval remains `UNVALIDATED`.
- Stale build lock was removed after verification; temporary worktree and branch were removed. Canonical website checkout remained at pre-existing local HEAD `3f58a73f87f07a00b849b9a069554aca9bb08a96`; remote `origin/main` is `489c0bae98a476e24375364fc87f90206a77a4c8`.

## 2026-09-03 19:25 UTC — rev2 breaking-news upgrade (Thursday 15:00 EDT REFRESH tick)

- Trigger: between the 14:00 EDT tick (18:00 UTC) and this tick, the @ChatGPT "stars" teaser resolved. OpenAI launched GPT-6 Astra on Thursday 2026-09-03 (~18:00–18:40 UTC press coverage; Axios published 18:00:19Z). Henry's X pulse flipped to launch amplification at 18:43–18:55 UTC (RT of Brockman-AGI breaking post, RT of Axios release post, original "Astra 🔥🔥🔥🔥").
- Source verification: Axios full text (web_extract, 19:08 UTC) + The New Stack full text (web_extract, 19:08 UTC) + TechCrunch title (direct curl, 19:20 UTC) + VentureBeat title (search index; Cloudflare-blocked to curl) + OpenAI "Path to Astra" (Jina, verified title) + Wikipedia rapid entry. Receipt ledger: sources/gpt6-astra-launch.md. Four slide URLs title-checked: TNS PASS, TechCrunch PASS, Axios 403->Jina title PASS, openai.com 403->Jina title PASS (qa/rev2-source-link-check.json).
- Editorial decision: in-place upgrade of already-selected B3 (teaser 8.5 -> launch 9.7), not a swap. Draft is UNVALIDATED; no approved/pinned story displaced. Grid slot, slide count, structure unchanged.
- Artifacts: rev2 written via revs/make_rev2.py (deck from Episode 27 rev6 grid template, content-only) + revs/make_rev2_md.py + revs/make_rev2_pass2.py (derived views). New banner assets/images/artifacts/t-gpt6-astra.png (Gemini 3 Pro Image, prompt tmp/imagegen/t-gpt6-astra.txt; normalized 1856x576 RGB PNG 1,168,885 bytes; tesseract OCR empty = no stray text; luminance stats consistent with dark editorial banner). media-manifest.json B3 entry replaced with supersedes note + revision_history.
- Stale-teaser sweep: CLEAN across all seven rev2 artifacts (no "stars are almost aligned", "cryptic teaser", "community inference", "teaser" framings remain).
- Canonical validator: PASS against Episode 23 authority (~/clawd/projects/weeklyclaw-ai/episodes/23/deck.html) AND Episode 26 grid authority (episodes/27/showprep/qa/authority-deck-ep26.html): 10 slides <-> notes parity, 26 source links, no autoplay, 14 local media resolved, theme/symbol/layout/sponsor gates PASS, deck 48,908 bytes.
- Render QA: qa/render_qa.py rev2 -> PASS 10/10 slides at 1600x900, zero bad slides. Grid-B active-slide check: all four card images naturalWidth 1856 (incl. t-gpt6-astra.png). Nav chrome present (slideTotal=10, navDots, .slide-container); ArrowRight advances. Close-slide QR decoded from render: https://weeklyclaw.ai/discord (cv2.QRCodeDetector).
- Runtime: grid B 7:30 -> 8:15 (B3 1:15 -> 2:00); total target still inside 34–38 min band; cut order updated (demo-reel detail first).
- Approval state stays UNVALIDATED. Hosts get the rev2 delta card in-topic.
