# Request031 verification receipt

Development implementation and verification completed. Commit `39b9b21cc681b4bde762f30bb0193778d9b295ec` on `codex/request031-capture-controller`; not pushed. Parent gitlink unchanged.

Final source packet: `415166b1c98cdc3e76c8678fc5954b62f2c7239ab11e01d4e0ea58c1c499a962`. All 32 files match VM108 bytes; all 19 Forge files imported exactly and all 15 inherited Request030 files unchanged.

## Verification

- Eight final-packet scenarios passed: positive capture/independent PostgreSQL restore, SSH-client SIGKILL, Mac-caller SIGKILL, real DB-fence termination, worker SIGKILL, supervisor SIGKILL, supervisor SIGSTOP/systemd expiry, and capture deadline expiry.
- Every serving stop recovered the exact incumbent ID within its absolute deadline. Holds remained unchanged. Duplicate dispatch, all three held VM locks and competing Mac dispatch were refused. A fresh raw target competitor also failed before any stop intent; its uncertain attempt is retained without replay.
- 35 database/candidate negatives and 16 specification/real-lock negatives rejected.
- VM108 Forge: 49/49 passed. Native Mac Forge: 44/49 passed, five fixture setup errors from unsupported extended metadata; no suppression or core changes. Actual Mac/SSH interruption tests passed.
- Existing activation boundaries: 19 passed. Parent inventory suites: 293 passed. Production compiler and controller refusals remain intact; all 21 production evidence slots remain null.
- All 55 pre-existing dev containers and both production containers retained IDs, config hashes, running state, start times and restart counts. Production hold hashes/inodes/modes and retained Request020 bytecode match baseline. VM101 was not touched.

## Retention and limitations

All 27 attempts, six sealed source packets, component evidence and partial captures remain under `/srv/dev-data/workspaces/cbm-capture-controller-20260921-031`. Only the 28 recorded fresh Request031 containers were stopped after recovery verification; none or their data were deleted.

The first packet failed its fresh-incumbent startup health check before stopping anything. A reviewed v2 finalizer closed that pre-stop attempt after confirming the same healthy incumbent and holds; the immutable attempt was retained. Subsequent packets fixed fixture readiness, strengthened database/schema/source binding, and were retested. Historical v1 recovery is not claimed as final-packet proof.

Recovery is bounded only while the VM, systemd, Docker, filesystem and bound controls remain available. Host failure, reboot, changed controls or failed finalization are not guaranteed to restore serving within deadline. The candidate is not installed, its pending intent is not consumed by the production scheduler, and its synthetic DB validator is not a full production catalog/writer-admission validator. See `OPERATOR-PROPOSAL.md` for the next concrete gate.

Read-only identity metadata at 2026-09-21 15:12:47 UTC showed the four relevant expiries still at 2026-09-22 20:53:07 UTC. No renewal, rotation, production maintenance/capture/transfer/cutover/resume, VM resize or provider spend occurred. No private content or signing material is in this relay package.

Machine receipts: `verification-results.json`, `vm108-audit.json`, `preservation.json`, final `*6-client-result.json`, evidence/boundary receipts, and `artifact-manifest.json`. Source: archive, source manifest, lineage and commit patch.
