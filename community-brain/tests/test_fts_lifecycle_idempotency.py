"""FTS-index idempotency under detection failure, plus the isolation guards
that keep this suite off the production corpus.

All of this pins one incident, diagnosed on the n8n VM 2026-08-02.

`has_fts_index` is best-effort: it swallows any `list_indices()` failure and
returns False. `ensure_fts_index` then called `create_fts_index` on a table
that already had the index, LanceDB answered "already exists", and the raise
propagated through `verify_corpus_v3_state` into a 503 on every /query.

The measured trigger was client/index version skew: lancedb 0.30.2 (host
venv) enumerated ZERO indices on the very table where 0.34.0 (the serving
container) enumerated `bm25_text_idx`. Same directory, same bytes, different
client. Nothing was wrong with the corpus.
"""
from __future__ import annotations

import os

import pytest

from community_brain.query.fts_lifecycle import ensure_fts_index


class _IndexExistsButUndetectable:
    """The index exists on disk, but the reading client cannot enumerate it."""

    def __init__(self) -> None:
        self.create_calls = 0

    def list_indices(self):
        return []

    def create_fts_index(self, column, **kwargs):
        self.create_calls += 1
        raise RuntimeError(
            "lance error: LanceError(Index): Index name 'bm25_text_idx' already "
            "exists, please specify a different name or use replace=True"
        )


class _ListIndicesRaises(_IndexExistsButUndetectable):
    """The second route to the same place: has_fts_index swallows this and
    returns False, so detection failure becomes a create attempt."""

    def list_indices(self):
        raise RuntimeError("Failed to get statistics for index bm25_text_idx")


def test_already_exists_is_treated_as_success():
    table = _IndexExistsButUndetectable()
    ensure_fts_index(table, column="bm25_text")
    assert table.create_calls == 1


def test_already_exists_is_treated_as_success_when_list_indices_raises():
    table = _ListIndicesRaises()
    ensure_fts_index(table, column="bm25_text")
    assert table.create_calls == 1


def test_genuine_build_failures_still_propagate():
    """Fail closed on real problems. An unbuildable table is still invalid."""

    class _Unbuildable:
        def list_indices(self):
            return []

        def create_fts_index(self, column, **kwargs):
            raise RuntimeError("No space left on device")

    with pytest.raises(RuntimeError, match="No space left on device"):
        ensure_fts_index(_Unbuildable(), column="bm25_text")


def test_present_index_is_not_rebuilt():
    """The happy path must stay cheap: never rebuild a healthy index."""

    class _Idx:
        index_type = "FTS"
        columns = ["bm25_text"]

    class _Healthy:
        def __init__(self) -> None:
            self.create_calls = 0

        def list_indices(self):
            return [_Idx()]

        def create_fts_index(self, column, **kwargs):
            self.create_calls += 1

    table = _Healthy()
    ensure_fts_index(table, column="bm25_text")
    assert table.create_calls == 0


def test_tests_never_point_at_the_production_corpus():
    """conftest's autouse guard must redirect LANCEDB_PATH away from the live
    corpus. Without it, /query tests reach verify_corpus_v3_state ->
    ensure_fts_index -> create_fts_index, which WRITES to production."""
    from community_brain.query import retrieval_server as server_mod

    assert os.environ.get("LANCEDB_PATH")
    assert os.environ["LANCEDB_PATH"] != str(server_mod.DEFAULT_DB_PATH)


@pytest.mark.parametrize(
    "var",
    [
        "COMMUNITY_BRAIN_SESSION_THEMES_MODEL",
        "COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL",
    ],
)
def test_deployment_dotenv_does_not_leak_into_the_suite(var):
    """retrieval_server calls load_dotenv() at import time and pytest imports
    every test module during collection, so config/.env reaches os.environ
    before the first test runs unless conftest strips it."""
    assert var not in os.environ
