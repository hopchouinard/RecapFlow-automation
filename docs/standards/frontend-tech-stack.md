---
title: "Patchou Personal Standard — Frontend Tech Stack"
version: "0.6"
updated: "2026-09-05"
owner: "Patrick Chouinard"
status: "Locked baseline with explicit deferred decisions"
source_conversation_id: "6a9c7aa4-7900-83ea-82d7-114fad1c26fd"
companions:
  - "backend-tech-stack.md"
  - "hosted-services-tech-stack.md"
---

# Frontend Tech Stack

## Purpose and authority

Use this reference when starting a frontend, selecting its application composition, or evaluating a substantial frontend change. The objective is to reduce repeated technology decisions and integration overhead across similar personal projects. These are opinionated defaults with defined exceptions, not a requirement to rewrite every existing application.

This document consolidates the decisions in [Standardize Tech Stack](https://chatgpt.com/c/6a9c7aa4-7900-83ea-82d7-114fad1c26fd). It records the conversation’s selected technologies, not a fresh product comparison or a verified package-version matrix. Backend language, framework, and service exceptions are authoritative in [Backend Tech Stack](backend-tech-stack.md). External hosting platforms and managed services are authoritative in [Hosted Services Tech Stack](hosted-services-tech-stack.md).

**Status vocabulary:** **Locked** means a selected standard; **approved exception** means a permitted departure under the stated condition; **deferred** means no standard has been chosen. Architecture guidance below explains how the selected pieces fit together; it does not silently select additional libraries.

## Locked decision register

| ID | Decision | Scope and rationale |
| --- | --- | --- |
| FE-01 | TypeScript | Standard language for browser application code and Cloudflare/Vercel workloads; also used for internally hosted web UIs. Consolidates substantial JavaScript development around one language. |
| FE-02 | Astro + TypeScript for information-oriented sites | Standard content-first composition for static or primarily static experiences, with client JavaScript introduced where needed. The platform companion maps this composition to Cloudflare Workers. |
| FE-03 | Next.js + TypeScript for externally hosted web applications | Standard composition for application-oriented web experiences, with or without server-side application logic. The platform companion maps this composition to Vercel. |
| FE-04 | React + Vite + TypeScript for internal web UIs | Rich internal applications and simple new tools expected to grow. Provides a browser application that consumes service APIs without requiring Next.js as the internal default. |
| FE-05 | React as the common interactive component model | React islands in Astro, React through Next.js on Vercel, and React directly with Vite internally. Reuses component knowledge and avoids parallel UI ecosystems. |
| FE-06 | Tailwind CSS | Shared styling technology across all three frontend architectures. Keeps styling intent close to components and provides a common implementation vocabulary. |
| FE-07 | shadcn/ui with Base UI | Shared React component foundation: shadcn/ui supplies application component source; Base UI supplies underlying accessible primitives. Source ownership makes components inspectable and adaptable by coding agents. |
| FE-08 | Lucide primary; Tabler Icons secondary | Lucide supplies the default icon vocabulary. Tabler fills a required concept missing from Lucide; this is a conditional exception, not a second interchangeable default. |
| FE-09 | Vitest for TypeScript tests | Standard runner for frontend and other TypeScript unit and integration tests. It provides the fast local and CI feedback layer beneath component and browser testing. |
| FE-10 | React Testing Library for React component behavior | Standard React component-testing library, paired with Vitest. Tests exercise observable DOM behavior and user interaction rather than component internals. |
| FE-11 | Playwright for browser and end-to-end testing | Standard for real-browser workflows, frontend/backend integration, authentication flows, compatibility checks, traces, screenshots, and release-critical user journeys. |

## Hosted-platform integration

The [Hosted Services Tech Stack](hosted-services-tech-stack.md) owns external hosting and managed-service choices:

| Application profile | Frontend composition |
| --- | --- |
| Cloudflare information site | Astro + TypeScript, static-first, with React islands for substantial interaction. |
| Vercel web application | Next.js + TypeScript with React and server-side TypeScript where appropriate. |
| Internal home-lab application | React + Vite + TypeScript consuming service APIs. |

This document owns frontend composition inside each profile. The hosted-services document owns external providers; the backend companion retains the internal technology standard.

For the Vercel application profile, the hosted-services companion currently supplies Neon PostgreSQL, mandatory Neon Auth with Google and GitHub sign-in for protected applications, and Cloudflare R2 only when object storage is required.

## Shared UI implementation

The selected layers have distinct responsibilities:

1. **Tailwind CSS:** styling and the implementation vocabulary for layout and visual properties.
2. **Base UI:** underlying React interaction primitives and accessibility behavior.
3. **shadcn/ui:** reusable application component source maintained in the project.
4. **React:** common interactive component model within the selected platform framework.
5. **Lucide:** primary icon source; Tabler only under FE-08’s exception.

Use the Base UI variant when adopting shadcn components for this standard. Project-generated components and configuration must preserve the selected Tailwind, shadcn/ui, and Base UI foundation.

Tailwind is the default styling architecture. Use targeted custom CSS when it expresses a requirement more clearly. Exact compatible versions remain part of the developer-tooling decision.

The technology commitment supports token-based styling; actual token values and visual rules await the separate design system. Shared token or component distribution remains a deferred stack decision.

## Testing and delivery

Use **Vitest** for TypeScript unit and integration tests. Use **React Testing Library with Vitest** when the subject is a React component; query and interact through observable DOM semantics such as roles, labels, visible content, and user behavior. Implementation-detail selectors and broad mocking are not the standard testing style.

Use **Playwright** for browser-level integration and end-to-end workflows. Cover critical journeys and browser-dependent boundaries rather than reproducing every unit assertion through a browser. Important Playwright workflows run on the default branch; a focused smoke suite may run on every pull request when the project's risk justifies it. Broader browser matrices belong to release or explicitly requested verification unless the project promises wider continuous compatibility.

Frontend repositories use **GitHub Actions** under the shared policy in the [Hosted Services Tech Stack](hosted-services-tech-stack.md). Each repository exposes one canonical verification command used locally and in CI. Pull requests ordinarily run the selected formatting, linting and type checks, Vitest tests, targeted integration tests, and a production build. Exact linting, formatting, package-management, and TypeScript configuration remain part of the unresolved developer-tooling family.

Cloudflare and Vercel provider choices are governed by the hosted-services companion. Infrastructure topology and application deployment procedures are defined outside this technology-stack document.

## Approved exceptions and existing applications

| Case | Permitted behavior | Boundary |
| --- | --- | --- |
| A required icon concept is absent from Lucide | Use a suitable Tabler icon. | Keep the product’s primary icon family consistent; avoid casual family mixing. |
| Tailwind expresses a styling requirement poorly | Use targeted custom CSS. | Tailwind remains the main styling architecture. |
| Existing HTMX application | Continue maintaining it. Evaluate migration when substantial changes create a reason to revisit the UI. | No blanket rewrite; HTMX is not a second default for new internal projects. |
| Substantial interaction within an Astro site | Use React islands and suitable shared React components. | This is part of the approved Astro architecture, not a reason to hydrate the entire site. |

A project may deviate from the standard for a concrete requirement. Record the reason, affected scope, and maintenance implications with that project.

## Deferred technology decisions

These placeholders identify unresolved standard-stack categories.

| Area | Decision still needed |
| --- | --- |
| Versions and developer tooling | Compatible framework/runtime versions, package manager, lockfiles, linting, formatting, and TypeScript configuration. |
| Application conventions | Internal routing, client/server state, data fetching, forms, validation, error handling, and API client generation. |
| Specialized UI | Tables, charts, graphs, editors, and other components beyond the selected foundation. |
| Shared component distribution | Whether to create a Patchou UI base or registry, its ownership, versioning, and adoption mechanism. The conversation proposed this as future work. |

## Boundary: future design and brand system

The technology stack selects Tailwind, shadcn/ui, Base UI, and icon libraries. A separate **Patchou Design System / Brand Kit** will decide typography, color tokens, spacing philosophy, radii, shadows, density, motion, visual tone, dark-mode conventions, and other visual identity rules.

Typography remains deferred to the **Patchou Design System / Brand Kit**. An eventual UI registry may distribute those decisions after they are made.

## Coding-agent application checklist

- Read the hosted-services companion for an external application; select FE-02, FE-03, or FE-04 according to the application profile.
- Apply FE-01 and FE-05 through FE-11 within that composition.
- Inspect existing project decisions and dependencies before proposing a migration; preserve the HTMX transition rule.
- Consult the backend document when adding server behavior or a service integration.
- Resolve a required deferred choice explicitly at project scope. Keep provisional choices distinguishable from locked personal standards.
- Record any deviation with its reason and scope. Completion means every introduced technology is covered by a locked default, an applicable exception, or a documented project choice.

## Decision provenance

The source conversation contains explicit acceptance of the platform-aware language split, Astro for Cloudflare, Next.js for Vercel, React/Vite for internal UIs, Tailwind CSS, shadcn/ui with Base UI, and Lucide with Tabler as secondary. The HTMX transition and targeted custom-CSS allowances accompany the recommendations that were accepted. The final typography exchange explicitly separates the future design/brand system from this stack.

Revision 0.6 records the accepted Neon, Neon Auth, and conditional R2 services supplied to externally hosted frontend applications; provider authority remains in the hosted-services companion.
