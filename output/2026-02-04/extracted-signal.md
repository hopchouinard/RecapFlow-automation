## general

This was a group coaching/community call led by Patrick Chouinard (taking over from Brandon) with Paul Miller as a co-facilitator. The session opened with pre-submitted questions on multi-tenancy, Google ADK production readiness, and OpenClaw security, then moved into member project updates and open discussion.

Ty Wells presented Frank Labs (franklabs.io), an AI-powered business team platform featuring voice-capable agents with phone numbers, emails, and autonomous/co-pilot/advisory modes. Patrick Chouinard walked through a security framework he published for OpenClaw installations, covering identity isolation, GitHub-based authorization pipelines, SSH tunneling, and externalized memory via Obsidian. Morgan Cook shared a workflow for iterating on document-processing automation using Claude skills before converting deterministic logic to JavaScript. Ana Preciado discussed a market research/recommendation system project and sought advice on starting as a solo AI specialist at a bank. The call closed with discussion on OpenClaw's broader implications, hallucination management, and deployment strategies.

The session also featured extended discussion on the emerging tension between AI-native development workflows and traditional engineering team structures, the "software on demand" philosophy (building custom tools instead of subscribing to SaaS), and practical advice for navigating corporate AI adoption in regulated industries.

## insights

- **Patrick:** Anything that can be made deterministic should be — use AI to organize and manage when to run logic, but convert the actual job to a script once the process is stable. This cuts execution time from ~60 seconds to ~3 seconds and eliminates token waste.
- **Morgan:** Use Claude skills to iterate through a problem until the process is deterministic, then have Claude convert the skill to a JavaScript/script. The skill remains as a thin wrapper that calls the script.
- **Patrick:** Give an AI agent its own identity (dedicated Gmail, calendar, GitHub account) and use GitHub PRs as an authorization pipeline for all agent-produced artifacts — nothing merges without human approval.
- **Patrick:** Never expose the OpenClaw web control panel publicly. Access it only via SSH tunnel when absolutely necessary, then close the tunnel. Use Telegram as the primary interaction channel.
- **Ty:** Use a "council" of independent agents (optimistic, pessimistic, neutral perspectives) for security and prompt-injection checking — agents self-check each other's outputs.
- **Patrick:** In corporate/regulated environments, identify the approved AI platform or hyperscaler first, then run everything through that. A simple rule for non-technical users: "Would you be comfortable if this appeared on the front page of a newspaper tomorrow?"
- **Patrick:** For OpenClaw, use Claude Code as a tool called by the agent rather than making the agent itself the coding engine — this allows swapping the orchestration model (Gemini, ChatGPT) independently of the coding model (Claude Sonnet).
- **Paul:** Start client engagements with the smallest possible proof of concept. The most successful SaaS tools are often simple solutions, not complex ones. Don't boil the ocean.
- **Ty:** "Software on demand" — if you need a function, build it rather than subscribing to a SaaS tool. The cost of building is now lower than the ongoing subscription in many cases.
- **Patrick:** Hallucinations are a signal of insufficient context in the prompt. Always give the model a path to say "I don't know" rather than forcing it to hallucinate to reach a goal.
- **Ty:** Using a "reverse hallucination" process — when a model hallucinates, use that instance to train it to ask more clarifying questions rather than guessing.
- **Juan:** AI-native development teams will need new documented modes of operation; most existing documentation covers solo developers, not multi-role teams using agentic tools collaboratively.
- **Patrick:** Replace "vibe coder" with "AI-assisted developer" in corporate contexts — the former has become pejorative and creates unnecessary resistance.
- **Elijah:** To overcome resistance from teams (security, compliance, IT) that could block AI projects, provide them a useful service for free first — it becomes very hard for them to say no afterward.

## qa

**Q (Paul Gallovich):** What is the best approach to implementing multi-tenancy, specifically using Clerk authentication with organizations and Supabase?
**A (Morgan Cook):** Use a server-side data access layer with a dedicated role rather than relying on Supabase RLS directly. The core challenge is table structure — ensure tenant ID is present in all appropriate tables. Public data for search can be served via views populated by a cron job. For user-to-tenant binding, consider an invitation flow where tenant admins invite users via email link. Users belonging to multiple tenants add complexity.

**Q (Hemal Shah):** Has anyone taken Google ADK to production?
**A (Ana Preciado):** Not shipped to production, but Brandon had noted that Google's API call configuration for ADK was not optimal and recommended against it. The main issues were with the Agent Engine; Google later tried to migrate everyone to Cloud Run instead, suggesting the original deployment approach was not the intended final path.

**Q (Juan Torres):** What made Ty choose a hybrid approach (local Mistral 7B + GPT-4o API), and where is the local model deployed?
**A (Ty Wells):** The local model runs on an EC2 instance. Business function logic (accounts payable, sales, etc.) is fairly standard and doesn't require large models — you just need the business context via a light RAG. GPT-4o handles the heavier reasoning while the local model handles character/persona consistency.

**Q (Juan Torres):** What is Ty's high-level guardrail strategy for Frank Labs agents?
**A (Ty Wells):** A council of independent agents (optimistic, pessimistic, neutral) provides self-checking. There are also prompt-injection councils reviewing agent outputs, plus front-end and back-end guardrails. The tradeoff is always latency and token cost vs. security coverage.

**Q (Shah Martinez):** How does the lead-generation agent work at a high level?
**A (Ty Wells):** The agent has access to tools including Perplexity, Hunter, Apollo, and Clay as a package of "lead enrichment" capabilities. Different experts have different tool sets. The data is stored in a custom business suite (accounts, sales, POS, invoicing) built previously.

**Q (Hemal Shah):** What are the hardware and model requirements for running OpenClaw?
**A (Patrick Chouinard):** Very lightweight — 4GB RAM, ~50GB disk, 2 cores is sufficient. Patrick runs his on a Proxmox Linux VM (a box under his desk). For models, he uses his Codex account for the orchestration layer and runs Claude Code as a separate tool on the same machine for coding tasks, allowing the orchestration model to be swapped independently.

**Q (Elijah):** Where is the Notebook LM link on Patrick's security documentation site?
**A (Patrick Chouinard):** On the homepage there is an "Interactive Notebook" button that links directly to the Notebook LM instance containing all the markdown files.

**Q (Paul Gallovich):** For a PI with large case files and privacy concerns, could a similar Notebook LM approach work locally?
**A (Patrick Chouinard / Morgan Cook):** Notebook LM is a Google/Gemini service — do not put private data there. For local private data, use LM Studio with a model like GPT-4o OSS 20B or Gemma 3 14B. You can point it at a local directory without needing a RAG pipeline for many use cases. Morgan noted Claude Code (without writing source) can also consume local content while keeping data local, though the LLM calls still go out.

**Q (Ana Preciado):** Any advice for starting as a solo AI specialist at a bank?
**A (Patrick Chouinard, Paul Miller, Tom Welsh):** First, get the bank to define what "AI specialist" means to them. Governance is the bedrock — understand SOC 2 compliance for financial services. Identify whether there is an approved AI platform or hyperscaler (Azure, AWS, GCP) and run everything through that. Build a Claude project or Notebook LM with all governance documentation to get up to speed quickly. Align your success metrics to your boss's KPIs. Tom Welsh: expect frequent knockbacks from security, compliance, and risk — don't be dismayed, work within the frameworks. Patrick: providing a useful service to the security/compliance team early makes future negotiations much easier.

**Q (Raghav):** Do I need deep cloud knowledge to deploy an app, and how should I prompt Claude Code to help?
**A (Patrick Chouinard, Ty Wells, Tom Welsh):** You need enough knowledge to know where you want to deploy and what the goal is — Claude automates the job but you define the job. For simplest deployment, Vercel (for TypeScript/Next.js) is easiest; Railway or Render for serverless/Python. Tell Claude Code to guide you step-by-step through setting up the CLI and environment. Ty: also instruct it to check that the CLI is on the latest version before each deploy, as CLIs update frequently and version mismatches cause failures.

## tools

- **OpenClaw** — AI agent framework being discussed for security hardening, deployment, and production use
- **Claude / Claude Code** — Primary AI coding assistant; Patrick uses Claude Code as a tool called by OpenClaw rather than as the agent itself
- **ChatGPT / GPT-4o** — Used by Ty for orchestration in Frank Labs; Patrick used it for the initial security framework conversation
- **Gemini / Notebook LM** — Patrick used Notebook LM to create an interactive chatbot over his OpenClaw security documentation
- **Supabase** — Discussed in context of multi-tenancy implementation with server-side data access layers
- **Clerk** — Authentication platform with multi-tenant/organization support, referenced in multi-tenancy question
- **Proxmox** — Patrick's local virtualization platform hosting his OpenClaw Linux VM
- **Tailscale** — Mentioned by Paul Miller for locking down server infrastructure
- **Docploy (Coolify/Dokploy)** — Mentioned by Paul Miller for DevOps/server management
- **DeepGram** — Integrated in Frank Labs for voice transcription
- **LiveKit** — Integrated in Frank Labs for real-time voice communication
- **NVIDIA PersonaPlex** — Ty evaluated and drew from it for natural speaking ability in Frank Labs voice agents
- **Mistral 7B** — Local model Ty uses on EC2 for persona/character consistency in Frank Labs
- **LM Studio** — Recommended for running local LLMs with private data (e.g., GPT-4o OSS 20B, Gemma 3 14B)
- **Gemma 3 (14B)** — Patrick's preferred local model, runs on Mac Mini 24GB or dual 1080 Ti
- **Obsidian** — Patrick externalizes his OpenClaw agent's memory/decisions to an Obsidian Vault synced via GitHub
- **Playwright** — Used by Morgan in document automation pipeline to generate PDFs from HTML
- **Perplexity** — Used as a tool by Frank Labs lead-generation agent
- **Hunter** — Email finding tool used by Frank Labs SDR agent
- **Apollo** — Lead database tool used by Frank Labs; noted as getting less reliable due to data quality issues
- **Clay** — Used for ICP grounding and lead enrichment in Frank Labs
- **Vercel** — Recommended as easiest deployment platform for TypeScript/Next.js apps
- **Render** — Mentioned as alternative to Railway for serverless deployments
- **Railway** — Mentioned as deployment option for Python/serverless
- **Cloudflare Pages** — Patrick hosts his documentation sites on Cloudflare Pages with DNS redirect from Hostinger
- **Hostinger** — Patrick's domain registrar; uses it for DNS redirection to Cloudflare Pages subdomains
- **Privacy.com** — Jake shared a link; allows creating virtual cards with spending limits and freeze capability, useful for capping AI API spend
- **Pickaxe** — Mentioned by Elijah as a tool for monetizing GPTs/chatbots
- **Zendesk** — Mentioned as a SaaS tool Ty is replacing with a custom-built ticketing system
- **FreshBooks** — Mentioned as a SaaS invoicing tool Ty is replacing with a custom-built solution
- **ShipKit** — The app template framework the community is built around; referenced throughout
- **Google ADK (Agent Development Kit)** — Discussed regarding production readiness; noted as having API configuration issues and migration from Agent Engine to Cloud Run
- **LangGraph / LangChain** — Mentioned as alternatives to Google ADK for agent orchestration
- **Telegram** — Patrick's primary interface for interacting with his OpenClaw agent (instead of the web control panel)
- **Cursor** — Mentioned by Mitch as an IDE he switched away from due to paid account prompts
- **Codex (OpenAI)** — Mentioned as a new cloud-based coding tool Mitch is evaluating for client deployments
- **NanoClaw** — Mentioned as a lightweight fork/entry-level version of OpenClaw

## links

- **franklabs.io** — Ty Wells' AI business team platform with voice-capable agents; shared in chat for live demo
- **Patrick's OpenClaw Security Framework site** — Published documentation site (subdomain of Patrick's main domain, hosted on Cloudflare Pages); shared in chat by Juan Torres and Patrick; includes Interactive Notebook LM link
- **Privacy.com** — Jake Maymar shared link in chat for virtual card/API spend capping service
- **San Diego Machine Learning Group (Meetup link)** — Juan Torres shared in chat; hybrid online/in-person group covering ML case studies

## decisions

- **Patrick Chouinard** will post the question thread earlier before future calls to give members more time to submit questions
- **Morgan Cook** will share his multi-tenancy/Supabase conversation notes in the school meeting notes (after cleaning them up) for Paul Gallovich and Shah Martinez
- **Patrick Chouinard** will post his GitHub profile link in the community for members who want to follow his public repositories
- **Ty Wells** will replace FreshBooks with a custom-built invoicing system (project for that evening)
- **Ty Wells** will replace Zendesk/WhatsApp Business ticketing with a custom-built ticketing system (in progress)
- **Mitch** will explore deploying his CSV-to-HTML reporting tool via OpenAI Codex for cloud-based client access, and will update the group
- **Morgan Cook** will continue converting Claude skills to JavaScript once processes are deterministic, and will share the multi-tenancy notes in school
- **Patrick Chouinard** will work on making the documentation publication process (Markdown → Claude-generated website → Cloudflare Pages) more universal and reusable as a template
- **Ana Preciado** will look into the San Diego Machine Learning Group (shared by Juan) for resources on combining classical ML with AI engineering