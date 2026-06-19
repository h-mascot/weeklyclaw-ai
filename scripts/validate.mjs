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
];

const weeks = [11, 12, 13, 14, 15, 16, 17, 18];
for (const week of weeks) {
  required.push(`w${week}/index.html`, `w${week}/changelog/index.html`);
}

const missing = required.filter((p) => !existsSync(new URL(`../${p}`, import.meta.url)));
if (missing.length) {
  console.error(`Missing required files: ${missing.join(', ')}`);
  process.exit(1);
}

const html = readFileSync(new URL('../index.html', import.meta.url), 'utf8');
for (const needle of ['WeeklyClaw.ai', 'The Weekly Claw', 'OpenClaw Discord', '/changelog/', 'Main slides', '/episodes/10/deck.html', '/episodes/12/deck.html', '/episodes/14/deck.html', '/w12/changelog/', '/w14/changelog/', '/w18/changelog/']) {
  if (!html.includes(needle)) {
    console.error(`Missing expected copy: ${needle}`);
    process.exit(1);
  }
}

if (html.includes('superada.ai/weekly-claw') || html.includes('SuperAda edition') || html.includes('Short route')) {
  console.error('Homepage still contains stale SuperAda or Short route links');
  process.exit(1);
}

const changelogHtml = readFileSync(new URL('../changelog/index.html', import.meta.url), 'utf8');
for (const needle of ['Changelog archive', '/w11/changelog/', '/w18/changelog/', '/episodes/12/deck.html', '/episodes/14/deck.html', 'Main slides']) {
  if (!changelogHtml.includes(needle)) {
    console.error(`Changelog index missing expected copy: ${needle}`);
    process.exit(1);
  }
}


for (const week of [10, 12, 13, 14, 15]) {
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
  const shortRoute = readFileSync(new URL(`../w${week}/index.html`, import.meta.url), 'utf8');
  if (!shortRoute.includes(`/w${week}/changelog/`)) {
    console.error(`Week ${week} short route does not redirect to changelog`);
    process.exit(1);
  }
}

console.log(`weeklyclaw-ai static validation passed (${weeks.length} changelog routes)`);
