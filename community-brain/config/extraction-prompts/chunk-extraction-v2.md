# Chunk Extraction Prompt (v2)

You extract structured metadata from a single chunk of conversational content. Your output MUST be valid JSON matching the schema described below. Do not include any prose, markdown, or explanation outside the JSON.

## Input context

You will receive:
- `CHUNK_TEXT` — the full text of the chunk (may include speaker attribution, segment headers, inline tags)
- `ENTITY_REGISTRY` — list of canonical entity names and their aliases (informational only — see entities rule below)
- `SPEAKER_ALIASES` — list of canonical speaker names and their aliases (informational only — see speakers rule below)
- `SPEAKERS_SPOKE` — JSON array of canonical speaker names who actually spoke in this chunk. Use this to exclude those names from `speakers_mentioned` (see speakers_mentioned rule below).

## Output schema (JSON)

```json
{
  "topic_label": "short descriptive label for this chunk's central topic",
  "entities": ["all proper-noun entities mentioned in CHUNK_TEXT, raw form unless registry recognizes them"],
  "speakers_mentioned": ["subset of entities that are PEOPLE, EXCLUDING anyone in speakers_spoke for this chunk"],
  "keywords": ["topical keywords / concepts / techniques / tools mentioned"],
  "speech_acts": ["one or more of: question | answer | opinion | recommendation | warning | anecdote | decision | action_item | prediction | comparison | definition"],
  "stance": "positive | negative | neutral | mixed | null",
  "certainty": "asserted | hedged | speculative",
  "chunk_local_markers": ["zero or more of: emphasized | sustained | breakthrough | resolved"],
  "decisions": ["zero or more concrete decisions/conclusions stated in the chunk"],
  "action_items": ["zero or more explicit commitments like 'X will do Y'"],
  "external_refs": ["zero or more URLs, paper titles, or resource references mentioned"],
  "references_prior": true,
  "has_question": true,
  "has_answer": true,
  "has_unresolved_question": true,
  "has_insight": true
}
```

## Extraction rules

### entities

Extract ALL proper-noun entities mentioned in CHUNK_TEXT across these four categories:

- **People** — proper-noun human names ("Adam James", "Andrej Karpathy"). When SPEAKER_ALIASES recognizes the name (canonical or alias), use the canonical form. Otherwise use the raw form as it appears.
- **Companies / orgs** — "OpenAI", "Anthropic", "Gold Flamingo", "Microsoft".
- **Products / tools** — "Claude Code", "Cursor", "n8n", "LanceDB", "Ollama", "Sonnet 4.6".
- **Frameworks / standards / techniques** — "RAG", "MCP", "OAuth", "BM25".

Excluded:
- Places (city, country names) — rarely meaningful in this corpus.
- URLs, hashes, commit refs — these go in `external_refs`.
- Generic nouns ("the team", "users", "developers").

Normalization:
- Case-preserved canonical form ("Claude Code" not "claude code").
- De-duplicated within a chunk (same entity twice in CHUNK_TEXT → one entry).

The pipeline applies a separate canonicalization pass at chunk write time to map raw extracted names to registry canonicals; you don't need to canonicalize unrecognized names yourself.

### speakers_mentioned

Output the deterministic subset of `entities` that satisfies BOTH:
1. The entity is a person (category 1 above).
2. The person is NOT in the `SPEAKERS_SPOKE` list provided in the input context (i.e., they are talked-about but not a speaker in this chunk).

Empty list if the chunk has no people-typed entities, or all such person entities are also in `SPEAKERS_SPOKE`.

### keywords

Topical keywords / concepts / techniques / tools mentioned. 5-15 entries per chunk (target ~10).

- De-duplicate within a chunk.
- Lower-case unless the term is conventionally capitalized ("RAG" stays uppercase; "context window" stays lowercase).
- Apply uniformly to all content types: prepared_transcript, extracted_signal, community_post.

### topic_label

A short (3-12 word) descriptive label for the chunk's central topic. For prepared_transcript chunks: descriptive ("Sales Funnel Optimization for Law Firms"). For extracted_signal chunks: section labels are fine ("decisions", "action_items", "general"). For community_post chunks: section labels ("session_narrative", or content-derived if richer signal is available).

### speech_acts

List all that apply. A chunk may contain multiple. Empty list `[]` for pure exposition. Do NOT return null.

### stance

Positive/negative/neutral about the chunk's main topic or entity. Use "mixed" when the speaker explicitly weighs pros and cons. Use null when stance isn't applicable (pure factual exposition, questions-only chunks).

### certainty

"asserted" for confident claims; "hedged" when the speaker uses "I think", "maybe", "probably"; "speculative" for "what if" or "I imagine" framing.

### chunk_local_markers

- `emphasized` — speakers explicitly signal importance ("this is key", "the big thing is", "I want to stress")
- `sustained` — multiple speakers engage across 3+ turns on the same specific point
- `breakthrough` — speakers frame as novel ("I just realized", "this changes how I think about X")
- `resolved` — contains a decision, conclusion, or closed question

### decisions, action_items, external_refs

Same semantics as v1: short self-contained strings; concrete decisions / explicit commitments / verbatim or clear references. Empty list when none.

### references_prior

`true` if the chunk explicitly refers to a previous session or earlier discussion ("like we discussed last week"); `false` otherwise.

### has_question, has_answer, has_unresolved_question, has_insight

Boolean flags:
- `has_question`: chunk contains an explicit question (whether asked rhetorically or to elicit response).
- `has_answer`: chunk contains a direct answer to an earlier or same-chunk question.
- `has_unresolved_question`: chunk contains a question that is left open without resolution within the chunk. Include subtle cases (awkward pause, soft topic-change after the question).
- `has_insight`: chunk contains a learning, realization, or substantive takeaway worth remembering.

## Rules

- Output ONLY the JSON object. No prose before or after.
- Every field must be present. Use `null` for scalar fields (like `stance`) when not applicable; use `[]` for list fields (like `speech_acts`, `entities`, `decisions`) when empty. Never omit a field.
- Do not invent content. Only extract what's explicitly present.
- When in doubt, prefer null / empty list over guessing.
- The v1 fields `new_entities_seen` and `new_speakers_seen` are no longer part of the output schema. The pipeline canonicalization pass handles new-name tracking.
