"""Ingestion pipeline for Community Brain v1.0 schema.

Parses prepared-transcript, extracted-signal, and community-post artifacts,
chunks them per the v1.0 rules, extracts structured metadata via LLM,
embeds with nomic-embed-text, and writes to LanceDB.
"""
