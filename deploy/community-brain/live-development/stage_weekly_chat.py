"""Upload the selected chat without submitting a job or enabling a worker."""

import hashlib
import json
import os
import subprocess
from pathlib import Path

from compose import read_env

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
raw = (root / "selected-weekly-chat.txt").read_bytes()
expected = "5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084"
assert hashlib.sha256(raw).hexdigest() == expected
script = """
import hashlib,json,sys,time,httpx
assert time.time() < 1789069401, "Development identity expired"
payload=json.load(sys.stdin)
with httpx.Client(base_url="http://api:8090",headers={"Authorization":"Bearer "+payload["token"]},timeout=20) as client:
    parent=client.get("/api/v1/jobs/33cc7538-e326-4f74-93ef-f2fcbb5c1624")
    assert parent.status_code == 200
    job=parent.json()
    assert job["identity"]["meeting_id"] == "181075701"
    assert job["identity"]["local_date"] == "2026-09-08"
    assert job["sources"]["transcript"] == "27969d75-10a9-4a46-8cf4-b63d1d7035d9"
    response=client.post("/api/v1/sources",json={"meeting_id":"181075701","kind":"chat","content":payload["content"]})
    assert response.status_code in (200,201)
    receipt=response.json()
    assert receipt["sha256"] == hashlib.sha256(payload["content"].encode()).hexdigest()
    print(json.dumps(receipt,sort_keys=True))
"""
result = subprocess.run(
    [
        "docker",
        "run",
        "--rm",
        "-i",
        "--network",
        "cbm-live-development_default",
        "--read-only",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges:true",
        "--memory",
        "256m",
        "community-brain:rehearsal",
        "python",
        "-c",
        script,
    ],
    input=json.dumps(
        {
            "token": read_env("/etc/community-brain-development/test-client.env")[
                "CB_DEV_OPERATOR_TOKEN"
            ],
            "content": raw.decode("utf-8"),
        }
    ).encode(),
    stdout=subprocess.PIPE,
    check=True,
)
receipt = json.loads(result.stdout)
assert receipt["sha256"] == expected and receipt["bytes"] == len(raw)
(root / "weekly-chat-source.json").write_text(
    json.dumps(receipt, sort_keys=True) + "\n"
)
print(json.dumps(receipt, sort_keys=True))
