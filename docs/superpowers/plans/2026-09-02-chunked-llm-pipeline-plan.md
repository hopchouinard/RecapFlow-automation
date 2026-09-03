# Chunked LLM Pipeline + Shared OpenRouter Component — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make both summarizer workflows produce correct artifacts for a transcript of any size, and make truncation impossible to mistake for success.

**Architecture:** A new shared sub-workflow, `OpenRouter Call` (W3), becomes the only component that talks to OpenRouter — an HTTP Request node using the existing `openRouterApi` credential, which exposes `finish_reason` (the n8n `chainLlm` node discards it). W1 and W2 split their transcript-consuming steps into chunks, invoke W3 once per step with N items, and guard/reassemble the results. Every model is configurable from a single `Code: Pipeline Config` node per workflow.

**Tech Stack:** n8n 2.36.8 workflow JSON, Node 24 Code nodes, OpenRouter API, `node --test` run in a throwaway `n8nio/n8n` container.

**Spec:** `docs/superpowers/specs/2026-09-02-chunked-llm-pipeline-design.md`

## Global Constraints

- **Workflow JSON in `workflows/` is the single source of truth.** No build step, no code generation. Tests read the committed JSON and execute node `jsCode` directly, so the operator's n8n UI edits are never overwritten by tooling.
- **`maxTokens` stored in any node parameter must be ≤ 32768.** n8n's editor silently re-clamps higher values on save (spec §2.1). Escalation above 32768 happens only at runtime inside Code-node logic, where the clamp does not apply.
- **Model ceilings** (spec §4.5): `z-ai/glm-5.3-flash` = 131072, `anthropic/claude-sonnet-5` = 128000, unknown slug = 32768.
- **Six canonical signal slugs, in this order:** `general`, `insights`, `qa`, `tools`, `links`, `decisions`.
- **Section parsing tolerates H1–H3** — `/^#{1,3}[ \t]+([a-z]+)[ \t]*$/m` (spec §4.6). A parser keyed to `^## ` returns zero sections on 2026-09-01.
- **`executeWorkflow` typeVersion 1.2 requires the resourceLocator form** `{__rl: true, value, mode, cachedResultName}`. A bare string errors with *"No information about the workflow to execute found"*.
- **Never modify** `data/config`, `N8N_ENCRYPTION_KEY`, or the artifact filenames/`/ingest` contract.
- **Model config lives only in `Code: Pipeline Config`.** No model slug may appear in any other node.
- Run n8n CLI with `N8N_RUNNERS_BROKER_PORT=5680 N8N_RUNNERS_AUTH_TOKEN=foo` to avoid a port-5679 collision with the live container.

---

## File Structure

| Path | Responsibility |
|---|---|
| `tests/workflows/harness.js` | Loads workflow JSON, executes a named Code node's `jsCode` against mocked n8n globals |
| `tests/workflows/*.test.js` | Unit tests per Code node |
| `scripts/test-workflows.sh` | Runs the suite in a throwaway container |
| `workflows/openrouter-call.json` | **New.** W3 — the shared OpenRouter component |
| `workflows/merged-call-summarizer.json` | W1 — chunked prep / signal / post |
| `workflows/transcript-only-summarizer.json` | W2 — same pattern, its own models |

---

### Task 1: Test harness and runner

**Files:**
- Create: `tests/workflows/harness.js`
- Create: `tests/workflows/harness.test.js`
- Create: `scripts/test-workflows.sh`

**Interfaces:**
- Produces: `runCodeNode(workflowFile, nodeName, ctx) -> any`, `getCodeNode(workflowFile, nodeName) -> string`, `loadWorkflow(file) -> object`. `ctx` accepts `{ items, json, nodes, fsMock }`. Every later task consumes `runCodeNode`.

- [ ] **Step 1: Write the harness**

Create `tests/workflows/harness.js`:

```js
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const REPO = process.env.REPO_ROOT || '/repo';

function loadWorkflow(file) {
  return JSON.parse(fs.readFileSync(path.join(REPO, 'workflows', file), 'utf8'));
}

function getCodeNode(workflowFile, nodeName) {
  const wf = loadWorkflow(workflowFile);
  const node = wf.nodes.find((n) => n.name === nodeName);
  if (!node) throw new Error(`node not found: ${nodeName} in ${workflowFile}`);
  if (!node.parameters || typeof node.parameters.jsCode !== 'string') {
    throw new Error(`node has no jsCode: ${nodeName}`);
  }
  return node.parameters.jsCode;
}

// Execute a Code node's jsCode against mocked n8n globals.
// ctx: { items?, json?, nodes?, fsMock? }
function runCodeNode(workflowFile, nodeName, ctx = {}) {
  const code = getCodeNode(workflowFile, nodeName);
  const items = ctx.items || [];
  const $input = {
    all: () => items,
    first: () => items[0],
    last: () => items[items.length - 1],
  };
  const $json = ctx.json !== undefined ? ctx.json : (items[0] && items[0].json) || {};
  const $ = (name) => {
    const stub = (ctx.nodes || {})[name];
    if (stub === undefined) throw new Error(`unstubbed $('${name}')`);
    return {
      item: { json: stub },
      first: () => ({ json: stub }),
      all: () => (Array.isArray(stub) ? stub.map((j) => ({ json: j })) : [{ json: stub }]),
    };
  };
  const fakeRequire = (mod) => {
    if (mod === 'fs' && ctx.fsMock) return ctx.fsMock;
    if (mod === 'fs' || mod === 'path') return require(mod);
    throw new Error(`require not allowed: ${mod}`);
  };
  const sandbox = { $input, $json, $, require: fakeRequire, console, Buffer, JSON, Date, Math };
  const wrapped = `(function(){ ${code} \n})()`;
  return vm.runInNewContext(wrapped, sandbox, { timeout: 5000 });
}

module.exports = { loadWorkflow, getCodeNode, runCodeNode };
```

- [ ] **Step 2: Write the failing test**

Create `tests/workflows/harness.test.js`:

```js
const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode } = require('./harness');

test('runs a real Code node from workflow JSON', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Calculate Next Tuesday', {
    json: { datePrefix: '2026-09-01', compressedText: 'x', outputDir: '/tmp/o' },
  });
  assert.strictEqual(out.json.inviteDate, '2026-09-08');
  assert.strictEqual(out.json.formattedDate, 'September 8th');
});

test('a Monday call still resolves to the next Tuesday', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Calculate Next Tuesday', {
    json: { datePrefix: '2026-08-31' },
  });
  assert.strictEqual(out.json.inviteDate, '2026-09-01');
});
```

- [ ] **Step 3: Write the runner script**

Create `scripts/test-workflows.sh`:

```bash
#!/usr/bin/env bash
# Run n8n Code-node unit tests in a throwaway container (no host node required).
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec docker run --rm --entrypoint node \
  -v "$REPO/tests/workflows:/work" \
  -v "$REPO:/repo:ro" \
  -w /work -e REPO_ROOT=/repo \
  n8nio/n8n:latest --test "$@"
```

- [ ] **Step 4: Make it executable and run it**

Run: `chmod +x scripts/test-workflows.sh && ./scripts/test-workflows.sh`
Expected: `pass 2`, `fail 0`.

- [ ] **Step 5: Commit**

```bash
git add tests/workflows scripts/test-workflows.sh
git commit -m "test: add n8n Code-node unit test harness"
```

---

### Task 2: Reconcile live workflows into the repo

The committed JSON is stale — it shows `maxTokens: 8192` and `claude-sonnet-4.6`, while live W1 runs `claude-sonnet-5` for Extract Signal and `glm-5.3-flash` elsewhere, all at 32768. Editing the stale file would silently revert the operator's UI changes.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`
- Modify: `workflows/transcript-only-summarizer.json`

- [ ] **Step 1: Export live workflows**

```bash
cd ~/n8n
docker exec n8n n8n export:workflow --id=5 --output=/tmp/w1.json
docker exec n8n n8n export:workflow --id=6 --output=/tmp/w2.json
docker cp n8n:/tmp/w1.json /tmp/w1.json && docker cp n8n:/tmp/w2.json /tmp/w2.json
```

- [ ] **Step 2: Inspect the diff before overwriting**

```bash
python3 - <<'PY'
import json
for src, dst in (('/tmp/w1.json','workflows/merged-call-summarizer.json'),
                 ('/tmp/w2.json','workflows/transcript-only-summarizer.json')):
    live = json.load(open(src)); live = live[0] if isinstance(live, list) else live
    repo = json.load(open(dst))
    lm = {n['name']: n['parameters'].get('model') for n in live['nodes'] if 'lmChatOpenRouter' in n['type']}
    rm = {n['name']: n['parameters'].get('model') for n in repo['nodes'] if 'lmChatOpenRouter' in n['type']}
    print(dst)
    for k in sorted(set(lm) | set(rm)):
        if lm.get(k) != rm.get(k): print(f"  {k}: repo={rm.get(k)} -> live={lm.get(k)}")
PY
```
Expected: W1 shows `claude-sonnet-4.6 -> claude-sonnet-5` for all five, plus GLM on models 2–5.

- [ ] **Step 3: Write live JSON into the repo, preserving credential placeholders**

The committed files use `"id": "PLACEHOLDER"` for credentials; live exports contain the real credential id. Keep the placeholder convention:

```bash
python3 - <<'PY'
import json
for src, dst in (('/tmp/w1.json','workflows/merged-call-summarizer.json'),
                 ('/tmp/w2.json','workflows/transcript-only-summarizer.json')):
    wf = json.load(open(src)); wf = wf[0] if isinstance(wf, list) else wf
    for n in wf.get('nodes', []):
        for cred in (n.get('credentials') or {}).values():
            cred['id'] = 'PLACEHOLDER'
    json.dump(wf, open(dst,'w'), indent=2)
    print('wrote', dst)
PY
```

- [ ] **Step 4: Verify the harness still passes against the refreshed JSON**

Run: `./scripts/test-workflows.sh`
Expected: `pass 2`, `fail 0`. (If `Code: Calculate Next Tuesday` was renamed in the UI, fix the test's node name now.)

- [ ] **Step 5: Verify no real credential ids leaked**

Run: `grep -c PLACEHOLDER workflows/*.json && ! grep -q '1YRALvHjmQ3E6pqd' workflows/*.json && echo "no credential ids leaked"`
Expected: prints the placeholder counts and `no credential ids leaked`.

- [ ] **Step 6: Commit**

```bash
git add workflows/
git commit -m "chore(workflows): reconcile committed JSON with live n8n config"
```

---

### Task 3: Chunking and reassembly logic

Pure functions, embedded as Code nodes in Task 6+. Built and tested first because every later task depends on them. **All code below is verified against the real 2026-09-01 artifacts.**

**Files:**
- Create: `tests/workflows/chunking.test.js`
- Modify: `workflows/merged-call-summarizer.json` (adds `Code: Chunk Lib` node)

**Interfaces:**
- Produces, on the item emitted by `Code: Chunk Lib`, nothing at runtime — the node exists so its `jsCode` is testable and copy-pasteable. Later tasks inline these four functions into their own splitter/aggregator nodes: `estimateTokens(s)`, `splitTranscriptByLines(text, targetTokens)`, `splitSignalIntoSections(md)`, `reassemblePrep(texts)`.

- [ ] **Step 1: Write the failing tests**

Create `tests/workflows/chunking.test.js`:

```js
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh chunking.test.js`
Expected: FAIL with `node not found: Code: Chunk Lib`.

- [ ] **Step 3: Add the `Code: Chunk Lib` node**

Add this node to `workflows/merged-call-summarizer.json` (disconnected — it is a library holder, not part of the execution path; set `"disabled": true`):

```json
{
  "parameters": { "jsCode": "PLACEHOLDER_REPLACED_IN_STEP_4" },
  "id": "c11b0000-0000-4000-8000-00000000c11b",
  "name": "Code: Chunk Lib",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [220, 600],
  "disabled": true
}
```

- [ ] **Step 4: Set its `jsCode` to the verified implementation**

Use this exact body (verified 2026-09-02 against real artifacts — 5 chunks of ~14.4k tokens on 2026-09-01):

```js
const estimateTokens = (s) => Math.ceil(s.length / 3.6);

function splitTranscriptByLines(text, targetTokens) {
  const lines = text.split('\n');
  const chunks = [];
  let buf = [], bufTokens = 0;
  for (const line of lines) {
    const t = estimateTokens(line) + 1;
    if (bufTokens + t > targetTokens && buf.length > 0) {
      chunks.push(buf.join('\n'));
      buf = []; bufTokens = 0;
    }
    buf.push(line); bufTokens += t;
  }
  if (buf.length && buf.join('\n').trim()) chunks.push(buf.join('\n'));
  return chunks;
}

const CANON = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'];

function splitSignalIntoSections(md) {
  const out = {};
  const re = /^#{1,3}[ \t]+([a-z]+)[ \t]*$/gm;
  let m; const marks = [];
  while ((m = re.exec(md)) !== null) marks.push({ slug: m[1], start: m.index, bodyStart: re.lastIndex });
  for (let i = 0; i < marks.length; i++) {
    const end = i + 1 < marks.length ? marks[i + 1].start : md.length;
    const body = md.slice(marks[i].bodyStart, end).trim();
    if (CANON.includes(marks[i].slug) && body) out[marks[i].slug] = body;
  }
  return out;
}

function reassemblePrep(texts) {
  const SESSION_RE = /===\s*SESSION\s*===[\s\S]*?(?=\n<!--SEGMENT|\n===|$)/;
  const UNRES_RE = /===\s*UNRESOLVED SPEAKERS\s*===([\s\S]*)$/;
  let header = null;
  const bodies = [], unresolved = new Set();
  for (const raw of texts) {
    let t = raw;
    const u = t.match(UNRES_RE);
    if (u) {
      u[1].split('\n').map((l) => l.trim()).filter((l) => l.startsWith('-')).forEach((l) => unresolved.add(l));
      t = t.slice(0, u.index);
    }
    const h = t.match(SESSION_RE);
    if (h) { if (header === null) header = h[0].trim(); t = t.slice(0, h.index) + t.slice(h.index + h[0].length); }
    if (t.trim()) bodies.push(t.trim());
  }
  let out = (header ? header + '\n\n' : '') + bodies.join('\n\n');
  if (unresolved.size) out += '\n\n=== UNRESOLVED SPEAKERS ===\n' + [...unresolved].join('\n');
  return out;
}

return [{ json: { lib: true } }];
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh chunking.test.js`
Expected: `pass 4`, `fail 0`.

- [ ] **Step 6: Commit**

```bash
git add workflows/merged-call-summarizer.json tests/workflows/chunking.test.js
git commit -m "feat(workflows): add verified chunking and reassembly library"
```

---

### Task 4: W3 — request normalization

**Files:**
- Create: `workflows/openrouter-call.json`
- Create: `tests/workflows/openrouter-call.test.js`

**Interfaces:**
- Consumes: input items shaped per spec §4.1 — `{ stepName, model, system, user, maxTokens, reasoningEffort?, temperature?, expect?, chunkIndex }`.
- Produces: `Code: Normalize` emits items with `{ ...input, temperature, attempt: 1, ceiling }` where `ceiling` is the model output ceiling. Task 5 consumes `expect` and `chunkIndex`; Task 6 consumes `ceiling`.

- [ ] **Step 1: Write the failing test**

Create `tests/workflows/openrouter-call.test.js`:

```js
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh openrouter-call.test.js`
Expected: FAIL — `openrouter-call.json` does not exist.

- [ ] **Step 3: Create W3 with the trigger and normalize node**

Create `workflows/openrouter-call.json`:

```json
{
  "id": "openrouterCall",
  "name": "OpenRouter Call",
  "nodes": [
    {
      "parameters": { "workflowInputs": { "values": [] } },
      "id": "0e000000-0000-4000-8000-00000000e001",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "typeVersion": 1.1,
      "position": [0, 0]
    },
    {
      "parameters": { "jsCode": "REPLACED_IN_STEP_4" },
      "id": "0e000000-0000-4000-8000-00000000e002",
      "name": "Code: Normalize",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [220, 0]
    }
  ],
  "connections": {
    "When Executed by Another Workflow": {
      "main": [[{ "node": "Code: Normalize", "type": "main", "index": 0 }]]
    }
  },
  "settings": { "executionOrder": "v1" }
}
```

- [ ] **Step 4: Set `Code: Normalize`'s `jsCode`**

```js
const CEILINGS = {
  'z-ai/glm-5.3-flash': 131072,
  'anthropic/claude-sonnet-5': 128000,
};
const DEFAULT_CEILING = 32768;
const REQUIRED = ['stepName', 'model', 'system', 'user', 'maxTokens'];

return $input.all().map((item, i) => {
  const j = item.json;
  for (const f of REQUIRED) {
    if (j[f] === undefined || j[f] === null || j[f] === '') {
      throw new Error(`missing required field '${f}' on item ${i} (stepName=${j.stepName})`);
    }
  }
  return {
    json: {
      ...j,
      chunkIndex: j.chunkIndex === undefined ? i : j.chunkIndex,
      temperature: j.temperature === undefined ? 0.3 : j.temperature,
      attempt: 1,
      ceiling: CEILINGS[j.model] || DEFAULT_CEILING,
    },
  };
});
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh openrouter-call.test.js`
Expected: `pass 4`, `fail 0`.

- [ ] **Step 6: Commit**

```bash
git add workflows/openrouter-call.json tests/workflows/openrouter-call.test.js
git commit -m "feat(w3): add OpenRouter Call trigger and request normalization"
```

---

### Task 5: W3 — HTTP request and response classification

The classifier is the heart of the fix: it turns OpenRouter's correctly-reported truncation into a hard signal, which `chainLlm` discarded (spec §2.3).

**Files:**
- Modify: `workflows/openrouter-call.json`
- Modify: `tests/workflows/openrouter-call.test.js`

**Interfaces:**
- Consumes: normalized items from Task 4; raw OpenRouter responses from the HTTP node.
- Produces: `Code: Classify` emits `{ chunkIndex, stepName, text, ok, finishReason, usage: { promptTokens, completionTokens, reasoningTokens, cost }, attempts, failureKind, model, maxTokens, reasoningEffort, temperature, system, user, ceiling, expect }`. `failureKind` ∈ `null | reasoning_burn | content_truncated | structure | api_error`. Task 6 consumes `ok`, `failureKind`, `attempts`, `ceiling`.

- [ ] **Step 1: Write the failing tests**

Append to `tests/workflows/openrouter-call.test.js`:

```js
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh openrouter-call.test.js`
Expected: FAIL with `node not found: Code: Classify`.

- [ ] **Step 3: Add the HTTP Request and Classify nodes**

Add to `workflows/openrouter-call.json` `nodes`:

```json
{
  "parameters": {
    "method": "POST",
    "url": "https://openrouter.ai/api/v1/chat/completions",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "openRouterApi",
    "sendBody": true,
    "specifyBody": "json",
    "jsonBody": "={{ JSON.stringify(Object.assign({ model: $json.model, max_tokens: $json.maxTokens, temperature: $json.temperature, messages: [ { role: 'system', content: $json.system }, { role: 'user', content: $json.user } ] }, $json.reasoningEffort ? { reasoning_effort: $json.reasoningEffort } : {})) }}",
    "options": { "timeout": 1800000, "response": { "response": { "neverError": true } } }
  },
  "id": "0e000000-0000-4000-8000-00000000e003",
  "name": "HTTP: OpenRouter",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4.2,
  "position": [440, 0],
  "credentials": { "openRouterApi": { "id": "PLACEHOLDER", "name": "OpenRouter account" } }
},
{
  "parameters": { "jsCode": "REPLACED_IN_STEP_4" },
  "id": "0e000000-0000-4000-8000-00000000e004",
  "name": "Code: Classify",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [660, 0]
}
```

And extend `connections`:

```json
"Code: Normalize": { "main": [[{ "node": "HTTP: OpenRouter", "type": "main", "index": 0 }]] },
"HTTP: OpenRouter": { "main": [[{ "node": "Code: Classify", "type": "main", "index": 0 }]] }
```

`neverError: true` matters — without it a 4xx/5xx aborts the node before the classifier can record `api_error`.

- [ ] **Step 4: Set `Code: Classify`'s `jsCode`**

```js
const CANON = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'];

function parseSections(md) {
  const re = /^#{1,3}[ \t]+([a-z]+)[ \t]*$/gm;
  const found = []; let m;
  while ((m = re.exec(md)) !== null) found.push(m[1]);
  return found.filter((s) => CANON.includes(s));
}

function structureOk(expect, text) {
  if (!expect || expect === 'none') return true;
  if (expect === 'prep.chunk') {
    const opens = (text.match(/<!--SEGMENT/g) || []).length;
    const closes = (text.match(/-->/g) || []).length;
    return opens > 0 && opens === closes;
  }
  if (expect === 'signal.map') return parseSections(text).length > 0;
  if (expect === 'signal.reduce') {
    const found = parseSections(text);
    return CANON.every((s) => found.includes(s));
  }
  if (expect === 'post.section') {
    return !/^\s*#{1,6}\s/m.test(text) && !/\*\*/.test(text) && !/^\s*[-*]\s+/m.test(text);
  }
  return true;
}

const requests = $('Code: Normalize').all().map((i) => i.json);

return $input.all().map((item, idx) => {
  const req = requests[idx] || requests[0];
  const body = item.json || {};
  const choice = (body.choices || [])[0] || {};
  const usage = body.usage || {};
  const details = usage.completion_tokens_details || {};
  const text = (choice.message && choice.message.content) || '';
  const finishReason = choice.finish_reason || null;

  let failureKind = null;
  if (body.error || (!body.choices && !text)) {
    failureKind = 'api_error';
  } else if (text.trim() === '') {
    failureKind = 'reasoning_burn';
  } else if (finishReason !== 'stop') {
    failureKind = 'content_truncated';
  } else if (!structureOk(req.expect, text)) {
    failureKind = 'structure';
  }

  return {
    json: {
      chunkIndex: req.chunkIndex,
      stepName: req.stepName,
      text,
      ok: failureKind === null,
      failureKind,
      finishReason,
      attempts: req.attempt,
      usage: {
        promptTokens: usage.prompt_tokens || 0,
        completionTokens: usage.completion_tokens || 0,
        reasoningTokens: details.reasoning_tokens || 0,
        cost: usage.cost || 0,
      },
      model: req.model, maxTokens: req.maxTokens, reasoningEffort: req.reasoningEffort,
      temperature: req.temperature, system: req.system, user: req.user,
      ceiling: req.ceiling, expect: req.expect,
      errorMessage: (body.error && body.error.message) || null,
    },
  };
});
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh openrouter-call.test.js`
Expected: `pass 11`, `fail 0`.

- [ ] **Step 6: Commit**

```bash
git add workflows/openrouter-call.json tests/workflows/openrouter-call.test.js
git commit -m "feat(w3): add HTTP request and truncation-aware response classifier"
```

---

### Task 6: W3 — retry escalation ladder

Reasoning burn is non-deterministic — spec §2.5 recorded 1 of 3 identical requests burning its whole budget — so a plain retry frequently succeeds. Escalation may exceed 32768 because it happens at runtime, not in a stored node parameter.

**Files:**
- Modify: `workflows/openrouter-call.json`
- Modify: `tests/workflows/openrouter-call.test.js`

**Interfaces:**
- Consumes: classified items from Task 5.
- Produces: `Code: Escalate` emits only the items needing another attempt, re-shaped as normalize-style requests with `attempt` incremented. `Code: Collect` emits the final ordered result set consumed by W1/W2.

- [ ] **Step 1: Write the failing tests**

Append to `tests/workflows/openrouter-call.test.js`:

```js
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
  assert.deepStrictEqual(out.map((i) => i.json.text), ['first', 'second']);
  assert.strictEqual(out[1].json.ok, true);
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh openrouter-call.test.js`
Expected: FAIL with `node not found: Code: Escalate`.

- [ ] **Step 3: Add the `IF`, `Code: Escalate` and `Code: Collect` nodes**

Add to `nodes`:

```json
{
  "parameters": {
    "conditions": {
      "options": { "caseSensitive": true, "version": 2 },
      "conditions": [{
        "leftValue": "={{ $input.all().filter(i => !i.json.ok && i.json.attempts < 3).length }}",
        "rightValue": 0,
        "operator": { "type": "number", "operation": "gt" }
      }],
      "combinator": "and"
    }
  },
  "id": "0e000000-0000-4000-8000-00000000e005",
  "name": "IF: Needs Retry",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [880, 0]
},
{
  "parameters": { "jsCode": "REPLACED_IN_STEP_4" },
  "id": "0e000000-0000-4000-8000-00000000e006",
  "name": "Code: Escalate",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [1100, -120]
},
{
  "parameters": { "jsCode": "REPLACED_IN_STEP_5" },
  "id": "0e000000-0000-4000-8000-00000000e007",
  "name": "Code: Collect",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [1100, 120]
}
```

Extend `connections` — the escalate branch loops back to the HTTP node:

```json
"Code: Classify": { "main": [[{ "node": "IF: Needs Retry", "type": "main", "index": 0 }]] },
"IF: Needs Retry": {
  "main": [
    [{ "node": "Code: Escalate", "type": "main", "index": 0 }],
    [{ "node": "Code: Collect", "type": "main", "index": 0 }]
  ]
},
"Code: Escalate": { "main": [[{ "node": "HTTP: OpenRouter", "type": "main", "index": 0 }]] }
```

- [ ] **Step 4: Set `Code: Escalate`'s `jsCode`**

```js
const LADDER = { 2: { effort: 'low', factor: 1.5 }, 3: { effort: 'minimal', factor: 2 } };

return $input.all()
  .filter((i) => !i.json.ok && i.json.attempts < 3)
  .map((i) => {
    const j = i.json;
    const nextAttempt = j.attempts + 1;
    const rung = LADDER[nextAttempt];
    const raised = Math.floor(j.maxTokens * rung.factor);
    return {
      json: {
        stepName: j.stepName, model: j.model, system: j.system, user: j.user,
        chunkIndex: j.chunkIndex, temperature: j.temperature, expect: j.expect,
        ceiling: j.ceiling, attempt: nextAttempt,
        reasoningEffort: rung.effort,
        maxTokens: Math.min(raised, j.ceiling),
      },
    };
  });
```

- [ ] **Step 5: Set `Code: Collect`'s `jsCode`**

```js
const best = new Map();
for (const item of $input.all()) {
  const j = item.json;
  const prev = best.get(j.chunkIndex);
  // Prefer a successful attempt; otherwise keep the latest attempt for its error detail.
  if (!prev || (j.ok && !prev.ok) || (j.ok === prev.ok && j.attempts > prev.attempts)) {
    best.set(j.chunkIndex, j);
  }
}
return [...best.values()]
  .sort((a, b) => a.chunkIndex - b.chunkIndex)
  .map((json) => ({ json }));
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh openrouter-call.test.js`
Expected: `pass 17`, `fail 0`.

- [ ] **Step 7: Import W3 and record its id**

```bash
cd ~/n8n
python3 -c "
import json; p='workflows/openrouter-call.json'; w=json.load(open(p))
for n in w['nodes']:
    for c in (n.get('credentials') or {}).values():
        c['id']='1YRALvHjmQ3E6pqd'
json.dump(w, open('/tmp/w3.json','w'), indent=2)"
docker cp /tmp/w3.json n8n:/tmp/w3.json
docker exec n8n n8n import:workflow --input=/tmp/w3.json
docker exec n8n_db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -t -A -c "select id,name from workflow_entity where name = '"'"'OpenRouter Call'"'"';"'
```
Expected: `openrouterCall|OpenRouter Call`. Record this id — Tasks 7–11 need it for the resourceLocator.

- [ ] **Step 8: Smoke-test W3 live with a two-item batch**

```bash
docker exec -e N8N_RUNNERS_BROKER_PORT=5680 -e N8N_RUNNERS_AUTH_TOKEN=foo \
  n8n n8n execute --id openrouterCall
```
Expected: `status: success`. (The trigger has no input items on a bare CLI run; this confirms the graph loads and wires without error. Real batches are exercised in Task 8.)

- [ ] **Step 9: Commit**

```bash
git add workflows/openrouter-call.json tests/workflows/openrouter-call.test.js
git commit -m "feat(w3): add retry escalation ladder and result collection"
```

---

### Task 7: W1 — pipeline config node

**Files:**
- Modify: `workflows/merged-call-summarizer.json`
- Create: `tests/workflows/pipeline-config.test.js`

**Interfaces:**
- Produces: a single item `{ steps: { prep, signalMap, signalReduce, postSection, compress, invite }, retry: { componentAttempts, callerHalvings } }`, read elsewhere via `$('Code: Pipeline Config').first().json`.

- [ ] **Step 1: Write the failing test**

Create `tests/workflows/pipeline-config.test.js`:

```js
const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode, loadWorkflow } = require('./harness');

const STEPS = ['prep', 'signalMap', 'signalReduce', 'postSection', 'compress', 'invite'];

for (const file of ['merged-call-summarizer.json', 'transcript-only-summarizer.json']) {
  test(`${file}: config exposes every step`, () => {
    const out = runCodeNode(file, 'Code: Pipeline Config', {});
    const cfg = out[0].json;
    for (const s of STEPS) {
      assert.ok(cfg.steps[s], `missing step ${s}`);
      assert.ok(cfg.steps[s].model, `step ${s} has no model`);
      assert.ok(cfg.steps[s].maxTokens <= 32768, `step ${s} maxTokens exceeds the UI clamp`);
    }
    assert.strictEqual(cfg.retry.callerHalvings, 2);
  });

  test(`${file}: kimi is retired and no model slug leaks outside the config node`, () => {
    const wf = loadWorkflow(file);
    const cfgCode = wf.nodes.find((n) => n.name === 'Code: Pipeline Config').parameters.jsCode;
    assert.ok(!/kimi/i.test(cfgCode), 'kimi must be retired');
    for (const n of wf.nodes) {
      if (n.name === 'Code: Pipeline Config') continue;
      const blob = JSON.stringify(n.parameters || {});
      assert.ok(!/z-ai\/|anthropic\/|moonshotai\//.test(blob), `model slug leaked into node ${n.name}`);
    }
  });
}
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `./scripts/test-workflows.sh pipeline-config.test.js`
Expected: FAIL with `node not found: Code: Pipeline Config`.

- [ ] **Step 3: Add the node to W1**

Add to `workflows/merged-call-summarizer.json` `nodes` (position it right after the trigger, and connect the trigger to it, then it to the node the trigger previously fed):

```json
{
  "parameters": { "jsCode": "REPLACED_IN_STEP_4" },
  "id": "cf000000-0000-4000-8000-0000000000cf",
  "name": "Code: Pipeline Config",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [120, 0]
}
```

- [ ] **Step 4: Set its `jsCode`**

```js
return [{
  json: {
    steps: {
      prep:         { model: 'z-ai/glm-5.3-flash',        maxTokens: 32768, reasoningEffort: 'low', chunkTargetTokens: 15000 },
      signalMap:    { model: 'anthropic/claude-sonnet-5', maxTokens: 16384, chunkTargetTokens: 15000 },
      signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000 },
      postSection:  { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
      compress:     { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
      invite:       { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
    },
    retry: { componentAttempts: 3, callerHalvings: 2 },
  },
}];
```

- [ ] **Step 5: Run the test**

Run: `./scripts/test-workflows.sh pipeline-config.test.js`
Expected: the W1 tests pass; the W2 tests still fail (`transcript-only-summarizer.json` gets its config in Task 11). That is expected at this point.

- [ ] **Step 6: Commit**

```bash
git add workflows/merged-call-summarizer.json tests/workflows/pipeline-config.test.js
git commit -m "feat(w1): add pipeline config node"
```

---

### Task 8: W1 — chunked Prep-Prompt

First step to actually use W3. Replaces `LLM: Prep-Prompt` + `OpenRouter Chat Model 5`.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`
- Create: `tests/workflows/w1-prep.test.js`

**Interfaces:**
- Consumes: `Code: Pipeline Config` (Task 7); W3's item contract (Tasks 4–6); the four library functions (Task 3).
- Produces: `Code: Aggregate Prep` emits `{ preparedTranscript, chunkCount, totalCost }` consumed by the existing `Code: Save prepared-transcript.md`.

- [ ] **Step 1: Write the failing tests**

Create `tests/workflows/w1-prep.test.js`:

```js
const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode } = require('./harness');

const transcript = fs.readFileSync('/repo/output/2026-09-01/transcript.txt', 'utf8');
const cfg = {
  steps: { prep: { model: 'z-ai/glm-5.3-flash', maxTokens: 32768, reasoningEffort: 'low', chunkTargetTokens: 15000 } },
  retry: { componentAttempts: 3, callerHalvings: 2 },
};

test('split emits one W3 request per chunk with prep config applied', () => {
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 0 } }],
    nodes: { 'Code: Pipeline Config': cfg, 'Code: Validate and Check Partner': { transcriptText: transcript } },
  });
  assert.ok(out.length >= 4 && out.length <= 7, `unexpected chunk count ${out.length}`);
  out.forEach((item, i) => {
    assert.strictEqual(item.json.stepName, 'prep');
    assert.strictEqual(item.json.model, 'z-ai/glm-5.3-flash');
    assert.strictEqual(item.json.reasoningEffort, 'low');
    assert.strictEqual(item.json.expect, 'prep.chunk');
    assert.strictEqual(item.json.chunkIndex, i);
    assert.ok(item.json.user.length > 0);
    assert.ok(item.json.system.includes('SEGMENT'), 'prep system prompt must survive');
  });
});

test('split halves the chunk target on a retry pass', () => {
  const once = runCodeNode('merged-call-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 0 } }],
    nodes: { 'Code: Pipeline Config': cfg, 'Code: Validate and Check Partner': { transcriptText: transcript } },
  });
  const twice = runCodeNode('merged-call-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 1 } }],
    nodes: { 'Code: Pipeline Config': cfg, 'Code: Validate and Check Partner': { transcriptText: transcript } },
  });
  assert.ok(twice.length > once.length, 'halving must produce more, smaller chunks');
});

test('aggregate joins chunks, hoists one header, merges unresolved speakers', () => {
  const items = [
    { json: { chunkIndex: 0, ok: true, text: '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: a\n-->\nbody A\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C', usage: { cost: 0.01 } } },
    { json: { chunkIndex: 1, ok: true, text: '=== SESSION ===\ndate: x\n\n<!--SEGMENT\ntopic: b\n-->\nbody B\n\n=== UNRESOLVED SPEAKERS ===\n- Ryan C\n- Prem', usage: { cost: 0.02 } } },
  ];
  const out = runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Prep', { items });
  const md = out[0].json.preparedTranscript;
  assert.strictEqual((md.match(/=== SESSION ===/g) || []).length, 1);
  assert.strictEqual((md.match(/- Ryan C/g) || []).length, 1);
  assert.ok(md.includes('body A') && md.includes('body B'));
  assert.strictEqual(out[0].json.chunkCount, 2);
  assert.ok(Math.abs(out[0].json.totalCost - 0.03) < 1e-9);
});

test('aggregate throws when any chunk failed, so nothing is written', () => {
  const items = [
    { json: { chunkIndex: 0, ok: true, text: 'fine', usage: { cost: 0 } } },
    { json: { chunkIndex: 1, ok: false, failureKind: 'reasoning_burn', text: '', attempts: 3, usage: { cost: 0 } } },
  ];
  assert.throws(
    () => runCodeNode('merged-call-summarizer.json', 'Code: Aggregate Prep', { items }),
    /reasoning_burn|chunk 1|failed/i,
  );
});
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh w1-prep.test.js`
Expected: FAIL with `node not found: Code: Split Prep`.

- [ ] **Step 3: Add `Code: Split Prep`**

`jsCode` — note the system prompt is copied verbatim from the existing `LLM: Prep-Prompt` node's `SystemMessagePromptTemplate`, with the `SPEAKER_ALIASES` expression replaced by a runtime reference:

```js
const cfg = $('Code: Pipeline Config').first().json.steps.prep;
const src = $('Code: Validate and Check Partner').first().json.transcriptText;
const halving = $input.first().json.halving || 0;
const target = Math.floor(cfg.chunkTargetTokens / Math.pow(2, halving));

const estimateTokens = (s) => Math.ceil(s.length / 3.6);

function splitTranscriptByLines(text, targetTokens) {
  const lines = text.split('\n');
  const chunks = [];
  let buf = [], bufTokens = 0;
  for (const line of lines) {
    const t = estimateTokens(line) + 1;
    if (bufTokens + t > targetTokens && buf.length > 0) {
      chunks.push(buf.join('\n'));
      buf = []; bufTokens = 0;
    }
    buf.push(line); bufTokens += t;
  }
  if (buf.length && buf.join('\n').trim()) chunks.push(buf.join('\n'));
  return chunks;
}

const aliases = $('HTTP Request: Get Speaker Aliases').first().json.data || '';
const SYSTEM = `You are preparing a meeting transcript for embedding in a semantic knowledge base. Transform the raw transcript into an enriched, topic-segmented document that will produce high-quality, independently retrievable chunks when split.

## Speaker Name Normalization

Apply the speaker alias map supplied in the \`SPEAKER_ALIASES\` context block below. If you encounter a speaker whose raw name is NOT in that map, do NOT guess a canonical form — pass the name through unchanged AND list it under "=== UNRESOLVED SPEAKERS ===" at the end of your output.

${aliases}

## Pass 1 — Clean the transcript

- Apply speaker normalization above
- Fix obvious transcription artifacts: "gpt four" → "GPT-4", "llm" → "LLM", "open a i" → "OpenAI"
- Remove pure filler (stutters, "um", "uh") only when they add no meaning
- Preserve all timestamps and speaker attribution exactly

## Pass 2 — Segment by topic

Divide the transcript into coherent topic blocks. Start a new segment when the conversation meaningfully shifts subject. For each segment, prepend a structured header:

<!--SEGMENT
topic: <2–5 word label>
speakers: <comma-separated list of speakers who contribute>
keywords: <8–12 terms: tools, models, concepts, companies, people explicitly mentioned>
summary: <2–3 sentence description of what this segment covers and why it matters>
-->

Target 300–500 words per segment body. If a topic recurs later, open a new segment — do not merge non-contiguous discussion.

## Pass 3 — Inline annotations

Within each segment body, mark key moments:

- When a tool, service, model, or product is named: append \`[tool:name]\` after first mention
- When someone asks a question: wrap with \`<Q>\` ... \`</Q>\`
- When someone answers it: wrap with \`<A>\` ... \`</A>\`
- When a URL or resource is shared: append \`[link:url-or-description]\`
- When a sentence contains a concrete recommendation or takeaway: prefix with ▶

## Output format

This is ONE PART of a longer transcript. Emit segments for the portion you are given. Include a \`=== SESSION ===\` header block (date, duration_estimate, main_themes) and, if any speakers were not in the alias map, a trailing \`=== UNRESOLVED SPEAKERS ===\` block. Both are merged across parts downstream.

## Quality constraints

- Do not invent or infer content not present in the source
- Every segment must be independently understandable
- Segment header \`keywords\` and \`summary\` are what get embedded — make them precise and information-dense
- Prefer 8 focused segments over 4 sprawling ones`;

return splitTranscriptByLines(src, target).map((chunk, i) => ({
  json: {
    stepName: 'prep',
    model: cfg.model,
    maxTokens: cfg.maxTokens,
    reasoningEffort: cfg.reasoningEffort,
    expect: 'prep.chunk',
    chunkIndex: i,
    system: SYSTEM,
    user: chunk,
  },
}));
```

- [ ] **Step 4: Add `Code: Aggregate Prep`**

```js
const items = $input.all().map((i) => i.json);
const failed = items.filter((i) => !i.ok);
if (failed.length) {
  const f = failed[0];
  throw new Error(
    `Prep step failed on chunk ${f.chunkIndex} after ${f.attempts} attempts ` +
    `(failureKind=${f.failureKind}, finishReason=${f.finishReason}). No artifact written.`
  );
}

function reassemblePrep(texts) {
  const SESSION_RE = /===\s*SESSION\s*===[\s\S]*?(?=\n<!--SEGMENT|\n===|$)/;
  const UNRES_RE = /===\s*UNRESOLVED SPEAKERS\s*===([\s\S]*)$/;
  let header = null;
  const bodies = [], unresolved = new Set();
  for (const raw of texts) {
    let t = raw;
    const u = t.match(UNRES_RE);
    if (u) {
      u[1].split('\n').map((l) => l.trim()).filter((l) => l.startsWith('-')).forEach((l) => unresolved.add(l));
      t = t.slice(0, u.index);
    }
    const h = t.match(SESSION_RE);
    if (h) { if (header === null) header = h[0].trim(); t = t.slice(0, h.index) + t.slice(h.index + h[0].length); }
    if (t.trim()) bodies.push(t.trim());
  }
  let out = (header ? header + '\n\n' : '') + bodies.join('\n\n');
  if (unresolved.size) out += '\n\n=== UNRESOLVED SPEAKERS ===\n' + [...unresolved].join('\n');
  return out;
}

const ordered = items.slice().sort((a, b) => a.chunkIndex - b.chunkIndex);
return [{
  json: {
    preparedTranscript: reassemblePrep(ordered.map((i) => i.text)),
    chunkCount: ordered.length,
    totalCost: ordered.reduce((s, i) => s + ((i.usage && i.usage.cost) || 0), 0),
  },
}];
```

- [ ] **Step 5: Add the Execute Workflow node and rewire**

Add:

```json
{
  "parameters": {
    "workflowId": { "__rl": true, "value": "openrouterCall", "mode": "list", "cachedResultName": "OpenRouter Call" },
    "options": { "waitForSubWorkflow": true }
  },
  "id": "ee000000-0000-4000-8000-0000000000e1",
  "name": "Execute: Prep via OpenRouter",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1.2,
  "position": [1340, 460]
}
```

Rewire so `HTTP Request: Get Speaker Aliases` → `Code: Split Prep` → `Execute: Prep via OpenRouter` → `Code: Aggregate Prep` → `Code: Save prepared-transcript.md`. Delete `LLM: Prep-Prompt` and `OpenRouter Chat Model 5`, and remove their entries from `connections`.

Then update `Code: Save prepared-transcript.md` to read `$json.preparedTranscript` instead of `$json.text`.

- [ ] **Step 6: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh w1-prep.test.js`
Expected: `pass 4`, `fail 0`.

- [ ] **Step 7: Verify no orphaned references remain**

Run:
```bash
python3 -c "
import json; w=json.load(open('workflows/merged-call-summarizer.json'))
names={n['name'] for n in w['nodes']}
assert 'LLM: Prep-Prompt' not in names, 'old prep node still present'
assert 'OpenRouter Chat Model 5' not in names, 'orphaned model sub-node'
for src,conns in w['connections'].items():
    assert src in names, f'connection from missing node {src}'
    for out in conns.values():
        for grp in out:
            for c in grp: assert c['node'] in names, f'connection to missing node {c[\"node\"]}'
print('graph consistent')"
```
Expected: `graph consistent`.

- [ ] **Step 8: Commit**

```bash
git add workflows/merged-call-summarizer.json tests/workflows/w1-prep.test.js
git commit -m "feat(w1): chunk Prep-Prompt through the shared OpenRouter component"
```

---

### Task 9: W1 — chunked Extract Signal (map-reduce)

**Files:**
- Modify: `workflows/merged-call-summarizer.json`
- Create: `tests/workflows/w1-signal.test.js`

**Interfaces:**
- Consumes: Task 7 config, Task 3 library, W3 contract.
- Produces: `Code: Aggregate Signal` emits `{ signalText }` consumed by the existing `Code: Save extracted-signal.md`. Heading level is normalized to H2 here (spec §4.6).

- [ ] **Step 1: Write the failing tests**

Create `tests/workflows/w1-signal.test.js`:

```js
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
  retry: { componentAttempts: 3, callerHalvings: 2 },
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh w1-signal.test.js`
Expected: FAIL with `node not found: Code: Split Signal`.

- [ ] **Step 3: Add `Code: Split Signal`**

```js
const cfg = $('Code: Pipeline Config').first().json.steps.signalMap;
const src = $('Code: Validate and Check Partner').first().json.transcriptText;
const halving = $input.first().json.halving || 0;
const target = Math.floor(cfg.chunkTargetTokens / Math.pow(2, halving));

const estimateTokens = (s) => Math.ceil(s.length / 3.6);
function splitTranscriptByLines(text, targetTokens) {
  const lines = text.split('\n');
  const chunks = [];
  let buf = [], bufTokens = 0;
  for (const line of lines) {
    const t = estimateTokens(line) + 1;
    if (bufTokens + t > targetTokens && buf.length > 0) { chunks.push(buf.join('\n')); buf = []; bufTokens = 0; }
    buf.push(line); bufTokens += t;
  }
  if (buf.length && buf.join('\n').trim()) chunks.push(buf.join('\n'));
  return chunks;
}

const SYSTEM = `You are analysing ONE PART of a longer coaching-call transcript. Extract the signal from this part only — the information that would help a future reader understand what was discussed, who said what, and what artefacts or resources were referenced.

Emit a markdown document using H2 headings drawn from exactly these six lowercase slugs, in this order: general, insights, qa, tools, links, decisions. Omit a section entirely if this part contains nothing for it. Do not invent new sections.

## general
A short narrative of what this part covered. Factual, not promotional.

## insights
Bullet points of the most valuable takeaways surfaced in this part. Each bullet self-contained. Attribute the speaker when it matters.

## qa
Pairs of questions and answers, formatted:
**Q (Questioner):** ...
**A (Answerer):** ...
Include only exchanges where both sides had real content.

## tools
Bullet list of tools, products, frameworks, platforms or services mentioned. One line each, with a 5–15 word note on context.

## links
Bullet list of URLs, repositories, documents or resources shared. One line each with a brief descriptor.

## decisions
Bullet list of commitments, action items or decisions. Phrase each as actor + action.

Do not invent content not present in this part. Results from all parts are merged downstream.`;

return splitTranscriptByLines(src, target).map((chunk, i) => ({
  json: {
    stepName: 'signal.map',
    model: cfg.model,
    maxTokens: cfg.maxTokens,
    reasoningEffort: cfg.reasoningEffort,
    expect: 'signal.map',
    chunkIndex: i,
    system: SYSTEM,
    user: chunk,
  },
}));
```

- [ ] **Step 4: Add `Code: Build Signal Reduce`**

```js
const cfg = $('Code: Pipeline Config').first().json.steps.signalReduce;
const items = $input.all().map((i) => i.json);
const failed = items.filter((i) => !i.ok);
if (failed.length) {
  const f = failed[0];
  throw new Error(`Signal map failed on chunk ${f.chunkIndex} after ${f.attempts} attempts (failureKind=${f.failureKind}). No artifact written.`);
}

const chatText = $('Code: Validate and Check Partner').first().json.chatText || '';
const ordered = items.slice().sort((a, b) => a.chunkIndex - b.chunkIndex);
const parts = ordered.map((i, n) => `### PART ${n + 1}\n\n${i.text}`).join('\n\n');

const SYSTEM = `You are merging per-part signal extractions from a single coaching call into one consolidated document, and folding in the call's chat log.

Emit a markdown document with exactly six H2 sections, using these literal lowercase slugs in this order:

## general
## insights
## qa
## tools
## links
## decisions

Rules:
- general: write a 2–4 paragraph narrative covering the WHOLE call, synthesized across all parts — not a concatenation of the per-part summaries.
- insights, qa, decisions: merge across parts, preserving chronological order and dropping duplicates.
- tools and links: the chat log is the primary source for these. Merge chat-log entries with those found in the parts, and DEDUPE aggressively — the same URL or tool must appear once.
- Omit a section entirely if there is genuinely no content for it.
- Do not invent content that is not present in the parts or the chat log.

SIZE BUDGET: the complete document must not exceed approximately ${cfg.budgetTokens} tokens (roughly ${cfg.budgetTokens * 4} characters). If the material exceeds that, cut the weakest insights and least-useful Q&A first. Never cut links or tools to fit.

CRITICAL: output the sections in EXACTLY the order listed above. Do not re-order, merge or rename them.`;

return [{
  json: {
    stepName: 'signal.reduce',
    model: cfg.model,
    maxTokens: cfg.maxTokens,
    reasoningEffort: cfg.reasoningEffort,
    expect: 'signal.reduce',
    chunkIndex: 0,
    system: SYSTEM,
    user: `# PER-PART EXTRACTIONS\n\n${parts}\n\n# ZOOM CHAT LOG\n\n${chatText}`,
  },
}];
```

- [ ] **Step 5: Add `Code: Aggregate Signal`**

```js
const CANON = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'];
const items = $input.all().map((i) => i.json);
const failed = items.filter((i) => !i.ok);
if (failed.length) {
  const f = failed[0];
  throw new Error(`Signal reduce failed after ${f.attempts} attempts (failureKind=${f.failureKind}). No artifact written.`);
}

// Normalize heading level to H2 (spec 4.6: the model emits H1 on roughly half of runs).
let md = items[0].text.replace(/^#{1,3}[ \t]+([a-z]+)[ \t]*$/gm, (m, slug) =>
  CANON.includes(slug) ? `## ${slug}` : m);

const found = [];
const re = /^##[ \t]+([a-z]+)[ \t]*$/gm;
let m;
while ((m = re.exec(md)) !== null) if (CANON.includes(m[1])) found.push(m[1]);
const missing = CANON.filter((s) => !found.includes(s));
if (missing.length) {
  throw new Error(`extracted-signal is missing required section(s): ${missing.join(', ')}. No artifact written.`);
}

return [{ json: { signalText: md, totalCost: items.reduce((s, i) => s + ((i.usage && i.usage.cost) || 0), 0) } }];
```

- [ ] **Step 6: Add the two Execute Workflow nodes and rewire**

Add `Execute: Signal Map via OpenRouter` and `Execute: Signal Reduce via OpenRouter`, both shaped exactly like the node in Task 8 Step 5 (same `workflowId` resourceLocator, `waitForSubWorkflow: true`), with distinct `id` and `name` values and their own positions.

Wire: `Code: Merge Content` → `Code: Split Signal` → `Execute: Signal Map via OpenRouter` → `Code: Build Signal Reduce` → `Execute: Signal Reduce via OpenRouter` → `Code: Aggregate Signal` → `Code: Save extracted-signal.md`. Delete `LLM: Extract Signal` and `OpenRouter Chat Model 1`. Update `Code: Save extracted-signal.md` to read `$json.signalText`.

- [ ] **Step 7: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh w1-signal.test.js`
Expected: `pass 5`, `fail 0`.

- [ ] **Step 8: Re-run the graph-consistency check from Task 8 Step 7**

Expected: `graph consistent`.

- [ ] **Step 9: Commit**

```bash
git add workflows/merged-call-summarizer.json tests/workflows/w1-signal.test.js
git commit -m "feat(w1): chunk Extract Signal into map-reduce via OpenRouter component"
```

---

### Task 10: W1 — section-mapped Community Post, plus Compress and Weekly Invite

Section mapping makes ordering a property of code rather than prompt discipline, which is why the `CRITICAL: output sections in EXACTLY this order` instruction can be dropped here.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`
- Create: `tests/workflows/w1-post.test.js`

**Interfaces:**
- Consumes: `Code: Aggregate Signal` (`signalText`), Task 7 config.
- Produces: `Code: Assemble Post` emits `{ communityPostText }`; the converted Compress and Invite steps emit `{ compressedText }` and `{ inviteText }`.

- [ ] **Step 1: Write the failing tests**

Create `tests/workflows/w1-post.test.js`:

```js
const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const { runCodeNode } = require('./harness');

const cfg = {
  steps: {
    postSection: { model: 'z-ai/glm-5.3-flash', maxTokens: 16384, reasoningEffort: 'low' },
    compress:    { model: 'z-ai/glm-5.3-flash', maxTokens: 16384, reasoningEffort: 'low' },
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
  assert.deepStrictEqual(out.map((i) => i.json.section),
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh w1-post.test.js`
Expected: FAIL with `node not found: Code: Split Post Sections`.

- [ ] **Step 3: Add `Code: Split Post Sections`**

```js
const cfg = $('Code: Pipeline Config').first().json.steps.postSection;
const md = $input.first().json.signalText;

const CANON = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'];
function splitSignalIntoSections(src) {
  const out = {};
  const re = /^#{1,3}[ \t]+([a-z]+)[ \t]*$/gm;
  let m; const marks = [];
  while ((m = re.exec(src)) !== null) marks.push({ slug: m[1], start: m.index, bodyStart: re.lastIndex });
  for (let i = 0; i < marks.length; i++) {
    const end = i + 1 < marks.length ? marks[i + 1].start : src.length;
    const body = src.slice(marks[i].bodyStart, end).trim();
    if (CANON.includes(marks[i].slug) && body) out[marks[i].slug] = body;
  }
  return out;
}

const BRIEF = {
  general:   'Write ONE short paragraph summarizing the overall value and themes of the call.',
  insights:  'Summarize the strongest practical or strategic takeaways as short lines, one per takeaway.',
  qa:        'Present the most useful question-and-answer pairs clearly and concisely, one exchange per block.',
  tools:     'List the important tools, frameworks and concepts with a short explanation each, one per line.',
  links:     'Present the most useful links and resources in a clean, easy-to-scan way. Write URLs as plain text.',
  decisions: 'List the open questions, follow-ups and commitments worth revisiting, one per line.',
};

const sections = splitSignalIntoSections(md);
return CANON.filter((s) => sections[s]).map((slug, i) => ({
  json: {
    stepName: `post.section.${slug}`,
    section: slug,
    model: cfg.model,
    maxTokens: cfg.maxTokens,
    reasoningEffort: cfg.reasoningEffort,
    expect: 'post.section',
    chunkIndex: i,
    system: `You are writing ONE section of a polished community post about a weekly AI community call, for members who may not have attended live.

${BRIEF[slug]}

IMPORTANT: This post is published on Skool, which does NOT render markdown. Output PLAIN TEXT only. Do NOT use #, **bold**, - bullets, or [links](url). Use line breaks and spacing for readability.

Output ONLY this section's body text. Do NOT write a heading — the heading is added automatically. Do not invent information not present in the input. Keep it concise, skimmable and ready to copy-paste.`,
    user: sections[slug],
  },
}));
```

- [ ] **Step 4: Add `Code: Assemble Post`**

```js
const HEADERS = {
  general:   '📝 SUMMARY',
  insights:  '💡 KEY INSIGHTS',
  qa:        '❓ KEY Q&A',
  tools:     '🛠️ TOOLS AND CONCEPTS MENTIONED',
  links:     '📎 SHARED RESOURCES',
  decisions: '🔄 FOLLOW-UPS WORTH EXPLORING',
};
const ORDER = ['general', 'insights', 'qa', 'tools', 'links', 'decisions'];

const items = $input.all().map((i) => i.json);
const failed = items.filter((i) => !i.ok);
if (failed.length) {
  const f = failed[0];
  throw new Error(`Community post section '${f.section}' failed after ${f.attempts} attempts (failureKind=${f.failureKind}). No artifact written.`);
}

const bySection = new Map(items.map((i) => [i.section, i.text.trim()]));
const post = ORDER
  .filter((s) => bySection.has(s) && bySection.get(s))
  .map((s) => `${HEADERS[s]}\n\n${bySection.get(s)}`)
  .join('\n\n\n');

return [{
  json: {
    communityPostText: post,
    totalCost: items.reduce((sum, i) => sum + ((i.usage && i.usage.cost) || 0), 0),
  },
}];
```

- [ ] **Step 5: Convert Compress and Weekly Invite to W3**

These are not chunked (spec §5.4). Add `Code: Build Compress Request` and `Code: Build Invite Request`, each emitting a single W3 item whose `system` is copied verbatim from the existing `LLM: Compress Post` / `LLM: Weekly Invite` system prompts, with `expect: 'none'`, `chunkIndex: 0`, and model fields drawn from `steps.compress` / `steps.invite`. Add matching `Code: Unwrap Compress` and `Code: Unwrap Invite` nodes:

```js
const items = $input.all().map((i) => i.json);
const failed = items.filter((i) => !i.ok);
if (failed.length) {
  const f = failed[0];
  throw new Error(`Step ${f.stepName} failed after ${f.attempts} attempts (failureKind=${f.failureKind}). No artifact written.`);
}
return [{ json: { text: items[0].text, totalCost: (items[0].usage && items[0].usage.cost) || 0 } }];
```

Delete `LLM: Community Post`, `LLM: Compress Post`, `LLM: Weekly Invite` and `OpenRouter Chat Model 2`, `3`, `4`. Rewire the save nodes to their new sources.

- [ ] **Step 6: Run the whole suite**

Run: `./scripts/test-workflows.sh`
Expected: all tests pass except the two W2 `pipeline-config` cases, which Task 11 fixes.

- [ ] **Step 7: Verify every chainLlm node is gone from W1**

Run:
```bash
python3 -c "
import json; w=json.load(open('workflows/merged-call-summarizer.json'))
bad=[n['name'] for n in w['nodes'] if 'chainLlm' in n['type'] or 'lmChatOpenRouter' in n['type']]
assert not bad, f'leftover LLM nodes: {bad}'
print('W1 fully migrated to the OpenRouter component')"
```
Expected: `W1 fully migrated to the OpenRouter component`.

- [ ] **Step 8: Commit**

```bash
git add workflows/merged-call-summarizer.json tests/workflows/w1-post.test.js
git commit -m "feat(w1): section-map community post, migrate compress and invite to W3"
```

---

### Task 11: W2 — apply the same pattern

W2 keeps its own model assignment: `claude-sonnet-5` for prep and signal (preserving current backfill behaviour), `glm-5.3-flash` for post. Kimi is retired.

**Files:**
- Modify: `workflows/transcript-only-summarizer.json`
- Create: `tests/workflows/w2.test.js`

**Interfaces:**
- Consumes: W3 contract; the same node names and `jsCode` bodies as Tasks 7–10, with W2's own prompts and no chat log.
- Produces: same artifact fields; W2's existing state-file and `/ingest` nodes are untouched.

- [ ] **Step 1: Write the failing test**

Create `tests/workflows/w2.test.js`:

```js
const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode, loadWorkflow } = require('./harness');

test('W2 config retires kimi and keeps sonnet for prep and signal', () => {
  const cfg = runCodeNode('transcript-only-summarizer.json', 'Code: Pipeline Config', {})[0].json;
  assert.strictEqual(cfg.steps.prep.model, 'anthropic/claude-sonnet-5');
  assert.strictEqual(cfg.steps.signalMap.model, 'anthropic/claude-sonnet-5');
  assert.strictEqual(cfg.steps.postSection.model, 'z-ai/glm-5.3-flash');
});

test('W2 has no chainLlm or model sub-nodes left', () => {
  const wf = loadWorkflow('transcript-only-summarizer.json');
  const bad = wf.nodes.filter((n) => /chainLlm|lmChatOpenRouter/.test(n.type)).map((n) => n.name);
  assert.deepStrictEqual(bad, []);
});

test('W2 splits a transcript into prep requests', () => {
  const transcript = Array.from({ length: 4000 }, (_, i) =>
    `[00:${String(Math.floor(i / 60)).padStart(2, '0')}:${String(i % 60).padStart(2, '0')}] Speaker: line ${i}`).join('\n');
  const out = runCodeNode('transcript-only-summarizer.json', 'Code: Split Prep', {
    items: [{ json: { transcriptText: transcript, halving: 0 } }],
    nodes: {
      'Code: Pipeline Config': runCodeNode('transcript-only-summarizer.json', 'Code: Pipeline Config', {})[0].json,
      'Code: Read Session': { transcriptText: transcript },
      'HTTP Request: Get Speaker Aliases': { data: '' },
    },
  });
  assert.ok(out.length >= 1);
  assert.strictEqual(out[0].json.stepName, 'prep');
  assert.strictEqual(out[0].json.model, 'anthropic/claude-sonnet-5');
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `./scripts/test-workflows.sh w2.test.js`
Expected: FAIL with `node not found: Code: Pipeline Config`.

- [ ] **Step 3: Add W2's config node**

Same node shape as Task 7 Step 3, with this `jsCode`:

```js
return [{
  json: {
    steps: {
      prep:         { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, chunkTargetTokens: 15000 },
      signalMap:    { model: 'anthropic/claude-sonnet-5', maxTokens: 16384, chunkTargetTokens: 15000 },
      signalReduce: { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000 },
      postSection:  { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
      compress:     { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
      invite:       { model: 'z-ai/glm-5.3-flash',        maxTokens: 16384, reasoningEffort: 'low' },
    },
    retry: { componentAttempts: 3, callerHalvings: 2 },
  },
}];
```

W2 has no compress or invite step; the keys are present so both workflows share one config shape and one test.

- [ ] **Step 4: Port the split/aggregate nodes**

Add `Code: Split Prep`, `Code: Aggregate Prep`, `Code: Split Signal`, `Code: Build Signal Reduce`, `Code: Aggregate Signal`, `Code: Split Post Sections`, `Code: Assemble Post` using the same `jsCode` as Tasks 8–10, with two W2-specific changes:

1. Replace `$('Code: Validate and Check Partner')` with W2's transcript source node.
2. In `Code: Build Signal Reduce`, W2 has no chat log — set `const chatText = '';` and drop the `# ZOOM CHAT LOG` block from the `user` string.

Add three `Execute Workflow` nodes pointing at `OpenRouter Call`, and delete `LLM: Prep-Prompt (W2)`, `LLM: Extract Signal (W2)`, `LLM: Community Post (W2)` and their three model sub-nodes.

- [ ] **Step 5: Run the full suite**

Run: `./scripts/test-workflows.sh`
Expected: all tests pass, including both `pipeline-config` W2 cases.

- [ ] **Step 6: Commit**

```bash
git add workflows/transcript-only-summarizer.json tests/workflows/w2.test.js
git commit -m "feat(w2): migrate backfill workflow to chunked OpenRouter component"
```

---

### Task 12: Caller-level halving retry

Spec §4.2 defines two retry levels. Tasks 4–11 implemented only the component level (inside W3). The splitters already accept a `halving` input and divide `chunkTargetTokens` by `2^halving`, but nothing increments it and no edge loops back — so a step that exhausts W3's ladder currently throws immediately instead of re-splitting smaller. This task closes that loop for all three chunked steps in both workflows.

**Files:**
- Modify: `workflows/merged-call-summarizer.json`
- Modify: `workflows/transcript-only-summarizer.json`
- Create: `tests/workflows/halving.test.js`

**Interfaces:**
- Consumes: W3 result items (Task 6), `retry.callerHalvings` from `Code: Pipeline Config` (Task 7).
- Produces: `Code: Check Chunks` emits either the unchanged result items with `retry: false`, or a single `{ retry: true, halving }` item routed back to the splitter. Aggregate nodes are unchanged and keep their throw as a backstop.

- [ ] **Step 1: Write the failing tests**

Create `tests/workflows/halving.test.js`:

```js
const { test } = require('node:test');
const assert = require('node:assert');
const { runCodeNode } = require('./harness');

const cfg = { steps: {}, retry: { componentAttempts: 3, callerHalvings: 2 } };
const ok = (i) => ({ json: { chunkIndex: i, ok: true, text: 'fine', attempts: 1, usage: { cost: 0 } } });
const bad = (i) => ({ json: { chunkIndex: i, ok: false, failureKind: 'content_truncated', attempts: 3, text: '', usage: { cost: 0 } } });

for (const file of ['merged-call-summarizer.json', 'transcript-only-summarizer.json']) {
  test(`${file}: passes results through when every chunk succeeded`, () => {
    const out = runCodeNode(file, 'Code: Check Chunks', {
      items: [ok(0), ok(1)],
      nodes: { 'Code: Pipeline Config': cfg, 'Code: Split Prep': { halving: 0 } },
    });
    assert.strictEqual(out.length, 2);
    assert.strictEqual(out[0].json.retry, false);
  });

  test(`${file}: requests a halving when a chunk failed and budget remains`, () => {
    const out = runCodeNode(file, 'Code: Check Chunks', {
      items: [ok(0), bad(1)],
      nodes: { 'Code: Pipeline Config': cfg, 'Code: Split Prep': { halving: 0 } },
    });
    assert.strictEqual(out.length, 1);
    assert.strictEqual(out[0].json.retry, true);
    assert.strictEqual(out[0].json.halving, 1);
  });

  test(`${file}: throws once halvings are exhausted`, () => {
    assert.throws(
      () => runCodeNode(file, 'Code: Check Chunks', {
        items: [bad(0)],
        nodes: { 'Code: Pipeline Config': cfg, 'Code: Split Prep': { halving: 2 } },
      }),
      /No artifact written/,
    );
  });
}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./scripts/test-workflows.sh halving.test.js`
Expected: FAIL with `node not found: Code: Check Chunks`.

- [ ] **Step 3: Make each splitter publish its own halving level**

In `Code: Split Prep`, `Code: Split Signal` and `Code: Split Post Sections` in **both** workflows, add `halving` to every emitted item so the checker can read the level that produced these chunks. In each splitter's returned object, add one field alongside `chunkIndex`:

```js
    halving: halving,
```

For `Code: Split Post Sections`, which has no `halving` variable, add this line near the top and include the same field:

```js
const halving = ($input.first().json && $input.first().json.halving) || 0;
```

- [ ] **Step 4: Add `Code: Check Chunks` to both workflows**

One instance per chunked step. Give each a distinct name suffix — `Code: Check Chunks (Prep)`, `Code: Check Chunks (Signal)`, `Code: Check Chunks (Post)` — and set the `SPLITTER` constant to the matching splitter node name. The test targets the base name `Code: Check Chunks`, so also keep one node with exactly that name for the prep step; name the other two with suffixes.

```js
const cfg = $('Code: Pipeline Config').first().json;
const maxHalvings = cfg.retry.callerHalvings;
const SPLITTER = 'Code: Split Prep';
const halving = ($(SPLITTER).first().json.halving) || 0;

const items = $input.all().map((i) => i.json);
const failed = items.filter((i) => !i.ok);

if (failed.length === 0) {
  return items.map((json) => ({ json: { ...json, retry: false } }));
}

if (halving >= maxHalvings) {
  const f = failed[0];
  throw new Error(
    `Step failed on chunk ${f.chunkIndex} after ${f.attempts} component attempts and ` +
    `${halving} re-splits (failureKind=${f.failureKind}, finishReason=${f.finishReason}). ` +
    `No artifact written.`
  );
}

return [{ json: { retry: true, halving: halving + 1, failedChunks: failed.length } }];
```

- [ ] **Step 5: Add the routing IF node and loop-back edge**

For each chunked step add an `IF` node — `IF: Retry Step (Prep)` and so on:

```json
{
  "parameters": {
    "conditions": {
      "options": { "caseSensitive": true, "version": 2 },
      "conditions": [{
        "leftValue": "={{ $json.retry }}",
        "rightValue": true,
        "operator": { "type": "boolean", "operation": "true" }
      }],
      "combinator": "and"
    }
  },
  "id": "aa000000-0000-4000-8000-0000000000a1",
  "name": "IF: Retry Step (Prep)",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [1780, 460]
}
```

Rewire the prep chain to:

`Code: Split Prep` → `Execute: Prep via OpenRouter` → `Code: Check Chunks` → `IF: Retry Step (Prep)` → **true** back to `Code: Split Prep`; **false** to `Code: Aggregate Prep`.

Repeat for signal (loop back to `Code: Split Signal`, false to `Code: Build Signal Reduce`) and post (loop back to `Code: Split Post Sections`, false to `Code: Assemble Post`). Apply the same wiring to W2's prep, signal and post chains.

- [ ] **Step 6: Run tests to verify they pass**

Run: `./scripts/test-workflows.sh halving.test.js`
Expected: `pass 6`, `fail 0`.

- [ ] **Step 7: Run the full suite and the graph-consistency check**

```bash
./scripts/test-workflows.sh
python3 -c "
import json
for f in ('merged-call-summarizer','transcript-only-summarizer'):
    w=json.load(open(f'workflows/{f}.json'))
    names={n['name'] for n in w['nodes']}
    for src,conns in w['connections'].items():
        assert src in names, f'{f}: connection from missing node {src}'
        for out in conns.values():
            for grp in out:
                for c in grp: assert c['node'] in names, f'{f}: connection to missing {c[\"node\"]}'
    print(f, 'graph consistent')"
```
Expected: all tests pass and both workflows report `graph consistent`.

- [ ] **Step 8: Commit**

```bash
git add workflows/ tests/workflows/halving.test.js
git commit -m "feat(workflows): add caller-level halving retry for chunked steps"
```

---

### Task 13: Live validation

Executes spec §8. Criterion 5 is the one that matters — it is the exact failure that went undetected on 2026-09-01.

**Files:**
- Modify: `CLAUDE.md` (status section)

- [ ] **Step 1: Deploy all three workflows**

```bash
cd ~/n8n
for f in openrouter-call merged-call-summarizer transcript-only-summarizer; do
  python3 -c "
import json,sys; p='workflows/$f.json'; w=json.load(open(p))
for n in w['nodes']:
    for c in (n.get('credentials') or {}).values():
        if c.get('id')=='PLACEHOLDER': c['id']='1YRALvHjmQ3E6pqd'
json.dump(w, open('/tmp/$f.json','w'), indent=2)"
  docker cp /tmp/$f.json n8n:/tmp/$f.json
  docker exec n8n n8n import:workflow --input=/tmp/$f.json
done
```
Expected: three `Successfully imported 1 workflow.` lines.

- [ ] **Step 2: Confirm the Execute Workflow ids resolve**

```bash
docker exec n8n_db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -t -A -c "select id,name from workflow_entity order by id;"'
```
Expected: `openrouterCall|OpenRouter Call` present alongside ids 1–6. If W3's id differs from the resourceLocator `value` in W1/W2, fix those three nodes and re-import.

- [ ] **Step 3: Resolve the chat-log date mismatch (spec §9)**

`watch/2026-09-01-zoom-chat.txt` contains chat timestamped `2026-08-25`, so 2026-09-01's `links` section may derive from the wrong call:

```bash
cd ~/n8n
head -1 watch/2026-09-01-zoom-chat.txt
head -1 watch/2026-08-25-zoom-chat.txt
diff -q watch/2026-09-01-zoom-chat.txt watch/2026-08-25-zoom-chat.txt && echo "IDENTICAL — 09-01 chat is a copy of 08-25"
```

If the two files are identical, the correct 09-01 chat log must be re-copied from the Mac before re-running; otherwise the regenerated artifacts will carry last week's links. **Stop and ask the operator** rather than regenerating on known-wrong input. If the first line simply shows Zoom's own labelling quirk and the content is genuinely from 09-01, proceed.

- [ ] **Step 4: Re-run 2026-09-01 end to end**

```bash
mv output/2026-09-01 output/2026-09-01.pre-chunking
docker exec -e N8N_RUNNERS_BROKER_PORT=5680 -e N8N_RUNNERS_AUTH_TOKEN=foo \
  n8n n8n execute --id 5 2>&1 | grep -E '"status"|message' | head
```
Expected: `"status": "success"`.

- [ ] **Step 5: Check criteria 1–4**

```bash
cd ~/n8n/output/2026-09-01
wc -c *
grep -c '^## \(general\|insights\|qa\|tools\|links\|decisions\)$' extracted-signal.md
grep -nE '^#|\*\*|^- ' community-post.md | head
```
Expected: five artifacts, none 0 bytes; `prepared-transcript.md` between 140 KB and 180 KB (0.6–0.7× the 247 KB transcript); the grep returns `6`; the markdown grep returns nothing.

- [ ] **Step 6: Check criterion 5 — truncation must fail loudly**

```bash
cd ~/n8n
python3 -c "
import json; p='/tmp/merged-call-summarizer.json'; w=json.load(open(p))
n=[x for x in w['nodes'] if x['name']=='Code: Pipeline Config'][0]
n['parameters']['jsCode']=n['parameters']['jsCode'].replace('maxTokens: 32768','maxTokens: 200').replace('maxTokens: 16384','maxTokens: 200')
json.dump(w, open('/tmp/trunc-test.json','w'), indent=2)"
docker cp /tmp/trunc-test.json n8n:/tmp/trunc-test.json
docker exec n8n n8n import:workflow --input=/tmp/trunc-test.json
docker exec -e N8N_RUNNERS_BROKER_PORT=5680 -e N8N_RUNNERS_AUTH_TOKEN=foo \
  n8n n8n execute --id 5 2>&1 | grep -E '"status"|No artifact written' | head
```
Expected: `"status": "error"` **and** a `No artifact written` message. A `success` here means the guard is not wired — stop and fix before proceeding.

- [ ] **Step 7: Restore the real config**

```bash
docker cp /tmp/merged-call-summarizer.json n8n:/tmp/restore.json
docker exec n8n n8n import:workflow --input=/tmp/restore.json
docker exec -e N8N_RUNNERS_BROKER_PORT=5680 -e N8N_RUNNERS_AUTH_TOKEN=foo \
  n8n n8n execute --id 5 2>&1 | grep '"status"'
```
Expected: `"status": "success"`, and `output/2026-09-01/` is repopulated.

- [ ] **Step 8: Check criterion 7 — a normal-size call is unchanged**

```bash
cd ~/n8n
cp output/2026-08-25/extracted-signal.md /tmp/0825-signal-before.md
# Re-run 2026-08-25 through the new pipeline, then compare shape (not wording):
wc -c /tmp/0825-signal-before.md output/2026-08-25/extracted-signal.md
grep -c '^## ' /tmp/0825-signal-before.md output/2026-08-25/extracted-signal.md
```
Expected: both have 6 sections and sizes within roughly ±30% of each other.

- [ ] **Step 9: Check criterion 8 — ingestion still works**

```bash
curl -s http://10.1.30.10:8999/sessions | python3 -m json.tool | grep -c 2026-09-01
```
Expected: `1` or more.

- [ ] **Step 10: Remove the pre-chunking backup and commit artifacts**

```bash
cd ~/n8n
diff -q output/2026-09-01.pre-chunking/transcript.txt output/2026-09-01/transcript.txt && rm -rf output/2026-09-01.pre-chunking
git add output/2026-09-01
git commit -m "chore(output): regenerate 2026-09-01 artifacts under chunked pipeline"
```

- [ ] **Step 11: Update CLAUDE.md**

Add to the "Current status" section:

```markdown
**Chunked LLM pipeline — DEPLOYED (2026-09-02).** Both summarizer workflows now call a shared `OpenRouter Call` sub-workflow (n8n id `openrouterCall`) instead of Basic LLM Chain nodes. Prep, Extract Signal and Community Post are chunked; truncation and reasoning-burn are detected via `finish_reason` and fail the execution instead of writing a partial artifact. Models are configured per step in each workflow's `Code: Pipeline Config` node. See `docs/superpowers/specs/2026-09-02-chunked-llm-pipeline-design.md`.
```

- [ ] **Step 12: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: record chunked LLM pipeline deployment"
```
