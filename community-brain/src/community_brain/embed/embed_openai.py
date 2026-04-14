"""Embed chunk summaries into LanceDB using text-embedding-3-large via OpenAI.

Usage:
    python -m community_brain.embed.embed_openai
    python -m community_brain.embed.embed_openai --date 2025-09-02
    python -m community_brain.embed.embed_openai --dry-run
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

import click
import lancedb
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

logger = logging.getLogger(__name__)

OPENAI_EMBED_MODEL = "text-embedding-3-large"
OPENAI_DIMS = 3072
BATCH_SIZE = 100
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"


def load_chunks_from_jsonl(jsonl_path: Path) -> list[dict]:
    """Load chunks from a JSONL file."""
    chunks = []
    if not jsonl_path.exists():
        return chunks
    for line in jsonl_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            chunks.append(json.loads(line))
    return chunks


def build_lancedb_records(chunks: list[dict]) -> list[dict]:
    """Convert chunk dicts to LanceDB-ready records."""
    records = []
    for chunk in chunks:
        speakers = chunk.get("speakers_in_chunk", [])
        if isinstance(speakers, list):
            speakers = json.dumps(speakers)
        records.append({
            "chunk_id": chunk["chunk_id"],
            "session_date": chunk["session_date"],
            "session_title": chunk["session_title"],
            "topic": chunk.get("topic", ""),
            "summary": chunk.get("summary", ""),
            "text": chunk["text"],
            "speakers_in_chunk": speakers,
            "chunk_position": chunk["chunk_position"],
            "total_chunks_in_session": chunk["total_chunks_in_session"],
            "content_tier": chunk["content_tier"],
            "content_type": chunk["content_type"],
            "source": chunk["source"],
        })
    return records


def embed_and_store(
    chunks: list[dict],
    db_path: str,
    table_name: str = "transcripts",
    api_key: str | None = None,
) -> int:
    """Embed chunk summaries via OpenAI and store in LanceDB."""
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise click.ClickException("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    db = lancedb.connect(db_path)
    records = build_lancedb_records(chunks)

    # Deduplicate input records by chunk_id (keep first occurrence)
    seen_input: dict[str, dict] = {}
    for r in records:
        if r["chunk_id"] not in seen_input:
            seen_input[r["chunk_id"]] = r
    records = list(seen_input.values())

    # Check existing
    try:
        table = db.open_table(table_name)
        existing_ids = set(table.to_arrow()["chunk_id"].to_pylist())
        records = [r for r in records if r["chunk_id"] not in existing_ids]
        if not records:
            logger.info("All chunks already embedded.")
            return 0
    except Exception:
        existing_ids = set()
        table = None

    # Track committed IDs across batches for idempotency
    committed_ids: set[str] = set()

    embedded_count = 0
    for i in tqdm(range(0, len(records), BATCH_SIZE), desc="Embedding (OpenAI)"):
        batch = [r for r in records[i : i + BATCH_SIZE] if r["chunk_id"] not in committed_ids]
        if not batch:
            continue
        summaries = [r["summary"] or r["text"] for r in batch]

        response = client.embeddings.create(
            model=OPENAI_EMBED_MODEL,
            input=summaries,
        )
        embeddings = [item.embedding for item in response.data]

        for record, vector in zip(batch, embeddings):
            record["vector"] = vector

        if table is None:
            table = db.create_table(table_name, data=batch)
        else:
            table.add(batch)

        committed_ids.update(r["chunk_id"] for r in batch)
        embedded_count += len(batch)

    logger.info("Embedded %d new chunks", embedded_count)
    return embedded_count


@click.command()
@click.option("--date", "target_date", default=None, help="Only embed chunks from this date")
@click.option("--dry-run", is_flag=True, help="Show what would be embedded")
@click.option("--db-path", default=None, help="Override LanceDB path")
def main(target_date: str | None, dry_run: bool, db_path: str | None) -> None:
    """Embed chunk summaries into LanceDB using OpenAI text-embedding-3-large."""
    load_dotenv(CONFIG_DIR / ".env")

    jsonl_path = PROJECT_ROOT / "raw-chunks" / "all-chunks.jsonl"
    if not jsonl_path.exists():
        raise click.ClickException(f"No chunks found at {jsonl_path}")

    if db_path is None:
        db_path = str(PROJECT_ROOT / "lancedb" / "openai-v1")

    chunks = load_chunks_from_jsonl(jsonl_path)
    if target_date:
        chunks = [c for c in chunks if c["session_date"] == target_date]

    if not chunks:
        click.echo("No chunks to embed.")
        return

    if dry_run:
        click.echo(f"Would embed {len(chunks)} chunks into {db_path}")
        return

    click.echo(f"Embedding {len(chunks)} chunks into {db_path}...")
    count = embed_and_store(chunks=chunks, db_path=db_path)
    click.echo(f"Done. Embedded {count} new chunks.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
