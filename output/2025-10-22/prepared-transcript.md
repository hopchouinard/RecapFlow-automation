=== SESSION ===
date: Not specified (estimated recent, based on tool references)
duration_estimate: ~2 hours (00:14:00 – 02:18:24)
main_themes: AI coding tools and cost comparison (Claude Code vs. Cursor), interactive presentation software demo, MCP servers and Playwright, agent-to-agent (A2A) protocol discussion, SaaS sales strategy, Next.js architecture decisions, background task queuing tools, prompt engineering for large-context video generation

---

<!--SEGMENT
topic: Pre-Call Banter and Introductions
speakers: Ty Wells, Manny, Mitch, Marc Juretus, Morgan Cook, Brandon Hancock
keywords: Omaha, Nebraska, Bahamas, Sidney Poitier, male pattern baldness, Atlas, OpenAI, ChatGPT, agent mode, Mac
summary: The session opens with informal small talk about hairlines, geographic backgrounds, and personal anecdotes. Brandon Hancock then pivots to announce two notable updates: the new Atlas browser agent from OpenAI and upcoming Claude Code improvements for ShipKit members.
-->

00:14:00 - Ty Wells
All right, Mitch.

00:14:45 - Manny
Good afternoon, can you hear me now?

00:14:47 - Manny
Yeah, I can.

00:14:48 - Ty Wells
I can hear you.

00:14:49 - Manny
I was talking on mute. Sorry.

00:15:23 - Mitch
There we go. I'm back.

00:15:29 - Ty Wells
I joined the club, man.

00:15:31 - Mitch
It's a baldness.

00:15:34 - Ty Wells
I've joined the club of baldness. No, that's a choice you've got there. That's a difference.

00:15:40 - Mitch
This is a reality.

00:15:45 - Ty Wells
Yeah, you and Marc — you cut yours. You shave that every day, don't you?

00:15:49 - Marc Juretus
Yeah, just about every day. It looks like me and him have the same MPB going on — male pattern baldness. It's funny.

00:15:57 - Mitch
My mother's Hungarian.

00:15:58 - Marc Juretus
I'm half Black and white. So my choice was my uncle on her side has all his hair but grayed at 29, or my dad with the male pattern baldness and no gray. Pick your poison.

00:16:21 - Ty Wells
If I don't cut this every day, I'm in trouble.

00:16:27 - Marc Juretus
Yeah, get some weird kind of missing-link look going on because the hair is growing weird.

00:17:04 - Mitch
And then you got Morgan. Morgan's like, oh, you guys talking about hair?

00:17:14 - Mitch
My problem is I have to go get it cut frequently.

00:17:17 - Morgan Cook
Otherwise it gets real bushy and out of control.

00:17:20 - Marc Juretus
Oh, those first-world problems you're talking about.

00:17:48 - Marc Juretus
You down in Bermuda, Ty, huh? Is that correct?

00:17:52 - Ty Wells
No, I was in the Bahamas. I'm back in Omaha now.

00:18:01 - Ty Wells
Well, I'm from the Bahamas, transplanted to Nebraska, but I claim Omaha as home. Been here about 30-some years.

00:18:13 - Ty Wells
Sidney Poitier — wasn't he from the Bahamas?

00:18:18 - Ty Wells
Yeah, I think he was an ambassador or something.

00:18:27 - Brandon Hancock
Hello, hello. All right. Guys, all the cool things have happened today and yesterday. First off, Atlas [tool:Atlas] — if you haven't got to try it yet, this thing is legit. Let me show it to you really fast. It's basically the new OpenAI [tool:OpenAI] browser, but you can turn on agent mode and have it do stuff. So you can say like, "Can you pause the current timer?" and it'll actually interface with your websites to do stuff. Obviously this is super simple right now, but you can actually have it go off and copy stuff from a Google Doc and break it down and put it over into a website. So all around, it's really, really freaking cool.

▶ If you already have the ChatGPT [tool:ChatGPT] subscription, it's definitely worth giving a try.

00:19:44 - Brandon Hancock
Well, you need a Mac first of all.

00:19:46 - Ty Wells
So I guess I'll be waiting.

00:19:50 - Brandon Hancock
I think it's the $20 and $200 plans. I think you just get way less on the $20. So definitely worth a shot if you haven't got to do that yet.

---

<!--SEGMENT
topic: ShipKit Claude Code Updates Announcement
speakers: Brandon Hancock, Mitch
keywords: ShipKit, Claude Code, Cursor, terminal renaming, cheat sheet, billing, Sonnet, Haiku, cost comparison, commands
summary: Brandon announces he is building a Claude Code cheat sheet and command set for ShipKit members, inspired by Mitch's terminal-renaming tip. He argues Claude Code is significantly cheaper than Cursor for heavy coders, especially on the $100/month plan, and previews upcoming training modules.
-->

00:20:10 - Brandon Hancock
One other cool update for you guys — for ShipKit [tool:ShipKit] — I've been going super deep today into making things way easier on Claude Code [tool:Claude Code] for you guys. So if you're using Claude Code with ShipKit, I'm adding Claude commands for everybody, adding all sorts of Claude shortcuts. Mitch, you actually inspired me on one of these. I'll show you really fast. So shout out to Mitch — Mitch had such a good idea the other day with renaming terminals. So I was like, why am I not doing that? Why am I playing hard mode? So doing things like this to say like "diff creator" — you can rename your different chats, you can open up new commands.

▶ Basically I'm working on a cheat sheet for you guys to let you copy my Claude Code setup. I'll hopefully start to record tomorrow or tonight, but that'll be coming out really soon to make Claude Code development way easier.

00:21:18 - Brandon Hancock
After doing the math breakdown for you guys, you actually save an insane amount of money using Claude Code compared to Cursor [tool:Cursor]. Obviously Cursor is easier, but for actual "let's make our dollars go as far as possible," Claude Code is winning right now. So I wanted to make it as easy as possible for you to use.

---

<!--SEGMENT
topic: Ty Wells Interactive Presentation Software Demo
speakers: Ty Wells, Brandon Hancock, Mitch, alroj, Prem
keywords: presentation software, QR code, real-time Q&A, engagement intelligence, screen sharing, Zoom app, Stack Overflow, Experts Exchange, interactive slides, audience polling
summary: Ty Wells demonstrates his custom-built interactive presentation platform, which replaces traditional slide decks with real-time polls, AI-powered Q&A, audience registration via QR code, and a live control panel. Brandon contextualizes the build as a weekend V1 and highlights its potential for Zoom integration.
-->

00:22:16 - Brandon Hancock
It looks like Ty is up first — Mr. Awesome AI Presentation Man.

00:22:27 - Ty Wells
Okay, what's going on, guys? So the presentation went well. The activities did not go so well — they couldn't see them, but that's been fixed. So this thing has taken an exponential leap forward since the presentation.

00:23:02 - Brandon Hancock
I'm so pumped. I've been looking forward to this all week, Ty.

00:23:09 - Ty Wells
This is the control screen, like I think you saw before, right? I've added some stuff here — an engagement intelligence system where basically if you're trying to collect information about your audience, they can opt in to see that information. The Q&A questions still come in real time over here. But I've added the ability to share screen.

00:23:52 - Brandon Hancock
And real quick, just in case anyone didn't get to see this last week — I basically helped him make his own presentation software. Instead of just having regular slides like slide one through slide ten, he's made it insanely interactive. Everything you're seeing right now — polls, AI questions — it's so cool. And he knocked out V1 in a weekend. So Ty's in absolute beast mode.

00:24:36 - Ty Wells
So going into a presentation, you would see this screen — you're waiting in the lobby. And from there, I can share a screen or I can do a slide. If you guys want, you can use your phone to scan this QR code to give you an idea of how this would work.

00:25:33 - Brandon Hancock
Dude, I'm all in, man. So I'm trying to make it work within the existing platforms.

00:25:45 - Ty Wells
Actually, I'm building an app for Zoom [tool:Zoom] so you can get the results right into Zoom. Got to submit that. So if you sign in, you basically register. You can put anything — I'm not checking anything. You don't have to put your real email. You'll be at the landing page at this point.

00:26:09 - Ty Wells
<Q>Do you see an ability to ask AI or Q&A?</Q>

00:26:14 - Brandon Hancock
I see "Try Agent Hub," and then I see a little AI logo.

00:26:28 - Ty Wells
<A>So that's a chat interface, and that's based on the presentation itself. So if you had questions, you can chat with it.</A>

00:28:22 - Brandon Hancock
I see "Ask an Expert." Is there something else I'm supposed to do?

00:28:27 - Ty Wells
Yeah, the expert one — you have an ability to chat. That goes to the expert. That's the other one, because I'm building something else on top of this — similar to Stack Overflow [tool:Stack Overflow] or Experts Exchange, where you get points based on if you respond with an answer.

00:29:23 - alroj
The expert works for me, but the Q&A — it's not active for me when I try to make a question. It doesn't allow me.

00:29:26 - Ty Wells
I'm not shocked. I didn't know I was first. It's like I'm mid-juggling.

00:29:37 - alroj
I find this is brilliant, man, you know?

00:29:50 - Brandon Hancock
One of the main things I've always wanted to do is launch a Zoom hot seat equivalent — just because right now, for example, what's the call order? Like, right now I have to post a screenshot. So I absolutely love what you're doing with presenting. But yeah, I've always wanted to make a hot seat version — who's next, ask questions, all sorts of stuff.

00:31:21 - Brandon Hancock
Well, Ty, seriously, you are absolutely crushing this. Every part of this is absolutely beautiful. I love the direction. I'm very excited for you to do more presentations. From last week to this week — it was beautiful last week, and now it got even cooler. Awesome, Ty, seriously.

---

<!--SEGMENT
topic: Best LLM for Coding Cost Comparison
speakers: Brandon Hancock, Mitch, Paul Miller
keywords: Claude Code, Cursor, Sonnet 4.5, Haiku, Codex, Zed, token usage, billing per runtime, $100 plan, $200 plan, agentic coding, Gosu Coder
summary: The group discusses which LLM and coding platform offers the best value for money. Brandon argues the Claude Code $100/month plan is the best deal for heavy coders, explains the per-runtime billing model, and compares verbosity between Claude and Codex. Mitch references Gosu Coder's benchmarks on agentic coding platforms.
-->

00:32:02 - Mitch
Yeah, so the latest and best LLM for coding — what are people using for dollar stretchers? I still think it's Claude Sonnet 4.5, but yeah.

00:32:26 - Brandon Hancock
Well, real fast, just to go into this — I was breaking down the math, and it looks like best bang for buck on top-tier models if you're coding like an absolute beast: it is the Claude Code [tool:Claude Code] $100 plan or $200 plan. The $200 plan costs you — I have an Excel sheet I can go find — but it is infinitely cheaper than everything else on the market. And you are tied to the Claude Code models, but that's the only one I really use at this point anyway. I will say, I've been coding pretty much nonstop. I'm not going over $100 right now, and I'm doing tasks in parallel — working on ShipKit, YouTube, startup stuff. So I'm doing like four things at once and I'm still not hitting my usage for my weekly period.

▶ The $100 plan, Claude Code, current — absolute best deal in my opinion.

00:33:33 - Brandon Hancock
I have not got to try Haiku [tool:Claude Haiku]. If anybody has, I'd be very curious to see your results with it. It's supposed to have the same capability as Claude Sonnet 4, but it's faster.

00:33:53 - Mitch
Yeah, I posted the results from Gosu Coder [tool:Gosu Coder]. He created his own tester. What I like about it is when he says "his tests," he actually has it change multiple files — it's more about agentic coding, like knowing what to do. He was saying in his tests that Zed [tool:Zed] is really famously known for doing way more than what you asked. So it will pass the tests, but it will also use like 2x the amount of tokens for the same task.

00:34:44 - Mitch
I've noticed Codex [tool:Codex] does not use as many tokens as Claude. Like Claude is just way more verbose. Whereas Codex is like, I am a robot — I will do exactly what you asked me to do.

00:35:06 - Brandon Hancock
The cool, interesting thing — if you are using Claude Code, regardless if you're doing Haiku or Sonnet, you get charged per runtime. It's not how many tokens — it's per runtime. So whether a task runs for 10 minutes in Claude Sonnet 4.5 or Haiku, you're still getting charged the same. Which means you should be able to get a lot more done with Haiku than Sonnet, because its output tokens and speed are way faster.

▶ The way they do billing and tracking your usage in Claude Code is per runtime, not per request — unlike everything else on the market.

---

<!--SEGMENT
topic: Personal Reflections, Career Pivots, and Mindset
speakers: Brandon Hancock, Mitch, Paul Miller
keywords: entrepreneurship, agency clients, Amazon brands, ShipKit launch, work-life balance, fun, career strategy, Vegas, Idaho, Australia, New Zealand, SaaS leads, competitor implosion
summary: Brandon reflects on his first year of full-time entrepreneurship — describing the emotional highs and lows — while Mitch shares his plan to shift from agency work to direct brand partnerships and relocate to Vegas for faster project execution. Paul Miller reports a major business opportunity in Australia following a competitor's collapse.
-->

00:35:58 - Mitch
Yeah, so I'm old now, by the way.

00:36:05 - Mitch
Yeah. 3-0.

00:36:12 - Brandon Hancock
I want to ask you any personal reflections because it's been a whole year since you left the whole Crew situation. You left your job to go to Crew and then from Crew to your own thing — you've done a lot in a year. Any reflections for yourself?

00:36:28 - Brandon Hancock
I really want to make a video on this to put out. I need to think on it more because I actually want to be very concise and value-add with it. But from an emotional standpoint, this is the most highs and most lows all in a year — from "Oh my God, I had this great idea, I'm just going to quit my job and go all in, this is fantastic" to three days after: "Holy shit, what have I done? I don't have a paycheck coming in" — to "I launched something, I'm making money" — to "Oh my God, I don't have anything else in the pipeline, I'm back to broke." So it's just a constant high, low, high, low. I told my wife, I was like, why did I choose violence for myself? I'm absolutely loving it. I'm very excited where I am now, but it has taken what I thought would take two months — it has taken basically eight or nine months. So kind of off, but still on track.

00:37:43 - Mitch
For me, I've kind of realized I just need to have more fun with things. I've been so focused on the outcome where I'm now reversing — actually, how can I have more fun with this task? And that's kind of been the overall thing. What's been draining that fun? So I'm really assessing the career aspect — sending in some applications for working directly with Amazon brands instead of being an agency, because on the agency front, working with agency clients just really drains you. So I've really felt drained of the fun. Looking at finding other companies to work directly with — not being on so many client calls — and just reverse engineering where I've done the best work and made the most money, which is when it's been pretty fun. So really looking at how can I change what I'm doing and just make it more enjoyable.

00:40:05 - Mitch
I'll update the journey — I've made some harder pivots to get this project done faster. I'll be leaving Idaho. I just decided today, Thursday — I'll be going to Vegas so I can work with Debris directly on the projects just so I can get it done way faster. What's happening right now is not the speed that I want. So definitely making some more advantageous decisions to get it done faster.

00:41:40 - Paul Miller
I'm over in Australia at the moment. As I think I'd mentioned a few months ago, suddenly our biggest competitor has imploded. And I've got all these leads and opportunities from my software company over here. For those that don't really know the demographics — Australia has a population of about 27 million people, New Zealand has 5 million. So proportionately the market is five times as big for my company. And now we're getting word of mouth within an industry vertical. I just get random calls. These are above $10,000 a month SaaS income.

00:43:29 - Paul Miller
The bill's gone up to $1,200, and I kind of thought, oh my God, I've kind of lost it a bit. But yeah, when you said at the start of the call that Claude Code — because I was thinking, can I do some of the next updates in Claude Code? That sounds like it's the way to go.

00:43:47 - Brandon Hancock
Yeah, 100%. It's almost four times cheaper, depending on which plan you buy. So your bill would have been maybe $300–$400 versus $1,200, which is crazy, the difference.

00:44:17 - Paul Miller
<Q>So when you say plan — I've got the Claude $200 a month plan, the normal chat plan. Is that the same package?</Q>

00:44:22 - Brandon Hancock
<A>Yeah, if you have Claude Max — you already have it. The kicker is just in Claude Code, you sign in and choose: do you want to use the API, or do you want to use your plan? And obviously you want to use your plan to take advantage of those built-in credits.</A>

▶ If you already have the Claude $200/month Max plan, you already have access to Claude Code — just sign in and select "use your plan" instead of the API.

---

<!--SEGMENT
topic: MCP Servers, Playwright, and Developer Tooling
speakers: Marc Juretus, Brandon Hancock, Mitch
keywords: MCP servers, Playwright, Docker Desktop, GitHub, web scraping, Cursor, IntelliJ, GitHub Copilot, VS Code, Asana, Linear, Supabase, Notion, browser automation, screenshot
summary: Marc Juretus asks about the practical benefit of running Playwright as an MCP server versus having the IDE generate scraping code directly. Brandon explains that pre-built MCP tool sets reduce context overhead and error surface for agents. The group also discusses which MCP servers are most useful in practice.
-->

00:49:32 - Marc Juretus
I'm trying to prep for teaching people at work how to use GitHub Copilot [tool:GitHub Copilot] with the IDE, which unfortunately we use IntelliJ [tool:IntelliJ] / JetBrains instead of VS Code [tool:VS Code]. I was playing around with the Copilot instructions — it was really cool where I could go in and if I was creating JavaScript functions, I could have different headers on top of it. Then I was doing builds with project requirements where I would blow away all the code, let it build it. I'm assuming when I do the demo, I'm going to have somebody pull down the repo, execute the project requirements, and show how you can have a functioning app within less than a couple minutes.

00:50:13 - Marc Juretus
And then the other thing I was playing with was MCP servers [tool:MCP servers] off of GitHub. I was playing around with Playwright [tool:Playwright]. Now, obviously, you know my fantasy football tracker — I pull in all my stats using Playwright, using Python code inside my code. But I was like, let me try to get an MCP server. I was able to install it and call it, but it would always bail out. What worked was running the Playwright MCP container on my Docker Desktop [tool:Docker Desktop]. So my question is: what is the benefit of using Playwright as an MCP server, as opposed to just having the IDE write that code?

00:52:00 - Brandon Hancock
One quick side note — if you are using Cursor out the gate, now what's insane is you get Playwright out the box. It's an auto-suggested feature, which is phenomenal for debugging. So you can always say like, "Hey, go look at localhost/chat. Something's off with the UI. Can you take a quick screenshot, tell me what you see, and fix the colors?" That's how I'm using Playwright right now.

00:53:17 - Brandon Hancock
<A>So the main benefit of a pre-built MCP that wraps the most common actions you would want to run with Playwright — for example, you're automatically getting access to 21 tools for the most common actions you would want to take. The agent can look at the tool call description to see: I have access to 21 different potential options for interacting with the browser, everything from clicking to dragging. Whereas the other option — on-command code generation — the agent has to understand the problem, then understand the code to write, then execute the code, hope it didn't make a mistake, hope your environment is already set up perfectly to run Playwright, potentially debug it if something goes wrong. Whereas with an MCP that's already set up to work perfectly, it just treats it as a black box.</A>

▶ Using a pre-built Playwright MCP server is more context-efficient and less error-prone than having an agent dynamically generate scraping code from scratch.

00:55:20 - Brandon Hancock
Can I tell you exactly what I did the other day? I'm helping out a client on a project. I was like, man, their website is so much better. Hey, Playwright, go take screenshots of the entire landing page — every section — and now what I want you to do is take those 12 screenshots, help me reformat what I'm trying to do, make it my style, my content, and redo it for me. So I ended up with 12 tasks: here's what I need to do for the hero section, the about section, the feature section, the how-to section. That's how I just used Playwright to speed up taking 12 screenshots.

00:57:40 - Brandon Hancock
I'm more and more falling in love with different MCP servers. There's like three to five that are very helpful. The rest of them I just haven't really got a chance to use. Very few tools actually have an MCP server. Google doesn't have an MCP server — you always have to go to a third party.

00:57:40 - Mitch
Asana [tool:Asana] — I recommend. So it's a task management platform. Each client has their own project. You can have Asana say, "This project is with this client. Please give them the update of what we completed this week, the previous week, and the things that are in progress, their different priorities, our comments underneath those tasks, and here's the account performance as well. Please draft out the email using this template." And then it just does it. I was like, wow, that was like a whole hour saved.

▶ Recommended MCP servers in active use by the group: Playwright, Asana, Linear [tool:Linear], Supabase [tool:Supabase], and Notion [tool:Notion].

---

<!--SEGMENT
topic: Background Task Queuing — Moshe.dev vs. Trigger.dev
speakers: Morgan Cook, Brandon Hancock
keywords: Moshe.dev, Trigger.dev, Next.js, background jobs, streaming updates, task observability, NaN instance, parallel jobs, Whisper, transcription, agentic workflows
summary: Morgan Cook introduces Moshe.dev as a lightweight background task API with streaming updates and observability. Brandon recommends Trigger.dev as a more feature-rich and AI-friendly alternative, and previews upcoming ShipKit projects that will demonstrate Trigger.dev for agentic workflows including a transcription service.
-->

01:00:09 - Morgan Cook
Has anybody used Moshe.dev [tool:Moshe.dev]?

01:00:16 - Brandon Hancock
How do you spell it?

01:00:16 - Morgan Cook
M-O-T-I-A dot D-E-V. [link:motia.dev] It's a pretty cool, lightweight, NaN kind of front task API entry point with streaming updates. Our Next.js [tool:Next.js] and everything is pretty good at the request-response cycle, but anything that's a long process, you want to hand off. This is an excellent way to hand it off. They have a specific type of task pattern. They have observability into the entire thing through a web page, so you can go look at all of your tasks that ran.

01:01:12 - Brandon Hancock
Real fast, Morgan — before pulling too deep into one — I just want to mention, I think we briefly talked about Trigger.dev [tool:Trigger.dev]. I really, really would recommend Trigger.dev because it seems like it's that, but on steroids. Everything you're describing with tracking and watching in real time, multiple task management, doing everything from series, parallel, loops, routing — it has all of this. Each one of these is going to trigger a different task that's going to get kicked off in the background. So just as another option with probably more support — 12.6K stars.

01:02:38 - Brandon Hancock
I'm actively working on a project that will be the base — it'll be a transcription service, like we'll use Whisper [tool:Whisper] as a transcription service, while parallel back we'll have parallel jobs. And then immediately after that, I will show you guys how to convert the base template to do some — I think we'll have two or three extra projects — to showcase agent workflows using Trigger.dev. So I'll have plenty of examples with Trigger.dev for you guys.

▶ For long-running background tasks in Next.js, Trigger.dev is recommended over building custom API routes — it provides built-in observability, parallel job management, and is more AI-friendly than alternatives.

01:03:06 - Morgan Cook
Good to know. I'll review them both and see where I feel like I need to go with the project I have for it. I appreciate that info on Trigger because that's what I was looking for — what else is out there? Because I didn't want to have to load up a whole NaN instance to have that backend doing all that work. I wanted something a little bit more coder-friendly that's not visible to the end user.

---

<!--SEGMENT
topic: Patrick's AI Platform Launch and Chat UX Redesign Concept
speakers: Patrick Chouinard, Brandon Hancock, alroj
keywords: AI platform aggregation, HR agent, provisioning agent, document generation, prompt library, custom GPT, ShipKit Mentor, two-panel interface, VS Code, nano model, autocomplete, CI/CD, Claude Code parallel tasks, SDLC
summary: Patrick describes an enterprise AI platform going live in one week that aggregates 12+ internal AI tools built over 18 months. He also shares a concept for reimagining the AI chat UX with a two-panel composer interface featuring nano-model autocomplete. Brandon highlights Claude Code parallel tasks as a documentation accelerator.
-->

01:04:18 - Patrick Chouinard
So this week, I can't say that I've really created anything new. We are about a week away from going live because at my client, we're building basically a new AI platform — in the sense that they decided to create a platform to aggregate every single AI tool they've built. For the past year and a half, they've built a bunch of AI tools that do a bunch of things, but they were hard to find and people were always context switching. So we basically built a platform to aggregate everything together, and it's going live in about a week. I have to build all of the training material and the documentation and everything.

01:05:00 - Patrick Chouinard
Right now I think we're at 12 tools, and still counting. The platform itself is actually a foundation, so there will be other tools spawning from it. It's also a host for all of the custom agents — like the HR agent, the provisioning agent asking about contracts and things like that, or asking about your vacation. There's also a document generation tool, a briefing tool, a financial tool — everything gets put in there. A whole prompt library functionality. So yeah, a whole lot of things to document and train people on, and we're on the last mile.

01:05:52 - Patrick Chouinard
But I was able to use my own GPT — ShipKit Mentor [tool:ShipKit Mentor] — while driving, to start working at least conceptually on a project I would like to spend some time on if I ever get that free time back. Basically, I'm rethinking the AI chat UX, because I've been hating the chat UX where you have that tiny little box. I always create huge prompts that never fit in there. So I hate the fact that I need to create the prompt somewhere, copy and paste it into the tool in order to use it. It doesn't make sense.

01:06:36 - Patrick Chouinard
So what I've started to design with the custom GPT is a two-panel interface. Basically, the left side is your composer — I leverage the same mechanic that you have in VS Code [tool:VS Code]. So basically, having a very small nano model, actually, looking every time you stop typing, sending what you've typed so far, and suggesting autocomplete. Basically what you would have in a VS Code or Cursor [tool:Cursor] environment, but for text composition. And the right side being your response from the larger model. The least amount of buttons possible, the least amount of toolbar possible — just discussion which is autocomplete-friendly, and the results on the other side. And the other side would also include all types of export formats.

01:07:48 - Brandon Hancock
That's awesome. It is wild — now that you've said that out loud — it is wild to me that ChatGPT, Claude, all of these online editors don't have that. Like, I can do it in code. Why can't I do it online? Awesome idea. I absolutely love that. Very cool workaround on the nano model for speed.

01:08:17 - Patrick Chouinard
It's just autocomplete. So it doesn't need to be really intelligent — it's just "take a look at what I wrote so far and propose to me in a grayed-out fashion what I would need." Exactly the way — and yeah, Alex is right — it's exactly what I've started to imagine: leveraging the base of VS Code because it's open source now, but just strip all of the development functionality from it and just keep it as a text editor.

01:09:18 - Brandon Hancock
What's so cool about what you're doing at work right now is every big company is tackling this. We all are building things in silos. There's an insane amount of value in: how do we make sure people have access to tools built by other organizations? How do they even know what exists? How can they contribute themselves? These are all questions big organizations are having to answer right now.

01:10:50 - Brandon Hancock
Dude, really cool thing I just want to recommend — I have not given it enough of a chance — Claude Code Parallel Tasks [tool:Claude Code]. I just updated six projects completely. I spun off six separate projects that did an insane amount of work in each project, and it took a minute, whereas normally it would have taken six minutes or longer. I said: here's what we're trying to do, I did it for one project, and I was like, great — now that you understand what I want, spin off seven parallel tasks and go do it. So in your case, with the right step structure, you could easily start to use Claude Code to do parallel tasks to kick off and literally document the entire process.

▶ Claude Code parallel tasks can dramatically accelerate documentation of multiple codebases — define the approach for one, then spin off parallel tasks for the rest.

---

<!--SEGMENT
topic: SaaS Sales Strategy and Customer Acquisition
speakers: Brandon Hancock, Prem, Jake Maymar, alroj, Paul Miller
keywords: SaaS sales, customer acquisition, lateral market, upstream distribution, awareness funnel, Software as a Science, Dan Martell, server actions, API vs server actions, Next.js, Zod validation, contract negotiation, Claude AI dad prompt
summary: Prem asks for tips on scaling a SaaS application's customer base. Brandon outlines a two-level strategy: lateral (finding similar buyers) and upstream (finding distributors who serve many of your target customers). The group also discusses Next.js server actions vs. API routes, and Jake shares a lesson on getting contracts signed early, with Brandon recommending a creative AI prompt for contract analysis.
-->

01:17:43 - Prem
From an architecture perspective, I just had one question. You were suggesting to use server actions for most of the server side. Was there a reason — instead of using APIs which can be exposed in the future — you call out APIs purely for webhooks, but pretty much everything else use server actions. Is there anything while you choose server actions or APIs?

01:19:05 - Brandon Hancock
<A>So from a few main things — I like to structure APIs always for external, so external services or things that I want to then later make external, because I just don't want there to ever be a weird edge case to accidentally put something in the wrong spot. Two, when using server actions, you're getting better type safety because you know what the function is going to return. The function tells you: I'm going to accept these parameters and I'm going to return this object type. Whereas if you're using an API endpoint, you have to do JSON, you have to do Zod [tool:Zod] validation on multiple fronts — on the passing it in, then input validation, then authentication, then authorization, then handle three or four different error codes. There's so many extra layers the second you let it actually leave from front end to an API endpoint and come back. All I'm trying to do is just create a new object — why add in all that extra abstraction?</A>

▶ Use Next.js server actions for internal operations (better type safety, less boilerplate); reserve API routes for external-facing services and webhooks.

01:20:41 - Prem
The last question I have is — as I'm building this SaaS, I have a few clients I know I'm building it for. But I'm relatively new in terms of marketing. Is there any tips on how to scale your SaaS applications? Any thoughts?

01:21:50 - Brandon Hancock
<A>So the way I like to think about it — two approaches. Approach one is lateral, where I'm basically just looking for: let me describe who this person is. They're in this position, they're in this job, they have this problem. Is there an adjacent market? Is there another person in the same company? I'm still on the same playing field, just looking for that person in different roles that could buy it. That's level one. Level two is upstream — who is the person that serves 500 other clients? Because if I can find that person, I have direct distribution to those people. So you can go up and find the person who's connecting to all of your desired customers, or you're searching on the same plane. What really happens in real life, most of the time, is you first find two to three people manually that are on the same playing field — copies of your existing clients. Then you notice the pattern and know to look up. The second you look up, you now have access to distribution to almost unlimited extra clients.</A>

▶ SaaS customer acquisition strategy: first find 2–3 lateral customers manually, detect the pattern, then go upstream to find distributors or aggregators who already serve your target market.

01:13:00 - Jake Maymar
Yeah, I'm in contract land. I learned a really powerful lesson. I was doing the show-up with the mock-up, mock data, mock things that are all running — basically proving the concept completely. Client got really excited. We started rolling forward. We got funding. I got to the point where they're actually going to send the first initial payment, and they're like, "Oh, we don't have a contract yet."

01:14:55 - Brandon Hancock
Real fast — something I did recently because I had to do a contract. My favorite new thing is: I basically tell the prompt, "You are my dad, I'm your son, and you are an expert at software and contracts. You've done many things in the past, and now you're helping me understand and explaining things simply, giving me your recommendation and what's fair and unfair." And it's like, "Hey son, I'm so happy and proud of you for landing this contract." I promise you, it was the best way for me to analyze the contract.

▶ For contract analysis, prompt Claude as "you are my dad, I'm your son, you are an expert at software contracts — explain simply, tell me what's fair and unfair, and give an example of each clause going right and going wrong."

---

<!--SEGMENT
topic: Vibe Coding, SDLC Discipline, and New Member Welcome
speakers: Garron Selliken, Brandon Hancock, Patrick Chouinard, Mitch, Ty Wells
keywords: vibe coding, Cursor, ADK, GitHub, version control, SDLC, save points, real estate coaching, E-Myth, ShipKit, Codespace, context management, Claude Code revert, Singularity is Near
summary: New member Garron Selliken, a 27-year real estate veteran and sales coach, shares how adopting Brandon's workflow and Cursor transformed his progress after six months of struggle. Patrick and Ty add advice on SDLC discipline and reading AI output carefully. Brandon connects Garron's coaching expertise to the ShipKit model of codifying expert knowledge into prompt templates.
-->

01:26:01 - Garron Selliken
This is my first time joining you guys. I just discovered you, Brandon, about a week ago on YouTube. And you basically saved my enthusiasm for actually continuing to do this because I'm not a coder. I'm not a programmer. But I actually built a really large software application in real estate with a friend of mine. I designed it all and he was my lead developer. We ended up getting some investment and built out this huge MLS backend interactive property search. So I have experience on what are the use cases, what should it feel like, how do you do it — but then how do you actually make it? I have some experience, like I can listen and be like, kind of like a foreign language — I kind of get it, but I certainly can't speak it.

01:27:00 - Garron Selliken
I've been basically vibe coding now for about six months, and I just could not get past certain places until I saw your video and I adopted all your workflow — the five things, whatever those are, I think you had three videos — took all your templates, trained the agent that I've been using to help me be a coding assistant, and then implemented Cursor [tool:Cursor]. And I got more done in the last day and a half than the last month.

01:27:34 - Brandon Hancock
Oh, that makes me so happy, man. And it actually worked.

01:27:38 - Garron Selliken
I was like, in fact, I watched Cursor run through the nightmare of a week's troubleshooting when it decided it was going to do Python best practices instead of sticking to the ADK [tool:ADK] as a single source of truth. And I just watched it go into the weeds and mess everything up. And then we built some rules, ran it again, and it worked.

01:28:08 - Garron Selliken
I've been a real estate trainer for 27 years, and a sales trainer for about 20 of those. I coach a bunch of agents with a coaching program that I developed. So what I'm building is basically something to support my coaching clients with the framework that I coach on. They really need help on conversations, and then I'm going to attempt to build some agents that will actually be able to have a substantive real estate conversation with someone in the public as well, down the road.

01:30:08 - Brandon Hancock
So a few just high-level ideas to throw your way. What's really cool — you and I have a ton of parallels on what we're doing. I obviously have a ton of experience in software. You have a ton of experience in real estate and coaching. So what I did with ShipKit [tool:ShipKit], and what I recommend you do for your stuff too, is I try to basically codify the entire journey that a software developer goes on — from an idea to a full-blown app. You break it down into a bunch of very small steps, and then for each step, you create small prompts that have your 20 years of experience on how to achieve that desired result. The second you have the first two or three of those prompts created, when you start to work on prompt template number five or six, you can basically say: "Hey, go look at the previous style. Now here's the new step." And you'll speed through it. You're basically getting people access to 20 years of experience.

▶ The ShipKit model — codifying expert knowledge into structured prompt templates — can be applied to any domain, not just software development.

01:31:36 - Brandon Hancock
The book E-Myth [tool:E-Myth] — that's where I got inspiration for ShipKit, where you standardize the process for running a business. But I was like, well, I'm going to standardize the process for creating software. You could standardize the process for coaching real estate, selling, whatever you're doing specifically.

01:36:00 - Patrick Chouinard
That's where a proper SDLC and actual commits into a GitHub repo [tool:GitHub] can save you. And that's — I think this is where the introduction of a lot of vibe coders or people that come from outside of software engineering into software engineering — they gain the capability of creating working software, and that's absolutely awesome. But the ability to have save points they can return to — if something like ShipKit or any AI tool can guide them and hold their hands into the SDLC itself, so they have save points they can return to — I think this is the next step that we need to do.

00:37:46 - Ty Wells
You can revert in Claude Code — conversation or code. But as for coming from the outside in with no software engineering experience, the best thing you can do is read what it's telling you to do. Don't let it run wild, because it'll say something it's about to do, and you may skim through it, and then you say "yeah, go ahead" — and it's completely not what you wanted. So read what they're saying. Does it make sense to you? Is it what you want? That helps a lot.

▶ For non-developers using AI coding tools: always read the agent's proposed plan before approving — skimming and approving blindly is the most common cause of runaway changes.

---

<!--SEGMENT
topic: Agent-to-Agent Protocol, AI Framework Landscape, and Content Strategy
speakers: alroj, Brandon Hancock, Mitch, Jake Maymar
keywords: A2A protocol, Google A2A, agent-to-agent, AgentKit, LangChain, Crew AI, LangGraph, OpenAI, network effects, Google Trends, ADK, content creation strategy, quantum computing, AGI, MCP, version 1.0
summary: The group debates which agent communication protocol and framework will dominate — Google's A2A protocol vs. MCP vs. others. Brandon analyzes Google Trends data live to assess A2A adoption, explains the network effects required for A2A to succeed, and advises on content strategy around emerging protocols. Jake and Mitch discuss what it takes for a framework to be taken seriously (build, deploy, evaluate pipeline).
-->

01:54:28 - alroj
Just in that topic — I think that whenever we connect quantum computing with LLMs, that's where it goes to a thousand IQ.

01:54:42 - Brandon Hancock
Yeah. Ultra genius. AGI. All of it.

01:54:51 - alroj
So I just had a question actually regarding these. I've been brainstorming a lot. The agent-to-agent communication and the protocols that are coming — I've seen a couple of podcasts and it seems that even commerce in the future is going to be agent-to-agent. Like agents are going to represent the buyer, the seller, they will negotiate, they execute the purchase. So what are the protocols that they're actually talking to each other? I know there's agent-to-agent by Google, or the MCP [tool:MCP]. <Q>Which one do you think is going to be the key protocol?</Q>

01:55:37 - Brandon Hancock
<A>The actual A2A protocol [tool:A2A protocol] by Google is the one that everyone's referring to on all of this. Let me look this up real fast. Okay, no, they haven't hit version one yet. I mean, this is the repository. They are adding extra features all the time — encryption, purchasing — they're doing so much in here.</A>

01:56:26 - Brandon Hancock
Speaking of being an expert on a subject, Alex — you were doing some YouTube videos there for a second. Like, literally just going deep into A2A land — there's 30 things you can do with A2A. I'm just going to break it down in one video and cover a small section of it. And just by going on a deep dive into A2A, you really could become an expert on it. I know if you go to their presentation from one of Google's IO events, everyone who's adopting A2A — it's up and to the right. So if I'm ever trying to become a specialist on something, I don't want flat — I want exponential growth and adoption, and I want the people who are adopting it to be making a lot of money and have a lot of money to spend. A2A fits a lot of those buckets.

01:57:44 - Brandon Hancock
So that's flatlining a little bit. That is a little bit concerning. So here's the thing — if you were to go all in on A2A, you have to take a bet. The bet right now is Google is going to get their act together and make adoption easier. Because right now, you have to assume all agent frameworks are going to go all in on A2A. And I think they are. The kicker is you kind of need that first domino to say "we accept A2A." Because it's literally network effects — if only one business uses A2A, the value of that network is one. But when three companies use A2A, now it's six. It grows factorial. So I think that's just the issue with A2A right now — it needs some bigger adoption by bigger companies before it becomes fully valuable.

▶ A2A protocol adoption follows network effects — value grows factorially with each major framework that adopts it; the catalyst to watch for is version 1.0 and adoption by a major agent framework like AgentKit or LangGraph.

01:59:24 - Mitch
Yeah, what would you compare that search volume with — like Crew.ai versus LangChain? Like what would that look like?

02:00:02 - Mitch
So when I was making a lot of the ADK [tool:ADK] videos, I was here. So you either need to be an early adopter or wait for a big catalyst. A big catalyst is version 1.0 of A2A and going all in. So like, if you're talking strategy with content creation, I usually write when a project comes out from a big player or when a major release comes out. So like LangChain [tool:LangChain] 2.0, LangChain 3.0 — those are the times to go all in on the platforms because everyone has the same question: "How do I use this thing?" So right now, if you wanted to play the long game, you could start on A2A today and just know: the second 1.0 comes out, I'm going to go deep on it again.

02:02:24 - Jake Maymar
Going back to AgentKit [tool:AgentKit] versus Agent Development Kit — one thing I mentioned in one of the latest videos was: I've never used a tool so easy to deploy before than AgentKit. That was the fastest I've ever made an agent. It's hard to do complex workflows in AgentKit, but the fact that I could literally press deploy and it just did it — that's wild. So you have to have the entire build, deploy, and evaluate funnel to work for you to be taken seriously. And LangGraph [tool:LangGraph] has that right now. LangChain has it. I think Crew AI [tool:Crew AI] has that. The prices are very high. From last time I saw, Agent Development Kit [tool:ADK] — very cheap, very affordable. Deployment's very difficult. And evaluation is very hard right now on ADK.

02:03:22 - Jake Maymar
The thought I was watching — Bitcoin and how they were creating these agents that were basically doing companies, completely autonomous. And the A2A — if you're able to basically barter or trade resources back and forth, agents can trade basically money back and forth. So that's going to cause — I think that's a catalyst. And I think A2A literally, as of like a month or so ago, started to build in transaction capabilities, I think, from my understanding.

02:04:44 - Brandon Hancock
And final thing — one quick trap to avoid. There is a world where there are 200–300 people that are building out A2A and adding it to all the major agent players, and we never know it exists. It's like HTTP. How many of us are HTTP experts nowadays? It's a protocol — you just know you send stuff to an endpoint and you get stuff back, but you're not developing the protocol. So unless you're one of those 200–300 experts that helped build it out and implement it at all the big players, it's kind of a winner-take-all, at least for protocols. A thousand companies might implement it, and then after that, who's doing it?

---

<!--SEGMENT
topic: Large-Context Prompt Engineering for Video Generation
speakers: Mitch, Brandon Hancock, Morgan Cook
keywords: prompt engineering, master prompt, context window, video generation, VO3, agent pipeline, sliding window, JSON output, fine-tuning, Manus, Claude Code, content creation, Dharman, scene generation
summary: Mitch shares a counterintuitive prompt engineering finding: for AI video generation pipelines, giving each agent the full 50–60 page master prompt with only the task changed produces better outputs than trying to decompose and specialize each agent's context. The group discusses context compression strategies, sliding window approaches, and why JSON output formatting can suppress creativity.
-->

02:05:53 - Mitch
So with prompt engineering — this is going to sound so simple, but basically we create a really long master prompt, and what we try to do is break it down into different agents. And what we realize is, actually, the best outcomes we were getting is basically just taking the whole master prompt, but we change the tasks. So every agent kind of gets the same overall prompt, but they just have different tasks. So the first one is to create the idea, the second one is to ensure that the ideas are congruent — but they all have the giant 70-page master prompt. Basically, you have the same giant prompt, and each of them really understands how to do their tasks well. And so all you're really doing is just delegating the specific ask that they're doing, not necessarily taking down the context engineering.

▶ For complex, continuous creative pipelines (e.g., AI video generation), giving each agent the full master prompt with only the task changed outperforms trying to decompose and specialize each agent's context window.

02:06:59 - Mitch
With content creation, that's been the prompt engineering hack of all time — screw trying to break this stuff up. Just give them separate tasks and give them the same giant master prompt. That's been the main winner.

02:07:17 - Brandon Hancock
Would you want a concrete example of that? I think I'm understanding. Sure. So basically, we give them an idea and then they have to create a series of clips that we would then feed to VO3 [tool:VO3] to actually make those clips. So the first thing is: first we have the idea, but now they need to create the concrete beginning, middle, and end. And then once they create that, then they create the key characters, create the key scenes, create key environments. Then they make the scenes and the clips, and then you evaluate: did I give every clip what was needed? Now, obviously not all agents need the whole master context. But for most of the first four agents, we give them the whole thing, and it's actually way better outputs than trying to figure out how to optimize the prompt for each one.

02:08:41 - Brandon Hancock
I'm going to say it back to you. Instead of siloing everything and trying to make an agent an absolute expert on that one task, you're saying what has worked best is: the agent is still a specialist, however the last 10–20% of the prompt is the specialty. The other 80% was still the original master high-level context.

02:09:15 - Mitch
Yeah. This one is like 50 pages. Close to 60 pages.

02:09:22 - Brandon Hancock
I don't think I've ever seen a 50-page prompt. This thing's probably a beast.

02:09:26 - Mitch
It's a beast. So it's just like, okay, great — can we try to break this up? And the answer is no. You cannot break this up. Each of these is in there for a solid reason. And they all have very critical rules. And it's still not outputting it the way — the only thing we haven't tried is fine-tuning a model, which I don't think the juice is worth the squeeze.

02:11:18 - Brandon Hancock
Cool. Final thing, Mitch — I think at least in engineering, electronic warfare background, there's a concept called sliding window. So you basically take a window and you slide it through. So you have a 50-page prompt. I would be very curious if you took the sliding window approach — pass the whole thing in, but then do a combination of two things: a sliding window, meaning you're now tackling page one and two, that is what the window is looking at, and then maybe accompanying the sliding window with some additional instructions.

02:12:00 - Mitch
It's tough. I've tried a lot of different things. It's just so tough because they all feed into each other, and if they don't understand page one and two equally to how they understand page 58 and 57, they just make slop. Because it's really like, I'm asking an AI to go against all of its training and make a video of some dude throwing a coffee at a homeless guy. It's not easy to do.

02:15:07 - Mitch
Real fast, Mitch — if you get a chance, if you could try out Manus [tool:Manus] with this problem. The exact process of adding stuff, referencing it — Manus specializes in decomposing tasks, storing the results of tasks. I would be very curious if you passed in that prompt and had it try to do something for you.

02:16:49 - Brandon Hancock
I'm going to give you one final thing I would like to try to solve this. Claude Code had a brand new thing — Skills — which allows you to basically say: when you're solving this problem, use this approach. So you almost get to build like an N8N [tool:N8N] style workflow. I would be very curious to start if you could actually just use Claude Code [tool:Claude Code] inside a file explorer to basically say: here's the master prompt, here's the idea, now save artifact one, save artifact two — and just see if you can crack the code manually first once. Because that's the hardest problem. The second you figure out and crack the code once manually, then you can systematize it. The hard part now is we're trying to jump to an automated system when we haven't proved it working yet manually.

▶ Before automating a complex multi-agent pipeline, prove the full workflow works manually in Claude Code — save each artifact step by step — then systematize once the manual process is validated.

02:18:17 - Brandon Hancock
All right, guys. Well, hey, we just hit eight. But yeah, seriously, glad to see all the awesome projects. You guys are absolutely crushing. Please keep me posted if there's anything else that comes up that I can help with.

---

=== UNRESOLVED SPEAKERS ===
- Manny (appears only in the opening minutes; not in the alias map)
- alroj (appears multiple times; name appears to be a username or handle, not resolved to a full name)
- Elijah (appears briefly around 00:46:57; not in the alias map)
- Garron Selliken (appears around 01:26:01; not in the alias map — passed through unchanged)
- Prem (appears around 01:17:43; not in the alias map — passed through unchanged)