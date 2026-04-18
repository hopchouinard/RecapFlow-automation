# Community Brain Ingestion Pipeline — Plan A (Phases 1 & 2)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship config artifacts + a Python retrieval server that can ingest the three artifact types (prepared-transcript, extracted-signal, community-post) into LanceDB with the v1.0 schema, and serve them via the extended `/query` API.

**Architecture:** Extend the existing `community-brain` Python package with a new `ingestion/` subpackage (parser, chunker, extractor, pipeline) and expand `retrieval_server.py` with `/ingest`, `/sessions`, and `/reindex` endpoints. All LLM calls go through the existing OpenRouter client. LanceDB stores the new 37-field schema. Tests use pytest with mocked LLM responses.

**Tech Stack:** Python 3.11+, FastAPI, LanceDB, Ollama (nomic-embed-text), OpenRouter (Gemini 3.1 Flash Lite), PyYAML, pytest, tiktoken.

**Reference spec:** [2026-04-18-community-brain-ingestion-pipeline-design.md](../specs/2026-04-18-community-brain-ingestion-pipeline-design.md)

**Scope:** Phases 1 and 2 from the spec's rollout plan. Phases 3-6 (n8n workflows, backfill execution, Open WebUI integration) are separate plans.

---

## File Structure

All paths are relative to repo root unless otherwise noted. `CB/` is shorthand for `community-brain/`.

### New files

**Config artifacts (Phase 1):**
- `CB/config/speaker-aliases.yaml` — canonical speaker registry
- `CB/config/entity-registry.yaml` — canonical entity registry
- `CB/config/chunking.yaml` — token thresholds and tunables
- `CB/config/extraction-config.yaml` — points at active prompt versions
- `CB/config/extraction-prompts/prep-prompt-v1.md`
- `CB/config/extraction-prompts/chunk-extraction-v1.md`
- `CB/config/extraction-prompts/session-themes-v1.md`
- `CB/config/extraction-prompts/extract-signal-v1.md`
- `CB/config/extraction-prompts/CHANGELOG.md`
- `docs/inference-guidelines.md` (repo root)
- `docs/migrations/CHANGELOG.md` (repo root)

**Python modules (Phase 2):**
- `CB/src/community_brain/ingestion/__init__.py`
- `CB/src/community_brain/ingestion/schema.py` — LanceDB schema definition (v1.0, 37 fields)
- `CB/src/community_brain/ingestion/config_loader.py` — YAML config loading
- `CB/src/community_brain/ingestion/registries.py` — speaker & entity registry load/append with atomic writes
- `CB/src/community_brain/ingestion/parser.py` — parse the three artifact types
- `CB/src/community_brain/ingestion/chunker.py` — produce Chunk records from parsed content
- `CB/src/community_brain/ingestion/extractor.py` — Stage C LLM chunk extraction
- `CB/src/community_brain/ingestion/session_extractor.py` — Stage B session-level extraction
- `CB/src/community_brain/ingestion/pipeline.py` — orchestrator (parse → chunk → extract → embed → commit)

**Tests:**
- `CB/tests/test_config_loader.py`
- `CB/tests/test_registries.py`
- `CB/tests/test_ingestion_parser.py`
- `CB/tests/test_ingestion_chunker.py`
- `CB/tests/test_ingestion_extractor.py`
- `CB/tests/test_ingestion_session_extractor.py`
- `CB/tests/test_ingestion_pipeline.py`
- `CB/tests/test_retrieval_server_ingest.py`
- `CB/tests/fixtures/prepared-transcript-sample.md`
- `CB/tests/fixtures/extracted-signal-sample.md`
- `CB/tests/fixtures/community-post-sample.md`

### Modified files

- `CB/src/community_brain/query/retrieval_server.py` — extend `/query`, add `/ingest`, `/reindex`, `/sessions`
- `CB/src/community_brain/query/query_local.py` — extend `search_chunks` with new filter fields and structured result
- `CB/pyproject.toml` — add `pyyaml` dependency

---

## Task List

Phase 1 is small (create config files). Phase 2 is the bulk of the work (TDD implementation of the ingestion pipeline).

---

## PHASE 1 — Config Artifacts

### Task 1: Create speaker-aliases.yaml

**Files:**
- Create: `community-brain/config/speaker-aliases.yaml`

- [ ] **Step 1: Create the file with initial aliases**

```yaml
# Canonical speaker alias registry.
# Maps raw names (as they appear in transcripts) to canonical full names.
# Ingestion pipeline reads this at startup; unknown speakers get appended to `pending:`.

version: "2026-04-18"

aliases:
  Alex Rojas:
    - alexrojas
    - "Alex R"
    - arojas
  Alex Wilson:
    - AlexH
    - "Alex H"
  Sam:
    - sam
    - "Sam C"
  Shakur:
    - shakur

pending: []
```

- [ ] **Step 2: Commit**

```bash
git add community-brain/config/speaker-aliases.yaml
git commit -m "config(community-brain): add canonical speaker aliases YAML"
```

---

### Task 2: Create entity-registry.yaml

**Files:**
- Create: `community-brain/config/entity-registry.yaml`

- [ ] **Step 1: Create the file (empty seed; will be populated as ingestion discovers entities)**

```yaml
# Canonical entity registry.
# Maps raw entity mentions (tools, people, companies, concepts) to canonical names.
# Ingestion pipeline reads this; unknowns get appended to `pending:`.
#
# Structure:
#   entities:
#     <CanonicalName>:
#       type: tool | framework | company | person | concept | product
#       category: <optional grouping string>
#       aliases: [list of raw mentions that should resolve here]

version: "2026-04-18"

entities: {}

pending: []
```

- [ ] **Step 2: Commit**

```bash
git add community-brain/config/entity-registry.yaml
git commit -m "config(community-brain): add empty entity registry with pending queue"
```

---

### Task 3: Create chunking.yaml

**Files:**
- Create: `community-brain/config/chunking.yaml`

- [ ] **Step 1: Create the file**

```yaml
# Chunking and extraction tunables for the ingestion pipeline.
# Read at startup by community_brain.ingestion.config_loader.

schema_version: "1.0"

chunking:
  # Prepared-transcript segments longer than this get sub-chunked (sliding window).
  transcript_segment_max_tokens: 1500

  # Community posts longer than this get sliding-window split (rare).
  post_max_tokens: 2500

  # Stage B input threshold: community_post used only if under this size.
  session_themes_input_max_tokens: 3000

extraction:
  # Retries per LLM call before marking the chunk extraction_status = "failed".
  retry_attempts: 3

  # Exponential backoff in seconds between retry attempts.
  retry_backoff_seconds: [2, 8, 32]

  # Inter-session delay for batch (Workflow 2) ingestion.
  inter_session_delay_seconds: 30
```

- [ ] **Step 2: Commit**

```bash
git add community-brain/config/chunking.yaml
git commit -m "config(community-brain): add chunking and extraction tunables"
```

---

### Task 4: Create extraction-config.yaml

**Files:**
- Create: `community-brain/config/extraction-config.yaml`

- [ ] **Step 1: Create the file**

```yaml
# Active extraction prompt versions per stage.
# Bump this file when swapping in a new prompt version.
# Bumping does NOT re-extract existing chunks; that requires a POST /reindex call.

session_themes:
  prompt_file: session-themes-v1.md
  model: google/gemini-3.1-flash-lite-preview

chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: google/gemini-3.1-flash-lite-preview

# extract_signal and prep_prompt are produced by n8n but tracked here for
# version coordination across the pipeline.
extract_signal:
  prompt_file: extract-signal-v1.md

prep_prompt:
  prompt_file: prep-prompt-v1.md
```

- [ ] **Step 2: Commit**

```bash
git add community-brain/config/extraction-config.yaml
git commit -m "config(community-brain): add extraction config pointing at v1 prompts"
```

---

### Task 5: Create extraction prompts

**Files:**
- Create: `community-brain/config/extraction-prompts/prep-prompt-v1.md`
- Create: `community-brain/config/extraction-prompts/chunk-extraction-v1.md`
- Create: `community-brain/config/extraction-prompts/session-themes-v1.md`
- Create: `community-brain/config/extraction-prompts/extract-signal-v1.md`
- Create: `community-brain/config/extraction-prompts/CHANGELOG.md`

- [ ] **Step 1: Create prep-prompt-v1.md**

```markdown
# Transcript Preparation Prompt (v1)

You are preparing a meeting transcript for embedding in a semantic knowledge base. Transform the raw transcript into an enriched, topic-segmented document that will produce high-quality, independently retrievable chunks when split.

## Speaker Name Normalization

Apply the speaker alias map supplied in the `SPEAKER_ALIASES` context block below. If you encounter a speaker whose raw name is NOT in that map, do NOT guess a canonical form — pass the name through unchanged AND list it under "=== UNRESOLVED SPEAKERS ===" at the end of your output.

{{SPEAKER_ALIASES_BLOCK}}

## Pass 1 — Clean the transcript

- Apply speaker normalization above
- Fix obvious transcription artifacts: "gpt four" → "GPT-4", "llm" → "LLM", "open a i" → "OpenAI"
- Remove pure filler (stutters, "um", "uh") only when they add no meaning
- Preserve all timestamps and speaker attribution exactly

## Pass 2 — Segment by topic

Divide the transcript into coherent topic blocks. Start a new segment when the conversation meaningfully shifts subject. For each segment, prepend a structured header:

<!--SEGMENT
topic: <2–5 word label>
speakers: <comma-separated list of speakers who contribute>
keywords: <8–12 terms: tools, models, concepts, companies, people explicitly mentioned>
summary: <2–3 sentence description of what this segment covers and why it matters>
-->

Target 300–500 words per segment body. If a topic recurs later, open a new segment — do not merge non-contiguous discussion.

## Pass 3 — Inline annotations

Within each segment body, mark key moments:

- When a tool, service, model, or product is named: append `[tool:name]` after first mention
- When someone asks a question: wrap with `<Q>` ... `</Q>`
- When someone answers it: wrap with `<A>` ... `</A>`
- When a URL or resource is shared: append `[link:url-or-description]`
- When a sentence contains a concrete recommendation or takeaway: prefix with `▶`

## Output format

```
=== SESSION ===
date: YYYY-MM-DD
duration_estimate: ~X min
main_themes: [3–6 overarching topics]
===

<!--SEGMENT
topic: ...
speakers: ...
keywords: ...
summary: ...
-->

[HH:MM:SS] Speaker Name: transcript text [tool:X] continued text
<Q>[HH:MM:SS] Speaker: question</Q>
<A>[HH:MM:SS] Speaker: answer</A>

<!--SEGMENT
...
-->

...

=== UNRESOLVED SPEAKERS ===
- raw_name_1 (appears N times, example: "<first line they spoke>")
- raw_name_2 (appears N times, example: "...")
===
```

If no unresolved speakers, omit the "=== UNRESOLVED SPEAKERS ===" section entirely.

## Quality constraints

- Do not invent or infer content not present in the source
- Every segment must be independently understandable
- Segment header `keywords` and `summary` are what get embedded — make them precise and information-dense
- Prefer 8 focused segments over 4 sprawling ones
```

- [ ] **Step 2: Create chunk-extraction-v1.md**

```markdown
# Chunk Extraction Prompt (v1)

You extract structured metadata from a single chunk of conversational content. Your output MUST be valid JSON matching the schema described below. Do not include any prose, markdown, or explanation outside the JSON.

## Input context

You will receive:
- `CHUNK_TEXT` — the full text of the chunk (may include speaker attribution, segment headers, inline tags)
- `ENTITY_REGISTRY` — list of canonical entity names and their aliases
- `SPEAKER_ALIASES` — list of canonical speaker names and their aliases

## Output schema (JSON)

```json
{
  "entities": ["list of canonical entity names explicitly mentioned in CHUNK_TEXT"],
  "new_entities_seen": ["mentions that appear to be entities but don't match the registry"],
  "new_speakers_seen": ["speaker names in CHUNK_TEXT that don't match SPEAKER_ALIASES"],
  "speech_acts": ["one or more of: question | answer | opinion | recommendation | warning | anecdote | decision | action_item | prediction | comparison | definition"],
  "stance": "positive | negative | neutral | mixed | null",
  "certainty": "asserted | hedged | speculative",
  "chunk_local_markers": ["zero or more of: emphasized | sustained | breakthrough | resolved"],
  "decisions": ["zero or more concrete decisions/conclusions stated in the chunk"] ,
  "action_items": ["zero or more explicit commitments like 'X will do Y'"],
  "external_refs": ["zero or more URLs, paper titles, or resource references mentioned"],
  "references_prior": true
}
```

## Extraction rules

1. **entities** — Only include canonical names from ENTITY_REGISTRY whose aliases or canonical form appear in CHUNK_TEXT. Empty list if none.

2. **new_entities_seen** — Names that LOOK LIKE entities (tools, products, companies, frameworks) but don't resolve via the registry. These go to a review queue; do not guess their canonical form.

3. **new_speakers_seen** — Speaker attributions in CHUNK_TEXT (e.g., after `[HH:MM:SS]`) that don't match any canonical name or alias in SPEAKER_ALIASES. Empty list if all speakers are known.

4. **speech_acts** — List all that apply. A chunk may contain multiple (e.g., a question AND an answer). Use null NOT empty-list ONLY if the chunk is pure exposition without any of the listed act types.

5. **stance** — Positive/negative/neutral about the chunk's main topic or entity. Use "mixed" when the speaker explicitly weighs pros and cons. Use null when stance isn't applicable (pure factual exposition, questions-only chunks).

6. **certainty** — "asserted" for confident claims; "hedged" when the speaker uses "I think", "maybe", "probably"; "speculative" for "what if" or "I imagine" framing.

7. **chunk_local_markers**:
   - `emphasized` — speakers explicitly signal importance ("this is key", "the big thing is", "I want to stress")
   - `sustained` — multiple speakers engage across 3+ turns on the same specific point
   - `breakthrough` — speakers frame as novel ("I just realized", "this changes how I think about X")
   - `resolved` — contains a decision, conclusion, or closed question

8. **decisions** and **action_items** — Extract as short, self-contained strings. A decision is a conclusion reached ("We'll use nomic-embed-text"). An action item is a commitment ("Sam will benchmark LangChain by Friday"). Empty list when none.

9. **external_refs** — URLs verbatim when present; otherwise clear resource references ("the Langchain docs", "the paper Alex mentioned"). Empty list when none.

10. **references_prior** — `true` if the chunk explicitly refers to a previous session or earlier discussion ("like we discussed last week", "following up on the thread from March"). `false` otherwise.

## Rules

- Output ONLY the JSON object. No prose before or after.
- Every field must be present. Use `null` or `[]` when the field doesn't apply — never omit.
- Do not invent content. Only extract what's explicitly present.
- When in doubt, prefer null / empty list over guessing.
```

- [ ] **Step 3: Create session-themes-v1.md**

```markdown
# Session Themes Extraction Prompt (v1)

You extract 3-5 high-level themes from a summary of one coaching call session. Your output MUST be valid JSON matching the schema below.

## Input context

You will receive `SESSION_INPUT` — one of:
- A community post (narrative session summary), OR
- A concatenation of segment headers from the prepared transcript, OR
- An extracted-signal document (categorized facts)

## Output schema (JSON)

```json
{
  "themes": ["3-5 high-level themes, each 2-6 words"]
}
```

## Extraction rules

1. Themes are the main topics the session covered, at a zoom-out level. Not specific tools or people — topics.
2. Good examples: "agent framework comparison", "production deployment patterns", "embedding model tradeoffs".
3. Bad examples (too specific): "Alex's LangChain demo", "the GPU pricing question".
4. Bad examples (too broad): "AI", "coding", "tools".
5. Minimum 3 themes, maximum 5. Favor fewer, higher-quality themes over padding.
6. Output ONLY the JSON object. No prose.
```

- [ ] **Step 4: Create extract-signal-v1.md**

```markdown
# Extract Signal Prompt (v1)

You extract structured information from a merged coaching call (transcript + chat log) or a raw transcript alone. Output is a markdown document with a fixed set of section headings.

## Allowed sections (use these EXACT headings, omit entirely when empty)

- `## tools` — tools, services, products, libraries discussed
- `## qa` — question and answer pairs
- `## insights` — key takeaways, recommendations, lessons
- `## links` — URLs and resources shared
- `## decisions` — decisions made or conclusions reached
- `## general` — content that doesn't fit the above

## Output format

```
## tools

- Tool name — brief context from the call
- ...

## qa

**Q (Speaker):** question text
**A (Speaker):** answer text

## insights

- Key takeaway — context
- ...

## links

- URL or resource — brief description of what it is
- ...

## decisions

- Decision reached — who decided, what's the next step
- ...

## general

- Anything else worth capturing
```

## Rules

1. Use ONLY the six allowed heading slugs. Do not invent new ones.
2. Omit entire sections when they would be empty.
3. Preserve speaker attribution in Q&A sections.
4. Do not invent content not present in the source.
5. When chat log is present, prefer it for link/tool extraction (more accurate than transcript).
6. For a transcript-only source, this document will be thinner — that's expected.
```

- [ ] **Step 5: Create CHANGELOG.md**

```markdown
# Extraction Prompts Changelog

## 2026-04-18 — v1 initial set

- `prep-prompt-v1.md` — transcript preparation with segment markers and inline tags
- `chunk-extraction-v1.md` — per-chunk structured metadata extraction
- `session-themes-v1.md` — session-level theme extraction
- `extract-signal-v1.md` — merged-content signal extraction with canonical vocabulary
```

- [ ] **Step 6: Commit**

```bash
git add community-brain/config/extraction-prompts/
git commit -m "config(community-brain): add v1 extraction prompts with canonical vocabulary"
```

---

### Task 6: Create inference-guidelines.md

**Files:**
- Create: `docs/inference-guidelines.md`

- [ ] **Step 1: Create the file**

```markdown
# Community Brain — Inference Guidelines

This document defines the contract between the Community Brain retrieval server and downstream LLM consumers (Open WebUI filter, query scripts, custom agents). It MUST be prepended to any system prompt that reasons over retrieved chunks.

## Trust hierarchy

- **`ground_truth.full_text` is authoritative.** All direct quotes must come from here.
- **`derived_metadata` fields** (stance, speech_acts, chunk_local_markers, decisions, action_items, entities, topic_label, etc.) are LLM-extracted approximations. Use them to orient your retrieval and frame your response, but verify against `full_text` before citing as fact.
- **`provenance`** tells you which extraction prompt version produced the derived fields. Treat older extractions with appropriate skepticism.

## Rules when generating responses

1. Direct quotes must cite a specific `chunk_id` and be locatable in that chunk's `full_text`.
2. When summarizing what someone said, check `speakers_spoke` against `full_text` attribution — the former is LLM-inferred, the latter shows actual speaker labels.
3. Claims about decisions, outcomes, or action items: verify against `full_text` before stating. The `decisions` and `action_items` fields are hints, not records.
4. When `derived_metadata` fields are null (e.g., on older chunks), reason from `full_text` alone. Do NOT infer "no decisions" from "decisions field is null" — absence means the chunk predates that extraction.
5. If `full_text` contradicts a `derived_metadata` value, state the source-of-truth reading and flag the discrepancy.

## Tolerating mixed generations

Corpus chunks may be from different `schema_version` or `extraction_prompt_version` eras. Missing fields are normal. Field richness varies. Reason from what's present; don't speculate about what's absent.

## Enforcement boundary

The reference compliant consumer is the `community_brain_filter` Open WebUI function. Consumers that bypass these guidelines — direct LanceDB access, custom API clients that ignore the `ground_truth` vs `derived_metadata` distinction, LLM prompts that don't prepend this fragment — are considered **unsupported**. The system's correctness guarantees apply only within the enforcement boundary.
```

- [ ] **Step 2: Commit**

```bash
git add docs/inference-guidelines.md
git commit -m "docs: add Community Brain inference guidelines contract"
```

---

### Task 7: Create docs/migrations/CHANGELOG.md

**Files:**
- Create: `docs/migrations/CHANGELOG.md`

- [ ] **Step 1: Create the file**

```markdown
# Community Brain — Schema and Extraction Migration Log

Every schema version bump or extraction-breaking change is recorded here.

## Entry template

```
## YYYY-MM-DD — vX.Y {short description}
- Change: {what changed}
- Rationale: {why}
- Migration: {automatic | reindex required | full re-ingest}
- Affected chunks: {scope}
- Rollback: {plan if this goes wrong}
```

## 2026-04-18 — v1.0 initial release

- Change: First release of the 37-field LanceDB schema and v1 extraction prompts.
- Rationale: Replaces the prior Open WebUI native RAG path and the old chunk schema. Adds the dual-field embedding architecture and structured metadata layer required by the query types in the spec.
- Migration: N/A — greenfield deployment.
- Affected chunks: None (empty corpus at release).
- Rollback: N/A for initial release.
```

- [ ] **Step 2: Commit**

```bash
git add docs/migrations/CHANGELOG.md
git commit -m "docs(migrations): initialize schema migration log with v1.0 entry"
```

---

### Task 8: Add pyyaml dependency

**Files:**
- Modify: `community-brain/pyproject.toml`

- [ ] **Step 1: Add pyyaml to dependencies**

Edit `community-brain/pyproject.toml`. In the `dependencies` list, add `"pyyaml>=6.0"` so the list reads:

```toml
dependencies = [
    "tiktoken>=0.7",
    "httpx>=0.27",
    "python-dotenv>=1.0",
    "click>=8.1",
    "tqdm>=4.66",
    "lancedb>=0.15",
    "ollama>=0.4",
    "openai>=1.50",
    "fastapi>=0.115",
    "uvicorn>=0.32",
    "pyyaml>=6.0",
]
```

- [ ] **Step 2: Install the updated dependencies**

Run: `cd community-brain && pip install -e ".[dev]"`
Expected: pyyaml gets installed without errors.

- [ ] **Step 3: Commit**

```bash
git add community-brain/pyproject.toml
git commit -m "deps(community-brain): add pyyaml for config loading"
```

---

## PHASE 2 — Python Implementation

### Task 9: Config loader module

**Files:**
- Create: `community-brain/src/community_brain/ingestion/__init__.py`
- Create: `community-brain/src/community_brain/ingestion/config_loader.py`
- Create: `community-brain/tests/test_config_loader.py`

- [ ] **Step 1: Create `ingestion/__init__.py` (empty package marker)**

```python
"""Ingestion pipeline for Community Brain v1.0 schema.

Parses prepared-transcript, extracted-signal, and community-post artifacts,
chunks them per the v1.0 rules, extracts structured metadata via LLM,
embeds with nomic-embed-text, and writes to LanceDB.
"""
```

- [ ] **Step 2: Write failing test for config loader**

Create `community-brain/tests/test_config_loader.py`:

```python
"""Tests for the YAML config loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from community_brain.ingestion.config_loader import (
    ChunkingConfig,
    ExtractionConfig,
    load_chunking_config,
    load_extraction_config,
)


def test_load_chunking_config_from_yaml(tmp_path: Path) -> None:
    config_file = tmp_path / "chunking.yaml"
    config_file.write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )

    config = load_chunking_config(config_file)

    assert isinstance(config, ChunkingConfig)
    assert config.schema_version == "1.0"
    assert config.transcript_segment_max_tokens == 1500
    assert config.post_max_tokens == 2500
    assert config.session_themes_input_max_tokens == 3000
    assert config.retry_attempts == 3
    assert config.retry_backoff_seconds == [2, 8, 32]
    assert config.inter_session_delay_seconds == 30


def test_load_extraction_config_from_yaml(tmp_path: Path) -> None:
    config_file = tmp_path / "extraction-config.yaml"
    config_file.write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: google/gemini-3.1-flash-lite-preview
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: google/gemini-3.1-flash-lite-preview
        """,
        encoding="utf-8",
    )

    config = load_extraction_config(config_file)

    assert isinstance(config, ExtractionConfig)
    assert config.session_themes_prompt_file == "session-themes-v1.md"
    assert config.session_themes_model == "google/gemini-3.1-flash-lite-preview"
    assert config.chunk_extraction_prompt_file == "chunk-extraction-v1.md"
    assert config.chunk_extraction_model == "google/gemini-3.1-flash-lite-preview"


def test_load_chunking_config_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_chunking_config(tmp_path / "does-not-exist.yaml")
```

- [ ] **Step 3: Run the test to confirm it fails**

Run: `cd community-brain && pytest tests/test_config_loader.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'community_brain.ingestion.config_loader'`

- [ ] **Step 4: Implement config_loader.py**

Create `community-brain/src/community_brain/ingestion/config_loader.py`:

```python
"""YAML config loader for the ingestion pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ChunkingConfig:
    """Chunking and retry tunables (from chunking.yaml)."""
    schema_version: str
    transcript_segment_max_tokens: int
    post_max_tokens: int
    session_themes_input_max_tokens: int
    retry_attempts: int
    retry_backoff_seconds: list[int]
    inter_session_delay_seconds: int


@dataclass(frozen=True)
class ExtractionConfig:
    """Active extraction prompt versions (from extraction-config.yaml)."""
    session_themes_prompt_file: str
    session_themes_model: str
    chunk_extraction_prompt_file: str
    chunk_extraction_model: str


def load_chunking_config(path: Path) -> ChunkingConfig:
    """Load chunking.yaml and return a typed config object."""
    if not path.exists():
        raise FileNotFoundError(f"Chunking config not found: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    chunking = data["chunking"]
    extraction = data["extraction"]
    return ChunkingConfig(
        schema_version=data["schema_version"],
        transcript_segment_max_tokens=chunking["transcript_segment_max_tokens"],
        post_max_tokens=chunking["post_max_tokens"],
        session_themes_input_max_tokens=chunking["session_themes_input_max_tokens"],
        retry_attempts=extraction["retry_attempts"],
        retry_backoff_seconds=list(extraction["retry_backoff_seconds"]),
        inter_session_delay_seconds=extraction["inter_session_delay_seconds"],
    )


def load_extraction_config(path: Path) -> ExtractionConfig:
    """Load extraction-config.yaml and return a typed config object."""
    if not path.exists():
        raise FileNotFoundError(f"Extraction config not found: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return ExtractionConfig(
        session_themes_prompt_file=data["session_themes"]["prompt_file"],
        session_themes_model=data["session_themes"]["model"],
        chunk_extraction_prompt_file=data["chunk_extraction"]["prompt_file"],
        chunk_extraction_model=data["chunk_extraction"]["model"],
    )
```

- [ ] **Step 5: Run the test to confirm it passes**

Run: `cd community-brain && pytest tests/test_config_loader.py -v`
Expected: 3 tests PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/ingestion/__init__.py \
        community-brain/src/community_brain/ingestion/config_loader.py \
        community-brain/tests/test_config_loader.py
git commit -m "feat(ingestion): add YAML config loader with typed configs"
```

---

### Task 10: Speaker and entity registries with atomic writes

**Files:**
- Create: `community-brain/src/community_brain/ingestion/registries.py`
- Create: `community-brain/tests/test_registries.py`

- [ ] **Step 1: Write failing tests**

Create `community-brain/tests/test_registries.py`:

```python
"""Tests for speaker/entity registry load and atomic append."""

from __future__ import annotations

from pathlib import Path

import yaml

from community_brain.ingestion.registries import (
    SpeakerRegistry,
    EntityRegistry,
    load_speaker_registry,
    load_entity_registry,
)


def _write_speaker_yaml(path: Path, aliases: dict[str, list[str]], pending: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"version": "2026-04-18", "aliases": aliases, "pending": pending}),
        encoding="utf-8",
    )


def _write_entity_yaml(path: Path, entities: dict, pending: list[str]) -> None:
    path.write_text(
        yaml.safe_dump({"version": "2026-04-18", "entities": entities, "pending": pending}),
        encoding="utf-8",
    )


def test_load_speaker_registry_resolves_aliases(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Alex Rojas": ["alexrojas", "Alex R"]}, [])

    reg = load_speaker_registry(path)

    assert reg.canonicalize("alexrojas") == "Alex Rojas"
    assert reg.canonicalize("Alex R") == "Alex Rojas"
    assert reg.canonicalize("Alex Rojas") == "Alex Rojas"


def test_load_speaker_registry_unknown_returns_none(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Alex Rojas": ["alexrojas"]}, [])
    reg = load_speaker_registry(path)
    assert reg.canonicalize("SomeoneElse") is None


def test_speaker_registry_append_pending_is_atomic(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    reg = load_speaker_registry(path)
    reg.append_pending(["NewPerson", "AnotherOne"])
    reg.flush(path)

    # Re-read from disk
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert data["pending"] == ["NewPerson", "AnotherOne"]
    # Existing data preserved
    assert data["aliases"]["Sam"] == ["sam"]


def test_speaker_registry_append_pending_dedupes(tmp_path: Path) -> None:
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {}, ["ExistingPending"])

    reg = load_speaker_registry(path)
    reg.append_pending(["ExistingPending", "NewOne", "NewOne"])
    reg.flush(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert sorted(data["pending"]) == ["ExistingPending", "NewOne"]


def test_entity_registry_canonicalize(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    _write_entity_yaml(
        path,
        {
            "LangChain": {
                "type": "framework",
                "category": "agent_framework",
                "aliases": ["Langchain", "langchain"],
            }
        },
        [],
    )

    reg = load_entity_registry(path)

    assert reg.canonicalize("langchain") == "LangChain"
    assert reg.canonicalize("LangChain") == "LangChain"
    assert reg.canonicalize("SomethingElse") is None


def test_entity_registry_flush_preserves_yaml_shape(tmp_path: Path) -> None:
    path = tmp_path / "entity-registry.yaml"
    _write_entity_yaml(
        path,
        {
            "Codex": {
                "type": "tool",
                "category": "coding_assistant",
                "aliases": ["codex"],
            }
        },
        [],
    )

    reg = load_entity_registry(path)
    reg.append_pending(["MystTool"])
    reg.flush(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert data["entities"]["Codex"]["type"] == "tool"
    assert data["pending"] == ["MystTool"]


def test_registry_flush_uses_atomic_rename(tmp_path: Path) -> None:
    """Writing should not leave a partial file if interrupted."""
    path = tmp_path / "speaker-aliases.yaml"
    _write_speaker_yaml(path, {"Sam": ["sam"]}, [])

    reg = load_speaker_registry(path)
    reg.append_pending(["X"])
    reg.flush(path)

    # After flush, no `.tmp` file should remain.
    tmp_files = list(tmp_path.glob("*.tmp"))
    assert tmp_files == []
```

- [ ] **Step 2: Run tests to confirm they fail**

Run: `cd community-brain && pytest tests/test_registries.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'community_brain.ingestion.registries'`

- [ ] **Step 3: Implement registries.py**

Create `community-brain/src/community_brain/ingestion/registries.py`:

```python
"""Speaker and entity registries with atomic YAML writes.

v1 constraint: single-writer. The pipeline orchestrator holds one registry
instance per session and flushes once at the end. Atomic rename guarantees
no partial writes survive a crash.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class SpeakerRegistry:
    """In-memory view of speaker-aliases.yaml with pending queue."""
    version: str
    aliases: dict[str, list[str]]  # canonical -> list of raw aliases
    pending: list[str]
    _lookup: dict[str, str] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        self._rebuild_lookup()

    def _rebuild_lookup(self) -> None:
        self._lookup = {}
        for canonical, raws in self.aliases.items():
            self._lookup[canonical] = canonical
            for raw in raws:
                self._lookup[raw] = canonical

    def canonicalize(self, raw: str) -> str | None:
        """Return the canonical name for a raw speaker mention, or None if unknown."""
        return self._lookup.get(raw)

    def append_pending(self, raw_names: list[str]) -> None:
        """Buffer unknown raw names into the pending queue (deduped in memory)."""
        existing = set(self.pending)
        for name in raw_names:
            if name and name not in existing:
                self.pending.append(name)
                existing.add(name)

    def flush(self, path: Path) -> None:
        """Atomically write the registry to disk.

        Writes to a temp file in the same directory, fsyncs, then renames.
        """
        tmp = path.with_suffix(path.suffix + ".tmp")
        payload = {
            "version": self.version,
            "aliases": self.aliases,
            "pending": self.pending,
        }
        tmp.write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        # fsync to ensure the bytes hit disk before we rename
        fd = os.open(str(tmp), os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        os.replace(tmp, path)


@dataclass
class EntityRegistry:
    """In-memory view of entity-registry.yaml with pending queue."""
    version: str
    entities: dict[str, dict]  # canonical -> {type, category, aliases}
    pending: list[str]
    _lookup: dict[str, str] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        self._rebuild_lookup()

    def _rebuild_lookup(self) -> None:
        self._lookup = {}
        for canonical, meta in self.entities.items():
            self._lookup[canonical.lower()] = canonical
            self._lookup[canonical] = canonical
            for alias in meta.get("aliases", []) or []:
                self._lookup[alias.lower()] = canonical
                self._lookup[alias] = canonical

    def canonicalize(self, raw: str) -> str | None:
        """Return the canonical entity name for a raw mention, or None."""
        if raw in self._lookup:
            return self._lookup[raw]
        return self._lookup.get(raw.lower())

    def append_pending(self, raw_names: list[str]) -> None:
        """Buffer unknown raw mentions into the pending queue (deduped)."""
        existing = set(self.pending)
        for name in raw_names:
            if name and name not in existing:
                self.pending.append(name)
                existing.add(name)

    def flush(self, path: Path) -> None:
        tmp = path.with_suffix(path.suffix + ".tmp")
        payload = {
            "version": self.version,
            "entities": self.entities,
            "pending": self.pending,
        }
        tmp.write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        fd = os.open(str(tmp), os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        os.replace(tmp, path)


def load_speaker_registry(path: Path) -> SpeakerRegistry:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return SpeakerRegistry(
        version=data.get("version", ""),
        aliases=data.get("aliases") or {},
        pending=list(data.get("pending") or []),
    )


def load_entity_registry(path: Path) -> EntityRegistry:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return EntityRegistry(
        version=data.get("version", ""),
        entities=data.get("entities") or {},
        pending=list(data.get("pending") or []),
    )
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_registries.py -v`
Expected: 7 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/registries.py \
        community-brain/tests/test_registries.py
git commit -m "feat(ingestion): add speaker/entity registries with atomic YAML writes"
```

---

### Task 11: Test fixtures for artifact parsing

**Files:**
- Create: `community-brain/tests/fixtures/prepared-transcript-sample.md`
- Create: `community-brain/tests/fixtures/extracted-signal-sample.md`
- Create: `community-brain/tests/fixtures/community-post-sample.md`

- [ ] **Step 1: Create prepared-transcript fixture**

```markdown
=== SESSION ===
date: 2026-03-10
duration_estimate: ~90 min
main_themes: [agent frameworks, production deployment, model selection]
===

<!--SEGMENT
topic: agent orchestration tools
speakers: Alex Rojas, Sam
keywords: LangChain, LangGraph, CrewAI, agent orchestration, tool calling, state machines
summary: Alex and Sam compare LangChain, LangGraph, and CrewAI for production agent deployments. Alex argues for LangGraph's state-machine model over CrewAI's role-based approach.
-->

[00:02:15] Alex Rojas: So I've been running [tool:LangGraph] in production for about three months now, and the state-machine model is way more predictable than [tool:CrewAI].
<Q>[00:02:45] Sam: Can you say more about the predictability angle?</Q>
<A>[00:03:01] Alex Rojas: ▶ With LangGraph you explicitly define the state transitions, so when something breaks you can trace back through the state history. CrewAI's role-based thing is nice for demos but painful to debug.</A>
[00:03:40] Alex Rojas: [link:https://langchain.com/docs/langgraph] is the best reference I've found.

<!--SEGMENT
topic: embedding model tradeoffs
speakers: Sam, Shakur
keywords: nomic-embed-text, text-embedding-3-large, embedding, local inference, cost
summary: Sam and Shakur discuss choosing between local nomic-embed-text and OpenAI's text-embedding-3-large. They agree local is right for BYO-AI but cloud quality is still better.
-->

[00:15:20] Sam: For our use case, [tool:nomic-embed-text] via Ollama is plenty. The quality gap with [tool:text-embedding-3-large] isn't worth $0.13 per million tokens.
[00:15:55] Shakur: Depends on the retrieval pattern. For conversational recall, nomic is fine. For precise technical queries, the OpenAI model catches nuances we lose locally.
```

- [ ] **Step 2: Create extracted-signal fixture**

```markdown
## tools

- LangGraph — Alex Rojas uses it for production agent deployments
- CrewAI — mentioned as an alternative to LangGraph
- nomic-embed-text — local embedding via Ollama
- text-embedding-3-large — cloud embedding alternative

## qa

**Q (Sam):** Can you say more about the predictability angle?
**A (Alex Rojas):** With LangGraph you explicitly define state transitions, making debugging easier than CrewAI's role-based approach.

## insights

- State-machine agent frameworks are easier to debug than role-based ones
- Local embeddings are sufficient for conversational recall; cloud wins on technical precision

## links

- https://langchain.com/docs/langgraph — LangGraph documentation
```

- [ ] **Step 3: Create community-post fixture**

```markdown
# Session notes — 2026-03-10

The main thread this week was a deep comparison of agent orchestration frameworks, led by Alex Rojas sharing his three months of production experience with LangGraph. Alex made a strong case for state-machine models over role-based approaches like CrewAI, specifically around debuggability — when things go wrong in production, being able to trace state transitions is worth more than the demo-friendly ergonomics.

Sam pushed on the predictability claim and got a concrete answer: explicit state transitions mean you can replay the history. This felt like a genuine insight the group landed on together rather than just Alex's opinion.

The second thread picked up on embedding models, with Sam and Shakur weighing local (nomic-embed-text via Ollama) against cloud (text-embedding-3-large). Sam's position: the quality gap doesn't justify the per-token cost for conversational recall. Shakur's counter: it depends on query precision needs. Both positions had merit and the group didn't force a resolution, which felt right.
```

- [ ] **Step 4: Commit**

```bash
git add community-brain/tests/fixtures/
git commit -m "test(ingestion): add sample fixtures for prepared-transcript, signal, post"
```

---

### Task 12: Parser — prepared-transcript segmentation

**Files:**
- Create: `community-brain/src/community_brain/ingestion/parser.py`
- Create: `community-brain/tests/test_ingestion_parser.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_ingestion_parser.py`:

```python
"""Tests for the three artifact parsers."""

from __future__ import annotations

from pathlib import Path

import pytest

from community_brain.ingestion.parser import (
    TranscriptSegment,
    SignalSection,
    CommunityPost,
    parse_prepared_transcript,
    parse_extracted_signal,
    parse_community_post,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_prepared_transcript_yields_segments() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    assert len(segments) == 2
    assert isinstance(segments[0], TranscriptSegment)


def test_prepared_transcript_first_segment_header() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    first = segments[0]
    assert first.topic == "agent orchestration tools"
    assert "Alex Rojas" in first.speakers
    assert "Sam" in first.speakers
    assert "LangChain" in first.keywords
    assert "LangGraph" in first.keywords
    assert first.summary.startswith("Alex and Sam compare")


def test_prepared_transcript_segment_body_preserves_tags() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    first_body = segments[0].body
    assert "[tool:LangGraph]" in first_body
    assert "<Q>" in first_body
    assert "<A>" in first_body
    assert "▶" in first_body


def test_prepared_transcript_empty_input() -> None:
    assert parse_prepared_transcript("") == []


def test_prepared_transcript_unresolved_speakers_extracted() -> None:
    text = """=== SESSION ===
date: 2026-04-01
===

<!--SEGMENT
topic: test
speakers: Unknown Person
keywords: test
summary: test segment
-->

[00:00:00] Unknown Person: something

=== UNRESOLVED SPEAKERS ===
- Unknown Person (appears 1 times, example: "something")
===
"""
    segments = parse_prepared_transcript(text)
    assert len(segments) == 1
    # Unresolved speakers are reported via a separate API or via parser return
    # For now, segment parsing should not fail in presence of unresolved block.


def test_parse_extracted_signal_yields_canonical_sections() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)

    slugs = [s.slug for s in sections]
    assert "tools" in slugs
    assert "qa" in slugs
    assert "insights" in slugs
    assert "links" in slugs
    # 'general' and 'decisions' not present in fixture — should not appear
    assert "general" not in slugs
    assert "decisions" not in slugs


def test_extracted_signal_section_contains_body() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)

    tools_section = next(s for s in sections if s.slug == "tools")
    assert "LangGraph" in tools_section.body


def test_extracted_signal_rejects_non_canonical_slug() -> None:
    text = """## Tooling

- Something
"""
    with pytest.raises(ValueError, match="non-canonical"):
        parse_extracted_signal(text)


def test_parse_community_post_returns_whole_document() -> None:
    text = (FIXTURES / "community-post-sample.md").read_text(encoding="utf-8")
    post = parse_community_post(text)

    assert isinstance(post, CommunityPost)
    assert post.body == text
    assert post.token_count > 0
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_ingestion_parser.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'community_brain.ingestion.parser'`

- [ ] **Step 3: Implement parser.py**

Create `community-brain/src/community_brain/ingestion/parser.py`:

```python
"""Parsers for the three ingestable artifact types.

- prepared-transcript.md → list[TranscriptSegment]
- extracted-signal.md    → list[SignalSection]
- community-post.md      → CommunityPost
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from community_brain.chunk_utils import count_tokens

CANONICAL_SIGNAL_SLUGS = frozenset({
    "tools", "qa", "insights", "links", "decisions", "general"
})


@dataclass(frozen=True)
class TranscriptSegment:
    """One <!--SEGMENT--> block from prepared-transcript.md."""
    topic: str
    speakers: list[str]
    keywords: list[str]
    summary: str
    body: str  # segment content after the header comment, before next SEGMENT or EOF


@dataclass(frozen=True)
class SignalSection:
    """One top-level section from extracted-signal.md."""
    slug: str  # canonical slug (e.g. "tools", "qa")
    body: str  # full section text including the heading


@dataclass(frozen=True)
class CommunityPost:
    """A community post, kept whole unless oversized."""
    body: str
    token_count: int


# Matches the opening <!--SEGMENT ... --> block.
_SEGMENT_HEADER_RE = re.compile(
    r"<!--SEGMENT\s*\n"
    r"topic:\s*(?P<topic>.*?)\n"
    r"speakers:\s*(?P<speakers>.*?)\n"
    r"keywords:\s*(?P<keywords>.*?)\n"
    r"summary:\s*(?P<summary>.*?)\n"
    r"-->",
    re.DOTALL,
)


def parse_prepared_transcript(text: str) -> list[TranscriptSegment]:
    """Parse a prepared transcript into segments.

    Splits on `<!--SEGMENT ... -->` headers. Content between a header and the
    next header (or end-of-file, or a closing === marker) becomes the segment body.
    """
    if not text.strip():
        return []

    segments: list[TranscriptSegment] = []

    # Find all header positions.
    matches = list(_SEGMENT_HEADER_RE.finditer(text))
    if not matches:
        return []

    for i, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        body = text[body_start:body_end]
        # Strip trailing === blocks (UNRESOLVED SPEAKERS section)
        end_marker = body.find("=== UNRESOLVED SPEAKERS ===")
        if end_marker != -1:
            body = body[:end_marker]

        segments.append(TranscriptSegment(
            topic=match.group("topic").strip(),
            speakers=_split_csv(match.group("speakers")),
            keywords=_split_csv(match.group("keywords")),
            summary=match.group("summary").strip(),
            body=body.strip(),
        ))

    return segments


def parse_extracted_signal(text: str) -> list[SignalSection]:
    """Parse extracted-signal.md into canonical sections.

    Raises ValueError if a non-canonical heading is encountered.
    """
    sections: list[SignalSection] = []

    # Split on `## ` at start of line
    parts = re.split(r"(?m)^##\s+", text)
    # parts[0] is any preamble before the first heading; ignore
    for part in parts[1:]:
        # First token of the section is the heading slug
        lines = part.splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        slug = heading.lower().split()[0] if heading else ""
        if slug not in CANONICAL_SIGNAL_SLUGS:
            raise ValueError(
                f"non-canonical signal section heading: {heading!r}. "
                f"Allowed: {sorted(CANONICAL_SIGNAL_SLUGS)}"
            )
        body = f"## {heading}\n" + "\n".join(lines[1:])
        sections.append(SignalSection(slug=slug, body=body.strip()))

    return sections


def parse_community_post(text: str) -> CommunityPost:
    """Parse community-post.md into a single whole-document record."""
    return CommunityPost(body=text, token_count=count_tokens(text))


def _split_csv(raw: str) -> list[str]:
    """Split a comma-separated header value, stripping and ignoring empty parts."""
    return [part.strip() for part in raw.split(",") if part.strip()]
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_ingestion_parser.py -v`
Expected: 9 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/parser.py \
        community-brain/tests/test_ingestion_parser.py
git commit -m "feat(ingestion): parse prepared-transcript, extracted-signal, community-post"
```

---

### Task 13: LanceDB schema definition (v1.0, 37 fields)

**Files:**
- Create: `community-brain/src/community_brain/ingestion/schema.py`
- Create: `community-brain/tests/test_ingestion_schema.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_ingestion_schema.py`:

```python
"""Tests for the v1.0 LanceDB chunk schema."""

from __future__ import annotations

import datetime as dt

from community_brain.ingestion.schema import Chunk, SCHEMA_VERSION


def test_schema_version_is_1_0() -> None:
    assert SCHEMA_VERSION == "1.0"


def test_chunk_construction_with_all_fields() -> None:
    chunk = Chunk(
        schema_version="1.0",
        chunk_id="2026-03-10:transcript:001",
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Agent frameworks comparison",
        content_type="prepared_transcript",
        source_file="output/2026-03-10/prepared-transcript.md",
        chunk_index=1,
        total_chunks_in_source=2,
        speakers_spoke=["Alex Rojas", "Sam"],
        speakers_mentioned=["Alex Rojas", "Sam"],
        entities=["LangGraph"],
        keywords=["agent orchestration"],
        topic_label="agent orchestration tools",
        session_themes=["agent frameworks", "production deployment"],
        speech_acts=["comparison", "recommendation"],
        stance="positive",
        certainty="asserted",
        chunk_local_markers=["emphasized"],
        corpus_derived_markers=[],
        corpus_markers_computed_at=None,
        has_question=True,
        has_answer=True,
        has_unresolved_question=False,
        has_insight=True,
        decisions=None,
        action_items=None,
        external_refs=["https://langchain.com/docs/langgraph"],
        references_prior=False,
        extraction_model="google/gemini-3.1-flash-lite-preview",
        extraction_prompt_version="chunk-extraction-v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime(2026, 3, 10, 14, 22, 11, tzinfo=dt.timezone.utc),
        embed_text="...",
        full_text="...",
        embedding=[0.0] * 768,
    )
    assert chunk.chunk_id == "2026-03-10:transcript:001"
    assert chunk.extraction_status == "success"


def test_chunk_to_arrow_dict_roundtrip() -> None:
    """Chunk.to_arrow_dict returns a dict suitable for LanceDB insertion."""
    chunk = Chunk(
        schema_version="1.0",
        chunk_id="2026-03-10:post:main",
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title=None,
        content_type="community_post",
        source_file="output/2026-03-10/community-post.md",
        chunk_index=0,
        total_chunks_in_source=1,
        speakers_spoke=None,
        speakers_mentioned=["Alex Rojas", "Sam"],
        entities=[],
        keywords=None,
        topic_label="session_narrative",
        session_themes=["agent frameworks"],
        speech_acts=[],
        stance=None,
        certainty="asserted",
        chunk_local_markers=[],
        corpus_derived_markers=[],
        corpus_markers_computed_at=None,
        has_question=False,
        has_answer=False,
        has_unresolved_question=False,
        has_insight=False,
        decisions=None,
        action_items=None,
        external_refs=None,
        references_prior=False,
        extraction_model="google/gemini-3.1-flash-lite-preview",
        extraction_prompt_version="chunk-extraction-v1",
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime(2026, 3, 10, 15, 0, 0, tzinfo=dt.timezone.utc),
        embed_text="text",
        full_text="text",
        embedding=[0.0] * 768,
    )

    d = chunk.to_arrow_dict()
    assert d["chunk_id"] == "2026-03-10:post:main"
    assert d["content_type"] == "community_post"
    # Null list-valued fields become empty lists in the arrow representation
    # (LanceDB/Arrow doesn't handle null lists well; we use empty lists)
    assert d["speakers_spoke"] == []
    assert d["keywords"] == []
```

- [ ] **Step 2: Run the test to confirm it fails**

Run: `cd community-brain && pytest tests/test_ingestion_schema.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement schema.py**

Create `community-brain/src/community_brain/ingestion/schema.py`:

```python
"""LanceDB schema v1.0 for the Community Brain ingestion pipeline.

37 fields, organized into ground-truth, derived-metadata, and provenance groups.
See docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md §6
for the authoritative schema definition.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, asdict, field
from typing import Literal

SCHEMA_VERSION = "1.0"

ContentType = Literal["prepared_transcript", "extracted_signal", "community_post"]
Stance = Literal["positive", "negative", "neutral", "mixed"]
Certainty = Literal["asserted", "hedged", "speculative"]
ExtractionStatus = Literal["success", "failed"]


@dataclass
class Chunk:
    """A single row in the LanceDB chunks table (v1.0 schema, 37 fields)."""

    # --- Identity & positional (9) ---
    schema_version: str
    chunk_id: str
    session_id: str
    session_date: str  # YYYY-MM-DD
    session_title: str | None
    content_type: ContentType
    source_file: str
    chunk_index: int
    total_chunks_in_source: int

    # --- Attribution (2) ---
    speakers_spoke: list[str] | None
    speakers_mentioned: list[str] | None

    # --- Semantic tags, chunk-level (3) ---
    entities: list[str]
    keywords: list[str] | None
    topic_label: str | None

    # --- Session-level context (1) ---
    session_themes: list[str]

    # --- Interpretation (LLM-derived, chunk-local) (6) ---
    speech_acts: list[str]
    stance: Stance | None
    certainty: Certainty
    chunk_local_markers: list[str]
    corpus_derived_markers: list[str]
    corpus_markers_computed_at: dt.datetime | None

    # --- Deterministic flags (4) ---
    has_question: bool
    has_answer: bool
    has_unresolved_question: bool
    has_insight: bool

    # --- Structured extracts (4) ---
    decisions: list[str] | None
    action_items: list[str] | None
    external_refs: list[str] | None
    references_prior: bool

    # --- Provenance (5) ---
    extraction_model: str
    extraction_prompt_version: str
    extraction_status: ExtractionStatus
    extraction_error: str | None
    extracted_at: dt.datetime

    # --- Content & embedding (3) ---
    embed_text: str
    full_text: str
    embedding: list[float]

    def to_arrow_dict(self) -> dict:
        """Flatten to a dict suitable for pyarrow / LanceDB insertion.

        LanceDB / Arrow doesn't nicely support null for list columns,
        so we normalize null list-valued fields to empty lists on write.
        """
        d = asdict(self)
        for list_field in (
            "speakers_spoke",
            "speakers_mentioned",
            "keywords",
            "decisions",
            "action_items",
            "external_refs",
        ):
            if d[list_field] is None:
                d[list_field] = []
        # Datetimes: ISO-format strings for portability
        if d["corpus_markers_computed_at"] is not None:
            d["corpus_markers_computed_at"] = d["corpus_markers_computed_at"].isoformat()
        d["extracted_at"] = d["extracted_at"].isoformat()
        return d


def lancedb_table_schema() -> dict:
    """Return a JSON-schema-ish description of the table shape.

    Used by the pipeline for LanceDB table creation / verification.
    Actual table creation uses pyarrow schema derived from this.
    """
    return {
        "schema_version": "string",
        "chunk_id": "string",
        "session_id": "string",
        "session_date": "string",
        "session_title": "string|null",
        "content_type": "string",
        "source_file": "string",
        "chunk_index": "int",
        "total_chunks_in_source": "int",
        "speakers_spoke": "list[string]",
        "speakers_mentioned": "list[string]",
        "entities": "list[string]",
        "keywords": "list[string]",
        "topic_label": "string|null",
        "session_themes": "list[string]",
        "speech_acts": "list[string]",
        "stance": "string|null",
        "certainty": "string",
        "chunk_local_markers": "list[string]",
        "corpus_derived_markers": "list[string]",
        "corpus_markers_computed_at": "string|null",
        "has_question": "bool",
        "has_answer": "bool",
        "has_unresolved_question": "bool",
        "has_insight": "bool",
        "decisions": "list[string]",
        "action_items": "list[string]",
        "external_refs": "list[string]",
        "references_prior": "bool",
        "extraction_model": "string",
        "extraction_prompt_version": "string",
        "extraction_status": "string",
        "extraction_error": "string|null",
        "extracted_at": "string",
        "embed_text": "string",
        "full_text": "string",
        "embedding": "list[float]",
    }
```

- [ ] **Step 4: Run the tests**

Run: `cd community-brain && pytest tests/test_ingestion_schema.py -v`
Expected: 3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/schema.py \
        community-brain/tests/test_ingestion_schema.py
git commit -m "feat(ingestion): add v1.0 LanceDB schema with 37 fields"
```

---

### Task 14: Chunker — produce Chunk records from parsed artifacts

**Files:**
- Create: `community-brain/src/community_brain/ingestion/chunker.py`
- Create: `community-brain/tests/test_ingestion_chunker.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_ingestion_chunker.py`:

```python
"""Tests for the chunker that composes Chunk records from parsed artifacts."""

from __future__ import annotations

from pathlib import Path

from community_brain.ingestion.parser import (
    parse_prepared_transcript,
    parse_extracted_signal,
    parse_community_post,
)
from community_brain.ingestion.chunker import (
    chunk_prepared_transcript,
    chunk_extracted_signal,
    chunk_community_post,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_chunk_prepared_transcript_creates_one_chunk_per_segment() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)

    chunks = chunk_prepared_transcript(
        segments,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Agent frameworks comparison",
        source_file="output/2026-03-10/prepared-transcript.md",
        segment_max_tokens=1500,
    )

    assert len(chunks) == 2
    assert chunks[0].chunk_id == "2026-03-10:transcript:001"
    assert chunks[1].chunk_id == "2026-03-10:transcript:002"
    assert chunks[0].content_type == "prepared_transcript"
    assert chunks[0].total_chunks_in_source == 2


def test_chunk_prepared_transcript_embed_text_uses_segment_header() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10",
        "Agent frameworks comparison",
        "output/2026-03-10/prepared-transcript.md",
        1500,
    )
    first = chunks[0]
    assert "agent orchestration tools" in first.embed_text  # topic
    assert "LangChain" in first.embed_text  # keywords present in embed input
    assert first.topic_label == "agent orchestration tools"


def test_chunk_prepared_transcript_speakers_spoke_from_body() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10", "t", "t", 1500,
    )
    assert "Alex Rojas" in chunks[0].speakers_spoke
    assert "Sam" in chunks[0].speakers_spoke


def test_chunk_prepared_transcript_flags_qa_and_insight() -> None:
    text = (FIXTURES / "prepared-transcript-sample.md").read_text(encoding="utf-8")
    segments = parse_prepared_transcript(text)
    chunks = chunk_prepared_transcript(
        segments, "2026-03-10", "2026-03-10", "t", "t", 1500,
    )
    # First segment has <Q>, <A>, and ▶
    assert chunks[0].has_question is True
    assert chunks[0].has_answer is True
    assert chunks[0].has_unresolved_question is False
    assert chunks[0].has_insight is True


def test_chunk_extracted_signal_one_chunk_per_section() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(
        sections,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        source_file="output/2026-03-10/extracted-signal.md",
    )

    # Fixture has tools, qa, insights, links
    assert len(chunks) == 4
    slugs = sorted(c.chunk_id.split(":")[-1] for c in chunks)
    assert slugs == ["insights", "links", "qa", "tools"]


def test_chunk_extracted_signal_topic_label_matches_slug() -> None:
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(sections, "2026-03-10", "2026-03-10", "t", "t")

    for chunk in chunks:
        slug = chunk.chunk_id.split(":")[-1]
        assert chunk.topic_label == slug
        assert chunk.content_type == "extracted_signal"


def test_chunk_extracted_signal_embed_text_equals_full_text() -> None:
    """Per dual-field rule: signal chunks embed and return the same text."""
    text = (FIXTURES / "extracted-signal-sample.md").read_text(encoding="utf-8")
    sections = parse_extracted_signal(text)
    chunks = chunk_extracted_signal(sections, "2026-03-10", "2026-03-10", "t", "t")
    for chunk in chunks:
        assert chunk.embed_text == chunk.full_text


def test_chunk_community_post_single_chunk_whole_doc() -> None:
    text = (FIXTURES / "community-post-sample.md").read_text(encoding="utf-8")
    post = parse_community_post(text)
    chunks = chunk_community_post(
        post,
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        source_file="output/2026-03-10/community-post.md",
        post_max_tokens=2500,
    )
    assert len(chunks) == 1
    assert chunks[0].chunk_id == "2026-03-10:post:main"
    assert chunks[0].topic_label == "session_narrative"
    assert chunks[0].embed_text == chunks[0].full_text
    assert chunks[0].full_text == text
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_ingestion_chunker.py -v`
Expected: FAIL (module does not exist).

- [ ] **Step 3: Implement chunker.py**

Create `community-brain/src/community_brain/ingestion/chunker.py`:

```python
"""Compose Chunk records from parsed artifacts.

Each function here produces partially-filled Chunk instances. The extractor
(Task 15) fills in LLM-derived fields later. Provenance and embedding are
populated by the pipeline orchestrator (Task 18).
"""

from __future__ import annotations

import datetime as dt
import re

from community_brain.chunk_utils import count_tokens
from community_brain.ingestion.parser import (
    TranscriptSegment,
    SignalSection,
    CommunityPost,
)
from community_brain.ingestion.schema import Chunk, SCHEMA_VERSION


_TRANSCRIPT_LINE_RE = re.compile(r"^\[\d{2}:\d{2}:\d{2}\]\s+(.+?):\s+", re.MULTILINE)


def _base_chunk(
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
    content_type: str,
    chunk_id: str,
    chunk_index: int,
    total_chunks_in_source: int,
    embed_text: str,
    full_text: str,
    topic_label: str | None,
    speakers_spoke: list[str] | None,
    keywords: list[str] | None,
) -> Chunk:
    """Construct a Chunk with deterministic-only fields populated.

    LLM-derived fields default to empty / null; extractor fills them later.
    Embedding defaults to empty list; pipeline fills it.
    """
    return Chunk(
        schema_version=SCHEMA_VERSION,
        chunk_id=chunk_id,
        session_id=session_id,
        session_date=session_date,
        session_title=session_title,
        content_type=content_type,  # type: ignore[arg-type]
        source_file=source_file,
        chunk_index=chunk_index,
        total_chunks_in_source=total_chunks_in_source,
        speakers_spoke=speakers_spoke,
        speakers_mentioned=None,   # filled by extractor
        entities=[],               # filled by extractor
        keywords=keywords,
        topic_label=topic_label,
        session_themes=[],         # filled by pipeline (session-level)
        speech_acts=[],            # filled by extractor
        stance=None,               # filled by extractor
        certainty="asserted",      # default; extractor overrides
        chunk_local_markers=[],    # filled by extractor
        corpus_derived_markers=[],
        corpus_markers_computed_at=None,
        has_question=_scan_tag(full_text, "<Q>"),
        has_answer=_scan_tag(full_text, "<A>"),
        has_unresolved_question=_has_unresolved_q(full_text),
        has_insight="▶" in full_text,
        decisions=None,
        action_items=None,
        external_refs=None,
        references_prior=False,
        extraction_model="",                   # filled by pipeline
        extraction_prompt_version="",          # filled by pipeline
        extraction_status="success",
        extraction_error=None,
        extracted_at=dt.datetime.now(dt.timezone.utc),  # overridden by pipeline
        embed_text=embed_text,
        full_text=full_text,
        embedding=[],
    )


def _scan_tag(text: str, tag: str) -> bool:
    return tag in text


def _has_unresolved_q(text: str) -> bool:
    """True if <Q> appears without a matching <A> within the same chunk body."""
    q_count = text.count("<Q>")
    a_count = text.count("<A>")
    return q_count > a_count


def _extract_speakers_from_body(body: str) -> list[str]:
    """Pull distinct speaker labels from `[HH:MM:SS] Speaker: ...` lines."""
    speakers = sorted(set(_TRANSCRIPT_LINE_RE.findall(body)))
    return speakers


def _segment_embed_text(segment: TranscriptSegment) -> str:
    """Build the text that gets embedded for a transcript segment.

    Per dual-field design: embed the topical header fields, return the body.
    """
    return (
        f"topic: {segment.topic}\n"
        f"summary: {segment.summary}\n"
        f"keywords: {', '.join(segment.keywords)}"
    )


def chunk_prepared_transcript(
    segments: list[TranscriptSegment],
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
    segment_max_tokens: int,
) -> list[Chunk]:
    """Produce one Chunk per transcript segment.

    Segments longer than segment_max_tokens get sub-chunked via sliding window,
    with each sub-chunk retaining the full segment header as its embed_text.
    """
    chunks: list[Chunk] = []
    total_position = 0

    # First pass: count total to populate total_chunks_in_source.
    sub_segment_plans: list[tuple[TranscriptSegment, list[str]]] = []
    for segment in segments:
        body_tokens = count_tokens(segment.body)
        if body_tokens <= segment_max_tokens:
            sub_segment_plans.append((segment, [segment.body]))
        else:
            sub_segment_plans.append((segment, _slide_window_split(segment.body, segment_max_tokens)))

    total_chunks = sum(len(plan[1]) for plan in sub_segment_plans)

    for segment, bodies in sub_segment_plans:
        embed_text = _segment_embed_text(segment)
        for body in bodies:
            total_position += 1
            chunk_id = f"{session_id}:transcript:{total_position:03d}"
            chunks.append(_base_chunk(
                session_id=session_id,
                session_date=session_date,
                session_title=session_title,
                source_file=source_file,
                content_type="prepared_transcript",
                chunk_id=chunk_id,
                chunk_index=total_position,
                total_chunks_in_source=total_chunks,
                embed_text=embed_text,
                full_text=body,
                topic_label=segment.topic,
                speakers_spoke=_extract_speakers_from_body(body) or segment.speakers,
                keywords=segment.keywords,
            ))

    return chunks


def _slide_window_split(text: str, max_tokens: int, overlap_tokens: int = 50) -> list[str]:
    """Naive sliding-window split by paragraph when a segment is too large."""
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    out: list[str] = []
    current: list[str] = []
    current_tokens = 0
    for para in paragraphs:
        t = count_tokens(para)
        if current_tokens + t > max_tokens and current:
            out.append("\n\n".join(current))
            # Apply overlap: keep last paragraph if possible
            if current and count_tokens(current[-1]) <= overlap_tokens:
                current = [current[-1]]
                current_tokens = count_tokens(current[-1])
            else:
                current = []
                current_tokens = 0
        current.append(para)
        current_tokens += t
    if current:
        out.append("\n\n".join(current))
    return out or [text]


def chunk_extracted_signal(
    sections: list[SignalSection],
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
) -> list[Chunk]:
    """One Chunk per canonical signal section. embed_text == full_text."""
    total = len(sections)
    chunks: list[Chunk] = []
    for i, section in enumerate(sections, start=1):
        chunk_id = f"{session_id}:signal:{section.slug}"
        chunks.append(_base_chunk(
            session_id=session_id,
            session_date=session_date,
            session_title=session_title,
            source_file=source_file,
            content_type="extracted_signal",
            chunk_id=chunk_id,
            chunk_index=i,
            total_chunks_in_source=total,
            embed_text=section.body,
            full_text=section.body,
            topic_label=section.slug,
            speakers_spoke=None,  # signal is already-summarized, no speaker
            keywords=None,
        ))
    return chunks


def chunk_community_post(
    post: CommunityPost,
    session_id: str,
    session_date: str,
    session_title: str | None,
    source_file: str,
    post_max_tokens: int,
) -> list[Chunk]:
    """Community post as one chunk if small enough, else sliding-window split."""
    if post.token_count <= post_max_tokens:
        return [_base_chunk(
            session_id=session_id,
            session_date=session_date,
            session_title=session_title,
            source_file=source_file,
            content_type="community_post",
            chunk_id=f"{session_id}:post:main",
            chunk_index=1,
            total_chunks_in_source=1,
            embed_text=post.body,
            full_text=post.body,
            topic_label="session_narrative",
            speakers_spoke=None,
            keywords=None,
        )]

    # Rare fallback: sliding window
    parts = _slide_window_split(post.body, post_max_tokens)
    total = len(parts)
    return [
        _base_chunk(
            session_id=session_id,
            session_date=session_date,
            session_title=session_title,
            source_file=source_file,
            content_type="community_post",
            chunk_id=f"{session_id}:post:{i:03d}",
            chunk_index=i,
            total_chunks_in_source=total,
            embed_text=part,
            full_text=part,
            topic_label="session_narrative",
            speakers_spoke=None,
            keywords=None,
        )
        for i, part in enumerate(parts, start=1)
    ]
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_ingestion_chunker.py -v`
Expected: 8 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/chunker.py \
        community-brain/tests/test_ingestion_chunker.py
git commit -m "feat(ingestion): chunk parsed artifacts into v1.0 schema records"
```

---

### Task 15: Extractor — Stage C chunk-level LLM extraction

**Files:**
- Create: `community-brain/src/community_brain/ingestion/extractor.py`
- Create: `community-brain/tests/test_ingestion_extractor.py`

- [ ] **Step 1: Write failing tests (with LLM mocked)**

Create `community-brain/tests/test_ingestion_extractor.py`:

```python
"""Tests for Stage C chunk extraction (LLM mocked)."""

from __future__ import annotations

import json
from unittest.mock import patch

from community_brain.ingestion.extractor import (
    ExtractionResult,
    extract_chunk_metadata,
)


def _mock_llm_response(payload: dict) -> str:
    return json.dumps(payload)


def test_extract_chunk_metadata_success() -> None:
    payload = {
        "entities": ["LangGraph"],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": ["comparison", "recommendation"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": [],
        "external_refs": ["https://langchain.com/docs/langgraph"],
        "references_prior": False,
    }

    with patch("community_brain.ingestion.extractor._call_llm", return_value=_mock_llm_response(payload)):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=["LangGraph"],
            speaker_alias_names=["Alex Rojas", "Sam"],
            model="google/gemini-3.1-flash-lite-preview",
            prompt_template="...prompt...",
        )

    assert isinstance(result, ExtractionResult)
    assert result.status == "success"
    assert result.entities == ["LangGraph"]
    assert "comparison" in result.speech_acts
    assert result.stance == "positive"
    assert result.certainty == "asserted"
    assert result.error is None


def test_extract_chunk_metadata_invalid_json_marks_failed() -> None:
    with patch("community_brain.ingestion.extractor._call_llm", return_value="not json"):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )

    assert result.status == "failed"
    assert "json" in (result.error or "").lower()


def test_extract_chunk_metadata_llm_exception_marks_failed() -> None:
    def _raise(*_a, **_k):
        raise RuntimeError("llm unavailable")

    with patch("community_brain.ingestion.extractor._call_llm", side_effect=_raise):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=[],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )

    assert result.status == "failed"
    assert "llm unavailable" in (result.error or "")


def test_extract_chunk_metadata_missing_fields_filled_with_defaults() -> None:
    """LLM returns partial JSON; extractor fills missing fields safely."""
    payload = {"entities": ["X"]}  # missing almost everything
    with patch("community_brain.ingestion.extractor._call_llm", return_value=_mock_llm_response(payload)):
        result = extract_chunk_metadata(
            chunk_text="...",
            entity_registry_names=["X"],
            speaker_alias_names=[],
            model="m",
            prompt_template="p",
        )
    # Missing fields default — but because required fields missing, we still mark success
    # only if parsed cleanly. Partial fields should be filled with safe defaults.
    assert result.status == "success"
    assert result.entities == ["X"]
    assert result.speech_acts == []
    assert result.stance is None
    assert result.certainty == "asserted"
    assert result.chunk_local_markers == []
```

- [ ] **Step 2: Run tests to confirm they fail**

Run: `cd community-brain && pytest tests/test_ingestion_extractor.py -v`
Expected: FAIL (module does not exist).

- [ ] **Step 3: Implement extractor.py**

Create `community-brain/src/community_brain/ingestion/extractor.py`:

```python
"""Stage C: per-chunk LLM metadata extraction.

Takes a chunk's full_text plus the current entity registry and speaker aliases,
calls the extraction LLM, parses JSON, and returns structured metadata.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Literal

from community_brain.llm import call_openrouter  # see Task 16; we add this wrapper

logger = logging.getLogger(__name__)


@dataclass
class ExtractionResult:
    """Parsed output of Stage C extraction for a single chunk."""
    status: Literal["success", "failed"]
    entities: list[str]
    new_entities_seen: list[str]
    new_speakers_seen: list[str]
    speech_acts: list[str]
    stance: str | None
    certainty: str
    chunk_local_markers: list[str]
    decisions: list[str]
    action_items: list[str]
    external_refs: list[str]
    references_prior: bool
    error: str | None = None


def _call_llm(model: str, prompt: str) -> str:
    """Indirection for testing. Wraps the OpenRouter client."""
    return call_openrouter(model=model, prompt=prompt)


def extract_chunk_metadata(
    chunk_text: str,
    entity_registry_names: list[str],
    speaker_alias_names: list[str],
    model: str,
    prompt_template: str,
) -> ExtractionResult:
    """Run Stage C extraction on one chunk.

    Failures (network, invalid JSON) are returned as status="failed" rather
    than raised — the pipeline continues ingestion and can retry later.
    """
    prompt = (
        f"{prompt_template}\n\n"
        f"ENTITY_REGISTRY:\n{json.dumps(entity_registry_names)}\n\n"
        f"SPEAKER_ALIASES:\n{json.dumps(speaker_alias_names)}\n\n"
        f"CHUNK_TEXT:\n{chunk_text}\n"
    )

    try:
        raw = _call_llm(model=model, prompt=prompt)
    except Exception as exc:  # pragma: no cover - wrapped intentionally
        logger.warning("LLM call failed: %s", exc)
        return _failure(str(exc))

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return _failure(f"invalid JSON from LLM: {exc}")

    return ExtractionResult(
        status="success",
        entities=list(data.get("entities") or []),
        new_entities_seen=list(data.get("new_entities_seen") or []),
        new_speakers_seen=list(data.get("new_speakers_seen") or []),
        speech_acts=list(data.get("speech_acts") or []),
        stance=data.get("stance"),
        certainty=data.get("certainty") or "asserted",
        chunk_local_markers=list(data.get("chunk_local_markers") or []),
        decisions=list(data.get("decisions") or []),
        action_items=list(data.get("action_items") or []),
        external_refs=list(data.get("external_refs") or []),
        references_prior=bool(data.get("references_prior", False)),
        error=None,
    )


def _failure(msg: str) -> ExtractionResult:
    return ExtractionResult(
        status="failed",
        entities=[],
        new_entities_seen=[],
        new_speakers_seen=[],
        speech_acts=[],
        stance=None,
        certainty="asserted",
        chunk_local_markers=[],
        decisions=[],
        action_items=[],
        external_refs=[],
        references_prior=False,
        error=msg,
    )
```

- [ ] **Step 4: Add the thin OpenRouter call wrapper**

Open `community-brain/src/community_brain/llm.py` and check if a simple `call_openrouter(model, prompt)` helper exists. If not, append this function at the bottom of the file:

```python
def call_openrouter(model: str, prompt: str, temperature: float = 0.0) -> str:
    """Simple chat completion wrapper: single user message, returns content.

    Raises LLMError on failure.
    """
    api_key = _get_api_key()
    if not api_key:
        raise LLMError("OPENROUTER_API_KEY not set")

    resp = httpx.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60.0,
    )
    if resp.status_code != 200:
        raise LLMError(f"OpenRouter returned {resp.status_code}: {resp.text[:200]}")
    data = resp.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise LLMError(f"unexpected OpenRouter response shape: {exc}")
```

Only add this if it does not already exist. If a similar function exists under a different name, adjust the import in `extractor.py` accordingly.

- [ ] **Step 5: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_ingestion_extractor.py -v`
Expected: 4 tests PASS.

- [ ] **Step 6: Commit**

```bash
git add community-brain/src/community_brain/ingestion/extractor.py \
        community-brain/src/community_brain/llm.py \
        community-brain/tests/test_ingestion_extractor.py
git commit -m "feat(ingestion): add Stage C chunk metadata extraction with failure-tolerant parsing"
```

---

### Task 16: Session-level Stage B extractor

**Files:**
- Create: `community-brain/src/community_brain/ingestion/session_extractor.py`
- Create: `community-brain/tests/test_ingestion_session_extractor.py`

- [ ] **Step 1: Write failing tests**

Create `community-brain/tests/test_ingestion_session_extractor.py`:

```python
"""Tests for Stage B session-level theme extraction and deterministic input selection."""

from __future__ import annotations

import json
from unittest.mock import patch

from community_brain.ingestion.parser import TranscriptSegment, CommunityPost, SignalSection
from community_brain.ingestion.session_extractor import (
    SessionThemesResult,
    select_session_input,
    extract_session_themes,
)


def test_select_session_input_prefers_community_post_when_small() -> None:
    post = CommunityPost(body="short post", token_count=100)
    segments = [
        TranscriptSegment(topic="x", speakers=[], keywords=[], summary="s", body="body")
    ]
    sections = [SignalSection(slug="tools", body="## tools\n- X")]

    source, text = select_session_input(
        community_post=post,
        transcript_segments=segments,
        signal_sections=sections,
        max_tokens=3000,
    )
    assert source == "community_post"
    assert text == "short post"


def test_select_session_input_falls_back_to_segment_headers_when_post_too_large() -> None:
    post = CommunityPost(body="huge post", token_count=5000)
    segments = [
        TranscriptSegment(topic="t1", speakers=["A"], keywords=["k1"], summary="s1", body="b"),
        TranscriptSegment(topic="t2", speakers=["B"], keywords=["k2"], summary="s2", body="b"),
    ]
    sections = []

    source, text = select_session_input(
        community_post=post,
        transcript_segments=segments,
        signal_sections=sections,
        max_tokens=3000,
    )
    assert source == "transcript_headers"
    assert "t1" in text
    assert "t2" in text
    assert "s1" in text


def test_select_session_input_falls_back_to_signal_when_no_post_no_segments() -> None:
    sections = [SignalSection(slug="tools", body="## tools\n- X")]
    source, text = select_session_input(
        community_post=None,
        transcript_segments=[],
        signal_sections=sections,
        max_tokens=3000,
    )
    assert source == "signal"
    assert "tools" in text


def test_select_session_input_returns_none_when_no_input_available() -> None:
    source, text = select_session_input(
        community_post=None,
        transcript_segments=[],
        signal_sections=[],
        max_tokens=3000,
    )
    assert source is None
    assert text == ""


def test_extract_session_themes_success() -> None:
    payload = {"themes": ["agent frameworks", "production deployment", "model selection"]}
    with patch(
        "community_brain.ingestion.session_extractor._call_llm",
        return_value=json.dumps(payload),
    ):
        result = extract_session_themes(
            input_text="...",
            model="m",
            prompt_template="p",
        )
    assert isinstance(result, SessionThemesResult)
    assert result.themes == ["agent frameworks", "production deployment", "model selection"]
    assert result.status == "success"


def test_extract_session_themes_invalid_json_returns_empty_themes() -> None:
    with patch(
        "community_brain.ingestion.session_extractor._call_llm",
        return_value="garbage",
    ):
        result = extract_session_themes(input_text="x", model="m", prompt_template="p")
    assert result.status == "failed"
    assert result.themes == []
```

- [ ] **Step 2: Run tests to confirm they fail**

Run: `cd community-brain && pytest tests/test_ingestion_session_extractor.py -v`
Expected: FAIL (module does not exist).

- [ ] **Step 3: Implement session_extractor.py**

Create `community-brain/src/community_brain/ingestion/session_extractor.py`:

```python
"""Stage B: session-level theme extraction.

Deterministic input priority (per spec §5.3):
  1. community_post if present AND within max_tokens
  2. ELSE concatenation of transcript segment headers (not bodies)
  3. ELSE extracted_signal full text
  4. ELSE soft-fail with empty themes (log warning; caller continues)
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Literal

from community_brain.ingestion.parser import (
    CommunityPost,
    SignalSection,
    TranscriptSegment,
)
from community_brain.llm import call_openrouter

logger = logging.getLogger(__name__)


InputSource = Literal["community_post", "transcript_headers", "signal"]


@dataclass
class SessionThemesResult:
    themes: list[str]
    status: Literal["success", "failed", "skipped"]
    source_used: str | None
    error: str | None = None


def _call_llm(model: str, prompt: str) -> str:
    return call_openrouter(model=model, prompt=prompt)


def select_session_input(
    community_post: CommunityPost | None,
    transcript_segments: list[TranscriptSegment],
    signal_sections: list[SignalSection],
    max_tokens: int,
) -> tuple[InputSource | None, str]:
    """Pick the Stage B input per deterministic priority.

    Returns (source_name, text). source_name is None when no input is available.
    """
    if community_post is not None and community_post.token_count <= max_tokens:
        return "community_post", community_post.body

    if transcript_segments:
        chunks = [
            f"topic: {s.topic}\nsummary: {s.summary}\nkeywords: {', '.join(s.keywords)}"
            for s in transcript_segments
        ]
        return "transcript_headers", "\n\n".join(chunks)

    if signal_sections:
        return "signal", "\n\n".join(s.body for s in signal_sections)

    return None, ""


def extract_session_themes(
    input_text: str,
    model: str,
    prompt_template: str,
) -> SessionThemesResult:
    """Call the session-themes LLM and return parsed themes.

    Failure returns status="failed" with empty themes; caller proceeds.
    """
    if not input_text:
        return SessionThemesResult(themes=[], status="skipped", source_used=None, error="no input")

    prompt = f"{prompt_template}\n\nSESSION_INPUT:\n{input_text}"

    try:
        raw = _call_llm(model=model, prompt=prompt)
    except Exception as exc:
        logger.warning("Stage B LLM failed: %s", exc)
        return SessionThemesResult(themes=[], status="failed", source_used=None, error=str(exc))

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return SessionThemesResult(themes=[], status="failed", source_used=None, error=str(exc))

    themes = list(data.get("themes") or [])
    return SessionThemesResult(
        themes=themes,
        status="success",
        source_used=None,  # caller can set after select_session_input
        error=None,
    )
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_ingestion_session_extractor.py -v`
Expected: 6 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/session_extractor.py \
        community-brain/tests/test_ingestion_session_extractor.py
git commit -m "feat(ingestion): add Stage B session-themes extraction with deterministic input"
```

---

### Task 17: Embedding — reuse existing nomic helper

**Files:**
- Create: `community-brain/src/community_brain/ingestion/embedding.py`
- Create: `community-brain/tests/test_ingestion_embedding.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_ingestion_embedding.py`:

```python
"""Tests for embedding batch helper."""

from __future__ import annotations

from unittest.mock import patch, MagicMock

from community_brain.ingestion.embedding import embed_texts


def test_embed_texts_returns_list_of_vectors() -> None:
    mock_response = {"embeddings": [[0.1] * 768, [0.2] * 768]}
    mock_client = MagicMock()
    mock_client.embed.return_value = mock_response

    with patch("community_brain.ingestion.embedding.ollama.Client", return_value=mock_client):
        result = embed_texts(["hello", "world"], ollama_base_url="http://localhost:11434")

    assert len(result) == 2
    assert len(result[0]) == 768
    mock_client.embed.assert_called_once_with(model="nomic-embed-text", input=["hello", "world"])


def test_embed_texts_empty_input_returns_empty_list() -> None:
    result = embed_texts([], ollama_base_url=None)
    assert result == []
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_ingestion_embedding.py -v`
Expected: FAIL (module does not exist).

- [ ] **Step 3: Implement embedding.py**

Create `community-brain/src/community_brain/ingestion/embedding.py`:

```python
"""Batch embedding helper using Ollama + nomic-embed-text."""

from __future__ import annotations

import ollama

EMBED_MODEL = "nomic-embed-text"


def embed_texts(texts: list[str], ollama_base_url: str | None) -> list[list[float]]:
    """Embed a batch of texts. Returns list of vectors in input order.

    ollama_base_url: explicit Ollama host, e.g. "http://localhost:11434".
    When None, uses the default client (process env / ollama default).
    """
    if not texts:
        return []

    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=EMBED_MODEL, input=texts)
    else:
        response = ollama.embed(model=EMBED_MODEL, input=texts)

    return list(response["embeddings"])
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_ingestion_embedding.py -v`
Expected: 2 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/embedding.py \
        community-brain/tests/test_ingestion_embedding.py
git commit -m "feat(ingestion): add batch embedding helper using Ollama nomic-embed-text"
```

---

### Task 18: Pipeline orchestrator (parse → chunk → extract → embed → commit)

**Files:**
- Create: `community-brain/src/community_brain/ingestion/pipeline.py`
- Create: `community-brain/tests/test_ingestion_pipeline.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_ingestion_pipeline.py`:

```python
"""Integration tests for the ingestion pipeline orchestrator.

LLM calls are mocked; LanceDB uses a temp directory; embeddings are faked.
"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from community_brain.ingestion.pipeline import IngestRequest, ingest_session

FIXTURES = Path(__file__).parent / "fixtures"


def _fake_embed(texts, ollama_base_url=None):
    return [[0.0] * 768 for _ in texts]


def _fake_extract_response(_model, prompt):
    """Mock OpenRouter responses.

    Distinguishes Stage B (themes) vs Stage C (chunk) by prompt content.
    """
    if "SESSION_INPUT:" in prompt:
        return json.dumps({"themes": ["agent frameworks", "embeddings"]})
    # Stage C
    return json.dumps({
        "entities": ["LangGraph"],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": ["comparison"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    })


def _write_min_configs(tmp_path: Path) -> Path:
    (tmp_path / "chunking.yaml").write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    (tmp_path / "extraction-config.yaml").write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: m
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: m
        """,
        encoding="utf-8",
    )
    (tmp_path / "speaker-aliases.yaml").write_text(
        """
version: "2026-04-18"
aliases:
  Alex Rojas: [alexrojas]
pending: []
        """,
        encoding="utf-8",
    )
    (tmp_path / "entity-registry.yaml").write_text(
        """
version: "2026-04-18"
entities:
  LangGraph:
    type: framework
    aliases: [langgraph]
pending: []
        """,
        encoding="utf-8",
    )
    prompts_dir = tmp_path / "extraction-prompts"
    prompts_dir.mkdir()
    (prompts_dir / "session-themes-v1.md").write_text("session themes prompt", encoding="utf-8")
    (prompts_dir / "chunk-extraction-v1.md").write_text("chunk extraction prompt", encoding="utf-8")
    return tmp_path


def test_ingest_session_end_to_end(tmp_path: Path) -> None:
    config_dir = _write_min_configs(tmp_path / "config")

    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="Agent frameworks comparison",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            "extracted_signal": str(FIXTURES / "extracted-signal-sample.md"),
            "community_post": str(FIXTURES / "community-post-sample.md"),
        },
        force_reextract=False,
    )

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=lambda model, input: {"embeddings": [[0.0] * 768 for _ in input]},
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ):
        result = ingest_session(
            request=request,
            config_dir=config_dir,
            db_path=str(db_path),
            ollama_base_url=None,
        )

    assert result.chunks_written > 0
    assert result.chunks_by_type["prepared_transcript"] == 2
    assert result.chunks_by_type["extracted_signal"] == 4
    assert result.chunks_by_type["community_post"] == 1
    assert result.extraction_prompt_version == "chunk-extraction-v1"


def test_ingest_session_idempotent_reingest(tmp_path: Path) -> None:
    """Re-running ingest on same session with same version is a no-op."""
    config_dir = _write_min_configs(tmp_path / "config")
    db_path = tmp_path / "lancedb"

    request = IngestRequest(
        session_id="2026-03-10",
        session_date="2026-03-10",
        session_title="t",
        artifact_paths={
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        force_reextract=False,
    )

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=lambda model, input: {"embeddings": [[0.0] * 768 for _ in input]},
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ):
        first = ingest_session(request, config_dir, str(db_path), None)
        second = ingest_session(request, config_dir, str(db_path), None)

    assert first.chunks_written > 0
    assert second.chunks_skipped_idempotent == first.chunks_written
    assert second.chunks_written == 0
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_ingestion_pipeline.py -v`
Expected: FAIL (module does not exist).

- [ ] **Step 3: Implement pipeline.py**

Create `community-brain/src/community_brain/ingestion/pipeline.py`:

```python
"""Pipeline orchestrator for Community Brain ingestion.

Stages (per spec §5):
  A. Parse artifacts and build Chunk records (deterministic).
  B. Session-level LLM extraction → session_themes (one call).
  C. Chunk-level LLM extraction → entities, speech_acts, stance, etc. (N calls).
  D. Embedding (batched via nomic-embed-text).
  E. Atomic commit to LanceDB (per-session transaction).

Idempotency: chunks whose (chunk_id, extraction_prompt_version) already exist
in the table with extraction_status=success are skipped unless force_reextract=true.
"""

from __future__ import annotations

import datetime as dt
import logging
from dataclasses import dataclass, field
from pathlib import Path

import lancedb
import pyarrow as pa

from community_brain.ingestion.chunker import (
    chunk_prepared_transcript,
    chunk_extracted_signal,
    chunk_community_post,
)
from community_brain.ingestion.config_loader import (
    load_chunking_config,
    load_extraction_config,
)
from community_brain.ingestion.embedding import embed_texts
from community_brain.ingestion.extractor import extract_chunk_metadata
from community_brain.ingestion.parser import (
    parse_prepared_transcript,
    parse_extracted_signal,
    parse_community_post,
)
from community_brain.ingestion.registries import (
    load_speaker_registry,
    load_entity_registry,
)
from community_brain.ingestion.schema import Chunk, SCHEMA_VERSION
from community_brain.ingestion.session_extractor import (
    extract_session_themes,
    select_session_input,
)

logger = logging.getLogger(__name__)

TABLE_NAME = "chunks"


@dataclass
class IngestRequest:
    session_id: str
    session_date: str
    session_title: str | None
    artifact_paths: dict[str, str]  # keys: prepared_transcript, extracted_signal, community_post
    force_reextract: bool = False


@dataclass
class IngestResult:
    session_id: str
    chunks_written: int
    chunks_by_type: dict[str, int]
    chunks_skipped_idempotent: int
    chunks_failed: int
    extraction_model: str
    extraction_prompt_version: str
    schema_version: str
    warnings: list[str] = field(default_factory=list)
    unknown_entities_flagged: list[str] = field(default_factory=list)
    unknown_speakers_flagged: list[str] = field(default_factory=list)


def ingest_session(
    request: IngestRequest,
    config_dir: Path,
    db_path: str,
    ollama_base_url: str | None,
) -> IngestResult:
    """Orchestrate the full ingestion of one session. See module docstring."""
    config_dir = Path(config_dir)
    chunking_cfg = load_chunking_config(config_dir / "chunking.yaml")
    extraction_cfg = load_extraction_config(config_dir / "extraction-config.yaml")
    speaker_reg = load_speaker_registry(config_dir / "speaker-aliases.yaml")
    entity_reg = load_entity_registry(config_dir / "entity-registry.yaml")

    prompts_dir = config_dir / "extraction-prompts"
    chunk_extraction_prompt = (prompts_dir / extraction_cfg.chunk_extraction_prompt_file).read_text(encoding="utf-8")
    session_themes_prompt = (prompts_dir / extraction_cfg.session_themes_prompt_file).read_text(encoding="utf-8")

    chunk_prompt_version = Path(extraction_cfg.chunk_extraction_prompt_file).stem
    session_prompt_version = Path(extraction_cfg.session_themes_prompt_file).stem

    # --- Stage A: parse & chunk ---
    transcript_chunks: list[Chunk] = []
    signal_chunks: list[Chunk] = []
    post_chunks: list[Chunk] = []
    transcript_segments = []
    signal_sections = []
    community_post = None

    if "prepared_transcript" in request.artifact_paths:
        text = Path(request.artifact_paths["prepared_transcript"]).read_text(encoding="utf-8")
        transcript_segments = parse_prepared_transcript(text)
        transcript_chunks = chunk_prepared_transcript(
            transcript_segments,
            session_id=request.session_id,
            session_date=request.session_date,
            session_title=request.session_title,
            source_file=request.artifact_paths["prepared_transcript"],
            segment_max_tokens=chunking_cfg.transcript_segment_max_tokens,
        )

    if "extracted_signal" in request.artifact_paths:
        text = Path(request.artifact_paths["extracted_signal"]).read_text(encoding="utf-8")
        signal_sections = parse_extracted_signal(text)
        signal_chunks = chunk_extracted_signal(
            signal_sections,
            session_id=request.session_id,
            session_date=request.session_date,
            session_title=request.session_title,
            source_file=request.artifact_paths["extracted_signal"],
        )

    if "community_post" in request.artifact_paths:
        text = Path(request.artifact_paths["community_post"]).read_text(encoding="utf-8")
        community_post = parse_community_post(text)
        post_chunks = chunk_community_post(
            community_post,
            session_id=request.session_id,
            session_date=request.session_date,
            session_title=request.session_title,
            source_file=request.artifact_paths["community_post"],
            post_max_tokens=chunking_cfg.post_max_tokens,
        )

    all_chunks = transcript_chunks + signal_chunks + post_chunks
    if not all_chunks:
        return IngestResult(
            session_id=request.session_id,
            chunks_written=0,
            chunks_by_type={},
            chunks_skipped_idempotent=0,
            chunks_failed=0,
            extraction_model=extraction_cfg.chunk_extraction_model,
            extraction_prompt_version=chunk_prompt_version,
            schema_version=SCHEMA_VERSION,
            warnings=["no artifacts to ingest"],
        )

    # --- Idempotency check ---
    existing_ids_by_version = _load_existing_chunk_versions(db_path, request.session_id)
    if not request.force_reextract:
        skip_ids: set[str] = set()
        for chunk in all_chunks:
            prior_version = existing_ids_by_version.get(chunk.chunk_id)
            if prior_version == chunk_prompt_version:
                skip_ids.add(chunk.chunk_id)
        if skip_ids:
            all_chunks = [c for c in all_chunks if c.chunk_id not in skip_ids]
            if not all_chunks:
                return IngestResult(
                    session_id=request.session_id,
                    chunks_written=0,
                    chunks_by_type={},
                    chunks_skipped_idempotent=len(skip_ids),
                    chunks_failed=0,
                    extraction_model=extraction_cfg.chunk_extraction_model,
                    extraction_prompt_version=chunk_prompt_version,
                    schema_version=SCHEMA_VERSION,
                )

    # --- Stage B: session themes ---
    source, session_input = select_session_input(
        community_post=community_post,
        transcript_segments=transcript_segments,
        signal_sections=signal_sections,
        max_tokens=chunking_cfg.session_themes_input_max_tokens,
    )
    themes_result = extract_session_themes(
        input_text=session_input,
        model=extraction_cfg.session_themes_model,
        prompt_template=session_themes_prompt,
    )
    if themes_result.status != "success":
        logger.warning("Stage B skipped/failed for %s: %s", request.session_id, themes_result.error)
    for chunk in all_chunks:
        chunk.session_themes = list(themes_result.themes)

    # --- Stage C: per-chunk extraction ---
    entity_names = list(entity_reg.entities.keys())
    speaker_names = list(speaker_reg.aliases.keys())
    unknown_entities: set[str] = set()
    unknown_speakers: set[str] = set()
    failed_count = 0

    for chunk in all_chunks:
        res = extract_chunk_metadata(
            chunk_text=chunk.full_text,
            entity_registry_names=entity_names,
            speaker_alias_names=speaker_names,
            model=extraction_cfg.chunk_extraction_model,
            prompt_template=chunk_extraction_prompt,
        )
        chunk.extraction_model = extraction_cfg.chunk_extraction_model
        chunk.extraction_prompt_version = chunk_prompt_version
        chunk.extracted_at = dt.datetime.now(dt.timezone.utc)

        if res.status == "failed":
            chunk.extraction_status = "failed"
            chunk.extraction_error = res.error
            failed_count += 1
        else:
            chunk.extraction_status = "success"
            chunk.extraction_error = None
            chunk.entities = res.entities
            chunk.speakers_mentioned = list(set((chunk.speakers_spoke or []) + res.new_speakers_seen))
            chunk.speech_acts = res.speech_acts
            chunk.stance = res.stance  # type: ignore[assignment]
            chunk.certainty = res.certainty  # type: ignore[assignment]
            chunk.chunk_local_markers = res.chunk_local_markers
            chunk.decisions = res.decisions or None
            chunk.action_items = res.action_items or None
            chunk.external_refs = res.external_refs or None
            chunk.references_prior = res.references_prior
            unknown_entities.update(res.new_entities_seen)
            unknown_speakers.update(res.new_speakers_seen)

    # --- Stage D: embeddings ---
    embeddings = embed_texts(
        [c.embed_text for c in all_chunks],
        ollama_base_url=ollama_base_url,
    )
    for chunk, emb in zip(all_chunks, embeddings, strict=True):
        chunk.embedding = emb

    # --- Stage E: atomic commit ---
    _commit_chunks(db_path, all_chunks, replace_ids=[c.chunk_id for c in all_chunks])

    # Flush registry pending updates atomically
    if unknown_entities:
        entity_reg.append_pending(sorted(unknown_entities))
        entity_reg.flush(config_dir / "entity-registry.yaml")
    if unknown_speakers:
        speaker_reg.append_pending(sorted(unknown_speakers))
        speaker_reg.flush(config_dir / "speaker-aliases.yaml")

    # Tally by content type
    by_type: dict[str, int] = {}
    for c in all_chunks:
        by_type[c.content_type] = by_type.get(c.content_type, 0) + 1

    return IngestResult(
        session_id=request.session_id,
        chunks_written=len(all_chunks),
        chunks_by_type=by_type,
        chunks_skipped_idempotent=len(existing_ids_by_version) if request.force_reextract else 0,
        chunks_failed=failed_count,
        extraction_model=extraction_cfg.chunk_extraction_model,
        extraction_prompt_version=chunk_prompt_version,
        schema_version=SCHEMA_VERSION,
        unknown_entities_flagged=sorted(unknown_entities),
        unknown_speakers_flagged=sorted(unknown_speakers),
    )


def _load_existing_chunk_versions(db_path: str, session_id: str) -> dict[str, str]:
    """Return dict mapping chunk_id -> extraction_prompt_version for existing rows.

    Returns empty dict if table does not exist yet.
    """
    try:
        db = lancedb.connect(db_path)
        if TABLE_NAME not in db.table_names():
            return {}
        table = db.open_table(TABLE_NAME)
    except Exception:
        return {}

    try:
        rows = (
            table.search()
            .where(f"session_id = '{session_id}' AND extraction_status = 'success'")
            .select(["chunk_id", "extraction_prompt_version"])
            .to_list()
        )
    except Exception:
        return {}

    return {r["chunk_id"]: r["extraction_prompt_version"] for r in rows}


def _commit_chunks(db_path: str, chunks: list[Chunk], replace_ids: list[str]) -> None:
    """Write chunks to LanceDB as a single atomic operation per session.

    If the target table exists and replace_ids are provided, delete those rows
    first, then append — giving us an "upsert by chunk_id" semantics.
    """
    if not chunks:
        return

    records = [c.to_arrow_dict() for c in chunks]

    db = lancedb.connect(db_path)
    if TABLE_NAME not in db.table_names():
        db.create_table(TABLE_NAME, data=records)
        return

    table = db.open_table(TABLE_NAME)
    if replace_ids:
        id_list = ", ".join(f"'{cid}'" for cid in replace_ids)
        table.delete(f"chunk_id IN ({id_list})")
    table.add(records)
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_ingestion_pipeline.py -v`
Expected: 2 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/ingestion/pipeline.py \
        community-brain/tests/test_ingestion_pipeline.py
git commit -m "feat(ingestion): orchestrator for parse-chunk-extract-embed-commit with idempotency"
```

---

### Task 19: Retrieval server `/ingest` endpoint

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Create: `community-brain/tests/test_retrieval_server_ingest.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_retrieval_server_ingest.py`:

```python
"""Tests for POST /ingest endpoint."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod

FIXTURES = Path(__file__).parent / "fixtures"


def _fake_extract_response(_model, prompt):
    if "SESSION_INPUT:" in prompt:
        return json.dumps({"themes": ["agent frameworks"]})
    return json.dumps({
        "entities": [],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": [],
        "stance": None,
        "certainty": "asserted",
        "chunk_local_markers": [],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    })


def _write_configs(tmp_path: Path) -> Path:
    cfg = tmp_path / "config"
    cfg.mkdir()
    (cfg / "chunking.yaml").write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    (cfg / "extraction-config.yaml").write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: m
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: m
        """,
        encoding="utf-8",
    )
    (cfg / "speaker-aliases.yaml").write_text('version: "x"\naliases: {}\npending: []\n', encoding="utf-8")
    (cfg / "entity-registry.yaml").write_text('version: "x"\nentities: {}\npending: []\n', encoding="utf-8")
    prompts = cfg / "extraction-prompts"
    prompts.mkdir()
    (prompts / "session-themes-v1.md").write_text("p", encoding="utf-8")
    (prompts / "chunk-extraction-v1.md").write_text("p", encoding="utf-8")
    return cfg


def test_post_ingest_success(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"

    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    # No API key required (dev mode)

    client = TestClient(server_mod.app)

    body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "t",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=lambda model, input: {"embeddings": [[0.0] * 768 for _ in input]},
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ):
        resp = client.post("/ingest", json=body)

    assert resp.status_code == 200
    data = resp.json()
    assert data["session_id"] == "2026-03-10"
    assert data["chunks_written"] > 0
    assert data["schema_version"] == "1.0"


def test_post_ingest_missing_all_artifacts_returns_400(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _write_configs(tmp_path)
    db_path = tmp_path / "lancedb"

    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))

    client = TestClient(server_mod.app)

    body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "t",
        "artifact_paths": {},
        "force_reextract": False,
    }

    resp = client.post("/ingest", json=body)
    assert resp.status_code == 400
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_retrieval_server_ingest.py -v`
Expected: FAIL (endpoint not yet defined).

- [ ] **Step 3: Modify retrieval_server.py to add `/ingest`**

In `community-brain/src/community_brain/query/retrieval_server.py`:

Add imports at the top (after existing imports):

```python
from community_brain.ingestion.pipeline import IngestRequest, ingest_session
```

After `PROJECT_ROOT` / `CONFIG_DIR` definitions, add:

```python
# Config dir can be overridden per-deployment (tests use tmp_path).
CONFIG_DIR_OVERRIDE_ENV = "COMMUNITY_BRAIN_CONFIG_DIR"


def _config_dir() -> Path:
    return Path(os.environ.get(CONFIG_DIR_OVERRIDE_ENV, CONFIG_DIR))
```

Add Pydantic request/response models near the existing `QueryRequest`:

```python
class IngestArtifactPaths(BaseModel):
    prepared_transcript: str | None = None
    extracted_signal: str | None = None
    community_post: str | None = None


class IngestHTTPRequest(BaseModel):
    session_id: str
    session_date: str
    session_title: str | None = None
    artifact_paths: dict[str, str]
    force_reextract: bool = False


class IngestHTTPResponse(BaseModel):
    session_id: str
    chunks_written: int
    chunks_by_type: dict[str, int]
    chunks_skipped_idempotent: int
    chunks_failed: int
    extraction_model: str
    extraction_prompt_version: str
    schema_version: str
    warnings: list[str]
    unknown_entities_flagged: list[str]
    unknown_speakers_flagged: list[str]
```

Add the endpoint before `if __name__ == "__main__":`:

```python
@app.post("/ingest", response_model=IngestHTTPResponse)
def ingest(req: IngestHTTPRequest, _key: str | None = Depends(_verify_api_key)):
    if not req.artifact_paths:
        raise HTTPException(status_code=400, detail="no artifact_paths provided")

    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)

    pipeline_req = IngestRequest(
        session_id=req.session_id,
        session_date=req.session_date,
        session_title=req.session_title,
        artifact_paths=req.artifact_paths,
        force_reextract=req.force_reextract,
    )

    result = ingest_session(
        request=pipeline_req,
        config_dir=_config_dir(),
        db_path=db_path,
        ollama_base_url=ollama_base_url,
    )

    return IngestHTTPResponse(
        session_id=result.session_id,
        chunks_written=result.chunks_written,
        chunks_by_type=result.chunks_by_type,
        chunks_skipped_idempotent=result.chunks_skipped_idempotent,
        chunks_failed=result.chunks_failed,
        extraction_model=result.extraction_model,
        extraction_prompt_version=result.extraction_prompt_version,
        schema_version=result.schema_version,
        warnings=result.warnings,
        unknown_entities_flagged=result.unknown_entities_flagged,
        unknown_speakers_flagged=result.unknown_speakers_flagged,
    )
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_retrieval_server_ingest.py -v`
Expected: 2 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_retrieval_server_ingest.py
git commit -m "feat(retrieval): add POST /ingest endpoint backed by ingestion pipeline"
```

---

### Task 20: Extended `/query` with structured response and new filters

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Modify: `community-brain/src/community_brain/query/query_local.py`
- Create: `community-brain/tests/test_retrieval_server_query_v2.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_retrieval_server_query_v2.py`:

```python
"""Tests for the extended POST /query endpoint with structured response."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def _fake_search_results() -> list[dict]:
    return [
        {
            "chunk_id": "2026-03-10:transcript:001",
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t",
            "content_type": "prepared_transcript",
            "source_file": "x.md",
            "full_text": "ground truth",
            "embed_text": "topic: x",
            "topic_label": "x",
            "speakers_spoke": ["Alex Rojas"],
            "speakers_mentioned": ["Alex Rojas"],
            "entities": ["LangGraph"],
            "keywords": ["agents"],
            "session_themes": ["agent frameworks"],
            "speech_acts": ["comparison"],
            "stance": "positive",
            "certainty": "asserted",
            "chunk_local_markers": ["emphasized"],
            "corpus_derived_markers": [],
            "corpus_markers_computed_at": None,
            "has_question": False,
            "has_answer": False,
            "has_unresolved_question": False,
            "has_insight": True,
            "decisions": [],
            "action_items": [],
            "external_refs": [],
            "references_prior": False,
            "schema_version": "1.0",
            "extraction_model": "m",
            "extraction_prompt_version": "chunk-extraction-v1",
            "extraction_status": "success",
            "extraction_error": None,
            "extracted_at": "2026-03-10T14:22:11+00:00",
            "_distance": 0.12,
        }
    ]


def test_post_query_returns_structured_shape(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch("community_brain.query.query_local.search_chunks_v2", return_value=_fake_search_results()):
        resp = client.post("/query", json={"question": "what about agents?", "top_k": 5})

    assert resp.status_code == 200
    data = resp.json()
    assert "chunks" in data
    chunk = data["chunks"][0]
    assert "ground_truth" in chunk
    assert "derived_metadata" in chunk
    assert "provenance" in chunk
    assert chunk["ground_truth"]["chunk_id"] == "2026-03-10:transcript:001"
    assert chunk["ground_truth"]["full_text"] == "ground truth"
    assert chunk["derived_metadata"]["stance"] == "positive"
    assert chunk["provenance"]["extraction_prompt_version"] == "chunk-extraction-v1"


def test_post_query_applies_entity_filter(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    capture = {}

    def _spy(question, db_path, top_k, filters, ollama_base_url):
        capture["filters"] = filters
        return _fake_search_results()

    with patch("community_brain.query.query_local.search_chunks_v2", side_effect=_spy):
        resp = client.post(
            "/query",
            json={
                "question": "x",
                "top_k": 5,
                "filters": {
                    "entities": ["LangGraph"],
                    "entities_match": "any",
                    "require_chunk_markers": ["emphasized"],
                },
            },
        )
    assert resp.status_code == 200
    assert capture["filters"]["entities"] == ["LangGraph"]
    assert capture["filters"]["entities_match"] == "any"
    assert capture["filters"]["require_chunk_markers"] == ["emphasized"]
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_retrieval_server_query_v2.py -v`
Expected: FAIL (new shape not implemented).

- [ ] **Step 3: Modify query_local.py — add `search_chunks_v2`**

At the top of `community-brain/src/community_brain/query/query_local.py`, keep existing imports and add `from typing import Any`. Below the existing `search_chunks`, add a new function:

```python
def build_filter_expression_v2(filters: dict[str, Any] | None) -> str | None:
    """Build a LanceDB WHERE clause from the v2 filter dict.

    Supported filter keys:
      session_date_range: [start, end]
      content_type: list[str]
      speakers_spoke / speakers_spoke_match
      speakers_mentioned / speakers_mentioned_match
      entities / entities_match
      keywords / keywords_match
      schema_version_min
      require_chunk_markers / exclude_chunk_markers
      require_corpus_markers / exclude_corpus_markers
      has_question / has_answer / has_unresolved_question / has_insight / references_prior
    """
    if not filters:
        return None

    clauses: list[str] = []

    dr = filters.get("session_date_range")
    if dr and len(dr) == 2:
        clauses.append(f"session_date >= '{dr[0]}' AND session_date <= '{dr[1]}'")

    for key in ("content_type",):
        vals = filters.get(key)
        if vals:
            quoted = ", ".join(f"'{v}'" for v in vals)
            clauses.append(f"{key} IN ({quoted})")

    for field_name in (
        "speakers_spoke",
        "speakers_mentioned",
        "entities",
        "keywords",
    ):
        vals = filters.get(field_name)
        if not vals:
            continue
        match = filters.get(f"{field_name}_match", "any")
        if match == "all":
            parts = [f"array_has({field_name}, '{v}')" for v in vals]
            clauses.append("(" + " AND ".join(parts) + ")")
        else:  # any (default)
            parts = [f"array_has({field_name}, '{v}')" for v in vals]
            clauses.append("(" + " OR ".join(parts) + ")")

    for marker_field, key in (
        ("chunk_local_markers", "require_chunk_markers"),
        ("corpus_derived_markers", "require_corpus_markers"),
    ):
        vals = filters.get(key)
        if vals:
            parts = [f"array_has({marker_field}, '{v}')" for v in vals]
            clauses.append("(" + " AND ".join(parts) + ")")

    for marker_field, key in (
        ("chunk_local_markers", "exclude_chunk_markers"),
        ("corpus_derived_markers", "exclude_corpus_markers"),
    ):
        vals = filters.get(key)
        if vals:
            parts = [f"NOT array_has({marker_field}, '{v}')" for v in vals]
            clauses.append("(" + " AND ".join(parts) + ")")

    for bool_field in (
        "has_question",
        "has_answer",
        "has_unresolved_question",
        "has_insight",
        "references_prior",
    ):
        v = filters.get(bool_field)
        if v is not None:
            clauses.append(f"{bool_field} = {'true' if v else 'false'}")

    ver_min = filters.get("schema_version_min")
    if ver_min:
        clauses.append(f"schema_version >= '{ver_min}'")

    if not clauses:
        return None
    return " AND ".join(clauses)


def search_chunks_v2(
    question: str,
    db_path: str,
    top_k: int,
    filters: dict | None,
    ollama_base_url: str | None = None,
    table_name: str = "chunks",
) -> list[dict]:
    """Filter-then-rank v2 search against the new chunks table."""
    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=EMBED_MODEL, input=[question])
    else:
        response = ollama.embed(model=EMBED_MODEL, input=[question])
    query_vector = response["embeddings"][0]

    db = lancedb.connect(db_path)
    table = db.open_table(table_name)
    query = table.search(query_vector).limit(top_k)

    expr = build_filter_expression_v2(filters)
    if expr:
        query = query.where(expr)

    results = query.to_arrow()
    return [
        {col: results[col][i].as_py() for col in results.column_names}
        for i in range(results.num_rows)
    ]
```

- [ ] **Step 4: Modify retrieval_server.py — replace `/query` handler**

In `community-brain/src/community_brain/query/retrieval_server.py`:

Replace the existing `QueryRequest`, `ChunkResult`, `QueryResponse`, and `query` function with:

```python
class QueryFilters(BaseModel):
    session_date_range: list[str] | None = None
    content_type: list[str] | None = None

    speakers_spoke: list[str] | None = None
    speakers_spoke_match: str = "any"
    speakers_mentioned: list[str] | None = None
    speakers_mentioned_match: str = "any"

    entities: list[str] | None = None
    entities_match: str = "any"

    keywords: list[str] | None = None
    keywords_match: str = "any"

    schema_version_min: str | None = None

    require_chunk_markers: list[str] | None = None
    exclude_chunk_markers: list[str] | None = None
    require_corpus_markers: list[str] | None = None
    exclude_corpus_markers: list[str] | None = None

    has_question: bool | None = None
    has_answer: bool | None = None
    has_unresolved_question: bool | None = None
    has_insight: bool | None = None
    references_prior: bool | None = None


class QueryRequestV2(BaseModel):
    question: str
    top_k: int = 10
    filters: QueryFilters | None = None
    response_shape: str = "structured"


class QueryChunkResult(BaseModel):
    ground_truth: dict
    derived_metadata: dict
    provenance: dict
    similarity: float


class QueryResponseV2(BaseModel):
    query: str
    chunks: list[QueryChunkResult]
    total_matched: int
    filters_applied: dict


GROUND_TRUTH_FIELDS = [
    "chunk_id",
    "session_id",
    "session_date",
    "session_title",
    "source_file",
    "full_text",
]

PROVENANCE_FIELDS = [
    "schema_version",
    "extraction_model",
    "extraction_prompt_version",
    "extraction_status",
    "extraction_error",
    "extracted_at",
]

DERIVED_FIELDS_ALL = [
    "content_type", "chunk_index", "total_chunks_in_source",
    "speakers_spoke", "speakers_mentioned", "entities", "keywords",
    "topic_label", "session_themes",
    "speech_acts", "stance", "certainty",
    "chunk_local_markers", "corpus_derived_markers", "corpus_markers_computed_at",
    "has_question", "has_answer", "has_unresolved_question", "has_insight",
    "decisions", "action_items", "external_refs", "references_prior",
]


@app.post("/query", response_model=QueryResponseV2)
def query(req: QueryRequestV2, _key: str | None = Depends(_verify_api_key)):
    from community_brain.query.query_local import search_chunks_v2

    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")

    filters_dict = req.filters.model_dump(exclude_none=False) if req.filters else {}

    raw = search_chunks_v2(
        question=req.question,
        db_path=db_path,
        top_k=req.top_k,
        filters=filters_dict,
        ollama_base_url=ollama_base_url,
    )

    chunks = []
    for row in raw:
        ground = {k: row.get(k) for k in GROUND_TRUTH_FIELDS}
        derived = {k: row.get(k) for k in DERIVED_FIELDS_ALL}
        provenance = {k: row.get(k) for k in PROVENANCE_FIELDS}
        similarity = round(1 - row.get("_distance", 0), 4)
        chunks.append(QueryChunkResult(
            ground_truth=ground,
            derived_metadata=derived,
            provenance=provenance,
            similarity=similarity,
        ))

    return QueryResponseV2(
        query=req.question,
        chunks=chunks,
        total_matched=len(chunks),
        filters_applied=filters_dict,
    )
```

Remove or comment out the old `QueryRequest` / `ChunkResult` / `QueryResponse` to avoid duplicate names.

- [ ] **Step 5: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_retrieval_server_query_v2.py -v`
Expected: 2 tests PASS.

- [ ] **Step 6: Remove obsolete tests for the old /query shape**

The existing `community-brain/tests/test_retrieval_server.py` tests the pre-v1.0 query shape (`chunk_id`, `topic`, `score` flat on the chunk). The new structured shape is incompatible. Delete the old test file — its coverage is now subsumed by `test_retrieval_server_query_v2.py` and `test_end_to_end.py` (added in Task 24).

Run: `rm community-brain/tests/test_retrieval_server.py`

Note: keep `community-brain/tests/test_query.py` — it tests the LanceDB `search_chunks` helper independently and covers the old `filter_date`/`filter_speaker` path. Verify it still passes: `cd community-brain && pytest tests/test_query.py -v`. Expected: PASS (the old `search_chunks` function is still present in `query_local.py`; only the new `search_chunks_v2` was added).

- [ ] **Step 7: Also re-run the ingestion tests to verify no regressions**

Run: `cd community-brain && pytest tests/test_retrieval_server_ingest.py tests/test_ingestion_pipeline.py -v`
Expected: all PASS.

- [ ] **Step 8: Commit**

```bash
git add -u community-brain/tests/test_retrieval_server.py
git add community-brain/src/community_brain/query/query_local.py \
        community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_retrieval_server_query_v2.py
git commit -m "feat(retrieval): extend /query with structured response and v1.0 filter set"
```

---

### Task 21: `/sessions` and `/sessions/{session_id}` endpoints

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Create: `community-brain/tests/test_retrieval_server_sessions.py`

- [ ] **Step 1: Write failing tests**

Create `community-brain/tests/test_retrieval_server_sessions.py`:

```python
"""Tests for GET /sessions and /sessions/{id} endpoints."""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def _fake_rows() -> list[dict]:
    return [
        {
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t1",
            "content_type": "prepared_transcript",
            "has_unresolved_question": False,
            "session_themes": ["a", "b"],
        },
        {
            "session_id": "2026-03-10",
            "session_date": "2026-03-10",
            "session_title": "t1",
            "content_type": "community_post",
            "has_unresolved_question": True,
            "session_themes": ["a", "b"],
        },
        {
            "session_id": "2026-04-01",
            "session_date": "2026-04-01",
            "session_title": "t2",
            "content_type": "prepared_transcript",
            "has_unresolved_question": False,
            "session_themes": ["c"],
        },
    ]


def test_get_sessions_returns_aggregated_sessions(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch("community_brain.query.retrieval_server._load_all_session_rows", return_value=_fake_rows()):
        resp = client.get("/sessions")

    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 2
    session_ids = [s["session_id"] for s in data["sessions"]]
    assert "2026-03-10" in session_ids
    assert "2026-04-01" in session_ids

    s_03 = next(s for s in data["sessions"] if s["session_id"] == "2026-03-10")
    assert s_03["chunk_counts"]["prepared_transcript"] == 1
    assert s_03["chunk_counts"]["community_post"] == 1
    assert s_03["unresolved_question_count"] == 1


def test_get_sessions_detail(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch("community_brain.query.retrieval_server._load_all_session_rows", return_value=_fake_rows()):
        resp = client.get("/sessions/2026-03-10")

    assert resp.status_code == 200
    data = resp.json()
    assert data["session_id"] == "2026-03-10"
    assert data["chunk_counts"]["prepared_transcript"] == 1


def test_get_sessions_detail_not_found(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch("community_brain.query.retrieval_server._load_all_session_rows", return_value=_fake_rows()):
        resp = client.get("/sessions/1999-01-01")

    assert resp.status_code == 404
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_retrieval_server_sessions.py -v`
Expected: FAIL (endpoints don't exist).

- [ ] **Step 3: Add endpoints to retrieval_server.py**

In `retrieval_server.py`, add:

```python
def _load_all_session_rows() -> list[dict]:
    """Load the minimum session-level columns for aggregation.

    Returns empty list if the chunks table does not exist.
    """
    import lancedb
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    try:
        db = lancedb.connect(db_path)
        if "chunks" not in db.table_names():
            return []
        table = db.open_table("chunks")
    except Exception:
        return []
    cols = ["session_id", "session_date", "session_title", "content_type",
            "has_unresolved_question", "session_themes"]
    arr = table.search().select(cols).limit(100_000).to_arrow()
    return [
        {col: arr[col][i].as_py() for col in arr.column_names}
        for i in range(arr.num_rows)
    ]


def _aggregate_sessions(rows: list[dict]) -> dict[str, dict]:
    agg: dict[str, dict] = {}
    for row in rows:
        sid = row["session_id"]
        if sid not in agg:
            agg[sid] = {
                "session_id": sid,
                "session_date": row["session_date"],
                "session_title": row.get("session_title"),
                "chunk_counts": {},
                "unresolved_question_count": 0,
                "session_themes": row.get("session_themes") or [],
            }
        ctype = row["content_type"]
        agg[sid]["chunk_counts"][ctype] = agg[sid]["chunk_counts"].get(ctype, 0) + 1
        if row.get("has_unresolved_question"):
            agg[sid]["unresolved_question_count"] += 1
    return agg


@app.get("/sessions")
def list_sessions(_key: str | None = Depends(_verify_api_key)):
    rows = _load_all_session_rows()
    agg = _aggregate_sessions(rows)
    sessions = sorted(agg.values(), key=lambda s: s["session_date"], reverse=True)
    return {"total": len(sessions), "sessions": sessions}


@app.get("/sessions/{session_id}")
def get_session(session_id: str, _key: str | None = Depends(_verify_api_key)):
    rows = _load_all_session_rows()
    agg = _aggregate_sessions(rows)
    if session_id not in agg:
        raise HTTPException(status_code=404, detail=f"session not found: {session_id}")
    return agg[session_id]
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_retrieval_server_sessions.py -v`
Expected: 3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_retrieval_server_sessions.py
git commit -m "feat(retrieval): add /sessions inventory endpoints"
```

---

### Task 22: `/reindex` endpoint (minimal v1: re-extract by filter)

**Files:**
- Modify: `community-brain/src/community_brain/query/retrieval_server.py`
- Create: `community-brain/tests/test_retrieval_server_reindex.py`

- [ ] **Step 1: Write failing test**

Create `community-brain/tests/test_retrieval_server_reindex.py`:

```python
"""Tests for POST /reindex with operation=re-extract."""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod


def test_post_reindex_dry_run_returns_match_count(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    with patch(
        "community_brain.query.retrieval_server._reindex_select_chunk_ids",
        return_value=["2024-01-01:transcript:001", "2024-01-01:transcript:002"],
    ):
        resp = client.post(
            "/reindex",
            json={
                "filter": {"extraction_prompt_version": "chunk-extraction-v1"},
                "operation": "re-extract",
                "dry_run": True,
            },
        )

    assert resp.status_code == 200
    data = resp.json()
    assert data["matched_chunk_ids"] == ["2024-01-01:transcript:001", "2024-01-01:transcript:002"]
    assert data["dry_run"] is True
    assert data["operation"] == "re-extract"


def test_post_reindex_unsupported_operation(monkeypatch) -> None:
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)
    client = TestClient(server_mod.app)

    resp = client.post(
        "/reindex",
        json={"filter": {}, "operation": "something-else", "dry_run": True},
    )
    assert resp.status_code == 400
```

- [ ] **Step 2: Run test to confirm it fails**

Run: `cd community-brain && pytest tests/test_retrieval_server_reindex.py -v`
Expected: FAIL (endpoint not implemented).

- [ ] **Step 3: Implement `/reindex` (minimal dry-run + re-extract skeleton)**

Add to `retrieval_server.py`:

```python
class ReindexRequest(BaseModel):
    filter: dict = {}
    operation: str
    dry_run: bool = True
    priority_order: str = "newest_first"


class ReindexResponse(BaseModel):
    operation: str
    dry_run: bool
    matched_chunk_ids: list[str]
    note: str


SUPPORTED_REINDEX_OPS = {"re-extract", "re-embed", "delete"}


def _reindex_select_chunk_ids(filter_clause: dict) -> list[str]:
    """Select chunk_ids matching the filter. Used by /reindex."""
    import lancedb
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    db = lancedb.connect(db_path)
    if "chunks" not in db.table_names():
        return []
    table = db.open_table("chunks")
    clauses: list[str] = []
    for key in ("extraction_prompt_version", "extraction_status"):
        if key in filter_clause and filter_clause[key]:
            clauses.append(f"{key} = '{filter_clause[key]}'")
    dr = filter_clause.get("session_date_range")
    if dr and len(dr) == 2:
        clauses.append(f"session_date >= '{dr[0]}' AND session_date <= '{dr[1]}'")

    query = table.search().select(["chunk_id"])
    if clauses:
        query = query.where(" AND ".join(clauses))
    arr = query.limit(100_000).to_arrow()
    return [arr["chunk_id"][i].as_py() for i in range(arr.num_rows)]


@app.post("/reindex", response_model=ReindexResponse)
def reindex(req: ReindexRequest, _key: str | None = Depends(_verify_api_key)):
    if req.operation not in SUPPORTED_REINDEX_OPS:
        raise HTTPException(
            status_code=400,
            detail=f"unsupported operation: {req.operation}. Allowed: {sorted(SUPPORTED_REINDEX_OPS)}",
        )
    matched = _reindex_select_chunk_ids(req.filter)

    note = ""
    if req.dry_run:
        note = "dry run: no mutations applied"
    else:
        note = (
            f"{req.operation} against {len(matched)} chunks is not implemented in v1 minimal; "
            "use force_reextract=true on POST /ingest for re-extraction per session."
        )
    return ReindexResponse(
        operation=req.operation,
        dry_run=req.dry_run,
        matched_chunk_ids=matched,
        note=note,
    )
```

- [ ] **Step 4: Run tests to confirm they pass**

Run: `cd community-brain && pytest tests/test_retrieval_server_reindex.py -v`
Expected: 2 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add community-brain/src/community_brain/query/retrieval_server.py \
        community-brain/tests/test_retrieval_server_reindex.py
git commit -m "feat(retrieval): add POST /reindex with dry-run matching (re-extract deferred to per-session)"
```

---

### Task 23: Docker Compose integration for the VM deployment

**Files:**
- Modify: `docker-compose.yml` (repo root)

- [ ] **Step 1: Read current docker-compose.yml**

Run: `cat docker-compose.yml`

Note the existing n8n and postgres service definitions.

- [ ] **Step 2: Add retrieval server service**

Edit the repo-root `docker-compose.yml`. Add a new service under `services:` — use the existing indentation style of the file. The service definition:

```yaml
  retrieval-server:
    build:
      context: ./community-brain
      dockerfile: Dockerfile
    container_name: community_brain_retrieval
    restart: unless-stopped
    ports:
      - "8999:8999"
    environment:
      - RETRIEVAL_HOST=0.0.0.0
      - RETRIEVAL_PORT=8999
      - LANCEDB_PATH=/data/lancedb/nomic-v1
      - OLLAMA_BASE_URL=${OLLAMA_BASE_URL:-http://host.docker.internal:11434}
      - COMMUNITY_BRAIN_CONFIG_DIR=/app/config
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - RETRIEVAL_API_KEY=${RETRIEVAL_API_KEY:-}
    volumes:
      - ./community-brain/config:/app/config:ro
      - ./community-brain/lancedb:/data/lancedb
      - ./output:/data/output:ro
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

Also ensure the n8n service has `./output:/home/node/output` volume mount (it likely already does — verify and leave alone).

- [ ] **Step 3: Create community-brain/Dockerfile**

Create `community-brain/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# System deps (LanceDB needs a bit extra on slim)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
COPY src ./src

RUN pip install --no-cache-dir -e ".[dev]"

EXPOSE 8999

CMD ["uvicorn", "community_brain.query.retrieval_server:app", "--host", "0.0.0.0", "--port", "8999"]
```

- [ ] **Step 4: Verify the compose file parses**

Run: `docker compose config > /dev/null && echo OK`
Expected: `OK` (no syntax errors).

- [ ] **Step 5: Commit**

```bash
git add docker-compose.yml community-brain/Dockerfile
git commit -m "infra: add retrieval-server container to docker-compose with shared output volume"
```

---

### Task 24: Smoke test — full end-to-end round-trip

**Files:**
- Create: `community-brain/tests/test_end_to_end.py`

- [ ] **Step 1: Write the end-to-end test**

Create `community-brain/tests/test_end_to_end.py`:

```python
"""End-to-end smoke test: ingest fixtures then query them via the API.

Runs fully in-process using TestClient and a temp LanceDB directory.
All LLM calls are mocked. Embeddings are fake 768-dim zero vectors.
"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from community_brain.query import retrieval_server as server_mod

FIXTURES = Path(__file__).parent / "fixtures"


def _fake_extract_response(_model, prompt):
    if "SESSION_INPUT:" in prompt:
        return json.dumps({"themes": ["agent frameworks", "embeddings"]})
    return json.dumps({
        "entities": ["LangGraph"],
        "new_entities_seen": [],
        "new_speakers_seen": [],
        "speech_acts": ["comparison"],
        "stance": "positive",
        "certainty": "asserted",
        "chunk_local_markers": ["emphasized"],
        "decisions": [],
        "action_items": [],
        "external_refs": [],
        "references_prior": False,
    })


def _seed_config(tmp_path: Path) -> Path:
    cfg = tmp_path / "config"
    cfg.mkdir()
    (cfg / "chunking.yaml").write_text(
        """
schema_version: "1.0"
chunking:
  transcript_segment_max_tokens: 1500
  post_max_tokens: 2500
  session_themes_input_max_tokens: 3000
extraction:
  retry_attempts: 3
  retry_backoff_seconds: [2, 8, 32]
  inter_session_delay_seconds: 30
        """,
        encoding="utf-8",
    )
    (cfg / "extraction-config.yaml").write_text(
        """
session_themes:
  prompt_file: session-themes-v1.md
  model: m
chunk_extraction:
  prompt_file: chunk-extraction-v1.md
  model: m
        """,
        encoding="utf-8",
    )
    (cfg / "speaker-aliases.yaml").write_text('version: "x"\naliases: {}\npending: []\n', encoding="utf-8")
    (cfg / "entity-registry.yaml").write_text(
        'version: "x"\nentities:\n  LangGraph:\n    type: framework\n    aliases: [langgraph]\npending: []\n',
        encoding="utf-8",
    )
    prompts = cfg / "extraction-prompts"
    prompts.mkdir()
    (prompts / "session-themes-v1.md").write_text("p", encoding="utf-8")
    (prompts / "chunk-extraction-v1.md").write_text("p", encoding="utf-8")
    return cfg


def test_end_to_end_ingest_then_query(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _seed_config(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)

    ingest_body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "Agent frameworks comparison",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
            "extracted_signal": str(FIXTURES / "extracted-signal-sample.md"),
            "community_post": str(FIXTURES / "community-post-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=lambda model, input: {"embeddings": [[0.1] * 768 for _ in input]},
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ):
        ingest_resp = client.post("/ingest", json=ingest_body)

    assert ingest_resp.status_code == 200
    assert ingest_resp.json()["chunks_written"] >= 7

    # Query with an embedding mocked to match the first row
    with patch(
        "community_brain.query.query_local.ollama.embed",
        return_value={"embeddings": [[0.1] * 768]},
    ):
        query_resp = client.post("/query", json={"question": "agent frameworks", "top_k": 5})

    assert query_resp.status_code == 200
    data = query_resp.json()
    assert data["total_matched"] > 0
    chunk = data["chunks"][0]
    assert "ground_truth" in chunk
    assert chunk["provenance"]["schema_version"] == "1.0"
    assert chunk["derived_metadata"]["entities"] == ["LangGraph"]


def test_end_to_end_sessions_endpoint_after_ingest(tmp_path: Path, monkeypatch) -> None:
    cfg_dir = _seed_config(tmp_path)
    db_path = tmp_path / "lancedb"
    monkeypatch.setenv("COMMUNITY_BRAIN_CONFIG_DIR", str(cfg_dir))
    monkeypatch.setenv("LANCEDB_PATH", str(db_path))
    monkeypatch.delenv("RETRIEVAL_API_KEY", raising=False)

    client = TestClient(server_mod.app)

    body = {
        "session_id": "2026-03-10",
        "session_date": "2026-03-10",
        "session_title": "t",
        "artifact_paths": {
            "prepared_transcript": str(FIXTURES / "prepared-transcript-sample.md"),
        },
        "force_reextract": False,
    }

    with patch(
        "community_brain.ingestion.embedding.ollama.embed",
        side_effect=lambda model, input: {"embeddings": [[0.1] * 768 for _ in input]},
    ), patch(
        "community_brain.ingestion.extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ), patch(
        "community_brain.ingestion.session_extractor._call_llm",
        side_effect=lambda model, prompt: _fake_extract_response(model, prompt),
    ):
        client.post("/ingest", json=body)

    resp = client.get("/sessions")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 1
    assert data["sessions"][0]["session_id"] == "2026-03-10"
```

- [ ] **Step 2: Run the smoke test**

Run: `cd community-brain && pytest tests/test_end_to_end.py -v`
Expected: 2 tests PASS.

- [ ] **Step 3: Run the full test suite to make sure nothing regressed**

Run: `cd community-brain && pytest -v`
Expected: all tests PASS.

- [ ] **Step 4: Commit**

```bash
git add community-brain/tests/test_end_to_end.py
git commit -m "test(community-brain): end-to-end smoke test for ingest→query→sessions round-trip"
```

---

## Self-Review Notes

Spec coverage check (done during plan writing):

| Spec section | Covered by task |
|---|---|
| §3 Architecture (single-host, shared volume) | Task 23 (docker-compose) |
| §4 Data flow (artifacts → ingest → LanceDB) | Tasks 12-18 (parser/chunker/pipeline) |
| §5.1 Three stages (A parse, B session, C chunk) | Tasks 12, 14, 15, 16 |
| §5.2 Chunking rules per content type | Task 14 |
| §5.2.1 Extracted-signal canonical vocabulary | Task 5 (prompt), Task 12 (parser rejects non-canonical) |
| §5.3 Stage B deterministic input selection | Task 16 (`select_session_input`) |
| §5.4 LLM selection | Task 4 (extraction-config points at Gemini Flash Lite) |
| §5.6 Extraction idempotency | Task 18 (`_load_existing_chunk_versions`) |
| §5.7 Batch resumability | Deferred to Plan B (Workflow 2 concern) |
| §5.8 Unknown entities/speakers → pending | Tasks 10, 18 (registries + pipeline flush) |
| §5.9 Prompt versioning | Tasks 4, 5 (versioned files + config pointer) |
| §6.1 37-field schema | Task 13 |
| §6.3 Chunk ID conventions | Task 14 |
| §7.1 /query extended contract | Task 20 |
| §7.2 /ingest endpoint | Task 19 |
| §7.3 /reindex endpoint | Task 22 |
| §7.4 /sessions endpoints | Task 21 |
| §8 Trust model / migration policy | Task 6 (docs), Task 7 (CHANGELOG) |
| §9 Config files | Tasks 1-5 |

**Not covered by this plan (deferred to later plans):**
- Phase 3 (n8n Workflow 1 extension) → Plan B
- Phase 4 (n8n Workflow 2 — transcript-only) → Plan B
- Phase 5 (historical backfill execution) → Plan C
- Phase 6 (Open WebUI integration + validation) → Plan C

---

## Execution Handoff

Plan complete and will be saved to `docs/superpowers/plans/2026-04-18-community-brain-ingestion-plan-a.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
