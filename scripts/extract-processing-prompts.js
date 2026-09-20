// Explicit development extraction; writes only packaged prompt/config snapshots.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { runCodeNode } = require('../tests/workflows/harness');
const root = path.resolve(__dirname, '..');
const output = path.join(root, 'community-brain/src/community_brain/processing/prompts-v1.json');
const result = {};
for (const [mode, workflow] of Object.entries({weekly:'merged-call-summarizer.json', transcript_backfill:'transcript-only-summarizer.json'})) {
  const config = runCodeNode(workflow, 'Code: Pipeline Config')[0].json;
  const nodes = {
    'Code: Pipeline Config': config,
    'Code: Validate and Check Partner': {transcriptText:'source',chatText:'chat'},
    'Code: Read Transcript': {transcriptText:'source'},
    'HTTP Request: Get Speaker Aliases': {data:'@@ALIASES@@'},
  };
  const call = (node, json={}) => runCodeNode(workflow, node, {nodes,items:[{json}]});
  const prompts = {};
  prompts.prep = call('Code: Split Prep')[0].json.system;
  prompts.signalMap = call('Code: Split Signal')[0].json.system;
  config.steps.signalReduce.budgetTokens = 87654321;
  prompts.signalReduce = call('Code: Build Signal Reduce', {ok:true,text:'signal',chunkIndex:0})[0].json.system
    .replaceAll('350617284', '@@BUDGET_CHARS@@').replaceAll('87654321', '@@BUDGET_TOKENS@@');
  config.steps.signalReduce.budgetTokens = 8000;
  prompts.postSection = Object.fromEntries(call('Code: Split Post Sections', {
    signalText: ['general','insights','qa','tools','links','decisions'].map(s=>`## ${s}\nbody`).join('\n\n'),
  }).map(x=>[x.json.section,x.json.system]));
  if (mode === 'weekly') {
    prompts.compress = call('Code: Build Compress Request', {communityPostText:'post'})[0].json.system;
    prompts.invite = call('Code: Build Invite Request', {compressedText:'post',formattedDate:'date'})[0].json.system;
  }
  result[mode] = {config,prompts,workflow,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(root,'workflows',workflow))).digest('hex')};
}
fs.mkdirSync(path.dirname(output), {recursive:true});
fs.writeFileSync(output, JSON.stringify(result,null,2)+'\n');
