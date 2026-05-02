=== SESSION ===
date: Not explicitly stated (references upcoming season start on "the 4th" and ShipKit pre-launch "tomorrow")
duration_estimate: ~2 hours 20 minutes
main_themes: ShipKit product launch, AI development tooling (N8N, LangFlow, ADK, Cursor), member project updates, freelance/consulting business development, structured data extraction tools, production scaling challenges

---

<!--SEGMENT
topic: Pre-Session Tool Discussion
speakers: Paul Miller, Marc Juretus, Andrew Nanton
keywords: N8N, FlowWise, LangFlow, Workday, Opal, Google, JavaScript, Python, MongoDB, FastAPI, Supabase, proof-of-concept
summary: Before the main session begins, Paul, Marc, and Andrew discuss the landscape of visual AI workflow builders. They compare N8N, FlowWise (recently acquired by Workday), LangFlow, and Google's early-stage Opal tool, sharing practical experiences hosting and building with these platforms.
-->

00:03:21 - Paul Miller
Hey, Marc.

00:03:24 - Marc Juretus
What do you say, Paul?

00:03:25 - Marc Juretus
How you doing, mate?

00:03:26 - Paul Miller
Good, good. I'm just a viewer today. Brandon is back.

00:03:31 - Marc Juretus
Oh, our keeper's back, huh?

00:04:07 - Andrew Nanton
Oh, Marc, was thinking about you the other day, because I remember mentioning on one of the previous chats that it looked like N8N [tool:N8N] was kind of the front runner for visual, you know, tool builder kind of stuff. But I did see that, I think it's called FlowWise [tool:FlowWise].

00:04:29 - Andrew Nanton
Which is another one that I checked out a while ago, because it ultimately produces — it's more of a Python-based tool, rather than JavaScript, which it seems like most of the other tools are pretty JavaScript focused. And I guess they very recently got bought by Workday.

00:04:48 - Marc Juretus
That's what we have at my hospital.

00:04:57 - Andrew Nanton
So, but I mean, that should give them plenty of funding. They just released a version 3 that looks like it might be worth a look. I guess that one's still alive. I thought it had sort of disappeared into the background with some of these other tools, but it looks like maybe it's still alive and kicking.

00:05:13 - Marc Juretus
Well, a guy in my job mentioned — did we talk about Opal [tool:Opal]? That's Google's version of N8N? Is that true?

00:05:24 - Marc Juretus
Somebody mentioned it and that they liked it, but I think what I recall is that they were saying it's still pretty rough around the edges, but it looked promising.

00:05:40 - Paul Miller
Yeah, it's a bit early on for Opal.

00:05:42 - Marc Juretus
Yeah, I was thinking if I did have any potential clients — for whatever real estate, this and that — it is a great idea to do the flow in N8N just for proof of concept before you get into some serious customization, if that's what you're doing.

00:06:00 - Paul Miller
▶ Yeah, I'm heavily getting into N8N, so I've got my own privately hosted one — I've stuck it on a droplet, and then I've put it alongside a MongoDB [tool:MongoDB] database, and then I'm building some sort of core proof-of-concept projects on it, but it's going really well. I'm enjoying it, because I just don't have time to build out a big back end for proof of concepts, and I need to spend as much time with the client and on the front end to get them excited, and it's the way to go.

00:06:44 - Marc Juretus
Yeah, agree. One of my reasons was to learn the frameworks at their core, so that I know both options. I couldn't get to ADK [tool:Google ADK]. I had some issues with that, so I rewrote that fantasy tool now in LangFlow [tool:LangFlow], so it's just about done. So now I'll probably go to N8N. And yeah, it's a back end with FastAPI [tool:FastAPI] and Supabase [tool:Supabase]. And then the front end is Next.js [tool:Next.js].

00:07:18 - Marc Juretus
One thing that sucks with LangChain [tool:LangChain], though, is there's always dependency conflicts. And then you got to let Cursor [tool:Cursor] find out — okay, you need this version with this version in the requirements file.

00:07:35 - Marc Juretus
<Q>Are you using UV for dependency management?</Q>

00:07:40 - Marc Juretus
No, I'm just using the Python environment variable. I should use UV [tool:UV], I know it, I just didn't use it in this project.

00:07:48 - Andrew Nanton
It might help.

00:07:50 - Paul Miller
Yeah, it's a good suggestion, Andrew. It saved me. It's so elegant, the way it deals with it.

00:08:05 - Marc Juretus
It's always with LangChain and dependencies. Like, for example, I can't even use LangSmith [tool:LangSmith] with this LangFlow project I have. Every time I try to bring it in, so I'd like to see the visualization and the flow, it just chokes out. And I was like, you know what, I don't need LangSmith that bad. It's working fine.

00:08:29 - Andrew Nanton
<A>And, you know, your statement made me realize I misspoke. It is LangFlow, the one you're already using, that's more Python-based. The other one, FlowWise, is another TypeScript sort of thing that's more like Node.js.</A>

00:08:46 - Marc Juretus
▶ Yeah, LangFlow, you have the nodes and it goes from node to node to node. It's basically the same as Crew AI [tool:Crew AI]. If you have a flow, Crew AI or LangFlow is the way to go. But if you're just doing a standard chat, you could just use LangChain. There's no reason — you don't need a complex flow at all.

---

<!--SEGMENT
topic: Brandon's Return and Updates
speakers: Brandon Hancock, Paul Miller, Marc Juretus, Andrew Nanton, Al Cole, Alex
keywords: ShipKit, Google ADK, ADK Agent Challenge, San Francisco, scuba diving, YouTube, Presentify, Cursor, agentic paradigm, pre-launch
summary: Brandon returns from vacation and a Google AI competition, sharing highlights from scuba diving and a Google-hosted coding challenge. He announces the imminent free launch of ShipKit, his new AI application starter kit, and previews upcoming YouTube content on agentic coding with Cursor.
-->

00:09:04 - Brandon Hancock
All fingers, all digits. The sharks, the fish — they didn't get them. Feels good to be back. I've missed you guys. Also, once again, thanks to Paul for holding down the fort.

00:09:51 - Brandon Hancock
So quick all-around updates. Diving — one of the coolest experiences ever. Absolutely love it. We did night diving, scuba diving, snorkeling, night snorkeling. Loved every single one of them. The only one I will never do again is night snorkeling, because you literally just walk into the ocean, and it just tripped me out. So many big fish, and I was like, I just don't like this.

00:10:32 - Brandon Hancock
A ton of updates for you guys on the code side. YouTube had a ton of videos in the pipeline. The Presentify [tool:Presentify] creator — awesome guy. It was really cool to hear exactly how he's launched multiple profitable SaaS startups, literally step by step. Did an 80K video for you guys. That one is like 40-plus hours of work trying to figure out how everything works.

00:11:22 - Brandon Hancock
Last week, I got to actually fly out to San Francisco for a Google competition. So Google does this thing called an AI agent challenge. Basically, it's like Top Chef, but for coding. You go and you build with 80K [tool:Google ADK]. You have five hours to build something. Can't announce what happened yet, but just know I went and had a ton of fun.

00:12:28 - Brandon Hancock
Drum roll. Okay, ShipKit [tool:ShipKit]. It is — the free launch starts tomorrow. So pumped for this. Bastian has been helping out. A few other developers have been helping out, have made an insane amount of progress on ShipKit.

00:13:00 - Brandon Hancock
It's not 100% ready for pre-purchase and everything, but it will be tomorrow. So yeah, all around have absolutely loved it. I have a ton — you'll see in the video on the landing page — but it walks through all the different templates, what they do, how they work, and what's going to be included in the course.

00:13:33 - Brandon Hancock
And then final update. I have a video coming up for you tomorrow that goes along with the pre-launch. It basically walks you guys through how to actually use Cursor and how to code in the new agentic paradigm. So I walk through exactly step by step how to do it.

00:14:33 - Brandon Hancock
So if you guys have any questions on literally anything, we'll do our normal — drop a question in the chat. Happy to dive into it. And then we'll just go around the room. I'd love to hear all the amazing things you guys have been up to while I've been out.

00:14:40 - Brandon Hancock
So asked so many questions to Google. A few major ones — I just wanted to understand what they're doing next. And the biggest thing is I complained a lot about friction areas. Like, it's very hard for people to use deployed agents in Next.js. And like, right now, would I recommend people to do it? I mean, eh, not really, because it's very hard. And I shared a lot of ways that they could fix it. Like, for example, Vercel AI SDK [tool:Vercel AI SDK] — you just install it, boom, you're talking with AI. So they literally have listened to everything. The lead project manager will actually be coming on the channel at the very end of the month and sharing more of the roadmap with you guys.

00:15:57 - Brandon Hancock
▶ And also, if you guys have complaints too, please send them to me so I can pass them along, because they want to know what we don't like.

00:16:05 - Brandon Hancock
Yeah, Paul, can dive into ShipKit real fast.

---

<!--SEGMENT
topic: ShipKit Product Deep Dive
speakers: Brandon Hancock, Al Cole, Alex
keywords: ShipKit, CLI, MCP servers, RAG, SaaS templates, chat applications, agent applications, Mailgun, vector store, Next.js, AI-first development
summary: Brandon gives a live walkthrough of ShipKit, his new AI application starter kit featuring six templates (simple and SaaS versions of chat, RAG, and agent apps), a CLI for local project scaffolding, AI-guided setup agents, and course modules. He explains the extensible design and plans to keep adding templates for voice agents, video generation, and more.
-->

00:16:09 - Brandon Hancock
Okay, so here's exactly what comes with ShipKit. What I've tried to do is multiple things at the same time. One, I've tried to aggregate what are all the most common types of AI applications that I have been asked to be paid to build. It comes down to just regular chat applications, RAG applications, and agent applications. So for each one of those project types, there's a template. There's a simple template and a SaaS template.

00:17:05 - Brandon Hancock
Inside of ShipKit, there are six templates total — there's a simple and SaaS version of everything. The simple is the best way to just play around with the technology. The SaaS is like, oh, you're actually trying to make money on this? Cool — added in all the additional features and functionalities that you need to just instantly spin up a SaaS version of an application.

00:17:32 - Brandon Hancock
What's really cool, though, is everything is AI first. So for example, if you wanted to spin up the chat SaaS application, you'll be able to do `shipkit.ai` — there's actually a CLI [tool:ShipKit CLI]. You get to do like `demo chat`, you get to pick the type of application you want. And what this will do is actually locally clone the application to your computer.

00:18:22 - Brandon Hancock
▶ It comes with all the MCP servers [tool:MCP servers] that I use for development. And what I wanted to do is to make this the easiest product that you guys have ever used. So instead of old-school learning — reading a document and then clicking around on the other screen — no, we have AI agents for everything. So this is just like the quickest one: to actually set up your project, we have a setup file that will literally step-by-step walk you through everything you need to do one step at a time.

00:19:15 - Brandon Hancock
▶ Let's just have agents actually verify your system is set up properly. Let's make sure that all your environment variables are set up correctly. So it's just going to check everything for you. You just add — every step along the journey from idea to production application — try to incorporate templates to make it as easy as possible. So yeah, agents just do the work. You just say go and it does it for you.

00:20:04 - Brandon Hancock
The other part that I think you guys are really going to like is — okay, cool, there's templates. Well, how do I take these templates and actually convert them over to a real-world AI application? And that's exactly what we have all modules for — that literally just help you go from coming up with your idea and then walking you step-by-step through kicking off a template, making your idea concrete, then how to actually come up with your development roadmap, how we're using AI agents to actually do all the work for you to build out the application, and then a bunch more templates at the end to help you set up Mailgun [tool:Mailgun] and all these other services.

00:21:00 - Brandon Hancock
Even the course has accompanying — every module has steps in it. Like, for example, in the beginning, when you're coming up with your master plan and trying to figure out how everything works, the templates are trained on the course, so they understand what needs to be done and will help you do it. So it's just like — at every point there could be AI, there is AI.

00:21:36 - Brandon Hancock
▶ Why I'm so pumped for this is the way ShipKit is set up, it's extensible. So what I mean by that is — one of the big promises of it is as time goes on, I keep adding more. So like, voice agents, creating video, like AI video shorts — I just want to keep adding more and more in here so it keeps getting more and more valuable.

00:23:31 - Brandon Hancock
So another thing that's going to be super cool for it is ShipKit is building ShipKit. So what I mean by that is ShipKit has a RAG template in here. So one of the cool things that is happening is every video module, every document, everything that goes into ShipKit will be in the vector store. So what's nice is at some point, if you're ever like, what did Brandon say to do to spin up chat SaaS? You'll be able to chat with the course.

00:24:27 - Brandon Hancock
▶ Please don't buy it today. Tomorrow afternoon will be good, but until tomorrow afternoon, please know it's not going anywhere. And then yeah — on the email sequences, there are a few bonuses that are given out. You get instant access to the previous course I made, the marketing course, you get instant access to that.

00:22:12 - Al Cole
It looks tremendous. It really does. And I am looking forward to getting my hands on this. I will learn a ton.

00:23:04 - Alex
<Q>Where do I buy it? I need it right now.</Q>

00:23:13 - Brandon Hancock
<A>We are wrapping up a few things right now to make sure the email sequences come out properly. So we're just wrapping up, adding a few videos. I just want to make sure when you get it, you get instant access. So that's the kicker. That's what we're fixing today and tomorrow morning.</A>

---

<!--SEGMENT
topic: Structured Extraction Tools: LangExtract and BAML
speakers: Andrew Nanton, Brandon Hancock, Jusin Gibbs
keywords: LangExtract, BAML, Google, structured extraction, graph RAG, triplets, Kuzu, Docling, long documents, citations, Romeo and Juliet, local LLM, Python
summary: Andrew shares his exploration of Google's LangExtract library for structured data extraction from long plain-text documents, highlighting its citation tracking and multi-pass chunking. He also introduces BAML as a more developer-oriented alternative for reliable structured extraction. The group discusses use cases including graph RAG triplet extraction and processing high volumes of similar documents.
-->

00:25:38 - Andrew Nanton
Not a lot of updates today. I've just still been continuing to work on playing with LangExtract [tool:LangExtract], that Google library for structured extraction for very long documents. Seems like it will probably be really promising for my work, both for general structured extraction, but also I've been trying to play around a bit more with graph RAG and extracting triplets for graph RAG. So that's what I've been up to. Short update today, but I'll put in a link to it because if people haven't looked at it, it's worth a look. [link:LangExtract GitHub repository]

00:26:25 - Andrew Nanton
And a couple of gross, weird people who camp on empty domain names have set up fake domains for it, but yeah, it's just this GitHub one. So it's pretty straightforward to get started with, and it does this cool HTML visualization of what you get out of it. So yeah, it's extracting — it'll show the character, the emotion, and the relationship. And because they go through all of Romeo and Juliet with just a couple of really simple examples, you can have it do like take a couple of passes at it. And because it's not super complicated, this seems like one that you might actually be able to run with maybe a local GPT model, because you may need to run it a couple of times to get decent accuracy. But if you really wanted to keep everything totally local, it seems like that wouldn't be out of the question, depending on how complex your task is.

00:27:32 - Brandon Hancock
<Q>So just because this is cool, I'm going to make sure I fully understand it. So I'm passing in text files or PDFs and it is extracting all text from the document. And it looks like you said it was also adding in some metadata to it — like this came from this section, right? Is that what's happening?</Q>

00:27:54 - Andrew Nanton
<A>Yes. So it does that by character count. It does not handle PDFs, only plain text, but it says this selection starts at character X and ends at character Y. And then if things are selected — like if you do two or three passes and it's selecting slightly different boundaries — it will combine all those together in a way that I still don't totally understand. It seems to do its own chunking under the hood. But yeah, I've been pretty impressed and it's moving very quickly. So if you do play with it, make sure you update the library often.</A>

00:28:35 - Brandon Hancock
Yeah, well, because the main one — Docling [tool:Docling] — I think you introduced that to the group. So it sounds like this one is best for just an insanely long document. From your experience using it, when would one use this?

00:28:58 - Andrew Nanton
<A>So the two things that make it interesting for what I'm doing — because I was between this and actually another one that you should take a look at called BAML [tool:BAML], B-A-M-L. There are two things that are relevant for me for this one. BAML seems much more developer-oriented and I'm not a developer. The other two things are: it's great for long documents, and it's great for very specific citations about where this information came from. And so those are two really key ingredients for me. It also is super easy to get started with.</A>

00:29:39 - Andrew Nanton
BAML — I sent Bastian a link and I'll put it in the chat. There's someone who wrote a guide — Kuzu [tool:Kuzu] embedded database — they have a couple of tutorials using BAML for structured extraction, specifically about building graphs, but it could be for anything. It really is just structured extraction, but it seeks to make structured extraction a lot more predictable and straightforward. It looks really neat. I haven't found any use for it myself, but another one that's maybe good to know about. [link:Kuzu BAML structured extraction tutorial]

00:30:38 - Brandon Hancock
<Q>I would be very curious to see how it works just compared to like a Gemini [tool:Gemini] structured output. Like that's one in my head — like why would I use BAML versus Gemini with a structured output?</Q>

00:31:05 - Jusin Gibbs
<A>I think BAML is based on the models that it's doing. So if you're going to do a thousand different receipts of a similar type, Gemini might get a couple of those messed up where BAML is going to make sure it's still getting the same structure when you're importing it.</A>

00:31:20 - Brandon Hancock
▶ Okay, cool. So they probably have a lot more backend stuff that's making sure it works every time.

---

<!--SEGMENT
topic: Marc's Fantasy Football AI App Demo
speakers: Marc Juretus, Brandon Hancock
keywords: LangFlow, Next.js, FastAPI, Supabase, fantasy football, react-markdown, Google ADK, streaming, N8N, Linear, Notion, project management
summary: Marc demos his near-complete fantasy football lineup optimizer built with LangFlow, FastAPI, Supabase, and Next.js. Brandon provides feedback on rendering markdown responses and shares his current view on Google ADK (great for non-streaming workflows). The conversation expands to project management tools including Linear, Notion, and using AI agents for to-do lists.
-->

00:34:11 - Marc Juretus
Hey, thanks for the video, by the way. That's on my consume list. So right now, what I've been working on — it's like 95% on the fantasy app. I guess I can show it real quick if you want.

00:34:39 - Marc Juretus
So you guys hear me chirping about this for the longest time. But anyways, this is basically my fantasy app. So it's a front end — it's Next.js. Back end is Python with FastAPI served up with Supabase. So basically, I can come in here. I can set the roster for it. So there's my players. I can search them. It has them out in groups. And then I have my starting lineup. I can add a player, edit a player. I can actually look at the rankings that are listed here for every player — the score that it has. And I can also edit some of the players that I have in my roster. I can delete them, add them, put them to the bench.

00:35:20 - Brandon Hancock
Dude, this is looking awesome.

00:35:26 - Marc Juretus
So, well, I mean, part of this process — and this is completely written in LangFlow as well. Yeah, I switched off ADK, man. I was like, man, I got to get this done. Season starts on the 4th. So, but at any rate, the main piece of it is it's going to email me its lineup. So what it does is it interfaces with Supabase, takes in the rankings that it's got for that week, and it has two separate ranking points, and it gives an average score. And then whoever has the lower score — you have to start two running backs, two wide receivers, a flex, a quarterback, and a tight end. So I basically say, get starting lineup. And this will get kicked off by a PowerShell job. But right now I can just come in here and if I click on email, it'll email me.

00:36:42 - Marc Juretus
So right now, I just have to factor in injury status, and I can't really pull that feed into its evaluation until injury status is available and relevant, which won't be for about another week.

00:37:33 - Brandon Hancock
I just dropped in the chat — I saw the response from the agents was in raw markdown. Cool thing, if you look in the chat, there are two libraries you can use: react-markdown [tool:react-markdown], and then there's a plugin. But what it'll do is, as the agent is streaming back a response, it'll automatically format it for you in real time. So that way, when the agent is generating a response, it looks super clean. So if you want to add that into your fantasy app, it could make the messages look more formatted — literally two imports and then that file.

00:38:14 - Brandon Hancock
▶ And then second — ADK for workflows, where you're doing stuff, as long as you're not streaming, I've had an insane amount of — it is so easy to use the backend. Now that I've figured it all out, as long as you're not streaming, so easy to use. It works perfect with Agent Engine, it works perfect with local development. It's so easy — create the session, send the message, and it just works perfectly. It's just streaming. Streaming is the thing — it looks cool, but it adds so much complexity and breaks. So if you're ever thinking about just doing a straight-up workflow, I still am really bullish on ADK, just not streaming right now.

00:38:55 - Marc Juretus
The app that I want to do — like if I want to try to stir up some work — is just a company where you can upload the resume for opening positions and it'll analyze your resume, let you know if you're qualified, and a bunch of other things. Like here's a full-function phony company with whole functionality with AI built in for different aspects of it. So that would be my other thing to have — just as like, hey, what are you doing with AI here? Go play in this phony company and you can see.

00:39:42 - Marc Juretus
<Q>How do you guys manage your to-do lists? I've been using Google Docs like a checklist. Are you using like a checkbox list? Is there something even easier?</Q>

00:40:00 - Brandon Hancock
<A>If it's an idea or a big project, it's going into Notion [tool:Notion]. If it's a long-term goal, like a vision, like a map for the next month, I have a huge board in front of me and I just stick high-level goals. So I usually break stuff down from goals for the month, then to daily actions on paper. And then if it's more of a bigger project where I need to keep up with stuff long-term, Notion. That's my system. And then if I am working with another developer, I use Linear [tool:Linear] for literally everything. I think Linear is such a cheat code when keeping up with to-dos, bugs, fixing. It's like Trello, but made for developers. And it's also hooked up to GitHub [tool:GitHub], so you can easily — they work together. So whenever you're in code and you check out this branch, and you make progress on it, it'll actually update the activity timeline.</A>

00:42:15 - Brandon Hancock
▶ And then Andrew and Patrick also have some really good ideas too. Patrick's going down the agent to-do list to keep up with stuff, which I think I should probably lean into more.

---

<!--SEGMENT
topic: Alex Wilson Job Search and Claude vs Gemini
speakers: Alex Wilson, Brandon Hancock
keywords: Claude, Gemini, Claude Code, MacBook, Cursor, GitHub Copilot, screenplay tool, personal branding, LinkedIn, YouTube, AI Authority Accelerator, job search
summary: Alex Wilson, recently laid off and new to Mac, asks about Claude versus Gemini for development. Brandon clarifies he uses Claude 90% of the time, reserving Gemini 2.5 Pro for large context window tasks. The conversation shifts to job search strategies including personal branding, content creation, and networking through people with overflow work.
-->

00:43:25 - Alex Wilson
Right now, I'm working on figuring out what job I'm going to do next. So I'm doing all the — I'm part of LHH for my last job and looking for work. Saul recommended a MacBook Air. So I had my first Mac in decades. So I'm getting used to it. I just started your course again, just to get everything set up.

00:44:01 - Alex Wilson
<Q>One of the questions I had is — you're using Gemini a lot now. What are you doing for like projects that you used to do with like Claude?</Q>

00:44:15 - Brandon Hancock
<A>So I am still mostly using Claude [tool:Claude]. Like if I was to map it out, it's 90% Claude. The only time I am using Gemini is for huge context problems. For example, that's how you saw I had that setup process that was going to walk people through the entire process. I use Gemini Max — like Gemini 2.5 Pro [tool:Gemini 2.5 Pro] on max setting — because I want to hit that million token context window. But outside of that, I am always in Claude 4.0, Claude 4 thinking. That's where I'm at nine hours of the time.</A>

00:44:54 - Alex Wilson
I built a screenplay tool and instead of using the projects the way you normally use them, I hooked it up to GitHub. So all of the assets that you use — like your script Bible and your character profiles and all that — I can just drop it from the editor directly into Copilot [tool:GitHub Copilot]. And then as you're writing your different scenes and everything, it has access to all that info in Claude.

00:45:33 - Brandon Hancock
<Q>Are you doing Claude Code [tool:Claude Code] out of curiosity?</Q>

00:45:38 - Brandon Hancock
<A>One of the big things I hope to work on next week is making — and I'll hopefully get a video up later next week — is on Claude Code subagents. I think that is an insanely valuable — you'll see in the video that's coming out tomorrow how I'm using templates to make sure when I'm writing code, it just does exactly what I want. But you can also achieve the same result with Claude Code subagents.</A>

00:46:46 - Brandon Hancock
▶ A few things that I have seen just recently, job-wise. I think it could be very helpful to find people who have too much work to do. For example, Dan Martell — the one that hopped on the group — he has that incubator where he helps out SaaS founders. And every time SaaS founders run into an issue, they go, Dan, do you know someone? And then from there, Dan goes, whoever's good in this field, I will just point to. So I think it could be very helpful to reach out and just say, hey, I am this developer, here's what I'm awesome at. If anyone on your teams ever needs help on anything in here, I'm happy to help.

00:48:00 - Brandon Hancock
▶ And also, if you ever want to talk more about building an AI personal brand, I would be happy to just give you — for your situation — a 30-minute crash course on exactly what I would do, just because all it takes is a little bit of posting for a little while and it just opens so many doors. The whole model is: give free stuff away on the internet to show that you're the expert and it will pay dividends, because people go, that was awesome, can you do it for me?

00:49:06 - Brandon Hancock
I think you watched that YouTube video I did a while ago on the AI Authority Accelerator [link:AI Authority Accelerator YouTube video]. If you want to rewatch it, and there is a Notion masterclass attached to it — I'll link that too. I would love for every one of you guys to have your own LinkedIn or YouTube.

---

<!--SEGMENT
topic: Paul's Political AI Briefing Tool
speakers: Paul Miller, Brandon Hancock
keywords: N8N, political campaigns, voter personas, RAG, parallel workflow, municipal elections, New Zealand, chatbot, social media, speech analysis, AI briefing
summary: Paul describes building an N8N-based AI tool for a local municipal election campaign that grounds candidates in voter concerns and party policy before they post on social media or speak publicly. Brandon suggests a parallel agent workflow to critique speeches per voter persona and recommends building a small platform with persona review, Q&A, and document upload tabs.
-->

00:50:46 - Paul Miller
Like Marc, I've actually gone down the N8N path quite a lot more because I've got so many balls in the air. The moment with different projects, I just need to focus on what the customers want — and the customers that are going to pay the money — and the customers want to see tangible deliverables, and then the money flows.

00:51:34 - Paul Miller
I think, you know, while I've always been impressed in my tech life about a really good back end and really well-built architecture, customers never get that. They're all about the front end and seeing a demonstration that knocks it out of the park in terms of delivering what they want.

00:51:53 - Paul Miller
As many of you might know, I get quite involved with politics. And at the moment, we've got a local body politics election — so it's for municipal. Mayoral elections, councillor elections. And sure enough, I'm involved with this huge group of people, all asking very similar questions. And while I won't get into the politics side, the challenge when you have a very grassroots organisation — linking that together with a little N8N process to say, I'm focused on this area in my city, these are the top three things that people have said they're concerned about, and these are the persona of the people that actually vote.

00:53:19 - Paul Miller
▶ Make an engine that puts that information through and guides people in a way that's not biased — that says, look, this is how people think. Put it through there, talk with the chatbot, get your — before you do a post on social media or you go and say something stupid at a press event — go through this, sense check what is core to your voter base.

00:55:46 - Paul Miller
And if you think in terms of the next steps — say if someone videos or records your presentation, you go and talk at some town hall, record that, put that back into the Google engine, play that audio back in there, you convert it back and you give them a rating and say, did you stick to the subject? How well did you do? You want to rate your candidates? In who you're going to put forward in the next election or in a more senior role, you can look at who's the most effective at communicating the party line.

00:53:57 - Brandon Hancock
▶ In my head, I instantly went to implementation of doing basically a parallel workflow — passing the message or the speech, whatever you're about to do next — and per persona, an agent would critique: here's what I like, here's what I dislike, here's what you could have done better. And then afterwards, combine all of their different reports and complaints. Once you have that feedback, generate an updated speech that drives it home with each demographic or voter persona.

00:56:12 - Brandon Hancock
▶ Cool thing, if I was in your shoes, I would try making a small platform for whichever party you're involved with — where you could do the persona review, a general Q&A, and an upload section where you could always upload more to the party database. So you could instantly get questions answered, and then boom — like, everyone in that party would have access to the platform and could spin up really fast and amplify their impact.

00:56:58 - Brandon Hancock
▶ If it works for one party, it works for all of them. That's why I think that'd be a very cool project to dog-food with your own organization first. Hey, we'd love to see a demo next week, man.

---

<!--SEGMENT
topic: Geo-Referenced News Monitoring Tool and Monetization
speakers: Alex, Brandon Hancock, Al Cole
keywords: Deep River, geo-referencing, news monitoring, supply chain, Mexico, logistics, SQL, LLM, custom newsletter, SaaS pricing, government clients, video editor
summary: Alex (the second Alex on the call) presents a friend's geo-referencing news monitoring platform (Deep River) that screens open media in near real-time and maps events geographically. The group discusses pivoting it toward supply chain/logistics monitoring in Mexico and a monetization strategy of selling customized AI newsletters to businesses, with an upfront customization fee plus monthly subscription.
-->

00:01:02:33 - Alex
So he has developed these — he's a mathematician mainly, but he studied computer science as well. And he's developed through a couple of years some geo-reference algorithm. So what this — he's working currently with more of these monitoring news agencies and government.

00:01:04:17 - Alex
Okay, so this feed takes — it's open media. It's screening, I think, like every half a second. It's processing news. And the added value of this guy — like you can see here how many times this news has been mentioned: 40 times, 128, 251. And you could come here to this event. And here you see like the principal trends. And the same — 367 times it has been mentioned. Then you have like by topic: law and justice, safety, security, politics.

00:01:05:18 - Alex
Here in the analysis section, this is where he grabs the content of the news and he geo-references it and puts it down in this map. Of course, it's focused in Mexico now. So let's say if I go to Mexico — if I just put like events that have happened around here — here, for instance, if I press here, I can see that there's like 59 news happening in this area. So it's pretty cool in terms of live monitoring.

00:01:06:28 - Alex
And we had a conversation to make these — and of course, like we're trying to develop this for supply chain monitoring in Mexico. Given the big amount of logistic transport, having one hour your bus stopped can mean a lot in terms of changes, especially for big companies. So when we had a conversation — we want to spin this because he's working already with governments and the tool, like we can tweak it to make it custom made. Instead of just being general news, let's just focus on monitoring retail for food specifics.

00:01:07:43 - Alex
▶ And I find this is like all mostly made with SQL-type algorithms. So the cost is like only — he uses a call to an LLM just for the final deliverable. So it's very efficient. It costs nothing to keep it operated.

00:01:08:13 - Brandon Hancock
▶ So I just want to share with you what I've seen people do that have been paid for applications. So another AI developer was reaching out to companies for work. And the thing that he ended up getting traction on and getting paid for was a custom AI newsletter for that organization. Every Saturday or Friday, he would go through, do all of that research. And every Friday, that company would get a tangible report on — in this case, if you wanted to go logistics, he would build it for them. And so the key lesson here is you might just want to make a demo version of it. And then it is a very straightforward playbook of going to each business and saying, hey, I've done this logistics at a high level, but I can tailor this to your business. And usually you'd want to charge some upfront fee — like a pretty high customization upfront fee — then just a monthly basis, depending on the size of the organization, many hundreds of dollars per month, because they get to share it with all their employees.

00:01:09:35 - Brandon Hancock
▶ And the cool part is 90%, 80% of the core technology to do it for one company applies to the next. At that point, you're literally just swapping out prompts for different companies. So it would probably be a pretty high-margin business.

00:01:11:00 - Alex
I think the user — I think they just want their deliverable given, like, in the morning and at night. And I don't want to deal with — using the tool would be more like an agency, I would imagine.

00:01:10:49 - Brandon Hancock
▶ Yeah, exactly. You're a custom news agency where you build the news they need for them.

---

<!--SEGMENT
topic: Al Cole's Freelance Wins and Business Model
speakers: Al Cole, Brandon Hancock
keywords: N8N, marketing agency, buzz research agent, social media crawling, networking, meetups, AI consulting, business development, N8N developer, revenue model
summary: Al Cole shares two new freelance opportunities acquired through in-person networking at AI meetups — a buzz research/newsletter agent for a digital marketing agency and a new lead from a business leaders group. Brandon and Al discuss the business model of fronting client relationships while subcontracting technical work to N8N developers, and the scalability of this approach.
-->

00:01:13:43 - Al Cole
So while you were gone, I picked up a couple of gigs. And this is me getting my feet wet. So it's early on the pricing. What I've got for the first one — because I know I'm learning — so with someone I've known for a while, they run a digital agency, so they want automation and they're looking for doing initially a kind of buzz research agent. And the newsletter idea was a different format than I was thinking. So what they've done is given me access to three clients that they serve and sites where you would find information about those clients. So they're looking for a kind of real-time summary of, is there anything out there that as a marketing agency they should be aware of, that they could potentially be exploiting. And then they're also looking for crawling social sites.

00:01:14:43 - Al Cole
▶ For me, the way to ease into this — it'll be N8N, I'll probably leverage that initially, and then just see how far I can get leveraging that platform, at least as a starting point.

00:01:15:35 - Al Cole
I actually have another opportunity that emerged again from another meetup last week. So I have been intermixing with just business leaders who are coming together just to talk about some AI topics. And I got yet another lead. I'm speaking to them first time Thursday of this week.

00:01:17:22 - Al Cole
So I'm focusing more on the solution side. When I've spoken to — so where I'll typically start when I'm in a room is I go find the organizer and I make sure they understand my interest in the group they have and my background and what I bring. And the way this happened was the business owner — he says, I've run it for 10 years as an analog business. He goes, we're all old school and it's been a great business, but he knows it is the time now where he's going to start thinking about automation. So he literally went to the organizer while we were at this meeting and says, I need a builder. Organizer said, I just met him. Go see Al. And that's how it happened.

00:01:18:27 - Brandon Hancock
▶ I love boots on the ground. You're getting in there doing it yourself. The hardest part is what you just did. Because now you get success for the first few guys, they tell some friends, and then you get the next guys. So it literally is a domino at this point. You have done the hardest part — zero to one — hardest part, and you're absolutely crushing it.

00:01:19:21 - Brandon Hancock
▶ And one other thing I just want to project forward — like you crush this, you do this for a client or two. What's so awesome is once you understand how these systems are built in and out, the real money-value-making skill in this is actually the networking and landing the deal. So going forward, you really could potentially bring on a developer of some sort — like an N8N developer, probably $30 to $40 an hour — and at that point, you're just overseeing and managing the contract, landing deals, and doing all the actual architecture thinking.

00:01:20:01 - Al Cole
<A>You just described exactly the business model I'm looking for — I want to be able to front-end it, but I'd like to be able to follow along as I participate in these calls with enough technical knowledge so I can at least steer a conversation properly. But ultimately, it would be tapping into the talents of others as this thing scales up.</A>

---

<!--SEGMENT
topic: Hemal's GCP AI Strategy and Dynamic UI Question
speakers: Hemal Shah, Brandon Hancock
keywords: Google Cloud Platform, Google ADK, evals, GCP, agent development, React, structured outputs, dynamic UI, calendar widget, Next.js, Atlanta
summary: New member Hemal Shah, working at a GCP-focused company preparing to roll out AI tools, shares his focus on establishing best practices and an end-to-end development framework for Google ADK. He asks about generating dynamic UI components (e.g., calendar widgets) from agent responses. Brandon explains using structured outputs combined with author-based message routing to render different UI components dynamically.
-->

00:01:21:42 - Hemal Shah
I'm from the Atlanta area. And I'm focusing on — so for my company, they are going to open up more, allow AI-related tools. It was like close-knit — they wanted to do a lot of security research and make sure all the policies are in place. So they're going to open it up in coming weeks, and right now I'm focusing on capturing all the best practices, identifying the right framework that we'll be using to create different AI-based applications. And we are mostly a GCP shop. So Google Cloud is what we are using, and that's where I was researching different Google ADK agents, and that's where I learned about your masterclass and came to know about this amazing community.

00:01:22:33 - Hemal Shah
I'm focusing a bit more on end-to-end development process that I can lay down the whole path for my company, so other engineers can look into that. For Google ADK, evals [tool:Google ADK evals] is another thing that I'm trying to find some information around — so that is one thing on my plate to explore a little bit, how to use evals in Google ADK.

00:01:23:04 - Hemal Shah
<Q>You mentioned about react-markdown earlier. I'm wondering if there are any other similar options — my understanding is react-markdown will provide the responses in more polished ways. But what if we want to also get some information from the end user, not in plain text, but maybe — we're booking a flight, user did not put in a date — so we want a date from the end user, but we want to show them nice widgets, a calendar widget or something. So dynamic form generation — instead of just text. If you have any recommendation on libraries that can give a jump start, that would be great.</Q>

00:01:23:50 - Brandon Hancock
<A>So I can go ahead and tell you high level what I've done recently. ADK is the one I've been using the most recently. What I'm doing is a combination of structured outputs and an author message to determine what message to show. Long story short, what I do is once agents respond, I check who sent the message and I'll check — using some structured outputs — of like what else is needed. In your case, if it was the agent, it could respond with a structured output of like input field or input type, and you would just say like calendar widget, billing information widget — like whatever the widget is you want to show — you could just have that pop up in real time and show dynamic UIs and take it beyond just a regular chat message back and forth.</A>

00:01:26:23 - Brandon Hancock
▶ What I end up having is like a message wrapper, and you basically just do like — if it is from this author, you show this component. So you basically just wrap it and then just have a switch statement to dynamically determine what type of UI to load. That's how I've been tackling it.

00:01:25:16 - Hemal Shah
Something like React JSON Form [tool:React JSON Form] and some of those libraries that can, based on metadata, generate dynamic UI. But just wondering.

00:01:25:27 - Brandon Hancock
▶ Yeah, I mean, the cool part is the agents are smart enough to tell you when they need information. The input fields that you're collecting information from — it's just at the end of the day, it's context. It's context that's going to go back into the agent in the form of a raw string.

---

<!--SEGMENT
topic: Temitayo's App Launch and Database Disaster Recovery
speakers: Temitayo Gbolahan, Brandon Hancock
keywords: Orientee, VPS, Contabo, Docker, CI/CD, database wipe, Supabase, Neon, backups, PostgreSQL, career orientation platform, production environment
summary: Temitayo shares the launch of Orientee v2, a college career orientation platform that got 80 sign-ups, but recounts a critical incident where a missing flag in a Docker Compose CI/CD command wiped the entire production database. Brandon recommends Supabase or Neon for managed databases with automatic 24-hour backups to prevent future data loss.
-->

00:01:29:48 - Temitayo Gbolahan
Last week, we launched a version two of our app, Orientee [tool:Orientee]. It's an orientation platform for those guys getting ready to go to college, university, and they are finding it difficult to choose a career path. So they basically use AI to analyze their scores and everything, and they also give them some recommendations. So we launched, we got about 80 sign-ups.

00:01:30:32 - Temitayo Gbolahan
Now, the funniest part about it is that we were working on a production environment. So one of the leads, he wanted us to have a test environment so that we could run some tests before we roll back to get them into production. So we had a VPS. And basically what happened was — I just forgot one simple command, a minus T, like a hyphen T that I was to put in a Docker Compose. So I ran a command for the test database, for the test environment, and everything in production wiped. Everything.

00:01:31:53 - Brandon Hancock
Oh no. Oh no. Dude, that is — that is the biggest fear at every startup I've worked at — hitting the deploy button. That is always my biggest fear because that actually does happen. And it's so easy. You said you missed like a dash T or something. That is a nightmare. That is like I have nightmares about that.

00:01:32:37 - Temitayo Gbolahan
To get the chatbot back, it took us a while to search for that, but we didn't record that — at least we had the emails so that everyone who signed up could sign up again. So we sent a mass email for them to sign up again, which they did. So everything's up and running.

00:01:33:37 - Brandon Hancock
<Q>Did you have backups?</Q>

00:01:33:42 - Temitayo Gbolahan
<A>At that time, we didn't have any backup. So that was the biggest mistake we did.</A>

00:01:33:51 - Brandon Hancock
<Q>Where is your database deployed? What are you using, out of curiosity?</Q>

00:01:33:55 - Temitayo Gbolahan
<A>So we got a VPS on Contabo [tool:Contabo].</A>

00:01:34:09 - Brandon Hancock
▶ Really quick recommendation — especially like, I don't know how many people are using the app, but Neon [tool:Neon] or Supabase — you could get so far on the free tier and it automatically has built-in backups every 24 hours. So like, just if you're looking for something that is free to use, I would definitely look at both of those just because when you're doing custom stuff, it's so easy to accidentally do that. And then all that progress you made, it's just hard to get back the momentum.

---

<!--SEGMENT
topic: Juan's Client Work, RAG Challenges, and GPU Deployment
speakers: Juan Torres, Brandon Hancock, Al Cole
keywords: RAG, Chroma, OpenAI embeddings, context engineering, vector database, A100 GPU, CUDA, Maxim, subcontracting, medical terminology, Istanbul, data science
summary: Juan Torres returns from presenting at a conference in Istanbul and shares two client challenges: a Brazilian surgeon's RAG system struggling with medical terminology retrieval (possibly needing specialized embeddings and better context engineering), and a separate project involving stress-testing an A100 GPU and building an API networking tool for a data center client. Brandon suggests connecting with community member Maxim for RAG work and recommends posting in the community for GPU expertise.
-->

00:01:35:13 - Juan Torres
Hey, good, good. I just came from a trip to Istanbul, Turkey. I'm still recovering. I think I got some degree of food poisoning. But it was awesome. I got invited to present my data science, data engineering project on the concentration of banking, which is kind of like an econometric modeling project. And people really liked it.

00:01:37:43 - Juan Torres
So right now I have too much client work. There's this physician, surgeon — Brazilian — that approached me through LinkedIn, and he wants me to help him essentially get his RAG system working. He's using Chroma [tool:Chroma], he's using OpenAI [tool:OpenAI] embedded models. And I don't think I have the time right now to be able to do it. I could do it by the end of the month, but I don't want to get too much work and not deliver good results for everyone.

00:01:39:49 - Juan Torres
My hypothesis is that he needs to create an embedding of the terminology and have a specialized agent that correlates the query of the user to the specific documents that he wants to pull. My two hypotheses are: the issue of context engineering, or the fact that he's using several vector databases and the model in the agentic system does not know from which database it has to retrieve the documents.

00:01:41:38 - Brandon Hancock
▶ I think Maxim, if you are looking for a developer — I think Maxim was taking on some RAG stuff. I mean, Maxim is like the RAG expert. So if you just wanted to hand it to competent hands, I think he was looking for just a bit of extra work. So I would definitely connect with him.

00:01:42:21 - Brandon Hancock
▶ The typical structure that I've seen most developers do is offer some sort of arrangement to another developer like, hey, I'll take anywhere between 20 to 30 percent and you do the work, and then you just charge the client a high dollar amount. That structure works. Everyone's incentives are aligned.

00:01:43:08 - Juan Torres
For one of my clients, I've successfully deployed a model on a server — an Oculus server. Now I have to go through the process — I have two tests at hand. One is testing the model. I've downloaded some CUDA [tool:CUDA] libraries in order to test the stress level I'm placing on the A100 GPU [tool:A100 GPU] for the local server. From the last attempt I tried to do a simple test, it didn't work out. So I'm assuming that even the 8 billion parameter model that I deployed might not be sufficient or might be too big for the specific GPU.

00:01:44:36 - Juan Torres
And then secondly, my client — the people in charge of managing the data center are attempting to charge him about $15,000 to $20,000 to create an API recall tool to basically allow the AI to communicate externally to other servers. So I am hypothesizing that perhaps I could help him create this networking tool without actually having to spend $15,000 to $20,000.

00:01:45:23 - Brandon Hancock
▶ Not at that bare-metal level — definitely out of my wheelhouse. But if you want to do a community post on that, dude, go for it. Just because there are 9,000 people — I'm sure there's someone that has more experience with the actual CUDA libraries and working on all that.

---

<!--SEGMENT
topic: Production Scaling, Cloud Architecture, and Tooling
speakers: Mitch, Brandon Hancock, Jake Maymar, Al Cole
keywords: Google Cloud Functions, Cloud Run, Cloud Tasks, EventArc, webhooks, Ngrok, Next.js, Convex, Redis, PostHog, Sentry, database indexing, connection pooling, Supabase, Cursor, Claude Code
summary: Mitch asks about triggering Google Cloud Functions via webhooks in local development. Brandon explains the Cloud Functions vs. Cloud Run tradeoff and recommends a queue-based Cloud Tasks architecture. Jake then shares anxiety about scaling a communication tool from 100 to 10,000 users using Convex; Brandon and Al Cole offer advice on database indexing, connection pooling, Redis caching for read-heavy workloads, and adding PostHog and Sentry for observability.
-->

00:01:46:33 - Mitch
So basically I'm trying to figure out — I'm able to do basically the Google Cloud Functions [tool:Google Cloud Functions], I'm running in local development, and I'm able to get it to mostly work. Now I'm getting to the point where I need to have it get triggered by like a webhook, and when I'm in local Python land, I don't necessarily know how to hook over. So I'm getting — need webhook into the local development. I'm guessing I would use like Ngrok [tool:Ngrok] and something like that to build up like a local development to public land. I was just curious about any opinion on that.

00:01:47:19 - Brandon Hancock
<Q>Are you using Cloud Run or Cloud Functions? Which one are you doing?</Q>

00:01:47:25 - Mitch
<A>You know, it was so confusing because they changed the name. So there's Cloud Run, but you can still run it on the Docker image or you can run it on the cloud function. So it's technically called Cloud Run, even if it's for Google Cloud Functions. But yeah, it's Cloud Functions, technically speaking, but it's still on Run.</A>

00:01:47:52 - Brandon Hancock
<A>So here's usually how the split works. Cloud Run [tool:Cloud Run] is usually for very long-running jobs — like you could basically just have a couple of full-blown FastAPI servers just running and deployed and always listening forever. Cloud Functions [tool:Cloud Functions] are more like Lambda functions, if you're familiar with that on AWS, where it's like you send in a request, and it will spin up and generate a quick response and throw the answer back. A Cloud Function caps out at 60 minutes, which is way less than what I think your stuff's ever going to hit.</A>

00:01:49:19 - Brandon Hancock
▶ So what you really could do — you'll usually want to do a few things. You'll want to have some sort of Cloud Task scheduler [tool:Google Cloud Tasks] — so you submit, everything's queue-based. You would submit something to the database, kick off a job. That gets added to a task. That task then gets consumed by your Cloud Function, does the work, and saves it back to your database. That is what the loop, if I was to build this, would look like. What's nice about this is every time you submit a request, the way you're spinning things up with Google Cloud Tasks, it can actually handle unlimited requests. Every request is going to spin up its own thing and just go to work.

00:01:50:00 - Brandon Hancock
▶ Cloud Functions — it's only going to spin up when it's working. So it's probably going to be like a dollar a month. So you're saving a lot doing this versus Cloud Run where you had this running as a backend job forever in Google Cloud — I think it's like $60 a month to have their basic version running 24/7.

00:01:50:41 - Mitch
Supabase has their webhook tooling. So then it would even create it. I just don't know how to test it on local development.

00:01:51:02 - Brandon Hancock
▶ That's the hard part about cloud versus local — they're two completely different paradigms because you can't locally just clone EventArc [tool:EventArc] — that's in Google. So once you usually get to a spot like where you're at, testing locally is starting to become less of a thing because you're so reliant on the cloud. The good news is you just spin up a production environment and a development environment, test the heck out of development until it's working, and then copy the changes to production. That's usually what I've seen most people do in these scenarios.

00:01:52:55 - Mitch
<Q>Side question — are you using Claude Code more than Cursor recently? Or are you still on the Cursor lane?</Q>

00:01:52:58 - Brandon Hancock
<A>Cursor, 99% of the time.</A>

00:02:05:00 - Jake Maymar
I think it's really just the production — like scaling this up — is what makes me nervous. It's definitely RAG, different flavors of RAG, sort of light AI prompts and some heavy AI prompts. It's a communication tool and a lot of moving pieces.

00:02:11:10 - Brandon Hancock
▶ Most failures I've seen when working on things are mostly related to the database. Like queries at a scale of a hundred users become exponentially more difficult on a large application because if you're not doing indexing properly, well, it doesn't matter at a hundred users. But when 10,000 users all have a thousand rows, you know, you're working with an insane amount of data. So indexing is insanely important. Another big issue I've seen in the past is working with concurrent database connections. Making sure you're using like a shared pool — instead of every client getting their own instant access to the database, it puts a pooler in front of it and basically just makes sure that you stay under your database connection threshold.

00:02:14:42 - Al Cole
<Q>Jake, do you tend to be read-bound or write-bound with that app?</Q>

00:02:14:46 - Al Cole
<A>So the reason I was going here, guys, is because I come from Redis [tool:Redis]. And Redis — this is where we would get the phone call. It's when the databases got absolutely hammered, fall over, and because they were read-bound, Redis had a role. Wherever you have play where you could leverage it — it is more than capable. You could go a million ops per second and you'd be okay. It's an extra infrastructure component, but if that was your concern and you're mostly read-bound, that could be a way to ensure you offloaded it.</A>

00:02:16:00 - Brandon Hancock
▶ I would 100% look into adding some sort of metrics to track what's happening in your app. PostHog [tool:PostHog] — phenomenal for that. You want to have Sentry [tool:Sentry] — so if users do have an error in the front end of the application, you know about it. The second there's 10,000 users, you just want issues to automatically pop up for you to address. In real time, you can be like, oh my God, I got 50 errors — boom, you get an alert on your phone, and then you know to at least tell people something's going wrong and you're on it.

---

<!--SEGMENT
topic: Patrick's Vibe Coding Framework and AI Personality Design
speakers: Patrick Chouinard, Brandon Hancock, Jake Maymar
keywords: vibe coding, shadow IT, enterprise templates, prompt engineering, personality traits, GPT-5, YAML, ChatGPT, voice mode, NotebookLM, YouTube, memory layers, system prompt
summary: Patrick shares two parallel efforts: internally consulting on a structured vibe coding framework for business users to safely prototype apps at his client company, and personally developing a sophisticated AI personality trait system (curiosity, restraint, sarcasm, etc.) with YAML-based configuration for use in ChatGPT projects. Jake asks about voice consistency for emotional AI personas, and Patrick notes that standard voice mode adheres better to custom personality prompts than advanced voice, especially with GPT-5.
-->

00:01:54:23 - Patrick Chouinard
So a couple of sides of Dr. Jekyll and Mr. Hyde this week. At the job site, at my client, I started to work on a new workshop — basically the whole development department asked me to participate in an exercise where they are starting to investigate vibe coding inside of the business. Basically creating — not for the developer necessarily — but because they have an issue with a lot of shadow IT. Basically, a lot of people in the business creating tools, but they create tools left, right, and center. There's no standard whatsoever, and it's very complicated to maintain.

00:01:55:11 - Patrick Chouinard
▶ So they want to see if they can use vibe coding well-integrated and well-managed — because basically what I would create is a list of tools for them, list of templates, a list of prompts, list of chat modes. So basically everything to give them all of the context they would require to create their prototype in the business in a way that, first of all, would not create huge security holes. Second, would be upgradable to an enterprise product eventually. So basically structure their proof of concept in a way that can be inherited by a true development group to upgrade to production value.

00:01:58:10 - Patrick Chouinard
So that's the Dr. Jekyll part. If I look at my personal project — I've now reopened my YouTube channel, but fed it specifically. It's basically all NotebookLM [tool:NotebookLM] created material. Since my project is all text — it's everything, it's philosophy, how to work with AI, things like that — I feed that into NotebookLM for their video creation, the video overview, where they create kind of a PowerPoint presentation with an audio presentation as well. All of those I store in the repo and I started to push them to my YouTube channel as a playlist. That's called a Clara Forge playlist.

00:01:59:14 - Patrick Chouinard
And this week, the big piece I've added is a personality trait system. So I've started splitting the personality of my agents into individual parts. So I have curiosity, restraint, whimsy, skeptic, obsession, empathy, sarcasm, sass, and I'm going to be working on a list of others. The idea is those are completely defined — the trait, the trait philosophy, the behavioral definition, and even trait configuration for the system prompt, the linguistic style pattern, integration guidance.

00:02:01:36 - Patrick Chouinard
▶ And that actually — quick note — with GPT-5 [tool:GPT-5], that is extremely sensitive to personality design. Made a huge difference on the type of output and the quality of output I got from the model in discussion.

00:02:02:19 - Patrick Chouinard
I create a project in OpenAI and I gave it this personality as project instruction. And then I just have multiple discussions and files with long-term memory. Basically, I've designed a system where I have three layers of memory that I work with. Personality is the first — this is where I'm going to put all the information concerning the behavior I want from the AI assistant. Short-term memory — basically all the chats that are within the project. And long-term memory is all the files I put in the project, because basically those are factual. I try to keep those as purely factual information for the model knowledge. The three of them together build that way — I have an awesome amount and type of reaction from the model.

00:02:05:09 - Jake Maymar
<Q>Have you hooked it up to voice yet? We might have already mentioned that, but... And how reliable are — like, I'm working on a use case where, sounds kind of odd, but people are crying or laughing or like different kinds of emotions. Do you feel like it's consistent or do you feel like it's kind of hit or miss?</Q>

00:02:06:03 - Patrick Chouinard
<A>All of what I do, all of the interaction is always through voice. Again, that's why I use ChatGPT [tool:ChatGPT]. It works well with Perplexity [tool:Perplexity]. It works decently with Gemini, but definitely the voice model used by ChatGPT is the best one. I found that so far — that's why I'm a little bit scared that they say they will retire standard voice pretty soon — because with this level of prompting or system prompt, I feel like standard voice is more true to the emotional tone I gave to the personality than advanced voice. Because advanced voice seems to want to put its own personality on top of it, and it flattened a lot of what I wrote in the prompt. It's getting better with GPT-5 — it adheres to the prompt more — but standard voice still has an edge.</A>

00:02:07:29 - Patrick Chouinard
▶ When you have very specifically defined character traits, especially with the configuration block in YAML [tool:YAML], where I actually gave them weight, it seems to reinforce it a lot.

---

=== UNRESOLVED SPEAKERS ===
- Alex (second participant named Alex, distinct from Alex Wilson — appears at timestamps ~00:23:04, ~01:01:51, ~01:09:17, ~01:13:36; last name not provided in transcript)
- Sam (New Zealand-based participant; last name not provided)
- Jusin Gibbs (name may be "Justin Gibbs" — passed through unchanged as raw name was "Jusin Gibbs")
- Jake Maymar (name may be "Jake Maymar" or similar — passed through as given)
- Temitayo Gbolahan (passed through as given)
- Juan Torres (passed through as given)
- Hemal Shah (raw name was "Hemal Shah" — passed through as given; may be "Hemal" per Brandon's pronunciation check)