---
title: "Patchou Personal Standard — Hosted Services Tech Stack"
version: "0.5"
updated: "2026-09-05"
owner: "Patrick Chouinard"
status: "Locked hosted application foundation; remaining service families open"
source_conversation_id: "6a9c7aa4-7900-83ea-82d7-114fad1c26fd"
companions:
  - "frontend-tech-stack.md"
  - "backend-tech-stack.md"
---

# Hosted Services Tech Stack

## Purpose and authority

Use this reference when an application consumes externally hosted platforms or managed services. It owns reusable choices for public hosting, managed data services, external identity, storage, asynchronous execution, observability, communications, and hosted delivery automation.

The [Frontend Tech Stack](frontend-tech-stack.md) owns browser frameworks and UI composition. The [Backend Tech Stack](backend-tech-stack.md) owns application services, data technologies, messaging, internal platform services, and testing. This document selects the hosted provider or managed service through which those standards operate outside the home lab.

Infrastructure topology, deployment sequencing, rollback procedures, host placement, service sizing, backup procedures, and application-specific integration design belong to infrastructure or application architecture. They enter this standard only when repeated use establishes a reusable technology choice.

**Status vocabulary:** **Locked** means a selected standard; **approved exception** means a permitted departure under a concrete condition; **deferred** means that the hosted-service family remains unresolved. Keep rejected-provider catalogues and speculative services outside the normative document.

## Locked decision register

| ID | Decision | Scope and rationale |
| --- | --- | --- |
| HS-01 | Cloudflare Workers for information-oriented sites | Cloudflare Workers is the selected host for information sites, documentation, reports, portals, and information-oriented dashboards. Astro + TypeScript is the companion frontend composition; React islands provide selective interaction. |
| HS-02 | Vercel for externally hosted web applications | Vercel is the selected host for application-oriented external web experiences. Next.js + TypeScript is the companion application composition and may include server-side application logic. |
| HS-03 | GitHub Actions for hosted CI/CD orchestration | GitHub Actions is the standard hosted automation control plane for verification, release, and deployment. Destination-specific deployment adapters remain implementation choices within each platform. |
| HS-04 | Cost-controlled GitHub-hosted Linux CI | Standard GitHub-hosted Linux runners are the default for ordinary CI. Narrow triggers, concurrency cancellation, evidence-based matrices, bounded artifacts, and a hard paid-usage budget control consumption. |
| HS-05 | Isolated self-hosted runners for trusted internal delivery | Self-hosted runners are approved when trusted deployment needs access to the home lab or measured workload cost justifies local execution. They must not execute untrusted pull-request code. |
| HS-06 | One canonical verification entry point per repository | Each repository exposes one documented verification command used identically by developers, coding agents, and GitHub Actions. The application-layer documents define the relevant test tools. |
| HS-07 | Neon for externally hosted PostgreSQL | Neon is the standard managed PostgreSQL provider for externally hosted applications. It preserves the universal PostgreSQL data standard while fitting small, intermittent, and independently deployed applications. |
| HS-08 | Neon Auth for mandatory external application authentication | Any externally hosted application with users or protected capabilities uses Neon Auth. Google and GitHub are the standard sign-in providers. Applications do not implement or store their own primary credentials. |
| HS-09 | Cloudflare R2 for hosted object storage when required | R2 is the standard hosted object-storage service when an application needs durable files or objects outside PostgreSQL. Applications without such data do not provision a storage service. |
| HS-10 | No hosted realtime service by default | Realtime infrastructure is introduced only for a concrete application requirement. The absence of a selected service is deliberate and does not weaken ordinary request/response applications. |
| HS-11 | Vercel Workflow for durable background execution in Vercel applications | Keep application-owned workflows in the same repository, deployment boundary, credentials, and diagnostic surface as the Vercel application. This is especially important when coding and operations agents perform development, deployment, and diagnosis. |
| HS-12 | Vercel Cron within the active plan's limits | Use Vercel Cron for native scheduled starts when its frequency and precision satisfy the application. Vercel Hobby supports daily, imprecisely timed jobs and is not the standard mechanism for higher-frequency schedules. |
| HS-13 | Hermes as the higher-frequency hobby scheduler | For personal and noncritical Vercel applications, Hermes may provide higher-frequency scheduling and invoke an authenticated Vercel endpoint that starts a Vercel Workflow. Workflow state, retries, execution, and diagnostics remain on Vercel. |
| HS-14 | Platform-native secrets for hosted workloads | Store each hosted secret with the platform executing the application layer that consumes it. Use Vercel environment variables and secrets for Vercel workloads and Cloudflare secrets for Cloudflare workloads. Infisical remains internal-only. |

## Hosted application profiles

### Cloudflare information sites

**Composition:** Cloudflare Workers → Astro + TypeScript → static HTML and CSS with React islands where substantial interaction warrants them.

Use this profile for information-oriented experiences. Interactive charts, filters, search, and isolated client behavior do not by themselves require an application backend. Limited edge logic or Astro server rendering is permitted while the project remains information-oriented.

Cloudflare-specific runtime configuration and any additional managed services remain open. If extensive application workflows or connected state become the defining behavior, reassess the application against the Vercel profile.

### Vercel web applications

**Composition:** Vercel → Next.js + TypeScript → React UI with TypeScript server-side application logic where appropriate.

Use this profile for externally hosted application-oriented web experiences. A separate Python service is not required for language uniformity. Neon supplies PostgreSQL and Neon Auth supplies authentication. Cloudflare R2 is added when the application requires object storage. Vercel Workflow supplies durable application-owned background execution, with Vercel Cron or Hermes supplying scheduled starts according to the boundary below. Observability and other hosted services are selected through the remaining backlog.

### Internal applications

The internal technology standard remains in the backend companion: Python and FastAPI, PostgreSQL, NATS and JetStream, Docker and Docker Compose, Authentik and OIDC, Infisical, the selected observability stack, UniFi networking, Traefik, step-ca, Wiki.js, and n8n. This hosted-services document does not redesign their infrastructure topology.

## Authentication boundary

Authentication is mandatory for any externally hosted application that has users, private data, administrative functions, or protected capabilities. Public information sites with no protected behavior do not add authentication merely to satisfy ceremony.

Use **Neon Auth** and enable **Google** and **GitHub** as the standard sign-in providers. A project may enable another Neon Auth-supported identity provider for a concrete audience requirement. The application must not create its own password database, credential-verification system, account-recovery mechanism, token issuer, or parallel primary identity service.

Neon Auth owns identity proof, provider integration, sessions, and authentication tokens. The application owns authorization: roles, permissions, tenant membership, resource ownership, administrative powers, and decisions about what an authenticated identity may access or change.

Keep authentication integration behind a small application-owned boundary so provider-specific SDK calls do not spread through business logic. This boundary supports testing and limits migration cost; it is not an excuse to reconstruct authentication badly in a utility module with an ambitious filename.

## Hosted storage boundary

Use **Cloudflare R2** when an externally hosted application requires object storage. Prefer its S3-compatible interface where it covers the requirement. Keep object metadata, ownership, and access-control references in PostgreSQL when they are part of authoritative application state.

Do not provision R2 for ordinary relational records, small configuration values, or rebuildable temporary output. Backup, retention, versioning, lifecycle, and recovery procedures remain application or infrastructure architecture decisions.

## Hosted workflow and scheduling boundary

Use **Vercel Workflow** for durable background execution owned by an application hosted on Vercel. Keep workflow definitions in the application repository and deployment so coding and operations agents can inspect the implementation, deployment, runs, retries, failures, and logs through one platform. Typical starts include application requests, user actions, webhooks, and other application events.

Use **Vercel Cron** when the active plan supplies the required frequency and timing precision. On Vercel Hobby, scheduled jobs may run at most once per day and do not have precise execution timing.

For personal and noncritical applications that need more frequent scheduled starts, **Hermes** may schedule the invocation and call a secured Vercel entry point. Hermes acts only as the clock and trigger. Vercel Workflow continues to own durable state, steps, retries, execution history, and diagnosis. The entry point must authenticate Hermes, validate the request, accept a stable idempotency key, and return promptly after starting the workflow.

Do not make availability-critical or user-facing guarantees depend on a homelab-hosted Hermes scheduler. When scheduled execution becomes operationally important, move the schedule to the appropriate native paid hosting capability.

Use **Cloudflare Workflows** and its scheduled triggers when the application's dynamic execution already runs on Cloudflare. Do not place a Vercel application's workflows on Cloudflare solely to bypass Vercel Hobby scheduling limits.

## Hosted secrets and configuration boundary

Use the **native secret and environment-configuration service of the hosting platform that executes the consuming application layer**. Vercel workloads use Vercel environment variables and secrets. Cloudflare workloads use Cloudflare secrets and environment configuration. If an application spans platforms, give each platform only the secrets required by the layer it executes.

**Infisical is restricted to internally hosted services.** Do not make a hosted application depend on connectivity to the internal Infisical service, and do not treat Infisical as the source of truth for externally hosted application secrets.

Keep secrets out of source control, build output, client bundles, logs, workflow payloads, and ordinary configuration files. Separate production, preview, and development values using the hosting platform's environment model. Detailed naming, rotation, emergency revocation, and operator procedures belong to engineering or application operations standards.

## GitHub Actions service standard

Patrick currently uses **GitHub Pro**. As of this revision, its 3,000 monthly GitHub-hosted minutes for private repositories are planning context rather than an architecture guarantee. Confirm current allowances and prices in [GitHub included usage](https://docs.github.com/en/billing/reference/product-usage-included) before relying on them.

Use standard GitHub-hosted Linux runners for ordinary pull-request and default-branch verification. A normal service policy has three scopes:

1. Pull requests run formatting validation, linting, static type checking, unit tests, targeted integration tests, and the applicable production build.
2. The default branch adds important Playwright workflows and other integration checks needed before release.
3. Release or manually requested workflows run broader compatibility suites, publish artifacts or containers, and invoke the selected host's deployment adapter.

Control hosted consumption as part of the standard:

- avoid duplicate push and pull-request runs for the same change;
- cancel superseded runs on the same branch through workflow concurrency;
- add operating-system, runtime-version, browser, or service-version matrices only for compatibility the project promises;
- retain artifacts for bounded periods and prefer uploading diagnostic traces, screenshots, and logs on failure;
- add scheduled workflows only for a concrete detection need;
- configure a paid Actions budget with spending stopped at the selected limit.

Run self-hosted workers in isolated environments with narrowly scoped credentials and network access. Accept only trusted workflows and protected refs. GitHub-hosted runners handle untrusted pull-request code.

## Hosted-service technology-family backlog

The register contains recurring hosted-service families that could become personal standards. It does not prescribe infrastructure architecture or catalogue services that have no established need.

| ID | Status | Family | Decision to resolve | Current boundary |
| --- | --- | --- | --- | --- |
| HF-01 | Locked | Managed PostgreSQL | Neon is the standard externally hosted PostgreSQL provider. | PostgreSQL remains the universal relational technology; connection and data-access details follow each application runtime. |
| HF-02 | Locked | External identity | Neon Auth is mandatory for externally hosted applications with users or protected capabilities; Google and GitHub are the standard sign-in providers. | Authentik + OIDC remains universal internally. Applications own authorization and never implement a parallel primary authentication system. |
| HF-03 | Locked | Object and file storage | Cloudflare R2 is the standard hosted object store when an application requires durable files or objects outside PostgreSQL. | Storage is conditional rather than universal; applications without object data provision no storage service. |
| HF-04 | Locked | Background work and scheduling | Vercel Workflow is standard for durable execution in Vercel applications. Vercel Cron supplies native schedules within plan limits; Hermes may trigger personal, noncritical workflows more frequently. Cloudflare Workflows is platform-local to dynamic Cloudflare applications. | Keep workflow ownership and diagnosis with the application host. Hermes may supply the clock but must not become the workflow state store or execution engine. |
| HF-05 | Locked | External secrets and configuration | Use the native secret and environment-configuration service of the platform executing the consuming layer: Vercel for Vercel workloads and Cloudflare for Cloudflare workloads. | Infisical is internal-only. In a multi-platform application, each platform receives only the secrets required by its own layer. |
| HF-06 | Deferred | External observability | Select hosted error reporting, metrics, logs, traces, uptime monitoring, and alert delivery needed outside the home lab. | The internal observability stack remains locked; public-hosted integration is unresolved. |
| HF-07 | Deferred | Transactional communications | Select hosted email and other application-generated communications when a project requires them. | No provider is selected; marketing automation is outside this family unless separately required. |

## Remaining decision order

The externally hosted application foundation is now Vercel, Neon PostgreSQL, Neon Auth, conditional Cloudflare R2, Vercel Workflow with plan-appropriate scheduling, platform-native hosted secrets, and GitHub Actions. Resolve the remaining hosted-service families one at a time, beginning with external observability when a concrete need exceeds native platform diagnostics.

Do not add a realtime, messaging, storage, or auxiliary service speculatively. A service becomes part of the standard only when a recurring requirement gives it a job.

## Approved exceptions and scope discipline

A hosted service may deviate from the standard for a concrete product, customer, regulatory, regional, compatibility, isolation, recovery, or measured performance requirement. Record the requirement, affected capabilities, data ownership, operational implications, and migration path with the project.

A provider feature used by one application does not become part of the standard automatically. Add only technologies that Patrick explicitly accepts as reusable defaults or defined exceptions.

## Coding-agent application checklist

- Classify the application as a Cloudflare information site, Vercel web application, or internal application before selecting hosted services.
- Apply the frontend and backend companion standards inside that profile.
- Use HS-03 through HS-06 for hosted verification and delivery automation.
- Use Neon for externally hosted PostgreSQL, Neon Auth for protected applications, and R2 only when object storage is required.
- Keep Vercel application workflows on Vercel. Use Vercel Cron within plan limits or Hermes as a higher-frequency trigger for personal, noncritical workloads.
- Store hosted secrets on the platform executing the consuming layer. Never route hosted-secret management through internal Infisical.
- Treat each deferred hosted service as a project-specific provisional choice until Patrick locks a standard.
- Record any deviation with its concrete reason and scope.

## Design-system boundary and provenance

Typography, color tokens, spacing, radii, shadows, density, motion, dark-mode conventions, and visual identity belong to the future **Patchou Design System / Brand Kit**. Hosted-provider convenience creates no design-system commitment.

Revision 0.5 additionally locks platform-native hosted secrets: Vercel workloads use Vercel environment variables and secrets, Cloudflare workloads use Cloudflare secrets and environment configuration, and Infisical remains restricted to internally hosted services.
