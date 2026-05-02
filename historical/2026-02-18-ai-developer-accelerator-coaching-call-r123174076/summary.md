## Meeting Purpose

[A weekly sync on AI development projects, blockers, and new tools.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=1394.0)

## Key Takeaways

  - [**Productionizing AI:** Use Claude Code for rapid prototyping, then the Claude Agent SDK to convert skills into production-ready agents. For reusable components, package them as NPM modules for easy installation and removal.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4380.0)
  - [**New Tools & Frameworks:** Scott shared a public repo for a mobile Claude Code app, while Ty presented `trylucid.dev`, a tool to detect and fix AI code hallucinations.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3565.0)
  - [**Client Acquisition:** Juan will target enterprise clients by specializing in "Agentic ETL" (enriching data with LLMs) and AI Ops, leveraging his data engineering background.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5100.0)
  - [**Community Value:** The group affirmed the call's high value, citing its open sharing, diverse expertise, and focus on practical application over platform-specific hype.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=7075.0)

## Topics

### Project Updates & Blockers

  - [**Morgan:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2121.0)
      - [**Blocker:** Removing ShipKit from a client repo to share with new resources while preserving personal commit history.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2139.0)
      - [**Solution:** Use a script to create a clean public repo, or package reusable components as NPM modules for easy removal.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2213.0)
  - [**Marc:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2670.0)
      - [**Shipped:** OpenClaw agent on a Google VM.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2673.0)
      - [**Functionality:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=705.0)
          - [`email trainer [name] [email]` → Sends a pre-formatted email with Calendly availability.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=705.0)
          - [`get jobs [title]` → Fetches job listings via API.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=726.0)
      - [**Security Concern:** Patrick warned of prompt injection risk from email access.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=636.0)
  - [**Patrick:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2741.0)
      - [**Shipped:** V6 of a news pipeline with a new admin view.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2741.0)
      - [**Pipeline:** Brave (sources) → Perplexity (enrichment) → Daily brief.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3098.0)
      - [**Admin View:** Manages budget, replays pipeline stages, and tracks article quality feedback to improve future results.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2820.0)
      - [**Origin:** OpenClaw generated the initial scaffolding, which Claude Code then refined.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3120.0)
  - [**Scott:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3565.0)
      - [**Shipped:** `Cloud Code Mobile`, a public repo for a mobile web app.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3570.0)
      - [**Functionality:** Hooks into a Claude Code instance via the Anthropic Agent SDK, enabling mobile access to skills, MCPs, and agents.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3889.0)
      - [**Tech Stack:** Google login, Cloud Console, Cloudflare Tunnel.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3721.0)
  - [**Tom:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4431.0)
      - [**Shipped:** Personal website and CV using Cursor.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4458.0)
      - [**Finding:** Recreated a Next.js nav bar in 480MB with plain HTML/CSS at 15KB, proving that simpler tools can be superior for simple tasks.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4468.0)
      - [**Blocker:** Integrating GoCardless for donations; Stripe's 3% fee is too high for large sums.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4500.0)
  - [**Juan:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4647.0)
      - [**Focus:** Client acquisition for "Agentic ETL" (enriching data with LLMs) and AI Ops (productionizing models on AWS EC2).](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5100.0)
      - [**Strategy:** Create video content and present to local tech groups.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4668.0)
  - [**Ty:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5470.0)
      - [**Shipped:** `trylucid.dev`, a tool to detect and fix AI code hallucinations.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5474.0)
      - [**Status:** Patent pending. Seeking an academic endorser for a research paper.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5820.0)
  - [**Ana:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6090.0)
      - [**Project 1:** Analyzes US Congress stock trades via the Quiver Quants API.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6128.0)
      - [**Goal:** Add an AI chat feature for portfolio analysis.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6399.0)
      - [**Project 2:** "Mindy" meal planner using the "MIND Diet" to optimize grocery spending.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6649.0)

### Strategy & Best Practices

  - [**Client Acquisition:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4647.0)
      - [**Authenticity:** Use a marketing strategy that aligns with your communication style.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4796.0)
      - [**Niche Down:** Specialize in a rare, high-value area (e.g., AI Ops) to attract enterprise clients.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5100.0)
      - [**Brand Voice:** Use AI to create a "voice file" based on your content (e.g., Zoom calls) to ensure consistent, authentic communication.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5274.0)
  - [**Project Structure:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3317.0)
      - [**Dependency Management:** Package reusable components (e.g., ShipKit skills, brand kits) as NPM modules. This isolates them from the main repo and simplifies removal.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3317.0)
      - [**Prototyping → Production:** Prototype rapidly with Claude Code, then convert the stable skills into a production-ready agent using the Claude Agent SDK.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4380.0)
  - [**AI Development:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=567.0)
      - [**Security:** Lock down agent access (e.g., email) to prevent prompt injection.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=636.0)
      - [**Efficiency:** Use simpler tools (e.g., HTML/CSS) over complex frameworks (e.g., Next.js) for simple tasks to reduce bloat.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4468.0)
      - [**Self-Improvement:** Use Claude Code's `/insights` command for a monthly usage analysis and personalized workflow recommendations.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6919.0)

## Next Steps

  - [**Morgan:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2121.0)
      - [Use a script to create a clean public repo, or explore packaging ShipKit skills as NPM modules.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2213.0)
  - [**Marc:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2670.0)
      - [Implement security measures to prevent prompt injection in the OpenClaw agent.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=636.0)
  - [**Ty:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5470.0)
      - [Contact Brandon for an academic connection to endorse the Lucid research paper.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5887.0)
  - [**Juan:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4647.0)
      - [Create video content and presentation materials for the "Agentic ETL" and AI Ops services.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=4668.0)
  - [**Ana:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6090.0)
      - [Explore adding historical performance charts and a portfolio analysis chat feature to the investment project.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6525.0)
      - [Investigate using Apify to scrape grocery prices for the Mindy meal planner.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=6809.0)
  - [**Scott:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=3565.0)
      - [Share the "build a better voice framework" prompt in the chat.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=5317.0)
  - [**Patrick:**](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=2741.0)
      - [Publish the meeting summary with all shared links.](https://fathom.video/share/z-o74XyBT4WHr_Ly8ycAt2ndyJyzvkDH?tab=summary&timestamp=7021.0)

