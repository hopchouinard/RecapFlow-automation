# Fathom call URL and approximate time — development verified

Patrick specified https://fathom.video/calls/821559116 and a +/-10-minute
recording-start tolerance. Implemented URL normalization in the new-meeting form,
call-ID matching against Fathom meeting url/share_url as well as native recording
IDs, and inclusive600-second timestamp tolerance. Transcript fetch uses the
resolved API recording ID. SelectedFathom guard now allows only that resolved
transcript endpoint while retaining its5-page/1-transcript ceilings.

The metadata query still spans a bounded surrounding date window because Fathom's
created_after/before filters refer to creation time, not necessarily recording
start. The selected recording's actual start must pass the +/-10-minute check.
No nearest-meeting fallback, unrelated transcript fetch or model calls.

20 acquisition tests passed, including numeric/full call URL with offsets-601,
-600,-230,+600,+601 seconds through the actual selected worker guard. Six frontend
tests, three browser scenarios and typecheck/build passed. Existing unrelated
working-tree changes preserved. Production received these code changes under request019; see closure below.

Live VM108 isolated acquisition succeeded using fullURL and entered time
2026-09-15T22:00:00Z. Resolved recording183401214 started21:56:10Z (17:56:10Toronto).
One metadata request and one transcript request.86,144bytes, SHA256
76c44ab52cd4105d6c4d9fd0762c5d4a6e72f9ffc10721175f4969368a918cd5.
Only disposable container access to the private Fathom bundle and dedicated output
folder; no app/database/corpus volumes or processing provider key. Container removed.
First container invocation failed before acquisition because staged source files
were0600; corrected source-only readability and reran. No production write.

Private transcript and receipt:
/srv/dev-data/artifacts/cbm-fathom-fix-20260917/ on VM108.
Source packet: /srv/dev-data/workspaces/cbm-fathom-fix-20260917/.
Local safe receipt: cbm-fathom-fixed-dev-receipt.json.

Production rollout must include jobs/acquisition.py AND automatic/selected_fathom.py
with updated backend worker mounts/image as appropriate and the rebuilt UI. Merely
updating the UI or selected wrapper leaves the importer unfixed. Preserve existing
weekly guards, Authentik grants, latest extraction config and management pins.
Historical Sept15 production transcript/output stays unchanged; no reprocessing.
Automatic fallback after a manually supplied transcript and actionable acquisition
error messages remain separate follow-up improvements, not fixed by this patch.


## Request019 production closure

Management deployed2026-09-17. Forge verified all12 receipt-file hashes, trusted
HTTPS root/JS/CSS against the approved packet, and both deployed acquisition.py
and selected_fathom.py bytes. Actual manual_host.py mounts acquisition.py in the
worker module directory. Runner is idle. Management tested actual worker mounts
using credential-free network-disabled fixtures, including +/-600 accepted and
+/-601 rejected. Database/data fingerprints unchanged,88sessions/1924FTSrows and
zero unindexed. No production transcript fetch or reprocessing used for deployment.

Effective worker packet: /srv/community-brain/workspaces/cbm-fathom-20260917-effective-r019.
Evidence: receipts/cbm-fathom-019/receipt.md and fixture-result.json. Request019
acknowledged. Next new production acquisition is the live production acceptance;
selected real September15 acquisition already passed on isolated VM108.
