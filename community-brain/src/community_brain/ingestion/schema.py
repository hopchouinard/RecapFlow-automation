"""LanceDB schema v1.0 for the Community Brain ingestion pipeline.

37 fields, organized into ground-truth, derived-metadata, and provenance groups.
Authoritative field-by-field definition:
    docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md §6

## Trust partitions (see docs/inference-guidelines.md)

- **Ground truth**: chunk_id, session_id, session_date, session_title, source_file,
  full_text, chunk_index, total_chunks_in_source. Authoritative. Quotes must resolve
  to these. chunk_index and total_chunks_in_source are positional/deterministic (set
  by the chunker, not derived by LLM).
- **Derived metadata**: entities, speech_acts, stance, certainty, chunk_local_markers,
  decisions, action_items, external_refs, references_prior, session_themes, topic_label,
  speakers_spoke, speakers_mentioned, keywords, corpus_derived_markers,
  corpus_markers_computed_at, has_question, has_answer, has_unresolved_question,
  has_insight, content_type. LLM-interpreted or derived; probabilistic; re-derivable
  from full_text. NOTE: speakers_mentioned is not populated in v1 (always None);
  reserved for a future Stage C extractor update — consumers should read speakers_spoke.
- **Provenance**: schema_version, extraction_model, extraction_prompt_version,
  extraction_status, extraction_error, extracted_at. Tracks WHAT generated the
  data and WHETHER it succeeded.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, asdict
from typing import Literal

import pyarrow as pa

SCHEMA_VERSION = "1.0"

ContentType = Literal["prepared_transcript", "extracted_signal", "community_post"]
Stance = Literal["positive", "negative", "neutral", "mixed"]
Certainty = Literal["asserted", "hedged", "speculative"]
ExtractionStatus = Literal["success", "failed", "pending"]

#: Embedding vector dimension. Must match the active embed model.
#: Swapping COMMUNITY_BRAIN_EMBED_MODEL to a model with a different dimension
#: requires a full table rebuild; vectors from different models are
#: incompatible anyway (see docs/migrations/CHANGELOG.md §8.4).
EMBEDDING_DIM = 768  # nomic-embed-text

#: List-valued fields that should serialize as `[]` (not None) in LanceDB/Arrow.
#: Null lists are poorly supported in the Arrow type system; normalizing on write
#: avoids downstream schema-inference surprises.
_LIST_FIELDS_NORMALIZED_TO_EMPTY: tuple[str, ...] = (
    "speakers_spoke",
    "speakers_mentioned",
    "keywords",
    "decisions",
    "action_items",
    "external_refs",
)


@dataclass
class Chunk:
    """A single row in the LanceDB chunks table (v1.0 schema, 37 fields).

    Note: not frozen — the chunker (Task 14) and extractor (Tasks 15/16) mutate
    fields in-place during construction. Do not add frozen=True.
    """

    # --- Identity & positional (9) ---
    schema_version: str
    chunk_id: str
    session_id: str
    session_date: str
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

    # --- Session-level context, denormalized (1) ---
    session_themes: list[str]

    # --- Interpretation (6) ---
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
    extracted_at: dt.datetime | None

    # --- Content & embedding (3) ---
    embed_text: str
    full_text: str
    embedding: list[float]

    def to_arrow_dict(self) -> dict:
        """Flatten to a dict suitable for pyarrow / LanceDB insertion.

        Normalizations applied:
        - Null list-valued fields (e.g. speakers_spoke, keywords) become `[]`
          so Arrow doesn't need to infer nullable-list types.
        - Datetimes become ISO-8601 strings for portability across backends.
        - Failed-chunk embeddings (empty list) are padded to a zero vector of
          length EMBEDDING_DIM so they fit the FixedSizeList schema. Query-side
          filtering on extraction_status='success' keeps them unsearchable.
        """
        d = asdict(self)
        for field_name in _LIST_FIELDS_NORMALIZED_TO_EMPTY:
            if d[field_name] is None:
                d[field_name] = []
        if d["corpus_markers_computed_at"] is not None:
            d["corpus_markers_computed_at"] = d["corpus_markers_computed_at"].isoformat()
        if d["extracted_at"] is not None:
            d["extracted_at"] = d["extracted_at"].isoformat()
        if len(d["embedding"]) != EMBEDDING_DIM:
            d["embedding"] = [0.0] * EMBEDDING_DIM
        return d


def pyarrow_table_schema() -> pa.Schema:
    """Explicit pyarrow schema for the chunks table.

    Used at `create_table` time so list-column element types are declared
    rather than inferred from the first batch. Inference would otherwise
    produce `List(Null)` for list columns that happen to be all-empty in the
    first write (e.g. speakers_spoke when the first ingested session is
    community_post-only or extracted_signal-only), poisoning the column and
    making any future write with real values fail with a Utf8-to-Null cast
    error. Field order mirrors the Chunk dataclass.
    """
    return pa.schema([
        ("schema_version", pa.string()),
        ("chunk_id", pa.string()),
        ("session_id", pa.string()),
        ("session_date", pa.string()),
        ("session_title", pa.string()),
        ("content_type", pa.string()),
        ("source_file", pa.string()),
        ("chunk_index", pa.int64()),
        ("total_chunks_in_source", pa.int64()),
        ("speakers_spoke", pa.list_(pa.string())),
        ("speakers_mentioned", pa.list_(pa.string())),
        ("entities", pa.list_(pa.string())),
        ("keywords", pa.list_(pa.string())),
        ("topic_label", pa.string()),
        ("session_themes", pa.list_(pa.string())),
        ("speech_acts", pa.list_(pa.string())),
        ("stance", pa.string()),
        ("certainty", pa.string()),
        ("chunk_local_markers", pa.list_(pa.string())),
        ("corpus_derived_markers", pa.list_(pa.string())),
        ("corpus_markers_computed_at", pa.string()),
        ("has_question", pa.bool_()),
        ("has_answer", pa.bool_()),
        ("has_unresolved_question", pa.bool_()),
        ("has_insight", pa.bool_()),
        ("decisions", pa.list_(pa.string())),
        ("action_items", pa.list_(pa.string())),
        ("external_refs", pa.list_(pa.string())),
        ("references_prior", pa.bool_()),
        ("extraction_model", pa.string()),
        ("extraction_prompt_version", pa.string()),
        ("extraction_status", pa.string()),
        ("extraction_error", pa.string()),
        ("extracted_at", pa.string()),
        ("embed_text", pa.string()),
        ("full_text", pa.string()),
        ("embedding", pa.list_(pa.float32(), EMBEDDING_DIM)),
    ])


def lancedb_table_schema() -> dict[str, str]:
    """Return a human-readable description of the table shape.

    Used for documentation and validation. Actual LanceDB table creation uses
    `pyarrow_table_schema()` above to declare explicit column types.
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
        "extracted_at": "string|null",
        "embed_text": "string",
        "full_text": "string",
        "embedding": "list[float]",
    }
