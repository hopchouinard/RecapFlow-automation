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

// Finding B: community_brain.ingestion.parser.parse_extracted_signal RAISES on ANY
// non-canonical heading. The old validator called parseSections, which FILTERS
// non-canonical slugs before checking CANON.every(...), so a document with all six
// canonical headings PLUS a stray seventh used to pass here and then fail /ingest
// every single time. The validator must require EXACTLY the six canonical slugs.
test('classify rejects signal.reduce output with all six canonical headings plus an extra non-canonical one (Finding B)', () => {
  const good = ['general', 'insights', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  const withExtra = `${good}\n\n## bonus\n\nan extra section the model was not asked for`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(withExtra, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'an extra heading must be rejected, not silently stripped');
  assert.strictEqual(out[0].json.failureKind, 'structure');
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

// Finding 3: a well-formed SEGMENT header with no real transcript body after it used to
// pass structureOk (opens > 0 && opens === closes), get written as a successful prepared
// transcript, and then have that portion of the call silently dropped downstream by the
// ingestion parser. The validator must also require a non-trivial body per segment.
const longBody = 'x'.repeat(60); // well over the 50-non-whitespace-char threshold

// Full four-field header matching community_brain.ingestion.parser._SEGMENT_HEADER_RE
// exactly: topic, speakers, keywords, summary, in that order.
const fullHeader = (topic) =>
  `<!--SEGMENT\ntopic: ${topic}\nspeakers: A, B\nkeywords: k1, k2\nsummary: a summary\n-->`;

test('classify rejects a well-formed SEGMENT header with an empty body (Finding 3)', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(`${fullHeader('x')}\n`, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('classify rejects a SEGMENT header with only whitespace/punctuation after it (Finding 3)', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(`${fullHeader('x')}\n\n   ...\n`, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('classify accepts a SEGMENT header followed by a real transcript body (Finding 3)', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(`${fullHeader('x')}\n${longBody}\n`, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, true);
});

test('classify rejects a multi-segment response when only one segment has a real body (Finding 3)', () => {
  const text = `${fullHeader('a')}\n${longBody}\n${fullHeader('b')}\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false);
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('classify accepts a multi-segment response when every segment has a real body (Finding 3)', () => {
  const text = `${fullHeader('a')}\n${longBody}\n${fullHeader('b')}\n${longBody}\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, true);
});

// Finding A: the parser's _SEGMENT_HEADER_RE requires topic/speakers/keywords/summary,
// in that exact order, or the whole segment is silently dropped at ingestion. The old
// validator only counted markers and body length — a header missing a field, or with
// fields reordered, used to sail through. It must now be rejected.
test('classify rejects a SEGMENT header missing the keywords field (Finding A)', () => {
  const text = `<!--SEGMENT\ntopic: x\nspeakers: A, B\nsummary: a summary\n-->\n${longBody}\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'a header missing a required field must not pass');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('classify rejects a SEGMENT header with fields out of order (Finding A)', () => {
  const text = `<!--SEGMENT\ntopic: x\nkeywords: k1, k2\nspeakers: A, B\nsummary: a summary\n-->\n${longBody}\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'a header with fields out of order must not pass — the parser requires the exact order');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('classify accepts a full four-field SEGMENT header in the exact parser order (Finding A)', () => {
  const text = `${fullHeader('x')}\n${longBody}\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, true);
});

// ---------------------------------------------------------------------------
// Round-3 Codex review findings (labeled R3-A .. R3-I to avoid colliding with
// the pre-existing "Finding A"/"Finding B" labels from earlier rounds, which
// name different bugs).
// ---------------------------------------------------------------------------

const sixHeadings = (bodyFor = (s) => 'body') =>
  ['general', 'insights', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `## ${s}\n\n${bodyFor(s)}`).join('\n\n');

// R3-A: parser._strip_fenced_code runs BEFORE splitting on '##', so a reducer/map
// response wrapped whole in a ```fence``` still looks structurally valid to a naive
// heading scan, but the parser strips the fence first and finds ZERO sections.
test('R3-A: classify rejects signal.reduce output wrapped whole in a code fence', () => {
  const fenced = '```markdown\n' + sixHeadings() + '\n```';
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(fenced, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'a fenced reduce response must be rejected, not silently unwrapped');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('R3-A: classify rejects signal.map output wrapped whole in a code fence', () => {
  const fenced = '```markdown\n## general\n\nbody\n```';
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(fenced, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.map' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'a fenced map response must be rejected, not silently unwrapped');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('R3-A: classify still accepts an unfenced signal.reduce response with all six headings', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(sixHeadings(), 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, true);
});

// R3-B: parseAllHeadingSlugs used to require the ENTIRE heading line be one lowercase
// word ('^#{1,3}[ \t]+([a-z]+)[ \t]*$'), so '## Appendix Notes' was invisible to it --
// the count stayed at 6 and the response was accepted, then the parser split on every
// '##', lowercased the first word, and raised on 'appendix'.
test('R3-B: classify rejects a signal.reduce response with a multi-word extra heading the old regex could not see', () => {
  const withHiddenExtra = `${sixHeadings()}\n\n## Appendix Notes\n\nsome extra content`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(withHiddenExtra, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'a multi-word extra heading must be caught, not invisible to the count');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

// R3-C: parse_prepared_transcript strips '=== UNRESOLVED SPEAKERS ===' from a segment body
// BEFORE testing whether the body is empty, and skips empty segments. The old
// MIN_BODY_CHARS check counted that footer, so a final segment with no transcript but a
// long unresolved-speaker list passed here and was then silently dropped by the parser.
test('R3-C: classify rejects a SEGMENT whose only body content is the unresolved-speakers footer', () => {
  const text = `${fullHeader('x')}\n\n=== UNRESOLVED SPEAKERS ===\n- Speaker Nine\n- Speaker Ten\n- Speaker Eleven\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'a body that is only the unresolved-speakers footer must not pass');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('R3-C: classify accepts a SEGMENT with a real body even when followed by the unresolved-speakers footer', () => {
  const text = `${fullHeader('x')}\n${longBody}\n\n=== UNRESOLVED SPEAKERS ===\n- Speaker Nine\n`;
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(text, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'prep.chunk' })] },
  });
  assert.strictEqual(out[0].json.ok, true, 'real body content before the footer must still be counted');
});

// R3-F: the reduce check used to be membership + count only (CANON.every(includes) plus
// found.length === CANON.length), not order. All six headings in the wrong order used to
// pass and get written to disk as-is.
test('R3-F: classify rejects a signal.reduce response with all six canonical headings in the wrong order', () => {
  const wrongOrder = ['insights', 'general', 'qa', 'tools', 'links', 'decisions']
    .map((s) => `## ${s}\n\nbody`).join('\n\n');
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(wrongOrder, 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, false, 'headings out of order must be rejected');
  assert.strictEqual(out[0].json.failureKind, 'structure');
});

test('R3-F: classify accepts the six canonical headings in the exact canonical order', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse(sixHeadings(), 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ expect: 'signal.reduce' })] },
  });
  assert.strictEqual(out[0].json.ok, true);
});

test('Finding 3: the prep.chunk structureOk logic is byte-identical across Classify, Classify 2 and Classify 3', () => {
  const { loadWorkflow } = require('./harness');
  const wf = loadWorkflow('openrouter-call.json');
  const byName = Object.fromEntries(wf.nodes.map((n) => [n.name, n]));
  const extractStructureOk = (code) => {
    const start = code.indexOf('function structureOk');
    const end = code.indexOf('\n\nconst requests');
    assert.ok(start > -1 && end > start, 'structureOk function must be present and locatable');
    return code.slice(start, end);
  };
  const a = extractStructureOk(byName['Code: Classify'].parameters.jsCode);
  const b = extractStructureOk(byName['Code: Classify 2'].parameters.jsCode);
  const c = extractStructureOk(byName['Code: Classify 3'].parameters.jsCode);
  assert.strictEqual(a, b, 'Classify and Classify 2 structureOk must be byte-identical');
  assert.strictEqual(b, c, 'Classify 2 and Classify 3 structureOk must be byte-identical');
});

// Controller Ruling R: Code: Classify used to rebuild its output from an explicit field
// whitelist, silently dropping any caller-supplied metadata (e.g. Code: Split Post Sections'
// `section` field) that wasn't on the list. This is exactly the pattern from Ruling N and
// Ruling Q — a node rebuilding an object instead of forwarding what it didn't need to touch.
// Prove a caller-supplied field (and an arbitrary second one) survives the round trip.
test('Ruling R: classify preserves caller-supplied fields not on its own whitelist', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Classify', {
    items: [mkResponse('post body', 'stop', 5)],
    nodes: { 'Code: Normalize': [req({ section: 'insights', someArbitraryKey: 'keep-me' })] },
  });
  assert.strictEqual(out[0].json.section, 'insights',
    'Code: Classify must not drop caller-supplied fields like section');
  assert.strictEqual(out[0].json.someArbitraryKey, 'keep-me',
    'Code: Classify must forward ANY caller-supplied field, not just known ones');
});

const classified = (over = {}) => ({
  json: {
    chunkIndex: 0, stepName: 'prep', text: '', ok: false, failureKind: 'reasoning_burn',
    finishReason: 'length', attempts: 1, model: 'z-ai/glm-5.3-flash', maxTokens: 32768,
    baseMaxTokens: 32768,
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
    items: [classified({ attempts: 2, maxTokens: 100000, baseMaxTokens: 100000, ceiling: 131072 })],
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

// Finding 5: attempt 3's budget must be 2x the ORIGINAL requested budget, not 2x of
// attempt 2's already-1.5x-inflated maxTokens (which would silently make it 3x). Run the
// ladder end-to-end from a 32768 base, exactly as the caller experiences it: Normalize sets
// baseMaxTokens once, then each Escalate call reads maxTokens from the PRIOR attempt's output.
test('Finding 5: attempt-2 and attempt-3 budgets are 1.5x and 2x of the ORIGINAL base, not compounding (32768 -> 49152 -> 65536)', () => {
  const normalized = runCodeNode('openrouter-call.json', 'Code: Normalize', {
    items: [{ json: { stepName: 'prep', model: 'z-ai/glm-5.3-flash', system: 's', user: 'u', maxTokens: 32768 } }],
  })[0].json;
  assert.strictEqual(normalized.baseMaxTokens, 32768, 'Normalize must capture the caller\'s original budget');

  const attempt1Failed = { ...normalized, ok: false, failureKind: 'reasoning_burn', attempts: 1 };
  const attempt2 = runCodeNode('openrouter-call.json', 'Code: Escalate', { items: [{ json: attempt1Failed }] })[0].json;
  assert.strictEqual(attempt2.attempt, 2);
  assert.strictEqual(attempt2.maxTokens, 49152, 'attempt 2 must be 1.5x the base (32768 * 1.5)');
  assert.strictEqual(attempt2.baseMaxTokens, 32768, 'baseMaxTokens must survive unchanged into attempt 2');

  const attempt2Failed = { ...attempt2, ok: false, failureKind: 'reasoning_burn', attempts: 2 };
  const attempt3 = runCodeNode('openrouter-call.json', 'Code: Escalate', { items: [{ json: attempt2Failed }] })[0].json;
  assert.strictEqual(attempt3.attempt, 3);
  assert.strictEqual(attempt3.maxTokens, 65536, 'attempt 3 must be 2x the ORIGINAL base (32768 * 2), not 3x from compounding on attempt 2\'s 49152');
});

// Controller Ruling R: Code: Escalate has the same whitelist-rebuild hole as Code: Classify —
// a retry would silently lose caller-supplied metadata like `section`.
test('Ruling R: escalate preserves caller-supplied fields not on its own whitelist', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Escalate', {
    items: [classified({ section: 'qa', someArbitraryKey: 'keep-me' })],
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.section, 'qa',
    'Code: Escalate must not drop caller-supplied fields like section on retry');
  assert.strictEqual(out[0].json.someArbitraryKey, 'keep-me',
    'Code: Escalate must forward ANY caller-supplied field, not just known ones');
});

test('Finding 5: Code: Escalate and Code: Escalate 2 are byte-identical', () => {
  const { getCodeNode } = require('./harness');
  const a = getCodeNode('openrouter-call.json', 'Code: Escalate');
  const b = getCodeNode('openrouter-call.json', 'Code: Escalate 2');
  assert.strictEqual(a, b, 'Code: Escalate and Code: Escalate 2 must stay byte-identical');
});

// Code: Collect no longer reads $input.all() — the loop-back edge was deleted (Controller
// Ruling J) so it reconstructs the full result set by reaching back into each Classify
// stage via $('Code: Classify[ N]').all(). A stage that never ran on this execution is
// simply absent from the `nodes` stub map, which makes the harness's `$` throw
// `unstubbed $('...')` — the same shape of failure real n8n raises for a node that hasn't
// executed (verified live: ExpressionError "Node '...' hasn't been executed"). Collect's
// try/catch must swallow that.

test('collect: only stage 1 ran (single-attempt success)', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Collect', {
    items: [],
    nodes: {
      'Code: Classify': [classified({ chunkIndex: 0, ok: true, failureKind: null, text: 'only' }).json],
    },
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.text, 'only');
  assert.strictEqual(out[0].json.ok, true);
});

test('collect: stages 1+2 ran, chunk succeeds on retry', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Collect', {
    items: [],
    nodes: {
      'Code: Classify': [classified({ chunkIndex: 0, ok: false, text: '', attempts: 1 }).json],
      'Code: Classify 2': [
        classified({ chunkIndex: 0, ok: true, failureKind: null, text: 'retried', attempts: 2 }).json,
      ],
    },
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.text, 'retried');
  assert.strictEqual(out[0].json.ok, true);
  assert.strictEqual(out[0].json.attempts, 2);
});

test('collect: all three stages ran, best result kept', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Collect', {
    items: [],
    nodes: {
      'Code: Classify': [classified({ chunkIndex: 0, ok: false, text: '', attempts: 1 }).json],
      'Code: Classify 2': [classified({ chunkIndex: 0, ok: false, text: '', attempts: 2 }).json],
      'Code: Classify 3': [
        classified({ chunkIndex: 0, ok: true, failureKind: null, text: 'final', attempts: 3 }).json,
      ],
    },
  });
  assert.strictEqual(out.length, 1);
  assert.strictEqual(out[0].json.text, 'final');
  assert.strictEqual(out[0].json.ok, true);
  assert.strictEqual(out[0].json.attempts, 3);
});

// Regression test for the Critical finding: a mixed batch where chunk 0 succeeds on
// attempt 1 (never revisits Escalate/Classify 2/3) and chunk 1 only succeeds on attempt 3
// must yield BOTH chunks, ordered by chunkIndex. Under the old loop-back graph, chunk 0
// would flow into `Code: Escalate` alongside chunk 1's retries (the IF condition is
// batch-aggregate) and be silently dropped since Escalate filters to `!ok`; Collect would
// only ever see whichever pass ran last. This test asserts the fix: reconstruction from
// each Classify stage by reference means chunk 0's single successful attempt (visible only
// in stage 1's output) is never lost, independent of how many retries chunk 1 needed.
test('collect: mixed batch — chunk succeeds attempt 1, sibling only succeeds attempt 3 (regression for dropped-item Critical)', () => {
  const out = runCodeNode('openrouter-call.json', 'Code: Collect', {
    items: [],
    nodes: {
      'Code: Classify': [
        classified({ chunkIndex: 0, ok: true, failureKind: null, text: 'fast-success', attempts: 1 }).json,
        classified({ chunkIndex: 1, ok: false, text: '', attempts: 1 }).json,
      ],
      'Code: Classify 2': [
        classified({ chunkIndex: 1, ok: false, text: '', attempts: 2 }).json,
      ],
      'Code: Classify 3': [
        classified({ chunkIndex: 1, ok: true, failureKind: null, text: 'slow-success', attempts: 3 }).json,
      ],
    },
  });
  assert.strictEqual(out.length, 2);
  assert.strictEqual(out[0].json.chunkIndex, 0);
  assert.strictEqual(out[0].json.text, 'fast-success');
  assert.strictEqual(out[0].json.ok, true);
  assert.strictEqual(out[1].json.chunkIndex, 1);
  assert.strictEqual(out[1].json.text, 'slow-success');
  assert.strictEqual(out[1].json.ok, true);
});
