# Approved development collector: management delivery needed

Patrick approved this integration on 2026-09-09. Production changes, recurring
Mac sync and remote publication remain prohibited. No further permission is
needed for the approved scope; the blocker is missing CA/Infisical provisioning
access in Forge. Do not transfer management credentials to work around it.

## Prepared and verified

DNS inspection confirms `community-brain-dev.patchoutech.lab` → `10.1.30.20`.
VM UFW currently permits only SSH from Forge `10.1.10.60` and Mac `10.1.50.219`.
No port 443 service, CA issuance client or Infisical bootstrap is installed.
The infrastructure broker supports read-only queries, not issuance or secret writes.

The staged proxy is `deploy/community-brain/compose.collector-development.yml`:
digest-pinned cached nginx, host networking, listener `10.1.30.20:443`, upstream
`127.0.0.1:8090`, 128 MiB memory ceiling, source allowlist for those two addresses.
Only health and source-upload paths are exposed. No public route, port 80,
shared Traefik change or Authentik redirect change is needed. This endpoint is
for the manual collector; existing browser login stays on its localhost tunnel.

Compose and `nginx -t` passed using a disposable fixture certificate, now removed.
Validation corrected temp-directory permissions/paths for the read-only container.
The proxy is **not running** and the firewall is unchanged.

## Deliver through the existing Mac management environment

1. Issue a lab-CA server certificate with DNS SAN
   `community-brain-dev.patchoutech.lab`. Keep certificate/key lifecycle in the
   approved Infisical/CA workflow. Deliver to VM 108, root-owned:
   `/etc/community-brain-development/collector-tls/fullchain.pem` and `key.pem`,
   directory 0700, key 0600. Include intermediates in fullchain; the Mac and VM
   must trust the issuing lab CA. No production key reuse.
2. Provision a new random collector token in Infisical `homelab`, environment
   `development`, path `/applications/community-brain`, proposed name
   `CB_DEV_MAC_COLLECTOR_TOKEN`. Subject `community-brain-dev-mac-collector`, scope
   `community-brain-dev`, **only `sources:upload:chat`**, expiry
   `1789069401` (September 10, 2026 at 19:43:21 UTC). If provisioning occurs after
   that expiry, choose and report a new bounded expiry instead.
3. Append its SHA-256/subject/scope/permissions/expiry record to the authoritative
   development `CB_SERVICE_IDENTITIES` array and rerender VM `runtime.env` using
   the existing workflow. Preserve all existing identities and flags. Do not
   install the raw token in the API, model worker, Forge checkout or chat.
4. Deliver a mode-0600, Mac-user-owned private file at
   `~/Library/Application Support/CommunityBrainDevelopment/collector.json`, with
   keys `backend`, `token`, `expires_at`. Backend must be
   `https://community-brain-dev.patchoutech.lab`. Report delivery paths and expiry
   only, never values. Do not send the file back to Forge.

After delivery, this migration agent can validate cert/key match, chain/SAN and
expiry, recreate only the development API with the added identity, add UFW rules
for TCP 443 from the two approved source addresses, start the prepared proxy,
and verify TLS plus authorization. No upstream network ACL changes are inferred;
if Mac-to-VM reachability is denied upstream, management must inspect that path.
No certificate or identity was created outside Infisical to bypass this dependency.

## Exact manual Mac exercise after endpoint validation

Copy these two reviewed source files into a private Mac development tools directory:
`deploy/community-brain/collector-development/manual_upload.py` and
`community-brain/src/community_brain/jobs/acquisition.py`, adjacent to one another.
Use Python with the project's `httpx` dependency and trusted lab CA bundle
(`SSL_CERT_FILE` when needed). The agent will confirm the final local tool path
and selected relative Zoom path before invocation.

```sh
python3 /path/to/development-tools/manual_upload.py 'relative/path/under/Documents/Zoom/chat.txt'
```

The runner requires the exact already-selected file hash
`5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084` and recording
`181075701`. It uses the collector's safe path/read logic and checks the hash
on the same in-memory content that is uploaded, before any HTTP request. It
prints only source receipt metadata. The existing source API deduplicates the
matching hash. No raw chat is printed, unrelated recording submitted, job created
or model call started. No timer, folder action or production sync edit is included.

Rollback removes only this proxy and its two new UFW rules and revokes the new
development collector identity through Infisical. Preserve existing development
identities, source/artifact state, and all production configuration.
