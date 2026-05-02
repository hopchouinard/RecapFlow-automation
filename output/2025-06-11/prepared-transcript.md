=== SESSION ===
date: Not explicitly stated (Tuesday, estimated mid-2025 based on context)
duration_estimate: ~2 hours
main_themes: Google ADK development and deployment, A2A protocol, RAG architecture and chunking strategies, LLM-based data extraction, prompt management and evals, HIPAA-compliant AI tooling, Lovable/Cursor/Next.js development workflow, Crew AI vs ADK comparison, CRM recommendations

---

<!--SEGMENT
topic: Session Opening and Host Updates
speakers: Brandon Hancock, Mitch, Paul Miller, Ty Wells
keywords: ADK, A2A protocol, agent-to-agent, LangGraph, Crew AI, FastAPI, ADK deployment, Google ADK Masterclass, ShipKit, TypeScript
summary: Brandon opens the weekly developer call, explains the round-robin format, and shares updates on a newly completed A2A (agent-to-agent) tutorial video covering ADK, LangGraph, and Crew AI agents communicating via the A2A protocol. He also previews an upcoming video on deploying ADK agents via a FastAPI-style endpoint. Pre-call small talk touches on transitioning from Airtable to a proper software stack.
-->

00:01:50 - Mitch
How's it going, Paul?

00:01:55 - Paul Miller
Good, Mitch. How are you?

00:02:05 - Mitch
Getting some good work done, managing clients, and trying to keep this project moving forward. Kind of thrifted it out, and now it's time to actually build a realistic software stack.

00:02:24 - Mitch
Yeah, Airtable [tool:Airtable] can only do so much, and I'm like, yeah. It's unfortunate, because you're like, tech debt, but also at the same time, it's like, exciting. It's like, now actually have it be what you want it to be.

00:02:39 - Paul Miller
Well, I've enjoyed working with the FastAPI [tool:FastAPI] stuff. It's been good. Having a nice separate segregated back-end part that I can control, and without having to take on the complexity of dealing with JavaScript-based or TypeScript-based backend stuff, which I just couldn't do. It's good for the frontend and maybe get Lovable [tool:Lovable] to generate the code or Cursor [tool:Cursor], but I really want to control the backend because if you don't have that right, then you're kind of stuffed.

00:03:17 - Mitch
So basically you're backend pure Python based and you use FastAPI, you got to manage that.

00:03:25 - Mitch
I haven't watched Brandon's course. I've been going through it. And yeah, it's kind of like the thing that scares me is the TypeScript end of it all. But with how Lovable and Supabase [tool:Supabase] connect together, I'd say it's pretty good for someone who semi-knows stuff.

00:04:00 - Brandon Hancock
What's up, gang? Hope everyone's having an awesome week so far. Let me get everything ready, and we'll start the fun.

00:04:16 - Ty Wells
I take it you're going to tell us about the world sphere, the AI engineering, because you're wearing the t-shirt. You're promoting it.

00:04:23 - Brandon Hancock
I know, I know. I only have so much AI swag, so I have to represent on my calls, make it look like I know what I'm doing. If you have enough AI words on your shirt, they assume you know what you're doing.

00:04:43 - Brandon Hancock
Just taking a screenshot so I can share the call order for today. Welcome if it's your first time to the call. Love to have new developers and everyone else hopping on. Quick lay of the land — usually the way we go about these calls is first come first serve, and basically when we're going around the room, usually keep it to around six to eight minutes, so that way everyone has a chance to go, and usually just talk about a problem that you're having, happy to help as a team, or any cool AI news or anything that you think the group would find interesting.

00:05:28 - Brandon Hancock
Quick updates for you guys before we kick things off. Just wrapped up an A2A [tool:A2A protocol] tutorial for you guys — agent-to-agent tutorial, just describing exactly how the protocol works, some simple examples, and then pretty excited because the last example in the video, I haven't seen anything else like it on YouTube, but it's basically you have an A2A agent that's using the A2A protocol to talk to a Crew AI [tool:Crew AI] agent, a LangGraph [tool:LangGraph] agent, and another ADK [tool:Google ADK] agent, so it's like the full shebang. It's taken way too long to make and record, so I apologize for the delay. A2A kicked my butt, but I finally figured out how to do it and make it simple for you guys. So that'll be in the video, hopefully actually coming out tomorrow.

00:06:21 - Brandon Hancock
No, I mean, I had so much fun with ADK. ADK, still absolutely loving it. Literally zero negative things at this point to say about ADK. A quick update for future videos — they released, as we saw on last week's chat, basically the FastAPI for it. So it's basically ADK — how do you just quickly expose it so that it's a website that you can almost chat with, or an API endpoint that you can chat with. I will be doing a video on that late next week. A lot of people had questions on deploying ADK agents and that's on the roadmap.

---

<!--SEGMENT
topic: Mitch's Video Generation Tool Demo
speakers: Mitch, Brandon Hancock
keywords: Airtable, Google Image Gen API, shot generation, video generation, Lovable, Next.js, Vite, Supabase, wireframing, data models, ShipKit
summary: Mitch demos a content pipeline tool that takes seed story ideas from Airtable, generates scene shot descriptions, and calls the Google Image Gen API to produce images for video creation. Brandon advises on next steps: wireframe first in Lovable for MVP validation, then migrate to Cursor with a Next.js project rather than staying in Lovable's Vite-based environment.
-->

00:07:08 - Brandon Hancock
Robin, Mitch, you are up first, man. What awesome stuff have we been working on?

00:07:11 - Mitch
Oh, it's been good. I haven't hopped on one of these calls in a while. But yeah, for everyone's info, working on this tool where I basically input a series of prompts that have like a seed idea and then kind of clone ideas from...

00:07:46 - Mitch
So yeah, we have like an Airtable [tool:Airtable] where we have just different series of stories and then those stories would have kind of sub-columns or data points underneath it. Then when we press this button, it will then create a rescape of that idea to then create a series of shots — those shots are just like a long list of describing what each scene is. So then when we do the request to the Google Image Gen API [tool:Google Image Gen API], then we can generate the large list of shots.

00:08:25 - Mitch
And yeah, basically from here, then we generate the videos. But basically this takes the bulk of the work. It's really creating the shots that is key. And if you're curious why we have to generate four, it's because sometimes Image Gen messes up. But yeah, Airtable has been great, but it also has its limitations as far as shot selection and stuff like that. So basically starting to map out, hey, what do I want each page to look like? What do I want to do?

00:09:03 - Brandon Hancock
That's looking clean, man. The thing I was going to say is I got to talk to Mitch earlier and just going through how he has a very cool process that he did in Airtable. And it's like, how do you actually turn this into an application that you can use in a more scalable format than Airtable? So it's cool to see that you're doing the work, man. Have we got to code yet, or are we still in wireframe?

00:09:38 - Mitch
Yeah, honestly, the coding part has been a little bit scary just because of all the TypeScript and stuff. Like, I haven't been on that train yet. So excited for it, but also really postponing it a little bit.

00:09:53 - Brandon Hancock
Yeah, the unknown, man. That's the worst part. But hey, it's not going to blow up.

00:10:00 - Mitch
Hopefully I'm not sharing too much, but this section right here has been the most helpful as far as just, what do I need to think about before I even hop into the code of things. And yeah, I really liked it. I think the one thing I would like in the future is like a checklist. So when we go into this section, it's like a to-do list — okay, if you have a project, here's an example task, and then here's your task, and please fill this in. That'd be really cool, because that's what I had to do after these videos.

00:10:45 - Brandon Hancock
Awesome feedback. No, I appreciate that. That's the goal for ShipKit [tool:ShipKit]. That's the goal — to actually make everything simplified with GPTs to help you with everything, kind of like with the AI Authority Accelerator. But I love that you like them all. Because seriously, most developers are just like, oh, I need to code. And it's like, no, no, no. Before you even code, you need to figure out what the heck you're trying to build.

00:11:24 - Brandon Hancock
▶ Next steps — if I was in Mitch's shoes, what I would do next is as soon as he gets done wireframing it, I'd hop over to Lovable [tool:Lovable] and just have Lovable mock up the entire application. You're going to pay 20 bucks probably to have it do the work for you, but you're going to have a full-blown MVP that you can go, hmm, does this workflow even work for what I'm trying to do from a UI perspective? And then once you're done with that, you now have a Git repository that you can pull down.

00:12:18 - Mitch
<Q>My question is, how far do you kind of document the database and the valid values within the database? Because on the course you were talking about, you had different databases before we even hopped into the wireframe part.</Q>

00:12:29 - Brandon Hancock
<A>Yeah, just data models — I just keep data models as the core information that's necessary. So like if it's a person: name, phone number, email, whatever the core information is, just high level, what value and a quick description. And that's usually enough, especially when you hop over to Lovable, for it to understand what the key data types are. It's just going to make dummy data anyway, so there is no database in Lovable. It's all just fake dummy data. All we're trying to do is say, do I like this workflow in Lovable? That's all we're trying to do.</A>

00:13:14 - Mitch
Yeah, I got mixed up because there's someone else who does Lovable and they connect with Supabase [tool:Supabase]. And I'll have to chat with you guys to see what's the pros and cons of that versus the other.

00:13:29 - Brandon Hancock
▶ High level, real fast — I'm not the biggest fan of keeping the project in Lovable. I want Lovable to go from zero to one, and then I want to be in Cursor [tool:Cursor] as quickly as I can. And I specifically want to be doing a Next.js [tool:Next.js] application. What they actually create is a Vite [tool:Vite] project, and it's not the same. You end up hitting a wall when I'm like, no, I actually want to fetch the data here as a server action, and then I want to pass it down to my client component. There are a lot of walls that you're going to hit with Vite. So as quickly as I can, I get out of there and go to Next.js, once I'm happy with the layout.

---

<!--SEGMENT
topic: RAG Infrastructure for Tabular Data
speakers: Juan Torres, Brandon Hancock, Sam, Al Cole
keywords: LlamaIndex, RAG, PostgreSQL, CSV, vector database, NER, named entity recognition, GPT-4.1-nano, structured outputs, LLM extraction, NVIDIA H100
summary: Juan Torres describes a client project deploying LLMs and a RAG system on an 8x H100 GPU data center to query tabular/PostgreSQL data. The group debates LlamaIndex vs. direct SQL tool approaches, then pivots to discussing how to extract vendor names from free-text description columns — with recommendations ranging from NER models to lightweight LLM calls with structured outputs and a validation-before-write workflow.
-->

00:15:03 - Juan Torres
So I'm working with a client and deploying AI infrastructure, deploying the LLMs [tool:LLM], and then the RAG system in order to manage and get tabular data to read that information. So hopefully they're going to give us the keys to the data center pretty soon. But essentially what I'm working with is a data center that has eight H100 NVIDIA graphic cards. So they can handle pretty big models. So I've got to figure out which open-sourced RAG system, vector database, models I'm going to use for that. I'm thinking of LlamaIndex [tool:LlamaIndex] in order to create the infrastructure in order to unify everything, but I'm open to suggestions.

00:16:15 - Brandon Hancock
<Q>So real quick, what functionality led you to picking LlamaIndex? Like, is there certain things that you're like, oh, I'm mostly doing RAG requests?</Q>

00:16:26 - Juan Torres
<A>Yes, and it seems to have other infrastructure that is well-modulated to handle tabular structured data. I'm not going to be feeding it PDFs. And it just seemed that LlamaIndex had a comprehensive integration of a lot of datasets. So that's the reason why.</A>

00:17:00 - Brandon Hancock
Yeah, because it's mostly CSVs you're working with, right?

00:17:05 - Juan Torres
They do have a PostgreSQL [tool:PostgreSQL] database. So we're going to use the CSV files in order to test the RAG system, but at one point I think we also want to transpose the PostgreSQL database into a vector database if necessary, in order for that data to be funneled directly through to the LLM.

00:17:38 - Brandon Hancock
Yeah, no, LlamaIndex is awesome. They've been around for a minute. They definitely are more on the data side of agents. ▶ Only thing I would mention — for instantly going from PostgreSQL to RAG, I really think with just creating custom queries for data, for each table, you could probably get away with using just custom SQL queries. You don't always have to go to RAG unless you're doing similarity searches. You could actually probably get away with just creating three to five tools that do some sort of regular SQL command, or more advanced SQL commands and joins. You can even have a SQL tool that's just a read tool and all it can do is read, and just give it unfettered access to all the tables and say, hey, create your queries in this read tool.

00:19:53 - Juan Torres
<Q>Before they give us access to the data center, I'm working on transforming a column that has descriptions — just normal language. And I'm trying to explore how I can extract the name of the vendor from that description into the vendor column that may have no entity inside. Would people recommend using agentic systems to do that, or a machine learning model like named entity recognition in order to extract that information?</Q>

00:22:20 - Al Cole
<A>Name entity recognition is one I've seen used. I come from the search space, and that is a lightweight approach. If you've got a known list of entities you can feed it, otherwise you can pick from a collection of captured entities in a database that you could reference. I'll look up some I've been part of in the past to see if that might help jumpstart you.</A>

00:23:00 - Sam
<A>I've had a lot of success with turning an AI or just an LLM call into a named entity recognition through prompting. If the format is variable or there's a reasoning step — inferring what the company name is — I would go that approach using an AI to do it. And it doesn't have to be a strong one. I did a lot of my stuff on some of the early big LLM models and they handled it reasonably well if your prompt was there, so you don't have to go for the beasts out there. It can be a small AI model to do it.</A>

00:24:00 - Brandon Hancock
<A>If I was in Python with a Jupyter Notebook open in front of me, I would probably go more of the AI route, just like GPT-4.1-nano [tool:GPT-4.1-nano], being so cheap at this point. What I would do is: first, go through the table, extract all existing business names, come up with a unique set — here are exact examples of real-life businesses in there. I'd also pull out 10 examples of, here's a description, here's the company name, just to give the prompt some more instructions. Then I would set up the LLM call with structured outputs — hey, you are here to return a name, nothing else, no commentary, the raw name, or NA. ▶ Per row, I would call that, but I would just save it to a CSV first — the ID of the row, the company name — so you can analyze it before you accidentally write to your database. Then validate it with your own eye, and then do a batch SQL write statement. That's how I would tackle it.</A>

00:25:41 - Brandon Hancock
And if you do go down the GPT-4.1-nano route, I'd love if you could let me know how much it costs. I'm guessing like 20 cents, and you could write an insane amount of data, so I think you'll be good unless you're working with terabytes.

---

<!--SEGMENT
topic: Voice Agent Date Bug and MCP vs. Direct Tools
speakers: alexrojas, Brandon Hancock, Robert
keywords: Google ADK, Railway, before_model_callback, get_current_time, MCP, FastMCP, Google Calendar API, Google Workspace, agent deployment, callbacks
summary: Alex demos a voice agent deployed on Railway where the current date becomes stale after deployment because it is hard-coded at agent startup. Brandon diagnoses the issue and recommends either moving the get_current_time call into a tool call or using ADK's before_model_callback to dynamically inject the date before each LLM request. The group also debates MCP servers vs. direct API tool calls for Google Calendar, with Brandon advising caution around third-party MCP servers due to token security concerns.
-->

00:26:19 - alexrojas
Just getting some videos done. Also, I wanted to make a comment regarding Juan. I posted a video now — it talks exactly about the data analyst, what Brandon was talking about. Like in that, I think that is one of the examples of Google ADK [tool:Google ADK], that they have a data scientist that actually does a sub-agent that makes those queries.

00:27:19 - alexrojas
Also, I got addicted to uploading everything in Railway [tool:Railway]. So I did the one on the voice agent and I set it up in Railway. I just ran into one problem — everything works perfectly, but the date does not get updated unless I redeploy.

00:27:45 - Brandon Hancock
<Q>The date? Would you mind sharing code, just real fast, like your screen, and maybe I could point at it?</Q>

00:28:19 - alexrojas
<A>Yeah, so this is the agent. I updated it here in Calendar Utils. According to me, that's where I made it so that every time the chat opens, it kind of calls this last GetCurrentDateTime. But I redeployed it and it's just not happening. I tried a couple of days and I do need to go to redeploying Railway. So I don't know if I need to do something in Railway or can I just do it here in the code.</A>

00:29:37 - Brandon Hancock
<A>Okay, yeah, so what I would do differently is — I think what's happening is your agent started running, and it's a long-running agent. So the second this agent was deployed, today's date is — and that's a hard-coded string. That string is not updated. The second the agent's deployed, the session's running, and it's not every night like, oh, I need to redeploy. It has no idea. ▶ So what you could do, just a quick workaround, is to actually put get_current_time in the tool call down below. And then in the important section, I would say, always call get_current_time before making a request, so that you understand what's going on.</A>

00:31:00 - Brandon Hancock
▶ The other option that you could do is use callbacks. So every time before you make an LLM request, you could always update that master prompt and just at the end of it say today's current date is this — but you'd have to do callbacks for that one. So you can either do the tool call every time, or you could use before_model_callback [tool:before_model_callback]. In the root agent, you would just set up before_model_callback right at the end. And I would definitely go check out the ADK Masterclass, but you'll see an example of exactly how you can update the prompt and just dynamically put in the time.

00:33:08 - Robert
<Q>I noticed that you built a lot of your own tools. So would MCP [tool:MCP] have been an alternate way of interacting with the Google Calendar service?</Q>

00:33:23 - Brandon Hancock
<A>So actually, what I would have done instead now is I would have used Google Calendar — it does have an MCP tool. But that's the kicker. I know there are MCP servers, I just don't see one from Google. There's a random guy, NS Paddy. If you trust him to make sure he doesn't do anything with your keys, then yeah. I prefer only to use MCP servers that come from GitHub or Google. I'm a little hesitant of using random people's MCP servers because they literally have access to your tokens.</A>

00:34:33 - alexrojas
<Q>Could you grab the FastMCP [tool:FastMCP] folder and develop your own?</Q>

00:34:44 - Brandon Hancock
<A>Yes, you could. But for what you were doing — at the end of the day, you're calling five different tools: create event, list event, delete event, edit event. Even if you're doing FastMCP, it'll still be 20% more code, and especially if you're not planning on sharing with anybody, just a straight-up tool call is the easiest. But if your end goal is to connect the entire Google Workspace into your agent, then yeah, I would 100% create a FastMCP server that takes an environment variable, which is probably going to be your credentials or a file path to your credentials.</A>

---

<!--SEGMENT
topic: Al Cole Introduction and Prompt Management Tools
speakers: Al Cole, Brandon Hancock, Andrew Nanton, Juan Torres
keywords: Langfuse, BrainTrust, PromptLayer, prompt management, evals, LLM evals, Google ADK, Google Cloud, Spanner, agent-to-agent, consulting, Silicon Valley, prompt versioning
summary: Al Cole introduces himself as a former Silicon Valley professional services executive now re-entering consulting, shares artifacts from a Google ADK event in Boston, and raises the question of whether a prompt management application is worth building. Andrew Nanton recommends existing tools — Langfuse (open source, HIPAA-compliant tier), BrainTrust, and PromptLayer — for versioning, running evals, and empirically refining prompts across models.
-->

00:36:34 - Al Cole
Nice to meet you as well. Thank you for all the contributions you've been making out there. You've got some great videos. I've been learning a lot. So just to introduce myself to the team here — I literally have wrapped up 10 years of running professional service organizations for Silicon Valley companies. And prior to that, I ran my own consulting practice for 18 years. While I'm catching up on the technical side again — used to be highly technical — I really understand the business of running consulting, so if any of you ever have questions about scenarios or how to partner with companies or things like that, I'm happy to help in that capacity as I'm ramping on the technical side.

00:37:22 - Al Cole
In terms of what I'm focusing on right now — I was at Google, and I'm up here in New England, so I went to Boston to catch a Google event. They had a half day there to go over the ADK [tool:Google ADK]. Just props to you, Brandon — your video was way better than the presentation of the ADK there. You did a much better job explaining their tech.

00:37:56 - Al Cole
I did accumulate some artifacts. I've got the general presentation that gives you an overview of their tech, and then they had some pretty in-depth labs. We did not get agent-to-agent communication, but we did do a bunch with their tools, and we also leveraged Spanner [tool:Google Spanner]. They wanted to do a social platform kind of scenario — they exported data, threw it up in Spanner as a graph, and you were leveraging the social graph to figure out how to put together an event planner. It was actually a clever little lab, all agent-driven. I think we all gather in the AI Developer Accelerator, so I'll put those artifacts there.

00:39:05 - Al Cole
I've got a ChatGPT [tool:ChatGPT] type thing going with Streamlit [tool:Streamlit], which has been fine. I guess a question for the team — as I start thinking about a services focus, from a prompt management perspective, has anyone thought it was worth the time to put together a kind of a prompt application that gathers prompts, maybe tags them for different LLMs that we know they're good for, maybe different roles that you might want to apply them to, and almost kind of validate, rank, and then maybe reapply them if you get a new model to see how well they do with the new model?

00:39:49 - Al Cole
<Q>So my question is, is it worth building a simple app to kind of manage prompts and then maybe leverage them from an embedded perspective in the agents that we build, simply because we know we've validated them with this test harness?</Q>

00:40:11 - Andrew Nanton
<A>Yeah, I mean, you could certainly build your own if you don't like how they're doing it. But some of the ones that I was pretty impressed with were — Langfuse [tool:Langfuse] has a completely open-source implementation that you can deploy locally if you want to just check it out and see. But it will let you version and edit prompts and run evals against those prompts, so you can see what you think of that. BrainTrust [tool:BrainTrust] — I think their UI is more slick, but it's not free. And then PromptLayer [tool:PromptLayer] also looked kind of neat. But yeah, I mean, you could just sort of poke around and see. There's some cool stuff out there.</A>

00:41:00 - Al Cole
Yeah, if it's pre-built, I don't need to build it. I just thought that prompt management would be key, especially with the agents, and especially with models that are evolving — just some way to sanity check and qualify them before you throw that new model in.

00:41:20 - Andrew Nanton
Yeah, and this is what came to mind when Juan was talking about extracting the names of companies out of that description — let's say you did a few of those, you could put the description in, and then the result that you want is the company name, and you put together 15 or 20 of those, and then as you tweak your prompt in something like Langfuse, you can run it like a test suite, and say, oh, well, this got 18 out of 20, or this got 80 out of 200 of the names right, let's tweak this prompt a little bit — okay, well, I got 95 that time. ▶ It gives you a much more empirical way to continue to refine.

00:42:01 - Al Cole
And one of the other reasons I like this type of solution is when you're working with a client and you're able to educate them about the prompts that are being utilized and their effectiveness — there's also value in that education so they understand the probabilistic nature of what you're doing, because you can get varied responses just by pointing to a different model.

00:42:25 - Brandon Hancock
<Q>Al, quick question back to you on business experience — what's the long-term plan?</Q>

00:42:38 - Al Cole
<A>I want to run the consulting practice again. Where I had success was being solution-oriented. One of the novel ways that I built a sustaining annuity with my business was I would join through partnerships with technology companies — would find niche ways to bring, in my case, search before search was really broadly adopted, and helping a relational database and an application built on it discover information in unique ways. I had a whole subscription business going with that for years. ▶ As you're thinking about your agents, you may have opportunities partnering with companies that can't innovate this quickly and being able to help them with some capabilities — essentially get tied into that ecosystem. You can simplify that customer acquisition process just by getting aligned with vendors that you think you could have complementary solutions to.</A>

---

<!--SEGMENT
topic: Ty Wells' Business Software Replacement Projects
speakers: Ty Wells, Brandon Hancock, alexrojas
keywords: Lovable, Cursor, Supabase, Next.js, liquid glass UI, Apple iOS design, POS system, life safety software, SaaS, MCP tool, Google AppSheet, Firebase Studio
summary: Ty Wells describes replacing two expensive legacy software systems for his life safety and security businesses — one asset management tool saving $10K/year and a POS/accounting system worth ~$30K — using Lovable for UI scaffolding and Cursor for backend development. Discussion covers Supabase integration with Lovable, MCP tool stability issues with multiple Cursor instances, and Apple's new liquid glass UI aesthetic. Alex introduces Google AppSheet as a Lovable alternative for Google Workspace-integrated internal tools.
-->

00:44:25 - Ty Wells
Hey, good. How are you doing?

00:44:42 - Ty Wells
Thanks for everything. You put out some great videos. I can't wait to see this ADK A2A video. That should be sweet.

00:45:39 - Ty Wells
I've got four different projects going right now. I've got a couple of businesses, and we're in the life safety business, security business, and we use some software that's just clunky — they don't make customizations, it's a German product — and it's really heavy for managing assets in a life safety fire alarm system type scenario. So I met with my business partner and the operations manager and went over the software. I have access to it. And so I went ahead and reverse-engineered it and rewrote it, and hopefully they're in production next week. So we'll be saving 10 grand a year on fees for something they're probably using 60% of.

00:46:35 - Brandon Hancock
You get a cut?

00:46:43 - Ty Wells
Well, since I'm half owner, I'm going to charge them the one-time license fee. We needed this. I win both ways. It was very complicated software. Just getting the data out of it was crazy.

00:47:00 - Ty Wells
We have another piece of software, same company, we do for accounting, and then we have a POS for the store, and servicing in the back end — access control, CCTV, that type of stuff. I looked at that — that's like 30 grand — so I'm in the process of creating a SaaS solution just for what they need, because they don't use a lot of pieces in the other software as well. Gonna build all that, hopefully I'll have that done in a couple of weeks.

00:47:51 - Brandon Hancock
You're a software machine, man, I love it.

00:47:53 - Ty Wells
I know. The ability to just produce at record pace is just crazy. ▶ I build all that UI in Lovable [tool:Lovable], and then I switch to Cursor [tool:Cursor], and off I go, that's it.

00:48:07 - Brandon Hancock
Yeah, I think there's an arbitrage window right now where anybody can make a Lovable app, but actually getting it functional — Cursor's doing so much for us. I don't know how many years, maybe months, until AI can do all of it. But for right now, oh my gosh, golden era of helping other people bridge the gap and build functionality for them.

00:49:15 - Brandon Hancock
<Q>Are you actually connecting to Supabase [tool:Supabase] through Lovable? Like, are you directly allowing Lovable to connect to Supabase in your own projects?</Q>

00:49:23 - Ty Wells
<A>Yeah, I always start my project, and then I connect it to Lovable, and Lovable will create all the tables and so forth. There were some issues, but that was really in Lovable 1.0. They fixed those. The infinite recursion that it causes — it basically has a trigger on top of a function and on top of a new insert. They fixed that. I haven't run across it — usually it takes a max of three tries for it to fix something. Now, if it goes beyond that, then I go into chat mode and actually walk through it. But no, Supabase running in Lovable is great. And then into Cursor with the MCP tool [tool:MCP]. The only thing is the MCP tool is not very stable. I keep getting disconnected — probably because I've got multiple instances of Cursor running.</A>

00:51:50 - Ty Wells
Let me show you guys this real quick. This is the POS thing that I'm building out. Do you see the style in this? This is a new — what's it called? Apple iOS. This is supposedly their new glass view look.

00:52:17 - Brandon Hancock
Oh, the liquid glass [tool:Apple liquid glass UI]?

00:52:18 - Ty Wells
The liquid glass look that I threw out here, and it actually looks pretty good. I think I'm switching all a bunch of apps to it. It's an easy prompt to get it to switch over.

00:52:41 - alexrojas
Yeah, I ran into this Google product. It's called AppSheet [tool:Google AppSheet]. I don't know if you guys have heard of it. It's the Lovable version, but of Google. And I think if you're integrated in Google Workspace [tool:Google Workspace], you can really take it into production. It's even included if you have a Google Workspace. You could do through Gemini [tool:Gemini], start the app, or just grab a template, or even start your app if you have a database — just upload it. It's more internal and very process-efficient.

00:53:43 - Brandon Hancock
That's very cool. So I'm guessing it's mostly to connect to your internal Google tools and then build apps around what you already have in Google?

00:53:54 - alexrojas
Exactly. If you're integrated into a suite of Google, these can take you like 90% of the way. Yeah, I saw in the Google I/O thing, they mentioned AppSheet. I was like, wait, they have Firebase Studio [tool:Firebase Studio]. I didn't understand why, but oh, it's because internal versus external. Totally makes sense.

---

<!--SEGMENT
topic: Paul Miller's SaaS Exit Opportunity and RAG Architecture for Council Documents
speakers: Paul Miller, Brandon Hancock, Andrew Nanton, alexrojas
keywords: RAG, Docling, hybrid chunking, Chonky AI, MongoDB, vector database, graph RAG, OpenAI embeddings, PDF processing, meeting minutes, political analysis, New Zealand, Supabase, PostgreSQL
summary: Paul Miller shares exciting business news — a potential acquisition by a US company — then presents a technical challenge: building a hybrid RAG system over hundreds of Auckland city council meeting PDFs to extract political promises vs. outcomes for a political party client. Brandon recommends Docling for PDF extraction and the Hybrid Chunker, Andrew introduces Chonky AI for chunking visualization, and the group discusses embedding model consistency, metadata filtering in vector stores, and chaining parallel RAG calls.
-->

00:54:49 - Paul Miller
Hey guys. Latest on my side — I have a sort of a day job that's a SaaS business that I started up about 10 years ago, and suddenly I'm getting this wave of new customers signing up, because one of our biggest competitors seems to have imploded, and it's always good when sales sort of drop out of the sky.

00:55:55 - Paul Miller
And then the other cool thing was, I've been dealing with a US company that was wanting to acquire us, and then they got acquired. And now the company that's acquired them has contacted me and said, look, we want to start conversations. I'd love to get an exit — of course, the multiplier that I want and my other shareholders want. I've been a bit distracted with that. And if you've got upward sales trajectory and you're profitable, that's everything an investor wants. But I kind of get more kicks — while money is nice, I want to just play more with AI.

00:56:53 - Brandon Hancock
Paul, you just get all the money, and then boom, you just play around with AI like me all day, man.

00:57:59 - Paul Miller
I have a practical question on one of the projects I'm doing now. My users want to be able to extract information from a council — our city council in Auckland — they produce minutes of every meeting, it all goes into a PDF for every meeting, there are hundreds and hundreds of these PDFs, and I'm trying to look over the last three years — that's the sort of term of local government — and put it into a system that I can have a kind of a hybrid RAG search, I can extract document NER stuff out of those documents, and I'm thinking that Docling [tool:Docling] is the way to go based on all the calls we've had. <Q>Is there some coding project with a RAG project that I could get started with in Python to just grab it? And I was thinking too, if the objective is to understand what people are talking about in certain meetings, maybe a graph-based RAG might be the better way to go. We're talking about four or five hundred documents, averaging about a quarter of a meg per document. What are people thinking in terms of architecture?</Q>

01:00:03 - Brandon Hancock
<A>So I understand chatting with the documents totally makes sense. The thing that I think you'd want — to get better performance when it comes to chunking — I would be very curious what the transcript style is like. There are multiple different types of chunkers, and you want to make sure the chunker you're using actually ties to the data you're using. Because you could just default to 500 tokens and it is what it is, but you're not going to get as good results as you'd expect. ▶ The Hybrid Chunker [tool:Docling Hybrid Chunker] is one that I've had the best luck with when it comes to working with documents. That document chunker is expecting headings, subheadings, and stuff you would see in a normal document. In your case, it might be more transcript-like, so you might have to create a quick custom chunker.</A>

01:00:16 - Paul Miller
<A>The goal is — I'm supporting one of the political parties, and they need to be able to dig up for certain candidates: they went out and said three years ago they were going to do this, they were going to do that. I wanted to compare what they promised with what they did. So getting the insights of, well, they said they were going to improve the bus routes or the trains — extracting all of that information and what they did, along with the references back to the documents where the source of that information was.</A>

01:04:18 - Andrew Nanton
<Q>Is it specifically transcripts, Paul?</Q>

01:04:22 - Paul Miller
<A>It's meeting minutes, so it's not transcript format. It's quite structured — they throw it together in quite a usable format. It's got some quite logical groupings of data.</A>

01:05:45 - Andrew Nanton
<A>Yeah, okay, so if the meeting minutes are all in PDF, then — I put a link in the chat — Chonky AI [tool:Chonky AI] [link:GitHub - Chonky AI chunking library]. You can grab the whole chunking library off of GitHub, and I was playing with it a while ago, and it seems really good. They have a nice chunking visualizer that somebody made that you can sort of visualize how it's chunking stuff up, and that's really nice because you can see for real how it looks. ▶ The most basic naive chunking where it's just a number of tokens almost never produces good results, and so some of these other ones, if you get more structure out of something like Docling, you can do a whole lot better than that. Also, late chunking — embed first, then chunk — there are some really interesting choices. So you just play with them and see what works.</A>

01:07:25 - Brandon Hancock
▶ I love this — picking the chunker is one of the most important parts. You just want to make sure the data you're capturing goes into the right thing. The recursive chunker is really good for a book or research paper — probably very applicable to you. And then potentially the semantic chunker — both of those look pretty relevant based on what you're trying to do.

01:08:12 - Brandon Hancock
▶ Real quick, something to mention, Paul — whatever model you do the embedding with, remember, when you're doing the RAG request, you need to keep it the same. If you're going to go with an open-source model, whenever for your deployed web application, you need to have the same deployed model accessible. Personally, just if you're going to go for max efficiency, just OpenAI [tool:OpenAI]. Their embedding is just all around the easiest that I've always had luck with. It's gotten insanely cheap. So definitely recommend checking that out.

01:11:07 - Brandon Hancock
▶ Just to give a quick example — I'm working with a fire chief to help them when it comes to doing SOAP operations and answering medical questions. All I'm doing is making two RAG requests, kind of like what Paul was talking about — two separate requests, and then you feed them into your prompt. One goes off and looks up billing, the other is medical. It's all in the same VectorStore, but you can do unique tricks with metadata tags, so you can be like, I only want to look at all embeddings that have this meta ID. What's cool is you can also chain — so that's parallel calls — you can also chain different calls together. For example, you could first just get all the embeddings, the embeddings will tell you which meeting notes they came from, and then you can have a second LLM call that actually reads that whole document. So you can get parallel, sequential — you can get as fancy as you want with a lot of these workflows.

---

<!--SEGMENT
topic: Andrew's HIPAA Toolchain: Langfuse, LLM Guard, and FastHTML
speakers: Andrew Nanton, Brandon Hancock, Juan Torres
keywords: Langfuse, LLM Guard, LiteLLM, spaCy, NER, HIPAA compliance, anonymization, de-anonymization, FastHTML, MonsterUI, Tailwind, Claude, Azure GPT-4.1, BAA, Claude Code, Windsurf
summary: Andrew shares a HIPAA-focused toolchain combining Langfuse (free HIPAA-compliant tier via .edu email) for prompt management and tracing, LLM Guard for local named entity recognition and anonymization/de-anonymization using spaCy, and LiteLLM as a proxy layer. He also introduces FastHTML as a single-stack UI prototyping alternative to Streamlit, and discusses Claude Code and Jules as CLI-based coding tools. The group clarifies what makes a system HIPAA compliant vs. merely anonymized.
-->

01:14:09 - Andrew Nanton
Yeah, not a ton of updates. I'll just mention a few things I've been playing with in case they are useful to anyone else. So Langfuse [tool:Langfuse], which I already mentioned, for the prompt management and evals — that's pretty cool. ▶ And with a .edu address, they gave me a free year of the cloud-hosted version that's HIPAA compliant. Like no questions asked — a single line email, because they said on their website, if you have a .edu address, we'll give you a year. I was like, hey, can I get that HIPAA compliant one? And yeah, okay, sure.

01:14:51 - Andrew Nanton
The other thing, HIPAA-wise, that I was dealing with is using LLM Guard [tool:LLM Guard]. I don't know if you all have heard of this, but it does use named entity recognition — you can, it'll do by default regex, but it will do NER via spaCy [tool:spaCy], and it has a built-in model that is pretty specific to anonymizing health data. And LLM Guard — yeah, that's it — it's all open source, you can grab it for nothing. It has a great integration with LiteLLM [tool:LiteLLM] as well, where you can stick those two together pretty easily, and then Langfuse works well with this combo also. Langfuse has some cool tracing stuff with using this Observe decorator that you stick on stuff, and it tracks things pretty well. So that was a cool combo to work with.

01:16:00 - Andrew Nanton
I haven't really gotten anything to a point that I would want to show it off, but anyway, those are cool technologies. The last thing I'll mention is I was trying to use FastHTML [tool:FastHTML] [link:https://fastht.ml] for prototyping UIs, and it's nice because there is no front-end or back-end — it's all just one thing. And so ostensibly it's pretty simple, and it has an LLMs text file that you can point Cursor [tool:Cursor] or Windsurf [tool:Windsurf] or whatever to, and that's pretty slick. But there's just not enough documentation about it for me to vibe-code my way out of my horrible knowledge of making UIs and web technologies. But it's out there. If people are using something like Streamlit [tool:Streamlit], it's a viable alternative. There's a thing called MonsterUI [tool:MonsterUI] that basically lets you use all of the Tailwind stuff in FastHTML very easily. I'll drop some links in the chat. And working my way around Claude Code [tool:Claude Code] and Jules [tool:Jules] and trying some of these CLI-based tools because I've been such a Cursor guy.

01:17:42 - Brandon Hancock
<Q>For LLM Guard — does it do banning, like, hey, no patient data? Like, you can never say the patient's name?</Q>

01:18:01 - Andrew Nanton
<A>I know it has some guardrail stuff. It's a pretty big library, but what I was using it for is anonymize this content. I turn documents into Markdown, and then it will go through and do named entity recognition and be fairly smart about things like, if someone's named Bill, and it has Bill and William, and it's Bill Jones, and it says Mr. Jones, it'll replace all of those with Person 1. So there's some continuity through the document, and it will let you sort of seed that as well — give aliases and nicknames and that kind of stuff. But that is like 5% of what it does.</A>

01:19:01 - Juan Torres
<Q>So this is the thing that makes you HIPAA compliant, Andrew?</Q>

01:19:07 - Andrew Nanton
<A>No — Langfuse, that's what I was saying, they have a HIPAA compliant version that they were quite generous with giving me access to. As a separate thing, LLM Guard is a tool that will anonymize data — it'll anonymize and then de-anonymize. As far as I understand, that does not make something HIPAA compliant by itself. You could sort of round-trip it to say, replace all of these instances with Person 1, and then ship it out to an LLM, and when it comes back, replace all of that information. But HIPAA is a large beast, and just doing that isn't really enough. It doesn't hurt, but just anonymizing it, especially with an automated tool, probably isn't enough to say you're HIPAA compliant. ▶ I have a HIPAA compliant Claude or Anthropic API account. And on Azure [tool:Azure], I have a HIPAA compliant GPT-4.1 [tool:GPT-4.1] deployment. As far as I understand, if you set up an Azure account, you have a BAA with them. And Amazon has something similar if you want to deploy the Anthropic models.</A>

01:22:17 - Brandon Hancock
<A>Just to clear that up — Langfuse is the observability tool. All it's doing is taking in, hey, what did your agent do? I'm going to store everything about that so you can look at it at a later date. And what they're saying is, hey, Langfuse itself, the way it stores information, it is HIPAA compliant. So yes, it actually will have the patient's name. LLM Guard — that has nothing to do with HIPAA compliance. It's just more about how do you want your LLM to behave.</A>

01:24:06 - Andrew Nanton
And the anonymization processing — that happens locally. That's before any data leaves your system. That anonymization step and using spaCy for the named entity recognition is running locally. It is faster if you have something that accelerates PyTorch.

---

<!--SEGMENT
topic: ADK Agent Building, Workflow Parallelization, and Deployment Roadmap
speakers: Robert, Brandon Hancock, Marc Juretus, Juan Torres, Al Cole
keywords: Google ADK, Crew AI, LangGraph, A2A protocol, Cloud Run, FastAPI, agent deployment, customer service agent, parallel tasks, Cursor workflow, agent-to-agent, ADK agent engine
summary: Robert discusses his journey adopting ADK from scratch, asks about parallelizing task creation in Brandon's AI workflow, and previews a customer service agent he plans to demo. Marc Juretus demos a working arcade game inventory agent (RalloPort) using ADK with a Docker/PostgreSQL backend, raises a PDF parsing issue with ChromaDB and LangChain embeddings, and asks about industry patterns for RAG-based customer service. Juan asks about Crew AI's enterprise UI builder vs. ADK. Brandon previews an upcoming ADK deployment video covering Cloud Run and the new FastAPI-style endpoint approach.
-->

01:24:43 - Robert
Good afternoon, everybody. Just for reintroduction, I'm Robert. Basically, I'm a beginner ADK developer. So I'm starting my journey into AI directly with ADK [tool:Google ADK]. I totally skipped LangChain [tool:LangChain], LangGraph [tool:LangGraph], Crew AI [tool:Crew AI]. So with that being said, this is also one of the obstacles I've had — letting go of my old mindset of the way I used to develop various things and being more trusting of the AI.

01:25:24 - Robert
<Q>As a follow-up question from last week, Brandon — your video about your AI workflow, when you created your master plan document and then went to your tasks — when you created your tasks, do you specifically request for your tasks to be independent of each other? Because there was that great point where you're basically able to feed three tasks to Cursor at the same time to parallelize your workflow.</Q>

01:25:51 - Brandon Hancock
<A>Yeah, so let me just give you an example from what I did this week for A2A. In the A2A workflow, at the end in phase three, we have multiple server agents — one's LangGraph, one's Crew AI, one's ADK. So when I was going through and creating task documents, they were basically encapsulated work. So as I was creating the ADK agent, I was outlining the task: hey, your job is to create the ADK task, it needs to follow A2A protocol, so there's gonna be an agent executor, you need to have a server, you need to spin up a server, here's some example code that you should look at for reference, and here's the purpose I'm trying to accomplish. And then I just rinse and repeat — one for ADK, did another one for Crew AI, and another one for LangGraph. ▶ I tried to keep everything isolated for tasks. However, when I was creating task two, I was totally fine to point back to the first one to say, hey, this task just finished up, I really like the style and approach it finished, now we're just going to do it again for the next technology. So you could also use previous tasks to help you create future tasks.</A>

01:27:24 - Robert
Yeah, totally get that. I also used AI Studio [tool:Google AI Studio] to help me finish an online certification — I was able to upload the manual into the context window, as well as a written journal that I've had of various ideas, and I was able to use this to create the answers that sounded more like me. So that was like another evolution in my process of using AI to push what I perceive to be its boundaries.

01:28:16 - Robert
My next step definitely is to build that agent I've been talking about for the past couple of weeks and have maybe a brief demo next week of a high-level agent just to get feedback. Because now that I've gone through your video about the workflow, I'm finally able to put everything step-by-step. If I tried to create that agent three weeks ago before I went through your content, it would have been a very long, painful process.

01:28:47 - Brandon Hancock
<Q>So what is the goal of the agent you're looking to build?</Q>

01:28:50 - Robert
<A>So basically it's a virtual customer service agent that helps individuals with customer service. The end goal is the learning process of building agents. And I already have a roadmap — the FastAPI to give it voice, and then deploying it to Agent Space. So I already have a roadmap on where to go from when I actually create the MVP on how to actually deploy it into my personal Google Cloud account.</A>

01:30:52 - Brandon Hancock
▶ I will say, real fast — I am going to be doing a second video on deployment now that they've released the new way to deploy. Because everything in the past was, yeah, you deploy a root agent and it just works, like it was magic. But if you want a little bit more control with what's happening, you might want the new approach I'm going to show — you're going to see how it exposes an API endpoint, we can maybe massage some data along the way, so you're going to have a little bit more control. And yes, it will include Cloud Run [tool:Cloud Run].

01:31:33 - Robert
I guess the last thing I just want to close off is that this journey towards being an ADK developer has really required an identity shift on my part — letting go of all the old practices that made me successful previously in my tech career, and embracing a whole new mindset. Similar to what Yoda said, you need to unlearn what you've learned.

01:32:01 - Brandon Hancock
Yeah, totally, totally makes sense. A lot of developers just refuse to use AI — they're like, I'll never let AI write code for me. It's like, okay, cool, it took you one afternoon to make one file. I've literally built the entire project.

01:34:15 - Marc Juretus
Yeah, I'll say, Robert — out of the three frameworks, ADK is the most fun, the easiest to use. LangGraph can be a pain, but Crew AI is kick-butt too, but I really like ADK.

01:34:59 - Marc Juretus
Of course, work is starting to get that AI thing, so we developed a job at Spring Boot [tool:Spring Boot] — there's a Spring AI [tool:Spring AI] that's out there, so we kind of did just a demo where I had an employee where you had the first name, the last name, the skill set needed for the job, and then the last piece was it went out with the AI, pulled in a journey to learn and get them ready to go for the last property in the field for the database.

01:35:43 - Marc Juretus
What I'm working on right now is in ADK — I'm trying to have some fun and stop trying to learn new stuff. I created a company called RalloPort — it's my little game. So I have an inventory where you can go on with ADK with the customer service agent. I have a Docker [tool:Docker] Postgres database where you query it and it'll tell you the number in stock, what they have, what's the price.

00:37:40 - Marc Juretus
So right now I can say, do you have Donkey Kong? And then it'll come back — doing the agent, getting inventory. That's going against Docker. It's pulling in from the database. And then it'll come back. That's the one thing — when it goes back in and pulls in a dataset, it can massage the data. And then the other one is, like, my machine won't turn on, which is obviously going to call the trouble agent.

01:39:13 - Marc Juretus
<Q>So right now, I went into Claude and I said, hey, my company's name is RalloPort, here's our warranty information, give me a bunch of troubleshooting stuff for arcade games. I basically have a conversion to ChromaDB [tool:ChromaDB]. I have it in RAG, using OpenAI embeddings. And I'm able to query that. But my one problem was — I saved this as a PDF using QPDF or something. Any other PDF that I read in for RAG was fine, but this one, when I would pull it in, I would have a bunch of backslash N's or empty values. Was there a specific format of PDF you had to save it as?</Q>

01:40:22 - Brandon Hancock
<A>No, I'm just curious if just the LangChain document processor is what was causing that issue. If you did that exact same process with Docling [tool:Docling], I would be curious if it just does a better job processing PDFs. And I would assume yes. ▶ If you're going to be generating stuff, probably just going directly to Markdown would probably be the easiest. If you're going to be doing the data generation. Oh, it's so clean — easy headings, easy subheadings. I'd also be curious what version of ChromaDB you're using, because I think that could be another one.</A>

01:43:51 - Marc Juretus
<Q>So the question I had was — if somebody had, say, 20 PDFs on the company that were technical documents, would they structure their agent that way — hey, we need to build something that somebody wants to ask a question about any of the items that we own, that would not be in any way database-driven — would that be something that, in the industry, they would pull in 10, 20 PDFs, RAG it up, and make it searchable?</Q>

01:45:19 - Brandon Hancock
<A>Yeah, it's a direct knowledge base is what they would do. There's a company that basically — you just throw in PDFs, we make an open-ended chatbot that your users can talk to. So yeah, if there's just 20 PDFs that are all made to help handle external requests, that's literally exactly what you would do.</A>

01:49:34 - Brandon Hancock
For Crew AI, they have been cranking out a bunch of updates — potentially doing a video with them on Friday. I was curious if you guys had any questions for them. <Q>So far I was mostly just going to ask about new use cases, any new ways developers can get involved, make money. Are they releasing any new tools coming out soon?</Q>

01:50:43 - Juan Torres
<Q>What is the highest market demand for people you see in Crew AI right now in the market? Like, what is it that they're building agentic systems for — news analysis, spreadsheet analysis? I just want to know what's the highest demand out there, specifically for the finance sector.</Q>

01:51:34 - Paul Miller
<Q>With ADK out, where does Crew AI sit?</Q>

01:52:09 - Brandon Hancock
<A>I'll tell you my answer — for standardized workflows, there's not a better tool. I think it is the most straightforward tool to allow you to automate processes with AI. Especially the multi-agent aspect. In ADK, you can't do true multi-agent where multiple agents work on the same task collaborating together. Crew AI still has that — no one's even come close right now on true multi-agent to where they're all working on the same task. Because right now, even in ADK, it's just straight-up tool calls. It's like, okay, agent, what do you think? Okay, other agent, what do you think? And then it takes action. It's never really true multi-agent. ▶ Straight-up workflows, Crew AI dominates. But the second I have to do chat with it, that's when I would probably have to make a harder decision about how important chat is versus AI automations.</A>

---

<!--SEGMENT
topic: A2A Protocol Future and CRM Recommendations
speakers: Brandon Hancock, Al Cole, Andrew Nanton, Nate Ginn, Paul Miller, Ty Wells, Bastian Venegas
keywords: A2A protocol, agent-to-agent, authentication, MCP, GoHighLevel, Pipedrive, Attio, CRM, ADK agent engine, Crew AI, multi-agent, abstraction
summary: Brandon explains the A2A protocol as an abstraction layer above tool calls — enabling agents to communicate without knowing each other's internals — and notes it is still early (v0.2) but will become critical once authentication is solved. Al Cole shares Google's internal framing of A2A as the path to competing/collaborating agent architectures. The session closes with CRM recommendations for Nate Ginn, with Brandon pitching GoHighLevel and Paul recommending Pipedrive for its API accessibility.
-->

01:54:40 - Andrew Nanton
<Q>You mentioned that you were doing this A2A stuff, and I'd be curious — while we're discussing Crew AI and MCP — what are his thoughts on A2A and is there a role in Crew AI for that? And do you think A2A is going somewhere or do you think it's a passing thing?</Q>

01:55:01 - Brandon Hancock
<A>So, if we just start abstracting up from the bottom — an LLM to a tool call, it's kind of abstracted, meaning the agent doesn't know what's happening in the tool call, all it knows is the parameters it's gonna send in, and then it knows what the tool is gonna send back. What A2A is doing is basically just abstracting upstream. So instead of, hey, I don't need to know exactly the code that's happening inside of this tool call — well, they're just going upstream and saying, hey, I actually don't need to know the inner workings of this other agent, I just need to know what inputs I can give it, what I can expect to get back, and when I should call it. All they're doing is going up the abstraction chain. It kind of feels like Web3 right now — I see the need for it in a world where Andrew's agent is trying to talk to Paul's agent, and they're gonna go hash stuff out, figure a plan, see when they can meet, schedule a trip. ▶ The second they finish getting authentication working — that's when it makes sense. When they can properly do handshakes, it's gonna be so easy to say, all right, I would like to go send an email, check a calendar, and almost not have to do MCP. I do think it's early, but it's one of those things — I think it's a very important technology that will gain traction as more companies make external-facing agents.</A>

01:57:31 - Al Cole
And just 30 seconds — this is Al again, Brandon. I wanted to highlight from the slides I'll share with the team. They covered A2A very lightly, but they did give us this diagram. I remember you mentioning the same thing about Crew AI and its ability to have competing agents and then evaluate. They're claiming in their slides that A2A is how you would get there — that kind of architecture where you have competing agents and then synthesize.

01:58:05 - Brandon Hancock
No, it totally makes sense. ▶ Definitely early. I think the second 1.0 comes out, probably in a few months, it'll be simpler, it'll have better authentication, and then I think you're going to see an insane rise in people building front-end and internal agents. Because everyone's always like, oh, I want to have an army of agents. Well, right now you can't. Because I have an ADK agent, it has a fixed number of sub-agents, and that's all that little cluster of agents can do. There's no actually talking to the next cluster of agents. That doesn't exist right now. But that's what they're solving.

01:59:22 - Brandon Hancock
Okay, any other quick questions?

01:59:42 - Nate Ginn
Okay, so I'm gonna dummy down this conversation like I usually do. I'm looking for a CRM program. And I know there's a lot of them out there. But with all the stuff that you're working on, it seems like this would be like the simplest thing to create. But where it might have not only the database of your contacts, but also like a chat component that you could ask questions like, when was the last time we had a conversation with this contact? <Q>Anyway, I just was trying to get suggestions if anybody had a recommendation for a simple CRM.</Q>

02:00:48 - Brandon Hancock
<A>▶ I'd seriously love for everyone to check out GoHighLevel [tool:GoHighLevel]. A hundred bucks a month. You get a CRM. You get the ability to send emails, text messages, phone calls. You can set up pipelines, automation. Now they have the ability to do AI employees. I think eventually all small to medium-sized businesses, it makes sense to just use GoHighLevel for everything. Chatbots — GoHighLevel, put a chatbot on your website. They already allow you to do that. I am now curious if they're going to allow you to automate outreach using these AI employees.</A>

02:02:03 - Ty Wells
I built my own just because it was more AI-related. Chatbot's already built into it and prompt library and all kinds of stuff. But it was that and Attio [tool:Attio] I looked at as well. But yeah, GoHighLevel — can't beat the price for what you get.

02:02:25 - Paul Miller
<A>▶ Just from my perspective, we just moved my SaaS business back to Pipedrive [tool:Pipedrive]. It's just really easy to use and it's simple and it's got a good UI/UX. It's got a really good API that comes with it. So if you're wanting to do really weird queries or update records in a unique way, it's really easy just to go into Claude and make an interface that communicates with the API. So you might say, oh, I want to create tickets against customers in this way or these types of records from this other database. And it's so easy to do because Pipedrive's been out there for quite some time. You can do that with the base license — whereas with GoHighLevel, to get the API access, you've got to go to the $300 a user one. But GoHighLevel's got a lot more features included in the price. Pipedrive's one of those models that you keep stacking on top, and it ends up getting quite expensive. But it's so simple to use.</A>

02:04:00 - Brandon Hancock
All right, any final questions, guys? I gotta hop off to get ready for another call in just a few. I love all the — I've learned so much. I love these calls because I learn so many new things, and I love getting hyped up to see all the cool projects you guys are working on. So I always love the Tuesday calls. But just want to check — any final things? If not, I'll post this recording, guys. I'll keep y'all posted, and A2A coming out, the Crew AI interview hopefully on Friday. And I'll keep you guys in the loop. Hope you guys have a great rest of your week, and talk to you soon.

---

=== UNRESOLVED SPEAKERS ===

- **Sam** — Contributed advice on NER and LLM-based entity extraction (around 00:20:57–00:23:58). Raw name "Sam" does not appear in the SPEAKER_ALIASES context block and could not be resolved to a canonical full name.
- **alexrojas** — Contributed throughout the session (voice agent demo, AppSheet mention, RAG hybrid question). Raw name "alexrojas" does not appear in the alias map as a resolvable full name.
- **Bastian Venegas** — Brief comment on Crew AI MCP usage (around 01:54:05). Raw name passed through unchanged.