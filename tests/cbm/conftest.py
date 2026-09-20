"""Real, private services. Never accept a database URL or external NATS address."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

import pytest
from sqlalchemy import URL, create_engine


def executable(name, cached):
    cache = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
    candidate = cache / "cbm-test-services/root" / cached
    found = str(candidate) if candidate.is_file() else shutil.which(name)
    if not found:
        pytest.fail(f"Missing {name}; run scripts/setup-cbm-test-services.sh (Forge).")
    return found


@pytest.fixture(scope="session")
def isolated_environment():
    with pytest.MonkeyPatch.context() as patch:
        for name in os.environ:
            if name.startswith("PG"):
                patch.delenv(name)
        yield


@pytest.fixture(scope="session")
def services(isolated_environment):
    # Short, mode-0700 path keeps Unix sockets below the platform length limit.
    with tempfile.TemporaryDirectory(prefix="cbm-") as directory:
        root = Path(directory)
        pg_bin = Path(executable("initdb", "usr/lib/postgresql/18/bin/initdb")).parent
        nats = executable("nats-server", "usr/sbin/nats-server")
        # Ignore libpq configuration inherited from an operator shell.
        env = {"PATH": os.defpath, "LANG": "C.UTF-8"}
        cached_lib = pg_bin.parents[2] / "x86_64-linux-gnu"
        if cached_lib.is_dir():
            env["LD_LIBRARY_PATH"] = str(cached_lib)
        subprocess.run(
            [
                str(pg_bin / "initdb"),
                "-D",
                str(root / "pg"),
                "-U",
                "cbm_test",
                "--auth=trust",
                "--no-locale",
                "-E",
                "UTF8",
            ],
            env=env,
            check=True,
            capture_output=True,
        )
        processes = []
        try:
            with (
                (root / "postgres.log").open("wb") as pg_log,
                (root / "nats.log").open("wb") as nats_log,
            ):
                processes.append(
                    subprocess.Popen(
                        [
                            str(pg_bin / "postgres"),
                            "-D",
                            str(root / "pg"),
                            "-k",
                            directory,
                            "-c",
                            "listen_addresses=",
                            "-c",
                            "max_connections=20",
                        ],
                        env=env,
                        stdout=pg_log,
                        stderr=subprocess.STDOUT,
                    )
                )
                # NATS chooses its own free port and writes the actual endpoint.
                processes.append(
                    subprocess.Popen(
                        [
                            nats,
                            "-a",
                            "127.0.0.1",
                            "-p",
                            "-1",
                            "-js",
                            "-sd",
                            str(root / "js"),
                            "--ports_file_dir",
                            directory,
                        ],
                        env=env,
                        stdout=nats_log,
                        stderr=subprocess.STDOUT,
                    )
                )
                import json

                deadline = time.monotonic() + 20
                while True:
                    ports = list(root.glob("*.ports"))
                    ready = (
                        subprocess.run(
                            [
                                str(pg_bin / "pg_isready"),
                                "-h",
                                directory,
                                "-U",
                                "cbm_test",
                            ],
                            env=env,
                            capture_output=True,
                        ).returncode
                        == 0
                    )
                    if ready and ports:
                        endpoint = json.loads(ports[0].read_text())["nats"][0]
                        break
                    if (
                        any(p.poll() is not None for p in processes)
                        or time.monotonic() > deadline
                    ):
                        pytest.fail(
                            "Private services failed to start:\n"
                            + (root / "postgres.log").read_text()
                            + (root / "nats.log").read_text()
                        )
                    time.sleep(0.05)
                yield (
                    URL.create(
                        "postgresql+psycopg",
                        username="cbm_test",
                        database="postgres",
                        query={"host": directory},
                    ),
                    endpoint,
                )
        finally:
            for process in reversed(processes):
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)


@pytest.fixture
def engine(services):
    from reference import metadata

    engine = create_engine(services[0])
    metadata.create_all(
        engine
    )  # Disposable contract schema, NOT application migrations.
    try:
        yield engine
    finally:
        metadata.drop_all(engine)
        engine.dispose()
