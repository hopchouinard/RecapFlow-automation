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

const mkResponse = (content, finish, reasoningTokens) => ({
  json: {
    choices: [{ finish_reason: finish, message: { content } }],
    usage: {
      prompt_tokens: 100, completion_tokens: 400, cost: 0.001,
      completion_tokens_details: { reasoning_tokens: reasoningTokens },
    },
  },
});

const req = (over = {}) => ({
  stepName: 'prep', model: 'z-ai/glm-5.3-flash', system: 's', user: 'u',
  maxTokens: 32768, chunkIndex: 0, attempt: 1, ceiling: 131072, temperature: 0.3, ...over,
});

test('classify accepts a clean completion', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('hello world', 'stop', 10)],
    nodes: { 'Code: Normalize': [req()] },
  });
  assert.strictEqual(out[0].json.ok, true);
  assert.strictEqual(out[0].json.failureKind, null);
  assert.strictEqual(out[0].json.text, 'hello world');
});

test('classify flags reasoning burn when content is empty', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('', 'length', 399)],
    nodes: { 'Code: Normalize': [req()] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'reasoning_burn');
});

test('classify flags conventional truncation when content is cut', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('a partial sentence that just st', 'length', 0)],
    nodes: { 'Code: Normalize': [req()] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'content_truncated');
});

test('classify enforces the signal.reduce structural contract', () => {
  const good = ['general', 'insights', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  const okOut = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(good, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(okOut[0].json.ok, true);

  const badOut = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('## general\n\nbody', 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(badOut[0].json.ok, false);
  assert.strictEqual(badOut[0].json.failureKind, 'structure');
});

test('classify accepts H1 headings for signal.reduce', () => {
  const h1 = ['general', 'insights', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `# ${s}\n\nbody`).join('\n\n');
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(h1, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, true, 'H1 headings must be accepted (spec 4.6)');
});

test('classify rejects markdown in a post section', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('- **bold** bullet', 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'post.section' })] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('classify rejects an unclosed SEGMENT header in prep output', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('<!--SEGMENT\ntopic: x\nbody with no close', 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

const classified = (over = {}) => ({
  json: {
    chunkIndex: 0, stepName: 'prep', text: '', ok: false, failureKind: 'reasoning_burn',
    finishReason: 'length', attempts: 1, model: 'z-ai/glm-5.3-flash', maxTokens: 32768,
    temperature: 0.3, system: 's', user: 'u', ceiling: 131072, expect: 'none',
    usage: { promptTokens: 0, completionTokens: 0, reasoningTokens: 0, cost: 0 }, ...over,
  },
});

test('escalate forces low reasoning effort and 1.5x budget on attempt 2', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Escalate', { items: [classified()] });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.attempt, 2);
  assert.strictEqual(out[0].json.reasoningEffort, 'low');
  assert.strictEqual(out[0].json.maxTokens, Math.floor(32768 * 1.5));
});

test('escalate goes minimal and 2x on attempt 3', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Escalate', {
    items: [classified({ attempts: 2 })],
  });
  assert.strictEqual(out[0].json.attempt, 3);
  assert.strictEqual(out[0].json.reasoningEffort, 'minimal');
  assert.strictEqual(out[0].json.maxTokens, 32768 * 2);
});

test('escalate never exceeds the model ceiling', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Escalate', {
    items: [classified({ attempts: 2, maxTokens: 100000, ceiling: 131072 })],
  });
  assert.strictEqual(out[0].json.maxTokens, 131072);
});

test('escalate emits nothing once attempts are exhausted', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Escalate', {
    items: [classified({ attempts: 3 })],
  });
  assert.strictEqual(out.length, 0);
});

test('escalate passes over items that already succeeded', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Escalate', {
    items: [classified({ ok: true, failureKind: null, text: 'fine' })],
  });
  assert.strictEqual(out.length, 0);
});

test('collect orders by chunkIndex and keeps the best attempt per chunk', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Collect', {
    items: [
      classified({ chunkIndex: 1, ok: true, failureKind: null, text: 'second', attempts: 2 }),
      classified({ chunkIndex: 0, ok: true, failureKind: null, text: 'first' }),
      classified({ chunkIndex: 1, ok: false, text: '' }),
    ],
  });
  // Array.from: runCodeNode's vm.runInNewContext returns a cross-realm array;
  // deepStrictEqual on a cross-realm Array.prototype.map() result throws a
  // spurious "same structure but not reference-equal" error even when the
  // primitive contents match. Rehoming into the test's own realm avoids it.
  assert.deepStrictEqual(Array.from(out.map((i) => i.json.text)), ['first', 'second']);
  assert.strictEqual(out[1].json.ok, true);
});
