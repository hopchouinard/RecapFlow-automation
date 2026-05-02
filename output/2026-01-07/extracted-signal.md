## general

This was a group coaching call for members of the ShipKit community, hosted by Brandon Hancock. The session opened with casual conversation about AI deepfakes and cybersecurity fraud before transitioning into a series of member project updates and demos. Brandon shared major news: his startup EMS Soap, which helps EMTs generate SOAP reports for insurance billing, had received funding from TinySeed — less than 12 months after he left Crew AI. He also announced he had converted to using Git work trees for parallel feature development and planned to record a ShipKit module on the topic.

The bulk of the session consisted of members presenting their projects. Ty Wells demonstrated a machine learning platform for small businesses enabling predictive analytics (customer churn, etc.) from POS data. HP (Scott) showed a live call coaching Chrome extension using Deepgram for real-time speech-to-text and Supabase edge functions. Ryan (One Stop Creative Agency) demoed "Screenly," a fully branded digital signage SaaS with a node-based flow builder, estate agent QR lead generation, and a custom Windows kiosk package. Tiran Dagan walked through a preparedness/emergency planning platform with complex inventory management, an async workflow microservice he built as an alternative to Trigger.dev, and PlantUML diagram generation. Garron Selliken described a successful collaboration workflow with a developer (Prem) using Claude Code and Google AI Studio to build a real estate CRM. Bastian Venegas Arevalo demoed a CLI-based general-purpose agentic orchestrator built in Elixir with SQLite, using GLM 4.7 and EXA for web search. Dmitry Avramenko presented his agentic orchestrator platform featuring named agents (Raj, Sarah, Maya, George) with voice interfaces, token usage tracking dashboards, and a live production incident management demo.

The call also covered technical discussions on Git work trees, framework choices (Next.js vs. Vite vs. Astro), model selection (Gemini 3 Flash Preview on low thinking vs. GPT-4.1), agent frameworks (LangChain, LangGraph, Crew AI falling out of favor), YouTube transcript scraping challenges, deployment platforms (Railway vs. Render), and pricing strategy for AI-accelerated development work.

## insights

- **Brandon Hancock:** The same RAG template applied to different problems is worth vastly different amounts of money — the ShipKit templates he gave members are the same ones powering his funded startup.
- **Brandon Hancock:** Selling AI tokens in a formatted, high-value way yields extreme margins — tokens cost dollars, you sell the output for hundreds.
- **Brandon Hancock:** Git work trees enable true parallel feature development: each branch is isolated, each feature gets its own IDE instance, and Claude Code isn't competing to edit the same files simultaneously. The main gotcha is database schema migrations (e.g., Drizzle journal conflicts) which must still be done in series.
- **Brandon Hancock:** The hardest part of AI-assisted coding is the thinking and planning phase. Once a detailed task spec exists, cheaper models can handle implementation — use expensive models for specs, cheaper ones for execution.
- **Brandon Hancock:** Gemini 3 Flash Preview on low thinking is currently the best model for production AI applications: better instruction-following than GPT-4.1, similar speed, lower cost, and capable of handling 25,000+ token RAG contexts in ~15 seconds.
- **Brandon Hancock:** Agent frameworks (LangChain, LangGraph, Crew AI) are being used less in favor of direct structured LLM calls chained together programmatically — simpler, more predictable, and sufficient for most production pipelines.
- **Dmitry Avramenko:** Graphite (acquired by Cursor, not Anthropic) is designed to solve the parallel branch merge ordering problem that arises when running many agents on Git work trees simultaneously.
- **Tiran Dagan:** Building a cost-tracking dashboard across all LLM calls is essential as costs accumulate from many small sources (AI summaries, microservice calls, etc.).
- **Bastian Venegas Arevalo:** GLM 4.7 (from Zhipu AI, available via OpenRouter) is extremely cheap — three days of heavy agentic coding experiments cost ~$6 — and produced better website output than GPT-5 in one test.
- **Patrick Chouinard:** Using Claude Code with custom skills (Python/Bash scripts) to manage network infrastructure as code — including VLAN configuration, firewall rules, and documentation — stored in a Git repo, is a powerful pattern for infrastructure automation.
- **HP (Scott):** Deepgram is significantly better than OpenAI Whisper for streaming/chunked speech-to-text; Whisper hallucinates on streaming chunks. Deepgram also offers domain-specific models (e.g., medical) at no extra cost over the base model.
- **Brandon Hancock:** When pricing AI-accelerated development work, frame it as charging more per hour but delivering the equivalent of 8 hours of traditional work in 2 — and proactively suggest next steps to keep the engagement going.
- **TinySeed funding criteria:** Minimum $500 MRR demonstrated over multiple months; preference for B2B; new batch opens in February.
- **Dmitry Avramenko:** Using custom Claude Code skills (pre-built scripts) instead of generic tool calls significantly reduces token consumption — Claude's generic tool use can cost 5x more than a targeted custom script.

## qa

**Q (Marc Juretus):** Can you give a two-minute explanation of Git work trees and why I should know about it?
**A (Brandon Hancock):** Normally when doing AI development, you build multiple features under the same branch, which creates messy, untraceable PRs. Git work trees let you create a separate folder per feature, each on its own branch, each with its own IDE open. You can work on five features in parallel without Claude Code competing to edit the same files. The only gotcha is database schema changes (like Drizzle journal files) which still need to be done in series.

**Q (Dmitry Avramenko):** Are you going to continue updating ShipKit given how busy you are with the startup?
**A (Brandon Hancock):** Yes — the goal is to keep adding modules as I learn new things (like Git work trees). I still owe one more walkthrough (the Worker SaaS template turned into a real app). Weekly calls will become intermittent, probably once a month, but ShipKit itself will keep getting updates.

**Q (Dmitry Avramenko):** What's your view on Vite vs. Next.js for new projects?
**A (Brandon Hancock / Bastian Venegas Arevalo):** Next.js is preferred for anything API-heavy, server-side rendering, or with complex state management. Vite/React is great for quick AI-generated prototypes and simple dashboards but falls apart for more complex apps. Astro is a good alternative if you need no APIs and want extreme load speed with JavaScript islands.

**Q (Dmitry Avramenko):** If you run out of Claude tokens on the $20 plan, is it bad to switch to Cursor?
**A (Brandon Hancock / Dmitry Avramenko):** No — both use the same underlying models and are ~90% similar in capability. A better strategy is to use expensive models (Claude) for planning and spec creation, then switch to cheaper models for implementation. An orchestrator that automatically routes tasks to the appropriate model based on complexity is the ideal end state.

**Q (Dmitry Avramenko):** Are LangChain, LangGraph, and Crew AI doomed?
**A (Brandon Hancock):** They're being used less and less for production work. Direct structured LLM calls chained together are simpler and more reliable. Frameworks are still useful for demos or single-shot complex tasks, but for production pipelines with known inputs and outputs, they add unnecessary complexity.

**Q (HP/Scott):** What should I use instead of Supabase edge functions for persistent WebSocket connections (they time out at ~3-6 minutes)?
**A (Brandon Hancock / Ty Wells / Tiran Dagan):** Railway is cheap and simple (just provide a Docker image). Render is another strong option — Ty switched from Railway to Render for stateless services and found it more reliable. Render also has an MCP. LiveKit is an all-in-one alternative that handles WebSockets and works with Deepgram under the hood.

**Q (Dmitry Avramenko):** How do you charge clients when AI lets you do in 4 hours what used to take a week?
**A (Brandon Hancock):** Charge more per hour and frame it as "2 of my hours equals 8 of someone else's." Proactively suggest next steps after delivery to keep the engagement going. The real opportunity is doing more volume of work, not just the same work faster.

**Q (Garron Selliken):** Are there better tools than Google AI Studio for quick prototyping before handing off to a developer?
**A (Brandon Hancock):** Bolt.new and Lovable are the two main options — both are great for quickly turning prompts into visual prototypes. The Pro plan (~$25/month) is sufficient. The typical workflow is to prototype in Bolt/Lovable, then pull the code into Claude Code and rebuild it properly.

**Q (Hemal Shah):** What's the best approach for using AI to add dimension annotations to product images at scale?
**A (Brandon Hancock):** Start by building a strong system prompt with 5-10 test images, iterating on errors. Use Gemini 3 Pro Image Preview (Nano Banana) for generation. Then build a separate "critiquer" prompt that takes the output image and returns a structured pass/warning/fail with a message — so users only manually review the ~2% that fail rather than all images. Make the model selection per step configurable in your app so you can swap cheaper models for validation steps.

## tools

- **EMS Soap** — Brandon's funded startup; AI-powered SOAP report generation for EMTs to improve insurance billing accuracy
- **ShipKit** — Brandon's template/course platform; RAG template and Worker SaaS templates discussed as foundations for real-world apps
- **Git Work Trees** — Brandon adopted for parallel feature development; each feature gets its own branch and IDE instance
- **Graphite** — Acquired by Cursor; solves parallel branch merge ordering for agentic Git work tree workflows
- **Claude Code** — Primary agentic coding tool used by most members; used for everything from feature development to network infrastructure management
- **Cursor** — IDE used alongside Claude Code; mentioned as interchangeable for most tasks
- **Deepgram** — HP's speech-to-text service for live call coaching app; far superior to Whisper for streaming; offers domain-specific models (medical, etc.); $200 free credit on signup
- **Supabase** — Backend/edge functions used by HP for call coaching app; edge function WebSocket timeout (~3-6 min) is a known limitation
- **Railway** — Deployment platform for stateless services; recommended by Brandon as simple Docker-based hosting
- **Render** — Deployment platform; Ty and Tiran prefer it over Railway for stateless services; has MCP integration
- **LiveKit** — All-in-one WebSocket/audio streaming service; works with Deepgram under the hood; suggested as alternative to Supabase edge functions
- **Drizzle** — ORM used by Brandon; journal file conflicts are the main pain point when doing parallel database migrations with Git work trees
- **Supabase Branches** — Mentioned as a potential way to handle parallel database changes across Git work trees
- **N8N** — Patrick's workflow automation server; used to receive Fieldy webhook transcripts and decompose/categorize them
- **Fieldy** — Wearable always-on recording/transcription device (similar to Limitless Pendant); Patrick using it to feed transcripts into N8N pipelines
- **Limitless Pendant** — Previous wearable recorder; now acquired by Meta, hardware no longer sold
- **Twingate / Tailscale** — Patrick's zero-trust network tunneling tools for securely exposing local N8N server
- **Ngrok** — Tunneling service for exposing local ports externally; mentioned as simpler alternative for Patrick's use case
- **Daytona** — Sandboxed container service for running sub-agents safely; persistent storage, own machines, streaming SDK; Bastian planning to use for isolating agent code execution
- **EXA** — Web search API used by Bastian's CLI agent for real-time search; recommended for adding search to AI apps
- **OpenRouter** — Model aggregator used by Bastian and Tiran; enables switching between any model provider; Bastian ran 3 days of experiments for ~$6
- **GLM 4.7 (Zhipu AI)** — Extremely cheap Chinese model available via OpenRouter; Bastian used it as root orchestrator agent; produced better website output than GPT-5 in one test
- **Kimi K2** — Chinese model (Moonshot AI); good at writing, comparable to GPT-4.5 feel; available via OpenRouter
- **Gemini 3 Flash Preview (low thinking)** — Brandon's current recommended model for production AI apps; best instruction-following, faster than GPT-4.1, lower cost
- **Gemini 3 Pro Image Preview ("Nano Banana")** — Google's image generation/editing model; used by Hemal for product image annotation; ~$1.13 per 1024x1024 image
- **Google AI Studio** — Used by Garron for prototyping real estate CRM; also used to identify model names and pricing
- **PlantUML / Kroki** — Tiran uses PlantUML for workflow diagrams generated from JSON; Kroki is a free API that renders PlantUML (and Mermaid, etc.) to JPEG
- **Trigger.dev** — Async job queue service; Tiran built his own alternative microservice instead
- **Bolt.new** — AI prototyping tool; recommended for quick UI mockups before handing to Claude Code
- **Lovable** — AI prototyping tool similar to Bolt; uses Vite/React; good for fast prototypes, not complex apps
- **TinySeed** — Micro-VC that funded EMS Soap; requires $500 MRR minimum; new batch opens February; prefers B2B
- **Hyros** — Ad tracking SaaS by Alex Becker; Brandon referenced as inspiration for adding data pipeline/analytics to Ty's ML platform
- **Stripe** — Payment processor; Brandon suggested integrating with Ty's platform to auto-collect customer data for ML predictions
- **PostHog** — Analytics tool; mentioned alongside Stripe as a data source for Ty's ML platform
- **Warp** — AI-powered terminal; mentioned as useful for terminal-level AI assistance with cheap models
- **Apify** — Web scraping platform; suggested as affordable option for YouTube transcript scraping
- **YouTube DLP** — Open-source YouTube downloader (Python); mentioned for downloading video as MP3 for transcription
- **Dakota (Oxylabs?)** — Residential proxy/scraping service with Amazon scraper templates; Tiran uses it; Bastian also referenced it for Amazon product data ingestion
- **Cloudflare Workers** — Dmitry built a custom ChatGPT action endpoint on Cloudflare that creates GitHub issues from voice conversations
- **React Flow** — Visual workflow/node graph library for React; mentioned by Juan as potentially what Ryan used for his flow builder
- **Elixir** — Language Bastian chose for his CLI agent orchestrator for resilience and fault tolerance
- **SQLite** — Local persistent storage for Bastian's CLI agent
- **Flower** — Job monitoring UI for Celery; Tiran uses it in his workflow microservice for async job management
- **Russell Brunson books (DotCom Secrets, Traffic Secrets, Expert Secrets)** — Tiran using them as business strategy framework; prompted ChatGPT to apply the Russell Brunson model for customer segmentation
- **Genom** — Prompt management and A/B testing startup that reached out to Dmitry for partnership
- **GitHub Actions** — Dmitry runs his Claude Code agent workflows in GitHub Actions for automated blog post generation and other tasks

## links

- Dmitry Avramenko's LinkedIn post about his agentic orchestrator — posted in chat; received ~6,000 views and inquiries from 3 CIOs within a week
- Dmitry Avramenko's YouTube demo — shows "George" agent conducting a weekly agentic sprint retrospective; link shared in chat
- Tiran Dagan's workflow microservice GitHub repo — open-source async LLM workflow orchestrator with webhook support, OpenRouter integration, and markdown prompt templates with include commands; link posted in chat
- Daytona — sandboxed container service for agent code execution; Bastian shared link in chat (daytona.io)
- EMS Soap — Brandon's funded startup (screen shared briefly during call)
- Screenly — Ryan's digital signage SaaS (screenly branding shown during demo)

## decisions

- **Brandon Hancock** will record a ShipKit module on Git work trees this Saturday, including a Claude Code `worktree` command that automates the checkout/branch/open workflow.
- **Brandon Hancock** will record the remaining ShipKit walkthrough (Worker SaaS template → real-world app) this weekend.
- **Brandon Hancock** will unblock HP (Scott) from the ShipKit school group immediately after the call (Scott to email brandon@brandonhancock.io).
- **Brandon Hancock** will review the Claude slash command audit that HP sent and respond to the correct email address.
- **Brandon Hancock** will connect with Patrick Chouinard next week to record a video together.
- **Brandon Hancock** will join the Thursday 10am call to walk Tiran through the TinySeed funding process in more detail.
- **Brandon Hancock** will connect Ryan (One Stop Creative Agency) with his brewery friend whose digital signage broke, as a potential early Screenly customer.
- **Dmitry Avramenko** will share his email in chat so Tiran can connect him with an Agile consultant for a potential partnership.
- **HP (Scott)** will investigate Railway and Render as alternatives to Supabase edge functions for persistent WebSocket connections.
- **HP (Scott)** will email Brandon at brandon@brandonhancock.io to get unblocked from the school group.
- **Bastian Venegas Arevalo** will integrate Daytona sandboxed containers as the next step for his CLI agent orchestrator to enable safe remote sub-agent execution.
- **Tiran Dagan** will test Gemini 3 Flash Preview on low thinking for his preparedness platform's plan generation workflow and report back next week.
- **Patrick Chouinard** will explore opening a YouTube channel (potentially through his consulting firm) to share AI-driven SDLC content publicly.
- **Dmitry Avramenko** will push his locally-running agents to the cloud as the next major milestone for his orchestrator platform.