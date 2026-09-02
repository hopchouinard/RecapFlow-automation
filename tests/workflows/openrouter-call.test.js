const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode } = require('./harness');

const base = { stepName: 'prep', model: 'z-ai/glm-5.3-flash', system: 's', user: 'u', maxTokens: 32768, chunkIndex: 0 };

test('normalize fills defaults and resolves the model ceiling', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Normalize', { items: [{ json: base }] });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.temperature, 0.3);
  assert.strictEqual(out[0].json.attempt, 1);
  assert.strictEqual(out[0].json.ceiling, 131072);
});

test('normalize resolves the Sonnet ceiling and preserves explicit temperature', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Normalize', {
    items: [{ json: { ...base, model: 'anthropic/claude-sonnet-5', temperature: 0 } }],
  });
  assert.strictEqual(out[0].json.ceiling, 128000);
  assert.strictEqual(out[0].json.temperature, 0);
});

test('normalize falls back to a safe ceiling for an unknown model', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Normalize', {
    items: [{ json: { ...base, model: 'someone/new-model' } }],
  });
  assert.strictEqual(out[0].json.ceiling, 32768);
});

test('normalize rejects an item missing a required field', () => {
  assert.throws(
    () => runCodeNode('openrouter-call.json', 'Code: Normalize', { items: [{ json: { stepName: 'x' } }] }),
    /missing required field/i,
  );
});
