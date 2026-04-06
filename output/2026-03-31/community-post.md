📝 SUMMARY

This week's call was packed with practical value across project showcases, tool discoveries, and substantive discussions on the future of work. Members shared live demos and early-stage builds including a Claude Code plugin ecosystem with voice integration, a facial recognition clock-in app, an AI news digest blog, and hedge fund expense software. The group also dug into RAG architecture decisions, scope creep management in an AI-accelerated world, repurposing gaming PCs as local AI servers, and which careers are most defensible as AI capabilities expand. The throughline across all of it: the people who thrive will be those who know how to structure problems and ask the right questions, not just those who can execute tasks.


💡 KEY INSIGHTS

Working WITH AI versus delegating TO AI is the critical distinction for career longevity. Structuring problems, designing workflows, and asking good questions remain deeply human skills.

Curiosity is the single most important skill to cultivate right now. Breadth of knowledge and subjective experience build the judgment that AI cannot replicate.

Knowledge work with no judgment calls is most at risk. If your job is following a decision tree and clicking through steps, it is automatable. Cybersecurity and skilled trades are the most defensible paths.

Scope creep has become app creep. Because AI enables rapid prototyping, clients immediately want more features. Anchor every request back to OKRs and critical business needs before agreeing to anything.

Clients who create chaos are also your best source of ongoing work. The problems they generate are the reason you have a mandate.

Using AI to rewrite emotionally charged emails before sending is a simple, immediately applicable workflow. Write what you actually want to say, then let Claude rewrite it professionally.

Small RAG systems under roughly 1,000 documents are increasingly unnecessary as context windows grow. RAG remains essential for large document libraries. Re-ranking via tools like Cohere is a better first step than jumping to heavier solutions like RLM.

Non-technical founders building with Claude Code often do not know their own tech stack, database, or cost structure. A quick audit conversation can save them thousands and earn lasting trust.

Repurposing a gaming PC as a local AI server using Proxmox, Docker, and Tailscale or Twingate is a practical, cost-effective alternative to burning cloud GPU dollars.

Data sovereignty is a real selling point for boutique finance and professional services firms. Local model deployments that keep data off external networks are a viable product offering.

IT adoption follows a historical cycle: mainframe to PC to cloud to AI. We are currently in the mainframe era of AI, with specialists leading and mass adoption coming. Local personalized models are the next PC era.


❓ KEY Q&A

Q: Which jobs will be most impacted by AI, and in what timeframe?
A: The more useful question is which jobs will not be impacted. Knowledge work with no judgment calls is most at risk. Cybersecurity, skilled trades, and data center construction are most defensible. Programming is not going away, but syntax is being automated while architectural thinking and problem structuring still require humans. Multiple participants agreed that the ability to ask good questions and think across domains is the meta-skill.

Q: Should young people entering the workforce pursue tech careers?
A: Cybersecurity is the strongest tech recommendation. Avoid pure programming or sysadmin paths unless the person understands their role will shift to directing AI rather than writing code. Skilled trades remain highly defensible. Breadth of knowledge and subjective experience matter more than any single degree path.

Q: Will workers have personal AI agents as part of their daily workflow in 3 to 5 years?
A: Yes, universally agreed. The first agent most people already use is ChatGPT or similar. Over time, agents will be personalized to individual workflows and deficits. Paul cited OECD education research showing governments are already deploying personalized AI teacher aides as a model for what is coming in the workplace.

Q: Is RAG going away? What replaces it?
A: RAG is not going away for large document libraries. Small RAG use cases are being replaced by large context windows and agentic search. The recommended layered approach is RAG as layer one, a re-ranker like Cohere as layer two, and RLM or GraphRAG only for very large-scale or complex retrieval needs. RLM adds latency and is overkill for most current use cases.

Q: What is the best approach for building iOS and Android native apps with offline sync using Claude?
A: Start with a cross-platform framework like React Native. For iOS native, use Xcode with Claude Code but note it requires setup and Claude's understanding of the stack is still somewhat brittle. Finding a well-starred GitHub repo as a starting scaffold is recommended. Android guidance was less certain and deep research on GitHub is advised.

Q: How do you handle compliance such as SOC 2, HIPAA, and ISO for financial software?
A: SOC 2 Type 1 is a common starting point. Tools like Vanta automate much of the compliance process. Piggybacking on a SOC 2-compliant cloud partner like AWS, Azure, or GCP is another path. Financial firms often prefer Azure. Cyber insurance can cover known gaps while you build toward full compliance. Having a qualified CISO and DevOps person is strongly recommended for financial verticals.

Q: How do you manage clients who keep expanding scope because AI makes everything feel fast and easy?
A: Anchor every request to OKRs and the critical business path. Jake's practice is to explicitly ask on every call whether a request is a critical path item and deprioritize anything that does not affect an OKR. Ty's practice is to define scope upfront and put new requests on a waitlist. Patrick's reframe is that clients who create chaos are your best long-term customers because they continuously generate problems you can solve.


🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code — Primary coding agent used by most members and central to nearly every project showcase this week.

Codex Plugin for Claude Code — Allows OpenAI Codex to run inside Claude Code for adversarial code review, saving Claude tokens for creation tasks.

Everything Claude Code (GitHub) — Hackathon-winning project from Anthropic featuring hundreds of agent plugins and skills that upgrade Claude Code. Described as worth reviewing immediately.

GPT-4o Mini TTS — Used by Patrick for Claude Code voice output. Very cheap at roughly one dollar per day of heavy use with decent quality.

Whisperflow — Voice-to-text tool used to talk to Claude Code. Mentioned as a candidate for local deployment on a gaming PC.

RecapFlow — Tool used to generate call summaries, described as dialed in by Patrick.

LabSync — Patrick's custom tool to sync new plugins and skills to his marketplace and lab website automatically from GitHub repos.

RAG (Retrieval-Augmented Generation) — Core architecture for large document retrieval. Still the standard but increasingly supplemented for smaller use cases.

Re-ranker (e.g., Cohere) — Recommended as layer two on top of RAG before considering heavier solutions like RLM.

RLM (Retrieval-Language Model loop) — More powerful but slower RAG enhancement. Recommended only for very large-scale data needs.

GraphRAG — Next-generation RAG variant mentioned as an emerging alternative for complex retrieval.

Proxmox — Recommended platform for turning a gaming PC into a full local AI infrastructure server. Supports GPU passthrough, Docker, reverse proxy, and monitoring.

DocPloy — Docker deployment tool used as an alternative to Proxmox for local server management.

Tailscale — VPN and mesh networking tool for remote access to local servers.

Twingate — More restrictive alternative to Tailscale. Preferred by Patrick for security due to IP-specific access controls.

Caddy and Traefik — Reverse proxy options for local server setups. Patrick prefers Traefik.

Prometheus and Grafana — Monitoring and dashboarding stack recommended for local AI infrastructure.

Pop OS — Linux distribution recommended for AI and CUDA workloads. Described as more GPU-friendly than standard Ubuntu.

Vanta — Compliance automation tool for SOC 2. Described as the go-to option by Jake.

FaceGate — Ty's web-native facial recognition authentication system built for multi-user device clock-in and clock-out.

Unitree R1 — Humanoid robot available for under $13,000. Cited as evidence that robotics timelines are closer than most expect.

Resend — Email delivery service used by Scott for his AI news digest.

Xero — Accounting software mentioned as an integration target for Ryan's hedge fund expense app.


📎 SHARED RESOURCES

Codex Plugin for Claude Code
https://github.com/openai/codex-plugin-cc
Allows Codex to run inside Claude Code for code review. Useful token-saving strategy.

Patrick's Lab Site
https://lab.patchoutech.com/
Central hub for all of Patrick's Claude Code plugins, skills, and tools. Growing weekly and worth bookmarking.

Everything Claude Code (GitHub)
https://github.com/affaan-m/everything-claude-code
Hundreds of agent plugins and skills for Claude Code from an Anthropic hackathon. Highly recommended to explore.

Scott's AI News Digest Blog
https://news.poweryourprocess.ai/
Publicly browsable AI news blog with audio versions of new posts. Built on RSS feeds, Claude Haiku, and RAG.

Claude Code Leak Reddit Thread
https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/
Community analysis of the Claude Code source leak. Described as entertaining and informative.

NPM Hack Explainer Video
https://www.youtube.com/watch?v=eGSsoSEppNU
Explanation of the major NPM security incident this week. Relevant for anyone with Node.js dependencies.

Unitree R1 Robot
https://ca.robotshop.com/products/unitree-r1-humanoid-robot
Humanoid robot under $13K referenced in the robotics timeline discussion.

Ty's Workshop Tool
https://nperson.ai
Tool Ty uses in AI workshops. Shared for members to explore.

Juan's Diffusion Model Project
https://radiant-shaders.com/
Juan's current project using diffusion models.

Scott's AI Digest Newsletter
Contact scott@poweryourprocess.ai to be added to the email digest with audio summaries of AI news.


🔄 FOLLOW-UPS WORTH EXPLORING

Claude Speak demo — Patrick's voice integration for Claude Code did not fully demo live due to a suspected microphone conflict. Worth a clean demo next session.

Everything Claude Code deep dive — Multiple members expressed interest but had not yet gone through it. Worth a dedicated discussion once members have had time to explore.

Gaming PC to local AI server setup — Ty and Paul both committed to setting up Proxmox and Tailscale local AI server environments. Patrick offered to help. Follow-up on results would be valuable for the whole group.

Alex's local model stack — Alex offered to share an MD file with his full local AI stack including Pop OS, Ollama, and a Whisperflow equivalent. Ty expressed interest. This should be shared in the community.

iOS and Android offline sync frameworks — Jake raised the question of best frameworks for native apps with offline sync. No definitive answer was reached. Worth researching and reporting back, particularly around React Native and local database sync options.

Ryan's hedge fund expense software — Early-stage project with significant potential. Ryan mentioned connecting with Brandon about compliance. Worth checking in on architecture decisions and the compliance path chosen.

OpenAI's upcoming model referred to as SPUD — Paul mentioned OpenAI shutting down Sora to make way for a new model releasing in two to three weeks. Worth tracking.

Alex's AI workshop business model — Alex is running four-hour workshops for around $1,200 and exploring local model product offerings for data-sovereign clients. The group showed interest and a fuller discussion would be worthwhile.

Open source model for managing virtual entities — Paul mentioned a recently released open source model in this space but could not recall the name. Worth identifying and sharing with the group.