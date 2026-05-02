=== SESSION ===
date: 2025-05-27 (inferred from transcript reference)
duration_estimate: ~2 hours 20 minutes
main_themes: MCP adoption, WhatsApp chatbot architecture, vector stores and RAG, app deployment (Railway/Cloudflare/Cloud Run), PDF extraction tools, multi-agent orchestration (ADK/CrewAI), AI coding tools (Cursor/Windsurf/Bolt), personal branding for AI developers

---

<!--SEGMENT
topic: Session Opening and MCP Announcement
speakers: Brandon Hancock, Marc Juretus, Paul Miller, AbdulShakur Abdullah, Alex
keywords: MCP, Model Context Protocol, tool calls, Notion, Google Drive, GitHub, external APIs, agents, tutorial announcement, weekly coaching call format
summary: Brandon opens the weekly coaching call with small talk about GPS and navigation, then announces an upcoming MCP tutorial. He explains his evolution from MCP skeptic to advocate, arguing that MCP servers eliminate the need to manually wrap individual API endpoints as tools. He also outlines the call format for new attendees.
-->

00:00:00 - Alex
It's business, which is a big short.

00:00:08 - AbdulShakur Abdullah
That and directions.

00:00:09 - AbdulShakur Abdullah
I have a unique ability to always get lost, too.

00:00:15 - Paul Miller
Oh, I could use that for its training.

00:00:18 - Marc Juretus
You ever think where we were before GPS, man?

00:00:21 - Marc Juretus
I used to do stand-up for a number of years, so I'd be going on shows, and I'd be printing out MapQuest stuff.

00:00:30 - Marc Juretus
And I'd still get lost, and it was, like, so hard.

00:00:34 - Marc Juretus
And they're like, aren't you in IT?

00:00:36 - Marc Juretus
Aren't you supposed to be sharp?

00:00:37 - Marc Juretus
Yeah, well, I suck with directions, man.

00:00:42 - Paul Miller
I ended up having arguments with my wife, who would be trying to do the navigation.

00:00:48 - Paul Miller
She was hopeless.

00:00:52 - Paul Miller
It's like, we are so glad that there are electronic maps.

00:00:57 - Paul Miller
So we've got something else to argue about now.

00:01:00 - Brandon Hancock
Thank you. Save the relationship.

00:01:04 - Paul Miller
I remember I was on holiday in Greece on a Greek island, and I'd been working really hard, and I had laryngitis, so I was driving, I was trying to drive the car, and I couldn't say anything, and she was trying to instruct me.

00:01:25 - Paul Miller
It was a nightmare holiday.

00:01:30 - Brandon Hancock
But hey, y'all survived. That's the important part.

00:01:54 - Brandon Hancock
It goes by faster, I swear. But yeah, before we dive in, I want to give a quick update. I just wrapped up an MCP tutorial for you guys.

00:02:08 - Brandon Hancock
So long story short, I did not like MCP for the longest time, just genuinely did not understand the need for it, just because I was like, oh, I'll just do tool calls.

00:02:21 - Brandon Hancock
But as I started to dive deeper into it and start to connect to more external APIs, I'm like, oh my God, MCP [tool:Model Context Protocol] is a godsend. If you're going to work with any common API, just use their MCP.

00:02:38 - Brandon Hancock
So there's everything from Notion [tool:Notion], Google Drive [tool:Google Drive], Google Docs [tool:Google Docs], GitHub [tool:GitHub] — every software company now is making their own MCP.

00:02:44 - Brandon Hancock
▶ So if you ever want your agents to start to work with other real-life interfaces, MCP is amazing.

00:02:52 - Brandon Hancock
So I was anti-MCP because I was like, this is silly, but now I've drank the Kool-Aid and I cannot go back.

00:03:07 - Brandon Hancock
And also, just real quick in case you're first time on the call — basically the way we do these weekly coaching calls is we go around the room and usually just share if there's something interesting that you're working on that you think the group would like, or if you have a question on something, feel free to ask in the group. Together we're smart.

---

<!--SEGMENT
topic: WhatsApp Chatbot for Music Venue
speakers: Alex, Brandon Hancock, Maksym Liamin
keywords: WhatsApp API, Meta API, Cloudflare Workers, Railway, RAG, vector store, structured database, Twilio, webhook, Python, chatbot architecture
summary: Alex presents a project to build a WhatsApp chatbot for a music venue in Mexico that lets attendees query band information. Brandon recommends replacing RAG with a simple structured SQL/Airtable database keyed by date. Maksym advises on WhatsApp API integration via Cloudflare Workers, and Brandon suggests Railway as an alternative hosting option, sharing a link to WhatsApp Cloud Docs.
-->

00:03:40 - Brandon Hancock
Alex, you're up first.

00:04:04 - Alex
Yeah, actually, I'm doing two main projects — doing another video, and I'm also working on a little app. I based myself on the RAG agent [tool:RAG] that you did in the course.

00:04:21 - Alex
And I had a question. Maybe if I share my screen...

00:04:52 - Alex
So this is a little diagram. It's for a friend of mine. He has a venue — bands, a big rehearsal space. There's a lot of bands coming.

00:05:30 - Alex
What we want to do is, through WhatsApp [tool:WhatsApp] — in Mexico it's hugely used — we want to send a WhatsApp to one number. And that number just makes a little RAG query, very simple information about the band. So what you get back is like a one-pager of the band, where you get the contacts if you want to keep in touch with them.

00:05:58 - Alex
<Q>So what I was thinking is to base myself on the RAG agent video. The question I had is: how do I make the user experience from the WhatsApp?</Q>

00:06:27 - Brandon Hancock
<A>So I want to give a few pieces of advice on this. If I was you, what I would do instead of a RAG query is I would actually create a database — just a plain SQL database — where all it had is dates, and per date it would have who's playing and an itinerary for that date. So at any point, anyone can say, hey, what band is playing? And you would just assume they're talking about today or this upcoming weekend.

▶ The reason why is because the amount of information you're doing could literally fit on a notepad. So the biggest thing is: RAG not needed, but structured data is.

▶ And what's nice about this is you could easily do Airtable [tool:Airtable] or a Google Sheet [tool:Google Sheets], so you could let the venue easily update the document.</A>

00:08:00 - Brandon Hancock
When it comes to WhatsApp, I haven't had a ton of experience. Maxim and Michael in the group are the WhatsApp experts. Maxim, any advice for Alex?

00:08:22 - Maksym Liamin
<A>So basically, the Meta API [tool:Meta WhatsApp API] has everything for that. You just have your route that lives on some kind of worker or whatever. I really recommend Cloudflare Workers [tool:Cloudflare Workers]. It's just amazing — five dollars and it can support thousands of users without problem, scaling in different locations. You just host your worker there. It runs with your tools that call your database, get the info, generate the answer, and then you push them to WhatsApp as a normal answer.

▶ You need to understand that when you work with WhatsApp API, you will not be working with push notifications because it takes too long to get approved. But the person needs to contact you first and then you can answer instantly.

You don't even need Twilio [tool:Twilio]. If you can get a normal phone number, you can go to a local carrier and buy the SIM. I really recommend you go into the OpenAI app on WhatsApp [tool:OpenAI WhatsApp bot] or Meta AI app on WhatsApp and really see what they do — when you open the chat, there are like four template messages you can start with, and how they show the syncing process, how they stream.</A>

00:11:44 - Brandon Hancock
The other one I really like is using Railway [tool:Railway]. You make a Docker container — a Python application designed to receive webhooks. So every time a message comes in, it's going to hit webhooks/WhatsApp, and that's going to handle the message, generate a response, and send it back.

00:12:39 - Brandon Hancock
▶ Either way — Cloudflare or Railway — you're going to need to make a Python application that starts to receive queries.

00:12:42 - Brandon Hancock
I dropped a link to the WhatsApp Cloud Docs [link:WhatsApp Cloud API documentation] in chat. Definitely recommend checking that out.

00:13:47 - Alex
Also, just one quick update. After the video, there were some people from the government of Guanajuato who contacted me for some tutorials on AI tools.

00:14:00 - Brandon Hancock
Congrats! I've been saying all along — just the power of the internet. Put yourself out there and it's insane. The opportunities you would never know they needed help, but you put yourself out there, they find you.

---

<!--SEGMENT
topic: Content Creation Tools and YouTube Channel Launch
speakers: AbdulShakur Abdullah, Brandon Hancock
keywords: YouTube, content creation, TeleTV, Descript, Screen Studio, OBS, recording software, Bromi, N8N, Greg Eisenberg, LinkedIn marketing, Prompt Warrior channel
summary: AbdulShakur shares that he published his first YouTube video on his "Prompt Warrior" channel and has been experimenting with Greg Eisenberg's N8N LinkedIn marketing platform. Brandon recommends TeleTV for full YouTube videos and Screen Studio for short-form content, with Descript as another strong option. The segment emphasizes consistency as the hardest part of content creation.
-->

00:14:38 - Brandon Hancock
AbdulShakur, you're up. What projects are we working on?

00:14:45 - AbdulShakur Abdullah
Yeah, so I have had some downtime on the projects as the family came back. But I did manage to make my first YouTube video.

00:15:05 - AbdulShakur Abdullah
It's bad quality, and I just put it out there to get it out there.

00:15:18 - Brandon Hancock
<Q>What's the channel?</Q>

00:15:20 - AbdulShakur Abdullah
<A>Channel is Prompt Warrior [link:YouTube channel "Prompt Warrior" by AbdulShakur Abdullah].</A>

00:15:27 - Brandon Hancock
Alright, I'm gonna like and subscribe, man.

00:16:02 - AbdulShakur Abdullah
Yeah, so I've been playing around with the new models that came out, and then I was like, let me see which one can actually do some different tasks for me. Bastian had a meeting with me and actually told me what I was doing wrong with my previous agent. And then Greg Eisenberg [tool:Greg Eisenberg N8N LinkedIn platform] came out with a video on doing mostly exactly what I wanted to do, so I started playing with his N8N [tool:N8N] LinkedIn vibe marketing platform. And then I was like, oh man, connecting all these APIs is really annoying.

00:17:05 - AbdulShakur Abdullah
I was like, hey, can you just do it without me connecting all these APIs to ChatGPT [tool:ChatGPT]? And it started building and making stuff, so that was fun.

00:17:40 - AbdulShakur Abdullah
I found this other platform. Have you heard of Bromi? It's a new recording software. They have a lifetime deal right now.

00:17:57 - Brandon Hancock
The two I've heard and seen a lot of people use with really good success — so if anyone's thinking about making YouTube videos to start, if you don't want to go down the OBS [tool:OBS] and manually set it up route, you can use TeleTV [tool:TeleTV]. This is like one of the easiest ways to make videos and clips and make them look super nice. You can share screen, split screen — it's like 19 bucks a month and you get an insane amount of things.

00:18:44 - Brandon Hancock
And the other one is, if you don't want to do that, there's one called Screen Studio [tool:Screen Studio], if you're on a Mac. It's 230 bucks. ▶ If you're recording anything under three minutes, go Screen Studio. If you're doing full-blown YouTube videos, I would do TeleTV.

00:20:06 - Brandon Hancock
Seriously, check out TeleTV. I think that's the one you'll like the best.

00:20:10 - Brandon Hancock
Yeah, Descript [tool:Descript] is another great one, too.

00:20:17 - Brandon Hancock
▶ The hard part is just making content consistently. That is the hardest part. So flip a coin and go.

---

<!--SEGMENT
topic: Vector Stores, Supabase, and Document Chunking
speakers: Marc Juretus, Brandon Hancock
keywords: vector store, Chroma, Upstash, Supabase, Postgres, Drizzle ORM, LangChain, docling, PDF chunking, embeddings, similarity search, Google Cloud ADK, Agent Development Kit, MCP, Notion API
summary: Marc shares his deep dive into vector stores using Chroma and Upstash with LangChain, and his goal of deploying an app to Google Cloud using ADK. Brandon recommends Supabase with Drizzle ORM for production vector store setups, explains proper schema migration practices, and advocates for docling as the best PDF chunking tool. The segment also covers MCP's value proposition for wrapping third-party API endpoints.
-->

00:20:28 - Brandon Hancock
Marc, you are up next, buddy.

00:20:33 - Marc Juretus
My OCD kicks in — when I didn't know as much about vector stores, guess who was playing with vector stores all last week? So I did work in Chroma [tool:Chroma] and then I made one with Upstash [tool:Upstash] and I have LangChain [tool:LangChain] talking to it. Basically it consumes a couple of Wikipedia pages up to a vector store that's searchable.

00:21:00 - Marc Juretus
I got enough comprehension on it. So I want to move on. My objective still is to publish an app on Google Cloud using ADK [tool:Google Agent Development Kit]. I basically built every one of those examples you had.

00:21:21 - Marc Juretus
And then I went down the MCP road and I want to see how you sell me otherwise. Because as soon as you release that, I'm going to watch your video — I pretty much left that with what you just said. Like, why am I going to do this when I could just define functions to do all these tasks?

00:22:00 - Brandon Hancock
So if you are looking at going like a full-blown real-world application, I would look at using Supabase [tool:Supabase] for handling authentication, blob store, and database. And what's so nice about the Supabase database is it's a Postgres database, so you can easily make it a vector store as well.

00:22:50 - Brandon Hancock
For a freelancing project right now, that's exactly what I'm using. He needed a vector store, so I was like, all right, Supabase instantly is the route I went down.

00:23:40 - Brandon Hancock
The only thing I would change — so you're going to want that link I just sent, it's a YouTube video. The only thing I would change is in the video, you're going to see me manually make tables and create them inside Supabase. ▶ What you want to do instead is use Drizzle [tool:Drizzle ORM] as your ORM. So you create a Drizzle schema, and this is how I'm creating my vector table for storing vectors.

00:24:26 - Brandon Hancock
The most important part is the embedding, because that's what you're going to do the similarity comparison on. You need to set up the dimensions, and then you just need to make it easy to index so when you are doing a similarity search, you can do it faster.

00:25:25 - Brandon Hancock
▶ This is so much easier because it's like, generate, and then I run migrate. So yeah, really like Supabase for a vector store.

00:25:52 - Marc Juretus
So to summarize the vector databases for what you're doing in industry with projects — basically you're creating knowledge bases, vectorizing that data, so they have specific models to call?

00:26:00 - Brandon Hancock
<A>Exactly. The individual use case is to help emergency medical responders. There are huge documents that are hundreds of pages, and they need to be able to look up: a person is experiencing this, what is our protocol? And then it's like, oh, that happened on page 345. Here's a link to the page. Here's a summary of what I see on the page. But go obviously cross-reference to make sure there's no hallucinations.</A>

00:26:33 - Brandon Hancock
And then finally — docling [tool:docling]. If you're going to be parsing big documents, docling is — there's no substitute for ease of chunking.

00:27:42 - Brandon Hancock
▶ Old-school way was: hey, I'm just going to start grabbing tokens until I run out of tokens, and then start the next chunk. But that's actually not the best way to chunk PDFs, because you really want to grab stuff in paragraphs or under headers. Docling does a phenomenal job. It is the best chunking tool out there for extracting information from PDFs.

00:29:09 - Marc Juretus
<Q>What MCP are you consuming — what third-party APIs are you consuming in the tutorial about to come out?</Q>

00:29:16 - Brandon Hancock
<A>The one I used was Notion — that was the main one I used. Notion was the easiest one just to get spun up.

▶ The quick cheat code that MCP gives you is: let's say you wanted to interface with a common package like Notion. They have an API with like 40 endpoints. So if you wanted to use Notion effectively, per endpoint, per API request you could possibly make, it is up to you to code up that tool. MCP — specifically as it has grown and evolved — these frameworks are going, hey, we know people want to use agents against our tool now, so for every endpoint, hey, we've already built the tool. Just use our MCP server.

So it's almost like you're just installing it. It feels like the Matrix when you're like, I want to learn Notion, and then boom, now I can use it. You just instantly get access to every endpoint.</A>

00:30:37 - Marc Juretus
▶ If you can write up your own custom tools and suddenly some stuff changes, you don't have to worry about that with MCP. You just point to that, and if they update their endpoint, your code's fine.

---

<!--SEGMENT
topic: Housing Cost Calculator App Demo and Chat Feature Design
speakers: Paul Miller, Brandon Hancock, Jake Maymar, Bastian Venegas
keywords: Vercel AI SDK, structured outputs, tool calls, Next.js, Lovable, Cursor, scenario modeling, housing policy, New Zealand, chatbot UI, Excalidraw, wizard onboarding, persona selection
summary: Paul demos a web app that models the cost impact of housing development policies for New Zealand economists and government officials. He wants to add a chat interface that converts natural language into API calls and returns structured chart data. Brandon recommends the Vercel AI SDK for structured outputs and advises deferring the chat feature until UI requirements are confirmed. Jake suggests preset scenario buttons for quick user onboarding.
-->

00:31:08 - Brandon Hancock
Paul, you are up next, buddy.

00:31:14 - Paul Miller
Hey, guys. So I've got the app and we're pretty much in launch mode now. We're just getting users. I thought I'd give you a little demo and I was keen to get everyone's input.

00:31:54 - Paul Miller
So just a bit of background. This is an app that helps economists and people in the New Zealand government understand the consequences of their policies on reducing the cost of building new housing subdivisions — the cost of land.

00:32:34 - Paul Miller
So kind of — can you see my Excalidraw [tool:Excalidraw]?

00:32:40 - Brandon Hancock
Yes, I love it. You're speaking my love language, Excalidraw.

00:33:09 - Paul Miller
I went down the Lovable [tool:Lovable] path on that. Once things quieten down a little bit, I'll pull the app out of GitHub so I can put that into Cursor [tool:Cursor] so it can guide me through updating, because Lovable gets a bit expensive and it's a bit away from the code.

00:33:41 - Paul Miller
What might be better is someone that just asks a question to say, look, I'm thinking of doing the following things. Let's convert that question into a call to the API and then just come back with a chat response and display the charts.

00:35:40 - Paul Miller
So the app's kind of improved quite a lot here. On the left-hand side is the input form. So you can go and do things to change the inputs. And this goes and tells you then what the resulting cost is over here in terms of the land price.

00:36:48 - Paul Miller
What I've gone and added is that you can start adding a whole lot of scenarios where you change certain inputs in one scenario, and then you can add that scenario and compare it all.

00:37:39 - Paul Miller
What I was thinking in terms of the chatbot is that instead of having the input up here, we have a little chatbot window, start talking, and it creates the scenarios out of the API.

00:38:30 - Brandon Hancock
<A>Okay, so high level — I'm about to drop a link in the chat. What's really nice is you could get away with doing everything with the Vercel AI SDK [tool:Vercel AI SDK].

So the good thing is, every time you have been calling your calc API, I'm guessing in there there's probably just a bunch of functions that are just math — takes in four inputs, calculates the output. Well, each one of those could be a tool call, which is nice because then all you need to do is recreate those tool calls and add them as tool calls to your model.

But I also think you need to go a little bit deeper because in your case, you want to return structured outputs. You could probably return back the data that you want to put in the UI. So like, for example, if you had some charts you wanted to show, you could just be like, hey, I'm trying to not only get a chat response, but I'm also trying to get back data that I could use in my form.</A>

00:43:22 - Jake Maymar
<Q>As you mentioned persona — would it make sense to have, like, select a persona? Because it would be kind of interesting to see which of these fields has the most impact.</Q>

00:43:29 - Paul Miller
<A>Yeah, that's a good suggestion, because not to put labels on politicians, but they're very tight on time, and they've got a very narrow perspective of which lever they kind of want to look at. So an economist might want to delve down into the detail and work a model, while a politician might say, well, just give me the three options and tell me the outcome.</A>

00:45:00 - Jake Maymar
<Q>What if there was basically a button that says Houston, right? The Houston scenario, this scenario, this scenario, and you just instantly click that button, it changes all the situation. Because you want to get to your point as soon as possible.</Q>

00:46:04 - Paul Miller
<A>Yeah, yeah. At the moment, it sits kind of as a sub-app that's going to be on a website with a whole lot of supporting material around videos, around what's the problem we're trying to solve, who are we, all this kind of stuff. And then go down this path if you want a detailed calculator, step by step.</A>

00:47:15 - Brandon Hancock
▶ Real fast, last tech piece of feedback: I would stay away from adding the chat feature until you get confirmation from your users on what they want graphically. The reason why is your chat output — the structured outputs you're going to set up in your chat — are going to be 100% coupled to whatever output your visualizations are expecting. So if there's any change that they want, you're going to have to go back and redo the chat. I would do chat last.

00:48:47 - Brandon Hancock
▶ Basically you're just defining the schema that you want it to return, and it'll do it. The AI SDK [tool:Vercel AI SDK] is awesome.

---

<!--SEGMENT
topic: Bolt.new Hackathon Experience and ADK Hackathon Opportunity
speakers: Ty Wells, Brandon Hancock
keywords: Bolt.new, hackathon, Supabase, skill matchmaker app, hallucination, AI coding tools, Google ADK hackathon, prize pool, community hackathon, Cloudflare, Docker
summary: Ty shares his experience building an AI skill-set matchmaker app during a community Bolt.new hackathon, describing significant frustration with Bolt's hallucinations and poor Supabase integration. Brandon highlights an upcoming Google Agent Development Kit hackathon with a large prize pool as an alternative opportunity. The segment provides a candid negative review of Bolt.new for production use.
-->

00:49:15 - Brandon Hancock
Ty, you're up next, buddy.

00:49:19 - Ty Wells
Hey, guys. Well, I'm recovering from a Bolt.new [tool:Bolt.new] hackathon.

00:49:32 - Ty Wells
Well, let's just say I'm missing some hours I'm not going to get back. It was Friday, Saturday at 11 Central until Sunday at 8 p.m. Central.

00:50:04 - Ty Wells
So this is — we built basically an AI skill-set matchmaker. This is our dashboard here. Shows us people and their profiles, basically what skill sets they have.

00:51:42 - Ty Wells
So you can obviously filter and show, and you can send them a message. This is internal messaging, assuming it's working, to get a notification ping.

00:52:27 - Brandon Hancock
<Q>So what was your experience like with Bolt? And then what did y'all end up using for database?</Q>

00:52:36 - Ty Wells
<A>Bolt was not a great experience. It hallucinates like crazy. That's not the tool I go to, but that was the deal. It is seriously flawed in whatever model they're using.

And with Supabase [tool:Supabase], it destroyed Supabase. I mean, don't let it touch your Supabase. It really doesn't do a good job setting up — losing track of where tables are and asking me to tell it where the code is in the codebase. It was just crazy.</A>

00:53:20 - Ty Wells
I gave it a prompt telling it that if I don't get this fixed, my family's not going to eat tonight. It was rather comical how it responded because it kept that in context. It says, oh no, I fixed it. Your family will be able to eat. They'll be proud of you. And I'm like, it's still broken.

00:55:53 - Brandon Hancock
Let me share real fast — if people are looking for hackathons, here's one that I might take seriously. So this is the Agent Development Kit [tool:Google Agent Development Kit] hackathon. The prize pool is insane — grand prize winner, North America winner, there's just a ton of money they're giving out.

00:56:20 - Brandon Hancock
▶ It's free to sign up. There's a month until it's done. Basically, it's just use Agent Development Kit to do anything. And the thing that's interesting is it's not a timed thing — you can make it and publish it anytime. [link:Google ADK Hackathon]

00:57:24 - Ty Wells
Oh, no, because I have to use Bolt, and I'm not going to do it. It would be like pulling my hair out, as you can see. There is none.

---

<!--SEGMENT
topic: Supabase MCP Integration in Cursor
speakers: Ty Wells, Brandon Hancock
keywords: Supabase MCP, Cursor, MCP JSON config, PostgreSQL, access token, mcp.json, Supabase MCP server package, database connection, Cursor IDE, developer tooling
summary: Ty raises a persistent issue connecting Supabase to Cursor via MCP, where only the query tool appears and it works inconsistently. Brandon diagnoses the problem as using the wrong MCP package — directly connecting to Postgres rather than the dedicated Supabase MCP server — and shares the correct package configuration and a screenshot showing it working live.
-->

00:57:50 - Ty Wells
I'm having a hell of a time getting Supabase connected in my Cursor [tool:Cursor]. It only gives me the query tool. And a lot of the time, the query tool doesn't even work. Sometimes it works, sometimes it doesn't. It does not work with my access token, and I have to use the URI to get in.

00:59:03 - Ty Wells
Well, if I take it out, then it's not going to work, but I'll show you what it looks like.

00:59:28 - Brandon Hancock
<A>So the password would be in there, but it's taken out. Instead of `@model-context-protocol/server-postgres`, can you change it to this? I'm dropping it in chat right now.

What right now you're trying to do is directly connect to Postgres. That didn't work for me either. I had to directly connect to the Supabase MCP server [tool:Supabase MCP server]. So change line nine in your `mcp.json` to get rid of that package and change it to the one I sent you, and then all you need to do is go create a Supabase access token — it works.</A>

01:00:51 - Brandon Hancock
Yeah, just to show that it works — what tables do I have in Supabase? It gets the project, it gets the table, and then it lists all the tables right here.

01:01:39 - Brandon Hancock
▶ Final thing, Supabase MCP — I'll show you the instructions I followed. [link:Supabase MCP setup instructions]

---

<!--SEGMENT
topic: Bastian's Database Migration Issues and AI-Powered Civic Investigation
speakers: Bastian Venegas, Brandon Hancock
keywords: Supabase, database migration, Prisma, Drizzle ORM, schema changes, Selenium, web scraping, docling, PDF processing, LLM, government permits, Regex, DuckLink, civic tech
summary: Bastian reports struggles with Supabase schema migrations using Prisma and endorses Drizzle ORM as a better alternative. He then shares a remarkable side project: using Selenium to scrape a government permit website, docling to process over 1,000 scanned PDFs, and an LLM to clean the output — ultimately uncovering an illegal construction permit next to his home. Brandon highlights this as a powerful real-world demonstration of AI's ability to compress months of manual work into days.
-->

01:01:51 - Brandon Hancock
Bastian, buddy. What's going on?

01:02:00 - Bastian Venegas
I have been trying to make compatible, working for delivering the last phase of work for a client. Talking about the database and Supabase, I had some issues with the database migration, because I had to change the schema, and it was kind of a pain to do it inside Supabase, because it kind of lost track of the previous migrations, so it just wanted to delete all of the tables. Obviously, that's no good. So I spent until 2 or 3 a.m. just trying to work that out.

01:02:47 - Brandon Hancock
<A>▶ Using Drizzle [tool:Drizzle ORM] as your ORM is a cheat code, because that's what sets up those migrations, that's what'll let you apply those migrations. Because if not, you're doing exactly what you're describing — you have to do everything in the SQL query editor, and it's just not infrastructure as code. So things can get lost, it's harder to keep up, and it's hard to replicate. If anything does go wrong, you're starting over from zero.</A>

01:03:18 - Bastian Venegas
Yeah, I was using Prisma [tool:Prisma], but it was kind of hard. And also Supabase has a nice feature where if you're doing stuff like this and you want to do it securely, you can clone the database that you have in production and restore it into a new project, and then you can make all of the changes there and try everything with a real database without running into hiccups.

01:04:08 - Bastian Venegas
Also on a side note — there are people building a big warehouse just next to my house. And they are not respecting any of the fire hazard regulations. So I had to scrape the government website that obviously doesn't have an API, where you can check every permit that your city has given to everyone.

01:05:00 - Bastian Venegas
There was no filter by address or property code or anything, so I just had to automate a Selenium [tool:Selenium] Chrome browser. And I actually used docling [tool:docling] because I was able to retrieve a CSV file that contained all of the permits for each month, so I had to do that for like 36 months. Then I had to use Regex to extract all of the links to every PDF that they delivered — so it was over 1,000 PDFs. I processed that with docling, which made a really good job.

01:05:36 - Bastian Venegas
And then I had a small step where I just asked an LLM [tool:LLM] to format this in a more friendly way, because docling can have some errors when they are mainly scanned documents, not if it's truly a PDF that was built electronically. So the LLM made the document with the corrections, and I was able to find the damn permit that they were obviously doing something illegal in the end.

01:06:13 - Bastian Venegas
So that was a fun thing, and it also talks about how every government tries to — I don't know if intentionally, but I guess kind of yes — obfuscate information that makes it really hard for a concerned citizen to get the information they need.

01:06:41 - Brandon Hancock
What's crazy, though, is it would have taken a person manually — forever. Like, you would have spent the next three months doing nothing but downloading a CSV, skimming it, no, this one doesn't work. This would have taken months of work, and instead it was like two days.

01:07:10 - Bastian Venegas
And obviously the PDFs were not searchable either, so you'd have to manually read every one of the over 1,000 PDFs. So I was really glad I knew how to do this.

01:07:19 - Brandon Hancock
Bastian, I told you — AI and Bastian sticking up for the little man. Not all heroes wear capes.

01:07:48 - Bastian Venegas
And they actually stopped building the thing, so I think it kind of worked because I went there and said, hey, you're not respecting the law. I quoted the law. And I said, you have this permit from 2023, this date, it hasn't been modified, so just stop it.

---

<!--SEGMENT
topic: Gemini Diffusion Architecture Deep Dive
speakers: Juan Torres, Brandon Hancock, Paul Miller
keywords: Gemini Diffusion, diffusion models, autoregressive models, LLM architecture, masked diffusion, LADA model, GSM8K benchmark, token generation, reversal reasoning, in-context learning, AWS SQS, ETL pipelines
summary: Juan presents an analysis of Google's Gemini Diffusion model, explaining how masked diffusion architecture differs from autoregressive token generation by processing the full output holistically rather than left-to-right. He shares benchmark results showing improvements in math reasoning (GSM8K), reversal reasoning, and instruction following. The segment closes with a brief discussion of AWS SQS for ETL job queuing.
-->

01:08:17 - Brandon Hancock
Juan, you're up next, man.

01:09:07 - Juan Torres
I did publish an article regarding the architecture of Gemini Diffusion [tool:Gemini Diffusion]. Gemini Diffusion is essentially using a diffusion architecture, much like you would use stable diffusion in order to denoise an image, instead of the sequential autoregressive modeling principle that is used for most LLMs [tool:LLM].

01:09:46 - Juan Torres
There are already indicators that Gemini's diffusion models are performing in a very significant, improved way compared to autoregressive models. And this is just based on the change in the modeling principle — the probability principle of the models they're using.

01:10:29 - Juan Torres
That's the paper that we reviewed [link:Gemini Diffusion / LADA model paper]. I recommend you guys check it out because the diffusion model is still in — you still have to get on the waiting list.

01:11:20 - Brandon Hancock
<Q>Explaining it like I'm five years old — my understanding of diffusion models... can you break it down?</Q>

01:11:31 - Juan Torres
<A>The architecture of the current models you're using, like ChatGPT [tool:ChatGPT], is like each token — they try to review it linearly, one by one. So if you see ChatGPT creating code, it creates code in a linear, sequential way, much like if you're reading a book from left to right.

With the diffusion model, what essentially happens is that the prompt is taken from a holistic view from far away. Like instead of reading each word from left to right, you're seeing the whole page, and you're seeing all the words at the same time. So what you're doing is masking all the words, and in each step, what you're doing is denoising the page in order to make some letters visible, and progressively it becomes more clear what each word says. And based on that, the model starts developing code from the bottom and the top and the middle, instead of going from left to right.

▶ That is one of the powers of this architecture — it no longer is cursed with some of the limitations of the current regression model, which is that it cannot engage in a logistical principle like if A equals B then B equals A, because it's not very good at making a regressive logical conclusion. With this, you overcome that limitation.</A>

01:13:17 - Brandon Hancock
<Q>How does it compare to other models? Is it better, or does it have the potential to be better?</Q>

01:13:47 - Juan Torres
<A>It seems that on the benchmarks, with LADA [tool:LADA model] with 8 billion parameters — the model that was being tested openly — in domains like the GSM8K performance, it does much better and has a stronger performance than those of the autoregressive models. And it performs at par with LLaMA 3 [tool:LLaMA 3], especially once you turn to dialogue and reasoning tasks, instruction following, and reversal reasoning. That's one of the main characteristics and improvements that it has.</A>

01:19:08 - Juan Torres
I do have a question as to whether people have used AWS Glue [tool:AWS Glue] as their ETL data pipeline as a service, or what other cloud service you use in order to get ETL data pipelines to work — any jobs that you want to not execute through your computer.

01:19:47 - Paul Miller
<A>There are other message queuing options on AWS. Glue is an option, but there's some more traditional type — if you think of the old computing model, where you'd add a message into a queue and then it processes it in quite an open, standardized way. Like everything with AWS, this is quite proprietary, so whether that's something you want to follow — I'm sure there's an open-source variant of it you might want to use.</A>

01:21:03 - Brandon Hancock
You're going to SQS [tool:Amazon SQS], right? Is that what you're suggesting, Paul?

01:21:05 - Paul Miller
Yeah.

---

<!--SEGMENT
topic: Complex PDF Invoice Extraction Challenge
speakers: Jake Maymar, Brandon Hancock, Andrew Nanton, Bastian Venegas
keywords: PDF extraction, docling, OCR, Tesseract, Azure Document Intelligence, Surya, Marker, batch processing, invoice parsing, Regex, Claude Sonnet, Gemini 2.5, computer vision, HIPAA compliance, unstructured data
summary: Jake describes an extremely difficult invoice extraction project involving 800-page PDFs with no consistent formatting, where data on page 4 may relate to page 206. He is using docling, Regex, and multiple LLMs (Gemini 2.5, Claude Sonnet 4) for verification. Andrew recommends Azure Document Intelligence for structured extraction and the Surya+Marker library combination, and notes that docling supports swappable OCR engines including Tesseract and OCR Mac.
-->

01:21:17 - Brandon Hancock
Jake, you are up next.

01:21:24 - Jake Maymar
I don't have a lot, mostly just heads down, trying to figure out some stuff. Sometimes I feel like I've bitten off way more than I can chew.

01:21:43 - Jake Maymar
One of the invoices — I'm doing a lot of data extraction, and I almost think that they made these invoices so they couldn't be extracted. They are some of the hardest things I've ever seen. The easiest one is 800 pages.

01:22:26 - Jake Maymar
There's a whole bunch of things we're trying to extract, but there doesn't seem to be any pattern for how they appear in this readout.

01:22:41 - Jake Maymar
So I'm definitely doing batch processing. But each page is different and unique. So I'm building a format — basically pattern recognition for that format — and trying to apply it to other pages. The biggest problem is it keeps missing data.

01:24:29 - Jake Maymar
I did a Regex back end as well, just to kind of run two things against each other. So I was verifying the data with significant LLMs — Gemini 2.5 [tool:Gemini 2.5], Claude Sonnet 4 [tool:Claude Sonnet 4] is amazing. It's totally amazing. And then I think it was 4.1, and then there is a computer vision part about it.

01:25:00 - Jake Maymar
The biggest problem is when I get the results, I have to hand-verify the results. Because the problem is you have a set of charges and a set of descriptions, and some are credits and some are unusual numbers and some are charges. But then you have to go down — so like maybe page four and now page 206 are connected.

01:25:33 - Brandon Hancock
That's disgusting.

01:25:44 - Brandon Hancock
▶ Bastian just pointed out an idea to force OCR with docling [tool:docling]. And then I was also going to call out Cyril in the community — he was focused on something pretty similar from what I remember him describing.

01:26:33 - Andrew Nanton
When I was looking at PDF processing stuff, in addition to docling, I also looked at one called Surya [tool:Surya], which is paired with something called Marker [tool:Marker] for Markdown output.

01:27:12 - Andrew Nanton
I was able to get docling to process a 16,000-page file. So I mean, that's pretty impressive, and I never found anything else that would do something that large.

01:27:23 - Andrew Nanton
▶ But I know that Azure's Document Intelligence [tool:Azure Document Intelligence] — they have two different modes: more like standard OCR, and then a structured output thing that you can customize. They have a pretty neat little web interface for it where you can play with one- or two-page PDFs and see what the output is or drop in one of your own.

01:29:06 - Andrew Nanton
▶ Docling has some weird options in there — you can get its intermediate format or Markdown or JSON, and you can switch out which OCR engine it uses. You can use OCR Mac as the engine if you're on a Mac, or Tesseract [tool:Tesseract], or some other stuff. It's really buried in the documentation, but if the OCR is tripping you up, it might be worth diving in to see if one of the different OCR engines gets better results on your documents.

01:29:35 - Jake Maymar
Yeah, we're using Tesseract.

01:29:43 - Andrew Nanton
I just tried OCR Mac because it was fast on my MacBook, and it got pretty good results. But given the scale of your problem, it might be worth trying a few different ones and see what you get.

01:29:59 - Jake Maymar
Yeah, that's really helpful. I was almost trying to get to like an exact sort of representation of the invoice and then trying to flag certain areas, but that ended up being a lot of manual work.

---

<!--SEGMENT
topic: Telegram Music Bot Deployment and YouTube Download Feature
speakers: Aleksandr, Brandon Hancock, Bastian Venegas
keywords: Telegram bot, FFmpeg, yt-dlp, Python, Railway, audio processing, reverb, speed change, Shazam-like search, YouTube download, cookies, session hijacking, cloud deployment, pip
summary: Aleksandr shares his Telegram music bot, now deployed 24/7, which can apply audio effects (reverb, speed changes), search for music by text or voice similar to Shazam, and will soon support YouTube video downloads. Bastian warns that yt-dlp often gets IP-blocked on cloud providers. Aleksandr explains his workaround using browser cookies for authentication. Brandon issues a security warning about cookie hijacking risks.
-->

01:30:46 - Brandon Hancock
Alexander, you're up next, man.

01:30:52 - Aleksandr
Now I'm continuing to work with my Telegram bot [tool:Telegram], music Telegram bot. And this week I had to add new functions for upgrading music files, and I had to deploy my project in a real way, and now my bot is working 24 hours a day.

01:31:38 - Brandon Hancock
<Q>So you have the app deployed — what is it officially doing for your different music files?</Q>

01:31:49 - Aleksandr
<A>My bot can change, for example, speed. You can use this bot to upgrade music — if you want to make a reverb version, or you can make different compositions with different effects. You can also use three or five effects at one time. And also the first function of this bot is that it can find all music that you want. You can only write some words from the text, or author, or you can also say it with voice. It works like Shazam [tool:Shazam].</A>

01:32:44 - Aleksandr
And I want this week to add a new function — a person who uses the bot can download a video from YouTube [tool:YouTube].

01:33:11 - Brandon Hancock
<Q>Under the hood — what tool are you using to make all those changes?</Q>

01:33:24 - Aleksandr
<A>Python, FFmpeg [tool:FFmpeg]. I also use different libraries — I ask GPT what can I add to my bot and what function would I learn to write code. I also use yt-dlp [tool:yt-dlp] for audio and JSON traceback and another import things for music.</A>

01:35:11 - Bastian Venegas
<A>▶ I have used the same library that you were using. First, always keep it up to date, because YouTube is always playing this cat-and-mouse game. But it usually works pretty good locally. If you deploy it to a cloud provider, they will likely have that IP address flagged, and you won't be able to download anything. So you may want to try different providers in case you find one that's not blocked.</A>

01:35:44 - Aleksandr
I found this problem, and I found another way. I downloaded with Chrome — I asked GPT what edition can I use, and it told me I can download the "Edit This Cookie" extension. And in this add-on I found all my cookies, I downloaded them. And now my YouTube is from the account that can download all music and videos. And with my cookies from my account, I can use and download all music with Railway [tool:Railway].

01:37:10 - Brandon Hancock
▶ Alexander, super quick piece of advice. On the cookies — I would be careful to make sure someone doesn't have access to them, meaning I would not share them with others. Because there's a thing called session hijacking — if someone has your cookies, they could potentially do anything on behalf of your account. So just be careful when you are using tools to make sure they are local and not sharing. It's called cookie hijacking. Just be careful.

01:37:52 - Brandon Hancock
▶ I would love next week if you have time to do a quick demo of some of the music stuff. I think that'd be pretty cool.

---

<!--SEGMENT
topic: Pharmaceutical Multi-Agent Orchestration System
speakers: Mauri Lindberg, Brandon Hancock, AbdulShakur Abdullah, Bastian Venegas, Jake Maymar
keywords: multi-agent orchestration, Agent Development Kit, ADK, CrewAI, N8N, custom GPTs, pharmaceutical expansion, clinical trials, regulatory compliance, sequential workflow, Anthropic prompt generator, XML prompts, JSON prompts, Mermaid diagrams, Excalidraw
summary: New member Mauri (Finland/Paris) presents a plan to orchestrate 17 custom GPTs into a unified pharmaceutical geographic expansion analysis system that can assess feasibility of bringing a drug molecule from one region to another. Brandon whiteboard-demos a sequential ADK workflow (find docs → categorize drug → analyze feasibility → generate report) and recommends the Anthropic Prompt Generator for creating better agent instructions. The group debates XML vs. JSON prompt formats across different LLMs.
-->

01:38:32 - Brandon Hancock
Mari, you're up next, man. How are you doing?

01:38:37 - Mauri Lindberg
First time here. I'm from Finland, living currently in Paris, France, and I'm honored to be with you guys here. I feel like I was trying to find an analog — I feel like talking to Ferrari engineers, and I'm kind of trying to ask, when can I have a test drive?

01:39:21 - Mauri Lindberg
One of my suggestions or ideas — is there a matchmaking platform for developers and customers going through a website, having a prompt engineer asking them, what is your pain point? What kind of an agent would you like to have? And then there would be a library of guys who would just go in there and choose a job, and they would solve those problems.

01:40:04 - Mauri Lindberg
I'm currently building a swarm of agents for the pharmaceutical niche sector. I have a consultant who is doing geographical expansion — bringing from one region pharmaceutical products to a new region. It's a very complex, multilayered operation.

01:40:46 - Mauri Lindberg
You embark on a project and you start bringing a product from one region to another. And then all of a sudden, after working on this for a year or two, there was somebody in a clinical trial in late phases bringing with big money the same molecule into that same market, and all of your project was completely in vain.

01:41:18 - Mauri Lindberg
I've created so far 17 different custom GPTs [tool:custom GPTs] that do independently these jobs. But now I'm looking for an orchestrating layer to where I could just say, can I take from Taiwan this molecule — is it feasible to take it to Germany? And it would delegate that job to all of these little niche areas to check it out, and five minutes later, my consultant would have a presentation saying, it's not feasible, these are the reasons, or yes, you could make this amount of money.

01:42:17 - Brandon Hancock
<A>No, I love this. This is my favorite type of problem because it's where AI meets real-world problems.

So here's the main thing I would do for you. The basic question is: is this molecule feasible to bring from Taiwan to Germany? That's a geographical expansion test.

So here's what you would do. You have currently 17 independent agents. The next level is where a framework like Agent Development Kit [tool:Google Agent Development Kit], CrewAI [tool:CrewAI], or LangGraph [tool:LangGraph] would be helpful, because they're multi-agent orchestration systems.

What you could do is create a root agent — what you'll call like an HR agent. In this root agent, what's so nice is in your case, to answer this question, it's actually a sequential workflow. So it's like: find relevant docs → categorize drug → analyze feasibility → generate report.

This is literally what you could do inside of Agent Development Kit. This would all go in something known as a workflow — a sequential workflow where agent one does work, stores the results to memory, then agent two does work, updates memory, agent three does work, updates memory. So each agent's doing work and then sharing results with the next guy.</A>

01:48:49 - Mauri Lindberg
<Q>So is it some kind of a tool like N8N [tool:N8N] or Make.com [tool:Make.com] or something?</Q>

01:48:50 - Brandon Hancock
<A>It is. It's called Agent Development Kit. It is a little bit more programming-focused. So if that's not your style, N8N works great as well. It's the same thing in code or no code — you're taking a request, routing that request to the proper workflow, going through the workflow, and then generating the result.</A>

01:50:43 - Mauri Lindberg
<Q>How close are we in the world that I could just talk to some kind of a bot to develop these agents? I participated in Paris a couple of days ago with Agent Force Congress, and they allowed me to talk to a bot to create an agent. We created the agents there just by me talking to a prompt engine.</Q>

01:51:16 - Brandon Hancock
<A>So Anthropic has a phenomenal tool for creating initial prompts — the Anthropic Prompt Generator [tool:Anthropic Prompt Generator]. You just brain dump what you want the prompt to do, and then it generates a better prompt that will perform better inside of an agent. So you just brain dump what you want, and then it'll create the prompt. [link:Anthropic Prompt Generator / Claude console]</A>

01:53:00 - AbdulShakur Abdullah
I used it before, but I found myself going directly into Claude [tool:Claude] and using it, kind of telling it, hey, improve my prompt. And Claude is really good at just having at it.

01:53:32 - Bastian Venegas
In the past, I have used this tool by Anthropic called the Metaprompt Generator [tool:Anthropic Metaprompt Generator]. So it has like a huge prompt in a Google Colab notebook, and it asks you a few questions — like a four-part question. And then you get the final template that's a prompt you can use to generalize for stuff like this.

01:55:28 - AbdulShakur Abdullah
▶ I found that whenever I get Gemini [tool:Gemini] and ChatGPT to help me with prompt engineering, they both prefer JSON output to get consistency, versus Anthropic's Claude model, which prefers XML.

01:56:00 - Brandon Hancock
▶ Definitely recommend checking out all the links dropped in chat for Mari.

---

<!--SEGMENT
topic: Windsurf SWE-1 Model Review and Website Recovery
speakers: Nate G, Brandon Hancock, Andrew Nanton
keywords: Windsurf, SWE-1, Cursor, Gemini 2.5 Pro, DigitalOcean, droplet, SEO optimization, N8N, Google Sheets, Cron job, GitHub, website deployment, .edu Cursor discount
summary: Nate shares two updates: he accidentally deleted his DigitalOcean droplet and used Windsurf with the SWE-1 model to rebuild and redeploy his website, praising SWE-1 for staying focused on requested changes. He also started an N8N Cron job to process Google Sheets billing data. Brandon recommends Gemini 2.5 Pro in Cursor as his current favorite model. Andrew offers a counterpoint that SWE-1 over-architected his project, and shares a tip about free Cursor access with a .edu email.
-->

01:56:26 - Brandon Hancock
Nate, you look so stoic, so comfy. What's going on, buddy?

01:56:34 - Nate G
So a while back, I had some guy build me a nice rig with a 4090 in it, and it's been sitting in my basement in my theater room for months, and the only thing that's been happening is my daughter's been playing games on it. But I finally decided it was time for me to start using it.

01:57:07 - Nate G
But I have a couple of — just a funny thing. ▶ Don't ever cancel your DigitalOcean [tool:DigitalOcean] account because you can never get your droplet back if you cancel the account. I thought, I'm not using this account, why do they keep charging me $12? So I canceled it. Well, it turns out my website went down the next day.

01:57:47 - Nate G
So I went in, and I will say this — a plug for the SWE-1 [tool:SWE-1], which is the Windsurf [tool:Windsurf] model. Right now it's free to use. And I used SWE-1, and it was the best I've seen in all of the LLMs as far as just helping me kind of fix all my problems on my website.

01:58:26 - Nate G
In the past, a lot of times I'm sure we've had this when we're using these, where it starts changing stuff a lot. But I felt like SWE-1 was really good at just sticking to what I was asking it to do.

01:59:00 - Brandon Hancock
Real fast, Nate — if you get a chance, because do you have Cursor [tool:Cursor] as well?

01:59:11 - Brandon Hancock
▶ If you do, I would recommend my favorite model right now is Gemini 2.5 Pro [tool:Gemini 2.5 Pro]. It's included in Pro. Like, I'll have a video coming out at the end of the week recapping, hey, I've been building AI projects for a client. Here's everything I did to reduce it from what normally should have taken a month to like a week. And this is my favorite model that I was going to talk about in that video. So 10 out of 10, try that too.

02:00:00 - Andrew Nanton
I just wanted to offer a quick counterexample. So I'm currently using Windsurf and Cursor. My experience with SWE-1 has not been great. It really wanted to over-architect and over-complicate stuff that should be really simple. It's like, oh, you know, you should build this interfaces file, and then you'll have all these adapters to interfaces, and then you'll build a factory factory function. And it just was bonkers.

02:00:46 - Andrew Nanton
▶ On the Cursor side — I don't know if everyone else knows this, but I found somewhere on their website that if you have a `.edu` address, you can get a free year of Cursor [tool:Cursor]. [link:Cursor .edu free plan]

02:01:00 - Andrew Nanton
I've had pretty good results with Gemini 2.5, but I just can't quit Claude [tool:Claude]. It seems to constantly give me the best results, even though I have to remind all of them, hey, use the functions that are built into the libraries I'm using instead of reinventing the wheel every day.

02:02:00 - Nate G
What was cool was the one that I had built — it was like 80% of the way done — was still in my Windsurf account somewhere. So I opened it up, and Windsurf with the SWE-1 basically walked me through — I didn't use Docker this time. I just hosted it locally and then put it through the DigitalOcean droplet. And it walked me through step-by-step and was pretty good about doing that with me. And it's up and running now.

02:04:06 - Nate G
One of the cool things it did is I don't know how to do all the SEO side of stuff, and it was really great at doing that. I said, hey, can you optimize this for SEO? And it said, sure, and it did a bunch of stuff.

02:04:30 - Nate G
Also, I started my N8N [tool:N8N] Cron job to go back and search through all my Google Sheets [tool:Google Sheets] that I create when I do my billing process.

02:04:52 - Nate G
<Q>I got it to work as long as I gave it the sheet ID, but I don't know how to give it the folder ID and then have it search from sheet to sheet to sheet.</Q>

02:05:08 - Brandon Hancock
<A>Once you make a call to the Google Docs or Google API, I think there's a specific command to call like Get Sheets for a specific document. And then you're going to get back an array. And then I would just do a for-each on that array. So before you start processing each sheet, because right now I'm guessing it's automatically processing the first one — what you really want to do is for each sheet, take action. So you just need to do a quick check before going to the next step.</A>

---

<!--SEGMENT
topic: ADK Career Path, Cursor Workflow Tips, and Personal Branding
speakers: robertchirwa, Brandon Hancock, Andrew Nanton, Alex
keywords: Agent Development Kit, ADK, Cloud Run, FastAPI, Agent Engine, Cursor rules, personal branding, LinkedIn, YouTube, content creation, AI engineer career, data engineer transition, hackathon, Anthropic prompt generator, community-driven content
summary: Robert (transitioning from data engineer to AI engineer) shares a real job posting requiring ADK, Cloud Run, and Python skills, and outlines his learning path through Brandon's masterclass toward building an MVP. Brandon recommends Cloud Run over Agent Engine for production deployments and emphasizes publishing content on YouTube and LinkedIn to attract opportunities. Andrew shares a key Cursor tip: /generate cursor rule to automate prompt engineering for persistent project rules.
-->

02:06:12 - Brandon Hancock
Robert, you're up, buddy.

02:06:20 - robertchirwa
So today is my second call here. I'm jumping into the whole AI engineering thing straight with ADK [tool:Google Agent Development Kit]. I don't have any previous experience with CrewAI [tool:CrewAI], LangChain [tool:LangChain], or LangGraph [tool:LangGraph], so I'm jumping in right here.

02:06:44 - robertchirwa
As mentioned last week — Brandon mentioned, do I have Cursor? And of course, I could just talk to it. And then that gave me the aha moment — I'm not proficient in Cursor yet.

02:07:08 - robertchirwa
One thing that might be useful, Brandon, is if you had like a very simple video creating a very simple AI agent using Cursor as workflow — maybe use Cursor to create your root agent, as well as use the Anthropic Metaprompt Generator [tool:Anthropic Metaprompt Generator] to create like an instruction set, all using Cursor AI to get into the Cursor workflow. Because I'll be the first to admit that I'm relatively late to using agentic IDEs.

02:08:20 - Brandon Hancock
<A>No, 100% can do that. I think that would be helpful. Yeah, I can make a video on that very soon. So just a heads up, what I'm planning on doing next: one is just a high-level overview of, hey, I just did a freelance project. I'm going to share everything that I did to go from beginning idea conversation to end — just share what tips I used and how I used AI along the way. There will be some Cursor topics in there. And then yeah, I could do a follow-up one on how to use these tools to make better agents and prompts as a secondary one.</A>

02:09:26 - Andrew Nanton
▶ The one Cursor tip that I learned this week that really blew my mind is `/generate cursor rule` [tool:Cursor], which will generate a cursor rule. It will do some of that prompt engineering for you to make sure that it's a good rule for Cursor, and it will generate a rule for the project you're working on. So maybe give that a shot if you're running into an issue, especially if you're running into the same issue over and over again and then you start a new chat and it forgets.

02:09:55 - Brandon Hancock
▶ Cursor rules are a cheat code because I hate getting in arguments — I'm like, I told you 10 times, stop doing this. So definitely recommend: if you notice a common issue, rules.

02:10:16 - Brandon Hancock
Yeah, I didn't know you could do the forward slash generate rules, so thank you, Andrew. I'll probably do a post to aggregate tips — a community-generated tips and tricks post tomorrow.

02:11:00 - robertchirwa
I just shared this job application that I got today about ADK. So basically here they're looking for developing agent background on Google ADK, building APIs as seamless communication between web app and the backend, analyzing and monitoring system performance, and here's a major one — deploying onto GCP and Cloud Run [tool:Google Cloud Run].

02:13:21 - robertchirwa
The requirements here are strong Python skills, experience building AI-driven web applications, and last but not least, agentic frameworks such as either ADK or CrewAI background.

02:14:04 - Brandon Hancock
<Q>Is this a full-time position? Is this a freelance position?</Q>

02:14:08 - robertchirwa
<A>It's an hourly position — a contract, and potential contract to hire.</A>

02:14:30 - Brandon Hancock
<Q>You're trying to go for these kinds of jobs, right? This is your ultimate goal based off last week's chat?</Q>

02:14:36 - robertchirwa
<A>Yes. So basically what I'm doing is I'm rebranding from previously being a data engineer to becoming a junior AI engineer. I'm getting into ADKs, really getting into LLM orchestrations, and that type of workflow. Even if I have to take the next month off, just focusing on ADKs specifically — and maybe even using the hackathon that you shared as a true north point of reference for creating some sort of product that I can use as a demo MVP to be more competitive with such roles.</A>

02:15:16 - Brandon Hancock
<A>Did you get a chance to watch the AI authority video I did? Long story short, I would watch this video because the biggest issue I think developers run into is: even if you're the world's smartest AI engineer, if no one knows what you can do, it's just hard. When you do apply to jobs, it's hard to showcase that you're the best.

▶ My core recommendation is LinkedIn and YouTube. Even if your videos are not super high-polished, just every time you build something — quick demos, cap it at 30 minutes. Hey, in today's video, I'm going to show you how to deploy agents on ADK over to Cloud Run. You would be amazed once you make that video — there's potential for opportunities to come to you. Like Alex today at the very beginning of the call — he made a video and he already got an opportunity to go almost like for speaking and coaching. One video.

▶ Learning is one thing, but every bit you learn, you need to share at the same time just to really explode opportunities. Don't just share it on YouTube — share it on LinkedIn as well.</A>

02:19:29 - Brandon Hancock
▶ Quick point on that. The more me-focused something is, you'll notice a decline. Like people are in it for them — what's in it for me? The more you can make it like, I am building this for you guys, I built this so you — this took me 20 hours to learn how to do, I'm giving it to you in 10 minutes. That type of stuff crushes it. So as you're building stuff and sharing it with the world, the more it's "you" versus "I and me," the better it does.

02:20:10 - Brandon Hancock
Okay, I do got to run. So if y'all have any questions, anything, feel free — always shoot me a DM, make a post, and always happy to help. And yeah, I'll also do a post tomorrow about Cursor tips and tricks. So we'll have one aggregated spot. We'll turn it to a video — it'll be the first community-driven video. I'm pumped. Y'all have a great rest of your week. Bye, guys!

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was empty/unpopulated at processing time). All names have been passed through unchanged:

- Alex
- AbdulShakur Abdullah
- Paul Miller
- Marc Juretus
- Brandon Hancock
- Maksym Liamin
- Bastian Venegas
- Ty Wells
- Juan Torres
- Jake Maymar
- Andrew Nanton
- Aleksandr
- Mauri Lindberg
- Nate G
- robertchirwa