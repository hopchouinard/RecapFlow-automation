"""Topic-aware chunking for Community Brain transcripts.

Two-pass pipeline:
  Pass 1: LLM segments transcript into discussion topics
  Pass 2: Chunks by topic boundaries, generates summaries
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from community_brain.chunk_utils import (
    Chunk,
    SpeakerTurn,
    _format_turn,
    chunk_transcript,
    count_tokens,
)
from community_brain.llm import call_llm, call_llm_json

logger = logging.getLogger(__name__)

SEGMENTATION_PROMPT = """You are segmenting a coaching call transcript into discussion topics.

For each distinct topic discussed, provide:
- topic_title: A short descriptive title (5-10 words)
- start_timestamp: The [HH:MM:SS] where this topic begins
- end_timestamp: The [HH:MM:SS] where this topic ends
- summary: 1-2 sentence summary of what was discussed

Rules:
- A topic is a coherent discussion thread (e.g., "Trying Codex in Cursor", "GPU benchmarks for local models")
- Greetings, small talk, and transitions between topics are NOT separate topics — attach them to the adjacent topic
- If a topic is briefly interrupted and resumed, treat it as one topic
- Aim for 5-20 topics per hour of conversation
- Output as a JSON array only, no other text

Transcript:
{transcript_text}"""

SUB_SUMMARY_PROMPT = """Summarize this section of a coaching call transcript in 1-2 sentences.
Focus on the specific points discussed, tools mentioned, and conclusions reached.

Topic: {topic_title}
Transcript section:
{chunk_text}"""


@dataclass
class Topic:
    """A discussion topic identified by LLM segmentation."""
    topic_title: str
    start_timestamp: str
    end_timestamp: str
    summary: str


def build_segmentation_prompt(transcript_text: str) -> str:
    """Build the prompt for topic segmentation."""
    return SEGMENTATION_PROMPT.format(transcript_text=transcript_text)


def parse_segmentation_response(response: list[dict]) -> list[Topic]:
    """Parse the LLM's JSON response into Topic objects."""
    topics = []
    for item in response:
        topics.append(Topic(
            topic_title=item.get("topic_title", "Untitled"),
            start_timestamp=item.get("start_timestamp", ""),
            end_timestamp=item.get("end_timestamp", ""),
            summary=item.get("summary", ""),
        ))
    return topics


def segment_transcript(transcript_text: str) -> list[Topic]:
    """Pass 1: Send full transcript to LLM for topic segmentation.

    Returns a list of Topic objects with timestamp boundaries and summaries.
    """
    prompt = build_segmentation_prompt(transcript_text)
    response = call_llm_json(prompt)
    if not isinstance(response, list):
        response = [response]
    topics = parse_segmentation_response(response)
    logger.info("Segmented transcript into %d topics", len(topics))
    return topics


def extract_turns_for_topic(
    turns: list[SpeakerTurn],
    topic: Topic,
) -> list[SpeakerTurn]:
    """Extract speaker turns that fall within a topic's timestamp range."""
    result = []
    for turn in turns:
        if topic.start_timestamp <= turn.timestamp <= topic.end_timestamp:
            result.append(turn)
    return result


def _generate_sub_summary(topic_title: str, chunk_text: str) -> str:
    """Generate a summary for a sub-chunk of an oversized topic."""
    prompt = SUB_SUMMARY_PROMPT.format(
        topic_title=topic_title,
        chunk_text=chunk_text,
    )
    return call_llm(prompt)


def chunk_by_topics(
    turns: list[SpeakerTurn],
    topics: list[Topic],
    session_date: str,
    session_title: str,
    content_tier: str = "historical",
    source: str = "fathom_transcript",
    max_topic_tokens: int = 800,
) -> list[Chunk]:
    """Pass 2: Chunk transcript by topic boundaries with summaries.

    For each topic:
    - If total tokens <= max_topic_tokens: one chunk, use topic summary
    - If > max_topic_tokens: sub-split using chunk_transcript(), generate sub-summaries via LLM

    Returns a flat list of Chunk objects with sequential IDs.
    """
    all_chunks: list[Chunk] = []
    header = f"## Session: {session_title} | Date: {session_date}\n\n"

    for topic in topics:
        topic_turns = extract_turns_for_topic(turns, topic)
        if not topic_turns:
            logger.warning("No turns found for topic %r (%s-%s)",
                           topic.topic_title, topic.start_timestamp, topic.end_timestamp)
            continue

        topic_text = "\n".join(_format_turn(t) for t in topic_turns)
        topic_tokens = count_tokens(topic_text)

        if topic_tokens <= max_topic_tokens:
            text = header + topic_text
            speakers = sorted(set(t.speaker for t in topic_turns))
            all_chunks.append(Chunk(
                chunk_id="",
                session_date=session_date,
                session_title=session_title,
                speakers_in_chunk=speakers,
                chunk_position=0,
                total_chunks_in_session=0,
                content_tier=content_tier,
                content_type="transcript",
                source=source,
                topic=topic.topic_title,
                summary=topic.summary,
                text=text,
            ))
        else:
            logger.info(
                "Topic %r is %d tokens, sub-splitting (threshold: %d)",
                topic.topic_title, topic_tokens, max_topic_tokens,
            )
            sub_chunks = chunk_transcript(
                topic_turns,
                session_date=session_date,
                session_title=session_title,
                target_tokens=500,
                overlap_tokens=50,
                content_tier=content_tier,
                source=source,
            )
            for sub_chunk in sub_chunks:
                text_for_summary = sub_chunk.text
                if text_for_summary.startswith(header):
                    text_for_summary = text_for_summary[len(header):]
                summary = _generate_sub_summary(topic.topic_title, text_for_summary)
                sub_chunk.topic = topic.topic_title
                sub_chunk.summary = summary
                all_chunks.append(sub_chunk)

    total = len(all_chunks)
    for i, chunk in enumerate(all_chunks):
        chunk.chunk_position = i + 1
        chunk.total_chunks_in_session = total
        chunk.chunk_id = f"{session_date}-chunk-{i + 1:03d}"

    return all_chunks
