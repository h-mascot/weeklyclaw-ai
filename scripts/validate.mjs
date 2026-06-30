import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = new URL('..', import.meta.url);
const required = [
  'index.html',
  'changelog/index.html',
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
for (const needle of ['WeeklyClaw.ai', 'The Weekly Claw', 'OpenClaw Discord', '/changelog/', 'Episode deck', 'Changelog/DX deck', '/episodes/10/deck.html', '/episodes/12/deck.html', '/episodes/14/deck.html', '/episodes/19/deck.html', '/w12/changelog/', '/w14/changelog/', '/w18/changelog/', '/w19/changelog/']) {
  if (!html.includes(needle)) {
    console.error(`Missing expected copy: ${needle}`);
    process.exit(1);
  }
}

if (html.includes('superada.ai/weekly-claw') || html.includes('SuperAda edition') || html.includes('Short route')) {
  console.error('Homepage still contains stale SuperAda or Short route links');
  process.exit(1);
}

if (html.includes('Open changelog archive') || html.includes('Browse recent materials') || html.includes('Host deck') || html.includes('Main slides') || html.includes('Recent materials') || html.includes('show packets') || html.includes('this mirror') || html.includes('MascotM3')) {
  console.error('Homepage still contains low-value or duplicate CTA copy');
  process.exit(1);
}


if (html.includes('May 22, 2026 · Show deck + changelog/DX')) {
  console.error('Homepage still contains stale date/availability meta copy');
  process.exit(1);
}

if (!readFileSync(new URL('../README.md', import.meta.url), 'utf8').includes('/w19/changelog/')) {
  console.error('README is missing the W19 changelog route');
  process.exit(1);
}

const changelogHtml = readFileSync(new URL('../changelog/index.html', import.meta.url), 'utf8');
for (const needle of ['Release changelogs', '/w11/changelog/', '/w18/changelog/', '/w19/changelog/', '/episodes/12/deck.html', '/episodes/14/deck.html', '/episodes/19/deck.html', 'Episode deck', 'Changelog/DX deck']) {
  if (!changelogHtml.includes(needle)) {
    console.error(`Changelog index missing expected copy: ${needle}`);
    process.exit(1);
  }
}

if (changelogHtml.includes('Open changelog') || changelogHtml.includes('Host deck') || changelogHtml.includes('/episodes/19/host.html') || changelogHtml.includes('Main slides') || changelogHtml.includes('Changelog archive') || changelogHtml.includes('mirrored SuperAda') || changelogHtml.includes('short week routes')) {
  console.error('Changelog index still exposes low-value or duplicate CTA copy');
  process.exit(1);
}


for (const week of [10, 12, 13, 14, 15, 19]) {
  const mainDeck = readFileSync(new URL(`../episodes/${week}/deck.html`, import.meta.url), 'utf8');
  if (!mainDeck.includes('Weekly') && !mainDeck.includes('OpenClaw')) {
    console.error(`Week ${week} main deck does not look like a Weekly Claw deck`);
    process.exit(1);
  }
}

const week19HostDeck = readFileSync(new URL('../episodes/19/host.html', import.meta.url), 'utf8');
if (!week19HostDeck.includes('Host cue') || !week19HostDeck.includes('Weekly Claw #19')) {
  console.error('Week 19 host deck is missing expected host cue/content markers');
  process.exit(1);
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
