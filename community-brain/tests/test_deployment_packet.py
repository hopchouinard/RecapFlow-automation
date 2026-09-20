import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.parametrize(
    "filename",
    [
        "compose.yml",
        "compose.production-staging.yml",
        "compose.rehearsal.yml",
        "compose.scenario.yml",
        "compose.live-development.yml",
    ],
)
def test_candidate_compose_v2_configuration(tmp_path, filename):
    cache = (
        Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
        / "cbm-test-services/root"
    )
    cached = cache / "usr/bin/docker"
    docker = str(cached) if cached.exists() else shutil.which("docker")
    assert docker, "Run scripts/setup-cbm-test-services.sh for the isolated Compose CLI"
    config = tmp_path / "docker-config"
    config.mkdir()
    (config / "config.json").write_text(
        json.dumps(
            {"cliPluginsExtraDirs": [str(cache / "usr/libexec/docker/cli-plugins")]}
        )
    )
    compose = ROOT / "deploy/community-brain" / filename
    names = re.findall(r"\$\{([A-Z_]+)", compose.read_text())
    environment = {
        k: v
        for k, v in os.environ.items()
        if not k.startswith(("CB_", "DOCKER_", "OLLAMA_"))
    }
    environment.update({name: "fixture" for name in names})
    environment.update(
        {
            "CB_STATE_DIR": str(tmp_path / "state"),
            "CB_API_BIND": "127.0.0.1",
            "CB_IMAGE": "community-brain:fixture",
        }
    )
    subprocess.run(
        [
            docker,
            "--config",
            str(config),
            "compose",
            "--env-file",
            "/dev/null",
            "-f",
            str(compose),
            "config",
            "--quiet",
        ],
        env=environment,
        check=True,
        capture_output=True,
        timeout=20,
    )


def test_candidate_has_no_shared_service_provisioning_or_default_spend():
    compose = yaml.safe_load((ROOT / "deploy/community-brain/compose.yml").read_text())
    assert set(compose["services"]) == {"api", "worker"}
    assert (
        compose["services"]["api"]["environment"]["COMMUNITY_BRAIN_DISTRIBUTION_MODE"]
        == "true"
    )
    assert (
        compose["services"]["worker"]["environment"]["CB_ENABLE_MODEL_CALLS"]
        == "${CB_ENABLE_MODEL_CALLS:-false}"
    )
    assert compose["services"]["worker"]["profiles"] == ["processing"]
    assert all(
        s["user"] == "10001:10001" and s["read_only"]
        for s in compose["services"].values()
    )


def test_rehearsal_is_disposable_and_network_isolated():
    compose = yaml.safe_load(
        (ROOT / "deploy/community-brain/compose.rehearsal.yml").read_text()
    )
    assert compose["networks"]["default"]["internal"]
    for service in compose["services"].values():
        assert not service.get("ports")
        assert not service.get("privileged")
        assert service.get("network_mode") != "host"
    env = compose["services"]["api"]["environment"]
    assert env["CB_ENABLE_MODEL_CALLS"] == "false"
    assert env["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    assert "@postgres:5432/cbm_rehearsal" in env["CB_DATABASE_URL"]
    assert (
        compose["services"]["api"]["depends_on"]["migrate"]["condition"]
        == "service_completed_successfully"
    )
    assert not any(v.get("external") for v in compose["volumes"].values())


def test_scenario_keeps_simulated_providers_and_readonly_retrieval():
    compose = yaml.safe_load(
        (ROOT / "deploy/community-brain/compose.scenario.yml").read_text()
    )
    assert compose["networks"]["default"]["internal"]
    services = compose["services"]
    assert all(not s.get("ports") for s in services.values())
    assert "corpus:/state/corpus:ro" in services["api"]["volumes"]
    assert services["worker"]["command"] == [
        "python",
        "/checks/fixture_runtime.py",
        "worker",
    ]
    assert all(
        "CB_OPENROUTER_API_KEY" not in s.get("environment", {})
        for s in services.values()
    )
    assert all(not v.get("external") for v in compose["volumes"].values())


def test_live_login_stack_has_no_inference_key_or_worker_and_only_loopback_port():
    compose = yaml.safe_load(
        (ROOT / "deploy/community-brain/compose.live-development.yml").read_text()
    )
    services = compose["services"]
    assert "worker" not in services
    assert compose["networks"]["default"]["internal"]
    assert not any(v.get("external") for v in compose["volumes"].values())
    for name, service in services.items():
        env = service.get("environment", {})
        assert "CB_OPENROUTER_API_KEY" not in env
        assert not any("TOKEN" in key for key in env)
        if name != "api":
            assert not service.get("ports")
    api = services["api"]
    assert api["ports"] == ["127.0.0.1:8090:8090"]
    assert api["environment"]["CB_ENABLE_MODEL_CALLS"] == "false"
    assert api["environment"]["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    assert "config:/state/config:ro" in api["volumes"]
    assert api["environment"]["SSL_CERT_FILE"] == "/run/certs/ca-bundle.pem"
    assert api["environment"]["CB_ENABLE_RETRIEVAL"] == "true"
    assert api["environment"]["COMMUNITY_BRAIN_DISTRIBUTION_MODE"] == "true"
    assert "corpus:/state/corpus:ro" in api["volumes"]


def test_bounded_worker_has_no_publication_or_acquisition_credentials():
    overlay = yaml.safe_load(
        (ROOT / "deploy/community-brain/compose.bounded-development.yml").read_text()
    )
    worker = overlay["services"]["bounded-worker"]
    assert worker["profiles"] == ["bounded"]
    assert worker["environment"]["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    assert "CB_GITHUB_TOKEN" not in worker["environment"]
    assert "CB_FATHOM_API_KEY" not in worker["environment"]
    assert "CB_SERVICE_IDENTITIES" not in worker["environment"]
    assert not worker.get("ports")
    assert "config:/state/config" in worker["volumes"]
    assert "corpus:/state/corpus" in worker["volumes"]


def test_production_staging_cannot_start_worker_or_mount_writable_state():
    compose = yaml.safe_load(
        (ROOT / "deploy/community-brain/compose.production-staging.yml").read_text()
    )
    assert set(compose["services"]) == {"api"}
    api = compose["services"]["api"]
    assert "build" not in api
    assert api["pull_policy"] == "never"
    assert all(volume.endswith(":ro") for volume in api["volumes"])
    env = api["environment"]
    assert env["CB_ENABLE_MODEL_CALLS"] == "false"
    assert env["CB_ENABLE_NETWORK_PUBLICATION"] == "false"
    assert not any(
        name in env
        for name in ("CB_OPENROUTER_API_KEY", "CB_FATHOM_API_KEY",
                     "CB_GITHUB_TOKEN", "CB_NATS_URL")
    )
