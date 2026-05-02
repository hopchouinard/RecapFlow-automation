## general

This was a group coaching call led by Brandon Hancock (returning after an absence) with regular members including Patrick Chouinard, Marc Juretus, Ty Wells, Jaylen Davis, Scott Rippey, Morgan Cook, Paul Miller, Rag Ch, and others. The session opened with informal catch-up conversations about ongoing projects before Brandon rejoined and shared updates on his own work, including using Meta Quest 3 for multi-instance Claude Code sessions and using Codex for PowerPoint generation.

The bulk of the call followed a round-robin format where each member presented their current project or question. Projects demoed or discussed included: Patrick's personal CV/portfolio website with a custom CMS and AI-assisted bilingual content generation; Marc's fitness tracking app with voice-dictated workout logging and a stock market education app; Jaylen's content creator monetization platform; Ty's formal verification layer for AI output (Usai); Scott's mobile Claude Code interface (Code Anvil Mobile) and a Neural Spark internal SaaS build; Morgan's cemetery management system with D3 visualization and Freedom of Information compliance features; and Paul's large-scale AI consulting engagements in Australia/New Zealand.

A significant portion of the call was devoted to OpenClaw (an autonomous AI agent framework) — specifically how members are deploying, securing, and constraining it. Patrick described a highly structured setup using a dedicated Ubuntu VM on Proxmox, a separate GitHub account, isolated Gmail/Google Drive, and Discord for context management. Brandon described a simpler containment approach using Slack and Appify. Security practices around prompt injection, email access, and resource permissions were debated at length.

The call closed with a philosophical discussion about the urgency of the current AI moment — the group compared it to the internet and mobile waves — and Brandon strongly encouraged members, especially Morgan, to move fast on commercializing their work, referencing TinySeed and investor introductions.

---

## insights

- **Brandon:** Running 15 Claude Code instances simultaneously via Meta Quest 3 (virtual screens) is his current productivity setup — humans are the bottleneck, not AI.
- **Brandon:** Codex (OpenAI) outperforms Claude Code for long-running, high-precision tasks like generating 90-slide PowerPoint decks; Claude Code is better for rapid iterative feature work.
- **Patrick:** OpenClaw should be treated like a human employee for security: its own GitHub account, its own email (with a rule to only read mail from one trusted address), its own calendar, its own machine, and its own Google Drive — to prevent prompt injection and scope creep.
- **Patrick:** Using Discord channels to split OpenClaw's context by topic prevents context window bloat and runaway token costs.
- **Brandon:** OpenClaw should be given a strict "box" — only write to Google Drive/Sheets, no email sending capability — to prevent autonomous actions like blasting customers with emails.
- **Patrick:** Running OpenClaw on a local VM (Ubuntu on Proxmox) costs nothing beyond hardware; paying for a VPS monthly for something that needs minimal resources is unnecessary.
- **Morgan:** When AI struggles to produce a structured output (e.g., a GIS map), asking it to write a *function* that produces the output works far better than asking it to produce the output directly.
- **Brandon:** For AI-heavy applications, traditional deterministic testing tools like Cypress break down; the real challenge is testing non-deterministic, permutation-heavy AI behavior at scale.
- **Patrick:** Spreading Claude Code, Gemini, and GPT/Codex across separate tasks lets developers leverage all subscription token budgets simultaneously rather than exhausting one.
- **Brandon:** The highest-leverage activity right now is not coding — it's identifying the right business problem. Coding is now trivially easy; problem selection and go-to-market are the hard parts.
- **Brandon:** "Boring niche" software (cemetery management, compliance tools) is a prime opportunity because legacy competitors develop slowly and AI-assisted developers can outpace them dramatically.
- **Patrick:** Reducing unit cost of work doesn't reduce total work — it expands the set of use cases that become economically viable, increasing demand for skilled orchestrators.
- **Brandon:** Work done in 2026 compounds more than work done in five years — the window of low competition and high willingness to pay is now.
- **Scott:** Naming a public repo after a proprietary tool (e.g., "Claude Code Mobile") risks legal issues; neutral names like "Code Anvil Mobile" are safer.

---

## qa

**Q (Darryl):** Is OpenClaw running on a Mac Mini?
**A (Patrick):** No, it's running on an Ubuntu VM on Proxmox.

**Q (Juan):** How do you manage the relationship between OpenClaw and cloud resources like a database inside a VPC without it accidentally deleting things?
**A (Patrick):** Isolate it — run it on a local VM or Docker container. It doesn't need significant resources. Give it only what it needs: a dedicated Google Drive for documents, a dedicated email that only reads from your address, and its own calendar so it invites you rather than touching yours.

**Q (Juan):** Are you worried about OpenClaw using your home network?
**A (Brandon):** Not currently, because the scope of tasks is very narrow — it only accesses Appify and specific known sites. The risk is low when the task surface is small, but it's an orange flag worth monitoring.

**Q (Rag):** What's the difference between using the Claude Code VS Code extension terminal versus a regular terminal?
**A (Brandon):** Don't use the Claude Code extension terminal — it has fewer features. Open a regular terminal in the editor (using the + button in the terminal tab row), navigate to your project, and type `claude` to start a session. This gives you full Claude Code functionality.

**Q (Rag):** When using Claude Sonnet inside the editor (e.g., anti-gravity/Gemini), is it using my Claude subscription or my Gemini subscription?
**A (Brandon):** It's hitting your Gemini subscription limits, not your Claude subscription.

**Q (Elena, via chat):** Is there a meaningful difference between building a GenAI backend in TypeScript versus Python?
**A (Brandon):** Python is the better choice for AI-specific work because the leading AI libraries (e.g., Dockling for RAG/chunking) are Python-native. TypeScript wrappers for these libraries often just proxy to a Python server anyway. The practical approach is TypeScript for front-end and general back-end, Python for AI-specific tasks.

**Q (Elijah):** Claude Code has agent teams that run in tmux — is that a good terminal multiplexer to use?
**A (Brandon):** He had conflicts between Claude's shortcut keys and tmux's shortcut keys when running an interactive CLI inside another CLI. He moved to Warp terminal instead, which avoids those conflicts and allows easy multi-window management.

**Q (Morgan):** For a multi-tenant Supabase app, does each organization need its own Supabase instance for SOC 2 compliance?
**A (Brandon):** No. SOC 2 doesn't care about multi-tenancy within a single database instance — that's just application-level security. You pay for the HIPAA/SOC 2 compliant Supabase tier (~$600/month) and the auditor focuses on breach response policies, not your schema design.

**Q (Jaylen):** Any feedback on the content creator monetization platform?
**A (Brandon):** Consider a subscription model ($50–$99/month per creator) rather than pure transaction fees — it creates recurring revenue and reduces dependency on individual transactions. Also, do the math on which monetization model reaches your revenue target with the fewest customers.
**A (Darryl):** Consider adding in-app video recording so creators (including non-YouTubers like athletes) can record and deliver short personalized videos directly in the platform, similar to Cameo.
**A (Ryan):** Suggested a hybrid model combining monthly subscriptions with transaction fees.

---

## tools

- **Claude Code** — Primary coding agent used by most members for iterative development across multiple simultaneous instances.
- **Codex (OpenAI)** — Brandon's preferred tool for long-running, high-precision tasks like generating large PowerPoint decks; hooks up to Gemini for image generation.
- **Meta Quest 3** — Brandon uses it to run 15+ Claude Code instances on virtual screens for maximum parallel throughput.
- **Warp** — Terminal application Brandon uses instead of VS Code's built-in terminal or tmux; supports easy multi-pane Claude Code sessions.
- **OpenClaw** — Autonomous AI agent framework being deployed by multiple members for tasks like customer research, job searching, email drafting, and calendar management.
- **Appify** — Used by Brandon with OpenClaw for LinkedIn browsing and customer research automation.
- **N8N** — Discussed as an orchestration layer for complex flows; noted as cost-effective when self-hosted on a local VM versus paying per-token for Claude.
- **Proxmox** — Patrick's hypervisor for running the Ubuntu VM that hosts OpenClaw.
- **Telegram** — Marc uses it as the interface to communicate with his OpenClaw instance.
- **Vertex AI / Model Garden (Google Cloud)** — Marc used it to spin up a RAG and generate images for a clothing site demo; studying for the Google Generative AI Leader certification.
- **Gemini (Google)** — Used as a cost-effective model for background/non-critical tasks; also the model behind the anti-gravity editor integration.
- **Dockling** — Python-native embedding and chunking tool for RAG applications; mentioned as an example of why Python is preferred for AI backends.
- **Supabase** — Database backend used by Morgan for the cemetery management system; HIPAA/SOC 2 compliant tier costs ~$600/month.
- **Vercel** — Hosting platform used by Morgan; static IP requires the $100/month plan for compliance purposes.
- **Hostinger** — Patrick's hosting provider; Claude Code automatically pushes his static site there.
- **Claude Sonnet 4.6** — The specific model Patrick uses behind his CV site's AI content generation (bilingual JSON extraction).
- **D3 (D3 hierarchy)** — JavaScript visualization library Morgan used to build interactive cemetery plot hierarchy diagrams.
- **Cloudflare Tunnel** — Scott uses it to securely expose his local Claude Code instance to his mobile device via Code Anvil Mobile.
- **Anthropic Agent SDK** — Scott built Code Anvil Mobile on top of this to create a mobile-friendly UI for Claude Code.
- **Discord** — Patrick recommends it over Slack for OpenClaw context management because channels naturally segment context windows.
- **GitHub Actions** — Ty uses it for automated code verification as part of his formal verification layer (Usai).
- **Cypress** — Mentioned as the standard for end-to-end testing but noted as insufficient for non-deterministic AI applications.
- **TinySeed** — Early-stage SaaS investor Brandon referenced as a potential funding source for Morgan's cemetery management business.
- **Grok** — Marc used it to generate exercise demonstration videos for his fitness app.
- **11 Labs** — Scott's Neural Spark SaaS allows users to connect their 11 Labs voice accounts.
- **Mermaid** — Diagramming extension used by Rag in VS Code; Brandon helped him find the correct "edit diagram" button to enable zoom functionality.
- **Fast API / Flask** — Mentioned as the key frameworks needed to build a Python AI backend service.
- **Railway** — Mentioned as a hosting option for running Python AI microservices.

---

## links

- **Starter Story YouTube channel / My First Million episode** — Brandon referenced a recent episode where the Starter Story founder discusses validating app ideas via YouTube Shorts before building; recommended for idea generation.
- **Accelerando (book, 2005, Charles Stross)** — Brandon and Scott recommended this sci-fi novel as a prescient description of the current AI acceleration trajectory, including concepts of transhumanism and the technological singularity.
- **Code Anvil Mobile (GitHub repo, Scott Rippey)** — Scott's public repo for a mobile-friendly Claude Code interface using Anthropic's Agent SDK and Cloudflare tunnels; he said the latest merged version would be available the following day.
- **Usai presentation (Ty Wells)** — Ty shared a presentation link in the call for his formal AI verification layer project; attendees were invited to review it directly.

---

## decisions

- **Scott Rippey** will merge and publish the updated Code Anvil Mobile repository to GitHub by the following day so group members can clone and use it.
- **Ty Wells** will contact Brandon on Friday to discuss AI testing, reliability, and formal verification approaches in more depth.
- **Brandon Hancock** will introduce Morgan Cook to TinySeed (or Dan Martell) once Morgan has a first paying customer for the cemetery management system.
- **Brandon Hancock** will share HIPAA/SOC 2 compliance process details and vendor contacts with Morgan Cook via email.
- **Marc Juretus** will take the Google Generative AI Leader certification exam the following week.
- **Paul Miller** will contact Brandon on Friday to discuss strategies for managing multiple simultaneous AI consulting projects efficiently.
- **Brandon Hancock** will send Ty Wells a file (referenced as "Insights") for review; Ty will add it to the library the following day.
- **Patrick Chouinard** will continue managing OpenClaw with its dedicated GitHub organization, isolated VM, and channel-separated Discord context as a model for the group.
- **Jaylen Davis** will use the call recording (captured on his phone) to extract and summarize the monetization feedback via AI for further analysis.