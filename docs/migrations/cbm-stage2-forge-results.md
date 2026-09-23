# Stage 2 Forge development acceptance — September23

Patrick authorized full stage 2. Forge built a fresh isolated VM108 WebUI/API fixture
from the pinned September integration source and images at
`/srv/dev-data/workspaces/cbm-stage2-webui-20260923-034`. It used generated
synthetic credentials and data only. All13 rendered source/Compose files matched
the retained manifest. The VM's four standing development services remained up.

The actual WebUI logged in, retrieved the expected source chunk through the real
Community Brain development API, and survived the five-identity interrupted
renewal and API/WebUI restarts. Authority storage and the other consumers in this
Forge run were fixtures. A fresh volume preserved synthetic chat, upload, custom
model, prompt, Chroma query and live filter cache. No paid/provider request or
production data was used.

Three concurrent clients completed350 real retrieval/filter request pairs over
90 seconds. The worst pair took1.18 seconds. Across28 VM memory samples, the
minimum available memory was2,094,656KiB. Both containers reported no OOM.
This measures the fixture's retrieval/WebUI profile only; it does not cover the
intended worker plus restore workload or real provider latency. The present4GiB
VM remains the baseline until those measurements justify a change.

The pinned OpenWebUI image's default health command reported `jq ... break` even
while its `/health` and `/api/version` endpoints returned200. A development Compose
health override using the actual JSON health response became healthy after a
container recreation. Read-only verification then passed existing login, actual
retrieval and the restored Chroma query. The override is source for integration
into the qualified renderer; it has not been installed in production.

A preconditioned attempt to disable signup stopped before mutation because the
persisted admin setting was already false. Readback confirmed signup returned403
and existing login still worked. The failed precondition and its script remain in
the private VM108 fixture; no replay was made. Playwright then passed a real
rendered sign-in, confirmed no signup button, and displayed the retained synthetic
chat message before and after page reload. No real user session or original signing
key was used. Those require the separate protected phase.

All four new fixture containers were stopped by Compose after acceptance. Their
IDs, images, volumes, private credentials, journals and synthetic data remain
retained on VM108. The transient SSH browser tunnel closed and its private Forge
credential copy was removed. No existing development or production service was
stopped. No production runtime, VM101 or external authority was changed.

[Safe acceptance](receipts/cbm-stage2-forge-20260923/acceptance.json),
[rendered browser test](receipts/cbm-stage2-forge-20260923/playwright.txt),
[signup readback](receipts/cbm-stage2-forge-20260923/signup-verification.json),
[teardown](receipts/cbm-stage2-forge-20260923/teardown.json).

Stage 2 remains open. [Request034](cbm-stage2-qualification-request.md) is posted
for actual scoped Infisical/CA/consumer acceptance, production-capable controller
source with VM108 failure validation, full workload capacity, and any additional
rendered successor checks. Old production authority/cutoff expired September22;
no prior approval or synthetic receipt can refresh it. Keep all21 production
slots null and both production execution refusals until the later reviewed phase.
