const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode } = require('./harness');

test('runs a real Code node from workflow JSON', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Calculate Next Tuesday', {
    json: { datePrefix: '2026-09-01', compressedText: 'x', outputDir: '/tmp/o' },
  });
  assert.strictEqual(out.json.inviteDate, '2026-09-08');
  assert.strictEqual(out.json.formattedDate, 'September 8th');
});

test('a Monday call still resolves to the next Tuesday', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Calculate Next Tuesday', {
    json: { datePrefix: '2026-08-31' },
  });
  assert.strictEqual(out.json.inviteDate, '2026-09-01');
});
