# CBM-08 live assessment — September 20, 2026

Actor: Codex on Forge. Scope: Patrick's requested evidence review, local Git
reconciliation and current-solution assessment before deciding further work.

Result: **evidence review complete; CBM-08 acceptance remains open**. Only one
new-meeting production loop is complete, with documented manual recovery. Current
automatic execution is stopped and service identity renewal has failed.

| File | Method / what it establishes |
| --- | --- |
| `live-data.json` | Existing API container, SQLAlchemy connection with `default_transaction_read_only=on`, repeatable-read/read-only transaction; allowlisted job/stage/attempt metadata, counts and 72 SHA-256 reference checks. LanceDB read-only mounted corpus statistics; no index mutation. Meeting dates separately read from `identity.local_date`. |
| `live-runtime.json` | VM109 marker/maintenance reads; allowlisted Docker metadata and service identity expiry/scope projections; authenticated API and real hybrid retrieval checks. Probes used existing runtime token privately on VM109; no token value exported. |
| `artifact-api.json` | Existing scoped read probe: actual job status and six artifact downloads, checked for size/hash without exporting their contents. |
| `checkpoint-integrity.json` | Re-hash acknowledged checkpoint manifest and its ten files on VM109. This does not replay a backup or certify a new restore/off-host copy. |
| `source-parity.json` | SHA-256 comparison of effective API package, frontend and selected config files against Forge. Runtime registries are not copied into source. |
| `worker-parity.json` | Effective automatic-worker and first-publication Python workspace hashes compared with local modules/helpers. |
| `https-frontend.json` | Real Forge HTTPS GET of active HTML/JS/CSS; verified TLS with production CA bundle read over authenticated SSH; exact local-build match. |
| `infrastructure.json` | `forge-infra-read pve resources`, limited in this receipt to VMs 101/108/109. No infrastructure mutation. |
| `public-release.json` | Anonymous GitHub release metadata read; current release identity and asset digests. The actual installer/container rehearsal remains September 17 evidence. |
| `verification.json` | Fresh canonical test/build results and source-control checks. |

The metadata captures span approximately 01:11–01:20 UTC. They are observations,
not a single globally atomic snapshot. No active stage was observed; production
was not quiesced for this read-only review. The checkpoint and file integrity
checks are independently bounded reads.

Limitations: current Mac ownership/renewal implementation and PVE backup internals
were not directly audited; VM109's current management projection reports renewal
failure and verified nightly backup. No fresh human OIDC/Open WebUI acceptance,
Fathom acquisition, paid generation, queue execution, restore, deployment, secret
rotation or publication was performed. No management action request was sent.
The real query used the retained Ollama embedding service; returned text was
discarded and only metadata retained.

The original September 18 runner error's root cause is unresolved. Its retained
marker records only `RuntimeError`, and current logs provide no underlying
exception. The September 19 boot hold is separately established by boot/pause
records and the installed boot-guard source.

See [current assessment and continuation](../../cbm-current-state-and-continuation.md)
for the acceptance ledger, deployment differences and prioritized next decisions.
`receipt-manifest.json` binds these evidence files; it excludes itself.
