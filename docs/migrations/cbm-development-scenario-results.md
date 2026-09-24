# Durable application rehearsal — 2026-09-09

Executed on authorized PVE1 VM 108, using the image from the standalone boot
rehearsal, isolated project `cbm-scenario`, and development fixtures only.
Production services, identities, intake and remote publication were unchanged.

## Results

| Check | Observed outcome |
| --- | --- |
| HTTP submission | Weekly and historical jobs accepted; repeating the idempotency key returned the same job |
| Durable execution | Real SQLAlchemy store, outbox publisher, JetStream pull consumer, worker claims, model journal and artifact promotion |
| Weekly output | Six artifacts, each fetched through the API and SHA-256 verified |
| Historical output | Three artifacts, each fetched through the API and SHA-256 verified |
| Indexing | Actual ingestion/chunking/extraction validation, LanceDB schema, writes and FTS index; providers simulated |
| Retrieval | Actual authenticated hybrid query through the mounted retrieval API, including existing `X-API-Key` transport; nonempty structured ground truth |
| Process restart | Restarted API/worker; artifact hashes and model-call count unchanged |
| Interrupted effect | SIGKILL during a simulated provider call; real lease expiry produced `outcome_unknown` |
| Reconciliation | Missing duplicate-effect acknowledgment rejected with 409; explicit fixture acknowledgment allowed recovery |
| Coordinated restore | Stopped writers, dumped PostgreSQL and archived files/config/corpus, deleted all project volumes, restored into fresh volumes |
| Queue loss | Started fresh JetStream; an accepted pending job completed from the restored database outbox |
| Restore integrity | Previously completed artifact hashes and model-call counts unchanged; four jobs ultimately succeeded with complete indexing |
| Local Git output | Actual Git handler committed/pushed to a disposable bare repository; receipt and hashes verified; repeated request idempotent |
| Consumer output | Actual distribution handler built and reopened package with four sessions; status `validated`; no release pointer or remote release |

Six deployment configuration/isolation tests and Ruff checks passed on Forge.
These container checks complement the prior unit/integration suite; they do not
measure model quality, embedding relevance, real OAuth login, or production ACLs.

## Simulation boundary

`deploy/community-brain/rehearsal/fixture_runtime.py` injects deterministic model
responses into the existing worker and mocks only the ingestion LLM boundary.
A local Ollama-shaped HTTP endpoint returns synthetic 768-dimensional embeddings.
The real ingestion, LanceDB, package, Git and retrieval code runs unchanged.
These scripts are bind-mounted only for rehearsal and are excluded from the
application image by its Dockerfile ignore rules. No production auth bypass or
alternate model routing was introduced.

`compose.scenario.yml` has an internal network and no host port bindings. The API
mounts corpus/config read-only; a one-shot fixture initializer owns the private
project volumes. Fixture tokens have explicitly scoped permissions and expiry.
Keep the rehearsal directory traversable (0755) and scripts readable (0644) for
container UID 10001; the source directory's original 0700 mode initially blocked
the bind-mounted helper and was corrected before successful execution.

## Reproduction

Sync the reviewed Compose file and `rehearsal/` helpers to the existing development
build context. Use `compose.scenario.yml` alone; do not merge it with production.
Build `community-brain:rehearsal` using the standalone instructions first.

The normal sequence is:

```sh
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml up -d --wait --wait-timeout 180 api worker
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml run --rm scenario
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml restart api worker
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml run --rm scenario python /checks/scenario.py check
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml run --rm scenario python /checks/scenario.py interrupt
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml kill -s SIGKILL worker
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml start worker
docker compose --env-file /dev/null -f deploy/community-brain/compose.scenario.yml run --rm scenario python /checks/scenario.py reconcile
```

Wait for API health after restarts. The interrupt command waits for the effect
marker before returning. Reconcile waits for the real lease to expire; it does
not accelerate the database clock or alter durable state directly.

For restore: stop the worker, run `scenario.py pending`, stop the API, then make
the coordinated dump/archive. Restore those into fresh project volumes and
start `api worker` (which provisions an empty fixture stream). Run
`scenario.py restore-check`, then `scenario.py publish`. Preserve evidence before
`down --volumes`, which removes only this disposable project's state.

## Evidence and resource use

Evidence is on the VM at `/srv/dev-data/artifacts/cbm-scenario-20260909/`.
The recovery-point files are:

- `database.dump`: SHA-256 `30bab22840147b1b9c9699d8b70592f44f323b8a768e4aa8b4fa8832b7959ec2`
- `files.tar`: SHA-256 `812dd86056cb1cb31f7f482ac88c0fb81be046d7cc7997324cca51ecd66c2271`

Final evidence also includes scenario logs, final database/files snapshots and
the reviewed scenario configuration/helpers. All contents are synthetic fixtures.

Post-test Docker memory snapshot: worker 153.8 MiB, API 174.1 MiB, simulated
embedding endpoint 146 MiB, PostgreSQL 39.62 MiB, NATS 4.281 MiB (~518 MiB total).
This is not a peak production sizing result. No local LLM is hosted.

Next: separate development Authentik/Infisical setup, as selected by Patrick.
Live paid-model work awaits the development key and explicit budget decision.

## Manual-input worker follow-up

The worker now treats Fathom acquisition as optional when no key is configured.
Sixteen targeted runtime/auth/deployment tests passed, including configured and
absent acquisition adapters. A rebuilt image passed the standalone boot and
smoke checks again, then its disposable stack was removed:
`sha256:5e234ec55b2bf0f8aa42d39b721fd3e0c219d674860ca0729db2e2c98c1d6259`.
The extended scenario above used the preceding image; its provider simulation
did not depend on the optional-acquisition entrypoint change.
