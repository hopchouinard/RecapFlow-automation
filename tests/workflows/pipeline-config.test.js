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

  test(`${file}: kimi is retired from the config node`, () => {
    const wf = loadWorkflow(file);
    const cfgCode = wf.nodes.find((n) => n.name === 'Code: Pipeline Config').parameters.jsCode;
    assert.ok(!/kimi/i.test(cfgCode), 'kimi must be retired');
  });
}
