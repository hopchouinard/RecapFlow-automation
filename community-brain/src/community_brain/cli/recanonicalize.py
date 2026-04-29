"""recanonicalize CLI — rewrite chunks against the current registry.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §7.1.

Usage:
    python -m community_brain.cli.recanonicalize \\
        [--db /data/lancedb/nomic-v1] \\
        [--registry community-brain/config/speaker-aliases.yaml] \\
        [--dry-run]

Decoupled from Stage C extraction — no LLM call. Re-applies the alias
map to person-bearing fields, re-synthesizes embed_text (transcripts)
and bm25_text, re-embeds via Ollama if embed_text changed. Idempotent.
"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any, Callable

import lancedb
import yaml

from community_brain.ingestion.bm25_synthesis import synthesize_bm25_text
from community_brain.ingestion.canonicalize import build_alias_map, canonicalize_names
from community_brain.ingestion.embedding import build_transcript_embed_text


logger = logging.getLogger(__name__)


def _is_transcript(row: dict) -> bool:
    return row.get("content_type") == "prepared_transcript"


def _diff_lists(a: list[str] | None, b: list[str] | None) -> bool:
    """True if list contents differ."""
    return (a or []) != (b or [])


def recanonicalize_chunks(
    db_path: str | Path,
    registry: dict[str, Any],
    *,
    embed_fn: Callable[[str], list[float]],
    dry_run: bool = False,
) -> dict[str, int]:
    """Apply current registry to all chunks; return summary stats.

    embed_fn: callable(text: str) -> list[float]. Production callers pass
    an Ollama-backed function; tests pass a deterministic stub.

    Uses table.update(where=..., values=...) for row-level rewrites — the
    documented LanceDB 0.30.x API for in-place field updates. This avoids
    the delete-then-add risk of a torn table on process interrupt.
    """
    alias_map = build_alias_map(registry)
    db = lancedb.connect(str(db_path))
    table = db.open_table("chunks")
    rows = table.to_arrow().to_pylist()

    scanned = 0
    updated = 0
    for row in rows:
        scanned += 1
        new_spk, _ = canonicalize_names(row.get("speakers_spoke") or [], alias_map)
        new_men, _ = canonicalize_names(row.get("speakers_mentioned") or [], alias_map)
        new_ent, _ = canonicalize_names(row.get("entities") or [], alias_map)

        spk_changed = _diff_lists(new_spk, row.get("speakers_spoke"))
        men_changed = _diff_lists(new_men, row.get("speakers_mentioned"))
        ent_changed = _diff_lists(new_ent, row.get("entities"))
        anything_changed = spk_changed or men_changed or ent_changed

        if not anything_changed:
            continue

        chunk_id = row["chunk_id"]

        # Re-synthesize bm25_text and (for transcripts) embed_text.
        keywords = row.get("keywords") or []
        topic_label = row.get("topic_label")
        full_text = row.get("full_text", "")
        new_bm25_text = synthesize_bm25_text(
            topic_label=topic_label,
            entities=new_ent,
            speakers_spoke=new_spk,
            speakers_mentioned=new_men,
            keywords=keywords,
            full_text=full_text,
        )
        if _is_transcript(row):
            existing = row.get("embed_text") or ""
            if "summary:" not in existing:
                logger.warning(
                    "recanonicalize: chunk %s has no 'summary:' marker in embed_text; "
                    "skipping canonicalization to preserve vector content. "
                    "Re-extract via /ingest force_reextract=true if name canonicalization is needed.",
                    chunk_id,
                )
                continue
            summary = existing.split("summary:", 1)[-1].lstrip()
            new_embed_text = build_transcript_embed_text(
                topic_label=topic_label,
                speakers_spoke=new_spk,
                speakers_mentioned=new_men,
                entities=new_ent,
                keywords=keywords,
                summary=summary,
            )
        else:
            # signal/post: embed_text == full_text; canonicalization doesn't change
            # full_text, so embed_text is stable.
            new_embed_text = row.get("embed_text") or ""

        # Re-embed only if embed_text changed.
        if new_embed_text != (row.get("embed_text") or ""):
            new_embedding = embed_fn(new_embed_text)
        else:
            new_embedding = row.get("embedding")

        updated += 1
        if dry_run:
            continue

        # table.update() can't serialize list-valued Arrow fields (embedding,
        # speakers_spoke, entities, etc.) through LanceDB's value_to_sql path.
        # Use delete-then-add instead, which is the established pattern in
        # pipeline._commit_chunks. Not truly atomic but consistent with project
        # convention; snapshot original row so we can restore on add failure.
        safe_id = chunk_id.replace("'", "''")
        original_row_snapshot = dict(row)  # full snapshot for restore
        new_row = {
            **original_row_snapshot,
            "speakers_spoke": new_spk,
            "speakers_mentioned": new_men,
            "entities": new_ent,
            "embed_text": new_embed_text,
            "bm25_text": new_bm25_text,
            "embedding": new_embedding,
        }
        try:
            table.delete(f"chunk_id = '{safe_id}'")
            table.add([new_row])
        except Exception as add_exc:
            logger.error(
                "recanonicalize add failed for %s: %s; attempting restore",
                chunk_id, add_exc,
            )
            try:
                table.add([original_row_snapshot])
                logger.info(
                    "recanonicalize: restored original row for %s after add failure",
                    chunk_id,
                )
            except Exception as restore_exc:
                logger.critical(
                    "recanonicalize CRITICAL: row %s LOST after add failure (%s) AND "
                    "restore failure (%s). Source artifact at /data/output/<session>/ "
                    "is the recovery path.",
                    chunk_id, add_exc, restore_exc,
                )
            raise add_exc

    return {"scanned": scanned, "updated": updated}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rewrite chunks against the current speaker-aliases registry."
    )
    parser.add_argument("--db", default="/data/lancedb/nomic-v1")
    parser.add_argument("--registry", default="community-brain/config/speaker-aliases.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    registry = yaml.safe_load(Path(args.registry).read_text())

    # embed_texts takes a list; wrap it into a single-text callable.
    from community_brain.ingestion.embedding import embed_texts

    def _embed_one(text: str) -> list[float]:
        results = embed_texts([text], ollama_base_url=None)
        return results[0]

    stats = recanonicalize_chunks(
        args.db,
        registry,
        embed_fn=_embed_one,
        dry_run=args.dry_run,
    )
    print(
        f"[ok] scanned {stats['scanned']}, updated {stats['updated']} "
        f"(dry_run={args.dry_run})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
