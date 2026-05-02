## Meeting Purpose

[A weekly support call for AI developers to share progress, ask questions, and collaborate.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1074.0)

## Key Takeaways

  - [**Agent Engine is unreliable; use Cloud Run.** Google's own documentation now recommends Cloud Run for deploying Agent Development Kit (ADK) agents, as Agent Engine has broken features (e.g., server-side events) and is not actively maintained.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1556.0)
  - [**Partner with sales trainers for a project funnel.** Sales trainers have direct access to clients with immediate, funded AI project needs, providing a reliable source of work for developers.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3711.0)
  - [**Build a public portfolio to get clients.** The most effective way to land freelance work is by creating a public portfolio (e.g., YouTube videos) that demonstrates skills and builds trust, solving the "no one knows you exist" problem.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5944.0)
  - [**ShipKit roadmap prioritizes core templates.** Brandon is sprinting to deliver the `worker-sass` and `base-template` by Nov 16, followed by walkthroughs for an AI video platform. A GitHub management module is a 2026 priority.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2797.0)

## Topics

### ShipKit Roadmap & Community Initiatives

  - [**Roadmap:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2797.0)
      - [**Nov 16:** Deliver `worker-sass` and `base-template`.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2797.0)
      - [**Post-Nov 16:** Create walkthroughs for the new templates, including:](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2797.0)
          - [Using Trigger.dev for background tasks (transcription, chunking).](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2827.0)
          - [Implementing real-time subscription data.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2827.0)
          - [Building a basic AI video shorts generator.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2854.0)
  - [**Community Initiatives:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2754.0)
      - [**GitHub Management Module:** Patrick proposed a module to enforce corporate-level code hygiene (PRs, commits) for "vibe coding." Brandon agreed, noting it's a 2026 priority.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2754.0)
      - [**Discord Knowledge Base:** Patrick suggested using the ShipKit Discord as a knowledge base for agents. Brandon will integrate it into the main vector store and create an MCP for in-editor queries.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2912.0)
      - [**Email Automation Video:** Brandon will record a video on using Claude Code/Cursor with Gmail (via MCP) to automate email responses.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1191.0)

### Project & Workflow Deep Dives

  - [**Ty's Personal Knowledge Base:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1691.0)
      - [**Goal:** Create a "system of record" by consolidating personal knowledge to identify synergies.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1691.0)
      - [**Sources:** Limitless device recordings, 113 GitHub repos, and scraped video content (via Appify).](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1691.0)
      - [**Control:** A Telegram bot for issuing commands and approving agent actions.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2038.0)
  - [**Mitch's AI Video Generation Workflow:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4865.0)
      - [**Goal:** Generate monetized AI shorts (e.g., "body cam stories").](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4965.0)
      - [**Tech Stack:** n8n, Supabase, Dropbox, Sora/Ki AI.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4924.0)
      - [**Process:** User input → n8n workflow → Supabase row & Dropbox folder → Ki AI generation.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4924.0)
      - [**Key Learning:** Use simple code snippets for data parsing (e.g., finding text between markers) instead of relying on LLMs, which struggle with large, structured inputs.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4865.0)
  - [**Jake's User Simulation & Stress Testing:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4088.0)
      - [**Problem:** Simulate users on a forum to find bugs and stress-test an app.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4088.0)
      - [**Solution:** Use Cypress for end-to-end testing and Playwright for concurrent user simulation.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4140.0)
      - [**Monitoring:** Supabase's built-in metrics (requests, response times, DB connections) to track load.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4463.0)
      - [**Observability:** Agent Ops was recommended for tracking AI calls, but Jake will defer to save costs.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4560.0)

### Developer Growth & Business Strategy

  - [**Tiberius's Freelance Strategy:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5788.0)
      - [**Problem:** A non-coder using AI to build projects (TypeScript, Supabase) struggles to find clients.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5797.0)
      - [**Solution:** Brandon advised creating a public portfolio (e.g., YouTube) to demonstrate skills and build trust, solving the "no one knows you exist" problem.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5944.0)
  - [**Paul's Partnership Strategy:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3711.0)
      - [**Insight:** Partnering with sales trainers provides a direct pipeline to clients with funded, immediate AI project needs.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3711.0)
      - [**Rationale:** This allows developers to focus on product delivery while the partner handles sales.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3942.0)
  - [**Mitch's Interview Portfolio:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4682.0)
      - [**Insight:** A structured portfolio of SOPs and reference docs for specific tasks (e.g., Amazon SEO) is highly effective in interviews, demonstrating deep expertise and leadership potential.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=4682.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2797.0)
      - [Deliver `worker-sass` and `base-template` by Nov 16.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2797.0)
      - [Record the email automation video.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=1191.0)
      - [Integrate the ShipKit Discord into the vector store and create an MCP.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2912.0)
  - [**Patrick:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=2751.0)
      - [Share custom GPT files in Discord.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3021.0)
      - [Publish blog posts on Gemini CLI and Agent HQ.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3120.0)
  - [**Mitch:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5125.0)
      - [Connect with Elijah on School to discuss the AI video workflow.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5125.0)
  - [**Tiberius:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=5785.0)
      - [Review Brandon's video on building a personal brand.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=6221.0)
  - [**All:**](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3500.0)
      - [Explore 21stDev for UI inspiration and code snippets.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3500.0)
      - [Consider partnering with sales trainers to find project opportunities.](https://fathom.video/share/uhtqA-SMyVeReczVnHHrJuEByzYuRf5z?tab=summary&timestamp=3711.0)

