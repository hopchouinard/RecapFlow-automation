"""VM-only temporary API using the restored corpus, no provider key or host port."""

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "live-development"))
from compose import read_env


def main():
    os.umask(0o077)
    candidate = sys.argv[1:] == ["--candidate"]
    control = sys.argv[1:] == ["--control"]
    assert not sys.argv[1:] or candidate or control
    name = "cbm-preserved-api"
    assert (
        subprocess.run(
            ["docker", "inspect", name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        != 0
    )
    values = json.loads(
        subprocess.check_output(
            [
                "docker",
                "inspect",
                "--format",
                "{{json .Config.Env}}",
                "cbm-live-development-api-1",
            ]
        )
    )
    env = dict(x.split("=", 1) for x in values)
    assert not any("OPENROUTER_API_KEY" in k or "FATHOM_API_KEY" in k for k in env)
    env.update(
        LANCEDB_PATH="/delivery/corpus/lancedb/nomic-v1",
        CB_PIPELINE_CONFIG_DIR="/delivery/config",
        COMMUNITY_BRAIN_CONFIG_DIR="/delivery/config",
        CB_ENABLE_MODEL_CALLS="false",
        CB_ENABLE_NETWORK_PUBLICATION="false",
        COMMUNITY_BRAIN_DISTRIBUTION_MODE="true",
    )
    if candidate or control:
        env["LANCEDB_PATH"] = "/candidate/lancedb/nomic-v1"
    with tempfile.TemporaryDirectory(
        prefix="cbm-preserved-api-", dir="/srv/dev-data/workspaces"
    ) as temporary:
        path = Path(temporary) / "runtime.env"
        assert all("\n" not in v for v in env.values())
        path.write_text("".join(k + "=" + v + "\n" for k, v in env.items()))
        try:
            subprocess.run(
                [
                    "docker",
                    "run",
                    "-d",
                    "--name",
                    name,
                    "--network",
                    "cbm-live-development_default",
                    "--read-only",
                    "--tmpfs",
                    "/tmp",
                    "--cap-drop",
                    "ALL",
                    "--memory",
                    "1g",
                    "--cpus",
                    "1",
                    "--env-file",
                    str(path),
                    "-v",
                    "/srv/dev-data/workspaces/cbm-preserved-20260910/delivery:/delivery:ro",
                    "-v",
                    "cbm-live-development_files:/state/files:ro",
                    "-v",
                    "/srv/dev-data/workspaces/cbm-preserved-20260910/results/index-control:/candidate:ro"
                    if control
                    else "/srv/dev-data/workspaces/cbm-preserved-20260910/results/consumer-candidate-v1/installed:/candidate:ro",
                    "-v",
                    "/etc/ssl/certs/ca-certificates.crt:/run/certs/ca-bundle.pem:ro",
                    "community-brain:rehearsal",
                    "uvicorn",
                    "community_brain.jobs.runtime:app",
                    "--factory",
                    "--host",
                    "0.0.0.0",
                    "--port",
                    "8090",
                    "--no-access-log",
                ],
                stdout=subprocess.DEVNULL,
                check=True,
            )
            subprocess.run(
                ["docker", "network", "connect", "cbm-live-development_oidc", name],
                check=True,
            )
            for _ in range(40):
                check = subprocess.run(
                    [
                        "docker",
                        "exec",
                        name,
                        "python",
                        "-c",
                        "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=2)",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False,
                )
                if check.returncode == 0:
                    break
                time.sleep(1)
            else:
                raise RuntimeError("Temporary API not healthy")
            result = subprocess.check_output(
                [
                    "docker",
                    "run",
                    "--rm",
                    "-i",
                    "--network",
                    "cbm-live-development_default",
                    "--read-only",
                    "--tmpfs",
                    "/tmp",
                    "--cap-drop",
                    "ALL",
                    "--memory",
                    "256m",
                    "-v",
                    str(HERE / "retrieval_checks.py") + ":/checks/check.py:ro",
                    "community-brain:rehearsal",
                    "python",
                    "/checks/check.py",
                ],
                input=json.dumps(
                    read_env("/etc/community-brain-development/test-client.env")
                ).encode(),
            )
            receipt = json.loads(result)
            Path(
                "/srv/dev-data/artifacts/cbm-preserved-corpus-rehearsal/"
                + (
                    "control-retrieval-result.json"
                    if control
                    else "candidate-retrieval-result.json"
                    if candidate
                    else "source-comparison-retrieval-result.json"
                )
            ).write_text(json.dumps(receipt, sort_keys=True) + "\n")
            print(json.dumps(receipt, sort_keys=True))
        finally:
            subprocess.run(
                ["docker", "rm", "-f", name], stdout=subprocess.DEVNULL, check=True
            )


if __name__ == "__main__":
    main()
