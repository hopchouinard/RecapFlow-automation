=== SESSION ===
date: Unknown (references January 1st HMRC regulation, New Year 2026 resolutions, and "last week" demos)
duration_estimate: ~2 hours 47 minutes (00:41:00 – 03:28:19)
main_themes: Startup funding announcements, AI-powered development tools and workflows, Git worktrees for parallel development, agentic orchestration systems, digital signage SaaS, machine learning for small businesses, live call coaching AI, RAG applications, model selection and cost optimization, deepfake awareness

---

<!--SEGMENT
topic: Pre-Call Chat and Deepfake Awareness
speakers: Tom Welsh, Patrick Chouinard, Bastian Venegas Arevalo, Ty Wells, Marc Juretus
keywords: deepfakes, AI-generated video, Robert De Niro, HSBC fraud, WhatsApp impersonation, Zoom deepfake, social engineering, phishing, cybersecurity, crypto capital gains tax
summary: Participants warm up before the formal call begins, discussing AI-generated deepfake videos circulating online, including a suspected AI-generated Robert De Niro video and a real-world $25M bank fraud executed via deepfake Zoom call. A similar WhatsApp-based impersonation incident from Chile is also recounted. The segment highlights growing difficulty distinguishing real from AI-generated content and the social engineering risks this creates.
-->

00:41:00 - Tom Welsh
Thank you.

00:41:32 - Tom Welsh
Hey, Patrick.

00:41:36 - Patrick Chouinard
Hey, Tom.

00:41:38 - Tom Welsh
How goes it?

00:41:40 - Patrick Chouinard
Good, good. Yourself?

00:41:43 - Tom Welsh
Yeah, first day back at a proper job. Leaving the house and going to a client site. Exciting, but not really.

00:41:55 - Patrick Chouinard
Don't worry. They've got project managers that cannot manage projects.

00:42:08 - Patrick Chouinard
Don't worry, I have architects that don't want to learn AI.

00:42:16 - Tom Welsh
There's just so many of them. Oh, no, it's just a bubble that won't catch. Seeing that, you're just missing the boat completely. You can't put the genie back in the bottle. It's out there.

00:42:31 - Patrick Chouinard
Exactly. It's like, oh, you can't force me to learn AI. No, but AI is going to force you out of a job when we find someone who's able to learn.

00:42:42 - Tom Welsh
The market will force you to learn AI.

00:42:50 - Tom Welsh
I did a post yesterday on the group. There's a YouTube video of supposedly Robert De Niro spouting how bad Trump was. He literally sits there in a three-quarter view of the camera, his head turns, blinks a couple of times, a few hand movements. No background. That's got to be an AI render — it just seems so fake.

00:43:41 - Tom Welsh
My background is cybersecurity. There was a thing probably three years ago now where there was a conference call on Zoom with the chief exec of a bank, the chief financial officer, and one of his underlings. It was a completely faked deepfake video, and they got the employee to move $25 million to a different bank account.

00:44:14 - Tom Welsh
That's just classic phishing. If somebody says move funds to a new bank account, don't do it. I think it was HSBC.

00:44:31 - Patrick Chouinard
Not over a Zoom meeting.

00:44:40 - Tom Welsh
She said it was just so believable because you could see the people she knew on screen.

00:44:55 - Bastian Venegas Arevalo
We had a similar story here in our country. I think it was also a deepfake. Someone from the Ministry of Education — there was a vault in the facilities and someone called via WhatsApp to the guards. They got them to open the safe and remove hard drives and computers because they saw the minister on video. The minister is bald and was wearing a cap. They were talking to him via WhatsApp, and then the caller removed the video and continued speaking audio-only. It was a huge scandal, about two or three years ago.

00:45:51 - Tom Welsh
Yeah, that seems to be the era when it started to happen. The Robert De Niro video the other day looked quite convincing, but you can tell — his voice changes and goes a bit English at some stages.

---

<!--SEGMENT
topic: Brandon's EMS Startup Funding Announcement
speakers: Brandon Hancock, Dmitry Avramenko, Ty Wells, Patrick Chouinard, Bastian Venegas Arevalo, Marc Juretus, Tom Welsh
keywords: EMS Soap, SOAP reports, medical billing, RAG application, Tiny Seed, funding, C Corp, fire departments, ambulance companies, Florida, ShipKit, embedding models, Google deprecation
summary: Brandon Hancock announces that his startup EMS Soap — which helps EMTs and fire departments generate SOAP reports for insurance billing using a RAG-based AI application — has received funding through Tiny Seed. He explains the origin story: his co-founder (an EMS chief in Florida) built a GPT proof-of-concept, then hired Brandon to build a production RAG app. The segment covers the business model (annual contracts, high-margin token resale), a heads-up about a deprecated Google embedding model in the ShipKit RAG template, and the insight that the same technical template applied to different enterprise problems commands vastly different prices.
-->

00:46:07 - Ty Wells
I see we got some exciting news in the form of an email from Brandon.

00:46:24 - Bastian Venegas Arevalo
He's going all in on the startup.

00:46:29 - Ty Wells
<Q>Does anybody know what the project is about? I don't know Tiny Seed.</Q>

00:46:45 - Ty Wells
<A>I know the startup is in medical billing.</A>

00:47:36 - Bastian Venegas Arevalo
Brandon has been nailing it. I think it's been less than 12 months since he quit Cree AI [tool:Cree AI].

00:48:47 - Bastian Venegas Arevalo
Yo, Brandon, congratulations.

00:48:53 - Brandon Hancock
Thank you, Bastian. Sorry, I literally just got back from a long walk. Trying to get outdoors a little bit more.

00:49:09 - Brandon Hancock
Touch grass — that's a resolution for 2026.

00:49:15 - Brandon Hancock
While everyone's getting on, I literally just sent out an email two seconds ago. I want to clear it up if anyone has questions.

00:49:25 - Dmitry Avramenko
I was shocked. I woke up and I wasn't going to join, but I saw it. Got to congratulate you, man.

00:49:35 - Dmitry Avramenko
Brandon, I think you're living proof that dedication, commitment, and perseverance more often than not works.

00:49:55 - Brandon Hancock
Yeah, so — quick recap. I did a startup with a co-founder. It's called EMS Soap [tool:EMS Soap]. I'll show it to you guys real fast.

Basically, we're helping EMTs — fire departments and ambulance companies — build SOAP reports, which they then use to properly bill insurance companies. It's a huge pain, there's a ton of room for error, and if they don't do the reports right, they lose money. Fire departments are losing a ton of money.

My partner is actually the EMS chief down in Florida, one of the bigger cities. He started off making a GPT [tool:GPT] as a proof of concept in his own organization. His guys loved it — they were addicted. He hired me back in July to build it out, take it from a GPT to a real-world RAG application [tool:RAG]. Since then we've just been taking on more customers and growing. Right now we have the biggest ambulance company in Florida. It's growing very fast.

In November we actually got funding — that's the first time I've ever made a C Corp and done all the fundraising stuff, so I had to get very smart on that very quickly.

▶ The lesson learned is: solving enterprise problems pays extremely well — kind of like what Dan Martel mentioned when he hopped on one of the calls.

00:52:00 - Brandon Hancock
The RAG template [tool:ShipKit] is the foundation for one of the biggest projects in ShipKit, and it's basically the same thing we use. So all the templates I was giving you guys — it's what I'm using in the real world too.

00:52:16 - Dmitry Avramenko
<Q>Is the RAG template still available?</Q>

00:52:17 - Brandon Hancock
<A>Yes, it's still there. Heads up though — one of the embedding models, Google's deprecating it. We're working on teaching you guys how to migrate from the old deprecated model to the new one so you don't get blocked. It still works right now, but an update is coming.</A>

▶ The same template applied to different problems is worth different amounts of money — that's the key insight.

00:53:00 - Dmitry Avramenko
<Q>Is your company profitable from the beginning, or are you still trying to make money like every startup?</Q>

00:53:08 - Brandon Hancock
<A>Right now we're not really paying ourselves, but we're not losing money at all. We're doing annual contracts — tens of thousands of dollars each. Tokens cost dollars and you sell them for hundreds. That's why I love AI — very high margins. Profitable from day one.</A>

---

<!--SEGMENT
topic: Dmitry's Agentic Orchestrator Startup
speakers: Dmitry Avramenko, Brandon Hancock, Tiran Dagan
keywords: agentic orchestrator, autonomous AI, software development lifecycle, Graphite, Cursor acquisition, Git merge management, parallel agents, LinkedIn traction, Genom, prompt A/B testing, GitHub, sprint retrospective
summary: Dmitry Avramenko announces he is building an agentic orchestrator platform designed to replace full software development cycles with autonomous AI agents. He reports strong early traction — 6,000 LinkedIn views and three CIOs reaching out within a week, including one seeking to sell the product in the Middle East. He demonstrates a "George" agent running a weekly sprint retrospective and discusses Graphite (acquired by Cursor) as a solution to the parallel Git merge-ordering problem that arises when running many agents on Git worktrees simultaneously.
-->

00:53:49 - Dmitry Avramenko
I have an announcement also. I'm doing an agentic orchestrator, which — if they're going to be the biggest things we hear about in 2026 — is basically fully autonomous AI replacing a full software development cycle.

I just posted the link to my LinkedIn post about what I'm doing. I got like 6,000 views, I have three CIOs of companies reach out to me already this week, and they want to understand more. One wanted to sell my product in the Middle East — even though it's the first demo. He's like, "I have customers who will buy this tomorrow."

I also have an AI startup called Genom [tool:Genom] that contacted me — they're basically managing your prompts and doing A/B testing on your prompts. And Brandon, I think you may want to use my product because it's basically going to let you sleep while my agents work for you.

00:55:22 - Dmitry Avramenko
You'll be able to watch the demo on YouTube. I'm demonstrating George, one of my agents, who is kind of like a Scrum Master. I'm running a weekly sprint review report with him. He's actually documenting everything to GitHub as we speak.

00:56:00 - Dmitry Avramenko
However, the Weekly Agentic Sprint Retrospective — George is conducting the retrospective, finding issues in our process, and documenting everything to GitHub.

00:56:24 - Brandon Hancock
One thing I have been doing — the templates I'm using in ShipKit are the exact same templates we're using to build the startup. And a cool thing I started doing today: Git worktrees [tool:Git worktrees]. I've been 100% opposed to them, and now I have given in. I'm churning through tokens. I never thought I'd hit the Max plan limits, but now I have Git worktrees and every feature I'm building is in its own worktree. I'm literally a team of 10.

00:57:06 - Tiran Dagan
<Q>Are you using Git worktrees more as a way to segregate features? What aspect of that are you using?</Q>

00:57:16 - Brandon Hancock
<A>Normally when I'm coding, I use Git worktrees to follow best coding practices — building small features in parallel. One of the biggest problems is you end up with no traceability because each commit ends up being a mixed task. With Git worktrees, each branch gets its own worktree, I build the thing, and I'm doing it all in parallel. Every branch can then be tested better. It provides more clarity.</A>

00:58:06 - Tiran Dagan
<Q>Are you also using the LLM to merge and reconcile all of the changes?</Q>

00:58:13 - Brandon Hancock
<A>Yes. The only gotcha is when you start making database changes in parallel — that's the bottleneck. If you want to make database changes, you kind of have to do those in series. The second it's all UI, pick up as many parallel changes as you want.</A>

00:58:33 - Tiran Dagan
You can also have branches on Supabase [tool:Supabase]. If you're working on a separate branch and have a Supabase branch, you can probably handle that as well.

00:58:52 - Brandon Hancock
The only gotcha is the metadata journal. With Drizzle [tool:Drizzle], there's a file called your journal that's tied to incremental updates. When you go from database change 63 to 64, it's like — wait, there are three 63s now. What's the proper order? That's been the issue.

00:59:10 - Dmitry Avramenko
Your problem can be solved with Graphite [tool:Graphite]. Graphite is the company that Cursor [tool:Cursor] just acquired. They're working on exactly the problem you're describing — because agentic problems, if you start spanning 10 or 15 parallel agents working on Git worktrees, the order of merge is very important. Graphite is solving exactly this. They integrate with GitHub [tool:GitHub]. You just outsource all the merging to them.

01:00:00 - Brandon Hancock
That's awesome. The database merging is the main bottleneck I'm running into.

01:01:34 - Brandon Hancock
Just of note — Cursor bought them, not Anthropic.

01:01:45 - Dmitry Avramenko
Oh yeah, Cursor bought them, not Anthropic. Sorry.

▶ Eventually, with tools like Graphite managing merge order, you'll be able to run 50 or 100 parallel agents — Dmitry plans to push his agents to the cloud as remote sub-agents.

---

<!--SEGMENT
topic: Tom Welsh's Contract Work and Offline LLM Benchmarking
speakers: Tom Welsh, Brandon Hancock
keywords: Qwen3-Coder-30B, Ollama, Cursor, offline models, WordPress, creative agency, subcontracting, boilerplating, token throughput, client work
summary: Tom Welsh shares that he has started a new client contract working on WordPress websites through a creative agency. He also discusses his benchmarking of offline LLM models via Ollama, finding that Qwen3-Coder-30B performs well as a coding agent on Cursor while commuting without internet access. Brandon asks about the WordPress contract market, noting that legacy systems still generate real demand.
-->

01:02:00 - Tom Welsh
Yeah, I started a new contract today. Nothing overly exciting — just doing client work, WordPress websites and stuff like that. That's good money.

01:03:01 - Tom Welsh
I did a post on the site the other day — I saw a Robert De Niro YouTube video and I'm convinced it's AI-generated. It's just got all the nuances: no branding behind it, he just sits three-quarters to the camera, his head moves slightly side to side. It just looks wrong.

01:05:13 - Tom Welsh
I was playing with Cursor [tool:Cursor] today. I've done quite a bit of benchmarking on Ollama [tool:Ollama] models and taking stuff offline. Qwen3-Coder-30B [tool:Qwen3-Coder-30B] seems to be quite a good coding agent offline using Ollama. I've had that plugged into Cursor and just using it on the train. It seems to be churning out code quite happily and rips through tokens quite nicely. For boilerplating, I found that quite useful.

01:05:50 - Brandon Hancock
<Q>For the WordPress contracts — are clients just paying because they don't want to deal with the time of doing it themselves? They just don't have a development team?</Q>

01:06:13 - Tom Welsh
<A>My client is a creative agency, and their clients need websites. I'm subcontracting through the creative agency. They were trying to use things like Adobe Fonts [tool:Adobe Fonts] with WordPress and never knew anything about it.</A>

▶ Legacy systems still need work done — the barrier to entry for development has risen with AI, but demand for WordPress and similar work persists because clients simply don't have the knowledge or time.

---

<!--SEGMENT
topic: Ty Wells' Machine Learning Platform for Small Businesses
speakers: Ty Wells, Brandon Hancock, Tiran Dagan, Bastian Venegas Arevalo
keywords: machine learning, predictive analytics, customer churn, small business, POS data, Stripe integration, Hyros, Alex Becker, ShipKit Studio, CSV data ingestion, LLM field mapping, Simon mascot
summary: Ty Wells demos a machine learning platform built for a hackathon that brings predictive analytics (customer churn, sales forecasting) to small businesses at an accessible price point. The platform includes a guided data upload flow, model training with a mascot called Simon, and a dashboard for managing trained models. Brandon suggests integrating with Stripe and ad tracking tools (inspired by Alex Becker's Hyros) to automate data collection. Ty also previews his ShipKit Studio tool, which wraps ShipKit to generate full applications from a roadmap.
-->

01:07:19 - Brandon Hancock
Ty, you're up next, man. What awesome projects do we got cooking?

01:07:22 - Ty Wells
Oh, we have tons of projects, but today I'm short on time, so I'm just going to show you the machine learning one.

01:10:00 - Ty Wells
So this was our hackathon entry in another community. Basically it's bringing machine learning predictions to small businesses. Small businesses have a lot of data they collect on their POS [tool:POS] or whatever they use, but they don't know anything about machine learning. All the big companies use machine learning and predictive analysis to determine what you're going to purchase next — all the stuff that shows up on Amazon [tool:Amazon] and e-commerce websites. We built this platform to allow businesses to do those same things at a price point that makes sense for them.

01:11:00 - Ty Wells
There are two paths: a step-by-step guide or a chat interface to see how to collect data. Machine learning is very specific — there's no agentic side to it. The data has to be correct and in a certain format. You can do different predictions like customer churn based on your incoming data.

01:11:46 - Tiran Dagan
<Q>Quick suggestion — I solved this particular problem in a few other apps I built: make a quick LLM call so you feed any CSV someone gives you and then figure out the fields and the mapping to your structure.</Q>

01:12:46 - Ty Wells
<A>Yes and no. For a customer to just feed any data in — what we do is data aggregation. If you feed in data at a transactional level, we will aggregate it to see if it's valid for any particular prediction use case. If your data is bad, we'll tell you it's bad and tell you why.</A>

01:13:30 - Ty Wells
I've got clean data here. I can download a quality report. I would name the model — let's call this... [laughter] — and then Simon, our mascot, runs the training. You get analytics once it's done on how well the model trained.

01:14:38 - Ty Wells
That's the flow of the application. It gives small businesses an opportunity to use all the data they collect from their customers.

01:14:52 - Brandon Hancock
<Q>Ty, this is sick. Have you watched Alex Becker talk about Hyros [tool:Hyros] at all?</Q>

01:15:16 - Ty Wells
I have not.

01:15:19 - Brandon Hancock
<A>If you look it up — H-Y-R-O-S — he has a YouTube channel dedicated to B2B SaaS. His whole tool tracks ad spend and ties the user journey from Instagram to Facebook to YouTube to figure out which ads drive sales. What's very cool about yours is: the business model works because it's just tracking. The cool thing I'm seeing in your app is the first part — literally just hook me up to Stripe [tool:Stripe], PostHog [tool:PostHog], or whatever you use for tracking, and I'll tell you everything: how people are coming in the door and when people are leaving. Look at Alex Becker on YouTube [link:YouTube/AlexBecker].</A>

▶ Any time you can merge together three or four systems that don't talk to each other and give people actionable insights — for ad campaigns, to reduce churn, for onboarding — you help them print more money and keep customers longer.

01:17:42 - Ty Wells
I'm just finishing up my code cranker — it's going to knock out and test code overnight. I've sort of wrapped ShipKit [tool:ShipKit] around the other tool I was building, the ShipKit Studio. It walks you through a 10-step process of coming up with the idea and a roadmap, and at the end it basically takes the roadmap and just builds you an app.

---

<!--SEGMENT
topic: Framework Choices: Next.js vs Vite vs Astro
speakers: Dmitry Avramenko, Brandon Hancock, Bastian Venegas Arevalo, Ty Wells
keywords: Next.js, Vite, Astro, React, server-side rendering, server components, Lovable, API-heavy applications, prototyping, state management, frontend frameworks
summary: Dmitry asks whether new projects should be built on Vite rather than Next.js, given the trend toward Vite. Brandon and Bastian recommend sticking with Next.js for API-heavy or AI-driven applications due to server components and server-side rendering, while Vite (used by Lovable) is better for quick prototypes. Astro is suggested as an alternative for content-heavy sites with minimal API needs. The group agrees Vite falls short once you need layouts, server-side rendering, or complex state management.
-->

00:00:00 - Dmitry Avramenko
<Q>I see a lot of people moving to Vite [tool:Vite] right now. What's your view on Vite? Would you recommend building new projects on Vite rather than Next.js [tool:Next.js]?</Q>

01:19:13 - Brandon Hancock
<A>I personally would like to stick to Next.js over Vite. Vite is very fast, but from my understanding it's just made for using React quickly. They're missing out on a lot of the additional things Next.js provides — like state management and server-side rendering. Lovable [tool:Lovable] uses it to build apps as fast as possible, which is great when you just want to take an AI prompt into an app, but for a lot of the state and server stuff, I don't think that comes in the box.</A>

01:20:13 - Bastian Venegas Arevalo
<A>That's also my understanding. I use Vite a lot — it's very fast — but just for things that are not really API-heavy. If it has server components and a lot of API and AI stuff, I'd definitely go with Next.js.</A>

01:20:41 - Bastian Venegas Arevalo
It's kind of weirdly in the spot, because if it doesn't need APIs at all, you could almost do it with Astro [tool:Astro] — insane speeds for loading times and you just use dynamic JavaScript islands for interactive parts. I would go with Astro in that case. For prototyping, Lovable is perfectly fine.

▶ Recommendation: Use Next.js for production AI/API-heavy apps, Vite/Lovable for quick prototypes, and Astro for content-heavy sites with minimal interactivity.

01:21:11 - Brandon Hancock
It's great for quick prototypes spun up by an AI. It's simple, but the second you want layouts, server-side rendering, or anything more than a pretty landing page and a very basic dashboard, it kind of falls apart. Would not recommend for production.

---

<!--SEGMENT
topic: ShipKit Roadmap, Agent Frameworks, and Model Cost Strategy
speakers: Brandon Hancock, Dmitry Avramenko, Patrick Chouinard, Marc Juretus
keywords: ShipKit, Git worktrees, Claude Code, Cursor, LangChain, LangGraph, CrewAI, agent frameworks, structured LLM calls, model cost optimization, Gemini, Claude Max plan, task templates, worker SaaS
summary: Brandon outlines his plans to keep updating ShipKit with real-world learnings like Git worktrees, while shifting to intermittent rather than weekly calls due to startup commitments. The group debates the relevance of agent frameworks like LangChain, LangGraph, and CrewAI, with Brandon arguing he now prefers direct structured LLM calls in loops over framework abstractions for production apps. Dmitry proposes a cost-optimization strategy: use expensive models for spec/planning, then cheaper models for implementation, with an orchestrator that selects the right model per task complexity.
-->

01:21:28 - Dmitry Avramenko
<Q>Brandon, you're going to be so busy with your startup — are you going to continue making changes to ShipKit, or is that basically done?</Q>

01:21:38 - Brandon Hancock
<A>The goal for ShipKit: I owe you guys one more walkthrough — the Worker SaaS template walkthrough. For every template I give, I show how to take it and turn it into a real-world app. That's one major thing left. But the big thing I want to keep doing is: as I continue to get smarter and build more stuff, just turn around and put it in ShipKit. As for calls — depending on the week, I'll do intermittent calls. The default is not doing them consistently on a week-by-week basis, but ideally one a month.</A>

01:38:05 - Marc Juretus
<Q>Could you give me the two-minute summary of what Git worktrees are and why I should know about them?</Q>

01:38:17 - Brandon Hancock
<A>Normally, when doing AI development, we're just at our desk saying "build this feature," kicking it off in one Claude Code [tool:Claude Code] session, then starting the next thing in parallel — but all under the same branch. We've technically worked on five or six features that have nothing to do with each other. At a normal company, if you submit a PR with changes A through F that have nothing to do with each other, you'd give your lead developer a heart attack. It's hard to maintain and hard to trace.

With Git worktrees, per branch, every time I want to work on a new feature, I create a new worktree. It clones your whole repository, makes a new folder on your computer, branches off main, and is tied to that new feature. I have five Windsurf [tool:Windsurf] windows open, working on feature one, two, three — all on their own branch. Claude Code isn't competing to edit the same file.</A>

▶ Git worktrees enable true parallel feature development with proper branch isolation — each branch tied to one task, versus dumping 30 changes directly to main.

01:53:25 - Dmitry Avramenko
<Q>Brandon, as Claude Code and other powerful agents emerge, it seems like a lot of people are stopping using frameworks like LangChain and CrewAI. Are they all doomed?</Q>

01:54:01 - Brandon Hancock
<A>Personally, at this point, I'm using them less and less — LangChain [tool:LangChain], LangGraph [tool:LangGraph], CrewAI [tool:CrewAI] — all of them. In production applications, I'm manually doing most of my calls in just regular programmatic ways: do this thing, structured output, go in loops. I actually don't need an agent framework to do loops of structured LLM calls. Most people want: I give you this input, I want this output. If I know the desired input and the desired output, I don't need multi-agents that could go awry — I just need a very structured output to deliver high-quality results every time.</A>

01:44:13 - Dmitry Avramenko
<Q>I obviously run out and get throttled at some point on the $20/month Claude plan. Is it bad to switch over to Cursor when I run out?</Q>

01:44:33 - Brandon Hancock
<A>No, at the end of the day they're both using the same models, just wrapped differently. They're probably 90% similar. Both do great. I will just say I have absolutely loved using Claude Code — since I started using it, I really haven't gone back.</A>

▶ Cost strategy: Use expensive models (Claude Code, Claude Sonnet) for designing specs and planning, then implement with cheaper models. An orchestrator can automatically switch to a cheaper model based on task complexity — this is what Dmitry's platform is building toward.

---

<!--SEGMENT
topic: HP's Live Call Coaching Chrome Extension
speakers: HP, Brandon Hancock, Bastian Venegas Arevalo, Ty Wells, Tiran Dagan
keywords: live call coaching, Chrome extension, Deepgram, speech-to-text, WebSocket, Supabase edge functions, Railway, Render, LiveKit, real-time transcription, sales coaching, SARB framework, LRP framework, call summary
summary: HP (Scott) demos a live call coaching tool he built in three days: a Chrome extension that captures microphone audio, transcribes it in real time using Deepgram, and surfaces coaching suggestions based on frameworks like LRP (Listen, Repeat, Poke) and SARB (Summarize, Ask, Recommend). The backend uses Supabase edge functions and WebSockets. He discusses a bug where the mic drops after ~3 minutes due to Supabase edge function time limits, and the group recommends Railway or Render for persistent WebSocket hosting. Brandon highlights the business opportunity of niching this down to sales team coaching.
-->

00:55:00 - HP
I ended up developing something totally different than what I had planned. In September, I was on a video job in Michigan, sitting there dumping footage, and I had this thought: what if I built a live call coach — transcribing audio and sending it through my frameworks of whatever I wanted to be trained on, getting things live in a dashboard on the side, and then a Chrome extension [tool:Chrome extension] to hit the call and capture my mic. I built it in the last three days and it's working completely except for one little thing I've got to fix.

01:24:06 - HP
So how it works: I've got a Chrome extension. It's a local install — not in the Chrome store. I'm using it for a few of my people, but I'm using it too. The frameworks are LRP — Listen, Repeat, Poke — and SARB — Summarize, Ask, Recommend. But you can use it for sales, brainstorming, catch-ups, interviews, meetings. It contextually knows the type of call.

I do a new session, put in the title and guest name, and set how often you want suggestions to pop up. You can give it pre-call context notes and upload context files — all goes into the database. It's Supabase [tool:Supabase] on the backend. The edge functions have all the AI code — framework stuff, WebSocket, and I'm using Deepgram [tool:Deepgram].

01:25:00 - HP
I was using Whisper [tool:Whisper] — I'd never heard of Deepgram — and apparently it's a known issue that Whisper is terrible with streaming stuff in chunks. It'll hallucinate and give you garbage characters. So I did some research and found Deepgram, which is actually even cheaper. They give you a $200 credit. And it's stupid accurate.

▶ Deepgram is purpose-built for real-time speech-to-text streaming and is cheaper and more accurate than OpenAI Whisper for chunked streaming use cases.

01:31:11 - HP
The only issue I'm debugging: Supabase edge functions have a time limit of staying connected — anywhere from three to six minutes. Every time around the three-minute mark, it was cutting off. So we just have to reconnect the WebSocket and keep the same session. Got it all working to where it stays recording the guest on the tab, but it's dropping my mic after three minutes. That's the only thing I'm testing.

01:31:49 - Brandon Hancock
<Q>If the Supabase edge function timeout is becoming an issue, you might want to look at an external service. Railway [tool:Railway] — you just give it a Docker image and it goes. That would be the next easiest step.</Q>

01:33:26 - Ty Wells
<A>Look into Render [tool:Render] when you're there. I was on Railway and I switched to Render for stateless services. It ran better for me.</A>

01:33:44 - Tiran Dagan
I've been using Render for all of my deployments. They have an MCP and some advanced management features. Very cool.

01:34:41 - Brandon Hancock
Bastian had a cool tip as well — if you want to have it all together, LiveKit [tool:LiveKit] would be a cool alternative. It works with Deepgram under the hood as well.

▶ For persistent WebSocket connections beyond Supabase edge function limits, use Railway, Render, or LiveKit as dedicated hosting services.

01:35:33 - Brandon Hancock
Real fast, guys — Deepgram has multiple models for their voice. We actually use one of their medical models, and it's phenomenal. When you start doing acronyms and medical terms, regular models might substitute an English word. Deepgram's medical model handles that correctly. They're usually the same price as the base model. Very underrated tool.

01:27:30 - Brandon Hancock
Final thing — a cool mental model. You've built level one where the person clicks. Level two: any action you're taking is just another AI call to say "did I say this?" It could auto-check it off. Every time you build a manual feature, think about whether an AI call could automate it.

---

<!--SEGMENT
topic: Ryan's Screenly Digital Signage SaaS
speakers: Ryan - One Stop Creative Agency, Brandon Hancock, Bastian Venegas Arevalo, Tiran Dagan, Dmitry Avramenko
keywords: Screenly, digital signage, estate agents, QR code, pay-per-lead, Cloudflare R2, node-based flow builder, mini PC, kiosk mode, Bolt, Claude Code, review display, property management API, subscription SaaS
summary: Ryan demos Screenly, a fully branded digital signage SaaS he built in approximately one week. The platform allows businesses to manage content on screens via a node-based flow builder with custom transitions, review displays, and property integrations for estate agents. The backend uses Cloudflare R2 for storage, and a local Windows mini-PC package runs the display in kiosk mode, syncing content from the cloud. Brandon offers to connect Ryan with a brewery client whose existing screen software just broke. Ryan also previews his social media management app nearing its first client onboarding.
-->

02:10:39 - Brandon Hancock
Next up, Ryan, what's up, buddy?

02:10:43 - Ryan - One Stop Creative Agency
It's quarter past midnight, so morning. I think last week I mentioned I was going to be building a screen software SaaS project. Pretty much done.

02:11:22 - Ryan - One Stop Creative Agency
I've fully branded it. It's called Screenly [tool:Screenly]. I'm going to sell it to as many businesses as I possibly can on a subscription model. It's a one-pager on the front end — talks about features, stats, done a load of market research. All the text is kind of final, just need to replace stock images.

02:11:57 - Ryan - One Stop Creative Agency
Ironically, my favorite page on the entire website is the login page — it's just a stunner. I'm really happy with how this turned out in terms of its look.

02:12:29 - Ryan - One Stop Creative Agency
The front page and login page — I took inspiration from other websites, gave it screenshots, and I designed the UI of those two pages in Bolt [tool:Bolt], then brought it into Claude Code [tool:Claude Code]. Claude Code went "yeah, this is great" and rewrote the whole thing while keeping the look and feel. The pulsing background — I didn't ask it to do that. The image I gave it had a picture behind the text and it just did that.

02:13:15 - Ryan - One Stop Creative Agency
I started designing this for QR generation for estate agents where it can API into their property management systems and pull out their properties. I was going to do a pay-per-click or pay-per-lead type thing as an alternative to Google AdWords — on their screens there's a QR code people can scan, it takes you to a branded page with property images and a form, sends the lead to the estate agent, and they pay per lead.

02:14:00 - Ryan - One Stop Creative Agency
And then the normal subscription model where they pay and just get their properties on a screen, maybe with reviews inserted and custom slides for seasonal messaging.

02:15:48 - Ryan - One Stop Creative Agency
I then built an entire node-based flow builder [tool:flow builder]. You can add a node, put in your images, reviews, embed HTML, create completely custom slides with different templates. You can change transitions between each node, upload your own stinger, change duration — all that. That then syncs to a local package on a mini Windows machine. I downloaded the BIOS and kernel to get rid of Windows updates so it never restarts, put it in kiosk mode, and it's a full-blown little application. I put in a provisioning code to tell it which screen it is, and it syncs updated information every 15 minutes or however often I want.

▶ The display system uses a local mini-PC in kiosk mode running Chrome, syncing content from the cloud via a provisioning code — no ongoing manual updates needed.

02:17:02 - Brandon Hancock
I mentioned in the last call — I built something similar five years ago, more to hook up to a point of sale. It broke today for one of my friend's businesses — a brewery downtown. If you want an early testimonial from a brewery and are looking for first customers at a discount, I'd be happy to connect you.

02:18:31 - Tiran Dagan
<Q>Ryan, what are you using for the flow building? Any particular open-source library?</Q>

02:19:34 - Ryan - One Stop Creative Agency
<A>I can't remember off the top of my head, but I'll ask Claude Code what tech stack the flow builder is using and chuck it in the chat.</A>

02:19:38 - Juan Torres
Just put something in the chat — React Flow [tool:React Flow] looks pretty cool.

---

<!--SEGMENT
topic: Patrick's Fieldy Wearable and AI-Driven Network Engineering
speakers: Patrick Chouinard, Brandon Hancock, Dmitry Avramenko, Bastian Venegas Arevalo, Ty Wells
keywords: Fieldy, Limitless pendant, N8N, Claude Code, VLAN, firewall, network engineering, Twingate, Tailscale, ngrok, tunneling, ChatGPT voice, GitHub issues, infrastructure as code, AI-assisted networking, wearable AI
summary: Patrick Chouinard describes his plan to use a Fieldy wearable (similar to the now-discontinued Limitless pendant) to record his day, feed transcripts via webhook to N8N, and have an AI agent decompose, categorize, and act on tasks — including triggering Claude Code to implement code changes. He also shares how he used Claude Code as a network engineer to redesign his home network with VLANs and firewall rules, documenting everything as infrastructure-as-code in a Git repo. Dmitry describes a parallel project using ChatGPT voice to brainstorm while riding, then automatically creating fully-documented GitHub issues for implementation.
-->

01:56:00 - Patrick Chouinard
Back to work today. We're testing a different AI platform and I have an account for Claude at work, but I've been working the past three weeks with my own Max account. I didn't know the one they gave me at work is actually just a $20/month account. Ran out of tokens at 9:15.

01:57:06 - Dmitry Avramenko
Basically last week I decided to get myself a Fieldy [tool:Fieldy] — basically the same thing as what Limitless [tool:Limitless] pendant was.

01:57:32 - Patrick Chouinard
Field-Y.

01:57:54 - Patrick Chouinard
There's a webhook for it. My idea was not so much to use it for all the summary and research — I just wanted to do the transcription, so it can feed it to N8N [tool:N8N]. N8N would then take it and through agent configuration, decompose everything it gets, categorize, prioritize. And then I thought — now that I've decomposed all of that, I'm sure there's a whole lot there that says "I need to do this, I need to implement X" — why don't I just have Claude Code [tool:Claude Code] do it?

So just speak, do my thing, go through my day, don't bother with anything, feed it back to a pipeline, and whatever is "implement X," start to do it.

02:00:00 - Patrick Chouinard
But I realized I have to be careful — I don't want it to delete production. So whenever it has an action to do, my thinking is I'd feed it back into a dashboard app on my phone. You just have: "here's the thing I think you've asked me to do" — you approve or reject.

02:00:41 - Patrick Chouinard
It's basically an all-day assistant in the background doing: "this is something he needs to remember, let's shoot that to Obsidian [tool:Obsidian]; this is something he wants to do, let's propose to do it for him."

02:00:58 - Patrick Chouinard
Then I realized — I want to deploy an N8N server locally, but I need to expose it externally for Fieldy to be able to talk to it. So I need a secure way to do that. I decided to start building a bunch of skills for Claude Code so it could be my network engineer to rework and resplit my internal network. Now I have a bunch of VLAN configurations, all the firewall rules configured — all done by Claude Code.

02:01:32 - Patrick Chouinard
There is a tool called ngrok [tool:ngrok]. If you have a local port 3000, ngrok will connect to that and make an external endpoint accessible online. Just want to throw that out there in case you run into hiccups.

02:02:05 - Dmitry Avramenko
I already have Twingate [tool:Twingate] and Tailscale [tool:Tailscale] configured as external tunnels. But I wanted to make sure whatever hits that server cannot do lateral movement in my home network. So I gave the skill to Claude Code to create a new VLAN, protect it, make sure it's isolated — only this VLAN can communicate with it.

▶ Claude Code can act as a network engineer: given the right skills (Python/Bash scripts), it can create VLANs, configure firewall rules, deploy them, test them, document them, and check everything back into a Git repo — creating infrastructure-as-code with full memory.

02:03:06 - Dmitry Avramenko
Funny enough, just yesterday I built something similar but integrated with ChatGPT [tool:ChatGPT]. I built a custom ChatGPT that has an action hitting my endpoint on Cloudflare [tool:Cloudflare]. That one calls my GitHub and creates an issue in GitHub immediately. Then my Claude Code picks it up and works on it.

I was riding on my OneWheel, brainstorming with ChatGPT in voice, exploring products I want to use. And I have a template for how my issues have to be created in GitHub — fully documented. So all my work going into what I'm building is done through ChatGPT voice, and I just say "save it to my database" and it does it.

02:06:01 - Brandon Hancock
Patrick — very recently, a big company reached out asking for literally everything you talk about, for software development lifecycle. Please, in public, on LinkedIn and YouTube, talk about everything you talk about on these calls. Bigger businesses are not doing AI software development properly. You have all the right ideas and the proof to show it because you're actually implementing it right now.

---

<!--SEGMENT
topic: Tiran's Preparedness Platform, Workflow Microservice, and Model Benchmarking
speakers: Tiran Dagan, Brandon Hancock, Dmitry Avramenko, Ryan - One Stop Creative Agency
keywords: preparedness site, emergency planning, Amazon affiliate links, Dakota scraping, PlantUML, Kroki, OpenRouter, Gemini 2.5 Flash Preview, trigger.dev, async workflows, JSON workflow system, Mermaid, Tiny Seed, $500 MRR, Russell Brunson, Dot Com Secrets
summary: Tiran Dagan demos a preparedness planning platform with a complex admin backend for managing emergency supply bundles, Amazon affiliate link generation (bypassing Site Stripe), and a Dakota-powered product scraper. He shares a custom async workflow microservice he built (as an alternative to trigger.dev) that uses JSON-defined workflows, markdown prompt templates with include commands, and OpenRouter for model-agnostic LLM calls. He generates a PlantUML diagram from the workflow JSON using the free Kroki API. Brandon recommends Gemini 2.5 Flash Preview on low thinking as the best current model for production instruction-following. Brandon also explains Tiny Seed's $500 MRR qualification threshold.
-->

02:21:57 - Tiran Dagan
Awesome. Do you read Russell Brunson's [tool:Russell Brunson] books?

02:22:03 - Tiran Dagan
Dude, I have them all right behind me. I'm using them like my Bible. The Traffic Secrets, Expert Secrets — the green and red ones are the two most important.

02:22:28 - Tiran Dagan
I'm going to share a project I talked about last time, and make my way towards something I'm giving out for free.

02:22:48 - Tiran Dagan
I'm building a preparedness site for people to use AI and customize what they should get — learning resources and training. Using ShipKit, I got to a nice design. As an admin, I can manage products with a very complex product tree: categories, subcategories, master items (which hide what I'm actually selling), and underneath are specific items I actually order and fulfill.

02:23:56 - Tiran Dagan
I can pull in a product from an Amazon link, paste it, and it does a Dakota [tool:Dakota] scrape. I've tried everything possible — theirs is really the easiest and cleanest solution. For the description, I make an AI call to take out marketing fluff and turn it into a real product description.

02:25:00 - Tiran Dagan
My inventory management is very complex because I have to know when to pick what product for how many people in a family, what kind of emergency scenario you're planning for. All of these tags: if you're planning for one month or three months, sheltering in place, for males and females, et cetera.

For Amazon affiliate links — they make you go through hoops to get access to the basic API. I hacked it. I figured out how to dynamically create affiliate links without using Site Stripe [tool:Amazon Site Stripe], which is a pain if you're trying to dynamically generate them.

02:26:17 - Tiran Dagan
On the front end, a user can create a plan: here's what I'm worried about, I want to plan for natural disaster, I'm going to pull in my family details, here's a weather API call, I want to plan for three months — generate the plan.

This is the part I always get stuck on. Brandon, I told you about sync/async calls, and you said I should look at trigger.dev [tool:trigger.dev]. And I had the natural reaction everyone here has — why don't I build my own trigger.dev?

02:26:56 - Brandon Hancock
So here, while this is running — my system has a whole monitoring of the queue of calls. I have my own trigger.dev server. You see the job is running, and when it's done, it calls a webhook back to my system.

02:27:00 - Tiran Dagan
The workflow service I built uses OpenRouter [tool:OpenRouter] to use any LLM and service. I developed a simple way to manage markdown prompt templates with include commands — you can create a markdown that calls another markdown, et cetera. It's a JSON-based workflow system where you define how the workflow works.

02:30:33 - Tiran Dagan
I discovered something really cool. You were showing Mermaid [tool:Mermaid] for diagrams. Have you heard of PlantUML [tool:PlantUML]? I have a script that takes the JSON and creates a diagram. There's a free API called Kroki [tool:Kroki] that can process PlantUML, Mermaid, and everything else — free, with throttling limitations. You just call it, pass it the script, and it returns a JPEG.

02:31:59 - Brandon Hancock
<Q>Just quick feedback on what I've been testing over the past week — for AI production applications, the best LLM right now for following instructions is Gemini 2.5 Flash Preview [tool:Gemini 2.5 Flash Preview] on low thinking. It's the same speed as GPT-4.1 [tool:GPT-4.1], smarter than it, and costs less. What used to take two LLM calls with GPT, I can now do in one.</Q>

02:29:51 - Tiran Dagan
<Q>Gemini 2.5 Flash Preview on low thinking — the name of the model again?</Q>

02:29:59 - Brandon Hancock
<A>Gemini 2.5 Flash Preview on low thinking. Medium thinking takes too long. Pro takes too long and costs too much money. So it's 2.5 Flash Preview on low thinking. We're passing in 20 to 25,000 characters of full-page medical protocols, plus a system prompt, plus a user prompt, all the RAG — and on low thinking it takes roughly 15 seconds and follows instructions perfectly.</A>

▶ Gemini 2.5 Flash Preview on low thinking is currently the best model for production instruction-following: faster than GPT-4.1, smarter, and cheaper — capable of consolidating multiple chained LLM calls into one.

02:36:05 - Tiran Dagan
I've posted this on my GitHub. Here's the link [link:GitHub/TiranDagan-workflow-microservice]. This is essentially three microservices — an API you call, a worker process, and a Flower dashboard for job management. It's totally async with conflict management between processes. Feel free to grab it and give me feedback.

02:41:38 - Brandon Hancock
The short answer on Tiny Seed [tool:Tiny Seed] — that's who we got funding from. The main criteria: you basically have to have $500 MRR coming in and proof of that for a few months. That is the qualifying factor. They prefer B2B. They open up in February.

---

<!--SEGMENT
topic: Dmitry's Agentic Orchestrator Live Demo — Raj the Incident Management Agent
speakers: Dmitry Avramenko, Brandon Hancock, Tiran Dagan
keywords: agentic orchestrator, incident management, GitHub Actions, Claude Code SDK, production logs, root cause analysis, voice agents, Slack integration, ChatGPT voice, token cost tracking, Sarah coding agent, George Scrum Master, Raj incident agent, multi-agent system, cloud deployment
summary: Dmitry gives a live demo of his agentic orchestrator platform, showing a token usage dashboard generated by his "George" Scrum Master agent, and then launching "Raj" — a production incident management agent — who investigates GitHub Actions logs, identifies a root cause (max_turns configuration too low in the Claude Code SDK), and reports back verbally. The demo illustrates a fully operational multi-agent system with named agents having distinct roles, personalities, and voices, integrated with Slack and ChatGPT for remote invocation. Dmitry tracks agentic vs. non-agentic sessions and custom skill usage to optimize costs.
-->

03:18:31 - Dmitry Avramenko
Okay, guys. Can you see my screen?

03:18:39 - Dmitry Avramenko
Yep. Looks great.

03:18:41 - Dmitry Avramenko
So what I'm going to show you first is basically a weekly report of my token spend. This has been generated by one of my agents. I can now ask it verbally and it actually does that. It looks at how many sessions are run, how many tokens I spent, my cost. This is all of my agents who do different things, and I track each of them separately.

03:19:09 - Dmitry Avramenko
You can see that Sarah [tool:Sarah agent] is my coding agent. She did 20% of the work during last week. If I were to pay API, I would have paid $200, but the subscription cost was basically a lot less.

03:19:21 - Brandon Hancock
Dude, you gotta fire Maya. She's slacking. She's doing nothing.

03:19:34 - Dmitry Avramenko
So if you listen to my video that I shared on YouTube, I'm talking to George [tool:George agent], who generated this report, and I'm having a conversation with him about this report. You'll be mind blown what he tells me.

03:19:41 - Dmitry Avramenko
This is my trend of using agentic versus non-agentic sessions. A wipe session to me is when I'm talking to Claude directly, like asking questions. I track how many agentic sessions versus wipe sessions I have.

03:21:20 - Dmitry Avramenko
This one is my custom skills. What I track is custom scripts versus generic. When you use generic tools with Claude, you actually spend more because Claude tries to search for things. If I have like a voice command that does five or six different shell commands at the same time — if I were to just ask Claude to do it, it would cost me probably about five times more. So building custom skills helps optimize cost.

03:22:09 - Dmitry Avramenko
This is a production incident management agent. I asked him to look for the last three weeks of my logs in the production system. There were some errors I deliberately created. He will search through the logs, search through change management requests, look through Git commits, identify what happened, and tell me. He will generate an incident report, identify root cause analysis, email it to me, and produce an issue with steps to fix — then commit it to Git. By the time this is done, I can launch Sarah and she'll fix it.

03:22:53 - Dmitry Avramenko
Re-introduce yourself.

03:22:55 - Dmitry Avramenko (as Raj)
Raj here. Let's see what broke in the last two and a half weeks, Dmitry. Something tells me there's a trail of failures waiting for us.

03:23:05 - Dmitry Avramenko
He's going into my GitHub Actions [tool:GitHub Actions] logs. There were errors I deliberately introduced about a week ago to train this guy. He's going to look at my logs for multiple days, find all the errors, report them, generate an incident report, identify root cause analysis, and email it to me. He will also produce an issue with steps to fix the issue and commit it to Git.

03:25:18 - Dmitry Avramenko (as Raj)
The picture is becoming clear, Dmitry. All five failures share the same root cause. Max turns limits were too low. The good news — a fix was deployed on December 29th. Let me verify the fix effectiveness.

03:26:00 - Dmitry Avramenko
This is a real production agent. He's actually looking at my production right now — all my commits, deployments, everything in Git. Every time I deploy, there is a deployment log generated so you can see who deployed when. This is part of my platform. It's only one of my agents. I have a Scrum Master, Implementer, Feature Planner, Architect, Researcher — they all do different things, speak in different voices, and have different personalities.

03:27:21 - Dmitry Avramenko (as Raj)
Dmitry, five failures, one root cause, already fixed. The new blog workflow should be stable now. Just waiting for the next real run to confirm. Raj.

03:27:39 - Brandon Hancock
<Q>My concern would be — I do a lot of parallel stuff. I would have four of them talking to me at once.</Q>

03:27:53 - Dmitry Avramenko
<A>Of course I have silent mode. When they run in the cloud, they don't talk. Right now, I asked him to talk. Default mode is silent. When they go to the cloud, there's an environmental variable set that detects it's running on the cloud. Right now I can run through Slack [tool:Slack] — I've integrated with Slack already — so I can launch all of this from Slack from anywhere in the world. I can just walk on the beach and all my agents can be launched from Slack, do the work. I also integrated with ChatGPT [tool:ChatGPT], so now I can do this through the ChatGPT voice interface as well.</A>

▶ The full agentic orchestrator stack: named agents with distinct roles and voices, running locally or in the cloud, invocable via Slack or ChatGPT voice, with token cost tracking, custom skill optimization, and Git-integrated incident management.

---

<!--SEGMENT
topic: Bastian's Elixir-Based Local-First Agentic CLI
speakers: Bastian Venegas Arevalo, Brandon Hancock, Patrick Chouinard, Dmitry Avramenko, Tiran Dagan
keywords: Elixir, CLI agent, GLM 4.7, OpenRouter, Manus, local-first, SQLite, EXA web search, Daytona sandboxing, KimiK2, Moonshot Minimax, sub-agents, plan mode, build mode, Cursor MCP, agentic orchestration, open source
summary: Bastian Venegas Arevalo demos a local-first CLI agentic tool built in Elixir, designed for resilience and persistent SQLite storage. The agent uses GLM 4.7 (a Chinese open-source model available via OpenRouter at a fraction of the cost of GPT-4) and EXA for web search. He demonstrates it researching Brandon's startup, generating markdown documents, and building a responsive website — all autonomously. He discusses plans to sandbox sub-agents using Daytona for safe remote code execution, and compares KimiK2 and Moonshot Minimax as additional cheap model options. The segment also covers GLM's 670B parameter scale and why it cannot run on consumer hardware.
-->

03:08:04 - Bastian Venegas Arevalo
Thank you. So this is a CLI tool — it's like my version of sort of Manus [tool:Manus] meets Claude Code, a general-purpose agent. It's built in Elixir [tool:Elixir] because I want it to be very resilient and able to see into the whole workflow, with agents responding if they make a mistake without worrying about it too much. It also has persistent storage in SQLite [tool:SQLite] locally, so it's meant to be local-first.

03:08:54 - Bastian Venegas Arevalo
Here's an example. The green is the agent. When it says "build," it's the build agent. I was saying: say hello to Brandon and the guys at the coaching call, and asking who you are. So it searched for your startup, searched online for you, did a bunch of stuff, then I had it write this in markdown. It built three different markdowns, and then I asked it to make a website with the markdown documents, and it built this — which is kind of decent. It's your AI learning methodology, and it is mobile responsive. It also built a competitor analysis with seven companies.

03:10:01 - Bastian Venegas Arevalo
This web search is powered by EXA [tool:EXA], which is a great service if you guys want to add search to your apps.

03:10:19 - Bastian Venegas Arevalo
Then this is GPT-5 [tool:GPT-5] trying to do the same. It works, but it didn't get the markdown documents imported.

03:10:52 - Bastian Venegas Arevalo
This is the list of tools it has — very few tools, because I want to do it like Claude Code, which basically uses bash for everything. It's proven that it works.

03:11:09 - Bastian Venegas Arevalo
The first model — the website that was actually better — was built with GLM 4.7 [tool:GLM 4.7], the one that's crazy cheap from the Chinese company. So it's actually kind of cool.

03:11:29 - Brandon Hancock
<Q>Under the hood — is it multiple agents with multiple tools? How are you orchestrating them and sharing tasks?</Q>

03:11:41 - Bastian Venegas Arevalo
<A>It has a to-do schema that is used to delegate tasks to whatever agent you choose — it could be a different model, a different company. They all follow the same schema, so it's kind of fractal. It has a plan mode and a build mode, they all can have different tools enabled, and it's very resilient. It can do sub-agents.</A>

03:12:34 - Brandon Hancock
<Q>How are you actively using this right now?</Q>

03:12:38 - Bastian Venegas Arevalo
<A>I'm using it to produce artifacts — web artifacts for medical education, medical-clinical cases and challenges — and also for coding. I use it as a way to ask about my codebase, then hop on to Claude Code without spending my usage so quickly. I can actually delegate from this model to, for example, the Cursor [tool:Cursor] agent, which exposes an MCP and a CLI. So you can have this be the root agent — GLM 4.7 — and then have the Cursor composer model cranking through all the work, which is very fast.</A>

03:13:56 - Brandon Hancock
<Q>How much is GLM costing out of curiosity?</Q>

03:13:58 - Bastian Venegas Arevalo
<A>It's crazy cheap — like in the cost range of GPT-4o Mini or a flash model, even less. I've been coding and doing all of these experiments for the last three days and just with $6 that I got via OpenRouter [tool:OpenRouter] — that's all.</A>

▶ GLM 4.7 via OpenRouter costs roughly the same as GPT-4o Mini or less, is open-source with public weights (670B parameters, requires a cluster to run), and outperformed GPT-5 on the website generation task in this demo.

03:14:36 - Bastian Venegas Arevalo
It is open source and the weights are public. I don't think they have it available on Ollama yet — it's a very dense model, 670 billion parameters, so it won't fit any personal hardware. You need a cluster to run it. It's running in their own inference via OpenRouter API.

03:15:14 - Bastian Venegas Arevalo
You can also run Ollama [tool:Ollama] models through it. And you can use Groq [tool:Groq] or Cerebras [tool:Cerebras] as well — basically instant, but the models have less output in size, usually 8K tokens. So you're limited because we've grown accustomed to 64K token outputs.

03:16:17 - Bastian Venegas Arevalo
I'm thinking about having it really be my dog — I wanted to actually use this myself to code and do all my stuff. I may open source the core. I want the sub-agents to be able to respond on demand and not necessarily be everything on my machine. I've been thinking of sandboxing the sub-agents using Daytona [tool:Daytona] — basically like any container when you spawn machines, but they have their own machines, don't rely on Amazon or Google, and have persistent storage. You spawn the container, it does its thing, you go back an hour later and it still has what it produced. You can stream it right back to the agent instantly. They have a really nice SDK.

03:17:03 - Patrick Chouinard
<Q>Did you try KimiK2 [tool:KimiK2]? I've heard some very good stuff — it's about 32 cents per million input and 48 cents per million output.</Q>

03:17:07 - Bastian Venegas Arevalo
<A>Yes, I have used KimiK2, but not in this project. I've used it a lot for chat and web search. It's really good at writing — it has a GPT-4.5 feel to it without breaking the bank. The non-thinking model by KimiK2 is really good at writing. Not for coding, but I've heard it's really good. And the other one is the Minimax model [tool:Minimax] by Moonshot — there's a lot of open-source cheap models you can leverage.</A>

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names were not found in the SPEAKER_ALIASES context block and have been passed through unchanged:

- **HP** — appears to be "Scott" based on in-call references ("Scott, great find"), but the alias map was not provided to confirm. Passed through as "HP."
- **David** — appears briefly around 01:09:15 discussing a virtual machine code swarm. No alias map entry confirmed.
- **Mitch** — appears briefly around 01:46:27 discussing YouTube transcript downloading. No alias map entry confirmed.
- **Juan Torres** — appears around 02:54:05 and 03:02:14. No alias map entry confirmed.
- **Hemal Shah** — appears around 02:54:08. No alias map entry confirmed.
- **Garron Selliken** — appears around 02:43:00. No alias map entry confirmed.
- **Prem** — referenced as a collaborator by Garron Selliken but does not appear as a speaker. Not in alias map.