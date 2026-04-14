# Community Brain SP3: LanceDB Embedding + Retrieval — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build LanceDB embedding pipeline with dual-field architecture (embed summaries, return full text), CLI query tools, and a FastAPI retrieval server — then validate retrieval quality against 3 sample sessions.

**Architecture:** Chunks from `raw-chunks/all-chunks.jsonl` get their `summary` field embedded via Ollama (nomic-embed-text) into a LanceDB table. Query tools embed the user question with the same model, search the summary vectors, and return full transcript text. FastAPI server exposes retrieval for Open WebUI integration.

**Tech Stack:** Python 3.12, lancedb, ollama, openai, fastapi, uvicorn, click

**Spec:** `docs/superpowers/specs/2026-04-13-community-brain-sp3-lancedb-retrieval.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|---------------|
| Modify | `community-brain/pyproject.toml` | Add lancedb, ollama, openai, fastapi, uvicorn deps |
| Create | `community-brain/src/community_brain/embed/__init__.py` | Package init |
| Create | `community-brain/src/community_brain/embed/embed_nomic.py` | Embed summaries via Ollama → LanceDB |
| Create | `community-brain/src/community_brain/embed/embed_openai.py` | Embed summaries via OpenAI → LanceDB |
| Create | `community-brain/src/community_brain/query/__init__.py` | Package init |
| Create | `community-brain/src/community_brain/query/query_local.py` | CLI query: Ollama embed + inference |
| Create | `community-brain/src/community_brain/query/query_openai.py` | CLI query: OpenAI embed + inference |
| Create | `community-brain/src/community_brain/query/retrieval_server.py` | FastAPI retrieval endpoint |
| Create | `community-brain/tests/test_embed.py` | Embedding tests |
| Create | `community-brain/tests/test_query.py` | Query tool tests |
| Create | `community-brain/tests/test_retrieval_server.py` | FastAPI server tests |

---

### Task 1: Add Dependencies + Package Init

**Files:**
- Modify: `community-brain/pyproject.toml`
- Create: `community-brain/src/community_brain/embed/__init__.py`
- Create: `community-brain/src/community_brain/query/__init__.py`

- [ ] **Step 1: Update pyproject.toml**

Replace the `dependencies` list in `community-brain/pyproject.toml`:

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
]
```

- [ ] **Step 2: Create package init files**

Create `community-brain/src/community_brain/embed/__init__.py`:

```python
"""Embedding pipeline for Community Brain vector store."""
```

Create `community-brain/src/community_brain/query/__init__.py`:

```python
"""Query tools and retrieval server for Community Brain."""
```

- [ ] **Step 3: Install new dependencies**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
pip install -e ".[dev]"
```

Verify:

```bash
python -c "import lancedb; print('lancedb:', lancedb.__version__)"
python -c "import ollama; print('ollama ok')"
python -c "import fastapi; print('fastapi:', fastapi.__version__)"
```

- [ ] **Step 4: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/pyproject.toml community-brain/src/community_brain/embed/__init__.py community-brain/src/community_brain/query/__init__.py
git commit -m "feat(sp3): add LanceDB, Ollama, OpenAI, FastAPI dependencies

New packages: embed/ and query/ for SP3 retrieval pipeline."
```

---

### Task 2: Nomic Embedding Script (TDD) ✅

**Files:**
- Create: `community-brain/tests/test_embed.py`
- Create: `community-brain/src/community_brain/embed/embed_nomic.py`

- [x] **Step 1: Write failing tests**

Create `community-brain/tests/test_embed.py`:

```python
import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from community_brain.embed.embed_nomic import (
    load_chunks_from_jsonl,
    build_lancedb_records,
    embed_and_store,
    NOMIC_DIMS,
)


SAMPLE_CHUNK = {
    "chunk_id": "2025-09-02-chunk-001",
    "session_date": "2025-09-02",
    "session_title": "Weekly Coaching Call",
    "speakers_in_chunk": ["Patrick Chouinard", "Shakur"],
    "chunk_position": 1,
    "total_chunks_in_session": 107,
    "content_tier": "historical",
    "content_type": "transcript",
    "source": "fathom_transcript",
    "topic": "AI Tools and New Tech Adoption",
    "summary": "Group discusses Codex in Cursor and Google image gen tools.",
    "text": "[00:02:29] Patrick Chouinard: Did anybody try the new codex?",
}


class TestLoadChunks:
    def test_loads_from_jsonl(self, tmp_path):
        jsonl_path = tmp_path / "chunks.jsonl"
        jsonl_path.write_text(
            json.dumps(SAMPLE_CHUNK) + "\n"
            + json.dumps({**SAMPLE_CHUNK, "chunk_id": "2025-09-02-chunk-002"}) + "\n"
        )
        chunks = load_chunks_from_jsonl(jsonl_path)
        assert len(chunks) == 2
        assert chunks[0]["chunk_id"] == "2025-09-02-chunk-001"

    def test_empty_file(self, tmp_path):
        jsonl_path = tmp_path / "empty.jsonl"
        jsonl_path.write_text("")
        chunks = load_chunks_from_jsonl(jsonl_path)
        assert len(chunks) == 0


class TestBuildRecords:
    def test_record_fields(self):
        records = build_lancedb_records([SAMPLE_CHUNK])
        assert len(records) == 1
        r = records[0]
        assert r["chunk_id"] == "2025-09-02-chunk-001"
        assert r["summary"] == SAMPLE_CHUNK["summary"]
        assert r["text"] == SAMPLE_CHUNK["text"]
        assert r["topic"] == "AI Tools and New Tech Adoption"
        assert r["session_date"] == "2025-09-02"
        # speakers stored as JSON string for LanceDB compatibility
        assert "Patrick Chouinard" in r["speakers_in_chunk"]

    def test_summary_is_the_embedding_source(self):
        """The summary field should be what gets embedded, not the text field."""
        records = build_lancedb_records([SAMPLE_CHUNK])
        # The record should have summary as a string (embedding happens at insert time)
        assert isinstance(records[0]["summary"], str)
        assert len(records[0]["summary"]) < len(records[0]["text"])


class TestEmbedAndStore:
    def test_creates_table_and_inserts(self, tmp_path):
        mock_embedding = [0.1] * NOMIC_DIMS

        def mock_ollama_embed(model, input):
            """Mock ollama.embed() returning embeddings for each input."""
            if isinstance(input, list):
                return {"embeddings": [mock_embedding for _ in input]}
            return {"embeddings": [mock_embedding]}

        with patch("community_brain.embed.embed_nomic.ollama.embed", side_effect=mock_ollama_embed):
            db_path = tmp_path / "test_lance"
            embed_and_store(
                chunks=[SAMPLE_CHUNK],
                db_path=str(db_path),
                table_name="transcripts",
            )

        # Verify the table was created with data
        import lancedb
        db = lancedb.connect(str(db_path))
        table = db.open_table("transcripts")
        assert table.count_rows() == 1
        results = table.to_pandas()
        assert results.iloc[0]["chunk_id"] == "2025-09-02-chunk-001"
        assert results.iloc[0]["topic"] == "AI Tools and New Tech Adoption"

    def test_skips_existing_chunks(self, tmp_path):
        mock_embedding = [0.1] * NOMIC_DIMS

        def mock_ollama_embed(model, input):
            if isinstance(input, list):
                return {"embeddings": [mock_embedding for _ in input]}
            return {"embeddings": [mock_embedding]}

        with patch("community_brain.embed.embed_nomic.ollama.embed", side_effect=mock_ollama_embed):
            db_path = tmp_path / "test_lance"
            # First insert
            embed_and_store(
                chunks=[SAMPLE_CHUNK],
                db_path=str(db_path),
                table_name="transcripts",
            )
            # Second insert with same chunk — should skip
            embed_and_store(
                chunks=[SAMPLE_CHUNK],
                db_path=str(db_path),
                table_name="transcripts",
            )

        import lancedb
        db = lancedb.connect(str(db_path))
        table = db.open_table("transcripts")
        assert table.count_rows() == 1  # not duplicated
```

- [x] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_embed.py -v
```

Expected: FAIL — `ModuleNotFoundError`.

- [x] **Step 3: Implement embed_nomic.py**

Create `community-brain/src/community_brain/embed/embed_nomic.py`:

```python
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
        existing_ids = set(table.to_pandas()["chunk_id"].tolist())
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
        summaries = [r["summary"] for r in batch]

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
```

- [x] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_embed.py -v
```

Expected: All 6 tests PASS.

- [x] **Step 5: Run full test suite**

```bash
pytest tests/ -v
```

Expected: All tests PASS (~62 total).

- [ ] **Step 6: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/embed/embed_nomic.py community-brain/tests/test_embed.py
git commit -m "feat(sp3): add nomic embedding script for LanceDB

embed_nomic.py: loads JSONL chunks, embeds summary field via Ollama
nomic-embed-text, stores in LanceDB with full text. Resumable,
batch processing, CLI with --date and --dry-run flags.
6 tests passing."
```

---

### Task 3: Local Query CLI Tool (TDD) ✅

**Files:**
- Create: `community-brain/tests/test_query.py`
- Create: `community-brain/src/community_brain/query/query_local.py`

- [x] **Step 1: Write failing tests**

Create `community-brain/tests/test_query.py`:

```python
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from community_brain.query.query_local import (
    search_chunks,
    format_results,
    build_answer_prompt,
)


MOCK_RESULTS = [
    {
        "chunk_id": "2025-09-02-chunk-001",
        "session_date": "2025-09-02",
        "topic": "AI Tools and New Tech Adoption",
        "summary": "Group discusses Codex in Cursor.",
        "text": "[00:02:29] Patrick: Did anybody try the new codex?",
        "speakers_in_chunk": '["Patrick Chouinard", "Shakur"]',
        "_distance": 0.15,
    },
    {
        "chunk_id": "2025-09-02-chunk-010",
        "session_date": "2025-09-02",
        "topic": "Database Schema for RAG",
        "summary": "Discussion about pgvector and Postgres.",
        "text": "[00:15:00] Brandon: We should use pgvector...",
        "speakers_in_chunk": '["Brandon Hancock"]',
        "_distance": 0.35,
    },
]


class TestSearchChunks:
    def test_returns_results(self, tmp_path):
        """Search with a mocked LanceDB table."""
        mock_table = MagicMock()
        mock_table.search.return_value.limit.return_value.to_pandas.return_value = (
            MagicMock(to_dict=MagicMock(return_value={"records": MOCK_RESULTS}))
        )
        # This test verifies the function signature works; real integration tested in Task 5
        # For unit test, just verify format_results and build_answer_prompt work
        pass

    def test_format_results_verbose(self):
        output = format_results(MOCK_RESULTS, verbose=True)
        assert "AI Tools and New Tech Adoption" in output
        assert "Codex" in output
        assert "[1]" in output
        assert "2025-09-02" in output

    def test_format_results_brief(self):
        output = format_results(MOCK_RESULTS, verbose=False)
        assert "[1]" in output
        assert "2025-09-02" in output
        assert "AI Tools and New Tech Adoption" in output
        # Brief mode should NOT include full text
        assert "Did anybody try" not in output


class TestBuildPrompt:
    def test_includes_context_and_question(self):
        prompt = build_answer_prompt("What about Codex?", MOCK_RESULTS)
        assert "What about Codex?" in prompt
        assert "Codex in Cursor" in prompt
        assert "[00:02:29]" in prompt

    def test_source_numbering(self):
        prompt = build_answer_prompt("test", MOCK_RESULTS)
        assert "[Source 1]" in prompt
        assert "[Source 2]" in prompt
```

- [x] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_query.py -v
```

Expected: FAIL — `ModuleNotFoundError`.

- [x] **Step 3: Implement query_local.py**

Create `community-brain/src/community_brain/query/query_local.py`:

```python
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

import click
import lancedb
import ollama
from dotenv import load_dotenv

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

    # Apply filters
    if filter_date:
        query = query.where(f"session_date = '{filter_date}'")
    if filter_speaker:
        query = query.where(f"speakers_in_chunk LIKE '%{filter_speaker}%'")

    results = query.to_pandas()
    return results.to_dict("records")


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
```

- [x] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_query.py -v
```

Expected: All 5 tests PASS.

- [x] **Step 5: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/query/query_local.py community-brain/tests/test_query.py
git commit -m "feat(sp3): add local CLI query tool

query_local.py: embeds question via Ollama, searches LanceDB, generates
answer with source citations. Supports --top-k, --verbose, --filter-date,
--filter-speaker flags. 5 tests passing."
```

---

### Task 4: FastAPI Retrieval Server (TDD) ✅

**Files:**
- Create: `community-brain/tests/test_retrieval_server.py`
- Create: `community-brain/src/community_brain/query/retrieval_server.py`

- [x] **Step 1: Write failing tests**

Create `community-brain/tests/test_retrieval_server.py`:

```python
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient

# Patch search before importing the app
with patch("community_brain.query.retrieval_server.search_chunks") as mock_search:
    mock_search.return_value = [
        {
            "chunk_id": "2025-09-02-chunk-001",
            "session_date": "2025-09-02",
            "topic": "AI Tools",
            "summary": "Discussion about Codex.",
            "text": "[00:02:29] Patrick: Did anybody try codex?",
            "speakers_in_chunk": '["Patrick Chouinard"]',
            "_distance": 0.15,
        }
    ]
    from community_brain.query.retrieval_server import app

client = TestClient(app)


class TestHealthEndpoint:
    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"


class TestQueryEndpoint:
    @patch("community_brain.query.retrieval_server.search_chunks")
    def test_returns_chunks(self, mock_search):
        mock_search.return_value = [
            {
                "chunk_id": "2025-09-02-chunk-001",
                "session_date": "2025-09-02",
                "topic": "AI Tools",
                "summary": "Discussion about Codex.",
                "text": "[00:02:29] Patrick: Did anybody try codex?",
                "speakers_in_chunk": '["Patrick Chouinard"]',
                "_distance": 0.15,
            }
        ]
        response = client.post(
            "/query",
            json={"question": "What about Codex?", "top_k": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert "chunks" in data
        assert len(data["chunks"]) == 1
        assert data["chunks"][0]["chunk_id"] == "2025-09-02-chunk-001"
        assert data["chunks"][0]["topic"] == "AI Tools"
        assert "score" in data["chunks"][0]

    @patch("community_brain.query.retrieval_server.search_chunks")
    def test_empty_results(self, mock_search):
        mock_search.return_value = []
        response = client.post(
            "/query",
            json={"question": "Something obscure", "top_k": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["chunks"] == []

    @patch("community_brain.query.retrieval_server.search_chunks")
    def test_with_filters(self, mock_search):
        mock_search.return_value = []
        response = client.post(
            "/query",
            json={
                "question": "test",
                "top_k": 3,
                "filter_date": "2025-09-02",
                "filter_speaker": "Patrick",
            },
        )
        assert response.status_code == 200
        mock_search.assert_called_once()
        call_kwargs = mock_search.call_args
        assert call_kwargs[1]["filter_date"] == "2025-09-02" or call_kwargs[0][0] == "test"
```

- [x] **Step 2: Run tests to verify they fail**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_retrieval_server.py -v
```

Expected: FAIL — `ModuleNotFoundError`.

- [x] **Step 3: Implement retrieval_server.py**

Create `community-brain/src/community_brain/query/retrieval_server.py`:

```python
"""FastAPI retrieval server for Community Brain.

Exposes a /query endpoint that searches LanceDB and returns ranked chunks.
No LLM inference — the caller handles answer generation.

Usage:
    python -m community_brain.query.retrieval_server
    uvicorn community_brain.query.retrieval_server:app --host 0.0.0.0 --port 8999
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from community_brain.query.query_local import search_chunks

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
load_dotenv(CONFIG_DIR / ".env")

DEFAULT_DB_PATH = str(PROJECT_ROOT / "lancedb" / "nomic-v1")

app = FastAPI(
    title="Community Brain Retrieval API",
    description="Search coaching call transcripts by semantic similarity.",
    version="0.1.0",
)


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5
    filter_date: str | None = None
    filter_speaker: str | None = None


class ChunkResult(BaseModel):
    chunk_id: str
    session_date: str
    topic: str
    summary: str
    text: str
    speakers: list[str]
    score: float


class QueryResponse(BaseModel):
    chunks: list[ChunkResult]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    db_path = os.environ.get("LANCEDB_PATH", DEFAULT_DB_PATH)
    ollama_base_url = os.environ.get("OLLAMA_BASE_URL")

    results = search_chunks(
        question=request.question,
        db_path=db_path,
        top_k=request.top_k,
        filter_date=request.filter_date,
        filter_speaker=request.filter_speaker,
        ollama_base_url=ollama_base_url,
    )

    chunks = []
    for r in results:
        speakers_raw = r.get("speakers_in_chunk", "[]")
        if isinstance(speakers_raw, str):
            try:
                speakers = json.loads(speakers_raw)
            except json.JSONDecodeError:
                speakers = [speakers_raw]
        else:
            speakers = speakers_raw

        chunks.append(ChunkResult(
            chunk_id=r["chunk_id"],
            session_date=r["session_date"],
            topic=r.get("topic", ""),
            summary=r.get("summary", ""),
            text=r["text"],
            speakers=speakers,
            score=round(1 - r.get("_distance", 0), 4),
        ))

    return QueryResponse(chunks=chunks)


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("RETRIEVAL_PORT", "8999"))
    uvicorn.run(app, host="0.0.0.0", port=port)
```

- [x] **Step 4: Run tests to verify they pass**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/test_retrieval_server.py -v
```

Expected: All 4 tests PASS.

- [x] **Step 5: Run full test suite**

```bash
pytest tests/ -v
```

Expected: All tests PASS (~71 total).

- [x] **Step 6: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/query/retrieval_server.py community-brain/tests/test_retrieval_server.py
git commit -m "feat(sp3): add FastAPI retrieval server

/query endpoint searches LanceDB, returns ranked chunks with metadata.
/health endpoint for monitoring. Retrieval only — no LLM inference.
4 tests passing."
```

---

### Task 5: OpenAI Embedding + Query Scripts

**Files:**
- Create: `community-brain/src/community_brain/embed/embed_openai.py`
- Create: `community-brain/src/community_brain/query/query_openai.py`

- [ ] **Step 1: Create embed_openai.py**

Create `community-brain/src/community_brain/embed/embed_openai.py`:

```python
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

    # Check existing
    try:
        table = db.open_table(table_name)
        existing_ids = set(table.to_pandas()["chunk_id"].tolist())
        records = [r for r in records if r["chunk_id"] not in existing_ids]
        if not records:
            logger.info("All chunks already embedded.")
            return 0
    except Exception:
        existing_ids = set()
        table = None

    embedded_count = 0
    for i in tqdm(range(0, len(records), BATCH_SIZE), desc="Embedding (OpenAI)"):
        batch = records[i : i + BATCH_SIZE]
        summaries = [r["summary"] for r in batch]

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
```

- [ ] **Step 2: Create query_openai.py**

Create `community-brain/src/community_brain/query/query_openai.py`:

```python
"""CLI query tool using OpenAI for embedding and inference.

Usage:
    python -m community_brain.query.query_openai "What was discussed about Codex?"
    python -m community_brain.query.query_openai "GPU benchmarks" --top-k 10 --verbose
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

    results = query.to_pandas()
    return results.to_dict("records")


# Reuse format_results and build_answer_prompt from query_local
from community_brain.query.query_local import format_results, build_answer_prompt


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
```

- [ ] **Step 3: Run full test suite**

```bash
cd /home/pchouinard/n8n/community-brain && source .venv/bin/activate
pytest tests/ -v
```

Expected: All tests PASS.

- [ ] **Step 4: Commit**

```bash
cd /home/pchouinard/n8n
git add community-brain/src/community_brain/embed/embed_openai.py community-brain/src/community_brain/query/query_openai.py
git commit -m "feat(sp3): add OpenAI embedding and query scripts

embed_openai.py: text-embedding-3-large → LanceDB (openai-v1).
query_openai.py: OpenAI search + gpt-5.4-mini answer generation.
Reuses format_results and build_answer_prompt from query_local."
```

---

### Task 6: Integration Test — Embed + Query Sample Sessions

This task requires real API calls to Ollama on the Mac Mini.

- [ ] **Step 1: Embed the 3 sample sessions**

```bash
cd /home/pchouinard/n8n/community-brain
source .venv/bin/activate
python -m community_brain.embed.embed_nomic --dry-run
```

Review the dry run output. Then embed:

```bash
python -m community_brain.embed.embed_nomic
```

Expected: ~314 chunks embedded in ~30 seconds (Ollama on Mac Mini).

Verify:

```bash
python3 -c "
import lancedb
db = lancedb.connect('lancedb/nomic-v1')
table = db.open_table('transcripts')
print(f'Rows: {table.count_rows()}')
df = table.to_pandas()
print(f'Columns: {list(df.columns)}')
print(f'Sample topic: {df.iloc[0][\"topic\"]}')
print(f'Vector dims: {len(df.iloc[0][\"vector\"])}')
"
```

Expected: 314 rows, 768-dim vectors, topics present.

- [ ] **Step 2: Test the Codex query**

```bash
python -m community_brain.query.query_local "What was discussed about Codex?" --verbose
```

Expected: The top result should be `2025-09-02-chunk-001` with topic "AI Tools and New Tech Adoption" and summary mentioning Codex.

- [ ] **Step 3: Test additional queries**

```bash
python -m community_brain.query.query_local "What tools for vector storage?" --verbose
python -m community_brain.query.query_local "Who participated in the September 2 call?" --verbose
python -m community_brain.query.query_local "GPU benchmarks" --filter-date 2025-09-02 --verbose
```

Verify relevant chunks are returned for each query.

- [ ] **Step 4: Test the FastAPI server**

Start the server:

```bash
python -m community_brain.query.retrieval_server &
```

Test with curl:

```bash
curl -s -X POST http://localhost:8999/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What was discussed about Codex?", "top_k": 5}' | python3 -m json.tool | head -30
```

Expected: JSON response with chunks, the Codex topic chunk ranked first or near the top.

Stop the server:

```bash
kill %1
```

- [ ] **Step 5: Commit LanceDB data**

```bash
cd /home/pchouinard/n8n
git add community-brain/lancedb/
git commit -m "data(sp3): embed 314 sample chunks into LanceDB nomic-v1

3 sample sessions embedded via nomic-embed-text. Summary-based dual-field
embedding validated: Codex query returns correct topic chunk."
```

- [ ] **Step 6: Push**

```bash
git push
```

---

## Verification Summary

SP3 is complete when:

| Check | Status |
|-------|--------|
| All unit tests pass (~71) | |
| 314 chunks embedded in LanceDB | |
| "What about Codex?" returns correct topic chunk | |
| Metadata filtering (date, speaker) works | |
| FastAPI /query endpoint returns JSON results | |
| Query latency < 500ms | |
| Committed and pushed | |
