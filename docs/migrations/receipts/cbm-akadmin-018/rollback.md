# Scoped rollback for request018

Rollback removes only akadmin's Community Brain grant and keeps pchouinard
functional. Do not restore the entire pre-change Authentik snapshot: the old
four-way group AND denied pchouinard too.

1. Hold the existing Mac management scheduler mutex, verify no pending recovery
   checkpoint, and compare current mappings/policies/memberships with verified.json
   and changed-controls.json. Stop on drift.
2. In one Authentik database transaction, resolve akadmin by pk 4 AND UUID
   dfae6a7f-e5a5-4575-9796-8187cbdd45b1. Remove only that user from groups
   69a3fcd8-fc2d-4ad2-b565-41f15c40701a and
   291e026d-b5d5-4871-beb2-af01750233b3. Keep every other membership.
3. In the new app-local identity policies and the two scope mappings listed in
   applied.json, remove only the pk4/UUID pair. Retain the active-user check,
   app-specific group check, pchouinard's pk6/UUID pair, and each app's existing
   permissions. Keep the two active bindings per app. Keep the six unrelated
   platform-group bindings disabled; re-enabling them breaks pchouinard access.
4. Update the source and live human_access.py HUMANS dictionary to retain only
   pk6; update management_controls.py's expected group members from [4,6] to [6].
   Update both source provision-auth.py group users/members and their current
   public-settings.json metadata to pchouinard only. Regenerate the claim and
   policy expressions with that one-identity definition, retaining all provider
   settings. Do not restore historical source expressions with weaker checks.
5. Evaluate actual Authentik policies and claim previews: pchouinard must remain
   allowed with the same per-app claims; akadmin must be denied with no claims.
   Repeat inactive, nonmember and mismatched identity cases. Capture a new current
   management-control snapshot and verify both off-host copies. Preserve the
   request018 capture and every historical checkpoint unchanged.

The original snapshots are diagnostic/recovery evidence, not an instruction to
restore unrelated settings or recreate the original login failure. Browser
sessions/tokens may retain old claims until their existing lifetimes expire or a
normal fresh login occurs; token/session settings were not changed.
