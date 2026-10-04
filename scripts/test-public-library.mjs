import assert from "node:assert/strict";
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";
import { createEpisodeSearch } from "../assets/episode-search.mjs";

const root = fileURLToPath(new URL("..", import.meta.url));
const build = spawnSync(process.execPath, [join(root, "scripts", "build-public-library.mjs")], { encoding: "utf8" });
assert.equal(build.status, 0, build.stderr || build.stdout);
const outputPath = join(root, "public-episodes.json");
assert.ok(existsSync(outputPath));
const corpus = JSON.parse(readFileSync(outputPath, "utf8"));
assert.equal(corpus.schemaVersion, 1);
assert.equal(corpus.episodes.length, 22);
assert.deepEqual(corpus.episodes.map((episode) => episode.week), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]);
assert.deepEqual(corpus.coverage.transcriptPublished, [22, 24, 27, 28, 29, 30, 31]);
assert.deepEqual(corpus.coverage.transcriptMissing, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 26]);
assert.equal(corpus.coverage.publicClipCount, 0);
assert.ok(corpus.episodes.find((episode) => episode.week === 27).transcript.segments.length > 400);
assert.ok(corpus.episodes.find((episode) => episode.week === 31).transcript.segments.length > 900);
assert.equal(corpus.episodes.find((episode) => episode.week === 10).publicationStatus, "unknown");
assert.equal(corpus.episodes.find((episode) => episode.week === 10).date, null);
assert.match(corpus.episodes.find((episode) => episode.week === 13).dateLabel, /publication unknown/);
const episodeKeys = ["clips", "date", "dateLabel", "deckUrl", "publicationEvidence", "publicationStatus", "summary", "title", "transcript", "url", "videoId", "week"];
const transcriptKeys = ["captionType", "language", "possibleCaptionErrors", "segments", "sourceHash", "sourceUrl", "status"];
for (const episode of corpus.episodes) {
  assert.deepEqual(Object.keys(episode).sort(), [...episodeKeys].sort());
  assert.equal(typeof episode.deckUrl, "string");
  assert.deepEqual(episode.clips, []);
  assert.match(episode.url, /^https:\/\/((www\.)?youtube\.com\/watch\?v=|weeklyclaw\.ai\/)/);
  if (episode.videoId) assert.match(episode.url, new RegExp(`[?&]v=${episode.videoId.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}`));
  assert.deepEqual(Object.keys(episode.transcript).sort(), [...transcriptKeys].sort());
  assert.equal(episode.transcript.status === "published", episode.transcript.segments.length > 0);
  const ids = new Set(episode.transcript.segments.map((segment) => segment.id));
  assert.equal(ids.size, episode.transcript.segments.length);
  for (const segment of episode.transcript.segments) {
    assert.match(segment.id, new RegExp(`^e${episode.week}-\\d{5}-\\d{2}$`));
    assert.equal(segment.endSeconds, null, "source exports provide cue starts only");
  }
}
const serialized = JSON.stringify(corpus);
for (const forbidden of ["/Users/", "/private/", "/var/folders/", '"sourcePath"', '"downloadURL"', '"downloadUrl"', '"password"', '"cookie"']) {
  assert.equal(serialized.toLowerCase().includes(forbidden.toLowerCase()), false, `public corpus contains ${forbidden}`);
}
assert.equal(corpus.episodes.some((episode) => episode.week === 32), false);

// The builder's explicit field projection must ignore private source metadata,
// and a transcript whose declared video ID changes must fail closed.
const fixtureRoot = mkdtempSync(join(tmpdir(), "weeklyclaw-public-corpus-"));
try {
  mkdirSync(join(fixtureRoot, "data", "public-transcripts"), { recursive: true });
  mkdirSync(join(fixtureRoot, "data", "public-speaker-annotations"), { recursive: true });
  const fixtureSource = JSON.parse(readFileSync(join(root, "episodes.json"), "utf8"));
  fixtureSource.episodes = fixtureSource.episodes.map((episode) => ({ ...episode, privatePath: "/Users/enterprise/secret-SHOULD_NOT_LEAK", downloadURL: "https://private.invalid/SHOULD_NOT_LEAK", notes: "SHOULD_NOT_LEAK" }));
  fixtureSource.episodes.push({ week: 33, title: "Future public catalogue entry", date: null, url: null, videoId: null, summary: ["Published summary pending transcript"] });
  fixtureSource.episodes.push(
    { week: 34, title: "Draft source must not appear", date: null, url: null, videoId: null, summary: ["zxqdraftmarker9341"], status: "draft" },
    { week: 35, title: "Private source must not appear", date: null, url: null, videoId: null, summary: ["zxqprivatemarker9342"], visibility: "private" },
    { week: 36, title: "False source must not appear", date: null, url: null, videoId: null, summary: ["zxqfalsemarker9343"], public: false },
    { week: 37, title: "Unpublished source must not appear", date: null, url: null, videoId: null, summary: ["zxqunpublishedmarker9344"], publicationStatus: "unpublished" },
    { week: 38, title: "Ready internal source must not appear", date: null, url: null, videoId: null, summary: ["zxqreadymarker9345"], status: "ready", sourceVisibility: "internal" },
    { week: 40, title: "Nonpublic visibility must not appear", date: null, url: null, videoId: null, summary: ["zxqvisibilitymarker9347"], visibility: "not_public" },
    { week: 41, title: "Scheduled source must not appear", date: null, url: null, videoId: null, summary: ["zxqschedulemarker9348"], status: "scheduled" },
    { week: 42, title: "Pending source must not appear", date: null, url: null, videoId: null, summary: ["zxqpendingmarker9349"], status: "pending" },
    { week: 44, title: "Nonpublic publication state must not appear", date: null, url: null, videoId: null, summary: ["zxqpublicationmarker9351"], publicationStatus: "not_public" },
    { week: 45, title: "Scheduled publication state must not appear", date: null, url: null, videoId: null, summary: ["zxqpublicationscheduledmarker9352"], publicationStatus: "scheduled" },
    { week: 46, title: "Pending publication state must not appear", date: null, url: null, videoId: null, summary: ["zxqpublicationpendingmarker9353"], publicationStatus: "pending" },
  );
  writeFileSync(join(fixtureRoot, "episodes.json"), JSON.stringify(fixtureSource));
  const fixtureSupplement = JSON.parse(readFileSync(join(root, "data", "public-episode-supplements.json"), "utf8"));
  fixtureSupplement.transcripts["22"].downloadURL = "https://private.invalid/SHOULD_NOT_LEAK";
  fixtureSupplement.transcripts["22"].notes = "SHOULD_NOT_LEAK";
  fixtureSupplement.archiveEpisodes.push({ week: 39, title: "Private archive source must not appear", dateLabel: "SHOULD_NOT_LEAK", url: "https://weeklyclaw.ai/private", summary: ["zxqarchivemarker9346"], deckUrl: "/private", status: "draft" });
  fixtureSupplement.archiveEpisodes.push({ week: 43, title: "Nonpublic archive source must not appear", dateLabel: "SHOULD_NOT_LEAK", url: "https://weeklyclaw.ai/private-archive", summary: ["zxqarchivevisibilitymarker9350"], deckUrl: "/private-archive", source_visibility: "not_public" });
  fixtureSupplement.archiveEpisodes.push(
    { week: 47, title: "Nonpublic archive publication state must not appear", dateLabel: "SHOULD_NOT_LEAK", url: "https://weeklyclaw.ai/private-publication", summary: ["zxqarchivepublicationmarker9354"], deckUrl: "/private-publication", publicationStatus: "not_public" },
    { week: 48, title: "Scheduled archive publication state must not appear", dateLabel: "SHOULD_NOT_LEAK", url: "https://weeklyclaw.ai/scheduled-publication", summary: ["zxqarchivescheduledmarker9355"], deckUrl: "/scheduled-publication", publicationStatus: "scheduled" },
  );
  writeFileSync(join(fixtureRoot, "data", "public-episode-supplements.json"), JSON.stringify(fixtureSupplement));
  for (const week of [22, 24, 27, 28, 29, 30, 31]) copyFileSync(join(root, "data", "public-transcripts", `e${week}.txt`), join(fixtureRoot, "data", "public-transcripts", `e${week}.txt`));
  copyFileSync(join(root, "data", "public-speaker-annotations", "e31.json"), join(fixtureRoot, "data", "public-speaker-annotations", "e31.json"));
  const runFixture = () => spawnSync(process.execPath, [join(root, "scripts", "build-public-library.mjs")], { encoding: "utf8", env: { ...process.env, PUBLIC_LIBRARY_ROOT: fixtureRoot } });
  const fixtureBuild = runFixture();
  assert.equal(fixtureBuild.status, 0, fixtureBuild.stderr);
  const fixtureOutput = readFileSync(join(fixtureRoot, "public-episodes.json"), "utf8");
  assert.equal(fixtureOutput.includes("SHOULD_NOT_LEAK"), false);
  assert.equal(fixtureOutput.includes("private.invalid"), false);
  const fixtureCorpus = JSON.parse(fixtureOutput);
  assert.equal(fixtureCorpus.episodes.find((episode) => episode.week === 33).transcript.status, "missing");
  assert.equal(fixtureCorpus.episodes.find((episode) => episode.week === 33).deckUrl, null, "a new episode without a local deck must not emit a broken Slides link");
  for (const excludedWeek of [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) assert.equal(fixtureCorpus.episodes.some((episode) => episode.week === excludedWeek), false);
  const fixtureE31 = fixtureCorpus.episodes.find((episode) => episode.week === 31);
  assert.ok(fixtureE31.transcript.segments.filter((segment) => segment.speaker).length >= 700);
  assert.equal(fixtureE31.transcript.segments.find((segment) => segment.id === "e31-00000-01").speaker, "Andy");
  assert.equal(fixtureE31.transcript.segments.find((segment) => segment.id === "e31-00041-01").speaker, "Henry");
  assert.equal(fixtureE31.transcript.segments.find((segment) => segment.id === "e31-00170-01").speaker, null, "the documented overlapping 2:50 cue remains unresolved");
  assert.equal(fixtureE31.transcript.segments.find((segment) => segment.id === "e31-01494-02").speaker, null, "embedded caption labels remain unresolved");
  assert.equal(fixtureE31.transcript.segments.find((segment) => segment.id === "e31-04243-01").speaker, null, "reconnect attribution remains unresolved");
  assert.equal(fixtureE31.transcript.segments.find((segment) => segment.id === "e31-04252-01").speaker, null, "reconnect exit remains unresolved");
  const annotationSerialized = readFileSync(join(fixtureRoot, "data", "public-speaker-annotations", "e31.json"), "utf8");
  for (const forbidden of ["/Users/", "/private/", "/var/folders/", "sourcePath", "downloadURL", "rawTranscriptPath"]) {
    assert.equal(annotationSerialized.toLowerCase().includes(forbidden.toLowerCase()), false, `speaker annotation contains ${forbidden}`);
  }
  const annotatedCueShape = fixtureE31.transcript.segments.map(({ id, startSeconds, endSeconds, text }) => ({ id, startSeconds, endSeconds, text }));
  delete fixtureSupplement.transcripts["31"].speakerAnnotationPath;
  writeFileSync(join(fixtureRoot, "data", "public-episode-supplements.json"), JSON.stringify(fixtureSupplement));
  const unannotatedBuild = runFixture();
  assert.equal(unannotatedBuild.status, 0, unannotatedBuild.stderr);
  const unannotatedE31 = JSON.parse(readFileSync(join(fixtureRoot, "public-episodes.json"), "utf8")).episodes.find((episode) => episode.week === 31);
  assert.deepEqual(unannotatedE31.transcript.segments.map(({ id, startSeconds, endSeconds, text }) => ({ id, startSeconds, endSeconds, text })), annotatedCueShape, "speaker enrichment must preserve caption identities, text, and times");
  fixtureSupplement.transcripts["31"].speakerAnnotationPath = "data/public-speaker-annotations/e31.json";
  writeFileSync(join(fixtureRoot, "data", "public-episode-supplements.json"), JSON.stringify(fixtureSupplement));
  assert.equal(runFixture().status, 0);
  const annotationPath = join(fixtureRoot, "data", "public-speaker-annotations", "e31.json");
  const originalAnnotation = JSON.parse(readFileSync(annotationPath, "utf8"));
  const expectAnnotationFailure = (mutate, pattern) => {
    const mutated = JSON.parse(JSON.stringify(originalAnnotation));
    mutate(mutated);
    writeFileSync(annotationPath, JSON.stringify(mutated));
    const result = runFixture();
    assert.notEqual(result.status, 0);
    assert.match(`${result.stdout}\n${result.stderr}`, pattern);
    writeFileSync(annotationPath, JSON.stringify(originalAnnotation));
    assert.equal(runFixture().status, 0);
  };
  expectAnnotationFailure((annotation) => { annotation.videoId = "wrong-video"; }, /wrong video/);
  expectAnnotationFailure((annotation) => { annotation.captionSourceHash = "0".repeat(64); }, /caption source hash/);
  expectAnnotationFailure((annotation) => { annotation.annotations[0].segmentId = "e31-99999-01"; }, /unknown cue/);
  expectAnnotationFailure((annotation) => { annotation.annotations[0].speakerId = "unknown"; }, /unknown speaker/);
  expectAnnotationFailure((annotation) => { annotation.annotations[0].textHash = "0".repeat(64); }, /cue text hash/);
  const fixtureSearch = createEpisodeSearch(fixtureCorpus);
  for (const privateTerm of ["zxqdraftmarker9341", "zxqprivatemarker9342", "zxqfalsemarker9343", "zxqunpublishedmarker9344", "zxqreadymarker9345", "zxqarchivemarker9346", "zxqvisibilitymarker9347", "zxqschedulemarker9348", "zxqpendingmarker9349", "zxqarchivevisibilitymarker9350", "zxqpublicationmarker9351", "zxqpublicationscheduledmarker9352", "zxqpublicationpendingmarker9353", "zxqarchivepublicationmarker9354", "zxqarchivescheduledmarker9355"]) {
    assert.deepEqual(fixtureSearch.search(privateTerm), []);
  }
  mkdirSync(join(fixtureRoot, "episodes"), { recursive: true });
  const renderedFixture = spawnSync(process.execPath, [join(root, "scripts", "render-public-library.mjs")], { encoding: "utf8", env: { ...process.env, PUBLIC_LIBRARY_ROOT: fixtureRoot } });
  assert.equal(renderedFixture.status, 0, renderedFixture.stderr || renderedFixture.stdout);
  for (const excludedWeek of [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) assert.equal(existsSync(join(fixtureRoot, "episodes", String(excludedWeek), "index.html")), false);
  const e22Path = join(fixtureRoot, "data", "public-transcripts", "e22.txt");
  const e22 = readFileSync(e22Path, "utf8");
  writeFileSync(e22Path, e22.replace("Video ID: f2yugYwXOBo", "Video ID: WRONG_VIDEO_ID"));
  const mismatch = runFixture();
  assert.notEqual(mismatch.status, 0);
  assert.match(`${mismatch.stdout}\n${mismatch.stderr}`, /does not identify expected video|source hash does not match/);
} finally {
  rmSync(fixtureRoot, { recursive: true, force: true });
}
console.log(`Public corpus validation passed: ${corpus.episodes.length} episodes, ${corpus.coverage.transcriptPublished.length} transcripts.`);
