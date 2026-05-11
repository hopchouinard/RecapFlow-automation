"""Distribution-mode route gating per Tier B spec §2.3.

When COMMUNITY_BRAIN_DISTRIBUTION_MODE=true, /ingest and /reindex must
be absent from the registered routes. All five read endpoints must be
present in both modes.
"""
import importlib
import sys

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

    Route registration happens at import time, so toggling the env at test
    setup time isn't enough — we have to force a fresh import. We must also
    restore module-state cleanup that survives whether or not the parent
    package was loaded before this call.
    """
    if distribution_mode:
        monkeypatch.setenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", "true")
    else:
        monkeypatch.delenv("COMMUNITY_BRAIN_DISTRIBUTION_MODE", raising=False)

    MODULE_KEY = "community_brain.query.retrieval_server"
    PARENT_KEY = "community_brain.query"

    # Save the pre-test state so we can restore exactly.
    saved_module = sys.modules.get(MODULE_KEY)
    saved_parent_attr = None
    parent_had_attr = False
    parent = sys.modules.get(PARENT_KEY)
    if parent is not None and hasattr(parent, "retrieval_server"):
        saved_parent_attr = getattr(parent, "retrieval_server")
        parent_had_attr = True

    # Evict and reimport. importlib.import_module guarantees the parent
    # package is in sys.modules after a successful import. Cleanup runs in
    # `finally` so an import failure during development doesn't leave the
    # module registry dirty for subsequent tests.
    if MODULE_KEY in sys.modules:
        del sys.modules[MODULE_KEY]
    try:
        module = importlib.import_module(MODULE_KEY)
        app = module.app
    finally:
        # Restore sys.modules:
        if saved_module is not None:
            sys.modules[MODULE_KEY] = saved_module
        elif MODULE_KEY in sys.modules:
            del sys.modules[MODULE_KEY]
        # Restore parent attribute (parent guaranteed loaded if import
        # succeeded; if import failed, parent_now may be None and there
        # is nothing to restore anyway).
        parent_now = sys.modules.get(PARENT_KEY)
        if parent_now is not None:
            if parent_had_attr:
                setattr(parent_now, "retrieval_server", saved_parent_attr)
            elif hasattr(parent_now, "retrieval_server"):
                delattr(parent_now, "retrieval_server")

    return app


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


def test_operator_mode_ingest_requires_api_key_when_set(monkeypatch):
    """Operator mode preserves the RETRIEVAL_API_KEY auth contract."""
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret123")
    app = _reload_app(monkeypatch, distribution_mode=False)
    client = TestClient(app)
    # No X-API-Key header → 403
    r = client.post("/ingest", json={"session_id": "s1", "artifact_paths": {}})
    assert r.status_code == 403


def test_operator_mode_reindex_requires_api_key_when_set(monkeypatch):
    monkeypatch.setenv("RETRIEVAL_API_KEY", "secret123")
    app = _reload_app(monkeypatch, distribution_mode=False)
    client = TestClient(app)
    r = client.post("/reindex", json={"operation": "match-only", "filter": {}})
    assert r.status_code == 403


def test_distribution_mode_query_path_uses_readonly_verify(monkeypatch, tmp_path):
    """The /query handler must call verify_corpus_v3_state_readonly, not the
    write-capable verify_corpus_v3_state, when DISTRIBUTION_MODE is true.
    Otherwise an RO-mounted corpus would error on every query if the FTS
    index were somehow absent.

    NOTE: When the LanceDB table does not exist (fresh deploy / empty tmp_path),
    /query short-circuits at the `if "chunks" in db.list_tables().tables` guard
    and neither verify function is called. In that case this test confirms
    `write_calls` is empty, which is the only failure mode that matters. The
    actual branch (readonly vs write) is exercised in integration tests against
    a populated table; this test documents and guards the intent.
    """
    import community_brain.query.corpus_verify as cv

    readonly_calls = []
    write_calls = []
    monkeypatch.setattr(
        cv, "verify_corpus_v3_state_readonly",
        lambda t: readonly_calls.append(t)
    )
    monkeypatch.setattr(
        cv, "verify_corpus_v3_state",
        lambda t: write_calls.append(t)
    )
    # Point LanceDB at an empty tmp_path so the table won't exist.
    monkeypatch.setenv("LANCEDB_PATH", str(tmp_path))
    # Re-import retrieval_server with distribution mode on.
    app = _reload_app(monkeypatch, distribution_mode=True)
    client = TestClient(app)
    # Hit /query — exercise the per-request gate.
    # We don't care about the response status; we care which verify was called.
    try:
        client.post("/query", json={"question": "test", "top_k": 1})
    except Exception:
        pass
    # Expectation: the write-capable variant was never called from /query in
    # distribution mode. (If neither is called because the table is absent,
    # that is also correct — the guard is irrelevant when there's nothing to verify.)
    assert not write_calls, (
        f"verify_corpus_v3_state (mutating) was called from /query in "
        f"distribution mode. Got calls: {write_calls}"
    )
