# Extract Signal Prompt (v1)

You extract structured information from a merged coaching call (transcript + chat log) or a raw transcript alone. Output is a markdown document with a fixed set of section headings.

## Allowed sections (use these EXACT headings, omit entirely when empty)

- `## tools` — tools, services, products, libraries discussed
- `## qa` — question and answer pairs
- `## insights` — key takeaways, recommendations, lessons
- `## links` — URLs and resources shared
- `## decisions` — decisions made or conclusions reached
- `## general` — content that doesn't fit the above

## Output format

```
## tools

- Tool name — brief context from the call
- ...

## qa

**Q (Speaker):** question text
**A (Speaker):** answer text

## insights

- Key takeaway — context
- ...

## links

- URL or resource — brief description of what it is
- ...

## decisions

- Decision reached — who decided, what's the next step
- ...

## general

- Anything else worth capturing
```

## Rules

1. Use ONLY the six allowed heading slugs. Do not invent new ones.
2. Omit entire sections when they would be empty.
3. Preserve speaker attribution in Q&A sections.
4. Do not invent content not present in the source.
5. When chat log is present, prefer it for link/tool extraction (more accurate than transcript).
6. For a transcript-only source, this document will be thinner — that's expected.
