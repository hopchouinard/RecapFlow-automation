# Request031 consumed: capture controller integration

September21. Forge verified all56 manifest-listed response artifacts (57 including
the manifest), independently matched all32 final packet files on VM108, verified
all19 inherited Forge files unchanged, and imported source unchanged into
`deploy/community-brain/capture-controller/`. Home.servers source commit:
`39b9b21cc681b4bde762f30bb0193778d9b295ec`; not pushed.
Packet manifest: `415166b1c98cdc3e76c8678fc5954b62f2c7239ab11e01d4e0ea58c1c499a962`.
Forge reran the imported49-test suite successfully. Existing immutable fixtures
were not replayed; their actual execution receipts remain the integration evidence.

## Accepted development evidence

Eight final-packet runs covered successful capture/independent PostgreSQL restore,
SSH-client kill, Mac-caller kill, lost DB fence, worker kill, supervisor kill,
supervisor freeze/systemd expiry and capture expiry. Every tested serving stop
restored the exact incumbent within its bound. Holds stayed unchanged; duplicate
and competing dispatch and busy locks were refused.35 database/candidate negatives
and16 specification/lock negatives rejected. Production compilation/controller
refusals remain; all21 production evidence slots are null.

VM108 Forge tests49/49; existing activation boundaries19 and parent inventory293
passed in home.servers receipts. Native Mac Forge tests44/49: five fixture setup
errors from inherited extended metadata. This is not a full Mac test pass. Actual
Mac/SSH interruption runs passed. Keep metadata rejection; resolve fixture
portability separately without editing sealed imported source.

Receipt preservation comparison covers55 pre-existing dev containers, both prod
containers, prod hold identities and retained Request020 bytecode. It does not
certify every production file unchanged. VM101 was not touched.28 new fixture
containers stopped and retained; all27 attempts and six sealed source packets
remain under `/srv/dev-data/workspaces/cbm-capture-controller-20260921-031`.
Earlier failed packets remain historical, not substitutes for final-packet proof.

## Next implementation gate

The controller is synthetic-only, not installed in production. Its systemd recovery
assumes VM/systemd/Docker/filesystem availability and unchanged controls; reboot,
unavailable Docker, changed bindings and failed finalization remain unresolved.
Its pending record is not read by the deployed scheduler. Its database validator
covers a fixed public fixture schema, not production extensions, ACLs, additional
schemas or all writer/DDL/sequence admission.

Next, implement a common admission path for scheduler/manual/capture operations
and recovery of unresolved intents, plus a production-shaped synthetic catalog and
writer-exclusion validator. Validate these on VM108 before requesting production
maintenance. Treat reboot/finalizer failures explicitly; do not promise unconditional
recovery. Close the Mac fixture portability finding while preserving metadata checks.
Then assemble the exact immutable production plan and rollback package for Patrick.
Do not issue a protected transfer request merely because Request031 completed.

Later gates still include protected off-host recovery, real signing/session/browser
acceptance, capacity and any separately authorized provider-spend proof. No private
data/signing transfer into VM108 or anywhere else is authorized now. The earlier
proposed private offline VM108 enclave is not approved by these synthetic receipts;
any future proposal must explicitly reconcile its destination and authorization.

Read-only home.servers metadata at15:12:47UTC reported identity expiry still
September22 20:53:07UTC. That observation is not renewal authority; refresh metadata
before any later bounded phase. Expiry must not bypass development or approval gates.

[Original receipt](receipts/cbm-capture-controller-20260921/receipt.md),
[verification results](receipts/cbm-capture-controller-20260921/verification-results.json),
[Forge source verification](receipts/cbm-capture-controller-20260921/forge-source-verification.json),
[operator proposal](receipts/cbm-capture-controller-20260921/OPERATOR-PROPOSAL.md).
