#!/usr/bin/env bash
# Forge Ubuntu 26.04 only: extract distro binaries, never install/start host services.
set -euo pipefail
cache="${XDG_CACHE_HOME:-$HOME/.cache}/cbm-test-services"
mkdir -p "$cache/packages" "$cache/root"
cd "$cache/packages"
apt-get download postgresql-18=18.6-0ubuntu0.26.04.1 \
  postgresql-client-18=18.6-0ubuntu0.26.04.1 \
  libpq5=18.6-0ubuntu0.26.04.1 nats-server=2.10.27-1build1 \
  docker.io=29.1.3-0ubuntu4.1 docker-compose-v2=2.40.3+ds1-0ubuntu1
for package in ./*.deb; do
  dpkg-deb -x "$package" "$cache/root"
done
"$cache/root/usr/lib/postgresql/18/bin/postgres" --version
"$cache/root/usr/sbin/nats-server" --version
