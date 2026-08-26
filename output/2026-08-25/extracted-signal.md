## general

This session was a rotating show-and-tell among members of an AI/agentic-development coaching group, with each person walking through what they built or learned in the past week. Scott Rippey demoed two personal tools: "Power Your Process AI" and a Mac-native Electron app called CC Blackbox (an IDE/agent harness built around Claude Code) plus a companion "Model Radar" app that scans local project folders to track which AI models are active, deprecated, or retired across many client apps. Ty Wells described his CMUX-based setup for driving a browser during agent testing, managing multiple Claude/Codex subscriptions programmatically, and using "intent capsules" to run cold agent sessions from his phone (including from a golf course).

Patrick Chouinard discussed adapting the open-source Codex review plugin to run on GitHub Copilot CLI (since OpenAI tools are banned at his workplace), his in-progress "Pi" harness optimized purely for code/security review, and an enterprise-oriented Agentic SDLC combining Superpower with Matt Pocock-style skills (Grill with Docs, /teach) tailored for non-technical business analysts. He also shared his custom CC-StatusLine plugin for tracking Claude/Codex usage and git state. Daniel Zivkovic talked about "optometry-style" requirements elicitation, his Fable-based book-publishing/thinking-partner workflow, a "Dark Factory" wrapper around Nate B. Jones's compound engineering framework, and community/hiring philosophy. Morgan covered migrating an app from Supabase to Convex using Pocock's Wayfinder skill for code review, a client data-cleanup project, and questions about deploying to iOS, which Ryan C and Paul Miller answered in depth (Expo vs. native Swift, offline storage, biometric identity verification via SumSub). Later in the call, newer members Elena and Varun Sharma asked for guidance — Elena on fully autonomous AI-DLC frameworks and guardrails, and Varun on breaking into an AI/software engineering career — prompting a broader discussion on resumes, portfolios, and even prompt-injection tricks in CVs. Paul Miller closed with an update on AI-driven CRM reporting for his software company, aimed at competing with Salesforce.

## insights

- Scott Rippey: A local-first "Model Radar" tool can hybrid-scan project folders (excluding markdown/lockfiles/build output) plus call provider APIs to detect which AI models are actually active vs. deprecated/retired across many apps and clients.
- Scott Rippey: Machine-to-machine sync (via Bonjour, encrypted) can keep session/reporting databases consistent when developing from two different Macs.
- Ty Wells: Automating subscription switching (Claude/Codex) based on remaining usage percentage avoids manually babysitting quota and prevents work loss.
- Ty Wells: "Intent capsules" — self-contained context bundles — let a cold agent session pick up and execute a plan without needing prior conversation history, enabling mobile/remote continuation of work.
- Patrick Chouinard: When a company bans OpenAI/Codex, you can recreate the Codex review-plugin mechanics on top of GitHub Copilot CLI, satisfying security/governance while still giving developers access to frontier models.
- Patrick Chouinard: Building an agentic SDLC for an enterprise requires more hand-holding than single-developer frameworks (like Pocock's skills) provide, because business analysts don't share developers' technical assumptions.
- Patrick Chouinard: Fully autonomous AI-DLC is a misnomer — there must always be a human supplying intent; loops/goals-based automation only works when requirements are hard, testable facts rather than opinions.
- Patrick Chouinard: "Just-in-time training" (Pocock's /teach skill, pointed at any repo/doc) beats building static courses, which become obsolete before they're finished; it also supports active quizzing for retention.
- Patrick Chouinard: Good agent skills are short, composable, and can be invoked recursively/out of order (e.g., "teach" can teach you how to use "grill me") rather than forcing a strict serial workflow.
- Daniel Zivkovic: Requirements elicitation from non-technical stakeholders works better as an iterative "optometry" process (show a prototype, ask "this or that," refine) than asking them to specify requirements upfront.
- Daniel Zivkovic: Running multiple AI-generated ticket implementations in parallel causes conflicts; running them in sequence overnight avoids collisions while still producing a morning review queue ("Dark Factory").
- Daniel Zivkovic: The best hiring signal now is curiosity — pairing a junior and senior (both AI-augmented) so someone can keep the other honest, rather than hiring people who just echo AI output.
- Elena: Autonomous coding agents drift when given large/ambiguous tasks; they perform much better on very small, tightly defined tasks.
- Paul Miller: In an agentic-AI hiring market, companies expect junior candidates to already perform at an "intermediate" level — self-built apps and demonstrated initiative matter more than credentials.
- Ryan C: For CVs, the best approach is to write it yourself, have AI critique it, then rewrite the improvements in your own voice — this avoids the "AI slop" sameness that makes candidates blend together.
- Patrick Chouinard: AI can (and should) be used to re-target/optimize a CV per job description, but not to embellish it — fabrications are easy for AI reviewers (or human interviewers) to catch.
- Paul Miller: For cross-platform mobile apps, Expo is sufficient for most functionality (GPS, camera, biometrics) unless you need deep native-only integrations; build costs are per-push, so batch changes before building/pushing.
- Paul Miller: Running an Apple + Android emulator pair under Claude Code lets an agent iteratively test UI/UX before pushing costly builds to app stores.

## qa

**Q (Ryan C, in chat):** Did u guys discuss @skills?
**A (Paul Miller, in chat):** No.

**Q (Morgan):** For iOS deployment, should he do it "the proper way" with Swift/Xcode, or is there an easier path?
**A (Ryan C):** If the app is largely offloading logic to a server ("dumb" client), you can use Expo to build once for both iOS and Android; it handles Apple credentials and app-store submission, though it costs a monthly fee, whereas going fully native gives more control for deep native features.

**Q (Morgan):** What's the Expo subscription/build-cost model?
**A (Ryan C):** About $45/month for roughly 15 pushes, charged per build — so it's best to batch changes and build once you're done iterating rather than pushing on every change.

**Q (Aaron Ferrell, in chat):** Does Expo handle offline app storage?
**A (Ryan C / Paul Miller):** Yes — Ryan's capture app stores data locally when offline and syncs once back online; Paul confirmed SQLite (or a third-party option) is a good cross-platform starting point for offline storage.

**Q (Morgan):** Which stack is Paul using for biometric driver verification?
**A (Paul Miller):** SumSub — roughly $1 per full authentication, with lighter face-only re-verification for returning users; rated as the most polished of the three or four identity-verification tools he tested (Amazon's equivalent was described as "janky").

**Q (Elena):** Does anyone have good experience with guardrails, security, observability, and implementation blueprints for a fully autonomous AI development lifecycle?
**A (Patrick Chouinard):** "Fully autonomous" is a misnomer since human intent is always required; Matt Pocock's skills (grill-with-docs → spec → ticket → code) are powerful but require developer expertise, while Superpower is more guided/autonomous but less flexible — it's always a trade-off between autonomy and customization, and goal/loop-based automation only works when requirements are hard, testable facts rather than opinions.

**Q (Varun Sharma):** Beyond experience, what do recruiters/companies look for in a junior candidate transitioning into AI/software engineering?
**A (Paul Miller):** Companies now expect self-starters who've already built their own apps/solutions and operate at an intermediate level, not people expecting on-the-job ramp-up time.
**A (Daniel Zivkovic):** Curiosity is the key hiring trait — some companies pair a junior and senior (both AI-augmented) specifically so someone can challenge and keep the other honest rather than just echoing AI output; recommended studying Systems Thinking via Prof. Joseph Eli Kasser.
**A (Patrick Chouinard):** Build a public GitHub portfolio of projects, use AI to optimize (not embellish) your resume per job description, and consider a "humanizer" pass so AI-written text doesn't read as obviously AI-generated.

**Q (Patrick Chouinard):** Are you (Paul) still running three other Cloud/Claude accounts to keep tokens topped up?
**A (Paul Miller/Patrick Chouinard):** Patrick clarified he's actually down to one Claude account and one Codex account, spending about $100/month on each rather than running multiple accounts.

**Q (Daniel Zivkovic):** Is Ty using Mark Kashif's multiplexing/pooling code across multiple subscriptions?
**A (Ty Wells):** No — he programmatically switches plans himself and uses "intent capsules" (self-contained context bundles) so any new session starts cold but with full context, rather than using Mark's specific utility.

## tools

- **Power Your Process AI** – Scott Rippey's personal app project, pushed to Vercel/GitHub with automated build notifications.
- **CC Blackbox** – Scott's Electron-based Mac IDE/agent harness built on Claude Code, tracks usage/cost per session and customer.
- **Model Radar** – Scott's app that scans local dev folders (hybrid AI + non-AI scan) to flag deprecated/retired AI models in use.
- **CMUX** – Ty Wells' agent harness derivative that lets him drive a browser for testing and access sessions remotely from his phone.
- **Doppler** – Used by Scott for API key management across projects.
- **Claude Code / Codex CLI** – Core coding agents discussed throughout; usage tracked via status lines and subscription switching.
- **CC-StatusLine** – Patrick Chouinard's open-source Claude Code status line plugin showing usage, time remaining, git branch.
- **GitHub Copilot CLI** – Used by Patrick to rebuild Codex-plugin review functionality where OpenAI tools are banned at work.
- **Pi.dev** – Open-source, model-agnostic agent harness Patrick is customizing into a review-only harness.
- **Superpower / Matt Pocock skills (Grill with Docs, /teach, Wayfinder, unslop, /wait-what)** – Skill frameworks referenced repeatedly for brainstorming, code review, and just-in-time training.
- **Fable** – AI "thinking partner" used by Daniel and Patrick for requirements discussion, weekly task planning (via Hermes), and book publishing.
- **Hermes** – Patrick's custom agent managing his entire dev environment across machines, running on his Codex subscription.
- **Convex** – Sync database Morgan is migrating an app to from Supabase, handling WebSockets/client sync automatically.
- **Supabase** – Previous backend being migrated away from in Morgan's Carpool App project.
- **Expo** – Cross-platform (iOS/Android) app framework recommended by Ryan C and Paul Miller for mobile deployment.
- **SQLite** – Recommended for offline app storage within Expo-built apps.
- **SumSub** – Biometric/ID verification service used by Paul Miller for driver identity checks.
- **LanceDB** – Vector DB used by Daniel and referenced by Paul for grounding/RAG work.
- **Deep Wiki / NotebookLM** – Daniel's earlier workflow for turning repos into learning podcasts (superseded by /teach skill).
- **Compound Engineering framework (every.to)** – Framework Daniel recommends as an enterprise-ready alternative to piecing together other skill frameworks.
- **Dark Factory** – Daniel's personal wrapper automating overnight compound-engineering ticket runs.
- **Flutter** – Alternative cross-platform mobile framework mentioned by Daniel (used by a friend).
- **Google ADK** – Framework Varun Sharma used to build and deploy personal agents on Google Cloud.
- **AWS AI-DLC workflows** – Framework Elena referenced for guidance on autonomous AI development lifecycle.

## links

- https://www.youtube.com/watch?v=S_QdQ1G4GlU — Video shared by Patrick Chouinard at session start.
- https://every.to/guides/compound-engineering — Daniel Zivkovic's referenced AI-assisted SDLC framework.
- https://lnkd.in/p/gTQAAjrS — Daniel Zivkovic's published output-optimization methodology (Opus topic).
- https://github.com/scott-rippey/cc-blackbox-app — Scott Rippey's IDE/agent harness for Mac.
- https://github.com/scott-rippey/model-radar-app — Scott Rippey's model-tracking tool.
- https://github.com/hopchouinard/CC-StatusLine — Patrick Chouinard's Claude Code status line plugin.
- https://github.com/hopchouinard/patchoutech-plugins — Patrick Chouinard's plugin repository.
- https://www.youtube.com/watch?v=0oXOOlqVu5M — Theo (T3) video discussing Matt Pocock's skills, cited as Patrick's inspiration.
- https://sumsub.com/pricing/ — Biometric identity verification pricing, shared by Paul Miller.
- https://github.com/awslabs/aidlc-workflows — AWS AI-DLC workflow reference shared by Elena.
- https://therightrequirement.com/ — Prof. Joseph Eli Kasser's Systems Thinking courses, recommended by Daniel Zivkovic.
- https://www.youtube.com/@t3dotgg, @mattpocockuk, @indydevdan, @NetworkChuck, @BuildingwithReason, @unsupervised-learning, @AndrejKarpathy, @NateBJones — Patrick Chouinard's list of daily-followed YouTube channels.
- https://www.zalak-patel.com/ — Example portfolio website shared by Ryan C.
- https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md — "unslop" skill Morgan recommends for cleaning up Opus responses.
- https://www.linkedin.com/in/magmainc/ — Daniel Zivkovic's LinkedIn, shared for outside-group networking.

## decisions

- Scott Rippey to post the Power Your Process AI walkthrough video/link in chat for interested members.
- Scott Rippey to add browser-control integration to CC Blackbox as his next development priority.
- Patrick Chouinard to continue building his Pi-based, review-only agentic harness and eventually refactor it for client implementation.
- Patrick Chouinard to look into the "compound engineering" framework (every.to) that Daniel recommended.
- Paul Miller to prepare a demo next week of his AI-driven CRM reporting (without exposing customer core data).
- Ryan C to email Paul Miller to schedule a time-zone-friendly catch-up/demo on Expo emulator testing and the Omnicom/Salesforce opportunity.
- Varun Sharma to test a prompt-injection trick in his résumé, but only when applying to enterprise jobs he's not genuinely interested in.
- Daniel Zivkovic to look up Mark Kashif's subscription-multiplexing utility/proxy for API-key services.