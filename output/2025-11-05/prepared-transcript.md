=== SESSION ===
date: Unknown (Tuesday)
duration_estimate: ~110 minutes
main_themes: ShipKit development roadmap, AI coding tools and workflows, Google ADK/Agent Engine issues, personal knowledge management, AI video generation, developer business strategy, Clerk/Stripe payment integration, end-to-end testing, freelance developer visibility

---

<!--SEGMENT
topic: Pre-Call Introductions and Vibe Coding Governance
speakers: Patrick Chouinard, Marc Juretus, Ana P, Paul Miller, Ty Wells
keywords: GitHub Copilot, vibe coding, code hygiene, GitHub Copilot CLI, Claude Code, Gemini CLI, Cursor, GitHub Agent HQ, branching, pull requests, hospital merger, reorg
summary: Participants join and exchange informal greetings before the host arrives. Patrick raises a critical enterprise concern: widespread vibe coding is producing unmanaged applications that lack proper Git hygiene — no PRs, no branching strategy, no commit discipline. He sees GitHub's emerging platform as a potential solution for orchestrating multiple AI coding agents under a single pane of glass.
-->

00:07:00 - Patrick Chouinard: Thank you.

00:07:41 - Patrick Chouinard: Hi, Marc.

00:07:43 - Patrick Chouinard: What's up, brother?

00:07:44 - Marc Juretus: How you doing?

00:07:46 - Marc Juretus: Good, good.

00:07:46 - Patrick Chouinard: Yourself?

00:07:47 - Patrick Chouinard: I can't complain.

00:07:49 - Marc Juretus: Another day in the books, you know what I mean?

00:07:52 - Patrick Chouinard: How's your training going?

00:07:54 - Patrick Chouinard: Well, training's going well, but the company is in a big reorg.

00:08:02 - Marc Juretus: Yeah, we had a merger with another hospital. We've been kind of going through that for the last year.

00:08:09 - Patrick Chouinard: Yeah, we had the merger last year. So this year it's reorganization after the merger. Fun times. Everybody's asking me, how are you taking it? Are you okay?

00:08:22 - Marc Juretus: It's like, I've done that for like 30 years.

00:08:25 - Patrick Chouinard: It's my 100th reorg.

00:08:39 - Patrick Chouinard: Hi, nice to meet you.

00:08:43 - Ana P: Hello, nice to meet you too.

00:08:50 - Patrick Chouinard: Is it your first time on the call?

00:08:52 - Patrick Chouinard: It is.

00:08:53 - Ana P: I want to learn more about Generative AI. I've been playing around with ADK [tool:Google Agent Development Kit]. I was able to deploy an agent to Agent Engine [tool:Google Agent Engine].

00:09:06 - Patrick Chouinard: Good. Definitely in the right place. We're all just participants on the call. The host hasn't joined yet.

00:10:00 - Patrick Chouinard: This week, tons of things, but more about what I have to do with the business on a corporate level. Not so much having fun working with ShipKit [tool:ShipKit]. Except for the little idea I've posted in the show-and-tell, and also in the feature request. I think I got the interest of Tom pretty well on that.

00:10:15 - Paul Miller: <Q>Oh, what was that? I haven't seen that one, Patrick. Where was it posted?</Q>

00:10:29 - Patrick Chouinard: Yeah, because I don't go to Discord enough.

00:10:34 - Paul Miller: I should live in there because I'm really getting into using Claude Code [tool:Claude Code] now with ShipKit. It's my new go-to.

00:10:47 - Ty Wells: Hey, Ty.

00:11:05 - Paul Miller: <Q>Has the expectations gone through the roof with what everyone now wants to do? Now everyone is vibe coding — is that kind of a question?</Q>

00:11:31 - Patrick Chouinard: <A>Yes and no. And that's actually touching on the suggestion I made. Everybody wants to vibe code. So we have tons of people that are now creating applications, but nobody actually managing them. We're missing the PR hygiene, the commit hygiene, the branching, the merging. All of those things are not in vibe coding if you don't put them in the framework.</A>

▶ If GitHub Copilot [tool:GitHub Copilot] goes the way I think they're going right now, GitHub might take a whole lot more of the market — because basically they're offering a platform where you could manage Claude Code [tool:Claude Code], Gemini CLI [tool:Gemini CLI], Copilot CLI, Cursor [tool:Cursor] — whatever agent you have — managed from a GitHub pane of glass. That might get them pretty far, actually.

▶ And again, if we have that, then we can orchestrate to make sure that vibe coders actually do good code hygiene and don't just produce functional things that are unmaintained.

00:13:08 - Patrick Chouinard: But yeah, with the reorg we just went through, let's just say it moved a lot of the targets we had. But even in that context, I'm still training another 50 people on GitHub Copilot next week.

00:13:27 - Paul Miller: <Q>How big is your company?</Q>

00:13:30 - Patrick Chouinard: <A>It's 6,000 people all in all — but my client, not my company, but the client I'm at right now is 6,000 people. They have about 400 people in IT.</A>

00:13:44 - Paul Miller: My company is about the same size, 6,500 people, but actually about 1,000 developers. We're an IT consulting firm. And I'm doing training on both sides.

00:14:00 - Patrick Chouinard: Yeah, I'm not short of listening people for the training I give.

---

<!--SEGMENT
topic: Early IT Career Nostalgia
speakers: Marc Juretus, Patrick Chouinard, Paul Miller, Ty Wells, Brandon Hancock
keywords: Netscape, Internet Explorer, Drumbeat 2000, ASP, ColdFusion, SQL Server, RealPlayer, Sun Microsystems, Spark workstations, CBT training, 3D Studio Max
summary: Before the formal session begins, participants share memories of early web development in the late 1980s and 1990s, including browser compatibility challenges between Netscape and IE, early multimedia tools like RealPlayer and Drumbeat 2000, and 3D computer-based training. This segment is primarily social context with no technical recommendations.
-->

00:15:01 - Patrick Chouinard: I started in 98.

00:15:03 - Marc Juretus: I started in 89.

00:15:06 - Paul Miller: I was going to say, I started in 89 too.

00:15:09 - Ty Wells: See, now I don't feel as much of an artifact at this stage. Thanks, Paul.

00:15:16 - Ty Wells: Not 89, sorry — 91.

00:15:19 - Paul Miller: Tom can outdo me, but he's not on the calls.

00:15:24 - Patrick Chouinard: You have to be present to win.

00:15:30 - Paul Miller: We can ask him about punch cards.

00:15:35 - Marc Juretus: We started with ASP, ColdFusion [tool:ColdFusion], and SQL Server [tool:SQL Server] database sites, JavaScript, and this front-end thing called Drumbeat 2000 [tool:Drumbeat 2000], which was basically kind of like FrontPage where you could drag and drop, but its big selling point was — you remember how you had different code for Netscape [tool:Netscape] and IE [tool:Internet Explorer] differently? It did all of that for you, which was awesome.

00:16:03 - Marc Juretus: That's because I was working for Lucid Technologies, and they had Sun Microsystems [tool:Sun Microsystems], so they were running Netscape. And every site you made better work, or we can't use it.

00:16:21 - Paul Miller: Did you have Spark workstations and stuff like that?

00:16:34 - Marc Juretus: To make it real brief, they were making CBTs in the lab. Like, you know that electrostatic discharge is dangerous where you can ruin chips? So they made, like, a 3D with 3D Studio Max [tool:3D Studio Max], a 3D reality where you could take training. At the end, you were done, you got credit for it.

00:17:29 - Marc Juretus: You know what the coolest thing was back then? We got this — remember RealPlayer [tool:RealPlayer]? So we had this thing where you could sync up a PowerPoint slide with the video. When you pulled it up, the video was synced with the PowerPoint. And to them, that was like the biggest thing since sliced bread because they could actually watch these speakers without having to be there.

---

<!--SEGMENT
topic: Session Kickoff and Round-Robin Format
speakers: Brandon Hancock, Marc Juretus
keywords: GitHub Copilot, Spring Boot, React, Markdown, AI-assisted learning, Udemy, round-robin, ShipKit, Discord
summary: Brandon Hancock officially opens the session, explains the round-robin format, and Marc Juretus shares his current work using GitHub Copilot to scaffold a Spring Boot and React application via a Markdown script. Marc highlights AI's unique advantage as a learning-while-doing tool compared to traditional platforms like Udemy.
-->

00:17:55 - Brandon Hancock: All right. We'll dive on in, guys. Hope you all are having an awesome Tuesday so far. What I'm going to do is take a super quick screenshot of call order. Just in case — new on the call — the way we go about this is we just kind of go round-robin based on that screenshot. So if you have any questions, any wins, or anything else you want to share, that's kind of the way we do it. It looks like Marc, you were up first anyway, if you want to kick us off with what you're working on. And then Ana after that, then Ty.

00:18:36 - Marc Juretus: Right now, I'm not really working on too much. I'm basically just doing some stuff with GitHub Copilot [tool:GitHub Copilot] at work. Just basically writing out a Markdown file, a script, and having a person that is like a non-specific user that can actually run and build that application in Spring Boot [tool:Spring Boot] with a React [tool:React] front end. I'm trying to get some more time into this to work on my own, but that's where I'm at right now. Not a whole lot of questions this week, Brandon.

00:19:18 - Marc Juretus: Like, I was trying to tell my boss today — one of the most amazing things about AI, in my opinion — as opposed to using a Udemy [tool:Udemy] or a lot of YouTube videos, if you have a specific project you want to do and you really don't know much about it, you can actually learn on the way.

▶ AI enables project-based learning in real time, which is a fundamental shift from traditional tutorial platforms like Udemy.

00:19:41 - Brandon Hancock: Yeah. No, I mean, if you're determined enough, you can get the answer to most stuff. So yeah, totally agree.

---

<!--SEGMENT
topic: Brandon's Announcements and Trigger.dev for Prompt Chaining
speakers: Brandon Hancock, Mitch
keywords: Claude Code, Cursor, Gmail MCP, email automation, Trigger.dev, N8N, Make, prompt chaining, ShipKit, Mermaid, Excalidraw, Eraser, worker SaaS, base template
summary: Brandon announces two upcoming projects: a Gmail MCP-based email auto-responder using Claude Code or Cursor, and a ShipKit base template with background task workflows. He also answers Mitch's question about agent kit replacements, recommending Trigger.dev for prompt chaining and sequential task execution, while noting it lacks a graphical UI like N8N or Make.
-->

00:19:48 - Brandon Hancock: Oh, and real fast, before going on, two things. I forgot to make some announcements.

▶ A few videos I want to work on this week. One is I'm going to share with you guys how I'm working on making an email auto-responder — not full-blown — but how I'm using Claude Code [tool:Claude Code] and Cursor [tool:Cursor] to actually respond to emails. I'm going to showcase how to use Gmail with MCP [tool:Gmail MCP] and then you can use Claude Code or Cursor to actually understand and respond to stuff — to where you're literally just hitting send, or "no, change that." So I'll be sharing, hopefully recording this tomorrow, and I'll be sharing with you guys the actual skills and the ghostwriters and everything so you can just copy my homework and run it yourself.

00:20:54 - Brandon Hancock: And then outside of that, Mitch, real fast, answering your question: <Q>Are there any good replacements for agent kit or prompt chaining?</Q>

<A>The main thing that I'm about to be recommending for ShipKit [tool:ShipKit], and I think you've heard me say it before — I'm absolutely loving Trigger.dev [tool:Trigger.dev] for this. They actually have the exact thing that you're talking about. You basically just do a series of tasks. Task one runs prompt one. Task two runs prompt two.</A>

00:21:43 - Mitch: <Q>Do they have a UI? Because I'm really just trying to share this with someone who has no coding experience at all. Do they have a UI that shows like the N8N [tool:N8N] nodes, similar to how N8N has those? Or would I just code it up?</Q>

00:21:59 - Brandon Hancock: <A>Yeah, unfortunately, a lot of the way it works is — it basically just gives you a run log. It's very like, "here's the tasks that are running and you can view their activity." It's not a graphical interface like you would see with N8N or Make [tool:Make]. It's very much just "look at the logs" and you can chain them together however you want.</A>

▶ But you could always make the wireframe and then say, "hey, Mermaid [tool:Mermaid], make me the drawing for the person to see." So you can always do that and then export it to Eraser [tool:Eraser] or Excalidraw [tool:Excalidraw]. As long as you have the Mermaid drawing, you can do anything.

00:23:00 - Brandon Hancock: And then final note — the ideal goal for the base template: if I could wave my magic wand, I would love to have it done and ready by the same time we ship the worker SaaS. So ideally the 16th is the day we're shooting for right now. Basically, it's just a blank spin-up project. And then I'll be recording some courses showcasing how to take a base template, my process for fine-tuning, workflow generation — everything — so that you guys can start to copy it however you would like.

---

<!--SEGMENT
topic: Google ADK and Agent Engine Deployment Issues
speakers: Brandon Hancock, Ana P
keywords: Google ADK, Agent Engine, Cloud Run, Flask, Vertex AI, streaming query, server-sent events, ADK run command, Google Cloud, beginner agent deployment
summary: Ana P, a first-time caller, describes her portfolio project: a basic AI agent deployed to Agent Engine with a Flask front end on Cloud Run. Brandon validates her approach and warns that Agent Engine has significant known bugs when combined with ADK — particularly broken streaming/server-sent events — and strongly recommends Cloud Run as the deployment target instead.
-->

00:23:39 - Brandon Hancock: All right. Next up, Ana. What's going on? Welcome. How can we help?

00:23:44 - Ana P: Nice to meet you. Thank you. You already helped a lot. I used your content to get started with AI. I was able to create a very basic agent. I'm looking to expand the tools. It's really a portfolio project. And within that, at the moment, I was able to deploy using Agent Engine [tool:Google Agent Engine]. And last week I started developing a Flask [tool:Flask] app to have an interface that I can hand over to a client who might want to query their data and have the app deployed in Cloud Run [tool:Google Cloud Run].

00:24:41 - Ana P: My recent struggles — I'm a beginner. I didn't want to say that, but I'm definitely a beginner compared with the level of expertise I see in the conversations within this chat.

00:25:00 - Ana P: I was able to see that Vertex AI [tool:Vertex AI] offers some sort of API for making requests to a deployed agent in Agent Engine, but it's not a best practice to send the request directly — rather, have an app that can handle everything for you. I want to kind of just confirm that. I'm honestly still working on this project. This week I'm starting a machine learning basic project, but I know that ML is not as flashy as AI, but all of them use Vertex AI. So I'm kind of playing around with that platform a lot, and I'm here to listen.

00:25:49 - Brandon Hancock: Super happy to have you. And honestly, you're already crushing it. So I wouldn't underwrite your skills.

▶ Hot take on Agent Engine [tool:Google Agent Engine]: this is a consistent topic we bring up because Google is very behind on updating Agent Engine. The current ways you can interface with it — when it comes to stream a query or just making a query — the stream query function actually doesn't work if you're doing server-side events. So there's a lot of actual functionality with Agent Engine that's broken with ADK [tool:Google ADK] and deployed instances right now.

▶ Even on their own website, as of about a month ago, they're all recommending Cloud Run [tool:Google Cloud Run] going forward — where basically you're spinning up your own instance of your agents, exposing the API. I think it's just `adk run` — there's an actual command that exposes the full-blown API to where you can track events, see what's going on, send over requests.

▶ Going back to what you're saying: I think you would save a lot of headache not using Agent Engine at this exact moment — through personal battle scars — would be my main recommendation.

00:27:38 - Brandon Hancock: Main takeaway is: if you look at the way they recommend deploying Cloud ADK, there's Agent Engine and then Cloud Run. Please, to save yourself a lot of headache, go with Cloud Run — because you'll get so many unknown errors with Agent Engine.

---

<!--SEGMENT
topic: Personal Knowledge Management with Limitless and Memento
speakers: Ty Wells, Brandon Hancock, Paul Miller
keywords: Limitless device, Memento repo, Apify, Telegram, MCP, GitHub repo, knowledge base, pattern recognition, context management, meta glasses, Claude Code, vector store
summary: Ty Wells demonstrates a personal knowledge management system built around the Limitless AI recording device and a GitHub repo called Memento. He is cross-referencing daily insights, repos, and video content using Apify for scraping, with a Telegram interface for agent commands. Brandon connects this to his own practice of storing all project context in GitHub repos for Claude Code access, and speculates about future AR glasses as an ambient AI interface.
-->

00:28:04 - Ty Wells: You know, every week I'm working on something different. I'm trying to capture all what I'm reading, what I'm consolidating on a daily basis and sort of try to figure out what synergies are happening. So this device — this is a Limitless device [tool:Limitless]. That's recording. It definitely helps you keep organized and stuff, but it doesn't do enough. So I'm trying to link in some other things.

00:28:55 - Ty Wells: So I found this repo called Memento [tool:Memento], that's basically based off the Limitless API. Limitless is this AI recording device — it has an app, you can see daily insights and stuff like that. This platform, Memento, is based off of it. It has an API, supposedly an MCP, but it didn't work for me. So what I'm trying to do is cross-reference the knowledge that I'm coming across every day. So I've got my daily insights — any decisions that I would have made, any ideas that I may have said out loud.

00:30:19 - Ty Wells: So since then, I've added in some additional things for knowledge searching and being able to do pattern recognition across my repos. These are all my repos and different learning experiences, bug fixes, documentation. I'm trying to extract all of that and then be able to cross-reference different projects, different knowledge, different articles that I go through every day.

00:31:29 - Ty Wells: I just grabbed one of Cole's videos, grabbed it off of there, and I'm using Apify [tool:Apify] to go get it, scrape it, summarize it, get the content, and then see if there are any insights relative to my entire knowledge base of information.

00:33:58 - Ty Wells: Yeah, no, thanks. I've got it connected to Telegram [tool:Telegram] too. So the intent is I say "do something," it kicks off whatever it needs to be done and then responds to me back in Telegram. And then I can approve or deny or whatever.

00:34:35 - Brandon Hancock: One quick thing I want to add on to this, because I think all of you guys will nerd out on this idea. The new Meta glasses [tool:Meta glasses], the display glasses — starting I think in like six months, they're going to have an app functionality, like an app store. And what I would love to do is exactly what you're talking about, Ty. Like I have my GitHub repo that has everything about every project I'm working on, and I can just talk to it. Like I'm basically spinning up Claude Code [tool:Claude Code] chats in my glasses is what I'm envisioning. And I'm just like, "hey, go write that email, look at this and this." And then whenever I get home at the end of the day, there's an inbox of all the things that I wanted to do.

00:35:33 - Brandon Hancock: <Q>Are you using any MCPs to quickly grab stuff? I saw you used Apify at one spot.</Q>

00:35:47 - Ty Wells: <A>I was going to look into that. I've just been doing this the last couple of days. I've got to see what all I'm going to add. I'm trying to get all the sources in first. But yeah, if there's an MCP that adds value based on what I'm trying to do, I will definitely add it.</A>

00:36:10 - Brandon Hancock: So I love this because I'm actively tackling this same thing. The root issue is context. Because if you watched a video and you were like, "cool, I want to talk about what they talked about in a blog post or apply it at work" — everything has to connect and agents have to be in the middle of it. So I absolutely love what you're doing.

▶ Right now I'm literally, for every project in my life, every time I have a meeting, a transcript, anything — I'm literally throwing it into a GitHub repo [tool:GitHub], so then I can always just say, "hey, Claude Code, I was reviewing these legal docs, and now I need to write a response to this person." It grabs the docs, it grabs my ghostwriter, and it just starts spitting out stuff.

---

<!--SEGMENT
topic: ShipKit Roadmap and Discord MCP Feature Request
speakers: Patrick Chouinard, Brandon Hancock
keywords: ShipKit, Discord MCP, vector store, GitHub, branching, pull requests, commit hygiene, Trigger.dev, worker SaaS, base template, Gemini CLI, GitHub Agent HQ, Mission Control, spec-driven development, custom GPT
summary: Patrick presents two feature requests for ShipKit: (1) an admin layer managing Git hygiene — branching, merging, PRs, commit messages — to make ShipKit enterprise-ready; and (2) a Discord MCP integration that would feed ShipKit's Q&A knowledge base into a vector store accessible from coding agents like Claude Code or Cursor. Brandon outlines the ShipKit roadmap through the end of the year, including worker SaaS, base template, and an AI video walkthrough.
-->

00:45:54 - Patrick Chouinard: A couple of things. First, I've posted a couple of things in the feature requests in the Discord server. So basically, the first one is the one I've already talked to you about — the admin part of ShipKit [tool:ShipKit], basically making it manage all the branching, all the merging, all the commit messages, the PRs, all of that. Because, as I mentioned, in order to make it corporate-incentive to bring it in, we need that part.

00:46:37 - Brandon Hancock: Yeah, go ahead. I will just say high level, just real fast for everybody — roadmap, exactly what I'm going to be doing. On paper, this is what's supposed to happen. The whole goal is the next two weeks to sprint like a madman to finish worker SaaS [tool:ShipKit worker SaaS] and base SaaS. After that, I'm going to be doing YouTube walkthroughs, where I'm basically just giving you guys the templates as soon as they're ready.

▶ In the base template, you're going to see how we use Trigger.dev [tool:Trigger.dev] to actually pick off all sorts of background tasks — to transcribe, chunk stuff, do stuff. Also real-time subscription data — that's another feature we're going to be showcasing. So there's going to be multiple ways we're just trying to show how to use background tasks, and that's all in the worker SaaS.

▶ Then the walkthrough, which will happen in the following week — I'll be showing you guys how to transform the worker application to an AI video platform. Shorts generator — shout out to Mitch for that one. Basically, at the end of the day, AI video: take in a few ideas, come up with a five-second variation of what the clip should be, and then basically we're just trying to generate five-second shorts.

00:48:36 - Patrick Chouinard: And the other one that might be a 2026 thing — and that's perfectly okay. The idea I came up with: there's a whole lot of intelligence building into Discord right now. The ShipKit Discord has a whole lot of questions and answers. It's a knowledge base. <Q>What if we use the Discord MCP [tool:Discord MCP] to ask questions to Discord while we're in Cursor or Claude Code working with the templates?</Q>

00:49:13 - Brandon Hancock: <A>I love what you're thinking. I think the way I would take that — because you're spot on, Patrick — is actually throw everything into the same vector store [tool:vector store] that exists for ShipKit. So the courses feed the vector store, Discord feeds the same vector store, and then step one would just be allow you to naturally ask questions. And then step two is providing you guys an MCP so that in your codebase at any point, with your personal access token, you could start requesting stuff to the vector store.</A>

▶ Why answer the same question 30 times when we can just ask directly from our coding agents?

00:50:00 - Brandon Hancock: That's a must. It's AI — how is there not an MCP, you know?

00:50:22 - Patrick Chouinard: One last thing. In the show-and-tell, I published the link to the custom GPT [tool:custom GPT]. I was asked to share the files that are part of it. Are you okay with me sharing that in the Discord server?

00:50:40 - Brandon Hancock: Yeah. In Discord, that's fine. Yeah, totally cool. Literally got a request for your stuff this morning on the 10 a.m. call. So you're in demand, Patrick.

00:52:00 - Patrick Chouinard: To close on my side — what I'm doing: I haven't been able to build a whole lot because I've been working on reviving my blog this week. I'm working on an article on what we discussed last week about using Gemini CLI [tool:Gemini CLI] as a search agent, and working on another piece about the junction of what GitHub released last week called Agent HQ [tool:GitHub Agent HQ] with Mission Control — and tying it in to something like either a spec kit for a general project or even ShipKit. Having Agent HQ running the orchestration that manages all the different agents actually implementing spec-driven development.

00:53:05 - Brandon Hancock: That's very cool. Real fast — the Gemini CLI — if you end up making a workflow for that, I would absolutely love to see what your magic sauce is. Long story short, we need to do parallel searches all across a state, and per state, we need to look up these 10 different places in each city. And I was like, "oh my gosh, this is literally what Patrick has been describing in using parallel" — yeah, just so I was like, if you have any information around that, I would love to pick your brain.

00:53:57 - Patrick Chouinard: <A>Honestly, that is just a bash script going through a list of query variables that you can send to a headless version of Gemini CLI [tool:Gemini CLI]. You can even have an Excel sheet that has all of the variables and go through it. That's it.</A>

▶ Using Gemini CLI in headless mode with a variable list (e.g., from an Excel sheet) is a simple and effective pattern for parallel web searches at scale.

---

<!--SEGMENT
topic: Clerk Payment Integration and ShipKit Template Cleanup
speakers: Morgan Cook, Brandon Hancock
keywords: Clerk, Stripe, Supabase, ShipKit, payment integration, subscription billing, cleanup script, shiny object syndrome, Software as a Science, template feature removal
summary: Morgan Cook discusses two topics: (1) difficulty removing unused template features from ShipKit, which Brandon resolves by pointing to the cleanup markdown script; and (2) Clerk's new payment integration backed by Stripe, which simplifies subscription billing by co-locating user auth and payment data. Brandon is intrigued but cautious, noting ShipKit currently offloads all Stripe management to Stripe's own portal and wants to see a full implementation before switching.
-->

00:37:11 - Brandon Hancock: All right. I think next up, let's keep going back to the list. I think Morgan, you're up next, man. What's going on?

00:37:31 - Morgan Cook: As far as progress, I'm just chunking along, working through the current project I'm on. I've got three projects and two of them are kind of sitting on the side waiting for me to finish the first implementation of this one. One of the problems I ran into was pulling features out from the template is kind of difficult — a feature that I don't actually need in my application. Trying to remove that out of the template takes a little bit of effort.

00:38:11 - Brandon Hancock: <A>So real fast, there's a thing called cleanup, and it'll look for unused code and just drop it. There's a Markdown file.</A>

00:38:25 - Morgan Cook: <Q>But how do you make it unused when it was part of the original template? At what point does it become viewed as unused code?</Q>

00:38:38 - Brandon Hancock: <A>Most of the time, in the very last video of each of the walkthroughs, I run the cleanup script, and I'm usually just saying like, "hey, I don't use the chat anymore. We're now using the model comparison page. Can you just go drop all the chat stuff?" And then I tag the cleanup Markdown file, and then it's like, "oh, I will happily fix it for you." And it makes a monster task to fix everything for you.</A>

▶ Use the ShipKit cleanup script by describing what you no longer need in natural language — the AI will generate a comprehensive removal task.

00:39:12 - Morgan Cook: I've been reading the *Software as a Science* book [link:Software as a Science book]. Dude, how far are you?

00:39:22 - Brandon Hancock: Chapter five or something like that. Yeah, it's a great read.

00:39:26 - Morgan Cook: ▶ If you guys haven't read or listened to it, that's got to be on your plate for sure.

00:39:43 - Morgan Cook: <Q>What are your thoughts about the Clerk [tool:Clerk] payment integration? Clerk just added payment, and the payment is backed by Stripe [tool:Stripe]. So it helps because your payment stuff is all associated with the user. They have some really nice components that are just quickly dropped in to build all that support for subscription information. It does not at this point support anything for one-offs or per-item charges — it's subscription-based only at this point. But it's a really, really good first start that simplifies the entire process and still uses Stripe as a back end.</Q>

00:40:47 - Brandon Hancock: <A>Oh, no, via Stripe. Yeah, the transactions are via Stripe, so the percentage is through Stripe. But all the components and your monthly authentication codes, I think, are just through Clerk. I would just, without seeing a full-blown example, be curious what it actually looks like to bring it to life. Because like for right now, with Stripe checkout [tool:Stripe Checkout], the way we're doing it in ShipKit is just — all we're doing is storing this person's Stripe customer ID. And if they want to do anything on Stripe, we kick them out of the app immediately and throw them over to Stripe to manage everything. So I would be a little bit curious to see it in action — what is actually getting simplified in there?</A>

00:44:11 - Brandon Hancock: ▶ Shiny object syndrome is a legit real thing. Fundamentally, if the problem's solved and it works for me, unless it's a 10x improvement that completely makes it easier, I'm just going to stick with the thing I know — because I don't know what I don't know about this, and I could end up spending extra days getting something set up when the hard part was actually getting customers and building the features they care about.

---

<!--SEGMENT
topic: UI Component Libraries and Business Partnership Strategy
speakers: Paul Miller, Brandon Hancock
keywords: Claude Code, Cursor, ShipKit, 21stDev, Mobbin, UI components, sales training partnerships, industry verticals, freelance strategy, Stripe, Supabase
summary: Paul Miller shares two wins: (1) discovering 21stDev, a free UI component library that provides copy-paste prompts for AI editors — similar to Mobbin but with source code and AI editor integration; and (2) a business strategy insight about partnering with sales trainers who have deep industry vertical access and a pipeline of AI project opportunities. Brandon enthusiastically endorses both, connecting the partnership idea to the power of complementary skill sets.
-->

00:56:09 - Paul Miller: Hey, guys. So I'm having fun with Claude Code [tool:Claude Code]. I made the jump. I've moved from Cursor [tool:Cursor] to Claude Code. I'm not seeing the money go crazy. I've finally started using ShipKit [tool:ShipKit] with it. So I'm really comfortable.

00:58:00 - Paul Miller: Take those screens, but apply this design methodology to those screens, and then iterate through it, but never touch any of the graphical elements. And God, that is so good as guardrails for my UI/UX design.

00:58:20 - Brandon Hancock: Sometimes you just see something and you're like, "that's beautiful, that's what I want to do." One thing I'm looking at doing is to update either the improve UI section or to update the generate landing page. It's called 21stDev [tool:21stDev], but basically what they do is they have all sorts of — like, let's look up hero sections. You can actually look up hero components. And what's super nice is they give you a little button that says, "hey, copy and paste this into your AI editor," and it'll help match things for you or help make this.

▶ 21stDev [tool:21stDev] is free and provides UI components with copy-paste prompts for AI editors like Claude Code or Cursor — a significant step beyond screenshot-only tools like Mobbin [tool:Mobbin].

00:59:28 - Paul Miller: <Q>Does that do what Mobbin [tool:Mobbin] does?</Q>

00:59:32 - Brandon Hancock: <A>I think it's a very similar concept, to be honest. I think 21stDev is free. And then the difference is they allow you to actually get the UI source code — it comes with instructions on how to update it. So they've taken it much further. You can open the component, copy the prompt, pick which tool you're using, and paste it in. And now it will know how to make it. They're basically taking the ShipKit approach but for strictly the UI — they'll come up with a thousand examples of beautiful UIs and let you pick the closest to what you're trying to do.</A>

01:01:51 - Paul Miller: Now, just more of a general money side of things in terms of creating opportunities. I have connected with someone who does sales training for lots of organizations. They go out and come up with a sales training course that looks at how a company utilizes their sales team and how they can become more effective. And I've said to them, "look, you think about the ideas of how you embed better sales practice." He's come up with like six opportunities in which there are people willing to spend money that connect to very baseline AI projects that I could churn out.

▶ If you're not in that funnel thing — getting that real niche stuff in an industry vertical — those are the people you want to align with. Find the top sales trainer in your local area and connect with them, because they have all the opportunities.

01:05:01 - Brandon Hancock: <A>I love it. And the cool part is they're literally selling, selling. The second you get into anything where you have a loop like that — anytime you have that meta loop — you just print money because it's like you just do the same thing all day and teach others how to do it.</A>

▶ The magic partnership is developer + domain expert: they know what the customer wants and the process; you know how to bring their idea to life. Two developers partnering up typically just step on each other's toes.

01:05:45 - Paul Miller: What we're doing — I'm saying to him, because I don't want to go out there and do the selling anymore. I just want to focus on the product. Because if it's becoming this easy to make the products and do it really well, then I just want to do that and do the shoveling where you put the money in the bank.

---

<!--SEGMENT
topic: End-to-End Testing, Load Testing, and Supabase Observability
speakers: Jake Maymar, Brandon Hancock
keywords: Cypress, Playwright, end-to-end testing, load testing, concurrent users, Supabase, Sentry, AgentOps, real-time subscriptions, database connections, stress testing, proxies
summary: Jake Maymar asks how to simulate concurrent users on a forum application to stress-test it before a large rollout. Brandon recommends Cypress for end-to-end testing and Playwright for recording manual interactions to generate test scripts. He also walks through Supabase's built-in analytics dashboard for monitoring database connections and response times, and recommends AgentOps for AI query observability.
-->

01:07:24 - Jake Maymar: That's brilliant. The selling, selling is brilliant. I'm sort of in that situation right now. I partnered with this guy that sells and boy, does he sell. We went from no clients to five and he wants to have like 5,000 users in this app that doesn't even exist.

01:08:08 - Jake Maymar: <Q>I have a question that might be kind of an odd one. What I want to do is I actually want to simulate users on a forum. So just pretend that you are on a Slack or any sort of communication platform, and you just start doing all the things — upload files, make comments, post different things. I basically want to create a series of agents that do that. I wanted to pick your brain to see if there's a better way to do it, if there's already a platform, because they need to interact with each other.</Q>

01:09:02 - Brandon Hancock: <A>You asked the right man. So it's called Cypress [tool:Cypress]. They've been around a long time. The problem you're describing — literally just clicking on the page, not testing functions — is end-to-end testing. You can actually use Cypress. Even the old-school version: hey, load this page, click this button, find this element, enter this text — and at each step, you're saying "this should happen."

▶ Here's what I would do first: I would say, "hey AI, I need to help build an end-to-end test. What I'm going to do is do the test manually first with Playwright [tool:Playwright]. I'm going to tell Playwright to click on this button, scroll down — so you can capture how I interact with a web page. And then once I'm done, I want you to turn it into a Cypress end-to-end test." And then it would do it.</A>

01:11:40 - Jake Maymar: <Q>And then the other one is concurrent users. I want to basically create a series of Playwright users doing end-to-end things all at once to just basically stress test it. Is there an obvious way to do that?</Q>

01:12:00 - Brandon Hancock: <A>So once again, I would still use Cypress [tool:Cypress]. The thing that I'm curious about is they have visit commands — like visit this URL or this page. The thing you would want to do is open up a tab per user. So user 1 is on tab 1, user 2 is on tab 2. I just haven't had to do that, but I'm pretty sure that exists.</A>

▶ The main thing you want to do is test load first. Make sure your database can handle potentially this many requests per second. Then watch for UI state bugs — like a `useEffect` accidentally triggering an infinite call — which can blow up everything. Those are probably the two most likely errors you're going to run into.

01:14:21 - Jake Maymar: Yeah, I think that's what I'm going to do. And then use Sentry [tool:Sentry], right? That's the other one.

01:14:22 - Brandon Hancock: Sentry [tool:Sentry] for error detection. And then final thing — you're using Supabase [tool:Supabase], right, Jake?

01:14:43 - Brandon Hancock: So you can see, like in the last 60 minutes on ShipKit, there's been like a thousand requests. And what you can do is go out to 24 hours. Here's what you'll need to look at — this is built into Supabase. You can quickly see what load looks like, what response time looks like. You can see database use. In my case, the ceiling is 90 connections. So I already know what my threshold is. I want to make sure when I'm looking at this, I never even get close to 90 — because if I am, I need to buy a more expensive instance of Supabase.

▶ Key thing: when you upgrade your Supabase instance, it completely turns off the app for like five minutes. So you probably want to do it in off hours or before the project starts.

01:16:18 - Brandon Hancock: <A>The main thing that I would need to do is start to add in observability. I would start to use AgentOps [tool:AgentOps]. It's my preferred one. AgentOps will track how long a query lasted, what the question was — you'll get a list, you can start to do some evals. They have a lot of stuff on there that I recommend. It's about $40 a month, so it's a little bit more expensive than the typical observability tool, but they do really good stuff.</A>

---

<!--SEGMENT
topic: AI Video Generation Workflow with Sora and Kling
speakers: Mitch, Brandon Hancock, Jake Maymar, Elijah
keywords: Sora, Kling AI, N8N, Supabase, Dropbox, video generation, AI video, Facebook monetization, TikTok, Looker Studio, Google Sheets, Amazon PPC, body cam stories, VO3, image-to-video, prompt engineering
summary: Mitch showcases an N8N workflow that generates AI video shorts using Sora and Kling AI, storing metadata in Supabase and organizing output in Dropbox. He demonstrates a body-cam-style AI video already monetized on Facebook, discusses the challenge of prompt engineering for narrative tension, and shares AI-generated product photography for a soap business. Elijah expresses interest in licensing the workflow for a franchise SEO client. Jake suggests using comment sentiment for reinforcement learning on future scripts.
-->

01:17:10 - Mitch: I built some N8N [tool:N8N] workflows for Sora [tool:Sora] video generation. So basically just built a simple form — user inputs this stuff. And I was having such a difficult time with parsing because we're taking like 50 different clips and LLMs have a really hard time parsing all that data. And I was just like, I am not thinking about this as simply as possible. I could just write a simple code snippet: find clip one, and then trim everything in between clip one and clip two. And that's the text for clip one.

▶ When LLMs struggle with complex parsing, a simple code snippet (e.g., find/trim between delimiters) is often more reliable than prompting the LLM to parse it.

01:22:04 - Mitch: This basically makes a large set of rows on a Supabase [tool:Supabase] flow, and then it makes the folder on Dropbox [tool:Dropbox]. So then once the Dropbox folder is made for each of those Supabase rows, that runs a separate workflow — which is an overview — and then it runs the generation status for Sora [tool:Sora]. But I'm changing it to Kling AI [tool:Kling AI], because it's like six times cheaper than Sora.

01:22:43 - Mitch: We have a couple of videos, but I'll show the one — mostly body cam stories. So this is a doctor that parks the motorcycle in front of the hospital. The cop is like, "hey, you can't park here." But she's trying to do a life-saving surgery. And there's some drama that goes on. But yeah, it was just posted five hours ago.

01:23:24 - Brandon Hancock: That's crazy. It's funny, because people are like, "wow, like, this is AI?" It's like, yeah — you can't tell from the video.

01:23:34 - Mitch: Because on Facebook, you have to really label that it's AI. Because these fake cop videos can cause a lot of drama. People really believe that it's real. And it's like, yeah, of course — she changes faces, and locations. I'm kind of blown away that people don't even notice.

01:24:02 - Brandon Hancock: What's so funny — our monkey brains are just like, well, if the story's good, I don't care. If it pattern-interrupts enough and gets your emotions, you really don't care.

01:24:18 - Brandon Hancock: <Q>Quick question — are you a Sora man? Are you using Kling?</Q>

01:24:25 - Mitch: <A>Kling is just like open router, right? So I mean, you can still use Sora. VO [tool:Google Veo] is decent, but it kind of misses the ball on certain things. The thing we can do with VO is you can have images — you can take an image and use that image as the starting clip for the next one. Sora can't use real people's faces — it'll stop that. So that's why when we use Sora, they're all different people. Whereas on VO 3 or 3.1, you can use the starting clip to be an AI person.</A>

01:25:07 - Mitch: And then this is what I want to share with you guys too — this is an update on the Looker Studio [tool:Looker Studio] stuff. So basically, this is like a list of Amazon data. And so you're able to make a query. With that query, you'll adjust the different data that shows.

01:32:39 - Mitch: <Q>Looker gets expensive, though, right?</Q>

01:32:42 - Mitch: <A>This is Looker Studio [tool:Looker Studio], not Looker. So it's free. Looker Studio is just like, you connect Google Sheets [tool:Google Sheets] and stuff.</A>

01:25:31 - Elijah: <Q>I think I might have missed why you were doing the video. Was that for a client or why you put that together?</Q>

01:25:43 - Mitch: <A>Yeah, because that page is monetized. So it makes RPM, right? And once it has a certain watch time, then you just make money from it.</A>

01:25:55 - Elijah: I'm literally building that. I just got an estimate yesterday. I'm working on building out that same workflow. He has a franchise business — he does all the SEO and content for all of his franchises. I don't know if you're interested, but I definitely love what you're doing. I think it's going to be easier for us to build something that's more customized. But you already built it. So if you want to talk, I'd love to talk to you about it.

01:26:44 - Mitch: Yeah, sure. I can shoot my email or something if you want.

01:27:00 - Jake Maymar: I actually love these things, Mitch. What you could do — because you have this flow — is you could actually take the comments and then basically do reinforcement learning to your script. So basically, it's not real, our face is changing, all those different things. But then you could create another video based on their comments about whether it's real or not. So very Inception — it goes very meta.

▶ Using audience comment sentiment as a feedback loop to refine AI video scripts is a practical form of reinforcement learning for content optimization.

01:28:57 - Mitch: I'm more of the mind, right now, still mastering the prompts. Because basically it has a really hard time finding the story and how to make a good story. Like, when we first did all the Sora clips, it was kind of giving the core value of the video at the middle. And there wasn't enough tension — like where the cop is trying to stop this person. So it has a hard time understanding what are the ups and downs of a video. And so that's really what I'm trying to address first.

---

<!--SEGMENT
topic: Developer Visibility and Personal Branding via YouTube
speakers: Brandon Hancock, Tiberius K, Ty Wells
keywords: YouTube, personal brand, freelance, LinkedIn, portfolio, ShipKit, AI development, content creation, social proof, client acquisition, transformation, ghostwriting
summary: New member Tiberius K, a self-taught AI developer with no formal coding background, asks how to find freelance work and showcase his skills. Brandon delivers an extended framework: the core problem for developers is invisibility, and the solution is YouTube content that demonstrates a clear transformation. He cites multiple community members (Vlad, Alexandra, Masatoshi) who landed contracts within three months of following this approach, and explains why YouTube outperforms LinkedIn cold outreach for developer lead generation.
-->

01:36:28 - Tiberius K: Hey, good evening, everybody. So I'm very new to the group. First time on a call. I don't have a coding background. So everything I do is just through AI. But I also don't use any platforms — Lovable, Bold. I'm working as if I'm managing a crew of devs. I work with the files. I work with VS Code [tool:VS Code]. And that's just Gemini [tool:Gemini] and VS Code. And I've built multiple TypeScript websites, a few TypeScript dynamic web forms. I create N8N [tool:N8N] workflows, Supabase [tool:Supabase] databases. And I'm just, to be honest, I'm looking for a way to showcase my skills and jumpstart or bootstrap my freelance work.

01:38:05 - Brandon Hancock: <Q>So are you looking mostly for freelance work? Is that the goal?</Q>

01:38:10 - Tiberius K: <A>Yeah, freelance. I really feel like I've got the abilities to work as a junior dev. I feel like I can do things quickly and a lot of things.</A>

01:38:40 - Brandon Hancock: I mean, hey — at this point, anyone with AI can basically build anything. It's just how long it's going to take them. They might not know as many approaches to solve the same problem. But you can get very, very far.

▶ The biggest issue that most developers run into is: no one knows we exist. That's the hardest problem to overcome as a developer. Even if you were the world's best programmer, but only two people know who you are — your potential for opportunity is two.

01:41:06 - Brandon Hancock: ▶ Biggest thing that's changed my life is doing YouTube [tool:YouTube]. It's a longer play. But as long as you're growing and giving value, the more opportunities come to you.

01:41:30 - Brandon Hancock: So let me be very tactical. I've actually helped a few people do this recently at the start of the year. Vlad got a contract, Alexandra got a contract, Masatoshi got a contract. And here's what they did. They picked three things that they were focused on — usually AI, coding, and something else. Just pick three things that you have an unfair advantage on. That's the thing — you need to have an unfair advantage. So your previous work, your contacts, whatever those three things are, double down on it.

▶ Then all you do is make content that teaches people how to make a transformation. The transformation I'm trying to do on YouTube is take developers of all skill levels and teach them how to become profitable AI developers. You can land contracts. There has to be a transformation that you want to take people on a journey through.

01:44:29 - Brandon Hancock: So here's the thing that's interesting, Tiberius, when doing the LinkedIn approach. What ends up happening is you have a specific solution you're trying to sell to customers. And what's interesting is they might not want that exact solution you're selling, but they could be open to you doing other AI work for them.

▶ The way we flip that on its head: the automation you've already made — you literally on YouTube say, "I'm going to show you how you can do this for free yourself." What's so nice about this is then people see what you're capable of and they come to you saying, "oh, I saw you could do this — could you do this instead?" You're just opening the conversation. Right now it's just knocking on doors — and if it's not that exact thing at the exact same time they need it, it's so hard to get a sale.

▶ YouTube is the best way to have a portfolio because you can just point to it. And especially once you start to land client work — the second you land the first client, the dominoes just start falling. You do the client work, you talk about the high-level concepts on YouTube (not sharing anything personal), and that showcases your expertise as a contractor doing AI-related work, which is more social proof, which leads to more work. And then it just snowballs. Do this for three months and you swap from no one's talking to you to "oh my gosh, I have too much work to do."

---

<!--SEGMENT
topic: Memorial TikTok App and AI Biographer Tool
speakers: Ty Wells, Brandon Hancock, Mitch, Patrick Chouinard
keywords: TikTok-style memorial app, iCloud, photo sharing, ShipKit, Otto Writes, AI biographer, Ashita, personal brand, family sharing, swipe UI
summary: Ty Wells shares a personal project built in memory of his father-in-law: a TikTok-style photo and video sharing app that consolidates family memories in a swipeable interface accessible via a shared link, solving the cross-platform problem of iCloud-only sharing. Brandon connects this to an AI personal biographer product called Otto Writes, and the session closes with encouragement for Ty and general wrap-up.
-->

01:49:16 - Ty Wells: So unfortunately, my father-in-law passed away yesterday.

01:49:21 - Brandon Hancock: I'm sorry, man.

01:49:25 - Ty Wells: Thank you. He was 93. What I did was I promised him the day before — to give him his own TikTok.

01:49:44 - Brandon Hancock: Let me see it.

01:49:55 - Ty Wells: So basically, I built him his TikTok because what happened was — that's in there. We had an album share in iCloud [tool:iCloud], but anybody with an Android, they're out, so they can't do it. So we sent out a message to everybody with the link, and then they could come in and like the photo, leave a comment or whatever. So it's all consolidated. And it looks just like you're running TikTok. And you can swipe up and out. I tried to pull some metadata — you can upload photos and stuff right here, and you can switch the videos and play the videos.

01:50:41 - Brandon Hancock: So that was him on the beach at like 87? Dude, that's the goal. Go ahead, man. That makes me so excited. Yeah, and you can share the link, and then people get to celebrate his life during the process.

01:51:09 - Brandon Hancock: Real fast, one other thing that could be cool. Oh, my gosh — what's her name? I have to look this up real fast. But she made that autobiography thing. It would be very cool to have the family all chip in and do their memories, and then it would come up with a story of his life.

01:53:00 - Brandon Hancock: <A>Yeah, it's called Otto Writes [tool:Otto Writes] — O-T-T-O Writes — but she, it's like a personal AI biographer. Obviously yours is post — like it's after — so very cool to check it out. She's a very talented developer. She just cranks out apps nonstop, so we definitely recommend checking it out.</A> [link:Otto Writes - personal AI biographer by Ashita on X]

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context (which was not supplied in this session):

- **Ana P** — passed through unchanged; last name initial only
- **Mitch** — no last name provided; passed through unchanged
- **Morgan Cook** — passed through unchanged
- **Alex Wilson** — passed through unchanged
- **Jake Maymar** — passed through unchanged
- **Tiberius K** — passed through unchanged; last name initial only
- **Adam** — no last name provided; passed through unchanged
- **Elijah** — no last name provided; passed through unchanged
- **Brandon Hancock** — treated as host/canonical name; passed through unchanged