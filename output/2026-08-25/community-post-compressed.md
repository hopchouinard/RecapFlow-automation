📝 SUMMARY

This week's call covered agent harness demos, enterprise AI strategies, and mobile deployment. Members showcased tools for tracking AI model usage, automating subscription management, and running agentic workflows from mobile. Topics included rebuilding Codex on banned networks, AI-era hiring philosophies, and cross-platform mobile stacks.

💡 KEY INSIGHTS

Scott Rippey demoed "Model Radar" using hybrid-scanning of local folders and APIs to track active versus deprecated models, plus Bonjour sync across Macs.

Ty Wells automates subscription switching between Claude and Codex based on usage to prevent quota interruptions. His "intent capsules" are self-contained context bundles letting agents execute plans without history, enabling remote mobile work.

Patrick Chouinard recreates Codex reviews on GitHub Copilot CLI when OpenAI tools are banned. He emphasized that "fully autonomous" development is misleading since human intent is always required, and goal-based automation needs hard, testable facts. Just-in-time training via composable skills beats static courses.

Daniel Zivkovic recommends "optometry" style requirements elicitation (prototypes with "this or that" choices) over upfront specs. Parallel AI implementations cause conflicts; sequential overnight runs create morning review queues without collisions.

On hiring, curiosity is the primary signal. Companies expect juniors to perform at intermediate levels, making self-built apps more valuable than credentials. Pairing AI-augmented juniors with seniors prevents echoing AI output that creates "AI slop."

Expo handles most cross-platform mobile needs (GPS, camera, biometrics) unless deep native integrations are required. Pricing is per build push, so batching saves money.

❓ KEY Q&A

Q: For iOS deployment, native Swift/Xcode or easier path?
A: If offloading logic to servers, Expo builds for both platforms while handling credentials and submission. Native offers more control for deep features but requires more effort.

Q: Expo pricing?
A: Approximately $45/month for ~15 build pushes. Batch changes before building.

Q: Expo offline storage?
A: Yes, SQLite or third-party options work cross-platform, syncing when connectivity returns.

Q: Biometric verification stack?
A: SumSub, roughly $1 per full authentication with lighter face-only re-verification for returning users. More polished than Amazon.

Q: Guardrails for fully autonomous AI development?
A: "Fully autonomous" is misleading since human intent is always required. Goal-based automation only works with hard, testable requirements, not opinions.

Q: What do recruiters seek in junior candidates?
A: Self-starters who have built apps and operate at intermediate levels. Curiosity is key. Pair juniors with seniors (both AI-augmented) to prevent echoing AI output. Build a public GitHub portfolio and optimize resumes per job description.

Q: How to avoid "AI slop" in resumes?
A: Write the CV yourself, have AI critique it, then rewrite in your own voice to avoid sameness.

🛠️ TOOLS AND CONCEPTS MENTIONED

Power Your Process AI: Personal app with automated build notifications.
CC Blackbox: Mac-native Electron IDE around Claude Code, tracking usage and cost.
Model Radar: Scans local folders to track active versus deprecated AI models.
CMUX: Agent harness for driving browsers and remote mobile session access.
Intent Capsules: Self-contained context bundles allowing cold agent sessions to execute plans.
CC-StatusLine: Open-source plugin tracking Claude Code usage, time remaining, and git state.
Pi.dev: Open-source, model-agnostic agent harness for review-only workflows.
GitHub Copilot CLI: Recreates Codex review functionality where OpenAI tools are banned.
Superpower and Matt Pocock Skills: Frameworks including Grill with Docs, /teach, Wayfinder, and unslop for brainstorming, review, and just-in-time training.
Fable: AI thinking partner for requirements and task planning.
Convex: Sync database handling WebSockets automatically.
Expo: Cross-platform mobile framework with managed app store submission.
SumSub: Biometric identity verification service.
Compound Engineering Framework: Enterprise-ready AI-assisted SDLC methodology from every.to.
Dark Factory: Wrapper for overnight sequential ticket implementation runs.
LanceDB: Vector database for grounding and RAG.
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

Scott Rippey will share the Power Your Process AI walkthrough video and add browser-control integration to CC Blackbox.
Patrick Chouinard will continue building his Pi-based review harness and investigate the compound engineering framework for enterprise use.
Paul Miller will demo his AI-driven CRM reporting capabilities next week and coordinate with Ryan C on Expo emulator testing.
Daniel Zivkovic will research Mark Kashif's subscription-multiplexing utility for API-key services.
Varun Sharma will test prompt-injection techniques in resumes applied to non-target enterprise jobs.
Elena's question about AWS AI-DLC workflows and fully autonomous frameworks remains open for future discussion.