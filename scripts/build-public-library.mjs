import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(process.env.PUBLIC_LIBRARY_ROOT || resolve(dirname(fileURLToPath(import.meta.url)), ".."));
const sourcePath = join(root, "episodes.json");
const supplementPath = join(root, "data", "public-episode-supplements.json");
const outputPath = join(root, "public-episodes.json");
const SOURCE_REVISION = "4966c04a46dc3df8bfee0cd4a03ac011ea55898b";
const PUBLIC_EPISODE_STATUSES = new Set(["published", "archived"]);
const PUBLIC_PUBLICATION_STATUSES = new Set(["published", "archived", "public_verified", "unknown"]);
const PRIVATE_STATES = new Set(["private", "draft", "planned", "unpublished", "local_review_only", "ready"]);

const readJson = (path) => JSON.parse(readFileSync(path, "utf8"));

function formatDate(date) {
  if (!date) return null;
  const parsed = new Date(`${date}T00:00:00Z`);
  if (Number.isNaN(parsed.getTime())) return null;
  return new Intl.DateTimeFormat("en-GB", {
    day: "numeric",
    month: "short",
    year: "numeric",
    timeZone: "UTC",
  }).format(parsed);
}

function parseTimestamp(value) {
  const parts = value.split(":").map(Number);
  if (parts.length === 2 && parts.every(Number.isInteger)) {
    const [minutes, seconds] = parts;
    if (minutes >= 0 && seconds >= 0 && seconds < 60) return minutes * 60 + seconds;
  }
  if (parts.length === 3 && parts.every(Number.isInteger)) {
    const [hours, minutes, seconds] = parts;
    if (hours >= 0 && minutes >= 0 && minutes < 60 && seconds >= 0 && seconds < 60) {
      return hours * 3600 + minutes * 60 + seconds;
    }
  }
  return null;
}

function videoIdFromUrl(value) {
  try {
    const url = new URL(value);
    if (url.hostname === "youtu.be") return url.pathname.slice(1);
    if (url.hostname === "youtube.com" || url.hostname === "www.youtube.com") return url.searchParams.get("v");
  } catch {}
  return null;
}

function parseTranscript(text, week, expectedVideoId, allowedSpeakers = []) {
  const header = text.split(/\r?\n/, 6).slice(0, 4).join("\n");
  const idMatch = header.match(/^Video ID:\s*(\S+)\s*$/m);
  if (!idMatch || idMatch[1] !== expectedVideoId) {
    throw new Error(`Transcript E${week} does not identify expected video ${expectedVideoId}`);
  }

  const segments = [];
  for (const line of text.split(/\r?\n/)) {
    const match = line.match(/^\[(\d{1,6}:\d{2}(?::\d{2})?)\]\s*(.*)$/);
    if (!match) continue;
    const startSeconds = parseTimestamp(match[1]);
    if (startSeconds === null) throw new Error(`Invalid timestamp in E${week}: ${match[1]}`);
    let transcriptText = match[2].replace(/\s+/g, " ").trim();
    let speaker = null;
    for (const candidate of [...allowedSpeakers].sort((a, b) => b.length - a.length)) {
      const prefix = `${candidate}:`;
      if (!transcriptText.startsWith(prefix)) continue;
      const remainder = transcriptText.slice(prefix.length).trim();
      if (!remainder) continue;
      speaker = candidate;
      transcriptText = remainder;
      break;
    }
    if (!transcriptText) continue;
    segments.push({ startSeconds, speaker, text: transcriptText });
  }
  if (!segments.length) throw new Error(`Transcript E${week} has no timestamped segments`);
  const timestampOccurrences = new Map();
  return segments.map((segment) => {
    const timestampKey = String(segment.startSeconds).padStart(5, "0");
    const occurrence = (timestampOccurrences.get(timestampKey) || 0) + 1;
    timestampOccurrences.set(timestampKey, occurrence);
    return {
    id: `e${week}-${timestampKey}-${String(occurrence).padStart(2, "0")}`,
    startSeconds: segment.startSeconds,
    // The export supplies cue starts only. Keep the end unclaimed rather than
    // presenting the next cue's start as a verified source boundary.
    endSeconds: null,
    speaker: segment.speaker,
    text: segment.text,
    };
  });
}

function transcriptMetadata(record) {
  return {
    language: typeof record.language === "string" ? record.language : null,
    captionType: typeof record.captionType === "string" ? record.captionType : null,
    sourceHash: typeof record.sourceHash === "string" ? record.sourceHash : null,
    possibleCaptionErrors: record.possibleCaptionErrors === true,
  };
}

const SPEAKER_ANNOTATION_KEYS = new Set([
  "schemaVersion",
  "week",
  "videoId",
  "captionSourceUrl",
  "captionSourceHash",
  "sourceTranscriptHash",
  "timebaseOffsetSeconds",
  "speakerSource",
  "speakers",
  "annotations",
]);
const SPEAKER_KEYS = new Set(["id", "displayName"]);
const SPEAKER_ANNOTATION_ENTRY_KEYS = new Set(["segmentId", "speakerId", "textHash"]);

function assertExactKeys(value, allowed, label) {
  for (const key of Object.keys(value || {})) {
    if (!allowed.has(key)) throw new Error(`${label} has unsupported field ${key}`);
  }
}

function readSpeakerAnnotations(record, week, expectedVideoId, transcriptSegments) {
  if (!record.speakerAnnotationPath) return new Map();
  if (record.status !== "published") throw new Error(`E${week} speaker annotations require a published transcript`);
  if (typeof record.speakerAnnotationPath !== "string") throw new Error(`E${week} speaker annotation path is invalid`);
  const annotationPath = resolve(root, record.speakerAnnotationPath);
  if (!annotationPath.startsWith(`${root}${"/"}`) || !existsSync(annotationPath)) {
    throw new Error(`Missing speaker annotation source for E${week}`);
  }
  const annotation = readJson(annotationPath);
  assertExactKeys(annotation, SPEAKER_ANNOTATION_KEYS, `E${week} speaker annotations`);
  if (annotation.schemaVersion !== 1) throw new Error(`E${week} speaker annotations have an unsupported schema version`);
  if (annotation.week !== week) throw new Error(`E${week} speaker annotations identify the wrong episode`);
  if (annotation.videoId !== expectedVideoId) throw new Error(`E${week} speaker annotations identify the wrong video`);
  if (annotation.captionSourceUrl !== record.sourceUrl) throw new Error(`E${week} speaker annotations identify the wrong caption URL`);
  if (annotation.captionSourceHash !== record.sourceHash) throw new Error(`E${week} speaker annotations do not match the caption source hash`);
  if (!/^[a-f0-9]{64}$/i.test(annotation.sourceTranscriptHash || "")) throw new Error(`E${week} speaker annotations have an invalid source hash`);
  if (!Number.isFinite(annotation.timebaseOffsetSeconds)) throw new Error(`E${week} speaker annotations have an invalid timebase offset`);
  if (typeof annotation.speakerSource !== "string" || !annotation.speakerSource.trim() || annotation.speakerSource.length > 200) {
    throw new Error(`E${week} speaker annotations have no safe source description`);
  }
  if (/[\\/]|(?:path|download|token|cookie|password|credential|secret)/iu.test(annotation.speakerSource)) {
    throw new Error(`E${week} speaker annotations have an unsafe source description`);
  }
  if (!Array.isArray(annotation.speakers) || !annotation.speakers.length) throw new Error(`E${week} speaker annotations have no speaker registry`);
  if (!Array.isArray(annotation.annotations)) throw new Error(`E${week} speaker annotations have no entries`);

  const speakers = new Map();
  for (const speaker of annotation.speakers) {
    assertExactKeys(speaker, SPEAKER_KEYS, `E${week} speaker registry entry`);
    if (!/^[a-z][a-z0-9_-]{0,31}$/.test(speaker.id || "")) throw new Error(`E${week} speaker annotation ID is invalid`);
    if (typeof speaker.displayName !== "string" || !/^[A-Za-z][A-Za-z0-9 .'-]{0,63}$/.test(speaker.displayName.trim())) {
      throw new Error(`E${week} speaker display name is invalid`);
    }
    if (speakers.has(speaker.id)) throw new Error(`E${week} speaker annotation IDs are duplicated`);
    speakers.set(speaker.id, speaker.displayName.trim());
  }

  const segmentsById = new Map(transcriptSegments.map((segment) => [segment.id, segment]));
  const annotated = new Map();
  for (const entry of annotation.annotations) {
    assertExactKeys(entry, SPEAKER_ANNOTATION_ENTRY_KEYS, `E${week} speaker annotation entry`);
    if (!segmentsById.has(entry.segmentId)) throw new Error(`E${week} speaker annotation references an unknown cue`);
    if (!speakers.has(entry.speakerId)) throw new Error(`E${week} speaker annotation references an unknown speaker`);
    if (!/^[a-f0-9]{64}$/i.test(entry.textHash || "")) throw new Error(`E${week} speaker annotation has an invalid cue text hash`);
    const segment = segmentsById.get(entry.segmentId);
    const expectedTextHash = createHash("sha256").update(segment.text).digest("hex");
    if (entry.textHash !== expectedTextHash) throw new Error(`E${week} speaker annotation cue text hash does not match`);
    if (annotated.has(entry.segmentId)) throw new Error(`E${week} speaker annotation cues are duplicated`);
    annotated.set(entry.segmentId, speakers.get(entry.speakerId));
  }
  return annotated;
}

function safeEvidence(record) {
  return Array.isArray(record?.evidence) ? record.evidence.filter((item) => typeof item === "string" && item.trim()).map((item) => item.trim()) : [];
}

function localDeckUrl(week) {
  return existsSync(join(root, "episodes", String(week), "deck.html")) ? `/episodes/${week}/deck` : null;
}

function isPublicCatalogueRecord(record) {
  if (!record || record.public === false || record.isPublic === false) return false;
  if (record.sourcePublic === false || record.publiclyAvailable === false) return false;
  if (record.status !== undefined && record.status !== null && !PUBLIC_EPISODE_STATUSES.has(String(record.status).trim().toLowerCase())) return false;
  if (record.publicationStatus !== undefined && record.publicationStatus !== null && !PUBLIC_PUBLICATION_STATUSES.has(String(record.publicationStatus).trim().toLowerCase())) return false;
  const states = [record.publicationStatus]
    .filter(Boolean)
    .map((value) => String(value).trim().toLowerCase());
  const visibilities = [record.visibility, record.sourceVisibility, record.source_visibility]
    .filter((value) => value !== undefined && value !== null)
    .map((value) => String(value).trim().toLowerCase());
  return !states.some((value) => PRIVATE_STATES.has(value)) && !visibilities.some((value) => value !== "public");
}

function normalizeCurrentEpisode(source, supplement, week) {
  if (!Number.isInteger(source.week) || source.week !== week) throw new Error(`Invalid episode week ${week}`);
  if (typeof source.title !== "string" || !source.title.trim()) throw new Error(`E${week} has no title`);
  const date = /^\d{4}-\d{2}-\d{2}$/.test(source.date || "") ? source.date : null;
  const videoId = /^[A-Za-z0-9_-]{11}$/.test(source.videoId || "") ? source.videoId : null;
  const url = typeof source.url === "string" && source.url.startsWith("https://") ? source.url : null;
  if (videoIdFromUrl(url) !== videoId) throw new Error(`E${week} catalogue URL does not match its video ID`);
  const record = supplement.transcripts[String(week)] || {
    status: "missing",
    sourceUrl: null,
    evidence: ["episodes.json"],
  };
  if (!["published", "missing"].includes(record.status)) throw new Error(`E${week} has invalid transcript status`);
  const metadata = transcriptMetadata(record);
  const evidence = safeEvidence(record);
  if (record.status === "published") {
    if (!videoId || !record.sourcePath || !record.sourceUrl) throw new Error(`E${week} published transcript is missing source metadata`);
    const transcriptPath = resolve(root, record.sourcePath);
    if (!transcriptPath.startsWith(`${root}${"/"}`) || !existsSync(transcriptPath)) throw new Error(`Missing transcript source for E${week}`);
    const transcriptText = readFileSync(transcriptPath, "utf8");
    const sourceHash = createHash("sha256").update(transcriptText).digest("hex");
    if (record.sourceHash !== sourceHash) throw new Error(`Transcript source hash does not match E${week}`);
    const transcriptSegments = parseTranscript(transcriptText, week, videoId, record.speakerLabels);
    const speakerAnnotations = readSpeakerAnnotations(record, week, videoId, transcriptSegments);
    for (const segment of transcriptSegments) {
      if (speakerAnnotations.has(segment.id)) segment.speaker = speakerAnnotations.get(segment.id);
    }
    if (record.sourceUrl !== url) throw new Error(`Transcript source URL does not match E${week}`);
    return {
      week,
      title: source.title.trim(),
      date,
      dateLabel: formatDate(date),
      url,
      videoId,
      summary: (Array.isArray(source.summary) ? source.summary : []).filter((item) => typeof item === "string" && item.trim()).map((item) => item.trim()),
      deckUrl: localDeckUrl(week),
      publicationStatus: "public_verified",
      publicationEvidence: evidence,
      transcript: { status: "published", sourceUrl: record.sourceUrl, ...metadata, segments: transcriptSegments },
      clips: [],
    };
  }
  return {
    week,
    title: source.title.trim(),
    date,
    dateLabel: formatDate(date),
    url,
    videoId,
    summary: (Array.isArray(source.summary) ? source.summary : []).filter((item) => typeof item === "string" && item.trim()).map((item) => item.trim()),
    deckUrl: localDeckUrl(week),
    publicationStatus: "public_verified",
    publicationEvidence: evidence,
    transcript: { status: "missing", sourceUrl: null, ...metadata, segments: [] },
    clips: [],
  };
}

function normalizeArchiveEpisode(record) {
  const week = Number(record?.week);
  if (!Number.isInteger(week) || week < 1) throw new Error("Archive episode has invalid week");
  if (typeof record.title !== "string" || !record.title.trim()) throw new Error(`Archive E${week} has no title`);
  const url = typeof record.url === "string" && record.url.startsWith("https://weeklyclaw.ai/") ? record.url : null;
  return {
    week,
    title: record.title.trim(),
    date: null,
    dateLabel: typeof record.dateLabel === "string" ? record.dateLabel : "Archive label · publication unknown",
    url,
    videoId: null,
    summary: (Array.isArray(record.summary) ? record.summary : []).filter((item) => typeof item === "string" && item.trim()).map((item) => item.trim()),
    deckUrl: typeof record.deckUrl === "string" ? record.deckUrl : null,
    publicationStatus: "unknown",
    publicationEvidence: safeEvidence(record),
    transcript: { status: "missing", sourceUrl: null, language: null, captionType: null, sourceHash: null, possibleCaptionErrors: false, segments: [] },
    clips: [],
  };
}

function assertPublicOutput(output) {
  const serialized = JSON.stringify(output);
  for (const forbidden of ["/Users/", "/private/", "/var/folders/", '"sourcePath"', '"downloadURL"', '"downloadUrl"', '"password"', '"cookie"']) {
    if (serialized.toLowerCase().includes(forbidden.toLowerCase())) throw new Error(`Forbidden private content in public output: ${forbidden}`);
  }
  const weeks = output.episodes.map((episode) => episode.week);
  if (new Set(weeks).size !== weeks.length) throw new Error("Public catalogue contains duplicate episode weeks");
}

const source = readJson(sourcePath);
const supplement = readJson(supplementPath);
if (supplement.sourceSnapshot.revision !== SOURCE_REVISION) throw new Error("Supplement source revision is not the verified catalogue snapshot");
const excludedWeeks = new Set(Object.keys(supplement.excludedWeeks || {}).map(Number));
const sourceEpisodes = (Array.isArray(source.episodes) ? source.episodes : []).filter((episode) => Number.isInteger(episode.week) && !excludedWeeks.has(episode.week) && isPublicCatalogueRecord(episode));
const currentWeeks = new Set(sourceEpisodes.map((episode) => episode.week));
const archiveEpisodes = (Array.isArray(supplement.archiveEpisodes) ? supplement.archiveEpisodes : []).filter((episode) => !excludedWeeks.has(Number(episode.week)) && !currentWeeks.has(Number(episode.week)) && isPublicCatalogueRecord(episode));
const episodes = [...sourceEpisodes.map((episode) => normalizeCurrentEpisode(episode, supplement, episode.week)), ...archiveEpisodes.map(normalizeArchiveEpisode)].sort((a, b) => a.week - b.week);
if (!episodes.length) throw new Error("No public catalogue episodes found");
const publishedEpisodes = episodes.filter((episode) => episode.transcript.status === "published").map((episode) => episode.week);
const missingEpisodes = episodes.filter((episode) => episode.transcript.status === "missing").map((episode) => episode.week);
const sourceSnapshot = {
  revision: String(supplement.sourceSnapshot.revision),
  catalogue: String(supplement.sourceSnapshot.catalogue),
  archive: String(supplement.sourceSnapshot.archive),
  scope: String(supplement.sourceSnapshot.scope),
};
const output = {
  schemaVersion: 1,
  generatedAt: supplement.asOf,
  sourceSnapshot,
  coverage: {
    inventoryStart: episodes[0].week,
    inventoryEnd: episodes.at(-1).week,
    episodeCount: episodes.length,
    transcriptPublished: publishedEpisodes,
    transcriptMissing: missingEpisodes,
    publicClipCount: episodes.reduce((count, episode) => count + episode.clips.length, 0),
    publicationEvidence: Object.fromEntries(episodes.map((episode) => [String(episode.week), episode.publicationEvidence])),
    limitations: Array.isArray(supplement.limitations) ? supplement.limitations.filter((item) => typeof item === "string") : [],
  },
  episodes,
};
assertPublicOutput(output);
writeFileSync(outputPath, `${JSON.stringify(output, null, 2)}\n`);
console.log(`Built ${episodes.length} public episodes (${publishedEpisodes.length} published transcripts, ${missingEpisodes.length} missing).`);
