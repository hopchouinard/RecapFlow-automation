## general

This was a group coaching call hosted by Brandon Hancock for ShipKit members. The session followed a round-robin format where participants shared project updates, asked technical questions, and received feedback. Topics ranged from website deployment and agentic AI tools to multi-tenant database architecture, SOC 2 compliance, voice agents, and IDE tooling. The call featured a mix of experienced developers and newer builders, all working on varied real-world projects using the ShipKit stack (Next.js, Supabase, Vercel, and related tools).

Several members presented notable work: Tom Welsh rebuilt his cybersecurity consulting website using ShipKit; Ty Wells built an interactive live presentation platform with polling, trivia, and a voice agent for a Chamber of Commerce event; Paul Miller demonstrated a completed beta of a route optimization SaaS for the traveling salesperson problem applied to New Zealand retail; and Patrick Chouinard showed a custom ChatGPT GPT he built to run ShipKit's master idea prompting workflow entirely by voice while commuting.

Brandon also shared updates on ShipKit itself, including a Windows fix for the RAG SaaS template, an upcoming vanilla Next.js + Trigger.dev template, and a note about the pending deprecation of Google's text-embedding-004 model. The call closed with discussions on IDE choices (Cursor vs. Windsurf), GitHub Copilot for Markdown work, domain naming conventions, and using MCP integrations (Perplexity, Atlassian, Notion) inside IDEs.

## insights

- **Patrick Chouinard:** The ShipKit master idea prompt can be split into personality, workflow, and output template components and loaded into a custom ChatGPT GPT, enabling full voice-based ideation while commuting — saving expensive Cursor tokens for actual coding.
- **Brandon Hancock:** ShipKit templates are essentially SOPs (Standard Operating Procedures) for AI agents. The mental model: define the desired output first, use existing templates as style references, then iterate the new template 5–10 times until quality is high.
- **Brandon Hancock:** For non-RAG, non-agent projects, a new vanilla Next.js + Trigger.dev template is coming that will serve as the catch-all foundation — demonstrated use cases include voice transcription services and video short generators.
- **Brandon Hancock:** Vercel's "Fluid Compute" feature extends cloud function timeouts to up to 13 minutes, which is sufficient for chained LLM call workflows without needing Trigger.dev.
- **Brandon Hancock:** OpenAI's new agent builder UI scores 10/10 for ease of deployment but ~6/10 for agentic capability — no true agent-to-agent delegation exists yet, and a ~20% error rate was observed shortly after launch.
- **Mitch:** Tmux is highly recommended for managing multiple simultaneous terminal sessions when running several AI coding agents (Claude Code, Codex CLI, etc.) across different projects.
- **Paul Miller:** The traveling salesperson problem for 400+ stores is computationally intractable by brute force (10^1134 combinations for New Zealand alone); the solution combines a specialized algorithm in Docker containers with an agentic AI layer for pre- and post-analysis.
- **Brandon Hancock:** Multi-tenant architecture requiring separate databases per client is a massive scope increase — Supabase is not designed for per-tenant databases; alternatives include Neon (spin up per-tenant DBs) or AWS Aurora Serverless v2. Row-Level Security (RLS) with a tenant ID is often sufficient and far simpler for MVP.
- **Patrick Chouinard:** GitHub Copilot ($10/month) is superior to Cursor for Markdown autocomplete, and GPT-4.1 / GPT-5 Mini have zero request multipliers (effectively unlimited use), making it far cheaper than burning Claude tokens in Cursor for non-code document work.
- **Patrick Chouinard:** Setting a `.github` directory at the home/documents folder level turns your entire file system into a Copilot project, enabling paragraph-level autocomplete trained on your own writing patterns.
- **Brandon Hancock:** The Perplexity MCP inside VS Code/Cursor enables deep web search directly in the IDE — unlike Brave or other search MCPs, it supports deep research queries.
- **Brandon Hancock:** For LLC setup, a single-member LLC is the fastest start but carries high self-employment tax; converting to an S-Corp when income is consistent allows salary control and avoids double taxation.
- **Morgan Cook:** In Windsurf, the `.codiumignore` file (IDE-level ignore) is not honored by background AI tasks — only the `.gitignore` is. Workaround: place the reference project as a sibling folder under a shared parent directory.
- **Brandon Hancock:** Google's `text-embedding-004` model is being deprecated (approximately June); a utility migration script will be added to ShipKit RAG SaaS to re-embed to `text-embedding-005` at minimal cost (pennies).

## qa

**Q (AlexH):** What are your thoughts on OpenAI's new agent builder UI?
**A (Brandon Hancock):** Ease of deployment is 10/10 — it felt like N8N-level simplicity. However, agentic capability is about a 6/10 because there's no real agent-to-agent delegation or collaboration like you'd get with Crew AI or ADK. Also observed roughly a 20% error rate right after launch, likely due to server load. The good news is this is the worst it'll ever be.

**Q (Mitch):** I want to run a chain of LLM calls (output of one feeds the next). Should I use Trigger.dev or Google Cloud Functions, or is there another option within the ShipKit stack?
**A (Brandon Hancock):** Look at Vercel's Fluid Compute feature first — it extends cloud function timeouts to up to 13 minutes, which should be sufficient for chained LLM calls since the server isn't doing compute, just waiting for AI responses. You may not need Trigger.dev at all for this use case.

**Q (Hemal Shah):** For a non-standard application (e.g., e-commerce) that doesn't fit the chat/RAG/agent templates, where do I start in ShipKit?
**A (Brandon Hancock):** Use the chat project template for now. A new vanilla Next.js + Trigger.dev template is coming soon that will be the catch-all for non-AI projects. It will be demonstrated with real-world conversions like a voice transcription service and a video shorts generator.

**Q (Hemal Shah):** For forming an LLC, should I use an online service like LegalZoom, and what about business banking?
**A (Jake Maymar):** Avoid LegalZoom — the upsells can push costs to $1,500+. Use Perplexity for deep research, then file directly with your state (Georgia is $100). You can do it yourself for very little.
**A (Brandon Hancock):** After filing, get your EIN, then open a Chase business account and a business credit card (Chase Ink Business Preferred) to earn points on business spending. For tax structure, start as a single-member LLC but consider converting to an S-Corp once income is consistent to reduce self-employment tax.

**Q (Ty Wells / Hemal Shah):** What tools and tech did you use for your voice agent?
**A (Ty Wells):** Retell AI for the voice agent, integrated with Cal.com for calendar booking and appointment scheduling.

**Q (Morgan Cook):** I'm having issues with Windsurf not seeing reference projects that are in the .gitignore — the interactive chat can see them via .codiumignore, but background tasks can't. Any fix?
**A (Morgan Cook, self-resolved):** The workaround is to place the reference project as a sibling to the main project under a shared parent folder, so it's outside the Git structure but still visible to the IDE.

**Q (Morgan Cook):** For a multi-tenant SaaS serving charter schools that want separate databases, what's the best approach?
**A (Brandon Hancock):** Supabase isn't designed for per-tenant databases. Options are Neon (spin up a new DB per tenant) or AWS Aurora Serverless v2. However, for MVP, Row-Level Security (RLS) with a tenant ID in Supabase is likely sufficient — data isolation is enforced at the query level, similar to how Gmail works. Separate databases are a massive scope increase.

**Q (Morgan Cook):** What voice AI platforms are good for low-latency phone/conversational use beyond LiveKit?
**A (Ty Wells):** Retell AI is easy to spin up and handles numbers/dates well. Audiovox (Vapi) is cheaper (~5 cents/minute vs. 11 Labs at 18–22 cents/minute). For LiveKit latency issues specifically, reach out to Maxim in the group — he used a custom inference tool workaround.

**Q (Elijah):** Where do I find the ShipKit files to create custom templates for non-coding tasks like project management or content creation?
**A (Brandon Hancock):** A dedicated template deep-dive video is being recorded tomorrow. The core concept: know your desired output first, use existing ShipKit templates as style/structure references, then ask the AI agent to replicate that structure for your new template. Iterate 5–10 times. Templates are just SOPs for agents.

**Q (Prem):** Can ShipKit prep templates be used as Cursor slash commands instead of drag-and-drop?
**A (Brandon Hancock / Prem):** Yes — create a `commands` folder under `.cursor`, move the markdown template files there, then update the `.cursorignore` file with a `!` negation rule for that folder and re-sync the index. After that, typing `/` in Cursor chat surfaces all templates as slash commands.

## tools

- **ShipKit** — The core product being used by all participants; a Next.js SaaS starter kit with AI templates and development workflows
- **Vercel** — Hosting/deployment platform; Fluid Compute feature discussed for extending LLM chain timeout to 13 minutes
- **Supabase** — Database backend used across most projects; discussed limitations for multi-tenant per-database setups
- **Trigger.dev** — Background job processing; mentioned as an alternative for long-running LLM chains and upcoming template foundation
- **Cursor** — Primary AI coding IDE used by Brandon and most members; discussed for Markdown limitations vs. GitHub Copilot
- **Windsurf (Codeium)** — AI IDE used by Morgan Cook on Windows; bug noted where background tasks ignore `.codiumignore`
- **GitHub Copilot** — Recommended by Patrick for Markdown autocomplete in VS Code; $10/month with unlimited GPT-4.1/GPT-5 Mini usage
- **Tmux** — Terminal multiplexer recommended by Mitch for managing multiple simultaneous AI coding agent sessions
- **OpenAI Agent Builder (Responses API / Agent UI)** — New product reviewed by Brandon; praised for deployment simplicity, criticized for lack of agent-to-agent communication
- **Retell AI** — Voice agent platform used by Ty Wells; integrates with Cal.com for appointment booking
- **Deepgram** — Voice-to-text platform used by Brandon for voice projects; noted as very affordable with $200 free credits
- **Audiovox / Vapi** — Voice AI platform mentioned by Ty as cheaper alternative (~5 cents/minute)
- **11 Labs** — Voice synthesis platform; noted as premium option at 18–22 cents/minute
- **LiveKit** — Real-time audio/video platform; Morgan noted latency issues in conversational voice use
- **Cal.com** — Calendar/scheduling tool integrated with Ty's voice agent for booking consultations
- **Gamma** — Presentation tool used by Ty to generate slides, then imported into his custom ShipKit presentation app
- **Google Cloud Run Jobs** — Recommended by Brandon for Paul's long-running route optimization jobs; no hard timeout cap
- **Google Cloud (GCP)** — Paul's target deployment environment for his route optimization Docker containers
- **Docker** — Used by Paul to run route optimization algorithm instances locally in dev
- **PostGIS** — Postgres geospatial extension used by Paul for geographic routing calculations
- **AWS Aurora Serverless v2** — Mentioned by Juan as a flexible multi-database option for multi-tenant scenarios
- **AWS EC2** — Used by Juan for inference engine and web app hosting in SOC 2-compliant private subnet architecture
- **Ngrok** — Tunneling tool used by Juan to expose private subnet EC2 instances for client demos
- **Vanta** — SOC 2 compliance automation platform; discussed pricing (reportedly ~$100K/year for government use cases)
- **Neon** — Postgres database provider; mentioned as option for spinning up per-tenant databases
- **Fern** — API spec generation tool recommended by Brandon for coordinating front-end/back-end teams
- **Perplexity MCP** — MCP integration enabling deep web search directly inside VS Code/Cursor
- **Atlassian MCP** — MCP for JIRA/Confluence integration inside IDE, used by Patrick
- **Notion MCP** — MCP for pushing Markdown content to Notion from IDE
- **Warp** — CLI client used by Morgan Cook alongside Windsurf
- **OBS Studio** — Screen recording software; Juan bought a mini PC specifically to run it for YouTube content creation
- **LegalZoom** — LLC formation service; Jake warned against it due to aggressive upselling
- **Chase Ink Business Preferred** — Business credit card recommended by Brandon for LLC banking setup
- **Namecheap** — Domain registrar mentioned; noted that .ai domains require 2-year purchase (~$180 total)
- **Udemy (AWS course by Stephane Maarek)** — AWS Certified Cloud Practitioner course recommended for certification prep
- **N8N** — Workflow automation tool referenced as a simplicity benchmark for OpenAI's agent builder deployment experience
- **Crew AI / ADK (Google Agent Development Kit)** — Multi-agent frameworks referenced when comparing agent-to-agent collaboration capabilities

## links

- No explicit URLs were shared in the transcript text. Brandon mentioned dropping links in chat (Vanta, Fern, Tmux, AWS Udemy course, Chase Ink referral) but the actual URLs were not captured in the transcript.

## decisions

- **Brandon Hancock** will record a ShipKit template deep-dive video tomorrow covering how to create and customize templates
- **Brandon Hancock** will release the Windows fix for the RAG SaaS template after the call tonight
- **Brandon Hancock** will add a utility migration script to ShipKit RAG SaaS to upgrade from `text-embedding-004` to `text-embedding-005` before the deprecation deadline
- **Brandon Hancock** will build and release a vanilla Next.js + Trigger.dev template as the next ShipKit project, with real-world conversion examples (voice transcription service, video shorts generator)
- **Patrick Chouinard** will share his custom ChatGPT GPT (ShipKit master idea voice workflow) with the group
- **Ty Wells** will share the recording of his Chamber of Commerce AI workshop presentation with the group
- **Paul Miller** will deploy his route optimization app to Google Cloud within the next few days using GCP credits, referencing the RAG SaaS GCP setup script as a starting point
- **Paul Miller** will have his business analyst (Vladimir) test the beta app for a week, then record a Zoom reveal session to share with the group
- **Paul Miller** purchased an additional ShipKit subscription for Vladimir Mirkhev to onboard him to the tooling
- **Juan** will create a test database in AWS Aurora Serverless v2 with synthetic data to begin building out the RAG/vector system independently while waiting for front-end/back-end teams
- **Brandon Hancock** will follow up with Vanta on SOC 2 pricing and share findings with the group
- **Elijah** will attempt to create a custom ShipKit template using the backward-design approach discussed and return with questions if needed
- **Juan** will set up OBS Studio on his new mini PC and begin creating YouTube content about AWS for AI projects
- **Brandon Hancock** will try using GitHub Copilot in VS Code for Markdown-heavy work as a personal challenge this week
- **Morgan Cook** will reach out to Maxim in the group regarding LiveKit latency workarounds