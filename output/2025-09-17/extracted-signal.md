## general

This was a weekly group coaching call for Brandon Hancock's AI Developer Accelerator program. Brandon opened by demoing ShipKit, his upcoming AI course platform built on a RAG template, which allows students to query course content conversationally and navigate to relevant modules. The platform is scheduled to launch on the 27th after being pushed back from the 20th.

The session followed a round-robin format where each participant shared their current project status and received feedback. Topics ranged from building AI-powered business tools (CRM systems, accounting automation, portfolio builders, RAG applications) to deployment architecture (Google Cloud ADK, Vercel, Supabase), HIPAA compliance costs, UI testing strategies, multi-LLM routing patterns, and personal branding via YouTube. Two first-time attendees, Kris Larson and Elijah, introduced themselves and received onboarding advice.

Brandon also addressed pre-submitted questions on UI testing tools (Cypress, Playwright MCP), multi-model provider strategies (LiteLLM, OpenRouter), and database architecture patterns for applications using multiple sub-services.

## insights

- **Brandon on multi-model routing:** Use the factory design pattern or a routing layer to handle different LLM providers cleanly rather than embedding provider-specific logic throughout business code.
- **Andrew on incremental development:** Building small, isolated working pieces and integrating them is less risky than attempting large monolithic builds, even though integration can still be painful.
- **Brandon on planning vs. execution models:** Use the highest-capability model (e.g., Claude Sonnet with 1M token window) to generate a detailed task blueprint, then "lobotomize" it and hand the plan to a cheaper model for execution. Andrew independently described the same workflow.
- **Ola on multi-model workflow:** ChatGPT Codex (high reasoning mode) is better for planning and systematically reading codebases; Claude is better for fast iteration; GitHub Copilot with Claude 4 acts as a senior reviewer catching errors Claude alone would miss.
- **Brandon on Supabase vs. fragmented services:** Supabase consolidates authentication, Postgres database, vector store, and blob storage in one platform, avoiding the cost and complexity of paying for five separate services (Clerk, Neon, Pinecone, Uploadthing, etc.).
- **Brandon on HIPAA audit logging:** HIPAA requires audit logs (who accessed what, when) far beyond standard development logs — this can cost ~$2,000/month on Azure. Switching log storage to cold storage buckets could significantly reduce costs since audit logs are rarely accessed except during audits.
- **Brandon on Cursor allow-list:** Setting Cursor's auto-run mode to "allow list" prevents the AI from accidentally spinning up duplicate dev server instances or running destructive build commands.
- **Brandon on content strategy for job seekers:** Combining a deep existing skill (e.g., Android development) with AI creates a top-1% niche with very few competitors; consistent weekly content for 3–4 months is the minimum before opportunities materialize.
- **Paul on Claude Projects as a consulting tool:** Building a master prompt persona inside a Claude Project lets you instantly context-switch into a consulting role for any client without re-prompting from scratch each time.
- **Patrick on vibe coding for non-developers:** The hard part of teaching non-developers to vibe-code is not the AI prompting — it's Git hygiene (commit messages, PRs, branching). AI-guided workflows with checkboxes can automate this so users never need to understand Git.
- **Brandon on ShipKit RAG update:** Switched from Cloud Run instances (one machine polling for jobs) to Cloud Run Jobs (each document gets its own ephemeral instance), which is simpler and more scalable.
- **Morgan on RAG for electrical panels:** A QR code linking to a RAG chatbot that answers "which breaker controls X?" is a practical, monetizable use case for commercial buildings with complex electrical systems.

## qa

**Q (Hemal Shah):** Are there any recommendations for automating UI testing using AI?
**A (Brandon Hancock):** Cypress is a solid tool for end-to-end UI testing — have AI generate the Cypress tests. Playwright with an MCP server can also control a browser locally, but it's more expensive to run than Cypress.

**Q (Andrew Nanton):** When using multiple LLM providers, should I use native SDKs for each or a wrapper like LiteLLM?
**A (Brandon Hancock):** LiteLLM is recommended for most cases. For situations requiring native features (e.g., Claude's native PDF handling), consider implementing the factory design pattern to spin up the appropriate provider instance based on request type, rather than embedding conditional logic throughout the codebase.

**Q (Marc Juretus):** For a FastAPI + Supabase setup, is it better to use the Postgres connection string directly rather than the REST API for security?
**A (Brandon Hancock):** Yes — the preferred pattern is to have all sub-applications (web app and Python backend) share a common database rather than calling each other directly. Create a single database service layer with insert/read/update/delete functions. Use Supabase's connection pooler to avoid exhausting database connections.

**Q (Jake Maymar):** What are reasonable monthly infrastructure costs for a HIPAA-compliant Azure-hosted AI chatbot?
**A (Brandon Hancock / Andrew Nanton):** Base infrastructure (servers, database) is roughly $100–$200/month. However, HIPAA audit logging on Azure can run ~$2,000/month — far more than standard dev logging. Switching to cold storage for audit logs (which are rarely accessed) could reduce this significantly. Azure-hosted models (including OpenAI models via Azure) are covered under Microsoft's BAA, so they can be used in HIPAA-compliant architectures.

**Q (Jake Maymar):** Does it make sense to build a simple isolated version of a feature first and then integrate it?
**A (Andrew Nanton):** Yes — incremental complexity is better than attempting everything at once. Writing tests first and running them after each feature addition creates fast feedback loops and catches regressions early.

**Q (Hemal Shah):** For a private internal application, what's the best way to restrict access without a public sign-up flow?
**A (Brandon Hancock):** Disable the sign-up page entirely in your auth provider (e.g., Supabase). Build an admin "Invite User" flow instead — admins enter a name and email, the user receives an invitation email, and only invited users can access the app. NextAuth is also a good option if not using Supabase.

**Q (Hemal Shah):** Is the difference in API endpoints between local ADK (run SSE) and deployed Agent Engine (stream query) a known limitation?
**A (Brandon Hancock):** Yes, and it's a major complaint. Every developer has to build custom dynamic routing between dev and production environments to handle the endpoint mismatch. The workaround is to use stream query in production but wait for the full response and return it synchronously. Brandon is actively pushing Google to fix this.

**Q (Alex Wilson):** Why use Supabase specifically — is the $25/month plan worth it?
**A (Brandon Hancock):** Yes. Supabase provides authentication, Postgres database, vector store, and blob storage in one place for $25/month, supporting up to ~5–10 projects. The main cost watch-out is Point-in-Time Recovery (PITR), which costs $100/month extra; daily backups are included in the base plan.

**Q (Adam):** I'm presenting to local businesses — should I do the human vs. AI creativity comparison idea or something more practical?
**A (Brandon Hancock / Andrew Nanton):** Frame the presentation around what's in it for the audience — give them 5–10 actionable tools they can use immediately after the talk. Brandon shared a slide deck from a June "AI for Local Businesses" presentation that can be reused/adapted.

## tools

- **ShipKit** — Brandon's upcoming AI course platform built on a RAG template; allows conversational querying of course content with links to relevant modules
- **Cypress** — Recommended for end-to-end UI testing; have AI generate the test scripts
- **Playwright (with MCP server)** — Can control a browser locally for UI testing; more expensive than Cypress
- **LiteLLM** — Library for routing requests to multiple LLM providers with a single interface; recommended for multi-model applications
- **Vercel AI SDK** — Used alongside LiteLLM for streaming AI responses in Next.js applications
- **N8N MCP** — N8N released an MCP server that allows building/modifying N8N workflows from a screenshot or natural language description
- **Claude Projects (with Claude Opus)** — Used by Paul to maintain a persistent consulting persona and context for client engagements
- **Supabase** — All-in-one platform for auth, Postgres database, vector store, and blob storage; recommended over fragmented alternatives
- **Neon** — Postgres database alternative to Supabase; mentioned for its more generous free tier (more projects)
- **Google Cloud ADK / Agent Engine** — Brandon's primary agentic framework; has known endpoint mismatch issues between local and deployed environments
- **Google Cloud Run Jobs** — Updated RAG architecture; each document ingestion gets its own ephemeral job instance
- **Datadog** — Centralized log aggregation across multiple cloud services; noted as expensive and having an aggressive sales team
- **ELK Stack** — Open-source alternative to Datadog for log management; appropriate for on-prem or Kubernetes deployments
- **Azure (with BAA)** — HIPAA-compliant cloud platform; covers hosted models under Microsoft's Business Associate Agreement
- **AWS Bedrock** — Mentioned as another HIPAA-compliant option for LLM API calls
- **NextAuth (next-auth)** — Authentication library for Next.js; recommended as an alternative to Supabase Auth for simpler setups
- **Cursor** — AI coding IDE; allow-list mode prevents unwanted auto-execution of commands like `npm run dev`
- **Context7 MCP** — MCP used by Morgan for rubber-ducking with AI on unfamiliar technologies
- **Tailwind CSS v4** — CSS framework; noted as easier to set up than previous versions but has some breaking changes from v3
- **PySide6** — Python GUI framework used by Andrew for local desktop application development
- **Textual / TUI** — Python terminal UI framework Andrew tried before returning to PySide6
- **Electron** — Desktop app framework Andrew attempted but abandoned due to inter-process communication complexity
- **Whisper Flow / Super Whisper** — Voice-to-text tools; Elijah switched from Whisper Flow to Super Whisper on Mac
- **Ollama** — Tool for running local LLM models; Morgan has models running locally, noted as slow on consumer hardware
- **OpenRouter** — Single API key for accessing multiple LLM providers; recommended for model comparison use cases
- **Grok 4** — xAI model; Brandon using it for medium/simple tasks via task documents; free but cannot process images
- **ChatGPT Codex (high reasoning mode)** — Recommended by Ola for planning and systematic codebase analysis before handing off to Claude
- **GitHub Copilot with Claude 4** — Used by Ola as a "senior developer" review layer to catch errors
- **TypeShare** — Example company cited by Brandon where developer partnered with influencer-marketers rather than doing marketing himself
- **ListKit** — Cold email service started by Daniel Frazio, mentioned by Mitch in context of agency AI tools discussion
- **AWS CloudWatch** — AWS native log management; Juan uses custom logging instead to control costs
- **Nano Banana** — AI image generation tool; Paul used it to create a thematic board meeting image from his profile photo
- **Railway** — Deployment platform; Marc planning to use it for LangChain/LangGraph application

## links

- **Brandon's "AI for Local Businesses" slide deck** — Shared in chat during Adam's segment; a reusable presentation template for non-technical business audiences (from June, some content outdated)
- **Miramira (Thinking Machines)** — Open-source project from former OpenAI researchers; allows deterministic LLM outputs using temperature=0 and seed parameters — shared by Jake Maymar
- **N8N MCP release** — Jake Maymar referenced and briefly showed the N8N MCP that builds/modifies workflows from natural language or screenshots
- **Network Chuck videos on N8N + MCP** — Morgan Cook posted two links in chat showing how to build an MCP server in ~5 minutes and integrate it with N8N
- **Daniel Frazio YouTube video** — Mitch recommended a video by the ListKit founder on how AI tools are disrupting agencies; described as good for the business perspective on AI adoption
- **AWS Skill Builder RPG game** — Jake Maymar referenced an AWS gamified learning environment (RPG-style) for teaching cloud concepts; couldn't locate exact link during call

## decisions

- **Brandon Hancock** will push ShipKit launch to the 27th (moved from the 20th) and continue recording modules this week
- **Brandon Hancock** will release a ShipKit preview video the following day (Wednesday)
- **Brandon Hancock** will add guidance on GitIgnore best practices for ShipKit template files in Module 1
- **Brandon Hancock** will continue escalating ADK endpoint inconsistency issues to Google and share updates with the group
- **Kris Larson** committed (public accountability challenge) to record and publish a "welcome to my channel" YouTube video by the following Tuesday, focused on Android + AI development
- **Paul Miller** will prepare a demo of his Claude Projects "second brain" / master prompt methodology to share with the group before his university MBA presentation
- **Paul Miller**, **Mitch**, and **Ty Wells** agreed to connect offline to collaborate on their respective AI-powered CRM/personal assistant approaches
- **Brandon Hancock** will connect Kris Larson and Alex Wilson in the school community given their similar situations (career transition, building portfolios)
- **Adam** will review and adapt Brandon's "AI for Local Businesses" slide deck for his upcoming local business presentation
- **Hemal Shah** will explore NextAuth or Supabase invite-only flow to add authentication to his back-office automation app
- **Andrew Nanton** will investigate cold storage options for HIPAA audit logs on Azure (with Maxim) to reduce the ~$2,000/month logging cost
- **Morgan Cook** will test N8N + Ollama local model integration for an air-gapped project and report back to the group