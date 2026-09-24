const { test } = require('node:test');
const assert = require('node:assert');
const { loadWorkflow, runCodeNode } = require('./harness');

const CANON = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'];
const response = (content) => ({
  json: { choices: [{ finish_reason: 'stop', message: { content } }] },
});
const request = (expect) => ({
  stepName: 'review', model: 'fixture', system: 's', user: 'u',
  maxTokens: 4000, chunkIndex: 0, attempt: 1, expect,
});

test('review: reducer rejects a fenced document with introductory prose', () => {
  const fence = String.fromCharCode(96).repeat(3);
  const document = CANON.map((slug) => '## ' + slug + '\n\nbody').join('\n\n');
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [response('Here is the result:\n' + fence + 'markdown\n' + document + '\n' + fence)],
    nodes: { 'Code: Normalize': [request('signal.reduce')] },
  });
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('review: prep rejects prose before its first segment but accepts session metadata', () => {
  const segment = '<!--SEGMENT\ntopic: Testing\nspeakers: A\nkeywords: qa\nsummary: A test\n-->\n'
    + 'A real transcript body with enough words to satisfy the minimum length check.';
  const metadata = '=== SESSION ===\ndate: 2026-09-01\nduration_estimate: 1h\nmain_themes: testing\n\n';
  const classify = (text) => runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [response(text)], nodes: { 'Code: Normalize': [request('prep.chunk')] },
  })[0].json;
  assert.strictEqual(classify(metadata + segment).ok, true);
  assert.strictEqual(classify(metadata + 'Unsegmented transcript text was here.\n' + segment).failureKind, 'structure');
});

test('review: title-case H1 and H3 reducer headings become canonical H2 in both workflows', () => {
  const text = CANON.map((slug, i) => (i % 2 ? '### ' : '# ')
    + slug[0].toUpperCase() + slug.slice(1) + '\n\nbody').join('\n\n');
  const classified = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [response(text)], nodes: { 'Code: Normalize': [request('signal.reduce')] },
  });
  assert.strictEqual(classified[0].json.ok, true);
  for (const workflow of ['merged-call-summarizer.json', 'transcript-only-summarizer.json']) {
    const out = runCodeNode(workflow, 'Code: Aggregate Signal', {
      items: [{ json: { ok: true, text, usage: { cost: 0 } } }],
    });
    assert.strictEqual(out[0].json.signalText,
      CANON.map((slug) => '## ' + slug + '\n\nbody').join('\n\n'));
  }
});

test('review: W2 reduce-size and empty-transcript failures follow the per-session error path', () => {
  const workflow = loadWorkflow('transcript-only-summarizer.json');
  const byName = Object.fromEntries(workflow.nodes.map((node) => [node.name, node]));
  for (const name of ['Code: Build Signal Reduce', 'Code: Split Prep']) {
    assert.strictEqual(byName[name].onError, 'continueErrorOutput');
    assert.deepStrictEqual(workflow.connections[name].main[1].map((edge) => edge.node),
      ['Code: Record Pipeline Failure']);
  }
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': { steps: { prep: {} } },
      'Code: Read Transcript': { transcriptText: '' },
    },
  }), /Historical transcript is empty/);
  assert.deepStrictEqual(workflow.connections['Code: Record Pipeline Failure'].main[0].map((edge) => edge.node),
    ['Code: Update State File']);
  assert.deepStrictEqual(workflow.connections['Code: Update State File'].main[0].map((edge) => edge.node),
    ['Wait: Inter-session Delay']);
  assert.deepStrictEqual(workflow.connections['Wait: Inter-session Delay'].main[0].map((edge) => edge.node),
    ['Split In Batches']);
});

test('review: successful W2 retry clears the pipeline error log and failed state', () => {
  const files = {
    '/home/node/n8n-state/backfill-state.json': JSON.stringify({
      schema_version: '1', completed: [], failed: [],
    }),
  };
  const fsMock = {
    existsSync: (path) => files[path] !== undefined,
    readFileSync: (path) => files[path],
    writeFileSync: (path, content) => { files[path] = content; },
    renameSync: (from, to) => { files[to] = files[from]; delete files[from]; },
    unlinkSync: (path) => { delete files[path]; },
  };
  const nodes = {
    'Code: Parse Session Meta': { session_id: '2026-09-01' },
    'Code: Read Transcript': { outputDir: '/tmp/out/2026-09-01' },
  };
  const run = (body) => runCodeNode('transcript-only-summarizer.json',
    'Code: Update State File', { items: [{ json: body }], nodes, fsMock });
  run({ pipelineFailureMessage: 'first run failed' });
  const log = '/tmp/out/2026-09-01/pipeline-error.log';
  assert.ok(files[log]);
  run({ chunks_written: 12, chunks_failed: 0 });
  const state = JSON.parse(files['/home/node/n8n-state/backfill-state.json']);
  assert.strictEqual(files[log], undefined);
  assert.strictEqual(state.failed.length, 0);
  assert.strictEqual(state.completed.length, 1);
});
