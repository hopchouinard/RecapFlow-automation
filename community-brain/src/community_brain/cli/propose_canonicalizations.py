"""propose_canonicalizations CLI — heuristic merge proposals from the
pending queue against existing canonicals.

Spec: docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md §7.1.

Usage:
    python -m community_brain.cli.propose_canonicalizations \\
        [--registry community-brain/config/speaker-aliases.yaml] \\
        [--out community-brain/canonicalization-proposals.yaml]

Read-only on the registry; write-only to the proposals file.
"""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
from typing import Any

import yaml


def _exact_case_insensitive(pending: str, canonicals: list[str]) -> str | None:
    pl = pending.lower()
    for c in canonicals:
        if c.lower() == pl:
            return c
    return None


def _first_name_single_match(pending: str, canonicals: list[str]) -> str | None:
    """Return canonical iff exactly one canonical has `pending` as first token (case-insensitive)."""
    pl = pending.lower().strip()
    if " " in pl:
        return None
    matches = [c for c in canonicals if c.lower().split(" ", 1)[0] == pl]
    return matches[0] if len(matches) == 1 else None


def _token_containment_single(pending: str, canonicals: list[str]) -> str | None:
    """Multi-token pending like 'Adam - Gold Flamingo': match by first token,
    require exactly one canonical candidate."""
    head = pending.lower().split(" ", 1)[0].strip().rstrip(",")
    if not head:
        return None
    matches = [c for c in canonicals if c.lower().split(" ", 1)[0] == head]
    return matches[0] if len(matches) == 1 else None


def generate_proposals(registry: dict[str, Any]) -> dict[str, Any]:
    """Produce {generated_at, proposals: [...], ambiguous: [...]}.

    Each proposal: {canonical, candidate_aliases, confidence, reason}.
    Each ambiguous: {name, reason}.
    """
    aliases = registry.get("aliases") or {}
    pending = registry.get("pending") or []
    canonicals = list(aliases.keys())
    by_canonical: dict[str, dict[str, Any]] = {}
    ambiguous: list[dict[str, str]] = []

    for entry in pending:
        match: str | None = None
        confidence = "high"
        reason = ""
        # 1. Exact case-insensitive (high)
        match = _exact_case_insensitive(entry, canonicals)
        if match is not None:
            reason = "case-insensitive exact match"
        # 2. First-name single-match (high)
        if match is None:
            match = _first_name_single_match(entry, canonicals)
            if match is not None:
                reason = "first-name token match, single canonical candidate"
        # 3. Token containment (medium)
        if match is None:
            match = _token_containment_single(entry, canonicals)
            if match is not None:
                confidence = "medium"
                reason = "token containment, single canonical candidate"

        if match is None:
            ambiguous.append({
                "name": entry,
                "reason": "no canonical candidate found via heuristics",
            })
            continue

        if match not in by_canonical:
            by_canonical[match] = {
                "canonical": match,
                "candidate_aliases": [],
                "confidence": confidence,
                "reason": reason,
            }
        if entry not in by_canonical[match]["candidate_aliases"]:
            by_canonical[match]["candidate_aliases"].append(entry)
        # Demote confidence to medium if any contributing entry came via medium-tier.
        if confidence == "medium":
            by_canonical[match]["confidence"] = "medium"

    proposals = sorted(by_canonical.values(), key=lambda p: p["canonical"])
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "proposals": proposals,
        "ambiguous": sorted(ambiguous, key=lambda a: a["name"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="community-brain/config/speaker-aliases.yaml")
    parser.add_argument("--out", default="community-brain/canonicalization-proposals.yaml")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    out_path = Path(args.out)
    registry = yaml.safe_load(registry_path.read_text())
    proposals = generate_proposals(registry)
    out_path.write_text(yaml.safe_dump(proposals, sort_keys=False, allow_unicode=True))
    print(f"[ok] wrote {len(proposals['proposals'])} proposals + "
          f"{len(proposals['ambiguous'])} ambiguous to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
