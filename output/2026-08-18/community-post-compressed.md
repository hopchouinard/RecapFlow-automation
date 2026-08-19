📝 SUMMARY
Patrick Chouinard rolled out Claude to roughly two thousand enterprise users. Daniel Zivkovic demonstrated low-code AI search for real estate. The group discussed consultant value as vibe coding spreads, with updates on video generation, digital signage, cemetery management, and conversational commerce. System prompt engineering can cut token costs by appending instructions directly to Claude Code rather than using CLAUDE.md.

💡 KEY INSIGHTS
Appending instructions to Claude Code's system prompt keeps them fresh, unlike CLAUDE.md that gets buried. Patrick adopted IndieDevDan's verbosity-fix with alias tables and reference numbering, dropping token consumption significantly.

Daniel showed that low-code tools like Algolia let developers tune prompts with business owners in real time, avoiding months of isolated RAG work.

When scaling hands-on services, staying in the field preserves raw feedback, but employees surface UX issues founders unconsciously work around.

Morgan noted viewing business as an Infinite Game reduces anxiety, since operations are continuous renegotiation rather than fixed endpoints.

Paul emphasized coding agents need a clear roadmap and chief of staff orchestrator to avoid scope creep.

Vibe-coded demos look finished quickly but collapse at edge cases. The gap between writing code and software engineering remains where consultants add durable value.

A durable niche exists with budget-rich companies that refuse to become technical organizations, such as in construction or hospitality. Positioning as implementation and education beats competing on coding speed.

Enterprise tool adoption is frequently driven by support contracts rather than technical merit. Unsupported excellent tools often cannot clear procurement.

❓ KEY Q&A
Q: Hemal Shah asked for recommendations for a conversational agent that answers from a knowledge corpus, pulls real-time data, and takes actions.
A: Patrick moved away from LangChain toward the Claude SDK and harness workflows. Daniel recommended Algolia AI Search and Agent Studio for grounded answers with CRM connectivity, plus Thrillet for voice.

Q: Patrick asked Juan Torres how to scale his AI photo booth without being present.
A: Juan will hire a technician eventually but wants to stay in the field now for direct feedback, possibly using his social media contractor to gather reactions.

Q: Daniel asked how to integrate Anthropic on AWS skills with Microsoft Copilot.
A: Patrick explained there is no direct integration as they use different paradigms. Claude Code and Desktop connect to M365 via read-only connectors, separate from Copilot internals.

Q: Elijah asked why not build a custom front-end instead of Claude Desktop or Code.
A: Enterprise support contracts are the deciding factor. Tools like Pi.dev or Omnigen lack corporate support, making them non-viable for procurement regardless of capability.

Q: Elijah asked how Patrick structures corporate hierarchical AI memory.
A: Markdown files with frontmatter organized into categories. Large files become tables of contents linking to sub-files; the model walks links to load minimal context. Git-backed for versioning.

Q: Daniel and Elijah asked how to sell services now that clients can vibe code.
A: Focus on clients with budget who refuse to become technical organizations. Position as implementation and education, then transition contracts from doing work to building agents, re-pricing around agents delivered.

🛠️ TOOLS AND CONCEPTS MENTIONED
Claude Code, Desktop, and Cowork — Enterprise harness via AWS Bedrock.

IndieDevDan's append technique — Curb verbosity via system prompt aliases and reference shorthand.

Algolia AI Search and Agent Studio — Low-code enterprise search.

ComfyUI plus MiniMax H3 — AI video generation.

Convex — Backend for Morgan's Plastic Curve rewrite.

Git-backed hierarchical memory — Markdown wiki with frontmatter, TOC, and link traversal.

Compound Engineering — Parallel-agent overnight coding.

Chief of staff agent and AIOS harness — Roadmap orchestration.

Mac Mini M4 24GB — 24/7 coding agent hardware.

M365 Connectors — Read-only SharePoint, Teams, Outlook, Calendar access.

Codex — Validate Claude code.

SignPy — Digital signage for Raspberry Pi.

Arduino stackable hats — Lightweight embedded alternative.

📎 SHARED RESOURCES
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

🔄 FOLLOW-UPS WORTH EXPLORING
Tom Welsh will share his custom ComfyUI workflow for video generation.

Patrick will continue refining a TechStack recommendation skill to constrain Claude's suggestions for non-technical enterprise users, and will explore triggering it automatically via global instructions.

Patrick will keep developing a level zero support skill trained on pilot support tickets ahead of the full two thousand user rollout.

Patrick will continue expanding the Git-backed hierarchical corporate memory system across personal, team, and corporate layers.

Juan will have his social media contractor help gather user feedback and content at an upcoming event.

Shakur will evaluate Arduino and other cheaper embedded alternatives now that Gumstix is discontinued.

Daniel will test IndieDevDan's system prompt verbosity fix and reach out to Ty Wells about a security audit tool for his ShipKit project.

Morgan will wait for county buy-in before investing further in the Heritage Plot cemetery system, and may use it as a marketing case study.

Morgan will hold off onboarding users to Plastic Curve until the Convex rewrite is further along.