#!/usr/bin/env bash
set -euo pipefail
set +x
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/../../scripts/lib/infisical.sh"
infisical_load_env
infisical_login
project_id="$(infisical_project_id)"
infisical_ensure_folder_path "$project_id" prod /applications/community-brain
if [[ "$1" == provision-auth.py ]]; then
 infisical_get_secret_var CBM_AUTH_URL AUTHENTIK_API_URL "$project_id" prod /platform/authentik
 infisical_get_secret_var CBM_AUTH_TOKEN AUTHENTIK_API_TOKEN "$project_id" prod /platform/authentik
 export CBM_AUTH_URL CBM_AUTH_TOKEN
fi
if [[ "$1" == provision-app-dns.py ]]; then
 infisical_get_secret_var T3_UNIFI_HOST UNIFI_HOST "$project_id" prod /network/unifi-cloud-gateway
 infisical_get_secret_var T3_UNIFI_KEY UNIFI_API_KEY "$project_id" prod /network/unifi-cloud-gateway
 export T3_UNIFI_HOST T3_UNIFI_KEY
fi
exec python3 "${script_dir}/$1"
