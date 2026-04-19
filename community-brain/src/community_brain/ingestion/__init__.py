"""Ingestion pipeline for Community Brain v1.0 schema.

Parses prepared-transcript, extracted-signal, and community-post artifacts,
chunks them per the v1.0 rules, extracts structured metadata via LLM,
embeds with nomic-embed-text, and writes to LanceDB.

## Error handling contract

All loaders and registries in this package follow these rules:

1. Missing input file -> ``FileNotFoundError`` with the path in the message.
2. Malformed YAML structure (wrong shape, missing required key, wrong type)
   -> ``ValueError`` with the file name and the offending key/type in the message.
3. Valid-but-empty input (e.g. ``aliases: {}``) -> returns an empty object,
   no error raised.

Downstream code should let ``FileNotFoundError`` propagate (operator config
mistake) and log/surface ``ValueError`` clearly (operator content mistake).
"""

from community_brain.ingestion.registries import EntityRecord  # re-export

__all__ = ["EntityRecord"]
