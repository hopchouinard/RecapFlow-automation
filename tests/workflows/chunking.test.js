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

test('dedupes unresolved speakers that differ only by internal whitespace', () => {
  const { reassemblePrep } = loadLib();
  const a = '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: a\n-->\nbody A\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C (appears 5 times)';
  const b = '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: b\n-->\nbody B\n\n=== UNRESOLVED SPEAKERS ===\n-  Ryan C   (appears 5 times)';
  const out = reassemblePrep([a, b]);
  assert.strictEqual((out.match(/Ryan C/g) || []).length, 1, 'whitespace-variant duplicate not deduped');
});
