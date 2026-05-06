=== SESSION ===
date: Unknown (transcript does not specify)
duration_estimate: ~70 minutes
main_themes: Community knowledge base / RAG pipeline development, Claude Code enterprise deployment, AI-powered investment agents, AI image transformation booth, Raspberry Pi kiosk display system, Superpower + Codex workflow transition, AI model regulation discussion, Claude Code preferred tech stack

---

<!--SEGMENT
topic: Pre-meeting Chatter and Introductions
speakers: Patrick Chouinard, Marc Juretus, Paul Miller, Ty Wells, Juan Torres, Adam
keywords: golf, handicap, RAG, conversational data filtering, Claude Code, enterprise deployment, community brain, OpenWebUI
summary: Participants exchange informal greetings and golf talk before the meeting begins. Patrick previews his community brain RAG project and mentions the go-live of Claude Code in his enterprise environment, noting he is the sole trainer for a 100-person pilot. Sets the stage for the technical demos to follow.
-->

[00:00:25] Patrick Chouinard: Hey, Marc.
[00:00:31] Patrick Chouinard: Give a sec. I think I have an audio issue. Give me a second.
[00:00:41] Marc Juretus: Hey, what's up, man? That was me.
[00:00:43] Patrick Chouinard: Okay.
[00:00:45] Marc Juretus: Oh, like the backdrop. I assume that's not your residence. Would that be correct?
[00:00:50] Patrick Chouinard: I would love it to be mine.
[00:00:55] Paul Miller: I don't know if I would need a pool in there, but outside of that, I'm in.
[00:00:59] Patrick Chouinard: Actually, the only thing I would like to have is the board.
[00:01:02] Marc Juretus: A chalkboard? Wow, okay. I'm not with you on that one, brother.
[00:01:13] Patrick Chouinard: Hey, guys.
[00:01:16] Marc Juretus: Tiger Woods is at it again, I see.
[00:01:19] Ty Wells: This is a hacking opportunity for me.
[00:01:21] Patrick Chouinard: I'm going to try to hack this ball out of the rough.
[00:01:24] Paul Miller: <Q>What's your handicap, Ty?</Q>
[00:01:27] Marc Juretus: Ten.
[00:01:28] Paul Miller: <A>Oh, okay. Well, you need to be working on it.</A>
[00:01:32] Ty Wells: You need to get into those single digits. Absolutely. Well, that's hard to maintain, though.
[00:01:39] Ty Wells: Well, due to the pressure of it. I'll be in and out, guys.
[00:01:54] Patrick Chouinard: Based on last week, Ty out-designed us while golfing.
[00:02:00] Paul Miller: I think there's some secret sauce somehow in there.
[00:02:04] Patrick Chouinard: My golfing is terrible though. Honestly, the only thing I've done in golf is the driving range and I can get the ball really far. I just have no direction whatsoever.
[00:02:20] Marc Juretus: I'm actually a fairly good athlete. Don't feel bad. I can't golf at all. All I would do is the driving range. I could never do that or skate growing up.
[00:02:39] Patrick Chouinard: Hi, Adam.
[00:02:42] Adam: That's going to be fun this week.
[00:02:53] Patrick Chouinard: I'm going to be able to give a more complete demo of my community brain.
[00:03:02] Patrick Chouinard: I've learned more doing that about RAG [tool:RAG] than I've learned doing any other project.
[00:03:15] Patrick Chouinard: Filtering conversational data is brutally hard.
[00:03:24] Paul Miller: Yeah, I'm just doing a project now with that. It's a project that I attempted a year ago, and it's always harder than you think.
[00:03:34] Patrick Chouinard: Well, I've figured out a couple of tricks if you ever want to discuss it. I mean, I've had many, many hundreds of thousands of tokens thrown at the issue.
[00:04:27] Juan Torres: Hey, folks. Can you hear me?
[00:04:29] Paul Miller: This meeting is being recorded.
[00:04:40] Juan Torres: Patrick, I got the app. So I can show it to you guys.
[00:04:50] Patrick Chouinard: Sorry about my late post for the primer for this week. I completely forgot about it and then remembered it at like midnight.
[00:05:10] Patrick Chouinard: This week was the big go-live for Claude [tool:Claude Code] in the Enterprise for us, so let's just say I'm the sole trainer for Claude Code. And just in the pilot, I have a hundred people, so we're kind of busy.
[00:05:29] Paul Miller: It's a big pilot.
[00:05:34] Patrick Chouinard: And the fun part is we have people — pure dev — and we have business users with Claude Code.
[00:05:44] Paul Miller: Those are fun. Yeah, that's scary.
[00:05:49] Patrick Chouinard: It's like, oh, we're not going to give Copilot right now, it's too dangerous. Okay, so no hammer, but AK-47, no problem.

---

<!--SEGMENT
topic: Claude Code Enterprise Configuration Hardening
speakers: Patrick Chouinard, Juan Torres, Paul Miller
keywords: Claude Code, enterprise deployment, settings.json, CLAUDE.md, configuration hardening, organizational policy, pilot users, cybersecurity, VibeCoding
summary: Patrick describes how he configured Claude Code for a 100-person enterprise pilot, including deploying an organizational-level settings.json and a seeded CLAUDE.md file to constrain and explain behavior to business users. He contrasts enterprise AI governance with casual VibeCoding use.
-->

[00:06:01] Patrick Chouinard: It allowed me to learn how to do configuration hardening for Claude Code [tool:Claude Code].
[00:06:14] Juan Torres: <Q>How do you do that?</Q>
[00:06:16] Patrick Chouinard: <A>▶ Actually, you can deploy a `settings.json` at the organizational level that supersedes the personal one. And for my pilot users, I also included a seeded `CLAUDE.md` that constrained them even more, but actually explained to them why they're constrained. So they're not just trying to bypass it. It's something that tells them, no, we want that behavior for these reasons.</A>
[00:06:49] Patrick Chouinard: So yeah, quite not really easy, but really, really interesting to do.
[00:07:11] Patrick Chouinard: ▶ That's where you learn that those tools in the enterprise are very different than VibeCoding.

---

<!--SEGMENT
topic: Community Brain RAG Pipeline Demo
speakers: Patrick Chouinard, Paul Miller, Juan Torres
keywords: RAG, LanceDB, BM25, vector embeddings, OpenWebUI, Ollama, Nomic, Gemini Embedding V2, Sonnet, Kimi, chunking, hybrid retrieval, community transcript, preprocessing
summary: Patrick demonstrates his "community brain" — a RAG system built over 68 sessions (~130 hours) of community meeting transcripts. He covers his preprocessing pipeline, embedding model comparisons, hybrid BM25 + vector retrieval, and the surprising finding that preprocessing quality matters far more than the choice of embedding model. Cost for the entire pipeline was approximately $30 in tokens.
-->

[00:09:19] Patrick Chouinard: What I wanted to show this week is I've kept on working on my recap flow / community brain. So basically digesting all of the transcripts of the past two and a half years worth of this community.
[00:09:37] Patrick Chouinard: A big thank you to Brandon for supplying me with all the historical transcripts that I didn't yet have.
[00:09:49] Patrick Chouinard: Doing all of the pre-treatment of the information, plus the chunking, plus the summarizing and the embedding — I've used a lot of OpenRouter [tool:OpenRouter] models to do that, and a lot of the pre-treatment used quite big models. I used a lot of Sonnet [tool:Claude Sonnet] and Kimi 2.5 [tool:Kimi 2.5] because for the pre-treatment, I need to digest the entire two-and-a-half hours worth of transcript at once to understand the order and the topics being addressed.
[00:10:26] Patrick Chouinard: ▶ Treating 68 sessions — over 130 hours worth of transcript — cost total, total, total, like $30 worth of tokens. So pretty impressed on that front.
[00:10:52] Patrick Chouinard: ▶ I also realized building that, that the chunking and the embedding are the most worthless part of the whole project. The real value is in the pre-processed data, pre-chunking, pre-embedding, because re-summarizing all of the chunks cost 75 cents for the whole 68 sessions out of the $30.
[00:11:26] Patrick Chouinard: And I've done a lot of tests with multiple embedding models. I'm still using Nomic 1.5 [tool:Nomic Embed 1.5], the one that comes with Ollama [tool:Ollama]. I've tried the latest Nomic 2. I tried the new one from Google, the Gemini Embedding V2 [tool:Gemini Embedding V2]. ▶ Honestly, found almost no gain as long as I had very solid prep work done on my data.
[00:12:04] Patrick Chouinard: I'm using a hybrid retrieval method with both BM25 [tool:BM25] keyword search plus the vector embedding. I've done a lot of metadata insertion. So let me show you guys what it looks like.
[00:12:19] Patrick Chouinard: I'm not able to share it just yet because I haven't packaged it. But the goal is to eventually package the completely processed LanceDB [tool:LanceDB] vector database for anybody to download and use, as well as the raw prepared material. So anyone who wants to build on top of or re-embed it in their own application or run it under ChromaDB [tool:ChromaDB] or Pinecone [tool:Pinecone] or whatever, I'm going to share everything because it's our content.
[00:13:02] Patrick Chouinard: So you see, I'm running it in OpenWebUI [tool:OpenWebUI], so it's a local container that connects to my local Ollama instance. And the model you see here, "community brain," is basically just GPT-OSS with a system prompt specifically made to interrogate that database.
[00:13:27] Juan Torres: <Q>Nice. So you download the whole model together with the repo?</Q>
[00:13:30] Patrick Chouinard: <A>Well, actually, you don't need to. I'm packaging it right now. It's going to be a deployment instruction because the only thing that that is, is once you have GPT-OSS [tool:GPT-OSS], the standard model, you just go here and edit the configuration and insert a custom system prompt and save it. That's it.</A>
[00:14:00] Patrick Chouinard: And in OpenWebUI, there's one more thing that you need to configure. It's a filter function that you just copy and paste. That's just Python code to connect to the retrieval server that interrogates the LanceDB. And there's a bit of configuration — basically where it is, your API key, your top K and your timeout. That's it.
[00:14:44] Patrick Chouinard: So this is across all coaching calls — what are the most consistently discussed topics about agentic AI development? This is extremely hard. I had to redo the database multiple times to get it to answer such basic cases — not "find me the latest point where this was discussed," but "analyze all of the chunks across all the calls and tell me the top discussion scenarios."
[00:15:32] Patrick Chouinard: So you have all the themes, why they showed up in every roundtable, and the calls themselves that keep talking about it.
[00:16:17] Patrick Chouinard: And what's nice is to look at the thinking of GPT-OSS, how it actually drilled inside of the content. It's not perfect yet, but I did a test with Claude Code where I asked Opus [tool:Claude Opus] to basically do a test where it uses the same system prompt as I gave to GPT-OSS, does the retrieval itself, and then compare its answer with the one that GPT-OSS gave me.
[00:16:50] Patrick Chouinard: ▶ We're about 80% of the performance for 1% of the size. GPT-OSS is giving me results that are approximately 75% as good as Opus. So we see that the retrieval server does a lot of work to bypass the shortcomings of the model.
[00:17:18] Paul Miller: <Q>Have you looked at Gemma 4 yet?</Q>
[00:17:21] Patrick Chouinard: <A>I've tried Gemma 4 [tool:Gemma 4]. It's actually what does my summarizing at the chunk level. So for that, it's awesome. But for retrieval logic, it could not follow instructions to save its life. It does very good function calling. But following complex logic — I even tried the Gemma 4 30B, the biggest one — maybe half as good as GPT-OSS.</A>
[00:18:00] Juan Torres: You know, Patrick, I tested GPT-OSS 20 billion parameters for the extraction of entities in general ledgers, and it was actually doing pretty well — reaching 85% accuracy. But given the tax purposes of the clients, I did have to use a bigger model. I've seen the 80/20 performance difference, and it really depends on your specific needs and tolerance level.
[00:18:44] Patrick Chouinard: Yeah, but again, we're talking about the hardest possible data to query because it has to map meaning across years of transcript. The original content is a bunch of conversations with a lot of side information that's not necessary. So the cleaning up has to do a lot of legwork.
[00:19:16] Patrick Chouinard: I realized that what I was doing for RecapFlow — creating the detailed summary after each call — was already very valuable preprocessing. So I'm leveraging that on top of reclassifying the entire transcript itself.
[00:19:45] Patrick Chouinard: ▶ My version four of the specs are at a degree where I'm ready to start packaging it for deployment. So hopefully, if everything goes well, I should have a packaged version next week to share with all of you guys.

---

<!--SEGMENT
topic: Superpower SDD Framework Enterprise Rollout
speakers: Patrick Chouinard, Paul Miller
keywords: Superpower, SDD framework, Claude Code, enterprise, corporate cybersecurity, ShipKit, configuration, network constraints, sysadmin
summary: Patrick announces that his organization has adopted the Superpower SDD framework as the default for their Claude Code enterprise deployment. He notes that real-world corporate constraints — cybersecurity, network policy, sysadmin restrictions — make enterprise AI tool configuration a very different challenge from personal use, and that he will soon have scale data on Superpower's usability in that environment.
-->

[00:20:12] Patrick Chouinard: About Superpower [tool:Superpower] — I might have a little something to talk about there, not in the context of ShipKit [tool:ShipKit], but in the context of Superpower in and of itself. As you might know, we're deploying Claude Code in the enterprise, and we decided to push Superpower as the SDD framework by default for everyone.
[00:20:39] Patrick Chouinard: ▶ So I'm going to have a lot of data pretty soon on its usability at scale in a pretty constrained corporate environment.
[00:20:52] Paul Miller: Yeah, that would be helpful.
[00:20:55] Patrick Chouinard: Yep. Because it's always fun when you're an admin on your own station and you configure anything any way you want, but when it's time to make that work with the corporate cybersecurity department and network department and sysadmin, it's another ballgame.
[00:21:15] Paul Miller: Indeed.

---

<!--SEGMENT
topic: AI Investment Agent and Copilot Studio Work
speakers: Marc Juretus, Paul Miller
keywords: Alpaca API, investment agent, JSON lessons file, Copilot Studio, ServiceNow, SharePoint, Azure AI Search, CMS authentication, Zoho helpdesk, Claude
summary: Marc describes building AI investment agents using the Alpaca paper-trading API, where agents write daily lessons to a JSON file and have grown a simulated portfolio by $3,000. He also discusses frustrations with a Microsoft Copilot Studio agent project involving ServiceNow connectors, SharePoint latency, and CMS authentication issues. Paul shares a Claude-based Zoho helpdesk ticket analysis system he built.
-->

[00:21:28] Marc Juretus: Nothing really new to report. I'm kind of all wrapped up in — this one guy that I follow has agents actually investing for him. So there's an API called Alpaca [tool:Alpaca API] that'll give you $100,000 if you start out — obviously play money. So I've built some agents that are basically investing.
[00:21:54] Marc Juretus: What I'm more into is I love the lessons it learns each day on its own, and it writes back to a JSON lessons file, and it's kind of interesting to read. So it's up $3,000 already, but I just keep tweaking it a little bit each day. I'm curious to see where it is in about two months, and I actually may give it some real money and see what it can do.
[00:22:16] Marc Juretus: I saw those routines in Claude where it'll pull from the repo, my code, and run it, so instead of me running jobs on the AP scheduler locally, I think I'm going to look into doing that. But it's pretty interesting where we're at right now. I'm kind of into the guy I followed — he's got another guy in this space, and they basically have a bet on whose agent's going to earn more money in two months.
[00:22:44] Marc Juretus: We're doing a Copilot Studio [tool:Microsoft Copilot Studio] agent with all kinds of ServiceNow [tool:ServiceNow] connectors, so I'm having a whole lot of fun with that — if you didn't catch the sarcasm.
[00:23:16] Marc Juretus: It sucks, man. We're connecting to SharePoint [tool:SharePoint], but it's like a six-second lag time until you get it in context. So we've got to move it up to Azure AI Search [tool:Azure AI Search] that indexes it. The ServiceNow connector — you can submit incidents, but requests you can't do that way. And they want an agent that can submit an incident request. Well, incident is pretty much out of the box, but request is a different beast.
[00:23:51] Paul Miller: Yeah. We use Zoho helpdesk [tool:Zoho Helpdesk] and we were getting a tiresome customer just putting lots of terrible support tickets through the helpdesk and then following up with email. But I built a reporting system out of Claude [tool:Claude] that analyzed the Zoho helpdesk tickets, the ticket nature, and all the emails, and categorized every one of them about their appropriateness and whether they were taking advantage of our helpdesk team. ▶ There's some great stats and insights you can get from that and see the trends of whether you're actually responding in a positive way or not, or whether that customer is taking the proverbial.
[00:24:48] Marc Juretus: Yeah, one of our biggest problems is — the other guy on my team, I feel bad for him — we're using a third-party CMS called Unile [tool:Unile], and the authentication of the agent running in a widget in it, where you need to pass your credentials over, is not playing nice with a token. So we're working through stuff like that.

---

<!--SEGMENT
topic: AI Image Transformation Booth Demo
speakers: Juan Torres, Paul Miller, Marc Juretus, Patrick Chouinard, Morgan Cook
keywords: AI image transformation, style transfer, Disney, Akira, oil painting, Clerk authentication, EC2, CloudFront, AWS, auto-scaling, social events, QR code, inference engine, staging environment
summary: Juan demonstrates a touchscreen application designed for use as an AI photo booth at social events like weddings. Guests select artistic styles (Disney, Akira, classical oil painting), photos are sent to an inference engine for transformation, and results are retrievable via QR code. The app runs on a staged EC2 instance with CloudFront for front-end egress and uses Clerk for authentication.
-->

[00:26:05] Juan Torres: I want to just show what I did for the front end. A couple of weeks ago, I was presenting the data web application that was kind of a testing and prompt engineering ground for me to create the prompts for each of the styles I'm creating. For an app that essentially transforms a picture into an AI-style generated image.
[00:26:49] Juan Torres: And this is an idea for its deployment as an AI booth studio on the field at social events.
[00:27:09] Juan Torres: So this is basically the first screen that I intend the guests to be able to see. And I'm going to touch because this is an actual touchscreen.
[00:27:35] Juan Torres: And then the guests are able to pick a couple of styles. <Q>What do you guys want me to pick?</Q>
[00:27:39] Paul Miller: Disney.
[00:27:41] Juan Torres: Disney. Two more.
[00:27:50] Juan Torres: Classic oil painting. All right.
[00:27:57] Morgan Cook: Akira.
[00:27:57] Juan Torres: Yeah. All right. So now it's going to go through the process of sending this to the inference engine. It's going to take about a minute and a half to transform the images.
[00:28:22] Juan Torres: In the meantime, I'm going to show you this is what I have for the backend transformation. So this is my test — I can basically go into each one of the styles that I have right here and edit them if I want to. And this basically gets saved into a database, specifically a table that has the prompt test. And I have a couple of transformations here as well, organized by event in order to have a different capacity to test them and group them per event.
[00:29:49] Juan Torres: And you can actually get this through a QR code. So I have my phone here. And now, as you can see my screen right here, that's all my transformations. And I can save it on my phone. And I can click Save Images or post them to Instagram or whatever it is.
[00:30:37] Juan Torres: So this is what I have. If you guys have questions, constructive criticism.
[00:30:43] Marc Juretus: That's cool, man. I like that.
[00:30:44] Paul Miller: Yeah, that's neat stuff.
[00:30:52] Morgan Cook: <Q>Juan, this is meant to be used at social events like weddings and bar mitzvahs or whatever, right?</Q>
[00:31:00] Juan Torres: <A>Yeah, I've got ideas for you to share later.</A>
[00:31:21] Patrick Chouinard: <Q>Is it publicly available?</Q>
[00:31:22] Juan Torres: <A>No. It's authenticated with Clerk [tool:Clerk]. It says "staging" because I specifically chose the domain "staging." I haven't placed it in an auto-scaling group yet. So it's just an EC2 [tool:AWS EC2] instance. I'm going to do a couple of tests in the field with the staging environment because right now I don't think it's necessary — the current egress network data is being processed by CloudFront [tool:AWS CloudFront], not by the EC2 instance, at least for the front-end application. So I don't think it's going to get overwhelmed, but later on if I try to have several events, I do think I'm going to have to auto-scale it.</A>
[00:32:31] Patrick Chouinard: This is the type of thing that my boss would actually love for the Christmas party.
[00:32:44] Juan Torres: I don't know where you are — you're in Canada, right?
[00:32:44] Patrick Chouinard: Yeah.
[00:32:51] Patrick Chouinard: Well, if it's ever available online, it would definitely be a service you would be ready to pay for.
[00:33:00] Juan Torres: Maybe if it picks up from a field thing to license it, you know, maybe that's a thing I can do in the future.
[00:33:22] Paul Miller: <Q>What's the end game for you with that project? Where do you want to take it?</Q>
[00:33:33] Juan Torres: <A>Well, I was trying to really deploy a functional application that can be tested in the field on my own, just to also exercise my DevOps capacity. And it's a test of my capacity to actually create AI applications for when I start applying for jobs. And then test it in the field and see how popular it gets and see if people like it.</A>

---

<!--SEGMENT
topic: Raspberry Pi Kiosk Display System
speakers: Morgan Cook, Paul Miller, Juan Torres, Tom Welsh, Bastian Venegas
keywords: Raspberry Pi, kiosk display, Chrome headless, manifest, HTML slides, AI-generated content, markdown, QR code, push-pull sync, Playwright alternative, social events, SaaS, foundation
summary: Morgan demonstrates a Raspberry Pi-based kiosk display system he built over a weekend for a foundation client. The Pi boots Chrome in kiosk mode, pulls a content manifest, and displays AI-generated HTML slides with expiration dates and countdown timers. He proposes integrating it with Juan's photo booth for event displays. Tom Welsh sees potential for train station information screens. Bastian mentions a lightweight Playwright alternative for browser automation.
-->

[00:41:21] Morgan Cook: Going good. Really busy. I've got a little movement on the heritage plot — the client is on board, just a slow process. I've got a client I'm helping with a book right now that she wants to push out to Kindle Direct Print [tool:Kindle Direct Publishing]. And then a foundation is requesting a display unit they can have in their lobbies to display content.
[00:42:01] Morgan Cook: He had originally suggested he had a bunch of old iPads, and I'm like, man, that's not really going to work all that well. It can, but it's a pain to update. So this last weekend, I thought, you know what, I'm going to build this. I've thought about this several times before — having a kiosk slideshow kind of display that shows information and updates as it goes.
[00:42:29] Morgan Cook: And Juan, if you're paying attention, this is what I'm talking about for you. So in the background of my video, if you guys maximize my screen — I can't share it because it's actually running — is one of the kiosks. And this runs on a Raspberry Pi [tool:Raspberry Pi], and it self-boots and recovers from any kind of failure.
[00:43:13] Morgan Cook: ▶ It's connected through Wi-Fi off the network, but it doesn't rely on the network at all for the content. So what it does is a push-and-pull process — the Raspberry Pi checks a manifest, and if there's something new, it'll go pull all the new content, and then just runs locally. So if it can't find anything new, it just runs with whatever you have on there.
[00:43:28] Morgan Cook: For you, Juan, the thought that came to my mind with your project was — at an event, you could have a couple of these set up where the pictures that people are taking end up rotating out to the public, so everybody can see the images going on. As well as other content that would be relevant — if it was like a wedding, they could have some wedding information and different content shown throughout the event.
[00:44:11] Juan Torres: <Q>So you're saying that use a Raspberry Pi as the computational unit to then project on the screen the rotation of the transformed images?</Q>
[00:44:13] Morgan Cook: <A>So everything's running off this right here — the little Pi, just on the HDMI. It boots Chrome [tool:Google Chrome] up into a kiosk state — maximized full screen, no mouse, no keyboard, no dialogues ever pop up. It just boots right into Chrome. And then sits and rotates. It's got a manifest, and the manifest for my specific situation has each slide with a specific time. There's a default time, and then every slide has its own time. If you need one that has a lot of content, you want it on a little longer. And then it has expiration dates. So for the foundation, some of the things they put — like job fairs that have a time — it'll count down. And as soon as that's in the past, it'll just stop displaying that slide altogether.</A>
[00:45:38] Morgan Cook: So going back to my plan for it — what I tested this last weekend was just the engine. Make sure I can get the Raspberry Pi engine working, and I can push files to it, and it'll update. So I don't have to do anything with that. I could push a couple of files out there, and in five minutes, on the next cycle, it would update and start displaying new slides.
[00:46:02] Morgan Cook: For my purpose on the foundation, what I want to do is — all those slides that you're seeing are AI-generated from some simple markdown. So it takes the markdown, the AI generates this content — that's a countdown to a scheduled event, it has a QR code that you could scan to register for the event, those kinds of things.
[00:46:48] Morgan Cook: ▶ So the AI on the back side is going to allow the non-technical user to say, okay, I've got this event, here's the generic information, just as simple as possible — in a markdown or JSON format, just the name, content, everything. And then it'll build the slide to the perfect size with the nice color, the boxes and everything. And push it out to the device.
[00:47:04] Morgan Cook: So that's the next phase — to build that for what I'm doing with it. For what you would have, Juan, same kind of thing. You've already got the front end side done, taking the picture, generating the image. And then all you've got to do is push it to a hot folder, let the hot folder sync it with the devices. And then that would be a cool little event display added thing to the whole event.
[00:49:09] Bastian Venegas: I sent something in the chat. It's an alternative to Playwright [tool:Playwright] that, instead of running Chrome, uses something based in SIG and uses like one-tenth of the memory. It can be useful for some automations that access the browser. [link:chat message - Playwright alternative tool]
[00:50:29] Morgan Cook: The engine looks for any kind of injection in JavaScript and all that. So it's actually pretty cool. I've been running it for about three days now.
[00:53:16] Juan Torres: <Q>Have you thought of utilizing touchscreens together with your setup, especially when they have to input data or forms?</Q>
[00:53:21] Morgan Cook: <A>▶ This device is meant to be display only. No kind of input whatsoever. Think about it as something that's 10, 15 feet up in the air on the side of a wall that's not meant to be interacted with at that level. The interaction is through QR code.</A>
[00:53:58] Tom Welsh: Just when she's 15 feet in the air — half the train companies I work for around the country here have these custom information screens just sitting there displaying this stuff. I can just see this being perfect for that kind of operation — you host the managed ones and just push content to them daily, because all the CIS screens are just HTML.
[00:54:20] Morgan Cook: ▶ Right, this supports any kind of graphics. The AI piece generates one static HTML with built-in JavaScript to do whatever needs to be done on that specific page, and those are all loaded into an iframe inside the content. The next phase is to create a slide folder — for one slide, it might have an actual folder with the HTML and its associated resources, any graphics and JavaScript or CSS that it needs to display that one slide. And so there can be some decent animation and graphics.
[00:55:23] Paul Miller: Yeah, that could be a winner for you, Tom.

---

<!--SEGMENT
topic: Superpower vs. Codex Workflow Transition
speakers: Patrick Chouinard, Paul Miller, Morgan Cook, Ty Wells, Bastian Venegas
keywords: Superpower, Claude Code, Codex, OpenAI Codex, Claude Max, Codex Max, token limits, auto-review mode, Opus, Sonnet slowdown, T3 Chat, Tailscale, SSH, remote access, GitHub Copilot
summary: The group discusses transitioning from Claude Code to OpenAI Codex, with Superpower acting as a bridge framework that works across both. Patrick notes Codex Max offers a more generous $100/month tier and that he runs Codex in auto-review mode to catch Claude Code's errors. Paul reports hitting Claude's token limits and degraded output quality. Morgan and Ty note Sonnet's slowdown. Bastian describes remote Codex access via QR code, SSH, and Tailscale.
-->

[00:57:03] Paul Miller: Did anyone want to talk about where their thinking is at at the moment with Superpower [tool:Superpower] and Claude, or Superpower and Codex [tool:OpenAI Codex] for that matter?
[00:57:37] Patrick Chouinard: Yeah, actually, I think that's the nice thing about Superpower — they're bridging the gap with Codex because I was always afraid to switch to Codex full time. I use it for debugging and for certain tasks, but to switch it for the full development process was more about all of the niceties that I had in my harness. So basically it's not as much that I was attached to the model as I was attached to the harness, but now with Superpower that exists on both harnesses, it basically blurs the line.
[00:58:15] Patrick Chouinard: ▶ And to be quite honest, by next month, I'm thinking of shutting down my Claude Max and flipping to Codex Max that now has a $100 a month tier in between the $20 and $200. And it's vastly more generous than Claude's limits, so if I have Superpower on the other side, I have my full development harness there.
[00:58:49] Patrick Chouinard: ▶ Superpower works everywhere — they work in GitHub Copilot [tool:GitHub Copilot], they work in Claude Code, they work in Codex. And honestly, they're getting better every single month. Really, really a big fan of using it, even in brownfield projects — not just for greenfield projects, but even doing new additional functionality in an existing application.
[00:59:27] Paul Miller: It's interesting you're saying that, and I think from my own experience, I'm finding Claude a bit distracted at the moment. The token limits are being reached much more. I've been on the $200 plan, and for the first time yesterday, I nearly maxed it out in a week, and I'm kind of thinking, well, I'm not happy with the results that are coming out of it.
[01:00:00] Paul Miller: ▶ If you guys have made the jump to Codex but you're doing it with Superpower as well, that would be an easier transition from my perspective.
[01:00:10] Patrick Chouinard: The only sad thing to me is the fact that there's not yet any remote control or mobile Codex application. That's something that's very, very nice with Claude Code, honestly — to keep a process going while you're in the gym or on the road.
[01:00:41] Paul Miller: I've spent a week trying to fix my little nav map, and Claude's got to a point where it just can't fix it. I think I need to hand it to Codex and maybe put Superpower in there and get it to re-look at it.
[01:01:00] Patrick Chouinard: ▶ You know that if you use the Codex plugin for Claude Code, you can call "Codex Rescue." So basically, it flips the work to Codex, but with all of the context that you had in Claude Code. So everything Claude tried to debug that didn't work, it passes on to Codex, and then Codex rescues Claude Code by fixing the issue.
[01:01:47] Patrick Chouinard: Well, I've been using it — my current harness is running the Codex plugin in auto-review mode. So basically, every time it completes a coding iteration, it sends everything to be reviewed by Codex, sends it back, corrects whatever it finds, and it loops until it finds nothing. ▶ So far, it artificially makes it look like Claude Code is doing good work, but I realized that Claude Code is wasting a whole lot of tokens being corrected by Codex. That's what showed me that the quality seemed to be dipping, even though I didn't feel it because Codex rescued it all the time.
[01:02:33] Morgan Cook: <Q>Does anybody notice the slowdown of Sonnet? Like, it's just really slow.</Q>
[01:02:40] Patrick Chouinard: Yep.
[01:02:41] Ty Wells: <A>They're all slow. They've got a compute problem. They just can't keep up.</A>
[01:02:46] Patrick Chouinard: And I'd be very curious to hear Bastian talk about using Codex with T3 Chat [tool:T3 Chat] for remote work.
[01:03:00] Bastian Venegas: I'm — I put two screenshots in the chat, so you can see it visually — but you can connect with a QR code if you're on the same network, or you can SSH into your computer. I've heard you can use Tailscale [tool:Tailscale] as well. Yeah, so that's what most people use for their open cloud, for example. It's a pretty common stack to connect. [link:chat screenshots - T3 Chat remote Codex access]

---

<!--SEGMENT
topic: AI Model Regulation and Government Oversight Discussion
speakers: Ty Wells, Paul Miller, Patrick Chouinard, Tom Welsh
keywords: AI regulation, frontier labs, export controls, Anthropic, government oversight, model approval, chip export controls, China, open source, security vulnerabilities, Claude Opus, benchmark guardrails
summary: Ty raises news about government discussions with frontier AI labs regarding potential regulatory oversight or pre-release review of AI models. The group debates parallels to SSL/crypto export controls, China's continued AI development, and whether the security risks from powerful models are as severe as media coverage suggests. Patrick argues that the most alarming capability demonstrations require compute budgets unavailable to typical users.
-->

[01:03:37] Ty Wells: Did you guys discuss the government speaking with the frontier labs about possibly some sort of regulation?
[01:03:52] Paul Miller: No. <Q>What was that about?</Q>
[01:03:55] Ty Wells: <A>They had a conversation with those guys to sort of give them a heads up — like, which models get released, maybe government purview — they have to look at and decide what they're going to release. Or that's a possibility. I'm just saying they gave them a heads up.</A>
[01:04:30] Patrick Chouinard: That smells of export control.
[01:04:35] Paul Miller: Well, whoever's going to donate to that ballroom, their models can get approved. Sorry, as a non-American, I don't want to really tread on that.
[01:05:02] Tom Welsh: That almost seems like going back to SSL and crypto and like export controls out of the US for stuff like that. Yeah, I mean, they're already doing that with China for chips and this, that, and the other.
[01:05:16] Paul Miller: <Q>Challenges — what is dangerous? China's not going to stop. They're going to keep going on.</Q>
[01:05:25] Tom Welsh: Europe's going for it. Yeah, 100%.
[01:05:26] Paul Miller: You've got the different AI houses in America all doing different approaches and amazing things. You've got hardware-based models that are doing things cleverly and all really fast instead of really smart. Can you really stop that?
[01:05:46] Tom Welsh: Well, I think there was a story a couple of weeks back where I think it was Anthropic [tool:Anthropic] wasn't going to open the models up to the government and the government was basically going to say, well, Anthropic won't be on any approved list. So using that kind of leverage against stuff — it just seems like they're trying to jerry-rig or backdoor everything.
[01:06:14] Paul Miller: It's a challenge. And you let that genie out of the bottle too. And just from a security standpoint — that stuff around the security vulnerabilities that Claude model was finding — that's a worry once that's out there.
[01:06:39] Patrick Chouinard: Yeah, but you have to take into consideration also that there's a lot there that is made to be sensational for the news cycle. Because yeah, Opus [tool:Claude Opus] is able to find those when it's unbounded and unleashed with no compute cap. The part they don't say is, yeah, it found a bug that was there hidden for 18 years. But how much did that single thing cost in tokens? It's multiple thousands of dollars. ▶ It's the type of agentic loop that you as a consumer, even with infinite money, would not be allowed to run because you would reach the rate limiting of Anthropic enterprise before you could do something like that. So internally the model is capable, but it's never going to be released in such an unbridled form.
[01:07:49] Patrick Chouinard: Because on an intelligence perspective, GPT-5.5 [tool:GPT-5.5] is right up there with it right now. The only reason it's not capping the same benchmark is because they benchmarked it in its guardrail version.
[01:08:17] Paul Miller: So yeah, it's a risk.
[01:08:04] Patrick Chouinard: I'm not downplaying the fact that it is, but it's not the existential doomsday risk that they're playing for the news cycle either.

---

<!--SEGMENT
topic: Claude Code Preferred Tech Stack and Closing
speakers: Patrick Chouinard, Paul Miller, Morgan Cook
keywords: Claude Code, tech stack, Vercel, Supabase, feature flags, authentication, observability, email, real-time, form validation, AI SEO, Opus, Codex, ShipKit
summary: Patrick shares a link to a document listing Claude Code's preferred default tech stack — covering everything from feature flags to observability — and frames it as the new SEO: if your technology isn't referenced by the model by default, it effectively doesn't exist. The group wraps up with Paul committing to switch to Codex after a week of unresolved Claude Code issues.
-->

[01:08:19] Paul Miller: On that scary note, is there anything else that anyone wants to raise? Any new cool projects or big questions you'd like to put to the team?
[01:08:32] Patrick Chouinard: One little thing I found this week that I want to share with you guys — this link — it's all of the preferred tech stack by Claude Code [tool:Claude Code]. And it's basically very similar to Codex as well. It's basically what the model learned. So whenever you don't give it a tech stack selection, what it will tend to recommend. [link:Claude Code preferred tech stack document]
[01:08:56] Patrick Chouinard: And it's really interesting. Not just, oh, it's going to do Vercel [tool:Vercel] and Supabase [tool:Supabase]. It goes way, way further than that. It talks about feature flag authentication, authorization, observability, email, real-time, form validation — like every tech choice of the model. And honestly, it's basically all of the tech stack that you see now performing. It's the one listed there.
[01:09:25] Patrick Chouinard: ▶ So this is the new SEO. If your technology is not referenced by the model by default, you basically don't exist anymore. So yeah, brutal, but very interesting read if you want to take a peek.
[01:09:48] Patrick Chouinard: And you can see clearly that it was created by Opus [tool:Claude Opus], but still.
[01:09:53] Morgan Cook: I like the term at the top — "near monopoly."
[01:10:01] Patrick Chouinard: It is.
[01:10:15] Paul Miller: Okay. Is there anything else before we wrap up?
[01:10:27] Paul Miller: Okay. Well, have a wonderful week, guys. I'm jumping into Codex [tool:OpenAI Codex] because I've wasted four days of not delivering. Thank you for putting up with my hosting, Patrick. Guys, cool stuff. Hopefully the golf game is going right for Ty.
[01:10:56] Ty Wells: I just won this hole. So, yes.
[01:11:00] Paul Miller: Good. But how's the round, though? Are you up on the round?
[01:11:03] Ty Wells: We're only discussing this hole.
[01:11:06] Paul Miller: Let's not get contingent. All the best. Have a good week.
[01:11:15] Ty Wells: All right. See you, guys. Bye.

---

=== UNRESOLVED SPEAKERS ===

- **Adam** — Appears throughout the transcript (e.g., [00:02:42], [00:34:22], [00:36:09]). No canonical full name found in the alias map; passed through as "Adam."
- **Morgan Cook** — Appears from [00:27:55] onward. Not present in the alias map; passed through unchanged.
- **Bastian Venegas** — Appears from [01:03:00] onward. Not present in the alias map; passed through unchanged.
- **Tom Welsh** — Appears from [00:30:33] onward. Not present in the alias map; passed through unchanged.