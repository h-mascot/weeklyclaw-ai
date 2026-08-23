import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = new URL('..', import.meta.url);
const required = [
  'index.html',
  'feedback.html',
  'api/feedback.js',
  'weeklyclaw-archive.html',
  'changelog/index.html',
  'episodes/index.html',
  'episodes.json',
  'feed.xml',
  'episodes/10/deck.html',
  'episodes/11/deck.html',
  'episodes/12/deck.html',
  'episodes/13/deck.html',
  'episodes/13/agenda.md',
  'episodes/14/deck.html',
  'episodes/15/deck.html',
  'episodes/15/agenda.md',
  'episodes/18/deck.html',
  'episodes/19/deck.html',
  'episodes/19/host.html',
  'episodes/19/viewer-agenda.md',
  'episodes/19/host-agenda.md',
  'episodes/20/agenda.md',
  'episodes/20/agenda/index.html',
  'episodes/20/deck.html',
  'episodes/26/agenda.md',
  'episodes/26/agenda/index.html',
  'episodes/26/deck.html',
  'episodes/25/agenda.md',
  'episodes/25/agenda/index.html',
  'episodes/25/deck.html',
  'episodes/24/agenda.md',
  'episodes/24/agenda/index.html',
  'episodes/24/deck.html',
  'episodes/23/agenda.md',
  'episodes/23/agenda/index.html',
  'episodes/23/deck.html',
  'episodes/22/agenda.md',
  'episodes/22/agenda/index.html',
  'episodes/22/deck.html',
  'episodes/21/agenda.md',
  'episodes/21/agenda/index.html',
  'episodes/21/deck.html',
  'w18/changelog/index.html', 'w19/changelog/index.html'];

const weeks = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
for (const week of weeks) {
  required.push(`w${week}/index.html`, `w${week}/changelog/index.html`);
}

const missing = required.filter((p) => !existsSync(new URL(`../${p}`, import.meta.url)));
if (missing.length) {
  console.error(`Missing required files: ${missing.join(', ')}`);
  process.exit(1);
}

const html = readFileSync(new URL('../index.html', import.meta.url), 'utf8');
for (const needle of [
  '<title>Weekly Claw</title>',
  '<meta property="og:title" content="Weekly Claw">',
  '<meta name="twitter:title" content="Weekly Claw">',
  'Weekly Claw',
  'The cost of intelligence collapsed',
  '/feedback',
  'https://www.youtube.com/watch?v=dquJyEBQWpE',
  'https://www.youtube.com/watch?v=MSRFmpDfaTg',
  'The Sandbox Failed',
  'assets/youtube-thumbnails/w22-v2-the-sandbox-failed-approved-20260727.jpg',
  'assets/youtube-thumbnails/w21-v2-approved-20260727.jpg',
  'assets/youtube-thumbnails/w20-v2-ai-got-cheap-approved-20260727.jpg',
  'live builder show about AI, agents, devtools, and the future of work',
  'The week decides',
  'Latest Episodes',
  'Supported by',
  'Herald Labs',
  'https://labs.theherald.co/',
  'https://superada.ai/',
  'https://heritagetel.com/',
  'assets/sponsors/heritage-logo.png',
  'assets/weeklyclaw-hosts-source.png?v=20260717-light-smile',
  'https://x.com/weeklyclaw',
  'https://youtube.com/@weeklyclaw',
  'https://space.bilibili.com/3707046262213278/',
  'action="https://weeklyclaw.beehiiv.com/create"',
  'name="sent_from_orchid" value="true"',
  'id="newsletter"',
  'class="social-icon"',
  'aria-label="Follow Weekly Claw on X"',
  'aria-label="Watch Weekly Claw on YouTube"',
  'aria-label="Watch Weekly Claw on Bilibili"',
  'rel="noopener noreferrer" referrerpolicy="no-referrer" aria-label="Watch Weekly Claw on Bilibili"',
  'href="https://podcasts.apple.com/us/podcast/weekly-claw/id6795290527"',
  'href="https://open.spotify.com/show/033WWP2IOLy2T3SApjvw8v"',
  'aria-label="Listen to Weekly Claw on Apple Podcasts"',
  'aria-label="Listen to Weekly Claw on Spotify"',
]) {
  if (!html.includes(needle)) {
    console.error(`Missing expected homepage copy: ${needle}`);
    process.exit(1);
  }
}

if (html.includes('platform-link-pending') || html.includes('>Soon<')) {
  console.error('Homepage still renders pending platform placeholders');
  process.exit(1);
}

const desktopNav = html.match(/<nav class="desktop-nav"[\s\S]*?<\/nav>/)?.[0] ?? '';
const mobileNav = html.match(/<nav class="mobile-nav"[\s\S]*?<\/nav>/)?.[0] ?? '';
const footerNav = html.match(/<nav class="footer-links"[\s\S]*?<\/nav>/)?.[0] ?? '';
for (const [label, nav] of [['desktop nav', desktopNav], ['mobile nav', mobileNav], ['footer nav', footerNav]]) {
  if (!nav) {
    console.error(`Missing ${label}`);
    process.exit(1);
  }
  for (const forbidden of ['#newsletter', 'https://x.com/weeklyclaw', '>Newsletter<', '>X<', '>YouTube<']) {
    if (nav.includes(forbidden)) {
      console.error(`${label} still contains forbidden menu item: ${forbidden}`);
      process.exit(1);
    }
  }
}

const feedbackHtml = readFileSync(new URL('../feedback.html', import.meta.url), 'utf8');
for (const needle of [
  'id="feedback-form"',
  'action="/api/feedback"',
  'id="form-status"',
  'Feedback sent. Thank you for helping shape the next Weekly Claw.',
  'form.reportValidity()',
  'Content-Type": "application/json"',
]) {
  if (!feedbackHtml.includes(needle)) {
    console.error(`Feedback page missing expected integration marker: ${needle}`);
    process.exit(1);
  }
}
if (feedbackHtml.includes('formsubmit.co')) {
  console.error('Feedback page still exposes the retired FormSubmit endpoint');
  process.exit(1);
}

const feedbackApi = readFileSync(new URL('../api/feedback.js', import.meta.url), 'utf8');
for (const needle of ['WEEKLYCLAW_FEEDBACK_REPO', 'WEEKLYCLAW_GITHUB_TOKEN', 'https://api.github.com/repos/${repo}/issues', 'website-feedback']) {
  if (!feedbackApi.includes(needle)) {
    console.error(`Feedback API missing expected GitHub integration marker: ${needle}`);
    process.exit(1);
  }
}

if (!readFileSync(new URL('../README.md', import.meta.url), 'utf8').includes('/w19/changelog/')) {
  console.error('README is missing the W19 changelog route');
  process.exit(1);
}

const changelogHtml = readFileSync(new URL('../changelog/index.html', import.meta.url), 'utf8');
for (const needle of ['Release changelogs', '/w11/changelog/', '/w18/changelog/', '/w19/changelog/', '/w20/changelog/', '/episodes/11/deck', '/episodes/12/deck', '/episodes/14/deck', '/episodes/18/deck', '/episodes/19/deck', 'Episode deck', 'Changelog/DX deck']) {
  if (!changelogHtml.includes(needle)) {
    console.error(`Changelog index missing expected copy: ${needle}`);
    process.exit(1);
  }
}

if (changelogHtml.includes('Open changelog') || changelogHtml.includes('Host deck') || changelogHtml.includes('/episodes/19/host.html') || changelogHtml.includes('Main slides') || changelogHtml.includes('Changelog archive') || changelogHtml.includes('mirrored SuperAda') || changelogHtml.includes('short week routes')) {
  console.error('Changelog index still exposes low-value or duplicate CTA copy');
  process.exit(1);
}


const episodesHtml = readFileSync(new URL('../episodes/index.html', import.meta.url), 'utf8');
for (const needle of ['Weekly Claw Episodes', 'W26', 'The Sandbox Failed', '/episodes/22/deck', 'data-video-id="f2yugYwXOBo"', 'data-video-id="dquJyEBQWpE"', 'data-video-id="MSRFmpDfaTg"', '/assets/youtube-thumbnails/w22-v2-the-sandbox-failed-approved-20260727.jpg', '/assets/youtube-thumbnails/w21-v2-approved-20260727.jpg', '/assets/youtube-thumbnails/w20-v2-ai-got-cheap-approved-20260727.jpg', '<strong>17</strong>', 'archived episodes']) {
  if (!episodesHtml.includes(needle)) {
    console.error(`Episodes index missing expected copy: ${needle}`);
    process.exit(1);
  }
}

// --- Episode summaries section + RSS feed (2026-08-23) ---
for (const needle of [
  'id="summaries"',
  'Every episode, summarized',
  'subscribe to the RSS feed',
  'data-summary-week="26"',
  'data-summary-week="20"',
  'data-summary-week="10"',
  '<link rel="alternate" type="application/rss+xml" title="The Weekly Claw — Episode Summaries" href="/feed.xml">',
]) {
  if (!episodesHtml.includes(needle)) {
    console.error(`Episodes index missing summaries marker: ${needle}`);
    process.exit(1);
  }
}
const summaryCount = (episodesHtml.match(/class="summary-item"/g) ?? []).length;
if (summaryCount !== 17) {
  console.error(`Episodes index should render 17 episode summaries, found ${summaryCount}`);
  process.exit(1);
}
const feedXml = readFileSync(new URL('../feed.xml', import.meta.url), 'utf8');
for (const needle of [
  '<rss version="2.0"',
  'The Weekly Claw — Episode Summaries',
  '<atom:link href="https://weeklyclaw.ai/feed.xml"',
  'weeklyclaw-episode-26',
  'weeklyclaw-episode-10',
]) {
  if (!feedXml.includes(needle)) {
    console.error(`RSS feed missing expected marker: ${needle}`);
    process.exit(1);
  }
}
const feedItemCount = (feedXml.match(/<item>/g) ?? []).length;
if (feedItemCount !== 17) {
  console.error(`RSS feed should contain 17 items, found ${feedItemCount}`);
  process.exit(1);
}
const episodesJson = JSON.parse(readFileSync(new URL('../episodes.json', import.meta.url), 'utf8'));
if (episodesJson.episodes.length !== 17) {
  console.error(`episodes.json should contain 17 episodes, found ${episodesJson.episodes.length}`);
  process.exit(1);
}
const latest = episodesJson.episodes[0];
if (latest.week !== 26 || !latest.videoId || latest.summary.length < 3) {
  console.error('episodes.json latest episode entry is incomplete');
  process.exit(1);
}

const playerMarkers = [
  'class="episode-player"',
  'aria-label="Episode player mode"',
  'data-player-mode="video"',
  'data-player-mode="audio"',
  'data-player-mode="spotify"',
  'id="episode-video-frame"',
  'id="episode-audio"',
  'id="audio-unavailable"',
  'id="episode-spotify-frame"',
  'id="spotify-unavailable"',
  'https://open.spotify.com/embed/episode/${spotifyId}',
  'card.dataset.spotifyId',
  'data-spotify-id="2GywqAyfGJMXafRHRbdIa6"',
  'data-play-video',
  'https://www.youtube-nocookie.com/embed/',
  'cards.find(card => card.dataset.videoId)',
  "card === latestArchiveCard ? 'Latest episode' : 'From the archive'",
  'if (!card || !loadEpisode(card)) return;',
  'event.preventDefault()',
];
for (const marker of playerMarkers) {
  if (!episodesHtml.includes(marker)) {
    console.error(`Episodes index missing player integration marker: ${marker}`);
    process.exit(1);
  }
}

const homepagePlayerMarkers = [
  'id="featured-player"',
  'aria-label="Featured episode player mode"',
  'data-featured-mode="video"',
  'data-featured-mode="audio"',
  'id="featured-video-frame"',
  'id="featured-audio"',
  'id="featured-audio-unavailable"',
  'https://www.youtube-nocookie.com/embed/${featuredVideoId}',
  'featuredCard?.dataset.videoId',
];
for (const marker of homepagePlayerMarkers) {
  if (!html.includes(marker)) {
    console.error(`Homepage missing Featured Episode player marker: ${marker}`);
    process.exit(1);
  }
}
const featuredEpisode = html.match(/<div class="latest-card"[^>]*>/)?.[0] ?? '';
const featuredVideoId = featuredEpisode.match(/data-video-id="([\w-]{11})"/)?.[1];
const featuredAudioSrc = featuredEpisode.match(/data-audio-src="([^"]+)"/)?.[1];
const featuredWeek = html.match(/<div class="latest-number" aria-hidden="true">(\d+)<\/div>/)?.[1];
const featuredArchiveCard = html.match(new RegExp(`<article class="episode-card">[\\s\\S]*?<span class="episode-week">W${featuredWeek}</span>[\\s\\S]*?</article>`))?.[0] ?? '';
const archiveVideoId = featuredArchiveCard.match(/youtube\.com\/watch\?v=([\w-]{11})/)?.[1];
if (featuredVideoId !== archiveVideoId) {
  console.error('Homepage Featured Episode player does not match the latest episode card video');
  process.exit(1);
}
if (html.includes('autoplay=1')) {
  console.error('Homepage Featured Episode player must not autoplay');
  process.exit(1);
}
if (featuredAudioSrc && (!featuredAudioSrc.startsWith('/') || !existsSync(new URL(`..${featuredAudioSrc}`, import.meta.url)))) {
  console.error(`Homepage Featured Episode audio source does not resolve to a local asset: ${featuredAudioSrc}`);
  process.exit(1);
}
const featuredCopy = html.match(/<div class="latest-card"[\s\S]*?<div class="featured-player"/)?.[0] ?? '';
if (featuredCopy.includes('Open episode') || featuredCopy.includes('class="latest-action"')) {
  console.error('Homepage Featured Episode still exposes the obsolete slides-opening action');
  process.exit(1);
}

const episode22Card = episodesHtml.match(/<article class="week-card"[^>]*data-week="22"[^>]*>[\s\S]*?<\/article>/)?.[0] ?? '';
if (!episode22Card.includes('data-video-id="f2yugYwXOBo"')) {
  console.error('Episode 22 card is missing its verified YouTube video ID');
  process.exit(1);
}
if (!episode22Card.includes('href="https://www.youtube.com/watch?v=f2yugYwXOBo"')) {
  console.error('Episode 22 player controls need a direct YouTube fallback');
  process.exit(1);
}
if (!episode22Card.includes('<h3>The Sandbox Failed</h3>')) {
  console.error('Episode 22 card is missing its canonical title');
  process.exit(1);
}
if (!episode22Card.includes('/assets/youtube-thumbnails/w22-v2-the-sandbox-failed-approved-20260727.jpg')) {
  console.error('Episode 22 card is missing its approved thumbnail');
  process.exit(1);
}
if (episodesHtml.includes('autoplay=1')) {
  console.error('Episode player must not autoplay');
  process.exit(1);
}
const heroEnd = episodesHtml.indexOf('</section>', episodesHtml.indexOf('<section class="hero"'));
const playerStart = episodesHtml.indexOf('<section class="episode-player"');
const archiveStart = episodesHtml.indexOf('<section class="archive"');
if (!(heroEnd < playerStart && playerStart < archiveStart)) {
  console.error('Episode player must appear directly between the hero and archive');
  process.exit(1);
}

const homepageEpisodeWeeks = [...html.matchAll(/<span class="episode-week">W(\d+)<\/span>/g)]
  .map((match) => Number(match[1]));
const newestArchiveWeeks = [...episodesHtml.matchAll(/<span class="week-number">W(\d+)<\/span>/g)]
  .map((match) => Number(match[1]))
  .sort((a, b) => b - a)
  .slice(0, 6);
if (!html.includes('.archive-grid > .episode-card:nth-child(n + 7) { display: none; }')) {
  console.error('Homepage is missing the 6-episode display limit');
  process.exit(1);
}
const visibleHomepageWeeks = homepageEpisodeWeeks.slice(0, 6);
if (visibleHomepageWeeks.join(',') !== newestArchiveWeeks.join(',')) {
  console.error(`Homepage episode cards are not the newest 6 archive weeks: expected ${newestArchiveWeeks.map((week) => `W${week}`).join(', ')}, found ${visibleHomepageWeeks.map((week) => `W${week}`).join(', ')}`);
  process.exit(1);
}

for (const [name, page] of [['homepage', html], ['episodes index', episodesHtml]]) {
  for (const forbidden of ['>Agenda<', 'slides + agenda', 'Slides + agenda', 'full agenda', '/agenda">']) {
    if (page.includes(forbidden)) {
      console.error(`${name} still exposes removed agenda UI: ${forbidden}`);
      process.exit(1);
    }
  }
}

for (const path of ['../episodes/20/agenda.md', '../episodes/20/agenda/index.html']) {
  const agenda = readFileSync(new URL(path, import.meta.url), 'utf8');
  for (const marker of ['Build notes', 'WINNERS:', 'fill in the winner', 'template.md']) {
    if (agenda.includes(marker)) {
      console.error(`Episode 20 public agenda exposes an internal marker: ${marker}`);
      process.exit(1);
    }
  }
}

const legacyArchiveHtml = readFileSync(new URL('../weeklyclaw-archive.html', import.meta.url), 'utf8');
if (!legacyArchiveHtml.includes("window.location.replace('/episodes'") || !legacyArchiveHtml.includes('href="/episodes"')) {
  console.error('Legacy archive page does not redirect to /episodes');
  process.exit(1);
}

for (const [name, page] of [['homepage', html], ['episodes index', episodesHtml], ['legacy archive', legacyArchiveHtml], ['changelog index', changelogHtml], ['feedback page', feedbackHtml]]) {
  const htmlRoute = page.match(/(?:href|src|action|data-url)=["'][^"']*\.html(?:[?#][^"']*)?["']/);
  if (htmlRoute) {
    console.error(`${name} still exposes a public .html URL: ${htmlRoute[0]}`);
    process.exit(1);
  }
}

for (const week of [10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26]) {
  const mainDeck = readFileSync(new URL(`../episodes/${week}/deck.html`, import.meta.url), 'utf8');
  if (!mainDeck.includes('Weekly') && !mainDeck.includes('OpenClaw')) {
    console.error(`Week ${week} main deck does not look like a Weekly Claw deck`);
    process.exit(1);
  }
}

const archivedMainDeckCanaries = new Map([
  [11, ['The Weekly Claw #11', 'Friday, April 24, 2026', "That's <span class=\"gradient-text\">Episode 11"]],
  [18, ['The Weekly Claw #18', 'Skill Workshop is your homework', 'Host: Andy · @AndyML']],
]);
for (const [week, canaries] of archivedMainDeckCanaries) {
  const mainDeck = readFileSync(new URL(`../episodes/${week}/deck.html`, import.meta.url), 'utf8');
  for (const canary of canaries) {
    if (!mainDeck.includes(canary)) {
      console.error(`Week ${week} archived main deck is missing source canary: ${canary}`);
      process.exit(1);
    }
  }
}

for (const week of weeks) {
  const dir = join(root.pathname, `w${week}`, 'changelog');
  const files = readdirSync(dir);
  const slideCount = files.filter((name) => /^slide-\d+\.jpg$/.test(name)).length;
  if (slideCount === 0) {
    console.error(`Week ${week} has no copied slide JPGs`);
    process.exit(1);
  }
  const deck = readFileSync(join(dir, 'index.html'), 'utf8');
  if (!deck.includes('Weekly') && !deck.includes('OpenClaw')) {
    console.error(`Week ${week} changelog does not look like a Weekly Claw deck`);
    process.exit(1);
  }
  if (!deck.includes('name="weeklyclaw-route"') || !deck.includes(`/w${week}/changelog/`)) {
    console.error(`Week ${week} changelog is missing weeklyclaw-route metadata`);
    process.exit(1);
  }
  const shortRoute = readFileSync(new URL(`../w${week}/index.html`, import.meta.url), 'utf8');
  if (!shortRoute.includes(`/w${week}/changelog/`)) {
    console.error(`Week ${week} short route does not redirect to changelog`);
    process.exit(1);
  }
}

const vercelConfig = JSON.parse(readFileSync(new URL('../vercel.json', import.meta.url), 'utf8'));
for (const source of ['/episodes/:episode/agenda', '/episodes/:episode/agenda.md']) {
  const redirect = vercelConfig.redirects?.find((item) => item.source === source);
  if (!redirect || redirect.destination !== '/episodes?week=:episode&deck=main' || redirect.permanent !== true) {
    console.error(`Missing permanent agenda redirect: ${source}`);
    process.exit(1);
  }
}

console.log(`weeklyclaw-ai static validation passed (${weeks.length} changelog routes)`);
