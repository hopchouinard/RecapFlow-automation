# CLAUDE.md — community-brain/

Guidance for Claude Code when working inside the `community-brain/` subfolder.

The root `CLAUDE.md` covers n8n + Docker Compose orchestration. This file covers the Python package that runs INSIDE the `retrieval-server` container — a separate concern with its own architecture, conventions, and footguns.

## What this is

Python package implementing the Community Brain ingestion pipeline and retrieval server:

- **Ingests** coaching-call artifacts (`prepared-transcript.md`, `extracted-signal.md`, `community-post.md`) produced by n8n workflows
- **Parses, chunks, extracts LLM metadata, embeds, and writes** to LanceDB per the v1.0 schema (37 fields)
- **Serves** `/query`, `/sessions`, `/ingest`, `/reindex` via FastAPI on port 8999

Distinct from the root repo's n8n workflows, which will call this service in Plan B. The package is deployed as a Docker container via the root-level `docker-compose.yml` (`retrieval-server` service).

**Authoritative docs:**
- Design spec: `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md`
- Plan A (what's built): `docs/superpowers/plans/2026-04-18-community-brain-ingestion-plan-a.md`
- Trust contract (for downstream LLMs): `docs/inference-guidelines.md`
- Migration log: `docs/migrations/CHANGELOG.md`
- **Deployment runbook** (SSH + Docker Compose on the VM): `community-brain/docs/DEPLOYMENT.md` — follow this end-to-end when deploying, updating, or operating the retrieval-server container. It encodes the permission model (🟢 auto / 🟡 confirm / 🔴 gated) that Claude must respect when acting as operator.

## Package layout

```
community-brain/
├── src/community_brain/
│   ├── ingestion/          # The pipeline: parser, chunker, extractors, embedding, orchestrator
│   │   ├── _io.py          # Atomic YAML writes with per-path locks
│   │   ├── _llm_parse.py   # Shared code-fence stripping for LLM JSON
│   │   ├── config_loader.py
│   │   ├── registries.py   # Speaker + entity registries
│   │   ├── parser.py       # Artifact parsers
│   │   ├── schema.py       # v1.0 LanceDB schema (37-field Chunk dataclass)
│   │   ├── chunker.py      # Three strategies per content type
│   │   ├── extractor.py    # Stage C per-chunk LLM
│   │   ├── session_extractor.py  # Stage B session-level LLM
│   │   ├── embedding.py    # Ollama nomic wrapper
│   │   └── pipeline.py     # Orchestrator (ingest_session)
│   ├── query/
│   │   ├── retrieval_server.py  # FastAPI app
│   │   ├── query_local.py       # search helpers (hybrid vector + BM25)
│   │   ├── cue_rules.py         # v2 cue-boost rules + apply_cue_boosts
│   │   └── fts_lifecycle.py     # ensure_fts_index / optimize_fts_index
│   └── openwebui/
│       └── community_brain_filter.py  # Open WebUI filter (ships as single file)
├── config/                 # YAMLs + extraction prompts (mounted into container)
├── lancedb/                # Vector store (persistent volume)
└── tests/                  # pytest; 296+ tests
```

## Non-negotiables (architectural discipline)

### Trust model
The `/query` response is structurally partitioned:

```
chunks[].ground_truth        ← authoritative; quotes must resolve here
chunks[].derived_metadata    ← LLM-interpreted; probabilistic; re-derivable
chunks[].provenance          ← tracks what generated it (model, prompt_version, status)
```

`docs/inference-guidelines.md` enforces the contract downstream. The filter at `src/community_brain/openwebui/community_brain_filter.py` embeds the guidelines text as a module-level constant — do **not** reintroduce filesystem loading; the filter deploys as a single Python file uploaded to Open WebUI with no `docs/` sibling. The `test_inference_guidelines_match_docs_file` test enforces parity; when editing the docs file, update the constant in the same commit.

### Schema v1.0 = 37 fields
- Additive changes are free (new nullable field, default None).
- Semantic changes require a migration entry in `docs/migrations/CHANGELOG.md` AND a `schema_version` bump.
- `test_chunk_dataclass_matches_lancedb_schema_fields` locks `Chunk` ↔ `lancedb_table_schema()` parity. Keep both in sync.

### Idempotency anchoring
- `extraction_prompt_version` is the version anchor (file stem of `config/extraction-prompts/chunk-extraction-vN.md`).
- Model changes alone don't bump it. Switching `COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL` mid-corpus requires `force_reextract: true` on `/ingest` to re-run existing sessions.
- `force_reextract: true` also triggers **full-session rewrite** — all existing rows for the session are deleted before new chunks are added. Use it explicitly when cleaning up orphan rows from prompts that produced more chunks than the current version does.

### Registries are single-writer (v1)
- `threading.Lock` per registry path + merge-on-flush for the `pending:` list handles concurrent same-process flushes.
- Multi-worker uvicorn (`--workers N`) is **not supported** — locks are in-process only.
- v2 would need file-level locks (flock) or a dedicated writer process.

### Failed-extraction chunks are intentionally unsearchable
- Chunks with `extraction_status="failed"` persist with empty `embedding: []`.
- They're excluded from vector search by design — operators use `/reindex` (v2) or `force_reextract` to retry.
- Do **not** "fix" this by backfilling embeddings for failed chunks.

### Security / injection
- `session_id` and `chunk_id` must match `_SAFE_ID_RE = ^[0-9A-Za-z_\-:.]+$`. Validated at `ingest_session` entry; trips a 400 at the HTTP boundary.
- Filter values (entities, speakers, keywords) in `build_filter_expression` go through `sql_quote` — SQL-standard `'` → `''` escaping. Simple string scalars only; anything structured would need parameterized queries.
- Artifact paths constrained to `COMMUNITY_BRAIN_ARTIFACT_ROOT` when that env is set (required in Docker deployment; optional on VM-direct runs).

## Env-var precedence chain (Docker deployment)

```
Dockerfile ENV  (lowest — baseline defaults)
  ↓ overridden by
env_file: community-brain/config/.env  (operator overrides; loaded when file exists)
  ↓ overridden by
docker-compose environment:  (currently empty on retrieval-server; reserved)
  ↓ overridden by
Shell env at `docker compose up`  (highest)
```

**Empty-string env vars clobber Dockerfile defaults.** This is why `community-brain/config/.env.example` has all override entries commented out (`#`-prefixed). Operators uncomment-and-set only what they want to override. Do not "help" by uncommenting empty-value lines.

Code defends against empty strings with `os.environ.get("X") or fallback`, **never** `os.environ.get("X", fallback)` — the latter only falls through when the key is MISSING, not when it's empty.

## Config discipline

| File | Purpose | Writable at runtime? |
|---|---|---|
| `config/speaker-aliases.yaml` | Canonical speaker registry | Yes — pipeline appends to `pending:` queue |
| `config/entity-registry.yaml` | Canonical entity registry | Yes — same `pending:` pattern |
| `config/chunking.yaml` | Token thresholds + retry settings | Read-only; container restart to pick up changes |
| `config/extraction-config.yaml` | Active prompt versions + models | Read on each /ingest call (cheap) |
| `config/extraction-prompts/*.md` | Versioned prompts | Read on each /ingest call |
| `config/.env` | Operator env overrides | Loaded at container start via env_file |

`community-brain/config/.env` is **distinct** from the repo-root `.env` (which holds n8n DB credentials per the root CLAUDE.md). Same rule: do not commit it if it contains real secrets — `.gitignore` already excludes both.

Volume-mounted at `/app/config` (read-write). Edits on the host take effect on the next `/ingest` call for YAMLs and prompt files; container restart required for Dockerfile-ENV-level changes.

## Testing conventions

### Run tests

First-time venv setup (from `community-brain/`):

```bash
python3.11 -m venv .venv
./.venv/bin/pip install -e ".[dev]"
```

Then run tests:

```bash
# From community-brain/
./.venv/bin/pytest tests/ -q

# Or activate first
source .venv/bin/activate
pytest tests/ -q
```

**Note for worktree users:** the `-e` editable install binds the venv to the directory it was installed from. If you `pip install -e .` from a git worktree and later remove the worktree, the venv breaks. Re-run `pip install -e ".[dev]"` from the current working tree to relink.

### Mock boundaries (things that have bitten us)

- **LLM calls**: mock at `community_brain.ingestion.extractor._call_llm` and `community_brain.ingestion.session_extractor._call_llm`. The `_call_llm` indirection in both modules exists precisely for this — don't bypass it by patching `call_llm` in `community_brain.llm` directly.
- **Ollama embedding**: mock `community_brain.ingestion.embedding.ollama.embed` (ingest side) and `community_brain.query.query_local.ollama.embed` (query side). Both use the shared `_active_embed_model()` resolver; an env override affects both consistently.
- **LanceDB**: don't mock. Use `tmp_path` fixtures with real storage — it's fast (sub-second) and catches real schema/ID bugs that mocks hide.
- **Env vars**: always use `monkeypatch.setenv` / `monkeypatch.delenv`. Raw `os.environ` edits leak between tests.
- **API key auth**: `monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)` for most tests. `_verify_api_key` reads the env var at call time (not import time), so reload tricks aren't needed.

### Pyright "import could not be resolved" warnings

The venv at `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain/.venv` is shared between the main repo and the worktree. When Pyright runs against the worktree from the main repo's IDE context, it can't resolve `community_brain.ingestion.*` imports. **These are environmental noise, not real errors.** Verify with the actual test run — if pytest finds and passes the tests, the imports resolve fine at runtime.

Other conventional Pyright warnings to ignore:
- `_key`, `_a`, `_kw`, `_retry_cfg`, `_source` "not accessed" — underscore prefix is intentional (unused dependency-injected parameters, or destructured-but-unused tuple elements)
- `mocked_pipeline_env` "not accessed" — pytest autouse fixture, Pyright doesn't understand the mechanism

## Deployment

### Docker (VM production)
```bash
# From repo root (one level up)
docker compose up -d retrieval-server
docker compose logs -f retrieval-server
```

Port published on `127.0.0.1:8999` only (not `0.0.0.0`). API reachable from the VM host but not from LAN. Cross-machine use requires an explicit reverse-proxy hop.

### Local dev (Mac Mini / laptop direct)
```bash
pip install -e .
uvicorn community_brain.query.retrieval_server:app --port 8999
# Optional: .env setup at community-brain/config/.env
```

Local dev reads `config/.env` via `python-dotenv`; Docker reads it via compose `env_file:`. Behavior is equivalent.

## Known v2 backlog (don't rediscover)

- **`RetryConfig`** loaded from `chunking.yaml` but not wired into Stage B/C LLM calls. `community_brain.llm.call_llm` has its own 3-retry default.
- **`/reindex` mutations** (`re-extract`, `re-embed`, `delete`): v1 returns match counts only. Callers use `force_reextract: true` on `/ingest` for per-session re-extraction.
- **Corpus-derived markers** (`recurrent` etc.): schema fields exist (`corpus_derived_markers`, `corpus_markers_computed_at`) but no populating pass. Needs a "corpus lint" job.
- **`speakers_mentioned` population**: always `None` in v1. Needs a Stage C prompt update that emits a distinct `mentioned_people` field.
- **Multi-writer registry support**: current in-process `threading.Lock` doesn't survive multi-worker uvicorn.
- **`/sessions` pagination**: hard cap at `limit(100_000)`, silently truncates past that.
- **Deep `/health`**: currently returns `{"status":"ok"}` unconditionally. No checks for config presence, LanceDB readability, Ollama reachability.
- **Read/write API key split**: single `RETRIEVAL_API_KEY` gates all endpoints including mutating ones.

## Trade-offs we've deliberately kept

- **`_commit_chunks` is delete-then-add, not truly atomic.** `CommitError` surfaces torn state in the HTTP 500 response; recovery is `force_reextract: true`.
- **Filter values are interpolated (sql_quote-escaped), not parameterized.** Safe for simple string scalars; would need real parameterization for structured or untrusted filter inputs.
- **The Open WebUI filter embeds inference guidelines as a module constant**, not loaded from disk at runtime. Deployment-safe; requires manual parity sync with `docs/inference-guidelines.md` (test enforces).
- **Empty-string env vars from env_file clobber Dockerfile ENV.** Worked around via commented `.env.example` entries + defensive `... or None` at read sites.
- **`/query` ranking is hybrid (vector + BM25 RRF, k=60) with cue-driven metadata boosting.** Replaced pure-vector ranking in v2; see `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`. Pure-vector ranking is no longer available as an opt-in mode — vector-only path is reserved for internal graceful-degradation when the FTS index is unavailable. The cue-boost layer composes additive RRF-score deltas based on lexical cues in the question matching candidate-chunk metadata flags (see `community_brain.query.cue_rules`).

## Interaction with n8n (root workflows)

The retrieval server is a CONSUMER of n8n's outputs, not a replacement:

1. n8n Merged Call Summarizer produces `output/<YYYY-MM-DD>/*.md` files (root workflow)
2. After producing them, n8n will POST to `http://retrieval-server:8999/ingest` (planned in Plan B — not yet wired)
3. Retrieval server reads the artifact files (via `./output:/data/output:ro` volume mount) and ingests them

The `./output` directory is shared between the two containers. n8n writes, retrieval-server reads. `COMMUNITY_BRAIN_ARTIFACT_ROOT=/data/output` in the container constrains `/ingest` to only accept paths under this mount.

## Commit style

Match the existing pattern visible in `git log --oneline`:

```
feat(ingestion): ...        # new capability in the ingestion pipeline
feat(retrieval): ...        # new HTTP endpoint or /query feature
fix(ingestion|retrieval|openwebui|docker): ...
refactor(ingestion): ...
test(ingestion|retrieval|openwebui): ...
config(community-brain): ...
docs(ingestion|migrations|plans|specs): ...
infra(docker): ...
chore(ingestion): ...
```

When Claude Code creates commits, include the footer:

```
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

This matches the convention used throughout the existing `git log` and the repo's auto-commit template.
