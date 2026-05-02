=== SESSION ===
date: Unknown (Tuesday meeting)
duration_estimate: ~2 hours 25 minutes (00:06:01 – 02:31:07)
main_themes: ShipKit AI course platform launch, member project updates, AI development tooling (ADK/Vercel/Supabase), HIPAA-compliant AI infrastructure, LLM workflow strategies, personal branding and content creation, AI-assisted CRM and business automation

---

<!--SEGMENT
topic: Pre-meeting Chatter and OpenAI Naming Confusion
speakers: Tom Welsh, Hemal Shah, Mitch, Paul Miller, Ty Wells, Brandon Hancock
keywords: OpenAI, Codex, Claude Code, GPT naming, Omaha, Idaho, marketing, AI tools, branding confusion, Nano Banana
summary: Participants join the call and exchange casual greetings. Mitch raises frustration with OpenAI's confusing product naming conventions, particularly around Codex. The group jokes about OpenAI's marketing decisions before Brandon opens the formal session.
-->

00:06:01 - Tom Welsh
Thank you.

00:06:49 - Hemal Shah
You got a different background, Tom.

00:06:58 - Tom Welsh
I've moved house.

00:07:03 - Tom Welsh
Yeah, this is the new office.

00:07:06 - Mitch
Nice.

00:07:07 - Mitch
How was the move?

00:07:09 - Tom Welsh
Well, actually, we've been in on Thursday. No one's here yet. This place is still a bit of a shithole. That's where the computer is now, so time to move for the meeting.

00:07:22 - Mitch
I haven't been on the coding side too much, but trying to hop back into, like, Claude Code [tool:Claude Code] or Codex [tool:Codex], but the GPT naming is just so confusing with Codex. There's, like, four different Codexes. <Q>I feel like there's someone at OpenAI [tool:OpenAI] who's just like, how can we completely make this as confusing as possible?</Q>

00:07:48 - Tom Welsh
They're just screwing with everyone, aren't they?

00:07:51 - Mitch
Yeah. They don't use their own tools to come up with names, do they?

00:08:00 - Paul Miller
Yeah, yeah. You're a marketing guru.

00:08:12 - Paul Miller
<Q>How's the fishing?</Q>

00:08:14 - Ty Wells
<A>I'm in Omaha, Nebraska, so there's no fishing here.</A>

00:08:23 - Ty Wells
Well, there is a river, but you don't want to fish or eat anything out of that river.

00:08:30 - Paul Miller
It's a bit like our harbour at the moment.

00:08:36 - Tom Welsh
Auckland Harbour got problems, is it, Paul?

00:08:40 - Paul Miller
Well, it's kind of like the Thames used to be with overflows when it rains.

---

<!--SEGMENT
topic: ShipKit Platform Demo and Launch Update
speakers: Brandon Hancock, Paul Miller, Tom Welsh, Mitch
keywords: ShipKit, RAG, AI course platform, course modules, Google Cloud, deployment, Vercel, recording, launch date, AI-powered search
summary: Brandon gives the group an exclusive first look at the ShipKit AI course platform, which is built on a RAG-based architecture allowing students to query course content conversationally. He explains the platform's goal of teaching real-world AI application development and shares the updated launch timeline of the 27th.
-->

00:09:06 - Brandon Hancock
All right, hopefully y'all have had a good Tuesday so far. All right, let's get some screenshots going up in here. I have a very cool demo to show you guys here in a second.

00:09:23 - Brandon Hancock
So this is — y'all are getting the first sneak peek. No one else has seen this yet. So here is what the inside of ShipKit [tool:ShipKit] is going to look like. So basically, I think you guys know, but ShipKit — whole goal — teach you guys how to build and ship real-world AI applications in days instead of weeks.

00:09:48 - Brandon Hancock
What's cool is I have set up — recorded the entire process — but something that I think y'all will absolutely love is it is a RAG [tool:RAG]-based application. So what I mean by that is like you can talk to anything inside the course ever. So like if you're like, hey, what command did Brandon say I should do whenever I'm trying to deploy my queue to Google Cloud [tool:Google Cloud]? You can run it. And at this point, it'll go do all the RAG, all the fancy fun RAG stuff. And it'll come back and be like, oh, well, according to the course material, this is the command you need to run in your RAG application to get everything deployed. And then you can go click it. And then it'll take you to the relevant course module where it's all discussed and covered.

00:10:44 - Brandon Hancock
I have been staying up like three or four in the morning every night trying to get all of this working. And it's all finally coming together. So yeah, literally so pumped. This is like the full-blown ShipKit. So the RAG template was turned into this AI course platform. Still a little bit more to do in here, but the app's mostly done at this point. It's now just recording a ton — there's a lot of extra things to get recorded. So getting that done this week.

00:11:21 - Brandon Hancock
I'll have a cool video coming out tomorrow that I'll be sending out to everybody. It was on the 20th, but there's just literally no way to get it out by the 20th. So it's on the 27th, but everything will be good to go.

00:12:01 - Brandon Hancock
And Paul, I love the AI Paul — that is swamped. That's a really good pick. Where is that? Is that Nano Banana [tool:Nano Banana]?

00:12:14 - Paul Miller
I took my profile picture and I chucked it in. I've got a board meeting today and I like having a thematic picture that summarizes where we've been as a business for the month. So the board understands it in one image.

00:12:41 - Paul Miller
It's good, but jeepers, I need to duplicate myself three times and AI can only go so far.

---

<!--SEGMENT
topic: UI Testing Tools and Multi-Model LLM Strategy
speakers: Brandon Hancock, Hemal Shah, Andrew Nanton
keywords: Cypress, Playwright, MCP server, UI testing, LiteLLM, Vercel AI SDK, end-to-end testing, multiple LLM providers, OpenRouter, automation
summary: Brandon answers pre-submitted questions from Hemal and Andrew. He recommends Cypress for AI-generated end-to-end UI testing and Playwright via MCP for browser automation. For using multiple LLM providers, he strongly recommends LiteLLM combined with the Vercel AI SDK as a unified interface.
-->

00:13:15 - Brandon Hancock
Hemal, to answer your question: any frameworks, tools, recommendations on automating UI testing using AI?

00:13:24 - Brandon Hancock
Off the top of my head, there's a ton of just general UI testing. Cypress [tool:Cypress] is a really good tool to use. I would definitely check that out as a really good tool to use to build standard UI testing and just have AI create the Cypress tests that then do all the end-to-end testing. ▶ That's what I would recommend.

00:13:53 - Brandon Hancock
Full-blown AI clicking around in your application — I saw a pretty cool video a while ago — you can use Playwright [tool:Playwright] on your local computer and set up an MCP server [tool:MCP server] to use Playwright to then control your browser to click through stuff. But it's not as end-to-end. You'll pay a lot of money. Whereas you could just use Cypress and it costs basically nothing to run. So hopefully that's helpful.

00:14:30 - Brandon Hancock
And Andrew, to answer your question: if you're wanting to use multiple model providers, are you using the native SDK for each LLM, LiteLLM [tool:LiteLLM], or what? ▶ I'm a huge fan of LiteLLM. I use it religiously — like one of the walkthrough demos where we allow you to compare and test against multiple AI models, that is using LiteLLM. It's so easy to use, especially because you use LiteLLM plus you just throw it into Vercel AI SDK [tool:Vercel AI SDK], and it works so well. So it's definitely worth it — I think it's like ten extra cents. I can't remember, but definitely, definitely recommend them.

---

<!--SEGMENT
topic: Mitch's Networking, Content Strategy, and N8N MCP
speakers: Mitch, Brandon Hancock, Jake Maymar
keywords: Idaho Tech Council, content creation, follow-up automation, MCP servers, N8N, Amazon keyword research, Substack, LinkedIn, venture capital, agency tools
summary: Mitch shares his networking progress with the Idaho Tech Council and describes market demand he's hearing for AI-powered call follow-up and content automation tools. Jake introduces the newly released N8N MCP that can build workflows from screenshots. Brandon advises Mitch to take on client work immediately rather than getting stuck in a learning loop.
-->

00:15:20 - Brandon Hancock
Mitch, you're up first, buddy.

00:15:30 - Mitch
So I met with the head of the Idaho Tech Council, kind of showed her some of the stuff that I was doing. And it's kind of funny — when I'm getting in front of these people, I keep talking about showing them what I'm doing with content creation. And they're like, this is great, but I want this. Three people now have told me that when they're on these calls, they want follow-up emails, follow-up texts, and to take those calls, have the notes, and use that to make content. So it's just kind of what I've been hearing more and more.

00:16:08 - Mitch
She's talking to a bunch of different CTOs, CIOs, and she's connecting with the largest venture capital slash investment firm in Idaho. And she'll share with them what I'm working on. I don't need funding or anything like that, but just broadening up that network.

00:16:41 - Mitch
Like, doing the phone calls or taking phone calls and using it for follow-up stuff would definitely be very cool. And I think the other idea is taking all of the Substack [tool:Substack] articles and analyzing them, saving them as data, seeing what's new for the week, and really being the industry leader on a specific set of Substacks. And you could just rip it on LinkedIn [tool:LinkedIn] and Twitter, just completely copy and paste, so to speak.

00:17:17 - Brandon Hancock
Dude, both of those are insanely exciting. I'm curious if they come back and they're like, Mitch, we found this guy. He's ready to invest tens of millions of dollars. Are you ready?

00:17:32 - Mitch
You know, if it's tens of millions, I'll just say, sir, yes, sir, what do you need me to do?

00:18:00 - Brandon Hancock
I think you're starting to get into some really cool conversations with people that have actual real-world problems and have the capital to fund it. Do you think you're going to maybe try some more freelancing on some of this?

00:18:22 - Mitch
Yeah, I think there's a couple of things — definitely still want to make the videos. It's pretty easy once I build that tech infrastructure. And then I do want to dedicate a week or so just to stay up to date, because I've been so far off with MCP [tool:MCP], like creating your own MCP servers, really creating your own digital assistant using AI. I have a lot of tools I can plug in — like with Amazon Keyword Research, I could create my own MCP. Put in a product and then get all the keywords out.

00:19:38 - Mitch
Daniel Frazio is going to be so off base from all of the other YouTubers that you guys watch. But basically, this guy is like an agency guru. He started ListKit [tool:ListKit], which is like a cold email service. He's done like a bunch of stuff for other agencies, collected a lot of money — I think like over 25 million in net revenue for his own agencies. And he's basically just talking about how these agencies are with AI tools. His vocalization of the problem is very real and it was really articulate. So I definitely recommend people watching that.

00:20:17 - Jake Maymar
<Q>Oh, I was just going to ask, are you using the N8N MCP [tool:N8N MCP] they released? I was curious to see.</Q>

00:20:24 - Mitch
What's that?

00:20:25 - Jake Maymar
<A>So N8N [tool:N8N] released an MCP that allows you to — so you can take existing N8N workflows and then basically say how you want to reconnect them and it builds it for you.</A>

00:20:41 - Mitch
Does it build like a new system, even if I haven't created it?

00:20:47 - Jake Maymar
So I used the old version of it and it was pretty clunky. I was curious to see if this one — I think it's fairly new. You can send it a screenshot of something and it builds it.

00:21:13 - Mitch
Wow. That's cool.

00:22:08 - Brandon Hancock
Only other quick advice, Mitch — you're in such a cool spot. A lot of times people are like, man, I know everything there is to know about AI, give me any problem, I can solve it, but I'm not talking to anyone in the real world. You're on the other side, which is you know exactly what all of these people who are spending tens of thousands of dollars a month in overhead need. ▶ I would not want you to get stuck in the learning trap. I would just say dive in. Every time you hit a problem, ask us. I would be taking all sorts of client work on just to build out that portfolio.

00:23:11 - Mitch
One thing I was talking to the head of the Idaho Tech Council — she was saying AI education is so hard for all these universities because they don't have the budget. And the professors are so behind. I feel like there's such a giant gap. You could be in the education space — it's a really difficult problem to solve, but whoever can do it, there's a lot of money in the education space.

00:23:42 - Brandon Hancock
It's so funny. They don't have enough money, yet each student is paying $40,000 a year. My God, what do you mean you don't have money?

---

<!--SEGMENT
topic: Tom Welsh and Paul Miller Project Updates
speakers: Tom Welsh, Paul Miller, Brandon Hancock, Mitch, Ty Wells
keywords: asset management, inventory management, Kubernetes, on-premise, cloud, MBA presentation, Claude Opus, Claude Projects, master prompt, second brain, Tiago Forte, traveling salesman problem, CRM, AI consulting persona
summary: Tom shares his move and progress on an asset/inventory management system with on-premise and cloud deployment options. Paul discusses an upcoming MBA presentation opportunity, his use of Claude Opus with a master prompt methodology for consulting, and his exploration of the traveling salesman problem for route optimization as a potential product.
-->

00:24:14 - Brandon Hancock
Tom, you're up next, man. New house, new you.

00:24:22 - Tom Welsh
New house, nobody here yet, which is great. So I packed in working for my friend. The community just got too much, sacked that off. I've been working a little bit on my asset management programme, but not much. The majority of time it's been spent doing this, but I'm looking forward to the ShipKit stuff.

00:25:00 - Brandon Hancock
I know — we are hitting 70 hours of deep work. That's if I pee, I pause it. So it's literally you can't go any faster. But it will be worth the wait.

00:25:14 - Tom Welsh
I'm sure it will be. And actually I'm trying to find a video — just a thing from the BBC — that speaks directly about what Mitch was just saying about education. University crews were being interviewed about how things are coming along. They're talking about like creative writing's gone, software development's gone, computer science is gone due to AI taking over a lot of the opening jobs. It was quite a nice little eye-opener. That came out yesterday. If I find it, I'll post it.

00:25:57 - Brandon Hancock
Wait, so any development — you said the inventory management is on hold right now?

00:26:03 - Tom Welsh
Yeah, I'm spitballing just some of the setup for a standalone system, mocking up the configuration pages and stuff. That's all really just so you can set up, create a database out of the box, the whole lot — try and make it as easy for anybody to set it up, basically, if they want to load on-prem, otherwise it's usually a managed service.

00:26:29 - Brandon Hancock
You're going deep. Final question — are you going to be using Kubernetes [tool:Kubernetes] and everything to do on-premise stuff, or what are we thinking?

00:26:40 - Tom Welsh
Undecided. Some of these enterprises want two servers, an A and a B, just to back one up. But then a lot of people are now going cloud. So, yeah, see how it goes.

00:27:15 - Brandon Hancock
Paul, you're up next, buddy. What's going on in Auckland minus the cool AI pictures?

00:27:27 - Paul Miller
Well, look, it's quite timely. I had a local university in Auckland come to me. They run an MBA program. Can I rock up and present to the MBA thing? Of course, they've got no money to pay me. And interestingly, a lot of my target customers — there's like 60% of the industry I sell to — are doing the course. So it's a perfect funnel for me. I'm thinking I might go for it because I'm going to develop the pitch and I'm going to reuse that presentation for a paid conference that I've got. And I'm just going to use that to start testing my methodology and seeing how it resonates with that group.

00:29:00 - Paul Miller
There's a method around creating a master prompt in advising an industry vertical. So that's the chat that does the second brain book — whose name escapes me right at this moment.

00:29:20 - Paul Miller
Yeah, Tiago. So Tiago Forte [tool:Tiago Forte] has a master prompt instruction. There is an OpenAI GPT model that will help you build that master prompt. But build that to define a consulting persona that you then take, put it into Claude [tool:Claude], into Claude Projects [tool:Claude Projects], and say, I'm doing this consulting gig on the side. Here is my persona in the background, and the industry, and the people I'm selling to, and all the other stuff. And then use that to build a framework of deliverables you then charge for as part of that consulting engagement. So you just refer to that project and then say, oh, someone else rocks up — you go and do your pitch at the university or wherever you do the talk and you say, yeah, I can do that consulting gig. And you've got it at your fingertips. ▶ I do use Claude Opus [tool:Claude Opus] model for that to do it really well. And my God, it's good.

00:31:00 - Paul Miller
I reached out to Tom because he did this cool project on the traveling salesman problem. It's a problem that all of us that have been geeks for a while, have done programming for a while, would have dealt with — the challenge of if you've got a list of customers and you've got so many sales reps and you have to cover them in the optimal journey plan. So I threw that into AI and some of the really good models. I took the one from GitHub where it does the planning on the project side. And said, look, if I'm trying to do the traveling salesperson and knowing the following off-the-shelf open-source models, so don't just chuck it into Google Places API [tool:Google Places API], how can I solve this model in a smart way now? Monetize that as a business — and I've got three customers that are asking for it and I don't have a product.

00:32:10 - Paul Miller
Got the $25,000 of credits with Google. That's plan B.

00:32:19 - Brandon Hancock
So the course — this is going back to last week — you were talking about how you were going to start going out and talking at conventions to basically give away something with AI as kind of a way, an excuse to start talking to businesses, right?

00:32:41 - Paul Miller
So I've got the college wanting me to talk in the next three weeks. In November, I've got — we're doing sponsorship of an industry event because everyone wants you to come and talk about AI. Give me some practical giveaways that I can walk away with. You want to give them something out of the presentation, but then you want to leave them wanting more and wanting to come back to you and engage with more.

00:33:36 - Brandon Hancock
One thing — you referred to the second brain project that you've been using for the past few weeks. What I think would be really cool is if you wouldn't mind doing like a demo post in school. I would just love to see it in action at some point.

00:34:44 - Paul Miller
My biggest other challenge — and hence that photo I posted earlier — is I've got so many opportunities now. My funnel of opportunities is so broad that the CRM [tool:CRM] just can't keep up. I'd have to be doing all the data entry on the CRM. So I'm kind of thinking, well, if I can build something that maintains a whole lot of markdown files and says, here's all the customers and their opportunities, constantly update where customers are at in the comms and in the interactions. So you're always preempting what the next step is. So you suddenly get a call from a customer, you've got the context right at the time. I think that for me, that's the thing, but it's just getting the brain space to focus on that.

00:36:14 - Mitch
Yeah, so what I was sharing with them is how they could add — they can manage their memories and then customize ChatGPT [tool:ChatGPT], right? And then also I was using CliftonStrengths [tool:CliftonStrengths]. And then this would give me a look at who I am, who my team is, and then you can even input brand vision or your company brand messaging, et cetera. Put that into the memory. And then one of my demos — about what I've done and about me — is when I share with them the CliftonStrengths, I give them some example prompts. So my strengths are also weaknesses that are blind spots. Given this, here's my key benefit and then key blind spot and then my step for thinking. So how do I think and how does my team think? And then you can customize strategy to say, hey, this is my blind spot. If I show patterns of this, be sure to call it out.

00:37:33 - Paul Miller
Yeah, that's exactly what the master prompt methodology is all about.

00:37:58 - Ty Wells
Yeah, I guess I'll join the team because I'm doing the same thing. I'm taking an architect approach and a persona. So it's a combination of two, but yeah, we can talk about that offline.

00:38:28 - Paul Miller
The Dynamic Trio.

00:38:47 - Brandon Hancock
I definitely want to look at more of the AI CRM too. Salesforce [tool:Salesforce] has something, GoHighLevel [tool:GoHighLevel] has something, HubSpot [tool:HubSpot] has something. But I don't know which one of them — all the big companies sometimes just have something that doesn't actually do what you want. So that's why I'm very curious to see what you guys find out.

---

<!--SEGMENT
topic: Ty Wells Accounting Automation and Workflow AI
speakers: Ty Wells, Brandon Hancock, Marc Juretus
keywords: accounting software, accounts payable, accounts receivable, email parsing, invoice automation, workflow automation, human-in-the-loop, guided tours, reduction in force, restaurant app, Bahamas
summary: Ty describes how he evolved his custom accounting business suite from generating help guides and guided UI tours into fully automated AI workflows that handle accounts payable and receivable via email parsing. He reflects on the workforce implications and plans a demo of the updated system.
-->

00:39:12 - Brandon Hancock
Ty, speaking of, you're up next anyway. So what's happening, buddy?

00:39:18 - Ty Wells
Not too much. Just finishing up what I think I demoed to you guys last week. Waiting on ShipKit. So for that CRM — well, accounting business suite — that's what I demoed last week. So I ran into a problem. I realized that I had custom-written this to the needs of the company, and there was only one person to train those people. That would be me, because it's a brand new system. Nobody knows it.

00:40:04 - Ty Wells
So I obviously used the tool to generate some help guides, but then help guides as a walkthrough is really not much — you have to read a lot. So then I took it a step further and I generated some tours. So it'll tour the application showing this, click this, do that, do that. So now everybody — all you have to do is log in and it'll walk you through what you tell it. Hey, this is what I want to do. And it'll take you on a tour of the application. See, this is how you post an invoice. This is how you create a sales order.

00:40:53 - Ty Wells
And then I took it to another level. If I'm showing you how to post an invoice, I might as well do it myself. So all of my accounts payable — now I'm on that level of saying, okay, well, if the accounts payable person gets a bill to pay in, how do they normally get it? Via email. Okay, well, let me get a new email box that I parse the email, parse the invoice, and post the bill automatically. So what they were doing — I don't need them to do that anymore.

00:41:35 - Ty Wells
So basically, and then I started going down accounts receivables and sales and all of these different verticals to say, well, if I did a guided tour, I might as well just do the work myself, right? So the only thing I ended up with is some human touchpoints, where you have to actually interact, you've got to make decisions — the human-in-the-loop type approach. So that's where I'm at now. I built it. I haven't obviously deployed it because that's a reduction-in-force type effort. So I think that's where we're going to end up with more of these generalist employees that can do everything and the system prevents them from doing more than they should be able to do and controls the separation of duties. Especially in the accounting space. So yeah, I think I'm going to have a RIF here probably in the new year.

00:42:19 - Brandon Hancock
That's awesome. So from my understanding, you have certain workflow sequences to help out with different parts of the business. Are you building in your application straight-up workflows? Or is AI just kicking off the process and the AI is going through the workflow?

00:42:49 - Ty Wells
So yes, I am kicking off what I was training them to do with the help guides. After they log in, they would click on whatever to get their tasks done. What I've done is then taken that — because I've got that workflow built into the software, built into the application — I took those help guides and turned them into workflows. So now the AI is running those workflows when a new bill comes in, when they have to pay money in, pay money out, and do these things that a person would do, but it would be a systematic thing that they would do. I'm having the workflows do those automatically so the stuff that they normally would do, they don't need to do anymore because the workflow can do it.

00:44:01 - Brandon Hancock
Awesome. And other quick question — do you miss the Bahamas already?

00:44:05 - Ty Wells
I'm going back on the 29th. 12 days and counting, man. Hopefully some more fishing.

00:44:27 - Brandon Hancock
And then also good luck on the other app idea with the restaurant.

00:44:27 - Ty Wells
Yeah, that's launched already. That's why I'm going back.

---

<!--SEGMENT
topic: Marc Juretus App Architecture and Google ADK Deployment
speakers: Marc Juretus, Brandon Hancock, Hemal Shah
keywords: Google ADK, Agent Engine, Next.js, Vercel, Google Cloud Platform, LangChain, LangGraph, FastAPI, Supabase, Postgres, connection pooling, Railway, database architecture, Datadog, ELK stack, logging
summary: Marc reviews Brandon's ADK deployment tutorial and asks about hosting architecture — specifically whether Next.js must live on Vercel while ADK runs on Agent Engine. Brandon confirms this split and explains the database communication paradigm. Marc describes his new multi-feature LangGraph app. A discussion on logging and monitoring tools (Datadog, ELK stack) follows from Hemal's question.
-->

00:44:34 - Brandon Hancock
Next up is Marc. What's going on, Marc? How is all our fantasy apps?

00:44:43 - Marc Juretus
It's still running in the background running the league. So that's still working fairly well for the most part.

00:45:07 - Marc Juretus
So all I've done of late — I actually went through a great deal of your Google Cloud development kit one that you had. And in the end, I noticed that it actually gets hosted on Vercel [tool:Vercel] or something like that, if I'm trying to remember correctly, like the ADK [tool:Google ADK]. So in the end, you really can't host the app on GCP [tool:Google Cloud Platform]. It's really going to be on another instance and you're just pointing to the Google backend. Is that correct?

00:45:38 - Brandon Hancock
<A>Yeah. So just for context for everyone, this was the ADK deploy video. One of the things I was trying to show in the video is: okay, you have ADK and your web app, get them working locally, deploy ADK to Agent Engine [tool:Agent Engine]. That's cool. Now deploy our Next.js [tool:Next.js] application to the cloud. The easiest way to deploy a Next.js application is to Vercel. So the end state is you have Google Cloud running over here running your Agent Engine — so ADK is doing its thing — and then over here on the right, you have your Next.js application on Vercel. So they're both in the cloud. They're both talking to each other. But yeah, that's where it ended up at. You could, if you wanted to, go fancy and actually deploy the Next.js application inside Google Cloud, but you will spend so much time doing that.</A>

00:46:33 - Marc Juretus
Yeah, there's a lot of stuff in that, man. I got to admit, there's a lot going on to get that. It was good for a foundation of what's going on. Your demo was actually pretty cool. I can't imagine how many times you had issues with something not working right. My hat goes off to you, man.

00:46:55 - Brandon Hancock
I was emailing because I was like, guys, I got to make this video. It'll take a week. It'll be so easy. I'll just flip it up. It took weeks, plural. It took like three to four because I had to constantly email them and be like, guys, this doesn't work. This doesn't work. What's going on? And they were like, oh, thank you for letting us know. We didn't know — which was very upsetting.

00:47:30 - Marc Juretus
So what I'm doing right now — it was the app that I told you — but I'm going to do this in LangChain [tool:LangChain] LangGraph [tool:LangGraph] where I basically have an application — a video game site, but on top of that, it's also a site that does like those bar touchscreens, like that you have in bars that you can play those games. And it's just going to be all fake, but I'll have jobs posted up there. I'll have the agent actually review your PDF resume, see if you're qualified. If so, it'll send you an interview. I'll have a contact thing where you can query and basically ask what's in inventory. A section where they can build their own game that you want to have made by our staff. So I can basically show, hey, what have you done with AI? So I have about four or five things going off of that site running. So I'll do that on Railway [tool:Railway] with LangGraph.

00:48:22 - Marc Juretus
<Q>I will ask you this, though. Is the best way for using Supabase [tool:Supabase], and I'm going to use FastAPI [tool:FastAPI] — is it best to use the actual Postgres connection string as opposed to the APIs for security reasons? Is that a more secure way of going at it to get into data?</Q>

00:48:40 - Brandon Hancock
<A>Yeah, so the question — I'll restate it — which is, at the end of the day, for most real-world AI applications, you end up with a database and multiple sub-applications. So in Marc's scenario, he's probably going to have a web application and a Python application of some part — LangChain, CrewAI, something. And usually you have to get both of these applications to listen to each other. So there's multiple paradigms. Paradigm one is your Python application, every time it needs something, it sends it to your Next.js application. Paradigm two is they actually do not talk to each other directly at all. Everything is shared in a common shared database. I think you will have much better — it'll be faster, more secure. ▶ The gotcha though, is when using a database, it doesn't matter which database platform you're using — Supabase, Neon [tool:Neon], any of them — you have to worry about the maximum number of database connection strings. One thing I really like about Supabase is they do a thing called a pooler, which basically says, hey, I will allow 10 people to talk to a pooler, and then this one pooler will take all those different connections and make one connection to the database, because you can very easily exhaust database resources. So Supabase handles that for you. ▶ Definitely recommend the second option where everything talks to the database and they go back and forth.</A>

00:50:20 - Marc Juretus
Yeah, I'm trying to connect directly for the FastAPI thing for when it's calling inventory — right to the string — but I'm still using Supabase for the front-end authentication, but it would be a Next.js front end and then a back end that's basically FastAPI. That's the manner that I'm going to build it in.

00:50:40 - Brandon Hancock
Yeah, that sounds great. Usually what you'll do is in your Python project, you'll create something called a database service. The database service is going to be using Postgres [tool:Postgres] because Supabase is using Postgres. So you basically just say, here's all my information from my database, here's my database passwords and everything. And at this point, you have one database service that all the different components of your application can reach out to. So your database just needs to be able to insert data, read data, edit data, delete data. So you basically just have one database service that handles everything. And then you just build custom functions on top of this.

00:51:49 - Marc Juretus
And I just have one small quick question. So I see Ty's talking about that, Paul and CRM. In a nutshell, is that just the customer relationship management where you have like you're keeping data, sending emails? What is the whole summary of what a CRM is in your mind?

00:52:09 - Brandon Hancock
<A>Everything. Something that you just said — basically, as a software business grows, you need to keep up with how many customers you have, what is their information, where are they in the sales pipeline journey, you need a way to contact them. So it's basically just all things related to knowing about your customers, where they're at, and then having the ability to act on it, send them emails, send them promotions. That's basically a CRM in a nutshell.</A>

00:52:44 - Brandon Hancock
And I know, Hemal, I saw you had your hand up for a while. Sorry about that.

00:52:54 - Hemal Shah
No worries. I just had one comment to Marc on his previous question about deploying to Vercel and Google Cloud. I went through, Brandon, your Next.js full-stack deployment tutorial. It's very clean. Most of my stuff is in GCP and from a troubleshooting perspective, I was just thinking if the application is also deployed in GCP in one place, then all the logs, alerting, monitoring — not for the small application, I think Vercel is perfect, but when you want to go a little bit deeper, that's what I was exploring. Firebase [tool:Firebase] and Cloud Run [tool:Cloud Run], Firebase, some combination, but like you said, you have to jump through several hoops to get to that state.

00:53:44 - Hemal Shah
If you're looking to synchronize logs across multiple platforms, there's a tool called Datadog [tool:Datadog].

00:53:51 - Brandon Hancock
Be careful if you give them your information. They call nonstop. Like if you sign up, I've never gotten so many calls from one platform before. But they do have a really cool tool where you can import logs from all of your services. So your Next.js Vercel application, you'll just set up Datadog, it'll put it there. If you're doing Google Cloud, Railway, whatever you're doing, it'll also ship the logs to one space, which is really nice because then it's one place to monitor everything. You can set alerts. They have a really nice tool. You'll see a lot of big companies will always usually use Datadog.

00:54:31 - Hemal Shah
It's a little bit pricier, and they have a very aggressive sales team.

00:55:44 - Brandon Hancock
There's a thing called the ELK stack [tool:ELK stack]. Basically it's a way for you, using open-source software, to manage your own logs. And it has a really cool way for you to view the current status of your application. Usually for most projects, this is way too in the weeds, but if you were building an on-prem solution for someone or working with Kubernetes and you wanted to monitor the health of all your different deployed applications in one nice way, you would use the ELK stack. ▶ For most simple one-to-two app applications that you have deployed to the cloud, I would just say if you need to track logs in multiple places, Datadog is way simpler. You're going to pay a little bit extra, but it's way simpler to use.

---

<!--SEGMENT
topic: Andrew Nanton's Multi-LLM Desktop App and Vibe Coding Strategy
speakers: Andrew Nanton, Brandon Hancock, Jake Maymar, Ola Oyo
keywords: PySide6, Toga, Textual, Electron, LiteLLM, Anthropic BAA, Azure, Claude, factory pattern, router pattern, Watchdog, FastAPI, plan mode, Claude Sonnet, Grok 4, unit testing, Codex, LangGraph
summary: Andrew shares his struggles building a local desktop GUI app that uses multiple LLM providers (Anthropic via BAA, Azure) while handling native features like PDF ingestion. Brandon recommends software design patterns (factory, router) to manage multi-model complexity. A broader discussion follows on AI-assisted coding workflows: using high-capability models for planning, cheaper models for execution, and incremental test-driven development.
-->

00:56:51 - Brandon Hancock
Next up is Andrew. What's going on, man? What are we working on?

00:57:05 - Andrew Nanton
Okay, whole screen. You have the report drafter. So yeah, I've been back working on some of this here. Although I mentioned last week that Toga [tool:Toga] is really convenient for local GUI stuff, I'm back to PySide6 [tool:PySide6] because I just needed some options that weren't possible in the other one. So it's got a lot of complexity there, and I feel like I am vibe coding far too much of it, and I'm going to just dig myself into a hole that I can't dig out of.

00:58:06 - Andrew Nanton
This is part of what I was asking about with using multiple LLMs, because part of this I have — so the hard part is I have a BAA, a business associate agreement with Anthropic [tool:Anthropic], and then it's included in your Azure [tool:Azure] subscription, basically. But because all of my information has to stay really secure, I can't use something like OpenRouter [tool:OpenRouter], where I can just use one key. So LiteLLM — I was looking at that as a library that I can just use and tell it, okay, this one goes to Anthropic, this one goes to — and I tried that before, but part of the problem that I had is that I wanted to use some of the native features that were not wrapped in that functionality, like Claude will natively handle sending it a PDF where GPT does not. And I think maybe Gemini [tool:Gemini] does now. And I don't know, this stuff changes every 10 minutes, right?

00:59:23 - Andrew Nanton
So I was like, okay, well, here's what I'm going to do. I'm just going to use the native SDK for each one. And then I know that I can get all the features that I want. But then I end up having to manage all of that in the business logic. Well, if it's a PDF, then this time you do that. And the complexity gets really overwhelming really quickly.

00:59:47 - Brandon Hancock
So do you want a quick tech deep dive? If you would definitely, as you're working on this — we're at the point where we need to think at a higher plane and say, hey, which types of software design patterns should I implement to handle this situation? So you're going to have to look into the factory pattern [tool:factory pattern], which will basically spin up a different LLM response instance. So if it's a PDF, the factory will generate an instance of, say, the Gemini model that can handle that. Another approach is to have some sort of routing functionality. ▶ I would start to say, let's look at design patterns that we should be implementing to make this as easy as possible. Because if you just say, hey, fix this — oh, and by the way, it should handle OpenAI, by the way, it should handle — it'll be soup. It'll be disgusting.

01:01:00 - Andrew Nanton
No, no, I still continue to steadily maintain that most of my code is a war crime. And so I am having a lot of it just cranked out by Claude. But almost all of that is plan mode. You know, it's like, okay, here's what I want to do. All right, are you sure? And then can you review the documentation? Is there a less complex way we can do that? And then I will have it put all that into another document, lobotomize Claude and start over and be like, hey, look at this plan. This guy I know said it was a good idea. What do you think? And so I mean, that — I would rather spend — a stitch in time saves nine, I guess. Like, that never feels like time poorly spent to make sure that there's a good blueprint to go from.

01:02:10 - Andrew Nanton
I've ended up trying to do a full rewrite a couple different times. Another time I tried using Textual [tool:Textual], the Python TUI framework, because everything I keep running into is these LLMs are awesome with web technologies, but I want to deal with files on disk. And I just continuously run into these things really don't like to play well together.

01:03:22 - Andrew Nanton
I had another one where I tried like a sort of a stateless FastAPI [tool:FastAPI] thing where it was like, okay, you just sit here in the corner and I'm going to send you something at this API endpoint and you send something out. But trying to get like a Tauri [tool:Tauri] or Electron [tool:Electron] front end to start a Python backend, manage that Python process — it's a mess. And so I was like, okay, I'm back to just all Python all the time.

01:04:00 - Brandon Hancock
So thought on — you did say Electron. That was literally one of the questions I was going to ask. I was curious why we're not using Electron everywhere. Why you did not want to go down that approach.

01:04:13 - Andrew Nanton
I tried it. And like, a lot of the complexity around interprocess communication, managing, starting and stopping the back end has been a persistent problem in every iteration of this technology. I know this is a solved problem, right? Like I know other people know how to do this, but what I keep running into — no matter how many times I tell Claude or give instructions or try to wrap the process management around — do not start another instance of the back end. It's like, oh, that port's busy. I'll just fire up another. Like, no, no, don't do that. That's not what I want. Only ever one — and then let's do a global lock file — I just only ever run one back end and it has been a losing battle.

01:05:28 - Brandon Hancock
One thing that I always do — I used to just allow every request. And I've changed it to use an allow list. And I've just slowly, as time has gone on, allowed it to do more things. Because the exact thing that you're recommending — it would always do npm run dev. And I'm like, no, it's already running. Like, I don't need it to run another instance. ▶ So I would always check out the allow list just to have it not accidentally spin something up.

01:06:11 - Brandon Hancock
And very final comment — the way you phrased it, I like better. You'll use the highest thinking model, like Claude Sonnet [tool:Claude Sonnet] with the 1 million token window, to come up with the blueprint and then lobotomize it and use a cheaper model. ▶ That's literally what I do every step in ShipKit. I use the 1 million token window to come up with a plan using Claude Sonnet. And then the second the blueprint is there, cool — so no more high-level thinking. We can now have a smaller, cheaper AI model do the actual work. And it leverages AI at what it's best at. Big models, great at thinking. Use the other less expensive ones when you just need to, hey, just do literally what that file says.

01:07:01 - Jake Maymar
<Q>So I'm curious, if you don't mind, what model are you using that's cheaper? Because are you thinking like Flash Lite or Flash?</Q>

01:07:09 - Brandon Hancock
<A>When I say cheaper, I'm just saying everything is cheaper than Claude Sonnet 1 million. Everything. So when I say cheaper, it's just like — here's my normal tier list. We'll use Claude Sonnet 1 million anytime I'm working on a big task. So anything that's medium or high level complexity, do the task template thing that I've shown you guys multiple times where I'm like, hey, here's the context, here's the goal, here's the issue, go search the code base, proceed to think through the whole process and come up with a task literally any AI model can follow. And then at that point, I just toss it to Claude Sonnet, thinking not on Max. That's been my current workflow to make sure I get really high-quality results. I've also — y'all saw the post — Grok 4 [tool:Grok 4]. Doing fast. Phenomenal. And just also working on those task documents on medium, simple tasks. I've been loving it. You can't give it images. That's the only thing I dislike, but I mean, it's free. So I will save whatever penny I can save right now.</A>

01:08:32 - Jake Maymar
<Q>And then I had one other question just really quick. Does it make sense to make small, very, very simple — this is sort of a question for Andrew, but also a question for Brandon. What I've been doing is when I get really stuck on something, I'll make a very, very, very simple version of it, get that working. And then I try and integrate it. But sometimes integrating is just like a freaking nightmare. And I'm wondering if you guys have any tips on that?</Q>

01:09:11 - Andrew Nanton
<A>Oh, so I have found that the alternative is just as bad or worse. Like, trying to have it do the whole thing — having to do one large, complex thing — like, okay, I want six different plates spinning at once — that almost always blows up in my face. Whereas, incrementally — okay, I know this is working. At least for me, what has been helpful is write tests, and then do the thing and run the tests. And because tests are boring and long, and Claude is happy to write them. I feel like that is a good hackstop. I've had more success with building up complexity incrementally and then trying to get it pulled in than the other way around.</A>

01:10:41 - Ola Oyo
One thing I've interestingly come across is ChatGPT's Codex [tool:Codex]. When you put it on the high reasoning capability, unlike Claude Sonnet that will go and hallucinate exactly what is in your code base and come back and say, oh, sorry, I didn't look at the code base before going ahead — Codex systematically will go through your code base and help with that huge plan. So where I typically start from is — if I have a task, like say, for example, now I'm trying to create dedicated virtual accounts, right? I literally start from ChatGPT and I say, okay, this is what I'm trying to do. Can you please give me the instructions to build a GPT for this specific task? So it goes, gives the instructions. I put that into ChatGPT. I take that also, put it into an agents.md, which is something that the Codex model is able to see. And with that, it looks through the entire code base and it's able to actually structure a plan. I have that plan. I put it in a markdown file also. Then send Claude to sort of do its thing, saying, based on the instructions for this specific task and based on the plan, then start working through things. ▶ And I also find that Codex is actually also better for testing because it looks at all the other dependencies. So Codex is good for planning, Claude is good for fast iteration, but then GitHub Copilot [tool:GitHub Copilot] with Claude 4 is like your senior developer that finds things that typically Claude will just go and mess up.

01:12:25 - Brandon Hancock
I absolutely loved all of that. ▶ The only thing I was going to mention — the second you do have a simple working application, kind of stealing between what Andrew and Ola just said — hey, here's our current code, here's our working code, come up with a plan to make that work.

01:13:50 - Jake Maymar
<Q>And because to run all of those — I guess that's the question. Do you run all of the tests after every feature? Because as these things get more and more complicated, there's a lot of tests that have to run.</Q>

01:14:05 - Brandon Hancock
What are we talking about — unit tests? Are we talking about end-to-end UI tests?

01:14:10 - Jake Maymar
I would say more unit tests.

01:14:13 - Brandon Hancock
<A>I mean, so one thing that I always have in my task is that the very final step is always to run Lint and just very quick commands to verify that it works. Because yeah, that's the worst thing — when you're like, I built feature one, cool, it works. Feature two, cool, it works. Feature three, it works. Now let's go actually run tests. And you're like, oh my God, it broke. When did it break? You know, so you want fast feedback loops. ▶ So yeah, I see nothing wrong with just making sure whatever your task template is, at the very end run npm run lint, also run whatever you need for your unit tests. That way, just every time it cranks out a feature, you instantly get feedback. Instant feedback is the main way to set yourself up for success.</A>

---

<!--SEGMENT
topic: HIPAA-Compliant AI Infrastructure and Azure Costs
speakers: Jake Maymar, Andrew Nanton, Brandon Hancock, Juan Torres, Ola Oyo
keywords: HIPAA compliance, Azure, BAA, audit logging, Bedrock, Vercel, Flashlight, healthcare AI, PITR, cold storage, Datadog, AWS CloudWatch, cost estimation, virtual private cloud, Miramira
summary: Jake raises questions about HIPAA-compliant AI chatbot infrastructure and cost estimation. Andrew shares real-world experience running a HIPAA-compliant app on Azure, noting that audit logging is the dominant cost at ~$2,000/month. Brandon explains the difference between development logs and HIPAA audit logs and suggests cold storage as a cost optimization. Juan discusses self-managed logging on EC2 as an alternative.
-->

01:15:18 - Jake Maymar
Some really exciting stuff happening on the healthcare side. Talking with — we're moving forward with — nothing too exciting yet, but I definitely want to share once I have something.

01:15:46 - Jake Maymar
<Q>I guess the other question is the HIPAA compliance. I shared Aptable a while back, and I'm kind of curious — what kind of budgets, if anyone's running Azure, HIPAA compliant, an AI chatbot — what kind of budgets are reasonable? Because I was trying to figure out run costs, and it was kind of all over the place.</Q>

01:16:23 - Brandon Hancock
<A>So quick thing — Juan had that cool calculator thing that he shared last week. I would definitely check that out. But let's just think about it — core components. Most of the time, when you have your own secure instance of an app running that's in its own virtual private cloud, the core components — you're probably going to have at least one server running 24/7. You're also going to have to have a database. You're also most likely going to — HIPAA has all sorts of requirements on log tracing and everything else. So the main core components, probably $100 to $200 a month, if I had to guess. Maxim would be a great person to ask on this. He already has one running. But at the end of the day, you need a computer, you probably need a few for redundancy, just in case it goes down. So we'll just say two instances, and then a database. And that's kind of the basics. Yeah, probably $100 to $200 a month, is what I would guess. And then your AI calls, whatever, on top of that.</A>

01:17:39 - Jake Maymar
So $100 to $200, but then I keep getting these like $700 a month, $10,000 a month, if it's HIPAA compliant. That's the part I'm — I just don't want any surprises.

01:19:26 - Andrew Nanton
<A>So I mean, we're running on Azure [tool:Azure] HIPAA compliant. I'm doing that project with Maxim. And that means you have to route everything within Azure. And Azure gives you a BAA. The logging is bonkers expensive. That has been by far the most expensive part. A lot. And the rest of it is, it adds up, but it's not as crazy. It's the logging that is killing us.</A>

01:20:07 - Jake Maymar
<Q>How — can you give me a range on the logging?</Q>

01:20:14 - Andrew Nanton
<A>Yeah, like, like, 2000 bucks a month.</A>

01:20:30 - Andrew Nanton
And so right now we're running on that Microsoft free money, basically — it's like the Google thing. And so we got 25,000. And so it's all Bill Gates's credit card. So on some level, it's very abstract, but it just feels like it should not be anywhere near this expensive. And it is.

01:20:47 - Juan Torres
<Q>What do you mean by logging?</Q>

01:20:50 - Andrew Nanton
<A>Azure, or excuse me, HIPAA obviously requires you to be able to track down everything that happened — like who accessed what and when. And so the amount of logging that's going on in terms of user interactions and what documents they've interacted with takes a lot of logging, apparently.</A>

01:21:15 - Brandon Hancock
Yeah, I was going to guess like $500 max, like if you were like had a small to medium sized amount of traffic. But I also haven't done that. So I'm well — there may well be room for optimization.

00:26:01 - Brandon Hancock
The one core difference is most of the time when we think logs, think development logs, such as like, Brandon made this request. Here is a little bit of the information. So it's all development logs. That's layer one. What HIPAA wants is it's called an audit log, which is a level above that. So it's not just like Brandon made a request. It's like Brandon literally opened this page. Brandon saw this information. It's at an extreme level. So you can at any point go — I could literally from two months ago tell you exactly what Brandon was doing on our app at 12:30 p.m. It's a level above. So that's why you'll create gigabytes of logs per day. ▶ But even though it's gigabytes per day, Andrew — I would be very curious how the logs are being stored. There's different types of storage. There's cold storage. Like literally just by changing how you store data, you could save a ton of money because you're not accessing these audit logs every day. You might access them, honestly, whenever you get audited. So there might just have Maxim look to see if he could change the bucket to a different type of bucket to save money. Because that's a quick fix, and that could save a lot of money.

01:22:56 - Andrew Nanton
Yeah, anything that Microsoft hosts in Azure is covered under their BAA.

01:22:44 - Andrew Nanton
But the hard part is when it goes in and out of Azure, how secure is it and where is it going? And so stitching together Azure and models from Bedrock [tool:Amazon Bedrock] and like — oh, you're getting really, really complex. But if it all stays in the little Azure bubble, then yes, that's doable.

01:23:06 - Ola Oyo
<Q>Just a quick question to Andrew, and maybe Juan could also help out with this. So when you talk about logging, is this capturing all of the different events? And Juan, because how I do my logging is I basically put my logs within the code, and that determines how I want to see them. But on GCP, I don't see myself having to pay anything extra for the logs. So is it a different type of logging you're referring to, Andrew?</Q>

01:23:35 - Andrew Nanton
<A>It is, and I will claim ignorance here. This is part of what I've handed off to Maxim, because this is more his expertise than mine. He's in the process of an international move. And so hopefully when that's done, he'll be back on here.</A>

01:24:01 - Juan Torres
<A>In terms of my logging mechanism, I take complete control of the environment and I create my own logging mechanisms without using the on-premise because AWS [tool:AWS] also has a — what is it called — CloudWatch [tool:AWS CloudWatch] application. And so I just rather have control of the environment and create the logging for the test of the GPU stress testing or the LLM stress testing. So what you can do is just have control of the EC2 instance [tool:AWS EC2] in the permanent memory mechanism. And so through that, whatever Python code you're incurring, if you're going to have a mechanism there, you're going to have a folder in which you can see the logs of each test and then be able to observe what's the particular pinpoint in your agentic system.</A>

01:27:01 - Jake Maymar
The only other thing is the link. So that link is Thinking Machines. It's Miramira [tool:Miramira]. This is kind of interesting. It's open source. The idea behind this is — and I'm kind of curious — this is a question in general, because I thought we could do this. Where if you set the temperature to zero and you have the seed, you can actually get the exact same result. So this basically says you can do it with this open-source version, which is pretty cool. Miramira is from former OpenAI. [link:Thinking Machines / Miramira open-source deterministic LLM]

---

<!--SEGMENT
topic: Kris Larson Introduction and Personal Branding Strategy
speakers: Kris Larson, Brandon Hancock
keywords: Android development, TensorFlow, machine learning, personal branding, YouTube, content creation, real estate scraping, Playwright, Gemini CLI, MCP, SaaS idea, AI authority accelerator
summary: New member Kris Larson introduces himself as a laid-off Android developer exploring his next career move in AI. He shares a SaaS idea around scraping real estate listings to generate AI video walkthroughs. Brandon advises him to leverage his Android expertise combined with AI as a niche YouTube content strategy, citing a student in Japan who landed freelance projects within four months.
-->

01:27:55 - Brandon Hancock
Next up is Chris. What's going on, Chris?

01:28:00 - Kris Larson
Hey, so this is my first time on the show here. I'm not here for talk therapy, although I'll take what I can get. Just a brief thing of my story. I've been a developer for like way too long. The last 10 years that I was working, I was actually doing Android development [tool:Android development]. And I got laid off in March, so what I've been telling people is I've been involuntarily retired.

01:29:07 - Kris Larson
There was a little bit of machine learning that we did with that project. We did actually train a recognition model. I actually put a TensorFlow [tool:TensorFlow] model into an Android app and had it doing inference right in the app. So that was kind of my first taste of this whole machine learning, artificial intelligence thing. And so I'm here looking for my next act, I guess is what I want to say.

01:29:37 - Kris Larson
Brandon, I was watching some of your videos, but it was when I saw the personal branding video. That was the one that really spoke to me.

01:30:05 - Kris Larson
So I haven't done a whole lot of Python. I haven't done a whole lot of AI. I have actually very few of the particular skills you need to do this. But what I am good with is just figuring stuff out. So I'm trying to just start — everybody says, just start, just do something. So I was trying to come up with some kind of SaaS idea. And I think there's a service for this already, but one thing that occurred to me is like if you had, for example, on a real estate website where you have the description of the property, have some pictures of the property, and being able to scrape all that and then be able to generate a video — you could take the pictures, you could turn them into some kind of animated walkthroughs. You could obviously have the voiceovers, you had music. So I can see the stuff is doable.

01:31:24 - Kris Larson
So far I did get Playwright [tool:Playwright] working with MCP [tool:MCP] and just in Gemini CLI [tool:Gemini CLI] here. And I got it to do basically what I needed it to do — just the pieces. So now it's like, okay, now I've just got to figure out how I run Playwright Headless in the cloud. How do I get an agent in the cloud to talk to this thing? And then that's just grabbing all the data. And then I have to figure out all the video stuff.

01:32:24 - Brandon Hancock
What I would love to quickly do is like an AI Authority Accelerator crash course — give you just a few quick high-level things based off what you've said so far, how you can apply it. So long story short, we need to pick something that you get known for in the world. So I know you said Android background — I mean, there's still plenty of Android. Android is still as relevant today as it was two years ago, if anything more. Can be applied now because now it's Android plus AI development. So if I was you and I was to pick — I have to get a new job within the next six to eight months — what I would do, obviously YouTube [tool:YouTube] is my favorite avenue, but I would literally just make small short tutorials on YouTube teaching people AI development plus Android applications.

01:33:28 - Brandon Hancock
What's sick about this is, like, you don't have to do huge monolithic projects that take two months to build. Because if no one is interested, then your feedback loop is two months. It takes two months to figure out if what you're putting out into the world is valuable or not, which we need to turn that to a week. So what I would like to do is just every week, obviously this is YouTube, you can do it on LinkedIn, it doesn't really matter which one — but basically the core idea is every week, I'm going to produce a valuable insert blank that is teaching people about Android plus AI development.

01:33:55 - Brandon Hancock
And that's what I would do. You already have an unfair advantage in the space — you have tons of experience. You're already probably in the top 5% of all Android developers. So now just by throwing AI on top of that — how many are very experienced Android developers plus can integrate with different AI tools? ▶ So now you're in the top 1%. By combining Android with AI, you've cut your skill deficit in half.

01:34:35 - Brandon Hancock
Your competition — maybe four people. Okay, can you outcompete four people? Yeah, of course. The starting part is going to be the hardest thing.

01:35:09 - Brandon Hancock
One of my students literally lives in Japan. He's worked at a huge company forever. And he was very scared to get on camera. And I was like, dude, literally just make videos, talk about big AI technology. Talk about ADK, talk about things, just make tutorials. ▶ Literally within four months, he is now getting freelance projects like 13, 15K to build stuff. So it's just like, you just have to trust the process for three to four months for AI plus YouTube to show the world what you can do. And good things happen.

01:36:24 - Brandon Hancock
Here's our public accountability challenge. Obviously it is Tuesday. I think what would be a very cool challenge is by Tuesday next week — this is what I have everyone do in the program — is I have them make their very first YouTube video. And all they do for their first YouTube video, just to start, is they say, hey, guys, my name is Chris. On this channel, I'm going to teach you everything you need to know about Android and AI development. And you can expect to see tutorials on ABC. So definitely hit like and subscribe so you can see all my future content and I'll see you in the next video — just to start. Because you have to just get that weird one out. ▶ That would be my public challenge — a simple, hey, welcome to my channel, YouTube video.

01:37:19 - Kris Larson
All right, that sounds awesome.

---

<!--SEGMENT
topic: Elijah's Ed-Tech Background and ShipKit Plans
speakers: Elijah, Brandon Hancock
keywords: ed-tech, paper grading, vibe coding, ShipKit, AI Authority Accelerator, software on demand, Sam Altman, Super Whisper, Whisper Flow, Claude Code, project management
summary: New member Elijah shares his background founding and selling an ed-tech paper grading company in 2015, and describes how AI has compressed months of development work into weeks. He asks about the AI Authority Accelerator program. Brandon explains the program timeline and reinforces ShipKit's goal of providing reusable AI application archetypes.
-->

01:37:40 - Brandon Hancock
Elijah, I saw you had your hand up, buddy.

01:37:43 - Elijah
Hello, hello. I've had the opportunity to see some of your stuff over the past few months. I was really searching for more of a project management type function inside of Claude Code [tool:Claude Code]. And so that's how I discovered some of your more recent stuff with ShipKit. And pretty excited about it. Looking forward to that coming out.

01:38:13 - Elijah
I've been binging over the past month pretty hard, vibe coding. I built an application that I'm working on, but it's more just for me to build my skills up. I'm in the ed-tech space. I had a company back in 2010. I was a teacher and I developed a software with a team. I wasn't a programmer, but I built a team and raised some money. And we built a paper grading solution and sold that in 2015. And then took a couple of years to integrate the technology into the parent company. And what took me a couple years to do, I've done in like the past month. So I mean, it's just unbelievable. And then when you see a bug, right? You're like, okay, we got to fix this. And then it just fixes it. I'm like, I didn't have to communicate to somebody. I mean, it's mind blowing.

01:39:16 - Elijah
And then I discovered your — when I bought ShipKit, I got into the community. So thank you for putting that in there. One of the things you mentioned was the AI Authority Accelerator. And I've been working on my school process to get people into my school community related to education and ed-tech. But I don't know if there's anything additional that you have, or this is kind of like just go through that other course, wait for ShipKit, and then just show up to these calls. Is that the best plan forward?

01:40:04 - Brandon Hancock
<A>Yeah, so there's a few different moving parts. So ShipKit, AI Developer Accelerator, which we're in right now, and then I had the AI Authority Accelerator, which was teaching people how to launch a YouTube channel, either build their own school, do freelancing opportunities. So the AI Authority Accelerator, I will most likely be looking at doing probably at the very end of the year again, or at the very beginning of the new year, just because it was so much work. A lot of people — like I said, one of the guys, literally from Japan, that was the coolest thing ever. He did it, he's crushing it, making money. And just it's an insane amount of dedicated work. So I'm probably going to wait until maybe early next year, because I really want to focus on ShipKit for the next year — just add a ton of projects continually in there for you guys. So it will happen again. It's just I need to focus on ShipKit for the foreseeable future.</A>

01:41:21 - Elijah
I read your FAQ there and it appears that with ShipKit, your goal is for people to be able to kind of jump off of that into their own SaaS applications to make money from them as well.

01:41:39 - Brandon Hancock
Literally the whole goal. Yes.

01:41:44 - Elijah
So I said, don't you think we're going to get to a place with software as this — software on demand? I think it's how Sam Altman [tool:Sam Altman] said it. He said we're entering into this new world where it's software on demand. And I know there's open source, which is effectively what you're doing, right? Because you're kind of like putting it out there and then letting people use that and then build upon it. I think that's what the future of software is going to be like, because so many people are going to be able to create.

01:43:14 - Brandon Hancock
Totally — the whole premise, literally you just nailed it, Elijah — is like going forward, AI, like building software is going to become easier than ever. It's that starting point which is the hardest part. So what I mean by that is, yeah, anyone can spin up a beautiful landing page in a simple CRUD application. But doing anything beyond that, it is not possible with today's tools. ▶ Like literally the whole goal of ShipKit is like, hey, I will go spend the months building out the core archetypes of projects. And then you guys get to just take my homework and implement your own app. So like I'm pumped — one of them, a LangChain app, another one — I want to do a Whisper [tool:Whisper]. I don't know if you guys have seen Whisper Flow [tool:Whisper Flow], but like all the core types of AI projects that exist, build out the boilerplate. So that way you guys just go off and dominate.

01:44:25 - Elijah
I'm using Super Whisper [tool:Super Whisper]. I evaluated them and I'm using that instead of Whisper Flow. I was using Whisper Flow, but Super Whisper, at least on the Mac, has been really good.

---

<!--SEGMENT
topic: Hemal Shah's Back-Office App Authentication and ADK Issues
speakers: Hemal Shah, Brandon Hancock, Morgan Cook
keywords: Supabase, NextAuth, authentication, invite-only, back-office automation, ADK, Agent Engine, streaming, Vercel AI SDK, Google Cloud, production deployment, data reconciliation
summary: Hemal asks how to add invite-only authentication to his back-office automation web app. Brandon recommends disabling public sign-up and using Supabase's invite user functionality, or NextAuth as an alternative. Hemal also raises a key ADK limitation: the local API server and deployed Agent Engine use different URL patterns and payloads, making environment switching painful.
-->

01:44:55 - Brandon Hancock
Hemal, you're up next, buddy.

01:45:04 - Hemal Shah
So for my back-office automation project, taking now to thinking more about the production level. So local testing and everything is good. So that's where the Vercel and ADK deployment — I did it last week. And I was wondering now, how do I protect the web app — like username, password, or certain ways — so that it puts some authentication in front of it. So if there's a recommendation on standard username, password, or something to protect our web applications.

01:45:47 - Brandon Hancock
<A>So wait — the question's on the web app, how do we keep it secure? So it is a private application. So one option that works really well — I actually had to do this for a client project. You can set up an invite. Basically, you can invite — so let me pull up something real fast on Supabase. Because you're using Supabase or no, you went with a different platform?</A>

01:46:42 - Hemal Shah
I'm using — so I'm not using a database yet. It is mostly kind of an agentic solution, just getting some files in the file comparison, data reconciliation.

01:46:57 - Brandon Hancock
<A>Inside of Supabase, you can pick how — what are the different ways you want people to log in? What are the different sign-in policies? Obviously email — that's just a known. However, the main thing that you change is you actually get rid of the sign-up page. Like you just do not allow people to sign up for your application. Instead, what you do is you build out the invite user functionality. So basically if people can't sign up, then there's no way that they can join your application. So that's just a very quick workaround — you basically just have to work on the invite user workflow in whichever authentication provider you're using. And that's the quickest workaround to make sure that your application doesn't accidentally, even if it did get shared to the world, people can never join. So it's invite only. ▶ That's how, in the simple way — just drop the sign-in form.</A>

01:49:47 - Hemal Shah
<Q>So the authentication setup that you mentioned — is that something out-of-box, open-source libraries? I mean, we can do it ourselves. I can create my own authenticator and comparison and password hashing and everything. I was just wondering if there's open-source, third-party, popular with Next.js, which we can just drop in, have some UI, put some middleware. There's one library — next...</Q>

01:49:51 - Brandon Hancock
Is it NextAuth [tool:NextAuth]?

01:49:52 - Morgan Cook
I think you can use NextAuth. I've used them plenty of times.

01:49:56 - Brandon Hancock
▶ That's a great one. If you just want to not have to worry about Supabase and other auth providers, yeah, NextAuth would be a really great one.

01:50:16 - Hemal Shah
And one more observation, Brandon — with ADK server, when we deploy it in Agent Engine, it has a different URL, like a stream query, something, and then the payload is a class method. But when I'm locally doing ADK API server, it is run SSE, and it is a different URL, different payload. I'm wondering — so that's a limitation right now, correct? So the client, if I want to test a local agent, then I have to have a different setup.

01:50:49 - Brandon Hancock
This was my biggest complaint. I was like, this is disgusting. You're making every single user who wants to play and use ADK to have to build out custom dynamic routing between production and dev. And every single person has to solve the same problem. Like this is awful the way that it's been set up. ▶ So the goal — my recommendation — it'll be cool if they do it — it should be like Vercel AI SDK, where I literally just install it, and then I send a request to that hook, and then it does all the routing. Like that's what it should be.

01:51:33 - Brandon Hancock
And fingers crossed, they'll do that. Because right now, yeah, you're totally right. And then one other thing — streaming is still broken. So if you want to do it, you have to handle stuff synchronously. ▶ The cheat code is we can actually go even simpler than I did in that YouTube video, where you do server-side, you do stream query when you're working with Agent Engine, but you just wait for it to send all the information, then you just send it back as a synchronous method.

01:52:23 - Hemal Shah
Also, I think the API documentation — that is not that rich. I mean, the tutorials are great, but the stream query, different parameters, combination — they have some write-up, I went through it, but it's not full-fledged REST API documentation.

01:52:52 - Brandon Hancock
No, dude, I could go on and on. Half of their docs are pointing to endpoint V1 beta, but then the thing that Agent Engine gives you is V1, so the docs don't match the endpoint. Like, there's so many things that are not synced up, and I think they're just moving fast, but they're moving a little too fast. It makes it hard to understand.

---

<!--SEGMENT
topic: Alex Wilson RAG Portfolio App and Supabase vs Neon Decision
speakers: Alex Wilson, Brandon Hancock
keywords: RAG application, portfolio builder, Supabase, Neon, Stripe, authentication, Google Cloud Run Jobs, vector store, blob store, PITR, point-in-time recovery, Cursor, allow list, npm run dev
summary: Alex shares a RAG-based portfolio builder app he built in four to five days. Brandon announces a significant RAG architecture update using Google Cloud Run Jobs instead of Cloud Run instances. The discussion covers Supabase vs Neon for multi-project development, Supabase's all-in-one value proposition (auth, Postgres, vector store, blob store), and how to prevent Cursor from auto-running destructive commands via the allow list setting.
-->

01:53:30 - Brandon Hancock
Next up is Alex. What we got going on, Alex? Anything fun?

01:53:37 - Alex Wilson
Still on the job hunt, but I did spin up a RAG application. I wanted to build a portfolio builder because I don't have a portfolio. And since I was in risk and security for the bank I worked at, I don't have anything to share from that other than saying, yeah, I did some really cool stuff there.

01:54:04 - Brandon Hancock
Quick feedback on the RAG application. Actually, the reason why I had to push stuff back for ShipKit — I have completely done it to where it's 10 times better now. So the old application used to do Google Cloud instances, run instances, and now we use Google Cloud Run Jobs [tool:Google Cloud Run Jobs]. So what's nice is now whenever you pass in a document, it spins up its own instance to work on that one document. In the past, it had one computer that would kind of just sit there and pull. So it actually overcomplicated it. The new version works so much better.

01:55:05 - Brandon Hancock
But yeah, so you're working on building out a portfolio. Is that the main thing, right?

01:55:10 - Alex Wilson
I'm building an app that actually you can drop in resumes and LinkedIn links and whatnot. It takes all that information and helps you and actually builds a portfolio. It's actually working right now. I did it over the past four or five days. And it's working. The biggest struggle was the Stripe [tool:Stripe] and the authentication and whatnot. And I'm only doing it to kind of show proof of concept. Right now, building up my portfolio and whatnot. So I don't know if that stuff is necessary, and I'm not sure how to cut it out.

01:56:01 - Brandon Hancock
Yeah, there will be a RAG Simple that doesn't have any of that. RAG SaaS has it, RAG Simple doesn't.

01:56:54 - Brandon Hancock
You know, absolutely love the portfolio approach. I think that's so cool that you're getting to try out and build. ▶ The one thing I would say — post on social media. I don't know if we're connected on social media or not on LinkedIn, but seriously, post, post, post, post, just so people know what you're working on. Even if it's just like, hey, cool lesson learned today, just nuggets of knowledge. That's the best way. So instead of like, hey, look at me, look at me — it's, hey, you might find this interesting. And just be more of a value add. It'll go much further.

01:57:41 - Alex Wilson
<Q>Are you using primarily Supabase just because of the authentication? And the reason I ask is Supabase — the free tier only has two projects. So if you're building stuff, you run out really quick. So I've done some of the other stuff I've built — I've migrated over to Neon [tool:Neon] because you can have the 10 projects at Neon, or maybe 20 now.</Q>

01:58:07 - Brandon Hancock
<A>So the main reason why I picked Supabase is it's an all-in-one solution. So the simplicity you get out of it is great, meaning we can use Supabase for authentication. We also get it for a Postgres database. Beautiful — it's a Postgres database. So we can also use it as a vector store [tool:vector store]. And then the third one is we can use it as a blob store. So anytime we want to upload images, documents, anything like that, it's all in one place. Because in the past, I have found this painful developing. It's like, okay, I'm going to hop over to Neon to look at my database. I'm going to hop over to Clerk [tool:Clerk] for auth. I'm going to hop over to Uploadthing or AWS or Google Cloud for blob. And then for like — I'm going to hop over to Pinecone [tool:Pinecone] for a vector store. I was in six apps. And I was like, man, I just want to — because eventually, once your app grows, you're going to not only have to pay on one platform, you got to pay on five. So it actually ends up costing less. The gotcha is, they all give that free tier. And then the second it's not free, you're paying 20 bucks times five, rather than just 20 for everything.</A>

01:59:20 - Alex Wilson
<Q>So would you recommend just doing the Supabase $25 a month plan?</Q>

01:59:27 - Brandon Hancock
<A>Yeah, I mean, that's what I use. And it's crazy that you can host for — just saying this out loud — for $25 a month, you get a full-blown authentication service, database, Postgres — you get everything for 25 bucks. And I think you get up to 10 projects, or five or 10 at the tier. So like, you could literally host five really big projects in there on the $25 a month plan. So it's really worth it. The gotcha — just so you guys know — there's a thing called PITR, which is point-in-time recovery [tool:PITR]. So if you want your database as you go to scale, and you have a ton of data and you're worried people can break it or something like that, it's $100 a month for Supabase. It doesn't matter what platform you're on — it's always an insane amount of money for point-in-time recovery. But Supabase does have daily backups, and those are included. But point-in-time, they will charge you for it.</A>

02:00:42 - Alex Wilson
<Q>One other question — earlier you were showing — I had that problem with the npm run dev. Where was that that you can set that?</Q>

02:00:52 - Brandon Hancock
<A>I still have it up. So in settings, in Cursor [tool:Cursor] settings — so I hit the top button, then go to chat, and then I changed my auto run mode to whitelist, to use allow list, sorry. And this is where I say, like, you can run these specific commands. So like, I don't mind when it runs Lint. I don't mind when it runs some of these other things. It's just, I don't want it to run npm run dev. Like, don't do that. So I just hit deny is the main thing. ▶ I would check out the allow list just to have it not accidentally spin something up.</A>

---

<!--SEGMENT
topic: Adam's Presentation Idea, TypeShare Model, and AI for Local Businesses
speakers: Adam, Brandon Hancock, Andrew Nanton
keywords: TypeShare, influencer partnership, revenue share, AI presentation, local businesses, OpenRouter, LiteLLM, model comparison, ChatGPT, Claude, GPT-5, creativity test, umbrella alternative uses, Nano Banana, Whisper Flow
summary: Adam shares a partnership arrangement where he helps someone with their SaaS in exchange for social media marketing. He pitches a presentation idea comparing human vs. AI creativity using an alternative-uses task. Brandon shares a past "AI for Local Businesses" presentation deck and recommends OpenRouter plus LiteLLM for multi-model comparison. Andrew asks about the audience to ensure relevance.
-->

01:59:59 - Brandon Hancock
Adam, then Morgan, then Patrick.

02:01:59 - Adam
So I don't know if I mentioned this in a previous meeting, but yeah, I just don't think I have any aptitude for YouTube, social media and stuff. So I've worked out an agreement with someone that says they'll do it for me and I'm helping them with their SaaS platform. So I've been kind of going through and debugging that.

02:02:20 - Brandon Hancock
So would you mind sharing a little bit more?

02:02:27 - Adam
We haven't put anything in writing, but well, I guess we have because we're doing emails back and forth. But the details aren't really worked out. I'm just like, hey, I'll help you with your SaaS. Hey, I'll do some social media marketing for me.

02:02:41 - Brandon Hancock
No, that's awesome. Quick thing that I've seen that has worked really well — so there is a company called TypeShare [tool:TypeShare], and the creator of it literally is not a big social media guy at all, but he built an app and then partnered with influencers. So Sam Shore, the creator — he's like, I will build the app, and basically I partner with creators who really like the platform. So they drive all the traffic, they get a revenue cut, but that way they both win, because they both do their strengths. Marketing guys market, developer guys develop. ▶ And so if there's any influencers, you could always just go into an agreement of like, hey, I will literally build this for you. You just market it. Here's what marketing looks like. And you get a cut. I get a cut. We both win. We both get to play to our strengths.

02:04:28 - Adam
So I am working on this — I'm supposed to do this presentation on AI. And this is the — well, I actually stole someone else's idea. But what I think I'm going to do is make a little web page. And I think it was a university research project. So you get like five minutes and you have to think of as many alternative uses for an umbrella as you can think of. And then at the end of that five minutes, I'm just going to generate a report that will compare people's answers — what's the mean, median — and then compare that to what did Claude do? What did GPT-5 [tool:GPT-5] give? Kind of thing.

02:05:15 - Brandon Hancock
Okay, so it's like a model comparison, is what you're saying?

02:05:20 - Adam
Well, you compare the humans to the humans, the models to the models, and then the models to the humans.

02:05:27 - Brandon Hancock
Oh, okay. That's a pretty cool idea. And that's for your presentation?

02:06:07 - Brandon Hancock
Kind of like Andrew talking about LiteLLM earlier — the simplest way to do model vs. model — I would use OpenRouter [tool:OpenRouter], and OpenRouter is where you could obviously buy one key to work with all the platforms, and then LiteLLM to basically work with all models. So you get one key, one tool, and boom, you're chatting with every model provider. ▶ So it's a really quick, cool way to not have to solve working with a thousand libraries. So I would definitely recommend that.

02:06:25 - Andrew Nanton
<Q>Oh, so I was just asking who the audience is. And I mean, I think this is a cool idea that you have, but I also think we might have some more useful feedback knowing who the group is and what they might intend to get out of it, because I think that's always the hard part — keeping people's attention if you're not telling them stuff that they care about.</Q>

02:06:50 - Adam
So I was supposed to meet with the group earlier this month, but unfortunately the organizer was sick, so not meeting with them till not this coming Wednesday, but the Wednesday after. So I don't quite know what they are, but I think it's just like a bunch of local businesses, so not real technical people.

02:07:27 - Brandon Hancock
I have a presentation if you want to steal it. Let me find it really fast. I did this back in June, and it's literally called AI for Local Businesses. [link:AI for Local Businesses presentation - shared in chat]

02:08:15 - Brandon Hancock
Long story short — always start off a conversation of like why they should listen to you, how you've implemented AI, and then basically break it down into like, also by the end of this conversation, I'm going to show you five awesome tools that you could use in your business, literally after walking out of today's call. And then that way they clearly know what they're going to get out of the presentation. And then at this point, like, I tell them what AI assistants to use, which one's best to use under different circumstances. You know, everything from image generation — this has obviously changed, like Nano Banana [tool:Nano Banana] is phenomenal. ▶ I would 100% steal this. And the main thing is, just assume they know nothing. So the more just actionable things that they could literally sign up with after walking out, the better. Like the fact that Whisper Flow [tool:Whisper Flow] — the fact that we talk to our computers — it breaks their brain. Like doing that on stage and then just going like, holy shit, I've been typing. I could just talk, you know?

---

<!--SEGMENT
topic: Morgan Cook's Refactoring, Carpool App, and Electrical Panel RAG Idea
speakers: Morgan Cook, Brandon Hancock
keywords: Clerk, Supabase Auth, NextAuth, Tailwind 4, Next.js 15, TypeScript, Context7 MCP, ShipKit templates, gitignore, carpool app, RAG chatbot, electrical panel, N8N MCP, Network Chuck, Ollama, local models, MCP server business model
summary: Morgan shares a productive week refactoring from Clerk to Supabase Auth and resolving a Tailwind 4 gradient text issue using Context7 MCP. He raises a practical concern about gitignore conflicting with ShipKit template files in IDEs. He also pitches a creative RAG SaaS idea: a QR-code-linked chatbot that answers questions about electrical panel breaker assignments for homes and businesses.
-->

02:10:15 - Brandon Hancock
Next up is Morgan, then Patrick.

02:10:20 - Morgan Cook
Sorry about that. I did some refactoring — refactored out to Clerk [tool:Clerk] and switched to Supabase Auth [tool:Supabase Auth]. That's awesome. That's a good coding week.

02:10:37 - Morgan Cook
And I ran into a couple of problems. And for me, the problem is — I've been developing for freaking decades, but some of the new technologies that I'm not familiar with — when you have a problem in that technology, man, is it a problem because you don't know where to go find — you don't have the experience with it to know what the normal problems are. So I had some problems with TypeScript [tool:TypeScript] and Tailwind [tool:Tailwind] last week that interfered with some of my UI. And I thought, you know what, I'm going to spend whatever time it takes to get this thing figured out. And I did. And thanks to using Context7 [tool:Context7] as my MCP and a few other things that helped me with rubber ducking with the AI to get the thing correct.

02:11:22 - Brandon Hancock
<Q>What the issue was? Like a quick recap of what that problem was?</Q>

02:11:25 - Morgan Cook
<A>I was doing a gradient text thing, but it was based — the model I found was based on an older version of Tailwind. And the newer version changed how they do their app themes. And basically, after I got done refactoring it all, I didn't need Tailwind at all. It was just a straight app theme added into the global CSS.</A>

02:11:47 - Brandon Hancock
No, that's awesome. Yeah, Tailwind and Next.js have been in a battle — if you had to use 3 for a while, if you went to 4, 4 broke, so everyone went back to like version 3. So I don't know, 3 has been insanely stable, so I've been sticking to that one at this point.

02:12:05 - Morgan Cook
Right now I'm using Next.js [tool:Next.js], the latest 15, I think it is, and Tailwind 4 [tool:Tailwind 4]. There's just a couple of problems every once in a while that I run into. But I'm getting there.

02:12:29 - Brandon Hancock
Hey, that's the best way to get smart, man. But no, it's — the worst part about Tailwind, it's getting it set up. The second it's set up, it's like, oh, this is nice. This is super helpful.

02:12:40 - Morgan Cook
You know what, Tailwind 4 is easier to set up now than the previous version was. You don't have to do as much to set it up and then get it included. You just include one statement in the global CSS and it pulls in pretty good.

02:13:00 - Morgan Cook
I mentioned previously about the carpool app or curbside. That's going to still be going. I've been playing around with ShipKit, generating functions for that a little bit to see how it's going to map it out.

02:13:30 - Brandon Hancock
Quick side note on that — the way it works the best is inside of an existing Next.js, Supabase, and Tailwind project. Like the docs were designed to live in a project. So I just want to call that out just because like one guy used the templates and he's like, it's not working. And he was using LangChain and like six other things. And I was like — okay, that's on me. I should have made it more clear. It won't just solve every problem ever. ▶ That's the point of specific task documents — they thrive in a specific environment.

02:14:02 - Morgan Cook
Yeah, no, and that's the framework that I'm using. The other question I had, though, on that is — we put all that in our project within, like, the AI docs. What is your — I haven't seen any kind of guidance or policy on how you want that as far as gitignore for checking into a public repository or private repository, et cetera.

02:14:25 - Brandon Hancock
Yeah, so I mean, the goal is to — obviously, like, you know, it is purchased content. So like, ideally, everything is private, just so it's not like — there is a license on the thing when you actually get ShipKit, like the actual code, not just the templates. Like the license is — you can do whatever you want with it, but just don't publicly share the source code. It's basically the agreement. But build your own apps with it? Hey, go for it. Knock yourself out.

02:15:03 - Morgan Cook
One of the problems I had was I had originally added it to the gitignore. I'm using Windsurf [tool:Windsurf], and maybe this is a problem with Windsurf. But the gitignore then ignored the directory for any of the commands that were being issued. So it would create a problem. I don't want it in my project for the sake of committing to GitHub, but I need it in my project for the sake of the tool to actually run. But it's trying to honor the gitignore.

02:16:29 - Brandon Hancock
Right. Yeah, I can look into that. Yeah, I have — like I said, everything I've done is private, so I haven't even — I know the problem. I can look into that as well. But thank you for letting me know.

02:16:40 - Morgan Cook
All right, and for the other guys — one of the things I keep coming up with — I got like 20 projects right now that I would like to work on, but don't have time. So last week, because I do other work besides programming — I also do some construction work and electrician work. And one of the things I always do is put a little QR code inside the panel box for the electrical panel, which points to a document that lists exactly everything in the breakers, right? And last week I was doing that for a house that has three different electrical panels and probably almost like 60 breakers, right? And so it's like, okay, I'm in this room. How do I identify which outlet goes to where? So I actually have a spreadsheet of all that. I thought, I can talk to this document if I throw it in the context of ChatGPT or something, right? So I threw it in there and started talking. Like, show me all the breakers that are controlling the cameras. Show me all the breakers that are controlling all the electric toilets, all the stuff, right? This thing is huge. This house was huge. And it was really cool.

02:17:50 - Morgan Cook
So now I want to do a project with that. Instead of just having a QR code that goes to my spreadsheet that lists out the breakers, I want them to go to a RAG SaaS kind of chatbot that allows them to just ask the question — you know, what breaker controls my kitchen dishwasher?

02:18:07 - Brandon Hancock
I know the exact — that is so helpful because like normally I'm like, did that do it? No, oh, they're on the Wi-Fi. Did that do it? No, they're just on the fridge. Like, and I just have to test six things until it finally gets the right thing.

02:18:26 - Morgan Cook
And so that's great for a house, but even more important for a huge business that has massive panels, right? They have all kinds of things. And usually those are all pretty dedicated, but finding it — and when you have multiple panels that are in different locations — so it's difficult sometimes to find the right path. So that's one of the little projects that I came up with last week to pump through your ShipKit. We'll see how that goes.

02:18:43 - Brandon Hancock
No, I love that. That's especially for big business. ▶ Solve big business problems. That's where you get paid. That's fun. It's fun at the house, but it's profitable in the business.

02:19:32 - Morgan Cook
One more point — just something that I posted in the chat earlier in the conversation. There was a conversation about N8N and MCP. And I don't know if you guys know who Network Chuck [tool:Network Chuck] is, but he did two videos last week on those two technologies, merging them together, and actually building your own little MCP server at like five minutes to get this thing up and running to do anything. It really shows the power of how those two technologies are going to really work tightly together going forward. So I would encourage you guys to take a few minutes and look at those two videos. [link:Network Chuck N8N + MCP videos - shared in chat]

02:20:23 - Brandon Hancock
I think it's going to be such a business model. It's like back in the day, people — like literally Grammarly [tool:Grammarly] is like a billion-dollar Chrome extension, you know? ▶ I think the next wave is going to be like paid MCP servers — just something that basically just helps allow agents to do something that they normally can't. I think that's going to be a very huge business at some point.

02:20:58 - Morgan Cook
I was looking at it because I need to — one of the projects needs to be in-house. It can't be across the network. So I wanted to have both that, the — not OpenRouter — Ollama [tool:Ollama], all working within one ecosystem that is isolated from the network.

02:21:36 - Brandon Hancock
Let me know how that goes. Like I said, I haven't got to play with any local models in a while, just been doing mostly cloud stuff. So please keep me posted on how that goes on your experience. I think maybe Juan was playing with some local network models. He was playing with some that I think you could run on your local computer.

02:21:50 - Morgan Cook
He might be. I got a couple of them running under Ollama [tool:Ollama], and they're not fast on my little machine, but you put it on a dedicated server and they're going to be fine.

---

<!--SEGMENT
topic: Patrick Chouinard's Git Workflow Automation and Conversation Manager
speakers: Patrick Chouinard, Brandon Hancock, Jake Maymar
keywords: vibe coding, Git workflow, pull requests, commit messages, branching, AI-assisted onboarding, conversation manager, context distillation, model routing, intent detection, ChatGPT, nano model, E-Myth, AWS Skill Builder, gamification, ShipKit
summary: Patrick shares two projects: a Git workflow automation system using AI-guided markdown checklists to help non-developers follow proper version control practices, and a conversation manager architecture that uses a small model to handle context distillation and routing rather than sending raw context to a large model. Brandon connects both to the E-Myth concept of building systems that deliver results regardless of operator skill level.
-->

02:22:02 - Brandon Hancock
Last but not least, Patrick, what's going on, man? Anything fun?

02:22:07 - Patrick Chouinard
Hey. As some of you know, I've been asked to help the company to integrate vibe coding into their habit. And fun, but I realized one thing is that when you throw a bunch of non-developers into a development environment, it's not too hard when you have some very good technical people to show them how to create a decent level of application. What's really hard to teach them is all of the administrative side of development, if you want. By that, I'm talking about doing commit messages that are more than "initial load," stuff like doing some decent PRs, and that's been basically hell in the beginning because they have no clue what that means and what it's used for.

02:23:14 - Patrick Chouinard
So basically, what I ended up doing is starting to make — I don't know how to call it — a version of ShipKit, but specifically for that part. So all the templates are for commit messages, PRs, branching, all of those, and an actual workflow that they can use in a markdown document with checkboxes. So basically, the flow will know — have you created an issue, have you created your PR, what's going to be in your commit document, what is going to be in your changelog — to make sure that the system knows for them what they need to fill based on the information they've vibe-coded so far.

02:23:51 - Brandon Hancock
Hey, I mean, dude, you're — yeah, that's the ShipKit cool. I can't remember if we talked about this the other week, but the book E-Myth [tool:E-Myth] is literally what all of us are about to do to help everyone else out. What I mean by that is — E-Myth, it's all about building the system that delivers the results. ▶ So that's exactly what Patrick's doing through prompting. He's building the Git system so that literally anyone, as long as they probably graduated high school, gets the desired outcome, which is crazy. So that's like the core — that is what all of us are going to be doing very soon through prompting, through AI development — allow anyone to get the desired outcome that they want. And we build the systems that help them get that.

02:24:42 - Patrick Chouinard
Well, it's the thing — everybody can get really quickly how to give intent to create software. That's not the hard part. But tell them why do they need to do a pull request? Why do they need to create a branch? Why do they need to merge? It's not instinctive as it is to say, build me a system that does X. So basically, I'm trying to leverage AI to accompany people, hold them by the hand until they know how to do those things, and obviously try to build in some best practices in there as well so they learn from good practice.

02:25:26 - Patrick Chouinard
The other thing I've been working on very quickly — I've been asked to help one of our internal dev team basically to create a conversation manager. So I had no clue what a conversation manager was a week ago, and I've started to chat with ChatGPT on my way to work and on my way back from work as I do every day. And honestly, it felt exactly like I was in the Matrix when they say, hey, now I know Kung Fu.

02:26:07 - Brandon Hancock
<Q>So when you say conversation manager, like a conversation between a human and AI, is that what?</Q>

02:26:13 - Patrick Chouinard
<A>No, no, no. What I mean is, you know, when you create a chatbot and you talk with a model, well, talking with the model itself is not being a chatbot. It's the very raw communication and just resending the whole context every time. Very extremely basic. And it gets overwhelmed really quickly. The real conversation manager is having a nano or a mini model actually do all of the workflow and all the distillation of the context and all of that stuff that's never going to get discussed. And everybody says, why am I talking to GPT? And it sounds dumb compared to the one from ChatGPT, because you're not talking with the model — you're talking with the raw API.</A>

02:26:58 - Brandon Hancock
Yeah, that's awesome. There are levels to AI that people genuinely, when you peek behind the curtain, you're like, oh my god, I thought it was just this. No, it's going everywhere, you know?

02:27:14 - Patrick Chouinard
Model routers, system prompt decision on the fly, intent generation — figuring out the intent of the user to choose the right model, the right effort, the right verbosity.

02:27:31 - Brandon Hancock
There's a thousand decisions, yeah.

02:27:33 - Brandon Hancock
Jake, sorry, I got sidetracked.

02:27:38 - Jake Maymar
I love this conversation. Patrick, I'm sure you played the AWS game, right? Like the — do you know which one it is, Brandon? The AWS game where it runs you through all of AWS. If you haven't played that, let me just find it really quick. It's an RPG where you actually like walk around and solve things. Is it this one? AWS Skill Builder [tool:AWS Skill Builder] — is this it? [link:AWS Skill Builder gamified learning platform]

02:28:43 - Jake Maymar
<Q>My question is, would it make sense to give them a game where they could basically do all these things where they can't break it? Like a sandbox environment? So you're going to build this application. And you're going to do commit messages, you're going to do a pull request, you're going to do all these different things, you're going to do a code review — but it's on rails, and it's gamified a little bit, and at the end you get this end result, but through the process it teaches you sort of why you do these steps and sort of how you get to the end.</Q>

02:29:20 - Patrick Chouinard
<A>It's a very good idea when you're dealing with people who are trying to learn development. The thing is, I'm working with people who just want the application, so I need to make sure that they do respect that without being interested in learning how to code. So that's what the AI and the workflow and all of the documentation I created is there to hold them by the hand, so they don't have to learn it, they just have to answer a bunch of questions, and it does the work.</A>

02:29:56 - Brandon Hancock
I mean, that's the cool part — it's like they shouldn't even have to know what Git is if Patrick's stuff works properly. It just — yeah, my stuff saved somewhere, you know, like that's the crazy part. Like they just care about the end result. They don't care. And that's the cool thing with AI — you can give people superpowers and they don't even know what they're doing, which is the crazy part.

02:30:31 - Patrick Chouinard
Well, not the ShipKit part, but the part of ShipKit, let's say. But that's it for this week.

02:30:43 - Brandon Hancock
Perfect. Well, hey, I got to run, guys, but seriously, always great getting to see you. I have a ton of updates coming out. I'm recording some more modules and stuff. So it's a busy next 11, 12 days, and then I'll have — yeah, it'll be ready for you guys. So I'll keep you in the loop, and if y'all have any questions, always feel free to shoot me a DM. If not, I'll see you guys on Tuesday. See you guys, have a great one. Bye.

---

=== UNRESOLVED SPEAKERS ===

The following speakers appeared in the transcript but were not present in the SPEAKER_ALIASES context block and have been passed through unchanged:

- **Elijah** (no last name provided in transcript)
- **Adam** (no last name provided in transcript)
- **Ola Oyo**
- **Juan Torres**
- **Alex Wilson**
- **Kris Larson**
- **Jake Maymar**
- **Marc Juretus**
- **Morgan Cook**
- **Patrick Chouinard**
- **Ty Wells**
- **Andrew Nanton**
- **Hemal Shah**