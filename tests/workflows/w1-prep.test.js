const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode } = require('./harness');

const transcript = fs.readFileSync('/repo/output/2026-09-01/transcript.txt', 'utf8');
const cfg = {
  steps: { prep: { model: 'z-ai/glm-5.3-flash', maxTokens: 32768, reasoningEffort: 'low', chunkTargetTokens: 15000 } },
  retry: { componentAttempts: 3, callerHalvings: 2 },
};

test('split emits one W3 request per chunk with prep config applied', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Validate and Check Partner': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(out.length >= 4 && out.length <= 7, `unexpected chunk count ${out.length}`);
  out.forEach((item, i) => {
    assert.strictEqual(item.json.stepName, 'prep');
    assert.strictEqual(item.json.model, 'z-ai/glm-5.3-flash');
    assert.strictEqual(item.json.reasoningEffort, 'low');
    assert.strictEqual(item.json.expect, 'prep.chunk');
    assert.strictEqual(item.json.chunkIndex, i);
    assert.ok(item.json.user.length > 0);
    assert.ok(item.json.system.includes('SEGMENT'), 'prep system prompt must survive');
  });
});

test('split halves the chunk target on a retry pass', () => {
  const once = runCodeNode('merged-call-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Validate and Check Partner': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  const twice = runCodeNode('merged-call-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 1 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Validate and Check Partner': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(twice.length > once.length, 'halving must produce more, smaller chunks');
});

test('aggregate joins chunks, hoists one header, merges unresolved speakers', () => {
  const items = [
    { json: { chunkIndex: 0, ok: true, text: '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: a\n-->\nbody A\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C', usage: { cost: 0.01 } } },
    { json: { chunkIndex: 1, ok: true, text: '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: b\n-->\nbody B\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C\n- Prem', usage: { cost: 0.02 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Prep', { items });
  const md = out[0].json.preparedTranscript;
  assert.strictEqual((md.match(/=== SESSION ===/g) || []).length, 1);
  assert.strictEqual((md.match(/- Ryan C/g) || []).length, 1);
  assert.ok(md.includes('body A') && md.includes('body B'));
  assert.strictEqual(out[0].json.chunkCount, 2);
  assert.ok(Math.abs(out[0].json.totalCost - 0.03) < 1e-9);
});

test('aggregate does not swallow a chunk body when it has no SEGMENT marker or trailing block', () => {
  const items = [
    { json: { chunkIndex: 0, ok: true, text: '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: a\n-->\nbody A', usage: { cost: 0.01 } } },
    { json: { chunkIndex: 1, ok: true, text: '=== SESSION ===\ndate: x\n\nbody B survives with no segment marker', usage: { cost: 0.02 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Prep', { items });
  assert.ok(out[0].json.preparedTranscript.includes('body B survives'), 'chunk body swallowed by SESSION header regex');
});

test('aggregate throws when any chunk failed, so nothing is written', () => {
  const items = [
    { json: { chunkIndex: 0, ok: true, text: 'fine', usage: { cost: 0 } } },
    { json: { chunkIndex: 1, ok: false, failureKind: 'reasoning_burn', text: '', attempts: 3, usage: { cost: 0 } } },
  ];
  assert.throws(
    () => runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Prep', { items }),
    /reasoning_burn|chunk 1|failed/i,
  );
});
