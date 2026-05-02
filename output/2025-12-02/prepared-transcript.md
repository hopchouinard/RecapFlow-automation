=== SESSION ===
date: Unknown (Monday, likely late November 2024 based on Black Friday/Cyber Monday references)
duration_estimate: ~2 hours 10 minutes (00:06:03 – 02:14:50)
main_themes: AI development tooling and workflows, spec-driven development, Claude Code usage patterns, ShipKit extensions, new member introductions, enterprise AI deployment considerations, productized AI services, real estate data analysis with AI

---

<!--SEGMENT
topic: Pre-call Chatter and Project Previews
speakers: Ty Wells, Patrick Chouinard
keywords: Gemini CLI, Claude Code, SpecStory, VS Code extension, Cursor, search agent, HTML dashboard, Supabase, spec-driven development, ShipKit
summary: Ty and Patrick catch up before the formal call begins, sharing what they are building. Patrick describes a bottom-up approach to a Gemini CLI-powered daily search and HTML dashboard pipeline, and introduces the SpecStory VS Code/Cursor extension that saves AI chat logs to markdown for rule extraction. This segment establishes the session's core technical themes.
-->

00:07:38 - Ty Wells
<Q>So what magic are you conjuring up this week?</Q>

00:07:43 - Patrick Chouinard
<A>Actually, I pretty much started building an application, but instead of building it from the top down, I'm beginning from the ground up. I realized I wanted something to do a daily search on a bunch of subjects. Then it said... A bunch of webpages out of those search results using Gemini CLI [tool:Gemini CLI] as the search engine and the HTML creation engine at the same time.</A>

00:08:14 - Patrick Chouinard
Problem is, there doesn't seem to be any examples of that in the models. So every time I try to have a model create that application, I'm running in circles because it doesn't have any reference material. So basically, I ended up doing all of the prompting, designing of all the prompts, all the search, all the prompt for creating the HTML content and everything.

00:08:43 - Patrick Chouinard
And now based on that repository, I'm trying to get Claude Code [tool:Claude Code] to code just the scaffolding that's going to tie it together. So it can be a browsable website with all of those files stored in something like Supabase [tool:Supabase] in the back end.

00:09:09 - Ty Wells
I just built this thing for me this morning — it's basically a learning, app-based thing. It basically teaches you at a five-year-old pace and does a quiz and it's voice. So it reads it to you and then you answer.

00:10:29 - Patrick Chouinard
Oh, the other thing I stumbled upon today, a Visual Studio Code [tool:Visual Studio Code] extension that works as a Cursor [tool:Cursor] extension as well called SpecStory [tool:SpecStory].

00:10:43 - Ty Wells
SpecStory? That thing is amazing.

00:10:45 - Patrick Chouinard
What it does is it takes your chat log with the AI, no matter if it's GitHub Copilot [tool:GitHub Copilot] or Cursor or whatever, and dumps it into a markdown file. And you can infer Cursor rules or GitHub instructions from the markdown file from the chat log.

00:11:15 - Ty Wells
I've got to get that in because I take my prompts. My prompts are my... that's my golden...

00:11:26 - Patrick Chouinard
▶ But that thing's insane because now I have to teach a course on spec-driven development. So I basically build an application with SpecKit [tool:SpecKit] because it has to be an internal application level. I build the application with it. Now I've exported my chat logs and now I'm having Claude 4.5 [tool:Claude 4.5] go over the chat log to build the course material from the example of an application that was built using SpecKit.

00:12:04 - Patrick Chouinard
Listen, if it's not circular, it's not AI. Seriously.

00:12:10 - Ty Wells
Because that is the ultimate dog food, if there is any. I mean, that's all I'm doing all day. I'm taking from one and... you take from Peter and you gladly Paul will accept because it's waiting, right?

00:12:43 - Ty Wells
I'm just trying to fill in that blank so that I don't have to actually be that human in the loop. I'm setting those up as markdown files or the project structure using Daniel Miser's Kai project [tool:Kai].

00:13:00 - Tom Welsh
Dan Mohler — is that a new project he's got, not Fabric [tool:Fabric]?

00:13:20 - Ty Wells
Kai. K-A-I. Mine's Jessica. Don't worry, mine's Clara.

00:13:34 - Patrick Chouinard
▶ But I definitely want to show a spec story to Brendan, because imagine if he turns his chat log through ShipKit [tool:ShipKit] as documentation for ShipKit.

---

<!--SEGMENT
topic: SpecStory, Spec-Driven Development Course, and Prompt Library
speakers: Patrick Chouinard, Brandon Hancock, Tom Welsh, Ty Wells
keywords: SpecStory, spec-driven development, Claude 4.5, ShipKit, SpecKit, MCP, RAG, prompt library, chat logs, VS Code documentation, course material
summary: Patrick formally presents SpecStory to the full group and explains how he is using exported AI chat logs as raw material for a spec-driven development training course, with Claude 4.5 synthesizing the course content. Brandon connects this to a planned ShipKit MCP and a prompt library concept built on RAG. The segment highlights the meta-use of AI outputs as AI training inputs.
-->

00:14:22 - Tom Welsh
<Q>Literally, I just want to ask Patrick, what's the difference between specs and tasks? So we're talking about SpecKit, and we're talking about how you use tasks in ShipKit. Is there a difference, or is it just a different normal culture for the same thing?</Q>

00:14:38 - Tom Welsh
<A>Yeah, because spec in SpecKit, it's the overall specification, including the user story, the requirement, all of that, and the tasks are just sub-items within the specs.</A>

00:14:56 - Brandon Hancock
Yeah, so just real quick diving into what Patrick's talking about. What's crazy is, like, when starting to work on tasks — literally two years ago at Core AI, whenever we were going to go build something new, we literally had to do that, but we were doing it by hand at the time. So like, it would be a huge whiteboard, Excalidraw drawing, showcasing like, literally everything Patrick's talking about. And like, it literally would be a full spec before we would dive into actually building anything. So like, but now it's like, we'll just have AI do that, you know?

00:17:44 - Brandon Hancock
Patrick, how's it going, man?

00:17:49 - Patrick Chouinard
It's been a big weekend and a big start of the week. I was just talking to the guys about a new extension I found for both Cursor and VS Code called SpecStory. And Tom was kind enough to put the link already in the chat, but basically what it does is it allows you to save your chat logs from either Cursor or GitHub Copilot and save it to markdown documents in order to be able to extract rules from it for both Cursor and GitHub instructions.

00:18:34 - Patrick Chouinard
▶ I am building, I'm working actively to create a training course for spec-driven development at my client. And what I've realized is that I just did one vibe-coded application internally. It's a research pipeline that I built, but basically that entire application was vibe-coded using SpecKit. So, basically what I did is I exported my chats and gave it to Claude to analyze in order to infer the training material from the actual chat of an application being built using spec-driven development.

00:19:10 - Brandon Hancock
<Q>So was it mostly just extracting the rules or what was it kind of doing along the way?</Q>

00:19:14 - Patrick Chouinard
<A>Not just the rules. It's basically constructing a full training material — introduction, why would you do that, all of that. Because I've also inserted into that project as a subproject, SpecKit itself, and VS Code documentation. So with both of those as subproject and material that could be referenced, plus an example of a spec-driven development chat log, it had all explained why you would do that, what the structure of it is, and example at each step.</A>

00:20:00 - Patrick Chouinard
And I was thinking, you know all the questions you get on Discord about documentation? If you were to extract your discussion with ShipKit to build ShipKit and structure it as documentation, that would be absolutely insane.

00:20:25 - Brandon Hancock
It's so funny you say that because I've really been going deeper into your idea that you mentioned a few weeks ago on an MCP [tool:MCP] and really giving that serious thought. And I want to add that next as one of the big things to where at any point it's just like either ask Brandon, ask ShipKit, and like, what do I do here?

00:21:39 - Patrick Chouinard
Yeah, because I'm also thinking I've also started another project with my AI assistant — it's still in the intention realm. Basically a prompt library, but built on top of the simple RAG [tool:RAG] example. So the prompts themselves are in the RAG library and used to feed in a prompt designer that would build new prompts with all of the existing prompts as data to train on.

00:22:10 - Brandon Hancock
I can remember last week you showed off your prompt generator that followed perfect prompting practices.

00:22:23 - Patrick Chouinard
The sequential thinking prompt that I have is basically just a way to determine which question to ask in order to build the ideal prompt. And I gave that to Gemini 3 [tool:Gemini 2.5 Pro] and told it, like, create an interface in HTML in a single file based on the structure of that prompt. And that's what I showed last week.

00:23:04 - Patrick Chouinard
▶ And by the way, all of that is because I made one gift for myself for Christmas, and it's the $200 Claude Code Max subscription for December.

00:23:27 - Brandon Hancock
<Q>What I would love for science — I have not been able to hit it once. I've only hit on the $200 plan limit once. I've exceeded the $100 and need to go to $200. So I would love, because I know you're about to put a hurtin' on it, I would love if you could report back and let me know how high of a Claude Code score you get, how much usage you do for a week.</Q>

00:23:51 - Patrick Chouinard
<A>Well, at least in one day on Sunday, I managed to top off the five-hour limit on the $100 plan. So that's why I decided to go to the $200, because if I'm going to wait still and not be able to work for five hours straight, then...</A>

---

<!--SEGMENT
topic: Patrick's Gemini CLI Search Agent Demo
speakers: Patrick Chouinard, Brandon Hancock
keywords: Gemini CLI, Gemini 2.5 Pro, search agent, sub-agents, HTML dashboard, daily briefing, parallel execution, scaffolding, Supabase, Claude Code
summary: Patrick screen-shares his multi-agent daily research pipeline built with Gemini CLI, showing how parallel search sub-agents feed an analysis agent that consolidates insights and generates HTML dashboards. Brandon extracts a key takeaway about decomposing workflows into reusable sub-agents. Patrick also reveals he received early waitlist access to Gemini 2.5 Pro on Gemini CLI for free.
-->

00:24:29 - Patrick Chouinard
Let me show you. I just want to make sure I show the right one, because I have so many screens open right now.

00:24:57 - Patrick Chouinard
This one is the one I worked on also this weekend. It's basically the same search agent with Gemini, but I wanted to build an application around it, and I've tried many times, and it works, but it's never exactly what I want, and I realize why — the way we're doing this, it's something that is not part of the training material of the model yet. So basically, it doesn't understand what I'm trying to do. So I decided to build the individual prompts themselves that will do the search, get some search results, build one prompt that will create an HTML dashboard out of every one of those search results.

00:25:44 - Patrick Chouinard
So basically, the entire flow is there. So now I will give that to Claude Code and ask it to create the scaffolding around it. Just create a database to shove those prompts into, examples of how to call Gemini CLI to execute those prompts in series.

00:26:08 - Brandon Hancock
<Q>If I was to explain this simply, my understanding is you are kicking off a root agent who now is going to kick off sub-agents to perform each one of those tasks in parallel, who's each going to produce their own output, and then the parent agent then synthesizes all of it back into a final actionable report?</Q>

00:26:30 - Patrick Chouinard
<A>Actually, all the sub-agents, the search agents, are triggered and can be triggered in parallel. After that, there's an analyze agent. This one will look at all of the results from all the other search agents, consolidate it into one, surface insight, surface action to be taken upon the result of the search, and the create dashboard will take the output here.</A>

00:27:00 - Patrick Chouinard
It will generate one HTML file per search result plus the master daily briefing, but now I want the whole navigation of those files to be automated, all those files to be stored in the database and being available on basically the scaffolding for that.

00:27:25 - Brandon Hancock
▶ Real quick, I just want to like pull out something actionable for everybody. What I think is awesome about what Patrick's doing is like if you decompose what you're trying to do, you end up with a bunch of sub-agents where each sub-agent has best practices for like, man, here's what I love to do when working with development frameworks. And what's cool is like once you one time go through the process of building out these prompts, tiplets, sub-agents, whatever you want to call them, you get infinite leverage.

00:28:13 - Brandon Hancock
▶ The key takeaway, guys, is if you are working on something and you're like, man, I wish this happened every time automatically, use Claude Code to help you build the prompt that you can call forever going forward.

00:28:18 - Patrick Chouinard
▶ And by the way, I was accepted on the waitlist from Gemini to have access to Gemini 3 on Gemini CLI without being on the Ultra plan. That's what's building all of this. Seriously.

00:28:43 - Brandon Hancock
<Q>Are you using your own API key, right? You're not using the free limit?</Q>

00:28:45 - Patrick Chouinard
<A>That's all free. Yep.</A>

00:29:00 - Patrick Chouinard
Honestly, I'm guessing the fact that I'm running hundreds of calls to Gemini CLI a day probably had something to do with me being on the waitlist.

---

<!--SEGMENT
topic: Ty's ShipKit Studio and Voice Learning App
speakers: Ty Wells, Brandon Hancock, Patrick Chouinard
keywords: ShipKit, ShipKit Studio, Claude Code, E2B, Lovable, Eleven Labs, voice interface, quiz app, wireframes, logo generation, DALL-E, web container, token limits
summary: Ty demonstrates two projects: a full GUI wrapper around the ShipKit project-creation workflow (dubbed "ShipKit Studio") that includes wireframing, DB schema visualization, and live code deployment via E2B; and a voice-based learning app built on Lovable with Eleven Labs TTS that teaches topics at adjustable levels and quizzes users. Brandon proposes a "Prompt Dojo" SaaS concept inspired by the learning app.
-->

00:29:35 - Ty Wells
Hey, what's up, guys! Hope you had a great Thanksgiving, buddy. Well, I can tell you, I've hit that limit on Claude Code. I had to open a new account yesterday.

00:29:58 - Ty Wells
I'm working on — I did promise you guys some stuff and share the screen with you. We talked about last week, what Patrick did for the ShipKit mentor. And so I decided to take that to another level.

00:30:42 - Ty Wells
So this is one of the projects I'm working on, so I can come in here and sort of preview how I want things to look. It's the same template that you're driving. The template behind it is driving it. And here are all of the steps. The logo. You go through, same thing, you know, the type of logo that you want, but I actually have it now generating the logo. So it brings over and it'll generate the logo for you.

00:31:17 - Ty Wells
So that's what it's doing here. I know you had some steps in there to go out to DALL-E [tool:DALL-E] and some other stuff.

00:31:55 - Brandon Hancock
Just real quick, just so everyone else has context, every time you start off a new project in ShipKit, there's like a 10-step process where you go through like coming up with your master idea, app name — so like there's full-blown prompts that you always pass over to your agents to help you do this, and Ty turned the whole process instead of like manually just only doing everything through a CLI, he actually converted it into a full-blown web app that basically does it all for you in a really nice GUI. ShipKit Studio — that's what it is.

00:32:04 - Ty Wells
I actually used ShipKit to build it initially and then I reverse-engineered the prompt to create a project in ShipKit so it has all of the necessary pieces. But the layout, the wireframes I did in here as well, so you can adjust them and move them for each page and reorganize whatever wireframes you want.

00:32:52 - Ty Wells
Then I've got the DB build and do a schema just so it's a little easier for them to visualize how it's tied together.

00:33:00 - Ty Wells
So this is the architect — once your planning is complete, you can go — this is what I'm working on, this is not working yet — I'm actually going to build the application live, launch it into E2B [tool:E2B], so it builds out the code, and you never actually touch the CLI. It builds the code based off of their — it's launching an instance. I was working with a web container with that, I didn't like the consistency, so I set up an E2B account to launch an instance.

00:33:43 - Brandon Hancock
Ty, this is — I'm lost for words at how cool this is, because like, I feel like I've made B1, and you just made B20. Because if you keep taking it to the extreme and say, hey, let's just make it better, more frictionless, and just have AI do more of the work for you and a better UI, you end up with this. This part right here, if you got this nailed, that would be insane. Because at the end of the day, it's going to be expensive to build. But like, if it auto-builds the entire roadmap for you, I mean, like, it's Lovable [tool:Lovable] on steroids.

00:35:00 - Ty Wells
One last quick thing I want to say — basically what one of the things I run into every day is, you know, there's so many shiny objects out there, right? And so this isn't one of them, but I built this little interface here, just a little web app so I can automatically go right into — if I'm looking for a particular topic, I'm just trying to get an understanding of a concept.

00:35:31 - Ty Wells
Llama means Large Language Model Meta AI. Imagine a super smart digital alpaca that talks. So basically you can go through the steps, and then it has a little quiz at the end. So once you're done with the session, it's sort of a memory — it's to help you with retaining.

00:36:10 - Brandon Hancock
<Q>Are you using Eleven Labs [tool:Eleven Labs] for the voice?</Q>

00:36:12 - Ty Wells
<A>I'm using Eleven Labs for the voice, yes.</A>

00:36:39 - Ty Wells
I'll come across a topic and I just don't know enough about it. I want to know about it. And then, of course, because when I'm driving, I'll just be able to respond with speech, which I'm building that in. So you can just respond with your answers.

00:38:07 - Brandon Hancock
Would you mind pulling that back up? I want to tie together a few ideas that Tom actually brought up maybe a month or so ago. So as like a new startup idea — okay, so here's what I love about this. Like, obviously, you have voice, you have AI, like, and people are learning. Absolutely love it.

00:38:33 - Brandon Hancock
▶ One of the biggest issues I see when developers build something over their shoulders, their prompting is their limitation, specifically their ability to like speak code. Like what I mean by that is like most time, like, you know, we'd say level one developer — it's like "make the page do blank." Well, like that's like, you know, a sentence, but it didn't give the AI any help. So to figure out what to do where. Like a level 10 would be like, hey, can you please update this page that's in this layout where the layout already has context about the user state...

00:39:28 - Brandon Hancock
▶ Cool idea — what I want to do at some point is basically make like a Prompt Dojo to like, hey, 20 bucks a month, we're going to show issues on screen. And it's your job, like in the Prompt Dojo to articulate how to fix the problem to where it forces you to think through it. And then it grades your prompt against what it should have been, teaches you the missing concepts. So I think that would be like a really cool project I want to do in 2026.

00:40:33 - Ty Wells
Actually, I built this on Lovable, so I use Lovable Cloud, which is Supabase. They're doing their own environment.

00:40:49 - Brandon Hancock
▶ Yeah, please keep me posted on the code deployment side of things for ShipKit version 10,000, because I would love to see that.

---

<!--SEGMENT
topic: New Member Introductions — Nick, Glenn, Scott
speakers: Nick Mohler, Glenn Marcus, Scott Rippey, Brandon Hancock, Ty Wells, Tom Welsh
keywords: Claude Code, Obsidian, warp.dev, Drive feature, mobile development, AI transformation consulting, inflection points, NNN Automations, Click Consulting, iOS Android
summary: Three new members introduce themselves. Nick (25, non-developer background, AI transformation consulting) is transitioning from Claude Desktop to Claude Code and plans to migrate Obsidian notes. Glenn (veteran developer since the 90s, CTO background, mobile consulting at Click Consulting) discusses warp.dev's Drive feature as a cloud-synced markdown store and shares his thesis that mobile/web UIs will be replaced by AgentOS. Scott Rippey is acknowledged as the connector who brought multiple new members.
-->

00:41:45 - Nick Mohler
How's it going? This is my first call with everyone here. I've actually never watched any of your content before, Brandon, and you were referred because Scott Rippey [tool:Scott Rippey] told me about you. He speaks very highly of ShipKit. Everyone in the community says that the calls are amazing and that you guys have a great vibe with it.

00:42:17 - Nick Mohler
I'm not good with Claude Code. I'm actually only using the Claude Desktop [tool:Claude Desktop] and I've been meaning to switch for like a month and a half, two months. I'm 25 years old. I don't have the background in doing like all this development, coding, things of that nature. But I want to have the correct foundation of where I can pick up this new age of development.

00:44:04 - Brandon Hancock
What I would really recommend to do, Nick, is I basically create a, like, Brandon life project where every single thing that I do, I put into my, just on my local computer so that I can start to automate it.

00:44:46 - Brandon Hancock
▶ What's cool about using Claude Code on your local computer is you'll start to build out the whole process for doing the different verticals of your life, like your current business, like with the coaching and consulting. You'll get to slowly build everything out. What's awesome about that is then I just throw transcripts. Everything that we do, I just throw in there. So we get to move so fast for our business.

00:47:16 - Nick Mohler
What kind of made me think about that — it's like right now I've just been using Obsidian [tool:Obsidian] for all the markdown files and just putting everything onto there as my living database. And that's the reason I'm actually wanting to move to Claude Code — having all the different verticals but in one place. I'm tired of Claude Desktop with it just being all the project folders.

00:48:47 - Brandon Hancock
Glenn, been doing some something similar with Warp [tool:warp.dev] and their Drive feature, thinking to move over to Claude Code. I've actually never got to try the Drive feature. Glenn, would you mind just sharing a little bit more about that?

00:49:16 - Glenn Marcus
Yeah, so like in any type — even when I got first started with ChatGPT [tool:ChatGPT] — my biggest challenge in working with these like sessions are really ephemeral, right? So this stuff needs to live somewhere so I can build knowledge base around it, get repeatability, scale and growth with it, right? Compounding effects.

00:49:43 - Glenn Marcus
So what I liked about warp.dev — it's just another agent that lives in the terminal itself as opposed to standalone CLI. They just had a built-in Drive feature where instead of trying to figure out where to throw stuff or try to throw them in various locations on your local machine, just throw them into their drive, organize it yourself, or let the agents organize it for you. That drive syncs to all of your other sessions. So it's basically just a cloud disk effectively for all your markdown.

00:50:31 - Glenn Marcus
▶ Yeah, it's also meant for collaboration, so you can invite other people into your shared drive effectively, like a Google Drive, but it's always available to you in the local terminal.

00:50:42 - Brandon Hancock
That's awesome, because that's actually one of the biggest issues of my approach right now — it works great as an individual contributor, but there's not really a way for someone else to access it.

00:51:47 - Glenn Marcus
My background — I'm like, you know, old-school developer, started in the 90s. My big superpower is that I've been able to always identify really important technologies as an inflection point. So like back in the 90s, it was object-oriented programming. Mid-90s, I was doing client-server. I was doing web application servers and web app development on large-scale e-commerce sites in 1996. I built a site called Topaga as a Silicon Valley startup. I was a CTO over there, built a team of 40. We had 14 million users. We were sending over five million emails a month. We took down AOL and Hotmail multiple times. And then 2009, I jumped on the mobile wave. I run a company called Click Consulting [tool:Click Consulting]. Clients hire us like Merriam-Webster, Gucci, Expedia to build their iOS and Android native mobile apps.

00:53:32 - Glenn Marcus
No surprise to anybody in this room, AI is clearly one of these inflection points. And what I like about the space is that it's a complete reset, right? There's no 10-year expert on AI. We're all kind of — it's a level playing field.

00:55:56 - Glenn Marcus
I have never seen, none of us, I think, have ever seen a firehose like AI, right? So it's all coming at us. So that whole noise-to-signal and pulling out the signal is really challenging with AI and the shiny object syndrome.

00:59:33 - Glenn Marcus
I have a very strong prediction that mobile apps and website front ends, UIs, are going to go away entirely. Like in the next five-year horizon. So most of my value add to my clients is building UI, UX, information architecture, product strategy. And I think the majority of that is going to go away, and the main interaction is going to be AgentOS, and you're just going to be working with your personal agent to get the same services you're getting from going to all these bespoke apps and different interfaces.

01:00:37 - Glenn Marcus
So I'm looking to pivot for consulting from mobile into AI right now.

01:01:00 - Brandon Hancock
▶ What I'm trying to figure out is where does it pivot next — because right now I think it pivots to more system design, pivots to more actually thinking through core user problems, like what am I actually trying to solve, the creativity part, understanding the user deeply, figuring out what to build, the marketing. But the actual UI — probably spot on, we just saw what Gemini 3 did as soon as it dropped, single shot in a few seconds, a beautiful UI. That normally would have taken a mock-up, UI/UX expert to mock it up, pass it over the wall to the front-end engineer, the front-end engineer spends a week making it happen — now getting compressed to 20 minutes.

01:02:30 - Glenn Marcus
I think where it is shifting to is the direction where OpenAI [tool:OpenAI] is going right now with their app widgets within chat, right? Where your services can surface the right UI at the right time for the person to bring the human back into the loop — present a choice, do a confirmation, or perform a transaction. But the need to build multi-page sites or apps — there's no reason for me to go to Airbnb.com anymore. Let my agent go plan my vacation for me and pop up a widget whenever it needs something from me.

---

<!--SEGMENT
topic: Claude Code Workflows, Skills, and Playwright Testing
speakers: Brandon Hancock, Prem, Scott Rippey, Tom Welsh
keywords: Claude Code, Playwright, MCP, PostHog, ShipKit templates, IndieDevDan, skills, slash commands, agents, mobile responsiveness, Tailwind, end-to-end testing, Web Dev Dan
summary: Prem asks about PostHog dashboard filtering and Playwright for UI testing. Brandon demonstrates a ShipKit prompt template that uses Playwright via MCP to automate mobile responsiveness testing across all viewport widths. Scott shares a breakdown document comparing Claude Code concepts (skills, slash commands, MCPs, agents) inspired by IndieDevDan's YouTube content. The segment provides concrete guidance on integrating Playwright into agentic development workflows.
-->

01:06:07 - Prem
So PostHog [tool:PostHog], again, based on the conversation we had last time I was able to implement it. I just had one big question on that. <Q>Do you kind of use different projects for each of the environment, or do you kind of have one project and then kind of have an environment variable to kind of differentiate it?</Q>

01:07:22 - Brandon Hancock
<A>Yeah, so the way I like to set up PostHog is I will set it up as one project. However, when I'm in PostHog and tracking events, I turn off things from localhost. Or, like in my dashboard widgets, that's where I add in the filters to say, hey, I don't — anything coming from a localhost, I don't care about.</A>

01:09:12 - Brandon Hancock
▶ The easiest way to build out these dashboards for your app is, did you get a chance to set up the PostHog MCP? My favorite way to do that is just to literally say, hey PostHog, on my dashboard, I don't want to show local development traffic from port 3000, localhost 3000. Can you just eliminate that? And then it will automatically make the filter for you.

01:09:54 - Prem
Playwright.dev [tool:Playwright]. Again, I know I've heard a lot about this in this forum, but I'm just getting started. Any good suggestions on videos or anything anybody can share on how to go about it?

01:10:09 - Brandon Hancock
Yeah, so Web Dev Dan [tool:IndieDevDan YouTube channel], he makes phenomenal Claude Code videos. He is my Claude Code inspiration. He literally just did one today about sub-agents where each sub-agent is kicking off a Playwright instance to go off and test your UI.

01:10:41 - Brandon Hancock
▶ The short lesson is Playwright — add it as an MCP tool, and then once you do that, use it for all sorts of UI testing. Like that's the easiest way — it's just like hook up Playwright and then anything you want to do, it can load the website, it can test all the different things.

01:11:02 - Brandon Hancock
I use Playwright when I'm developing, because once again, just for everyone to understand the problem — I was working on a startup landing page and I was spending forever to try and get it to work great on all sizes. Because we had some really fancy custom demos that we wanted to look great on all screen sizes. So I was like, hey, Tailwind [tool:Tailwind CSS], make it look good at 1400 pixels. And then I would shrink it a little bit more and I'm like, no, it's broke now for 1200 pixels. Eventually I was just like, wait, why am I doing this repetitive task a thousand times? Like I should just have my agents do this for me with Playwright.

01:12:04 - Brandon Hancock
So this is an example of I made a prompt template that performs a task where it performs mobile responsiveness on a specific page, and it tests all possible widths between these sizes. What it does when you hop down to the implementation part, it goes through these steps, where it's going to open up an instance of Playwright, locate the target component. Once it does that, it is going to continually shrink the page or grow the page for every different viewport along the way. It's going to analyze each screenshot to identify, man, at 500 pixels it's broken until we hit 800. So I need to fix it in that gap. Then it's going to come up with an implementation plan.

01:13:23 - Brandon Hancock
▶ You just kind of tie together prompt templates with MCP tools such as Playwright to automate tasking for you. And you could do the same to build out end-to-end tests where you could have, like, let's say you have a core workflow for your application of like, log in, go upload a document, wait, ask a query, make sure it has these results. Like you could 100% start to create your own test suite of end-to-end plays where the agent's clicking around.

01:13:48 - Scott Rippey
Brandon, I love that you brought up IndieDevDan because I just put a link in there that I created. One of his videos where he went over skills, but everything else. I actually broke down with how I've done stuff, and how he's doing stuff, and his videos linked in there, but I had this long conversation with Claude Desktop that I really crafted this document where like, you know, everybody was like, skills, and then replaced everything with skills, and it was like, his thinking is like, no, he's like, hey, slash commands, MCPs, agents, skills — about how they all build on each other, and how you can really learn how they all work together, and there's some overlap.

01:14:46 - Brandon Hancock
<Q>Would you mind, just out of curiosity, in the actual school, would you mind just like, copying, like, a quick paragraph and dropping it? Because I think there's so many people that would love to read this article.</Q>

---

<!--SEGMENT
topic: AI Video Pipeline and Pokémon Template Repurposing
speakers: Brandon Hancock, Prem, Scott Rippey
keywords: AI video generation, Pokémon template, Claude Code, Bible study, prompt templates, ShipKit, local pipeline, web app deployment, Eleven Labs, YouTube
summary: Prem asks about repurposing Brandon's Pokémon AI video generation template for a custom video series. Brandon explains how a community member (Elijah) already adapted the seven-prompt template for Bible study videos in 40 minutes by simply re-prompting Claude Code to rewrite each prompt for a new domain. Brandon also previews the next ShipKit project: converting a local AI pipeline into a deployed web application.
-->

01:16:58 - Prem
I kind of looked at the Pokémon video that you did. I was just trying to play with like creating a video kind of, you know, basically creating few characters and like, I want to kind of create more of like a series or something like that. <Q>My question is, is this like, I know it's more of Pokémon related, rather than kind of creating my own — is that a template I can start with and kind of take out all the Pokémon, or would you suggest starting fresh, or do you have anything like a ShipKit template planned around that?</Q>

01:17:37 - Brandon Hancock
<A>Yeah. So definitely if you get a chance, check out the call we had this morning, because Elijah, in the ShipKit call, he took that template that I posted on YouTube for all of you guys. And he literally — I guess he's in like a Bible study group. And what he did, he was like, hey, Brandon made these seven prompts that are focused on taking a name of a Pokémon and generating the output, which is the Pokémon video. However, you know, for my Bible study group, what I want to do is start to create like, you know, basically AI-generated videos for different scenes from the Bible. So what he did is he just said that and told Claude Code to redo each prompt, but from a more Bible approach, it recreated the seven prompts, it overwrote them all, and then he literally just said David and Goliath, and then it just did it all. And it made a video, and we showed it in the video this morning. So it literally took him 40 minutes, and he made a video, just redoing the whole thing.</A>

01:18:38 - Brandon Hancock
▶ Thing two is, the next ShipKit project is to showcase — fantastic, we have that working locally with Claude Code — how do you actually take an AI pipeline on your local machine, and actually build an AI web app for that. So that's where we're going with that one.

---

<!--SEGMENT
topic: New Member Introductions — Ryan and Lan
speakers: Ryan - One Stop Creative Agency, Lan, Brandon Hancock, Scott Rippey, Patrick Chouinard
keywords: Claude Code, social media automation, Zapier, real estate, MLS data, Supabase, PostGIS, Postgres, pandas, parquet, productized service, Nicholas Cole, ghostwriting, Gemini API, video processing
summary: Ryan (UK videographer/web developer) describes building a productized social media management service with a Claude-and-Zapier-powered content approval and scheduling app. Brandon advises on scaling the model and references Nicholas Cole's ghostwriting academy. Lan (real estate professional) asks how to handle 50 million MLS records for time-series market analysis; the group recommends starting with Excel/pandas locally, then migrating to Postgres with PostGIS and Supabase for a web application.
-->

01:24:00 - Brandon Hancock
All right, Ryan's from the UK and he's new here too. So I want to just let him introduce himself.

01:24:00 - Ryan - One Stop Creative Agency
I'm Ryan. I have been coding just basic HTML, CSS, a little bit of JavaScript since I was 13. My stepfather builds membership systems for huge multi-corporations — the NHS, National Trust, a few other places in the UK. So he taught me how to code from quite a young age. I picked up a camera for the first time in 2020 during COVID, and joined an online school called Full-Time Filmmaker [tool:Full-Time Filmmaker], run by a guy called Parker Walbeck. And that's how Scott and I met.

01:26:10 - Ryan - One Stop Creative Agency
I got made redundant in September. So took my little business that I've been running for seven, eight years, just doing websites, a couple of years full time in September, and do a lot of videography for estate agents and stuff. And then I decided to make a client portal for all of my clients.

01:29:00 - Ryan - One Stop Creative Agency
I'm currently building a sodding great app that integrates with Claude and Zapier [tool:Zapier] to essentially run all of my clients' social medias, and I just upload the content, shoot the content, and put the descriptions in, and then...

01:29:21 - Scott Rippey
Brandon, you'd be impressed with this. He has come a long way, a long way on this. He just showed this to me earlier today, and I'm like, my boy over here is building. It's about three quarters of the way there.

01:29:30 - Ryan - One Stop Creative Agency
There's some refinement that's needed in a couple of additional bits that I need to build in for the client side so they can request amendments. But they have a full approval mechanism, whole month's worth of content being built, and it just automatically generates every week to keep them always having a month's worth of content available. I just turn up once a month and shoot, upload it into the platform.

01:30:12 - Brandon Hancock
▶ What Ryan is doing is it sounds like he's building a productized service, which is insane, because you're no longer in the hour-for-dollar model. It's just like, I will give you this result. And what's sick is like, it sounds like he probably knows exactly how to do the service. And now just filling in the gaps with Claude Code agents tasks to actually deliver high-quality results. What's so cool about this is how scalable it is, because at this point, as long as you can pay the Claude Code membership, there's no reason why the next bottleneck is literally going to be feedback from clients and shooting the video.

01:31:16 - Ryan - One Stop Creative Agency
If I can just run social media for people, turn up and shoot once a month for them and load the stuff on — they pay me between 700 to 1000 pounds per month. I can really only cope with two or three of those people, clients at the moment in terms of my time. But if this works, which I think it will, I can probably run 20, 30 clients.

01:32:43 - Brandon Hancock
▶ One, I mean, Alex Hormozi, 100 Million Dollar Offers [tool:100 Million Dollar Offers], probably for your top of funnel, like the actual offer that you're going to productize. Would 100% dive back into that if you haven't got a chance to read it. Another one that I think would be very cool to take inspiration from — there's a guy named Nicholas Cole [tool:Nicholas Cole YouTube] on YouTube, and his whole game plan is ghostwriting. He has a whole ghostwriting academy where he's teaching people how to kind of do what you're doing, but without the video.

01:34:36 - Brandon Hancock
▶ I would seriously check out using the Gemini API [tool:Gemini API] for their video processing. You could literally use Claude Code with FFMPEG [tool:FFMPEG], split it at 400 megabytes, upload each video using the Google Generative AI API, pass them up, get the full context of the video, and then start your pipelines.

01:37:22 - Lan
So I'm actually in real estate. I'm trying to build my application. My question — I use vibe coding, Claude Code, to build some of the real estate app, and we have, in real estate, we roughly have 50 million records data per year. So, first of all, from a technical perspective, I don't know whether it should be structured as a simple CSV file, or Parquet [tool:Parquet], or I should structure as a Supabase-type relational database, or how to really think about a data-intensive type of project.

01:43:00 - Brandon Hancock
<Q>So you've been able to download it in the past. Is it like a CSV? What are we actually downloading?</Q>

01:43:10 - Brandon Hancock
<A>So they have .txt files. So essentially we treat it as a CSV file. And how big is it? Like how is it a gig? Roughly per year, it's like maximum 20 megabytes.</A>

01:43:49 - Brandon Hancock
▶ Here's how I like to tackle these type of projects. Step one, I would have an agent to where I could point to a folder that's full of text files, and it should convert them to CSV files. That's how I would start off. Next, what I want to do is, let's say we're going towards the process of making a full-blown neighborhood analysis. Maybe at step two, I have some sort of agent that is able to start to go through the data and within a certain lat/long area, and it's going to start to do queries against our CSV data to find the properties within this neighborhood. Step three is going to track these property IDs over a series of years.

01:47:21 - Patrick Chouinard
▶ For that specific workflow though, wouldn't it be easier to start with a simple pivot table in Excel? Because sometimes we tend to go to AI all the time for everything, but there still are some scenarios where deterministic applications are still a good way to go. And for this, to analyze that kind of data, I think it's basically a subset of what Power BI [tool:Power BI] would do with larger data sets. But I think a good way to start is just Excel and pivot tables.

01:47:54 - Lan
Actually, you could use Copilot inside of Excel to help you create the pivot table.

01:48:39 - Patrick Chouinard
▶ And actually, now that Copilot is able to write Python inside of Excel to do data analysis, there's a whole lot you can do without before you actually need another application or building something custom outside of the Excel world.

01:50:24 - Brandon Hancock
▶ If you do start to go more code style, the main libraries you're going to see that get used are pandas [tool:pandas]. And that is capable of handling insanely large files. So if you do run into issues, I would definitely check out like, hey, Claude Code, I'm trying to look at this 20-megabyte file. Can you please load it into pandas so that I can start to ask questions about it.

01:53:55 - Brandon Hancock
▶ I would 100% use Postgres with an extension called PostGIS [tool:PostGIS], which is a great extension to make sure that your database works great with properties. Because at the end of the day, a property usually is just a combination of a lat and a long. And the way it does is it kind of breaks things up into lat/long. So whenever you want to quickly find houses in this area, it does a much better job at indexing the 50 million records to quickly find houses or properties in this range.

01:55:42 - Brandon Hancock
▶ I love using Supabase for this because you have authentication, you have a database that you just seeded, you have the ability to upload files — there's so many things that Supabase does. And it's kind of a one-stop shop. So we're not having to hop between 10 different tools.

---

<!--SEGMENT
topic: Enterprise AI Deployment — Security, Compliance, and Architecture
speakers: Brandon Hancock, David, Patrick Chouinard, Ryan - One Stop Creative Agency, Glenn Marcus
keywords: Claude for Financial Services, LangGraph, NetSuite MCP, Bedrock, Azure, GDPR, SOC compliance, audit trail, data residency, read-only permissions, Anthropic Opus 4.5, local model, on-premises, enterprise agents
summary: David (CFO background) asks about deploying AI agents within corporate ERP systems (NetSuite, QuickBooks, Xero) and the security, compliance, and architecture considerations involved. Patrick strongly recommends Claude for Financial Services for its audit trail and data residency guarantees. Brandon outlines a model-agent-tools stack using Anthropic Opus 4.5 and custom MCP servers. The group discusses GDPR risks, read-only permissions as a starting point, and the trade-offs between on-premises local models and cloud-hosted proprietary models. Brandon previews LangGraph as the enterprise agent framework coming to ShipKit in January.
-->

01:57:13 - David
Oh, hey, Brandon. So, yeah, look, I haven't attended one of your tutorials in a while. And so just trying to pick back up on the AI self-learning train. My career background is in finance and trading, right now I'm the CFO of a company and my general interests are just in how to utilize AI and agentic systems with AI to optimize the operation of and make more efficient the operation of my business and businesses that I want to establish in the future.

01:58:50 - Brandon Hancock
▶ The way I have been tackling it internally by firing myself from as many tasks as I can is every week I aim to automate and build an AI employee for one thing that I do. So, for example, like on YouTube, I genuinely hate the process of coming up with different titles and everything. So what I do is I then create an AI agent that I feed in every previous title I've ever made. And then I pass in a bunch of high-performing videos and basically train out a title and hook agent.

02:02:00 - David
▶ I think of skills as small employees who are specialists at one outcome, and eventually, if you tie together enough outcomes, you've built the entire system, to where now, I have the title and hook generator, which then creates the title and hook, it then creates the outline for the full video, after I have the video, I record the whole thing, then it comes up with my email, where I can blast that out to everybody, it comes up with my LinkedIn post, my every other post, to where like, I basically have employees to automate my entire YouTube business, where the only thing left is me doing the actual coding, exploring the topic, and recording.

02:03:40 - David
<Q>Which is the best code agent for interacting with new APIs in your opinion? Is there a better one than others?</Q>

02:04:48 - Brandon Hancock
<A>The Opus models are the best at doing tool calls. So Anthropic Opus 4.5 [tool:Anthropic Opus 4.5] is by far the best. That is the best tool-calling model.</A>

02:05:19 - Brandon Hancock
▶ With that being said, let's see — NetSuite MCP [tool:NetSuite MCP]. So now that we've found a model, great. Well, now we need an agent. So at the end of the day, these large language models, they need instructions on how to actually perform, breakdown tasks, and actually attack it in an agentic manner. So like, for personal use, Claude Code, phenomenal. And now the next step is, great, we have the model, Opus, check. We have the agent tool that we can control locally. We're going to use Claude Code. The next step is to start adding in the tools. What I would recommend is — if there's not an MCP, which is just a really clever way of adding in API calls to your agents — what you can always do is just say, hey, Claude Code, I would like you to build an MCP server that builds out all the different functionalities for all of the possible NetSuite API calls.

02:08:12 - Brandon Hancock
<Q>When you start deploying that kind of infrastructure within a corporate setting, what's the kind of recommended repository locations for the different components? How do you get it plugged in to the firm-wide architecture? What are the risks and considerations you have to think of in terms of security and exposing tools to people that they shouldn't be exposed to?</Q>

02:08:26 - Brandon Hancock
<A>When you want an employee to be able to do this, you almost need the developers to be able to say, hey, I'm generating for this financial team, I'm going to give them the appropriate API keys, the appropriate permissions, and allow them to only read data, most likely to start, where they can't make any issues and delete or write stuff they weren't supposed to.</A>

02:09:00 - Brandon Hancock
▶ Everything I've been describing is running on a local computer. Eventually, when we're actually talking about building internal productivity tools for the company, and to build out these workflows, I would 100% look at LangGraph [tool:LangGraph], as like, that is like the enterprise agent tool of choice. And I'll be going deeper into LangGraph, LangChain [tool:LangChain] within ShipKit in January.

02:09:31 - Patrick Chouinard
▶ Yeah, I just want to say, if you want to connect tools like that, just be very careful, especially if you're building an MCP server in a corporate environment. Yes, I'm absolutely agreeing with Brandon — it should be read-only in the beginning, especially if you're connecting with an ERP system. You don't want an AI going rogue without being tested to the hilt before it does any kind of change in an ERP system.

02:10:00 - Patrick Chouinard
▶ I mentioned Claude for Financial Services [tool:Claude for Financial Services] for one reason, because it already has all the connection to all of the financial data streams, as well as a lot of pre-built skills and MCP servers built for the financial industry with the most important thing — audit trail for everything it does, which none of the other models will have. And even if you do everything with Claude, you're going to do the work, but you're not going to have the audit trail that SOC compliance, for example, will require where Claude for Financial Services adds that on top of all the other tools that they're offering. So it's pretty much a go-to solution for investment firms.

02:11:00 - Patrick Chouinard
▶ You've got to be super careful, make sure you let your IT guys know that that's what you're doing, and depending on what country you're in, you've obviously got to be careful of your data protection laws as well, because depending on what you're sending where, you might end up sending sensitive information into an open AI model that then uses that for learning, and then there's a whole route of privacy problems that you could create yourself as well.

02:12:07 - Patrick Chouinard
▶ That's exactly why I'm talking about Claude for Financial Services, because they're built for that and they have contractual obligation to be completely isolated and making sure that your data is never going to be used for training.

02:13:10 - Brandon Hancock
▶ Just be careful with Bedrock [tool:AWS Bedrock] because there are some data residency issues that you might run into. Not all models are available in all geographic locations. We ran into this at my client site. We're in Canada and some of our requirements are for the data residency to be only in Canada and some of the Bedrock models are not available in Canadian data centers.

02:14:00 - Brandon Hancock
▶ When it comes to Sonnet and Opus 4.5 being the best tool-calling models right now, you can't run them locally — that's the gotcha. It's like all the good stuff is proprietary, and you have to run on Google Cloud, Azure [tool:Azure], Bedrock, one of these places. And the best open-source model right now is like Kimi K2 [tool:Kimi K2], which is like one of the best open-source tool-calling models, but it's still nowhere as close to as smart or powerful as some of the 4.5 models. And you're also having to pay the tens of thousands of dollars to actually buy the servers, hook them up, someone is having to manage them. So like, it's a hundreds of thousands of dollars of investment, versus just spinning it up in the cloud. So there's always trade-offs for on-prem versus cloud for this kind of stuff.

---

=== UNRESOLVED SPEAKERS ===

- **Prem** — appears as "Prem" throughout; no canonical form in alias map
- **Adam** — appears as "Adam" throughout; no canonical form in alias map
- **Lan** — appears as "Lan" throughout; no canonical form in alias map
- **David** — appears as "David" throughout; no canonical form in alias map
- **Nick Mohler** — appears as "Nick Mohler" throughout; no canonical form in alias map
- **Glenn Marcus** — appears as "Glenn Marcus" throughout; no canonical form in alias map
- **Ryan - One Stop Creative Agency** — passed through unchanged; no canonical form in alias map