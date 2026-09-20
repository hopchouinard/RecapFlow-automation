"""Mac-only selected-chat upload. Credentials and content are never printed."""

import importlib.util
import json
import os
import stat
import sys
import time
from pathlib import Path

EXPECTED = "5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084"


def main():
    credential = (
        Path.home()
        / "Library/Application Support/CommunityBrainDevelopment/collector.json"
    )
    info = credential.lstat()
    assert stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid()
    assert stat.S_IMODE(info.st_mode) == 0o600
    private = json.loads(credential.read_text())
    assert private["backend"] == "https://community-brain-dev.patchoutech.lab"
    assert time.time() < private["expires_at"]
    module_path = Path(__file__).with_name("acquisition.py")
    spec = importlib.util.spec_from_file_location("cbm_collector", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    collector = module.ZoomCollector(
        Path.home() / "Documents/Zoom", private["backend"], private["token"]
    )
    assert len(sys.argv) == 2, "Supply the selected relative Zoom file path"
    with module.httpx.Client(
        base_url=private["backend"], timeout=20, follow_redirects=False
    ) as client:
        assert client.get("/health").status_code == 200
        assert client.post("/api/v1/sources", json={}).status_code == 401
        headers = {"Authorization": "Bearer " + private["token"]}
        for kind in ("transcript", "aliases"):
            response = client.post(
                "/api/v1/sources",
                headers=headers,
                json={
                    "meeting_id": "181075701",
                    "kind": kind,
                    "content": "denied permission probe",
                },
            )
            assert response.status_code == 403
        assert client.get("/api/v1/jobs", headers=headers).status_code == 404
    receipt = collector.upload(sys.argv[1], "181075701", expected_sha256=EXPECTED)
    assert receipt["sha256"] == EXPECTED and receipt["bytes"] == 6804
    print(
        json.dumps(
            {
                "receipt": receipt,
                "tls_health_verified": True,
                "unauthenticated_upload_denied": True,
                "nonchat_uploads_denied": True,
                "job_route_hidden": True,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001 - sanitize private credential/content diagnostics
        raise SystemExit(
            "Collector check/upload failed; no automatic retry. Inspect privately without printing credentials or chat."
        ) from None
