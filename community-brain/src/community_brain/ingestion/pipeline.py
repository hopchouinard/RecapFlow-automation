"""Pipeline orchestrator for Community Brain session ingestion.

Stages (per spec §5):
  A. Parse artifacts and build Chunk records (deterministic).
  B. Session-level LLM extraction -> session_themes (one call per session).
  C. Chunk-level LLM extraction -> entities, speech_acts, stance, etc.
     (N calls, per-chunk failures don't abort the session).
  D. Embedding (one batched call via nomic-embed-text).
     Only chunks with extraction_status='success' receive embeddings;
     failed chunks are persisted with an empty embedding vector so they
     are excluded from vector search by design.
  E. Atomic commit to LanceDB (delete-then-append for UPSERT semantics).

Idempotency: chunks whose (chunk_id, extraction_prompt_version) already exist
in the table with extraction_status='success' are skipped unless
force_reextract=true. The chunker uses segment-indexed IDs so sub-chunking
changes don't ripple across the whole session's chunk_ids.

force_reextract=True additionally performs a full-session rewrite: ALL existing
rows for the session_id are deleted before the new chunks are added. This cleans
orphan rows left by prior prompt versions that produced more chunks than the
current version.  Use force_reextract=True as the explicit "clean up orphans"
trigger when the prompt template or chunking logic changes.

TODO(v2): wire RetryConfig into Stage B/C LLM calls to honor configured
retry_attempts and retry_backoff_seconds.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import re
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
from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
from community_brain.ingestion.canonicalize import build_alias_map, canonicalize_names
from community_brain.ingestion.embedding import build_transcript_embed_text
from community_brain.ingestion.schema import SCHEMA_VERSION, Chunk, pyarrow_table_schema
from community_brain.ingestion.session_extractor import (
    extract_session_themes,
    select_session_input,
)
from community_brain.query.fts_lifecycle import optimize_fts_index
from community_brain.cli.lint_corpus import lint_corpus_chunks

logger = logging.getLogger(__name__)

TABLE_NAME = "chunks"

# Session IDs and chunk IDs are used in LanceDB WHERE clauses. Strict charset
# avoids any quote/escape ambiguity without needing parameterized queries.
_SAFE_ID_RE = re.compile(r"^[0-9A-Za-z_\-:.]+$")


def _resolve_artifact_root() -> Path | None:
    """Read COMMUNITY_BRAIN_ARTIFACT_ROOT env var. Returns None if unset.

    When set, all artifact_paths passed to ingest_session MUST be inside this
    directory. Unset = no constraint (development / VM deployment without
    a filesystem sandbox).
    """
    raw = os.environ.get("COMMUNITY_BRAIN_ARTIFACT_ROOT")
    if not raw:
        return None
    return Path(raw).resolve()


def _validate_artifact_path(path_str: str, root: Path) -> Path:
    """Resolve `path_str` and verify it lives inside `root`.

    Uses Path.resolve() so symlinks can't escape the root. Raises ValueError
    with a clear message if the path escapes or doesn't exist.
    """
    candidate = Path(path_str).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(
            f"artifact path {path_str!r} escapes COMMUNITY_BRAIN_ARTIFACT_ROOT={root}"
        ) from exc
    if not candidate.is_file():
        raise ValueError(f"artifact path does not exist or is not a file: {path_str!r}")
    return candidate


class CommitError(RuntimeError):
    """Raised when LanceDB commit leaves the table in a torn state."""


def _validate_session_id(session_id: str) -> None:
    if not _SAFE_ID_RE.match(session_id):
        raise ValueError(
            f"session_id must match {_SAFE_ID_RE.pattern!r}, got {session_id!r}"
        )


def _validate_chunk_id(chunk_id: str) -> None:
    if not _SAFE_ID_RE.match(chunk_id):
        raise ValueError(
            f"chunk_id must match {_SAFE_ID_RE.pattern!r}, got {chunk_id!r}"
        )


@dataclass
class IngestRequest:
    """One session's worth of artifact paths + config overrides.

    force_reextract: When True, skips idempotency checks and re-extracts all
        chunks. Also performs a full-session rewrite in LanceDB, deleting ALL
        existing rows for this session_id before adding new chunks. Use this
        when the prompt template or chunking logic has changed and orphan rows
        from prior runs (chunks no longer produced) must be removed.
    """
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

    # Validate session_id before any work — must be safe for WHERE clauses.
    _validate_session_id(request.session_id)

    # Constrain artifact paths to COMMUNITY_BRAIN_ARTIFACT_ROOT if set.
    artifact_root = _resolve_artifact_root()
    if artifact_root is not None:
        for path_str in request.artifact_paths.values():
            _validate_artifact_path(path_str, artifact_root)

    # Note: RetryConfig from chunking.yaml is loaded for schema compatibility
    # but NOT yet wired into Stage B/C calls in v1. Retries use call_llm's
    # built-in 3-attempt policy. Plumbing is planned for v2.
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
    # Build alias map once per session; cheap (dict construction over registry data).
    # Wraps speaker_reg.aliases as {"aliases": ...} to match build_alias_map's expected shape.
    speaker_alias_map = build_alias_map({"aliases": speaker_reg.aliases})
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
            speakers_spoke=chunk.speakers_spoke or [],
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
        # v2 fields — all assigned BEFORE bm25_text / embed_text re-synthesis so
        # re-synthesis sees the freshly-populated values, not chunker defaults.
        chunk.topic_label = res.topic_label
        chunk.speakers_mentioned = res.speakers_mentioned
        chunk.keywords = res.keywords
        chunk.has_question = res.has_question
        chunk.has_answer = res.has_answer
        chunk.has_unresolved_question = res.has_unresolved_question
        chunk.has_insight = res.has_insight
        chunk.speech_acts = res.speech_acts
        chunk.stance = res.stance  # type: ignore[assignment]
        chunk.certainty = res.certainty  # type: ignore[assignment]
        chunk.chunk_local_markers = res.chunk_local_markers
        chunk.decisions = res.decisions or None
        chunk.action_items = res.action_items or None
        chunk.external_refs = res.external_refs or None
        chunk.references_prior = res.references_prior

        # Apply canonicalization to person-bearing fields. Unknowns from the
        # speakers_spoke and speakers_mentioned paths (always people) flow to the
        # speaker-aliases pending queue. Entity-side unknowns are intentionally
        # NOT tracked: no entity registry exists in v3, so they stay raw and
        # surface via BM25 over bm25_text / full_text instead.
        # res.new_speakers_seen / res.new_entities_seen are always [] since T6
        # (extractor no longer emits them); canonicalization-derived unknowns
        # replace them as the pending-queue feed source.
        canon_spoke, unk_spoke = canonicalize_names(chunk.speakers_spoke, speaker_alias_map)
        canon_mentioned, unk_mentioned = canonicalize_names(chunk.speakers_mentioned, speaker_alias_map)
        canon_entities, _unk_entities = canonicalize_names(chunk.entities, speaker_alias_map)
        chunk.speakers_spoke = canon_spoke or chunk.speakers_spoke
        chunk.speakers_mentioned = canon_mentioned
        chunk.entities = canon_entities
        unknown_speakers.update(unk_spoke)
        unknown_speakers.update(unk_mentioned)
        # entity-side unknowns intentionally discarded (see comment above)

        # Re-synthesize bm25_text after Stage C mutated chunk.entities,
        # speakers_mentioned, etc. Construction-time synthesis used empty
        # entities; the FTS-index-relevant value is the post-Stage-C form.
        chunk.bm25_text = synthesize_bm25_text(
            topic_label=chunk.topic_label,
            entities=chunk.entities,
            speakers_spoke=chunk.speakers_spoke,
            speakers_mentioned=chunk.speakers_mentioned,
            keywords=chunk.keywords,
            full_text=chunk.full_text,
        )

        # Re-synthesize embed_text for transcript chunks after Stage C populated
        # entities (and eventually speakers_mentioned + keywords). Construction-time
        # used empty lists for those fields; the embedding-relevant value is the
        # post-Stage-C form. signal/post chunks keep embed_text == full_text.
        #
        # Summary recovery: the LLM-written summary isn't stored as a Chunk field,
        # but it was encoded into the construction-time embed_text by
        # build_transcript_embed_text() as the last "summary: <text>" line.
        # Parse it back here rather than storing a redundant field on Chunk.
        # This is stable as long as build_transcript_embed_text format doesn't change.
        if chunk.content_type == "prepared_transcript":
            existing = chunk.embed_text or ""
            summary = existing.split("summary:", 1)[-1].lstrip() if "summary:" in existing else ""
            chunk.embed_text = build_transcript_embed_text(
                topic_label=chunk.topic_label,
                speakers_spoke=chunk.speakers_spoke,
                speakers_mentioned=chunk.speakers_mentioned,
                entities=chunk.entities,
                keywords=chunk.keywords,
                summary=summary,
            )

    # --- Stage D: embeddings (one batched call) ---
    # Only embed chunks with successful extraction. Failed chunks persist with
    # extraction_status="failed" and an empty embedding so they're excluded from
    # vector search by design (reindex via force_reextract=True to include them).
    chunks_to_embed = [c for c in all_chunks if c.extraction_status == "success"]
    embeddings = embed_texts(
        [c.embed_text for c in chunks_to_embed],
        ollama_base_url=ollama_base_url,
    )
    for chunk, emb in zip(chunks_to_embed, embeddings, strict=True):
        chunk.embedding = emb

    # --- Flush registry pending updates BEFORE commit ---
    # Unknown entities/speakers are worth preserving even if the LanceDB commit
    # fails. Flush early so operator review queue stays current.
    try:
        if unknown_entities:
            entity_reg.append_pending(sorted(unknown_entities))
            entity_reg.flush(config_dir / "entity-registry.yaml")
    except Exception as exc:
        logger.warning("Failed to flush entity-registry pending updates: %s", exc)

    try:
        if unknown_speakers:
            speaker_reg.append_pending(sorted(unknown_speakers))
            speaker_reg.flush(config_dir / "speaker-aliases.yaml")
    except Exception as exc:
        logger.warning("Failed to flush speaker-aliases pending updates: %s", exc)

    # --- Stage E: commit to LanceDB ---
    # full_session_rewrite=True (force_reextract) deletes ALL existing rows for
    # this session_id to clean orphan chunks from prior prompt versions.
    # Otherwise, only rows matching the new chunk_ids are replaced (preserves
    # any skipped-by-idempotency rows not in this commit set).
    _commit_chunks(
        db_path,
        request.session_id,
        all_chunks,
        full_session_rewrite=request.force_reextract,
    )

    # Refresh FTS index so the freshly-committed chunks become BM25-searchable
    # on the next /query. Under LanceDB 0.30.x this is a no-op (auto-update
    # path verified by spike, spec §11.1 Resolution); kept as the canonical
    # refresh seam in case a future LanceDB version drops auto-update.
    if all_chunks:
        try:
            db = lancedb.connect(db_path)
            if TABLE_NAME in db.list_tables().tables:
                table = db.open_table(TABLE_NAME)
                optimize_fts_index(table, "bm25_text")
        except Exception as exc:
            # optimize_fts_index already catches and logs internally; this is
            # belt-and-suspenders against future changes that might propagate.
            logger.warning(
                "optimize_fts_index after ingest raised %r; chunks committed but FTS "
                "may lag until next refresh", exc
            )

    # Auto-trigger corpus lint to refresh corpus_derived_markers across the
    # (now-larger) corpus. WARN-on-failure: chunks are already committed; lint
    # will retry on next ingest or a manual run.
    try:
        _lint_db_path = os.environ.get("COMMUNITY_BRAIN_DB_PATH") or db_path
        lint_stats = lint_corpus_chunks(_lint_db_path)
        logger.info(
            "lint_corpus auto-trigger: scanned %d, recurrent %d",
            lint_stats["scanned"],
            lint_stats["recurrent"],
        )
    except Exception as exc:
        logger.warning("lint_corpus auto-trigger failed: %s; chunks committed", exc)

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
        if TABLE_NAME not in db.list_tables().tables:
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


def _commit_chunks(
    db_path: str,
    session_id: str,
    chunks: list[Chunk],
    full_session_rewrite: bool,
) -> None:
    """Write chunks with UPSERT semantics.

    If full_session_rewrite=True, deletes ALL rows for the session_id before
    adding new chunks (cleans orphans from prior prompt versions that produced
    more chunks than the current version produces). Triggered by force_reextract.

    If full_session_rewrite=False, deletes only rows matching the new chunk_ids
    and appends. Used when idempotency has already kept some existing rows that
    must be preserved.

    NOT fully atomic: if add() fails after delete() succeeded, raises CommitError
    so the caller knows the table is in a torn state (old rows removed, new rows
    not written). Operators can recover by re-running ingest with
    force_reextract=True.
    """
    if not chunks:
        return

    _validate_session_id(session_id)
    for c in chunks:
        _validate_chunk_id(c.chunk_id)

    records = [c.to_arrow_dict() for c in chunks]

    db = lancedb.connect(db_path)
    if TABLE_NAME not in db.list_tables().tables:
        table = db.create_table(TABLE_NAME, data=records, schema=pyarrow_table_schema())
        # Build FTS index immediately on the newly-created table; otherwise
        # subsequent /query hybrid calls have no FTS leg until server restart.
        # Fresh-deploy regression: spec §17.1 drops the table; first /ingest
        # creates it; without this call, the new table ships without an index.
        try:
            from community_brain.query.fts_lifecycle import ensure_fts_index
            ensure_fts_index(table, column="bm25_text")
            logger.info("Created chunks table and built FTS index on bm25_text")
        except Exception as exc:
            logger.error(
                "Created chunks table but FTS index build failed: %s. "
                "/query hybrid will fall back to vector-only until the index is built. "
                "Run server startup hook or call ensure_fts_index manually.",
                exc,
            )
        return

    table = db.open_table(TABLE_NAME)

    # Schema compatibility preflight: refuse to mutate if the existing
    # table predates v1.1 (no bm25_text column). Otherwise the delete-then-add
    # pattern would lose rows when the v1.1 add() raises on schema mismatch.
    if "bm25_text" not in table.schema.names:
        raise CommitError(
            f"chunks table schema is pre-v1.1 (no bm25_text column). "
            f"Refusing to mutate; drop the table and re-ingest under v1.1 "
            f"per docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §17.1."
        )

    try:
        if full_session_rewrite:
            table.delete(f"session_id = '{session_id}'")
        else:
            id_list = ", ".join(f"'{c.chunk_id}'" for c in chunks)
            table.delete(f"chunk_id IN ({id_list})")
    except Exception as exc:
        raise CommitError(
            f"failed to delete before re-add for session {session_id}: {exc}"
        ) from exc

    try:
        table.add(records)
    except Exception as exc:
        raise CommitError(
            f"CRITICAL: deleted rows for session {session_id} but add() failed: {exc}. "
            f"If this is a transient LLM/IO failure, re-run with force_reextract=True "
            f"to recover. If it is a type/cast error, the table schema predates the "
            f"explicit-schema fix and must be rebuilt from scratch (see "
            f"community-brain/docs/DEPLOYMENT.md §5.4)."
        ) from exc
