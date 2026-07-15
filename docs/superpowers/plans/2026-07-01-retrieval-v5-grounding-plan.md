# Community Brain Retrieval v5 — Grounding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stop `gpt-oss:20b` fabricating session dates and citations by (1) recruiting cue-matched chunks into the retrieval candidate pool instead of only re-ranking it, (2) verifying every date/citation in the model's answer against the retrieved context in the Open WebUI filter, and (3) shipping a fabrication-rate evaluation harness — plus three small debt items (speaker-rule last-known-good cache, unresolved-rate alarm, RetryConfig wiring).

**Architecture:** All changes live in the `community-brain/` Python package of `RecapFlow-automation` (plus two prompt/docs files at repo root and one new script in root `scripts/`). A new `query/candidate_injection.py` module derives targeted LanceDB queries from firing cue rules and merges results into `search_chunks`'s pool before the existing boost pass. The single-file Open WebUI filter gains an `outlet` hook with a deterministic grounding verifier. The eval harness reuses the filter's verifier functions so measurement and enforcement can't drift.

**Tech Stack:** Python ≥3.11, FastAPI, LanceDB ≥0.15 (0.30.x API in use), Ollama (`nomic-embed-text` embeddings; `gpt-oss:20b` answering), pytest ≥9, PyYAML, httpx.

**Design doc (normative):** `Patchou-plan/tasks/03-community-brain-grounding/2026-07-01-community-brain-grounding-design.md` (decisions D1–D16 referenced below).

## Global Constraints

- **Work on the VM clone.** All development for this repo happens on the n8n VM (`n8n-automation.patchoutech.lab`) at `~/n8n/` per root `CLAUDE.md` "Development model". The Mac clone (`/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation`) is a read-only mirror — never edit it. Run this session on the VM (or over SSH into it).
- **Branch:** `feature/retrieval-v5-grounding`, cut from up-to-date `main`.
- **Working directory for all Python/test commands:** `~/n8n/community-brain/`.
- **Venv:** `./.venv` (create if missing: `python3 -m venv .venv` then `./.venv/bin/pip install -e ".[dev]"`; Python ≥3.11 required by pyproject). Test command: `./.venv/bin/pytest tests/ -q`. There is no configured linter; match surrounding style. Current suite: 512 passing — it MUST stay green.
- **Shell style (Patchou):** one command per shell invocation. NEVER chain commands with `&&`, `||`, or `;`. Use separate invocations instead. Do not combine `cd` with another command; rely on the session's working directory.
- **Commit style:** repo convention `feat(retrieval): ...`, `fix(openwebui): ...`, `test(ingestion): ...`, `config(community-brain): ...`, `docs(migrations): ...` etc., with footer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- **Env-var reads:** always `os.environ.get("X") or fallback`, never `os.environ.get("X", fallback)` (empty-string clobber defense, per `community-brain/CLAUDE.md`).
- **Test mock boundaries:** LLM at `extractor._call_llm` / `session_extractor._call_llm`; Ollama embed at `ollama.embed`; LanceDB never mocked (use `tmp_path` + real storage); env vars only via `monkeypatch`.
- **Do NOT** touch `community-brain/lancedb/`, do NOT call the live server's `/ingest`, do NOT modify `chunk-extraction-v3.md`, do NOT change the LanceDB schema (37→38-field v1.1 stays), do NOT reintroduce filesystem loading in the filter (it ships as one uploaded file).
- **Invariants that MUST survive** (design §1): trust partition, `verify_corpus_v3_state` fail-closed, additive-only lint auto-path, speaker partition, filter tag position contract, cue-YAML last-known-good semantics, no `/query` contract break (additive fields only).

---

### Task 1: `CueRule.recruit` + `predicate_spec` and YAML loader support

**Files:**
- Modify: `community-brain/src/community_brain/query/cue_rules.py`
- Test: `community-brain/tests/test_cue_rules_recruit.py` (new)

**Interfaces:**
- Consumes: existing `CueRule`, `load_cue_rules_from_yaml`, `build_speaker_auto_rule`.
- Produces: `CueRule` gains fields `recruit: bool = False` and `predicate_spec: dict | None = None`. Loader parses optional `recruit:` on both rule shapes and preserves the raw `target_predicate` mapping in `predicate_spec`. Both speaker auto-rules carry `recruit=True`. Task 2 reads `rule.recruit`, `rule.predicate_spec`.

- [ ] **Step 1: Write the failing tests**

Create `community-brain/tests/test_cue_rules_recruit.py`:

```python
"""v5: recruit flag + predicate_spec preservation on cue rules (design D3)."""
from __future__ import annotations

from community_brain.query.cue_rules import (
    build_speaker_auto_rule,
    load_cue_rules_from_yaml,
)

V4_RULE_YAML = """
cue_rules:
  - name: date_iso_match
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
    recruit: true
"""

V4_RULE_NO_RECRUIT_YAML = """
cue_rules:
  - name: date_iso_match
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
"""

LEGACY_RULE_YAML = """
cue_rules:
  - name: unresolved_questions
    cue_phrases:
      - unresolved
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.04
    recruit: true
"""

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
"""


def test_loader_parses_recruit_flag_on_v4_rule(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(V4_RULE_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert len(rules) == 1
    assert rules[0].recruit is True


def test_loader_recruit_defaults_to_false(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(V4_RULE_NO_RECRUIT_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert rules[0].recruit is False


def test_loader_preserves_predicate_spec_on_legacy_rule(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(LEGACY_RULE_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert rules[0].recruit is True
    assert rules[0].predicate_spec == {"field": "has_unresolved_question", "value": True}
    # legacy predicate callable still built
    assert rules[0].target_predicate is not None
    assert rules[0].target_predicate({"has_unresolved_question": True}) is True


def test_v4_rule_has_no_predicate_spec(tmp_path):
    p = tmp_path / "cues.yaml"
    p.write_text(V4_RULE_YAML)
    rules = load_cue_rules_from_yaml(p)
    assert rules[0].predicate_spec is None


def test_speaker_auto_rules_recruit_by_default(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    spoke, mentioned = build_speaker_auto_rule(p)
    assert spoke.recruit is True
    assert mentioned.recruit is True
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_cue_rules_recruit.py -q`
Expected: FAIL — `TypeError` / `AttributeError` (`CueRule` has no `recruit` attribute).

- [ ] **Step 3: Implement**

In `community-brain/src/community_brain/query/cue_rules.py`:

(a) Extend the dataclass (currently the `CueRule` definition around line 259):

```python
@dataclass(frozen=True)
class CueRule:
    name: str
    cue_phrases: tuple[str, ...]
    target_predicate: Callable[[dict], bool] | None
    delta: float
    # v4 additions (all optional for backward compat):
    question_regex: str | None = None
    match_field: str | None = None
    match_strategy: str | None = None
    # v5 additions (design D3): recruitment opt-in + the raw YAML
    # target_predicate mapping, preserved so candidate_injection can derive
    # a WHERE clause from the same definition the boost predicate uses.
    recruit: bool = False
    predicate_spec: dict | None = None
```

(b) In `load_cue_rules_from_yaml`, in the v4 branch (`if has_qr and has_ms:`), add `recruit`:

```python
            if has_qr and has_ms:
                rules.append(CueRule(
                    name=name,
                    cue_phrases=(),
                    target_predicate=None,
                    delta=delta,
                    question_regex=entry["question_regex"],
                    match_field=entry.get("match_field"),
                    match_strategy=entry["match_strategy"],
                    recruit=bool(entry.get("recruit", False)),
                ))
                continue
```

(c) In the legacy branch, replace the final `rules.append(...)` with:

```python
            cue_phrases = tuple(raw_phrases)
            predicate = _build_predicate(entry["target_predicate"])
            rules.append(CueRule(
                name=name,
                cue_phrases=cue_phrases,
                target_predicate=predicate,
                delta=delta,
                recruit=bool(entry.get("recruit", False)),
                predicate_spec=dict(entry["target_predicate"]),
            ))
```

(d) In `build_speaker_auto_rule`, add `recruit=True` to all four `CueRule(...)` constructions (the two never-match sentinels and the two real rules). Example for the real `spoke` rule:

```python
    spoke = CueRule(
        name="speaker_auto_spoke",
        cue_phrases=(),
        target_predicate=None,
        delta=0.04,
        question_regex=pattern,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
        recruit=True,
    )
```

Apply the same `recruit=True` line to `mentioned`, and to both sentinel rules in the empty-registry branch.

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_cue_rules_recruit.py -q`
Expected: 5 passed.

- [ ] **Step 5: Run the full cue-rules suites (regression)**

Run: `./.venv/bin/pytest tests/test_cue_rules.py tests/test_cue_rules_match_strategies.py tests/test_cue_rules_speaker_auto.py -q`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/query/cue_rules.py community-brain/tests/test_cue_rules_recruit.py
```
```bash
git commit -m "feat(retrieval): add recruit flag + predicate_spec to cue rules (v5 D3)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: Recruitment-query derivation (`build_recruitment_query`)

**Files:**
- Create: `community-brain/src/community_brain/query/candidate_injection.py`
- Test: `community-brain/tests/test_candidate_injection.py` (new)

**Interfaces:**
- Consumes: `CueRule` (with `recruit`, `predicate_spec` from Task 1); `cue_rules` module-level speaker resolver dicts (accessed via module attribute, NOT `from`-imported — they are rebound on refresh).
- Produces: `RecruitmentSpec(rule_name: str, where: str | None, fts_text: str | None)` (frozen dataclass) and `build_recruitment_query(rule: CueRule, question: str) -> RecruitmentSpec | None`. Constants `INJECT_PER_RULE = 10`, `MAX_INJECTED_TOTAL = 30`. Task 3 adds `inject_candidates` to this module.

- [ ] **Step 1: Write the failing tests**

Create `community-brain/tests/test_candidate_injection.py`:

```python
"""v5 cue-driven candidate injection: recruitment-query derivation (design D4)."""
from __future__ import annotations

from community_brain.query.candidate_injection import (
    RecruitmentSpec,
    build_recruitment_query,
)
from community_brain.query.cue_rules import CueRule, build_speaker_auto_rule

ISO_RULE = CueRule(
    name="date_iso_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
    match_field="session_date", match_strategy="iso_date_equals", recruit=True,
)

MONTH_RULE = CueRule(
    name="date_month_year_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
    match_field="session_date", match_strategy="month_year_overlap", recruit=True,
)

QUARTER_RULE = CueRule(
    name="date_quarter_match", cue_phrases=(), target_predicate=None, delta=0.04,
    question_regex=r"\b(Q[1-4])\s+(\d{4})\b",
    match_field="bm25_text", match_strategy="token_overlap", recruit=True,
)

LEGACY_BOOL_RULE = CueRule(
    name="unresolved_questions", cue_phrases=("unresolved",), target_predicate=None,
    delta=0.04, recruit=True,
    predicate_spec={"field": "has_unresolved_question", "value": True},
)

LEGACY_NON_EMPTY_RULE = CueRule(
    name="decisions", cue_phrases=("decision",), target_predicate=None,
    delta=0.008, recruit=True,
    predicate_spec={"field": "decisions", "check": "non_empty"},
)

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
"""


def test_non_recruit_rule_returns_none():
    rule = CueRule(
        name="x", cue_phrases=(), target_predicate=None, delta=0.04,
        question_regex=r"\b(\d{4}-\d{2}-\d{2})\b",
        match_field="session_date", match_strategy="iso_date_equals", recruit=False,
    )
    assert build_recruitment_query(rule, "what happened on 2025-12-30?") is None


def test_iso_date_rule_derives_equality_where():
    spec = build_recruitment_query(ISO_RULE, "What was discussed on 2025-12-30?")
    assert spec == RecruitmentSpec(
        rule_name="date_iso_match",
        where="session_date = '2025-12-30'",
        fts_text=None,
    )


def test_iso_date_rule_none_when_question_has_no_date():
    assert build_recruitment_query(ISO_RULE, "What did Adam say?") is None


def test_month_year_rule_derives_range_where():
    spec = build_recruitment_query(MONTH_RULE, "What happened in December 2025?")
    assert spec is not None
    assert spec.where == (
        "session_date >= '2025-12-01' AND session_date <= '2025-12-31'"
    )
    assert spec.fts_text is None


def test_token_overlap_rule_recruits_via_fts_token():
    spec = build_recruitment_query(QUARTER_RULE, "themes in Q1 2026 calls?")
    assert spec is not None
    assert spec.where is None
    assert spec.fts_text == "Q1-2026"


def test_speaker_rule_derives_array_has_where(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    spoke, _mentioned = build_speaker_auto_rule(p)
    spec = build_recruitment_query(spoke, "What did Adam say about pricing?")
    assert spec is not None
    assert spec.where == (
        "(array_has(speakers_spoke, 'Adam') OR array_has(speakers_spoke, 'Adam James'))"
    )


def test_legacy_bool_predicate_derives_equality_where():
    spec = build_recruitment_query(LEGACY_BOOL_RULE, "what stayed unresolved?")
    assert spec is not None
    assert spec.where == "has_unresolved_question = true"
    assert spec.fts_text is None


def test_legacy_bool_rule_none_when_no_phrase_match():
    assert build_recruitment_query(LEGACY_BOOL_RULE, "what was decided?") is None


def test_legacy_non_empty_predicate_is_not_recruitable():
    assert build_recruitment_query(LEGACY_NON_EMPTY_RULE, "what decisions happened?") is None


def test_where_values_are_sql_quoted():
    rule = CueRule(
        name="q", cue_phrases=("about",), target_predicate=None, delta=0.01,
        recruit=True, predicate_spec={"field": "stance", "value": "o'brien"},
    )
    spec = build_recruitment_query(rule, "tell me about stances")
    assert spec is not None
    assert spec.where == "stance = 'o''brien'"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_candidate_injection.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'community_brain.query.candidate_injection'`.

- [ ] **Step 3: Implement the module**

Create `community-brain/src/community_brain/query/candidate_injection.py`:

```python
"""Cue-driven candidate injection (v5).

Cue boosts re-rank the fixed candidate pool of top_k * OVERSAMPLE_FACTOR;
they cannot rescue chunks whose base hybrid relevance is too weak to enter
the pool (the v4 pool-limit finding). This module recruits candidates
directly: for each firing cue rule with recruit=True, it derives a targeted
LanceDB query from the rule's own match definition and merges the results
into the candidate pool BEFORE the boost pass prices them.

Design: Patchou-plan tasks/03 2026-07-01-community-brain-grounding-design.md
§D2-D7. Recruitment always ANDs the caller's WHERE (success guard + user
filters) so injection can never leak filtered-out or failed chunks.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

# Module import (not from-import): the speaker resolver dicts inside
# cue_rules are REBOUND by _refresh_speaker_resolver on every registry
# reload. A from-import would freeze a stale reference.
from community_brain.query import cue_rules as _cue_rules
from community_brain.query.cue_rules import CueRule, cue_phrase_matches

logger = logging.getLogger(__name__)

# Per-rule recruitment budget: how many chunks one firing rule may pull
# into the candidate pool.
INJECT_PER_RULE = 10

# Hard cap on total injected candidates per query, across all firing rules.
# Bounds worst-case pool growth and per-query latency.
MAX_INJECTED_TOTAL = 30


def _sql_quote(value: str) -> str:
    """SQL-standard single-quote doubling. Mirrors query_local.sql_quote;
    duplicated (one line) because query_local imports this module and the
    reverse import would be circular.
    """
    return value.replace("'", "''")


@dataclass(frozen=True)
class RecruitmentSpec:
    """A targeted recruitment query derived from one firing cue rule.

    where: LanceDB WHERE fragment selecting chunks the rule targets, or None.
    fts_text: override text for the FTS leg (token_overlap recruits by the
        date token itself — the question's other words are noise), or None
        to search with the original question.
    """
    rule_name: str
    where: str | None
    fts_text: str | None


def build_recruitment_query(rule: CueRule, question: str) -> RecruitmentSpec | None:
    """Derive a recruitment query for `rule` against `question`.

    Returns None when the rule is not recruit-enabled, does not fire on the
    question, or has no strategy with a derivable targeted predicate
    (legacy non_empty/contains checks stay boost-only — no portable
    LanceDB SQL for list-column membership).
    """
    if not rule.recruit:
        return None

    # v4 shape: question_regex + match_strategy
    if rule.question_regex is not None and rule.match_strategy is not None:
        try:
            m = re.search(rule.question_regex, question, flags=re.IGNORECASE)
        except re.error as exc:
            logger.warning(
                "recruitment: rule %r regex failed to compile: %s", rule.name, exc
            )
            return None
        if not m:
            return None

        if rule.match_strategy == "iso_date_equals":
            captured = m.group(1) if m.lastindex else m.group(0)
            return RecruitmentSpec(
                rule_name=rule.name,
                where=f"{rule.match_field} = '{_sql_quote(captured)}'",
                fts_text=None,
            )

        if rule.match_strategy == "month_year_overlap":
            if not m.lastindex or m.lastindex < 2:
                return None
            month_name = m.group(1).capitalize()
            year = m.group(2)
            month_num = _cue_rules._MONTH_TO_NUM.get(month_name)
            if month_num is None:
                return None
            prefix = f"{year}-{month_num}"
            return RecruitmentSpec(
                rule_name=rule.name,
                where=(
                    f"{rule.match_field} >= '{_sql_quote(prefix)}-01' "
                    f"AND {rule.match_field} <= '{_sql_quote(prefix)}-31'"
                ),
                fts_text=None,
            )

        if rule.match_strategy == "token_overlap":
            if not m.lastindex:
                return None
            captures = [m.group(i) for i in range(1, m.lastindex + 1) if m.group(i)]
            if not captures:
                return None
            token = "-".join(captures)
            # bm25_text token membership is exactly what the FTS index
            # answers; recruit by searching the token itself.
            return RecruitmentSpec(rule_name=rule.name, where=None, fts_text=token)

        if rule.match_strategy == "name_resolve_then_check":
            captured = m.group(1) if m.lastindex else m.group(0)
            canonical = _cue_rules._SPEAKER_CASEFOLD_LOOKUP.get(captured.casefold())
            if canonical is None:
                return None
            names = sorted(
                n
                for n, c in _cue_rules._SPEAKER_NAME_TO_CANONICAL.items()
                if c == canonical
            )
            if not names:
                return None
            clauses = " OR ".join(
                f"array_has({rule.match_field}, '{_sql_quote(n)}')" for n in names
            )
            return RecruitmentSpec(
                rule_name=rule.name, where=f"({clauses})", fts_text=None
            )

        logger.warning(
            "recruitment: unknown strategy %r on rule %r", rule.match_strategy, rule.name
        )
        return None

    # Legacy shape: cue_phrases + predicate_spec
    if not rule.cue_phrases or not cue_phrase_matches(question, rule.cue_phrases):
        return None
    spec = rule.predicate_spec
    if not spec or "field" not in spec:
        return None
    if "value" in spec and "check" not in spec:
        field_name = spec["field"]
        value = spec["value"]
        if isinstance(value, bool):
            return RecruitmentSpec(
                rule_name=rule.name,
                where=f"{field_name} = {'true' if value else 'false'}",
                fts_text=None,
            )
        if isinstance(value, str):
            return RecruitmentSpec(
                rule_name=rule.name,
                where=f"{field_name} = '{_sql_quote(value)}'",
                fts_text=None,
            )
    return None
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_candidate_injection.py -q`
Expected: 10 passed.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/candidate_injection.py community-brain/tests/test_candidate_injection.py
```
```bash
git commit -m "feat(retrieval): derive per-strategy recruitment queries from cue rules (v5 D4)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 3: `inject_candidates` — run recruitment against LanceDB

**Files:**
- Modify: `community-brain/src/community_brain/query/candidate_injection.py`
- Test: `community-brain/tests/test_candidate_injection.py` (append)

**Interfaces:**
- Consumes: `build_recruitment_query` (Task 2); `query_local._cosine_distance` via function-level import (avoids the module-level circular import — `query_local` imports this module in Task 4).
- Produces: `inject_candidates(*, question: str, table, rules: tuple[CueRule, ...], where_expr: str, existing_chunk_ids: set[str], query_vector: list[float]) -> list[dict]`. Each returned row is a full chunk row dict plus `_rrf_score` (0.0), `_distance`, `_vector_similarity`, `_injected_by: list[str]`. Task 4 merges these into `search_chunks`'s candidate list.

- [ ] **Step 1: Write the failing tests**

Append to `community-brain/tests/test_candidate_injection.py`:

```python
# ---------------------------------------------------------------------------
# inject_candidates (real LanceDB, tmp_path storage — never mocked)
# ---------------------------------------------------------------------------
import datetime as dt

import lancedb

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema
from community_brain.query.candidate_injection import (
    INJECT_PER_RULE,
    MAX_INJECTED_TOTAL,
    inject_candidates,
)
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index


def _chunk_row(
    *,
    chunk_id: str,
    session_date: str,
    full_text: str = "generic content",
    bm25_text: str = "generic content",
    extraction_status: str = "success",
    has_unresolved_question: bool = False,
    speakers_spoke: list[str] | None = None,
    embedding: list[float] | None = None,
) -> dict:
    return {
        "schema_version": "1.1",
        "chunk_id": chunk_id,
        "session_id": session_date,
        "session_date": session_date,
        "session_title": None,
        "content_type": "prepared_transcript",
        "source_file": "test.md",
        "chunk_index": 0,
        "total_chunks_in_source": 1,
        "speakers_spoke": speakers_spoke or [],
        "speakers_mentioned": [],
        "entities": [],
        "keywords": [],
        "topic_label": "t",
        "session_themes": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "corpus_derived_markers": [],
        "corpus_markers_computed_at": None,
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": has_unresolved_question,
        "has_insight": False,
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
        "extraction_model": "test-model",
        "extraction_prompt_version": "chunk-extraction-v3",
        "extraction_status": extraction_status,
        "extraction_error": None,
        "extracted_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "embed_text": "x",
        "full_text": full_text,
        "bm25_text": bm25_text,
        "embedding": embedding if embedding is not None else [0.1] * EMBEDDING_DIM,
    }


def _make_table(tmp_path, rows):
    db = lancedb.connect(str(tmp_path / "db"))
    table = db.create_table("chunks", schema=pyarrow_table_schema())
    table.add(rows)
    ensure_fts_index(table, "bm25_text")
    optimize_fts_index(table, "bm25_text")
    return table


SUCCESS_GUARD = "extraction_status = 'success'"
QUERY_VEC = [0.5] * EMBEDDING_DIM


def test_inject_recruits_quiet_session_by_iso_date(tmp_path):
    rows = [
        _chunk_row(chunk_id="q1", session_date="2025-12-30",
                   full_text="holiday call check-ins",
                   bm25_text="holiday call check-ins"),
        _chunk_row(chunk_id="q2", session_date="2025-12-30",
                   full_text="year wrap-up thread",
                   bm25_text="year wrap-up thread"),
        _chunk_row(chunk_id="other", session_date="2026-01-07"),
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    ids = sorted(r["chunk_id"] for r in injected)
    assert ids == ["q1", "q2"]
    for r in injected:
        assert r["_rrf_score"] == 0.0
        assert r["_injected_by"] == ["date_iso_match"]
        assert "_distance" in r
        assert "_vector_similarity" in r


def test_inject_excludes_failed_extractions(tmp_path):
    rows = [
        _chunk_row(chunk_id="ok", session_date="2025-12-30"),
        _chunk_row(chunk_id="bad", session_date="2025-12-30",
                   extraction_status="failed"),
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert [r["chunk_id"] for r in injected] == ["ok"]


def test_inject_dedups_against_existing_pool(tmp_path):
    rows = [
        _chunk_row(chunk_id="q1", session_date="2025-12-30"),
        _chunk_row(chunk_id="q2", session_date="2025-12-30"),
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids={"q1"},
        query_vector=QUERY_VEC,
    )
    assert [r["chunk_id"] for r in injected] == ["q2"]


def test_inject_accumulates_rule_names_on_shared_recruit(tmp_path):
    month_and_iso = (ISO_RULE, MONTH_RULE)
    rows = [_chunk_row(chunk_id="q1", session_date="2025-12-30")]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30, in December 2025?",
        table=table,
        rules=month_and_iso,
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert len(injected) == 1
    assert injected[0]["_injected_by"] == ["date_iso_match", "date_month_year_match"]


def test_inject_respects_per_rule_budget(tmp_path):
    rows = [
        _chunk_row(chunk_id=f"c{i:02d}", session_date="2025-12-30")
        for i in range(MAX_INJECTED_TOTAL + 10)
    ]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="What was discussed on 2025-12-30?",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert 0 < len(injected) <= INJECT_PER_RULE


def test_inject_returns_empty_when_no_rule_fires(tmp_path):
    rows = [_chunk_row(chunk_id="q1", session_date="2025-12-30")]
    table = _make_table(tmp_path, rows)
    injected = inject_candidates(
        question="Tell me about onboarding.",
        table=table,
        rules=(ISO_RULE,),
        where_expr=SUCCESS_GUARD,
        existing_chunk_ids=set(),
        query_vector=QUERY_VEC,
    )
    assert injected == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_candidate_injection.py -q`
Expected: new tests FAIL with `ImportError: cannot import name 'inject_candidates'`; Task 2's tests still pass.

- [ ] **Step 3: Implement `inject_candidates`**

Append to `community-brain/src/community_brain/query/candidate_injection.py`:

```python
def inject_candidates(
    *,
    question: str,
    table,
    rules: tuple[CueRule, ...],
    where_expr: str,
    existing_chunk_ids: set[str],
    query_vector: list[float],
) -> list[dict]:
    """Run recruitment for every firing recruit-enabled rule; return
    normalized rows not already in the pool.

    Every returned row carries:
      _rrf_score = 0.0            (no base hybrid signal; the downstream
                                   boost pass prices it via the rules)
      _distance / _vector_similarity  (cosine vs the query vector so the
                                   public `similarity` keeps spec §7.2
                                   semantics)
      _injected_by = [rule names that recruited it]

    Per-rule flow: FTS query (fts_text or the question) over bm25_text with
    (<rule where>) AND <where_expr>, limit INJECT_PER_RULE. If the FTS leg
    errors or finds nothing and the rule has a hard WHERE, fall back to a
    plain filtered scan — a quiet session may share zero lexical tokens
    with the question; that pathological case is this feature's reason to
    exist. Total injections are capped at MAX_INJECTED_TOTAL.
    """
    # Function-level import: query_local imports this module at module
    # level; importing back at module level would be circular.
    from community_brain.query.query_local import _cosine_distance

    injected: dict[str, dict] = {}
    for rule in rules:
        if len(injected) >= MAX_INJECTED_TOTAL:
            logger.warning(
                "recruitment: MAX_INJECTED_TOTAL=%d reached; remaining rules skipped",
                MAX_INJECTED_TOTAL,
            )
            break
        spec = build_recruitment_query(rule, question)
        if spec is None:
            continue
        combined_where = (
            f"({spec.where}) AND {where_expr}" if spec.where else where_expr
        )
        fts_query = spec.fts_text if spec.fts_text is not None else question
        rows: list[dict] = []
        try:
            rows = (
                table.search(fts_query, query_type="fts", fts_columns="bm25_text")
                .where(combined_where)
                .limit(INJECT_PER_RULE)
                .to_arrow()
                .to_pylist()
            )
        except Exception as exc:
            # Transient: recruitment is additive best-effort; the base
            # hybrid results are unaffected. Fall through to the scan path.
            logger.warning(
                "recruitment: FTS query for rule %r failed (%r); trying filtered scan",
                rule.name,
                exc,
            )
            rows = []
        if not rows and spec.where is not None:
            try:
                rows = (
                    table.search()
                    .where(combined_where)
                    .limit(INJECT_PER_RULE)
                    .to_arrow()
                    .to_pylist()
                )
            except Exception as exc:
                logger.warning(
                    "recruitment: filtered scan for rule %r failed (%r); skipping rule",
                    rule.name,
                    exc,
                )
                rows = []
        for row in rows:
            if len(injected) >= MAX_INJECTED_TOTAL:
                break
            chunk_id = row.get("chunk_id") or ""
            if not chunk_id or chunk_id in existing_chunk_ids:
                continue
            if chunk_id in injected:
                injected[chunk_id]["_injected_by"].append(rule.name)
                continue
            row["_rrf_score"] = 0.0
            embedding = row.get("embedding")
            if embedding:
                row["_distance"] = _cosine_distance(query_vector, list(embedding))
            else:
                row["_distance"] = 0.0
            row["_vector_similarity"] = 1.0 - float(row["_distance"])
            row["_injected_by"] = [rule.name]
            injected[chunk_id] = row
    return list(injected.values())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_candidate_injection.py -q`
Expected: 16 passed.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/candidate_injection.py community-brain/tests/test_candidate_injection.py
```
```bash
git commit -m "feat(retrieval): inject_candidates recruits cue-matched chunks from LanceDB (v5 D5-D7)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 4: Wire injection into `search_chunks`; expose `injected_by` in `score_breakdown`

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py`
- Modify: `community-brain/src/community_brain/query/retrieval_server.py` (ScoreBreakdown model + population)
- Modify: `community-brain/tests/fixtures/golden_corpus/seed.py` (quiet-session fixtures)
- Test: `community-brain/tests/test_injection_integration.py` (new)

**Interfaces:**
- Consumes: `inject_candidates` (Task 3).
- Produces: `search_chunks` return shape unchanged except each chunk's `score_breakdown` dict gains `"injected_by": list[str]`. `/query` response `ScoreBreakdown` gains `injected_by: list[str] = []` (additive). Golden seed gains rows `v5-quiet-1`, `v5-quiet-2` (session `2025-12-30`).

- [ ] **Step 1: Add the quiet-session fixtures to the golden seed**

In `community-brain/tests/fixtures/golden_corpus/seed.py`, inside the `rows = [...]` list in `seed()`, immediately after the `f7-prior-1` entry, add:

```python
        # --- v5 injection fixtures: a quiet session invisible to both
        # hybrid legs. session_date carries the date; bm25_text deliberately
        # holds NO date tokens and no vocabulary shared with any golden
        # query; the embedding sits far from the constant 0.5 query vector.
        # Pre-v5 these chunks cannot enter the candidate pool on a date
        # query — only cue-driven recruitment can surface them.
        _row(13, "v5-quiet-1", "2025-12-30",
             "brief seasonal gathering with informal catch-ins on sabbatical intentions",
             bm25_text="brief seasonal gathering informal catch-ins sabbatical intentions",
             embedding=[0.9] * EMBEDDING_DIM),
        _row(14, "v5-quiet-2", "2025-12-30",
             "closing remarks regarding upcoming sabbaticals and reduced cadence",
             bm25_text="closing remarks upcoming sabbaticals reduced cadence",
             embedding=[0.9] * EMBEDDING_DIM),
```

Note: `_row()` already accepts arbitrary `**overrides`, and `EMBEDDING_DIM` is already imported at the top of `seed.py`. No other change to the file.

- [ ] **Step 2: Run the golden suite to prove the fixtures don't perturb it**

Run: `./.venv/bin/pytest tests/test_golden_queries.py -q`
Expected: all pass. If any golden query regresses, the new fixture vocabulary collided with an existing query — change the fixture words (keep them free of date tokens and cue phrases), not the retrieval code.

- [ ] **Step 3: Write the failing integration tests**

Create `community-brain/tests/test_injection_integration.py`:

```python
"""End-to-end cue-driven injection through search_chunks (v5 D2, D6, D7).

Seeds the golden corpus, points COMMUNITY_BRAIN_CUE_RULES_PATH at a
recruit-enabled cue YAML, and proves a quiet session invisible to both
hybrid legs is recruited into top_k — and missed without recruitment
(the pool-limit finding reproduced in miniature).
"""
from __future__ import annotations

import sys
from pathlib import Path

import lancedb
import pytest

from community_brain.ingestion.schema import EMBEDDING_DIM
from community_brain.query.fts_lifecycle import ensure_fts_index, optimize_fts_index
from community_brain.query.query_local import search_chunks

FIXTURES_DIR = Path(__file__).parent / "fixtures"

RECRUIT_CUES_YAML = """
cue_rules:
  - name: date_iso_match
    question_regex: '\\b(\\d{4}-\\d{2}-\\d{2})\\b'
    match_field: session_date
    match_strategy: iso_date_equals
    delta: 0.04
    recruit: true
"""

QUESTION = "What was discussed on 2025-12-30?"


@pytest.fixture()
def injection_db(tmp_path):
    sys.path.insert(0, str(FIXTURES_DIR / "golden_corpus"))
    from seed import seed  # type: ignore

    db_path = tmp_path / "golden_db"
    seed(str(db_path))
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    ensure_fts_index(table, "bm25_text")
    optimize_fts_index(table, "bm25_text")
    return str(db_path)


@pytest.fixture()
def recruit_cues(tmp_path, monkeypatch):
    p = tmp_path / "query-cues.yaml"
    p.write_text(RECRUIT_CUES_YAML)
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(p))
    monkeypatch.setenv(
        "COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH", str(tmp_path / "missing-aliases.yaml")
    )


@pytest.fixture()
def boost_only_cues(tmp_path, monkeypatch):
    p = tmp_path / "query-cues-boost-only.yaml"
    p.write_text(RECRUIT_CUES_YAML.replace("\n    recruit: true", ""))
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(p))
    monkeypatch.setenv(
        "COMMUNITY_BRAIN_SPEAKER_ALIASES_PATH", str(tmp_path / "missing-aliases.yaml")
    )


@pytest.fixture()
def fake_embed(monkeypatch):
    def _embed(model, input):
        return {"embeddings": [[0.5] * EMBEDDING_DIM]}

    import ollama

    monkeypatch.setattr(ollama, "embed", _embed)


def test_iso_date_query_recruits_quiet_session(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    ids = [c["chunk_id"] for c in result["chunks"]]
    assert "v5-quiet-1" in ids
    assert "v5-quiet-2" in ids


def test_quiet_session_missed_without_recruit(injection_db, boost_only_cues, fake_embed):
    """The pool-limit finding: the same rule as boost-only cannot rescue
    chunks that never entered the candidate pool."""
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    ids = [c["chunk_id"] for c in result["chunks"]]
    assert "v5-quiet-1" not in ids
    assert "v5-quiet-2" not in ids


def test_injected_chunks_report_injected_by(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    by_id = {c["chunk_id"]: c for c in result["chunks"]}
    quiet = by_id["v5-quiet-1"]
    assert quiet["score_breakdown"]["injected_by"] == ["date_iso_match"]
    assert quiet["score_breakdown"]["rrf_score"] == 0.0
    assert quiet["score_breakdown"]["cue_delta"] == pytest.approx(0.04)
    assert "date_iso_match" in quiet["score_breakdown"]["cue_rules_fired"]


def test_pool_native_chunks_report_empty_injected_by(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION, db_path=injection_db, top_k=5, filters=None
    )
    natives = [
        c for c in result["chunks"] if c["chunk_id"] not in ("v5-quiet-1", "v5-quiet-2")
    ]
    assert natives, "expected some pool-native chunks in top_k"
    for c in natives:
        assert c["score_breakdown"]["injected_by"] == []


def test_injection_respects_user_filters(injection_db, recruit_cues, fake_embed):
    result = search_chunks(
        question=QUESTION,
        db_path=injection_db,
        top_k=5,
        filters={"session_date_range": ["2026-01-01", "2026-12-31"]},
    )
    ids = [c["chunk_id"] for c in result["chunks"]]
    assert "v5-quiet-1" not in ids
    assert "v5-quiet-2" not in ids
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_injection_integration.py -q`
Expected: `test_iso_date_query_recruits_quiet_session`, `test_injected_chunks_report_injected_by`, `test_pool_native_chunks_report_empty_injected_by` FAIL (quiet chunks absent / `injected_by` KeyError). The two negative tests may already pass.

- [ ] **Step 5: Wire injection into `search_chunks`**

In `community-brain/src/community_brain/query/query_local.py`:

(a) Add the import (with the existing cue_rules imports at the top):

```python
from community_brain.query.candidate_injection import inject_candidates
```

(b) Locate the end of the candidate-normalization loop (the line `candidates.append(row)`) and the block that follows it (the BM25-only rank query). Insert BETWEEN them:

```python
    # --- v5 cue-driven candidate injection (design D2) ---
    # Rules are resolved here (moved up from the boost step) so the same
    # rule set drives recruitment and boosting for this request.
    rules = _resolve_cue_rules()

    if _use_hybrid:
        injected = inject_candidates(
            question=question,
            table=table,
            rules=rules,
            where_expr=where_expr,
            existing_chunk_ids={c.get("chunk_id", "") for c in candidates},
            query_vector=list(query_vector),
        )
        if injected:
            fired = sorted(
                {name for c in injected for name in c.get("_injected_by", [])}
            )
            logger.info(
                "cue-driven injection recruited %d candidate(s) via %s",
                len(injected),
                fired,
            )
            candidates.extend(injected)
```

(c) Delete the now-duplicate `rules = _resolve_cue_rules()` line that currently sits immediately before `boosted = apply_cue_boosts(...)`. The boost call itself stays exactly as is (`boosted = apply_cue_boosts(question, candidates, rules=rules)`).

(d) In the `score_breakdown` construction loop, add the `injected_by` key:

```python
    for chunk in top_k_chunks:
        chunk["score_breakdown"] = {
            "vector_similarity": chunk.get("_vector_similarity", 0.0),
            "bm25_rank": chunk.get("_bm25_rank"),
            "rrf_score": chunk.get("_rrf_score_pre_boost", 0.0),
            "cue_delta": chunk.get("_cue_delta", 0.0),
            "cue_rules_fired": chunk.get("_cue_rules_fired", []),
            "injected_by": chunk.get("_injected_by", []),
        }
```

(e) Update the `search_chunks` docstring pipeline description — replace the numbered pipeline list with:

```python
    Pipeline (spec §3.1 + v5 injection):
      1. Embed `question` via Ollama (nomic-embed-text).
      2. LanceDB hybrid query: RRF(vector, BM25 on bm25_text), oversampled
         by OVERSAMPLE_FACTOR.
      3. WHERE clause: extraction_status = 'success' AND caller's filters.
      4. v5: cue-driven candidate injection — firing recruit-enabled cue
         rules pull targeted chunks (same WHERE) into the pool.
      5. Cue boost re-ranks the merged pool; truncate to top_k.
```

- [ ] **Step 6: Expose `injected_by` in the `/query` response model**

In `community-brain/src/community_brain/query/retrieval_server.py`:

(a) In `class ScoreBreakdown`, after the `cue_rules_fired` field, add:

```python
    injected_by: list[str] = Field(default_factory=list)
```

and append to its docstring bullet list:

```python
    - injected_by: names of v5 recruitment rules that pulled this chunk
      into the candidate pool (empty for pool-native chunks)
```

(b) In the `query()` handler where `ScoreBreakdown` is constructed, add the field:

```python
        score_breakdown = ScoreBreakdown(
            vector_similarity=_sb_data.get("vector_similarity", 0.0),
            bm25_rank=_sb_data.get("bm25_rank"),
            rrf_score=_sb_data.get("rrf_score", 0.0),
            cue_delta=_sb_data.get("cue_delta", 0.0),
            cue_rules_fired=_sb_data.get("cue_rules_fired") or [],
            injected_by=_sb_data.get("injected_by") or [],
        )
```

- [ ] **Step 7: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_injection_integration.py -q`
Expected: 5 passed.

- [ ] **Step 8: Full regression**

Run: `./.venv/bin/pytest tests/ -q`
Expected: all pass (512 pre-existing + new). Pay attention to `test_golden_queries.py`, `test_query_local.py`, `test_search_hybrid.py`, `test_retrieval_server_query_v2.py` — any failure there is a regression you introduced, not a flake.

- [ ] **Step 9: Commit**

```bash
git add community-brain/src/community_brain/query/query_local.py community-brain/src/community_brain/query/retrieval_server.py community-brain/tests/fixtures/golden_corpus/seed.py community-brain/tests/test_injection_integration.py
```
```bash
git commit -m "feat(retrieval): merge recruited candidates into search pool pre-boost; expose injected_by (v5 D2,D6)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 5: Speaker auto-rule last-known-good cache

**Files:**
- Modify: `community-brain/src/community_brain/query/cue_rules.py`
- Test: `community-brain/tests/test_speaker_auto_lkg.py` (new)

**Interfaces:**
- Consumes: existing `build_speaker_auto_rule`, `_refresh_speaker_resolver`.
- Produces: module-level `_LAST_GOOD_SPEAKER_RULES: dict[str, tuple[tuple[CueRule, CueRule], dict[str, str], dict[str, str]]]`. `build_speaker_auto_rule` returns cached rules AND restores the resolver dicts when a previously-good path loads empty. No signature change.

- [ ] **Step 1: Write the failing tests**

Create `community-brain/tests/test_speaker_auto_lkg.py`:

```python
"""Last-known-good cache for speaker auto-rules (v5 D12).

The cue-rules YAML loader already survives transient edit windows via
_LAST_GOOD_RULES; build_speaker_auto_rule did not — a partial write to
speaker-aliases.yaml silently degraded speaker boosts to never-match for
that request. The cache must restore the resolver dicts too, since
name_resolve_then_check resolves through module-level state.
"""
from __future__ import annotations

from community_brain.query import cue_rules

ALIASES_YAML = """
aliases:
  Adam James:
    - Adam
  Garron Selliken:
    - Garron
"""


def test_lkg_returns_cached_rules_after_corrupt_rewrite(tmp_path):
    p = tmp_path / "speaker-aliases.yaml"
    p.write_text(ALIASES_YAML)
    first = cue_rules.build_speaker_auto_rule(p)
    assert "Adam" in (first[0].question_regex or "")

    # Simulate a partial-write window: the file is momentarily unparseable.
    p.write_text("aliases: [unclosed")
    second = cue_rules.build_speaker_auto_rule(p)

    assert second == first
    # The resolver dicts survived too — not just the rule objects.
    assert cue_rules._SPEAKER_CASEFOLD_LOOKUP.get("adam") == "Adam James"
    assert cue_rules._SPEAKER_NAME_TO_CANONICAL.get("Garron") == "Garron Selliken"


def test_first_time_empty_registry_still_returns_never_match(tmp_path):
    p = tmp_path / "empty-aliases.yaml"
    p.write_text("aliases: {}\n")
    spoke, mentioned = cue_rules.build_speaker_auto_rule(p)
    assert spoke.question_regex == r"(?!x)x"
    assert mentioned.question_regex == r"(?!x)x"


def test_lkg_is_per_path(tmp_path):
    good = tmp_path / "good.yaml"
    good.write_text(ALIASES_YAML)
    cue_rules.build_speaker_auto_rule(good)

    other = tmp_path / "other.yaml"
    other.write_text("aliases: [unclosed")
    spoke, _ = cue_rules.build_speaker_auto_rule(other)
    # No prior good load for THIS path -> never-match, not the good cache.
    assert spoke.question_regex == r"(?!x)x"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_speaker_auto_lkg.py -q`
Expected: `test_lkg_returns_cached_rules_after_corrupt_rewrite` FAILS (second call returns never-match sentinels). The other two pass already — that's fine; they lock current behavior.

- [ ] **Step 3: Implement the cache**

In `community-brain/src/community_brain/query/cue_rules.py`:

(a) Above `build_speaker_auto_rule`, add:

```python
# Last-known-good cache for the speaker auto-rules, keyed by resolved path.
# Stores (rule_pair, name_to_canonical snapshot, casefold snapshot) so a
# transient partial-write window on speaker-aliases.yaml cannot degrade
# speaker boosts/recruitment to never-match sentinels for that request
# (v5 D12; mirrors _LAST_GOOD_RULES semantics for the YAML loader).
_LAST_GOOD_SPEAKER_RULES: dict[
    str,
    tuple[tuple["CueRule", "CueRule"], dict[str, str], dict[str, str]],
] = {}
```

(b) Replace the body of `build_speaker_auto_rule` after `aliases_map = _refresh_speaker_resolver(path)` so the full function reads:

```python
def build_speaker_auto_rule(path: str | Path) -> tuple["CueRule", "CueRule"]:
    """Synthesize the speaker auto-rules from the alias registry.

    Builds a regex with all canonical names and aliases, longest-first so
    multi-word names match before single-word alternatives.

    Returns a tuple of TWO rules sharing the same regex:
      - 'speaker_auto_spoke' (match_field=speakers_spoke, delta=0.04)
      - 'speaker_auto_mentioned' (match_field=speakers_mentioned, delta=0.02)

    Both use match_strategy='name_resolve_then_check' which respects the
    match_field -- only checks that one field for the canonical's group.

    Resilience (v5 D12): when a previously-good path loads empty (missing,
    unparseable, or transiently truncated), the last-known-good rule pair
    is returned and the module-level resolver dicts are restored from the
    cached snapshot. First-time-empty registries still return never-match
    sentinels and cache nothing.
    """
    global _SPEAKER_NAME_TO_CANONICAL, _SPEAKER_CASEFOLD_LOOKUP

    aliases_map = _refresh_speaker_resolver(path)
    p = Path(path)
    cache_key = str(p.resolve()) if p.exists() else str(p)

    # Collect ALL names (canonicals + aliases)
    name_to_canonical: dict[str, str] = {}
    for canonical, aliases in aliases_map.items():
        name_to_canonical[canonical] = canonical
        for alias in aliases:
            name_to_canonical[alias] = canonical

    if not name_to_canonical:
        cached = _LAST_GOOD_SPEAKER_RULES.get(cache_key)
        if cached is not None:
            rules, cached_names, cached_casefold = cached
            _SPEAKER_NAME_TO_CANONICAL = dict(cached_names)
            _SPEAKER_CASEFOLD_LOOKUP = dict(cached_casefold)
            logger.warning(
                "speaker-aliases load returned empty for %s; using "
                "last-known-good speaker auto-rules (%d names)",
                path,
                len(cached_names),
            )
            return rules
        # First-time empty registry -- never-match sentinels, nothing cached.
        never_match = r"(?!x)x"
        spoke = CueRule(
            name="speaker_auto_spoke", cue_phrases=(), target_predicate=None,
            delta=0.04, question_regex=never_match,
            match_field="speakers_spoke", match_strategy="name_resolve_then_check",
            recruit=True,
        )
        mentioned = CueRule(
            name="speaker_auto_mentioned", cue_phrases=(), target_predicate=None,
            delta=0.02, question_regex=never_match,
            match_field="speakers_mentioned", match_strategy="name_resolve_then_check",
            recruit=True,
        )
        return (spoke, mentioned)

    # Longest-first alternation; escape regex metacharacters.
    sorted_names = sorted(name_to_canonical.keys(), key=lambda n: -len(n))
    escaped = [re.escape(n) for n in sorted_names]
    pattern = r"\b(" + "|".join(escaped) + r")\b"

    spoke = CueRule(
        name="speaker_auto_spoke",
        cue_phrases=(),
        target_predicate=None,
        delta=0.04,
        question_regex=pattern,
        match_field="speakers_spoke",
        match_strategy="name_resolve_then_check",
        recruit=True,
    )
    mentioned = CueRule(
        name="speaker_auto_mentioned",
        cue_phrases=(),
        target_predicate=None,
        delta=0.02,
        question_regex=pattern,
        match_field="speakers_mentioned",
        match_strategy="name_resolve_then_check",
        recruit=True,
    )
    _LAST_GOOD_SPEAKER_RULES[cache_key] = (
        (spoke, mentioned),
        dict(_SPEAKER_NAME_TO_CANONICAL),
        dict(_SPEAKER_CASEFOLD_LOOKUP),
    )
    return (spoke, mentioned)
```

(Note: this replaces the Task 1 edit to this function — the `recruit=True` lines are already present above; keep them.)

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_speaker_auto_lkg.py tests/test_cue_rules_speaker_auto.py tests/test_cue_rules_recruit.py -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/cue_rules.py community-brain/tests/test_speaker_auto_lkg.py
```
```bash
git commit -m "fix(retrieval): last-known-good cache for speaker auto-rules incl. resolver snapshot (v5 D12)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 6: Citation-guard verifier functions in the filter (pure logic)

**Files:**
- Modify: `community-brain/src/community_brain/openwebui/community_brain_filter.py`
- Test: `community-brain/tests/test_filter_citation_guard.py` (new)

**Interfaces:**
- Consumes: existing `CONTEXT_TAG`, `_render_chunk`, `Filter._build_sources_message`.
- Produces (module-level, importable by the eval harness in Task 11):
  - `extract_grounding_facts(context_content: str) -> dict | None` — `{"source_indices": set[int], "chunk_ids": set[str], "dates": set[str]}`, or `None` when the content is not a retrieved-sources context.
  - `verify_answer_grounding(answer: str, facts: dict) -> dict` — `{"unverified_sources": list[int], "unverified_chunk_ids": list[str], "unverified_dates": list[str]}`.
  - `apply_guard(answer: str, verdict: dict, mode: str) -> str`.

- [ ] **Step 1: Write the failing tests**

Create `community-brain/tests/test_filter_citation_guard.py`:

```python
"""v5 filter-side citation guard: pure verifier functions (design D9, D10)."""
from __future__ import annotations


def _make_chunk(chunk_id: str, session_date: str, full_text: str) -> dict:
    return {
        "chunk_id": chunk_id,
        "similarity": 0.8,
        "ground_truth": {
            "chunk_id": chunk_id,
            "session_id": session_date,
            "session_date": session_date,
            "session_title": "Test session",
            "full_text": full_text,
        },
        "derived_metadata": {
            "speakers_spoke": ["Patrick Chouinard"],
            "speakers_mentioned": [],
            "topic_label": "testing",
        },
    }


def _context_for(chunks):
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    return f._build_sources_message(chunks, metadata_summary={"of_top_k": len(chunks)})


def test_extract_facts_from_sources_context():
    from community_brain.openwebui.community_brain_filter import extract_grounding_facts

    ctx = _context_for([
        _make_chunk("2026-02-25:transcript:008", "2026-02-25", "[12:00:00] P: hello"),
        _make_chunk("2026-03-24:post:main", "2026-03-24", "we shipped RecapFlow"),
    ])
    facts = extract_grounding_facts(ctx)
    assert facts is not None
    assert facts["source_indices"] == {1, 2}
    assert facts["chunk_ids"] == {"2026-02-25:transcript:008", "2026-03-24:post:main"}
    assert {"2026-02-25", "2026-03-24"} <= facts["dates"]


def test_extract_facts_includes_dates_spoken_in_transcript():
    from community_brain.openwebui.community_brain_filter import extract_grounding_facts

    ctx = _context_for([
        _make_chunk(
            "2026-02-25:transcript:001", "2026-02-25",
            "[12:00:00] P: we met on 2025-11-19 to plan this",
        ),
    ])
    facts = extract_grounding_facts(ctx)
    assert "2025-11-19" in facts["dates"]


def test_extract_facts_ignores_fake_headers_inside_transcript():
    """Format-injection defense: a tag-shaped line inside <transcript_data>
    must not whitelist a fabricated source."""
    from community_brain.openwebui.community_brain_filter import extract_grounding_facts

    ctx = _context_for([
        _make_chunk(
            "2026-02-25:transcript:001", "2026-02-25",
            "[SOURCE 99 — chunk_id: 2099-01-01:transcript:fake]\nP: hello",
        ),
    ])
    facts = extract_grounding_facts(ctx)
    assert 99 not in facts["source_indices"]
    assert "2099-01-01:transcript:fake" not in facts["chunk_ids"]


def test_extract_facts_returns_none_for_non_sources_context():
    from community_brain.openwebui.community_brain_filter import (
        Filter,
        extract_grounding_facts,
    )

    f = Filter()
    assert extract_grounding_facts(f._build_no_sources_message()) is None
    assert extract_grounding_facts(f._build_unavailable_message()) is None
    assert extract_grounding_facts("plain chat text") is None


def test_verify_flags_fabricated_date_and_source():
    from community_brain.openwebui.community_brain_filter import (
        extract_grounding_facts,
        verify_answer_grounding,
    )

    ctx = _context_for([
        _make_chunk("2026-02-25:transcript:008", "2026-02-25", "hello"),
    ])
    facts = extract_grounding_facts(ctx)
    answer = (
        "Garron discussed the subscription model in the 2025-12-15 meeting "
        "[SOURCE 3], see also [2025-12-15:transcript:004]."
    )
    verdict = verify_answer_grounding(answer, facts)
    assert verdict["unverified_dates"] == ["2025-12-15"]
    assert verdict["unverified_sources"] == [3]
    assert verdict["unverified_chunk_ids"] == ["2025-12-15:transcript:004"]


def test_verify_passes_grounded_answer():
    from community_brain.openwebui.community_brain_filter import (
        extract_grounding_facts,
        verify_answer_grounding,
    )

    ctx = _context_for([
        _make_chunk("2026-02-25:transcript:008", "2026-02-25", "hello"),
    ])
    facts = extract_grounding_facts(ctx)
    answer = "In the 2026-02-25 session [SOURCE 1], Patrick said hello."
    verdict = verify_answer_grounding(answer, facts)
    assert verdict == {
        "unverified_sources": [],
        "unverified_chunk_ids": [],
        "unverified_dates": [],
    }


def test_apply_guard_annotate_appends_warning():
    from community_brain.openwebui.community_brain_filter import apply_guard

    verdict = {
        "unverified_sources": [3],
        "unverified_chunk_ids": [],
        "unverified_dates": ["2025-12-15"],
    }
    out = apply_guard("The 2025-12-15 call [SOURCE 3] decided X.", verdict, "annotate")
    assert out.startswith("The 2025-12-15 call [SOURCE 3] decided X.")
    assert "Grounding check (automated)" in out
    assert "2025-12-15" in out
    assert "[SOURCE 3]" in out


def test_apply_guard_strip_replaces_tokens():
    from community_brain.openwebui.community_brain_filter import apply_guard

    verdict = {
        "unverified_sources": [3],
        "unverified_chunk_ids": ["2025-12-15:transcript:004"],
        "unverified_dates": ["2025-12-15"],
    }
    answer = "See [2025-12-15:transcript:004] and [SOURCE 3] from 2025-12-15."
    out = apply_guard(answer, verdict, "strip")
    assert "[2025-12-15:transcript:004]" not in out
    assert "[SOURCE 3]" not in out
    assert "2025-12-15." not in out.split("Grounding check")[0]
    assert "[unverified source]" in out
    assert "[unverified date]" in out
    assert "Grounding check (automated)" in out


def test_apply_guard_clean_verdict_returns_answer_unchanged():
    from community_brain.openwebui.community_brain_filter import apply_guard

    verdict = {
        "unverified_sources": [],
        "unverified_chunk_ids": [],
        "unverified_dates": [],
    }
    assert apply_guard("clean answer", verdict, "annotate") == "clean answer"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_filter_citation_guard.py -q`
Expected: FAIL — `ImportError: cannot import name 'extract_grounding_facts'`.

- [ ] **Step 3: Implement the verifier functions**

In `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

(a) At the top, extend the imports:

```python
import logging
import re
from collections import OrderedDict
from typing import Optional
```

(b) After the `CONTEXT_TAG` constant, add:

```python
# --- v5 citation guard (design D8-D10) ------------------------------------
# Deterministic post-generation verification. gpt-oss:20b demonstrably
# ignores system-prompt verification scaffolding under specific-query /
# weak-retrieval pressure (v4 validation Q3); these functions verify the
# ANSWER against the retrieved context instead of trusting the model.

RETRIEVED_SOURCES_MARKER = "## Retrieved Sources"

_SOURCE_HEADER_RE = re.compile(r"\[SOURCE (\d+) — chunk_id: ([^\]]+)\]")
_SOURCE_REF_RE = re.compile(r"\[SOURCE\s+(\d+)\]", re.IGNORECASE)
_CHUNK_ID_REF_RE = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}:[a-z_]+:[A-Za-z0-9_\-.]+)\]"
)
_ISO_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
_TRANSCRIPT_BLOCK_RE = re.compile(
    r"<transcript_data>.*?</transcript_data>", re.DOTALL
)

# Bounded per-chat grounding stash: outlet-side fallback for Open WebUI
# versions that don't replay injected system messages into outlet.
_GROUNDING_STASH_MAX = 32


def extract_grounding_facts(context_content: str) -> dict | None:
    """Parse grounding facts out of a retrieved-sources context message.

    Returns None when the content is not a sources context (no-results
    notice, unavailable notice, arbitrary text) — callers must skip the
    guard in that case.

    source_indices / chunk_ids come from the [SOURCE N — chunk_id: ...]
    header lines with all <transcript_data> bodies removed first, so a
    tag-shaped line spoken inside a transcript cannot whitelist a
    fabricated source (position contract, docs/inference-guidelines.md).
    dates come from the FULL context including transcript bodies — a date
    a speaker actually said is legitimate for the model to repeat.
    """
    if CONTEXT_TAG not in context_content:
        return None
    if RETRIEVED_SOURCES_MARKER not in context_content:
        return None
    metadata_only = _TRANSCRIPT_BLOCK_RE.sub("", context_content)
    source_indices: set[int] = set()
    chunk_ids: set[str] = set()
    for m in _SOURCE_HEADER_RE.finditer(metadata_only):
        source_indices.add(int(m.group(1)))
        chunk_ids.add(m.group(2).strip())
    dates = set(_ISO_DATE_RE.findall(context_content))
    return {
        "source_indices": source_indices,
        "chunk_ids": chunk_ids,
        "dates": dates,
    }


def verify_answer_grounding(answer: str, facts: dict) -> dict:
    """Check every [SOURCE N] reference, chunk_id-shaped citation, and bare
    ISO date in `answer` against the grounding facts. Returns the sorted
    lists of tokens that could NOT be verified."""
    cited_sources = {int(n) for n in _SOURCE_REF_RE.findall(answer)}
    unverified_sources = sorted(cited_sources - facts["source_indices"])

    cited_chunk_ids = set(_CHUNK_ID_REF_RE.findall(answer))
    unverified_chunk_ids = sorted(cited_chunk_ids - facts["chunk_ids"])

    dates_in_answer = set(_ISO_DATE_RE.findall(answer))
    unverified_dates = sorted(dates_in_answer - facts["dates"])

    return {
        "unverified_sources": unverified_sources,
        "unverified_chunk_ids": unverified_chunk_ids,
        "unverified_dates": unverified_dates,
    }


def apply_guard(answer: str, verdict: dict, mode: str) -> str:
    """Apply the guard policy to an answer given a non-empty verdict.

    annotate: append a delimited warning block naming the unverified tokens.
    strip: additionally replace each unverified token in place. Chunk-id
        citations are replaced BEFORE bare dates so a fabricated date inside
        a fabricated citation is handled once.
    Returns the answer unchanged when the verdict is clean.
    """
    lines: list[str] = []
    if verdict["unverified_dates"]:
        lines.append(
            "- session dates not present in the retrieved sources: "
            + ", ".join(verdict["unverified_dates"])
        )
    if verdict["unverified_sources"]:
        lines.append(
            "- source citations with no matching retrieved source: "
            + ", ".join(f"[SOURCE {n}]" for n in verdict["unverified_sources"])
        )
    if verdict["unverified_chunk_ids"]:
        lines.append(
            "- chunk ids not in the retrieved set: "
            + ", ".join(verdict["unverified_chunk_ids"])
        )
    if not lines:
        return answer

    if mode == "strip":
        for cid in verdict["unverified_chunk_ids"]:
            answer = answer.replace(f"[{cid}]", "[unverified source]")
        for n in verdict["unverified_sources"]:
            answer = re.sub(
                rf"\[SOURCE\s+{n}\]", "[unverified source]", answer,
                flags=re.IGNORECASE,
            )
        for d in verdict["unverified_dates"]:
            answer = answer.replace(d, "[unverified date]")

    warning = (
        "\n\n---\n"
        "**Grounding check (automated):** this answer references material "
        "that does NOT appear in the retrieved sources and may be "
        "fabricated:\n" + "\n".join(lines) + "\n"
        "Treat those specific claims as unverified."
    )
    return answer + warning
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_filter_citation_guard.py -q`
Expected: 9 passed.

- [ ] **Step 5: Filter regression**

Run: `./.venv/bin/pytest tests/test_filter.py tests/test_filter_rendering_v4.py -q`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/openwebui/community_brain_filter.py community-brain/tests/test_filter_citation_guard.py
```
```bash
git commit -m "feat(openwebui): deterministic grounding verifier for answers (v5 D9,D10)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 7: Filter `outlet` hook, `citation_guard` valve, per-chat stash

**Files:**
- Modify: `community-brain/src/community_brain/openwebui/community_brain_filter.py`
- Test: `community-brain/tests/test_filter_citation_guard.py` (append)

**Interfaces:**
- Consumes: Task 6 functions.
- Produces: `Filter.Valves.citation_guard: str = "annotate"`; `Filter.outlet(body, __user__) -> dict`; `Filter.__init__` gains `self._grounding_by_chat: OrderedDict`. `inlet` stashes facts per chat (facts on `ok`, `None` otherwise).

- [ ] **Step 1: Write the failing tests**

Append to `community-brain/tests/test_filter_citation_guard.py`:

```python
# ---------------------------------------------------------------------------
# Filter.outlet integration (design D8)
# ---------------------------------------------------------------------------


def _sources_context():
    return _context_for([
        _make_chunk("2026-02-25:transcript:008", "2026-02-25", "hello world"),
    ])


def _outlet_body(context_content: str | None, answer: str, chat_id: str = "c1") -> dict:
    messages = []
    if context_content is not None:
        messages.append({"role": "system", "content": context_content})
    messages.append({"role": "user", "content": "question?"})
    messages.append({"role": "assistant", "content": answer})
    return {"chat_id": chat_id, "messages": messages}


def test_outlet_annotates_fabricated_date():
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    body = _outlet_body(_sources_context(), "That was decided on 2025-12-15.")
    out = f.outlet(body)
    answer = out["messages"][-1]["content"]
    assert "Grounding check (automated)" in answer
    assert "2025-12-15" in answer


def test_outlet_leaves_grounded_answer_untouched():
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    clean = "Per [SOURCE 1], the 2026-02-25 session covered hello world."
    body = _outlet_body(_sources_context(), clean)
    out = f.outlet(body)
    assert out["messages"][-1]["content"] == clean


def test_outlet_off_valve_disables_guard():
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    f.valves.citation_guard = "off"
    fabricated = "That was decided on 2025-12-15."
    body = _outlet_body(_sources_context(), fabricated)
    out = f.outlet(body)
    assert out["messages"][-1]["content"] == fabricated


def test_outlet_strip_mode_redacts():
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    f.valves.citation_guard = "strip"
    body = _outlet_body(_sources_context(), "Decided on 2025-12-15 [SOURCE 9].")
    out = f.outlet(body)
    answer = out["messages"][-1]["content"]
    assert "[unverified date]" in answer
    assert "[unverified source]" in answer


def test_outlet_skips_when_context_is_no_sources_notice():
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    notice = f._build_no_sources_message()
    fabricated = "Generally speaking, 2025-12-15 was a Monday."
    body = _outlet_body(notice, fabricated)
    out = f.outlet(body)
    # No sources context -> model was told to answer generally; guard skips.
    assert out["messages"][-1]["content"] == fabricated


def test_outlet_fails_open_without_any_context():
    from community_brain.openwebui.community_brain_filter import Filter

    f = Filter()
    fabricated = "On 2025-12-15 the group met."
    body = _outlet_body(None, fabricated, chat_id="unknown-chat")
    out = f.outlet(body)
    assert out["messages"][-1]["content"] == fabricated


def test_outlet_uses_inlet_stash_when_context_absent(monkeypatch):
    """Some Open WebUI versions do not replay injected system messages into
    outlet; the per-chat stash written by inlet covers that."""
    from community_brain.openwebui import community_brain_filter as cbf

    f = cbf.Filter()
    ctx = _sources_context()
    facts = cbf.extract_grounding_facts(ctx)
    f._grounding_by_chat["c9"] = facts

    body = _outlet_body(None, "Decided on 2025-12-15.", chat_id="c9")
    out = f.outlet(body)
    assert "Grounding check (automated)" in out["messages"][-1]["content"]


def test_inlet_stashes_facts_per_chat(monkeypatch):
    from community_brain.openwebui import community_brain_filter as cbf

    f = cbf.Filter()

    def _fake_retrieve(question):
        chunks = [_make_chunk("2026-02-25:transcript:008", "2026-02-25", "hello")]
        return "ok", chunks, {"of_top_k": 1}

    monkeypatch.setattr(f, "_retrieve_chunks", _fake_retrieve)
    body = {
        "chat_id": "c42",
        "messages": [{"role": "user", "content": "what happened on 2026-02-25?"}],
    }
    f.inlet(body)
    facts = f._grounding_by_chat.get("c42")
    assert facts is not None
    assert "2026-02-25" in facts["dates"]


def test_inlet_clears_stash_on_retrieval_error(monkeypatch):
    from community_brain.openwebui import community_brain_filter as cbf

    f = cbf.Filter()
    f._grounding_by_chat["c42"] = {"source_indices": {1}, "chunk_ids": set(), "dates": set()}

    def _fake_retrieve(question):
        return "error", [], None

    monkeypatch.setattr(f, "_retrieve_chunks", _fake_retrieve)
    body = {
        "chat_id": "c42",
        "messages": [{"role": "user", "content": "anything"}],
    }
    f.inlet(body)
    assert f._grounding_by_chat.get("c42") is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_filter_citation_guard.py -q`
Expected: new tests FAIL — `AttributeError: 'Filter' object has no attribute 'outlet'` / `_grounding_by_chat`.

- [ ] **Step 3: Implement valve, stash, and outlet**

In `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

(a) Add the valve to `Filter.Valves` after `expose_score_breakdown`:

```python
        citation_guard: str = Field(
            default="annotate",
            description=(
                "Post-generation grounding guard: 'annotate' appends a "
                "warning block listing session dates / [SOURCE N] refs / "
                "chunk_ids in the answer that don't appear in the retrieved "
                "context; 'strip' additionally replaces them with "
                "[unverified ...] markers; 'off' disables the guard. "
                "The guard is deterministic (regex against the retrieved "
                "context) — no extra LLM call."
            ),
        )
```

(b) Extend `__init__`:

```python
    def __init__(self):
        self.valves = self.Valves()
        # Per-chat grounding stash (v5 D8): fallback for outlet when the
        # injected system message is not replayed in the outlet body.
        # ok -> facts dict; no_results/error -> None (clears stale facts).
        self._grounding_by_chat: "OrderedDict[str, dict | None]" = OrderedDict()
```

(c) Add a small helper method to `Filter` (below `_retrieve_chunks`):

```python
    @staticmethod
    def _chat_id_of(body: dict) -> str:
        return str(
            body.get("chat_id")
            or (body.get("metadata") or {}).get("chat_id")
            or "default"
        )

    def _stash_grounding(self, chat_id: str, facts: dict | None) -> None:
        self._grounding_by_chat[chat_id] = facts
        self._grounding_by_chat.move_to_end(chat_id)
        while len(self._grounding_by_chat) > _GROUNDING_STASH_MAX:
            self._grounding_by_chat.popitem(last=False)
```

(d) In `inlet`, after the `if status == "ok": ... else: ...` block that sets `context_content` and BEFORE `context_message = ...`, add:

```python
        # Stash grounding facts for outlet (v5 D8). Non-ok statuses stash
        # None so a previous turn's facts can't leak into this turn's guard.
        chat_id = self._chat_id_of(body)
        if status == "ok":
            self._stash_grounding(chat_id, extract_grounding_facts(context_content))
        else:
            self._stash_grounding(chat_id, None)
```

(e) Add `outlet` at the end of the `Filter` class:

```python
    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """Post-generation grounding guard (v5 D8-D10).

        Verifies session dates, [SOURCE N] references, and chunk_id-shaped
        citations in the assistant's answer against the retrieved context.
        Fails OPEN: when no grounding context is available the answer
        passes through untouched (the guard is defense-in-depth, not a
        gate). When the context message for this turn is a no-sources or
        unavailable notice, the guard skips — the model was explicitly
        told to answer generally or refuse.
        """
        mode = (self.valves.citation_guard or "annotate").strip().lower()
        if mode == "off" or not self.valves.enabled:
            return body

        messages = body.get("messages", [])

        facts: dict | None = None
        context_found = False
        for m in messages:
            if m.get("role") == "system" and CONTEXT_TAG in (m.get("content") or ""):
                context_found = True
                facts = extract_grounding_facts(m.get("content") or "")
                break

        if context_found and facts is None:
            # This turn's context is a no-sources/unavailable notice.
            return body
        if not context_found:
            facts = self._grounding_by_chat.get(self._chat_id_of(body))
        if not facts:
            logger.warning(
                "citation guard: no grounding context available; failing open"
            )
            return body

        for m in reversed(messages):
            if m.get("role") == "assistant":
                answer = m.get("content") or ""
                verdict = verify_answer_grounding(answer, facts)
                if any(verdict.values()):
                    m["content"] = apply_guard(answer, verdict, mode)
                break

        body["messages"] = messages
        return body
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_filter_citation_guard.py -q`
Expected: 18 passed.

- [ ] **Step 5: Full filter + suite regression**

Run: `./.venv/bin/pytest tests/ -q`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/openwebui/community_brain_filter.py community-brain/tests/test_filter_citation_guard.py
```
```bash
git commit -m "feat(openwebui): outlet citation guard with annotate/strip/off valve (v5 D8)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 8: Wire `RetryConfig` into Stage B/C LLM calls

**Files:**
- Modify: `community-brain/src/community_brain/llm.py`
- Modify: `community-brain/src/community_brain/ingestion/extractor.py`
- Modify: `community-brain/src/community_brain/ingestion/session_extractor.py`
- Modify: `community-brain/src/community_brain/ingestion/pipeline.py`
- Modify (mock signatures only): `community-brain/tests/test_end_to_end.py`, `community-brain/tests/test_ingestion_pipeline.py`, `community-brain/tests/test_retrieval_server_ingest.py`
- Test: `community-brain/tests/test_retry_config_wiring.py` (new) + addition to `community-brain/tests/test_llm.py`

**Interfaces:**
- Consumes: `RetryConfig` from `community_brain.ingestion.config_loader` (fields `retry_attempts: int`, `retry_backoff_seconds: list[int]`, `inter_session_delay_seconds: int`).
- Produces: `call_llm(prompt, model=None, retries=3, backoff_schedule: list[int] | None = None)`; `extractor._call_llm(model, prompt, retries=3, backoff_schedule=None)`; `extract_chunk_metadata(..., retry_config: RetryConfig | None = None)`; `extract_session_themes(..., retry_config: RetryConfig | None = None)`; `ingest_session` threads the loaded config. When `retry_config is None`, every call site is byte-identical to v4 behavior.

- [ ] **Step 1: Write the failing tests**

Create `community-brain/tests/test_retry_config_wiring.py`:

```python
"""RetryConfig threading: pipeline -> Stage B/C -> _call_llm (v5 D14).

Closes the documented v2 TODO in ingestion/pipeline.py. The mock boundary
(extractor._call_llm / session_extractor._call_llm) keeps positional
compatibility: without retry_config the call is exactly (model=, prompt=).
"""
from __future__ import annotations

import json
from unittest.mock import patch

from community_brain.ingestion.config_loader import RetryConfig
from community_brain.ingestion.extractor import extract_chunk_metadata
from community_brain.ingestion.session_extractor import extract_session_themes

RETRY = RetryConfig(
    retry_attempts=5,
    retry_backoff_seconds=[1, 2, 3, 4, 5],
    inter_session_delay_seconds=0,
)


def test_session_extractor_threads_retry_config():
    captured = {}

    def _fake(model, prompt, retries=3, backoff_schedule=None):
        captured["retries"] = retries
        captured["backoff_schedule"] = backoff_schedule
        return json.dumps({"themes": ["a"]})

    with patch(
        "community_brain.ingestion.session_extractor._call_llm", side_effect=_fake
    ):
        res = extract_session_themes(
            input_text="text", model="m", prompt_template="p", retry_config=RETRY
        )
    assert res.status == "success"
    assert captured["retries"] == 5
    assert captured["backoff_schedule"] == [1, 2, 3, 4, 5]


def test_session_extractor_without_retry_config_uses_defaults():
    captured = {}

    def _fake(model, prompt, retries=3, backoff_schedule=None):
        captured["retries"] = retries
        captured["backoff_schedule"] = backoff_schedule
        return json.dumps({"themes": []})

    with patch(
        "community_brain.ingestion.session_extractor._call_llm", side_effect=_fake
    ):
        extract_session_themes(input_text="text", model="m", prompt_template="p")
    assert captured["retries"] == 3
    assert captured["backoff_schedule"] is None


def test_chunk_extractor_threads_retry_config():
    captured = {}

    def _fake(model, prompt, retries=3, backoff_schedule=None):
        captured["retries"] = retries
        captured["backoff_schedule"] = backoff_schedule
        return "not json"  # extraction fails downstream; only threading matters

    with patch("community_brain.ingestion.extractor._call_llm", side_effect=_fake):
        extract_chunk_metadata(
            chunk_text="t",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
            retry_config=RETRY,
        )
    assert captured["retries"] == 5
    assert captured["backoff_schedule"] == [1, 2, 3, 4, 5]
```

Append to `community-brain/tests/test_llm.py`:

```python
def test_call_llm_uses_backoff_schedule(monkeypatch):
    """5xx retries sleep per the configured schedule, not 2**attempt."""
    import time as _time

    import httpx as _httpx

    from community_brain.llm import call_llm

    sleeps: list[int] = []
    monkeypatch.setattr(_time, "sleep", lambda s: sleeps.append(s))

    calls = {"n": 0}

    class _Fail:
        status_code = 500

        def raise_for_status(self):  # pragma: no cover - not reached on 5xx
            raise AssertionError("raise_for_status should not run on the 5xx path")

        def json(self):  # pragma: no cover
            return {}

    class _OK:
        status_code = 200

        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "ok"}}], "usage": {}}

    def _fake_post(url, headers=None, json=None, timeout=None):
        calls["n"] += 1
        return _Fail() if calls["n"] <= 2 else _OK()

    monkeypatch.setattr(_httpx, "post", _fake_post)
    out = call_llm("hi", model="m", retries=3, backoff_schedule=[7, 11, 13])
    assert out == "ok"
    assert sleeps == [7, 11]


def test_call_llm_default_backoff_is_exponential(monkeypatch):
    import time as _time

    import httpx as _httpx

    from community_brain.llm import call_llm

    sleeps: list[int] = []
    monkeypatch.setattr(_time, "sleep", lambda s: sleeps.append(s))

    calls = {"n": 0}

    class _Fail:
        status_code = 500

        def raise_for_status(self):  # pragma: no cover
            raise AssertionError

        def json(self):  # pragma: no cover
            return {}

    class _OK:
        status_code = 200

        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "ok"}}], "usage": {}}

    def _fake_post(url, headers=None, json=None, timeout=None):
        calls["n"] += 1
        return _Fail() if calls["n"] <= 2 else _OK()

    monkeypatch.setattr(_httpx, "post", _fake_post)
    call_llm("hi", model="m", retries=3)
    assert sleeps == [1, 2]
```

(Note: `test_llm.py` has an autouse fixture mocking `OPENROUTER_API_KEY`; these tests rely on it, so they MUST live in that file.)

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_retry_config_wiring.py tests/test_llm.py -q`
Expected: new tests FAIL — `TypeError: call_llm() got an unexpected keyword argument 'backoff_schedule'` / `extract_session_themes() got an unexpected keyword argument 'retry_config'`.

- [ ] **Step 3: Implement**

(a) `community-brain/src/community_brain/llm.py` — change `call_llm`'s signature and both backoff computations:

```python
def call_llm(
    prompt: str,
    model: str | None = None,
    retries: int = 3,
    backoff_schedule: list[int] | None = None,
) -> str:
    """Call OpenRouter chat completions API and return the response text.

    Args:
        prompt: The user message to send.
        model: Override the default model.
        retries: Number of retry attempts on failure.
        backoff_schedule: Per-attempt sleep seconds (index = attempt).
            When None, falls back to exponential 2**attempt. Callers
            wiring chunking.yaml's RetryConfig pass its
            retry_backoff_seconds here (the loader guarantees the list is
            at least retry_attempts long).
    """
```

Inside the loop, replace BOTH occurrences of `backoff = 2 ** attempt` with:

```python
                if backoff_schedule is not None and attempt < len(backoff_schedule):
                    backoff = backoff_schedule[attempt]
                else:
                    backoff = 2 ** attempt
```

(One occurrence is in the `status_code >= 500` branch, one in the `except httpx.HTTPError` branch.)

(b) `community-brain/src/community_brain/ingestion/extractor.py`:

```python
from community_brain.ingestion.config_loader import RetryConfig
```

```python
def _call_llm(
    model: str,
    prompt: str,
    retries: int = 3,
    backoff_schedule: list[int] | None = None,
) -> str:
    """Indirection for testing. Wraps the OpenRouter client call."""
    return call_llm(
        prompt=prompt, model=model, retries=retries, backoff_schedule=backoff_schedule
    )
```

Add `retry_config: RetryConfig | None = None` as the last parameter of `extract_chunk_metadata`, document it in the docstring Args (`retry_config: chunking.yaml retry policy; None preserves call_llm's built-in 3-attempt exponential default.`), and replace the call:

```python
    try:
        if retry_config is not None:
            raw = _call_llm(
                model=model,
                prompt=prompt,
                retries=retry_config.retry_attempts,
                backoff_schedule=list(retry_config.retry_backoff_seconds),
            )
        else:
            raw = _call_llm(model=model, prompt=prompt)
    except Exception as exc:
```

(c) `community-brain/src/community_brain/ingestion/session_extractor.py` — identical treatment: import `RetryConfig`, extend `_call_llm` the same way, add `retry_config: RetryConfig | None = None` to `extract_session_themes`, and use the same conditional call around its `raw = _call_llm(...)`.

(d) `community-brain/src/community_brain/ingestion/pipeline.py`:
- Delete the module-docstring lines `TODO(v2): wire RetryConfig into Stage B/C LLM calls to honor configured retry_attempts and retry_backoff_seconds.`
- Replace the load line and its comment:

```python
    # RetryConfig from chunking.yaml is wired into Stage B/C LLM calls (v5):
    # retry_attempts + retry_backoff_seconds override call_llm's built-in
    # 3-attempt exponential default.
    chunking_cfg, retry_cfg = load_chunking_config(config_dir / "chunking.yaml")
```

- Pass it to Stage B:

```python
    themes_result = extract_session_themes(
        input_text=session_input,
        model=extraction_cfg.session_themes_model,
        prompt_template=session_themes_prompt,
        retry_config=retry_cfg,
    )
```

- Pass it to Stage C:

```python
        res = extract_chunk_metadata(
            chunk_text=chunk.full_text,
            entity_registry_names=entity_names,
            speaker_alias_names=speaker_names,
            model=extraction_cfg.chunk_extraction_model,
            prompt_template=chunk_extraction_prompt,
            speakers_spoke=chunk.speakers_spoke or [],
            retry_config=retry_cfg,
        )
```

(e) Update the NINE test mock functions whose signature is `(model, prompt)` to tolerate the new kwargs — add `**_kwargs`:

- `tests/test_end_to_end.py` — `def _fake_extract_response(model, prompt, **_kwargs):`
- `tests/test_ingestion_pipeline.py` — same change to `_fake_extract_response`, `_broken_extract`, `_broken_chunk_extract`, `_alias_extract`, `_partition_extract`, `_unknown_extract`, `_canon_resync_extract` (7 functions)
- `tests/test_retrieval_server_ingest.py` — `def _fake_extract_response(model, prompt, **_kwargs):`

(Do NOT touch the mocks in `test_ingestion_extractor.py` / `test_ingestion_session_extractor.py` — those tests call the extract functions without `retry_config`, so `_call_llm` still receives exactly `(model=, prompt=)`.)

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_retry_config_wiring.py tests/test_llm.py -q`
Expected: all pass.

- [ ] **Step 5: Full regression (the mock-signature edits touch e2e/pipeline suites)**

Run: `./.venv/bin/pytest tests/ -q`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/llm.py community-brain/src/community_brain/ingestion/extractor.py community-brain/src/community_brain/ingestion/session_extractor.py community-brain/src/community_brain/ingestion/pipeline.py community-brain/tests/test_retry_config_wiring.py community-brain/tests/test_llm.py community-brain/tests/test_end_to_end.py community-brain/tests/test_ingestion_pipeline.py community-brain/tests/test_retrieval_server_ingest.py
```
```bash
git commit -m "feat(ingestion): wire RetryConfig into Stage B/C LLM calls (v5 D14, closes v2 TODO)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 9: `has_unresolved_question` over-permissiveness alarm in `lint_corpus`

**Files:**
- Modify: `community-brain/src/community_brain/cli/lint_corpus.py`
- Test: `community-brain/tests/test_lint_corpus.py` (append)

**Interfaces:**
- Consumes: existing `lint_corpus_chunks` / `main`.
- Produces: constant `UNRESOLVED_RATE_ALARM_THRESHOLD = 0.50`; `lint_corpus_chunks` return dict gains `"unresolved_rate": float` and `"unresolved_alarm": bool` (additive — existing `scanned`/`recurrent` unchanged). No marker writes, no exit-code change.

- [ ] **Step 1: Write the failing tests**

Append to `community-brain/tests/test_lint_corpus.py` (the file already defines `_make_chunk_row`, `_create_table`, `_direction_vector`, and the `db_path` fixture — reuse them; add `import logging` and `import pytest` are already present or add `import logging` at the top if missing):

```python
def test_unresolved_rate_alarm_triggers_above_threshold(db_path: Path, caplog):
    import logging

    rows = []
    for i in range(10):
        row = _make_chunk_row(
            chunk_id=f"alarm-{i}",
            session_id=f"s{i}",
            embedding=_direction_vector(i),
        )
        row["has_unresolved_question"] = i < 6  # 60% > 50% threshold
        rows.append(row)
    _create_table(db_path, rows)

    with caplog.at_level(logging.WARNING):
        stats = lint_corpus_chunks(db_path)

    assert stats["unresolved_rate"] == pytest.approx(0.6)
    assert stats["unresolved_alarm"] is True
    assert any("over-triggering" in r.message for r in caplog.records)


def test_unresolved_rate_no_alarm_at_healthy_rate(db_path: Path):
    rows = []
    for i in range(10):
        row = _make_chunk_row(
            chunk_id=f"ok-{i}",
            session_id=f"s{i}",
            embedding=_direction_vector(i),
        )
        row["has_unresolved_question"] = i < 2  # 20%
        rows.append(row)
    _create_table(db_path, rows)

    stats = lint_corpus_chunks(db_path)

    assert stats["unresolved_rate"] == pytest.approx(0.2)
    assert stats["unresolved_alarm"] is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_lint_corpus.py -q`
Expected: the two new tests FAIL with `KeyError: 'unresolved_rate'`; existing tests pass.

- [ ] **Step 3: Implement**

In `community-brain/src/community_brain/cli/lint_corpus.py`:

(a) With the other module constants:

```python
# v5 D13: corpus-wide alarm threshold for has_unresolved_question=True.
# chunk-extraction-v3 deliberately defaults the flag toward true; healthy
# corpus rate observed ~27%. Above 50% the flag has stopped discriminating
# and the prompt has likely drifted over-permissive.
UNRESOLVED_RATE_ALARM_THRESHOLD = 0.50
```

(b) In `lint_corpus_chunks`, right after `rows = table.to_arrow().to_pylist()` and the `now_iso` line, add:

```python
    unresolved_count = sum(
        1 for r in rows if r.get("has_unresolved_question") is True
    )
    unresolved_rate = (unresolved_count / len(rows)) if rows else 0.0
    unresolved_alarm = unresolved_rate > UNRESOLVED_RATE_ALARM_THRESHOLD
    if unresolved_alarm:
        logger.warning(
            "lint_corpus: has_unresolved_question rate %.1f%% exceeds %.0f%% "
            "alarm threshold — the chunk-extraction prompt may be "
            "over-triggering; review before the next re-extract",
            unresolved_rate * 100,
            UNRESOLVED_RATE_ALARM_THRESHOLD * 100,
        )
```

(c) Change the return statement:

```python
    return {
        "scanned": len(rows),
        "recurrent": recurrent_count,
        "unresolved_rate": unresolved_rate,
        "unresolved_alarm": unresolved_alarm,
    }
```

(d) Update the docstring's `Returns` line to `Returns {"scanned": int, "recurrent": int, "unresolved_rate": float, "unresolved_alarm": bool}.` and extend `main()`:

```python
    stats = lint_corpus_chunks(args.db, rebuild=args.rebuild)
    print(
        f"[ok] lint_corpus: scanned {stats['scanned']}, "
        f"recurrent {stats['recurrent']}, "
        f"unresolved_rate {stats['unresolved_rate']:.1%}"
    )
    if stats["unresolved_alarm"]:
        print(
            "[ALARM] has_unresolved_question rate exceeds "
            f"{UNRESOLVED_RATE_ALARM_THRESHOLD:.0%} — extraction prompt may be "
            "over-triggering"
        )
    return 0
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_lint_corpus.py -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/cli/lint_corpus.py community-brain/tests/test_lint_corpus.py
```
```bash
git commit -m "feat(ingestion): corpus-wide has_unresolved_question over-trigger alarm in lint_corpus (v5 D13)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 10: Config + prompt/docs updates (recruit flags; guidelines rule 8 + citation exemplar; parity test)

**Files:**
- Modify: `community-brain/config/query-cues.yaml`
- Modify: `docs/inference-guidelines.md` (repo root)
- Modify: `prompts/community-brain-v4-openwebui-system-prompt.md` (repo root)
- Test: `community-brain/tests/test_prompt_artifacts.py` (new)

**Interfaces:**
- Consumes: loader `recruit:` support (Task 1).
- Produces: recruit-enabled production cue rules; guidelines rule 8 + rule 2 exemplar; a parity test locking `docs/inference-guidelines.md` ⊆ `prompts/community-brain-v4-openwebui-system-prompt.md`.

- [ ] **Step 1: Write the failing parity test**

Create `community-brain/tests/test_prompt_artifacts.py`:

```python
"""Paired prompt artifacts must not drift (v5 D15).

docs/inference-guidelines.md is the canonical system-prompt body; the
prompts/ file is the copy-paste deploy artifact whose body must contain
the guidelines verbatim. The v5 grounding rules live in BOTH.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

GUIDELINES = REPO_ROOT / "docs" / "inference-guidelines.md"
DEPLOY_ARTIFACT = REPO_ROOT / "prompts" / "community-brain-v4-openwebui-system-prompt.md"


def test_deploy_artifact_embeds_guidelines_verbatim():
    guidelines = GUIDELINES.read_text(encoding="utf-8")
    artifact = DEPLOY_ARTIFACT.read_text(encoding="utf-8")
    assert guidelines.strip() in artifact, (
        "prompts/community-brain-v4-openwebui-system-prompt.md must contain "
        "docs/inference-guidelines.md verbatim — update BOTH in the same commit"
    )


def test_guidelines_contain_v5_grounding_rules():
    guidelines = GUIDELINES.read_text(encoding="utf-8")
    assert "Flagged-unresolved chunks may be surveyed" in guidelines
    assert "never the raw chunk_id" in guidelines
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `./.venv/bin/pytest tests/test_prompt_artifacts.py -q`
Expected: `test_guidelines_contain_v5_grounding_rules` FAILS. (`test_deploy_artifact_embeds_guidelines_verbatim` should already pass — the files are in sync today; if it fails, STOP and inspect both files before proceeding.)

- [ ] **Step 3: Enable recruitment in `community-brain/config/query-cues.yaml`**

Add a `recruit: true` line to exactly these six rules (design D3), each directly after the rule's `delta:` line:

- `unresolved_questions` (after `delta: 0.040  # was 0.010 — v4 boost per spec 2026-05-03`):

```yaml
    delta: 0.040  # was 0.010 — v4 boost per spec 2026-05-03
    recruit: true  # v5: recruit flagged chunks into the pool (design D3)
```

- `date_iso_match`, `date_month_year_match`, `date_phrased_with_day`, `date_relative_phrasing`, `date_quarter_match` — for each, after its `delta: 0.04`:

```yaml
    delta: 0.04
    recruit: true  # v5: recruit date-matched chunks into the pool (design D3)
```

Do NOT add `recruit:` to `decisions`, `action_items`, `insights`, `referenced_prior`, or `questions_general` (generic cues would flood the pool — design D3 rationale).

- [ ] **Step 4: Update `docs/inference-guidelines.md`**

(a) In **rule 2** ("Cite by `[SOURCE N]` only — and verify before citing."), append these lines at the end of the rule's paragraph (inside rule 2, before rule 3):

```markdown
   BAD: "Garron discussed the subscription model in the 2025-12-15 meeting [2025-12-15:transcript:004]" — that session date does not appear in any `[session: ...]` header above; the citation is fabricated. GOOD: "I don't see Garron mentioned in the retrieved sources for December 2025." Citations must use the bracket-number form ("[SOURCE 2]"), never the raw chunk_id.
```

(b) After rule 7, append a new rule 8:

```markdown
8. **Flagged-unresolved chunks may be surveyed from the flag alone.** A chunk tagged `unresolved_question` in its `[flags:]` line raised a question that the chunk did not fully resolve — deferred answers, pivots, and partial responses count. For survey-style questions ("list the open questions"), you may enumerate from flagged chunks and cite them without locating an explicit unanswered question-and-answer pair verbatim in the transcript; quote the question text where it is visible.
```

- [ ] **Step 5: Apply the identical edits to `prompts/community-brain-v4-openwebui-system-prompt.md`**

The file is the HTML deploy-comment block followed by the guidelines body. Apply the exact same rule-2 addition and rule-8 append to the body so the body remains byte-identical to `docs/inference-guidelines.md`.

- [ ] **Step 6: Run tests to verify they pass**

Run: `./.venv/bin/pytest tests/test_prompt_artifacts.py -q`
Expected: 2 passed.

- [ ] **Step 7: Full regression (cue YAML changed — loader/golden suites must stay green)**

Run: `./.venv/bin/pytest tests/ -q`
Expected: all pass.

- [ ] **Step 8: Commit**

```bash
git add community-brain/config/query-cues.yaml docs/inference-guidelines.md prompts/community-brain-v4-openwebui-system-prompt.md community-brain/tests/test_prompt_artifacts.py
```
```bash
git commit -m "config(community-brain): enable recruitment on date/unresolved cues; v5 grounding rules in system prompt (D3,D15)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 11: Fabrication-rate evaluation harness

**Files:**
- Create: `scripts/eval/fabrication-queries.yaml` (repo root `scripts/`)
- Create: `scripts/eval-fabrication.py` (repo root `scripts/`)
- Test: smoke invocation only (the deterministic verifier is already unit-tested in Task 6; the harness is operator tooling like `scripts/reextract-all-sessions.py`, which is likewise not pytest-covered)

**Interfaces:**
- Consumes: live `/query` (`http://127.0.0.1:8999` on the VM); filter module functions `Filter`, `extract_grounding_facts`, `verify_answer_grounding`, `_recompute_metadata_summary`; Ollama `/api/chat`.
- Produces: JSON result files consumed by `--compare`; the before/after fabrication numbers for the v5 validation report.

- [ ] **Step 1: Create the adversarial query set**

Create `scripts/eval/fabrication-queries.yaml`. Session facts below were verified against the live corpus and the v4 validation forensics on 2026-07-01 (December 2025 sessions: 12-02, 12-09, 12-17, 12-30, 12-31; Adam James spoke in 10 sessions; Hemal+Garron co-occur in 2025-12-17; RecapFlow content in 2026-03-24; 97 chunks contain "codex"):

```yaml
# Adversarial fabrication probes for Community Brain (v5 design D11).
# target_sessions: session_dates that SHOULD be retrieved (recall metric).
#   Lists are verified-but-possibly-non-exhaustive; recall is measured
#   against the listed dates only.
# expect_refusal: the correct answer is a refusal (content doesn't exist).
# forbidden_dates: dates that must NOT appear in the answer (known traps).
queries:
  - id: iso-quiet-date
    class: quiet_session_date
    question: "What was discussed in the call on 2025-12-30?"
    target_sessions: ["2025-12-30"]
    expect_refusal: false
    forbidden_dates: []

  - id: phrased-date-with-day
    class: phrased_date
    question: "What did the community discuss in the coaching call from March 4th, 2026?"
    target_sessions: ["2026-03-04"]
    expect_refusal: false
    forbidden_dates: []

  - id: relative-late-december
    class: relative_date
    question: "What was discussed in late December 2025?"
    target_sessions: ["2025-12-17", "2025-12-30", "2025-12-31"]
    expect_refusal: false
    forbidden_dates: []

  - id: quarter-q1-2026
    class: quarter_date
    question: "What were the main themes across the Q1 2026 calls?"
    target_sessions: ["2026-01-07", "2026-02-25", "2026-03-04", "2026-03-24"]
    expect_refusal: false
    forbidden_dates: []

  - id: nonexistent-session
    class: nonexistent_date
    question: "Summarize the 2025-12-15 session."
    target_sessions: []
    expect_refusal: true
    forbidden_dates: ["2025-12-15"]

  - id: hemal-garron-conjunction
    class: rare_entity_date_conjunction
    question: "Did any discussions in late August or mid-December 2025 mention Hemal or Garron?"
    target_sessions: ["2025-08-20", "2025-08-27", "2025-12-17"]
    expect_refusal: false
    forbidden_dates: ["2025-12-15"]

  - id: adam-james-contributions
    class: speaker_enumeration
    question: "What are three contributions Adam James made on coaching calls?"
    target_sessions: ["2025-02-05", "2025-02-12", "2025-08-06", "2025-08-12", "2025-08-27", "2025-09-02", "2025-09-17", "2025-10-30", "2026-04-21", "2026-04-28"]
    expect_refusal: false
    forbidden_dates: []

  - id: garron-subscription-trap
    class: speaker_attribution_trap
    question: "What did Garron say about subscription models, and in which session?"
    target_sessions: ["2025-10-22", "2025-10-30", "2025-11-19", "2025-12-17", "2026-01-07"]
    expect_refusal: false
    forbidden_dates: ["2025-12-15"]

  - id: codex-production
    class: topic_coverage
    question: "Has anyone used Codex for production work?"
    target_sessions: []
    expect_refusal: false
    forbidden_dates: []

  - id: unresolved-survey
    class: unresolved_survey
    question: "List five questions from the calls that nobody fully answered."
    target_sessions: []
    expect_refusal: false
    forbidden_dates: []

  - id: fictitious-speaker
    class: fictitious_speaker
    question: "What did Zara Whitfield say about pricing?"
    target_sessions: []
    expect_refusal: true
    forbidden_dates: []

  - id: verbatim-quote-trap
    class: quote_trap
    question: "Quote exactly what Patrick said about RecapFlow."
    target_sessions: ["2026-03-24"]
    expect_refusal: false
    forbidden_dates: []
```

- [ ] **Step 2: Create the harness script**

Create `scripts/eval-fabrication.py` (make it executable):

```python
#!/usr/bin/env python3
"""Fabrication-rate evaluation harness for Community Brain (v5 design D11).

Phases:
  RETRIEVAL  POST /query per adversarial probe; measure target-session
             recall@top_k. Deterministic; no LLM required.
  ANSWER     (--answer) Render the LLM context with the REAL filter code,
             call the answering model via Ollama /api/chat with the
             canonical system prompt, then run the filter's own grounding
             verifier over the answer. Fabrication is measured by the same
             functions that enforce the guard in production.
  REPORT     Aggregate + write JSON. --compare BASELINE.json prints deltas.

Run from community-brain/ with its venv, e.g.:
  ./.venv/bin/python ../scripts/eval-fabrication.py --out eval-v5.json
  ./.venv/bin/python ../scripts/eval-fabrication.py --answer \
      --model community-brain-v5-gpt-oss:20b --out eval-v5-answers.json
  ./.venv/bin/python ../scripts/eval-fabrication.py --compare eval-v4.json eval-v5.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import httpx
import yaml

from community_brain.openwebui.community_brain_filter import (
    Filter,
    _recompute_metadata_summary,
    extract_grounding_facts,
    verify_answer_grounding,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_QUERIES = REPO_ROOT / "scripts" / "eval" / "fabrication-queries.yaml"
DEFAULT_SYSTEM_PROMPT = REPO_ROOT / "docs" / "inference-guidelines.md"

REFUSAL_PATTERNS = (
    "don't see",
    "do not see",
    "doesn't cover",
    "does not cover",
    "not in the retrieved",
    "no retrieved sources",
    "cannot answer",
    "can't answer",
    "don't have",
)


def looks_like_refusal(answer: str) -> bool:
    lowered = answer.lower()
    return any(p in lowered for p in REFUSAL_PATTERNS)


def load_queries(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)["queries"]


def run_retrieval(server: str, api_key: str, question: str, top_k: int) -> dict:
    resp = httpx.post(
        f"{server}/query",
        json={"question": question, "top_k": top_k},
        headers={"X-API-Key": api_key},
        timeout=60.0,
    )
    resp.raise_for_status()
    return resp.json()


def render_context(chunks: list[dict], min_score: float) -> tuple[str, list[dict]]:
    """Mirror production: min_score cutoff, recomputed summary, then the
    filter's real context builder."""
    kept = [c for c in chunks if c.get("similarity", 0) >= min_score]
    filt = Filter()
    if not kept:
        return filt._build_no_sources_message(), []
    summary = _recompute_metadata_summary(kept)
    return filt._build_sources_message(kept, summary), kept


def run_answer(
    ollama_url: str, model: str, system_prompt: str, context: str,
    question: str, temperature: float,
) -> str:
    resp = httpx.post(
        f"{ollama_url}/api/chat",
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": context},
                {"role": "user", "content": question},
            ],
            "stream": False,
            "options": {"temperature": temperature},
        },
        timeout=600.0,
    )
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def evaluate_query(q: dict, args) -> dict:
    result: dict = {"id": q["id"], "class": q["class"], "question": q["question"]}

    data = run_retrieval(args.server, args.api_key, q["question"], args.top_k)
    retrieved_sessions = sorted({
        (c.get("ground_truth") or {}).get("session_date", "")
        for c in data.get("chunks", [])
    } - {""})
    result["retrieved_sessions"] = retrieved_sessions
    result["injected_counts"] = sum(
        1
        for c in data.get("chunks", [])
        if (c.get("score_breakdown") or {}).get("injected_by")
    )
    targets = q.get("target_sessions") or []
    if targets:
        hit = len(set(targets) & set(retrieved_sessions))
        result["target_recall"] = hit / len(targets)
    else:
        result["target_recall"] = None

    if not args.answer:
        return result

    context, kept = render_context(data.get("chunks", []), args.min_score)
    answer = run_answer(
        args.ollama_url, args.model, args.system_prompt_text, context,
        q["question"], args.temperature,
    )
    result["answer"] = answer
    result["refused"] = looks_like_refusal(answer)
    result["refusal_correct"] = (
        result["refused"] if q.get("expect_refusal") else None
    )

    facts = extract_grounding_facts(context)
    if facts is not None:
        verdict = verify_answer_grounding(answer, facts)
        result["unverified_dates"] = verdict["unverified_dates"]
        result["unverified_sources"] = verdict["unverified_sources"]
        result["unverified_chunk_ids"] = verdict["unverified_chunk_ids"]
    else:
        # No sources retrieved: only explicit traps are checkable.
        result["unverified_dates"] = [
            d for d in (q.get("forbidden_dates") or []) if d in answer
        ]
        result["unverified_sources"] = []
        result["unverified_chunk_ids"] = []
    result["forbidden_date_hits"] = [
        d for d in (q.get("forbidden_dates") or []) if d in answer
    ]
    result["fabricated"] = bool(
        result["unverified_dates"]
        or result["unverified_sources"]
        or result["unverified_chunk_ids"]
        or result["forbidden_date_hits"]
    )
    return result


def aggregate(per_query: list[dict], answered: bool) -> dict:
    agg: dict = {"queries": len(per_query)}
    recalls = [r["target_recall"] for r in per_query if r["target_recall"] is not None]
    agg["mean_target_recall"] = (sum(recalls) / len(recalls)) if recalls else None
    agg["queries_with_injection"] = sum(
        1 for r in per_query if r.get("injected_counts", 0) > 0
    )
    if answered:
        answered_qs = [r for r in per_query if not r.get("refused")]
        agg["fabrication_rate"] = (
            (sum(1 for r in answered_qs if r.get("fabricated")) / len(answered_qs))
            if answered_qs
            else 0.0
        )
        refusal_probes = [r for r in per_query if r.get("refusal_correct") is not None]
        agg["refusal_correctness"] = (
            (sum(1 for r in refusal_probes if r["refusal_correct"]) / len(refusal_probes))
            if refusal_probes
            else None
        )
    return agg


def compare(baseline_path: Path, current_path: Path) -> None:
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    current = json.loads(current_path.read_text(encoding="utf-8"))
    print(f"baseline: {baseline_path}  →  current: {current_path}")
    for key in ("mean_target_recall", "fabrication_rate", "refusal_correctness",
                "queries_with_injection"):
        b = baseline.get("aggregates", {}).get(key)
        c = current.get("aggregates", {}).get(key)
        print(f"  {key}: {b} → {c}")
    b_by_id = {r["id"]: r for r in baseline.get("per_query", [])}
    for r in current.get("per_query", []):
        b = b_by_id.get(r["id"], {})
        if b.get("target_recall") != r.get("target_recall") or b.get(
            "fabricated"
        ) != r.get("fabricated"):
            print(
                f"  {r['id']}: recall {b.get('target_recall')} → "
                f"{r.get('target_recall')}, fabricated {b.get('fabricated')} → "
                f"{r.get('fabricated')}"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--server", default="http://127.0.0.1:8999")
    parser.add_argument(
        "--api-key", default=os.environ.get("RETRIEVAL_API_KEY") or ""
    )
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--min-score", type=float, default=0.2)
    parser.add_argument("--answer", action="store_true",
                        help="run the ANSWER phase via Ollama")
    parser.add_argument("--ollama-url", default="http://10.1.50.219:11434")
    parser.add_argument("--model", default="gpt-oss:20b")
    parser.add_argument("--system-prompt", type=Path, default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--out", type=Path, default=Path("eval-fabrication.json"))
    parser.add_argument("--compare", nargs=2, type=Path, metavar=("BASELINE", "CURRENT"))
    args = parser.parse_args()

    if args.compare:
        compare(args.compare[0], args.compare[1])
        return 0

    args.system_prompt_text = args.system_prompt.read_text(encoding="utf-8")
    queries = load_queries(args.queries)

    per_query = []
    for q in queries:
        print(f"[eval] {q['id']} ...", file=sys.stderr)
        try:
            per_query.append(evaluate_query(q, args))
        except httpx.HTTPError as exc:
            print(f"[eval] {q['id']} FAILED: {exc}", file=sys.stderr)
            per_query.append({"id": q["id"], "error": str(exc)})

    report = {
        "server": args.server,
        "top_k": args.top_k,
        "answer_phase": bool(args.answer),
        "model": args.model if args.answer else None,
        "temperature": args.temperature if args.answer else None,
        "per_query": per_query,
        "aggregates": aggregate(
            [r for r in per_query if "error" not in r], args.answer
        ),
    }
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["aggregates"], indent=2))
    print(f"[eval] wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Make it executable**

Run: `chmod +x ../scripts/eval-fabrication.py`

- [ ] **Step 4: Smoke-test argument parsing and YAML validity**

Run: `./.venv/bin/python ../scripts/eval-fabrication.py --help`
Expected: usage text, exit 0.

Run: `./.venv/bin/python -c "import yaml, pathlib; d = yaml.safe_load(pathlib.Path('../scripts/eval/fabrication-queries.yaml').read_text()); print(len(d['queries']))"`
Expected output: `12`

- [ ] **Step 5: Commit**

```bash
git add scripts/eval/fabrication-queries.yaml scripts/eval-fabrication.py
```
```bash
git commit -m "feat(scripts): fabrication-rate evaluation harness + adversarial probe set (v5 D11)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 12: Version bump, CHANGELOG, operator docs

**Files:**
- Modify: `community-brain/pyproject.toml`
- Modify: `docs/migrations/CHANGELOG.md` (repo root)
- Modify: `community-brain/CLAUDE.md`
- Modify: `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`

**Interfaces:**
- Produces: package version `0.5.0` (surfaces in `/health` `server_version` and `app.version`).

- [ ] **Step 1: Bump the version**

In `community-brain/pyproject.toml` change:

```toml
version = "0.3.0"
```

to:

```toml
version = "0.5.0"
```

- [ ] **Step 2: Re-link the editable install so `importlib.metadata` sees 0.5.0**

Run: `./.venv/bin/pip install -e ".[dev]"`

- [ ] **Step 3: Verify the version-source test agrees**

Run: `./.venv/bin/pytest tests/test_version_source.py -q`
Expected: 2 passed.

- [ ] **Step 4: CHANGELOG entry**

Append to `docs/migrations/CHANGELOG.md` (follow the existing entry format in that file; place it as the newest entry):

```markdown
## 2026-07-XX — Retrieval v5: grounding (candidate injection + citation guard)

No schema migration. Schema stays v1.1 (38 fields). No re-extract.

- **Cue-driven candidate injection**: cue rules with `recruit: true` in
  `config/query-cues.yaml` (and the speaker auto-rules) now pull targeted
  chunks into the candidate pool before the boost pass, fixing the v4
  pool-limit finding (date/rare-entity queries on quiet sessions missed
  entirely). Budgets: 10 per rule, 30 total per query. Recruitment ANDs
  the success guard and caller filters.
- **/query response (additive)**: `score_breakdown.injected_by` lists the
  recruitment rules that pulled a chunk into the pool (empty for
  pool-native chunks). No other contract change.
- **Filter citation guard**: the Open WebUI filter gained an `outlet`
  post-processing hook verifying session dates, `[SOURCE N]` refs, and
  chunk_id citations in the answer against the retrieved context.
  Valve `citation_guard`: annotate (default) / strip / off.
- **RetryConfig wired** into Stage B/C LLM calls (closes the v2 TODO):
  chunking.yaml `retry_attempts` / `retry_backoff_seconds` now honored.
- **lint_corpus** reports `unresolved_rate` and alarms above 50%.
- **Speaker auto-rule last-known-good cache** (incl. resolver snapshot).
- **Version note**: package metadata jumps 0.3.0 → 0.5.0; "0.4.0" existed
  only as a docs/deploy label and was never bumped in pyproject.toml.
```

(Replace `XX` with the actual commit date.)

- [ ] **Step 5: Update `community-brain/CLAUDE.md`**

(a) In "Known v2 backlog (don't rediscover)", DELETE the line:

```markdown
- **`RetryConfig`** loaded from `chunking.yaml` but not wired into Stage B/C LLM calls. `community_brain.llm.call_llm` has its own 3-retry default.
```

(b) In "Trade-offs we've deliberately kept", locate the bullet beginning `**`/query` ranking is hybrid (vector + BM25 RRF, k=60)...` and append to the end of that bullet:

```markdown
v5 adds cue-driven candidate injection: rules with `recruit: true` (plus the speaker auto-rules) pull up to 10 chunks each (30 max per query) into the pool via targeted queries before the boost pass; `score_breakdown.injected_by` records provenance. Note: injected chunks from semantically distant sessions can carry low cosine `similarity`; the Open WebUI filter's `min_score` valve (default 0.2) is safe, but raising it past ~0.3 trades away injection rescues.
```

(c) Add a new bullet to "Trade-offs we've deliberately kept":

```markdown
- **The filter verifies answers post-generation (v5).** `Filter.outlet` re-parses the injected context and flags/strips session dates, `[SOURCE N]` refs, and chunk_ids that don't resolve against the retrieved set (`citation_guard` valve: annotate/strip/off; deterministic, fail-open). The guard exists because gpt-oss:20b demonstrably ignores in-prompt verification scaffolding under specific-query/weak-retrieval pressure (v4 validation Q3). Re-uploading the filter resets ALL valves — re-set `retrieval_url`, `api_key`, and `citation_guard` after every upload.
```

- [ ] **Step 6: Update the handoff doc**

In `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`, insert a new section directly under the `## One outstanding track` heading level (as a sibling section above "### v4 design (when warranted)"):

```markdown
### Retrieval v5 — Grounding (candidate injection + citation guard) — IMPLEMENTED (2026-07)

Design + plan: `Patchou-plan` task 03 (external planning repo). Implements
v5 candidates #1 (cue-driven candidate injection), #2 (speaker auto-rule
LKG cache), #3 (`has_unresolved_question` alarm), #6 (filter-side citation
post-processing) and #8 options (b)+(c), plus the RetryConfig TODO.
Fabrication measurement: `scripts/eval-fabrication.py` +
`scripts/eval/fabrication-queries.yaml` (12 adversarial probes; run the
RETRIEVAL phase against a live server, ANSWER phase via Ollama).
Deployment: bump to 0.5.0, redeploy container, recreate the Open WebUI
custom model as `community-brain-v5-gpt-oss:20b` (temperature 0), re-upload
the filter and RE-SET VALVES (`retrieval_url`, `api_key`, `citation_guard`).
```

- [ ] **Step 7: Full suite one more time**

Run: `./.venv/bin/pytest tests/ -q`
Expected: all pass.

- [ ] **Step 8: Commit**

```bash
git add community-brain/pyproject.toml docs/migrations/CHANGELOG.md community-brain/CLAUDE.md docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md
```
```bash
git commit -m "docs(migrations): v5 CHANGELOG entry; bump community-brain to 0.5.0 (v5 D16)" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 13: Final verification, PR, and operator deployment checklist

**Files:** none new (verification + PR).

- [ ] **Step 1: Full suite, final**

Run: `./.venv/bin/pytest tests/ -q`
Expected: 0 failures. Record the total test count for the PR body.

- [ ] **Step 2: Push and open the PR**

```bash
git push -u origin feature/retrieval-v5-grounding
```
```bash
gh pr create --title "Retrieval v5: grounding — cue-driven candidate injection + filter citation guard" --body "Implements v5 per the locked design (Patchou-plan task 03, 2026-07-01). Candidate injection (D2-D7), filter outlet citation guard (D8-D10), fabrication eval harness (D11), speaker-rule LKG cache (D12), unresolved-rate alarm (D13), RetryConfig wiring (D14), prompt v5 rules (D15), version 0.5.0 (D16). No schema change, no re-extract, /query contract additive-only (score_breakdown.injected_by).

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

- [ ] **Step 3: BEFORE deploying — capture the v4 baseline with the new harness**

The deployed VM stack still runs v4 at this point; the harness runs from the branch checkout against it. Note: the baseline `injected_counts`/`injected_by` will be absent on v4 responses — the harness treats missing `score_breakdown.injected_by` as zero.

Run (RETRIEVAL phase): `./.venv/bin/python ../scripts/eval-fabrication.py --api-key "$RETRIEVAL_API_KEY" --out eval-baseline-v4-retrieval.json`

Run (ANSWER phase, against the deployed v4 custom model): `./.venv/bin/python ../scripts/eval-fabrication.py --answer --model community-brain-v4-gpt-oss:20b --api-key "$RETRIEVAL_API_KEY" --out eval-baseline-v4.json`

Expected: JSON aggregates printed; files written. Keep both files (do not commit them; they contain corpus content).

- [ ] **Step 4: OPERATOR-GATED — merge and deploy per the runbook**

Everything below follows `community-brain/docs/DEPLOYMENT.md` and its 🟢/🟡/🔴 permission model; do not improvise:

1. Merge the PR into `main` (operator approval).
2. On the VM: rebuild and restart the `retrieval-server` container (runbook procedure). Verify `curl http://127.0.0.1:8999/health` reports `"server_version": "0.5.0"`.
3. Open WebUI (manual, runbook "custom-model deploy step"): create custom model `community-brain-v5-gpt-oss:20b`, base `gpt-oss:20b`, system prompt = updated `prompts/community-brain-v4-openwebui-system-prompt.md` body, **temperature 0** (D15).
4. Re-upload `community_brain_filter.py` to Open WebUI Functions. **Re-set ALL valves** — `retrieval_url`, `api_key`, `top_k`, and the new `citation_guard` (uploading resets them; known v4 hazard).
5. Do NOT touch the Open WebUI image SHA (alembic hazard is out of v5 scope).

- [ ] **Step 5: OPERATOR-GATED — after-deploy eval + comparison**

Run: `./.venv/bin/python ../scripts/eval-fabrication.py --api-key "$RETRIEVAL_API_KEY" --out eval-v5-retrieval.json`

Run: `./.venv/bin/python ../scripts/eval-fabrication.py --answer --model community-brain-v5-gpt-oss:20b --api-key "$RETRIEVAL_API_KEY" --out eval-v5.json`

Run: `./.venv/bin/python ../scripts/eval-fabrication.py --compare eval-baseline-v4.json eval-v5.json`

**Acceptance targets (from the design):**
- `mean_target_recall` strictly improves (the injection classes — `iso-quiet-date`, `phrased-date-with-day`, `relative-late-december`, `adam-james-contributions`, `hemal-garron-conjunction` — are where the lift must show).
- `fabrication_rate` at or near 0 with the guard counted (any residual fabrication MUST now arrive annotated in Open WebUI).
- `refusal_correctness` = 1.0 on `nonexistent-session` and `fictitious-speaker`.

Record the numbers in a dated validation note at `docs/superpowers/validation/2026-07-XX-retrieval-v5-validation.md` (same style as the v4 validation doc) and commit it to `main`.

---

## Self-review notes (already applied)

- **Spec coverage:** D1–D16 all map to tasks (D1→scope; D2/D6/D7→T4; D3→T1+T10; D4→T2; D5→T3; D8→T7; D9/D10→T6; D11→T11+T13; D12→T5; D13→T9; D14→T8; D15→T10+T13; D16→T12).
- **Mock-signature blast radius:** exactly nine `(model, prompt)` side-effect functions enumerated in T8; extractor/session-extractor unit-test mocks intentionally untouched (their call path passes no retry_config).
- **Import-cycle handling:** `candidate_injection` ← `query_local` is module-level one way, function-level the other (documented in both files).
- **Golden-corpus risk:** T4 Step 2 gates fixture vocabulary before any retrieval code changes land.
