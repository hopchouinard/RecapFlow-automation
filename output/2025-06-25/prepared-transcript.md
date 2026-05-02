=== SESSION ===
date: Unknown (Tuesday, mid-July estimated)
duration_estimate: ~2 hours 34 minutes
main_themes: RAG architecture and chunking strategies, vector store selection (Supabase vs. ChromaDB), Google ADK integration with Next.js/FastAPI, browser automation limitations, AI personal branding, Cursor/Claude Code AI-assisted development, Limitless pendant for productivity, community project showcases

---

<!--SEGMENT
topic: Pre-Call RAG and LocalGPT Discussion
speakers: Paul Miller, alexrojas, AbdulShakur Abdullah
keywords: LocalGPT, RAG, Dockling, IBM, MLX, open source, Mohamed, Prompt Engineering channel, PDF parsing, semantic chunking
summary: Before the formal call begins, Paul Miller describes his collaboration with Mohamed (PhD, Prompt Engineering YouTube channel) on LocalGPT v2, an open-source RAG project. The group discusses Dockling as a multi-format document parser from IBM, its local GPU/MLX support, and the challenge of keeping up with the pace of AI tooling. This segment establishes the RAG theme that recurs throughout the session.
-->

00:01:00 - AbdulShakur Abdullah
Hey, Paul.

00:01:39 - Paul Miller
Hey, guys. Hey, Abdul.

00:02:03 - alexrojas
<Q>How are you doing with the hybrid model for the Congress documents?</Q>

00:02:14 - Paul Miller
<A>Oh, well, I reached out to — what's his name? The guy that runs the Prompt Engineering channel. I don't know if you know that video channel. The guy behind it is Mohamed, and he is really at the cutting edge of a lot of AI stuff. And he's got a thing called LocalGPT [tool:LocalGPT], which is an open-source RAG project, and they're about to release a version two. He was looking for people that want to do niche things in that space, and I have some ideas on one of the things I'm trying to do, so I'm going to collaborate with him on it.</A>

00:03:11 - alexrojas
Nice. LocalGPT?

00:03:12 - Paul Miller
▶ Yeah, so look up LocalGPT. I'll post the video. He's talking about the version 2, which uses the search tool that Brandon was talking about last time.

00:04:03 - Paul Miller
Yeah, he's like a PhD in data science and AI, so he knows his stuff. So he's been developing it as an open-source project, LocalGPT.

00:04:23 - alexrojas
Yeah, I see that the GPT 2.0 is coming, right?

00:04:33 - Paul Miller
▶ What I liked about his video was he talked about not just preparing the data and putting it into the RAG, but how you validate that you're not doing searches incorrectly and how he sort of cross-checks the testing of that. The thinking that's gone into it is really, really impressive.

00:05:04 - Paul Miller
And it's an open-source project. So what you could do is potentially go in and change it as you see fit.

00:05:20 - alexrojas
Been working this week a lot with RAG, so this is going to be very useful.

00:05:25 - Paul Miller
Yeah, so the version 2 comes out in the middle of July, according to Mohamed.

00:05:53 - Paul Miller
So essentially, he's using Dockling [tool:Dockling] for — he's focused on all the initial imports being PDFs, but the benefit with Dockling is that it can read all sorts of file types.

00:06:10 - alexrojas
<Q>And Dockling is open source, right?</Q>

00:06:12 - Paul Miller
<A>It's free. You could host it locally. Yeah, from IBM [tool:IBM Dockling]. And if you run a Mac, you can get it to run on the Mac's MLX local processing. If you've got a GPU, you can do it on that, or you can run it on CPU.</A>

00:06:44 - AbdulShakur Abdullah
Yeah, that's why this group is good. I always come and leave with lots of homework.

00:07:06 - Paul Miller
You don't want to look at something that's rubbish and not going to solve the problem.

00:07:16 - AbdulShakur Abdullah
I found even trying to keep up with all the things that you guys are already into and falling behind.

00:07:23 - Paul Miller
I'm many, many weeks behind. I just have to pick what's going to pay the bills, let alone all the stuff that's really cool that I'd love to have a play with, like some of the video stuff looks really neat, but I just don't have time for that.

---

<!--SEGMENT
topic: Session Kickoff and Host Updates
speakers: Brandon Hancock, Paul Miller, alexrojas
keywords: Fathom, CrewAI, ADK, LangChain, ShipKit, Zhuo interview, scuba certification, product coaching platform
summary: Brandon opens the formal session, shares updates on a pending interview with Zhuo covering CrewAI vs. ADK vs. LangChain use cases, and introduces ShipKit — a product coaching platform with templates and example projects. He also shares personal news about scuba certification. The segment sets the agenda for the round-robin discussion format.
-->

00:08:04 - Brandon Hancock
What's up, everybody?

00:08:41 - Brandon Hancock
Hope everyone's having an awesome Tuesday so far. A few quick updates for you. So I just got the video for the interview with Zhuo just sent over like a few minutes ago. Waiting for the thumbs up from Zhuo to publish that.

00:09:00 - Brandon Hancock
Fathom [tool:Fathom] has recorded hundreds of calls for me, and it will always do video. On this one, it didn't. All it did was screen share. ▶ Always have a backup is the main lesson learned.

00:09:20 - Brandon Hancock
Joy talks about a ton of cool stuff. I asked all the questions you guys asked, like when CrewAI [tool:CrewAI] versus ADK [tool:Google ADK] versus LangChain [tool:LangChain] use cases. How are people using it in the real world? How are people actually making money with it? How are big companies using it? So I asked all those, learned a ton of cool insights that I actually didn't even know they were working on. Super pumped for that to come out hopefully in the next few days, as soon as Zhuo gives the thumbs up.

00:09:56 - Brandon Hancock
Outside of that, I've been insanely busy with family stuff and working on ShipKit [tool:ShipKit]. So that's the new product coaching platform I'm working on for you guys. Almost done with the first template. So there'll be three templates and three example projects. So all in all, there's going to be a ton in there. Just literally coding as fast as I can to get that out for you guys.

00:10:14 - Brandon Hancock
And final update, just random topic — in the middle of getting our scuba certification. We did it all Saturday, all Sunday from like nine to five. And the second you're done, you just pass out. We have our final dive test this Saturday and Sunday, and then I'll be back to a regular schedule.

00:11:00 - Brandon Hancock
If you haven't been on the call before, the way we usually do is I just go round robin based on that call order in the chat. Basically the way we go is we usually share, like, if there's a question you have or if there's something cool that you're working on that you think the group would find interesting, feel free to drop it in.

---

<!--SEGMENT
topic: Alex's Legal RAG Application Demo
speakers: alexrojas, Brandon Hancock, Juan Torres, Paul Miller, Bastian Venegas
keywords: RAG, legal app, Supabase, Next.js, Chunky, semantic chunking, Gemini embeddings, PDF parsing, Mexico City civil law, background worker, Dockling, exponential backoff
summary: Alex demos a RAG-based legal consultation app covering Mexico City civil law, built with Next.js and Supabase, using Chunky for semantic chunking at 500 characters and Gemini 768 embeddings. The group discusses PDF parsing challenges, background worker architecture for chunking, rate limiting with exponential backoff, and the app's monetization strategy targeting law firms. Brandon recommends a job-queue pattern with Dockling running in a Docker/Python background worker.
-->

00:13:13 - alexrojas
So this week I've been — I'm about to release the video on YouTube — but also I've been working on the RAG legal application. I could actually show you guys.

00:14:15 - alexrojas
This is my legal RAG app. So as of now, you just enter — I have it locally now. It's in Spanish. It focuses on civil rights in Mexico City. So everything from the Constitution all the way to local laws, state level, local level. Here you can see in documents it has like eight main documents. This is the Constitution, and then it goes all the way local.

00:15:36 - alexrojas
Here, if you put — you can upload more documents. It tells you which type of documents. Here you just put like Mexico, if it's nationwide, then Mexico City, and then state of Mexico. And here you just choose if it's like an international treaty, a federal law, a local constitution, like all the different types of laws.

00:16:03 - Brandon Hancock
<Q>So out of curiosity, what did you end up using to chunk everything? What did you end up going with?</Q>

00:16:11 - alexrojas
<A>Okay, so it's a Supabase [tool:Supabase], Next.js [tool:Next.js] app, and then it connects to my Supabase. And I did use Chunky [tool:Chunky]. I did some tests and the semantic chunking of Chunky was very efficient. I think I went to 500 characters per chunk. I did 1000 and then a bit smaller and 500 was like the sweet spot. And then I used Gemini [tool:Gemini], all around Gemini 768.</A>

00:16:48 - Brandon Hancock
<Q>When it does come to running Chunky, are you doing that in like a background worker? How do you have that running?</Q>

00:17:00 - alexrojas
<A>It's a background worker. It's like right here in Cursor [tool:Cursor].</A>

00:17:07 - alexrojas
You know, I got to say that for the first time, I understand you, Brandon. It's impressive, like how working with the tabs and really just like, hey, I want to make this happen. And you just see like the matrix happening.

00:17:31 - alexrojas
The video of Andrej Karpathy [tool:Andrej Karpathy video] — he says that he's the one who came up with the vibe coding concept.

00:17:49 - Brandon Hancock
So the reason I asked about chunking is — the second you start to deal with PDFs, usually once you deploy it to Vercel [tool:Vercel], it usually will go past the timeout. So that's why I was curious how you were tackling taking a PDF and chunking it.

00:18:08 - alexrojas
Yeah, so the first is TXT, the easiest. And then I did struggle with the PDF. I went through many PDF libraries, and I think I ended up with PDF Parse [tool:pdf-parse]. But I did struggle a lot, and my conclusion was — try to get them in TXT when I'm going to do a deployment.

00:18:55 - Brandon Hancock
▶ The main approach I'd suggest right now is actually having one central place — a database and a blob store. The blob store is going to save your PDFs. Then from there, every time you upload a document, it creates a processing job. And then you have a background worker who is running and all it's doing is looking for incomplete jobs. It takes that PDF and then it runs everything needed in Python to actually chunk it. So that's where you can use Dockling and/or Chunky — just let it rip and do its thing in Python.

00:19:55 - Brandon Hancock
▶ The two main suggestions: the easiest way to spin it up is to create a Docker container where it just has one main Python function that handles it, and then it just, next to your database, looks for jobs, works on jobs, puts chunks back in database. Doing it on Railway [tool:Railway], what you'll find is when you deploy it, it's going to be super slow, because Railway does not have a GPU, so you usually want to deploy to like a Google Compute Engine [tool:Google Compute Engine] to where you have access to a GPU, and it'll go through it in seconds versus minutes.

00:21:02 - Brandon Hancock
Yeah, Juan, if you want to go real fast and then I can pull up the code while you're asking.

00:21:08 - Juan Torres
<Q>Yeah, I just wanted to ask if it can create contracts, for example, for servers, contracts or lending of equipment contracts, according to Mexican law.</Q>

00:21:19 - alexrojas
<A>Yeah, that's exactly where I wanted to ask the flow because I have a meeting this week with my friend, a lawyer. As of now, we have the solution of consult, which is just a normal RAG. And I'm thinking of adding functionalities — that's one of the functionalities. I think I would need to make another corpus of information that is solely in contracts. I can see now that I'm going to need an agent for research and an agent for a contract.</A>

00:22:15 - Juan Torres
I'm going to be building those contracts. So if you want to use me as a guinea pig, I'll be happy to.

00:22:30 - Paul Miller
<Q>Alex, this is really cool. How are you going to monetize this? Do you have an existing client?</Q>

00:22:40 - alexrojas
<A>So as of now, I have a friend who works in a big lawyer firm. Initially, what I want to work out with him before doing the sale is to try to solve the pain point. When I'm with this MVP that I have now, I can say like, hey, tell me, what do you deal with that's very painful every day? So I'll just adapt it to — what type of law do you check every day? And then maybe focus on that one. Once I get the feedback from him and kind of add that functionality, maybe think about, hey, talk to your boss, let's make this product together so that it actually adds value and your firm is willing to pay for it. So it's more of a custom solution. That would be like my monetizing plan.</A>

00:23:48 - Bastian Venegas
▶ A quick comment about rate limiting — you can look into exponential backoff. Basically, you can make more API requests within a defined time frame. For example, in a minute you will get to make more API calls if you use exponential backoff versus if you just set up, like, wait five seconds after each call.

00:24:37 - alexrojas
Yeah, so I do an initial chunking and embedding, and as needed — let's say there's another reform or an update — it will just get updated, but maybe not replace any of the previous, but just add on top of it.

00:25:00 - Bastian Venegas
Not like a daily update thing. It's more like every few months, maybe once a year.

00:25:07 - Bastian Venegas
▶ Chunking is not a big issue once you already have everything with your base legal corpus. You kind of go through it once and you're off the hook.

---

<!--SEGMENT
topic: Background Worker Architecture and Supabase Vector Store
speakers: Brandon Hancock, Marc Juretus, alexrojas, Juan Torres
keywords: Supabase, ChromaDB, Drizzle ORM, vector store, background worker, Docker, Python, pgvector, migrations, schema, embeddings, Next.js, FastAPI
summary: Brandon live-demos his background document processing pipeline — a Python while-loop worker that polls for pending jobs, downloads PDFs, runs Dockling, and saves chunks back to Supabase. He then explains why Supabase with pgvector is preferable to ChromaDB for production, showing Drizzle ORM schema management and cascade deletes. Marc asks about migrating from ChromaDB to Supabase, and Juan asks about chunking infrastructure within Supabase edge functions.
-->

00:25:27 - Brandon Hancock
So I just want to show this super fast just so you can see the high-level process. Basically what you do is you have one background job. In the main file, it's just going to run forever. So it's a while loop and it's just going to poll constantly — all it's doing is going over to your database: hey, are there any jobs that are in status pending or basically need to be retried?

00:26:12 - Brandon Hancock
Once we get a job that we like, just extract all the information from it. Basically what we want to do is download the relevant artifact — download the PDF. Once we have it, create the temporary directory where we're going to download everything. And then finally, you're going to start to create all of your Dockling setup that's going to process the document. And then it just processes PDF chunks. This is where you just have Dockling go off, convert the local document, get the chunks out of it. And then eventually it's going to save each one of those chunks back to your database.

00:27:00 - Brandon Hancock
▶ This is the approach that I think you'll see a much better experience deploying it, and you can handle bigger documents.

00:32:46 - Marc Juretus
<Q>Now, if I'm all coding up and ready to go, obviously I'm not going to use ADK Web. If I'm consuming with Next.js, do I just make all the calls like FastAPI endpoints? What would your approach be to that architecture?</Q>

00:33:29 - Marc Juretus
<Q>Like, if you actually push something to production, you wouldn't use ChromaDB [tool:ChromaDB], would you?</Q>

00:33:37 - Brandon Hancock
<A>I think Chroma has a deployed instance — they do have a paid version. However, if you're already going to be using Supabase, it's already there. So it's like, why bring in an entirely new service to manage your embeddings when, if you were going to use Supabase for your database and authentication, it's already right there. I would recommend doing that.</A>

00:34:47 - Brandon Hancock
▶ I would personally stick to just using Supabase, because if not, it's just one extra service that you're having to manage, keep up with. And it's very easy for things to get out of sync, because technically now you have your data saved in your database, and they need to point to embeddings over in ChromaDB. So now you're having to synchronize state across multiple services.

00:35:21 - Brandon Hancock
So let me just share my screen really fast so you can see what it looks like inside of Supabase. You can see, like, right here, I have artifact sections. An artifact section says like, oh, I came from PDF number two, here's the text corresponding to this section, and directly next to it, you can see the actual raw embedding.

00:36:23 - Brandon Hancock
▶ What you're going to run into with ChromaDB is this entire table is going to exist in a different service, so then it's up to you to keep these in sync. That's why Supabase is so nice — I can just click over and I'm there. And more importantly, when you're setting your database schema, anytime I delete a document, you say on delete cascade, and that just means like, hey, if I delete this PDF, delete all the corresponding chunks. That way it keeps the database in sync.

00:37:38 - Brandon Hancock
▶ It would actually look something more like this — you're using a database ORM, like Drizzle [tool:Drizzle ORM], where Drizzle allows you to define your schema. And then in your schema, the main thing that you need to do is set up an embedding. This one line right here is what allows you to start to set up a vector store in Supabase.

00:38:30 - Brandon Hancock
It's almost like you're treating it just like you would every other piece of data in your database. It's really just like, oh, I'm inserting data to my database like normal CRUD operations like I'm doing for every other row in my table. And it just so happens that this one row has a bunch of numbers which make for a vector store.

00:44:03 - Brandon Hancock
<Q>So Supabase — I mean, the part that I dislike right now is you can create edge functions, but I believe it's only Node. You cannot create edge functions that are long-running Python jobs.</Q>

00:44:44 - Brandon Hancock
<A>So that's like, you are almost stuck doing some sort of background worker. Like, I have yet to see a workaround to that yet. Meaning, it's up to you to basically put together a Python application. That Python application's looking for jobs in your database. When it finds an active job, it just works on them one at a time. Chunks and embeds them and saves it back to the database for your web application.</A>

00:45:25 - alexrojas
<Q>Just when you were talking about Next.js — is Drizzle in between Supabase and Next.js? You sneak in the middle Drizzle to manage all the SQL?</Q>

00:45:43 - Brandon Hancock
<A>Yes. So it's like object-relational mapping. The whole point is just so it's actually looking at your schema. What's happening is this is your ORM, which is Drizzle, and what it's doing is it's taking in this raw schema, and every time you make a change to it, it's actually creating changes to be applied to your database — specifically, migrations. So like, you can see every time I make a change to the database, whether I'm creating a new function, a new trigger, a new table — Drizzle uses DrizzleKit to look at all the changes you made to your schema file, and it will create one of these migration files where it's like, hey, Postgres database, I'd like you to create this new table. Here's what's in this new table. Here are the indexes for that table. And then when you run migrate, it applies the change over to your Postgres database.</A>

00:47:28 - Brandon Hancock
▶ What's so nice about this is I can actually access types throughout my code. I can export this type throughout my code — an organization is a type, and I can see, like, an organization is of type ID, name, etc. So you're able to export your types and handle them safely throughout the rest of your application.

---

<!--SEGMENT
topic: ADK Integration with Next.js and FastAPI
speakers: Brandon Hancock, Marc Juretus
keywords: Google ADK, FastAPI, Next.js, streaming, background agents, Cursor AI, static client, voice agent, deployment, long-running process
summary: Marc asks how to serve Google ADK agents to a Next.js frontend. Brandon explains that ADK is a long-running agentic process that should be wrapped in a FastAPI endpoint, with the frontend polling or streaming for results. He shares code examples from a voice agent tutorial demonstrating a static HTML/JS client connecting to an ADK backend, and previews an upcoming Next.js + ADK tutorial. Marc also shares his conversion to using Cursor AI for rapid development.
-->

00:39:45 - Marc Juretus
<Q>My last quick question is — I have my Next.js application up and running. The application does stuff against the database via FastAPI [tool:FastAPI] for the inventory, the games and stuff. But I want to call it to vector embeddings where it pulls up the technical document, answers questions. When you're making your Next.js call to it, are you going to create a FastAPI endpoint that receives the data, processes it, and then returns it back to the client? How are you serving up the ADK that Next.js can consume it?</Q>

00:41:32 - Brandon Hancock
<A>Yeah, so the short answer is ADK is a long-running process — when you kick off anything in ADK, it's agentic. So it's thinking, it's responding, and it just takes a second. It is not like a normal API call to just like forward slash get inventory, where it's like an instant response. Usually what's happening is you are making a request where you pass along your new message. The new message is appended to the conversation. That then kicks off the entire ADK workflow — each agent processes it, delegates it, processes it, and then returns back a message. So you are correct. ADK will be wrapped inside of a FastAPI endpoint to kick off the job. However, it is up to you to pull back in real time — hey, where is the current status of the current messages?</A>

00:49:40 - Brandon Hancock
▶ They actually have some updated docs. I just dropped this into chat. The main thing I wanted to show you is — even if you don't use it fully — you can kind of throw this website link into Cursor and just say, hey, walk me through this step by step. Because the main thing that's important is you'll see how they're basically creating a static client website and how they're connecting that over to and triggering your agent application.

00:49:29 - Brandon Hancock
If you actually want to see this in action, I have a simplified version that I think is a little bit cleaner — done through the voice agent tutorial I did. I just dropped it in chat. You can see I have a static website that has some basic HTML and JavaScript. The main thing about the application is it's made for streaming. It will connect over to my ADK web server, and then it'll handle sending conversations back and forth.

00:50:42 - Brandon Hancock
▶ I will be doing a video on this very, very soon. Probably one of the next big tutorials I do is a simple Next.js application talking to ADK that's deployed. That's probably one of the very next things I'm going to do.

00:43:03 - Marc Juretus
I've come around — being an old coder I was like, you know, I'm just going to code it myself. You're right. Cursor AI, just spinning stuff up. It's just stupid not to. Like real brief, for example, last night, I just wanted to do a simple form submission to a FastAPI endpoint that received first name, last name, email, phone, and just processed it. Wrote it in less than 45 minutes. That probably took me about two nights after work to do so.

---

<!--SEGMENT
topic: AbdulShakur's Sentiment Analysis Tool and Card Game Launch
speakers: AbdulShakur Abdullah, Brandon Hancock
keywords: LLM, sentiment analysis, brand monitoring, OpenRouter, Replit, Supabase, Substack, ConvertKit, Mailgun, Kickstarter, email marketing, waitlist
summary: AbdulShakur describes two projects: an LLM-based brand sentiment analysis tool using OpenRouter for bring-your-own-key access, and a physical card game ("The Deck is Rigged") launched via a Replit-built landing page targeting a Kickstarter campaign. Brandon advises replacing the Substack embed for email capture with either a Supabase + Mailgun setup or ConvertKit for better open-rate tracking and sequence automation.
-->

00:27:42 - AbdulShakur Abdullah
So, it's been a pretty packed week with other things. I haven't gotten too much time to get on my project, but I did kind of map out a little more of the inputs and outputs on what I want. I also jumped on a bunch of free trials of similar tools to kind of see what they're doing.

00:28:02 - AbdulShakur Abdullah
Just to remind everyone — my project was on using an LLM [tool:LLM] to do sentiment analysis to figure out what all the different chatbots are saying about your particular brand, and using OpenRouter [tool:OpenRouter] or some other type of API key so the person can kind of bring their own key rather than providing that, so I can have a very low cost, low friction option.

00:28:47 - AbdulShakur Abdullah
Other project I was working on — which we launched this past weekend — was a card game that we're working on. The Deck is Rigged. So it's basically a fun game where you kind of get prompts and then you match. We designed and built this out, and then one of us went to a conference, and so we're hoping to launch it to Kickstarter in October.

00:29:22 - Brandon Hancock
<Q>Technically, how did you create the landing page? What was your go-to?</Q>

00:29:28 - AbdulShakur Abdullah
<A>Replit [tool:Replit]. Yeah, this was Replit all the way.</A>

00:30:18 - AbdulShakur Abdullah
I tried to just embed Substack [tool:Substack] and use that because I thought most of the users would be Substack, which then I found out later on that there's like a friction on mobile to signing up through the website. So I might have missed some sign-ups, and I should have done the Supabase and then just transferred people over.

00:30:48 - Brandon Hancock
▶ Definitely my recommended approach for sign-up forms like that — two approaches. One is just to keep everything in your Next.js application where you have a database tracking signups, and these aren't like user signups, these are just like interested parties. Then all you need to do is, on Mailgun [tool:Mailgun], you just set up — I think it's like $6 or $12 a month, or actually you'd probably be on the free tier, realistically, and you're allowed to send out like 1,000 emails a month for free. Approach two is actually go ahead and put them in a CRM — upon sign up, capture their information, save it to a local database, and then also add them as a user to ConvertKit [tool:ConvertKit]. That way, you don't have to make the email blast script at all. They're automatically just put into ConvertKit, and then you can have them set up for sequences.

00:32:15 - Brandon Hancock
▶ I'd actually probably go with ConvertKit just to make it easier to see open rates, click-through rates, and all sorts of stuff like that — since yours is strictly a launch.

---

<!--SEGMENT
topic: LinkedIn Automation Agent and Browser Agent Limitations
speakers: Matias, Brandon Hancock
keywords: LinkedIn automation, Playwright, browser-use, Google ADK, agents, deterministic automation, OpenAI, Ollama, Mac Mini M4, lead generation, Google Cloud, Vertex AI
summary: Matias (Buenos Aires, Google Cloud partner) demos an ADK-based LinkedIn connection agent using Playwright to send invitations from a URL list. Brandon advises separating deterministic browser tasks (Playwright scripts) from agentic tasks (message classification and response drafting), warning that browser-use agents are unreliable due to context window bloat from large HTML pages. The key recommendation is to get data out of the browser as fast as possible and process it with agents offline.
-->

00:51:51 - Matias
I am from Buenos Aires, Argentina. I'm very familiar with Google Cloud because I have some Google Cloud certifications — data engineer and cloud architect. I am working with the cloud since four years ago, mainly with big data. I don't know if you're familiar with Hadoop [tool:Hadoop], Hive, Spark, and all these things.

00:52:38 - Matias
I created an LLC in the United States to give cloud services, Google Cloud services. I have the Google Cloud partnership [tool:Google Cloud]. But my big challenge was to get clients. Last year, I invested a lot of time and money to generate leads — through LinkedIn, with Apollo [tool:Apollo], sending emails, with a product that creates marketing campaigns through LinkedIn. But this didn't work.

00:55:00 - Matias
That's where AI came into my life, and the agents. I was the last six months studying and trying to know where to go, because there are a lot of tools — CrewAI, LangGraph, a lot of things. But one month ago, I saw that Google has its own ADK. I saw your videos, Brandon, on YouTube. That's very, very helpful. My idea is to try to create a lot of agents to do this work for me — that means sending LinkedIn invitations automatically.

00:57:07 - Matias
For example, last week, I created an agent with a tool that does — well, with Playwright [tool:Playwright] — because this is not deterministic, right? And I want to do it as deterministic as I can. I have my agent, and for example, if I send a connection — I have a list of URLs that I get with another process, scrolling LinkedIn Sales Navigator, in a list. And for example, I want to process one URL. What this is doing is it's going to the profile, clicking the connect button, and sending an invitation without a note.

00:58:53 - Matias
My idea is to have another agent — if I have a brief draft — that gets a message and prepares the answer for each one, based on some things that I can tell to the agent. I am telling all this because I want feedback from the team about what you think about this, if this can work.

01:00:17 - Brandon Hancock
<A>So right now when it came to everything I just saw with sending out connections, I would actually not use an agent for that because it's the exact same screens every single time. So I don't think there's a need for agents on that side — the URLs, you already have the links, you're using Playwright to open up the page, clicking connect, waiting two seconds, clicking send invite without note. We actually could scrap agents and not need it for that part. If anything, it would just take longer and cost tokens to go through that cycle. ▶ So I would just stick to raw normal web drivers that have been around for that process.</A>

01:01:11 - Brandon Hancock
▶ However, on side two, when it comes to the actual responding and classifying — junk, valid lead, stuff like that — that is where I think agents would be super handy. With that said, what you might want to do is get out of the browser as quickly as you can. Have a normal web driver — all it does is it finds the message history, adds it to a database of some sort, and just get out of the browser as fast as possible. From there, having some sort of background agents that analyze those messages, figure out next steps, figure out a response — that's what I would look at doing.

01:02:40 - Matias
I was testing also browser-use [tool:browser-use]. Do you know browser-use? I tested with OpenAI [tool:OpenAI], and with ChatGPT [tool:ChatGPT], and also with local Ollama [tool:Ollama] on my Mac Mini M4. Browser-use is very, very heavy for all the process that it's using. And also, that's why I told you at the beginning that I want to be very deterministic with this, because it's very difficult — I didn't find a way to have browser-use do what you want.

01:03:37 - Brandon Hancock
▶ Browser-use, browser-base, browser-lists — all browser agent tools right now are not the most reliable. That's why I'm saying get out of the browser as quickly as possible, just because these agents really do struggle with — what's my overarching goal? Wait, okay, I need to click here. Well, this one page has 50,000 lines of HTML, CSS, and JavaScript. Boom, you just blew up my context window. What was I initially trying to do? So that's why I'm just saying — static, because you know exactly what you're trying to do. Browsers themselves aren't reliable. I would get the agent out of the browser as quickly as possible.

---

<!--SEGMENT
topic: Zain's AI Second Brain and Personal Knowledge Management
speakers: Zain K, Brandon Hancock, Bastian Venegas, Paul Miller
keywords: ADHD, second brain, MCP tools, Notion, Gmail, Zoom, Limitless pendant, ADK, Google ADK hackathon, Vertex AI, personal knowledge base, executive assistant agent, Context 7
summary: Zain describes his goal of building an AI executive assistant / semantic second brain to manage ADHD-related cognitive challenges, having tried many tools including Supabase, Pinecone, and GCP Matching Engine. Brandon advises starting with one focused agent (e.g., email assistant) connected via MCP tools rather than tackling the full vision at once. Zain shares that he submitted an ADK hackathon project using Brandon's tutorials. Bastian suggests the Limitless Pendant API as a passive data capture layer for such a system.
-->

01:05:37 - Zain K
Hey, guys. My name is Zain. I work for a small boutique consulting firm. We help implement enterprise applications like Oracle, NetSuite [tool:NetSuite], replacing on-prem systems.

01:06:14 - Zain K
Some of the pain points — same issues a lot of people over here are struggling with: lead generation, scaling marketing efforts to personalize some opportunities. I'm a huge GCP, Google fan. They've introduced so many plug-and-play solutions, like Vertex AI [tool:Vertex AI], et cetera. But aside from those obvious pain points, the specific ones I always run into is — I'll start something, like the Supabase conversation you guys were having, I'll run over to Pinecone [tool:Pinecone]. I had some issues with Pinecone. I'll go over to GCP Matching Engine [tool:GCP Matching Engine] quota. I drive myself crazy because I've tested so many different applications.

01:07:30 - Zain K
One of the biggest things I want to be able to solve is building an integrated AI assistant that centralizes my personal knowledge base, but it's tracking my personal activity with my operational data. Think of it like a semantic second brain that automates workflows, but also is able to structure my unstructured chaos.

01:08:46 - Brandon Hancock
<A>So on the idea of basically just having a true executive AI assistant that knows everything about you — it literally comes down to a context problem. It really comes down to getting context. So for example, having the meetings, looking at your emails, looking at your Zoom conversations — it really does come down to allowing your agents to quickly go out, grab everything they need, and bring it back to the relevant conversation. ▶ The biggest thing that I would recommend to start is, if you are using ADK, just setting up and connecting as many MCP tools as you can, such as Notion [tool:Notion MCP], so you can easily grab anything you've ever said. If you're using Zoom [tool:Zoom MCP], they have one — you can easily look up previous transcripts. Gmail [tool:Gmail MCP], they have one — you can easily search through every email. I think just creating one monster agent that has access to all these different tools would be a really great starting spot.</A>

01:10:29 - Zain K
I was probably the first person to sign up for Rewind and then it changed over to Limitless [tool:Limitless]. Here's where I fall short — I'll forget that I had started a process. I have a habit issue. How do I supplement my bad habits with continuing moving forward?

01:11:23 - Zain K
My whole entire idea is based on the inspiration of Cortana. I don't know if anybody is a Halo fan, but I grew up playing Halo.

01:11:52 - Brandon Hancock
▶ I think we're trying to tackle an insanely big goal to start. One of the biggest things that I always do when I pick too big of a goal — I don't know what to work on, so then I just wander aimlessly. So that's why I like to zoom in. What am I actually trying to do here? I would 100% look at — I think just zooming that in just a little bit. I just want an email assistant first. Let's just pick one and get that working. Then, okay, cool, I now have an email assistant agent. Now I want a Notion assistant. Just do one of these at a time, and then eventually have a master agent who talks to these other ones.

01:17:41 - Zain K
Also last thing — shout out to you because I was able to submit my ADK project for the hackathon from watching your video. It was straight to the point. I even told the GCP team, I'm like, Christina, I don't know if you guys actually consider him an affiliate, but y'all better give him credit because I was able to check off all the bonus point criteria of the hackathon because of you.

01:27:50 - Bastian Venegas
I was thinking about this idea — something like the Limitless Pendant [tool:Limitless Pendant] can have a lot of potential since it's recording you always, and it also has various API endpoints, so you can in theory pull the API endpoint every some number of seconds and have it generate a tool call. So you can have some use cases where you have this agent use MCP or agent-to-agent protocol, and just have some stuff done for you.

01:29:21 - Bastian Venegas
▶ A lot of use cases — like the one he mentioned about storing your screenshots and images — are actually solved by deterministic tools. For example, Pinterest. You can just use the regular software deterministic way to get the data, and if that's all it's going to be is for something for the LLM to reference, then just getting it as text in some database is more than enough. Be as much as deterministic as you can until the point where you need to pass this to an agent.

---

<!--SEGMENT
topic: Paul's Dockling Experience, Limitless Productivity, and Pythagora AI
speakers: Paul Miller, Brandon Hancock, Mitch, Bastian Venegas
keywords: Dockling, LocalGPT, Limitless, Otter AI, CRM, Pythagora AI, Lovable, Cursor, MLX, MacBook M4, PDF processing, sales productivity, personal branding
summary: Paul shares hands-on experience with Dockling on an M4 MacBook Pro using MLX acceleration, processing 20–50 page council PDFs in ~20 seconds. He reports using Limitless + Otter AI to close three customers in four weeks (down from six months average) by automating meeting notes and follow-ups. He introduces Pythagora AI as a VS Code-based tool with built-in app planning. Brandon recommends AI task template documents as a meta-productivity layer for Cursor-based development.
-->

01:34:32 - Paul Miller
So, I've been looking a bit further on RAG. One of the things that I saw was a video from the Prompt Engineering channel. Muhammad's got a project — LocalGPT — it's an open-source project on RAG. He's added Dockling and done a whole lot of stuff looking at improving the accuracy of the RAG searching. He did put a message out there to see if anyone's got any verticals that you might want to turn into a commercial project. That appealed to me and I had a Zoom call this morning with Muhammad just going through his thinking on that.

01:35:51 - Paul Miller
▶ If you're looking at the LocalGPT project — being released according to Muhammad in the middle of July — watch the video. On the LocalGPT, he raises some really good points on the way the framework should be set up. His framework is designed to run locally, but there's no reason why you couldn't point it out to external LLMs rather than doing local LLMs.

01:36:36 - Paul Miller
Out of watching that video and hearing all the feedback from a number of you, I got into Dockling over the weekend. I needed to do some analysis of a whole lot of PDFs, and boy, that's a lovely library. I've just wasted so much time with stuff reading PDFs.

01:37:10 - Brandon Hancock
<Q>Quick question for you — how big were the PDFs, and how long did it take to process each one for you?</Q>

01:37:11 - Paul Miller
<A>So the PDFs were council data — local municipality data. The PDFs were in the sort of up to 50 pages, so sort of between 20 and 50 pages. On average, they were probably around maybe 15 to 20 pages, and taking about — so I was running it on my MacBook Pro M4 [tool:MacBook Pro M4] with about 64 gigs of RAM. I was using the MLX extension of Dockling, it was taking about 20 seconds per document. That's, given the quality of the output, that seemed pretty good to me.</A>

01:38:07 - Brandon Hancock
The reason I ask is because I have an M1 32 gigabytes, and I did not turn on the MLX side of things, and it took forever. The document I was working with was like 20–25 megabytes — 700 pages — in like 10 minutes. I thought Dockling broke the first time I ran it. I was like, man, everyone hyped this up. It doesn't even work. And then I was like, oh wait, my computer is the actual problem.

01:39:25 - Paul Miller
Look, I've got Limitless [tool:Limitless], I'm not selling for the company, but Brandon is. I won — it usually takes me to onboard a customer six months. In the last four weeks, I signed three customers that took on average five weeks each, because I'm capturing all of the notes, either when I have my Zoom calls with Otter AI [tool:Otter AI], or with Limitless. So I'm talking in the car, I'm talking in meetings, Limitless is tying it all together, combined with Otter AI for all the Zoom calls. ▶ My God, what a difference it makes. Right after the meeting — because I'm slack, I never write up the notes, actions, go back to the customer, say, we had the sales meeting, we had this outcome — it's meant that I've been able to close customers much better.

01:41:22 - Paul Miller
<Q>Has anyone seen the Pythagora AI solution?</Q> It's yet another VS Code branch, but it's a prompt-based kind of solution. What this one seems to do is you put the prompt initially when you're trying to build a plan, and the plan part of building the app is built into the framework, so it does the plan properly first, after you do your app idea, and then it expands into building the app side.

01:43:08 - Brandon Hancock
<Q>So does it actually set up and connect to a backend as well? Is it doing Next.js under the hood? Do you have any details on what's happening under the hood?</Q>

01:43:18 - Paul Miller
I haven't had a proper play yet. I just wanted to see if anyone else had. The video I saw this morning was from David André — he was talking about it. My only concern — I love David André, but it's a sponsored video.

01:45:13 - Brandon Hancock
▶ So like, I'll just show you guys exactly what I'm doing really fast. What I'm starting to do now with setting up more AI docs is create templates for myself. For example, I'm building AI web applications — what I'm setting up for myself is what I'm calling as many templates as I possibly can for everything. Anytime I create a task, I want the output to be as actual and concise as possible to where it just works. ▶ I'll start off with a template, and I'm like, I'm trying to implement this new feature. It will create a document for me. I almost have a feedback loop to where I am the training agent — every time it produces a result, I'm like, oof, you forgot to do this, or you overlooked this. And then I continually will update this master template document. To start off, it was like 70% right. Now it's like 95% right at creating tasks that AI can almost one-shot.

01:47:55 - Brandon Hancock
▶ The key takeaway is just like, when you're creating tasks, there's a term that the Air Force uses called OODA loops. When I'm creating these tasks, I always start off so that the AI has to restate every framework that it's using, actually write out the full problem it's trying to solve, the functional requirements of what the final result should be. Most AI applications come down to making changes to your database, making new backend changes, setting up some frontend changes. Anytime it makes a mistake in frontend changes, you fix it here. Anytime it makes an error when it creates new backend routes, you fix it here. This one living document will now, anytime you make a new task in the future, be that much better.

01:56:45 - Paul Miller
My father's got early Alzheimer's and I needed to have lots of meetings with the doctors and things like that. You're trying to listen, but you don't want to have to sit and write notes about what the doctor's saying. But Limitless was capturing all the detail and it summarized the detail and I could go back to that part of the recording as well. So you can get the recording snapshot as well as the transcription, as well as the summary. ▶ So it's got all of the components there — really nice software.

---

<!--SEGMENT
topic: Bastian's RAG Search Engine Project and GraphRAG Discussion
speakers: Bastian Venegas, Brandon Hancock, Sam (unnamed speaker)
keywords: RAG, vector search, GraphRAG, Neo4j, knowledge graph, hybrid search, agentic loop, query rewriting, LangGraph, Supabase, pgvector, RAG as a service
summary: Bastian describes a planned Google-style RAG search engine that returns ranked results rather than LLM-synthesized answers, with an agentic loop for query rewriting when result thresholds aren't met. The group then discusses when GraphRAG outperforms plain vector search — specifically for domain-specific knowledge graphs (e.g., medical, legal) where entity relationships matter. Brandon floats the idea of "RAG as a service" as a future product. Sam shares experience with RAGAnything (LightGraph-based) and Claude Code for building an MCP RAG server.
-->

01:30:59 - Brandon Hancock
We're going to hopefully start working on a project together pretty soon — Bastian, I mean, it'll become Bastian's project — but he'll get to work on almost like a RAG search engine. Bastian, if you want to talk about that in a few seconds, I think that might be pretty cool to tell people what you're about to do.

01:31:20 - Bastian Venegas
Basically, the use case is — they want more like a Google-type search engine where you get, instead of the response an LLM interprets from a bunch of text that it retrieved during a search — you don't want that. You want more like actual results that you can browse through.

01:33:07 - Bastian Venegas
▶ You can also have agentic loops trying to set the score. For example, you can set a threshold where you want to get at least 10 results. So you can have the agent evaluate and filter which results are best for the user query instead of just relying on the score for the vector store. And then you can say, okay, I will ask the system to go in a loop again and rewrite the user query, and send more queries that can actually match or use a different rewrite technique until I get, for example, 10 results. So it becomes agentic in a true way.

01:34:00 - Brandon Hancock
I think it's going to be a super cool project. The long story short — it's like Google search, except with a vector store. You type in a query, you get back 20 results, and you can browse through old-school Google, but it was actually done through a vector store, plus all sorts of other features that Bastian was just going to talk about.

02:07:16 - Brandon Hancock
<Q>Bastian, super fast — have you seen any full-blown RAG solution where plain vector store would not work unless it was GraphRAG? That's the one thing I haven't fully seen yet — oh, this use case does not work until you use GraphRAG.</Q>

02:07:43 - Bastian Venegas
<A>Yeah, it really depends on what makes your database and what topics they cover. For example, if you try to make a system that's supposed to be very general — like legal, medicine — think of a purpose that's really different, each thing is different from each other, like the kind of data that you would use to train an LLM, that's very general — then it would not make sense to use GraphRAG [tool:GraphRAG] because there's not much semantic relation between each document. So if it's like random documents from a user, you could use simple RAG perfectly, or you can use traditional GraphRAG. If your corpus is really specific — for example, if it's just legal — then there are multiple reports that they do get better results with using knowledge-based graphs, where the only change versus GraphRAG is that it's specific to the relationships that the graph has — they are custom for the domain. For example, this medication is from a family of medications, and they are used to treat this condition. So yeah, then it will produce things that are useful in addition to the vector database. But you can always have them — it usually is run in parallel, and you just have to decide how you will weight these scores to present it back to the user.</A>

02:05:35 - Brandon Hancock
▶ What I've not seen yet is — all these problems that we're talking about, like, hey, I have a PDF, I just want to chunk it and get back the embeddings. Or I have a text file, or I have a video — all of that, like RAG as a service, to where it just spits out all the different embeddings and chunks that you can go put in any database ever. I have not seen that. That is a project I want to work on as soon as I'm done with ShipKit, just because every problem that we're talking about — man, this is a pain to solve — that is a direct developer tool that you could use and sell.

02:03:01 - Brandon Hancock
There's this RAGAnything [tool:RAGAnything], which I found — it's based on LightGraph [tool:LightGraph] underneath it. What they're doing makes total sense. It's kind of a wrapper on a graph, so you can throw anything in through the RAG, and then it sort of pulls it out into a graph and your embeddings. So it grows. You can put images in, you can put PDFs, I think they're even saying you can do videos.

---

<!--SEGMENT
topic: Jaylen's Topic Funding Platform and Andrian's LangGraph Personal Brand
speakers: Jaylen.Davis, Brandon Hancock, Mitch, alexrojas, andrean georgiev
keywords: TopicLaunch, YouTube creators, crowdfunding, Patreon, feature requests, LangGraph, personal branding, Context 7 MCP, Claude Code, Cursor, AI content creation, LangChain
summary: Jaylen demos TopicLaunch.com — a platform where fans propose and fund YouTube video topics with a money threshold and 48-hour creator deadline. Brandon suggests adding free upvoting tiers and a creator-pays subscription model. Andrian (UK, 1am) introduces himself as a former project manager building a LangGraph-based memory chatbot, seeking career direction. Brandon recommends building a LangGraph-focused personal brand with weekly tutorials as the fastest path to consulting opportunities. Context 7 MCP is recommended for pulling up-to-date LangGraph docs into Cursor.
-->

02:10:18 - Jaylen.Davis
I recently created a platform that allows YouTubers' fans to propose and fund topics. You can actually find it on topiclaunch.com [link:topiclaunch.com]. I finished it two days ago.

02:10:47 - Jaylen.Davis
For example, let's say you're a fan of Mr. Beast, and you want him to talk about a specific topic. You propose a topic and you create a threshold with it. He has to approve of the topic. Once he approves of it, everybody has the opportunity to put money into the topic. Once it meets the threshold, the creator gets a notification and they have 48 hours to create the video or do the live stream. If they fail to do so, then all of the people who put in their money just get refunded.

02:11:48 - Brandon Hancock
I think that's a very, very cool idea because constantly — I mean, I do this in others — it's like, what do you guys want to see next? And the current approach is polls on YouTube, it's polls on a school community. But obviously, if, you know, the top 10% of following is like, no, I'm all in on what you're doing, I need more guidance — I really think that's a very cool idea.

02:12:38 - Brandon Hancock
▶ I am curious on the 48-hour thing, just because sometimes it does take a minute to create something. I would just be curious — almost having two tiers: just allowing people to upvote for free, but then allowing creators to say, I only want people to vote but they have to pay a dollar or two dollars, and if I make the video that they want, then I do it back. Either way, it's insanely helpful. Even if the creator paid $30 a month for the service that they could show to their audience — hey, you guys come in here and vote, you guys create your own topics, you guys upvote existing topics — something like that would be super helpful.

02:15:49 - Brandon Hancock
▶ The thing I was going to show real fast — I think the tool is called Bonobo, but it's called Flow [tool:Flow app]. It's like a little drawing app you can put on your phone. What's nice about it is, instead of like, hmm, what do we build next? — this is actually how they pick what they build in real time. Users in the app basically say — they have a little thing: do you want to see something new in the application? And then you click it. It takes you to this page where you can see all existing feature requests. And then their development team in real time just builds each one of these one at a time. For you, flipping it to be more for creators, it would just be basically like, what video do you want to see? And then people would upvote.

02:19:23 - andrean georgiev
Hi there. I'm Andrian. I've been wanting to join this call for weeks now, but I'm based in the UK, so it's pretty late up here. It's just after 1am.

02:20:00 - andrean georgiev
I'm resonating so much with what you guys talk about. I've been watching the recordings and getting lots of good ideas. I used to be in project management, and I was a team lead of a group of project managers in the cloud industry. At some point, seven years ago, I got a computer science education as well, but I've never worked a technical job in my life.

02:21:42 - andrean georgiev
I have strong interest in AI agents, particularly LangGraph [tool:LangGraph] is my framework choice. I played with n8n [tool:n8n] as well, as a way for doing automations. But I quickly realized there are some limitations in n8n that prevented me from really exploring the full potential of agents. Right now, as a way of me learning and really getting more expertise in LangGraph, I am building a chatbot that is kind of hyper-personalized, uses memory management, uses that plan-execute cycle, and things like that.

02:23:03 - Brandon Hancock
<Q>Is goal new job? Is goal to scale up, promotion at current job? Is it to go freelancing? Did you want to launch AI applications?</Q>

02:23:27 - andrean georgiev
<A>Oh, that's the big question for me, actually. That's what I need to figure out. I've been out — I quit my job a year ago and I've taken a sabbatical. My interest in AI started six months ago. I wasn't sure which way to go. Maybe a product manager would be a good development for me, at least in the short term, because I've been out of work for more than a year. I've got to have some income at some point. But long term, it will be amazing if I really built expertise, some sort of authority in something specific, just like you advised in your video, and really dig into that.</A>

02:26:00 - Brandon Hancock
<A>▶ All right, if you have six months — what I would do is, like you said in the video, I'm going to make an AI personal brand. What I would recommend is pick a tech stack and then just explore as many opportunities as you can in there. For example, you already have familiarity with LangGraph. Cool. LangGraph is probably one of the most enterprise-grade tools out there. That is what Fortune 500 companies are using currently. They're also using CrewAI, but if you got to see the Interrupt 2025 conference, the big boys are all using LangGraph. So cool — you already are in a great spot to focus on a framework that's used by the big boys. What I would do is focus on creating an AI personal brand where your whole goal is — once a week, you create a LangGraph project and make a tutorial on it and a LinkedIn post. Every week, one YouTube video, one LinkedIn post. And what's crazy is, after doing that for a while, you will clearly become — if you just did that for six months straight, you would probably be the number one LangGraph-producing person on the internet. You're going to get smarter on it. People who have questions are going to come to you. It's going to lead to consulting opportunities. It's going to lead to job opportunities.</A>

02:30:25 - Brandon Hancock
Yeah, LangGraph, Docs — and tell me what version you have. So long story short, Context 7 [tool:Context 7 MCP] is basically an MCP tool that has access to every single code repo — not all, but like it's growing, like 13,000 code repositories or something crazy like that. And what happens is you can just say like, hey, can you look up the documents for this? So you can see it went off and looked up the library LangGraph. It found some results, then it's like, okay, cool, I now know you're talking about LangChain, LangGraph, great, I now can start to look deeper into what actually the docs of LangGraph say, and it can actually fully understand what's going on.

02:32:07 - Brandon Hancock
▶ The second their documents are a little bit more finalized, you can actually say like, oh hey, when you're trying to build an agent, refer to the docs. And what's crazy is it'll bring the entire docs down to Cursor and it'll do a much, much better job. Because without it, the model is only as smart as the training data, which is probably an outdated version. This is a good way to bring in the latest version.

02:34:08 - Brandon Hancock
All right, well, I got to run. It was awesome getting to see all of you per usual. One thing I am going to change for next week is I'm going to create a Typeform [tool:Typeform]. So before we have a call, what I'm going to allow people to do is basically just submit all questions before starting. That way we can get all questions asked and answered, and then we'll probably in part two go to round robin on success and cool projects. That way everyone's making progress and not stuck and it'll be a little bit more structured. So that's one thing I'm going to change for next week and we'll experiment.

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names were not found in the SPEAKER_ALIASES context block (which was not provided) and have been passed through unchanged:

- **alexrojas** — active participant throughout; first name appears to be Alex
- **Matias** — guest from Buenos Aires, Argentina; Google Cloud partner
- **Zain K** — guest; enterprise consulting, ADHD productivity focus
- **Mitch** — recurring member; data/reporting work, Amazon seller analytics
- **Marc Juretus** — recurring member; Next.js + ADK game/fantasy app project
- **Juan Torres** — recurring member; contract law interest
- **Bastian Venegas** — recurring member; RAG search engine project
- **Jaylen.Davis** — guest; TopicLaunch.com creator
- **andrean georgiev** — guest from UK; LangGraph chatbot developer
- **Sam** (unnamed speaker at ~01:57:18) — recurring member; Claude Code + RAGAnything exploration