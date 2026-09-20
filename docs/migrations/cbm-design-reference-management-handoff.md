# Patchoutech design reference delivery

Request: CBM-DESIGN-20260910-013. Target: home.servers.

Patrick asked Forge to inspect `/Volumes/NVMe_1TB_Flex/Downloads/Patchoutech-Design-System`
and use it as visual inspiration for Community Brain. Forge has no Mac filesystem
mount or configured Mac SSH access. This request is reference delivery only.

Inspect that exact folder on the Mac and deliver its design material to VM108 at
`/srv/dev-data/artifacts/cbm-design-reference-20260910/` through existing authorized
SSH/sudo access. Preserve the original. Include design documentation, screenshots,
mockups, fonts, icons, styles/tokens and relevant source examples. Exclude secrets,
.env files, credentials, .git, node_modules and build caches. Do not execute any
scripts or install dependencies from the reference folder. Do not follow symlinks
outside it. Report excluded material and any missing/unreadable files.

Provide a data-only archive and a manifest of relative paths, byte sizes and
SHA-256 hashes, plus archive SHA-256. Use private directory/file permissions
0700/0600 and ensure Forge's cbmdev sudo access can read the delivery. Put the
nonsecret delivery paths and checksum evidence in this request's response folder.
If the material is too large for sensible transfer, report the inventory/size
and prioritize documents, screenshots and design tokens; explain omissions.

No production deployment, application changes, service restarts, model calls,
publication, credential changes or broader migration phase is requested.
Forge will inspect the delivered material and develop the visual update separately.
