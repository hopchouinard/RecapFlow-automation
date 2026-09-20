# Dark mode deployed — September10,2026

Patrick requested a dark-mode switch before subsequent migration work.
The workspace and sign-in/error screens now offer a keyboard-accessible switch,
with system-preference default and locally remembered explicit choice.

Build/typecheck, component and browser checks passed, including keyboard toggle,
reload persistence,390px mobile layout and literal Markdown preview/download.
The exact static bundle also passed an isolated VM108 HTTP hash check.

Management request CBM-DARK-MODE-20260910-008 deployed the read-only static bundle
at16:24UTC, retaining prior hashed asset URLs. Backend image and API environment
are unchanged; effective recreation manifests and private/off-host rollback
copies were updated and verified. Seven HTTP and15 scope/health checks passed.
Database, managed files, corpus/config and terminal ownership controls are unchanged.

Forge verified all15 management receipt files, matched the deployed asset manifest
to the original build and independently fetched all3 new assets over verified
HTTPS. The shared request is acknowledged. Receipts are in
cbm-dark-mode-receipts-20260910/. Patrick confirmed the dark mode works perfectly and authorized resuming migration
work. Visual acceptance is complete. Publication and retirement remain gated.
