=== SESSION ===
date: Unknown (transcript references recent events including January/February timeframe based on Atlanta snowstorm and New Zealand summer internship context)
duration_estimate: ~2 hours 45 minutes
main_themes: Claude Code adoption and workflows, AI productivity tools for enterprise and non-technical users, RAG pipeline optimization with cross-encoder re-ranking and recursive LLM (RLM), knowledge artifact generation via NotebookLM, AI-assisted content creation and training documentation, voice agents, local model experimentation with Ollama/Qwen, freelancing and business monetization strategies, AI in education

---

<!--SEGMENT
topic: Pre-Call Chatter and Introductions
speakers: Patrick Chouinard, Paul Miller, Hemal Shah, Morgan Cook, Brandon Hancock
keywords: Atlanta snowstorm, Montreal, community management, WhatsApp, Brandon Hancock, pre-call logistics, geographic introductions, French language, Cowork tool
summary: Participants exchange informal greetings and discuss geographic contexts including Atlanta's rare snowstorm and Patrick's Montreal winters. Brief discussion of community management logistics and keeping the online call active between in-person sessions.
-->

00:03:04 - Patrick Chouinard
Thank you.

00:03:37 - Patrick Chouinard
Hi, Paul.

00:03:39 - Patrick Chouinard
Hey, Patrick.

00:03:40 - Paul Miller
How are you going?

00:03:41 - Paul Miller
Good, good.

00:03:46 - Paul Miller
How is your workplace with all those AI projects going on?

00:03:53 - Patrick Chouinard
Yeah, I actually have some pretty interesting updates for you guys.

00:04:05 - Paul Miller
It's one thing to get everyone excited about AI.

00:04:07 - Paul Miller
It's another thing to implement it in an enterprise.

00:04:13 - Patrick Chouinard
Yeah, because again, you get some people excited, not everyone.

00:04:20 - Paul Miller
You get people scared. You get some that are excited.

00:04:22 - Patrick Chouinard
You always have some that it never goes fast enough. Some others it goes way too fast.

00:04:30 - Paul Miller
Or the lack of practical understanding of what it is to run something in prod.

00:04:47 - Patrick Chouinard
But no, I think I've stumbled upon something because of you guys, actually.

00:04:59 - Patrick Chouinard
<Q>Do you know if Brandon has thought about using the community to make the call live between his presence?</Q>

00:05:12 - Paul Miller
<A>Yeah, I think he has, but I think he's waiting for you and me to go back to keep — he kind of needs someone to hold the baton, and I'm happy to work with you to do that, because we've got to keep it going online as well as on the call.</A>

00:05:38 - Patrick Chouinard
Yeah, definitely, I'd be more than happy.

00:05:44 - Paul Miller
I'll just flick him a WhatsApp, maybe copy me in.

00:05:55 - Patrick Chouinard
Okay, yeah, flick him an email or text.

00:06:05 - Paul Miller
Hey, Morgan.

00:06:08 - Paul Miller
Hey, Mo.

00:06:10 - Hemal Shah
Hello, guys.

00:06:12 - Morgan Cook
Good morning or afternoon or whatever time of day it is in your part of the country or world.

00:06:19 - Hemal Shah
Here in Atlanta, we are expecting a huge snowstorm this weekend. So everybody is running around to hold stuff.

00:06:29 - Patrick Chouinard
I cannot handle snow.

00:06:36 - Hemal Shah
How often does it snow in Atlanta? Every three, four years, five years. So they are not prepared.

00:06:42 - Paul Miller
I'm curious, what's a huge snowstorm for you guys?

00:07:00 - Hemal Shah
When it stays on the ground, it doesn't melt, I suppose.

00:07:07 - Paul Miller
We get snow once every 40 or 50 years.

00:07:18 - Patrick Chouinard
We get at least two or three, one and a half to two feet snowstorm per year.

00:07:29 - Hemal Shah
Patrick, you are in Canada, right?

00:07:34 - Patrick Chouinard
No, South Shore Montreal.

00:07:38 - Paul Miller
My cousin lives in Montreal.

00:07:55 - Hemal Shah
You speak French — it's used heavily in Montreal, right? So you speak French?

00:08:02 - Hemal Shah
Yeah, it's my mother tongue.

00:08:07 - Paul Miller
Comment ça va?

00:08:12 - Morgan Cook
Oh la la, c'est magnifique!

00:08:31 - Patrick Chouinard
No, I'm pretty happy continuing to call in English, no worries.

---

<!--SEGMENT
topic: Cowork, Claude Desktop, and Local File Access Tools
speakers: Morgan Cook, Patrick Chouinard, Brandon Hancock
keywords: Cowork, Claude Code, Claude desktop client, Windsurf IDE, OpenWork, open-source, Mac-only, Windows, local file access, non-developer workflows
summary: Morgan and Patrick discuss Cowork and its alternatives for non-developer users who need local file access and modification capabilities. Patrick explains that the Claude desktop client now wraps Claude Code in a web interface accessible on any platform, and mentions open-source alternatives like OpenWork.
-->

00:08:49 - Morgan Cook
<Q>Hey, Patrick, have you had a chance to look at Cowork?</Q>

00:08:54 - Morgan Cook
<A>Yeah, well, a bit. Not a lot beyond just reordering a couple of files, but it's pretty much Claude Code [tool:Claude Code] wrapped into a couple of execution layers.</A>

00:09:09 - Paul Miller
Yeah, it's pretty impressive what it can do.

00:09:15 - Morgan Cook
The reason I ask is I have a process for somebody who is not a programmer that uses — it's not Cowork [tool:Cowork] because they're not on Mac, but it uses the same kind of concepts of being able to access local files and modify files and output to directories. So I have them in the Windsurf IDE [tool:Windsurf], but they're not a developer, right? They're just a user making use of scripts to modify files.

00:09:43 - Patrick Chouinard
You know that now with the desktop client, you have access to Claude Code in a web-ish interface. That's not the CLI.

00:09:55 - Morgan Cook
<Q>From where?</Q>

00:09:57 - Morgan Cook
<A>From the Claude desktop client. On Windows? Yeah, on any platform.</A>

00:10:06 - Patrick Chouinard
Cowork is Mac only.

00:10:21 - Patrick Chouinard
▶ If you flip from chat to code, you're going to get Claude Code just wrapped into a web interface inside of the desktop platform. And it has access to your files and everything. So you can do mostly what Cowork does in there.

00:10:36 - Patrick Chouinard
Otherwise, there's stuff like OpenWork [tool:OpenWork], which is just a rip-off copy of Cowork that does pretty much the same thing. There's a bunch of open-source versions that came out since Cowork was announced.

00:10:51 - Morgan Cook
The concept is agnostic to the environment. It has nothing to do with Claude per se. They're the ones who really identified the workflow and made it real.

---

<!--SEGMENT
topic: Cowork Demo Story and AI Productivity for Non-Technical Users
speakers: Brandon Hancock, Morgan Cook, Patrick Chouinard, elijah stambaugh
keywords: Cowork, Excel automation, Fathom, skills, Windsurf, HTML, markdown, PDF, non-technical users, workflow automation, systems thinking, vibe coding
summary: Brandon shares a story of using Cowork to solve a complex Excel matching problem for a non-technical user in minutes. Morgan describes building Claude skills to automate a document creation workflow for a client, converting markdown to styled HTML. The group debates whether non-technical users will level up to systems thinking or rely on developers to build templates for them.
-->

00:11:04 - Brandon Hancock
Quick, fun story on Cowork. I actually got off a call. Amongst my wife's friends, I'm the AI guy. So one of them was like, I'm stuck, I need help. And she had a monster Excel sheet that was connecting parts from one distributor that's no longer in business to a new company. They have to order it. They have to basically balance out across like 50 distribution centers, each part. It's like a 50 times 50 — like 50 distribution centers times 50 parts. Like, so it got very hard to match everything up. And she's been like toying at it for like a week, trying to get it to work. And I was like, please stop. Just literally give it to me and I'll do it in five minutes. And so we just hopped on a call. She described the problem, Fathom [tool:Fathom], copy the transcript, pasted it into Cowork, gave it the Excel file. And it just did it. It literally did all of it.

00:12:00 - Brandon Hancock
And she was like, well. Oh, damn. So I was like, so what are you going to do now? Like, are you going to do the rest of the work? She's like, yeah, I'm going to do that today and tomorrow, and then I'm not doing anything for the rest of the month. So like, it's just funny how the bar — people are just so used to human limits, not AI limits.

00:12:25 - Brandon Hancock
▶ Companies that aren't adjusting, they're just paying unnecessarily. So I don't know, for all you CEOs out there, I would 100% do some sort of like, watch people work. Like, hey, just show me how you're about to do this task. And if they're not doing it with AI, like, what are you doing?

00:12:47 - Brandon Hancock
So yeah, I think enterprise companies are really about to have to adapt fast.

00:13:00 - Brandon Hancock
A few other quick updates, action items for you guys. So I recorded things for Shipkit [tool:Shipkit] today. I tried to get fancy updating a RAG pipeline for you guys — was trying to tweak some stuff, so the uploading process, I tweaked, so I'm going to have to fix it right after this call. But I've recorded an updated batch. I basically cover the AI coding stack, how I think about Claude Code, the multiple different ways that I would recommend to do AI development — basic, mid, and advanced — and I just break them all down, plus some stuff with Git work trees.

00:14:00 - Brandon Hancock
The task review command and a few other new ones I've been adding — I'm basically just cutting a new version, so fingers crossed late tonight, worst case first thing in the morning for all of it.

00:16:38 - Morgan Cook
So this last week I've been using — first off, I switched completely to Claude CLI [tool:Claude CLI].

00:16:45 - Brandon Hancock
Ooh. Welcome to the dark side, buddy.

00:16:50 - Morgan Cook
And because I was running into problems with Windsurf, and I think this is a problem that we have with all of the tools — at some point they have network connectivity issues or whatever that break down. I was in the middle of something that I needed to really get accomplished, and so I went to Claude, and then I quickly ran out of my Pro limits, so then I went to Max.

00:17:17 - Brandon Hancock
Dude, you're all in. You're not just in, you're all in.

00:17:28 - Morgan Cook
▶ If any of you guys are still on the fence about trying to decide to go one way or the other, I hit the bullet and jumped in.

00:18:35 - Morgan Cook
Yeah, I was talking with Patrick a little bit before the meeting started about the concept of what Cowork has brought to the table. I have somebody who was manually creating worksheets in Word and trying to make them look nice and everything and I'm like, what are you doing? Same kind of process. So I said, look, just stop for a minute, let me throw it together. I don't have Cowork, I'm on Windows, but what I did do was use skills. So I just created a couple of skills to do the major steps that she needed to have done. It takes a markdown output from whatever research she does on chat and creates an HTML page out of that markdown and then applies a very nice stylesheet, which I have a couple that I've created for different styles. And then after that she's just manually printing from the HTML to the PDF. Also, the script generates a meta.json so that she can just copy and paste the JSON into the products page that she's posting these things on.

00:20:10 - Morgan Cook
▶ So it took like what she was spending days on and chunked it down into less than 10 minutes.

00:20:19 - Morgan Cook
And now she has a whole structure that is local. It's not being done on the web anymore. It's now local to her machine.

00:20:38 - Brandon Hancock
<Q>So what do you guys think is going to happen going forward? That is a perfect example, Morgan. Do you think people who are non-AI users are going to start skilling up to learn how to think at a systems level, how to break things down into steps and use AI to then help with their work? Or do you think that's not going to happen and it's still going to be like developers or systems-level thinking people providing the templates for the others to use?</Q>

00:21:31 - Patrick Chouinard
<A>Well, basically, my thinking is whoever still has a job after AI took its place is going to be people who are doing exactly that. This is the future world where you instruct, you templatize, and you have to think about the system, not about individual tasks. Because there's always going to be people who do individual tasks for sure, but they're going to be users of the material that the others are creating. So who's going to make money? Most probably the guys that define the template that the others use.</A>

00:22:09 - Morgan Cook
I think for me, this client was more or less just unaware. Now that she has the tools and understands what the tools are and how to modify them — I said, don't edit the files directly. Tell AI to do what you want it to do. And then tell it to remember that and put it as part of the skill. So it becomes a cyclical thing that they have to learn how to work with AI in that feedback loop.

00:23:00 - Morgan Cook
▶ Your question whether people are going to level up or whether AI has to come down — I think people have to level up. It's a knowledge thing. When your car breaks down, if you're not a mechanic, you've got to take it to the mechanic because the mechanic is the one with the knowledge. And that's the same thing with vibe coding — you can make things look pretty at first, but then when something breaks, you're stuck.

00:23:44 - Brandon Hancock
I also just want to go back to what Patrick's saying. I really do see a future to where you have system creators and system managers. You don't have task doers anymore. So I think everyone shifts up one.

00:24:26 - Patrick Chouinard
No, you would need few system creators today with what we are able to do today. It's always what that new technology, what that new framework, what that new method of working will enable — it's going to enable things that are not doable today, or that are not profitable today. When you get into a world where everyone is a creator, it enables new framework or new work items that you would not have done today. So it's an economy of scale. The easier you make it, the more people will create.

00:25:13 - Patrick Chouinard
▶ I don't think there's going to be a shortage of jobs, because I know I've automated a part of my job that used to be my entire work, and I've never had more work than now.

00:26:17 - elijah stambaugh
Two different things. One is that one of my clients made a goal to automate one hour a week. So he's got his team thinking about, what can we do for one hour a week? And then by the end of the year, obviously he'll automate 50 hours — a full-time position.

00:26:52 - elijah stambaugh
The other thing is, I think the real constraint is not the — there's a developmentally appropriate time to learn certain things. In the state of Ohio, they talked about doing a computer science course for one semester during high school. And the bill is proposed to start that in 2035.

00:27:25 - elijah stambaugh
So like they're saying in 2035, you should have at least one semester of computer science in high school. And we're all shaking our heads because in the next 48 hours, I could learn what would take me a whole semester. My one friend said, how is new technology adopted? One death at a time.

---

<!--SEGMENT
topic: Claude Code Mobile Workflow and Git Branch Management
speakers: Brandon Hancock, Hemal Shah, Alex Wilson
keywords: Claude Code, GitHub, Git branches, work trees, mobile workflow, voice input, task template, Calendly, sales page, parallel development, Shipkit
summary: Brandon demonstrates his workflow of using Claude Code on mobile while at the gym to kick off development tasks via voice, connected to a GitHub repository. He explains how tasks are created using a task template, committed to new branches, and then reviewed and merged when back at the desktop. He also covers using Git work trees to run multiple features in parallel.
-->

00:28:43 - Hemal Shah
Hello. So like Morgan, I'm also coming to the dark side. I canceled my subscription and finally going for Claude. So yeah, looking forward to it. I'll go to the videos that you just mentioned — skills. I think Anthropic [tool:Anthropic] is doing amazing advancement, the whole hardness thing — long-running agents — and every now and then they will come up with something interesting. I plan to go full all-in in Claude and Anthropic ecosystem.

00:29:16 - Hemal Shah
<Q>One question I have is — in the last call, you and Patrick both mentioned that while you are not in front of the computer, you are talking to Claude about your ideas, whether you're at the gym and all that. So if, let's say it's about some of your projects, do you upload that project document first to Claude, and then how do you go about that?</Q>

00:29:37 - Brandon Hancock
<A>Yeah, let me show you real fast. So the way it works is in Claude — this is literally the Claude application. What you do is you just connect it to the default Git repository that you have access to. At that point going forward, every time you start to work on something, it'll make a new branch. I always ask it to make a new branch. I think it does by default, but I always explicitly state make a new branch because I don't want it to ever accidentally do something on main.</A>

00:30:33 - Brandon Hancock
So like, I'm literally on the cycle at the gym. I was basically just like, hey, we want to update our sales page so that after someone books a Calendly [tool:Calendly] link, instead of just showing a Calendly page, hey, we have the opportunity to take them back to our website, show all the stuff. So I'm just literally there talking, and then I say, hey, please create a new task for this using template.md. And that's it. At that point, it did all of this.

00:31:39 - Brandon Hancock
▶ And I did six PRs — created six new features — to kick them off while on the cycle. So it's just like, I love listening to business podcasts, and as the idea comes up, I open up Claude Code and I just blurt it out right then and there. And then whenever I get home, I just have to finish up the task.

00:32:18 - Brandon Hancock
▶ It prevents that I have an idea and then forget it 24 hours later. No, let's go and get it started, get it 60–80% done. So then when you are back at your computer, you're just like, hey, what branches are not done? Cool, let me just take them to the finish line.

00:33:22 - Hemal Shah
<Q>So just to recap — your Claude Code is connected to your GitHub or Git repository, and that's how it will — all the interactions, everything is stored there in the Git itself?</Q>

00:33:28 - Brandon Hancock
<A>Yes, yeah. And it's literally all you do — when you open up Claude on your phone, it says "code." So you go to Claude, and then it says sessions or code in the left, and then you just click it, and then you just talk. And do the exact same thing you would normally do if you were in Claude Code, where you would say make a task for this using task template, which then forces it to go through the whole breaking it down and everything, because you don't have planning mode. That's the problem. So that's why we force it to go into the task template.</A>

00:34:11 - Brandon Hancock
My main project that I'm working on is only one, just so I don't end up in any weird spots.

00:34:38 - Brandon Hancock
<Q>Alex, I saw you said you had a question about it, buddy. Do you want me to clear anything up?</Q>

00:34:24 - Alex Wilson
<A>Not really a question. I just wanted to know — I'd love to see a video to see that workflow in action. I don't know how to do the GitHub review later, that portion of it.</A>

00:34:38 - Brandon Hancock
Yeah, I can definitely add that as a video. The good news is it's so simple. It's literally like, hey Claude, yesterday I worked on some new features. Can you tell me what branches are available? And it's going to say, oh yeah, of course. And then it's just going to show you the name of the branch.

00:35:54 - Brandon Hancock
So I updated the landing page on how it works. Each one of these has its own branch. So like I had the sales confirmation video — whenever I get back home, I just say like, okay, cool, check out this branch, and I'd like to start working on it, and then you just start working on it, and then merge it in.

00:36:40 - Brandon Hancock
▶ And if you guys want to get double fancy — because Claude makes each one of these on its own branch — what I did today and yesterday is I made a new work tree for each one of those branches, so all six ideas I had at the gym, I made a new work tree for each branch, so when I got home, I was knocking out all six tasks in parallel.

00:37:00 - Brandon Hancock
I have an updated video on that in the advanced development workflow. That's how I was able to tackle six features over a day and a half, basically, in parallel. So really recommend it. Start simple, just do one, but then when you're feeling frisky, try six in parallel with the work trees.

---

<!--SEGMENT
topic: Voice Agents for Lead Qualification and Scheduling
speakers: Hemal Shah, Brandon Hancock
keywords: voice agents, Bland AI, N8N, Calendly, Google Calendar, lead qualification, no-code, tool calls, appointment scheduling, Vapi, Retell
summary: Hemal asks for recommendations on voice agent tools to automatically call incoming leads, qualify them, and schedule calendar meetings. Brandon recommends Bland AI as the easiest no-code option, describing its N8N-like flow builder with Google Calendar integration for appointment booking.
-->

00:37:23 - Hemal Shah
<Q>One more question — voice agents. I'm looking into a voice agent option where, you know, whenever some lead comes in, it will initiate a call, talk to a customer, maybe starting to set up a scheduled calendar meeting invite through voice. So any recommendation, any tool?</Q>

00:38:00 - Brandon Hancock
<A>The one that comes to my mind is Bland [tool:Bland AI] and setting that up. But basically you just set up a loop to where a call comes in and then it's like you're trying to collect three pieces of information — their name, what they want to talk about, and then schedule a time. So that's the whole workflow, and then you have a general knowledge base. So if someone asks a question outside of that pre-built workflow, it can answer it. And Bland makes that pretty easy to set up, and it's pretty affordable.</A>

00:38:50 - Brandon Hancock
▶ Bland is the easiest no-code option. You literally just — it feels like N8N [tool:N8N], but with voice. And you can hook it up to Google Calendar [tool:Google Calendar] to set up your actual appointment availability. So like, I want to take appointments from nine to five, and I want a buffer on each side of an hour. And then there's the tool calls to your calendar. So pretty straightforward to set up.

---

<!--SEGMENT
topic: Project Management Challenges and Landing Page Development
speakers: Juan Torres, Brandon Hancock
keywords: ETL process, general ledger, front-end engineering, project management, landing page, work trees, Gemini, Vercel AI SDK, Shipkit, agentic coding
summary: Juan discusses challenges integrating multiple engineers on an ETL project due to poor initial project management. Brandon suggests using work trees to generate multiple landing page design variations in parallel using different AI models, and encourages Juan to join Shipkit to improve his agentic coding workflow.
-->

00:39:18 - Brandon Hancock
All right, I think next up, going back to the call order, was Juan. What's cooking, man?

00:39:25 - Juan Torres
Hey, nothing much. Just integrating someone else for a project. For the same project we're integrating another front-end engineer. The last one, there was an issue with the front-end engineer, Natalie, being able to use the back-end engineer for the canonical aspect of the ETL process of changing some general ledgers.

00:40:15 - Brandon Hancock
Oh, engineering drama, man.

00:40:21 - Juan Torres
It's not even drama, it's just like, I don't think there was good project management from the beginning. And so now the stakeholder is paying dearly for his sins against the gods of coding.

00:41:19 - Juan Torres
I was going to share my landing page, but it has some issues. I'll share with you maybe on the next one, but I'm trying to grow more professional in my attire.

00:41:41 - Brandon Hancock
Whenever I was building out ours, what I would do is — once again, going back to work trees — if you don't mind burning through tokens, I would literally make five new work trees. Two of them, I would be very like, hey, make it professional. Two other ones, I'd say make it creative. And then the fifth, throw it over to Gemini [tool:Gemini] and give them the same prompt with a few minor tweaks and just build out five versions of each section. And then you're like, holy crap, I don't even need to be creative at this point. I just pick which one I like and it takes five minutes to spin up five new instances of it. Then use whatever one you like and you just merge back into main and delete the other four.

00:42:30 - Juan Torres
Yeah, I definitely need to join the Shipkit community because I am not optimized in my agentic coding as much as I should. I've been wanting to increase my agentic slash vibe coding capacity because I'm using a lot of the old modes still.

00:43:01 - Brandon Hancock
▶ Yeah, I mean, it genuinely is — the second you start to get traction and you're like, holy crap, I'm building faster than I ever thought possible, it's addicting. By noon, you're like, dang, I did a week's worth of work.

00:43:22 - Brandon Hancock
Um, I just raised the price, but I can put it back to the older one for you. So if you just want to email me, I'll put it back to the price.

---

<!--SEGMENT
topic: Call Coach AI SaaS Development and Go-to-Market Strategy
speakers: Scott Rippey, Brandon Hancock
keywords: Call Coach AI, sales frameworks, LRP, SARB, multi-user SaaS, framework picker, user profile, videographers, niche marketing, LinkedIn, organic marketing, close rate, testimonials, go-to-market
summary: Scott presents updates to his Call Coach AI tool, including multi-user support, a manual override button, user profiles, and a planned dynamic framework picker to replace hardcoded sales frameworks. Brandon and Scott discuss go-to-market strategies including niching down to videographers/photographers, organic YouTube content, and leveraging Scott's existing network to drive testimonials tied to measurable sales outcomes.
-->

00:43:51 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I've been doing a lot of work on the Call Coach AI [tool:Call Coach AI]. I think I showed you that last week. We talked about the MVP, which is fully functional. I want to keep adding features, because I'm probably not going to SaaS it out there completely, but it'll be more of like a company SaaS kind of a thing. But I'm making it more and more so that I don't have to customize it that much — meaning it's going to be very adaptable. So I already made it multi-user, I have a couple of friends in there testing. Added a manual button — you can choose to not have it automatically suggest things on the call and just hit it when you want it. Or you can still override it and hit it manually if you really want to analyze something in the moment. Added a user profile for you, so you can actually upload stuff about you that you don't have to keep uploading every time, so it knows you, your offers, your positions, and everything like that.

00:45:03 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
The next step is going to be, I'm actually going to make a framework picker. Instead of having those two frameworks baked in, I'm going to have it be dynamic, where I'm going to make all these different frameworks for all these different sales and other things. So literally I'll have, you could just pick what it is or which ones you want before you start the call. Instead of, right now I've got the LRP — listen, repeat, poke — and then the SARB sales thing are just baked in there. I want to make it more dynamic because then it's just less work for me whenever I resell it.

00:45:32 - Brandon Hancock
▶ What I love about that is when you're using the terminology, you're using the jargon that they're already doing and that they would manually have to do to use your system how they would like. So it's like, why not just — the cool journey that I think you're on, which is what all AI SaaS development is — just eliminate friction. What is my end user trying to do and how can I make that frictionless?

00:46:09 - Brandon Hancock
One thing I really always like to do, Scott, is just look at the customer journey from like, what were they doing an hour before the call? What are they doing during the call? And what do they normally do after? And then I try to figure out how I can make sure the software helps be as seamless as possible with all of that.

00:47:14 - Brandon Hancock
<Q>What are other competitors doing in the space? And then, okay, what's our go-to-market strategy? Is it going to be grassroots, find salesmen who have their own independent business? Or do we go upstream and find big companies that then want to take it on?</Q>

00:47:54 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
That's one of the things I want to kind of figure out. I tend to work on apps that are useful to me because I know it'll be useful for somebody else. But then I still have to have other people test it.

00:48:53 - Brandon Hancock
The other option is to niche down and to be the sales AI tool for all videographers and photographers. That's still a stupid big market. They're constantly on calls doing things for weddings, for business. That could literally be the best way to do it.

00:49:34 - Brandon Hancock
▶ And the other part, too, that you could do with organic marketing, is starting to just give away all the trade secrets on a YouTube channel, and then whenever I get the customer on the call, I always use this software to help make sure I do everything that you just learned. That's always an approach, too, because you have more knowledge on that than anyone else who's going to build a sales tool. That is your true unfair advantage.

00:50:22 - Brandon Hancock
▶ You're tied to the money because of the sale — if it goes through, they make more money. You get to ask them beforehand, what's your close rate? If it's 30%, fantastic. They go to 50%, like that's a huge difference for them. And that just writes itself for testimonials. "I'm working with Scott and he made me an additional $100,000 last year."

---

<!--SEGMENT
topic: NeuralSpark RAG Pipeline with Cross-Encoder Re-Ranking and Recursive LLM
speakers: Scott Rippey, Brandon Hancock
keywords: NeuralSpark, RAG pipeline, vector embeddings, cross-encoder re-ranking, Cohere, recursive LLM, context rot, Claude tools, OpenAI embeddings, Sonnet, Haiku, Google API, knowledge base, context window
summary: Scott presents a three-layer RAG architecture he built for NeuralSpark: layer one is standard vector embeddings (OpenAI), layer two is cross-encoder re-ranking using Cohere to improve retrieval precision, and layer three is a recursive LLM (RLM) approach where the model actively hunts for information via tool calls rather than receiving a large context dump. He plans to extend this to a Google API wrapper and discusses model selection trade-offs between Sonnet and Haiku.
-->

00:50:54 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So back to NeuralSpark [tool:NeuralSpark]. So this is actually huge, and it's going to apply to way more than just NeuralSpark. So the reason I'm talking about NeuralSpark right now is because, you know, it started as the knowledge base — so I just had these simple embeddings, the vector, the chunking with some overlap, just the basics. And it was kind of a layer one thing for when you're searching through your knowledge base. I've only got like under 20 documents in there. But this is an app that I'm putting several people on, so that this one's going to be an easy reseller.

00:51:37 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
But I was like, you know what, even with vector embeddings, if anybody gets on this thing and they really start hammering data into there, the results are going to start getting worse — context rot. So I added this layer two of cross-encoder re-ranking [tool:Cohere]. I'm using Cohere, which is a really cool thing — it reads the query and the document together, returns the top 50, the re-ranking score. That helps a little bit. So that's layer two.

00:52:09 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
And then layer three — now it's like a funnel, right? I'm funneling it down to get more accurate. But the true thing for context rot, because I don't want to shove 50 full documents down the pipe, is the recursive language model. And I don't know if I talked about that here. This is freaking nuts. And I found this paper on it that came out in like December. They were testing with GPT models where they could get GPT mini to outperform by two times in accuracy.

00:52:52 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
And the concept basically — it's like a wrapper on a language model. What it does is — so I recreated this using the Claude tools because Claude literally has tools that are made for this. I don't need to do a sandbox with Python and all that stuff. So you don't send all your data. You send basically — Claude receives a query, plus some chunk metadata, not full content. And so everything is still on my side. You actually have the LLM decide what to explore via tool calls. It's like reversing the process. It's going to hunt for the information. So it can peek and grab chunks, get details, summarize, search more. It can loop — literally it's like, to get a synthesized answer, it's a way to make it smarter and not have context rot.

00:53:43 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So that's my layer three on this search. It's working. I'm working on the logs right now because I want to track how it's working and have some metrics in there.

00:53:56 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
And I even set a max amount of loops. It doesn't slow it down too much. My voice conversational agent that talks to my knowledge base — it only adds like two or three seconds to it, which is still fine for that, because it's just thinking.

00:54:29 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Then I thought — wait, this wasn't even made for RAG. I was just like, this would be great as a third layer or second layer or anything. So I'm going to add this into the Google side and create a second tool that gets called for all the Google API stuff, so that it can start searching and calling and getting stuff from Google to give me better results on that AI assistant tab. So I'm going to have a Google wrapper for RLM, and I'll have the knowledge base — my own database knowledge. I'll have these two tools that can get called. And the one can call the other because Google can actually check my knowledge base for meetings and stuff.

00:55:12 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I really want to get some data on this thing, because I actually have it to where I can turn RLM on or off in the app.

00:55:22 - Brandon Hancock
▶ Did — I'm pumped. I'd love if you have, next week, I'd love to see a demo of it on and off, just for some hard questions, just to see how fast it is too.

00:57:05 - Brandon Hancock
<Q>Please let me know what models you end up picking. I'm guessing GPT-4 Flash or 4.1, but I'd be curious when you use them, what models you're picking.</Q>

00:57:18 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
<A>I think I'm using Sonnet [tool:Claude Sonnet] on the Google side, like because it's got to be smart. So I'm not using super quick models. I'm using models where it's still fast, but because it needs to synthesize and be smart, although I can turn it to Haiku [tool:Claude Haiku] for certain things. So it does use OpenAI's [tool:OpenAI] actual embeddings model for searching. I think I'm also using Sonnet for this part and I'm going to test it. I'll probably test between the two to see the results, but I want it smart. For the knowledge base strict RAG searching, I might be able to use a lower model, but for the Google side, I'm probably going to stick with Sonnet, just because I'm asking it to look up calendars and tasks and all kinds of more complicated stuff.</A>

00:58:20 - Brandon Hancock
▶ On the model size, depending on what — if you do use Haiku and stuff, a lot of the times those models have a limited context window. So just know those have like a 200K cap through the API.

00:59:00 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
The whole point is it should be less tokens — there should never be one large shove down the pipe when you use an RLM because it's continually going back and forth and figuring it out.

00:59:11 - Brandon Hancock
Yeah, no, please keep me posted. I have not used any RLM stuff yet, but if you're noticing a huge difference, please let me know.

---

<!--SEGMENT
topic: Patrick's AI News Aggregator and NotebookLM Training Pipeline
speakers: Patrick Chouinard, Brandon Hancock, Juan Torres, elijah stambaugh, Paul Miller
keywords: Claude Code, NotebookLM, knowledge artifacts, PRD, markdown, skills, RAG, training documentation, Notebook LM, ChatGPT, YAML, podcast generation, bilingual content, Jack Butcher, Build Once Sell Twice, LinkedIn lead magnet, Shipkit, sub-agents
summary: Patrick presents a system he built using Claude Code to aggregate AI platform news, where each of 22 development conversations automatically generates a structured markdown knowledge artifact. These artifacts are loaded into NotebookLM to create a full interactive course with podcast audio, slides, and a RAG chatbot. The group discusses the broader implications for content creation, monetization via LinkedIn, and the "Build Once, Sell Twice" framework by Jack Butcher.
-->

01:00:02 - Brandon Hancock
Next up is Patrick. What's up, buddy?

01:00:07 - Patrick Chouinard
Yeah, I actually don't think to talk to Claude Code. I talk to ChatGPT [tool:ChatGPT], but same principle.

01:00:16 - Patrick Chouinard
No, what I wanted to tell you guys this week is — I come here every week, I share, but I don't ask a whole lot of questions. But I still wanted to thank everyone here because what I said in the beginning was that I was coming here to get ideas, use cases. And I think this week I fell into one of the use cases that was the hardest because I'm asked to prepare training, training, training, training. And generating training at the speed of AI is pretty hard right now.

01:00:55 - Patrick Chouinard
And you, Brandon, specifically, every week are on my case to publish. Publish stuff on LinkedIn. Publish stuff on YouTube. And my thinking was, yeah, I'd love to do that, but when?

01:01:07 - Patrick Chouinard
Well, last week, I was asked to build a tool to do the gathering of news on all the AI platforms because, again, it goes too fast. So I decided to build this with Claude Code. So Claude Code being the engine that will do the actual searching and managing the information. And I decided, you know what? Everybody wants to know how I do those things. And just recording it's not going to work. I decided that I'd build this skill that would condense the content of a conversation with Claude into an artifact that would highlight all the patterns that I've used from the conversation. Basically, create a knowledge artifact out of each and every single conversation.

01:02:10 - Patrick Chouinard
The entire build of the application took 22 conversations, and some of them are long. This is the whole thing — the design. I started with the PRD that I discussed with ChatGPT, but from the PRD, ingesting it into a project, finding how to split into a feature, how to revise the feature, make sure they're consistent, all of that, then start implementing. It took 22 conversations. It generated 22 markdown artifacts.

01:02:49 - Patrick Chouinard
Then I took those 22 markdown files, loaded them into NotebookLM [tool:NotebookLM], and now I've created all the training on — if you want to know how I did that, go look at that NotebookLM notebook. You have a podcast talking about it, you have video describing it, you have slides explaining it. So now I've — this version is really a rough version one, but now what I discuss with ChatGPT again to figure out is how to have specific prompts to process the creation of those artifacts, so they're consistent across courses. And even have it create one video that would be basically the showcase of what's in it. So just to explain, oh, this course includes this information, and that's what I would publish to YouTube with a link to the full NotebookLM.

01:03:52 - Patrick Chouinard
▶ So basically you have a bundle of intelligence that you can ask any question you want. So no matter where you're coming from, if you're interested in this, you can get the information tied to you and how you want to use it. So I can save that and provide it to my employer but also provide it in a YouTube channel without taking any more time because it's basically created from the work I do anyway. I just have to at the end of every conversation execute one skill.

01:04:26 - Brandon Hancock
This is crazy. So from my understanding — I guess I have to — there's multiple end users of this. Like a thing was made, but as we were building this, we were building this way, so that anyone else in the future can learn how to do the same, correct?

01:04:49 - Brandon Hancock
Yeah. So could you walk me through what both end users get of this process? So end user one is a student — do they basically have access to a full-blown course?

01:05:08 - Patrick Chouinard
It's basically — let me share, it's going to be easier if I share. This is the NotebookLM implementation. That's the notebook itself. Here is all of the steps that I took. So people coming in here can do one or two things. They can actually look at the extract, because this is not written in a cryptic way. It's easy to follow. Everything is readable and it's clear information on how I did this step. And this is all because of the prompt I use in the skill to extract that information from the conversation. And honestly, that works with a conversation with AI, but it would work just as well with a conversation between two humans. AI doesn't even need to be involved in the creation of those artifacts.

01:06:26 - Patrick Chouinard
Then they have access to the chatbot. So it's a RAG system. So they can ask any question they have about the content or for the content to be presented in any form that talks to them as a student. And then there's the artifacts. So they can listen to the content. They can view slides about the content. And they even have — and I've done them bilingual, so they're in French and English — graphics about everything that was done. So you need to do the PRD, hierarchical construction, atomic task definition — you're going to see a lot of things that resemble the concept of Shipkit in there because it's highly influenced by it.

01:07:22 - Brandon Hancock
<Q>So you went through the process of 22 conversations. At the end of item one — you're going through the process of planning and architecting — what exactly is happening?</Q>

01:07:43 - Patrick Chouinard
<A>Extracting a tech stack from a PRD. The PRD is the product requirement — it's the starting point. But here it's really: you have requirements, you give it to Claude Code, and then you interact with Claude Code to extract the tech stack. Once you have your tech stack, you refeed those two into Claude Code, and then you ask it to construct a roadmap. Then you decompose the roadmap into a list of features. Then you decompose the feature into a list of tasks. Then you verify that they are ordered properly. Then you verify that you have not contradicted yourself between everything. And you just validate the content. At the end of the documentation, you start implementing. It took about 10 conversations to do the design, and the last 10 or 12 conversations are just: implement this feature, now implement this feature, now implement this feature. And every loop is: here's the context, here's what I want you to do, then we're validating together, then you're going to recheck what you've done, then you're going to commit, do your PR, go on to the next one.</A>

01:09:22 - Brandon Hancock
Okay, and then final thing — so what is the person actually reading in this source? What value would a random developer get from this artifact?

01:09:47 - Patrick Chouinard
That's the last piece I need to add — I need to add a note in here, which I define as the onboarding. How do you use this? This one, I haven't done it yet. Like I said, it's a very rough version one, but the idea is to have an onboarding node that tells you, here's the content you're going to see in here, here's how you can use it, here's how you can use the artifact that I've already created, and if you have questions of that type, ask it to the chatbot.

01:10:30 - Patrick Chouinard
▶ But to me, this is — every time I do something from now on, I'm going to document it using the skill I told you about, and structure it into a notebook like that. So I'm going to have examples of everything that I've created or built.

01:10:45 - Brandon Hancock
This is genius. I love this.

01:10:48 - Juan Torres
<Q>Is this going to be available for the public?</Q>

01:10:53 - Patrick Chouinard
<A>Oh, yeah, absolutely. Actually, let me just post in the chat.</A>

01:11:23 - Patrick Chouinard
But yeah, the idea is eventually have Claude Code communicate with NotebookLM and do that whole pipeline automatically.

01:11:36 - Patrick Chouinard
▶ But yeah, I think what I find amazing here is the skill to compress a discussion into an artifact that always shows the same thing about what happened in the discussion. It really saved me a whole lot of time constructing this, and it becomes basically background work. So constructing this — once I have finished automating all of the little steps, especially having all the specialized prompts that are constrained to create the artifacts — I'm going to be able to spend maybe an hour more on every project and have full documentation and training material.

01:12:21 - Brandon Hancock
<Q>So I — Noob at NotebookLM — for these artifacts right here, were they created automatically, or did you manually use something to create those?</Q>

01:12:35 - Patrick Chouinard
<A>I created those. I need to automate their creation. But the shared notebook — first of all, people cannot modify it. Obviously that's the goal of a shared notebook. But yeah, the creation of the artifact is what I've done manually and what I'm going to look at — what Paul sent — to see how I can get Claude Code to automate.</A>

01:13:22 - Brandon Hancock
So, Patrick, I want to share a few things on this. There is a course called Build Once, Sell Twice [link:Gumroad - Jack Butcher], one of the most frame-breaking courses I've ever bought — like 50 bucks. But what it talks about is you, as a creative, go through the process, at the end you achieve a result, you make a painting, you write code, you make food. And what people always want to do is say, well, how did you do that? So you built it once — to the end consumer, you give them the application. But then people also want to know how did you do that.

01:14:00 - Brandon Hancock
▶ What I absolutely love about this is that entire back half of "how did you do that" is there — there is now a system wrapped around that process to make sure as I'm coding, with this much additional work, I get this much additional output.

01:14:46 - Brandon Hancock
Oh yeah, Jack Butcher [tool:Jack Butcher]. Jack Butcher is like the predecessor to Dan Coe. So if you like Dan Coe, you'll love Jack Butcher. He's the one who created the concept of Visualize Value, which is what all things that you see from Dan Coe are always coming from.

01:15:32 - Brandon Hancock
▶ So seriously, Patrick, what you're doing — you're setting yourself up to, as you go off and do more things on the software development lifecycle, become known as an expert in this field. I think just having this repertoire of how to monetize it — you've way more than needed, you know, and you're already crushing it.

01:23:42 - Brandon Hancock
▶ Seriously, on LinkedIn, please give this away as a lead magnet — free, not free, whatever you want to do. And just say "post below to get access" to insert a very cool word. And in the post, just describe all the value they're about to get. Dude, you will see what this one post easily gets — like six figures of impressions, if done right. And the amount of opportunities that come out of that, unreal.

01:24:47 - Brandon Hancock
Final thing, Patrick, just to peel back the curtain really fast — a very cool deal came across the table like a week ago. A huge big company, everyone would know them if I said them. Basically saying, hey, help us do Shipkit inside of our company. And the reason I say this is because I want you to do this — it's like a six-figure deal for a month or two months of work. You do that six times a year, dude, that's stupid money. Every company on earth that has a software factory needs you. So that's how I'm phrasing it. Please what you're talking about — yell it. I mean, don't stop yelling until deals start — companies saying, shut up, here's $100K, here's $200K, please just coach my guys for two months to help them just even get close to where you are. Because you help 30 developers in a team all become 50–100% more productive, the company is going to say $200K was a steal — you just generated us a million.

---

<!--SEGMENT
topic: Enterprise AI Adoption, IT Compliance, and Secure Deployment
speakers: Paul Miller, Brandon Hancock, Patrick Chouinard
keywords: enterprise AI, IT departments, SOC 2, HIPAA, AWS, Google Cloud, Terraform, Claude Code, DeepSeek, data security, Ernst & Young, ring-fenced environment, ChatGPT wrapper, Microsoft Access migration, intern productivity
summary: Paul discusses his CTO's agreement to use agentic AI for all new standalone projects, and raises the challenge of onboarding a university intern who lacks the background to effectively use AI tools. He also identifies a market opportunity in migrating legacy Microsoft Access databases to modern apps. Brandon counters with a larger opportunity: helping IT departments deploy secure, ring-fenced AI environments so employees can use full-featured tools instead of limited internal ChatGPT wrappers, citing compliance frameworks and the fact that most data leaks are internal.
-->

01:28:10 - Brandon Hancock
Paul, you are up next. Last time, we had some spicy updates, dude. Where is the journey of Paul?

01:28:19 - Paul Miller
Well, thanks for putting me after Patrick's session.

01:28:39 - Paul Miller
No, I'm a little bit more down to earth this week. I needed to do my follow-up with my CTO. Look, to give him credit — and I think it's important to put context back in the scenario — we are an existing software company, we've got thousands of end users made up with a number of big companies who employ those end users. We can't immediately jump our whole code set into the modern agentic approach, but I have got agreement that all the new projects that we're doing, where we can stand them alone and plug them into our framework, that is going to be the approach going forward.

01:29:42 - Paul Miller
Now, I've had an interesting sort of run. We talked — well, Brandon, you've talked a lot about what do you tell young people now? Our kid is 19. They're very anti-AI — oh, AI should be banned and stopped and all this kind of thing. And I hear that a lot from younger people in university at the moment.

01:30:31 - Paul Miller
So we decided that we'd take on an intern over our summer. And we're sort of at the end of the internship now. And a lot of the time I challenge this young woman to sort of tell her to look at using AI to do stuff. She doesn't have the same view as our kid. She's a lot more into using AI, but I think the biggest challenge that I'm seeing with kids out of uni at the moment is that they just don't have the background of the questions to ask. They know they can use AI, but they don't know what to ask.

01:31:32 - Paul Miller
I remember when I went to university, there were many papers and lectures I found incredibly boring. I would love to be able to record it with Fathom [tool:Fathom] or whatever and get it to summarize it in a much better format that's going to make me think about those subject materials. And have you ever thought about that? And it's like, oh, no, that's a good idea. I'm thinking, why aren't you guys using all of this?

01:32:12 - Paul Miller
I think the amount of time I've had to spend to try and get an intern to think the right way versus the time it took to use AI to improve the productivity of our team — I don't know if I'd do it again. And it's a real worry, a real worry for the future.

01:32:53 - Paul Miller
Another area — and this is kind of a bit of a blast from the past — I was catching up with a friend of mine, an IT guy looking for IT work. And this shows my age, but it does highlight a really typical problem. How many small businesses have a critical process running in Microsoft Access [tool:Microsoft Access], that you could take Access, de-analyse it in terms of looking at all the forms — and the problem with Microsoft Access is a lot of the process and the nuance of the application is embedded within the same file. One of the founders of the business set up some Access database 20 years ago and that's their practice management system. They've got to keep maintaining Access to keep it going. And just getting into one or two of those and doing a little project of converting that into a modern app — there's not many people advertising this. I think it could be a good opportunity for those guys that are looking for projects.

01:34:44 - Brandon Hancock
Can I actually give you a counter idea for them? I think this same use case I'm about to say applies across all medium to large scale businesses. When I was on the call with my wife's friend today, she was showing me — I was like, hey, can you use ChatGPT, Claude Code, can you use any of that stuff? No. They have their own internal thing that's like a smaller version of ChatGPT that's approved inside the organization. So like the thing I did, we literally had to go around their entire system. No data in there was even remotely sensitive. It was just part numbers that mean nothing to the outside world. But she literally has access to only what I would call ChatGPT Mini. It didn't have agent mode. It literally was a chat app that you could pick nano or regular or whatever.

01:36:00 - Brandon Hancock
▶ I think the bigger opportunity is for anyone who's IT-focused — because this is an actual IT problem — they don't do it because they're scared. They're like, oh my gosh, our data. And like, bro, if your company is going bankrupt, who cares about your data? I think the bigger opportunity is to say, AI is changing faster than you can imagine. Here's a case study of employees with and without AI, and the limiting factor, the hard truth to face — it's you. It's you're not allowing your employees to use all the amazing tools that they could to get their work done faster, which would infinitely reduce costs.

01:36:53 - Brandon Hancock
▶ The fact that these IT departments are not just being blasted off the map and replaced with a team of two guys who know the compliance rules, can set up the servers and just let them rip — if I was a CEO, I'd be having an aneurysm right now at any of these companies.

01:37:10 - Brandon Hancock
▶ Understand all the compliance rules — SOC 2, HIPAA, whatever — understand the backend security rules, how to set up a secure cloud environment for that local company. At the end of the day, you're probably going to use AWS [tool:AWS] or Google Cloud [tool:Google Cloud]. At the end of the day, it's just going to be a bunch of Terraform [tool:Terraform] code to spin it all up. And then a web app or two. And just copy and paste that for an infinite number of companies across America that have IT processes that are handicapping them.

01:38:06 - Paul Miller
Depending on which cloud vendor the IT department was happy with — and I always like using Amazon as a good example, because when you sort of say, look, Amazon does all the world's leading banks, Amazon does the CIA, Amazon does all sorts of very high-profile customers — you can set up a sub-Amazon Cloud with Claude running in there in a completely ring-fenced environment, and build a little automated pre-deployment tool that deploys a Claude Code instance using Amazon's engine, and it doesn't even go out.

01:39:00 - Paul Miller
And I used to work for Ernst & Young for a number of years, and one of the key statistics for Ernst & Young around IT audits was the biggest risk from a risk perspective for companies with company data is that 80% of all leaks occur because of staff. It's internal staff that's the risk. It's not the AI. If you're worried about that, then let's get real about where the real risk is, and then let's focus on a solution that's best practice, that some of the biggest, most secure companies in the world follow that methodology to protect their data.

01:41:00 - Brandon Hancock
▶ The hard truth is your employees are using it, it's just they're not using it how you want them to. Because now they're going to go over to DeepSeek [tool:DeepSeek] that they just found as a subscription, and they're like, oh hey, China, here's all the internal documents for our organization, thank you for offering DeepSeek for free. So you're forcing bad incentives.

01:42:38 - Paul Miller
<Q>Just on, if I wanted just to enhance Shipkit for my different apps — am I better off just adding a few additional skills onto a basic vanilla chat?</Q>

01:43:00 - Brandon Hancock
<A>If you could share a little bit more of what you're thinking of, I'll tell you exactly what I would do. I've got multiple apps, but the first is one where I want to do aggregated reporting — it takes a whole lot of Postgres data, summarizes it, and then I'll probably apply agentic AI to firstly categorize all the base data and then look at building some kind of pseudo-RAG hybrid.</A>

01:44:00 - Brandon Hancock
<A>So here's what I mean. The RAG application does a great job of showcasing basically information injection into a prompt, because at the end of the day, what you're trying to do — just dump a bunch of database rows into a prompt — is the same thing that RAG is doing because RAG is just doing a vector search, you get data and then dump it in the prompt. At the end of the day, it's the same concept. I'm getting data from a database and I'm putting it into a chat model. That's literally all that's happening. So the chat application is totally great for that.</A>

01:45:15 - Brandon Hancock
▶ What you can also do — I don't know how many different databases, how much data you're trying to ingest — but here is what level two could look like. You could have in parallel three different — basically it's called generate text. Vercel AI SDK [tool:Vercel AI SDK], just generate text. Don't stream text, just generate text. Do three of them in parallel. One for data source one, the second one for data source two, and the third for data source three. Then all of those are going to generate summary A, B, C. Then you could pass that into a second one that's going to stream the text back to the front end.

01:46:23 - Brandon Hancock
▶ I wouldn't even do RAG. RAG would be, I think, overkill for what you're trying to do, because it's just database data. I would look at the core structure to see how the chat route takes in RAG data and adds it to the conversation. Because that's what's happening. So we're just hijacking the fundamentals for our unique purpose.

---

<!--SEGMENT
topic: AI in Education, Youth Adoption, and Presidential AI Challenge
speakers: Paul Miller, Brandon Hancock, elijah stambaugh, Ryan C
keywords: education, AI adoption, university interns, Presidential AI Challenge, Ohio computer science curriculum, N8N, refining education, Shipkit, K-12, critical thinking, Luddites, China AI curriculum
summary: The group discusses the challenge of getting young people and university graduates to adopt AI tools effectively, noting a gap between awareness and practical systems thinking. Elijah shares his son's participation in the Presidential AI Challenge using an N8N newsletter automation workflow. Brandon describes his refiningeducation.com brand and advocates for subvertly teaching systems thinking through AI use cases kids actually want (e.g., cramming for tests). The Luddite analogy is raised as a warning against resistance to adoption.
-->

01:47:08 - Brandon Hancock
Final thing, just going back to question one. Dude, I have no idea what's going to happen to kids. I generally don't know. I think about it quite often because, I mean, I'll just hop on a soapbox real fast — America's education system is trash. I think it's like 40% of kids can't read, literally just came out like a report or something today. So it's like, how the hell are they going to do anything?

01:47:45 - Brandon Hancock
And then on top of that, when it does come to being a productive member — just at your company, for example, coming out of college — unless there is someone driving that kid to build out projects and have a curious take on the world of like, oh, this is hard, I wonder if I can make it easier — unless that thought process is built in, it's very hard to just turn that on.

01:48:50 - elijah stambaugh
I think it's wild though that kids are thinking about not using it. I mean, I understand where they're coming from because it is going to make their lives harder. But like, China's not going to stop. Their three-year-olds are using AI. It's a part of their mandatory curriculum. So it's like, it's not stopping. So it's like adapt — which is hard. No one said it's easy, but yeah.

01:49:13 - Brandon Hancock
Well, it's exactly where the name Luddite came from. When the cotton mills, they were automating the manufacture of material. That's where the first Luddites came out. And I don't think Luddite is an option for young people all over the world.

01:49:41 - elijah stambaugh
I do have some ideas. Shipkit's going to help with that delivery. It'll take me a little couple — but I do own refiningeducation.com [link:refiningeducation.com]. So that is my brand that is coming out this year and it's not just simply to teach AI or that, but it's more about refining education matters for the future of work. And that's my tagline because we need to change a lot. I'm operational in a school, so I will tell you that this is on my mind all the time. But it's not on everybody's mind. They're just — it's a tool to cheat with and therefore don't use it.

01:51:00 - Brandon Hancock
▶ If tomorrow I had to make a YouTube channel on this topic, here's literally what I would do — they don't know they're learning, in their head they're going to think they're cheating, but the strategies I would show, they're going to be learning fundamentals of systems thinking. For example, hey guys, I'm going to show you how to cram for a test with AI. And then basically you would, in the act of teaching how to do it, you would break down exactly how a systems-level person would think about it. So you almost subvertly put in the critical thinking skills and expose them to that. You almost have to subvertly introduce the thoughts. You don't say, oh, I'm teaching you how to system design — you just give them the outcome, oh I'm going to help you cram for a test, because that's what they want.

01:52:22 - elijah stambaugh
And I am currently working on the Presidential AI Challenge [link:Presidential AI Challenge]. I'll be submitting it in three, four hours. So President Trump signed the executive order — not being political — and my son, it's for — there's three different tracks. And you submit, and it's been happening for a while. I've been on these calls every Monday. To your point, it's for the United States. It's to push AI in education.

01:52:00 - Brandon Hancock
So my son and his friend — he's a junior in high school — we're doing an automated newsletter. And so we've been working through this for a few months. We're doing an N8N [tool:N8N] workflow. I was going to try to — I did vibe code a front end and some other things to it. I'm really proud of him. He's worked really hard on this, but at the same time, he plays basketball, and his friend does too, so it's like other competing priorities. There are two state winners in Ohio.

01:52:14 - Brandon Hancock
▶ It's a phenomenal thing to add to resumes, especially if you win — you get to go to DC. There are so many cool perks that come from it.

01:53:46 - elijah stambaugh
So I'll show you — this is just an app that I am building with my family. It's just a Bible reading app, using Shipkit. Nothing super sophisticated, but you can see the familiar — we got the dashboard, add in here, it's got a bunch of different plans, you can browse different plans as well. And then in here, I've got the English Standard Version API coming in, and then you can go ahead and mark off where you left, you can highlight and then share that to a group. And then this is the Hebrew-Greek — so I highlighted the word Pharaoh, and then just click it, and it'll pull up the definition of it, the Hebrew word, and the passage.

01:57:57 - elijah stambaugh
I showed this — I built it for my son because he wants to read through the Bible this year, and then I showed it to a friend and he was like, can I use this? And I was like, well, I really didn't plan for it that way. So I said, give me about a month and I'll just kind of vibe slowly because it's not a major project.

01:59:07 - Brandon Hancock
▶ Two things that would be very cool — if I could just highlight any text or anything like that, and then it instantly throws it over to a quick summary of, like, here's what this means, here's how most people are talking about this — just a very quick summary or an action. And then that just starts a new chat interface with the context of the page here. And then here's literally what the whole prompt would be: this person has a question about this page, they're specifically asking a question about this section, please give them A, B, C, D. And then allow the conversation to just go wherever it wants to go from there. I think that would be super helpful — you're involved in the book, rather than just a passive consumer, you're participating with the book.

---

<!--SEGMENT
topic: Multi-Project DevOps Tool and Ollama Local Model Experimentation
speakers: Ty Wells, Brandon Hancock, Patrick Chouinard, Paul Miller, elijah stambaugh
keywords: Ollama, Qwen 3 Coder, local models, Claude Code, sub-agents, rate limits, Anthropic Max plan, knowledge graph, cross-project memory, RAG, DevOps tool, Shipkit Studio, Garmin watch, parallel agents
summary: Ty presents a cross-project DevOps tool that tracks memory, patterns, flaws, credentials, and insights across multiple simultaneous projects, feeding into a Shipkit Studio scaffolding system for on-demand software generation. Patrick raises the possibility of using Ollama with Qwen 3 Coder 32B as a local model backend for Claude Code to run background automation tasks without consuming API tokens, noting he hit his Max plan rate limit running a daily AI news aggregation pipeline. The group discusses the trade-offs of local vs. hosted models for agentic tasks.
-->

02:20:01 - Ty Wells
All right, I think next up is Ty. Floor is yours, buddy.

02:20:09 - Ty Wells
How's it going, guys? Really don't have any — well, I can show you something. I'm always working on it. That's a problem. So it's building while I'm talking to you. But really, I've been working on internal tools, mostly for different projects that I've got going.

02:21:00 - Ty Wells
A way to enrich what I'm learning — what works, what doesn't work — when I'm building with Claude Code. So I built this project that works across — it's global, that works across all my projects, and it injects different pieces of memory when I'm working on projects. So I'm storing that off through the sessions that I'm having with each build. These are different projects that I'm working on here, and some of the session saving that information helps build the memory, and then it's got some RAG in there, so you can look at that. But the key is really finding insights across these multiple projects.

02:22:00 - Ty Wells
You know, not have to remember where that is, but then I can look at some of these things and say, oh, this is good, so it's trying to find things that could work well in other projects. It's giving me those insights that run every so often and say how I can better improve another project, and then I get decisions to make about what I'm going to do with those insights.

02:22:31 - Ty Wells
This is the memory that I was talking about — patterns that it's trying to pick up. It's got sort of my identity, about me, and then obviously my preferences. So again, that's cross-project, so I don't have to go and set this context up every single time.

02:23:07 - Ty Wells
This flaw tracker is really what I like the best — I track flaws across projects, candidates where Claude Code is failing. Like, they haven't fixed a particular issue in the development process, they make the same mistake over and over. So I'm tracking those, but I also go out and do GitHub and web research to see — I gather candidates three times a day to see who's complaining about what on Reddit or wherever. And then I automatically try to reproduce that issue. If I do, then I add that as an actual flaw. If I don't, it's just a candidate.

02:24:06 - Ty Wells
I've got a lot of different keys and stuff, so I wanted to use the key store to take advantage of that, so it stores my credentials for the different projects that I'm working on, and I create test accounts, so I don't have to keep entering them.

02:24:51 - Ty Wells
And then skills is another thing — what projects have access to what skills. I'm going to have that organized so I can grant permission to certain skills for certain projects.

02:25:02 - Ty Wells
And then I'm adding subscriptions in here, which is my subscriptions for AI, different tools and stuff. It's connected to my Gmail, scans that, and I can upload a CSV for my credit card statement, so it can tell me, oh, you haven't touched this in X amount of days. I wanted to have it log in with those credentials and actually check, what was my usage on that, which is a tool, and so I can decide if I want to cancel that or not cancel it.

02:25:47 - Paul Miller
<Q>Ty, have you thought about what the actions are? Because you've discovered all of these things and all these gaps and these learnings. How will you translate that into something that you can use then with new projects? How will it move across?</Q>

02:26:49 - Ty Wells
<A>Well, there's a scaffolding project that I have that's going to build projects for me. You guys know I was working on this — the Shipkit Studio [tool:Shipkit Studio]. So that's where that's coming in. So when it's building in a one-shot — it's not really one-shot, it's just a very organized spec that it's building on — I need that to ensure that those known flaws are taken care of, otherwise it's going to run into the same thing. The end result is, I say, I need this built. And I'm questioned and quizzed about what it is I'm building. And then it produces that software on demand.</A>

02:28:12 - Brandon Hancock
<Q>Is this more a Ty tool? Are we going, oh, I want customers on this?</Q>

02:28:22 - Ty Wells
<A>No, this is a Ty tool. I don't know how many projects you guys work on usually at a time, but I show you my windows and I've got nine windows. Actually, I've got 11 because they're overlapping. But my point is I'm constantly building and I'm learning and I'm trying to curate that learning process because it's multiple projects for multiple things — for my own businesses, for clients.</A>

02:29:00 - Ty Wells
I built something today for a client — she told me she was struggling with eight hours. She spent a whole day on it every day, and I built it today for her, and she runs it, and that's it. So that's what I'm trying to get to — that software on demand.

02:32:01 - Patrick Chouinard
<Q>Yeah, it's more for the group before we finish — just because I was wondering if anybody has actually tried Claude Code with Ollama [tool:Ollama] since they've released the connectivity, because I think there's an insane possibility that I want to try, and I don't know if anybody did it. It's basically all the automated stuff that we talked about — automated research — and I think it doesn't require any intelligence whatsoever. It just needs the harness of Claude Code. So I would use Qwen 3 Coder 32B [tool:Qwen 3 Coder] to be the model behind Claude Code. I know it's never going to be as good as the Claude model, but if you have to run 30 web searches in parallel, they can do that, and they can do that for free with no rate limit.</Q>

02:33:29 - Brandon Hancock
<A>Yeah, sorry — the thing I was saying, so I was using Ollama, but I was using it to use Llama 3, and it was just such a bad model that I kind of got burned on using local models. I would love to hear how that goes with like a Qwen, because I never really got on the Qwen train, but I've heard great things.</A>

02:33:51 - Patrick Chouinard
It's good at tool calling, and it's smart enough. The 32B Q4 would most probably run on a Mac mini.

02:34:11 - Brandon Hancock
Again, it's not going to be — I'm not going to build a Shipkit application with it. But for simple tasks, like doing a web search, doing summarization, doing comparison between two files — if I can give one of those models access to the full harness and tool call of Claude Code, I think it could build some pretty insane local applications where the kernel is actually Claude Code without taking in a single token.

02:35:31 - Patrick Chouinard
▶ For building applications, completely agree, and I'm on the Max plan now, and I'm not planning on going back to anything else. But that said, I'm still hitting my rate limit every single day, even on the Max plan. So if I want something to run in the background like 24-7, I'm not going to give $10,000 a month to Anthropic. So if I have something that can run on a local model, if I have the harness for it.

02:36:00 - Patrick Chouinard
Is it possible to make a sub-agent that's a web search agent that then — I mean, right? You can then have it say, hey, when running agent X, use model Y, right? So that's literally the use case.

02:36:23 - Patrick Chouinard
That's literally what I've shared earlier — the whole process that I went through is to build an application that does exactly that. It does run multiple sub-agents using iQoo [tool:iQoo], because if I was using Opus, I would blow my limit every single day just running my pipeline that researches every provider every day. Because it researches all of them in the global news, it researches all of their tools, it updates its inventory of all of their tools and it makes note of the changes to the new way, and it does a mapping with all of our internal use cases and how each tool and each news item maps to our own use case internally.

02:37:22 - Patrick Chouinard
But running that every day uses all of the tokens that I had on a $20 a month Pro account. And a single run took basically the whole thing. So if I can run that on iQoo, it was already good. But if I could run it on a local model, well, damn, that would run 24-7.

02:37:46 - Brandon Hancock
The biggest question I have going through that experiment is how many you can run in parallel. That's actually would be my question — what can your computer handle? Because that would be the new bottleneck.

02:38:00 - Patrick Chouinard
I was able to go up to 12.

02:38:03 - Brandon Hancock
Seriously? That's crazy. I thought it was going to be like 3, 4.

02:38:29 - Ryan C
What sort of news are you scraping, Patrick, to kind of aggregate down? Because I've got to do something similar for my little content generation thing that I'm making for this influencer guy who's essentially wanting to do faceless influencing with his face. I'm going to do an AI generation of all that stuff, but I need to aggregate news on the things he wants the videos to talk about before I even think about generating the videos.

02:38:59 - Patrick Chouinard
It's a lot of the correlation that takes forever because for every vendor, I run an inventory. So a first run of search that I do on every vendor is find out all of the tools in their ecosystem. Because to me, if I'm going to say, oh, we're going to buy the Claude Enterprise again — well, Anthropic, it's not just the Claude model. It's Claude, but it's also Claude Code. And it's also their desktop thing. There's tons of things. Google, it's NotebookLM, it's all of that. So I had something discovering those tools. But again, I don't want to do that every day. And I want to make sure that I only add whatever is new. So I do a comparison. I build a YAML file with the content. And I do a compare between the two and just keep whatever is new every day. Then I take that to run the next search, which is going to search every one of those tools to get all the latest news of what changed on those tools, and then I do another search, which is global news, specifically in the finance industry.

02:40:12 - Ryan C
<Q>Where are you scraping that off? Web search or like a specific service?</Q>

02:40:15 - Patrick Chouinard
<A>Just web search from Claude Code. I just let Claude submit the search, gather the result, and that's it.</A>

02:40:32 - Paul Miller
▶ I was going to have a go at using that the next few days — using the Theo OSS model via Open Router [tool:Open Router], which is hosted, so you don't have to have it locally, but then keep it really, really cheap. Maybe a dollar per million tokens, which is less than Haiku, but the model's better than Haiku for agentic quality. Because now pretty much you're just paying for the hosting if you're using Open Router with some of those open-source frameworks.

---

=== UNRESOLVED SPEAKERS ===

The following raw speaker names appeared in the transcript and could not be resolved against the provided alias map (which was empty/not supplied in context):

- **Ryan C** — appears late in the transcript discussing freelancing, YouTube content creation, screen signage app, and estate agent client
- **Alex Wilson** — asks about the GitHub branch review workflow
- **Ty Wells** — presents the cross-project DevOps/memory tool and Shipkit Studio
- **elijah stambaugh** — discusses education, Presidential AI Challenge, Bible reading app, and refiningeducation.com
- **Juan Torres** — discusses ETL project engineering challenges and landing page
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** — presents Call Coach AI and NeuralSpark RAG pipeline