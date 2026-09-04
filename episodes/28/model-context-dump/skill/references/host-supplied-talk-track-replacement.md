# Host-Supplied Talk-Track Replacement

Use when Henry or Andy says an existing WeeklyClaw segment is superseded and provides a replacement document, reply-linked attachment, or long-form script.

## Authority and recovery

1. Treat `disregard/replace/use this instead` as an explicit supersession boundary. The previous talk track becomes stale immediately and must not survive in current host-facing artifacts.
2. Treat reply text plus attachment as one instruction packet. If the attachment is not visible in the active message, recover the original message/asset using the reply-linked attachment recipe before declaring it missing.
3. Preserve the supplied document verbatim in `showprep/sources/<segment>.md`, alongside provenance: supplying host, Telegram topic/message when available, original filename, date, and hash.
4. Verify source metadata independently where possible: canonical URL, current platform title, channel/speaker, publication date, duration, chapters/timestamps, transcript, poster URL. Keep host editorial title distinct from platform title when they differ.

## Replacement closure

Update every current revision surface, not one convenient file:

- canonical source file;
- agenda and runtime;
- speaker notes;
- talking points;
- owning host view;
- host cheat sheet;
- slide-content source and final Sources slide;
- state/media metadata and asset provenance;
- local poster/fallback asset;
- append-only evidence/runlog.

If the supplied script is long, keep the complete script in the source file and put an explicit `read full canonical talk track` pointer plus opening, spine, landing, source, and runtime in derived host artifacts. Do not silently condense away the host's prose.

## Verification

1. Rebuild the deck from the canonical slide-content source.
2. Run the canonical deck validator against the prior approved authority deck.
3. Render every slide at 1600×900.
4. Visually inspect the changed slide for correct poster/title, clipping, overlap, and readability.
5. Search all current revision artifacts and rebuilt deck for the old video ID, old title/channel, stale runtime/date, and old poster provenance. Zero current-revision hits required.
6. Recompute hashes and update state/evidence only after final edits.
7. On a passing material rebuild, republish the standing-authorized WeeklyClaw website draft and verify live deck, agenda-draft, host-cheat-sheet, and representative asset URLs with decoded-content canaries. Approval is still required for canonical root promotion and final multi-platform episode publication.

## Delivery contract

Do not report only `replacement done` or worker status. Deliver:

- replacement source URL;
- where the full host script lives;
- artifacts updated;
- validator/render result;
- mobile-openable draft links after publication;
- explicit gaps or pending approval state.

A worker result sitting in a transcript is not delivered work. Surface the requested answer or link in the thread.