const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode } = require('./harness');

const transcript = fs.readFileSync('/repo/output/2026-09-01/transcript.txt', 'utf8');
const cfg = {
  steps: {
    signalMap:    { model: 'anthropic/claude-sonnet-5', maxTokens: 16384, chunkTargetTokens: 15000 },
    signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000 },
  },
  retry: { callerHalvings: 2 },
};
const nodes = {
  'Code: Pipeline Config': cfg,
  'Code: Validate and Check Partner': { transcriptText: transcript, chatText: 'chat log here' },
};

test('signal map emits one request per chunk and excludes the chat log', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Split Signal', {
    items: [{ json: { halving: 0 } }], nodes,
  });
  assert.ok(out.length >= 4 && out.length <= 7);
  for (const item of out) {
    assert.strictEqual(item.json.stepName, 'signal.map');
    assert.strictEqual(item.json.expect, 'signal.map');
    assert.ok(!item.json.user.includes('chat log here'), 'chat log must not enter the map step');
  }
});

test('reduce request carries all chunk outputs plus the full chat log and a budget', () => {
  const mapped = [
    { json: { chunkIndex: 0, ok: true, text: '## general\n\npart one', usage: { cost: 0.01 } } },
    { json: { chunkIndex: 1, ok: true, text: '## general\n\npart two', usage: { cost: 0.01 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.expect, 'signal.reduce');
  assert.ok(out[0].json.user.includes('part one') && out[0].json.user.includes('part two'));
  assert.ok(out[0].json.user.includes('chat log here'), 'chat log must reach the reduce step');
  assert.ok(/8000/.test(out[0].json.system), 'reduce prompt must state its size budget');
});

test('reduce build throws if any map chunk failed', () => {
  const mapped = [{ json: { chunkIndex: 0, ok: false, failureKind: 'structure', attempts: 3, text: '' } }];
  assert.throws(() => runCodeNode('merged-call-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes }), /failed/i);
});

test('aggregate normalizes headings to H2 and requires all six sections', () => {
  const h1 = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'].map((s) => `# ${s}\n\nbody`).join('\n\n');
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Signal', {
    items: [{ json: { chunkIndex: 0, ok: true, text: h1, usage: { cost: 0.01 } } }],
  });
  const md = out[0].json.signalText;
  assert.ok(md.includes('## general'), 'headings must be normalized to H2');
  assert.ok(!/^# general/m.test(md));
  for (const s of ['insights', 'qa', 'tools', 'links', 'decisions']) assert.ok(md.includes(`## ${s}`));
});

test('aggregate throws when the reduce output is missing sections', () => {
  assert.throws(
    () => runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Signal', {
      items: [{ json: { chunkIndex: 0, ok: true, text: '## general\n\nonly one', usage: { cost: 0 } } }],
    }),
    /section/i,
  );
});

test('Finding B: aggregate throws naming the offending heading when the reduce output has all six sections plus an extra one', () => {
  const withExtra = ['general', 'insights', 'qa', 'tools', 'links', 'decisions', 'bonus']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  assert.throws(
    () => runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Signal', {
      items: [{ json: { chunkIndex: 0, ok: true, text: withExtra, usage: { cost: 0 } } }],
    }),
    /non-canonical section heading\(s\): bonus/i,
  );
});

test('Finding 2: reduce prompt requires all six headings always, not omission, so it cannot contradict the reduce validator', () => {
  const mapped = [
    { json: { chunkIndex: 0, ok: true, text: '## general\n\npart one', usage: { cost: 0.01 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes });
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

test('Finding 2: map prompt is unaffected — it may still omit a section, since its validator only requires one canonical heading', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Split Signal', {
    items: [{ json: { halving: 0 } }], nodes,
  });
  const system = out[0].json.system;
  assert.ok(
    /Omit a section entirely if this part contains nothing for it/.test(system),
    'map prompt legitimately keeps its omit-if-empty instruction',
  );
});

// R3-F: Code: Aggregate Signal used to check membership + count only (CANON.every(includes)
// plus found.length === CANON.length), not order. All six headings in the wrong order used
// to pass and get written as the extracted-signal artifact as-is.
test('R3-F: aggregate throws naming the actual order received when headings are all present but out of order', () => {
  const wrongOrder = ['insights', 'general', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  assert.throws(
    () => runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Signal', {
      items: [{ json: { chunkIndex: 0, ok: true, text: wrongOrder, usage: { cost: 0 } } }],
    }),
    /order|insights, general, qa/i,
  );
});

test('R3-F: aggregate still accepts the six canonical headings in the correct order', () => {
  const rightOrder = ['general', 'insights', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Signal', {
    items: [{ json: { chunkIndex: 0, ok: true, text: rightOrder, usage: { cost: 0 } } }],
  });
  assert.ok(out[0].json.signalText.includes('## general'));
});

// R3-I: Code: Build Signal Reduce used to concatenate every map part plus the whole chat
// log into ONE request with no size guard. Use a small configured contextLimit so we don't
// need megabyte-sized fixtures to exercise the guard.
test('R3-I: build signal reduce throws loudly when the assembled input exceeds the configured context-limit fraction', () => {
  const tinyLimitNodes = {
    ...nodes,
    'Code: Pipeline Config': {
      steps: {
        signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000, contextLimit: 1000 },
      },
      retry: { callerHalvings: 2 },
    },
  };
  // contextLimit 1000 * 0.5 fraction = 500 allowed tokens ~= 1800 chars. Force well past it.
  const huge = 'x'.repeat(5000);
  const mapped = [{ json: { chunkIndex: 0, ok: true, text: `## general\n\n${huge}`, usage: { cost: 0 } } }];
  assert.throws(
    () => runCodeNode('merged-call-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes: tinyLimitNodes }),
    /too large.*estimated.*tokens.*claude-sonnet-5.*1000-token context/is,
  );
});

test('R3-I: build signal reduce passes with large headroom for realistic call-sized material against the real production contextLimit', () => {
  // The real 2026-09-01 transcript plus a modest chat log, against claude-sonnet-5's
  // actual configured contextLimit (1,000,000, matching Code: Pipeline Config) and the
  // default 0.5 fraction -- this is the shape of material the guard must NOT block.
  const realLimitNodes = {
    ...nodes,
    'Code: Pipeline Config': {
      steps: {
        signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000, contextLimit: 1000000 },
      },
      retry: { callerHalvings: 2 },
    },
  };
  const mapped = [
    { json: { chunkIndex: 0, ok: true, text: `## general\n\n${transcript.slice(0, 8000)}`, usage: { cost: 0 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Build Signal Reduce', { items: mapped, nodes: realLimitNodes });
  assert.strictEqual(out.length, 1, 'realistic material must not trip the guard');
  const estimated = Math.ceil((out[0].json.system.length + out[0].json.user.length) / 3.6);
  const allowed = Math.floor(1000000 * 0.5);
  assert.ok(estimated < allowed, `expected well under the ${allowed}-token allowance, got ~${estimated}`);
});
