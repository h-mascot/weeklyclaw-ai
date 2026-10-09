import { existsSync, mkdirSync, readFileSync, readdirSync, unlinkSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(process.env.PUBLIC_LIBRARY_ROOT || fileURLToPath(new URL("..", import.meta.url)));
const publicDataPath = join(root, "public-episodes.json");
const fallbackDataPath = join(root, "episodes.json");
const outputDataPath = join(root, "public-episodes.json");

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function safeUrl(value, { internal = false } = {}) {
  if (typeof value !== "string" || !value.trim()) return "";
  const candidate = value.trim();
  if (internal && candidate.startsWith("/") && !candidate.startsWith("//")) return candidate;
  try {
    const url = new URL(candidate);
    if (url.protocol !== "https:") return "";
    const allowed = ["weeklyclaw.ai", "www.youtube.com", "youtube.com", "youtu.be", "open.spotify.com", "x.com", "bsky.app", "bilibili.com", "www.bilibili.com"];
    return allowed.some((host) => url.hostname === host || url.hostname.endsWith(`.${host}`)) ? url.href : "";
  } catch {
    return "";
  }
}

const PUBLIC_RECORD_STATUSES = new Set(["published", "archived"]);
const PUBLIC_PUBLICATION_STATUSES = new Set(["published", "archived", "public_verified", "unknown"]);
const PRIVATE_STATES = new Set(["private", "draft", "planned", "ready", "scheduled", "unpublished", "local_review_only", "not_public"]);

function isPublicRecord(record) {
  if (!record) return false;
  const explicitFalse = (value) => value === false || value === 0 || String(value).trim().toLowerCase() === "false";
  if ([record.public, record.isPublic, record.sourcePublic, record.publiclyAvailable].some(explicitFalse)) return false;
  if (record.status !== undefined && !PUBLIC_RECORD_STATUSES.has(String(record.status).trim().toLowerCase())) return false;
  for (const value of [record.visibility, record.sourceVisibility, record.source_visibility]) {
    if (value !== undefined && value !== null && String(value).trim().toLowerCase() !== "public") return false;
  }
  if (record.publicationStatus !== undefined && record.publicationStatus !== null && !PUBLIC_PUBLICATION_STATUSES.has(String(record.publicationStatus).trim().toLowerCase())) return false;
  return true;
}

function videoIdFromUrl(url) {
  if (typeof url !== "string") return "";
  try {
    const parsed = new URL(url);
    if (parsed.hostname === "youtu.be") return parsed.pathname.slice(1).match(/^[A-Za-z0-9_-]{11}$/)?.[0] || "";
    if (parsed.hostname.endsWith("youtube.com")) return parsed.searchParams.get("v")?.match(/^[A-Za-z0-9_-]{11}$/)?.[0] || "";
  } catch {}
  return "";
}

function formatDate(value) {
  if (!value) return null;
  const parsed = new Date(`${value}T00:00:00Z`);
  if (Number.isNaN(parsed.getTime())) return String(value);
  return new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "short", year: "numeric", timeZone: "UTC" }).format(parsed);
}

const UNKNOWN_SPEAKER = "Speaker not identified";
const UNKNOWN_SPEAKER_KEYS = new Set([
  "",
  "unknown",
  "unidentified",
  "speaker",
  "speaker not identified",
  "none",
  "null",
  "n/a",
  "na",
  "authored or unspecified",
  "auto generated",
]);

function normalizeSpeakerKey(value) {
  const normalized = String(value || "")
    .trim()
    .toLowerCase()
    .replace(/[_-]+/g, " ")
    .replace(/\s+/g, " ");
  if (UNKNOWN_SPEAKER_KEYS.has(normalized) || /^(?:speaker|participant)(?: \d+)?$/.test(normalized)) return "unknown";
  return normalized;
}

function readableSpeaker(value) {
  const raw = String(value || "").trim();
  const key = normalizeSpeakerKey(raw);
  if (key === "unknown") return UNKNOWN_SPEAKER;
  const readable = raw.replace(/[_-]+/g, " ").replace(/\s+/g, " ").trim();
  return /^[a-z][a-z ]*$/u.test(readable) ? readable.replace(/\b[a-z]/gu, (letter) => letter.toUpperCase()) : readable;
}

function speakerInitial(label) {
  return label === UNKNOWN_SPEAKER ? "?" : [...label.trim()][0]?.toUpperCase() || "?";
}

function normalizeSegment(segment, index) {
  const seconds = (value) => typeof value === "number" && Number.isFinite(value) && value >= 0 ? value : null;
  const start = seconds(segment?.startSeconds);
  const end = seconds(segment?.endSeconds);
  return {
    id: String(segment?.id || `segment-${index + 1}`),
    startSeconds: start,
    endSeconds: end,
    speaker: segment?.speaker ? String(segment.speaker) : null,
    text: String(segment?.text || "").trim(),
  };
}

function normalizeEpisode(episode) {
  if (!isPublicRecord(episode)) return null;
  const week = Number(episode?.week ?? episode?.number);
  if (!Number.isInteger(week) || week < 1) return null;
  const title = String(episode?.title || `Weekly Claw episode ${week}`).trim();
  const date = episode?.date ? String(episode.date) : null;
  const videoId = String(episode?.videoId || videoIdFromUrl(episode?.url) || "").match(/^[A-Za-z0-9_-]{11}$/)?.[0] || null;
  const transcript = episode?.transcript || {};
  const segments = Array.isArray(transcript.segments) ? transcript.segments.map(normalizeSegment).filter((segment) => segment.text) : [];
  const transcriptPublished = transcript.status === "published" && segments.length > 0;
  const clips = Array.isArray(episode?.clips) ? episode.clips.filter((clip) => isPublicRecord(clip) && (clip?.public === true || clip?.isPublic === true || clip?.published === true || String(clip?.status || "").toLowerCase() === "published")).map((clip, index) => ({
    id: String(clip?.id || `clip-${index + 1}`),
    title: String(clip?.title || `Clip ${index + 1}`),
    url: safeUrl(clip?.url),
    platform: String(clip?.platform || "Published clip"),
    startSeconds: typeof clip?.startSeconds === "number" && Number.isFinite(clip.startSeconds) && clip.startSeconds >= 0 ? clip.startSeconds : null,
  })).filter((clip) => clip.url) : [];
  const deckUrl = safeUrl(episode?.deckUrl, { internal: true }) || (existsSync(join(root, "episodes", String(week), "deck.html")) ? `/episodes/${week}/deck` : null);
  return {
    week,
    title,
    date,
    dateLabel: episode?.dateLabel === null ? null : String(episode?.dateLabel || formatDate(date) || "Date unavailable"),
    url: safeUrl(episode?.url),
    videoId,
    thumbnailUrl: typeof episode.thumbnailUrl === "string" && /^\/assets\/youtube-thumbnails\/[A-Za-z0-9._-]+$/.test(episode.thumbnailUrl) ? episode.thumbnailUrl : null,
    summary: Array.isArray(episode?.summary) ? episode.summary.map((item) => String(item).trim()).filter(Boolean) : [],
    deckUrl,
    publicationStatus: episode?.publicationStatus === "public_verified" ? "public_verified" : "unknown",
    transcript: {
      status: transcriptPublished ? "published" : "missing",
      sourceUrl: safeUrl(transcript.sourceUrl),
      captionType: transcript.captionType ? String(transcript.captionType) : null,
      language: transcript.language ? String(transcript.language) : null,
      possibleCaptionErrors: transcript.possibleCaptionErrors === true,
      segments: transcriptPublished ? segments : [],
    },
    clips,
  };
}

function loadEpisodes() {
  const sourcePath = existsSync(publicDataPath) ? publicDataPath : process.env.PUBLIC_LIBRARY_ALLOW_LEGACY === "1" ? fallbackDataPath : null;
  if (!sourcePath) throw new Error("public-episodes.json is required; set PUBLIC_LIBRARY_ALLOW_LEGACY=1 only for local legacy scaffolding");
  const parsed = JSON.parse(readFileSync(sourcePath, "utf8"));
  if (sourcePath === publicDataPath && parsed.schemaVersion !== 1) throw new Error("public-episodes.json must declare schemaVersion: 1");
  const episodes = (Array.isArray(parsed) ? parsed : parsed.episodes || []).map(normalizeEpisode).filter(Boolean);
  const unique = new Map(episodes.map((episode) => [episode.week, episode]));
  return [...unique.values()].sort((a, b) => b.week - a.week);
}

function timestamp(seconds) {
  if (!Number.isFinite(seconds) || seconds < 0) return "";
  const whole = Math.floor(seconds);
  return `${Math.floor(whole / 60)}:${String(whole % 60).padStart(2, "0")}`;
}

function captionLabel(value) {
  const key = String(value || "").trim().toLowerCase();
  if (key === "authored_or_unspecified") return "Published captions · authorship unspecified";
  if (key === "auto_generated" || key === "auto-generated" || key === "autogenerated") return "Auto-generated captions";
  return value ? `Published captions · ${String(value).replaceAll("_", " ")}` : "Published transcript";
}

function visibleEpisodeTitle(episode) {
  const title = String(episode.title || "");
  return title.replace(new RegExp(`\\s*\\|\\s*Weekly Claw\\s*#?${episode.week}\\s*$`, "i"), "").trim() || title;
}

function pageFrame({ title, description, canonical, body, script = "", thumbnailUrl = null }) {
  return `<!doctype html>
<html lang="en" data-page="episode-library">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeHtml(description)}">
  <link rel="canonical" href="https://weeklyclaw.ai${canonical}">
  <meta property="og:title" content="${escapeHtml(title)}">
  <meta property="og:description" content="${escapeHtml(description)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://weeklyclaw.ai${canonical}">
  <meta property="og:image" content="https://weeklyclaw.ai${escapeHtml(thumbnailUrl || '/assets/og-image.jpg')}">
  <meta name="theme-color" content="#ece4d5">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>try { document.documentElement.dataset.theme = localStorage.getItem('weeklyclaw-theme') || 'light'; } catch { document.documentElement.dataset.theme = 'light'; }</script>
  <link rel="stylesheet" href="/assets/episode-library.css">
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header"><div class="shell header-inner">
    <a class="wordmark" href="/" aria-label="Weekly Claw home">WEEKLY CLAW</a>
    <nav class="site-nav" aria-label="Primary navigation"><a href="/episodes">Episodes</a><a href="/timeline/">Timeline</a><a href="/episodes#summaries">Summaries</a><button class="theme-toggle" data-theme-toggle type="button" aria-pressed="false" aria-label="Switch to dark mode" title="Switch to dark mode"><span aria-hidden="true" data-theme-icon>☾</span><span data-theme-label>Dark mode</span></button></nav>
  </div></header>
  ${body}
  <footer class="site-footer"><div class="shell footer-inner"><span>© 2026 Weekly Claw</span><nav aria-label="Footer navigation"><a href="/episodes">Episodes</a><a href="/timeline/">Topic timeline</a><a href="/">Home</a></nav></div></footer>
  ${script}
</body>
</html>`;
}

function transcriptSpeakerGroups(segments) {
  return segments.reduce((groups, segment) => {
    const key = normalizeSpeakerKey(segment.speaker);
    const label = readableSpeaker(segment.speaker);
    const previous = groups.at(-1);
    if (!previous || previous.key !== key) groups.push({ key, label, initial: speakerInitial(label), segments: [] });
    groups.at(-1).segments.push(segment);
    return groups;
  }, []);
}

function transcriptSegmentMarkup(segment) {
  const searchableText = `${readableSpeaker(segment.speaker)} ${segment.text}`.toLowerCase();
  const timestampMarkup = segment.startSeconds === null
    ? "Timestamp unavailable"
    : `<a class="timestamp" href="#${escapeHtml(segment.id)}" data-start-seconds="${segment.startSeconds}">${timestamp(segment.startSeconds)}</a>`;
  return `<li id="${escapeHtml(segment.id)}" data-transcript-text="${escapeHtml(searchableText)}"><div class="transcript-meta">${timestampMarkup}</div><p>${escapeHtml(segment.text)}</p></li>`;
}

function transcriptMarkup(segments) {
  return transcriptSpeakerGroups(segments).map((group) => `<section class="transcript-speaker-group" data-speaker-group="${escapeHtml(group.key)}"><h3 class="transcript-speaker-heading"><span class="speaker-badge" aria-hidden="true">${escapeHtml(group.initial)}</span><span>${escapeHtml(group.label)}</span></h3><ol class="speaker-turns">${group.segments.map(transcriptSegmentMarkup).join("")}</ol></section>`).join("");
}

function episodeBody(episode, previous, next) {
  const displayTitle = visibleEpisodeTitle(episode);
  const summaryItems = episode.summary.length ? episode.summary.map((item) => `<li>${escapeHtml(item)}</li>`).join("") : `<li class="muted-copy">No summary is recorded for this episode.</li>`;
  const video = episode.videoId
    ? `<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/${episode.videoId}?rel=0" title="Weekly Claw episode ${episode.week}: ${escapeHtml(episode.title)}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>`
    : `<div class="video-missing"><strong>Video unavailable</strong><p>No verified video embed is recorded for this episode.</p>${episode.url ? `<a class="button secondary" href="${escapeHtml(episode.url)}" target="_blank" rel="noopener">Open source link ↗</a>` : ""}</div>`;
  const transcriptPanel = episode.transcript.status === "published"
    ? `<div class="transcript-provenance"><span>${escapeHtml(captionLabel(episode.transcript.captionType))}</span>${episode.transcript.language ? `<span>Language · ${escapeHtml(episode.transcript.language)}</span>` : ""}${episode.transcript.possibleCaptionErrors ? `<span>Caption errors are possible; verify against the video.</span>` : ""}${episode.transcript.sourceUrl ? `<a href="${escapeHtml(episode.transcript.sourceUrl)}" target="_blank" rel="noopener">Transcript source ↗</a>` : ""}</div><label class="transcript-search"><span>Search transcript</span><input type="search" data-transcript-search placeholder="Find a phrase…"></label><p class="search-status" data-transcript-status>${episode.transcript.segments.length} published segments</p><div class="transcript-list" data-transcript-list>${transcriptMarkup(episode.transcript.segments)}</div>`
    : `<div class="unavailable"><strong>Transcript unavailable</strong><p>No published transcript is recorded for this episode. We will show it here when a verified transcript is published.</p>${episode.transcript.sourceUrl ? `<a href="${escapeHtml(episode.transcript.sourceUrl)}" target="_blank" rel="noopener">Open transcript source ↗</a>` : ""}</div>`;
  const clips = episode.clips.length ? `<button id="clips-tab" class="tab-button" role="tab" aria-selected="false" aria-controls="clips-panel" tabindex="-1">Clips <span>${episode.clips.length}</span></button>` : "";
  const clipsPanel = episode.clips.length ? `<section id="clips-panel" class="tab-panel" role="tabpanel" aria-labelledby="clips-tab"><div class="clip-grid">${episode.clips.map((clip) => `<a class="clip-card" href="${escapeHtml(clip.url)}" target="_blank" rel="noopener"><span class="eyebrow">${escapeHtml(clip.platform)}</span><strong>${escapeHtml(clip.title)}</strong><span>Open published clip ↗</span></a>`).join("")}</div></section>` : "";
  const sourceLink = episode.url ? `<a class="button secondary" href="${escapeHtml(episode.url)}" target="_blank" rel="noopener">${episode.videoId ? "Source video" : "Archive source"} ↗</a>` : "";
  const deckLink = episode.deckUrl ? `<a class="button secondary" href="${escapeHtml(episode.deckUrl)}">Slides ↗</a>` : "";
  const prevLink = previous ? `<a href="/episodes/${previous.week}/" rel="prev"><span>Previous episode</span><strong>W${previous.week} · ${escapeHtml(previous.title)}</strong></a>` : `<span></span>`;
  const nextLink = next ? `<a href="/episodes/${next.week}/" rel="next"><span>Next episode</span><strong>W${next.week} · ${escapeHtml(next.title)}</strong></a>` : `<span></span>`;
  const description = episode.summary[0] || `Weekly Claw episode ${episode.week}`;
  return `<main id="main-content" class="episode-main">
  <section class="episode-hero"><div class="shell narrow">
    <p class="eyebrow">Weekly Claw · episode ${episode.week}</p>
    <p class="episode-date">${escapeHtml(episode.dateLabel || "Date unavailable")}</p>${episode.publicationStatus === "unknown" ? `<p class="episode-status">Publication status unknown; this archive record has no verified released video.</p>` : ""}
    <h1>${escapeHtml(displayTitle)}</h1>
    <div class="hero-actions">${sourceLink}${deckLink}<a class="button secondary" href="/timeline/?q=${encodeURIComponent(episode.title.split(" ").slice(0, 3).join(" "))}">Search this topic ↗</a></div>
  </div></section>
  <section class="episode-player"><div class="shell narrow"><div class="section-kicker">Watch</div>${video}</div></section>
  <section class="episode-content"><div class="shell narrow">
    <div class="tab-list" role="tablist" aria-label="Episode content"><button id="summary-tab" class="tab-button" role="tab" aria-selected="true" aria-controls="summary-panel" tabindex="0">Summary</button><button id="transcript-tab" class="tab-button" role="tab" aria-selected="false" aria-controls="transcript-panel" tabindex="-1">Full transcript</button>${clips}</div>
    <section id="summary-panel" class="tab-panel" role="tabpanel" aria-labelledby="summary-tab"><p class="section-kicker">What this episode covers</p><ul class="summary-list">${summaryItems}</ul></section>
    <section id="transcript-panel" class="tab-panel" role="tabpanel" aria-labelledby="transcript-tab"><p class="section-kicker">Published record</p>${transcriptPanel}</section>
    ${clipsPanel}
  </div></section>
  <nav class="episode-pagination shell narrow" aria-label="Episode navigation">${prevLink}${nextLink}</nav>
</main>`;
}

function timelineBody(episodes) {
  const entries = episodes.map((episode) => {
    const summary = episode.summary.map((item) => `<li>${escapeHtml(item)}</li>`).join("");
    return `<article class="timeline-entry" data-week="${episode.week}" data-summary-text="${escapeHtml(episode.summary.join(" ").toLowerCase())}"><div class="timeline-marker"><span>W${episode.week}</span><time datetime="${escapeHtml(episode.date || "")}">${escapeHtml(episode.dateLabel || "Date unavailable")}</time></div><div class="timeline-card"><p class="eyebrow">Weekly Claw · W${episode.week}</p><h2><a href="/episodes/${episode.week}/">${escapeHtml(visibleEpisodeTitle(episode))}</a></h2><ul class="timeline-summary">${summary}</ul><div class="timeline-hit-label" data-hit-label hidden>Matching passages</div><ol class="timeline-transcript" data-transcript-results hidden></ol><a class="inline-link" href="/episodes/${episode.week}/">Open episode page →</a></div></article>`;
  }).join("");
  return `<main id="main-content" class="timeline-main"><section class="timeline-hero"><div class="shell narrow"><p class="eyebrow">Weekly Claw · research trail</p><h1>Episode timeline</h1><p>Search episode summaries and published transcript segments together. Missing transcripts remain outside the search coverage.</p><form class="timeline-search" action="/timeline/" method="get"><label for="timeline-query">Search every published episode</label><div><input id="timeline-query" name="q" type="search" placeholder="Try OpenAI, agents, verification…"><button class="button" type="submit">Search</button></div></form><p class="search-coverage">Coverage: ${episodes.length} episode records · ${episodes.filter((episode) => episode.transcript.status === "published").length} published transcripts</p><noscript><p class="muted-copy">Enable JavaScript to search published transcript segments; episode summaries remain available above.</p></noscript></div></section><section class="timeline-controls shell narrow"><div><strong data-search-status>${episodes.length} episodes</strong><span> · chronological archive</span></div><div class="order-buttons" role="group" aria-label="Timeline order"><button class="text-button" type="button" data-order="newest" aria-pressed="true">Newest first</button><button class="text-button" type="button" data-order="oldest" aria-pressed="false">Oldest first</button></div></section><section class="timeline-list shell narrow" data-timeline-list>${entries}</section></main>`;
}

function renderPages(episodes) {
  const detailScript = `<script src="/assets/episode-detail.js" defer></script>`;
  for (let index = 0; index < episodes.length; index += 1) {
    const episode = episodes[index];
    const previous = episodes[index + 1];
    const next = episodes[index - 1];
    const title = `Weekly Claw #${episode.week} — ${episode.title}`;
    const html = pageFrame({ title, description: episode.summary[0] || title, canonical: `/episodes/${episode.week}/`, body: episodeBody(episode, previous, next), script: detailScript, thumbnailUrl: episode.thumbnailUrl });
    const directory = join(root, "episodes", String(episode.week));
    mkdirSync(directory, { recursive: true });
    writeFileSync(join(directory, "index.html"), html);
  }
  const timelineDirectory = join(root, "timeline");
  mkdirSync(timelineDirectory, { recursive: true });
  writeFileSync(join(timelineDirectory, "index.html"), pageFrame({ title: "Weekly Claw Episode Timeline", description: "Search Weekly Claw episode summaries and published transcript segments by topic.", canonical: "/timeline/", body: timelineBody(episodes), script: `<script src="/assets/timeline.js" defer></script>` }));
}

function cleanupGeneratedPages(episodes) {
  const keep = new Set(episodes.map((episode) => String(episode.week)));
  for (const entry of readdirSync(join(root, "episodes"), { withFileTypes: true })) {
    if (!entry.isDirectory() || !/^\d+$/.test(entry.name) || keep.has(entry.name)) continue;
    const candidate = join(root, "episodes", entry.name, "index.html");
    if (existsSync(candidate) && readFileSync(candidate, "utf8").includes('data-page="episode-library"')) unlinkSync(candidate);
  }
}

function addArchiveLinks(episodes) {
  const archivePath = join(root, "episodes", "index.html");
  if (!existsSync(archivePath)) return;
  let html = readFileSync(archivePath, "utf8");
  const keep = new Set(episodes.map((episode) => String(episode.week)));
  html = html.replace(/<a class="deck-button secondary episode-library-link" href="\/episodes\/(\d+)\/">Episode page<\/a>/g, (match, week) => keep.has(week) ? match : "");
  if (!html.includes("/timeline/")) html = html.replace(/(<div class="filters"[\s\S]*?<\/div>)/, `$1<a class="deck-button secondary episode-library-timeline" href="/timeline/">Topic timeline →</a>`);
  for (const episode of episodes) {
    const cardPattern = new RegExp(`(<article class="week-card"[^>]*>(?:(?!<\\/article>)[\\s\\S])*?(?:data-week="${episode.week}"|<span class="week-number">(?:W|E)${episode.week}<\\/span>)(?:(?!<\\/article>)[\\s\\S])*?<div class="card-actions">)([\\s\\S]*?)(<\\/div>)`);
    if (!cardPattern.test(html)) continue;
    html = html.replace(cardPattern, (match, open, actions, close) => actions.includes(`href="/episodes/${episode.week}/"`) ? match : `${open}<a class="deck-button secondary episode-library-link" href="/episodes/${episode.week}/">Episode page</a>${actions}${close}`);
  }
  writeFileSync(archivePath, html);
}

function updateSitemap(episodes) {
  const sitemapPath = join(root, "sitemap.xml");
  if (!existsSync(sitemapPath)) return;
  let xml = readFileSync(sitemapPath, "utf8");
  xml = xml.replace(/\s*<url><loc>https:\/\/weeklyclaw\.ai\/timeline\/?<\/loc><\/url>/g, "");
  xml = xml.replace(/\s*<url><loc>https:\/\/weeklyclaw\.ai\/episodes\/\d+\/?<\/loc><\/url>/g, "");
  const generated = [`  <url><loc>https://weeklyclaw.ai/timeline/</loc></url>`, ...episodes.map((episode) => `  <url><loc>https://weeklyclaw.ai/episodes/${episode.week}/</loc></url>`)].join("\n");
  xml = xml.replace("</urlset>", `${generated}\n</urlset>`);
  writeFileSync(sitemapPath, xml);
}

function addHomepageLink() {
  const homepagePath = join(root, "index.html");
  if (!existsSync(homepagePath)) return;
  let html = readFileSync(homepagePath, "utf8");
  if (html.includes('href="/timeline/"')) return;
  const marker = '<div class="archive-head-actions"><a class="button" href="/episodes">View all weeks <span aria-hidden="true">→</span></a></div>';
  if (html.includes(marker)) html = html.replace(marker, '<div class="archive-head-actions"><a class="button" href="/episodes">View all weeks <span aria-hidden="true">→</span></a><a class="button secondary" href="/timeline/">Topic timeline</a></div>');
  writeFileSync(homepagePath, html);
}

const episodes = loadEpisodes();
if (!episodes.length) throw new Error("No public episodes found in public-episodes.json or episodes.json");
cleanupGeneratedPages(episodes);
renderPages(episodes);
addArchiveLinks(episodes);
addHomepageLink();
updateSitemap(episodes);
console.log(`Rendered ${episodes.length} public episode pages and /timeline/`);
