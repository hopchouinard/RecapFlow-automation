1. 📝 SUMMARY
This week's call covered a wide range of topics including Patrick Chouinard's enterprise Claude rollout to roughly two thousand users, Daniel Zivkovic's low-code AI search implementation for real estate, and ongoing discussions about how AI consultants can stay valuable as vibe coding becomes ubiquitous. Members shared project updates spanning video generation, digital signage, cemetery management, and conversational commerce, while a deep dive into system prompt engineering revealed immediate ways to cut token costs and improve model focus.

2. 💡 KEY INSIGHTS
Appending instructions directly to Claude Code's system prompt keeps them persistently fresh across turns, unlike CLAUDE.md content that gets buried deep in context. Patrick adopted IndieDevDan's verbosity-fix approach including an alias table and reference numbering, which dropped token consumption significantly while maintaining output quality.

Daniel demonstrated that low-code AI tools like Algolia let developers sit side-by-side with business owners to tune prompts in real time, avoiding the months-long lag of isolated RAG development.

When scaling a hands-on service business, staying in the field preserves raw user feedback, but bringing in employees often surfaces UX issues that founders unconsciously work around.

Morgan shared that reframing business as an Infinite Game rather than a finite project reduces anxiety about never finishing, because operations are a continuous cycle of renegotiation rather than a fixed end state.

Paul emphasized that coding agents need a clear roadmap and a chief of staff orchestrator to avoid open-ended scope creep; without deliverable discipline, the same tools produce endless expansion.

Vibe-coded demos can look finished quickly but often collapse at edge cases and security boundaries. The gap between writing code and actual software engineering remains where professional consultants add durable value.

A durable consulting niche exists with companies that have budget and need but explicitly refuse to become technical organizations, such as those in construction or hospitality. Positioning as an implementation and education layer beats competing on raw coding speed.

In enterprise environments, tool adoption is frequently driven by support contracts rather than raw technical merit. Unsupported excellent tools often cannot clear procurement regardless of capability.

3. ❓ KEY Q&A
Q: Hemal Shah asked for the current recommendation for a conversational agent that answers from a knowledge corpus, pulls real-time data like order status, and takes actions like scheduling appointments.
A: Patrick noted he has moved away from LangChain and LangGraph toward the Claude SDK and harness workflows. Daniel recommended Algolia's AI Search and Agent Studio for grounded corpus answers with CRM connectivity, and mentioned Thrillet as a voice channel option.

Q: Patrick asked Juan Torres how he plans to scale his AI photo booth business without being physically present at every event.
A: Juan plans to hire an AI booth technician eventually, but wants to stay in the field for now to keep collecting direct user feedback. He is also considering having his social media contractor gather event reactions.

Q: Daniel asked how to integrate skills running through Anthropic on AWS with Microsoft Copilot so business users get shared context.
A: Patrick explained there is no direct integration because Claude and Copilot use different underlying paradigms. Claude Code and Desktop connect to M365 via built-in read-only connectors, but this is separate from anything running inside Copilot.

Q: Elijah asked why not build a custom front-end harness instead of using Claude Desktop or Code directly.
A: Patrick said enterprise support contracts are the deciding factor. Tools like Pi.dev or Omnigen may be excellent but lack corporate-level support contracts, making them non-viable for enterprise adoption regardless of capability.

Q: Elijah asked how Patrick is structuring corporate hierarchical AI memory and how the agent traverses it.
A: Patrick uses Markdown files with frontmatter headers organized into categories like contacts, ideas, projects, and decisions. Large files become tables of contents linking to detailed sub-files, and the model walks the link structure to load minimal context. The system is Git-backed for versioning.

Q: Daniel and Elijah asked how to sell services now that clients feel they can vibe code anything themselves.
A: Elijah advised focusing on clients who have money and need but do not want to become technical organizations. Position yourself as an implementation and education layer, then structure contracts to transition from doing the work to building the agent that does the work, re-pricing around the agents delivered.

4. 🛠️ TOOLS AND CONCEPTS MENTIONED
Claude Code, Claude Desktop, and Claude Cowork — Anthropic's coding agent and enterprise harness, central to Patrick's rollout via AWS Bedrock.

IndieDevDan's append system prompt technique — A method for curbing Opus verbosity by injecting custom instructions at the system prompt level, including alias tables and reference shorthand.

Algolia AI Search and Agent Studio — Low-code enterprise search and chat tools Daniel used for a real estate client's grounded Q&A widget.

ComfyUI plus MiniMax H3 — Used by Tom Welsh for AI video generation.

Convex — Backend platform Morgan is using to rewrite his Plastic Curve carpool app.

Git-backed hierarchical corporate memory — Patrick's Markdown-based personal wiki with frontmatter, tables of contents, and link traversal for minimal context loading.

Compound Engineering — Daniel's methodology for parallel-agent overnight coding workflows.

Chief of staff agent and AIOS harness — Paul Miller's setup for continuous agent triggers and roadmap orchestration.

Mac Mini M4 with 24GB RAM — Paul's hardware choice for running coding agents twenty-four seven.

M365 Connectors — Built-in Microsoft connectors giving Claude read-only access to SharePoint, Teams, Outlook, and Calendar.

Codex — Used by Paul Miller to validate code generated by Claude.

SignPy — Morgan's digital signage system for Raspberry Pi.

Arduino with stackable hats — Recommended embedded alternative to Raspberry Pi for dedicated lightweight processes.

5. 📎 SHARED RESOURCES
IndieDevDan's video on the Opus verbosity-fixing system prompt technique
https://www.youtube.com/watch?v=S_QdQ1G4GlU

Daniel's live Algolia AI search demo for real estate
https://jasminahomes.ca/search-ai/

Algolia platform
https://www.algolia.com/

Daniel's write-up on Compound Engineering
https://every.to/guides/compound-engineering

Serverless Toronto meetup and recordings
https://www.meetup.com/serverless-toronto/
https://youtube.serverlesstoronto.org/

Juan's AI photo booth Instagram
https://www.instagram.com/ai.booth.studio/

Signagelive digital signage platform reference
https://build.signagelive.com/platform-services/

The Infinite Game by Simon Sinek
https://www.amazon.com/The-Infinite-Game-Simon-Sinek-audiobook/...

AI Developer Accelerator Skool community
https://www.skool.com/ai-developer-accelerator

Daniel's LinkedIn
https://www.linkedin.com/in/magmainc/

6. 🔄 FOLLOW-UPS WORTH EXPLORING
Tom Welsh will share his custom ComfyUI workflow for video generation.

Patrick will continue refining a TechStack recommendation skill to constrain Claude's suggestions for non-technical enterprise users, and will explore triggering it automatically via global instructions.

Patrick will keep developing a level zero support skill trained on pilot support tickets ahead of the full two thousand user rollout.

Patrick will continue expanding the Git-backed hierarchical corporate memory system across personal, team, and corporate layers.

Juan will have his social media contractor help gather user feedback and content at an upcoming event.

Shakur will evaluate Arduino and other cheaper embedded alternatives now that Gumstix is discontinued.

Daniel will test IndieDevDan's system prompt verbosity fix and reach out to Ty Wells about a security audit tool for his ShipKit project.

Morgan will wait for county buy-in before investing further in the Heritage Plot cemetery system, and may use it as a marketing case study.

Morgan will hold off onboarding users to Plastic Curve until the Convex rewrite is further along.