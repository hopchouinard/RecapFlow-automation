## Meeting Purpose

[Weekly support call for AI developers to share wins and get technical help.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=948.0)

## Key Takeaways

  - [**New Tools for AI Devs:** `SpecStory` (VS Code extension) saves AI chat logs to Markdown, enabling AI-driven documentation and course creation. `Warp Drive` syncs terminal sessions to a cloud disk for persistent knowledge bases.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=629.0)
  - [**AI-Powered Productized Services:** Ryan is building an AI app to scale his social media management service from 2–3 to 20–30 clients, using Claude and Zapier to automate content creation and approvals.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5323.0)
  - [**Future of UI/UX:** Glenn Marcus (Click Consulting) predicts traditional UIs will be replaced by AgentOS and contextual widgets within 5 years, prompting a pivot from mobile development to AI agents and backends.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=3573.0)
  - [**Enterprise AI Security:** For corporate systems like ERPs, use `Claude for Financial Services` for its built-in audit trails and data isolation. Start with read-only permissions and use sandboxes like `E2B` to mitigate risk.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=7663.0)

## Topics

### New Tools & Workflows

  - [**`SpecStory` Extension:** A VS Code extension that saves AI chat logs to Markdown.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=629.0)
      - [**Use Case:** Patrick Chouinard used it to export a `SpecKit` project's chat log, then fed the log to Claude 4.5 to generate training materials on spec-driven development.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=686.0)
  - [**`Warp Drive` Feature:** A cloud disk that syncs terminal sessions, creating a persistent, collaborative knowledge base for AI agents.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=2927.0)
  - [**`Kaiya` Project:** Ty Wells is building a personal assistant (`Jessica`) using Daniel Miser's `Kaiya` project structure to automate tasks.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=755.0)

### AI-Powered Projects & Services

  - [**`ShipKit Studio` (Ty Wells):** A web GUI for the `ShipKit` CLI, built using `ShipKit`.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=1884.0)
      - [**Features:** Logo generation (DALL-E), wireframe editing, and a database schema builder.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=1854.0)
      - [**Goal:** Automate live app deployment to `E2B` from the GUI.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=1980.0)
  - [**Daily Briefing Agent (Patrick Chouinard):** A ground-up build using Gemini CLI.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=458.0)
      - [**Workflow:** Parallel search agents → `Analyze` agent synthesizes results → `Create Dashboard` agent generates HTML.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=1568.0)
      - [**Next Step:** Use Cloud Code to build the web scaffolding (Supabase backend, navigation) around the pre-built prompt logic.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=1542.0)
  - [**Social Media Automation (Ryan):** Building an AI app to scale a productized service.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5323.0)
      - [**Goal:** Manage 20–30 clients (vs. 2–3) at £700–£1000/mo.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5470.0)
      - [**Tech:** Claude and Zapier for content generation and client approvals.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5323.0)

### Strategic Pivots & Future Trends

  - [**Glenn Marcus (Click Consulting):** Pivoting from mobile development to AI.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=3573.0)
      - [**Rationale:** Predicts traditional UIs will be replaced by AgentOS and contextual widgets within 5 years.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=3573.0)
  - [**Brandon Hancock:** Stressed the importance of building public "awareness" (e.g., via YouTube) to maintain market value during industry shifts.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=3840.0)

### Technical Deep Dives

  - [**Large-Scale Real Estate Data (Lan):**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5882.0)
      - [**Problem:** Analyzing 50M+ annual MLS records for market trends.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5882.0)
      - [**Initial Analysis:** Use Excel/Copilot for small datasets. For large files, use Python's `pandas` library.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=6429.0)
      - [**Production Architecture:** `Postgres` with the `PostGIS` extension for efficient geospatial queries.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=6832.0)
  - [**Enterprise AI & Security (David):**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=7080.0)
      - [**Problem:** Connecting AI agents to corporate ERPs (NetSuite, QuickBooks).](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=7388.0)
      - [**Solution:** Use `Claude for Financial Services` for its built-in audit trails and data isolation. Start with read-only permissions and use sandboxes like `E2B` to mitigate risk.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=7663.0)
  - [**PostHog Analytics (Prem):**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=4020.0)
      - [**Problem:** Filtering out local development traffic from analytics.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=4020.0)
      - [**Solution:** Use one PostHog project and filter dashboards by URL (e.g., `current URL does not contain "localhost"`).](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=4020.0)

## Next Steps

  - [**Brandon Hancock:**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=957.0)
      - [Publish YouTube video on developer resources.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=957.0)
      - [Fix missing "Generate Transcript Deep Dive" video.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=3967.0)
  - [**Patrick Chouinard:**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=2471.0)
      - [Share `ShipKit Studio` with the community repo.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=2471.0)
  - [**Scott Rippey:**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=4428.0)
      - [Post "Skills vs. MCPs" article to the Discord community.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=4428.0)
  - [**Ryan:**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5278.0)
      - [Review resources on productized services and the Gemini API.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5525.0)
  - [**Lan:**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=5882.0)
      - [Explore `Postgres` with `PostGIS` for the real estate project.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=6832.0)
  - [**David:**](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=7030.0)
      - [Investigate `Claude for Financial Services` for enterprise use cases.](https://fathom.video/share/6H_FPkBdX6C5Y1R6pLLndimszF8NFEGS?tab=summary&timestamp=7797.0)

