📝 SUMMARY

This coaching call brought together founders and developers navigating the tension between product development and market validation. Brandon Hancock shared a candid business update on EMS SOAP pivoting its ideal customer profile from slow-moving fire departments to faster-closing private ambulance companies under cash-flow pressure. Patrick Chouinard detailed his enterprise Claude Code rollout expanding from 250 to 2,500 users, including a self-improving support knowledge base and automated training generation. The group also demoed diverse projects including Agent Task for cross-agent orchestration, a multi-model security review system, fully automated ERP pipelines, an AI photo booth, and school pickup management software. Throughout, Brandon coached on sales segmentation frameworks, disciplined outreach habits, and productizing internal tools while technical discussions covered cross-model review strategies, local model use cases, and AI architecture decisions.

💡 KEY INSIGHTS

Whale/Minnow/Tuna Segmentation: Brandon introduced a sales framework distinguishing whales (huge slow contracts taking a year or more), minnows (small deals handled via automation), and tunas (mid-size $20-40k accounts closing in months). Most startups should focus limited selling time on tunas for sustainable growth.

Cash-Flow Driven ICP Pivots: While standard advice suggests staying with one avatar until saturated, burning startups may need to pivot ICPs specifically to accelerate sales cycles when survival is at stake.

Sales Enablement as Champion Creation: Providing prospects with case studies, ROI calculators, and one-pagers they can hand up their chain of command turns customers into internal advocates who sell to both department heads and budget authorities.

Cross-Model Review Discipline: Never use the same model family to review code it generated. Using Claude for generation and Codex (or another vendor) for review surfaces different cognitive biases and catches issues the original model misses.

Local Models for Background Tasks: Small local models like GPT-OSS-20B or Qwen 9B are not replacements for frontier models like Opus but excel at stable, low-cognition, 24/7 background tasks where you want deterministic behavior without burning premium tokens.

Plan Quality Determines Rework: Most AI-assisted coding rework stems from under-specified plans rather than the coding agent itself. Adding a "poke holes" review step after planning significantly reduces downstream cleanup.

Fuzzy Matching for Findings: Model-authored security findings vary in phrasing across runs, requiring fuzzy matching on title and body content rather than exact string matching to avoid false-positive dismissals.

Case Studies Over Early Revenue: Giving product away free to a handful of customers in exchange for measurable before/after results creates collateral that makes future sales conversations about outcomes rather than features.

Loom Structure for Outreach: Follow "Promise, Proof, Next Steps" in sales videos. State the outcome you will deliver, show proof you have done it before, and give a clear call to action without long backstory.

Gate Coding with Sales Milestones: Discipline patterns shared by multiple founders include blocking further development until outreach milestones are hit, such as sending five Looms or signing ten customers, forcing market validation over endless feature building.

HTML Over PowerPoint: Interactive HTML presentations generated via Claude Design outperform PowerPoint for outreach decks because animations, transitions, and interactivity are easier to generate than hand-building slides.

❓ KEY Q&A

Q: How do you give engineers unlimited AI budgets without CEO fear?
A: Start with an arbitrary budget, raise it incrementally as users request more via usage data, and size enterprise plans around real plateau patterns. Only about five percent of users need significantly more than the baseline.

Q: Did engineers see real productivity gains from Claude or was it hype?
A: Heavy Claude Code users showed real data where engineering work requiring a three-person team for a year was completed by one person in three months, providing clear ROI evidence.

Q: How does cross-model review actually work in practice?
A: It uses a slash command inside Claude Code with the official OpenAI Codex plugin, which automatically feeds the last artifact produced to Codex for adversarial review without manual copying.

Q: What is Agent Tax exactly?
A: It is a space-based source of truth where teams organize projects and tasks, claim and track work across sessions and computers via MCP and plugins, maintaining full session history and progress visibility weeks later.

Q: Is Superpowers still worth using now that Opus 5 exists?
A: Yes, it remains valuable for enforcing a full brainstorm to spec to plan to build workflow. The artifacts produced become reusable inputs for training generation, documentation, and presentations.

Q: When do local models actually make sense versus Opus?
A: Local models work best for background twenty-four-seven jobs needing light cognition without burning tokens, such as automated monitoring or simple classification tasks, rather than day-to-day complex development work.

Q: How do you handle destructive requests in an automated WhatsApp support pipeline?
A: A classifier flags anything beyond scope or existing intent documents for manual approval via Telegram before execution, while new features require sign-off and fixes proceed automatically with safeguards.

Q: Are you running security review agents on paid API tokens or existing subscriptions?
A: Currently runs on existing Codex and Anthropic subscription plans with a Node CLI as the local orchestrator and Supabase for tracking, meaning no marginal API cost per review.

🛠️ TOOLS AND CONCEPTS MENTIONED

Claude Code: Primary coding agent used by nearly all participants for development and cross-model reviews via the Codex plugin.

Superpowers: Third-party Claude plugin enforcing brainstorm to spec to plan to build workflow, creating reusable artifacts for training and documentation.

Agent Task: Cross-agent task orchestration and source-of-truth platform for tracking work across sessions and computers.

Codex Plugin for Claude Code: Official OpenAI plugin allowing Claude Code to invoke Codex for adversarial review of specs, plans, and code.

Local Models: GPT-OSS-20B and Qwen 9B for stable, low-cost background tasks requiring twenty-four-seven operation without premium token costs.

Loom: Video recording tool for async sales outreach following the promise, proof, next steps framework.

Instantly: Cold outreach and email warm-up tool for automated minnow lead generation.

Supabase and Vercel: Backend database and frontend hosting stack used for security review dashboards and application hosting.

Claude Design: Anthropic tool for converting PowerPoint decks into interactive HTML presentations with better animations and interactivity.

Even Realities: AI-assisted smart glasses with real-time transcription and overlay capabilities.

Fable: Claude-family sub-agent used for dispatching independent review and testing sessions.

Hermes: Agent and install system being set up as a personal assistant framework.

📎 SHARED RESOURCES

class2curb.com and class2curb.ai — School pickup and dismissal management SaaS

ttl.golf — Golf tee-time organizing application

evenrealities.com — Smart glasses with AI transcription and overlay features

github.com/openai/codex-plugin-cc — Official OpenAI Codex plugin for Claude Code

github.com/hopchouinard/patchoutech-plugins — Personal Claude plugin marketplace repository including status line tools

agent-task.com — Agent Task cross-agent task platform

youtube.com/@BuildingwithReason — Scott Rippey's YouTube channel on AI development

mdt.mt.gov/business/grants-ems.aspx — Montana DOT EMS grant program page

🔄 FOLLOW-UPS WORTH EXPLORING

Alireza will record demo videos of Agent Tax in action to clarify differentiation from standard Claude Code workflows.

Scott is considering building a freemium or plugin version of his security review tool to start market conversations and gather user feedback.

Brandon will test Claude Design for converting PowerPoint sales presentations into interactive HTML slides.

Ryan will draft a good versus bad photo checklist to standardize inputs from amateur photographers for scaling AI real estate video services.

Patrick and Scott discussed adding an enterprise governance and compliance rule layer to the security review tool for organizational policy checking.

Morgan will validate Class2Curb pricing assumptions regarding salary versus hourly staff costs with real customers before finalizing pitches.

Morgan committed to producing three to five Loom outreach videos daily before allowing himself to continue coding features.

Juan will share a promotional video of his AI photo booth product for Brandon to forward to potential venue rental partners.
