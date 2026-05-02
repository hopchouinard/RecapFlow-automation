## general

This was a group coaching/community call hosted by Brandon Hancock for members of the ShipKit community — a SaaS starter kit and developer education platform. The session followed a round-robin format where participants shared what they were working on, asked questions, and received feedback. Attendees included Patrick Chouinard, Marc Juretus, Ana P, Ty Wells, Paul Miller, Morgan Cook, Alex Wilson, Jake Maymar, Mitch, Elijah, Tiberius K, and others.

Topics ranged widely: vibe coding governance challenges in enterprise settings, Google ADK and Agent Engine deployment issues, personal knowledge management systems, AI video generation workflows, Clerk payment integration, end-to-end testing strategies, Supabase load monitoring, and strategies for developers to find freelance work. Brandon also previewed upcoming ShipKit roadmap items including a Worker SaaS template, a base template, and an AI video walkthrough.

Patrick Chouinard raised two feature requests for ShipKit: adding Git workflow management (branching, PRs, commit hygiene) to support enterprise adoption, and creating a Discord MCP so developers could query the ShipKit knowledge base directly from their coding agents. Brandon responded positively to both ideas and outlined how a shared vector store could power the latter.

The call closed with Ty Wells sharing a personal TikTok-style memorial photo/video app he built for his late father-in-law, which prompted discussion about AI biography tools and the emotional applications of these technologies.

---

## insights

- **Vibe coding creates governance gaps**: When everyone in an organization can generate code, no one is managing PRs, branching, merging, or commit hygiene. A management layer (e.g., GitHub's Agent HQ / Mission Control) is needed to enforce code hygiene at scale. *(Patrick Chouinard)*
- **GitHub may capture significant market share** by offering a single pane of glass to manage multiple coding agents (Claude Code, Gemini CLI, Copilot CLI, Cursor). *(Patrick Chouinard)*
- **Google Agent Engine has significant bugs**: The stream query function doesn't work properly with server-sent events when using ADK. Google itself now recommends deploying agents via Cloud Run instead of Agent Engine. *(Brandon Hancock)*
- **AI is a better learning tool than Udemy for project-based learning**: You can learn on the way while building a specific project, rather than consuming generic courses. *(Marc Juretus)*
- **Parallel web searches with Gemini CLI are simple to implement**: Use a headless Gemini CLI call with a bash loop iterating over a list of query variables (e.g., from a spreadsheet). *(Patrick Chouinard)*
- **The ShipKit Discord is an untapped knowledge base**: Feeding Discord Q&A into a vector store and exposing it as an MCP would let developers query institutional knowledge directly from their coding agents. *(Patrick Chouinard / Brandon Hancock)*
- **Shiny object syndrome is a real productivity killer for developers**: Unless a new tool is a 10x improvement, sticking with what works is usually the right call. *(Brandon Hancock)*
- **Partnering with a domain expert (e.g., a sales trainer) rather than another developer** creates a powerful funnel: the partner surfaces client needs and sells; the developer builds. *(Paul Miller)*
- **The biggest problem for developers is visibility, not skill**: Even the world's best programmer gets zero opportunities if no one knows they exist. YouTube is the recommended solution. *(Brandon Hancock)*
- **YouTube content compounds into a portfolio and trust signal**: Clients and partners can verify competence before engaging, eliminating friction in sales and partnerships. *(Brandon Hancock)*
- **LLMs can overcomplicate parsing tasks**: A simple code snippet (e.g., find "Clip 1," trim to "Clip 2") often outperforms prompting an LLM to parse structured data. *(Mitch)*
- **When stress-testing an app, focus on two failure modes**: database connection limits under load, and infinite re-render loops caused by poorly managed useEffect/state. *(Brandon Hancock)*
- **Supabase has built-in observability**: Connection counts, response times, and request volumes are visible in the dashboard — useful for knowing when to upgrade your instance tier. *(Brandon Hancock)*
- **Upgrading a Supabase instance causes ~5 minutes of downtime**: Plan upgrades for off-hours or before a project launches. *(Brandon Hancock)*

---

## qa

**Q (Mitch):** Are there good replacements for agent kit or prompt chaining?
**A (Brandon Hancock):** Trigger.dev is the current recommendation. It lets you chain tasks sequentially — task one runs prompt one, task two runs prompt two — and provides a run log to monitor activity. It doesn't have a graphical node-based UI like N8N or Make, but you can generate a Mermaid diagram and export it to Eraser or Excalidraw for visualization.

**Q (Mitch):** Does Trigger.dev have a UI similar to N8N nodes for non-technical users?
**A (Brandon Hancock):** No, it's log-based rather than graphical. For visualization, generate a Mermaid diagram from your workflow and export it to a tool like Eraser or Excalidraw.

**Q (Ana P):** Is it best practice to send requests directly to a deployed agent on Agent Engine, or to use an intermediary app?
**A (Brandon Hancock):** An intermediary app is correct in principle, but Agent Engine itself has significant bugs right now — the stream query function doesn't work properly with server-sent events. Google now recommends deploying via Cloud Run instead, where you expose the ADK API directly. Save yourself the headache and skip Agent Engine for now.

**Q (Morgan Cook):** How do you remove unused template features that were part of the original ShipKit template?
**A (Brandon Hancock):** Use the cleanup markdown file and tell the AI agent which features you no longer need (e.g., "I don't use chat anymore, drop all the chat code"). It will generate a comprehensive task to remove everything related to that feature.

**Q (Morgan Cook):** What do you think of Clerk's new payment integration backed by Stripe?
**A (Brandon Hancock):** Interesting, but I'd want to see it in action. The current ShipKit approach just stores a Stripe customer ID and redirects users to Stripe for all payment management. Clerk's integration sounds like it adds components and possibly a subscriptions table, but I'm curious what else it actually simplifies. It's subscription-only for now (no one-time payments), which is a limitation. Worth watching but not necessarily a 10x improvement yet.

**Q (Jake Maymar):** I want to simulate multiple users interacting on a forum simultaneously — is there a platform or obvious approach for this?
**A (Brandon Hancock):** Use Cypress for end-to-end testing. A good workflow: manually perform the actions using Playwright (which records your interactions), then have AI convert that recording into a Cypress end-to-end test. For concurrent users, the two most likely failure modes to test for are database connection limits under load and infinite re-render loops from poorly managed state/useEffect.

**Q (Jake Maymar):** What about AI/RAG observability — is there anything in Supabase for that?
**A (Brandon Hancock):** Supabase covers database-level observability (connections, response times, request volume). For AI/agent observability, Agent Ops is the preferred tool — it tracks query duration, question content, and supports evals. It's about $40/month, so it's worth adding once you're past the lean startup phase.

**Q (Tiberius K):** I have no coding background, I've built things with AI through VS Code, and I'm getting crickets on LinkedIn outreach to real estate agents. How do I get freelance work?
**A (Brandon Hancock):** The core problem is visibility — no one knows you exist. LinkedIn cold outreach for a specific solution rarely works unless the prospect needs exactly that thing at exactly that moment. The recommended approach: pick three areas where you have an unfair advantage, then create YouTube content teaching people how to achieve a transformation in those areas. Give away your automations for free on video — people see what you can do and come to you asking for related work. Three months of consistent content typically flips the switch from no inbound to too much work.

---

## tools

- **ShipKit** — SaaS starter kit template being built and discussed throughout; central product of the community
- **GitHub Copilot** — Patrick training 50 employees on it; discussed as enterprise AI coding tool
- **Claude Code** — Paul switched from Cursor to Claude Code; Brandon uses it for email management and project work
- **Cursor** — Mentioned as prior tool Paul moved away from; Brandon using it alongside Claude Code for email workflows
- **Gemini CLI** — Patrick using it headlessly as a parallel search agent; Brandon wants to use it for multi-city data lookups
- **GitHub Agent HQ / Mission Control** — New GitHub release Patrick is writing about; orchestrates multiple coding agents with spec-driven development
- **Trigger.dev** — Recommended for background task chaining and prompt chaining as an alternative to agent kit
- **N8N** — Mentioned as a graphical workflow tool with node-based UI; Mitch built Sora video generation workflows in it
- **Agent Engine (Google)** — Ana deployed an agent here; Brandon flagged significant bugs and recommended Cloud Run instead
- **ADK (Agent Development Kit)** — Google's toolkit for building agents; Ana used it; stream query function broken with Agent Engine
- **Cloud Run (Google)** — Recommended deployment target for ADK agents instead of Agent Engine
- **Vertex AI** — Ana mentioned its SDK/API for making requests to deployed agents
- **Flask** — Ana building a Flask app as a UI layer for her agent, to be deployed on Cloud Run
- **Limitless device** — Ty's AI recording wearable that logs daily activity and generates insights
- **Memento (repo)** — Open-source project Ty found that builds on Limitless API for knowledge management; MCP didn't work for him
- **Apify** — Ty using it to scrape YouTube video content for his knowledge base system
- **Telegram** — Ty using it as a conversational interface to trigger and approve agent actions
- **Sora (OpenAI)** — Mitch using it for AI video generation; can't use real people's faces
- **Kling / Kei AI** — Mentioned as ~6x cheaper alternative to Sora for video generation
- **VO / VO 3 / VO 3.1 (Google)** — Video generation model; supports using an image as a starting frame, unlike Sora
- **Looker Studio** — Mitch using it (free, Google product) to visualize Amazon data with query-driven dashboards; distinct from the expensive enterprise Looker product
- **Cypress** — Recommended for end-to-end and concurrent user testing
- **Playwright** — Suggested for recording manual interactions to convert into Cypress tests
- **Sentry** — Mentioned for error detection and monitoring in production
- **Agent Ops** — Recommended for AI/agent observability; tracks query duration, content, supports evals; ~$40/month
- **Supabase** — Used by multiple members; Brandon showed built-in dashboard for monitoring connections and response times
- **Clerk** — Morgan raised Clerk's new Stripe-backed payment integration; subscription-only currently
- **Stripe** — Backend payment processor; used directly in ShipKit; also backs Clerk's new payment feature
- **21stDev** — UI component library Brandon discovered; provides source code and AI-editor-ready copy prompts for components
- **Mobbin** — UI inspiration tool Paul mentioned; provides PNG screenshots of real app UIs (no source code)
- **Eraser / Excalidraw** — Mentioned as export targets for Mermaid diagrams to visualize workflows
- **Meta glasses (smart glasses)** — Brandon speculated about building a voice-to-agent interface on upcoming Meta glasses app store
- **Otto Writes** — AI personal biographer app built by a developer Brandon follows on X; shared in context of Ty's memorial app idea
- **Dropbox** — Mitch using it to organize generated video clip folders in his N8N workflow
- **Looker (enterprise)** — Mentioned only to distinguish it from the free Looker Studio; noted as "many thousands of dollars a month"

---

## links

- **Patrick's custom GPT** — Posted in ShipKit Discord show-and-tell; Patrick received permission to share the associated files in Discord
- **Mitch's YouTube video on AI image/soap product photography workflow** — Mitch offered to drop the link in chat; covers how to generate product images using AI tools
- **Brandon's YouTube video on building a personal brand as a developer** — Shared in chat during Tiberius discussion; described as a deeper dive into the visibility/YouTube strategy
- **Otto Writes (X / Twitter profile)** — Brandon shared the link in chat; AI personal biographer app by a developer Brandon follows

---

## decisions

- **Patrick Chouinard** will share the custom GPT files in the ShipKit Discord server (Brandon approved)
- **Patrick Chouinard** will publish a blog article on using Gemini CLI as a search agent
- **Patrick Chouinard** will publish a blog article connecting GitHub's Agent HQ / Mission Control with spec-driven development using ShipKit
- **Brandon Hancock** will record a video this week demonstrating Gmail + MCP with Claude Code/Cursor for email management, and share the ghostwriter files with the community
- **Brandon Hancock** will sprint to finish the Worker SaaS template and base SaaS template by approximately the 16th
- **Brandon Hancock** will record a walkthrough showing how to transform the Worker SaaS into an AI video/shorts generator platform
- **Brandon Hancock** will explore building a ShipKit MCP backed by a vector store fed by Discord Q&A and course content, so members can query it from their coding agents
- **Brandon Hancock** will look into the smart glasses David recommended in chat
- **Brandon Hancock** will contact Patrick to discuss using headless Gemini CLI for parallel multi-city data lookups
- **Mitch and Brandon Hancock** agreed to collaborate on creating AI-generated ShipKit promotional shorts using public Twitter posts as triggers
- **Mitch** will connect with Elijah via School to discuss the N8N Sora video generation workflow for Elijah's franchise content client
- **Ty Wells** will look into Apify MCPs to add additional data sources to his personal knowledge management system
- **Brandon Hancock** will share the Otto Writes link with Ty Wells for the memorial/biography app concept