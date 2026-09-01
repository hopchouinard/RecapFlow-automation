📝 SUMMARY

This week's call was a show-and-tell round robin: members demoed the agent harnesses and workflows they've been building — Scott Rippey's CC BlackBox IDE and Model Radar, Ty Wells' remotely-controlled agent setup, Patrick Chouinard's review-only harness and enterprise "Agentic SDLC" thinking, and Daniel Zivkovic's overnight "Dark Factory" runs. Morgan shared his Supabase-to-Convex migration and got in-depth advice on iOS deployment. The back half tackled two big audience questions: how to build a fully autonomous AI development lifecycle, and how to break into an AI/software engineering career — with candid, practical answers from the group.

💡 KEY INSIGHTS

• Autonomy vs. flexibility trade-off (Patrick): the more autonomous a system or skill is, the less customization freedom you have. Fully autonomous "goal/loop" automation only works when initial requirement quality is very high — agents can only evaluate against hard, testable facts, not opinions.
• Separate coding from reviewing (Patrick): instead of one harness doing both, he's building a review-only agent (based on pi.dev) whose sole job is adversarial code/security review at multiple checkpoints, handing a report to a separate agent to act on.
• Overnight autonomy works — with caveats (Daniel): his "Dark Factory" runs tickets unattended overnight, but parallel tickets can conflict; sequential runs avoid collisions, and better up-front planning means better unattended output.
• Keep agent tasks small (Elena): autonomous agents drift unless tasks are tightly defined — too much scope and they wander off-target.
• "Intent capsules" (Ty): self-contained context bundles let a cold session start with zero prior context and still fully execute a plan — the key to gapless switching between Claude/Codex subscriptions when usage limits hit.
• Write skills like Matt Pocock (Morgan/Patrick): short, modular, non-sequential skills that can be invoked independently are the model for good skill design.
• Just-in-time training beats static courses (Patrick): Pocock's /teach builds an interactive, quiz-based mini-course scoped to exactly what you don't know — replacing internal training that's obsolete by the time it's finished.
• Hiring has shifted (Paul): companies want self-starters who've already built and shipped personal projects — a visible portfolio beats promised ramp-up time.
• Curiosity is the real value of a second person (Daniel, citing Avery.tv): pair a junior with a senior, both using AI — the point is someone who challenges your AI-assisted conclusions rather than echoing them.
• AI-written CVs: optimize, don't embellish (Patrick/Ryan): restructure real experience for the specific job. Write it yourself first, have AI critique it, then rewrite the improvements yourself to keep a human voice. Daniel adds: pull live job-posting data to see which skills and keywords are actually in demand.

❓ KEY Q&A

Q: Can you run a fully autonomous AI development lifecycle — what about guardrails, security, observability? (Elena)
A: "Fully autonomous" is a misnomer — a human always supplies intent. Matt Pocock's skills are a strong baseline for advanced developers; Superpower is more guided/autonomous but requires following its process. Goal/loop systems only work when requirements are high quality and testable.

Q: What's a must-have for breaking into a junior AI/software engineering role beyond experience? (Varun)
A: Be a self-starter with visible, self-driven projects. Aim to reach an "intermediate dev" level before applying — companies no longer have time to train juniors from scratch.

Q: For iOS, do I need to build properly in Swift/Xcode, or is there an easier path? (Morgan)
A: Expo lets you build once and deploy to both iOS and Android — sufficient if most logic lives on a backend. It supports GPS, camera, and most native features; the caveat is deeper platform-specific functionality.

Q: What does Expo cost?
A: About $45/month including a limited number of builds and pushes. Batch your changes and build only when work is more complete, since each build draws down your quota.

Q: What's the storage model for offline app functionality?
A: SQLite for cross-platform offline storage, layered independently of Expo.

Q: Is Ty's mobile/remote session control a plugin?
A: No — custom-built around a personal need. It uses Proxmox so sessions clone over and keep running remotely when his laptop closes, accessible from his phone.

Q: How many AI subscriptions does Patrick run?
A: One Claude account and one Codex account, about $100/month each, flipping between them as needed.

🛠️ TOOLS AND CONCEPTS MENTIONED

• CC BlackBox — Scott's Electron-based Claude Code IDE/agent harness for Mac, with cross-machine sync and usage/cost reporting.
• Model Radar — Scott's hybrid AI/rule-based scanner tracking which AI models are active vs. deprecated across local project folders.
• pi.dev — open-source, model-agnostic agent harness Patrick is customizing into a review-only harness.
• Matt Pocock skills — /teach (just-in-time quiz-based training), /grill-me (requirements grilling), Wayfinder (code review), /wait-what, and "unslop" (cleans up AI response slop).
• Superpower — agentic skill framework; more guided/autonomous but less flexible than Pocock's skills.
• Compound engineering (every.to) — framework behind Daniel's "Dark Factory" overnight ticket runs; also cited for its junior+senior+AI hiring model.
• Intent capsules — Ty's self-contained context bundles enabling cold-start sessions and automatic subscription switching.
• CMUX — base for Ty's custom agent harness with browser control for testing.
• Claude Code / Codex / GitHub Copilot CLI — core coding agent CLIs; Patrick ported a Codex-style review plugin to Copilot CLI for work.
• CC-StatusLine — Patrick's open-source Claude Code status line plugin (session usage, time remaining, git branch).
• Convex — sync database with WebSockets built in; Morgan's migration target from Supabase.
• Expo + SQLite — cross-platform mobile deployment and offline storage.
• SumSub / Clerk — biometric ID verification (escalated from Clerk's base-level auth) for driver/AML use cases.
• LanceDB — vector DB used by Daniel and Paul for RAG/grounding work.
• Fable + Hermes — Patrick's AI "thinking partner" for requirements and prompt work, plus the custom agent that manages his dev environment and preps weekly Fable prompts.

📎 SHARED RESOURCES

• CC BlackBox repo (Scott): https://github.com/scott-rippey/cc-blackbox-app
• Model Radar repo (Scott): https://github.com/scott-rippey/model-radar-app
• CC-StatusLine plugin (Patrick): https://github.com/hopchouinard/CC-StatusLine
• Patrick's plugins repo: https://github.com/hopchouinard/patchoutech-plugins
• Compound engineering guide: https://every.to/guides/compound-engineering
• Theo (T3.gg) video on Matt Pocock's skills: https://www.youtube.com/watch?v=0oXOOlqVu5M
• AWS AI-DLC workflows (shared by Elena): https://github.com/awslabs/aidlc-workflows
• Prof. Joseph Eli Kasser's systems-thinking course: https://therightrequirement.com/
• SumSub biometric verification pricing: https://sumsub.com/pricing/
• "unslop" skill (recommended by Morgan): https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md
• Example developer portfolio site (shared by Ryan C): https://www.zalak-patel.com/
• Daniel's output-optimization methodology: https://lnkd.in/p/gTQAAjrS
• Daniel's LinkedIn (for networking): https://www.linkedin.com/in/magmainc/
• Patrick's daily YouTube follows: t3dotgg, mattpocockuk, indydevdan, NetworkChuck, BuildingwithReason, unsupervised-learning, AndrejKarpathy, NateBJones

🔄 FOLLOW-UPS WORTH EXPLORING

• Scott will share the full walkthrough/blog content for "Power Your Process AI" and is adding browser-control integration to CC BlackBox next.
• Paul Miller will demo his AI-powered CRM reporting next week (customer-data-safe version).
• Paul and Ryan are scheduling a separate call to demo Ryan's Apple/Android emulator testing setup.
• Patrick is continuing his pi.dev-based review-only harness and his combined Superpower + Pocock enterprise "Agentic SDLC" skill layer.
• Morgan's open thread: Convex migration progress and the Expo vs. native Swift decision.
• Varun may test a prompt-injection/steganography trick against ATS screeners — only for large enterprises he's not seriously pursuing. Results could be worth sharing.
• Elena's autonomous-DLC exploration via AWS's aidlc-workflows is worth revisiting.