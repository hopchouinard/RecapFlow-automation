# OpenRouter Usage & Cost Tracking — Implementation Plan

> **Status:** DRAFT — do not begin implementation until Plan C (n8n Workflow 6 backfill) is complete.
> **Tier:** Personal preprocessing tier only. Not bundled into the shareable Community Brain artifact.

**Goal:** Capture per-call OpenRouter usage (tokens, cost, model, provider, finish reason, latency) for every LLM invocation in n8n workflows, store it in Postgres + a JSONL audit log on the n8n-automation VM, and expose it through Grafana on the monitoring-stack VM for spend visibility and trend analysis.

**Architecture:**

```
n8n LLM call (ChainLLM, OpenRouter)
        │
        ▼
   Code node
   ├─ extract usage from response
   ├─ append line to JSONL (~/n8n/logs/openrouter-usage-YYYY-MM-DD.jsonl)
   └─ pass clean object to next node
        │
        ▼
   Postgres node
   └─ INSERT INTO openrouter_usage
        │
        ▼
   (continue normal workflow)

monitoring-stack VM (10.1.30.X)
   Grafana
   └─ Postgres datasource → n8n-automation:5432 (read-only grafana_ro user)
```

**Tech stack:**
- n8n 2.15 — Code nodes (`fs`-enabled) + native Postgres node
- Postgres 17 (existing `n8n_db` container) — new `openrouter_usage` table + `grafana_ro` role
- Grafana (existing on monitoring-stack VM) — Postgres datasource plugin
- JSONL files — durable append-only audit log on the n8n VM

**Out of scope:**
- Prometheus integration (wrong tool for event data — see memory `project_openrouter_cost_tracking`)
- Loki log aggregation (deferred; revisit only if cross-service log search becomes a need)
- Alerting on cost thresholds (Phase 6 stretch goal, not part of initial delivery)
- Bundling cost tracking into the distributable Community Brain artifact (explicitly excluded — personal tier only)

---

## File map

| Action | Path | Purpose |
|---|---|---|
| Create | `scripts/sql/usage_tracking_schema.sql` | DDL for `openrouter_usage` table, indexes, `grafana_ro` user |
| Create | `scripts/sql/usage_tracking_grants.sql` | Idempotent GRANT statements (separated for re-runnability) |
| Create | `scripts/backfill-openrouter-usage.py` | One-shot import of historical OpenRouter activity into Postgres + JSONL |
| Create | `scripts/postgres-test-grafana-access.sh` | Smoke test: connect from monitoring-stack as `grafana_ro`, run sample query |
| Modify | `docker-compose.yml` | Add `./logs/` bind mount on `n8n` container; bind `n8n_db` Postgres port to VM's LAN IP |
| Modify | `.gitignore` | Exclude `logs/openrouter-usage-*.jsonl` (runtime data) |
| Modify | `workflows/merged-call-summarizer.json` | Add Code + Postgres node pair after each of the 4 LLM calls |
| Create | `docs/grafana/openrouter-usage-dashboard.json` | Exported Grafana dashboard for version control |
| Modify | `CLAUDE.md` | Document the new logging layer + dashboard URL |
| Modify | `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md` | Mark cost-tracking phase as DEPLOYED once complete |

Runtime-only actions (not code changes):
- `pg_hba.conf` edit on `n8n_db` container to whitelist `monitoring-stack`'s LAN IP
- Grafana UI: add Postgres datasource, import dashboard JSON
- One-time historical backfill via `scripts/backfill-openrouter-usage.py`

---

## Task dependency overview

```
Phase 0 (discovery)
        │
        ▼
Phase 1 (Postgres schema + grafana_ro user)
        │
        ▼
Phase 2 (JSONL infrastructure on n8n VM)
        │
        ├─────────────────────────┐
        ▼                         ▼
Phase 3 (n8n workflow nodes)   Phase 4 (network access for Grafana)
        │                         │
        └────────────┬────────────┘
                     ▼
              Phase 5 (Grafana dashboard)
                     │
                     ▼
              Phase 6 (backfill + validation)
```

Phases 3 and 4 are independent and can land in either order; everything else is sequential.

---

## Phase 0: Discovery & verification

**Purpose:** Confirm load-bearing assumptions before writing any code. Prevents wasted work if ChainLLM strips the `usage` field or OpenRouter changed its API shape.

### Steps

- [ ] **0.1 — Inspect a real ChainLLM execution output.**
  Open n8n UI → Workflow 5 (Merged Call Summarizer) → most recent successful execution → click into the LLM: Extract Signal node → "JSON" view of output. Look for:
  - Top-level `tokenUsage` field (LangChain's wrapper name)
  - Nested `response.usage` or `usage` block
  - Total tokens, prompt tokens, completion tokens
  - Cost field (may be absent unless `usage_include_cost` was set)
  - Model name and provider

  **If `tokenUsage` is present:** Code node can extract directly, no fallback needed.
  **If `tokenUsage` is absent / stripped:** fall back to direct HTTP-Request-to-OpenRouter pattern with `usage: {include: true}` in the request body. (Workflow 5 is currently using ChainLLM, so this would be a structural change.)

- [ ] **0.2 — Verify OpenRouter activity API is usable for backfill.**
  ```bash
  curl -s -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    "https://openrouter.ai/api/v1/activity" | jq '. | keys, .[0]'
  ```
  Confirm: response has per-call records with `id`, `created_at`, `model`, `tokens_prompt`, `tokens_completion`, `total_cost`, `provider_name`. If structure differs, adjust the backfill script accordingly.

- [ ] **0.3 — Decide cost source-of-truth.**
  Two choices:
  - **(Preferred)** Set `usage: {include: true}` in OpenRouter requests so each response carries `usage.cost` directly. Most accurate, no per-model price table to maintain.
  - **(Fallback)** Maintain a static price table per model and compute `cost = prompt_tokens * input_price + completion_tokens * output_price`. Cheap to start but rots when OpenRouter changes prices.

  Lock in one approach for the rest of the plan. Default to (Preferred); switch only if it doesn't work with ChainLLM.

**Phase 0 exit criteria:** all three discovery items resolved; assumptions documented in this plan as a comment block before Phase 1 begins.

---

## Phase 1: Postgres schema + grafana_ro user

**Purpose:** Stand up the storage layer. Schema is intentionally narrow — flat table, no joins needed, optimized for time-series + filter-by-dimension queries.

### 1.1 Schema (`scripts/sql/usage_tracking_schema.sql`)

```sql
CREATE TABLE IF NOT EXISTS openrouter_usage (
  id              BIGSERIAL PRIMARY KEY,
  ts              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  workflow_id     TEXT,
  workflow_name   TEXT,
  execution_id    BIGINT,
  node_name       TEXT,
  model           TEXT NOT NULL,
  provider        TEXT,
  prompt_tokens   INT,
  completion_tokens INT,
  total_tokens    INT,
  cost_usd        NUMERIC(10, 6),
  finish_reason   TEXT,
  latency_ms      INT,
  generation_id   TEXT,        -- OpenRouter's per-call id, for cross-reference with their dashboard
  raw_response    JSONB        -- full response payload for forensic queries; nullable if size becomes a concern
);

CREATE INDEX IF NOT EXISTS idx_openrouter_usage_ts ON openrouter_usage (ts DESC);
CREATE INDEX IF NOT EXISTS idx_openrouter_usage_model ON openrouter_usage (model);
CREATE INDEX IF NOT EXISTS idx_openrouter_usage_workflow ON openrouter_usage (workflow_id);
CREATE INDEX IF NOT EXISTS idx_openrouter_usage_execution ON openrouter_usage (execution_id);
```

### 1.2 Read-only role (`scripts/sql/usage_tracking_grants.sql`)

```sql
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'grafana_ro') THEN
    CREATE ROLE grafana_ro LOGIN PASSWORD 'CHANGE_ME_USE_SECRET';
  END IF;
END$$;

GRANT CONNECT ON DATABASE n8n TO grafana_ro;
GRANT USAGE ON SCHEMA public TO grafana_ro;
GRANT SELECT ON openrouter_usage TO grafana_ro;
```

Password should be set from a secret, not committed. Update `.env` with `GRAFANA_RO_PASSWORD=...` and have the apply script substitute it.

### Steps

- [ ] **1.1 — Write `scripts/sql/usage_tracking_schema.sql`** with the DDL above.
- [ ] **1.2 — Write `scripts/sql/usage_tracking_grants.sql`** with the role + grants.
- [ ] **1.3 — Generate and store `GRAFANA_RO_PASSWORD`** in the VM's `.env`. Use `openssl rand -base64 32` or similar. Confirm `.env` is gitignored (it is).
- [ ] **1.4 — Apply schema** by running both SQL files via `docker exec n8n_db psql -U n8n -d n8n -f -`.
- [ ] **1.5 — Verify** with `\dt openrouter_usage` and `\du grafana_ro` in psql.

**Phase 1 exit criteria:** table exists, role exists, role can `SELECT` from `openrouter_usage` and **cannot** SELECT from any n8n internal table (verify with explicit deny test).

---

## Phase 2: JSONL infrastructure on n8n VM

**Purpose:** Belt-and-suspenders durable log. JSONL is append-only, human-greppable, and survives Postgres outages. Daily rotation keeps individual files manageable.

### 2.1 Volume mount (`docker-compose.yml`)

Add to the `n8n` service:

```yaml
    volumes:
      - ./data:/home/node/.n8n
      - ./watch:/home/node/watch
      - ./output:/home/node/output
      - ./logs:/home/node/logs    # NEW
```

### 2.2 `.gitignore` update

```
# Runtime usage logs (rebuild from Postgres if lost)
logs/openrouter-usage-*.jsonl
```

Keep `logs/.gitkeep` so the directory exists at checkout.

### Steps

- [ ] **2.1 — Update `docker-compose.yml`** to add the `./logs:/home/node/logs` mount.
- [ ] **2.2 — Update `.gitignore`** with the JSONL exclusion.
- [ ] **2.3 — Create `logs/.gitkeep`** so the directory survives clean checkouts.
- [ ] **2.4 — `mkdir -p ~/n8n/logs && chmod 755 ~/n8n/logs`** on the VM, owned by the host user that maps to n8n's container user.
- [ ] **2.5 — `docker compose up -d n8n`** to pick up the new mount. Verify with `docker exec n8n ls -la /home/node/logs`.

**Phase 2 exit criteria:** n8n container can read and write to `/home/node/logs/`; corresponding host path is `~/n8n/logs/`.

---

## Phase 3: n8n workflow integration

**Purpose:** Add the Code + Postgres node pair after each of the 4 LLM calls in Workflow 5 (Merged Call Summarizer). Workflow 6 (Plan C backfill) does not get this treatment because Plan C is one-shot — historical Plan C cost is recovered via the Phase 6 backfill script, not inline logging.

Per LLM call, the wiring becomes:

```
LLM: Extract Signal (ChainLLM)
        │
        ▼
[NEW] Code: Log LLM Usage  ─ writes JSONL line, returns shaped object
        │
        ▼
[NEW] Postgres: Insert Usage  ─ INSERT INTO openrouter_usage
        │
        ▼
Save extracted-signal.md  (existing next node)
```

### 3.1 Code node template

```javascript
// Extract usage from previous LLM node's output
const llmOutput = $input.item.json;
const usage = llmOutput.tokenUsage || llmOutput.response?.usage || {};
const fs = require('fs');
const path = require('path');

const now = new Date();
const date_str = now.toISOString().slice(0, 10);
const log_path = `/home/node/logs/openrouter-usage-${date_str}.jsonl`;

const record = {
  ts: now.toISOString(),
  workflow_id: $workflow.id,
  workflow_name: $workflow.name,
  execution_id: $execution.id,
  node_name: $('Resolve LLM node name').first().json.name || 'unknown',  // captured upstream or hardcoded
  model: llmOutput.model || llmOutput.response?.model || 'unknown',
  provider: llmOutput.response?.provider || null,
  prompt_tokens: usage.prompt_tokens || usage.promptTokens || null,
  completion_tokens: usage.completion_tokens || usage.completionTokens || null,
  total_tokens: usage.total_tokens || usage.totalTokens || null,
  cost_usd: usage.cost || null,
  finish_reason: llmOutput.response?.finish_reason || llmOutput.finish_reason || null,
  latency_ms: llmOutput.latency_ms || null,
  generation_id: llmOutput.id || llmOutput.response?.id || null,
  raw_response: JSON.stringify(llmOutput).slice(0, 50000),  // cap at 50KB for safety
};

// Append to JSONL (best-effort — Postgres insert is the canonical write)
try {
  fs.appendFileSync(log_path, JSON.stringify(record) + '\n');
} catch (err) {
  // Don't fail the workflow on log write — Postgres is the source of truth
  console.error(`JSONL append failed: ${err.message}`);
}

return { json: record };
```

### 3.2 Postgres node config

- **Operation:** Insert
- **Schema:** `public`
- **Table:** `openrouter_usage`
- **Columns:** map all fields from the previous Code node's output
- **Continue on Fail:** YES — don't break the workflow if logging fails (we have JSONL as backup)

### Steps

- [ ] **3.1 — Build the Code node template** in a scratch workflow first, test against one LLM output until JSONL line and Postgres row both appear.
- [ ] **3.2 — Verify field mappings.** Run a real LLM call, inspect the produced row in `openrouter_usage`, cross-check against OpenRouter's UI for the same call. Reconcile any discrepancies.
- [ ] **3.3 — Wire into Workflow 5.** Insert Code+Postgres pair after each of: LLM: Extract Signal, LLM: Community Post, LLM: Compress Post, LLM: Weekly Invite. Total: 8 new nodes.
- [ ] **3.4 — Wire prep-prompt LLM call too.** That one was added in Plan B — Code+Postgres pair goes after `LLM: Prep-Prompt`. Total now: 10 new nodes in Workflow 5.
- [ ] **3.5 — Set Continue on Fail = YES** on every Postgres insert node.
- [ ] **3.6 — Trigger Workflow 5** with a real session. Verify all 5 LLM calls produced JSONL lines and Postgres rows.

**Phase 3 exit criteria:** one full Workflow 5 run produces 5 JSONL lines and 5 `openrouter_usage` rows. Costs match OpenRouter's web UI within rounding.

---

## Phase 4: Network access for Grafana

**Purpose:** Allow `monitoring-stack` VM to reach `n8n-automation:5432` over the LAN, restricted to the `grafana_ro` role.

### 4.1 Postgres binding (`docker-compose.yml`)

The `n8n_db` service currently binds Postgres to the Docker network only. We need to publish 5432 to the n8n VM's LAN interface so monitoring-stack can reach it. Bind to the LAN IP, NOT `0.0.0.0`:

```yaml
  n8n_db:
    image: postgres:17
    ports:
      - "10.1.30.X:5432:5432"   # NEW — replace X with the n8n VM's actual LAN IP
```

Hardcoding the IP is intentional — `0.0.0.0` would expose Postgres beyond the VLAN if the VM ever picks up a different network.

### 4.2 `pg_hba.conf` entry

Inside the `n8n_db` container, edit `/var/lib/postgresql/data/pg_hba.conf`:

```
# Allow grafana_ro from monitoring-stack VM only
host    n8n    grafana_ro    10.1.30.Y/32    scram-sha-256
```

Replace `Y` with monitoring-stack's actual LAN IP. `/32` ensures host-specific match.

Reload Postgres config:
```bash
docker exec n8n_db psql -U n8n -c "SELECT pg_reload_conf();"
```

### Steps

- [ ] **4.1 — Identify n8n-automation's LAN IP** with `ip addr show` on the VM. Note the address on the `10.1.30.0/24` interface.
- [ ] **4.2 — Identify monitoring-stack's LAN IP** the same way (or via Proxmox UI).
- [ ] **4.3 — Update `docker-compose.yml`** with the LAN-IP-bound port mapping.
- [ ] **4.4 — Restart `n8n_db`** with `docker compose up -d n8n_db`. Verify Postgres is listening on the LAN IP only with `ss -tlnp | grep 5432`.
- [ ] **4.5 — Edit `pg_hba.conf`** with the monitoring-stack whitelist entry.
- [ ] **4.6 — Reload Postgres config** via `pg_reload_conf()`.
- [ ] **4.7 — Smoke test from monitoring-stack:**
  ```bash
  ssh monitoring-stack "psql -h 10.1.30.X -U grafana_ro -d n8n -c 'SELECT COUNT(*) FROM openrouter_usage;'"
  ```
  Expected: connection succeeds, returns row count. If it fails, check pg_hba ordering (allow rule must precede any `reject` rules).
- [ ] **4.8 — Verify deny path:** same query as a non-whitelisted role or from a non-whitelisted IP must fail. Don't skip this — you want positive confirmation that the firewall isn't accidentally permissive.

**Phase 4 exit criteria:** monitoring-stack can SELECT from `openrouter_usage` as `grafana_ro`; cannot SELECT from any other table; non-monitoring-stack hosts cannot connect at all.

---

## Phase 5: Grafana dashboard

**Purpose:** Build the dashboard panels. Export the dashboard JSON to the repo for reproducibility — if Grafana is ever rebuilt, the dashboard restores from JSON.

### 5.1 Datasource

In Grafana UI → Configuration → Data sources → Add data source → PostgreSQL:
- **Host:** `10.1.30.X:5432`
- **Database:** `n8n`
- **User:** `grafana_ro`
- **Password:** from `.env`
- **TLS/SSL Mode:** `disable` (LAN-only, same VLAN — TLS is overhead with no threat model benefit here)
- **Version:** 17

### 5.2 Dashboard panels (initial set)

| Panel | Type | SQL |
|---|---|---|
| Daily cost by model | Stacked bar | `SELECT date_trunc('day', ts) AS time, model, SUM(cost_usd) FROM openrouter_usage GROUP BY 1, 2 ORDER BY 1` |
| Total spend (last 30 days) | Stat | `SELECT SUM(cost_usd) FROM openrouter_usage WHERE ts >= NOW() - INTERVAL '30 days'` |
| Token usage time series | Time series | `SELECT date_trunc('hour', ts) AS time, SUM(prompt_tokens) AS prompt, SUM(completion_tokens) AS completion FROM openrouter_usage GROUP BY 1` |
| Top 20 expensive calls | Table | `SELECT ts, workflow_name, node_name, model, cost_usd, total_tokens FROM openrouter_usage ORDER BY cost_usd DESC LIMIT 20` |
| Cost per session | Bar | (joins workflow + execution; query depends on how session id is captured — likely needs a derived column or annotation node in n8n) |
| Finish reason distribution | Pie | `SELECT finish_reason, COUNT(*) FROM openrouter_usage GROUP BY 1` |
| Avg latency by model | Bar | `SELECT model, AVG(latency_ms) FROM openrouter_usage WHERE latency_ms IS NOT NULL GROUP BY 1` |

### Steps

- [ ] **5.1 — Add Postgres datasource** in Grafana UI; click "Save & test" — must show "Database Connection OK".
- [ ] **5.2 — Build each panel** in a new dashboard, one at a time. Validate SQL by running it in psql first.
- [ ] **5.3 — Set time range and refresh interval** at the dashboard level (last 30 days, refresh every 5 min is fine).
- [ ] **5.4 — Export dashboard JSON** (Settings → JSON Model → copy) and commit to `docs/grafana/openrouter-usage-dashboard.json`.
- [ ] **5.5 — Document the dashboard URL** in `CLAUDE.md` so future sessions know where to look.

**Phase 5 exit criteria:** dashboard renders all 7 panels with real data; JSON exported and committed.

---

## Phase 6: Backfill + validation

**Purpose:** Fill in historical OpenRouter usage from before the inline logging existed (everything Plan C consumed, plus the live Workflow 5 runs). Validate end-to-end accuracy against OpenRouter's own UI.

### 6.1 Backfill script (`scripts/backfill-openrouter-usage.py`)

Standalone Python script that:
1. Reads `OPENROUTER_API_KEY` from environment
2. Pages through `https://openrouter.ai/api/v1/activity?after=<earliest_unwritten_ts>` (or whatever the actual API supports)
3. For each record, INSERT INTO `openrouter_usage` with `ON CONFLICT (generation_id) DO NOTHING` to be idempotent
4. Also writes to `~/n8n/logs/openrouter-usage-backfill.jsonl` for audit trail

Note: the `openrouter_usage` schema needs a UNIQUE constraint on `generation_id` for the upsert to work. Add to Phase 1's DDL: `CREATE UNIQUE INDEX IF NOT EXISTS idx_openrouter_usage_generation_id ON openrouter_usage (generation_id) WHERE generation_id IS NOT NULL;` (partial index — generation_id is nullable).

### Steps

- [ ] **6.1 — Add the partial unique index** to the schema (retroactive Phase 1 update).
- [ ] **6.2 — Write `scripts/backfill-openrouter-usage.py`.** Test against last 24 hours of data first.
- [ ] **6.3 — Run full backfill** for the last 30 days (OpenRouter's typical retention window — verify the actual limit).
- [ ] **6.4 — Cross-check totals:** sum `cost_usd` from `openrouter_usage` for a known time window, compare to the same window in OpenRouter's web UI. Should match within rounding.
- [ ] **6.5 — Spot-check a Plan C session.** Pick `2026-04-30` — that's a real ingestion day. Confirm the dashboard shows the expected ~30-90 LLM calls (3 per session × N sessions) with realistic costs.
- [ ] **6.6 — Update `CLAUDE.md`** to document: backfill script, dashboard location, schema location, refresh expectations.
- [ ] **6.7 — Update `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`** to mark cost-tracking as DEPLOYED.

**Phase 6 exit criteria:** dashboard shows correct historical and live data; backfill is idempotent (re-running doesn't double-count); documentation reflects the live state.

---

## Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| ChainLLM strips `usage` from response | Medium | High | Phase 0.1 verifies first; fallback is direct HTTP-to-OpenRouter pattern |
| Postgres insert fails (lock contention, network blip) | Low | Low | Continue on Fail = YES on Postgres node + JSONL is durable backup |
| `pg_hba.conf` misconfiguration leaves Postgres exposed | Low | High | Phase 4.8 explicitly tests deny path before declaring done |
| Grafana password leaks via committed config | Medium | Medium | Password lives only in `.env` (gitignored) and Grafana UI; never inline in dashboard JSON |
| OpenRouter API rate-limits during backfill | Low | Low | Backfill script paginates with sleep; idempotent on re-run |
| Cost field absent from response (no `usage_include_cost`) | Medium | Medium | Phase 0.3 locks in source; fallback price table maintained in script if needed |
| Schema migration needed later | Medium | Low | Use `ALTER TABLE` patterns + version comments at top of `usage_tracking_schema.sql` |

---

## Open questions to resolve during Phase 0

1. Does the LangChain ChainLLM node in n8n 2.15 expose `tokenUsage` in its main output, or only in `pairedItem`/sub-node output? Affects the Code node's data-fetching pattern.
2. Does OpenRouter's response include `cost` natively without `usage_include_cost`, or is that flag required? Affects Phase 0.3 decision.
3. What's OpenRouter's activity API retention window — 30 days, 90 days, longer? Affects backfill scope.
4. Does the n8n `n8n_db` Postgres need a password rotation now, given we're about to expose it on LAN? (Probably yes.)
5. Should we add session_id as a dedicated column for clean cost-per-session queries, or derive it from `execution_id` joins? Affects Phase 1 schema.

---

## Notes for the implementer

- This plan is self-contained — no separate spec doc. The "why" is in the architecture summary up top and in memory `project_openrouter_cost_tracking`.
- Do not start before Plan C completes. Modifying Workflow 5 while Plan C runs Workflow 6 is fine in principle (different workflows) but unnecessary risk during a 12-hour batch.
- Phase 0 is non-optional. Skipping discovery to "just write the code" is how we end up with a Code node that returns `null` for every cost field because LangChain swallowed the response shape.
- Keep raw_response capped (50KB cap in the Code node template) — full LLM responses can be huge and bloat the table.
- Continue on Fail must be YES on the Postgres insert. The workflow's primary job is producing artifacts; logging is secondary.
