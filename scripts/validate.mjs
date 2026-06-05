import { readFileSync, existsSync } from 'node:fs';
const required = ['index.html','episodes/13/deck.html','episodes/13/agenda.md','episodes/15/deck.html','episodes/15/agenda.md'];
const missing = required.filter((p) => !existsSync(new URL(`../${p}`, import.meta.url)));
if (missing.length) {
  console.error(`Missing required files: ${missing.join(', ')}`);
  process.exit(1);
}
const html = readFileSync(new URL('../index.html', import.meta.url), 'utf8');
for (const needle of ['WeeklyClaw.ai', 'The Weekly Claw', 'superada.ai/weekly-claw', 'OpenClaw Discord']) {
  if (!html.includes(needle)) {
    console.error(`Missing expected copy: ${needle}`);
    process.exit(1);
  }
}
console.log('weeklyclaw-ai static validation passed');
