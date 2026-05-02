## Meeting Purpose

[A roundtable on AI development progress, challenges, and strategic insights.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1668.0)

## Key Takeaways

  - [**AI Agents are a Game-Changer:** OpenClaw (formerly ClawdBot) automates tedious tasks (e.g., invoicing, traffic monitoring) and manages projects end-to-end, freeing developers for higher-value work.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=991.0)
  - [**Security is Paramount:** Agents require strict isolation (dedicated VMs, limited-scope API keys) to prevent unauthorized access and contain potential "blast radius" failures.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3615.0)
  - [**Shift to Value-Based Pricing:** AI's speed makes time-based billing obsolete. The focus must shift to solving business problems, not just writing code.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2880.0)
  - [**Business-First Strategy:** AI's real value is in business discovery and process optimization. Frame solutions around client business goals, not just the technology.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3971.0)

## Topics

### The AI Agent Revolution: OpenClaw

  - [**Core Concept:** OpenClaw is an AI agent framework that automates complex tasks via natural language.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1097.0)
  - [**Key Features:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1211.0)
      - [**Memory:** Stores persona ("soul"), identity, and task-specific context in a SQLite DB.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1211.0)
      - [**Skills:** Can be prompted to build its own tools for specific tasks.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=934.0)
      - [**Communication:** Integrates with platforms like Discord and WhatsApp.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1300.0)
  - [**Use Cases:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=991.0)
      - [**Traffic Monitoring (Patrick):** Gathers real-time Montreal traffic data to predict commute delays and send early-wake alerts.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=991.0)
      - [**Automated Invoicing (Ty):** Replaced FreshBooks by building a custom agent to pull API usage, credit card data, and draft invoices for client approval.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3780.0)
      - [**Project Management (Scott):** Used an early version to build the Clarity app, watching files appear on his laptop as the agent worked.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1481.0)

### Securing and Optimizing Agents

  - [**Primary Concern:** OpenClaw's out-of-the-box security is poor.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3877.0)
  - [**Solution → Strict Isolation:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3615.0)
      - [**Dedicated Identity:** Give the agent its own Gmail, calendar, Google Drive, and GitHub accounts.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3663.0)
      - [**Limited API Keys:** Create keys with strict caps (e.g., $5) to contain potential "blast radius" failures.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3695.0)
      - [**Isolated Environment:** Run on a dedicated VM (Proxmox, AWS) or a hardened local machine.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3615.0)
  - [**Optimization Strategy (Patrick):**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5580.0)
      - [**Discord for Context:** Uses a private Discord server with dedicated channels to keep conversations concise, improving precision and reducing token costs.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5586.0)
      - [**Tiered Model Routing:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5628.0)
          - [**Quen 3 (OpenRouter):** For cheap, day-to-day tasks.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5672.0)
          - [**Kimike 2.5:** For more complex needs.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5672.0)
          - [**Claude Opus:** For hard tasks, called via a headless Claude Code instance to leverage an existing subscription and avoid high API costs.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5640.0)
      - [**Layered Memory:** Plans to add channel-specific memory on top of global memory to further refine context.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5728.0)
      - [**External Tools:** Uses GitHub Projects for task management and Obsidian for a searchable "journal" of the agent's decisions.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5863.0)

### Strategic Implications: Pricing & Client Engagement

  - [**The Problem:** AI's speed makes time-based billing unsustainable. A 30-minute AI fix for 1,000 Jira tickets (Jake) creates a pricing dilemma.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2880.0)
  - [**The Solution → Value-Based Pricing:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2983.0)
      - [**Focus on Business Outcomes:** Shift the conversation from "how long" to "what value" the solution provides.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2983.0)
      - [**Prioritize Business Discovery:** Use AI to accelerate coding, then reinvest that time into deeper business analysis and process optimization (Paul).](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3210.0)
      - [**Understand Client Motivations:** Frame the solution around how it makes the client look good internally (Bastien's point).](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3555.0)

### Project Updates & Technical Challenges

  - [**Marc's Projects:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1716.0)
      - [**Fitness App:** Python/Next.js on Railway with an AI "trainer" (Nice Guy, Motivator, Drill Sergeant) and Groq-generated workout videos.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1772.0)
      - [**Stock School App:** Vercel/Google Cloud app teaching stock basics, then providing $25k in paper money for trading.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1861.0)
  - [**Scott's Clarity App:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2182.0)
      - [**Goal:** A developer tool combining code-base context (GitHub sync) with project management (meeting note analysis, time blocking).](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2255.0)
      - [**Monetization:** Stripe-integrated plans ($20/mo for $13 AI credit, $50/mo for $35 credit) with top-up options.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2393.0)
  - [**Ryan's Projects:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2500.0)
      - [**Social Platform:** Optimized performance by replacing raw images with thumbnails.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2520.0)
      - [**E-commerce Site:** Major project to rebuild a WordPress site, requiring integrations for label printing and the USPS API.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2580.0)
      - [**N8N Cost Reduction:** Scott suggested running a local N8N instance on a VM to avoid high cloud usage costs.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2794.0)
  - [**Morgan's Technical Learnings:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=4852.0)
      - [**Drizzle DB:** Use `prepare: false` in connection strings to prevent silent failures from prepared transactions being lost when the connection pool resets.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=4852.0)
      - [**Vercel/Supabase:** Vercel's IPv4-only support prevents using dedicated Postgres roles for multi-tenancy, forcing a less-secure `postgres` user connection.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=4920.0)
      - [**Sharp Library:** Requires a `vercel.json` file and `package.json` updates to include both Windows and Linux binaries for cross-platform development.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5024.0)

## Next Steps

  - [**Marc:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2018.0)
      - [Investigate OpenClaw for automating stock reports and personal learning apps.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2026.0)
      - [Evaluate Clerk, Auth0, and WorkOS for authentication.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=1949.0)
  - [**Scott:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2182.0)
      - [Continue testing and refining the Clarity app.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2433.0)
      - [Connect with Ryan to discuss N8N deployment options.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2794.0)
  - [**Ryan:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2500.0)
      - [Begin the e-commerce project, focusing on USPS and label printer integrations.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2580.0)
      - [Schedule a call with Scott to discuss local N8N deployment.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2794.0)
  - [**Jake:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2855.0)
      - [Research OpenClaw, prioritizing secure setup and isolation.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3586.0)
      - [Shift client conversations to business outcomes and value.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=2983.0)
  - [**Paul:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3958.0)
      - [Focus on business discovery and process optimization for the new logistics client.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=3971.0)
  - [**Patrick:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5307.0)
      - [Continue formalizing the layered memory and tiered model routing overlay for OpenClaw.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=5580.0)
  - [**Raghav:**](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=6663.0)
      - [Record and transcribe upcoming client meetings.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=6669.0)
      - [Use AI to generate tailored research and analysis prompts.](https://fathom.video/share/Kd19Hd4YThcsA2fSgja_iGx4NKnTsCJc?tab=summary&timestamp=6669.0)

