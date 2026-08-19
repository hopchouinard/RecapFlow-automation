# general

This session was a recurring community coaching call (part of the "AI Developer Accelerator" Skool community, meeting Tuesdays/Thursdays, organized primarily by Patrick Chouinard) where members gave weekly updates on their AI projects and traded technical advice. A newcomer, Daniel Zivkovic (Toronto, runs the Serverless Toronto meetup), joined and shared his experience building an AI search/chat assistant for his wife's real estate business using Algolia. Regulars gave updates: Tom Welsh discussed video generation with MiniMax/ComfyUI and a fantasy-cat merchandising idea; Hemal Shah asked for agentic-framework recommendations for an e-commerce conversational AI project; Paul Miller described wrapping up a large Australian logistics project, buying a Mac Mini for 24/7 agent operation, and plans to hire a Philippines-based support team; Juan Torres updated on his AI photo booth business and discussed staffing/scaling; Morgan (mdcatc) covered multiple projects (SignPy digital signage on Raspberry Pi, Heritage Plot cemetery management, Plastic Curve carpool app rewritten in Convex); and Shakur Abdullah shared a UI-to-design tool experiment and a shared shopping-list app for his wife.

A major throughline was Patrick Chouinard's enterprise Claude rollout (~2,000 users via AWS Bedrock), including building skills to constrain Claude's tech-stack recommendations for non-technical "citizen developers," a "level zero support skill" trained from pilot support tickets, and a Git-backed hierarchical corporate memory system. Elijah Stambaugh (a consultant building "second brain"/agent infrastructure for client companies) asked Patrick extensive follow-up questions about enterprise architecture, training methodology, and monetization strategy, leading into a broader group discussion about how AI consultants find and retain clients now that "everyone can vibe code." The call also covered IndieDevDan's technique of appending custom instructions to Claude Code's system prompt to reduce Opus verbosity, which several members had already tested with strong results.

# insights

- **Patrick Chouinard**: Claude Code's `append system prompt file` option inserts content at the same priority level as the system prompt itself (higher than CLAUDE.md), and because the system prompt is reposted every turn, instructions placed there stay "fresh" — unlike CLAUDE.md content, which gets buried deep in context after many turns.
- **Patrick Chouinard**: IndieDevDan's verbosity-fix system prompt addition includes an alias table (e.g., "ELI" expands to "explain it to me like I'm 12") and reference numbering (R1, R2, F1, F2 for risks/findings) so users can refer back to earlier context items by short codes instead of re-describing them — effectively embedding a lightweight skill directly into the system prompt.
- **Patrick Chouinard**: After adopting this approach, token consumption dropped significantly while output quality/quantity stayed the same or improved; the shorthand vocabulary became "muscle memory" within a day.
- **Daniel Zivkovic**: Low-code AI tools (like Algolia's AI Search) let you sit directly with the actual business owner and tune the prompt/answers in real time — skipping the typical months-long lag where developers build a RAG system in isolation and only discover bad answers long after deployment.
- **Tom Welsh / Patrick Chouinard**: When scaling a hands-on service business (e.g., Juan's AI photo booth), staying "in the field" longer preserves access to raw user feedback; but bringing in an employee without the founder's tacit knowledge often surfaces UX issues the founder has learned to unconsciously work around.
- **Morgan (mdcatc)**: Reframing project completion using the "Infinite Game" mindset (vs. finite-game thinking) reduces the anxiety of never finishing — business is a continuous cycle of renegotiation rather than a project with a fixed end state.
- **Paul Miller**: Efficiency gains come from having a clear roadmap and a "chief of staff"-style orchestrating agent — without deliverables and scope discipline, the same coding-agent setup produces open-ended, ever-expanding work.
- **Morgan (mdcatc)**: A "moat" is essential for defensibility against larger SaaS incumbents — e.g., his cemetery software's moat is being the only system that supports a specific state's Freedom of Information Act requirements for government-run cemeteries.
- **Morgan (mdcatc)**: Vibe-coded demos can look functional quickly, but break down at edge cases and security — the gap between "writing code" and "software engineering" is where professional consultants still add value.
- **Patrick Chouinard**: A viable consulting model in the AI era: warn clients in advance about a coming problem, let them ignore the warning, then charge a premium to fix it after it materializes ("AI amplifies stupidity as much as it amplifies intelligence").
- **Elijah Stambaugh**: A durable niche for AI consultants is companies that have money and need but explicitly don't want to become technical/software organizations themselves (e.g., construction, hospitality) — as opposed to competing with internal IT for technical vibe-coding work.
- **Patrick Chouinard**: In enterprise environments, tool choice is often driven by support contracts rather than technical merit — unsupported tools (custom harnesses, open-source agents) can't be adopted at the corporate level regardless of capability.
- **Patrick Chouinard**: Model release and Claude Code version rollout are not synchronized — new models often ship first on a "latest" branch weeks before reaching the "stable" branch enterprises use.

# qa

**Q (Hemal Shah):** From an agentic-framework perspective, what's the current recommendation for building a conversational agent that needs to answer from a knowledge corpus, pull real-time data (order status), and take actions (schedule appointments)?
**A (Patrick Chouinard / Daniel Zivkovic):** Patrick noted he's moved away from LangChain/LangGraph toward using the Claude SDK and a "harness" workflow depending on the use case. Daniel recommended Algolia's AI Search/Agent Studio for grounded, corpus-based answers with CRM connectivity (free for small sites), and mentioned Thrillet as a voice-channel option, though the two aren't yet integrated.

**Q (Patrick Chouinard):** For Juan's AI photo booth business, how do you plan to scale beyond needing to be physically present at every event?
**A (Juan Torres):** The plan is to hire an AI booth technician to handle setup/install, though this isn't yet systematized; Juan wants to stay in the field for the immediate future to keep getting direct user feedback, and is considering having his social-media contractor also gather event reactions.

**Q (Daniel Zivkovic):** How do you integrate skills run through Anthropic on AWS with Microsoft Copilot so that business users get shared context?
**A (Patrick Chouinard):** There's no integration — Claude and Copilot use different underlying paradigms (Copilot's "agents" resemble skills/sub-agents in Claude's world), and Claude Code/Desktop connect to M365 (SharePoint, Teams, Outlook, Calendar) via built-in read-only connectors, but this is separate from anything running in Copilot.

**Q (Elijah Stambaugh):** Why not build a custom front-end harness instead of using Claude Desktop/Code/Cowork directly?
**A (Patrick Chouinard):** Enterprise support contracts are the deciding factor — tools like Pi.dev or Omnigen are excellent but come without a corporate-level support contract, so they can't be adopted at enterprise scale regardless of capability.

**Q (Elijah Stambaugh):** How are you structuring corporate/hierarchical AI memory — database, Git, or something else — and how does the agent traverse it?
**A (Patrick Chouinard):** Using Markdown files with frontmatter headers organized into categories (contacts, ideas, projects, decisions); large files become tables of contents linking to more detailed sub-files, and the model walks the link structure to load minimal context needed to answer a question. The system is Git-backed for versioning/reconciliation, inspired loosely by knowledge graphs and personal-wiki concepts but customized to their infrastructure.

**Q (Daniel Zivkovic / Elijah Stambaugh):** With AI making code generation cheap and clients feeling like they can build anything themselves, how do you actually sell services now?
**A (Elijah Stambaugh):** Focus on clients who have money and need but explicitly don't want to become technical (e.g., construction, hospitality) — position as an implementation/education layer rather than competing on raw coding ability; structure contracts to transition from "doing the work" to "building the agent that does the work," then re-price around the agents delivered.

# tools

- **Claude Code / Claude Desktop / Claude Cowork** – Anthropic's coding agent and enterprise desktop harness; central to Patrick's enterprise rollout to ~2,000 users via AWS Bedrock.
- **Opus 5 / Claude Sonnet** – Models discussed for architecture design and code delivery in multi-agent pipelines (Paul Miller's workflow).
- **Codex** – Used by Paul Miller to validate/check code generated by Claude.
- **IndieDevDan's "append system prompt" technique** – A YouTube-shared method for curbing Opus verbosity via a supplemental system prompt file.
- **ComfyUI + MiniMax H3** – Used by Tom Welsh for AI video generation for a children's story project.
- **Algolia (AI Search / Agent Studio)** – Low-code enterprise search/chat tool Daniel Zivkovic used for a real-estate client's grounded Q&A widget.
- **Thrillet** – Voice AI agent company mentioned as an option for a voice channel.
- **Mac Mini (M4, 24GB RAM)** – Purchased by Paul Miller to run coding agents 24/7 remotely.
- **AIOS / "harness" agent environment** – Paul Miller's setup for continuous agent triggers and a master orchestrating "chief of staff" agent.
- **Convex** – Backend platform Morgan is using to rewrite "Plastic Curve" (carpool app), simplifying prior MVP design.
- **SignPy** – Morgan's digital signage system for Raspberry Pi with automated content expiration/rules.
- **Raspberry Pi 4 & 5** – Hardware used to run SignPy signage; Pi 5 needed for crisper animation.
- **Fire Stick** – Considered as cheaper signage hardware but rejected due to new publishing/app-store restrictions.
- **Gumstix (Overo Series)** – Suggested embedded hardware option for Shakur's project; confirmed discontinued (final deliveries Dec 2025).
- **Arduino (with stackable "hats")** – Recommended by Morgan as a lightweight, dedicated-process alternative to Raspberry Pi for Shakur's grandparent-call device.
- **M365 Connectors (in Claude environment)** – Built-in Microsoft-provided connectors giving Claude read-only access to SharePoint, Teams, Outlook, Calendar.
- **GitHub Copilot / Microsoft Copilot** – Compared against Claude Code/Cowork; noted as improving but still "third player."
- **Honcho** – Memory/context tool Patrick Chouinard uses (~3 months at $27), asked about in chat by Biggi Fraley.
- **Compound Engineering (framework/methodology)** – Used by Daniel Zivkovic for parallel-agent overnight coding workflows ("dark factory" setup with Claude + Codex).
- **ShipKit** – Framework Daniel Zivkovic used with his son for a side project.
- **Postforme** – Social media scheduling tool suggested to Juan Torres by Shakur Abdullah.
- **Signagelive / BrightSign** – Digital signage platform/hardware Tom Welsh's client uses, shared as reference for Morgan's SignPy project.
- **Skool community platform** – Hosts the "AI Developer Accelerator" group where this call takes place.
- **Pi.Dev** – New tool Patrick Chouinard mentioned starting to use; also referenced regarding IndieDevDan's pivot.

# links

- https://www.youtube.com/watch?v=S_QdQ1G4GlU — IndieDevDan's video on the Opus verbosity-fixing system prompt technique (shared twice by Patrick Chouinard).
- https://www.skool.com/ai-developer-accelerator — Link to the community/group hosting these calls (shared by Paul Miller in response to Daniel's question).
- https://www.algolia.com/ — Algolia platform homepage (shared by Paul Miller).
- https://jasminahomes.ca/search-ai/ — Live demo of Daniel Zivkovic's Algolia-powered AI search widget for his wife's real estate site.
- https://www.instagram.com/ai.booth.studio/ — Juan Torres's Instagram showcasing his AI photo booth transformations.
- https://www.meetup.com/serverless-toronto/ and https://youtube.serverlesstoronto.org/ — Daniel Zivkovic's long-running Serverless Toronto meetup group and its recorded events.
- https://build.signagelive.com/platform-services/ — Signagelive digital signage platform (shared by Tom Welsh as reference for Morgan's project), paired with BrightSign hardware.
- https://www.amazon.com/The-Infinite-Game-Simon-Sinek-audiobook/... — Audiobook link for "The Infinite Game" by Simon Sinek, referenced by Morgan.
- https://every.to/guides/compound-engineering — Daniel Zivkovic's shared write-up on his "compound engineering" AI-assisted SDLC approach.
- https://www.linkedin.com/in/magmainc/ — Daniel Zivkovic's LinkedIn, shared for members to connect outside the call.
- https://www.diamandis.com/podcast and https://www.youtube.com/@MoonshotsClips — Podcast/channel links shared by Paul Miller (context not fully discussed in transcript).
- https://www.youtube.com/@aiDotEngineer, https://www.youtube.com/@alejandro_ao, https://www.youtube.com/@HealthyGamerGG — YouTube channels shared in chat (AI Engineer-related content and ADHD coaching platform recommended to Juan Torres).

# decisions

- **Patrick Chouinard** will run/lead the call for Paul Miller this session as requested.
- **Tom Welsh** will dig out and share his custom ComfyUI workflow used for video generation.
- **Patrick Chouinard** will continue building and refining a "TechStack recommendation" skill so Claude stops suggesting non-approved tools (e.g., Vercel, Supabase) to non-technical enterprise users.
- **Patrick Chouinard** will continue developing the "level zero support skill" trained on pilot support-ticket knowledge ahead of the full 2,000-user Claude rollout.
- **Patrick Chouinard** will explore referencing the tech-stack skill directly in global instructions to trigger automatically on relevant user requests.
- **Patrick Chouinard** will continue building out the Git-backed hierarchical corporate memory system (personal → team → corporate layers) over the coming months.
- **Juan Torres** will contact his social-media/event contractor to help gather user feedback and content at this weekend's photo booth event.
- **Shakur Abdullah** will look into Arduino and other cheaper embedded alternatives (since Gumstix is discontinued) for his "call grandparents" button device.
- **Daniel Zivkovic** will try out IndieDevDan's system-prompt verbosity fix.
- **Daniel Zivkovic** will reach out to Ty Wells regarding a security audit tool for his ShipKit-based project.
- **Morgan (mdcatc)** will hold off pushing users onto Plastic Curve until the Convex rewrite is further along.
- **Morgan (mdcatc)** will wait for county buy-in/feedback before investing further in the Heritage Plot cemetery system, but may pursue it as a marketing case study to other cemeteries if time allows.