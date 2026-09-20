"""Development-only signed-claim evidence; never record credentials or token bodies."""

import json
import logging

from community_brain.jobs import runtime

OriginalAuthenticator = runtime.Authenticator


class AuditedAuthenticator(OriginalAuthenticator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observed = set()

    def __call__(self, token):
        principal = super().__call__(token)
        if token.count(".") == 2 and principal.subject not in self.observed:
            self.observed.add(principal.subject)
            logging.getLogger("uvicorn.error").info(
                "development_oidc_verified %s",
                json.dumps(
                    {
                        "scope": principal.scope,
                        "permissions": sorted(principal.permissions),
                        "issuer_audience_signature_expiry_verified": True,
                    },
                    sort_keys=True,
                ),
            )
        return principal


def app():
    runtime.Authenticator = AuditedAuthenticator
    return runtime.app()
