# Brainstorming Brief: Community-Tier Distribution

**For:** the next brainstorming session, to be opened in a fresh chat.
**Topic:** how to package and distribute the RecapFlow stack for users beyond the original operator (you).
**Date created:** 2026-05-09 (context handoff from the operator-tier packaging session).

## What this brief is for

This is NOT a spec. It's a context dump for a fresh session that will brainstorm two community-distribution tiers. Read it, then start brainstorming with the user — don't try to write a spec from this alone.

The user (`pchouinard` / `chouinpa@gmail.com`) wants a sassy, opinionated collaborator. Honesty over compliance. Don't sugarcoat bad ideas. Ask clarifying questions before diving into complex answers. Refer to `~/.claude/CLAUDE.md` for the full personality contract.

## What's been built (the operator tier — DONE)

A two-node disaster-recovery-grade self-hosted deployment of the RecapFlow stack, fully operational on the user's hardware:

- **VM** (`n8n-automation.patchoutech.lab`, Ubuntu, Proxmox) running Docker Compose with:
  - `n8n` (workflow automation, port 5678)
  - `db` (PostgreSQL 17)
  - `retrieval-server` (FastAPI, port 8999, the community-brain Python package)
  - `open-webui` (port 3000, with the community-brain filter + custom gpt-oss model)
- **Inference workstation** (Mac mini, 24 GB unified memory) running:
  - Ollama with `nomic-embed-text:v1.5` (embeddings) + `gpt-oss:20b` (generation)
  - Zoom chat sync orchestration (Automator + launchd + rsync)
  - Daily pull of VM backup snapshots → boot volume → Arq → encrypted cloud
- **Daily backup pipeline:** VM cron at 06:00 UTC → workstation launchd at 02:30 local → Arq.
- **`bootstrap.sh`** for fresh-VM DR install (8 phases, ~20–45 min).

Spec: `docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md`
Plan: `docs/superpowers/plans/2026-05-07-operator-tier-packaging-and-dr-plan.md`
DR runbooks: `docs/runbooks/{vm,workstation}-disaster-recovery.md`, `docs/runbooks/dr-rehearsal-operator-checklist.md`

## What needs brainstorming (the work for the new session)

The user wants to package this stack for distribution. They've decided on two tiers — these were called out as explicit non-goals during the operator-tier work and deferred to follow-up specs. Brainstorm them now.

### Tier A: Community-Full

Distributable to other people who want to run the **full pipeline themselves**:
- Mac sync (Zoom chat capture)
- n8n workflows
- Retrieval server with their own LanceDB
- Open WebUI with the filter + custom model
- They bring their own API keys (OpenRouter, Fathom, etc.)

### Tier B: Community-Retrieval-Only

Distributable to people who want **only** the LanceDB + retrieval-server piece. The user's preprocessing/ingestion pipeline stays personal. They get pre-populated retrieval over the user's curated coaching-call corpus, served read-only via the FastAPI server.

This is the canonical historical position per the user's memory: "Hard split: preprocessing/cost-tracking stays personal, only LanceDB + retrieval-server is distributed."

## Constraints carried forward from the operator tier

These are things the operator-tier work locked in that the community-tier specs should respect (or explicitly revisit):

1. **Two-node architecture is real.** Inference (Ollama with `nomic-embed-text` + `gpt-oss:20b`) needs a workstation with sufficient unified memory or GPU+VRAM. The VM doesn't run models. Community users will need to make this same hardware decision — many won't have it. This is the single biggest distribution constraint.

2. **The `community-brain` Python package is already designed to be standalone.** It has its own `CLAUDE.md`, `Dockerfile`, `pyproject.toml`, deployment runbook (`community-brain/docs/DEPLOYMENT.md`), trust contract (`docs/inference-guidelines.md`), and a hard-split philosophy: registries, schema, ingestion, retrieval all encapsulated. The retrieval-only tier already exists in spirit; it just needs packaging discipline.

3. **The Open WebUI custom model + filter are reproducible from the repo.** `community-brain/src/community_brain/openwebui/community_brain_filter.py` + `docs/inference-guidelines.md` (system prompt for the custom model). NOT in webui.db, since webui.db is operator-personal state.

4. **Open WebUI image is pinned by SHA, not tag.** Bumping breaks alembic. Documented in `dr-rehearsal-operator-checklist.md` and the spec addendum.

5. **Operator (you) personal-tier artifacts that should NOT distribute:**
   - Real `.env` files (n8n encryption key, Postgres password, OpenRouter/Fathom keys)
   - Open WebUI's webui.db (chats, prompts, knowledge, files — all your personal coaching)
   - n8n's `data/config` encryption key
   - `output/`, `historical/` — your actual session corpus
   - `community-brain/lancedb/` — your embedded corpus (UNLESS this is the retrieval-only tier, in which case yes-distribute but read-only)
   - `~/.zoom-chat-synced` and the workstation sync state

6. **`OLLAMA_BASE_URL=http://10.1.50.219:11434` is operator-personal.** Community deployers will have a different LAN topology.

7. **n8n workflows in `workflows/` are largely shareable** — they're the orchestration logic — but they reference credentials by name (OpenRouter, Fathom). Community users would re-bind them.

8. **`prompts/` are shareable.** They're the LLM extraction prompts for the chunking pipeline. Already in git.

## Open design questions (start here in the new session)

These are the forks I'd hit early in the brainstorming. Ask the user one at a time, multiple-choice where possible:

### About the audience

- **Who specifically is "the community"?** Is this for users in a specific Skool community (the `community-brain` name suggests a community context)? Public open-source? Friends and family? Different audiences = wildly different packaging effort.
- **What's their technical sophistication?** Can they handle `docker compose up`? Read a README? Use SSH? Or do they need a one-click installer?
- **What hardware can we assume?** Apple Silicon Mac with 16+ GB? Linux box with NVIDIA? Anything goes? This determines whether community-full is even feasible for them.

### About the business / motivation

- **What's the incentive structure?** Free open-source? Donations? Paid product? "Pay the LLM API bill yourself"?
- **Is the user (operator) hosting anything for community users, or is it 100% self-host?** Hosting introduces operator-side cost, multi-tenancy concerns, privacy lawyering.
- **What's the support model?** Best-effort GitHub issues? Skool channel? Operator-as-support?

### About Tier A (Community-Full) specifically

- **LLM keys:** users bring their own OpenRouter/Fathom keys, or operator proxies through their own (cost-bearer = operator)?
- **Local model serving:** mandatory Ollama? Or can users point at hosted (OpenRouter, OpenAI) and skip the workstation entirely? The latter sidesteps the hardware barrier but changes economics and privacy.
- **Mac-side sync (Automator + launchd):** is the Zoom→VM sync a hard requirement or optional? Many users won't have a separate VM; they'll run everything on one box.
- **Multi-user vs single-user:** does each instance serve one person or a household / small team?

### About Tier B (Community-Retrieval-Only) specifically

- **Pre-populated corpus distribution:** ship a snapshot of the LanceDB (operator's coaching-call corpus, 5+ GB) so users get a working RAG out of the box?
- **Read-only?** No `/ingest` endpoint exposed; users can `/query` but not add their own data?
- **License/IP:** what's the licensing posture for the operator's corpus? Are coaching-call transcripts (with names of attendees) shareable at all?
- **Update cadence:** how do users get new content? They re-pull a tarball monthly? They subscribe to deltas?

### About distribution mechanics

- **Distribution channel:** public GitHub repo? Private repo with invites? Docker images on a registry? Helm chart? Tarball download? `npm`-style package?
- **Versioning model:** tagged releases? Continuous? `:latest`?
- **Onboarding:** README walk-through? `make install`? Web installer? Video?
- **Updates:** how does a user upgrade after release N+1? Especially if a schema migration is needed (we just lived through this pain).

### About the personal/shareable split

- **Walking back the memory note:** the user originally said "preprocessing stays personal, only retrieval-server distributes." Tier A walks this back — the FULL preprocessing pipeline distributes. Confirm this is intentional. If so, what changes about cost tracking? About the operator's curated prompts? About the workflows that have personal API key bindings?

## Files worth scanning before brainstorming

- `community-brain/CLAUDE.md` — architectural constraints, what's already standalone-ish
- `community-brain/docs/DEPLOYMENT.md` — current deployment runbook, mostly operator-focused but informs community packaging
- `docs/inference-guidelines.md` — the trust contract; informs what flows through to community users
- `docs/superpowers/specs/2026-05-07-operator-tier-packaging-and-dr-design.md` — the operator-tier spec, contains the explicit deferral of community tiers
- `docker-compose.yml` — what currently ships in the stack
- `community-brain/open-webui/docker-compose.yml` — old workstation-side OW compose, deprecated but illustrative

## Pragmatic notes from the operator-tier session (lessons that may matter)

- **macOS TCC blocks launchd UserAgents from secondary APFS volumes.** If community users run on a Mac with external drives, document this gotcha or stage on boot volume by default.
- **Open WebUI alembic migrations are destructive across version jumps.** Pin by SHA in any community distribution. Document the upgrade-rehearsal procedure.
- **Compose volume names get project-prefixed by default** (`<dirname>_<volume>`). This silently bit us. For community users with unpredictable repo paths, declare external or use absolute volume names.
- **Image SHAs are immutable but ghcr.io eventually GCs old digests.** A SHA pin good today may not pull tomorrow. Plan for this — re-tag periodically?
- **The `extra_hosts: host.docker.internal:host-gateway` directive** is needed wherever a service must reach the VM host's published ports. Easy to forget; bit us once.

## Recommended first move

Start the new session with: scope check. The two tiers might be too much for one spec. The full tier requires deciding hardware, LLM-routing, sync, multi-user. The retrieval-only tier is much smaller (it's basically "ship the existing FastAPI service with a baked LanceDB, lock down `/ingest`, document install").

Recommend brainstorming **Tier B (retrieval-only) first** — it's smaller, more constrained, and forces the personal/shareable boundary to be explicit. Tier A can follow once Tier B's distribution mechanics are validated.

If user disagrees and wants both in parallel, fine — but be ready to decompose into separate specs anyway because the design forks for each are different.

## Skills the new session will use

- `superpowers:brainstorming` (mandatory; we're brainstorming)
- `superpowers:writing-plans` (after brainstorming produces a spec)
- `superpowers:subagent-driven-development` (for implementation, in a session after that)

## Session opening prompt suggestion

A good opening message for the user to send in the new chat:

> Read `docs/superpowers/community-tiers-brainstorming-brief.md` for context, then let's brainstorm the community-full and community-retrieval-only distribution tiers. Recommend starting with retrieval-only since it's more bounded.

That'll bootstrap the next session efficiently without dragging the entire operator-tier troubleshooting transcript along.
