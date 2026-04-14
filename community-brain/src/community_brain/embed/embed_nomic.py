"""Embed chunk summaries into LanceDB using nomic-embed-text via Ollama.

Usage:
    python -m community_brain.embed.embed_nomic
    python -m community_brain.embed.embed_nomic --date 2025-09-02
    python -m community_brain.embed.embed_nomic --dry-run
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

import click
import lancedb
import ollama
from dotenv import load_dotenv
from tqdm import tqdm

logger = logging.getLogger(__name__)

NOMIC_DIMS = 768
NOMIC_MODEL = "nomic-embed-text"
BATCH_SIZE = 50
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
    """Convert chunk dicts to LanceDB-ready records.

    Converts speakers_in_chunk from list to JSON string for LanceDB compatibility.
    """
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


def _get_embeddings(summaries: list[str], ollama_base_url: str | None = None) -> list[list[float]]:
    """Get embeddings for a batch of summaries from Ollama."""
    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=NOMIC_MODEL, input=summaries)
    else:
        response = ollama.embed(model=NOMIC_MODEL, input=summaries)
    return response["embeddings"]


def embed_and_store(
    chunks: list[dict],
    db_path: str,
    table_name: str = "transcripts",
    ollama_base_url: str | None = None,
) -> int:
    """Embed chunk summaries and store in LanceDB.

    Returns the number of new chunks embedded.
    """
    db = lancedb.connect(db_path)
    records = build_lancedb_records(chunks)

    # Check for existing chunks to skip
    try:
        table = db.open_table(table_name)
        existing_ids = set(table.to_arrow()["chunk_id"].to_pylist())
        records = [r for r in records if r["chunk_id"] not in existing_ids]
        if not records:
            logger.info("All chunks already embedded, nothing to do.")
            return 0
        logger.info("Skipping %d already-embedded chunks", len(existing_ids))
    except Exception:
        # Table doesn't exist yet — will create it
        existing_ids = set()
        table = None

    # Embed in batches
    embedded_count = 0
    for i in tqdm(range(0, len(records), BATCH_SIZE), desc="Embedding"):
        batch = records[i : i + BATCH_SIZE]
        summaries = [r["summary"] or r["text"] for r in batch]

        # Get embeddings
        embeddings = _get_embeddings(summaries, ollama_base_url)

        # Add vector to each record
        for record, vector in zip(batch, embeddings):
            record["vector"] = vector

        # Insert into LanceDB
        if table is None:
            table = db.create_table(table_name, data=batch)
        else:
            table.add(batch)

        embedded_count += len(batch)

    logger.info("Embedded %d new chunks", embedded_count)
    return embedded_count


@click.command()
@click.option("--date", "target_date", default=None, help="Only embed chunks from this date (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="Show what would be embedded without doing it")
@click.option("--db-path", default=None, help="Override LanceDB path")
def main(target_date: str | None, dry_run: bool, db_path: str | None) -> None:
    """Embed chunk summaries into LanceDB using nomic-embed-text via Ollama."""
    load_dotenv(CONFIG_DIR / ".env")

    jsonl_path = PROJECT_ROOT / "raw-chunks" / "all-chunks.jsonl"
    if not jsonl_path.exists():
        raise click.ClickException(f"No chunks found at {jsonl_path}")

    if db_path is None:
        db_path = str(PROJECT_ROOT / "lancedb" / "nomic-v1")

    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")

    chunks = load_chunks_from_jsonl(jsonl_path)
    if target_date:
        chunks = [c for c in chunks if c["session_date"] == target_date]

    if not chunks:
        click.echo("No chunks to embed.")
        return

    if dry_run:
        click.echo(f"Would embed {len(chunks)} chunks into {db_path}")
        dates = sorted(set(c["session_date"] for c in chunks))
        for d in dates:
            count = sum(1 for c in chunks if c["session_date"] == d)
            click.echo(f"  {d}: {count} chunks")
        return

    click.echo(f"Embedding {len(chunks)} chunks into {db_path}...")
    count = embed_and_store(
        chunks=chunks,
        db_path=db_path,
        ollama_base_url=ollama_base_url,
    )
    click.echo(f"Done. Embedded {count} new chunks.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
