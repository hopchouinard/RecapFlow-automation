import json
from hashlib import sha256
from pathlib import Path

import lancedb

root = Path("/state/corpus")
manifest = globals()["MANIFEST"]
for name, expected in manifest["files"].items():
    assert sha256((root / name).read_bytes()).hexdigest() == expected
actual = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()}
assert actual == set(manifest["files"])
table = lancedb.connect(str(root / "lancedb/nomic-v1")).open_table("chunks")
rows = (
    table.search()
    .select(["session_id", "schema_version", "extraction_status"])
    .limit(None)
    .to_list()
)
assert len(rows) == 1901 and len({r["session_id"] for r in rows}) == 87
assert {r["schema_version"] for r in rows} == {"1.1"}
assert {r["extraction_status"] for r in rows} == {"success"}
assert table.schema.field("embedding").type.list_size == 768
stats = table.index_stats("bm25_text_idx")
assert stats["num_indexed_rows"] == 1901 and stats["num_unindexed_rows"] == 0
print(
    json.dumps(
        {
            "rows": 1901,
            "sessions": 87,
            "dimensions": 768,
            "schema": "1.1",
            "fts_indexed_rows": 1901,
            "fts_unindexed_rows": 0,
            "all_file_hashes_match": True,
        }
    )
)
