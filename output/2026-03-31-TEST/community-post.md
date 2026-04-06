📎 SHARED RESOURCES

Codex Plugin for Claude Code
https://github.com/openai/codex-plugin-cc
Runs Codex as a tool inside Claude Code. Use it for code review and adversarial review to save Claude Code tokens for creation work.

Patrick's Lab Site
https://lab.patchoutech.com/
Personal project registry with tools, plugins, MCPs, and workflows. Includes a graph navigation UI and marketplace with install instructions.

Everything Claude Code (GitHub)
https://github.com/affaan-m/everything-claude-code
From an Anthropic hackathon. A comprehensive system of hundreds of agent plug-in skills — described as a full Claude Code upgrade, not just a library. Highly recommended.

Scott's AI News Digest
https://news.poweryourprocess.ai/
Daily AI news digest using Claude Haiku to summarize RSS feeds. Includes audio versions and semantic search via RAG. To join the private email list, contact scott@poweryourprocess.ai

Reddit: Claude Code Leaked Source Analysis
https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/
Community analysis of the Claude Code source leak. Described as an entertaining and informative read.

Major NPM Hack Explainer (YouTube)
https://www.youtube.com/watch?v=eGSsoSEppNU
Covers a significant NPM security incident from this week. Priority watch if you have servers or Node.js dependencies.

Unitree R1 Humanoid Robot
https://ca.robotshop.com/products/unitree-r1-humanoid-robot
General-purpose humanoid robot available for under $13,000 CAD. Shared as a data point in the robotics discussion.

Ty's Workshop Tool
https://nperson.ai
Tool Ty built for AI workshops. Shared for community review.

Juan's Diffusion Model Project
https://radiant-shaders.com/


❓ KEY Q&A

Q: What is the Codex plugin for Claude Code and why use it?
A: It installs Codex as a tool within Claude Code. The intended workflow is to use Codex for code review and adversarial review, reserving Claude Code tokens for generation. Patrick reported approximately $1 in OpenAI API fees for a full day of use with GPT-4o Mini TTS running alongside it.

Q: What is Claude Speak?
A: A plugin Patrick built that gives Claude Code a voice. It uses GPT-4o Mini TTS to read aloud the last block of Claude's response at the end of each turn. Claude can also call the speak function mid-turn to get the user's attention. Cost is roughly $1 for a full day of heavy use. Published on Patrick's lab marketplace.

Q: How does Scott's AI News Digest work technically?
A: It pulls from multiple RSS feeds, uses Claude Haiku to summarize and deduplicate stories, and tracks story development over time so threads are followed without repetition. Each story includes key takeaways, why it matters, and practical implications. Output is published to a blog with audio and supports semantic search via a RAG database.

Q: Is RAG going away?
A: Not for large document libraries. For small collections under roughly 1,000 documents, large context windows and agentic folder-search loops are increasingly replacing it. The recommended layered approach is RAG first, then a re-ranker like Cohere as layer two, and RLM-style loops only if data volume truly justifies the added latency.

Q: What fields will be most impacted by AI?
A: Knowledge work with defined decision trees and no judgment calls is most at risk. Cybersecurity, skilled trades, and data center infrastructure roles are resilient. Programming is not dead but shifts toward system design and workflow thinking rather than syntax. Patrick's framing: ask which fields will NOT be impacted — that is the shorter list.

Q: Should young people still go into programming?
A: Patrick argued yes, but the role shifts toward directing AI rather than writing syntax. System design, workflow thinking, and problem structuring remain essential human skills. Others noted that in two to three years AI may close that gap further, making the answer less clear.

Q: What is the best compliance approach for financial clients?
A: SOC 2 Type 1 is the standard. Vanta is a common tool for managing it. Piggybacking on a SOC 2-compliant partner's infrastructure is another path. Azure is the preferred cloud in finance. ISO compliance may be sufficient for lower-risk use cases, and insurance policies can cover known gaps as an interim measure. A qualified CISO and dedicated DevOps are strongly recommended.

Q: How do you handle scope creep when clients can see how fast you build?
A: Filter everything against critical path and OKRs. Ask on every ticket whether it is a critical business need. Alex built a Claude Code system that processes client call transcripts and runs a decision matrix against the project's North Star. Patrick's reframe: clients who create problems are the reason you have ongoing work.

Q: How do you repurpose an old gaming PC for AI workloads?
A: Install Proxmox as the base layer, deploy Docker instances of LLMs and services on top, use Prometheus and Grafana for monitoring, and connect remotely via Tailscale or Twingate. Caddy or Traefik can serve as a reverse proxy. Claude Code can handle most of the deployment. Alex confirmed this works on older hardware like a GeForce RTX 2070 running an 8B model with Pop OS.


💡 KEY INSIGHTS

Use Claude to rewrite emotionally charged emails before sending. Write what you actually want to say unfiltered, then ask Claude to rewrite it professionally. Patrick, Ryan, and Morgan all do this independently. Patrick described it as eliminating email-related stress entirely.

The last mile problem is real and expensive. Getting to 80% quality is easy, 90% is hard, and 95% feels nearly impossible — especially as clients raise expectations after seeing early success.

Scope creep has become app creep and system creep. Because AI enables rapid delivery, clients immediately want more. Asking "is this on the critical path?" and "does this affect an OKR?" is now more important than ever.

When clients start building with Claude Code themselves, they bring partially-built, insecure repos and expect contractors to consolidate and productionize them — often without pausing their own development.

The most valuable skill for working with AI is knowing how to ask good questions. Multiple members converged on this. Formulating precise, contextual questions is described as old-school BA-type knowledge that is now more valuable than ever.

Curiosity is the single most important skill to cultivate. Patrick's direct recommendation for anyone entering the field or advising others.

Patrick's mental model for AI adoption: the current moment mirrors the mainframe-to-PC transition. Today's AI interfaces are like dumb terminals connecting to centralized compute. A small group of specialists are building deeply now. Mass adoption and personalized local models will follow, just faster than before.

Non-technical people can build meaningful things with Claude Code but often do not know what they are building on. Practical advice: run code review and security review skills aggressively, and use third-party auth like Google or Meta instead of rolling your own.

Live demos that produce a working agent are the turning point in AI workshops. Alex reported that skeptical executives become fully bought in the moment they see a working agent connected to Telegram doing real office tasks.

Data sovereignty is a growing concern. Running models locally on repurposed hardware is a viable answer to the "what happens to our data?" objection from enterprise and boutique finance clients.


🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Anthropic's CLI coding agent. Central tool throughout the call.

Codex (OpenAI) — Now installable as a plugin inside Claude Code for code review tasks.

GPT-4o Mini TTS — Used by Patrick for voice output in Claude Speak. Cheapest option with acceptable quality.

Whisperflow — Voice-to-text tool used to speak to Claude Code.

Proxmox — Recommended base infrastructure platform for repurposing gaming PCs. Supports Docker and Claude Code can deploy to it effectively.

DocPloy — Docker deployment tool that can detect CUDA-capable GPUs and route LLM workloads to them.

Tailscale — VPN-style remote access. Broad network access.

Twingate — More restrictive alternative to Tailscale. Allows access only to specified IPs. Preferred for production environments.

Caddy / Traefik — Reverse proxy options. Both are Claude Code-deployable.

Prometheus + Grafana — Monitoring and dashboard stack for self-hosted AI infrastructure.

Pop OS — Linux distribution recommended for AI and CUDA workloads. More CUDA-friendly than standard Ubuntu.

Cohere Re-ranker — Recommended as a layer-two addition to RAG pipelines before considering heavier retrieval systems.

GraphRAG / RLM — Advanced retrieval architectures. RLM adds significant latency and is considered overkill for most current use cases.

Vanta — Third-party SOC 2 compliance management tool.

OKRs and Critical Path — Jake's primary framework for managing scope creep with clients.

Everything Claude Code — Hackathon project from Anthropic. A comprehensive skill and plugin system for Claude Code. Highly recommended by Patrick and Ty.


🔄 FOLLOW-UPS WORTH EXPLORING

Claude Speak live demo — The demo failed during the call due to a microphone conflict. Worth a proper demo next session.

Everything Claude Code deep dive — Both Patrick and Ty flagged this as significant but no one had fully explored it during the call. Worth a dedicated walkthrough in a future session.

FaceGate (Ty's face ID authentication tool) — Ready but missing a feedback widget. Ty planned to share the URL after the call. Worth checking in on and testing.

Repurposing gaming PCs with Proxmox — Ty and Paul both expressed intent to set this up. Alex offered to share his full stack as an MD file. A practical follow-up session or async walkthrough could be valuable for several members.

Ryan's hedge fund expense software — Early stage. Worth revisiting once he has a clearer architecture and compliance scope.

Android and iOS native app development with offline sync — Jake raised this as an open question. No definitive answer was reached. Worth bringing back to the group.

Prakrit's question (sent privately to Patrick) — How to get started building a business idea with AI, validation approach, paper workflow vs. prompting. Not addressed publicly. Worth bringing to the group.

Open source model for managing virtual entities — Paul mentioned a new model in this space but could not recall the name. Worth identifying and sharing.


📝 SUMMARY

This was a wide-ranging and practically dense call covering everything from Claude Code plugins and self-hosted AI infrastructure to compliance for financial clients, scope creep management, and the long-term future of programming as a career. The strongest recurring themes were the importance of asking good questions, the discipline required to manage fast-moving client expectations, and the growing viability of running AI workloads on local hardware for data-sovereign use cases. Several tools and projects were shared that are worth exploring directly, with Everything Claude Code and the Codex plugin standing out as immediate priorities for anyone building seriously with Claude Code.