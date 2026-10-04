import test from "node:test";
import assert from "node:assert/strict";

import {
  MAX_QUERY_LENGTH,
  createEpisodeSearch,
  normalizeSearchText,
  searchEpisodeGroups,
  searchEpisodes,
} from "../assets/episode-search.mjs";

const corpus = {
  schemaVersion: 1,
  episodes: [
    {
      week: 31,
      title: "OpenAI's verification gap",
      date: "2026-09-25",
      dateLabel: "25 September 2026",
      url: "https://weeklyclaw.ai/episodes/31",
      videoId: "w31video",
      summary: [
        "Open AI changes the cost and capability curve for practical coding work.",
        "Operators need a verification layer around autonomous systems.",
      ],
      transcript: {
        status: "published",
        sourceUrl: "https://weeklyclaw.ai/transcripts/31",
        segments: [
          { id: "w31-004", startSeconds: 42, endSeconds: 58, speaker: "Henry", text: "OpenAI is cheaper, but the verification gap still matters." },
          { id: "w31-005", text: "This segment has no supplied timestamp and must keep null." },
        ],
      },
    },
    {
      week: 30,
      title: "Café operators",
      date: "2026-09-18",
      url: "https://weeklyclaw.ai/episodes/30",
      videoId: "w30video",
      summary: ["A practical café workflow turns a narrow model into a useful tool."],
      transcript: { status: "missing", segments: [{ id: "private-1", text: "PRIVATE SHOULD NEVER BE INDEXED" }] },
    },
    {
      week: 29,
      title: "Unpublished internal episode",
      date: "2026-09-11",
      url: "https://weeklyclaw.ai/episodes/29",
      videoId: "w29video",
      summary: ["Public summary remains available."],
      transcript: { status: "private", sourceUrl: "https://private.invalid", segments: [{ id: "secret", text: "SECRET PRIVATE TRANSCRIPT" }] },
    },
    {
      week: 28,
      title: "OpenAI title-only episode",
      date: "2026-09-04",
      url: "https://weeklyclaw.ai/episodes/28",
      videoId: "w28video",
      summary: ["A summary with no matching title term."],
      transcript: {
        status: "published",
        sourceUrl: "https://weeklyclaw.ai/transcripts/28",
        segments: [{ id: "w28-unrelated", startSeconds: 77, text: "This unrelated segment must not be a title hit." }],
      },
    },
  ],
};

test("normalizes Unicode accents, case, and the Open AI alias", () => {
  assert.equal(normalizeSearchText("  OPEN-AI Café  "), "openai cafe");
  const results = searchEpisodes(corpus, "OPEN AI");
  assert.ok(results.length > 0);
  assert.equal(results[0].episode.week, 31);
});

test("returns truthful summary and published transcript citations", () => {
  const results = searchEpisodes(corpus, "verification");
  assert.equal(results[0].sourceType, "summary");
  assert.match(results[0].snippet, /verification/i);
  const transcript = searchEpisodes(corpus, "cheaper verification gap").find((result) => result.sourceType === "transcript");
  assert.ok(transcript);
  assert.equal(transcript.segmentId, "w31-004");
  assert.equal(transcript.startSeconds, 42);
  assert.equal(transcript.endSeconds, 58);
  const noTimestamp = searchEpisodes(corpus, "supplied timestamp")[0];
  assert.equal(noTimestamp.segmentId, "w31-005");
  assert.equal(noTimestamp.startSeconds, null);
});

test("never indexes missing/private transcripts or fabricates unmatched hits", () => {
  assert.deepEqual(searchEpisodes(corpus, "private-semaphore"), []);
  assert.deepEqual(searchEpisodes(corpus, "SECRET PRIVATE TRANSCRIPT"), []);
  assert.deepEqual(searchEpisodes(corpus, "qzxv-lunar"), []);
});

test("excludes prepared and nonpublic episode records before indexing", () => {
  const blockedStates = ["draft", "planned", "ready", "local_review_only"];
  const blocked = blockedStates.map((status, index) => ({
    week: 200 + index,
    status,
    title: `Prepared ${status}`,
    date: `2026-08-${String(index + 10).padStart(2, "0")}`,
    url: `https://weeklyclaw.ai/episodes/${200 + index}`,
    summary: [`BLOCKED_${status}_SUMMARY_MARKER`],
    transcript: {
      status: "published",
      sourceUrl: "https://private.invalid",
      segments: [{ id: `blocked-${status}`, startSeconds: 12, text: `BLOCKED_${status}_TRANSCRIPT_MARKER` }],
    },
  }));
  blocked.push({
    week: 204,
    title: "Not public visibility",
    date: "2026-08-14",
    url: "https://weeklyclaw.ai/episodes/204",
    visibility: "not_public",
    summary: ["BLOCKED_VISIBILITY_MARKER"],
  });
  blocked.push({
    week: 205,
    title: "Private flag",
    date: "2026-08-15",
    url: "https://weeklyclaw.ai/episodes/205",
    public: false,
    summary: ["BLOCKED_PUBLIC_FLAG_MARKER"],
  });
  for (const row of blocked) {
    const marker = row.summary[0];
    assert.deepEqual(searchEpisodes({ episodes: [row] }, marker), []);
  }
});

test("keeps validated legacy archive rows searchable when status is omitted", () => {
  const archive = {
    week: 9,
    title: "Archive-only public record",
    date: null,
    dateLabel: "Archive label · publication unknown",
    url: "https://weeklyclaw.ai/episodes/9",
    publicationStatus: "unknown",
    summary: ["UNIQUECORPUS"],
    transcript: { status: "missing", segments: [] },
  };
  const result = searchEpisodes({ episodes: [archive] }, "UNIQUECORPUS");
  assert.equal(result.length, 1);
  assert.equal(result[0].episode.week, 9);
  assert.equal(result[0].sourceType, "summary");
});

test("allows recognized publication states and rejects scheduled or unavailable records", () => {
  for (const publicationStatus of ["published", "archived", "public_verified", "unknown"]) {
    const row = {
      week: 300,
      title: "Recognized publication state",
      date: "2026-08-20",
      url: "https://weeklyclaw.ai/episodes/300",
      publicationStatus,
      summary: [`RECOGNIZEDSTATE_${publicationStatus}`],
    };
    assert.equal(searchEpisodes({ episodes: [row] }, `RECOGNIZEDSTATE_${publicationStatus}`).length, 1);
  }
  for (const publicationStatus of ["scheduled", "pending", "not_public"]) {
    const row = {
      week: 301,
      title: "Unreleased publication state",
      date: "2026-08-21",
      url: "https://weeklyclaw.ai/episodes/301",
      publicationStatus,
      summary: [`REJECTED_${publicationStatus}_TOKEN`],
    };
    assert.deepEqual(searchEpisodes({ episodes: [row] }, `REJECTED_${publicationStatus}_TOKEN`), []);
  }
  for (const field of ["sourcePublic", "publiclyAvailable"]) {
    const row = {
      week: 302,
      title: "Explicit unavailable flag",
      date: "2026-08-22",
      url: "https://weeklyclaw.ai/episodes/302",
      [field]: false,
      summary: [`REJECTED_${field}_TOKEN`],
    };
    assert.deepEqual(searchEpisodes({ episodes: [row] }, `REJECTED_${field}_TOKEN`), []);
  }
});

test("title-only matches are labelled without fabricating transcript moments", () => {
  const results = searchEpisodes(corpus, "OpenAI");
  const titleOnly = results.find((result) => result.episode.week === 28);
  assert.ok(titleOnly);
  assert.equal(titleOnly.sourceType, "episode");
  assert.equal(titleOnly.matchType, "title");
  assert.equal(titleOnly.segmentId, null);
  assert.equal(titleOnly.startSeconds, null);
  assert.equal(results.some((result) => result.episode.week === 28 && result.sourceType === "transcript"), false);
});

test("grouped retrieval covers every matching episode while capping passages per episode", () => {
  const longEpisode = {
    week: 100,
    title: "A long searchable episode",
    date: "2026-10-02",
    url: "https://weeklyclaw.ai/episodes/100",
    videoId: "w100video",
    summary: ["A long transcript for bounded retrieval tests."],
    transcript: {
      status: "published",
      sourceUrl: "https://weeklyclaw.ai/transcripts/100",
      segments: Array.from({ length: 100 }, (_, index) => ({
        id: `w100-${index + 1}`,
        startSeconds: index * 10,
        text: `Needle evidence passage ${index + 1}.`,
      })),
    },
  };
  const secondEpisode = {
    week: 101,
    title: "A second matching episode",
    date: "2026-10-03",
    url: "https://weeklyclaw.ai/episodes/101",
    videoId: "w101video",
    summary: ["A single needle summary match."],
    transcript: { status: "missing", segments: [] },
  };
  const groups = searchEpisodeGroups({ episodes: [longEpisode, secondEpisode] }, "needle");
  assert.equal(groups.length, 2);
  const longGroup = groups.find((group) => group.episode.week === 100);
  const secondGroup = groups.find((group) => group.episode.week === 101);
  assert.equal(longGroup.totalMatches, 100);
  assert.equal(longGroup.passages.length, 3);
  assert.equal(secondGroup.totalMatches, 1);
  assert.equal(secondGroup.passages.length, 1);
  assert.equal(secondGroup.passages[0].sourceType, "summary");
});

test("keeps deterministic ranking and bounded results", () => {
  const search = createEpisodeSearch(corpus);
  const first = search.search("operators", { limit: 100 });
  const second = search.search("operators", { limit: 100 });
  assert.deepEqual(first, second);
  assert.ok(first.length <= 50);
  assert.deepEqual(search.search("   "), []);
  assert.deepEqual(search.search("x".repeat(MAX_QUERY_LENGTH + 1)), []);
});
