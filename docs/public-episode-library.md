# Public episode library operations

The public library is a deterministic projection of evidence that is already public. It does not publish source material, fetch credentials, scrape private notes, or run on a nightly schedule.

## Authoritative inputs

- `episodes.json` is the current public catalogue source. At the current snapshot it contains E20–E31 with the public title, date, canonical YouTube URL, video ID, and published summary topics.
- `episodes/index.html` is the public archive-card source for deck-only E10–E19 records. Those rows have `date: null`, an honest archive-label `dateLabel`, no video ID, and `publicationStatus: "unknown"`.
- `data/public-episode-supplements.json` records transcript status, public source URLs, caption language/type, SHA-256 hashes, evidence strings, and the current catalogue coverage boundary. Its archive rows and metadata are public-safe because the site output directory serves this tree.
- `data/public-transcripts/eN.txt` contains only public YouTube transcript exports. Each published entry must bind to the exact canonical video ID and source URL declared in the manifest.

Recording-only references such as E4, E7, and E9 are coverage limitations, not public episode pages. E32 is absent from the current source snapshot because it is not a verified released catalogue row; a future verified catalogue record follows the same normal addition workflow.

## Adding a released episode

1. Add one public catalogue row to `episodes.json` with the canonical public URL and exact video ID. A new row without a transcript defaults to `transcript.status: "missing"`.
2. For a public transcript, copy the approved YouTube export to `data/public-transcripts/eN.txt` and add a manifest record with `status: "published"`, the exact `sourceUrl`, SHA-256 `sourceHash`, language, caption type, evidence, and any validated speaker labels. Do not use an agenda, speaker notes, Riverside recording, draft captions, or a live replay as a full transcript.
3. Run `npm run build`. The builder rejects a transcript whose header video ID, source URL, or content hash does not match the catalogue and manifest. If a catalogue row declares `status`, it must be `published` or `archived`; if it declares a visibility field, it must be `public`. Draft, private, scheduled, pending, unpublished, ready, and other nonpublic rows are excluded before normalization. Omitted legacy status/visibility fields remain supported for verified archive rows.
4. Run the focused tests and inspect the generated record. The build creates the episode detail page, timeline entry, and search corpus from `public-episodes.json`; it does not publish the video or update external platforms.

## Coverage and transcript limits

`coverage.transcriptPublished` contains only episodes with a verified public export and parsed timestamped segments. `coverage.transcriptMissing` includes public catalogue or archive rows for which no approved transcript source is available. Missing coverage is explicit; the builder does not infer a transcript from a title, deck, agenda, or recording date.

Transcript segments preserve supplied cue starts. The source exports do not provide verified cue ends, so `endSeconds` remains `null`. Segment IDs use the episode and timestamp with a same-timestamp disambiguator. E31 additionally has a public-safe speaker annotation bound to its exact video ID, caption hash, cue IDs, and cue text hashes. It maps only normalized caption text corroborated by both named Riverside transcript sources after the verified four-second opening trim; short generic replies, overlap, embedded video audio, and unresolved reconnect cues remain unlabeled. The annotation contains names and hashes only, never recording text or local source paths. Future speaker enrichment needs the same source-bound review and must fail closed on video, source-hash, cue, or text mismatch. No speaker is inferred from ordinary caption prose.

Caption provenance is retained in each transcript: `language`, `captionType`, `sourceHash`, and `possibleCaptionErrors`. Auto-generated captions remain searchable but are labelled as such and may contain recognition errors. Public caption exports are not human-edited transcripts.

## Clips

The versioned schema and renderer can display individually verified, publicly published clip records when they are present. The current builder imports no clips and emits an empty `clips` array for every episode. Adding clips requires an explicit ingestion change with public URL, episode evidence, and publication verification; local review renders, planned clips, source windows, and private media remain omitted. The current public clip count is zero.

## Build, test, and cleanup

```bash
npm run build
npm run test:public-library
node --test scripts/test-episode-search.mjs
```

`npm run build` rebuilds `public-episodes.json`, renders the public episode pages and `/timeline/`, then runs the existing static validation. The renderer removes stale `episodes/<week>/index.html` files only when they carry its `data-page="episode-library"` marker; source decks, agendas, and other authored files are preserved. It refreshes generated timeline, sitemap, homepage, and archive links for the current public corpus.

Because the static deployment output is the repository root, every served file under `data/` must remain public-safe. Do not place private research, credentials, cookies, local host paths, draft media, or operational review metadata in the supplement or transcript directories.

The existing publishing workflow remains responsible for legacy homepage/archive/RSS content and external release receipts. Use the established `scripts/sync-weeklyclaw-archive.py` workflow and its review steps when those surfaces need updating; the public-library build does not replace that sync and does not imply automatic or nightly publishing.
