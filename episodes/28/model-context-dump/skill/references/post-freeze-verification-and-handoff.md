# Post-freeze verification and presenter handoff

Use this after a draft has been frozen but receives an independent fact-check, asset correction, or presenter complaint.

## Claim precision pass

1. Re-open every aired claim affected by the new evidence, not only the main agenda. Search agenda, deck, speaker notes, host sheets, candidate files, comparison tables, and source receipts.
2. Preserve distinctions hidden by shorthand:
   - Benchmark: separate official leaderboard score, organizer-verified public-set result, and vendor result from an alternative harness.
   - Security: do not imply a contemporaneous security product fixed or responded to an incident unless a primary source states that causal link.
   - Local-model hardware: scope claims to full official/unpruned weights versus pruned, distilled, or expert-reduced derivatives. Record memory footprint, measured speed, source ownership, and quality warnings separately.
   - Preliminary incident disclosures remain preliminary until the promised technical report appears.
3. Label vendor-reported measurements and custom-license/open-weight status precisely.
4. Search for superseded phrases after editing. Zero matches is part of validation.

## Canonical and generator synchronization

1. Compare canonical presenter files with generator output byte-for-byte before claiming they agree.
2. Determine which side is authoritative. Canonical may contain legitimate later fixes such as sponsor assets. Never blindly overwrite it from an older generator directory.
3. Copy in the authoritative direction, then copy every newly referenced local asset.
4. Recompute artifact and asset hashes in the receipt. Update state hashes and append the run log.
5. Re-run JSON parsing, JavaScript syntax, slide-ID parity, media resolution, no-autoplay, and receipt-hash checks.

## Clickable delivery

1. Serve the exact showprep root that makes deck-relative assets resolve.
2. Fetch the public URL independently and compare returned bytes with canonical deck and agenda hashes.
3. Test sponsor images and at least one local media URL separately.
4. Send direct clickable deck and agenda URLs, not local paths. Add a cache-busting query after a late correction.
5. Presenter legibility: browser `Ctrl +` / `Cmd +` should increase apparent text size without breaking slide navigation. Do not rebuild typography merely because browser zoom is available.

## Slowness triage during presentation prep

If the presenter reports lag, distinguish deck problems from host contention before editing the deck:

- Check load average and top CPU consumers on the presentation host.
- Check whether build/review agents are still active or merely idle/completed.
- Report concrete consumers and current utilization.
- Do not kill agents, indexers, renderers, or control-plane services without explicit approval.
- Avoid launching another heavyweight review while the presenter is actively using the machine.
