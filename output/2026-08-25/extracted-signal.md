## general

This session of the coaching call was largely a round-robin update where members shared what they had built or learned over the prior week, followed by an open Q&A block toward the end. Scott Rippey demoed two personal tools — "Power Your Process AI" and a "Model Radar" app that tracks which AI models are active across local project folders — plus his Electron-based Claude Code IDE/agent harness ("CC BlackBox") with cross-machine sync. Ty Wells discussed his CMUX-derived agent harness with automated subscription switching and mobile/remote session control (built out of necessity to keep working from the golf course). Patrick Chouinard covered a Copilot-CLI port of the Codex review plugin he built for work, an in-progress review-only agent harness based on pi.dev, his broader "Agentic SDLC for the enterprise" thinking (merging Superpower with Matt Pocock's skills), and Matt Pocock's `/teach` skill for just-in-time training.

Later in the call, Morgan shared progress migrating an app from Supabase to Convex using Pocock's "Wayfinder" skill for code review, plus open questions about iOS deployment (Expo vs. native Swift), which Ryan C and Paul Miller answered in depth, including a tangent into biometric identity verification (SumSub) for driver/AML use cases. Daniel Zivkovic discussed his "optometry theory" of requirements elicitation, his "Dark Factory" compound-engineering wrapper, and recommended the compound-engineering framework and systems-thinking coaching from Professor Joseph Eli Kasser.

The back half of the call featured audience questions: Elena asked about fully autonomous AI-driven development lifecycles (guardrails, security, observability), Varun Sharma asked about breaking into an AI/software engineering career, and the group (Paul Miller, Patrick, Daniel, Ryan C) gave extended advice on hiring signals, portfolio-building, CV optimization with AI, and even (half-jokingly) prompt-injection/steganography tricks to game AI resume screeners. Paul Miller closed with an update on AI-powered reporting he's building into his CRM software company's product to compete against Salesforce.

## insights

- **Patrick Chouinard**: There's an inherent trade-off in agentic development — the more autonomous a system/skill is, the less liberty/customization freedom you have, and vice versa. Fully autonomous "goal/loop" style automation only works if the initial requirement quality is extremely high, because these systems can only evaluate against hard, testable facts — not opinions.
- **Patrick Chouinard**: Rather than have one harness do coding + review, he's building a harness (based on pi.dev) that is deliberately *not* a coding agent — its sole job is adversarial code/security review at multiple points (stop hook, pre-commit, branch, whole project) and handing back a report for a separate agent to act on.
- **Daniel Zivkovic**: Fully autonomous parallel ticket runs ("Dark Factory," built around the compound-engineering framework) work reasonably well overnight, but parallel tickets can conflict/step on each other — running them sequentially avoids this. The better the up-front planning, the better the unattended output.
- **Elena**: In practice, autonomous agents drift unless tasks are kept very small and tightly defined; giving too much scope causes them to wander off-target.
- **Scott Rippey**: A hybrid AI + rule-based scanner (Model Radar) can automatically detect which AI models are active vs. deprecated/retired across many local project folders — useful once you have enough client/personal projects to lose track of model usage.
- **Ty Wells**: "Intent capsules" — self-contained context bundles — allow a cold session to start with zero prior context but still fully execute a plan, which is what enables automatic, gapless switching between subscriptions (Claude/Codex) when usage limits are hit.
- **Morgan / Patrick**: Matt Pocock's skills (e.g., `/teach`, `/grill-me`) are notable for being short, modular, and non-sequential — they can be invoked independently rather than requiring a fixed step order, which Morgan cites as a model for how to write good skills.
- **Patrick Chouinard**: Generating training material just-in-time via `/teach` (which builds an interactive quiz-based mini-course scoped to exactly what the user doesn't know) is replacing static internal training courses, which become obsolete by the time they're finished.
- **Paul Miller**: Hiring criteria for developers has shifted — companies increasingly want self-starters who've already built and shipped personal projects, not people expecting on-the-job ramp-up time.
- **Daniel Zivkovic**: Citing Avery.tv's hiring model (pairing one junior + one senior, both using AI), the value of a second person isn't experience per se but curiosity — someone who challenges your AI-assisted conclusions rather than just echoing them back.
- **Patrick Chouinard / Ryan C**: When using AI to write a CV, the goal should be optimization (restructuring/prioritizing real experience for a specific job) rather than embellishment — embellished CVs get caught either by AI screening tools or in the interview itself.
- **Ryan C**: The most effective CV-writing approach is to write it yourself first, have AI critique and suggest improvements, then rewrite the improved sections yourself — keeping the voice human and avoiding the generic "written by ChatGPT" look that makes candidates blend together.
- **Daniel Zivkovic**: Market requirements shift fast enough that it's worth periodically pulling live job-posting data via API to see what skills/keywords are actually in demand before optimizing a resume around them.

## qa

**Q (Daniel Zivkovic):** Is the mobile/remote session control something you developed, Ty, or a plugin available for Claude Code?
**A (Ty Wells):** No, it's custom-built around a personal need (originally for continuing work from the golf course); it uses Proxmox so that when his laptop is closed, sessions clone over and keep running remotely, accessible from his phone.

**Q (Paul Miller):** What about the other three Claude accounts you have to run to keep tokens up?
**A (Patrick Chouinard):** He's actually only running one Claude account and one Codex account, spending about $100/month on each, flipping between them as needed.

**Q (Daniel Zivkovic):** Patrick, have you looked at the "compound engineering" framework?
**A (Patrick Chouinard):** He's not looking for a ready-made framework but rather pieces of various frameworks to modify for enterprise use, since most existing frameworks (including this one, in his view) are built for single developers or small teams, whereas he needs something that scales across users of different technical levels.

**Q (Paul Miller):** Did you see the Theo (T3) video on Pocock's approach?
**A (Patrick Chouinard):** Yes — that video is exactly where he got the inspiration for building his own customized harness/skill approach.

**Q (Elena):** Can I get advice on a fully autonomous AI development lifecycle — guardrails, security, observability, and any good frameworks/implementation blueprints?
**A (Patrick Chouinard):** "Fully autonomous" is a misnomer since you always need a human to supply intent; Matt Pocock's skills are a strong baseline for advanced developers, while Superpower is more guided/autonomous but requires following its process; autonomous "goal/loop" systems only work well when requirement quality is very high, since they need testable facts to evaluate against, not opinions.

**Q (Varun Sharma):** Beyond experience, what's a must-have that recruiters/companies look for from someone trying to break into a junior AI/software engineering role?
**A (Paul Miller):** Hiring now favors self-starters — people who show what they've built for themselves, ideally getting to an "intermediate dev" level before applying, since companies no longer have time to train juniors from scratch; building a visible portfolio of self-driven projects is the differentiator.

**Q (Daniel Zivkovic):** What storage model do you use for offline app functionality — Firebase? Is it part of Expo?
**A (Paul Miller):** SQLite is used for cross-platform offline storage (a third-party option is also possible), and this is layered independently of Expo itself.

**Q (Morgan):** Can you tell me about the Expo subscription model — what's the monthly cost structure?
**A (Ryan C):** About $45/month, which includes a limited number of builds/pushes; because each build costs against your quota, it's best to batch iterative changes and only push once work is more complete rather than building on every change.

**Q (Morgan, to Scott, re: iOS deployment):** Do I need to develop this properly in Swift/Xcode, or is there an easier path?
**A (Ryan C, with input from Paul Miller):** You can do it "the proper way" with Swift/Xcode, or use Expo to build once and deploy to both iOS and Android — sufficient if the app offloads most logic to a backend server; Expo supports GPS, camera, and most native features, with the main caveat being deeper native-only functionality (e.g., certain platform-specific AI features).

## tools

- **CC BlackBox** — Scott Rippey's Electron-based Claude Code IDE/agent harness for Mac, with cross-machine sync via Bonjour and usage/cost reporting.
- **Model Radar** — Scott's hybrid AI/rule-based scanner that tracks which AI models are active/deprecated across local project folders.
- **Doppler** — mentioned as Scott's existing tool for managing API keys, insufficient alone for tracking model usage.
- **CMUX** — Ty Wells' base for a custom agent harness with browser control for testing.
- **Cloud Code (Claude Code) / Codex / GitHub Copilot CLI** — core coding agent CLIs discussed throughout, including plugin work to bring Codex-style review to Copilot CLI at Patrick's workplace.
- **pi.dev** — open-source, model-agnostic agent harness Patrick is customizing into a review-only harness.
- **Fable** — Daniel's/Patrick's AI "thinking partner" used for requirements discussions, prompt condensation, and even publishing books to Kindle.
- **Hermes** — Patrick's custom agent that manages his entire dev environment and prepares weekly Fable prompts.
- **Superpower** — an agentic skill framework offering more guided/autonomous but less flexible dev workflows, discussed vs. Pocock's skills.
- **Matt Pocock skills** (`/teach`, `/grill-me`/"Grill with Docs," "Wayfinder," `/wait-what`, "unslop") — modular skills for training, requirements grilling, code review, and cleaning up AI ("Opus") response slop.
- **CC-StatusLine** — Patrick Chouinard's open-source Claude Code status line plugin tracking session usage, time remaining, and git branch.
- **Convex** — sync database (WebSockets built-in) Morgan is migrating an app to from Supabase.
- **Supabase** — prior backend being migrated away from by Morgan.
- **Expo** — cross-platform (iOS/Android) app framework recommended by Ryan C and Paul Miller for mobile deployment without full native development.
- **SQLite** — used for offline app data storage in Expo-based apps.
- **SumSub** — third-party biometric/ID verification service Paul Miller uses for driver authentication.
- **Clerk** — base-level user authentication service mentioned by Paul Miller, escalated to SumSub when needed.
- **LanceDB** — vector DB used by both Daniel Zivkovic and Paul Miller for RAG/grounding work.
- **Deep Wiki + NotebookLM** — Daniel's prior workflow for scraping repos and generating summary podcasts, now superseded by `/teach`.
- **Dark Factory** — Daniel Zivkovic's personal wrapper around compound engineering for running autonomous overnight ticket batches.
- **Flutter** — mentioned by Daniel as an alternative cross-platform framework a friend uses.
- **Avery.tv's compound engineering framework** — cited for its junior+senior+AI hiring model.

## links

- https://www.youtube.com/watch?v=S_QdQ1G4GlU — video shared by Patrick Chouinard at session start.
- https://every.to/guides/compound-engineering — Daniel Zivkovic's reference for his AI-assisted SDLC approach ("compound engineering").
- https://github.com/scott-rippey/cc-blackbox-app — Scott Rippey's Mac IDE/agent harness repo, with full feature docs and user guide.
- https://github.com/scott-rippey/model-radar-app — Scott's Model Radar app repo for tracking AI model usage across local projects.
- https://www.youtube.com/watch?v=0oXOOlqVu5M — Theo (T3.gg) video on Matt Pocock's skills, cited as inspiration for Patrick's harness work.
- https://github.com/hopchouinard/CC-StatusLine — Patrick Chouinard's open-source Claude Code status line plugin.
- https://github.com/hopchouinard/patchoutech-plugins — Patrick's plugins repository.
- https://sumsub.com/pricing/ — biometric/ID verification pricing page shared by Paul Miller.
- https://github.com/awslabs/aidlc-workflows — AWS's AI-DLC workflow framework, shared by Elena in relation to her autonomous-AI-DLC question.
- https://therightrequirement.com/ — Prof. Joseph Eli Kasser's systems-thinking course site, recommended by Daniel to Varun.
- https://lnkd.in/p/gTQAAjrS — Daniel Zivkovic's published output-optimization methodology (Opus/Claude related).
- https://www.linkedin.com/in/magmainc/ — Daniel Zivkovic's LinkedIn, shared for networking outside the call.
- https://www.zalak-patel.com/ — example of a well-built developer portfolio site, shared by Ryan C.
- https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md — "unslop" skill Morgan recommended for cleaning up Opus/Claude responses.
- YouTube channel list shared by Patrick Chouinard as his daily follows: t3dotgg, mattpocockuk, indydevdan, NetworkChuck, BuildingwithReason, unsupervised-learning, AndrejKarpathy, NateBJones.

## decisions

- Scott Rippey to share the full walkthrough/blog content for "Power Your Process AI" in chat after the call.
- Scott Rippey to add browser-control integration to CC BlackBox as his next feature priority (inspired by Ty Wells' CMUX setup).
- Patrick Chouinard to continue building his pi.dev-based, review-only agent harness and his combined Superpower + Matt Pocock enterprise "Agentic SDLC" skill layer.
- Paul Miller to prepare and share a demo of his CRM AI-reporting work next week without exposing customer data.
- Paul Miller and Ryan C agreed to schedule a separate catch-up call to demo Ryan's Apple/Android emulator testing setup and discuss a potential UK/Omnicom business introduction.
- Varun Sharma to experiment with a prompt-injection/steganography trick in his résumé, but only when applying to large enterprises he's not seriously interested in, to test ATS screener behavior.
- Daniel Zivkovic recommended Varun Sharma pursue systems-thinking coursework from Professor Joseph Eli Kasser.