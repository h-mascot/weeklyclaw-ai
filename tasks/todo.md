# Episode page multimedia player

- [x] Inspect episode archive architecture and deployment conventions.
- [x] Confirm Episode 22 YouTube video ID and available on-site audio sources.
- [x] Add validation for data-driven player wiring.
- [x] Implement responsive player below the episode archive hero.
- [x] Verify build, interaction, accessibility, and responsive layout.
- [x] Run Codex review and address accepted findings.
- [x] Commit and report status to the coordinator.

## Review

- Focused tests: `python3 -m unittest scripts/test_sync_weeklyclaw_archive.py` (7 passing).
- Static build validation: `npm run build` (passing).
- Browser proof: Episode 22 (`f2yugYwXOBo`) loaded through the privacy-enhanced YouTube embed with no autoplay; video/audio switching, archive episode switching, and responsive layouts at 320, 768, 1024, and 1440px verified.
- Audio source audit: no Episode 22 audio file or feed exists, so the Audio mode presents an honest unavailable state and is ready to use `data-audio-src` when one is published.
- Accepted review findings fixed: Video links restore Video mode, direct YouTube links remain as a no-JavaScript fallback, sync preserves video/audio media wiring both online and offline, active links expose current state, and an older playable episode is never mislabeled as latest.
- Final Codex review: `~/.codex/skills/codex-review/scripts/codex-review --parallel-tests "python3 -m unittest scripts/test_sync_weeklyclaw_archive.py && npm run build"` returned no accepted/actionable findings.
- Jeff Dean review: media identity remains owned by the existing archive sync pipeline; no duplicate episode metadata source was introduced.
- Luke W + Ryan Singer review: player sits immediately below the hero, keeps one obvious two-mode control, and remains usable without horizontal overflow on mobile.

# Episode 22 canonical title and approved artwork

- [x] Add a versioned Episode 22 thumbnail asset and persistent sync override
- [x] Make `The Sandbox Failed` canonical on homepage, archive, and episode surfaces
- [x] Add focused validation coverage
- [x] Run tests, static build, and Codex review
- [ ] Commit and push the production website change
- [ ] Verify live desktop and mobile title/artwork
