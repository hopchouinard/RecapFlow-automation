"""Session-wide test isolation guards.

Two production-safety guarantees, both learned from live incidents diagnosed
on the n8n VM on 2026-08-02:

1. **No test may touch the production LanceDB.** `retrieval_server`'s /query
   pre-search gate calls `verify_corpus_v3_state` -> `ensure_fts_index` ->
   `table.create_fts_index(...)`, which is a WRITE. `DEFAULT_DB_PATH` points
   at the live corpus, so any test exercising /query without setting
   LANCEDB_PATH attempts to create an index in production. On this box it
   failed only because the index already existed; against a fresh or
   partially-migrated table it would have succeeded and mutated the live
   corpus from a test run.

2. **config/.env must not leak into os.environ.** `retrieval_server` calls
   `load_dotenv(CONFIG_DIR / ".env")` at MODULE IMPORT time, and pytest
   imports every test module during *collection* -- so real deployment
   config is injected before the first test executes, regardless of test
   order. That is why tests/test_config_loader.py passed in isolation
   (15/15) and failed 2 in the full suite: the yaml fixtures under test were
   being silently overridden by the deployment's own model pinning.

Both guards are autouse and function-scoped. A test that legitimately needs
a different value calls `monkeypatch.setenv` itself; fixture ordering means
the test's own call runs after this one and wins.
"""
from __future__ import annotations

import pytest

# config_loader.load_extraction_config reads these as overrides
# (`os.environ.get(...) or <yaml value>`). config/.env sets the model pair on
# this deployment, which silently beats any yaml fixture under test.
_DOTENV_LEAKED_VARS = (
    "COMMUNITY_BRAIN_SESSION_THEMES_MODEL",
    "COMMUNITY_BRAIN_SESSION_THEMES_PROMPT",
    "COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL",
    "COMMUNITY_BRAIN_CHUNK_EXTRACTION_PROMPT",
)


@pytest.fixture(autouse=True)
def _isolate_test_environment(tmp_path, monkeypatch):
    """Redirect LANCEDB_PATH to a per-test temp dir; strip leaked .env config."""
    monkeypatch.setenv("LANCEDB_PATH", str(tmp_path / "lancedb"))
    for var in _DOTENV_LEAKED_VARS:
        monkeypatch.delenv(var, raising=False)
