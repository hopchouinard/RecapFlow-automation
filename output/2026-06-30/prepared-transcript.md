=== SESSION ===
date: Unknown (Tuesday evening, exact date not provided)
duration_estimate: ~2 hours 27 minutes
main_themes: AI-powered hardware gadgets and wearables, voice-driven coding workflows, homelab automation and agent orchestration, SaaS go-to-market strategy and cold outreach, AI-assisted code review pipelines, event-tech hardware business models, sub-agent efficiency tooling

---

<!--SEGMENT
topic: Session Open and Introductions
speakers: Ty Wells, Paul Miller, Patrick Chouinard, Ryan C, Brandon Hancock
keywords: meeting recording, group check-in, Brandon Hancock return, AI community, weekly update format, stress and creativity, social week, catch-up
summary: The session opens with casual greetings and confirmation of recording. Brandon Hancock rejoins after an absence and sets the agenda: sharing personal AI project updates and hearing from the group. The segment establishes the collaborative, show-and-tell format of the meeting.
-->

[00:00:06] Paul Miller: This meeting is being recorded.

[00:00:10] Ty Wells: Do we get a sighting today of Brandon?

[00:00:24] Patrick Chouinard: We are supposed to see Mr. Brandon today.

[00:00:30] Ty Wells: How are you doing, Patrick?

[00:00:33] Patrick Chouinard: Surviving.

[00:00:43] Patrick Chouinard: It seems that the more stress I'm under, the more creative I become.

[00:02:11] Ryan C: Evening.

[00:02:46] Brandon Hancock: How's everybody doing? Happy Tuesday, everybody.

[00:03:02] Brandon Hancock: I know Paul, we've got to catch up tomorrow too at some point. I've got to send some stuff over. I talked to Patrick yesterday, so it's a social week. I'm liking it. But what I'd love to do today is give you guys some cool updates of what I've been doing, and then would love to go and hear what you guys have been up to too, just so we can see what's all going on in the AI land.

---

<!--SEGMENT
topic: Smart Glasses and Wearable AI Gadget
speakers: Brandon Hancock, Ryan C, Ty Wells, Paul Miller
keywords: smart glasses, Claude Code, Codex, Limitless, Meta glasses, ring controller, prescription lenses, wearable computing, voice coding, productivity gadget
summary: Brandon Hancock announces he purchased a pair of AI-enabled smart glasses featuring a built-in display and microphone (no camera), with integrations for Claude Code and Codex. The glasses also perform real-time meeting transcription and contextual fact-surfacing similar to Limitless. The group discusses the productivity implications of hands-free, voice-driven coding and the prescription lens limitation.
-->

[00:03:31] Brandon Hancock: So first off, I want you guys — y'all know I love a good gadget, so I'm going to drop it in chat.

[00:04:06] Brandon Hancock: So they're smart glasses where they have a display built in. They don't have a camera. They just have a microphone. And so for code addicts like us, what they do that's super cool is they have integrations with already existing tools. And you can make your own apps. So they already have additional apps out like Claude Code [tool:Claude Code], Codex [tool:Codex]. So literally with your glasses and this little ring thing, you could just at any point talk and be like, pick up a session that you were working on and just answering questions. And then whenever it's done, it just dings you like, hey, code's done. What do you want to do next? So it's like unlimited productivity.

[00:05:00] Brandon Hancock: I know a lot of us got like Limitless [tool:Limitless] and Plod and all sorts of other things, but because it's already glasses with a microphone, it just does what Plod does. So as you're talking, it'll record speaker A, speaker B, speaker C, do all the normal summarizing and everything. But what's also cool is if the person says something that you might not know, it'll just give you like a little blurb like, oh, you know, the capital of this — it'll just show highlights. So it feels like you're cheating in real life.

[00:05:44] Brandon Hancock: It has everything that we have looked at in the past between like Meta [tool:Meta glasses], Plod and everything else. And it's all in one. It'll translate for you. I saw a guy build an app so he could control his Tesla from it.

[00:06:03] Ryan C: Do you just like spending my money at this point, Brandon? Come on.

[00:06:13] Brandon Hancock: How do you justify it as a business expense?

[00:06:24] Brandon Hancock: I will be living inside these things with Claude Code pretty much 24/7.

[00:16:46] Ty Wells: <Q>Can you get prescription in those?</Q>

[00:16:48] Brandon Hancock: <A>That's the only issue. It comes with like a little ring around your finger. So you can just scroll and like, oh, I want to go to this session or I want to do a new session. The only gotcha is they don't do both. They only help you see far away. They don't do the reading thing.</A>

---

<!--SEGMENT
topic: Ty's GPS-Limitless Device Tracker App
speakers: Ty Wells, Brandon Hancock, Ryan C
keywords: Limitless, Garmin GPS, Bluetooth, BlueFi, AirTag, golf, lost device, app development, GPS cross-reference, Omni pendant
summary: Ty Wells recounts building a custom app on the fly to locate his lost Limitless wearable pendant during a golf round. He cross-referenced Garmin GPS data with Limitless life-log timestamps to pinpoint the device's last known location, then used Bluetooth ranging in the browser via BlueFi to navigate to within five feet of it. He lost the device again the very next day and used the same app to recover it a second time.
-->

[00:09:32] Ty Wells: I told the guys I had a story I wanted to tell. So on Sunday I golfed, and I have my Limitless [tool:Limitless] device — I have it on now — and I lost it during golfing.

[00:10:02] Ty Wells: So I came home and I wrote an app that took my Garmin [tool:Garmin] GPS data and took the life logs from the Limitless, cross-referenced the time to tell me when the last message came in, and then I used the GPS. So I went out back on the course that night, on Sunday night, using my home-built AirTag [tool:AirTag-equivalent], if you will — just tracked it and told me 17, 16, 15, you know, 10 feet. I was in five feet and the guy who drove me out there from the clubhouse said, is this it? I showed him a picture. He's like, I think I got it.

[00:10:49] Brandon Hancock: What you need to do is tag Limitless and Garmin in a post because someone's going to see that and be like, that's freaking awesome.

[00:11:05] Brandon Hancock: The fact that you did that is like some detective work, man. Like, most people would just be like, oh, damn, it's gone. The fact that you're like, oh, my Garmin tracked me to within a couple meters, and I can replay this back — dude, you should have been in the CIA.

[00:11:51] Ty Wells: So I started the GPS once I got close to hole five. And then I started the Bluetooth thing running through BlueFi [tool:BlueFi] because it runs in the browser. BlueFi will run Bluetooth devices within it.

[00:12:40] Ty Wells: On Monday I couldn't wait to tell the guys I played Monday again. So on the first hole I hit, I go to the second hole and I touch my chest and it's gone. I lost it again on the first hole. So I used the same app to go find it again. I found it. They're like, Ty, at this point we know you're just dropping it so you can look cool.

▶ [00:13:08] Ty Wells: Yeah, I'm going deep to try to get this done, because obviously I wanted it. It was a problem. I had to solve it.

---

<!--SEGMENT
topic: Ty's Golf Tee Time App and Voice Coding Agent
speakers: Ty Wells, Brandon Hancock, Ryan C
keywords: golf tee time app, Proxmox, LiveKit, voice coding, AI agent, pull requests, GitHub, mobile coding, phone interface, secure token preview
summary: Ty demonstrates two additional projects: a golf tee-time aggregator app called "Omaha Tea Times" that scrapes local courses and links directly to booking pages, and a voice-driven coding agent running on his Proxmox home server via LiveKit. The voice agent gives him full coding capability — including creating PRs and accessing repos — entirely through his phone, eliminating the need to open a laptop.
-->

[00:13:23] Ty Wells: Can you guys see this? It says Omaha Tea Times. This is another app I'm building just for us, for my golfing buddies, where they can come in and choose a day, and it'll scan — it's scanning all of the actual courses that are in town, pulling up and showing you the availability as you mouse over. And then you can click, and then you book directly.

[00:13:57] Ryan C: Put yourself on an affiliate scheme there, Ty.

[00:14:16] Ty Wells: This is what I talked about last week — the ability for me to talk to my code. So I built this agent that runs on my Proxmox [tool:Proxmox] that does everything that I wanted to do. I get in a LiveKit [tool:LiveKit] session and it's as if I'm right there with the code.

[00:15:17] Ty Wells: I just have a room open, I talk to it, it has access to everything as if I'm in a code session, but it's not giving me code back. I'm iterating like you would talk in ChatGPT [tool:ChatGPT] voice mode, except it can access my repos, it can create PRs, it can do anything I can do as if I was in front of my computer.

▶ [00:15:41] Ty Wells: This is the way to go. This is the only interface I will be using moving forward. So there's going to be a lot more golf in my future — I literally do not have to open my laptop. I can have it do whatever I need it to do.

[00:16:00] Brandon Hancock: I feel guilty if I'm not using AI. Like, I'm wasting tokens. I could be doing something. I hate if AI needed me for two seconds and then it was going to go on a tear for another 45 minutes. If I'm not there to respond, it's just like, damn, I wasted 45 minutes.

[00:17:20] Ty Wells: The unique thing about it is when you're building something, you need to see what it looks like. So I have it generate a secure token to show me the preview that I can look at right on my phone, and then I can go back on. It only opens in Safari, but other than that, it works just fine.

---

<!--SEGMENT
topic: Brandon's EMS App Business Updates and Cold Outreach Strategy
speakers: Brandon Hancock, Dave Gottschalk, Juan Torres, Paul Miller
keywords: EMS app, HIPAA compliance, cold outreach, Loom video, Yesware, PE firm, pipeline, ambulance companies, customer discovery, Instantly, feedback loop
summary: Brandon Hancock shares business milestones for his EMS documentation SaaS: a second app version shipped, HIPAA compliance achieved, a conference booth with $100K+ in pipeline, and an upcoming PE firm meeting about distribution and acquisition. He then details his cold outreach playbook — using Claude to research prospects city by city, recording personalized Loom videos with ROI estimates, and using Yesware for email tracking — and explains the iterative feedback loop of incorporating customer language into subsequent pitches.
-->

[00:06:55] Brandon Hancock: So big thing — we are finally getting a bunch of traction for our app. We've built a whole second version of our application, HIPAA compliance through the full nine yards, we went to a conference, actually hosted our own booth, we were giving out coffee, books, everything, and we actually booked a ton of demos. Pipeline is like $100,000 of deals.

[00:08:00] Brandon Hancock: We've now just understood what our customers want. We're starting to do some cold direct DMs, just recording Loom videos, and it's actually working, because we finally can articulate the customer's problems better than they can.

[00:08:24] Brandon Hancock: We finally talk with a PE firm tomorrow about half doing distribution for us, and eventually buying us. So we have a huge pitch deck that I have to get done after this call tonight.

[00:20:05] Brandon Hancock: What I do, at least what I'm actively doing right now for direct outreach, is I'm using Claude [tool:Claude] to go city by city, because I know exactly where my customers are. They're private ambulance companies, hospitals, or fire departments. So it's very easy to find these people and allow Claude to discover who's the chief, who's the owner. So I can easily find my customers and research them, which is a cheat code.

▶ [00:21:00] Brandon Hancock: I try to put in as much effort and as much value into each direct outreach as possible to improve the likelihood that they just open the door. I'm not a big fan of Instantly [tool:Instantly] because it's just shooting like a thousand bullets at the wall and maybe something hits. I would much rather be like a sniper — reach out to each person with max value, because I don't want to burn through my whole customer base.

[00:22:00] Brandon Hancock: It would be like, hey, Zach, hope you're having a great day. My name is Brandon Hancock, co-founder of EMS. We help transport units just like yourselves reduce their QA overhead and 10x their reimbursement rate. And what I'd love to do in this video is just show you exactly how we work, make it easy for your crews, show you the proof and results of other agencies just like you, and then show you some estimates on how much money we believe we could save for your agency.

[00:23:44] Brandon Hancock: You send the direct outreach, have the conversation, pull out the keywords that they said, throw it into the next iteration, and it just has a feedback loop where every time I pitch, I'm pitching stronger because I'm using their words back to them.

[00:24:10] Brandon Hancock: It's called Yesware [tool:Yesware]. They basically allow you to track everything that gets sent out. You get to see who opened it, when they opened it. Did they click the link? Did they not? It's like some spy-level stuff. [link:Yesware email tracking tool]

▶ [00:24:38] Brandon Hancock: It does take the product working and some social proof, but you only need one success story to start the flywheel.

---

<!--SEGMENT
topic: Dave's Data Ownership Platform and Go-to-Market Discussion
speakers: Dave Gottschalk, Brandon Hancock
keywords: data ownership, Payback Owned, advertising invitations, data portability, two-sided marketplace, content creators, media consumption, go-to-market strategy, Udemy comparison
summary: New attendee Dave Gottschalk introduces his startup "Payback Owned," a platform for personal data ownership where users aggregate their online data, receive paid advertising invitations from marketers, and use earnings to pay directly for ad-free content at roughly a penny per minute. Brandon offers go-to-market advice, drawing parallels to two-sided marketplace playbooks like Udemy, and suggests separate outreach tracks for creators versus advertisers.
-->

[00:19:01] Dave Gottschalk: Sure. Great meeting you guys. I'm building a new thing. Going to market, similar to sounds like what you're going through, Brandon. So that was my question — cold outreach, trying to tell people about what your thing is.

[00:27:28] Dave Gottschalk: We're in the phase right now where data is the most valuable thing on the planet and we give it all away. So I'm building the data ownership economy where people own and control all their online data. Everything that currently makes money with data, now you make money with that data.

[00:28:03] Dave Gottschalk: Privacy is defense. Ownership is offense. So when you own your data, you port it out — you bring it into my thing called Payback Owned [tool:Payback Owned], and you merge it all together into one account that you own and control, and you have it forever, it gets better every day, and now you have a whole new economy based on it.

[00:28:45] Dave Gottschalk: Anytime a marketer wants to talk to you, they invite you. It's a new category of advertising called invitations. So I invite you, if you engage, I pay you. Now you take that money over to the media side, and you say, hey, now I'm going to pay content creators directly for stuff that I consume. So it's all ad-free, I pay for consumption, no subscriptions, whatever you engage with, that's what you pay for.

[00:29:29] Brandon Hancock: This is a two-sided marketplace. You might have two separate email pitches — pitch one is to invite the creators, and then pitch two is like, hey, I have this valuable data that you could use. I would be following the playbook of Udemy [tool:Udemy], any video course platform — their go-to-market strategy I would really look at emulating.

▶ [00:31:17] Dave Gottschalk: We can build the rails and finance everything at about a penny per minute. So if you go on Reddit or YouTube or whatever, you pay a penny per minute. You earn at about a dollar per minute on the other side. So most people would be interested in that.

---

<!--SEGMENT
topic: Infrastructure Stack and Web Scraping Ethics
speakers: Juan Torres, Brandon Hancock
keywords: Supabase, AWS, Google Cloud, Gemini, Claude Haiku, Claude Opus, RAG pipeline, HIPAA, SOC2, Apify, web scraping, public data, ShipKit
summary: Juan Torres asks Brandon about his infrastructure choices. Brandon explains his stack: Supabase as the core backend with HIPAA/SOC2 add-ons, AWS strictly for Claude model access, and Google Cloud for Gemini and backend jobs. Juan then raises the issue of Claude models refusing web scraping tasks on ethical grounds; Brandon notes Claude Haiku has been permissive for public data while Opus is more restrictive, and describes using Apify as a tool call within his Claude agent for LinkedIn lookups.
-->

[00:31:54] Juan Torres: <Q>Hey, Brandon. What did you decide to use for your infrastructure at the end of the day?</Q>

[00:32:00] Brandon Hancock: <A>Dude, same thing that we did in ShipKit [tool:ShipKit]. It is Supabase [tool:Supabase] as the core backend. The main thing that is an addition is we have AWS [tool:AWS] and Google Cloud [tool:Google Cloud], but AWS is strictly just so we could use models like Claude. That's really all AWS is there for. And then when it comes to Google Cloud, it's so we can access Gemini [tool:Gemini], but we also use Google Cloud to run some backend jobs. Very similar to the RAG pipeline in ShipKit.</A>

[00:32:46] Brandon Hancock: Supabase does charge you a pretty penny to get all of these HIPAA, SOC2 things — they're all add-ons. So every time you click a new button, they're like, that's $300 a month. That's $400 a month. But it is very easy.

[00:33:09] Juan Torres: <Q>Did you have any problems with the web scraping? Because I do remember trying to indicate to Claude Code web scraping for particular clients in an industry, and it was saying, oh, I cannot collect their emails. That's a permissible kind of deal.</Q>

[00:33:27] Brandon Hancock: <A>What I do — I'm not doing this at mass. I have a skill that I have on my local computer. And every time I want to reach out to a new area, I have a state. A state has cities and counties. And then within those, there's private ambulance companies, fire departments, and everyone else. It doesn't even have to get it perfect, because we also have something with Apify [tool:Apify], where the second I find a few guys' names, if their information is not there, it just has some Apify tokens that does like a LinkedIn scrape. It's a tool call, basically, for my agent. So it's all done through Claude. I would use Haiku [tool:Claude Haiku] to do most of it.</A>

[00:34:35] Brandon Hancock: Opus has done weird stuff in the past — Opus is like a stickler. Haiku, I have not run into any issues with that. And I think it's all public data, too. So it's not even like I'm trying to be weird. It's just like, what's the website say?

---

<!--SEGMENT
topic: Paul's CTO AI Adoption and Legacy Code Modernization
speakers: Paul Miller, Brandon Hancock, Patrick Chouinard
keywords: legacy code, technical debt, C-sharp, iOS Android, Claude, Codex, Supabase branching, sandboxes, staging environment, code review bottleneck, LanceDB, knowledge base
summary: Paul Miller reports that his CTO has fully embraced AI development tools and is using Claude to audit legacy C# and mobile codebases, extract technical documentation, and establish a clean baseline for future platform development. Brandon advises on managing the resulting 10x increase in code output by implementing Supabase ephemeral branches as sandboxes, standardizing the sandbox-to-staging-to-main merge pipeline, and building automated tests to prevent the reviewer from becoming the new bottleneck. Paul also mentions building a searchable knowledge base using LanceDB for retail audit data.
-->

[00:35:17] Paul Miller: Our CTO is fully AI, really into everything now.

[00:35:44] Paul Miller: He's a real Claude man. He probably needs to move to Codex, but look, we take the wins. Baby steps.

[00:35:58] Paul Miller: He's rewriting all of our legacy code. So he's going through everything. He is extracting technical documentation out of it so he can build a vision for the next version of the platform. We've got a lot of stuff written in C#. We've got the server components. We've got native field apps because we've got iOS and Android stuff. He's going through the whole lot.

[00:36:48] Paul Miller: The good thing is I don't have to worry about that as much. I can focus now back on the selling, and customers that have asked for new features are happening really fast now.

[00:37:00] Paul Miller: Patrick, you had your project the other day — you were doing some stuff with LanceDB [tool:LanceDB] in terms of organising information and things. One of our base company's natures is we have a lot of data in which people have captured notes or discussions or audits of retailers, and it's in all sorts of formats. I'm trying to build that so it's a lot more searchable and usable.

[00:38:14] Paul Miller: What I'm trying to do is have a comprehensive knowledge base that is a mixture of agentic searching, old-fashioned RAG, upgraded RAG with re-sorting, and then testing it constantly for needle-in-a-haystack and bigger trends as to what's happening.

[00:43:31] Brandon Hancock: The one thing I was going to mention that we have done to help us sleep better at night is: new features are going to come in. The old way — human way of doing it — is people are the pipeline. So because it takes so long to build out, the review also takes probably equally as long. So it's just a one-to-one ratio. But what happens now that your CTO is about to find out is it's like 10 to 1 — meaning we're going to do 10 times the amount of work, but we still only have so many review hours. So now the reviewer becomes the bottleneck.

▶ [00:44:22] Brandon Hancock: We have sandboxes for everything that we do. Anytime we build a new feature, it's a throwaway thing — it's literally in its own environment. We have it build its own tests. If the AI completely destroys the database, so be it. Really embrace doing separate environments that are spinoffs.

▶ [00:45:58] Brandon Hancock: For ours, every time we create a new sandbox for a new feature, it's a Supabase [tool:Supabase] branch — we basically make a branch that's ephemeral, meaning as soon as the work tree is done, it deletes automatically. So we're not paying $20 a month — it's up for two days and it's gone, cool, we paid $2. We just seed it with as much real-life-looking data as possible to where every time you're working on something, it feels like you're working on the app, not just a shell of the app.

---

<!--SEGMENT
topic: Patrick's AgentOps Homelab Automation System
speakers: Patrick Chouinard, Brandon Hancock, Scott Rippey
keywords: AgentOps, Hermes, Proxmox, MCP, Cloudflare Pages, Hostinger, Infisical, NATS, enterprise service bus, Authentic, Docker, Claude Code, Codex, GitHub PR review, LoopForge, ChatGPT MCP
summary: Patrick Chouinard presents AgentOps, a comprehensive homelab management harness built on top of his Hermes agent. It uses MCP CLI scripts to control Proxmox VM/container provisioning, a Traefik reverse proxy, Authentik authentication, and Infisical for secrets management. He also describes a one-shot deployment skill that publishes documentation sites to Cloudflare Pages with automatic DNS via Hostinger. Additionally, Patrick is building LoopForge — a pipeline that converts conversational intent captured via a ChatGPT MCP into structured GitHub issues, which are then processed into detailed prompts for long-running Codex agent goals. NATS serves as the homelab's internal message bus.
-->

[00:47:00] Patrick Chouinard: As I said earlier, stress is making me more creative. My Claude Code [tool:Claude Code] is my way to relax — I have it still coding right now, actually.

[00:47:43] Patrick Chouinard: The one thing I've worked on last week was my front-end for AgentOps [tool:AgentOps]. AgentOps is a harness that I'm building on top of Hermes [tool:Hermes] in order to manage my home lab. So basically, what it does is it's a set of MCP [tool:MCP] CLI scripts, and a bunch of connectors to hook onto all of my homelab services, and it uses the homelab itself as its nervous system. Hermes is on one VM running on Proxmox [tool:Proxmox], and Proxmox is behind a Traefik reverse proxy, which gets authenticated using Authentik [tool:Authentik].

[00:48:47] Patrick Chouinard: It hands control to a Hermes instance — the ability to spawn new VMs or new containers on Proxmox, connect to an existing VM that is defined as a Docker [tool:Docker] host to spawn new containers inside of it. It can create new entries in the reverse proxy. It can create new authentication in Authentik. And all of this security is managed through a secret management system called Infisical [tool:Infisical]. So it's the poor man's version of a vault, basically.

▶ [00:49:39] Patrick Chouinard: Now, anytime my agent needs to access an API key for anything, it doesn't use its own ENV file. It actually asks Infisical to give it access. And Infisical is there to do all the key rotation and all of that. So basically, my lab is alive now.

[00:50:00] Patrick Chouinard: I realized that I was documenting everything I was doing in the form of a website. My main domain is controlled by Hostinger [tool:Hostinger]. And then I create subdomains for every project that I have, but those projects are hosted in Cloudflare [tool:Cloudflare Pages] as Cloudflare Pages. So I wanted a way to just tell Claude Code, "publish this." And it would create the project on Cloudflare, go and do the DNS CNAME on Hostinger, bind everything, upload the thing — one shot.

[00:51:27] Brandon Hancock: <Q>So going from raw code to website, obviously there has to be a middle step somewhere that's automating the creation of this white paper — is that just a part of your CI pipeline?</Q>

[00:51:47] Patrick Chouinard: <A>Not yet. Right now, it's pure conversation. I'm just chatting with Claude. And honestly, Claude memory has improved a lot recently. Now when I talk about creating a documentation site out of a project, I've done it enough times that it knows exactly what I want.</A>

[00:53:03] Patrick Chouinard: While I build with Claude, I have Codex [tool:Codex] and Copilot [tool:GitHub Copilot] that monitor my GitHub repos. And now as part of my loop, I ask Claude Code to monitor every PR for half an hour — to give the time to Codex and Copilot to post their analysis. And I tell them to automatically reply and resolve the issues that are found by the code reviewer.

[00:54:32] Patrick Chouinard: The first one is what I told you about the LoopForge [tool:LoopForge]. I created a tool that allows me to take a raw intent statement and convert it into a slash-goal prompt to be given to the other system to implement — to run long-running operations. The problem is I talk to ChatGPT all the time, like every single minute of the day, so a lot of the ideas are pieces of a conversation. I didn't want to lose that.

[00:55:21] Patrick Chouinard: So I'm building an MCP to be deployed through the OpenAI [tool:OpenAI] infrastructure, so it's available to ChatGPT mobile. Whenever I invoke it, it will look at my communication for the last couple of minutes, summarize the intent behind it, and then create a GitHub [tool:GitHub] issue in a specific repo with that intent. That list of issues will be monitored by the LoopForge as a pipeline of incoming stuff. So I will be in my car just like, oh, that's interesting, create an issue with it.

[01:02:35] Patrick Chouinard: All of that communication had to be managed by something. So I needed to build an integration highway of data between all of those that could be consumed by Hermes or myself. And that's a product that I've discovered called NATS [tool:NATS], N-A-T-S. It's basically the personal version of an ESB — an enterprise service bus. It creates a service bus of standardized messages with publish/subscribe implementation. And basically all of my systems are publishing their data. Hermes picks up whatever it needs from it. It reacts. And if it needs to push something back into one of the systems, it just uses the service bus as well. So it's like the circulatory system of the lab.

---

<!--SEGMENT
topic: Scott's Hermes Setup, GitHub Cron Sync, and AI Video Channel
speakers: Scott Rippey, Patrick Chouinard, Brandon Hancock
keywords: Hermes, Ironclaw, GitHub cron job, CLAUDE.md, docs folder, app documentation, YouTube channel, AI avatar, Higgsfield, ElevenLabs, HeyGen, Claude Code, video pipeline, second brain
summary: Scott Rippey shares that he abandoned an Ironclaw build in favor of Hermes after Patrick's recommendation, achieving a better system in two days. He describes a nightly cron job that uses a read-only GitHub PAT to pull all app documentation (CLAUDE.md and docs folders) into a local database, giving Hermes full context of his apps. He also reveals a new YouTube channel where an AI avatar (built entirely in Claude Code) delivers weekly videos combining Higgsfield, ElevenLabs, and HeyGen, debunking AI hype — with the first episode on "second brains."
-->

[00:58:18] Scott Rippey: So I ripped out Ironclaw [tool:Ironclaw]. Brandon, you probably don't know, but last week I jumped on here — I've been working on an Ironclaw build for a while on a Mac Mini, and Patrick sent me down this road and I was like, oh, there it is. I ripped it out and pivoted, and in two days I have a better system with Hermes [tool:Hermes] than I ever did with Ironclaw.

[00:58:55] Scott Rippey: What I did with GitHub was I have a cron job where — with a read-only PAT — I have a way I do my apps where I have a docs folder, and then obviously everybody, if you're in Claude Code, does the CLAUDE.md file. So I actually have something that reads into my database nightly, a cron job, all of my app documentation across customers, so that my Hermes agent actually understands my apps.

[01:00:01] Patrick Chouinard: I've used those tools for one simple reason — I wanted that to work in ChatGPT. To me, that's the easiest way to communicate verbally with any kind of AI. It has nothing to do with the model.

[01:00:08] Scott Rippey: Well, and the fact that we can use OAuth for — local models, like Mac Mini is pretty tough to push the boundaries. Like, you can only do like a 7 billion model. There's not a lot of headroom for context and stuff. So the fact that Hermes legally lets you do chat is killer. I will use GPT-4.5 [tool:GPT-4.5], I will pay a hundred dollars and use it all day long.

[02:00:13] Scott Rippey: Let me share my screen. So you guys see this GitHub? Brandon, you weren't here before for this, but so I started a YouTube channel.

[02:00:42] Scott Rippey: I'm kind of over the hype. Like, all of the AI stuff — everybody's just on these trends. So I created an avatar. And so basically it's like — I spend like an hour at least coming up with the scripts, and it's kind of like thinking like an engineer. The whole video generator thing combines Higgsfield [tool:Higgsfield], ElevenLabs [tool:ElevenLabs], HeyGen [tool:HeyGen] — it kind of combines everything. This whole thing is 100% in Claude Code.

[02:01:00] Scott Rippey: *[plays video clip]* "2,400 years ago, Plato warned that a hot new technology would wreck your memory and leave you with the appearance of wisdom instead of the real thing. He wasn't talking about Notion or Obsidian or some shiny AI app. He was talking about writing — the original second brain."

[02:02:42] Scott Rippey: So I'm just having fun with it because every Tuesday I'm going to release a video, and it's just normally just stuff I'm seeing online because there's so much crap. And I'll put this repo in there — this is kind of like a good little starter for this.

---

<!--SEGMENT
topic: Scott's Google Workspace Telegram Bot and Claude Code Security Review Hook
speakers: Scott Rippey, Brandon Hancock, Patrick Chouinard
keywords: Google Workspace, Telegram, n8n, OpenAI Whisper, voice notes, calendar, contacts, business card scan, Claude Code hooks, Codex adversarial review, Supabase, security review, code quality, CodeRabbit, Claude Opus, Claude Sonnet, false positives, feedback loop
summary: Scott presents two additional tools: a Google Workspace automation via Telegram and n8n that uses OpenAI Whisper for voice-to-action commands (calendar, email, tasks, contacts, business card scanning), and a custom Claude Code pre-push hook system he calls "CodeRabbit on steroids." The hook triggers three parallel review agents — a Claude Opus agent team for code quality, Anthropic's built-in security review on Sonnet, and Codex for adversarial review — storing all findings in Supabase with a dashboard for human-in-the-loop triage. Brandon suggests adding a "lessons learned" extraction step at merge time to build stateful coding memory.
-->

[02:03:26] Scott Rippey: The next thing I'm going to show you guys is a Google Workspace n8n [tool:n8n] flow, where I can basically, in Telegram [tool:Telegram], just anything I want to do with calendar, email, tasks, contacts — I can even take a picture of a business card, and it will make the contact.

[02:04:10] Scott Rippey: This whole thing was built because I was like, if I'm on the go, I've got to be able to just do this stuff quick. So it does the OpenAI Whisper [tool:OpenAI Whisper] thing, because I want to do a voice note to Telegram and have my Google Workspace do the thing.

[02:04:42] Scott Rippey: Now, this is the fun one, Brandon. So I wanted a method of checking for security things every time I pushed a repo, or like I pushed a code change. So this thing basically is a local Claude Code hook that runs agents. The second thing is the security dash review thing from Claude Code, and then Codex [tool:Codex] is the third thing. So I have three models, two vendors.

[02:05:52] Scott Rippey: It puts this all into a database — that's Supabase [tool:Supabase]. And so it's observability. Every time I do a new repo, the first time I push a repo, it will do a whole codebase scan of the entire codebase, but then after that, it's just one-off.

[02:08:08] Scott Rippey: I have an agent team that I built — code quality, security, blah, blah, blah — and that's all on Opus [tool:Claude Opus], because it's plan-based. And then the security agent review is an Anthropic built-in thing. I have that on Sonnet [tool:Claude Sonnet]. And then the Codex is the adversarial review.

[02:10:11] Scott Rippey: Yeah, exactly! Because the thing about CodeRabbit [tool:CodeRabbit] was it was only PR pushes, and I'm like, but I don't do that. Sometimes when you're a solo guy, it's like, I'm not pushing a PR, I just have commits and then pushes, but I'm not actually doing a PR. So that's what — it literally is CodeRabbit on steroids.

[02:11:28] Scott Rippey: So it actually flags stuff in the database and resolves it. So the hook knows to do turn-based style with me. One by one, we go through everything and we figure out if it's real. Is it a fix? Is it a false positive? Is it dismissed? And I track all that in the database, so I can manually do a dismiss or a false positive, and I put the reason why. But the autofixes — it actually does it on its own.

▶ [02:15:16] Brandon Hancock: If I'm not building a feedback loop into my system, it means there's value being left over that an agent could use. So there's so much context on the code change, there's so much context on the review. Anything that you can do — specifically, as soon as something is fully done and ready to merge — I might do one final quick hook or step before merging, which is: extract lessons learned from review. And then it's just one long log of how you think about things — a markdown file that's continually growing. It's basically stateful memory.

[02:16:23] Scott Rippey: Patrick got me into Hermes, and I'm telling you, I lit that system on fire. I'm almost kind of thinking about how I can meld some of these systems together now. Because data is power, right? Our information is the best tool. And it's not the AI — it's actually your most valuable asset is your data.

---

<!--SEGMENT
topic: Ryan's Client Work, CRM for Estate Agents, and Parking Lot Economics
speakers: Ryan C, Brandon Hancock, Scott Rippey, Patrick Chouinard
keywords: Kratom website, CRM, estate agents, UK property, RAG database, iOS companion app, drag-and-drop email builder, MailChimp, Fable, digital screens, parking lot, affiliate revenue, image generator, Higgsfield, Nano Banana, real estate photography, AI photo enhancement
summary: Ryan C describes his current client work portfolio: a full CRM and custom MailChimp-style email builder for a Kratom company, an AI-forward CRM for UK estate agents with RAG history and an iOS companion app, and a growing digital screens business now at 12 locations. The group then discusses the economics of Scott's parking lot app client — $24K revenue in one month — which sparks a broader conversation about underutilized physical assets (parking lots, storage units) as high-margin AI arbitrage opportunities. Ryan also demos a custom AI property photo enhancer built with Higgsfield and Nano Banana.
-->

[01:04:09] Ryan C: I've got nothing for show and tell today. I've actually been working a lot on a website, but I can't show it to you because I'm under NDA. I've been doing a lot on a website for Kratom [tool:Kratom website]. K-R-A-T-O-M. It's a bit like marijuana, but legal in quite a lot of US states. I'm building a website and a full CRM and my own version of MailChimp [tool:MailChimp] for them.

[01:05:00] Ryan C: I built the coolest drag-and-drop MailChimp-style mail builder, which is wicked, and it works. I'm quite happy with myself with that.

[01:05:20] Ryan C: And then I've started another company, just because I had some free time between about 3 a.m. and 6 a.m. I'm building an AI-forward CRM system for estate agents in the UK that manages all their properties, but it ingests all of their emails, WhatsApps, triages it, drafts responses in their brand voice, understands them, has a full RAG [tool:RAG] database with their history, and has a companion iOS app with an AI chat that you can talk back and forth with.

[01:06:26] Ryan C: I started it with Fable [tool:Fable], and then Trump tariffs hit me.

[01:08:33] Ryan C: I'm building a couple of businesses underneath that with the screen stuff that is now at 12 screens, about to get another two screens on, potentially another seven or eight with this guy that I talked to this morning.

[01:11:29] Scott Rippey: He made $24K in one month. Like, he made $15K, he paid me off.

[01:11:38] Brandon Hancock: In three weeks? How much — if that plot of land was for sale, how much do you think it would be?

[01:12:27] Brandon Hancock: Every time you guys give me ideas, I try to extract the abstract formula of it. And I think the cool thing from listening to both of you guys is: people have assets that are underutilized as of pre-AI. And that same asset can now be way more profitable for them and you as an arbitrage opportunity. So in my head, it's like, how do I copy and paste that? Okay, parking lots, storage units. What's a static asset that is low overhead and is very systematizable?

▶ [01:13:37] Brandon Hancock: Someone who's listening to the recording of this — take this three-minute snapshot, and then just say, in my local area, in 50 miles, find every opportunity that fits this archetype. There's literally probably hundreds of thousands of dollars sitting right under your nose.

[01:15:01] Ryan C: The only other thing I've done is build out a completely custom image generator that's hooked into Higgsfield [tool:Higgsfield] using Nano Banana [tool:Nano Banana] through it, and I've just tweaked it for real estate, because I keep getting asked by people that have old photography that's crap, and they go, can you make this look a bit better with AI? So I built the entire thing through Claude Code [tool:Claude Code] as a project. I've given it thousands of photos that I've taken to train it on — it's literally just for editing property photos to make them look like they've been taken on an HDR camera and not on a potato.

---

<!--SEGMENT
topic: Juan's AI Photo Booth Hardware and Business Model Brainstorm
speakers: Juan Torres, Brandon Hancock, Ryan C, Patrick Chouinard, Paul Miller
keywords: mirror booth, mini PC, GPU, multi-model diffusion pipeline, image-to-image, AI photo booth, event photography, QR code, CloudWatch, EC2, franchise model, vending machine model, wedding venue, revenue share, printing affiliate, image-to-video pipeline, unit economics
summary: Juan Torres presents his AI-powered mirror photo booth: a touch-screen mirror with a custom mini PC replacing the original industrial computer, running a multi-model diffusion pipeline that generates stylized AI images of guests. The group engages in an extended business model brainstorm — covering franchise/vending-machine distribution, revenue-share partnerships with wedding venues, QR-code-based voting and AI roast features, print-on-demand affiliate revenue, and an image-to-video pipeline extension. Brandon emphasizes proving the model with 10 self-operated events before scaling, and offers to introduce Juan to a wedding venue owner.
-->

[01:25:30] Juan Torres: My setup is I have mini PCs — one for the mirror booth that I have here and another one for the display, which is going to have my AI booth-generated images. The mini PCs are attached on the back. This mirror booth actually had an old PC. I basically took it apart, rearranged the cables away from the touch control board, the display board, and reconnected them to my mini PC, because it has enough GPU capacity to make this halo effect.

[01:29:42] Juan Torres: I just finished creating a multi-model diffusion pipeline. So the pipeline has the ability for me to edit each transformation part. That's why you see several styles.

[01:35:00] Juan Torres: The observability is there. I have CloudWatch [tool:CloudWatch] already set up to observe memory, CPU utilization, disk. And also, I have the data web application which basically displays all the metrics, including AI job runs, and basically all the jobs that have been generated with thumbnails.

[01:36:17] Brandon Hancock: <Q>How can I get my first 10 things myself? Like, how can I physically go try it out myself where I'm the operator and get feedback from the customers?</Q>

<A>[01:37:22] Brandon Hancock: Some sort of a franchise model — you do some sort of case study for a city or two in a local area, and you just showcase on social media, like, hey, I'm starting to sell this thing, and let me just show you guys the numbers. I book 12 events per month at $200 each — that's $4K, and all I have to do is work for not that many hours. And then what's cool is you literally set yourself up for a franchise model because other people are just going to be like, well, I'd like to make easy money. You're telling me all I have to do is buy that thing from you for $800? That's the initial upfront investment.</A>

[01:41:25] Ryan C: I went to my best mate's wedding on Sunday, and they had a little wooden pod with an iPad in it. You literally just take a picture with the iPad's front camera, doing some kind of art. They're charging £600, which is equivalent to about $750, $800 for a day. They come pick it up in the morning, and it goes to another wedding. So if they're making that a day, you can potentially franchise that out, right? You charge a rental fee and just ship it to the places you need it to be.

▶ [01:45:58] Brandon Hancock: The other option is: if you could make this to where it literally needs zero human operators — I need you to hook me up to Wi-Fi once, put this thing on wheels, to where during the event, I roll it out, and at the end of the event, I roll it back up — you're not doing the vending machine model, you're doing the partnership model. You give that wedding venue an additional way to make an additional $700 per event. Hey, it's $700 — if your customers sign it, I'll just give you $350. I'm going to send you the hardware, I'm going to maintain the software, you don't have to do anything else.

[01:50:01] Patrick Chouinard: How about — because I remember you showed a way to scan a QR code with the application — imagine you do that and you're in the wedding, and people can use the QR code to vote on which of the groom and the bride they want to be roasted out of all of their pictures at the end of the night, and whoever gets the most votes gets roasted.

[01:52:10] Ryan C: You could partner up with some sort of printing company, and people can then choose to pay to print stuff out or make a physical album out of them. And then you get a cut of every single album that they produce.

[01:56:34] Juan Torres: How about you couple what you did with the video pipeline that Scott presented last week? So you feed all of the pictures and then it generates the video with the narration exactly like Scott did for his YouTube channel. But your pictures are the input to his pipeline.

▶ [01:58:01] Brandon Hancock: Scale as fast as possible, build this as quickly as possible, get as many partners as possible, even if the money at first isn't just cash flowing in, because it will flood in. This is how you make an exit. Just grow as fast as possible — literally 50% of your time should be spent selling this.

---

<!--SEGMENT
topic: Bastian's Elixir Sub-Agent Harness and Agentic Tooling
speakers: Bastian Venegas Arevalo, Brandon Hancock, Scott Rippey, Patrick Chouinard
keywords: Elixir, sub-agents, Codex, memory optimization, WebSockets, ACP protocol, T3 Code, Zed editor, Claude Code hooks, OpenAI subscription, caching, worktree, agentic harness, open source
summary: Bastian Venegas Arevalo presents an Elixir-based agentic harness designed to solve the memory explosion problem when spawning multiple Codex sub-agents (which can consume 10+ GB RAM). By running each sub-agent in the same Elixir memory process, the harness scales to hundreds of sub-agents at a fraction of the memory cost. It supports a CLI, integrates with T3 Code and Zed via the ACP client protocol, uses WebSockets for faster requests, and maximizes prompt caching. A companion parrot-themed desktop agent with a single MCP tool call delegates work to the harness. Bastian plans to open-source it the following week.
-->

[02:19:48] Bastian Venegas Arevalo: I'll make it brief. I just want to show a project I've been working on just to burn everyone's tokens, hopefully.

[02:19:57] Bastian Venegas Arevalo: You guys really know how Codex [tool:Codex] and Claude Code [tool:Claude Code] has this sub-agents feature, and the issue with Codex, at least, is that when you spawn like over six agents, it will eat all of your memory, and it can spend like 10 gigs of memory or more, and it will also spike your processor like crazy. So I built an agentic harness that is built on Elixir [tool:Elixir], so each time it spawns a new agent, it's actually running in the same memory process, so the scaling is from hundreds of megabytes — not even a megabyte. So this is meant to be able to run dozens and even hundreds of sub-agents.

[02:20:42] Bastian Venegas Arevalo: It's also meant to be a sub-agent as a service, so you don't need to use the harness, you can just use it as a sub-agent for Codex. It has a CLI that you spawn, and you spawn each sub-agent, or it can also spawn a workflow where it will map all the chain dependencies, create a workflow, and then spawn each sub-agent, each one on its own worktree.

[02:21:17] Bastian Venegas Arevalo: I also built this to be really friendly on your cache, so it has a prefix that is really small — it's inspired by Pi — and most of it gets cached every time you hit a request. And since a sub-agent is typically just cranking up work and you're not really interacting with it, everything gets cached at crazy lower costs. And since it uses WebSockets [tool:WebSockets], it's also much faster in terms of the request.

[02:22:07] Bastian Venegas Arevalo: Basically, it doesn't have a user interface, because it uses the ACP client protocol [tool:ACP protocol] that Zed [tool:Zed editor] introduced. So you can use it in the CLI, you can use it in something like T3 Code [tool:T3 Code], and you can use it on Zed, which is a very lightweight editor. T3 Code also has a mobile app, so I have mobile running from my phone as well, connected to my computer.

[02:22:41] Bastian Venegas Arevalo: It actually has this cool feature where it will follow the agent as it works. So it will start appearing here. Every time it opens a file or it edits something, you will see it happen in real time.

[02:23:15] Bastian Venegas Arevalo: And I also have this little guy here — I don't know if anyone is familiar with Polly Parrot from the 90s. The cool thing is that this guy has only one tool, which is an MCP [tool:MCP] tool. And under the hood, this calls my agent. So it gets access to everything. It's like having a second pair of eyes on top of everything you're doing. And it has permission to see your screen. So it's like an agent on top of your agent.

▶ [02:24:01] Bastian Venegas Arevalo: So I guess, real fast — the biggest thing, said simply, is it is mostly improving the user experience and also reducing memory usage. It's sub-agents as a service.

[02:24:24] Brandon Hancock: I know on my laptop, whenever I'm ripping on Codex, I just hear my computer gets hot as hell, my fans — thank God I have a newer Mac. My old one would have just died.

[02:25:00] Bastian Venegas Arevalo: For now, I just added OpenAI [tool:OpenAI] just to make it really simple because they're the most general subscription by far.

▶ [02:23:04] Brandon Hancock: This will be open source. So probably next week I'll have it ready so anyone can try it.

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names did not appear in the supplied `SPEAKER_ALIASES` context block (which was empty/unpopulated at generation time) and are passed through unchanged:

- **Ty Wells**
- **Paul Miller**
- **Patrick Chouinard**
- **Brandon Hancock**
- **Ryan C**
- **Dave Gottschalk**
- **Juan Torres**
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** (display name includes social handle and URL; passed through as-is)
- **Bastian Venegas Arevalo**
- **Adam** (first name only; appears briefly at ~[01:22:08])