📝 SUMMARY

This week's call covered demos, workflow strategies, and tool discoveries. Eric Li demoed Kira, a natural language Text-to-SQL platform with a standout Slack integration. Patrick shared updates to his Claude Code plugin ecosystem and an Obsidian-based knowledge management setup. Ryan walked through a rebuilt SEO-optimized agency site and a hands-free lead capture app. The group also discussed enterprise agentic development workflows, the Claude Code source leak and its Rust rewrite, Gemma 4 for local/private AI, and the Claude plus Codex hybrid development pattern.


💡 KEY INSIGHTS

Claude + Codex hybrid workflow is delivering extraordinary value
Patrick runs Claude Max ($100/month) alongside the OpenAI Codex plugin ($20/month) and estimates he is getting roughly $5,000/month in API value. The plugin adds slash commands into Claude Code sessions including /codex review, /codex status, /codex rescue, and an adversarial review function that actively tries to break your application and reports vulnerabilities. You can configure a completion hook so Codex automatically reviews every Claude output in a loop until no issues remain.

Obsidian plus Claude Code as a lightweight RAG
Using Andrej Karpathy's prompt (linked below), you can turn an Obsidian vault into a self-organizing knowledge base managed by Claude Code via terminal. It auto-classifies and backlinks documents and performs comparably to a light RAG system for up to a few hundred documents with no additional infrastructure.

Enterprise SDLC adapted for agentic development
Patrick's team records design meetings, transcribes them, and has Claude Code convert them into an intent document split into independent workstreams for parallel development across a team of four. Sprint planning transcripts become the workstream specs — a scalable model for teams moving beyond solo agentic development.

User-driven development loop (Ty's model)
Ty built a feedback hub where end users describe issues with screenshots or video. Claude Code asks clarifying questions until it reaches 85% confidence, then autonomously builds a fix in a headless session, creates a PR, and Ty only approves and merges. The Codex plugin validates before the PR is created.

Gemma 4 for local and private use cases
Gemma 4 runs on-device including phones and Raspberry Pi hardware. Patrick uses it locally for a private health data RAG covering lab results and scans he does not want sent to cloud LLMs. Jake confirmed it is surprisingly good and highlighted the value of fully offline mobile inference.

Claude Code source leak and community response
The Claude Code source was leaked and a Rust rewrite called claw-code appeared on GitHub, reaching 174,000 stars and 105,000 forks within days. The group consensus is that Anthropic may need to go fully open source in response.

Anthropic pricing changes are coming
The current $200/month Max plan offering roughly $5,000 in API value is expected to be restructured upward. Members are maximizing usage now while current pricing holds.

Demo and pitch tip
Lead with the killer feature, not the plumbing. For a product like Kira, open with the Slack integration demo, not the architecture. Explain the value proposition first, then show how it works.

Competitive research before investor conversations
Use Google Deep Research to build competitive market analysis. Review sites like G2 Crowd help you understand what users like and dislike about competing products, sharpening your differentiator positioning.

F6S for startup cloud credits
F6S.com offers cloud service discounts including up to roughly $5,000 for GCP and other providers. Requirements are minimal: a website and a demo.


❓ KEY Q&A

Q: How does Kira handle data security when non-technical users access the data warehouse?
A: Security is managed at the workspace level. Admins control which tables each workspace can access. Slack-based access is governed by channel membership, so users can only query data that channel is authorized to see. The app enforces SELECT-only queries with no INSERT, UPDATE, or CREATE operations permitted.

Q: What differentiates Kira from other Text-to-SQL competitors?
A: The Slack integration. Very few competing platforms support querying a data warehouse directly from Slack, and those that do are expensive and complex to configure. Kira requires only three variables to connect: API Token, Verification Token, and Signing Secret.

Q: How do you use Claude Code and Codex together without switching tools?
A: Install the official OpenAI Codex plugin for Claude Code. It adds slash commands directly into your session. Configure a completion hook so Codex automatically reviews every Claude output in a loop until no issues remain.

Q: Is Gemma 4 worth using for local and private AI tasks?
A: Yes. It runs on phones and Raspberry Pi hardware. Patrick uses it for a local health data RAG. Paul noted Google has released demo iOS code showing local on-device inference. Jake confirmed it is surprisingly capable fully offline.

Q: What resources are recommended for learning about Claude Code?
A: The claw-code GitHub repo is a useful reference. The Karpathy Obsidian gist is a practical starting point for knowledge management use cases. Both are linked below.


🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Core agentic coding tool central to all workflows discussed.

OpenAI Codex plugin for Claude Code — Enables automated code review, adversarial testing, and rescue loops within Claude Code sessions. Significant token savings and quality improvements reported.

Obsidian plus Claude Code (Karpathy method) — Turns an Obsidian vault into a self-organizing knowledge base. Lightweight RAG alternative for up to roughly 200 documents with no extra infrastructure.

claw-code — Open-source Rust reimplementation of Claude Code following the source leak. 174,000+ stars and 105,000 forks within days.

Gemma 4 — Google's lightweight open model runnable on-device. Useful for private and local AI tasks. Multimodal with agentic capabilities.

Adversarial review (Codex plugin) — Actively attempts to break your application and reports failure points. Patrick uses it daily.

Workstream-based enterprise SDLC — Record design meetings, generate an intent document, split into independent workstreams, develop in parallel.

User-driven development loop — Users submit feedback, AI clarifies to 85% confidence, headless Claude session builds the fix, Codex validates, PR is created, human only approves and merges.

Text-to-SQL / NL-to-SQL — Category of tools translating natural language to SQL. Kira is an example; Salesforce recently acquired a competitor in this space.

F6S.com — Startup platform offering cloud credits and perks for early-stage founders with minimal requirements.

Google Deep Research — Recommended for building competitive market analysis before investor conversations.

G2 Crowd — Review site for understanding user sentiment about competing products.

Anthropic Mythos model — New Anthropic model in preview with a 240-page spec. Noted for fast vulnerability discovery in cybersecurity contexts.

Cursor 3 — New release mentioned briefly. Jake noted terminal and tmux workflows have largely superseded it for advanced users in this community.

Meta Glasses — Ryan uses them for hands-free photo capture while driving to feed a lead capture app.

ngrok — Used by Eric to expose a local port for Slack webhook integration during the Kira demo.

Superpowers add-on for Claude — Browser-based UI enhancement for Claude, updated the day of the call and widely praised.


📎 SHARED RESOURCES

Andrej Karpathy's Obsidian plus Claude Code gist
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Patrick's Lab Website (PatchouTech) — Claude Code plugins including Claude Speak, with interactive constellation graph of tools.
https://lab.patchoutech.com/

Ryan's Website (One Stop Creative Agency) — SEO-optimized site with custom animations built using agentic coding tools.
https://onestopcreativeagency.co.uk/

claw-code GitHub repo (Rust rewrite of Claude Code)
https://github.com/ultraworkers/claw-code

openclaude GitHub repo — Alternative repo also circulated during discussion.
https://github.com/Gitlawb/openclaude

OpenAI Codex plugin for Claude Code
https://github.com/openai/codex-plugin-cc

F6S (startup funding and cloud discounts)
https://www.f6s.com/

Gemma 4 agentic demo video (Prompt Engineering YouTube)
https://youtu.be/VFYnD1WREdU?si=F51POhFXfXlYeqiR


🔄 FOLLOW-UPS WORTH EXPLORING

Ty's UI Arena skill — Generates multiple UI/UX mockup options from an existing codebase. Ty indicated he may publish it to a public repo. Worth following up.

Patrick and Ty plugin collaboration — Ty expressed interest in contributing his Arena skill to PatchouTech. Patrick confirmed he just needs repo access. Not finalized on the call.

Enterprise SDLC workstream model deep dive — Patrick's method was introduced briefly and would benefit from a dedicated demo in a future call.

Anthropic pricing restructuring — Changes are imminent. Worth revisiting once confirmed to assess workflow impact and whether to lock in usage now.

Gemma 4 for local health data RAG — Patrick planned to migrate from Gemma 3 to Gemma 4. A follow-up on performance would be useful for others interested in private on-device AI.

Eric's Kira app funding progress — Eric is seeking funding and applied for Canadian government grants. The group suggested NVIDIA credits and F6S as alternatives. Worth checking back on traction.

Cursor 3 evaluation — Mentioned briefly but not evaluated. A dedicated comparison to current Claude Code and terminal-based workflows would be worthwhile.
