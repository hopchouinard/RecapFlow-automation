=== SESSION ===
date: Not stated in transcript (weekly community/mastermind call, referenced as "Tuesday")
duration_estimate: ~2 hours 58 minutes (00:01:22–02:58:49)
main_themes: AI coding agents (Claude Code, Codex, cloud infrastructure), startup sales strategy and ICP pivoting, AI-generated media (video/image) for real estate and events, autonomous support/dev-ops agent loops, security review tooling for AI-generated code, personal productivity gadgets (AI glasses), local vs. frontier LLMs, go-to-market and monetization brainstorming for member side projects.

=== UNRESOLVED SPEAKERS ===
(listed here because no SPEAKER_ALIASES data was returned by the alias lookup; all raw speaker labels below were passed through unchanged)
- Andrew Nanton
- Ty Wells
- Patrick Chouinard
- Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
- mdcatc (self-identified in transcript as "Morgan")
- Brandon Hancock
- Juan Torres
- Alireza Mounesisohi
- Ryan - One Stop Creative Agency

---

<!--SEGMENT
topic: Meeting Opening and Attendance
speakers: Andrew Nanton, Ty Wells, Patrick Chouinard, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, mdcatc, Brandon Hancock
keywords: community call, roll call, Hermes install, attendance, small talk
summary: Informal opening of a recurring community/mastermind call as members join, including brief mentions of a Hermes installation project and confirmation that "Brandon" (referred to earlier as "Mr. Brandon") would be joining. Establishes call participants before substantive topics begin.
-->

[00:01:22] Andrew Nanton: How's it going?
[00:01:23–01:25] Ty Wells / Andrew Nanton: Casual greetings exchanged.
[00:01:30] Patrick Chouinard: <Q>We're supposed to have the visit of Mr. Brandon tonight.</Q>
[00:01:37] Patrick Chouinard: Hopefully there's going to be a little bit more people.
[00:01:43] Ty Wells: They're just lurking in the shadows.
[00:01:53–02:36] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com joins and explains he almost missed the call because he'd been heads-down all day working with Patrick on a **Hermes** [tool:Hermes] install for another member. ▶ Scott plans to share the setup repo later in the call: "I got a good repo that uses **Claude Code** [tool:Claude Code] to walk people through an entire setup," describing it as much simpler than a prior system he calls "Ironclaw" while still being locked down securely.
[00:02:43–02:56] Patrick Chouinard confirms he uses the tool "every day" but is being cautious since he's actively developing on it live in a production context.
[00:03:06–03:33] Patrick Chouinard: <Q>Ty, were you able to try the training generator?</Q> Ty Wells: <A>I did something with it, though I'll have to check with my Hermes to remember what exactly — I'll look and get back to you.</A>
[00:04:12–04:52] mdcatc joins, identified in-call as "Morgan," and notes he hasn't configured his meeting setup since switching to Ubuntu.
[00:05:00–05:18] Patrick Chouinard checks in with "the man himself" as Brandon Hancock joins the call.

---

<!--SEGMENT
topic: AI Smart Glasses Demo
speakers: Brandon Hancock, mdcatc
keywords: smart glasses, AI wearables, real-time transcription, Tesla, Claude Code sessions, hands-free workflow, prescription AR
summary: Brandon Hancock demos a pair of prescription smart glasses with a built-in lens/display that provides real-time conversation transcription and cheat-sheet style answers during calls, plus a ring controller for double-click navigation. He describes using the ring to switch between parallel Claude Code coding sessions from his home computer while riding in a self-driving Tesla.
-->

[00:05:18–05:38] Brandon Hancock opens the call, joking about running upstairs for fluids, then transitions into gadget updates before business updates.
[00:06:00–06:33] Brandon Hancock: "Patrick, a while ago, I was telling you about these glasses. Dude, I pulled the trigger." He shares his screen to show the glasses in action. mdcatc: <Q>So those are the prescription ones?</Q> Brandon Hancock: <A>Yeah, they're prescription — if I take these off, I'm blind.</A>
[00:06:45–07:22] Brandon Hancock explains the core feature: "they literally have a built-in lens in the top," and in real time it "transcribe[s] and give[s] you tips on what's being said" during customer or investor conversations — essentially popping up a "cheat code" explanation when unfamiliar terms come up, and even suggesting what the other party might want to know. ▶ He notes it's "not personalized to you yet, which is like the only thing I don't like," but expects that to improve.
[00:07:28–08:02] Brandon Hancock describes a ring controller that lets him double-click to bring up a mini-map overlay or, more notably, to jump between multiple parallel **Claude Code** [tool:Claude Code] sessions running on his home computer while riding in his self-driving **Tesla** [tool:Tesla]: "I'm just sitting there anyway... I double click, and then I can work with all of my different cloud code sessions in parallel." He jokes about turning off recorders given the driving-while-multitasking angle, then clarifies the Tesla is self-driving.
[00:08:05–08:15] Brandon Hancock: ▶ "10 out of 10 would recommend for all you glasses folks out there. It is genuinely unreal what's possible nowadays."

---

<!--SEGMENT
topic: EMSO Sales Strategy — Whales, Tunas, Minnows
speakers: Brandon Hancock
keywords: EMSO, ICP, ideal customer profile, whales tunas minnows, fire departments, ambulance companies, outreach, Instantly, Loom, sales pipeline, cash runway
summary: Brandon Hancock gives a business update on his startup EMSO, which helps fire departments and ambulance companies write documentation to increase insurance reimbursement. He explains the company's cash-runway pressure and introduces a customer-segmentation framework (learned at Crew AI) of "whales," "tunas," and "minnows" to explain a strategic pivot in sales focus.
-->

[00:08:18–08:41] Brandon Hancock reintroduces EMSO: "we help fire departments, ambulance companies... do their narratives and increase their reimbursement rate."
[00:08:43–09:21] Brandon Hancock explains the company has completed core product features and is now in an intense outreach phase to avoid running out of money: "selling is still 99% usually the problem... it's stressful... it's like you have to sell, or else the company dies." ▶ He acknowledges the pipeline is uncertain and they are "trying to figure it out in real time."
[00:09:37–09:53] Brandon Hancock mentions using **Loom** [tool:Loom] for outreach videos and **Instantly** [tool:Instantly] for email warm-up/outreach automation, offering to demo both later.
[00:09:53–10:22] Brandon Hancock introduces the segmentation framework learned from working at **Crew AI** [tool:Crew AI]: "whales," "tunas," and "minnows." A whale is "a behemoth of an agency... contract could be worth hundreds of thousands of dollars," but takes "a year and a half for anything to happen." A minnow is a small agency worth a couple thousand dollars — low individual value but fine in aggregate.
[00:10:25–11:13] Brandon Hancock: ▶ Tunas are "midsize ones... worth a good amount of money, 20 to $40,000" and "fast enough to make decisions... in months" rather than years. He explains EMSO had been treating every prospect like a whale, causing everything to move slowly, and the company is now "in real time pivoting our entire organization" to focus sales effort on tunas while letting Instantly handle minnows automatically — a deliberate strategy to avoid running out of cash within "the next five, six months."
[00:11:17] Brandon Hancock hands off to Juan Torres for questions, transitioning into the next segment.

---

<!--SEGMENT
topic: ICP Pivot — Political Strategy for Fire Departments
speakers: Brandon Hancock, Juan Torres
keywords: ICP pivot, fire chief, EMS chief, city council, board of supervisors, private ambulance companies, union organizing, sales collateral, PowerPoint pitch deck
summary: Juan Torres questions Brandon Hancock about why EMSO is pivoting its ideal customer profile from fire departments to private ambulance companies, prompting a detailed explanation of misaligned incentives in government fire agencies versus private companies. The discussion extends into strategies for reaching city councils and boards of supervisors as decision-makers, drawing analogies to union political-campaign tactics.
-->

[00:11:25–11:59] Juan Torres: <Q>Are you also talking about pivoting because the friction and duration of the sales cycle is quicker on the private-company side?</Q>
[00:12:01–13:36] Brandon Hancock: <A>Yeah, a few things at the same time.</A> He explains the core problem is misaligned incentive: fire departments cost cities "hundreds of thousands or millions of dollars per city" because firefighters are forced to write documentation, and if done incorrectly "the insurance keeps the money" — meaning taxpayers subsidize the shortfall. ▶ "There is zero incentive as a fire department to make a few million dollars or lose a few million dollars. They get paid no matter what." By contrast, private ambulance companies "feel the burn... they need to make money to survive," making them faster, more motivated buyers. He notes this feedback loop with paying customers also improves the product faster.
[00:13:49–14:35] Juan Torres draws a comparison to mdcatc's ("Morgan's") funeral-industry product and asks: <Q>Have you considered engaging boards of supervisors/city councils directly, since they're often the actual decision-makers over department heads?</Q>
[00:14:35–16:13] Brandon Hancock: <A>Currently the sales motion runs "hand-to-hand combat" through his co-founder's network (a fire chief), moving from medic → EMS chief → fire chief → city council.</A> He shares a one-page pitch deck used identically for both fire departments and private ambulance companies — covering three core benefits, a product demo, case studies from other agencies, and projected revenue impact — designed so an EMS/fire chief can hand it directly to city council as "internal champions." ▶ "We're providing them the material that they can then turn around to become internal champions to pitch up and down the chain."
[00:16:13–17:20] Juan Torres suggests a two-front strategy: engage both department heads and city council/board of supervisors simultaneously, since councils often appoint department heads and may have more leverage. Brandon Hancock responds positively: "That is an actually super interesting point... I really like that," noting EMSO has worked top-down from the state level and bottom-up from medics, but hasn't yet directly targeted city councilmembers.
[00:17:21–17:51] Juan Torres adds context from his own experience working with labor unions, where political campaigns mobilized workers and community activists to pressure city councils into ratifying contracts — suggesting a similar mobilization tactic could pressure department heads.
[00:17:57–18:12] Brandon Hancock: "You have given me so many ideas... I need to dig into that," specifically flagging interest in exploring grant-funding processes mentioned by another participant ("Andrew").

---

<!--SEGMENT
topic: Avatar Saturation Debate and Pivot Justification
speakers: Brandon Hancock
keywords: ideal customer profile, avatar saturation, Alex Hormozi, market saturation, burn rate, pivot urgency, sales velocity
summary: Brandon Hancock addresses a written point from a participant ("Biggi") arguing that changing customer avatars is generally unwise before fully saturating the existing market — a principle attributed to Alex Hormozi. He explains why EMSO's pivot to a new avatar is a necessary exception due to runway constraints rather than a rejection of the general principle.
-->

[00:18:12–18:36] Brandon Hancock reads out a point from participant "Biggi": "The current avatar has not been fully saturated," and references the related quote from Alex Hormozi (transcribed as "Alex Ramosi"): <Q>changing avatars is genuinely usually not the best idea if the market isn't fully saturated — why change?</Q>
[00:18:48–19:26] Brandon Hancock: <A>"The only gotcha on that approach, for us, is time." Even if EMSO reached every fire chief in America tomorrow, sales cycles mean "we probably wouldn't see a change for eight months, maybe seven." Since the company's burn rate can't tolerate that timeline, they're forced to pivot the avatar even though it's "the exact same offer... same software... same tools... same service" — just funded differently (state vs. private agency).</A>
[00:19:44–19:54] Brandon Hancock reaffirms agreement with the underlying principle in normal circumstances: ▶ "Under normal circumstances, that is... more of the existing thing at the existing avatar until you're capped" is correct, but the existing avatar's sales velocity is "so slow" that it's "forcing our hand to pivot."
[00:20:00–20:25] Brandon Hancock closes the business update, thanking Patrick Chouinard for holding down prior calls and passing the floor to him.

---

<!--SEGMENT
topic: Testing Claude Security Plugin
speakers: Patrick Chouinard, Brandon Hancock, Ty Wells
keywords: Claude Security, Anthropic marketplace plugin, token consumption, Opus 4.5, sub-agents, code audit, custom prompts
summary: Patrick Chouinard reports testing a new Anthropic-made plugin called "Claude Security" that audits repositories for vulnerabilities, finding it extremely token-expensive relative to the value of findings it surfaced. He concludes his own custom prompts achieve comparable results far more cheaply, while praising the newly released Opus model powering it.
-->

[00:20:28–20:38] Patrick Chouinard: this week was spent testing a new **Claude Code** feature called **Claude Security** [tool:Claude Security], calling it "interesting" but "a token sponge... insane to test."
[00:20:45–21:00] Brandon Hancock: <Q>What is it?</Q> Patrick Chouinard: <A>Claude Security is a new plugin that Anthropic created as part of the Claude default marketplace; it scans your project.</A>
[00:21:06–21:30] Patrick Chouinard notes it does something similar to a tool Ty Wells demoed weeks earlier but consumes vastly more tokens: "In order to audit a single repository, I had to burn through like [a] five hour limit on a 5x plan." ▶ Despite the interesting concept, he says he'll continue using his own tools since the token cost isn't justified by the results.
[00:21:52–22:01] Ty Wells jokes the tool likely ships with "verify extra usage enabled," implying it's designed to drive up billable usage; Brandon Hancock agrees: "I'm sure you can pay us more money. That's crazy."
[00:22:07–22:35] Patrick Chouinard: <Q>Did it find anything of curiosity?</Q> <A>Yeah, it found something, but honestly, if it wouldn't have found those, I would have survived — it was not project-changing.</A> ▶ He estimates he can tweak his own prompts to achieve "95% for 5% of the cost."
[00:22:37–23:22] Brandon Hancock asks how large the audited repo was, surprised at the token burn; Patrick clarifies it was actually a small project — his own "training generator" skill — and that the plugin spun up numerous sub-agents in "Ultra Mode," running on **Opus 4.5** [tool:Claude Opus 4.5] (referred to as "Opus 5" in conversation). Patrick calls Opus 4.5 "a big fan, by the way — big improvement over 4.8" (likely referring to the prior model version).

---

<!--SEGMENT
topic: Enterprise Claude Rollout and Budget Management
speakers: Patrick Chouinard, Brandon Hancock
keywords: enterprise rollout, Claude Code, Claude Desktop, token budget, slash insights, ROI, pilot to production, fall launch
summary: Patrick Chouinard describes his organization's transition from a Claude pilot program (250 supported users) to full enterprise production (2,500 users) by fall, explaining how usage-based budget increases were managed during the pilot and citing concrete ROI evidence — a single engineer completing a year-plus of engineering work in three months.
-->

[00:23:28–23:57] Patrick Chouinard shares that his organization (kept intentionally vague for confidentiality) is "pivoting from pilot to full production," deploying **Claude** [tool:Claude] to over 2,500 people, up from 250 currently supported.
[00:23:57–24:23] Brandon Hancock: <Q>For a real-world organization at scale, how are agencies thinking about giving developers an "unlimited" AI budget without it becoming reckless "token maxing"?</Q>
[00:24:23–25:15] Patrick Chouinard: <A>During the pilot they set an arbitrary starting budget, then increased individual token allowances weekly as users reported topping out and still needing more, until reaching a stable point where only about 5% of users still request increases.</A> ▶ That stable threshold becomes the basis for enterprise-tier budgeting, since going over that point typically requires real justification.
[00:25:17–25:34] Patrick Chouinard notes the rollout means supporting roughly 2,250 additional users with a support team of only four people.
[00:25:39–26:17] Brandon Hancock asks whether engineers actually saw a measurable productivity bump, referencing the broader industry debate (citing Jason Calacanis's optimism vs. "the Chamaths" skepticism about AI ROI).
[00:26:17–27:09] Patrick Chouinard: <A>For heavy Claude Code users specifically, the team collected usage data via the **Slash Insights** [tool:Claude /insights] command and a custom-built equivalent skill for chat/co-work, tracking model choice, multi-session usage, etc. The heaviest users show concrete ROI: "we've done the engineering work that would have required a team of three a year and we've done it with one guy in three months."</A>
[00:27:35–27:51] Brandon Hancock confirms the enterprise rollout timeline is "fall," expressing excitement about the scale of impact.

---

<!--SEGMENT
topic: Self-Improving Support Knowledge Base
speakers: Patrick Chouinard, Brandon Hancock, Juan Torres
keywords: knowledge base, Co-Work, level-one support automation, ServiceNow, RAG connector, feedback loop, skill compilation
summary: Patrick Chouinard explains how he built a self-improving internal support system by logging every real user question into Claude's Co-Work tool to generate a training knowledge base, which now powers a self-service support skill for end users and a parallel skill for support staff that continuously feeds validated answers back into the knowledge base.
-->

[00:27:47–28:28] Patrick Chouinard describes his process: throughout the pilot he copied every question received via Teams, email, or discussion into **Co-Work** [tool:Claude Co-Work], had it generate answers, and documented them — building "a solid knowledge base." He then had Claude "compile a support skill that will work for the support staff as well as the end user."
[00:28:28–29:18] Patrick Chouinard explains the mechanism: only knowledge-base entries that are "signed off on" and confirmed stable are pushed to the end-user-facing skill, allowing users to self-serve level-one support. Support staff use a parallel version tied to Co-Work, where every resolved issue feeds back into the knowledge base until it stabilizes and graduates to the user-facing skill. ▶ "It's a feedback loop that will increase the efficiency of the support platform."
[00:29:26–30:11] Brandon Hancock asks what model or infrastructure powers this under the hood — self-hosted, open-source, or a major vendor. Patrick clarifies: <A>"That's done through the flawed [Claude] desktop application... we just created a skill, gave it to Claude, so people can ask Claude if they have questions about Claude."</A> Brandon calls it "inception" and "very smart."
[00:30:28–31:25] Juan Torres: <Q>Do you think a knowledge graph would enhance this Q&A system?</Q> Patrick Chouinard: <A>Not really — the goal isn't knowledge search; it's supplementing Claude's own self-knowledge with organization-specific specifics not known to Anthropic (e.g., who approves a given connector). Latency is being kept minimal since if an answer doesn't return within a second, users will just call someone instead.</A>
[00:31:38–32:44] Juan Torres proposes a controlled experiment comparing empty context files vs. a knowledge graph for a more technical team. Patrick responds that the next planned step is direct integration with **ServiceNow** [tool:ServiceNow] as the source of knowledge/ticketing — described as "a form of RAG" — though this isn't yet in production.

---

<!--SEGMENT
topic: Training Generator and Recursive Skill Design
speakers: Patrick Chouinard, Brandon Hancock
keywords: training generator, self-generating skill, progress tracking, CICD, recursion, superpowers spec/plan artifacts
summary: Patrick Chouinard describes a "training generator" skill that produces a self-contained training program from a project's spec and plan artifacts, tracks user progress in a JSON file, and can even be run as a CI/CD step. Brandon Hancock praises the recursive design as a major unlock for standardizing engineering onboarding at scale.
-->

[00:32:56–33:39] Patrick Chouinard elaborates on his favorite project this week: the "training generator... the ability to generate training as a CI/CD step." It creates a skill that itself delivers the training, and tracks the user's position in a `progress.json` file, allowing users to go on tangents and later say "let's resume" to pick up exactly where they left off.
[00:33:35–35:56] Brandon Hancock draws an analogy to first learning recursion: "it calls itself?... that's like that unlock." He praises the design as maximally efficient — "not too much engineering, not too little" — and frames it as a high-leverage skill: enabling hundreds or thousands of developers to work better via a standardized training strategy. ▶ Brandon Hancock: "It's crazy how much AI can help standardize every core operation of a business... it's just up to us to find items like you just did and standardize it."
[00:36:13–36:23] Patrick Chouinard jokes that "wanting to have a weekend once in a while is an incentive to do some creative engineering," attributing his efficient system design to time pressure.

---

<!--SEGMENT
topic: Agent Task Platform Introduction
speakers: Alireza Mounesisohi, Brandon Hancock
keywords: Agent Task, agent-task.com, long polling, task orchestration, MCP, Claude Code sessions, source of truth, multi-agent projects
summary: New participant Alireza Mounesisohi introduces his side project "Agent Task," a task-management platform where users can launch and track Claude Code sessions across machines via a long-polling system, aiming to serve as a persistent "source of truth" for AI-assisted project work across multiple sessions and tools.
-->

[00:36:38–38:00] Alireza Mounesisohi introduces himself as a Los Angeles-based long-time viewer of Brandon Hancock's YouTube channel, and pitches his project **Agent Task** [tool:Agent Task] at **agent-task.com** [link:agent-task.com].
[00:38:00–39:00] Alireza Mounesisohi describes a new feature: running a long-polling listener on a local computer or server so users can launch Claude sessions/tasks remotely from any device, grouped and assigned to that listening machine.
[00:39:00–40:28] Alireza Mounesisohi explains the platform's "source of truth" value: it records which session and computer a task was launched from, so returning weeks later, Claude can read the task, subtasks, links, and prior progress and continue exactly where it left off — valuable for busy users managing many parallel AI sessions. It integrates via MCP plugins for **Claude**, **Cursor**, and **Windsurf** [tool:Claude][tool:Cursor][tool:Windsurf], with dedicated commands beyond basic task claiming.
[00:41:10–41:28] Alireza Mounesisohi mentions pending credit applications with **NVIDIA** and **GCP** [tool:NVIDIA][tool:GCP], the latter already approved.
[00:41:34–42:24] Brandon Hancock: <Q>Is this essentially a Kanban-style task board that orchestrates work across any coding harness underneath — an "agent orchestration on top of agent orchestrators"?</Q>
[00:42:27–44:14] Alireza Mounesisohi: <A>Currently the main use case is as a "source of truth" organized into "spaces" (e.g., personal, work, project-specific), each with its own tasks and access-controlled agents/people, connected via OAuth/MCP. A future release aims to add live monitoring of which agent is doing what across the platform.</A>
[00:44:16–45:00] Brandon Hancock praises the visual reimagining of AI-assisted work management compared to the flat sidebar lists in Claude Code/Codex, and asks what kind of help Alireza is seeking (growth strategy, partnerships, etc.).

---

<!--SEGMENT
topic: Agent Task Differentiation and Partnership Ideas
speakers: Alireza Mounesisohi, Brandon Hancock
keywords: differentiation, go-to-market, avatar/ICP clarity, influencer partnership, Ben Affleck AI acquisition, distribution
summary: Brandon Hancock pushes Alireza Mounesisohi to clarify Agent Task's target customer and concrete differentiation from using Claude or Codex directly, using the "money shot" demo concept. The conversation closes with a tangent on the value of influencer partnerships, referencing a high-profile Ben Affleck-linked AI acquisition by Netflix.
-->

[00:45:02–45:47] Alireza Mounesisohi asks if Brandon Hancock would be open to making a promotional video for Agent Task; Brandon clarifies he's paused all YouTube content creation until his startup (EMSO) stabilizes financially. ▶ Brandon Hancock: "If money was not an issue, I would just make YouTube content for the rest of my days."
[00:46:58–48:12] Brandon Hancock requests a concrete demo video showing real work being done on the platform, referencing advice from a past startup coach about needing to show "the money shot" — the clear "oh wow" moment. He presses for a specific customer avatar: <Q>Is this for solo developers with many passion projects, or software agencies running multiple client projects?</Q> ▶ "That would be super helpful for me to just understand... it also forces you to pick the customer and it helps you force to pick the outcome that you give them."
[00:48:30–50:00] Alireza Mounesisohi gives a concrete example: building a mobile app end-to-end (via Figma integration plus Claude Code) in about five hours using Agent Task as the coordination layer, and describes onboarding a new engineer by generating a precise task-skill so the engineer had no ambiguity about what to build.
[00:50:35–51:21] Brandon Hancock reiterates the need to clearly articulate what Agent Task unlocks that raw Claude/Codex cannot, framing this as essential for justifying pricing.
[00:51:50–52:15] Alireza Mounesisohi claims early users report roughly halved token usage since Agent Task consolidates multiple agents' work into one shared source of truth rather than re-planning across tools like Codex.
[00:52:19–52:53] Alireza Mounesisohi asks Brandon's opinion on the recently reported ~$580M Netflix acquisition of an AI company associated with Ben Affleck, and whether the same company minus the celebrity name could achieve similar value.
[00:52:56–54:00] Brandon Hancock: <A>Referencing advice previously shared by Dan Martell on a past community call, a strong partnership pairs a builder with a distribution-savvy figurehead: "product without distribution, worthless... a ton of distribution without a product, well, there's no way to monetize."</A> ▶ Brandon Hancock's advice to Alireza: find a distribution-strong partner, since a well-known face can unlock deals and valuation "directly proportional" to the partner's reach.

---

<!--SEGMENT
topic: Dev Tool Roundup — ADK, BAML, Herder, LlamaParse
speakers: Andrew Nanton
keywords: ADK, BAML, Herder, Tmux, LlamaParse, Docling, PDF parsing, Markdown conversion, dogfooding
summary: Andrew Nanton shares a rundown of tools he's been experimenting with while building an unnamed (not-yet-anonymized) product, including Google's ADK, the BAML DSL, a Tmux alternative called Herder for managing multiple agents, and LlamaParse as a faster replacement for Docling in PDF-to-Markdown conversion.
-->

[00:54:15–54:53] Andrew Nanton reports he hasn't yet anonymized his in-progress product enough to demo it publicly, but has been enjoying "dogfooding it" — using it himself to discover needed features organically. ▶ "That's the best way to build it."
[00:54:53–55:15] Andrew Nanton: has been enjoying **ADK** [tool:Google ADK] and pairing it with **BAML** [tool:BAML], noting BAML is "in a lot of flux right now" — worth investigating but not necessarily worth committing to yet.
[00:55:15–55:29] Andrew Nanton: ▶ recommends **Herder** [tool:Herder] ("H-E-R-D-R") as a replacement for **Tmux** [tool:Tmux] when running multiple agents in parallel, calling it "pretty slick."
[00:55:44–56:20] Andrew Nanton: switched from **Docling** [tool:Docling] to **LlamaParse** [tool:LlamaParse] (from the Llama Index team) for large-scale PDF conversion, citing Docling as "slow and fragile." ▶ "If anyone is trying to parse large numbers of PDFs, LlamaParse... has been super impressive... it outputs Markdown now very, very rapidly, so worth a look."

---

<!--SEGMENT
topic: Local Models and Superpowers Plugin Discussion
speakers: Andrew Nanton, Patrick Chouinard, Brandon Hancock
keywords: local LLMs, GPT-OSS-20B, Qwen 9B, superpowers plugin, Opus 4.5, background tasks, "poke holes" custom skill, Codex cross-model review
summary: Andrew Nanton asks the group for guidance on when local models are worth using versus frontier models like Opus, and whether the "superpowers" Claude plugin remains valuable after recent Opus updates. Patrick Chouinard and Brandon Hancock both affirm continued value, explaining use cases for local models in stable background tasks and describing supplemental techniques like a custom "poke holes" assumption-testing skill.
-->

[00:56:20–57:20] Andrew Nanton: <Q>Does anyone have recommendations for local models — when and where are they actually useful, since local models never seem to justify the time investment versus Opus 4.5?</Q> He also asks: <Q>Is "superpowers" still worth using, or has it become redundant given recent Claude updates, as some online commentary suggests?</Q>
[00:57:24–58:53] Patrick Chouinard: <A>Still using **Superpowers** [tool:Superpowers] daily; the small team maintaining it recently optimized it specifically for Opus 4.5 just days after people claimed it was obsolete. It's one of the only public repos in Anthropic's default Claude marketplace despite not being an Anthropic product. Its value lies in enforcing a structured workflow — brainstorming, spec, plan — whose artifacts Patrick's training generator depends on to build documentation and presentations.</A> ▶ "I'm more to the idea of adding more skills to that loop... then stop using it for sure [if you no longer need it]."
[00:58:53–00:59:58] Patrick Chouinard on local models: <A>"It's never going to replace Opus. That's not the goal of local [models]." They're valuable for background/24-7 tasks where you don't want to burn premium tokens, such as his "Community Brain" project running **GPT-OSS-20B** [tool:GPT-OSS-20B] for full independence, or pairing **Qwen 9B** [tool:Qwen 9B] behind Hermes background jobs needing light cognition. A key benefit is stability — local checkpoints don't silently change overnight the way hosted models do.</A>
[01:01:00–01:02:21] Brandon Hancock echoes Patrick's points on Superpowers, crediting Patrick for introducing him to it, then describes his own supplemental custom skill he calls "poke holes" — a follow-up step after brainstorming/planning that stress-tests assumptions before coding begins. ▶ "Always think... where did the problem actually happen? Was it the coding agent that messed up, or was the coding agent following instructions that were not set up for success in the first place?"
[01:02:49–01:03:51] Andrew Nanton mentions dispatching a "second opinion" review agent he calls "Fable," and Patrick Chouinard describes doing something similar but specifically routing reviews through the **Codex** [tool:OpenAI Codex] CLI/plugin to get a genuinely different model family's perspective rather than reusing the same Claude family (and thus the same potential cognitive biases). ▶ Patrick Chouinard: "I never, ever, ever use the same model that [wrote the] code to do the review."

---

<!--SEGMENT
topic: Cross-Model Code Review Workflow
speakers: Patrick Chouinard, Brandon Hancock, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: Codex plugin, slash codex review, cross-vendor review, Claude Code, Anthropic marketplace, official OpenAI plugin
summary: Brandon Hancock follows up on Patrick Chouinard's cross-model review technique, learning that Patrick uses an official OpenAI-built Codex plugin inside Claude Code (triggered via a "/codex review" slash command) to automatically feed the most recent artifact — spec, plan, or code — to Codex for review. Scott Rippey notes he prefers calling the Codex CLI directly rather than using the plugin.
-->

[01:03:57–01:04:24] Brandon Hancock: <Q>How exactly do you do that review handoff — do you manually prompt Claude to invoke a Codex sub-agent, or is it a fully separate step?</Q> Patrick Chouinard: <A>"I just do slash Codex review, enter" inside a Claude Code session — enabled by installing the official Codex plugin for Claude Code.</A>
[01:04:37–01:04:54] Patrick Chouinard clarifies the plugin automatically feeds Codex whichever artifact was most recently produced — spec, plan, or code — for review.
[01:05:00–01:05:20] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com notes he actually prefers calling the Codex CLI directly rather than through the plugin, previewing his upcoming deep-dive demo on his own security review system. Patrick Chouinard agrees the plugin approach is "more than enough" for simple spec/plan reviews, while direct CLI access is better when custom prompts or skills are needed.
[01:06:01–01:06:10] Brandon Hancock notes he currently does this kind of cross-model review "infrequently and manually" and flags it as a personal to-do to formalize, thanking Patrick for the "Codex plugin" pointer.

---

<!--SEGMENT
topic: Automated ERP Support Loop via WhatsApp Agent
speakers: Ty Wells, Brandon Hancock
keywords: ERP system, client portal, quoting system, WhatsApp automation, forward deployed engineer, cron job, Telegram approval, intent document, feedback hub
summary: Ty Wells demonstrates a custom ERP/quoting platform for his company that adds plain-language part descriptions and an embedded quote-chat feature, then describes a fully automated support pipeline where a junior "forward deployed engineer" reports bugs via WhatsApp to an AI agent that autonomously fixes and ships code, escalating only out-of-scope requests to Ty via Telegram.
-->

[01:07:20–01:08:35] Ty Wells demos his ERP/quoting system, explaining a recent addition: mapping cryptic part numbers to plain-language descriptions in the client portal so customers understand what they're being quoted, plus an embedded conversation chat scoped to each specific quote so customers can ask after-hours questions without waiting on staff.
[01:08:45–01:09:59] Ty Wells: if a customer request falls outside the quote's parameters, the system automatically emails the relevant salesperson a direct link into that quote's chat thread to respond — keeping all communication centralized in the platform.
[01:09:59–01:10:47] Ty Wells describes his broader automation loop: he employs a computer-science-major intern acting like a "forward deployed engineer" who visits employees, documents issues with screenshots/recordings, and submits them to a dedicated **WhatsApp** [tool:WhatsApp] channel monitored by an AI agent (not Ty himself).
[01:10:29–01:11:19] Ty Wells: <A>The agent picks up the request via a cron job, diagnoses the issue, kicks off a **Claude** session through his "feedback hub" to build a fix, and replies to the intern to test it. If a request falls outside Ty's predefined feature intent (documented in a markdown "intent" file), it's flagged and routed to Ty via **Telegram** [tool:Telegram] for a manual approval toggle before proceeding.</A> ▶ "I'm not involved in it at all... I'm golfing all the time now."
[01:11:25–01:12:39] Brandon Hancock: <Q>What happens if the intern requests something dangerous but seemingly innocent, like deleting data during an outage — does the classifier prevent accidental damage?</Q> Ty Wells: <A>Yes — safeguards exist within the spawned build session itself, and anything beyond a documented fix requires Ty's explicit approval via the intent document and Telegram gate.</A>
[01:12:39–01:13:49] Ty Wells describes automatic versioning: the app displays a version number and prompts users to refresh when updates ship, and confirms he's replicated the same WhatsApp-monitoring support-agent pattern for a second company, replacing **Zendesk** [tool:Zendesk] entirely — with an allow-list restricting who can trigger requests. ▶ Brandon Hancock calls it a real-world realization of the "four-hour work week" concept, but with an AI agent instead of a human VA.

---

<!--SEGMENT
topic: TTL.golf App and Marketplace Business Model
speakers: Ty Wells, Brandon Hancock
keywords: TTL.golf, tee time booking, Golf Now competitor, B2B marketplace, affiliate revenue, weather overlay, status line customization
summary: Ty Wells demos TTL.golf, a golf-round organizing app he built covering tee-time discovery, weather, settlement of bets/games, and player polling, positioned as a leaner alternative to Golf Now. Brandon Hancock advises pursuing a two-sided B2B marketplace model — free/low-cost for golfers, revenue via a small booking cut or SaaS fee from golf courses — and suggests a phased state-by-state rollout strategy.
-->

[01:15:34–01:16:00] Ty Wells demos **TTL.golf** [tool:TTL.golf][link:TTL.golf], an app for organizing golf rounds: real-time tee-time availability across roughly 15,000 courses, positioned against **Golf Now** [tool:Golf Now], which he criticizes for hidden clubhouse fees.
[01:16:37–01:17:31] Ty Wells: the platform also tracks recurring groups, member ledgers/"greenies," game formats like Wolf, weather per time slot, availability polling with cutoff times, and post-round bet settlement — essentially covering the entire round lifecycle, "the 19th hole" included.
[01:17:32–01:18:39] Brandon Hancock lays out two possible business models: ▶ (1) recurring subscription revenue, or (2) affiliate/booking-fee revenue as a middleman between golfers and courses, arguing the latter is easier to sell since golf courses' core pain point is filling tee times: "that's one option... I would much rather have 300 people paying me a dollar... than trying to get 20 hardcore people to pay me 15 [dollars]." He recommends a B2B-over-B2C bias generally, offering free player-facing features to grow volume before negotiating course partnerships backed by proven traffic data.
[01:19:57–01:20:02] Ty Wells confirms he's already headed down that path.
[01:20:20–01:21:02] Brandon Hancock suggests adding weather icons directly onto the existing time-slot table UI; Ty Wells clarifies weather data is already integrated per day.
[01:21:15–01:21:33] Ty Wells jokes about needing to "pair up with Tiger Woods" for distribution, echoing the earlier influencer-partnership discussion with Alireza.
[01:21:36–01:22:29] Brandon Hancock asks about Ty's visually distinctive **Claude Code** status line; Patrick Chouinard reveals (jokingly) it originated from his own status-line project, which he's actively improving that same night.

---

<!--SEGMENT
topic: Security Review System Architecture
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Brandon Hancock, Patrick Chouinard, Ryan - One Stop Creative Agency
keywords: git pre-push hook, secret redaction, multi-agent security review, Codex adversarial pass, Supabase, Next.js dashboard, false-positive learning loop, Anthropic security review prompt
summary: Scott Rippey demonstrates a self-built automated code security review system triggered on every git push, combining a coordinator plus five specialist Claude sub-agents, Anthropic's own security review prompt, and an adversarial cross-vendor pass via the Codex CLI — all tracked in a Supabase-backed Next.js dashboard. He highlights a recently fixed bug where dismissed false positives weren't properly persisting due to inconsistent model-generated finding titles.
-->

[01:25:13–01:25:32] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: describes a git pre-push hook that captures the local diff, with secrets scanned and redacted before anything reaches a model or database. The dashboard (built on **Vercel** with **Supabase** [tool:Vercel][tool:Supabase]) tracks all findings from local Claude Code security reviews.
[01:25:56–01:26:23] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: the review consists of three engines: (1) a coordinator plus five specialist agents (security, documentation, code review, etc.) each running with stripped tool access, explicit deny-lists, and isolated MCP so they can only see the redacted diff — never files, commands, or network; (2) Anthropic's own built-in security review prompt on a separate model; (3) **OpenAI Codex** [tool:OpenAI Codex] CLI run as a cross-vendor adversarial pass.
[01:26:47–01:27:20] Brandon Hancock: <Q>Are you using existing subscription plans or API tokens to run this?</Q> Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: <A>Built to support either; currently running on his own Codex and Anthropic subscription plans, with the system flexible enough to switch if vendors change headless-mode policies.</A>
[01:27:27–01:28:30] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: architecture is a Node CLI acting as the deterministic local orchestrator (triggered by the git hook), so "the models only ever do judgment." First-time pushes trigger a full onboarding code-base scan (configurable to block); subsequent pushes typically run in "shadow mode," reviewing without blocking the push.
[01:28:42–01:29:41] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com: describes the key recent fix — a "living layer" of findings (open/fixed/false-positive/dismissed) wasn't properly matching dismissed findings across review runs because different models phrase the same finding differently. ▶ He implemented fuzzy matching across title and body so dismissed/false-positive reasoning now persists as context fed into future specialist prompts (not just a suppression list), preventing the same bad finding from being regenerated, paid for, and filtered out repeatedly. A guard also prevents a dismissed warning from being silently cleared by a fresh "critical" relabeling.
[01:30:17–01:31:11] Ryan - One Stop Creative Agency confirms he's used the tool on an early, messy personal project: "the performance is way better... it had 80 things that it found that I fixed pretty much all of them... it's night and day now."
[01:31:59–01:32:05] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com notes Codex tends to catch different classes of issues (edge cases, performance) than Anthropic's own review, reinforcing the value of cross-model blending. ▶ "Cross-model and cross-company stuff I think is super important to blend it together."
[01:33:43–01:34:00] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com runs a live test push against an in-progress SOP-documentation app for construction companies to demonstrate the pipeline end-to-end, showing near-real-time updates in the dashboard as findings arrive.
[01:35:19–01:36:00] Juan Torres asks whether this could double as an AI FinOps tracking tool at the organizational level; Patrick Chouinard agrees tracking token/credit usage this way is valuable, but sees greater potential in encoding organization-specific governance/compliance validation rules into the review pipeline, beyond generic code correctness.
[01:36:46–01:37:06] mdcatc notes a parallel use case: he maintains custom scripts ensuring website copy for therapist clients doesn't violate licensure rules, and suggests this kind of compliance-specific review would fit naturally into Scott's system as a pluggable rule set.

---

<!--SEGMENT
topic: Security Review Tool — Monetization Strategy
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Brandon Hancock, Patrick Chouinard
keywords: go-to-market, CodeRabbit competitor, freemium plugin, ICP for security tooling, WorkOS, multi-tenant Supabase, marketplace distribution, bring-your-own-keys enterprise
summary: The group debates how Scott Rippey could commercialize his security review system, comparing it to CodeRabbit and weighing enterprise vs. solo-developer positioning. Brandon Hancock and Patrick Chouinard converge on recommending a free/freemium marketplace plugin distribution strategy with paid enterprise integrations (e.g., WorkOS, custom governance rules) to gather real market feedback before fully productizing.
-->

[01:40:00–01:41:57] Brandon Hancock asks Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com about go-to-market strategy compared to **CodeRabbit** [tool:CodeRabbit]: <Q>Who's the target customer — solo developers, small teams, or enterprises requiring heavier compliance/rules — and what clearly differentiates this from CodeRabbit?</Q> He draws a parallel to the earlier Alireza/Agent-Task differentiation discussion.
[01:42:20–01:42:59] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com admits he's been "noodling" on this without a clear answer — the system currently requires local setup (hooks on a machine) rather than being a simple hosted signup product, making distribution non-trivial.
[01:43:27–01:43:59] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com floats an idea: package it as a plugin for the same model ecosystems being discussed elsewhere (Hermes, OpenClaw, etc.), offering ~50-60% of functionality free and gating the rest.
[01:44:00–01:44:11] Patrick Chouinard reframes the core question crisply: ▶ "What's the problem we're solving in one sentence that's different from Claude Code or CodeRabbit, then part two, how do I get it to those people?" He suggests positioning as "a model-agnostic code reviewer... plugged into X" and reaching customers by embedding as a plugin inside an existing marketplace (e.g., a Hermes plugin) rather than building distribution from scratch.
[01:45:00–01:45:11] Patrick Chouinard adds that packaging could include an `install.md` so Claude Code itself acts as the installer, following instructions automatically for minimal setup friction.
[01:45:20–01:46:24] Patrick Chouinard highlights a strong enterprise angle: organizations increasingly worry about SaaS/cloud dependency for inference, and a bring-your-own-keys architecture (as Scott's system already supports) is "a high selling point for the enterprise," particularly for validating that enterprise-level coding rules/instructions are actually followed down to implementation — an emerging pain point as "citizen development" grows.
[01:46:24–01:48:00] Brandon Hancock recommends explicitly: ▶ make the tool a free plugin on a marketplace immediately, even though it feels premature: "if it's free and people are still not trying it, it gives you feedback... the second you put an offer or a product in front of customers, they're going to ask for more stuff." He argues real user conversations, not internal speculation, will reveal whether to monetize the current product or pivot entirely. ▶ "You can't steer a ship if it's sitting still."
[01:48:17–01:49:21] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com and Patrick Chouinard discuss a freemium tiering model: free up to a project limit, paid tiers unlocking integrations like **WorkOS** [tool:WorkOS] for enterprise SSO, noting the database overhead for this kind of telemetry is minimal.
[01:49:41–01:50:25] Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com clarifies the current architecture is single-tenant per customer (each gets their own Supabase project via Vercel/Google login), though it could be adapted to multi-tenant with more engineering.
[01:50:26–01:52:04] Brandon Hancock and Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com discuss the ease of pivoting infrastructure with AI-assisted development — e.g., swapping SQLite for hosted Postgres — as long as the system is built in an extensible way from the start.
[01:53:21–01:53:56] Patrick Chouinard extends the idea further: if telemetry captured the most frequent bugs/errors across a team, the system could proactively recommend improvements to CLAUDE.md or team skills, creating an organization-wide "self-improving loop" in coding quality. ▶ "Imagine that at a team level, you would increase the skill... of every single developer by contributing errors from other developers in the telemetry."

---

<!--SEGMENT
topic: AI Photo Booth Event Recap
speakers: Juan Torres, Brandon Hancock, mdcatc
keywords: AI photo booth, EC2 inference, image-to-image pipeline, QR code delivery, physical AI, event equipment, productionalization, autoscaling
summary: Juan Torres recaps running his first live event with an AI-powered photo booth application — which delivers both original and AI-transformed images via QR code — reporting successful real-world stress testing of network and inference reliability. He outlines next steps focused on productionalizing the backend (autoscaling groups) before expanding to image-to-video generation, and receives a warm-lead introduction from mdcatc.
-->

[01:54:57–01:55:35] Juan Torres reports running his first paid event the previous Saturday: "it went pretty well... the main task was to stress test the case studies... it went better than I thought." He confirms network egress and inference engine reliability held up under load, and his EC2 [tool:AWS EC2] backend instance wasn't overwhelmed by concurrent image-transformation and database tasks.
[01:56:07–01:56:28] Juan Torres: the phone-based image viewer worked reliably, letting attendees download both original and AI-transformed photos. The main friction point was physical setup/teardown time, which he plans to formalize into a standard operating procedure.
[01:56:46–01:57:14] Juan Torres describes the underlying app: an AI photo booth that delivers original photos plus AI-transformed images, run through his own custom pipeline; next steps include producing a promotional video for LinkedIn and Instagram, and productionalizing the backend.
[01:57:35–01:58:38] Brandon Hancock praises the milestone, requests the promotional video to potentially share with a friend's network (paused due to a new baby), and commends Juan for the courage to pitch and launch: ▶ "It takes guts to put yourself out there... dude, that is awesome."
[01:59:47–02:01:31] Brandon Hancock: <Q>What's next — more outreach, or more coding?</Q> Juan Torres: <A>Prioritizing productionalization first — moving the backend into an autoscaling group so API and image-retrieval/email delivery (zip files valid for 24 hours) remain highly available — before expanding into image-to-video generation, deliberately restraining the urge to chase the more exciting feature.</A>
[02:01:32–02:02:16] Brandon Hancock issues a challenge: ▶ complete a fixed list of remaining features, then no more coding until 10 paying customers are secured — using continual outreach/marketing as the gate, framing coding as "the carrot" earned only after sales milestones. mdcatc echoes this from his own painful experience with feature-heavy, sales-starved products.
[02:04:37–02:05:33] mdcatc offers a warm introduction to a San Diego-area event-rental-equipment business owner (PA systems, sound, chairs) as a potential distribution partner for Juan's photo booth at events like bar mitzvahs and quinceañeras. Juan Torres agrees to send his promotional video once ready.
[02:06:52–02:07:07] Juan Torres mentions he'll consult Patrick Chouinard (an AWS-native expert) separately on vertical vs. horizontal scaling questions for his Docker-based containerized architecture.

---

<!--SEGMENT
topic: Class2Curb Pricing Calculator and Case Study Strategy
speakers: mdcatc, Brandon Hancock, Patrick Chouinard
keywords: Class2Curb, school pickup automation, ROI calculator, hourly vs salary staff, charter school budget threshold, case studies, government sales cycle, minnow market advantage
summary: mdcatc demos his Class2Curb product — a school carpool-dismissal coordination app with an interactive ROI calculator for administrators — and receives feedback questioning a key cost assumption (teacher pay structure). Brandon Hancock and Patrick Chouinard advise prioritizing free pilot case studies over early revenue, framing the school market as a "minnow" segment where mdcatc effectively has no AI-savvy competition.
-->

[02:09:00–02:10:55] mdcatc demos **Class2Curb** [tool:Class2Curb][link:Class2Curb.com/Class2Curb.ai], showing an animation of the core workflow: an attendant enters car numbers at pickup, students are notified in their classrooms via display, and everyone arrives at the curb simultaneously — eliminating wasted wait time.
[02:10:44–02:11:39] mdcatc walks through an interactive ROI calculator with adjustable sliders (current dismissal time, staff count, hourly cost) showing time and dollar savings versus the current process (e.g., reducing dismissal from 35 to 25 minutes).
[02:11:41–02:12:00] Brandon Hancock: <Q>Are the teachers being modeled hourly or salaried? That assumption matters for the ROI math.</Q> mdcatc confirms the calculator assumes $35/hour. Brandon Hancock: ▶ "I would just check with a customer... if their salary, well, whether they work 90 hours a week or 20, they're getting paid the same" — recommending validating this assumption directly with prospects, since the true value driver might instead be time savings for parents, traffic reduction, or something else entirely.
[02:13:00–02:14:00] mdcatc reaffirms three core value points — parent time, teacher time, neighborhood traffic — but chose to monetize via a dollar-savings framing since that's what a budget-approver ultimately weighs, and notes school district contracts here are typically small ("minnows") requiring invoice-based payment rather than card/Stripe.
[02:14:39–02:14:59] mdcatc explains he intentionally priced the product under $1,500 so an individual charter school administrator can approve it without a board vote — directly paralleling Brandon Hancock's own EMSO strategy of staying under a $14,000 threshold to avoid triggering city council votes.
[02:15:14–02:15:30] mdcatc notes an even harder constraint on a separate product (a cemetery "Heritage Plot" tool): county government budgets are annual, not quarterly, requiring pre-planning up to a year in advance.
[02:15:42–02:16:36] Brandon Hancock draws a direct parallel to EMSO's own slow government sales cycles, expressing regret at not building pipeline earlier: ▶ "Start building the relationship now so that it's in their mind and it's not new to them in six months."
[02:16:41–02:17:34] Brandon Hancock: ▶ recommends prioritizing free pilot case studies over immediate revenue — offering the software free for a semester/year to 5-10 schools in exchange for documented before/after metrics, since concrete results ("I helped save them 50% efficiency") make every future sales call dramatically easier than pitching product features. ▶ "Case studies make every future call we do easier."
[02:18:59–02:19:00] Patrick Chouinard reframes mdcatc's competitive position positively: even though school districts are individually small ("minnows"), mdcatc faces essentially no AI-savvy competition in that niche, making him effectively "a shark" in an otherwise underserved market. ▶ "There might be minnows, but you're a shark in there... you have extreme opportunity."
[02:19:53–02:20:39] mdcatc shares progress on the related "Heritage Plot" cemetery-mapping tool, including a new manual map-tracing tool that lets users create burial plot sections without needing to source GIS data from the county.

---

<!--SEGMENT
topic: Sales Outreach via Loom Videos
speakers: mdcatc, Brandon Hancock, Ryan - One Stop Creative Agency
keywords: Loom outreach, cold calling, asynchronous sales, daily quota, promise-proof-next-steps structure, idea sourcing methodology
summary: mdcatc describes shifting his sales approach from cold calling toward short asynchronous Loom videos structured around a clear promise-proof-next-steps format. Brandon Hancock reinforces this with tactical advice on keeping Looms brief and setting a daily outreach quota, while also answering a question about how mdcatc sources his product ideas from real-world workflow observation.
-->

[02:20:39–02:21:53] mdcatc describes his current outreach method using **Loom** [tool:Loom]: a short video walking through a fixed structure — what we do, three discussion points, demo, results/case studies, next steps — designed as an asynchronous, scalable alternative to scheduled cold calls. ▶ "It just makes it more asynchronous... it takes all the friction out of it."
[02:22:37–02:22:56] mdcatc relays a question relayed in chat from a participant ("Biggie"): <Q>Do you do a lot of research to come up with your product ideas, or do they come from problems in your life?</Q>
[02:23:00–02:23:53] mdcatc: <A>Mostly from paying close attention to real workflows throughout his career — observing where people waste time or experience unnecessary stress, regardless of whether it changes output quality. The Class2Curb concept originated from a similar PHP-based app he built roughly 12-13 years ago for his own kids' school pickup, reducing pickup time from two hours to 15-20 minutes.</A>
[02:24:24–02:24:53] Brandon Hancock suggests explicitly including that origin story/track record as a "proof slide" in the Loom — demonstrating prior experience solving the exact problem, now enhanced with AI. ▶ "That's literally all it is... promise, proof, next steps."
[02:25:20–02:26:11] Brandon Hancock gives tactical Loom advice: keep videos short and lead with the value proposition rather than backstory. ▶ "Don't bury the lead... speak plainly. I can help you. Here's what we do. I'd love to talk to you."
[02:26:25–02:26:39] Brandon Hancock: ▶ recommends setting a firm daily Loom quota (e.g., three to five per day) as a personal discipline rule, tying further coding work to hitting that outreach quota — reiterating the same challenge given earlier to Juan Torres.
[02:26:47–02:27:27] Ryan - One Stop Creative Agency notes he follows a similar personal quota system for his own outreach given a smaller customer base, suggesting shorter, quicker videos are appropriate when just starting out.

---

<!--SEGMENT
topic: AI-Generated Real Estate Marketing Websites
speakers: Ryan - One Stop Creative Agency, Brandon Hancock, Juan Torres
keywords: scroll animation website, private jet company spec pitch, estate agency website, AI headshots, Claude Design, pricing UK market
summary: Ryan demos two client-facing web projects built with AI-assisted animation techniques — a speculative "spec pitch" redesign of a private jet charter company's website and a live estate agency website — including AI-generated headshots replacing outdated photography, while discussing UK pricing constraints (~£2,500 per site) relative to what similar work commands in the US.
-->

[02:28:51–02:29:19] Ryan - One Stop Creative Agency demos a fully scroll-animated website he built overnight as a speculative "spec pitch" redesign for a private jet charter company he found online, planning to reach out to see if they'd buy it. Brandon Hancock reacts positively to the animation quality.
[02:30:01–02:30:34] Ryan - One Stop Creative Agency continues the demo, showing the full range of jets pulled from the client's existing site content, noting the original site "is really ugly... feels like I'm booking an Airbnb."
[02:30:39–02:30:56] Ryan - One Stop Creative Agency shows a second project: a live estate agency website he built for an actual paying client, calling it "one of the better looking estate agency websites in the area," with numerous lead-capture modals and property guide content (referencing the Ascot horse-racing area).
[02:31:21–02:31:40] Brandon Hancock: <Q>How much are you charging for that?</Q> Ryan - One Stop Creative Agency: <A>"Not enough" — around £2,500 (~$3,200), acknowledging the client "battered me on price," but valuing it as an initial portfolio piece.</A>
[02:31:48–02:32:41] Ryan - One Stop Creative Agency shows AI-generated headshots replacing the agency's outdated photography. Brandon Hancock draws a comparison to his sister's real-estate experience, where similarly polished imagery previously required expensive pre-AI videographer shoots, noting AI now makes that quality far more accessible.
[02:32:56–02:33:17] Ryan - One Stop Creative Agency notes his primary income source is actually real estate videography, and this website work has natural synergy with those existing client relationships, mentioning he secured this estate agency client simply by walking into their storefront and asking.

---

<!--SEGMENT
topic: AI Video Generation for Real Estate and UK Pricing Constraints
speakers: Ryan - One Stop Creative Agency, Brandon Hancock, Juan Torres, Patrick Chouinard
keywords: Higgsfield CLI, Seedance, Nanobanana, Gaussian Splats, real estate video pricing, UK vs US market, image-to-video pipeline, before/after renovation video
summary: Ryan demonstrates AI-generated real estate video content built with an image-to-video pipeline (Nanobanana for stills, Seedance for motion via Higgsfield CLI), explaining that despite strong output quality, UK real estate clients won't pay comparable US rates, capping his pricing far below what similar AI/video services command stateside.
-->

[02:33:37–02:33:59] Ryan - One Stop Creative Agency explains his image-to-video rendering pipeline: he uses **Nanobanana** [tool:Nanobanana] to generate a still image with a prompted camera movement description, then pushes it through **Seedance** [tool:Seedance] at 4K/15 seconds via the **Higgsfield CLI** [tool:Higgsfield CLI], noting 1080p "doesn't quite cut it."
[02:34:20–02:34:44] Ryan - One Stop Creative Agency shows example luxury property renders (one rental listed at £17,000/month, ~$23,000/month) generated this way, noting he can't reuse other agents' proprietary imagery for actual client work but uses these as style references.
[02:36:38–02:37:00] Ryan - One Stop Creative Agency plays an actual delivered client video incorporating AI-generated time-lapse elements, for which he charged roughly £600 (~$780) — noting Instagram's declining organic reach ("Mark Zuckerberg has blood on his hands") has made it harder to justify even that rate to clients.
[02:37:44–02:38:00] Juan Torres: <Q>Have you looked at world models using Gaussian Splats for 3D property walkthroughs?</Q> Ryan - One Stop Creative Agency: <A>Yes, he follows creators like Corridor Digital's Gaussian Splat work, but the 3D walkthrough market locally is already dominated by established players who rent equipment cheaply directly to agents, making it a crowded niche he's chosen not to pursue.</A>
[02:38:59–02:39:40] Ryan - One Stop Creative Agency shows a before/after style AI video for a dilapidated property (mold, poor condition) marketed toward developers, charging around £400 given the property's low value tier, noting the time and travel cost of production.
[02:39:47–02:40:26] Ryan - One Stop Creative Agency states his broader strategic goal is to move away from labor-intensive video shoots entirely and focus on his "screens" software product line, which is scaling well with new signups, plus a recently Claude-Design-redesigned social app and an in-progress mobile-optimization of his client portal.
[02:40:59–02:41:16] Brandon Hancock and Ryan - One Stop Creative Agency discuss the stark pricing gap: similar AI/video real estate content commands $10,000-$15,000 in the US market versus £600-700 in Ryan's UK market, which he attributes to what local clients are willing/able to pay rather than production quality.

---

<!--SEGMENT
topic: Scaling AI Real Estate Video Across Markets
speakers: Brandon Hancock, Juan Torres, Ryan - One Stop Creative Agency, Patrick Chouinard
keywords: image-only pipeline feasibility, US market expansion, Upwork contracted photographers, photo quality feedback loop, listing disclosure laws
summary: The group brainstorms whether Ryan's AI video pipeline could work from photographs alone (rather than his own on-site filming) to enable remote service delivery into the higher-paying US real estate market, discussing contracted local photographers, a simple photo-quality guide/checklist as a low-tech feedback mechanism, and legal caution around altering listing images.
-->

[02:41:41–02:42:04] Ryan - One Stop Creative Agency clarifies his existing showcase videos come from his own on-site filming, not photographs, but confirms he hasn't tested how well the pipeline works starting purely from still images.
[02:42:52–02:43:00] Brandon Hancock proposes sending example videos to his sister, a US real estate agent working with investors, to gauge interest in this service for the US market, since it could reach clients "with a budget purely to make sure that [a] multi-million dollar house gets a little bit more" polish.
[02:43:34–02:44:37] Brandon Hancock and Ryan - One Stop Creative Agency discuss outsourcing image capture via **Upwork** [tool:Upwork] contractors who simply take requested photos on-site, with Ryan's AI pipeline handling all downstream image editing/video generation — including AI room "staging" (clearing clutter, virtually furnishing empty rooms).
[02:45:59–02:46:32] Juan Torres proposes a thought experiment: could Ryan operate as a US-facing service by hiring local Upwork photographers per listing and running his existing pipeline remotely? Ryan - One Stop Creative Agency: <A>Feasible in principle, though output quality is highly dependent on input photo quality, and real estate photography skill varies widely, especially from less experienced Upwork photographers.</A>
[02:47:00–02:47:53] Brandon Hancock and Ryan - One Stop Creative Agency brainstorm a low-tech solution: ▶ a simple visual checklist/guide showing "good" vs. "bad" example shots for each required angle (front view, side view, etc.) to coach non-expert photographers to roughly 85% quality without needing a sophisticated app. ▶ Brandon Hancock: "It's literally ShipKit... for every step of the pipeline, give it max context on what's good and what's bad."
[02:48:00–02:48:58] Juan Torres suggests a more automated version: reviewing edited shots post-capture with software that gives improvement tips per shot type, potentially bundled as a paid subscription an estate agency requires its photographers to use.
[02:49:02–02:50:00] Patrick Chouinard raises a caution: enhancing/altering listing photos too aggressively can create legal exposure around real estate "misdescription" laws, so any AI photo modification needs to stay within disclosure boundaries.
[02:50:00–02:51:44] Brandon Hancock reframes the simplest viable version: ▶ a PDF "picture book" checklist handed to any on-site photographer showing exactly which 15 shots to capture and examples of good/bad framing — requiring no app at all — as the minimum viable front-end to the video-generation backend. ▶ "That is your entire front of business model, and then three days later, they have a video."
[02:51:44–02:53:08] Ryan - One Stop Creative Agency commits to emailing Brandon Hancock example videos and iterating on the checklist idea; Brandon Hancock agrees to share them with his sister for US market feedback, floating a potential at-cost pilot test on a real listing.

---

<!--SEGMENT
topic: Closing Tips — Interactive HTML Presentations
speakers: Patrick Chouinard, Brandon Hancock, Ryan - One Stop Creative Agency
keywords: Claude Design, interactive HTML slides, PowerPoint alternative, Higgsfield CLI, Google motion graphics model, Remotion
summary: In closing remarks, Patrick Chouinard advises Brandon Hancock to replace his outreach PowerPoint decks with interactive HTML built via Claude Design for a more polished, animated presentation experience, and the group layers on additional tool suggestions (Higgsfield CLI, a new Google motion-graphics model, Remotion) before wrapping the call.
-->

[02:53:09–02:53:23] Patrick Chouinard flags, half-jokingly, an "allergic reaction" to seeing Brandon Hancock's outreach PowerPoint decks, offering unsolicited advice.
[02:53:36–02:53:59] Patrick Chouinard: ▶ recommends using **Claude Design** [tool:Claude Design] to convert brand-kit PowerPoint decks into interactive HTML slides for Loom-embedded pitches, claiming it "bumps the quality and the interactiveness of the showcase by 20x" and that Claude "will do an insane job very, very quickly." He notes he's driving a similar PowerPoint-to-HTML transformation at his own (PowerPoint-native investment firm) workplace.
[02:54:34–02:54:59] Brandon Hancock clarifies his understanding: converting slides into clickable, keyboard-navigable interactive HTML with built-in transitions/animations, avoiding the tedium of manual PowerPoint animation work Patrick describes.
[02:55:41–02:56:00] Ryan - One Stop Creative Agency and Patrick Chouinard suggest layering in **Higgsfield CLI** [tool:Higgsfield CLI] (referencing a $50/month plan with direct Claude Code integration for video generation models) plus a new **Google** motion-graphics-focused model (referred to as "Omni") for advanced animated visuals.
[02:56:35–02:57:31] Ryan - One Stop Creative Agency adds **Remotion** [tool:Remotion] as a complementary interface, suggesting combining all three (Claude Design, Higgsfield/Omni, Remotion) for maximum polish; Brandon Hancock jokes that at that point clients might just ask him to build their PowerPoints professionally.
[02:57:05–02:58:31] Brandon Hancock clarifies the tool name as **Google Omni** [tool:Google Omni] after confusion with "Flow"/"Stitch," noting it accepts structured JSON prompts via CLI for finer control than natural-language prompting through its website, and thanks the group for leveling up his presentation workflow.
[02:58:49] Brandon Hancock closes the call, thanking participants and confirming he'll be recording outreach Looms immediately afterward.