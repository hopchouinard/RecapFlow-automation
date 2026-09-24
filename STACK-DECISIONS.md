# Stack decisions

What *this* project chose, and why it differs from the personal standard where it does.
The standard itself lives in the `tech-stack` skill; this file records only the
project-specific outcome.

- **Standards version:** `0.1.0`
- **Adopted:** `2026-09-10`
- **Profile:** Internal home-lab app (Community Brain standalone migration)

## Composition

Fill in as the project takes shape. Cite the decision ID for anything that came
straight from the standard.

| Concern | Choice | Basis |
| --- | --- | --- |
| Language | | |
| Framework | | |
| Persistence | | |
| Auth | | |
| Hosting | | |
| Testing | | |
| Verification command | `scripts/verify-forge.sh` | HS-06 |
| Automatic stage scheduling | Linux cron invokes a nonoverlapping selected-stage launcher; PostgreSQL/JetStream retain durable work | BE-25, BE-24 |

## Provisional choices (Deferred families)

Families the standard has not locked, that this project had to resolve anyway.
These are **provisional and project-scoped** — they do not set the default for
other projects. If the same choice recurs across projects, that is the signal to
promote it into the standard.

| ID | Family | Choice | Rationale | Date |
| --- | --- | --- | --- | --- |
| FE-specialized-01 | Specialized UI (provisional) | react-markdown + remark-gfm | Render CommonMark/GFM previews as React elements, including tables and task lists; keep raw HTML disabled and original download bytes unchanged. Project-local choice. | 2026-09-10 |

## Exceptions taken

Departures from a locked decision. Each needs a concrete, expressible reason.

### None yet

<!-- Copy this block per exception:

### <ID> — <short title>

- **Departs from:** <decision ID and what it requires>
- **Problem:** <what the standard does not solve here>
- **Evidence:** <measurement, constraint, or requirement — not a hunch>
- **Scope:** <what this affects>
- **Maintenance implications:** <ongoing cost, migration path back>
- **Date:** <YYYY-MM-DD>

-->

## Open questions

Stack questions this project has not answered yet.

-

Markdown renderer references: [react-markdown](https://github.com/remarkjs/react-markdown), [remark-gfm](https://github.com/remarkjs/remark-gfm). Remote images are shown as text labels to avoid fetching external content merely by previewing a private file.

### Patchoutech Signal visual adaptation (2026-09-10)

Project design choice: adapt Patrick's verified Patchoutech Design System reference
(request CBM-DESIGN-20260910-013) to the existing internal React workspace using
CSS tokens, cyan/ember atmosphere and glass panels. Light mode is a project-specific
companion to the reference's dark-first direction. No framework or dependency
changes; supplied reference scripts and Google Fonts imports are not included.
The named typography stacks use system fallbacks until font binaries are bundled.
See [design review](docs/migrations/cbm-signal-design-review.md). This changes no
universal technology defaults. Patrick approved the previews and rollout; request014
tracks deployment.
