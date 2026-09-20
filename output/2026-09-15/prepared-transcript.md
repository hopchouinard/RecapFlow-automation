=== SESSION ===
date: 2026-09-15
duration_estimate: unknown
main_themes: agentic morning-briefing pipeline (Beacon/Clara/TTS); photo booth AI sales strategy; Claude Code skills & token management; ShipKit skill conversion; enterprise AI operationalization; ERP platform launch with "UI in reverse" testing; home lab & AI agent setups (Proxmox; Hermes; Pi); AI dev harnesses (T3; Pi; ECC; Agent Ops); member project updates (estate agency site; fitness app; Fable models); visual ML shelf-recognition reinvention

<!--SEGMENT
topic: Introductions and flu small talk
speakers: Patrick Chouinard, Juan Torres, Ty Wells, Paul Miller, Rod Morrison
keywords: flu, Quebec, weather, Canada, Vancouver, Seattle, Zoom, hosting, fall, winter
summary: Patrick opens the call hosting while sick with the flu, noting Paul is also ill. Participants make light small talk about Quebec's extreme weather, Juan's planned Vancouver trip in 2020, and how the tag-team hosting will work between Patrick and Paul.
-->

Patrick Chouinard opens the meeting, announcing he's hosting despite having the flu since yesterday: "I have to mute sometime for a fit of cough and don't be too worried." He may talk less than usual. Juan Torres, Ty Wells, Paul Miller, and Rod Morrison check in.

<Q>Juan: "Can you get the flu through a Zoom call?"</Q> <A>Patrick: "No."</A> Patrick jokes that his family told him to work from home but not to stop working, so presumably he's not contagious.

Paul Miller reveals he has the same illness and proposes they "do tag team today." Small talk covers Quebec's weather extremes (−40°F winters, 110°F summers) versus Juan's Seattle-area experience and his pandemic-aborted 2020 plan to visit Vancouver. Rod compliments Quebec as a great food town.

---

<!--SEGMENT
topic: Beacon morning briefing agentic pipeline
speakers: Patrick Chouinard, Ty Wells, Juan Torres, Paul Miller
keywords: Beacon, Clara, research agent, TTS, Discord, Hermes VM, Perplexity, ChatGPT, archive, Traefik, Tailscale, newsletter, contextualization
summary: Patrick demos "Beacon," a daily research agent whose raw reports are contextualized by his main agent "Clara" into a personalized monologue, converted to audio via TTS, delivered via Discord, and archived on the Hermes VM with transcript and source evidence. He describes a feedback loop using ChatGPT discussions to improve future briefings, and plans external access via Traefik and Tailscale.
-->

▶ SCREEN SHARING: https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=519.654363

Patrick describes his research agent architecture: [tool:Beacon] searches the web daily for news adapted to his ongoing AI projects and sends a newsletter-style report. Beacon "has no knowledge of me" — Patrick instead interacts with his main agent [tool:Clara], which knows everything about him. Pipeline: Beacon produces a raw report → Clara contextualizes and reformats it as a morning monologue ("as if you were getting into my office in the morning") → TTS model generates audio → delivered through Discord.

He demos the newly built internal site on the Hermes VM: the "Beacon Morning Briefing" archive stores audio, Clara's transcript, and the original Beacon evidence including source and generation details. ▶ The evidence can be pasted into ChatGPT for a discussion of impressions, whose output feeds back into the system to optimize tomorrow's briefing — a continuously improving loop.

In the demo audio, Clara highlights that Perplexity is packaging the full agent operating loop for Windows (model, harness, orchestrator, scheduler, local tools, local MCP servers) on an NVIDIA workstation — keeping routine execution local with cloud intelligence as explicit escalation.

ACTION ITEM: Expose the archive via Traefik reverse proxy + Tailscale for mobile/road access — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=654.9999

<Q>Juan: at what point do accumulated daily reports exceed model context limits — do you need bigger-context models or tagging/limiting by date range?</Q> <A>Patrick: execution runs on a cheap model with ~900k–1M token context via Hermes; news archives don't need re-analysis or vectorization — a year-old news item's value is limited, and the archive exists mainly to replay audio.</A>

---

<!--SEGMENT
topic: Patrick's parallel AI projects and token burn
speakers: Patrick Chouinard, Ty Wells, Juan Torres
keywords: Astra, sub-agents, personal website rebuild, token limits, Fable 5.1, browser extension, ChatGPT JSONL, podcast, TTS, $200 subscription, Tebow reset
summary: Patrick shares three additional projects: an Astra-orchestrated rebuild of his personal website using dispatched sub-agents (ran ~17 hours straight), a training app for Claude design using Fable 5.1, and a planned browser extension exporting ChatGPT conversations as JSONL to publish AI-human collaboration stories as potential podcasts. Discussion turns to severe token exhaustion on $200 plans and recent Tebow usage resets.
-->

Patrick reports on three more vacation builds:

1. **Personal website revamp** — his six-month-old resume/portfolio site was fed to an Astra loop that rebuilt it from scratch. ▶ Astra was instructed to act as team lead, dispatching sub-agents for tasks and only validating with Patrick when needed — it ran ~17 hours straight before running out of tokens. A staging deployment exists; completion awaits Thursday's token replenishment.

2. **Training application** demonstrating how to leverage Claude design using Fable 5.1 — also token-exhausted, roughly halfway done.

Ty Wells commiserates: he burned his Astra allocation and all three resets in two days, dropping from medium to light tier. Patrick notes he runs only Astra medium and went through four resets, mentioning a global reset by "Tebow" on the 6th and recent usage-percentage jumps (1%→80%, or luckily for him 90%→20%).

Patrick then reveals (after Ty guesses it) a podcast-adjacent project: a browser extension to download entire ChatGPT conversations as raw JSONL, to be reformatted into publishable stories that openly show human-AI collaboration — each point of view explained separately — potentially fed into TTS as a podcast. ▶ He upgraded to $200 subscriptions on both sides and still exhausted tokens in a week of vacation-time generation (four parallel P3 code sessions plus Claude Code plus Hermes simultaneously).

---

<!--SEGMENT
topic: Juan's photo booth AI go-to-market strategy
speakers: Juan Torres, Patrick Chouinard, Paul Miller
keywords: photo booth, image-to-image, Fusion models, FX AI segmentation, San Diego venues, country clubs, bespoke transformation, landing page, demo kit, iPad, free pilot
summary: Juan pivots from engineering to go-to-market for his AI photo booth application. He believes his image-to-image pipeline outperforms major providers, and plans a four-step outreach escalation to high-end San Diego venues: bespoke demo email, call, in-person visit, and network joining. Paul advises a portable phone+iPad demo and pre-recorded offline fallback.
-->

Juan reports a strategy week rather than a build week. His application is a photo booth with AI transformations via fusion image-to-image models. ▶ Based on research into major image-to-image providers, his pipeline compares favorably — competitors offer FX AI segmentation or nascent image-to-video, and existing photo booth apps' "AI" outputs are bland or nonexistent.

ACTION ITEM: Create a bespoke image-to-image style for each target venue (using their symbolic places and brand), then email the venue director with a demo and offer a free first pilot — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=1277.9999

ACTION ITEM: Build a photo booth landing page (none exists yet) — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=1316.9999

▶ His escalation plan: (1) send email with bespoke transformation, (2) follow-up call for a rundown, (3) visit the venue to talk to the country club director, (4) final email — plus joining venue/country-club networks.

ACTION ITEM: Identify and join local country club/venue networks — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=1401.9999

ACTION ITEM: Prepare portable demo kit (phone + iPad) and pre-recorded demo — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=1421.9999

Paul Miller suggests one phone for camera capture plus one iPad for the transformed-display demo, always with an offline pre-recorded fallback. ▶ Paul also recommends the OpenAI app-building tool to create native iPad/Android versions of the two-screen system, arguing the slickest portable in-person presentation wins at the point of sale. Juan hesitates on native app priority — client acquisition comes first — and shares a physical-setup reel video for demonstrating the workflow. Later roadmap: printing capabilities and image-to-video pipeline.

---

<!--SEGMENT
topic: ShipKit templates converted to Claude skills
speakers: Rod Morrison, Patrick Chouinard
keywords: ShipKit, skills, YAML front matter, slash commands, orchestrator skill, tech stack, Matt Pocock, Claude, GitHub, PRs, skill decomposition
summary: Rod asks whether anyone still uses ShipKit. Patrick explains he converts ShipKit templates into Claude Code skills — decomposing long templates into sub-skills with an orchestrating uber-skill, adding YAML front matter and slash-command plumbing — and maintains a personal tech stack at account level so Claude stops recommending mismatched technology. Rod shares he's using Matt Pocock's skills methodology with his team.
-->

Rod Morrison reports a heavy build week pushing a release as a "player coach" (team lead who also builds) and asks: <Q>"Anybody still using ShipKit?"</Q> <A>Patrick: not to build from, but to generate skills from — many of his internal skills are reformatted ShipKit templates.</A>

Patrick details the conversion: ShipKit templates are essentially basic skills already; he sometimes decomposes long ones into sections with an uber-skill orchestrating them underneath, adds YAML front matter defining callable skills and slash commands, and tweaks technology references. ▶ He also maintains a permanent personal tech stack at his account level so Claude recommends exactly his coherent ecosystem instead of "recommending weird technology every single time." He notes Brendan is working on something similar, possibly a ShipKit skill version.

Rod describes operationalizing Claude as a team in his organization — the hard part is business people and skeptical-but-bought-in data scientists. He's using GitHub PR-review tips he learned here and leaning into Matt Pocock's skills methodology for simplicity.

Patrick responds: ▶ build infrastructure so skills like Matt's have their questions pre-answered — his proprietary Grille-with-Docs variant knows the tech stack, deployment targets, protocols, and existing reusable code, cutting spec cycles from 70–80 questions to 15–20, saving enormous token overhead.

---

<!--SEGMENT
topic: Skills marketplace, department memory, token efficiency
speakers: Rod Morrison, Patrick Chouinard
keywords: Azure DevOps, GitHub migration, internal marketplace, Cowork, department memory, Git, Obsidian, agent swarm, Wayfinder, Fable, Sonnet, Opus, orchestrator context window
summary: Patrick describes his team's internal skill marketplace on Azure DevOps (migrating to GitHub) and a planned department-memory system: context documents managed via skills in Git repos, synced to all machines daily, invisible Git UX. Discussion covers orchestrator token efficiency, Wayfinder phase-splitting for context windows, model selection (Sonnet vs Opus by complexity), and cross-model code review.
-->

<Q>Rod: are skills hosted in Cloud or GitHub — internal marketplace?</Q> <A>Patrick: private repository on Azure DevOps, migrating to GitHub. Works for Claude Code and GitHub Copilot; not yet for Cowork/Claude AI which requires a GitHub repo — those will be the first repos migrated.</A>

▶ Department memory plan: memory management at department level inside Git repositories, managed through skills — one skill manages the org chart, another procedures, etc. Context documents sync to everyone's machine each morning so every Cowork query runs with latest department info plus personal memory.

<Q>Rod: not Obsidian? It's new for Cowork, right?</Q> <A>Patrick: Obsidian-style second brains don't work at organization scale — no sync, diff, or rollback. They use Git underneath, fully automated so users never see it.</A>

On multi-agent token burn, ▶ Patrick argues structured agent swarms beat one vague agent: an investment banker asking an agent to "reanalyze those 600-page PDFs and tell me if I should buy" wastes a truckload of tokens versus organized agents doing programmed tasks.

▶ Architecture guidance: start from Wayfinder (not Grille) which splits projects into phases and small contexts fitting one session's context window; the Fable orchestrator should hold minimal context — it only watches other agents — leaving large windows to Sonnet or Opus by complexity. A REST endpoint: Sonnet handles it easily; a crucial route connecting six systems: Opus. ▶ "If you split the work correctly, Sonnet builds a whole lot" — it just can't do 300 pages in one shot. Rod mentions his Implement → Simplify (for >300-line diffs) → Fable code-review loop.

▶ Cross-model validation: Patrick never code-reviews with the model that built the code — build with Astra, validate with Opus; build with Opus, validate with Sonnet/another.

---

<!--SEGMENT
topic: OpenRouter, GLM, benchmarks, and compliance
speakers: Rod Morrison, Patrick Chouinard, Paul Miller, Juan Torres
keywords: GLM 5.3, OpenRouter, Bedrock, benchmarks, GCP, Google startup school, Hermes, Cursor, AWS, MCP gateway, compliance, financial institution, API keys
summary: Patrick recommends GLM 5.3 on OpenRouter as between Sonnet and Opus at a fraction of the cost. Paul suggests benchmarking Claude against cheaper OpenRouter models, including secure Bedrock-hosted options. Rod plugs Google's startup school funding. Patrick explains his personal setup (OpenRouter + Codex + Claude via Hermes) versus corporate AWS-backed Claude/Copilot at a financial institution where compliance rules out OpenRouter.
-->

ACTION ITEM (Rod): Evaluate GLM 5.3 on OpenRouter, set Claude benchmarks, run OpenRouter comparison tests — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=2523.9999

▶ Patrick: "Look at GLM 5.3 on the open router. I find it does a marvelous job. It's basically between Sonnet and Opus... and it costs like a fraction of what Opus costs."

▶ Paul Miller's method: have strong Claude models set a benchmark, then run the same code through cheaper OpenRouter models (including firewall-secure Bedrock-hosted open-source models) until one matches.

Rod shares that Google Startup School started today — Google is funding small companies, recognizing it missed the cloud wave (40% of internet traffic but ~11% cloud share).

<Q>Juan: do you combine Hermes with OpenRouter for outside-work experimentation?</Q> <A>Patrick: big OpenRouter user for personal work — AWS is too complicated for weekend fiddling, and Hermes is "insanely good" at operating the OpenRouter API (creating and storing API keys internally). At work he uses Claude and Copilot on an AWS backend.</A>

Juan considers dropping his Cursor subscription for Hermes + OpenRouter, keeping a Claude subscription for frontier models — noting OpenRouter access to top Claude models means paying per-token without subscription rates.

<Q>Rod: is OpenRouter for personal or corporate — compliance questionnaires are arriving about AI tools and data handling.</Q> <A>Patrick: OpenRouter is personal only; it's a financial institution, already a full AWS client with API gateway implemented and MCP gateway planned — easier with a 30-person infrastructure department.</A>

---

<!--SEGMENT
topic: Ty's ERP platform launch and UI-in-reverse testing
speakers: Ty Wells, Paul Miller, Rod Morrison, Lisa Jetton, Patrick Chouinard
keywords: ERP, pitch deck, Bahamas, regulatory compliance, launch day, UI in reverse, adversarial testing, Astra tokens, analytics, tracked links, 1400 screens, postmortem
summary: Ty demoed his ERP platform launch — delivered as an in-app 31-slide interactive presentation with click analytics and tracked share links rather than static slides. He describes his weekend "UI in reverse" methodology: extract UI contracts from source, make code meet them, then adversarially verify — seven agents, 1,400 screens, five hours of Astra tokens. Launch reception is strong with inbound calls.
-->

SCREEN SHARING: https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=2891.133309

Ty announces launch day: "the pitch deck came in the form of an application itself." ▶ Instead of slides, he built the presentation into the platform — 31 interactive screens explaining features to customers awaiting app access — so analytics flow back (tracked copy-share links show who clicked and opened). He delivered in 45 minutes plus Q&A; customers get platform access tomorrow.

Weekend testing: his "UI in reverse" method — with source access, read the requirements/contracts defined on each screen without opening the UI, write code to meet those contracts, then run an adversarial session looping to confirm completion. ▶ Long-term vision: mock up UI with a client first, then have the agent build code to make the agreed UI work, with adversarial checks verifying contracts — design-first, code-second. Cost: ~5 hours, seven agents, ~1,400 screens — where his Astra tokens went.

ACTION ITEM: Run ERP launch postmortem with team (skipped due to launch-day exhaustion) — https://fathom.video/share/sTLHaj9eU9y5J4Uhc492BZpG1PCE6kyg?timestamp=3152.9999

<Q>Paul: were you able to see funnel engagement from the interactive screens?</Q> <A>Ty: it's still live and he's watching clicks in real time — that's exactly why he built it as an app rather than a slideshow.</A> Response has been good: calls coming in, people ready to sign up and requesting walkthroughs.

---

<!--SEGMENT
topic: Lisa Jetton introduction and Ty's platform context
speakers: Lisa Jetton, Ty Wells, Patrick Chouinard
keywords: Lisa Jetton, Austin Texas, full-stack engineer, distributed computing, P2P, Holochain, hash graph, construction company, agentic systems, Linux, Arch Linux, CachyOS, Fedora, Bahamas, brokerage
summary: New member Lisa Jetton introduces herself: Austin-based full-stack engineer with eight years in distributed computing/P2P (Holochain 2D hash graphs), now building agentic backend systems for her husband's construction company as a service for local SMBs. She's rebuilding on Fedora after leaving Arch-ecosystem CachyOS. Ty clarifies his platform consolidates $50k of subscriptions for his Bahamas companies, tailored to local regulatory compliance.
-->

<Q>Lisa Jetton (new member): looking at Ty's app, what is the broader vision — a brokerage space, AI-built infrastructure, funnel pairing, an à-la-carte model? What AI is under the hood and what's the goal?</Q> <A>Ty: it's for one of his companies in the Bahamas (eventually both) — it replaces $50,000 in subscriptions across five to eight separate tools, consolidated into one platform, launched today to their business clients, and is purpose-built for Bahamas regulatory compliance that US/European/Canadian software doesn't meet.</A> Lisa notes that explains "The Island" branding; Patrick praises the niche.

Lisa's introduction: Austin, Texas; full-stack software engineer, eight years in distributed computing and P2P — systems adjacent to blockchain, built on [tool:Holochain], a 2D hash graph rather than a 1D hash chain. She left her job months ago to build backend agentic systems for her husband's construction company, aiming to abstract them into a service for local small-to-medium companies. She joined this community seeking technologically grounded peers beyond the hype.

She's also rebuilding a device from the ground up: leaving the Arch Linux ecosystem (CachyOS) — concerned that Omarchy's arrival adds noise to an under-vetted ecosystem — for a Fedora build, deciding how tightly to couple AI systems into the new OS. She's also slightly sick: "The North American bug is real."

---

<!--SEGMENT
topic: Home lab and Hermes agent setups
speakers: Patrick Chouinard, Lisa Jetton, Paul Miller
keywords: Proxmox, Linux, LXC containers, VMs, Mac, Hermes agent, Raspberry Pi, AI DevStack, smart TV, remote management, router
summary: Members describe their personal infrastructure: Patrick runs three Proxmox servers with Linux VMs and LXC containers orchestrated by a Hermes agent, and Paul set up a Raspberry Pi at his mother's house as a router/media server for her smart TV, managed remotely via his AI DevStack. Lisa expresses enthusiasm for Hermes as an essential tool.
-->

Patrick Chouinard: I'm running a small platform personally to have fun with. I have three Proxmox servers running a list of Linux VMs and also LXC containers on them. So I don't try to attach to a single OS platform. The only thing I no longer have at home is Windows — Mac is the workstation, and Linux is my backend running on multiple Proxmox servers. And all of that is operated by a Hermes agent.

Lisa Jetton: Hermes is like a must for me. I love Hermes. I was very happy to have found her a few months ago.

Paul Miller: I've jumped into managing a Pi from my AI DevStack because my mother has a whole lot of old videos and CDs, and I wanted to create an easy way she could play them from her smart television. So I set up a little Pi to be a router and route that back to one of the servers I'm hosting, but it's remotely managing the Pi in her network, so I can do remote support without having to drive over and fix stuff all the time. Controlling that Pi stack has been quite cool with the AI Dev side.

---

<!--SEGMENT
topic: AI harnesses and T3 stack discussion
speakers: Lisa Jetton, Paul Miller, Patrick Chouinard
keywords: harness, T3 stack, Shipkit, Claude subscriptions, OpenAI, orchestrators, Theo, T3 Chat, T3 code servers, ECC, Pi, skills, markdown
summary: Lisa asks the group which AI harnesses and toolkits people prefer as she rebuilds her setup from the ground up. Paul describes moving from Shipkit-style markdown skills to the T3 stack with multiple Claude and OpenAI subscriptions managed by orchestrators, and Patrick shares his dev/staging/prod T3 code server architecture with walled-off environments.
-->

Lisa Jetton: <Q>I'm curious what harnesses people use, what setups. I'm trying to build from the ground up. I'd be open to feedback on favorite harness toolkits, maybe even ECC, and ways you've found efficiencies to navigate different competencies and coordinations.</Q>

Paul Miller: A lot of us have been using the Shipkit product — it seems like a generation ago, about last year. Every month seems like a year in AI. A lot of us built a lot of understanding of skills from following that path, because that was made up with a whole lot of markdown data. We've all been converting across, but I'm using the T3 stack now and loving it, because I've got multiple Claude subscriptions and OpenAI, using them simultaneously with orchestrators that manage my program of work across all the applications, then a project focus for each application stack set up in T3. That helps me keep so many concurrent projects aligned. ▶ Good on Theo with T3 Chat — that's certainly made things a lot easier with multiple subscriptions going. [tool:T3 stack] [tool:T3 Chat]

Patrick Chouinard: I'm also a fan of T3 code. Paul, did you deploy some of the T3 code servers, or just have it installed on your workstation?

Paul Miller: I'm about to — I've got my Mac mini and my Linux home servers. I'll do my day stuff on my Mac, and process overnight or slower tasks on a box with a GPU.

Patrick Chouinard: ▶ What I've done is split the security frontier of each: a T3 code server for the dev environment, one for staging, and one for prod. They can't work against each other — the only thing they can do is talk to each other. My dev server can talk to a session on staging to deploy from GitHub, and when staging finishes, it calls up the session on prod to do the deployment. The server instances are completely walled in from each other, but everything works through T3 code on my Mac. And each of them has both Claude Code and Codex. I'm starting to play with Pi to make it a specialized harness since it's completely open source — I want to make it a specialized harness for code review across the board.

Lisa Jetton: <Q>Have you dabbled with ECC and compared that with Pi at all?</Q>
Patrick Chouinard: No, I haven't.
Lisa Jetton: People usually do one or the other, and I'm wanting to find someone who's done both for a comparison.

---

<!--SEGMENT
topic: Hermes memory, OnShow, and Agent Ops plugin
speakers: Lisa Jetton, Patrick Chouinard
keywords: Hermes, skills, self-learning, dynamic memory, OnShow, tokens, Agent Ops, MCP servers, infrastructure monitoring, network operator, context bloat
summary: Lisa asks whether others tune Hermes' implicit learning and self-adaptation settings, noting potential context bloat from ephemeral tasks. Patrick explains he uses OnShow as a dynamic memory layer (very cheap, $100 free credit lasting months) and built an "Agent Ops" add-on with API, infrastructure documentation, and MCP servers to monitor his whole network.
-->

Lisa Jetton: <Q>Have you guys played with configuring or changing the skills Hermes has implicitly about its learning techniques or self-adapting techniques? It acquires context from whatever you write without explicit orders to adapt. Sometimes it can lead to a little bloat if you're doing focused but ephemeral tasks in sequence. Have you tried playing with that, or are you happy with defaults?</Q>

Patrick Chouinard: I've used OnShow as my dynamic memory layer. It has the basic memory, but it also uses OnShow. Honestly, it's a paid service, but when I created my account it gave me $100 worth of tokens — that was six months ago and I think I still have $79. It's really dirt cheap, and it's running every single day nonstop. A refreshing moment by comparison to everything else. [tool:OnShow]

▶ On top of that, I've created an add-on I call Agent Ops — a full plugin with an API, full documentation of my entire infrastructure, plus a couple of MCP servers and tons of skills to leverage those MCP servers to basically monitor everything going on. It's my network operator. [tool:Agent Ops]

Lisa Jetton: That's well thought out. I'll be back with feedback next week on what I chose to go with.

Patrick Chouinard: Once a month, Brendan Hancock, the original creator of the group, joins us. He's not here full time right now because he's starting a business, but he tries to be here at least once a month, and there's normally a lot more people on these days.

---

<!--SEGMENT
topic: Ryan's project updates — estate agency site and fitness app
speakers: Paul Miller, Ryan C (One Stop Creative Agency - UK)
keywords: OBS camera, Fable, Claude 4.8, Claude 5, estate agency website, CRM, SEO, Hermes telephone calls, fitness app, Mac, iPhone, watch app, calorie tracking, CC Black Box, Higgsfield
summary: Ryan reports he exhausted his Fable usage and downgraded to 4.8 because he dislikes 5. He launched an estate agency website with a CRM backend that is already outranking century-old competitors in local SEO, added telephone capability to his Hermes agents, and built a Mac/iPhone/watch fitness app three-quarters complete. He also recommends Scott's CC Black Box IDE (ccblackbox.app) and mentions experimenting with Higgsfield for video/image generation.
-->

Ryan C (One Stop Creative Agency - UK): I'd love for my video to be working, but my only option is OBS camera, which is entirely useless. I've blasted through all my Fable usage on both my accounts, and I'm back to having to downgrade myself to 4.8, because I just can't get on with 5 at all. I've tried changing skills — it's just dumb. I hate it. So I'm back on 4.8 and it seems to be working fine.

I launched an estate agency website with a full back-end that acts a bit like a CRM for them to manage their properties, and it's been ranking above estate agents SEO-wise that have been around for 100-plus years. I've managed to get them above them for the local area within a week or two of launching, which is quite good. They're very happy and getting leads coming through already versus their old website, which got them nothing.

Scott and I have added telephone ability to our Hermes agents, so I can now make calls to people and organise my life for me. We tested it by getting her to ring my dad — it was an entertaining listen to the phone recording after that.

Then I decided I needed to get back into shape, went to the gym for the first time in two weeks, and thought — can I make myself a full application that teaches me how to do that? So I built a Mac, iPhone, and watch application that tracks everything, including meals and food — you can literally take a picture of what you're eating and it will guesstimate calories. I'm about three-quarters of the way through building that, which has been the last week, and I've not been to the gym since.

I've been using Scott's CC Black Box IDE — it's got all the simulators built in, so it can drive the simulator within the thing. He's open-sourced it and has a little website going, ccblackbox.app. Mac only, but if anybody wants to drive their Claude stuff off a Mac, it's a better view and feels nicer than Cursor or VS Code. [tool:CC Black Box] [link:ccblackbox.app]

Absolutely avalanche of video and photo stuff because it's busy season for an estate agent. I've also been playing around with Higgsfield on the video generation and image generation side. [tool:Higgsfield]

---

<!--SEGMENT
topic: Morgan's update and group reflection
speakers: Paul Miller, mdcatc, Patrick Chouinard, Ryan C (One Stop Creative Agency - UK)
keywords: Fable 5, GPT-6, $20 Pro subscription, rapid prototyping, agentic work, away-from-keyboard, projects portal, context upgrade, community
summary: Morgan shares that client work keeps him busy but he's enjoying Fable 5 despite occasional quality drops. He only has a $20 Pro subscription, hasn't tried GPT-6 yet, and is still building his away-from-keyboard agentic processes. He reflects on the speed of rapid prototyping versus rapid trashing, and agrees to clean up his personal projects portal. Patrick notes the group is his weekly "context upgrade."
-->

mdcatc: I've been really busy with clients' work, so no new stuff to show, but I have been enjoying Fable 5. It's amazing some of the stuff it does, and then every once in a while it's like, what happened?

Paul Miller: Are you dancing with the GPT-6 as well?

mdcatc: No, not yet. I don't have a $100 subscription, but I do have the $20 Pro subscription, so I was going to play with it for some small stuff. I'm not burning through the whole thing yet because I have so many other things on my plate — I don't have all my processes in place for agentic away-from-keyboard work. Still slowly building that up.

I had a friend I talk to every six months ask what I've been doing, and I started listing off all my projects and sending links to my little websites. He said, damn, you've been busy. I said, that's not even all of it — that's just the stuff that's visible. There's a lot of work that's been done that's already been thrown away. The speed of this stuff is so far past where we were five years ago. Rapid prototype, rapid trash.

Patrick Chouinard: ▶ You need to create the "World of Morgan" portal so we can see all your work in a single place. Tell Claude to use design to give it a facelift.

mdcatc: I do have one, but the portal that's out there right now is not anything I want looked at. I'll work on cleaning it up — it's been on my mind for a month and a half.
ACTION ITEM: Clean up and update personal projects portal

Patrick Chouinard: ▶ There's too much for a single person to be aware of all the time. This group is basically how I do my context upgrade every week.

---

<!--SEGMENT
topic: Paul's visual ML shelf-recognition project
speakers: Paul Miller, Patrick Chouinard
keywords: visual shelf recognition, machine learning, consumer goods, Israeli company, open source, visual LLM models, fine-tuning, orchestrator, training data, Mac Mini, GPU pod, self-training
summary: Paul describes reinventing his 12-year-old visual shelf-recognition software project (originally built with an Israeli partner for a large US cola manufacturer). Using open source visual ML combined with visual LLM models and an orchestrator, he can now automate the fine-tuning and training-data-gathering process that previously required low-cost manual labeling — running comparisons across models on his Mac Mini or cloud GPU pods.
-->

Paul Miller: I've been working away at a software project for pretty much the last 12 years. It came out of an initiative I did with a very large cola manufacturer based in the eastern side of the United States that has a red logo — that's about as much as I can say. The core of what they do, and a lot of companies in the consumer goods space, is visual shelf recognition in supermarkets and retailers of what products are on shelves. The technology is more machine learning than AI, and I'd partnered with an Israeli company to use their technology with that customer.

Now, there's so much open source content out there in the visual learning, machine learning side that if you mix it up with using the LLM models, I'm able to retune and use some of the visual LLM models to look at how I can automate the fine-tuning process and the gathering process of doing the training. In the past, you would get people in low-cost countries to help program the image models, using identification tools to submit images for training — but now you can throw cheap visual LLM models at all of that work and self-train it with an orchestrator.

I've been doing that in the past week and my goodness, it's pretty impressive. It's been able to come up with much more advanced machine learning models for shelf recognition purely off an open source stack, then compare all the different models on how good they are, and find ways to do all the fine-tuning — whether running on my spare Mac Mini or throwing it up on a GPU pod in the cloud. It's a project I've been doing over the last 12 years, and it's been quite a good one to try and reinvent without having to pay these third-party vendors. ▶ Open source visual models plus LLM-driven orchestration can replace paid third-party visual ML vendors for training and fine-tuning workflows.

Patrick Chouinard: Anyone else have anything to contribute? Any questions before we call it a day? Going once, going twice. Sold. Thank you very much, everyone, and thank you for keeping up with your two handicapped moderators today. We'll try to be in better shape next week.

=== UNRESOLVED SPEAKERS ===
- Rod Morrison
- Lisa Jetton
- Ryan C (One Stop Creative Agency - UK)
- mdcatc