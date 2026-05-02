=== SESSION ===
date: Not explicitly stated (Tuesday, approximate April/May 2025 based on content references)
duration_estimate: ~105 minutes
main_themes: Google Agent Development Kit (ADK) deep-dive and comparison with other agent frameworks; job search and career advice for junior developers; chatbot/RAG architecture for small-scale use cases; WhatsApp conflict-resolution bot development; life-manual workbook-to-app conversion; AI-powered union research newsletter service; OpenAI model landscape (GPT-4.1, GPT-4.5, o4-mini); MCP (Model Context Protocol) evaluation; YouTube personal brand launch advice

---

<!--SEGMENT
topic: Session Open and Host Updates
speakers: Brandon Hancock, Paul Miller, Cyril I
keywords: Agent Development Kit, ADK, Firebase Studio, Google, GitHub stars, Pydantic, CrewAI, agent deployment, YouTube tutorials, AI frameworks
summary: Brandon Hancock opens the weekly community call, welcomes new attendees drawn in by recent YouTube releases, and shares a GitHub-stars chart showing ADK's explosive growth relative to Pydantic over eight months. He explains his bullish stance on ADK, citing its deployment-first design philosophy and upcoming GUI for agent management. The segment establishes the meeting format and sets the thematic tone around Google's ADK.
-->

00:04:31 - Brandon Hancock
What's up, gang? Hey, Brandon. Hello, hello. Let's see. Okay, we'll definitely give people a few more minutes to pop on today. Definitely seeing some new names — always exciting whenever new videos release on new topics, because it always brings in a bunch of cool new people working on cool new projects, so always...

00:05:00 - Brandon Hancock
Always excited to see new faces. All right, yeah, we'll give a few more seconds. Also, Paul, sick shirt, by the way. Cyril, same to you, man — that looks very comfy. What is that? Is it like a police — okay, that's very cool, dude. You can stay warm in that no matter where you're at. All right, well, we'll go ahead and get started. So, quick updates for you guys: if you haven't got a chance to see them yet, last week was a busy week in the world of YouTube. Firebase Studio [tool:Firebase Studio] and Agent Development Kit [tool:ADK] dropped — both of those. Super excited for the Agent Development Kit tutorial. Basically, what I'm doing for you guys is working backwards through the whole process, so I'm starting off with deployment, then I'm doing a crash course, covering ADK as a whole.

00:06:00 - Brandon Hancock
And there are layers to it, guys.

00:06:03 - Brandon Hancock
I have been in the weeds over the past four or five days trying to learn everything to break it down as simply as possible for you guys.

00:06:10 - Brandon Hancock
▶ I am hyper bullish on ADK.

00:06:13 - Brandon Hancock
Let me show you guys a quick chart that I thought was pretty interesting. One second and I'll flip it up for you guys.

00:06:31 - Brandon Hancock
What's wild is in a single week, ADK has almost replaced what Pydantic [tool:Pydantic] has done over the course of like eight or nine months, which is wild.

00:06:46 - Brandon Hancock
And this is just GitHub stars.

00:06:48 - Brandon Hancock
▶ But I think the reason they're doing it and outpacing other frameworks so fast is because it is built to be deployed. A lot of other frameworks — Pydantic was one — it's all open source, but then you go put it in a container, put it into a FastAPI application — all the work's on you. But what Google is doing is saying, "We'll do the whole process with you."

00:07:19 - Brandon Hancock
The only other thing that I think is pretty insightful to know about is ADK's agent engine, which is how you can deploy your agents. They haven't fully built out the UI yet, so the difficulty level right now — you do kind of have to be a bit more of a programmer to fully understand: "I run this script to deploy, I run this script to test."

00:07:43 - Brandon Hancock
▶ But soon, very, very soon, they're going to be releasing the website UI, which I'm so excited about — just click around and deploy an agent through a GUI. That's going to be insane.

00:07:55 - Brandon Hancock
So I am hyper bullish on what Google's doing. I have a lot more tutorials on it coming up very, very soon.

00:08:03 - Brandon Hancock
So those are updates for me. What I'm going to do, guys, is take a quick screenshot of what I see on my screen — this is the order we're going to go in. Just in case it's your first call, super excited to have you here. The way it usually works: we go round-robin based on that image I just sent out. We try to keep it roughly six to ten minutes so that everyone has time to talk. If there's something you're working on, you're stuck, or you have questions, bring it on. Or if you're working on something cool in the AI space that you'd like to share — either one is fantastic.

00:08:42 - Brandon Hancock
So, yeah, Cyril, you are first on the screen today. What's been going on, buddy?

---

<!--SEGMENT
topic: Cyril's Job Search and Offer Revocation
speakers: Cyril I, Brandon Hancock, Juan Torres, Michal Simko, Paul Miller
keywords: job offer revocation, HR, internship, FAANG, startup, Village Labs, Marvik, junior developer, remote work, networking
summary: Cyril recounts having a job offer revoked by HR despite four senior managers advocating for him, and describes the company reopening the role within two weeks after the replacement candidate failed. The group discusses strategies for breaking into FAANG companies, with consensus forming around the value of startup experience over big-tech internships for learning breadth, and the importance of referrals for large-company entry.
-->

00:08:47 - Cyril I
Actually, quite a few things. So, yeah, starting off with that — I did have a job offer, and it has been revoked from me, because I did lie when I applied about being a graduate. They did revoke the offer from me.

00:09:03 - Cyril I
It's quite funny because the offer was revoked and there were four senior managers and programmers who spoke with management to keep me, because they interviewed me and they knew my potential, my intellectual ability, etc. They passed it to HR, who couldn't care less — not really interested in the company or employees — just "no is no."

00:09:38 - Cyril I
And the funny thing I saw after is, two weeks later, I see a job opening for this exact role. Which means that after they rejected me, they went to the second-best person, took him on, he lasted one week, and they needed to open the job again — which just shows how ridiculous it is.

00:10:06 - Brandon Hancock
Wasting so much time on this. This is wild. It's money as well.

00:10:09 - Cyril I
The whole process — five interviews, one month — rather than just saying yes, they decide to say no, go for someone else, and now they've wasted money and time.

00:10:26 - Cyril I
So, yeah, after that, I didn't really stop. I'm still applying to jobs. I was able to land a summer internship with a local company here for software. The owner told me that after the internship, if I'm successful, I'll be able to work for them full-time or part-time.

00:10:53 - Cyril I
<Q>And in the meantime, there's a side project I want to do — a chatbot where you can put a company's FAQ policy inside it, and it should output information in regards to that FAQ. I actually have a question about it. What are chatbots usually based on? What LLMs are usually used? And how would you approach writing a chatbot?</Q>

00:11:22 - Brandon Hancock
<Q>Okay, so real quick — just to make sure I fully understand, you're focused on entering a company's policy?</Q>

00:11:33 - Cyril I
<A>Yeah, it's like a chatbot, like a support bot on a website. You press it, input a query — like if it's a shopping website, you input "how long is delivery?" — and the chatbot with RAG would have the company FAQ: what's delivery time, what's delivery price, etc. It gives you an output about the company.</A>

00:11:54 - Brandon Hancock
<A>Okay, so what's cool for that is you actually don't need RAG at all, because a company's entire policy could fit within about 30,000 tokens. So it's way under the limit of all these models. You actually don't even need to technically do an agent. You really could just spin up a regular — you could use Next.js AI SDK [tool:Next.js AI SDK], or Vercel AI SDK [tool:Vercel AI SDK], and just put in a custom prompt. Here's the entire resource policy of a company, and allow them to ask questions. You don't even need to do agents for that. So you could actually keep it as simple as possible. All you'd need to do is keep up with the message history for each session — user said this, assistant said this, back and forth.</A>

00:12:47 - Brandon Hancock
▶ Let me pull up my screen so you can see what I'm talking about. Yeah, basically it's the AI toolkit for TypeScript. On your deployed Next.js applications, if you're building a website for them, this approach would be pretty nice.

00:13:30 - Brandon Hancock
▶ GPT-4.5 is the most conversational at this point. Your prompt would be very long — like, here's the entire policy of the company, your job is to first understand who the user is, what their question is, then refer them to the proper policy and respond succinctly. You could also bring in tool calls too. ▶ I'll drop a link in the chat so you can play around with it, but yeah, that would be the best way to get started. [link:Vercel AI SDK documentation]

00:14:00 - Cyril I
<Q>Thanks, that's really helpful. Now, second thing — as I'm looking through companies and as I know how to pass interviews now, I want to try to get an internship at one of the FAANG companies — Facebook, Amazon, Apple, Netflix, and Google. I'm wondering whether anyone has advice on how to pass the CV screening and actually have a chance to get in. Most things I see on the internet are people who get referred there, or people who go to Oxford, Cambridge, or MIT — just fully exceptional students. I do have big projects on my CV, but I don't think I passed the screening. I'd be interested if anyone has advice on how to potentially pass screening and get an internship at one of those companies.</Q>

00:15:22 - Brandon Hancock
<A>Yeah, I don't know — dude, if I knew, I would tell you. Because the only people I know who have got in have known people. Every single one of them had a friend. Out of every single person I know that's at one of those bigger companies — from Microsoft to Google — they know somebody. So all the big tech companies with the ridiculous bonuses — it is a buyer's market, meaning they pick who they want, because they're in no rush. The second they open a job role, they probably get thousands of applications.</A>

00:16:14 - Brandon Hancock
▶ With that said, in your case, I would also look at startups as another option. The amount you're going to learn at Apple versus a startup — I think at Apple, yes, it would be awesome on the résumé, but you might barely touch the stack. As an intern, you might ship a color change on a button. But at a startup, if you want to focus on learning, you're going to get to touch everything.

00:17:06 - Juan Torres
<A>Yeah, I have a friend from UCLA — she works at Google as a back-end developer, but she actually started at a startup. She started as a developer in a startup, and then from there she applied to Google in Poland. She had to move to Poland to work there. And to be fair, she's one of the most intelligent people I know. But she started from a very humble background, just working at a startup for maybe a year or two, and then transitioned to Google. But I agree with Brandon — startup work is going to help you learn a lot. Now that I talk to her, she does seem a little unsatisfied because her work is so specialized — developing tools for developers, which is very niche. So in that way, she might be left behind in a lot of AI development because she doesn't have to do any of that.</A>

00:18:45 - Brandon Hancock
▶ Yeah, my vote — AI startup, however you can do it. The amount of contacts you'll meet, everything you'll get to touch, the people you get to meet who will then go on to do more things and recognize how awesome you are. This is just the first one — you're going to be doing plenty more.

00:20:02 - Paul Miller
▶ Things are a bit different from an internship perspective in the UK versus the USA. In the US, an internship often means unpaid, while in the UK you have to be paid. Another path I've seen: if you're really keen to get into the big players — the Facebooks, the Apples — look at who their biggest customers are that do case studies, and get a job with them. Get an IT dev job with one of the biggest case-study customers of Apple or Google, because then that puts you in a really powerful position to go back to Apple or Google and say, "I'm experienced working with your code with one of your biggest customers." That's really attractive from a software perspective, because not only do you get the software, but you get the problem the software is trying to solve with their most important customers.

00:21:11 - Michal Simko
<A>I did ask some friends who have startups in San Francisco, and all of them want junior devs who wouldn't work remotely — they want people to move to the US. So there is that constraint. But I do agree with what Brandon was saying. There are some cool startups, like Village Labs [tool:Village Labs], that are at the forefront of what's happening in the AI space. I'll also follow up on the Marvik guys because I think they were a bit more open to remote work.</A>

---

<!--SEGMENT
topic: Google ADK Deep Dive vs. Other Frameworks
speakers: Brandon Hancock, Paul Miller, Juan Torres, Bastian Venegas
keywords: ADK, Agent Development Kit, CrewAI, Pydantic, LangGraph, agent engine, deployment, state management, Vertex Search, RAG, Google Cloud Platform, flows, multi-agent
summary: Paul Miller asks Brandon to make the case for ADK over existing frameworks. Brandon provides a structured comparison: CrewAI excels at ease of use and flows; LangGraph supports code-step execution; Pydantic lacks deployment tooling. ADK's advantages are cost-effective serverless deployment (~11 cents/hour), built-in Google tools, native RAG via Vertex Search, stateful multi-agent workflows, and session persistence — all in one integrated platform.
-->

00:24:14 - Paul Miller
<Q>Brandon, I had a question for you. A lot of people are clicking positively on this Google ADK environment or dev kit. You've done CrewAI [tool:CrewAI], you've done a lot of the agentic stuff. Why is it better? Give an overview — do the sell job on why we should get into it and invest in it.</Q>

00:24:48 - Brandon Hancock
<A>So I'll give perspectives for both. I still think CrewAI is the easiest to get started, because it's really: I create, boom, you have a project, and then you just update — test one, test two, test three — and you give instructions to agents and tasks. That is a crew. It is left to right. You save it to your GitHub repository, you go over to CrewAI Enterprise, and then it just deploys. It is very easy. Now, it's $50 a month for the enterprise plan. So you're paying for ease. Also, CrewAI has a feature that ADK doesn't, which is flows. Flows are basically where you're interchanging between agents and code, agents and code. So that just does not exist in ADK. Those are two huge bonuses for CrewAI.</A>

00:25:50 - Brandon Hancock
<A>Reasons why I like ADK right now are cost. I'm more cost-sensitive now that I'm an entrepreneur. The deployment is insanely cheap — it's like 11 cents per hour. It might go up to 20 cents, but it is very cost-effective to run your agents. It's like a Lambda function but for agents — when they're sitting there, no charge; when they're running, you're paying. For most other frameworks, it is not like that — you're paying per scenario, per pipeline, a constant fee. And with ADK, it was just a few tweaks of creating a deploy script, boom, you have agents deployed.</A>

00:27:00 - Brandon Hancock
Let me show you guys a link — GitHub ADK samples [link:https://github.com/google/adk-samples] — I just want to show you what's possible. So this is the ADK — they have a bunch of samples that walk you through real-world examples of agents. They rank them by ease of use and complexity — some are easy multi-agent solutions, some are advanced single-agent solutions. I want to show you the customer service one.

00:28:03 - Brandon Hancock
Going back to what Cyril was talking about earlier — almost wanting to make a RAG chatbot — what's crazy is how easy it is to create an agent powered by all these different tools. It is platform-agnostic, which I really like.

00:28:47 - Brandon Hancock
So what's cool is you can have a multi-phased travel planner inside ADK. You can have a root agent. And that's another thing that's awesome — you can share state. You can make stateful multi-agent workflows, meaning at any point you can say what phase you're in — the exploration phase, the planning phase, the booking phase — and depending on what phase, it determines which agents are available and how it acts.

00:29:49 - Brandon Hancock
So in your root agent, you always have one agent in your root folder — this is the key, the master agent — and all the agents you want to work with go into the sub-agent folder. It's just a rinse and repeat. So you can see in the pre-trip agent: you have a what-to-pack agent, a pre-trip agent, and it feels very much like a crew. You get controls over how agents work together.

00:30:35 - Brandon Hancock
▶ This is what it looks like to share state — you can pass in the current itinerary, the user profile. And what's crazy is everything can interact with state. Tools can update state. Agents can update state. So at any point throughout the application, you're just updating state.

00:31:13 - Brandon Hancock
▶ One other thing that's really cool is how easy they make it to hook up to databases. Once your agents are running, you can go back and look through sessions to see the entire message history between user A and the system. Everything's saved in a session.

00:31:36 - Brandon Hancock
So I'm day five in, week one in, and I'm loving it. I'll have two more videos coming out, and then I'm going to start building more real-world applications with it.

00:31:52 - Juan Torres
<Q>Would you say it has more capabilities than LangGraph [tool:LangGraph], Pydantic, and LangChain [tool:LangChain] together?</Q>

00:32:02 - Brandon Hancock
<A>So I'll speak to LangGraph. LangGraph gives the ability to run code — that's the one thing I think ADK has missed on. Because sometimes you don't want to run an agent; you just want to run code. Once I get to a certain step, I just want to run code. So that's one thing I dislike right now. Pydantic — the main thing I dislike is that I have to become an expert on containerizing my agents, putting it inside a FastAPI application. It is not made for deployment. With ADK's Agent Engine, everything is stored in sessions and state, designed to be saved in a database so you can come back at a later point. In Pydantic land, you have to create your own session database, your own state management. They just missed a few important things.</A>

00:33:36 - Brandon Hancock
▶ They also have a few custom workflows, and all they need to do is add a code workflow and then they've enabled the flows feature. The path to get there is actually within reach, just looking at their codebase.

00:34:09 - Brandon Hancock
▶ And it just comes built in with Google tools — Google Search, all of that. And to do RAG, they have Vertex Search [tool:Vertex Search]. They make RAG easy. You get the entire backend of Google Cloud Platform [tool:Google Cloud Platform] built into ADK, whereas with other platforms, you're using Pinecone [tool:Pinecone] for this, connecting to another platform for 200 tools, and deploying somewhere else. With ADK, I was in one place doing everything. It just felt so clean.

---

<!--SEGMENT
topic: Michal's WhatsApp Conflict-Resolution Chatbot
speakers: Michal Simko, Brandon Hancock, Sam
keywords: Twilio, WhatsApp, ngrok, GPT-3.5 Turbo, GPT-4.0 Mini, Supabase, Cloudflare, short-term memory, long-term memory, service decoupling, conflict resolution
summary: Michal Simko demos a WhatsApp chatbot built with Twilio's SDK and ngrok for webhook tunneling, aimed at mediating conflict resolution between two users. Brandon advises upgrading from GPT-3.5 Turbo to GPT-4.0 Mini for better performance at lower cost, and recommends decoupling the messaging service from Twilio to enable faster local testing. Michal outlines a memory architecture plan using Supabase and Cloudflare object storage.
-->

00:37:09 - Michal Simko
Hey, so yeah, I managed to advance on my chatbot — the in-committee one that we discussed when we were designing. Yeah, so I connected to Twilio [tool:Twilio] to use their SDK to connect to WhatsApp.

00:37:46 - Michal Simko
So basically, at first I was trying to pair two users. Then I abandoned that, and I first want to focus on one side of the communication. Because Twilio — I'm using the free version — the sandbox has to always be updated with the new URL generated by Docker, so I can catch the webhooks. I was like, okay, let me just create a local version. So I created a frontend, and now I'm playing with that frontend and building it in steps. Now I'm at the step of implementing memory. I'll probably go down the route of Supabase [tool:Supabase].

00:39:42 - Brandon Hancock
<Q>So real quick — the end goal is to have two people chatting in WhatsApp to help with conflict resolution, correct?</Q>

00:39:54 - Michal Simko
<A>Mm-hmm, exactly.</A>

00:41:18 - Michal Simko
Next up, I wanted to test different models, because here I'm just using GPT-3.5 Turbo [tool:GPT-3.5 Turbo], so I want to have a way to switch models between Gemini [tool:Gemini] and others, to test the context window.

00:41:48 - Brandon Hancock
<Q>I have a quick note on your model. I could be wrong on this, but I think GPT-3.5 is dumber, more expensive, and slower than GPT-4.0. So I would, as quickly as possible, stop using 3.5. It's just worse results for more money.</Q>

00:42:09 - Sam
▶ GPT-4.0 Mini [tool:GPT-4.0 Mini] is cheaper, faster, and better than 3.5 as well.

00:42:19 - Brandon Hancock
▶ Yeah, I think everything after 3.5 is better and faster.

00:43:49 - Brandon Hancock
<Q>Can I give you a few quick ideas on designing your code? I believe the Twilio code is coupled to messages. What you could do — just to make your life a thousand times easier — is decouple messaging. I would create a messaging service, and then I would have a Twilio service, and then I would have a mock or dummy local web messaging service.</Q>

00:44:30 - Brandon Hancock
<A>So basically, you're going to have a messaging service, and messaging is just going to have all the core things — create, read, and delete. And to make your life easier, you're going to have two things: a Twilio service and a web interface, both calling the messaging service. This way they're not coupled together. What's so nice about this is now, because the messaging service just creates, updates, and sends messages, you could start to test in the web as well just by making a different service that communicates with the messaging one.</A>

00:45:47 - Michal Simko
Yeah, no, it does make sense. I'll just separate it out.

00:45:53 - Brandon Hancock
▶ Yeah, that way you could easily fully test things out in the web, get it working perfectly, quickly. And then all you have to do is hook up Twilio to call the same messaging service.

00:43:21 - Michal Simko
Now the next step is to implement the database and then go the route of having a mid-term database and a long-term memory. I'll probably use Cloudflare object storage [tool:Cloudflare] for that mid-term memory to put some of the messages.

---

<!--SEGMENT
topic: Fernando's Life-Manual Workbook App
speakers: Fernando Lopes Jr., Brandon Hancock
keywords: Google Docs, workbook, Lovable, Supabase, Firebase Studio, Vercel AI SDK, custom GPT, ChatGPT, authentication, life manual, Go High Level, Make
summary: Fernando Lopes Jr. describes wanting to convert a long-standing personal-development Google Doc workbook into a web application for clients. Brandon walks through three levels of complexity: custom GPTs as a no-code starting point, Lovable plus Supabase for a full web app with authentication and database, and eventually an ADK-powered conversational agent that progressively fills out the life manual. He also suggests integrating Go High Level with Make for automation.
-->

00:47:25 - Fernando Lopes Jr.
Hey, Brandon, thanks for hosting, man. I found you last week or two weeks ago with your Firebase YouTube video.

00:47:39 - Fernando Lopes Jr.
So I think the reason the algorithm brought me your video is because I've been wanting to turn a Google Doc [tool:Google Docs] that's a workbook into an app. It's a workbook that I use for me and some of my clients.

00:48:45 - Fernando Lopes Jr.
So this is the workbook. It started as a journaling tool years ago. And I figured, you know, maybe I need a website or an app. So that's where I am. I haven't put the time into Google Studio yet, but that's going to be my project — turning this into an app so that when I update and add things to it, all the users get the new sections, the new graphs, mind maps, or diagrams.

00:49:51 - Brandon Hancock
<Q>So would you mind going up to the top again? And real quick, just to help me fully understand — this is like wellness, self-improvement? And is the goal for the client to answer questions and then be given an artifact, or do they just fill it all out — what do they get?</Q>

00:50:33 - Fernando Lopes Jr.
<A>Yeah, so then you'd get like — I used to call this a life manual. You have your life manual that you keep tuning up, improving, iterating to the next level of your next awareness. So it's mainly like, if humans had a main.md, this could be it, but you create your own. So it's very custom.</A>

00:51:07 - Brandon Hancock
<A>Okay, so let's talk about turning this into a software application. I'm going to go in levels of complexity. So first things first — one possibility is, per section of that workbook, to create something just like this: for every portion of that workbook, you basically put the prompt in here and give it a structured output. You just give it instructions to help people fill out a certain portion of that document. That could be the easiest option. You would just share a special link — maybe five or ten special links. Like, this one helps you come up with your life legacy, this one helps you pick your purpose. You could share a custom GPT [tool:ChatGPT] for each one. That is the easiest one to do. All you need is to know how to create prompts.</A>

00:53:19 - Brandon Hancock
▶ Okay, so that's level one — the easiest, no coding required. Everything after that starts to require some level of coding. So I'm going to talk about Firebase Studio [tool:Firebase Studio] and an alternative. Firebase Studio is a no-code builder — it's great at spinning up single-page applications very quickly. Currently, there are some issues with it because Google's still sorting them out, specifically connecting a database and authentication. I've tried, and for whatever reason they've made it so hard to do.

00:54:01 - Brandon Hancock
▶ So personally, what I would recommend is looking at Lovable [tool:Lovable] as an alternative to creating the web application. Lovable — it is the easiest application you will use to go from prompt to application. The kicker is we're going to have to hook up a database and authentication. I plan to make a video on this — it probably won't happen until mid-May. But I want to talk about specifically how to build your first application using Lovable and Supabase [tool:Supabase]. If you're not in a rush, I would definitely recommend waiting for that to come out mid-May.

00:55:34 - Brandon Hancock
▶ Supabase is the main one you want to do because it's going to give you access to two things you'll need: database and user authentication. Because it sounds like you're selling this to clients, so you might want clients to log in and only have access once they've paid.

00:56:00 - Brandon Hancock
▶ Going back to helping people fill out that form — we would have to hop on a whiteboard session, because basically we just need to chunk it down into smaller steps. When it's that long, it needs to be like: we're going to work on filling out your life manual in five steps. Step one, we answer 20 questions. Step two, another 20. And we'd just be saving the results along the way to a database. And then eventually at the end, you could probably have it generate a nice-looking report that they could download and continually go back and update sections and regenerate the report.

00:58:55 - Brandon Hancock
▶ What's pretty cool is eventually you could turn everything you're talking about into a chat. You could have an agent per section of that document — a specialist on helping people fill it out — and basically people could start to chat with it, answer questions, and as they're answering, information gets saved to state. Over time, they're slowly building up all the information you want them to store, and then you could export it to a document.

01:00:17 - Fernando Lopes Jr.
<Q>I have an agency with Go High Level [tool:Go High Level]. Is there anything on Go High Level as an agency owner that I could use?</Q>

01:00:42 - Brandon Hancock
<A>Not really for what you just showed. One powerful combination though — if you are looking to get more into AI and using it with Go High Level, I would 100% look at exploring using Go High Level with Make [tool:Make], where Make is running AI agents and LLMs on your behalf to take an action. For example, every time you move someone through a pipeline, you could easily create messages, go do research on their behalf — there's a thousand things you could do. You need to use Go High Level webhooks for the pipeline, and that's how you can start to unlock an insane amount of capability that Go High Level doesn't have natively.</A>

---

<!--SEGMENT
topic: Juan's AI Newsletter Service for Labor Unions
speakers: Juan Torres, Brandon Hancock
keywords: AWS EC2, Airflow, ETL pipeline, RDS, agentic system, news report, labor unions, Instantly, cold outreach, parameterized agents, productized service, testimonial
summary: Juan Torres describes a data pipeline running on AWS EC2 with a cron job, transitioning to Apache Airflow, that feeds a financial-sector intelligence web app. He proposes leveraging his background as a union research analyst to offer AI-generated weekly news reports to labor unions as a productized service. Brandon endorses the idea, recommends Instantly for cold outreach, and advises getting a first testimonial client at near-cost before scaling.
-->

01:01:52 - Juan Torres
Yeah, I wasted too much time trying to get my data pipeline to work through AWS EC2 [tool:AWS EC2]. I was using a Linux terminal to upload my data pipeline and using a cron job to automate the process of executing the ETL data pipeline. So now I'm transitioning towards trying to use Airflow [tool:Apache Airflow], still based on AWS, but using the framework they have. My data pipeline works — it retrieves information from the API, saves it in my AWS RDS [tool:AWS RDS] PostgreSQL database, and then populates the figures and plots in my data web application.

01:02:55 - Juan Torres
<Q>I had an idea for trying to get clients. I used to work as a research analyst for the labor movement, for unions here in the United States. One of my tasks was developing a news report every week — retrieving information from several sources, some companies, some policies on certain industries. Since I already developed an agentic system that retrieves information on the finance sector for four banks, I thought I could use this or a similar tool to reach out to research directors and union presidents to demonstrate value and try to get them to become my clients — getting them to develop agentic systems that automate the process of generating insights through a weekly newsletter. Has anyone tried to develop that kind of outreach model?</Q>

01:04:23 - Brandon Hancock
<A>It really sounds like Instantly [tool:Instantly] and then any agent framework — CrewAI or ADK or LangGraph. If you can master both of those — Instantly for cold outreach — have you got a chance to watch any of their YouTube videos? Their channel shows specifically how to go from a raw idea all the way out to a complete custom service business, because that's what you're offering. You're offering a service business: "Hey, I will make this for you. I'll set it up one time — I don't know, $5K? — and then a monthly retainer, $300, something like that."</A>

01:05:20 - Brandon Hancock
▶ The kicker is you probably would have to do this free or close to free one time just to get a testimonial, because people are going to ask: does it work? And what value am I going to get out of it? If you can say, "I did it for them, it worked, and because of this report they unlocked a new revenue stream or went down a different path" — that's the story you need.

01:07:27 - Juan Torres
<A>The thing is, I know this kind of product will be of greatest value to labor unions because I used to do it for the union I worked for, and the manual product I created was so valuable that the sister organization wanted to replicate it. I already have the methodology — targeted industry, targeted company, targeted policies, targeted competitors. What I was thinking of doing is creating a framework that emulates what I did manually. You can create AI agents with parameterized descriptions: "You're a policy analyst analyzing [Bill 58 from the state of Washington]" or "You're a strategic campaign researcher tasked with researching [company name] — look at financials, any reports on union busting." With that parameterization, you can replicate the same agentic system framework throughout several unions working within specific industries.</A>

01:10:09 - Brandon Hancock
▶ Yeah, I totally agree — you do it for one, you could easily copy and paste 80% to the next one. I still think the second you start offering it as a platform for multiple people, people start to think SaaS, and then what you can charge on a custom service is thousands, whereas what you can charge on a news report is a few hundred, maybe a grand max. So just keep the positioning as a custom service.

01:11:02 - Brandon Hancock
▶ The final hard thing I would recommend investigating is some sort of dashboard to allow them to track topics they do and do not want to care about. Because as a customer, if 60% of what it told me to care about I didn't care about, that's a problem. Allow them to confirm and deny auto-suggested topics, so they're always getting more information on stuff they care about.

01:11:42 - Brandon Hancock
▶ And as an add-on upsell — allowing them to chat with the data too. Not only giving them the report, but also offering the ability to chat with all the data being collected instantly. Do the first thing first to get your foot in the door, then upsell.

01:12:07 - Brandon Hancock
▶ After this call, please start messaging people. Let's take action on this. This is a very cool idea. I don't want this one to go to waste.

---

<!--SEGMENT
topic: OpenAI Model Landscape Review
speakers: Andrew Nanton, Brandon Hancock, Bastian Venegas
keywords: GPT-4.1, GPT-4.5, o4-mini, o3-mini, reasoning models, context window, million-token context, prompt engineering, XML formatting, instruction following, writing quality, agentic use
summary: Andrew Nanton raises questions about the current OpenAI model lineup — GPT-4.1, GPT-4.5, and o4-mini — and asks for community experience. Brandon praises GPT-4.5 as the best writing/instruction-following model despite its cost, and notes GPT-4.1's strong agentic performance. Bastian Venegas adds that o4-mini significantly outperforms o3-mini on tool usage, and that GPT-4.1 is a strong coding workhorse comparable to Gemini for non-complex tasks.
-->

01:12:32 - Andrew Nanton
So I had just a quick thought about what you said — I think this general idea of AI suggestions, give it a thumbs up or thumbs down, applies to a ton of different things. That pattern keeps coming up over and over again.

01:13:08 - Andrew Nanton
But the only thing I had today was I was digging into the OpenAI prompt guide on their new models. Sorting out what they are has taken me a couple of steps. It seems like GPT-4.1 [tool:GPT-4.1] is a sort of distillation of GPT-4.5 [tool:GPT-4.5]. And GPT-4.5 is one that nobody should use because it's just this incredibly expensive research behemoth. But GPT-4.1 has this million-token context window. It's not a reasoning model, which is interesting. And then they have o4 [tool:o4-mini].

01:14:00 - Andrew Nanton
<Q>One thing I saw in that prompt guide was that they were recommending that if you have a lot of context in your prompt, you include the instructions both at the top and at the bottom — like sort of wrap all the context in the middle. And they talk about using either Markdown or XML to wrap stuff, which is my preferred way to go. I was curious if anyone had a chance to bang on these models and had any thoughts — are they a winner? Is the huge context useful or is it kind of junk?</Q>

01:14:58 - Brandon Hancock
<A>So I can answer on GPT-4.5. GPT-4.5 is actually my favorite writing model. That and Claude 3 [tool:Claude 3] — those are my favorite writing models right now. I'm constantly cranking out slides for the AI Authority Accelerator to help me rapidly say my ideas and then convert those into slides. GPT-4.0 always does so much other stuff — like, it will just randomly take a style. I'm like, no, we've been doing the same thing for 20 slides, stop. GPT-4.5 has been probably one of the best at continually following the same instructions and continually delivering really high-quality results. I know they're discontinuing it because it costs them an arm and a leg, but I appreciate it. GPT-4.1 — I've done small tests with it. It does follow instructions very well. I haven't gone to the long-context side, but at 40K tokens it absolutely crushed it.</A>

01:16:33 - Andrew Nanton
<Q>What about o4-mini?</Q>

01:16:38 - Brandon Hancock
<A>I haven't got to do that one either. After my one video flopped, I got salty and was like, I'm not doing another one for a while.</A>

01:16:46 - Bastian Venegas
<A>I can summarize a bit of that. o4-mini [tool:o4-mini] is much better at tool usage than o3-mini [tool:o3-mini]. o3 is also really good at subcoding and can do it in its chain of thought, which is quite awesome to watch. I have the same experience as Brandon with GPT-4.5 — really great writer, the best by OpenAI at least. GPT-4.1 is also much better as an agent than GPT-4.0, definitely. The context usage is pretty good — at least for coding, it's kind of similar to Gemini, which is pretty impressive. If you're not doing something overly complex but you need a true workhorse with a lot of specific edits, it really shines. It uses tools in a pretty good sequence — it can run for a long time. Not as much as Gemini, but it's really impressive.</A>

---

<!--SEGMENT
topic: MCP Demo and Evaluation
speakers: Bastian Venegas, Brandon Hancock, Juan Torres
keywords: MCP, Model Context Protocol, Claude Sonnet, Semantic Scholar, Bayesian probability, TypeScript, tool calls, medical diagnosis, function calling, agent tools, Dave Ebbert
summary: Bastian Venegas demos a medical-diagnosis assistant built with nine MCP tools on Claude Sonnet 3.7, showing how it autonomously stores patient history, searches Semantic Scholar for literature, runs Bayesian probability calculations in TypeScript, and renders graphical artifacts — all in three messages. Brandon and Bastian then debate MCP's value proposition versus traditional function calling, concluding it adds power at the cost of complexity and lacks a clear killer use case beyond large tool-reuse scenarios.
-->

01:24:57 - Bastian Venegas
Yeah, I want to show a cool demo of an MCP [tool:MCP] I built — a medical assistant focusing on MCP.

01:25:03 - Brandon Hancock
<Q>Real quick, I have an MCP question for you. I have strictly stayed away from it because of the immense amount of complexity to make a tool call. My question is: it's a flashy thing, everyone talked about it — do you like it? Is it making things easier for you?</Q>

01:25:39 - Bastian Venegas
<A>It's not easier at all. It's more powerful, but it's not easier.</A>

01:25:49 - Brandon Hancock
<Q>Could you elaborate on the "more powerful" part?</Q>

01:25:49 - Bastian Venegas
<A>Yeah. So I built the same assistant as a custom GPT. I gave it a very thorough prompt — to think through stuff systematically and consider using Python to calculate the baseline probability of a given disease for a patient, just simple statistics, and updating that with a Python function to pass it through a test and give you the updated odds of that disease in that same patient. That could be done through an API call, through the interpreter in GPT, or here through running the code yourself, which is what the MCP is doing. But this allows you to create a much more powerful setup. I have no custom prompt here — this is just Claude Sonnet [tool:Claude Sonnet] as it is. I didn't give it any specifics, just set up the MCP with these nine tools.</A>

01:28:19 - Bastian Venegas
So I just read this history of a patient — a summary that doctors do when they bring a patient to hospitalization. It has the typical brief history summary, what they found in the physical exam, some tests, imaging, and evaluations by specialists. My prompt was just that, and I told it to analyze through the MCP.

01:28:56 - Bastian Venegas
And it said: "I'm going to make a quick summary of the history, I'll use this first tool to store this in state where it has the ability to reference it over and over again as the context gets long." Then it said: "I have these two main hypotheses, so I'll use Semantic Scholar Search [tool:Semantic Scholar], which is an AI-powered service like PubMed, to quickly search through different papers." And it found some it could reference. Then it started using code — TypeScript and math — to compare the actual probabilities for each disease. It goes: "I had this prior thought, and now that I'm reading and gathering this information, I can give you the updated probabilities."

01:30:18 - Bastian Venegas
After that, it says: "Let's quickly check if this is a time-dependent disease" — for example, if you had a heart attack, you need to get the clot out. So some things are truly time-dependent. This wasn't one of those. So: "This is an emergency, we can think." That's all in one message. Then I told it to use the MCP tool to render some artifacts and show some cool summaries.

01:30:56 - Bastian Venegas
This is the graphical representation of the odds — first baseline, and after the test for three different hypotheses. This is a representation of how abnormal the lab values are. And this is an algorithm trying to show you how you could think of this problem and what follow-up tests would be most useful — a quick decision tree. And this is the final report.

01:32:33 - Brandon Hancock
Juan called it out — that's only three messages.

01:32:37 - Bastian Venegas
Three messages to get this kind of analysis. Was it Claude 3.7?

01:32:43 - Brandon Hancock
3.7? Or was it 3.7 reasoning or 3.7 plain?

01:32:48 - Bastian Venegas
I don't think it was reasoning. I think it's the normal type.

01:32:54 - Brandon Hancock
<Q>So here's what I had a question on. I dropped a video in the chat — Dave Ebbert [link:Dave Ebbert MCP crash course video] had a great video on an MCP crash course for Python developers. After watching the video, I still didn't know why or when to use MCP. He has this chart comparing MCP to traditional function calling. At a small scale, the traditional approach — agent and tools — is easier. The main argument for MCP is when you have a bunch of tools, reuse matters, and distribution is needed. The only reason I could understand for MCP is if you had shared tools you wanted to drop into multiple agents — almost like a mono repo. That's the only reason I could think of.</Q>

01:35:01 - Bastian Venegas
<A>We have this bias of thinking that MCP is something between an API call and calling a function, which is true. But the way they divided it — we have prompts in the server, we have resources (which could be something in a database), and we have the tools (which could be RAG or any API). I think the way you can make it shine is if you make a good LLM prompt layer in the server, and that enables better use of the other stuff available in the MCP. That can help you scale in a better way where your MCP is almost like a dedicated server for your agent that does a really complex thing. But that may not always make sense.</A>

01:36:14 - Brandon Hancock
▶ Yeah, no, I totally agree. And I think it's one of those things — just like YouTube, you can't show off 200 tools, so all the demos are two tools. And that's where I'm just like, I would just put that in a function. So yeah.

01:36:39 - Bastian Venegas
▶ It's not worth making a very in-the-weeds video on MCP yet, in my opinion.

---

<!--SEGMENT
topic: YouTube Personal Brand Launch Advice
speakers: Alex, Brandon Hancock, Andrew Nanton
keywords: YouTube channel, OBS, Screen Studio, Upwork, video editing, thumbnails, listicles, how-to videos, Spanish-language content, personal brand, AI content creator, Deity mic
summary: Alex, returning after a break from real estate projects, shares plans to launch a Spanish-language AI YouTube channel inspired by Brandon's content. Brandon provides a practical starter kit: use OBS for recording, hire editors and thumbnail designers on Upwork, start with listicle and how-to formats, and treat early videos as deliberate practice by mirroring existing successful content before developing a personal style. He emphasizes consistency over perfection and the exponential nature of YouTube growth.
-->

01:39:17 - Alex
I just wanted to say hi. Back into getting a hold of my AI projects.

01:39:30 - Alex
I actually ended some business — real estate projects — it's a wrap. So I could dedicate more time to growing these AI projects of mine. I'm catching up with your videos, which are really cool, and thinking of starting an AI personal brand. Getting inspiration from your channel and trying to make like a Spanish version — a Mexico version.

01:40:03 - Brandon Hancock
Did you get a chance to watch that video? The personal brand one?

01:40:07 - Alex
Oh, yeah, by chance.

01:40:09 - Brandon Hancock
▶ Yeah, if you haven't fully watched that, 10 out of 10 would recommend. And yeah, dude, I love it. I think being in different countries — it does have different ceilings, but it's a completely different competition and playing field. The two most competitive right now are America and India. If you look at my YouTube channel, the majority of my views come from India. But by competing in different languages, there are hundreds of thousands of companies in Mexico, Spain, and all Spanish-speaking countries that also need to use AI. So it's just competing in different ponds.

01:41:07 - Brandon Hancock
▶ And if you have any questions for kicking things off, always happy to point you in the right direction and share a few battle scars of things I wouldn't do.

01:41:22 - Alex
<Q>Just for starting — do you use Loom to record your videos?</Q>

01:41:28 - Brandon Hancock
<A>No. Quick answer: I use OBS [tool:OBS] for recording my screen. And then within OBS — I'm a huge fan of hiring editors. You are an AI developer, an AI engineer. That hourly rate is much higher than a video editor. So we have to arbitrage our time appropriately. ▶ I would recommend hiring someone on Upwork [tool:Upwork] to do your video editing for you — $25 to $30 an hour to handle all editing needs. And same for a thumbnail — I'd hire a thumbnail editor for $30 a thumbnail.</A>

01:42:23 - Brandon Hancock
▶ The two main video formats I would focus on when starting out are listicles and how-to videos. Those are the two main ways to get started for good practice reps. Then you'll eventually move over to doing beefier videos — over 20 minutes — on things like quick-start guides for new frameworks, masterclasses. But get started first on making videos, talking to a camera, properly getting your ideas across, going through the process a few times before diving into the deeper stuff.

01:43:32 - Brandon Hancock
▶ The main thing is: it takes time. The only way you lose is by stopping. Because if you just keep going on YouTube, it is an exponential game. The longer you stay in, the bigger the rewards. YouTube naturally just doesn't know who you are and who your audience is at first, but the exact same video a year in — once it knows your style and you have a following — will do five times better.

01:44:51 - Brandon Hancock
▶ The main thing I would recommend is getting a good mic. I have a Deity [tool:Deity mic] mic — any of the Deity mics.

01:45:22 - Brandon Hancock
▶ Final recommendation: it's kind of like when you're learning how to do anything new. I would just — you have my permission — just copy me for a practice run. Like, Brandon's making a video on this topic, I'm going to make a video on this topic but try my own style. Brandon did a video on ADK Quick Start — I'm going to make a video on ADK Quick Start. Script it out, see what you would do, then compare it to what I did. Be like, why did he do that? Oh, it's because he was guiding the viewer in this way.

01:46:26 - Andrew Nanton
▶ Screen Studio [tool:Screen Studio] — if you have a Mac, it's also amazing. It's not the easiest for doing long-form videos with multiple clips, but if you're doing stuff in a single take, it is the best video recording software out there right now.

---

=== UNRESOLVED SPEAKERS ===

- **Sam** — Raw name "Sam" with last name mentioned as "Harris" (or similar, self-described as uncertain); no canonical form confirmed in alias map. Passed through as "Sam."
- **The Dharma House** — Raw speaker label used as-is; no alias map entry found. Appears to be "Aaron" based on in-meeting references ("Aaron, all settled in, Florida man now"), but canonical full name not confirmed.
- **Fernando Lopes Jr.** — Passed through unchanged; not confirmed in alias map.
- **Andrew Nanton** — Passed through unchanged; not confirmed in alias map.
- **Bastian Venegas** — Passed through unchanged; not confirmed in alias map.
- **Juan Torres** — Passed through unchanged; not confirmed in alias map.
- **Alex** — Single name only; no alias map entry found.