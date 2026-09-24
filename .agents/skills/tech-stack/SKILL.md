---
name: tech-stack
description: Patchou personal technology standard for frontend, backend, and hosted services. Read this BEFORE selecting or adding any framework, library, database, host, auth provider, message bus, scheduler, test tool, or dependency; before scaffolding a new project; and before resolving a stack decision marked Deferred.
version: 0.1.0
author: Patrick Chouinard
license: proprietary
metadata:
  hermes:
    tags: [standards, architecture, tech-stack, scaffolding]
    category: software-development
---

# Patchou Technology Standard

These are the preferred technologies for every project on this workstation. They
are **not absolute law** — exceptions are permitted with a concrete, expressible,
and describable reason. They are not permitted silently.

**Status vocabulary.** *Locked* = selected standard. *Approved exception* = a
permitted departure under a stated condition. *Deferred* = no standard chosen yet;
the project must choose explicitly and record the choice as provisional.

## 1. Classify the profile first

Every other decision follows from this. Do not skip it.

| Profile | Frontend | Backend | Host |
| --- | --- | --- | --- |
| **Information site** | Astro + TS, static-first, React islands | none by default; limited edge/SSR TS | Cloudflare Workers |
| **External web app** | Next.js + TS + React | TypeScript server-side; Python only for a concrete workload | Vercel |
| **Internal home-lab app** | React + Vite + TS | Python + FastAPI | Home lab (Docker Compose) |

If an information site grows connected state and application workflows, reassess
it against the external web app profile.

## 2. Locked decisions

### Frontend (FE)

| ID | Decision |
| --- | --- |
| FE-01 | TypeScript for all browser/Cloudflare/Vercel application code |
| FE-02 | Astro + TypeScript for information-oriented sites |
| FE-03 | Next.js + TypeScript for externally hosted web applications |
| FE-04 | React + Vite + TypeScript for internal web UIs |
| FE-05 | React as the common interactive component model everywhere |
| FE-06 | Tailwind CSS for styling, all three architectures |
| FE-07 | shadcn/ui (Base UI variant) for components; Base UI for primitives |
| FE-08 | Lucide icons primary; Tabler only for a concept Lucide lacks |
| FE-09 | Vitest for TypeScript unit/integration tests |
| FE-10 | React Testing Library for React component behavior |
| FE-11 | Playwright for browser and end-to-end testing |

### Backend (BE)

| ID | Decision |
| --- | --- |
| BE-01 | Python for internally hosted application/service logic |
| BE-02 | TypeScript for Cloudflare and Vercel workloads |
| BE-03 | FastAPI for internal Python backends/APIs |
| BE-04 | Django only as an exception, when the integrated platform genuinely reduces work. "I need an API" does not qualify |
| BE-05 | PostgreSQL for all authoritative relational data, from day one. SQLite is never the app store |
| BE-06 | Shared home-lab PostgreSQL cluster by default; own database + credentials per app/env |
| BE-07 | Dedicated PostgreSQL cluster by exception only (isolation, compatibility, recovery, measured load) |
| BE-08 | SQLAlchemy 2 + Alembic + Psycopg 3 for Python persistence |
| BE-09 | PostgreSQL + pgvector for service-backed vector retrieval |
| BE-10 | LanceDB OSS for embedded/offline in-process retrieval |
| BE-11 | Dedicated vector platform only after measured pgvector shortfall |
| BE-12 | Vector data is derived, reproducible, and carries provenance |
| BE-13 | PostgreSQL is the only standard database *service* |
| BE-14 | DuckDB as an embedded analytical engine, never a shared service |
| BE-15 | PostgreSQL for ordinary operational analytics |
| BE-16 | DuckDB for bounded batch/file-oriented/offline analysis |
| BE-17 | Isolate heavy analytical reads (snapshots, exports, replica) |
| BE-18 | DuckDB files are rebuildable derived artifacts |
| BE-19 | Shared analytical service by measured exception only |
| BE-20 | NATS for internal messaging and events |
| BE-21 | Core NATS for ephemeral pub/sub, request/reply, queue groups |
| BE-22 | JetStream when messages must survive restarts, ack, retry, or replay |
| BE-23 | HTTP/OpenAPI for straightforward synchronous APIs |
| BE-24 | JetStream for durable background jobs |
| BE-25 | cron for Linux/Unix scheduling |
| BE-26 | launchd for macOS scheduling |
| BE-27 | Authentik as the universal internal identity provider |
| BE-28 | OpenID Connect between internal apps and Authentik |
| BE-29 | Infisical for internal secrets — **internal only** |
| BE-30 | Uptime Kuma, Prometheus, Grafana, Alertmanager, Loki for observability |
| BE-31 | Docker + Docker Compose for containers |
| BE-32 | UniFi Cloud Gateway Fiber, Traefik, step-ca for internal networking |
| BE-33 | Wiki.js for shared internal docs; repo-local docs stay in the repo |
| BE-34 | n8n for workflow automation (JetStream stays the durable job foundation) |
| BE-35 | pytest for Python testing |
| BE-36 | Real disposable service dependencies for integration tests — never SQLite-for-PostgreSQL |

### Hosted services (HS)

| ID | Decision |
| --- | --- |
| HS-01 | Cloudflare Workers for information-oriented sites |
| HS-02 | Vercel for externally hosted web applications |
| HS-03 | GitHub Actions for hosted CI/CD orchestration |
| HS-04 | Cost-controlled GitHub-hosted Linux runners; narrow triggers, concurrency cancellation, hard budget |
| HS-05 | Isolated self-hosted runners for trusted internal delivery only; never untrusted PR code |
| HS-06 | **One canonical verification command per repository**, used identically by humans, agents, and CI |
| HS-07 | Neon for externally hosted PostgreSQL |
| HS-08 | Neon Auth mandatory for external apps with users or protected capabilities; Google + GitHub sign-in |
| HS-09 | Cloudflare R2 for hosted object storage, only when actually required |
| HS-10 | No hosted realtime service by default |
| HS-11 | Vercel Workflow for durable background execution in Vercel apps |
| HS-12 | Vercel Cron within plan limits (Hobby = daily, imprecise) |
| HS-13 | Hermes as higher-frequency scheduler for personal, noncritical Vercel apps — clock and trigger only |
| HS-14 | Platform-native secrets: Vercel for Vercel, Cloudflare for Cloudflare. Never internal Infisical |

## 3. Deferred — decide explicitly, record as provisional

Do not silently pick these. Choose, then write the choice into `STACK-DECISIONS.md`
marked provisional. A project-level provisional choice is **not** a locked personal
standard, and does not set the default for other projects.

| ID | Family |
| --- | --- |
| BK-01 | Runtime & dependency tooling — versions, package managers, lockfiles, env setup |
| BK-08 | AI/model access — provider abstraction, routing, credentials, cost accounting |
| BK-09 | Agent/tool protocols — capability discovery, schemas, agent identity |
| BK-10 | Application configuration — formats, precedence, validation, env separation |
| BK-13 | Git & repository conventions — organization, branching, review, change records |
| BK-18 | Service/API communication — versioning, errors, pagination, generated clients |
| HF-06 | External observability outside the home lab |
| HF-07 | Transactional communications (hosted email, etc.) |
| — | Frontend: developer tooling, app conventions, specialized UI (tables/charts/editors), shared component distribution |

Typography, color tokens, spacing, radii, shadows, density, motion, and dark-mode
conventions belong to the future **Patchou Design System / Brand Kit**. Selecting
Tailwind and shadcn/ui creates no visual-identity commitment.

## 4. Approved exceptions already on the books

- **Django** instead of FastAPI, when the integrated platform materially reduces work.
- **Tabler icon** when Lucide lacks the concept.
- **Targeted custom CSS** when Tailwind expresses a requirement poorly.
- **React islands** for substantial interaction inside an Astro site.
- **Existing HTMX apps** keep being maintained; no blanket rewrite, and HTMX is not a second default.
- **LanceDB** instead of pgvector for embedded/offline retrieval.
- **Dedicated PostgreSQL cluster** under the BE-07 conditions.

## 5. Taking a new exception

Permitted, but it must be concrete, expressible, and describable. Record in the
project's `STACK-DECISIONS.md`:

1. the decision ID being departed from;
2. the specific problem the standard does not solve here;
3. the evidence (measurement, constraint, requirement — not a hunch about future growth);
4. the affected scope;
5. the maintenance and migration implications.

Application importance, expected growth, or "it's simpler for now" are **not**
sufficient reasons on their own.

## 6. Completion criteria

You are done when **every technology introduced** is covered by one of:

- a locked default above,
- an applicable approved exception,
- or a documented project choice in `STACK-DECISIONS.md`.

…and every required Deferred family the project touched has been explicitly
resolved and marked provisional, rather than decided by accident.

## 7. Full documents

Read these only when justifying an exception, resolving a Deferred family, or when
the rationale actually matters. They are the authoritative source; the tables above
are a navigational summary.

- `references/frontend-tech-stack.md` — frontend composition, UI layers, testing
- `references/backend-tech-stack.md` — services, persistence, vectors, analytics, messaging, identity, internal platform
- `references/hosted-services-tech-stack.md` — hosting profiles, managed services, auth/storage/workflow/secrets boundaries, GitHub Actions policy
