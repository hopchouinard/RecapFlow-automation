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

  // Finding C: componentAttempts was inert -- W3 never read it, both callers never passed
  // it, and both IF: Retry Step nodes plus Code: Escalate/Escalate 2 hardcode a 3-attempt
  // ceiling (three explicitly unrolled OpenRouter stages). Removed rather than wired up:
  // the ladder is structural, so a value above 3 couldn't be honoured and honouring only
  // values below 3 would be more confusing than not offering the knob at all.
  test(`${file}: componentAttempts is not present on the retry config (Finding C)`, () => {
    const out = runCodeNode(file, 'Code: Pipeline Config', {});
    const cfg = out[0].json;
    assert.strictEqual(cfg.retry.componentAttempts, undefined,
      'componentAttempts must be removed, not just left unread -- it was dead configuration');
  });

  test(`${file}: kimi is retired from the config node`, () => {
    const wf = loadWorkflow(file);
    const cfgCode = wf.nodes.find((n) => n.name === 'Code: Pipeline Config').parameters.jsCode;
    assert.ok(!/kimi/i.test(cfgCode), 'kimi must be retired');
  });
}
