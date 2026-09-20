"""Image boot checks against disposable services only; no provider calls."""

import asyncio
import json
import urllib.error
import urllib.request

import nats


def get(path, authenticated=False):
    headers = (
        {"Authorization": "Bearer cbm-disposable-fixture"} if authenticated else {}
    )
    request = urllib.request.Request("http://api:8090" + path, headers=headers)
    with urllib.request.urlopen(request, timeout=10) as response:
        return response.read()


async def main():
    assert json.loads(get("/health")) == {"status": "ok"}
    assert b"<html" in get("/").lower()
    assert b"<html" in get("/callback").lower()
    try:
        get("/api/v1/jobs")
    except urllib.error.HTTPError as error:
        assert error.code == 401
    else:
        raise AssertionError("Unauthenticated API request was accepted")
    assert json.loads(get("/api/v1/me", True))["scope"] == "cbm-rehearsal"
    assert json.loads(get("/api/v1/jobs", True))["items"] == []
    nc = await nats.connect("nats://nats:4222", connect_timeout=5)
    try:
        js = nc.jetstream()
        await js.add_stream(name="CBM_BOOT", subjects=["cbm.boot"])
        receipt = await js.publish("cbm.boot", b"fixture")
        assert receipt.seq >= 1
        message = await js.get_last_msg("CBM_BOOT", "cbm.boot")
        assert message.data == b"fixture"
    finally:
        await nc.close()
    print("PASS: image, migration, API authorization, SPA and JetStream storage")


if __name__ == "__main__":
    asyncio.run(main())
