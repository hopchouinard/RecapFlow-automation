=== SESSION ===
date: unknown (transcript timestamps span ~04:59–02:14:00)
duration_estimate: ~2 hours 10 minutes
main_themes: Microsoft Copilot vs. GitHub Copilot confusion in enterprise settings; SpecKit extension for vibe-coding governance; ShipKit launch preparation and feature overview; Supabase staging/production environment cloning; Google ADK agent orchestration patterns; RAG pipeline architecture and PDF chunking challenges; GPU/EC2 horizontal scaling for LLM inference; community knowledge-sharing and deployment cost management

---

<!--SEGMENT
topic: Copilot Naming Confusion & Enterprise AI Adoption
speakers: Patrick Chouinard, Marc Juretus, Paul Miller, Al Cole
keywords: Microsoft Copilot, GitHub Copilot, IntelliJ, Spring Boot, Next.js, SpecKit, vibe coding, RAG, enterprise AI, prompt engineering
summary: Marc and Patrick discuss the confusing naming overlap between Microsoft Copilot (productivity/office suite) and GitHub Copilot (code assistant), both Microsoft products. The conversation broadens to enterprise AI adoption challenges, including naive executive expectations around vibe coding, the risks of shadow IT from ungoverned AI-generated code, and the gap between what non-technical users think they know about AI versus reality.
-->

00:04:59 - Patrick Chouinard
Hi, Marc.

00:05:06 - Marc Juretus
What's up, Patrick?

00:05:12 - Patrick Chouinard
Just managed to get back from work in time for the call this week, finally.

00:05:19 - Marc Juretus
Thought of you yesterday — my boss wants to start considering using Copilot [tool:Microsoft Copilot]. So I had to kind of explain that there's a Microsoft Copilot where it's the regular one, as opposed to GitHub Copilot [tool:GitHub Copilot], even though I heard that's owned by Microsoft as well.

00:05:37 - Patrick Chouinard
They're both Microsoft products. It's Copilot and GitHub Copilot.

00:05:42 - Marc Juretus
▶ The naming convention is extremely confusing.

00:05:47 - Marc Juretus
I was using it — like to ask, what is it? Ask, edit, and agent mode. So it's interesting. I'm using IntelliJ [tool:IntelliJ], so we've got to tell them how they can apply it to their day-to-day. It works pretty well for the most part.

00:06:04 - Patrick Chouinard
▶ Yeah, actually, I wouldn't develop a huge application using it, but for day-to-day stuff and as an accelerator, yeah, it does the job. Actually, if you couple it with SpecKit [tool:SpecKit] from GitHub, it gains a whole lot of capabilities.

00:06:25 - Marc Juretus
Yeah, I was playing around with how you can highlight and chat against your code, and it's interesting.

00:06:40 - Patrick Chouinard
Yeah, actually, that's going to be part of stuff I'm going to share tonight. The idea is — because last week I mentioned how I wanted to automate some of the admin stuff surrounding development, like all the issues, the pull requests, the commits, that most vibe coders have no idea how to do. And now we have a whole bunch of vibe coders doing those, so if we don't want to get into shadow IT hell, we have to find a way to automate those things. So I'm thinking about extending SpecKit so it manages that part as well, not just the specifications.

00:07:19 - Paul Miller
<Q>Hey, Patrick, were you talking about your workplace that's gone vibe crazy? I really couldn't imagine — it's a really exciting, cool thing, but I can see the stress in having a whole user group playing around with those tools. How's your sanity?</Q>

00:07:42 - Patrick Chouinard
<A>Let's just say that stress level is not low, but there's a whole lot of opportunity though.</A>

00:07:51 - Marc Juretus
I'm sure you hear a lot of "oh, that's cool" — hey, no, let's not do "that's cool" before you get into some trouble here. I was telling Patrick, my boss is like, let's start using GitHub Copilot at my job, but the first hurdle is we have Microsoft Copilot, but we don't have the GitHub version. So I had to explain that's not a code assistant — that's for day-to-day PowerPoint slides, rewriting your email, this, that, and the other. So I was playing around with it, and I was creating some Spring Boot [tool:Spring Boot] apps and some Next.js [tool:Next.js] stuff. It writes it pretty well for the most part. It's just another tool.

00:08:30 - Patrick Chouinard
When you create an office suite, an AI assistant, an AI development tool, and give them all the name Copilot, don't be surprised when customers are like, what the hell is that?

00:08:42 - Marc Juretus
I mean, the one cool thing it does do is — I can see a usage with the regular Copilot where you can create an agent and have a RAG against a 20-page document and say, okay, for my area, this is how we handle PTO, downtime, disaster recovery. Ask the agent, and then you can assign it to a specific user's ID, and only they have access to it. So I could see a very good use case for that part of Microsoft Copilot, but it's not the full-blown one that I think they think it is.

00:09:14 - Paul Miller
Yeah, within a corporate environment, you kind of don't want them — you want guardrails that are quite tight about what they can do, what they can't do, how they can access their corporate email without blowing it apart and missharing it. It's a lot harder and more complicated than they think, and these are naive users — a little knowledge is dangerous, it sends a lot of scary thinking.

00:09:46 - Marc Juretus
The funny thing I've noticed is what they think they know about AI, from what I've learned, is not truly AI. I'm giving basic, advanced, and expert training on prompt engineering.

00:10:06 - Patrick Chouinard
The number of people that get into the advanced course saying "oh, I already know the basic stuff," and they have no clue whatsoever, is impressive.

00:10:22 - Paul Miller
Look, I used to do a lot of work as a CIO and in other senior IT roles in corporates, and that side I don't really miss. Everyone thinks they can do that role, but it's blooming hard. Managing expectations, keeping the environment stable, moving the enterprise forward — this is tough stuff.

00:10:49 - Patrick Chouinard
You want to know what the scariest sentence actually is? I heard it last week. It's a C-level individual telling you, "Oh, we have to do more vibe coding. I actually vibe coded a CRM in three hours yesterday."

00:11:06 - Paul Miller
Yeah, right. Well, we should move the whole corporation onto that platform.

00:11:13 - Al Cole
Ship it. No, ship it.

00:11:20 - Patrick Chouinard
▶ I'm going to ship that thing under one condition — if you guarantee that I'm going to get paid to fix the problems afterward. So yeah, bringing those people back into reality of where do you actually create stuff, and how do you do that safely?

---

<!--SEGMENT
topic: SpecKit Extension for Vibe-Coding Governance
speakers: Patrick Chouinard, Marc Juretus, Al Cole, Paul Miller
keywords: SpecKit, vibe coding, GitHub issues, pull requests, commits, shadow IT, Jira, agile, waterfall, LLM hallucinations, intent-driven specification
summary: Patrick outlines a plan to extend SpecKit to automate the software development administrative tasks — issue creation, pull requests, and commits — that vibe coders typically skip, creating shadow IT risk. The group debates whether SpecKit's spec-first approach is too waterfall, and Patrick argues that sufficiently small, well-scoped specs can remain agile. Al raises LLM hallucination concerns for this use case.
-->

00:12:06 - Patrick Chouinard
So now, like you do in chain-of-thought, you have to separate a problem into individual chunks. I'm taking care of one very individual chunk: how do you get vibe coders to actually do issues, commits, and pull requests correctly without having to teach them as DLC?

00:12:26 - Al Cole
Now, I think we're into the LLM hallucinations area. I'm not sure how well that's going to go for you.

00:12:34 - Patrick Chouinard
<A>Well, I'm thinking — I'm playing with SpecKit and actually thinking of extending it, because what SpecKit is, is basically you give an intent and it starts creating specifications. Well, why not actually define the number of issues into which it should be split? Provided with templates for either Jira [tool:Jira] tickets or GitHub issues [tool:GitHub Issues] or things like that. My idea is not to get them perfectly as if they were a software engineer, but if I can get them like 50% there, it's already a whole lot better than the zero percent there they are right now creating code that has to be managed somehow.</A>

00:13:27 - Marc Juretus
<Q>Isn't SpecKit too much waterfall?</Q>

00:13:36 - Patrick Chouinard
<A>It depends. It is waterfall for implementation of the specification that you create, but if you create it small enough and you split it into enough parts, it can be pretty agile actually.</A>

---

<!--SEGMENT
topic: ShipKit Launch Overview & Session Format
speakers: Brandon Hancock, Paul Miller, Ty Wells
keywords: ShipKit, coaching calls, RAG template, Next.js, Supabase, Vimeo, MCP server, Cursor, Google Cloud, staging environment, production environment
summary: Brandon Hancock joins and reframes the session as a question-and-answer format due to time pressure from the imminent ShipKit launch. He briefly previews ShipKit's support structure — weekly coaching calls, an AI chatbot over course content, per-module discussion threads — and mentions switching video hosting to Vimeo. Paul Miller raises the idea of an MCP server integration so developers can query ShipKit content directly from Cursor.
-->

00:13:55 - Brandon Hancock
Guys, I gotta hop in. Today is going to be a shorter call. I have so much work to do. What I was hoping to do today is — normally we go round robin — but what I would love to do today is make today more question-based. And then if you guys want to keep going after all questions are answered, would love for you guys to keep going. We are in the home sprint for ShipKit [tool:ShipKit]. I can't tell you how excited I am for literally the two seconds after it's launched. So I'm going to take a small coma for 12 hours and then bounce back.

00:14:52 - Brandon Hancock
So what we'll do today — quick heads up — I think the best thing to do today is to just drop questions in chat. That way I can make sure everyone gets their questions answered. I can definitely stay until 7 today, and then we'll go round robin, but just at 7:05, I gotta hop off, just because I have to get back to coding. But you guys can keep the party going.

00:21:01 - Brandon Hancock
So one of the main things I want to do with ShipKit is provide as much support as possible. We are going to have the weekly coaching calls. For the first six weeks, I think we're doing three a week just because I want everyone to hit the ground, absolutely crush it, see what you guys are stuck on, and just keep recording modules and improve it — just to make ShipKit literally the best project that's ever existed.

00:21:27 - Brandon Hancock
So one is just like general AI chatting. Like, coming in here and just asking any module — like, hey, what does Brandon say to do for deploying? It would point you to the right course. Or if you're on a specific page, you can always chat with that specific module.

00:21:55 - Brandon Hancock
I ran into some issues with video streaming speeds, so I had to switch to Vimeo [tool:Vimeo]. So I'm in the middle of fixing it.

00:22:59 - Paul Miller
<Q>As part of the subscription — is there an MCP server [tool:MCP server] option?</Q>

00:23:04 - Brandon Hancock
<A>Well, right now, everything is done through just Git, meaning when you Git a project, it already has all the AI docs, all the prompt templates and everything. I've not looked at setting up an MCP server to do anything with MCP yet. Is there a concrete example that you were thinking of for MCP?</A>

00:23:25 - Paul Miller
Well, I just think some of the tool sets that I work with, the best alignment that you've got is if you can add an MCP into the MCP path. And so as you dynamically update questions and answers and best practice, then that's constantly linked using the MCP path.

00:23:49 - Brandon Hancock
<Q>So you're saying from Cursor [tool:Cursor], allow people to do queries against the course?</Q>

00:23:58 - Brandon Hancock
I really like that. That's pretty cool. Yeah, definitely don't have that yet, but that would be a really cool project and something to add on.

---

<!--SEGMENT
topic: Google Cloud Cost Management & Auto-Scaling
speakers: Brandon Hancock, Paul Miller
keywords: Google Cloud, auto-scale to zero, RAG, Cloud Run, bill shock, token usage, Claude Sonnet, cost management, Supabase, budget alerts
summary: Paul Miller raises concerns about unpredictable Google Cloud billing when building and reselling applications. Brandon explains ShipKit's design philosophy of auto-scaling to zero to minimize baseline costs, discusses the trade-off between 30-second cold starts and avoiding large unexpected bills, and advises users to match model choice (e.g., Claude Sonnet Max vs. lighter thinking models) to their cost sensitivity.
-->

00:24:25 - Paul Miller
<Q>The Google — you might already have an answer for this, but a lot of us, when you say "we'll just put it in Google Cloud," how do we get comfort that it's not going to — oh my God — we're going to get hit with bill shock? It's predictable. Because if you're going to resell it to other people, you're going to stick your credit card on there.</Q>

00:24:41 - Brandon Hancock
<A>Yeah. The main ways to avoid sticker shock — I literally will be doing an email on this on Thursday to cover this exact question. The main thing I wanted to call out is when it does come to Google Cloud [tool:Google Cloud], I think it really comes down to usage. For example, if you upload a gigabyte file and put it through RAG, I think it costs anywhere from 60 to 80 cents to process that. So obviously if someone puts in a terabyte, they're going to get a higher bill than someone who does a 20-megabyte project.</A>

00:25:30 - Brandon Hancock
▶ The way we have designed everything — and I'll explain this more on Thursday — we've designed everything to auto-scale to zero. Because that's one of the biggest ways to add cost. For example, running some of these Google Cloud instances, if you do it 24/7, it's $50–$60 a day. You do that for a month — oh my God, you just accidentally had a thousand-dollar bill. So everything auto-scales to zero, which means yes, when you upload something to the RAG processor, it's going to take an additional 30 seconds to kick on, but that's just the way to save you guys hundreds of dollars. So 30 seconds or $100 — I think you guys would pick 30 seconds.

00:26:30 - Brandon Hancock
▶ Whenever it comes to token usage, there are multiple strategies I'll cover. Some people who just want speed are happy to use Claude Sonnet Max [tool:Claude Sonnet] the whole way through. If you are very price-sensitive, you can use just the regular thinking models and take on smaller tasks. You have to play at your own comfort levels. If you want speed and don't mind the money, go for it. If you're very cost-sensitive, then you have to take a different approach.

---

<!--SEGMENT
topic: Supabase Staging & Production Environment Cloning
speakers: Brandon Hancock, Ty Wells
keywords: Supabase, staging environment, production environment, edge functions, UUID mapping, database migration, db seed, setup scripts, point-in-time recovery, feature branches
summary: Ty Wells asks about cloning a Supabase instance to create a feature branch, noting that point-in-time recovery covers schema and data but not edge functions or users, and that UUID mismatches complicate data porting. Brandon walks through his approach of codifying environment setup via migration scripts, seed scripts, and bucket/permission setup scripts, acknowledging that migrating real production data between environments remains a manual, careful process.
-->

00:15:18 - Ty Wells
<Q>Yeah, really — my question is about cloning a Supabase [tool:Supabase] instance. Supabase has a point-in-time recovery option, but that's schema. You can get data as well, but what you cannot get is edge functions or users. I think those are really the only two. So I went through a process scripting out to gather and pull all of that data, but then you've got UUID issues. I'm trying to see if anybody has any thought on that. Ross is writing an agent to do what I did, except I still have to match that data back to the users — some sort of cross-mapping table. I wonder if anybody's been there.</Q>

00:16:14 - Brandon Hancock
<A>Yeah, this is one of the hardest parts — where most people get stuck is they're like, cool, I built a local app on my computer, cool, I deployed it to the cloud, ta-da, I'm done. And that's the start of your real-world journey as building a production application, because you really need to create a staging environment and a production environment.</A>

00:17:01 - Brandon Hancock
So the way I have it is I create a collection of setup scripts. What you end up doing is you codify everything so that you don't have to manually recreate buckets, and you don't have to manually recreate all the different permissions. You just spin up a few setup scripts, and that way whenever you start working in a new environment, even if you have to blow everything away, you just literally run like three commands: `npm run db migrate`, pull your new database to match your current schema, then run a few setup scripts to create all your buckets, deploy your edge functions, and then run `npm db seed` to seed your database with some fake data.

00:19:34 - Brandon Hancock
I think you're already doing that, but you're just in the hard part now — what do I do with my data? How do I actually clean it for the two different environments?

00:19:38 - Ty Wells
Well, really port it over so that I could use real data, because there's real data in there, and I know that data is cleaned already, so I want to make sure. I was just hoping there was an easier way, but apparently there's not.

00:20:05 - Brandon Hancock
▶ Yeah. There are some scripts you can make that copy data from one environment to the other, but you just have to do a bunch of checks to make sure it's what you want. That is the hard part with working in two different environments.

---

<!--SEGMENT
topic: Google ADK Agent Orchestration Patterns
speakers: Brandon Hancock, Jahangir Jadi, AlexH
keywords: Google ADK, agent as tool, sub-agents, sequential pipeline, loop workflow, phased approach, state management, structured output, root agent, delegation, ShipKit
summary: Two members ask about Google ADK agent design. Jahangir Jadi is building a multi-phase query validation and classification pipeline and asks whether to use agents-as-tools or sub-agent delegation, and whether tool-calling can be nested. AlexH is designing a multi-agent bill-of-materials quote system and asks how to manage large JSON state across agents without overloading context windows. Brandon recommends phased prompting, breaking state into small named objects, and maintaining a "digital twin" agent architecture document.
-->

00:36:48 - Brandon Hancock
So, Jahangir, I see you are working on some agent workflows. ADK [tool:Google ADK], LangChain [tool:LangChain]?

00:37:00 - Jahangir Jadi
Yeah, basically I'm creating a system where a user will enter a query, and the system is going to first identify if it is complete or not. Secondly, it is going to extract some information from it, like names and dates. And last, it is going to classify the event based on a template I'm going to provide. So what happens is I have created a flow, but my first agent works fine, but it doesn't go to the second agent. If I use the agent as tools, then it kind of works, but it does not work with fallback. Like, for example, if there is an invalid query, I want to stop that agent right there and ask the user to enter the query again.

00:38:11 - Brandon Hancock
<A>So most of this is a prompting, prompt engineering issue with ADK. ADK loves phased approaches — loves them. I cannot express it enough. So you can see here, I'm basically doing the exact same thing that you're asking about — phase one, gather information. You specifically tell it what it needs to look for and basically just say, don't proceed to the next step until you're good to go.</A>

00:38:57 - Brandon Hancock
▶ Doing phased approaches like this is an absolute game-changer. If you go look at all of the example ADK samples that ADK has provided, all of them use this. It works the best, and you can basically say, hey, ask these questions, don't proceed until we're good to go to the next one.

00:39:25 - Jahangir Jadi
<Q>Yeah, but what is the recommended way? Should I do it with the tools or should I do it the normal way with the sub-agents?</Q>

00:39:56 - Brandon Hancock
<A>So there are two options. When you want to use agent as tool — what happens is your root agent will say, hey, I need help on this, and it instantly treats your agent like a function. It's going to pass over a query, this agent's going to do whatever it needs to do, and instantly return the results back to the agent that called it. What's different in delegation land is when you say, hey, I have all the information I need, now I need this sub-agent to take over the process. This agent now becomes the main controller agent, and as you continue to interface, you're talking to this sub-agent going forward — unless you provide instructions to say, hey, delegate back under this certain condition.</A>

00:42:43 - Jahangir Jadi
<Q>If we are using a tool, can that tool call another tool?</Q>

00:42:50 - Brandon Hancock
<A>Like tool inception? Yeah, that's fine. If you have a root agent that does agent as tool, that sub-agent or tool agent can do a tool request. I just don't know if that agent can do an agent-as-tool request two levels deep — I don't think we can do that, but I've never tested it. But straight-up tool calls, like calling a piece of code — yes, that agent tool can do it. I've 100% done that.</A>

00:49:12 - Brandon Hancock
So AlexH, you're building on the ADK framework with multiple LLM agents working and updating a quote. Quotes can contain up to 100 line items, and the JSON schema has multiple fields per line. <Q>Do you recommend using ADK state to maintain this across agents, or artifacts?</Q>

00:49:55 - AlexH
Right now I have each agent working in isolation. They're going from input to output, but now I'm trying to hook them up together and they need to persist and maintain the status of this quote. The quote can be like a hundred line items — like a bill of materials — and I'm trying to figure out how to maintain state around the quote so that as each agent accesses it, there's a persistent understanding of where the status is.

00:51:06 - Brandon Hancock
<A>The way I like to work with state and ADK is I like to break things down into smaller manageable components. If there are a hundred items, the first question I would ask myself is: is there any way we could break down a hundred different rows into sub-categories? I would have, say, an exterior bill of materials object in state, and I would have a structured output for it. Then each agent would work on just that one final part, and towards the end, you could have a composer agent that would look at all the different states and put them together in one final version.</A>

00:53:00 - AlexH
It's mostly in design. My fear right now is the JSON — if you look at the JSON doc being produced by any given one, in testing I'm giving it a fraction of what it's going to have to manage, call it like 50%, and trying to pass those around and maintain them — it's more in design of trying to figure that out without overloading the context window of any individual LLM where it just goes haywire.

00:53:10 - Brandon Hancock
▶ That's the key reason why I say break stuff down — the second you have too many instructions back to back, it will just not perform as expected. It might do four out of seven instructions. Anytime this one agent's getting a little too complex and I couldn't just do a simple checklist to check things off, I know I need to break things up.

00:56:26 - Brandon Hancock
▶ One thing I really recommend when you're doing anything that is working with multiple agents: build a digital twin document of your entire workflow. It calls out what all the agents do, what state they read, what state they write, what models they use. When you make a change to state for agent one, it instantly knows by looking at this document — oh, if you change state for agent one, this is going to completely destroy agents three, four, and five down here. Because if you just try doing agent development and building agents one at a time, the second you get to complex state management, things are just going to ripple and break.

00:58:23 - Brandon Hancock
<Q>Is that MD file — are you doing that manually, or is that like a Cursor agent writing that in the background?</Q>

00:58:26 - Brandon Hancock
<A>Yeah, so this is part of ShipKit. I've never written a single line for all of ShipKit. Agents do everything. You take a screenshot of those wireframes — hey, I kind of want to build this — that instantly gets turned into that roadmap. And then as I go into building out each agent, I constantly update that roadmap. That way, it's a digital twin.</A>

---

<!--SEGMENT
topic: Google ADK Labs Recap & AI Presentation Workflow
speakers: Brandon Hancock, Al Cole, Elijah
keywords: Google ADK, Agent Development Kit, GCP, multi-agent architecture, guardrails, Gamma, Claude, spec-driven presentation, financial services AI adoption, Google Drive
summary: Al Cole shares materials from a Google ADK lab event in Boston covering mature multi-agent architectures with inter-agent guardrails and collaboration. He also describes using Claude to generate a presentation outline fed into Gamma to produce 40 slides in under 20 minutes, which he used to present to 18 financial services companies — all of whom were significantly behind in AI adoption. Brandon highlights the ADK orchestration improvements and his wish for easier Next.js integration.
-->

00:30:39 - Brandon Hancock
Al, I saw you said you attended Google Labs in Boston. And they had an ADK presentation?

00:30:51 - Al Cole
So this is an update from the one I did in the fall, Brandon. This one was actually much more mature — had multiple agents collaborating together on projects. I just wanted to share it with the team. I captured all the labs, the presentation, all that stuff. You'd need to leverage it on GCP [tool:GCP], but it was a pretty comprehensive set of labs to showcase the functionality and where they are with the maturity.

00:31:38 - Brandon Hancock
<Q>Would you say any of them are more helpful than the others?</Q>

00:31:38 - Al Cole
<A>I'd say the overview slides would be the most helpful. And then what they did — they wanted to gamify it for the group that was there, so this is all centered around a collection of games. But the keynote's going to give you an overview of the architecture.</A>

00:32:07 - Al Cole
This is definitely a maturing of where we all were back in May when I first did it. It certainly was much further along. And they even have guardrails now where, with the ADK, you can completely intercept anything going between agents and be able to control how you react to it. So just an improvement on the overall architecture.

00:32:38 - Brandon Hancock
Yeah, they are throwing so much effort at this. The core agent orchestration is becoming so powerful and so simple to set up. I am so pumped as they continue to make changes to make it easier to add into Next.js, because right now we as developers have to do more work on our side to get it to work properly in a real-world application. Getting it to where it's just a one-click button and boom, you have your ADK agents — oh my gosh, that's going to be a game-changer.

00:33:33 - Al Cole
For me, I did do a presentation last Tuesday to 18 financial service companies. They're all woefully behind in their AI adoption. But what I wanted to highlight — that was my first time going through 100% AI-driven. I did a spec in Claude [tool:Claude], asked it to generate a presentation outline of the topics I wanted to cover so that I could feed it into Gamma [tool:Gamma], and then I used Gamma to generate 40 slides. Other than maybe 20 minutes of cleanup, I had a presentation I could start rehearsing right after that.

00:34:37 - Al Cole
▶ For me, that was a validation of what you could do in terms of starting with a spec and ending with something that the entire room could engage in for a couple of hours.

00:34:40 - Brandon Hancock
I thought I saw Gamma has an API too, right?

00:34:44 - Elijah
Yeah, it wasn't leveraging it in that way, but that would be another way. I saw that in the new release a couple weeks ago. So I think that's a really interesting loop there for learning as well.

00:35:39 - Al Cole
▶ If you're pitching to financial services people, they're just not even close yet in their AI adoption.

00:36:09 - Al Cole
If you go back in the chat, you'll see I mentioned Google ADK, and there'll be a link to a Google Drive folder [link:Google Drive folder shared in chat], and then I'll put my stuff up in there.

---

<!--SEGMENT
topic: ShipKit Licensing, Target Audience & Enterprise Potential
speakers: Brandon Hancock, Patrick Chouinard, Al Cole, Tom Welsh
keywords: ShipKit, licensing, indie developer, enterprise, SaaS, freelance, RAG template, Supabase, Kubernetes, Next.js, TypeScript, asset management, risk tracking
summary: Patrick Chouinard asks whether ShipKit is licensed per developer or per enterprise team, and whether it could be used to train a class of 40+ developers at a client site. Brandon clarifies ShipKit targets individual indie developers and freelancers, not full enterprise deployments, and that derivative works built with ShipKit templates are the user's own. Tom Welsh asks whether ShipKit can help him add a risk-tracking module to an existing TypeScript/Supabase asset management system.
-->

00:27:44 - Brandon Hancock
Tom had the next question. I have an asset management system — wondering if ShipKit can take this app as-is and improve it.

00:28:00 - Tom Welsh
Yeah. So basically I've got AssetMS working quite happily and I want to create a new module for risk tracking and then bolt that into AssetMS. Using the base AssetMS as the start app, but build a completely new app to pull into it through ShipKit.

00:28:31 - Brandon Hancock
<A>ShipKit is really designed to do best with the containers it was built in — meaning Supabase and Next.js. That's the way the chat application is set up to work. If you're doing the RAG application, Python, Next.js, and Google Cloud. Obviously if you're going to be posting all those out the window and trying something completely different, your results will completely vary. However, one of the coolest things I've been recommending people to do is — if you are working with a different language or different backend — you already have phenomenal template examples, and you can just say, here's the template, it's currently designed to work with Supabase for the backend, I'm using this as a backend, please update this to work for the new backend.</A>

00:29:04 - Tom Welsh
Luckily I'm using TypeScript [tool:TypeScript] and Supabase, so I'm happy that way. My question is: I want to create a new module for risk tracking and bolt that into AssetMS. Basically using the base AssetMS as the start app, but build a completely new app to pull into it through ShipKit. You flick a switch in the settings page and bring on new functionality.

00:30:03 - Brandon Hancock
▶ Yeah, I don't see why it wouldn't — at the end of the day, it's just updating the application. The one thing you would probably want to do is break it down into a bunch of smaller steps along the way, instead of one huge task.

00:43:48 - Brandon Hancock
Patrick, are you envisioning ShipKit to be mostly for indie developers? Are you targeting more enterprise clients?

00:43:55 - Brandon Hancock
<A>My audience is like us — individuals, some doing our own things, some working at a company trying to do side projects. At this point, it is more for the indie developer to launch that production SaaS application, or for the developer who wants to do freelance work. The RAG template, for example — that one is the perfect project for anyone wanting to do real-world freelancing. A few months ago I did a huge RAG project for a client, like $10K or so, and basically all the core lessons from that just got copied and pasted into the RAG template. For full-blown enterprise, that's where it gets more confusing — enterprises are not going to use Supabase, enterprises are probably going to be doing much more deep work, they have their own Kubernetes [tool:Kubernetes] cluster — there's just so much extra stuff, and the target audience is so much smaller, so that's probably outside the scope for ShipKit.</A>

00:45:17 - Patrick Chouinard
<Q>If a client were to buy the license — if they have a hundred developers and want to tweak a version for their own infrastructure — is that one license for the enterprise or one license per developer?</Q>

00:45:46 - Brandon Hancock
<A>It's really not as much a license as it is — it's more like, hey, this is your code, go forth and build your own projects with it. The main thing is it's not like, buy ShipKit and then hand ShipKit over to a hundred friends — that's obviously not cool. But if you build something cool with the chat application and then go to sell that, yeah, it is your derivative work. It is designed for individual developers.</A>

00:47:05 - Al Cole
And that makes sense, because you've got support commitments to it, Brandon. And if you find any traction with this, you could get creative and think about an enterprise license with numbers to match that kind of discussion.

00:47:22 - Patrick Chouinard
That was my question — because next month I'm training 40 devs in one shot. So that's something you'd be ready to take on if we say, oh, we've just bought 100 ShipKits.

00:48:31 - Brandon Hancock
▶ ShipKit is designed to build real-world applications. In the age of vibe coding, you're actually moving away from needing to know exactly what a `useEffect` is. As long as you have proper context, proper working projects, and a clear roadmap and templates to help you go along the way, you can build pretty much anything. That's the goal — shipping real-world projects.

00:48:56 - Patrick Chouinard
I understood, but are you ready to teach ShipKit to a class of 100?

00:48:59 - Brandon Hancock
Hey, if there's a right price, I'm down for everything.

00:48:47 - Patrick Chouinard
I prefer to ask first than to drop that type of load without asking first. If you want to DM me, I'd be happy to learn a little bit more about what they're looking at.

00:49:05 - Brandon Hancock
▶ Yeah, we can talk offline.

---

<!--SEGMENT
topic: Mermaid Diagrams, Excalidraw & Visual Tooling in Development
speakers: Brandon Hancock, Mitch, Elijah
keywords: Mermaid, Excalidraw, Cursor, Presentify, voice memo, Markdown, diagram-as-code, client presentations, visual workflow, content automation
summary: Mitch shares a workflow tip of maintaining a live Mermaid diagram file in Markdown, updated via voice memos through Cursor, which impresses clients during live sessions. Brandon endorses Mermaid for visualizing code structure inside Cursor and demonstrates the Mermaid Chart extension. He also recommends Presentify for on-screen annotation during presentations. Elijah asks whether Brandon draws on a physical board or uses a mouse for Excalidraw diagrams.
-->

01:04:41 - Mitch
So, you know how you're saying you don't write code manually anymore. But you do make your Excalidraw [tool:Excalidraw] boards manually.

01:04:58 - Brandon Hancock
I sometimes write on a notepad too.

01:05:00 - Mitch
Yeah, and so I was like, I'm supposed to be the AI guy — what am I not doing with AI? So I was like, wait, why don't I just make a current, active Mermaid [tool:Mermaid] file, like an MD, and then just have Cursor edit that? It's been really good. You just quote the voice memo, it edits the Markdown file, does all the changes for you — do it right in front of the client.

01:05:23 - Brandon Hancock
I've been really liking Mermaid, except — I've been liking Mermaid for when I have a ton of code and I want to make a cool visual for that code, to break it down and walk it through other people. But like, my creative process — I'm struggling, I can't even put words on what I'm trying to build sometimes, and I literally have to draw a box and I'm like, okay, what happens next? Sometimes drawing is the way I get my ideas out of my head. But no, you're totally spot on for Mermaid.

01:06:34 - Brandon Hancock
▶ There's a cool tool inside Cursor — it's called Mermaid Chart [tool:Mermaid Chart]. This is the tool that will allow you to visualize Mermaid drawings inside of Cursor. With Mermaid, you get to do this inside of Cursor — when I'm trying to break down how does this code work, it's sick. With AI, you just say, hey, make a Mermaid diagram, and it creates this, and it's so easy to explain code.

01:08:19 - Elijah
<Q>When you showed the Excalidraw boards, do you draw on a real-world board? You have a pen there with you, or you're just using your mouse?</Q>

01:08:25 - Brandon Hancock
<A>Mouse is the main way I do it.</A>

01:08:34 - Brandon Hancock
▶ The other tool — all these arrows — that's called Presentify [tool:Presentify]. So if you ever see me draw on top of something, that's Presentify. It's like $10. Definitely recommend it. If you're ever trying to annotate on your stuff, it is the best tool for quickly showcasing what's happening on your screen.

---

<!--SEGMENT
topic: ShipKit Platform Architecture & LMS Integration
speakers: Brandon Hancock, Elijah, Jake Maymar, Patrick Chouinard, Ty Wells
keywords: ShipKit, RAG template, learning management system, SCORM, school.so, Vimeo, document chunking, vector embedding, course platform, GitHub repository, ed-tech
summary: Elijah asks whether the ShipKit course portal is itself built using the RAG ShipKit template, and whether the learning management system software is included as a deliverable. Brandon confirms the RAG pipeline (chunking, embedding) powers the course's AI chat feature, and that a walkthrough showing how to build a simpler version of the LMS from the RAG template is included. Elijah raises the SCORM file format standard as a significant ed-tech opportunity. The group discusses migrating from school.so to the ShipKit platform.
-->

01:09:43 - Elijah
<Q>When you showed the courses for the RAG ShipKit software — what were the courses that you're developing in there? Is that the actual ShipKit project, basically that learning structure, that learning management system?</Q>

01:10:09 - Brandon Hancock
<A>Yes. So inside of ShipKit, this is where you guys will come to learn the process end to end. In addition to that, you will hook up your GitHub repository, and this is how you'll get instant access to all the different project templates and the rest of the other examples. And then inside of each example project, that's where you'll get all the AI templates and everything else.</A>

01:11:38 - Brandon Hancock
<A>The RAG template — the RAG pre-built project — was used to build out the course platform. So all of the document chunking [tool:document chunking], embedding, and everything that you guys learn, that's the exact same pipeline I use to help you guys ask questions about the course. Inside of the course, you'll get to see walkthroughs and lessons for every single project type — chat, ADK, RAG — it's all in there.</A>

01:12:18 - Elijah
<Q>So you're not going to host your courses on school.so [tool:school.so]? They're going to be in this new platform?</Q>

01:12:44 - Brandon Hancock
<A>Correct. Just because school does not allow you to add comments on posts, they have no AI functionality. It's honestly not the best for learning. Right now, if you were to watch a module and you had a question, you had to go back to the homepage to find a post, to then drop a question, to then hop back — it's just not intuitive for learning.</A>

01:13:14 - Elijah
<Q>Are you familiar with SCORM [tool:SCORM]? SCORM is just a file format for learning management systems. I come from the ed-tech world, and I see a very significant opportunity for what you've built related to that piece. If you can import SCORM files, there are big companies in that space that can't do what you're doing. So there's a pretty good opportunity there.</Q>

01:14:04 - Brandon Hancock
<A>The whole goal of ShipKit is you guys come from all sorts of different technical backgrounds, all sorts of opportunities that I would never even think of. What I'm hoping is: give you guys the core foundation and you guys go off, take these templates, and literally launch your own real-world applications. It sounds like you have a really cool opportunity or idea — let's make it happen, man.</A>

---

<!--SEGMENT
topic: Context Management, Grok4, and Model Consistency
speakers: Jake Maymar, Patrick Chouinard, Ty Wells, Bastian, Mitch
keywords: Claude Code, context window, Grok4, Grok3 mini, Codex 2, context management, sub-agents, NotebookLM, Bolt, Chef open source, Convex, xAI tools, multi-phase tasks
summary: After Brandon leaves, the group discusses context window management in Claude Code, referencing a shared video on the topic. Jake raises Grok4 Fast's unusual eval performance and Bastian explains Grok3 mini's built-in tool-calling in reasoning chains, its cost advantage (40x cheaper than Grok4), and automatic mode selection. The group also discusses Codex 2's inconsistency across repeated tasks, the open-sourcing of Chef (likely Bolt-based), and Patrick's workflow of feeding video transcripts into NotebookLM for podcast-style summaries.
-->

01:27:34 - Jake Maymar
Patrick, do you kind of want to talk about it a little bit because this is really interesting?

01:27:41 - Patrick Chouinard
Yeah, the video I've pointed you to is very, very nice about context management with Claude Code [tool:Claude Code] — how to maximize the amount of context that you have, how to compress, when to do it, how to remove tools, how to include tools, when to do it, how to split into multiple sub-agents. Always focusing on having enough context left for any task you want to start with. I love the video. It's a bit long, but it's extremely well-built.

01:28:20 - Ty Wells
Patrick, it's 29 minutes. How is that long?

01:28:27 - Ty Wells
I watch my videos at 2X, so that's a good one.

01:28:34 - Patrick Chouinard
No, it's just because it focuses specifically on context management. So 30 minutes on context management — not how to include MCP. It's really how do you manage context in Claude Code for 30 minutes.

01:28:59 - Patrick Chouinard
▶ What I do really often — maybe I shouldn't say that — but I've taken those videos, shoved them into NotebookLM [tool:NotebookLM], and just listened to the stripped-down podcast coming from the transcript.

01:29:11 - Ty Wells
Yeah, I do that too. Don't worry about it. Everybody's doing it.

01:29:20 - Jake Maymar
Well, I'll take the transcript and then I'll just ask it questions. Sometimes that's actually really helpful.

01:29:34 - Jake Maymar
Oh, I did want to talk about Grok4 Fast [tool:Grok4 Fast]. Bastian, have you had a chance to use that? Because that was really interesting — where it popped up on the evals is a really unusual place.

01:30:27 - Bastian
<A>Yes, I did try it. I only use Grok code for Cursor, but in the Grok app, they bake a bunch of tools into the model itself. So it's very awesome to watch it carry out multi-phase tasks. You can actually instruct it to use multiple phases, and you can also guide it on what tools it should use. All of these tools are prefixed like `xai_underscore_tool_name`. In fact, Grok3 mini [tool:Grok3 mini] was kind of incredible for its size because it was able to call a bunch of tools in its reasoning chains — and that's not something to take for granted. It's 40 times cheaper than Grok4, much, much faster. And even if you use it in the application, you don't need to select modes for deep research, think, and all that — it handles all of that automatically. I would encourage you to try it out, especially for the research phases — it's quite good. It can look inside X posts and browse the internet and kind of decides what the next step is. It has a lot of adaptability built in.</A>

01:32:21 - Jake Maymar
Oh, and then Bastian — did you see Chef [tool:Chef] is open source now?

01:32:24 - Bastian
<A>It's interesting, but what they use that's unique to Chef, as far as I can tell, in terms of connecting it to Convex [tool:Convex] — it's like just a Markdown file inside their web application. So when you download those projects, you can get those Markdown files directly with very good instructions for how to manage your TypeScript files and all of that in your environment. I think it's based on Bolt [tool:Bolt], and Bolt is open source, so it's kind of like open-sourcing the derivative.</A>

01:33:10 - Jake Maymar
Yeah, I think you're totally right. I think Bolt DIY, like all of those different branches — I was kind of looking at the code and it looked kind of familiar. But they're doing some pretty interesting things.

01:33:41 - Patrick Chouinard
Yeah, I just said I was thinking about extending SpecKit, but it's a thought I had while driving back from work today, so not ready for implementation yet. But I've used it quite a bit, and so far it does a very good job. It's not even ShipKit-lite — it's really just managing, creating the spec, the plan, and the task. That's it. ShipKit is 20 times bigger than that, but the principle of the thing is really interesting, and it's multi-tool.

01:34:18 - Paul Miller
They've just done updates that take it further, so it does more steps along the way.

01:34:31 - Patrick Chouinard
▶ They're going to add stuff at implementation and debugging and doing a lot more on that side. I was thinking about doing things upfront instead — all of the managing the issues, all of the pull requests, the commits, all of the administrative part of code management that nobody does in the vibe coding world right now. Even if it does half the job correctly, it's already 50% more than what's getting done today.

---

<!--SEGMENT
topic: GPU Inference, EC2 Scaling & LLM Deployment on AWS
speakers: Juan Torres, Bastian, Jake Maymar, Ty Wells
keywords: EC2, A10 GPU, A100 GPU, horizontal scaling, vertical scaling, VRAM, CPU offloading, quantization, LLM inference, CUDA, DigitalOcean, Docker, Kubernetes, vLLM, token speed, latency to first token
summary: Juan Torres describes his work deploying LLMs and diffusion models on AWS EC2 instances with A10 GPUs (24GB VRAM), using CPU offloading and swap memory conversion to extend capacity. He explains the cost-benefit decision to use Oculus (offering isolated A100 instances) before migrating to EC2 with horizontal scaling across multiple A10 units. Bastian and Juan discuss the technical nuances of horizontal vs. vertical GPU scaling, cold-start costs, CPU-to-GPU bandwidth as a bottleneck for latency to first token, and the trade-offs of quantization on inference speed.
-->

01:53:06 - Juan Torres
One of the things that I think is really interesting is you can use your agentic ID for EC2 [tool:AWS EC2] instances. I've been playing around with that the last couple of weeks, just deploying LLMs or diffusion models. Right now, it's just been to an A10 GPU [tool:A10 GPU], which is not very powerful in order to handle 14 billion parameter diffusion models. You'll be surprised that you actually need way more GPU in order to handle those.

01:54:12 - Juan Torres
The way I've been trying to go around it is by engaging in CPU offloading. So you can basically set up the EC2 instance to use — the A10 has 24 gigabytes of VRAM, and then you have, let's say, 16 gigabytes of CPU. So what you can do is set up the environment to offload a lot of the processing power from the CUDA [tool:CUDA] environment to the CPU. And apparently you can convert some of the SSD memory into actual processing capacity — you can recruit it to handle some of the capacity, and you can do it permanently.

01:57:00 - Juan Torres
The reason I can't really rely on one A100 in AWS is because they don't offer one single A100 GPU. They offer an EC2 instance with, like, A10, and then A10 with more CPU capacity, and then it jumps to a bundle of A100s. So I actually carried the cost-benefit analysis for my clients, and that's the reason we opted for Oculus at the beginning, because they were actually offering an A100 isolated. In the cost-benefit schema, it made sense to go for that option. The problem is that at one point there were some costs that were not perceived at the beginning, so then we decided to reorganize around an EC2 instance and provide the option for horizontal scalability.

01:59:00 - Juan Torres
▶ It's called horizontal scaling because you have the recruiting of several instances of a computational unit across the same EC2 instance, versus vertical scaling in which you actually go up a hierarchy of EC2 instances that have more capacity as you go higher. Here, horizontal scaling — we're just recruiting the same A10 GPUs across several of them. The reason I'm recommending horizontal scaling is because what we're trying to recruit here is GPU real estate instead of CPU real estate.

02:00:51 - Bastian
<Q>So if I understand correctly, horizontal scaling is traditionally used in ML models when the model doesn't fit in one instance, so you distribute it. And in those cases, you might actually find a bottleneck where the CPU is not fast enough to load the model into the GPU. When does a CPU matter for ML loads that run in GPU?</Q>

02:01:28 - Bastian
<A>Well, it's just to give it the instructions to load the model into the memory. So if you are doing horizontal scaling and those instances are cold, you will pay that cost upfront for every instance you spawn. And that's the difference with the other kind of scaling — when the model fits and you just spawn more instances, you don't pay that.</A>

02:02:26 - Bastian
<Q>Are you facing that bottleneck yourself?</Q>

02:02:31 - Bastian
<A>Not personally, but it's part of the things I had to study when I was considering using a GPU for the chunking in ShipKit. The most demanding process is by far chunking and the OCR process — it's not the query part or inference. It's actually the part where you front-load all these files. Processing things that require FFmpeg are actually much faster than processing OCR in a PDF. So you could route everything very smartly — everything can run on a CPU if it's video, audio, text, and Markdown, but if you have PDFs, you would optimally benefit more from using a GPU.</A>

02:07:06 - Bastian
▶ Speed in tokens per second shouldn't change too much once it's loaded into the GPU or the cluster of GPUs, but the latency to the first token should be very influenced by the CPU and traditional RAM — its capacity to load the model into the GPU and how they are connected. That's where I would look if you have a problem from question to first token.

---

<!--SEGMENT
topic: RAG PDF Chunking Challenges & Complex Document Handling
speakers: Bastian, Patrick Chouinard, Jake Maymar
keywords: RAG, PDF chunking, OCR, merged cells, tables, vector embedding, vision LLM, FFmpeg, document intelligence, agentic RAG, ShipKit, Docling, inference pipeline
summary: Patrick Chouinard raises the challenge of chunking complex PDFs with merged table cells, which become nearly unreadable after standard OCR-based chunking. Bastian recommends routing complex graphical pages to vision-capable LLM agents rather than traditional OCR, pre-processing PDFs into test categories (plain text, tables, images), and potentially bringing images as additional context at inference time rather than embedding them. Jake mentions using Azure Document Intelligence but finding it unstable, and references an agentic RAG system (attributed to Andrew Ng) that handles complex tables well.
-->

02:08:02 - Bastian
Patrick had a question about how you manage chunking — specifically about if you had to test with very complex PDFs, especially including complex tables with merged cells, because from experience they're hell to chunk properly.

02:08:15 - Bastian
<A>Yeah, that's an important factor. I designed different template PDFs — some had different domains, some had more tables, some had more graphics, even simple PNGs stuck into them. I tried to stick with — and this is what I would encourage you guys to do — because you will have to tweak the parameters of whatever Brandon ends up coding for you. The complexity of your documents is a great factor that adds variability. I would recommend having test documents. Claude can create these for you. Like you just described: I need a very basic one, just one page of plain text, then five to 20 pages of pure text, then a variation where you have one table, maybe five tables, then maybe a more traditional image. Define what looks like your most typical use cases.</A>

02:09:52 - Patrick Chouinard
Yeah, because a lot of the problems we've encountered — we build our own RAG system — and they have a lot of very complex tables that have merged columns, merged rows, merged cells. And chunking makes it almost unreadable. It's extremely complex to chunk it in a way that the LLM will understand, "oh, those two cells are actually reporting to those two rows."

02:10:22 - Bastian
<A>I think those should be handled separately. Like, okay, I have this 30-page PDF, but there are these four pages that are super heavy on graphics and super technical. Those would benefit more from an LLM with very good vision capability, instead of trying to chunk it with traditional OCR — which is what Docling [tool:Docling] and all this stuff do under the hood. So I think those that need a deeper understanding on the knowledge domain — agents with vision is basically the way to go for those concrete pages. But then you will lose the benefit of the embedding, or you will have to handle that separately.</A>

02:11:47 - Bastian
▶ Something you could do is — if you have documents that contain some hard graphics but are mostly text — do the chunking and embeddings for everything text-related, and just have the model bring the images as additional context for it to analyze at inference time. I think that could work.

02:12:23 - Bastian
So it receives the RAG input, the chunks it retrieves, but also — oh yeah, this document has also these images. Do you want me to add this to the analysis and have some idea of where in the text they go?

02:12:43 - Jake Maymar
Right now, we're using Document Intelligence [tool:Azure Document Intelligence], but honestly, it's not the most stable thing in the world.

02:12:50 - Jake Maymar
Yeah, I think the thing that has Andrew Ng's product — I forgot what it's called — but it's like an agentic RAG system. It excels for graphical complex tables and stuff like that. I've seen it used for medical examples, even tissue analysis — looking at the microscope with all this complicated stuff — and it has a very good understanding and can produce a structured output. So it's like, okay, the skin has three layers, in the first layer I see this, in the second I see this, and I can produce a structured JSON for you.

02:13:39 - Bastian
▶ Yeah, sure. I think those are really good questions. This is great, guys. Great call. I'm looking forward to the next chat and looking forward to seeing what everyone builds.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not provided in this session):

- **Elijah** — appears multiple times; no canonical form confirmed
- **AlexH** — appears multiple times; likely "Alex H." but full name not confirmed
- **Bastian** — appears multiple times; no canonical form confirmed
- **Jake Maymar** — appears multiple times; no canonical form confirmed
- **Jahangir Jadi** — appears multiple times; no canonical form confirmed
- **Juan Torres** — appears multiple times; no canonical form confirmed
- **Mitch** — appears multiple times; no last name provided
- **Alex Wilson** — appears once; no canonical form confirmed
- **David Stamper** — appears multiple times; no canonical form confirmed
- **Tom Welsh** — appears multiple times; no canonical form confirmed
- **Ty Wells** — appears multiple times; no canonical form confirmed