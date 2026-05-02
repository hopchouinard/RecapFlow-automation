## Meeting Purpose

[A weekly support call for AI developers to share wins, get feedback, and solve problems.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1309.0)

## Key Takeaways

  - [**Claude Code is the most cost-effective coding assistant.** Its $100/mo plan is cheaper than Cursor, and Brandon is creating a ShipKit cheat sheet to make its UX feel as natural.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1931.0)
  - [**Use Server Actions for internal logic and APIs for external services.** This simplifies development by leveraging Next.js's built-in type safety and authentication, reducing boilerplate.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4711.0)
  - [**To scale a SaaS, first find 2-3 direct customers, then pivot to upstream partners.** This strategy leverages existing distribution channels for exponential growth.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4841.0)
  - [**For complex, multi-step agent workflows, pass the full master prompt to each agent.** This ensures consistent context and better outputs than trying to optimize prompts for individual tasks.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7558.0)

## Topics

### AI Development Tools & Cost-Effectiveness

  - [**Claude Code vs. Cursor:** Claude Code is the most cost-effective coding assistant.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1931.0)
      - [**Cost:** The $100/mo plan is cheaper than Cursor.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1931.0)
      - [**Billing:** Charges per runtime, not per token. This means using faster models like Haiku can increase output for the same cost.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2106.0)
      - [**UX:** Brandon is creating a ShipKit cheat sheet to make Claude Code's UX feel as natural as Cursor's.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2681.0)
  - [**Playwright MCP Servers:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2950.0)
      - [**Benefit:** Pre-built MCPs are faster and more context-friendly than dynamic code generation.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=3197.0)
      - [**Use Case:** They act as reliable tools for development tasks (e.g., scraping, debugging UI) rather than becoming part of the final application.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=3300.0)

### Project Updates & Wins

  - [**Ty's Interactive Presentation Software:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1336.0)
      - [**Progress:** The V1 presentation software is live and has been significantly enhanced since last week.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1336.0)
      - [**New Features:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1389.0)
          - [**Engagement Intelligence:** An opt-in system for collecting audience info.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1389.0)
          - [**Real-time Q\&A:** Questions appear instantly on the presenter's control screen.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1417.0)
          - [**AI Chat:** An AI assistant answers audience questions based on presentation content.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1569.0)
      - [**Goal:** Build a Zoom app to integrate results directly into calls.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=1533.0)
  - [**Paul's SaaS Growth:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2492.0)
      - [**Opportunity:** A major competitor's failure in Australia/New Zealand created a surge of inbound leads.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2507.0)
      - [**Result:** Securing new SaaS contracts \>$10k/mo.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2547.0)
      - [**Action:** Transitioning development to Claude Code to reduce costs (a recent bill was $1,200) and accelerate sales.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2585.0)
  - [**Patrick's AI Platform Launch:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=3858.0)
      - [**Project:** Launching a new internal platform in one week to aggregate 12+ AI tools built over the last 1.5 years.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=3858.0)
      - [**Challenge:** Documenting the entire platform. Patrick will work with Brandon to use ShipKit prompts for this.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4206.0)
      - [**New Idea:** Designing a two-panel AI chat UX with a VS Code-like composer (auto-completion) and a separate response panel.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=3952.0)
  - [**Garron's Real Estate AI:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5152.0)
      - [**Background:** A non-coder with 27 years in real estate, previously built a software company to 2,000 subscribers at $1k/yr.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5281.0)
      - [**Progress:** Using ShipKit and Cursor, Garron completed more work in 1.5 days than in the previous month.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5220.0)
      - [**Goal:** Build an AI platform to support coaching clients with real estate conversation frameworks.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5297.0)

### Strategic Discussions

  - [**SaaS Customer Acquisition:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4841.0)
      - [**Strategy:** Find 2-3 direct customers, then identify and partner with an "upstream" provider who serves many of your target clients.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4909.0)
      - [**Resource:** Dan Martell's "Software as a Science" (Chapters 3-7) was recommended for its sales and marketing pipeline guidance.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2725.0)
  - [**Agent-to-Agent (A2A) Protocols:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=6891.0)
      - [**Status:** Google's A2A protocol is pre-V1.0, causing slow adoption as companies wait for a stable release.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=6937.0)
      - [**Catalyst:** A2A will likely explode when a major player (e.g., OpenAI) adopts it, creating network effects.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7080.0)
      - [**Risk:** A2A could become an invisible utility like HTTP, with value captured by the few who implement it, not the many who use it.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7470.0)
  - [**Complex Agent Workflows:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7558.0)
      - [**Problem:** Generating continuous creative outputs (e.g., video scenes) with a 60-page master prompt.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7558.0)
      - [**Solution:** Pass the full master prompt to each agent, but assign different, sequential tasks.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7558.0)
      - [**Rationale:** This ensures consistent context and better outputs than trying to optimize prompts for individual steps.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=7558.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2681.0)
      - [Record and release the ShipKit cheat sheet for Claude Code.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2681.0)
      - [Create a ShipKit module for sharing custom prompts and agents.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5914.0)
  - [**Paul:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2492.0)
      - [Transition development to Claude Code to manage costs.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2585.0)
      - [Read "Software as a Science" (Ch. 3-7) to accelerate sales.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2725.0)
  - [**Patrick:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4206.0)
      - [Connect with Brandon to use ShipKit prompts for documenting the new AI platform.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4206.0)
  - [**Jake:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4347.0)
      - [Use the "AI dad lawyer" prompt to analyze the complex client contract.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=4495.0)
  - [**Mitch:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2399.0)
      - [Move to Vegas to collaborate with Debris and accelerate the project.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=2399.0)
      - [Test the "full master prompt" strategy for video generation with Manus and Claude Code.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=8112.0)
  - [**Alex (Wilson):**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5962.0)
      - [Connect with Al on LinkedIn regarding potential job opportunities.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=6824.0)
  - [**Garron:**](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5152.0)
      - [Purchase ShipKit to accelerate development of the real estate AI platform.](https://fathom.video/share/j1mCDiihwsQGdMCV9xKjokeDjc_d_6cF?tab=summary&timestamp=5557.0)

