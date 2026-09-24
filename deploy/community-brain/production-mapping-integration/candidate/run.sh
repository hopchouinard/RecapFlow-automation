#!/usr/bin/env bash
set -euo pipefail
set +x
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Admission is checked before login or any authority/helper side effect.
python3 -B "${script_dir}/wrapper_guard.py" "$1"
source "${script_dir}/../deployed-mac/platform-services/scripts/lib/infisical.sh"
infisical_load_env
infisical_login
project_id="$(infisical_project_id)"
# Existing folders must already exist. This wrapper never creates authority scope.
infisical_folder_exists "$project_id" prod /applications community-brain
exec python3 -B "${script_dir}/effect_entry.py" "$1"
