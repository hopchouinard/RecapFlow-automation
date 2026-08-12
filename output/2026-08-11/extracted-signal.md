## general

This session was a peer coaching call among AI builders/consultants, largely centered on the evolution of "assistant" agent architectures into "chief of staff" style multi-agent orchestration. Patrick Chouinard opened with a detailed walkthrough of his shift from a single Claude assistant to a two-tier system (Claude Cowork as "chief of staff" coordinating with Claude Code as "implementer" via a shared local Git repo/ledger), driven by the crunch of rolling out 2,000+ Claude licenses at his enterprise. Paul Miller, Ty Wells, and Rod Morrison independently confirmed they had converged on nearly identical patterns in their own work, discussing how to manage agent verbosity (especially with the new, chatty "Opus 5" model), timeline expectations, and how to surface only decision-worthy items rather than raw agent noise.

Other project updates included Morgan (mdcatc) evaluating a migration of his "Carpool" app from Supabase to Convex.dev for built-in real-time sync at multi-tenant scale (with detailed input from Bastian Venegas Arevalo on Convex/WorkOS integration and cost safeguards), and an automated multi-format book/podcast production pipeline for a client. Ty Wells demoed a family-history visualization tool built from WhatsApp group chat exports, plus a golf-swing coaching system using Garmin GPS data. Rod Morrison and Patrick discussed strategies for overcoming organizational resistance to AI-assisted coding (including a "swap projects" experiment) and how to measure real ROI from AI coding tools versus vanity metrics like token spend or PR count. Juan Torres discussed his AI photo-booth business, considerations around VC funding vs. distribution partnerships, and ADHD/productivity strategies were touched on with Ryan C, who also described his "Hermes" personal-assistant setup (built by "Scott") and an in-progress animated video project. Alex closed the call by recommending the Moonshots podcast and sharing that he'd closed a follow-on client payment.

## insights

- **Assistant model breaks down at scale**: Patrick Chouinard found that coordinating more Claude "assistant" agents eventually consumes more time than it saves ("the more fuel you put in, the more fuel you need to lift the fuel") — prompting a move to a "chief of staff" model where one agent (Claude Cowork) coordinates and delegates to an implementer agent (Claude Code) via a shared local ledger/repo.
- **Two independent agents talking to each other is the real unlock**: Patrick and Paul Miller both independently arrived at architectures where a "coordinator" agent and an "executor" agent communicate and write status back to each other without the human relaying messages — reducing the human to a pure decision-maker.
- **Only surface decisions, but keep some "wins" visible**: Ty Wells noted that showing only problems (not successes) to the human creates a demoralizing, imbalanced interface; a chief-of-staff agent should also highlight progress/wins, not just escalations.
- **Set explicit time expectations for agents**: Paul Miller (via lessons from "Bastian") stressed being decisive about time budgets for agent tasks, since tasks without deadlines can silently balloon from an hour into three or four hours, cascading delays across a project.
- **Opus 5 is notably verbose**: Multiple attendees (Patrick, Ty, Morgan, Rod) independently observed that Opus 5 produces long, sometimes confusing paragraphs; mitigations included Matt Pocock's "wait, what?" skill (which detects confusing output and asks for simplification) and custom natural-language/verbosity-reduction hooks.
- **Sarcastic/personality-driven system prompts reduce verbosity organically**: Patrick found that giving agents a sarcastic, "cheeky" personality naturally produces shorter, simpler word choices and more engaging output — he applies this uniformly across Claude Code, Codex, and his personal-assistant agents, with tone dialed down automatically for outside-facing communication.
- **Governance should live in skills/plugins, not policy documents**: At enterprise scale, Patrick's org concluded that governance (tech stack constraints, approved integrations, output formats) must be enforced via mandatory onboarding skills and managed settings, because users will otherwise ask Claude for things like raw Anthropic API keys or unsanctioned Supabase/Vercel access to "publish" artifacts.
- **Reframe AI-generated prototypes as "living specifications"**: Rather than calling clickable HTML outputs "prototypes" (which invites scope confusion), Patrick's team labels them "living specifications" — the HTML is generated with embedded structured comments that a downstream Claude Code session can parse into a real functional spec.
- **A head-to-head swap test defeats developer skepticism fast**: When one developer resisted agentic coding, Patrick's team swapped his project with a colleague's (same team, shared context) — the AI-aided developer tripled output, which quickly converted holdouts once they saw the result rather than accepting anecdote.
- **ROI shouldn't be measured by volume metrics**: Patrick and Bastian agreed that PR counts, token spend, or lines of code are easily gamed/misleading; real ROI has to be judged by delivered value/quality — Patrick cited a real case where a $2,000-token developer shipped 3 shallow solutions vs. an $800-token developer who shipped roughly half a year's worth of deliverables.
- **Team-member resistance can stem from fear of replacement**, not just stubbornness — Rod Morrison observed that data scientists who previously "owned the black box" may resist AI-built solutions partly because non-technical staff (former consultants) can now build competing prototypes themselves.
- **Personality-profile projects help manage stakeholder change**: Paul Miller built a per-team-member Claude project that reviews past emails/discussions to derive each person's motivational "hot buttons," which he used to tailor persuasion strategies during rollout.
- **Convex.dev's built-in reactive sync removes a lot of custom plumbing**: Bastian and Morgan noted Convex's subscribed-query model avoids manual socket/refresh logic needed with Supabase, and typed backend schemas in the same codebase give agents (Claude Code, Codex) full-stack type-safety context, making them easier to steer.
- **Convex billing risk is manageable via indexing**: Bastian advised that cost blowouts mostly come from unindexed queries — proper indexing keeps costs low even at scale (contrasted with Theo/T3Chat's much higher, transactional-chat-driven Convex bill).

## qa

**Q (Paul Miller): Why did you go with Convex instead of your existing Supabase setup?**
**A (Morgan/mdcatc):** Convex has native built-in sync — when one client updates data, all other subscribed clients see it instantly with no manual refresh, socket handling, or subscription management, which is exactly what a multi-tenant carpool app with real-time classroom updates requires.

**Q (Paul Miller): Bastian, any advice for Morgan before he makes the Convex plunge, especially around scary billing stories?**
**A (Bastian Venegas Arevalo):** As long as you're not making excessive raw database calls and instead index your queries, cost stays very low; Convex integrates well with WorkOS for multi-tenant auth/social logins, and even at scale the worst case is needing to upgrade your plan — billing is generally very affordable (the highest known Convex bill, Theo's T3Chat, is ~$6-7k/month but that's driven by hundreds of thousands of transactional real-time chat users).

**Q (Rod Morrison): How do you measure ROI/productivity gains from AI coding tools at an enterprise level (e.g., parsing GitHub activity)?**
**A (Patrick Chouinard):** Counting volume metrics (tokens consumed, PRs, lines of code) is dangerous because those can be trivially gamed — Claude can generate a "truckload of useless things" quickly. Real ROI must be judged on end deliverable quality/value ("solution per token"), citing an example where a $2,000-token developer delivered only 3 basic solutions while an $800-token developer delivered roughly half a year's worth of value.

**Q (Ty Wells): In your developer swap test, did the two developers have zero context on each other's projects, or just different deliverables?**
**A (Patrick Chouinard):** They weren't starting from zero context — both were on the same team already familiar with each other's projects; only the assigned deliverable was swapped, so it was a fair test isolating tool usage from prior project knowledge.

**Q (Paul Miller): Does Claude's enterprise layer play nice in providing usage/license data back for tracking?**
**A (Patrick Chouinard):** Yes, the enterprise admin layer exposes an API mirroring everything in the admin console, though the compliance API (which can expose every user prompt) carries heavy legal/red-tape restrictions; the gap between Teams and Enterprise license control is huge.

**Q (Biggi Fraley, chat): So sounds like you'd recommend Honcho — do you like it?**
**A (Patrick Chouinard, chat):** Yes, loves it — has been running it for about 3 months on roughly $27 of usage, talking to it ~12 hours a day; it pre-analyzes memory before storing and re-injects only the specific context needed to answer a given question, rather than dumping the whole memory into context.

## tools

- **Claude Cowork** — used by Patrick (and Paul, Ty) as the "chief of staff" coordination layer sitting above Claude Code.
- **Claude Code** — the "implementer" agent that executes coding/JIRA work and reports back to the shared repo/ledger.
- **Claude Desktop / Claude AI (chat)** — one of three license tiers Patrick's org distributes and tracks via Entra ID groups.
- **Opus 5 (Claude model)** — flagged repeatedly as unusually verbose/chatty by Patrick, Ty, Morgan, and Rod.
- **Matt Pocock's Claude skills ("teach" skill, "wait, what?" skill)** — referenced for training/onboarding and for catching/simplifying confusing verbose output.
- **Convex.dev** — reactive backend-as-a-service being evaluated by Morgan to replace Supabase for the Carpool app; discussed extensively with Bastian.
- **WorkOS** — auth provider that integrates with Convex for multi-tenant social login (free up to ~1M users per Morgan's chat correction).
- **Supabase** — Morgan's current backend, being compared against Convex due to socket/connection scaling concerns.
- **Whisperflow (note taker)** — Ty Wells trialed this real-time meeting transcription tool live on the call.
- **Fathom** — notetaker used to record/summarize this meeting (per chat log); Bastian noted it fails often at speaker/turn detection.
- **Otter** — Paul Miller's usual transcription tool, noted as reliable for transcript but weaker on video.
- **Honcho.ai (Huncho AI)** — LLM memory-reasoning layer Patrick uses for his personal-assistant/chief-of-staff memory management.
- **Hermes** — Scott-built personal/business assistant system used by Ryan C and Patrick (in different configured profiles) for admin, calls, and scheduling.
- **Higgsfield CLI + 11 Labs (MCP'd together)** — Ryan C's video generation stack for an animated video project.
- **Verif / VERIFF** — biometric ID/face-verification API Paul Miller is evaluating for a logistics client's driver-authentication problem.
- **Entra ID (Azure AD)** — used by Patrick's org to manage Claude license/group membership at enterprise scale.
- **GitHub / GitHub Copilot** — standardized code repository and secondary front-end AI coding tool in Patrick's org's dual-population environment.
- **Jira** — ticketing system Patrick's chief-of-staff agent writes fully-specified tickets into.
- **Streamlit** — legacy data-science front-end tooling Rod Morrison is replacing with Next.js UIs.
- **Next.js** — front-end framework Rod Morrison introduced to make data science tools business-user friendly.
- **T3 Chat** — referenced as the source of Morgan's original Convex recommendation and as Convex's highest-billing use case.
- **Codex (OpenAI) / codex-plugin-cc** — mentioned alongside Claude Code as part of the coding agent ecosystem; GitHub link shared in chat.
- **class2curb.com** — Morgan's carpool product, shared for feedback/testing.
- **data-terrain / Data Terrain Showcase** — Ty Wells' visualization tool used for both the family tree and testing Morgan's class2curb data.
- **Fable (Fable x 4.8)** — mentioned in chat by Ryan C as an alternative to Opus 5 that's been working well for him.

## links

- https://class2curb.com/ — Morgan's carpool pickup product, shared for referrals/testing.
- https://data-terrain-showcase.vercel.app/t/the-holding-pool-ws8r19 — Ty Wells' test run of Morgan's class2curb data through his terrain visualization tool.
- https://www.linkedin.com/posts/juan-torres-ai-engineering_i-made-a-game-its-called-ai-booth-activity... — Juan Torres' LinkedIn post about his AI Booth project.
- https://www.score.org/ — Adam's suggestion to Juan Torres for business/funding advice.
- https://github.com/openai/codex-plugin-cc — Codex plugin for Claude Code, shared by Patrick.
- https://www.convex.dev/ — Convex.dev homepage, shared by Patrick during the sync/backend discussion.
- https://www.honcho.dev/ — Honcho.ai memory-layer platform recommended by Patrick.
- https://ericscouler.com/projects/church-of-claude — Humorous link Patrick shared in response to being called "the messiah of Claude."
- https://www.diamandis.com/podcast — Peter Diamandis' Moonshots podcast, recommended by Alex/Paul.
- https://www.youtube.com/@MoonshotsClips — Moonshots podcast YouTube clips channel.
- https://www.youtube.com/@aiDotEngineer — AI Engineer YouTube channel referenced by Juan Torres.
- https://www.youtube.com/@alejandro_ao — Recommended by Bastian as a practical AI implementation channel (head of AI Engineer conference).
- https://www.youtube.com/@HealthyGamerGG — ADHD-focused psychiatrist/coaching channel recommended by Bastian to Juan Torres.
- https://youtu.be/Q6PTLG71NGc — Video link shared by Alex (context: Moonshots podcast episode).
- Juan Torres' additional LinkedIn posts (economics/finance/data science and agentic systems activity links) shared in chat as portfolio examples.

## decisions

- Morgan (mdcatc) to decide this week whether to rewrite the Carpool app's backend on Convex before onboarding more client schools, estimating a ~4-day rewrite.
- Morgan to reach out directly to Bastian with follow-up Convex/WorkOS implementation questions.
- Patrick Chouinard to build separate Claude style templates for the "chief of staff" (Cowork) and "implementer" (Claude Code) roles to reduce report verbosity.
- Juan Torres to prepare a pitch/application for the September funding round referenced by Brandon.
- Paul Miller to set up a direct meeting with Juan Torres to discuss funding/partnership strategy (message already sent during the call).
- Ryan C to onboard his 30 existing clients into his new Hermes-based personal/business assistant system.
- Ryan C and Patrick to compare notes offline on their respective Hermes/chief-of-staff configurations and multi-profile setups.
- Scott (via Ryan C) to demo his in-progress coding-tool replacement (Mac app) to the group once back from holiday.
- Juan Torres to consider Bastian's suggestion of structuring venue/event partnerships as revenue-share deals rather than seeking traditional equity investors.