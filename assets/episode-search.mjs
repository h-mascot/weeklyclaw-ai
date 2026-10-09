/**
 * Small, deterministic lexical retrieval for the public Weekly Claw corpus.
 *
 * This module deliberately has no network, model, or DOM dependency. A later
 * chat layer can use the returned citation fields as retrieval context without
 * inventing episode text or timestamps.
 */

export const MAX_QUERY_LENGTH = 160;
export const DEFAULT_RESULT_LIMIT = 20;
export const MAX_RESULT_LIMIT = 50;
export const DEFAULT_PASSAGES_PER_EPISODE = 3;
export const MAX_PASSAGES_PER_EPISODE = 3;

const WORD_RE = /\S+/gu;
const TOKEN_RE = /[\p{L}\p{N}]+/gu;
const PUBLIC_EPISODE_STATUSES = new Set(["published", "archived"]);
const PUBLIC_PUBLICATION_STATUSES = new Set(["published", "archived", "public_verified", "unknown"]);
const PRIVATE_STATES = new Set(["private", "draft", "planned", "ready", "unpublished", "local_review_only", "not_public"]);

/**
 * Normalize public search text while retaining a Unicode-friendly token
 * surface. NFKD removes accents for matching, and the explicit Open AI alias
 * keeps "Open AI" and "OpenAI" in the same lexical lane.
 */
export function normalizeSearchText(value) {
  if (typeof value !== "string") return "";
  return value
    .normalize("NFKD")
    .replace(/\p{M}/gu, "")
    .toLowerCase()
    .replace(/\bopen[\s-]+ai\b/gu, "openai")
    .replace(/\s+/gu, " ")
    .trim();
}

function tokenize(value) {
  return normalizeSearchText(value).match(TOKEN_RE) ?? [];
}

function cleanText(value) {
  return typeof value === "string" ? value.trim() : "";
}

function isPublicEpisode(episode) {
  if (!episode || episode.public === false || episode.isPublic === false || episode.sourcePublic === false || episode.publiclyAvailable === false) return false;
  // Legacy public catalogue rows omit status. If present, accept only an
  // explicitly released/archive state; prepared states are never searchable.
  if (episode.status !== undefined) {
    const status = String(episode.status).trim().toLowerCase();
    if (!PUBLIC_EPISODE_STATUSES.has(status)) return false;
  }
  if (episode.publicationStatus !== undefined) {
    const publicationStatus = String(episode.publicationStatus).trim().toLowerCase();
    if (!PUBLIC_PUBLICATION_STATUSES.has(publicationStatus)) return false;
  }
  for (const value of [episode.visibility, episode.sourceVisibility, episode.source_visibility]) {
    if (value === undefined || value === null) continue;
    const state = String(value).trim().toLowerCase();
    if (PRIVATE_STATES.has(state)) return false;
  }
  for (const value of [episode.visibility, episode.sourceVisibility, episode.source_visibility]) {
    if (value !== undefined && value !== null && String(value).trim().toLowerCase() !== "public") return false;
  }
  return true;
}

function toEpisodeIdentity(episode) {
  return {
    week: Number.isInteger(episode.week) ? episode.week : null,
    title: cleanText(episode.title),
    date: cleanText(episode.date),
    dateLabel: cleanText(episode.dateLabel),
    url: cleanText(episode.url),
    videoId: cleanText(episode.videoId),
  };
}

function isFiniteSeconds(value) {
  return typeof value === "number" && Number.isFinite(value) && value >= 0;
}

function optionalSegmentId(value) {
  return typeof value === "string" && value.trim() ? value.trim() : null;
}

function makeDocument({ episode, sourceType, text, sourceUrl, segment }) {
  const clean = cleanText(text);
  if (!clean) return null;
  const identity = toEpisodeIdentity(episode);
  return {
    identity,
    sourceType,
    sourceUrl: cleanText(sourceUrl) || identity.url || null,
    text: clean,
    titleTokens: tokenize(identity.title),
    bodyTokens: tokenize(clean),
    bodyTokenSet: new Set(tokenize(clean)),
    segmentId: segment ? optionalSegmentId(segment.id) : null,
    startSeconds: segment && isFiniteSeconds(segment.startSeconds) ? segment.startSeconds : null,
    endSeconds: segment && isFiniteSeconds(segment.endSeconds) ? segment.endSeconds : null,
  };
}

function buildDocuments(corpus) {
  const episodes = Array.isArray(corpus) ? corpus : corpus?.episodes;
  if (!Array.isArray(episodes)) return [];
  const documents = [];

  for (const episode of episodes) {
    if (!isPublicEpisode(episode)) continue;
    const identity = toEpisodeIdentity(episode);
    if (!identity.title) continue;

    // Keep title-only retrieval explicit. It is useful for finding an episode,
    // but must never masquerade as a matching transcript moment.
    const titleDocument = makeDocument({
      episode,
      sourceType: "episode",
      text: identity.title,
      sourceUrl: identity.url,
    });
    if (titleDocument) documents.push(titleDocument);

    if (Array.isArray(episode.summary)) {
      for (const summary of episode.summary) {
        const document = makeDocument({
          episode,
          sourceType: "summary",
          text: summary,
          sourceUrl: identity.url,
        });
        if (document) documents.push(document);
      }
    }

    // Only an explicitly published transcript can enter the public index.
    const transcript = episode.transcript;
    if (transcript?.status !== "published" || !Array.isArray(transcript.segments)) continue;
    for (const segment of transcript.segments) {
      const document = makeDocument({
        episode,
        sourceType: "transcript",
        text: segment?.text,
        sourceUrl: transcript.sourceUrl || identity.url,
        segment,
      });
      if (document) documents.push(document);
    }
  }
  return documents;
}

function boundedLimit(value) {
  if (!Number.isFinite(value)) return DEFAULT_RESULT_LIMIT;
  return Math.max(1, Math.min(MAX_RESULT_LIMIT, Math.trunc(value)));
}

function boundedPassagesPerEpisode(value) {
  if (!Number.isFinite(value)) return DEFAULT_PASSAGES_PER_EPISODE;
  return Math.max(1, Math.min(MAX_PASSAGES_PER_EPISODE, Math.trunc(value)));
}

function makeSnippet(text, queryTokens, maxChars = 280) {
  if (text.length <= maxChars) return text;
  const words = [...text.matchAll(WORD_RE)];
  const querySet = new Set(queryTokens);
  let hitIndex = words.findIndex((match) => tokenize(match[0]).some((token) => querySet.has(token)));
  if (hitIndex < 0) hitIndex = 0;
  let start = Math.max(0, hitIndex - 8);
  let end = Math.min(words.length, hitIndex + 17);
  while (start < end && words[end - 1][0].length + (words[end - 1].index - words[start].index) > maxChars) end -= 1;
  if (end <= start) end = Math.min(words.length, start + 1);
  const from = words[start].index;
  const last = words[end - 1];
  const to = last.index + last[0].length;
  return `${start > 0 ? "…" : ""}${text.slice(from, to)}${to < text.length ? "…" : ""}`;
}

function scoreDocument(document, queryTokens) {
  const titleCounts = new Map();
  for (const token of document.titleTokens) titleCounts.set(token, (titleCounts.get(token) || 0) + 1);
  const bodyCounts = new Map();
  for (const token of document.bodyTokens) bodyCounts.set(token, (bodyCounts.get(token) || 0) + 1);
  // Summary and transcript hits need evidence in their own source text. The
  // separate episode document above is the only place title-only matching is
  // allowed, so a title cannot create an unrelated timestamped transcript hit.
  const matched = document.sourceType === "episode"
    ? queryTokens.filter((token) => titleCounts.has(token))
    : queryTokens.filter((token) => document.bodyTokenSet.has(token));
  if (!matched.length) return null;
  const uniqueMatched = [...new Set(matched)];
  const titleHits = document.sourceType === "episode"
    ? uniqueMatched.reduce((total, token) => total + (titleCounts.get(token) || 0), 0)
    : 0;
  const bodyHits = uniqueMatched.reduce((total, token) => total + Math.min(bodyCounts.get(token) || 0, 3), 0);
  const phrase = normalizeSearchText(document.text).includes(normalizeSearchText(queryTokens.join(" ")));
  const score = document.sourceType === "episode"
    ? uniqueMatched.length * 10 + titleHits * 2
    : uniqueMatched.length * 20 + bodyHits * 4 + (phrase ? 6 : 0);
  return {
    score,
    matchedCount: uniqueMatched.length,
    titleHits,
    bodyHits,
  };
}

function compareRanked(a, b) {
  for (const field of ["score", "matchedCount", "titleHits", "bodyHits"]) {
    if (a.rank[field] !== b.rank[field]) return b.rank[field] - a.rank[field];
  }
  const aDate = a.document.identity.date;
  const bDate = b.document.identity.date;
  if (aDate !== bDate) return bDate.localeCompare(aDate);
  const aWeek = a.document.identity.week ?? -1;
  const bWeek = b.document.identity.week ?? -1;
  if (aWeek !== bWeek) return bWeek - aWeek;
  const sourceOrder = { summary: 0, transcript: 1, episode: 2 };
  if (a.document.sourceType !== b.document.sourceType) {
    return (sourceOrder[a.document.sourceType] ?? 9) - (sourceOrder[b.document.sourceType] ?? 9);
  }
  return a.order - b.order;
}

function toResult(document, rank, queryTokens) {
  return {
    episode: document.identity,
    sourceType: document.sourceType,
    sourceUrl: document.sourceUrl,
    snippet: makeSnippet(document.text, queryTokens),
    segmentId: document.segmentId,
    startSeconds: document.startSeconds,
    endSeconds: document.endSeconds,
    matchType: document.sourceType === "episode" ? "title" : "content",
    score: rank.score,
  };
}

/**
 * Build an immutable search handle. The handle can be reused by the UI and a
 * future citation-aware chat layer without reparsing the public corpus.
 */
export function createEpisodeSearch(corpus) {
  const documents = buildDocuments(corpus);
  return Object.freeze({
    search(query, options = {}) {
      return searchEpisodeIndex(documents, query, options);
    },
    searchGroups(query, options = {}) {
      return searchEpisodeGroupsIndex(documents, query, options);
    },
    size: documents.length,
  });
}

/** Search a corpus directly, or use createEpisodeSearch for repeated queries. */
export function searchEpisodes(corpus, query, options = {}) {
  return createEpisodeSearch(corpus).search(query, options);
}

/**
 * Return every matching episode, with at most three ranked passages per
 * episode. This is the UI-safe shape; unlike flat retrieval it cannot let a
 * long transcript crowd other matching episodes out of the result.
 */
export function searchEpisodeGroups(corpus, query, options = {}) {
  return createEpisodeSearch(corpus).searchGroups(query, options);
}

function prepareQuery(query) {
  const rawQuery = typeof query === "string" ? query.trim() : "";
  if (!rawQuery || rawQuery.length > MAX_QUERY_LENGTH) return null;
  const queryTokens = [...new Set(tokenize(rawQuery))];
  return queryTokens.length ? queryTokens : null;
}

function rankDocuments(documents, queryTokens) {
  const ranked = [];
  documents.forEach((document, order) => {
    const rank = scoreDocument(document, queryTokens);
    if (rank) ranked.push({ document, rank, order });
  });
  ranked.sort(compareRanked);
  return ranked;
}

function searchEpisodeIndex(documents, query, options = {}) {
  const queryTokens = prepareQuery(query);
  if (!queryTokens) return [];
  const ranked = rankDocuments(documents, queryTokens);
  return ranked.slice(0, boundedLimit(options.limit)).map(({ document, rank }) => toResult(document, rank, queryTokens));
}

function episodeKey(identity) {
  return Number.isInteger(identity.week)
    ? `week:${identity.week}`
    : `episode:${identity.url}\u0000${identity.date}\u0000${identity.title}`;
}

function searchEpisodeGroupsIndex(documents, query, options = {}) {
  const queryTokens = prepareQuery(query);
  if (!queryTokens) return [];
  const grouped = new Map();
  for (const ranked of rankDocuments(documents, queryTokens)) {
    const key = episodeKey(ranked.document.identity);
    const group = grouped.get(key) || {
      episode: ranked.document.identity,
      matches: [],
      best: ranked,
    };
    group.matches.push(ranked);
    grouped.set(key, group);
  }
  const passageLimit = boundedPassagesPerEpisode(options.passagesPerEpisode);
  return [...grouped.values()]
    .sort((a, b) => compareRanked(a.best, b.best))
    .map((group) => ({
      episode: group.episode,
      totalMatches: group.matches.length,
      titleMatch: group.matches.some(({ document }) => document.sourceType === "episode"),
      passages: group.matches
        .slice(0, passageLimit)
        .map(({ document, rank }) => toResult(document, rank, queryTokens)),
    }));
}
