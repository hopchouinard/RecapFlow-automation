=== SESSION ===
date: unknown (estimated recent, post-Cursor background agents release)
duration_estimate: ~2 hours 50 minutes
main_themes: Cursor background agents via Slack, ShipKit template library, Oracle NetSuite automation, Google ADK agent-to-agent errors, AI tool recommendations, MCP performance, voice AI latency, LiveKit, Claude Code vs Cursor, CodeRabbit, cursor rules and iteration, asset management app demo, FastAPI + ADK frontend integration, LangGraph vs ADK, HIPAA-compliant infrastructure, AI consulting go-to-market strategy, SEO optimization, GitHub Copilot agent mode, enterprise AI adoption

---

<!--SEGMENT
topic: Cursor Background Agents via Slack
speakers: Ty Wells, Marc Juretus, alexrojas, Brandon Hancock
keywords: Cursor, background agents, Slack integration, Lovable, Supabase, session management, scaffolding, remote development, agentic workflow, desktop IDE
summary: Ty Wells describes a newly released Cursor feature that allows background coding agents to be triggered and monitored via Slack, enabling development to continue while away from the computer. The group discusses how this fits into a workflow starting with Lovable for scaffolding and Supabase for auth, then handing off iterative feature work to remote agents. Brandon Hancock redirects the group to a Q&A-first format for the session.
-->

00:00:00 - Ty Wells
And respond back and say, okay, so if you plan out your development process, just have all your stuff on your phone, you're ready to go, and just kick off the initial scaffolding, and then have your stuff right on your phone, just send it off through Slack, and it'll run that agent until it completes, tell you the response, and then you can start another.

00:00:20 - Ty Wells
And so, four hours later, when I come back from golfing, I've got an app.

00:00:26 - Ty Wells
I mean, I've got what I needed, and I golfed.

00:00:29 - Ty Wells
Hopefully I shot it around.

00:00:30 - Marc Juretus
<Q>This isn't a predefined task that you're trying to accomplish — it's you're trying to actually write an actual application?</Q>

00:00:37 - Ty Wells
<A>Yeah, but let's say my application had 10 features, right, and I wanted to — I don't want to waste a minute not building it. So if I'm golfing, I would kick off an agent. For Cursor [tool:Cursor], it's installed locally, right? It's a desktop app. I don't know if it's for Mac, but I have to physically be in front of my computer to do it. This gives me the option. If I plan it out, which I always do, kick it off while I'm golfing, and as I'm playing, I'll just kick off additional ones if it completes the task that I assign. So I don't have to physically be in front of my computer running the Cursor application.</A>

00:01:16 - alexrojas
<Q>How reliable has it been for you? Because many times when you're in Cursor, you can actually say, oh no, use this endpoint instead or something.</Q>

00:01:29 - Ty Wells
<A>It just came out today, so I haven't tried it yet, but I'm golfing in the morning, so I will be doing it. I'll kick off the scaffolding tonight, and that's the key — just planning out really the features and stuff that you want. So I plan it right down, so there's not much room for interpretation of what I want. I treat it like a junior developer, although it's a senior developer, and so I kick that off and just wait for it to come back.</A>

00:01:57 - Marc Juretus
I got to admit, Cursor is pretty impressive. I was playing around with it, because I just started with Supabase [tool:Supabase], so I had it write Next.js [tool:Next.js] to basically an authorization page and a CRUD. And I was like, wow, I really only had to change about 10% of that code for what I was trying to accomplish.

00:02:25 - Ty Wells
Yeah, what I like to do is I'll kick off in Lovable [tool:Lovable], right, for two reasons. One, it will integrate initially and get your Supabase set up and get your authentication set up. Big start, right? Then I'll work on session management in Lovable to make sure I've got specific ways I want to deal with session management. Once that's done, I'm looking really at features, right? So that's where those agents would come in place. I could kick those off because sometimes they take long. It's an iterative process, so I physically have to stay in front of my computer. So this is like a game changer for me. I don't have to be in front of my computer, but I can continue working and just communicating via Slack [tool:Slack].

00:03:23 - Ty Wells
I was in the Bolt.new [tool:Bolt.new] hackathon, and we had another community hackathon. So I was a little busy, but I caught up with it. And yeah, it might have come out a couple days ago, but it's going to be powerful, I can tell you, for me at least.

00:03:42 - Brandon Hancock
So, real fast before we keep going down this path — one thing I was going to say is today, I did promise you guys we were going to start doing some type forms to submit questions beforehand. So what I just did is I dropped a chat message to say, hey, if you have a question, drop that first. And then we'll just knock out questions first today. That way, if you're stuck on something, we get to keep you cruising.

---

<!--SEGMENT
topic: ShipKit Template Library Preview
speakers: Brandon Hancock, Juan Torres, AbdulShakur Abdullah, Jake Maymar
keywords: ShipKit, CLI, RAG applications, agentic apps, Next.js, Supabase, Vertex AI, Google ADK, LM Arena, chat templates, vector store, embeddings, chain of density, LangSmith
summary: Brandon Hancock previews ShipKit, a new project providing a CLI-driven template library for spinning up AI applications including chat, RAG, and agentic apps. He demonstrates repurposing a chat template into an LM Arena-style model battle app in 25 minutes. Attendees ask about LangSmith integration, interactive project guidance, and RAG customization with advanced retrieval techniques.
-->

00:04:36 - Brandon Hancock
Okay, so let me share my screen. All right, so here is the thing I was working on for you guys. So ShipKit [tool:ShipKit] — this is the new project I'm working on for you guys — basically what it's going to come with is you're going to be able to launch new projects, like AI projects. So normal chat projects, RAG applications, and then you'll also be able to launch agentic apps. So eventually, you'll be able to run a command like this, and what it'll do is it'll walk you through the process of making an app, with a nice little CLI, and then it'll spin up these different templates. So there'll be six to eight templates, and each template is basically going to come with everything you need to crank out the app.

00:06:07 - Brandon Hancock
So I had this chat application that I was working on — just trying to prove to myself that it worked. This is basically like Theo's — I don't know if you guys watch Theo on YouTube — he basically has the ability for you to chat with any model. So it's basically that application. And I was like, so that's the first template. I was like, all right, let's see if we can actually turn this template into something else. I don't know if you guys have heard of LM Arena [tool:LM Arena] — so I was like, hey, here's a template, I create new tasks, the new tasks describe what changes I want. And within like three of these templates, I basically launched a new app that lets you test out different models against each other.

00:07:12 - Brandon Hancock
The part that was just pretty cool is like this literally took 25 minutes to take an existing template and then repurpose it, just taking a few screenshots. ▶ But yeah, once you have these different projects set up with the right rules, once you have it set up with the right rules, the right templates, and just giving AI context when it needs it, you can crank out projects.

00:08:00 - Juan Torres
<Q>Have you thought of integrating LangSmith [tool:LangSmith] in order to assess context window usage in terms of comparing the different models?</Q>

00:08:13 - Brandon Hancock
<A>Yeah, I mean, there is towards the end of it, there's set up with PostHog, add in Sentry for front-end issues. So there is a lot more things at the end that will be added in — that will 100% be one of them.</A>

00:08:31 - AbdulShakur Abdullah
<Q>I just wanted to know if there was kind of an interactive platform that basically you could interact with and say, this is what I'm looking to build, and it'll tell you which part of the dev kit to use.</Q>

00:08:49 - Brandon Hancock
<A>So it is still all a work in process. It really just depends — what core functionality do you want? Do you just want a chat app? Do you want a RAG app or an agentic app? That's really the core question. Then after that, the cool part is you have access to all the other templates. So it's just like, oh, I want an agent in the chat. Once you hook these templates up, you basically just say, go grab the chat functionality from this working application. Because that's the main thing — once AI has access to something that is working, oh my gosh, you can hum. That's actually where the hard part is, because 90% of the time when you're starting something new, you're starting from scratch.</A>

00:09:40 - Brandon Hancock
▶ So for chat it's Next.js for frontend and Supabase for RAG, because you want to support video, images, and text. It is more of a text-based just because Google's the only provider that supports video — like RAGging or chunking and embedding videos. It's the only one that really does it. So that's why that one's all Vertex [tool:Vertex AI]. And then Agentic, I'm still in between — I'm most likely going to go down the ADK [tool:Google ADK] route, but that's later this week going to start knocking out those templates.

00:10:23 - Jake Maymar
<Q>The RAG — can I fine-tune the RAG? Can I basically add in different versions? Like how easy is it to take it from vanilla RAG and then start applying like chain of density or any of those techniques?</Q>

00:10:49 - Brandon Hancock
<A>So the cool part is most of the things you're talking about — you already have the vector store set up, you already have all the embeddings in the vector store. And then it's really just afterwards, after you've already made the query, that's when you can add in all the additional layers. Like if you wanted to do a single shot, cool. If you wanted to break up a query into its subcomponents and then make multiple queries in parallel — you could actually get as complex as you want. The key thing is just having the pipeline work and then adding all the additional layers on top.</A>

---

<!--SEGMENT
topic: Oracle NetSuite Automation with Apache Airflow
speakers: Brandon Hancock, Cyril I, Al Cole, Juan Torres
keywords: Oracle NetSuite, Apache Airflow, DAGs, ETL pipeline, automation, AWS, Make.com, n8n, CRM, enterprise automation, directed acyclic graphs
summary: Cyril I asks how to build automations within Oracle NetSuite for a supplier company internship, noting the system's outdated interface. Brandon Hancock recommends Apache Airflow for enterprise-grade DAG-based automation, drawing on direct experience automating accounting workflows in NetSuite. Juan Torres adds context on DAG file setup and AWS deployment costs.
-->

00:11:45 - Brandon Hancock
Cyril, I saw you said you had a question about Oracle and NetSuite. So I've used it — I'd be curious what your situation is.

00:11:56 - Cyril I
<Q>So unfortunately it's not my decision, but I'm doing an internship right now, and the internship is for some supplier company, and they use Oracle NetSuite [tool:Oracle NetSuite] as a CRM for their company, and they require some automation tools in terms of deliveries and some internal systems. I'm curious — what is the way to create an automation within it? Because it is the first time I've seen such a system. I'm aware how to create automation in cloud services like AWS, and how to use automation on websites like Make.com [tool:Make.com] and n8n [tool:n8n], but Oracle NetSuite — I'm just looking at it, it looks so outdated, and I'm not quite sure how to approach the problem.</Q>

00:12:46 - Al Cole
The interface feels like 1990, doesn't it?

00:12:53 - Al Cole
I've used it many times. I haven't tried to hook into it programmatically, but you know you've got Oracle as the back end. There must be APIs — I'm sure that thing's been around forever.

00:13:10 - Brandon Hancock
<A>So going off what I was saying — yeah, actually the last company before Cray AI, it was called Softbox, and it was NetSuite exactly like what you're saying — more for CRM and for accounting purposes. And the way we built all automations was using Airflow [tool:Apache Airflow]. So just Apache Airflow. That's what we did. I mean, it was as enterprise as enterprise gets with NetSuite. NetSuite does expose some APIs. It's disgusting how you have to create all the credentials. But that's what we did, and it worked — it literally worked fine, and it's how we automated the entire accounting of that business.</A>

00:14:03 - Cyril I
<Q>So how would I use this Airflow tool? What does it actually do?</Q>

00:14:13 - Brandon Hancock
<A>You can produce DAGs — directed acyclic graphs. So when you think of Make, that is a DAG because it is basically a node that does an action and it moves to the next node and does more actions. So that's literally all it is. So if you were to come in and say, hey, this is the most enterprise approach to working with this other super heavy old-school enterprise application — when we were working on it, we used ChatGPT [tool:ChatGPT] religiously to help us figure out how to set these things up because they were so old and disgusting. So the good news is they're old, so all the documentation's already in OpenAI [tool:OpenAI], and you really don't have to look up latest docs. It's already all there.</A>

00:15:11 - Juan Torres
I just wanted to mention that you can create a DAG file — that's the one that's going to instruct how your ETL data pipeline is going to move forward. For me, at least, it was two documents that I had to set up. And I did it in AWS [tool:AWS]. It's connected AWS to a database within a VPC, a private virtual cloud. But you might actually be able to do it on your local server if you have access to that. It's relatively easy if you have Python. It's just that if you do it in AWS, it's going to be a bit expensive.

00:15:51 - Cyril I
<Q>And then the other question is, should I even bother trying to use built-in workflow tools in NetSuite, or would it just be a waste of time?</Q>

00:16:08 - Brandon Hancock
<A>I just know there were limitations of what you could and couldn't do in theirs, because they are more of a CRM accounting tool, so they're not going to give you all the niceties of a pure automation platform like Airflow. That's why we just went out. It is pricier, but enterprise tools are pricey for big businesses. Ping me if you have any questions on it, but that's literally how the last company did it, and it worked.</A>

---

<!--SEGMENT
topic: Google ADK Agent-to-Agent 503 Error
speakers: Matias Coca, Brandon Hancock
keywords: Google ADK, agent-to-agent, A2A protocol, 503 error, localhost, server-sent events, UV, pyproject.toml, version pinning, FastAPI, multi-agent
summary: Matias Coca describes a persistent 503 network communication error when running Google ADK agent-to-agent locally using ADK web, where the host and agent connect and process correctly but the web UI reports an error. Brandon Hancock suggests cloning the reference repo to isolate whether the issue is version-related or a code configuration problem, and emphasizes pinning package versions due to rapid ADK changes.
-->

00:16:57 - Brandon Hancock
Matthias, if you want to — I saw you had your hand up.

00:17:00 - Matias Coca
Hi, I was working with ADK and agent-to-agent, and finally I can create a host and an agent and send a request between them, and they can connect. I interact with the host, and the host sends a message to the agent, but I continuously receive an error that I put in the chat — this error doesn't stop the process. It's like the host doesn't connect with the client — a network communication error, 503 — but the agent does what it does, and both are running on my local machine. I opened two terminals, one for the agent and the other for the host with `adk web`, using UV, run, all these commands, but I continually receive this error. I don't know if you've faced it — I investigated and everything I look at says there is a connection error, but the connection is there, the agents connect between each other, but I receive this error in the web UI.

00:18:57 - Brandon Hancock
<Q>Did you copy my repo and start getting this, or was this like you've spun up your own thing?</Q>

00:19:03 - Matias Coca
No, I used part of your repo, but with my own code for the agent.

00:19:14 - Brandon Hancock
<A>Okay, because 503 is more of like a — hey, this server is unresponsive — kind of thing, which is interesting because it is localhost. So whenever I was setting it up, I had zero issues with that error. I would be curious if you just 100% ran my project, if you get the same error. Because one of those things — it worked on my machine. So I would be very curious if you can just clone my project, run it, and if it works, fantastic. That means there's something wrong with the way your server is sending events to your client, because with A2A [tool:A2A protocol], each agent gets wrapped in its own server. So I'm assuming something is going wrong in that area.</A>

00:20:37 - Brandon Hancock
▶ The only other thing is just make sure you are using the same version I'm using, because they are changing stuff rapidly and breaking stuff — they're moving so fast. So I would just make sure the exact version of A2A Python that I was using — make sure you're using that. This could just be a new bug that they added.

00:21:00 - Matias Coca
When I UV-added the packages, I didn't put the same versions — the pyproject.toml has the same packages, but I didn't check the versions exactly. But the error is not stopping the process. It's like in the ADK web, I chat with the host, and the host sends a message to the agent, and the agent begins to process all, but I receive this error in the web UI.

00:21:42 - Brandon Hancock
Yeah, literally no idea, but just please keep me posted, because that one is interesting.

---

<!--SEGMENT
topic: Recommended AI Content Creators and Channels
speakers: Brandon Hancock, Tom Welsh, Bastian Venegas
keywords: Theo T3, Greg Eisenberg, Matt Berman, Prompt Engineering, WebDev Cody, Programmatic Engineer, YouTube, Twitter, T3 stack, full-stack development, personal brand
summary: Brandon Hancock answers a question from AbdulShakur Abdullah about the best people to follow in AI, sharing his personal recommendations including Theo (T3), Greg Eisenberg, Matt Berman, and Prompt Engineering. He shares personal background on how Theo's T3 stack guidance helped launch his career. Community members add additional channel recommendations in chat.
-->

00:21:51 - Brandon Hancock
Abdul, I think this is a cool question for everybody — what are the best people to follow with AI, because he's just trying to follow the fewest number of people?

00:22:08 - Brandon Hancock
Main ones — I usually follow Theo [link:youtube.com/@t3dotgg]. He is like, I watch his video every single morning when I take a shower. Greg Eisenberg, I like a lot, but I've kind of stopped watching some of his stuff a good bit. What are some of the other ones? Feel free to hop in if anyone else has really good suggestions.

00:22:52 - Brandon Hancock
Oh, yeah — Matt Berman, Prompt Engineering. All those are awesome. Tom, thank you, buddy.

00:23:08 - Brandon Hancock
I mean, I'll just share Theo's channel — he's actually, I know he has some controversial opinions, but legit awesome guy. Like honestly helped me launch my entire — quick background on Theo just because I owe a lot to him. When I was at my old job back in like 2020, I was trying to get into more full-stack web development. He came up with the T3 stack [tool:T3 stack] — game changer for building full-stack web applications that were type-safe. I had multiple questions. I would just ping him sometimes on Twitter. He actually responded, helped — that led me to get new jobs. So yeah, he literally — I owe a lot to him because he helped kind of bump-start a career. So seriously, if you're not following him, definitely recommend.

00:23:53 - Brandon Hancock
Bastian dropped some good ones — WebDev Cody [link:youtube.com/@WebDevCody]. Literally all those are so good. I think someone said the Programmatic Engineer, Brett — this guy is awesome. If you're looking more for just inspirational stories, I mean, some of them are wild. Like I watched this and I'm like, damn, what am I doing wrong with life? I'm not 21 and I do not have that. So sometimes it's a little disheartening, but a lot of these are really cool just to see how other people are absolutely crushing it.

---

<!--SEGMENT
topic: Claude Code Swarms and Background Coding Agents
speakers: Jake Maymar, Brandon Hancock, Andrew Nanton
keywords: Claude Code, Claude Code Flow, swarms, Spark, Jules, Google Jules, background agents, GitHub, pull requests, async coding, CodeRabbit, Gemini CLI, cursor IDE
summary: Jake Maymar introduces Claude Code with Swarms (Spark) as a next-level background coding tool capable of producing millions of lines of code autonomously. The group discusses Google Jules as an async background agent that checks out code in a VM and returns pull requests. Brandon Hancock explains why Gemini CLI's single-shot limitation prevents him from using it in pipelines, and CodeRabbit is introduced as an automated PR review tool with a free Cursor extension tier.
-->

00:25:00 - Jake Maymar
<Q>So I'm curious about Claude Code Flow, if anyone's using Claude Code Flow with Spark.</Q>

00:25:11 - Brandon Hancock
I'm not, but if someone else is, I'd love to learn more about it myself.

00:25:19 - Jake Maymar
<A>Yeah, so it's — sorry guys, long day — Claude Code with Swarms [tool:Claude Code], and I really think this is next level. I don't know what the hardware requirement is, but the demos I've seen are kind of mind-blowing. I sent you a link, Brandon. The thing is, I just haven't had time to really look into it. Similar to what Ty was talking about this morning — you kind of set it up, and then you go away, and then you come back, and you have something finished, and then you use Cursor or basically some other IDE to sort of clean up the code or refine the code at that point. But it looks really, really amazing, and I've actually used some of the repos that it produced, and it's pretty amazing stuff.</A>

00:29:41 - Jake Maymar
The thing that was blowing my mind, Brandon, is the guy made it and it was like three million lines of code.

00:29:50 - Jake Maymar
Yeah, the Spark and just the things he was making with it were just massive. And you can use them now. Fathom [tool:Fathom] is a neural network — I don't know if you guys have used Fathom, but it's been around for a long time. It's not very efficient — it's heavily GPU and processor intensive. So Roof, which Ty put the link in — he made Roof Fathom, and it runs on your phone. So just to give you an idea of how powerful these things are.

00:30:49 - Brandon Hancock
Al, I saw you had a question real fast. If you just want to hop in and say it, just so the group can hear.

00:42:51 - Brandon Hancock
Abdul, I'm probably not going to be doing any updates on that one. Just because ShadCN [tool:ShadCN] has changed, Stripe [tool:Stripe] has changed, Next.js is a whole new version — some of the core fundamental technologies have just absolutely changed. But the good news is in the new one, there'll be so many more examples. So you get to pick and choose from them. And what I'm aiming to do with ShipKit is basically to have it be the project where as time goes on, I keep adding new templates to it.

00:44:36 - Brandon Hancock
Jake, if you want to hop on real fast for your question.

00:44:58 - Jake Maymar
So I'm curious about Claude Code, Claude Code Flow, if anyone's using Claude Code Flow with Spark.

00:26:54 - Brandon Hancock
So I would love to use it, but there's one thing missing that's preventing me from doing it. What I would love to do is in Gemini CLI [tool:Gemini CLI] is kick off like six jobs at the same time. I would love to say, hey, the second I kick off something new, I want to kick off six prompts in parallel. But the kicker is, with Gemini prompt, it is a single shot. So it is not doing the interactive loop over and over and over fixing. So that's what's preventing me from going deeper into using it in an actual pipeline or in a CI/CD pipeline.

00:50:01 - Paul Miller
Jules? Andrew's saying Jules. How much is Jules? Is it affordable at the moment?

00:50:08 - Andrew Nanton
<A>Oh, when I played with it, it was free. I mean, in true Google fashion, they've got eight different things that have overlapping functionality, and they might just decide to stop doing any of them tomorrow. But it did look like you definitely can set it to do something and walk away and come back a long time later.</A>

00:50:37 - Andrew Nanton
So the way that it works, as I understand it — you have to connect it to GitHub [tool:GitHub]. It checks out a copy of your code, runs it all in a VM somewhere, makes its changes, and then sends you a pull request when it thinks it has done what you want it to do.

00:50:53 - Brandon Hancock
Yeah, this is what I wanted right here, the async part. Because I just want to have almost like a peer reviewer, because that's how most coding is — you do the work, and then someone reviews your code. I just want to have that guy. I don't want to hire a full-blown engineer to do that. I want AI to do it for me.

00:51:25 - Brandon Hancock
I've seen CodeRabbit [tool:CodeRabbit]. I know it's free if you're working on an open-source product. But this is what Andrew's talking about — it's pretty nice. Every time you create a PR, it automatically reviews it, checks to see what's happening, gets a summary, and reviews — oh, this is dead code.

00:52:29 - Bastian Venegas
▶ You can use the extension in Cursor for free, and it will — every time you have a branch, it will check — it has some limits, like if you push like 10 commits in hours it will check them all, but if you do like four per day, it's free. The only caveat is that it won't apply the changes that the AI suggests on its own, but it will give you a prompt to pass to the Cursor agent. That's the only difference between paying and not paying for it in the IDE. Because also the cool thing is that you can connect this to Linear or Jira, or any of those tools where you track your issues. And then you have a full system where you automatically review all of that with CodeRabbit.

---

<!--SEGMENT
topic: MCP Performance and Voice AI Latency
speakers: Maksym Liamin, Brandon Hancock, Bastian Venegas, Ty Wells
keywords: MCP, Model Context Protocol, JSON-RPC, tool schema, 11 Labs, Twilio, LiveKit, voice agents, latency, Azure, OpenAI real-time, Mexico, peak hours, containerization
summary: Maksym Liamin asks whether MCP servers pre-select tools before passing them to the LLM (reducing context), which he believes explains observed speed improvements over passing full tool schemas. Brandon Hancock clarifies his understanding that MCP still returns all tool summaries. Maksym then asks about voice AI infrastructure to reduce latency for a Mexico-based deployment using 11 Labs and Twilio, and Bastian Venegas recommends LiveKit as a solution that supports Azure-hosted OpenAI real-time with regional deployment options.
-->

00:33:52 - Maksym Liamin
So what I noticed is that whenever we switched our voice agents from normal tool schemas in 11 Labs [tool:11 Labs] to having an MCP server [tool:MCP] where we have all the tools defined, it became noticeably faster. And then once I started reading it, I somehow got an idea — so if we pass a whole tool schema in JSON to an LLM, basically what we do is we pass all the tools every time, and then the LLM takes the decision which one to take. What I understand happens with the MCP server is that it has a router, which is run by the agents library — I think this is the most common for MCP — and it kind of already pre-picks the tool that will be used by the LLM and passes only this tool to the model. So instead of passing all of them and choosing from all, you already have a targeted one that you pull — just one — and therefore it's faster. <Q>Is that how I understand it correctly?</Q>

00:36:27 - Brandon Hancock
<A>So my understanding — what MCP does is when you say tools, it's returning a summary of all available tools. So if you have five, it's returning the name, type, name, description, and parameters. But from my understanding, when you just have an ADK agent or a Cray AI agent, it still is the same thing — all it's doing is getting the name, description, and parameters, and adding that to context to the actual LLM call. So I thought they would have been the same, personally. If anything, I thought it would be slower, actually, because it's having to make a network request, get a response, and then give it back. So if anything, I thought it would have been slower. So that's interesting that it got faster.</A>

00:37:39 - Maksym Liamin
So I also found that JSON-RPC [tool:JSON-RPC] is generally faster, but why or how it gets faster — that's something I was trying to understand, but I didn't really find any good answer.

00:38:14 - Brandon Hancock
Also I saw your other question for best voice AI agents. Bastian, what was the name of the one you found? Because I love that thing.

00:38:47 - Brandon Hancock
So long story short, we were potentially going to work on something for a client — what they wanted in a nutshell was a basic voice agent that could be used for elderly patients to just talk. They wanted low latency, and they eventually wanted a phone call. What was nice is we were going to use OpenAI or some of these other tools for the website, but as Bastian found out, when we wanted to scale to actually setting up actual phone calls — getting the phone number registered, routing it from a phone call to our app — LiveKit [tool:LiveKit] had all of it right there for us. ▶ So next real-world voice AI application, which is general tool calling, really leaning towards this if there's a need for a phone.

00:39:59 - Maksym Liamin
<Q>For you and Bastian — can you put in LiveKit an API token? So for example, if you select the models that you would like to use for your voice agent, is it possible to give your own token? Because the point — what I'm talking about in the latency thing — is that we have right now the setup, it's 11 Labs in Twilio [tool:Twilio]. It works, amazing, everything is great, but only in the morning and in the daytime. Once it gets to the peak hours in the evening, because 11 Labs right now doesn't allow you to put an API key yourself or an LLM in the conversational agent settings — I believe they're using models hosted in the US — so it takes, it starts getting slower and slower because of demand and also the time it goes from Mexico to the US and back. So I was trying to find some sort of provider that allows me to insert my own keys that I can host in Azure or wherever, to have them hosted in Mexico so that it's closer.</Q>

00:41:17 - Brandon Hancock
<A>From what it looks like, yeah, 100% — you could use OpenAI real-time [tool:OpenAI real-time]. So at that point, you could use Azure [tool:Azure], and at that point, yeah, you could host it wherever you'd like. So if you wanted it closer to you and your target audience. I'll drop this in chat, just so you can see it. If you go down just a little bit more, you can actually see under partners, partner spotlights — they actually have one directly for Azure, and they have everything you're wanting.</A>

00:41:43 - Bastian Venegas
<A>So are you trying to have an API key to connect to some other service, or trying to use a specific LLM key for the provider of the LLM? So this — it is basically a wrapper around the real-time interaction, but you can use the model hosted anywhere. And also that service that they provide in terms of the connections — you can deploy that anywhere that can have a Docker image, because all of this is open source. You actually do not need to — I mean, there's a server in Brazil that might be close enough for you. I used that one, it was really fast, even considering that it had to jump to the United States. So I think you could start by doing that, just for testing purposes, but you can deploy it anywhere, and your LLMs can be anywhere as well.</A>

00:43:11 - Maksym Liamin
Okay, and so it needs a container, right? Do you think it can be deployed in a Cloudflare worker?

00:43:21 - Bastian Venegas
I don't think so.

00:43:23 - Brandon Hancock
▶ It does look like you potentially could deploy it locally, so if you could deploy it locally, you could do it somewhere else. But the pricing wasn't wild, and I sent you that link in chat. If you go down just a little bit more, you can actually see under partners, partner spotlights — they actually have one directly for Azure, and they have everything you're wanting. So I think that's everything you need to actually build something that's not going to dip in throughput during peak hours.

---

<!--SEGMENT
topic: Cursor Rules, Iteration Strategy, and Unit Testing
speakers: Brandon Hancock, Neel More, Tom Welsh, Jake Maymar
keywords: Cursor rules, .cursor folder, rule files, Next.js, Python, Google ADK, unit testing, error prevention, iteration, AI-generated rules, task templates, code quality
summary: Neel More asks about Cursor rules files for Python and Google ADK projects. Brandon Hancock explains his workflow of building rules iteratively from real errors — every mistake becomes a new rule to prevent recurrence — and demonstrates his .cursor folder structure. Tom Welsh shares that he maintains a Git repository of rules. Jake Maymar asks about unit testing templates, and Brandon Hancock advises building one well-documented example and letting AI generate subsequent tests.
-->

00:54:38 - Neel More
<Q>Yeah, the question is I'm struggling with the Cursor rules files. I know there is a .cursor directory, but there are a lot of Python categories also there. So as we are working on Python and Google ADK, is there any Cursor rules files which we can share in the group so that everyone can use the same thing?</Q>

00:55:02 - Brandon Hancock
<A>So I don't have any rules set up strictly right now for ADK or Python, but I can show you my workflow. So on your own, you can hopefully do the same. So in a project, you're going to have your .cursor folder. This is where you're going to have your rules. And this is where you're going to have your MCP server connections. So here's my cycle. What I do is I find one rule file that I like. So I will create something like this to where it provides context, it gives a rule, and shows some examples. So this is what a good rule, in my opinion, looks like. It's kind of like if I was to teach a new employee — what's the problem, give them context about what's happening, here's the rule, and then show good and bad. It's like how you would just train a normal human.</A>

00:56:19 - Brandon Hancock
▶ Then any time I run into an issue — like let's say Cursor goes off and doesn't put a specific Next.js page that's an asynchronous component in a Suspense — any time something goes wrong, what a lot of developers do is they just say fix it and then they move on. I don't do that. Every time there's a mistake, I add a rule to prevent it from happening next time. Because what's nice is eventually, as this keeps growing, I end up with a full repository of rules to make sure that I can just copy from this project over to the next. So that way I'm continually almost building an archive of how I like to build apps and how to do things properly. So I almost have like a training set that I can take from any project over to the next.

00:57:06 - Brandon Hancock
And it's like — I used to maybe fix one out of three lines from Cursor, or like every three messages something went wrong. And the more you do this, it goes from one out of three to one out of five files you have to fix. Then it's one out of 10, then one out of 20. Like it's insane once you set up a good repository of rules — you eventually get to the place where you're just cruising because it knows what to do and what not to do.

00:57:47 - Neel More
<Q>Just a quick question — have you written all these rules by yourself, or did you use ChatGPT or Claude to write these rules?</Q>

00:58:03 - Brandon Hancock
<A>So the way I like to think about it is all you need is one example of something good. You need to put brain power into it once — think through what makes for a good rule. And then going forward with these models, you just say, analyze my style and format for writing rules. Analyze the error. Make a new rule to make sure you never make that mistake again. And it'll do a 90% job. You might have to tweak one or two things. But we're trying to get as much leverage in not repeating ourselves ever again.</A>

00:58:41 - Tom Welsh
Yeah, I was just going to say the rules again are just iterations over iterations. And I keep a Git repository now of my rules that I pull down, teach my projects. And I like your part there where you're fixing the errors. Because yeah, I'm sick of seeing them coming up again and again.

00:59:33 - Jake Maymar
<Q>What about unit testing or just testing in general for Cursor? Do you have any kind of templates that you're like, run this test?</Q>

00:59:54 - Brandon Hancock
<A>So for what I'm working on right now, I've actually just wanted to get the thing working. So I have not added in all those unit tests. But the key takeaway is — one time, just put all your brain power into making a good unit test, explain why it's good, why you did it, and you can have AI help you write that initial document. But just the main thing is to get across the why you did what you did and why you liked it. And then what's nice is that's a good starting 80%, so then you're going to have it generate the next unit test, and you're going to go, oh, I didn't even think about that edge case. So the main thing I've worked on — this is iteration 50 — is this task template document, and I have it say exactly how to make code changes. Just anytime something doesn't go right, tell AI what it should do differently next time and put it somewhere so you can access it later. That's the key lesson.</A>

---

<!--SEGMENT
topic: Asset Management App Demo (Tom Welsh)
speakers: Tom Welsh, Brandon Hancock, Al Cole
keywords: Next.js, Vercel, Neon, Supabase, Drizzle ORM, Cursor, barcode scanner, asset management, database indexing, WorkOS, caching, Browserless, Puppeteer, Notion, Obsidian
summary: Tom Welsh demonstrates a fully Cursor-built asset management application deployed on Vercel with Next.js and Neon/Supabase, featuring 12,000 synthetic users, 71,000 assets, barcode scanning, PDF export via Browserless, and color-coded asset tracking. Brandon Hancock provides a database indexing explainer and recommends WorkOS for enterprise authentication. Tom explains his document-driven prompting workflow using Notion and Obsidian.
-->

01:02:17 - Brandon Hancock
All right, Tom, you're up first, man.

01:02:28 - Tom Welsh
I'm still awake, and it's midnight.

01:02:34 - Tom Welsh
Yeah, so I've been working away at this — I've got an asset management system. So I got a bit passive-aggressive, and it's called One Space, so I've kind of written Two Space to start. Let me share my screen.

01:03:04 - Tom Welsh
So this is literally completely Cursor [tool:Cursor] — not a single line of code written by myself. I use a lot of prompting from — so basically I write documents inside Notion [tool:Notion] or I'll use Obsidian [tool:Obsidian]. So I set it all up. This is Next.js [tool:Next.js] and it's hosted on Vercel [tool:Vercel]. So I've got my little assets that are running here. I've got 12,000 users, 71,000 assets kicking around. And I can just go — I can click into a user and go, here's a user. She's in the marketing department. So I've set up my seed data type stuff that does this — if you're in marketing, you get two monitors, you get a certain machine, you get this, that, and the other.

01:04:35 - Tom Welsh
I've got an export running, which I just did a bit earlier. That's using Browserless.io [tool:Browserless.io]. Yeah, because I was using Puppeteer [tool:Puppeteer], but there was a lot of problems using Puppeteer on Vercel, because you can't do server functions — you have to go use Express or something to actually go and call stuff. Then I've got my barcode scanner — I can look up an asset, and basically it's a quick diagnostic test to make sure your scanners are working.

01:05:49 - Tom Welsh
This is my passive-aggressive — I hate your crap you're doing, and this is what it should be doing. Because everyone's getting blamed for deleting stuff. Well, if you delete an asset, it goes to the archive table, along with all the history. What the head of IT does is he just deletes everything.

01:06:12 - Brandon Hancock
All right, so a few questions for you. TechStack — Next.js, deployed to Vercel, Neon, right? No, Supabase?

01:06:23 - Tom Welsh
No, I jumped between — I started with Supabase [tool:Supabase], then I went wrong, so I just drizzled it across to Neon [tool:Neon]. And so I've got the back end, but I've now bought subscriptions to both, so I'll probably swap back at some stage when I want to go and start doing the authentication. I know I can do it on Neon, but I think Supabase has got a better stack. And what Bastian was saying about Neon being bought by Databricks, I might actually have a sway on it as well.

01:06:51 - Brandon Hancock
▶ The few pieces I think will be really helpful — so if you are thinking about making this more enterprise, one option is, because you're already out of Supabase, is to use WorkOS [tool:WorkOS] for authentication.

01:07:22 - Tom Welsh
So I've already got things like depreciation — straight line or balance — which will work on the assets. And I'm going to stick it in here, basically, as an option. If you've got WorkOS to suck in your AD or your directory services somehow. I've got caching because I was sick of running a query and pooling stuff every time. Because assets don't change that often. So we may as well cache.

01:07:39 - Brandon Hancock
Did you end up adding indexing?

01:07:42 - Tom Welsh
Yeah. I did. So I didn't notice a massive difference myself. But then I didn't run timing tests as such. And I haven't re-indexed since I've jumped back to Neon and I've redone my schema several times. So it needs another index.

01:08:01 - Brandon Hancock
▶ So just real quick, quick full-stack tip. So when you are building stuff, when you do stuff locally and it's just you as a user — let's say you're trying to look up an asset. Well, you're going to try and look up that asset by an ID. So what's actually happening usually is it's an O(N) search — a linear time search. So the database literally usually starts at spot one and then works its way down. What indexing does is it actually indexes your database. So it basically makes it to where instead of being linear time, it does some fanciness behind the scenes — a tree structure — to where it is O(log N). So it's like, instead of 60,000 queries, it gets there in maybe 50 queries. So when you're building big-boy applications and you have lots of users, people are going to be like, it's so slow. Indexing is 99% of the time what's going wrong. If you're using a tool like Supabase, PlanetScale [tool:PlanetScale], or some of these database providers, they'll actually have a field for you showing long queries, which is nice because it's kind of like a red flag waving — hey, something's wrong here.

01:10:03 - Al Cole
So you said you were prompting most of that app — was it through Cursor?

01:10:10 - Tom Welsh
<A>I did it through Cursor. Yeah. But I'm literally — I write my consultant docs, I write my project initiation documents, I write it all out, and I feed it to Cursor so it's got context. I've got MD docs from Brandon's previous thing about the Cloud Crash Course, so I've got a master plan and a build on that, and then for everything I want — every feature I want to do — I write a document of how I want it, and then I feed that to it so it knows what's going on.</A>

---

<!--SEGMENT
topic: Lovable and CMS for Consulting Website
speakers: Al Cole, Ty Wells, Brandon Hancock
keywords: Lovable, CMS, content management system, blog, Vercel, n8n, static site, markdown, Supabase, website launch, consulting practice
summary: Al Cole asks whether Lovable is a good platform for building and maintaining a consulting website with periodic blog updates. Ty Wells recommends Lovable with an n8n workflow for dynamic content. Brandon Hancock explains the CMS pattern — keeping the Lovable frontend separate from a headless CMS for blog content — so updates don't require redeployment, and warns against using Lovable once database state management becomes complex.
-->

00:30:51 - Al Cole
So I am ramping up the consulting practice. It is time to start building out a website. And my question for the team is — Lovable [tool:Lovable], a good platform to host a website that will periodically get updated with mostly probably blog-oriented type articles? Vexil's another one, right? And I wasn't sure if the team had a preference.

00:31:20 - Ty Wells
Lovable is my choice. Lovable is what I would do if it's a website, because it's static, and then maybe throw — if you want to bring in some dynamic content — throw an n8n [tool:n8n] workflow behind it to bring in your blogs or whatever else you want to bring in. But it'll build out a fairly decent, really fast — if it's just for the website you're landing in context.

00:32:08 - Brandon Hancock
I love Lovable, especially for what you're trying to do — where it's not code heavy. The second something is where I have to start managing state, I'm making actions to a database — I hop out of Lovable as soon as I have that prototype stood up. I hop out just because it's not designed for that yet. But the thing I was going to show you is there's a thing — what you would actually be looking for is a blog post CMS, so content management system. What's super nice is you could actually spin Lovable up, build it out perfectly, and say, great, I'm trying to use this CMS tool to actually — this is where all the blog posts are at. What's so nice about this is you could just have the client or you log into the CMS, save the blog post, and it will automatically appear in the Lovable app. So they're not even ever in Lovable — they're just in a CMS tool.

00:33:19 - Brandon Hancock
▶ So it's mostly just for publishers. You'd have a static website, and then you would just point to your own blog. But yeah, there are plenty of them. Another way is you have a database to where you would allow them to just type in markdown, then you would present the markdown — but then you're starting to get back into database land, and that's when I instantly try to get out of Lovable. So this would be — you're all Lovable for frontend, and then CMS for your actual blogs, and they would just show up in your website.

---

<!--SEGMENT
topic: FastAPI and ADK Frontend Integration, LangGraph vs ADK
speakers: Marc Juretus, Brandon Hancock, Juan Torres, Bastian Venegas
keywords: Google ADK, FastAPI, Next.js, React, LangGraph, LangSmith, agent evaluation, Crew AI, deployment, Google Cloud Run, planning mode, multi-step agents, ReAct, CICD
summary: Marc Juretus asks about a promised video showing a Next.js frontend consuming a FastAPI backend calling ADK agents. Brandon Hancock previews new ADK features including a full-stack React + FastAPI template and planning/multi-step agent mode. He compares ADK's simplicity to LangGraph's enterprise control complexity, and discusses agent evaluation gaps in ADK versus LangSmith's feedback loop capabilities. Juan Torres mentions successfully implementing LangSmith tracing with Crew AI.
-->

01:35:09 - Marc Juretus
I know you had mentioned you said you owe this video — you said about possibly having a Next.js front-end consuming a FastAPI [tool:FastAPI] API that was calling ADK agents. Now, I did take the one you showed me, I downloaded it, and I have it running — it does a chat where you can either do the audio or the text, and it will actually interface with the client. I actually got that running. It just seemed like a lot of extra code. I would be curious to see if you do put that out, what your approach is, and how you would strip it down. Because all I'm basically looking to do is — can I make a chat that I can call the endpoint in from ADK, and just call a FastAPI, pass that, and return it back.

01:36:00 - Brandon Hancock
So I was going to — there are two videos I need to do on ADK. So ADK just released some new features. They've made some changes now to where you can actually get a complete React [tool:React] front end with a FastAPI back end. So I was going to dive deeper because they just dropped this — it wasn't even one week ago at this point. It was like four or five days ago. So I paused because I was waiting because of this. So I'm going to look into this more. You can kind of see in this little quick GIF of the actual — so this is the planning side of things. You can see full-stack React component, you make a request, goes to a deployed ADK instance, it's planning. So this is one thing that I haven't got to talk about much.

01:37:08 - Brandon Hancock
▶ ADK right now is single-step. So even when you're saying, hey, go do all these tool calls, what it does is it's like, cool, I need to make three tool calls in this order. So it calls tool one, two, three. It's not a Crew AI to where it's React — meaning reason and act. It just puts up a queue of actions and then just executes them all. Once it's made its mind up, that's all it does. It doesn't do iteration, iteration, iteration. But with planning it does. So I need to do a video on this.

01:38:21 - Marc Juretus
I got to admit, I love ADK and I did your deployment video where I went through soup to nuts and I did that deployment to Google Cloud [tool:Google Cloud]. I got to admit to you, Brandon, it's a lot of steps to deploy an application.

01:39:00 - Brandon Hancock
I 100% agree with what you're saying because it should just be like `adk deploy` — that's it. Like I should make the project and I click, I type deploy and that's it. They do have — from what I can see, they've made changes. So I think that is actually out of date at this point. It's more streamlined now. So you can see — yeah, for production-ready deployment with CI/CD, follow this guide. I haven't got to dig deep into it because he just on Friday tagged me. So I haven't got to dig too deep, but it looks like they've made a bunch of improvements to it.

01:40:01 - Brandon Hancock
Really cool, amazing course I just watched — we had a long drive down. Email agent course. I watched this on the way down. It is LangGraph [tool:LangGraph], but I just wanted to see from a conceptual standpoint — I just wanted to see what other frameworks are doing. And this was awesome, because I need to get smarter on agent evaluation. ▶ What's really cool that I thought they did good on is agent evaluation with LangSmith [tool:LangSmith]. The way most people build agents — you just like normally test LLMs. I give the LLM this request, I would expect it to do this tool call and give an output that is in this format. That is evals 101. But when it comes to multi-agent solutions or just agentic solutions, there's so many LLM calls happening left and right. And what I thought was really cool — if you watch one module, watch module three — all they do is just show how your deployed agents in LangSmith save everything to LangSmith, and then you can build up a repository of good and bad runs. So what's so nice is your data's right there. I'm really hoping ADK does something like that.

01:42:20 - Marc Juretus
<Q>So would you say you believe LangSmith and LangGraph are trying to catch up with this other cool stuff guys are doing? And you think they're going to come up and kind of level off with them? Or do you think they're going to just kind of use a Visual Basic — it works, but that's not what people are using now?</Q>

01:42:35 - Brandon Hancock
<A>I think so — specifically for enterprises — just because they have to have an insane level of control over it. Because they're deploying it to hundreds of thousands of users. They need to be able to monitor every little piece of what's going on. Like they have zero tolerance for mistakes at the cost of deployment cycles. So LangGraph gets control at the cost of complexity. That's why I like ADK — you get the power but the simplicity. So that's why I'm so bullish on ADK right now.</A>

01:43:30 - Juan Torres
I just wanted to say that I actually was able to implement LangSmith for Crew AI [tool:Crew AI] in order to assess context windows. So I don't know if there's a possibility to implement LangSmith assessment mechanisms for ADK.

01:45:19 - Brandon Hancock
▶ I think it's super easy to add in tracing. It's just I don't know if they add in tracing for ADK. And Bastian is right — you can basically place the LangSmith evaluation based on wrapping the LLM calls. So I think it could be agnostic.

---

<!--SEGMENT
topic: Claude Code Pricing, Cursor Billing, and Model Preferences
speakers: Andrew Nanton, Brandon Hancock, Tom Welsh, Jake Maymar, Bastian Venegas
keywords: Claude Max, Claude 4 Opus, Claude Sonnet 4, Cursor pricing, usage-based pricing, context window, Gemini 2.5 Pro, Anthropic API, Claude Code, VS Code, fast requests, billing
summary: Andrew Nanton shares his experience paying $200 for Claude Max and finding it more cost-effective than API usage for heavy coding sessions, noting Claude Code provides better context window utilization than Claude in Cursor. The group discusses Cursor's opaque billing model, usage-based pricing toggle, and the tradeoffs between Claude Sonnet 4 and Gemini 2.5 Pro. Tom Welsh reveals he keeps usage-based pricing off, which may explain why he doesn't get charged extra.
-->

01:21:37 - Andrew Nanton
Hey. All right. Well, this week I'll drop into the chat. There's some stuff I've been working on and I'm hoping that it may potentially be useful to some other people. Still under heavy development. Expect breaking changes. But briefly, it's a FastAPI application that does a couple of things that are really helpful to me.

01:22:00 - Andrew Nanton
So the first one is that Azure Document Intelligence [tool:Azure Document Intelligence] will generate JSON with PDFs that you send it, which is useful, but it has a couple of limitations. The first is it'll only do 2,000 pages, and the second is that things can sort of get lost in the shuffle — it's hard to trace things back to where they originally came from. So this will assemble an arbitrarily large JSON for documents that are thousands of pages long, and give you a unique element ID for each of them. So if you do stuff, you can trace it back. And that's important because it gives you a whole bunch of stuff that you may not want. And so there's also a filter endpoint to say, I don't want all the bounding boxes, I don't want all that other stuff — because that's going to fill up your context window really fast if you're trying to work with large documents. So you can filter all that stuff out, send it to an LLM, but you still have that later — you can use those unique IDs to go back and trace and maybe re-enrich whatever it is that you've done.

01:17:39 - Andrew Nanton
It also — and this part is being worked on fairly heavily — has an anonymization endpoint as well where you can send JSON or Markdown and get something anonymized. It mostly uses a BERT-based transformer [tool:BERT] and Presidio [tool:Presidio], but it also does some date shifting with some fuzzing of dates — to kind of keep a consistent timeline rather than just Presidio's default of replacing dates with random dates. So yeah, if you're messing around with documents that are large and that you want to keep private, hopefully one or several of these functions will be helpful.

01:21:57 - Andrew Nanton
Yeah, so I had been doing a fair amount of stuff using — well, one, paying for Cursor after I blew through the monthly allowance, and two, using my Anthropic API key, which I did for like half an hour until I said, oh no, this is a terrible idea. I think I went through — one afternoon, I was using the Cursor stuff, and I wasn't really paying attention to how much I was doing it. And I blew through like $80 in like a few hours. And I was like, okay, I am going to just try — what happens if I buy the $200 Claude Max [tool:Claude Max] account? Like, how much do I get out of that? And so I was just hammering away at it. And after, I think I hit the limit where it was like, you've used half of what you're allowed to use — and it was after one day.

01:23:13 - Andrew Nanton
But then what happens is they actually reset it every five hours and you get — they're using Claude 4 Opus [tool:Claude 4 Opus] and then it will step down after you've used half of your allowed stuff. It'll step down to Sonnet. But you get like 50 of these sessions a month. After getting that initial warning the first time, I've never hit it again. And I've just gone nuts on it. If I were paying through an API or through Cursor, there's no doubt in my mind it would be substantially more than the $200.

01:24:00 - Andrew Nanton
So I'm using Claude Code [tool:Claude Code] from inside Cursor using the IDE connection. But I will say that I don't really know how much I need Cursor with the way that I've been using Claude Code. It's so comprehensive. I think I could use just regular VS Code [tool:VS Code] or really any kind of code editor and run it inside there. I mean, it's so robust that I think I would probably be just fine with something that's just a more basic kind of editor. But yeah, I've been pretty happy with the results and I definitely feel like I see a difference between what I get with Claude Code versus what I get choosing Claude in Cursor. I think it seems like the context window — I can use more of it somehow.

01:27:16 - Brandon Hancock
Does anyone fully understand the Cursor plan limits? Because I know I get charged, but I could not tell you why I get charged. Because I'm paying the 20 bucks a month, I'm using Claude Sonnet [tool:Claude Sonnet], and then sometimes I get charged. Other times I don't.

01:32:11 - Tom Welsh
Are you using usage-based pricing? Under settings.

01:32:14 - Brandon Hancock
Yeah.

01:32:18 - Tom Welsh
Mine is off.

01:32:21 - Brandon Hancock
Okay.

01:32:23 - Jake Maymar
Yeah, turn it off and see if it makes any difference.

01:32:30 - Tom Welsh
Yeah, because I've got it on, I'm using it all the time.

01:32:32 - Brandon Hancock
It's basically just — get requests beyond your plan's included quota. That's what it says. Tom, thanks for letting me know. I didn't know that was a thing.

01:29:37 - Jake Maymar
So, I've been using Gemini 2.5 Pro [tool:Gemini 2.5 Pro], and it's free. And I don't know why. I'm not changing anything. But I haven't been charged yet. I keep looking to see if I'm charged, but I haven't been charged yet. I'm just hammering it. I have multiple Cursors open running. And it's not charging me.

01:31:05 - Jake Maymar
I've been using Gemini 2.5 Pro more than Sonnet 4.

01:31:08 - Brandon Hancock
I have hopped back and forth between both of them. Literally, if one gets stuck, I hop to the other until it gets stuck, and then I hop back. So depending on the day, whatever got stuck, I rotate. I'm just constantly swapping between the two. I have, for the past two to three days, been using Claude 4 Sonnet, pretty much without getting stuck once. So that's why I'm using that one. And it's been crushing it.

---

<!--SEGMENT
topic: AI Consulting Go-to-Market Strategy
speakers: Al Cole, Brandon Hancock, Paul Miller, Tom Welsh, Jake Maymar
keywords: AI consulting, enterprise sales, go-to-market, LinkedIn, YouTube, lead magnets, flywheel, maturity model, center of excellence, agentic mesh, AWS Summit, personal brand, case studies
summary: Al Cole presents a consulting maturity framework for guiding enterprise clients through AI adoption stages and asks for feedback on go-to-market strategy. Brandon Hancock recommends a content flywheel approach — implement for friendly clients, document the solution, give it away as a lead magnet, and let organic opportunities follow. Paul Miller validates the market opportunity from a SaaS perspective. Tom Welsh emphasizes the importance of C-suite buy-in for culture change. Brandon Hancock shares his LinkedIn lead magnet strategy as a live example.
-->

01:49:32 - Al Cole
So, I am ramping a consulting practice, gentlemen. So, I've been working on getting legal and really a strategy for engaging clients. And I have one slide I wanted to run by the team to get your feedback in terms of how I'm thinking about engaging in the enterprise. Does this team think about consulting and also long-term relationships with your customers? I know you're definitely solution-oriented, but I don't know if you think in terms of just broad consulting within an enterprise organization. And what I'm trying to do is put together kind of a way of thinking about how to mature an organization through the adoption of more AI-related tooling.

01:50:52 - Brandon Hancock
Paul, if you want to go first, I'd love to go second.

01:51:00 - Paul Miller
Yeah, that's interesting. I think we — if you remember, I have a SaaS business. We've got a lot of enterprise and B2B kind of corporate customers. And there is such a gap for enterprise knowledge as to what they need to do with the approach on this kind of thing. So you're right to recognize the market. I think one of the things — if you can kind of go in there and say, what we're finding is giving that independent view, because we're seeing very large ERP companies and CRM companies like Salesforce, go and say, the answer for your strategy around AI is just to give us lots of money and use our products. And if you can achieve that balance and that perspective, there is a lot of value with the consulting work around that.

01:55:00 - Tom Welsh
Yeah, a couple of things. So I'm definitely aligned with what you're saying. These big ERP companies kind of go, oh yeah, we've got this AI, which is really just another function they've got in there that's wrapped up in marketing and hype. The thing with this is it's getting at the C-suite and getting the buy-in from the higher-ups, because if you're getting low-level, it's just hiding. That's where I used to play, so I'm okay working my way up that leadership chain.

01:55:41 - Al Cole
I will do better if I go and organically make a few teams successful, because it's easier to have that conversation up top, right? But the idea here is, when I get that land opportunity, is to explain that with the relationship, we're able to guide them over successive quarters on further and further adoption of the tech stacks.

01:57:04 - Brandon Hancock
So I want to get super concrete on this and also going from personal experience. One of the biggest things that I've worried about when it comes to AI consulting is — when a lot of people come in, they're like, cool, we just hired consultants. The consultant comes in and they go, you guys need to use AI. You need to use ChatGPT. And they don't have an actual playbook to implement. They're just very vague. ▶ So even like, you know, here's a template — think of my YouTube channel as an example. You're constantly giving away templates. Because that's invaluable. But the cool part is there's thousands of these that you could do. So even if you give away 20 of them for free, there's still 600 more that you could build that are of value. So that's thing one — just actually being very concrete with your implementation. Here's the exact problem this solves. Here's a template that does it for you. Do you want more? Hire me.

01:59:27 - Brandon Hancock
<Q>What is your kind of go-to-market approach? Are you thinking cold email? LinkedIn? You already have some friends in the space?</Q>

01:59:38 - Al Cole
<A>So a couple of ways I'm thinking of attacking this. One, I have worked with large enterprise sales teams for years, have great relationships with them. So letting them know as an independent, I could help out with projects that they might need that expertise. Two, it's the groundwork of the meetups, the conferences, the one-on-ones at different organizations. So Brandon, that's actually the thing I probably have the least comfort level with, because I'm used to a sales team bringing me who I need to talk to. But what I was going to do is leverage my network initially and then over time through meetups and everything else also build relationships. And my thinking was in the meetups, I am starting that giveaway and starting to help people understand the art of the possible.</A>

02:00:35 - Brandon Hancock
▶ So the way I like to think about it is funnels. Top of funnel is — do people know that I exist? When starting anything, the answer is no. So the biggest issue is actually just letting people know that you exist before even operations. So my favorite way to do this is — you have friends, let them be your dummies, case studies. And at the caveat of — you get to talk about it as much as possible. And here's what that would look like. You have a friend, business A, and you're working in a specific department. What that would look like is you are building stuff for your friend. Maybe setting up some sort of knowledge corpus. And then what that would involve is — you take an action in that business and you instantly turn around on LinkedIn or YouTube and describe the problem the business was facing, what you did to solve it, and when you're starting out, just give away the solution. So hey, here's the five-step template that they implemented to make query times researching internal knowledge 100 times faster. And then that's all you do — you implement, the second you implement something successfully, turn it around, give it away as a lead magnet, and you will be shocked just how fast that feedback loop opens up an insane amount of opportunities for you.

02:03:40 - Brandon Hancock
▶ And doing this — seriously, after you do three successful implementations for someone and you promote it on LinkedIn as a lead magnet and YouTube — organic opportunities will come towards you. Like it's just magic. It's a flywheel all in one because it's action. Action leads to marketing. Marketing leads to new opportunities, which then leads to more action. And that's the entire flywheel. But it does involve you being on LinkedIn and YouTube.

02:06:00 - Brandon Hancock
So a high level — the what is what you sell, get people excited, and then you give away the how as a lead magnet. So then people comment, I give them the master class. So the master class is my lead magnet because I know my target audience is developers. Developers want to build a personal brand on YouTube. So I already have the transformation outlined perfectly. ▶ So that's something you need to think about for your customers — what is the actual transformation they're trying to go through? And how do they make that transformation? That entire from A to Z — that is you. And that's where there's a thousand lead magnets in that journey that you should be giving away to grow your audience.

---

<!--SEGMENT
topic: Secure AI Infrastructure and Private LLM Deployment
speakers: Juan Torres, Brandon Hancock, Paul Miller, Tom Welsh, Bastian Venegas
keywords: Oculus Digital, NVIDIA GPUs, Mistral 7B, AWS Bedrock, Azure, private virtual cloud, egress traffic, NLP, vendor extraction, agentic system, SageMaker, EC2, DeepSeek, model agnostic
summary: Juan Torres describes a client project requiring secure, private AI infrastructure using Oculus Digital GPU servers to run an NLP agentic system for vendor name extraction, with a 70% accuracy proof of concept approved. Brandon Hancock and Paul Miller advise on the tradeoffs between Oculus, AWS Bedrock, and Azure for private LLM deployment, emphasizing the importance of understanding future model requirements before committing to infrastructure, and the single-point-of-failure risk of any single provider.
-->

02:08:33 - Juan Torres
I just am recovering from an absolute whooping last week. I had a lot of work to do, had a presentation. And this week, I'm just going to be working with my client in terms of just trying to deliver AI through a secure method so I can use an API LLM, just because it's private information and it needs to be protected. So what I think we're going to try to do is use Oculus Digital App [tool:Oculus Digital], which is a data center service that has like 800 NVIDIA GPU cards. And so the thing that I have to do is figure out what is the model that I'm going to be using specifically for the tasks of an agentic system that has to resolve NLP problems — which is essentially extracting vendor name and transposing the vendor name from a description column to a name column. And the proof of concept, the first product was finalized with a 70% accuracy, which is good. And I haven't developed the accuracy rate just because I just wanted my client to see the proof of concept. He seems to be happy. So now it's the task of helping him create a delivery system that is based on a secure AI infrastructure. So I'm thinking — I don't know if people have suggestions — but since we're handling an 800 GPU card with probably 40 gigabytes, I think maybe Mistral 7B [tool:Mistral 7B] will be a good model in order to resolve NLP problems.

02:10:40 - Brandon Hancock
<A>So real fast — major suggestion first is to talk to Maxim because I know you said you couldn't do API calls, data was super sensitive. So Maxim by far has the most experience at deploying basically containerized applications inside of Azure [tool:Azure], where they're all within a private virtual cloud, so there's no egress traffic. The only thing that is happening is there is access to all the OpenAI models, which are — if you're working with most companies, that's what they want. It's just like, I just want AI. They hear, oh, ChatGPT — cool. So if that's all you have to have is access to OpenAI models, there cannot be any egress traffic, everything needs to be on a virtual private cloud — Azure has been seeming to become one of the more enterprise platforms right now. Anytime I get client calls, usually most people are using Azure.</A>

02:12:08 - Brandon Hancock
▶ And I would just look at requirements, because if OpenAI is all they need, cool, I would go with that. If they need to be model agnostic, I don't know — that's where it gets a little bit more tricky. And if you're having to do open-source stuff, maybe AWS — Paul would probably share a little bit more on Bedrock. But I would actually just — this is the most important decision for this entire project. And literally, one sentence they add later is like, oh, I want to work with Gemini. Why? You're like, well, everything we just did — the infrastructure as code, everything's deployed — it's all gone because of one simple phrase that they need later on. So it is usually when I'm working with a client at this point — I'm like, cool, we're very excited on MVP. What I like to do next is I like to brainstorm three months, six months, 12 months out of where you think this could go. Because I just need to know what you're even thinking about.

02:16:20 - Brandon Hancock
▶ For Bedrock [tool:AWS Bedrock], you can access Claude — there's no egress. Google, you can securely access Gemini — no egress.

02:16:47 - Paul Miller
On AWS, you can even do DeepSeek [tool:DeepSeek]. They've got it all focused. Even Amazon can't see what you're querying of DeepSeek. So if you're going that Amazon path, as long as you don't need OpenAI access, the base models are all accessible, and Amazon's own models are pretty good as well. The Nova models and the Haiku ones and pretty much all of the Meta models — and if you wanted to sort of do the best of all type things, it's not a lot of extra code to be calling the models in a consistent way without being too locked down.

02:16:07 - Tom Welsh
I was going to say that also by sticking all the eggs on one bus, you literally have a single point of failure sitting there. You need to look at some way of — if that goes down, how does the business keep running?

---

<!--SEGMENT
topic: HIPAA-Compliant Infrastructure and GitHub Copilot Agent Mode
speakers: Jake Maymar, Brandon Hancock, Bastian Venegas, Chouinpa
keywords: HIPAA compliance, SOC 2, Palantir, Fathom, Fireflies, AWS, Cloudtamer, Next.js, GitHub Copilot, VS Code, Obsidian MCP, Gemini CLI, agent mode, Claude Sonnet 4, training pipeline
summary: Jake Maymar shares a HIPAA-compliant infrastructure platform (Cloudtamer/Kion) built on AWS as an alternative to expensive Palantir deployments, noting Fathom and Fireflies also offer HIPAA-compliant meeting note-taking. New member Chouinpa describes building an automated training material pipeline from GitHub Copilot release notes using VS Code agent mode with Claude Sonnet 4, an Obsidian MCP vault, and Gemini CLI — noting GitHub Copilot has significantly improved and is approaching Cursor-level capability.
-->

02:21:06 - Jake Maymar
<Q>Has anyone used — I'll put the link in the chat — this at all? I thought this was pretty interesting. So looking for HIPAA-compliant solutions that are easy to deploy — it's kind of interesting. Basically, it's kind of a front end to like an AWS or an Azure. It kind of sets up everything for you. And so you can basically be HIPAA-compliant or SOC 2 compliant.</Q>

02:22:10 - Brandon Hancock
<A>No, that's awesome. I've looked for stuff like this because there's been a few people that have reached out and they're like, we have to have HIPAA-compliant stuff. And the second that happens, I'm like, well, to be honest with you, unless you have tens of thousands of dollars, the answer is like no, just because it is an ordeal. So I think this is awesome because they're basically giving HIPAA-compliant infrastructure. I think it's at 500 bucks a month.</A>

02:23:03 - Jake Maymar
Yes, absolutely. So it's interesting — we're doing stuff with Palantir [tool:Palantir], and that is expensive, like insane expensive. So we're trying to figure out a solution for the client. They're on Palantir. And so we're trying to figure out a solution that's a little bit more affordable. Also, interestingly enough — Fireflies [tool:Fireflies] — I don't know if you guys are — you know, Fathom [tool:Fathom] is the one I'm using. Fireflies is HIPAA compliant, Fathom is HIPAA compliant. What's interesting is a lot of times clients want a note taker. Now I know Zoom is a note taker, but it's just kind of interesting.

02:23:55 - Jake Maymar
Well, you have to pay for it. That's the only thing — you got to pay for it. It's $700 a month if you want to do the HIPAA compliant. Fireflies is a little bit cheaper. The HIPAA stuff gets so expensive so quick. It's insane.

02:24:10 - Brandon Hancock
▶ Yeah, seriously, great find. Because that's honestly been the biggest thing — man, like I know how to code, but it is so much — the client won't ever see all the work you're doing because it is 80% of it at that point. I'm having to spin up this virtual private cloud, I have to adhere to certain logging standards, I have to get so many agreements — so much extra stuff. That's awesome that they have that.

02:43:22 - Chouinpa
Thank you. First time attending. Love the chat. Really interesting. I didn't come prepared with a project to present, but the biggest one I'm working on right now is I'm working as a trainer internally at an investment firm, specifically around AI and AI integration. And right now, I'm also the trainer to the dev team internally. But sadly, I cannot show them personally WindSurf [tool:WindSurf] and all of those nice things, because the politics defined that GitHub Copilot [tool:GitHub Copilot] in VS Code [tool:VS Code] is the tool they went with. But it's getting better on a month-by-month basis. So it's not yet to the level of the other tools, but it's slowly getting there.

02:44:17 - Chouinpa
The one thing I've tried and I'm working on right now is digesting the release notes into a pipeline to actually generate the training material. Because there's so many changes on a monthly basis, it's almost impossible to keep training up to date. So the goal is to have a complete pipeline to automate ingestion of the release notes and generate the training from it from a lot of prompts. And I actually took some of your ideas — actually copied some of the instruction from the task list that you've shown that will be shipped soon — and tweaked it to have, here's the template I want you to fill, here's what I want you to put in each of those sections, and having the prompt as mostly the workflow operation to actually fill that based on the ingested release notes.

02:45:24 - Brandon Hancock
<A>So cool thing — I think you would find helpful — at Crew AI, we actually ran into the same issue. Whenever Joao cut a new version, what it would do is — same thing you're talking about — we basically had one crew that could access Git, and we kicked it off with a changelog, and it also had access to all of our docs, which were all markdown. So it could analyze the new things, it could analyze the current state of the documents, and it would generate new examples, generate new sections, create new pages, and it just did it all on a new branch, so we at least had somewhere to start, and we weren't starting from zero. So Crew AI [tool:Crew AI] — awesome tool for just like straightforward, hey, this is a constant process we're going to be doing for the rest of time, as long as we're shipping new stuff.</A>

02:47:35 - Chouinpa
Agent mode with Claude Sonnet 4 [tool:Claude Sonnet 4] — pretty solid. I mean, it's missing all the functionality, obviously. I've tried to compensate with the instruction file, but it's getting there.

02:48:09 - Chouinpa
If you take agent mode in conjunction with a couple of cool MCP servers — I really love the one tying it to my Obsidian vault [tool:Obsidian]. Because it basically makes Obsidian another memory for whatever I do. So basically, I construct my Obsidian vault within VS Code using Copilot Agent.

02:48:43 - Chouinpa
And right now, I want to try to integrate Gemini CLI [tool:Gemini CLI] in the terminal of VS Code and manage the documentation with Copilot and the code writing with CLI to see if I can create documentation that is enough context to make CLI a little bit better.

02:49:22 - Brandon Hancock
▶ Yeah, because just real fast — going back to it — you might not even have to use Crew if you come up with a well enough context template to say, here's what you normally do, here's your inputs, here's your desired outputs, and here's some additional steps you need to be aware of as you go off and actually build it. You might even have to do Crew because you basically have a built-in agent right in your editor.

---

=== UNRESOLVED SPEAKERS ===
- alexrojas (appears as "alexrojas" in raw transcript — no canonical form confirmed from alias map)
- Alex (appears separately from "alexrojas" at ~02:05:00 onward, possibly same person driving; treated as distinct occurrence)
- Chouinpa (introduced as "Patrick" by Brandon Hancock at 02:43:16 but raw speaker label is "Chouinpa" — passed through unchanged)
- Zain Khan (appears as "Zain Khan" — not confirmed in alias map)
- Neel More (appears as "Neel More" — not confirmed in alias map)
- Nate Ginn (appears as "Nate Ginn" — not confirmed in alias map)
- Bastian Venegas (appears as "Bastian Venegas" — not confirmed in alias map; referenced as "Bastian/Bastion" by others)
- AbdulShakur Abdullah (appears as "AbdulShakur Abdullah" — not confirmed in alias map)
- Matias Coca (appears as "Matias Coca" — not confirmed in alias map; referenced as "Matthias" by Brandon)
- Maksym Liamin (appears as "Maksym Liamin" — not confirmed in alias map; referenced as "Maxim" by others)
- Jake Maymar (appears as "Jake Maymar" — not confirmed in alias map)
- Juan Torres (appears as "Juan Torres" — not confirmed in alias map; referenced as "Kwon" by Brandon at 02:08:30, likely a mispronunciation)
- Cyril I (appears as "Cyril I" — not confirmed in alias map)
- Paul Miller (appears as "Paul Miller" — not confirmed in alias map)
- Tom Welsh (appears as "Tom Welsh" — not confirmed in alias map)
- Al Cole (appears as "Al Cole" — not confirmed in alias map)
- Andrew Nanton (appears as "Andrew Nanton" — not confirmed in alias map)
- Marc Juretus (appears as "Marc Juretus" — not confirmed in alias map)