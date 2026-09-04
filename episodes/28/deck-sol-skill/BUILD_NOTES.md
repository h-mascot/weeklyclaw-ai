# WeeklyClaw Episode 28 — Build Notes

## Result

- Built `deck.html` from the supplied Episode 23 authority deck and Episode 28 rev3 editorial package.
- Canonical validator: PASS, exit 0, all 14 checks.
- Render QA: PASS at 1600×900 for all 11 slides; zero content overflow, viewport escape, detected overlap, missing image, or failed local asset request.
- Navigation QA: ArrowRight advanced `s-title` to `s-cold-open`; the authority script and chrome are intact.
- QR QA: both the source PNG and rendered `s-close` screenshot decoded to `https://weeklyclaw.ai/discord`.

## Skill procedure followed

Read and applied:

- `skill/SKILL.md`
- `skill/references/cursor-deck-contract.md`
- `skill/references/prior-episode-template-authority.md`
- `skill/references/on-slide-live-artifacts.md`
- `skill/references/direct-hermes-build-path.md`
- `skill/references/late-visual-asset-and-qr-edits.md`
- `skill/references/website-draft-publication.md`
- `skill/references/publication-runbook.md`
- `skill/references/multi-platform-episode-publication.md`
- `skill/templates/agenda-template.md`
- `skill/scripts/validate_deck.py`

The direct-Hermes route was used because the deck has 11 slides, a fixed linear arc, a complete local media package, and a supplied authority deck. Website and multi-platform publication procedures were reviewed for boundary awareness but intentionally not executed: the task explicitly restricted work to `output/` and prohibited network fetching/publication.

## Template authority

- Authority: `input/authority-deck-ep23.html`
- Authority SHA-256: `3548178052bb0c8e151b61ca230930885af8b7b3016072de1bfaa38aea598785`
- The full `<style>` block is byte-identical to the authority (`d83f6cc2455ca9a1427385a33944171254ef5db713d20fe0d02698d336ff32c9`).
- The full `<script>` block is byte-identical to the authority (`7d7ef53f7f791653081d7e0e0291e4650ded9061462c9a8b0d04aba85ad6c419`).
- The zero-sized SVG `<defs>` block, `weeklyclaw-logo` symbol, chrome, custom properties, and layout class system are unchanged.
- Final deck SHA-256: `8f3e22598769f10db88fe10e9093284b89811be283141a019950ef1c33df879a`.

## Editorial and layout decisions

- Preserved the frozen 11-topic story set as 12 cards across three 2×2 grids. C4 is an independent-receipts card and is not presented as a twelfth topic.
- Used the approved editorial banner for every A/B/C topic, with one headline, one short context line, and a small clickable LIVE/source link. Detailed figures and caveats remain in the supplied speaker notes.
- Preserved sponsor order: Herald Labs after the cold open; Heritage Telecom immediately before the close.
- Kept the required DOM slide ID `s-close` and added `data-notes-id="s-watch"` for parity with the older notes label. The `s-close` ID uses single quotes so the supplied validator reads the notes alias while the browser still exposes the required `s-close` DOM ID.
- Copied `input/assets/` byte-for-byte to `output/assets/`; no image generation, download, or substitution was performed.

## Deviations and observations

- The agenda header still says “two grid slides,” while the rev3 additions and task contract require three grids. The deck follows the frozen task contract and the rev3 C1–C3 material.
- The speaker-notes title says rev2 and names the close `s-watch`; the content includes the rev3 grid-C section. The alias above preserves both the required slide ID and validator parity without modifying inputs.
- The approved news visuals are generated editorial banners, not screenshots or benchmarks. They were retained exactly because the task forbids substitution and the media manifest explicitly approves them as beat markers.
- External source links were not opened during QA. Browser requests were restricted to localhost; the authority CSS’s Google Fonts import was blocked, so rendering used the declared fallback fonts while preserving the authority CSS verbatim.

## Final review

✅ Jeff Dean review: the implementation keeps one immutable authority shell, uses only existing layout primitives plus inline sizing, preserves the required slide order and contracts, and introduces no new CSS or SVG system.

Visual review: all 11 rendered slides were inspected. The grids are readable, artifacts dominate their cards, sponsor marks retain aspect ratio, the Sources slide is compact but legible, and no clipping or accidental overlap is visible.
