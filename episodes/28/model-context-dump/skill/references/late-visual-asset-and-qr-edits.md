# Late visual assets and QR CTA edits

Use this procedure for post-freeze sponsor logos, social links, QR codes, and other small visual corrections to an already-live WeeklyClaw deck.

## Preserve concurrent work

1. Re-read canonical deck and generator output immediately before editing. Late show-prep work may be concurrent.
2. Compare bytes and inspect the diff. Never copy a stale generator file over a newer canonical deck merely to restore parity.
3. Identify the authoritative candidate from the latest validated changes, apply the bounded edit there, then synchronize in the authoritative direction.
4. Copy every newly referenced local asset into both trees. Resolve all local `img`, `source`, and poster paths from each tree before claiming parity.
5. Record the new candidate hash and append a bounded runlog entry naming the edit, authority direction, validation, and approval source.

## Sponsor logo rules

- Source marks from the sponsor's official website or official brand kit.
- Preserve aspect ratio. Use `object-fit: contain`; never stretch or crop a wordmark.
- Keep a readable text label when a compact icon alone may be ambiguous.
- Capture the title placement and each dedicated sponsor slide from the exact live candidate at 1600 × 900.

## QR CTA rules

- Encode the exact user-supplied HTTPS URL with high error correction and a standard quiet zone.
- Use a plain high-contrast QR image. Put branding, border, shadow, and CTA copy outside the code matrix.
- Pair it with a human-readable fallback URL and make the containing card clickable to the same destination.
- Keep the rendered QR large enough for presentation capture. Treat source-image dimensions as irrelevant unless the rendered CSS size is also recorded.

## Required QR proof

1. Decode the generated source asset and assert exact URL equality.
2. Render the exact live deck at 1600×900 and navigate through normal deck controls to the target slide.
3. Confirm the image loaded, record intrinsic and rendered dimensions, and capture the full slide.
4. Decode the QR from that rendered slide screenshot. This is the decisive scanability proof.
5. Visually inspect spacing, clipping, overlap, label clarity, and hierarchy.
6. Fetch the live deck and QR asset with cache bypass. Require HTTP 200 and byte equality between the live deck and local candidate.
7. Recompute receipts only after the final edit. If the candidate changes, recapture affected evidence.

### QR decode toolchain (verified Ep26 rev11, 2026-08-23)

- `cv2.QRCodeDetector` decodes the source PNG but FAILS on a browser-scaled QR inside a 1600×900 slide render (empty result at x2–x8 upscale, grayscale, and binarized variants). Do not conclude "QR unscannable" from cv2 alone.
- `pip install zxing-cpp` + `zxingcpp.read_barcodes(full_render)` decodes the QR from the FULL unmodified 1600×900 screenshot — no crop, no upscale. Use zxing-cpp as the primary decoder; cv2 only as fallback.
- Snap Chromium on this host cannot write `--screenshot` output under `/tmp` (AppArmor "Failed to write file" despite exit 0). Write QA screenshots under `$HOME`. The dbus/AppArmor stderr lines are noise.
- Verify the img actually loaded via DOM before trusting any render evidence: inject a script reading `img.naturalWidth` (0 = broken src; a fixed-size CSS box still reserves layout, so the slide "looks" fine). QA renders must run from inside `revs/` where the `assets/` symlink resolves; an HTML copy placed elsewhere silently breaks every relative asset.
- **Vision-model reads of slide renders can hallucinate.** During Ep26 QA the vision tool confidently described a "Discord QR card with link" in a render whose image had `naturalWidth: 0` — no QR pixels existed. DOM load-state checks and programmatic decode are the proof; vision is for layout/clipping inspection only, never for "the QR is there and correct."

## Pitfalls

- A QR that decodes from its source PNG may still fail after browser scaling or slide capture.
- Matching deck filenames do not prove canonical/generator parity.
- Blindly synchronizing from the generator can destroy concurrent canonical edits.
- A clickable card does not prove the printed or streamed QR scans; test both paths.
- **CSS present is not element present.** Ep26 rev1–rev10 inherited the `.discord-qr` CSS rules from the authority deck while dropping the `<a class="discord-qr">` element itself — a class-name grep found 4 hits (all in `<style>`), so a text-grep "verification" passed while the live slide had no QR at all. Gate on the element pattern (`<a class="discord-qr"` + child `<img src>`), never the bare class name. `validate_deck.py` check 5b enforces this; apply the same element-level pattern to any future social/CTA element check.
