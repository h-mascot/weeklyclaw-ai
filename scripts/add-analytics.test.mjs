import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';
test('build adds one deferred tracker to static and generated public pages and preserves content', () => {
  const root = mkdtempSync(join(tmpdir(), 'weeklyclaw-analytics-'));
  const pages = ['index.html', 'episodes/35/index.html', 'episodes/35/deck.html', 'timeline/index.html'];
  const excluded = ['episodes/27/showprep/qa/private.html', 'episodes/28/model-context-dump/output/deck.html', 'node_modules/fixture/index.html'];
  const html = '<!doctype html><html><head><title>Keep me</title></head><body>Same content</body></html>';
  try {
    for (const page of [...pages, ...excluded]) {
      mkdirSync(join(root, page, '..'), { recursive: true });
      writeFileSync(join(root, page), html);
    }
    const run = () => execFileSync(process.execPath, [new URL('./add-analytics.mjs', import.meta.url).pathname, root]);
    run();
    const first = pages.map(page => readFileSync(join(root, page), 'utf8'));
    run();
    for (const [i, page] of pages.entries()) {
      const output = readFileSync(join(root, page), 'utf8');
      assert.equal(output, first[i], 'second build must not duplicate tags');
      const tags = output.match(/<script\b[^>]*data-website-id[^>]*><\/script>/g) || [];
      assert.equal(tags.length, 1);
      assert.ok(tags[0].includes('defer'));
      assert.ok(tags[0].includes('d3a6d170-e9f1-4301-a801-50ce6aadcaf1'));
      assert.equal(output.replace(tags[0], ''), html);
      assert.ok(output.indexOf(tags[0]) < output.indexOf('</head>'));
    }
    for (const page of excluded) assert.equal(readFileSync(join(root, page), 'utf8'), html);
  } finally { rmSync(root, { recursive: true, force: true }); }
});
