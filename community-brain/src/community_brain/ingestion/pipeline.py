"""Pipeline orchestrator for Community Brain session ingestion.

Stages (per spec §5):
  A. Parse artifacts and build Chunk records (deterministic).
  B. Session-level LLM extraction -> session_themes (one call per session).
  C. Chunk-level LLM extraction -> entities, speech_acts, stance, etc.
     (N calls, per-chunk failures don't abort the session).
  D. Embedding (one batched call via nomic-embed-text).
  E. Atomic commit to LanceDB (delete-then-append for UPSERT semantics).

Idempotency: chunks whose (chunk_id, extraction_prompt_version) already exist
in the table with extraction_status='success' are skipped unless
force_reextract=true. The chunker uses segment-indexed IDs so sub-chunking
changes don't ripple across the whole session's chunk_ids.
"""

from __future__ import annotations

import datetime as dt
import logging
from dataclasses import dataclass, field
from pathlib import Path

import lancedb

from community_brain.ingestion.chunker import (
    chunk_community_post,
    chunk_extracted_signal,
    chunk_prepared_transcript,
)
from community_brain.ingestion.config_loader import (
    load_chunking_config,
    load_extraction_config,
)
from community_brain.ingestion.embedding import embed_texts
from community_brain.ingestion.extractor import extract_chunk_metadata
from community_brain.ingestion.parser import (
    parse_community_post,
    parse_extracted_signal,
    parse_prepared_transcript,
)
from community_brain.ingestion.registries import (
    load_entity_registry,
    load_speaker_registry,
)
from community_brain.ingestion.schema import SCHEMA_VERSION, Chunk
from community_brain.ingestion.session_extractor import (
    extract_session_themes,
    select_session_input,
)

logger = logging.getLogger(__name__)

TABLE_NAME = "chunks"


@dataclass
class IngestRequest:
    """One session's worth of artifact paths + config overrides."""
    session_id: str
    session_date: str
    session_title: str | None
    artifact_paths: dict[str, str]  # keys: prepared_transcript | extracted_signal | community_post
    force_reextract: bool = False


@dataclass
class IngestResult:
    """Summary of what the pipeline did for one session."""
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
    config_dir: Path | str,
    db_path: str,
    ollama_base_url: str | None,
) -> IngestResult:
    """Run the full ingestion pipeline for one session. See module docstring."""
    config_dir = Path(config_dir)
    chunking_cfg, _retry_cfg = load_chunking_config(config_dir / "chunking.yaml")
    extraction_cfg = load_extraction_config(config_dir / "extraction-config.yaml")
    speaker_reg = load_speaker_registry(config_dir / "speaker-aliases.yaml")
    entity_reg = load_entity_registry(config_dir / "entity-registry.yaml")

    prompts_dir = config_dir / "extraction-prompts"
    chunk_extraction_prompt = (
        prompts_dir / extraction_cfg.chunk_extraction_prompt_file
    ).read_text(encoding="utf-8")
    session_themes_prompt = (
        prompts_dir / extraction_cfg.session_themes_prompt_file
    ).read_text(encoding="utf-8")

    chunk_prompt_version = Path(extraction_cfg.chunk_extraction_prompt_file).stem

    # --- Stage A: parse & chunk (deterministic) ---
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

    # --- Idempotency: drop chunks already successfully extracted under this version ---
    skipped_count = 0
    if not request.force_reextract:
        existing = _load_existing_chunk_versions(db_path, request.session_id)
        kept: list[Chunk] = []
        for chunk in all_chunks:
            prior_version = existing.get(chunk.chunk_id)
            if prior_version == chunk_prompt_version:
                skipped_count += 1
                continue
            kept.append(chunk)
        all_chunks = kept
        if not all_chunks:
            return IngestResult(
                session_id=request.session_id,
                chunks_written=0,
                chunks_by_type={},
                chunks_skipped_idempotent=skipped_count,
                chunks_failed=0,
                extraction_model=extraction_cfg.chunk_extraction_model,
                extraction_prompt_version=chunk_prompt_version,
                schema_version=SCHEMA_VERSION,
            )

    # --- Stage B: session themes (one LLM call) ---
    _source, session_input = select_session_input(
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
    if themes_result.status not in ("success", "skipped"):
        logger.warning(
            "Stage B failed for session %s: %s",
            request.session_id, themes_result.error,
        )
    for chunk in all_chunks:
        chunk.session_themes = list(themes_result.themes)

    # --- Stage C: per-chunk LLM extraction ---
    entity_names = list(entity_reg.entities.keys())
    speaker_names = list(speaker_reg.aliases.keys())
    unknown_entities: set[str] = set()
    unknown_speakers: set[str] = set()
    failed_count = 0
    now = dt.datetime.now(dt.timezone.utc)

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
        chunk.extracted_at = now

        if res.status == "failed":
            chunk.extraction_status = "failed"
            chunk.extraction_error = res.error
            failed_count += 1
            continue

        chunk.extraction_status = "success"
        chunk.extraction_error = None
        chunk.entities = res.entities
        spoken = chunk.speakers_spoke or []
        chunk.speakers_mentioned = sorted(set(spoken + res.new_speakers_seen))
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

    # --- Stage D: embeddings (one batched call) ---
    embeddings = embed_texts(
        [c.embed_text for c in all_chunks],
        ollama_base_url=ollama_base_url,
    )
    for chunk, emb in zip(all_chunks, embeddings, strict=True):
        chunk.embedding = emb

    # --- Stage E: atomic commit to LanceDB ---
    _commit_chunks(db_path, all_chunks)

    # --- Registry pending flushes ---
    if unknown_entities:
        entity_reg.append_pending(sorted(unknown_entities))
        entity_reg.flush(config_dir / "entity-registry.yaml")
    if unknown_speakers:
        speaker_reg.append_pending(sorted(unknown_speakers))
        speaker_reg.flush(config_dir / "speaker-aliases.yaml")

    # Tally chunks_written by content type
    by_type: dict[str, int] = {}
    for c in all_chunks:
        by_type[c.content_type] = by_type.get(c.content_type, 0) + 1

    return IngestResult(
        session_id=request.session_id,
        chunks_written=len(all_chunks),
        chunks_by_type=by_type,
        chunks_skipped_idempotent=skipped_count,
        chunks_failed=failed_count,
        extraction_model=extraction_cfg.chunk_extraction_model,
        extraction_prompt_version=chunk_prompt_version,
        schema_version=SCHEMA_VERSION,
        unknown_entities_flagged=sorted(unknown_entities),
        unknown_speakers_flagged=sorted(unknown_speakers),
    )


def _load_existing_chunk_versions(db_path: str, session_id: str) -> dict[str, str]:
    """Return {chunk_id -> extraction_prompt_version} for existing SUCCESS rows.

    Returns empty dict if the table does not exist yet. Only successful rows
    count for idempotency -- failed rows should be re-attempted on next ingest.
    """
    try:
        db = lancedb.connect(db_path)
        if TABLE_NAME not in db.table_names():  # type: ignore[attr-defined]
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


def _commit_chunks(db_path: str, chunks: list[Chunk]) -> None:
    """Write chunks to LanceDB in one transaction (delete-then-append by chunk_id).

    If the table doesn't exist, create it from the first batch. If it does,
    delete any existing rows with matching chunk_ids and append new records.
    Net effect: upsert-by-chunk_id semantics on a single session's commit.
    """
    if not chunks:
        return

    records = [c.to_arrow_dict() for c in chunks]

    db = lancedb.connect(db_path)
    if TABLE_NAME not in db.table_names():
        db.create_table(TABLE_NAME, data=records)
        return

    table = db.open_table(TABLE_NAME)
    id_list = ", ".join(f"'{c.chunk_id}'" for c in chunks)
    table.delete(f"chunk_id IN ({id_list})")
    table.add(records)
