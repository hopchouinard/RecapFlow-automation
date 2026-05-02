## general

This was a group coaching call led by Brandon Hancock, returning after an absence, with regular members including Patrick Chouinard, Marc Juretus, Ty Wells, Scott Rippey, Morgan Cook, Jaylen Davis, Paul Miller, Rag Ch, and others. The session opened with informal catch-up conversations about members' current projects before Brandon shared updates on his own work, including his use of Meta Quest 3 for running multiple Claude Code instances simultaneously and his use of Codex for PowerPoint generation.

The bulk of the call consisted of member demos and feedback rounds. Jaylen Davis presented a content creator monetization platform where fans fund video requests. Marc Juretus showed a fitness tracking app with voice-dictated workout logging and a stock market education app. Ty Wells introduced a formal verification layer for AI output (renamed to Usai) with a provisional patent, and discussed autonomous long-running agents. Scott Rippey demonstrated "Code Anvil Mobile," a mobile-friendly UI for accessing Claude Code remotely via a Cloudflare tunnel. Morgan Cook presented a cemetery management system targeting government compliance requirements in Utah, which received significant business coaching from Brandon.

Recurring themes throughout the call included OpenClaw security architecture (Patrick's approach of isolated VMs, dedicated email accounts, and GitHub organizations versus Brandon's simpler Slack-only containment), the optimal workflow for running multiple Claude Code instances in parallel, and a broader philosophical discussion about AI's impact on labor markets, the value of agent orchestration skills, and the urgency of building now while competition is low. Brandon recommended the book *Accelerando* as a roadmap for where AI development is heading societally.

## insights

- **Brandon Hancock:** Running multiple Claude Code instances simultaneously in a terminal multiplexer (Warp) rather than inside an IDE editor is the key workflow unlock — the editor becomes a bottleneck when you can only see 2–3 windows at once.
- **Brandon Hancock:** Codex (OpenAI) outperforms Claude Code for long-running, high-precision tasks like generating large PowerPoint decks (90 slides in 30 minutes); Claude Code is better for rapid iterative feature work.
- **Patrick Chouinard:** Giving OpenClaw its own isolated Ubuntu VM, dedicated Gmail account (with a rule to only read email from one trusted address), its own calendar, and its own GitHub organization treats it like a human worker and prevents prompt injection and privilege escalation.
- **Patrick Chouinard:** Using Discord channels to split OpenClaw's context by topic prevents context window bloat and runaway token costs compared to a single long conversation.
- **Brandon Hancock:** OpenClaw/Claude Code should be given a clearly bounded "box" — write to Google Drive or Sheets, never send email directly — so a human-controlled external service can act on the output rather than the AI acting autonomously.
- **Morgan Cook:** When AI struggles to produce a correctly structured document directly, asking it to write a *function* that generates the document often works perfectly — AI knows how to write code better than it knows how to execute multi-step reasoning in natural language.
- **Brandon Hancock:** Gemini offers the best capability-to-cost ratio for high-volume, always-on agent tasks; Opus/Claude is expensive for repetitive background jobs like daily motivational messages.
- **Patrick Chouinard:** Spreading parallel work across multiple AI subscriptions (Claude, Gemini, Codex/GPT) with different responsibilities avoids token exhaustion on any single platform.
- **Brandon Hancock:** The highest-leverage activity right now is not coding — it's identifying the right business model. Coding is easy; finding the problem worth solving is the hard part.
- **Brandon Hancock:** "Boring" niche software markets (cemeteries, compliance, legacy industries) are prime targets because competitors are still developing as if it's 2015 and have no AI-assisted development advantage.
- **Patrick Chouinard:** Reducing the unit cost of work doesn't reduce total work — it expands the set of use cases that become economically viable, increasing demand for skilled orchestrators.
- **Brandon Hancock:** Work done in 2025–2026 compounds more than work done in five years because the pool of people who can do this work is still tiny; competition is at its lowest point it will ever be.
- **Scott Rippey:** SOPs are the critical context layer for AI agents — an agent needs both the procedural steps (SOP) and the knowledge base to execute tasks reliably.

## qa

**Q (Darryl Goldstein):** Are you running OpenClaw on a Mac Mini? What hardware are you using?
**A (Patrick Chouinard):** It's a Ubuntu VM running on Proxmox. It doesn't need significant resources — isolation is what matters, not compute power. Running it on a local VM or even Docker Desktop costs nothing compared to a VPS.

**Q (Juan Torres):** How do you manage the relationship between OpenClaw and resources like a database inside a VPC without it accidentally deleting things?
**A (Patrick Chouinard / Brandon Hancock):** Patrick runs it in an isolated VM with no direct database access; Brandon limits it to reading from a Slack channel and writing to Google Drive/Sheets only, with no ability to send email or take external actions. The principle is: give it the smallest possible surface area and have a human-controlled external service act on its outputs.

**Q (Rag Ch):** In your videos you seem to be typing in a different terminal than the Claude Code extension terminal — what's the right setup?
**A (Brandon Hancock):** Don't use the Claude Code VS Code extension terminal — it has fewer features. Open a regular terminal inside the editor pane (not the bottom panel), type `c` to launch Claude, and use keyboard shortcuts to navigate between multiple instances. Brandon has since moved entirely to Warp terminal for this workflow.

**Q (Elena, via chat):** Is there a difference between building a GenAI backend in TypeScript versus Python?
**A (Brandon Hancock):** Python leads the AI ecosystem — most cutting-edge libraries (e.g., Dockling for RAG/chunking) are Python-native, and TypeScript wrappers often just proxy to a Python server anyway. The practical answer is: use TypeScript for front-end and general back-end, and learn enough Python to handle AI-specific tasks. With AI assistance, the language barrier is shrinking.

**Q (Elijah Stambaugh):** Claude Code has agent teams that run in tmux — is that a good terminal approach?
**A (Brandon Hancock):** tmux has conflicting shortcut keys when running an interactive CLI inside another CLI, which caused issues. Brandon moved to Warp terminal instead, which handles multiple panes cleanly without key conflicts.

**Q (Morgan Cook):** For a multi-tenant Supabase app, does each organization need its own Supabase instance for SOC 2 compliance?
**A (Brandon Hancock):** No — SOC 2 doesn't care about multi-tenancy within a single database instance. You just need the HIPAA/SOC 2 compliant Supabase tier (~$600/month) and a static IP on Vercel (~$100/month). The auditor focuses on breach response procedures, not your data architecture.

**Q (Jaylen Davis, implicit):** What monetization model would work best for a content creator video request platform?
**A (Brandon Hancock):** Consider a monthly subscription model ($50–99/month) where creators pay to host their community and fans vote/request videos, rather than relying on per-transaction revenue. This creates recurring revenue, reduces dependency on individual transactions, and gives creators an incentive to grow their community on your platform.

## tools

- **Claude Code** — Primary coding tool used by most members; Brandon runs 10–15 instances simultaneously via Warp terminal
- **Codex (OpenAI)** — Brandon's preferred tool for long-running, high-precision tasks like generating large PowerPoint presentations; hooks up to Gemini for image generation
- **Meta Quest 3** — Brandon uses it as a virtual multi-monitor setup to run many Claude Code instances simultaneously without being desk-bound
- **Warp Terminal** — Brandon's current terminal of choice for managing multiple parallel Claude Code sessions with keyboard shortcuts
- **OpenClaw** — Autonomous AI agent framework; members discussed security architecture, isolation strategies, and use cases
- **Appify** — Used by Brandon with LinkedIn browse features for customer research and profiling trial users
- **N8N** — Discussed as an orchestration layer for complex flows; noted as cost-effective when self-hosted on a local VM versus paying per-token for Claude
- **Proxmox** — Patrick's hypervisor for running the Ubuntu VM that hosts OpenClaw
- **Vertex AI / Model Garden (Google Cloud)** — Marc used it to spin up a RAG and generate images for a clothing site demo
- **Gemini** — Recommended by Brandon as best cost-to-capability ratio for high-volume agent tasks; also used inside VS Code (Gemini Code Assist)
- **Dockling** — Python-native embedding and chunking tool for RAG applications; mentioned as an example of why Python leads AI tooling
- **Cloudflare Tunnel** — Scott uses it to securely expose his local Claude Code instance to his phone via Code Anvil Mobile
- **Anthropic Agent SDK** — Scott built Code Anvil Mobile on top of it to create a mobile-friendly Claude Code interface
- **D3.js (D3 hierarchy)** — Morgan used it for interactive cemetery plot visualization with zoomable tree diagrams
- **Supabase** — Backend/database used by Morgan for the cemetery management system; HIPAA/SOC 2 compliant tier discussed
- **Vercel** — Hosting platform used by Patrick and Morgan; static IP add-on mentioned for compliance
- **Hostinger** — Patrick's hosting provider; Claude Code auto-deploys his personal site to it
- **Discord** — Patrick uses it for OpenClaw communication, splitting context across channels to manage token usage
- **Telegram** — Marc uses it as the interface to communicate with his OpenClaw instance
- **Mermaid** — Diagramming extension in VS Code; Rag Ch asked about zoom functionality
- **TinySeed** — Early-stage SaaS investor mentioned by Brandon as a potential funding source for Morgan's cemetery app
- **Banta** — Compliance/SOC 2 tooling Brandon's company purchased; mentioned as an example of investment-funded spend
- **11 Labs** — Voice integration Scott is adding to his Neural Spark internal SaaS for clients
- **GitHub Actions** — Ty uses it for automated code verification as part of his formal verification layer

## links

- **Accelerando (book by Charles Stross, 2005)** — Brandon recommended it as a prescient description of AI's societal trajectory, including the concept of "transhumanism"; available publicly
- **My First Million podcast — Starter Story episode** — Brandon referenced a recent episode breaking down app business trends, including the strategy of faking an app on YouTube Shorts to validate demand before building; no direct URL given
- **Code Anvil Mobile (GitHub repo, Scott Rippey)** — Scott's open-source mobile-friendly Claude Code interface built on Anthropic Agent SDK with Cloudflare tunnel; Scott said he would share the updated link the following day after merging latest changes
- **Usai presentation (Ty Wells)** — Ty shared a link to a public presentation on his formal AI verification layer / autonomous agent project; URL not captured in transcript

## decisions

- **Scott Rippey** will merge his latest Code Anvil Mobile changes and share the updated GitHub repo link with the group by the following day.
- **Brandon Hancock** will schedule a call with Ty Wells on Friday to discuss AI testing, reliability, and formal verification approaches in more depth.
- **Brandon Hancock** will schedule a call with Paul Miller on Friday afternoon to advise on managing multiple simultaneous AI consulting projects efficiently.
- **Brandon Hancock** will send Morgan Cook information about HIPAA compliance vendors and offer to introduce him to TinySeed or other investors once Morgan has his first paying customer.
- **Brandon Hancock** will share a Claude Code Insights file with the group (Patrick had requested it).
- **Marc Juretus** plans to take the Google Generative AI Leader certification exam the following week.
- **Jaylen Davis** will record the feedback from the call, transcribe it with AI, and use it to evaluate monetization model changes for his creator platform.
- **Morgan Cook** will prioritize closing his first paying customer for the cemetery management system and then pursue go-to-market outreach to other Utah counties.
- **Patrick Chouinard** will continue developing his personal CV/portfolio site with the admin CMS backend and add more project showcases as subdomains.