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
  'episodes/10/deck.html',
  'episodes/12/deck.html',
  'episodes/13/deck.html',
  'episodes/13/agenda.md',
  'episodes/14/deck.html',
  'episodes/15/deck.html',
  'episodes/15/agenda.md',
  'episodes/19/deck.html',
  'episodes/19/host.html',
  'episodes/19/viewer-agenda.md',
  'episodes/19/host-agenda.md',
  'episodes/20/agenda.md',
  'episodes/20/agenda/index.html',
  'episodes/20/deck.html',
  'episodes/21/agenda.md',
  'episodes/21/agenda/index.html',
  'episodes/21/deck.html',
  'w18/changelog/index.html', 'w19/changelog/index.html'];

const weeks = [11, 12, 13, 14, 15, 16, 17, 18, 19];
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
  'Weekly Claw',
  'The cost of intelligence collapsed',
  '/feedback',
  'https://www.youtube.com/watch?v=dquJyEBQWpE',
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
  'action="https://weeklyclaw.beehiiv.com/create"',
  'name="sent_from_orchid" value="true"',
  'id="newsletter"',
  'class="social-icon"',
  'aria-label="Follow Weekly Claw on X"',
  'aria-label="Watch Weekly Claw on YouTube"',
]) {
  if (!html.includes(needle)) {
    console.error(`Missing expected homepage copy: ${needle}`);
    process.exit(1);
  }
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
for (const needle of ['Release changelogs', '/w11/changelog/', '/w18/changelog/', '/w19/changelog/', '/episodes/12/deck', '/episodes/14/deck', '/episodes/19/deck', 'Episode deck', 'Changelog/DX deck']) {
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
for (const needle of ['Weekly Claw Episodes', 'W21', '/episodes/21/deck', '/episodes/21/agenda', '<strong>12</strong>', 'archived episodes']) {
  if (!episodesHtml.includes(needle)) {
    console.error(`Episodes index missing expected copy: ${needle}`);
    process.exit(1);
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

for (const week of [10, 12, 13, 14, 15, 19, 20, 21]) {
  const mainDeck = readFileSync(new URL(`../episodes/${week}/deck.html`, import.meta.url), 'utf8');
  if (!mainDeck.includes('Weekly') && !mainDeck.includes('OpenClaw')) {
    console.error(`Week ${week} main deck does not look like a Weekly Claw deck`);
    process.exit(1);
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

console.log(`weeklyclaw-ai static validation passed (${weeks.length} changelog routes)`);