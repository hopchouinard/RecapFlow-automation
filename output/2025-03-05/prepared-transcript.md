=== SESSION ===
date: Not explicitly stated (inferred as a weekly community call, circa early March 2025)
duration_estimate: ~2 hours 10 minutes (timestamps 00:28:03 – 02:37:31)
main_themes: Cursor IDE agent mode debate, AI voice recorders, vector embeddings and local GPU processing, junior developer interview prep, second brain / knowledge management, no-code vs. full-code development, vibe coding, AI personal brand building, CrewAI cost optimization, structured output with Pydantic, local multimodal models, voice-to-text medical tools, ElevenLabs voice agents, corporate learning SaaS, security vulnerability agents

---

<!--SEGMENT
topic: Cursor Agent Mode Debate
speakers: Brandon Hancock, Paul Miller
keywords: Cursor, agent mode, ask mode, cursor rules, IDE, AI coding assistant, multitasking, prompt control, code quality, workflow
summary: Brandon and Paul open the call discussing their mixed experiences with Cursor's agent mode versus the more controlled "ask" mode. Brandon finds agent mode useful for multitasking but inconsistent; Paul decides to revert to ask mode for better control and updated rules. The segment surfaces a common tension between autonomous AI coding and guided, iterative development.
-->

00:28:03 - Brandon Hancock
Whoa-ho-ho-ho-ho! Brandon, how's your week going so far?

00:28:32 - Paul Miller
Yeah, you know, that's just having fun with Cursor [tool:Cursor].

00:28:40 - Brandon Hancock
I gotcha. Fun in Cursor land?

00:28:44 - Paul Miller
<Q>How much are you relying on the use of the Cursor agent? Because I'm just a bit skeptical.</Q>

00:28:55 - Brandon Hancock
<A>Sometimes it absolutely crushes it and then other times it just loses control and does not what I want it to do. I've been trying to use it more and more just because I've been trying to multitask — give it a long description of what I want, come back in three minutes. But doing the regular ask method where I'm very guided in telling it what to do, I've been seeming to get better results. Jury is still out.</A>

00:29:00 - Paul Miller
<A>I just had a run through it and I think I'm going to stop using agent, go back to ask, get the control, and get my rules updated.</A>

00:30:00 - Brandon Hancock
On paper it should absolutely crush it. I think it's just new — that's why I keep playing with it, curious if it's going to unlock and become better.

---

<!--SEGMENT
topic: AI Voice Recorder Recommendations
speakers: Brandon Hancock, Jake Maymar
keywords: PLAUD, Limitless, AI voice recorder, meeting notes, transcription, brainstorming, wearable, subscription pricing, data export, voice notes
summary: Brandon shares his experience with the PLAUD AI voice recorder as an alternative to Limitless, covering pricing, accessories, and data export capabilities. Jake asks about Limitless pricing and hype. The segment is a practical product comparison for anyone seeking ambient meeting or brainstorming capture tools.
-->

00:30:17 - Brandon Hancock
I want to share some cool updates. Update one: I finally got one of those AI voice recorders going around right now. There's one on Amazon called PLAUD [tool:PLAUD] — P-L-A-U-D — and I finally got it. It's a little thing that comes with a bunch of different ways to attach it to your shirt: necklace, clip, and so on.

▶ If you're in a lot of in-person meetings, it's awesome. I love going on a long walk and brainstorming — in the past I was doing voice notes on my phone, but now I just throw this on, walk through everything I want to work on, and the meeting notes from it are insane.

00:31:47 - Brandon Hancock
I'll get my Limitless [tool:Limitless] at the end of the week, so I'll let you know which is the go-to voice recorder for the channel — which one is worth your money.

00:32:00 - Jake Maymar
<Q>What's the pricing and subscription on this? I keep hearing really amazing things about Limitless. Does it actually live up to the hype?</Q>

00:32:12 - Brandon Hancock
<A>This one was $160 and it came with four different ways to wear it, which is pretty nice. They have plans — either $9 or $20 a month for PLAUD. The $20 is unlimited, which is half the price of Limitless — Limitless is about $40 a month. The other thing that's nice about PLAUD is it's easily set up to export data. I can't tell yet if Limitless makes it as easy to get your data out.</A>

---

<!--SEGMENT
topic: AI Authority Accelerator Video Announcement
speakers: Brandon Hancock
keywords: AI personal brand, content creation, monetization, YouTube, networking, AI Authority Accelerator, lead magnet, email list, personal branding, video masterclass
summary: Brandon announces the upcoming release of a comprehensive masterclass video on building an AI personal brand in 2025, covering niche selection, content creation, networking, and monetization strategies. He previews the five pillars and mentions a waitlist for a paid accelerator program. This segment is relevant to anyone looking to build visibility and income around AI skills.
-->

00:33:04 - Brandon Hancock
Final other thing: I finally finished the AI Authority Accelerator video. It is a masterclass. I tried as hard as I possibly could to show you guys how to build an AI personal brand. The video will come out tomorrow — it's about an hour and twenty minutes.

▶ It literally walks through exactly how to pick a brand, how to start making content the proper way, how to properly network with people, the different levels of monetization within your AI personal brand, what are the best ways to do it to start, and what you can do as you grow your brand. It covers literally everything step-by-step.

So very excited for you guys to see that when it comes out tomorrow morning. Then I'll go back to regular coding tutorials.

---

<!--SEGMENT
topic: Vector Embeddings and Local GPU Processing
speakers: Paul Miller, Brandon Hancock, Jake Maymar, Bastian Venegas
keywords: vector database, embeddings, BGE-base-EN-V1.5, Qdrant, Ollama, Cohere, OpenAI text-embedding-3-small, GTE-small, GPU, SSH, local models, recipe database, Supabase
summary: Paul describes building a recipe recommendation app with a 2.5-million-recipe database and the challenge of generating embeddings locally on a MacBook Pro versus offloading to an NVIDIA GPU server over SSH. The group discusses embedding model choices — BGE, Cohere, Ollama, and OpenAI's text-embedding-3-small — and the trade-offs between speed, accuracy, and cost for local versus API-based embedding generation.
-->

00:34:44 - Paul Miller
I've got to get this code out for this app that I'm building. I'm really on the final parts now. I've been focused on how to tokenize all the embeddings around all of the recipes. I've got a recipe master database of two and a half million recipes, so I've been throwing a lot of GPU at doing that really effectively, because I have to keep applying it to new restaurants that I'm reviewing.

00:35:41 - Paul Miller
<Q>I've got one of these new MacBook Pros with a lot of RAM. But I've started offloading to SSH to another box that's got a bit more grunt with an NVIDIA GPU. Is that what other people do? When you're doing high-processing stuff on your base machine, what do you do, Brandon?</Q>

00:36:34 - Brandon Hancock
<Q>Would you mind sharing a little bit more — when you say data, what are we actually looking at?</Q>

00:36:39 - Paul Miller
<A>As part of setting this up I need to set up some vector databases alongside my base relational database. To create the vectors and do the embedding — all of which sucks a lot of resources — I'm doing it locally because I don't want to wait for the API. I'm putting it on a GPU to generate it as well.</A>

00:37:28 - Brandon Hancock
<A>Personally, I'm not — I've strictly been using all online models just to speed through stuff. I'm not going deep on local for big actions like you're doing.</A>

00:38:00 - Jake Maymar
<Q>What model are you using for embeddings? Are you using the Meta models, Mistral?</Q>

00:38:09 - Paul Miller
<A>I had used some API-based commercial ones, but I wanted to switch. Because I'm doing a lot of things locally, I'm using BGE-base-EN-V1.5 [tool:BGE-base-EN-V1.5], which is a recommended one — about 700 or so dimensions. It's kind of optimal and accurate for my use case.</A>

00:38:51 - Brandon Hancock
Were you storing this in Qdrant [tool:Qdrant]? The reason I ask is that Supabase [tool:Supabase] actually recommends using even fewer dimensions. They also have a recommended model — GTE-small [tool:GTE-small] — and I'm curious if their models are even faster for what you're trying to do. I will look into that and send it over to you.

00:41:01 - Bastian Venegas
<A>I have used Cohere [tool:Cohere] as a local model for embedding — it's decent but not state-of-the-art. I've also seen some people use Ollama [tool:Ollama] to do embeddings. But my usual go-to is OpenAI's text-embedding-3-small [tool:text-embedding-3-small]. The small version is almost exactly as good as the larger model. That's what I would use if it's not proprietary data.</A>

00:41:44 - Jake Maymar
The local models aren't great.

00:41:46 - Paul Miller
The challenge is the speed of creation — how quickly is it generating the embeddings. That's why I moved local for this.

00:42:00 - Brandon Hancock
▶ I just sent you a link to what Supabase recommends — GTE-small — for most vector use cases. I would be curious if you switch to that smaller model whether you notice a speed improvement. They wrote an article saying they've actually noticed improvements by using some of these smaller models. You can run that one locally, so it's a win-win.

---

<!--SEGMENT
topic: Junior Developer Interview Preparation
speakers: Brandon Hancock, Cyril I, Jake Maymar, Bastian Venegas
keywords: junior Python developer, technical interview, object-oriented programming, whiteboard coding, soft skills, University of York, interview preparation, Self-Made Millennial, abstract class, behavioral questions
summary: Cyril shares that he has reached the interview stage for a junior Python developer role at the University of York out of 5,000 applicants. Brandon and others provide detailed advice on both the soft-skills interview (storytelling, prepared project examples) and the technical interview (OOP principles, whiteboard questions, asking clarifying questions). Jake adds tips on unexpected questions and no-tool coding environments.
-->

00:43:28 - Cyril I
I've been applying to some junior software developer jobs, and I've surprisingly somehow got to an interview stage out of about 5,000 applicants for a junior Python developer role, which quite impressed me. I've never had an interview in my life for a technical role.

<Q>Are there any ending pieces of advice, or is there anything I need to know? I'm stressed — if I've made it that far, I'm already proud of myself. Any suggestions on how to pass the interview?</Q>

00:44:50 - Brandon Hancock
<A>I actually just did an interview with someone for a junior spot this morning, so this is a very fresh topic. Usually there are two stages: the general soft interview — your soft skills, your background — and then the actual technical code side. It's usually a two-part interview when you're applying for an engineering role.

For the first one, there is a YouTube channel — Self-Made Millennial [tool:Self-Made Millennial YouTube channel] — and her big thing is just having a box of stories. Most interview questions come down to "tell me about yourself" or "tell me about a time on a project when you did blank." You can already have a list of prepared projects that best showcase your abilities. You'd be amazed how many times you can tie back most questions that are asked. Watch her two videos and you'll dominate the soft side of the interview.

For the technical interview: for a junior Python role, master the core basics of object-oriented programming. A classic whiteboard question is "design a parking lot application." That question serves two purposes — it tests your initiative to ask clarifying questions and your communication. If you just start building right off the gate, that's a huge red flag. Ask a ton of clarifying questions to make sure the interviewer is on the same page as you. The more you can impress with your understanding of OOP principles — abstract classes, concrete classes, interfaces — the more you'll dominate the competition, because most people only get to the function level.</A>

00:50:16 - Jake Maymar
<A>A lot of times you'll prep for the interview and they give you content ahead of time, and then they ask you completely different questions. Also, sometimes in a code interview they won't let you use any tools — you basically write it in a notepad. Just be prepared for those two things.</A>

00:51:00 - Brandon Hancock
▶ Even though it's a real-life interview, there might be a whiteboarding component — you physically go to a whiteboard. I would expect you to ask clarifying questions: what kind of parking lot, are there multiple stories, do we want to count how many cars are in there? Pull information out of the interviewer.

00:51:56 - Cyril I
The interview is on the 10th of March.

00:52:00 - Brandon Hancock
Coming up, man. I'll send you over some more resources. Seriously, congrats on getting this far.

---

<!--SEGMENT
topic: Second Brain and Knowledge Management
speakers: Jake Maymar, Brandon Hancock, Bastian Venegas
keywords: second brain, Notion, Obsidian, RAG, knowledge base, Tiago Forte, Thomas Frank, Notion AI, journal, personal knowledge management, search engine, Discord, Slack
summary: Jake describes building a RAG-based personal second brain to capture and query information from calls, Slack, Discord, and other channels, with a personalized prompt layer. Brandon demonstrates his own Notion-based second brain approach — a journal for brain dumps queryable via Notion AI — and recommends Tiago Forte's book and Thomas Frank's Notion templates. The segment is a practical guide to personal knowledge management for people overwhelmed by information across multiple platforms.
-->

00:52:27 - Jake Maymar
I'm very excited — finally building out my second brain. I'm on a lot of these calls and I cannot capture all the great information. What I'm hoping to do once I have the second brain up is share it. It's a RAG-based [tool:RAG] system — essentially a way to access all the data.

00:53:00 - Brandon Hancock
<Q>When I hear "second brain," I think like Tiago Forte's Notion second brain. Where do you mean?</Q>

00:53:10 - Jake Maymar
<A>Exactly. I was using Obsidian [tool:Obsidian] because Notion [tool:Notion] wouldn't let you export, but now Notion lets you export. Notion is pretty awesome and nicely integrated into everything. It's great for assistants. Just finding a place to dump everything — images, videos, transcripts — and then start connecting all the different channels. I have Slack channels, Discord channels, tons of stuff all over the place. It's all valuable but hard to sift through. Essentially it's a search engine for those things. But what's cool is you can prompt it and make it personal — I have one prompt that's like my interests, so it will automatically prioritize and bubble up things I'm looking for. What I'm building is essentially a form so you can fill it out and the same knowledge base should appeal to you as well.</A>

00:54:40 - Brandon Hancock
▶ I literally call my second brain "second brain." Two files everyone needs: a journal — a brain dump — so every time you do anything, put it in here. Then you can ask questions about it using Notion AI [tool:Notion AI]. I was just like, "what was the last thing I talked about with Nate?" and it pulled up all conversations where I'd mentioned him. One place, brain dump it, talk into Notion, pin it into a Notion journal, and you can instantly query anything ever. I cannot tell you how much this is a lifesaver.

▶ I would seriously recommend Tiago Forte's book "Building a Second Brain" [link:Building a Second Brain by Tiago Forte]. It is honestly life-changing. Notion has a very generous free tier — definitely recommend looking into that.

00:56:28 - Brandon Hancock
▶ Bastion, thank you for calling out Thomas Frank [tool:Thomas Frank YouTube channel]. He does have some awesome stuff. If you're looking for templates and a quick Notion masterclass, his free stuff is awesome.

---

<!--SEGMENT
topic: No-Code Tools and Vibe Coding Trends
speakers: Jake Maymar, Brandon Hancock
keywords: no-code, low-code, Lovable, n8n, proof of concept, vibe coding, Claude, rapid prototyping, SaaS, consultancy, Windsurf, Cursor
summary: Jake reports that a consultancy he worked with has split into three firms, all moving toward no-code tooling even among advanced developers. Brandon and Jake discuss the appropriate use cases for no-code — rapid prototyping and POCs — versus full-stack development for production. Jake also introduces "vibe coding," a trend of giving extremely vague prompts to Claude and iterating with "make it better" to generate unexpected results.
-->

00:57:00 - Jake Maymar
The consultancy that I was working with has split into three consultancies — one focused on healthcare, one on all verticals, one more product-based. What's really interesting is they're all leaning toward more no-code, which I think is fascinating. These are pretty advanced developers and very technical people, and they're all moving to this more no-code structure. <Q>Are other people finding this as well?</Q>

00:57:47 - Brandon Hancock
<A>Yes, on the rapid-idea iteration side of things, for single-purpose applications, yes. But as things grow beyond proof of concept, you still kind of need the full-stack development. For rapid idea generation, a lot of these no-code tools are awesome. I've seen a lot of people use Lovable [tool:Lovable] plus n8n [tool:n8n] to quickly spin up an application. It's great for rapid prototyping, but you will pay more for it.</A>

00:58:50 - Jake Maymar
Mostly looking at POCs — proves the concept is viable, then they shop it around, and once it's viable they build it out with traditional tools.

00:59:24 - Jake Maymar
<Q>Is anyone doing vibe coding at all — where you say something very vague like "make a grocery app" and then just say "improve it, make it better, make it better" in Claude [tool:Claude] or other tools? Claude seems to be the one. You get some wildly garbage results but also some really cool, bizarre ideas.</Q>

01:00:03 - Brandon Hancock
<A>I haven't got to it yet, but that sounds awesome. If there's any specific videos or examples, Jake, if you don't mind sending them over, I'd love to see them.</A>

---

<!--SEGMENT
topic: CrewAI YouTube Content Strategy and Thumbnail Review
speakers: Bastian Venegas, Brandon Hancock, Jake Maymar
keywords: CrewAI, Docker, YouTube thumbnail, Canva, lead magnet, landing page, Kit, email list, hook, video title, source code, call to action, content strategy, enterprise deployment
summary: Bastian shares a landing page built with Kit to capture emails via a source-code lead magnet, and previews a YouTube video about deploying CrewAI Enterprise for free using Docker. Brandon and Jake give detailed feedback on the landing page CTA copy, thumbnail design, video title, hook structure, and step-count framing. The segment is a practical workshop on YouTube content strategy and conversion-optimized landing page design.
-->

01:01:00 - Bastian Venegas
I have a ton of projects that are interesting but not necessarily in a YouTube-video-friendly format. I'm taking projects I already have and building a more tailored video around them. I can share the source code from GitHub [tool:GitHub] and I built a landing page using Kit [tool:Kit] so I can grab emails and send them the source code.

01:03:01 - Brandon Hancock
If anything, could we make that lock icon bigger? The three things someone needs to see on the site are: yes, it is yours; why did I come here — it's to get source code; and the button. It's not really "subscribe" — it's a call to action, which is "get source code."

▶ Change the CTA text to "Grab free source code" and "Get instant access" — make that bigger so it catches the eye, because that's why people came to this site.

01:04:53 - Jake Maymar
▶ If you change the lock to a different icon — gold, money, something that doesn't feel like a lock — subconsciously a lock stops the user. Also make this work on the phone first. You have too much text. People have very short attention spans. Make things for drunk babies — super easy to click, as if you are 10 feet away or on a phone.

01:06:28 - Bastian Venegas
The title would be: "CrewAI Enterprise is Expensive — Deploy It for Free Using Docker." And the hook: "CrewAI [tool:CrewAI] is my favorite framework for building production applications and 40% of Fortune 500 companies agree. But deploying them is expensive — just look at the pricing tiers. And if I told you there's a way to get the same power for free? I'll show you how to deploy CrewAI using Docker [tool:Docker]."

01:07:27 - Brandon Hancock
▶ I would change the title to: "How to Run CrewAI Enterprise for Free with Docker." Plain and simple — if I was looking up how to do this, that's the exact language I would use.

▶ For the hook: cut "but what if I told you there was a way to get it for free" — too salesy. Just say "and in this video I'm going to show you how you can completely run it for free." People love numbers — say "in today's video I'm going to show you the six steps to deploy for free." That way they know what they're getting into.

01:10:50 - Brandon Hancock
▶ On the thumbnail: you're hiding the lead. The main text should be "Run CrewAI Enterprise for Free" — huge text. Then throw the Docker logo and the CrewAI logo in there. We want to be hyper-clear, not cute. Use an existing Canva [tool:Canva] template — do not start from scratch.

---

<!--SEGMENT
topic: Master's Program vs. AI Personal Brand for Career Growth
speakers: Naveen Selvaraju, Brandon Hancock, Jake Maymar, Bastian Venegas, sherif abushadi
keywords: Georgia Tech OMSCS, interactive intelligence, machine learning specialization, AI engineering, personal brand, career transition, Canada job market, applied AI, LangChain, CrewAI, Pydantic, RAG, Andrew Ng, Coursera
summary: Naveen asks whether to pursue Georgia Tech's interactive intelligence or machine learning specialization to break into AI roles in Canada. Brandon, Jake, Bastian, and Sherif collectively advise against deep machine learning theory in favor of applied AI and building a visible personal brand. Sherif adds nuanced points about visa constraints, cultural overvaluation of credentials, and using frontier LLMs to self-teach any syllabus. The segment is a career strategy discussion highly relevant to developers trying to transition into AI roles.
-->

01:15:00 - Naveen Selvaraju
I applied for a master's program — Georgia Tech [tool:Georgia Tech OMSCS] — and they have multiple specializations. The two I'm interested in are interactive intelligence (more like generative AI / applied AI) and machine learning specialization (more mathematical, deep learning background). <Q>What would people who are actively working with AI recommend?</Q>

01:18:37 - Brandon Hancock
<A>Machine learning — I would stay away. You're going to have to go so deep into calculus and theory, and the gap between that and providing value to people is huge. You'll come out with your brain doubled in size but not making more money. I would stay with Andrew Ng's [tool:Andrew Ng Coursera] courses on Coursera.

As an AI engineer, what you need is: competency on what all models can do and when to use them; the core pillars of building agent systems — frameworks like LangChain [tool:LangChain], CrewAI [tool:CrewAI], Pydantic [tool:Pydantic], small agents; and understanding what an agent is — really nothing more than tool calling and prompts, but that goes very deep with RAG [tool:RAG] and vector stores. There's no machine learning in that. Applied AI is what you want — building full-stack applications that do something with this new technology.</A>

01:22:01 - Jake Maymar
I totally agree. Understanding the math is important but you'll figure it out as you go. If you're focused on evals or fine-tuning, you'll learn the math for that specific thing. Practical applications of AI are really about efficiency and quality.

01:23:10 - Bastian Venegas
Focusing on learning deep into the weeds is not the way to go right now because that's not what the market perceives AI actually is. I would just ride the wave of large language models.

01:27:49 - sherif abushadi
<A>Maybe you have visa constraints in Canada that require you to be in good standing with an employer or educational institution. Culturally, based on your background, it's possible you overvalue education — the industrial illusion we've all been drunk on for 200 years.

▶ You can apply and get accepted to these programs and put it on your resume, then during your interview process tell them you're in the middle of taking it. That is often just as strong a signal as having finished it.

▶ Any school right now is in a white heat about AI taking over their business, so you can probably shoot higher — MIT, Stanford — they're probably bleeding applications as people self-educate.

▶ Almost certainly any program you join is going to be 6–12 months behind the times. Just look at what's happened in the last 90 days.

▶ Any one of the modern frontier models — if you copy-pasted the syllabus and told it "you are responsible for teaching this class, walk me chapter by chapter, create sub-chapters, references, books, YouTube videos, podcasts" — you can probably create two or three versions of the thing you'd see at the best university in a matter of minutes in 2025.</A>

01:30:55 - Naveen Selvaraju
It's a part-time program. I'm not leaving my job. It only starts in September, so I have plenty of time to try new things. Maybe having it in my profile would show visibility that I'm doing something.

01:31:48 - Brandon Hancock
▶ After tomorrow, watch the video and let me know. The whole goal of the video is to show you that the root problem is: you're a very smart developer and the world doesn't know that. How do we solve it? We get leads by showcasing what we can do — shout from the rooftops and showcase our competencies online on LinkedIn and YouTube.

---

<!--SEGMENT
topic: Local Multimodal Models for Code Extraction from Images
speakers: Alex Wilson, Brandon Hancock, Paul Miller
keywords: local LLM, multimodal model, vision model, LM Studio, Ollama, Microsoft Phi-4, OCR, code extraction, banking security, data privacy, Faster Whisper
summary: Alex needs to extract code from images of old work projects without using public-facing AI services due to banking security concerns. Paul recommends Microsoft's Phi-4 models runnable locally via LM Studio as a privacy-safe multimodal option. Brandon expresses curiosity about the quality of local vision models for text extraction. The segment is a practical guide to privacy-preserving local AI for sensitive professional data.
-->

01:33:08 - Alex Wilson
<Q>I use ChatGPT a lot with images to extract text. I have a bunch of old code that I only have images of — I don't have the code anymore. I want to use something to bring that code back into code state. But I don't want to use public-facing stuff because it was for my job — banking security. Do you know of any vision models that might do a reasonable job of helping with that locally?</Q>

01:34:07 - Brandon Hancock
I'll drop the option in the chat — that's a local multimodal model.

01:34:12 - Paul Miller
<A>Microsoft put out the Phi-4 [tool:Microsoft Phi-4] models and you can run all those locally — the 3.5 GB ones. You should be able to run them on your desktop. Some can work with Ollama [tool:Ollama], but they need an upgraded Ollama that hasn't been released yet. So you might have to run with LM Studio [tool:LM Studio] or one of the other local hosts.</A>

01:35:00 - Alex Wilson
OK, I will try LM Studio.

01:35:02 - Brandon Hancock
<Q>As you do it, let me know what you think — does it do well? Some vision models are garbage, some of the older ones could barely break out stuff and really struggled with text. I'm curious because it looks very promising.</Q>

01:35:26 - Alex Wilson
I will definitely let you know.

---

<!--SEGMENT
topic: Voice-to-Text Medical Documentation Tool
speakers: Nate Ginn, Brandon Hancock, Jake Maymar
keywords: EHR, speech recognition, Faster Whisper, local LLM, Python, speech-to-text, text-to-speech, chiropractic, review of systems, medical documentation, SpeechRecognition, Ollama, beta testing
summary: Nate, a chiropractor, demonstrates a Python tool he built (with GPT-4o's help) that conducts a voice-driven review-of-systems interview and generates structured EHR notes using local speech recognition and a local LLM. A colleague has already expressed interest in buying it. Brandon and others discuss improving the speech-to-text pipeline with Faster Whisper and local text-to-speech models. The segment showcases a compelling real-world AI application in healthcare documentation.
-->

01:55:33 - Nate Ginn
I used voice access to talk to the agent in Cursor [tool:Cursor] and Windsurf [tool:Windsurf] — it was like this: "OK, I need to go to this" and it was so funny. I'm like, I'm just too tired. "I'm going to bed." "OK, thanks. We'll work on this tomorrow." I love it when they respond like that.

01:56:06 - Nate Ginn
I'm a chiropractor, just so you know. I wrote a program that goes into my EHR — the one I talked about last week — it codes and does that. I told my buddy about it and he was like, "Hey, do you want to — I will buy that from you, I will need that in my office." And I'm like, "Oh, it's nowhere near production ready." I might try and beta test it with him.

Last night I was writing templates for my EHR — just a review of systems template. My EHR is very template-based. I wrote a program — well, GPT-4o [tool:GPT-4o] wrote a program — where the program asks me the questions like "do they have a fever?" and I just respond "yes" or "no" or "positive" or "negative," and it totally worked.

01:58:00 - Nate Ginn
[Live demo — the tool speaks questions aloud and captures voice responses]

**Tool voice:** "Let's begin with the general section. Is there any fever?"
**Nate:** "Negative."
**Tool voice:** "Is there any chills?"
**Nate:** "Positive."

01:59:06 - Brandon Hancock
It takes the whole transcript and then it'll get to the output. That is awesome.

02:01:29 - Brandon Hancock
Dude, it sounded like the Stephen Hawking voice — cracked me up. I was not ready for that when it started talking. But that is awesome.

02:02:00 - Brandon Hancock
<Q>Does anyone know if there are any good local text-to-speech models?</Q>

02:02:07 - Nate Ginn
It's using Faster Whisper [tool:Faster Whisper]. At least at one point it was supposed to be using Faster Whisper for speech-to-text. It kept rewriting and going back and forth between Google voice recognition and Faster Whisper.

02:04:05 - Brandon Hancock
▶ I'm sending two links over — I think if you just pass those into Cursor and say "I want to use the first thing for speech-to-text and the second for text-to-speech," it will just take it from there. Point and click — it feels like cheating.

---

<!--SEGMENT
topic: Voice Agent for Automotive Dealerships
speakers: Maksym Liamin, Brandon Hancock, Bastian Venegas
keywords: ElevenLabs, voice agent, automotive dealership, lead management, text-to-speech, trial, car manufacturer, API integration, sales AI, Mexico, 11Labs credits
summary: Maksym updates the group on a delayed but progressing AI sales tool for automotive dealerships. Due to early success with test users, the team has been invited into a paid three-month trial with a car manufacturer, competing against four other companies, focused on voice-based marketing to 6,000 leads. The team is building custom voice agents using ElevenLabs rather than third-party frameworks, due to proprietary API integration requirements.
-->

02:05:14 - Maksym Liamin
Launch didn't happen — we postponed it, not because of our reasons. We already delivered all the features needed and even more, and we're iterating with testers. We're still missing some important data needed for the actual global launch across all the dealerships. I hope we can get that by mid-month.

Because of this success with the test users, we were able to get into a trial with the actual car manufacturer — the ones these dealers are affiliated with. It's a competition between four different companies, and it's a paid trial. It will be around three months, testing with about 6,000 leads, focused on marketing and voice. If it goes well, we get full capacity after three months.

02:07:37 - Brandon Hancock
<Q>For voice agents — are you going to go Bland [tool:Bland AI], some other tool, or thinking custom? What's the team currently thinking?</Q>

02:07:47 - Maksym Liamin
<A>We'll use ElevenLabs [tool:ElevenLabs] for text-to-speech and just build it ourselves. We won't be using any frameworks. It's somehow faster for me to build from scratch than using built-in stuff. Also, we need a lot of integrations — the manufacturer has its own in-house software that we won't be able to get through third parties, so we'll need to connect it ourselves. They already gave us some API details.</A>

02:09:00 - Maksym Liamin
We already use ElevenLabs for the dealership software — to translate voice notes. As soon as we introduced it, people immediately started using it. We got a nice deal with ElevenLabs to get credits.

---

<!--SEGMENT
topic: AI in Mental Health and Psychiatric Evaluation
speakers: Andrew Nanton, Brandon Hancock
keywords: Massachusetts Psychiatric Society, NIH, Wellcome Trust, mental health AI accelerator, psychiatric evaluation, forensic psychiatry, Oregon Department of Justice, grant funding, AI in medicine, speaking engagement
summary: Andrew shares an upcoming speaking engagement with the Massachusetts Psychiatric Society on AI in medicine and psychiatry, and discusses a Wellcome Trust / Google mental health and AI accelerator program offering up to £3 million per approved group. He connects this to his project with Maksym on streamlining psychiatric evaluations for the justice system, where backlogs are creating legal scrutiny. The segment highlights a significant funding opportunity for AI-in-mental-health projects.
-->

02:11:34 - Andrew Nanton
This weekend I got an update for an event — talking to the Massachusetts Psychiatric Society [tool:Massachusetts Psychiatric Society] about AI in medicine and psychiatry. Still keeping that speaking gig going.

02:12:38 - Andrew Nanton
People at the NIH [tool:NIH] have made moving a hackathon project into a grant-funded proposal more complicated. But there's a person I'm collaborating with — that could still come together. I also put in the school forum about a group from Google and Wellcome Trust [tool:Wellcome Trust] — they have a mental health and AI accelerator program that they just announced with up to £3 million in funding per approved group. [link:Wellcome Trust Mental Health and AI Accelerator]

▶ If anyone wants to take a look at that and you've got something you want to do that is mental health related, I'd be happy to chat with you about it.

02:14:00 - Andrew Nanton
Right now, Oregon is under scrutiny from the Department of Justice because if someone is arrested and they're too mentally ill to proceed to court, the amount of time to get them from court to evaluation to treatment is too long. In California it's like six months. The idea that there needs to be a more efficient way to help evaluators evaluate — reliably, ethically, responsibly — a larger volume of people: the demand is clearly there.

02:15:05 - Brandon Hancock
▶ Please post it on that one. I feel like most developers are not in that space, but there's a lot of good that could be done by mixing the two.

---

<!--SEGMENT
topic: CrewAI Agent Cost Optimization and Structured Output
speakers: Sagar Passi, Brandon Hancock
keywords: CrewAI, GPT-4o, o3-mini, AgentOps, Pydantic output, cost optimization, token usage, traceability, travel agent demo, financial services agent, structured JSON, prompt engineering, API cost
summary: Sagar, a UK-based software agency owner, reports that his CrewAI financial services agent costs £3 per run using GPT-4o. Brandon recommends switching to o3-mini for immediate cost reduction, using AgentOps for traceability to identify expensive steps, assigning simpler tasks to cheaper models like GPT-4o-mini, and using Pydantic output schemas on tasks to enforce consistent structured JSON without verbose prompt instructions.
-->

01:49:34 - Sagar Passi
I found you through the YouTube channel. I've been in the AI space for a year, building wrapper apps. I have my software development company. In the last three weeks I used your demo to create my own agent — a financial services agent for a back-office team. One thing I struggled with: the cost. Every time I ran the agent it was £3. I was using GPT-4o [tool:GPT-4o]. I recently switched to o3-mini [tool:o3-mini] because I think the API just came out. <Q>Is there a way to reduce the cost?</Q>

01:50:25 - Brandon Hancock
<A>o3-mini should be a drastic drop — that change alone should be a sizable improvement.

▶ A few other things for cost minimization: certain tasks and certain agents you could honestly put on dumb models — like GPT-4o-mini [tool:GPT-4o-mini]. If there's any task where you're just checking to see if something exists, instantly go GPT-4o-mini.

▶ Have you used AgentOps [tool:AgentOps]? They give you the ability to replay the entire crew end-to-end — it's called traceability. You can see where your crew gets stuck. What we're ultimately trying to do is have every task be a single shot. The more times it has to do stuff, check, do stuff, check — that's just more money out of your pocket. I'm reading it line by line — the input that went into it and the output that came out — and just tweaking prompts.</A>

01:53:29 - Sagar Passi
The second thing: I needed the output to come out in a JSON structure so I can use it downstream, and I'm really struggling to get it into the same format consistently even with prompt engineering.

01:53:45 - Brandon Hancock
<A>▶ There's actually a field that will force it to spit out structured output — it's called output Pydantic [tool:Pydantic]. In each task, you specify the model you want out of it. I'll send you a link to this part of the code. Basically you update a task to say "I want you to output something like a blog, and a blog has a title and content." That should also really help reduce the size of your prompt because you're not having to add in all those additional instructions — under the hood it will take care of it for you.</A>

---

<!--SEGMENT
topic: Eleanor AI App: Document Ingestion and Demo Strategy
speakers: AK, Brandon Hancock, Jake Maymar
keywords: Eleanor, document ingestion system, Google Drive, Supabase, Chroma, vector database, LangGraph, RAG, UI, GitHub, demo branch, version control, co-coding, product development
summary: AK updates the group on Eleanor, an AI assistant with a document ingestion system (DISH) that connects to Google Drive, with fallback vector stores in Supabase and Chroma. He reports a setback after moving the codebase broke his pipeline. Brandon advises building end-to-end first before adding fallbacks; Jake strongly recommends maintaining a dedicated demo branch in Git and demoing frequently to accelerate product focus and user feedback. AK also mentions a VC who expressed interest and a no-code/low-code job application.
-->

01:36:21 - AK
Where I am since we spoke last week: I took your advice. My graph was working really well — I was just having a little bit of retrieval stuff, but in my test scripts it was working really well. I had it set up so it would fall back to Supabase [tool:Supabase] and then fall back to Chroma [tool:Chroma] after that when it looked for similarity.

What I did was switch gears and started working on what I call the DISH — Document Ingestion System — food for Eleanor [tool:Eleanor AI]. The success I had: I created a UI, built the platform where you could get a Google OAuth connection, list all my documents from Google Drive [tool:Google Drive], pull documents, and have them back through it right away from my DISH. Where I'm having trouble is still just getting the documents to be added as part of context.

01:38:43 - AK
I did something stupid and had to move my whole codebase, so I'm re-putting things back together. Had I not done that I think I would be able to show you guys the functional chat interface as well as the ingestion system.

01:42:07 - Brandon Hancock
<A>▶ My only strategic advice: fallbacks are awesome once it's working end-to-end. Let's get it working end-to-end first, then implement fallbacks. You might realize later that now that I've built it end-to-end and I see it working, I need to tweak something else. I love getting things working all the way through very shallow, then going back and saying "this needs love, this needs love."</A>

01:45:00 - Jake Maymar
<A>▶ Once you have customers — friends and family — you are so close to a product. It's a focus tool: they hold you to what you're building, they have skin in the game, and as they're using it you're like "oh, that's a good idea, I should build that in." It saves you a lot of time because instead of building a product you think everyone wants, you actually build a product they want.

▶ Make a branch called "demo" right when you have it working. Push the changes to that branch — you know it works, you know it's solid — and then keep going. When you have another demo, make another branch called "demo-2." I can't tell you how many times in the middle of the night I overwrite demo-1. Plan on demoing, because the more you demo the better your product is going to be and the faster you'll get it there.</A>

01:48:52 - Jake Maymar
I've started over four times from scratch because I did that and I learned my lesson.

---

<!--SEGMENT
topic: Corporate Learning SaaS and Monetization Strategy
speakers: Patrick Hutchinson, Brandon Hancock, Jake Maymar, Paul Miller
keywords: corporate learning, SaaS, survey engine, performance-focused surveys, instructional design, LinkedIn Learning, Cursor, test-driven development, Windsurf, context window, monetization, affiliate, consulting, personal brand, AI-powered analytics
summary: Patrick, a first-time caller with a background in corporate learning and development, introduces a survey engine SaaS that uses AI to evaluate training program effectiveness. Brandon and Paul offer monetization strategy advice — starting with services before productizing, affiliate/referral models, and embedding in organizations via recurring AI coaching subscriptions. Jake and Patrick discuss practical Cursor/Windsurf tips for managing large codebases, including test-driven development and breaking scripts into smaller modules.
-->

02:15:53 - Patrick Hutchinson
I was a Linux systems administrator early in my career, then got into corporate learning and development. Got laid off almost a year ago and got back into trying to start my own business. I'm building a paid SaaS app — AI-powered and using AI to code it. My expertise in corporate learning and development is really focused on helping businesses evaluate training programs better using analytics, basically prompting the AI to do it how a professional would do it.

▶ I'm thinking about soft-launching in the creator space — people on School, for example, who have courses but might not know how to ask the right questions of their learners to improve their courses.

It's a survey engine — Performance Focus Surveys — that helps evaluate whether learners have actually learned the skills and can transfer them back into their work. It also scores your survey and does sentiment analysis for open text questions.

02:18:44 - Patrick Hutchinson
I kept running into context issues as my codebase gets bigger — regressions as a result. I went back to old-school test-driven development and have been having it build out tests. Now if I change something and the test fails, instead of missing something when it's rewriting, the test is failing and it knows what it's doing. That's been really helpful.

02:19:16 - Jake Maymar
▶ Testing basically every component saves so much time. Summarize everything as you get to a good place. Make sure you're doing version control. I love Windsurf [tool:Windsurf] — it's really nice — but don't do automation, do check. You can take a really big script and ask it to break it down into pieces, then test each one. Once you have those smaller scripts it gets so much more manageable.

02:23:30 - Brandon Hancock
<Q>Are you talking about this on LinkedIn?</Q>

02:23:49 - Brandon Hancock
<A>▶ I think you could very easily start positioning yourself as the guy who ensures quality for courses. There's a two-sided market: people building content and organizations consuming it. You could easily agitate organizations: "You're probably spending tens of thousands of dollars every quarter on professional education for all your employees — but are they retaining it?" You could also offer audits. There are a hundred things you could do — not even AI yet — just as the specialist.

▶ The easiest way to start making money is to do the service yourself and then productize it later. If you can do this yourself 10 times under your own umbrella, it's a lot easier to then productize it. Once you productize it, it's harder to tweak and change. So be quick and agile first.

▶ Two other monetization ideas: (1) Affiliate — be a conduit between the specialists and the businesses. Build a brand, educate people on the problem, and every time a specialist gets a new client from you, take 10–5% of the corporate sale. (2) Influencer/speaker for the specialist — get paid to do the talk at corporate learning events. The affiliate approach is highly scalable because all you're doing is posting and directing traffic with zero fulfillment needs.</A>

02:28:14 - Paul Miller
<A>▶ I've seen people doing this kind of advising productize it by putting content in a streamable format, then doing one-on-one AI-based interaction with teams to question how they're going with the methodology, and then you subscribe to having a virtual coach that validates you're following the methodology and reports back up to the program manager. If you're actually connected to the metric of confirming it's done and feeding back to the person who pays the bill the value of what they've achieved — you're really in the money.</A>

---

<!--SEGMENT
topic: Security Vulnerability Detection Agent and Session Wrap-Up
speakers: hackysterio, Brandon Hancock
keywords: CrewAI, security agent, business logic vulnerabilities, Loom, screen recording, AI Authority Accelerator, YouTube video, personal brand, waitlist, community
summary: A new member (hackysterio) briefly introduces a CrewAI-based security agent for detecting business logic vulnerabilities. Due to the technical depth required, Brandon redirects to an async Loom review rather than a live walkthrough. Brandon closes the session by reminding attendees of the upcoming AI personal brand masterclass video and the AI Authority Accelerator waitlist.
-->

02:34:17 - hackysterio
I've been building agents with CrewAI [tool:CrewAI]. I'm in server security, so I built an agent recently to detect business logic vulnerabilities — because even the normal scanners we use don't catch those well.

02:35:04 - Brandon Hancock
▶ I think for this question, because we're about to go pretty technical, if you're able to record a Loom [tool:Loom] and record the crew that you're building, I will happily review it tomorrow and can point out what's going wrong and how to fix it. If you wouldn't mind doing that, I think that's probably the best way.

02:36:10 - Brandon Hancock
All right, guys, we're a little past time. Final updates: be on the lookout tomorrow for a new YouTube video all about building your AI personal brand. I held nothing back — so excited to see your feedback. Inside the video I cover the five pillars and go much deeper. If you want additional support, there'll be a link to join the waitlist for the AI Authority Accelerator [tool:AI Authority Accelerator] — if you want help building your personal brand with a bit more hand-holding and review along the way. That'll all get blasted out tomorrow. Thanks — another great call. See you next week.

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names were not found in the SPEAKER_ALIASES context block (which was not provided in this session) and have been passed through unchanged:

- **Cyril I** — junior developer / computer vision student, University of York interview candidate
- **AK** — building Eleanor AI assistant with document ingestion system
- **Sagar Passi** — UK-based software agency owner building CrewAI financial services agent
- **Nate Ginn** — chiropractor building voice-driven EHR documentation tool
- **Maksym Liamin** — building AI sales/voice agent for automotive dealerships
- **Andrew Nanton** — psychiatrist, speaking on AI in medicine, collaborating with Maksym
- **Patrick Hutchinson** — corporate learning and development SaaS founder
- **Naveen Selvaraju** — full-stack developer in Canada considering Georgia Tech OMSCS
- **sherif abushadi** — community member offering career strategy advice
- **Bastian Venegas** — developer building CrewAI/Docker YouTube content
- **hackysterio** — security professional building CrewAI vulnerability detection agent
- **Alex Wilson** — developer needing local vision model for code extraction from images
- **Jake Maymar** — community member, building second brain, consulting background
- **Paul Miller** — building recipe recommendation app with vector embeddings