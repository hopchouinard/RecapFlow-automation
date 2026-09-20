#!/usr/bin/env bash
# Forge-only user-space Chromium libraries; no sudo or system package installation.
set -euo pipefail
cache="${XDG_CACHE_HOME:-$HOME/.cache}/cbm-test-services"
mkdir -p "$cache/packages" "$cache/root"
cd "$cache/packages"
apt-get download libatk1.0-0t64 libatk-bridge2.0-0t64 libatspi2.0-0t64 \
  libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2t64 \
  libdrm2 libwayland-server0 libxrender1 libxi6 libxres1 fonts-dejavu-core
for package in ./*.deb; do dpkg-deb -x "$package" "$cache/root"; done
python3 - "$cache" <<'PY'
import html, pathlib, sys
root=pathlib.Path(sys.argv[1])
fonts=html.escape(str(root/'root/usr/share/fonts/truetype/dejavu'))
cachedir=html.escape(str(root/'font-cache'))
(root/'fonts.conf').write_text(f'<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>{fonts}</dir><cachedir>{cachedir}</cachedir></fontconfig>')
PY
