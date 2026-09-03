=== SESSION ===
date: unspecified (recent, post-Claude-5.1-release era)
duration_estimate: ~45 minutes
main_themes: T3 Code adoption and agentic development workflows; startup update (EMSO, fundraising, cold outreach); new side-project Listio.ai and customer-validation-first methodology; AI model cost curves and model selection; personal agentic OS architecture (dashboards, knowledge graphs, chief-of-staff agents); observability and meta-review of agent pipelines

---

<!--SEGMENT
topic: T3 Code adoption and remote dev workflow
speakers: Patrick Chouinard, Paul Miller, Bastian Venegas
keywords: T3 Code, T3 dev agent, CMUX IDE, Claude, Codex, Claude 5.1, subscription, VM, remote access, Cursor, SpaceX, Proxmox
summary: Patrick, Paul, and Bastian discuss Patrick's full migration to T3 Code over two weeks, how it leverages existing subscriptions and harnesses, and its superior remote access compared to Claude and Codex native remote tooling. They also touch on the overnight 5.1 update not yet appearing in T3 Code.
-->

[00:00:00] Patrick Chouinard: This meeting is being recorded. Hey, Paul. How's it going? You're on.

[00:00:08] Paul Miller: Hey, Patrick. How's it going?

[00:00:15] Patrick Chouinard: Cross our fingers, it's supposed to be a Brendan week. Did you text him today or was it the other day? Well, not today, but I texted him and he told me he was going to be there. I never announce a Brendan week without his say-so.

[00:00:43] Paul Miller: Well, supposedly he has some good news for us today... very interesting times. 5.1 update overnight. That seems interesting.

[00:01:11] Patrick Chouinard: Yeah, the only thing is it's not showing up in T3 code yet.

[00:01:39] Patrick Chouinard: ▶ I've been exclusively using [tool:T3 Code] for about two weeks now, and it's a complete revolution of the way I work.

[00:01:51] Paul Miller: So are you using the T3 dev agent? I've been doing everything through [tool:CMUX IDE] at the moment, but it's not really ideal.

[00:02:05] Patrick Chouinard: ▶ It uses your subscription and leverages the harness you already have installed. You have the interface, the link, the T3 server. That's insane because now I can have my workstation doing some work and the actual development going on on the VM somewhere else.

[00:02:38] Patrick Chouinard: ▶ The remote stuff is vastly superior to Claude and Codex native remote access.

[00:02:52] Paul Miller: I followed your lead and did the big jump into loading Hermes. I've also got GrokBot going as well.

[00:03:03] Patrick Chouinard: You know that Hermes has HermesBots that are really inspired by Grok.

[00:03:18] Patrick Chouinard: I just can't get myself to give any money to Grok.

[00:03:22] Paul Miller: I have a real issue technically with him for a number of reasons, one of which is on the security side, how he just went and stole all people's inputs and reused it.

[00:03:39] Patrick Chouinard: ▶ I've canceled my Cursor subscription since it was acquired by SpaceX.

[00:03:52] Patrick Chouinard: ▶ Especially when you can have all of your Codex and Claude Code sessions inside of the same interface, aggregated by project.

[00:04:17] Patrick Chouinard: I actually had to create myself a dashboard just to follow all of the interdependent projects I'm working on because I couldn't follow anymore which task was dependent on which other task. All of my deliverables are split by package... So now I have a dashboard where I can just copy and paste the seed prompt, give it to a new session, start developing. As soon as it's committing, it rebuilds the site. ▶ Basically I need an assistant just to know what job to give to my other assistants.

---

<!--SEGMENT
topic: Brandon's startup update and outreach machine
speakers: Brandon Hancock, Patrick Chouinard, Hemal Shah
keywords: EMSO, SOC 2, HIPAA, enterprise sales, fundraising, investment round, Instantly, cold outreach, distributors, pipeline, agencies, Raul
summary: Brandon gives a life-of-a-startup update: enterprise sales cycles take ~5 months despite completing SOC 2 and HIPAA compliance, forcing another investment round. He demonstrates a cold outreach machine built on Instantly to contact 5,000–8,000 agencies over 45 days, and shares the lesson of not lining up customers before compliance was complete.
-->

[00:05:19] Hemal Shah: Patrick, roughly most of your projects, are those agentic software, generative AI software, or traditional?

[00:05:29] Patrick Chouinard: It's actually the building block of my agentic OS — stuff managing my infrastructure, extra tools for Hermes, a bunch of daily reports. Now I have it building a dashboard for all of the field output... updating my intelligence dashboard, my daily news feed, and now I want that integrated into Hermes because Hermes has multiple profiles. That's why I need the board to manage what belongs to what.

[00:06:25] Brandon Hancock: What I'd love to do is give you guys a quick update... life of a startup. ▶ We have learned very quickly that enterprise sales take forever — by that I mean like five months. After finishing all of our SOC 2 and HIPAA stuff, we were like, fantastic, the floodgates are going to happen. And then we're just stuck in limbo waiting for legal to talk to their other person to talk to their other person.

[00:07:47] Brandon Hancock: With that being said, we're actually having to do another investment round of some sort. Fingers crossed that goes through, so I can work full-time without having to go get another job.

[00:08:10] Brandon Hancock: Outside of that, going super deep into [tool:Instantly]. We have built a cold outreach machine. We have Raul doing day-to-day direct outreach, we're working with distributors in the discovery process... Over the next 45 days, reach out to hopefully 5,000 to 8,000 agencies and just blast all of them, because we just have to explode our pipeline. We tried ads, the conversion rates were too slow. It's great because every customer is a public employee so we can find them.

[00:09:27] Brandon Hancock: ▶ Lesson learned, learn from my battle scars: we rushed to get SOC 2 and HIPAA completed, and what we should have done at the same time is had 100 customers waiting to say "we will buy as soon as HIPAA or SOC 2 is done." Instead we lost out on three or four months. Now we're just playing catch up.

---

<!--SEGMENT
topic: Listio.ai side project and validation-first challenge
speakers: Brandon Hancock
keywords: Listio.ai, lead magnets, YouTube creators, Kit, ConvertKit, Bitly, GLM 5.3, landing pages, customer discovery, ShipKit, Google Cloud, timeboxing
summary: Brandon unveils Listio.ai, a tool helping YouTube content creators generate per-video lead magnet pages, positioned as "Bitly meets ConvertKit meets lead magnet software." He shares his self-imposed challenge to reach $2K–5K MRR in 30 days and his rule of finding 1,000 customers before writing any code, plus a two-week forced launch deadline.
-->

[00:10:00] Brandon Hancock: Now that coding slowed down a little bit for EMSO, I'm starting to tinker with some ideas. I want to do a challenge for myself to see if I could make 2K, 3K, 5K per month recurring in 30 days.

[00:10:30] Brandon Hancock: I bought a website, [tool:Listio.ai] [link:listio.ai], where I'm going to help content creators work on creating all of their lead magnet software. Anytime you go to one of my YouTube videos, you'll see at the bottom a bunch of "here's a free thing." There are legitimately thousands of people on YouTube who are not capturing emails. They have thousands of subscribers but they just give away everything for free — they could be growing a business and giving their audiences even more value.

[00:11:24] Brandon Hancock: The only option today is they build a whole website themselves, or they use [tool:Kit] — and if they use Kit, you make one landing page and that's it for everything. I made this landing page back in 2024 and really haven't touched it, but every single YouTube video I have points to this. I should have a custom lead magnet page per lead magnet to increase conversions, and AI should do all of it.

[00:12:05] Brandon Hancock: Now that AI is getting cheaper, GLM 5.3 specifically, I'm going to make a new website where people can just upload their video and I'll make the website page, the custom link. ▶ It's like Bitly meets ConvertKit meets lead magnet software.

[00:12:25] Brandon Hancock: ▶ I have forced myself to find a thousand customers and their email addresses before I even build a single line of code. I made this exact same mistake with EMSO. If I cannot actively find a thousand people and a way to contact them to pitch them, it's not worth an idea to build. If you can't think of a pure sales engine and a product engine at the same time, I wasn't going to try it.

[00:13:12] Brandon Hancock: Hopefully in 30 days we'll have a cool little app to share. I'm documenting the whole process — eventually it'll probably be something I could put inside of [tool:ShipKit]. It'll be a Google Cloud project. Building now that AI has had a year of ShipKit — the cloud design now is so much better than what we were doing.

[00:15:30] Brandon Hancock: Even for this build, I have two weeks basically for my Instantly campaigns to warm up, and that's going to be my deadline for launching v1. ▶ I'm self-imposing a two-week deadline, then I won't touch it until people say "yes, I'd like to try it." Launch, let the email campaign run, wait a week to see if I get any traffic — if I do, then it's time to keep building.

---

<!--SEGMENT
topic: Model cost curves and model selection economics
speakers: Brandon Hancock, Paul Miller
keywords: DeepSeek v4 Flash, Luna, Gemini, GLM 5.3 Flash, OpenRouter, BAA, classification, cost per task, HIPAA, Chinese models, Kimmy K, fine-tuning
summary: Brandon describes building a YouTube scraper to find 1,000 prospective customers, classifying descriptions with an LLM. Switching from Luna to DeepSeek v4 Flash cut the cost from ~$350 to $3 — a 100x saving on identical classification quality. He also explains EMSO's AI service costs 10x'd in eight months and will reset when GLM 5.3 becomes available, and why OpenRouter and non-US-hosted models are blocked by customer BAA requirements.
-->

[00:13:53] Brandon Hancock: In order to find a thousand customers, I had to build a YouTube scraper to find YouTube audiences, look at their descriptions, see if they were offering a lead magnet. I was going to use the [tool:Luna] model to look at the prompt, classify it — if they were giving away stuff for free, what they were doing — classifying all of it to find ideal customers. It was going to cost me like $350, and then I was like, wait, I'm just doing a classification, just 10,000 times. ▶ I swapped to [tool:DeepSeek v4 Flash] and it cost me $3 — I literally saved a hundred X by just changing models. First time I've seen a model change do the exact same level of intelligence but a hundred times cheaper.

[00:14:47] Brandon Hancock: I'm so excited to get away a little bit from HIPAA-regulated stuff, because I can't use these Chinese models, and do more personal stuff — I'm having a field day playing with all of them.

[00:16:14] Brandon Hancock: The model I need is GLM 5.3 Flash. That will become our new default model for everything — it's just waiting to go out. It's so new, it's not there yet.

[00:16:36] Brandon Hancock: As an AI service, we've constantly been asking ourselves, how can we make the value for our customers better and better? When we built EMSO back in the day, it was literally one prompt that would write a narrative. Now we still write a narrative, then do an integrity check to make sure everything said in the narrative sources back to the original item. After that, we have a live QA feature which finds all the gaps between a perfect narrative and a subpar one.

[00:17:25] Brandon Hancock: ▶ Our cost for providing AI services has 10x'd over the past eight months — it cost us $0.05 and now it's $0.50 to $0.80 depending on what we're doing. As soon as GLM 5.3 comes back out, we're going to reset the clock at $0.05. ▶ For anyone building AI-related software: look at the cost curves. Yes, new features might eat into your revenue for three to six months, but then it resets and you're back at providing an insane amount of value at a really cheap cost. It is the coolest thing to see depreciation happen in real time and the cost of intelligence going towards zero.

[00:18:39] Brandon Hancock: OpenRouter is awesome. We just have to have a BAA with these different agreements, and a lot of these models are outside the United States, and our customers only want things in Google Cloud, AWS hosted on American infrastructure. Even the Kimmy K one — we'd love to try it, it was just a little slow. We'd love to fine-tune our own at some point, but we have to come up with the data ourselves — we can't use customer data. ▶ We need to sell and make more money first before more engineering work. That's our motto.

---

<!--SEGMENT
topic: Patrick's agentic OS and T3 Code server plan
speakers: Patrick Chouinard, Brandon Hancock
keywords: T3 Code, Proxmox, VM, home lab, Pachu plan, markdown repo, task dashboard, commit skill, AgentOps, Hermes, parallel projects, seed prompt
summary: Patrick details his vacation project: migrating fully to T3 Code and installing a T3 Code server on his Proxmox home lab so his Mac is just a thin client. He shows his task dashboard built from a markdown-only "Pachu plan" repo, updated automatically by a skill that analyzes every commit, coordinating 35 packages across 7 underlying projects with workers dispatched via SSH wherever needed.
-->

[00:19:56] Patrick Chouinard: I'm finally on vacation — basically I just split my work from basic cloud to other AI providers and implementation platforms. I've pretty much transferred almost 100% to T3 code now. All of my cloud and codex stuff is just happening within the T3 code interface.

[00:20:42] Patrick Chouinard: ▶ I want to start a new project in T3 code based on the infrastructure of my home lab to install a T3 code server. The GUI application running on my Mac is just going to be a thin client, and everything's going to happen in a Proxmox VM on the back end.

[00:21:13] Brandon Hancock: Can I ask a quick T3 question? I downloaded it like two weeks ago — it felt very much like coding inside of Codex or Claude Code's GUI. Is there a way to work on stuff in side-by-side tabs? A lot of times I have a worker orchestrator and two tabs.

[00:21:49] Patrick Chouinard: I don't have side-by-side tabs, I have a bunch of tabs working simultaneously. The bigger problem I was having is which task I needed to work on next — the order in which I need to implement, because they're all working on the same project.

[00:22:11] Patrick Chouinard: Everything I'm working on right now is basically the foundation of an agentic OS. I have one major project called the Pachu plan, which is a repo composed only of markdowns — basically my program guide. Here's all the packages, all the repos you need to focus on, which machine they're on, all of the infrastructure. But the thing is, what do I work on and when? So I built myself a map: deployment wave, where I'm standing, next up. All the green tasks have been implemented; when you point, you see all the relationships between the different tasks. ▶ The queue is text I can literally cut and paste into a new Claude Code or Codex session, and it's enough for it to find the rest of the information within the markdown of the project.

[00:24:09] Brandon Hancock: What is feeding or populating this queue? Something has to be monitoring the work and pushing up, right?

[00:24:18] Patrick Chouinard: ▶ I have a skill that analyzes every single commit I do. Every commit and every PR that gets merged updates a file that is used to generate that dashboard.

[00:24:41] Brandon Hancock: How many parallel projects was that? Thirty-five?

[00:24:45] Patrick Chouinard: There are 35 packages I need to build, but essentially seven underlying projects behind it, including Hermes treated as a project.

[00:25:26] Brandon Hancock: Where are the workers running?

[00:25:32] Patrick Chouinard: They run wherever they need to run. If I have a project that needs to be developed on Hermes, it SSHes into Hermes and starts a session, because all of the VMs have Claude Code and Codex deployed. It can trigger the worker wherever it needs to be based on the infrastructure and location.

---

<!--SEGMENT
topic: Chief-of-staff agent and InfraKnowledge graph
speakers: Patrick Chouinard, Brandon Hancock, Elijah Stambaugh
keywords: Hermes, chief of staff, specialized agents, researcher, operator, coder, InfraKnowledge, knowledge graph, markdown files, dependency sequencing, monorepo, agentic OS, context load
summary: Patrick explains his Hermes architecture: the default profile is a chief-of-staff agent specialized in understanding him and delegating, while specialist agents (researcher, operator, coder) carry their own tools, skills, and memory. Elijah asks how the knowledge spine is structured; Patrick describes InfraKnowledge, a markdown-only project feeding a knowledge graph that computes implementation order and safe parallel work. Brandon shares his meta-idea of an agent that reviews the whole development pipeline after each merge.
-->

[00:26:00] Patrick Chouinard: A lot of the work happens in something I call AgentOps — the big CLI/MCP that exposes my entire Proxmox infrastructure to the agent framework. The rest is stuff like Infra Knowledge, a database of all the inventory/role/policy of my infrastructure, updated anytime something changes. I've started to rip out all of the functionality out of my main Hermes profile and make it a specialist in understanding me. ▶ Its role is chief of staff: it knows how to interact with me and how its team can be leveraged. Now I have a specialist researcher, an operator, a coder, and it will invoke whichever profile when needed.

[00:27:16] Brandon Hancock: I feel like I pulled a Patrick this week. One of the coolest things Patrick does routinely is he works on the work itself — his agentic process. What I started to experiment with: my software development lifecycle has so many steps — brainstorm, write the plan, poke holes in the plan, come up with deliverables, implement, review, merge into staging. Normally I just go through it and at the end go "ah, you messed up, fix it." ▶ I now have something that sits above, monitoring the process: when we merge staging into dev, it goes back and looks at the entire work pipeline to identify "hey, your poke-holes-in-plan skill is missing so much stuff, or there's a whole second thing that should be happening here." I'm continually critiquing my skills — why am I not being meta about my skill flow? This understands my process, like yours understands you.

[00:29:23] Elijah Stambaugh: <Q>How do you structure that knowledge spine? You have this idea that your chief of staff knows where to go and how to get there, and you're stripping your Hermes down to just being that particular knowledge base.</Q>

[00:29:50] Patrick Chouinard: <A>Not the Hermes itself — Hermes has multiple profiles, multiple agents and sub-agents living inside. The default profile is the chief of staff. Every time I remove a role from the chief of staff and develop a specialized agent for it, I give that specialized agent all the tools, skills, knowledge, and memory it requires to do its job — but I remove that context load from the main agent and replace it with an understanding of the sub-agent's role. The main agent becomes an expert at what I want, how I work, and the sub-agents at its disposal, instead of being the executor for everything.</A>

[00:30:47] Patrick Chouinard: As for the knowledge spine itself, it's a sub-project I call InfraKnowledge that hosts all the planning, decisions, sequencing of a package, all the dependencies, and loads it into a knowledge graph. Out of that knowledge graph it builds me: here's the order in which you need to implement those packages, and here are the packages you can work on in parallel that won't screw each other.

[00:31:27] Elijah Stambaugh: <Q>Is that basically a markdown file, or a database structure?</Q>

[00:31:36] Patrick Chouinard: <A>No, multiple markdown files — an entire project that's just markdown. I'm using projects as islands of information: my plan project, my InfraKnowledge (all inventory and policy), and the implementation projects themselves — Hermes, AgentOps, all the sub-projects. Eventually the goal is to aggregate that into a single large monorepo that will be my agentic OS.</A>

---

<!--SEGMENT
topic: Observability and meta-review of agent pipelines
speakers: Juan Torres, Patrick Chouinard, Brandon Hancock
keywords: Prometheus, Grafana, Loki, observability, CI/CD, agent logs, structured outputs, session review, debugging, security analysis, mini PCs
summary: Juan asks what logs and observability Patrick generates across his agent pipeline; Patrick describes a full Prometheus/Grafana/Loki monitoring backend fed by every application, with AgentOps able to read the observability platform — all running on three mini PCs. Brandon elaborates on his end-of-session meta-review approach and its structured outputs per lifecycle step.
-->

[00:32:38] Juan Torres: The knowledge graph was one of the things I thought you'd need sooner or later — fascinating seeing you edify it. Regarding what Brandon was saying on the CI/CD pipeline agentic overview: <Q>Are the logs, the observability, through the artifacts generated for each agent in the pipeline? Which kind of logs are you generating in order to see through the whole system?</Q>

[00:33:20] Patrick Chouinard: <A>I have an entire monitoring and observability backend — a Prometheus server, a Grafana server, a Loki server — all fed by every single application I add. One of the functions of AgentOps is the ability to read all of those and understand the observability platform. And that sounds like I have a data center, but I literally have like three mini PCs and the desktop that runs all of that.</A>

[00:34:00] Brandon Hancock: On the code side, my setup knows what the ideal software development lifecycle is, so it's not always asking what to do next — we always go to the same flywheel. Every step has a structured output: when we clear a plan, here's what you expected; when we create the task template, here's what we expect; when we poke a hole, here's what we expect. Then the plan gets punched in the face by the real world with coding and testing. At the end of the session it goes back: "here's what theoretical was, here's what happened in actuality — identify room for improvement and suggest it." ▶ We're always moving fast with these agents, so just have it look in the rear-view mirror and check for you. It's a few extra tokens' worth of time, and it makes sense to always improve the thing you do every day.

[00:35:52] Juan Torres: It will be interesting to see Patrick's edification of the DataWeb application to manage observability, specifically with Grafana, seeing the metrics you're collecting on your servers.

[00:36:16] Patrick Chouinard: I'll be more than happy to bring that as soon as it's a little bit more production-ready.

---

<!--SEGMENT
topic: Dashboard vs. simple OS; visualization approaches
speakers: Shakur, Patrick Chouinard, Ty Wells
keywords: JSON file, grep, email digest, dashboard, visualization, complexity reduction, T3 Code server, ACS integration, project tower, Ty Wells
summary: Shakur questions the ROI of graphical dashboards, describing his simpler OS: a big greppable JSON file plus a daily email of status, next actions, and blockers. Patrick explains his dashboard is an aggregator preventing duplicate work and will eventually be clickable/executable, possibly replaced entirely by T3 Code if ACS integration lands. Ty Wells shows his "tower" visualization where lit floors represent project completion.
-->

[00:36:24] Shakur: I literally just started building my OS this week too. I kept looking at all the different OSes and graphical interfaces and asked, what is the real return on that? ▶ I went simpler: a huge JSON file I can just grep whatever is in there. It sends me an email each morning — here are all the things you have going on, proposed next actions, blockers. I was trying to get everything as simple as possible, and I found I'm moving a lot faster. <Q>What's the benefit of the big dashboard, linking everything together graphically? I purposely left that out to reduce complexity.</Q>

[00:37:45] Patrick Chouinard: <A>If I was just managing emails and meetings, I would probably do the same — that's what I do on my work account. But on my personal account I have so many sub-tools working actively that I need visualization just to know what's going on and what I can launch. Since I don't work on it day in and day out — I do have a day job — sometimes I forget I coded something and end up coding the same thing three or four times. So the dashboard is an aggregator.</A> ▶ To me, the graphical interface will be the last thing I build — something where I see all the tools at my disposal and can click a skill and have it executed in the backend. Not just cute charts — I can execute work directly from the interface.

[00:39:30] Patrick Chouinard: Honestly, if T3 implements their open issue about ACS integration — meaning T3 code could become an interface for Hermes on top of Claude Code and Codex — I would probably forgo the entire front-end interface and use T3 code as my universal interface platform for all of my agentic backend.

[00:40:03] Shakur: <Q>Have you set up a separate machine for T3? Right now I have it on one machine, and I'm looking to set up a couple of old laptops, strip them down, put Linux on them, and have T3 linked into that. If you do that before me, let me know how it goes.</Q>

[00:40:24] Patrick Chouinard: Believe me, as soon as it's done, you're going to see it the following Tuesday.

[00:40:36] Ty Wells: Since we're on the topic, I wanted to show you guys something — we're always down the same highway. This is my representation of the same thing. I needed a legend, it was so big. This tower is my representation of your building, Patrick — depending on how light it is, relative to how the project is going in terms of completeness. To be able to come in and execute a particular task and have that kicked off, you need to see it some sort of way. If the floor is full, that means the project is done.

[00:41:28] Brandon Hancock: That's a cool skyscraper. I log in tomorrow and the building's on its side and everything's on fire.

---

<!--SEGMENT
topic: Custom review model with Py.dev
speakers: Patrick Chouinard, Brandon Hancock
keywords: Py.dev, code review, security evaluation, red teaming, open source, plugins, Claude Code, Codex, model diversity, debugging specialist, work tree
summary: Patrick proposes building a custom, open-source review model based on Py.dev, fine-tuned specifically for code review, security evaluation, and red teaming — not coding — wrapped in plugins callable from Claude Code or Codex. Brandon agrees this is better than having the same model review itself and plans a call to incorporate it into his end-of-session review flow.
-->

[00:42:00] Patrick Chouinard: One last thing — you talked about your review cycle within your profile. Give me a call, because I'm working on something for review. We've been talking a lot about "always review with a different model, review with a different artist if you can." ▶ I decided to take the plunge and start using [tool:Py.dev], the open-source one that can be modified, and create a custom version specifically designed for code review, security evaluation, red teaming — not for coding, not for development, strictly for that — wrapped into a bunch of plugins to integrate it into Claude Code, Codex, whatever, to call upon it to do that job.

[00:43:00] Brandon Hancock: I 100% will — probably tomorrow afternoon or evening. Here's where I'm struggling, a thought exercise for everyone: I envisioned it like a person working from a task end to end, their whole thought process in one session, so I'd just have Claude go back through that session knowing it called all the skills in the same order. What you're suggesting is my task review should call what you're building instead of the same model calling itself. ▶ I definitely think that would cause a huge improvement — still do it in the same session, but it needs to be incorporated for much better results. I'd rather fix things in the small island of a work tree than three days later in staging when something's broke again.

[00:44:05] Patrick Chouinard: ▶ That way you can have a harness with the specific tools and skills for debugging, analysis, and security analysis at every step within your process — equipped to be a specialist in debugging, not a specialist in coding.

[00:44:26] Brandon Hancock: Awesome idea, Patrick. If you have time tomorrow evening or Thursday, would love to learn more. Hamal, you were next up — what's going on, buddy?

<!--SEGMENT
topic: E-commerce AI copilot architecture
speakers: Hemal Shah, Brandon Hancock
keywords: AI co-pilot, e-commerce, orchestrator, sub-agent, planner-executor, intent routing, knowledge base, product search, purchase actions, architecture
summary: Hemal Shah describes an AI co-pilot for an e-commerce site that can answer from a knowledge base, search products, and execute purchases. He asks Brandon whether to use an orchestrator-with-sub-agents design or a planner-executor architecture. Brandon endorses starting with the orchestrator pattern but frames the decision as something to be tested empirically rather than chosen up front.
-->

[00:44:44] Hemal Shah: Hello, I'm working on this one project for my company, kind of an AI co-pilot for the site, e-commerce site, where you can, besides answering from knowledge base, you can buy products and literally, you can do everything that you can [00:45:00] do typically from traditional website. My question — I asked this question last time as well, I'm continuing working on it — I wanted to pick your brain, Brandon, in terms of two things: architectural style and any technology implementation. <Q>Architecturally, because there are multiple capabilities — not just Q&A from knowledge base, there are actions: you can buy product and you can search for products and things like that. I was wondering if having an orchestration agent and then having a sub-agent per capability and handing over to the respective sub-agent based on the intent was one way; the other way was a planner-and-executor style architecture where everything is tied together. What are your thoughts on architectural style for this?</Q>

[00:45:53] Brandon Hancock: So I love this, and I'm going to answer this exactly how I would work on it if I was you. What you're suggesting, they're all awesome ideas. ▶ I do think probably the orchestrator sub-agent [concept:orchestrator-with-sub-agents] would probably be what would end up happening, but here's actually how I would test this.

---

<!--SEGMENT
topic: Adversarial eval sets and loop engineering
speakers: Brandon Hancock, Hemal Shah
keywords: adversarial conversations, evaluation set, forward/reverse propagation, prompt injection, black box testing, loop engineering, feedback loops, cost function, experiment log, markdown journaling, Karpathy auto-loop
summary: Brandon lays out his testing methodology: generate 100+ adversarial test conversations bucketed by user type (crystal-clear, confused, prompt-injection), lock them in as an evaluation set with expected outcomes, then run an automated experiment loop — start with one agent with many tools, measure failures, iterate architecture, and let the AI run the optimize-test-hypothesize loop overnight while journaling every experiment to markdown files so progress survives context compaction.
-->

[00:46:11] Brandon Hancock: What I would do is — and I do this literally every day when we're building up new capabilities — step one is I ask AI, because at the end of the day you're having conversations. The user has a question, they might be a little confusing, they're trying to get to an intent, and then they might have follow-up stuff. ▶ In your case, I would say: I want you to come up with at least a hundred adversarial conversations to stress test the system.

In machine learning, there's a concept of forward and reverse propagation — this is literally what we're going to do to your system. Some inputs: the user is the best user online — "I would like to buy the product with this SKU number at a quantity of two" — easiest request ever. Then others: "Could you tell me about this product and this product and this product? Fantastic. I want to buy the first one." — where it's not hyper clear. And some people are just going to try prompt injection [concept:prompt-injection]. ▶ So you need to say: hey AI, come up with buckets — bucket one is crystal-clear, then confused Carl — come up with as many adversarial inputs as possible.

Step two, lock that in, save it. ▶ That becomes your evaluation set [concept:evaluation-set]: here's the input and here's the expected theoretical outcome. It's a science experiment from there. It's kind of like the Karpathy auto-loop, but instead of researching, we are creating a black box that just happens to be your agentic layer.

Start off with the most simple version possible: one agent with a ton of tools. Is it going to work? Most likely not. Throw it all through and see what failed. "Hmm, that didn't work — but I now know it failed 60% of the time. Why? Theoretically it was supposed to buy the item, but in reality it called the wrong tool, emailed a person." So now I know this exact system had these issues. Then: let's try the orchestration layer — an orchestrator and two sub-agents, the buy agent, the Q&A agent. Then try again. I just go forward, get results, and say "hey AI, go back and use your best judgment to fix this."

I've had this loop run for 12 hours before — I'm not kidding, it costs quite a bit of money, but it got us — like in machine learning, you'll see your cost function drop precipitously as it achieves higher and higher results. You just literally do it on an auto loop: propose what to fix, run it through, analyze the results, come up with a new hypothesis, implement the change, test it again. ▶ This is loop engineering [concept:loop-engineering] — feedback loops to get to the desired outcome, and you let the AI have total control over it.

[00:52:06] Hemal Shah: A couple of follow-up questions. <Q>Running on loop — loop engineering — my understanding is you just craft your prompt so it keeps going until it meets the criteria, correct?</Q>
[00:52:19] Brandon Hancock: <A>Exactly. And you're just going to say, hey, we're going to do this loop together three times just so you can see it. Then: you solve the whole process end to end. Make sure you save this as a plan because you're going to get compressed or compacted — you need to be able to look at a log of all your previous experiments. ▶ Every experiment should get saved to a markdown file so it can review what it's done in the past, like a good scientist would — I don't want to go back and try option two if I've already tried it. Journal it out, so if it gets compacted it can go back and check.</A> Run it three times with your help, then after three times you can let that bad boy rip for the rest of the night: "I'll go to bed, don't come back to me until this is done." I literally do that quite often.

---

<!--SEGMENT
topic: Model selection and cost strategy
speakers: Brandon Hancock, Hemal Shah
keywords: Chinese models, GPT-5.5, Gemini 3.5, Gemini 3.6, Gemini 3.7, cost discount, classification, thinking model, Opus 5, responder model, speed, experiment cost
summary: Brandon recommends using cheap Chinese models for overnight experimentation loops (his run cost ~$400 overnight), reserving GPT-5.5 without thinking for complex production tasks and classification, and Gemini 3.6 for quick small tasks due to a 50% cost discount and speed. For Hemal's American-model constraint: a slow thinking model for the orchestrating agent plus the cheapest fast responder (Gemini 3.6 Flash or GPT-5.5 no-thinking).
-->

[00:50:00] Brandon Hancock: ▶ If you have a chance to use the Chinese models [concept:Chinese-models], use them — at least to experiment to start, especially if it's all fake data. I've run it before and it cost me like 400 bucks overnight; I thought I was going to spend 30 bucks before I went to bed, I was not ready for that bill when I woke up. Then later you can throw in GPT-5.5 [tool:GPT-5.5] — that's what we use internally for actual complex big tasks, ton of rules, hyper-specific on how we talk to the user. No thinking — it's the fastest affordable American model. For classification and quick smaller stuff, we're currently using Gemini 3.5/3.6 [tool:Gemini-3.6]. 3.6 and 3.7 have a 50% cost discount right now — I ran an experiment before this call; we're switching from 3.5 to 3.6 because of cost and speed. I'd love to use 3.7 for our use case, but it was five times slower, so we just can't use it.

[00:55:39] Hemal Shah: <Q>If I want to use American models for this research, any recommendation? Opus 5 is giving a lot of problems. I have both GPT 5.6 and Opus 5 subscriptions.</Q>
[00:55:57] Brandon Hancock: <A>For the agent who's running this, I'd use a slower thinking model since you're going to bed. But the actual model that's responding — use the cheapest one you can. If it has to be American: Gemini 3.6 Flash [tool:Gemini-3.6-Flash] for the responder navigating the chat, or GPT-5.5 no-thinking. Those would be the two.</A>

---

<!--SEGMENT
topic: Router vs multi-agent orchestration
speakers: Brandon Hancock, Hemal Shah
keywords: agentic framework, sequential LLM calls, classifier, router, one-to-many-to-one orchestration, parallel agents, intent overlap, seed ideas, terminology, agent definition, tool calls
summary: Hemal asks whether to steer the auto-loop toward a specific agentic framework. Brandon says the system is really sequential LLM calls, not true agents; the adversarial tests will reveal whether a pure router suffices or whether a one-to-many-to-one pattern (triggering multiple agents in parallel, merging results) is needed. He also clarifies terminology: an LLM with a tool call is still just an LLM — an agent reasons and acts in a loop, which this system does not do.
-->

[00:53:27] Hemal Shah: <Q>Once we run it, it will implement it and pick its own frameworks. Do we need to guide it toward any agentic framework over another?</Q>
[00:53:37] Brandon Hancock: <A>You have to pick the lab out of the gate. At the end of the day, nothing about this is truly agentic — it's a bunch of sequential LLM calls. There's nothing stopping you from having step one be a categorization step that buckets it, then it goes to the responding parties. That's what your adversarial stuff is going to test: what happens when there's an overlap between sales and Q&A? You might not want a pure router that calls only one of five things — you might want to call two or three, trigger three different agents to respond, pipe those results into the final agent that responds to the user. It just depends how complex it is. With how smart 5.5 is, the prompts we pass in are monsters — you might just need 5.5 and eat the bill with one agent. I'd pass in this conversation as seed ideas: start with one, branch out, try edge cases, try the one-to-many-back-to-one [concept:one-to-many-to-one orchestration]. Give it seed ideas but let it experiment and log whether it did better or worse.</A>

[01:02:06] Hemal Shah: <Q>What you mentioned is LLM calls versus agents — there could be a RAG-type capability as well, right, if it's question-answer. So you still think there's no agentic part in it, just plain LLM calls?</Q>
[01:02:23] Brandon Hancock: <A>Yeah — to be hyper-clear on terminology: an LLM with a tool call, in my head, is still just an LLM. An agent is something that takes in an input, reasons, and takes action in a loop. We're not doing that. We're piping a conversation in and spitting out an answer as quick as possible — it's not going to rip for 30 minutes by itself; it's going to stream out text as fast as possible. ▶ It's a series of LLM calls, some in parallel, some in sequence, to generate an answer for the user.</A>

---

<!--SEGMENT
topic: Observability via data web app
speakers: Juan Torres, Hemal Shah
keywords: observability, data web application, Flask, Docker, containerized, JSON blob, test client, sequential agents, debug mode, entity recognition, reasoning output, non-deterministic systems, start.sh
summary: Juan recommends building a simple containerized Flask data web application for observability of non-deterministic agentic systems: register each test inquiry under a "test client," log each sequential agent's input/output as JSON rows, and include a debug mode that surfaces the LLM's reasoning (extra tokens dropped in production). This gives sustainable, visual inspection of each transformation, which he has used for named-entity recognition and diffusion model work.
-->

[00:56:34] Juan Torres: <Q>Suggestion: I believe you should create a simple data web application in which every test inquiry you make can be registered — a dev test client — and register the level of categorization as a JSON blob.</Q> With non-deterministic systems, having a simple data web application that lets you see each performance has helped me in named-entity recognition problems and even in diffusion models — being able to observe each transaction, each transformation. ▶ If you're serious about systematizing this and having sustainable improvement on your agentic system, invest in this: create a containerized image [tool:Docker], activate it whenever you go into DevOps/testing mode, and the front end maintains itself completely separately. You don't even have to create another database — just have the data web application connect to the same database and create a client called "test client," and carry out the stress test.

[00:58:46] Hemal Shah: <Q>Juan, do you mean the web application will visualize all the question and answer, or will it kind of test hardness?</Q>
[00:58:53] Juan Torres: <A>Depending on the categories — say the nine severe attack types — each row registers an input, and then, if you have a truly sequential agentic system, each row sequentially shows output one from agent one, agent two, agent three — because one feeds the output of the other. You want to actually see the output of the first agent feed into the second and third.</A> You can create a development/debug mode where sometimes you want the agents to have a purification of outputs — outputs that don't necessarily work in production. For example, in the NER problems I face with the accounting firm I'm working with, debug mode outputs not only the extracted entity but the reasoning behind it. ▶ Those are extra tokens you don't want to expend once you productionalize, but you may want that extra observability — the LLM's reasoning — during development. That's why I'm a big fan of adding observability through a Flask [tool:Flask] data web application: containerize a Docker image, create a shell command like `start.sh webapp` and it starts your webapp, or `start.sh old systems` and it starts the app plus the data web application. That's how I maintain observability on non-deterministic systems.

[01:01:31] Brandon Hancock: Please let us know what ends up working — I'm very curious. My guess: if you have to generate an answer within seconds, it'll be a classifier then one of three. If you can wait 10+ seconds, it'll probably be the 1-3-1 or 1-5-1 pattern. Please draw a little doodle and let us know what happens.

---

<!--SEGMENT
topic: Startup finances and cloud vendor pain
speakers: Paul Miller, Brandon Hancock, Ty Wells
keywords: Google startup fund, AWS credits, Claude on AWS, rate limits, timeout jail, Chinese models, fundraising, tiny seed, salary, bootstrapping, OpenAI, Google
summary: Paul asks whether Brandon leverages Google startup fund credits. Brandon explains credit tiers tied to fundraising, and vents about how fickle Claude on AWS is — rate limits, a month-long "timeout jail" he had to pay to escape, and quota caps that break his thousand-test evaluation runs. He shares candidly about his startup's finances: no salary for months, tiny salaries since, fundraising in progress, and excitement for Chinese models to escape Claude/AWS friction.
-->

[01:03:05] Paul Miller: Given your exposure to Google costs, <Q>are you leveraging the Google startup fund access?</Q>
[01:03:26] Brandon Hancock: <A>Yeah — whenever we did our tiny seed fund, we got access to some credits. Unfortunately they had buckets: how much you raise is how much credit you get, and tiny seed money isn't a stupid amount. As soon as we raise the next round, I'll hit them back up. We got AWS credits and Google credits.</A> Quick ticker, guys: AWS, specifically Claude [tool:Claude-on-AWS], is so fickle. I have struggled to build anything using the Claude models in AWS. I accidentally got put in AWS timeout for literally a month — I had to pay $50–100 to get my tickets reviewed faster to finally get it resolved. I had to pay money to get out of jail. And what I'm allotted for calling models — I needed a Haiku model for speed — if I go over, which I do when testing (like the thousand tests I proposed to Hemal), we go to jail again. It's a fallback of a fallback; it's scary. ▶ I'm very excited for the Chinese models to come out and get off of anything Claude, because it's so hard to use their stuff. OpenAI, Google — really no issues. Claude, pain in the butt.

[01:05:12] Brandon Hancock: I'll just be transparent about what's happening: at the beginning of the year I went all in — didn't take a salary for a couple months, then we started taking $2,000 each. I had a really big gig at the beginning of the year that paid for the year, very fortunate, but it's been nine months. What keeps me up at night is: how do I get my next dollar? If this fundraising comes in, I'll actually be able to take an engineering salary. Sales cycles take forever even though the product's built — we need something to happen. Funny thing: at Dunkin', the tip screen — guys, I made zero dollars last month, this coffee should be free, the Dunkin' employee is making more than I am.
[01:07:00] Ty Wells: And ask for a tip.
[01:07:03] Brandon Hancock: Seriously. I will work for tokens. Fingers crossed, big things happen on the other side of this — this is my swing for the fences, and it is not for the faint of heart.

---

<!--SEGMENT
topic: VC partnership, enterprise moats, defensibility
speakers: Paul Miller, Brandon Hancock
keywords: VC setup, AI dev studio, SaaS, enterprise development, due diligence, defensibility, rapid pilot copy, biometric authentication, logistics app, driver impersonation, judgment at scale, domain expertise, Rich Dad Poor Dad
summary: Paul describes wrapping up a contracted logistics-industry product delivery where funders want to convert the relationship into a VC-style AI dev studio. He shares a hard-won lesson: drivers impersonating other drivers to work illegal long shifts, solved with biometric authentication against driver's license tokens (out-of-scope, billable work). Brandon connects this to moats: weekend rapid pilots can copy apps during due diligence, so defensibility comes from expert judgment at scale — extracting a thousand edge cases from field experts — plus enterprise/legal complexity.
-->

[01:07:32] Paul Miller: I've gone through exactly what you went through — I'm in my 11th year of that business, paying myself nothing, accruing huge mortgage repayments, putting my wife through stress. Now we've got a business that generates really good revenue, and this new project is about to go live in the next month. It's a contracted delivery of a product, and now the funders — who are well-funded — want to turn the relationship with me into more of a VC setup: a modern AI dev studio where the VC funding includes covering my time, and over time I put cash back into the partnership, looking for capital gain more than income. This investor has a lot to invest out of Australia. The question we're wrestling with: if you're doing enterprise SaaS apps, what are all the VC funds doing? How are people building apps differently? ▶ The cost of dev has come right down, but realistically the cost of enterprise dev hasn't — you don't build an enterprise app in two weeks, and then there's onboarding and everything else.

Example: it's a logistics industry app, and we had drivers pretending to be other drivers to do different jobs so they could do really long shifts — 19 hours in a row, a breach of law, legal risk and liability if they have an accident. So we added biometric testing and authentication [concept:biometric-authentication]: the system throws a biometric challenge back to the driver before logging and assigning the next job, verified against their driver's license token.
[01:11:00] Brandon Hancock: That's crazy — you would not have guessed that problem going in. Hopefully a few extra dollars were charged for all of that.
[01:11:08] Paul Miller: Oh yeah, all that's out-of-scope stuff — we've got to build that, define that. The money's been good, the lessons have been good, and I haven't had the stress of funding it myself. It's important to set myself up with the reality of doing software in 2026, because your whole moat proposition is different and what VC firms expect is different. Part of due diligence research: someone will look at your app and run a rapid pilot over a weekend copying your whole app, then ask how defensible it is — is it worth spending all these millions to go ahead?

[01:12:20] Brandon Hancock: What Paul is saying is so true — there's an actual study on the five levels of this. Anytime your app could just be ripped like Paul said — what I'm doing with the Listio app: I want this plus this plus this, and I'm going to rip it; I know it's a quick cash play, can I make 5–10k for a couple months. But if you're building a multi-year play, this is what we're doing with EMSO: it takes a software engineer plus someone who's been in the field who has to give their particular judgment on a thousand edge cases, because AI can't do that. You can't just say "do what an EMS chief would do" — what does that mean across 500 different situations? ▶ You have to extract all the use cases from an expert in the field to get the moat, because you can't automate that away — judgment at scale with AI is not going anywhere for a long time. Same with enterprise: legal and compliance add so much complexity. Going back to Rich Dad Poor Dad — you win no matter what: they take the shot, you take the paycheck, like an investment banker who gets paid fees whether the trade makes or loses 100k. Paul, please scale the heck out of that.

---

<!--SEGMENT
topic: Agentic reporting stack with LanceDB
speakers: Paul Miller, Brandon Hancock, Daniel Zivkovic
keywords: CRM, sales force automation, merchandising, agentic reporting, ground truth, SQL, LanceDB, DuckDB, columnar, classification, RunPod, GPU, Cerebras, Qwen, GLM, Postgres, 11 years of data
summary: Paul explains how he converted his CRM company's traditional dashboard reporting into an agentic-aware system: ground truth stays in SQL tables, while word-based conversation data is classified into pure metrics via LanceDB-stored JSON. He ran 11 years of data through GPU-powered RunPod servers to extract per-role insights, then built a query stack on LanceDB + DuckDB (columnar, file-based, pre-modeled per metric category from Postgres master data) with a Cerebras-hosted Qwen model front end for fast grounded chat. Nine models are used across the system.
-->

[01:15:00] Paul Miller: For my existing business — a CRM-type company for sales force automation, selling tools to people who do merchandising at retail stores — we've got 11 years of market data and extensive industry knowledge. We've been taking our traditional dashboard-style drill-down reports and converting them to being fully agentic-aware. ▶ Agentic-aware means ground truth always sits in the SQL tables, but for word-based content we built modeling and classification so we could build ground truth based on the words: using LanceDB [tool:LanceDB] to pull all the word content into JSONs, classifying every conversation so it has a pure metric — "this conversation was a positive sales outcome" — queryable in a way where there can never be any misunderstanding in how the AI translates it.

Then I ran up a few RunPod [tool:RunPod] servers with a lot of GPU capability, threw 11 years of data and insights into it, and got the models to churn through it: for every area of the business, what does good look like? If you had a magic wand and could drill through an organization at every level, what would you tell senior leadership or participants at each level that they'd have loved to know before they went into a situation? My God, the reporting is amazing.

The whole stack sits in a combination of LanceDB and DuckDB [tool:DuckDB] so it can compact the data and respond really quickly for queries — it doesn't always have to go into an LLM, it always refers to that. And I've put a front end with Cerebras [tool:Cerebras] so you can chat with that content really fast and it knows what you're talking about without going back through an AI — and it's always grounded.

[01:18:03] Brandon Hancock: A few quick questions — when it comes to DuckDB, is it a vector store? <Q>Are you using two different vector stores, basically?</Q>
[01:18:17] Daniel Zivkovic: <A>No, it's on top of it. You can treat it like a big database.</A>
[01:18:17] Paul Miller: <A>Yeah, it's columnar — a file-based columnar search database. You put a lot of data in very specific stacks; instead of huge tables, you pre-build data in a format that can be really quickly searched.</A> Everything's originally in a Postgres [tool:Postgres] database because that's where all the master data comes from; then it pulls it into a format optimized for queries and building AI recommendations. There are about eight categories of metrics, and for each category the data needs to be modeled slightly differently to answer questions relating to that metric. Some people want to know: I'm going into my work day — what do I need to know from what I did last time with that customer? Or I manage a team — tell me what I should know about how those people did this week, how I can motivate them. Or I'm a third party — what do I need to know, how is it vetted, and how does it compare with every other participant?

[01:20:03] Brandon Hancock: Were you saying Cerebras? Cerebras AI?
[01:20:10] Paul Miller: Yes — Cerebras is kind of like Groq: really fast hosted models. I've got some of the Chinese models. If you want to do a really quick query at 2,000 transactions per second, you can scale that up and run really quick results.
[01:20:38] Brandon Hancock: <Q>Which model specifically — are you a GLM guy, a Qwen guy?</Q>
[01:20:45] Paul Miller: <A>I think I'm using a Qwen [tool:Qwen] model for that — I can't specifically remember, but I've got about nine models used in this system at the moment, as well as running up models in RunPod for the back data. Then it's really just the iterative change each night with what happens in the reporting.</A>
[01:21:07] Brandon Hancock: That's very cool, Paul. Please keep us posted, good luck on the upcoming launch — and if I can ever help out with anything, let me know. It sounds like you're getting yourself in a great spot after a lot of hard work and decades in the field — all rightfully earned.

---

<!--SEGMENT
topic: AI Boot Studio promo and go-to-market
speakers: Juan Torres, Brandon Hancock, Shakur
keywords: AI Boot Studio, DaVinci Resolve, promo video, AI-generated images, event photo booth, San Diego, country club, ICP, wedding venues, convention centers, Instantly, email warmup, cold email campaign, Calendly, domain setup, sales engine
summary: Juan shares a DaVinci-edited promo video for AI Boot Studio, his AI photo booth now in its second field deployment, drawing rave reviews. Brandon calls it a 10/10 app, hardware, and promo, then gives a concrete go-to-market plan: buy 3–5 domains and warm up emails for two weeks via Instantly, scrape 1,000 contacts per ICP (wedding venues, convention centers), run three-email campaigns per ICP leading to Calendly, and build a waitlist so the sales engine runs in parallel with hardware scaling. Juan notes a country-club lead three hours away in India, motivating hardware-deployment contracts.
-->

[01:21:44] Juan Torres: Can I share my screen? This is a video I'm creating in DaVinci [tool:DaVinci-Resolve] for one of the last events where I placed the AI Boot Studio [tool:AI-Boot-Studio]. This is my second time putting it into the field.
[01:22:58] Brandon Hancock: Holy — this is probably the coolest thing I've ever seen. Easily one of the coolest promo videos — I'm like, I want to go do this right now. Please send me this video. Two things: dude, this is going to go so well, I'm so pumped. From a video perspective: it's instant dopamine, then once people are like "this is crazy," you show what it really looks like. That could not have been done any better — 10 out of 10 app, 10 out of 10 hardware, 10 out of 10 promo.
[01:25:55] Shakur: Is it in the U.S. yet?
[01:25:57] Juan Torres: It's in San Diego. I need to carry a campaign to systematize having clients. For this event, an operations manager for a country club said he wants to talk to his boss about having it at the country club because in September we're going to have a lot of events. The problem is the country club is in India, three hours away from San Diego. ▶ Having the hardware deployed at the place and left there, under a contract where both of us make money, would be more efficient — going back and forth is a lot of time.

[01:27:00] Brandon Hancock: Juan, you are in the world's best spot for this: you have a sick promo, you have social proof. The next immediate bottleneck is how do we get you in contact with a hundred different agencies to figure out who's ready to go now? ▶ Immediately after this call: buy three to five domains and set up Instantly [tool:Instantly], because you have to spend two to two-and-a-half weeks warming up your email list. That lets you spend two weeks figuring out an email campaign per ICP. An ICP for you would be a wedding venue, a convention center — scrape for five different ICP types, build an email list of a thousand with all their contact information, and when two weeks pass, send a campaign per ICP: "here's what I have, here's what it looks like, we've had awesome results, here's my Calendly [tool:Calendly]." You might not even put them on a call — put them on a waitlist, because you might just need the initial 10. But at least get on calls with a hundred customers, even if they go in a queue, to gauge interest — so when you're ready to launch with 10 more devices, you're not making the mistake I made: having it ready and only then starting the month-long warmup. Today, your sales engine runs in parallel. Three emails: initial, follow-up, final follow-up, all leading to your Calendly. Three weeks from now you'll know who your next 100 customers are.
[01:30:00] Juan Torres: Do you have literature or channels — the magnum opus work on this campaign, this email campaign?

---

<!--SEGMENT
topic: AI-driven ICP list building
speakers: Juan Torres, Brandon Hancock
keywords: ICP, Grok 4, Claude, convention centers, wedding venues, San Diego, Appify, lead scraping, sub-agent, EMSOAP, Listio, rulebook
summary: Juan asks how to systematize building a database of country clubs and venues as ICPs and run outreach campaigns. Brandon brain-dumps his exact process: use Grok to find 10–20 venues locally, inject human judgment on bad fits, repeat across cities 3–5 times, then scale the refined query with AI review and scraping tools.
-->
[01:30:14] Juan Torres: Because I can see myself actually, and that was one of the things that I have in my board is to develop a database of country clubs, venues, other social gathering places, right? But, you know, then how to, once I systematize the identification of that 1,000 ICPs, then what is the methodology to carry out this campaign? <Q>What is the methodology to carry out this campaign?</Q>
[01:30:47] Brandon Hancock: ▶ Step one: use Grok [tool:Grok] (he says "Brock/Grok 4") because it's fast. Tell it exactly the type of customer you want (e.g., convention centers, wedding venues in San Diego), have it find 10–20 locally.
[01:31:33] Brandon Hancock: Then apply judgment: articulate why each bad choice is bad, feed that back so the model understands what to look for. Repeat in different cities 3–5 times until it understands your ICP and what info to gather.
[01:32:25] Brandon Hancock: Then scale: search query = "state, city, wedding venue" / "state, city, convention center," let AI review the results once you've judged 50–60 manually. ▶ Figure out tooling needs (Appify [tool:Apify], scraping sub-agents for contacts) by manually assisting the AI first; codify everything into a rulebook, then scale like crazy.
[01:33:35] Brandon Hancock: ▶ In parallel: buy AI Booth [tool:AIBooth] burner domains (3–5), set up Instantly [tool:Instantly] for cold outreach — takes ~2 weeks to spin up domains, DNS records, five email accounts. Never use your primary domain for cold outreach; you'll burn it. ~$8/account/month.
[01:35:00] Brandon Hancock: ▶ Cold email best practice: short, readable on one screen, one call to action, point to Calendly [tool:Calendly] or email. Referenced Instantly's YouTube training as "our bible for cold outreach." [link:Instantly YouTube channel / cold outreach training shared in chat]
[01:35:41] Brandon Hancock: This is the exact approach for EMSOAP and what he'll do for Listio — "the easiest way to get your next 100 customers."

<!--SEGMENT
topic: Landing page and immediate assets
speakers: Juan Torres, Brandon Hancock
keywords: landing page, Claude Design, Vercel, Calendly, business cards, Pod design, Jack Roberts, call to action
summary: Juan notes he has warm interest from a San Diego event organizer and a country club owner but lacks business cards and a landing page. Brandon lays out a one-day stack: buy a domain, build the page with Claude Design, single CTA to Calendly, deploy on Vercel.
-->
[01:36:17] Juan Torres: An organizer for high-end San Diego events was impressed by the product; a country club owner/ops manager too. People asked for business cards — he has none yet, and no landing page.
[01:36:50] Brandon Hancock: ▶ Use Claude Design [tool:Claude] for the landing page — "you'll literally have it up in an hour." Keep it as simple as possible with one call to action (talk to you / reserve — they can't buy yet). Point to Calendly. Deploy in a day with Vercel [tool:Vercel]. Jack Roberts [person:Jack Roberts] has a good video on this. The existing demo video can be the marketing asset on the page. ▶ "You did all the hard stuff; the rest is small tasks."

<!--SEGMENT
topic: GrokBot agents and lean tech
speakers: Paul Miller, Brandon Hancock
keywords: GrokBot, LinkedIn connector, serpapi.com, Google Places, agents, marketing team, total addressable market, Australia, New Zealand
summary: Paul recommends not over-building tech and instead delegating to GrokBot agents as a "marketing team" — watching inbound emails, building funnels, pulling LinkedIn data via its native connector at no extra cost. He suggests serpapi.com for Google Places data to build venue lists, tying back to presenting TAM to VCs.
-->
[01:37:57] Paul Miller: ▶ Be lean with tech; invest in more hardware/display units so you can do parallel shows. His "hot shiny thing" this week: GrokBot [tool:GrokBot] — great UI; set up agent "people" you control to manage your time. Build a little marketing team: one agent watching inbound campaign emails.
[01:40:27] Paul Miller: Had GrokBot build a whole new funnel for Australia/New Zealand over a weekend; default LinkedIn connector authenticates and pulls data at no extra cost. For Google Places data (wedding venues, golf clubs) he uses serpapi.com [tool:serpapi] [link:serpapi.com]. ▶ Give it to a GrokBot tool: "build a list of 50 potential venues." Ties into total addressable market story for VC conversations — five units, flexible format, contractor for manufacturing.

<!--SEGMENT
topic: Pre-seed fundraising and C-Corp setup
speakers: Brandon Hancock, Paul Miller, Juan Torres, Shakur
keywords: TinySeed, YC, pre-seed, C-Corp, S-Corp, Delaware, Clerky, cap table, capital bottleneck, Shakur, funding deadline
summary: Brandon identifies capital as the predictable bottleneck (units cost ~$400–800 + labor; 100 units ≈ $100k). He urges opening fundraising doors now: TinySeed (batch deadline ~8 days away, ~$130k for solo founders) and YC (~$150k+, funds in January). Requires converting to a C-Corp in Delaware via Clerky. Paul clarifies the VC-prep framing; Shakur endorses the action plan.
-->
[01:43:42] Brandon Hancock: ▶ Capital will be a bottleneck within six months — machines cost roughly $400–800 in materials plus labor; scaling to 100 venues ≈ $100k. Options: TinySeed [tool:TinySeed] (next batch Sept 1–9, ~$130k for solo founders) or YC [tool:Y Combinator] (~$150k+, but funds not until January). Open as many doors now as possible.
[01:45:57] Brandon Hancock: ▶ Use Grok or Claude to research: "find me a list of 30 pre-seed funds, figure out when everything's due, start applications on my behalf." TinySeed deadline is ~8 days out. Paul offers to share his own fundraising experience offline.
[01:46:41] Juan Torres: Asks why VCs would fund without shareholding — Paul clarifies he meant the VC prep work: clarifying TAM, differentiation, scaling plan, costs, contractors, path to 100–1,000 units, patents. All pre-done so the VC pitch is easy.
[01:48:52] Brandon Hancock: ▶ Absolute must for the VC route: create a C-Corp. Use Clerky [tool:Clerky] (~$800–1,000). Juan has an S-Corp — heads up: most funds require a C-Corp, ideally Delaware, for stock management. Clerky handles ownership agreement, cap table, end-to-end setup in a weekend or two.
[01:50:11] Shakur: 100 units for $100k could pay back in ~2 months (a few hundred bucks per event, multiple events per weekend). ▶ Actions for next week: set up Instantly, set up a C-Corp, apply for investments — "set yourself up for success over the next year, not just the next month."

<!--SEGMENT
topic: Referrals and customer pre-funding
speakers: Shakur, Brandon Hancock
keywords: referral program, warm intro, deposits, pre-sales, affiliates, wedding coordinators, $100M Leads, ROI, self-funding
summary: Shakur suggests a referral program (e.g., $50 or a voucher for warm intros). Brandon flips it into a pre-sale strategy: offer the first 100 venues a deposit-based spot in line (~$1,000) to self-fund manufacturing. He also recommends affiliate/referral splits (20–30% of profits for six months), especially via wedding coordinators, referencing the $100M Leads playbook.
-->
[01:51:13] Shakur: <Q>Have you looked at a referral program?</Q> ▶ Venues already talking about you go to conferences and peer companies — offer $50 or a voucher for finding another customer; it's a great way to get a warm intro.
[01:52:11] Brandon Hancock: ▶ Alternative to outside investment: offer the first 100 venues a deal — put down a deposit (unit cost plus cushion) to be first in line when their unit is ready. Warm-intro venues may take it; this self-funds growth and cuts out extra work.
[01:53:28] Brandon Hancock: ▶ On the call itself: "If you want to jump to the head of the line, send a $1,000 check now to be the first customer, then we do a profit split." Clear ROI — you help them make more money. Social proof compounds: once venues show $12k–$30k/year gains, adoption gets easy.
[01:54:28] Brandon Hancock: References the $100M Leads book [tool:$100M Leads]: hyper-scalable cold outreach plus affiliates/referrals — 20–30% of profits for the first six months; wedding coordinators are the best referrers since they talk to 30 different venues.

<!--SEGMENT
topic: Wrap-up and handoff
speakers: Juan Torres, Brandon Hancock, Scott Rippey
keywords: OnlyFans joke, video request, wedding venue friend, installment support, call order, Ryan, Scott
summary: Light wrap-up of Juan's segment: jokes about fundraising, a request for the product demo video to share with a friend who owns a wedding venue, and an offer to help with installation locally. The call moves to the next agenda item — Ryan (asleep) then Scott.
-->
[01:56:10] Juan Torres: Jokes about opening an OnlyFans to fund hardware; Brandon: "founder mood."
[01:56:33] Scott: Please send the demo video [link:product demo video] — his friend owns a wedding venue and had many questions. Scott lives two minutes from a venue and offers to be an installment contact. Thank-yous exchanged.
[01:57:13] Scott: Next on the call order: Ryan, then Scott. Ryan appears to be asleep ("normally it's midnight for him").

<!--SEGMENT
topic: Agent observability dashboard update
speakers: Scott Rippey
keywords: CC security engine, Codex Sol, dashboard, observability, Claude Code, Opus, Sonnet, multi-repo agents, API spend, global CLAUDE.md rules, guardrails
summary: Scott shares updates on his multi-engine agent security system (previously demoed): he added observability so he can watch agents running across multiple repos from a dashboard, which lets him grant more autonomy. He spent ~$2k equivalent in API spend last month and now trusts the system (Opus, Sonnet, Sol running adversarial checks) guided by global CLAUDE.md rules and guardrails.
-->
[01:57:38] Scott Rippey: Recaps last week's CC security engine and dashboard, including the Codex Sol [tool:Codex Sol] fourth engine used at onboarding. New: observability — a recorded video shows agents running across multiple different repos, visible in the dashboard [link:screen-shared video of agent dashboard]. No more asking "is it done yet" in Claude Code [tool:Claude Code].
[01:59:02] Scott Rippey: Captures a ton of data; ~$2k/month equivalent spend (under a plan) — valuable if he ever switches providers.
[01:59:15] Scott Rippey: With global CLAUDE.md rules and guardrails, he lets rounds run autonomously until fixed, flagging decisions — multiple models (Opus, Sonnet 5.5, Sol) with adversarial checks. ▶ Trust comes from observability: logs are reviewable at any point. Hasn't figured out how to productize it yet.

<!--SEGMENT
topic: HYROX training SaaS partnership
speakers: Scott Rippey, Brandon Hancock
keywords: HYROX, Acceler8 Training, 8th Day Gym, Michigan, world champion coach, periodization, CLAUDE.md, ghostwriter, Dickey Bush, Nicolas Cole, Instagram, partnership agreement, equity split, SaaS
summary: Scott is building a HYROX programming SaaS with a Michigan gym owner (world-champion coach) and a champion athlete as the face. He describes the domain/knowledge-extraction plan (coach brain-dumps into Claude Desktop to produce an MD file), the revenue model (cover costs, split three ways), and his plan to embed at the gym for 2–3 weeks in September. Brandon probes business model limits and warns to formalize deliverables in a partnership agreement; recommends a ghostwriter (~$4–5k/month) for the athlete's Instagram.
-->
[02:00:35] Scott Rippey: Skeletoned an application/initial template for a HYROX [tool:HYROX] programming app. Partner gym in Michigan: multiple levels, world champion coach ("Joe"), plus the current HYROX women's champion as the face. Domain bought: Acceler8 Training [link:Acceler8 Training], playing off the 8th Day Gym branding.
[02:01:42] Scott Rippey: HYROX is predictable (same race/movements every time, unlike CrossFit) — ideal for codification. Coach has an MD file built from the backend; 4–6 hierarchical frameworks planned. Coach will brain-dump into Claude Desktop [tool:Claude Desktop] to produce the knowledge file, informing V1 periodization logic; athlete onboarding collects metrics and shapes weekly programming. Scott will stay with in-laws 2–3 weeks from mid-September, train at the gym mornings, build all day, and test on Joe's athletes.
[02:03:11] Brandon Hancock: "Magic dream team" — expert + social proof + builder. <Q>What's the business model at the limit? Who's splitting the money?</Q> Athlete has 37k Instagram followers; 1,000 subscribers at $40 ≈ $40k/month, half a million a year.
[02:04:22] Scott Rippey: Cover operating costs first, then split three ways evenly — cool with it given Joe's methodology and her marketing reach.
[02:04:44] Brandon Hancock: ▶ Steal from Dickey Bush and Nicolas Cole: hire a ghostwriter (~$4–5k/month) to run the athlete's Instagram content on a schedule — she just sends pictures; distribution already exists. Nothing stops this becoming a half-million-dollar business in 12 months; the sport is growing and there's a regular (non-elite) division. (HYROX = 8 stations with 1km runs between, ~1 hour for elite athletes.)
[02:06:44] Brandon Hancock: ▶ Caution on the even split: as developer you'll put in the most work but they hold decade-built social leverage — nail down concrete deliverables and a partnership agreement ("you're basically getting married"). <Q>Are you on the hook forever, or is there a defined engagement?</Q>
[02:08:16] Scott Rippey: Final terms to be worked out in person; he's known Joe a long time and they'll formalize it. Long-term plan: monitor and support, building recurring income — deliberately waited for the right project rather than "sassing wide" anything.

<!--SEGMENT
topic: Builder-Distributor Partnership Trifecta
speakers: Scott Rippey, Brandon Hancock
keywords: distribution, partnership, audience growth, monetization, eyeballs, 37k followers, product builder, trifecta, Joe, creator economy
summary: Scott celebrates a three-way partnership structure where a creator with 37k followers builds audience while he builds the monetizing product and Joe acts as connector. He argues this solves the developer's biggest problem — distribution — and that the creator also needs to monetize her own work.
-->
[02:09:05] Scott Rippey: This checks a ton of boxes — I want everyone to hear this. <Q>What is the biggest issue that developers have?</Q> <A>Distribution.</A> The fact that you already hop in with someone who has 37k followers — do I wish she had 300k? Yes, but she just got this, so she's a growing asset in the space, and it will only get bigger. The more she can do while you're building this to grow from 37k to 50k to 100k, the better for everybody, and she needs to monetize her own work too.
▶ Y'all can win so easily doing this: she builds eyeballs, you build the product that monetizes it, and Joe is the in-between.
[02:09:54] Scott Rippey: We just keep tweaking, pulling from his brain — it's the perfect trifecta. I'm pretty excited and will keep you guys up to date.

<!--SEGMENT
topic: 3D Database Visualization Demo
speakers: Scott Rippey, Brandon Hancock
keywords: 3D database model, Tron-inspired fly-through, Fathom Design, table relationships, data flow, backend, metadata, React, Claude Code
summary: Scott demos a Tron-inspired 3D visualization of his database schema, built from a massive prompt describing the backend, taken into a design tool. Each cube represents a table with clickable relationship details. Brandon asks about live sync and the underlying library.
-->
[02:10:11] Scott Rippey: I created a 3D model of the database because I wanted to truly visualize it — Tron-inspired, you can do a fly-through, move, click on things, see relationships and which way data flows. I created this from the backend: took a massive prompt with how the backend was already built, took it into the design tool, then back in.
[02:10:49] Brandon Hancock: Does each one of the cubes represent a table? <A>Yes.</A> This is mapped out with relationship flows, and you can click and get the details over here.
[02:11:14] Scott Rippey: The one thing I don't have is live pulling — if I change something in the backend, I'll just have it update this manually. It's not pulling live.
[02:11:27] Scott Rippey: I love that because I understand databases, but visually it's just different — you can actually see it.
[02:13:50] Brandon Hancock: I'm more impressed about the data schema than the whole business. <Q>If you were to click on one of them, would the schema table come out?</Q> <A>It just has the metadata over here.</A> It'd be cool to have a table grid of some of the data you could filter.
[02:14:17] Brandon Hancock: <Q>What are you using for this, code-wise?</Q> <A>I think it's in React, if I remember right.</A> Scott will drop the library in the chat [link:3D database visualization library, promised in chat].

<!--SEGMENT
topic: Supabase Backups and Environments
speakers: Scott Rippey, Brandon Hancock, Juan Torres
keywords: Supabase, point-in-time recovery, production, staging, development, work trees, Git branches, dev database mirror, downtime, parallel features
summary: Scott confirms he's a heavy Supabase user and is urged to enable point-in-time recovery before real customers. The group discusses production/staging/development separation: Juan describes his Git-branch + mirrored dev Supabase database pipeline, which Scott endorses.
-->
[02:11:43] Brandon Hancock: <Q>Are you using Supabase?</Q> <A>Yeah, Supabase. I'm a heavy, heavy Supabase guy.</A>
[02:11:50] Scott Rippey: ▶ Please make sure you turn on point-in-time recovery whenever you start doing real-world stuff, so in the worst situation possible you have recoveries — you don't want to lose customers.
[02:12:17] Scott Rippey: Whenever it comes time to bring on your first customers, the ability to do production, staging, and development work trees will be the biggest game changer to help you keep moving fast when real-world customers come on. Happy to demo this later.
[02:12:35] Brandon Hancock: You're going to want to work on a bunch of small features in parallel, and you cannot afford downtime on production — especially in your case, you're going to have hopefully 1,000 concurrent users.
[02:12:56] Juan Torres: What I do is have a whole separate dev work tree locally on a branch in Git, hooked through Google, and a whole separate Supabase database that's a mirror. I completely test on dev, then merge to main. With the database, I'll then make that edit to prod after I know everything works on dev. I have a pipeline for that I've done multiple times.
[02:13:28] Scott Rippey: ▶ Highly recommend that. I know you can do a git tree thing with Supabase, but I didn't go that way — just want to make sure you have something.

<!--SEGMENT
topic: Claude Design Backend-First UI Workflow
speakers: Scott Rippey, Brandon Hancock
keywords: Claude Design, UI mockups, color palettes, mobile specs, backend-first, Figma, UX designer, workflow, React
summary: Scott shares his backend-first workflow: once the database and app logic are built, he uses Claude Design with a massive prompt to generate full UI mockups including color palettes and mobile specs. A professional UX designer validated the approach and said he doesn't need to learn Figma.
-->
[02:14:33] Scott Rippey: Once the database was built and a lot of the app was built, I just in Claude Code told it what I was going to do. When I go to Claude Design, I usually have a lot of the backend built, then I'll do UI from that — once I figured out my workflow, it made it so much easier.
[02:15:29] Scott Rippey: This was a massive prompt that drafted the whole thing — it literally did the legit color palettes, and I've got all the mobile stuff already spec'd out. It did a really, really good job.
[02:15:43] Scott Rippey: I used to fuddle through UI first. I talked to a real UX/UI guy in Michigan, and when I told him how I was doing this, he said that's actually really good. <Q>Do you think I need to learn Figma?</Q> <A>No — seeing what you're doing, you don't even have to mess with it. He actually liked the backwards way I was doing it.</A>
▶ Backend-first with Claude Design generating UI may make learning Figma unnecessary for solo builders.

<!--SEGMENT
topic: Blackbox IDE and Agent Harness
speakers: Scott Rippey, Brandon Hancock
keywords: Blackbox, Mac software, IDE, agent harness, flight recorder, SQLite, decision logging, sandbox, auto orchestrator, Vercel CLI, Claude sessions, GitHub repo, free and open source
summary: Scott demos Blackbox, his free, open-source Mac IDE and agent harness with 60+ iterations. It includes a flight recorder backed by SQLite for per-customer spend reporting, decision logging to see why an agent acted, sandbox configurations, and cloud mode with auto-injected Vercel CLI credentials.
-->
[02:16:14] Scott Rippey: I built Mac software, did my Apple developer thing, built my own IDE and agent harness — over 60 versions. This is free and open. It updates over the air from a DMG [link:GitHub repo, shared in chat and School group].
[02:16:43] Scott Rippey: I didn't want all the extra crap in IDEs that I hate — simple, things automatically come up in the same order as your Explorer, no weird names.
[02:17:06] Scott Rippey: The agent harness is what I want some people to test — auto orchestrator, sandbox, all kinds. I did add decision logging so you can see why an agent did something, though I haven't fully tested everything.
[02:17:11] Scott Rippey: It's called Blackbox because it's got a flight recorder — a little SQLite database installed with it so I can report per customer, like what I've spent per customer. Reporting works; I just want to make it prettier.
[02:17:43] Scott Rippey: I also did a cloud mode where you can track by clients and hook in Vercel on the CLI — community plugins. If I do a Claude session instead of a shell, it'll auto-launch Claude and auto-inject securely the thing to connect to Vercel, so I don't have to log into all my Vercels — just let me know if the build succeeded past GitHub.
[02:18:39] Brandon Hancock: The cockpit is beautiful, Scott. The cockpit alone — sold. It feels like the best of T3 and Codex but also your own stuff.
[02:22:15] Scott Rippey: With the agent harness I built a real simple one; I'd like to develop that section more based on people testing it. I can save different configurations and run them against the codebase whenever. I don't have the CMUX-style multi-agent window view — I'd want feedback on the agent part to flesh that out, and the reporting. But the IDE experience is dialed in.
[02:23:10] Scott Rippey: I've got $200 plans and a $100 Codex plan — I'm just the hammer in the nail. I didn't use API to build it, but I tracked how much it would have cost. ▶ I'm keeping it free — the iOS app will be free too — I'm not trying to compete in the developer space; I built a tool for me and want to give it to people who could use it.

<!--SEGMENT
topic: Agentic Browser and iOS Companion App
speakers: Scott Rippey, Brandon Hancock
keywords: agentic browser, Chromium, MCP, iOS simulator, TestFlight, Face ID, Cloudflare, Bonjour sync, voice notes, QR code pairing, multi-Mac sync
summary: Scott shows new additions to Blackbox: an agentic Chromium browser driven over MCP with dev tools and console (demonstrated with a Wikipedia click-game), an iOS simulator, and an unreleased free iOS companion app that syncs to Macs via Cloudflare with Face ID, QR-code pairing, Bonjour-based database sync, and voice notes.
-->
[02:18:16] Scott Rippey: Last week I didn't have a browser, a simulator, or an iOS app — now I have all three. The browser is agentic, Claude Code can run it, it's got the dev tools and console.
[02:18:55] Scott Rippey: This is a test: how many clicks to find coffee on a random Wikipedia thing within eight clicks, and tell me your reasoning. It uses MCP to this little browser — it's using Chromium with all the internal tools. I found it in a couple of hops.
[02:19:16] Scott Rippey: I've got an iOS simulator that works — that was suggested last time. Normally I'm a web app guy, but I went down this rabbit hole because I wanted this for me.
[02:19:51] Scott Rippey: I hate Claude's mobile thing. This is still legal because it's IDE to IDE. Now I have an iOS app — not released yet, but in a day or two, testing through TestFlight.
[02:20:11] Scott Rippey: The app can sync to multiple Macs, it's all secure through a Cloudflare thing, uses Face ID for everything (or just first time), and connects to whatever machine I have running sessions — so I can walk out and just keep going.
[02:20:48] Scott Rippey: Since I have two Macs, I have a database sync that uses Bonjour to connect initially and then syncs both ways, so your data is the same on both — I work on an iMac and a MacBook. I even have voice using the latest Apple voice thing, so I can do voice notes. The mobile UI is super clean: model and context shown, expandable tool calls — more information without clutter.
[02:21:42] Brandon Hancock: You're using the product to build the product — you're in the inner loop, my friend. Please keep me posted on the cockpit experience.

<!--SEGMENT
topic: Daniel's EMS Documentation Startup
speakers: Daniel Zivkovic, Brandon Hancock, Shakur
keywords: EMS providers, fire departments, ePCR, patient transport documentation, reimbursement, EMR, Epic, Cerner, co-founder, distribution partner, domain experts, healthcare
summary: Daniel, a long-time viewer and first-time caller, introduces his startup helping EMS providers (fire departments, hospitals, ambulance companies) write transport documentation for reimbursement inside ePCR systems. His co-founder is an EMS chief in Florida who first hired him as a freelancer; like Scott's story, they had builder and domain expert but lacked a distribution partner, now in discovery with a distribution company.
-->
[02:25:05] Daniel Zivkovic: It's probably my third week here — a long-time viewer, third-time caller. Ty said we're all driving the same highway. I've never been in a group where three or more people had less DBA — we're soulmates. On the negative side, you started the meeting saying we should get clients and make money, not just code. I used to have more clients; now it's one client paying the bills and me goofing around with AI.
[02:26:11] Brandon Hancock: I was a healthcare data architect before AI — it was so bold, boring, bureaucratic, some of the worst software I've seen. I crossed from healthcare to data engineering. <Q>How did you choose that niche? I would never think to compete with Cerner, with Epic, with Google Healthcare Data Engine — what is your customer and how do we find it?</Q>
[02:26:40] Daniel Zivkovic: We're not in that space — we help EMS providers: fire departments, hospitals, ambulance companies. Every one of them has to transport a patient and write documentation to get reimbursed, today inside what's called an ePCR. We built a tool to help them write their documentation.
[02:27:41] Daniel Zivkovic: My co-founder is an EMS chief in Florida who hired me as a freelancer last May, I built V1, and he said let's become partners and go all in. Like Scott's situation, we had two of the three elements — me the builder, Raul the "I know exactly what the people need" — but not the distribution partner. We're actively trying to partner with a distribution company and are in the discovery phase; anything in this field takes forever, which I'm learning the hard way.
[02:28:41] Shakur: I liked your advice about finding domain experts — that's how Google Earth came: the only people who could make money photographing indoors, because Google couldn't see that. So we have to get into companies and either become experts or find one.

<!--SEGMENT
topic: Shakur's Automated Outreach Experiments
speakers: Shakur, Brandon Hancock, Patrick Chouinard
keywords: Google review replies, email outreach, warmup, 30 emails per day, Instantly, PurelyMail, $50 budget experiment, offer value, 10x ROI, CAPTCHA scripts, Facebook Marketplace, Sam Ovens, Alex Hormozi
summary: Shakur demoed an AI-run experiment: a tool that auto-replies to Google reviews for service businesses via cold email, with a $50 budget where the AI makes all decisions. Brandon shares outreach best practices (30 emails/day per account, one domain to five accounts), and the group debates offer economics — is a 10x ROI no-brainer offer behind the zero replies? Patrick mentions a similar automated website-redesign offer getting positive replies.
-->
[02:29:27] Shakur: I set a goal to have a couple of automated projects that just go off and make me money. Also, I stripped everything out, started bare and rebuilt all my skills — it took longer than I thought but I'm moving much faster now. ▶ I recommend everyone strip everything off and start over again, because the models are just getting so much better.
[02:30:28] Shakur: The product — basically, find service-based businesses who have Google reviews and automatically reply for them. Every morning it tells me how many companies it emailed, replies, bounces. It says it has to slowly warm up the email so it can't send too many.
[02:31:11] Brandon Hancock: <Q>What tool are you using?</Q> <A>PurelyMail — I told it to be as cheap as possible but still high quality.</A> The general rule of thumb is 30 per day per email account. Instantly recommends one domain, five email accounts = 150 outreaches per day; to go harder, buy more domains and keep that one-to-five ratio — or else you burn the account or the domain.
[02:31:53] Shakur: I told the AI I wouldn't give it more than $50 for the whole experiment, and no more money until it actually makes a little.
[02:32:29] Brandon Hancock: A few ideas: I always ask about the value in the offer, then work back to a product. Businesses make more money three ways: more customers in the door, more dollars per customer, or customers coming more often. <Q>What happens if a company answers every single Google review, and what if it answers none?</Q> ▶ I always ask myself what's the financial impact — if there's not at least a 10x ROI on what I'm offering, I need to tweak the offer.
[02:34:08] Brandon Hancock: The cool thing is you're actually outreaching — taking the action that opens you up to feedback. Not getting feedback is feedback in and of itself: is it the email, the volume, or the offer itself? I'm a big fan of Sam Ovens, Alex Hormozi — is the offer a no-brainer where they're like "holy crap"?
[02:35:12] Shakur: The experiment I want to run: email local businesses, offer as simple as possible — I know how to use Claude Design, they don't. I'd literally rebuild their landing page, and the email I send could be their new redesigned website.
[02:35:28] Patrick Chouinard: Funny — I actually have another automated offer doing that exact thing: it finds businesses with terrible websites, emails them what's wrong and offers a preview. I'm a little more hands-on with that one; it's already gotten positive replies, I have a meeting tomorrow, and I've had a couple of clients book.
[02:36:11] Shakur: Mine sends 15 drafts every morning into my Google account and I just click send. My setup: it automatically searches Google reviews for business types the AI thinks will convert, looks at their reviews, and says "you have this many without replies, here's the reply I'd already put for you." What I'd change: lower the price, put a dashboard so a person can send replies themselves, and increase the volume — right now the AI said only 40, so I'm about to take the reins.
[02:38:07] Shakur: I also built scripts so the AI automatically fills out CAPTCHAs — each time it figures out a new one, it saves it to a file to redo later. I told it to also find things on Facebook Marketplace to buy and sell with $50 — it drafts messages and asks if I can go, and I'm like no, not going to that area tomorrow. Those are my three automated ones.

<!--SEGMENT
topic: Gated Looping Agent Workflows
speakers: Shakur, Brandon Hancock
keywords: skills, grill me, triad critique, Fable, Sol, Opus, plan critique loop, loop deep work, gates, kiosk mode phone, grandparents video calls, long-running agents, Terraform, Google Cloud
summary: Shakur describes his rebuilt planning skill (grill-me critique, then a Fable/Sol/Opus triad that argues until they agree on the best plan) and a kiosk-mode phone for his son to video-call grandparents. Brandon shares his "loop deep work" pattern: break a long-term goal into gates the agent must pass, looping plan-critique-execute-review per gate, enabling 6–8 hour autonomous runs.
-->
[02:39:30] Shakur: I rebuilt a couple of skills. One is like Matt Popok's "grill me" — it grills me and flushes out the whole plan. Then I do a triad: it'll pass the plan to Sol, who says "these are all the holes, here's the plan I would do," then to Opus, and they keep going around until they all agree this is the best plan. I feel like it's a pretty useful skill.
[02:40:33] Shakur: Last time I mentioned a little phone device so my son could call his grandparents without using a phone. I decided to completely simplify it: buy an old cheap phone, switch it to kiosk mode so the only thing he can do is make calls. If they pick up, he can video chat; if not, he can leave a message and they can call back — with bedtime set up in the program.
[02:41:49] Brandon Hancock: Every part of that workflow makes sense. The one thing I'd change: I use something called loop deep work — it actively keeps pursuing and coming up with its own plan to attack the goal. Here's how I structure it: I have a long-term goal, but I break it into gates it has to pass. The agent figures out the gates and what success and failure look like for each; within each gate it does plan, critique, action, review, fix — until the gate passes and unlocks the next. That solves the problem with prompt-based coding where it says "I'm done" after one prompt. ▶ I let it loop as many times as it needs per gate — I'll have it run six to eight hours sometimes, just cranking out valuable work, and I wake up and go "you did it." It's running right now on transcript stuff in Google Cloud and working on Terraform.
[02:43:11] Shakur: I've tried to get that working and mine always says "okay, I'm done" — you're not done. If you make a video or can tell me the steps, tell me.
[02:44:11] Brandon Hancock: That's a great learning opportunity — point back and say "here's what you should have done differently," update the prompt to determine what loop deep work looks like, update the actual plan so you don't run into the issue in the future, and then with that feedback, go off and execute.

<!--SEGMENT
topic: Loop-until-done agent workflow
speakers: Brandon Hancock, Shakur
keywords: loop until done, plan, critique, review, Ralph Wiggum, Claude, Codex, adversarial models, review prompts, gates, iteration
summary: Brandon describes a "loop until you're done" agent pattern where each gate contains a loop: plan, critique the plan, do the work, review the work, and repeat until the goal is achieved. Shakur asks whether the review step uses a different model, and both discuss review prompts and Claude plugin skills as inspiration.
-->
[02:44:35] Brandon Hancock: So it just takes iterations, but once again, if it doesn't work, it's feedback that something underlying is broken. It's the hardest part getting it going from nothing to working. I have a couple of projects in mind to try that kind of loop-until-you're-done work. It's very Ralph Wiggum-esque, except within each gate there's a loop.
[02:45:11] Brandon Hancock: Like, the loop is: come up with a plan, critique the plan, do the work, review the work — did you achieve the goal? No?
[02:45:18] Shakur: Okay, do it again, until it's done. If you're looking for inspiration with updating it, I'd point at that — just to give it some ideas of what ultimately we're trying to do. <Q>So for the review, do you use a different model? Are you kind of adversarial modeling?</Q>
[02:45:39] Shakur: I should have Claude call Codex or something like that, like Patrick's talking about, or something totally different — but for simplicity right now, just have it call itself: have a review task, have a prompt that is "this is how I review stuff for this code base." That's what I always recommend.
[02:45:58] Brandon Hancock: <Q>What does a good review look like? What does a bad review look like?</Q> I think the super skills you can get in the Claude plugin have some review stuff in there you can take for inspiration.
[02:46:08] Varun Sharma: There's a ton of files — we just need to have something. Just as a starting point.

---

<!--SEGMENT
topic: YouTube transcription skill demo
speakers: Varun Sharma, Shakur
keywords: YouTube video, transcription, skills, cold email, context, summarization, cheat code
summary: Varun shares that he built a skill that ingests a YouTube video, transcribes it, and surfaces only the parts useful to him so he doesn't have to watch the whole thing. Shakur demos the output, noting the skill combines context on the user with context on the video.
-->
[02:46:18] Varun Sharma: I also threw that YouTube video into one of my skills — the one you sent with the cold email — where it transcribes everything, lists out whatever could actually be useful to me, and tells me, so I don't have to watch the whole video.
[02:46:42] Shakur: Let me share that quickly. I gave it the video, the whole breakdown, and it told me there's two parts that will be useful.
[02:47:01] Shakur: It has context on you and context on the video. ▶ That's a cheat code, man.

---

<!--SEGMENT
topic: AI cold outreach follow-up
speakers: Varun Sharma, Brandon Hancock, Shakur
keywords: cold email, follow-up, outreach, subject lines, email copy, funnel, offer, voice typing, few-shot examples, human tone, isolation testing
summary: The group critiques Varun's autonomous AI outreach experiment. Key advice: the money is in the follow-up (4–5 touches), AI-written emails sound too corporate so you should voice-type your own tone as few-shot examples, and isolate variables — test subject lines first, then copy — to find the weak link between offer and messaging.
-->
[02:47:11] Varun Sharma: On the review stuff and outreach — in marketing, there's a saying that the money is in the follow-up. You'll need to send at least four or five follow-ups to those emails if you expect a response. The whole experiment was me not doing anything; now I'm getting more involved. I already told it each day to review what it did the previous day and come up with improvements.
[02:48:03] Varun Sharma: <Q>If you're sending a hundred emails a day, ideally shouldn't half of them be follow-ups?</Q> The most important thing I've noticed is that emails AI writes in general are pretty bad — like corporate immunity. I would vomit if somebody emailed me like that. ▶ You have to get it to write in a very human way: voice-type how you would send a message to somebody, have it transcribed, and use that as few-shot examples to get the emails written in that kind of voice.
[02:48:51] Brandon Hancock: Something that has worked for me with Google email is to test a lot of different things. If you're sending 20 emails, first send emails with different subject lines, because then you'll notice what kind of emails get opened. Once that metric is dialed in, go to the email copy itself and send 25 different versions to see what copy gets replies. ▶ By isolating these specific components you can identify the weak link — right now you wouldn't be clear if it's the email or the offer that's the problem. Personally I feel like this offer is gold for any local business, so it must be the copy or the outreach execution.
[02:50:11] Brandon Hancock: Everything Bruun said is spot on — usually the second or third email is when they finally respond. The other thing: letting AI just be AI without any constraints is dangerous, because it's pulling from everybody, so it's almost doing nothing. ▶ Per activity of the business — coming up with the offer, writing the email — emulation is key. Anytime AI is going to take an action, find someone who has done it successfully, copy their playbook almost verbatim — the way they write, the way they think — and emulate it, to give it constraints and base it off what's worked.
[02:50:55] Varun Sharma: I'm probably going to step in and revamp it pretty soon. It's an experience we're figuring out — that's the whole point. Hey, 50 bucks is much better than 5,000. Glad we didn't burn too much.

---

<!--SEGMENT
topic: Build-in-public challenge videos
speakers: Varun Sharma, Brandon Hancock
keywords: career switch, Google Cloud, Gemini, positioning, build in public, scalable systems, AWS, challenge video, 800,000 views, social proof, job applications, DeepSeek
summary: Varun, focused on skill-building for a career switch, asks whether to pivot his Google-stack positioning given Google's lag. Brandon responds with a case study: an engineer who built a two-hour video scaling a system to 800,000 views, arguing that doing valuable work in public and giving it away free generates more job opportunities than thousands of applications. He suggests a challenge like "handle 1,000 customer queries with AI for under a dollar."
-->
[02:51:30] Varun Sharma: My questions are pretty rudimentary compared to the missions others are getting — other folks are building startups. I'm more focused on skill building. In an earlier ShipKit call I mentioned moving towards a career switch. First question: you suggested focusing my skills so I can position myself as, say, a Google guy. I've completely focused on Google — Google Cloud, Gemini API, everything you teach on your YouTube channel. But Google has lagged badly in the last few months — nobody talks about Google ADK, everyone is gung-ho on Claude agents. <Q>Should I pivot my positioning strategy, or look at fundamentals from a different angle?</Q>
[02:52:37] Brandon Hancock: I still think that strategy works, but let me step back and explain how we could pivot, because you're totally right — are their models the frontier like ChatGPT or Claude? No. What's the goal? From my understanding, it's to start getting freelance opportunities or a job as a software engineer. That takes a bunch of eyeballs knowing you're skilled at a specific thing. The old approach of straight job applications — it's very hard to get a job that way now.
[02:54:41] Brandon Hancock: What this guy did is he showcased that he is an engineer who can build scalable systems — and he showed how others can do it too. He scales up handling 100 requests, 1,000, then 10,000 on his local computer, then: "now we hit a bottleneck — to solve it, we have to do this." ▶ In your case: do a cool experiment like this in public, with Google Cloud plus their AI features — e.g., "How can I handle a thousand customer queries with AI for under a dollar?" Show pivoting from Gemini 3.5 to 3.6, then to Chinese models like DeepSeek v4 Flash, hitting intelligence or cost limits, and adjusting strategy at each level.
[02:56:46] Brandon Hancock: If this guy didn't get an AWS-related job after 800,000 views, I'd be shocked. ▶ This two-hour video will give him more value than 10,000 job applications — he showed in public he is a skilled thinker and got 800,000 eyeballs. The key lesson: do something valuable in public and give it away for free.
[02:57:29] Brandon Hancock: If I was you, I'd paste this conversation and say, "Hey AI, I want to come up with a similar challenge" — here's the whole two-hour transcript. Over two hours he does 10 different iterations. As long as you can ask intelligent questions, you could copy this. Give away all the code — you could have AI scaffold the whole video, the prompt, everything.
[02:58:33] Varun Sharma: That's definitely building social proof, basically.
[02:58:37] Brandon Hancock: Literally building social proof. Also, YouTube is just copying success — once he figured out what worked, he just copied it again. As a YouTuber, I always have my eye out for that outlier number — when a video is like 68x, that means the idea was viral, and I ask how I can use that viral idea for my use case. [tool:vidIQ — YouTube plugin that flags outlier videos]

---

<!--SEGMENT
topic: Viral challenge ideation examples
speakers: Varun Sharma, Brandon Hancock
keywords: viral ideas, lead generation, DeepSeek, cost optimization, personal brand, challenge a week, leverage, case study
summary: Brandon and Varun brainstorm concrete viral challenge formats, like "find a thousand leads for $5," mirroring Brandon's own case study of switching to DeepSeek to cut lead-gen costs from $400 to a few dollars. Doing one challenge a week is framed as the highest-leverage way to grow a personal brand.
-->
[02:59:38] Varun Sharma: There's so many things you could do here — "How to find a thousand leads for $5" — that's in and of itself a viral idea. You could do the exact same case study I did for my own business: I could find a thousand, but it was going to cost me $400. Cool — I switched to DeepSeek. DeepSeek found me a thousand for a dollar or $3. Okay, how do I scale that up even more?
[03:00:11] Brandon Hancock: There's a thousand ways to do that challenge, and by doing a challenge it forces you to learn. ▶ If you just did one challenge a week, you'd get so much smarter and something awesome would happen — that's the best two months you could spend growing the Varun personal brand. There's no higher-leverage effort.

---

<!--SEGMENT
topic: YouTube channel strategy and cohort
speakers: Varun Sharma, Brandon Hancock
keywords: YouTube channel, cohort, transformation, niche triangle, software, AI, business, vidIQ, outliers, first video, timeboxing, ShipKit, Listio
summary: Varun asks about Brandon's past YouTube cohort. Brandon explains why he may not relaunch (tiny conversion rate) but argues YouTube is the most valuable skill for a developer: pick a transformation at the intersection of software, AI, and business. He advises copying the challenge-video formula, starting simple, timeboxing the first video to three weeks, and using vidIQ to spot outliers.
-->
[03:00:38] Varun Sharma: I completely agree — I do want to build a personal brand once I feel confident I have enough skill. You launched a cohort for building a YouTube channel — is that something on your mind? Building a YouTube channel is a skill in itself, and I'd rather do it the right way.
[03:01:12] Brandon Hancock: I'll give you the entire pitch in two minutes. I launched it at 50–60,000 subscribers, but developers who at that exact moment wanted to start a channel — it was like 20 people, a conversion rate of 0.04 of my audience. I personally think it is the most valuable skill any developer could learn, period. It doesn't matter if you're the world's best engineer if no one knows who you are. ▶ I'd much rather have a million people know me and be an average engineer than be the world's best engineer with three people knowing me.
[03:02:09] Brandon Hancock: The whole pitch of a YouTube channel: you take people on a transformation. The thing I picked was helping developers become profitable AI developers — I have to learn business, AI, and code. Those are three triangles, and dead middle is where my channel lives. Anytime I teach, I make sure it hits two of the three: software + AI, AI + business, or all three.
[03:02:42] Varun Sharma: When it comes to content, I wouldn't go for a home run out of the gate.
[03:02:55] Brandon Hancock: In your case, making a challenge video like this would be fine — you could literally just copy that guy's formula ten times until something hits. Each time you make it, it gets better. Start with a simple challenge first, because you're learning code, software, speaking on camera — there's so much more to it.
[03:03:24] Brandon Hancock: The tool is called vidIQ — just a plugin. Anytime you go on YouTube, it tells you what an outlier is. I always use it to check for outliers and note: I need to copy this viral idea. That literally is the fastest way to grow.
[03:03:40] Varun Sharma: <Q>Do you have coaching call videos that aren't confidential that you could give out or roll out as a course for subscribers?</Q>
[03:04:00] Brandon Hancock: Pending money coming in for our investment, my whole goal is to start YouTube again. What I'm doing right now with Listio — the goal is, as quickly as possible, please investment gods, let money come, so I can do eight hours a day on the job and get back to YouTube and ShipKit. I'd totally be fine putting that course material in ShipKit for you guys and updating it — I just need money to come in so I'm not spending every waking moment on EMS soap.
[03:05:11] Brandon Hancock: ▶ Don't overthink it: timebox it — "I'm going to spend three weeks starting tomorrow to come up with a challenge and finish the whole thing." Your first one will take the longest; two and a half weeks is what I'd do. Just say, "Hey AI, this is my first video, I want to come up with a challenge like this, help me through it." Know you have a deadline — otherwise it takes eight weeks and nothing happens. If what I produce is eh, so be it, I'll do it again the week after.
[03:05:52] Varun Sharma: <Q>Do you think a 20-minute video would be good for the first try?</Q>
[03:05:56] Brandon Hancock: Oh yeah, dude, anything — even just hopping on camera saying, "Hey, this is my YouTube channel, I'm going to be doing challenge videos." That truly would be the best first video.
[03:06:11] Brandon Hancock: ShipKit — I launched it last year to help developers launch applications in days instead of months: my exact methodology for letting agents do all the work, with pre-built templates where you just talk to the agent and it builds your whole app. I'm literally using it right now to build Listio, but a year has passed, so a lot of changes need to be pushed to it.
[03:11:22] Brandon Hancock: Next time we hop on, I'd love to see your first video — that's the homework. The first one is the hardest, most uncomfortable — you'll be a deer in the headlights, but so did everyone else. Before recording my first YouTube video, I took two shots — tequila or whiskey, I can't remember. ▶ It will be the cringiest video you make, but every video after that gets better. Just get it out.

---

<!--SEGMENT
topic: Spec-driven development and skills
speakers: Varun Sharma, Brandon Hancock
keywords: ShipKit, task templates, self-reflection, plan mode, Claude Code, spec driven development, skills, artifacts, software development lifecycle, poke holes, second-order consequences
summary: Varun asks how to get deep model self-reflection within ShipKit's task-template prompting. Brandon explains his full lifecycle: Claude plan mode produces a plan, a separate skill expands it into a hyper-detailed task template (~12 sections covering data model and UI specs), another skill pokes holes in the plan, then execution and review — every step is a skill that generates or updates an artifact.
-->
[03:06:49] Varun Sharma: ShipKit question only. In the task templates, you have a very specific way of prompting the AI to do its thinking before it generates the steps required for the task. That's a bit like self-reflection. <Q>If I were to copy that way of getting the model to think deeply, is there a technique to do that within a single prompt? How would you do it from first principles?</Q>
[03:07:24] Brandon Hancock: This is the exact approach I use for our existing product. I tell Claude the problem and go into plan mode. A plan is nothing but condensed information on what should happen. We give AI this much information; a plan is then condensed info: "I've researched, I think I found the issue." Then I have it create a task template, which is hyper-detailed. We're planting a seed of information and expanding it, forcing the AI to keep thinking about building this.
[03:08:18] Brandon Hancock: After I have the task, I have a separate skill whose sole job is to poke holes in the plan — look for logic gaps, second-order consequences that weren't thought about. It's like having two engineers discuss it. Then, after the plan has been rigorously tested, it's time to execute. Once the code is implemented, we review the work. ▶ The task template is still a core piece — I've just expanded before it and around it since making ShipKit.
[03:09:03] Brandon Hancock: You'll hear a common term: spec driven development. It's an abstract term — what is a spec? What you should build. The task template is like 12 sections where we force it to think about specs for the data model, specs for the UI, and fill out what should happen — a concrete spec, not a general "it should make things." ▶ That's why I'm such a big fan of task templates versus a general spec: "what makes a good spec" is too hard a question; forcing your way through the task template gets you there.
[03:10:15] Varun Sharma: So you're giving it enough context, the empty task template file, and the skill all within a single prompt — or a separate prompt where it first generates a task and then you use the skill?
[03:10:35] Brandon Hancock: The entire software development lifecycle — every step has a skill. That's the cleanest way to think about it. The plan mode that comes out of the box with Claude Code, I just let it do its thing: "here's what I'm trying to solve, go plan mode." Once it has a plan, that gets saved, then a task template gets created — that's a separate skill. Then "go execute," then review is a separate skill. ▶ Every action is a skill with best practices, where every step generates an artifact or updates an artifact.

---

<!--SEGMENT
topic: Wrap-up, entrepreneurship, Delaware warning
speakers: Brandon Hancock, Patrick Chouinard, Daniel Zivkovic, Varun Sharma
keywords: ShipKit, YouTube, entrepreneurship, Delaware C-Corp, Y Combinator, Eric Ries, equity, Twilio, founders, scheduling
summary: Closing remarks: Brandon expresses eagerness to return to creative work once revenue arrives, and schedules a Thursday call with Patrick. The conversation shifts to a warning about Delaware C-Corps — Eric Ries's new book and a YC video caution that founders can lose control through equity dilution, illustrated by a Twilio champion's founder being ousted after eight years.
-->
[03:12:07] Brandon Hancock: Anybody else? So many good ideas, guys. I'm so pumped for dollars to come in so I can finally get back to this. My creative side is dying — every day it's just execution, less room for what I find interesting. Hopefully you'll know what's happening because the YouTube video will go out.
[03:13:18] Daniel Zivkovic: Patrick, I pulled up my calendar — Thursday afternoon would be best. I'd like to hear a little more about what's been going on. Just send me an invite; I'm on vacation this week.
[03:13:41] Daniel Zivkovic: Hope you guys have an awesome rest of your Tuesday. Thank you once again, Patrick, for holding everything down. Looking forward to being back on a more regular cadence and shipping some value for you guys.
[03:14:02] Brandon Hancock: Everybody needs it. It's scary — like being a CEO with no money.
[03:14:10] Daniel Zivkovic: They always make it seem exciting in the books whenever you read about entrepreneurship, and then you get into it and you're like, this hurts.
[03:14:18] Brandon Hancock: This hurts spiritually, mentally, physically — all of them.
[03:14:23] Varun Sharma: About your advice for Delaware — I'm from Canada, but I follow Y Combinator videos. Eric Ries, who we love, wrote another book warning companies not to do that. I used to be a Twilio Champion, and the founder was kicked out of the company after eight years because of this Delaware contract — obligations to shareholders. ▶ Listen to that YC video before you become rich, because it's going to be hard to untangle yourself. [link:Y Combinator video on Delaware C-Corp warnings]
[03:15:07] Patrick Chouinard: I thought it was the standard. Watch the video — it's really warning signs for why he wrote the book, because he felt guilty for teaching startup companies to become successful and then they lose everything.
[03:15:32] Brandon Hancock: My guess is they gave up so much equity they became a minority. I just did a quick summarize on Google — it talked about C-Corp specifically, and they're counterproductive for founders.

---

=== UNRESOLVED SPEAKERS ===
- Hemal Shah
- Daniel Zivkovic
- Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
- Varun Sharma