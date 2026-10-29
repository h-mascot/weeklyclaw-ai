import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(process.argv[2] || fileURLToPath(new URL('..', import.meta.url)));
const excluded = new Set(['.git', '.vercel', 'node_modules', 'showprep', 'model-context-dump', 'tmp', 'dist']);
const tag = '<script defer src="https://analytics.henrymascot.com/script.js" data-website-id="d3a6d170-e9f1-4301-a801-50ce6aadcaf1" data-tag="WeeklyClaw"></script>';
let updated = 0;
function visit(directory) {
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory() && !excluded.has(entry.name)) visit(path);
    else if (entry.isFile() && entry.name.endsWith('.html')) {
      const html = readFileSync(path, 'utf8');
      if (!/<head\b/i.test(html) || !/<\/head>/i.test(html)) continue;
      if (html.includes('data-website-id=')) {
        if (!html.includes('data-website-id="d3a6d170-e9f1-4301-a801-50ce6aadcaf1"')) throw new Error(`Unexpected analytics website ID in ${path}`);
        continue;
      }
      writeFileSync(path, html.replace(/<\/head>/i, `${tag}</head>`));
      updated++;
    }
  }
}
visit(root);
console.log(`Umami tracking: ${updated} public HTML pages updated`);
