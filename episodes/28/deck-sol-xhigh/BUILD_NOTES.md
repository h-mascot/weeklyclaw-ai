# WeeklyClaw Episode 28 rebuild notes

## Result

- Rebuilt `deck.html` as an 11-slide Episode 28 deck using the approved Episode 23 authority.
- Preserved the baseline visible copy, external links, media references, story order, sponsors, facts, figures, dates, quotes, and model/company names.
- Copied `speaker-notes.rev3.md` to `speaker-notes.md` byte-for-byte for handoff.
- Kept asset references in the baseline `assets/...` form; `output/assets` is a relative symlink to `input/assets`, so the supplied validator resolves the original files without duplication.

## Composition changes

- Restored the authority heading scale and retained the authority CSS, logo SVG, and primary navigation script exactly.
- Gave each 2×2 news grid a consistent full-height frame, centered header stack, tighter rhythm, and more room for the dominant editorial images.
- Rebalanced the Sources appendix to six story/source groups per column, removing the baseline bottom clipping without shrinking the source text.
- Shifted the Signal From Outside split toward the video poster and vertically centered the visual card.
- Tightened the close-slide Discord CTA into a compact centered lockup with clearer spacing.
- Preserved the baseline wheel and touch navigation as a small secondary enhancement script while leaving the authority script unchanged.

## Validation evidence

- Supplied validator: PASS, all 14 checks.
- Structural order: 11 unique slide IDs in the requested order.
- Content audit: baseline and rebuilt decks have identical visible-text, `href`, and media-`src` multisets.
- Template audit: first `<style>`, first `<script>`, and hidden logo SVG match the authority byte-for-byte.
- Browser QA: 11/11 slides rendered at 1600×900 with zero viewport overflow, zero scroll overflow, and zero unloaded images. ArrowRight, Home, End, wheel, and swipe checks passed.

## Frozen-input observations

- The baseline title still says “Eight cards, two grids” even though rev3 contains 12 cards across three grids. This was preserved under the same-data rule.
- The supplied notes header still says `rev2` / `deck.rev2.html` and calls the close slide `s-watch`. The deck uses the required actual ID `s-close` plus `data-notes-id="s-watch"` solely for compatibility with the supplied validator’s unchanged-notes parity check.
- A naive dark-pixel density heuristic flags the image-heavy B and C grids because their banners are dark; DOM geometry and full-slide visual inspection show sparse copy and no clipping.

