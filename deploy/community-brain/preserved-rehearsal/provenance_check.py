"""Inventory preserved artifact references and failed-row scope without mutation."""

import json
from collections import Counter
from pathlib import Path

import lancedb
from verify_delivery import verify

root = Path("/delivery")
before = verify(root)
table = lancedb.connect(str(root / "corpus/lancedb/nomic-v1")).open_table("chunks")
rows = (
    table.search()
    .select(
        ["session_id", "source_file", "extraction_status", "content_type", "chunk_id"]
    )
    .limit(None)
    .to_list()
)
references = {(r["session_id"], r["source_file"]) for r in rows}
counts = Counter()
failures = Counter()
mappings = []
for session, source in sorted(references):
    name = Path(source).name
    direct = root / "output" / session / name
    candidates = (
        [direct]
        if direct.is_file()
        else list((root / "historical").glob(session + "*/" + name))
    )
    state = (
        "direct"
        if direct.is_file()
        else "historical_unique"
        if len(candidates) == 1
        else "missing"
        if not candidates
        else "ambiguous"
    )
    counts[state] += 1
    mappings.append(
        {
            "session_id": session,
            "source_file": source,
            "state": state,
            "candidates": [str(p.relative_to(root)) for p in candidates],
        }
    )
failed = [r for r in rows if r["extraction_status"] != "success"]
for r in failed:
    failures[r["session_id"]] += 1
assert verify(root) == before
result = {
    "references": len(references),
    "source_mapping_counts": dict(counts),
    "failed_rows": len(failed),
    "failed_by_session": dict(failures),
    "failed_by_type": dict(Counter(r["content_type"] for r in failed)),
    "delivery_unchanged": True,
}
Path("/results/provenance-map.json").write_text(
    json.dumps(mappings, sort_keys=True) + "\n"
)
Path("/results/provenance-summary.json").write_text(
    json.dumps(result, sort_keys=True) + "\n"
)
print(json.dumps(result, sort_keys=True))
