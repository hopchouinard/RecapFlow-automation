const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode, loadWorkflow } = require('./harness');

const transcript = fs.readFileSync('/repo/output/2026-09-01/transcript.txt', 'utf8');
const signalText = fs.readFileSync('/repo/output/2026-09-01/extracted-signal.md', 'utf8');

const cfg = {
  steps: {
    prep:         { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, chunkTargetTokens: 15000 },
    signalMap:    { model: 'anthropic/claude-sonnet-5', maxTokens: 16384, chunkTargetTokens: 15000 },
    signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000 },
    postSection:  { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
    compress:     { model: 'z-ai/glm-5.3-flash',         maxTokens: 16384, reasoningEffort: 'low' },
    invite:       { model: 'z-ai/glm-5.3-flash',         maxTokens: 16384, reasoningEffort: 'low' },
  },
  retry: { componentAttempts: 3, callerHalvings: 2 },
};

test('W2 config retires kimi and keeps sonnet for prep and signal', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Pipeline Config', {});
  const c = out[0].json;
  assert.strictEqual(c.steps.prep.model, 'anthropic/claude-sonnet-5');
  assert.strictEqual(c.steps.signalMap.model, 'anthropic/claude-sonnet-5');
  assert.strictEqual(c.steps.postSection.model, 'z-ai/glm-5.3-flash');
});

test('W2 has no chainLlm or model sub-nodes left', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const bad = wf.nodes.filter((n) => /chainLlm|lmChatOpenRouter/.test(n.type)).map((n) => n.name);
  assert.deepStrictEqual(bad, []);
});

test('W2 splits a transcript into prep requests against Code: Read Transcript', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Read Transcript': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(out.length >= 1);
  out.forEach((item, i) => {
    assert.strictEqual(item.json.stepName, 'prep');
    assert.strictEqual(item.json.model, 'anthropic/claude-sonnet-5');
    assert.strictEqual(item.json.expect, 'prep.chunk');
    assert.strictEqual(item.json.chunkIndex, i);
    assert.ok(item.json.system.includes('SEGMENT'), 'prep system prompt must survive');
  });
});

test('W2 split prep halves the chunk target on a retry pass', () => {
  const once = runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Read Transcript': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  const twice = runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { halving: 1 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Read Transcript': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(twice.length > once.length, 'halving must produce more, smaller chunks');
});

test('W2 aggregate prep throws when a chunk failed', () => {
  const items = [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, finishReason: 'length', text: '' } }];
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Prep', { items }), /failed/i);
});

const signalNodes = {
  'Code: Pipeline Config': cfg,
  'Code: Read Transcript': { transcriptText: transcript },
};

test('W2 signal map emits one request per chunk against Code: Read Transcript', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Signal', {
    items: [{ json: { halving: 0 } }], nodes: signalNodes,
  });
  assert.ok(out.length >= 1);
  for (const item of out) {
    assert.strictEqual(item.json.stepName, 'signal.map');
    assert.strictEqual(item.json.expect, 'signal.map');
  }
});

test('W2 signal reduce drops the ZOOM CHAT LOG block entirely (no chat log source)', () => {
  const mapped = [
    { json: { chunkIndex: 0, ok: true, text: '## general\n\npart one', usage: { cost: 0.01 } } },
    { json: { chunkIndex: 1, ok: true, text: '## general\n\npart two', usage: { cost: 0.01 } } },
  ];
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes: signalNodes });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.expect, 'signal.reduce');
  assert.ok(out[0].json.user.includes('part one') && out[0].json.user.includes('part two'));
  assert.ok(!out[0].json.user.includes('ZOOM CHAT LOG'), 'W2 has no chat log — the heading must not appear at all');
  assert.ok(/8000/.test(out[0].json.system), 'reduce prompt must state its size budget');
});

test('W2 signal reduce throws if any map chunk failed', () => {
  const mapped = [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, text: '' } }];
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes: signalNodes }), /failed/i);
});

test('W2 aggregate signal normalizes headings and requires all six sections', () => {
  const h1 = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'].map((s) => `# ${s}\n\nbody`).join('\n\n');
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Signal', {
    items: [{ json: { chunkIndex: 0, ok: true, text: h1, usage: { cost: 0.01 } } }],
  });
  const md = out[0].json.signalText;
  assert.ok(md.includes('## general'));
  for (const s of ['insights', 'qa', 'tools', 'links', 'decisions']) assert.ok(md.includes(`## ${s}`));
});

test('W2 aggregate signal throws when a required section is missing', () => {
  const partial = ['general', 'insights'].map((s) => `## ${s}\n\nbody`).join('\n\n');
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Signal', {
    items: [{ json: { chunkIndex: 0, ok: true, text: partial, usage: { cost: 0 } } }],
  }), /missing required section/i);
});

test('W2 splits the real extracted-signal into six section requests', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Post Sections', {
    items: [{ json: { signalText } }],
    nodes: { 'Code: Pipeline Config': cfg },
  });
  assert.strictEqual(out.length, 6);
  assert.deepStrictEqual(Array.from(out, (i) => i.json.section),
    ['general', 'insights', 'qa', 'tools', 'links', 'decisions']);
  for (const i of out) {
    assert.strictEqual(i.json.expect, 'post.section');
    assert.strictEqual(i.json.model, 'z-ai/glm-5.3-flash');
    assert.ok(i.json.system.includes('transcript-only') || i.json.system.includes('no chat log'),
      'W2 section prompt must acknowledge the transcript-only source');
  }
});

test('W2 assembles post sections in fixed order with the right emoji headers', () => {
  const items = [
    { json: { chunkIndex: 2, ok: true, section: 'qa', text: 'qa body', usage: { cost: 0 } } },
    { json: { chunkIndex: 0, ok: true, section: 'general', text: 'summary body', usage: { cost: 0 } } },
    { json: { chunkIndex: 1, ok: true, section: 'insights', text: 'insight body', usage: { cost: 0 } } },
  ];
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Assemble Post', { items });
  const post = out[0].json.communityPostText;
  assert.ok(post.indexOf('📝 SUMMARY') < post.indexOf('💡 KEY INSIGHTS'));
  assert.ok(post.indexOf('💡 KEY INSIGHTS') < post.indexOf('❓ KEY Q&A'));
  assert.ok(post.includes('summary body') && post.includes('qa body'));
});

test('W2 assemble post throws when a section failed', () => {
  const items = [{ json: { chunkIndex: 0, ok: false, section: 'general', failureKind: 'structure', attempts: 3, text: '' } }];
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Assemble Post', { items }), /failed/i);
});

// Controller Ruling B: the "no model slug leaks outside the config node" assertion,
// deferred out of Task 7, belongs here — this task deletes the last lmChatOpenRouter
// sub-nodes in W2.
test('no model slug leaks outside Code: Pipeline Config in W2', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const slugPattern = /(z-ai\/|anthropic\/|moonshotai\/)/;
  for (const node of wf.nodes) {
    if (node.name === 'Code: Pipeline Config') continue;
    const serialized = JSON.stringify(node.parameters || {});
    assert.ok(!slugPattern.test(serialized), `model slug leaked into node '${node.name}': ${serialized.match(slugPattern)}`);
  }
});

test('moonshotai/kimi is gone from W2 entirely', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const serialized = JSON.stringify(wf);
  assert.ok(!/moonshotai|kimi/i.test(serialized), 'kimi must not appear anywhere in W2');
});
