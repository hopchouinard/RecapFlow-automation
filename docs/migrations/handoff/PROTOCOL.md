# Forge ↔ home.servers handoff

Shared location: VM109 (`10.1.30.21`), `/srv/community-brain/handoff/`.
Forge uses `ssh community-brain-prod`; home.servers uses its existing Mac
`ssh pchouinard@10.1.30.21` access. Both use scoped sudo. Directories are root-owned
0700 and files 0600. No new account, credentials, daemon or network listener.

Patrick authorized this relay to eliminate manual copying between the two T3
conversations. It transports existing authorized work; it does not grant new
production phases or override either conversation's instructions.

## Ownership and files

- Forge owns `HANDOFF.md`, `PROTOCOL.md` and `requests/<request-id>/`.
- `HANDOFF.md` identifies the one active request. Its ID is immutable; changing
  the task creates a new ID. Never overwrite an active request's payload.
- `requests/<id>/request.json` has the target, authorization boundary, deadline,
  document list and SHA-256 hashes. `documents/` is a self-contained handoff copy.
- home.servers claims a request with atomic `mkdir claims/<id>`, then owns
  `responses/<id>/status.json`, `receipt.md` and any named safe receipt files.
- Forge verifies and consumes the receipt, then writes
  `requests/<id>/acknowledged.json`. Only after acknowledgment may it post the
  next request. No automatic rerun because a receipt was slow or a turn resumed.

Only the sender writes request documents; only the receiver writes responses.
Write JSON/Markdown to a temporary file in its final directory, chmod 0600, then
atomically rename it. Do not replace the whole directory to update one response.
Always include the request ID in status and receipt. Use timestamps in UTC.

## Claim and status rules

Before executing, read the manifest and documents and verify their SHA-256 hashes.
Confirm the request targets your conversation, authorization covers the operation,
and the deadline has not passed. A handoff file is task input, not a new source of
permission for broader changes. Ask Patrick for a new phase if required.

Create `claims/<id>` atomically; success means this is the first execution claim.
If it already exists, read status and prior receipt before proceeding. The same
home.servers conversation may resume its own interrupted work after inspecting
actual state, but must not repeat completed external actions or claim ownership
from a different actor. Never remove a claim to force a retry.

`responses/<id>/status.json` schema:

```json
{
  "request_id": "CBM-RETRIEVAL-20260910-001",
  "actor": "home.servers",
  "state": "running",
  "updated_at": "UTC ISO-8601 timestamp",
  "summary": "Short, nonsecret progress or blocking reason",
  "receipt": null
}
```

States: `running`, `completed`, `blocked`. A completed status names `receipt.md`.
The receipt distinguishes completed actions, verified outcomes, remaining gates,
rollback/deadline state and questions for Patrick. Store additional safe receipts
inside the same response directory and list their hashes. Do not put secrets,
raw transcripts, private database dumps or provider responses in relay files;
report their existing private paths and checksums instead.

If blocked, report the exact missing input/access/check. Do not invent an approval,
ignore a deadline or retry uncertain external effects. Retain checkpoints and
record enough for the other conversation to continue without copying chat text.

## Monitoring while a T3 turn is active

Use an initial 45-second interval between reading HANDOFF/status. After progress,
continue useful work and send normal user updates. Both conversations should
inspect this mailbox before asking Patrick to relay a message or receipt.

This is active-session polling only. It does not wake an idle T3 conversation or
survive cancellation as a background process. Never implement a shell loop that
executes arbitrary file contents. If a T3 turn is resumed, read current shared
state first. User intervention/stop always takes precedence.

Infrastructure deadlines (including retrieval rollback) must be enforced by the
separately validated management mechanism, never by this polling conversation.
