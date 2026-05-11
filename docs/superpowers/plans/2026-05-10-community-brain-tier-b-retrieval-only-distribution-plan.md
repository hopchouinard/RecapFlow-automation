# Community Brain — Tier B (Retrieval-Only) Distribution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship Tier B — a distributable Docker stack that lets community participants run the Community Brain retrieval experience on their own machines, against a pre-built LanceDB corpus, with zero operator-side hosting.

**Architecture:** Two-repo split. Operator repo (`RecapFlow-automation`) gains distribution-mode capability in the retrieval-server, plus release tooling that publishes Docker images to ghcr.io and a corpus tarball to GitHub Releases on a new sibling public repo (`community-brain-distribution`). Recipients clone the distribution repo, fetch the corpus blob, run `docker compose up -d`, and get Open WebUI + filter + custom model with pluggable inference backend (Ollama for local, any OpenAI-compatible endpoint for cloud).

**Tech Stack:** Python 3.11, FastAPI, LanceDB, Docker Compose v2, Ollama, Open WebUI, GitHub Actions, bash, pytest.

**Spec:** [`docs/superpowers/specs/2026-05-10-community-brain-tier-b-retrieval-only-distribution-design.md`](../specs/2026-05-10-community-brain-tier-b-retrieval-only-distribution-design.md)

---

## Plan Structure

Four milestones, ~24 tasks total. Each milestone ends with a checkpoint that produces working/testable software:

| Milestone | Outcome | Where it lives |
|---|---|---|
| 1. Server-side foundations | Distribution-mode-capable retrieval-server image | `community-brain/` Python package |
| 2. Operator release pipeline | `scripts/release-corpus.sh` + GitHub Actions workflows that build images + open distribution PRs | Operator repo |
| 3. Distribution repo creation | New public `community-brain-distribution` repo with full install path + CI smoke test passing | New external repo |
| 4. v1.0.0 release | First public release tagged, corpus published, recipients can install | Both repos |

## File map

**Modified files:**
- `community-brain/pyproject.toml` — version bump + canonical version source
- `community-brain/src/community_brain/query/retrieval_server.py` — distribution-mode route gating, extended `/health`, lifespan branch
- `community-brain/src/community_brain/query/corpus_verify.py` — new `verify_corpus_v3_state_readonly` function

**New files (server-side):**
- `community-brain/src/community_brain/cli/__init__.py` (if not present)
- `community-brain/src/community_brain/cli/verify_corpus_clean_v3.py`
- `community-brain/src/community_brain/cli/write_corpus_manifest.py`
- `community-brain/tests/test_distribution_mode_routes.py`
- `community-brain/tests/test_health_endpoint_extended.py`
- `community-brain/tests/test_corpus_verify_readonly.py`
- `community-brain/tests/test_cli_verify_corpus_clean_v3.py`
- `community-brain/tests/test_cli_write_corpus_manifest.py`

**New files (operator repo):**
- `scripts/release-corpus.sh`
- `scripts/release-corpus-test.sh` (small sanity test)
- `.github/workflows/build-retrieval-image.yml`
- `.github/workflows/sync-curated-files.yml`

**New repo `community-brain-distribution` files:**
- `README.md`
- `INSTALL.md`
- `verify-install.sh`
- `docker-compose.yml`
- `.env.example`
- `community_brain_filter.py` (auto-synced)
- `inference-guidelines.md` (auto-synced)
- `download-corpus.sh`
- `docs/tour.md`
- `docs/troubleshooting.md`
- `docs/screenshots/` (operator-captured)
- `tests/fixtures/corpus/` (pre-built tiny LanceDB)
- `tests/fixtures/mock-ollama/` (FastAPI shim)
- `.github/workflows/verify-on-pr.yml`
- `.gitignore`

---

## Milestone 1: Server-side foundations

Outcome: a `community-brain` Python package that builds a Docker image which, when run with `COMMUNITY_BRAIN_DISTRIBUTION_MODE=true`, exposes only the read endpoints and supports an extended `/health` endpoint. Full pytest passes.

### Task 1: Reconcile version source via `importlib.metadata`

**Files:**
- Modify: `community-brain/pyproject.toml` (line 3)
- Modify: `community-brain/src/community_brain/query/retrieval_server.py` (line 141)
- Create: `community-brain/tests/test_version_source.py`

- [ ] **Step 1: Write failing test for version source consistency**

Create `community-brain/tests/test_version_source.py`:

```python
"""Version source must be canonical: pyproject.toml → importlib.metadata."""
from importlib.metadata import version

from community_brain.query.retrieval_server import app


def test_fastapi_app_version_matches_package_metadata():
    """FastAPI app.version must read from package metadata, not a hardcoded string."""
    expected = version("community-brain")
    assert app.version == expected, (
        f"app.version={app.version!r} but package metadata says {expected!r}. "
        f"Read from importlib.metadata.version('community-brain') instead of "
        f"hardcoding."
    )
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd community-brain
./.venv/bin/pytest tests/test_version_source.py -v
```

Expected: FAIL — `app.version='0.2.0'` does not equal `version('community-brain')` which returns `'0.1.0'` (from pyproject.toml).

- [ ] **Step 3: Bump pyproject.toml version**

Edit `community-brain/pyproject.toml` line 3 (the `version = "0.1.0"` line) to:

```toml
version = "0.3.0"
```

Rationale: distribution mode is a meaningful capability addition. Previous FastAPI hardcode was 0.2.0; bump past it cleanly.

- [ ] **Step 4: Make FastAPI read version from package metadata**

In `community-brain/src/community_brain/query/retrieval_server.py`, find the `app = FastAPI(...)` block around line 138-143 and update:

```python
from importlib.metadata import version as _package_version

app = FastAPI(
    title="Community Brain Retrieval API",
    description="Search coaching call transcripts by semantic similarity.",
    version=_package_version("community-brain"),
    lifespan=lifespan,
)
```

- [ ] **Step 5: Reinstall editable package so metadata picks up the version bump**

```bash
cd community-brain
./.venv/bin/pip install -e . --quiet
```

- [ ] **Step 6: Run test to verify it passes**

```bash
./.venv/bin/pytest tests/test_version_source.py -v
```

Expected: PASS — both should report `0.3.0`.

- [ ] **Step 7: Run the full test suite to confirm no regressions**

```bash
./.venv/bin/pytest tests/ -q
```

Expected: all existing tests pass (302+ tests per CLAUDE.md).

- [ ] **Step 8: Commit**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
git add community-brain/pyproject.toml \
        community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_version_source.py
git commit -m "$(cat <<'EOF'
refactor(retrieval): unify version source via importlib.metadata

Bumps community-brain to 0.3.0 (Tier B distribution-mode capability)
and removes the hardcoded FastAPI version="0.2.0" string in favor of
reading from importlib.metadata.version("community-brain"), which is
sourced from pyproject.toml. /health.server_version (added in next
task) reads from the same source.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Extended `/health` endpoint with metadata

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py` (the `@app.get("/health")` handler around line 285)
- Create: `community-brain/tests/test_health_endpoint_extended.py`

- [ ] **Step 1: Read the existing /health handler to understand current shape**

```bash
sed -n '283,295p' community-brain/src/community_brain/query/retrieval_server.py
```

Expected: current handler returns something like `{"status": "ok"}`.

- [ ] **Step 2: Write failing tests for extended /health**

Create `community-brain/tests/test_health_endpoint_extended.py`:

```python
"""/health returns server + corpus metadata per Tier B spec §4.2."""
from importlib.metadata import version
from fastapi.testclient import TestClient

from community_brain.ingestion.schema import SCHEMA_VERSION
from community_brain.query.retrieval_server import app


def test_health_returns_status_ok():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_health_returns_server_version():
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["server_version"] == version("community-brain")


def test_health_returns_schema_version_bare_numeric():
    """Schema version is bare numeric (e.g. '1.1'), no 'v' prefix.
    Matches community_brain.ingestion.schema.SCHEMA_VERSION format."""
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["schema_version"] == SCHEMA_VERSION
    assert not r.json()["schema_version"].startswith("v")


def test_health_returns_embedding_model_default(monkeypatch):
    """When COMMUNITY_BRAIN_EMBED_MODEL is unset, /health returns the default."""
    monkeypatch.delenv("COMMUNITY_BRAIN_EMBED_MODEL", raising=False)
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["embedding_model"] == "nomic-embed-text"


def test_health_returns_embedding_model_override(monkeypatch):
    """COMMUNITY_BRAIN_EMBED_MODEL override surfaces in /health."""
    monkeypatch.setenv("COMMUNITY_BRAIN_EMBED_MODEL", "custom-embed-model")
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["embedding_model"] == "custom-embed-model"


def test_health_distribution_mode_false_by_default(monkeypatch):
    monkeypatch.delenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", raising=False)
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["distribution_mode"] is False


def test_health_distribution_mode_true_when_env_set(monkeypatch):
    monkeypatch.setenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", "true")
    client = TestClient(app)
    r = client.get("/health")
    assert r.json()["distribution_mode"] is True
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd community-brain
./.venv/bin/pytest tests/test_health_endpoint_extended.py -v
```

Expected: tests 2-7 FAIL because the existing handler returns only `{"status": "ok"}`. Test 1 may pass.

- [ ] **Step 4: Update /health handler in retrieval_server.py**

In `community-brain/src/community_brain/query/retrieval_server.py`, find the `@app.get("/health")` handler and replace its body:

```python
@app.get("/health")
def health():
    """Health probe + version metadata.

    Returns server identity (version, schema version, embedding model,
    distribution mode flag). Used by verify-install.sh in Tier B
    distribution to cross-check the running server against the
    corpus-manifest.json shipped with the corpus blob.
    """
    from community_brain.ingestion.embedding import _active_embed_model
    from community_brain.ingestion.schema import SCHEMA_VERSION

    return {
        "status": "ok",
        "server_version": _package_version("community-brain"),
        "schema_version": SCHEMA_VERSION,
        "embedding_model": _active_embed_model(),
        "distribution_mode": (
            os.environ.get("COMMUNITY_BRAIN_DISTRIBUTION_MODE", "").lower() == "true"
        ),
    }
```

If `os` is not yet imported in `retrieval_server.py`, add `import os` at the top.

- [ ] **Step 5: Run tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_health_endpoint_extended.py -v
```

Expected: all 7 tests PASS.

- [ ] **Step 6: Run full suite for regressions**

```bash
./.venv/bin/pytest tests/ -q
```

Expected: all existing tests still pass.

- [ ] **Step 7: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_health_endpoint_extended.py
git commit -m "$(cat <<'EOF'
feat(retrieval): extend /health with version + corpus metadata

/health now returns server_version (from importlib.metadata),
schema_version (from schema.SCHEMA_VERSION, bare numeric like "1.1"),
embedding_model (from _active_embed_model() — respects
COMMUNITY_BRAIN_EMBED_MODEL override), and distribution_mode
(reads COMMUNITY_BRAIN_DISTRIBUTION_MODE env).

Used by Tier B verify-install.sh to cross-check the running server
against corpus-manifest.json before declaring an install green.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: `verify_corpus_v3_state_readonly` — pure read-only verification

**Files:**
- Modify: `community-brain/src/community_brain/query/corpus_verify.py`
- Create: `community-brain/tests/test_corpus_verify_readonly.py`

- [ ] **Step 1: Read existing corpus_verify.py to understand the API**

```bash
cat community-brain/src/community_brain/query/corpus_verify.py
```

Note: `verify_corpus_v3_state(table)` calls `ensure_fts_index(table, column="bm25_text")` which can mutate. We want a sibling function that does the structural check + asserts FTS index presence WITHOUT trying to create it.

- [ ] **Step 2: Write failing tests for the readonly variant**

Create `community-brain/tests/test_corpus_verify_readonly.py`:

```python
"""verify_corpus_v3_state_readonly: structural check + index-presence assert,
no mutation. Per Tier B spec §5.6."""
import pytest
import lancedb
import pyarrow as pa

from community_brain.query.corpus_verify import (
    CorpusInvalidError,
    verify_corpus_v3_state_readonly,
)


def _make_table(tmp_path, schema_fields, indices=None):
    """Build a test LanceDB table at tmp_path with given fields and indices."""
    db = lancedb.connect(str(tmp_path))
    schema = pa.schema(schema_fields)
    # Empty table is fine for these tests
    table = db.create_table("chunks", schema=schema, mode="overwrite")
    if indices:
        for col, idx_type in indices:
            table.create_fts_index(col, replace=True) if idx_type == "fts" else None
    return table


def test_readonly_passes_on_clean_v3_table(tmp_path):
    """A table with bm25_text column AND an FTS index on it passes."""
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
        # ... minimal v3 schema fields not enumerated here; the
        # readonly check only inspects bm25_text presence and FTS index.
    ]
    table = _make_table(tmp_path, schema, indices=[("bm25_text", "fts")])
    # Should not raise
    verify_corpus_v3_state_readonly(table)


def test_readonly_raises_when_bm25_text_column_missing(tmp_path):
    """No bm25_text column → CorpusInvalidError (pre-v1.1 corpus)."""
    schema = [
        ("session_id", pa.string()),
        ("full_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)
    with pytest.raises(CorpusInvalidError, match="bm25_text"):
        verify_corpus_v3_state_readonly(table)


def test_readonly_raises_when_fts_index_missing(tmp_path):
    """bm25_text column present but no FTS index → CorpusInvalidError.
    Critical: the function must NOT try to create the index."""
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema)  # no indices argument

    with pytest.raises(CorpusInvalidError, match="FTS index"):
        verify_corpus_v3_state_readonly(table)


def test_readonly_does_not_call_ensure_fts_index(tmp_path, monkeypatch):
    """Spy on ensure_fts_index — readonly variant must not invoke it."""
    schema = [
        ("session_id", pa.string()),
        ("bm25_text", pa.string()),
    ]
    table = _make_table(tmp_path, schema, indices=[("bm25_text", "fts")])

    calls = []
    import community_brain.query.corpus_verify as cv
    monkeypatch.setattr(
        cv, "ensure_fts_index",
        lambda *args, **kwargs: calls.append((args, kwargs))
    )
    verify_corpus_v3_state_readonly(table)
    assert calls == [], (
        f"verify_corpus_v3_state_readonly must NOT call ensure_fts_index "
        f"(would mutate). Got calls: {calls}"
    )
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd community-brain
./.venv/bin/pytest tests/test_corpus_verify_readonly.py -v
```

Expected: ImportError or all FAIL — `verify_corpus_v3_state_readonly` does not exist yet.

- [ ] **Step 4: Implement the readonly function**

Edit `community-brain/src/community_brain/query/corpus_verify.py`. After the existing `verify_corpus_v3_state` function, add:

```python
def verify_corpus_v3_state_readonly(table) -> None:
    """Read-only variant of verify_corpus_v3_state for distribution mode.

    Performs the same structural checks (bm25_text column present, FTS index
    on bm25_text exists) but does NOT attempt to create the index if it's
    missing. Used in distribution-mode startup against an RO-mounted corpus.

    Raises:
        CorpusInvalidError: if bm25_text column missing OR FTS index absent.
            The shipped corpus is malformed in this case; recipient should
            re-fetch via download-corpus.sh or report to operator.
    """
    schema_names = set(table.schema.names)
    if "bm25_text" not in schema_names:
        raise CorpusInvalidError(
            "chunks table is pre-v1.1 (no bm25_text column). v3 server "
            "cannot serve this corpus. The shipped corpus is malformed; "
            "re-fetch via ./download-corpus.sh, or report to operator."
        )

    # Inspect indices without mutating. LanceDB's list_indices() returns
    # the index metadata; we look for one whose column list includes
    # bm25_text and whose type is FTS.
    try:
        indices = table.list_indices()
    except Exception as exc:
        raise CorpusInvalidError(
            f"chunks table FTS index state cannot be inspected: {exc}. "
            f"The shipped corpus may be corrupted; re-fetch via "
            f"./download-corpus.sh."
        ) from exc

    has_bm25_fts = any(
        getattr(idx, "index_type", None) in ("FTS", "INVERTED")
        and "bm25_text" in (getattr(idx, "columns", []) or [])
        for idx in indices
    )
    if not has_bm25_fts:
        raise CorpusInvalidError(
            "chunks table has bm25_text column but no FTS index on it. "
            "The shipped corpus is malformed (release pipeline failed to "
            "build the FTS index before tarballing). Re-fetch via "
            "./download-corpus.sh, or report to operator."
        )
```

- [ ] **Step 5: Verify LanceDB's `list_indices()` API matches assumption**

Run a quick sanity check:

```bash
./.venv/bin/python -c "
import lancedb
import pyarrow as pa
import tempfile, os
with tempfile.TemporaryDirectory() as d:
    db = lancedb.connect(d)
    t = db.create_table('c', schema=pa.schema([('bm25_text', pa.string())]), mode='overwrite')
    # Add a row so we can build an index
    t.add([{'bm25_text': 'hello world'}])
    t.create_fts_index('bm25_text', replace=True)
    for idx in t.list_indices():
        print(repr(idx), dir(idx))
"
```

Expected: prints an index object. Confirm it has `index_type` and `columns` attributes (or equivalents). If the API is different (e.g. attribute named differently in this lancedb version), adjust the implementation in Step 4 to match.

- [ ] **Step 6: Run tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_corpus_verify_readonly.py -v
```

Expected: all 4 tests PASS. If the spy test fails because the function ends up importing `ensure_fts_index` differently, adjust the `monkeypatch.setattr` target.

- [ ] **Step 7: Run full suite for regressions**

```bash
./.venv/bin/pytest tests/ -q
```

Expected: all existing tests still pass.

- [ ] **Step 8: Commit**

```bash
git add community-brain/src/community_brain/query/corpus_verify.py \
        community-brain/tests/test_corpus_verify_readonly.py
git commit -m "$(cat <<'EOF'
feat(retrieval): add verify_corpus_v3_state_readonly for distribution mode

Sibling of verify_corpus_v3_state that performs the same structural
checks (bm25_text column + FTS index presence) but never attempts to
create the index. Used by Tier B distribution-mode startup against an
RO-mounted corpus, where any write attempt would fail.

If the FTS index is absent, raises CorpusInvalidError with a clear
"re-fetch corpus" message instead of trying to repair. Repair is the
release pipeline's job, not the recipient's runtime.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Distribution-mode route gating + lifespan branch

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Create: `community-brain/tests/test_distribution_mode_routes.py`

- [ ] **Step 1: Write failing tests for route absence in distribution mode**

Create `community-brain/tests/test_distribution_mode_routes.py`:

```python
"""Distribution-mode route gating per Tier B spec §2.3.

When COMMUNITY_BRAIN_DISTRIBUTION_MODE=true, /ingest and /reindex must
be absent from the registered routes. All five read endpoints must be
present in both modes.
"""
import importlib
import sys

import pytest
from fastapi.testclient import TestClient


# Routes that MUST exist in distribution mode (read-only API surface)
DISTRIBUTION_MODE_ROUTES = {
    ("GET", "/health"),
    ("POST", "/query"),
    ("GET", "/sessions"),
    ("GET", "/sessions/{session_id}"),
    ("GET", "/speaker-aliases-block"),
}

# Routes that MUST be absent in distribution mode (write endpoints)
WRITE_ROUTES = {
    ("POST", "/ingest"),
    ("POST", "/reindex"),
}


def _reload_app(monkeypatch, distribution_mode: bool):
    """Re-import retrieval_server with the env var toggled.

    Route registration happens at import time, so toggling the env at
    test setup time isn't enough — we have to force a fresh import.
    """
    if distribution_mode:
        monkeypatch.setenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", "true")
    else:
        monkeypatch.delenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", raising=False)
    if "community_brain.query.retrieval_server" in sys.modules:
        del sys.modules["community_brain.query.retrieval_server"]
    module = importlib.import_module("community_brain.query.retrieval_server")
    return module.app


def _route_set(app) -> set:
    """Return the set of (method, path) tuples registered on the app."""
    out = set()
    for route in app.routes:
        methods = getattr(route, "methods", None)
        path = getattr(route, "path", None)
        if methods and path:
            for m in methods:
                if m in ("GET", "POST", "PUT", "DELETE", "PATCH"):
                    out.add((m, path))
    return out


def test_distribution_mode_excludes_write_routes(monkeypatch):
    app = _reload_app(monkeypatch, distribution_mode=True)
    registered = _route_set(app)
    leaked = WRITE_ROUTES & registered
    assert not leaked, (
        f"Distribution mode must not register write routes. Leaked: {leaked}"
    )


def test_distribution_mode_includes_all_read_routes(monkeypatch):
    app = _reload_app(monkeypatch, distribution_mode=True)
    registered = _route_set(app)
    missing = DISTRIBUTION_MODE_ROUTES - registered
    assert not missing, (
        f"Distribution mode is missing required read routes: {missing}"
    )


def test_operator_mode_includes_write_routes(monkeypatch):
    """When COMMUNITY_BRAIN_DISTRIBUTION_MODE is unset, all routes register."""
    app = _reload_app(monkeypatch, distribution_mode=False)
    registered = _route_set(app)
    missing = WRITE_ROUTES - registered
    assert not missing, (
        f"Operator mode must include write routes. Missing: {missing}"
    )


def test_distribution_mode_ingest_returns_404_via_client(monkeypatch):
    """Behavioural confirmation: /ingest 404s, not 401."""
    app = _reload_app(monkeypatch, distribution_mode=True)
    client = TestClient(app)
    r = client.post("/ingest", json={"session_id": "test", "artifacts": {}})
    assert r.status_code == 404


def test_distribution_mode_reindex_returns_404_via_client(monkeypatch):
    """Behavioural confirmation: /reindex 404s."""
    app = _reload_app(monkeypatch, distribution_mode=True)
    client = TestClient(app)
    r = client.post("/reindex", json={})
    assert r.status_code == 404
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd community-brain
./.venv/bin/pytest tests/test_distribution_mode_routes.py -v
```

Expected: tests for distribution mode FAIL because `/ingest` and `/reindex` are always registered today. Operator-mode test should pass.

- [ ] **Step 3: Add the distribution-mode env check at module top**

In `community-brain/src/community_brain/query/retrieval_server.py`, near the top (after imports, before route definitions), add:

```python
DISTRIBUTION_MODE = (
    os.environ.get("COMMUNITY_BRAIN_DISTRIBUTION_MODE", "").lower() == "true"
)
```

- [ ] **Step 4: Wrap /ingest and /reindex registration in the env check**

Find the `@app.post("/ingest", ...)` decorator (around line 399) and the `@app.post("/reindex", ...)` decorator (around line 642). Convert each from decorator syntax to conditional registration. The cleanest pattern is to use a `register_if(condition)` wrapper or convert to imperative registration:

Replace `@app.post("/ingest", response_model=IngestHTTPResponse)` and its function definition with:

```python
def _ingest_handler(req: IngestHTTPRequest) -> IngestHTTPResponse:
    # ... existing body unchanged ...

if not DISTRIBUTION_MODE:
    app.post("/ingest", response_model=IngestHTTPResponse)(_ingest_handler)
```

Apply the same pattern to `/reindex`. Move the function bodies into `_ingest_handler` / `_reindex_handler` and conditionally call `app.post(...)(handler)` only when `not DISTRIBUTION_MODE`.

If the existing handlers use decorators with multiple parameters or have docstrings, preserve them by passing them to `app.post(...)`:

```python
if not DISTRIBUTION_MODE:
    app.post(
        "/ingest",
        response_model=IngestHTTPResponse,
        summary="Ingest a session's artifacts into the corpus",
    )(_ingest_handler)
```

- [ ] **Step 5: Update lifespan to branch on distribution mode**

Find the `lifespan` async context manager (around line 90-135) and update the corpus-verify call:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ... existing docstring ...
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    try:
        db = lancedb.connect(db_path)
        if "chunks" in db.list_tables().tables:
            table = db.open_table("chunks")
            if DISTRIBUTION_MODE:
                # RO-mounted corpus: no repair attempts, no legacy cleanup.
                # Spec §5.6.
                verify_corpus_v3_state_readonly(table)
            else:
                # Operator mode: existing behavior (verify + repair + cleanup).
                verify_corpus_v3_state(table)
                try:
                    drop_full_text_index_if_present(table)
                except Exception as exc:
                    logger.debug("legacy full_text FTS index cleanup skipped: %s", exc)
        else:
            logger.info(
                "startup: chunks table does not exist yet at %s; FTS index "
                "will be built on first /ingest or next boot",
                db_path,
            )
    except CorpusInvalidError:
        raise
    except Exception as exc:
        logger.warning("startup corpus check raised %r; continuing", exc)
    yield
```

Add the `verify_corpus_v3_state_readonly` to the imports at the top of the file:

```python
from community_brain.query.corpus_verify import (
    CorpusInvalidError,
    verify_corpus_v3_state,
    verify_corpus_v3_state_readonly,
    drop_full_text_index_if_present,
)
```

- [ ] **Step 6: Run distribution-mode tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_distribution_mode_routes.py -v
```

Expected: all 5 tests PASS.

- [ ] **Step 7: Run full suite for regressions**

```bash
./.venv/bin/pytest tests/ -q
```

Expected: all existing tests pass. The operator-mode tests confirm /ingest and /reindex still work normally.

- [ ] **Step 8: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_distribution_mode_routes.py
git commit -m "$(cat <<'EOF'
feat(retrieval): add COMMUNITY_BRAIN_DISTRIBUTION_MODE for Tier B

When the env is true:
- /ingest and /reindex are not registered on the app (return 404)
- lifespan uses verify_corpus_v3_state_readonly (no repair attempts)
- /health.distribution_mode is True

When unset (operator default):
- All routes register as before
- lifespan uses verify_corpus_v3_state + drop_full_text_index_if_present
- /health.distribution_mode is False

Same source code, different runtime config. Per Tier B spec §2.3.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: `verify_corpus_clean_v3` CLI

**Files:**
- Create: `community-brain/src/community_brain/cli/__init__.py` (if not present)
- Create: `community-brain/src/community_brain/cli/verify_corpus_clean_v3.py`
- Create: `community-brain/tests/test_cli_verify_corpus_clean_v3.py`

- [ ] **Step 1: Check whether the cli/ directory exists**

```bash
ls community-brain/src/community_brain/cli/ 2>/dev/null || echo "does not exist"
```

If it does not exist, create the directory with an empty `__init__.py`:

```bash
mkdir -p community-brain/src/community_brain/cli
touch community-brain/src/community_brain/cli/__init__.py
```

- [ ] **Step 2: Write failing tests for the CLI**

Create `community-brain/tests/test_cli_verify_corpus_clean_v3.py`:

```python
"""verify_corpus_clean_v3 CLI: release-time gate per Tier B spec §5.4.

Asserts a compacted-and-staged LanceDB is in clean v3 state (FTS index
built on bm25_text, no legacy v2 FTS index on full_text). Exit 0 if
clean; exit non-zero with stderr message if not.
"""
import subprocess
import sys

import lancedb
import pyarrow as pa
import pytest


def _make_db(path, *, with_bm25=True, with_fts_index=True, with_legacy_fts=False):
    db = lancedb.connect(str(path))
    fields = [("session_id", pa.string())]
    if with_bm25:
        fields.append(("bm25_text", pa.string()))
    fields.append(("full_text", pa.string()))
    table = db.create_table("chunks", schema=pa.schema(fields), mode="overwrite")
    table.add([{"session_id": "s1", "bm25_text": "hi", "full_text": "hi"}]
              if with_bm25
              else [{"session_id": "s1", "full_text": "hi"}])
    if with_fts_index and with_bm25:
        table.create_fts_index("bm25_text", replace=True)
    if with_legacy_fts:
        table.create_fts_index("full_text", replace=True)
    return path


def _run_cli(db_path):
    return subprocess.run(
        [sys.executable, "-m",
         "community_brain.cli.verify_corpus_clean_v3", str(db_path)],
        capture_output=True, text=True,
    )


def test_cli_exits_zero_on_clean_v3_corpus(tmp_path):
    _make_db(tmp_path, with_bm25=True, with_fts_index=True, with_legacy_fts=False)
    result = _run_cli(tmp_path)
    assert result.returncode == 0, f"stderr: {result.stderr}"


def test_cli_exits_nonzero_when_bm25_column_missing(tmp_path):
    _make_db(tmp_path, with_bm25=False, with_fts_index=False)
    result = _run_cli(tmp_path)
    assert result.returncode != 0
    assert "bm25_text" in result.stderr.lower()


def test_cli_exits_nonzero_when_fts_index_missing(tmp_path):
    _make_db(tmp_path, with_bm25=True, with_fts_index=False)
    result = _run_cli(tmp_path)
    assert result.returncode != 0
    assert "fts" in result.stderr.lower() or "index" in result.stderr.lower()


def test_cli_exits_nonzero_when_legacy_full_text_fts_present(tmp_path):
    _make_db(tmp_path, with_bm25=True, with_fts_index=True, with_legacy_fts=True)
    result = _run_cli(tmp_path)
    assert result.returncode != 0
    assert "full_text" in result.stderr.lower() or "legacy" in result.stderr.lower()


def test_cli_handles_nonexistent_path(tmp_path):
    bogus = tmp_path / "nonexistent"
    result = _run_cli(bogus)
    assert result.returncode != 0
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd community-brain
./.venv/bin/pytest tests/test_cli_verify_corpus_clean_v3.py -v
```

Expected: ModuleNotFoundError — the CLI does not exist yet.

- [ ] **Step 4: Implement the CLI**

Create `community-brain/src/community_brain/cli/verify_corpus_clean_v3.py`:

```python
"""verify_corpus_clean_v3 — release-time gate for Tier B corpus tarballs.

Asserts a staged (post-compaction) LanceDB at the given path is in
clean v3 state:
  1. bm25_text column present
  2. FTS index on bm25_text exists
  3. NO legacy FTS index on full_text (left over from pre-v3)

Used by scripts/release-corpus.sh between compaction and tarballing.
A non-zero exit aborts the release before the bad blob can ship.

Usage:
    python -m community_brain.cli.verify_corpus_clean_v3 <lancedb_path>

The path should point to the directory containing the `chunks.lance`
table (i.e. one level above chunks.lance, e.g. `/tmp/staging/lancedb/nomic-v1`).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import lancedb

from community_brain.query.corpus_verify import (
    CorpusInvalidError,
    verify_corpus_v3_state_readonly,
)


def _has_legacy_full_text_fts(table) -> bool:
    """True if any FTS-style index is registered on the full_text column."""
    try:
        indices = table.list_indices()
    except Exception:
        return False
    for idx in indices:
        idx_type = getattr(idx, "index_type", None)
        columns = getattr(idx, "columns", []) or []
        if idx_type in ("FTS", "INVERTED") and "full_text" in columns:
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify a staged LanceDB is in clean v3 state for distribution."
    )
    parser.add_argument(
        "db_path",
        type=Path,
        help="Path to LanceDB directory (e.g. /tmp/staging/lancedb/nomic-v1)",
    )
    args = parser.parse_args(argv)

    if not args.db_path.exists():
        print(f"ERROR: path does not exist: {args.db_path}", file=sys.stderr)
        return 2

    try:
        db = lancedb.connect(str(args.db_path))
    except Exception as exc:
        print(f"ERROR: cannot open LanceDB at {args.db_path}: {exc}", file=sys.stderr)
        return 2

    tables = db.list_tables().tables if hasattr(db.list_tables(), "tables") else list(db.table_names())
    if "chunks" not in tables:
        print(f"ERROR: no 'chunks' table in {args.db_path}", file=sys.stderr)
        return 2

    table = db.open_table("chunks")

    # Structural + FTS-presence check (raises CorpusInvalidError on failure).
    try:
        verify_corpus_v3_state_readonly(table)
    except CorpusInvalidError as exc:
        print(f"ERROR: corpus failed v3 readonly check: {exc}", file=sys.stderr)
        return 1

    # Legacy v2 index check (clean v3 corpora must NOT carry full_text FTS).
    if _has_legacy_full_text_fts(table):
        print(
            "ERROR: legacy FTS index detected on full_text column. "
            "Compaction did not strip the v2 index. Drop it before "
            "tarballing — recipients on RO mounts cannot do this themselves.",
            file=sys.stderr,
        )
        return 1

    print(f"OK: corpus at {args.db_path} is clean v3 state.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_cli_verify_corpus_clean_v3.py -v
```

Expected: all 5 tests PASS. If the `_has_legacy_full_text_fts` heuristic doesn't catch the legacy index in the test (e.g., index_type naming varies between lancedb versions), adjust the type-matching set.

- [ ] **Step 6: Run full suite for regressions**

```bash
./.venv/bin/pytest tests/ -q
```

Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add community-brain/src/community_brain/cli/ \
        community-brain/tests/test_cli_verify_corpus_clean_v3.py
git commit -m "$(cat <<'EOF'
feat(cli): add verify_corpus_clean_v3 release-time gate

CLI used by scripts/release-corpus.sh between compaction and tarballing.
Confirms the staged LanceDB is in clean v3 state (bm25_text column +
FTS index present; no legacy full_text FTS index). Non-zero exit
aborts the release before a malformed corpus can ship.

Spec: §5.4 release recipe.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 6: `write_corpus_manifest` CLI

**Files:**
- Create: `community-brain/src/community_brain/cli/write_corpus_manifest.py`
- Create: `community-brain/tests/test_cli_write_corpus_manifest.py`

- [ ] **Step 1: Write failing tests for the manifest CLI**

Create `community-brain/tests/test_cli_write_corpus_manifest.py`:

```python
"""write_corpus_manifest CLI: emits corpus-manifest.json per Tier B spec §5.5.

Manifest fields:
  - corpus_version (string, from --version flag)
  - schema_version (from community_brain.ingestion.schema.SCHEMA_VERSION)
  - embedding_model (from COMMUNITY_BRAIN_EMBED_MODEL env or default)
  - session_count (distinct values of session_id column)
  - chunk_count (total row count)
  - generation_timestamp_utc (ISO 8601 'Z')
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone

import lancedb
import pyarrow as pa


def _seed_db(path, sessions: list[str], chunks_per_session: int = 2):
    db = lancedb.connect(str(path))
    schema = pa.schema([
        ("session_id", pa.string()),
        ("chunk_id", pa.string()),
        ("bm25_text", pa.string()),
    ])
    table = db.create_table("chunks", schema=schema, mode="overwrite")
    rows = []
    for s in sessions:
        for i in range(chunks_per_session):
            rows.append({
                "session_id": s,
                "chunk_id": f"{s}:c{i}",
                "bm25_text": f"chunk {i} of {s}",
            })
    table.add(rows)
    return path


def _run_cli(staging_path, out_path, version):
    return subprocess.run(
        [sys.executable, "-m", "community_brain.cli.write_corpus_manifest",
         "--staging", str(staging_path),
         "--out", str(out_path),
         "--version", version],
        capture_output=True, text=True,
    )


def test_writes_manifest_with_expected_fields(tmp_path):
    db_dir = tmp_path / "lancedb" / "nomic-v1"
    db_dir.mkdir(parents=True)
    _seed_db(db_dir, sessions=["s1", "s2", "s3"], chunks_per_session=4)
    out = tmp_path / "manifest.json"

    result = _run_cli(db_dir.parent.parent, out, "v1.0.0")
    assert result.returncode == 0, f"stderr: {result.stderr}"

    data = json.loads(out.read_text())
    assert data["corpus_version"] == "v1.0.0"
    assert data["schema_version"] == "1.1"  # matches schema.SCHEMA_VERSION
    assert data["session_count"] == 3
    assert data["chunk_count"] == 12  # 3 sessions * 4 chunks
    assert "embedding_model" in data
    assert "generation_timestamp_utc" in data
    # ISO 8601 with 'Z' suffix
    assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", data["generation_timestamp_utc"])
    assert data["generation_timestamp_utc"].endswith("Z")


def test_embedding_model_respects_env(tmp_path, monkeypatch):
    db_dir = tmp_path / "lancedb" / "nomic-v1"
    db_dir.mkdir(parents=True)
    _seed_db(db_dir, sessions=["s1"], chunks_per_session=1)
    out = tmp_path / "m.json"

    monkeypatch.setenv("COMMUNITY_BRAIN_EMBED_MODEL", "custom-model")
    result = subprocess.run(
        [sys.executable, "-m", "community_brain.cli.write_corpus_manifest",
         "--staging", str(db_dir.parent.parent),
         "--out", str(out),
         "--version", "v0.0.1"],
        capture_output=True, text=True,
        env={**__import__("os").environ, "COMMUNITY_BRAIN_EMBED_MODEL": "custom-model"},
    )
    assert result.returncode == 0
    data = json.loads(out.read_text())
    assert data["embedding_model"] == "custom-model"


def test_exits_nonzero_on_missing_db(tmp_path):
    out = tmp_path / "m.json"
    result = _run_cli(tmp_path / "nonexistent", out, "v1.0.0")
    assert result.returncode != 0
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd community-brain
./.venv/bin/pytest tests/test_cli_write_corpus_manifest.py -v
```

Expected: ModuleNotFoundError — CLI does not exist yet.

- [ ] **Step 3: Implement the manifest CLI**

Create `community-brain/src/community_brain/cli/write_corpus_manifest.py`:

```python
"""write_corpus_manifest — emit corpus-manifest.json for a staged LanceDB.

Used by scripts/release-corpus.sh after compaction. The manifest ships
alongside the corpus tarball; verify-install.sh reads it to cross-check
the running server's /health response.

Usage:
    python -m community_brain.cli.write_corpus_manifest \
        --staging /tmp/corpus-staging-v1.0.0 \
        --out corpus-manifest.json \
        --version v1.0.0

The --staging path should point to the staging root that contains
lancedb/nomic-v1/chunks.lance/ inside.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import lancedb

from community_brain.ingestion.embedding import _active_embed_model
from community_brain.ingestion.schema import SCHEMA_VERSION


def _utc_iso_z() -> str:
    """ISO 8601 timestamp with 'Z' suffix (Zulu time)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _count_sessions_and_chunks(table) -> tuple[int, int]:
    """Return (distinct session_id count, total row count)."""
    df = table.to_pandas()
    return (df["session_id"].nunique(), len(df))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write corpus-manifest.json for a staged LanceDB."
    )
    parser.add_argument("--staging", type=Path, required=True,
                        help="Staging root containing lancedb/nomic-v1/chunks.lance/")
    parser.add_argument("--out", type=Path, required=True,
                        help="Path to write corpus-manifest.json")
    parser.add_argument("--version", required=True,
                        help="Corpus version string (e.g. 'v1.0.0')")
    args = parser.parse_args(argv)

    db_path = args.staging / "lancedb" / "nomic-v1"
    if not db_path.exists():
        print(f"ERROR: lancedb path not found: {db_path}", file=sys.stderr)
        return 2

    try:
        db = lancedb.connect(str(db_path))
        table = db.open_table("chunks")
    except Exception as exc:
        print(f"ERROR: cannot open chunks table at {db_path}: {exc}", file=sys.stderr)
        return 2

    session_count, chunk_count = _count_sessions_and_chunks(table)

    manifest = {
        "corpus_version": args.version,
        "schema_version": SCHEMA_VERSION,
        "embedding_model": _active_embed_model(),
        "session_count": session_count,
        "chunk_count": chunk_count,
        "generation_timestamp_utc": _utc_iso_z(),
    }

    args.out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"OK: wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_cli_write_corpus_manifest.py -v
```

Expected: all 3 tests PASS.

- [ ] **Step 5: Run full suite**

```bash
./.venv/bin/pytest tests/ -q
```

Expected: all tests pass.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/cli/write_corpus_manifest.py \
        community-brain/tests/test_cli_write_corpus_manifest.py
git commit -m "$(cat <<'EOF'
feat(cli): add write_corpus_manifest

Emits corpus-manifest.json with corpus_version, schema_version,
embedding_model, session_count, chunk_count, generation_timestamp_utc.
Used by scripts/release-corpus.sh; ships alongside the corpus tarball
so verify-install.sh can cross-check the running server's /health
response on recipient machines.

Spec: §5.5.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Milestone 1 Checkpoint

- [ ] **Run the full test suite end-to-end:**

```bash
cd community-brain
./.venv/bin/pytest tests/ -q
```

Expected: all tests pass. Count should be 302+ baseline + ~20 new tests added in this milestone = ~325+.

- [ ] **Manual smoke test of distribution mode:**

```bash
cd community-brain
COMMUNITY_BRAIN_DISTRIBUTION_MODE=true \
LANCEDB_PATH=/nonexistent \
./.venv/bin/uvicorn community_brain.query.retrieval_server:app --port 8999 &
SERVER_PID=$!
sleep 2
curl -s http://127.0.0.1:8999/health | jq .
curl -s -X POST http://127.0.0.1:8999/ingest -d '{}' -w "\nstatus: %{http_code}\n"
kill $SERVER_PID
```

Expected:
- `/health` returns `{status: ok, server_version: 0.3.0, schema_version: "1.1", embedding_model: "nomic-embed-text", distribution_mode: true}`
- `/ingest` returns HTTP 404

- [ ] **Verify operator mode still works:**

```bash
unset COMMUNITY_BRAIN_DISTRIBUTION_MODE
LANCEDB_PATH=/nonexistent \
./.venv/bin/uvicorn community_brain.query.retrieval_server:app --port 8999 &
SERVER_PID=$!
sleep 2
curl -s http://127.0.0.1:8999/health | jq .distribution_mode
curl -s -X POST http://127.0.0.1:8999/ingest -d '{}' -w "\nstatus: %{http_code}\n"
kill $SERVER_PID
```

Expected:
- `/health.distribution_mode` is `false`
- `/ingest` returns 422 (request validation error, not 404 — route IS registered)

Milestone 1 done. The retrieval-server image now supports Tier B distribution mode end-to-end at the package level.

---

## Milestone 2: Operator release pipeline

Outcome: operator can produce a corpus tarball + manifest from a live VM LanceDB; GitHub Actions builds the retrieval-server image on tag and opens a PR in the distribution repo with the new SHA.

### Task 7: `scripts/release-corpus.sh`

**Files:**
- Create: `scripts/release-corpus.sh`
- Create: `scripts/release-corpus-test.sh` (local sanity test)

- [ ] **Step 1: Check that the scripts/ directory exists**

```bash
ls scripts/ | head
```

Should already contain `snapshot-vm.sh` and others.

- [ ] **Step 2: Create the release-corpus.sh script**

Create `scripts/release-corpus.sh`:

```bash
#!/usr/bin/env bash
# scripts/release-corpus.sh — produce a Tier B corpus tarball + manifest.
#
# Performs the safe-snapshot sequence from spec §5.4:
#   1. Pauses retrieval-server on the VM
#   2. rsync-snapshots the live LanceDB to a staging path
#   3. Unpauses retrieval-server
#   4. Compacts the staging copy (optimize_files + cleanup_old_versions)
#   5. Verifies clean v3 state on the compacted copy
#   6. Tarballs + computes SHA-256 + writes corpus-manifest.json
#
# Output files (in $OUTPUT_DIR, default /tmp/corpus-release):
#   corpus-<VERSION>.tar.gz
#   sha256sum.txt
#   corpus-manifest.json
#
# Usage:
#   ./scripts/release-corpus.sh <VERSION>
#   ./scripts/release-corpus.sh v1.0.0
#
# Environment overrides:
#   VM_HOST                 (default: n8n-automation.patchoutech.lab)
#   VM_USER                 (default: pchouinard)
#   VM_LANCEDB_PATH         (default: /home/pchouinard/n8n/community-brain/lancedb)
#   VM_COMPOSE_DIR          (default: /home/pchouinard/n8n)
#   OUTPUT_DIR              (default: /tmp/corpus-release)
#   COMMUNITY_BRAIN_VENV    (default: ./community-brain/.venv)
#
# Exit codes:
#   0 — success
#   1 — verification or release step failed
#   2 — usage error or pre-flight failure

set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <VERSION>  (e.g. $0 v1.0.0)" >&2
    exit 2
fi

VERSION="$1"
VM_HOST="${VM_HOST:-n8n-automation.patchoutech.lab}"
VM_USER="${VM_USER:-pchouinard}"
VM_LANCEDB_PATH="${VM_LANCEDB_PATH:-/home/pchouinard/n8n/community-brain/lancedb}"
VM_COMPOSE_DIR="${VM_COMPOSE_DIR:-/home/pchouinard/n8n}"
OUTPUT_DIR="${OUTPUT_DIR:-/tmp/corpus-release}"
COMMUNITY_BRAIN_VENV="${COMMUNITY_BRAIN_VENV:-$(pwd)/community-brain/.venv}"

PYTHON="${COMMUNITY_BRAIN_VENV}/bin/python"

# Local staging path (on operator workstation; we rsync FROM the VM TO here).
STAGING_LOCAL="/tmp/corpus-staging-${VERSION}"

log() { echo "[release-corpus] $*" >&2; }

# Pre-flight checks
[[ -x "$PYTHON" ]] || { log "FATAL: python not found at $PYTHON"; exit 2; }
ssh -o BatchMode=yes -o ConnectTimeout=5 "${VM_USER}@${VM_HOST}" 'true' \
    || { log "FATAL: cannot SSH to ${VM_USER}@${VM_HOST}"; exit 2; }

# Step 1: pause retrieval-server on VM and rsync the live LanceDB.
log "pausing retrieval-server on ${VM_HOST}"
ssh "${VM_USER}@${VM_HOST}" \
    "cd ${VM_COMPOSE_DIR} && docker compose pause retrieval-server"

# Trap to ensure unpause on any failure.
unpause_vm() {
    log "unpausing retrieval-server"
    ssh "${VM_USER}@${VM_HOST}" \
        "cd ${VM_COMPOSE_DIR} && docker compose unpause retrieval-server" \
        || log "WARN: unpause failed; manual recovery required"
}
trap unpause_vm EXIT

log "rsyncing LanceDB from VM (this is the longest step; ~5-10 min at 5 GB)"
rm -rf "${STAGING_LOCAL}"
mkdir -p "${STAGING_LOCAL}/lancedb"
rsync -a "${VM_USER}@${VM_HOST}:${VM_LANCEDB_PATH}/" "${STAGING_LOCAL}/lancedb/"

log "unpausing retrieval-server"
ssh "${VM_USER}@${VM_HOST}" \
    "cd ${VM_COMPOSE_DIR} && docker compose unpause retrieval-server"
trap - EXIT  # clear the unpause trap; we already unpaused

# Step 2: compact the staging copy.
log "compacting staged LanceDB"
"${PYTHON}" - <<PYEOF
import lancedb
from datetime import timedelta
db = lancedb.connect("${STAGING_LOCAL}/lancedb/nomic-v1")
table = db.open_table("chunks")
table.optimize()
table.cleanup_old_versions(older_than=timedelta(seconds=0))
print("compaction OK")
PYEOF

# Step 3: assert clean v3 state on compacted copy.
log "verifying clean v3 state on compacted copy"
"${PYTHON}" -m community_brain.cli.verify_corpus_clean_v3 \
    "${STAGING_LOCAL}/lancedb/nomic-v1"

# Step 4: produce output artifacts.
mkdir -p "${OUTPUT_DIR}"
cd "${OUTPUT_DIR}"

TARBALL="corpus-${VERSION}.tar.gz"
log "tarring -> ${OUTPUT_DIR}/${TARBALL}"
tar -czf "${TARBALL}" -C "${STAGING_LOCAL}" .

log "writing sha256sum.txt"
sha256sum "${TARBALL}" > sha256sum.txt

log "writing corpus-manifest.json"
"${PYTHON}" -m community_brain.cli.write_corpus_manifest \
    --staging "${STAGING_LOCAL}" \
    --out "${OUTPUT_DIR}/corpus-manifest.json" \
    --version "${VERSION}"

log "release artifacts ready in ${OUTPUT_DIR}:"
ls -lh "${OUTPUT_DIR}"

log "next steps:"
log "  1. gh release create ${VERSION} ${OUTPUT_DIR}/${TARBALL} \\"
log "       ${OUTPUT_DIR}/sha256sum.txt ${OUTPUT_DIR}/corpus-manifest.json \\"
log "       --repo <operator>/community-brain-distribution"
log "  2. Open PR in community-brain-distribution updating download-corpus.sh"
log "     constants: CORPUS_VERSION=\"${VERSION}\", EXPECTED_SHA256=\"\$(awk '{print \$1}' sha256sum.txt)\""
```

Make it executable:

```bash
chmod +x scripts/release-corpus.sh
```

- [ ] **Step 3: Create a local sanity test for the script**

Create `scripts/release-corpus-test.sh`:

```bash
#!/usr/bin/env bash
# Minimal sanity test for release-corpus.sh.
# Builds a tiny fake LanceDB on this machine and runs the script's
# compaction + verification + tarball steps against it (no VM needed).
#
# Skip the rsync-from-VM portion by pre-staging the fake DB at the
# location the script expects.

set -euo pipefail

VERSION="v0.0.0-test"
STAGING="/tmp/corpus-staging-${VERSION}"
OUTPUT_DIR="/tmp/corpus-release-test"
PYTHON="$(pwd)/community-brain/.venv/bin/python"

rm -rf "${STAGING}" "${OUTPUT_DIR}"
mkdir -p "${STAGING}/lancedb/nomic-v1"

# Build a tiny clean-v3 fake corpus directly into staging.
"${PYTHON}" <<PYEOF
import lancedb
import pyarrow as pa
db = lancedb.connect("${STAGING}/lancedb/nomic-v1")
schema = pa.schema([
    ("session_id", pa.string()),
    ("chunk_id", pa.string()),
    ("bm25_text", pa.string()),
])
table = db.create_table("chunks", schema=schema, mode="overwrite")
table.add([
    {"session_id": "s1", "chunk_id": "s1:c0", "bm25_text": "alpha beta gamma"},
    {"session_id": "s1", "chunk_id": "s1:c1", "bm25_text": "delta epsilon"},
    {"session_id": "s2", "chunk_id": "s2:c0", "bm25_text": "zeta eta theta"},
])
table.create_fts_index("bm25_text", replace=True)
print("staging built")
PYEOF

# Run only the local-effect portion of release-corpus.sh.
echo "--- compact ---"
"${PYTHON}" - <<PYEOF
import lancedb
from datetime import timedelta
db = lancedb.connect("${STAGING}/lancedb/nomic-v1")
t = db.open_table("chunks")
t.optimize()
t.cleanup_old_versions(older_than=timedelta(seconds=0))
PYEOF

echo "--- verify ---"
"${PYTHON}" -m community_brain.cli.verify_corpus_clean_v3 \
    "${STAGING}/lancedb/nomic-v1"

echo "--- tar + sha + manifest ---"
mkdir -p "${OUTPUT_DIR}"
cd "${OUTPUT_DIR}"
tar -czf "corpus-${VERSION}.tar.gz" -C "${STAGING}" .
sha256sum "corpus-${VERSION}.tar.gz" > sha256sum.txt
"${PYTHON}" -m community_brain.cli.write_corpus_manifest \
    --staging "${STAGING}" \
    --out "${OUTPUT_DIR}/corpus-manifest.json" \
    --version "${VERSION}"

echo "--- artifacts ---"
ls -lh "${OUTPUT_DIR}"
cat "${OUTPUT_DIR}/corpus-manifest.json"

echo
echo "OK: release-corpus.sh local sanity test passed"
```

Make it executable:

```bash
chmod +x scripts/release-corpus-test.sh
```

- [ ] **Step 4: Run the local sanity test**

```bash
./scripts/release-corpus-test.sh
```

Expected output: `OK: release-corpus.sh local sanity test passed`. Artifacts in `/tmp/corpus-release-test/` should include the tarball, sha256sum.txt, and a manifest reporting `session_count: 2, chunk_count: 3`.

- [ ] **Step 5: Commit**

```bash
git add scripts/release-corpus.sh scripts/release-corpus-test.sh
git commit -m "$(cat <<'EOF'
feat(scripts): add release-corpus.sh for Tier B corpus snapshots

Implements the safe-snapshot recipe from spec §5.4:
  1. SSH to VM, pause retrieval-server
  2. rsync live LanceDB to local staging
  3. Unpause retrieval-server (trap on any failure path)
  4. Compact staging copy (optimize + cleanup_old_versions)
  5. Run verify_corpus_clean_v3 CLI to assert ship-quality state
  6. Tar + SHA-256 + corpus-manifest.json

Companion script release-corpus-test.sh exercises the local-only
portion (compaction, verification, tarball, manifest) against a
synthetic tiny LanceDB without needing the VM. CI can run it as a
smoke test.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 8: `.github/workflows/build-retrieval-image.yml`

**Files:**
- Create: `.github/workflows/build-retrieval-image.yml`

- [ ] **Step 1: Create the workflow file**

Create `.github/workflows/build-retrieval-image.yml`:

```yaml
name: Build retrieval-server image (Tier B)

on:
  push:
    tags:
      - 'tier-b-retrieval-v*'

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Extract version from tag
        id: version
        run: |
          # tag format: tier-b-retrieval-v1.0.0 → version 1.0.0
          VERSION="${GITHUB_REF_NAME#tier-b-retrieval-v}"
          echo "version=${VERSION}" >> "$GITHUB_OUTPUT"

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.repository_owner }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build and push image
        id: build
        uses: docker/build-push-action@v5
        with:
          context: ./community-brain
          file: ./community-brain/Dockerfile
          push: true
          tags: |
            ghcr.io/${{ github.repository_owner }}/community-brain-retrieval:${{ steps.version.outputs.version }}
            ghcr.io/${{ github.repository_owner }}/community-brain-retrieval:latest
          # Build for amd64 + arm64 to cover Mac (Apple Silicon) and Linux x86.
          platforms: linux/amd64,linux/arm64
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Print published digest
        run: |
          echo "Published digest: ${{ steps.build.outputs.digest }}"
          echo "Tag: ${{ steps.version.outputs.version }}"
          echo ""
          echo "Next step: open a PR in community-brain-distribution that"
          echo "updates docker-compose.yml to pin the new SHA:"
          echo "  ghcr.io/${{ github.repository_owner }}/community-brain-retrieval@${{ steps.build.outputs.digest }}"

      - name: Open PR in distribution repo
        env:
          GH_TOKEN: ${{ secrets.DISTRIBUTION_REPO_TOKEN }}
          NEW_DIGEST: ${{ steps.build.outputs.digest }}
          NEW_VERSION: ${{ steps.version.outputs.version }}
          OWNER: ${{ github.repository_owner }}
        run: |
          set -euo pipefail
          WORK=$(mktemp -d)
          cd "$WORK"
          gh repo clone "${OWNER}/community-brain-distribution" dist
          cd dist
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          BRANCH="bump-retrieval-${NEW_VERSION}"
          git checkout -b "${BRANCH}"

          # Update the image SHA in docker-compose.yml.
          python3 - <<PYEOF
          import re, pathlib
          p = pathlib.Path("docker-compose.yml")
          s = p.read_text()
          # Match: image: ghcr.io/<owner>/community-brain-retrieval@sha256:...
          new_image = f"image: ghcr.io/${OWNER}/community-brain-retrieval@${NEW_DIGEST}"
          s = re.sub(
              r"image:\s*ghcr\.io/[^/]+/community-brain-retrieval@sha256:[a-f0-9]+",
              new_image,
              s,
          )
          p.write_text(s)
          PYEOF

          git add docker-compose.yml
          git commit -m "chore: bump retrieval-server to ${NEW_VERSION}

          Image: ghcr.io/${OWNER}/community-brain-retrieval@${NEW_DIGEST}
          Tag: ${NEW_VERSION}

          Auto-opened by operator-repo build-retrieval-image.yml workflow."
          git push -u origin "${BRANCH}"

          gh pr create \
            --title "Bump retrieval-server to ${NEW_VERSION}" \
            --body "Auto-opened by operator-repo \`build-retrieval-image.yml\`.

          New image: \`ghcr.io/${OWNER}/community-brain-retrieval@${NEW_DIGEST}\`
          Version: ${NEW_VERSION}

          Verify before merging:
          1. CI on this PR (verify-on-pr.yml) runs the fixture-corpus smoke install.
          2. Inspect the image SHA matches the publish event.
          3. Confirm no schema-version bump (or, if there is one, that a matching corpus release was published)."
```

- [ ] **Step 2: Document the required secret**

Manual operator task (not part of automated steps): in the operator repo settings → Secrets → Actions, create:

- `DISTRIBUTION_REPO_TOKEN` — a fine-grained Personal Access Token scoped to `<owner>/community-brain-distribution` with `contents: write` and `pull-requests: write` permissions.

Add a comment at the top of the workflow file linking to spec §4.3.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/build-retrieval-image.yml
git commit -m "$(cat <<'EOF'
feat(ci): add Tier B image build + cross-repo PR workflow

On `tier-b-retrieval-v*` tag push:
  1. Build community-brain Docker image for linux/amd64 + linux/arm64
  2. Push to ghcr.io with version tag + @sha256 digest
  3. Open PR in community-brain-distribution that bumps the SHA pin
     in docker-compose.yml

Requires DISTRIBUTION_REPO_TOKEN secret — a fine-grained PAT scoped
to the distribution repo with contents+pull-requests write.

Spec: §4.1 Flow A.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 9: `.github/workflows/sync-curated-files.yml`

**Files:**
- Create: `.github/workflows/sync-curated-files.yml`

- [ ] **Step 1: Create the sync workflow**

Create `.github/workflows/sync-curated-files.yml`:

```yaml
name: Sync curated files to distribution repo

on:
  push:
    branches:
      - main
    paths:
      - 'community-brain/src/community_brain/openwebui/community_brain_filter.py'
      - 'docs/inference-guidelines.md'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout operator repo
        uses: actions/checkout@v4

      - name: Sync curated files to community-brain-distribution
        env:
          GH_TOKEN: ${{ secrets.DISTRIBUTION_REPO_TOKEN }}
          OWNER: ${{ github.repository_owner }}
        run: |
          set -euo pipefail
          WORK=$(mktemp -d)
          cd "$WORK"
          gh repo clone "${OWNER}/community-brain-distribution" dist
          cd dist
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

          # Copy curated files in. Source paths relative to the workspace
          # (we keep them in the runner from the actions/checkout step).
          cp "${GITHUB_WORKSPACE}/community-brain/src/community_brain/openwebui/community_brain_filter.py" \
             ./community_brain_filter.py
          cp "${GITHUB_WORKSPACE}/docs/inference-guidelines.md" \
             ./inference-guidelines.md

          # If nothing changed, exit silently.
          if git diff --quiet; then
              echo "No changes to sync."
              exit 0
          fi

          BRANCH="sync-curated-$(date -u +%Y%m%d-%H%M%S)"
          git checkout -b "${BRANCH}"
          git add community_brain_filter.py inference-guidelines.md
          git commit -m "chore: sync curated files from operator repo

          Auto-synced from upstream commit ${GITHUB_SHA}."
          git push -u origin "${BRANCH}"

          gh pr create \
            --title "Sync curated files from operator repo" \
            --body "Auto-opened by operator-repo \`sync-curated-files.yml\` workflow.

          Updated files:
          - community_brain_filter.py (Open WebUI filter)
          - inference-guidelines.md (custom-model system prompt)

          Upstream commit: ${GITHUB_SHA}

          Verify before merging:
          1. CI on this PR (verify-on-pr.yml) runs the smoke install
          2. Inspect that the diff looks intentional (no merge-conflict noise)"
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/sync-curated-files.yml
git commit -m "$(cat <<'EOF'
feat(ci): auto-sync filter + inference guidelines to distribution repo

When community_brain_filter.py or docs/inference-guidelines.md changes
on main, this workflow opens a PR in community-brain-distribution that
pulls the new versions into the distribution repo. Operator reviews
and merges.

Eliminates drift between the two repos for files that should be byte-
identical in both places.

Spec: §4.1 sync-curated-files.yml.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Milestone 2 Checkpoint

- [ ] **Run release-corpus-test.sh end-to-end:**

```bash
./scripts/release-corpus-test.sh
```

Expected: green output, artifacts in `/tmp/corpus-release-test/`. Inspect the manifest:

```bash
cat /tmp/corpus-release-test/corpus-manifest.json
```

Expected fields: `corpus_version`, `schema_version` ("1.1"), `embedding_model`, `session_count`, `chunk_count`, `generation_timestamp_utc`.

- [ ] **Lint workflow files:**

```bash
# yamllint if installed, otherwise just YAML-parse them:
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/build-retrieval-image.yml'))"
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/sync-curated-files.yml'))"
```

Expected: both parse without errors.

- [ ] **Defer to actual operator action:** publishing the first `tier-b-retrieval-v*` tag, creating the `DISTRIBUTION_REPO_TOKEN` secret, and verifying the cross-repo PR opens. These all require the distribution repo to exist (Milestone 3). Mark complete pending that integration.

Milestone 2 done at the script + workflow definition level. Live verification happens after Milestone 3.

---

## Milestone 3: Distribution repo creation

Outcome: a new public `community-brain-distribution` GitHub repo exists with all the install-side files, a fixture corpus, and CI that runs a fresh-install smoke test on every PR. Tagged v0.0.0-rc1 (release candidate, pre-real-corpus).

This milestone produces files in a NEW external repository. Tasks here create local files in a sibling directory `../community-brain-distribution/` (operator pushes them to the new repo manually). For implementation purposes, all paths in this milestone are relative to a sibling working directory that the operator will turn into the repo.

### Task 10: Bootstrap the distribution repo locally

**Files:**
- Create: sibling directory `../community-brain-distribution/`

- [ ] **Step 1: Decide whether the sibling dir already exists**

```bash
ls ../community-brain-distribution/ 2>/dev/null && echo "exists" || echo "does not exist"
```

If exists, ask operator before overwriting. If not, proceed.

- [ ] **Step 2: Create the directory structure**

```bash
mkdir -p ../community-brain-distribution/{docs/screenshots,tests/fixtures/corpus,tests/fixtures/mock-ollama,.github/workflows}
cd ../community-brain-distribution
git init -b main
```

- [ ] **Step 3: Create .gitignore**

Create `../community-brain-distribution/.gitignore`:

```
# Recipient-local state
.env
corpus/
corpus.previous/

# Container runtime state (Open WebUI persistence)
open-webui-data/

# Python local-dev artifacts (only relevant if recipients muck around)
__pycache__/
*.pyc
.venv/

# OS noise
.DS_Store
Thumbs.db
```

- [ ] **Step 4: Initial commit**

```bash
cd ../community-brain-distribution
git add .gitignore
git commit -m "chore: initial repo with .gitignore"
```

---

### Task 11: `.env.example` for the distribution repo

**Files:**
- Create: `../community-brain-distribution/.env.example`

- [ ] **Step 1: Create the .env.example file**

Create `../community-brain-distribution/.env.example`:

```bash
# Community Brain — Tier B Distribution
# ----------------------------------------------------------------------
# Copy this file to `.env` (`cp .env.example .env`) and fill in the
# required placeholders. Optional overrides are commented out — leave
# them as-is unless you have a reason to change them.

# ============================================================
# Required — fill in before `docker compose up`.
# ============================================================

# URL where Ollama is reachable from inside the Docker network.
# For Docker Desktop on Mac/Windows: host.docker.internal works.
# For Linux: same, thanks to extra_hosts: host.docker.internal:host-gateway
# in docker-compose.yml.
OLLAMA_BASE_URL=http://host.docker.internal:11434

# Open WebUI session secret. Generate with:  openssl rand -hex 32
# This MUST be set, or `docker compose up` will fail fast.
WEBUI_SECRET_KEY=

# ============================================================
# Optional — image defaults are fine for nearly everyone.
# Uncomment only if you have a specific reason to override.
# ============================================================

# Embedding model name (must match the one used to embed the shipped
# corpus). Default: nomic-embed-text (Ollama default tag).
# COMMUNITY_BRAIN_EMBED_MODEL=nomic-embed-text

# ============================================================
# Chat inference — uncomment EXACTLY ONE block below.
# Open WebUI reads these env vars on startup and auto-configures the
# connection. You do NOT need to paste credentials in the GUI.
# ============================================================

# --- Option A: Local Ollama chat ---
# Requires ~24 GB unified memory (Mac Apple Silicon) or a beefy GPU.
# Make sure `ollama pull gpt-oss:20b` has been run first.
# INFERENCE_LOCAL_MODEL=gpt-oss:20b

# --- Option B: Cloud OpenAI-compatible chat ---
# Works with: OpenAI, OpenRouter (proxies Anthropic/Gemini/etc),
# Together, Groq, and anyone else who speaks OpenAI's API shape.
# OPENAI_API_BASE_URL=https://openrouter.ai/api/v1
# OPENAI_API_KEY=sk-or-v1-...
# INFERENCE_CLOUD_MODEL=anthropic/claude-sonnet-4.6
```

- [ ] **Step 2: Commit**

```bash
cd ../community-brain-distribution
git add .env.example
git commit -m "feat: add .env.example with required + optional + chat-mode blocks"
```

---

### Task 12: `docker-compose.yml` for the distribution repo

**Files:**
- Create: `../community-brain-distribution/docker-compose.yml`

- [ ] **Step 1: Create the compose file**

Create `../community-brain-distribution/docker-compose.yml`:

```yaml
# Community Brain — Tier B Distribution
# ----------------------------------------------------------------------
# Self-host stack for recipients. All services bind to 127.0.0.1 only.
# Image SHAs are pinned for reproducibility; CI bumps them via PR when
# the operator cuts a new release.

services:
  retrieval-server:
    # SHA bumped by .github/workflows/build-retrieval-image.yml in the
    # operator repo on `tier-b-retrieval-v*` tag.
    image: ghcr.io/REPLACE_OPERATOR_HERE/community-brain-retrieval@sha256:PLACEHOLDER_BUMPED_BY_CI
    environment:
      OLLAMA_BASE_URL: ${OLLAMA_BASE_URL}
      COMMUNITY_BRAIN_EMBED_MODEL: ${COMMUNITY_BRAIN_EMBED_MODEL:-nomic-embed-text}
      COMMUNITY_BRAIN_DISTRIBUTION_MODE: "true"
      LANCEDB_PATH: /data/lancedb/nomic-v1
    volumes:
      # Corpus directory: ./corpus/lancedb/nomic-v1/chunks.lance/...
      # Mounts at /data so LANCEDB_PATH resolves correctly.
      # Read-only: distribution-mode server expects clean v3 state and
      # never writes (no /ingest, no /reindex, no index repair).
      - ./corpus:/data:ro
    ports:
      - "127.0.0.1:8999:8999"
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

  open-webui:
    # SHA pinned manually by operator (Flow C). Bumping requires
    # confirming alembic migrations don't break the filter.
    image: ghcr.io/open-webui/open-webui@sha256:PLACEHOLDER_OWUI_SHA
    # env_file passes .env contents directly. Commented-out variables in
    # .env simply don't enter the container env, so OWUI's defaults
    # apply. Required values are forced via shell-substitution below
    # for fail-fast behavior.
    env_file:
      - .env
    environment:
      WEBUI_SECRET_KEY: ${WEBUI_SECRET_KEY:?WEBUI_SECRET_KEY must be set in .env}
    volumes:
      - open-webui-data:/app/backend/data
    ports:
      - "127.0.0.1:3000:8080"
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

volumes:
  open-webui-data:
    external: false
```

- [ ] **Step 2: Commit**

```bash
cd ../community-brain-distribution
git add docker-compose.yml
git commit -m "feat: add docker-compose.yml with SHA-pin placeholders

Both image SHAs are PLACEHOLDER values that get bumped by CI on real
releases. Local fixture-CI uses an override compose file (added in a
later task) to substitute fixture images."
```

---

### Task 13: `verify-install.sh`

**Files:**
- Create: `../community-brain-distribution/verify-install.sh`

- [ ] **Step 1: Create verify-install.sh**

Create `../community-brain-distribution/verify-install.sh`:

```bash
#!/usr/bin/env bash
# verify-install.sh — verification harness for Tier B install.
#
# Run after each major install step, or end-to-end after Step 9.
# Idempotent. Per spec §7.
#
# Usage:
#   ./verify-install.sh                  # all checks
#   ./verify-install.sh --step N         # checks for step N (1-9)
#   ./verify-install.sh --post-install   # end-to-end smoke
#   ./verify-install.sh --check-env-drift  # warn on missing .env keys

set -uo pipefail   # NOT -e: we want to keep running after a single check fails

PASS_COUNT=0
FAIL_COUNT=0
declare -a FAILURES=()

# Color codes; degrade gracefully if not a TTY.
if [[ -t 1 ]]; then
    GREEN='\033[0;32m'; RED='\033[0;31m'; YELLOW='\033[0;33m'; NC='\033[0m'
else
    GREEN=''; RED=''; YELLOW=''; NC=''
fi

ok()  { PASS_COUNT=$((PASS_COUNT+1)); printf "${GREEN}[✓]${NC} %s\n" "$1"; }
bad() {
    FAIL_COUNT=$((FAIL_COUNT+1))
    FAILURES+=("$1")
    printf "${RED}[✗]${NC} %s\n" "$1"
    [[ -n "${2:-}" ]] && printf "    ${YELLOW}→${NC} %s\n" "$2"
}

# Detect SHA256 tool (macOS uses shasum -a 256; Linux uses sha256sum).
sha256_cmd() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "$1" | awk '{print $1}'
    else
        return 2
    fi
}

# === Individual checks ===

check_docker() {
    if command -v docker >/dev/null 2>&1; then
        ok "docker installed ($(docker --version 2>&1 | head -1))"
    else
        bad "docker not installed" "install Docker Desktop or docker-ce"
    fi

    if docker compose version >/dev/null 2>&1; then
        ok "docker compose v2 ($(docker compose version --short 2>&1))"
    else
        bad "docker compose v2 missing" \
            "v1 'docker-compose' is unsupported; upgrade to v2 plugin"
    fi
}

check_ollama() {
    local url="${OLLAMA_BASE_URL:-http://host.docker.internal:11434}"
    # Convert host.docker.internal to localhost for direct testing from
    # the recipient's shell (not from inside a container).
    local probe_url="${url/host.docker.internal/localhost}"
    if curl -sf "${probe_url}/api/tags" >/dev/null 2>&1; then
        ok "Ollama reachable at ${probe_url}"
        if curl -s "${probe_url}/api/tags" | grep -q '"name":\s*"nomic-embed-text'; then
            ok "nomic-embed-text model is pulled"
        else
            bad "nomic-embed-text model not in Ollama" \
                "run: ollama pull nomic-embed-text"
        fi
    else
        bad "Ollama not reachable at ${probe_url}" \
            "start Ollama (mac/win: open Ollama app; linux: ollama serve)"
    fi
}

check_env_file() {
    if [[ ! -f .env ]]; then
        bad ".env does not exist" "run: cp .env.example .env  and fill in the required values"
        return
    fi
    ok ".env exists"

    # WEBUI_SECRET_KEY must be set and non-empty.
    if grep -qE '^WEBUI_SECRET_KEY=.+' .env; then
        ok "WEBUI_SECRET_KEY is set"
    else
        bad "WEBUI_SECRET_KEY is empty" \
            "generate one: openssl rand -hex 32 and paste into .env"
    fi

    # Exactly one inference block uncommented.
    local local_set=0 cloud_set=0
    grep -qE '^INFERENCE_LOCAL_MODEL=' .env && local_set=1
    grep -qE '^OPENAI_API_BASE_URL=' .env && cloud_set=1
    if (( local_set + cloud_set == 0 )); then
        bad "no inference mode configured" \
            "uncomment EXACTLY ONE block in .env (Option A or Option B)"
    elif (( local_set + cloud_set == 2 )); then
        bad "both inference modes configured" \
            "uncomment EXACTLY ONE block in .env, not both"
    else
        ok "exactly one inference mode configured"
    fi
}

check_corpus() {
    if [[ ! -d ./corpus ]]; then
        bad "./corpus directory missing" "run: ./download-corpus.sh"
        return
    fi
    if [[ ! -d ./corpus/lancedb/nomic-v1/chunks.lance ]]; then
        bad "./corpus/lancedb/nomic-v1/chunks.lance missing" \
            "run: ./download-corpus.sh (your corpus is incomplete)"
        return
    fi
    ok "corpus directory present"

    if [[ ! -f ./corpus/corpus-manifest.json ]]; then
        bad "./corpus/corpus-manifest.json missing" \
            "run: ./download-corpus.sh"
        return
    fi
    ok "corpus-manifest.json present"
}

check_stack_running() {
    if ! docker compose ps --status running 2>/dev/null | grep -q retrieval-server; then
        bad "retrieval-server container is not running" \
            "run: docker compose up -d"
        return
    fi
    ok "retrieval-server container running"

    if ! docker compose ps --status running 2>/dev/null | grep -q open-webui; then
        bad "open-webui container is not running" \
            "run: docker compose up -d"
        return
    fi
    ok "open-webui container running"

    # Check 127.0.0.1 binding (not 0.0.0.0).
    local rs_binding
    rs_binding=$(docker compose port retrieval-server 8999 2>/dev/null || echo "")
    if [[ "$rs_binding" == *"127.0.0.1"* ]]; then
        ok "retrieval-server bound to 127.0.0.1"
    else
        bad "retrieval-server binding looks wrong: ${rs_binding}" \
            "compose.yml ports: should be \"127.0.0.1:8999:8999\""
    fi
}

check_health_and_manifest_match() {
    local health_json
    health_json=$(curl -sf http://127.0.0.1:8999/health 2>/dev/null || echo "")
    if [[ -z "$health_json" ]]; then
        bad "/health unreachable on 127.0.0.1:8999" \
            "check: docker compose logs retrieval-server"
        return
    fi
    ok "/health returns 200"

    if ! command -v jq >/dev/null 2>&1; then
        bad "jq not installed" "install jq (brew install jq or apt install jq)"
        return
    fi

    local server_schema server_embed server_dm
    server_schema=$(echo "$health_json" | jq -r '.schema_version')
    server_embed=$(echo "$health_json" | jq -r '.embedding_model')
    server_dm=$(echo "$health_json" | jq -r '.distribution_mode')

    if [[ "$server_dm" != "true" ]]; then
        bad "/health.distribution_mode is not true: ${server_dm}" \
            "image was built without COMMUNITY_BRAIN_DISTRIBUTION_MODE=true in compose"
    else
        ok "/health.distribution_mode is true"
    fi

    if [[ ! -f ./corpus/corpus-manifest.json ]]; then
        return  # already reported by check_corpus
    fi
    local manifest_schema manifest_embed
    manifest_schema=$(jq -r '.schema_version' ./corpus/corpus-manifest.json)
    manifest_embed=$(jq -r '.embedding_model' ./corpus/corpus-manifest.json)

    if [[ "$server_schema" == "$manifest_schema" ]]; then
        ok "schema_version matches (${server_schema})"
    else
        bad "schema_version mismatch: server=${server_schema} corpus=${manifest_schema}" \
            "re-fetch corpus: ./download-corpus.sh"
    fi
    if [[ "$server_embed" == "$manifest_embed" ]]; then
        ok "embedding_model matches (${server_embed})"
    else
        bad "embedding_model mismatch: server=${server_embed} corpus=${manifest_embed}" \
            "your server and corpus were embedded by different models"
    fi
}

check_sessions_count_matches_manifest() {
    if [[ ! -f ./corpus/corpus-manifest.json ]]; then return; fi
    if ! command -v jq >/dev/null 2>&1; then return; fi
    local expected actual
    expected=$(jq -r '.session_count' ./corpus/corpus-manifest.json)
    actual=$(curl -sf http://127.0.0.1:8999/sessions 2>/dev/null \
             | jq -r '.sessions | length' 2>/dev/null || echo "")
    if [[ -z "$actual" ]]; then
        bad "/sessions unreachable or malformed" \
            "check: docker compose logs retrieval-server"
        return
    fi
    if [[ "$expected" == "$actual" ]]; then
        ok "/sessions count matches manifest (${expected})"
    else
        bad "/sessions count mismatch: server=${actual} manifest=${expected}" \
            "corpus mount may be wrong; check docker compose config"
    fi
}

check_owui_reachable() {
    if curl -sf http://127.0.0.1:3000 -o /dev/null; then
        ok "Open WebUI reachable on 127.0.0.1:3000"
    else
        bad "Open WebUI not reachable on 127.0.0.1:3000" \
            "check: docker compose logs open-webui"
    fi
}

# === Step dispatchers ===

run_step_1() { check_docker; }
run_step_2() { check_ollama; }
run_step_4() { [[ -d .git ]] && ok "in a git checkout" || bad "not a git checkout" "git clone the distribution repo, then cd in"; }
run_step_5() { check_env_file; }
run_step_6() { check_corpus; }
run_step_7() { check_stack_running; check_health_and_manifest_match; }

run_post_install() {
    check_docker
    check_ollama
    check_env_file
    check_corpus
    check_stack_running
    check_health_and_manifest_match
    check_sessions_count_matches_manifest
    check_owui_reachable
}

run_all() { run_post_install; }

# === Main ===

MODE="all"
STEP=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        --step) MODE="step"; STEP="$2"; shift 2 ;;
        --post-install) MODE="post"; shift ;;
        --check-env-drift) MODE="env-drift"; shift ;;
        *) echo "Unknown arg: $1" >&2; exit 2 ;;
    esac
done

# Load .env if present so OLLAMA_BASE_URL etc. are visible to checks.
if [[ -f .env ]]; then
    # shellcheck disable=SC1091
    set -a; source .env; set +a
fi

case "$MODE" in
    all)        run_all ;;
    post)       run_post_install ;;
    step)
        case "$STEP" in
            1) run_step_1 ;;
            2) run_step_2 ;;
            4) run_step_4 ;;
            5) run_step_5 ;;
            6) run_step_6 ;;
            7) run_step_7 ;;
            *) echo "Unknown step: $STEP (valid: 1, 2, 4, 5, 6, 7)" >&2; exit 2 ;;
        esac ;;
    env-drift)
        if [[ ! -f .env ]]; then
            bad ".env missing" "cp .env.example .env"
        else
            # Compare keys in .env.example to keys in .env.
            example_keys=$(grep -oE '^[A-Z_]+=' .env.example | sort -u)
            actual_keys=$(grep -oE '^[A-Z_]+=' .env | sort -u)
            missing=$(comm -23 <(echo "$example_keys") <(echo "$actual_keys"))
            if [[ -n "$missing" ]]; then
                bad "missing keys in .env vs .env.example:" "$(echo "$missing" | tr '\n' ' ')"
            else
                ok ".env has all keys from .env.example"
            fi
        fi ;;
esac

echo
if (( FAIL_COUNT == 0 )); then
    printf "${GREEN}All checks passed${NC} (%d)\n" "$PASS_COUNT"
    exit 0
else
    printf "${RED}%d failed${NC} (%d passed)\n" "$FAIL_COUNT" "$PASS_COUNT"
    exit 1
fi
```

Make it executable:

```bash
chmod +x ../community-brain-distribution/verify-install.sh
```

- [ ] **Step 2: Smoke test the script against an empty install state**

```bash
cd ../community-brain-distribution
./verify-install.sh
```

Expected: most checks FAIL (no .env, no corpus, no stack running) but the script exits cleanly with exit code 1, not a syntax error. Output should be clean unicode ✓/✗ markers.

- [ ] **Step 3: Commit**

```bash
git add verify-install.sh
git commit -m "feat: add verify-install.sh harness

Per-step checks with idempotent invocation. Modes:
  --step N         single step (1, 2, 4, 5, 6, 7)
  --post-install   end-to-end smoke
  --check-env-drift  warn on .env keys missing vs .env.example

Detects sha256sum vs shasum -a 256 per spec §6.2.
Loads .env so checks see recipient configuration."
```

---

### Task 14: `download-corpus.sh`

**Files:**
- Create: `../community-brain-distribution/download-corpus.sh`

- [ ] **Step 1: Create download-corpus.sh**

Create `../community-brain-distribution/download-corpus.sh`:

```bash
#!/usr/bin/env bash
# download-corpus.sh — fetch + verify + extract the Tier B corpus.
#
# Idempotent: re-running with the same CORPUS_VERSION already-extracted
# exits 0 without re-fetching. Rollback rotation: existing ./corpus/ is
# moved to ./corpus.previous/ (one level kept).
#
# Per spec §5.5.

set -euo pipefail

# === Pinned by operator on each corpus release ===
CORPUS_VERSION="v0.0.0-rc1"
EXPECTED_SHA256="PLACEHOLDER_REPLACE_ON_RELEASE"
RELEASE_REPO="REPLACE_OPERATOR_HERE/community-brain-distribution"
# =================================================

CORPUS_DIR="./corpus"
PREVIOUS_DIR="./corpus.previous"

log() { echo "[download-corpus] $*" >&2; }

# Detect SHA tool.
sha256_of() {
    local f="$1"
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$f" | awk '{print $1}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "$f" | awk '{print $1}'
    else
        log "ERROR: neither sha256sum nor shasum found; install one"
        exit 2
    fi
}

# Idempotency short-circuit: already at target version?
if [[ -f "${CORPUS_DIR}/corpus-manifest.json" ]]; then
    if command -v jq >/dev/null 2>&1; then
        current=$(jq -r '.corpus_version' "${CORPUS_DIR}/corpus-manifest.json" 2>/dev/null || echo "")
        if [[ "$current" == "$CORPUS_VERSION" ]]; then
            log "corpus already at ${CORPUS_VERSION}; nothing to do"
            exit 0
        fi
    fi
fi

# Need gh CLI for release asset downloads (works on public + private alike).
if ! command -v gh >/dev/null 2>&1; then
    log "ERROR: gh CLI is required to download release assets"
    log "  install: https://cli.github.com/"
    exit 2
fi

# Fetch into a tmp dir to avoid touching ./corpus until validated.
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

log "fetching corpus ${CORPUS_VERSION} from ${RELEASE_REPO}"
cd "$TMP"
gh release download "${CORPUS_VERSION}" \
    --repo "${RELEASE_REPO}" \
    --pattern "corpus-${CORPUS_VERSION}.tar.gz" \
    --pattern "sha256sum.txt" \
    --pattern "corpus-manifest.json"

# Verify SHA-256.
log "verifying SHA-256"
actual=$(sha256_of "corpus-${CORPUS_VERSION}.tar.gz")
if [[ "$actual" != "$EXPECTED_SHA256" ]]; then
    log "ERROR: SHA-256 mismatch"
    log "  expected: $EXPECTED_SHA256"
    log "  actual:   $actual"
    log "  the download may be corrupt or the EXPECTED_SHA256 constant is stale"
    exit 1
fi
log "SHA-256 verified"

# Rollback rotation.
cd - >/dev/null
if [[ -d "$PREVIOUS_DIR" ]]; then
    log "removing old rollback at ${PREVIOUS_DIR}"
    rm -rf "$PREVIOUS_DIR"
fi
if [[ -d "$CORPUS_DIR" ]]; then
    log "rotating ${CORPUS_DIR} -> ${PREVIOUS_DIR}"
    mv "$CORPUS_DIR" "$PREVIOUS_DIR"
fi

# Extract.
mkdir -p "$CORPUS_DIR"
log "extracting tarball into ${CORPUS_DIR}"
tar -xzf "$TMP/corpus-${CORPUS_VERSION}.tar.gz" -C "$CORPUS_DIR"
cp "$TMP/corpus-manifest.json" "${CORPUS_DIR}/corpus-manifest.json"

log "corpus ${CORPUS_VERSION} ready"
log "  $(ls -lh "${CORPUS_DIR}/corpus-manifest.json" | awk '{print $5, $9}')"
log "  $(du -sh "${CORPUS_DIR}/lancedb" 2>/dev/null || true)"
```

Make it executable:

```bash
chmod +x download-corpus.sh
```

- [ ] **Step 2: Smoke test (will fail at the gh release step since the release doesn't exist yet; that's expected)**

```bash
cd ../community-brain-distribution
./download-corpus.sh || echo "expected failure: no real release yet (rc=$?)"
```

Expected: fails at the `gh release download` step with "release not found" or similar. The pre-flight checks (sha tool detection, current-version short-circuit attempt) should pass.

- [ ] **Step 3: Commit**

```bash
git add download-corpus.sh
git commit -m "feat: add download-corpus.sh with idempotency + rollback rotation

Constants CORPUS_VERSION + EXPECTED_SHA256 + RELEASE_REPO are bumped
by the operator on each corpus release. Re-running with the same
version short-circuits to a no-op (per spec §5.5)."
```

---

### Task 15: Fixture corpus for CI

**Files:**
- Create: `../community-brain-distribution/tests/fixtures/corpus/lancedb/nomic-v1/...`
- Create: `../community-brain-distribution/tests/fixtures/corpus/corpus-manifest.json`
- Create: `../community-brain-distribution/tests/fixtures/build-fixture.sh`

- [ ] **Step 1: Create build-fixture.sh that constructs the tiny fixture**

Create `../community-brain-distribution/tests/fixtures/build-fixture.sh`:

```bash
#!/usr/bin/env bash
# build-fixture.sh — construct a tiny clean-v3 LanceDB for CI fixtures.
#
# Run this once during initial setup or when fixture format needs to change.
# Output: tests/fixtures/corpus/lancedb/nomic-v1/chunks.lance/...
#         tests/fixtures/corpus/corpus-manifest.json

set -euo pipefail

FIXTURE_ROOT="$(cd "$(dirname "$0")" && pwd)"
CORPUS="${FIXTURE_ROOT}/corpus"
PYTHON="${COMMUNITY_BRAIN_VENV:-../../../community-brain/.venv}/bin/python"

if [[ ! -x "$PYTHON" ]]; then
    echo "ERROR: python venv not found. Set COMMUNITY_BRAIN_VENV or run from a place where" >&2
    echo "  ../../../community-brain/.venv exists." >&2
    exit 2
fi

rm -rf "$CORPUS"
mkdir -p "$CORPUS/lancedb/nomic-v1"

"$PYTHON" - <<PYEOF
import json, pathlib
import lancedb
import pyarrow as pa

DB_PATH = "${CORPUS}/lancedb/nomic-v1"
db = lancedb.connect(DB_PATH)

# Minimal v3 schema subset (must include bm25_text for FTS index).
# For CI smoke install, we don't need the full 37-field schema —
# the verify-install.sh check is /sessions count + /health metadata,
# not real retrieval quality.
schema = pa.schema([
    ("session_id", pa.string()),
    ("chunk_id", pa.string()),
    ("bm25_text", pa.string()),
    ("vector", pa.list_(pa.float32(), 768)),
])
table = db.create_table("chunks", schema=schema, mode="overwrite")

# Canned rows with canned vectors (deterministic, all-zeros vectors for
# CI; real retrieval quality is not tested here).
def zero_vec(): return [0.0] * 768
rows = [
    {"session_id": "fixture-001", "chunk_id": "fixture-001:c0",
     "bm25_text": "hello fixture corpus", "vector": zero_vec()},
    {"session_id": "fixture-001", "chunk_id": "fixture-001:c1",
     "bm25_text": "second chunk of fixture-001", "vector": zero_vec()},
    {"session_id": "fixture-002", "chunk_id": "fixture-002:c0",
     "bm25_text": "another fixture session", "vector": zero_vec()},
]
table.add(rows)
table.create_fts_index("bm25_text", replace=True)

# Manifest.
manifest = {
    "corpus_version": "v0.0.0-fixture",
    "schema_version": "1.1",
    "embedding_model": "nomic-embed-text",
    "session_count": 2,
    "chunk_count": 3,
    "generation_timestamp_utc": "2026-05-10T00:00:00Z",
}
pathlib.Path("${CORPUS}/corpus-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print("fixture built at ${CORPUS}")
PYEOF
```

Make it executable:

```bash
chmod +x tests/fixtures/build-fixture.sh
```

- [ ] **Step 2: Build the fixture once**

```bash
cd ../community-brain-distribution/tests/fixtures
./build-fixture.sh
```

Expected: `fixture built at ...`. The `corpus/lancedb/nomic-v1/chunks.lance/` directory now exists with data + FTS index. `corpus/corpus-manifest.json` reports 2 sessions, 3 chunks.

- [ ] **Step 3: Commit the fixture (it's binary but tiny)**

```bash
cd ../community-brain-distribution
git add tests/fixtures/build-fixture.sh tests/fixtures/corpus/
git commit -m "feat: add fixture corpus for CI smoke install

Tiny clean-v3 LanceDB (2 sessions, 3 chunks, 768-dim zero vectors)
that the verify-on-pr.yml workflow uses in place of the real corpus
blob. Vectors are zeros — retrieval quality is not tested in CI;
only route shape, count consistency, and version metadata.

build-fixture.sh is checked in so the fixture can be regenerated
when the schema evolves."
```

---

### Task 16: Mock Ollama for CI

**Files:**
- Create: `../community-brain-distribution/tests/fixtures/mock-ollama/Dockerfile`
- Create: `../community-brain-distribution/tests/fixtures/mock-ollama/server.py`
- Create: `../community-brain-distribution/tests/fixtures/mock-ollama/requirements.txt`

- [ ] **Step 1: Create the mock server**

Create `../community-brain-distribution/tests/fixtures/mock-ollama/server.py`:

```python
"""Mock Ollama for CI: serves /api/tags and /api/embeddings with canned data.

Vector shape matches nomic-embed-text (768-dim). Returns all-zeros
vectors — retrieval quality is not tested in CI; only route shape,
count consistency, and version metadata.

The fixture corpus (tests/fixtures/corpus/) is also all-zeros, so query-
time embeddings vacuously "match" and /query returns deterministic results.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

EMBED_DIM = 768
ZERO = [0.0] * EMBED_DIM


@app.get("/api/tags")
def tags():
    """Mimic `ollama list` shape."""
    return {
        "models": [
            {"name": "nomic-embed-text:latest", "model": "nomic-embed-text:latest"},
        ]
    }


class EmbedRequest(BaseModel):
    model: str
    prompt: str | None = None
    input: str | list[str] | None = None


@app.post("/api/embeddings")
def embeddings(req: EmbedRequest):
    """Ollama-compatible embeddings endpoint. Returns zeros."""
    return {"embedding": ZERO}


@app.post("/api/embed")
def embed(req: EmbedRequest):
    """Newer Ollama embed endpoint. Returns zeros."""
    if isinstance(req.input, list):
        return {"embeddings": [ZERO for _ in req.input]}
    return {"embeddings": [ZERO]}
```

Create `../community-brain-distribution/tests/fixtures/mock-ollama/requirements.txt`:

```
fastapi==0.115.0
uvicorn==0.32.0
pydantic==2.9.2
```

Create `../community-brain-distribution/tests/fixtures/mock-ollama/Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py .
EXPOSE 11434
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "11434"]
```

- [ ] **Step 2: Local smoke test the mock**

```bash
cd ../community-brain-distribution/tests/fixtures/mock-ollama
docker build -t mock-ollama:test .
docker run --rm -d -p 11434:11434 --name mock-ollama-test mock-ollama:test
sleep 2
curl -s http://127.0.0.1:11434/api/tags | jq .
curl -s -X POST http://127.0.0.1:11434/api/embeddings \
    -H 'Content-Type: application/json' \
    -d '{"model":"nomic-embed-text","prompt":"hello"}' | jq '.embedding | length'
docker stop mock-ollama-test
```

Expected: tags returns the nomic model; embeddings returns a 768-element zero array.

- [ ] **Step 3: Commit**

```bash
cd ../community-brain-distribution
git add tests/fixtures/mock-ollama/
git commit -m "feat: add mock-ollama for CI

FastAPI shim serving /api/tags + /api/embeddings with canned zero-vector
responses. Lets verify-on-pr.yml run the stack on ubuntu-latest without
a real Ollama install."
```

---

### Task 17: `INSTALL.md`

**Files:**
- Create: `../community-brain-distribution/INSTALL.md`

- [ ] **Step 1: Create INSTALL.md**

Create `../community-brain-distribution/INSTALL.md`:

```markdown
# Community Brain — Install Guide

A retrieval interface over a curated coaching-call corpus. Search the calls you were on; ask questions and get cited answers.

**If you use an AI coding assistant** (Claude Code, Codex, Cursor, Gemini CLI, Aider, etc.):
> Open this file in that assistant and say: "Follow this install guide on my machine. Run `./verify-install.sh` between major steps. If a step fails verification, fix it before continuing. Ask me for confirmation before any installs that need sudo or before pasting anything I would need to authorize."

The rest of this doc is written so an agent can drive it. Humans follow the same instructions by hand.

---

## 0. Before You Start

### Hardware
- **Minimum:** 8 GB RAM, ~5 GB free disk.
- **For local-LLM mode (Option A in Step 5):** 24+ GB unified memory (Apple Silicon) or a beefy GPU (Linux). Cloud mode skips this requirement.

### Software prerequisites (all platforms)
- `git` — any modern version
- `docker` + `docker compose` v2 — Docker Desktop on Mac/Windows, `docker-ce` on Linux
- `ollama` — native installer on Mac/Linux; inside Ubuntu WSL on Windows
- `curl`, `tar`, `jq`, `openssl` — preinstalled on macOS/Linux; `apt install jq` if missing on WSL/Ubuntu
- `gh` (GitHub CLI) — used by `download-corpus.sh`
- SHA-256 tool — `sha256sum` (Linux/WSL) or `shasum -a 256` (macOS); scripts auto-detect

### Windows
Install Docker Desktop with WSL2 backend + Ubuntu, and run every command in this guide from an **Ubuntu WSL2 shell**, not PowerShell or Git Bash. The distribution ships Bash-shaped tooling; native Windows is unsupported in v1.

### Pick your inference mode
- **Option A — Local LLM** (Ollama with gpt-oss:20b). Free to run, requires 24+ GB unified memory.
- **Option B — Cloud LLM** (OpenAI, OpenRouter, Anthropic, Gemini, etc.). You pay per query, no hardware requirement beyond the embedding model.

You can switch between modes later by editing `.env` and restarting the stack.

---

## 1. Install Docker + Ollama

### macOS
```bash
# Docker Desktop or OrbStack: download from their websites.
# Then install Ollama:
brew install --cask ollama
# Or: download from https://ollama.com/download
```

Verify:
```bash
docker --version
docker compose version
ollama --version
```

### Linux
```bash
# Docker:
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# Log out and back in for group change to take effect.

# Ollama:
curl -fsSL https://ollama.com/install.sh | sh
```

### Windows (inside Ubuntu WSL2)
```bash
# Docker Desktop is installed on Windows side. Ollama goes inside WSL:
curl -fsSL https://ollama.com/install.sh | sh
```

Verify (in WSL Ubuntu shell):
```bash
docker --version
docker compose version
ollama --version
```

**Verify:** `./verify-install.sh --step 1` (after Step 4 makes the script available).

---

## 2. Pull the embedding model

```bash
ollama pull nomic-embed-text
```

This is ~250 MB and runs CPU-only. Required regardless of which inference mode you pick — query-time embeddings must match the corpus's pre-built vectors.

Verify:
```bash
ollama list | grep nomic-embed-text
```

---

## 3. (Optional, local-LLM mode only) Pull the chat model

Skip this step if you're using Option B (cloud LLM) in Step 5.

```bash
ollama pull gpt-oss:20b
```

This is ~12 GB. Requires the hardware noted in Step 0.

Verify:
```bash
ollama list | grep gpt-oss
```

---

## 4. Clone the distribution repo

```bash
git clone https://github.com/REPLACE_OPERATOR_HERE/community-brain-distribution
cd community-brain-distribution
./verify-install.sh --step 4
```

---

## 5. Configure your .env

```bash
cp .env.example .env
```

Open `.env` in your editor. Set the required values:

- `WEBUI_SECRET_KEY`: generate with `openssl rand -hex 32`, paste the output here.
- `OLLAMA_BASE_URL`: leave at `http://host.docker.internal:11434` unless you have a custom Ollama setup.

Then **uncomment exactly one inference block**:

- **Option A — Local Ollama chat**: uncomment the `INFERENCE_LOCAL_MODEL=gpt-oss:20b` line.
- **Option B — Cloud chat**: uncomment all three `OPENAI_API_*` and `INFERENCE_CLOUD_MODEL` lines, and fill in your API base URL, key, and model name.

For OpenRouter (which proxies Anthropic, Gemini, OpenAI, etc.):
- `OPENAI_API_BASE_URL=https://openrouter.ai/api/v1`
- `OPENAI_API_KEY=sk-or-v1-...` (get one at https://openrouter.ai/keys)
- `INFERENCE_CLOUD_MODEL=anthropic/claude-sonnet-4.6` (or another model from https://openrouter.ai/models)

Verify:
```bash
./verify-install.sh --step 5
```

---

## 6. Download the corpus

```bash
./download-corpus.sh
```

This fetches ~600-900 MB and extracts to `./corpus/`. On second run with the same version, it short-circuits to a no-op.

If you ever need to roll back, `./corpus.previous/` keeps the immediately-prior version.

Verify:
```bash
./verify-install.sh --step 6
```

---

## 7. Start the stack

```bash
docker compose up -d
```

This pulls the pinned `retrieval-server` and `open-webui` images (first run only; ~500 MB total) and starts both containers.

Verify:
```bash
./verify-install.sh --step 7
```

This checks:
- Both containers running
- Ports bound to `127.0.0.1` (not LAN-exposed)
- `/health` returns 200 with `distribution_mode: true`
- `/health.schema_version` matches `corpus-manifest.json`
- `/health.embedding_model` matches `corpus-manifest.json`

---

## 8. Configure Open WebUI

Open `http://127.0.0.1:3000` in your browser. First user becomes admin.

### 8a. Verify the inference connection (already auto-configured from .env)

Settings → Connections.

- **Local mode (Option A):** the Ollama section should show your Ollama endpoint populated from `OLLAMA_BASE_URL`. Confirm the connection reports as available.
- **Cloud mode (Option B):** the OpenAI section should show your endpoint and a redacted API key populated from `OPENAI_API_BASE_URL` and `OPENAI_API_KEY`. Confirm the connection reports as available.

**You do NOT paste credentials in the GUI.** They came in via `.env`. If a connection is missing here, return to Step 5 and verify the `.env` block for your chosen mode is uncommented and filled in.

### 8b. Create the custom "community-brain" model

Workspace → Models → New Model.

- **Name:** `community-brain`
- **Base model:** `gpt-oss:20b` (local mode) or your cloud model (e.g. `anthropic/claude-sonnet-4.6`)
- **System prompt:** open `inference-guidelines.md` (in this directory) and paste the entire file content into the system-prompt field.
- Save.

### 8c. Upload + enable the filter

Workspace → Functions → Import Function.

- Select `community_brain_filter.py` from this directory.
- After upload, find the filter in the list and:
  - Toggle it ON globally, OR
  - Attach it to the `community-brain` model from Step 8b.

---

## 9. End-to-end validation

### 9a. Server-side checks (deterministic)

```bash
curl -s http://127.0.0.1:8999/sessions | jq '.sessions | length'
```
Expected: matches `session_count` in `./corpus/corpus-manifest.json`.

```bash
curl -s http://127.0.0.1:8999/health | jq '{schema_version, embedding_model}'
jq '{schema_version, embedding_model}' ./corpus/corpus-manifest.json
```
Expected: both fields match between server and manifest.

### 9b. Open WebUI retrieval smoke test (qualitative)

In OWUI chat, select the `community-brain` model. Send a content question you know the corpus can answer, e.g.:

> Summarize a recent discussion about pricing in the coaching calls.

Expected: the response contains a `[corpus summary: of the N retrieved chunks, ...]` line above the answer (rendered by the filter), and citations include session IDs that match values from `/sessions`. Click a citation; it should show a quote that resolves to actual corpus content.

If the response doesn't include the `[corpus summary: ...]` line: the filter is not attached. Re-check Step 8c.

---

## Troubleshooting

See [`docs/troubleshooting.md`](./docs/troubleshooting.md).

---

## Updating to a new release

```bash
git pull
./verify-install.sh --check-env-drift   # warn if new keys appear in .env.example
./download-corpus.sh                    # no-op if CORPUS_VERSION unchanged
docker compose pull                     # grab new image SHAs from compose.yml
docker compose up -d                    # restart with new images
./verify-install.sh --post-install      # confirm green
```
```

- [ ] **Step 2: Commit**

```bash
cd ../community-brain-distribution
git add INSTALL.md
git commit -m "feat: add INSTALL.md runbook (agent-and-human friendly)"
```

---

### Task 18: README.md, docs/tour.md, docs/troubleshooting.md

**Files:**
- Create: `../community-brain-distribution/README.md`
- Create: `../community-brain-distribution/docs/tour.md`
- Create: `../community-brain-distribution/docs/troubleshooting.md`

- [ ] **Step 1: Create README.md**

Create `../community-brain-distribution/README.md`:

```markdown
# community-brain-distribution

A self-host Tier B distribution of the Community Brain retrieval system: search and ask questions over a curated coaching-call corpus on your own machine.

## What this is

- A Docker Compose stack: a retrieval-server (LanceDB-backed search API) + Open WebUI (chat UI).
- A pre-built corpus blob downloaded from this repo's GitHub Releases.
- A filter for Open WebUI that injects retrieval results into your chat.

Recipients run everything locally. No data leaves your machine.

## Quick start

1. Read [`INSTALL.md`](./INSTALL.md).
2. If you use an AI coding assistant (Claude Code, Codex, Cursor, etc.), point it at `INSTALL.md` and say "follow this on my machine."

## Operator

This repo is the cooked-product face of [RecapFlow-automation](https://github.com/REPLACE_OPERATOR_HERE/RecapFlow-automation). Source code, Python package, and release tooling live there.

## License

[TBD by operator — replace this section with chosen license terms.]
```

- [ ] **Step 2: Create docs/tour.md**

Create `../community-brain-distribution/docs/tour.md`:

```markdown
# Tour

A quick orientation to what you just installed.

## The stack

```
┌──────────────────────────────────────────────────────┐
│  Open WebUI  (http://127.0.0.1:3000)                 │
│    - Chat interface                                  │
│    - The community-brain custom model                │
│    - The community-brain filter (injects retrieval)  │
│         │                                            │
│         ▼ /query                                     │
│  retrieval-server (http://127.0.0.1:8999)            │
│    - FastAPI, distribution mode (read-only)          │
│    - Hybrid retrieval (vector + BM25)                │
│    - LanceDB at ./corpus/lancedb/                    │
│         │                                            │
│         ▼ embedding lookup                           │
│  Ollama (http://localhost:11434)                     │
│    - nomic-embed-text (mandatory, ~250 MB)           │
│    - gpt-oss:20b (optional, local-LLM mode)          │
└──────────────────────────────────────────────────────┘
```

## What you can ask

The corpus contains coaching-call transcripts plus structured artifacts (extracted signal, community posts). Try questions like:

- "Find a quote from <speaker name> about <topic>"
- "What did we discuss about <topic> in <month>?"
- "Summarize recent discussions of <theme>"
- "Show me unresolved questions from <speaker>"

The filter injects retrieved chunks above your question and tells the LLM how to cite them. The trust contract (in the system prompt) instructs the LLM to:

- Quote only from `ground_truth` content (verbatim transcript text)
- Treat `derived_metadata` (LLM-extracted flags like `has_question`, `references_prior`) as provisional and re-derive as needed
- Always include session-ID citations

## Where things live

- `docker-compose.yml` — stack definition (image SHAs pinned)
- `.env.example` / `.env` — your local config (don't commit `.env`)
- `corpus/` — the LanceDB blob (don't commit)
- `community_brain_filter.py` — uploaded to Open WebUI in Step 8
- `inference-guidelines.md` — system prompt for the custom model
- `verify-install.sh` — run anytime to check stack health
- `download-corpus.sh` — fetch / update the corpus blob

## Updating

See the bottom of `INSTALL.md`.

## Loom walkthrough

[Placeholder for operator-recorded video; link to be added after first release.]
```

- [ ] **Step 3: Create docs/troubleshooting.md**

Create `../community-brain-distribution/docs/troubleshooting.md`:

```markdown
# Troubleshooting

Issues are grouped by which install step they typically surface in.

## Step 1: Docker / Ollama install

**"docker: command not found"**
Install Docker Desktop (Mac/Win) or `curl -fsSL https://get.docker.com | sh` (Linux). Add yourself to the `docker` group on Linux and log out/in.

**"docker compose: 'compose' is not a docker command"**
You have legacy `docker-compose` v1. Install Docker Desktop or the v2 plugin: `sudo apt install docker-compose-plugin`.

**Ollama installed but `ollama list` returns nothing**
Ollama service isn't running. macOS: open the Ollama app. Linux: `ollama serve` in a separate terminal. Then re-run `ollama pull nomic-embed-text`.

## Step 6: Corpus download

**"gh: command not found"**
Install GitHub CLI: `brew install gh` (Mac), `sudo apt install gh` (Linux/WSL).

**"release not found"**
The pinned `CORPUS_VERSION` in `download-corpus.sh` doesn't match a published release. Pull the latest distribution-repo commits: `git pull`.

**SHA-256 mismatch**
The downloaded tarball doesn't match the expected hash. Re-run `./download-corpus.sh` — likely a transient download corruption. If it persists, file an issue.

## Step 7: Stack startup

**"WEBUI_SECRET_KEY must be set in .env"**
You missed Step 5. `openssl rand -hex 32`, paste into `.env`.

**retrieval-server exits with "CorpusInvalidError"**
The corpus is missing the FTS index. Re-run `./download-corpus.sh`. If it still fails, file an issue with the docker logs output: `docker compose logs retrieval-server`.

**retrieval-server starts but `/health` is unreachable**
Check ports aren't taken: `lsof -iTCP:8999 -sTCP:LISTEN`. If a stale process holds the port, kill it.

**`/health.embedding_model` doesn't match manifest**
Your `.env` has a `COMMUNITY_BRAIN_EMBED_MODEL` override that disagrees with the corpus's embedding model. Comment out the override (or set it to match the manifest's value).

## Step 8: Open WebUI configuration

**The community-brain filter doesn't appear after upload**
Refresh the page. Then re-check Workspace → Functions; the filter should be in the list with a toggle. Some OWUI versions cache aggressively.

**Filter is uploaded but responses don't show `[corpus summary: ...]` header**
The filter isn't attached to the active model. Either toggle it on globally (Workspace → Functions → toggle the filter) or attach it explicitly to the community-brain model (Workspace → Models → community-brain → Functions tab).

**Inference connection missing in Settings → Connections**
Your `.env` block for the chosen mode isn't uncommented. Re-edit `.env`, then `docker compose restart open-webui`.

## Update path

**Git pull conflicts on `docker-compose.yml`**
You edited `docker-compose.yml` locally — possibly to expose a port to LAN, change OWUI version, etc. The release pipeline assumes the file is unmodified. Resolve by stashing your changes, pulling, and re-applying. If you want a permanent customization, document it in your own fork or in a side note.
```

- [ ] **Step 4: Commit**

```bash
cd ../community-brain-distribution
git add README.md docs/
git commit -m "feat: add README, docs/tour, docs/troubleshooting"
```

---

### Task 19: Stub `community_brain_filter.py` and `inference-guidelines.md`

**Files:**
- Create: `../community-brain-distribution/community_brain_filter.py` (placeholder; auto-synced post-merge)
- Create: `../community-brain-distribution/inference-guidelines.md` (placeholder; auto-synced post-merge)

- [ ] **Step 1: Copy the current operator-repo versions in (will be auto-synced going forward)**

```bash
cd ../community-brain-distribution
cp ../RecapFlow-automation/community-brain/src/community_brain/openwebui/community_brain_filter.py .
cp ../RecapFlow-automation/docs/inference-guidelines.md .
```

(The exact path to the operator repo's parent dir might vary; adjust if it lives elsewhere.)

- [ ] **Step 2: Commit**

```bash
git add community_brain_filter.py inference-guidelines.md
git commit -m "feat: seed filter + inference-guidelines from operator repo

These are auto-synced by sync-curated-files.yml going forward. Initial
commit is a hand-copy."
```

---

### Task 20: `.github/workflows/verify-on-pr.yml`

**Files:**
- Create: `../community-brain-distribution/.github/workflows/verify-on-pr.yml`

- [ ] **Step 1: Create the CI workflow**

Create `../community-brain-distribution/.github/workflows/verify-on-pr.yml`:

```yaml
name: Verify install on PR

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  fixture-smoke-install:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install jq + curl + tar
        run: sudo apt-get update && sudo apt-get install -y jq curl tar

      - name: Build mock-ollama image
        run: |
          docker build -t mock-ollama:ci tests/fixtures/mock-ollama/

      - name: Start mock-ollama
        run: |
          docker run -d --name mock-ollama --network host mock-ollama:ci
          sleep 3
          curl -sf http://127.0.0.1:11434/api/tags | jq .

      - name: Stage fixture corpus as ./corpus
        run: |
          cp -r tests/fixtures/corpus ./corpus

      - name: Write a CI .env
        run: |
          cat > .env <<EOF
          OLLAMA_BASE_URL=http://127.0.0.1:11434
          WEBUI_SECRET_KEY=$(openssl rand -hex 32)
          INFERENCE_LOCAL_MODEL=gpt-oss:20b
          EOF

      - name: Patch docker-compose for CI
        # Replace placeholders / use host networking for the mock-ollama
        # connection, and pull the latest retrieval-server image (CI doesn't
        # have access to a SHA-pinned image yet on first run).
        run: |
          # For CI, replace the PLACEHOLDER SHA with :latest tag. Real
          # releases use SHA-pinning; CI just needs SOMETHING to pull.
          sed -i 's|@sha256:PLACEHOLDER_BUMPED_BY_CI|:latest|g' docker-compose.yml
          sed -i 's|@sha256:PLACEHOLDER_OWUI_SHA|:main|g' docker-compose.yml
          # Replace REPLACE_OPERATOR_HERE with the github.repository_owner.
          sed -i "s|REPLACE_OPERATOR_HERE|${GITHUB_REPOSITORY_OWNER}|g" docker-compose.yml
          # Use host networking so retrieval-server can reach mock-ollama on 127.0.0.1.
          # (docker compose port mapping wouldn't be visible to the container otherwise.)
          # Quick override via env:
          echo "OLLAMA_BASE_URL=http://127.0.0.1:11434" >> .env

      - name: docker compose up
        run: |
          docker compose pull || true   # tolerate :latest-not-yet-published
          docker compose up -d
          sleep 5
          docker compose ps

      - name: Run verify-install.sh --post-install
        run: |
          chmod +x verify-install.sh
          ./verify-install.sh --post-install

      - name: Verify route shape (distribution mode)
        run: |
          # /ingest should 404 (route removed in distribution mode)
          status=$(curl -s -o /dev/null -w '%{http_code}' \
              -X POST http://127.0.0.1:8999/ingest -d '{}')
          if [[ "$status" != "404" ]]; then
              echo "ERROR: /ingest returned $status, expected 404"
              exit 1
          fi
          # /reindex should 404
          status=$(curl -s -o /dev/null -w '%{http_code}' \
              -X POST http://127.0.0.1:8999/reindex -d '{}')
          if [[ "$status" != "404" ]]; then
              echo "ERROR: /reindex returned $status, expected 404"
              exit 1
          fi
          echo "OK: write routes are absent"

      - name: Dump logs on failure
        if: failure()
        run: |
          docker compose logs retrieval-server || true
          docker compose logs open-webui || true
          docker logs mock-ollama || true

      - name: Cleanup
        if: always()
        run: |
          docker compose down --volumes || true
          docker stop mock-ollama || true
          docker rm mock-ollama || true
```

- [ ] **Step 2: Commit**

```bash
cd ../community-brain-distribution
git add .github/workflows/verify-on-pr.yml
git commit -m "feat: add verify-on-pr.yml CI

Fixture-based smoke install: builds mock-ollama, stages fixture corpus,
boots stack, runs verify-install.sh --post-install, asserts /ingest
and /reindex return 404. Catches doc-drift, image-pin regressions,
schema-version mismatches, route-shape regressions."
```

---

### Milestone 3 Checkpoint

- [ ] **Push the distribution repo to GitHub:**

Manual operator step:
1. Create the public repo `community-brain-distribution` on GitHub (operator's account or org).
2. `cd ../community-brain-distribution && git remote add origin <url> && git push -u origin main`.

- [ ] **Confirm CI runs:**

Open a PR with a trivial change (e.g., README typo) to trigger `verify-on-pr.yml`. Expected: smoke install succeeds, route-shape checks pass, all-green.

If the workflow fails, inspect the logs. Common issues:
- The retrieval-server image isn't published yet (CI is using `:latest` which doesn't exist). Tag and push the operator-repo's first `tier-b-retrieval-v0.0.0-rc1` to publish a real image first.
- OWUI's `:main` tag changed shape in a way that breaks alembic. Pin a known-good SHA in the CI override step.

- [ ] **Local smoke install from the distribution repo (manual):**

```bash
cd ../community-brain-distribution
cp -r tests/fixtures/corpus ./corpus    # fake the download
echo "OLLAMA_BASE_URL=http://host.docker.internal:11434" > .env
echo "WEBUI_SECRET_KEY=$(openssl rand -hex 32)" >> .env
echo "INFERENCE_LOCAL_MODEL=gpt-oss:20b" >> .env
docker compose up -d
sleep 5
./verify-install.sh --post-install
docker compose down -v
rm -rf ./corpus .env
```

Expected: all checks pass.

Milestone 3 done. The distribution repo exists, CI passes, the fixture-based install works end-to-end.

---

## Milestone 4: v1.0.0 release

Outcome: the first real, public Tier B release. Image is built and pushed; corpus is snapshotted, compacted, tarballed, and published; both repos are tagged; recipients can install.

### Task 21: Pre-flight rehearsal on a clean Mac VM

- [ ] **Step 1: Provision a clean Mac VM (or fresh user account)**

Operator decision: use a UTM/Parallels VM, or `sudo dscl . -create /Users/cb-test ...` to create a fresh user account. The point is: no Docker, no Ollama, no pre-existing state.

- [ ] **Step 2: Walk through INSTALL.md literally**

Open `INSTALL.md` in the VM. Follow every step. No shortcuts, no operator memory. Time it; record any friction.

- [ ] **Step 3: Run `verify-install.sh --post-install`**

Expected: all green.

- [ ] **Step 4: Run the §6.2 Step 9 validation queries**

9a (server-side): `/sessions` count + `/health` metadata match manifest.
9b (OWUI retrieval test): the canonical test query returns a response with `[corpus summary: ...]` and citations that resolve to corpus content.

- [ ] **Step 5: Record any doc-fixes needed**

If any step was unclear or wrong, fix `INSTALL.md` / `docs/troubleshooting.md` and re-run from Step 2. Loop until clean.

- [ ] **Step 6: Commit any doc fixes**

```bash
cd ../community-brain-distribution
git add INSTALL.md docs/troubleshooting.md
git commit -m "docs: fixes from pre-flight rehearsal on clean Mac VM"
```

---

### Task 22: Cut the corpus release

- [ ] **Step 1: Run release-corpus.sh against the live VM**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
./scripts/release-corpus.sh v1.0.0
```

Expected: artifacts in `/tmp/corpus-release/`:
- `corpus-v1.0.0.tar.gz` (~600-900 MB)
- `sha256sum.txt`
- `corpus-manifest.json`

- [ ] **Step 2: Publish the corpus Release**

```bash
SHA=$(awk '{print $1}' /tmp/corpus-release/sha256sum.txt)
gh release create v1.0.0 \
    /tmp/corpus-release/corpus-v1.0.0.tar.gz \
    /tmp/corpus-release/sha256sum.txt \
    /tmp/corpus-release/corpus-manifest.json \
    --repo REPLACE_OPERATOR_HERE/community-brain-distribution \
    --title "Corpus v1.0.0" \
    --notes "First public corpus release. SHA-256: ${SHA}"
```

- [ ] **Step 3: Open PR bumping CORPUS_VERSION + EXPECTED_SHA256 in download-corpus.sh**

```bash
cd ../community-brain-distribution
git checkout -b release-v1.0.0
sed -i "s/^CORPUS_VERSION=.*/CORPUS_VERSION=\"v1.0.0\"/" download-corpus.sh
sed -i "s/^EXPECTED_SHA256=.*/EXPECTED_SHA256=\"${SHA}\"/" download-corpus.sh
git add download-corpus.sh
git commit -m "chore: bump corpus to v1.0.0"
git push -u origin release-v1.0.0
gh pr create --title "Release v1.0.0" \
    --body "First public Tier B release. CI must pass before merge."
```

- [ ] **Step 4: Confirm CI passes, merge, tag**

```bash
# After CI green and merge:
git checkout main && git pull
git tag tier-b-v1.0.0
git push origin tier-b-v1.0.0
```

---

### Task 23: Cut the image release (operator repo)

- [ ] **Step 1: Tag operator repo to trigger image build**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
git tag tier-b-retrieval-v1.0.0
git push origin tier-b-retrieval-v1.0.0
```

Expected: `.github/workflows/build-retrieval-image.yml` fires. It builds the image, pushes to ghcr.io, and opens a PR in `community-brain-distribution`.

- [ ] **Step 2: Confirm the PR opened in distribution repo**

Check `community-brain-distribution`'s open PRs. Expected: a PR titled "Bump retrieval-server to 1.0.0" with the new SHA.

- [ ] **Step 3: Merge the image-bump PR**

CI on the PR runs verify-on-pr.yml against the new image + the fixture corpus. If green, merge.

---

### Task 24: Announce + verify recipient install

- [ ] **Step 1: Post the release announcement in Skool**

Manual operator step: post in the Skool community with:
- Link to `community-brain-distribution` README
- Link to v1.0.0 release
- Note on which inference modes are supported (Ollama + cloud)
- Note on hardware requirements
- Link to `INSTALL.md`

- [ ] **Step 2: Watch for first install reports**

If something breaks for a recipient, treat it as a doc/scripts bug — open an issue in the distribution repo, fix, ship a patch release.

- [ ] **Step 3: Tag this work complete**

Update `CLAUDE.md` in the operator repo to reflect Tier B is live:

```diff
- **What's still open — one operational track:**
- - **Track B:** Plan C — full backfill across remaining ~57 of 65 historical sessions...
+ **What's done as of 2026-05-10:** Plan C complete (69 sessions in LanceDB), Tier B v1.0.0 shipped.
+ **What's still open:** Tier A (community-full) — operator-only ingestion stack as a separable distribution. Separate spec needed.
```

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
git add CLAUDE.md
git commit -m "docs(claude.md): Tier B v1.0.0 shipped; Tier A is next open thread"
git push
```

---

### Milestone 4 Checkpoint

- [ ] **Recipient install works end-to-end:** at least one community member (or you on a clean VM) has installed and validated against v1.0.0.
- [ ] **Both repos tagged:** `tier-b-retrieval-v1.0.0` in operator repo, `tier-b-v1.0.0` in distribution repo.
- [ ] **Corpus blob is downloadable:** `gh release view v1.0.0 --repo <owner>/community-brain-distribution` shows the three assets.
- [ ] **Announcement posted in Skool.**

Tier B is live.

---

## Out of scope (deferred to v1.1+ or separate plans)

Per spec §13:
- `configure-open-webui.sh` — programmatic OWUI setup via REST API
- `check-for-updates.sh` — recipient-pull update notification
- Personal-notes side-table
- Loom walkthrough video
- Pre-commit hook to block .env commits
- Cloudflare R2 hosting (v2; only if corpus crosses 1.5 GB compacted)
- Mobile-friendly UI
- Multi-corpus support
- **Tier A (community-full)** — separate spec
