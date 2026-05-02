=== SESSION ===
date: Unknown (transcript timestamps begin at 00:06:27)
duration_estimate: ~2 hours 55 minutes
main_themes: Claude.ai computer-use agent ("Claude.ai computer-use agent" / "Claudebot"), SOC 2 & HIPAA compliance, AI-powered SaaS project planning, voice AI platforms, developer tooling (RAG, embeddings, GSD framework), community call format changes

---

<!--SEGMENT
topic: Call Format & Community Updates
speakers: Tom Welsh, Marc Juretus, Paul Miller, Brandon Hancock
keywords: community call, weekly cadence, Brandon Hancock, Patrick Chouinard, YouTube channel, EMS Soap, SaaS journey, podcast format, School platform, topic post
summary: The group discusses the future format of the weekly community call now that Brandon is stepping back to focus on his SaaS project EMS Soap. Brandon explains a new structure where Paul, Patrick, and Tom will co-host, members post questions in advance, and Brandon joins every fourth call. Brandon also shares plans to pivot his YouTube channel toward a podcast-style format documenting the EMS Soap build journey.
-->

00:06:27 - Tom Welsh
Hey, Marc.

00:06:32 - Marc Juretus
Thomas, what do you say, brother?

00:06:36 - Tom Welsh
Is this the final one, is what I'm asking?

00:06:40 - Marc Juretus
Supposedly with Brandon. I hope somebody else does sound like, even if it's every two weeks.

00:06:45 - Tom Welsh
Yeah, Brandon's asked Patrick, myself, and Paul to run some, so I think that's what's going to happen. And I think he's going to jump in once a month.

00:06:58 - Marc Juretus
I'm in, definitely.

00:07:01 - Tom Welsh
I think it's just good to keep talking, just keep the conversation going.

00:07:07 - Marc Juretus
You've got more people experiencing different things where we can't experience everything. So this is priceless for that.

00:16:29 - Marc Juretus
Hey Paul, did I hear Tom right there — one of you guys going to try to keep this call going during the month or so?

00:16:16 - Paul Miller
Yep, yep, yep. So between Patrick, myself, and Brandon. Brandon's going to be on every fourth call.

00:17:00 - Brandon Hancock
Yeah, so Paul and Patrick had a really cool idea — basically to take better advantage of the School community. More content should be in there, and to help make calls a little bit more orderly so people kind of have a rough road map. We should basically be using a weekly post to bring up a topic or two, and then let you guys add in cool questions that you have or wins that you want to talk about. And then we'll take that as the call order.

00:17:50 - Brandon Hancock
That way there's communication on the platform and on Zoom calls — more AI talking happening all the time.

00:18:08 - Brandon Hancock
One cool update I want to bring up: at least how I'm thinking about YouTube content. I'm wanting to basically start switching YouTube over to almost like a podcast platform — take you guys along the journey of building out EMS Soap [tool:EMS Soap]. I still have to talk to my co-founder about this, but basically bring on whatever bottleneck we're facing, bring on and interview someone who's in that space. So example: marketing, Google Ads, landing pages. Basically they get a platform, I learn, I pass down the learnings, and you guys get to learn about it as well.

00:19:16 - Brandon Hancock
▶ At this point, all of you are phenomenal at making apps, and it's the next part that's the hard part — getting the leads, building the systems. There's a thousand extra things.

---

<!--SEGMENT
topic: Claudebot Setup & Security
speakers: Brandon Hancock, Patrick Chouinard, Scott Rippey, Juan Torres, Paul Miller
keywords: Claudebot, Claude Code, service accounts, Ubuntu VM, Proxmox, GitHub pull requests, Obsidian Vault, Telegram, security hardening, isolated VLAN, SSH
summary: The group dives into the newly released Claudebot (Claude.ai computer-use agent), sharing first impressions, security concerns, and setup strategies. Patrick describes creating a fully isolated Ubuntu VM with dedicated Google and GitHub service accounts, treating the agent like a new employee. Scott shares his experience coding an app via WhatsApp through Claudebot. The segment covers best practices for isolating the agent from personal machines and Patrick's technique of syncing the agent's memory to an Obsidian Vault via GitHub.
-->

00:20:31 - Brandon Hancock
Okay, so this is my favorite question, actually. Thoughts on Claudebot [tool:Claudebot], guys.

00:20:55 - Brandon Hancock
Patrick, if you're on, buddy, I know you have been doing some awesome stuff. I'd love to do a demo, too, because I think Patrick's gone beast mode on Claudebot.

00:21:12 - Patrick Chouinard
Configuring the thing will take forever, but I'm going to get there. It's just the pattern I've used to make sure that I had something powerful but secure at the same time, because giving access to your account, your email, your files to that thing is a recipe for disaster.

00:21:38 - Patrick Chouinard
▶ What I did is I created a Google account for itself. So it has its own email, calendar, Google Drive [tool:Google Drive], everything. I want to treat it exactly as I would treat a coworker.

00:22:18 - Patrick Chouinard
I started by deploying it on an Ubuntu VM [tool:Ubuntu VM] but Ubuntu server, and I realized that might not be the right thing, so I'm going to transfer it to an Ubuntu desktop so it has full web capability, but still in an isolated environment. That VM I'm never going to use myself — this is going to be dedicated to the agent itself.

00:22:45 - Patrick Chouinard
▶ I've created its own GitHub account [tool:GitHub]. It's going to have read access to mine, but read only. So if I ask it to work on the project, it's going to create a clone, work on the clone, and submit a pull request. Drive it exactly as an individual. You're going to have a secure environment, but an insanely powerful agent.

00:23:13 - Brandon Hancock
Basically, the key thing Patrick told me yesterday when it clicked — service accounts is what he's done. So when he says an additional employee, like own email, own everything, and basically onboarding them — which is the best way to think about Claudebot.

00:23:39 - Brandon Hancock
My biggest concern, because I've watched so many videos on it at this point, is all it takes is one security vulnerability and they have access to everything. So that's why remote access to everything scares me. I'm going to give it at least a week before I start hooking up my stuff, just in case there's a big "we hacked everybody" incident.

00:24:42 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I coded an entire app through WhatsApp [tool:WhatsApp] with Claudebot last night. I just went YOLO — I'm setting this up on my PC. Patrick makes good points, and obviously as an IT person I need to harden my security, probably make separate accounts. But holy crap, how cool this is. I was lazy on my phone in WhatsApp building something, and I could see it — I remoted into my machine and was watching files happen. It's not controlling your screen, it's happening in the background.

00:25:38 - Patrick Chouinard
<Q>Why does this feel like it's kind of smarter than just going and writing?</Q>
<A>As smart as nothing to do with the intelligence of the pure LLM — it's scaffolding and tools, and they nailed the scaffolding and tools for that.</A>

00:27:26 - Patrick Chouinard
▶ The very last little trick that I love — because it gives me a peek into its memory — I told it to create itself in its own GitHub repository, a GitHub repo for an Obsidian Vault [tool:Obsidian]. And to duplicate every single thing it thinks, all the lists it builds, all its to-dos, everything, drop it in there. Then I just sync it to my PC, and I have a window into its brain.

00:28:10 - Brandon Hancock
<Q>Hey, final thing on that, Patrick — is that through a hook? Does Claudebot have a hook concept, or is this just at the end of every instruction, save here?</Q>
<A>I just ask it to do it. I just told it in chat: duplicate everything you write to your memory to the Vault, and it now knows that the Vault is its own Obsidian Vault.</A>

00:28:51 - Patrick Chouinard
▶ You have to be very specific when you give it something — say, this is your email, this is your calendar, you're not operating it for me, it's yours. You do what you want, because it belongs to you. It tends to think that it's acting on your behalf.

00:29:04 - Paul Miller
▶ There is a skill on the library that it self-trains itself — it's got a skill library if you go to the website, and one of the most popular of the skills is the skill that it trains itself.

00:29:20 - Brandon Hancock
Yeah, that's recursion, self-improvement — as a cheat code.

---

<!--SEGMENT
topic: SOC 2 & HIPAA Compliance Deep Dive
speakers: Brandon Hancock, Prem, Jake Maymar
keywords: SOC 2, HIPAA, Vanta, Drata, TinySeed, Supabase, Railway, Google Cloud, zero data retention, Type 1 Type 2 audit, compliance cost, EMS Soap
summary: Brandon walks through his firsthand experience pursuing SOC 2 and HIPAA certification for EMS Soap using Vanta, covering vendor selection criteria (integrations with Supabase), cost breakdown (~$20K for dual audit with TinySeed discount), and the grueling process of completing ~65 tests. The segment also covers the distinction between SOC 2 Type 1 and Type 2, zero data retention as a compliance shortcut, and why compliance creates a competitive moat for SaaS businesses.
-->

00:29:29 - Brandon Hancock
So, Prem is looking at HIPAA SOC 2 for a project. Would appreciate some pointers on how you're planning and achieving it, which vendor you're using, and the cost and timeline.

00:29:42 - Brandon Hancock
▶ There are two main players in the field: Drata [tool:Drata] and Vanta [tool:Vanta]. The key thing you want to look for when picking a compliance partner is integrations. The more things that platform is integrated into, the more things that just happen automatically versus you digging through the settings, taking a screenshot, pasting it in.

00:30:22 - Brandon Hancock
▶ Vanta had ours, which was Supabase [tool:Supabase]. That was the main thing. And literally as of today, migrating off of Railway [tool:Railway] and over to Google Cloud [tool:Google Cloud], because they don't have connections for Railway.

00:31:22 - Brandon Hancock
Cost: Vanta for us — we got a little bit of a discount because of TinySeed [tool:TinySeed]. The raw numbers were: we did SOC 2 and HIPAA with two audits — a Type 1 and Type 2. For all of that, it's $20,000. We got $4K off by being through TinySeed.

00:32:02 - Brandon Hancock
The audits are one-time. The annual subscription I think is like $10 or $12K something like that.

00:33:00 - Brandon Hancock
▶ I really recommend doing it when it hurts if you know there's a few big customers on the other side of it. They also look at the size of your startup — the smaller you are, they're not going to ream you.

00:33:26 - Brandon Hancock
The whole process is: you log in and it says "test." There are like 65 tests. Every test has multiple things you have to do. Thank God for AI — it's doing most of it for me, but it still takes time. It feels like the worst video game ever created — to achieve the main goal, there's a side quest, and that side quest has another side quest.

00:34:38 - Brandon Hancock
I'm hoping we'll get it done in a month of dedicated work.

00:34:42 - Jake Maymar
<Q>Are you doing ZDR at all?</Q>
<A>Zero data retention — it's a way to get around the audits, essentially. If you're not retaining the data at all, it's less of a headache.</A>

00:35:28 - Brandon Hancock
Right now our tool — we do not store HIPAA or anything. We are zero data retention. We're literally just a: you put information into the calculator, and it spits out. We don't store memory, nothing. What we would love to do is actually get to the point where we can store, because that just unlocks so many levels of improvement — feedback loops to improve our entire platform.

00:36:38 - Brandon Hancock
▶ A lot of big companies won't even look at you unless you have both of these. And it technically allows us to do a lot more with AI — set up more aggressive evals and alerts.

00:38:32 - Brandon Hancock
<Q>SOC 2 Type 1 vs. Type 2 — do you have to go through Type 1 first?</Q>
<A>SOC 1 is like for banks. SOC 2 is more for tech companies. SOC 2 Type 1 is a point in time — at January 1st, 2026, Brandon was compliant. Type 2 is: we have monitored Brandon's business for 90 to 120 days and the entire time he remained compliant. SOC 2 Type 2 is the gold standard.</A>

00:37:43 - Brandon Hancock
▶ Compliance is putting a moat around your business — it's expensive, and not a lot of people want to do it. Anything that costs a lot of money or is regulated is the best way to set up yourself for success in a SaaS.

---

<!--SEGMENT
topic: Ama's Task Execution SaaS Concept
speakers: Brandon Hancock, Ama, Raghav Ram
keywords: Claude Code, task management, agent workflow, decision tree, todos.md, context.md, ShipKit, Worker SaaS, cron job, prototype-first approach
summary: Ama presents an idea for a personal execution system — a minimal app that surfaces the right next action each day and uses AI to help break down tasks when the user stalls. Brandon advises against jumping straight into code, recommending instead that Ama use Claude Code with a simple markdown-based prototype to clarify the exact decision logic before building. The segment covers how to translate nebulous product ideas into concrete agent instructions.
-->

00:40:00 - Brandon Hancock
Okay, so Ama — you're looking at making a SaaS project which is an execution system that helps you consistently take the right next action without dashboards, chat, or automation. What are you envisioning?

00:40:33 - Ama
I basically want some sort of — I don't actually want a productivity tool. I don't want a habit tracker or anything like that. I just want a very simple system which on the front end puts in front of me what I need to get done on that particular day. And if I'm not in a great mood to do that one thing, it could perhaps suggest a smaller step. The idea is to be able to take action every single day and move a project forward.

00:41:38 - Ama
If I don't execute something a number of times, there'll be a trigger that says, the times when you've been really productive was usually in the mornings. So it's kind of like I'm still experimenting.

00:42:52 - Brandon Hancock
▶ To start off, to help gain clarity around what feels right and doesn't feel right for this, what I would recommend is to create a new project on your computer and use Claude Code [tool:Claude Code]. All that Claude Code is going to have is a few core files: a file which lists your to-dos, a file which just contains your high-level instructions, and then just a chat interface. Experiment locally with Claude Code first to get an understanding of what you're actually trying to achieve.

00:43:44 - Brandon Hancock
▶ I recommend to just use Claude Code at first, and do everything through prompts. You don't have a database, you just have a file called todos.md. You have a context.md — that's where you're going to say, here's how you're supposed to help me, and here's what I'm ultimately trying to do. That way you can codify exactly how you want the agent to behave. The second you have that working, it's so easy to then convert into smaller actions inside of a codebase.

00:46:54 - Brandon Hancock
These are the decisions we have to make: Are we triggering a cron job every hour to check the status of the task? Are we triggering it once a day? When it does trigger, what are we looking at? If the person hasn't done the task, what do we do — do we break into smaller tasks, do we email them? This is where actual systems thinking has to start being applied.

00:49:33 - Brandon Hancock
▶ For Ama's case, the Worker SaaS [tool:Worker SaaS] would be a great one the second she figures out how everything works — she could have a bunch of tasks that get triggered every 10 minutes to analyze the person's current state of all their to-dos, go through an AI decision tree of: does this task need to be broken down? Do I need to send them a reminder?

00:50:43 - Brandon Hancock
▶ Before writing a single line of code, we could just have AI pretend to be an application. I'm trying to build out a system for an AI to help me achieve this task. Can we work together on coming up with a system? Ideally I want a list of to-dos and a set of instructions, and we're going to pretend you're the application, and we're going to start going through a bunch of different scenarios so that we could really solidify the system.

00:51:11 - Brandon Hancock
If it doesn't make sense, I would really recommend checking out the video I did on making an AI video generator — the Pokémon one — because I basically built a pretend application with Claude Code, only with prompts. There's no code, it's just all Claude Code following AI instructions. [link:Brandon Hancock Pokémon video generator tutorial]

---

<!--SEGMENT
topic: Email Infrastructure & Supabase Auth Limits
speakers: Brandon Hancock, Morgan Cook, Ty Wells, Jake Maymar
keywords: Supabase, Resend, Mailgun, SendGrid, email throttling, 30 per day limit, Wix domain, client hosting, Vercel, authentication emails
summary: Morgan asks about email providers for Supabase Auth, noting the 30-email-per-day development limit. The group recommends Resend or Mailgun as production replacements for Supabase's built-in email. Jake adds a practical warning about client hosting environments (e.g., Wix domains) that can restrict which email providers work, and recommends verifying the client's domain host before committing to a provider.
-->

00:51:47 - Brandon Hancock
What is everyone using for emails from Supabase Auth [tool:Supabase]? My understanding is Supabase email is for development, and they throttle 30 per day. So I was thinking of Resend [tool:Resend]. What are you guys using?

00:52:00 - Brandon Hancock
▶ In a large application where you're getting more than 30 customers a day — which is a huge success — I would recommend using Mailgun [tool:Mailgun] or Resend. That's literally what we do. Upon sign up or reset password, where that normally used to get handled inside of Supabase, now you just have the same email templates that go out through Mailgun or Resend.

00:53:16 - Ty Wells
I use Resend, so I just switched to that. I've started with that and I've been using that ever since. It's easy to work with. Pricing is good.

00:53:47 - Jake Maymar
▶ One thing I found out — I was using Resend, but then I found our client was on an unusual hosting. You want to know what your client is on, because sometimes that affects what you can use. If your client has control of the hosting, you want to find out what their domain is hosted on, because some of the tools don't work. This client was on Wix, and I had to use SendGrid [tool:SendGrid] instead.

00:55:07 - Morgan Cook
I've already moved them off that. So they're on Supabase and Vercel [tool:Vercel].

---

<!--SEGMENT
topic: Marc's Fitness App & Token Throttling
speakers: Marc Juretus, Brandon Hancock
keywords: Sanford Fitness, Supabase, Railway, usage table, context provider, Vercel AI SDK, tool calls, workout proposal, gamification, Next.js
summary: Marc demos his Sanford Fitness app — a workout tracker that randomly selects exercises, tracks history, and will feature AI coaching personas (passive, moderate, or "David Goggins" style). He asks how to throttle AI chat token usage per user. Brandon recommends a usage table in Supabase and a React context provider to track and surface per-user query counts. Brandon also introduces the concept of Vercel AI SDK tool calls to enable the AI to propose, confirm, and edit workouts conversationally.
-->

00:55:35 - Brandon Hancock
Marc, you are up first, buddy.

00:55:43 - Marc Juretus
I'm going to make an app front to back where I do it somewhat professionally — I have Notion, I got the whole thing. This is the app I've built so far. I work out at like 5am, so sometimes it's like brain fog. So you load your own exercises in there. When you do Quick Workout, you select tricep/chest, and it'll go in and grab two exercises from each one of those groups, display it to your screen, and say, hey, you haven't done this exercise in the last three weeks.

00:57:15 - Marc Juretus
I'm going to have three virtual guys where you have either the passive agent that's always saying nice stuff, the in-between that I kind of prefer, or you could have the militant one — basically David Goggins, get out of here.

00:58:01 - Marc Juretus
<Q>How do I limit them — if they're using the chat — so they're not using up a whole lot of tokens? How do I throttle them based on login?</Q>

00:59:02 - Brandon Hancock
<A>▶ The simple thing is you'll make a new table called `usage` or `query_usage`. All it's going to have is the user ID, the type of query. Then what's so nice is eventually you'll make something called a query context provider. Inside your application, you usually have something called a user context, which has information about the user. You can also hydrate it with the query usage — so you can automatically say, hey, they've done three custom workouts, they've sent 30 messages. That way, just anywhere in your application where you want to do like, hey, how many messages has this person sent? You'll do `useUser` — that's the hook to get access to the context provider — and in there you'll be able to see usage.</A>

01:02:18 - Brandon Hancock
▶ The one thing that's really going to help level up your application in the chat is the ability for the AI to propose a workout — and that's strictly coming down to a tool call. In Vercel AI SDK [tool:Vercel AI SDK], you have the ability to make tool calls. You can make three tools: propose workout, confirm workout, or edit workout. And then whenever the user confirms it, you'll just add that to their workout for today.

01:03:14 - Brandon Hancock
▶ A workout is just an array of sets and reps and movements. At the end, the user can just say confirm if they like it, or they can talk to AI again and say, hey, I actually want this one to be different, change it to three sets of eight reps. That's all done through tool calls — and that's what's going to make your app feel magic.

01:04:46 - Marc Juretus
Anything you can gamify will get you traffic, in my opinion. Like, post the number of steps you have up there, and I'll have this step leaderboard. You know how people are — they'll go up there, all right, but this dude did 5,000 steps, now I'm doing 10,000.

---

<!--SEGMENT
topic: AI Agency Sales Strategy & Voice Platforms
speakers: Paul Miller, Brandon Hancock, Hemal Shah, Scott Rippey
keywords: LiveKit, Bland AI, WAPI, voice agents, AI agency, productized service, case studies, objection handling, compliance artifacts, MBA presentation, Dan Martell
summary: Paul shares his experience presenting AI strategy to MBA students and pitching AI consulting to businesses ranging from small resellers to half-billion-dollar companies. Brandon advises on how to convert interest into paid engagements: lead with concrete case studies from adjacent industries, pick a vertical (voice agents or compliance artifact generation), and become a trusted implementer for a platform like LiveKit. Hemal adds WAPI as an emerging alternative to Bland AI, and Brandon outlines a content-to-client playbook for building an AI agency in 2026.
-->

01:08:15 - Paul Miller
Other than playing with Claudebot — which has renamed itself, it's now Moltbot, I think they might have gotten in trouble with trademarks — one of the use cases I'm using for Claudebot is for it to monitor all of the servers that I've got Docker [tool:Docker] and Docploy on, just looking at security changes and reviewing logs.

01:09:34 - Paul Miller
For those that are running with the Next.js [tool:Next.js] stack, there was that flaw that came out in December — there was a big security hole. People are leveraging that now, so you've just got to be on top of making sure you patch Next.js on that and block your ports.

01:10:00 - Paul Miller
I've got AI projects where people have said, we want to pay you to advise us how we can use AI to transform our business. From a half-a-billion-dollar business to a small resale business. Most of the demand is coming from people asking a lot of the same things.

01:11:01 - Paul Miller
I got invited by a university to come talk to an MBA course. The biggest thing they asked about was: how do I, within the company I'm in, help build a justification to run an AI project and not get in trouble with the gatekeepers of tech?

01:13:20 - Brandon Hancock
▶ A lot of the times when you're talking to potential clients, they're in an industry. One of the biggest issues — until I see something done as a customer, I don't believe it. If you have any case studies, even in adjacent markets — I have seen how customers in this adjacent industry had a very similar problem, and now they're closing more deals, they reduced the overhead of their staff by 60% — the more concrete numbers, the more you can study the industry, the easier it is to sell.

01:15:38 - Brandon Hancock
▶ The hardest one is just to get that first case study in, and picking a vertical. Like, are you going to be voice AI? Or — any business where you have to produce an artifact to get paid, or to not go to jail — people will pay that all day. That applies to everything from teachers, police, lawyers, the entire IT department.

01:18:49 - Brandon Hancock
▶ If I was starting an AI agency in 2026 and I just wanted to create a productized service — I will build AI voice agents for you — the exact playbook I would follow: create an audience, build a few for free to get trust and service, create tutorials, and then tell LiveKit [tool:LiveKit], hey, is there any way I can become a trusted advisor? But only after providing massive value to LiveKit first. Don't ask. Give, then ask.

01:19:50 - Brandon Hancock
▶ If you do LiveKit properly, that's easily probably $300K+ this year. It takes a few customers a month — two to three at $10–15K a piece, and it's mostly going to be a two, three month retainer.

01:20:27 - Hemal Shah
Besides Bland [tool:Bland AI] and LiveKit, WAPI [tool:WAPI] was one thing that kept coming back up. One of my colleagues used Bland AI and then moved from Bland to WAPI. I'm going to meet him soon to understand what made him make that move.

01:21:07 - Brandon Hancock
▶ Voice and AI workflows that produce an artifact — I think those are the gold mines of 2026.

01:22:17 - Brandon Hancock
▶ Paul, book reminder: Extreme Ownership [link:Extreme Ownership by Jocko Willink], Chapter Three. I was thinking of you — the entire chapter, the whole dynamic between the CEO and CTO.

---

<!--SEGMENT
topic: Patrick's Claudebot Training Harness & Daily Digest
speakers: Patrick Chouinard, Brandon Hancock, Paul Miller, Juan Torres, Jake Maymar, Elijah, Ty Wells
keywords: Claudebot, Proxmox, Ubuntu VM, Telegram, Brave API, Perplexity, Obsidian Vault, Notebook LM, GitHub, Claude Code, training harness, cron job, service account, BM25, vector memory
summary: Patrick demos two major Claudebot projects: (1) a daily AI news digest that uses Brave search and Perplexity for deep dives, delivered via email from the agent's own Gmail account on a cron schedule; and (2) a "training harness" — a set of Claude skills and commands that document every coding session, push summaries to Notebook LM via MCP, and generate reusable training artifacts. The group discusses the agent's hybrid memory system (vector + BM25), security isolation via VLAN, and the philosophical implications of having an agent build tools for itself.
-->

01:30:02 - Patrick Chouinard
Actually, for the Claudebot, what I just did is I configured it using a Brave API [tool:Brave API] and my Perplexity API [tool:Perplexity] key. And now it writes me a daily digest of AI news.

01:30:47 - Patrick Chouinard
Remember, when you look at it, this was done simply by chatting through Telegram [tool:Telegram]. Nothing more. There's literally no code, no specs, no nothing.

01:31:00 - Patrick Chouinard
It's running on an Ubuntu VM on a Proxmox [tool:Proxmox] server. No GUI right now. I want to move it to a machine with a GUI, specifically to have the ability to do the browsing.

01:31:39 - Patrick Chouinard
The first section is from an authoritative update — information from the site of the supplier, right now following OpenAI [tool:OpenAI]. Discovery — this is Brave doing unknowns unknowns, basically searching for stuff I might not even have thought about. And here it does a deep dive with Perplexity on specific subjects that either have to do with the release of a new model, security update, or things that need to be drilled into a little bit more detail.

01:32:56 - Patrick Chouinard
I also have the cost for the Perplexity calls, because this is the only paid one — the Brave is free within the limit I'm using. But this is just like two, three messages, and it built that, and now I'm going to get that email every morning.

01:34:16 - Patrick Chouinard
What I've been working on is a project because I do a lot of training. I train people on AI as my day-to-day job. I've come up with a prompt that I've turned into a skill that documents our interaction. So every time I complete a discussion, it summarizes the discussion, puts out the insight that comes out of it, the technique we're using, it documents everything.

01:35:09 - Patrick Chouinard
▶ I've used the Notebook LM MCP [tool:Notebook LM] to actually push those into an MCP notebook. I've created a pipeline that generates the prompt that I can just copy and paste to customize the artifacts so they are the way I want them to look.

01:35:56 - Patrick Chouinard
This is a notebook that was created by that pipeline. You can see all of the case studies here — those are all the discussions that happened. To find the application and code it, it took me 17 conversations, and they're all in there.

01:36:20 - Patrick Chouinard
The training harness is just a bunch of Claude skills and Claude commands. They're built to be imported in any new project I start as a sub-module. I have an install script in there that when I run, it copies all of the files in the proper `.claude` folder structure for it to be used with the project you just instantiated.

01:37:52 - Patrick Chouinard
▶ It's a public repo. [link:Patrick Chouinard training harness GitHub repo — shared in chat]

01:38:16 - Brandon Hancock
▶ Here's exactly how I'm imagining this: any time you go through any process, this can document exactly how you did something. So if you're like, I'm going to go work on making a Google ad campaign and Claude Code is going to help me do everything — it's recording exactly how you went through it. So anyone else can come behind you. Those artifacts can be converted into templates for a student to follow along that same journey you did.

01:41:23 - Patrick Chouinard
Claudebot used an identity prompt and a soul prompt to define its own behavioral pattern. I've merged their version with the personality of an AI assistant I've always used on ChatGPT [tool:ChatGPT]. So its personality is made to be a little bit abrasive, but also really confrontational — basically challenges me.

01:42:26 - Patrick Chouinard
The one thing I would like to see — my next week's work — is I want to give it the ability to code, but I want to figure out a way to make it understand that I want it to code for itself. Don't code something for me to build or for me to use. Code something that will extend your own capability in order to help me.

01:47:25 - Juan Torres
<Q>What kind of tools are you thinking of downloading to your virtual machine in order to facilitate your Claudebot — CLIs, or what are you thinking?</Q>
<A>To me, once it has a productivity suite, a Google suite, email, a way to communicate, a GitHub account, and it has Claude Code — after that, all the other software are made for humans, so for it to use it, it will downgrade its performance. That's why I wanted it to learn how to code for itself, so it can create CLI tools that are probably going to be horrible for humans to use, but highly tuned for the assistant to use.</A>

01:48:10 - Patrick Chouinard
▶ The nice thing if you do that is that you can push security up the wazoo because it doesn't mind typing a 200-character password every 10 seconds if it has to. So you can make things very, very secure — too complicated for a human to manage, but it makes the assistant more secure.

01:51:00 - Brandon Hancock
<Q>Is this a dedicated device or server?</Q>
<A>A dedicated VM running on Proxmox in a divided VLAN, an isolated VLAN with firewall rules to isolate it, and it can only be communicated with through a specific list of ports.</A>

01:56:00 - Jake Maymar
Claudebot is doing two different things: it's vectorizing the information in a `.db` structure, and it's also doing BM25 [tool:BM25] — Best Match 25 — which is a search method. It's a combination of both of those search methods that helps it create this personalized experience, which is why people are really raving over it — it feels like it knows them.

02:01:00 - Brandon Hancock
▶ If you have a Windows machine and you don't have any other option, use WSL at the very least, but otherwise a Docker container — but isolate it. Don't run that because it has access to the file system. Any prompt injection that happens, it could leak everything on your machine.

---

<!--SEGMENT
topic: Developer Tooling: RAG, Embeddings & Project Management
speakers: Scott Rippey, Brandon Hancock, Ty Wells, Glenn Marcus, Juan Torres
keywords: RAG, Voyage AI, Cohere re-ranking, ChunkHound, OpenAI embeddings, Supabase edge functions, PDF chunking, Clarity app, GitHub integration, NeuralSpark, BM25, tiktoken, GSD framework, spec-driven development
summary: Scott demos his "Clarity" developer tool — a project tracker that links to GitHub repos, optimizes Claude Code prompts, and imports meeting notes. The group discusses RAG architecture (hybrid keyword + vector, Cohere re-ranking, recursive LLM as layer 3), PDF chunking strategies, and Voyage AI as Anthropic's recommended embeddings partner. Glenn then demos the GSD (Get Stuff Done) framework for spec-driven development, showing how it acts as an AI product manager that interviews the developer, breaks work into phases and tasks, and maintains file-system memory for resumable, parallelizable agent execution.
-->

02:03:43 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So what I coded through Claudebot — I want a developer tool called Clarity [tool:Clarity], where you log in and create a project, and you can link your GitHub repo. It can actually know your documentation, automatically pull the CLAUDE.md, the docs. I can write prompts in here, and I have a Claude Code prompt optimizer that does this looping thing — you can literally word-vomit the worst thing ever and it will organize this into a loop using Context7 [tool:Context7] for planning and then verifying.

02:05:36 - Ty Wells
I want like a one-stop shop tracking for a developer that's still connected to your GitHub repo — tracking all the decisions, tracking my code changes, tracking prompts. I'm trying to build this cohesive ecosystem that totally manages your coding project in one main window.

02:09:07 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
▶ What I would focus on doing is meeting people exactly where they're at and what they're already using — almost doing a micro SaaS. What is every developer on earth doing right now? Claude Code. So what I would do is go back to the WordPress days — when WordPress came out, how did people make an absolute ton of money? They made small microservices or micro SaaS around it. Either templates or something to allow Claude Code to be 10 times easier to use.

02:12:29 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
▶ Voyage AI [tool:Voyage AI] — that's apparently someone Anthropic's got a partnership with for doing embeddings. They're owned by MongoDB.

02:16:26 - Glenn Marcus
Did anybody mention ChunkHound [tool:ChunkHound] earlier? I'm using that for RAG-ing up or indexing my local code bases. They also recommend using Voyage AI. Voyage AI gives you like 200 million tokens free, which is great for most of the models.

02:17:27 - Brandon Hancock
▶ I did this whole layer two, layer three thing with RAG — layer two is re-ranking through Cohere [tool:Cohere], and layer three is a recursive language model. I reverse-engineered it and built it into the knowledge base. Layer one is RAG and keyword hybrid, layer two is re-ranking, and then it feeds that into layer three which is recursive. I did it using Claude SDK tools because it can grep, it can search, it can do all those things.

02:19:00 - Juan Torres
I did finally switch to Claude Code to do my editing of code. For complex tasks, I don't need to repeat myself — it tries it and does it on the first trial. What I do is I have still my Cursor [tool:Cursor], and then on my other screen I just have the extension of Claude Code, and I start basically using both in order to speed up through my tasks.

02:20:10 - Juan Torres
I was working on an agentic system for extraction of vendor names from description columns in a general ledger sheet for an accounting firm. I've also created a measure of token utilization. I want to A/B test when you carry out certain agentic extractions — what are the things that are decreasing the total amount of token utilization per agentic run.

02:21:27 - Brandon Hancock
▶ Tiktoken [tool:tiktoken] — that's probably one of the most popular tools to actually track token usage. And to do it preliminarily too — before you actually do the embedding, if you're working with some models, you have to ensure that your payload is under a certain token size. You can always use tiktoken to go, oh yeah, I am below 1,000 tokens, I can save this to the database.

02:43:43 - Glenn Marcus
I've been playing around this week with the GSD framework [tool:GSD framework] — Get Stuff Done — with some mixed results. I've been a big promoter of spec-driven development since early days with vibe coding, so I like to call it now VibeSpec-ing. I started with SpecKit and Amazon Hero IDE, which had a spec-driven development framework built in.

02:44:29 - Glenn Marcus
I told it to build a single web page app that displays how many days have passed since the last Claude Code release, styled like a construction safety sign, fetching a release date from GitHub and showing a snarky message that escalates in drama as the days pile up.

02:45:00 - Glenn Marcus
▶ If you're not familiar with GSD, it comes with a whole bunch of commands: you define it, it helps you — it interviews like a product manager, draws out from you all the user-facing specs and goals of the project, then starts to iterate. It breaks it up into phases, you can discuss the phase, research the phase, then it breaks it up into tasks. You get to a point where you have everything spec'd out in file-system memory through markdowns.

02:47:36 - Glenn Marcus
▶ Once you define it, it has its own built-in RALF loop — it can just go forever. It's not only a good product manager, it's also a project planner and project manager. Every discrete handoff ends with a commit, so you can roll back and branch and fork and try different ideas.

02:49:39 - Brandon Hancock
▶ The project management and memory system it builds for itself makes it interruptible, resumable, and idempotent — you can re-enter at any time. That's what makes it really powerful, especially when you start thinking about running multiple agents all attacking 100 tasks — it's also scheduling the sequence, knowing when tasks are dependent on others, running them sequentially or in parallel as needed.

---

<!--SEGMENT
topic: AI Futures, AGI Debate & Claudebot Enterprise Opportunity
speakers: Jake Maymar, Ty Wells, Scott Rippey, Brandon Hancock, Juan Torres, Ryan C
keywords: Dario Amodei, Anthropic, AGI, technological adolescence, Claudebot open source, enterprise AI agent, sensor arrays, AR glasses, Ryan's social media automation, avatar content generation, Agen, Suno
summary: The call closes with a wide-ranging discussion sparked by Dario Amodei's essay on AI's "technological adolescence." Ty and Scott debate whether current models constitute AGI, settling on the view that predictive scaffolding plus collective human critical thinking is driving exponential capability growth. Jake envisions Claudebot as a launchpad for enterprise-grade AI agent platforms. Ryan shares a paid project to build a fully automated social media content pipeline for a billionaire client — scraping crypto/news Twitter, generating AI avatars, voice-cloning, and auto-posting. Brandon frames this as a productized service opportunity and recommends connecting with Mitch for AI video expertise.
-->

02:30:16 - Jake Maymar
My mind is still blown on Claudebot. I started thinking — Patrick said just giving the bot the tools so it can just do what it's doing — reminded me of like 10 years ago, NVIDIA said we made all these chips, and he showed this chip and goes, we don't even know how this is made. But it works. And keep in mind, this is 10 years ago. What the hell are they doing now?

02:31:32 - Jake Maymar
I kept thinking Claudebot — it's very early on, but it's basically building the tools that it needs, communicating in a language that we probably don't understand. I thought that was really interesting — the security level where basically make it hard for a human to interact with it. But I think the next level is making it hard for another malware computer to interact with it.

02:32:00 - Jake Maymar
▶ Think businesses. Think small software, but then also think big enterprises. Anytime something like this comes out, it is a beautiful idea to think: how could I build a secure version of this? How can I make it to where it's easy to manage accounts, each account has certain credentials, then it's in its own different instance on their servers? If I was to have a moonshot idea — Claudebot has kind of showed everyone's talking about it, so every industry is probably like, how can I get something like this for us?

02:35:29 - Ty Wells
<Q>So Dario's the founder of Anthropic, and he basically posted this really interesting essay talking about the evolution of AI, kind of where it's going. I think we're already at AGI — I'm seeing models move across verticals with no problem whatsoever.</Q>
<A>I have an opinion on that, because it's all predictive. We are not anywhere close to AGI. This is just machine learning models. It's predicting based on patterns. It looks smart to us. But it's just that it has so many domains of predicted patterns — it's a scaffolding that is improving rapidly.</A>

02:37:00 - Ty Wells
▶ With that scaffolding — all human knowledge on that scaffolding — the explosion's crazy. We're smart people. You're adding that to a predictive analytic system, you're going to get some good stuff out of that.

02:38:20 - Jake Maymar
▶ Think of all of us using Claude Code — that's billions of people basically writing valuable information, sharing critical thinking on a regular basis in all verticals and across all nations. You've never seen anything like that. No matter how many conferences you would have gone to on a specific subject, that's nothing compared to 7 billion people pushing their thoughts through and it synthesizing that information.

02:39:08 - Juan Torres
Yeah, that's why Dario posted that essay. It's kind of fun — in the very beginning it's like talking about Contact, the movie, where Jodie Foster is selected to talk to the aliens, and the number one question she asked them was: if you could ask the aliens just one question, what would it be? Her reply: I asked them, how did you do it? How did you evolve? How did you survive this technological adolescence without destroying yourselves? [link:Dario Amodei essay on AI's technological adolescence]

02:23:07 - Ryan C
I've got a couple of other big AI projects. I've got to build a completely custom platform to build out completely automated content — essentially scrape two or three Twitter accounts on crypto news and right-wing American news. And then it's literally going to be like an AI avatar, voice clone, writing the script, storyboarding it, generating it, and then putting that into a background. Something that's going to AI-edit the whole thing together, write a post, and then post it to his social media platforms on just a looping basis. He's a billionaire, so he's got like a million followers on Twitter.

02:27:01 - Ryan C
He's literally paying me a lump sum to build it, and then he's going to pay me $2,000 a month to maintain it.

02:27:13 - Ryan C
Do that 20 times? That's pretty sick. I'm using Agen [tool:Agen] or something to do the AI avatars. That's $300 a month. It's not cheap to run.

02:28:35 - Brandon Hancock
▶ If you can successfully do that, like I'm sure you will — for basically creating avatars to help people who want to have a digital presence — that skill to then copy and paste is insanely powerful. Once again, going back to productized services: if you can say, hey, I have built a thing like this for this guy, I'd be happy to do it for you too. You do one of those a month — dude, you're golden.

02:29:22 - Brandon Hancock
▶ I would talk to Mitch — he's probably the resident expert on all things AI and video. He's been actively trying to crack automating the video editing with AI.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript and were not present in the SPEAKER_ALIASES context block (which was not supplied in this session). All names have been passed through unchanged:

- Tom Welsh
- Marc Juretus
- Paul Miller
- Brandon Hancock
- Patrick Chouinard
- Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
- Juan Torres
- Morgan Cook
- Ty Wells
- Jake Maymar
- Prem
- Ama
- Raghav Ram
- Ryan C
- Hemal Shah
- Glenn Marcus
- Elijah