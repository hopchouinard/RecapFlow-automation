## general

This was a weekly coaching/community call facilitated by Patrick Chouinard, with Ty Wells as a regular co-host. The session covered updates from several members on their ongoing projects, a live demo, and substantive discussion on agentic development workflows, tooling, and business strategy.

Patrick opened with updates on two fronts: the packaging of a "community brain" RAG system built on community call transcripts (using a vector DB, retrieval server, Open Web UI, and Ollama), and his evolving dual-tool workflow using both Claude Code and OpenAI Codex in tandem — using Codex as a red-teaming and validation layer against Claude Code's output. He also noted regulatory context: a Quebec financial regulator (AMF) is requiring auditability and provenance tracking of AI/NLP artifacts by May 2027, which is driving his firm's internal SDLC for natural language artifacts.

Ty Wells demonstrated two tools he built: a "feedback hub" enabling user-driven development (screen recording, narration, network capture, AI-assisted clarification, and PR generation), and a new testing package called "Isotope" that logs UI state, database state before/after changes, and screenshots to enable full-stack test visibility. Morgan Cook shared progress on a digital signage system for lobby displays, built on Raspberry Pi and Amazon Fire Stick hardware, using HTML/SVG slides generated from raw content inputs. Elena demoed a multi-cloud disaster recovery planning agent system powered by AWS Bedrock and Strands, capable of ingesting AWS infrastructure and GitHub repos, performing criticality assessments, and generating cross-cloud DR plans with semantic service mapping.

The latter portion of the call included Hemal Shah asking about tools for a social media automation pipeline and email agent workflows, and Elijah Stambaugh discussing how to approach AI consulting engagements with SMBs — covering process documentation, ERP replacement, and change management. The call closed with a detailed Q&A on Claude Code agent architecture, skills, MCP servers, Superpower plugin, and Playwright for UI testing.

## insights

- **Use different AI providers for validation**: When doing security or code review, avoid evaluating the output of a model with the same model — different providers have different biases, so what's invisible to one may be visible to the other (Patrick Chouinard).
- **Codex as a red-teaming harness**: Running Codex as an adversarial validator against Claude Code output — with explicit prompts to "destroy the application" — produces detailed failure reports that can be fed back into Claude Code for remediation (Patrick Chouinard).
- **Codex includes GPT Image 2 in the $20/month subscription**: Image generation can be part of an agentic workflow in Codex without additional API costs, unlike Claude Code which requires a separate API call (Patrick Chouinard).
- **Don't download skills from external sources**: Supply chain attacks on AI tooling have increased; recreate skills from reference rather than downloading them, especially in regulated environments (Patrick Chouinard).
- **Split agent responsibilities by context, not by human work logic**: Agents should have a single main goal; giving an agent two opposing objectives creates unstable, unpredictable results. It's acceptable for one agent to have more work than another (Patrick Chouinard, Morgan Cook).
- **Ask AI to generate code that generates artifacts, not the artifacts directly**: When Morgan asked an LLM to draw a circle on a map, it produced an "amoeba"; asking it to write JavaScript to draw the circle produced a perfect result. AI knows what correct code looks like better than it knows what a correct image looks like (Morgan Cook).
- **Use deterministic scripts for repeatable processes**: Once AI has helped identify and design a process, have it generate a script that runs without AI involvement — faster, cheaper, and more reliable for stable workflows (Morgan Cook).
- **AI amplifies broken processes**: Applying AI to a poorly defined process exposes and accelerates the problems rather than fixing them. Process cleanup must precede AI integration (Morgan Cook).
- **Vertical slicing over horizontal layering in development**: Build features end-to-end (back to front) rather than completing all database work before UI work — this confirms connectivity, avoids wasted tokens, and surfaces integration issues early (Ty Wells).
- **Intentionally leaving bugs can force user adoption**: Ty Wells deliberately left known bugs in his ERP replacement to force employees to actually use the new system and report issues, since they would otherwise default to the legacy system while it remained available.
- **Use `/slash goal` in Claude Code for long-running autonomous tasks**: The new `/goal` command runs until a testable outcome is achieved — potentially for hours or days — but is a significant token consumer (Patrick Chouinard).
- **Use `/insights` in Claude Code** to get a report on how you've been using the tool and suggestions for improving your workflow (Patrick Chouinard).
- **Superpower plugin covers the full SDLC**: Brainstorming → spec → implementation plan → sub-agent spawning → code review, all in one plugin available in the Anthropic marketplace, compatible with both Claude Code and Codex (Patrick Chouinard).
- **Skills in Claude Code are invoked via natural language**: You don't need to explicitly call a skill; Claude infers when to use it based on context. Skills live in a `.claude/skills` folder at the project or profile level (Patrick Chouinard).
- **For enterprise AI consulting, target medium-sized companies making the jump to enterprise infrastructure**: Large enterprises use PwC/Deloitte and equate low cost with low quality; startups lack budget. The sweet spot is companies scaling rapidly who need DR, SLAs, and proper infrastructure but lack internal expertise (Patrick Chouinard).
- **Identify "boots on the ground" employees as AI champions**: Frontline employees know exactly what's broken and what would help. Finding and empowering these people is more valuable than top-down framework adoption (Ty Wells).

## qa

**Q (Biggi Fraley):** Have you compared Plan mode between Codex and Claude?
**A (Patrick Chouinard):** I don't use their plan mode — I use Superpower, which calls it "brainstorming." It goes deeper than standard Plan Mode without the token consumption of Ultra Plan, and it works in both Codex and Claude Code.

**Q (Ty Wells):** I thought I saw a video on running Claude inside of Codex — you said you're running them separately?
**A (Patrick Chouinard):** It's actually Codex inside Claude. Codex has a plugin for Claude, but it's limited to specific things like adversarial code review. I built my own complete harness of prompts that I use at every step of the SDLC.

**Q (Patrick Chouinard):** What's your differentiator between your digital signage app and the vast majority of digital wall applications?
**A (Morgan Cook):** Garbage in, beauty out. The goal is to take whatever raw content someone provides — even a photo of a paper poster — and automatically reformat it into a beautiful, animated, expiring slide with QR codes and countdown timers, without manual design work.

**Q (Ty Wells):** Are you deploying the Fire Stick app directly to the device, through ADB, or putting something in the Amazon store?
**A (Morgan Cook / Ty Wells):** Morgan was planning to go direct to device, but Ty warned that newer Fire Stick models (beyond plain HD) don't allow sideloading — you'd need to publish to the Amazon Appstore. Ty also warned not to use "Fire" in the product name, as Amazon requires notarized documents and may still block approval.

**Q (Hemal Shah):** Is there any recommendation on tools for building a social media content automation pipeline?
**A (Patrick Chouinard):** Consider the Claude Agent SDK rather than building a standalone Python app. You can either self-host it or use Anthropic's managed agent option. Since the workflow is multi-step with approvals, use it as a full agent rather than a one-shot prompt — otherwise just use any inference platform.

**Q (Hemal Shah):** How have you configured your email agent?
**A (Patrick Chouinard):** I don't fully automate email replies — the 0.1% failure case is too risky. Instead, I feed received emails to Claude via mailbox connectors, add context, and have it draft a reply. I write my raw (sometimes blunt) response and Claude reformulates it to be politically correct while preserving the message.

**Q (Hemal Shah):** How do you use project tracking alongside AI-assisted development?
**A (Patrick Chouinard):** We use Jira with a layer on top via Superpower. We split incoming Jira requests into independent vertical work streams, feed each into Superpower's brainstorming step, go through spec → implementation plan → sub-agent implementation, with Codex validation injected at each phase. Jira tickets are updated automatically at each step via the Atlassian MCP server.

**Q (Elena):** For the disaster recovery tool, is the ideal customer enterprise or startup?
**A (Patrick Chouinard):** Medium-sized companies making the jump to enterprise infrastructure are the best fit. Large enterprises use consulting firms like PwC or Deloitte and won't consider a low-cost SaaS. Startups that are scaling rapidly — identifiable by public announcements of growth — need exactly this kind of guidance and are willing to pay for it.

**Q (Elena):** What is a Claude Code agent, and how does the sub-agent model work?
**A (Patrick Chouinard):** A Claude Code session is itself called an agent. When implementing, it can spawn sub-agents — separate processes with their own fresh context windows — that inherit only the context needed for their specific task. This avoids filling the main context window and keeps each sub-agent focused. Skills and MCP connectors are available to all agents.

**Q (Elena):** Where can I find good templates or starting points for skills?
**A (Patrick Chouinard):** Don't download skills from external sources due to supply chain risks. Instead, use the built-in skill creator skill in Claude Code: after completing a process, tell Claude Code to "look at what we just did and create a skill from it." It will generate the proper structure and syntax. Run `/insights` to see how you've been using Claude and what to improve.

**Q (Elena):** Can Playwright MCP run tests against a locally running app?
**A (Patrick Chouinard):** Yes. Install the Playwright MCP server, provide the localhost URL, and Claude can instruct Playwright to spawn a browser, navigate the UI, and execute tests — all locally, without you doing it manually.

## tools

- **Claude Code** — Primary agentic coding harness used by most participants; discussed throughout for spec-driven development, sub-agent spawning, and SDLC workflows.
- **OpenAI Codex** — Used by Patrick as a parallel validation and red-teaming layer alongside Claude Code; also noted to include GPT Image 2 in the $20/month subscription.
- **Superpower (plugin)** — Claude Code/Codex/GitHub Copilot plugin covering full SDLC: brainstorming, spec, implementation plan, sub-agent orchestration, code review; listed in Anthropic's official marketplace.
- **Open Web UI** — Frontend interface being packaged as part of Patrick's community brain RAG system.
- **Ollama** — Local LLM runner included in the community brain deployment stack.
- **Supabase** — Database backend used by Ty Wells for his projects; Isotope testing package integrates with it to log DB state changes.
- **Isotope** — Ty Wells's custom testing package that captures UI screenshots, DB state before/after, and endpoint logs for full-stack test visibility.
- **AWS Bedrock** — Inference backend powering Elena's multi-cloud DR agent system.
- **Strands (AWS)** — Agentic framework used by Elena as the orchestration layer for her DR planning system.
- **AWS Amplify** — Frontend hosting for Elena's DR POC (Next.js dashboard).
- **MCP (Model Context Protocol) servers** — Connectors used throughout: AWS MCP, GCP MCP, Atlassian MCP, Playwright MCP mentioned specifically.
- **Playwright MCP** — Used for UI testing; Claude Code instructs it to spawn a browser and execute tests against a local or remote app.
- **GitHub Copilot** — Used at Patrick's corporate environment as a substitute for Codex; same Superpower principles applied.
- **Raspberry Pi** — Hardware platform Morgan Cook used for his digital signage engine prototype.
- **Amazon Fire Stick (HD model only)** — Cheaper alternative hardware for digital signage; Ty Wells warned newer models don't support sideloading.
- **Vercel** — Mentioned as a hosting platform for Morgan's signage backend and Ty's DeepSeek-Claude redirect tool.
- **Trigger.dev** — Mentioned by Morgan as a potential backend for heavy-lifting tasks in his signage automation pipeline.
- **Jira / Atlassian** — Project tracking system used at Patrick's firm; updated automatically via Atlassian MCP server at each SDLC step.
- **Linear** — Mentioned as a lightweight alternative to Jira for project tracking; Ty Wells uses a custom "feedback hub" instead.
- **Odoo** — ERP system Ty Wells replaced with his custom-built solution; provided ~60% of needed functionality.
- **ERPNext** — Open-source ERP framework evaluated by Elijah Stambaugh as a potential foundation for client work.
- **DeepSeek** — Used by Ty Wells as a fallback when Claude goes down; configured via API redirect so Claude Code routes to DeepSeek's endpoint.
- **GPT Image 2** — Image generation model available within Codex subscription; Patrick noted it can generate images as part of an agentic workflow.
- **Gemini CLI** — Mentioned as an open-source harness built around Google's Gemini models.
- **OpenCode** — Mentioned as an open-source agentic harness that accepts any model as input.
- **Kindle Direct Publishing (KDP)** — Used by Morgan Cook to help publish a book; formatting assistance was the main challenge.
- **Google Workspace / App Scripts** — Morgan Cook's current automation target for a client; writing App Scripts to automate manual workflows in Gmail, Drive, and Sheets.
- **CrowdPix** — Ty Wells's existing digital signage/display product; available at crowdpics.ai.

## links

- **https://crowdpics.ai** — Ty Wells's digital signage/display product (formerly "Fire Photo"), shared as reference for Morgan Cook's similar project.
- **https://deepseek-claude-code.vercel.app** — Instructions/tool for configuring Claude Code to redirect API calls to DeepSeek as a fallback when Claude is unavailable.
- **https://github.com/obra/superpowers** — Superpower development methodology plugin repository, shared by Fitz in chat.
- **https://fathom.video/customize** — Fathom AI notetaker settings link (auto-posted by Fathom bot).

## decisions

- **Patrick Chouinard** will finish packaging the community brain RAG system this week and aim to have it ready for sharing by next week, including source material, pre-chunked data, and an install.md for agent-assisted deployment.
- **Patrick Chouinard** will manage next week's call in Paul's absence.
- **Patrick Chouinard** will search for and post links to security skill repositories (from security companies) in the community for members to evaluate.
- **Ty Wells** will share instructions for configuring Claude Code to use DeepSeek as a fallback (posted to chat during the call: https://deepseek-claude-code.vercel.app).
- **Ty Wells** will package the "Isotope" testing tool for reuse across projects and make it available to the group.
- **Ty Wells** will connect with Morgan Cook offline to share lessons learned from building and deploying CrowdPix on Amazon Fire Stick hardware.
- **Ty Wells and Elijah Stambaugh** agreed to connect offline to discuss Ty's custom ERP build, stack details, and approach to replacing Odoo.
- **Morgan Cook** will look into acquiring older (plain HD) Amazon Fire Stick units via eBay before they become unavailable, based on Ty's sideloading warning.
- **Elena** will install Superpower in Claude Code and use `/insights` to evaluate and improve her current workflow.
- **Elena** will continue refining the DR planning system, focusing on multi-cloud support, cost estimation accuracy, and adding DR testing via AI agents.
- **Hemal Shah** will evaluate the Claude Agent SDK (managed agent option) as the backend for his social media automation pipeline instead of a standalone Python app.