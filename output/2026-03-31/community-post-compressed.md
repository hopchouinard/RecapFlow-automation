📝 SUMMARY

This week's call covered project showcases, tool discoveries, and substantive discussions on the future of work. Members demoed a Claude Code plugin ecosystem with voice integration, a facial recognition clock-in app, an AI news digest blog, and hedge fund expense software. The group also explored RAG architecture decisions, scope creep management, repurposing gaming PCs as local AI servers, and which careers are most defensible as AI expands. The throughline: people who thrive will be those who structure problems and ask the right questions, not just those who execute tasks.


💡 KEY INSIGHTS

Working WITH AI versus delegating TO AI is the critical distinction for career longevity. Structuring problems, designing workflows, and asking good questions remain deeply human skills.

Curiosity is the single most important skill right now. Breadth of knowledge and subjective experience build the judgment AI cannot replicate.

Knowledge work with no judgment calls is most at risk. If your job follows a decision tree, it is automatable. Cybersecurity and skilled trades are the most defensible paths.

Scope creep has become app creep. Because AI enables rapid prototyping, clients immediately want more features. Anchor every request to OKRs and critical business needs before agreeing to anything.

Clients who create chaos are also your best source of ongoing work. The problems they generate are the reason you have a mandate.

Using AI to rewrite emotionally charged emails is a simple, immediately applicable workflow. Write what you want to say, then let Claude rewrite it professionally.

Small RAG systems under roughly 1,000 documents are increasingly unnecessary as context windows grow. RAG remains essential for large document libraries. Re-ranking via Cohere is a better first step than jumping to heavier solutions like RLM.

Non-technical founders building with Claude Code often do not know their own tech stack, database, or cost structure. A quick audit conversation can save them thousands and earn lasting trust.

Repurposing a gaming PC as a local AI server using Proxmox, Docker, and Tailscale is a practical, cost-effective alternative to cloud GPU spend.

Data sovereignty is a real selling point for boutique finance and professional services firms. Local model deployments that keep data off external networks are a viable product offering.

IT adoption follows a historical cycle: mainframe to PC to cloud to AI. We are in the mainframe era of AI now, with mass adoption and personalized local models coming next.


❓ KEY Q&A

Q: Which jobs will be most impacted by AI?
A: Knowledge work with no judgment calls is most at risk. Cybersecurity, skilled trades, and data center construction are most defensible. Programming is not going away, but syntax is being automated while architectural thinking still requires humans. The ability to ask good questions and think across domains is the meta-skill.

Q: Should young people pursue tech careers?
A: Cybersecurity is the strongest recommendation. Avoid pure programming or sysadmin paths unless the person understands their role will shift to directing AI. Skilled trades remain highly defensible. Breadth of knowledge matters more than any single degree path.

Q: Will workers have personal AI agents in 3 to 5 years?
A: Yes, universally agreed. Agents will become personalized to individual workflows and deficits. Paul cited OECD research showing governments are already deploying personalized AI teacher aides as a model for what is coming in the workplace.

Q: Is RAG going away?
A: Not for large document libraries. Small RAG use cases are being replaced by large context windows and agentic search. Recommended approach: RAG as layer one, a re-ranker like Cohere as layer two, and RLM or GraphRAG only for very large-scale needs. RLM adds latency and is overkill for most current use cases.

Q: What is the best approach for building iOS and Android native apps with offline sync?
A: Start with a cross-platform framework like React Native. For iOS native, use Xcode with Claude Code but note it requires setup and Claude's understanding of the stack is still somewhat brittle. Finding a well-starred GitHub scaffold is recommended. Android guidance was less certain.

Q: How do you handle compliance such as SOC 2, HIPAA, and ISO for financial software?
A: SOC 2 Type 1 is a common starting point. Vanta automates much of the process. Piggybacking on a compliant cloud partner like AWS, Azure, or GCP is another path. Cyber insurance can cover known gaps while you build toward full compliance. A qualified CISO and DevOps person is strongly recommended for financial verticals.

Q: How do you manage clients who keep expanding scope?
A: Anchor every request to OKRs and the critical business path. Jake explicitly asks on every call whether a request is a critical path item. Ty defines scope upfront and puts new requests on a waitlist. Patrick's reframe: clients who create chaos are your best long-term customers because they continuously generate problems you can solve.


🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Primary coding agent used by most members and central to nearly every project showcase.

Codex Plugin for Claude Code — Allows OpenAI Codex to run inside Claude Code for adversarial code review, saving Claude tokens for creation tasks.

Everything Claude Code (GitHub) — Hackathon-winning project from Anthropic featuring hundreds of agent plugins and skills. Worth reviewing immediately.

GPT-4o Mini TTS — Used by Patrick for Claude Code voice output. Roughly one dollar per day of heavy use with decent quality.

Whisperflow — Voice-to-text tool used to talk to Claude Code. Candidate for local deployment on a gaming PC.

RecapFlow — Tool used to generate call summaries.

LabSync — Patrick's custom tool to sync new plugins and skills to his marketplace from GitHub repos automatically.

RAG (Retrieval-Augmented Generation) — Core architecture for large document retrieval. Still standard but supplemented for smaller use cases.

Re-ranker (e.g., Cohere) — Recommended as layer two on top of RAG before considering heavier solutions.

RLM — More powerful but slower RAG enhancement. Recommended only for very large-scale data needs.

GraphRAG — Emerging next-generation RAG variant for complex retrieval.

Proxmox — Platform for turning a gaming PC into a local AI server. Supports GPU passthrough, Docker, reverse proxy, and monitoring.

DocPloy — Docker deployment tool used as an alternative to Proxmox.

Tailscale — VPN and mesh networking tool for remote access to local servers.

Twingate — More restrictive alternative to Tailscale. Preferred by Patrick for IP-specific access controls.

Traefik and Caddy — Reverse proxy options for local server setups.

Prometheus and Grafana — Monitoring and dashboarding stack for local AI infrastructure.

Pop OS — Linux distribution recommended for AI and CUDA workloads. More GPU-friendly than standard Ubuntu.

Vanta — Compliance automation tool for SOC 2.

FaceGate — Ty's web-native facial recognition authentication system for multi-user device clock-in and clock-out.

Unitree R1 — Humanoid robot available for under $13,000. Cited as evidence that robotics timelines are closer than expected.

Resend — Email delivery service used by Scott for his AI news digest.

Xero — Accounting software mentioned as an integration target for Ryan's hedge fund expense app.


📎 SHARED RESOURCES

Codex Plugin for Claude Code
https://github.com/openai/codex-plugin-cc
Allows Codex to run inside Claude Code for code review. Useful token-saving strategy.

Patrick's Lab Site
https://lab.patchoutech.com/
Central hub for Patrick's Claude Code plugins, skills, and tools. Growing weekly.

Everything Claude Code (GitHub)
https://github.com/affaan-m/everything-claude-code
Hundreds of agent plugins and skills from an Anthropic hackathon. Highly recommended.

Scott's AI News Digest Blog
https://news.poweryourprocess.ai/
AI news blog with audio versions of posts. Built on RSS feeds, Claude Haiku, and RAG.

Claude Code Leak Reddit Thread
https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/
Community analysis of the Claude Code source leak. Entertaining and informative.

NPM Hack Explainer Video
https://www.youtube.com/watch?v=eGSsoSEppNU
Explanation of the major NPM security incident. Relevant for anyone with Node.js dependencies.

Unitree R1 Robot
https://ca.robotshop.com/products/unitree-r1-humanoid-robot
Humanoid robot under $13K referenced in the robotics timeline discussion.

Ty's Workshop Tool
https://nperson.ai

Juan's Diffusion Model Project
https://radiant-shaders.com/

Scott's AI Digest Newsletter
Contact scott@poweryourprocess.ai to be added to the email digest with audio summaries.


🔄 FOLLOW-UPS WORTH EXPLORING

Claude Speak demo — Patrick's voice integration did not fully demo live due to a suspected microphone conflict. Worth a clean demo next session.

Everything Claude Code deep dive — Multiple members expressed interest but had not yet explored it. Worth a dedicated discussion once members have had time to review.

Gaming PC to local AI server — Ty and Paul committed to setting up Proxmox and Tailscale environments. Patrick offered to help. Follow-up results would be valuable for the whole group.

Alex's local model stack — Alex offered to share an MD file with his full local AI stack including Pop OS, Ollama, and a Whisperflow equivalent. This should be shared in the community.

iOS and Android offline sync frameworks — No definitive answer was reached. Worth researching and reporting back, particularly around React Native and local database sync options.

Ryan's hedge fund expense software — Early-stage project with significant potential. Worth checking in on architecture decisions and the compliance path chosen.

OpenAI's upcoming model referred to as SPUD — Paul mentioned it releasing in two to three weeks. Worth tracking.

Alex's AI workshop business model — Alex is running four-hour workshops for around $1,200 and exploring local model offerings for data-sovereign clients. A fuller discussion would be worthwhile.

Open source model for managing virtual entities — Paul mentioned a recently released model in this space but could not recall the name. Worth identifying and sharing with the group.