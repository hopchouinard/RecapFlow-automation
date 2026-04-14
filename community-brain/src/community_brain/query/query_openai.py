"""CLI query tool using OpenAI for embedding and inference.

Usage:
    python -m community_brain.query.query_openai "What was discussed about Codex?"
    python -m community_brain.query.query_openai "GPU benchmarks" --top-k 10 --verbose
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

import click
import lancedb
from dotenv import load_dotenv
from openai import OpenAI

from community_brain.query.query_local import format_results, build_answer_prompt

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
DEFAULT_DB_PATH = PROJECT_ROOT / "lancedb" / "openai-v1"
EMBED_MODEL = "text-embedding-3-large"
DEFAULT_LLM_MODEL = "gpt-5.4-mini"


def search_chunks(
    question: str,
    db_path: str,
    table_name: str = "transcripts",
    top_k: int = 5,
    filter_date: str | None = None,
    filter_speaker: str | None = None,
    api_key: str | None = None,
) -> list[dict]:
    """Embed the question via OpenAI and search LanceDB."""
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(model=EMBED_MODEL, input=[question])
    query_vector = response.data[0].embedding

    db = lancedb.connect(db_path)
    table = db.open_table(table_name)
    query = table.search(query_vector).limit(top_k)

    if filter_date:
        query = query.where(f"session_date = '{filter_date}'")
    if filter_speaker:
        query = query.where(f"speakers_in_chunk LIKE '%{filter_speaker}%'")

    results = query.to_arrow()
    return [
        {col: results[col][i].as_py() for col in results.column_names}
        for i in range(results.num_rows)
    ]


@click.command()
@click.argument("question")
@click.option("--top-k", default=5, help="Number of chunks to retrieve")
@click.option("--model", default=DEFAULT_LLM_MODEL, help="OpenAI model for answer generation")
@click.option("--verbose", is_flag=True, help="Show retrieved chunks before the answer")
@click.option("--filter-date", default=None, help="Only search chunks from this date")
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
    """Query the Community Brain knowledge base using OpenAI."""
    load_dotenv(CONFIG_DIR / ".env")

    if db_path is None:
        db_path = str(DEFAULT_DB_PATH)

    click.echo(f"Searching for: {question}")
    results = search_chunks(
        question=question,
        db_path=db_path,
        top_k=top_k,
        filter_date=filter_date,
        filter_speaker=filter_speaker,
    )

    if not results:
        click.echo("No results found.")
        return

    if verbose:
        click.echo(f"\n{format_results(results, verbose=True)}\n")

    prompt = build_answer_prompt(question, results)

    click.echo("Generating answer...\n")
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content
    click.echo(f"Answer:\n{answer}")
    click.echo(f"\n{format_results(results, verbose=False)}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
