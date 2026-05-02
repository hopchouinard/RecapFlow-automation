=== SESSION ===
date: Unknown (Tuesday session, date not specified)
duration_estimate: ~2 hours
main_themes: Gemini CLI as search agent, web scraper UI development, cybersecurity repo scanner, Cursor 2.0 release, Claude Code vs Cursor cost comparison, AI developer hiring trends, trigger.dev real-time subscriptions, document processing pipeline for wholesale supply, ADK agent framework evaluation, automated PR review tools, chart generation in agentic UIs

---

<!--SEGMENT
topic: Session Open and Housekeeping
speakers: Patrick Chouinard, Tom Welsh, Paul Miller, Ty Wells, brandon hancock
keywords: ShipKit, calendar confusion, Claude Code, Playwright, MCP server, Cursor, landing page, brewery, automation
summary: The session opens with informal catch-up and apologies for scheduling confusion. Brandon shares two quick updates: an upcoming YouTube video on using Playwright as an MCP server with Claude Code and Cursor for browser automation, and a real-world demonstration of Claude Code completing a full day's email workload for a brewery client in under 10 minutes.
-->

00:07:00 - Patrick Chouinard
Hey, Patrick.

00:07:01 - Tom Welsh
How's it going?

00:07:02 - Tom Welsh
Good, good.

00:07:04 - Patrick Chouinard
I think it's going to be a quiet one tonight.

00:07:08 - Patrick Chouinard
It's caught everyone on the hop.

00:07:13 - Tom Welsh
For some reason, I keep thinking it's a Thursday night, but yeah.

00:07:20 - Patrick Chouinard
Yeah, there was a bit of confusion yesterday as well with how it was announced and it was shown in the calendar.

00:07:29 - Tom Welsh
I was on the ShipKit [tool:ShipKit] call yesterday, so I knew it wasn't on.

00:07:38 - Patrick Chouinard
How are your developers getting on?

00:07:41 - Patrick Chouinard
There's tons of change that happened in the last couple of days that has been keeping me busy. Every time I find a new way to save time, they find three new ways to consume time.

00:08:00 - Tom Welsh
I got to see you guys twice in one week.

00:08:25 - Tom Welsh
We had a power cut on Monday and it's blown up my PC. Luckily I've got the Macs.

00:09:00 - brandon hancock
I apologize in advance for causing all the confusion yesterday. I thought I even did it all right. I updated the event. I was like, man, I got this in the bag. And then I get a call from Paul, Brandon, where are you?

00:09:30 - brandon hancock
What I will do is let's get this opened up. We'll do some quick screenshots. All right, so we'll do that as the call order. Let's see, quick updates for you guys. So one, I'm working on a new YouTube video right now to show you guys how to use Playwright [tool:Playwright] as an MCP server with Claude Code [tool:Claude Code] and Cursor [tool:Cursor]. This thing is so cool. The second you see it do work, because it's like, it just feels agentic. For example, I was working on a landing page and I'm like making it 50 pixels bigger. Oh, that's bad. I make another 50 pixels bigger. And it just over and over and over again. And I'm like, why the heck am I doing it? So I have a new script for you guys that's working. You'll all get the updated script so you can do this yourself if you're ever doing mobile responsive stuff.

00:10:38 - brandon hancock
Thing two, I've been always helping out one of my buddies. He owns a brewery and a wedding venue with all things related to AI. I built him a Notion [tool:Notion] pipeline way back. And today they needed some help to get through writing and sending out emails faster. And it's so funny because all four girls that are working on this, they're like, man, there's so many tasks to do. And I was like, hey, I'm just going to hook up Claude Code, give me 10 minutes, and I will do your entire workload today, all of yours. And it did. That's the part that's crazy.

00:11:15 - brandon hancock
I texted my buddy, I was like, so I'll take a paycheck, actually, for all of them. It is crazy the second you kind of see how to use these tools effectively. It was the most eye-opening experience of, like, post-AI world and pre-AI world. And they were like, that's disheartening and exciting at the exact same time.

▶ 00:11:42 - brandon hancock
Seriously, if you're not using Claude Code or Cursor to automate non-code stuff, you're leaving a lot of time that could be automated.

---

<!--SEGMENT
topic: Gemini CLI as Parallel Search Agent
speakers: brandon hancock, Patrick Chouinard, Jake Maymar, Paul Miller
keywords: Gemini CLI, Google ecosystem, parallel search, NotebookLM, deep research, rate limits, Gmail account, Network Chuck, file output, simultaneous queries
summary: Patrick introduces Gemini CLI as a powerful search agent that leverages Google's ecosystem to run simultaneous multi-perspective research queries and save results directly to disk. The group compares this approach to Claude and OpenAI deep research, noting the key differentiator is parallel execution. Rate limit differences between Google Cloud Enterprise accounts (100/day) and standard Gmail accounts (1,000/day) are clarified.
-->

00:12:34 - brandon hancock
Dude, I've been going into Gemini Research, and you're right. It's good. So, Gemini CLI [tool:Gemini CLI] for the win on all things searching. So, thank you, Patrick.

00:12:46 - Patrick Chouinard
Honestly, I've started this morning to use it for that reason, and it's been going nonstop the entire day.

00:12:55 - brandon hancock
And I think I found your issue with the number of requests.

00:13:00 - Patrick Chouinard
Correct me if I'm wrong, but you probably have a Google Cloud Enterprise account or a corporate account of some kind.

00:13:10 - brandon hancock
Don't limit it at 100 calls per day.

00:13:13 - Patrick Chouinard
If you go through a simple Google account, a Gmail account, you're going to have the 1,000 calls per day. So you should be able to put it nonstop also.

▶ 00:13:25 - brandon hancock
Just quick background, guys. What Patrick's talking about is Gemini CLI. I've just been using it a little bit less recently because I would just love Gemini 3.0 to come out. So it feels like a much beefier tool is my main reservation right now. And the other issue was I was getting rate limited at 100 requests — I thought it was 1,000, but it was actually 100. So thank you, Patrick, for pointing that out.

00:14:00 - Patrick Chouinard
Basically, just to answer, Paul, what I mean by that is that Gemini CLI does have intrinsic access to the Google ecosystem. So basically, you can ask Gemini CLI, like, go search on X subject from 20 different points of view, and it's going to go and do its thing. And since it's a dev tool originally, it means you can actually save the result of that search directly into a file. So you can have multiple calls, or you can even start 20 of them in parallel, running a bunch of research, dumping all that content in files, and then having the last one correlate everything together.

00:14:47 - Jake Maymar
<Q>So how does this relate to, like, Claude Deep Research or OpenAI Deep Research?</Q>

00:14:55 - Patrick Chouinard
<A>Deep research of any kind is going through hundreds of sources on one question. What I'm doing right now is giving the AI 20 different questions to observe from 20 different points of view simultaneously. So it's not going to create as much content about one single subject, but it's going to create content for the same subject on multiple points of view at once. And then you correlate all of the content that you've written on disk afterward.</A>

00:15:27 - Jake Maymar
I'd love to understand that a little bit more. Are you playing around with the command browser as well, or no?

00:15:49 - Patrick Chouinard
I don't know if everybody knows Network Chuck [tool:Network Chuck], but he's the one who created a video this morning about it. And since I watched it, I haven't stopped. He explains extremely well how to use Gemini CLI as a search agent.

00:16:07 - Jake Maymar
Yeah, because the thing is, I use it all the time. I do deep research in Claude all the time, but I can't do simultaneous searches.

00:16:17 - Patrick Chouinard
That's the biggest problem. And this one does simultaneous. That's pretty cool.

00:16:21 - Jake Maymar
Also, I heard you could hook it up to NotebookLM [tool:NotebookLM], too.

00:16:28 - Patrick Chouinard
You can actually ask it to look at videos because, again, connected to the Google infrastructure. Not a model I would use for development, but for a lot of other things, it's actually insane. And since you can spawn a new instance, you can run as many of them as you want. With a thousand queries per day, it can search pretty much all day long without any kind of cap or limit.

▶ 00:16:51 - Patrick Chouinard
With a thousand queries per day, you can do a whole lot — it can search pretty much all day long without any kind of cap or limit.

---

<!--SEGMENT
topic: Prompt Editor UI with Autocomplete
speakers: Patrick Chouinard, brandon hancock, Jake Maymar
keywords: prompt editor, autocomplete, Monaco editor, TipTap, debounce, tab completion, template library, GitHub Flavored Markdown, Mermaid, UX design, ShipKit
summary: Patrick demos a custom chatbot UI he built that separates prompt design (left panel) from AI responses (right panel), featuring a debounce-triggered autocomplete that predicts prompt completions in real time — similar to VS Code's IntelliSense but for production content generation. He also describes a prompt template library with executable function support. Brandon and Jake discuss editor library choices (Monaco vs TipTap) and suggest using Gemini CLI to research the best option.
-->

00:17:09 - Patrick Chouinard
The other thing I wanted to show today is... Last week, I talked about wanting to rethink the actual UX for chatbots. And I actually implemented something. It's not polished yet, but that's the idea. Basically, my interface, instead of having a small little text box at the bottom just to do chat a couple of sentences at a time — we keep telling our users, like, no, if you want good results from AI, you need to provide context and a lot of meat around your prompt. So you always end up designing your prompt somewhere, copy and pasting it into whatever chat utility you're using. So instead, you can design your prompt on the left, and you're going to get your answer on the right. And it does keep in mind the context, so it still has the full context of the entire exchange, but you focus on one answer at a time.

00:18:20 - Patrick Chouinard
But the really fun thing that I've created is, let's say you start to say, so I'm designing a prompt. I'm going to go, "you are a help..." And I wait, and there we go. After a debounce amount of time — 600 milliseconds for me — it sends actually what I wrote so far, plus a bit of the context, with a system prompt that's going to ask, what do you think would be the end of that sentence? So it can actually predict the end of the sentence. So I can just go tab complete exactly as if I was within Visual Studio, but within a production environment instead to produce content.

00:19:15 - brandon hancock
<Q>Patrick, super quick question on this. Did you end up using TipTap [tool:TipTap] to make your editor or did you end up using Visual Studio Code open source stuff?</Q>

00:19:25 - Patrick Chouinard
<A>Actually, neither. For the first MVP, it's just a very well-constructed text area with a lot of CSS. But eventually what I would like is to have Monaco [tool:Monaco], the open source for VS Code. There's a lot of packages to install, but I want to prove the concept that I have a prompt designing area that has that autocomplete. And whenever I submit, I have an area where I could have a formatted or unformatted response. So if I want to implement GFM, like GitHub Flavored Markdown, to have Mermaid [tool:Mermaid] in there and all of those.</A>

▶ 00:20:13 - brandon hancock
A comparison of using Monaco versus TipTap — I would be very curious to see what AI says is the best one to use. So if you ever do that research, please let me know what it says, because I genuinely have a question mark on which one's the best option right now.

00:20:45 - Patrick Chouinard
Believe me, when I get there, there's going to be research done up front, so I don't waste my time going one way and then deciding to go the other way.

00:21:00 - Patrick Chouinard
Whatever prompt I've designed, I can save as a template. I also created a template library. I can load, I can edit the prompt in the library, I can mark it as a favorite. And I want to put a lot of intelligence in that prompt library. Basically, I want to create some prompts that will be prompt editors — like you submit another prompt and it improves it. So I want to be able to call those as functions. So basically, the prompt library will be a library of text, but also a library of executable functions.

00:21:33 - brandon hancock
That's awesome. It's so cool just how you guys keep turning these ShipKit templates into wildly different things. Tom on his scraper, you on your editor — everyone is doing so many cool things.

---

<!--SEGMENT
topic: Web Scraper with Visual Element Picker
speakers: Tom Welsh, brandon hancock
keywords: web scraper, Next.js, Python, Celery, Vercel, element overlay, competitor analysis, template library, Cursor, workers, job queue
summary: Tom demos a consumer-friendly web scraper app built with a Next.js frontend and Python/Celery backend. The headline feature — built in under 24 hours after the previous session — is an augmented overlay that lets non-technical users visually click page elements to define scraping targets, replacing the previous manual-only approach. The backend uses Celery workers for scalable job processing, with preview and production environments running through Vercel.
-->

00:22:23 - Tom Welsh
Yeah, after your little discussion yesterday about my little apps, which I'm obviously going to try and throw up now, because I've broken it blatantly today.

00:22:57 - Tom Welsh
Yeah, as Brandon was saying, I've been working on this little app. Which is Web Scraper [tool:Web Scraper], Login. So I've gone to the augmented stuff.

00:23:12 - brandon hancock
I'll give background for everyone who's just seen this for the first time. So what's really cool, what Tom has worked on, is building up his own scraper that is going to be more consumer-friendly. Meaning, ideally, what a consumer should be able to do is say, like, hey, I want to track these three, four elements on a page. And over time, just every day, do a scrape or some amount of time. Tom has all the background infrastructure working, where he actually has Python containers doing all the scraping. And he has built a really cool front end. And yesterday, we were brainstorming what's the best way to make the UI and UX experience as easy as possible for someone to pick elements that they want to track on a page.

00:24:13 - Tom Welsh
After a little chat with Brandon yesterday, we were talking about throwing up a screen for the customer, the client, and then being able to just click on the page — basically an overlay on the page. So it comes up with this little thing down here. And you can see, as you move about, it highlights. Continue to field map. Continue to scrape. So I've broken it. But basically, the idea is, like Brandon says, to give this to front of people. People that aren't in IT. People who want to do product competitor analysis or whatever, and just pull stuff up left, right, and center, save them off to templates.

00:25:22 - Tom Welsh
The front end's Next.js [tool:Next.js], the back end's a Python back end, but on the back end, I'm now using Celery [tool:Celery], which breaks it down into multiple workers, so you can actually send in a job, the job's then picked up by the workers, and this is disconnected from the database, so you have multiple workers running, and it all scales. So if you send in a thousand jobs, it'll go from five workers working on five tasks, up to 20 running concurrently.

00:26:05 - Tom Welsh
I've got a back-end dev set up, but I've got a preview and a prod set up as well, all running through Vercel [tool:Vercel], making use of their Vercel API to get things up and running.

00:26:47 - brandon hancock
Literally yesterday, the only option was manual. So the fact that Tom did the full load-the-website, do-the-overlay, augmented-clicking — that was done in like 24 hours, guys. So yeah, hats off to Tom.

00:27:05 - brandon hancock
<Q>Quick question, are you using Claude Code right now or Cursor, just out of curiosity?</Q>

00:27:09 - Tom Welsh
<A>Cursor. I started watching your Claude Code video. I thought, no, too much to learn. Go back to Cursor.</A>

▶ 00:27:25 - Tom Welsh
I think if I move to Claude Code CLI, I'll just get stuck in the weeds and wonder how I'm doing stuff. Whatever you're doing is working — you're moving lightning fast.

---

<!--SEGMENT
topic: Cybersecurity Repo Scanner App
speakers: Ty Wells, brandon hancock
keywords: cybersecurity, GitHub, NIST, OWASP, CVE, AWS Lambda, static analysis, vulnerability scanning, scheduled scans, Next.js, dependency checks
summary: Ty demos a security scanning application that connects to GitHub repositories, runs 40+ static analysis checks against NIST and OWASP Top 10 standards, and surfaces CVE-linked vulnerabilities with fix prompts ready for Claude Code or Cursor. The app runs on AWS Lambda, supports scheduled recurring scans, and generates downloadable reports. A freemium model offers two free project scans before requiring a paid plan.
-->

00:27:48 - Ty Wells
I'm still working on the in-person. Well, it's actually, I'm sort of done with it. I've productized it with a payment platform and other stuff. But that's not what I'm showing you guys today.

00:28:13 - Ty Wells
Okay, so I'm obviously a cybersecurity guy, if you guys don't know. I started to build this. This is basically to scan your repo and check your code base for known security vulnerabilities and other things. And I know there's platforms out there, but there's so much AI slop out there. So this is the platform to do just that. So you can connect to your GitHub here through a PAT or OAuth. And then you can come in and basically scan that repository.

00:28:55 - Ty Wells
What it's doing is it's connecting to your GitHub, pulling down, and then checking it against the NIST [tool:NIST] and OWASP [tool:OWASP] Top 10 vulnerabilities and so forth. And then I have it checking using a couple other tools to test it out. And it runs out in Lambda on AWS [tool:AWS Lambda], in that environment, and then it comes back with results.

00:29:37 - Ty Wells
I actually ran it on this code and found three vulnerabilities. So I fixed the vulnerabilities. What happens is if you have a vulnerability, you can open it up. It's a modal that'll tell you what the vulnerability is and have a link to that CVE [tool:CVE], which is the exploit out there so you can find out what that does. It gives you a simple version and an advanced version. The simple version gives you basically the TL;DR of what the issue is, and it gives you a prompt that you can inject into Claude Code or Cursor to fix that issue, like if it's a dependency issue or something along that line.

▶ 00:30:24 - Ty Wells
The simple version gives you a prompt that you can inject into Claude Code or Cursor to fix that issue directly.

00:30:28 - Ty Wells
I haven't touched this in like four months. But this is the gist of it. You can generate a report. It'll show you everything in there. And then you can schedule it to run because the minute you scan your code base, it's vulnerable again, basically, right? As soon as you clean up all the room. So the ability to have it run on whatever frequency and then report via whatever notification system you set up.

00:31:08 - brandon hancock
<Q>So I know you said AWS is your go-to, at least for this one. And then you're using Lambda functions. Is there anything before or after the Lambda functions?</Q>

00:31:38 - Ty Wells
<A>There's, I think, 40 plus checks that I'm running right now as a static analysis. And then I'm running those against the CVEs to see what exploits exist for those packages and so forth.</A>

00:31:52 - brandon hancock
<Q>And so just to understand architecture, is it like direct Next.js application to Lambda function and back?</Q>

00:32:01 - Ty Wells
<A>Yes.</A>

▶ 00:32:29 - Ty Wells
You get two free scans — two projects you can scan — and then if you want to get on a plan, that gives you more projects and so forth.

---

<!--SEGMENT
topic: Claude Code System Prompt Discovery
speakers: Ty Wells, Patrick Chouinard, Jake Maymar, brandon hancock
keywords: Claude Code, system prompt, Anthropic, prompt engineering, published prompts, prompt length, Haiku 4.5, token cost, Claude subscription pricing
summary: Ty accidentally reveals that Claude Code's internal system prompt — extracted mid-session — runs to 35 pages, significantly longer than what Anthropic publicly documents. Patrick notes Anthropic does publish system prompts but suspects the public version is incomplete. The group discusses implications for prompt engineering best practices and transitions into a cost-optimization discussion around Claude Haiku 4.5 versus Sonnet, and subscription tier recommendations.
-->

00:40:32 - Ty Wells
I was working on a project and somehow it got crossed up and I was trying to make some adjustments to a prompt, but it started making adjustments to its own prompt. And then I'm like, okay, well, remind me again, what was the original prompt? And there it was.

00:41:14 - Ty Wells
Cloud Code System Prompt. So I was trying to make some adjustment to a prompt, and it decided that it needed to revise this prompt to include what I wanted. So that's where the confusion sometimes came in. I was adding intent analysis and other stuff to my prompt, but further down here... this was the original prompt here that it gave me.

00:42:09 - brandon hancock
It's crazy. At the end of the day, all of these amazing tools are literally just prompts built on top of insane models. Like, it's literally just prompts.

00:42:17 - Ty Wells
35 pages.

00:42:20 - brandon hancock
Whoa, that's wild.

00:42:50 - Patrick Chouinard
Yeah, actually, that's special because Anthropic [tool:Anthropic] is known to actually publish their system prompt. You look at the link I've sent you — it's not actually really the same, so that's why I find it interesting, because they might be publishing something, but not the actual 100% real system prompt, because yours seems to be more detailed compared to what they've published on their website.

00:43:18 - Ty Wells
Yeah, it's way more than this.

00:43:26 - Jake Maymar
I think it would evolve, right? So you'd have the system prompt, it would probably have nightlies, where they go through and they review, and then they pick — I'm assuming it's multiple things all running the same prompt, and whichever ones are doing the best, those are the winners. But I'd be surprised that they went from what they post for October 15, and getting something like five times as big in a week.

▶ 00:43:55 - brandon hancock
Yeah, Ty, I would be very curious just to study that, just to see, like, what am I not doing in my own prompting versus what they're doing?

00:44:14 - Tom Welsh
You're not writing 75-page prompts. That's the problem.

00:44:23 - brandon hancock
Yeah, that's it. I got to level it up. I thought my 20-page prompts were hitting the ceiling, but apparently there is no ceiling, honestly.

▶ 00:44:34 - brandon hancock
Patrick really said it concisely in the chat, but basically Haiku 4.5 [tool:Claude Haiku 4.5] is twice as fast and a third of the price, which is crazy. So seriously, if you get a chance to use it on your subscription, your usage will go way further.

---

<!--SEGMENT
topic: Cursor 2.0 Release and Tool Cost Tradeoffs
speakers: Paul Miller, brandon hancock, Patrick Chouinard
keywords: Cursor 2.0, proprietary model, built-in browser, Claude 4.5, Anthropic, Claude Code, Haiku, token cost, ShipKit, $200 plan, agentic coding
summary: Paul flags the overnight release of Cursor 2.0, which includes a proprietary coding model and an embedded browser for agentic self-checking. Brandon discusses hesitancy around immediate upgrades due to breaking changes, and the group debates cost optimization strategies — specifically when to use Claude Haiku 4.5 for small/medium tasks versus Sonnet, and whether the $100 or $200 Claude subscription tier makes sense for heavy build sessions.
-->

00:35:39 - Paul Miller
<Q>Has everyone had a look at the Cursor 2 release that's come out overnight?</Q>

00:35:52 - Paul Miller
<A>They've got a new model in there, which seems really good. Their own model for code. I think they're sick of having to give away all their money to Claude, to Anthropic. And they also have a browser built in, so when you're testing the app, it's looking at their browser within the code, so it can self-check from an agentic perspective what's going on.</A>

00:36:33 - brandon hancock
<Q>I'm curious because it doesn't show which one is the best. Like, I'm guessing best Frontier is Claude 4.5 [tool:Claude 4.5], if I had to guess. And they're saying they're right under it. It's so funny that they don't say which one they're competing against. Like, who is Frontier? I'd like to know.</Q>

▶ 00:37:06 - brandon hancock
I'll 100% try it out tonight because I'm sometimes hesitant to even upgrade Cursor because I've done it a few times right when a new version comes out and something breaks. So I'm very hesitant to update until it's been a week or two. Then I'm like, okay, they've probably figured that out.

00:37:29 - Paul Miller
My big focus is I want to make the jump from Cursor to Claude Code. I've spent $1,200 US on that app that I'm doing for my core business. This is the one I want to show our CTO. But I've got some deliverables I've got to do, and I just don't want to have to keep putting it on the model that I've already burned $1,200 on.

00:38:14 - Paul Miller
<Q>So I haven't been on the ShipKit calls, but are you saying now with the current version of ShipKit, that if I update the version and I load that in, it's already got the hooks for Cursor?</Q>

00:38:31 - brandon hancock
<A>Yeah, it's got the hooks, it's got the commands, it's got everything. So you'll be able to cruise through it. There's one example video at the end — the demo walkthrough — so you can actually see it in action.</A>

▶ 00:39:26 - brandon hancock
If you are trying to be price sensitive, Paul, I have been experimenting with Haiku, and for small, medium tasks, it's very impressive. No complaints on Haiku. And Patrick's been using it — he definitely recommended it to me as well. Really, really impressed with how effective it's been at just, like, small, medium tasks.

▶ 00:40:18 - brandon hancock
In your case, you might want to do the $200 a month plan, Paul. If you're going to be like going back into deep build mode, I think you could probably get the full $200 out of it. But you might just want to start at $100.

---

<!--SEGMENT
topic: AI Developer Hiring Trends and Team Structure
speakers: Paul Miller, brandon hancock, Patrick Chouinard, Jake Maymar, Prem, Tom Welsh, Sam, Adam
keywords: junior developers, senior developers, AI-assisted coding, college education, Upwork, context window, business analyst, Theo T3, ChatGPT, hiring strategy, AI upskilling
summary: Paul raises the question of whether teams are still hiring junior developers or pivoting to AI-only workflows. The group shares diverse hiring strategies: Brandon favors overseas college-level freelancers on Upwork for small tasks; Patrick hires developers with AI proficiency and frames experience as "context window size"; Jake upskills subject-matter experts in AI rather than hiring coders; Prem's company is shifting toward business-analyst-heavy roles with technical backgrounds. The discussion references Theo's (T3) recent video on junior vs. senior dev value in the AI era.
-->

00:45:01 - Paul Miller
<Q>A question for the guys out there. If you've got developers, are you still hiring juniors or are you just getting seniors or just getting AI?</Q>

00:47:58 - brandon hancock
<A>So I currently really like hiring overseas developers in college. They are way smarter. Like, when I was in college versus what they're doing in senior year, I was like, dude, you made me look like I'm picking my nose. With the latest frameworks and everything. Insanely smart, insanely sharp, insanely hardworking. So yeah, a lot of Upwork [tool:Upwork] freelance developers, they absolutely crush it. Because the kicker is, you can keep the small medium tasks that a junior developer can do and just literally throw them all in Linear [tool:Linear]. That's just kind of how we've been burning and churning.</A>

00:49:28 - Patrick Chouinard
Yeah, we're still hiring, but we're hiring developers that have a background in AI usage. So basically, we're not replacing them with AI, but we want a developer that knows how to use AI. Nowadays, when you start, you all have access to the same tools. It's just that the more experience you have, the larger your context window.

00:50:00 - brandon hancock
<Q>Do you measure your employees based on their context window?</Q>

00:50:04 - Patrick Chouinard
<A>Exactly, because the one with more experience can manage more agents simultaneously and understand where they are in the process, where the junior one, they're going to manage a single agent at a time to make sure they don't make mistakes. So yeah, more experience equals more context window.</A>

00:50:25 - Jake Maymar
I was just going to say, I don't actually hire that many devs, but I do find people that have subject matter expertise that I need, and then I upskill them in AI. And that's been really helpful because they do work for me and I do work for them kind of thing. Because certain things like this person has 20 years in healthcare — I don't even understand the whole payer structure. But I've been working with them and doing workflows and learning a lot, but now I can actually use them for certain things that they just wouldn't have time to do. Some of these people have actually retired, and they're really interested in AI, and they have time on their hands.

00:51:31 - Prem
One of the things that we have started doing is, again, we used to be heavy on the technical side of interviews, like for senior developers and stuff, but now we are looking more for people who understand the application as a whole and who can understand things from a customer perspective — who can understand the problem statement better. You used to have more introverted coders who could just sit in a cubicle and code, but right now it's more like who can understand the problem statement and who can be forward towards AI. We're moving more into a business analyst heavy role, I would say. They have a technical background, but not coding-heavy like what we used to do.

00:53:51 - Tom Welsh
I did a master's degree in cybersecurity about four years ago, and it was ridiculous, the stuff they were teaching us then. You're getting all these developers coming out of college and unis now, who are going for grad jobs, who have probably got more AI chops than senior devs in some of the companies. And they're like, how do you exploit that, but still keep the hierarchy in the business?

00:55:42 - Adam
My age, I've got a lot of friends whose kids recently graduated from college, some of them with CS majors, and they're doing things like parking boats at the marina. So yeah, those kids have had a real hard time.

▶ 00:46:24 - brandon hancock
College has literally failed most junior developers. You should be coming out as a mid-level developer. There's no reason to go through college and not come out as mid-level at this point. You should be building the entire four years.

---

<!--SEGMENT
topic: OpenAI Agent Builder and Model Agnosticism
speakers: Adam, brandon hancock
keywords: OpenAI Agent Kit, agent SDK, Python export, model agnostic, local models, workflow builder, GUI drag-and-drop, provider agnostic
summary: Adam asks whether the OpenAI Agent Kit GUI is simply a wrapper over the OpenAI Agents SDK and whether exported Python code can be swapped to use non-OpenAI models. Brandon confirms the GUI generates underlying code that can be exported, and community member Alex suggests the framework is model-agnostic, meaning local or alternative models could theoretically be substituted.
-->

00:56:38 - Adam
<Q>So, like, the OpenAI agent builder [tool:OpenAI Agent Kit], you know, the GUI drag-and-drop — is it just the agent SDK underneath? And I was wondering, like, if you could export the Python and switch, like, what models you use to use, like, a non-OpenAI model?</Q>

00:56:58 - brandon hancock
<A>So there's Agent Kit, which is like the cool UI that you were looking at. And then under the hood, OpenAI has its own OpenAI agent framework [tool:OpenAI Agents SDK]. And it's yeah, it is literally a UI on top of that. So once you're done building a workflow, there's actually a little export button that you can click and see all the generated underlying code. So that is possible to do. So you could export and then swap in a local model or something if you wanted.</A>

00:57:50 - brandon hancock
The only kicker I am worried about — I don't know if their tool is agent agnostic or provider agnostic. I don't understand why it wouldn't be. It's just maybe if there's a specific tool call or something that other models don't provide.

00:58:00 - brandon hancock
Alex thinks it is model agnostic. Yeah, no, Adam, I think that's definitely, definitely possible.

▶ 00:57:25 - brandon hancock
Once you're done building a workflow, there's actually a little export button that you can click and see all the generated underlying code — so you could export and then swap in a local model or something if you wanted.

---

<!--SEGMENT
topic: Trigger.dev Real-Time Subscriptions and Architecture
speakers: Morgan Cook, brandon hancock, Jake Maymar
keywords: trigger.dev, real-time, server-sent events, WebSockets, Supabase, RLS policies, background jobs, video processing, pub-sub, Inngest, Next.js 16, streaming
summary: Morgan introduces trigger.dev's subscribe/stream feature as a solution for real-time updates across users without exposing Supabase credentials client-side. The group discusses the architectural tradeoffs between polling, WebSockets, Supabase Realtime with RLS policies, and trigger.dev's approach of using server-side events with a dedicated background job server. Brandon explains why trigger.dev is preferred over Inngest for AI-heavy workloads. Morgan also raises Next.js 16 but Brandon advises waiting before upgrading core stacks.
-->

01:06:43 - Morgan Cook
One of the things I have, we talked about before, was trigger.dev [tool:trigger.dev]. And so that's for another project coming up, but I need a bunch of background tasks. They'll be long-running. Some of it will be video processing, but some of it is notification through to other users that are on the application — not necessarily the user that's submitting the information, but to other users currently on the application. There's a subscribe system that they have in trigger.dev.

01:07:23 - brandon hancock
So I will release the template before the videos, just so you're not waiting an extra week or so. And what is the exact feature? So you're saying on their subscribe capability?

01:07:47 - Morgan Cook
Yeah, they have — you can subscribe to a token and then anytime that metadata for that token updates, it automatically sends updates to all of the subscribed users, so their screen will refresh automatically. Instead of doing WebSockets [tool:WebSockets], it's doing server-side events or something?

01:09:42 - brandon hancock
<Q>So this is a real-time chat with Supabase [tool:Supabase] using trigger.dev, that's the idea, and then it's not client-side?</Q>

01:09:57 - brandon hancock
<A>It's both. Here's what we're really trying to solve. As you build out larger and larger applications, there comes a time when you need to build in what feels like real-time updates. The level-one intro way to do this is polling, where every user is just every second, every three seconds, just like, do you have data? But if you scale to a system where there's like thousands of users concurrently, all making reads at the same time, you can crash your system. Now, with Supabase, you can actually set up what they have — basically full-time persistent connections where you're watching in real-time what's happening to the database. The gotcha on that is there are things called RLS policies [tool:RLS policies], row-level security policies, which become a pain in the butt. The reason why you have to do it is because you have to bring the Supabase client out of the back end and put it in the front end. Which means if anyone knows how to access those environment variables and you don't have your RLS policies airtight, you're screwed if there's a bad actor.</A>

▶ 01:14:35 - brandon hancock
Morgan, phenomenal suggestion — it looks like trigger.dev has a workaround to have a friendly client version and a friendly back-end version to support this.

▶ 01:14:39 - brandon hancock
Trigger.dev and Inngest [tool:Inngest] are competing platforms, both very popular. Trigger.dev just has a ton more AI capabilities, which is kind of up our alley. So that's why we're going Trigger.

01:16:23 - brandon hancock
<Q>What's going on with Next.js 16 there, buddy?</Q>

▶ 01:16:31 - brandon hancock
<A>I'm waiting a little bit before making any upgrades, moves, or anything. I don't like to be first mover on core stacks because the second you do it, you spend so much time like, well, this package doesn't yet support this. And you'll spend forever working on stuff that literally doesn't move the needle for your app or your business. I usually wait at least two months before making big changes.</A>

---

<!--SEGMENT
topic: Document Processing Pipeline for Wholesale Supply
speakers: AlexH, brandon hancock, Patrick Chouinard, Prem
keywords: Chunker, ADK, fixture schedule, document extraction, OCR, Supabase, Postgres, vector search, fuzzy match, LandingAI, Reducto, Xtract, wholesale plumbing, co-founder search, Cloud Run, agent engine
summary: Alex demos a multi-agent pipeline built on Google ADK that processes construction fixture schedules (complex multi-column PDFs) for wholesale plumbing supply quoting. After two months struggling with document extraction, he found Chunker (CHUNKR) to be best-in-class for maintaining table architecture at ~96-97% accuracy, outperforming LandingAI, Reducto, and Xtract. The orchestration agent delegates to a "takeoff agent" that decomposes line items row by row. Next steps involve product catalog matching using vector search. Brandon advises deploying to Cloud Run instead of Agent Engine for streaming support. Alex mentions seeking a co-founder in San Diego.
-->

01:19:00 - AlexH
So I finally have a lightweight UI on top of my agent. So if you guys — I don't know who remembers, but I used to own a wholesale plumbing supply business. Are you guys seeing a fixture schedule or like a PDF?

01:33:36 - AlexH
So I used to own a wholesale plumbing supply business. Typically this is like a hundred-page document that gets sent down this waterfall from like a general contractor to a plumbing contractor or like HVAC mechanical. And then these get sent down to the suppliers. And so like suppliers, basically you have these teams that sit here and do these all day. Right now it's fully manual, and the only tech stack that exists in wholesale supply is the ERP. And those are like 90s UIs on top of DOS-based systems now. So it's super manual.

01:34:16 - AlexH
So basically, I've got this agent that goes and looks for these specific tables. Fixture connection schedule, heat pump water heater schedule, equipment schedule, circ pump schedule, drainage pump schedule. But it's ignoring all these other ones. And this was hard to figure out in the beginning just as a start because it's a huge document processing challenge, which is actually really hard. So I finally got that figured out. I'm actually using Chunker [tool:Chunker], if you guys have ever used Chunker or haven't tried it, you should try it. It's been the best — really honestly, even off the shelf above and beyond anything that I would try to fine-tune on top of Azure Doc Intelligence [tool:Azure Doc Intelligence] or Google Document AI [tool:Google Document AI].

01:35:00 - AlexH
So it posted this document processing pipeline, and then it hits an orchestration agent — this is on ADK [tool:Google ADK] — that then sends a task to what I call a takeoff agent. Basically what it's doing is it's going line by line through these tables, and it's decomposing what the engineer is specifying. So like this is one row, but it's not linear. One row is one item. Oftentimes here you have this schema where they give you a very nice, clean manufacturer model number, but then they'll also tuck in here in remarks or elsewhere additional items that they need to support this water closet, which is a fancy name for a toilet.

01:35:49 - AlexH
So this agent, I finally got stood up and is working really, really well. It will go through and it decomposes and groups and itemizes. And now you can actually chat with it. So from just a user workflow perspective, being able to just comment or talk to your quote and have it make updates is pretty epic versus having to do this in the ERP, which is really brutal.

00:36:51 - Patrick Chouinard
<Q>Yeah, actually, so awesome that I really want to figure out — how do you manage to chunk the merged columns and merged rows?</Q>

01:37:00 - AlexH
<A>I spent for the first two months just trying to figure out the document processing of this and nearly gave up on the project because I couldn't figure it out. And then literally I just happened to meet these guys from Chunker, C-H-U-N-K-R. It does it off the shelf phenomenally, like best in class, beats everyone else. And I tried like all the others. There's like Xtract [tool:Xtract], Reducto [tool:Reducto], and I think those two tend to get the biggest kind of brand that came out of Y Combinator. But Chunker's ability to maintain table architecture and the text architecture is incredible. It honestly prevented me from killing this project. So I've had like 96, 97% accuracy in terms of column architecture, maintaining table architecture, all that stuff.</A>

01:38:00 - Patrick Chouinard
<Q>They're a SaaS provider, so basically you have to run Chunker from their services, correct?</Q>

01:38:08 - AlexH
<A>So they have, yes, a paid service. They have an open source, but I use their paid service. I hit their API, and then it sends back a long JSON doc, and then I use a Python function to fetch the specific HTML tables. And then obviously there's a lot of tables in here, so it's doing a regex to look specifically for this string architecture, to make sure that it's actually grabbing what it needs to, versus all these other tables that are irrelevant, before sending that to the agent.</A>

01:38:51 - brandon hancock
<Q>Alex, super fast question. I would be very curious, just like science — did you try out LandingAI [tool:LandingAI]?</Q>

01:38:59 - AlexH
<A>Same issues. I found that LandingAI was good at maintaining the columnar architecture, the relationships there, but the actual OCR — so a lot of the text was disturbed. A lot of the actual individual manufacturer model numbers would come out distorted, and then the rest of the process fails pretty heavily, because you can't effectively quote.</A>

▶ 01:42:00 - brandon hancock
Key advice: people who have converted ADK — like what I built out where everything is deployed to Agent Engine — deployed it directly to Cloud Run [tool:Cloud Run] instead, and they had a much more scalable and streamlined experience, where they could do streaming and more. So just to save you time as you're proceeding, make sure you go down the Cloud Run route instead of Agent Engine [tool:Agent Engine].

01:43:44 - AlexH
By the way, I'm non-technical. So I'm learning everything on the fly, building the plane and flying it at the same time. My next thing is this product catalog because the product catalogs — American Standard, for example, that's 2,000 rows on just the residential.

01:44:07 - brandon hancock
The next thing that's actually going to get really hard is that matching element. Like, okay, we've got this decomposed line item set that has raw text. How do you go and validate that against hundreds of thousands of options? And then it becomes a question of — because some of that is exact, like a perfect manufacturer model number schema that the engineer has given you. And then the next set of plans is like, the engineer will give you, I need a 1.28 gallon per flush toilet. And you're like, great. So using vector search versus a fuzzy match versus an exact match — that's where I'm moving next. I foresee this being pretty challenging. I have scoped out like three weeks just to try and figure this out.

01:43:27 - AlexH
I'm looking for a co-founder if anyone happens to know anyone. I'm based on the West Coast, so I'm kind of aligning towards someone in person, but open to any conversations.

▶ 01:45:00 - brandon hancock
If you want to do a post in the community, I would be very happy to comment it, post it, pin it — this is a very cool project, would love to do whatever I can to help you find a co-founder.

---

<!--SEGMENT
topic: Automated PR Review Tools and AI Impact Measurement
speakers: Hemal Shah, brandon hancock, AlexH, Patrick Chouinard
keywords: CodeRabbit, Factory AI, Droids, PR review, GitHub, automated code review, AI productivity metrics, lines of code, sequence diagrams, Gemini code review, impact measurement
summary: Hemal asks for recommendations on automated PR review tools and how to measure AI's productivity impact for leadership. Brandon demos CodeRabbit, which provides PR summaries, sequence diagrams, and inline fix suggestions with code snippets. Alex recommends Factory AI's Droids package (free trial up to 20M tokens). The group debates meaningful AI impact metrics, concluding that lines of code is a poor proxy and that problem-solving velocity and revenue correlation are better indicators. Patrick offers a qualitative heuristic: the more questions an employee fields, the more valuable they are.
-->

01:20:23 - Hemal Shah
<Q>I've been looking into measuring the impact of AI for my company — how do we measure productivity and all that. And even before that, besides vibe coding, when we create a PR, I was looking into how we can do automated PR review and post comments and all that. Cursor's BugBot is something I was trying, but wanted to pick the brain of this panel — are there any recommendations for automated PR reviews?</Q>

01:20:33 - brandon hancock
<A>CodeRabbit [tool:CodeRabbit] is my personal favorite right now.</A>

01:21:13 - brandon hancock
So like, this was a PR a few weeks ago, we were working on making the calendar page better. Mostly UI changes. Nothing wild, just some updated logic in ShipKit to make it easier to check for upcoming events. And then you can see here, it gives you an update of the walkthrough. Like, here's what changed. It gives you a summary of all the key files that were changed. It does some cool sequence diagramming, and then usually if there's something wrong, it will start to list out, here's what I think is wrong, here's what you should do instead. It generates the code snippets for you to fix it.

▶ 01:22:24 - brandon hancock
If I was you, I would try three or four of them at the same time, just so you can see them side by side. It's like hiring new employees. If you can hire three guys at the same time and be like, clearly guy number two is outshining the rest, I'm going to hire him. So if I was you, I would just one month pay for three, and then use that going forward.

01:22:52 - AlexH
<A>So this is an automated package you can download from Factory AI [tool:Factory AI] from Droids. They have it on their GitHub, and I actually haven't used it yet, but I've heard from a couple of people now that it works really well, and it doesn't require — they have a free trial that allows for like up to 20 million tokens, and I've heard it's actually really good.</A>

01:24:01 - Hemal Shah
<Q>And besides that, to track the AI impact — you know, how fast a developer is progressing, number of lines of code written and all that — are there any tools, anything anybody's using to do that?</Q>

01:24:17 - brandon hancock
<A>So here's the fun part about what you're describing — you have to decompose the word impact. Because lines of code is so funny — I had this exact same discussion with my boss back when I was an intern, right out of college, and I was like, I'm writing so many lines of code, like, do I get a raise? And he was like, I mean, lines of code is just lines of code. He would come in behind me like, dude, I could actually get what you did done in a fifth of the lines of code. The true measure of progress is problem solved. The hard part is correlating code to additional revenue. Does the new feature bring more money? And obviously it also depends, like if you're a commercial product, what your entire funnel looks like. Software at the end of the day — did the customer achieve the thing that they wanted to do, and did the features help them do it faster?</A>

01:26:19 - Patrick Chouinard
Honestly, I would say if you want to evaluate the value of an employee, the more questions the employee gets, the more precious the employee is.

---

<!--SEGMENT
topic: Google ADK Evaluation and Agent Framework Roadmap
speakers: Hemal Shah, brandon hancock
keywords: Google ADK, LangChain, LangGraph, Claude Code extension, Cursor, deployment, Cloud Run, Agent Engine, Gemini 3, AgentKit, streaming, Next.js, framework flexibility
summary: Hemal asks whether Google ADK remains Brandon's top agent development framework. Brandon gives a nuanced assessment: ADK is still the easiest for local prototyping via the ADK editor, but deployment to Agent Engine is painful compared to AgentKit's one-click deploy, and Next.js integration is difficult. He previews upcoming LangChain/LangGraph master-class content and advises flexibility across frameworks. He also clarifies limitations of the Claude Code VS Code extension versus the terminal-based workflow, noting the two environments don't share conversation history.
-->

01:27:00 - Hemal Shah
<Q>One last question, Brandon — is Google ADK [tool:Google ADK] still your favorite agent development framework, or have you moved on?</Q>

01:27:11 - brandon hancock
<A>Yeah, so thoughts as of end of October. Key things — they haven't changed anything from last time. I still think it is the easiest to build local projects, because you have the ADK editor. Like, everything about it is phenomenal. I still am upset at this point that there's not a quicker way to actually do what AgentKit [tool:AgentKit] did, to where I just clicked deploy and it worked. Like, that hurts my brain that that is not there. So that's the main dislike, and the fact that it's very hard to actually use within a Next.js application. If they fix those two things, they will go back to number one.</A>

▶ 01:28:04 - brandon hancock
Now that version one of LangChain [tool:LangChain] and LangGraph [tool:LangGraph] came out, we'll be doing a new monster video on both frameworks. I think LangChain and LangGraph will probably become the new winner, especially if ADK doesn't pick up.

▶ 01:28:48 - brandon hancock
If you're getting into agents and you just quickly want to practice, there's nothing easier to learn and better to start building up proof of concepts than ADK. It's just that the deployment process is a monster right now.

01:29:29 - Hemal Shah
With AI, we have to always be ready to change our favorite tool set. Like, I love Cursor. I'm loving Cursor. But now with your recent video of Claude — if you are a hardcore developer, then probably. So I was trying that out. But CLI is still so hard for me to pick up. So luckily I found Visual Studio has a Claude extension [tool:Claude Code VS Code extension], which is kind of helping with GUI a little bit.

01:30:00 - brandon hancock
Seriously, really recommend getting that cheat sheet. So this is just like a brand new Cursor window open, but just doing the shortcuts that were in that cheat sheet. Whenever I open a terminal now, it pops up top. So I can type in Claude. And then I can split screen, and then I can open up files. So it feels like I'm doing Cursor, but I'm doing it with Claude Code. Because I mean, I'm the same as you — I love Cursor so much. It's just my wallet also loves not spending thousands.

▶ 01:32:35 - brandon hancock
Inside of the Claude Code extension, you don't have as much flexibility and control as the terminal version. And you can end up in a weird situation where if you were working on some task inside the extension, and you were opening it up the normal way in a terminal, you can't go back and resume previous conversations — they're isolated. If you start in the extension, you need to stay in the extension. If you start in the terminal, you have to stay in the terminal. They don't blend.

---

<!--SEGMENT
topic: Garron's ADK Canonical Library and Agent Memory Setup
speakers: Garron Selliken, brandon hancock
keywords: Google ADK, Memory Bank, MCP server, GitHub, RAG, Gemini gem, Cursor rules, canonical library, context drift, real estate, prototype, deployment
summary: Garron shares a breakthrough after months of frustration: he built an "ADK canonical library" by aggregating Brandon's YouTube video transcripts, Google ADK documentation, and sample projects into a Cursor repository with custom rules. This gave Claude/Cursor reliable context to generate working ADK code. He also got Memory Bank and a GitHub MCP server connection working, dramatically reducing context-setup overhead. His goal is a real estate coaching agent that extracts metrics from conversations and writes them to a database, with 150 existing clients as initial beta testers.
-->

01:48:14 - Garron Selliken
Well, it's funny for me to even be in this group, honestly, because I'm like, what I did today, you guys would be like, that's what you did today? And that's like, for me, it was an unbelievable victory as a non-technical person. I was able to take what I gleaned from last week and from your videos and realized that the main problem I was having was that I don't know what I'm doing as a programmer, and I don't understand ADK and I don't know where the examples that I would draw from are. So I was just leaning on, hey, can you make me this? And it would just make some piece of garbage, and it wouldn't work. And then it would kind of get it to work, and then it wouldn't work, and then I'd start over.

01:49:14 - Garron Selliken
So what I did is I went and took all of your videos and code and all of the Google Developer ADK videos and all of that code and all of the Google documentation. And I made a repository, and I put it in Cursor, and then created some rules from your videos for my resources. So I've got like 50 sample projects and the transcripts from your YouTube videos in there also. And then worked on a prompting thing with my Gemini gem [tool:Gemini Gem] off of your videos also and fed them those documents. So I created this workflow, and it actually worked.

01:50:38 - Garron Selliken
I decided to build an agent that would be more reliable, so I could have a RAG [tool:RAG], I could have a memory system, and I could connect it to the GitHub repository, so now I have something that's tracking what we're working on, so I don't have to spend an hour giving it the context just to even start something, which was so much friction I couldn't do it.

01:51:44 - Garron Selliken
So I put it together this week, and I built out the MCP server [tool:MCP server] to the GitHub and tested it today. I got Memory Bank [tool:Memory Bank] to work yesterday.

01:51:56 - Garron Selliken
Yeah, I was like, I'm like telling my girlfriend, I'm like, I got more done in the last three days than I did in three months.

01:52:04 - Garron Selliken
So I'm just trying to get a working prototype so I can actually interact with this agent in a way that it can relate to me along a use case and extract some information out and write it to a database. If I can do that, then I've got some — that's where all the value from the application would come from.

01:53:39 - brandon hancock
So the cool thing is, Garron, like I said, I know you said you're building over the next week for a demo. I would seriously love next week when you have a demo — would be happy to give honest opinion of, like, cool, so based on where you're at, you actually might be able to go to this, leverage all the core IP and infrastructure. And if you use it in this other way, it might be way simpler and help you get there faster.

01:55:28 - brandon hancock
I personally have clients already that I coach and a brokerage that I am embedded in. So I already have 150 people I can hand it to to say, okay, use this and give me your feedback. There's no risk. It's not like they're paying me and they're going to get pissed if it doesn't work.

▶ 01:56:47 - Prem
Making progress, getting the ideas out of your head into the computer, no matter which pattern you pick going forward or which approach — you've already made an insane amount of progress, and it's going to make anything else we do going forward easier. The worst thing to do is just have an idea and keep it in your head.

---

<!--SEGMENT
topic: LiveKit Latency Issues and Chart Generation in Agentic UIs
speakers: Morgan Cook, brandon hancock, Hemal Shah, Ty Wells
keywords: LiveKit, latency, self-hosting, KimiK, Chart.js, ADK state, agent tool, structured output, server-side events, Fathom, agentic charts
summary: Morgan asks about a LiveKit latency issue and Brandon references a prior session recording (July 22nd) where community member Maxim used KimiK on a separate platform as a workaround, including self-hosting LiveKit. Hemal then asks how to generate charts and graphs within an agentic UI. Brandon explains the correct pattern: have a specialist chart agent save structured output to ADK state rather than returning it through message text, then detect state diffs on the frontend to trigger chart rendering with a library like Chart.js.
-->

02:01:11 - Morgan Cook
<Q>A couple weeks ago we had talked about LiveKit [tool:LiveKit], and Ty, you had mentioned that maybe you had somebody that had used LiveKit? The main problem we're having is there's a latency issue, and I'm not sure if the solution is to separate the stack and put them on separate dedicated servers or what.</Q>

02:01:49 - brandon hancock
My name's Maxim. I'm trying to look it up real fast. I'm just looking through Fathom [tool:Fathom] real fast to see if I can find the video. July 22nd.

02:02:43 - brandon hancock
From my understanding, he had to use KimiK [tool:KimiK], which was fast, on a different platform to solve the latency issue. So he used KimiK plus something else.

02:03:00 - Hemal Shah
Yeah, so he had to self-host LiveKit. But it's in that video around an hour 51 is kind of when it happened. But you can also chat with the video too. He ran into the same issue and had to do a workaround.

02:04:00 - Hemal Shah
<Q>In one of the Google Agent Bake-off competitions, one of the other competitors had built a visualization agent to show charts and a few other things. My question is, if you want to have charts and different graphs in our UI, any recommendation on the markdown language or how do we generate it in the agentic world?</Q>

02:04:24 - brandon hancock
<A>So the kicker there is you actually are saving the chart to state, then inside of — what you then look for is the difference in state. So like, did the chart exist before? Does it exist now? Cool. It's a new chart, therefore I need to show it. And there's plenty of cool libraries inside of TypeScript. Chart.js [tool:Chart.js] is the main one that comes to mind.</A>

02:05:00 - brandon hancock
Your agent has to know what chart graph framework you're using and basically say like, all right, your job is to generate structured outputs, save them to state. Then what's really cool is that on the front end, whenever it's streaming back results, inside the message history, you can actually look at per-message state diff. So you can always see like, hey, did we update user chart? And if so, fantastic, I will display that user chart.

▶ 02:07:08 - brandon hancock
I would truthfully recommend to use state. Your life is going to be so much easier. In that same setup, have your chart agent save the result to state, and then just display it. Going through message text and parsing out markdown is one approach I would not recommend.

02:08:29 - brandon hancock
All right, guys. Well, if no other questions, I will call it a wrap. Thank you guys so much for hopping on on a Tuesday.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context (which was not supplied in this session):

- **brandon hancock** — primary host/facilitator
- **Patrick Chouinard** — recurring contributor, Gemini CLI and prompt editor demos
- **Tom Welsh** — web scraper demo
- **Paul Miller** — Cursor 2.0 discussion, business/hiring topics
- **Ty Wells** — cybersecurity scanner and in-person presentation app
- **Jake Maymar** — deep research, contracts, trigger.dev questions
- **Morgan Cook** — trigger.dev real-time, therapy app, Next.js 16
- **Hemal Shah** — PR review tools, ADK evaluation, chart generation
- **AlexH** — wholesale supply document processing pipeline
- **Garron Selliken** — ADK canonical library, real estate agent prototype
- **Prem** — hiring strategy, ShipKit organization template
- **Sam** — Azure Agent SDK evaluation, intern hiring
- **Adam** — OpenAI Agent Kit model-agnostic question, CS grad job market