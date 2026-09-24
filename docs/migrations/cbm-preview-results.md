# Markdown preview and collapsed navigation — deployed and verified

Patrick requested a Raw/Rendered Markdown toggle and collapsed year/month branches.
Both archive and Recent runs now share FilePreview. Raw is the default, text files
remain literal, and copying/downloading always uses the original bytes. CommonMark
and GFM previews include headings, lists, tables, task lists and code. Raw HTML and
unsafe links are not executed; external images are text labels. Theme-aware content
and controls were checked in the mobile browser screenshot.

All date branches start closed. Date search opens matches; clearing search closes
all branches. Existing automatic submission and recent-run behavior are preserved.

Six frontend tests, three Playwright scenarios and build/typecheck passed. Exact
three-file static packet passed in the pinned image on VM108 with network=none;
the disposable container was removed.

Management completed request CBM-PREVIEW-20260910-012 at
2026-09-10T21:05:43 UTC. Forge verified all eight management evidence hashes and
independently fetched the HTTPS root, JavaScript and stylesheet: all three match
the tested packet byte for byte. Scoped live API checks confirm automatic
processing enabled, 87 meetings, 481 archive files and one visible real job; the
automatic runner is idle. Management reports unchanged database fingerprints and
managed content, 1,901 corpus rows fully indexed, and verified off-host copies of
before/after deployment controls. Previous hashed assets remain available.

Evidence: [management receipt](receipts/cbm-preview-20260910-012/receipt.md),
[live asset hashes](receipts/cbm-preview-20260910-012/forge-live-assets.json),
[live API checks](receipts/cbm-preview-20260910-012/forge-live-api.json).
The accompanying automatic recovery operations receipt documents the installed
scheduler, recovery acceptance and rollback controls, including preservation of
request011 postactivation controls. Deployment was not replayed.

No production submission or model call was made for this interface update.
Publication, historical replacement and retirement remain gated. Patrick can
refresh the live workspace to validate the Raw/Rendered toggle and initially
collapsed navigation; production browser acceptance of these two changes is
pending that check.
