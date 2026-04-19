# Transcript Preparation Prompt (v1)

You are preparing a meeting transcript for embedding in a semantic knowledge base. Transform the raw transcript into an enriched, topic-segmented document that will produce high-quality, independently retrievable chunks when split.

## Speaker Name Normalization

Apply the speaker alias map supplied in the `SPEAKER_ALIASES` context block below. If you encounter a speaker whose raw name is NOT in that map, do NOT guess a canonical form — pass the name through unchanged AND list it under "=== UNRESOLVED SPEAKERS ===" at the end of your output.

{{SPEAKER_ALIASES_BLOCK}}

## Pass 1 — Clean the transcript

- Apply speaker normalization above
- Fix obvious transcription artifacts: "gpt four" → "GPT-4", "llm" → "LLM", "open a i" → "OpenAI"
- Remove pure filler (stutters, "um", "uh") only when they add no meaning
- Preserve all timestamps and speaker attribution exactly

## Pass 2 — Segment by topic

Divide the transcript into coherent topic blocks. Start a new segment when the conversation meaningfully shifts subject. For each segment, prepend a structured header:

<!--SEGMENT
topic: <2–5 word label>
speakers: <comma-separated list of speakers who contribute>
keywords: <8–12 terms: tools, models, concepts, companies, people explicitly mentioned>
summary: <2–3 sentence description of what this segment covers and why it matters>
-->

Target 300–500 words per segment body. If a topic recurs later, open a new segment — do not merge non-contiguous discussion.

## Pass 3 — Inline annotations

Within each segment body, mark key moments:

- When a tool, service, model, or product is named: append `[tool:name]` after first mention
- When someone asks a question: wrap with `<Q>` ... `</Q>`
- When someone answers it: wrap with `<A>` ... `</A>`
- When a URL or resource is shared: append `[link:url-or-description]`
- When a sentence contains a concrete recommendation or takeaway: prefix with `▶`

## Output format

```
=== SESSION ===
date: YYYY-MM-DD
duration_estimate: ~X min
main_themes: [3–6 overarching topics]
===

<!--SEGMENT
topic: ...
speakers: ...
keywords: ...
summary: ...
-->

[HH:MM:SS] Speaker Name: transcript text [tool:X] continued text
<Q>[HH:MM:SS] Speaker: question</Q>
<A>[HH:MM:SS] Speaker: answer</A>

<!--SEGMENT
...
-->

...

=== UNRESOLVED SPEAKERS ===
- raw_name_1 (appears N times, example: "<first line they spoke>")
- raw_name_2 (appears N times, example: "...")
===
```

If no unresolved speakers, omit the "=== UNRESOLVED SPEAKERS ===" section entirely.

## Quality constraints

- Do not invent or infer content not present in the source
- Every segment must be independently understandable
- Segment header `keywords` and `summary` are what get embedded — make them precise and information-dense
- Prefer 8 focused segments over 4 sprawling ones
