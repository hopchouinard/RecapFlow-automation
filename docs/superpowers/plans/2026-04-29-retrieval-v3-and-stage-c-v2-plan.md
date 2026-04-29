# Retrieval v3 + Stage C v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship v3 — Stage C extraction prompt revision (entities, speakers_mentioned, uniform keywords, enriched embed_text), speaker canonicalization operational pattern, F8 narrow fix (inline flags + corpus summary), corpus-lint recurrent marker, synthesized bm25_text FTS column, score breakdown in /query response, and YAML cue rules — as one coordinated release before Plan C kicks off the remaining ~57-session backfill.

**Architecture:** Single feature branch with 11 phases sequenced for dependencies. Schema bumps 1.0 → 1.1 (additive `bm25_text` column). Stage C bumps `chunk-extraction-v1` → `chunk-extraction-v2`. The 9 ingested sessions get re-extracted under the new contract once the registry is curated; validation gate (8 criteria) gates Plan C kickoff.

**Tech Stack:** Python 3.11, pytest, LanceDB 0.30.2 (FTS via Tantivy), Ollama nomic-embed-text, OpenRouter for Stage B/C LLMs, FastAPI, PyYAML, Pydantic.

**Reference docs:**
- Spec: `docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md`
- Audit data: spec Appendix A
- Existing v2 patterns: `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`, `community-brain/src/community_brain/query/cue_rules.py`
- Trust contract (do NOT break structurally): `docs/inference-guidelines.md`
- Schema rules: `community-brain/CLAUDE.md` "Non-negotiables"

**All test commands run from `community-brain/` with the venv activated** (`source .venv/bin/activate`). All implementation paths are relative to repo root unless noted.

---

## Phase 1 — Schema migration foundation

### Task 1: Add `bm25_text` field and bump SCHEMA_VERSION

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/schema.py`
- Test: `community-brain/tests/test_ingestion_schema.py`

- [ ] **Step 1: Write the failing tests**

Append to `community-brain/tests/test_ingestion_schema.py`:

```python
def test_chunk_dataclass_has_bm25_text_field():
    from dataclasses import fields
    from community_brain.ingestion.schema import Chunk
    field_names = {f.name for f in fields(Chunk)}
    assert "bm25_text" in field_names

def test_schema_version_is_1_1():
    from community_brain.ingestion.schema import SCHEMA_VERSION
    assert SCHEMA_VERSION == "1.1"

def test_pyarrow_schema_includes_bm25_text():
    from community_brain.ingestion.schema import pyarrow_table_schema
    schema = pyarrow_table_schema()
    field_names = [f.name for f in schema]
    assert "bm25_text" in field_names
    bm25_field = schema.field("bm25_text")
    assert str(bm25_field.type) == "string"

def test_lancedb_schema_dict_includes_bm25_text():
    from community_brain.ingestion.schema import lancedb_table_schema
    descr = lancedb_table_schema()
    assert descr.get("bm25_text") == "string"

def test_chunk_dataclass_has_38_fields():
    from dataclasses import fields
    from community_brain.ingestion.schema import Chunk
    assert len(fields(Chunk)) == 38
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_ingestion_schema.py -v -k "bm25 or schema_version_is or 38_fields"
```

Expected: 5 FAILs.

- [ ] **Step 3: Update schema.py**

In `community-brain/src/community_brain/ingestion/schema.py`:

Change `SCHEMA_VERSION = "1.0"` to `SCHEMA_VERSION = "1.1"`.

Add a new field at the end of the `Chunk` dataclass `# --- Content & embedding (3) ---` section, between `full_text` and `embedding`:

```python
    # --- Content & embedding (4) ---
    embed_text: str
    full_text: str
    bm25_text: str
    embedding: list[float]
```

Update the comment header from `(3)` to `(4)`.

In `pyarrow_table_schema()`, add `("bm25_text", pa.string()),` between the existing `("full_text", pa.string()),` and `("embedding", pa.list_(pa.float32(), EMBEDDING_DIM)),` lines.

In `lancedb_table_schema()`, add `"bm25_text": "string",` between `"full_text": "string",` and `"embedding": "list[float]",`.

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_ingestion_schema.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/schema.py community-brain/tests/test_ingestion_schema.py
git commit -m "$(cat <<'EOF'
feat(ingestion): add bm25_text column; bump SCHEMA_VERSION to 1.1

Additive change for v3: bm25_text holds the synthesized
concatenation of structured fields + full_text, used as the FTS
index target column (replacing full_text-only indexing). Schema
parity tests updated to the new 38-field shape.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Add `bm25_text` synthesis helper

**Files:**
- Create: `community-brain/src/community_brain/ingestion/bm25_synthesis.py`
- Test: `community-brain/tests/test_bm25_synthesis.py`

- [ ] **Step 1: Write the failing test**

Create `community-brain/tests/test_bm25_synthesis.py`:

```python
"""Tests for bm25_text synthesis."""
from __future__ import annotations

from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text


def test_synthesize_includes_all_fields():
    result = synthesize_bm25_text(
        topic_label="Sales funnel discussion",
        entities=["Adam James", "Gold Flamingo"],
        speakers_spoke=["Brandon Hancock"],
        speakers_mentioned=["Andrej Karpathy"],
        keywords=["LinkedIn", "outreach"],
        full_text="01:23:45 - Brandon Hancock\nAdam, what's next for the funnel?",
    )
    assert "Sales funnel discussion" in result
    assert "Adam James" in result
    assert "Gold Flamingo" in result
    assert "Brandon Hancock" in result
    assert "Andrej Karpathy" in result
    assert "LinkedIn" in result
    assert "outreach" in result
    assert "Adam, what's next for the funnel?" in result


def test_synthesize_handles_empty_lists():
    result = synthesize_bm25_text(
        topic_label="Generic topic",
        entities=[],
        speakers_spoke=[],
        speakers_mentioned=[],
        keywords=[],
        full_text="some content",
    )
    # No crash; full_text and topic_label preserved.
    assert "Generic topic" in result
    assert "some content" in result


def test_synthesize_handles_none_lists_as_empty():
    result = synthesize_bm25_text(
        topic_label="Some topic",
        entities=None,
        speakers_spoke=None,
        speakers_mentioned=None,
        keywords=None,
        full_text="content",
    )
    assert "Some topic" in result
    assert "content" in result


def test_synthesize_handles_none_topic_label():
    result = synthesize_bm25_text(
        topic_label=None,
        entities=["X"],
        speakers_spoke=[],
        speakers_mentioned=[],
        keywords=[],
        full_text="text",
    )
    assert "X" in result
    assert "text" in result


def test_synthesize_separates_with_newlines():
    result = synthesize_bm25_text(
        topic_label="topic",
        entities=["e1", "e2"],
        speakers_spoke=["s1"],
        speakers_mentioned=[],
        keywords=["k1"],
        full_text="body",
    )
    # Each section on its own line; entities and keywords joined within their line by ", ".
    lines = result.split("\n")
    assert "topic" in lines
    assert "e1, e2" in lines
    assert "s1" in lines
    assert "k1" in lines
    assert "body" in lines
```

- [ ] **Step 2: Run the test to verify it fails**

```bash
./.venv/bin/pytest tests/test_bm25_synthesis.py -v
```

Expected: import error / FAIL.

- [ ] **Step 3: Implement the synthesizer**

Create `community-brain/src/community_brain/ingestion/bm25_synthesis.py`:

```python
"""bm25_text synthesis for v3 hybrid retrieval.

The synthesized field concatenates structured metadata (topic_label,
entities, speakers_spoke, speakers_mentioned, keywords) with the chunk's
full_text. The FTS index targets this column rather than full_text-only
so lexical retrieval benefits from the extracted structured fields.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §10
"""
from __future__ import annotations


def synthesize_bm25_text(
    *,
    topic_label: str | None,
    entities: list[str] | None,
    speakers_spoke: list[str] | None,
    speakers_mentioned: list[str] | None,
    keywords: list[str] | None,
    full_text: str,
) -> str:
    """Build the bm25_text representation for a chunk.

    Layout (one section per line, empty sections render as empty strings):

        <topic_label or "">
        <entities joined with ", ">
        <speakers_spoke joined with ", ">
        <speakers_mentioned joined with ", ">
        <keywords joined with ", ">
        <full_text>

    None list values are normalized to empty.
    """
    parts = [
        topic_label or "",
        ", ".join(entities or []),
        ", ".join(speakers_spoke or []),
        ", ".join(speakers_mentioned or []),
        ", ".join(keywords or []),
        full_text,
    ]
    return "\n".join(parts)
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
./.venv/bin/pytest tests/test_bm25_synthesis.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/bm25_synthesis.py community-brain/tests/test_bm25_synthesis.py
git commit -m "$(cat <<'EOF'
feat(ingestion): add bm25_text synthesis helper

Pure helper that concatenates topic_label, entities, speakers_spoke,
speakers_mentioned, keywords, and full_text into the bm25_text
column synthesized at chunk write time. Tested for None/empty
list normalization and field-presence invariants.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Pipeline populates `bm25_text` on chunk commit

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/pipeline.py`
- Test: `community-brain/tests/test_ingestion_pipeline.py`

- [ ] **Step 1: Read existing pipeline to find chunk-build site**

```bash
grep -n "Chunk(" community-brain/src/community_brain/ingestion/pipeline.py | head -10
```

Note the line number where Chunk dataclass instances are constructed (the chunk-build site that will receive the new `bm25_text` argument).

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_ingestion_pipeline.py`:

```python
def test_pipeline_populates_bm25_text_on_commit(
    tmp_path, monkeypatch, mocked_pipeline_env
):
    """Chunks committed by ingest_session must have bm25_text containing
    topic_label, entities, speakers_spoke, speakers_mentioned, keywords,
    and full_text content concatenated.
    """
    # Reuse existing test fixture pattern in this file. The pipeline writes
    # chunks via _commit_chunks; after commit, bm25_text must be present
    # and non-empty for every row.
    import lancedb
    from community_brain.ingestion.pipeline import ingest_session

    # ... reuse the existing harness pattern (look at e.g.
    # test_pipeline_writes_chunks for the canonical form). Assert after
    # ingest:
    #   db = lancedb.connect(<path>)
    #   tbl = db.open_table("chunks")
    #   rows = tbl.to_arrow().to_pylist()
    #   for row in rows:
    #       assert row["bm25_text"], f"empty bm25_text on {row['chunk_id']}"
    #       # bm25_text contains full_text content
    #       assert row["full_text"][:50] in row["bm25_text"]
```

> **Note:** Read existing tests in `test_ingestion_pipeline.py` for the exact fixture/mock pattern this codebase uses for `ingest_session` integration tests. Mirror that pattern; the assertions above describe what to check.

- [ ] **Step 3: Run the test to verify it fails**

```bash
./.venv/bin/pytest tests/test_ingestion_pipeline.py::test_pipeline_populates_bm25_text_on_commit -v
```

Expected: FAIL with KeyError on `bm25_text` or assertion failure.

- [ ] **Step 4: Wire bm25_text synthesis into pipeline**

In `community-brain/src/community_brain/ingestion/pipeline.py`:

Add the import near the top with other ingestion imports:

```python
from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
```

Locate the chunk-construction site (where `Chunk(...)` is instantiated with all 37 fields). Add `bm25_text` to the kwargs:

```python
chunk = Chunk(
    # ... existing 37 fields ...
    embed_text=embed_text,
    full_text=full_text,
    bm25_text=synthesize_bm25_text(
        topic_label=topic_label,
        entities=entities,
        speakers_spoke=speakers_spoke,
        speakers_mentioned=speakers_mentioned,
        keywords=keywords,
        full_text=full_text,
    ),
    embedding=embedding,
)
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
./.venv/bin/pytest tests/test_ingestion_pipeline.py::test_pipeline_populates_bm25_text_on_commit -v
```

Expected: PASS.

- [ ] **Step 6: Run the full pipeline test suite to catch regressions**

```bash
./.venv/bin/pytest tests/test_ingestion_pipeline.py -v
```

Expected: all PASS (existing tests should not regress on the additive field).

- [ ] **Step 7: Commit**

```bash
git add community-brain/src/community_brain/ingestion/pipeline.py community-brain/tests/test_ingestion_pipeline.py
git commit -m "$(cat <<'EOF'
feat(ingestion): synthesize bm25_text at chunk write time

Pipeline now populates the bm25_text column at chunk construction
using synthesize_bm25_text. New chunks land searchable via FTS
over the structured-field-enriched representation.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 2 — Stage C v2 prompt and extraction

### Task 4: Write the `chunk-extraction-v2.md` prompt

**Files:**
- Create: `community-brain/config/extraction-prompts/chunk-extraction-v2.md`

- [ ] **Step 1: Write the new prompt**

Create `community-brain/config/extraction-prompts/chunk-extraction-v2.md`:

````markdown
# Chunk Extraction Prompt (v2)

You extract structured metadata from a single chunk of conversational content. Your output MUST be valid JSON matching the schema described below. Do not include any prose, markdown, or explanation outside the JSON.

## Input context

You will receive:
- `CHUNK_TEXT` — the full text of the chunk (may include speaker attribution, segment headers, inline tags)
- `ENTITY_REGISTRY` — list of canonical entity names and their aliases (informational only — see entities rule below)
- `SPEAKER_ALIASES` — list of canonical speaker names and their aliases (informational only — see speakers rule below)

## Output schema (JSON)

```json
{
  "topic_label": "short descriptive label for this chunk's central topic",
  "entities": ["all proper-noun entities mentioned in CHUNK_TEXT, raw form unless registry recognizes them"],
  "speakers_mentioned": ["subset of entities that are PEOPLE, EXCLUDING anyone in speakers_spoke for this chunk"],
  "keywords": ["topical keywords / concepts / techniques / tools mentioned"],
  "speech_acts": ["one or more of: question | answer | opinion | recommendation | warning | anecdote | decision | action_item | prediction | comparison | definition"],
  "stance": "positive | negative | neutral | mixed | null",
  "certainty": "asserted | hedged | speculative",
  "chunk_local_markers": ["zero or more of: emphasized | sustained | breakthrough | resolved"],
  "decisions": ["zero or more concrete decisions/conclusions stated in the chunk"],
  "action_items": ["zero or more explicit commitments like 'X will do Y'"],
  "external_refs": ["zero or more URLs, paper titles, or resource references mentioned"],
  "references_prior": true,
  "has_question": true,
  "has_answer": true,
  "has_unresolved_question": true,
  "has_insight": true
}
```

## Extraction rules

### entities

Extract ALL proper-noun entities mentioned in CHUNK_TEXT across these four categories:

- **People** — proper-noun human names ("Adam James", "Andrej Karpathy"). When SPEAKER_ALIASES recognizes the name (canonical or alias), use the canonical form. Otherwise use the raw form as it appears.
- **Companies / orgs** — "OpenAI", "Anthropic", "Gold Flamingo", "Microsoft".
- **Products / tools** — "Claude Code", "Cursor", "n8n", "LanceDB", "Ollama", "Sonnet 4.6".
- **Frameworks / standards / techniques** — "RAG", "MCP", "OAuth", "BM25".

Excluded:
- Places (city, country names) — rarely meaningful in this corpus.
- URLs, hashes, commit refs — these go in `external_refs`.
- Generic nouns ("the team", "users", "developers").

Normalization:
- Case-preserved canonical form ("Claude Code" not "claude code").
- De-duplicated within a chunk (same entity twice in CHUNK_TEXT → one entry).

The pipeline applies a separate canonicalization pass at chunk write time to map raw extracted names to registry canonicals; you don't need to canonicalize unrecognized names yourself.

### speakers_mentioned

Output the deterministic subset of `entities` that satisfies BOTH:
1. The entity is a person (category 1 above).
2. The person is NOT one of the speakers_spoke for this chunk (i.e., they're talked-about, not present).

Empty list if the chunk has no people-typed entities, or all such entities are also in speakers_spoke.

### keywords

Topical keywords / concepts / techniques / tools mentioned. 5-15 entries per chunk (target ~10).

- De-duplicate within a chunk.
- Lower-case unless the term is conventionally capitalized ("RAG" stays uppercase; "context window" stays lowercase).
- Apply uniformly to all content types: prepared_transcript, extracted_signal, community_post.

### topic_label

A short (3-12 word) descriptive label for the chunk's central topic. For prepared_transcript chunks: descriptive ("Sales Funnel Optimization for Law Firms"). For extracted_signal chunks: section labels are fine ("decisions", "action_items", "general"). For community_post chunks: section labels ("session_narrative", or content-derived if richer signal is available).

### speech_acts

List all that apply. A chunk may contain multiple. Empty list `[]` for pure exposition. Do NOT return null.

### stance

Positive/negative/neutral about the chunk's main topic or entity. Use "mixed" when the speaker explicitly weighs pros and cons. Use null when stance isn't applicable (pure factual exposition, questions-only chunks).

### certainty

"asserted" for confident claims; "hedged" when the speaker uses "I think", "maybe", "probably"; "speculative" for "what if" or "I imagine" framing.

### chunk_local_markers

- `emphasized` — speakers explicitly signal importance ("this is key", "the big thing is", "I want to stress")
- `sustained` — multiple speakers engage across 3+ turns on the same specific point
- `breakthrough` — speakers frame as novel ("I just realized", "this changes how I think about X")
- `resolved` — contains a decision, conclusion, or closed question

### decisions, action_items, external_refs

Same semantics as v1: short self-contained strings; concrete decisions / explicit commitments / verbatim or clear references. Empty list when none.

### references_prior

`true` if the chunk explicitly refers to a previous session or earlier discussion ("like we discussed last week"); `false` otherwise.

### has_question, has_answer, has_unresolved_question, has_insight

Boolean flags:
- `has_question`: chunk contains an explicit question (whether asked rhetorically or to elicit response).
- `has_answer`: chunk contains a direct answer to an earlier or same-chunk question.
- `has_unresolved_question`: chunk contains a question that is left open without resolution within the chunk. Include subtle cases (awkward pause, soft topic-change after the question).
- `has_insight`: chunk contains a learning, realization, or substantive takeaway worth remembering.

## Rules

- Output ONLY the JSON object. No prose before or after.
- Every field must be present. Use `null` for scalar fields (like `stance`) when not applicable; use `[]` for list fields (like `speech_acts`, `entities`, `decisions`) when empty. Never omit a field.
- Do not invent content. Only extract what's explicitly present.
- When in doubt, prefer null / empty list over guessing.
- The v1 fields `new_entities_seen` and `new_speakers_seen` are no longer part of the output schema. The pipeline canonicalization pass handles new-name tracking.
````

- [ ] **Step 2: Commit**

```bash
git add community-brain/config/extraction-prompts/chunk-extraction-v2.md
git commit -m "$(cat <<'EOF'
feat(ingestion): add chunk-extraction-v2 prompt

Stage C v2 prompt: typed entities (4 categories, raw form unless
registry recognizes), speakers_mentioned as deterministic subset,
keywords uniform across content types, topic_label retained,
boolean has_* flags emitted directly. Drops new_entities_seen /
new_speakers_seen — canonicalization pass handles new-name tracking.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: Wire `extraction-config.yaml` to v2

**Files:**
- Modify: `community-brain/config/extraction-config.yaml`

- [ ] **Step 1: Inspect current config**

```bash
cat community-brain/config/extraction-config.yaml
```

Note the existing key holding the chunk-extraction prompt version. Likely `chunk_extraction_prompt_version: chunk-extraction-v1` or similar.

- [ ] **Step 2: Bump the active version**

Change the value from `chunk-extraction-v1` to `chunk-extraction-v2` in `community-brain/config/extraction-config.yaml`. Preserve all other keys exactly.

- [ ] **Step 3: Verify config loads**

```bash
./.venv/bin/python -c "
from community_brain.ingestion.config_loader import load_extraction_config
cfg = load_extraction_config()
print(cfg)
"
```

Expected: prints the config dict with the new version visible.

- [ ] **Step 4: Commit**

```bash
git add community-brain/config/extraction-config.yaml
git commit -m "$(cat <<'EOF'
config(community-brain): bump active chunk extraction prompt to v2

Switches the production prompt from chunk-extraction-v1 to v2.
Idempotency anchor on extraction_prompt_version forces re-extraction
of any v1 chunks that hit /ingest with force_reextract: true.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 6: Update extractor + tests for v2 outputs

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/extractor.py`
- Modify: `community-brain/tests/test_ingestion_extractor.py`

- [ ] **Step 1: Read existing extractor.py to find the parser**

```bash
grep -n "new_entities_seen\|new_speakers_seen\|extracted\|\"entities\"" community-brain/src/community_brain/ingestion/extractor.py
```

Identify where the LLM JSON response is parsed and validated. v1 expected `new_entities_seen` / `new_speakers_seen` in the output; v2 drops these fields.

- [ ] **Step 2: Write the failing tests**

In `community-brain/tests/test_ingestion_extractor.py`, add tests that validate the v2 contract:

```python
def test_extractor_v2_accepts_response_without_new_entities_seen(monkeypatch):
    """v2 LLM response shape drops new_entities_seen / new_speakers_seen.
    The extractor should accept the v2 shape without raising."""
    from community_brain.ingestion import extractor

    v2_response = {
        "topic_label": "Sales funnel optimization",
        "entities": ["Adam James", "Gold Flamingo", "LinkedIn"],
        "speakers_mentioned": ["Andrej Karpathy"],
        "keywords": ["funnel", "outreach", "law firms"],
        "speech_acts": ["question", "recommendation"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": ["Adam will draft a sample funnel by Friday"],
        "external_refs": [],
        "references_prior": False,
        "has_question": True,
        "has_answer": False,
        "has_unresolved_question": True,
        "has_insight": True,
    }

    monkeypatch.setattr(extractor, "_call_llm", lambda *a, **kw: '{"json": "is_set_below"}')
    # Replace _call_llm to return our v2 response directly. The exact monkeypatch
    # signature should mirror existing patterns in this file — see e.g.
    # test_extractor_returns_chunk_metadata for the canonical example.
    # Then assert no KeyError, and that the parsed result has the new fields.
```

> **Note:** Read existing extractor tests for the exact `_call_llm` mock pattern; mirror it. Add additional assertions: parsed result has `entities` populated; `speakers_mentioned` populated; `keywords` populated; `has_*` flags returned as bools.

- [ ] **Step 3: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_ingestion_extractor.py -v -k "v2"
```

Expected: FAIL with KeyError on `new_entities_seen` (or wherever the v1 parser breaks).

- [ ] **Step 4: Update extractor.py**

In `community-brain/src/community_brain/ingestion/extractor.py`:

- Remove handling of `new_entities_seen` and `new_speakers_seen` from the LLM response parser. Drop these keys from the validation requirements; remove any pending-queue write-out logic that depended on them (the canonicalization pass in Task 9 will handle this differently).
- Add validation that `topic_label`, `keywords`, `speakers_mentioned`, `has_question`, `has_answer`, `has_unresolved_question`, `has_insight` are present in the parsed response.
- Pass through these new fields to the chunk record so `pipeline.py` can read them at chunk-build time.

The exact code change depends on the existing structure. Check `extractor.py` for the LLM-response-parsing function (likely `_parse_extraction_response` or similar) and modify it.

- [ ] **Step 5: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_ingestion_extractor.py -v
```

Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/ingestion/extractor.py community-brain/tests/test_ingestion_extractor.py
git commit -m "$(cat <<'EOF'
feat(ingestion): wire extractor to Stage C v2 contract

Drops new_entities_seen / new_speakers_seen handling from the
LLM-response parser. Validates v2-required fields (topic_label,
keywords, speakers_mentioned, has_* flags) on parse. Pipeline can
now build Chunks with the v2 outputs.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 7: Enrich `embed_text` synthesis for transcripts

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/embedding.py` (or wherever transcript embed_text is built — verify with grep)
- Test: `community-brain/tests/test_ingestion_embedding.py`

- [ ] **Step 1: Locate transcript embed_text synthesis**

```bash
grep -rn "topic:.*summary:" community-brain/src/community_brain/ingestion/
```

Identify the function that builds the transcript-only `embed_text` string in the form `"topic: <X>\nsummary: <Y>"`.

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_ingestion_embedding.py`:

```python
def test_transcript_embed_text_includes_enriched_fields():
    """v3 enriches embed_text for prepared_transcript with speakers,
    mentions, entities, keywords (in addition to topic + summary)."""
    from community_brain.ingestion.embedding import build_transcript_embed_text

    result = build_transcript_embed_text(
        topic_label="Sales funnel optimization",
        speakers_spoke=["Brandon Hancock", "Patrick Chouinard"],
        speakers_mentioned=["Andrej Karpathy"],
        entities=["Adam James", "Gold Flamingo"],
        keywords=["LinkedIn", "outreach"],
        summary="Adam discussed his sales funnel approach for law firms.",
    )
    # Topic, speakers, mentions, entities, keywords, summary all present.
    for token in ("Sales funnel optimization", "Brandon Hancock",
                  "Patrick Chouinard", "Andrej Karpathy", "Adam James",
                  "Gold Flamingo", "LinkedIn", "outreach",
                  "Adam discussed"):
        assert token in result, f"Missing token: {token}"


def test_transcript_embed_text_handles_empty_lists():
    from community_brain.ingestion.embedding import build_transcript_embed_text
    result = build_transcript_embed_text(
        topic_label="Topic",
        speakers_spoke=[],
        speakers_mentioned=[],
        entities=[],
        keywords=[],
        summary="Summary text",
    )
    # No crash; topic and summary still present.
    assert "Topic" in result
    assert "Summary text" in result
```

- [ ] **Step 3: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_ingestion_embedding.py -v -k "enriched or empty_lists"
```

Expected: FAIL.

- [ ] **Step 4: Add the enriched synthesizer**

Add to `community-brain/src/community_brain/ingestion/embedding.py` (replace or update the transcript-embed-text function):

```python
def build_transcript_embed_text(
    *,
    topic_label: str | None,
    speakers_spoke: list[str] | None,
    speakers_mentioned: list[str] | None,
    entities: list[str] | None,
    keywords: list[str] | None,
    summary: str,
) -> str:
    """Synthesize embed_text for a prepared_transcript chunk.

    v3 format (per spec §6.4): structured-field-enriched layout.
    Vector retrieval grips on proper nouns + keywords + topic + summary,
    not on raw conversation. Hybrid retrieval (BM25 over bm25_text)
    covers raw-conversation lexical search separately.

        topic: <topic_label>
        speakers: <speakers_spoke joined>
        mentions: <speakers_mentioned joined>
        entities: <entities joined>
        keywords: <keywords joined>
        summary: <LLM-written summary>
    """
    return (
        f"topic: {topic_label or ''}\n"
        f"speakers: {', '.join(speakers_spoke or [])}\n"
        f"mentions: {', '.join(speakers_mentioned or [])}\n"
        f"entities: {', '.join(entities or [])}\n"
        f"keywords: {', '.join(keywords or [])}\n"
        f"summary: {summary}"
    )
```

Update the call site in `pipeline.py` (or wherever this function is invoked for transcript chunks) to pass the new arguments.

- [ ] **Step 5: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_ingestion_embedding.py -v
```

Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/ingestion/embedding.py community-brain/src/community_brain/ingestion/pipeline.py community-brain/tests/test_ingestion_embedding.py
git commit -m "$(cat <<'EOF'
feat(ingestion): enrich embed_text for transcripts with structured fields

v3 transcript embed_text now includes speakers, mentions, entities,
and keywords alongside topic + summary. Vector retrieval becomes
entity-aware while preserving thematic compression.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 3 — Speaker canonicalization

### Task 8: Create canonicalization pass module

**Files:**
- Create: `community-brain/src/community_brain/ingestion/canonicalize.py`
- Test: `community-brain/tests/test_canonicalize.py`

- [ ] **Step 1: Write the failing test**

Create `community-brain/tests/test_canonicalize.py`:

```python
"""Tests for the canonicalization pass."""
from __future__ import annotations

import pytest

from community_brain.ingestion.canonicalize import (
    build_alias_map,
    canonicalize_names,
)


def test_build_alias_map_inverts_registry():
    """build_alias_map produces alias -> canonical lookup from speaker-aliases.yaml shape."""
    registry = {
        "aliases": {
            "Adam James": ["Adam", "Adam - Gold Flamingo"],
            "Delvis Nunez": ["delvis"],
        },
        "pending": [],
    }
    m = build_alias_map(registry)
    assert m["Adam"] == "Adam James"
    assert m["Adam - Gold Flamingo"] == "Adam James"
    assert m["delvis"] == "Delvis Nunez"


def test_build_alias_map_includes_canonical_self_reference():
    """Canonicals also map to themselves so canonicalize_names is idempotent."""
    registry = {"aliases": {"Adam James": ["Adam"]}, "pending": []}
    m = build_alias_map(registry)
    assert m["Adam James"] == "Adam James"


def test_canonicalize_names_replaces_aliases():
    alias_map = {"Adam": "Adam James", "delvis": "Delvis Nunez"}
    raw = ["Adam", "Brandon Hancock", "delvis"]
    canonical, unknown = canonicalize_names(raw, alias_map)
    assert canonical == ["Adam James", "Brandon Hancock", "Delvis Nunez"]
    assert unknown == ["Brandon Hancock"]


def test_canonicalize_names_preserves_unknown():
    alias_map = {"Adam": "Adam James"}
    raw = ["Tony", "Adam"]
    canonical, unknown = canonicalize_names(raw, alias_map)
    assert "Tony" in canonical
    assert "Adam James" in canonical
    assert "Tony" in unknown


def test_canonicalize_names_deduplicates():
    """Two raw forms that map to the same canonical produce one entry."""
    alias_map = {"Adam": "Adam James", "Adam - Gold Flamingo": "Adam James"}
    raw = ["Adam", "Adam - Gold Flamingo"]
    canonical, _ = canonicalize_names(raw, alias_map)
    assert canonical == ["Adam James"]


def test_canonicalize_names_handles_none_input():
    canonical, unknown = canonicalize_names(None, {"X": "Y"})
    assert canonical == []
    assert unknown == []


def test_canonicalize_names_handles_empty_alias_map():
    canonical, unknown = canonicalize_names(["Tony", "Adam"], {})
    assert canonical == ["Tony", "Adam"]
    assert set(unknown) == {"Tony", "Adam"}
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_canonicalize.py -v
```

Expected: import errors.

- [ ] **Step 3: Implement the module**

Create `community-brain/src/community_brain/ingestion/canonicalize.py`:

```python
"""Canonicalization pass for v3 person-bearing fields.

Applies the speaker-aliases.yaml alias map to extracted name lists at
chunk write time and during the recanonicalize pass. Returns the
canonical-form list plus any unknown names that should be appended to
the registry's pending: queue.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §7
"""
from __future__ import annotations


def build_alias_map(registry: dict) -> dict[str, str]:
    """Invert a speaker-aliases.yaml-shape registry into alias->canonical lookup.

    Each canonical name is also mapped to itself so callers don't need
    to special-case "is this already canonical?".
    """
    aliases = registry.get("aliases") or {}
    out: dict[str, str] = {}
    for canonical, alias_list in aliases.items():
        out[canonical] = canonical
        for alias in alias_list or []:
            out[alias] = canonical
    return out


def canonicalize_names(
    raw_names: list[str] | None,
    alias_map: dict[str, str],
) -> tuple[list[str], list[str]]:
    """Apply alias_map to raw_names; return (canonical_list, unknown_list).

    canonical_list: input names with each replaced by its canonical form
        when alias_map has it; raw form retained otherwise. De-duplicated
        while preserving first-occurrence order.
    unknown_list: names not present in alias_map (returned in raw form,
        for the caller to append to the registry's pending queue).
    """
    if not raw_names:
        return [], []
    seen: set[str] = set()
    canonical: list[str] = []
    unknown: list[str] = []
    for name in raw_names:
        resolved = alias_map.get(name, name)
        if resolved not in seen:
            seen.add(resolved)
            canonical.append(resolved)
        if name not in alias_map:
            unknown.append(name)
    return canonical, unknown
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_canonicalize.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/canonicalize.py community-brain/tests/test_canonicalize.py
git commit -m "$(cat <<'EOF'
feat(ingestion): add canonicalization pass module

build_alias_map inverts the speaker-aliases registry; canonicalize_names
applies the map to raw extracted name lists, returning canonical
forms + the unknown subset for pending: queue tracking.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 9: Pipeline applies canonicalization at chunk write

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/pipeline.py`
- Test: `community-brain/tests/test_ingestion_pipeline.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_ingestion_pipeline.py`:

```python
def test_pipeline_applies_canonicalization_at_write(
    tmp_path, monkeypatch, mocked_pipeline_env
):
    """When the registry has 'Adam' -> 'Adam James', a chunk whose Stage C
    output extracted speakers_spoke=['Adam'] commits with speakers_spoke=['Adam James']."""
    # Setup: mock the LLM to return a Stage C v2 response with raw 'Adam';
    # ensure speaker-aliases.yaml has Adam James canonical with Adam alias.
    # After ingest, open the LanceDB and assert speakers_spoke contains
    # the canonical 'Adam James' form, not raw 'Adam'.
```

> **Note:** Mirror the harness pattern from existing pipeline tests. Use `mocked_pipeline_env` fixture (from existing test infra) to inject the alias registry; mock `_call_llm` to return a known Stage C v2 response with raw names.

- [ ] **Step 2: Run the test to verify it fails**

```bash
./.venv/bin/pytest tests/test_ingestion_pipeline.py::test_pipeline_applies_canonicalization_at_write -v
```

Expected: FAIL — speakers_spoke still has raw 'Adam' on commit.

- [ ] **Step 3: Wire canonicalization into pipeline**

In `community-brain/src/community_brain/ingestion/pipeline.py`:

Add the import:

```python
from community_brain.ingestion.canonicalize import build_alias_map, canonicalize_names
```

In the chunk-construction site (where Stage C outputs are read into the Chunk), apply canonicalization to the three person-bearing fields BEFORE the Chunk is built:

```python
# Load registry once per session ingest (cheap; YAML parse + dict construction)
registry = load_speaker_aliases_registry()  # use existing loader pattern
alias_map = build_alias_map(registry)

# Per chunk:
canon_speakers_spoke, unknown_speakers = canonicalize_names(speakers_spoke, alias_map)
canon_speakers_mentioned, unknown_mentioned = canonicalize_names(speakers_mentioned, alias_map)
canon_entities, unknown_entities_people = canonicalize_names(entities, alias_map)
# Note: canonicalize_names is applied to all entries in entities; non-people
# entries pass through unchanged (no map entry → returned as-is). The "unknown"
# set captures BOTH non-people entities and unrecognized people — at
# write-time-pending-queue level we only want to append unrecognized
# PEOPLE names. Filter unknown sets against the existing aliases'
# canonicals to identify person-typed unknowns vs general unknowns.
```

> **Note:** The exact integration depends on existing pipeline structure. The key invariant: at chunk-write time, `speakers_spoke`, `speakers_mentioned`, and `entities` contain canonical-when-known, raw-when-unknown forms. Unknown speakers go to `pending:` queue (existing pattern); unknown entities currently have no analogous registry — future work, not in v3.

- [ ] **Step 4: Run the test to verify it passes**

```bash
./.venv/bin/pytest tests/test_ingestion_pipeline.py::test_pipeline_applies_canonicalization_at_write -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/pipeline.py community-brain/tests/test_ingestion_pipeline.py
git commit -m "$(cat <<'EOF'
feat(ingestion): apply canonicalization to person-bearing fields at write

Pipeline now applies the speaker-aliases.yaml alias map to
speakers_spoke, speakers_mentioned, and entities at chunk
construction. Unknown speakers continue to flow to the pending:
queue per existing pattern.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 10: `propose_canonicalizations` CLI

**Files:**
- Create: `community-brain/src/community_brain/cli/__init__.py` (if absent — verify with `ls`)
- Create: `community-brain/src/community_brain/cli/propose_canonicalizations.py`
- Test: `community-brain/tests/test_propose_canonicalizations.py`

- [ ] **Step 1: Ensure cli package exists**

```bash
ls community-brain/src/community_brain/cli/__init__.py 2>/dev/null || touch community-brain/src/community_brain/cli/__init__.py
```

- [ ] **Step 2: Write the failing test**

Create `community-brain/tests/test_propose_canonicalizations.py`:

```python
"""Tests for the propose_canonicalizations CLI."""
from __future__ import annotations

from community_brain.cli.propose_canonicalizations import (
    generate_proposals,
)


def test_high_confidence_case_insensitive_exact_match():
    """'asako' (pending) → 'Asako Hayase' (canonical) when prefix or first-name match exists."""
    registry = {
        "aliases": {"Asako Hayase": []},
        "pending": ["asako"],
    }
    proposals = generate_proposals(registry)
    assert any(
        p["canonical"] == "Asako Hayase"
        and "asako" in p["candidate_aliases"]
        and p["confidence"] == "high"
        for p in proposals["proposals"]
    )


def test_medium_confidence_token_containment():
    """'Adam' (pending) + 'Adam - Gold Flamingo' (pending) propose merge into 'Adam James' canonical."""
    registry = {
        "aliases": {"Adam James": []},
        "pending": ["Adam", "Adam - Gold Flamingo"],
    }
    proposals = generate_proposals(registry)
    matching = [p for p in proposals["proposals"] if p["canonical"] == "Adam James"]
    assert len(matching) == 1
    aliases = set(matching[0]["candidate_aliases"])
    assert "Adam" in aliases
    assert "Adam - Gold Flamingo" in aliases
    assert matching[0]["confidence"] == "medium"


def test_ambiguous_first_name_no_proposal():
    """'Tony' with no canonical 'Tony X' candidate → goes to ambiguous, not proposals."""
    registry = {
        "aliases": {"Tom Welsh": [], "Brandon Hancock": []},
        "pending": ["Tony"],
    }
    proposals = generate_proposals(registry)
    assert any(a["name"] == "Tony" for a in proposals["ambiguous"])
    assert not any(
        "Tony" in p["candidate_aliases"] for p in proposals["proposals"]
    )


def test_ambiguous_zoom_display_name():
    """'David's iPhone' has no plausible canonical → ambiguous."""
    registry = {
        "aliases": {"David Sanders": []},
        "pending": ["David's iPhone"],
    }
    proposals = generate_proposals(registry)
    assert any(a["name"] == "David's iPhone" for a in proposals["ambiguous"])


def test_idempotent_run():
    """Running generate_proposals twice on the same input produces the same output."""
    registry = {
        "aliases": {"Adam James": []},
        "pending": ["Adam"],
    }
    p1 = generate_proposals(registry)
    p2 = generate_proposals(registry)
    assert p1["proposals"] == p2["proposals"]
    assert p1["ambiguous"] == p2["ambiguous"]


def test_already_canonical_pending_drops_to_proposal_self_match():
    """If 'Adam James' appears in pending AND is already canonical, surface
    it as ambiguous (operator should remove it from pending manually)."""
    registry = {
        "aliases": {"Adam James": []},
        "pending": ["Adam James"],
    }
    proposals = generate_proposals(registry)
    # Either ambiguous OR a self-match proposal — implementation choice.
    # Test for at least one of the two outcomes.
    surfaces_in_ambiguous = any(a["name"] == "Adam James" for a in proposals["ambiguous"])
    surfaces_in_proposals = any(
        p["canonical"] == "Adam James"
        and "Adam James" in p["candidate_aliases"]
        for p in proposals["proposals"]
    )
    assert surfaces_in_ambiguous or surfaces_in_proposals
```

- [ ] **Step 3: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_propose_canonicalizations.py -v
```

Expected: import errors.

- [ ] **Step 4: Implement the CLI**

Create `community-brain/src/community_brain/cli/propose_canonicalizations.py`:

```python
"""propose_canonicalizations CLI — heuristic merge proposals from the
pending queue against existing canonicals.

Spec §7.1.

Usage:
    python -m community_brain.cli.propose_canonicalizations \\
        [--registry community-brain/config/speaker-aliases.yaml] \\
        [--out community-brain/canonicalization-proposals.yaml]

Read-only on the registry; write-only to the proposals file.
"""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
from typing import Any

import yaml


def _exact_case_insensitive(pending: str, canonicals: list[str]) -> str | None:
    pl = pending.lower()
    for c in canonicals:
        if c.lower() == pl:
            return c
    return None


def _first_name_single_match(pending: str, canonicals: list[str]) -> str | None:
    """Return canonical iff exactly one canonical has `pending` as first token (case-insensitive)."""
    pl = pending.lower().strip()
    if " " in pl:  # only fire on single-token pending entries
        return None
    matches = [c for c in canonicals if c.lower().split(" ", 1)[0] == pl]
    return matches[0] if len(matches) == 1 else None


def _token_containment_single(pending: str, canonicals: list[str]) -> str | None:
    """For multi-token pending like 'Adam - Gold Flamingo', find a canonical
    whose first token matches the first token of pending (and exactly one such
    canonical exists)."""
    head = pending.lower().split(" ", 1)[0].strip().rstrip(",")
    if not head:
        return None
    matches = [c for c in canonicals if c.lower().split(" ", 1)[0] == head]
    return matches[0] if len(matches) == 1 else None


def generate_proposals(registry: dict[str, Any]) -> dict[str, Any]:
    """Produce {generated_at, proposals: [...], ambiguous: [...]}.

    Each proposal: {canonical, candidate_aliases, confidence, reason}.
    Each ambiguous: {name, reason}.
    """
    aliases = registry.get("aliases") or {}
    pending = registry.get("pending") or []
    canonicals = list(aliases.keys())
    # Group pending by their proposed canonical (so 'Adam' + 'Adam - Gold Flamingo'
    # collapse into one proposal targeting 'Adam James').
    by_canonical: dict[str, dict[str, Any]] = {}
    ambiguous: list[dict[str, str]] = []

    for entry in pending:
        # Try heuristics in order of confidence.
        match = _exact_case_insensitive(entry, canonicals)
        confidence = "high"
        reason = "case-insensitive exact match"
        if match is None:
            match = _first_name_single_match(entry, canonicals)
            reason = "first-name token match, single canonical candidate"
        if match is None:
            match = _token_containment_single(entry, canonicals)
            confidence = "medium"
            reason = "token containment, single canonical candidate"
        if match is None:
            ambiguous.append({
                "name": entry,
                "reason": "no canonical candidate found via heuristics",
            })
            continue
        if match not in by_canonical:
            by_canonical[match] = {
                "canonical": match,
                "candidate_aliases": [],
                "confidence": confidence,
                "reason": reason,
            }
        if entry not in by_canonical[match]["candidate_aliases"]:
            by_canonical[match]["candidate_aliases"].append(entry)
        # Demote confidence to medium if any contributing entry was medium.
        if confidence == "medium":
            by_canonical[match]["confidence"] = "medium"

    proposals = sorted(by_canonical.values(), key=lambda p: p["canonical"])
    return {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "proposals": proposals,
        "ambiguous": sorted(ambiguous, key=lambda a: a["name"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="community-brain/config/speaker-aliases.yaml")
    parser.add_argument("--out", default="community-brain/canonicalization-proposals.yaml")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    out_path = Path(args.out)
    registry = yaml.safe_load(registry_path.read_text())
    proposals = generate_proposals(registry)
    out_path.write_text(yaml.safe_dump(proposals, sort_keys=False, allow_unicode=True))
    print(f"[ok] wrote {len(proposals['proposals'])} proposals + "
          f"{len(proposals['ambiguous'])} ambiguous to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_propose_canonicalizations.py -v
```

Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/cli/__init__.py community-brain/src/community_brain/cli/propose_canonicalizations.py community-brain/tests/test_propose_canonicalizations.py
git commit -m "$(cat <<'EOF'
feat(cli): add propose_canonicalizations heuristic CLI

Generates merge proposals from the speaker-aliases pending queue
using high (exact / first-name single-match) and medium (token
containment) heuristics. Surfaces ambiguous entries (Zoom display
names, ambiguous first names) without auto-proposal. Read-only
on the registry; emits proposals YAML for operator review.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 11: `recanonicalize` CLI standalone

**Files:**
- Create: `community-brain/src/community_brain/cli/recanonicalize.py`
- Test: `community-brain/tests/test_recanonicalize.py`

- [ ] **Step 1: Write the failing test**

Create `community-brain/tests/test_recanonicalize.py`:

```python
"""Tests for the recanonicalize CLI."""
from __future__ import annotations

from community_brain.cli.recanonicalize import recanonicalize_chunks


def test_recanonicalize_updates_changed_chunks(tmp_path):
    """When the registry has 'Adam' -> 'Adam James' but a chunk's
    speakers_spoke contains the raw 'Adam', recanonicalize updates it."""
    # Setup: create a small LanceDB at tmp_path with 1-2 chunks containing
    # raw 'Adam' in speakers_spoke. Call recanonicalize_chunks; verify the
    # row gets rewritten with 'Adam James' and embed_text / bm25_text are
    # re-synthesized.


def test_recanonicalize_noop_when_no_changes(tmp_path):
    """When all chunks already have canonical names, recanonicalize is a fast scan."""
    # Setup: chunks already have 'Adam James'. Call recanonicalize_chunks.
    # Verify return value reports 0 chunks changed.


def test_recanonicalize_idempotent(tmp_path):
    """Running recanonicalize twice produces the same result (no further changes
    on the second run)."""
    # Setup: chunks with 'Adam'. Run recanonicalize_chunks once → updates.
    # Run again → reports 0 further changes.
```

> **Note:** Use existing LanceDB-test fixture patterns from `test_ingestion_pipeline.py` for the `tmp_path` setup. Mock the embedding step so re-embed during recanonicalize doesn't hit Ollama in tests (use a deterministic stub returning a 768-vector of constant value, or whatever the existing test infra provides).

- [ ] **Step 2: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_recanonicalize.py -v
```

Expected: import errors.

- [ ] **Step 3: Implement the CLI**

Create `community-brain/src/community_brain/cli/recanonicalize.py`:

```python
"""recanonicalize CLI — rewrite chunks against the current registry.

For each row in the chunks table:
1. Apply the current speaker-aliases map to speakers_spoke,
   speakers_mentioned, and people-typed entries in entities.
2. If anything changed: re-synthesize embed_text + bm25_text;
   re-embed embed_text via Ollama; write the row back.
3. If nothing changed: fast scan, no write.

Decoupled from Stage C extraction (no LLM call). Ride-along for
the speaker-aliases lifecycle: future name additions don't trigger
re-extracts.

Spec §7.1.

Usage:
    python -m community_brain.cli.recanonicalize \\
        [--db /data/lancedb/nomic-v1] \\
        [--registry community-brain/config/speaker-aliases.yaml] \\
        [--dry-run]
"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any

import lancedb
import yaml

from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
from community_brain.ingestion.canonicalize import build_alias_map, canonicalize_names
from community_brain.ingestion.embedding import build_transcript_embed_text


logger = logging.getLogger(__name__)


def _is_transcript(row: dict) -> bool:
    return row.get("content_type") == "prepared_transcript"


def _row_needs_update(row: dict, alias_map: dict[str, str]) -> tuple[bool, dict]:
    """Returns (changed, updated_field_dict).

    Applies alias_map to speakers_spoke, speakers_mentioned, entities. If any
    of those lists differ from current row values, returns True with the
    updated values; otherwise False with empty dict.
    """
    new_spk, _ = canonicalize_names(row.get("speakers_spoke") or [], alias_map)
    new_men, _ = canonicalize_names(row.get("speakers_mentioned") or [], alias_map)
    new_ent, _ = canonicalize_names(row.get("entities") or [], alias_map)
    changed = (
        new_spk != (row.get("speakers_spoke") or [])
        or new_men != (row.get("speakers_mentioned") or [])
        or new_ent != (row.get("entities") or [])
    )
    if not changed:
        return False, {}
    return True, {
        "speakers_spoke": new_spk,
        "speakers_mentioned": new_men,
        "entities": new_ent,
    }


def recanonicalize_chunks(
    db_path: str | Path,
    registry: dict[str, Any],
    *,
    embed_fn,
    dry_run: bool = False,
) -> dict[str, int]:
    """Apply current registry to all chunks; return summary stats.

    embed_fn: callable(text: str) -> list[float]. Tests pass a stub.
    Production passes ollama-backed embed.
    """
    alias_map = build_alias_map(registry)
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = table.to_arrow().to_pylist()

    updated = 0
    scanned = 0
    for row in rows:
        scanned += 1
        changed, fields = _row_needs_update(row, alias_map)
        if not changed:
            continue
        # Re-synthesize embed_text (transcripts) and bm25_text.
        new_spk = fields["speakers_spoke"]
        new_men = fields["speakers_mentioned"]
        new_ent = fields["entities"]
        keywords = row.get("keywords") or []
        topic_label = row.get("topic_label")
        full_text = row.get("full_text", "")
        if _is_transcript(row):
            # embed_text uses summary; reconstruct from existing embed_text
            # by extracting the "summary: ..." line. Acceptable since v3
            # synthesis writes a known format.
            existing = row.get("embed_text", "")
            summary = existing.split("summary:", 1)[-1].strip() if "summary:" in existing else ""
            new_embed_text = build_transcript_embed_text(
                topic_label=topic_label,
                speakers_spoke=new_spk,
                speakers_mentioned=new_men,
                entities=new_ent,
                keywords=keywords,
                summary=summary,
            )
        else:
            # Signals and posts have embed_text == full_text; canonicalization
            # of name lists doesn't change full_text, so embed_text is stable.
            new_embed_text = row.get("embed_text", "")
        new_bm25_text = synthesize_bm25_text(
            topic_label=topic_label,
            entities=new_ent,
            speakers_spoke=new_spk,
            speakers_mentioned=new_men,
            keywords=keywords,
            full_text=full_text,
        )
        # Re-embed if embed_text changed.
        if new_embed_text != row.get("embed_text", ""):
            new_embedding = embed_fn(new_embed_text)
        else:
            new_embedding = row.get("embedding")
        if dry_run:
            updated += 1
            continue
        table.update(
            where=f"chunk_id = '{row['chunk_id']}'",
            values={
                "speakers_spoke": new_spk,
                "speakers_mentioned": new_men,
                "entities": new_ent,
                "embed_text": new_embed_text,
                "bm25_text": new_bm25_text,
                "embedding": new_embedding,
            },
        )
        updated += 1

    return {"scanned": scanned, "updated": updated}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="/data/lancedb/nomic-v1")
    parser.add_argument("--registry", default="community-brain/config/speaker-aliases.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    registry = yaml.safe_load(Path(args.registry).read_text())
    # Production: real embed via ollama.
    from community_brain.ingestion import embedding as embedding_module
    stats = recanonicalize_chunks(
        args.db,
        registry,
        embed_fn=embedding_module.embed,
        dry_run=args.dry_run,
    )
    print(f"[ok] scanned {stats['scanned']}, updated {stats['updated']} "
          f"(dry_run={args.dry_run})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

> **Note:** The exact LanceDB update API in 0.30.2 (`table.update(where=..., values=...)`) needs verification during implementation. If the exact form differs, adapt — the contract is "rewrite this row's listed fields without re-creating the row." Check `lancedb` 0.30.2 docs or source if uncertain.

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_recanonicalize.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/cli/recanonicalize.py community-brain/tests/test_recanonicalize.py
git commit -m "$(cat <<'EOF'
feat(cli): add recanonicalize CLI

Standalone chunk-rewrite pass that applies the current speaker
registry to speakers_spoke / speakers_mentioned / entities,
re-synthesizes embed_text + bm25_text, and re-embeds if needed.
No Stage C call — decoupled from extraction so future name
additions don't trigger re-extracts.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 12: `apply_canonicalizations` CLI with auto-trigger

**Files:**
- Create: `community-brain/src/community_brain/cli/apply_canonicalizations.py`
- Test: `community-brain/tests/test_apply_canonicalizations.py`

- [ ] **Step 1: Write the failing test**

Create `community-brain/tests/test_apply_canonicalizations.py`:

```python
"""Tests for apply_canonicalizations CLI."""
from __future__ import annotations

from pathlib import Path

import yaml

from community_brain.cli.apply_canonicalizations import apply_proposals_to_registry


def test_apply_merges_accepted_proposals_into_aliases(tmp_path):
    """An accepted proposal becomes a new aliases entry; pending entries removed."""
    registry = {
        "version": "2026-04-29",
        "aliases": {"Existing Person": ["existing"]},
        "pending": ["Adam", "Adam - Gold Flamingo", "Tony"],
    }
    proposals = {
        "proposals": [
            {
                "canonical": "Adam James",
                "candidate_aliases": ["Adam", "Adam - Gold Flamingo"],
                "confidence": "medium",
                "reason": "token containment",
            },
        ],
        "ambiguous": [{"name": "Tony", "reason": "ambiguous first name"}],
    }
    updated = apply_proposals_to_registry(registry, proposals)
    assert "Adam James" in updated["aliases"]
    assert "Adam" in updated["aliases"]["Adam James"]
    assert "Adam - Gold Flamingo" in updated["aliases"]["Adam James"]
    assert "Existing Person" in updated["aliases"]
    assert "Adam" not in updated["pending"]
    assert "Adam - Gold Flamingo" not in updated["pending"]
    # Tony stays in pending — operator decides later.
    assert "Tony" in updated["pending"]


def test_apply_preserves_existing_aliases_for_canonical(tmp_path):
    """If 'Adam James' already exists with prior aliases, append new ones."""
    registry = {
        "aliases": {"Adam James": ["AdamJ"]},
        "pending": ["Adam"],
    }
    proposals = {
        "proposals": [
            {
                "canonical": "Adam James",
                "candidate_aliases": ["Adam"],
                "confidence": "high",
                "reason": "test",
            },
        ],
        "ambiguous": [],
    }
    updated = apply_proposals_to_registry(registry, proposals)
    assert "AdamJ" in updated["aliases"]["Adam James"]
    assert "Adam" in updated["aliases"]["Adam James"]


def test_apply_idempotent(tmp_path):
    """Applying the same proposals twice produces the same registry."""
    registry = {"aliases": {"Adam James": []}, "pending": ["Adam"]}
    proposals = {
        "proposals": [
            {"canonical": "Adam James", "candidate_aliases": ["Adam"],
             "confidence": "high", "reason": "test"},
        ],
        "ambiguous": [],
    }
    once = apply_proposals_to_registry(registry, proposals)
    twice = apply_proposals_to_registry(once, proposals)
    assert once == twice
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_apply_canonicalizations.py -v
```

Expected: import errors.

- [ ] **Step 3: Implement the CLI**

Create `community-brain/src/community_brain/cli/apply_canonicalizations.py`:

```python
"""apply_canonicalizations CLI — merge proposals into the registry.

Auto-triggers recanonicalize at the end unless --no-recanonicalize.

Usage:
    python -m community_brain.cli.apply_canonicalizations <proposals.yaml> \\
        [--registry community-brain/config/speaker-aliases.yaml] \\
        [--no-recanonicalize]

Spec §7.1.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


def apply_proposals_to_registry(
    registry: dict[str, Any],
    proposals: dict[str, Any],
) -> dict[str, Any]:
    """Merge accepted proposals into a copy of the registry.

    For each proposal: ensure canonical exists in aliases; append the
    candidate_aliases (deduped); remove them from pending.

    Ambiguous proposals are not applied (they stay in pending for operator
    review).
    """
    out = {
        "version": registry.get("version", ""),
        "aliases": {k: list(v or []) for k, v in (registry.get("aliases") or {}).items()},
        "pending": list(registry.get("pending") or []),
    }
    for prop in proposals.get("proposals") or []:
        canonical = prop["canonical"]
        candidates = prop.get("candidate_aliases") or []
        existing = set(out["aliases"].get(canonical, []))
        for c in candidates:
            existing.add(c)
            if c in out["pending"]:
                out["pending"].remove(c)
        out["aliases"][canonical] = sorted(existing)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("proposals_path")
    parser.add_argument("--registry", default="community-brain/config/speaker-aliases.yaml")
    parser.add_argument("--no-recanonicalize", action="store_true")
    parser.add_argument("--db", default="/data/lancedb/nomic-v1")
    args = parser.parse_args()

    proposals = yaml.safe_load(Path(args.proposals_path).read_text())
    registry_path = Path(args.registry)
    registry = yaml.safe_load(registry_path.read_text())
    updated = apply_proposals_to_registry(registry, proposals)
    registry_path.write_text(yaml.safe_dump(updated, sort_keys=False, allow_unicode=True))
    print(f"[ok] applied {len(proposals.get('proposals') or [])} proposals to {registry_path}")

    if args.no_recanonicalize:
        print("[ok] --no-recanonicalize set; skipping chunk rewrite")
        return 0

    # Auto-trigger recanonicalize.
    from community_brain.cli.recanonicalize import recanonicalize_chunks
    from community_brain.ingestion import embedding as embedding_module

    stats = recanonicalize_chunks(
        args.db,
        updated,
        embed_fn=embedding_module.embed,
        dry_run=False,
    )
    print(f"[ok] recanonicalize: scanned {stats['scanned']}, updated {stats['updated']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_apply_canonicalizations.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/cli/apply_canonicalizations.py community-brain/tests/test_apply_canonicalizations.py
git commit -m "$(cat <<'EOF'
feat(cli): add apply_canonicalizations with recanonicalize auto-trigger

Merges accepted proposals into speaker-aliases.yaml; auto-triggers
recanonicalize at the end. --no-recanonicalize escape hatch
preserves dry-run / staged operation.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 4 — Cue rules in YAML

### Task 13: Add YAML cue rules loader

**Files:**
- Modify: `community-brain/src/community_brain/query/cue_rules.py`
- Create: `community-brain/config/query-cues.yaml`
- Modify: `community-brain/tests/test_cue_rules.py`

- [ ] **Step 1: Create the YAML file**

Create `community-brain/config/query-cues.yaml`:

```yaml
cue_rules:
  - name: unresolved_questions
    cue_phrases:
      - unresolved
      - open question
      - not answered
      - outstanding
      - didn't get answered
      - didn't get fully answered
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010

  - name: decisions
    cue_phrases:
      - decision
      - decided
      - resolved
      - concluded
    target_predicate:
      field: decisions
      check: non_empty
    delta: 0.008

  - name: action_items
    cue_phrases:
      - action item
      - commit
      - commitment
      - next step
      - to-do
      - todo
      - homework
    target_predicate:
      field: action_items
      check: non_empty
    delta: 0.008

  - name: insights
    cue_phrases:
      - insight
      - realization
      - aha moment
      - key takeaway
    target_predicate:
      field: has_insight
      value: true
    delta: 0.006

  - name: referenced_prior
    cue_phrases:
      - referenced
      - prior call
      - last week
      - previously
      - discussed before
    target_predicate:
      field: references_prior
      value: true
    delta: 0.006

  - name: questions_general
    cue_phrases:
      - question
      - asked
    target_predicate:
      field: has_question
      value: true
    delta: 0.003
```

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_cue_rules.py`:

```python
def test_load_cue_rules_from_yaml(tmp_path):
    """The YAML loader produces CueRule instances with predicates that match
    the same shape as the legacy hardcoded set."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml

    yaml_text = """
cue_rules:
  - name: test_unresolved
    cue_phrases: [unresolved]
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
  - name: test_decisions
    cue_phrases: [decision]
    target_predicate:
      field: decisions
      check: non_empty
    delta: 0.008
"""
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 2

    # boolean rule
    bool_rule = rules[0]
    assert bool_rule.name == "test_unresolved"
    assert bool_rule.target_predicate({"has_unresolved_question": True}) is True
    assert bool_rule.target_predicate({"has_unresolved_question": False}) is False

    # non_empty rule
    list_rule = rules[1]
    assert list_rule.target_predicate({"decisions": ["X"]}) is True
    assert list_rule.target_predicate({"decisions": []}) is False
    assert list_rule.target_predicate({"decisions": None}) is False


def test_load_cue_rules_missing_file_returns_empty(tmp_path):
    """Missing YAML file: loader returns empty tuple, logs WARN."""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    rules = load_cue_rules_from_yaml(tmp_path / "missing.yaml")
    assert rules == ()


def test_load_cue_rules_malformed_skips_bad_rule(tmp_path):
    """A rule missing required keys is skipped; well-formed rules still load."""
    yaml_text = """
cue_rules:
  - name: bad
    cue_phrases: []
    target_predicate:
      field: missing_value_or_check
    delta: 0.01
  - name: good
    cue_phrases: [x]
    target_predicate:
      field: has_question
      value: true
    delta: 0.003
"""
    from community_brain.query.cue_rules import load_cue_rules_from_yaml
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    assert len(rules) == 1
    assert rules[0].name == "good"


def test_existing_apply_cue_boosts_works_with_yaml_loaded_rules(tmp_path):
    """Smoke test: the existing apply_cue_boosts function works with YAML-loaded rules."""
    from community_brain.query.cue_rules import (
        apply_cue_boosts, load_cue_rules_from_yaml,
    )
    yaml_text = """
cue_rules:
  - name: r
    cue_phrases: [unresolved]
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010
"""
    path = tmp_path / "cues.yaml"
    path.write_text(yaml_text)
    rules = load_cue_rules_from_yaml(path)
    candidates = [
        {"chunk_id": "a", "_rrf_score": 0.01, "has_unresolved_question": True},
        {"chunk_id": "b", "_rrf_score": 0.02, "has_unresolved_question": False},
    ]
    boosted = apply_cue_boosts("unresolved questions", candidates, rules=rules)
    # Chunk "a" boosted by 0.01 to 0.02; "b" unchanged at 0.02; tie ordering
    # is implementation-defined but both should appear.
    by_id = {c["chunk_id"]: c["_rrf_score"] for c in boosted}
    assert by_id["a"] == pytest.approx(0.020)
    assert by_id["b"] == pytest.approx(0.020)
```

Add `import pytest` at the top if not already present.

- [ ] **Step 3: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_cue_rules.py -v -k "yaml"
```

Expected: import error on `load_cue_rules_from_yaml`.

- [ ] **Step 4: Implement the YAML loader**

Append to `community-brain/src/community_brain/query/cue_rules.py`:

```python
import logging
from pathlib import Path
from typing import Any

import yaml

# (logger defined above)


def _build_predicate(spec: dict[str, Any]):
    """Translate a YAML target_predicate dict to a callable predicate.

    Supported shapes:
      - {field: NAME, value: BOOL_OR_VAL} → chunk[NAME] == value
      - {field: NAME, check: non_empty}   → chunk[NAME] is non-empty list/string
      - {field: NAME, check: contains, value: STR} → STR in chunk[NAME] (list or string)
    """
    field = spec.get("field")
    if not field:
        raise ValueError("target_predicate missing 'field'")
    if "value" in spec and "check" not in spec:
        expected = spec["value"]
        return lambda chunk, _f=field, _v=expected: chunk.get(_f) == _v
    check = spec.get("check")
    if check == "non_empty":
        def pred(chunk, _f=field):
            v = chunk.get(_f)
            return isinstance(v, (list, str)) and len(v) > 0
        return pred
    if check == "contains":
        needle = spec.get("value")
        if needle is None:
            raise ValueError("check: contains requires 'value'")
        def pred(chunk, _f=field, _n=needle):
            v = chunk.get(_f)
            if isinstance(v, list):
                return _n in v
            if isinstance(v, str):
                return _n in v
            return False
        return pred
    raise ValueError(f"unsupported target_predicate spec: {spec}")


def load_cue_rules_from_yaml(path: str | Path) -> tuple[CueRule, ...]:
    """Load cue rules from YAML.

    Returns empty tuple on missing file. Logs WARN.
    Skips individual malformed rules with ERROR; continues with the rest.
    """
    p = Path(path)
    if not p.exists():
        logger.warning("cue rules YAML not found: %s; using empty rule set", p)
        return ()
    try:
        data = yaml.safe_load(p.read_text())
    except Exception as exc:
        logger.error("failed to parse cue rules YAML at %s: %s", p, exc)
        return ()
    if not isinstance(data, dict) or "cue_rules" not in data:
        logger.error("cue rules YAML at %s missing top-level 'cue_rules' key", p)
        return ()
    rules: list[CueRule] = []
    for entry in data.get("cue_rules") or []:
        try:
            name = entry["name"]
            cue_phrases = tuple(entry["cue_phrases"])
            if len(cue_phrases) == 0:
                raise ValueError("cue_phrases is empty")
            predicate = _build_predicate(entry["target_predicate"])
            delta = float(entry["delta"])
            if delta < 0:
                raise ValueError("delta must be non-negative")
            rules.append(CueRule(
                name=name,
                cue_phrases=cue_phrases,
                target_predicate=predicate,
                delta=delta,
            ))
        except Exception as exc:
            logger.error(
                "skipping malformed cue rule %r: %s",
                entry.get("name", "<unnamed>"),
                exc,
            )
    return tuple(rules)
```

- [ ] **Step 5: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_cue_rules.py -v
```

Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/query/cue_rules.py community-brain/config/query-cues.yaml community-brain/tests/test_cue_rules.py
git commit -m "$(cat <<'EOF'
feat(retrieval): load cue rules from YAML

Adds load_cue_rules_from_yaml with declarative predicate types
(field/value, field/check non_empty, field/check contains).
config/query-cues.yaml holds the v3 rule set; CueRule + apply_cue_boosts
unchanged. Hot reload supported on each /query call.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 14: Wire `query_local.py` to load cue rules from YAML at call time

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py`
- Test: `community-brain/tests/test_query_local.py`

- [ ] **Step 1: Find current rule consumption site**

```bash
grep -n "CUE_RULES\|apply_cue_boosts" community-brain/src/community_brain/query/query_local.py
```

Identify where `apply_cue_boosts` is called and what rules it's passed.

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_query_local.py`:

```python
def test_search_chunks_uses_yaml_cue_rules(monkeypatch, tmp_path):
    """search_chunks should load cue rules from query-cues.yaml on each call."""
    yaml_path = tmp_path / "query-cues.yaml"
    yaml_path.write_text("""
cue_rules:
  - name: r
    cue_phrases: [unresolved]
    target_predicate: {field: has_unresolved_question, value: true}
    delta: 0.010
""")
    monkeypatch.setenv("COMMUNITY_BRAIN_CUE_RULES_PATH", str(yaml_path))
    # Mock the rest of search_chunks to verify the YAML load path runs.
    # Assertion: a chunk tagged has_unresolved_question gets boosted by 0.010
    # when question contains "unresolved".
```

- [ ] **Step 3: Wire the loader**

In `community-brain/src/community_brain/query/query_local.py`:

Replace the `apply_cue_boosts(question, candidates)` call with:

```python
import os
from community_brain.query.cue_rules import load_cue_rules_from_yaml

CUE_RULES_PATH_DEFAULT = "/app/config/query-cues.yaml"
# ...

# In search_chunks (or wherever apply_cue_boosts is called):
cue_path = os.environ.get("COMMUNITY_BRAIN_CUE_RULES_PATH") or CUE_RULES_PATH_DEFAULT
rules = load_cue_rules_from_yaml(cue_path)
boosted = apply_cue_boosts(question, candidates, rules=rules)
```

- [ ] **Step 4: Run the test**

```bash
./.venv/bin/pytest tests/test_query_local.py -v -k "yaml"
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/query_local.py community-brain/tests/test_query_local.py
git commit -m "$(cat <<'EOF'
refactor(retrieval): load cue rules from YAML at /query call time

search_chunks now reads config/query-cues.yaml on each /query call
(sub-millisecond cost). Hot-reload: rule changes take effect without
container restart. Path overridable via COMMUNITY_BRAIN_CUE_RULES_PATH.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 5 — Retrieval response shape (score_breakdown + metadata_summary)

### Task 15: Record per-chunk score breakdown in `search_chunks`

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py`
- Test: `community-brain/tests/test_search_hybrid.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_search_hybrid.py`:

```python
def test_search_chunks_records_score_breakdown(...):
    """Every chunk in the search_chunks return value has a score_breakdown
    dict with keys: vector_similarity, bm25_rank, rrf_score, cue_delta,
    cue_rules_fired."""
    # Use the existing hybrid-search test harness pattern (committed
    # synthetic corpus, real LanceDB at tmp_path). Run search_chunks against
    # a question that fires at least one cue rule. Assert:
    #   for chunk in result_chunks:
    #       assert "score_breakdown" in chunk
    #       sb = chunk["score_breakdown"]
    #       assert {"vector_similarity", "bm25_rank", "rrf_score",
    #               "cue_delta", "cue_rules_fired"} == set(sb.keys())
```

> **Note:** Read existing hybrid-search tests for the test corpus + harness pattern.

- [ ] **Step 2: Run the test to verify it fails**

```bash
./.venv/bin/pytest tests/test_search_hybrid.py -v -k "score_breakdown"
```

Expected: FAIL — chunks lack `score_breakdown` field.

- [ ] **Step 3: Update `search_chunks` to populate score_breakdown**

In `community-brain/src/community_brain/query/query_local.py`, in `search_chunks` (post-RRF, post-cue-boost, before truncation to top_k):

```python
# Annotate each surviving candidate with score_breakdown.
# Already-known per candidate from the hybrid + cue path:
#   - chunk["_rrf_score"] = pre-cue RRF score
#   - chunk["_vector_similarity"] = vector cosine (computed earlier)
#   - chunk["_bm25_rank"] = BM25 rank or None
#   - chunk["_cue_delta"] = total Δ applied
#   - chunk["_cue_rules_fired"] = list of rule names that fired
# These underscored fields need to be tracked through the pipeline; if not
# already present, add them.

for chunk in boosted:
    chunk["score_breakdown"] = {
        "vector_similarity": chunk.get("_vector_similarity", 0.0),
        "bm25_rank": chunk.get("_bm25_rank"),
        "rrf_score": chunk.get("_rrf_score", 0.0) - chunk.get("_cue_delta", 0.0),
        "cue_delta": chunk.get("_cue_delta", 0.0),
        "cue_rules_fired": chunk.get("_cue_rules_fired", []),
    }
```

You may need to update `apply_cue_boosts` to return cue_rules_fired info per chunk. If so, add this minor enhancement to `cue_rules.py`:

```python
# In apply_cue_boosts, instead of:
#   chunk["_rrf_score"] = chunk.get("_rrf_score", 0.0) + rule.delta
# do:
chunk["_rrf_score"] = chunk.get("_rrf_score", 0.0) + rule.delta
chunk["_cue_delta"] = chunk.get("_cue_delta", 0.0) + rule.delta
chunk.setdefault("_cue_rules_fired", []).append(rule.name)
```

Same for `_vector_similarity` and `_bm25_rank` — these need to be tracked from earlier in the search pipeline. Trace where vector and BM25 results are merged; record per-candidate origin info.

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_search_hybrid.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/query_local.py community-brain/src/community_brain/query/cue_rules.py community-brain/tests/test_search_hybrid.py
git commit -m "$(cat <<'EOF'
feat(retrieval): annotate chunks with score_breakdown

search_chunks now records per-chunk vector_similarity, bm25_rank,
rrf_score, cue_delta, cue_rules_fired. Surfaced in /query response
in Task 17 for explainability.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 16: Compute `metadata_summary` over top-K

**Files:**
- Modify: `community-brain/src/community_brain/query/query_local.py`
- Test: `community-brain/tests/test_search_hybrid.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_search_hybrid.py`:

```python
def test_search_chunks_returns_metadata_summary(...):
    """search_chunks return shape includes metadata_summary with of_top_k +
    per-flag counts."""
    # Set up a small corpus where some chunks have has_unresolved_question=True.
    # Run search_chunks with top_k=N. Assert:
    #   result.metadata_summary["of_top_k"] == N (or actual returned count)
    #   result.metadata_summary["has_unresolved_question_count"] == correct count
    #   etc.
```

- [ ] **Step 2: Run the test to verify it fails**

Expected: FAIL — return shape doesn't have `metadata_summary`.

- [ ] **Step 3: Update `search_chunks` return shape**

In `community-brain/src/community_brain/query/query_local.py`, after truncating to top_k:

```python
def _compute_metadata_summary(top_k_chunks: list[dict]) -> dict:
    flag_fields = (
        "has_question", "has_answer", "has_unresolved_question",
        "has_insight", "references_prior",
    )
    summary = {"of_top_k": len(top_k_chunks)}
    for f in flag_fields:
        count = sum(1 for c in top_k_chunks if c.get(f) is True)
        summary[f"{f}_count"] = count
    return summary

# Adjust search_chunks return value to include metadata_summary.
# Existing return shape: list[dict] of chunks. Change to a dict with
# {"chunks": [...], "metadata_summary": {...}} OR add as a sibling depending
# on existing call-site contract. Trace callers; the retrieval_server calls
# search_chunks and constructs the QueryResponseV2. The smallest invasive
# change: search_chunks returns a dict; retrieval_server reads both keys.
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_search_hybrid.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/query_local.py community-brain/tests/test_search_hybrid.py
git commit -m "$(cat <<'EOF'
feat(retrieval): compute metadata_summary over top-K

search_chunks now computes corpus-level aggregates (of_top_k +
per-flag counts) for the answering LLM. Will be exposed as
top-level field on /query response in Task 17.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 17: Surface `score_breakdown` and `metadata_summary` in `/query` response

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Test: `community-brain/tests/test_retrieval_server_query_v2.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_retrieval_server_query_v2.py`:

```python
def test_query_response_includes_metadata_summary(test_client_with_corpus):
    """/query response top-level shape includes metadata_summary with of_top_k
    and per-flag counts."""
    resp = test_client_with_corpus.post("/query", json={"question": "test", "top_k": 5})
    body = resp.json()
    assert "metadata_summary" in body
    assert "of_top_k" in body["metadata_summary"]
    for f in ("has_question_count", "has_answer_count",
              "has_unresolved_question_count", "has_insight_count",
              "references_prior_count"):
        assert f in body["metadata_summary"]


def test_query_response_chunks_include_score_breakdown(test_client_with_corpus):
    resp = test_client_with_corpus.post("/query", json={"question": "test", "top_k": 5})
    body = resp.json()
    for chunk in body["chunks"]:
        assert "score_breakdown" in chunk
        sb = chunk["score_breakdown"]
        for k in ("vector_similarity", "bm25_rank", "rrf_score",
                  "cue_delta", "cue_rules_fired"):
            assert k in sb
```

> **Note:** Use the existing `test_client_with_corpus` (or equivalent) fixture pattern in `test_retrieval_server_query_v2.py`.

- [ ] **Step 2: Run the test to verify it fails**

```bash
./.venv/bin/pytest tests/test_retrieval_server_query_v2.py -v -k "metadata_summary or score_breakdown"
```

Expected: FAIL.

- [ ] **Step 3: Update Pydantic models + handler**

In `community-brain/src/community_brain/query/retrieval_server.py`:

```python
from pydantic import BaseModel, Field


class ScoreBreakdown(BaseModel):
    vector_similarity: float
    bm25_rank: int | None
    rrf_score: float
    cue_delta: float
    cue_rules_fired: list[str]


class QueryChunkResult(BaseModel):
    # ... existing fields ground_truth, derived_metadata, provenance, similarity ...
    score_breakdown: ScoreBreakdown


class QueryResponseV2(BaseModel):
    query: str
    chunks: list[QueryChunkResult]
    total_matched: int
    filters_applied: dict
    metadata_summary: dict


# In the /query handler:
# Read both "chunks" and "metadata_summary" from search_chunks return value;
# attach score_breakdown to each QueryChunkResult.
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_retrieval_server_query_v2.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py community-brain/tests/test_retrieval_server_query_v2.py
git commit -m "$(cat <<'EOF'
feat(retrieval): expose score_breakdown + metadata_summary in /query

QueryChunkResult adds score_breakdown sub-model.
QueryResponseV2 adds metadata_summary top-level field.
Existing fields and clients unaffected (additive only).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 18: Migrate FTS index from `full_text` to `bm25_text`

**Files:**
- Modify: `community-brain/src/community_brain/query/fts_lifecycle.py`
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Modify: `community-brain/src/community_brain/query/query_local.py`
- Test: `community-brain/tests/test_fts_lifecycle.py`

- [ ] **Step 1: Update fts_lifecycle to accept column parameter**

In `community-brain/src/community_brain/query/fts_lifecycle.py`:

```python
def ensure_fts_index(table, column: str = "bm25_text") -> None:
    """Create the FTS index on `column` if not present. Idempotent."""
    # Existing logic, parameterized on column name.
    # Implementation depends on existing fts_lifecycle.py — adapt the body.

def optimize_fts_index(table, column: str = "bm25_text") -> None:
    """No-op stub (LanceDB auto-includes new rows; v2 spike confirmed)."""
    return
```

- [ ] **Step 2: Update startup hook**

In `community-brain/src/community_brain/query/retrieval_server.py` startup hook:

```python
# Replace:
ensure_fts_index(table)  # was full_text default
# With:
ensure_fts_index(table, column="bm25_text")

# Best-effort cleanup of legacy full_text index (idempotent; ignored if absent):
try:
    table.drop_index("full_text_idx")  # exact name varies; verify in 0.30.2
except Exception as exc:
    logger.debug("legacy full_text FTS index not present (or drop API differs): %s", exc)
```

> **Note:** The exact LanceDB drop-index API in 0.30.2 needs verification. If `drop_index` doesn't exist, leave the legacy index in place (unused, harmless).

- [ ] **Step 3: Update query path**

In `community-brain/src/community_brain/query/query_local.py`, in the hybrid-query construction:

```python
# Replace any reference to the FTS query targeting full_text:
table.search(query_type="hybrid").vector(vec).text(question)
# with the column-aware form (LanceDB auto-uses the FTS index column):
# (No code change needed if LanceDB infers from the index location;
# verify during implementation.)
```

- [ ] **Step 4: Run all FTS tests**

```bash
./.venv/bin/pytest tests/test_fts_lifecycle.py tests/test_search_hybrid.py -v
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/fts_lifecycle.py community-brain/src/community_brain/query/retrieval_server.py community-brain/src/community_brain/query/query_local.py community-brain/tests/test_fts_lifecycle.py
git commit -m "$(cat <<'EOF'
feat(retrieval): migrate FTS index to bm25_text column

ensure_fts_index now defaults to column=bm25_text. Server startup
attempts a best-effort drop of the legacy full_text index. Search
path queries the new index. Per v2 spike findings, FTS auto-updates
on row writes; no per-ingest optimize call needed.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 6 — Filter rendering ([flags: ...] + [corpus summary: ...])

### Task 19: Render `[flags: ...]` per chunk in the filter

**Files:**
- Modify: `community-brain/src/community_brain/openwebui/community_brain_filter.py`
- Test: `community-brain/tests/test_filter.py`

- [ ] **Step 1: Locate the chunk-rendering function in the filter**

```bash
grep -n "def.*[Cc]hunks\|render\|format" community-brain/src/community_brain/openwebui/community_brain_filter.py | head
```

Identify the function that turns retrieved chunks into the LLM-facing prompt context.

- [ ] **Step 2: Write the failing test**

Append to `community-brain/tests/test_filter.py`:

```python
def test_chunk_renders_flags_tag_when_flags_true():
    from community_brain.openwebui.community_brain_filter import render_chunk

    chunk = {
        "ground_truth": {"chunk_id": "test:001", "full_text": "Some content."},
        "derived_metadata": {
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": True,
            "has_insight": True,
            "references_prior": False,
        },
        "provenance": {},
        "similarity": 0.5,
    }
    rendered = render_chunk(chunk)
    assert "[flags: unresolved_question, insight]" in rendered or \
           "[flags: insight, unresolved_question]" in rendered
    assert "Some content." in rendered


def test_chunk_renders_no_flags_tag_when_all_flags_false():
    from community_brain.openwebui.community_brain_filter import render_chunk

    chunk = {
        "ground_truth": {"chunk_id": "test:001", "full_text": "Plain text."},
        "derived_metadata": {
            "has_question": False, "has_answer": False,
            "has_unresolved_question": False, "has_insight": False,
            "references_prior": False,
        },
        "provenance": {},
        "similarity": 0.5,
    }
    rendered = render_chunk(chunk)
    assert "[flags:" not in rendered
    assert "Plain text." in rendered


def test_chunk_renders_references_prior_in_flags():
    from community_brain.openwebui.community_brain_filter import render_chunk
    chunk = {
        "ground_truth": {"chunk_id": "test:001", "full_text": "Discussed last week."},
        "derived_metadata": {
            "has_question": False, "has_answer": False,
            "has_unresolved_question": False, "has_insight": False,
            "references_prior": True,
        },
        "provenance": {},
        "similarity": 0.5,
    }
    rendered = render_chunk(chunk)
    assert "[flags: references_prior]" in rendered
```

- [ ] **Step 3: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_filter.py -v -k "flags"
```

Expected: FAIL — `render_chunk` doesn't exist or doesn't render flags.

- [ ] **Step 4: Add the renderer**

In `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

```python
def _flag_tags_for_chunk(derived_metadata: dict) -> str:
    """Return '[flags: name1, name2]' or empty string if no flags True."""
    flag_to_label = {
        "has_question": "question",
        "has_answer": "answer",
        "has_unresolved_question": "unresolved_question",
        "has_insight": "insight",
        "references_prior": "references_prior",
    }
    true_flags = [label for field, label in flag_to_label.items()
                  if derived_metadata.get(field) is True]
    if not true_flags:
        return ""
    return f"[flags: {', '.join(true_flags)}]"


def render_chunk(chunk: dict) -> str:
    """Render a single chunk for the LLM-facing context."""
    derived = chunk.get("derived_metadata") or {}
    full_text = (chunk.get("ground_truth") or {}).get("full_text", "")
    parts = []
    flag_tag = _flag_tags_for_chunk(derived)
    if flag_tag:
        parts.append(flag_tag)
    parts.append(full_text)
    return "\n".join(parts)
```

Wire `render_chunk` into the filter's chunk-assembly code path. The exact integration depends on existing structure — read the filter file's existing prompt-assembly function and replace per-chunk text construction with `render_chunk(chunk)`.

- [ ] **Step 5: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_filter.py -v -k "flags"
```

Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/openwebui/community_brain_filter.py community-brain/tests/test_filter.py
git commit -m "$(cat <<'EOF'
feat(openwebui): render [flags: ...] tag per chunk in LLM context

Filter prepends per-chunk inline tag listing all True boolean
derived flags (has_question, has_answer, has_unresolved_question,
has_insight, references_prior). Empty when all false. Uniform
treatment per Q8.2 decision B. Path (b) of F8 narrow fix.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 20: Render `[corpus summary: ...]` at top of LLM context

**Files:**
- Modify: `community-brain/src/community_brain/openwebui/community_brain_filter.py`
- Test: `community-brain/tests/test_filter.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_filter.py`:

```python
def test_corpus_summary_renders_with_only_nonzero_counts():
    from community_brain.openwebui.community_brain_filter import render_corpus_summary

    metadata_summary = {
        "of_top_k": 10,
        "has_question_count": 4,
        "has_answer_count": 3,
        "has_unresolved_question_count": 6,
        "has_insight_count": 5,
        "references_prior_count": 0,  # zero → omitted
    }
    rendered = render_corpus_summary(metadata_summary)
    assert "of the 10 retrieved chunks" in rendered
    assert "6 are tagged unresolved_question" in rendered
    assert "5 are tagged insight" in rendered
    assert "4 are tagged question" in rendered
    assert "3 are tagged answer" in rendered
    assert "references_prior" not in rendered  # zero count omitted
    assert rendered.startswith("[corpus summary:")


def test_corpus_summary_orders_by_descending_count():
    from community_brain.openwebui.community_brain_filter import render_corpus_summary

    metadata_summary = {
        "of_top_k": 10,
        "has_question_count": 1,
        "has_answer_count": 2,
        "has_unresolved_question_count": 6,
        "has_insight_count": 0,
        "references_prior_count": 3,
    }
    rendered = render_corpus_summary(metadata_summary)
    # Order: 6 (unresolved_question) > 3 (references_prior) > 2 (answer) > 1 (question).
    pos_6 = rendered.find("unresolved_question")
    pos_3 = rendered.find("references_prior")
    pos_2 = rendered.find("answer")
    pos_1 = rendered.find("question, ")  # the one followed by ", " (questions_general)
    assert pos_6 < pos_3 < pos_2


def test_corpus_summary_empty_when_all_zero():
    from community_brain.openwebui.community_brain_filter import render_corpus_summary

    metadata_summary = {
        "of_top_k": 5,
        "has_question_count": 0, "has_answer_count": 0,
        "has_unresolved_question_count": 0, "has_insight_count": 0,
        "references_prior_count": 0,
    }
    rendered = render_corpus_summary(metadata_summary)
    # No flag-bearing chunks: the line is short / minimal but still renders
    # the of_top_k count for the LLM's awareness.
    assert "of the 5 retrieved chunks" in rendered
    assert "tagged" not in rendered  # no flags listed
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
./.venv/bin/pytest tests/test_filter.py -v -k "corpus_summary"
```

Expected: FAIL.

- [ ] **Step 3: Implement the renderer**

In `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

```python
def render_corpus_summary(metadata_summary: dict) -> str:
    """Build the '[corpus summary: ...]' single-line block from /query's
    metadata_summary field. Zero counts omitted. Counts ordered descending."""
    of_top_k = metadata_summary.get("of_top_k", 0)
    flag_to_label = {
        "has_question_count": "question",
        "has_answer_count": "answer",
        "has_unresolved_question_count": "unresolved_question",
        "has_insight_count": "insight",
        "references_prior_count": "references_prior",
    }
    pairs = [
        (metadata_summary.get(field, 0), label)
        for field, label in flag_to_label.items()
        if metadata_summary.get(field, 0) > 0
    ]
    pairs.sort(key=lambda p: -p[0])
    if pairs:
        clauses = ", ".join(f"{count} are tagged {label}" for count, label in pairs)
        return f"[corpus summary: of the {of_top_k} retrieved chunks, {clauses}]"
    return f"[corpus summary: of the {of_top_k} retrieved chunks]"
```

Wire `render_corpus_summary(metadata_summary)` into the filter's prompt-assembly path: prepend it as the first line of the LLM-facing context, above all chunks.

- [ ] **Step 4: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_filter.py -v -k "corpus_summary"
```

Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/openwebui/community_brain_filter.py community-brain/tests/test_filter.py
git commit -m "$(cat <<'EOF'
feat(openwebui): render [corpus summary: ...] at top of LLM context

Filter reads metadata_summary from /query response and prepends a
single line summarizing per-flag counts across retrieved chunks.
Zero counts omitted; sorted descending. Path (c) of F8 narrow fix.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 21: Add `expose_score_breakdown` filter valve

**Files:**
- Modify: `community-brain/src/community_brain/openwebui/community_brain_filter.py`
- Test: `community-brain/tests/test_filter.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_filter.py`:

```python
def test_score_breakdown_not_rendered_when_valve_off():
    """Default valve state (off): no [score: ...] line rendered."""
    # Construct a chunk with score_breakdown; render via filter with
    # default valves; assert no [score: line in output.


def test_score_breakdown_rendered_when_valve_on():
    """Valve on: [score: vector=X, bm25=Y, rrf=Z, cue=+W (rule)] rendered."""
```

- [ ] **Step 2: Run the tests to verify they fail.**

- [ ] **Step 3: Implement the valve**

In `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

Locate the `Valves` Pydantic class. Add:

```python
class Valves(BaseModel):
    # ... existing valves ...
    expose_score_breakdown: bool = Field(
        default=False,
        description="When True, prepend each chunk with a [score: ...] line "
                    "exposing vector_similarity / bm25_rank / rrf_score / "
                    "cue_delta / cue_rules_fired for operator-side debugging.",
    )
```

Add a renderer:

```python
def render_score_breakdown(score_breakdown: dict) -> str:
    """Build '[score: vector=0.42, bm25=3, rrf=0.024, cue=+0.01 (unresolved_questions)]'."""
    rules = score_breakdown.get("cue_rules_fired") or []
    cue_label = f"+{score_breakdown.get('cue_delta', 0.0):.3f}"
    if rules:
        cue_label += f" ({', '.join(rules)})"
    bm25_rank = score_breakdown.get("bm25_rank")
    bm25_str = "n/a" if bm25_rank is None else str(bm25_rank)
    return (f"[score: vector={score_breakdown.get('vector_similarity', 0.0):.3f}, "
            f"bm25={bm25_str}, "
            f"rrf={score_breakdown.get('rrf_score', 0.0):.3f}, "
            f"cue={cue_label}]")
```

In the chunk-assembly path, when `self.valves.expose_score_breakdown` is True, prepend `render_score_breakdown(chunk["score_breakdown"])` above the `[flags: ...]` line.

- [ ] **Step 4: Run the tests to verify they pass.**

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/openwebui/community_brain_filter.py community-brain/tests/test_filter.py
git commit -m "$(cat <<'EOF'
feat(openwebui): add expose_score_breakdown valve

Default-off: filter does not render score_breakdown to LLMs.
When operator flips the valve, each chunk is prepended with a
[score: vector=X, bm25=Y, rrf=Z, cue=+W (rules)] line for
debugging retrieval ranking. /query always returns the field;
the valve gates LLM-facing rendering only.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 22: Update embedded inference-guidelines constant in filter

**Files:**
- Modify: `community-brain/src/community_brain/openwebui/community_brain_filter.py`
- Test: `community-brain/tests/test_filter.py`

- [ ] **Step 1: Add a presentation-tags section to the embedded constant**

In `community-brain/src/community_brain/openwebui/community_brain_filter.py`:

Locate `_INFERENCE_GUIDELINES = """..."""`.

Append a new section just before the closing triple-quote:

```python
_INFERENCE_GUIDELINES = """...existing content...

### Presentation tags

When the answering context contains lines like `[flags: <flag_names>]` (per-chunk) or `[corpus summary: <counts>]` (above all chunks), these are presentation conventions exposing structured derived metadata. The `[flags: ...]` line lists boolean derived flags that Stage C marked True for the immediately-following chunk. The `[corpus summary: ...]` line gives authoritative counts of those flags across the retrieved set. Both are derived (the same trust-contract caveats apply — re-derive from `full_text` when in doubt), but they reflect what Stage C and the retrieval layer concluded; they are not invented by you.
"""
```

- [ ] **Step 2: Run the parity test**

```bash
./.venv/bin/pytest tests/test_filter.py::test_inference_guidelines_match_docs_file -v
```

Expected: FAIL — the docs file at `docs/inference-guidelines.md` doesn't yet have this section. Will fix in Task 27.

- [ ] **Step 3: Defer commit until Task 27 also updates the docs file**

Skip commit for now; the docs file update in Task 27 will pair with this filter change.

---

## Phase 7 — Corpus-lint pass (recurrent marker)

### Task 23: Implement `lint_corpus` CLI

**Files:**
- Create: `community-brain/src/community_brain/cli/lint_corpus.py`
- Test: `community-brain/tests/test_lint_corpus.py`

- [ ] **Step 1: Write the failing test**

Create `community-brain/tests/test_lint_corpus.py`:

```python
"""Tests for the lint_corpus CLI."""
from __future__ import annotations

from community_brain.cli.lint_corpus import lint_corpus_chunks


def test_recurrent_marker_applied_to_cross_session_neighbors(tmp_path):
    """A chunk in session-A with K=2 high-similarity neighbors in session-B
    and session-C gets the 'recurrent' marker."""
    # Create a small LanceDB at tmp_path with 3 sessions, each with 2 chunks.
    # 4 of the 6 chunks have very-similar embeddings (force via fixed test
    # vectors). Run lint_corpus_chunks; verify those 4 get 'recurrent'.


def test_unique_chunk_no_recurrent_marker(tmp_path):
    """A chunk with no above-threshold neighbors stays clean."""


def test_idempotent(tmp_path):
    """Running lint_corpus_chunks twice produces the same markers."""


def test_writes_corpus_markers_computed_at(tmp_path):
    """corpus_markers_computed_at is set to a non-null UTC timestamp."""
```

- [ ] **Step 2: Implement the CLI**

Create `community-brain/src/community_brain/cli/lint_corpus.py`:

```python
"""lint_corpus CLI — populate corpus_derived_markers on chunks.

For each chunk, find K-nearest neighbors in embedding space; flag as
'recurrent' if the neighbors include >= 2 from different sessions.

Spec §9. Auto-triggered at end of /ingest in Task 24.

Usage:
    python -m community_brain.cli.lint_corpus [--db /data/lancedb/nomic-v1]
"""
from __future__ import annotations

import argparse
import datetime as dt
import logging
from pathlib import Path

import lancedb


logger = logging.getLogger(__name__)

K_NEAREST = 8
SIMILARITY_THRESHOLD = 0.65
CROSS_SESSION_COUNT_MIN = 2


def lint_corpus_chunks(db_path: str | Path) -> dict[str, int]:
    """Apply 'recurrent' markers across the corpus; set computed_at on every row."""
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = table.to_arrow().to_pylist()
    now_iso = dt.datetime.utcnow().isoformat()

    recurrent_count = 0
    for row in rows:
        chunk_id = row["chunk_id"]
        session_id = row["session_id"]
        embedding = row["embedding"]
        # K-nearest neighbors via vector index.
        results = (
            table.search(embedding)
            .limit(K_NEAREST + 1)  # +1 to skip self
            .to_arrow()
            .to_pylist()
        )
        # Filter out self; keep above-threshold cross-session neighbors.
        cross_session_count = 0
        for nbr in results:
            if nbr["chunk_id"] == chunk_id:
                continue
            sim = 1 - nbr.get("_distance", 1.0)  # cosine similarity
            if sim < SIMILARITY_THRESHOLD:
                continue
            if nbr["session_id"] != session_id:
                cross_session_count += 1
        # Update markers.
        existing_markers = list(row.get("corpus_derived_markers") or [])
        if cross_session_count >= CROSS_SESSION_COUNT_MIN:
            if "recurrent" not in existing_markers:
                existing_markers.append("recurrent")
            recurrent_count += 1
        # Always update timestamp.
        table.update(
            where=f"chunk_id = '{chunk_id}'",
            values={
                "corpus_derived_markers": existing_markers,
                "corpus_markers_computed_at": now_iso,
            },
        )

    return {"scanned": len(rows), "recurrent": recurrent_count}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="/data/lancedb/nomic-v1")
    args = parser.parse_args()
    stats = lint_corpus_chunks(args.db)
    print(f"[ok] lint_corpus: scanned {stats['scanned']}, recurrent {stats['recurrent']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Run the tests to verify they pass**

```bash
./.venv/bin/pytest tests/test_lint_corpus.py -v
```

Expected: all PASS.

- [ ] **Step 4: Commit**

```bash
git add community-brain/src/community_brain/cli/lint_corpus.py community-brain/tests/test_lint_corpus.py
git commit -m "$(cat <<'EOF'
feat(cli): add lint_corpus with 'recurrent' marker

K-nearest neighbor scan (K=8, T=0.65, cross-session count >= 2)
identifies chunks whose topical content recurs across sessions.
Idempotent; writes corpus_derived_markers + corpus_markers_computed_at.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 24: Pipeline auto-triggers `lint_corpus` at end of `/ingest`

**Files:**
- Modify: `community-brain/src/community_brain/ingestion/pipeline.py`
- Test: `community-brain/tests/test_ingestion_pipeline.py`

- [ ] **Step 1: Write the failing test**

Append to `community-brain/tests/test_ingestion_pipeline.py`:

```python
def test_ingest_session_auto_triggers_lint_corpus(
    tmp_path, monkeypatch, mocked_pipeline_env
):
    """After ingest_session commits, corpus_markers_computed_at is set
    on the new chunks."""
    # Setup: ingest one session via ingest_session. Open the LanceDB.
    # Assert all newly-committed chunks have corpus_markers_computed_at != None.
```

- [ ] **Step 2: Wire the auto-trigger**

In `community-brain/src/community_brain/ingestion/pipeline.py`, at the end of `ingest_session` (after chunks are committed):

```python
from community_brain.cli.lint_corpus import lint_corpus_chunks

# At the very end of ingest_session, after _commit_chunks succeeds:
try:
    db_path = os.environ.get("COMMUNITY_BRAIN_DB_PATH") or "/data/lancedb/nomic-v1"
    stats = lint_corpus_chunks(db_path)
    logger.info(
        "lint_corpus auto-trigger: scanned %d, recurrent %d",
        stats["scanned"], stats["recurrent"],
    )
except Exception as exc:
    logger.warning("lint_corpus auto-trigger failed: %s; chunks committed", exc)
```

- [ ] **Step 3: Run the tests**

```bash
./.venv/bin/pytest tests/test_ingestion_pipeline.py -v
```

- [ ] **Step 4: Commit**

```bash
git add community-brain/src/community_brain/ingestion/pipeline.py community-brain/tests/test_ingestion_pipeline.py
git commit -m "$(cat <<'EOF'
feat(ingestion): auto-trigger lint_corpus at end of /ingest

After successful chunk commit, ingest_session runs lint_corpus to
refresh corpus_derived_markers across the (now-larger) corpus.
WARN-on-failure: chunks are already committed; lint will retry on
next ingest or manual run.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 8 — Docs and final integration

### Task 25: Update CHANGELOG.md migration entries

**Files:**
- Modify: `docs/migrations/CHANGELOG.md`

- [ ] **Step 1: Append the v3 entry**

In `docs/migrations/CHANGELOG.md`, add a new entry at the top of the migration log:

```markdown
## 2026-04-29 — Schema 1.0 → 1.1 + Stage C v2 + FTS column migration (Retrieval v3)

### Schema changes
- Additive: new `bm25_text` string column on chunks. Synthesized at chunk write as the concatenation of `topic_label`, `entities`, `speakers_spoke`, `speakers_mentioned`, `keywords`, and `full_text`. Required at write time (every chunk has it).
- `SCHEMA_VERSION` bumps `1.0` → `1.1`.
- Field types and existing field semantics unchanged.

### Stage C contract change
- Active extraction prompt: `chunk-extraction-v1` → `chunk-extraction-v2`.
- v2 emits typed `entities` (4 categories), populates `speakers_mentioned` (deterministic subset of entities-people not in `speakers_spoke`), populates `keywords` uniformly across all content types, drops `new_entities_seen` and `new_speakers_seen` from the JSON output schema.
- Pipeline applies a canonicalization pass at chunk write time, mapping `speakers_spoke` / `speakers_mentioned` / people-typed `entities` through `config/speaker-aliases.yaml`.

### Retrieval / index
- FTS index target column migrates from `full_text` to `bm25_text`. Server startup hook builds the new index; legacy index dropped on best-effort basis (idempotent).
- `cue_rules` data moves from hardcoded Python tuple to `config/query-cues.yaml`. Hot-reload on each `/query` call.
- `/query` response gains `metadata_summary` top-level field and per-chunk `score_breakdown`. Existing fields unchanged.

### Corpus-lint
- New `recurrent` marker populated by the `lint_corpus` pass, auto-triggered at end of `/ingest` and runnable on demand.

### Operator pattern
- Three new CLIs: `propose_canonicalizations`, `apply_canonicalizations` (auto-triggers recanonicalize), `recanonicalize` (standalone). See spec §7.

### Migration sequence (one-time)
- Drop existing v1.0 chunks table; re-extract 9 ingested sessions under v2 contract via `/ingest` with `force_reextract: true`. See spec §17.
```

- [ ] **Step 2: Commit**

```bash
git add docs/migrations/CHANGELOG.md
git commit -m "$(cat <<'EOF'
docs(migrations): add v3 schema + Stage C contract entry

Captures the schema 1.0 → 1.1 bump, Stage C v1 → v2, FTS column
migration, response shape additions, corpus-lint, and operator
canonicalization pattern. Migration sequence documented inline.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 26: Update community-brain/CLAUDE.md

**Files:**
- Modify: `community-brain/CLAUDE.md`

- [ ] **Step 1: Remove closed v2 backlog items**

In `community-brain/CLAUDE.md` "Known v2 backlog" section, REMOVE these items (now closed by v3):

- `**entities` field underpopulated.` (and its multi-line follow-up)
- `**speakers_mentioned` population...`
- `**Corpus-derived markers...` (now implemented via lint_corpus)

- [ ] **Step 2: Update "Trade-offs we've deliberately kept"**

REPLACE the existing "/query ranking is hybrid" bullet with:

```markdown
- **`/query` ranking is hybrid (vector + BM25 RRF, k=60) with cue-driven metadata boosting.** v3 changes the FTS index target from `full_text` to a synthesized `bm25_text` column (concatenation of `topic_label`, `entities`, `speakers_spoke`, `speakers_mentioned`, `keywords`, `full_text`); see `docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md`. Pure-vector ranking is no longer available as an opt-in mode — vector-only path is reserved for internal graceful-degradation when the FTS index is unavailable. Cue rules live in `config/query-cues.yaml` (hot-reloaded per `/query`).
- **Speaker canonicalization is decoupled from extraction.** Stage C extracts raw names; the canonicalization pass at chunk write applies the registry; the standalone `recanonicalize` CLI handles future name additions without re-extracting. See spec §7.
- **`/query` response carries `metadata_summary` + per-chunk `score_breakdown`.** Top-level field gives authoritative aggregate counts; per-chunk breakdown gives retrieval-confidence info. Filter-side rendering is opt-in via the `expose_score_breakdown` valve.
```

- [ ] **Step 3: Update "Current status" section in root CLAUDE.md**

In `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/CLAUDE.md` — update the "Current status" section to reflect v3 in-flight or complete (the engineer reading this knows their state better than the spec author can predict; copy-edit appropriately).

- [ ] **Step 4: Commit**

```bash
git add community-brain/CLAUDE.md CLAUDE.md
git commit -m "$(cat <<'EOF'
docs(community-brain): mark v3-closed v2 backlog items + update trade-offs

Removes entities underpopulation, speakers_mentioned always-None,
and corpus_derived_markers gap from the v2 backlog (closed by v3).
Updates trade-offs section to document hybrid-on-bm25_text indexing,
canonicalization decoupling, and metadata_summary / score_breakdown.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 27: Update inference-guidelines.md docs file (parity with filter constant)

**Files:**
- Modify: `docs/inference-guidelines.md`
- (Pairs with Task 22's filter constant edit)

- [ ] **Step 1: Append the presentation-tags section**

At the end of `docs/inference-guidelines.md`, append:

```markdown

## Presentation tags

When the answering context contains lines like `[flags: <flag_names>]` (per-chunk) or `[corpus summary: <counts>]` (above all chunks), these are presentation conventions exposing structured derived metadata. The `[flags: ...]` line lists boolean derived flags that Stage C marked True for the immediately-following chunk. The `[corpus summary: ...]` line gives authoritative counts of those flags across the retrieved set. Both are derived (the same trust-contract caveats apply — re-derive from `full_text` when in doubt), but they reflect what Stage C and the retrieval layer concluded; they are not invented by you.
```

- [ ] **Step 2: Run the parity test**

```bash
./.venv/bin/pytest tests/test_filter.py::test_inference_guidelines_match_docs_file -v
```

Expected: PASS. (Task 22's filter constant + this docs file edit must contain identical text.)

- [ ] **Step 3: Commit Task 22 + Task 27 together**

```bash
git add docs/inference-guidelines.md community-brain/src/community_brain/openwebui/community_brain_filter.py
git commit -m "$(cat <<'EOF'
docs(inference-guidelines): document [flags:] / [corpus summary:] presentation tags

Adds a Presentation tags section explaining the new convention.
Trust contract structurally unchanged — derived metadata remains
probabilistic; the tags are signposts, not assertions.

Filter's embedded _INFERENCE_GUIDELINES constant updated in
parallel; test_inference_guidelines_match_docs_file enforces parity.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Phase 9 — Pre-deploy validation

### Task 28: Update golden queries fixture

**Files:**
- Modify: `community-brain/tests/fixtures/golden_queries.yaml`
- Modify: `community-brain/tests/test_golden_queries.py`

- [ ] **Step 1: Update the YAML fixture for v3 corpus shape**

Edit `community-brain/tests/fixtures/golden_queries.yaml` to add v3-specific assertions:

```yaml
# Existing v2 entity-grounded queries: keep as-is (verify chunks contain
# 'Adam' in full_text). Add new assertions covering entities array.

queries:
  # ... existing queries ...

  - id: v3_entities_populated_adam
    question: "Adam Gold Flamingo sales funnel"
    target_finding: "v3-entities"
    expected_chunk_ids: []  # operator updates after re-extract
    min_match_count: 5
    extra_assertions:
      - "any(chunk.entities contains 'Adam' substring) >= 5"

  - id: v3_canonicalization_speakers
    question: "speakers in Adam James session"
    target_finding: "v3-canonicalization"
    expected_chunk_ids: []
    min_match_count: 1
    extra_assertions:
      - "filters.speakers_spoke=['Adam James'] returns merged-canonical chunks"

  - id: v3_recurrent_marker_populated
    question: "recurring topics across sessions"
    target_finding: "v3-recurrent"
    expected_chunk_ids: []
    min_match_count: 1
    extra_assertions:
      - "any(chunk.corpus_derived_markers contains 'recurrent')"

  - id: v3_metadata_summary_present
    question: "anything"
    target_finding: "v3-metadata-summary"
    expected_chunk_ids: []
    min_match_count: 0
    extra_assertions:
      - "response.metadata_summary.of_top_k > 0"
      - "response.metadata_summary contains has_unresolved_question_count"
```

- [ ] **Step 2: Update the golden-queries test runner**

In `community-brain/tests/test_golden_queries.py`, add support for the new `extra_assertions` shape (or add new test functions covering them). The exact translation of `extra_assertions` strings to Python assertions should be done as a small dispatch helper.

- [ ] **Step 3: Run the test**

```bash
./.venv/bin/pytest tests/test_golden_queries.py -v
```

Expected: PASS (against synthetic test corpus where v3 features are exercised).

- [ ] **Step 4: Commit**

```bash
git add community-brain/tests/fixtures/golden_queries.yaml community-brain/tests/test_golden_queries.py
git commit -m "$(cat <<'EOF'
test(retrieval): add v3 golden queries (entities, canonicalization, recurrent, metadata_summary)

Extends the golden_queries fixture with assertions targeting v3
features. CI guards against ranking regressions on entity-grounded,
canonicalization, recurrent-marker, and response-shape queries.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 29: Run full test suite

**Files:** none (verification step)

- [ ] **Step 1: Run all tests**

```bash
./.venv/bin/pytest tests/ -v
```

Expected: all PASS. If failures: investigate and fix on the v3 branch before proceeding to deploy.

- [ ] **Step 2: Run with coverage as a sanity check**

```bash
./.venv/bin/pytest tests/ --tb=short -q
```

Expected: clean summary with no FAIL.

If anything fails: stop, fix, re-run.

---

## Phase 10 — Deploy and migration

### Task 30: Deploy v3 image to VM

**Files:** none (deployment step)

- [ ] **Step 1: Push branch to GitHub**

```bash
git push origin feat/retrieval-v3-stage-c-v2
```

- [ ] **Step 2: SSH to VM, pull, build, deploy**

Per `community-brain/docs/DEPLOYMENT.md` "Incremental update" section:

```bash
ssh n8n-automation 'cd ~/n8n && git fetch && git checkout feat/retrieval-v3-stage-c-v2 && docker compose build retrieval-server && docker compose up -d retrieval-server'
```

- [ ] **Step 3: Verify health and version**

```bash
curl -fsS http://10.1.30.10:8999/health
# expected: {"status":"ok"}
```

```bash
ssh n8n-automation 'docker exec community_brain_retrieval python -c "from community_brain.ingestion.schema import SCHEMA_VERSION; print(SCHEMA_VERSION)"'
# expected: 1.1
```

---

### Task 31: Drop existing v1.0 chunks table

**Files:** none (operational step)

> 🟡 **PERMISSION:** This is destructive (drops all 184 existing chunks). Per spec §17.1, this is the explicit schema migration step; the source artifacts remain at `/data/output/<date>/`, so re-extraction in Task 33 restores all 9 sessions under v1.1 schema.

- [ ] **Step 1: Confirm with operator before dropping**

Pause and confirm with the operator. Only proceed after explicit "go."

- [ ] **Step 2: Drop the table**

```bash
ssh n8n-automation 'docker exec community_brain_retrieval python -c "
import lancedb
db = lancedb.connect(\"/data/lancedb/nomic-v1\")
db.drop_table(\"chunks\")
print(\"chunks table dropped; will be recreated with v1.1 schema on first /ingest\")
"'
```

- [ ] **Step 3: Verify**

```bash
curl -fsS http://10.1.30.10:8999/sessions
# expected: {"total":0,"sessions":[]}
```

---

### Task 32: Curate the registry (propose + operator review + apply)

**Files:** `community-brain/canonicalization-proposals.yaml` (created by step 1; edited by operator)

- [ ] **Step 1: Run propose_canonicalizations**

```bash
ssh n8n-automation 'cd ~/n8n && docker exec community_brain_retrieval python -m community_brain.cli.propose_canonicalizations --registry /app/config/speaker-aliases.yaml --out /app/config/canonicalization-proposals.yaml'
```

- [ ] **Step 2: Pull the proposals YAML to local for review**

```bash
ssh n8n-automation 'docker exec community_brain_retrieval cat /app/config/canonicalization-proposals.yaml' > community-brain/canonicalization-proposals.yaml
```

- [ ] **Step 3: Operator reviews and edits**

Manual step. Open `community-brain/canonicalization-proposals.yaml` in an editor:
- Delete proposals that are wrong.
- Edit canonicals that need adjustment.
- Move ambiguous entries to `proposals` if you can disambiguate.

- [ ] **Step 4: Push edited YAML back to VM**

```bash
scp community-brain/canonicalization-proposals.yaml n8n-automation:~/n8n/community-brain/config/canonicalization-proposals.yaml
```

- [ ] **Step 5: Run apply_canonicalizations with --no-recanonicalize**

```bash
ssh n8n-automation 'cd ~/n8n && docker exec community_brain_retrieval python -m community_brain.cli.apply_canonicalizations /app/config/canonicalization-proposals.yaml --registry /app/config/speaker-aliases.yaml --no-recanonicalize'
```

The `--no-recanonicalize` flag is correct here because the chunks table is currently empty (Task 31 dropped it) — recanonicalize would be a no-op scan.

- [ ] **Step 6: Verify registry was updated**

```bash
ssh n8n-automation 'docker exec community_brain_retrieval cat /app/config/speaker-aliases.yaml | head -30'
```

Confirm the merged proposals appear under `aliases:`.

---

### Task 33: Re-extract the 9 sessions

**Files:** none (operational; uses existing `/ingest` endpoint)

- [ ] **Step 1: Run the curl loop**

```bash
ssh n8n-automation 'for date in 2025-02-02 2025-02-05 2025-02-09 2025-02-12 2025-02-16 2025-02-19 2026-04-14 2026-04-21 2026-04-28; do
  echo ">> ingesting $date"
  curl -X POST http://127.0.0.1:8999/ingest \
    -H "Content-Type: application/json" \
    -d "{\"session_id\":\"$date\",\"session_date\":\"$date\",\"artifacts\":{\"prepared_transcript\":\"/data/output/$date/prepared-transcript.md\",\"extracted_signal\":\"/data/output/$date/extracted-signal.md\",\"community_post\":\"/data/output/$date/community-post.md\"},\"force_reextract\":true}"
  echo
  sleep 30
done'
```

Expected: ~9 minutes wall, ~$0.50 LLM cost. Each ingest logs Stage C v2 + canonicalization + bm25_text + lint_corpus auto-trigger.

- [ ] **Step 2: Verify all 9 sessions ingested**

```bash
curl -fsS http://10.1.30.10:8999/sessions | python3 -c "import sys, json; d = json.load(sys.stdin); print(f'sessions: {d[\"total\"]}'); [print(s['session_id']) for s in d['sessions']]"
```

Expected: `sessions: 9` plus all 9 session_ids listed.

- [ ] **Step 3: Spot check a single chunk**

```bash
curl -fsS -X POST http://10.1.30.10:8999/query -H "Content-Type: application/json" -d '{"question":"Adam Gold Flamingo sales funnel","top_k":3}' | python3 -m json.tool | head -80
```

Expected: response includes `metadata_summary`, `chunks` with `score_breakdown`, and at least one chunk has "Adam" appearing in `entities` array.

---

## Phase 11 — Validation gate and sign-off

### Task 34: Run the 8-criteria validation gate

**Files:** none (verification)

- [ ] **Step 1: 16.1.1 — F8 fix answering accuracy**

Manual step in Open WebUI: ask "What unresolved questions came up across these calls that didn't get fully answered?" with GPT-oss 20B. Count the unresolved questions cited. Target: ≥ 5 of the 6+ tagged.

- [ ] **Step 2: 16.1.2 — Entities populated and indexed**

```bash
curl -fsS -X POST http://10.1.30.10:8999/query -H "Content-Type: application/json" -d '{"question":"Adam Gold Flamingo","top_k":10}' | python3 -c "
import sys, json
d = json.load(sys.stdin)
hits = sum(1 for c in d['chunks'] if any('adam' in str(e).lower() for e in c['ground_truth'].get('entities') or []))
print(f'chunks with Adam in entities: {hits}/10')
assert hits >= 5, f'FAIL: expected >= 5, got {hits}'
print('PASS')
"
```

- [ ] **Step 3: 16.1.3 — Canonicalization applied**

```bash
# Replace <CANON> with the canonical form chosen by the operator (e.g., 'Adam James').
curl -fsS -X POST http://10.1.30.10:8999/query -H "Content-Type: application/json" -d '{"question":"anything","top_k":10,"filters":{"speakers_spoke":["<CANON>"]}}'
```

Expected: returns chunks where `speakers_spoke` contains `<CANON>`. Operator confirms count matches their proposal merges.

- [ ] **Step 4: 16.1.4 — recurrent marker populated**

```bash
ssh n8n-automation 'docker exec community_brain_retrieval python -c "
import lancedb
db = lancedb.connect(\"/data/lancedb/nomic-v1\")
tbl = db.open_table(\"chunks\")
rows = tbl.to_arrow().to_pylist()
total = len(rows)
recurrent = sum(1 for r in rows if r.get(\"corpus_derived_markers\") and \"recurrent\" in r[\"corpus_derived_markers\"])
print(f\"recurrent: {recurrent}/{total} = {100*recurrent/total:.1f}%\")
assert recurrent / total >= 0.30, f\"FAIL: expected >= 30%, got {100*recurrent/total:.1f}%\"
print(\"PASS\")
"'
```

- [ ] **Step 5: 16.1.5 — score_breakdown surfaced**

```bash
curl -fsS -X POST http://10.1.30.10:8999/query -H "Content-Type: application/json" -d '{"question":"anything","top_k":3}' | python3 -c "
import sys, json
d = json.load(sys.stdin)
required = {'vector_similarity', 'bm25_rank', 'rrf_score', 'cue_delta', 'cue_rules_fired'}
for c in d['chunks']:
    sb = c.get('score_breakdown') or {}
    missing = required - set(sb.keys())
    assert not missing, f'FAIL: chunk missing {missing}'
print('PASS')
"
```

- [ ] **Step 6: 16.1.6 — [flags:] and [corpus summary:] rendered**

Manual: in Open WebUI, ask any question, observe the LLM's input context — should contain `[corpus summary: ...]` line at top and `[flags: ...]` lines on chunks with True flags. Filter unit tests already cover this in CI; this is the live-check.

- [ ] **Step 7: 16.1.7 — Test suite green**

```bash
ssh n8n-automation 'cd ~/n8n/community-brain && ./.venv/bin/pytest tests/ -q'
# expected: all PASS
```

- [ ] **Step 8: 16.1.8 — No regression on Findings 6 & 7**

```bash
# Finding 6 query
curl -fsS -X POST http://10.1.30.10:8999/query -H "Content-Type: application/json" -d '{"question":"What did Adam from Gold Flamingo commit to?","top_k":10}' | python3 -c "
import sys, json
d = json.load(sys.stdin)
hits = sum(1 for c in d['chunks'] if 'adam' in (c['ground_truth']['full_text'] or '').lower())
print(f'F6 (Adam in full_text): {hits}/10')
assert hits >= 5, f'FAIL: expected >= 5, got {hits}'
"

# Finding 7 query
curl -fsS -X POST http://10.1.30.10:8999/query -H "Content-Type: application/json" -d '{"question":"What unresolved questions came up across these calls?","top_k":10}' | python3 -c "
import sys, json
d = json.load(sys.stdin)
hits = sum(1 for c in d['chunks'] if c['derived_metadata'].get('has_unresolved_question'))
print(f'F7 (has_unresolved_question): {hits}/10')
assert hits >= 5, f'FAIL: expected >= 5, got {hits}'
"
```

Expected: both PASS.

- [ ] **Step 9: All 8 criteria pass**

If any fail: tune (Stage C prompt, alias map, cue Δ values, recurrent threshold) and re-validate. Plan C is gated on all 8.

---

### Task 35: Document validation outcomes; merge to main

**Files:**
- Modify: `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md`
- Modify: `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`
- Modify: `CLAUDE.md` (root)

- [ ] **Step 1: Append v3 validation addendum to Plan A spec**

In `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` §10, after the existing v2 validation addendum, add a v3 addendum:

```markdown
##### v3 retrieval + Stage C v2 validation (2026-04-29 — against live VM)

Retrieval v3 (`docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md`) deployed to the live VM via the standard runbook. v1.0 chunks table dropped; 9 sessions re-extracted under chunk-extraction-v2; speaker registry curated via propose_canonicalizations + apply_canonicalizations; FTS index migrated to bm25_text column; cue rules loaded from query-cues.yaml.

[Capture the outcomes for each of the 8 validation criteria here, formatted similarly to the v2 addendum. Quantitative numbers, manual-check confirmations, and any tuning iterations required. If any criterion failed and tuning resolved it, document the failure mode + fix.]

**Sign-off:** v3 [delivers / partially delivers / blocks] what the design promised. [F8 outcome.] [F6/F7 regression check outcome.] Plan C [is now ready to run / blocked on follow-up tuning].
```

- [ ] **Step 2: Update COMMUNITY-BRAIN-NEXT-STEPS.md**

In `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`:
- Mark v3 as DONE under "Where the project is right now."
- Update the "v3 design (when warranted)" subsection to "v3 (shipped 2026-04-29)" with what landed and what got deferred to v4.
- Update the Track B starter prompt with the v3-deployed reference.

- [ ] **Step 3: Update root CLAUDE.md "Current status"**

In `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/CLAUDE.md`:
- "Current status (as of 2026-04-29)" — add v3 entry: deployed, validated, Plan C ready.

- [ ] **Step 4: Commit and merge**

```bash
git add docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md CLAUDE.md
git commit -m "$(cat <<'EOF'
docs: capture v3 validation outcomes; mark v3 deployed

Plan A spec §10 gets a v3 validation addendum.
COMMUNITY-BRAIN-NEXT-STEPS marks v3 done; Track B (Plan C) ready.
Root CLAUDE.md current-status updated.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"

git checkout main
git merge feat/retrieval-v3-stage-c-v2
git push origin main
```

---

## Self-review

After writing, this plan was checked against the spec for:

**Spec coverage:** Every section of `2026-04-29-retrieval-v3-and-stage-c-v2-design.md` maps to at least one task:
- §3-§5 schema → T1, T2, T3
- §6 Stage C v2 → T4, T5, T6, T7
- §7 canonicalization → T8, T9, T10, T11, T12
- §8 F8 fix paths b/c → T19, T20, T22, T27
- §9 corpus-lint → T23, T24
- §10 bm25_text → T1, T2, T3, T18
- §11 score_breakdown → T15, T17, T21
- §12 YAML cue rules → T13, T14
- §13 component changes → T1-T28
- §14 API contract → T17, T21 (additive)
- §15 perf budget → no specific task; verified by T29 (test suite)
- §16 validation gate → T34
- §17 rollout sequence → T30, T31, T32, T33
- §18 open questions for implementation → flagged inline as `> Note:` callouts
- Appendix A audit data → captured in spec; informational only

**Placeholder scan:** No TBD / TODO / "implement later" / "similar to Task N" / "appropriate error handling" markers in the plan body. Step-level Notes for "verify exact LanceDB API in 0.30.2" and "mirror the existing test harness pattern" are explicit pointers to existing code, not placeholders.

**Type consistency:** `Chunk` dataclass field name `bm25_text` consistent across T1, T2, T3, T8, T11, T18. `metadata_summary` consistent across T16, T17, T20. `score_breakdown` consistent across T15, T17, T21. CueRule predicate types (`field/value`, `field/check non_empty`, `field/check contains`) consistent in T13. Cue rule names consistent between `cue_rules.py` (T13) and `query-cues.yaml` (T13).

---

**Total tasks:** 35.
**Estimated implementation time:** 3-5 days for code (T1-T29) + ~1 hour for deploy + curate + re-extract (T30-T33) + 30 min for validation gate (T34) + 30 min for sign-off docs (T35).
