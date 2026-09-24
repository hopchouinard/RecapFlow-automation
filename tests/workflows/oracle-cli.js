// Test-only JSON bridge. Production Python never executes workflow JavaScript.
const fs = require('node:fs');
const { runCodeNode } = require('./harness');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
try {
  const results = input.map(({ workflow, node, context = {} }) => runCodeNode(workflow, node, {
    ...context, fsMock: { readFileSync() { throw new Error('oracle filesystem access prohibited'); } },
  }));
  process.stdout.write(JSON.stringify(results));
} catch (error) {
  process.stderr.write(error.message);
  process.exitCode = 1;
}
