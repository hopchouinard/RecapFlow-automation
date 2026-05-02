=== SESSION ===
date: Unknown (likely early January 2025, based on references to "new year" and Christmas)
duration_estimate: ~3 hours 30 minutes
main_themes: Claude Code / AI coding tools, ShipKit framework, RAG architecture, agentic systems, SaaS product demos, business development, TinySeed funding, embedding model migration

---

<!--SEGMENT
topic: Pre-call Chatter & Weather
speakers: Tom Welsh, Patrick Chouinard, Paul Miller, Morgan Cook
keywords: Quebec, UK weather, London, Whistler, Banff, snowboarding, British Petroleum, Ernst & Young, Mayfair, Ritz Hotel
summary: Participants exchange casual pre-call small talk about weather differences between Quebec, the UK, and Ethiopia. The conversation drifts into nostalgia about formal corporate dress codes at firms like British Petroleum and Ernst & Young in the 1990s. No technical content; serves as social warm-up.
-->

00:07:01 - Tom Welsh
I should remember my headphones.

00:07:04 - Tom Welsh
Hey, y'all.

00:07:07 - Hemal Shah
Hello.

00:07:09 - Tom Welsh
Hey, Hemal.

00:07:11 - Tom Welsh
Hey, Patrick.

00:07:13 - Tom Welsh
Hey, Tom.

00:07:16 - Tom Welsh
How goes it in the land of the snow?

00:07:18 - Tom Welsh
You must have a few feet now.

00:07:20 - Patrick Chouinard
No, actually, it's kind of weird. We had a lot over Christmas and now it pretty much all melted because it'd been raining for three days.

00:07:29 - Tom Welsh
Yeah, it's been raining for three days here, but there was no snow beforehand. It's about eight or nine degrees as well, which is probably warmer.

00:07:37 - Patrick Chouinard
No, it's like one or two here for now, but...

00:07:45 - Patrick Chouinard
The fun time of winter in Quebec. You can be on a snowmobile one day and on a watercraft the next.

00:07:54 - Tom Welsh
Yeah, see, typically I'd go to the west coast, go up to Vancouver and up to Whistler and those areas, Banff, perhaps Alberta. Snowboarding. I've never really done the East Coast.

00:08:04 - Patrick Chouinard
Like in the UK, it's flatter on the East than it is in the West.

00:08:19 - Patrick Chouinard
We have summers that can be just as hot and humid as New Delhi, and winters that can be as cold as the North Pole.

00:08:29 - Tom Welsh
Yeah, my wife's Ethiopian, and when she came across here, she's like, how is it 30 degrees in London? Because that's what we get.

00:08:40 - Patrick Chouinard
And like, where she's from, Addis Ababa, it's a constant 24 degrees, so six degrees makes a lot of difference to her.

00:08:48 - Patrick Chouinard
Yeah, six degrees here is between breakfast and lunch.

00:11:28 - Paul Miller
Yep, client meeting with our third largest client today. So got to be in the car, given it's midday my time.

00:11:46 - Paul Miller
When I started my corporate career was in London, I remember they had bowler hats when I was working in the city. I went between the floors of British Petroleum's head office without wearing my jacket. I was brought into HR, and it was really serious.

00:14:00 - Paul Miller
So in the summertime, you want to just have a beer after crawling around on the data centre floor, you have to wear a jacket.

00:15:05 - Tom Welsh
Like, American company — they bring hot meals into meetings. Like, okay. And then my contract company was next door. So they'd take me out for lunch. And it was like 30, 40 bucks for lunch because it was Mayfair.

---

<!--SEGMENT
topic: Claude Code & AI Coding Tool Comparisons
speakers: Patrick Chouinard, Tom Welsh, Morgan Cook, Brandon Hancock
keywords: Claude Code, Claude CLI, Cursor, WindSurf, Claude Cowork, skills, workflows, Git hygiene, vibe coding, anti-gravity, Gemini
summary: Participants discuss their hands-on experience with Claude Code, Cursor, WindSurf, and the newly released Claude Cowork feature. Patrick describes using Claude Code as a network admin agent, Morgan shares converting Cursor skills to WindSurf workflows, and Brandon introduces the concept of using Claude Code for non-development knowledge-worker tasks. The segment highlights the rapid evolution of AI coding tools and the emerging skill/workflow paradigm.
-->

00:09:00 - Patrick Chouinard
By the way, anyone tried the Claude Cowork? [tool:Claude Cowork]

00:09:04 - Tom Welsh
No, not yet.

00:09:07 - Morgan Cook
Really insane.

00:09:11 - Patrick Chouinard
It's basically Claude Code [tool:Claude Code] wrapped for knowledge worker and classic user.

00:09:18 - Tom Welsh
<Q>Are you using Claude Code, or Cursor, or Claude Code?</Q>

00:09:23 - Patrick Chouinard
<A>Well, Claude Code with Cursor [tool:Cursor] to do the debugging in the background and serve as the IDE, but all the code that's being created. And now I've tried to live in anti-gravity [tool:anti-gravity] for a while just to see if I can get rid of the Cursor payment.</A>

00:09:46 - Tom Welsh
Again, I'm talking with trying the Claude CLI [tool:Claude CLI] out. I've not really got into that yet. I've been stuck in Cursor. Do I want to make the jump? But everyone's been coming out since we see Claude CLI now.

00:10:01 - Patrick Chouinard
Actually, I'm building something on Claude CLI right now to be my network admin, basically.

00:10:14 - Morgan Cook
I've been using your skills that you built over the past couple of weeks, and they've been very nice. It's made the development cycle and the pattern clean and committed, or at least verifiable.

00:10:33 - Morgan Cook
And I've transferred them to — I use WindSurf [tool:WindSurf] — so I converted them to WindSurf Workflows.

00:10:42 - Morgan Cook
And then today, WindSurf came out with skills that support the exact same model as Cursor Skills.

00:10:51 - Patrick Chouinard
Yeah, honestly, I've been building skills for the past two weeks pretty much nonstop. I have a vibe coder in the office who, yeah, she learns how to vibe code, but not how to code. So Git hygiene is not in her vocabulary. Not because she's bad, she just never learned it, she never needed to. So I created a skill that managed branches for her.

---

<!--SEGMENT
topic: Brandon's Updates: ShipKit, Claude Code Workflows & Google Ads
speakers: Brandon Hancock, Morgan Cook
keywords: ShipKit, Claude Code, Google Ads, landing pages, avatars, funnels, EMS Soap, RAG, text embedding deprecation, Excalidraw, The Unicorn Project, task templates
summary: Brandon shares several updates: visual ShipKit documentation in Excalidraw, using Claude Code to set up Google ad campaigns with per-avatar landing pages for EMS Soap, and a heads-up that Google's text-embedding model deprecates the next day requiring a ShipKit RAG migration. He also recommends The Unicorn Project as a book for developers. Morgan discusses Lemon Squeezy vs. Stripe for one-off product payments and recommends Dan Martell's "Software as a Science."
-->

00:15:32 - Brandon Hancock
Hey, Brandon. How are y'all doing today?

00:15:42 - Brandon Hancock
So I shot out an email earlier for all things ShipKit [tool:ShipKit] related on things I owe to you guys. Good news — I've drawn out a ton of stuff in Excalidraw [tool:Excalidraw] to make the concepts easy to understand visually. So now the next step is actually just to go through each one, record, and show some actual code. So it's just not abstract concepts, it's actually in practice.

00:16:13 - Brandon Hancock
One of my goals this year is focus and fitness. So I've been going to the gym. Using Claude on your phone because the book I'm listening to right now is called The Unicorn Project [link:book-The-Unicorn-Project]. It's basically if you've ever read The Phoenix Project, it's like that, but more software focused. It's given me a million ideas. So every time I get an idea, I just talk to Claude on my phone. And it checks out a new branch for me, stubs it all out. I'm using task templates and everything else. So whenever I get back to work at my desk later on, I can take it all the way home.

▶ 00:17:09 - Brandon Hancock
If you do have the Claude Code subscription, seriously, when you're out and about just driving or anything — obviously don't get in a wreck — but I love to just brainstorm and give it ideas. And when I get home, work on it.

00:17:31 - Brandon Hancock
Cool new thing started literally last night — it's already seeming to work. Use Claude Code to set up your Google ad campaign [tool:Google Ads]. And it works awesome. So far we're already getting impressions, we're already getting clicks, and it's already doing decent for day one. And you can actually have it set up custom funnels per avatar. So it spun up new landing pages per avatar.

▶ 00:18:01 - Brandon Hancock
When you're thinking avatar or thinking Google campaigns or just paid advertisement in general, think funnels per avatar and have the same Claude Code make the ad that's also making the actual landing page.

00:19:12 - Brandon Hancock
Biggie, quick update for you before we kick off. We actually revamped the entire ShipKit pipeline for RAG, so the course, and we're also now working on the RAG SaaS itself because the text embedding model deprecates tomorrow. So that's one of the main reasons I'm a little late on recording the videos — Google's deprecating the main model we used for embeddings. So there's a whole migration guide that we worked on for you guys.

00:20:02 - Morgan Cook
I've been using it for a couple weeks, and it's been fantastic, especially the code review, and it's found several little problems that the roadmap didn't have mapped out, but after it was executed and implemented, the code review found weak points, so it's been very useful.

00:20:41 - Morgan Cook
One of the problems I ran into — I'm looking at Lemon Squeezy [tool:Lemon Squeezy] for one of them for payment on some individual one-off products. But man, Lemon Squeezy is really hard to get approved sometimes.

00:21:28 - Brandon Hancock
<Q>Quick question on Lemon Squeezy — what was the thinking on that one?</Q>

00:21:12 - Morgan Cook
<A>The thinking was more of the implementation in getting everything set up for a bunch of one-off products. It's not a SaaS subscription. It's one-off products at ten bucks, five bucks, whatever it is. I didn't want to have to go through that process of setting all up in Stripe [tool:Stripe]. Stripe can do it, but it's a lot more work. And then I have to manage all the products locally, instead of just letting Lemon Squeezy handle all of the products.</A>

▶ 00:22:07 - Brandon Hancock
I've heard they are more user-friendly. They just charge, I think, like 2% more on the processing fees. So it's a trade-off.

00:22:48 - Morgan Cook
I've been listening to Dan Martell, and he's got a lot of really great entrepreneurial advice.

00:22:59 - Brandon Hancock
The book is called Software as a Science [link:book-Software-as-a-Science-Dan-Martell]. We use this religiously. Think about your avatar — he has an entire playbook on that, an entire playbook on marketing and funnels that talks about lead magnets, everything else. He also breaks down some of the math on paid advertising conversions. And he has a beautiful playbook on how to do sales calls. The sales calls chapters changed everything for us, because as software developers, we're very guilty of just showing off all these cool features. He completely changes it and flips it on its head with the 3A framework.

▶ 00:24:26 - Brandon Hancock
The book Morgan's talking about, Software as a Science — please buy if you're thinking about doing your own B2B. It changes everything.

---

<!--SEGMENT
topic: Meta Smart Glasses & Gemini Image Generation
speakers: Brandon Hancock, Hemal Shah
keywords: Meta Ray-Ban glasses, Meta AI, Gemini 2.0 Pro, image generation, API cost, Nano Banana, prescription glasses, eye insurance
summary: Hemal asks about Brandon's Meta smart glasses, prompting a discussion of their practical uses including hands-free recording and AI queries. Brandon rates Meta AI a B grade. Hemal then shares his experience with Gemini 2.0 Pro for image generation via API, noting impressive quality but high cost at $0.14 per call, and Brandon suggests thinking about higher-value markets that could justify the API cost.
-->

00:24:51 - Hemal Shah
<Q>Are you using Meta glasses?</Q>

00:24:58 - Brandon Hancock
<A>Yes. Pull the trigger, man. It's actually cheaper to go through, if you have eye insurance, it's cheaper to get prescription Metas [tool:Meta Ray-Ban glasses] than it is to get off-the-shelf Metas. Gen 2, the new ones that last eight hours, they last all day. Really would recommend if you're gonna go full nerd, just commit to it.</A>

▶ 00:25:28 - Brandon Hancock
I use them literally all day. Especially if you've got kids — I got them for my sister too. It's the best way to record your kid doing something awesome, because you just say "hey, record" and it does it.

00:25:44 - Brandon Hancock
The AI — I'm gonna give it a B, just a flat B. Meta AI [tool:Meta AI] is not where it needs to be. It's getting smarter, but it will get better in the future.

00:26:02 - Hemal Shah
So regarding one thing that I was playing with — image generation that I was mentioning last week using Nano Banana, Gemini 2.0 Pro version [tool:Gemini 2.0 Pro]. I went through things that you mentioned last time, and it worked out pretty well. The iterative process was good. But it's expensive — it's 14 cents per image or per API call for that particular model. But it's doing awesome jobs. I'm really impressed with that.

00:26:36 - Brandon Hancock
The hard part about the cost is using the same API endpoint to solve different problems is worth a thought — it completely changes everything. So like a radiologist using this call versus us playing with toys. The same API can be used for all sorts of different things. One thing — I think his name was Alex on the call maybe two months ago — he was using image models, like these image APIs, to help contractors look at spec sheets, and those contractors were willing to pay out the wazoo to help make sure they had the right quantities of everything.

▶ 00:27:22 - Brandon Hancock
You're getting good at using these tools. I would always just think: what are other markets that would pay a lot more to do the same workflow you have? It could be used for 1,000 different archetypes of problems.

---

<!--SEGMENT
topic: Marc's Personal Dashboard & Energy Rate Tracker
speakers: Marc Juretus, Brandon Hancock
keywords: Claude Code, Marc's World, YouTube summarizer, SQLite, Supabase, energy rate scraper, Rapid API, Apify, JustWatch, Next.js, vector stores, SaaS idea
summary: Marc shares his personal learning project "Marc's World" — a dashboard built with Claude Code that includes YouTube video summarizers, a TV/movie release tracker using Rapid API, and an energy rate monitoring tool that scrapes utility providers and alerts users before variable rates spike. Brandon identifies the energy rate tracker as a strong SaaS candidate with a clear pain point, recurring revenue potential, and a built-in marketing angle from social media complaints about high bills.
-->

00:29:21 - Marc Juretus
So I was trying to learn Claude Code a little more, because I basically was using Cursor and some other things for my development. So I basically created — it's called Marc's World, it's corny — but it has in-feeds where it's doing a summary of YouTube videos. And then I'm trying to get it to do like a TV monitoring thing, where it's pulling in recent releases, I give it kind of what I want to watch, it makes suggestions. And another one I have that I actually enjoy is — I don't know if you guys have the deal where you have the energy rate for, like, you have to change your kilowatts, you pay for different rates — the rate may fix for three months, and if you don't reset it, it goes back to a variable, so you might be paying 10 cents a kilowatt, next thing you know you're up at 18, you have a huge bill. So what I have it doing is I put in my rate — it's kind of like a SQLite [tool:SQLite] backend — and basically it goes to these couple sites and tells me the five best rates and reminds me, hey, your plan's about to go away.

00:32:14 - Marc Juretus
So it's kind of like me consuming Claude Code. The one good thing about Claude Code is I don't have as much time as you, but basically I have like an hour or two and then I'm actually out of my Claude. So you just do your hour a night where you run out of tokens and come back the next night.

00:32:50 - Brandon Hancock
Mark, I mean, I think you already said one with the energy saver — it directly solves a money problem for people. Like that, the second you said that, I was like, I think that would be a very cool project. You're just doing scraping and monitoring people to see — basically people are going through a pipeline, they're inactive during two and a half months, and in that final two-week period you're just blasting the reminders letting them know here's the best deals right now.

▶ 00:33:00 - Brandon Hancock
You can charge a quarterly subscription or monthly subscription or yearly, and you can charge up front for an annual contract because it happens four times a year. Everything about that checks all my initial boxes for a great idea.

00:34:48 - Brandon Hancock
The craziest part is you take a scraper, go off and find a hundred of those comments from people complaining about high bills, and that is your entire marketing campaign. You just copy a hundred screenshots from other people and say, do you want to end up like these guys? They didn't use my stuff. The entire business plan is there.

00:35:30 - Marc Juretus
<Q>Does anybody out there have a better feed for pulling in TV and movie releases? Like some type of RSS feed? I see sites like JustWatch [tool:JustWatch] or what's on Netflix.</Q>

00:36:09 - Brandon Hancock
<A>Paul just dropped a good suggestion on Apify [tool:Apify]. That's literally what I would go with — you're gonna have to pay for it, but you're gonna pay like 10 bucks, it's not gonna break the bank.</A>

▶ 00:36:26 - Brandon Hancock
Quick creative tip: when it comes to Claude Code and creative work such as laying out a new landing page or building a new feature, I created five work trees and basically gave each one of them the exact same prompt. I did four work trees with Claude Code and one with anti-gravity. Gemini did the best design actually, but the code was bad, so I had Claude Code come in afterwards and fix it.

▶ 00:37:35 - Brandon Hancock
Any time you're going to do bulk creative work, just don't even guess — have it do it five times in parallel, and you pick the one you like, then kill all the other ones.

00:38:17 - Marc Juretus
It definitely does help. Like all the stuff that I learned — Next.js [tool:Next.js] to the vector stores and all that — now I understand more what it's doing, and I can focus more on what I'm trying to accomplish. For example, it's SQLite now, I'm like, I gotta move this up to Supabase [tool:Supabase], because I have too much data at this point.

---

<!--SEGMENT
topic: Paul's Territory Compass App Demo
speakers: Paul Miller, Brandon Hancock, Elijah, Juan Torres
keywords: Territory Compass, traveling salesperson problem, DocPloy, Docker, Clerk, Vroom, OR-tools, RAG, NotebookLM, PRD, Claude Code, ShipKit, multi-level security, GitHub
summary: Paul demos Territory Compass I.O., a live SaaS app for optimizing field sales routes using the traveling salesperson problem, built entirely with Claude Code without writing a single line of code. He discusses the tech stack (DocPloy, Docker swarm, Clerk auth, Vroom/OR-tools APIs), an auto-updating help center that reads GitHub commits, and multi-level security. He also shares RAG-related resources including a YouTube channel on agentic RAG approaches and a technique using NotebookLM as a free RAG backend. Brandon and Elijah ask follow-up questions about RAG security, ShipKit's RPC filtering, and PRD quality.
-->

00:40:54 - Paul Miller
So I was saying to Brandon the other day that I've taken a ShipKit design project. It's gone live with a major global consumer goods business as the pilot customer. So we're live now with that.

00:41:45 - Paul Miller
There's a YouTube channel — it's prompt engineering, Muhammad's really good — he's focused on RAG and the evolution of RAG. He's like a PhD in data science. What he's talking about is, if you've got the complex context where you've got references to multiple documents — because if you go down the RAG path, you chunk parts of documents, and it doesn't get the full context if there's multiple documents — he looks quite differently from more of an agentic approach of looking at multiple documents, linking the multiple documents and the context between documents, as well as how you tie that back together with what you'd normally do with a RAG.

00:42:59 - Paul Miller
He's got a little open source project. I haven't tried it yet, but I have worked with Mohamed in the past on some client stuff, and he really, really knows his stuff.

00:43:36 - Paul Miller
The other one that was quite useful — it's all about making good PRDs. The post was talking about making sure, because one of the issues with getting AI to write the PRD is it often loses track of committing to the context of the intent of what you're trying to do, rather than just being so focused on giving you a list of sub broken-down deliverables that it forgets some of the nuanced parts of what the app should do.

▶ 00:44:24 - Paul Miller
He's adding an extra paragraph to say, look, while these are functional things that we want to do, the following things are really important to the core of the application — and making sure that that flows through to the AI dev tool.

00:45:16 - Paul Miller
Yeah, this is the app, basically. It's live. It's called Territory Compass I.O. [tool:Territory Compass] It does need authentication, and I use Clerk [tool:Clerk] for authentication. It basically gives you — you can define a number of territories where you've got all your sales calls. This is basically an app that helps organizations that have got people on the road that you need to go and visit things, so it deals with the traveling salesperson problem.

00:52:30 - Paul Miller
This has built it into a stack using a number of different APIs around Vroom [tool:Vroom] and OR-tools [tool:OR-tools], where I can optimize in a whole lot of different ways — visit prioritization, revenue, or method of how often visits are done — and it'll come back with what each scenario will save, and what extra time it will give you in the stores, or on the road, or in terms of delivering sales outcomes.

00:53:52 - Paul Miller
Claude Code automatically built a help centre, and it's got a little engine that goes and updates all the questions that people want. It goes into GitHub looking at all the requests that have gone through and all the updates, and then processes that. I'm going to convert that into non-geek speak to more customer-centric — what were the changes and why did those occur?

00:54:42 - Paul Miller
I've added a skill with Claude Code to know everything about working with Clerk and also working with DocPloy [tool:DocPloy], because I use DocPloy. Instead of using a traditional host, I'm just getting a VPS that I run. This is made up with six different Docker [tool:Docker] apps, so it's running as a Docker swarm.

00:57:13 - Juan Torres
<Q>Why did you decide to use DocPloy? Is that the best rapid way to do it, or are there scalability plans?</Q>

00:57:26 - Paul Miller
<A>It's so much easier to use than the other products that do the same thing. It's really, really logical. And if you look at people doing comparisons between DocPloy and other similar platforms, DocPloy usually always wins. For those who don't know what DocPloy is, it's basically an alternative to using Amazon or Azure — a whole management of your back-end ecosystem. Instead of using Vercel [tool:Vercel], you would publish to DocPloy.</A>

▶ 00:58:01 - Paul Miller
You can do things like setting up a DocPloy skill, so then you can get your Claude Code to master when it's preparing applications or repairing your back-end, then you can get it to do all that hard work for you, because becoming a DevOps expert on a back-end is no easy thing when you might be doing this part-time.

00:59:29 - Elijah
<Q>Is there permission for those sales calls to be viewed by certain people, like role level, so that not everybody can RAG all of the calls within the organization?</Q>

00:59:53 - Paul Miller
<A>It's multi-level security. Top-level SaaS agent, then you've got a single company that might assign the ability to create regions or do stuff, and then you've got the base user that really just wants to be able to see the maps and see the plan.</A>

01:00:32 - Brandon Hancock
<A>On the RAG query, the way it's set up right now, I think you query documents that are tied to a user ID. But if you look up the RPC function — it's called match text chunk — you literally just have to add one line in there when you're doing your filtering. So I want to get all chunks for user 123 and in organization ABC. It's a one-line change.</A>

▶ 01:01:14 - Paul Miller
One point out there to the newbies and the people that are not feeling so technically comfortable: I haven't written a single line of code. All I did was the prompts and the env file.

00:46:18 - Paul Miller
Talk about another one on the RAG side of things — it's where you add a skill that uses NotebookLM [tool:NotebookLM], multiple NotebookLMs, as your RAG libraries. So you build an agentic front end, and it uses in the back end your own NotebookLMs to access content. Hundreds of documents, all for free.

---

<!--SEGMENT
topic: Patrick's Agent Army & Agentic Architecture
speakers: Patrick Chouinard, Brandon Hancock, Juan Torres, Ty Wells, Elijah
keywords: Claude Code, MCP servers, skills, agents, Ubiquiti, Proxmox, VLAN, N8N, Context7, YAML front matter, agentic loop, documentation schema, network engineering, home lab
summary: Patrick describes a methodical two-week process of building a Claude Code-based network engineering agent for his home lab, starting with extensive spec and documentation work before writing any code. His architecture layers agents over skills over MCP servers, with security enforced so only skills can call MCPs. He explains how he optimized documentation with YAML front matter for efficient agent indexing rather than full RAG vector search. Brandon highlights the importance of thinking through the full agentic lifecycle — how agents read, act, and document for future sessions.
-->

01:03:35 - Patrick Chouinard
In the last week, I've really, really dived into creating my own agent army using Claude Code. I really want Claude Code to become my cloud engineer, basically. Right now, I'm focusing on a network engineer, and I want to add some infrastructure also, because basically, I can do it manually. I know how to manage an infrastructure. I just don't want to waste time doing it anymore inside my house or in my own lab. So I just want to give that to Claude Code to manage.

01:04:37 - Patrick Chouinard
So I've spent basically two weeks on documentation, on specs. I just started tonight creating the first line of code for it. Everything I've worked on was literally spec, spec, spec, spec, rereading, going back, improving the specs again. And actually, I even took what I thought was finished, loaded it completely into ChatGPT [tool:ChatGPT], went to the gym, chatted with ChatGPT all throughout my gym session to revalidate every assumption, to make sure that phase one was as complete and solid as possible.

01:05:33 - Patrick Chouinard
And basically, I came up with a four-step process. I create a web scraper for the vendor documentation. So in my case, I have a Ubiquiti Dream Machine [tool:Ubiquiti Dream Machine], so I want the Ubiquiti site to — basically, I've created a very, very small, very specific version of Context7 [tool:Context7] for infrastructure documentation. And I've changed the documentation to fit into a specific pattern to be optimized for Claude Code.

01:06:07 - Patrick Chouinard
And to answer Elijah's question earlier, whenever Claude Code actually navigates documentation, yeah, it looks like a RAG, but if you want it to be optimized — the front matter YAML in there — it's really, you can see it as if it was an index in a database. So it's not as much RAG in terms of vector closeness; it's more, here's an index that tells you what's in that file, just so it can find it without reading and wasting tokens reading the whole thing.

01:07:03 - Patrick Chouinard
The second step, I actually go in to create all of the MCP servers [tool:MCP servers] that are going to be needed because, surprise, surprise, in the infrastructure world, there is not that much MCP to interact with their APIs. And afterward, I have all of the skills built for that specific piece of hardware, as well as the slash command, and last is the agent that orchestrates the intervention of all of this together.

01:07:44 - Patrick Chouinard
Basically, the agent will use the skill, the skill will use the MCP. Doing that, I can actually make sure that from a security perspective, only the skill has access to call the MCP, and only the MCP can do the modification, so the agent can never do a modification directly.

01:08:00 - Patrick Chouinard
And the agent has a clear rule that it cannot consider a modification done before it actually creates the documentation of what it changed — written optimized for itself. So the next time I can ask it, why is that not working? Well, it has a history of what it did before.

▶ 01:08:28 - Brandon Hancock
Before doing any coding, Patrick did the hard part, which is thinking. When you're about to build an agent that's going to do your work going forward indefinitely, it's worth spending a day fully thinking through what perfect looks like. Everything that you have learned over your professional career — put it in a document. That's the hardest part. It's the most unfun part, but then the next day you're like, oh my gosh, I thank previous me for doing this.

01:10:46 - Patrick Chouinard
Just to be clear, it's not that I know all of those things — it's that I know how to ask the agent to make sure that it gives me all of that knowledge. Because I didn't say, here is a schema of the file you need to create for documentation. I said, I want you to create a schema that will be optimized for yourself to understand it when you come back.

▶ 01:11:08 - Patrick Chouinard
I'm using the AI agent to help you help it help you, basically.

01:11:17 - Patrick Chouinard
Right now I'm doing it atomically for one piece of hardware, but I already have phase two, three, and four thought about at a high level — Proxmox [tool:Proxmox], then network services, DNS, DHCP, all those. But the idea is that at the end, I want an agent over all of those agents — basically a coordinator that's going to take care of asking every agent whatever it needs.

01:15:28 - Patrick Chouinard
Actually, all of that is to get to the point where I can have a secure N8N [tool:N8N] server in a correctly partitioned VLAN on my own network that I can expose to the outside world, so I can send the stuff coming from the little voice recorder to be processed internally.

---

<!--SEGMENT
topic: Claude Cowork Privacy & Google Drive Classification
speakers: Patrick Chouinard, Ty Wells, Brandon Hancock
keywords: Claude Cowork, Google Drive, document classification, Anthropic, data privacy, Bitwarden, sensitive data, knowledge worker
summary: Patrick demonstrates using Claude Cowork to reclassify over 30,000 Google Drive documents in approximately 15 minutes. Ty raises a legitimate privacy concern about what data Claude Code and Cowork can access on a user's computer. Patrick clarifies the distinction between sensitive and non-sensitive files, and both agree users should exercise judgment about what files they expose to the tool.
-->

01:16:21 - Patrick Chouinard
I hope I've not built all of that for nothing, seeing what Claude Cowork — I just saw that yesterday. I had it reclassify my entire Google Drive [tool:Google Drive] and did a job that I've been putting off for like two years. It reclassified over 30,000 documents in about 15 minutes, if even.

01:16:53 - Ty Wells
Just sorry to interrupt you, Patrick, but I'm just on that Cowork — those documents that it's reading to classify them, where is that information going?

01:17:03 - Patrick Chouinard
Oh, yeah. The documentation I'm talking about is not internal sensitive information.

01:17:15 - Ty Wells
No, no. I'm just speaking generally. And like, that information — they've got access to all your stuff that's on your computer. It's Claude Code.

01:17:23 - Patrick Chouinard
It's just a wrapper around Claude Code for knowledge worker. So if you are ready to use Claude Code to work with those files, well, having Cowork classify them, it's no different.

01:17:40 - Ty Wells
Yeah, well, I don't think I'll have Claude Code working with the files that are on my computer. They're on there for a reason. They're sort of personal.

01:17:51 - Patrick Chouinard
Yeah, obviously, I would never use that to classify my health information, my financial information, all of that. But there are files on my Google Drive that are not sensitive whatsoever. All the sensitive stuff is in the Bitwarden [tool:Bitwarden] vault.

▶ 01:18:13 - Patrick Chouinard
But for that concept of reorganizing or doing work that is not development, it's pretty insane.

01:18:24 - Brandon Hancock
I'm trying to get my wife — she's a consultant — to get her to start using Claude Code at her company, because I was like, you will be seen as a god amongst regular consultants that aren't using it.

---

<!--SEGMENT
topic: RAG Embedding Migration & ShipKit Template Selection
speakers: Brandon Hancock, Prem, Elijah, Lan, Patrick Chouinard
keywords: RAG, text embedding, Google text-embedding, Supabase, vector dimensions, database migration, ShipKit templates, chat template, RAG SaaS, Shipkit Mentor GPT, Claude Code, work trees, anti-gravity
summary: Brandon announces that Google's text-embedding model deprecates the next day and walks through the migration plan: re-embedding existing text chunks into a new column with higher vector dimensions (768 → 3072+), then dropping the old column. He advises new RAG projects to wait for the updated repo. Prem asks about anti-gravity vs. Claude Code, and Brandon clarifies anti-gravity excels at UI/UX prototyping but not code quality. Lan gets live help with GitHub auth and ShipKit repo selection. Patrick introduces the ShipKit Mentor custom GPT for template selection guidance.
-->

01:22:37 - Brandon Hancock
I know you have your RAG application. So text embedding — which we're using from Google — dies tomorrow. So I'm actively working on doing the transition and making a video for you guys so that you can see how to transition from the old version to the new version. We've already coded it all.

01:23:00 - Brandon Hancock
In our database, we have a thing called Document Chunks. The Document Chunks column has a text chunk, which is literally the actual raw text. Directly next to it, we have the embedding — that's like 768 vectors, a vector of 768 dimensions. Using the new model, it goes to 3,000 something. So we have a script for you guys that you run, where it takes all the old text chunks, re-embeds them, puts them in a new column, and then afterwards we go through and drop the old one.

▶ 01:23:52 - Brandon Hancock
Anyone who's currently using the RAG template — that'll be coming out. If you're starting a new RAG project from scratch, it'll just have the updated stuff. I'll do Discord and an email for that one when it's ready.

01:25:50 - Elijah
<Q>Is that update currently in ShipKit, so if I start a new project and pull it down new, it'll have the new stuff in it?</Q>

01:25:21 - Brandon Hancock
<A>I would, if possible, at least wait one day, just because I would need to review his things that he added. I'll do Discord and an email for that one when it's ready.</A>

01:25:50 - Prem
<Q>You mentioned anti-gravity. Did you kind of move from — have you started using anti-gravity or any videos on that?</Q>

01:26:00 - Brandon Hancock
<A>I use anti-gravity one out of 100 requests. For AI. Like, half the time, it's just for an experiment. Because the quality of code — the more I've experimented with it, it is not as good as Claude Code, just period. However, its understanding of UX and UI is better than Claude Code. So I spun up five work trees to test out a new grading feature — four were Claude Code, and one was anti-gravity. The one that looked the best was anti-gravity. However, there were numerous errors on the implementation. So I had to come back with Claude Code to fix it.</A>

▶ 01:27:03 - Brandon Hancock
I'm strictly using anti-gravity for prototyping new UIs that I then clean up with Claude Code.

01:27:29 - Brandon Hancock
My Claude Code usage went from like nothing to like 20% in a day before lunch. And I'm on the max plan. So I was burning through tokens, but it's the coolest way to rapidly experiment because code is cheap at this point.

01:49:03 - Lan
Brandon, I am the one who had a problem pulling down the repo, but I sorted it myself, and thank you very much.

01:49:32 - Lan
I think I will create a video. Hopefully, I will document my hurdles, just for those people, if they have problems pulling it down.

01:50:35 - Brandon Hancock
So all you have to do now — could you run shipkit-ai and then just do test or something?

01:50:44 - Lan
Yeah, it works now, because I tested it.

01:50:52 - Brandon Hancock
So you do have access to the repository. So what issue are we running into now?

01:50:59 - Lan
So, because of that, a couple of things. First of all, I actually accidentally downloaded the chat repository into a run project. So my question is, can I just remove that?

01:50:04 - Brandon Hancock
Yeah, you can delete it, and then if you wanted to add it back two seconds later, you could just git clone and do it again.

01:51:20 - Lan
And second question is — I found that each stage I need a different repo. For instance, right now I think the chat repo fits my project. But as time goes along, I realize, oh geez, I need some RAG repo as well. So how do I move ahead step by step?

01:51:44 - Brandon Hancock
<A>So if you're going to be doing RAG, the difference between chat and RAG is huge. If you clone the RAG project, you're going to see inside of there, there's like four or five projects. That's why if you're thinking about RAG, you really want to, from the get-go, use RAG. Under most circumstances, if you're on chat and then you want to start using the worker SaaS, you could basically add in the worker SaaS as a secondary project into AI Docs references, and then just say, hey, my current project is a chat-based application, however, I now want to start doing some background jobs. Please look through the reference project, worker SaaS, and understand how it's building things out. Can you please update my current project?</A>

▶ 01:52:21 - Brandon Hancock
I would usually pick the most complicated project as the starting point, which is RAG. So if you are going to do RAG, that is the most complicated starting project of all the repos here.

01:54:39 - Patrick Chouinard
If you go in the community repo, I created what I call the ShipKit Mentor [tool:ShipKit Mentor GPT]. It's the first prompt wrapped into a custom GPT. It will tell you at the end, oh, for that project, the recommendation would be to start with X template, because it's complicated, and that would be easier to start from this one than add the other thing.

---

<!--SEGMENT
topic: EMS Soap Funding, Business Model & Sales Strategy
speakers: Brandon Hancock, Maksym Liamin, Juan Torres, Andrew Nanton
keywords: EMS Soap, TinySeed, HIPAA, SOC 2, Vanta, ambulance billing, medical documentation, RAG, Raul, YouTube channel, co-founder, pre-seed funding, Google Ads, Alex Hormozi, Russell Brunson
summary: Brandon reveals that EMS Soap received TinySeed pre-seed funding, explaining the product helps ambulance companies and fire departments improve medical billing documentation accuracy using RAG against medical protocols. He describes how the co-founder Raul, a fire chief in Florida, provides domain expertise and customer access. Brandon shares the founding story (YouTube → cold outreach → partnership), advice on co-founder equity splits, and the importance of public visibility for developers. Maksym asks detailed questions about the funding structure and HIPAA compliance.
-->

01:29:23 - Andrew Nanton
I wanted to make sure I hopped on today because I'm glad to hear you'll be back around some more, but mostly just to say thanks and to kind of reflect back on this crazy year of 2025 and how much things have changed, how much I've learned.

01:30:00 - Andrew Nanton
From the end of last year, with GPT-4.5 [tool:GPT-4.5] and Claude 4.5 [tool:Claude 4.5], things really changed a lot — there really was a shift, at least for someone who, like, I'm not a programmer by trade. That was a really big shift in what was possible.

01:30:26 - Andrew Nanton
That article that I posted — that guy, Steve Yegge, he's a programmer who used to work at Google. I posted a talk that he did with Gene Kim, the guy who wrote the Phoenix book that you like so much. Those two are working together right now on this agentic programming thing.

01:49:28 - Maksym Liamin
Hey, Brandon. I just wanted to join mostly to congratulate you. I saw the news. It's amazing. I logged in on the webpage and tried to read what actually you do, but I just wanted to ask you a little bit more — like, what is the actual product, how it works, how much you raised, if you can disclose it.

01:50:16 - Brandon Hancock
It wasn't a million, I'll say that, but it was a good starting chunk. Bank account was very happy.

01:50:42 - Brandon Hancock
That's the reason why people usually go with TinySeed [tool:TinySeed] — they're usually on the smaller side, basically smaller startups. I think they're technically pre-seed. It's not even a series A. It's like a pre-seed, basically. So they're not doing huge takes because they know most likely there's going to be A, B rounds going forward.

01:51:08 - Brandon Hancock
I had to write my first $16,000 contract today to buy something — Vanta [tool:Vanta]. If you're doing SOC 2, HIPAA, anything like that — yeah, so it was 16K, just to give you guys a heads up on big-boy costs. But if you're working with the government, you pretty much have to pay it.

01:51:22 - Brandon Hancock
Okay, so what we do — we help ambulance companies and fire departments with their medical billing. The problem is, here's the average day of EMT personnel: they're working in a busy city, they're going to houses, picking up people, addressing — it's a full-on ambulance. They have to help the patient out, transport them, stabilize them, then get them back. As soon as they're done, they have another call waiting. And during all of that, they have to write proper documentation to justify everything that happened. Insurance looks at that document and goes, did you do it right? If you mess up anything, they're going to say denied.

01:52:56 - Brandon Hancock
We do a lot of RAG stuff. We look at their medical protocols — what does the government and private recommendations require to write a proper report? And we help them do that. So we've helped people make a ton of money in reimbursements.

01:54:05 - Brandon Hancock
YouTube, man. That's why I always tell everyone, start a YouTube channel if you're a developer. It just opens up doors that you would have literally never guessed would exist in a thousand years. He, in May, just happened to see one of the videos I was doing on Google Cloud when I was doing a lot of deployment videos on the ADK and everything else. And he's like, oh, this guy seems cool, and reached out.

▶ 01:54:33 - Brandon Hancock
Put yourself out on the internet, because things come that you literally would have never guessed in a thousand years. Even if you're the world's best AI engineer, if no one knows you're good, good things literally can't come to you.

01:55:32 - Maksym Liamin
<Q>Do you have to be HIPAA or SOC 2 compliant because you're dealing with maybe medical records?</Q>

01:56:12 - Brandon Hancock
<A>The answer is no. Think of us as an AI calculator. Non-HIPAA information comes in, non-HIPAA information comes out. We actually ask you and check boxes — I will not give people's information, because we don't need it. To do the work, we don't need Bob Smith. We just need to know "patient." That's literally all we need to know to do compliant documentation.</A>

▶ 02:00:33 - Brandon Hancock
As the developer, make sure you get a 50/50 split. I think that's important, because without you, the business is dead; without your co-partner who's selling, the business is dead. Both of you should be working on it religiously.

▶ 02:01:22 - Brandon Hancock
The playbook that's been working well so far: as a developer, what is your unfair advantage? It's to build. Please, please, please partner up with someone who has an unfair advantage in the domain. Raul is the chief in one of the biggest counties in Florida. He knows the entire state. Every day he's talking to our customers, which is the biggest unfair advantage.

---

<!--SEGMENT
topic: Model Selection, Latency Optimization & GLM 4.7 Discussion
speakers: Brandon Hancock, Bastian Venegas Arevalo, Patrick Chouinard, Juan Torres, alexrojas
keywords: GLM 4.7, OpenCode, Claude Sonnet, Gemini 2.5 Flash, GPT-4.1, OpenRouter, TTFT, throughput, Grok, Perplexity, Exa, NotebookLM, WhatsApp webhook, parallel API calls, promise.all, caching, Elixir
summary: Bastian shares his agent work integrating Perplexity and Exa as search tools, and NotebookLM for research. The group discusses GLM 4.7, a Chinese model offering near-Claude Sonnet quality at dramatically lower cost (~$24 for 3 months), best used for code review and PR analysis rather than primary development. Alex demos a music studio booking app with WhatsApp/Instagram/Messenger webhook integration and asks about latency optimization. Brandon walks through OpenRouter to compare TTFT and throughput metrics for GPT-4.1, Gemini 2.5 Flash, and Gemini 3 Flash, recommending parallel API calls over caching for real-time availability data.
-->

02:25:42 - Bastian Venegas Arevalo
I've been keeping, continuing to work on the agent that I showed last week, and just kind of revamping the user interface. Now I added Perplexity [tool:Perplexity] as an agent, and also as a tool for my agent. I have Exa [tool:Exa] as well, which is a very nice web search provider, and you can go insane amounts of queries a day if you kind of switch in between both.

02:26:25 - Bastian Venegas Arevalo
They made some updates in the last few months to NotebookLM [tool:NotebookLM], and it's improved a lot. For example, I wanted to explain the database trade-offs and the caching for level one and level two in Elixir [tool:Elixir], and it made a really great podcast and a great roast for the way I had it set up.

02:27:11 - Brandon Hancock
<Q>I actually got an email about this yesterday. You're using GLM, right? The China model? So thoughts on it for inside Claude Code. Like, what would your practical tips be? Would you say use Claude Code to come up with a task plan and then GLM to implement? Just use GLM the whole way through?</Q>

02:27:38 - Bastian Venegas Arevalo
<A>Yeah, I think it depends. I actually use it inside OpenCode [tool:OpenCode]. It wasn't really ideal inside Claude Code because it didn't behave around the to-dos, which I think is really vital for the way that you code if you do it by tasks. But in OpenCode, I've used it to generate some really great code reviews — so like an external pair of eyes to review and roast your code base.</A>

02:28:49 - Bastian Venegas Arevalo
So Bastian showed, I think maybe three weeks ago at this point, that there's a model called GLM 4.7 [tool:GLM 4.7], which is like a Chinese model, but it's insanely powerful and it's insanely affordable — meaning like you pay 24 bucks and you have access to this model for three months. And you have super high limits, way higher than what Claude gives you.

▶ 02:29:26 - Brandon Hancock
It looks like a really cool backup for those who are more cost-sensitive. However, they don't mind maybe babysitting the model a little bit more. It looks like an awesome substitute if some of those boxes check.

02:29:47 - Patrick Chouinard
If you're like in cool-down time for Claude, for example, in your subscription, you can take some time to really take a look into the pull request. It's a good companion for thinking and for sharing what you think you should do about the app.

02:30:35 - Bastian Venegas Arevalo
And then Juan just shared an awesome post — basically, GLM 4.7 is right below Claude Sonnet 4.5 [tool:Claude Sonnet 4.5], which is still an insane model. It's almost 4.5 Sonnet-level capabilities, but like a stupid reduction in price. It's better than Haiku, for example, if you would compare it to the Claude plans.

02:31:00 - Bastian Venegas Arevalo
<Q>Did you think about maybe even using the Claude Delegator plugin? Where Claude Code can actually delegate tasks to other coding agents like Codex or Gemini CLI or OpenCode, so you can do all of the costly token tasks by OpenCode, but have it reviewed and monitored by Claude Code?</Q>

02:31:24 - Bastian Venegas Arevalo
<A>Yeah, that's a very cool way of implementing it. I did try it, but I didn't stick to it. But it's definitely interesting. It depends on how much babysitting you're willing to do.</A>

02:31:43 - Brandon Hancock
That's the idea behind this — you let Claude Code do the babysitting because the babysitting is not token-intensive. And you can use the hook to capture the to-do list. You can also use hooks to capture the plan, so you can decide to include some of that as a file that can be referenced by the sub-agent.

03:16:41 - alexrojas
So this has all the availabilities, all the information. Here you can see the four rooms, and then this is the quick fix for availability. So you can just go quick, click here very fast, and put in your email information. Really quick, and it sends you to Stripe — one click — and there you get your reservation done.

03:17:17 - Brandon Hancock
<Q>So I did ask Claude, and this is the question I wanted to ask you guys — they proposed me that I do cache with Redis Upstash, and to change from OpenAI to Grok. I think you mentioned in one call that Grok could reduce latency as well.</Q>

03:17:30 - Brandon Hancock
<A>Yeah, so if you just open up OpenRouter [tool:OpenRouter] real fast, I'll show you a few things that I always look at. So the two models I recommend for end-user applications are GPT-4.1 [tool:GPT-4.1] and Gemini 2.5 Flash [tool:Gemini 2.5 Flash]. The things you need to know are latency — time to first token, TTFT — one of the most important numbers that you need to think about as an AI developer, because if it takes 10 seconds to get that first token, you're losing. The second thing you need to look at is throughput — once it's going and thinking through your input, how many tokens per second is it generating.</A>

▶ 03:18:50 - Brandon Hancock
For quick chat-related stuff, I think you would like Gemini 2.5 Flash or Gemini 3 Flash [tool:Gemini 3 Flash] on minimal thinking. So I would just literally go to Google AI Studio, get a Gemini key, and then just try out 2.5 Flash.

▶ 03:25:30 - Brandon Hancock
No cache, no cache — just straight up, make the API call to the database and do the three calls in parallel. Because if each request takes 0.3 seconds, if you do them all in parallel, the total time is 0.3 seconds. If you do them sequentially, it's 0.3 + 0.3 + 0.3 — almost a full second, which is just killing your time.

---

<!--SEGMENT
topic: Prompt Optimization, Recursive LLMs & Developer Workflow Tips
speakers: Scott Rippey, Brandon Hancock, Patrick Chouinard, Andrew Nanton
keywords: Claude Code prompt optimizer, JSON Python prompting, Context7, recursive language models, GPT-5, Phoenix Project, Unicorn Project, skills, scratch file workflow, Linux, command line, Ingest, trigger.dev, Steve Yegge, Gene Kim
summary: Scott shares a Claude Code Prompt Optimizer he built using JSON+Python structured prompting to get more consistent one-shot results, plus a Prompt Architect tool for clients. He also introduces the concept of recursive language models — a technique where a stripped-down model using recursive calls outperformed GPT-5 in benchmarks. Andrew reflects on the shift in AI capability in late 2024, recommends Ingest as a self-hosted alternative to trigger.dev for data-sensitive workloads, and advocates for giving LLMs less instruction and more autonomy. Patrick shares his scratch-file workflow for capturing and reusing prompts that eventually become skills.
-->

03:01:16 - Scott Rippey | @scottmichaelmedia
I got another $55K thing I proposed — I'm waiting to hear back on. It's like an estimator tool for a construction guy in Colorado. He should bite because literally his words were, if I don't have something like this by summer, I'm screwed. So the pain is there.

03:03:21 - Brandon Hancock
When building knowledge-based AI projects that have a workflow — meaning there's things going in, and it's your job to use AI to produce an artifact — that is the golden, golden goose right now for AI projects.

▶ 03:03:42 - Brandon Hancock
I would use Deepgram [tool:Deepgram] so that he can just talk through a job. The second thing I would add is a feedback button. What I would do with that feedback button on the AI responses is a quick way for him to say, this was bad, you missed this. Then you'll just track the conversation, you'll know the system prompt, you'll know his input, you'll see the output and what went wrong.

▶ 03:04:29 - Brandon Hancock
Frame it like this: this is going to grow the more you use it. Day one is the worst, and every day you use it, it's going to continue to get better. We're building in features to make it easy to submit information to help us continually make this prompt better.

03:08:00 - Scott Rippey | @scottmichaelmedia
I created a Claude Code Prompt Optimizer [tool:Claude Code Prompt Optimizer], because these tools are so good, right, and I just word-vomit. So I've got a really, really cool set of instructions with the JSON Python thing — you get really consistent results with that. And this is built upon some stuff I did some research on. I mean, if you look at this — I just put this much in here for a prompt and look at the refactor prompt — it's like literally constraints, verification. Context7 [tool:Context7] is something I really use, so I would really encourage people to do that.

03:10:49 - Scott Rippey | @scottmichaelmedia
People have been talking about recursive language models lately. And I found this article, and then I wrote up a kind of thing with Claude. There's some GitHub repos. This stuff is just cool. It's solving context issues, and I actually saw some data where a stripped-down model using this outperformed — I think the test was on GPT-5 [tool:GPT-5] — and it was like the nano model or whatever it was, using this, double outperformed the model using it alone.

▶ 03:12:22 - Brandon Hancock
At the end of the day, it's just adding more information to our queries. Our whole job is to solve the context problem. Scott is working on that with his Claude Code thing — he's making sure his input goes to a better-formatted context and then passed to the agent.

01:32:57 - Andrew Nanton
I mentioned Ingest [tool:Ingest] — I-N-N-G-E-S-T — as an alternative to trigger.dev [tool:trigger.dev]. Trigger.dev is a much more comprehensive solution, but if you have documents or data that you cannot let run on Trigger's workers — like you need to keep control of that information and need to run your own workers — then it is absolutely worth a look.

01:33:41 - Andrew Nanton
I've found more and more I am giving fewer instructions to the LLMs. I will tell it what I want to achieve, but then when it says, oh, do you want to squibble the gibbets? — before, I would sometimes not want to sound stupid. Now I'm just like, I have no idea what you're talking about. What would be the pros and cons of doing that? Help me understand why I would choose one versus the other.

▶ 01:34:11 - Andrew Nanton
Just continually embracing that humility of being like, look, I don't know — why don't you tell me what I probably want to do or what the pros and cons are? And we'll go from there.

01:37:00 - Patrick Chouinard
When you say I always think about creating agents and creating tools and creating automation — the way I'm using those tools today is when I develop whatever instruction I'm about to give to Claude Code, Cursor, or whatever, I never type it directly anymore. I always have a scratch file open where I type every instruction I'm going to copy and paste into whichever agent is going to do the job.

01:37:27 - Patrick Chouinard
The reason why I do that is that at some point at the end of a session, I realize, oh, I've copied and pasted this one like five times. It's time to make a skill out of it.

▶ 01:37:53 - Brandon Hancock
That's great advice. It forces you to look at what you're doing. You have a version of you who's looking over your shoulder — wait, Patrick, why are you saying the same 10 things religiously? Silly, just make a skill.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the raw transcript but were not present in the SPEAKER_ALIASES context block and have been passed through unchanged:

- **Hemal Shah** — participant, discussed Meta glasses and Gemini image generation
- **Morgan Cook** — participant, discussed WindSurf workflows, Lemon Squeezy, Dan Martell
- **Marc Juretus** — participant, discussed Claude Code personal dashboard and energy rate tracker
- **Elijah** — participant, asked questions about RAG, skills, and ShipKit security
- **Juan Torres** — participant, discussed ETL agentic system, AWS, DocPloy, and asked various questions
- **Prem** — participant, discussed Doclin app, Google Ads, and anti-gravity
- **Andrew Nanton** — participant, discussed Steve Yegge article, Ingest, Go language, and LLM prompting philosophy
- **Maksym Liamin** — participant, discussed automotive AI product (Nissan/Mazda/Infiniti), TinySeed questions
- **Alexander Alymov** — participant, discussed music bot project in Telegram with Suno AI and FL Studio integration
- **ivan** — participant, discussed Symposium — a censorship-resistant voice/video conferencing app for Russia/Iran
- **Bastian Venegas Arevalo** — participant, discussed agent with Perplexity/Exa tools and GLM 4.7
- **Ryan - One Stop Creative Agency** — participant, discussed Screenly digital signage app, brewery client, and HeyGen avatar project
- **Lan** — participant, asked about ShipKit repo selection and GitHub auth
- **Raghav** — participant, asked about ShipKit template applicability for non-standard projects
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** — participant, discussed prompt optimizer, recursive LLMs, and $55K construction estimator project
- **alexrojas** — participant, demoed music studio booking app with WhatsApp/Stripe integration
- **Ty Wells** — participant, discussed Engram project management dashboard and privacy concerns about Claude Cowork
- **Paul Miller** — participant, demoed Territory Compass app and shared RAG/PRD resources
- **Patrick Chouinard** — participant, discussed agent army architecture, skills, and ShipKit Mentor GPT
- **Bastian Venegas Arevalo** — (see above)
- **Maksym Liamin** — (see above; also responded to Brandon's questions about automotive SaaS expansion)