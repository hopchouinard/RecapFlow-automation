# Session Themes Extraction Prompt (v1)

You extract 3-5 high-level themes from a summary of one coaching call session. Your output MUST be valid JSON matching the schema below.

## Input context

You will receive `SESSION_INPUT` — one of:
- A community post (narrative session summary), OR
- A concatenation of segment headers from the prepared transcript, OR
- An extracted-signal document (categorized facts)

## Output schema (JSON)

```json
{
  "themes": ["3-5 high-level themes, each 2-6 words"]
}
```

## Extraction rules

1. Themes are the main topics the session covered, at a zoom-out level. Not specific tools or people — topics.
2. Good examples: "agent framework comparison", "production deployment patterns", "embedding model tradeoffs".
3. Bad examples (too specific): "Alex's LangChain demo", "the GPU pricing question".
4. Bad examples (too broad): "AI", "coding", "tools".
5. Minimum 3 themes, maximum 5. Favor fewer, higher-quality themes over padding.
6. Output ONLY the JSON object. No prose.
