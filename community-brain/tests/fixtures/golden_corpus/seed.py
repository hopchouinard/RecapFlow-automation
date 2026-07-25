"""Seed a small LanceDB corpus for golden-query tests.

Creates a chunks table at a given path with engineered rows covering:
  - Entity-grounded queries (Finding 6): chunks with rare proper-noun
    tokens in full_text but bland embed_text vectors.
  - Metadata-tagged queries (Finding 7): chunks with has_unresolved_question,
    decisions, action_items, has_insight, references_prior set, alongside
    chunks lacking the flags but with similar thematic content.

Used by tests/test_golden_queries.py. Not a runtime dependency.
"""

from __future__ import annotations

import sys

import lancedb

from community_brain.ingestion.schema import EMBEDDING_DIM, pyarrow_table_schema


COMMON = {
    "schema_version": "1.0",
    "session_title": None,
    "content_type": "extracted_signal",
    "source_file": "extracted-signal.md",
    "total_chunks_in_source": 10,
    "speakers_spoke": [],
    "speakers_mentioned": [],
    "keywords": [],
    "topic_label": None,
    "session_themes": ["growth", "onboarding"],
    "speech_acts": [],
    "stance": None,
    "certainty": "asserted",
    "chunk_local_markers": [],
    "corpus_derived_markers": [],
    "corpus_markers_computed_at": None,
    "decisions": [],
    "action_items": [],
    "external_refs": [],
    "extraction_model": "test",
    "extraction_prompt_version": "test-v1",
    "extraction_status": "success",
    "extraction_error": None,
    "extracted_at": "2026-04-01T00:00:00",
    "embed_text": "...",
}


def _row(idx, chunk_id, session_id, full_text, **overrides):
    """Build a row with an embedding vector that places it generically.

    Default vector value is 0.01*(idx+1) — small so decoy chunks (which use
    vector value 0.5) rank above all targets under a constant-0.5 query
    vector. The query mock in test_golden_queries.py returns [0.5]*EMBEDDING_DIM,
    so distance(target, query) = sqrt(EMBEDDING_DIM) * |0.5 - 0.01*(idx+1)|
    which is non-zero, while decoys at vector value 0.5 land at distance 0.
    """
    base = {
        **COMMON,
        "chunk_id": chunk_id,
        "session_id": session_id,
        "session_date": session_id,
        "chunk_index": idx,
        "entities": [],
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "references_prior": False,
        "full_text": full_text,
        # bm25_text mirrors full_text in the golden corpus; in production it's
        # synthesized from full_text + structured metadata fields.
        "bm25_text": full_text,
        "embedding": [float((idx + 1) * 0.01)] * EMBEDDING_DIM,
    }
    base.update(overrides)
    return base


def _decoy(idx, chunk_id, full_text):
    """Build a decoy chunk: vector at distance 0 from the constant query
    vector ([0.5]*EMBEDDING_DIM), with thematic content that does not
    lexically match any golden query AND does not satisfy any cue rule
    predicate. There must be enough decoys (>= top_k * OVERSAMPLE_FACTOR =
    30 in the v2 search_chunks) for vector-only baseline to legitimately
    miss target chunks — otherwise the small fixture trap T9/T10 hit comes
    back: cue boost trivially surfaces metadata-flagged chunks because the
    candidate pool contains all rows.
    """
    return {
        **COMMON,
        "chunk_id": chunk_id,
        "session_id": f"2026-05-{(idx % 28) + 1:02d}",
        "session_date": f"2026-05-{(idx % 28) + 1:02d}",
        "chunk_index": idx,
        "entities": [],
        "has_question": False,
        "has_answer": False,
        "has_unresolved_question": False,
        "has_insight": False,
        "references_prior": False,
        "full_text": full_text,
        # bm25_text mirrors full_text in the golden corpus
        "bm25_text": full_text,
        "embedding": [0.5] * EMBEDDING_DIM,
    }


# Bland decoy texts: no proper-noun entities, no cue-rule trigger phrases
# ("unresolved"/"decided"/"action item"/"insight"/"prior"/"question"/etc.),
# no shared topic words with the f6-adam queries ("law firm", "linkedin",
# "gold flamingo"). Vague community-management filler.
_DECOY_TEXTS = (
    "members appreciated the new welcome flow more than the previous version",
    "monthly engagement charts trended upward through the second half of the quarter",
    "channels for casual chatter saw heavier traffic on weekends",
    "video posts performed better than image posts when measured by replies",
    "weekly digests had higher click-through when the subject line was concrete",
    "long-form posts kept readers longer than carousel summaries",
    "community lounge events drew mixed attendance depending on the time slot",
    "recurring sessions on craft topics retained more members than ad-hoc ones",
    "polls helped surface what topics members actually wanted covered",
    "moderation guidelines were updated to clarify expectations around self-promotion",
    "onboarding emails delivered higher conversion when sent within the first hour",
    "members who attended at least three live sessions stayed longer overall",
    "the resource library saw heaviest usage on Tuesday and Wednesday mornings",
    "feature requests from power users were tagged and grouped by theme",
    "newer members preferred bite-sized content over deep technical threads",
    "live event attendance correlated with how often hosts pinned reminder posts",
    "casual coffee-chat formats outperformed structured workshops on retention",
    "bookmarked posts were a leading indicator of which topics would trend",
    "reply velocity in the first hour predicted total engagement on a thread",
    "founders shared more freely when the format was conversational rather than panel",
    "the leaderboard quietly motivated returning members week over week",
    "themed weeks helped concentrate attention around a single subject",
    "members reported preferring async formats over live ones when topics were dense",
    "shared playbooks gathered more downloads than individual templates",
    "new members tended to lurk for several weeks before posting",
    "spotlight interviews drew steady traffic regardless of guest seniority",
    "shared spreadsheets of vendors collected slow but steady contributions",
    "the welcome video was watched far more often than its written counterpart",
    "regional sub-channels grew slowly but had high member retention",
    "side-project showcases became a recurring social ritual",
    "office-hours formats were rated highly when limited to small groups",
    "shared reading lists drove longer browsing sessions in the library",
    "monthly retros focused on what to stop doing rather than what to start",
    "swag drops drove a short-term spike in casual posting volume",
    "founders reported feeling less alone when peer-matched within cohorts",
)


def seed(db_path: str) -> None:
    db = lancedb.connect(db_path)
    schema = pyarrow_table_schema()
    if "chunks" in db.list_tables().tables:
        db.drop_table("chunks")
    table = db.create_table("chunks", schema=schema)
    rows = [
        # --- Finding 6 fixtures: entity-grounded ---
        _row(0, "f6-adam-1", "2026-02-01",
             "Adam from Gold Flamingo Solutions described the sales funnel for law firms",
             entities=["Adam", "Gold Flamingo"]),
        _row(1, "f6-adam-2", "2026-02-08",
             "Adam followed up on his LinkedIn outreach experiment to law firm partners",
             entities=["Adam"]),
        # 3 additional entity-grounded fixtures (spec §9.1: 5 entity-grounded queries total).
        # No cue-rule-firing flags set so these isolate Finding 6 (entity) from Finding 7 (metadata).
        _row(2, "f6-maria-1", "2026-02-08",
             "Maria from Beacon Analytics walked through her tiered pricing model for enterprise contracts",
             entities=["Maria", "Beacon Analytics"]),
        _row(3, "f6-blueocean-1", "2026-02-15",
             "the BlueOcean Capital partnership conversation surfaced a referral pipeline for fintech operators",
             entities=["BlueOcean Capital"]),
        _row(4, "f6-tokyo-1", "2026-02-22",
             "Tokyo Labs Research Group asked about co-marketing for the Japan launch in Q3",
             entities=["Tokyo Labs Research Group"]),
        _row(5, "f6-bland-1", "2026-02-15",
             "general weekly community sync about onboarding and retention strategies"),
        _row(6, "f6-bland-2", "2026-02-22",
             "checklist hygiene and follow-up cadence for new community members"),
        # --- Finding 7 fixtures: metadata-tagged ---
        _row(7, "f7-unres-1", "2026-03-01",
             "open question about how to scope the consulting engagement remained unresolved",
             has_unresolved_question=True),
        _row(8, "f7-unres-2", "2026-03-08",
             "we still don't know whether to charge a flat fee or hourly; the pricing question stayed unresolved at end of call",
             has_unresolved_question=True),
        _row(9, "f7-decision-1", "2026-03-15",
             "the team made a decision to ship the new pricing page next Monday",
             decisions=["ship pricing page Monday"], has_answer=True),
        _row(10, "f7-actions-1", "2026-03-22",
             "action items captured: send the LinkedIn message to all law firm contacts by Friday",
             action_items=["send LinkedIn message Friday"]),
        _row(11, "f7-insight-1", "2026-03-29",
             "key takeaway from the discussion: the funnel breaks at the demo-to-proposal handoff",
             has_insight=True),
        _row(12, "f7-prior-1", "2026-04-05",
             "as referenced from a prior call during the launch retro, the onboarding flow drops off at step three",
             references_prior=True),
        # --- v5 injection fixtures: a quiet session invisible to both
        # hybrid legs. session_date carries the date; bm25_text deliberately
        # holds NO date tokens and no vocabulary shared with any golden
        # query; the embedding sits far from the constant 0.5 query vector.
        # Pre-v5 these chunks cannot enter the candidate pool on a date
        # query — only cue-driven recruitment can surface them.
        _row(13, "v5-quiet-1", "2025-12-30",
             "brief seasonal gathering with informal catch-ins on sabbatical intentions",
             bm25_text="brief seasonal gathering informal catch-ins sabbatical intentions",
             embedding=[0.9] * EMBEDDING_DIM),
        _row(14, "v5-quiet-2", "2025-12-30",
             "closing remarks regarding upcoming sabbaticals and reduced cadence",
             bm25_text="closing remarks upcoming sabbaticals reduced cadence",
             embedding=[0.9] * EMBEDDING_DIM),
    ]
    # Append decoys. Index offset by 100 so chunk_index is unique and easy
    # to tell apart from targets in debug output.
    for i, text in enumerate(_DECOY_TEXTS):
        rows.append(_decoy(100 + i, f"decoy-{i:02d}", text))
    table.add(rows)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: seed.py <db_path>", file=sys.stderr)
        sys.exit(2)
    seed(sys.argv[1])
    print(f"seeded golden corpus at {sys.argv[1]}")
