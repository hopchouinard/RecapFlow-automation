const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode, loadWorkflow } = require('./harness');

const cfg = {
  steps: {
    postSection: { model: 'z-ai/glm-5.3-flash', maxTokens: 16384, reasoningEffort: 'low' },
    compress:    { model: 'z-ai/glm-5.3-flash', maxTokens: 16384, reasoningEffort: 'low' },
    invite:      { model: 'z-ai/glm-5.3-flash', maxTokens: 16384, reasoningEffort: 'low' },
  },
  retry: { componentAttempts: 3, callerHalvings: 2 },
};
const signalText = fs.readFileSync('/repo/output/2026-09-01/extracted-signal.md', 'utf8');

test('splits the real extracted-signal into six section requests', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Split Post Sections', {
    items: [{ json: { signalText } }],
    nodes: { 'Code: Pipeline Config': cfg },
  });
  assert.strictEqual(out.length, 6);
  assert.deepStrictEqual(Array.from(out, (i) => i.json.section),
    ['general', 'insights', 'qa', 'tools', 'links', 'decisions']);
  for (const i of out) {
    assert.strictEqual(i.json.expect, 'post.section');
    assert.strictEqual(i.json.model, 'z-ai/glm-5.3-flash');
  }
});

test('omits sections absent from the input', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Split Post Sections', {
    items: [{ json: { signalText: '## general\n\nonly this one' } }],
    nodes: { 'Code: Pipeline Config': cfg },
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.section, 'general');
});

test('assembles sections in fixed order with the right emoji headers', () => {
  const items = [
    { json: { chunkIndex: 2, ok: true, section: 'qa', text: 'qa body', usage: { cost: 0 } } },
    { json: { chunkIndex: 0, ok: true, section: 'general', text: 'summary body', usage: { cost: 0 } } },
    { json: { chunkIndex: 1, ok: true, section: 'insights', text: 'insight body', usage: { cost: 0 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Assemble Post', { items });
  const post = out[0].json.communityPostText;
  assert.ok(post.indexOf('📝 SUMMARY') < post.indexOf('💡 KEY INSIGHTS'));
  assert.ok(post.indexOf('💡 KEY INSIGHTS') < post.indexOf('❓ KEY Q&A'));
  assert.ok(post.includes('summary body') && post.includes('qa body'));
});

test('assemble throws when a section failed', () => {
  const items = [{ json: { chunkIndex: 0, ok: false, section: 'general', failureKind: 'structure', attempts: 3, text: '' } }];
  assert.throws(() => runCodeNode('merged-call-summarizer.json', 'Code: Assemble Post', { items }), /failed/i);
});

test('build compress request carries the community post text and compress config', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Build Compress Request', {
    items: [{ json: { communityPostText: 'the assembled post' } }],
    nodes: { 'Code: Pipeline Config': cfg },
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.expect, 'none');
  assert.strictEqual(out[0].json.chunkIndex, 0);
  assert.strictEqual(out[0].json.model, 'z-ai/glm-5.3-flash');
  assert.ok(out[0].json.user.includes('the assembled post'));
  assert.ok(out[0].json.system.includes('Condense the community post'));
});

test('unwrap compress returns text and throws on failure', () => {
  const ok = runCodeNode('merged-call-summarizer.json', 'Code: Unwrap Compress', {
    items: [{ json: { ok: true, text: 'compressed', usage: { cost: 0.01 } } }],
  });
  assert.strictEqual(ok[0].json.text, 'compressed');

  assert.throws(() => runCodeNode('merged-call-summarizer.json', 'Code: Unwrap Compress', {
    items: [{ json: { ok: false, stepName: 'compress', failureKind: 'structure', attempts: 3, text: '' } }],
  }), /failed/i);
});

test('build invite request carries the compressed text, formatted date, and invite config', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Build Invite Request', {
    items: [{ json: { compressedText: 'last week post', formattedDate: 'September 9th' } }],
    nodes: { 'Code: Pipeline Config': cfg },
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.expect, 'none');
  assert.strictEqual(out[0].json.chunkIndex, 0);
  assert.strictEqual(out[0].json.model, 'z-ai/glm-5.3-flash');
  assert.ok(out[0].json.user.includes('last week post'));
  assert.ok(out[0].json.user.includes('September 9th'));
  assert.ok(out[0].json.system.includes('HOW THE CALLS WORK'));
});

test('unwrap invite returns text and throws on failure', () => {
  const ok = runCodeNode('merged-call-summarizer.json', 'Code: Unwrap Invite', {
    items: [{ json: { ok: true, text: 'invite text', usage: { cost: 0.01 } } }],
  });
  assert.strictEqual(ok[0].json.text, 'invite text');

  assert.throws(() => runCodeNode('merged-call-summarizer.json', 'Code: Unwrap Invite', {
    items: [{ json: { ok: false, stepName: 'invite', failureKind: 'structure', attempts: 3, text: '' } }],
  }), /failed/i);
});

// Controller Ruling B: the "no model slug leaks outside the config node" assertion,
// deferred out of Task 7, belongs here — this task deletes the last lmChatOpenRouter
// sub-nodes in this workflow.
test('no model slug leaks outside Code: Pipeline Config', () => {
  const wf = loadWorkflow('merged-call-summarizer.json');
  const slugPattern = /(z-ai\/|anthropic\/|moonshotai\/)/;
  for (const node of wf.nodes) {
    if (node.name === 'Code: Pipeline Config') continue;
    const serialized = JSON.stringify(node.parameters || {});
    assert.ok(!slugPattern.test(serialized), `model slug leaked into node '${node.name}': ${serialized.match(slugPattern)}`);
  }
});

test('zero chainLlm or lmChatOpenRouter nodes remain in W1', () => {
  const wf = loadWorkflow('merged-call-summarizer.json');
  const bad = wf.nodes.filter((n) => n.type.includes('chainLlm') || n.type.includes('lmChatOpenRouter'));
  assert.deepStrictEqual(bad.map((n) => n.name), []);
});
