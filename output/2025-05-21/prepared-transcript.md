=== SESSION ===
date: Not explicitly stated (references Google I/O announcements as same-day)
duration_estimate: ~2 hours 7 minutes (00:04:16 – 02:11:30)
main_themes: Google I/O announcements, Google ADK development, RAG and vector store architecture, client project pricing and NDA negotiation, voice agent development, ETL pipelines on AWS, YouTube content creation, career advice for agentic AI roles

---

<!--SEGMENT
topic: Google I/O Recap and Weekly Updates
speakers: Brandon Hancock, Paul Miller
keywords: Google I/O, Firebase Studio, Gemini 2.5 Pro, Lovable, Supabase, row-level security, Codex, video generation, image generation, API upgrades
summary: Brandon and Paul debrief on Google I/O announcements, noting mostly model upgrades rather than new developer tools. Brandon highlights Firebase Studio's long-awaited Firebase integration and shares his current client project workflow combining Lovable, Gemini 2.5 Pro, and Cursor-based rules to dramatically compress development timelines.
-->

00:04:16 - Brandon Hancock
Yo, yo, everybody.

00:04:19 - Paul Miller
Hey, Brandon.

00:04:20 - Paul Miller
You've jumped out of Google I/O mode.

00:04:24 - Brandon Hancock
It actually finished in plenty of time, so all good. I was worried. Did you get a chance to watch them, out of curiosity?

00:04:35 - Paul Miller
I started going. I haven't fully processed them, because I got excited. I don't know if I've missed that on the keynote. I got excited with that thing that was announced yesterday, where they've done the Codex equivalent — which I think they came up with the Codex equivalent, and then OpenAI [tool:OpenAI Codex] copied them, and now they've released it. So I don't know if they've released it into live. I'm on the wait list for it. But yeah, I'm still processing. I don't really have any immediate feedback. What's your findings?

00:05:21 - Brandon Hancock
What's funny, real fast on that, they have like multiple competing products because they have Firebase Studio [tool:Firebase Studio], which does the thing. Then they have their coding project, like that's all Gemini [tool:Gemini]. I think the one that you're talking about basically also does the same thing. So I think they're just like, we're going to fund every innovative project internally that we can think of, and just throw everything out to the world. And whatever people continue to play with, we will continue to support. So I think that's what they're doing. It would take me more tools to play with.

00:05:58 - Brandon Hancock
I didn't find it — I thought there was going to be a bunch of new stuff, but it was mostly actually upgrades, like their new video generator, then they have their new image generator. All the APIs kind of got a new model, but yeah, I was hoping for a few new developer tools or things. Didn't really hear any.

00:06:20 - Brandon Hancock
The only one I'm kind of pumped for is Firebase Studio. They listened to everyone and were like, yeah, the whole point of Firebase Studio is to connect to Firebase. We're now going to actually let you do that. Like, which I thought was wild that they took this long — oh yeah, now you can do it. So I've been trying to log in over and over again to actually get involved or see if they've actually rolled it out because they said they were going to. So no update yet, but hey, maybe in just a few minutes they will.

00:07:04 - Brandon Hancock
The main updates on my side this week, mostly just spending a ton of time building out a project for a client. A ton of fun with Supabase [tool:Supabase] right now. Still stand by my earlier suggestion of, like, all the row-level security and all the other stuff that you have to set up — it's a pain in the butt. But when it works, great. But getting it actually working, God, it's taken up so much time. I want this data to go here. And even when you set the row-level security, it's like, oh actually, this role itself — not even user-based role, but this type of user itself cannot even make this action. So it's row-level security, then role security, and then there's the actual authentication you do in your app.

00:08:07 - Brandon Hancock
▶ One, I would just share like, hey, this same project a year ago would have taken like weeks. And now with Lovable [tool:Lovable], the new Gemini 2.5 Pro [tool:Gemini 2.5 Pro], absolutely love that thing. Cursor-based rules [tool:Cursor]. I've been able to crank out what should have taken multiple weeks in like days. So I was just going to share my workflow for knocking stuff out. So that'll be a video later this week.

---

<!--SEGMENT
topic: AI Camera Surveillance Side Project
speakers: Paul Miller, Brandon Hancock
keywords: Reolink NVR, video analysis, Gemini 2.5 Flash, frame sampling, computer vision, API, video processing, cost optimization
summary: Paul describes building an AI-powered system to analyze security camera footage from his Reolink NVR to identify a neighbor illegally dumping garden waste. Brandon recommends using Gemini 2.5 Flash for video analysis at low cost, and suggests frame-rate reduction as a preprocessing step to cut API costs.
-->

00:09:11 - Paul Miller
Yeah, so I've pretty much got launched into Alpha testing with the user, my little first-level app with the FastAPI [tool:FastAPI] backend. That's working well. He's about to share it with his clients at the end of today, so we've got one minor thing he's found, which I'm just going to jump into fixing, which is so easy now, because it's nice and segregated, and I don't go and stuff up the API, and that knocks onto everything else. So I'm pretty excited about that.

00:10:00 - Paul Miller
No other sort of real exciting stuff other than I got distracted in my usual way. I was out walking the dog — we live next to a park in Auckland — and we've got this lowlife who, instead of buying a garden waste collection subscription, dumps his branches in the park so he doesn't have to wait for someone to pick it up. Not cool. But it's been going for a couple of years. Being a sort of over-the-top geek, our house is surrounded by AI cameras, and it all goes to a DVR system, and the last time he did it, I got him filmed doing it. I sent it to the council with all the video clips. He didn't know that the cameras were there.

00:11:19 - Paul Miller
I noticed a couple of days ago, he's done it again. So instead of manually going into the Reolink NVR [tool:Reolink NVR], I thought, oh, I could go into some kind of API because it's quite an open environment, download all the videos, analyze them, and look for his car. Because I don't want to go through days of video footage. So I've kicked off a little project to build an API over the NVR and then build an AI app where I put a description of what I'm looking for and just get the AI to go off and drill the videos and find the car and find the incident.

00:12:04 - Brandon Hancock
He's pissed off the wrong nerd. That's all I got to say.

00:12:21 - Brandon Hancock
Real fast. Quick idea. ▶ Just the Gemini model itself — Gemini 2.5 Flash [tool:Gemini 2.5 Flash] — I think that is now more stable. I think you can pass videos to it and especially just throw it in at 720p because it doesn't need to be high res to detect it. And you could probably sift through all of that for like a couple dollars, which is wild. So that would be how I'd recommend trying it out.

00:13:13 - Brandon Hancock
▶ And Bastian had a cool idea too, of like, hey, you could actually probably do some preprocessing before you pass things up to Gemini just to cut down on frames. Because it doesn't need to be 30 frames per second. Probably just two, three, four, five — there's probably plenty. So pretty cool idea — could save money too.

---

<!--SEGMENT
topic: Local RAG Vector Store Architecture
speakers: Marc Juretus, Brandon Hancock, Bastian Venegas
keywords: ChromaDB, vector database, RAG, embeddings, FastAPI, MCP server, LangChain, Agno, PostgreSQL, text embeddings, Google embedding model, Graffiti GraphRAG
summary: Marc asks how to build a local vector knowledge base for use across multiple agent projects, including storing agent conversation outputs. Brandon recommends ChromaDB for local vector storage with a FastAPI wrapper exposing query and add endpoints, while Bastian suggests a GraphRAG MCP server called Graffiti and clarifies the role of embedding models in the pipeline.
-->

00:13:34 - Brandon Hancock
Mark, you're up next, man. What's going on? What projects are you working on?

00:13:41 - Marc Juretus
No rush, man. I figure you want that syllabus of what Chris went through. So yeah, I sent you basically the PDF that they sent us at the weekend course. So it has everything changed and stuff like that.

00:13:54 - Marc Juretus
As far as what I've been working on, I was kind of obsessed with consuming an MCP [tool:MCP]. Here I am inside of my Python code, as opposed to leveraging it in Claude or something like that. It took me a little while to get that working. But one of the videos I've watched on that, the guy was alluding to the fact that a lot of stuff, if you're going to do custom MCP, you can accomplish with either FastAPI or your own functions. But where it's going to go to is what he was pretty much saying — it's going to be a lot more useful in the future. I mean, it's obviously, because of all the plugins now and stuff, you can do a Claude personal shopper, scrubbing videos and stuff like that.

00:14:35 - Marc Juretus
So I was trying to get FastAPI working because, honestly, in my day job where I do Spring Boot, I serve up APIs with Java Spring Boot. So I was trying to learn the latest practices with that. But I did have a question. <Q>As far as, say, I wanted to actually convert some of my stuff to a vector database that I only — and what I want to do is go on to Postgres in Docker, maybe turn that on, and if I point to that tool, if I have information, I can have a tool created that can have an agent go against that only when I would need it. I wouldn't want to really push it in the cloud. So I'm wondering if I would do it in LangChain [tool:LangChain] or LangGraph [tool:LangGraph] or with Crew AI [tool:Crew AI] or just something else that's more progressive that you would recommend. I'm just going to basically take a bunch of data, throw it all in — and I've seen there's a pretty easy way to do it with Agno [tool:Agno] as well. But what would you do if you had data that you're going to use intermittently for maybe different projects, but you'd like to be able to turn on and point to it as a tool?</Q>

00:15:38 - Brandon Hancock
<A>Okay. And so just to make sure I fully understand — you have documents that you want to put to a vector store, and you are going to be interfacing, basically making RAG requests to this vector store in multiple applications?</A>

00:16:00 - Marc Juretus
Just mainly all agents. So I'll just turn it on and have a tool pointed to it in whatever way. And I might have a combination of data, PDFs, and stuff like that. It's like my own knowledge base. But I was like, sometimes I want to push in the cloud, but like, hey, I want to have this on. I want to point to it. What would you use? Would you use LangChain? Would you use Crew, Agno?

00:16:21 - Brandon Hancock
<A>No, I mean, strictly two approaches. One, I would just spin up a local server that connects to — so part by part. So you need somewhere to store all the vectors. So I would recommend ChromaDB [tool:ChromaDB] — it's the easiest one to just spin up a local vector store in. So I would definitely recommend if you're going to — you're going to need a vector store locally. ChromaDB is probably one of the easiest ones to use. There's a few other ones, but that's the one I'm most familiar with. You could also — you did mention you're pretty familiar with Postgres — you can do that as well, but Chroma is the easiest way to make a vector store.</A>

00:17:03 - Marc Juretus
Well, like, so you went to an agent and you typed in a question and then you say, I want to take the response to the answer I got to that. I want to store that locally in my RAG and have that as my own personal knowledge base — is what I was trying to accomplish.

00:17:17 - Brandon Hancock
Oh, okay. So you want, like, message history? Yeah. So in that case, I mean, either way, we still have to have the vector store. But basically what you'd want to do is spin up either, kind of like you just alluded to a second ago, either an MCP server or you want to just spin up a generic Python FastAPI. The FastAPI would expose, like, three endpoints — like query and add. Those are the two things that you would want to set up. And you could just create two tools in whatever agent framework you're using that knows how to use those two endpoints. So you're basically just going to wrap that endpoint.

00:17:52 - Brandon Hancock
So I know Bastian has the most experience with MCP. I'd love to get his thoughts on it really fast.

00:18:01 - Bastian Venegas
<A>Yeah. Actually, I just came across a repository that's called Graffiti [tool:Graffiti] because it's an MCP server that implements some sort of GraphRAG. So if you're trying to explore both spaces, I will link it in the chat.</A> [link:Graffiti GraphRAG MCP server repository]

00:18:25 - Marc Juretus
Okay. Yeah, I'll do that. I was kind of confused on what agent I would use to actually convert it to vector. That's where I was like, I could do the PostgreSQL to Chroma, like you said, or I'll look at what you have. But I was like, what's actually the agent to use if I could prove it?

00:18:40 - Bastian Venegas
<A>Oh, yeah. So that's the embedding model you can use. You can use like the text embeddings model [tool:OpenAI text-embedding-3], the three versions, which is really sufficient. And there's also a Google embedding model [tool:Google embedding model] that I will link in the chat as well.</A>

00:19:10 - Brandon Hancock
<A>Real fast, Mark, just to add onto that. So the agent will actually know nothing about RAG. That's the beauty of it. All the agent knows is, hey, whenever I want to get new information on a topic, I just make a tool call. That is the extent that the agent knows about RAG. All of the RAG service — meaning the taking in a text question from the agent, the embedding of that text, basically to embed it into all the ones and zeros and everything else that it needs to actually query the vector store — all of that is going to happen inside the FastAPI service that you're going to stand up. So I just wanted to draw a hard line: agents use tools; those tools, in the case of your example, will just pass a string query over to your API, and then your API is going to handle the embedding, it's going to handle making the query, and then it's going to come back with a response of like, hey, I found this chunk, this chunk, and this chunk.</A>

---

<!--SEGMENT
topic: Google ADK and Fantasy Football Agent
speakers: Marc Juretus, Brandon Hancock
keywords: Google ADK, Crew AI, sequential agent, ADK MCP tutorial, fantasy football, agent framework, tool wrapping, Next.js, Streamlit
summary: Marc shares progress converting his Crew AI fantasy football app to Google ADK, successfully wrapping Crew tools for use in ADK. Brandon praises ADK's responsive development team, notes a known issue with sequential agents asking unnecessary questions, and recommends Next.js over Streamlit for production frontends.
-->

00:20:31 - Marc Juretus
<Q>And you said whenever you have front-end stuff, you — like, as far as production — you never use like a Streamlit. It's always like a Next.js [tool:Next.js]. Is that what you said? Or a Streamlit, something just locally for testing that you found?</Q>

00:20:43 - Brandon Hancock
<A>I mean, I love just using Next.js for all things. That's how my brain thinks. So Streamlit [tool:Streamlit] can work. It's just like the second you want to do anything a little bit more advanced, you're kind of like, well, dang, now I just got to start over with Next.js anyway. So might as well just go with the thing. It is scalable. And every AI tool right now just really understands Next.js really well too. You'll be amazed how easy it is to get it spun up.</A>

00:21:33 - Brandon Hancock
Finally, something I think you'd find interesting — if I have time by the end of the week, I want to do an ADK MCP tutorial [tool:Google ADK]. So that might be also helpful just because, like, instead of setting up the FastAPI server, you might also consider MCP. So I'll go into that and I'll report back too on how easy I think it is.

00:21:54 - Brandon Hancock
Yeah, I'm getting pretty deep in your ADK stuff, though.

00:21:57 - Marc Juretus
Like, basically, I'm taking what I have in my Crew for that fantasy football app I have. I'm converting it completely to Google ADK, and I finally got the wrappers of Crew, because I like their scrape tool and their search tool. I was actually able to do that embedding, and ADK was able to consume and give me output. So some of the stuff I have, I can reuse, but I want to get it completely over there with a sequential agent. So it looks like, thanks to you though, man, that was really easy to go.

00:22:25 - Brandon Hancock
▶ What's really cool — I've started to talk to some of the guys on the ADK team. They're so responsive to feedback, like they're instantly chomping at the bit to add in features. So one of the issues you'll see with sequential agents is like, sometimes they pop out and say like, hey, do you have a question? Which is kind of not what you want in a workflow, because the whole point of a workflow is it just does the work and feeds you the answer. So they're looking into stuff like that — they're hyper responsive. So if you ever have anything, let me know, happy to pass along.

00:23:04 - Marc Juretus
I think this is exciting. It seems like doing Google ADK now, like I said last week, is kind of like doing Crew AI 10 months ago. Like, it's the most progressive thing in my opinion. That's just my two cents on it, but I like it a lot as well.

---

<!--SEGMENT
topic: YouTube Channel Launch and Content Strategy
speakers: Alex, Brandon Hancock
keywords: YouTube, NotebookLM, OBS, CapCut, Spanish content, personal brand, video frequency, content creation workflow
summary: Alex (Spanish-language creator) announces the launch of his first YouTube video — a NotebookLM tutorial — using OBS for recording and CapCut for editing. Brandon advises publishing as frequently as possible (minimum once per week) to find breakout content, and offers to review the video with feedback on title and presentation.
-->

00:23:54 - Brandon Hancock
Alex, you're up next, man. What's going on?

00:23:58 - Alex
Hey, how you doing, guys? Really cool stuff, Mark. So yeah, on my side, I finally got to do some editing, learning, and launched my first video on the YouTube channel.

00:24:14 - Brandon Hancock
Hey, congrats. How can I find you?

00:24:18 - Alex
Yeah. I just shared it. It's a Spanish version of Brandon, but of course I'm starting with the very easy stuff. This is a NotebookLM [tool:NotebookLM] tutorial, following all your teachings from your personal brand AI, I think. Of course, you know, it was a lot of learning curve now. Let's see how it goes. I ended up doing OBS [tool:OBS] for recording and CapCut [tool:CapCut]. So I'm just editing myself just to get the flow and try to understand what's happening.

00:25:25 - Alex
So, what do you recommend in terms of flow? <Q>Because, like, of course, I have a lot of, like, 10 ideas of what could be my next ideas. What do you recommend — every week, every two weeks?</Q>

00:25:41 - Brandon Hancock
<A>No, great question. So, I mean, the short answer is just the more the better. Just because, like, what you're trying to do is just keep producing videos until something hits. And then once something hits and takes off, you're like, okay, well, like, I'm now fully vested in this topic, you know? ▶ 10 out of 10 would recommend just as many as you can — minimum one a week. If you can do more, fantastic. The first few videos are the hardest, and then eventually you're going to get to the point to where you can turn through much faster.</A>

00:26:22 - Brandon Hancock
I don't have time today, but tomorrow afternoon, I can do a quick little Loom video over it with just a few pointers. So just shoot me a DM to remind me, but yeah, I'd be happy to do a quick review with a few pieces of feedback on the video and title and all the stuff.

00:26:36 - Brandon Hancock
Congrats, man. The first one's the hardest. So you did it. That's awesome.

---

<!--SEGMENT
topic: AWS Airflow ETL Pipeline Deployment
speakers: Juan Torres, Brandon Hancock, Maksym Liamin
keywords: Apache Airflow, AWS MWAA, Amazon RDS, PostgreSQL, VPC, ETL pipeline, cloud infrastructure, Supabase, OBS, cost management
summary: Juan demonstrates a successfully deployed ETL data pipeline using AWS Managed Workflows for Apache Airflow (MWAA), connected to an Amazon RDS PostgreSQL database within the same VPC. He shares the key architectural challenge of VPC connectivity and warns that MWAA is expensive for small-scale jobs, making it unsuitable for cost-sensitive client deployments.
-->

00:27:06 - Brandon Hancock
Next up, Juan, what's going on, man?

00:27:12 - Juan Torres
Hey, I was able to successfully launch the ETL data pipeline through Airflow, Apache Airflow [tool:Apache Airflow], finally.

00:27:22 - Brandon Hancock
Hey, congrats. I know that is no small feat. There's a lot of moving parts to that.

00:27:27 - Juan Torres
Man, yes. So you were just talking about the permissions, the roles. I mean, that thing, I already figured that out. But the thing is that, essentially, if I actually may share my screen.

00:28:00 - Brandon Hancock
Yeah, just to share with everyone, in case you haven't used Airflow before, it's like the OG N8N [tool:N8N], meaning like, in the past when you wanted steps one, two, three, four, five to happen, Apache Airflow is like how you do it.

00:28:12 - Juan Torres
So this is hosted by AWS — it's called Managed Workflow for Apache Airflow [tool:AWS MWAA]. So this is actually managed by AWS. And so the launching of the ETL data pipeline in a local environment, it's not a problem really. It's really easy now with agentic IDEs to construct an ETL data pipeline that goes along with your front-end application. And then even able to connect it to the PostgreSQL database hosted in the cloud-based RDS environment with AWS was relatively easy.

00:29:00 - Juan Torres
But what's really hard is the connectivity between the two applications. The Airflow Web UI can be managed by an AWS managed VPC — a virtual private cloud. And this is like supposed to work in itself, but there's specific permissions that you have to give to your RDS PostgreSQL database. So what I had to do is move the Airflow Web UI, the Airflow environment, into a VPC that I was able to use. So the change in diagram is really this — so now instead of being in a different VPC, it's in the same VPC as my Amazon RDS PostgreSQL database. So they can connect directly.

00:31:03 - Juan Torres
Yeah, no, it's — and the reason that I wanted to do, instead of use Supabase, I wanted to use RDS, AWS directly, because I know that for future projects, I'm going to need the flexibility of having to work directly with AWS.

00:33:06 - Juan Torres
One last tip. So actually, this transformation, this whole cloud architecture, I'm going to have to overthrow it and reinitiate it just because Amazon MWAA Airflow Environment is quite expensive. So Airflow is a really great tool for carrying massive amounts of data, but it is not very affordable specifically for the kind of jobs that only have to extract hundreds, even thousands of data points. ▶ So this is the only limitation that I face with MWAA. But nevertheless, this is going to be included in the video because it is a really powerful tool. Just wanted to let people know the limitations of this tool, because it can be limited, especially if you want to give clients the possibility of not having to spend a lot of money in maintaining ETL data pipelines.

00:34:15 - Brandon Hancock
That is very cool. I've only had to use it when someone else was paying the bill. So I've never had to be like, oh, like, is this expensive? Good to know that it is actually expensive. So thank you for sharing that.

---

<!--SEGMENT
topic: WhatsApp Bot Scale-Up and Nissan Voice Agent
speakers: Maksym Liamin, Brandon Hancock
keywords: WhatsApp bot, Cloudflare Workers, Supabase, Voyage AI, Azure OpenAI, Azure Document Intelligence, voice agent, Nissan, Latin America expansion, dealership pricing, Next.js, Python worker
summary: Maksym reports winning a Nissan voice agent purchase order for appointment confirmation, while his existing WhatsApp dealership bot reaches 3,400 users and transitions to per-dealership pricing with Latin America expansion approved. He also describes a YouTube tutorial app he's building that demonstrates document processing with Azure Document Intelligence and Azure OpenAI, running on minimal infrastructure cost.
-->

00:34:38 - Brandon Hancock
I think next up is Maxim. What's going on, man?

00:34:41 - Maksym Liamin
Yeah, hello, hello. It's nice to see you all, guys. Yeah, so in my world — do you remember that I was telling you about some biddings that we had against a couple other teams for Nissan for like a voice agents project back in April? So we finally got a purchase order from them.

00:35:04 - Brandon Hancock
Hey, that's amazing, man.

00:35:06 - Maksym Liamin
Now we are just thinking like if we should take it because I mean we have this project and we really want to grow it and it has a lot of potential. So we just need to see if we want to split our attention on two different ones, but it's great. And I mean, we already have the prototype and everything is working. So now it needs to just in a sense scale.

00:35:26 - Maksym Liamin
Yeah, and for the other stuff, for the sales component, for the main WhatsApp bot [tool:WhatsApp], right now we are at 3,400 users. We're just a little past the last week. And we are switching the pricing finally in June because before we were on kind of a development budget. So we just had the money that we were given every month to develop the stuff. And now we finally started charging per dealership. So we're going to make much more money, which is great. And we also got the green light to go to full Latin America. So I don't have an exact date yet, but we already kind of agreed and now finishing all the legal stuff so that we can expand to everything besides Brazil and Argentina.

00:36:09 - Brandon Hancock
What's amazing — I mean, seriously, just always amazing, Maxim. What's so cool is like you're officially feeling the power of software, meaning like once the thing works once, it's literally just like add more. And it takes no extra work, pretty much no extra work, infinite scale, but a lot more money comes in. So it's an infinite money glitch when done well. And you're doing it very well.

00:36:31 - Maksym Liamin
Yeah, and the most fun part is that it runs on the $5 Cloudflare worker [tool:Cloudflare Workers]. And we use free credits from Supabase, free credits from Voyage AI [tool:Voyage AI], free stuff for other apps from Azure [tool:Azure]. So basically the cost is almost zero.

00:36:49 - Brandon Hancock
▶ What's wild is, yeah, your next expense might be upgrading to a $10 a month plan instead of five. But outside of that, yeah, like infinite scale, it's wild. What's really cool — I just wanted to share something. In real time, you were learning horizontal and vertical scaling, and you're doing it the right way because too many engineers are like, I'm going to scale to the moon. And they spend weeks building out all these Kubernetes orchestrations. And it's like, dude, just throw it on one computer and just pay 20 bucks a month, and it works.

00:37:50 - Maksym Liamin
I also brought another friend of mine here on the call. So he is also my neighbor. He lives here in Germany with me, basically. It's Alexander — they're on the call. I think the order will go to him and he'll present himself, but yeah, just wanted to let you know, guys, that it's one of my players.

00:38:42 - Maksym Liamin
Yeah, it's basically for confirming the appointments for test drive. So it takes a lot of human power to just confirm the appointments or if people have some questions that are very little. So the primary goal is just to call right after somebody booked it on the web page or anywhere else — from the social media form — to confirm it, and then maybe call them one day before and remind them. So this is kind of the main function.

00:40:17 - Brandon Hancock
<Q>Okay, no, that's awesome. Yeah, I think that definitely is going a little bit deeper just because voice agents — setting up the actual call infrastructure would probably be harder.</Q>

00:40:21 - Maksym Liamin
<A>Yeah, here the interface is harder than the actual development. Getting all the numbers. Getting all the compliance to make robotic calls. At least in America, there are quite a few applications that take time. They don't cost an insane amount, but they just take time to get approval.</A>

---

<!--SEGMENT
topic: AI Music Bot and Google Lyria Announcement
speakers: Alex (Alexander), Brandon Hancock, Maksym Liamin
keywords: Telegram bot, Python, Suno, Google Lyria 2, music generation, audio effects, AI music tools, Google I/O, Image Gen 3
summary: Alexander (Maksym's neighbor, new to Python) presents a Telegram music bot that searches songs by lyrics, creates playlists, and applies audio effects including remixing. Brandon connects this to Google's newly announced Lyria 2 music generation model from Google I/O, recommending it as a complementary tool for AI music experimentation.
-->

00:41:24 - Brandon Hancock
Alexander, if you want to hop on, welcome, welcome, man. How are you doing?

00:41:28 - Alex
Good evening, I'm Alexander, and I only start to do something with programming, so now I'm writing in Python [tool:Python], and in my studies in Germany, I learn only Java, and I'm very bad in Java, but I try to learn this language also, and I think Python is the best language for me now, and I try to write something in Python. For example, now I write a bot for Telegram [tool:Telegram], and...

00:42:24 - Brandon Hancock
<Q>What do you try to get the bot to do? Is it, like, use AI with the bot, or what are you thinking about doing?</Q>

00:42:33 - Alex
<A>Bots can use AI, yes. I try to make a music bot that can — for example, I can write some words from text from the song, and this bot can search the song, and then people can download, find text, make a playlist, also... I tried to make different effects on music. Now, today, I developed a new function. Now we can upload the sound and then do some remix with different options. Hi-fi, low speeds and other options. And this week or next week, I want to make an integration with Suno [tool:Suno], one AI for music. I want to connect with a bot for creating some music in this bot.</A>

00:43:55 - Brandon Hancock
Real quick, I just wanted to call out two things. Because I was watching the Google I/O today. And they launched a new thing called Lyria 2 [tool:Google Lyria 2]. I think this is — if you're kind of getting into AI and music — yeah, if you're just looking for more ideas, yeah, for whatever reason, it's not — I don't know why it's taking so long to come out, but it should be — yeah, Models, Lyria is their music one. Yeah, because they have Image Gen 3 [tool:Google Image Gen 3], which they made the third one. Then Lyria is their music one. But yeah, if you get a chance to watch the Google I/O event, you might get to see how they're doing it too. So just more cool AI tools to play with as you're experimenting. ▶ I'll drop a link in the chat so you can see this as well. [link:Google Lyria 2 announcement]

---

<!--SEGMENT
topic: ETL Pipeline and LinkedIn Career Visibility
speakers: Juan Torres, Brandon Hancock
keywords: OBS, LinkedIn, AWS, documentation, video content, job opportunities, cloud architecture, career development
summary: Brandon encourages Juan to document and publish his AWS infrastructure journey on LinkedIn and as a video, noting that the combination of ETL pipeline skills and cloud architecture knowledge creates significant job market visibility. Juan confirms he has been recording his work sessions with OBS for a future video release.
-->

00:32:29 - Brandon Hancock
▶ And seriously, like, the amount of job opportunities by being able to do this that you're exposing yourself to is insane. So, like, I know you're going a lot more on LinkedIn and sharing your journey and everything. This would be an awesome article. Like, just like, hey, you're just documenting your journey, posting it on LinkedIn and just almost posting it as, sharing my journey, but also sharing a couple tips for the next guy. I think you would start to see a lot of traction and potentially some job opportunities.

00:32:54 - Juan Torres
No, I've been documenting by recording my whole work through OBS. I'm going to be publishing a video once I'm finalized with the project.

00:33:06 - Juan Torres
Awesome. One last tip. So actually, this transformation, this whole cloud architecture, I'm going to have to overthrow it and reinitiate it just because Amazon MWAA Airflow Environment is quite expensive.

---

<!--SEGMENT
topic: Grant Writing Agent Architecture and Pricing
speakers: The Dharma House, Brandon Hancock, Jake Maymar, Bastian Venegas
keywords: Google ADK, grant writing, artifacts, RAG, document upload, MIME type, MCP server, Mistral OCR, Vertex AI, pricing strategy, NDA, non-compete, sequential agent, Gemini context window
summary: Aaron (The Dharma House) presents a grant writing agent project for a client, built with Google ADK, and seeks advice on three fronts: technical architecture for document upload and artifact handling vs. RAG, client pricing strategy for a complex open-ended AI project, and NDA/non-compete negotiation. Brandon recommends artifacts over RAG for single-use document processing given Gemini's 1M token context window, prices the project in the $20K–$30K range, and advises charging a premium for exclusivity clauses.
-->

00:01:14:27 - Brandon Hancock
Aaron, you're up next, man.

00:01:14:42 - The Dharma House
Hey, team. Happy, as always, to be here with you guys. I'm thankful that, Brandon, you're still doing it, especially given the transition you've had in the last couple of months.

00:01:14:27 - The Dharma House
I kind of had an opportunity to shift away from Eleanor based on an opportunity to build a tool for a client. You guys can help me walk through the process of it. So I had to sign some NDAs, so I got to be careful about what I can really talk about. But essentially, being asked — and right now we're just in the disco. The disco is always the fun part, right? Figuring out whether it's something that we can do or not. But being asked to create a grant writing agent using a company's process. Like, hey, we write, we think that our grants are better because we do A, B, C, D, and E to create an outstanding grant. And we're wondering if we can automate it.

00:01:15:37 - The Dharma House
So yeah, what I did was I did the disco with them last week, went back, and I went right to Google ADK [tool:Google ADK] and put it together and just kind of started to mock it up for myself. Here are a couple of things that I think are a little bit sticky. They want it client-facing. So as opposed to it being an internal tool, which for me makes more sense for them, they want to kind of create like a new division — they're kind of thinking about this being its own product and kind of running itself and just giving like a membership-based access to their team.

00:01:16:17 - The Dharma House
And two things. One, they don't know exactly how they want it to interface. And also, I could really use some support in figuring out how to set up a relationship with them. Because what they want is for me to create an agent. I kind of gave them a little — I mocked it. And the only trouble I had, technically — it's around artifacts and around Google ADK and document uploads. I'm not sure if anybody's run into that wall yet.

00:01:16:56 - The Dharma House
But they want, essentially, to be able to upload documents. And I wanted to do that without RAG — without a RAG-based system at all. It's really just pure uploading of documents and then getting a product. So that's one part of it. Two is I thought, cool, I'll build it. I'm not sure what to price it at yet, but I think it'll probably look something like I'll build it, I'll give you a license around it, and you can do whatever you want to do with it for MVP. And they came back and said, well, we want to own it. We don't want to license it. We want to work for hire, and you build it out, and it's our product. And I'm like, well, guys, it's an MVP, and it makes the most sense to keep us along the board.

00:01:17:56 - The Dharma House
And they're kind of like, well, also, we don't want you to be able to do anything like this for anybody else for a while. Like, we don't want you to rebuild our product.

00:01:19:42 - Brandon Hancock
Okay, so first I want to talk pricing, then NDA, and then also the technical piece. Okay, so first off, when it comes to pricing — not gonna lie, this is a bigger project. So I want to give like levels of complexity for pricing really fast, just as a rule of thumb.

00:01:20:12 - Brandon Hancock
If you're building something like super standard, like let's just imagine a RAG chatbot — custom UI, authentication, database, blob store — and they've already done some sort of prompting on their own to where there's no more extra thinking to do on my end, I pretty much just have to build the app — you know, I'd probably minimum like six, but I'd probably go closer to eight just because this is a two-weeks-long project.

00:01:21:00 - Brandon Hancock
All right, next level, which is like, hey, they have no idea what they want — to where you're not only having to be a software engineer, but you're almost having to be like, take their job and understand the process of writing it. Like, you're doing two jobs at that point — you're almost like an AI adoption consultant plus an AI engineer. For those types of projects, it's a lot more, strictly because you have to take in raw requirements, understand how their job actually works, and then implement it. There's probably a thousand small edge cases where they're like, oh, yeah, on these documents, you do this. And you're like, we've been working on documents together for a month, and you've never mentioned this edge case. ▶ For those, I mean, you're realistically like probably in the 20s, like just because of like, you're going to have to go be an employee almost.

00:01:22:30 - Brandon Hancock
▶ Anytime someone excludes you from the ability to do anything else in the future, I charge more. Because like, hey, like, yeah, I'm happy to do this just for you guys. But if you want me to be 100% exclusive, and I never have the ability to work on this again for an extra year or two, then we're going to have to pay more. So just framing it that way of just like, hey, this is limiting my earning potential, and I'm happy to do that with you guys, but for more.

00:01:24:10 - Brandon Hancock
The third question was around artifacts, right? Kind of with ADK. Artifacts are tricky. So I'm going to talk artifacts versus RAG. ▶ RAG shines when you're making queries to the same document multiple, multiple, multiple times. Going back to the RAG chatbot — if you're going to have a thousand users all asking questions about the same document, it makes so much sense to embed it and then reuse those embeddings. If it's kind of like a one-time thing of like, hey, we're making a grant around this PDF, I might ask 10, 20 questions, but then I'm done with that — I would stick to artifacts. I would not go RAG. And also when it comes to the Gemini models, you know, they can easily handle a million tokens. So you could easily fit the whole PDF in there.

00:01:26:01 - The Dharma House
Are we at the point yet where you think we could create an interface where I throw up a page and it looks something like a ChatGPT page and it just saves the different grants that they've had pushed out as kind of conversations? Or do I need to create text fields and text boxes and have them fill out some information and then upload?

00:01:27:00 - Brandon Hancock
<Q>How long is a grant just so we're on the same page before I give an answer? Three pages? Two? Ten?</Q>

00:01:27:02 - The Dharma House
<A>It can be. The biggest one I've seen so far is like 25. Their process — they're taking about 100, 150 pages to create that. They're pulling a lot of information from the org, from the nonprofit that they're working for, and they're pulling a lot of information from the funder, and then they have a process as to how to marry that information for a better acceptance rate.</A>

00:01:27:33 - Brandon Hancock
So the short answer is with artifacts, you could also start to generate the grant. And what's nice is you could almost chat against that artifact. The hard part is just doing that in a UI. Because like if it's two pages, you could easily show that in a UI. But the second you get to 25 pages, like just managing that — it's like if you had to code your whole project in one file. That's disgusting, you know?

00:01:29:01 - Bastian Venegas
<A>Yeah, yeah. I think the way that it should ideally be done is this tool should make sense that it would be an MCP server for the company. This is the kind of division where MCP — it's like you want to make your tools available to any agent or LLM that the user may have, and that includes tools like Cursor. So then the Cursor agent itself is like the one that does every tool and stuff, but also is the one that refines the outputs. And you can also go back in the chat and all of that, that makes the user experience easier. And there's a public open source repo that Vercel has with an awesome UI that I linked there.</A> [link:Vercel open source ADK UI repository]

00:01:31:28 - The Dharma House
Is there something I just don't understand yet about uploading and the process involved with uploading a doc and why this binary thing is even a problem in the first place?

00:01:32:47 - Brandon Hancock
<A>I mean, it should work. So that's why I'm like, as you are mentioning this, I don't know why it's not working. But specifically — when you're uploading files, they do need to be in a byte stream. But specifically, I'm saying what type they are to help ADK understand what it's working with. And this is what I did to get it to work. The MIME type would just change to application/PDF. So just out of curiosity, like if you swap to this approach, but just put application/PDF here, that would work.</A>

00:01:33:47 - Brandon Hancock
There's a term called callbacks, and basically what I was doing is I was instantly taking the image — in your case, the PDF — saving it locally so that later on I could load that PDF, the agent could load it whenever it needed it. That was my approach. So taking a PDF, save it locally. Then whenever an agent in the future needs it, cool, I just load that PDF as an artifact. The other option, the simplified version, was just to instead of saving it locally, then having the agent read it, is just instantly add it as an artifact.

00:01:44:15 - The Dharma House
I kind of work side by side on Thursdays with this team that has a graph RAG locally. I found a team that's built a graph RAG. And they're doing the same thing, something very similar, but they're doing it for the construction industry. And they're using Mistral's OCR parser [tool:Mistral OCR], because I guess it's really powerful. There's a cost to it, but it handles schematics and pretty much anything you throw at it very, very well.

00:01:35:44 - Jake Maymar
<A>You know, if you can figure out kind of what the budget is, what the long-term budget is, if you can take them to drinks or just go have a beer with them or whatever, that's super valuable because, you know, Brandon's totally right about like a $25K, $30K budget — that totally makes sense. But you could be leaving money on the table. Those grants are millions of dollars. And so, you know, the organization could actually be granted millions of dollars just to do exactly what you're doing. There's no reason to be greedy, but just see if you can get an authentic conversation because sometimes there's more money there than you realize.</A>

00:01:38:05 - Jake Maymar
▶ The culture of the client almost never changes. So how the client deals with you in the very beginning is exactly how the relationship is going to be. And you have to kind of decide, OK, I like that. Or maybe we'll sort of ride this out and see where it goes. But I've found that they rarely change. And so, you know, just kind of how they're treating you is how they're continuing to treat you. And that's how I would also price it.

---

<!--SEGMENT
topic: Voice Agent Persona Fidelity and Evaluation
speakers: Jake Maymar, Brandon Hancock, Maksym Liamin
keywords: voice agent, ElevenLabs, OpenAI Advanced Voice, Sesame, emotion modeling, persona fidelity, prompt engineering, evaluation, multi-model, Claude Sonnet, GPT-4o Mini
summary: Jake describes a complex chatbot project requiring multiple distinct personas that must sound like specific recognizable people, using a mix of Claude Sonnet, GPT-4o Mini, and GPT-4.1 for different tool calls. The main challenge is consistent emotional expression in voice — OpenAI Advanced Voice says emotions rather than performing them. Maksym and Brandon recommend Sesame as superior to ElevenLabs for emotional voice fidelity.
-->

00:46:25 - Jake Maymar
Okay, so not much to report. Still in the weeds. Making some good progress. Really looking forward to showing what I'm working on. It's a lot of, like, prompt engineering, which is kind of interesting. Like, really sort of dialing in the customization of the — I mean, essentially, it's just a chatbot. But the funny thing is really trying to dial it in and make it as accurate as possible, which is kind of interesting.

00:47:04 - Brandon Hancock
<Q>Which model are you using right now?</Q>

00:47:07 - Jake Maymar
<A>Well, it's kind of interesting. It's a whole bunch of different models. Some of it is Claude Sonnet [tool:Claude Sonnet]. Some of it's GPT-4o Mini [tool:GPT-4o Mini]. Some of it's GPT-4.1 [tool:GPT-4.1]. I mean, I'm using different models for different, like, sort of tool calls, essentially, and cost and performance. One of the biggest problems is performance. And trying to figure out how to kind of sort of clean up the process so I don't have to use as many models.</A>

00:47:45 - Jake Maymar
But right now we're just trying to get it to — it's fairly complex. And the whole point is to sound not like one person, but sound like a collection of people. And those people are actually vetting the process. So it's actually hard because it's not me vetting. It's like, well, it sounds like that person. But then when you give it to that person and they run through it, they're like, well, it doesn't sound like me.

00:48:27 - Jake Maymar
It's sort of like a support group, where you go and you talk to these people and these people are very recognizable. And so they have a certain sort of personality and profile and just the way they interact with the individual is very recognizable. And so it's a group of people, and that's what's actually really hard. If it's dialed into one person, that's not easy, but it's fairly doable. It's just trying to get a full separation of the people.

00:49:24 - Jake Maymar
There is a voice element to it, like an ElevenLabs [tool:ElevenLabs] kind of thing. But even that isn't really doing what we want. <Q>Actually, love to know if anyone has success with emotions, doing voice and emotions.</Q>

00:50:00 - Brandon Hancock
<A>Not Sesame, Richard. I was thinking Richard — he is probably the most experienced when it comes to doing anything with voice. He's experimented with all of them. He's done ElevenLabs, he's done OpenAI [tool:OpenAI Advanced Voice], and he's experimented with one other one. And then Sesame [tool:Sesame]. Sesame is another tool that is also super, super powerful. Would 10 out of 10 recommend — I saw a demo of it, but I haven't got to play with it. But those are the three right now. From my understanding, he ended up going with OpenAI. I think he had the best luck with OpenAI.</A>

00:51:00 - Jake Maymar
Yeah, the thing is, we are using OpenAI Advanced Voice. But it's not doing the emotions. It says the emotions, but it's not consistently doing the emotions. That's a problem. Like we want it to actually act a certain way. But a lot of times it will sometimes act a certain way, but sometimes it will say, "I'm sad." The person acts, you know, and it will basically say the emotion that it's supposed to be doing.

00:51:36 - Maksym Liamin
<A>Yeah, actually the Sesame that already got mentioned is very good because we right now — like the demos that we have, it works with ElevenLabs. And I mean, it's pretty good. But if you compare it to Sesame, it's not even close. Yeah. So it transfers emotions like really, really well. ▶ So I would recommend test it out if that's the important part.</A>

00:51:54 - Jake Maymar
Yeah. Yeah. We definitely have that on the list. So let me try that out. Thank you. That's very, very helpful.

---

<!--SEGMENT
topic: AI Research Dashboard and Slide Generation
speakers: asako, Brandon Hancock, Bastian Venegas, Maksym Liamin
keywords: Google ADK, LLM multi-model, Google Slides, Crunchbase, BrowserBase, Tiptap, React PDF Highlighter, co-pilot UI, hallucination reduction, content generation, Japanese AI startups
summary: Asako presents a dashboard automating AI startup research content — pulling URLs, passing to multiple LLMs to reduce hallucination, and generating articles, Google Slides, and social media content. Key challenges discussed include AI slide generation complexity, adding a co-pilot chat interface for iterative edits, and implementing text highlighting with comments using Tiptap or React PDF Highlighter.
-->

00:54:26 - asako
Yeah, so I have two projects. One is the one that Brandon just mentioned. I'm going to share my screen. Yeah, so I started building a dashboard for my research work. What I'm doing right now is to provide an article, Google Slide [tool:Google Slides], and then social media contents for investors who are interested in AI startups, so I'm making those contents about AI startups, but right now there are a lot of manual work, like copy and paste company information from spreadsheet and then copy and paste prompt from Google Docs. And so I want to automate everything, and then eventually I want to sell the system to my employer.

00:55:31 - asako
Yeah, so it's Japanese, so you maybe have to understand, but it will pull all the URL and then pass those information to LLM. And then my employer wanted to use multiple LLMs to avoid hallucination, so generate output from multiple LLMs and then combine those. And then based on the generated combined report we are making, I want to make an article in Google Slide and in social media content.

00:56:13 - asako
Yes, but I'm thinking about three steps for this project. For my MVP, I want to focus on text content generation. And then for the second step, I want to generate slides. And then third, as a third step, I want to retrieve company information automatically using agent. For example, if you put the company name and it will pull funding from Crunchbase [tool:Crunchbase] and then something like that.

00:56:51 - asako
And text content generation seems to be pretty straightforward. But I feel like slide generation is hard. Like how to get the images and then format, like crop and scale so that it will fit in the template.

00:57:20 - asako
And then Bastian actually suggested me to use BrowserBase [tool:BrowserBase], which is like a computer use agent. So I'm thinking about playing around with it to do that.

00:57:36 - Brandon Hancock
No, that's awesome. So a few just like ideas. So I have looked at a bunch of like AI slides because I just needed to make a bunch of like presentations. I have yet to find one that does a good job. Like, so I'm curious if anyone has any like AI slide tool that they've used that does good work. I mean, I'd be curious to see it and try it myself. But I feel like if, once someone does crack that code, it's going to be wild because the amount of people that have to make slides for presentations — I mean, professionally and for side projects and everything — it's wild. So if you do find a good one, let me know. I just haven't seen one yet.

00:59:00 - Brandon Hancock
I did — this is like not 100% what you're trying to do, but like maybe a PowerPoint assistant you could look at doing. There was a demo from ADK where they added a browser agent to their agent so they could just chat and then the agent would go off and do stuff on the internet and report back. I'll have to find it and send it. Basically, what they did is they used ADK to control a browser agent. So in that one, they used Selenium [tool:Selenium], but you could also replace Selenium with BrowserBase, and it would still be just as powerful. ▶ So definitely recommend, like, if you're starting to go down the agent and browser path, that's a really good video to get started with, if you want to combine the two.

01:00:55 - asako
I actually have two challenges. One is that right now I'm doing just pass the prompt and then generate the output, but I want to make it more conversational so that if there's anything that I want to make adjustment, I can ask AI to modify.

01:01:18 - Brandon Hancock
<A>So there is a concept called just an AI co-pilot, and basically it's to do exactly what you're describing. So I think it'll become more of a common thing in applications going forward, but basically it's like making the side dashboard a co-pilot — specifically like allowing whenever someone clicks on anything to ask questions about it in the sidebar and make changes. The thing that's going to be hard about that is you have to start sharing global state across components, but it is doable. Like what you could do is probably add a third button, which is just like a little AI robot. And that just brings over a side window from the right that is just an agent, a chat to where you can say like, hey, I like this, I like where it's going, but I want to incorporate this feedback.</A>

01:02:28 - asako
And then the last question is that in Google Docs, it's easy to add comments, like if the editor wants to change specific wording, it's easy to point out, but with the dashboard, I feel like it's harder. <Q>So what is the best way to add comments?</Q>

01:03:37 - Brandon Hancock
<A>So, going down that approach, you have to start to use, like, an actual text editor, like, because right now it's just text. But you want to actually put a text editor in there. There's a framework — Maxim just raised his hand. Maxim, do you remember the framework?</A>

01:04:19 - Maksym Liamin
<A>Yeah, it is. So there is a great library that we use with Andrew for our project for exactly doing the highlighting and commenting stuff. It requires a little bit more setup than the frameworks that Brandon is looking up, because there I believe it at some point becomes paid, especially if you want like nice comments and all this kind of stuff. But if you needed more kind of simple and more control, the library is called React PDF Highlighter [tool:React PDF Highlighter]. And it's very easy to build on top of it, like whatever you need. It's very easy to integrate. I will share the link as soon as I find it.</A> [link:React PDF Highlighter library]

01:05:23 - Brandon Hancock
<A>The company I worked at, TypeShare [tool:TypeShare], that's what we used because we were allowing people to manually write blog posts, and when writing blog posts, you need to highlight, underline, basically feel like you're in Microsoft Word, but in a text editor, and it also had the ability to comment, and then you could make custom nodes, which would be like a comment. So you could do all of that. ▶ Tiptap [tool:Tiptap] — you can do literally anything in there, which is nice. So we definitely recommend, if you want to go super custom, Tiptap.</A>

01:06:18 - asako
Yeah, oh, and then lastly, it's an advertisement, but I launched a podcast website, which was built with AI, two AI bilingual agents, and a new episode will be launched tomorrow, so I'm going to drop the link. [link:asako's bilingual AI podcast website]

---

<!--SEGMENT
topic: Medical Billing Automation with N8N Cron Jobs
speakers: Nate Ginn, Brandon Hancock, Bastian Venegas
keywords: N8N, cron job, Google Sheets, SendGrid, Mailgun, MedGemma, HIPAA, local LLM, medical billing, automation, Python
summary: Nate, a doctor returning after a break, asks about automating his medical billing workflow — specifically scanning a Google Sheet for missing billing codes and sending reminder notifications. Brandon recommends an N8N cron job workflow as the simplest approach, while also highlighting Google's newly announced MedGemma model as a locally-runnable, HIPAA-friendly medical LLM worth exploring.
-->

01:07:59 - Nate Ginn
Hi. It's been a long time. What's going on? Yeah, I was, I just had to go to the office for a little bit, but anyway, I unfortunately haven't been doing a lot of programming. It's funny when you step away and you're not doing this as a profession, right? This isn't my thing. I'm like, oh, man, I have to relearn the language again, almost. And all of these new things you're talking about, I'm like, oh, man, I missed out. But I just missed hanging out with you guys, and I just wanted to say hi.

01:09:00 - Brandon Hancock
Well, hey, no, we always love seeing you, Nate. If you, I'll give you a quick update on things that I think you would like to see. So, crank it — not websites. So at this point, Firebase just said today that they're going to make Firebase Studio actually finally work, meaning you now can actually deploy it back in. So the next time you want to go to create like a full stack AI application, hopefully by the time you do that, Firebase Studio will actually do the thing it says it's going to do.

01:09:33 - Brandon Hancock
Other just cool things. I don't know if you've got to play with Lovable for cranking out a website. I'm still blown away with how easy it is. ▶ New way to like rapidly go through projects, guys, is like take the requirements document you make with your client or yourself and then a few Excalidraw [tool:Excalidraw] mockups and Lovable just cranks it out.

01:11:09 - Brandon Hancock
Google announced today their new Gemma model — I think they have a specialized medical one. You might want to look into it a little bit more, but you might be interested in running that locally. I'd be curious to see if you notice it does better work than some of the more open ones when it comes to answering medical questions. Yeah, it's called MedGemma [tool:MedGemma]. It's like focused on anything from medical questions. Apparently it's probably one of the best medical models that you can run privately. So you're not having to share data to the cloud, which is like an insane use case. ▶ That's going to be insanely valuable to use.

01:12:18 - Nate Ginn
<Q>That one — if you go in there, it's not capturing your data that you're asking. Is that what you're saying?</Q>

01:12:26 - Brandon Hancock
<A>More specifically, you actually will be able to — it's a model that you can run locally. So just like Llama [tool:Llama], like you can run locally on your computer. Or I think what they're recommending is like, as you deploy more HIPAA-compliant — like if you go cloud, you can just run this one. So the data never leaves.</A>

01:49:42 - Nate Ginn
I know it's getting late here, but so I — the program I wrote a long time ago that does my billing coding, it essentially puts everything into a Google Sheet program. Now I want to be able to go and extract that data. Like for instance, let's say I forgot to do my note for a day, so my line on — like Brandon Hancock came to see me, and there's no codes in there because I didn't finish, right? <Q>I want to be able to get to a point where it searches through the entire database looking for empty spots, and then essentially what would be great is it sends some kind of message to me, the provider, like whether it's an email or a text or something like that saying, hey, here's a list of all of the empty spots we have for you — extract the date of service, the patient name, and then send it to the patient.</Q>

01:50:47 - Brandon Hancock
<A>What you could actually do, even simpler, there's a term called a cron job, and basically what a cron job does is it says, hey, at this timestamp, perform this function. So in your case, you could get it done with a Python script, which is pretty nice because you don't even have to touch AI. And what it would do is like, okay, pull down Google Sheet, filter for all client meetings today where row is null. And then it would just say, okay, Brandon Hancock did it, Carly came, she also came in, no codes yet. And it would just — you could use a tool like SendGrid [tool:SendGrid] to send you, or Mailgun [tool:Mailgun] — there's plenty of mail tools that would just shoot you an email and say, client name needs attention.</A>

01:51:49 - Brandon Hancock
<A>▶ And Bastian also brings up a good point too. N8N [tool:N8N] might be the easiest way to do that, actually, because it's deployed, it runs 24/7, and all you have to do is just say, pull Google Sheet, run Python, send email if stuff was empty. You could probably get it done in four nodes.</A>

01:52:10 - Nate Ginn
<Q>What would you suggest for me to learn more about N8N? Because I have been watching a ton of videos lately. But everybody's using N8N, and my knowledge on it is what I've heard here.</Q>

01:52:31 - Brandon Hancock
<A>▶ Yeah, I mean, honestly, I think the easiest way to do it is just to start — like, literally just use it. Like, it is actually that straightforward. Just say, like, hey, here's what I'm trying to do. Please help me make an N8N workflow that does this. And it'll tell you the nodes, the connections, and the Python script. And that — like, I mean, seriously, like, if you tonight drank a cup of coffee, headphones on, you could build it tonight. So for N8N, it's so simple to use, I wouldn't need more tutorials. I think you could just get that set up.</A>

---

<!--SEGMENT
topic: ADK Career Pivot and Job Market Advice
speakers: Bert, Neel More, Brandon Hancock
keywords: Google ADK, LangChain, LangGraph, Azure AI, Vertex AI, MLOps, LLMOps, agent architecture, career transition, data engineering, fine-tuning, Azure AI Fundamentals certificate
summary: Bert (data engineer pivoting to ADK development) shares how Brandon's masterclass helped him debug a Google ADK sample repo bug involving agent-as-tool wrapping, and reports LinkedIn recruiter interest after updating his profile to highlight ADK skills. Neel (20-year MLOps veteran, recently unemployed) asks which agentic AI framework to prioritize for job hunting; Brandon recommends LangChain for corporate roles due to its foundational coverage, but pivots to Azure AI infrastructure for AI architect roles, noting Azure is commercially dominant.
-->

02:01:20 - Brandon Hancock
Bert, you're up next, man. What's going on?

02:01:25 - Bert
Oh, cool. So thank you so much, Brandon. I really appreciate being here on the masterclass and being able to absorb knowledge from a lot of very experienced individuals. So my journey is that I just started doing ADK maybe about six weeks ago. Just started like roughly dabbling it. But it wasn't until I found your masterclass last week, your three-hour masterclass, that I really started really getting into the whole ADK thing. So I've basically been watching it like every day for the last like seven days, especially like the second half of it where you go over like state, multi-agents and everything.

02:02:02 - Bert
So even going back to Google's own developer course that they had with getting ADK fundamentals, just by watching your class, I was able to find like a bug and debug it because — so yesterday when I was running the thing, I got this error over here. The reason why I got that error is because my spidey senses started going off. And the reason was because they didn't wrap this tool here. You said that never use an agent that uses a built-in tool as a subagent. So in the original code base, which is still on GitHub — I'm not trying to shame anybody here — they have the script agent here. Because of watching your videos, as soon as I got that error and I looked at the tool saying, oh, that's kind of suspicious, I was able to wrap that in front of that agent tool and move on.

02:04:03 - Bert
So I myself am trying to pivot from being a data engineer into being an ADK developer. As I mentioned, I've just been going over the last week really, really getting into the fundamentals of like the callbacks, the states, like how to use the runners as opposed to ADK web. So I really appreciate your masterclass video as well as the knowledge of this mastermind group as well.

02:04:28 - Brandon Hancock
No, that's awesome. Hey, thank you so much for all the kind words. And love that — like, I mean, you're a contributor now. Like, I mean, the thing — ADK is so new, like there's certain things like you probably know more than me on certain things because it's so new and there's so many edge cases and everything. So I love that you're taking it and running with it and building full things.

02:09:05 - Bert
And just to let you know that on LinkedIn, I put down that — because basically I'm in between jobs right now — so on LinkedIn, my current job is I just put down "sabbatical, upskilling on ADK," and just wrote down using my knowledge as a data engineer, using DAGs and everything, plus using my previous knowledge as an engineer working with web sessions in the background. Like we're merging those together for ADK. And I've already got like a couple of bites of recruiter just reaching out to me saying like, hey, we're looking for somebody who's doing ADK, like proof of concept. ▶ So just to show you that a lot of the stuff works that you're sharing with us today.

02:09:42 - Brandon Hancock
That's amazing.

02:09:53 - Neel More
Hi, Brandon. I got a quick question. Sorry, it's late night here, so my camera's not there. And it's a very, very basic question. I have started with the agentic AI. I have seen your agentic AI courses, especially with the LangChain [tool:LangChain]. And I have seen then you move to the Crew AI, and then you are, right now, you are working on the ADK. <Q>So as for the new guys, what will you suggest to start with, because I know LangGraph, you got the basic clear, but I want to get it more good in the agentic AI within the next one or two months at the max? And what is your suggestion?</Q>

02:00:33 - Brandon Hancock
<A>No, awesome question. So quick clarifying thing — are you looking like, what are you looking to do? Like, okay, let's just fast forward two months. Like you said, like, you know, say you just know you're an expert at AI. What are you looking to do next? And then we can work backwards.</A>

02:00:53 - Neel More
Okay, so I'll give my background. I lost my job like six months back and I'm more into like — I got 20 years of experience. I'm very good at the MLOps, so I know about the data science part, and I was just missing about this agentic AI when it came to the autonomous agent, right? So I want to add on top of my skill set the agentic AI. That's my core aim. And later on, what I want to do is to integrate this thing into the data science flow, right? How it can help with the MLOps or with the LLMOps. That is the intention where I'm going. And the two months, because I can prepare for the interview — so that's one of the goals.

02:01:37 - Brandon Hancock
<A>I gotcha. Okay, so if the goal is to get hired, from what I have seen, a lot of companies like LangChain and LangGraph, because it's very, very technical. I've seen a lot of that. For more personal projects and small business applications, I do think ADK right now is my favorite out of all of them. But if you're looking at getting experience to land a job at a corporate company, LangChain seems to be the best one. It really comes down to — LangChain at this point is just a wrapper around all things AI, meaning you're going to learn with LangChain all about embeddings, chunking, how to integrate to vector stores. By learning LangChain and building things with it, you will ultimately learn all those underlying skills, which is nice because Crew AI and ADK take away all of that, because they make it so easy to where all you're really doing is just passing in a prompt, making a few Python tools, and the agents handle the rest of the complexity for you. Whereas with LangChain, you're almost dealing with the raw underlying concepts, which is probably more appealing to an employer.</A>

02:01:41 - Neel More
Yeah. All right. Cool. Yeah. Thanks, Brandon. So if I got any questions — I'm just wondering what's the best way.

02:01:47 - Brandon Hancock
<A>If that's the case — you might not want to go as much LangChain. What you might want to do is go and just pick an infrastructure, like a cloud platform. It looks like commercially Azure [tool:Azure] is winning right now. And I would focus on building some sort of Azure course, infrastructure course, where you're going to learn about creating — where you're going to learn about how you can deploy your own LLMs, interface with them in Azure. You can also search — Azure is rolling out their agent foundry [tool:Azure AI Foundry]. So that's a great way to learn how to work with deployed agents. ▶ I would mix AI with a cloud infrastructure platform and Azure is winning from what I've seen commercially. Microsoft, they have a certificate for Azure AI Fundamentals [tool:Azure AI Fundamentals certificate]. That might be something nice to go deep in on.</A>

---

=== UNRESOLVED SPEAKERS ===

- **twell** — appears briefly at 00:49:53 with a single utterance ("I would say, okay, I cannot, what's right? Sesame."); no canonical name found in alias map.
- **asako** — used as-is; no canonical full name provided in alias map.
- **Bert** — used as-is; full name confirmed in transcript as Robert Chirwa, but raw speaker label is "Bert"; listed here as the alias map did not contain this mapping.
- **The Dharma House** — used as-is; Brandon addresses this speaker as "Aaron" during the session, but the alias map did not contain a mapping from "The Dharma House" to "Aaron."
- **Alex** — two distinct speakers share this raw label: (1) the Spanish-language YouTuber (first appears ~00:23:56) and (2) Alexander, Maksym's neighbor in Germany (first appears ~00:41:28). These could not be disambiguated from the alias map and are passed through unchanged.