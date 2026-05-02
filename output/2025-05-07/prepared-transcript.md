=== SESSION ===
date: Unknown (likely early May 2025, references Cinco de Mayo)
duration_estimate: ~2 hours 40 minutes
main_themes: AI agent frameworks (Google ADK), production AI deployments, database tooling (Drizzle/Neon/Supabase), AI-assisted development tools (Cursor/Windsurf/Kline), customer discovery, HIPAA compliance, web scraping, PDF data extraction, creative AI applications

---

<!--SEGMENT
topic: Session Opening and Host Updates
speakers: Brandon Hancock
keywords: ADK, Google Agent Development Kit, OpenAI image generator, YouTube thumbnail generator, Fathom, AI Developer Accelerator, agent frameworks, tutorial, weekly coaching call
summary: Brandon Hancock opens the weekly AI Developer Accelerator coaching call, welcomes new members, and shares two upcoming tutorials: a deep-dive ADK workflow for a YouTube thumbnail cloner/generator, and a tutorial on the OpenAI image generation API. He frames the session format as a round-robin of wins and problems.
-->

00:03:50 - Brandon Hancock
Okay, cool. So what I'll do is I will kick things off, and I will kind of give you guys lay the land, especially if it's your first time here.

00:04:07 - Brandon Hancock
So this is the order I'm going to go in for today's call. I'll just go around the room based on the image I just sent. And it's pretty much just based on the order everyone joined. And if you're new here, welcome to the AI Developer Accelerator weekly coaching calls. We have a bunch of amazing fellow AI nerds here. And every week we hop on a call where we usually just go around round robin to talk about any problems anyone's stuck on or any cool wins that they just think the group would find interesting.

00:04:41 - Brandon Hancock
I'm going to share my screen first. So updates for me this week is I'll be releasing a new tutorial for you guys here probably on Thursday at this point. But I built a like a monster example for you guys of an ADK [tool:Google ADK] workflow. And basically what it does is it's a YouTube thumbnail generator like cloner, meaning you can pass it in a YouTube channel you want. From there, the agent goes off, scrapes that YouTube channel, figures out their style, downloads the thumbnails, asks you what video you want to do, and then it will create a thumbnail in their style.

00:05:30 - Brandon Hancock
The only other update is for you guys, this video came out the other day. If you have not got a chance to watch it yet, 10 out of 10 recommend checking it out. ADK, absolutely loving it right now. ▶ Probably one of the easiest to use agent frameworks I've seen between how easy it is to get agents up and going, plus how easy it is to deploy them.

00:06:13 - Brandon Hancock
And when we're starting to go around Robin, if you guys will probably try and keep it to like six-ish minutes per person that way, you know, six, eight minutes, that way everyone has time to go.

---

<!--SEGMENT
topic: Nissan Dealership WhatsApp Sales Bot Demo
speakers: Brandon Hancock, Maksym Liamin, Juan Torres, AbdulShakur Abdullah, Jake Maymar
keywords: WhatsApp, GPT-4.1, Supabase, Voyage embeddings, RAG, OpenAI, Anthropic, Azure, content filtering, car dealership, Nissan, Mazda, Mitsubishi, production deployment
summary: Maksym Liamin demos a live WhatsApp-based AI sales assistant deployed for a Nissan dealership in Mexico, handling 2,500–3,000 daily conversations. The segment covers the tech stack (GPT-4.1, Supabase, Voyage embeddings, Meta WhatsApp Business API), cost optimization from switching away from Anthropic/Azure, and the team's fast-ship approach to quality assurance without formal evals.
-->

00:06:32 - Maksym Liamin
Yeah, hello, hello. It's nice to see you again, guys. It's been, I think, two weeks since I haven't been here.

00:07:05 - Maksym Liamin
From my side, we are just like cruising with the project. It's going great. Right now, we just hit 1,500 active users. Everybody's liking the tool. We have around 2,500, 3,000 daily conversations with our bot. And yeah, we started approaching already other brands. We built all the stuff around it to support the sales, like the dashboards and stuff. Added new functionality. Just today, I wrapped up the offer and financing part.

00:07:49 - Brandon Hancock
That's awesome, Maxim. I have a few nerd questions for you. <Q>So when it comes to, I know you said 300 conversations a day. Out of curiosity, what's that racking up bill-wise?</Q>

00:08:05 - Maksym Liamin
<A>It's not $300, it's like $2,800, so $3,000, close to $3,000, and we spent, I believe, around $10 per day.</A>

00:08:17 - Brandon Hancock
The amount of efficiency you're unlocking for $10 is stupid.

00:08:22 - Maksym Liamin
Yeah, we switched from Anthropic [tool:Anthropic Claude], and we reduced our bills by $4, yeah, so we were paying around $40 per day. Now we switched, even though we have GPT credits, but because we somehow couldn't battle the content filtering, somehow in Azure [tool:Azure OpenAI] is just too harsh, and we tried to disable it and talk to the tech support there, but it was not working, so we just switched to normal OpenAI [tool:OpenAI] with just our own API key. We have, like, two accounts of tier 5, so we are using them, and, like, we have good load, in a sense, it gives, like, almost 10 million tokens per minute, which is enough for us.

00:09:05 - Brandon Hancock
<Q>Out of curiosity, are y'all going 4.1? Are y'all going o3?</Q>

00:09:10 - Maksym Liamin
<A>No, 4.1. Speed is really important. We just cannot use o3.</A>

00:09:16 - Brandon Hancock
▶ Yeah, I mean, GPT-4.1 [tool:GPT-4.1] has been an absolute game changer on how well it follows instructions, plus speed. And they cut your pricing down 75%.

00:10:00 - Brandon Hancock
Meet Maksym for here's a project he's working on. Basically, he's working with a car dealership, and specifically a tool that's aimed to help their sales agents to answer questions in WhatsApp [tool:WhatsApp Business API]. So basically, when people ask questions, it provides the relevant context at the right time to help them answer it, because there's thousands of models, thousands of different variables, and this RAG tool always provides the right information.

00:10:28 - Maksym Liamin
So there are a lot of different tools that are in here, but one of the main ones, and they're mostly used, is just photos, so I can tell something like, hey, can you send me pictures of that? It's like a new model in blue, yeah?

[Demo proceeds showing photo retrieval, competitor comparison (Jetta vs. Versa), PDF catalog delivery, and financing/credit plan queries in Spanish]

00:14:06 - Juan Torres
<Q>Which vector database are you using? And then to connect to the WhatsApp application, are you using Make or n8n? And then how did you find a client and propose the idea?</Q>

00:14:34 - Maksym Liamin
<A>Okay, so the first one is we use Supabase [tool:Supabase] for everything, for both SQL and Vector. We use Voyage [tool:Voyage AI] for embeddings. That's something that is important. I really like this model. Second, we don't use any. We just use Meta servers and WhatsApp for business, in a sense. So we connect straight from the source and we deploy it on our Angular server and in Cloudflare [tool:Cloudflare]. And the third, through a personal connection.</A>

00:15:30 - AbdulShakur Abdullah
<Q>Yeah, I just wanted to know those photos and everything, were those taken, like you went directly to the showroom and added them? So you're kind of building a moat around your offering.</Q>

00:15:48 - Maksym Liamin
<A>Some of the pictures come from Nissan or Andanak, which is a group of dealerships directly. But also, some of them come from us also, yes.</A>

00:16:28 - Jake Maymar
<Q>So, yeah, this is awesome work, Maxim. So the question is the evals. How are you making sure there's no hallucinations in this process?</Q>

00:16:48 - Maksym Liamin
<A>If you want an honest answer, like we ship so fast that we just test it in production. Like, we don't even have neither, we don't have evals, we don't have even a test, like test deployment.</A>

00:19:31 - Brandon Hancock
▶ Yeah, I would love at some point to talk about our Lord and Savior, a staging environment, so you don't always have to go to production. Feature flags — you could just say like for users A, B and C, they have access to this new functionality.

---

<!--SEGMENT
topic: Database Tooling — Drizzle, Neon, Supabase Tradeoffs
speakers: Brandon Hancock, Paul Miller, Jake Maymar, Tom Welsh, Ty Wells
keywords: Drizzle ORM, Neon, Supabase, Postgres, row-level security, migrations, Lovable, Next.js, TypeScript, schema management, CRUD
summary: Paul Miller asks about low-code approaches to managing a reliable data layer when building with Lovable. Brandon recommends Neon (hosted Postgres) plus Drizzle ORM as the simplest path, explaining what an ORM does and how Drizzle handles schema migrations. Tom Welsh adds that Drizzle makes switching database dialects seamless. Ty Wells flags a known Supabase + Lovable infinite recursion issue with RLS policies.
-->

00:20:35 - Paul Miller
Thanks, Brandon. Yeah, so, okay. I've separated off the Supabase [tool:Supabase] to make sure that I get the whole structure in terms of the calculation really right, and then create a new project based on that data architecture and calculation to be better.

00:24:00 - Paul Miller
<Q>Is there anything, Brandon and everyone else, what thoughts would you suggest for a low code approach to making sure you've got the data layer right, and then tie into something like Lovable [tool:Lovable] for the UI, UX, for rapid development?</Q>

00:24:22 - Brandon Hancock
<A>So Supabase has a lot of extra complexity for like row level security. So if you want to just like very quick, the easiest way to get things set up would be, I mean, Lovable. From there, you would end up using Neon [tool:Neon] for your database, just a super simple Postgres database. You would use Drizzle [tool:Drizzle ORM] to create your schema and push those to your database, and then you would use Clerk [tool:Clerk]. Those four right there would get everything up and running for you.</A>

00:25:13 - Jake Maymar
<Q>I want to understand Drizzle, like if I have Neon and I'm doing Drizzle, how critical is Drizzle? Like what exactly does Drizzle do that Neon can't do?</Q>

00:25:52 - Brandon Hancock
<A>Awesome question. So Next.js [tool:Next.js], basically what's going on is it's your front end application and your back end application. So what happens is how the heck does your back end code talk to your database? Well, it's not going to write raw SQL queries. So that's what it's called a ORM, Object Relational Mapper. So what it does is it takes in whatever you want it to do, like whatever schema you have set up. It knows what you're wanting on your back end. It makes the request to the database. Once it gets that raw response, it converts it to the proper format that you can use in your code.</A>

00:27:20 - Brandon Hancock
▶ Drizzle would create that migration file. And it's all through code, so you literally would just make the change to your schema in code, then you would say push migration, and then it would start applying it for you. So you have a migration history, so you're not having to manually just go in there and change stuff.

00:29:30 - Tom Welsh
I would say that, I mean, the other thing I find good with Drizzle was that I was working with one particular database, I think it was Postgres, and I moved to a different one and literally just changed the dialect in the Drizzle config and just switched it seamlessly across. ▶ So migrating between different databases is really easy using the ORM.

00:31:13 - Paul Miller
<Q>So Neon, what does Neon do? What function does it do?</Q>

00:31:25 - Brandon Hancock
<A>▶ It is the fastest way to spin up a database, and they have the best free tier — you can have 10 projects, half a gigabyte, and then an insane amount of compute hours. It used to be PlanetScale, then they went off the free tier, so now Neon is the best for experimenting with databases.</A>

00:33:34 - Brandon Hancock
▶ However, if you're going to start getting to building an AI application to where you need to have access to vector stores and everything else like Maxim's doing, yes, 100% Supabase. Supabase is the move when you hit that next level of complexity.

00:33:42 - Ty Wells
The only thing I would add with Supabase — I'm using it with Lovable, and oftentimes it puts itself in an infinite recursion loop by using the security definer, supposedly to protect, but it actually puts itself in a loop because it's got the security definer and then it's got RLS policies. So they can flip with each other and they just can't seem to get that part right.

---

<!--SEGMENT
topic: Pharma AI Agent and News-to-Infographic Pipeline
speakers: Brandon Hancock, AbdulShakur Abdullah
keywords: customer discovery, pharma, clinical trials, RAG, Replit, ADK, OpenAI image generation, infographics, bio news APIs, sequential agents, loop agents
summary: AbdulShakur Abdullah reports on customer discovery for a pharma business development AI tool, finding that target users prefer expensive curated databases over public data. He pivots toward automating bio news summarization into infographics as a differentiated offering. Brandon points him to the ADK thumbnail generator project as architectural inspiration for sequential and loop agent patterns.
-->

00:34:35 - AbdulShakur Abdullah
All right. Just a little context. My overall goal was to build a kind of a system of agents that would help people in pharma fields, business development, pull in a bunch of information, organize it, and then make decisions.

00:35:11 - AbdulShakur Abdullah
So I started doing this past week some customer discovery, talking to users. And the business development part for the application, they didn't seem very enthusiastic about it. Basically, they want to pay like $100,000 for those highly curated databases just and not rely on the public database.

00:36:14 - AbdulShakur Abdullah
So then I started looking at the other aspects of the program, which was the pull-in business news. So I spun up a Replit [tool:Replit] instance and started pulling in a whole bunch of APIs from different bio news sources. And my idea was to quickly summarize all of them and then create like a daily summary of, hey, here's all the interesting news going on and send that out to all the users. I found that Replit, it kind of ate through all of my credits quite quickly with testing.

00:37:10 - Brandon Hancock
▶ Dude, go you for doing customer discovery. It is the hardest part because it's 100% out of comfort zone. But it is the most important thing because you're building it for customers. You found out feedback early on what data types they want to use.

00:38:31 - AbdulShakur Abdullah
I basically prompted telling me, hey, here are all the competitors. Here's what I want to offer. What am I offering that's unique? And it was like, nothing. So then I was like, okay, well, what can we offer that would be unique that they would might like? And the idea was to then pull in some key news articles to automatically convert those into short summaries that could then be converted into infographics, as no one's kind of really doing that angle.

00:39:39 - Brandon Hancock
No, I think that's super, super cool. I want to show you this really quickly. So yeah, you can 100% start to steal inspiration from there. The part you would really like to take inspiration from is the Thumbnail Analyzer Agent and the Generate Image Agent. The reason why is it starts to show off how you can use different types of agents together, specifically how you can do a sequential agent — go scrape the internet — and a loop agent, which is going to consistently try over and over and over again. ▶ So you can start to use these different types of workflows within a chat, and that's just like mind blowing that you can now just chat and then trigger a chain reaction of actions to happen.

---

<!--SEGMENT
topic: Geospatial Art Project and AI Analysis Potential
speakers: Om Kundalini, Brandon Hancock, Jake Maymar, AbdulShakur Abdullah, Michal Simko
keywords: Google My Maps, geospatial, mythology, Hindu mythology, zodiac, computer vision, A2A protocol, knowledge graphs, YouTube Shorts, text-to-video, AI agents
summary: Om Kundalini, an artist with no development background, presents an eight-year geospatial storybook project mapping mythological narratives (Hindu, Biblical, Zodiac) onto satellite imagery. He asks whether A2A agent protocols could support a knowledge graph and statistical analysis platform for his work. The group suggests YouTube Shorts storytelling, computer vision for shape matching, and connecting with community member Richard Collier for AI video production.
-->

00:42:10 - Brandon Hancock
Om, out of curiosity, welcome to the call, man.

00:42:19 - Om Kundalini
I'm an artist, and I'm not a developer at all, at none. Zero development skills do I have.

00:43:25 - Om Kundalini
So this map is a geospatial storybook of human heritage. It's something I've been working on for eight years. It didn't start out as this map. It started out as I like looking at palaces and castles and chateaus, and I like looking at their formal gardens and satellite imagery.

[Om describes finding mythological figures (Saraswati, Brahma, Ganesha, Vishnu avatars, Biblical Adam and Eve, Zodiac constellations) mapped onto terrain features in satellite imagery, all in correct logical/geographic order]

00:49:00 - Om Kundalini
And in the ocean, what I found was the entire Zodiac. There's Aquarius pouring water, there's Pisces, there's the Bull of Taurus, the Ram, then they go in the same order as they are in the night sky. When you take Google Earth [tool:Google Earth] and you tilt it 23.5 degrees, like our axial tilt, my Zodiac mirrors the constellations in the night sky perfectly.

00:51:28 - Om Kundalini
The other day, A2A protocol [tool:A2A protocol] was released, and I went and bought A2Aworld.ai, and I know it's just a domain name, but I want to make the A2A world, I want to make it A2A agents that wants a geo AI, wants a knowledge base, you know, that has knowledge of mythology.

00:53:31 - Om Kundalini
<Q>Do y'all think this is something that's realistic with A2A? Is it capable of doing this type of database retrieval, knowledge graphs, and stuff like that?</Q>

00:53:43 - Brandon Hancock
<A>So if you were to take a step back and analyze what you just did, it is like, you understood a lot of like core religious texts and stories. From there, there was a few like symbolic images of like scenes that happened. It was then looking on a map to see like, okay, cool. There's a thousand religious stories in different core scenes throughout these different texts. Now, how do I, looking at a specific area of a map, like which image best matches this scene? I don't know if it would be able to just look at a map of a random area and be like, oh yeah, that is this image. I don't think it's there yet.</A>

00:55:56 - Brandon Hancock
▶ Dude, I thought that was cool. I think it would be awesome if you just made YouTube Shorts. Like, if you made YouTube Shorts where you were just describing that story you just said, that would be the trippiest thing. If you need help finding video editors or thumbnail editors, talk to me.

00:56:34 - Jake Maymar
I always think of the same thing. It's the story. And if you can basically craft the story, do a YouTube crafting the story and sort of showing. And what I would almost do is kind of change the contrast so it's a little bit easier to see the silhouette. And then on the computer vision side, you're basically making vectors and you could take and analyze those vectors and look for that kind of shape on Earth.

00:59:43 - Brandon Hancock
▶ It's Richard Collier. If you look him up, you'll see him in the community. Just reach out to him and just say, I'd love to pick your brain and he could help with AI video production.

---

<!--SEGMENT
topic: Server Migration, Traveling Salesman Problem, ADK Evals
speakers: Tom Welsh, Brandon Hancock, Jake Maymar
keywords: Vercel, dedicated server, Lambda functions, ADK evals, LiteLLM, OpenRouter, traveling salesman problem, 3D robotics, function calling, Anthropic Claude
summary: Tom Welsh discusses migrating from a five-year-old dedicated server to cloud services (Vercel). Jake Maymar asks about 3D/4D extensions of the traveling salesman problem for robotics applications. Brandon demonstrates ADK's built-in eval system as unit tests for agents, and introduces LiteLLM and OpenRouter as universal model access layers.
-->

01:00:31 - Tom Welsh
Hey. Well, AI-wise, not very much. My traveling salesman problem was just stagnated due to me actually running around and doing the job. But yeah, I've been tinkering with it a little. This weekend I've had a monolithic server for about five years, paying about £200, say $300 a month, the past five years for the server. I'm now migrating most of that onto cloud services, Vercel [tool:Vercel] for websites.

01:03:47 - Brandon Hancock
▶ Guys, like, I play with every agent framework. I love the fact that I can easily chat. I can deploy. So I get all the coolness of a chatbot, I get all the coolness of a Crew AI workflow in one framework — ADK. That's why I'm so passionate about it right now.

01:05:11 - Jake Maymar
Yeah, so two questions. So the first question is for ADK. <Q>Evals, is that kind of built in so you can kind of sort of see how your eval?</Q>

01:05:43 - Jake Maymar
<Q>And then the next question I have — traveling salesman, but in 3D. Is that a pretty straightforward thing to do?</Q>

01:06:06 - Jake Maymar
And then the next thing is after 3D, then 3D in motion, so then 4D, and that's specifically for robotics.

01:07:07 - Tom Welsh
I was going to say one thing about the ADK thing. On the LLM model where you've got 4.1, I take it you just might change like the Anthropic Claude 3.5 or 3.7. When I changed that, I got a whole bunch of errors.

01:07:40 - Brandon Hancock
<A>Some models don't support things as well as other models. It probably is function calling.</A>

01:07:52 - Brandon Hancock
So LiteLLM [tool:LiteLLM] is the tool that handles all the complexities for you. And then OpenRouter [tool:OpenRouter] is a single place to where you can buy tokens to then get access to any model. ▶ So between these two tools, you can access every model everywhere. In the past, you would have to use like LangChain agents, an Anthropic agent — so complex. And now you just have these two and it's set up to go.

01:08:48 - Brandon Hancock
So basically what you can do is you can set up evals to do all sorts of things where you pass in an input and say what you're expecting for your results. So for example, like I'm working on this thumbnail cloner or emulator, so I can give in someone else's channel, and I would expect it to first scrape, then analyze, then generate a style guide, and then create the image. ▶ Think unit tests for agents — that's the best way to think about it.

---

<!--SEGMENT
topic: On-Prem AI Servers, HIPAA Compliance, and Claude Max
speakers: Jake Maymar, Brandon Hancock, Tom Welsh, Maksym Liamin, Andrew Nanton, Michal Simko
keywords: HIPAA, on-premises LLM, Docker, Stable Diffusion, AWS, Azure, N8N, Supabase HIPAA, Claude Max, Windsurf, Kline, Cursor, memory bank, Drizzle
summary: Jake Maymar shares the competitive advantage of running LLMs on-prem with Docker for cost-effective POCs, then raises HIPAA compliance questions for PII and medical decision-making applications. Maksym and Andrew advise on HIPAA-compliant deployments in AWS/Azure. Michal Simko discusses switching to Kline with a memory bank setup, and the group debates Claude Max ($100/month) versus Cursor for large codebases.
-->

01:10:21 - Jake Maymar
Not much to discuss, but I will say this. Running on a lot of, like, on-prem servers. And to me, that's definitely a competitive advantage because you can do so much and you don't have to pay for it. ▶ So I think that's a really interesting thing and kind of an interesting business model — introducing POCs, slightly MVPs, that are easier to spin up and actually sort of vet where the kind of costs it would cost if you were basically hosting those would be insane.

01:11:54 - Tom Welsh
Jake, are you running the LLM hardware locally as well?

01:11:59 - Jake Maymar
Yes. And Docker [tool:Docker]. Not Kubernetes at this point. I kind of like Docker Composes because I keep it very, very simple, but we're running local models. But what's kind of cool is we can actually do like Stable Diffusion [tool:Stable Diffusion], right? We can run all these things completely locally.

01:12:42 - Tom Welsh
I read quite an interesting article this week on Medium. It was literally about having on-prem hardware as opposed to calling API endpoints. And it was saying that the price you're paying for machines to run locally, you could probably get a year's worth of API calls.

01:13:22 - Jake Maymar
<Q>HIPAA — is anyone doing HIPAA where it's actually — I'm thinking Andrew might have information on this — HIPAA where I'm doing PII, where I'm not making a medical decision, and where I am making a medical decision?</Q>

01:13:56 - Andrew Nanton
<A>HIPAA is really at its heart, insurance legislation, and it has to do with being allowed to give your health information to insurance companies so that they can decide whether or not to cover it. Once a person signs a HIPAA release for their information, they can put it on a billboard if they want to. So you need to define what your relationship is with that material. If you're getting it in the course of providing clinical services, then, yeah, you need to do the HIPAA thing.</A>

01:15:37 - Maksym Liamin
<A>If you need to set up a deployment that is completely HIPAA compliant, I can help you. I can do it in providers like AWS [tool:AWS] or Azure [tool:Azure]. I would not trust myself to go somewhere else like DigitalOcean or GCP. It was a huge learning for me already to get it working in Azure.</A>

01:17:00 - Maksym Liamin
Yeah, it's like Supabase also charges you, I think, $600 or $700 per month just to maintain your HIPAA compliance. That's pretty much the only reason why me and Andrew went for Azure on Postgres to keep everything inside the Azure environment.

01:17:27 - Michal Simko
After the last time, I had to basically rebuild it again. So I basically decided to give a shot to Kline [tool:Kline]. And that is super interesting. I set up the whole memory bank. The new Kline has this memory bank structure — you create this memory bank that you can give it, like, active context, phase out, like, my implementation, you can have progress, debrief and whatnot.

01:19:15 - Michal Simko
I did the first mistake that I bought the credits through Kline, and like 20 bucks went very quickly on like Claude and whatnot. But the Claude is a beast. I have to say like the 3.7 is just, yeah, I'm even considering whether I should just go for like one month or two months with that Claude code, whatever it's called, like that agent, they sell for like $90 a month.

01:22:22 - Jake Maymar
So I got access to this. It's Claude Max [tool:Claude Max]. It's $100 a month, but you can get like a little coupon or whatever. I've been fighting with Claude on some really, really hard ESLint issues with my TypeScript and they were all interdependent. And so I would fix it here and it would break over here. It just fixed the code. Whereas I've been fighting with it. ▶ You didn't have to tell Claude that. It just doesn't. And I'm pretty impressed so far.

01:24:52 - Maksym Liamin
<Q>Did OpenAI actually buy Windsurf [tool:Windsurf]?</Q>

01:25:02 - Michal Simko
<A>It was in the cooking for a while, and then it came.</A>

01:25:15 - Jake Maymar
I used to, you know, I'd get on and go, Windsurf, Windsurf, Windsurf, loved it. I haven't been using it, honestly, recently. Kline and Cursor [tool:Cursor] and the other tools were just more stable.

01:27:05 - Tom Welsh
I was jumping to Windsurf with my code base when I was getting to that deadly embrace in Cursor, which went round and round in circles, like Jake or Andrew were saying earlier, where you were getting linting errors. ▶ I found that Windsurf had fixed the linting errors that had taken all the code back to Cursor and got on with it again.

---

<!--SEGMENT
topic: Cursor MCP Servers, Supabase Schema, and High School Seating App Demo
speakers: Ty Wells, Brandon Hancock, Tom Welsh, Andrew Nanton
keywords: Cursor, MCP servers, Supabase, Firecrawl MCP, project rules, cursorignore, Resend, Lovable, Next.js, Whisperflow, seating management, graduation, row-level security
summary: Ty Wells demos a high school graduation seating reservation system built after migrating from Lovable 2.0 to Cursor, using Supabase for storage and Resend for bulk email. He raises issues with MCP server disconnections in Cursor and the challenge of giving Cursor context about a large Supabase schema. The group discusses MCP maturity, .cursorignore files, project rules, and Whisperflow for voice-to-prompt input.
-->

01:31:45 - Ty Wells
Brandon, in particular, I see you're a big Cursor guy. I'm switching from Cursor to Cursor from Lovable 2.0. I love Lovable 1.0, but 2.0 is just... well, if you're working with an older application, it's problematic. But I'm looking for some tips and tricks on Cursor because my MCP servers keep disconnecting.

01:33:00 - Ty Wells
Yeah, my Supabase keeps dying. It keeps disconnecting. So I'm just telling it to do something and it didn't have access to the server.

01:33:23 - Brandon Hancock
<A>So, a lot of the time for these models, just going back to context window limits, using agents blows up the context window and it very quickly forgets what you told it to do earlier. So, if you want it to consistently refer back to using these, yeah, you need to mention it. MCP, at the end of the day, it's like tool calls. So, like it's supposed to show the available tools. It might not always know why or that it always needs to call these tools. So, yeah, I think a very quick one sentence, two sentence instructions there would make sure it doesn't forget.</A>

01:35:09 - Brandon Hancock
<Q>I know you said, I know you're talking about like your Postgres database that you have in Supabase. What was going wrong? Why did you add it?</Q>

01:35:31 - Ty Wells
<A>Well, like I said, I started this project in Lovable, but that was failing. There are issues in 2.0, Lovable 2.0 was causing issues. So I had to get out of there and I had to deliver this project. It didn't have any context as to the database schema and the schema is massive.</A>

01:36:14 - Brandon Hancock
▶ This is the hard part about working with Supabase — your schema is not in a file that's accessible to your local code. That's why I'm a huge fan for simpler projects where you don't need to use like a vector store to stay away from Supabase. In Supabase, all of your schemas and everything is kind of set up on Supabase. So it's not really managed in code where Cursor can easily look at your database schema on your computer because it's saved as a schema.ts file.

01:37:32 - Tom Welsh
So for each project that I set up, I write dedicated rules for that project, like what I'm using, what my command lines are going to be. And that's like just an overview of what the whole project is. And I dump that in the project rules for each individual project. ▶ Also, there's .cursorignore and .cursor rules files. .cursorignore is a good one to put in your environment variables and stuff so they don't get sucked around with your code.

01:38:28 - Andrew Nanton
<Q>I was just asking if there are specific MCPs that people have found especially useful with Cursor or any other editor.</Q>

01:38:51 - Ty Wells
<A>I've used the Firecrawl MCP [tool:Firecrawl MCP] server. That's pretty good. But I don't actually like MCP services just yet. I think the tech is a little bit immature. Black box, security issues — I'm a cybersecurity guy.</A>

01:41:42 - Ty Wells
So, this is actually for my kids' high school — this is a high school seating system for reservations that come in. The parents choose how many seats they need, because apparently high school seating is very political. The reservations go out via email, I use Resend [tool:Resend] to send it out, then I had to build an email template campaign to send out those emails. And then I built them a visual chart so they can see better where people are seated.

01:44:56 - Brandon Hancock
You've built Ticketmaster's, but for a high school.

01:47:58 - Ty Wells
I'll add one tool — Whisperflow [tool:Whisperflow]. Keyboard shortcut, hold down, speak. That's my prompting. ▶ It's just, it's, I actually ran out of credits. Had to bump my plan up today. But yeah, Whisperflow, it's so sweet.

01:49:52 - Jake Maymar
MacWhisper [tool:MacWhisper]. Andrew got it. That's it. And I think it has a sale, like there's a sale on it. And it's also compliant.

---

<!--SEGMENT
topic: AI in Legal Proceedings and Creative AI Business Ideas
speakers: Andrew Nanton, Brandon Hancock, AbdulShakur Abdullah
keywords: AI-generated video, court evidence, Arizona, victim impact statement, HIPAA, ethics, post-mortem AI, OpenAI voice, Santa AI app, Peter Levels, legal AI
summary: Andrew Nanton shares a landmark Arizona court case where an AI-generated video of a deceased shooting victim was permitted as a victim impact statement during sentencing. The group discusses the ethical and legal implications, the probative vs. prejudicial value debate, and the likelihood of appeal. Brandon pivots to brainstorming a seasonal AI Santa app as a potential viral consumer product, referencing indie developer Peter Levels as inspiration.
-->

01:50:19 - Andrew Nanton
Yeah, not a lot of big updates again this week. Hopefully working on a research paper on the thing that we did with the feedback for therapists who are doing addiction therapy.

01:51:01 - Andrew Nanton
I'll drop it in the chat, but probably the big buzz here in the last week or so around legal work in AI was the case in Arizona where a family made an AI-generated video of a man who was a victim in a shooting. And so the AI-generated video gave the witness statement in court. And so apparently in Arizona, that passes muster.

01:51:41 - Brandon Hancock
<Q>Can you say that again? Wait, I just want to make sure I understood that.</Q>

01:51:49 - Andrew Nanton
<A>So a man was, there was a road rage incident where a guy shot another guy. During the sentencing phase, the family, using some video, created an AI video of the victim who is dead, giving the impact statement about the effect that this had on his family. And you would expect that to be pretty emotionally compelling. What courts have to decide is, is the probative value — the information that it's adding — more than the sort of emotional heft that is so biasing.</A>

01:53:12 - Andrew Nanton
I'll guarantee you you'll see that on appeal. I mean, the judge permitted it, but yeah, I mean, I'm sure it will be in appeals for years.

01:53:24 - Brandon Hancock
Yeah, it's the amount of, like, ethical questions, like you always hear, like, AI and ethics, and I would have never thought of this use case of it.

01:54:10 - Brandon Hancock
I want to do, like, a Santa thing for, like, you know how, like, they have Elf on the Shelf and all this stuff where, like, oh, if you're good or bad, I definitely want to do an AI Santa at some point. I mean, you'll see Peter Levels [tool:Peter Levels], he'll do stuff, like, something like that, and he's like, oh, I made this tiny app, and I accidentally printed $1 million last month. ▶ That is my quick $1 million bet this Christmas.

---

<!--SEGMENT
topic: PDF Data Extraction Pipeline for Energy Savings Reports
speakers: Premkumar Subbiah Thangarajan, Brandon Hancock, AbdulShakur Abdullah
keywords: PDF extraction, ETL, Azure AI Document Intelligence, OpenAI, Power BI, data pipeline, unstructured data, schema normalization, Crawl4AI, Firecrawl, energy consumption, 2000 PDFs
summary: Premkumar Subbiah Thangarajan presents a client problem involving 2,000 PDFs containing energy savings data in non-standardized tabular formats across 10+ years. He needs to extract, normalize, and load the data into a database for Power BI dashboards. Brandon frames it as an ETL/data science problem requiring a wide-column approach first, then iterative reduction. AbdulShakur suggests grouping PDFs by similar header patterns before attempting unification.
-->

02:09:07 - Premkumar Subbiah Thangarajan
Thanks a lot, Brandon. And, you know, again, I'm relatively new to AI. So basically, you know, what I'm currently working on is like, we have a client where historically, they have a lot of, you know, PDFs, like, you know, thousands of PDFs. And they have data, basically energy consumption data across, you know, multiple years, like kind of in different projects, basically.

02:10:54 - Premkumar Subbiah Thangarajan
And again, there are multiple contractors who are working on this, so they don't have a standard template. So basically what the goal is, again, they have so much data where there is a lot of value in this, where they can kind of see, what is the cost savings across, you know, like the last 10 years.

02:11:33 - Premkumar Subbiah Thangarajan
So, and the first iteration we did was basically just kind of doing prompts, and again, like the other problem is like there's no standardization, so somebody might call it as electric energy, somebody might call it electric energy savings, which are kind of the same. So we kind of started doing prompt, you know, this thing to kind of, you know, read the data and then, you know, kind of create a JSON out of it and then finally, you know, dump it to a, you know, database.

02:12:37 - Brandon Hancock
<Q>So you have multiple PDFs that you have to deal with. Each PDF has different charts. Is there any additional information that you need in those PDFs or is it strictly just these, like, five types of charts?</Q>

02:13:17 - Brandon Hancock
<A>So step one, you have data in PDFs. Let's just imagine we were able to handle all data perfectly. What do you want to do with that data? What's the, like, what are we trying to do?</A>

02:13:33 - Premkumar Subbiah Thangarajan
<A>So I want to ideally get, like, again, the data into a database so that we can do metrics. I want to aggregate data by the different companies and so on. In a nutshell, I want to kind of get this data into a database where we are going to use Power BI [tool:Power BI] on all those things to kind of visualize.</A>

02:15:25 - Brandon Hancock
<A>So you're going more into, basically like, ETL. So basically like you're almost having to set up like a data pipeline in order to go from raw unstructured data, transform it into some sort of structured setup to then put into a database. ▶ What I would do is create almost infinite columns — meaning PDF1 gives these columns, PDF2 gives these columns — and then you end up with a really wide data that you save to a database. Then from there, when it comes to answering questions about it, you use LLMs to reduce that data set. I don't think you're ever going to get this perfectly into a table that has 10 rows that works for all these PDFs.</A>

02:21:30 - AbdulShakur Abdullah
▶ I probably would do a grouping first, where I'd first group — okay, all of these have similar headers, so this will be database one, all of these similar headers, this will be database two — that way maybe you end up with like ten different databases, but checking quickly when the columns already line up, and you don't have a hundred columns. Then it's a matter of matching database one through five, matching their values, that you could then do a union on them.

02:22:00 - AbdulShakur Abdullah
<Q>I did have a question — are these selectable? Because I know some PDFs are full image-based, and some are text-selectable-based. That kind of changes what tools you can use, too.</Q>

02:22:19 - Premkumar Subbiah Thangarajan
<A>These are, like, you know, text-based. So I've been using Azure AI Document Intelligence [tool:Azure AI Document Intelligence] to kind of read the text of it, and, you know, then try to apply, you know, prompt, you know, section on them.</A>

---

<!--SEGMENT
topic: Google ADK Architecture for Nonprofit Executive Assistant
speakers: The Dharma House, Brandon Hancock
keywords: Google ADK, LangChain, RAG, Firebase, Vertex AI, multi-agent system, artifacts, callbacks, sequential agents, loop agents, hexagonal architecture, nonprofit, onboarding agent, state management
summary: Aaron (The Dharma House) describes building a multi-agent executive assistant for nonprofits, covering knowledge base management, RAG retrieval, workflow prioritization, and stakeholder reporting. He shares inspiration from an InfoBip developer conference about small agents becoming major competitors (referencing Cursor/Windsurf). Brandon explains ADK artifacts vs. vector stores, the role of callbacks for pre-processing RAG queries, and the "agents as tools" pattern as an alternative to ReAct-style reasoning.
-->

02:27:28 - The Dharma House
I actually spent the day at the conference. I wasn't going to talk about that right away, but I'm at this conference called put on by InfoBip [tool:InfoBip]. They compete with who's doing messaging — Twilio [tool:Twilio]. They're offshore Twilio competitor.

02:28:06 - The Dharma House
The coolest thing I pulled away today, inspirational to you all — a guy said at the end of his presentation, sometimes you think that these big companies are going to come and just dominate the market. And this conversation was around the fact that when we look at what just happened with Cursor, with Windsurf, this was just an agent, and this agent became worth this money. ▶ When Copilot came out, people thought that Copilot would probably be the one and that there wouldn't be another strong competitor, but here we are watching some monumental moves in the industry, and the inspiration is just to keep on building because you don't know that small idea that you have of how it may literally become the next big competitor.

02:29:32 - The Dharma House
Google ADK [tool:Google ADK], you recommended that I try it. Thank you. I haven't had a lot of time to dig into it. Some of you guys know I just moved. I'm building an MAS, an executive assistant. The hardest part for me has been to dial into a specific use case. And essentially what I wanted for myself was a knowledge base of my businesses, a RAG retrieval, some data uploads, document uploader ingestion, workflow management, some time and task prioritization, and reporting.

02:30:34 - The Dharma House
I kind of feel like I've been backing into one really strongly in having this opportunity to work with a nonprofit. The client's telling me that the problem is really that these people really aren't well organized. And this is like this big opportunity because there's so many nonprofits that need to prove right now that they're worth their money with all the funding cuts.

02:31:48 - The Dharma House
If you don't know, I started building in LangChain [tool:LangChain]. Some deprecations and dependency hells kind of like turned me off from it a bit. A couple weeks ago, Brandon suggested, hey, I think Google ADK is the tool for you. What I like about it — cloud-based quick launch MVP. I like how agnostic it is. One of the really big awesome tools is it's got a native multimodal capacity kind of built right into it. I like how much more room I have to prompt.

02:33:18 - The Dharma House
<Q>My question for you, Sensei, is architecture. I built LangChain, and I built this monolith, and now, like, I want to take this system and use Google in its native capacity to its highest potential. Do I take this beautiful hexagonal design pattern and then try to fit that into ADK or do I disregard that work and now just kind of — I have like two basic throw at the wall iterations.</Q>

02:35:00 - Brandon Hancock
<A>The important things — the chat functionality, and also the workflow functionality. Okay, so diving deeper into what you're doing — artifacts. Report equals artifact. So inside of ADK, artifacts are how you feed PDFs and other documents into your agents. Same with images or whatever else you want to use. Artifacts are more like working documents. Like, I'm in a session working with this artifact. When you want more like long-term knowledge base, that's when you're going to use like the vector store setup that they have.</A>

02:37:00 - Brandon Hancock
<A>In your setup, from my understanding, you were doing a lot of like, oh, I want to get information about this user's queries, so you're going to have to master their callbacks, which is like, okay, this user has access to all this piece of information, therefore, I need to, before the model gets triggered, I'm going to need to perform that RAG query, I'm going to need to feed it, and add in all this extra additional information into the model to help the model generate a proper response.</A>

02:38:50 - The Dharma House
<Q>Your core agent, do you make — is the core agent just core, or can I make a core agent as dynamic as that beautiful machine I already built? Or do I need to break that into logic for each of these agents?</Q>

02:39:04 - Brandon Hancock
<A>So basically the core agent is strictly a delegator. For most ADK use cases, all it is, is a delegator. There's a term called ReAct, meaning reason and then take action. That is not what you get in ADK. ADK is strictly a delegator to some other agent to go do the work. ▶ You can do a thing called agents as tools, where you have your root agent is the RAG agent, and then it does tool calls to other agents. So you almost get that ReAct feel, but that is another option you could do too.</A>

02:41:00 - Brandon Hancock
Hey, I got this definitely went over. Y'all are awesome. Please be on the lookout for another ADK tutorial this week on using it with the image setup and then also one for Vertex AI [tool:Vertex AI]. Aaron, you're going to like the Vertex one when that comes out. Thanks, guys. Y'all are awesome. I'll post the recording right after this. Happy Cinco de Mayo, day late, and drink a margarita for me.

---

=== UNRESOLVED SPEAKERS ===
- `Om Kundalini` — name passed through unchanged; not found in SPEAKER_ALIASES context (note: the SPEAKER_ALIASES block was not populated in this request)
- `alexrojas` — raw name used as-is; no canonical form available
- `The Dharma House` — raw name used as-is; no canonical form available
- `Premkumar Subbiah Thangarajan` — raw name used as-is; no canonical form available
- `Gaurav Shukla` — raw name used as-is; no canonical form available