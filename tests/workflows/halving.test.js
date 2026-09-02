const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode } = require('./harness');

const cfg = { steps: {}, retry: { componentAttempts: 3, callerHalvings: 2 } };
const ok = (i) => ({ json: { chunkIndex: i, ok: true, text: 'fine', attempts: 1, usage: { cost: 0 } } });
const bad = (i) => ({ json: { chunkIndex: i, ok: false, failureKind: 'content_truncated', attempts: 3, text: '', usage: { cost: 0 } } });

for (const file of ['merged-call-summarizer.json', 'transcript-only-summarizer.json']) {
  test(`${file}: passes results through when every chunk succeeded`, () => {
    const out = runCodeNode(file, 'Code: Check Chunks', {
      items: [ok(0), ok(1)],
      nodes: { 'Code: Pipeline Config': cfg, 'Code: Split Prep': { halving: 0 } },
    });
    assert.strictEqual(out.length, 2);
    assert.strictEqual(out[0].json.retry, false);
  });

  test(`${file}: requests a halving when a chunk failed and budget remains`, () => {
    const out = runCodeNode(file, 'Code: Check Chunks', {
      items: [ok(0), bad(1)],
      nodes: { 'Code: Pipeline Config': cfg, 'Code: Split Prep': { halving: 0 } },
    });
    assert.strictEqual(out.length, 1);
    assert.strictEqual(out[0].json.retry, true);
    assert.strictEqual(out[0].json.halving, 1);
  });

  test(`${file}: throws once halvings are exhausted`, () => {
    assert.throws(
      () => runCodeNode(file, 'Code: Check Chunks', {
        items: [bad(0)],
        nodes: { 'Code: Pipeline Config': cfg, 'Code: Split Prep': { halving: 2 } },
      }),
      /No artifact written/,
    );
  });
}
