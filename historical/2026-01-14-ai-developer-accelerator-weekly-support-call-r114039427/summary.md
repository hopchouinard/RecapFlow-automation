## Meeting Purpose

[Weekly support call for AI Developer Accelerator members to share progress and get feedback.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1127.0)

## Key Takeaways

  - [**Brandon's EMS Soap SaaS secured pre-seed funding from TinySeed.** This validates the AI-first approach and highlights the value of a co-founder with deep domain expertise for customer acquisition.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=6571.0)
  - [**Paul built "Territory Compass," a live SaaS app, without writing a single line of code.** He used ShipKit and Claude Code to optimize sales routes, proving that AI can enable non-developers to build complex, production-ready products.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3074.0)
  - [**Google's `text-embedding-001` model deprecates Jan 14.** Brandon will provide a migration guide for existing ShipKit RAG projects; new projects should wait \~1 day for the updated template.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1147.0)
  - [**A key workflow emerged for building reliable AI systems:** first, create detailed specs by having the AI help define its own optimal documentation format. Then, use a scratch file to identify and convert reusable prompts into skills.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3877.0)

## Topics

### Brandon's Updates: EMS Soap & ShipKit

  - [**EMS Soap Funding:** Secured pre-seed funding from TinySeed, enabling Brandon to go full-time.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=6571.0)
      - [**Product:** AI-powered medical billing for ambulance/fire departments, increasing insurance reimbursement rates.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=6680.0)
      - [**Co-founder:** Raul, a chief in a major county, provides an "unfair advantage" for customer acquisition.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=7328.0)
      - [**Partnership:** 50/50 equity split, based on mutual commitment and hard conversations upfront.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=7233.0)
  - [**ShipKit RAG Migration:** A guide and video will be provided to migrate from the deprecated `text-embedding-001` model to `text-embedding-002`.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1147.0)
  - [**Marketing with Claude Code:** Successfully used Claude Code to build a Google Ads campaign with custom funnels and landing pages for different customer avatars.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1045.0)

### Paul's "Territory Compass" SaaS

  - [**Project:** A live SaaS app for optimizing sales routes (traveling salesperson problem).](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3074.0)
  - [**Key Insight:** Built the entire app without writing code, using Claude Code and ShipKit.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3354.0)
      - [**Tech Stack:** Clerk (auth), DocPloy (VPS/Docker swarm), Vroom/OR Tools (optimization APIs).](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3282.0)
  - [**Features:**](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3074.0)
      - [Optimizes routes by visit priority, revenue, or frequency.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3150.0)
      - [Allows map-based territory management (e.g., moving stores between territories).](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3189.0)
      - [Includes an AI-powered help center that pulls updates from GitHub and translates them into customer-friendly release notes.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3232.0)

### Patrick's "Agent Army" for Infrastructure Automation

  - [**Goal:** Build a "Cloud engineer" agent to automate home lab infrastructure management.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3840.0)
  - [**Workflow:**](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3930.0)
    1.  [**Scrape Vendor Docs:** Create a web scraper for hardware documentation (e.g., Ubiquiti).](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3930.0)
    2.  [**Optimize Docs for AI:** Use the AI to define a documentation schema that it can easily consume.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3941.0)
    3.  [**Build Skills:** Create skills for specific hardware (e.g., Ubiquiti Dream Machine).](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=4023.0)
    4.  [**Orchestrate with Agent:** A main agent calls skills, which use MCPs (minimal client libraries) to interact with APIs.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=4047.0)
  - [**Security:** The agent cannot make modifications directly; it must call a skill, which uses an MCP. This creates a clear separation of concerns.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=4064.0)
  - [**Self-Documentation:** The agent's rules require it to document all changes in its own optimized format before considering a task complete.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=4080.0)

### Alex's Studio Booking App & Latency Fixes

  - [**Project:** A studio/rehearsal space booking app built with ShipKit for a client.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=11636.0)
  - [**Problem:** The webhook for WhatsApp, Instagram, and Messenger has a 1-2 second latency.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=11804.0)
  - [**Solution:** Eliminate caching for real-time data and use parallel API calls (`Promise.all`) to fetch data simultaneously.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=11820.0)
  - [**Model Recommendation (via OpenRouter):**](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=11842.0)
      - [**Gemini 2.5 Flash:** High throughput, low latency.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=12190.0)
      - [**Gemini 3 Flash:** Higher throughput for longer responses.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=12110.0)
      - [**GPT-4o:** Good balance of latency and quality.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=11957.0)
  - [**Lead Gen Strategy:** Use the completed app as a portfolio piece to create personalized Loom videos for other local businesses, highlighting their current site's friction and demonstrating the new app's value.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=12377.0)

### Other Project Updates

  - [**Morgan:** Using Patrick's skills for code review; exploring Lemon Squeezy for one-off product sales.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1189.0)
  - [**Marc:** Building "Marc's World" for personal automation (YouTube summaries, TV monitoring, energy rate tracking). The energy rate tracker was identified as a strong product idea.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1870.0)
  - [**Juan:** ETL agent for extracting vendor names from general ledgers achieved \>99% accuracy, exceeding the 95% industry standard.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=6117.0)
  - [**Maksym:** Automotive SaaS is used by \~25% of the Mexican market; planning expansion to the US/Canada.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=7501.0)
  - [**Alexander:** Building a music creation Telegram bot integrating FL Studio, Suno AI, and GPT.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=7901.0)
  - [**Ivan:** Building "Symposium," a video conferencing app to bypass government protocol-level blocking.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=8311.0)
  - [**Bastian:** Agent now uses Perplexity and Exa for web search; using GLM 4.7 as a cost-effective companion model.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=8745.0)
  - [**Ryan:** Screenly digital signage app is nearly complete; building a large AI content generation machine for a client.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=9249.0)
  - [**Scott:** Proposed a $55k construction estimator tool; shared a "Prompt Optimizer" to improve Claude Code results.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=10878.0)
  - [**Ty:** Building "Engram," a personal dashboard to track activity across 25 projects, identify synergies, and manage credentials.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=12589.0)

## Next Steps

  - [**Brandon:**](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1147.0)
      - [Record and distribute the ShipKit RAG migration video/guide.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=1147.0)
      - [Notify the community when the updated RAG template is merged.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=5110.0)
      - [Explore hosting monthly community calls.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=2319.0)
  - [**Paul:** Share the help center agent/skill from "Territory Compass" with the community.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=3526.0)
  - [**Marc:** Demo the energy rate tracker at the next call.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=2109.0)
  - [**Alex:** Test Gemini 2.5/3 Flash and parallel API calls to reduce latency.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=11820.0)
  - [**Ty:** Research and share info on bypassing protocol-level internet blocking.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=8311.0)
  - [**All:**](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=5808.0)
      - [Consider using a scratch file to identify reusable prompts for skills.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=5808.0)
      - [Use the "Shipkit Mentor" custom GPT to select the correct starting template.](https://fathom.video/share/aJgwY9RExzBBoxMNFRroLe9FiadRR6ds?tab=summary&timestamp=10479.0)

