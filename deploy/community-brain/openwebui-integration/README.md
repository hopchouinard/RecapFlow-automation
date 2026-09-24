# VM108: actual Community Brain / OpenWebUI integration

Development only. No production identity, corpus, provider or VM101 dependency.
This harness uses the previously validated application image and exact OpenWebUI
image/filter. It does not add or change runtime application code. The existing
Request026 fixture remains separate and stopped.

Copy this directory's Python files and the unchanged Python files from
`../openwebui-development/` into a dedicated workspace's `source/`; copy
`compose.yml` to the workspace root. Make source readable to container UID10001.
The scripts enforce `/srv/dev-data/workspaces/cbm-openwebui-integration-20260920`
and VM108's hostname/mount. Private generated credentials stay under `private/`
with0700/0600 permissions; never commit them, Compose rendered environments or
private backups. Setup and mutation phases refuse replay markers. Diagnose prior
effects and reconcile state instead of deleting a marker to force reruns.

Run each phase separately with sudo Python on VM108:

```
python3 -B source/run.py setup
python3 -B source/run.py install
python3 -B source/run.py renewal
python3 -B source/run.py restore
python3 -B source/run.py load
```

The authenticated API factory, PostgreSQL records, LanceDB/FTS retrieval, WebUI
login/API, exact filter/live cache and SQLite/Chroma persistence are real. Only
query embeddings and the model list are deterministic isolated HTTP fixtures.
The provider fixture rejects retrieval and inference; a canned retrieval endpoint
cannot satisfy the expected corpus chunk assertion. Services use one internal
Docker network without published ports; host-side checks address bridge IPs.

`service_renewal_policy.py` is an exact copy of the deployed Request024 policy.
Its five subjects and permissions are unchanged. The adapter exercises it against
real API recreation and WebUI delivery/cache verification, interrupts delivery,
verifies old/new overlap and resumes the same prepared generation before revoking
old credentials. **The authority is a private file fixture, not Infisical**, and
the other consumer bundles are fixtures, not installed Kuma, Prometheus or Mac
collector clients. Production renderer/lease/monitoring integration must receive
separate development acceptance. Do not install this development adapter on Mac
or production, or use its file authority as an operational secret store.

Restore uses a consistent stopped synthetic WebUI volume archive, restores to a
new named volume, preserves the separate signing environment, validates all file
hashes before startup and then checks login/data/live retrieval and a Chroma query.
Internal cache symlinks are recorded as links and preserved; escaping links fail
closed. The old fixture volume remains unchanged. If preparation completed and
the stopped-volume boundary failed before writing a backup, `restore-volume`
resumes only that boundary after checking the retained evidence; it does not
replay chat/file/vector creation. Production user data is never used.
The load phase exercises concurrent real retrieval/filter requests and records
memory samples. Small synthetic corpus load does not certify production-scale
capacity or real provider latency; concurrent pipeline observations are separate.

API recreation uses the exact stabilization image and asserts there are no old
package/frontend overlays. It validates this candidate Compose renderer only,
not the still-pinned production management renderer. Stop these services after
acceptance and retain private volumes/receipts for inspection; do not run `down -v`
against an existing fixture with uncertain state or against any other project.
