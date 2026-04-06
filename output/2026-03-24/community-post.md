📎 SHARED RESOURCES

Claude Certified Architect Foundations Exam Guide (Official PDF, 40 pages)
https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773274827%2FClaude+Certified+Architect+%E2%80%93+Foundations+Certification+Exam+Guide.pdf

Claude Architect Certification Interactive Study App (built by Ty Wells — includes flashcards, quizzes, video summaries, and a Q&A chatbot)
https://anthropic-claude-architect.vercel.app/

Claude Certified Architect Exam Registration
https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request

CMux — Multi-Instance Claude Code Manager (run multiple Claude Code sessions simultaneously)
https://cmux.com/

Patrick's AI Personality Kit for CLI tools (Claude Code, Gemini CLI, Copilot CLI, Codex CLI)
https://github.com/hopchouinard/ai-personality

Patrick's CMux Plugin for Claude Code
https://github.com/hopchouinard/patchoutech-plugins

OpenClaw Security Architecture Guide (governance-first AI agent white paper)
https://opclwsec.patchoutech.com/

NVIDIA NemoClaw (alternative secure Claude architecture for self-hosted AI)
https://github.com/NVIDIA/NemoClaw.git

Three Buckets AI Framework (Elijah Stambaugh — useful for AI consulting and enterprise transformation)
https://threebuckets.ai

Databricks Medallion Architecture Reference
https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion

Session Buddy (browser tab manager for developers juggling many research threads)
https://sessionbuddy.com/

Accelerando by Charles Stross (sci-fi novel about living through the singularity — Brandon's top book recommendation, audiobook preferred)
https://a.co/d/0c9ni2OH

The Phoenix Project (book on systems thinking and SOPs — recommended for anyone doing AI consulting)


❓ KEY Q&A

Q: What are best practices for implementing Stripe without getting lost in key management?

Store only the Stripe customer ID in your app database. For everything else — subscription status, plan details, payment history — query Stripe directly at runtime. This prevents stale data and simplifies your data model. Use the Stripe CLI (ideally controlled by Claude Code or Codex) to automate product and key setup. Lemon Squeezy was mentioned as a simpler alternative. For donations specifically, PayPal has the best feature support.


Q: Are the ShipKit projects still relevant given how fast things are moving?

Core concepts (chat, RAG, Vercel AI SDK) remain valid and unchanged. The main shift is in tooling: the community has largely moved from Cursor to Claude Code as the primary development environment. CMux is now recommended for managing multiple Claude Code instances. For beginners, ShipKit is still the right starting point. Advanced users should layer in the newer tools on top.


Q: What is the best model for non-thinking consumer app use cases?

GPT-5.4 with thinking disabled has outperformed all other models tested for consumer-facing applications. Gemini Flash is the fastest option. For Claude Code specifically, Opus with the 1-million-token context window is the current recommendation — the larger context window reduces compaction interruptions during long sessions.


Q: Telegram vs. Discord as a communication layer for AI agents — which is better?

Both work. Telegram is easier to set up. Discord is preferable for more complex setups because you can split conversations into separate channels by topic, preventing context from different domains from polluting each other. This allows significantly more total content to be maintained across the agent's memory. Patrick recommends Discord for any setup that is growing in scope.


Q: What is Databricks and when should you use it?

Databricks is a lakehouse platform combining the speed and structure of a data warehouse with the flexibility of a data lake. It excels at both analytical queries and raw data processing with low latency, and integrates ML, AI pipelines, and dashboards. It does not store data itself — it sits on top of GCP, AWS, or Azure bucket storage using a proprietary format called Delta Lake. Best suited for data-heavy processing workloads.


Q: How do you handle ideation on the go and pass it into your development workflow?

Brandon: Open Claude on mobile, dictate the idea via microphone, and have Claude Code save it as a new task template to a branch. Pull the branch when back at the desktop. Whisper Flow on iPhone is recommended for fast voice-to-text.

Patrick: Uses ChatGPT voice (best voice model available) for extended ideation while driving. Asks ChatGPT to compile the conversation into a PRD at the end. The PRD goes into his CoworkOS design layer, which breaks it into feature-sized tasks and prepares a package for Claude Code to execute.

Key friction point noted: ChatGPT has the best voice model; Claude has the best development model. They do not currently interoperate.


Q: Is 99.7% face recognition accuracy sufficient for authentication?

For time-and-attendance and shared-device use cases, yes — it is significantly more secure than passwords. The system stores only an encrypted mathematical vector of the face, not the image itself. A new vector is captured at every authentication event, effectively rotating the credential daily without user action.

Important legal caveat: In the U.S., law enforcement can compel face unlock without a warrant but cannot compel disclosure of a passcode. This is a material consideration for any application handling sensitive data.


💡 KEY INSIGHTS

Self-Improving AI Pipelines — The Most Actionable Framework Shared This Call

Build systems that eliminate the human from the evaluation loop. The process: define explicit pass/fail criteria and a point-based rubric for what good output looks like, build a representative input suite (e.g., 60 test cases), let the AI run experiments, grade its own outputs, identify failure modes, update its own system prompt, and iterate. Apply this at the individual pipeline step level first, then at the full system level. Brandon is using Codex for this because it runs autonomously for long periods without prompting for human confirmation. This approach is expensive but produces measurable, compounding improvement.


The Hardest Part Is Defining "Good"

For mathematical outputs, scoring is straightforward. For language outputs — narratives, documents, summaries — defining what "good" means is the core challenge. Patrick's approach: use mechanical checks (did all URLs get extracted? is compression within bounds?) for the fast inner loop, and use community feedback as the slow outer loop for subjective quality.


Governance Before Features for AI Agents

When building a personal or business AI agent, prioritize governance before adding capabilities. Recommended architecture: read-only access to most systems, human-in-the-loop via Discord or Telegram for any action that changes state, full audit trail, and a smart router that uses local models (Ollama) for routine tasks and frontier models only for complex ones. This is the core principle behind the IronClaw framework Scott and Patrick have been building.


Infrastructure as Code Is Underused by Vibe Coders

Terraform gives Claude Code a source of truth for your cloud infrastructure state, makes changes reproducible, and eliminates the "what is the current state of my database?" problem. Claude Code knows Terraform well. If you have already built infrastructure manually, you can work backwards — ask Claude Code to inspect your existing setup and generate the Terraform files from it.


Building in Public Creates Inbound Opportunities You Cannot Manufacture

Patrick published a project to a public GitHub repo. An architect at a client company found it through GitHub's search agent while looking for an internal solution. This led to a production contract. The lesson: public repos are a discovery surface that outbound outreach cannot replicate.


The Zero Token Challenge

Brandon's personal challenge is to max out every AI subscription every week. You can only hit token limits by building systems that run autonomously for extended periods — you cannot do it through manual prompting alone. This constraint forces better automation design.


Every Business Runs on About 12 SOPs That Aren't Written Down

Brandon's framing for AI consulting: every employee at a small business executes roughly 12 standard operating procedures that exist only in their head. The job of an AI consultant is to surface those SOPs, codify them, and build agents to execute them. You discover what context is missing by running the agent at scale and observing where it fails.


🛠️ TOOLS AND CONCEPTS MENTIONED

CMux — Manages multiple simultaneous Claude Code instances. Significant productivity upgrade for power users. cmux.com

Claude Code with Opus and 1M context — Current recommended setup for Claude Code. Larger context window reduces compaction interruptions during long sessions.

Codex (OpenAI) — Preferred over Claude Code for long-running autonomous tasks. Requires fewer human check-ins, making it better suited for multi-hour self-improving experiment loops.

Whisper Flow — iPhone app for fast voice-to-text. Used to dictate ideas directly into Claude Code on mobile.

Terraform — Infrastructure as code. Gives AI agents a reliable source of truth for cloud infrastructure state. Claude Code knows it well.

Databricks / Delta Lake — Lakehouse platform combining data warehouse and data lake capabilities. Used for data-heavy AI pipeline deployments.

IronClaw — Secure, auditable, locally-hosted AI agent architecture with governance-first design and human-in-the-loop controls.

Ollama — Local model runner. Used in IronClaw to route routine tasks away from expensive frontier models.

Fieldy — Wearable ambient recording device. Transcribes accurately even in adjacent rooms. Offers a webhook for piping output to N8N or other automation tools.

Plaud — Wearable recorder that attaches to the back of a phone. Brandon's current recommendation for meeting recording when Fathom is blocked. Also records system audio via desktop app.

Limitless — Previously a leading ambient recording platform. Now acquired by Meta. Existing users have until September 2026 before the service ends.

Eleven Labs — Text-to-speech platform. Scott uses it with a custom Jarvis voice to convert his daily AI news digest into audio.

Vanta — Compliance automation platform. Ty is considering it for security review of his FaceGate biometric SDK.

CoworkOS (Patrick) — Patrick's configured Claude environment with memory, personality, and skills. Acts as a design layer between ideation and implementation. Parses PRDs and hands off structured feature packages to Claude Code.

FaceGate (Ty Wells) — In-development face authentication SDK for web apps. Stores only encrypted face vectors, not images. Designed for shared-device environments.

Immersed — VR app for Meta Quest 3 that creates a multi-monitor coding environment. Scott uses it for full-day coding sessions.

Auto-Research (Karpathy) — The philosophical framework behind self-improving AI loops. Core principle: define a scoring function, run experiments, let the system update itself. Applicable beyond ML to any domain with definable quality criteria.

Notion AI with MCP — Elijah runs an MCP integration to pull context from Notion pages directly into Claude Code.

Session Buddy — Browser extension for saving and annotating large numbers of open tabs.

Lemon Squeezy — Stripe alternative. Simpler to set up but takes a higher cut.


🔄 FOLLOW-UPS WORTH EXPLORING

RecapFlow community experiment — Patrick is asking community members to comment on the weekly recap post. Those comments will be fed back into the auto-research improvement loop as training signal. The more specific your feedback, the better. Worth participating actively over the coming weeks.

Ty's FaceGate SDK — Ty plans to have a testable version ready for the next call where community members can attempt to enroll, verify, and try to break the system. Worth revisiting.

Scott's IronClaw white paper — Scott plans to share the full 40-plus page document in the community. He and Patrick recommend reading it even if you never intend to implement it, as the governance-first thinking is broadly applicable.

Scott's AI News Digest — Scott runs a daily AI news email with an Eleven Labs Jarvis voice audio version.

Brandon's customer success manager agent — Brandon's startup is building an AI agent to handle customer success monitoring. He expects to have it built by the next call and will share results.

Elijah's competition win — Elijah and his son won a competition but cannot share details for another week or two. Follow up at the next call.

Anthropic terms of service for Claude subscriptions via Agent SDK — Scott flagged that using your Claude subscription via the Agent SDK in a web app may violate Anthropic's terms of service. Codex does not have this restriction. Anyone building Claude-backed web apps should verify their compliance posture before shipping.

Elijah's embed and equip consulting programs — Elijah is developing two consulting offerings for legacy businesses adopting AI and is forming a cohort. Worth following as he refines the model.


📝 SUMMARY

This was a dense, high-signal call covering everything from self-improving AI pipelines and governance-first agent architecture to Stripe best practices, biometric authentication, and mobile ideation workflows. The strongest through-line was the shift from using AI interactively to building systems that run autonomously — defining quality rubrics, letting agents evaluate and improve their own outputs, and removing the human from the loop wherever possible. Practical tool recommendations (CMux, Codex for autonomous tasks, Terraform for infrastructure, Discord over Telegram for agent memory) were grounded in real production experience. The IronClaw white paper, Ty's FaceGate SDK demo, and Patrick's RecapFlow auto-research experiment are the most concrete follow-ups to watch for in the coming week.
