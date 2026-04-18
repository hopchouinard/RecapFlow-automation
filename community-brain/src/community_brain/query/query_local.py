"""CLI query tool using Ollama for embedding and inference.

Usage:
    python -m community_brain.query.query_local "What was discussed about Codex?"
    python -m community_brain.query.query_local "GPU benchmarks" --top-k 10 --verbose
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

import click
import lancedb
import ollama
from dotenv import load_dotenv

from community_brain.query import build_filter_expression

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
DEFAULT_DB_PATH = PROJECT_ROOT / "lancedb" / "nomic-v1"
EMBED_MODEL = "nomic-embed-text"
DEFAULT_LLM_MODEL = "gemma4:e4b"


def search_chunks(
    question: str,
    db_path: str,
    table_name: str = "transcripts",
    top_k: int = 5,
    filter_date: str | None = None,
    filter_speaker: str | None = None,
    ollama_base_url: str | None = None,
) -> list[dict]:
    """Embed the question and search LanceDB for similar chunks.

    Returns list of result dicts with chunk metadata + _distance score.
    """
    # Embed the question
    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.embed(model=EMBED_MODEL, input=[question])
    else:
        response = ollama.embed(model=EMBED_MODEL, input=[question])
    query_vector = response["embeddings"][0]

    # Search LanceDB
    db = lancedb.connect(db_path)
    table = db.open_table(table_name)

    query = table.search(query_vector).limit(top_k)

    # Apply filters (safely escaped)
    filter_expr = build_filter_expression(filter_date, filter_speaker)
    if filter_expr:
        query = query.where(filter_expr)

    results = query.to_arrow()
    # Convert Arrow table to list of dicts
    return [
        {col: results[col][i].as_py() for col in results.column_names}
        for i in range(results.num_rows)
    ]


def build_filter_expression_v2(filters: dict[str, Any] | None) -> str | None:
    """Build a LanceDB WHERE clause from the v2 filter dict.

    Semantics (per spec §7.1):
      - None or empty list → filter ignored
      - list-valued filters (entities, speakers_spoke, speakers_mentioned,
        keywords) use `_match` companion: "any" → OR, "all" → AND
      - require_chunk_markers / require_corpus_markers → AND of array_has
      - exclude_chunk_markers / exclude_corpus_markers → AND of NOT array_has
      - has_* and references_prior → bool equality when not None
      - schema_version_min → >= lexicographic comparison

    Returns None if no filter clauses apply.

    Known limitation (v1): filter values are interpolated directly into the
    WHERE clause string. A single quote in a value will break the query.
    Values containing special characters are not supported in v1.
    """
    if not filters:
        return None

    clauses: list[str] = []

    dr = filters.get("session_date_range")
    if dr and len(dr) == 2:
        clauses.append(f"session_date >= '{dr[0]}' AND session_date <= '{dr[1]}'")

    content_types = filters.get("content_type")
    if content_types:
        quoted = ", ".join(f"'{v}'" for v in content_types)
        clauses.append(f"content_type IN ({quoted})")

    for field_name in ("speakers_spoke", "speakers_mentioned", "entities", "keywords"):
        vals = filters.get(field_name)
        if not vals:
            continue
        match = filters.get(f"{field_name}_match", "any")
        parts = [f"array_has({field_name}, '{v}')" for v in vals]
        joiner = " AND " if match == "all" else " OR "
        clauses.append("(" + joiner.join(parts) + ")")

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
        "has_question", "has_answer", "has_unresolved_question",
        "has_insight", "references_prior",
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
    """Filter-then-rank v2 search against the new chunks table.

    Applies `build_filter_expression_v2(filters)` as a LanceDB WHERE clause
    first, then ranks the filtered rows by vector similarity to the embedded
    question. Per spec §7.1: filtering precedes ranking; ranking uses vector
    similarity alone in v1.

    Returns raw LanceDB row dicts (including `_distance`). The retrieval server
    translates these into the structured ground_truth/derived_metadata/provenance
    response shape.
    """
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


def format_results(results: list[dict], verbose: bool = False) -> str:
    """Format search results for display."""
    if not results:
        return "No results found."

    lines = ["Sources:"]
    for i, r in enumerate(results, 1):
        score = 1 - r.get("_distance", 0)  # convert distance to similarity
        lines.append(
            f"  [{i}] {r['session_date']} — {r['topic']} "
            f"({r['chunk_id']}) [similarity: {score:.2f}]"
        )
        if verbose:
            lines.append(f"      Summary: {r['summary']}")
            lines.append(f"      Text: {r['text'][:200]}...")
            lines.append("")

    return "\n".join(lines)


def build_answer_prompt(question: str, results: list[dict]) -> str:
    """Build the prompt for LLM answer generation with retrieved context."""
    context_parts = []
    for i, r in enumerate(results, 1):
        context_parts.append(
            f"[Source {i}] Session: {r['session_date']} | "
            f"Topic: {r['topic']}\n"
            f"Summary: {r['summary']}\n"
            f"Transcript:\n{r['text']}\n"
        )

    context = "\n---\n".join(context_parts)

    return (
        "You are answering questions about AI community coaching call transcripts. "
        "Use ONLY the provided sources to answer. Cite sources as [1], [2], etc.\n\n"
        f"## Sources\n\n{context}\n\n"
        f"## Question\n\n{question}\n\n"
        "## Answer\n\n"
    )


@click.command()
@click.argument("question")
@click.option("--top-k", default=5, help="Number of chunks to retrieve")
@click.option("--model", default=DEFAULT_LLM_MODEL, help="Ollama model for answer generation")
@click.option("--verbose", is_flag=True, help="Show retrieved chunks before the answer")
@click.option("--filter-date", default=None, help="Only search chunks from this date (YYYY-MM-DD)")
@click.option("--filter-speaker", default=None, help="Only search chunks containing this speaker")
@click.option("--db-path", default=None, help="Override LanceDB path")
def main(
    question: str,
    top_k: int,
    model: str,
    verbose: bool,
    filter_date: str | None,
    filter_speaker: str | None,
    db_path: str | None,
) -> None:
    """Query the Community Brain knowledge base using Ollama."""
    load_dotenv(CONFIG_DIR / ".env")
    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")

    if db_path is None:
        db_path = str(DEFAULT_DB_PATH)

    # Search
    click.echo(f"Searching for: {question}")
    results = search_chunks(
        question=question,
        db_path=db_path,
        top_k=top_k,
        filter_date=filter_date,
        filter_speaker=filter_speaker,
        ollama_base_url=ollama_base_url,
    )

    if not results:
        click.echo("No results found.")
        return

    if verbose:
        click.echo(f"\n{format_results(results, verbose=True)}\n")

    # Generate answer
    prompt = build_answer_prompt(question, results)

    click.echo("Generating answer...\n")
    if ollama_base_url:
        client = ollama.Client(host=ollama_base_url)
        response = client.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
    else:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )

    answer = response["message"]["content"]
    click.echo(f"Answer:\n{answer}")
    click.echo(f"\n{format_results(results, verbose=False)}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
