## general

This coaching call was a weekly group session hosted by Brandon Hancock, covering member project updates, tool demonstrations, and Q&A. The session opened with pre-call conversation between Patrick Chouinard and Marc Juretus about Patrick's deep use of ShipKit templates to automate documentation workflows at his day job, including a fully automated pipeline using GitHub MCP, Jira/Atlassian MCP, and Azure DevOps MCP to create tickets, branches, commits, and pull requests. Patrick also discussed training 100 developers on GitHub Copilot the following week.

Brandon then led the main session, opening with an announcement about OpenAI's Dev Day releases, particularly a new tool called Agent Kit (described as "N8N meets OpenAI"), which he had just recorded a YouTube video about. He walked through its capabilities — easy RAG setup, guardrails, and one-click deployment — while noting its limitation to left-to-right workflows rather than true multi-agent orchestration. The session then moved into round-robin member updates.

Members shared a wide range of projects: Hemal Shah successfully deployed a Google ADK back-office reconciliation app to Cloud Run with a Next.js frontend; Morgan Cook was refactoring a legacy Supabase project away from row-level security; Paul Miller was building a traveling salesman/route optimization SaaS app and had already pre-sold it to a major consumer goods company; Adam presented at a local event using ChatGPT Research and Relay for lead generation; Elijah Stambaugh discussed using ShipKit for non-software project management and a student newsletter personalization project; Ty Wells demonstrated an N8N workflow validator with Gamma-generated slide decks and security badge minting; Al Cole announced he accepted a new role running the global services team at Kong (API gateway company); Alex Rojas got a RAG application running in under an hour using ShipKit; and Mario Polanco, a first-time caller, described consulting work in Mexico integrating AI into tourism and hospitality businesses.

Brandon also addressed ShipKit roadmap questions, including upcoming Windsurf and Claude Code variant rules (converting cursor rules into sub-agents for Claude Code), a future trigger.dev-based background jobs template, and ongoing Windows setup fixes. The session closed with discussion of content strategy for developers trying to market their AI services.

## insights

- **Patrick Chouinard:** ShipKit's value isn't just building the sample app — the templates and prompts are a Swiss Army knife for automating day-to-day work tasks entirely outside the intended use case.
- **Patrick Chouinard:** Forcing AI to challenge you rather than agree with you requires explicitly rewarding pushback in system prompts; AI is trained to be agreeable, so you must override that default.
- **Patrick Chouinard:** GitHub Copilot has an edge over Cursor for Markdown-heavy work because it autocompletes inline within Markdown files, saving tokens and improving writing speed.
- **Brandon Hancock:** The moment you have a well-written prompt, AI can match that bar consistently — the key is creating the good prompt once, then scaling it.
- **Brandon Hancock:** "Let AI train AI" — use AI to critique its own output, update the prompt/template based on that critique, and iterate until quality is high, then scale to hundreds of instances.
- **Brandon Hancock:** Nothing should ever stay only in your head — everything should be written to a file (Markdown) so agents can read and build on it. Cursor is becoming a universal workspace for all knowledge work, not just coding.
- **Brandon Hancock:** OpenAI's Agent Kit is excellent for left-to-right workflow deployment (10/10 on deployment ease) but lacks true multi-agent orchestration; Google ADK is stronger for pure agent work but weaker on deployment.
- **Brandon Hancock:** Row-level security (RLS) in Supabase is high-risk at scale — one edge case can expose or destroy all user data; server-side API endpoints are safer.
- **Brandon Hancock:** To minimize AI development costs, rotate between Cursor, Claude Code, and Windsurf $20/month plans rather than running up a large bill on one platform.
- **Brandon Hancock:** For legacy codebases, adapt the AI docs (rules/instructions) to the actual tech stack rather than the default ShipKit stack — treat it as a continual improvement process.
- **Brandon Hancock:** Claude Code does not support cursor rules; the workaround is converting rules into specialized sub-agents (e.g., a TypeScript agent, a Python agent) that carry those constraints.
- **Al Cole:** When evaluating whether to join a company full-time, the key question is whether AI is central to the business model or merely adjacent — adjacency is a long-term risk.
- **Mario Polanco:** In markets like Mexico, avoid AI buzzwords entirely; focus on outcomes and practical demonstrations, as the terminology creates barriers rather than interest.
- **Brandon Hancock:** Content that performs best is framed as "here's how this helps you achieve your goal" rather than "here's what I'm doing" — the pivot from self-promotion to viewer utility drives growth.
- **Kamal (Joel Wilson):** If unexpected Google Cloud charges appear due to accidental repeated vector store operations, Google support will often remove the charges if you explain the situation.

## qa

**Q (Patrick Chouinard):** Am I allowed to use ShipKit templates in other systems (e.g., as a ChatGPT custom GPT system prompt) as long as they're not made public?
**A (Brandon Hancock):** Yes — once you have the templates, use them however you want personally. A custom GPT keeps the contents hidden, so that's fine. Please also protect them.

**Q (Hemal Shah):** When working with vibe coding on a legacy monolith for bug fixing, are there best practices?
**A (Brandon Hancock):** Adapt the AI docs to the actual project tech stack — tell the AI exactly what database, frameworks, and patterns are in use. Treat it as a continual improvement process: when AI makes a mistake, update the AI docs to prevent recurrence. After 20 iterations the results become dramatically better.

**Q (Hemal Shah):** When hopping between Cursor, Claude Code, and Windsurf using the same underlying model, will output quality be similar?
**A (Brandon Hancock):** Mostly yes, but each platform has unique mechanisms — Cursor uses cursor rules, Claude Code requires sub-agents since it doesn't support rules. ShipKit is actively building variants for each platform.

**Q (Elijah Stambaugh):** Is using Cursor with Markdown files for non-software project management (e.g., project docs, newsletters) a good strategy?
**A (Brandon Hancock):** Yes — the moment you see it automate document generation across multiple files, you'll never go back. You can also connect MCPs for Google Drive, Notion, etc. to make it more powerful.

**Q (Elijah Stambaugh):** For a student newsletter personalization project, could I use MCPs (Google Drive OAuth) instead of Make/n8n to pull teacher content and generate personalized newsletters?
**A (Brandon Hancock):** It's possible, but for simplicity just download the Google Drive folder locally and run it in Cursor. You could have each student as a Markdown file with their learning style, then tell Cursor to generate a custom newsletter for every file in the folder — no automation platform needed at first.

**Q (Elijah Stambaugh):** Should I use the Chat SaaS template or wait for the upcoming trigger.dev background jobs template for my newsletter project?
**A (Brandon Hancock):** Start with the Chat SaaS template now for the Next.js foundation. The trigger.dev template (coming late October/early November) will be the right architecture for background batch jobs like sending 200 personalized newsletters.

**Q (Paul Miller):** What is the general-purpose ShipKit template for when you don't have a specific template?
**A (Brandon Hancock):** It's on the roadmap. The current focus is building all the base archetypes (RAG, SaaS chat, background jobs, LangGraph) first, then expanding. The MCP and rules infrastructure already provides a lot of the foundation.

**Q (Joel Wilson):** What are the honest criticisms or downsides of ShipKit right now?
**A (Brandon Hancock):** Main issues at launch: Docker changed how it handles offline models right before launch, causing a 6-day outage (now fixed); Windows setup instructions have issues (actively being fixed); some deploy videos at the end of the course still need to be recorded. It's a continual improvement product.

**Q (Joel Wilson):** What are the realistic ongoing costs (hidden fees) for running a ShipKit project?
**A (Brandon Hancock):** Core subscriptions are Supabase (~free tier for first projects, $20/month for production), Vercel (~free tier, $20/month for extras), and Cursor/AI development costs. AI development is the biggest variable — going fast can cost $100–$300+ for a full app build; being cost-conscious by rotating between $20/month plans on Cursor, Claude Code, and Windsurf can keep it much lower.

**Q (Alex Rojas):** For deploying the Next.js front end, Railway or Vercel?
**A (Brandon Hancock):** Vercel — it's specialized for Next.js and provides one-click deploy, deployment rollback, analytics, and easy environment variable management. Railway is more generalized and lacks those Next.js-specific benefits.

## tools

- **ShipKit** — Brandon's course/template product; members using it to build RAG apps, automate documentation, and generate prompts
- **GitHub Copilot** — Patrick training 100 developers on it; noted as superior to Cursor for inline Markdown autocomplete
- **Cursor** — Primary IDE used by most members for AI-assisted coding; discussed token costs and rule-based customization
- **Claude Code** — Used by Mitch and Mario; noted as not supporting cursor rules, requiring sub-agents instead
- **Windsurf** — Mentioned as a third IDE option for rotating to stay within $20/month limits; ShipKit adding variant rules for it
- **OpenAI Agent Kit** — Brandon demoed it; described as N8N-meets-OpenAI for left-to-right workflow agents with easy deployment
- **Google ADK (Agent Development Kit)** — Hemal using it for back-office reconciliation; deployed to Cloud Run
- **Google Cloud Run** — Hemal deployed both ADK API server and Next.js frontend here; noted as straightforward with GitHub repo integration
- **Vercel** — Recommended for Next.js deployment; one-click deploy, analytics, environment management
- **Supabase** — Database/auth platform used across multiple projects; discussed RLS risks and branching features
- **N8N** — Ty built an N8N workflow validator tool; also mentioned as a workflow automation platform members use
- **Gamma** — Ty demonstrated it generating a slide deck from N8N JSON; described as "the ElevenLabs of presentations"
- **Jira / Atlassian MCP** — Patrick using it to auto-create tickets as part of documentation pipeline
- **GitHub MCP** — Patrick using it to auto-create branches and pull requests in documentation workflow
- **Azure DevOps MCP** — Patrick using it alongside GitHub and Jira MCPs in his automation pipeline
- **Trigger.dev** — Brandon announced as the next ShipKit template focus for background job processing
- **ChatGPT (with Apps/Canva integration)** — Brandon referenced OpenAI Dev Day demo showing Canva and Zillow embedded in ChatGPT
- **Riverside** — Brandon recommended for auto-generating "magic clips" from long interview/podcast videos
- **Relay** — Adam used it to match leads to LinkedIn profiles and create Google Sheets of leads
- **T3 ENV (T3 OSS)** — Brandon recommended for failing deployments fast when environment variables are missing
- **Vertex AI / RAG Engine** — Alex ran up $700 in unexpected charges using Google's vector store; Brandon warned it's expensive compared to Supabase
- **GPT-5 Codex** — Mitch using it via OpenCode for code implementation; noted as brief but writes good code
- **OpenCode** — Mitch using it as an open-source alternative IDE with GPT-5 Codex
- **HeyGen** — Mario using it for AI avatar cloning for clients
- **Kong** — Al Cole's new employer; API gateway platform with rate limiting, caching, PII masking for AI traffic
- **Langsmith** — Al mentioned it in context of observability, which Kong's gateway also provides
- **Make (formerly Integromat)** — Elijah mentioned using it for newsletter automation workflow
- **Canva** — Mentioned in OpenAI Dev Day demo as embedded app within ChatGPT for pitch deck generation
- **Gemini** — Paul used it to analyze a long video for potential clip segments

## links

- Sam Altman OpenAI Dev Day video — referenced multiple times; Patrick linked it in chat; covers Agent Kit, embedded apps (Canva, Zillow) in ChatGPT
- Gamma 3.0 release — Elijah mentioned Gamma released a major API update recently, elevating it above competitors like GenSpark and Beautiful.ai

## decisions

- **Brandon Hancock** will release Windsurf variant rules and Claude Code sub-agents for ShipKit within two days
- **Brandon Hancock** will build the next ShipKit template using trigger.dev for background jobs, targeting late October/early November release
- **Brandon Hancock** will fix Windows setup instructions for ShipKit (actively in progress with developer Prem's help)
- **Brandon Hancock** will add remaining deploy videos (domain purchase, Mailgun setup, etc.) to ShipKit course
- **Brandon Hancock** will add a UI padding fix to the ShipKit backlog based on Tom Welsh's OCD report about misaligned buttons on multi-line lesson titles
- **Brandon Hancock** will DM Joel Wilson with additional ShipKit information and resources after the call
- **Hemal Shah** will email Brandon at brandon@shipkit.ai to reconcile his two different email addresses for ShipKit and the marketing platform course access
- **Hemal Shah** offered to contribute Cloud Run deployment documentation or assistance to ShipKit if Brandon wants to add it as a deployment option
- **Patrick Chouinard** will explore creating a custom GPT powered by a ShipKit template to handle the planning phase without burning Cursor tokens
- **Alex Rojas** will contact Google support to request removal of the unexpected $700 Vertex AI vector store charges
- **Al Cole** will drop his LinkedIn profile in the group chat so members can reach out for help or referrals
- **Paul Miller** will record a video of showing his CTO the app he built in a week and share it with Brandon
- **Mario Polanco** will attend the next ShipKit-specific coaching call to get deeper into Claude Code usage questions