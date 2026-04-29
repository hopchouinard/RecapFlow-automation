"""apply_canonicalizations CLI — merge proposals into the registry.

Auto-triggers recanonicalize at the end unless --no-recanonicalize.

Usage:
    python -m community_brain.cli.apply_canonicalizations <proposals.yaml> \\
        [--registry community-brain/config/speaker-aliases.yaml] \\
        [--no-recanonicalize] \\
        [--db /data/lancedb/nomic-v1]

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §7.1.
"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any

import yaml


logger = logging.getLogger(__name__)


class ProposalConflictError(Exception):
    """Raised when proposals would create alias-canonical conflicts."""
    pass


def _validate_proposals(
    registry: dict[str, Any],
    proposals: dict[str, Any],
) -> list[str]:
    """Return a list of conflict descriptions; empty if no conflicts."""
    aliases = registry.get("aliases") or {}
    pending = set(registry.get("pending") or [])
    canonicals = set(aliases.keys())

    # Build alias-to-canonical lookup for the existing registry.
    existing_alias_to_canonical: dict[str, str] = {}
    for canonical, alias_list in aliases.items():
        for alias in alias_list or []:
            existing_alias_to_canonical[alias] = canonical

    conflicts: list[str] = []
    # Track aliases proposed within THIS YAML to catch intra-file duplicates.
    # A stale or manually-edited proposals file could put the same alias under
    # two canonicals, creating silent ambiguity in the registry.
    proposed_alias_to_canonical: dict[str, str] = {}

    for prop in proposals.get("proposals") or []:
        canonical = prop["canonical"]
        for candidate in prop.get("candidate_aliases") or []:
            # Conflict 1: candidate is itself a canonical (other than the target one)
            if candidate in canonicals and candidate != canonical:
                conflicts.append(
                    f"candidate '{candidate}' is already a canonical name; "
                    f"refusing to merge it as an alias of '{canonical}'"
                )
            # Conflict 2: candidate is already an alias for a DIFFERENT canonical
            existing_canonical = existing_alias_to_canonical.get(candidate)
            if existing_canonical and existing_canonical != canonical:
                conflicts.append(
                    f"candidate '{candidate}' is already an alias of '{existing_canonical}'; "
                    f"refusing to remap to '{canonical}'"
                )
            # Conflict 3: candidate appears under a DIFFERENT canonical in this
            # same proposals file (intra-file duplicate).
            prior = proposed_alias_to_canonical.get(candidate)
            if prior is not None and prior != canonical:
                conflicts.append(
                    f"candidate '{candidate}' appears in this proposals file under "
                    f"both '{prior}' and '{canonical}'; cannot apply both."
                )
            else:
                proposed_alias_to_canonical[candidate] = canonical
            # Candidate not in pending — log but don't block (manually-curated registries
            # may have candidates already removed from pending; re-applying a known-good
            # proposal should still work).
            if candidate not in pending and candidate not in (aliases.get(canonical) or []):
                logger.warning(
                    "apply_canonicalizations: candidate '%s' is not in pending "
                    "(may have been manually promoted); applying anyway.",
                    candidate,
                )
    return conflicts


def apply_proposals_to_registry(
    registry: dict[str, Any],
    proposals: dict[str, Any],
) -> dict[str, Any]:
    """Merge accepted proposals into a copy of the registry.

    For each proposal: ensure canonical exists in aliases; append the
    candidate_aliases (deduped + sorted); remove them from pending.

    Ambiguous proposals are not applied (they stay in pending for
    operator review). The input registry is not mutated.

    Raises ProposalConflictError if any candidate would conflict with
    an existing canonical or alias. The conflict list is included in the
    exception message; nothing is applied when conflicts are detected.
    """
    conflicts = _validate_proposals(registry, proposals)
    if conflicts:
        raise ProposalConflictError(
            "Proposal application aborted due to "
            f"{len(conflicts)} conflict(s):\n  - " + "\n  - ".join(conflicts)
        )
    out: dict[str, Any] = {}
    if "version" in registry:
        out["version"] = registry["version"]
    out["aliases"] = {k: list(v or []) for k, v in (registry.get("aliases") or {}).items()}
    out["pending"] = list(registry.get("pending") or [])
    for prop in proposals.get("proposals") or []:
        canonical = prop["canonical"]
        candidates = prop.get("candidate_aliases") or []
        existing = set(out["aliases"].get(canonical, []))
        for c in candidates:
            existing.add(c)
            if c in out["pending"]:
                out["pending"].remove(c)
        out["aliases"][canonical] = sorted(existing)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("proposals_path")
    parser.add_argument("--registry", default="community-brain/config/speaker-aliases.yaml")
    parser.add_argument("--no-recanonicalize", action="store_true")
    parser.add_argument("--db", default="/data/lancedb/nomic-v1")
    args = parser.parse_args()

    proposals = yaml.safe_load(Path(args.proposals_path).read_text())
    registry_path = Path(args.registry)
    registry = yaml.safe_load(registry_path.read_text())
    updated = apply_proposals_to_registry(registry, proposals)
    registry_path.write_text(yaml.safe_dump(updated, sort_keys=False, allow_unicode=True))
    n_proposals = len(proposals.get("proposals") or [])
    print(f"[ok] applied {n_proposals} proposals to {registry_path}")

    if args.no_recanonicalize:
        print("[ok] --no-recanonicalize set; skipping chunk rewrite")
        return 0

    # Auto-trigger recanonicalize.
    from community_brain.cli.recanonicalize import recanonicalize_chunks
    from community_brain.ingestion import embedding as embedding_module

    def _embed_one(text: str) -> list[float]:
        return embedding_module.embed_texts([text], ollama_base_url=None)[0]

    stats = recanonicalize_chunks(
        args.db,
        updated,
        embed_fn=_embed_one,
        dry_run=False,
    )
    print(f"[ok] recanonicalize: scanned {stats['scanned']}, updated {stats['updated']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
