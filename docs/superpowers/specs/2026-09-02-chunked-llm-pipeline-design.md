# Chunked LLM Pipeline + Shared OpenRouter Component — Design

**Status:** Draft
**Date:** 2026-09-02
**Owner:** Solo operator
**Applies to:** `merged-call-summarizer.json` (n8n id 5, "W1") and `transcript-only-summarizer.json` (n8n id 6, "W2")
**Supersedes:** direct use of `@n8n/n8n-nodes-langchain.chainLlm` + `lmChatOpenRouter` for all LLM steps in W1 and W2.

---

## 1. Motivation

Coaching calls have grown. The 2026-09-01 call produced a 247 KB transcript (~62k tokens) against a ~100 KB norm earlier in the summer. That run failed in three places, and **every failure reported `status: success`**:

| Artifact | Expected | Actual |
|---|---|---|
| `output/2026-09-01/prepared-transcript.md` | ~150 KB | **absent** |
| `output/2026-09-01/community-post-compressed.md` | ~8 KB | **0 bytes** |
| `output/2026-09-01/community-post.md` | ~9 KB | produced only after a manual re-run |

The operator re-ran the workflow twice to get partial output. `2026-07-28` (234 KB transcript) shows the same disease in milder form: a 71 KB `prepared-transcript.md`, versus 65 KB produced from a *98 KB* transcript on 07-14 — heavy silent loss at 2.4× the input.

The pipeline has no way to tell a complete answer from a truncated one, so it writes whatever it gets and moves on.

## 2. Root cause (empirically established 2026-09-02)

All findings below were reproduced against the live container and the live OpenRouter credential.

### 2.1 The 32768 ceiling is a UI constraint, not a runtime one

`LmChatOpenRouter.node.js` declares `maxTokens` with `typeOptions: { maxValue: 32768 }`. `supplyData` then does:

```js
const model = new ChatOpenAI({
  apiKey, model: modelName,
  ...options,          // maxTokens spread straight through
  timeout, maxRetries, configuration, callbacks,
  modelKwargs: Object.keys(modelKwargs).length > 0 ? modelKwargs : undefined,
});
```

No clamping. A workflow imported via CLI with `maxTokens: 65536` sends 65536. **But** opening that node in the editor and saving re-clamps it to 32768 silently, so values above the clamp are fragile to routine UI edits and must not be load-bearing.

### 2.2 Reasoning tokens bill against `max_tokens`, and can consume all of it

Direct OpenRouter call, `z-ai/glm-5.3-flash`, `max_tokens: 400`, asking for a 600-word essay:

```json
{ "http": 200, "finish_reason": "length",
  "content_len": 0, "reasoning_len": 1808,
  "usage": { "completion_tokens": 400,
             "completion_tokens_details": { "reasoning_tokens": 398 } } }
```

398 of 400 completion tokens went to reasoning; 2 remained for content, so content was empty. This is the mechanism behind the 0-byte `community-post-compressed.md`. **GLM 5.3 Flash, OpenRouter and LangChain are all behaving correctly.**

Claude Sonnet truncates the conventional way instead — partial text cut mid-sentence, ~2000 chars, `finish_reason: length`. So the pipeline must detect **two** distinct truncation shapes.

### 2.3 n8n's `chainLlm` destroys the truncation signal

`chainLlm` emits an item whose only key is `text`. `finish_reason`, `reasoning`, and `usage` are all discarded, and empty content is treated as success. OpenRouter reports the truncation perfectly; n8n throws the report away. This is why nothing ever went red.

### 2.4 `reasoning_effort` works at the API, but is unreachable through the node

| Call path | Result |
|---|---|
| OpenRouter direct, `reasoning: {effort: "low"}` | `reasoning_tokens: 0`, 2145 chars content |
| OpenRouter direct, `reasoning_effort: "low"` (flat) | `reasoning_tokens: 0`, 2101 chars content |
| OpenRouter direct, `reasoning: {enabled: false}` | rejected — *"Reasoning is mandatory for this endpoint and cannot be disabled"* |
| n8n `chainLlm`, `options.reasoningEffort: "low"` | **0 chars** — not forwarded |
| n8n `chainLlm`, `options.reasoning_effort: "low"` | **0 chars** — not forwarded |

Injection through `options` cannot work: `modelKwargs` is assigned *after* `...options` in the constructor and overwrites anything smuggled in.

### 2.5 `reasoning_effort: "low"` is a hint, not a guarantee

Three identical-shape requests at `max_tokens: 400`, `reasoning_effort: "low"`, via an HTTP Request node:

```
item 0: finish=length  contentLen=2131  reasoningTokens=8
item 1: finish=length  contentLen=0     reasoningTokens=399   ← still empty
item 2: finish=length  contentLen=1803  reasoningTokens=27
```

One request in three still consumed its entire budget reasoning. **`reasoning_effort` makes the failure rare; it does not remove it.** Guard and retry logic is therefore mandatory, not optional. This is the single most important constraint in this design.

### 2.6 Both node types fan out per input item

Verified: a Code node emitting N items feeds `chainLlm` (and `httpRequest`) directly, which executes N times and emits N items **in input order**. No `Loop Over Items` node is required for map-style parallelism.

### 2.7 The existing OpenRouter credential is reusable by HTTP Request

`OpenRouterApi.credentials.js` declares `authenticate: { type: 'generic', properties: { headers: { Authorization: '=Bearer {{$credentials.apiKey}}' } } }`, so `httpRequest` can consume it via `authentication: "predefinedCredentialType"`, `nodeCredentialType: "openRouterApi"`. **No second copy of the API key is introduced.**

## 3. Goals and non-goals

**Goals**

1. The pipeline produces correct output for a transcript of any size, degrading in cost and latency rather than in content.
2. A truncated or empty LLM response can never be written to disk as if it were complete.
3. Every step's model is configurable from one place, with no model hard-coded into node internals.
4. One implementation of the OpenRouter call + guard + retry, shared by both workflows.

**Non-goals**

- Changing the artifact set, filenames, or the `/ingest` contract. Downstream community-brain consumers see no change.
- Changing the six canonical `extracted-signal.md` headings — the corpus depends on them.
- Re-ingesting the existing 85-session corpus. Audited 2026-09-02: the four largest `prepared-transcript.md` files (211 KB, 165 KB, 155 KB, 153 KB) all terminate with a complete `=== UNRESOLVED SPEAKERS ===` block. No truncation fingerprints. The corpus is intact.
- Migrating W1's Fathom/rendezvous front half or W2's backfill state file.

## 4. Architecture

Three components replace the current per-step `chainLlm` + `lmChatOpenRouter` pairs.

```
┌─ W1 / W2 ──────────────────────────────────────────────────┐
│  Code: Pipeline Config   (models, budgets, chunk targets)   │
│         │                                                   │
│  Code: Split <step>  ──►  Execute Workflow: OpenRouter Call │
│         ▲                          │                        │
│         └── halve chunk target ────┤ (caller-level retry)   │
│                                    ▼                        │
│  Code: Guard + Aggregate  ──►  next step / save             │
└─────────────────────────────────────────────────────────────┘

┌─ W3: OpenRouter Call (shared sub-workflow) ────────────────┐
│  Code: Normalize + Defaults                                │
│         ▼                                                  │
│  HTTP Request → openrouter.ai/api/v1/chat/completions      │
│         ▼         (predefinedCredentialType openRouterApi) │
│  Code: Classify   (finish_reason, empty, structure)        │
│         │                                                  │
│         ├─ all ok ─────────────► return items              │
│         └─ retryable ──► Code: Escalate ──► HTTP (loop)     │
└────────────────────────────────────────────────────────────┘
```

### 4.1 W3 — `OpenRouter Call` (new shared sub-workflow)

The only place in the project that talks to OpenRouter. Invoked by both workflows via `executeWorkflow` typeVersion 1.2, whose `workflowId` **must** use the resourceLocator form `{__rl: true, value, mode: "list", cachedResultName}` — the bare-string form errors with *"No information about the workflow to execute found"* (recorded in operator memory).

Execute Workflow passes **all** input items in a single sub-execution, so a map over N chunks is one sub-workflow call, not N.

**Input item contract:**

| Field | Required | Meaning |
|---|---|---|
| `stepName` | yes | For error messages and logs, e.g. `prep`, `signal.map`, `post.section.qa` |
| `model` | yes | OpenRouter model slug. Never defaulted in the component. |
| `system` | yes | System prompt |
| `user` | yes | User content (the chunk) |
| `maxTokens` | yes | Total completion budget: reasoning + content |
| `reasoningEffort` | no | `low` \| `minimal` \| `medium` \| `high`; omitted → provider default |
| `temperature` | no | Default 0.3 |
| `expect` | no | Structural validator key (§4.4) |
| `chunkIndex` | yes | Preserved on output for ordered reassembly |

**Output item contract:**

| Field | Meaning |
|---|---|
| `chunkIndex` | Echoed from input |
| `text` | Message content |
| `ok` | `true` only if non-empty, `finish_reason == "stop"`, and structural check passed |
| `finishReason` | Raw from the API |
| `usage` | `promptTokens`, `completionTokens`, `reasoningTokens`, `cost` |
| `attempts` | How many API calls this item consumed |
| `failureKind` | `null` \| `reasoning_burn` \| `content_truncated` \| `structure` \| `api_error` |

`httpRequest` fans out per item (§2.6), so the map is native — no loop node in the happy path.

### 4.2 Two-level retry

The two failure shapes have different remedies, so retry is split across two levels.

**Component-level (inside W3) — for budget failures.** Because reasoning burn is *non-deterministic* (§2.5), retrying the identical request often succeeds. Ladder, max 3 attempts per item:

| Attempt | Action |
|---|---|
| 1 | As requested |
| 2 | Retry with `reasoning_effort` forced to `low`, `maxTokens × 1.5` |
| 3 | `reasoning_effort: "minimal"`, `maxTokens × 2`, capped at the model ceiling (§4.5) |
| after | Emit item with `ok: false` and a `failureKind` |

Only items with `ok: false` are re-sent; successful items are carried forward untouched.

**Caller-level (inside W1/W2) — for genuine size failures.** If W3 returns any `ok: false` after its ladder, the calling step halves `chunkTargetTokens`, re-splits, and re-runs the whole step. Maximum 2 halvings, then **throw** — the execution goes red and no artifact is written for that step.

Step-level rather than per-chunk re-splitting is deliberate: it needs one loop-back edge instead of two, and redoing a whole GLM step costs ~$0.02. Simplicity is worth more than the wasted call.

### 4.3 Guard checks

`ok` requires all three:

1. **Non-empty** — catches reasoning burn (§2.2).
2. **`finish_reason == "stop"`** — catches conventional truncation. Now possible because HTTP Request exposes it (§2.3).
3. **Structural** — per `expect` key, catches a model that stopped cleanly but produced a malformed document.

### 4.4 Structural validators

| `expect` | Check |
|---|---|
| `prep.chunk` | Every `<!--SEGMENT` opened is closed by `-->`; body is non-trivial |
| `signal.map` | Output parses as markdown H2 sections drawn from the six canonical slugs |
| `signal.reduce` | **All six** headings present, in canonical order: `general`, `insights`, `qa`, `tools`, `links`, `decisions` |
| `post.section` | Non-empty, no markdown syntax (Skool constraint) |
| `none` | Non-empty only |

### 4.5 Model output ceilings

The escalation ladder caps `maxTokens` at the model's advertised completion limit, read from OpenRouter's `/api/v1/models` (`top_provider.max_completion_tokens`), verified 2026-09-02:

| Model | Context | Max completion |
|---|---|---|
| `z-ai/glm-5.3-flash` | 1310720 | **131072** |
| `anthropic/claude-sonnet-5` | 1000000 | **128000** |

Both are far above any budget this pipeline needs, so the ladder never saturates in practice. The component holds these as a lookup keyed by model slug, defaulting to 32768 for an unrecognised slug so that a newly configured model degrades safely rather than sending an out-of-range `max_tokens`.

## 5. Chunking strategies

Each chunked step splits along a boundary that is *semantically* meaningful for that step, not by raw byte count.

### 5.1 Prep-Prompt — map by transcript line

`transcript.txt` is exceptionally regular: all 2141 lines of the 2026-09-01 file match `^\[\d\d:\d\d:\d\d\] Speaker: `, longest line 1213 chars, **zero** non-conforming lines. Splitting on line boundaries therefore never cuts mid-utterance and needs no fuzzy boundary logic.

Accumulate lines until `chunkTargetTokens` (default **15000**) is reached, then start a new chunk. For the 62k-token 2026-09-01 transcript this yields ~5 chunks at ~10k output tokens each — roughly 3× headroom inside a 32768 budget.

Reassembly (`Code: Guard + Aggregate`), map-only, no reduce call:

1. Order by `chunkIndex`.
2. Hoist a single `=== SESSION ===` header; drop per-chunk duplicates.
3. Concatenate segment bodies in order.
4. Merge all `=== UNRESOLVED SPEAKERS ===` blocks into one deduped trailing block.

Segments are designed to be independently understandable, so no cross-chunk reconciliation is needed.

### 5.2 Extract Signal — map-reduce

**Map** over the same line-based chunks as §5.1, spoken content only. Each chunk emits the six canonical sections for its slice.

**Reduce** — one call receiving all chunk extractions **plus the complete Zoom chat log**. The chat log is deliberately excluded from the map: it uses wall-clock stamps (`2026-08-25 19:36:03`) while the transcript uses relative (`[00:00:00]`), and aligning them needs a call-start anchor that is not reliably available. Handing the whole log to the reduce step processes it exactly once, with no cross-chunk link duplication to reconcile. Chat is the dominant source of `links` and much of `tools`.

The reduce prompt carries an **explicit size budget** (default 8000 tokens ≈ 32 KB). This budget is what structurally bounds every downstream step, which is why Compress Post and Weekly Invite never need chunking regardless of call length.

### 5.3 Community Post — map by section

`extracted-signal.md` has exactly six canonical sections mapping nearly 1:1 onto the post's six:

| extracted-signal | community post |
|---|---|
| `general` | 📝 SUMMARY |
| `insights` | 💡 KEY INSIGHTS |
| `qa` | ❓ KEY Q&A |
| `tools` | 🛠️ TOOLS AND CONCEPTS MENTIONED |
| `links` | 📎 SHARED RESOURCES |
| `decisions` | 🔄 FOLLOW-UPS WORTH EXPLORING |

Split into six items, one per section, then concatenate in fixed order in a Code node.

This is not merely a size fix. Today the prompt must fight the model with `CRITICAL: You MUST output sections in EXACTLY this order` — operator memory records that specifying order in prose was insufficient and required numbered sections plus an explicit instruction. Under section-mapping, **ordering is enforced by code and that instruction stops being load-bearing.** Each section prompt also gets to be specific instead of one prompt juggling six jobs, which cuts per-call reasoning burn — the direct cause of the 09-01 failure at this step.

A section absent from the input emits no item and no output section, preserving today's "omit empty sections" behavior.

### 5.4 Compress Post, Weekly Invite — unchanged topology

Inputs are bounded by §5.2's reduce budget. They move to W3 for the guard and configurable model, but are not chunked.

## 6. Configuration

One `Code: Pipeline Config` node per workflow, placed immediately after the trigger, returning a config object read by every step via `$('Code: Pipeline Config').first().json`.

```js
return [{ json: {
  steps: {
    prep:          { model: 'z-ai/glm-5.3-flash',    maxTokens: 32768, reasoningEffort: 'low', chunkTargetTokens: 15000 },
    signalMap:     { model: 'anthropic/claude-sonnet-5', maxTokens: 16384, chunkTargetTokens: 15000 },
    signalReduce:  { model: 'anthropic/claude-sonnet-5', maxTokens: 32768, budgetTokens: 8000 },
    postSection:   { model: 'z-ai/glm-5.3-flash',    maxTokens: 16384, reasoningEffort: 'low' },
    compress:      { model: 'z-ai/glm-5.3-flash',    maxTokens: 16384, reasoningEffort: 'low' },
    invite:        { model: 'z-ai/glm-5.3-flash',    maxTokens: 16384, reasoningEffort: 'low' },
  },
  retry: { componentAttempts: 3, callerHalvings: 2 },
}}];
```

Changing any model is a one-line edit in one visible node, versioned in git. `maxTokens` values stay at or below 32768 so that opening a node in the editor cannot silently break them (§2.1); the component may escalate *above* the configured value during its retry ladder, where the UI clamp does not apply.

**W2 models:** `kimi-k2.5` is retired. W2 uses the same config shape, restricted to `claude-sonnet-5` and `glm-5.3-flash`, defaulting to Sonnet 5 for prep and signal (preserving current backfill behavior) and GLM for post.

## 7. Deployment sequence

The committed workflow JSON is **stale against live** — the repo shows `maxTokens: 8192` and `claude-sonnet-4.6` everywhere, while live W1 runs `claude-sonnet-5` for Extract Signal and `glm-5.3-flash` elsewhere, all at 32768. Implementation therefore begins by reconciling, not editing:

1. Export live W1 and W2 → repo, commit as a "reconcile live config" baseline.
2. Build W3, import, record its id.
3. Convert W1 step by step; after each step, run against `watch/2026-09-01-*` and diff artifacts.
4. Convert W2.
5. Re-run 2026-09-01 end to end to recover its missing `prepared-transcript.md`.

## 8. Validation

| # | Criterion | Method |
|---|---|---|
| 1 | 2026-09-01 produces all five artifacts, none 0-byte | Re-run; `wc -c` each |
| 2 | `prepared-transcript.md` ≈ 0.6–0.7× transcript size | Compare against 07-14's 98 KB → 65 KB ratio |
| 3 | `extracted-signal.md` has all six headings in canonical order | grep |
| 4 | `community-post.md` sections in fixed order, no markdown | grep for `#`, `**`, `- ` |
| 5 | Truncation fails loudly | Force `maxTokens: 200` on one step; execution must go **red** |
| 6 | Retry ladder recovers reasoning burn | Force a burn-prone config; confirm `attempts > 1` and `ok: true` |
| 7 | A normal-size call is unchanged | Re-run 2026-08-25; artifacts materially equivalent to committed ones |
| 8 | `/ingest` still succeeds | Confirm session appears via `/sessions` |

Criterion 5 is the one that matters most: it is the exact failure that went undetected on 2026-09-01.

## 9. Open items

- **`watch/2026-09-01-zoom-chat.txt` contains chat timestamped `2026-08-25`.** Either Zoom labels by a different date or last week's file was copied. 09-01's `links` section may derive from the wrong call. Operator to confirm before the re-run in §7.5.
- **Cost/latency baseline.** ~5 prep chunks + ~5 signal map + 1 reduce + 6 post sections + compress + invite ≈ 19 calls versus 5 today. Dominated by Sonnet 5 on signal; GLM steps are ~$0.02. Measure on the first real run.
- **Cross-workflow prompt drift.** W1 and W2 hold near-duplicate prep and signal prompts. This design shares the *transport*, not the prompts. Consolidating prompt text is deliberately out of scope; revisit if they diverge further.

## Appendix A — Probe methodology

All §2 findings were produced by temporary probe workflows imported via `docker exec n8n n8n import:workflow`, executed with `N8N_RUNNERS_BROKER_PORT=5680 N8N_RUNNERS_AUTH_TOKEN=foo` (operator memory: avoids a port-5679 collision with the live container), and deleted afterward. The decrypted credential file used for direct API probes was removed from the container. Post-probe state verified: 6 workflows, `git status` clean.
