"""VM-only bounded exercise launcher. Preserve safe evidence; never print secrets."""

import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

from compose import RUNTIME, read_env

HERE = Path(__file__).resolve().parent
EVIDENCE = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
EVIDENCE.mkdir(exist_ok=True)
expected = {
    "jobs:read",
    "jobs:submit",
    "jobs:retry",
    "jobs:rerun",
    "jobs:reconcile",
    "sources:upload",
    "artifacts:read",
    "retrieval:read",
}
logs = subprocess.check_output(
    ["docker", "logs", "cbm-live-development-api-1"], stderr=subprocess.STDOUT
).decode()
proofs = [
    json.loads(line.split("development_oidc_verified ", 1)[1])
    for line in logs.splitlines()
    if "development_oidc_verified " in line
]
if not proofs and (EVIDENCE / "oidc-verification.json").exists():
    proofs = [json.loads((EVIDENCE / "oidc-verification.json").read_text())]
assert any(
    p["scope"] == "community-brain-dev"
    and set(p["permissions"]) == expected
    and p["issuer_audience_signature_expiry_verified"] is True
    for p in proofs
), "Real signed browser claim evidence required"
(EVIDENCE / "oidc-verification.json").write_text(
    json.dumps(proofs[-1], sort_keys=True) + "\n"
)
operation = sys.argv[1]
if operation in ("submit", "inspect", "reconcile-index", "retrieval"):
    args = [
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
        "512m",
        "--cpus",
        "1",
        "-v",
        str(HERE / "fixture.py") + ":/checks/fixture.py:ro",
        "community-brain:rehearsal",
        "python",
        "/checks/fixture.py",
        operation,
    ]
    if operation in ("inspect", "reconcile-index"):
        args.append(json.loads((EVIDENCE / "fixture-job.json").read_text())["job_id"])
    result = subprocess.run(
        args,
        input=json.dumps(
            read_env("/etc/community-brain-development/test-client.env")
        ).encode(),
        stdout=subprocess.PIPE,
        check=True,
    )
    output = json.loads(result.stdout)
    (
        EVIDENCE
        / (
            "fixture-job.json"
            if operation == "submit"
            else "reconciliation.json"
            if operation == "reconcile-index"
            else "retrieval-result.json"
            if operation == "retrieval"
            else "fixture-result.json"
        )
    ).write_text(json.dumps(output, sort_keys=True) + "\n")
    print(json.dumps(output, sort_keys=True))
elif operation in (
    "run",
    "index",
    "approved-backfill",
    "approved-index",
    "approved-weekly",
    "approved-weekly-index",
):
    subprocess.run([sys.executable, str(HERE / "check_allowance.py")], check=True)
    private = read_env(RUNTIME)
    env = dict(os.environ)
    env["CB_LIVE_DATABASE_URL"] = (
        "postgresql+psycopg://cbmdev:"
        + quote(private["CB_DEV_POSTGRES_PASSWORD"], safe="")
        + "@postgres:5432/cbm_dev"
    )
    env["CB_LIVE_NATS_URL"] = (
        "nats://cbmdev:"
        + quote(private["CB_DEV_NATS_PASSWORD"], safe="")
        + "@nats:4222"
    )
    job_id = json.loads(
        (
            EVIDENCE
            / (
                "weekly-processing-job.json"
                if operation in ("approved-weekly", "approved-weekly-index")
                else "recording-processing-job.json"
                if operation in ("approved-backfill", "approved-index")
                else "fixture-job.json"
            )
        ).read_text()
    )["job_id"]
    cmd = [
        "docker",
        "compose",
        "--env-file",
        RUNTIME,
        "-f",
        str(HERE.parent / "compose.live-development.yml"),
        "-f",
        str(HERE.parent / "compose.bounded-development.yml"),
    ]
    if operation == "approved-weekly-index":
        cmd += ["-f", str(HERE.parent / "compose.weekly-index-development.yml")]
    subprocess.run(cmd + ["config", "--quiet"], env=env, check=True)
    if operation == "approved-weekly-index":
        subprocess.run(
            cmd + ["run", "--rm", "--no-deps", "weekly-initialize"], env=env, check=True
        )
    if operation in ("index", "approved-index"):
        subprocess.run(
            cmd + ["run", "--rm", "--no-deps", "initialize"], env=env, check=True
        )
    with (
        EVIDENCE
        / (
            "weekly-indexing.log"
            if operation == "approved-weekly-index"
            else "weekly-processing.log"
            if operation == "approved-weekly"
            else "bounded-worker.log"
            if operation == "run"
            else "recording-processing.log"
            if operation == "approved-backfill"
            else "recording-indexing.log"
            if operation == "approved-index"
            else "bounded-indexing.log"
        )
    ).open("ab") as log:
        result = subprocess.run(
            cmd
            + [
                "run",
                "--rm",
                "--no-deps",
                "bounded-worker",
                job_id,
                "approved-weekly-index"
                if operation == "approved-weekly-index"
                else "approved-weekly"
                if operation == "approved-weekly"
                else "processing"
                if operation == "run"
                else "approved-backfill"
                if operation == "approved-backfill"
                else "approved-index"
                if operation == "approved-index"
                else "indexing",
            ],
            env=env,
            stdout=log,
            stderr=subprocess.STDOUT,
            check=False,
        )
    print("Bounded worker exit:", result.returncode)
    raise SystemExit(result.returncode)
else:
    raise SystemExit("Use submit, run or inspect")
