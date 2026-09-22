#!/usr/bin/env bash

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  echo "source this file from an operator script" >&2
  exit 1
fi

infisical_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFISICAL_REPO_ROOT="${INFISICAL_REPO_ROOT:-$(cd "${infisical_script_dir}/../../.." && pwd)}"
INFISICAL_MANIFEST_PATH="${INFISICAL_MANIFEST_PATH:-${INFISICAL_REPO_ROOT}/platform-services/infisical/homelab-secret-authority.yaml}"
INFISICAL_ENV_FILE="${INFISICAL_ENV_FILE:-${INFISICAL_REPO_ROOT}/.env}"

if [ ! -f "${INFISICAL_ENV_FILE}" ] && [ -f /root/.infisical-bootstrap.env ]; then
  INFISICAL_ENV_FILE=/root/.infisical-bootstrap.env
fi

infisical_log() {
  printf '%s\n' "$*" >&2
}

infisical_xtrace_off() {
  if [[ $- == *x* ]]; then
    set +x
    return 0
  fi

  return 1
}

infisical_restore_xtrace() {
  local xtrace_was_on="$1"

  if [ "${xtrace_was_on}" = "true" ]; then
    set -x
  fi
}

infisical_require_loaded_var() {
  local var_name="$1"
  local xtrace_was_on="$2"

  if [ -z "${!var_name:-}" ]; then
    infisical_log "missing ${var_name}"
    infisical_restore_xtrace "${xtrace_was_on}"
    exit 1
  fi
}

infisical_load_env() {
  local xtrace_was_on=false
  local key
  local value

  if infisical_xtrace_off; then
    xtrace_was_on=true
  fi

  if [ ! -f "${INFISICAL_ENV_FILE}" ]; then
    infisical_log "missing Infisical env file: ${INFISICAL_ENV_FILE}"
    infisical_restore_xtrace "${xtrace_was_on}"
    exit 1
  fi

  while IFS= read -r line || [ -n "${line}" ]; do
    case "${line}" in
      ""|\#*) continue ;;
    esac

    key="${line%%=*}"
    value="${line#*=}"
    case "${key}" in
      INFISICAL_API_URL|INFISICAL_PROJECT_ID|INFISICAL_UNIVERSAL_AUTH_CLIENT_ID|INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET)
        export "${key}=${value}"
        ;;
    esac
  done <"${INFISICAL_ENV_FILE}"

  infisical_require_loaded_var INFISICAL_API_URL "${xtrace_was_on}"
  infisical_require_loaded_var INFISICAL_PROJECT_ID "${xtrace_was_on}"
  infisical_require_loaded_var INFISICAL_UNIVERSAL_AUTH_CLIENT_ID "${xtrace_was_on}"
  infisical_require_loaded_var INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET "${xtrace_was_on}"
  infisical_restore_xtrace "${xtrace_was_on}"
}

infisical_require_cli() {
  if ! command -v infisical >/dev/null 2>&1; then
    infisical_log "missing infisical CLI"
    exit 1
  fi
}

infisical_login() {
  local xtrace_was_on=false
  local login_status

  if infisical_xtrace_off; then
    xtrace_was_on=true
  fi
  if INFISICAL_TOKEN="$(
      INFISICAL_DOMAIN="${INFISICAL_API_URL}" infisical login \
        --domain "${INFISICAL_API_URL}" \
        --method universal-auth \
        --client-id "${INFISICAL_UNIVERSAL_AUTH_CLIENT_ID}" \
        --client-secret "${INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET}" \
        --plain \
        --silent
    )"; then
    login_status=0
  else
    login_status=$?
  fi
  if [ "${login_status}" -ne 0 ]; then
    infisical_restore_xtrace "${xtrace_was_on}"
    return "${login_status}"
  fi

  export INFISICAL_TOKEN

  if [ -z "${INFISICAL_TOKEN}" ]; then
    infisical_log "infisical login returned an empty token"
    infisical_restore_xtrace "${xtrace_was_on}"
    exit 1
  fi
  infisical_restore_xtrace "${xtrace_was_on}"
}

infisical_cli() {
  local xtrace_was_on=false
  local infisical_status

  if infisical_xtrace_off; then
    xtrace_was_on=true
  fi
  if INFISICAL_DOMAIN="${INFISICAL_API_URL}" infisical "$@" \
      --domain "${INFISICAL_API_URL}" \
      --token "${INFISICAL_TOKEN}" \
      --silent; then
    infisical_status=0
  else
    infisical_status=$?
  fi
  infisical_restore_xtrace "${xtrace_was_on}"
  return "${infisical_status}"
}

infisical_manifest_scalar() {
  local key="$1"
  awk -F': *' -v key="${key}" '$1 == key { print $2; exit }' "${INFISICAL_MANIFEST_PATH}"
}

infisical_manifest_list() {
  local section="$1"
  awk -v section="${section}" '
    $0 == section ":" { inside = 1; next }
    inside && /^[A-Za-z0-9_]+:/ { exit }
    inside && /^[[:space:]]*-[[:space:]]/ {
      sub(/^[[:space:]]*-[[:space:]]*/, "")
      print
    }
  ' "${INFISICAL_MANIFEST_PATH}"
}

infisical_project_id() {
  infisical_manifest_scalar project_id
}

infisical_recovery_project_id() {
  infisical_manifest_scalar recovery_project_id
}

infisical_folder_exists() {
  local project_id="$1"
  local env_name="$2"
  local parent_path="$3"
  local folder_name="$4"
  local folders_json

  if ! folders_json="$(
    infisical_cli secrets folders get \
      --projectId "${project_id}" \
      --env "${env_name}" \
      --path "${parent_path}" \
      --output json
  )"; then
    return 1
  fi

  printf '%s' "${folders_json}" | python3 -c '
import json
import sys

needle = sys.argv[1]
data = json.load(sys.stdin)
if isinstance(data, dict):
    entries = data.get("folders", data.get("data", []))
else:
    entries = data
if entries is None:
    entries = []
for entry in entries:
    if isinstance(entry, dict) and entry.get("name", entry.get("folderName")) == needle:
        sys.exit(0)
sys.exit(1)
' "${folder_name}"
}

infisical_ensure_folder_path() {
  local project_id="$1"
  local env_name="$2"
  local folder_path="$3"
  local current_path="/"
  local remainder="${folder_path#/}"
  local part

  if [ "${folder_path}" = "/" ]; then
    return 0
  fi

  IFS='/' read -r -a parts <<<"${remainder}"
  for part in "${parts[@]}"; do
    if [ -z "${part}" ]; then
      continue
    fi

    if ! infisical_folder_exists "${project_id}" "${env_name}" "${current_path}" "${part}"; then
      infisical_cli secrets folders create \
        --projectId "${project_id}" \
        --env "${env_name}" \
        --path "${current_path}" \
        --name "${part}" >/dev/null
    fi

    if [ "${current_path}" = "/" ]; then
      current_path="/${part}"
    else
      current_path="${current_path}/${part}"
    fi
  done
}

infisical_set_secret_stdin() {
  local key="$1"
  local project_id="$2"
  local env_name="$3"
  local folder_path="$4"

  (
    local tmp_file

    tmp_file="$(mktemp)"
    cleanup_infisical_secret_file() {
      rm -f "${tmp_file}"
    }
    trap cleanup_infisical_secret_file EXIT HUP INT TERM

    chmod 0600 "${tmp_file}"
    {
      printf '%s=' "${key}"
      cat
      printf '\n'
    } >"${tmp_file}"

    infisical_cli secrets set \
      --file "${tmp_file}" \
      --projectId "${project_id}" \
      --env "${env_name}" \
      --path "${folder_path}" >/dev/null
  )
}

infisical_get_secret_plain() {
  local key="$1"
  local project_id="$2"
  local env_name="$3"
  local folder_path="$4"

  infisical_cli secrets get "${key}" \
    --projectId "${project_id}" \
    --env "${env_name}" \
    --path "${folder_path}" \
    --plain
}

infisical_get_secret_var() {
  local target_var="$1"
  local key="$2"
  local project_id="$3"
  local env_name="$4"
  local folder_path="$5"
  local fetched_secret_value
  local xtrace_was_on=false
  local secret_status

  if [[ ! "${target_var}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    infisical_log "invalid target variable name: ${target_var}"
    return 2
  fi

  if infisical_xtrace_off; then
    xtrace_was_on=true
  fi
  if fetched_secret_value="$(infisical_get_secret_plain "${key}" "${project_id}" "${env_name}" "${folder_path}")"; then
    secret_status=0
  else
    secret_status=$?
  fi
  if [ "${secret_status}" -ne 0 ]; then
    infisical_restore_xtrace "${xtrace_was_on}"
    return "${secret_status}"
  fi

  printf -v "${target_var}" '%s' "${fetched_secret_value}"
  infisical_restore_xtrace "${xtrace_was_on}"
}

infisical_list_secret_names() {
  local project_id="$1"
  local env_name="$2"
  local folder_path="$3"
  local xtrace_was_on=false
  local list_status

  if infisical_xtrace_off; then
    xtrace_was_on=true
  fi

  # The CLI has no names-only listing mode, so what comes back here carries
  # secret VALUES. It is therefore piped straight into the filter below and
  # never bound to a shell variable, written to a file, or placed in argv --
  # only names leave this function. Imports and expansion are off on purpose:
  # the caller asks which keys actually exist at this folder, and an imported
  # or referenced key would answer a different question.
  if infisical_cli secrets \
      --projectId "${project_id}" \
      --env "${env_name}" \
      --path "${folder_path}" \
      --include-imports=false \
      --expand=false \
      --output json \
    | python3 -c '
import json
import sys

try:
    payload = json.load(sys.stdin)
except ValueError:
    # Deliberately does not echo the payload: it holds secret values.
    sys.stderr.write("infisical secret listing was not valid JSON\n")
    raise SystemExit(1)

if isinstance(payload, dict):
    entries = payload.get("secrets", payload.get("data", []))
else:
    entries = payload
if entries is None:
    entries = []

names = set()
for entry in entries:
    if not isinstance(entry, dict):
        continue
    name = entry.get("secretKey", entry.get("key", ""))
    if name:
        names.add(name)

for name in sorted(names):
    print(name)
'; then
    list_status=0
  else
    list_status=$?
  fi

  infisical_restore_xtrace "${xtrace_was_on}"
  return "${list_status}"
}
