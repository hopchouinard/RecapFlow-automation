---
title: "Patchou Personal Standard — Backend Tech Stack"
version: "0.15"
updated: "2026-09-05"
owner: "Patrick Chouinard"
status: "Locked foundation; technology-family backlog open"
source_conversation_id: "6a9c7aa4-7900-83ea-82d7-114fad1c26fd"
companions:
  - "frontend-tech-stack.md"
  - "hosted-services-tech-stack.md"
---

# Backend Tech Stack

## Purpose and authority

Use this reference when starting a backend, choosing a service framework, or extending the personal stack with another backend technology family. The objective is to reduce repeated choices while allowing concrete, justified exceptions.

This is a starter architecture document, not a complete backend specification. It consolidates [Standardize Tech Stack](https://chatgpt.com/c/6a9c7aa4-7900-83ea-82d7-114fad1c26fd). It records that conversation’s decisions rather than freshly verifying product capabilities or selecting compatible package versions. The authoritative frontend architecture and UI choices are in [Frontend Tech Stack](frontend-tech-stack.md). External hosting platforms and managed services are authoritative in [Hosted Services Tech Stack](hosted-services-tech-stack.md).

**Status vocabulary:** **Locked** means a selected standard; **approved exception** means a permitted departure under a concrete condition; **deferred** means the category remains unresolved. The document states selected technologies positively and keeps evaluation history outside the normative standard.

## Locked foundation

| ID | Decision | Scope and rationale |
| --- | --- | --- |
| BE-01 | Python for internally hosted application/service logic | Default for internal APIs, long-running services, AI/agent workloads, automation, ingestion, data processing, and infrastructure integrations. Fits the Python-centered AI ecosystem and orchestration-heavy workload. |
| BE-02 | TypeScript for Cloudflare and Vercel application workloads | The language boundary follows the deployment environment. Vercel applications may use TypeScript full-stack; internal TypeScript remains the web-UI language rather than a universal backend replacement. |
| BE-03 | FastAPI for internal Python backends/APIs | Default for internal APIs consumed by React UIs, agents, automation, scripts, and other services. Typed models, validation, and OpenAPI support are central reasons for the choice. |
| BE-04 | Django as an exceptional full-application option | Permitted when the integrated application platform is necessary and materially reduces work, especially its administration, ORM, authentication, permissions, and conventional CRUD capabilities. A need for an API alone does not establish this exception. |
| BE-05 | PostgreSQL for all authoritative relational application data | New applications begin with PostgreSQL regardless of expected size. SQLite is not an application-persistence alternative; it remains permitted only for disposable, rebuildable, or explicitly file-oriented data. |
| BE-06 | Shared PostgreSQL cluster for home-lab applications | The existing shared home-lab cluster is the default. Each application and environment receives its own database and credentials, without cross-application data access. |
| BE-07 | Dedicated PostgreSQL cluster by exception | A dedicated cluster requires a concrete workload, isolation, compatibility, recovery, security, or independent-lifecycle need. Application importance or an assumption of future growth is not sufficient by itself. |
| BE-08 | SQLAlchemy 2 + Alembic + Psycopg 3 for Python/FastAPI persistence | SQLAlchemy 2 is the standard Python data-access toolkit, Alembic owns schema migrations, and Psycopg 3 is the PostgreSQL driver. SQLAlchemy ORM covers ordinary entity persistence; Core or explicit SQL covers operations better expressed near SQL. |
| BE-09 | PostgreSQL + pgvector for service-backed vector retrieval | When an application has an appropriate PostgreSQL service, pgvector is the default vector store. Relational data, metadata, permissions, and retrieval state remain within the PostgreSQL operational boundary. |
| BE-10 | LanceDB OSS for embedded or offline retrieval | LanceDB OSS is the approved exception when retrieval must run in-process in a self-contained or offline-capable deployment without depending on a PostgreSQL service. It is a retrieval store rather than the default transactional application database. |
| BE-11 | Dedicated vector platform by measured exception only | Use a separate vector platform only when measured scale, isolation, filtered-search, multitenancy, quantization, or vector-native requirements exceed pgvector, including a dedicated PostgreSQL cluster where appropriate. |
| BE-12 | Vector data is derived and traceable | Embeddings must be reproducible from authoritative source data and carry provenance for the source revision, chunking strategy, embedding model and dimensions, preprocessing, creation time, and access scope. |
| BE-13 | PostgreSQL remains the only standard database service | PostgreSQL is the authoritative application store and the default service for persisted relational data. DuckDB does not introduce a second database service or shared source of truth. |
| BE-14 | DuckDB as an embedded analytical engine | DuckDB is an approved in-process analytical tool for Python, notebooks, command-line tasks, and packaged solutions. It is not operated as a networked shared database service. |
| BE-15 | PostgreSQL for ordinary operational analytics | Application dashboards, live reporting, current transactional data, modest aggregations, and multi-user analytical endpoints remain on PostgreSQL by default. |
| BE-16 | DuckDB for bounded analytical execution | Use DuckDB for batch analysis, file-oriented datasets, local exploration, transformations, and packaged offline analytics where columnar execution materially fits the workload. |
| BE-17 | Isolate heavy analytical reads | Heavy or reproducible analysis should use controlled exports, snapshots, or an appropriate read replica rather than imposing large scans on the shared transactional PostgreSQL cluster. |
| BE-18 | DuckDB files are derived analytical artifacts | A DuckDB database file is rebuildable analytical state unless a project explicitly establishes a different authority, lifecycle, backup, and recovery contract. |
| BE-19 | Shared analytical service by measured exception only | Use a shared analytical service only for demonstrated scale, concurrency, latency, or workload-isolation requirements beyond PostgreSQL plus embedded DuckDB. |
| BE-20 | NATS for internal messaging and events | NATS is the standard platform for asynchronous messaging, events, and decoupled internal service communication. |
| BE-21 | Core NATS for ephemeral communication | Use Core NATS for transient publish/subscribe, suitable request/reply, live notifications, and queue groups where subscribers need only messages published while they are connected. |
| BE-22 | JetStream for durable communication | Use JetStream when messages must survive restarts or subscriber downtime, require acknowledgement or redelivery, support replay, or feed durable consumers and work distribution. |
| BE-23 | HTTP/OpenAPI for straightforward synchronous APIs | Use the existing HTTP/OpenAPI service contract for direct synchronous request/response calls. The availability of NATS does not change the standard API surface. |
| BE-24 | JetStream for durable background jobs | JetStream is the standard foundation for queued or distributed work that requires persistence, acknowledgement, retry through redelivery, or worker decoupling. |
| BE-25 | cron for Linux and Unix scheduling | Use cron for recurring host-scheduled tasks in Linux and Unix environments. The scheduled command may perform bounded work or publish durable work to JetStream as the application requires. |
| BE-26 | launchd for macOS scheduling | Use launchd for recurring tasks and managed background processes on macOS. |
| BE-27 | Authentik as the universal internal identity provider | Internally hosted applications delegate human identity and sign-in to Authentik rather than implementing independent account systems. |
| BE-28 | OpenID Connect for internal application integration | OIDC is the standard protocol between internal applications and Authentik. Application authorization remains expressed in project-specific roles and permissions built on the authenticated identity. |
| BE-29 | Infisical for secrets management | Infisical is the standard internal system for storing and delivering application and service secrets. |
| BE-30 | Uptime Kuma, Prometheus, Grafana, Alertmanager, and Loki for observability | Uptime Kuma covers availability monitoring; Prometheus collects metrics; Grafana provides dashboards and exploration; Alertmanager routes metric-based alerts; Loki manages centralized logs. |
| BE-31 | Docker and Docker Compose for containers | Docker is the standard container runtime and image format; Docker Compose is the standard multi-container application definition and local/internal orchestration tool. |
| BE-32 | UniFi Cloud Gateway Fiber, Traefik, and step-ca for internal networking | UniFi Cloud Gateway Fiber is the network gateway; Traefik is the reverse proxy and application ingress; step-ca is the internal certificate authority. |
| BE-33 | Wiki.js for internal documentation | Wiki.js is the standard platform for internally hosted operational and knowledge documentation. Repository-local documentation remains with the project. |
| BE-34 | n8n for workflow automation | n8n is the standard workflow automation engine for integrations and orchestrated operational workflows. JetStream remains the durable application-job foundation. |
| BE-35 | pytest for Python testing | pytest is the standard Python framework for unit, integration, API, database, and service-level tests. Add plugins only for a concrete testing requirement. |
| BE-36 | Real disposable dependencies for integration testing | Tests that exercise PostgreSQL, pgvector, NATS, or another selected service use a real disposable instance where practical. Mocks remain suitable for controlled failures and genuinely external systems. |

The foundational application languages are **Python and TypeScript**. This does not replace SQL, declarative configuration, or small operating-system shell scripts with application code. Language selection also does not lock a package manager, interpreter version, server runtime, database, or deployment tool.

## Hosted-platform integration

The [Hosted Services Tech Stack](hosted-services-tech-stack.md) owns external providers. This backend document supplies the application services and the settled internal technology stack:

| Platform profile | Backend composition |
| --- | --- |
| Cloudflare information site | No application backend by default; limited edge or server-rendered TypeScript logic may be added while the project remains information-oriented. |
| Vercel web application | Next.js server-side TypeScript may own application logic; a separate Python service is unnecessary unless a concrete workload requires it. |
| Internal home-lab application | Python + FastAPI is the default service composition, with PostgreSQL, NATS, and other selected backend services as required. |

Framework selection does not mandate microservices, separate frontend/backend containers, or a particular process manager. Those choices belong to application or infrastructure architecture.

## Relational persistence

PostgreSQL is the universal relational database for authoritative application data. A small first release does not justify SQLite: the standard deliberately pays the modest PostgreSQL setup cost at the beginning to avoid a later database migration when the application grows.

SQLite remains suitable for disposable caches, rebuildable local indexes, temporary analysis artifacts, explicitly file-oriented exports, and tests whose purpose is unrelated to PostgreSQL behavior. It must not become the authoritative store for a new application. Development and integration testing that exercise persistence behavior should use PostgreSQL so concurrency, transactions, data types, constraints, migrations, and SQL behavior match the deployed database.

### Home-lab topology

Home-lab applications use the shared PostgreSQL cluster by default. Isolation is database-based rather than schema-based: each application and environment has its own database and credentials. Applications do not read or write another application's database, and shared tables do not become an undocumented integration mechanism.

A dedicated PostgreSQL cluster is an approved exception when at least one requirement justifies independent operation:

- high or unpredictable resource demand that could affect other applications;
- incompatible PostgreSQL versions or extensions;
- a stronger security or administrative boundary;
- independent upgrade, restart, tuning, backup, or recovery requirements;
- materially different availability or recovery objectives;
- a large or operationally critical dataset requiring independent capacity and restore procedures;
- third-party software with invasive ownership, extension, or privilege assumptions;
- measured database performance requirements needing workload-specific configuration.

The shared cluster's operational contract remains open. Version policy, upgrades, backup retention, point-in-time recovery, restore testing, monitoring, connection pooling, resource controls, migration credentials, and credential rotation will be decided separately.

### Externally deployed applications

PostgreSQL remains the selected database technology for externally deployed applications, with **Neon** as the standard managed provider under HF-01 in the hosted-services companion.


### Python data access and migrations

Python/FastAPI applications use **SQLAlchemy 2 + Alembic + Psycopg 3**.

- Use SQLAlchemy 2 typed declarative syntax for persistence models.
- Keep Pydantic API request and response contracts separate from SQLAlchemy persistence models. Their similarity does not make the database schema the public API.
- Use the ORM for ordinary entity persistence and relationships.
- Use SQLAlchemy Core or reviewed explicit SQL when it expresses a query, bulk operation, PostgreSQL feature, or performance-sensitive path more clearly.
- Treat Alembic autogeneration as a migration draft. Review and correct every generated migration, especially renames, constraints, data transformations, and destructive operations.
- Apply migrations as a controlled deployment operation rather than implicitly during application startup.
- Test persistence behavior against PostgreSQL.

Synchronous versus asynchronous SQLAlchemy sessions remains a separate application-runtime decision. FastAPI does not by itself require `AsyncSession`; the choice should follow the workload and concurrency model.

Within BE-08, use SQLAlchemy Core or reviewed explicit SQL for deliberately SQL-centric work. Django applications admitted under BE-04 use Django's ORM and migration system unless a documented project requirement governs otherwise.

## Vector storage and semantic retrieval

Use **PostgreSQL + pgvector** for service-backed applications. The decision follows topology rather than physical location: an internal embedded utility may qualify for LanceDB, while a client-hosted application that already operates PostgreSQL should normally use pgvector.

Keeping vectors in PostgreSQL allows retrieval data to share transactions, relational metadata, permissions, tenancy, backup, recovery, and lifecycle controls with the authoritative application records. Use PostgreSQL vector indexing and query tuning before adding a separate vector service. If vector workloads require resource isolation, evaluate a dedicated PostgreSQL cluster with pgvector before introducing another database technology.

Use **LanceDB OSS** when retrieval must be embedded in a packaged, self-contained, or offline-capable solution. The normal shape is in-process access to a local or deliberately portable dataset, with one application instance or a controlled writer model. Define refresh behavior when multiple processes read or write the same data, and define backup or regeneration when local storage is durable.

LanceDB does not replace PostgreSQL for transactional application state merely because the solution is installed at a client destination. Configuration, users, workflow state, audit history, and other authoritative relational data continue to follow the PostgreSQL standard unless another decision explicitly governs them.

A dedicated vector platform becomes a candidate only when evidence shows that pgvector cannot meet a defined requirement after appropriate schema design, indexing, query tuning, and workload isolation. Valid triggers include independent horizontal scaling, vector-native sharding or multitenancy, dense/sparse/multivector requirements, quantization, or unmet retrieval latency and recall targets.

### Vector provenance

Treat embeddings and vector indexes as derived, rebuildable data. Each vector record or collection must preserve or reference:

- authoritative source identity and revision;
- chunking strategy and version;
- embedding provider, model, and dimensions;
- preprocessing or normalization version;
- creation time;
- tenant and access-control scope.

Replacement or re-embedding workflows must not silently mix incompatible vector spaces. Keep authoritative source content outside a vector-only representation so the retrieval store can be rebuilt, migrated, or replaced.

## Analytical workloads

PostgreSQL remains the only standard database service and authoritative application store. Use it for application dashboards, live operational reporting, current transactional data, modest aggregations, scheduled summaries, and analytical endpoints serving concurrent users. Prefer indexes, aggregate tables, materialized views, scheduled precomputation, read replicas, or a dedicated PostgreSQL cluster before adopting another shared database service.

DuckDB is an approved **embedded analytical engine**, not a second operational database. Run it in-process from Python, notebooks, command-line tasks, batch jobs, or packaged applications for:

- analytical scans over Parquet, CSV, JSON, or DataFrames;
- bounded batch analysis and data transformation;
- local exploration and reproducible report generation;
- joining controlled database extracts with file-oriented datasets;
- packaged or offline analytical execution.

Heavy analysis should operate on controlled snapshots or exports, preferably columnar artifacts such as Parquet, when direct reads would burden the transactional PostgreSQL cluster. A read-only PostgreSQL connection or read replica may be appropriate when freshness is required, but the analytical job must have an explicit resource and consistency boundary.

DuckDB database files are derived analytical artifacts by default. They do not become authoritative application stores merely because they persist between runs. Any exception must define ownership, writers, durability, backup, recovery, and replacement behavior at project scope.

Operate DuckDB as the embedded analytical engine defined here. Adopt a shared analytical service only when measured scale, concurrency, latency, or workload-isolation requirements exceed PostgreSQL plus embedded DuckDB.

## Messaging and events

NATS is the standard internal messaging and event platform. Use **Core NATS** for ephemeral communication: transient publish/subscribe, request/reply where brokered decoupling is useful, live notifications, and queue groups whose members are online together. Message loss during subscriber downtime must be acceptable for a Core NATS subject.

Use **JetStream** when a message must survive restarts or subscriber downtime, when consumers acknowledge completion, or when redelivery, replay, retention, durable consumer state, or durable work distribution is required.

Use **HTTP/OpenAPI** for straightforward synchronous service APIs. Choose NATS because the interaction benefits from messaging semantics, not merely because two processes communicate.

## Background jobs and scheduling

Use **JetStream** for durable queued or distributed background work. Use **cron** for recurring host schedules on Linux and Unix systems, and **launchd** for recurring tasks or managed background processes on macOS. Externally hosted applications use the scheduler selected with their deployment platform.

Scheduling supplies the trigger; JetStream supplies durable work distribution when the triggered work must survive process or subscriber failure. The application decides whether a scheduled command executes bounded work directly or publishes a job to JetStream.

## Authentication and authorization

Use **Authentik** as the universal identity provider for internally hosted applications and **OpenID Connect (OIDC)** as the standard application integration protocol. Internal applications delegate sign-in and human identity to Authentik rather than creating independent account systems.

Externally hosted applications with users or protected capabilities use **Neon Auth** with Google and GitHub sign-in under the hosted-services companion. Application roles, permissions, resource ownership, and service or agent authorization remain application or cross-cutting architecture decisions built on the selected identity layer.

## Cross-cutting internal platform standards

- **Secrets:** Infisical.
- **Availability monitoring:** Uptime Kuma.
- **Metrics:** Prometheus.
- **Dashboards and observability exploration:** Grafana.
- **Alert routing:** Alertmanager.
- **Centralized logs:** Loki.
- **Containers:** Docker and Docker Compose.
- **Network gateway:** UniFi Cloud Gateway Fiber.
- **Reverse proxy and application ingress:** Traefik.
- **Internal certificate authority:** step-ca.
- **Internal documentation platform:** Wiki.js.
- **Workflow automation:** n8n.

Use n8n for integration and operational workflows. Use JetStream for durable application work distribution. Repository-local technical documentation stays with its codebase; Wiki.js is the shared internal documentation platform.

## Testing and continuous delivery

### Test toolchain

Use **pytest** for Python unit, integration, API, database, and service-level tests. Its fixture and parametrization model is the standard foundation for reusable test setup. Keep plugins requirement-driven rather than adopting a universal plugin bundle.

TypeScript and browser-facing testing follows the companion frontend standard: **Vitest** for TypeScript unit and integration tests, **React Testing Library** for observable React component behavior, and **Playwright** for browser-level integration and end-to-end workflows.

When behavior depends on PostgreSQL, pgvector, NATS, or another selected service, integration tests use real disposable infrastructure where practical. Do not substitute SQLite for PostgreSQL behavior. Mocks and fakes remain appropriate for deterministic failure paths, unavailable third-party systems, and tests whose subject does not include the dependency's behavior. The standard mechanism for controlling disposable service lifecycles remains open; do not treat either a project-specific Compose harness or Testcontainers usage as a universal choice yet.

Coverage is supporting evidence rather than a universal numeric gate. Each project selects meaningful coverage expectations according to its risk and behavior; a percentage alone does not establish adequate testing.

### CI execution boundary

GitHub Actions, hosted-runner policy, and cost controls are governed by the [Hosted Services Tech Stack](hosted-services-tech-stack.md). Backend repositories expose the canonical verification entry point required there and include the pytest and real-service checks defined above.

## API and agent-access architecture

The conversation framed capabilities as serving humans and agents. FastAPI’s typed request/response models and OpenAPI were identified as the natural contract for UI clients, automation, scripts, and agent consumers.

Apply that architectural intent by keeping service capabilities accessible through explicit APIs rather than making the browser the only integration surface. This is a consequence of the selected API-oriented architecture, not a separately completed API governance specification.

The following remain open: API versioning, error formats, pagination, compatibility policy, generated-client tooling, schema lifecycle, authentication and authorization, streaming/event transport, and agent/tool protocols. Framework support for WebSockets or streaming does not select either as the standard transport. Likewise, FastAPI’s use of Pydantic does not establish a universal schema library for every project or language.

## Approved exceptions

| Technology/case | Status and qualifying condition | Required scope discipline |
| --- | --- | --- |
| Django | Approved exception explicitly accepted alongside FastAPI, when the integrated application platform is necessary. | Explain which integrated capabilities remove enough work to justify the departure. A Django choice does not automatically replace the separately selected frontend with Django templates. |


Document a project-specific deviation with the problem, evidence, affected scope, and maintenance implications. Using an exception does not change the default for other projects. This document does not authorize a general migration of existing services.

## Backend technology-family backlog

The register names unresolved categories without cataloguing rejected or speculative technologies. The identifiers are reference keys, not an execution order; discuss and decide one family at a time.

| ID | Status | Family | Decision to resolve | Conversation context and current boundary |
| --- | --- | --- | --- | --- |
| BK-01 | Deferred | Runtime and dependency tooling | Python/TypeScript runtime versions, package managers, dependency locking, environment setup, update policy. | Python and TypeScript are selected languages; their tooling is open. |
| BK-02 | Locked | Relational persistence | PostgreSQL for authoritative data; shared home-lab cluster by default; dedicated cluster by exception; Neon for externally hosted PostgreSQL; SQLAlchemy 2 + Alembic + Psycopg 3 for Python/FastAPI. | TypeScript data access remains coupled to its runtime and developer-tooling decision. |
| BK-03 | Locked | Vector storage and semantic retrieval | pgvector for service-backed retrieval; LanceDB OSS for embedded/offline retrieval; a dedicated vector platform only after measured requirements exceed pgvector. | Detailed indexing, query tuning, and rebuild procedures belong to application architecture. |
| BK-04 | Locked | Messaging and event bus | NATS for internal messaging; Core NATS for ephemeral communication; JetStream for durable delivery; HTTP/OpenAPI for straightforward synchronous APIs. | Subject naming, schemas, retention, consumer ownership, and transaction-to-message coordination belong to application architecture or later cross-project conventions. |
| BK-05 | Locked | Background jobs and scheduling | JetStream for durable queued or distributed work; cron for Linux and Unix schedules; launchd for macOS schedules and managed background processes. | Externally hosted applications use the scheduling facility selected with their deployment platform. Job payloads, retry limits, idempotency, and worker lifecycle belong to application architecture. |
| BK-06 | Locked | Authentication and authorization | Authentik + OIDC is universal internally; Neon Auth with Google and GitHub sign-in is mandatory for externally hosted applications with protected capabilities. | Identity services own authentication. Applications own roles, permissions, resource ownership, and other authorization decisions. |
| BK-07 | Locked | Secrets management | Infisical is the internal secrets-management standard. | External secret delivery is selected in the hosted-services document. |
| BK-08 | Deferred | AI/model access | Provider abstraction, model routing, credentials, usage/cost accounting, failure handling. | AI/model access identified as a first-class family; no provider or library selected. |
| BK-09 | Deferred | Agent/tool protocols and accessibility | Capability discovery, schemas, tool interfaces, agent identity, relationship to human-facing capabilities. | Programmatic access is architectural intent; no protocol selected. |
| BK-10 | Deferred | Application configuration | Configuration formats, precedence, validation, environment separation. | No technology chosen. |
| BK-11 | Locked | Observability | Uptime Kuma for availability, Prometheus for metrics, Grafana for dashboards and exploration, Alertmanager for alert routing, and Loki for centralized logs. | External observability services are selected separately in the hosted-services document. |
| BK-12 | Locked | Testing and quality | pytest for Python; Vitest for TypeScript; React Testing Library for React components; Playwright for browser and end-to-end testing; real disposable service dependencies where practical. | Disposable-service lifecycle tooling remains open. Project-specific test selection and coverage expectations follow risk rather than a universal percentage. |
| BK-13 | Deferred | Git and repository conventions | Repository organization, branching, review, change records, dependency boundaries. | No standard selected. |
| BK-15 | Locked | Containers and packaging | Docker for containers and Docker Compose for multi-container application definitions and local/internal orchestration. | Image construction and deployment topology remain project and infrastructure architecture concerns. |
| BK-17 | Locked | Networking and ingress | UniFi Cloud Gateway Fiber for the network edge, Traefik for reverse proxy and application ingress, and step-ca for the internal certificate authority. | Routes, policies, certificates, and exposure boundaries remain operational configuration. |
| BK-18 | Deferred | Service/API communication | API conventions, OpenAPI lifecycle, generated clients, versioning, errors, streaming, compatibility. | FastAPI/OpenAPI provide the starting architecture; detailed rules are open. |
| BK-19 | Locked | Internal documentation | Wiki.js is the shared internal documentation platform; repository-local technical documentation remains with its project. | Document structure and content ownership remain documentation decisions. |
| BK-20 | Locked | Analytical and OLAP execution | PostgreSQL for ordinary operational analytics; DuckDB as the bounded embedded analytical engine; shared analytical services only after measured need. | Export formats, replica thresholds, artifact lifecycle, and workload-specific tuning belong to application architecture. |
| BK-21 | Locked | Workflow automation | n8n is the standard workflow automation engine for integrations and operational workflows. | JetStream remains the durable application-job foundation; workflow design remains application or operational architecture. |

Persistence, identity, and API conventions will constrain later implementation; external managed-service families are tracked in the hosted-services companion. Dependencies should inform which family is discussed next without treating this table as an implementation queue. Frontend-specific tooling and the future UI base remain in the frontend document.

Documents, files, object placement, export formats, replica thresholds, and analytical artifact lifecycle are not separate personal-stack decisions at this stage. Choose them within application architecture unless repeated evidence later justifies a new cross-project standard.

## Template for the next family decision

Copy this record when discussing a backlog item. Keep it **proposed** until Patrick accepts the decision; a coding agent’s recommendation alone does not lock a personal standard.

```markdown
### BK-XX — Family name
Status: Deferred | Proposed | Locked | Superseded
Decision date: TBD
Decision owner: Patrick Chouinard

Problem and scope:
- Workloads and deployment environments covered:
- Requirements and constraints:

Options:
- Requirements and material tradeoffs:

Decision:
- Default technology and architecture:
- Rationale:
- Approved exceptions and qualifying evidence:

Application:
- Interfaces and dependencies on other family decisions:
- Version/runtime policy, if decided:
- Existing-project migration implications:
- Verification or acceptance evidence:
- Remaining questions:

Provenance:
- Acceptance reference:
- Supersedes, if applicable:
```

## Coding-agent application checklist

- Classify the execution environment before applying the language default.
- For a new internal API, use BE-01 and BE-03 unless an applicable documented exception or project decision governs it.
- For Vercel, preserve the full-stack TypeScript allowance and the frontend document’s Next.js choice.
- Apply BE-35 and BE-36 when adding or changing backend tests; use the hosted-services companion for GitHub Actions and hosted delivery automation.
- Identify required backlog decisions explicitly. A project-level provisional choice is not a locked personal standard.
- Keep selected defaults, approved exceptions, and project-specific deviations distinct.
- Completion means each introduced backend technology has a clear default/exception/project-decision basis, and unresolved family choices remain visible.

## Design-system boundary and provenance

Typography, color tokens, spacing, radii, shadows, density, motion, dark-mode conventions, and visual identity belong to the future **Patchou Design System / Brand Kit**. They create no backend technology commitment.

The source explicitly accepts the platform-aware language split, FastAPI with the concrete Django exception, PostgreSQL persistence, pgvector and LanceDB retrieval roles, and PostgreSQL/DuckDB analytical roles. Evaluation history remains in the conversation rather than the normative stack.

Revision 0.15 records Neon as the external PostgreSQL provider and Neon Auth with Google and GitHub sign-in as the mandatory external authentication service. The hosted-services companion remains authoritative for provider rules.
