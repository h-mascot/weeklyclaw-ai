# Public episode retrieval contract

`assets/episode-search.mjs` is the shared lexical retrieval layer for the public Weekly Claw timeline. It has no network, model, or DOM dependency. The frontend can load the public corpus, create one search handle, and pass its results to a later citation-aware chat layer.

The corpus shape is versioned and public:

```json
{
  "schemaVersion": 1,
  "episodes": [{
    "week": 31,
    "title": "Episode title",
    "date": "2026-09-25",
    "dateLabel": "25 September 2026",
    "url": "https://weeklyclaw.ai/episodes/31",
    "videoId": "youtube-id",
    "summary": ["Published summary topic"],
    "deckUrl": "https://weeklyclaw.ai/episodes/31/deck.html",
    "transcript": {
      "status": "published",
      "sourceUrl": "https://weeklyclaw.ai/episodes/31/transcript",
      "segments": [{
        "id": "w31-004",
        "startSeconds": 42,
        "endSeconds": 58,
        "speaker": "Henry",
        "text": "Published transcript text"
      }]
    },
    "clips": [{"id": "clip-1", "title": "Clip", "url": "https://example.invalid", "platform": "youtube", "startSeconds": 42}]
  }]
}
```

`transcript.status` must be exactly `published` before any transcript segment is indexed. `missing`, `private`, `unpublished`, or malformed transcript rows are skipped. Segment IDs and timestamps are copied only when supplied as valid source data; missing values remain `null`. Summary rows use the episode URL as their citation source.

The public boundary is applied before summaries or transcripts are indexed. Legacy public rows may omit episode `status`; when supplied, it must be `published` or `archived`. Explicit `publicationStatus` must be `published`, `archived`, `public_verified`, or `unknown`; scheduled, pending, and other values are excluded. `draft`, `planned`, `ready`, `local_review_only`, private/nonpublic visibility, `public: false`, `isPublic: false`, `sourcePublic: false`, and `publiclyAvailable: false` rows are excluded. `publicationStatus: "unknown"` remains valid for verified public archive rows whose publication date is not established.

The public API is:

```js
import { createEpisodeSearch, searchEpisodeGroups, searchEpisodes } from "/assets/episode-search.mjs";

const search = createEpisodeSearch(corpus);
const results = search.search("Open AI verification", { limit: 10 });
const episodeGroups = search.searchGroups("Open AI verification");
// or: searchEpisodes(corpus, "Open AI verification", { limit: 10 })
// or: searchEpisodeGroups(corpus, "Open AI verification")
```

Each flat result has `{episode, sourceType, sourceUrl, snippet, segmentId, startSeconds, endSeconds, matchType, score}`. `sourceType` is `summary`, `transcript`, or `episode`. Summary/transcript results require a token match in their own source text. An `episode` result is a title-only match, has `matchType: "title"`, and always carries null segment/timestamp fields; it never claims that an unrelated transcript passage matched. `episode` carries the stable week/title/date/url/video identity. Snippets are bounded excerpts from the indexed source text.

`searchGroups` / `searchEpisodeGroups` is the UI-oriented shape:

```js
[{ episode, totalMatches, titleMatch, passages: [result, result, result] }]
```

It returns every matching episode, with at most three ranked passages per episode. A long transcript cannot crowd other matching episodes out of the timeline. `search` / `searchEpisodes` remains the flat, capped shape for a later RAG layer.

Results contain no generated answer and no hit for a query with no matching token. Ranking is lexical and deterministic. Empty queries return `[]`; the UI owns chronology for the empty-query timeline. Queries longer than 160 characters also return `[]`.

Matching is case-insensitive, accent-insensitive, Unicode-tokenized, and treats `Open AI` and `OpenAI` as the same term. Raw query strings are never compiled into regular expressions.

Run the focused tests with:

```bash
node --test scripts/test-episode-search.mjs
```
