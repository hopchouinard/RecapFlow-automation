=== SESSION ===
date: Unknown (Tuesday)
duration_estimate: ~2 hours
main_themes: ShipKit platform launch, agent architecture design, LLM/model selection, freelance client management, RAG vs. managed AI services, Google ADK vs. LangGraph deployment challenges, cloud infrastructure and CI/CD, local LLM hardware

---

<!--SEGMENT
topic: Call Scheduling and Introductions
speakers: Paul Miller, Tom Welsh, Patrick Chouinard, Brandon Hancock
keywords: ShipKit, time zones, call scheduling, Europe, Americas, Australia, coaching calls, community, Discord, poll
summary: Participants discuss the difficulty of finding a globally friendly call time for ShipKit coaching sessions, weighing US East Coast, European, and Australian time zones. Brandon shares a brief personal update about stress relief and the ShipKit launch going live, and proposes using a Discord poll to decide on shifting call times.
-->

00:02:10 - Paul Miller
Hey, guys.

00:02:12 - Paul Miller
Hey, Paul.

00:02:14 - Tom Welsh
Hey, Tom, Patrick, Hemal.

00:02:17 - Paul Miller
Hello, hello.

00:02:23 - Paul Miller
So are we all playing with ShipKit?

00:02:27 - Paul Miller
Obviously.

00:02:37 - Paul Miller
I literally had the video going on right now, just watching that while you asked that question on the ShipKit.

00:02:47 - Paul Miller
Well, just hear that my only issue is the time of the call. It's like five o'clock in the morning.

00:02:55 - Paul Miller
I don't do five o'clock in the morning. For anything.

00:03:00 - Tom Welsh
5pm, for me, it's perfect.

00:03:03 - Paul Miller
Yeah, well, that was the target, Europe. Middle of the working day for America.

00:03:08 - Paul Miller
I'm not sure if that's the right target. I'd be interested to hear the feedback.

00:03:16 - Paul Miller
How about you, Patrick? We've got Mitch here as well. When you're doing stuff on this kind of learning thing with AI, would it not be better for you to do this in the evening American time? Or what works best for you? Because you've got day jobs, you've got bills to pay, and clients to talk to, vibe coding to do around the office, Patrick.

00:03:46 - Patrick Chouinard
Since I'm in Quebec, I'm East Coast time. So for me, 6 o'clock is perfect. It gives me just the right amount of time to get back from work and get back home. That's why sometimes I arrive like 15 minutes late.

00:04:05 - Paul Miller
So for this call now, but the ShipKit, the ShipKit time.

00:04:07 - Patrick Chouinard
So honestly, it's doable if I need to, because if I were to do it in the middle of the day, the only place I could put it is at lunchtime.

00:04:19 - Patrick Chouinard
And that would make it possible for people around the world as well. So I think he's right. It's the only time schedule that works pretty much almost around the globe.

00:04:36 - Patrick Chouinard
It's never going to be perfect for everyone.

00:04:40 - Paul Miller
Well, my question would be, the fact you can do it in your lunch break is a bit tight. But what about the guys on the West Coast of the US? That's not going to work. But I don't think you can get it perfect.

00:05:05 - Paul Miller
But I think it comes back to the question of, well, who's your biggest audience? When in their day are they available?

00:05:29 - Paul Miller
The problem is it's not great for Western Europe.

00:05:32 - Patrick Chouinard
It's pretty awful for Asia.

00:05:36 - Paul Miller
The Australians, it's kind of okay for, but yeah, anyone west of Australia, all the way to Europe, it doesn't really work.

00:05:57 - Paul Miller
I think he suggested having two times. And the ShipKit calls would work just like stagger it a few hours and then you get the better reach.

00:06:08 - Paul Miller
I think Brandon's going to need an assistant.

00:06:21 - Tom Welsh
Sleep is for the weak.

00:07:31 - Patrick Chouinard
Hey, Brandon.

00:07:32 - Brandon Hancock
Hey. I hope everyone's having an awesome Tuesday so far. Sorry, we had to cut last week short, but I cannot tell you guys how much less stressed I am as a human being. I went outside. This whole time working on ShipKit, I'd have little golf videos in the background just to like, man, I'd love to try golf at some point. So yesterday, I actually went outside for like 10 minutes. My dog and I played golf where I would hit it and she'd bring back the ball. So it felt good to go outside, do something. It felt awesome. So my new me, Brandon 2.0.

00:08:23 - Brandon Hancock
Obviously, ShipKit's live, having some really fun on the coaching calls in there. And I'm building it live with everyone. So as people suggest things — like Mark had a good call out, there was a random button that shouldn't have been there — it's just fixing stuff, shipping code. It feels good. It's what nerds love to do.

00:09:01 - Brandon Hancock
I guess if anyone has any big questions first, we'll do that. And then if not, guys, we will just go round robin.

00:09:13 - Brandon Hancock
Yeah, we'll do that as the call order. But if anyone has any questions in the meantime, take those first.

00:09:21 - Brandon Hancock
I'm setting up a Discord thing right now just to communicate with you guys. The second I get a Discord stood up, I was going to start asking if everyone's cool with doing 2 p.m. I'm totally fine with that. It's just I want to make sure everyone else is.

00:09:35 - Brandon Hancock
So we'll do a poll. I think that's the easiest way. I'm down. I'm literally down to do any of them. I'm working on this whole time. So I'm free when y'all are free is the short answer.

00:15:53 - Tom Welsh
It's 11 p.m. in the UK. So it's midnight in Europe.

00:16:03 - Brandon Hancock
Yeah. That's the hard part. For you in Europe, noon Eastern is like 7 p.m. So it covers, yeah. Darn time zones. Everyone just move. Come hang out with me in Georgia. We'll all be in the same time zone. We'll all go hang out at a coffee shop and just nerd out. The problem is solved, guys.

00:16:27 - Tom Welsh
I mean, you've got three calls a week. It might be worth just staggering times, like a US/Europe friendly, an Antipodes friendly.

00:16:37 - Brandon Hancock
I think that's a great idea. Well, yeah. I will poll, but I guarantee one of them will 100% move. So we'll do that.

---

<!--SEGMENT
topic: Agent Architecture Design Principles
speakers: Brandon Hancock, Sam
keywords: agent architecture, LangGraph, ADK, root agent, sequential agents, context window, Excalidraw, wireframing, task decomposition, sub-agents
summary: Sam asks for general advice on deciding agent architecture, prompting Brandon to explain his visual-first design approach using Excalidraw and his rule of thumb for keeping agents focused on single tasks. The discussion covers when to use a root-delegate pattern versus sequential chains, and the importance of limiting agent scope to avoid context window overload.
-->

00:09:27 - Brandon Hancock
Okay, so any good tips on deciding agent architecture? Quick question — are you using ADK, LangGraph? You like LangGraph, right, Sam?

00:09:43 - Sam
Yes, yeah, I'm a LangGraph user. But just more of a general question, because I know there's a lot of clever people here, and I just don't want to get stuck in the same kind of rattle thinking. You know what I mean?

00:09:54 - Brandon Hancock
Yeah, so I'll go ahead and tell you the main way I build agents. I'm a very visual guy, so my go-to — I'll just show you a picture of literally what I do when I'm trying to build agents.

▶ 00:10:19 - Brandon Hancock
I actually just draw everything out in boxes inside of Excalidraw [tool:Excalidraw], and that's how I basically try and think of what is a single task that one agent can do very successfully. And from there, that's when I kind of go into actually building out things inside of code. So I do a wireframe first.

▶ 00:10:46 - Brandon Hancock
My overall practice is there's usually two types of workflows. It's usually you have a root agent that delegates, or you have a combination of a root agent that delegates and sequential agents. That's like 80% of all use cases most of the time. So that's exactly how I do it. I draw it out first, then I go into code land. That's my practice.

00:11:17 - Brandon Hancock
If anyone else has any ideas, I'd love to hear what anyone else is doing for agents. I don't know if anyone else is deep in agent architecture.

00:11:23 - Sam
<Q>I think one of the distinctions I find hard is like when to move from that kind of almost like a rapid agent supervisor to kind of more like those distinct flows or chains. So like it just kicks it off as opposed to it kind of passes between. I feel like anything more than two or three steps is kind of no longer viable to use that kind of pattern. Do you have a kind of rule of thumb for that or any thoughts on that?</Q>

00:11:50 - Brandon Hancock
<A>Yeah, I usually keep mine under five. Like if an agent can't do it on one hand — one virtual agent hand — it's too much. So at that point, what ends up happening is your root agent, instead of it being phase one through eight, it really is now phase one through three, where phase one has sub-phases. Like it's responsible for coming up with a core idea. And core idea might be a research plan, put together a core plan — you basically just chunk it down into smaller, smaller, actionable things that one agent can literally do on one hand.</A>

▶ 00:12:37 - Brandon Hancock
The context window is actually the root issue. The best way you can address that is just give everything a single purpose and a single function. So it's like writing good software — if your agent's prompt is more than about 200 lines, or if it's doing more than five phases, you need to start splitting stuff up.

---

<!--SEGMENT
topic: Wireframing Tools and Excalidraw Workflow
speakers: Brandon Hancock, Hemal Shah, Mitch
keywords: Excalidraw, wireframing, Cursor, screenshot, agent design, visual workflow, keyboard shortcuts, pen-and-paper alternatives
summary: Hemal asks for a tool recommendation for creating simple wireframes when moving from idea to design. Brandon recommends Excalidraw as his primary tool for both UI wireframing and agent architecture diagrams, explaining how keyboard shortcuts and the ability to screenshot directly into Cursor reduce friction in the AI-assisted development workflow.
-->

00:20:17 - Hemal Shah
<Q>One question I have is, going from an idea to design and rollout, in one of the videos you had the wireframe and how you iterate with customers and all those things. Do you have any recommendation for the tool to create the wireframe, simple boxes?</Q>

00:20:43 - Brandon Hancock
<A>My go-to is Excalidraw [tool:Excalidraw]. That's literally how I draw everything. They have a great free tier. Like, I know some people literally never upgrade Excalidraw — they end up just making one massive drawing that expands infinitely. I think it's like $8 a month or something.</A>

00:21:14 - Brandon Hancock
▶ Going back to Sam's question earlier, even for designing agents, I'm always drawing in Excalidraw just because sometimes you just need to get it out of your head. You're just like, man, sometimes I just need to — okay, I'm going to start this box, then I'm going to go over here and then go over here. And then eventually, oh, I can break that apart.

▶ 00:21:39 - Brandon Hancock
And it's really nice because then you can just take a screenshot and pass it into Cursor [tool:Cursor]. That's always my goal — to put as much information as I can into the computer so that I can as easily as possible screenshot and throw it into AI. So that's why I don't do as much stuff pen and paper, because I just want to quickly throw it into AI.

00:21:51 - Hemal Shah
Lower friction.

00:21:52 - Hemal Shah
<Q>And you use mouse and trackpad, or is there a stylus or something?</Q>

00:22:02 - Brandon Hancock
<A>No, if you know the shortcut keys, you literally just have to hit numbers one through six to go from everything like your text box to arrows to rectangles to circles, and then just trackpad. It's awesome what you can do in there. Eventually your brain will rewire like mine has, to where now I think in like, okay, two, six, four — draw it out. My brain thinks in numbers at this point when I'm in Excalidraw, just to try and get all the graphics out as quickly as possible.</A>

---

<!--SEGMENT
topic: Obsidian, Fabric, and Personal Knowledge Management for AI
speakers: Mitch, Brandon Hancock, Patrick Chouinard, Jake Maymar, Morgan Cook
keywords: Obsidian, Hugo, Fabric, Daniel Miessler, Claude Code, MCP, Asana MCP, markdown, folder structure, personal assistant, knowledge base, NetworkChuck
summary: Mitch shares a workflow combining Obsidian with Hugo for publishing AI-generated markdown as blog articles, and highlights how the Asana MCP dramatically accelerated his weekly account update emails. The group discusses Daniel Miessler's Fabric project as a model for structuring personal knowledge for AI consumption, and Brandon reflects on the broader trend of AI agents accessing all personal context through MCPs.
-->

00:22:41 - Mitch
There's actually one video I wanted to share with the group that I found really interesting. It's basically taking Obsidian [tool:Obsidian] and then using Hugo [tool:Hugo], and then from Hugo to any hosting provider, and basically taking your Obsidian markdown format file and then converting it into a blog article. And then you could use Claude Code [tool:Claude Code] or whatever coding agent to write that markdown file, and basically allow you to create a newsletter, and then use that to do a video off that or something.

00:23:43 - Mitch
It was from NetworkChuck. [link:NetworkChuck YouTube channel]

00:23:48 - Brandon Hancock
It looks at your own thoughts, pulls out — I guess you ask it a question about your own stuff, and then it generates a video based on your own internal docs?

00:24:00 - Mitch
Well, the creation of the blog article wasn't automated, but everything else from taking your local Obsidian file base. I was wanting to build that basically because I'm working more and more on having a better organized markdown file structure and just folder structure for all my different projects. So when I'm communicating to Claude, there's the developer agent.

00:24:37 - Mitch
I forgot to put this one out there — using MCPs [tool:MCP] and just work. Because I use this Asana MCP [tool:Asana MCP] and it was crazy how much work it did for me, like near instantly. I was blown away. Basically, I have to send weekly account updates, hooked up the Asana MCP and gave it the template and it wrote all of my weekly update emails as far as the progress updates. In probably like 15 minutes — took me at least like two hours to do it otherwise.

▶ 00:25:11 - Brandon Hancock
That's so funny because I'm working on setting up a Discord right now and you're so spot on. I did stuff with a manual script and the second you said that I was like, why did I do that? Should have been doing MCP. So yeah, instantly after this, homework is MCP plus Discord.

00:25:42 - Mitch
When MCP first came out, the tool was there, but the usage wasn't. And so now that the usage is there, I'm just really rethinking how I could start to leverage MCPs. Like the Limitless MCP — I saw someone just hook that up to their Claude Code, and say, hey, I had a conversation about Alex Hormozi that was sometime earlier today, could you find that conversation and tell me what it's about? And then it did it. It was crazy. It really made me rethink how I'm using these agents, not just for coding, but for everything else.

00:26:51 - Mitch
I think Jake put me on to Daniel Miessler or Meissler. The guy who created Fabric [tool:Fabric].

00:27:10 - Patrick Chouinard
It's — I love this guy.

00:27:23 - Mitch
Seeing how his folder structure of the markdown files is really, really interesting. It made me rethink everything. Very similar to ShipKit, but for using it more as your personal assistant.

▶ 00:28:01 - Brandon Hancock
Here is the core context: how do we as AI power users structure all of our information in a way that is as easy and frictionless as possible for AI to access it? That is the true problem to actually be solved.

---

<!--SEGMENT
topic: LLM Model Selection and Claude Sonnet 4.5
speakers: Brandon Hancock, Paul Miller
keywords: Claude Sonnet 4.5, Claude 4, Cursor, token window, max mode, Grok, model tiers, context window, cost, vibe coding
summary: Paul asks Brandon about his current preferred LLM model given recent announcements. Brandon shares that he has moved to Claude Sonnet 4.5 as his primary model, explaining the simplified two-tier system (standard vs. max mode with 1M token window) that replaced his previous three-model workflow. He also notes his Cursor bill reached thousands of dollars after building nearly 20 projects in a month.
-->

00:16:53 - Paul Miller
<Q>Have you got any movement in your preferred LLM model that you're using with Cursor with ShipKit? Given the announcements of the last week, you probably haven't had any time to look at them.</Q>

00:17:06 - Brandon Hancock
<A>No, man, I'm already in. As of yesterday, Claude Sonnet 4.5 [tool:Claude Sonnet 4.5]. I mean, it's crushing it. Claude 4, beautiful. It's just I had to pay for it. I didn't mind paying for it. It's just, guys, my bill for Cursor [tool:Cursor], it's thousands — like actually thousands of dollars. I didn't know that was possible, but I had to build out nine projects, plus troubleshoot stuff, plus there were so many things. I literally built almost 20 projects in the span of a month. So I paid for it.</A>

▶ 00:18:05 - Brandon Hancock
Claude 4.5 has been using it religiously the past day. It's a beast. It's an absolute beast. I'm going to use it primarily for everything.

▶ 00:18:10 - Brandon Hancock
In the past, I had a three-tier system where I would use Claude 4, Claude 4 max when I wanted to hit that 600,000 token window, and then I would swap over for really big tasks to the 1 million token window — basically a big brain model that does the big brain thinking, passes the task down to a worker who's much cheaper. But now in Claude 4.5, the second you go to Claude 4.5 max, it is the 1 million token window. So it actually got a lot simpler. You don't have to keep up with three different models now. It's just one.

00:19:27 - Brandon Hancock
Grok [tool:Grok] did release their Hidden One Million one, and it's okay. But I mean, my Cursor bill is many thousands of dollars right now. So I'm looking for any free model. Anything free, I'm a sucker for it right now because I need to save some pennies in Cursor.

---

<!--SEGMENT
topic: Mass Email Outreach and Lead Generation Tools
speakers: Brandon Hancock, Pedro Gomez, Mitch
keywords: Instantly, Mailgun, Firestore, Gemini CLI, B2B lead generation, cold email, non-profit outreach, personalized email, email warming, SMTP
summary: Pedro, a new member, describes building a B2B lead generator for non-profits using Firestore and the Gemini CLI, and asks about tools for sending personalized mass emails. Brandon recommends Mailgun for application-level sending and Instantly for larger outreach campaigns, pointing to the Instantly YouTube channel as a practical learning resource. Mitch is identified as a resident Instantly expert.
-->

00:29:44 - Pedro Gomez
Hi, I'm new. So pretty much I've been using the Gemini CLI [tool:Gemini CLI] to create something similar to Candy. I've been working on that a bit. And then also I'm trying to do a lead generator for business-to-business, mainly non-profit, and so I first uploaded the data into Firestore [tool:Firestore] using the NAN, and now I'm trying to create personalized emails so I could send out mass emails.

00:30:19 - Brandon Hancock
<Q>Is the issue you're stuck on how to create mass personalized emails? How many is mass? Like, are we talking about a hundred, a thousand, ten thousand?</Q>

00:30:43 - Pedro Gomez
<A>Probably like a hundred per week. Not as much, but I'm mainly just looking at non-profits in San Diego first.</A>

▶ 00:30:52 - Brandon Hancock
A few different options on that. If you're just doing this strictly within the confines of your software application, Mailgun [tool:Mailgun] is awesome for that. If you want to go higher level though and do way bigger market automations, Instantly [tool:Instantly] is phenomenal. Mitch is probably the resident Instantly expert. So definitely maybe if you two want to collaborate, or just a few pointers on how to do it.

▶ 00:31:47 - Brandon Hancock
Also, the Instantly YouTube channel itself is a goldmine of real world examples and walkthroughs. [link:Instantly YouTube channel] I watch their stuff all the time. They're so good at creating awesome examples. He has some examples in here where he literally starts a business with using direct outreach in a day.

00:32:22 - Pedro Gomez
Yeah, I have Instantly right now, I'm warming them up, but I haven't yet looked at the personalized email yet.

00:32:31 - Brandon Hancock
Well, hey, keep us posted. I watch all this stuff on Instantly, I hear nothing but good things about it, but I personally have yet to use it, so I'd love to hear your thoughts on it once everything's warmed up and sent out.

---

<!--SEGMENT
topic: Freelance Client Onboarding and Scoping Strategy
speakers: Brandon Hancock, Morgan Cook, Prem, Tom Welsh
keywords: requirements document, discovery phase, feature creep, milestones, paid discovery, freelance contracts, intellectual property, project kickoff, testing period, strategy document
summary: Morgan asks how to handle a new freelance client with unclear requirements and potential for feature creep, specifically whether to charge for a requirements document phase. Brandon, Prem, and Tom advise rebranding it as a paid "discovery" or "strategy" document, requiring upfront commitment to filter out tire-kickers, using milestone-based contracts, and including a defined two-week testing period to limit post-launch support obligations.
-->

00:33:06 - Morgan Cook
<Q>So right now I have a new client that wants to bring on. And I have concerns about the follow through from their side. I have some requirements documents that I'm working on for them. But I wanted to see how you guys deal with bringing on new clients that are freelance. Do you charge them for like the requirements document phase? And then after that is figured out, go forward from there?</Q>

00:33:48 - Brandon Hancock
<A>Are you at the stage now where you guys had initial talks where they're like, hey, I would like you to build this, and you're like, yeah, I could probably build that — and that's as far as it's gotten, like there's zero formal documents, correct?</A>

00:34:12 - Morgan Cook
Yeah, so this came to me from a previous co-worker of mine who knew my skills. The company has a document scanning and shredding and archiving kind of process, which I've dealt with a lot of internal work process, task processing, data collection, all that kind of stuff. The problem is they have potential of taking it somewhere else. And so I'm okay if they take the requirements information somewhere else, if they paid me for it. So that's why I was trying to see — is there a way to say, okay, let's do the requirements document as one part of the project, and when we're done with that, then we'll see what the costing is for development of the full system, but the requirements document stays my intellectual property until it's paid in full?

▶ 00:35:24 - Brandon Hancock
The way I like to frame it is — I wouldn't call it a requirements document. I would basically call it an AI discovery. Basically it's like, hey, I will go in, do an initial discovery of your system, create this document of your current state, how we can achieve your goal state, I'll map it out, I'll break it out into phases, I will do the full nine yards. However, this is a paid service. And what I'd like to do in these situations is if you want to go with me, this will apply towards the project — just so it's incentivizing them to continue working with you.

▶ 00:36:00 - Brandon Hancock
The worst thing that can happen is you spend a week on this, put all your effort into it, and then they go, well, I appreciate all the very free work, but we weren't serious about this. So it's another good way to get a sense of urgency and commitment.

00:36:54 - Prem
Yeah, just want to stress on one of the points that Brandon said. This requirements document is kind of the old way, doesn't give the same vibe. I would call the document a strategy or something, even though the requirements might be underneath that. One of my friends kind of marketed that way where he was able to sell it as a separate service.

00:39:18 - Tom Welsh
I agree with what Prem was saying regarding not calling it requirements. It's definitely a strategy or a project initiation document or something like that, and it has an innate value, because you could take that and give that to a third-party supplier. So you're doing the upfront work, so you should be paid for that. And as Bastian said in the comments, it's worth saying — if you do go with me, we'll discount it if you take the proper work on board. You discount your discovery when they take the project on.

▶ 00:40:26 - Brandon Hancock
When it comes to actually working on the project, huge fan of milestones. I cannot stress enough — milestones to where you break down exactly what functionality will exist at the end of each milestone, so there's no questions about it.

▶ 00:41:39 - Brandon Hancock
One thing that I've done recently that people have really liked is I usually leave a two-week testing period at the end, where I'll say, hey, during this two-week period, it's a new app for both of us, you're going to test it out, I'm going to test it out. I'm not going to add new features during this time, but it's just to confirm everything is great. You don't want six months from now for them to be like, hey, there's a bug, fix it for free. So that's just one other quick catch I've done to make sure you don't end up obligating yourself to a lifetime of support for free.

---

<!--SEGMENT
topic: ShipKit App Development and Route Optimization Project
speakers: Paul Miller, Brandon Hancock
keywords: ShipKit, Next.js, traveling salesman problem, Google Maps API, route optimization, field sales, merchandising, Australia, vaporware, background jobs, TypeScript
summary: Paul reveals he has sold a route optimization app concept to one of the world's largest consumer goods companies before fully building it, using ShipKit to structure the project. He describes the app's core functionality — optimizing field sales rep schedules across retail stores using Google traffic data and open-source routing algorithms. Brandon offers to review the plan and announces upcoming Next.js with background jobs templates for ShipKit.
-->

00:42:45 - Paul Miller
Well, yeah, I've been getting into ShipKit and I started with your demo alpha stuff. I've got a project — I've gone and bloody sold it as vaporware. It's one of the largest consumer goods businesses in the world, so oh God, the pressure's on. It's good — in terms of I've gone from the idea to the master sort of definition prompt, it's got all the wired up screens and things, I'm just going through all the steps now, and I'm hoping to goodness that I can get into a tangible app because the customer wants me to sign a contract tomorrow.

00:43:48 - Brandon Hancock
<Q>Out of curiosity, what's the app supposed to be, or is that top secret?</Q>

00:43:52 - Paul Miller
<A>I'll talk very high level. Customers hire people to go into stores — whether they're salespeople or merchandisers — into retail outlets, whether they're supermarkets or hardware stores or all different retailers across Australia and New Zealand. And the problem is, given X number of stores, given the time, given the geography, and you also tend to have different rankings for the stores — like some stores are worth more money because they buy more, or they've got potential to sell more — you put all these rankings in there, and then you get it to generate what should be the timetable of what each person does for each day.</A>

00:45:00 - Paul Miller
So how many staff do you need to cover all of Australia or all of New Zealand, if you only want to spend X number of minutes at this type of store and this number of minutes at this other type of store, and it optimizes your route, so you spend as little time visiting stores that are not worth it, you minimize the time on the road. I've got it so it will use Google's optimized traffic timing. The whole traveling salesman challenge is to come up with the grid of a point-to-point shortest distance from every point to point — so I'm doing that part open source, and I'm doing the rest with the Google Maps API [tool:Google Maps API], and then it's all wrapped together with a ShipKit application that's linking it all together.

00:45:55 - Paul Miller
I did a deep research on the top three tools that compete in that space in the world, and I got it to extract all the features as to why they're the top three, and all the things that users don't like about it, and I fed that into ShipKit and said, that's what I want to solve. I want to be in the top three, and it's pretty much got the app that operates in that space.

00:46:26 - Brandon Hancock
That's awesome. What I would love to do, Paul, at some point — if you want to go deeper on this, I'd be happy to review the plan just to make sure everything is sound. If any time tomorrow you want to hop on a call, happy to do that to make sure you're good.

▶ 00:48:04 - Brandon Hancock
One thing I really want to do soon for you guys — a lot of times people don't always need to add AI to do a really cool project. Sometimes just doing regular cool projects is still awesome. So one of the very immediate things I want to do for you guys is two videos. I want to do a Next.js [tool:Next.js] TypeScript tutorial for beginners, because there's so much out there that's just designed for teaching the old way, pre-AI. And then part two, I want to do a base template. Paul, the problem you're solving right now can be simplified down to the archetype of just a standard Next.js application with background jobs. That is the archetype of that problem. That is the next immediate template I really want to work on, because so many people have that type of problem.

---

<!--SEGMENT
topic: MCP Integrations, Email Providers, and Local App Exposure
speakers: Brandon Hancock, Marc Juretus, Bastian Venegas, Morgan Cook, Tom Welsh
keywords: Cloudflare, ngrok, Superhuman, Hostinger, SMTP, Railway, DNS, localhost, LangGraph, email provider, port forwarding, Cloudflare Tunnel
summary: Marc asks about third-party email providers to avoid using Gmail credentials in his LangGraph apps, and about exposing local apps without deploying to Railway. The group discusses Superhuman as an email client, Hostinger for SMTP, and Cloudflare Tunnels for DNS-based local exposure. Brandon recommends ngrok as a simpler alternative for exposing localhost ports, especially for testing and small-scale personal projects.
-->

00:53:57 - Marc Juretus
<Q>I'm using my Gmail and some of the LangGraph apps that I'm working on. Is there another third-party email that you would recommend? I just want to do just the basic emailing, like take my markdown and email me without having to bring my Gmail credentials in a way. What would you recommend?</Q>

00:54:12 - Brandon Hancock
<A>I know Bastian's a huge fan of Superhuman [tool:Superhuman]. Bastian, do you want to bring that up real fast?</A>

00:54:33 - Bastian Venegas
Superhuman is a great client to read your emails, but what I have there is a Gmail actually. I just want when it does the process and it sends out a message that it actually, instead of using my Gmail to do a send, something else that I could leverage.

00:54:41 - Morgan Cook
If you have a Hostinger [tool:Hostinger] account, you can use Hostinger to do your SMTP and pub services.

00:54:47 - Bastian Venegas
Yeah, you could eventually take them anywhere, like Cloudflare [tool:Cloudflare] — yeah, you just move the settings to another provider.

00:54:59 - Marc Juretus
<Q>So is Cloudflare basically a way that I can have DNS point to my house because it VPNs to my machine, so if I don't want to publish some of my apps — is that its usage?</Q>

00:55:17 - Bastian Venegas
<A>Yeah, it's one of them. It's one of the many.</A>

00:55:43 - Marc Juretus
Instead of me having to publish apps up to Railway [tool:Railway] and stuff like that, if I could do like an app or two from my house when I'm just playing around with something, would be nice.

▶ 00:55:52 - Brandon Hancock
If that's what you're trying to do — just expose an app on a few different ports — ngrok [tool:ngrok] has a paid service, and you don't have to set up all the things you'd set up with Cloudflare. You just — let me show my screen real fast.

00:56:26 - Brandon Hancock
Yeah, so in ngrok, it's like putting your APIs online. I think it's literally exactly what you want. Eight bucks a month, you can get three endpoints — three different apps. And basically from anywhere in the world, expose your localhost 3000. And as long as you can keep your computer running, this works.

00:56:47 - Marc Juretus
So it's simpler than Cloudflare. Okay, cool.

▶ 00:56:51 - Brandon Hancock
Well, it just — when you were describing it, I was like, man, that's so many steps. Yeah, I think the second you get that spun up, you're like, man, that was easy. Literally like two commands and you're running your app.

---

<!--SEGMENT
topic: ShipKit Platform Progress and Upcoming Features
speakers: Brandon Hancock, Tom Welsh, Patrick Chouinard
keywords: ShipKit, video timestamps, Windows compatibility, Mac shortcuts, Next.js templates, coaching calls, course material, keyboard shortcuts, progress tracking
summary: Tom provides feedback on working through ShipKit's deep dive section, noting a usability gap for Windows users around Mac-specific keyboard shortcuts. Brandon announces an upcoming video timestamp save feature and acknowledges the need to add Windows-friendly documentation. Patrick shares that his consulting firm just acquired another company, adding 450 developers who will need AI-assisted development training.
-->

00:57:25 - Tom Welsh
So yeah, I'm just walking through ShipKit, doing the deep dive section just now. It's all going on.

▶ 00:57:33 - Brandon Hancock
New feature — I haven't pushed it yet, but save timestamps. So as you're watching the video, it'll save where you're at. So if you ever have to come back, you don't have to re-guess. So I'm working on that right now.

00:57:50 - Tom Welsh
I tick as I go, so I do the whole section, then stop. Then go to the next one, then tick it. Done. I like tick boxes.

00:57:58 - Tom Welsh
Then I've got a couple of ideas for some simple apps. I want to do an app that takes company annual returns over several years and extracts information from them. And a friend of mine is in security — physical security — and he's talking about tender documents, and he's using ChatGPT [tool:ChatGPT] currently to write his tenders. I'm like, we can improve on that.

00:59:03 - Tom Welsh
The niggle is it's all Mac. You're not catering for your Windows users.

00:59:10 - Brandon Hancock
I mean, just trying to push everyone to be a Mac user, dude. That's the whole goal, because the second you make the switch — you know better than anyone else.

00:59:26 - Tom Welsh
Yeah, and I get that, so I don't want you to say R minus R, but it's Ctrl+Shift+S on Windows. Some of the Windows guys might not know that.

▶ 00:59:32 - Brandon Hancock
Yeah, no, I agree. I just need to get a Windows machine. I had one, I gave it to a friend. Yeah, I just need to add Windows-friendly documentation.

00:50:06 - Patrick Chouinard
Basically, all of my time was consuming video from ShipKit and thinking about what else I could do with ShipKit. And actually, it's awesome timing because the consulting firm I work with actually just acquired another firm this week. So there are 450 new developers joining us. A bunch of people that are going to need to be trained on AI-assisted development.

00:51:01 - Brandon Hancock
I swear, as soon as you get 1% of freedom, they doubled down on you, man.

00:51:17 - Patrick Chouinard
Basically, it's just because I'm the oldest employee for the firm here in Montreal, and I've been at my client for the past five years as well, so clients usually have me, and internally I've been there for like 17 years.

---

<!--SEGMENT
topic: Vibe Coding Horror Stories and Client Red Flags
speakers: Brandon Hancock, Jake Maymar, Andrew Nanton, Mitch
keywords: vibe coding, Replit, spaghetti code, git commits, password security, feature creep, client red flags, test-driven development, code quality, real-time collaboration
summary: Jake describes helping a developer whose executive client is vibe coding a production app in Replit, resulting in thousands of commits, millions of lines of code for simple functionality, and a broken "forgot password" feature that exposes user accounts. The group discusses the dangers of unreviewed AI-generated code in production, with Andrew suggesting extracting a test suite focused on intended behavior as a starting point for refactoring.
-->

01:09:44 - Jake Maymar
I'm dying to watch more ShipKit videos, and just, they're surprisingly buried with so much stuff. But there's a lot of things I really want to try out, specifically the RAG, so I'm really excited about that side of it.

01:09:25 - Jake Maymar
It's interesting — one of the projects, it's kind of funny, like helping a fellow developer on a project. He came to me and he says — he was telling me the whole client story. And I was like, there's so many red flags, are you sure you want to take this on? And he's like, yeah, I do. And I was like, okay, I'll help you do that thing. And it's hilarious because every time he comes back to me, it's more. And so he came back and it's a live conference that they're releasing the app. And they're releasing it in a couple of days.

01:17:58 - Brandon Hancock
That's so stressful.

01:18:02 - Jake Maymar
I know. So it went from — there's a lot of red flags, are you sure you want to do this? And then I had another conversation of like, man, there's so many red flags. And of course, you know this, Brandon — the way things begin, the way a project begins is how the project is basically going to go to the same ends, right?

▶ 01:18:25 - Jake Maymar
If there's friction up front, or if it's really smooth up front, likely it's going to be that way. If the client's willing to pay, the client continues to be willing to pay. If you have to constantly negotiate cost, well, you're going to have to continually do that.

01:18:51 - Jake Maymar
What I think is really fascinating is the executive that's making all the decisions is actually coding it. And they're vibe coding, but they're vibe coding in the most fascinating way I've ever seen. They really understand the business cases and the business use cases, and they really know what they're talking about, but they are using all sorts of very interesting tools to create things in the most bizarre way I've ever seen. So this is incredibly creative, but it's like millions of lines of code to do stuff that should just be a simple little 30-line thing.

01:19:31 - Brandon Hancock
Whoever inherits that, I feel so bad for. Like, whoever that is, I hope they get paid many hundreds of thousands of dollars, because it is going to be a beast of a project.

01:19:50 - Jake Maymar
When you look at the git, there's like thousands of commits, and it's like a SQL query, and then backing up the SQL query and then trying a different — it's almost like I'm looking at an agent doing all of this stuff. I recommend just understanding the high level of it and basically rebuilding the whole thing. Don't even bother with the existing code — just redo it properly.

▶ 01:20:21 - Brandon Hancock
Yeah. At this point, the code itself is becoming commoditized, but doing it the correct way, the scalable way, the way that's going to allow that company to grow — that is still a scarce commodity. Like, with enough "make this work, make this work," yeah, you could probably get it to do something, but dear God, if it ever has to change 1%, it all explodes, unless it's built properly.

01:21:00 - Jake Maymar
As I was working with this developer and he was showing me the code, the code was changing. So he was in a tool — I think he was in Replit [tool:Replit]. And as he was walking me through it, the code was actually changing. So there was someone else in Replit making changes to that code that he was also in. It was kind of crazy because it's weird to be in code where it's actually changing and the person isn't doing it and you're not doing it.

01:22:48 - Jake Maymar
My favorite thing, Brandon, is the forgot password. So keep in mind, this is a very expensive app. When you click forgot password, it gives you a password and you log in. I could log into your account. Forgot password gives you a password and then you log in.

01:23:49 - Brandon Hancock
And it's just like — someone needs to fire that guy. Or at least do executive stuff. That's crazy. That's awful.

01:24:14 - Andrew Nanton
Hey, so that absolutely does sound like a nightmare. And when I have created my own nightmare soup of spaghetti code, one of the things that I have tried with a lot of success — I'm not saying this is a great solution, but have it write a good test suite, really focused on the intended behavior, and then just extract out only the test suite and say, okay, these are the tests that need to pass. It needs to be able to — when this goes in, this comes out. And try to really just focus in on the intended behaviors. And then you can kind of take a fresh start with something more test-driven.

▶ 01:26:05 - Brandon Hancock
The only thing I would add is the worst part about what they've done is their test would validate that it's doing the wrong functionality. Like, if you're going in the right direction, oh yeah, tests are beautiful. But the worst thing is having tests verify that you're doing the wrong thing, which then keeps enforcing you to do the wrong thing. So that's the only drawback about tests written if you're not doing it the right way. You need a little bit of direction first.

---

<!--SEGMENT
topic: RAG Architecture: Railway vs. Google Cloud for Production
speakers: Brandon Hancock, Prem
keywords: RAG, Railway, Google Cloud, Dockling, GPU, CPU, background jobs, queue management, scaling, multi-tenant, ShipKit, production architecture, Docker
summary: Prem asks why ShipKit moved from Railway to Google Cloud for RAG processing, noting Railway's simpler setup. Brandon explains that Dockling's document processing is CPU/GPU-intensive and Railway's single-service architecture cannot scale for multi-tenant production workloads, while Google Cloud's queue-based approach handles concurrent jobs and scales affordably — sitting idle at roughly $3/month.
-->

01:04:20 - Prem
<Q>One of the things that I did for RAG for that was having the Python job running in Railway, which was simpler and easier. I wanted to kind of use the RAG from ShipKit for that application. But Railway is much more easier once you have the Docker, and I understand the architectural decision you have taken — it's very well thought of, like using queues and so on in Google, but I just feel like the setup and all those things are complicated. So is there a reason that you used Railway in the past and then kind of went to Google for this?</Q>

▶ 01:05:28 - Brandon Hancock
<A>So the whole goal was production, real-world application. The bottleneck is Railway, especially for doing anything related to RAG processing. Dockling [tool:Dockling] itself, especially when doing document processing, is insanely CPU-intensive, and realistically Dockling needs to be run on a GPU. So the kicker is, at that point, Railway is having to monitor the database to figure out what jobs need to be worked on. As soon as it finds what jobs need to be worked on, it just works on them one at a time. Because Dockling can be very CPU-intensive.</A>

▶ 01:06:35 - Brandon Hancock
Also, if you pass in a three-gigabyte video, well, that means no other customer can do anything — every other customer that's trying to use your background worker can't, because there is no scaling. It is a single service running on Railway, which is great for individual projects where you and I are using it or you plus like five customers. But the second you want to go to a real-world application, if you don't have built-in scale, you're setting up your customers to be frustrated because they're going to be like, dude, I just paid you 20 bucks and it says I have to wait three hours to get my video processed.

▶ 01:07:25 - Brandon Hancock
That's why I tried to set it up so that it is built to scale, it's built to have a queue, like every part of it is made for real world. Railway is phenomenal for MVP, and if I was building stuff to just test out stuff, I would 100% do that to start. But it costs like $3 a month if you just leave it idle on Google Cloud, so it's barely anything — it's actually cheaper than Railway on a month-to-month basis, which is crazy.

---

<!--SEGMENT
topic: Multi-Tenant Organization Architecture in SaaS
speakers: Brandon Hancock, Prem, Tom Welsh
keywords: multi-tenant, organizations, roles, WorkOS, Clerk, Active Directory, Supabase, Okta, Auth0, HIPAA, SOC 2, user management, database schema
summary: Prem asks about adding multi-organization support to ShipKit's current single-user template. Brandon explains the database abstraction needed — an organizations table and a roles table — and notes it's straightforward when users belong to one org. Tom follows up asking about Active Directory providers for enterprise use, and Brandon explains that WorkOS is the standard but expensive option at $125/month per org, with Clerk lacking true AD support, leaving Okta/Auth0 as the main alternatives for enterprise-grade identity.
-->

01:09:14 - Prem
<Q>One of the things I brought up earlier — I'm kind of looking at, I know this is more of a single-user SaaS application, but for an organization having a bunch of users, is there anything in your thing to kind of have a multi-user organization setup in this template?</Q>

01:09:32 - Brandon Hancock
<A>So you're saying you want to have user organizations. Okay. Right now it's like a single user — the template is more for single users registering. You want an organization that can register with multiple users within it, something like that?</A>

01:09:49 - Prem
Yeah, users like an organization basically sign up and then they have users.

▶ 01:10:04 - Brandon Hancock
I don't have that in the queue right now. But I can tell you very quickly — it's actually not that hard to do. Everything just has one layer of abstraction. Right now users just exist, but in a multi-organization setup, there's one table above that: user A belongs to organization A. The hard part is when users belong to multiple organizations — that's when it can get tricky. But if it's strictly user belongs to one parent org, it is pretty straightforward. You have to set up organizations, and then you have to set up roles within an organization — those are pretty much the two additional tables you have to set up. Outside of that, every time a person goes to a page, what organization do they belong to? Which information do I show for this organization? And then you can go from there.

01:14:18 - Tom Welsh
<Q>I'm just going to follow from Prem's question regarding organizations. We talk about WorkOS [tool:WorkOS] currently for Active Directory type import into organizations. I look at that license, it's a first-seat license, so I can't just mess around with it. Do you know of any AD type providers that allow you to have, say, 100 users? Because it's very hard to model a company on 10 users.</Q>

▶ 01:14:47 - Brandon Hancock
<A>What's wild is, unless you're doing an enterprise solution where you're also getting paid at the enterprise level, WorkOS is pretty pricey — it's $125 per month per org. So it's no joke. But if you're working with HIPAA, SOC 2 projects, at that point it makes sense. For non-enterprise-level intensity, from my understanding, Clerk [tool:Clerk] does everything you're asking for for Active Directory — but I could be wrong. Active Directory... I think they have it.</A>

01:15:52 - Brandon Hancock
I know Supabase [tool:Supabase] is single sign-on, but you have to pretty much connect it to something else. It's really just an in-between. So you pretty much have to use Auth0 [tool:Auth0] or Okta [tool:Okta], pretty much. So yeah, the second you want to do anything with Active Directory, you're going to have to start to pay the enterprise big boy prices.

▶ 01:16:25 - Brandon Hancock
But hey, good news is you get to charge more, but bad news is you also have to pay more.

---

<!--SEGMENT
topic: RAG Use Cases: Custom Build vs. Managed AI Services
speakers: Brandon Hancock, Hemal Shah
keywords: RAG, OpenAI vector store, ChatGPT Enterprise, Google Gemini, multimodal embeddings, knowledge base, document processing, PDF, video embeddings, Google Cloud
summary: Hemal asks when to recommend building a custom RAG solution versus using ChatGPT Enterprise or OpenAI's managed vector store. Brandon explains the key differentiator is control over file processing and multimodal support, noting that Google is currently the only provider offering true multimodal embeddings (including video), making it his preferred RAG platform for versatile enterprise use cases.
-->

01:11:10 - Hemal Shah
<Q>I wanted to understand the difference between the RAG-based SaaS application that we're talking here, where we can upload a knowledge base and everything, and ChatGPT Enterprise [tool:ChatGPT Enterprise], and there are other options where you can upload the knowledge base. So I'm asking — if a client approaches me and says they want to create a RAG-based solution, knowledge base, in what scenario should we go for maybe just choosing ChatGPT Enterprise licensing versus building the full-blown RAG SaaS?</Q>

01:11:47 - Brandon Hancock
<A>Yeah, so basically what Hemal's asking is when to use straight-up vector store inside of OpenAI [tool:OpenAI] versus doing your own. There's a few different reasons why you'd want to go between both of them. It really comes down to what you're trying to offer and what information you're trying to upload.</A>

▶ 01:13:24 - Brandon Hancock
If you're fine with pretty much all the defaults that OpenAI gives for creating the embeddings — from my understanding, OpenAI does not do multimodal embeddings at all. So if you want to do anything related to a video, I do not believe they have multimodal embeddings. I think Google [tool:Google Gemini] is the only company right now that does multimodal embeddings, but they're like one of the only platforms that allows you to literally talk with a video, which is crazy.

▶ 01:13:52 - Brandon Hancock
That's why Google is my favorite right now for RAG-based solutions, because they support not just 50% — they support 100% of all different mediums that you could actually want to ask questions about. So that's the main thing. OpenAI, phenomenal tool, it's just it really comes down to what use case you're trying to work with.

---

<!--SEGMENT
topic: Google ADK vs. LangGraph: Deployment Challenges
speakers: Brandon Hancock, Hemal Shah, Jake Maymar, Mitch, AlexH
keywords: Google ADK, LangGraph, Vertex AI, Agent Engine, streaming, deployment, dual endpoints, context window, ShipKit, GCP, production agents, rate limits, polling
summary: Multiple participants discuss the current state of Google ADK versus LangGraph for production agent deployment. Brandon gives a detailed assessment: ADK offers an excellent local developer experience but has critical production issues including broken streaming on Vertex AI, dual API endpoints for local vs. cloud, and low rate limits requiring polling. He recommends using the Google Generative AI library for sequential workflows now, with ADK as a future upgrade once Google fixes deployment. LangGraph is positioned as the more production-ready alternative currently.
-->

01:41:28 - Brandon Hancock
Just to share with the group — current thoughts on the state of ADK [tool:Google ADK] versus LangGraph [tool:LangGraph].

▶ 01:41:40 - Brandon Hancock
ADK, phenomenal developer experience locally, phenomenal. Like, the fact that you have all of the session viewers, events, you can view state — all of it, phenomenal. Right now, their deployment process is very difficult. Like, to the point where it is a four out of ten on friendliness and reliability. Especially between Agent Engine and their deployment process right now, it is very difficult.

▶ 01:42:12 - Brandon Hancock
So like, if you're working on an app that you might use plus three other guys, yeah, it is great, but the scalability right now of Agent Engine is just not really designed for big production, multi-tenant clients, at least from what I have found. That's why I'm very excited to dive into LangGraph, because LangGraph is more complicated up front, but running in the cloud, it crushes.

01:49:33 - Hemal Shah
Brandon, the recent discussion regarding Google ADK versus LangGraph that you mentioned — my love for Google ADK is fading a little bit as I'm coming towards the deployment stage and the API differences that we talked about a couple of weeks ago, where developing locally you have different API endpoints and developing on production Agent Engine, they are different endpoints. And I'm going to introduce the whole AI framework to my company. I'm just wondering — should I continue that path, or maybe take a pause and see how LangGraph comes around?

▶ 01:50:28 - Brandon Hancock
<A>So, quick update: as soon as they fix Vertex AI [tool:Vertex AI], Google has won, in my opinion. It is as simple as that. As soon as they fix Vertex AI to where it's a one-click deploy ADK app, and it just works, and they fix the issue of the dual endpoints — when I'm hitting the cloud I have to handle this type of path, when I'm hitting local I have to handle this type of path — all of that is solved in ShipKit. I can't tell you how many hours I spent on the back end to make it just automatically work for you guys, to where you just give it your agent URL locally and your agent URL in the cloud, and then boom, it works.</A>

▶ 01:51:21 - Brandon Hancock
The kicker that you guys will see is because Vertex AI doesn't stream, we have to poll. And because we have to poll, we end up consuming some of the credits — the rate limits are pretty small on Vertex AI. So there's just roadblock after roadblock right now, because it's all so new. It can work, it does work right now, but it's not perfect by any means. As soon as they fix it, I genuinely think they will be the winner in the race.

01:53:38 - Brandon Hancock
What are agents? What is ADK? It's really nothing more than a series of LLMs in a certain sequence that have tool calls. That's really what it is. So at the end of the day, you could always just straight up use the Generative AI library [tool:Google Generative AI Library]. That is solid — the Google Gen AI library is great. Zero complaints about it. And you can easily use it to do sequential workflows and tool calls — that's 100% doable.

▶ 01:55:29 - Brandon Hancock
Most businesses, like — oh, I need agents. No, dude, do you really? Like, you really just need four AI calls in a sequence. That's all you really need, which is totally good to do inside their Generative AI libraries right now. And they have voice, their voice is awesome. And they have video, which is awesome. They have all the base foundations of the pyramid set up perfectly. And now they're just trying to build layer two, layer three on top of the base.

01:57:09 - Jake Maymar
<Q>Brandon, do you see a trigger? I'm trying to figure out what's the market trigger where you think Google would be like, oh, we have to fix streaming, we have to make it production quality deployment that's easy to use.</Q>

01:57:46 - Brandon Hancock
<A>I know, I know — like, after the ADK competition, it was mostly just complaining of, hey, we would like to voice our — if it did X, this would be perfect. And it really is two things. A, I had to rebuild as a developer all sorts of Next.js to ADK functionality, which, if I'm having to do that, every single other developer on Earth is also having to do that — which is y'all's job. And then B, it's deployment. Those are the two main things. From my understanding, they're constantly adding new features, and I'm pretty sure they're going to be fixing all this, it's just how fast. And also, the more people that complain, the better, because then that pushes it on their priority map.</A>

▶ 01:59:59 - Brandon Hancock
The cool thing, Hemal, to answer another thing you'd find interesting — the cost structure for the deployed agents is stupid cheap. Because you're basically paying for when the agent's running, which is very affordable compared to most other places where you get one instance, you get to do three workflows, it's a hundred bucks a month because they're having to run the service constantly. But Google, they own compute, so they're happy just to spin it up whenever, because they own all the servers already. So they are set up to crush this — now it's just execution, in my mind.

---

<!--SEGMENT
topic: CI/CD Pipeline, EC2 Inference Architecture, and SOC 2 Compliance
speakers: Brandon Hancock, Juan Torres, Jake Maymar
keywords: EC2, Elastic Beanstalk, CI/CD, LLM inference, agentic systems, REST API, GPU, CPU, SOC 2, HIPAA, private network, microservices, containerization, LinkedIn, Waymo, Tesla Robotaxi
summary: Juan describes building a modular cloud architecture on AWS EC2 that separates LLM inference (GPU-optimized) from agentic workflow processing (CPU), communicating via REST API. This isolation enables SOC 2-compliant private inference without relying on OpenAI's API. Brandon encourages Juan to share this work on LinkedIn given high market demand for cloud AI engineering. Jake introduces the concept of autonomous vehicle fleets (Tesla Robotaxi, Waymo) selling GPU inference during off-hours as a novel distributed compute model.
-->

01:30:00 - Juan Torres
I'm helping the development team create a feasible CI/CD pipeline for going from the testing environment to the deployment phase in production. I'm trying to help the backend and the frontend developer unify their two separate microservices into one Elastic Beanstalk [tool:AWS Elastic Beanstalk] instance so we can put it into an environment that's near production, near deployment environments.

01:30:58 - Juan Torres
On my end, I already deployed an AI model in an EC2 [tool:AWS EC2] instance. So I have an environment for what is essentially an LLM inference engine, and then I'm creating another virtual environment for the agentic system, and they're going to be communicating through a REST API communication system. The reason that I'm separating both environments is because I do want to compartmentalize the different processes, especially because the application is just not going to be based on one simple agentic system — it's going to be several agentic systems. So having a differentiated, isolated inference engine is going to be really powerful.

▶ 01:31:55 - Juan Torres
Now there can be LLM inferences that are SOC 2 compliant, because now it's in a private network. It's not per OpenAI API [tool:OpenAI API] that you recall, and they use your data to train their models.

01:34:05 - Brandon Hancock
From my understanding, what you're doing is: cool, I have AI models — that is self-contained. I have my AI application — that is self-contained. That way I can hot-swap out the bottom. And that way they're not tied together, right?

01:35:00 - Juan Torres
For my specific services on the specific purposes of this project, it makes sense. Just because we're dealing with EC2 instances, and one of the things that EC2 instances have is they have a GPU with a certain amount of gigabytes and a CPU with a certain amount of gigabytes. So what I think is feasible from a computational engineering perspective is to partition and isolate GPU utilization just for LLM inferences, and then leave the rest of the CPU for agentic work, log processing, data, web application, monitoring.

▶ 01:36:22 - Brandon Hancock
Dude, please, please, please talk about this more on LinkedIn. I cannot express how many jobs I've seen that are people getting very high six figures or close to $200K+ for this exact type of work. Please talk about it, why you're making the decisions, give away all the secrets. I cannot tell you how many cool opportunities will come your way if somebody's like, hey, everything you did for them, here's our problem, please do it for us.

01:32:09 - Jake Maymar
Juan, when are you going to do the RoboTaxi?

01:32:18 - Jake Maymar
So the RoboTaxi — Tesla [tool:Tesla], Waymo [tool:Waymo], there's a couple of other ones. But they're really like eight GPUs rolling around. And so what they do is they find customers, they change their pricing depending on the cost for the car. But in sort of off-hours, it sells inference.

01:33:27 - Juan Torres
So you're saying that this Tesla Robotaxi or Robotaxi, when the car is not being used, essentially they're being a cloud computing service?

▶ 01:33:39 - Jake Maymar
Correct. And actually, sometimes when it is being used, it's still — as long as they can get to Starlink [tool:Starlink] — it depends on which one you're going with, but yeah, essentially you can sell inference. So essentially, yeah, it could be its own GPU server. Eight GPUs or something like that.

---

<!--SEGMENT
topic: Local LLM Hardware and Mini PC Specs
speakers: Juan Torres, Brandon Hancock
keywords: mini PC, AMD GPU, LPDDR5X, unified memory, local LLM, 7B parameter model, Ollama, hardware review, $2000, 128GB RAM, 2TB storage
summary: Juan shows off a newly purchased mini PC with 128GB LPDDR5X unified memory and a large AMD GPU, designed to run local LLM models. He reports it can run 7-billion-parameter models and cost approximately $2,000 for 2TB of storage. Brandon suggests this could be the basis for a YouTube channel reviewing AI hardware, and Bastian points to an existing channel doing similar GPU/model benchmarking.
-->

01:27:13 - Juan Torres
I got this for the Windows haters. That is the mini computer that I just bought. I think it's a beast.

01:27:25 - Brandon Hancock
<Q>What is it called? Give me some specs.</Q>

01:27:37 - Juan Torres
<A>The GMT, so it has 128 gigabytes of LPDDR5X. So you can then partition this to be — because it has a unified memory. It's with the big AMD GPU. Yeah, so it's a unified processing unit. You can actually run full-blown models, right?</A>

01:28:02 - Juan Torres
Yeah, I mean, you could run a 7-billion-parameter model on that one, but we'll see how that goes. I'm going to run some tests on it, but yeah, excited to test it out.

▶ 01:28:20 - Brandon Hancock
So you make a YouTube channel where all you do is buy cool gear and try and run models on them. That would be awesome.

01:28:54 - Juan Torres
It's only $2,000 as of now for 2 terabytes of memory. You can add more, but that will be the price to get it. And I did my research, and of all the computers and their specs, this was definitely top tier given its price. There was one that had the same specs as this one, but it was $200 less, but it had no reviews. So I just went for the one with decent reviews.

01:29:35 - Brandon Hancock
Bastian pointed out a channel that does exactly what we're talking about — he reviews it all side by side. [link:GPU/LLM hardware review YouTube channel referenced by Bastian]

---

<!--SEGMENT
topic: Quoting Agent Architecture and ADK vs. LangGraph Production Decision
speakers: Brandon Hancock, AlexH
keywords: quoting workflow, industrial suppliers, LangGraph, ADK, state management, database, wireframe, digital twin, multi-agent, tool limits, startup, production deployment
summary: Alex updates on his quoting workflow agent for industrial suppliers, having moved from in-state management to a database read/write approach for sharing quote state across agents. Brandon shares current ADK vs. LangGraph guidance: ADK is excellent locally but Agent Engine deployment is unreliable for production multi-tenant use, while LangGraph is more production-ready in the cloud. Brandon also highlights the value of Claude's digital twin feature for maintaining project context across commits.
-->

01:38:03 - AlexH
I think last time, if you remember, I'm working on an agent to be able to handle and manage specific quoting workflows for industrial suppliers. And last time, my question was around handling the quote in-state amongst multiple agents. And I actually went away from using in-state and now post to a DB that the agents have access to read/write from. So now I'm just kind of refactoring the state to handle what I needed to handle instead of the entire quote.

01:38:43 - Brandon Hancock
<Q>I know we briefly talked about wireframing it all and kind of how to tackle it, like how can we actually break it down to as many smaller actionable steps as possible. I was curious, any progress on that front, or is the database approach to where you're just calling to get the specific information at the right time helping?</Q>

01:39:07 - AlexH
<A>Yeah, I mean, I wireframed it all out, which helped. But I think a part of the challenge is, from a wireframe, it makes sense, like, when I'm like, okay, this is — but then in building, it's like, oh, this isn't actually working the way I thought it should. Kind of like to your point earlier, like, okay, more than five tools is too many. Yeah, I figured that out on the sixth tool. So I'm just working through what's feasible in production now versus what looks good on a wireframe and what makes sense in my head.</A>

▶ 01:39:46 - Brandon Hancock
Yeah, wireframe — great starting point, but you will quickly find it's a living document. Like, okay, well, that was a good hypothesis. It failed.

01:41:00 - Brandon Hancock
At the end of the day, after I do a commit, I just ask Claude to do my digital twin that you recommended, and rewrite my digital twin and post that into the .md file, and that's been pretty epic.

01:41:14 - Brandon Hancock
Yeah, cannot recommend digital twins enough.

▶ 01:41:28 - Brandon Hancock
ADK, phenomenal developer experience locally. Right now, their deployment process is very difficult — like a four out of ten on friendliness and reliability. So especially between Agent Engine and their deployment process right now, it is very difficult. So like, if you're working on an app that you might use plus three other guys, yeah, it is great, but the scalability right now of Agent Engine is just not really designed for big production, multi-tenant clients, at least from what I have found. That's why I'm very excited to dive into LangGraph, because LangGraph is more complicated up front, but running in the cloud, it crushes.

01:43:44 - Brandon Hancock
Is there much human in the loop, or is this very much like you just throw it in and then boom, a report's generated?

01:43:48 - AlexH
No, there is human in the loop. Yes, there is human in the loop. Like, call it a fair amount.

▶ 01:43:54 - Brandon Hancock
Yeah, right now, absolutely — ADK, their streaming capability on Vertex AI, Agent Engine — right now their streaming capabilities are just broken. Like, it's actually broken. So like, if you're just kicking off a workflow and you want ADK to do A, B, C, D, and then eventually spit back something, that's great, but a lot of quick back and forth — if you're in the loop, right now with Vertex AI, you kind of can't tell if the agent's doing something or if it's waiting for you. So just want to — the second it changes, I'll let you guys know. But for right now, on the cloud, it's playing a little bit hard mode. I want to save you heartache is the main thing I'm trying to say.

---

<!--SEGMENT
topic: AI Opportunity Window and Urgency to Build
speakers: Brandon Hancock, Sam
keywords: AI opportunity, commoditization, web era, mobile era, freelance, SaaS, Xero integration, MCP, accountant workflow, urgency, vibe coding, secure the bag
summary: Sam confesses to being behind on following up with a lead — his accountant who wants a workflow automation integrating with Xero. Brandon uses the moment to articulate his broader view that the current AI opportunity is larger than the web or mobile eras combined, and urges the group to build and ship as many projects as possible before the window closes through commoditization or autonomous AI agents.
-->

01:00:49 - Sam
I've been a bit slack. I've probably got one lead I need to follow back up on, and I need to do something with a client project that I've been working on. I've got a roadmap, so I probably need to update that. So there's a lot of just laziness on my part. So it's a confessional today.

01:01:10 - Brandon Hancock
That's fine. You are forgiven.

01:01:29 - Sam
It's actually my accountant who I used to help set up the business. He sat me down. He's like, this is my workflow. Can you do anything? And I was like, let me do this thing first and then we'll work on it. So it's quite complex in a sense that it integrates with Xero [tool:Xero], trying to integrate with Xero to do their workflow. And they have a lot of authentication and the steps to get certain parts of the data, so I just sort of have to go through and say, look, all things are doable, but it might be a lot of time to get there.

01:02:13 - Brandon Hancock
Oh, Paul just dropped a cool comment — they have a lot of MCP stuff now.

01:02:15 - Sam
Oh, yeah. Thanks, Paul. We'll have a look at that.

▶ 01:02:25 - Brandon Hancock
What's so cool, guys, just taking a step back, is we have an AI hammer, and the coolest part is — normally you don't always want to use a hammer to solve every problem, but you literally can do everything with AI and make it better. So that's why it is the coolest time to be alive, and I want everyone to try to build as many projects with AI as possible. A, I just don't know how long this opportunity exists, until it becomes commoditized or competitive. AI just does it itself, so I really don't know how many years we have.

▶ 01:03:00 - Brandon Hancock
The last two big opportunities were web, when the internet came alive, and mobile. But mobile was nowhere near as big as this one. And this one's bigger than both, in my opinion. That's why I don't mind working like a dog right now, because I genuinely don't know when we're going to get this opportunity again. Urgency is the main thing I want to get across — we gotta go.

---

=== UNRESOLVED SPEAKERS ===

The following speakers appeared in the transcript but were not present in the SPEAKER_ALIASES map and have been passed through unchanged:

- **Sam** — participant, asks about agent architecture and discusses an accountant/Xero workflow lead
- **Mitch** — participant, discusses Obsidian/Hugo/Fabric workflow and Asana MCP; identified as Excalidraw user and Instantly expert
- **Pedro Gomez** — new participant, building B2B lead generator for non-profits using Gemini CLI and Firestore
- **Prem** — participant, asks about RAG architecture, multi-tenant organizations, and ShipKit templates
- **Marc Juretus** — participant, building resume screening app; asks about email providers, Cloudflare, and ngrok
- **Bastian Venegas** — participant, comments on Superhuman and Cloudflare; mentioned in chat
- **Morgan Cook** — participant, discusses new freelance client onboarding and requirements documents
- **Jake Maymar** — participant, shares vibe coding horror story and discusses Fabric/Daniel Miessler; mentions Upstash
- **Andrew Nanton** — participant, suggests test-driven refactoring approach for spaghetti code
- **Juan Torres** — participant, describes EC2-based LLM inference architecture and mini PC hardware
- **AlexH** — participant, building quoting workflow agent for industrial suppliers startup
- **Adam** — participant, presenting AI demo at Reno Startup Week; scraped Google Maps with ChatGPT
- **Hemal Shah** — participant (also appears as "Hamal" in some turns — treated as same person); asks about wireframing tools, RAG vs. managed AI, and Google ADK deployment