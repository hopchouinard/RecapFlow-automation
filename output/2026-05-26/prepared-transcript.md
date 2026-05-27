=== SESSION ===
date: Unknown (Memorial Day week, US; likely late May 2025)
duration_estimate: ~2 hours 25 minutes
main_themes: AI agent frameworks (Hermes vs. OpenClaw), autonomous coding workflows (Codex deep-work sessions, Claude Code), PDF-to-markdown pipelines, community member project showcases (spelling-bee app, healthcare chatbot, parking app, AI news digest, lobby display board, AI photo booth, cemetery heritage platform, multi-tenant booking SaaS), local LLM hardware considerations, spec-driven development guidance

---

<!--SEGMENT
topic: Session Open & PDF Extraction Tools
speakers: Patrick Chouinard, Bastian Venegas Arevalo, Tom Welsh
keywords: Ollama, Dockling, MarkItDown, landing.ai, PDF extraction, embeddings, nomic-embed, Recap Flow, Hermes, OpenClaw
summary: The session opens with casual check-ins before Tom Welsh raises a practical question about processing large mixed-content PDFs for a military association archive. The group discusses the trade-offs between Dockling, Microsoft's MarkItDown, and landing.ai for document extraction, and establishes that Ollama with nomic-embed is a solid local embedding choice. The Recap Flow tool is clarified as a meeting-summary system, not a document-ingestion pipeline.
-->

[00:00:02] Patrick Chouinard: Hey, Bastian.
[00:00:17] Patrick Chouinard: Can you hear me?
[00:00:20] Bastian Venegas Arevalo: Hey, Patrick. Yeah, perfect.
[00:00:24] Patrick Chouinard: Good. It's a Brendan week.
[00:00:29] Bastian Venegas Arevalo: Oh, yeah. You had a holiday yesterday, Memorial Day.
[00:00:33] Patrick Chouinard: No, that's in the US. I'm in Canada.
[00:00:36] Bastian Venegas Arevalo: Oh, I thought you were in the US.
[00:00:39] Patrick Chouinard: No, no, no. I'm in Quebec.

[00:02:18] Tom Welsh: <Q>Question for you, Patrick, before we get stuck in everything. I've got a couple of large PDFs, about 30 megs each, which are my association Chronicle, mixed text and images. Now I'm thinking about using something like the Recap Flow to scan these things in and retrieve the data from them. Would that be a Recap Flow or should I go off and do something my own way?</Q>

[00:02:44] Patrick Chouinard: <A>No, a Recap Flow is actually built specifically for… It's not made to digest documents — it's actually the opposite. It's made exactly not to digest documents because everything else is made to digest documents.</A>

[00:03:06] Tom Welsh: That's why I've got the Mac sitting here doing the perplexity setup. Lots of Ollama [tool:Ollama] chunking coming up.

[00:03:17] Patrick Chouinard: ▶ Oh, for that, Ollama to do specifically the embedding works extremely well.

[00:03:25] Tom Welsh: Yeah, nomic or something like that, you know.

[00:03:29] Bastian Venegas Arevalo: ▶ Yeah. You just got to front-load the extraction for PDF, if not it's really, really annoying.

[00:03:34] Tom Welsh: Well, I was thinking about using Dockling [tool:Dockling] for that.

[00:03:38] Bastian Venegas Arevalo: You can use Dockling, but it's slow on CPU. It does use the GPU, but that kind of gets into a mess if you need to deploy it. But if you can do it locally and just front-load it like that, yeah. I'd use MarkItDown [tool:MarkItDown] by Microsoft — it's kind of good. It uses a lot fewer tokens compared to just using the LLM. And my favorite is by far landing.ai [tool:landing.ai] if you have complex documents or handwritten stuff that Dockling struggles with.

[00:04:12] Patrick Chouinard: ▶ Yeah, MarkItDown is great for standard documents. If you have highly complex scientific documents with embedded tables, merged columns — yeah, it's going to struggle. But standard documents work extremely well.

[00:04:25] Tom Welsh: Yeah, I mean, this is literally just a military document. Bunch of historical stuff, some photographs, standard text, set of accounts, association document once a year kind of thing. I've got them going back to 1926, but they're not all digital, as you can imagine.

---

<!--SEGMENT
topic: Hermes Agent vs. OpenClaw Introduction
speakers: Patrick Chouinard, Bastian Venegas Arevalo, Tom Welsh
keywords: Hermes, OpenClaw, Codex, OpenAI subscription, API key management, agent security, identity isolation, Pi agent, Discord
summary: Patrick introduces Hermes as his replacement for OpenClaw, praising its superior API key management, security defaults, and native Codex integration. The group briefly touches on a lightweight agent called Pi and the importance of isolating any autonomous agent from personal identity. This segment establishes Hermes as a key tool of interest for the session.
-->

[00:05:04] Patrick Chouinard: <Q>Any of you actually tried Hermes [tool:Hermes], the competitor to OpenClaw [tool:OpenClaw]?</Q>

[00:05:13] Bastian Venegas Arevalo: No, not yet. I've heard great comments about it, but I haven't tested it myself.

[00:05:18] Patrick Chouinard: Really impressive. I really love the thing. I've completely replaced my OpenClaw setup with it.

[00:05:24] Tom Welsh: That's a recommendation in itself. So I looked at OpenClaw and I'm like, oh, security, security, security. Like, so you've got to set it up with its own persona, the whole lot.

[00:05:36] Patrick Chouinard: ▶ Yeah, you have to isolate it. Any independent agent, you need to isolate it. A hundred percent.

[00:05:45] Bastian Venegas Arevalo: <Q>Is OpenClaw using Pi now? As an agent?</Q>

[00:05:53] Bastian Venegas Arevalo: A lightweight agent named Pi, like the number pi. It's really, really simple — just a couple of tools and a skill to build a skill and that's all.

[00:06:12] Patrick Chouinard: Honestly, what I love is that they support using your Codex [tool:Codex] subscription.

[00:06:21] Bastian Venegas Arevalo: Yeah, that's great. Major difference.

[00:06:22] Patrick Chouinard: Yeah, and what I love about Hermes is that it can leverage Codex as a tool — not only for the subscription.

---

<!--SEGMENT
topic: Community Q&A — Spec-Driven Development for Solo Devs
speakers: Brandon Hancock, Patrick Chouinard, Bastian Venegas Arevalo, Prakrit
keywords: spec-driven development, ShipKit, Next.js, Supabase, Vercel, LLM calls, structured outputs, sequential parallel calls, Gemini Flash, GPT-4o Mini, vocabulary app
summary: Community member Prakrit demos a vocabulary-learning app she built for her son's spelling-bee preparation, featuring word etymology, pronunciation, and language-rule cards. She describes losing momentum after adopting spec-driven development. Brandon and Patrick advise her to use ShipKit's master-plan prep phases, sequential/parallel LLM calls with structured outputs, and lightweight models to reduce latency and cost. Bastian suggests adding a TTS voice layer for pronunciation.
-->

[00:08:29] Patrick Chouinard: Just one thing, housekeeping. We have Hiral that posted a question this week, a very interesting one. She's saying that she's building an AI learning app prototype quickly, but once she shifted into spec-driven development, she lost momentum optimizing architecture and tooling instead of improving the actual product. So she wants to know when spec-driven development is actually worth it for a solo dev, which template framework to use, and what's next after a prototype stage.

[00:09:16] Prakrit: Hi. Thanks for addressing my question first, but I would like to show the prototype that I was working on.

[00:09:50] Prakrit: My son is ten years old and I'm trying to build something for him, just to get him going with words. This is what I had in mind. So when they look up a word they want to learn, I think there's a history behind that word. This is the prototype I built, where we learn about pronunciation, syllables, which ones to stress, what it means, what part of speech it is, basically where it originates from. The whole idea was to understand why certain words are spelled the way they are. The highlighted card is where I tried to point out the rule of language — why, if a word originates from German, you have certain rules versus if a similar word originates from French.

[00:11:40] Brandon Hancock: No, this is awesome. Very beautiful design. So out of curiosity, what is tripping you up? I know you said you were cranking out a bunch of new features and stuff started to slow you down. Where do you feel like you're at?

[00:12:07] Prakrit: I looked at all your videos, but I don't know which framework to apply. I think it should be a combination of multiple frameworks. But then I stumbled upon spec-driven development, where you decide on your mission and roadmap. I developed that entire spec, but once I started coding using that, I could not get to what I'm showing right now.

[00:13:00] Brandon Hancock: <A>So spec-driven development works awesome when you already have a great foundation to build off of. For example, if you already have clarity on: I'm going to be using Next.js [tool:Next.js] for my application, I'm already going to be using Supabase [tool:Supabase], I'm already going to be using Vercel [tool:Vercel] to deploy it. It needs a few core foundation pillars so that when it's spec-ing out each feature, it knows what it's building upon. If you're building a house but you don't know if you're going to be on the coastline or in the desert, it's hard to figure out what to build.</A>

[00:15:33] Brandon Hancock: <A>Here's the core paradigm your application is doing: it's taking in an input and generating about 30 different AI-generated components. Some of those components depend on previous components. The way I would tackle this is almost like a bunch of LLM calls in a very special manner, where each call takes the input — let's say the word — and the first LLM call decomposes it. Once we have the core element, you then call another that generates the meaning, the origin, and finds similar words. I would take the chat template specifically, because that's what's happening — we're chatting, but our chat is only one word. And instead of getting a conversational AI response, it's: I need the output for this word to generate this output. You're just going to do that over and over again.</A>

[00:17:20] Prakrit: So the other feature — my bigger vision is that once a student logs in and builds their vocabulary, I wanted to maintain their progress in terms of how many roots they mastered, what was the relationship between the words, different levels of progress. And then I want them to have a quiz on it, which means I would probably need a RAG kind of template as well.

[00:18:04] Brandon Hancock: <A>So the cool part is, we actually don't have to do any RAG. This is purely a database and chat. That is what we're building.</A>

[00:22:14] Patrick Chouinard: ▶ Yeah, actually, I was just going to add — if you do the sequential LLM calls, it's important to choose a smaller model for those treatments, especially if you're treating one word at a time. Don't go and ask Opus. First, it's going to cost a fortune, and it's not going to give you any better result. I would keep it to the biggest model being the latest Gemini Flash [tool:Gemini Flash] or even GPT-4o Mini [tool:GPT-4o Mini] or even Nano. So extremely fast response — it's going to improve the latency on your application and drastically diminish the cost.

[00:23:05] Brandon Hancock: ▶ And final thing, just to add to what Patrick said — structured outputs are key, because we're not trying to do a full-on chat. We're trying to say, hey, for this word, I need you to come up with this structured object which has an origin, whatever — you just need to do a bunch of structured outputs in series and parallel.

[00:23:49] Bastian Venegas Arevalo: ▶ My suggestion for further down the line: since you're probably going to use structured outputs, you could also use a structured output specifically for pronunciation and pass that to a model that generates voice — like one of the cheap ones from OpenAI [tool:OpenAI] — and the structured output will say the word just with that small caveat of where to stress it. It should be really helpful for your son or anyone trying to learn another language.

---

<!--SEGMENT
topic: Patrick's Community Brain Pre-Release
speakers: Patrick Chouinard, Brandon Hancock, Scott Rippey
keywords: Community Brain, Open Web UI, GPT-OSS-20b, Docker, Recap Flow, vector database, GitHub, install.md, Claude Code, weekly release
summary: Patrick shares a pre-release GitHub repository for "Community Brain," a locally deployable knowledge base built on Open Web UI that ingests weekly meeting recaps generated by the Recap Flow. The system uses GPT-OSS-20b as a retrieval model and is updated weekly with new meeting content. Scott and Brandon ask about API key configuration and update cadence.
-->

[00:32:00] Patrick Chouinard: I will give you a pre-release link to the Community Brain [tool:Community Brain].

[00:32:07] Brandon Hancock: Uh-oh. Uh-oh, teaser.

[00:32:09] Patrick Chouinard: Yeah, what I mean by that is it's not end-to-end tested yet. It just finished publishing the distribution repo. So if something doesn't work, don't yell at me. I will be fully testing the entire thing before doing a larger release, but this is the repo where I put the… basically, I will publish other repos including all of the mechanics and the behind-the-scenes prep work. This is the release platform. This is meant to be installed and used directly as-is with the content already built into it.

[00:32:54] Brandon Hancock: <Q>So if you wouldn't mind, what is the high-level overview? I guess I spin up Docker, it downloads, or is it pointing to somewhere else, or does it do it in the download?</Q>

[00:33:08] Patrick Chouinard: <A>You have an install.md file in there that you can give to Claude Code [tool:Claude Code], and it will take care of it.</A>

[00:33:16] Brandon Hancock: Hey, that's nice.

[00:33:18] Scott Rippey: <Q>Is this something where we can install our own API keys? I'm assuming you're not taking the cost on this, so…</Q>

[00:33:28] Patrick Chouinard: <A>Actually, this is built to work with Open Web UI [tool:Open Web UI], so you either put… I personally recommend using GPT-OSS-20b [tool:GPT-OSS-20b]. Works perfectly well as a retrieval model. But if you want to put an OpenAI API key, works just as well.</A>

[00:33:47] Scott Rippey: <Q>How does updates to the… so it would just be keeping this repo updated with things. So I assume you just keep making sure… or you pull, right?</Q>

[00:34:01] Patrick Chouinard: <A>Basically, yes, exactly. The Recap Flow that generates the weekly recap of our meeting is basically the inbound functionality that feeds into that system, and basically every week there's going to be a new release of the database with the content of the latest meeting.</A>

[00:34:26] Patrick Chouinard: So, like I said, don't be too critical of what has been released before the show, but hopefully I'm going to be able to… But if you find anything, please, if you have a couple of seconds, just file an issue in there. It's going to help me tremendously to find everything.

[00:34:51] Patrick Chouinard: I will refund you exactly what you paid for it, no problem.

---

<!--SEGMENT
topic: Hermes Deep Dive — Features, Security & Autonomous Workflows
speakers: Patrick Chouinard, Brandon Hancock, Scott Rippey
keywords: Hermes, OpenClaw, Codex, Claude Code, adversarial code review, identity isolation, Discord, Kanban board, Tavily, Firecrawl, mem0, sub-agents, GitHub, ChatGPT export
summary: Patrick gives a detailed account of replacing OpenClaw with Hermes, covering its superior API key management, identity isolation, Codex sub-agent spawning, and proactive daily email briefings. He demonstrates Hermes autonomously building its own GitHub profile and dashboard. Brandon shares his complementary "deep work" nightly Codex session workflow. Patrick also recommends the official Codex plugin for Claude Code, which includes an adversarial code review skill.
-->

[00:35:05] Patrick Chouinard: Actually, I was talking about it before you joined — I replaced my OpenClaw setup with Hermes, which I found a lot more interesting, and binding it to Codex, to my OpenAI subscription, actually pushed me toward going through one of their Pro plans.

[00:35:31] Brandon Hancock: So you're doing the $200?

[00:35:32] Patrick Chouinard: No, no, no. I'm already doing the $100 with Anthropic, so $100 is more than enough.

[00:35:43] Brandon Hancock: <Q>So are you liking it? Because I hear all sorts of awesome things on Hermes. I heard it's easier to do. I just heard nothing but pros. Any cons, just out of curiosity?</Q>

[00:35:52] Patrick Chouinard: <A>Honestly, well, there's the cons that are true for every single agent — you have to take care of security properly. I find it a lot more secure because, specifically, if you look at API key management, for example, with OpenClaw, it's a little bit all over the place whenever you have to add new systems. You can make it clean, but you have to purposefully do a lot of stuff. You have to know a lot to make it secure. Hermes already has a single place to put them. It's clear. It's easy. There's no confusion. It will warn you not to put the key in the chatbot. So if somebody doesn't know, they're aware that they should. So it's just more organized, more professional.</A>

[00:36:41] Patrick Chouinard: ▶ And just to give you an example, one thing I did is making sure not to give my identity to Hermes. So Hermes has its own identity — its own email address, its own… And the fun thing is, I basically gave the system all the information from all of my past AI assistants to build its own identity. Once it had that, I let the system create its own public profile in its own GitHub repo. If you want to take a look, everything was created by Hermes, including the graphics.

[00:37:47] Brandon Hancock: <Q>So you're saying you are using your OpenAI subscription with Hermes? And is it burning through tokens like crazy?</Q>

[00:37:54] Patrick Chouinard: <A>I can't say really because OpenAI has so much more… In their subscription compared to Claude, it seems like it's using nothing. But honestly, I've worked with it for a couple of hours and I was still over 80% left on my five-hour reset limit — and that's with it being a lot more aggressive in using sub-agents than OpenClaw is. It uses sub-agents that use tools like Codex. So if you ask it to code something, it's not going to use its own context — it's going to spawn up Codex and use it to do the coding.</A>

[00:38:45] Patrick Chouinard: So I've connected a lot of APIs with it. It's connected to Tavily [tool:Tavily], it's connected to Firecrawl [tool:Firecrawl], it's connected to mem0 [tool:mem0] for increased memory. I wanted to build an AI usage tracker. So I told it to insert it into its own dashboard, and I used the slash goal command. So basically, I told it: build yourself a prompt to use slash goal in order to do the independent development of that new functionality. And it actually decided by itself to fork the Hermes GitHub repo and started adding pages to its own dashboard. And honestly, you look at it — you could not say it was not built into the application. And I did not do anything past "here's what I want you to build, come back to me when it's done."

[00:40:07] Patrick Chouinard: Every morning it sends me an email asking me: what's your goal of the day? What are you doing today? I tell it. And an hour later, I'm going to get a ping to say, oh, by the way, based on what you told me, here's a research I did, here's something I prepped, here's a job I scheduled for you.

[00:40:38] Brandon Hancock: All right. I'm in. I have a Mac Mini sitting right there, unopened. And I have to put it to use. You've convinced me.

[00:40:57] Patrick Chouinard: One more thing. In its internal dashboard, it has a Kanban board built in, so you can just drop an idea in there, and it's going to develop it and move it along so you can see the progress as it goes. And the last project I asked it to build is: I will extract all of the two gigs of chat logs I have with ChatGPT [tool:ChatGPT], dump it in there, have it completely disassemble, chunk it, add the metadata — basically rebuild Community Brain but based on all the discussions I had with ChatGPT — and integrate it into its own memory. So it's going to inherit my last two years of chat with ChatGPT as a background.

[00:42:00] Brandon Hancock: I want to share a few things too that I think you guys might like — how Patrick's doing goal. So one thing I've really been experimenting with is what I've been calling deep work. It's very similar to goal. But basically, what I do every night is I will kick off deep work sessions in Codex on slow, and I basically just have it rip for like two to three hours. So what my new work schedule looks like: I'll start at nighttime. All day, I've been collecting like, oh, man, it would be awesome if insert new feature, new security, new bug test, new something. All day, I'm just keeping a small list of things that I want to run for multiple hours at night. Then at night, I'll kick off five separate work trees and I'll do a deep work session in each one. They're going to run for like two hours-ish, iterating over and over on the same goal — critiquing its own work, generating fixes. It does like five to seven iterations on something. And then every day when I wake up, my whole goal is to review it and then merge into main.

[00:44:14] Brandon Hancock: I'm at the $200 Codex plan, I'm at the $200 Claude plan, and that's kind of the sweet spot. Codex for nighttime stuff, Claude for daytime stuff. That's been what I've been able to do — it literally has AI running around the clock.

[00:44:39] Patrick Chouinard: ▶ And I highly recommend you try the Codex plugin for Claude Code [tool:Codex plugin for Claude Code]. The adversarial code review — incredibly useful. It's an official plugin made by OpenAI that you can call from within Claude Code as a skill. They have three skills: adversarial code review, code review, and basically rescue — that's their little dig that says, if Claude cannot do it, ask Codex to rescue you.

[00:45:36] Patrick Chouinard: ▶ The adversarial code review does a marvelous job — no matter how much review I made, it always finds something else I haven't found before. It's simple: different model, different bias. The model has different bias, so it'll find stuff the other one doesn't see.

---

<!--SEGMENT
topic: Bastian's Healthcare Chatbot Client Win
speakers: Bastian Venegas Arevalo, Brandon Hancock
keywords: healthcare chatbot, patient journey, state machine, YC-backed competitor, appointment booking, ROI calculator, partnership model, community sales strategy, AI consulting
summary: Bastian shares a successful first client pitch to a private healthcare center with multiple locations. Starting from a simple appointment-confirmation chatbot request, the team mapped the full patient journey as a state machine and built a best-in-class chatbot that outperforms a YC-backed competitor. Bastian describes a partnership pricing model and a compelling ROI calculator used in the pitch. Brandon reinforces the "foot in the door" consulting flywheel and the importance of targeting high-revenue clients.
-->

[00:24:50] Bastian Venegas Arevalo: Today I pitched a consultancy — not a SaaS actually, but more like a consultancy — about a private healthcare center that does procedures and radiology. They have really good earnings and multiple centers in the community. This is something that Brandon always advises: get involved in the community and help those businesses, because you will be the first one at the door. So I've been doing that. The first meeting went great, and they wanted us to build basically a chatbot that confirms appointments. But we went further than that and analyzed their whole funnel, because they can confirm or get appointments from their website, from email, or also by calling the center — but it's all fragmented. So actually, what we ended up building was a state machine to map all of the patient journey from when they tried to get the appointment until they finally paid for the consult.

[00:26:28] Bastian Venegas Arevalo: And we also built the chatbot, and I think it's best in class, at least for that center. They just added a software chatbot by a YC-backed company, and I think we're better than them already. So I'm pretty happy about that.

[00:26:42] Brandon Hancock: Dude, that's awesome. A, go you for having the balls to walk in and just talk to clients. Because seriously, everything you want is on the other side of a hard conversation. And another thing that I think Bastian did that's super cool — it's almost like AI is a foot in the door, where like, it's like consulting in general: there's one core pain problem they have off the top of their head. But then the second you start to untangle that, they realize there's so much more to it.

[00:27:50] Bastian Venegas Arevalo: It's in my hometown. Actually, it took like five minutes in — it's where my brother works as a doctor, and he's my CEO. They actually reached out to him because they were scared about the competition getting this YC software. They had a high number — like 38k equivalent. And we told them we would prefer to do a partnership, because you would be our first client. We won't try to — we will have you pay as you go, have your own costs, if you decide to do a partnership instead of just buying software. And if you don't, or the offer expires, well, you will have to pay full price.

[00:31:00] Bastian Venegas Arevalo: We also built a small HTML widget in the presentation — a slider — where we said: if we save you this percentage of attention, which is probably 2%, you will recover actually this amount of money. It was like 200k a year, 20k a month. And so, yeah, you can pay us. It's fine if you don't want it, but don't tell me you don't have the money because you do.

[00:31:20] Brandon Hancock: ▶ Yeah, seriously. Solve rich people problems. That's awesome. Because if you try and do that for like a local hair salon person charging $40 a client — versus what y'all are doing, it sounds like much bigger numbers.

---

<!--SEGMENT
topic: Tom's Military Association Database & PDF Pipeline
speakers: Tom Welsh, Brandon Hancock, Juan Torres, Morgan Cook, Patrick Chouinard, Bastian Venegas Arevalo
keywords: military association, membership database, PDF to image, Gemini Flash, PIL, markdown chunking, Ollama, nomic-embed, Dockling, OCR, Tesseract, Mac Studio cluster, networking costs, Thunderbolt
summary: Tom presents his military association membership database project (5,500 members, records back to 1926) and discusses digitizing historical Chronicle PDFs. Brandon shares a production-tested pipeline: convert each PDF page to an image using PIL, then pass to Gemini Flash for markdown conversion — dramatically outperforming Dockling for mixed-content documents. Juan asks about flowchart-to-Mermaid conversion; Brandon explains their decision-tree-to-nested-bullet-list approach for medical protocols. Tom also floats the idea of buying six Mac Studios for a local inference cluster, prompting a discussion of networking costs.
-->

[00:48:21] Tom Welsh: So I've got a couple of things going on. I've been writing an application for my military association, which is a membership database, basically. We've got 5,500 members, maybe 3,000 still alive — end of life to the battalion of 2006. So we're a dying breed, aging out. It was set up originally in Access, and I've retrieved it from that because it was just dead. But we've now had interest from two other military associations in what I'm actually doing. So mine's gratis for our association, but it'll be paid for others someday.

[00:50:15] Tom Welsh: Again, our association's got this annual document that comes out called The Chronicle. We've got them dating back to 1926. These have got historical stories about battles, the battalions being in this, that, and the other. And literally, whilst on the call, I've just scanned in two of them — 187 pages. So it all seems to be working quite nicely through the pipeline.

[00:50:44] Brandon Hancock: <Q>That's awesome. So it's like a RAG setup that you're doing, or are you…?</Q>

[00:50:47] Tom Welsh: I'm pulling it into vectors, yeah, but then I want to query it, so yeah, it won't be RAG. And I'm doing it all on Ollama currently, but using nomic-embed [tool:nomic-embed].

[00:51:01] Brandon Hancock: <A>Quick thing, Tom, just something that we've learned recently. So we get so many PDFs, it's unreal. What we were focused on at first was like Dockling text extractor, but one of the things that was causing issues was flowcharts, visuals, and tables — especially if they're not perfectly formatted, it just ends up being a bunch of text in random spots with no correlation. So what we did that costs a little bit more money, but the results are literally astronomically better: we take images. Every PDF page gets converted to an image. Then we have Gemini [tool:Gemini] — one of the cheaper Gemini models, like a Flash model — to say, hey, convert this into markdown. And we show an example of here's what good looks like, here's what bad looks like, here's what we want to happen. Especially if there's flowcharts, here's how we want flowcharts to be dictated and why. That one change alone — going from PDF page to image to a markdown — our new results are fantastic. And then you still have to worry about chunking, but now that you're in markdown land, chunking is so much easier.</A>

[00:52:35] Tom Welsh: <Q>Yeah, so what do you use for the OCRing? Tesseract or?</Q>

[00:52:36] Brandon Hancock: <A>No, we just use Gemini. Gemini's multimodal. So we pay a little bit more because you're ingesting an image, but man, the results speak for themselves.</A>

[00:53:27] Juan Torres: <Q>After you convert them to images, now the model has the image of the diagram. Do you have specific prompting or context engineering that basically displays the rules — for example, if you're using Mermaid — in order to systematize the conversion of the PDF image diagram into a Mermaid diagram in your markdown?</Q>

[00:54:27] Brandon Hancock: <A>So that's a kicker — our specific use case is for medical protocols. So imagine it's a flowchart: is the person alive? Step one. Are they in pain? Step two. So it's like a bunch of sub-trees — we're converting decision trees into markdown files. In our case, we need things to be in a decision tree with if-nots. It's like: if heart rate above this, go down this path. If heart rate below, go down this path. So in our case, it's pure markdown the whole way through — there's no Mermaid. The whole thing gets thrown into Gemini, the text and the graphic. And it's smart enough at this point to do it. We tested a bunch back in the day — Gemini 2 couldn't do it, GPT started to do it in the fives. But now it's affordable enough to just pass the whole page in and do one whole markdown out.</A>

[00:57:18] Morgan Cook: <Q>When you're converting that to images, you're just converting one image per page?</Q>

[00:57:20] Brandon Hancock: <A>Yes, one page, one image. At the end of the day, it's just PIL [tool:PIL] — the Python image library. And then so that's how you get the image. Once you have the image, it's then just: you turn that into base64 or whatever, do an LLM call, and then you're done. You just say, I want this text out in this format.</A>

[00:59:14] Tom Welsh: Well, I've got, I'm still with that client Derek Croy, and that's still going on. I've still got the banking thing going on, which is quite entertaining — it's my major client. I've got an invite to Vertex Ship, which is next month in London. So I'm off to do that.

[01:00:15] Tom Welsh: Yeah, I'm thinking about buying six Mac Studios [tool:Mac Studio] to build a stack.

[01:00:25] Brandon Hancock: Seriously? How much would that cost?

[01:00:51] Tom Welsh: 50k. Yeah, they're fully spec'd out.

[01:01:15] Tom Welsh: That's almost two terabytes of RAM in it.

[01:01:17] Brandon Hancock: Oh, my God. I mean, you're running the frontier at that point.

[01:02:36] Patrick Chouinard: ▶ Actually, you'd be surprised — the Mac Studio is the cheap alternative. Because if you look at DJI Spark, your problem is not the price of the machine, it's the price of the networking. Because then you're getting into micro-thick switches, because you need 100-gigabyte links between all of the nodes. The price of the networking is going to dwarf the price of the machine.

[01:03:03] Brandon Hancock: <Q>How much is some of the networking stuff?</Q>

[01:03:03] Patrick Chouinard: <A>Oh, a MikroTik 100-gigabyte switch could be easily 50k just for the switch. You're talking about bi-directional 100-gigabyte links.</A>

[01:03:18] Bastian Venegas Arevalo: They don't use networks — they just use cables directly. NVIDIA is famous for making these cables and there's some Mac equivalent to hook this up.

[01:03:40] Patrick Chouinard: ▶ And if I remember correctly, the cables themselves were like a couple of grand each. So that's why the Mac Studio, although the machines are expensive, they don't require all of that back-end stuff that gets brutally expensive.

---

<!--SEGMENT
topic: Scott's AI News Digest, Parking App Launch & Milanote Clone
speakers: Scott Rippey, Brandon Hancock, Morgan Cook, Elijah Stambaugh
keywords: AI News Digest, RSS feeds, Eleven Labs, Claude Haiku, Resend, semantic search, RAG, parking app, Stripe, Twilio, Milanote, Lightwell Board, Remotion, FFmpeg, Higgs Field, video generation, newsletter monetization
summary: Scott returns after two months to share three projects: (1) an AI News Digest email newsletter combining 10–12 RSS feeds with a Jarvis-voiced audio summary, built on Claude Haiku and Resend with a semantic search front end; (2) a parking management app for a gym client that generated $5,000 in its first weekend using Stripe and Twilio; and (3) Lightwell Board, a Milanote alternative with AI features. Brandon encourages Scott to scale the parking app aggressively. Scott also demos a Remotion-based video generation repo using Eleven Labs voice cloning.
-->

[01:04:45] Scott Rippey: Alright, so I just want to remind people — and I know, Brandon, you're on this — if anybody wants to be added to my AI News Tracker [tool:AI News Tracker], which is RSS feeds, but also I want to remind people that there is a searchable semantic link on the bottom where you can actually go and search through things. I think it's maybe two months now worth of… But if you guys want to be on this email list, it's like an email list that basically gives you AI news, about 10 to 12 feeds combined, and then there's like a voice thing with the Jarvis voice, which is my nerd stuff. I usually listen to this every day when I'm driving around.

[01:07:12] Brandon Hancock: <Q>Hey, what's a long-term plan for this? Because you listen to The Hustle, you listen to a bunch of different newsletter companies. They can become stupid profitable. So did you have thoughts on growth, scaling, partnerships?</Q>

[01:07:33] Scott Rippey: I was thinking about even turning — like Ryan actually told me I should put Google AdSense on this. I didn't yet. I probably should. Yeah, I mean, it could be something that could grow. I haven't really thought about it a whole lot. But it solves my problem. Like, I keep creating things that solve my problems, right?

[01:08:03] Brandon Hancock: ▶ Seriously, would look into — there's so many awesome videos on YouTube where Sean Puri created the Milk Road newsletter. And then same for Sam Parr creating The Hustle. Like, they just share the playbook very openly. And then the guy who made Beehive [tool:Beehive], he shares a playbook. Like, there's a bunch of cool playbooks out there. So I would just — hey, that could be another AI research task of like, hey, I am interested in monetizing it. What did the — how do I emulate those who've gone before me, but in this niche?

[01:09:21] Scott Rippey: Yeah, it was just somewhere like — and I'm able to use Haiku [tool:Claude Haiku], like, I actually don't need Sonnet for this, where I can use a cheap model. Yes, I have a $100 plan for Eleven Labs [tool:Eleven Labs], because I'm doing the whole voice thing and it's Jarvis. But my whole thing with this was: it's getting RSS feeds and combining them and not duplicating. Like, it's been almost perfect on not repeating a story. Developing stories will keep happening, and it's smart enough to know that. So it's trying to combine sources — sometimes there's more than one or two or three sources on a story.

[01:11:35] Scott Rippey: So, moving down the list, Brandon — you remember I was talking about a parking app that I was… So when I lived in Michigan, I had a guy who ran a gym, and I was doing that parking app. So we went live with it, and he made 5k on his first weekend.

[01:11:57] Brandon Hancock: Seriously?

[01:11:57] Scott Rippey: For, like, literally, it's just parking. He's banking space because he's downtown in prime real estate. And he made 5k his first weekend. I mean, I charged him 15. And I mean, I probably would charge a little bit more — he's a friend of mine anyway.

[01:12:35] Scott Rippey: So this is the page that comes up to the phone apps. He's got signs on site with a QR code. It's just phone number and license plate. And this uses Twilio [tool:Twilio] for texting and Stripe [tool:Stripe] for payments. Twilio was the pain in the ass — I think it took a long time to get everything compliant. But now that it's in, it's good. So this is the front end, and it will pull Google Pay or Apple Pay — like it kind of knows on your phone.

[01:14:38] Scott Rippey: Here's the crazy thing. When he opened this, and he set — because there's an amphitheater across the street — he set $50 event parking. He made $1,500. That was Friday night. Saturday, because of what was happening downtown, he made $3,800 in one day from hourly parking.

[01:16:00] Brandon Hancock: ▶ If I was you, Scott, I would seriously — today, right after this — have Claude go off in agent mode and look at every single parking place in anywhere downtown in Michigan, and if they have an existing app, ping them. I already have an existing one. I'll make you a killing, I'll undercut your other guy, and it's gonna work perfect. You could probably make a few hundred thousand this year, seriously.

[01:17:23] Scott Rippey: So, the next thing I have is, if you guys have heard of Milanote [tool:Milanote], I have been creating a replacement for it. Milanote is something that I love — it's an Australian company, and it's like what I organize all my stuff in. What I did was I kicked off this whole research prompt where I was like, okay, I want to see if I can build something better. Meaning, there are certain things in Milanote I don't need, and I want to see what the competitors do. And then also what we're missing. So I kicked off this whole thing, did a bunch of research, and then started building — I'm calling it Lightwell Board [tool:Lightwell Board]. I got Nano Banana in here to generate images, I got a brainstormer. This isn't done yet, but it's being built, and if anybody's interested in this, I might actually open it up to have people use it.

[01:32:47] Scott Rippey: So I have a GitHub repo I can share with you guys. If you guys want to create videos, I'm going to — so I have a GitHub repo that uses Remotion [tool:Remotion], which is really awesome. I have a repo that uses Remotion, Eleven Labs, Higgs Field [tool:Higgs Field] for scenes, which is the best video generator I can find now. But to me, this isn't generating the videos that's impressive — it's that I put real screenshots from actual applications for this real estate company that we made, and so I made a video because we were like, hey, we don't want to film anything, we just want to create this kind of teaser video.

[01:34:07] Scott Rippey: The fact that it can animate and circle things — that to me is like, I don't have to mess with After Effects anymore. I'm a video geek. I know how to do that stuff, but it's so hard. And this repo, if you guys want this, it will help you set this up and you plug everything in. And a lot of it's free — like Higgs Field you pay for, Eleven Labs you pay for. But most of it — all the Remotion, all the graphics things — it's free.

[01:34:35] Brandon Hancock: <Q>Out of curiosity, was that you actually doing a voiceover or was that Eleven Labs you?</Q>

[01:34:35] Scott Rippey: <A>That's Eleven Labs me. That's my clone.</A>

---

<!--SEGMENT
topic: Scott's Ironclaw Agent, Claude Managed Agents & Karpathy CLAUDE.md
speakers: Scott Rippey, Patrick Chouinard, Brandon Hancock
keywords: Ironclaw, local LLM, Mac Mini, Qwen, Claude Sonnet, Claude Managed Agents, rubric-based iteration, Karpathy, CLAUDE.md, GitHub CLI, keychain, Discord channels, Open Web UI, M5 Ultra, context window
summary: Scott updates on Ironclaw, his local AI assistant running on a $1,200 Mac Mini using Qwen for most tasks and Claude Sonnet for complex ones, with RAG via OpenAI embeddings and Discord for organized channels. He discusses Claude Managed Agents as a cloud-based agentic task runner with rubric-based iteration, and shares a Claude Code skill he built from Andrej Karpathy's CLAUDE.md recommendations. Patrick and Scott compare Ironclaw's security depth to Hermes's more accessible defaults.
-->

[01:19:12] Scott Rippey: Ironclaw [tool:Ironclaw] update, which is very on the conversation earlier with Patrick and everything. And Patrick, I know I have not talked to you about this. I've been working on it a bit off and on — there's been so much customer stuff I've had to do. But my system is working very well. You know, what I'm trying to do is do a proof of concept on a $1,200 Mac Mini [tool:Mac Mini], because you do have the cold start, the warm start — like there's costs, right? Like the model is only so fast. I'm trying to use the local one for as much as possible. I'm using Qwen [tool:Qwen] for the most part. And then it'll be like Sonnet [tool:Claude Sonnet] for more complex stuff. And the whole thing is — we've talked about this before — like its own identity, its own Google. It's more of an assistant, right? Like, I'm not trying to code with it. I'm trying to have it help me with my business. And so I want — I've got RAG locally, and I'm using OpenAI embeddings for that, which is so cheap, so it doesn't matter.

[01:20:40] Scott Rippey: I'm using Discord, like Patrick was saying — having channels, you don't want just one dump chat on this thing, like you want things organized. So it's getting there. I'm going to release — I will definitely give everybody that GitHub repo again when I update everything.

[01:21:15] Scott Rippey: I'm waiting for the M5 Ultra [tool:Apple M5 Ultra], I think we're waiting to find out about. But it's just — it's interesting, really, working with local models is so wild, even if it's not coding. It's so different. And very cool to learn this stuff because it's interesting about when it crashes, when it doesn't, like what the context windows are, what crashes — it's just insane.

[01:22:18] Scott Rippey: I have really been enjoying Karpathy [person:Andrej Karpathy]. So, you know, the guy from Tesla, OpenAI, now he's at Anthropic. I actually found something from his — a CLAUDE.md file [tool:CLAUDE.md]. So I created a skill. This is something I would really like to share for people if they want it, because this skill is a combination of — it injects his prompt in there, so you can actually inject a prompt from there, like so if I change anything, this file injects it in, it's a shared directory, but then it also has my rules on there as well. And then GitHub — I stopped using PATs and I started using the CLI and the local Mac keychain thing. So I've got this skill now that does all of this in one and you can run it and it'll really help you set it all up.

[01:24:06] Scott Rippey: Claude Managed Agents [tool:Claude Managed Agents] — so I've gotten into this stuff now too, where like, I know I'm not a guy who is going to be using API costs — like we all have plans, I'm not a big company. So I'm using my Claude Max plan. But the Claude Managed Agents — it's not for programming. I'm looking at that more as: okay, there's a way to run an agentic task in the cloud for clients, and it can tie into an app. So I'm doing a test right now with research. And the rubric thing is where the power is, because it will iterate until it meets a criteria. And that to me is the whole power of this.

[01:25:37] Brandon Hancock: <Q>What I think is very cool about that is like, you basically — for your client, if you know that they're gonna spend more than, let's just say 20 bucks a month in usage, then it's like, man, this actually is going to save them money, you know, maybe five times — like maybe their cost is gonna be 100, keep it at 20.</Q>

[01:26:56] Patrick Chouinard: ▶ First, I'm going to try a new anonymizer on the chat tonight, because obviously I'm guessing everyone doesn't want their email address being published tomorrow in the Recap Flow. And second, Scott, when you shared the parking lot information, you shared some screen — are those live screens, meaning do we need to remove the video from the post this week?

[01:27:40] Scott Rippey: Oh, yeah, when I was showing the numbers on the parking app, you mean? No, you're fine. There's nothing sensitive there.

[01:27:54] Patrick Chouinard: ▶ Okay, perfect. And as a warning, just keep in mind, guys, when you share stuff in video that we use that video after.

[01:28:08] Scott Rippey: Some other stuff, if you guys are interested — Anthropic did a live stream thing. They already did San Francisco, and they're doing Tokyo and somewhere else. I watched all nine hours of the Anthropic live from San Francisco, and I was recording it with Granola [tool:Granola] and breaking it down bit by bit — what would actually apply because like some things are for big companies and some things actually apply to us as smaller developers. And so I have that whole breakdown. I have a bunch of Boris videos from Anthropic that I broke down. And I'm finally starting to — I've always been a very manual person. And agentically, I use it for reports. But I'm starting to use more like skills and hooks and like try to improve processes. So I have a whole other thing — a developer's guide I've built that's a high-level kind of thing that I'd love to share if anybody thinks it'd be useful, where it's from planning to PRD to iteration to work trees and branches — just the whole end-to-end process.

[01:31:38] Scott Rippey: ▶ So the last thing I'm going to say is — so if you guys remember, I was a video guy for the last eight years. So I left IT and was a video strategist. So I have a GitHub repo I can share with you guys. If you guys want to create videos — I'm going to — so I have a GitHub repo that uses Remotion, which is really awesome. It uses Remotion, Eleven Labs, Higgs Field for scenes, which is the best video generator I can find now.

---

<!--SEGMENT
topic: Morgan's Projects — Lobby Display Board, Google Workspace Automation & Cemetery Heritage Platform
speakers: Morgan Cook, Brandon Hancock, Juan Torres, Patrick Chouinard, Scott Rippey
keywords: SignPy, lobby display board, Raspberry Pi, Node.js, Chromium kiosk, Google Workspace, Clasp, Apps Script, ORGO.ai, cemetery heritage, GIS mapping, PDF extraction, Fieldy API, wake-up word, Hermes, VPS
summary: Morgan (celebrating his birthday) shares three projects: (1) SignPy, a Raspberry Pi–based lobby display board with AI-generated slides, QR code event registration, and multi-device support; (2) Google Workspace automation for a foundation client, parsing PDFs into structured spreadsheets despite Google's friction-heavy scripting environment; and (3) a cemetery heritage platform with GIS plot mapping, circle-pack navigation, and a FOIA-based data-access layer. Patrick shares a Fieldy API wake-word trick for hands-free agent commands. Elijah mentions ORGO.ai as a cloud full-computer-use platform for running agents.
-->

[01:37:23] Morgan Cook: My ex-wife wrote a book, so we published that. Spent a lot of time doing that. Now she's working on some podcasts and other resources to go around that and funnels to feed into all of her therapeutic stuff that she does.

[01:37:52] Morgan Cook: Anyways, for me, today's my birthday.

[01:38:00] Brandon Hancock: Happy birthday. How old?

[01:38:00] Morgan Cook: I'm 56 young.

[01:38:07] Morgan Cook: So today I was spending my day setting up Hermes and a VPS server. So I've been playing with that all day.

[01:38:43] Elijah Stambaugh: Could I just say to check out ORGO.ai [tool:ORGO.ai]. They're full machines in the cloud. And it's a young company — I got to meet the founder today. You could set up your Hermes agent on those, and then they have an API as well. Check that out, because then your agent can run the system to spin up more computers, and it's full computer use, so you can have access to the screen and use it like a human would, but as an agent.

[01:39:27] Morgan Cook: Work-wise, I've been working on the paying customers, which one of them is all Google Workspace [tool:Google Workspace], and I can tell you that there is so much friction in trying to script anything in that framework right now. It's just a lot of work, but they're paying me, so I'm doing the work. I'm doing most of the work in Claude, and I use Google's Clasp [tool:Clasp] to sync it up to the Apps Script server, but it's not a very fun process and everything's so disconnected.

[01:42:15] Morgan Cook: Part of that process is for this foundation that I'm working on. I'm just automating some of their tasks. So they receive a bunch of emails. Each email has a PDF which has a bunch of content in it that they need to parse out. And that stuff has to be split out into different folders and into different spreadsheets. Then when they decide to accept or reject one of those, all that content needs to move around. And they're doing all that manually. So we're automating as much as we can.

[01:43:44] Morgan Cook: One thing you didn't see from when you've been gone — you had mentioned last time about building tools that you like. And so one of the things I built was SignPy [tool:SignPy]. And SignPy is just a lobby display board that automates displaying content. The moat that is around this is it's AI, so you can dump in any kind of content into the generator, and it will generate beautiful slides to present. The scheduled event creates an HTML that automatically has a timer countdown with a QR code registration. So somebody standing in the lobby can just scan the QR code and go register.

[01:48:03] Morgan Cook: On the Raspberry Pi [tool:Raspberry Pi], the one I've run there is just the Raspberry Linux. So it runs Chromium on the Raspberry Pi as a second thread. So when it boots up the Raspberry Pi, it automatically loads the server, launches Chromium, and starts to display. All of the slides and content are in either a graphic or an HTML container, and they all run inside an iframe. So if it has a problem, it just kicks it and goes to the next slide.

[01:51:22] Morgan Cook: The heritage plot is coming along. I've got right now what I'm working on — while I'm waiting for them to finish their piece — is just the mapping section of it. None of the cemeteries have any valid GIS information that they could just upload. Some of the county stuff does, but they're more for just whole properties — not for the individual plots or sections. So I needed a way to have a tool where they could have the map and then put an overlay over it and then trace out the plot sections and tile that stuff into the parent-child recursive tree that it generates.

[01:53:26] Morgan Cook: The moat on that is the grammar, which is kind of like a FOIA request process. They have a bunch of documents for each plot — who bought the plot, who owns the plot, is it transferable? All those kinds of things. Those documents are all not visible to everybody. There's the publicly available, it's available to the family, it's available to the court system — various things where it requires authorization to gain access to the content. The problem that the cemeteries have is they have no way to document or classify their existing documents into that system. So none of them can share anything — they don't release any information right now. So that's one of the things I need the PDF piece for — getting that content out of the PDF when a lot of the content on there might be handwritten.

[01:55:00] Brandon Hancock: ▶ And real fast, Morgan — that's why the picture approach is so helpful, because you can basically say, hey, when dealing with PDFs, if there's a handwritten section to it, what you should do is basically add like a little square box that says "additional note," and it'll basically put it right next to the content that it was talking about. Or if something was redacted — like a line through — you could basically say, here's all the common things that you're going to see from a human, and here's what you should do when putting this into markdown. So it's usable by an AI. That approach would really be helpful.

[01:58:54] Patrick Chouinard: ▶ And just a little thing I've added — Morgan, you might want to take a look at this. I don't know if you use any AI note takers. With the Fieldy [tool:Fieldy] API, you can connect it to Hermes, and I've actually set up wake-up words that I told it. So basically, every five minutes it goes and looks at the transcript for my Fieldy, and if it detects the wake-up word, it will actually take the next sentence as a command, and I have a close-up word so it stops reading the command. So I basically can say — with the wake-up word — oh, go do a search on XYZ and email it to me on Gmail. And 10 minutes later, I'm getting an email with the research material.

[01:59:48] Morgan Cook: So one of the things I was going to say, based on the research I've done on Hermes: one is there's not a pool of skills that is polluted — they have provided a set of skills that is pretty clean that they've used for months internally. Second is that it recursively builds its own skills based on what you're doing. So as you're doing stuff, it goes through and will create its own skill to do that and keeps reiterating over that process to update your skills along the way and get rid of any old skills that might not be useful anymore. The third thing that Hermes does that keeps it running clean is that it's bounded — it's not going to allow you to just create the biggest system file you can. The system file is limited to a certain number of characters. So its recursive process is very determined about making sure that the content in the system file is exactly what you need for what you're doing with the system.

---

<!--SEGMENT
topic: Juan's AI Photo Booth App Demo
speakers: Juan Torres, Brandon Hancock, Morgan Cook
keywords: AI photo booth, cDream 4.5, GPT image generation, Wavespeed, CloudFront, AWS, Resend, QR code, image-to-image, SQS queuing, AI FinOps, EC2, zip download, event photography
summary: Juan demos his AI photo booth application, which captures photos at events, applies style transformations (oil painting, Ghibli, etc.) using cDream 4.5 via Wavespeed, and delivers images to attendees via QR code and email through Resend. The system uses CloudFront for signed-link delivery to prevent hotlink attacks, and a data dashboard for AI FinOps cost tracking per event. Juan discusses QR code cross-platform compatibility issues and the zip-file download friction point.
-->

[02:03:37] Juan Torres: Well, I actually showed most of the folks here what I was doing with the AI booth application, but maybe to you, Brandon, if you want to see the progress on the front end.

[02:04:00] Juan Torres: So I plan to have an AI booth technician, basically. So create an event depending on the styles, how many photos per session. I can pick which camera it's going to be displaying, depending if I have several cameras. And so there's this huge button — make it obvious what to do. It's going to take a picture of me. And then there are several styles I can pick.

[02:04:42] Brandon Hancock: Dude, classic oil painting.

[02:05:16] Juan Torres: <Q>What models are you using for image transformation?</Q>

[02:05:16] Juan Torres: <A>For image-to-image transformation, I'm using cDream 4.5 [tool:cDream 4.5]. I've been thinking about using the new GPT image generation model [tool:GPT image generation], but this is what I'm using so far for the transformation of the images.</A>

[02:06:06] Juan Torres: While this is happening, the main issue that I was facing — and the thing that I was talking to Morgan about — is the QR code generation. So when I use this, essentially what happens is I can use my phone, and basically what's going to happen is that the images… So these are the images. And I can usually use it with your screen. You can actually pull it out if you want.

[02:07:16] Juan Torres: And you can download those images into your Photos app if you have an iPhone. And you can download them also individually. If you go scroll down, you see the images per job instead of per session that you can download.

[02:07:43] Juan Torres: One of the things that I was struggling with in this application is that the downloading mechanisms work differently for Safari and Chrome. And it works differently if it's Chrome from Android. So I created some branching rules. In order to manage the queuing process of downloading all the files — the queuing doesn't come from the EC2 [tool:AWS EC2] instance itself, it comes from CloudFront [tool:AWS CloudFront], which is the AWS service specialized in managing those assets.

[02:08:47] Juan Torres: And then what I also did — I recently added a feature so that after the event is over, essentially all the images for the sessions are sent to the client that paid for the event. I'm using Resend [tool:Resend] as the main mechanism for sending the emails.

[02:09:06] Brandon Hancock: <Q>Super quick question, info-wise. So are you using queues for a lot of this? I know you mentioned — is this getting sequenced out in a bunch of queues, or is this just all code in a list?</Q>

[02:09:17] Juan Torres: <A>Well, I was actually thinking of implementing an SQS [tool:AWS SQS] queuing mechanism to deal with the inference engine. The provider that I'm using is Wavespeed [tool:Wavespeed]. But Wavespeed actually already has their own queuing mechanism. I'm hypothesizing that they're actually using SQS. So I did some testing to stress test the queuing of Wavespeed to confirm they actually have the queuing mechanism, and they did. So I don't have to worry about queuing.</A>

[02:11:19] Juan Torres: And then one last thing — I have a data web application in the background that allows me to keep some level of observability to the mechanics of what's going on. In here, I can actually do some AI FinOps to allow me to see what are the costs that I'm incurring per event. And this is going to help me figure out some of the pricing. If I'm spending a lot of money for an event, I'm going to put that cost on the potential client.

[02:12:32] Juan Torres: I do have a tracking mechanism even for my links. I have also the ability to see what's going on in the background with each one of the events, the downloads, the emails that I sent — who they were sent to, the status of the sent, how long ago was it sent.

[02:14:06] Brandon Hancock: ▶ One thing that I've done recently — we basically used a Vercel log drain [tool:Vercel log drain], and then we hooked it up to Google Cloud. So everything that happens in Vercel, we're sending to Google Cloud. And then what we do is have it monitor the logs and send me alerts in Slack and emails. That way, if something is breaking, I know right away. So it's not like I have to happen to stumble upon it — the second something's going wrong, I want to know about it so I can address it.

---

<!--SEGMENT
topic: Alex's Multi-Tenant Booking SaaS & Closing Discussion
speakers: Brandon Hancock, Alex Roca, Patrick Chouinard, Bastian Venegas Arevalo, Adam, Scott Rippey
keywords: multi-tenant SaaS, booking software, studio scheduling, Supabase, subdomain routing, cold outreach, Stripe, Apple Pay, Google Pay, Codex deep work, tmux, Commodore Amiga, healthcare HIPAA
summary: Alex Roca shares that his studio booking app is working well for its first client and that other studios are interested, prompting a discussion on building a multi-tenant architecture from scratch rather than retrofitting. Brandon advises building a clean new codebase with organizations as a first-class concept, then porting the existing customer over. Adam discusses using tmux for managing parallel Claude Code sessions. Brandon closes with reflections on the realities of healthcare startup life under HIPAA compliance.
-->

[02:19:57] Alex Roca: Hey, so I just had a quick question. Brandon, do you remember the app that I was doing for the studio and the scheduling?

[02:20:11] Brandon Hancock: Dude, that's what I was referencing earlier — when Bastian was talking about building stuff and then, you know, you build a portfolio, then you get more customers. So yeah, I was talking about you earlier.

[02:20:27] Alex Roca: Yeah. I've been talking to some clients because I kind of left that one client up and running and it's working well. And I've been talking to other people and they are interested in getting one. So what I'm doing right now is making it multi-tenant. So I'm like, hey, do you have any recommendations on that? Because I think I need to do like a super admin role — I'm going to be the administrator, and then an organization layer, and then that organization has its own clients.

[02:20:56] Brandon Hancock: <A>So the hard part for what you're describing is the multiple domains — that's the hard part, because you're basically each app would have its own subdomain. So like, you know, it would be like company.alex.com. So like, I'm assuming what people are going to want is their own domain, you know, so that's when it gets a little bit harder. So honestly, what I would do — because you have an awesome mock-up — is I would build the new application, brand new database, brand new everything from scratch to be a multi-tenant, meaning from the get-go there's a concept of organizations, bookings belong to organizations, like everything has to be structured like that. Then, once you have it set up and working with a few dummy organizations, you could then work on porting over the existing customer to that. The thing I don't want to do is, like, oh, cool, we're just gonna start vibe-coding our way to this new app, the existing app, and growing it into multi-tenant, and then you break stuff, and then it breaks for the existing customer.</A>

[02:23:41] Brandon Hancock: ▶ It's so cool how there's unlimited niches, especially with small businesses, now that code has become affordable for businesses to buy. Like you can offer an affordable solution, you can build it very quickly. Once you find one where there's many — so like parking lots, there's multiple parking lot customers, there's studios, there's multiple studio booking — any of these can become real projects very fast. And like, Alex, for you, you'll just charge like many thousands up front, and then here's the hosting. And then what's cool is that it's so scalable. You could probably make a few hundred thousand this year, seriously.

[02:15:26] Adam: Yeah, my week's been pretty boring. Just basically doing some code cleanup. I've got a bunch of Linear tickets to go through. One thing is, I noticed you're pretty good at like starting an agent, getting it working on one bug, then you just go over to the next bug while it's working. And just my brain has a difficult time switching tasks like that.

[02:15:57] Brandon Hancock: <Q>Have you tried tmux [tool:tmux]?</Q>

[02:16:02] Adam: <Q>C-M-U-X? No, what's that?</Q>

[02:16:05] Brandon Hancock: <A>It's how — it splits your terminal. It's still mentally draining, but at least I'm not having to be mentally drained by finding the tab — it's just all right there in tmux, and I just Command-1 to hop to Workspace-1, Command-2 to Workspace-2. Like, my hands never leave the keyboard. And I name everything properly — like, this is merging staging into main, this is this bug fix — so that way it's just like, I'm not having to wait, what the heck am I looking at?</A>

[02:17:07] Adam: I guess on AI-related stuff — I used to have a Commodore Amiga in high school, and I found that you can simulate that under — so I just brought up one of those Amiga simulators and been playing around with that a little bit.

[02:25:31] Brandon Hancock: All right, guys. Well, I have to run, but seriously, always awesome seeing your amazing faces. We are hopefully — like, just a quick background — so startup, where it's so funny. I was talking to my wife, talking to my buddies about it. I was like, on paper, it's like, oh, you just do the thing, and then overnight, it's just like, I'll have millions. And then, like, real life happens, and it's like, oh, this is so much more work. There's so many new things, and especially being in the healthcare space with HIPAA and everything, everything's just more expensive. Everything takes longer, which is nice, because we have a moat, but it's just like, holy shit. This is exhausting. So I really do hope, here in the next month or two, now that we're getting over what we think is the last huge hurdle, I'll finally have more free time — because right now I wake up and I work until I go to bed.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the raw transcript but were not present in the SPEAKER_ALIASES context block (which was not supplied to this prompt) and have been passed through unchanged:

- **Prakrit** — community member who demoed a vocabulary-learning app
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** — passed through as-is (display name includes social handle)
- **Ryan - One Stop Creative Agency** — passed through as-is
- **Morgan Cook** — passed through as-is
- **Juan Torres** — passed through as-is
- **Elijah Stambaugh** — passed through as-is
- **Adam** — passed through as-is (no surname provided in transcript)
- **Alex Wilson** — brief appearance, single line
- **Alex Roca** — passed through as-is