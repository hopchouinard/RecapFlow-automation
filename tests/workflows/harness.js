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
