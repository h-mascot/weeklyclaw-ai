/* Run with: node scripts/test_render_public_library.mjs */
import assert from "node:assert/strict";
import { copyFileSync, existsSync, mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { execFileSync } from "node:child_process";
import { tmpdir } from "node:os";
import { fileURLToPath } from "node:url";

const fixtureRoot = mkdtempSync(join(tmpdir(), "weeklyclaw public library-"));
const writeFixture = (episodes) => {
  mkdirSync(join(fixtureRoot, "episodes", "7"), { recursive: true });
  mkdirSync(join(fixtureRoot, "episodes", "8"), { recursive: true });
  writeFileSync(join(fixtureRoot, "episodes", "index.html"), '<div class="filters"></div><div class="gallery"><article class="week-card"><span class="week-number">W7</span><div class="card-actions"><a class="source-link" href="https://www.youtube.com/watch?v=aaaaaaaaaaa">Video</a></div></article><article class="week-card"><span class="week-number">W8</span><div class="card-actions"><a class="source-link" href="https://www.youtube.com/watch?v=bbbbbbbbbbb">Video</a></div></article></div>');
  writeFileSync(join(fixtureRoot, "public-episodes.json"), JSON.stringify({ schemaVersion: 1, episodes }));
  writeFileSync(join(fixtureRoot, "episodes", "7", "deck.html"), "deck");
  writeFileSync(join(fixtureRoot, "episodes", "8", "deck.html"), "deck");
};
const run = () => execFileSync(process.execPath, ["scripts/render-public-library.mjs"], { cwd: new URL("..", import.meta.url), env: { ...process.env, PUBLIC_LIBRARY_ROOT: fixtureRoot }, stdio: "pipe" });

try {
  writeFixture([
    {
      week: 7,
      title: "Seven | Weekly Claw #7",
      date: "2026-01-01",
      url: "https://www.youtube.com/watch?v=aaaaaaaaaaa",
      videoId: "aaaaaaaaaaa",
      summary: ["Verified summary"],
      transcript: { status: "published", captionType: "authored_or_unspecified", segments: [{ id: "seven-12", startSeconds: 12.5, speaker: "Henry", text: "A timestamped public segment." }, { id: "seven-18", startSeconds: 18, speaker: "Henry", text: "A consecutive turn stays in the same group." }, { id: "seven-24", speaker: "speaker_1", text: "An unidentified speaker keeps an honest label." }] },
      clips: [
        { title: "Verified clip", url: "https://x.com/weeklyclaw/status/123", status: "published" },
        { title: "Unreviewed clip", url: "https://x.com/weeklyclaw/status/456" },
        { title: "Draft despite public flag", url: "https://x.com/weeklyclaw/status/789", public: true, status: "draft" },
        { title: "Ready despite public flag", url: "https://x.com/weeklyclaw/status/790", public: true, status: "ready" },
        { title: "Scheduled despite public flag", url: "https://x.com/weeklyclaw/status/791", public: true, status: "scheduled" },
        { title: "Scheduled publication", url: "https://x.com/weeklyclaw/status/792", public: true, status: "published", publicationStatus: "scheduled" },
      ],
    },
    { week: 99, title: "Private draft", status: "draft", url: "https://www.youtube.com/watch?v=ccccccccccc", videoId: "ccccccccccc", summary: ["Do not publish"] },
  ]);
  run();
  const firstDetail = readFileSync(join(fixtureRoot, "episodes", "7", "index.html"), "utf8");
  assert.match(firstDetail, /Verified summary/);
  assert.match(firstDetail, /Verified clip/);
  assert.doesNotMatch(firstDetail, /Unreviewed clip/);
  assert.doesNotMatch(firstDetail, /Draft despite public flag/);
  assert.doesNotMatch(firstDetail, /Ready despite public flag/);
  assert.doesNotMatch(firstDetail, /Scheduled despite public flag/);
  assert.doesNotMatch(firstDetail, /Scheduled publication/);
  assert.doesNotMatch(firstDetail, /Weekly Claw #7<\/h1>/, "display title should not duplicate the episode label");
  assert.match(firstDetail, /data-start-seconds="12\.5"/);
  assert.match(firstDetail, /class="transcript-speaker-group" data-speaker-group="henry"/);
  assert.match(firstDetail, /class="speaker-badge" aria-hidden="true">H<\/span>/);
  assert.match(firstDetail, /Speaker not identified/);
  assert.doesNotMatch(firstDetail, /speaker_1/);
  assert.equal((firstDetail.match(/transcript-speaker-heading/g) || []).length, 2, "consecutive turns should group by speaker and split on change");
  assert.match(firstDetail, /Published captions · authorship unspecified/);
  assert.doesNotMatch(firstDetail, /authored_or_unspecified/);
  assert.equal(existsSync(join(fixtureRoot, "episodes", "99", "index.html")), false, "private draft should not generate a public page");
  const timeline = readFileSync(join(fixtureRoot, "timeline", "index.html"), "utf8");
  assert.match(timeline, /href="\/episodes\/7\/"/);
  assert.doesNotMatch(timeline, /A timestamped public segment/, "timeline should lazy-load transcript hits instead of embedding full transcript text");
  assert.doesNotMatch(timeline, /Published transcript matches/);
  assert.doesNotMatch(timeline, /Seven \| Weekly Claw #7/);
  assert.match(readFileSync(join(fixtureRoot, "episodes", "index.html"), "utf8"), /href="\/episodes\/7\/"/);
  writeFixture([{ week: 8, title: "Eight", date: "2026-01-08", url: "https://www.youtube.com/watch?v=bbbbbbbbbbb", videoId: "bbbbbbbbbbb", summary: ["New summary"] }]);
  run();
  assert.equal(existsSync(join(fixtureRoot, "episodes", "7", "index.html")), false, "stale generated page should be removed");
  assert.equal(existsSync(join(fixtureRoot, "episodes", "8", "index.html")), true, "new episode page should be generated");
  const detailScript = readFileSync(new URL("../assets/episode-detail.js", import.meta.url), "utf8");
  const archiveScript = readFileSync(new URL("../episodes/index.html", import.meta.url), "utf8");
  const timelineScript = readFileSync(new URL("../assets/timeline.js", import.meta.url), "utf8");
  const libraryCss = readFileSync(new URL("../assets/episode-library.css", import.meta.url), "utf8");
  assert.match(detailScript, /addEventListener\("hashchange"/);
  assert.match(detailScript, /seekVideo\(Number\(timestamp\)\)/);
  assert.match(detailScript, /weeklyclaw-theme/);
  assert.match(detailScript, /Switch to light mode/);
  assert.match(archiveScript, /\.deck-button\[data-week\]\[data-deck\]\[data-url\]/, "episode navigation links must not enter the deck modal handler");
  assert.match(timelineScript, /sourceType === "summary"/);
  assert.match(timelineScript, /searchForm\?\.addEventListener\("submit"/);
  assert.match(libraryCss, /\.video-frame iframe \{[^}]*min-width: 0/);
  const spacedRoot = mkdtempSync(join(tmpdir(), "weeklyclaw renderer space-"));
  try {
    mkdirSync(join(spacedRoot, "episodes"), { recursive: true });
    mkdirSync(join(spacedRoot, "scripts"), { recursive: true });
    copyFileSync(fileURLToPath(new URL("../scripts/render-public-library.mjs", import.meta.url)), join(spacedRoot, "scripts", "render-public-library.mjs"));
    writeFileSync(join(spacedRoot, "public-episodes.json"), JSON.stringify({ schemaVersion: 1, episodes: [{ week: 8, title: "Eight", summary: ["Space-safe root"] }] }));
    const { PUBLIC_LIBRARY_ROOT: ignoredRoot, ...cleanEnv } = process.env;
    execFileSync(process.execPath, ["scripts/render-public-library.mjs"], { cwd: spacedRoot, env: cleanEnv, stdio: "pipe" });
    assert.equal(existsSync(join(spacedRoot, "episodes", "8", "index.html")), true, "renderer should resolve its own path when the checkout contains spaces");
  } finally {
    rmSync(spacedRoot, { recursive: true, force: true });
  }
  console.log("public library generation regression passed");
} finally {
  rmSync(fixtureRoot, { recursive: true, force: true });
}
