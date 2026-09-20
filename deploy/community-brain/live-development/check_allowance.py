"""Read-only provider verification on VM; no inference endpoint is called."""

import json
import urllib.request

from compose import RUNTIME, read_env

private = read_env(RUNTIME)
request = urllib.request.Request(
    "https://openrouter.ai/api/v1/key",
    headers={"Authorization": "Bearer " + private["CB_OPENROUTER_API_KEY"]},
)
try:
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.load(response)["data"]
    fields = (
        "limit",
        "limit_reset",
        "limit_remaining",
        "usage",
        "is_management_key",
        "include_byok_in_limit",
    )
    safe = {key: data.get(key) for key in fields}
    assert safe["limit"] == 5 and safe["limit_reset"] is None
    assert (
        isinstance(safe["limit_remaining"], (float, int))
        and safe["limit_remaining"] > 0
    )
    assert safe["is_management_key"] is False and safe["include_byok_in_limit"] is True
    print(json.dumps(safe, sort_keys=True))
except Exception:  # noqa: BLE001 - do not expose credential-bearing HTTP diagnostics
    raise SystemExit(
        "Allowance verification failed or is uncertain; model calls must remain disabled"
    ) from None
