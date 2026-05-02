=== SESSION ===
date: 2025-05-13 (inferred from demo output)
duration_estimate: ~2 hours
main_themes: Google ADK voice agent demo, AI framework landscape, member project showcases (vehicle routing, FastAPI calculator, Reddit sentiment tool, WhatsApp conflict-resolution bot), sales qualification frameworks, vibe coding pitfalls, Google I/O anticipation

---

<!--SEGMENT
topic: Pre-session Introductions and Community Context
speakers: Marc Juretus, Tom Welsh, Lucas cooper-Bey, AbdulShakur Abdullah
keywords: community learning, framework overload, LangChain, LangGraph, CrewAI, Agno, Amazon Bedrock, Krish Naik, learning disability, adaptability
summary: Participants introduce themselves across time zones (Philadelphia, London) and discuss the challenge of keeping up with rapidly evolving AI frameworks. The conversation touches on the value of adaptability over mastery of any single tool, and Lucas shares a personal story about late-blooming learning motivation.
-->

00:01:00 - Marc Juretus
Oh, hey. How you doing?

00:01:03 - Tom Welsh
You hear me now?

00:01:04 - Marc Juretus
Can't complain.

00:01:08 - Tom Welsh
<Q>Where are you located, if I may ask?</Q>

00:01:11 - Tom Welsh
<A>London.</A>

00:01:14 - Marc Juretus
I'm in the Philadelphia area of the United States.

00:01:22 - Lucas cooper-Bey
Hey, Tom. Hey.

00:01:36 - Lucas cooper-Bey
It's been a while since I dropped in on you guys, but I recognize some faces.

00:01:55 - Tom Welsh
I just, I'm just sticking with this community because there's too much to learn already. And you've already won half the battle. One of the guys, I can't remember who posted it this morning, had a very good point — there's just so much crap out there that you can look at. You could have a full day job just looking at stuff.

00:02:15 - Lucas cooper-Bey
Stick to one thing and go for it.

00:02:32 - Marc Juretus
I do a course — I'm in the Philly area, but it's at 5:30 in the morning because the guy does it in India. So it's 5:30 Saturday and Sunday, and we've been doing it since January. And I got to admit, that's starting to drag on me right now, man.

00:02:50 - Marc Juretus
His name is Krish Naik, and he has it. He does a course on Saturdays and Sundays. It's India time, I think 3 p.m., but it's 5:30 in the morning my time. We've gone from LangChain [tool:LangChain] to LangGraph [tool:LangGraph] to CrewAI [tool:CrewAI] to Agno [tool:Agno]. It's like you're knowledgeable of many, but master of none.

00:03:34 - Lucas cooper-Bey
<A>Yeah, I mean, I agree with that to an extent, but the ability to get up and move between them — you understand there are some consistencies between them. The ability to move quickly, to learn fast, and to adapt quickly — if that's all you take away from jumping from framework to framework, that's essentially the best skill anyone could ever have from now.</A>

00:04:10 - Lucas cooper-Bey
That's why I'm so proud of my gaming background growing up. Having to relearn control types and game rules and how to solve problems through video games for my entire childhood has actually helped me out a lot, because you just have to keep learning something new every day.

00:04:52 - Lucas cooper-Bey
I was learning disabled, so they put me in all the "special" rooms. I didn't get to learn anything until I was older, and then when I got older, I became infatuated with learning because I had found the things I was interested in.

00:05:00 - AbdulShakur Abdullah
Those were more focused learning rooms. That's what they told me.

---

<!--SEGMENT
topic: Google ADK Voice Agent Demo
speakers: Brandon Hancock, Lucas cooper-Bey
keywords: Google ADK, Agent Development Kit, Gemini voice models, Google Calendar API, WebSockets, tool calling, voice agent, VO2, Auth0, agent authentication
summary: Brandon Hancock demonstrates a live voice agent built with Google's Agent Development Kit (ADK) and Gemini's newest voice models, integrated with Google Calendar. The agent successfully creates, moves, and deletes calendar events via voice commands, and Brandon outlines upcoming content plans including VO2 video generation and agent authentication with Auth0.
-->

00:05:37 - Brandon Hancock
What I want to do real fast before things kick off — show you a cool demo I'm working on that I'll be making a video on for you guys this week.

00:05:56 - Brandon Hancock
All right, so I've been going deep into ADK [tool:Google ADK], and I keep going deeper. So, long story short, working on a voice agent for you guys. It's using Gemini's newest voice models [tool:Gemini], but it's also, at the same time, using Agent Development Kit. So it's actually combining both of them.

00:06:40 - Brandon Hancock
Here's the demo. Fingers crossed it works. It worked two minutes ago.

00:06:59 - Brandon Hancock
*[to agent]* What's today's date?

00:07:00 - Brandon Hancock
*[agent responds]* Today's date is May 13, 2025.

00:07:04 - Brandon Hancock
*[to agent]* What calendar events do I have on Thursday?

00:07:10 - Brandon Hancock
*[agent responds]* On Thursday, May 15, 2025, you have a meeting titled Steve and Brandon Hancock from 1 p.m. to 1:30 p.m.

00:07:18 - Brandon Hancock
*[to agent]* Can you please create an event for me on Thursday at 5 p.m.? That's one hour long and it should say Dinner Date with Carly.

00:07:30 - Brandon Hancock
*[agent responds]* I have created an event called Dinner Date with Carly for Thursday, May 15, 2025 from 5 p.m. to 6 p.m.

00:07:38 - Brandon Hancock
*[to agent]* I made a mistake. Can you actually move that dinner date to Friday at 5 p.m. and still needs to be one hour long?

00:07:50 - Brandon Hancock
*[agent responds]* I've moved the Dinner Date with Carly to Friday, May 16, 2025 from 5 p.m. to 6 p.m.

00:07:57 - Brandon Hancock
*[to agent]* Actually, I'm upset at her. Can you delete that event?

00:08:02 - Brandon Hancock
*[agent responds]* I have deleted the Dinner Date with Carly event.

00:08:13 - Brandon Hancock
But yeah, all around, freaking cool, guys. I've been loving this because every API call is just something you can talk to. There just hasn't been a nice programmatic tool to handle the routing, handle the tool calling, and once the tool calling happens, talk back to you.

00:08:47 - Brandon Hancock
▶ I've been absolutely loving it. The thing I'm loving the most about Google right now is: as long as I just learn the ecosystem, I'll have access to voice agents, video agents, the best agent right now — Gemini 2.5 Pro [tool:Gemini 2.5 Pro] — they have an agent framework, they have all of it. It checks every box for everything I need to create as a developer.

00:09:09 - Brandon Hancock
Quick update for what's coming down the pipeline: voice agent's going to be next for you guys, and then probably some sort of VO2 [tool:VO2] video creator next.

00:09:28 - Lucas cooper-Bey
I'll tell you, man, warning on VO2 — I accidentally racked up $800 on there real quick.

00:09:40 - Lucas cooper-Bey
I called them up, and then I got them to reduce it by 75%, but I'm still out some hundreds.

00:09:49 - Brandon Hancock
Yeah, so the UI was actually — Google has a super simple demo that doesn't have any additional tool calling, like integrating with the calendar. So I just beefed it up. It had zero styling — just a box and a box. There was nothing else, no styling, no loading, no connected to the WebSockets [tool:WebSockets], none of it was there.

00:10:32 - Brandon Hancock
▶ One of the core problems you guys are going to realize as you play more and more with agents is agent authentication. I'll probably be doing something on Auth0 [tool:Auth0] soon because they finally have something to where you log in once with your Google credentials and then it can go forth — you're trying to access your calendar, well, cool, because you're logged into Google, I can now do it for you. And you're not having to download credentials and create API services in Google Cloud.

---

<!--SEGMENT
topic: Marc's Learning Journey and ADK Project Plans
speakers: Marc Juretus, Brandon Hancock, Lucas cooper-Bey
keywords: Google ADK, Vertex AI, poetry, UV, virtual environment, LangChain, CrewAI, Amazon Bedrock, Autogen, fantasy football agent, planner agent, React agent, workflows
summary: Marc describes his multi-framework learning journey (LangChain → LangGraph → CrewAI → Agno → Amazon Bedrock → Autogen) and a setup issue with a Vertex AI project. Brandon clarifies ADK's plan-and-act architecture versus React agent loops, and Marc outlines his goal of building a fantasy football agent using ADK.
-->

00:11:33 - Marc Juretus
I was telling the gentlemen about my journey. I take a course — Saturday and Sunday with the gentleman from India. We went from LangChain [tool:LangChain] to CrewAI [tool:CrewAI] to now Amazon Bedrock [tool:Amazon Bedrock]. I'm wishing the class was over, man, because it's 5:30 in the morning. But I'm going to try to stay focused on Google ADK [tool:Google ADK], because I just see this going somewhere.

00:12:04 - Marc Juretus
I did post in the forum about the problem with the build for your first agent for Vertex AI [tool:Vertex AI]. I was getting "the project I gave is not a poetry project" and "poetry configuration is invalid." I could have sworn I followed it verbatim.

00:12:30 - Brandon Hancock
Yeah, the quick update on that project — I wanted to make it as basic as possible, because a lot of people were complaining about Poetry [tool:Poetry]. What you'll see in the README is basically you'll just do a Python `-m` to make a virtual environment. You'll type in `venv`. Even better than UV [tool:UV]? It's simpler. No, it's not as good as UV. UV is blazing fast. It is wild how powerful UV is. But just for following along for a YouTube tutorial, I can just say Python — there's no Python-and-Poetry, Python-and-UV. So it was more for the tutorial side of things.

00:13:50 - Marc Juretus
I'm a full-stack developer now. I've probably been at it about 29 years. I work for a hobby. Kind of making some moves and stuff. So I want to make sure if my next landing spot at 53 is maybe I can do something for the next few years. I've been aggressively trying to learn some of the frameworks — Java, ASP.NET, this, that, and the other.

00:14:47 - Marc Juretus
The last piece we have is Autogen [tool:Autogen].

00:16:51 - Marc Juretus
I'm going to try to stay on this Google ADK. I'm trying to build something with fantasy football. I used to do a radio show with that and give advice. What I want to do is maintain my fantasy roster, go out, look at the rankings, and have something like, "All right, here are your 15 players. This is who I want you to start this week." And I want to let the agent completely run the team for an entire season and see how it does.

00:17:18 - Brandon Hancock
That would be awesome. So high-level updates on ADK: the thing I'm loving the most is one platform that has access to everything. Up to this point, it was like, okay, you have LangChain to help do your chunking, embedding, then you have a Pinecone [tool:Pinecone] vector store, and then somewhere else where you're actually creating agents. There were just so many moving parts.

00:19:41 - Brandon Hancock
▶ This is such an important lesson when it comes to ADK — it is not a React agent. A React agent reasons and then acts, meaning it will continually loop over and over again. That is not Agent Development Kit. ADK is plan-and-act: you give a request, it's like, "Cool, I'm going to call these three tools, use the outputs in one final one, and then be done." There's no loop. If you want to do a loop, you have to do workflows to get that React-like nature that you're probably familiar with from CrewAI and LangChain.

00:20:45 - Marc Juretus
I have about 40% of the way in Crew. But now I'm like, I want to probably go into ADK. From what you said, I think I should be able to create my own custom tools and maybe reutilize what I've done in that way.

---

<!--SEGMENT
topic: Tom's Vehicle Routing Problem App
speakers: Tom Welsh, Brandon Hancock
keywords: vehicle routing problem, VRP, time windows, here.com, TimeFold, Cursor, route optimization, CSV, FastAPI, polylines, PDF export, vibe coding business opportunity
summary: Tom demonstrates a web-based vehicle routing problem (VRP) optimizer with time windows, built using here.com's routing API and Cursor IDE with custom rules. Brandon highlights a business opportunity in helping vibe coders complete their 60%-finished apps, noting he has already landed a contract doing exactly that.
-->

00:21:15 - Tom Welsh
I pulled my finger out and started walking into VR. Well, it gets rid of the blockage, you know.

00:22:07 - Tom Welsh
So I've been playing with my stupid little vehicle routing problem. I got stuck into Cursor [tool:Cursor] and set up a bunch of rules. You can set all the rules up, and you can upload them with your code base so anyone else can get that.

00:23:00 - Tom Welsh
This is my route optimizer. So I've got a route, validate my file, got my plan, so I can set up whether I'm going from East Croydon by car or by train. I've got constraints — vehicles, jobs, speeds and stuff. Got my view — map should come up in a minute — there, we've got a nice little map with my places on it. And then my route, then I optimize my route. There should be polylines going up here just now — it doesn't actually follow the road yet, but you can see I get a route coming out. I can export my stuff to PDF, get it out, normal stats.

00:24:19 - Brandon Hancock
<Q>Real quick before you pull that up — what did you decide to use for a blob store?</Q>

00:24:26 - Tom Welsh
<A>I haven't got a blob store. It's saved locally right now. Front-end, back-end, API calls to here.com [tool:here.com]. I'm using here.com. If I can find my thing again — so these guys, they're doing API for route making. I also found this one, TimeFold [tool:TimeFold], which is a Python module you can pull down, and it does route optimizations and everything. It requires a bit of Java, but they've also got a professional version as well. here.com's got a free tier, which is what I'm currently using.</A>

00:25:41 - Tom Welsh
Yeah, got FastAPI back-end and everything.

00:25:43 - Brandon Hancock
You're getting dangerous, Tom.

00:25:58 - Brandon Hancock
▶ Actual business idea. The amount of people who are now vibe coders that create ideas and get like 60% there — as an engineer, it's honestly a blessing. A lot of the times for people who have zero programming experience, they're like, "Hey, I made this app. It's 60% there" — meaning it has a great UI, barely any back-end. It's a phenomenal spot right now to be an engineer to help vibe coders complete their service. I actually just got a contract to do that exact same thing. So it is an actual business idea right now.

00:27:30 - Tom Welsh
So the VRP with time windows is coming along quite nicely. I'm really just stuck on routing the maps now, which is the problem.

00:27:48 - Brandon Hancock
I mean, you're literally right there. The second the lines go back up, that's amazing.

---

<!--SEGMENT
topic: Paul's FastAPI Calculator and Sales Qualification
speakers: Paul Miller, Brandon Hancock, AbdulShakur Abdullah, Sam
keywords: FastAPI, Lovable, DigitalOcean, Next.js, BANT, SPIN Selling, Alex Hormozi, sales qualification, economist tool, vibe coding, formula accuracy, decision makers
summary: Paul describes separating calculation logic from a Lovable-built front-end into a FastAPI back-end deployed on DigitalOcean, achieving reliable formula accuracy for an economist-facing tool. The discussion pivots to sales qualification frameworks — BANT and SPIN Selling — prompted by Paul's experience with a profitable but uncommitted prospect.
-->

00:28:04 - Paul Miller
So I'm still working away with my little calculator, just finalizing. So I've got the architecture right now. Originally I had everything running in Lovable [tool:Lovable], while it got me 60% of the way there, but the calculation was wrong, even though I prompted it very carefully with the right calculation.

00:28:38 - Paul Miller
And if I think of the use case, this is going to economists. So you start getting calculations wrong, then the whole credibility of the tool is out the door.

00:29:00 - Paul Miller
What I ended up doing was to take the underlying background office that does the calculation, and purely doing that in FastAPI [tool:FastAPI]. So I wrote it in Python with FastAPI and said, look, here's the inputs, here's the calculations, and here's the outputs. And then I published that FastAPI to a host. I did a nice little wrapper around it, and now it's working beautifully.

00:29:37 - Paul Miller
So then I went back to Lovable and said, here's the API, here's how you should be working with that API, and here's the result sets. Now you do the nice look and feel, and it's humming.

00:30:00 - Paul Miller
I used Claude [tool:Claude] to write the code for me. I said, look, write the FastAPI code in the most simple way possible, so I can just go in and edit the formula directly with Python. Any fixed values, use a JSON file, but all user input goes through the API.

00:31:47 - Paul Miller
That's the first time I've ever published my own API. I did it to DigitalOcean [tool:DigitalOcean], and it was really, really easy and really fast. I'm doing updates — the customer rings up and says they want to change a formula or an output, I can turn it around in about 10 minutes on the API side. I'm spending about $5 a month, which is probably overkill for the host.

00:33:00 - Brandon Hancock
▶ If you didn't want to pay the extra $5, just inside of a Next.js [tool:Next.js] project, you can always make an API folder — that's how you can create back-end on your Next.js application. Next.js is full-stack back-end and front-end, and that way, all in one app, you can say, front-end, make a request to the back-end.

00:34:03 - Paul Miller
Outside of that, I came across a pretty recurring issue I have with a lot of customers. The challenge is their business makes a lot of money. And the problem with a business that makes a lot of money is — while you have a noisy part of the business, the operational guys that do a lot of work, while those guys may have real problems that AI or apps can solve — they still make money regardless, so they can waste your time. They have no compelling reason to get off their backsides and go through software adoption.

00:35:28 - Paul Miller
<Q>Is it a business that's challenged commercially at the moment? Or is the leader of the business actually committed to making it more efficient?</Q>

00:36:16 - Sam
<Q>Do you do like a prototype kind of thing and then sort of reject it?</Q>

00:36:27 - Paul Miller
<A>We go in, do a lot of workshops and discussions and confirm what their problem is and how they can benefit from using us. Which wastes a huge amount of my team's valuable time. The pre-qualification — you kind of want to say, who's the ultimate decision-maker? How does this impact the commercials of your business? Are you a profitable business to start with? And how invested are the leadership team in seeing this problem solved?</A>

00:37:22 - Brandon Hancock
▶ The thing I just shared — Alex Hormozi's special — the acronym is BANT [tool:BANT framework]. Budget, Authority, Need, Timeline. And I cannot express how awesome of an acronym this is, because if any of these fall through, you're hosed. It literally does not matter.

00:39:02 - AbdulShakur Abdullah
So basically SPIN Selling [tool:SPIN Selling] — you try to quickly get them to describe the Situation they're going through, the Problem, the Implications, and you try to lead them to the implications of that problem. So you kind of already talked about how the solution would save time and stuff. At that point, you start asking questions like, what's the average amount that one of those people makes that you would be saving their time? How many current clients are they able to pile on? The issue with this technique is it causes a lot of initial front-loading of pulling out information.

00:40:31 - AbdulShakur Abdullah
Once you have all that, you then do the Need-Payoff, which Alex Hormozi is very good at — he basically really focuses in on what the payoff is if you're selling that particular product.

00:41:00 - Paul Miller
The thing that is the biggest difference is that if that business is highly profitable to start with, while the middle of the business — the operational layer — actually sees massive benefits with what we do, ultimately the business won't care because the decision-makers will not see the true reason to change.

00:41:52 - Paul Miller
The leadership team are never usually the ones that bring me in. It's the middle of the business that brings me in. And then it's like — we need your high-level leadership team that's going to approve it. Are they bought into your problem? Are they willing to fund it? Then you find out — unless you actually know that they're losing money and that this is their number one priority, then you're wasting your time.

---

<!--SEGMENT
topic: Google I/O Anticipation and ADK Production Readiness
speakers: Brandon Hancock, Paul Miller, Jake Maymar
keywords: Google I/O, ADK UI, Vertex AI agent studio, N8N, Azure AI Foundry, Amazon Bedrock agents, agent traces, production reliability, Gemini 2.5 Pro, agent deployment
summary: Paul flags that Google I/O is one week away, prompting discussion about what Google may still be holding back. Brandon explains the current gap in ADK's Vertex UI for deployed agents, anticipates a major UI release that could be the "N8N moment for developers," and contrasts Google's trajectory against Amazon and Azure's agent frameworks.
-->

00:43:39 - Paul Miller
I'm really excited to get into that Google stuff. And I just put a point in the comment — Google I/O [tool:Google I/O] conference, their main annual conference, is still a week away. So they've done all these announcements before. So what are they holding back? It's like my mind is blown with what Google is planning and doing. Every week, they're executing something crazy.

00:44:04 - Brandon Hancock
I got to talk to one of the DevRel guys. Right now, their agent kit UI doesn't exist. The ADK [tool:Google ADK] — the Agent Development Kit UI inside of Vertex [tool:Vertex AI] does not exist. So if you deploy an agent, it's like, okay, cool, you can use the CLI and API request, but it's disgusting on the UI right now. But apparently they're releasing that, and I am so pumped because I believe it's going to be the N8N [tool:N8N] moment, but for developers. Because N8N made it to where anyone can make agents and they just connect to tools. I believe they're getting to a point to do it with ADK.

00:45:01 - Brandon Hancock
Amazon, their agent framework that's deployed — it's impossible to use. Azure's [tool:Azure AI Foundry], on video, all their video demos are amazing. And if they can pull off what they're trying to do, they'll be a good competitor. But they just haven't even released anything to show that they're going in that direction. It's all just demo, demo, demo, but no actual substance yet.

00:46:56 - Brandon Hancock
▶ The main thing you need to look at as the developer hosting the project — you want to be able to look at traces. What actually happened per execution? They already have that, but it's kind of janky right now because it feels very enterprise-y. I'm hoping when they actually get the UI out there, it's like, oh, I can see exactly all the agent calls, the order that it happened, and I can see exactly where it went wrong.

00:47:00 - Jake Maymar
It's interesting — Google is really the one that's going to fill the gap. What's missing is something like SEO — a standard, you know, like I can point to this thing and it's going to not have any hallucinations, it's not going to drift, it's repeatable, it's standard. You can basically set it and essentially forget it. And I think Google is probably the closest to this.

---

<!--SEGMENT
topic: Abdul's News-to-Infographic Agent and Image Generation Comparison
speakers: AbdulShakur Abdullah, Brandon Hancock, Bastian Venegas
keywords: OpenAI GPT Image 1, Gemini 2.0 Flash image generation, Imagen, Google AI Studio, infographic agent, image verification, API authentication, cost comparison, thumbnail generation
summary: AbdulShakur describes building a news-article-to-infographic agent, hitting a wall with OpenAI's identity-verification requirement for GPT Image 1 API access, and switching to Google's Gemini 2.0 Flash image generation. He reports comparable quality, clear text rendering, and better cost. Pricing is briefly compared between providers.
-->

00:45:50 - AbdulShakur Abdullah
So I was working on the news article to infographic agent. I started with looking at your YouTube thumbnail and using that as the baseline, so I loaded that up, I got your version to work with creating thumbnails — great, okay, I got that working. Then I tried to brute-force change it with vibe coding, just sitting back, and it broke so many things. I wasted like half a day trying to do it that way.

00:47:00 - AbdulShakur Abdullah
I tried to just change it to where it would take whatever prompt was given, even from the beginning, getting part of the style guide to make an infographic from that. And then I ran into the issue of my image generator wouldn't connect anymore — my OpenAI [tool:OpenAI] one.

00:47:19 - Brandon Hancock
<Q>Like, you were using OpenAI image generator?</Q>

00:47:23 - AbdulShakur Abdullah
<A>Initially, I was, and then I tried to authenticate it, and for some reason, my authentication wasn't working. I tried it like four or five times, and I just gave up. I was like, all right, let me see if I can try Google's image generator.</A>

00:48:01 - Brandon Hancock
So in order to use OpenAI's new GPT Image 1 [tool:GPT Image 1] model through their API, you have to verify with a license and a face picture. Like, you have to submit your information to the OpenAI gods. Yeah, there's a whole verify, turn your head kind of thing.

00:48:38 - Brandon Hancock
When you do get to try out the Google Image Generator, I have yet to go deep into it. I would love to hear your feedback on the quality comparison between Gemini and OpenAI. It looks like VO2 [tool:VO2] is outperforming Sora when it comes to video, so I'm curious on the image quality.

00:49:11 - AbdulShakur Abdullah
I've only got the images to work in Google AI Studio [tool:Google AI Studio]. So basically testing — taking the prompt, throwing it directly in there, and doing an image to generate that way, to test to see if my prompts were actually any good. The images — the text was clear on it. The image quality was comparable. The speed was good. And the cost seemed better, too. So I didn't see, for my use case, any downside to switching.

00:50:41 - AbdulShakur Abdullah
I was actually using the new one — Gemini 2.0 Flash Preview Image Generation [tool:Gemini 2.0 Flash].

00:50:05 - Brandon Hancock
You have $0.04 per image.

00:50:18 - Bastian Venegas
<A>Yeah, it's $0.02 [for OpenAI]. Okay, so that's $0.20.</A>

00:51:59 - Brandon Hancock
▶ Once you get it up and running, I'd love to see some of the outputs, because creating infographics — I'd love to see what quality you're getting as you keep playing with it.

---

<!--SEGMENT
topic: Sam's Report Builder Sprint and Reasoning Models in React Agents
speakers: Sam, Brandon Hancock
keywords: LangGraph, React agent, reasoning models, O3 Mini, DeepSeek R1, GPT-4.1, report builder, subgraph, ADK artifacts, artifact versioning, sprint planning
summary: Sam asks whether reasoning models (e.g., O3 Mini, DeepSeek R1) can back a React agent effectively, and Brandon explains the trade-off: longer iteration loops but potentially more accurate actions. Sam also shares plans for a focused sprint week on a LangGraph-based report builder, and Brandon recommends ADK's artifact versioning as a useful feature for document generation workflows.
-->

00:53:49 - Sam
<Q>Anyone tried reasoning models with React agents? Someone asked me that question in another context. I just wasn't sure if anyone had any experience — whether that's going to fight each other because they're doing the same work.</Q>

00:54:06 - Brandon Hancock
<Q>So you're talking about doing multi-agents where each agent is a reasoning agent? As in, the backing model is actually a reasoning style model as opposed to like a GPT-4.1 or something?</Q>

00:54:31 - Sam
<A>So like say you deploy a React agent, but the model you're using is like O3 Mini [tool:O3 Mini] or O3 as opposed to like a GPT-4.1 [tool:GPT-4.1] or something. So the backing model is actually a reasoning style model.</A>

00:55:00 - Brandon Hancock
<A>For most reasoning models, that thinking step — it's not taking any action, but it's reasoning on its reasoning. It's more of an expanded chain of thought before it takes an action. So if you were to actually use it in a React agent, I think it would still work fine. I think just the iterations between the loops would take a lot longer — that would be the main thing. But you might be taking the correct action, where on a dumb model it's just like, do this, oh shoot, do this, oh shoot, that was wrong. We were doing it back in the day with O3 Mini. And DeepSeek R1 [tool:DeepSeek R1], you could do it with that too. Totally doable.</A>

00:56:14 - Sam
▶ Yeah, so it sounds like it's just a trade-off between — you might get better output, but it's just time and money because those models are quite expensive.

00:56:28 - Sam
I'm kind of eking out a sprint. I'm going to take leave from my day job and then do like a week with it. Just trying to work out what that is. It'll be a vacation work week. I'm not going to do a Brandon yet.

00:58:00 - Sam
It's kind of a report builder. My strategy is to kind of have the architecture in place and then just focus on one section, and then once we get that subgraph sorted, I'll just replicate it across all the sections of the report. Focusing on that one graph, you get the flow, and then you ramp it up as you go.

00:58:27 - Brandon Hancock
▶ One thing — I know you were using LangGraph [tool:LangGraph], but ADK has a concept of artifacts. The part that's pretty cool is it also includes artifact versioning, so for whatever reason, like in your case, you're working with these PDFs that you're creating, and for whatever reason you generate a version and they go "undo, I don't like it" — super easy to then go back to the previous version in that artifact as you're helping them create that document. Agents are prone to make errors, so the ability to roll back is a really cool feature.

---

<!--SEGMENT
topic: Maksym's WhatsApp Product Growth and HIPAA Deployment Video
speakers: Maksym Liamin, Brandon Hancock
keywords: WhatsApp, user engagement, pinned contacts, session metrics, HIPAA compliance, Azure, FastAPI, Next.js, Postgres, blob store, Docker, Loom, Tella.tv, OBS, YouTube content
summary: Maksym reports reaching 3,000 active onboarded users and growing average messages per user from 15 to 20.5 through a pin-prompt strategy. He also announces plans to record a HIPAA-compliant deployment tutorial covering a Python worker, FastAPI, Next.js, Azure blob store, and Postgres — a gap he found in existing resources.
-->

00:59:37 - Maksym Liamin
Hi, guys. I have not that many things to report. We just keep growing, keep building the same thing. Today we hit 3,000 active users who got onboarded. It's great. And now we're just waiting to add more stuff.

00:59:54 - Maksym Liamin
We've also been fighting to pin the bot for the users. In WhatsApp [tool:WhatsApp], you can have only three pinned contacts, so we've been trying to implement different strategies on how we can make people pin us. Normally our users have a pin for their wife, for their boss, and for a group chat of their colleagues, so we need to fight for a wife or the boss.

01:00:21 - Maksym Liamin
Every 10 sessions — we calculate sessions, like if you send 200 messages within 30 minutes, it's still one session — we try to send the message like, "Oh, if we really helped you, please pin us so that you can always find us." And then there are just two buttons — if the person pinned it, or "no, thank you." We can't check in the WhatsApp API if the user actually pinned it, so we're experimenting with this. But with this strategy recently, we brought up our average messages per user from around 15, two or three weeks ago, to now 20.5.

01:01:13 - Brandon Hancock
Amazing.

01:01:13 - Maksym Liamin
And then based on the call we had, Brandon — because now I have a little more free time — I want to come back to recording some YouTube videos. The ones I'm going to record are about HIPAA-compliant deployments [tool:HIPAA compliance]. I'm preparing a test setup that is exactly the project we do with Andrew — one back-end which is a Python worker, the other is Python with FastAPI [tool:FastAPI], Next.js [tool:Next.js] front-end. It has a blob store and Postgres [tool:Postgres], all on Azure [tool:Azure].

01:02:08 - Brandon Hancock
That's awesome. This is going to be a beast of a video because there's actually not a ton of stuff out there. Everything, if there is something, it's a single AWS tutorial where they just kind of talk high level and just point at services. Or it's just two guys talking back and forth. But nothing was like boom, boom, boom, boom. So I think this is something people would actually really like.

01:02:50 - Maksym Liamin
I needed to — I couldn't really find resources. The courses were too high level and not really practical. Especially once you have the service set up, like how you can actually check if they communicate to each other, especially once it's all private. You cannot even look into it from your local machine. And then how you test that your Docker [tool:Docker] is actually good for this kind of deployment. And you need to specify the arguments a special way when you deploy Next.js in Azure — you're better off not using PNPM or anything like that, but just go with NPM, or you have big troubles. And all this kind of stuff — I haven't found research that tells it.

01:03:53 - Brandon Hancock
▶ I can't remember how you were recording your videos — I think it was Loom [tool:Loom]. I would check out Tella.tv [tool:Tella.tv] — T-E-L-L-A.tv. You can add clips, and it's almost like an editing and recording platform all-in-one. A lot of people use it to avoid getting a video editor. I think you'll like the fact that you can record in clips, because yours is going to be a monster of a video.

01:04:19 - Maksym Liamin
Yeah, I will check it out, because I already ran out of my Loom subscription on all my 20 Google accounts, so I was thinking about recording just in OBS [tool:OBS] and then cutting it all myself in Premiere [tool:Adobe Premiere], but yeah, if I can do it all in one place, it would be great.

---

<!--SEGMENT
topic: Jake's Reddit Sentiment Analysis Tool Demo
speakers: Jake Maymar, Brandon Hancock, AbdulShakur Abdullah
keywords: Reddit API, PRAW, Supabase, Redis, GPT-4o Mini, sentiment analysis, bulk processing, semaglutide, Ozempic, Wegovy, healthcare, Cursor, Windsurf, Claude Code, TypeScript any errors, ESLint, project rules
summary: Jake demos a Reddit sentiment analysis tool targeting healthcare/pharma use cases (semaglutides, Ozempic vs. Wegovy comparison), built with Supabase, Redis, GPT-4o Mini, and the Reddit API via PRAW. The discussion covers bulk sentiment processing, cost efficiency, and vibe coding pitfalls — specifically, using "explain" before "fix" for ESLint TypeScript errors, and setting project rules to avoid TypeScript `any` types.
-->

01:05:20 - Jake Maymar
So first, I love your shirt.

01:05:45 - Jake Maymar
Love the ADK demo. That's awesome. And very excited about the Google announcements. I totally agree. I think something really big is coming.

01:06:08 - Jake Maymar
I was talking with some other friends about — we're all basically doing AI consultancy — and what's missing is something like SEO. A standard, you know, like I can point to this thing and it's going to not have any hallucinations, it's not going to drift, it's repeatable, it's standard and repeatable. So you can just basically set it and essentially forget it. And I think Google is probably the closest to this.

01:08:35 - Jake Maymar
I've been vibe coding and using AI to code and getting into a lot of issues that I did not expect. But I found this unlock that might help other people. Originally I was having issues — a perfect example is unexpected `any`, right? ESLint, fixing ESLint errors. And most of the time, it does a great job. But my project has gotten really, really complicated. And so changing those, auto-changing those unexpected `any` errors actually changes a tremendous amount.

01:09:39 - Brandon Hancock
<Q>So you're saying you're having your agent fix something, instead of just saying "fix it," you're like "explain it," then fix?</Q>

01:09:47 - Jake Maymar
<A>▶ If you say "explain" and then just paste in the error, it just streamlines the whole process and almost always solves it. It's amazing because you read through it and you're like, yeah, that's exactly what I was thinking you were going to do. Go ahead and do that. Or you read through it and you're like, no, no, no, this one has a different type or there's another error. And the reason I bring this up is I had one that had like 20 unexpected `any`s. At first I just let it fix the whole thing. And of course, it massively broke my system. Then I went back and fixed each one individually and it couldn't do it. It kept having all sorts of interconnected errors.</A>

01:11:23 - Brandon Hancock
▶ One other thing — I think potentially setting project rules to ask the agent to avoid using `any` at all costs, unless it's absolutely necessary. There's a retroactive solution and there's a proactive solution.

01:11:52 - Tom Welsh
Sorry, you definitely do, because that's one of my rules — I was sick and fed up of `any`s in my TypeScript. So yeah, I put that in my rules. And then it probably gets 95% of them.

01:12:07 - Jake Maymar
I need to go back and put my rules in because I had rules. I was using Windsurf [tool:Windsurf]. I was using Cursor [tool:Cursor]. I was using Claude Code [tool:Claude Code]. And Claude Code's odd. It's a very strange thing. Is anyone using Claude Code at all?

01:12:21 - Jake Maymar
It tends to overdo it. Like, you have to constantly stop it. "No, no, no, stop. Don't code. Tell me the plan." And it's harder to set up rules. So I've had all these rules with Claude Code, and it kind of ignores them.

01:12:25 - Jake Maymar
I started using Windsurf again because of the OpenAI acquisition. I figured, oh, well, maybe it's going to get better.

01:12:40 - Jake Maymar
I didn't realize Cursor was evaluated at $10 billion. I had no idea. That's insane.

01:12:46 - Jake Maymar
Windsurf is $3 billion. Cursor is $10 billion.

01:15:14 - Jake Maymar
So we did a big pitch and another big pitch and another big pitch. And it's definitely accelerating. It's gotten to the point that I'm kind of panicked, because my demo was first. I have a whole bunch of POCs. Some of the stuff is really rock solid and some of it just isn't. Unfortunately, they really liked the Reddit tool.

01:17:47 - Jake Maymar
So, semaglutides — I just basically added a whole bunch of semaglutides together. This is just three, but you can add as many as you want. When you go into it, it loads in posts. The posts are all pre-tagged. You can go to themes here, and you can add in any category you want. So we'll just add in diabetes. But you can get really specific. This is a prompt, so you can actually say "diabetes, A1C, people that only like broccoli" and see what comes up. And what I have on the back end is it actually refines the prompt into something that's actually usable.

01:19:26 - Jake Maymar
So it's Postgres [tool:Postgres]. I'm using Supabase [tool:Supabase], but I'm also using Redis [tool:Redis]. Redis for basically the caching and then Supabase for the long term. This is just the Reddit API [tool:Reddit API] with PRAW [tool:PRAW]. I don't have any authentication, and I'm just using OpenAI [tool:OpenAI] — GPT-4o Mini [tool:GPT-4o Mini]. And 4o Mini is essentially free at this point. So you can run this thing — it does like thousands of posts.

01:21:40 - Brandon Hancock
<Q>Does each result then get passed over to OpenAI for a quick sentiment analysis and get labeled? What's actually happening?</Q>

01:22:10 - Jake Maymar
<A>I was originally doing that, and then I started doing bulk. And then I also started using bulk to do the queuing, the job. I'm doing bulk posts, and I'm also grouping those. I'm using Regex and a couple other tools to group posts together and then bulk those, because that seems to go faster that way.</A>

01:22:55 - Brandon Hancock
<Q>Is there a cost to run those bulk operations?</Q>

01:23:00 - Jake Maymar
<A>The entire thing is running free. Everything in the sandbox is built local. So I have open-source Supabase, open-source Redis. But this is running on the cloud Supabase — it's just a lot slower. And on the cloud Redis, but it can't handle the same amount that I'm running locally.</A>

01:23:37 - Jake Maymar
So now I want to compare Ozempic to Wegovy. So I put in Ozempic and want to compare, and we'll just do Wegovy, and then we'll compare. What this does is a sentiment analysis between these two things. I have pain and anger, solution request, advice request, money talk, side effects. But I can also put in custom categories, and it will compare the categories to the subreddits.

01:26:29 - Jake Maymar
I'm normalizing the data because Wegovy has a much smaller audience than Ozempic. Ozempic is like 119,000 and Wegovy is like 8,000. So what I'm doing is normalizing the data so you can kind of see comparisons.

01:27:17 - Jake Maymar
If you want to see themes — this is actually probably the coolest part. You can see what's basically common themes between Ozempic and Wegovy, but then what's also neat is the Unique stuff. Ozempic was really focused around weight loss and exercise, and actually focused around clinical studies and data science, which I thought was really interesting.

01:28:27 - Jake Maymar
Money Talk — it's interesting that people talk more about Money Talk on Wegovy than Ozempic.

01:28:50 - Brandon Hancock
▶ No, this is amazing. I'd love to see where this keeps going. And I'd love at some point, if you wouldn't mind sending me over some screenshots — I would be curious to see what people are talking about in agent land, LangChain, ADK — see if there's any unique insights.

01:29:20 - Jake Maymar
I'm really looking forward to getting ADK in this for sure. Because the agent flow — it's problematic, but I really simplified a lot of it. I think that was kind of the key because it was really, really slow.

---

<!--SEGMENT
topic: Michal's WhatsApp Conflict-Resolution Bot and Business Model
speakers: Michal Simko, Brandon Hancock, Jake Maymar, Paul Miller, Marc Juretus
keywords: WhatsApp, Twilio, Cloudflare Workers, Supabase, Drizzle ORM, Claude 3.7, sentiment analysis, conflict resolution, divorce mediation, non-violent communication, B2B partnerships, marriage counselors, Oracle, BANT
summary: Michal introduces his WhatsApp-based conflict-resolution bot (via Twilio) that mediates communication between divorcing couples by rephrasing heated messages. The group discusses go-to-market strategy, recommending B2B partnerships with therapists and marriage counselors over direct-to-consumer, applying the BANT framework to validate the opportunity. Jake suggests certification against a communication framework to increase institutional adoption.
-->

01:30:02 - Michal Simko
I apologize for joining late, but I started the job at Oracle [tool:Oracle]. And really, it's about ecosystem development for what they call high-techs — tech companies in growth stage. I'll be kind of a technical pre-sales and salesperson in one, trying to understand where there are opportunities for agentic solutions and also for their cloud. Essentially you have to sell the whole thing from all the way from GPUs to Gen AI use cases.

01:31:43 - Michal Simko
I've been coding like crazy. I had a call with Maksym and he gave me a bit of a slap — "just publish it, just put it in the cloud, stop overthinking."

01:32:14 - Michal Simko
I'm progressing. I have, oh gosh, Bastian gave me some really cool insights. I had a very cool call with him. I think it's ready to be sent for testing.

01:33:09 - Michal Simko
Yeah, so I want to be — because it's through Twilio [tool:Twilio] and WhatsApp [tool:WhatsApp], right? So there is no — the interface is actually WhatsApp. So I put things on the workers on Cloudflare [tool:Cloudflare Workers], and the database is on Supabase [tool:Supabase] now. For now, it's only PL/SQL, so there's no vectors. And I created dev and prod environments, and then I implemented Drizzle [tool:Drizzle ORM]. And I've gone away from Claude 3.7 [tool:Claude 3.7] thinking — I was doing some stuff with thinking on and some stuff with none.

01:34:27 - Brandon Hancock
Marc hadn't heard about the app you're building. Could you give a quick recap?

01:34:48 - Michal Simko
<A>Yeah, so it's basically a WhatsApp agent or bot for now, which the idea is to intermediate — basically conversations that can be in some use cases conflictive. I'm starting with people who are either going through divorce or have gone through divorce and they don't want to communicate directly with each other. They want to have some neutral kind of steering bot in the middle, which does what? It either can clarify — because these people are looking to organize, let's say, kids being picked up from school, logistical problems — or there's a sentiment analysis that I also implemented this week. And so if the person sends a heated message, the bot would either clarify if it needs more information, or create a well-phrased and friendly message to pass on to the other person. So two people talk to each other, but through a bot.</A>

01:36:32 - Brandon Hancock
▶ Real fast, just like a business idea — if I was approaching this from a business aspect, I would not go directly to consumer. I would basically do all partnerships or all affiliates. So I would only work with actual therapists and have this be a tool they recommend. Because they're going to every day see potential customers of yours. Even if they got 50% of that, like you're golden because they're just giving you customers for free.

01:37:46 - Michal Simko
One use case — two people I'm working with on this are one psychologist and one coach. And so they already have these, they already speak to couples that have these problems. The other one is what you were saying, AbdulShakur — the law firms, for smaller cases and things that can be solved outside of the judicial system.

01:39:45 - Brandon Hancock
▶ Yeah, just like marriage counselors — that would be the play. They're already paying money to see a marriage counselor. So they're already in pain. Budget — they're paying a lot more for that counselor. Authority — it's them. Need — they're clearly in need. Timeline — they want it fixed now. So every box is checked. And yeah, I mean, this is a beautiful app, beautiful use case. Genuinely, there's no reason this is not a 10K, 20K, 30K a month app. Even if you got 1,000 at $20 a month — dude, I buy Oracle.

01:41:14 - Jake Maymar
If you can get certified or some sort of certification around your app, so that it guarantees that the communication will always stay basically at this mediation level — that could be really cool. Because once you have it certified, then therapists are like, we're just going to use this as the standard.

01:44:11 - Michal Simko
Yeah, I was thinking of using non-violent communication [tool:Non-Violent Communication] as the book — as one of the knowledge bases. But yeah, certification — I need to think about it, like what could be the framework that it complies to.

01:46:00 - Paul Miller
I think the opportunity — you look at the industries that gain, rather than directly challenging someone who makes their money from giving that advice. Who operates in that space? That's where your idea on the law firm was good, because they don't want to offer that kind of service. This is a value-add icing on top kind of recommendation. So there's a commercial incentive for them to add icing to what they already offer.

01:47:00 - Paul Miller
I think about my sister — she's gone through a horrendous divorce, and her husband's a narcissist. I said to my sister, just put all communication through AI, and set yourself up as a manual little bot, and translate it. She's kind of hard-coding what you're going to do as an app.

01:47:30 - Michal Simko
It's funny — I spoke to these guys who actually help couples go through these traumas. They say that this is quite common. They would have like a proxy — "just speak to my friend," and this friend then communicates with that ex-spouse. So people already look for these solutions. That's where there'll be urgency.

---

<!--SEGMENT
topic: Closing: AI Model Speed Research, Podcast Recommendations, and Wrap-Up
speakers: Brandon Hancock, Juan Torres, Michal Simko, AbdulShakur Abdullah, Paul Miller
keywords: AI model speed benchmarks, diminishing returns, Replit, Brett Weinstein, Devin AI, Greg Eisenberg, Google I/O, Tella.tv, CodeRabbit, Next.js, content creation
summary: Juan shares a published analysis on AI model problem-solving speed doubling every seven months, with a measured outlook on diminishing returns. Brandon recommends a podcast featuring the Replit founder and Brett Weinstein on AI futures. Bastian mentions CodeRabbit as a code review tool for a future demo. The session closes with Brandon previewing upcoming content: voice agents, video generation, and multimodal building blocks.
-->

01:53:02 - Juan Torres
Hey folks, this is Juan. Yeah, just working on the data engineering component — it's been a hassle just because I'm working with AWS [tool:AWS] and the permissions and the policies. I'm contacting AWS specialists to help me out, figure out why I can't detect my DAG files. But nevertheless, I also published an article.

01:54:02 - Juan Torres
Basically an analysis on a paper that tries to see the speed at which models are able to solve problems based on a time lapse. And essentially this article tells us that on an average of seven months, the speed at which these AI models have been able to increase their time to solve issues two-fold has been of seven months. This article we reviewed with the machine learning group in San Diego.

01:54:53 - Brandon Hancock
<Q>So extrapolating out, what happens next? What happens in seven months from now?</Q>

01:55:00 - Juan Torres
<A>I don't think there's going to be a continuation of the doubling down on the time it takes to solve issues. I think there's going to be the law of diminishing and negative returns kicking in based on the methodologies that each time a model gets optimized. I do have a more materialistic and pessimistic outlook. But I do think that there may be breakthroughs that are going to shatter my premises.</A>

01:55:43 - Brandon Hancock
▶ If you're looking for a podcast this week — this guy created Replit [tool:Replit], this guy, serial entrepreneur, just genius. Brett Weinstein [link:podcast featuring Replit founder and Brett Weinstein], if you haven't ever heard him speak — some people are geniuses. You basically have a super optimist — the Replit guy, all in, there's only great things coming. And obviously he's on the good side of it too because his company's worth billions. And then Brett is more pessimistic. So it's just like, I love those conversations when it's conflicting views and then them elaborating it.

01:58:00 - Michal Simko
The founder from Devin [tool:Devin AI] — he was on Lenny's Podcast [tool:Lenny's Podcast]. That's pretty nice. It's a cool podcast to listen to.

02:00:02 - AbdulShakur Abdullah
Have you seen that podcast format where they sit there and they just start trying to quickly build something? I could see you doing that.

02:02:15 - Brandon Hancock
The only podcast — Greg Eisenberg [tool:Greg Eisenberg] — his are like more that style. I would 100% want to do that style. Outside of that, I just love to watch it. My First Million [tool:My First Million podcast], All In [tool:All In podcast] — those are my like, I love Saturday mornings, a good coffee and then All In. That's how I like to start the weekend.

02:01:51 - Bastian Venegas
I actually just wanted to show CodeRabbit [tool:CodeRabbit] as a review tool, but I think considering the time, I can do that next week.

02:01:52 - Brandon Hancock
Bastion, I've heard about it. I've seen one small demo, but that was like a while ago, so I can't even imagine how good it is now. Would love to see that, to do a demo, because I think it would be super helpful for a lot of the developers.

02:02:01 - Brandon Hancock
▶ All right, well, I gotta run. Awesome Tuesday, guys. Voice agents coming out. I'll try and do something with videos for you guys as well, just so you can understand — boom, we have text, video, audio — trying to do all the things. Just did the image as well. Trying to hit all fronts so you guys can fully understand all the foundational building blocks of what's available right now. And then after that, I'm gonna start diving into a lot more use cases.

02:02:50 - Paul Miller
We've got a clash next time. Day one of Google I/O [tool:Google I/O] is in seven days from now.

02:02:58 - Brandon Hancock
Oh, it is? Okay. Well, hey, I will take a pause from the conference, hop on the call. Yeah, we'll figure it out. Thanks for the reminder. All right, see you guys. Have a great one.

---

=== UNRESOLVED SPEAKERS ===

None. All speakers were resolved via context or passed through unchanged where no alias map was provided. Note: "Lucas cooper-Bey" appears in the transcript as the speaker who is also addressed as "Paul" by Tom Welsh at 00:01:26 — this may indicate a name discrepancy not resolvable from the alias map alone. Passed through as transcribed.