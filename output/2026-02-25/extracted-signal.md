## general

This coaching call brought together a regular group of AI-developer practitioners led by Brandon Hancock, who had been away and returned with updates. The session opened with informal pre-call conversation among Marc Juretus, Patrick Chouinard, and Ty Wells discussing their current projects, OpenClaw security setups, and AI tooling costs before Brandon joined.

The bulk of the call followed a round-robin format where members demoed projects and received feedback. Jaylen Davis showed a content-creator monetization platform where fans fund video requests. Marc Juretus demonstrated a fitness tracking app with voice-dictated workout logging and a stock-market education app. Patrick Chouinard walked through a personal CV/portfolio site with a custom CMS and AI-powered bilingual content generation. Scott Rippey presented "Code Anvil Mobile," a mobile-friendly Claude Code interface secured via Cloudflare tunnel. Ty Wells introduced a formal verification layer for AI output aimed at reducing hallucinations and enabling long-running autonomous agents. Morgan Cook showed a cemetery management system with D3-based hierarchical plot visualization and Freedom of Information Act compliance features.

Recurring themes included OpenClaw security architecture, the right tool for the right task (Claude Code vs. Codex vs. Gemini), how to structure AI agent permissions, and the business opportunity window that currently exists for AI-native developers. The call closed with an extended discussion on the future of work, agent orchestration, and the urgency of acting now before the market matures.

A separate thread ran through the call on productivity philosophy: Brandon described measuring his day by "tokens generated per hour" and using a Meta Quest 3 headset to run 15 simultaneous Claude Code instances, framing the current moment as a once-in-a-generation opportunity comparable to the early internet or mobile era.

## insights

- **Brandon:** The limiting factor for AI output is no longer the AI — it's human input speed. Measure productive days by how often you are actively generating tokens, not by hours worked.
- **Brandon:** Codex (OpenAI) outperforms Claude Code for long-running, high-precision tasks like generating 90-slide PowerPoint decks; Claude Code is better for rapid iterative feature work.
- **Brandon:** Gemini offers the best capability-to-cost ratio for production applications where token costs matter; avoid running Opus-class models on high-frequency background tasks.
- **Patrick:** Give OpenClaw its own isolated machine, its own email (with a rule to only read mail from your address), its own calendar, and its own GitHub account — treat it exactly like a human contractor with scoped permissions.
- **Patrick:** Use Discord channels to split agent context windows by topic, preventing enormous token payloads on every exchange.
- **Patrick:** Reducing the unit cost of work doesn't reduce the volume of work — it expands the set of use cases that become economically viable, increasing total demand rather than eliminating jobs.
- **Brandon:** When building for AI agents, a structured SOP database is as important as the code itself; agents need SOPs the same way human employees do.
- **Brandon:** The highest-leverage activity right now is not coding — it is identifying the correct business problem to solve. Use AI to model multiple monetization paths before writing a line of code.
- **Morgan (insight surfaced by Brandon):** Boring, legacy-software niches (cemeteries, compliance, government records) are ideal targets because competitors are developing as if it's 2015 and have no AI advantage.
- **Brandon:** A compliance requirement (FOIA, HIPAA, SOC 2) that competitors haven't solved is a moat, not just a cost — it locks customers in and raises the barrier to entry.
- **Morgan:** When AI struggles to produce a correct structured document directly, ask it to write a *function* that generates the document instead — the function will be accurate even when the direct output is not.
- **Patrick:** Spread parallel AI workloads across multiple subscriptions (Claude, Gemini, Codex/GPT) to avoid exhausting any single token budget; assign each tool a distinct type of work.
- **Brandon:** Don't use the Claude Code VS Code extension terminal — open a native terminal in the editor pane and run `claude` from there for full feature access.
- **Ty:** GitHub Actions can be used to run formal verification checks automatically on every commit, catching semantic errors that syntactic checks miss.
- **Brandon:** The people who can orchestrate agents and design AI systems will become the scarcest and most valuable resource as junior-level work disappears.

## qa

**Q (Darryl Goldstein):** Is OpenClaw running on a Mac Mini?
**A (Patrick Chouinard):** No, it's a Ubuntu VM running on Proxmox.

**Q (Juan Torres):** How do you manage the relationship between OpenClaw and resources like a database inside a VPC without it accidentally deleting things?
**A (Patrick Chouinard):** Run it in an isolated VM or Docker container — it doesn't need significant resources, just isolation. Avoid paying for a VPS; run it on local hardware. Give it only the permissions it needs and nothing else.

**Q (Juan Torres):** Are you worried about OpenClaw using your home network?
**A (Brandon Hancock):** Not currently, because the scope of what it can access is extremely narrow — it can only read from a specific Slack channel and write to Google Drive. The smaller the attack surface, the lower the risk.

**Q (Rag Ch):** In your videos you seem to be typing in a different terminal than the Claude Code extension terminal — what's the right setup?
**A (Brandon Hancock):** Don't use the Claude Code VS Code extension terminal; it has fewer features. Instead, open a new terminal window inside the editor pane (the coding area, not the bottom panel), then type `c` or `claude` to launch Claude Code. Use keyboard shortcuts to tab between multiple instances.

**Q (Elena, via chat):** Is there a meaningful difference between building a GenAI backend in TypeScript versus Python?
**A (Brandon Hancock):** Python leads the AI ecosystem — most cutting-edge libraries (e.g., Dockling for RAG) are Python-native, and TypeScript wrappers often just proxy to a Python server anyway. Use TypeScript for front-end and general back-end; use Python for AI-specific tasks. With AI assistance, the learning curve for a second language is minimal.

**Q (Elijah Stambaugh):** Claude Code has agent teams that run in tmux — is that a good workflow?
**A (Brandon Hancock):** tmux causes shortcut key conflicts when running Claude Code (an interactive CLI inside another CLI). Warp terminal is a better alternative — it lets you open many split panes with `Cmd+D` / `Cmd+Shift+D` and script the layout on startup.

**Q (Morgan Cook):** For a multi-tenant Supabase app, does each organization need its own Supabase instance for SOC 2 compliance?
**A (Brandon Hancock):** No. SOC 2 auditors don't care about multi-tenancy within a single database instance — they care about your breach response plan and security policies. You just need to upgrade to the HIPAA/SOC 2 compliant Supabase tier (~$600/month) and get a static IP on Vercel (~$100/month). Row-level security handling org separation is a code concern, not a compliance-instance concern.

**Q (Brandon Hancock to Jaylen Davis):** Where's the friction for people who want to fund videos — why can't they give money to YouTubers today?
**A (Brandon Hancock):** It's mostly businesses that have budget to spend on sponsored content but no efficient channel to find and transact with mid-tier creators. The platform could position itself as the deal-maker in the middle rather than a fan-to-creator tip jar.

## tools

- **Claude Code** — Primary coding agent used by most members for rapid iterative development; discussed extensively re: terminal setup and parallel instances.
- **Codex (OpenAI)** — Recommended by Brandon for long-running, high-precision tasks like generating large PowerPoint decks; hooks into Gemini for image generation.
- **Gemini (Google)** — Recommended as best cost-to-capability ratio for production token-heavy workloads; used inside VS Code (Gemini Code Assist / anti-gravity extension).
- **OpenClaw** — Self-hosted autonomous AI agent; discussed at length for security architecture, isolation, and use cases (email triage, calendar management, customer research).
- **Warp** — Terminal application used by Brandon to manage 10–15 simultaneous Claude Code instances with keyboard-driven split panes.
- **Meta Quest 3** — VR headset used by Brandon to project unlimited virtual screens for running many Claude Code instances simultaneously.
- **N8N** — Workflow automation tool; Marc discussed using it for real estate lead-matching flows; debated whether Claude's native capabilities reduce the need for it.
- **Proxmox** — Hypervisor Patrick uses to run the Ubuntu VM hosting OpenClaw.
- **Appify** — Used by Brandon with LinkedIn browse features to do customer research via OpenClaw.
- **Dockling** — Python-native embedding/chunking library for RAG applications; cited as an example of why Python is preferred for AI backends.
- **Vertex AI / Model Garden (Google Cloud)** — Marc used it to spin up a RAG instance and generate images for a clothing site demo.
- **Cloudflare Tunnel** — Used by Scott Rippey to securely expose his local Claude Code instance to his phone via Code Anvil Mobile.
- **Anthropic Agent SDK** — Used by Scott as the backend for Code Anvil Mobile instead of the standard Claude desktop web interface.
- **D3.js (d3-hierarchy)** — JavaScript visualization library Morgan used to build hierarchical cemetery plot diagrams with zoom and radial tree views.
- **Supabase** — Database/backend platform used by Morgan; discussed re: HIPAA/SOC 2 compliant tier pricing (~$600/month).
- **Vercel** — Hosting platform used by Patrick and Morgan; static IP add-on (~$100/month) noted as needed for compliance.
- **Hostinger** — Patrick's hosting provider; Claude Code auto-deploys his static CV site to it.
- **Mermaid** — Diagramming extension in VS Code; Rag Ch asked about zoom functionality (resolved by using the "edit diagram" button in the `.md` file preview).
- **Telegram** — Marc uses it as the interface to send commands to his OpenClaw instance.
- **Discord** — Patrick recommended it over Slack for OpenClaw because channels naturally partition context windows.
- **Grok** — Marc used it to generate exercise demonstration videos for his fitness app.
- **TinySeed / Dan Martell** — Mentioned by Brandon as potential investor contacts for Morgan's cemetery SaaS.
- **Banta** — Compliance/security tooling Brandon's company purchased; mentioned in context of SOC 2 preparation costs.
- **11 Labs** — Voice integration Scott is adding to his Neural Spark internal SaaS for clients.
- **GitHub Actions** — Ty uses it to run automated formal verification checks on code commits.
- **WSL (Windows Subsystem for Linux)** — Morgan switched from PowerShell to WSL to eliminate Claude Code's repeated Linux/Windows syntax errors.

## links

- **My First Million podcast episode featuring Starter Story** — Brandon referenced it as a must-watch for app idea validation via YouTube Shorts before building; no URL provided but described as "the latest My First Million episode."
- **Accelerando (novel by Charles Stross, 2005)** — Brandon and Scott recommended this sci-fi book as a prescient description of the current AI acceleration trajectory, including the concept of "transhumanism."
- **Code Anvil Mobile (GitHub repo by Scott Rippey)** — Mobile-friendly Claude Code interface secured via Cloudflare tunnel and Google OAuth; Scott said he would share the updated link the following day after merging latest changes. No URL captured in transcript.
- **Usai presentation (Ty Wells)** — Ty shared a link to a presentation on his formal verification layer for AI output; attendees were invited to view it directly. No URL captured in transcript.
- **Marc's fitness app** — Marc said he would send Patrick a link during the call. No URL captured in transcript.

## decisions

- **Scott Rippey** will merge the latest Code Anvil Mobile branch and share the updated public GitHub repo link with the group by the following day.
- **Ty Wells and Brandon Hancock** agreed to connect offline on Friday to discuss AI testing frameworks and formal verification approaches.
- **Paul Miller** will text Brandon to schedule a Friday afternoon call to discuss managing multiple simultaneous AI consulting projects efficiently.
- **Brandon Hancock** will share the Claude Code Insights file with the group (Patrick requested it during the call).
- **Marc Juretus** plans to take the Google Generative AI Leader certification exam the following week.
- **Morgan Cook** was strongly encouraged (and implicitly committed) to prioritize the cemetery management SaaS above other projects, get a paying customer within weeks, and then pursue seed investment (Brandon offered to make introductions to TinySeed/Dan Martell once first dollars trade hands).
- **Brandon Hancock** offered to introduce Morgan Cook to his HIPAA/SOC 2 compliance contacts and walk him through the process if Morgan emails him.
- **Jaylen Davis** will take the call recording, feed it into AI to summarize the feedback, and use it to iterate on his creator monetization platform.
- **Brandon Hancock** will report back to the group on his Mac Mini + OpenClaw setup experience over the coming weeks.
- **Marc Juretus** will switch high-frequency OpenClaw tasks (e.g., daily motivator) from Opus to Haiku or Gemini to control token costs.