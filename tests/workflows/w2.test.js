const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode, loadWorkflow } = require('./harness');

const transcript = fs.readFileSync('/repo/output/2026-09-01/transcript.txt', 'utf8');
const signalText = fs.readFileSync('/repo/output/2026-09-01/extracted-signal.md', 'utf8');
// Finding D: W1's fixture above is `[HH:MM:SS] Speaker: text` (one line per utterance) --
// W2's real historical transcripts are turn BLOCKS (`HH:MM:SS - Speaker` header line +
// utterance lines + a blank-line separator). Use a REAL historical transcript for W2's
// splitter tests so they exercise the actual format, not W1's.
const historicalTranscript = fs.readFileSync(
  '/repo/historical/2026-01-14-ai-developer-accelerator-weekly-support-call-r114039427/transcript.md',
  'utf8',
);

const cfg = {
  steps: {
    prep:         { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, chunkTargetTokens: 15000 },
    signalMap:    { model: 'anthropic/claude-sonnet-5', maxTokens: 16384, chunkTargetTokens: 15000 },
    signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000 },
    postSection:  { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
    compress:     { model: 'z-ai/glm-5.3-flash',         maxTokens: 16384, reasoningEffort: 'low' },
    invite:       { model: 'z-ai/glm-5.3-flash',         maxTokens: 16384, reasoningEffort: 'low' },
  },
  retry: { callerHalvings: 2 },
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
      'Code: Read Transcript': { transcriptText: historicalTranscript },
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
      'Code: Read Transcript': { transcriptText: historicalTranscript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  const twice = runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { halving: 1 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Read Transcript': { transcriptText: historicalTranscript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(twice.length > once.length, 'halving must produce more, smaller chunks');
});

// Finding D: W2 reused W1's line-based splitter, which assumes one utterance per line.
// W2's real transcripts are turn BLOCKS (`HH:MM:SS - Speaker` header + utterance lines +
// blank-line separator) -- a line-based cut could land between a header and its body,
// leaving the next chunk starting with an unattributed utterance. Prove against a REAL
// historical transcript that (a) no chunk ends with a dangling speaker-header line, and
// (b) the concatenated chunks reproduce the source exactly (no content lost or duplicated).
const TURN_HEADER_RE = /^\d{2}:\d{2}:\d{2} - .+$/;

test('Finding D: W2 Split Prep chunks a real historical transcript on whole turn blocks only', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Read Transcript': { transcriptText: historicalTranscript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(out.length >= 2, `expected multiple chunks for a 258KB transcript, got ${out.length}`);
  for (const item of out) {
    const trimmed = item.json.user.replace(/\s+$/, '');
    const lastLine = trimmed.split('\n').pop();
    assert.ok(!TURN_HEADER_RE.test(lastLine),
      `chunk must not end with a dangling speaker header: "${lastLine}"`);
  }
  const reassembled = out.map((i) => i.json.user).join('');
  assert.strictEqual(reassembled, historicalTranscript,
    'concatenated chunks must reproduce the source transcript exactly');
});

test('Finding D: W2 Split Signal chunks a real historical transcript on whole turn blocks only', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Signal', {
    items: [{ json: { halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Read Transcript': { transcriptText: historicalTranscript },
    },
  });
  assert.ok(out.length >= 2, `expected multiple chunks for a 258KB transcript, got ${out.length}`);
  for (const item of out) {
    const trimmed = item.json.user.replace(/\s+$/, '');
    const lastLine = trimmed.split('\n').pop();
    assert.ok(!TURN_HEADER_RE.test(lastLine),
      `chunk must not end with a dangling speaker header: "${lastLine}"`);
  }
  const reassembled = out.map((i) => i.json.user).join('');
  assert.strictEqual(reassembled, historicalTranscript,
    'concatenated chunks must reproduce the source transcript exactly');
});

// W1's splitter is format-appropriate for its own line-per-utterance transcripts and must
// NOT be touched by Finding D -- assert W2's turn-block splitter never appears in W1.
test('Finding D: W1 Split Prep / Split Signal are untouched -- they still use splitTranscriptByLines, not the W2 turn-block splitter', () => {
  const wf = loadWorkflow('merged-call-summarizer.json');
  const byName = Object.fromEntries(wf.nodes.map((n) => [n.name, n]));
  for (const name of ['Code: Split Prep', 'Code: Split Signal']) {
    const code = byName[name].parameters.jsCode;
    assert.ok(code.includes('splitTranscriptByLines'), `${name} in W1 must keep its line-based splitter`);
    assert.ok(!code.includes('splitTranscriptByTurnBlocks'), `${name} in W1 must not adopt W2's turn-block splitter`);
  }
});

test('W2 aggregate prep throws when a chunk failed', () => {
  const items = [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, finishReason: 'length', text: '' } }];
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Prep', { items }), /failed/i);
});

test('Finding 4: W2 session header is built deterministically from the session date and last transcript timestamp, not trusted from chunk 1', () => {
  const items = [
    {
      json: {
        chunkIndex: 0, ok: true, usage: { cost: 0.01 },
        text: '=== SESSION ===\ndate: unspecified\nduration_estimate: ~45 minutes\nmain_themes: opening topic, shared topic\n\n---\n\n<!--SEGMENT\ntopic: a\n-->\nbody A',
      },
    },
    {
      json: {
        chunkIndex: 1, ok: true, usage: { cost: 0.02 },
        text: '=== SESSION ===\ndate: also wrong\nduration_estimate: ~10 minutes\nmain_themes: shared topic, later topic\n\n<!--SEGMENT\ntopic: b\n-->\nbody B',
      },
    },
  ];
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Prep', {
    items,
    nodes: {
      'Code: Read Transcript': { session_date: '2026-09-01', transcriptText: transcript },
    },
  });
  const md = out[0].json.preparedTranscript;
  assert.strictEqual((md.match(/=== SESSION ===/g) || []).length, 1, 'exactly one session header');
  assert.ok(md.includes('date: 2026-09-01'), 'date must come from the known session date, not chunk 1');
  assert.ok(md.includes('duration_estimate: 3h 15m'), 'duration must be computed from the transcript\'s last [HH:MM:SS] timestamp (03:15:43), not trusted from any chunk');
  assert.ok(md.includes('main_themes: opening topic; shared topic; later topic'), 'main_themes must merge and de-duplicate themes across all chunk headers, not just chunk 1\'s');
  assert.ok(md.includes('body A') && md.includes('body B'), 'chunk bodies must survive header replacement');
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

test('Finding 2: W2 reduce prompt requires all six headings always, not omission, so it cannot contradict the reduce validator', () => {
  const mapped = [
    { json: { chunkIndex: 0, ok: true, text: '## general\n\npart one', usage: { cost: 0.01 } } },
  ];
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes: signalNodes });
  const system = out[0].json.system;
  assert.ok(
    /Always emit all six headings.*even when a section has no content/s.test(system),
    'reduce prompt must instruct the model to always emit all six headings',
  );
  assert.ok(/_None\./.test(system), 'reduce prompt must give the model an explicit empty-section marker');
  assert.ok(
    !/Omit a section entirely if there is genuinely no content for it/.test(system),
    'reduce prompt must not contradict the CANON.every() reduce validator by telling the model it may omit a heading',
  );
});

test('Finding 2: W2 map prompt is unaffected — it may still omit a section, since its validator only requires one canonical heading', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Signal', {
    items: [{ json: { halving: 0 } }], nodes: signalNodes,
  });
  const system = out[0].json.system;
  assert.ok(
    /Omit a section entirely if this part contains nothing for it/.test(system),
    'map prompt legitimately keeps its omit-if-empty instruction',
  );
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

test('Finding B: W2 aggregate signal throws naming the offending heading when the reduce output has all six sections plus an extra one', () => {
  const withExtra = ['general', 'insights', 'qa', 'tools', 'links', 'decisions', 'bonus']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  assert.throws(
    () => runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Signal', {
      items: [{ json: { chunkIndex: 0, ok: true, text: withExtra, usage: { cost: 0 } } }],
    }),
    /non-canonical section heading\(s\): bonus/i,
  );
});

test('W2: Code: Save extracted-signal.md forwards signalText to Code: Split Post Sections', () => {
  // Ruling N regression seam: Code: Save extracted-signal.md must forward
  // signalText alongside the session context it spreads from Code: Read
  // Transcript, because Code: Split Post Sections reads $input.first().json.signalText
  // directly. Feed Split Post Sections the ACTUAL return value of the save
  // node (not a hand-written stub) so this seam is covered rather than assumed.
  const fsMock = makeFsMock();
  const saved = runCodeNode('transcript-only-summarizer.json', 'Code: Save extracted-signal.md', {
    items: [{ json: { signalText } }],
    nodes: { 'Code: Read Transcript': { outputDir: '/tmp/out/2025-09-01', session_id: '2025-09-01' } },
    fsMock,
  });
  assert.strictEqual(saved.json.signalText, signalText,
    'Code: Save extracted-signal.md must forward signalText downstream, not just spread session context');
  assert.strictEqual(saved.json.outputDir, '/tmp/out/2025-09-01',
    'the session fields already being spread must still be present');

  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Post Sections', {
    items: [saved],
    nodes: { 'Code: Pipeline Config': cfg },
  });
  assert.strictEqual(out.length, 6,
    'Split Post Sections must produce all six sections when fed the real Save-node output');
  assert.deepStrictEqual(Array.from(out, (i) => i.json.section),
    ['general', 'insights', 'qa', 'tools', 'links', 'decisions']);
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

// Controller Ruling Q: the 2026-09-01 live run of W1 proved that hand-written stubs miss
// field-name mismatches between a producing node and its consuming save node (Assemble Post
// emits communityPostText; the W1 save node had been reading $json.text). W2's save node was
// already correct, but nothing chained the real output through the harness to prove it and
// guard against regression. Do that here for W2 too.
test('Ruling Q: W2 Code: Assemble Post output chains into Code: Save community-post.md and is written verbatim', () => {
  const items = [
    { json: { chunkIndex: 0, ok: true, section: 'general', text: 'w2 summary body', usage: { cost: 0.001 } } },
    { json: { chunkIndex: 1, ok: true, section: 'insights', text: 'w2 insight body', usage: { cost: 0.002 } } },
  ];
  const assembled = runCodeNode('transcript-only-summarizer.json', 'Code: Assemble Post', { items });

  const fsMock = makeFsMock();
  const saved = runCodeNode('transcript-only-summarizer.json', 'Code: Save community-post.md', {
    items: assembled,
    nodes: { 'Code: Read Transcript': { outputDir: '/tmp/out/2025-09-01', session_id: '2025-09-01' } },
    fsMock,
  });

  const written = fsMock._files['/tmp/out/2025-09-01/community-post.md'];
  assert.strictEqual(typeof written, 'string', 'community-post.md must be written as a string, not undefined');
  assert.ok(written.length > 0, 'community-post.md must not be written empty');
  assert.ok(written.includes('w2 summary body') && written.includes('w2 insight body'));
  assert.strictEqual(saved.json.outputDir, '/tmp/out/2025-09-01');
});

test('Ruling Q: W2 Code: Save community-post.md refuses to write when handed no content', () => {
  const fsMock = makeFsMock();
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Save community-post.md', {
    items: [{ json: {} }],
    nodes: { 'Code: Read Transcript': { outputDir: '/tmp/out/2025-09-01', session_id: '2025-09-01' } },
    fsMock,
  }), /community-post\.md: refusing to write empty content/);
  assert.strictEqual(fsMock._files['/tmp/out/2025-09-01/community-post.md'], undefined,
    'no file should be written when content is missing');
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

// --- Controller Ruling M: chunked-node failures must reach the existing per-session
// failure path (state.failed) and let the backfill loop continue, instead of aborting
// the whole manual-trigger run. ---

function makeFsMock(initialState) {
  const files = {};
  if (initialState !== undefined) {
    files['/home/node/n8n-state/backfill-state.json'] = JSON.stringify(initialState);
  }
  return {
    existsSync: (p) => files[p] !== undefined,
    readFileSync: (p) => files[p],
    writeFileSync: (p, content) => { files[p] = content; },
    renameSync: (a, b) => { files[b] = files[a]; delete files[a]; },
    unlinkSync: (p) => { delete files[p]; },
    _files: files,
  };
}

test('W2: Aggregate Prep, Aggregate Signal, and Assemble Post are wired to continueErrorOutput', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const byName = Object.fromEntries(wf.nodes.map((n) => [n.name, n]));
  for (const name of ['Code: Aggregate Prep', 'Code: Aggregate Signal', 'Code: Assemble Post']) {
    assert.strictEqual(byName[name].onError, 'continueErrorOutput', `${name} must route its throw to the error output`);
    const targets = wf.connections[name].main;
    assert.strictEqual(targets.length, 2, `${name} must declare both a normal and an error output`);
    assert.ok(targets[1].length >= 1, `${name}'s error output must be wired somewhere`);
  }
});

test('W2: the three chunked nodes still throw on failure (errors are routed, not suppressed)', () => {
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Prep', {
    items: [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, finishReason: 'length', text: '' } }],
  }), /failed/i);
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Signal', {
    items: [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, text: '' } }],
  }), /failed/i);
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Assemble Post', {
    items: [{ json: { chunkIndex: 0, ok: false, section: 'general', failureKind: 'structure', attempts: 3, text: '' } }],
  }), /failed/i);
});

test('W2: Code: Record Pipeline Failure shapes a native error-output item into pipelineFailureMessage', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Record Pipeline Failure', {
    items: [{ json: {}, error: { message: 'Signal reduce failed after 3 attempts (failureKind=structure). No artifact written.' } }],
  });
  assert.strictEqual(out.json.pipelineFailureMessage, 'Signal reduce failed after 3 attempts (failureKind=structure). No artifact written.');
});

test('W2: Code: Record Pipeline Failure falls back to a generic message when no error is captured', () => {
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Record Pipeline Failure', {
    items: [{ json: {} }],
  });
  assert.ok(out.json.pipelineFailureMessage.length > 0);
});

test('W2 CRITICAL: a chunked-pipeline failure lands in state.failed and NOT in state.completed', () => {
  const fsMock = makeFsMock({ schema_version: '1', last_updated: null, completed: [], failed: [] });
  const shaped = runCodeNode('transcript-only-summarizer.json', 'Code: Record Pipeline Failure', {
    items: [{ json: {}, error: { message: 'Prep step failed on chunk 2 after 3 attempts (failureKind=structure, finishReason=stop). No artifact written.' } }],
  });
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Update State File', {
    items: [shaped],
    nodes: {
      'Code: Parse Session Meta': { session_id: '2025-09-01' },
      'Code: Read Transcript': { outputDir: '/tmp/out/2025-09-01' },
    },
    fsMock,
  });
  assert.strictEqual(out.json.ingest_status, 'pipeline_failed');

  const state = JSON.parse(fsMock._files['/home/node/n8n-state/backfill-state.json']);
  assert.strictEqual(state.failed.length, 1, 'the session must be recorded as failed');
  assert.strictEqual(state.failed[0].session_id, '2025-09-01');
  assert.ok(state.failed[0].reason.includes('Prep step failed on chunk 2'), 'the failure reason must preserve which chunk and failureKind caused it');
  assert.strictEqual(state.completed.length, 0, 'a failed session must NEVER be recorded as completed');
  assert.ok(!state.completed.some((c) => c.session_id === '2025-09-01'), 'a failed session must NEVER be recorded as completed');
});

test('W2 CRITICAL: a pipeline failure does not clobber an unrelated already-completed session', () => {
  const fsMock = makeFsMock({
    schema_version: '1',
    last_updated: null,
    completed: [{ session_id: '2025-01-01', completed_at: 't0', chunks_written: 10 }],
    failed: [],
  });
  const shaped = runCodeNode('transcript-only-summarizer.json', 'Code: Record Pipeline Failure', {
    items: [{ json: {}, error: { message: 'Community post section \'qa\' failed after 3 attempts (failureKind=structure). No artifact written.' } }],
  });
  runCodeNode('transcript-only-summarizer.json', 'Code: Update State File', {
    items: [shaped],
    nodes: {
      'Code: Parse Session Meta': { session_id: '2025-09-08' },
      'Code: Read Transcript': { outputDir: '/tmp/out/2025-09-08' },
    },
    fsMock,
  });
  const state = JSON.parse(fsMock._files['/home/node/n8n-state/backfill-state.json']);
  assert.strictEqual(state.completed.length, 1);
  assert.strictEqual(state.completed[0].session_id, '2025-01-01');
  assert.strictEqual(state.failed.length, 1);
  assert.strictEqual(state.failed[0].session_id, '2025-09-08');
});

test('W2: the loop-back edge to Split In Batches is intact from the error path', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const conns = wf.connections;
  // Trace: Code: Aggregate Prep (error) / Code: Aggregate Signal (error) / Code: Assemble Post
  // (error) -> Code: Record Pipeline Failure -> Code: Update State File -> Wait: Inter-session
  // Delay -> Split In Batches (same as the pre-existing success/ingest-failure path).
  for (const src of ['Code: Aggregate Prep', 'Code: Aggregate Signal', 'Code: Assemble Post']) {
    const errorTargets = conns[src].main[1].map((c) => c.node);
    assert.deepStrictEqual(errorTargets, ['Code: Record Pipeline Failure']);
  }
  assert.deepStrictEqual(conns['Code: Record Pipeline Failure'].main[0].map((c) => c.node), ['Code: Update State File']);
  assert.deepStrictEqual(conns['Code: Update State File'].main[0].map((c) => c.node), ['Wait: Inter-session Delay']);
  assert.deepStrictEqual(conns['Wait: Inter-session Delay'].main[0].map((c) => c.node), ['Split In Batches']);
});

test('Finding 1: W2 Check Chunks nodes are wired to continueErrorOutput, routed to Code: Record Pipeline Failure', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const byName = Object.fromEntries(wf.nodes.map((n) => [n.name, n]));
  for (const name of ['Code: Check Chunks', 'Code: Check Chunks (Signal)', 'Code: Check Chunks (Post)']) {
    assert.strictEqual(byName[name].onError, 'continueErrorOutput', `${name} must route its throw to the error output, or a single failing session aborts the whole backfill`);
    const targets = wf.connections[name].main;
    assert.strictEqual(targets.length, 2, `${name} must declare both a normal and an error output`);
    const errorTargets = targets[1].map((c) => c.node);
    assert.deepStrictEqual(errorTargets, ['Code: Record Pipeline Failure'], `${name}'s error output must reach the backfill failure path`);
  }
});

test('Finding 1: W2 Check Chunks nodes still throw on exhausted retries (errors are routed, not suppressed)', () => {
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Check Chunks', {
    items: [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, finishReason: 'length' } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Split Prep': { halving: 2 },
    },
  }), /failed/i);
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Check Chunks (Signal)', {
    items: [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, finishReason: 'length' } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Split Signal': { halving: 2 },
    },
  }), /failed/i);
  assert.throws(() => runCodeNode('transcript-only-summarizer.json', 'Code: Check Chunks (Post)', {
    items: [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, finishReason: 'length' } }],
    nodes: {
      'Code: Pipeline Config': cfg,
      'Code: Split Post Sections': { halving: 0 },
    },
  }), /failed/i);
});

test('Finding 1: W2 loop-back edge to Split In Batches is intact from the Check Chunks error path', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const conns = wf.connections;
  for (const src of ['Code: Check Chunks', 'Code: Check Chunks (Signal)', 'Code: Check Chunks (Post)']) {
    const errorTargets = conns[src].main[1].map((c) => c.node);
    assert.deepStrictEqual(errorTargets, ['Code: Record Pipeline Failure']);
  }
  assert.deepStrictEqual(conns['Code: Record Pipeline Failure'].main[0].map((c) => c.node), ['Code: Update State File']);
  assert.deepStrictEqual(conns['Code: Update State File'].main[0].map((c) => c.node), ['Wait: Inter-session Delay']);
  assert.deepStrictEqual(conns['Wait: Inter-session Delay'].main[0].map((c) => c.node), ['Split In Batches']);
});

test('Finding 1: W1 Check Chunks nodes are NOT given onError routing (single-run abort is intended)', () => {
  const wf = loadWorkflow('merged-call-summarizer.json');
  const byName = Object.fromEntries(wf.nodes.map((n) => [n.name, n]));
  for (const name of ['Code: Check Chunks', 'Code: Check Chunks (Signal)', 'Code: Check Chunks (Post)']) {
    assert.notStrictEqual(byName[name].onError, 'continueErrorOutput', `${name} in W1 must keep throwing unrouted — a single run should abort on failure`);
  }
});
