const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { getCodeNode } = require('./harness');

// Load the library functions out of the Code node so JSON stays the source of truth.
function loadLib() {
  const code = getCodeNode('merged-call-summarizer.json', 'Code: Chunk Lib');
  const module = { exports: {} };
  new Function('module', 'exports', code + '\nmodule.exports = { estimateTokens, splitTranscriptByLines, splitSignalIntoSections, reassemblePrep };')(module, module.exports);
  return module.exports;
}

const transcript = fs.readFileSync('/repo/output/2026-09-01/transcript.txt', 'utf8');

test('splits the real 247KB transcript into 4-7 chunks under target', () => {
  const { splitTranscriptByLines, estimateTokens } = loadLib();
  const chunks = splitTranscriptByLines(transcript, 15000);
  assert.ok(chunks.length >= 4 && chunks.length <= 7, `unexpected chunk count ${chunks.length}`);
  for (const c of chunks) assert.ok(estimateTokens(c) <= 15000, 'chunk over target');
});

test('splitting loses no content and cuts only on line boundaries', () => {
  const { splitTranscriptByLines } = loadLib();
  const chunks = splitTranscriptByLines(transcript, 15000);
  assert.strictEqual(chunks.join('\n'), transcript.replace(/\n+$/, ''));
  for (const c of chunks) {
    for (const line of c.split('\n')) {
      if (line.trim()) assert.match(line, /^\[\d\d:\d\d:\d\d\] /, `broken line: ${line.slice(0, 40)}`);
    }
  }
});

test('parses signal sections regardless of heading level (H1 or H2)', () => {
  const { splitSignalIntoSections } = loadLib();
  for (const d of ['2026-09-01', '2026-08-25', '2026-08-18', '2026-07-28']) {
    const md = fs.readFileSync(`/repo/output/${d}/extracted-signal.md`, 'utf8');
    const s = splitSignalIntoSections(md);
    assert.strictEqual(Object.keys(s).length, 6, `${d} parsed ${Object.keys(s).length} sections`);
    assert.deepStrictEqual(Object.keys(s).sort(), ['decisions', 'general', 'insights', 'links', 'qa', 'tools']);
  }
});

test('reassembles prep chunks with one header and merged unresolved speakers', () => {
  const { reassemblePrep } = loadLib();
  const a = '=== SESSION ===\ndate: 2026-09-01\n\n<!--SEGMENT\ntopic: a\n-->\nbody A\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C (appears 5 times)';
  const b = '=== SESSION ===\ndate: 2026-09-01\n\n<!--SEGMENT\ntopic: b\n-->\nbody B\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C (appears 5 times)\n- Prem (appears 2 times)';
  const out = reassemblePrep([a, b]);
  assert.strictEqual((out.match(/=== SESSION ===/g) || []).length, 1);
  assert.strictEqual((out.match(/=== UNRESOLVED SPEAKERS ===/g) || []).length, 1);
  assert.ok(out.includes('body A') && out.includes('body B'));
  assert.strictEqual((out.match(/- Ryan C/g) || []).length, 1, 'duplicate speaker not deduped');
  assert.ok(out.includes('- Prem'));
});

test('does not swallow a chunk body when it has no SEGMENT marker or trailing block', () => {
  const { reassemblePrep } = loadLib();
  const a = '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: a\n-->\nbody A';
  const b = '=== SESSION ===\ndate: x\n\nbody B survives with no segment marker';
  const out = reassemblePrep([a, b]);
  assert.ok(out.includes('body B survives'), 'chunk body swallowed by SESSION header regex');
});

test('dedupes unresolved speakers that differ only by internal whitespace', () => {
  const { reassemblePrep } = loadLib();
  const a = '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: a\n-->\nbody A\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C (appears 5 times)';
  const b = '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: b\n-->\nbody B\n\n=== UNRESOLVED SPEAKERS ===\n-  Ryan C   (appears 5 times)';
  const out = reassemblePrep([a, b]);
  assert.strictEqual((out.match(/Ryan C/g) || []).length, 1, 'whitespace-variant duplicate not deduped');
});

test('Finding 4: reassemblePrep accepts a headerOverride and uses it verbatim instead of chunk 1\'s own header', () => {
  const { reassemblePrep } = loadLib();
  const a = '=== SESSION ===\ndate: wrong-from-chunk-1\n\n<!--SEGMENT\ntopic: a\n-->\nbody A';
  const b = '=== SESSION ===\ndate: also-wrong\n\n<!--SEGMENT\ntopic: b\n-->\nbody B';
  const override = '=== SESSION ===\ndate: 2026-09-01\nduration_estimate: 3h 15m\nmain_themes: x; y';
  const out = reassemblePrep([a, b], override);
  assert.strictEqual((out.match(/=== SESSION ===/g) || []).length, 1);
  assert.ok(out.startsWith(override), 'override header must be used verbatim, not chunk 1\'s own header');
  assert.ok(!out.includes('wrong-from-chunk-1') && !out.includes('also-wrong'));
  assert.ok(out.includes('body A') && out.includes('body B'));
});

test('Finding 4: reassemblePrep falls back to chunk 1\'s header when no override is given (backward compatible)', () => {
  const { reassemblePrep } = loadLib();
  const a = '=== SESSION ===\ndate: 2026-09-01\n\n<!--SEGMENT\ntopic: a\n-->\nbody A';
  const out = reassemblePrep([a]);
  assert.ok(out.includes('date: 2026-09-01'));
});

test('Finding 4: reassemblePrep is byte-identical across Code: Chunk Lib, W1 Code: Aggregate Prep, and W2 Code: Aggregate Prep', () => {
  const { getCodeNode } = require('./harness');
  const extractFn = (code, fname) => {
    const start = code.indexOf(`function ${fname}(`);
    assert.ok(start > -1, `${fname} not found`);
    let depth = 0, i = start, started = false;
    while (i < code.length) {
      if (code[i] === '{') { depth += 1; started = true; }
      else if (code[i] === '}') {
        depth -= 1;
        if (started && depth === 0) return code.slice(start, i + 1);
      }
      i += 1;
    }
    throw new Error('unbalanced braces');
  };
  const lib = getCodeNode('merged-call-summarizer.json', 'Code: Chunk Lib');
  const w1 = getCodeNode('merged-call-summarizer.json', 'Code: Aggregate Prep');
  const w2 = getCodeNode('transcript-only-summarizer.json', 'Code: Aggregate Prep');
  const libFn = extractFn(lib, 'reassemblePrep');
  const w1Fn = extractFn(w1, 'reassemblePrep');
  const w2Fn = extractFn(w2, 'reassemblePrep');
  assert.strictEqual(libFn, w1Fn, 'Chunk Lib and W1 Aggregate Prep reassemblePrep must be byte-identical');
  assert.strictEqual(w1Fn, w2Fn, 'W1 and W2 Aggregate Prep reassemblePrep must be byte-identical');
});
