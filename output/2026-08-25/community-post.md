📝 SUMMARY

This week's call featured a rotating show-and-tell covering personal agent harnesses, enterprise AI adaptation strategies, and mobile deployment tactics. Members demoed custom tools for tracking AI model usage across projects, automating subscription management, and running agentic workflows from mobile devices. Discussions ranged from rebuilding Codex functionality on banned networks to hiring philosophies for the AI-augmented era, with deep dives into cross-platform mobile stacks and biometric verification services.

💡 KEY INSIGHTS

Scott Rippey demonstrated that hybrid-scanning local project folders alongside provider APIs can create a "Model Radar" to track which AI models are active versus deprecated across multiple client apps. He also showed how machine-to-machine sync via Bonjour keeps session databases consistent across multiple Macs.

Ty Wells revealed an automation setup that switches between Claude and Codex subscriptions based on remaining usage percentage, preventing work loss from hitting quotas. His "intent capsules" concept—self-contained context bundles—allows cold agent sessions to execute plans without prior conversation history, enabling remote work continuation from anywhere including mobile devices.

Patrick Chouinard explained how to recreate Codex review mechanics on GitHub Copilot CLI when OpenAI tools are banned at work, satisfying security requirements while maintaining access to frontier models. He emphasized that fully autonomous AI development is a misnomer because human intent is always required, and that goal-based automation only works with hard, testable facts rather than opinions. He also highlighted that just-in-time training via composable skills beats static courses, which become obsolete before completion.

Daniel Zivkovic shared that requirements elicitation works better as an iterative "optometry" process (showing prototypes and asking "this or that") rather than upfront specification. He noted that running multiple AI-generated implementations in parallel causes conflicts, while sequential overnight runs create a morning review queue without collisions.

On hiring, the group agreed that curiosity is now the primary signal—pairing AI-augmented juniors with seniors keeps both honest, while candidates who merely echo AI output blend into the "AI slop." Paul Miller added that companies now expect junior candidates to perform at intermediate levels, making self-built apps and demonstrated initiative more valuable than credentials.

For mobile development, Expo was recommended as sufficient for most cross-platform needs (GPS, camera, biometrics) unless deep native integrations are required, with costs charged per build push so batching changes saves money.

❓ KEY Q&A

Q: For iOS deployment, should one use Swift/Xcode natively or is there an easier path?
A: If the app offloads logic to a server, Expo builds for both iOS and Android while handling Apple credentials and app-store submission. Native development offers more control for deep native features but requires more effort.

Q: What is Expo's pricing model?
A: Approximately $45 per month for roughly 15 build pushes, charged per build. Batch changes before building rather than pushing every iteration.

Q: Does Expo handle offline storage?
A: Yes. SQLite or third-party options work well for cross-platform offline storage, syncing when connectivity returns.

Q: Which stack handles biometric verification?
A: SumSub, costing roughly $1 per full authentication with lighter face-only re-verification for returning users. It was rated more polished than alternatives like Amazon's service.

Q: What guardrails exist for fully autonomous AI development lifecycles?
A: "Fully autonomous" is misleading since human intent is always required. Matt Pocock's skills require developer expertise while Superpower offers more guidance but less flexibility. Goal-based automation only works with hard, testable requirements, not opinions.

Q: What do recruiters seek in junior AI/software engineering candidates?
A: Companies expect self-starters who have already built apps and operate at intermediate levels. Curiosity is the key trait—pairing juniors with seniors (both AI-augmented) prevents echoing AI output. Build a public GitHub portfolio and optimize (don't embellish) resumes per job description.

Q: How can candidates avoid "AI slop" in resumes?
A: Write the CV yourself, have AI critique it, then rewrite improvements in your own voice. This avoids the sameness that makes candidates blend together.

🛠️ TOOLS AND CONCEPTS MENTIONED

Power Your Process AI: Scott Rippey's personal app project with automated build notifications.

CC Blackbox: Mac-native Electron IDE and agent harness built around Claude Code, tracking usage and cost per session.

Model Radar: Tool scanning local project folders to track active versus deprecated AI models across client apps.

CMUX: Ty Wells' agent harness for driving browsers during testing and accessing sessions remotely from mobile devices.

Intent Capsules: Self-contained context bundles allowing cold agent sessions to execute plans without conversation history.

CC-StatusLine: Patrick Chouinard's open-source plugin tracking Claude Code usage, time remaining, and git state.

Pi.dev: Open-source, model-agnostic agent harness being customized for review-only workflows.

GitHub Copilot CLI: Used to recreate Codex review functionality in environments where OpenAI tools are banned.

Superpower and Matt Pocock Skills: Frameworks including Grill with Docs, /teach, Wayfinder, and unslop for brainstorming, code review, and just-in-time training.

Fable: AI thinking partner for requirements discussion and task planning.

Convex: Sync database handling WebSockets automatically, used for migrating away from Supabase.

Expo: Cross-platform mobile framework for iOS/Android deployment with managed app store submission.

SumSub: Biometric identity verification service for driver authentication and re-verification.

Compound Engineering Framework: Enterprise-ready AI-assisted SDLC methodology from every.to.

Dark Factory: Daniel Zivkovic's wrapper for overnight sequential ticket implementation runs.

LanceDB: Vector database for grounding and RAG work.

Doppler: API key management across projects.

📎 SHARED RESOURCES

https://www.youtube.com/watch?v=S_QdQ1G4GlU

https://every.to/guides/compound-engineering

https://lnkd.in/p/gTQAAjrS

https://github.com/scott-rippey/cc-blackbox-app

https://github.com/scott-rippey/model-radar-app

https://github.com/hopchouinard/CC-StatusLine

https://github.com/hopchouinard/patchoutech-plugins

https://www.youtube.com/watch?v=0oXOOlqVu5M

https://sumsub.com/pricing/

https://github.com/awslabs/aidlc-workflows

https://therightrequirement.com/

https://www.youtube.com/@t3dotgg

https://www.zalak-patel.com/

https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md

https://www.linkedin.com/in/magmainc/

🔄 FOLLOW-UPS WORTH EXPLORING

Scott Rippey will share the Power Your Process AI walkthrough video and plans to add browser-control integration to CC Blackbox.

Patrick Chouinard will continue building his Pi-based review harness and investigate the compound engineering framework for enterprise use.

Paul Miller will demo his AI-driven CRM reporting capabilities next week and coordinate with Ryan C on Expo emulator testing strategies.

Daniel Zivkovic will research Mark Kashif's subscription-multiplexing utility for API-key services.

Varun Sharma will test prompt-injection techniques in resumes applied to non-target enterprise jobs as an experiment.

Elena's question about AWS AI-DLC workflows and fully autonomous frameworks remains open for deeper technical discussion in future calls.