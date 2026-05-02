## general

This was a group coaching call hosted by Brandon Hancock, featuring roughly a dozen participants sharing project updates, wins, and technical questions. The session opened with Brandon demoing OpenAI's new "Atlas" browser agent and announcing upcoming Claude Code improvements for ShipKit users, including custom commands, shortcuts, and a cheat sheet to make Claude Code feel more like Cursor.

Participants took turns presenting: Ty Wells showed a live demo of his custom interactive presentation software (with real-time Q&A, polls, screen sharing, and an AI chat interface); Mitch shared birthday reflections on work-life balance and a planned move to Vegas to accelerate a project; Paul Miller reported a major business opportunity after a competitor imploded in Australia; Patrick Chouinard described an enterprise AI platform aggregating 12+ tools going live in a week, plus a concept for a reimagined two-panel AI chat UX with autocomplete; and Garron Selliken joined for the first time, sharing his background in real estate coaching and early vibe-coding progress.

Additional discussions covered LLM cost comparisons (Claude Code $100/$200 plan vs. Cursor), MCP server use cases (Playwright, Asana, Linear, Supabase, Notion), background job processing tools (Trigger.dev vs. Moshia.dev), long-term Next.js maintenance concerns, contract negotiation tips using AI, and a deep dive into agent-to-agent (A2A) protocol adoption strategy. The call closed with Mitch sharing a prompt engineering insight: giving all agents in a pipeline the same large master prompt (60 pages) with only the task varying produced better outputs than siloing context per agent.

## insights

- **Brandon:** Claude Code's $100/month plan is currently the best cost-per-output deal for heavy coding workloads — billing is per runtime, not per token, making Haiku and Sonnet equivalent in cost but different in speed/quantity.
- **Brandon:** Claude Code is ~4x cheaper than Cursor for equivalent work; the $200 Max plan makes it even more favorable for power users who already subscribe.
- **Mitch:** Zed (agentic coding tool) passes tests but uses ~2x the tokens for the same task — token efficiency matters when stretching dollars.
- **Brandon:** MCP servers reduce agent context overhead and error surface: the agent treats the tool as a black box (21 pre-built Playwright actions) rather than dynamically generating code, debugging environments, and handling HTTP error codes.
- **Brandon:** Playwright via MCP can be used mid-development to take screenshots of competitor sites, then feed those screenshots into the agent to restructure your own landing page sections — a practical shortcut.
- **Mitch (via Asana MCP):** Connecting an MCP to a project management tool lets an agent auto-draft client update emails from task data, saving roughly an hour per client per week.
- **Patrick:** Large enterprise orgs are all solving the same problem right now — AI tools built in silos, no discoverability, constant context switching. Aggregating them into one platform with a navigation agent is a high-value near-term opportunity.
- **Patrick:** Using a nano model for autocomplete in a prompt composer (left panel) + a large model for response (right panel) is a natural UX improvement that none of the major AI chat tools currently offer.
- **Brandon:** For SaaS sales, work two planes: lateral (find copies of your existing customer) and upstream (find the one person who serves 500 of your target customers). The upstream move unlocks distribution at scale.
- **Brandon:** When analyzing contracts with AI, framing the prompt as "you are my dad, I'm your son, you're a software contract expert" produces more protective, plain-language breakdowns than a generic legal prompt.
- **Mitch:** In content-creation agent pipelines, giving every agent the full 60-page master prompt with only the task varying outperformed siloing context per agent — continuity and rule adherence improved significantly.
- **Brandon:** For A2A protocol adoption strategy: be an early content creator now, then go deep again at version 1.0 release — that's the catalyst moment when search volume and enterprise adoption will spike.
- **Ty:** When vibe-coding without a software background, always read what the agent says it's about to do before approving — skimming and approving blindly is the primary cause of unwanted rewrites.
- **Patrick:** Proper Git commits and SDLC discipline are the safety net that non-engineers miss most — save points allow reverting when AI goes off the rails.
- **Brandon:** Prefer larger, more established libraries (e.g., Supabase over Mistral for storage) when building set-it-and-forget-it products — smaller/newer tools have more breaking changes.

## qa

**Q (Marc Juretus):** What is the benefit of using a Playwright MCP server (via Docker) versus just having the IDE write Playwright code directly?

**A (Brandon Hancock):** The MCP server gives the agent access to 21 pre-built, tested tool calls for common browser interactions. The agent doesn't need to understand Playwright's code, write it, hope the environment is configured correctly, or debug it. It just calls the tool. This is faster, uses less context, and is far less error-prone than dynamic code generation for every scraping task.

---

**Q (Prem):** Why use Next.js server actions instead of API routes for most server-side logic?

**A (Brandon Hancock):** Server actions give you better type safety (the function signature tells you exactly what goes in and comes out), skip JSON serialization/deserialization, and eliminate the need for ZOD validation on both ends, authentication checks, authorization checks, and multiple HTTP error code handlers. API routes are reserved for external services or things you intend to expose externally.

---

**Q (Prem):** Any tips on how to get more customers for a SaaS application when you're new to sales?

**A (Brandon Hancock):** Work two planes. First, lateral — find two or three people who are copies of your existing customers. Second, upstream — find the one person (aggregator, association, platform) who already serves 500 of your target customers. Once you find those first few manually, you'll naturally detect the pattern that points you upstream. Combine this with reading *Software as a Science* (chapters 3–7) for the full funnel from awareness to sales scripts.

---

**Q (Alex Wilson):** How do you handle long-term maintenance of a Next.js app — breaking changes, vulnerabilities, deprecations?

**A (Brandon Hancock):** Three layers: (1) Sentry for real-time error alerting and uptime health checks; (2) GitHub CVE reports for package vulnerabilities, usually a minor version bump every few months; (3) deprecation notices from Vercel/Node with plenty of lead time. Major paradigm shifts (like pages → app router) happen rarely and usually come with migration CLIs. One afternoon every two to three years is a realistic maintenance burden for a stable stack.

---

**Q (Elijah):** Can you explain the difference between Claude Code instructions, agents, and commands, and how they interact?

**A (Brandon Hancock):** A full answer is coming in four new ShipKit video modules (releasing Thursday morning). The cheat sheet on making Claude Code feel like Cursor will be free to everyone; the deeper agent templates, commands, and workflows will be inside ShipKit. Review the modules first and flag anything that's still unclear.

---

**Q (alroj / Alex):** Which agent-to-agent protocol do you think will win — Google A2A, MCP, or something else?

**A (Brandon Hancock):** Google's A2A is the one everyone references, but it hasn't hit v1.0 yet and search volume is currently flat. The real catalyst will be when a major agent framework (LangGraph, CrewAI, AgentKit) fully adopts it, triggering network effects. OpenAI's distribution (800M weekly users) means whoever they endorse will likely dominate. A2A could also become invisible infrastructure like HTTP — only ~200–300 specialists ever implement it at the framework level, and then everyone else just uses it without knowing.

## tools

- **Atlas (OpenAI browser agent):** New Mac-only agent mode in ChatGPT that can interact with websites and automate browser tasks; Brandon demoed it pausing a timer on a site.
- **Claude Code:** Anthropic's CLI coding agent; discussed extensively as the best cost-per-output tool for heavy development, with $100/$200 plan billing per runtime.
- **Cursor:** AI-powered IDE; compared to Claude Code on cost and ease of use; now includes Playwright as a built-in auto-suggested feature.
- **ShipKit:** Brandon's product — a template/prompt/workflow kit for building SaaS apps; new Claude Code modules and commands being added.
- **Playwright (MCP server):** Browser automation tool; discussed both as an MCP server (via Docker) and as a built-in Cursor feature for screenshots and debugging.
- **Sentry (sentry.io):** Error monitoring and uptime alerting platform; recommended for post-deployment issue detection on Next.js apps.
- **Trigger.dev:** Background job and agent workflow platform (12.6K GitHub stars); recommended by Brandon as a more AI-friendly alternative to Moshia.dev for long-running async tasks.
- **Moshia.dev (Motia.dev):** Lightweight task queue / background job tool with streaming updates and observability dashboard; Morgan Cook shared it as a discovery.
- **Asana (MCP):** Project management platform; Mitch uses its MCP to auto-generate client update emails from task data.
- **Linear:** Project management tool; mentioned as one of Brandon's regularly used MCP servers.
- **Supabase:** Database/backend platform; mentioned as a stable, large-library choice and as an MCP server Brandon uses.
- **Notion:** Note-taking/wiki platform; mentioned as one of Brandon's MCP servers.
- **Google A2A (Agent-to-Agent protocol):** Google's open protocol for inter-agent communication; discussed as the leading candidate for agentic commerce but not yet at v1.0.
- **AgentKit (Coinbase):** Agent deployment framework; praised for extremely easy deploy flow compared to ADK.
- **Google ADK (Agent Development Kit):** Google's agent framework; noted as cheap and easy to build with but difficult to deploy and evaluate.
- **LangGraph / LangChain:** Agent orchestration frameworks; mentioned as having full build-deploy-evaluate pipelines but high pricing.
- **CrewAI:** Agent framework; mentioned alongside LangGraph as having deployment pipelines.
- **Manus:** AI agent platform specializing in task decomposition and artifact storage; Brandon suggested Mitch try it for the 60-page prompt pipeline problem.
- **N8N:** Visual workflow automation tool; mentioned as a comparison point for agent orchestration.
- **GitHub Copilot (with IntelliJ/JetBrains):** Marc is preparing a workplace demo using Copilot instructions and project requirements files to build apps from scratch.
- **Docker Desktop:** Used by Marc to run the Playwright MCP container when the GitHub-sourced MCP server failed.
- **Notebook LM:** Google's document Q&A tool; Morgan referenced it as an analogy for large-context multi-document prompting.
- **VS Code:** Open-source editor; Patrick noted it could be stripped of dev features to serve as the base for a prompt-composer text editor.
- **Zed:** AI coding editor; Mitch noted it passes tests but uses ~2x tokens versus Claude Code for the same task.
- **Codex (OpenAI):** Coding agent; Mitch noted it is less verbose than Claude and uses fewer tokens.
- **Whisperflow:** Transcription service; Brandon mentioned it as the basis for an upcoming Trigger.dev demo project.
- **Vercel:** Deployment platform; mentioned in context of Node.js deprecation notices and Next.js hosting.

## links

- **Google A2A GitHub repository:** Referenced during the A2A protocol discussion — Brandon pulled it up live to check version status (not yet v1.0). (URL not explicitly stated but implied as the official google/A2A repo.)
- ***Software as a Science* by Dan Martell:** Book recommended multiple times for SaaS sales funnels, traffic, and pipeline strategy — chapters 3–7 specifically called out.
- ***E-Myth* by Michael Gerber:** Referenced by Brandon as inspiration for ShipKit's systematized approach; Garron confirmed he had read it.
- ***The Singularity Is Near* by Ray Kurzweil:** Mentioned by Garron as a long-time influence on his thinking about AI.
- **Gosu Coder benchmark results:** Mitch referenced a custom agentic coding benchmark (posted in chat) that tests multi-file changes across platforms including Zed and Claude Code.
- **Sentry.io:** Mentioned as the error monitoring tool; Brandon referenced the URL directly.
- **Trigger.dev:** Brandon pulled up the GitHub repo live, noting ~9K stars (he initially said 12.6K, then corrected to ~9K on screen).

## decisions

- **Brandon Hancock** will release a Claude Code cheat sheet (free to all) and four new ShipKit video modules covering commands, agents, and templates — targeting Thursday morning release.
- **Brandon Hancock** will record a one-year reflection video on leaving his job, going through Crew, and launching ShipKit.
- **Mitch** will move from Idaho to Las Vegas on Thursday to work directly with Debris (Drew) and accelerate their shared project.
- **Patrick Chouinard** will message Brandon after the call to discuss how to legitimately use ShipKit prompts within his client's CI/CD pipeline for documentation generation.
- **Brandon Hancock** will explore adding a contribution/sharing mechanism inside ShipKit so members can share custom prompts and commands with each other.
- **Morgan Cook** will evaluate both Moshia.dev and Trigger.dev and report back to the group on which better fits his use case.
- **Mitch** will try using Manus to tackle the 60-page master prompt pipeline problem and report findings.
- **Brandon Hancock** will use Claude Code parallel tasks to manually prototype the 60-page prompt pipeline (save artifact one, two, etc.) before attempting to automate it.
- **Alex Wilson** will reach out to "Al" (a previous call participant who mentioned a new position) via LinkedIn to explore potential job opportunities.
- **Prem** will read *Software as a Science* (just ordered/delivered) and apply it to his SaaS go-to-market strategy.
- **Garron Selliken** will purchase ShipKit to support his real estate coaching app development.
- **Patrick Chouinard** will report back next week on the enterprise AI platform go-live.