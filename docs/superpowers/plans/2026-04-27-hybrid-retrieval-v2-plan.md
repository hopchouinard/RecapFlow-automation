# Hybrid Retrieval v2 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Community Brain retrieval server's pure-vector ranking with hybrid (vector + BM25) ranking plus cue-driven metadata boosting, fixing Findings 6 (rare-token retrieval) and 7 (metadata-tagged retrieval) from the Plan A Phase 6 validation.

**Architecture:** Filter-then-rank stays. The ranker becomes LanceDB native hybrid (RRF, k=60) over an FTS-indexed `full_text` column plus the existing vector column, oversampled by 3×, then post-processed by a Python cue-boost pass that adds small additive deltas to RRF scores when the question's lexical cues align with chunks' structured-metadata flags. Legacy v0 (`transcripts` table) helpers and v0/v1 dual naming are removed in the same release; no parallel endpoint, no `mode` parameter.

**Tech Stack:** Python 3.11, LanceDB ≥0.15 (native FTS/Tantivy), pyarrow, FastAPI, Ollama (`nomic-embed-text` for query embedding — unchanged), pytest, click (CLI).

**Spec:** `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md` — read before starting.

**Working directory:** `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/community-brain` (most paths in this plan are relative to this directory unless prefixed `../`).

**Branch convention:** Work on a feature branch (e.g. `feat/hybrid-retrieval-v2`). Frequent small commits per the project's commit-style conventions documented in `community-brain/CLAUDE.md` (e.g. `feat(retrieval):`, `test(retrieval):`, `refactor(retrieval):`).

---

## Task 1: Spike — verify LanceDB FTS semantics on a chunks-shaped table

**Why first:** Spec §11.1 flagged this as an open question. The whole plan assumes `table.create_fts_index("full_text")` works and that subsequent `table.add(...)` either auto-includes new rows in the FTS index or requires an explicit refresh. Find out before writing the rest.

**Files:**
- Create (temporary, deleted at end of task): `community-brain/scripts/spike_lancedb_fts.py`

- [ ] **Step 1: Create the spike script**

```python
"""Spike: verify LanceDB FTS semantics for the v2 hybrid retrieval design.

Resolves spec open question §11.1: does table.add() auto-update the FTS index,
or do we need explicit optimize/recreate after each ingest?

Run:
    cd community-brain
    .venv/bin/python scripts/spike_lancedb_fts.py
"""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import lancedb
import pyarrow as pa


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="lancedb_fts_spike_"))
    try:
        db = lancedb.connect(str(tmp))
        schema = pa.schema([
            ("chunk_id", pa.string()),
            ("full_text", pa.string()),
            ("embedding", pa.list_(pa.float32(), 4)),
        ])
        table = db.create_table("chunks", schema=schema)

        # Initial population
        table.add([
            {"chunk_id": "a", "full_text": "Adam from Gold Flamingo discussed sales funnel design", "embedding": [1.0, 0, 0, 0]},
            {"chunk_id": "b", "full_text": "weekly sync about onboarding checklists", "embedding": [0, 1.0, 0, 0]},
        ])

        # Build FTS index on full_text
        table.create_fts_index("full_text")
        print("[ok] create_fts_index built")

        # FTS query
        results = table.search("Adam Gold Flamingo", query_type="fts").limit(5).to_list()
        print(f"[ok] FTS query returned {len(results)} rows: {[r['chunk_id'] for r in results]}")

        # Hybrid query (vector + FTS)
        results = (
            table.search([1.0, 0, 0, 0], query_type="hybrid")
            .text("Adam Gold Flamingo")
            .limit(5)
            .to_list()
        )
        print(f"[ok] hybrid query returned {len(results)} rows: {[r['chunk_id'] for r in results]}")

        # Add a NEW row AFTER FTS index was built. Does the FTS index see it?
        table.add([
            {"chunk_id": "c", "full_text": "Adam mentioned LinkedIn outreach for law firms", "embedding": [0, 0, 1.0, 0]},
        ])
        results = table.search("Adam LinkedIn", query_type="fts").limit(5).to_list()
        print(f"[after add, no optimize] FTS query for 'Adam LinkedIn' returned {len(results)} rows: {[r['chunk_id'] for r in results]}")

        # Try optimize and re-query
        try:
            table.optimize()
            print("[ok] table.optimize() succeeded")
        except Exception as exc:
            print(f"[fail] table.optimize() raised: {exc!r}")

        results = table.search("Adam LinkedIn", query_type="fts").limit(5).to_list()
        print(f"[after optimize] FTS query for 'Adam LinkedIn' returned {len(results)} rows: {[r['chunk_id'] for r in results]}")

        # Try recreate-with-replace
        try:
            table.create_fts_index("full_text", replace=True)
            print("[ok] create_fts_index(replace=True) succeeded")
        except Exception as exc:
            print(f"[fail] create_fts_index(replace=True) raised: {exc!r}")

        results = table.search("Adam LinkedIn", query_type="fts").limit(5).to_list()
        print(f"[after replace] FTS query for 'Adam LinkedIn' returned {len(results)} rows: {[r['chunk_id'] for r in results]}")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the spike**

```bash
cd community-brain
.venv/bin/python scripts/spike_lancedb_fts.py
```

Expected: clear output for each labeled `[ok]` / `[after ...]` line. The decisive lines:
- `[after add, no optimize] FTS query ... returned 1 rows: ['c']` → auto-update; `optimize_fts_index` becomes a no-op in production.
- `[after add, no optimize] FTS query ... returned 0 rows` AND `[after optimize] ... returned 1 rows: ['c']` → optimize required after each add.
- `[after add, no optimize] FTS query ... returned 0 rows` AND `[after optimize] ... returned 0 rows` AND `[after replace] ... returned 1 rows: ['c']` → recreate-with-replace required after each add (most expensive).

- [ ] **Step 3: Record the finding**

Pick the cheapest production hook based on the spike output:
- If auto-update: `optimize_fts_index` returns immediately; document why.
- If optimize required: `optimize_fts_index` calls `table.optimize()`.
- If replace required: `optimize_fts_index` calls `table.create_fts_index("full_text", replace=True)`.

Edit the spec's §11.1 to record the verified behavior and pick the implementation. Append to the spec file (do NOT replace §11.1 — append a new "Resolved 2026-04-27 (or current date)" subsection so the original open question is preserved as history):

```markdown
### 11.1 Resolution

LanceDB FTS update-on-write behavior verified via `community-brain/scripts/spike_lancedb_fts.py` on $(date +%Y-%m-%d):

- **Observed behavior:** [auto-update | optimize-required | replace-required]
- **Production hook:** `optimize_fts_index` calls [no-op | `table.optimize()` | `table.create_fts_index("full_text", replace=True)`].
- **Cost on current corpus:** [measured wall time].
```

- [ ] **Step 4: Delete the spike script**

The spike was diagnostic, not production code. Don't carry it.

```bash
rm community-brain/scripts/spike_lancedb_fts.py
# Remove community-brain/scripts/ if it ends up empty (don't delete if other scripts live there)
```

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md
git commit -m "docs(specs): resolve §11.1 — LanceDB FTS update-on-write behavior verified"
```

---

## Task 2: Delete legacy v0 query helpers (cleanup before rename)

**Why before rename:** The current code has both `query_local.search_chunks` (v0, targets the deleted `transcripts` table) and `query_local.search_chunks_v2` (v1, targets `chunks`). Renaming v2 → canonical name in Task 4 would collide. Delete v0 first.

**Files:**
- Modify: `community-brain/src/community_brain/query/__init__.py` — delete `build_filter_expression`
- Modify: `community-brain/src/community_brain/query/query_local.py` — delete `search_chunks` (v0), delete the legacy `format_results` / `build_answer_prompt` / `main` CLI helpers (they import the v0 helper). The CLI is reimplemented in Task 10 if kept.
- Delete: `community-brain/tests/test_query.py` (entirely — it tests v0 only)

- [ ] **Step 1: Verify no other call sites depend on the v0 helpers**

```bash
cd community-brain
grep -rn "from community_brain.query import build_filter_expression\b" src tests
grep -rn "from community_brain.query.query_local import .*search_chunks\b" src tests
```

Expected: only `query_local.py`, `tests/test_query.py`, and possibly the CLI `main()` should reference these. If anything else does, surface it before deleting.

- [ ] **Step 2: Run the existing test suite to capture baseline**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: all 252+ tests pass. Note the count.

- [ ] **Step 3: Delete `tests/test_query.py`**

```bash
rm community-brain/tests/test_query.py
```

- [ ] **Step 4: Replace `community-brain/src/community_brain/query/__init__.py` with a minimal stub**

The file currently exports v0 `build_filter_expression`. After cleanup it just declares the package.

```python
"""Query tools and retrieval server for Community Brain."""

from __future__ import annotations
```

- [ ] **Step 5: Edit `community-brain/src/community_brain/query/query_local.py` to remove v0 helpers**

Delete:
- The `from community_brain.query import build_filter_expression` import line
- The `search_chunks` function (the v0 one — current lines roughly 51–90)
- The `format_results` function
- The `build_answer_prompt` function
- The entire `@click.command()` `main()` function and its decorators
- The `if __name__ == "__main__":` block that calls `main()`
- The `import click` import line
- The `DEFAULT_LLM_MODEL` constant (only `main()` used it)

Keep:
- `sql_quote`
- `build_filter_expression_v2` (renamed in Task 3)
- `search_chunks_v2` (renamed in Task 4)
- The `__all__` list — update it: drop `search_chunks` and `build_filter_expression_v2`'s rename targets are handled later; for now it should read `__all__ = ["search_chunks_v2", "build_filter_expression_v2", "sql_quote"]`.

After editing, the file is much smaller and contains only v1-canonical code plus the v2-suffix-pending-rename symbols.

- [ ] **Step 6: Run the test suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: all remaining tests pass (you deleted ~9 v0 tests in Step 3). Pre-existing v1 tests (`test_query_local_v2.py`, `test_retrieval_server_query_v2.py`, etc.) continue to pass.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "refactor(retrieval): delete legacy v0 query helpers and CLI

The v0 transcripts-table search path is dead code (no live consumers since
Plan A migrated to chunks). Removing it now to clear the namespace before
v2 hybrid retrieval renames v2-suffixed symbols to canonical names.

- delete query/__init__.py::build_filter_expression (v0)
- delete query_local.py::search_chunks (v0)
- delete query_local.py click CLI (depended on v0 helpers; will rebuild
  in Task 10 if it stays)
- delete tests/test_query.py (v0 only)"
```

---

## Task 3: Rename `build_filter_expression_v2` → `build_filter_expression`

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py` — rename function
- Modify: `community-brain/tests/test_query_local_v2.py` — rename imports + symbol references; rename file → `test_query_local.py`
- Modify: `community-brain/src/community_brain/query/retrieval_server.py` — update import (currently uses `from community_brain.query.query_local import sql_quote`; if anything else imports `build_filter_expression_v2`, update)

- [ ] **Step 1: Find every reference to the old name**

```bash
cd community-brain
grep -rn "build_filter_expression_v2" src tests
```

- [ ] **Step 2: Rename the function in `query_local.py`**

Edit `src/community_brain/query/query_local.py`:
- Function definition `def build_filter_expression_v2(filters: dict | None) -> str | None:` → `def build_filter_expression(filters: dict | None) -> str | None:`
- All call sites within the same file (`search_chunks_v2` calls it on the line `user_expr = build_filter_expression_v2(filters)`) → update to `build_filter_expression(filters)`
- Update `__all__` to list `build_filter_expression` instead of `build_filter_expression_v2`

- [ ] **Step 3: Rename the test file and update its imports**

```bash
git mv community-brain/tests/test_query_local_v2.py community-brain/tests/test_query_local.py
```

Edit the renamed file:
- `from community_brain.query.query_local import build_filter_expression_v2, sql_quote` → `from community_brain.query.query_local import build_filter_expression, sql_quote`
- All test function names like `test_build_filter_expression_v2_*` → `test_build_filter_expression_*` (use a search-and-replace; preserve everything else)
- All in-test calls to `build_filter_expression_v2(...)` → `build_filter_expression(...)`

- [ ] **Step 4: Run the renamed test file**

```bash
cd community-brain
.venv/bin/pytest tests/test_query_local.py -v
```

Expected: all tests pass with new names.

- [ ] **Step 5: Run the full suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: pass. Any failures here mean a missed call site — go fix it.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "refactor(retrieval): rename build_filter_expression_v2 → build_filter_expression

The _v2 suffix was relative to the deleted v0 helper. With v0 gone there's
nothing to disambiguate from. Canonical name is shorter and more honest."
```

---

## Task 4: Rename `search_chunks_v2` → `search_chunks` (rename only, no behavior change)

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py` — rename function
- Modify: `community-brain/src/community_brain/query/retrieval_server.py` — update import in `query` handler
- Modify: tests that reference the old name (will be small set after Task 3)

- [ ] **Step 1: Find every reference to the old name**

```bash
cd community-brain
grep -rn "search_chunks_v2" src tests
```

Likely hits: `query_local.py` (definition + `__all__`), `retrieval_server.py` (`from community_brain.query.query_local import search_chunks_v2`), and possibly `tests/test_retrieval_server_query_v2.py`.

- [ ] **Step 2: Rename in `query_local.py`**

Edit `src/community_brain/query/query_local.py`:
- `def search_chunks_v2(...)` → `def search_chunks(...)`
- Docstring mentions of "v2" can stay (the v2 in the docstring refers to the response shape, not the function name); leave them.
- Update `__all__` to list `search_chunks` instead of `search_chunks_v2`

- [ ] **Step 3: Update `retrieval_server.py` import**

Edit `src/community_brain/query/retrieval_server.py` line ~234 (`from community_brain.query.query_local import search_chunks_v2`):
- → `from community_brain.query.query_local import search_chunks`
- Update the call site on line ~247 (`raw = search_chunks_v2(...)` → `raw = search_chunks(...)`)

- [ ] **Step 4: Update test files**

For each remaining hit from Step 1 (likely `tests/test_retrieval_server_query_v2.py` if it patches the symbol with `monkeypatch.setattr` or `mocker.patch`):
- `search_chunks_v2` → `search_chunks` in patches and assertions

- [ ] **Step 5: Run the full suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: pass.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "refactor(retrieval): rename search_chunks_v2 → search_chunks

Final rename in the v0/v1 cleanup chain. Function still does pure-vector
ranking; v2 hybrid behavior lands in subsequent tasks."
```

---

## Task 5: Create `cue_rules.py` — `CueRule` dataclass and initial rule set

**Files:**
- Create: `community-brain/src/community_brain/query/cue_rules.py`
- Create: `community-brain/tests/test_cue_rules.py`

- [ ] **Step 1: Write the failing test for the rule shape**

Create `community-brain/tests/test_cue_rules.py`:

```python
"""Tests for cue rule definitions and the CueRule dataclass."""

from __future__ import annotations

from community_brain.query.cue_rules import CueRule, CUE_RULES


def test_cue_rule_is_immutable_dataclass():
    rule = CueRule(
        name="test",
        cue_phrases=("foo",),
        target_predicate=lambda chunk: True,
        delta=0.005,
    )
    assert rule.name == "test"
    assert rule.cue_phrases == ("foo",)
    assert rule.delta == 0.005
    # frozen=True must prevent mutation
    try:
        rule.name = "other"  # type: ignore[misc]
        raised = False
    except Exception:
        raised = True
    assert raised, "CueRule must be frozen"


def test_cue_rules_initial_set_has_six_rules():
    """Initial set per spec §5.2: six rules."""
    names = {r.name for r in CUE_RULES}
    assert names == {
        "unresolved_questions",
        "decisions",
        "action_items",
        "insights",
        "referenced_prior",
        "questions_general",
    }


def test_cue_rules_deltas_match_spec():
    """Spec §5.2 delta calibration."""
    by_name = {r.name: r for r in CUE_RULES}
    assert by_name["unresolved_questions"].delta == 0.010
    assert by_name["decisions"].delta == 0.008
    assert by_name["action_items"].delta == 0.008
    assert by_name["insights"].delta == 0.006
    assert by_name["referenced_prior"].delta == 0.006
    assert by_name["questions_general"].delta == 0.003


def test_unresolved_questions_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["unresolved_questions"]
    assert rule.target_predicate({"has_unresolved_question": True})
    assert not rule.target_predicate({"has_unresolved_question": False})
    assert not rule.target_predicate({"has_unresolved_question": None})
    assert not rule.target_predicate({})


def test_decisions_predicate_requires_non_empty_list():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["decisions"]
    assert rule.target_predicate({"decisions": ["decided to X"]})
    assert not rule.target_predicate({"decisions": []})
    assert not rule.target_predicate({"decisions": None})
    assert not rule.target_predicate({})


def test_action_items_predicate_requires_non_empty_list():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["action_items"]
    assert rule.target_predicate({"action_items": ["follow up with Adam"]})
    assert not rule.target_predicate({"action_items": []})
    assert not rule.target_predicate({"action_items": None})


def test_insights_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["insights"]
    assert rule.target_predicate({"has_insight": True})
    assert not rule.target_predicate({"has_insight": False})


def test_referenced_prior_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["referenced_prior"]
    assert rule.target_predicate({"references_prior": True})
    assert not rule.target_predicate({"references_prior": False})


def test_questions_general_predicate():
    by_name = {r.name: r for r in CUE_RULES}
    rule = by_name["questions_general"]
    assert rule.target_predicate({"has_question": True})
    assert not rule.target_predicate({"has_question": False})


def test_cue_phrases_are_lowercase():
    """Phrases must be lowercase so case-insensitive matching is one .lower() away."""
    for rule in CUE_RULES:
        for phrase in rule.cue_phrases:
            assert phrase == phrase.lower(), f"{rule.name!r} has non-lowercase phrase {phrase!r}"
```

- [ ] **Step 2: Run the failing test**

```bash
cd community-brain
.venv/bin/pytest tests/test_cue_rules.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'community_brain.query.cue_rules'`.

- [ ] **Step 3: Implement `cue_rules.py`**

Create `community-brain/src/community_brain/query/cue_rules.py`:

```python
"""Cue rules for hybrid retrieval v2 metadata-aware boosting.

A CueRule fires when ANY phrase in `cue_phrases` is found
(case-insensitive substring) in the question, AND the chunk satisfies
`target_predicate`. When it fires, `delta` is added to the chunk's RRF score.

Rules are hardcoded here in v2; the schema's flag/array universe is small
enough that YAML config would be premature. See spec §5 for the full design.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class CueRule:
    name: str
    cue_phrases: tuple[str, ...]
    target_predicate: Callable[[dict], bool]
    delta: float


def _has_unresolved_question(chunk: dict) -> bool:
    return chunk.get("has_unresolved_question") is True


def _has_decisions(chunk: dict) -> bool:
    decisions = chunk.get("decisions")
    return isinstance(decisions, list) and len(decisions) > 0


def _has_action_items(chunk: dict) -> bool:
    items = chunk.get("action_items")
    return isinstance(items, list) and len(items) > 0


def _has_insight(chunk: dict) -> bool:
    return chunk.get("has_insight") is True


def _references_prior(chunk: dict) -> bool:
    return chunk.get("references_prior") is True


def _has_question(chunk: dict) -> bool:
    return chunk.get("has_question") is True


CUE_RULES: tuple[CueRule, ...] = (
    CueRule(
        name="unresolved_questions",
        cue_phrases=(
            "unresolved",
            "open question",
            "not answered",
            "outstanding",
            "didn't get answered",
            "didn't get fully answered",
        ),
        target_predicate=_has_unresolved_question,
        delta=0.010,
    ),
    CueRule(
        name="decisions",
        cue_phrases=("decision", "decided", "resolved", "concluded"),
        target_predicate=_has_decisions,
        delta=0.008,
    ),
    CueRule(
        name="action_items",
        cue_phrases=(
            "action item",
            "commit",
            "commitment",
            "next step",
            "to-do",
            "todo",
            "homework",
        ),
        target_predicate=_has_action_items,
        delta=0.008,
    ),
    CueRule(
        name="insights",
        cue_phrases=("insight", "realization", "aha moment", "key takeaway"),
        target_predicate=_has_insight,
        delta=0.006,
    ),
    CueRule(
        name="referenced_prior",
        cue_phrases=("referenced", "prior call", "last week", "previously", "discussed before"),
        target_predicate=_references_prior,
        delta=0.006,
    ),
    CueRule(
        name="questions_general",
        cue_phrases=("question", "asked"),
        target_predicate=_has_question,
        delta=0.003,
    ),
)
```

- [ ] **Step 4: Run the test to verify pass**

```bash
cd community-brain
.venv/bin/pytest tests/test_cue_rules.py -v
```

Expected: all 9 tests pass.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/cue_rules.py community-brain/tests/test_cue_rules.py
git commit -m "feat(retrieval): add CueRule dataclass and initial rule set

Six rules covering the schema's metadata flag/array fields:
unresolved_questions, decisions, action_items, insights, referenced_prior,
questions_general. Hardcoded per spec §5.3 — YAML lift deferred to v3."
```

---

## Task 6: Implement `apply_cue_boosts(question, candidates)` with graceful failure

**Files:**
- Modify: `community-brain/src/community_brain/query/cue_rules.py` — append `apply_cue_boosts` and the cue-match helper
- Modify: `community-brain/tests/test_cue_rules.py` — append `apply_cue_boosts` tests

- [ ] **Step 1: Write the failing tests**

Append to `community-brain/tests/test_cue_rules.py`:

```python
import logging

from community_brain.query.cue_rules import (
    CueRule,
    CUE_RULES,
    apply_cue_boosts,
    cue_phrase_matches,
)


def test_cue_phrase_matches_case_insensitive():
    assert cue_phrase_matches("What UNRESOLVED questions remain?", ("unresolved",))
    assert cue_phrase_matches("decided to ship", ("decided",))
    assert not cue_phrase_matches("everything is great", ("unresolved",))


def test_cue_phrase_matches_substring_not_word_boundary():
    """Spec §5.1: case-insensitive substring (not word-boundary)."""
    # 'decision' substring matches 'decisions' too, by design
    assert cue_phrase_matches("we made decisions today", ("decision",))


def test_apply_cue_boosts_no_cue_match_no_change():
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.020, "has_unresolved_question": True},
        {"chunk_id": "b", "_rrf_score": 0.015, "has_unresolved_question": False},
    ]
    result = apply_cue_boosts("what was the weather like?", candidates)
    assert result[0]["_rrf_score"] == 0.020
    assert result[1]["_rrf_score"] == 0.015


def test_apply_cue_boosts_unresolved_question_cue_promotes_flagged_chunk():
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.018, "has_unresolved_question": False},
        {"chunk_id": "b", "_rrf_score": 0.015, "has_unresolved_question": True},
    ]
    result = apply_cue_boosts("what unresolved questions remain?", candidates)
    by_id = {c["chunk_id"]: c for c in result}
    assert by_id["a"]["_rrf_score"] == 0.018
    assert by_id["b"]["_rrf_score"] == 0.015 + 0.010


def test_apply_cue_boosts_returns_resorted_list():
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.018, "has_unresolved_question": False},
        {"chunk_id": "b", "_rrf_score": 0.015, "has_unresolved_question": True},
    ]
    result = apply_cue_boosts("what unresolved questions remain?", candidates)
    # b boosted to 0.025; should now rank first
    assert result[0]["chunk_id"] == "b"
    assert result[1]["chunk_id"] == "a"


def test_apply_cue_boosts_multiple_rules_compose_additively():
    """A chunk satisfying multiple flag predicates whose cues are all in the
    question accumulates all the deltas."""
    candidates = [
        {
            "chunk_id": "a",
            "_rrf_score": 0.010,
            "has_unresolved_question": True,
            "references_prior": True,
        },
    ]
    result = apply_cue_boosts(
        "what unresolved questions referenced prior calls?", candidates
    )
    # 0.010 + 0.010 (unresolved) + 0.006 (referenced_prior) = 0.026
    assert abs(result[0]["_rrf_score"] - 0.026) < 1e-9


def test_apply_cue_boosts_predicate_exception_logs_and_skips_rule(caplog):
    """A rule whose target_predicate raises must not crash the whole boost
    pass — it logs and is skipped, other rules continue."""
    bad_rule = CueRule(
        name="bad_rule",
        cue_phrases=("trigger",),
        target_predicate=lambda chunk: chunk["nonexistent_field"]["nested"],
        delta=0.005,
    )
    rules = (*CUE_RULES, bad_rule)
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.010, "has_unresolved_question": True},
    ]
    with caplog.at_level(logging.WARNING):
        result = apply_cue_boosts(
            "trigger unresolved", candidates, rules=rules
        )
    # unresolved cue still fires
    assert abs(result[0]["_rrf_score"] - 0.020) < 1e-9
    assert any("bad_rule" in rec.message for rec in caplog.records)


def test_apply_cue_boosts_does_not_mutate_input():
    """Defensive: apply_cue_boosts returns a new list of new dicts."""
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.010, "has_unresolved_question": True},
    ]
    original_score = candidates[0]["_rrf_score"]
    apply_cue_boosts("what unresolved questions remain?", candidates)
    assert candidates[0]["_rrf_score"] == original_score
```

- [ ] **Step 2: Run the failing tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_cue_rules.py -v
```

Expected: 8 new tests fail with `ImportError: cannot import name 'apply_cue_boosts'` (and `cue_phrase_matches`).

- [ ] **Step 3: Implement `apply_cue_boosts` and `cue_phrase_matches`**

Append to `community-brain/src/community_brain/query/cue_rules.py`:

```python
import logging

logger = logging.getLogger(__name__)


def cue_phrase_matches(question: str, phrases: tuple[str, ...]) -> bool:
    """Case-insensitive substring match: returns True if any phrase appears
    anywhere in `question` ignoring case.
    """
    q = question.lower()
    return any(p in q for p in phrases)


def apply_cue_boosts(
    question: str,
    candidates: list[dict],
    rules: tuple[CueRule, ...] = CUE_RULES,
) -> list[dict]:
    """Apply cue-driven additive boosts to candidate RRF scores.

    For each rule whose cue phrases match the question, scan the candidates;
    for each candidate satisfying the rule's target_predicate, add the
    rule's delta to the candidate's `_rrf_score`. Returns a new list of new
    dicts, sorted by boosted score descending.

    Rule exceptions are caught and logged at WARNING; the offending rule is
    skipped, other rules continue.

    Spec §5.4 (composition): multiple rules can fire on the same candidate;
    deltas accumulate without cap.
    """
    boosted = [dict(c) for c in candidates]

    for rule in rules:
        if not cue_phrase_matches(question, rule.cue_phrases):
            continue
        for chunk in boosted:
            try:
                if rule.target_predicate(chunk):
                    chunk["_rrf_score"] = chunk.get("_rrf_score", 0.0) + rule.delta
            except Exception as exc:
                logger.warning(
                    "cue rule %r predicate raised on chunk %r: %s; skipping rule for remaining candidates",
                    rule.name,
                    chunk.get("chunk_id", "<no-id>"),
                    exc,
                )
                # Don't continue applying this rule to other chunks once it
                # has demonstrated it raises — the predicate is buggy.
                break

    boosted.sort(key=lambda c: c.get("_rrf_score", 0.0), reverse=True)
    return boosted
```

- [ ] **Step 4: Run the tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_cue_rules.py -v
```

Expected: all tests pass (the 9 from Task 5 + the 8 new ones = 17 passing).

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/cue_rules.py community-brain/tests/test_cue_rules.py
git commit -m "feat(retrieval): add apply_cue_boosts with graceful rule-failure handling

Pure function over candidate dicts. Composes deltas additively across rules
(spec §5.4); logs and skips a rule whose predicate raises. Returns a new list
of new dicts sorted by boosted score descending."
```

---

## Task 7: Create `fts_lifecycle.py` — `ensure_fts_index` (idempotent boot hook)

**Files:**
- Create: `community-brain/src/community_brain/query/fts_lifecycle.py`
- Create: `community-brain/tests/test_fts_lifecycle.py`

- [ ] **Step 1: Write the failing test for `ensure_fts_index`**

Create `community-brain/tests/test_fts_lifecycle.py`:

```python
"""Tests for the FTS index lifecycle (boot-time creation, post-ingest refresh)."""

from __future__ import annotations

import lancedb
import pyarrow as pa
import pytest

from community_brain.query.fts_lifecycle import (
    ensure_fts_index,
    has_fts_index,
)


def _make_chunks_table(db_path):
    db = lancedb.connect(str(db_path))
    schema = pa.schema([
        ("chunk_id", pa.string()),
        ("full_text", pa.string()),
        ("embedding", pa.list_(pa.float32(), 4)),
    ])
    table = db.create_table("chunks", schema=schema)
    table.add([
        {"chunk_id": "a", "full_text": "hello world", "embedding": [1.0, 0, 0, 0]},
    ])
    return db, table


def test_has_fts_index_returns_false_when_absent(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    assert has_fts_index(table, "full_text") is False


def test_ensure_fts_index_creates_when_absent(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    assert has_fts_index(table, "full_text") is False
    ensure_fts_index(table, "full_text")
    assert has_fts_index(table, "full_text") is True


def test_ensure_fts_index_is_idempotent(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")
    # Calling again must not raise nor duplicate work
    ensure_fts_index(table, "full_text")
    assert has_fts_index(table, "full_text") is True


def test_ensure_fts_index_logs_creation_time(tmp_path, caplog):
    import logging
    _db, table = _make_chunks_table(tmp_path)
    with caplog.at_level(logging.INFO):
        ensure_fts_index(table, "full_text")
    assert any(
        "FTS index" in rec.message and "full_text" in rec.message
        for rec in caplog.records
    )
```

- [ ] **Step 2: Run the failing test**

```bash
cd community-brain
.venv/bin/pytest tests/test_fts_lifecycle.py -v
```

Expected: FAIL with `ModuleNotFoundError`.

- [ ] **Step 3: Implement `fts_lifecycle.py`**

Create `community-brain/src/community_brain/query/fts_lifecycle.py`:

```python
"""FTS index lifecycle helpers for hybrid retrieval v2.

Two operations:
  - ensure_fts_index(table, column): idempotent. Creates an FTS index on the
    column if absent. Called at server boot so the first query never hits a
    missing index.
  - optimize_fts_index(table, column): called after each /ingest commit.
    Production behavior depends on the spike outcome (Task 1):
      * auto-update: no-op
      * optimize required: table.optimize()
      * recreate required: table.create_fts_index(column, replace=True)

Both operations log their work at INFO/WARNING and never raise into callers
on routine path. Caller-side fallback (graceful degradation) lives in
search_chunks.
"""

from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)


def has_fts_index(table, column: str) -> bool:
    """Return True if `table` has an FTS index on `column`.

    LanceDB exposes `list_indices()` which returns index metadata. The FTS
    indices have `index_type` containing "FTS" or "Inverted" depending on
    LanceDB version; we check both for forward compatibility.
    """
    try:
        indices = table.list_indices()
    except Exception as exc:
        logger.warning("table.list_indices() raised %r; assuming no FTS index", exc)
        return False
    for idx in indices:
        index_type = getattr(idx, "index_type", "") or ""
        columns = getattr(idx, "columns", []) or []
        if column in columns and ("FTS" in str(index_type).upper() or "INVERTED" in str(index_type).upper()):
            return True
    return False


def ensure_fts_index(table, column: str) -> None:
    """Idempotent: create the FTS index on `column` if absent. Logs duration."""
    if has_fts_index(table, column):
        logger.debug("FTS index on column %r already present; skipping creation", column)
        return
    logger.info("FTS index on column %r absent; building...", column)
    t0 = time.monotonic()
    table.create_fts_index(column)
    logger.info("FTS index on column %r built in %.2fs", column, time.monotonic() - t0)


def optimize_fts_index(table, column: str) -> None:
    """Refresh the FTS index after new rows are added.

    The exact mechanic was decided by the spike (Task 1, spec §11.1). Update
    the body of this function according to the recorded resolution:
      - auto-update: leave as no-op + debug log
      - optimize required: call table.optimize()
      - recreate required: call table.create_fts_index(column, replace=True)

    Failures are caught and logged at WARNING; chunks are already committed
    so a refresh failure is not fatal.
    """
    # IMPLEMENTATION NOTE for the engineer running this task:
    # Replace the body below with the path the spike (Task 1) verified.
    # Default is a no-op + warning so missing this step shows up loudly.
    logger.warning(
        "optimize_fts_index is a no-op until Task 1 spike outcome is wired in. "
        "If the spike showed auto-update, remove this warning. If it showed "
        "optimize-required, call table.optimize(). If it showed recreate-required, "
        "call table.create_fts_index(%r, replace=True).",
        column,
    )
```

- [ ] **Step 4: Run the tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_fts_lifecycle.py -v
```

Expected: 4 tests pass.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/fts_lifecycle.py community-brain/tests/test_fts_lifecycle.py
git commit -m "feat(retrieval): add ensure_fts_index lifecycle helper

Idempotent FTS index creation on chunks.full_text. Used at server boot to
guarantee the first /query has a hybrid-ready table. optimize_fts_index is
stubbed pending Task 8 (which wires it per the Task 1 spike resolution)."
```

---

## Task 8: Implement `optimize_fts_index` per the Task 1 spike resolution

**Why separate task:** Task 7 stubs `optimize_fts_index` because its body depends on the spike outcome. This task replaces the stub with the real implementation and tests it.

**Files:**
- Modify: `community-brain/src/community_brain/query/fts_lifecycle.py` — replace `optimize_fts_index` body
- Modify: `community-brain/tests/test_fts_lifecycle.py` — append tests

- [ ] **Step 1: Re-read the spike resolution recorded in spec §11.1**

The spec edit you made in Task 1, Step 3 tells you which path to take:
- auto-update → `optimize_fts_index` is a debug-log no-op
- optimize-required → `optimize_fts_index` calls `table.optimize()`
- recreate-required → `optimize_fts_index` calls `table.create_fts_index(column, replace=True)`

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_fts_lifecycle.py`:

```python
from community_brain.query.fts_lifecycle import optimize_fts_index


def test_optimize_fts_index_makes_new_rows_searchable(tmp_path):
    """End-to-end: add a row after the FTS index is built, call optimize,
    and verify the new row is visible to FTS query."""
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")

    # Add a row that contains a unique token absent from the original data
    table.add([
        {"chunk_id": "b", "full_text": "supercalifragilistic Adam", "embedding": [0, 1.0, 0, 0]},
    ])
    optimize_fts_index(table, "full_text")

    # FTS query for the new token must surface chunk_id 'b'
    results = table.search("supercalifragilistic", query_type="fts").limit(5).to_list()
    ids = [r["chunk_id"] for r in results]
    assert "b" in ids, f"expected 'b' to be searchable after optimize; got {ids}"


def test_optimize_fts_index_does_not_raise_on_repeated_calls(tmp_path):
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")  # second call must not raise
    optimize_fts_index(table, "full_text")  # third call must not raise


def test_optimize_fts_index_logs_failure_does_not_raise(tmp_path, caplog, monkeypatch):
    """If LanceDB raises during optimize, we log WARNING and return — don't
    propagate. The caller (pipeline.ingest_session) shouldn't fail because
    a post-commit FTS refresh failed."""
    import logging
    _db, table = _make_chunks_table(tmp_path)
    ensure_fts_index(table, "full_text")

    # Force the underlying call to raise
    def _boom(*args, **kwargs):
        raise RuntimeError("simulated lancedb internal error")
    # Patch whichever call optimize_fts_index uses (table.optimize OR
    # table.create_fts_index). The monkeypatch covers both.
    monkeypatch.setattr(table, "optimize", _boom, raising=False)
    monkeypatch.setattr(table, "create_fts_index", _boom, raising=False)

    with caplog.at_level(logging.WARNING):
        optimize_fts_index(table, "full_text")  # must NOT raise

    assert any("optimize" in rec.message.lower() or "fts" in rec.message.lower() for rec in caplog.records)
```

- [ ] **Step 3: Run the test (it should fail because the stub still warns)**

```bash
cd community-brain
.venv/bin/pytest tests/test_fts_lifecycle.py -v -k optimize
```

Expected: `test_optimize_fts_index_makes_new_rows_searchable` fails (the stub doesn't do anything that makes new rows searchable if optimize is required).

- [ ] **Step 4: Replace `optimize_fts_index` per the spike resolution**

Edit `community-brain/src/community_brain/query/fts_lifecycle.py` and replace the `optimize_fts_index` body with **one** of these three options based on the spike outcome:

**Option A — auto-update (cheapest):**

```python
def optimize_fts_index(table, column: str) -> None:
    """LanceDB FTS auto-includes rows added after index creation (verified
    by spike, spec §11.1 resolution). No-op."""
    logger.debug("optimize_fts_index(%r): auto-update path; no-op", column)
```

**Option B — optimize required:**

```python
def optimize_fts_index(table, column: str) -> None:
    """Refresh FTS index on `column` so rows added since last build are
    searchable. Verified path (spec §11.1 resolution): table.optimize()."""
    try:
        t0 = time.monotonic()
        table.optimize()
        logger.debug(
            "optimize_fts_index(%r): table.optimize() in %.2fs",
            column,
            time.monotonic() - t0,
        )
    except Exception as exc:
        logger.warning(
            "optimize_fts_index(%r) failed: %r; chunks committed but FTS may "
            "lag until next refresh",
            column,
            exc,
        )
```

**Option C — recreate required:**

```python
def optimize_fts_index(table, column: str) -> None:
    """Recreate FTS index on `column` so rows added since last build are
    searchable. Verified path (spec §11.1 resolution): create_fts_index(replace=True)."""
    try:
        t0 = time.monotonic()
        table.create_fts_index(column, replace=True)
        logger.debug(
            "optimize_fts_index(%r): create_fts_index(replace=True) in %.2fs",
            column,
            time.monotonic() - t0,
        )
    except Exception as exc:
        logger.warning(
            "optimize_fts_index(%r) failed: %r; chunks committed but FTS may "
            "lag until next refresh",
            column,
            exc,
        )
```

- [ ] **Step 5: Run the tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_fts_lifecycle.py -v
```

Expected: all 7 tests pass.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/query/fts_lifecycle.py community-brain/tests/test_fts_lifecycle.py
git commit -m "feat(retrieval): wire optimize_fts_index per spike resolution

Implementation matches the Task 1 spike outcome recorded in spec §11.1.
End-to-end test verifies new rows become FTS-searchable after optimize.
Failures log WARNING; never propagate to the ingest caller."
```

---

## Task 9: Wire hybrid LanceDB query into `search_chunks` (RRF, no cue boost yet)

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py` — replace pure-vector search body with hybrid; preserve filter-then-rank guards
- Modify: `community-brain/tests/test_retrieval_server_query_v2.py` (or create `tests/test_search_hybrid.py`) — TDD against a real tmp LanceDB

- [ ] **Step 1: Write the failing integration test**

Create `community-brain/tests/test_search_hybrid.py`:

```python
"""Integration tests for hybrid search_chunks: real LanceDB on tmp_path.

These tests exercise the LanceDB hybrid query path end-to-end. They mock
Ollama embed (we don't need real semantic similarity — hand-crafted vectors
suffice) but use real LanceDB tables so any schema/contract drift surfaces.
"""

from __future__ import annotations

import lancedb
import pyarrow as pa
import pytest

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema
from community_brain.query.query_local import search_chunks
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index


@pytest.fixture
def chunks_db(tmp_path, monkeypatch):
    """A real LanceDB with a chunks table populated for hybrid search tests."""
    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    table = db.create_table("chunks", schema=schema)

    # Two chunks: 'a' has Adam in full_text, 'b' has only thematic content.
    # Vectors are crafted: 'a' is far from query vector, 'b' is close.
    # If pure vector ranks alone, 'b' wins. With hybrid (BM25 finds 'Adam'
    # in 'a'), 'a' should surface in top results.
    common_fields = {
        "schema_version": "1.0",
        "session_id": "2026-04-01",
        "session_date": "2026-04-01",
        "session_title": None,
        "content_type": "prepared_transcript",
        "source_file": "prepared-transcript.md",
        "total_chunks_in_source": 2,
        "speakers_spoke": [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": None,
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "test",
        "extraction_prompt_version": "test-v1",
        "extraction_status": "success",
        "extraction_error": None,
        "extracted_at": "2026-04-01T00:00:00",
    }

    rows = [
        {
            **common_fields,
            "chunk_id": "a",
            "chunk_index": 0,
            "embed_text": "...",
            "full_text": "Adam from Gold Flamingo discussed sales funnel design",
            "embedding": [0.0, 1.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
        {
            **common_fields,
            "chunk_id": "b",
            "chunk_index": 1,
            "embed_text": "...",
            "full_text": "weekly community sync covered onboarding and retention strategies",
            "embedding": [1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2),
        },
    ]
    table.add(rows)
    ensure_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")

    # Mock the ollama embed call: return a vector close to 'b' (so pure
    # vector would rank 'b' first; hybrid+BM25 should surface 'a' for
    # an Adam-keyword question).
    def _fake_embed(model, input):
        # 'input' is a list; we always return a single embedding
        return {"embeddings": [[1.0, 0.0] + [0.0] * (EMBEDDING_DIM - 2)]}

    import ollama
    monkeypatch.setattr(ollama, "embed", _fake_embed)

    return str(db_path)


def test_hybrid_surfaces_adam_chunk_for_keyword_query(chunks_db):
    """The vector embedding aligns with chunk 'b'. Pure vector would rank
    'b' first. Hybrid (vector + BM25 over 'Adam Gold Flamingo') must
    surface 'a' in the results (top-2 must contain it)."""
    results = search_chunks(
        question="Adam from Gold Flamingo",
        db_path=chunks_db,
        top_k=5,
        filters=None,
    )
    assert len(results) >= 1
    ids = [r["chunk_id"] for r in results]
    assert "a" in ids, f"hybrid retrieval missed entity-grounded chunk; got {ids}"


def test_hybrid_returns_empty_on_missing_table(tmp_path):
    """Fresh LanceDB with no chunks table → empty list, no exception."""
    results = search_chunks(
        question="anything",
        db_path=str(tmp_path),
        top_k=5,
        filters=None,
    )
    assert results == []


def test_hybrid_excludes_failed_extraction_chunks(chunks_db, monkeypatch):
    """Pre-existing v1 contract: extraction_status='success' guard is preserved."""
    # Add a 'failed' chunk that lexically matches the query
    db = lancedb.connect(chunks_db)
    table = db.open_table("chunks")
    failed_row = dict(table.to_arrow().to_pylist()[0])
    failed_row.update(
        {
            "chunk_id": "c-failed",
            "extraction_status": "failed",
            "embedding": [0.0] * EMBEDDING_DIM,
            "full_text": "Adam Gold Flamingo failed extraction",
        }
    )
    table.add([failed_row])
    optimize_fts_index(table, "full_text")

    results = search_chunks(
        question="Adam Gold Flamingo",
        db_path=chunks_db,
        top_k=5,
        filters=None,
    )
    ids = [r["chunk_id"] for r in results]
    assert "c-failed" not in ids
```

- [ ] **Step 2: Run the test (expected fail — `search_chunks` is still pure vector)**

```bash
cd community-brain
.venv/bin/pytest tests/test_search_hybrid.py -v
```

Expected: `test_hybrid_surfaces_adam_chunk_for_keyword_query` fails (pure vector returns 'b' only, or 'a' below 'b'). The other two should already pass.

- [ ] **Step 3: Replace `search_chunks` body with hybrid query**

Edit `community-brain/src/community_brain/query/query_local.py`. Replace the body of `search_chunks` (formerly `search_chunks_v2`) with a hybrid LanceDB query.

```python
OVERSAMPLE_FACTOR = 3


def search_chunks(
    question: str,
    db_path: str,
    top_k: int,
    filters: dict | None,
    ollama_base_url: str | None = None,
    table_name: str = "chunks",
    _use_hybrid: bool = True,  # internal toggle for test/baseline comparisons; do NOT expose via HTTP
) -> list[dict]:
    """Hybrid (vector + BM25) search against the chunks table with optional
    structured filters and the success-guard.

    Pipeline (spec §3.1):
      1. Embed `question` via Ollama (nomic-embed-text).
      2. LanceDB hybrid query: RRF(vector, BM25 on full_text), oversampled
         by OVERSAMPLE_FACTOR.
      3. WHERE clause: extraction_status = 'success' AND caller's filters.
      4. Return top (top_k * OVERSAMPLE_FACTOR) raw rows; cue boost runs
         downstream in the caller.

    `_use_hybrid=False` is a test-only knob that drops the BM25 leg —
    used by the lift-validation tests in the golden query suite to prove
    the hybrid pathway is what surfaces the missing chunks.
    """
    db = lancedb.connect(db_path)
    if table_name not in db.list_tables().tables:
        return []
    table = db.open_table(table_name)

    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=_active_embed_model(), input=[question])
    else:
        response = ollama.embed(model=_active_embed_model(), input=[question])
    query_vector = response["embeddings"][0]

    user_expr = build_filter_expression(filters)
    status_guard = "extraction_status = 'success'"
    where_expr = f"({user_expr}) AND {status_guard}" if user_expr else status_guard

    candidate_count = top_k * OVERSAMPLE_FACTOR

    if _use_hybrid:
        try:
            query = (
                table.search(query_vector, query_type="hybrid")
                .text(question)
                .where(where_expr)
                .limit(candidate_count)
            )
            results = query.to_arrow()
        except Exception as exc:
            logger.warning(
                "hybrid query failed (%r); falling back to vector-only ranking",
                exc,
            )
            query = (
                table.search(query_vector)
                .where(where_expr)
                .limit(candidate_count)
            )
            results = query.to_arrow()
    else:
        query = (
            table.search(query_vector)
            .where(where_expr)
            .limit(candidate_count)
        )
        results = query.to_arrow()

    return [
        {col: results[col][i].as_py() for col in results.column_names}
        for i in range(results.num_rows)
    ]
```

You will need to add a module-level `logger = logging.getLogger(__name__)` if not already present.

- [ ] **Step 4: Run the hybrid integration tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_search_hybrid.py -v
```

Expected: all 3 tests pass. If the entity-grounded test still fails, increase the BM25 weight or check the LanceDB hybrid-mode docs — the test is the spec ground truth.

- [ ] **Step 5: Run the full suite to catch regressions**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: all tests pass. If `test_retrieval_server_query_v2.py` now fails because top-K rankings shifted under hybrid scoring, update the affected assertions to test the API shape (presence of structured response, similarity field non-negative, etc.) rather than specific chunk ordering. Don't weaken the test — port it to test what's actually contractual.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(retrieval): replace pure-vector search_chunks with hybrid (RRF) query

Hybrid scoring via LanceDB native query_type='hybrid' (RRF, k=60). Oversamples
by OVERSAMPLE_FACTOR=3 for downstream cue boost. Preserves filter-then-rank
contract and the extraction_status='success' guard. Internal _use_hybrid
toggle for lift-validation tests.

Hybrid query failure logs WARNING and degrades to vector-only — graceful
degradation per spec §6.3."
```

---

## Task 10: Wire `apply_cue_boosts` into the search pipeline

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py` — call `apply_cue_boosts`, then truncate to `top_k`
- Modify: `community-brain/tests/test_search_hybrid.py` — add cue boost end-to-end test

- [ ] **Step 1: Write the failing test for cue boost in the search pipeline**

Append to `community-brain/tests/test_search_hybrid.py`:

```python
def test_search_chunks_promotes_unresolved_question_chunk_via_cue_boost(
    chunks_db, monkeypatch
):
    """When the question contains 'unresolved questions', a chunk tagged
    has_unresolved_question=True must rank above an otherwise-equal chunk
    without the tag — even when their RRF scores are very close.

    Verifies the cue boost layer runs after RRF fusion."""
    # Add a third chunk with has_unresolved_question=True; vector embedding
    # placed so it would rank below 'b' under pure RRF.
    db = lancedb.connect(chunks_db)
    table = db.open_table("chunks")
    base = dict(table.to_arrow().to_pylist()[0])
    flagged_row = dict(base)
    flagged_row.update(
        {
            "chunk_id": "u",
            "full_text": "general weekly community sync about onboarding and retention",
            "has_unresolved_question": True,
            "embedding": [0.95, 0.05] + [0.0] * (EMBEDDING_DIM - 2),
        }
    )
    table.add([flagged_row])
    optimize_fts_index(table, "full_text")

    results = search_chunks(
        question="what unresolved questions came up?",
        db_path=chunks_db,
        top_k=5,
        filters=None,
    )
    ids = [r["chunk_id"] for r in results]
    assert "u" in ids
    # 'u' should rank at or above 'b' once cue boost is applied
    assert ids.index("u") <= ids.index("b") if "b" in ids else True
```

- [ ] **Step 2: Run the test**

```bash
cd community-brain
.venv/bin/pytest tests/test_search_hybrid.py::test_search_chunks_promotes_unresolved_question_chunk_via_cue_boost -v
```

Expected: FAIL — cue boosts are not yet wired into `search_chunks`.

- [ ] **Step 3: Wire `apply_cue_boosts` into `search_chunks`**

Edit `community-brain/src/community_brain/query/query_local.py` to:
1. Import `apply_cue_boosts` from `cue_rules`
2. After fetching the oversampled candidates, attach an `_rrf_score` to each (LanceDB returns `_relevance_score` for hybrid queries; treat that as the RRF score)
3. Call `apply_cue_boosts(question, candidates)`
4. Truncate to `top_k`

Add at module top:

```python
from community_brain.query.cue_rules import apply_cue_boosts
```

Replace the trailing block of `search_chunks` (the final `return [...]`) with:

```python
    candidates: list[dict] = []
    for i in range(results.num_rows):
        row = {col: results[col][i].as_py() for col in results.column_names}
        # LanceDB hybrid mode emits _relevance_score; vector-only emits
        # _distance. Normalize to a single key the cue boost layer reads.
        if "_relevance_score" in row:
            row["_rrf_score"] = float(row["_relevance_score"])
        else:
            # vector-only fallback path: convert _distance → similarity-like score
            row["_rrf_score"] = 1.0 - float(row.get("_distance", 0.0))
        candidates.append(row)

    boosted = apply_cue_boosts(question, candidates)
    return boosted[:top_k]
```

- [ ] **Step 4: Run the hybrid + cue test**

```bash
cd community-brain
.venv/bin/pytest tests/test_search_hybrid.py -v
```

Expected: all tests pass, including the new cue-boost test.

- [ ] **Step 5: Run the full suite to catch regressions**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: pass.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(retrieval): wire apply_cue_boosts into search_chunks pipeline

After hybrid RRF retrieval, attach _rrf_score to each candidate, run the
cue boost layer (additive deltas on flag-aligned chunks), re-sort, and
truncate to top_k. Preserves backward-compatible vector-only fallback path
when hybrid raises (caught upstream in this same function)."
```

---

## Task 11: Wire `ensure_fts_index` into FastAPI startup

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py` — add lifespan startup hook
- Modify: `community-brain/tests/test_retrieval_server_query_v2.py` (or new test file) — assert the hook is called

- [ ] **Step 1: Write the failing test**

Create `community-brain/tests/test_retrieval_server_startup.py`:

```python
"""Tests for the retrieval server startup lifecycle (FTS index ensure-on-boot)."""

from __future__ import annotations

import lancedb
import pyarrow as pa
import pytest
from fastapi.testclient import TestClient

from community_brain.ingestion.schema import pyarrow_table_schema


@pytest.fixture
def populated_db(tmp_path, monkeypatch):
    db_path = tmp_path / "lancedb"
    db = lancedb.connect(str(db_path))
    schema = pyarrow_table_schema()
    db.create_table("chunks", schema=schema)
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    return db_path


def test_startup_ensures_fts_index_on_chunks_full_text(populated_db):
    """When the server boots and the chunks table exists without an FTS
    index, the lifespan startup hook must build it."""
    from community_brain.query import retrieval_server
    from community_brain.query.fts_lifecycle import has_fts_index

    db = lancedb.connect(str(populated_db))
    table = db.open_table("chunks")
    assert has_fts_index(table, "full_text") is False, "precondition: no FTS index yet"

    with TestClient(retrieval_server.app) as _client:
        # TestClient context triggers lifespan startup
        pass

    table = db.open_table("chunks")
    assert has_fts_index(table, "full_text") is True


def test_startup_no_chunks_table_does_not_raise(tmp_path, monkeypatch):
    """Fresh deployment: no chunks table yet. Startup must not crash —
    /ingest will create the table later."""
    monkeypatch.setenv("LANCEDB_PATH", str(tmp_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    from community_brain.query import retrieval_server

    with TestClient(retrieval_server.app) as client:
        resp = client.get("/health")
        assert resp.status_code == 200
```

- [ ] **Step 2: Run the failing test**

```bash
cd community-brain
.venv/bin/pytest tests/test_retrieval_server_startup.py -v
```

Expected: `test_startup_ensures_fts_index_on_chunks_full_text` fails because the hook doesn't exist yet.

- [ ] **Step 3: Add the lifespan startup hook**

Edit `community-brain/src/community_brain/query/retrieval_server.py`. Replace the `app = FastAPI(...)` line with a lifespan-aware definition. Add at the top of the file:

```python
from contextlib import asynccontextmanager
import lancedb

from community_brain.query.fts_lifecycle import ensure_fts_index
```

Then add above `app = FastAPI(...)`:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Server startup hook: ensure the FTS index on chunks.full_text exists.

    No-ops if the chunks table doesn't exist yet (fresh deployment, no
    sessions ingested) — /ingest will create the table, and the next boot
    will build the index.
    """
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    try:
        db = lancedb.connect(db_path)
        if "chunks" in db.list_tables().tables:
            table = db.open_table("chunks")
            ensure_fts_index(table, "full_text")
        else:
            logger.info(
                "startup: chunks table does not exist yet at %s; FTS index "
                "will be built on first /ingest or next boot",
                db_path,
            )
    except Exception as exc:
        logger.warning("startup FTS index ensure raised %r; continuing", exc)
    yield
```

Then update the `app = FastAPI(...)` constructor:

```python
app = FastAPI(
    title="Community Brain Retrieval API",
    description="Search coaching call transcripts by semantic similarity.",
    version="0.2.0",
    lifespan=lifespan,
)
```

(Bump from `0.1.0` to `0.2.0` — minor version bump signals the v2 retrieval change.)

- [ ] **Step 4: Run the startup tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_retrieval_server_startup.py -v
```

Expected: both tests pass.

- [ ] **Step 5: Run the full suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: pass.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(retrieval): ensure FTS index on chunks.full_text at server boot

FastAPI lifespan startup hook builds the FTS index if the chunks table
exists but the index is absent. Idempotent. Bumps server version to 0.2.0
to flag the v2 hybrid retrieval cutover."
```

---

## Task 12: Wire `optimize_fts_index` into `pipeline.ingest_session`

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/pipeline.py` — call `optimize_fts_index` after successful chunk commit
- Modify: `community-brain/tests/test_ingestion_pipeline.py` — assert the hook is called

- [ ] **Step 1: Find where the pipeline writes chunks**

```bash
cd community-brain
grep -n "_commit_chunks\|table.add\|create_table" src/community_brain/ingestion/pipeline.py
```

Identify the function and the line just after a successful add/commit. The post-commit hook goes there.

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_ingestion_pipeline.py` (or create a new test file `test_ingestion_pipeline_fts.py` if the existing file is large):

```python
def test_ingest_session_calls_optimize_fts_index_after_commit(
    tmp_path, monkeypatch, mocked_pipeline_env
):
    """After a successful chunk commit, ingest_session must call
    optimize_fts_index so the new chunks become BM25-searchable on the
    next /query."""
    from unittest.mock import MagicMock
    from community_brain.ingestion import pipeline

    optimize_calls: list[tuple] = []

    def _capture(table, column):
        optimize_calls.append((column,))

    monkeypatch.setattr(pipeline, "optimize_fts_index", _capture)

    # Use the existing test-helper to drive a happy-path ingest. This will
    # vary by the existing pattern in test_ingestion_pipeline.py — match it.
    # Pseudocode:
    #   request = build_minimal_ingest_request(tmp_path)
    #   pipeline.ingest_session(request, config_dir=..., db_path=...)
    #   assert optimize_calls == [("full_text",)]
    raise NotImplementedError(
        "Adapt this test to the existing test_ingestion_pipeline.py harness. "
        "The body should drive a happy-path ingest and assert optimize_calls "
        "contains exactly one entry: ('full_text',)."
    )
```

When you run the test it'll fail with `NotImplementedError`. That's expected — the next step replaces the body with the real harness invocation. (This is a placeholder reminding you to wire it; running it as-is forces you to replace it before moving on.)

- [ ] **Step 3: Adapt the test to the existing harness**

Open `community-brain/tests/test_ingestion_pipeline.py` and find an existing test that drives a happy-path `pipeline.ingest_session` call. Copy its setup (request building, fixtures, monkeypatches), substitute the assertion at the end, and replace the placeholder body from Step 2.

- [ ] **Step 4: Run the failing test**

```bash
cd community-brain
.venv/bin/pytest tests/test_ingestion_pipeline.py -v -k optimize
```

Expected: FAIL because `pipeline.optimize_fts_index` is not yet imported nor called.

- [ ] **Step 5: Add the optimize call to the pipeline**

Edit `community-brain/src/community_brain/ingestion/pipeline.py`:

1. Add the import near the top:

```python
from community_brain.query.fts_lifecycle import optimize_fts_index
```

2. After the line that successfully commits chunks (e.g. `table.add(...)` or the helper that calls it), add:

```python
try:
    optimize_fts_index(table, "full_text")
except Exception as exc:
    # optimize_fts_index already catches and logs; this is belt-and-suspenders
    # against future changes that might propagate.
    logger.warning(
        "optimize_fts_index after ingest raised %r; chunks committed but FTS "
        "may lag until next refresh", exc
    )
```

(The exact placement depends on the existing code structure. Place it inside the success branch, AFTER the chunks have been committed but BEFORE the `IngestResult` is returned.)

- [ ] **Step 6: Run the test**

```bash
cd community-brain
.venv/bin/pytest tests/test_ingestion_pipeline.py -v -k optimize
```

Expected: pass.

- [ ] **Step 7: Run the full suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: pass.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(ingestion): refresh FTS index after each successful chunk commit

After ingest_session commits chunks, call optimize_fts_index('full_text')
so freshly-written rows become BM25-searchable on the next /query.
Failure logs WARNING but does not fail the ingest — chunks are already
committed and the next ingest's optimize will catch up."
```

---

## Task 13: Golden query fixtures + lift-validation integration tests

**Files:**
- Create: `community-brain/tests/fixtures/golden_queries.yaml`
- Create: `community-brain/tests/fixtures/golden_corpus/` (subset of real chunks committed as test data — ~10–20 chunks)
- Create: `community-brain/tests/test_golden_queries.py`

**Note:** This task requires picking real chunks from the live corpus. Run the live retrieval server's `/sessions` endpoint or query LanceDB directly on the VM to identify chunks that satisfy the spec's success criteria for findings 6 and 7. If the live VM is not accessible from the dev machine, fall back to a hand-crafted synthetic corpus that exercises the same code paths — call this out in the test docstring.

- [ ] **Step 1: Build the golden corpus fixture**

Create `community-brain/tests/fixtures/golden_corpus/seed.py` — a small Python script that creates a LanceDB at a given path with ~10 chunks engineered to exercise hybrid + cue boost.

```python
"""Seed a small LanceDB corpus for golden-query tests.

Creates a chunks table at a given path with engineered rows covering:
  - Entity-grounded queries (Finding 6): chunks with rare proper-noun
    tokens in full_text but bland embed_text vectors.
  - Metadata-tagged queries (Finding 7): chunks with has_unresolved_question,
    decisions, action_items, has_insight, references_prior set, alongside
    chunks lacking the flags but with similar thematic content.

Used by tests/test_golden_queries.py. Not a runtime dependency.
"""

from __future__ import annotations

import sys
from pathlib import Path

import lancedb

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema


COMMON = {
    "schema_version": "1.0",
    "session_title": None,
    "content_type": "extracted_signal",
    "source_file": "extracted-signal.md",
    "total_chunks_in_source": 10,
    "speakers_spoke": [],
    "speakers_mentioned": [],
    "keywords": [],
    "topic_label": None,
    "session_themes": ["growth", "onboarding"],
    "speech_acts": [],
    "stance": None,
    "certainty": "asserted",
    "chunk_local_markers": [],
    "corpus_derived_markers": [],
    "corpus_markers_computed_at": None,
    "decisions": [],
    "action_items": [],
    "external_refs": [],
    "extraction_model": "test",
    "extraction_prompt_version": "test-v1",
    "extraction_status": "success",
    "extraction_error": None,
    "extracted_at": "2026-04-01T00:00:00",
    "embed_text": "...",
}


def _row(idx, chunk_id, session_id, full_text, **overrides):
    """Build a row with an embedding vector that places it generically."""
    base = {
        **COMMON,
        "chunk_id": chunk_id,
        "session_id": session_id,
        "session_date": session_id,
        "chunk_index": idx,
        "entities": [],
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "references_prior": False,
        "full_text": full_text,
        "embedding": [float((idx + 1) * 0.01)] * EMBEDDING_DIM,
    }
    base.update(overrides)
    return base


def seed(db_path: str) -> None:
    db = lancedb.connect(db_path)
    schema = pyarrow_table_schema()
    if "chunks" in db.list_tables().tables:
        db.drop_table("chunks")
    table = db.create_table("chunks", schema=schema)
    rows = [
        # --- Finding 6 fixtures: entity-grounded ---
        _row(0, "f6-adam-1", "2026-02-01",
             "Adam from Gold Flamingo Solutions described the sales funnel for law firms",
             entities=["Adam", "Gold Flamingo"]),
        _row(1, "f6-adam-2", "2026-02-08",
             "Adam followed up on his LinkedIn outreach experiment to law firm partners",
             entities=["Adam"]),
        _row(2, "f6-bland-1", "2026-02-15",
             "general weekly community sync about onboarding and retention strategies"),
        _row(3, "f6-bland-2", "2026-02-22",
             "checklist hygiene and follow-up cadence for new community members"),
        # --- Finding 7 fixtures: metadata-tagged ---
        _row(4, "f7-unres-1", "2026-03-01",
             "open question about how to scope the consulting engagement remained unresolved",
             has_unresolved_question=True),
        _row(5, "f7-unres-2", "2026-03-08",
             "we still don't know whether to charge a flat fee or hourly",
             has_unresolved_question=True),
        _row(6, "f7-decision-1", "2026-03-15",
             "decided to ship the new pricing page next Monday",
             decisions=["ship pricing page Monday"], has_answer=True),
        _row(7, "f7-actions-1", "2026-03-22",
             "next steps: send the LinkedIn message to all law firm contacts by Friday",
             action_items=["send LinkedIn message Friday"]),
        _row(8, "f7-insight-1", "2026-03-29",
             "key takeaway: the funnel breaks at the demo-to-proposal handoff",
             has_insight=True),
        _row(9, "f7-prior-1", "2026-04-05",
             "as discussed before during the launch retro, the onboarding flow drops off at step three",
             references_prior=True),
    ]
    table.add(rows)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: seed.py <db_path>", file=sys.stderr)
        sys.exit(2)
    seed(sys.argv[1])
    print(f"seeded golden corpus at {sys.argv[1]}")
```

- [ ] **Step 2: Create the golden query manifest**

Create `community-brain/tests/fixtures/golden_queries.yaml`:

```yaml
# Golden query suite for hybrid retrieval v2 validation.
#
# Each entry maps a free-form question to the chunk_ids it MUST surface in
# top-K under hybrid retrieval. `min_match_count` is the floor — at least N
# of `expected_chunk_ids` must be present.
#
# `expect_lift_over_vector_only`: when true, the vector-only baseline is
# expected to fail this assertion (proves hybrid is responsible for the lift).

queries:
  # --- Finding 6 (entity-grounded) ---
  - id: f6-adam-direct
    question: "What did Adam from Gold Flamingo commit to?"
    target_finding: "6"
    top_k: 10
    expected_chunk_ids: [f6-adam-1, f6-adam-2]
    min_match_count: 2
    expect_lift_over_vector_only: true

  - id: f6-adam-rephrased
    question: "Adam Gold Flamingo law firms LinkedIn"
    target_finding: "6"
    top_k: 10
    expected_chunk_ids: [f6-adam-1, f6-adam-2]
    min_match_count: 2
    expect_lift_over_vector_only: false

  # --- Finding 7 (metadata-tagged) ---
  - id: f7-unresolved
    question: "What unresolved questions came up across these calls?"
    target_finding: "7"
    top_k: 10
    expected_chunk_ids: [f7-unres-1, f7-unres-2]
    min_match_count: 2
    expect_lift_over_vector_only: true

  - id: f7-decisions
    question: "What decisions were made?"
    target_finding: "7"
    top_k: 10
    expected_chunk_ids: [f7-decision-1]
    min_match_count: 1
    expect_lift_over_vector_only: true

  - id: f7-action-items
    question: "What action items did we commit to?"
    target_finding: "7"
    top_k: 10
    expected_chunk_ids: [f7-actions-1]
    min_match_count: 1
    expect_lift_over_vector_only: true

  - id: f7-insights
    question: "What were the key takeaways?"
    target_finding: "7"
    top_k: 10
    expected_chunk_ids: [f7-insight-1]
    min_match_count: 1
    expect_lift_over_vector_only: false

  - id: f7-references-prior
    question: "What was referenced from prior calls?"
    target_finding: "7"
    top_k: 10
    expected_chunk_ids: [f7-prior-1]
    min_match_count: 1
    expect_lift_over_vector_only: false
```

- [ ] **Step 3: Write the golden test**

Create `community-brain/tests/test_golden_queries.py`:

```python
"""Golden query suite — regression protection for hybrid retrieval v2.

For each query in tests/fixtures/golden_queries.yaml:
  1. Run search_chunks (hybrid + cue boost) against the seeded golden corpus.
  2. Assert top-K contains at least `min_match_count` of `expected_chunk_ids`.
  3. If `expect_lift_over_vector_only`, also run search_chunks(_use_hybrid=False)
     and assert it does NOT satisfy the same min_match_count — proving the
     hybrid path is responsible for the surfaced chunks.

If a query starts failing under code change, the implementation regressed.
Fix the implementation, not the test.
"""

from __future__ import annotations

from pathlib import Path

import lancedb
import pytest
import yaml

from community_brain.ingestion.schema import EMBEDDING_DIM
from community_brain.query.query_local import search_chunks
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index


FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="module")
def golden_db(tmp_path_factory):
    """Seed a LanceDB at module scope (once per pytest run); shared across queries."""
    import sys
    sys.path.insert(0, str(FIXTURES_DIR / "golden_corpus"))
    from seed import seed  # type: ignore

    db_path = tmp_path_factory.mktemp("golden_db")
    seed(str(db_path))

    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    ensure_fts_index(table, "full_text")
    optimize_fts_index(table, "full_text")
    return str(db_path)


@pytest.fixture
def fake_embed(monkeypatch):
    """Return a generic embedding for any input — golden tests rely on the
    BM25 + cue boost layers, not on semantic similarity. Vector path returns
    a constant vector that doesn't favor any specific golden chunk."""
    def _embed(model, input):
        return {"embeddings": [[0.5] * EMBEDDING_DIM]}
    import ollama
    monkeypatch.setattr(ollama, "embed", _embed)


def _load_queries():
    with open(FIXTURES_DIR / "golden_queries.yaml") as f:
        return yaml.safe_load(f)["queries"]


@pytest.mark.parametrize("query_spec", _load_queries(), ids=lambda q: q["id"])
def test_golden_query_hybrid(query_spec, golden_db, fake_embed):
    results = search_chunks(
        question=query_spec["question"],
        db_path=golden_db,
        top_k=query_spec["top_k"],
        filters=None,
    )
    ids = [r["chunk_id"] for r in results]
    matches = [c for c in query_spec["expected_chunk_ids"] if c in ids]
    assert len(matches) >= query_spec["min_match_count"], (
        f"hybrid retrieval missed expected chunks for {query_spec['id']}: "
        f"got {ids}; expected ≥{query_spec['min_match_count']} of "
        f"{query_spec['expected_chunk_ids']}"
    )


@pytest.mark.parametrize(
    "query_spec",
    [q for q in _load_queries() if q.get("expect_lift_over_vector_only")],
    ids=lambda q: q["id"],
)
def test_golden_query_vector_only_baseline_misses(query_spec, golden_db, fake_embed):
    """Lift validation: pure-vector path must NOT satisfy min_match_count
    on these queries — proves the hybrid+cue layers are doing the work."""
    results = search_chunks(
        question=query_spec["question"],
        db_path=golden_db,
        top_k=query_spec["top_k"],
        filters=None,
        _use_hybrid=False,
    )
    ids = [r["chunk_id"] for r in results]
    matches = [c for c in query_spec["expected_chunk_ids"] if c in ids]
    assert len(matches) < query_spec["min_match_count"], (
        f"vector-only baseline UNEXPECTEDLY satisfied {query_spec['id']}: "
        f"got {ids}; the lift assertion is now meaningless. Either the test "
        f"corpus is wrong (vector path got lucky) or the fixture needs "
        f"more thematic divergence between flagged and unflagged chunks."
    )
```

Note: `pyyaml` may not yet be a test dependency. If `import yaml` fails:

```bash
cd community-brain
.venv/bin/pip install pyyaml
```

And add `pyyaml` to the `[dev]` extras in `pyproject.toml`:

```toml
[project.optional-dependencies]
dev = [
    # ... existing deps ...
    "pyyaml",
]
```

- [ ] **Step 4: Run the golden tests**

```bash
cd community-brain
.venv/bin/pytest tests/test_golden_queries.py -v
```

Expected: all hybrid tests pass. Lift-validation tests pass. If `f7-decisions` or `f7-action-items` lift tests fail (vector-only baseline accidentally surfaces the target chunk), tweak the seeded chunks in `seed.py` to make the thematic content of decoys closer to the question — or lower the `min_match_count` floor.

- [ ] **Step 5: Run the full suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: pass. Total test count increases by ~10 (one per golden query × hybrid test + lift tests).

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "test(retrieval): golden query suite + lift validation against hybrid path

Engineered 10-chunk corpus exercises both Finding 6 (entity-grounded) and
Finding 7 (metadata-tagged) query types. Hybrid path must surface expected
chunks; vector-only baseline must NOT satisfy the same assertion on queries
flagged expect_lift_over_vector_only — proves the lift comes from the new
machinery, not corpus luck."
```

---

## Task 14: Update CHANGELOG.md and community-brain/CLAUDE.md

**Files:**
- Modify: `community-brain/docs/migrations/CHANGELOG.md` — add v2 entry
- Modify: `community-brain/CLAUDE.md` — refresh Trade-offs and v2-backlog sections

- [ ] **Step 1: Read the current CHANGELOG to match its style**

```bash
cd community-brain
cat docs/migrations/CHANGELOG.md | head -100
```

Match the heading style, version-numbering convention, and section ordering.

- [ ] **Step 2: Append the v2 retrieval entry**

Add a new section to `community-brain/docs/migrations/CHANGELOG.md` matching the existing pattern. Concrete content:

```markdown
## §X. Hybrid Retrieval v2 — 2026-04-27 (or current date)

**Type:** Retrieval-layer change (additive index, no schema migration).

**Scope:** `community_brain.query` package, `community_brain.ingestion.pipeline`. No change to chunks-table schema (still 37 fields, schema_version unchanged at "1.0").

**What changed:**
- LanceDB FTS index added on `chunks.full_text` (Tantivy-based).
- `/query` ranker is now hybrid (vector + BM25, RRF k=60) with oversampling 3× and a Python cue-boost post-processing layer. See `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`.
- Legacy v0 (`transcripts`-table) helpers removed: `query.__init__.build_filter_expression`, `query_local.search_chunks` (v0), `query_local.format_results`, `query_local.build_answer_prompt`, click CLI.
- `query_local.build_filter_expression_v2` renamed to `build_filter_expression`. `query_local.search_chunks_v2` renamed to `search_chunks`.
- `retrieval_server` version bumped from `0.1.0` to `0.2.0`.

**Operator action required:**
- None. First boot of the new container builds the FTS index automatically.
- Open WebUI filter and n8n workflows continue to work without change.

**Rollback:**
- Redeploy prior container image. The on-disk FTS index is auxiliary metadata — pre-v2 binaries ignore it (verified via spec §11.5 in implementation phase).
```

- [ ] **Step 3: Update `community-brain/CLAUDE.md`**

Edits to make in `community-brain/CLAUDE.md`:

1. **In the "Known v2 backlog" section**, remove items that v2 actually addresses. Specifically, hybrid retrieval is no longer a backlog item — delete or reword any line referencing "hybrid search" / "BM25" / "metadata-aware ranking" as backlog.

2. **In the "Trade-offs we've deliberately kept" section**, add an entry describing the v2 cutover:

```markdown
- **`/query` ranking is hybrid (vector + BM25 RRF, k=60) with cue-driven metadata boosting.** Fixed in v2; see `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`. Pure-vector ranking is no longer available as an opt-in mode — the fallback runs only on FTS-index unavailability and is internal.
```

3. **In the "Failed-extraction chunks are intentionally unsearchable" section**, no change needed — the success-guard semantics are preserved.

- [ ] **Step 4: Verify docs render and link integrity**

```bash
cd /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation
grep -l "v2 backlog\|backlog item" community-brain/CLAUDE.md
```

Make sure no stale "v2 backlog" references remain that v2 actually closed.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "docs(migrations,community-brain): record Hybrid Retrieval v2 cutover

CHANGELOG entry for v2 (no schema migration; FTS index is auxiliary).
CLAUDE.md updated: removes closed v2-backlog items, adds the new ranking
contract to Trade-offs."
```

---

## Task 15: Final verification — full test suite and clean import surface

**Files:** None modified — verification only.

- [ ] **Step 1: Run the full test suite**

```bash
cd community-brain
.venv/bin/pytest tests/ -q
```

Expected: all tests pass (counts will be original ~252 minus the 9 deleted v0 tests, plus ~25 new tests = ~270 total). Pyright noise about unused fixtures is OK.

- [ ] **Step 2: Confirm no dangling references to removed symbols**

```bash
cd community-brain
grep -rn "search_chunks_v2\|build_filter_expression_v2\|test_query_local_v2" src tests
```

Expected: no output. Any hits indicate a missed rename.

- [ ] **Step 3: Confirm no dangling v0 references**

```bash
cd community-brain
grep -rn "from community_brain.query import build_filter_expression$\|table_name=\"transcripts\"" src tests
```

Expected: no output. Any hits indicate v0 dead code that survived cleanup.

- [ ] **Step 4: Lint with the project's existing tooling (if any)**

```bash
cd community-brain
.venv/bin/python -m pyflakes src/community_brain/query/ 2>&1 | head -20
```

Expected: no unused-import warnings in the touched files. (Pyright noise about test fixtures is documented in CLAUDE.md and may be ignored.)

- [ ] **Step 5: Smoke test against a temp database**

```bash
cd community-brain
.venv/bin/python -c "
from community_brain.query.cue_rules import CUE_RULES, apply_cue_boosts
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index
from community_brain.query.query_local import search_chunks, build_filter_expression
print('symbol-resolution OK')
print(f'CUE_RULES: {len(CUE_RULES)} rules')
"
```

Expected: `symbol-resolution OK\nCUE_RULES: 6 rules`.

- [ ] **Step 6: Optional — run the server locally**

```bash
cd community-brain
LANCEDB_PATH=/tmp/test-cb \
RETRIEVAL_PORT=18999 \
.venv/bin/python -m uvicorn community_brain.query.retrieval_server:app --port 18999 &
sleep 2
curl -s http://127.0.0.1:18999/health
kill %1
```

Expected: `{"status":"ok"}`.

- [ ] **Step 7: Final commit (if anything got cleaned up in verification)**

If Steps 2–4 surfaced anything:

```bash
git add -A
git commit -m "chore(retrieval): clean up dangling references after v2 cutover"
```

---

## Task 16: Operator-side validation against live VM (post-merge)

**Why separate:** This task requires the deployed container, so it happens after merge. Run it the same day or next; document outcomes in the Plan A spec §10 as an addendum.

**Files:**
- Modify: `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` — append a §10.x addendum

- [ ] **Step 1: Deploy the v2 container to the VM**

Follow `community-brain/docs/DEPLOYMENT.md` for the canonical SSH-driven runbook. Confirm:

- New container image is running (`docker compose ps`)
- `retrieval_server` logs show `INFO: FTS index on column 'full_text' built in N.NNs` on first boot
- `/health` returns 200 from the LAN URL `http://10.1.30.10:8999/health`

- [ ] **Step 2: Run the five Phase 6 spec query types via Open WebUI**

Plan A spec §10 Phase 6 lists the five query types. For each, run a representative natural-language question against the live Open WebUI filter (which now hits v2 retrieval). Note:

- Top-K chunk_ids surfaced
- Whether the answering LLM cites real chunks
- Whether the answer satisfies the spec criterion in the Phase 6 table

Specifically retest the Finding 6 and Finding 7 cases that originally failed:

- **Finding 6:** *"What did Adam from Gold Flamingo commit to?"* — top-10 must contain ≥5 chunks tagged with Adam in `entities` or mentioning Adam in `full_text`.
- **Finding 7:** *"What unresolved questions came up across these calls?"* — top-10 must contain ≥5 chunks with `has_unresolved_question=True`.

- [ ] **Step 3: Append findings to the Plan A spec**

Edit `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md`. After the Phase 6 validation findings section (§10), add:

```markdown
##### v2 hybrid retrieval validation (YYYY-MM-DD)

After deploying Hybrid Retrieval v2 (see `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`), re-validated the queries that originally failed:

- **Finding 6 case** *(Adam from Gold Flamingo)*: top-10 contained N of M expected chunks. [Pass / Fail].
- **Finding 7 case** *(unresolved questions)*: top-10 contained N of 38 tagged chunks. [Pass / Fail].
- **Other Phase 6 query types**: [observed outcomes per type].

[Outcomes summary; any tuning required.]
```

- [ ] **Step 4: Update Findings 6 and 7 with the v2 cross-reference**

In the same spec, find the "v2 backlog item" notes inside Findings 6 and 7 and replace with:

```markdown
**Addressed in v2:** see `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md` and the v2 hybrid retrieval validation results above.
```

- [ ] **Step 5: Commit the validation results**

```bash
git add docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md
git commit -m "docs(specs): record v2 hybrid retrieval validation against live VM

Phase 6 §10 addendum capturing post-deploy validation outcomes for the two
findings that motivated v2: entity-grounded retrieval and metadata-tagged
retrieval. Cross-references back to the v2 design spec."
```

- [ ] **Step 6: Update root CLAUDE.md "Current status" section**

```bash
$EDITOR /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/CLAUDE.md
```

In the "Current status" section, mark Track C complete and update the date. Optionally remove the v2 brainstorming starter prompt from `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md` since the work is done.

```bash
git add -A
git commit -m "docs: mark Hybrid Retrieval v2 (Track C) complete in current status"
```

---

# Self-review (writing-plans skill)

**Spec coverage check:**

| Spec section | Covered by task |
|---|---|
| §1 Motivation | (no implementation) |
| §2 Goals/Non-goals | Task 9 (hybrid), Task 10 (cue boost), Tasks 2–4 (legacy ripout) |
| §2.3 Semantic break | Task 14 (CHANGELOG) |
| §3 Architecture (data flow) | Tasks 9, 10, 11, 12 |
| §3.2 Filter/boost layering | Task 9 (preserves WHERE) + Task 10 (boost over filtered set) |
| §3.3 Oversampling | Task 9 |
| §4.1 Code changes | Tasks 2–4, 9, 10, 11, 12 |
| §4.2 Test changes | Tasks 5, 6, 7, 8, 9, 10, 11, 12, 13 |
| §4.3 Doc changes | Task 14 |
| §5 Cue rule design | Tasks 5, 6 |
| §6 FTS lifecycle | Tasks 1, 7, 8, 11, 12 |
| §6.3 Missing-index degradation | Task 9 (try/except wraps hybrid query) |
| §7 API contract | Task 11 (lifespan); shape preserved by Task 9 |
| §8 Performance budget | (no specific implementation; covered by integration tests) |
| §9 Validation plan | Task 13 (golden queries), Task 16 (operator) |
| §10 Rollout | Task 16 |
| §11 Open questions | Task 1 resolves §11.1; §11.2–§11.5 flagged in-place |
| §12 Future work | (out of scope) |

**Placeholder scan:** None — every step contains the actual code or commands. The Task 12 Step 2 "raise NotImplementedError" is intentional (a forcing function the engineer must replace with real test harness in Step 3); not a true placeholder.

**Type consistency:** Function signatures match across tasks: `search_chunks(question, db_path, top_k, filters, ollama_base_url=None, table_name="chunks", _use_hybrid=True) -> list[dict]`; `apply_cue_boosts(question, candidates, rules=CUE_RULES) -> list[dict]`; `ensure_fts_index(table, column)`; `optimize_fts_index(table, column)`. Cue rule dataclass field names (`name`, `cue_phrases`, `target_predicate`, `delta`) consistent across Tasks 5, 6.

**Scope check:** Single sub-project. ~16 tasks. Average task size 5–10 minutes for the simple ones (renames, doc updates), 20–30 minutes for the heavy ones (Task 9 hybrid wiring, Task 13 golden corpus). Total estimate: ~6–8 hours of focused implementation, plus the post-merge VM validation in Task 16.

---

**Plan complete and saved to `docs/superpowers/plans/2026-04-27-hybrid-retrieval-v2-plan.md`.**

Two execution options:

**1. Subagent-Driven (recommended)** — Dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — Execute tasks in this session using `superpowers:executing-plans`, batch execution with checkpoints.

Which approach?
