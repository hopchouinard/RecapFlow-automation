# CBM-MANUAL-PREP-20260910-003 — activation guard finding

The existing collector-development/nginx.conf allows POST /api/v1/sources without inspecting JSON kind. jobs/api.py enforces chat-only uploads only when the caller lacks sources:upload and uses sources:upload:chat. Therefore the requested sources:upload production collector is not chat-restricted by the existing proxy. The existing Mac tool sends chat but is not an authorization boundary.

Management is preparing separate inactive requested credentials/configuration, preserving live identities and clients. Before activation, Forge must either deliver a verified chat-only enforcing proxy/API path that cannot be bypassed with this credential, or post a corrected scoped request selecting the already-supported sources:upload:chat permission. Do not activate the broad collector map on the ordinary API based on the existing proxy alone. No production API or collector activation has occurred.
