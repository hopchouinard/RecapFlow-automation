# Chapter 3 — Infrastructure & Deployment

**Category:** Infrastructure & Deployment
**Reading time:** 5 minutes

---

## VM Setup

The system runs on a Proxmox-hosted Linux VM accessible at `n8n-automation.patchoutech.lab` on the local network. The VM is not exposed to the internet.

### Docker Compose

Two containers orchestrated via Docker Compose v2:

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=db
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=n8n
      - DB_POSTGRESDB_USER=n8n
      - DB_POSTGRESDB_PASSWORD=n8n
      - N8N_SECURE_COOKIE=false
      - NODES_EXCLUDE=[]
      - NODE_FUNCTION_ALLOW_BUILTIN=fs,path
    ports:
      - "5678:5678"
    volumes:
      - ./data:/home/node/.n8n
      - ./watch:/home/node/watch
      - ./output:/home/node/output
    depends_on:
      - db

  db:
    image: postgres:17
    container_name: n8n_db
    environment:
      - POSTGRES_DB=n8n
      - POSTGRES_USER=n8n
      - POSTGRES_PASSWORD=n8n
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

### Critical Environment Variables

| Variable | Value | Why |
|----------|-------|-----|
| `N8N_SECURE_COOKIE=false` | Required | n8n runs over HTTP (no TLS on local network) |
| `NODES_EXCLUDE=[]` | Required | Re-enables Local File Trigger, disabled by default since n8n 2.0 |
| `NODE_FUNCTION_ALLOW_BUILTIN=fs,path` | Required | Allows Code nodes to read/write files via `require('fs')` |

### Volume Mounts

| Host Path | Container Path | Purpose |
|-----------|---------------|---------|
| `./data` | `/home/node/.n8n` | n8n runtime state, credentials, encryption key |
| `./watch` | `/home/node/watch` | Incoming files (chat logs, transcripts) |
| `./output` | `/home/node/output` | Generated output files organized by date |

## Version Pinning

### PostgreSQL 17

PostgreSQL is pinned to v17, not `latest`. When PostgreSQL 18 was released, it changed the data directory layout, breaking existing volumes. Always pin to the major version matching your existing data.

### n8n Latest

n8n uses `latest` tag. n8n handles database migrations automatically on startup, so upgrades are generally safe. The command to upgrade:

```bash
docker compose pull && docker compose up -d
```

## Network Architecture

```
Mac Mini ──── SSH/rsync ────► VM (n8n-automation)
                                │
                                ├── :5678 (n8n UI, local only)
                                │
                                ├──► api.fathom.ai (HTTPS)
                                └──► openrouter.ai (HTTPS)
```

The VM makes outbound HTTPS calls to two external APIs. No inbound connections from the internet are required.

## SSH Configuration

The Workstation connects to the VM via SSH key authentication. The key has a passphrase stored in the OS Keychain:

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

The SSH host is configured in `~/.ssh/config` on the Workstation as `n8n-automation`.
