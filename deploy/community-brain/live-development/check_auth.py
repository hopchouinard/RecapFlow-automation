"""Scoped VM test process. Never print bearer values or response headers."""

import json
import sys
import time
import urllib.error
import urllib.request

if time.time() >= 1789069401:
    raise SystemExit("Development identities expired; renew through Infisical")
BASE = "http://api:8090"
tokens = json.load(sys.stdin)


def request(path, token=None, method="GET", body=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(
        BASE + path,
        data=json.dumps(body).encode() if body is not None else None,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, {}


assert request("/health")[0] == 200
assert request("/api/v1/me")[0] == 401
assert request("/api/v1/me", "invalid-development-token")[0] == 401
assert request("/api/v1/me", tokens["CB_DEV_EXPIRED_TOKEN"])[0] == 401
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
for role in ("OPERATOR", "READER"):
    token = tokens["CB_DEV_" + role + "_TOKEN"]
    code, me = request("/api/v1/me", token)
    assert code == 200 and me["scope"] == "community-brain-dev"
    assert set(me["permissions"]) == (
        expected
        if role == "OPERATOR"
        else {"jobs:read", "artifacts:read", "retrieval:read"}
    )
    assert request("/api/v1/jobs", token)[0] == 200
    assert request("/metrics", token)[0] == 403
    assert (
        request(
            "/api/v1/jobs/00000000-0000-0000-0000-000000000001/publications/git",
            token,
            "POST",
            {},
        )[0]
        == 403
    )
    if role == "READER":
        assert (
            request(
                "/api/v1/sources",
                token,
                "POST",
                {
                    "meeting_id": "auth-negative-fixture",
                    "kind": "chat",
                    "content": "synthetic",
                },
            )[0]
            == 403
        )
    print(role.lower() + ": scope/permissions/read access verified")
print(
    "PASS: health; missing, malformed and expired token rejection; reader write denial; metrics denied; no publication permission"
)
