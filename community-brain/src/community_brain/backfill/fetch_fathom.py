"""Fetch coaching call transcripts from the Fathom API.

Usage:
    python -m community_brain.backfill.fetch_fathom
    python -m community_brain.backfill.fetch_fathom --after 2024-01-01 --before 2024-06-30
    python -m community_brain.backfill.fetch_fathom --dry-run
"""

from __future__ import annotations

import logging
import re
import time
from pathlib import Path

import click
import httpx
from dotenv import load_dotenv
from tqdm import tqdm

logger = logging.getLogger(__name__)

COACHING_TITLES = [
    "weekly coaching call",
    "ai developer accelerator — coaching call",
    "ai developer accelerator - coaching call",
]

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
RAW_TRANSCRIPTS_DIR = PROJECT_ROOT / "raw-transcripts"
CONFIG_DIR = PROJECT_ROOT / "config"


def is_coaching_call(title: str | None) -> bool:
    """Check if a meeting title matches known coaching call patterns."""
    if not title:
        return False
    return title.strip().lower() in COACHING_TITLES


def slugify_title(title: str) -> str:
    """Convert a title to a URL-safe slug."""
    slug = title.lower().strip()
    slug = re.sub(r"[—–]", "-", slug)
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def format_transcript_entries(entries: list[dict]) -> str:
    """Format Fathom API transcript entries into [HH:MM:SS] Speaker: text lines."""
    lines = []
    for entry in entries:
        speaker_obj = entry.get("speaker")
        if speaker_obj and isinstance(speaker_obj, dict):
            speaker = speaker_obj.get("display_name", "Unknown")
        else:
            speaker = "Unknown"
        timestamp = entry.get("timestamp", "00:00:00")
        text = entry.get("text", "")
        lines.append(f"[{timestamp}] {speaker}: {text}")
    return "\n".join(lines)


def _existing_dates(raw_dir: Path) -> set[str]:
    """Get set of dates that already have transcript files."""
    dates = set()
    if raw_dir.exists():
        for f in raw_dir.glob("*.txt"):
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
            if match:
                dates.add(match.group(1))
    return dates


def _wait_for_rate_limit(response: httpx.Response) -> None:
    """Sleep if rate limit is close to being hit."""
    remaining = response.headers.get("RateLimit-Remaining")
    reset = response.headers.get("RateLimit-Reset")
    if remaining is not None and int(remaining) < 5 and reset is not None:
        wait_seconds = int(reset) + 1
        logger.info("Rate limit low (%s remaining), waiting %ds", remaining, wait_seconds)
        time.sleep(wait_seconds)


def _api_get(
    client: httpx.Client,
    url: str,
    params: dict | None = None,
    retries: int = 3,
) -> httpx.Response:
    """GET with retry and rate-limit handling."""
    for attempt in range(retries):
        try:
            response = client.get(url, params=params)
            if response.status_code == 429:
                reset = response.headers.get("RateLimit-Reset", "5")
                wait = int(reset) + 1
                logger.warning("Rate limited (429), waiting %ds", wait)
                time.sleep(wait)
                continue
            response.raise_for_status()
            _wait_for_rate_limit(response)
            return response
        except httpx.HTTPError as e:
            if attempt < retries - 1:
                backoff = 2 ** attempt
                logger.warning("Request failed (%s), retrying in %ds", e, backoff)
                time.sleep(backoff)
            else:
                raise
    raise RuntimeError("Exhausted retries")


def fetch_all_meetings(
    client: httpx.Client,
    base_url: str,
    after: str | None = None,
    before: str | None = None,
) -> list[dict]:
    """Page through all meetings from the Fathom API."""
    meetings = []
    params: dict = {}
    if after:
        params["created_after"] = after
    if before:
        params["created_before"] = before

    url = f"{base_url}/meetings"
    while True:
        response = _api_get(client, url, params=params)
        data = response.json()
        items = data.get("items", data) if isinstance(data, dict) else data
        if isinstance(items, list):
            meetings.extend(items)

        next_cursor = data.get("next_cursor") if isinstance(data, dict) else None
        if not next_cursor:
            break
        params["cursor"] = next_cursor

    return meetings


def fetch_transcript(
    client: httpx.Client,
    base_url: str,
    recording_id: str,
) -> list[dict]:
    """Fetch transcript entries for a specific recording."""
    response = _api_get(client, f"{base_url}/recordings/{recording_id}/transcript")
    data = response.json()
    # API returns {"transcript": [...]} — extract the inner list
    if isinstance(data, dict) and "transcript" in data:
        return data["transcript"]
    return data


@click.command()
@click.option("--after", default=None, help="Fetch meetings created after this date (YYYY-MM-DD)")
@click.option("--before", default=None, help="Fetch meetings created before this date (YYYY-MM-DD)")
@click.option("--dry-run", is_flag=True, help="List what would be fetched without downloading")
def main(after: str | None, before: str | None, dry_run: bool) -> None:
    """Fetch coaching call transcripts from the Fathom API."""
    import os

    load_dotenv(CONFIG_DIR / ".env")
    api_key = os.environ.get("FATHOM_API_KEY")
    if not api_key:
        raise click.ClickException("FATHOM_API_KEY not set. Copy config/.env.example to config/.env and fill it in.")

    base_url = "https://api.fathom.ai/external/v1"
    RAW_TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    existing = _existing_dates(RAW_TRANSCRIPTS_DIR)

    client = httpx.Client(
        headers={"X-Api-Key": api_key},
        timeout=30.0,
    )

    try:
        logger.info("Fetching meeting list from Fathom API...")
        meetings = fetch_all_meetings(client, base_url, after=after, before=before)
        logger.info("Found %d meetings total", len(meetings))

        coaching_calls = []
        for m in meetings:
            title = m.get("title", "")
            if is_coaching_call(title):
                coaching_calls.append(m)
            else:
                logger.info("Ignored: %s — %r (not a coaching call)", m.get("date", "?"), title)

        logger.info("Found %d coaching calls", len(coaching_calls))

        if dry_run:
            for m in coaching_calls:
                date = m.get("date", m.get("recording_start_time", "unknown"))[:10]
                title = m.get("title", "Untitled")
                status = "SKIP (exists)" if date in existing else "FETCH"
                click.echo(f"  [{status}] {date} — {title}")
            return

        fetched = 0
        skipped = 0
        total = len(coaching_calls)

        for m in tqdm(coaching_calls, desc="Fetching transcripts"):
            date = m.get("date", m.get("recording_start_time", "unknown"))[:10]
            title = m.get("title", "Untitled")
            recording_id = str(m.get("recording_id", m.get("id", "")))

            if date in existing:
                logger.info("Skipped %s — already exists", date)
                skipped += 1
                continue

            if not recording_id:
                logger.warning("No recording_id for %s — %s, skipping", date, title)
                continue

            try:
                entries = fetch_transcript(client, base_url, recording_id)
                formatted = format_transcript_entries(entries)
                slug = slugify_title(title)
                filename = f"{date}-{slug}.txt"
                (RAW_TRANSCRIPTS_DIR / filename).write_text(formatted, encoding="utf-8")
                fetched += 1
                existing.add(date)
                logger.info(
                    "Fetched %d/%d: %s — %s (%d entries)",
                    fetched, total - skipped, date, title, len(entries),
                )
            except Exception:
                logger.exception("Failed to fetch transcript for %s — %s", date, title)

        click.echo(f"\nDone. Fetched: {fetched}, Skipped: {skipped}, Errors: {total - fetched - skipped}")

    finally:
        client.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
