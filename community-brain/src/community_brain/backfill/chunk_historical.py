"""Chunk historical Fathom transcripts into distribution-ready formats.

Usage:
    python -m community_brain.backfill.chunk_historical
    python -m community_brain.backfill.chunk_historical --date 2024-03-15
    python -m community_brain.backfill.chunk_historical --dry-run
"""

from __future__ import annotations

import json
import logging
import re
from datetime import date
from pathlib import Path

import click
from tqdm import tqdm

from community_brain.ingestion.registries import load_speaker_registry
from community_brain.chunk_utils import (
    _format_turn,
    chunk_to_markdown,
    chunk_transcript,
    chunks_to_jsonl,
    normalize_speaker,
    parse_transcript,
)

logger = logging.getLogger(__name__)

TIER_1_CUTOFF = "2026-03-10"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent


def _load_aliases(config_dir: Path) -> dict[str, str]:
    """Load speaker aliases from config."""
    aliases_path = config_dir / "speaker-aliases.yaml"
    if aliases_path.exists():
        return load_speaker_registry(aliases_path).as_flat_map()
    return {}


def _extract_date(filename: str) -> str | None:
    """Extract YYYY-MM-DD from a filename."""
    match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    return match.group(1) if match else None


def _extract_title(filename: str) -> str:
    """Extract title from filename like 2024-03-15-weekly-coaching-call.txt."""
    name = Path(filename).stem
    title_slug = re.sub(r"^\d{4}-\d{2}-\d{2}-?", "", name)
    if not title_slug:
        return "Coaching Call"
    return title_slug.replace("-", " ").title()


def chunk_single_session(
    transcript_path: Path,
    chunks_dir: Path,
    raw_chunks_path: Path,
    aliases: dict[str, str] | None = None,
    force: bool = False,
    use_llm: bool = True,
) -> dict | None:
    """Chunk a single transcript file.

    When use_llm=True (default), uses the two-pass LLM pipeline:
      Pass 1: Topic segmentation via LLM
      Pass 2: Chunk by topic boundaries with summaries

    When use_llm=False, falls back to v1 sliding-window chunker.

    Returns session metadata dict or None if skipped.
    """
    session_date = _extract_date(transcript_path.name)
    if not session_date:
        logger.warning("Cannot extract date from %s, skipping", transcript_path.name)
        return None

    session_title = _extract_title(transcript_path.name)

    session_chunk_dir = chunks_dir / session_date
    if session_chunk_dir.exists() and not force:
        logger.info("Skipped %s — already exists", session_date)
        return None

    text = transcript_path.read_text(encoding="utf-8")
    turns = parse_transcript(text)
    if not turns:
        logger.warning("No parseable turns in %s, skipping", transcript_path.name)
        return None

    if aliases:
        for turn in turns:
            turn.speaker = normalize_speaker(turn.speaker, aliases)

    if use_llm:
        from community_brain.topic_chunker import chunk_by_topics, segment_transcript

        # Format full transcript for LLM
        full_transcript = "\n".join(_format_turn(t) for t in turns)
        logger.info("Segmenting %s (%d turns)...", session_date, len(turns))
        topics = segment_transcript(full_transcript)
        logger.info("Found %d topics for %s", len(topics), session_date)

        # Chunk by topics
        chunks = chunk_by_topics(
            turns=turns,
            topics=topics,
            session_date=session_date,
            session_title=session_title,
            content_tier="historical",
            source="fathom_transcript",
        )
    else:
        chunks = chunk_transcript(
            turns,
            session_date=session_date,
            session_title=session_title,
            content_tier="historical",
            source="fathom_transcript",
        )

    if not chunks:
        logger.warning("No chunks produced for %s", session_date)
        return None

    # Write individual markdown files (one per chunk) for Open WebUI
    session_chunk_dir = chunks_dir / session_date
    session_chunk_dir.mkdir(parents=True, exist_ok=True)
    for chunk in chunks:
        # Slugify topic for filename
        topic_slug = re.sub(r"[^a-z0-9]+", "-", chunk.topic.lower()).strip("-") if chunk.topic else "chunk"
        filename = f"{chunk.chunk_id}-{topic_slug}.md"
        md_content = chunk_to_markdown(chunk)
        (session_chunk_dir / filename).write_text(md_content, encoding="utf-8")

    raw_chunks_path.parent.mkdir(parents=True, exist_ok=True)
    jsonl_content = chunks_to_jsonl(chunks)
    with open(raw_chunks_path, "a", encoding="utf-8") as f:
        f.write(jsonl_content)

    all_speakers = sorted(set(
        speaker
        for chunk in chunks
        for speaker in chunk.speakers_in_chunk
    ))

    return {
        "date": session_date,
        "title": session_title,
        "content_tier": "historical",
        "chunk_count": len(chunks),
        "speakers": all_speakers,
        "duration_minutes": None,
    }


def generate_manifest(sessions: list[dict], manifest_path: Path) -> None:
    """Generate manifest.json from a list of session metadata dicts."""
    sessions_sorted = sorted(sessions, key=lambda s: s["date"])
    total_chunks = sum(s["chunk_count"] for s in sessions_sorted)

    manifest = {
        "version": "1.0.0",
        "last_updated": date.today().isoformat(),
        "total_sessions": len(sessions_sorted),
        "total_chunks": total_chunks,
        "tier_1_cutoff": TIER_1_CUTOFF,
        "sessions": sessions_sorted,
    }

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


@click.command()
@click.option("--date", "target_date", default=None, help="Chunk a specific session (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="Show chunk counts without writing files")
@click.option("--force", is_flag=True, help="Re-chunk even if output already exists")
@click.option("--no-llm", is_flag=True, help="Use v1 sliding-window chunker instead of LLM pipeline")
def main(target_date: str | None, dry_run: bool, force: bool, no_llm: bool) -> None:
    """Chunk historical transcripts into markdown and JSONL."""
    raw_dir = PROJECT_ROOT / "raw-transcripts"
    chunks_dir = PROJECT_ROOT / "chunks" / "historical"
    raw_chunks_path = PROJECT_ROOT / "raw-chunks" / "all-chunks.jsonl"
    manifest_path = PROJECT_ROOT / "chunks" / "manifest.json"
    config_dir = PROJECT_ROOT / "config"

    if not raw_dir.exists():
        raise click.ClickException(f"No raw-transcripts directory found at {raw_dir}")

    aliases = _load_aliases(config_dir)

    transcript_files = sorted(raw_dir.glob("*.txt"))
    if target_date:
        transcript_files = [f for f in transcript_files if f.name.startswith(target_date)]

    tier1_files = []
    for f in transcript_files:
        file_date = _extract_date(f.name)
        if file_date and file_date < TIER_1_CUTOFF:
            tier1_files.append(f)

    if not tier1_files:
        click.echo("No Tier 1 transcripts found.")
        return

    if dry_run:
        click.echo(f"Found {len(tier1_files)} Tier 1 transcripts:")
        for f in tier1_files:
            text = f.read_text(encoding="utf-8")
            turns = parse_transcript(text)
            click.echo(f"  {f.name}: {len(turns)} turns")
        return

    if force:
        if raw_chunks_path.exists():
            raw_chunks_path.unlink()
        # Clean up old session directories
        import shutil
        for session_dir in chunks_dir.iterdir():
            if session_dir.is_dir() and _extract_date(session_dir.name):
                shutil.rmtree(session_dir)
        # Clean up old single-file format
        for old_file in chunks_dir.glob("session-*.md"):
            old_file.unlink()

    sessions = []
    for f in tqdm(tier1_files, desc="Chunking transcripts"):
        result = chunk_single_session(
            transcript_path=f,
            chunks_dir=chunks_dir,
            raw_chunks_path=raw_chunks_path,
            aliases=aliases,
            force=force,
            use_llm=not no_llm,
        )
        if result:
            sessions.append(result)

    all_sessions = list(sessions)
    # Scan for existing session directories from previous runs
    for session_dir in sorted(chunks_dir.iterdir()):
        if session_dir.is_dir() and _extract_date(session_dir.name):
            file_date = session_dir.name
            if not any(s["date"] == file_date for s in all_sessions):
                chunk_count = len(list(session_dir.glob("*.md")))
                all_sessions.append({
                    "date": file_date,
                    "title": "Coaching Call",
                    "content_tier": "historical",
                    "chunk_count": chunk_count,
                    "speakers": [],
                    "duration_minutes": None,
                })

    generate_manifest(all_sessions, manifest_path)

    click.echo(
        f"\nDone. Chunked {len(sessions)} sessions → "
        f"{sum(s['chunk_count'] for s in sessions)} chunks. "
        f"Manifest updated with {len(all_sessions)} total sessions."
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
