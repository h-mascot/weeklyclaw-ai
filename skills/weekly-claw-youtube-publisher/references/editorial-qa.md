# Editorial and master QA

Use this checklist before YouTube packaging.

## Candidate and participant coverage

- Resolve the exact episode and requested path.
- Inventory all plausible masters and mark superseded variants.
- Enumerate independent participant tracks before rendering.
- Require each usable participant in a focused scene and an all-present scene.
- Sample the opening, transitions, guest sections, referenced-source passages, known defects, and ending.

## Fact-check and source visuals

- Extract proper nouns, roles, attribution, dates, prices, benchmarks, statistics, and quotations from the matching transcript.
- Verify material claims against primary or authoritative sources.
- Preserve the source’s scope and qualifiers.
- Resolve tweets and reply chains to original status IDs.
- Show the source itself when practical; keep account, date, headline, author, and cited passage legible.
- Cover every repeated occurrence of an incorrect spoken claim.
- Add every visible source and correction to the YouTube description.

## Audio repair

- Encode the user’s exact interval in a failing regression before editing.
- Name the speaker to retain and speakers/noise to remove.
- Use speaker-targeted separation for overlapping human voices.
- Export original and repaired A/B samples for listening.
- Verify retained speech by transcript and listening.
- Compare waveform and loudness against the approved repair.
- Check crossfade boundaries for clicks, dropouts, or duplicated words.
- Never accept a self-declared cleanup flag as acoustic proof.

## Thumbnail

- Invoke and complete the saved `thumbnail-skill`; thumbnail work cannot be skipped.
- Ground the brief in the release-candidate footage/topic, complete participant list, verified references, brand assets, and most recently approved thumbnail.
- Include every on-screen podcast participant unless the user explicitly approves a different hierarchy.
- Verify Andy is the bald host and Henry wears glasses.
- Preserve native portrait proportions with cover/contain.
- AI layouts and treatments must not invent people, logos, claims, topics, or sponsors.
- Reject generated or altered real-person likenesses unless explicitly authorized and grounded in verified participant references.
- Require a reviewer other than the maker to inspect faces, spelling, labels, logo order, badge containment, participant coverage, adjacent-episode variation, and safe margins at 1280×720 and 160×90.
- Record itemised independent QA, candidate SHA-256, and exact user approval. Any change invalidates both QA and approval.

## Outro and delivery

- Use an exact 16:9 capture of the live `weeklyclaw.ai` hero.
- Verify the requested end-card duration and soundtrack overlap in the final render.
- Probe duration, dimensions, frame rate, codecs, color metadata, audio channels, and sample rate.
- Assert expected frame count or timestamp continuity when joining rendered segments.
- Run a complete decode with no errors.
- Review final frames and final audio, not only the build script. Measure final encoded AAC loudness/true peak and keep perceptual listening evidence separate from technical checks.
- Apply the master encode standard in `SKILL.md` to the exact candidate; record its average video bitrate and SHA-256.
- Run focused regressions for participant coverage, repaired intervals, source visuals, identity/aspect, and outro.

The release candidate is the exact immutable file that passes these checks.
