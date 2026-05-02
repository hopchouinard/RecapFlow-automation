=== SESSION ===
date: unknown (transcript timestamps span 00:06:01–02:03:17)
duration_estimate: ~2 hours
main_themes: Google Gemini 3 / Project Anti-Gravity launch, ShipKit platform updates and roadmap, member project updates (Dung Beetle, holiday SMS raffle, dashcam analytics, AI video generation, multi-agent apps), self-hosting with Docploy, GitHub Copilot agent workflows, AI video content strategy, Trigger.dev for agent deployment

---

<!--SEGMENT
topic: Session Open and Cloudflare Outage
speakers: Paul Miller, Tom Welsh, abdulshakur.abdullah, Andrew Nanton, Patrick Chouinard, Ty Wells, alexrojas
keywords: Cloudflare, AWS, Azure, infrastructure outage, LLM, Anthropic, automated hacking, vibe-coding, security, script kiddies
summary: Participants join the call and discuss a major Cloudflare outage affecting large portions of internet infrastructure. The conversation pivots to Anthropic's published research on the first fully automated LLM-based hacker, raising concerns about AI-enabled security threats and the rise of "vibe-coded" insecure applications.
-->

00:06:01 - Paul Miller
Hello?

00:06:04 - Paul Miller
Hey Tom?

00:06:09 - abdulshakur.abdullah
Hey Tom, hey Paul. I'm on time.

00:06:13 - Paul Miller
Hey guys.

00:06:15 - Tom Welsh
Hey. Headphones on now.

00:06:27 - Andrew Nanton
I love love.

00:06:35 - abdulshakur.abdullah
Hey Andrew.

00:06:47 - Patrick Chouinard
Hey guys.

00:06:52 - Tom Welsh
Hey Patrick, you're nice and loud today.

00:07:01 - Patrick Chouinard
Yeah, I'm having a little mic difficulty. Hopefully the sound's not too bad.

00:07:06 - Tom Welsh
No, it's decent though.

00:07:21 - Tom Welsh
How'd you join today, Paul?

00:07:24 - Paul Miller
Pretty good. Sold a few issues overnight, so that was good.

00:07:32 - Paul Miller
I've got to open the door to the cat.

00:07:44 - Tom Welsh
Cats are a life unto themselves.

00:07:47 - Paul Miller
Yeah, we're here to serve them.

00:08:55 - Ty Wells
It's wonderful waking up to that Cloudflare issue.

00:09:00 - Paul Miller
This morning, that was beautiful. Jesus.

00:09:04 - Tom Welsh
I've been out all day and just missed it.

00:09:08 - Ty Wells
Oh, it's still sort of going on. There's still some lingering effects.

00:09:14 - Tom Welsh
What a nightmare. Infrastructure again, or security?

00:09:19 - Ty Wells
I don't know. I haven't seen an update on it yet.

00:09:26 - Tom Welsh
It's happening so regularly now with the major infrastructure sites.

00:09:31 - Patrick Chouinard
Yeah, it's kind of hard to think that it's only infrastructure because AWS [tool:AWS], then Azure [tool:Azure], then Cloudflare [tool:Cloudflare] — like, kind of the backbone of the internet.

00:09:43 - Tom Welsh
Fathom had one first.

00:09:45 - Ty Wells
They had one before those. Hosting providers had one. And so this is their second one in as many months, I think.

00:09:53 - Tom Welsh
It's almost like somebody's probing. That's my security-suspicious head on.

00:10:00 - Patrick Chouinard
<Q>Well, didn't Anthropic just post a paper about the fact that they had the first completely automated hacker using an LLM [tool:LLM]?</Q>

00:10:11 - Ty Wells
<A>Yeah, that was ingenious. The approach was crazy how they did it. But yes, they did. I believe we have so many more developers now — vibe-coders, if you will — that are just pushing and plugging and filling up these spaces. And the load is obviously different for sure. And as we know, all of the vibe-coders are delivering absolute perfection in terms of security.</A>

00:10:45 - Paul Miller
Absolutely.

00:10:49 - Paul Miller
And Ty, the day of the script kiddies has probably come and gone now.

00:10:54 - Ty Wells
Now they're vibe-coding script kiddies. Just throw it at the wall and see what sticks.

00:11:04 - alexrojas
It's good for your security app, Ty, you know.

00:11:11 - Ty Wells
I'm actually rethinking some things since that Anthropic [tool:Anthropic] release. I am trying to see how I can integrate that.

---

<!--SEGMENT
topic: Google Gemini 3 and Project Anti-Gravity Launch
speakers: Brandon Hancock, Dave Far, Tom Welsh, abdulshakur.abdullah
keywords: Gemini 3, Project Anti-Gravity, GPT-5, Cursor, parallel workflows, agentic IDE, code diff editing, flight simulator, ShipKit
summary: Brandon opens the main session by highlighting Google's launch of Gemini 3 and the new agentic IDE "Project Anti-Gravity." Dave Far shares a hands-on comparison with GPT-5, praising speed but noting the inability to edit diffs. Tom Welsh and others discuss the paradigm shift of parallel task execution and its implications for existing workflows like ShipKit.
-->

00:11:22 - Brandon Hancock
Sorry guys, I've been trying to talk. I was muted. All right, let's get this show on the road. So, very busy day in the world of AI. All things Google. Just out of curiosity, who's got to try it out yet on Gemini and Anti-Gravity? Anybody got to try it out yet?

00:11:49 - Ty Wells
No. Watched the video.

00:11:54 - Brandon Hancock
▶ Seriously, if you get a chance, I would love for you guys to try it out and let me know what you think. I think they're trying to make it as smart as possible. And this was the first model — it was doing work that took me two months to build out, like a flight simulator. It took me two months as an engineer when I just started out my career, and it took it two minutes.

00:12:51 - Brandon Hancock
I've surrendered. It wins now. Dave, if you want to go quickly, and then Tom, if you want to go right after, buddy.

00:13:02 - Dave Far
Sure. So I tried it out — Gemini 3 [tool:Gemini 3] on Anti-Gravity [tool:Project Anti-Gravity] — and I really liked the speed. The results were on par with GPT-5 [tool:GPT-5] with max thinking for me. So no improvement there, but also not worse, but much faster.

00:13:57 - Dave Far
I do hate Anti-Gravity. I like it. So I will plug it into Codex [tool:Codex] or Cursor [tool:Cursor]. It is actually already available on Cursor before Anti-Gravity came out a couple of hours ago.

00:14:14 - Brandon Hancock
Yeah, it's definitely neck and neck with GPT-5 model-wise, but the speed is the thing that blew my mind. I could actually try Cursor twice before GPT finishes once — or sorry, Claude [tool:Claude].

00:14:43 - Brandon Hancock
On the Anti-Gravity thing, it is a complete parallel mind-shift to everything else. But I work in parallel constantly anyway, so it suited my workflow. It's day one, so we'll see how it keeps going.

00:15:06 - Dave Far
<Q>So one thing — I still like to sit in the driver's seat. I opened the diff for the code changes and I wasn't able to edit those, and I really hate when that happens.</Q>

00:15:20 - Dave Far
<A>That's the case with Kiro [tool:Kiro] as well, and with the more agentic version of Firebase Studio [tool:Firebase Studio] when you use the prototyper. If I see the diff, please let me edit it.</A>

00:15:38 - Brandon Hancock
No, I totally agree. There are a few quirks and I think they're just going to fix it. But for day one, I really like where they're going.

00:15:47 - Tom Welsh
Yeah, so obviously the video blew my mind — you're jumping around so much because it's all done in parallel, you're doing multiple things. I've got a serial mind currently; moving it to parallel is the paradigm shift.

00:16:04 - Tom Welsh
But my other thought was, you did so much work for ShipKit [tool:ShipKit], and then this comes along.

00:16:13 - Brandon Hancock
Yeah. No, so that's the part I was playing with late last night. The main thing — I just needed more time. I really want to try the task templates inside of Anti-Gravity, just because they have their own concept of task. I want to actually try ours.

00:17:00 - Brandon Hancock
There's definitely, when I saw it, I was like, huh, okay, I see you Google. Let the little guys have some. It's definitely good.

00:17:23 - Brandon Hancock
Abdul, and then we'll go to normal call order right after this.

00:17:27 - abdulshakur.abdullah
<Q>Just to follow up on what Tom was saying — do you see a future for ShipKit? Because I imagine the AI agents are just going to keep getting better.</Q>

00:17:42 - Brandon Hancock
<A>Yeah. The main few things I see as core pillars for ShipKit: A, the AI docs — that is its own straight-up pillar. How we handle tasks, how we automate most workflows — at the end of the day it's prompt engineering, just applied software prompt engineering. Then there's the actual projects themselves: even if the model is the smartest model on earth, what happens if you want to start off with a certain scaffold or follow best practices? And then obviously, even if you are using these models and they're doing most of the work, it's still important to understand a little bit of why you're using the tools and how they actually connect. So that's where the course comes in. No one single thing will replace it.</A>

---

<!--SEGMENT
topic: ShipKit Server Issues and Platform Roadmap
speakers: Brandon Hancock, abdulshakur.abdullah, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: ShipKit, server scaling, trigger.dev, LangGraph, LangChain, voice agent, RAG template, Supabase, Next.js, roadmap
summary: Abdul reports being unable to load ShipKit videos, prompting Brandon to investigate a possible server capacity issue following a traffic spike from a YouTube video. Brandon then outlines the ShipKit content roadmap — trigger.dev (just released), LangGraph/LangChain, and voice agents — driven by community demand. New member Scott Rippey introduces himself and expresses interest in the LangChain content.
-->

00:19:03 - abdulshakur.abdullah
I did actually finally get a chance yesterday to log into ShipKit after kind of getting it even pre-launch.

00:19:17 - abdulshakur.abdullah
When I logged in, I couldn't see any of the videos or anything. It was just a little spinning wheel.

00:19:25 - Brandon Hancock
I think I need to bump to a bigger server. I can look at my traffic right now — it's because of the video. If you mind, send me a screenshot, though, that would be huge.

00:19:39 - abdulshakur.abdullah
I was on public Wi-Fi yesterday. Right now at work I'm locked down to the point where I tried to log into ShipKit and I can't even get to the website because it's restricted.

00:19:54 - Brandon Hancock
Okay. Let me know. I'm just curious.

00:20:01 - Brandon Hancock
All right, well guys, we will go through normal call order. If it is your first time, here's how we usually go about it — we go around the room, keep it to maybe eight minutes, so everyone has a chance to share a win or a question, and everyone chimes in and helps out.

00:23:01 - Brandon Hancock
Real quick, just to answer Mitch's question: is Anti-Gravity recommended to use? Does it work with the Task.md-based workflow? I have not gone deep enough into trying it with the task-based workflow because it's a competing concept. If you tell Anti-Gravity to make a task, it prioritizes its own task system. So I'm curious if we might have to come up with a different name so they're not competing. I just need to test it a little bit more.

00:23:46 - Brandon Hancock
The way they manage rules and memory, it is purely agentic — meaning it's kind of just like, well, I hope it learns the right stuff. It's supposed to get smarter as you use it, but it is different. I'll keep you guys in the loop.

00:42:54 - Brandon Hancock
Yeah, no, super happy to answer any questions. On the roadmap — the guys on this call and on our ShipKit calls have kind of picked the roadmap. So basically what the group needs has been determining what we build. Alex and a few other developers were all running into the problem of needing the ability to do step one, two, three, four, five, six. ▶ The best way to do that is with Trigger.dev [tool:Trigger.dev]. That's the one that literally just dropped yesterday. After that, we're going to go to LangGraph [tool:LangGraph], LangChain [tool:LangChain] — that was one of the biggest ones. Then Voice. That's the roadmap going forward based on popular demand.

00:44:22 - Brandon Hancock
▶ If you are wanting to go enterprise agents — build more complex agents or get hired in the space — LangGraph/LangChain has kind of become the norm. Every big company is using it. I think it's going to open up a lot of job opportunities for you guys in the group.

00:45:08 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
It seems like a steal of a price. Even without the pre-price, I think it's $3.99. If you've got templates and you're still adding them, and you're doing that call — that seemed like a pretty good value.

00:45:21 - Brandon Hancock
Dude, that's the goal.

---

<!--SEGMENT
topic: Tom Welsh — Dung Beetle Project Architecture
speakers: Tom Welsh, Brandon Hancock
keywords: Dung Beetle, DrizzleKit, SQLAlchemy, Python backend, Next.js, JWT authentication, API architecture, Vercel, Gemini 3, traveling salesman problem
summary: Tom Welsh shares that he has fully removed DrizzleKit ORM from his front end and migrated to a Python/SQLAlchemy backend architecture. Brandon contextualizes the decision for the group, explaining why a Python-only stack forces the backend to own all database operations. Tom also discusses JWT-based API authentication and his plan to stay focused rather than chase new tools.
-->

00:20:41 - Tom Welsh
Yeah, not too much this week. I've been working on my Dung Beetle project [tool:Dung Beetle]. I've completely removed the Drizzle Kit [tool:DrizzleKit] ORM from the front end now, and I've put it to a proper stack. So it's just going API call straight to the back end through SQL Alchemy [tool:SQLAlchemy]. That's all working really, really well now. I've literally just this second finished the complete removal of DrizzleKit from my front end. So I'm very happy with that.

00:21:14 - Brandon Hancock
Quick update, guys, just so people have context, because this is a cool edge case. Tom has gone deep in Python land, so his backend is entirely Python, which means DrizzleKit only works with TypeScript. So Tom was kind of forced to make a decision of which application is going to be in control of the database, managing the schemas, migrations, and everything else. ▶ Tom went with Python being the manager of all things related to the database. So SQLAlchemy — phenomenal choice. And now his front end will always reach out to the Python backend, and the Python backend is responsible for everything else.

00:21:57 - Tom Welsh
One of the big takeaways from that is that my database isn't on the front end, so no one can actually get to my database. It goes straight in with an authenticated JWT token to get to the back end to actually commit stuff. So a bit of testing on there, but I think that's pretty secure.

00:22:16 - Tom Welsh
I'm always trying to watch more ShipKit videos and I'm getting there bit by bit.

00:22:23 - Brandon Hancock
Yeah, please do. I just dropped a lot more on the All Things Worker SaaS. I've got a lot more coming this week. A quick thing on that, Tom — your traveling salesman problem, I would love for you to throw Gemini 3 at that. I would just like to see how it attempts to solve it, and please report back. I want to test this thing as much as possible.

00:22:45 - Tom Welsh
I'm trying my best to stay focused on Dung Beetle. There are so many shiny things I want to go pull and play on. So I won't get around to the traveling salesman problem, definitely.

---

<!--SEGMENT
topic: Alex Rojas — Client Contracts and ShipKit Deep Dive
speakers: alexrojas, Brandon Hancock
keywords: ShipKit, Worker SaaS, client proposals, consulting contracts, Pokémon video generator, AI workflows, YouTube Shorts, copyright, video automation
summary: Alex shares that he has been deep in ShipKit videos and is waiting on a client decision after submitting proposals. Brandon reveals his next project: building a Pokémon Natural Geographic-style AI video generator using the Worker SaaS template, targeting YouTube Shorts. The group briefly discusses copyright considerations and the viral potential of AI-generated Pokémon content.
-->

00:24:12 - alexrojas
Hey, what's up guys? Now I'm getting some FOMO for not looking at Anti-Gravity. I was too busy looking at the ShipKit videos, which are amazing, man.

00:24:25 - Brandon Hancock
Thank you, Alex. I appreciate it, buddy.

00:24:27 - alexrojas
I totally decided to look at ShipKit. And then I saw your videos and I was like, okay, I should know what you guys are talking about.

00:24:38 - Brandon Hancock
The Worker video, man — that's literally for you. I think you're going to really like it when they keep coming out.

00:24:49 - alexrojas
I'm doing the whole thing, going through the whole deep dive. Even for the creativity aspect — learning how to approach the design phase of any application in the future — so useful. So yeah, I've been absorbed by ShipKit.

00:25:11 - Brandon Hancock
Can I share something really quick with you guys? I think you might find it pretty funny. So here's what I want to work on next. We have a new project where we're building out AI workflows using ShipKit. And they're literally Pokémon videos, because these get on YouTube and Shorts and everywhere else — millions of views. So what I'm going to do is take the Worker SaaS template and convert it into basically a Pokémon Shorts generator.

00:26:14 - abdulshakur.abdullah
<Q>You don't have to worry about copyright?</Q>

00:26:17 - Brandon Hancock
<A>I mean, so far what I've seen, everyone on YouTube has been absolutely doing it. If you get a chance, go on YouTube and look up Pokémon Natural Geographic. It's like a full-blown thing, guys. These channels have existed for years. There's a whole fan club around it.</A>

00:26:51 - alexrojas
Regarding my project — I did send all the proposals. We had a call, and in that aspect I'm kind of waiting for their decision-making process. I think they just wanted to make sure with all the operations. And also trying to revive some old leads — have a couple of calls, maybe smaller projects to close the year. But yeah, that's why I'm glad I also have a ShipKit Worker now to start getting hands dirty.

00:27:31 - Brandon Hancock
Yeah, it's so funny in contract land, because when you're doing work, you can't focus on anything else. But then when you're like, oh my God, there's no work — it's like, I have to reach out to everybody. It's a constant dance.

00:27:52 - Brandon Hancock
Hey Alex, please keep us posted and rooting for that contract.

---

<!--SEGMENT
topic: Abdul and Paul — Client Website Strategy
speakers: abdulshakur.abdullah, Brandon Hancock, Paul Miller
keywords: Lovable, static websites, CMS, Claude Code, GitHub, client workflow, white-glove experience, ShipKit, automation, Wix
summary: Abdul asks whether to automate client website intake via a form feeding into Lovable, or handle it manually. Brandon and Paul both advise a proactive, white-glove client approach. Paul shares his own workflow: using deep research to benchmark competitors, prototyping in Lovable, pulling the project to GitHub, and adding a lightweight custom CMS built with Claude Code — turning static sites into manageable, value-added products.
-->

00:28:10 - abdulshakur.abdullah
Yeah, so I mean, I haven't had too much time to do any projects. I do have two small contracts where some friends just want me to put together some websites for them. I was wondering if it was worth it to go the automated Lovable [tool:Lovable] route — where I connect a form and it automatically sends it to them, they fill out the form, then it sends it to Lovable. Or should I just not bother and just do it myself?

00:28:44 - Brandon Hancock
<Q>What level of complexity are they shooting for? Is it pretty much like a CRUD website?</Q>

00:29:00 - abdulshakur.abdullah
<A>They're both looking for kind of the standard. I did pitch to one of them having an agent in the background, but I felt like the agent could be completely separate and not really part of the website.</A>

00:29:17 - Brandon Hancock
I mean, you could always, once they're wowed with the website, add more to it. Like, oh, by the way, you can have an agent that answers customer support. It is a very hard time nowadays to do just static landing pages, because technically if you just go talk to AI enough, you can do this. I mean, you could charge one or two grand as usually what I see for static websites, just to make it worth your time. ▶ The cool part is you could standardize the process — come up with potential copy, spin up seven variations for them in an afternoon, and they would have their socks blown off.

00:30:51 - Brandon Hancock
▶ How I would look at it: hop on a 30-minute call, be as proactive as possible. Cover six or seven different touchpoints. Give some prep items to them before the call — like, hey, I need you to find at least five different companies that you might like. And every time you give them a suggestion, literally just copy and paste that same suggestion into ChatGPT [tool:ChatGPT] agent mode and say, do this for my customer. So you're never just putting the work on them.

00:31:43 - Paul Miller
Yeah, no, I've had a couple of friends ask me about doing the same kind of thing. So I did deep research to compare what they're doing with their main competitors — built a briefing that combined both where they were coming from and what their competitors are doing. Load it into taking their existing site, repurpose it through Lovable, publish out of Lovable into a show, then pull it down from Lovable via GitHub [tool:GitHub] and own the project and own the updates.

00:32:57 - Paul Miller
▶ I added a simple CMS, so it took the static site out of Lovable, and then used Claude Code [tool:Claude Code] to build a CMS management just for the parts of their site that change. One of my customers runs a beauty salon, another publishes a lot of articles — so the base pages don't change, it's just the article pages, and the beauty side it's just the pricing and the services. So it's got a simple way to manage their services. It's really easy for them; they don't have to use Wix [tool:Wix] or other stuff. A nice little value add, and really quick in terms of proof of concept.

00:34:16 - Brandon Hancock
▶ One other thing I always like to think about: how serious do you want to take this? If it is your moneymaker, go all in — ShipKit-ify it, standardize the entire process from end to end. If you nail it for one customer, the next customer will take seconds. And then always ask yourself: if I was the customer, what would be a 10-out-of-10 experience? White-glove, basically.

---

<!--SEGMENT
topic: Ty Wells — Holiday SMS Raffle App
speakers: Ty Wells, Brandon Hancock
keywords: SMS, Supabase, mobile recharge, holiday promotion, Claude Code, Twilio alternative, smsevil.eu, Convex, Superbase billing, image overlay
summary: Ty Wells demos a holiday promotional app for his mobile recharge company — a Thanksgiving-to-Christmas-Eve daily raffle with SMS notifications, a winner claim page with selfie-plus-overlay functionality, and a backend admin panel. He explains using Claude Code to generate SMS integration documentation for a custom local SMS server. Brandon raises the question of Convex as a Supabase alternative and concludes he's not yet convinced to switch.
-->

00:35:34 - Ty Wells
Hey guys. Cloudflare was down, so I got a break and went golfing this morning.

00:35:52 - Ty Wells
I'm working on a project for the holidays for one of my companies — it's a mobile recharge — and we're doing a Thanksgiving through Christmas Eve promotion where we have basically a raffle every day.

00:36:28 - Ty Wells
Okay, so this is the promotion I'm putting on, called "Big Up Your Minutes — Holiday Double Deal." Basically, you double — if you put in $10, you get five winners every day, so it's possible you're automatically entered in. I do a lot of SMS back and forth to show you the different pieces of it.

00:37:00 - Ty Wells
I like this color scheme — and oh wait, it looks really similar to the ShipKit color scheme. I think I like it. Oh, now it makes sense. So it turns out sick. I love the little flashing. The border, the trim is beautiful.

00:37:30 - Ty Wells
So what happens is when you win, you get a message saying, hey, you won, here's a link. You click on that link, it takes you to a claim page where you upload a selfie of yourself, and then it overlays a winning image on you. So that's basically the flow. And on the back end, you can come here and see the winners. It overlays the logo, automatically puts a big "Congrats" on there, says what you won and so forth.

00:38:38 - Brandon Hancock
<Q>How much did you get to port this over from your previous stuff? Like the SMS part?</Q>

00:38:42 - Ty Wells
<A>Actually, I had Claude Code [tool:Claude Code] build me the SMS integration that I can take to another LLM and that's what I did. So I've got a document of the SMS integration. This is a custom SMS server that runs locally in the Bahamas. So it's not like a Twilio [tool:Twilio] — it's designed, I've got a custom called smsevil.eu [tool:smsevil.eu], if you're not familiar with it.</A>

00:39:29 - Ty Wells
Yeah, Supabase [tool:Supabase] for this one.

00:39:35 - Brandon Hancock
Dude, I think you and I probably have top 1% Supabase bills with the amount of projects we have spun out.

00:39:47 - Ty Wells
Oh my goodness, I see my bill every month and I'm like, I need to kill that database, and I still haven't done it.

00:40:00 - Brandon Hancock
Awesome question on Convex [tool:Convex]. The more I've looked at it, I don't see the current appeal to switch to Convex. I know Theo [tool:Theo] did a huge video on it. The only thing I really saw that I liked about Convex was the real-time database updates. But most applications we're building, that's not the biggest issue. ▶ I think I'm going to wait on the Convex train to see if it was just all hype because of Theo or if it's actually a good move. But I'm still keeping an eye out on it.

---

<!--SEGMENT
topic: Scott Rippey — New Member Introduction and Background
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Brandon Hancock, Mitch, alexrojas
keywords: Claude desktop, MCP, Supabase, OpenAI embeddings, semantic search, ElevenLabs, voice agent, RAG, real estate, Auth0, Cursor, Next.js, Netlify, Vercel
summary: New member Scott Rippey introduces himself — an ex-IT consultant turned video producer who has pivoted to full-stack AI app development. He describes building a custom RAG knowledge base with semantic search, a voice agent using ElevenLabs, and a real estate brokerage chat agent. Mitch asks follow-up questions about his client pipeline. Brandon encourages Scott to join ShipKit and highlights the upcoming LangGraph content as particularly relevant.
-->

00:41:24 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Yeah, I'm new here. I kind of was in the group for a while but not really in it. I figured I'd give you a little background because I was looking at ShipKit. So like, I'm an ex-IT consultant — was in that industry for a long time, but I was kind of doing video production for about eight years full time, kind of switched. And then this year I kind of did a 180 again. And now I'm actually full time, kind of just on my own doing AI business automations, full-stack apps. I don't know how to code, but I understand tech stacks and the language and how it all works.

00:42:06 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I'm in Claude Code [tool:Claude Code] on Max 200 and Cursor IDE [tool:Cursor] and doing a lot of GitHub [tool:GitHub], Netlify [tool:Netlify], Vercel [tool:Vercel], Next.js [tool:Next.js] stuff, Supabase [tool:Supabase], and some Eleven Labs [tool:ElevenLabs] stuff.

00:42:19 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I was looking at ShipKit because I noticed you're a lot on the Google side, which I haven't really messed with in the coding space. I would love that voice agent template if you decide to do that.

00:43:49 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I've already developed a custom thing for myself where I built an MCP [tool:MCP] to Supabase from Claude desktop [tool:Claude Desktop] with edge functions to use OpenAI [tool:OpenAI] for embedding. But then I made a UI that has semantic search — I can browse, upload docs, and I have a whole voice agent with ElevenLabs that's my voice, completely custom. So I'm good on that. I'm actually interested in seeing some of the LangChain stuff, so it'd probably be good for me to see some of what you guys are doing with other things I haven't touched.

00:48:00 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I've done customer portals for people where they can schedule, pick calendar stuff, do requests, things like that. I've done a real estate brokerage office — we built a chat agent that has their own custom RAG [tool:RAG] knowledge base for real estate agents for their office, where it's a closed ecosystem, all of their own information. And it'll also give out some closed forms that they can send to the team.

00:48:40 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Yeah, so it's weird because my network kind of turned into the same network. Some of it was clients I had through video. Some of them are people I know through video who don't do AI, and they're like, hey, I've got a client that needs this.

00:49:33 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I knew I had to stop taking video clients and kind of tighten it up, because I really needed to dive into the coding part. After about six or seven months this year, now it's making money.

00:46:43 - Brandon Hancock
▶ I think it's cool that you're coming in with a background in something else — security, production — you are coming in with a ton of external skills, and now you get to apply the magic of AI and coding. That's the lottery ticket right now, because you can build solutions for your exact avatar.

---

<!--SEGMENT
topic: Paul Miller — Docploy Self-Hosting and Unit Testing Debate
speakers: Paul Miller, Brandon Hancock, Tom Welsh, Morgan Cook
keywords: Docploy, Vercel, VPS, Docker, GitHub CI/CD, Coolify, DigitalOcean, Hostinger, Kubernetes, reverse proxy, certificate management, unit testing, Maui, C#, SQLAlchemy, SOC 2
summary: Paul Miller introduces Docploy as a self-hosted alternative to Vercel, allowing developers to manage their own infrastructure stack — including reverse proxy, certificate management, and multi-service deployments — on any VPS provider. He contrasts it with Coolify and explains how Hostinger and DigitalOcean have invested in it. Brandon raises SOC 2 compliance questions, and Tom plans to use Dung Beetle as a test case. Paul also vents about a CTO who refuses to adopt AI-assisted unit testing.
-->

01:02:00 - Paul Miller
Hey guys. So I'm having lots of fun. Cursor 2 with Composer — what a model. It's saving money. It's bloody good. But in Claude Code, I've made the full jump. I'm saving money. No more $1,200 bills. Thank you very much, Brandon.

01:02:41 - Paul Miller
I had to attend our annual conference — three days of getting customers across the line from breakfast to drinks late at night. So I kind of lost a week last week. But I got a few new customers, so that was good.

01:03:18 - Paul Miller
Having fun and games with my CTO. Apparently, unit testing is something that business analysts should do. Not developers. So I have a special elongated board meeting at two o'clock to raise with my board colleagues that it is not my job, given I'm not the CTO, to come up with that. And that's what AI is for — to help you with unit testing and building the tests.

01:03:54 - Brandon Hancock
▶ We are firm believers in unit testing the core components of your application that make or break the app. I actually can't show it because it might have sensitive stuff, but long story short, it's a PII detector — one of the most core components of the application we're building. It allows users to say, hey, the PII detector detected a false flag. Every time it goes to a form, if it really was a true false flag, add it to the database as a whitelist, and then unit test. Why this is so important is because sometimes by fixing one PII test, we break another. For very critical components, I have like 700 tests for one function. It's a must.

01:06:09 - Paul Miller
I got really excited in the last few days. The question I had — and I posted it on the forum — is if you don't want to use Vercel [tool:Vercel] as the environment to launch your Next.js and all the cool apps we're building, how can I self-host that on my own VPS stack? So I went down the Docploy [tool:Docploy] path. And bloody hell, it's good.

01:06:49 - Paul Miller
▶ Basically, Docploy sets up a stack that's like your own Vercel. So you can go out and pick a VPS host — or even a physical host — and say, I'm going to divvy it up and have all of my dev applications or prod applications combined. It'll basically do the Vercel thing for you. Why would you go for this? You'd go for it because you then have no dependency on paying Vercel or Amazon or Google. You just say, where's the VPS host that I want? And you can always auto-scale the underlying VPS host and run all of your sub-microservices by customer, by project. It uses Docker [tool:Docker] and ties back into GitHub [tool:GitHub] — so you push an update through GitHub, it auto-refreshes through to the apps being hosted.

01:08:13 - Brandon Hancock
This is awesome. As you guys saw, Cloudflare went down, which I think messed up AWS. So it would have been awesome if you were agnostic right there and had not only serving from GCP [tool:GCP] but also serving from AWS [tool:AWS].

01:08:51 - Paul Miller
You cluster as well across multiple, so you could have a primary and a backup site and move your stuff around. It does all the reverse proxy, transport and security layers, certificate management, resiliency, backups — wrapping it into one neat box.

01:09:14 - Paul Miller
There are a few open source tools that do this. Have a look at the YouTube I put on the forum — the guy spends about 15 minutes setting up a host and pulling it from his GitHub. It takes you end to end through the steps. You might say, well, I want a Postgres server, I want a FastAPI box, I want a primary front-end server — and you get all that in the code, and you can just tell the code to include Docker Compose [tool:Docker Compose].

01:10:15 - Brandon Hancock
Yeah, this is genuinely very, very cool. Normally you would have to use Kubernetes [tool:Kubernetes] to basically build your entire cluster. And God, that's so awful — you basically have to be a full-blown infrastructure engineer. They've kind of made that way easier.

01:11:01 - Paul Miller
My engineer, my CTO, delivers a very stable network, and I'm really grateful as a CEO that it's not falling over every day. But when we can't move at the pace that our competitors are moving at and the pace that our customers are wanting to move us at, this is a problem.

01:13:20 - Tom Welsh
Yeah, I was just going to say — backing Paul up there — this is like a game changer for a lot of us. We're not paying people like Vercel to do what we can do ourselves. That's always been my thing. Vercel's great and it's easy to get going, but if a tool like this comes along that can do the same job, I'm more than happy to run that kind of stuff. ▶ I'll be moving Dung Beetle from Vercel to that as my test case.

01:14:11 - Morgan Cook
Yeah, I was previously looking at Coolify [tool:Coolify], but same kind of concept. I'm using Vercel and Supabase as a launch. Once I get it going, I really seriously plan on moving my stuff to a VPS of some sort, just to minimize costs across multiple projects.

01:14:45 - Paul Miller
▶ This does compete with Coolify, but you'll find it's a lot more logical. It just kind of makes sense. It's like you logically look at the certain places and you can work it out. It's a really clever UI/UX for managing something that is really complex when you think about what it is.

01:17:41 - Paul Miller
Hostinger [tool:Hostinger] and DigitalOcean [tool:DigitalOcean] have invested in it, because they can see that it so challenges their model that they have to adapt to it, otherwise they're going to miss out on revenue. So if you go to Hostinger, there's a .ploy deployment server — you can say, I want an Ubuntu host with Docploy default installed, and then just add my stuff on top of that.

01:18:15 - Brandon Hancock
I'm hooked. And real fast, bringing back to ShipKit — as I start to go through this infrastructure journey myself, because obviously I'm using the RAG template [tool:RAG template] — that's the startup we are working on. We're about to have to go full-blown cloud in 2026. So as we go deeper into cloud stuff, I definitely want to add more cloud stuff to ShipKit. ▶ You guys get the starter — Supabase, Next.js, crank out the app, verify it — and then when you have to go more enterprise, hey, there's some more infrastructure stuff there too.

---

<!--SEGMENT
topic: Patrick Chouinard — GitHub Copilot Agent Workflows and Neuro Elix Research System
speakers: Patrick Chouinard, Brandon Hancock
keywords: GitHub Copilot, VS Code, Azure DevOps, Confluence, Atlassian, parallel agents, Perplexity, Gemini CLI, OpenRouter, GPT-5.1, ChromaDB, SQLite, vector database, Milvus, ShipKit, Codex, Warp
summary: Patrick describes building a fully automated GitHub Copilot training update pipeline using parallel markdown-based agents that generate Confluence documentation, team messages, and training material updates from VS Code release notes. He also shares Neuro Elix — a Python-based AI research system using Perplexity for pre-filtering, Gemini CLI for deep research, and GPT-5.1 via OpenRouter for cross-research insights — now evolving toward a self-directing cognitive system with a local vector database.
-->

01:19:53 - Patrick Chouinard
But basically, I've just spent my weekend browsing the Discord server, finding questions, and just feeding them back into my AI assistant and trying to figure out what's the best solution that would cover the most problems.

01:20:23 - Patrick Chouinard
As for what I've been working on — obviously there was a big update in GitHub Copilot [tool:GitHub Copilot] this last week. And since I have a big class coming up, I had to reinvent the training material again. Three days before the training, obviously. So I actually leveraged the latest functionality of GitHub Copilot to update GitHub Copilot training.

01:20:46 - Patrick Chouinard
They've put some new functionality for agent management. I love how they did agents, actually, because they're pure markdown files. They used to be called chat mode, but they've migrated it to agent. And one of the tricks they've pulled is the ability to have hand-off between agents, just as part of the YAML front matter of the agent markdown file.

01:21:15 - Patrick Chouinard
Basically, I have an agent that takes the release note from VS Code [tool:VS Code] — I've actually cloned the repo called VS Code Docs Main, which feeds the Microsoft website documentation for VS Code. So I've cloned the repo locally, and now my agent goes and grabs the release note and creates a version to be published on our internal Confluence [tool:Confluence] server with all of the new functionality, stripped of everything we don't use — because we use Azure DevOps [tool:Azure DevOps] and Azure Repo [tool:Azure Repo], not GitHub internally.

01:22:25 - Patrick Chouinard
And then I spawn three parallel agents with parallel hand-offs. One creates a bunch of team messages to be published at intervals during the month about the new functionality. Another one prepares my agenda for my committee meeting with the administrator of the platform to know what they need to activate and deactivate. And the last one actually updates the training material, which is also in Markdown hosted in Confluence, leveraging the Atlassian [tool:Atlassian] MCP — it does the update automatically on the website.

01:23:04 - Brandon Hancock
Patrick, I'm just going to say it — if you left, how many people would they have to hire? You're doing it perfectly. Every company needs a Patrick right now to make the company move faster.

01:23:13 - Patrick Chouinard
At that client site, we have about 350 developers, and they have one trainer for GitHub Copilot. So I need to maintain the documentation, maintain the training material, and give the training at the same time. So I don't have a choice. I have to have agents work for me.

01:24:48 - Patrick Chouinard
Outside work, I also have the project I showed up two weeks ago, called Neuro Elix [tool:Neuro Elix] — basically my Gemini CLI [tool:Gemini CLI] researcher. Now it's a complete Python backend, and I migrated it to Python and Piper, and created it inside of a container, so it's no longer running on the machine directly.

01:25:21 - Patrick Chouinard
I'm creating now a pre-processor, because I realized I was burning a lot of time with Gemini CLI just to do research on subjects that might not have evolved since the day before. So what I did is now I'm using Perplexity [tool:Perplexity] to do a front search, just to say, is there news in the last 24 hours about a list of subjects hosted in a database? If there is, then it actually calls the Gemini CLI workflow to do the full research and full analysis. Then I call, through OpenRouter [tool:OpenRouter], a GPT-5.1 [tool:GPT-5.1] for those types of cross-research insights.

01:26:47 - Patrick Chouinard
All the development has been going on between Codex [tool:Codex] for the document to create all of the specs, and a mix of Warp [tool:Warp] and Claude Code to do the actual code development — all of that done with pieces of ShipKit that I've repurposed, either from the actual template or from the markdown documents.

01:27:46 - Brandon Hancock
▶ One cool concept Patrick just absolutely crushed: he identified a bottleneck — the model was looking up stale information. The cool trick Patrick applied is he added what I'll call seed data. Seed data is high-quality information as a starting point — like a really cool way you can see data pre-processing. Those are the two things I always like to think about when working on a problem: is there anything I could do that would make the main objective work better?

01:29:23 - Patrick Chouinard
Last thing I've started to work on is accumulating all of what I search every day inside of a local vector database — not to search it further, but something for the agents themselves to research to see their own evolution in the information they gather every day, and maybe find new stuff to research based on that. So basically, I wanted to make the entire system evolve naturally.

01:30:00 - Patrick Chouinard
I've also started another piece where it starts to ideate new projects based on the new information it searched on. I want to get it to a point where I could automate it to a very light proof of concept with the ShipKit infrastructure behind it.

01:30:32 - Brandon Hancock
<Q>Are we doing ChromaDB [tool:ChromaDB]? What are we doing locally for your vector store?</Q>

01:30:38 - Patrick Chouinard
<A>It's very simple — it's Milvus [tool:Milvus] just on SQLite [tool:SQLite]. Just a very quick, nothing very special. Maybe I'm going to migrate it further down the road, but right now the idea is I just want the framework to be in place. It's becoming a cognitive process more than just a search assistant.</A>

01:31:08 - Brandon Hancock
▶ This is kind of like rewind five years ago, everyone was making their own Notion to have a second brain, but this is like a second brain times infinity. I literally have a Brandon Hancock file — for every project I ever do, every YouTube, every business, ShipKit — everything is in there, it's all accessible. Cannot recommend setting up your own AI workspace on your computer with context. You will move so much faster.

01:32:03 - Patrick Chouinard
Wait — Gemini CLI running Gemini 3.0. I just set it up, I activated a preview, and it's there.

01:32:26 - Brandon Hancock
You can only use Gemini 3 Pro in the CLI with an API key — quick heads up. You either have to be on the $200 plan or Ultra, it said, to actually start using it.

01:32:47 - Patrick Chouinard
It's actually in Spark, it's actually in GitHub Copilot, and it's actually in Cursor already, so.

01:32:53 - Brandon Hancock
Okay, please let me know — I'm curious if they lied to me.

---

<!--SEGMENT
topic: Mitch — AI Video Generation and Facebook Content Strategy
speakers: Mitch, Brandon Hancock, abdulshakur.abdullah, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: N8N, Dropbox, AI video, Facebook, ElevenLabs, VO, Pokémon, pattern interrupt, meme culture, TikTok algorithm, content nodes, video automation, binary data, Worker SaaS
summary: Mitch shares that his AI-generated Facebook videos are approaching 250,000 views across two recent uploads, and discusses an N8N workflow issue with binary data memory allocation that he resolved by switching to Dropbox API links. Brandon and Mitch brainstorm a pattern-interrupt angle for the Pokémon video generator — using dark humor, meme archetypes, and narrator voice to differentiate. Abdul asks about political satire content viability, and Mitch explains TikTok's primary vs. secondary content node structure.
-->

00:53:38 - Mitch
It's good. The videos are doing pretty well. I'm sitting close to a quarter million — a quarter million views for the two recent ones that I launched. Need to make some more videos, man.

00:54:02 - Mitch
<Q>Can I ask for the topic if it's not too provocative?</Q>

00:54:09 - Mitch
<A>Yeah, one of them is a guy building a fence in his property and the cop is like, what are you doing here? He thought he was the worker, but he's really the landowner. And the other one — yeah, it's just all this silly stuff. But no, it's really good.</A>

00:54:22 - Mitch
Built out the workflow. I realized the issue I was running into in N8N [tool:N8N] last call — when you download a bunch of binary data, it takes up the memory allocation that N8N gives you. That's why I was just passing null or undefined. So then I figured out I could do the API request right to Dropbox [tool:Dropbox] to then just send them the link for them to download. But now it's not going through on all of them. So definitely going to need to integrate the ShipKit Worker SaaS and then build the workflow for all those different errors and handling.

00:55:15 - Mitch
Depending on how far you go with this video generator, I'll definitely add in the queuing process as far as creating the idea and all that other stuff. Definitely collab on that if you want.

00:55:30 - Brandon Hancock
Dude, yeah, my goal — mine will be like, it does the thing, but you are taking it to the top 1%. I'll get you 80% there with the new template and then you just take it to 100%.

00:51:43 - Mitch
Are any of them using ElevenLabs [tool:ElevenLabs] for the voice, to commentate the clips? Is anyone currently doing it in the marketplace for the videos that you're making?

00:52:05 - Brandon Hancock
I don't know. They don't tell you what they're using. They just make the videos.

00:52:12 - Mitch
But anyways, yeah, I'll definitely help you out. I think there's another thing we could vector in for, which is memes and then satire. I think the narrator should be, like, purposely very gruff — like, "the wild Pikachu, you know" — and have that narrative piece. And then I think the one thing that they're missing is the meme culture. I would try to figure out what are each of these archetypes and incorporate that as far as memes.

00:52:47 - Brandon Hancock
▶ You want a pattern interrupt. Like, you could go more dark and gloomy with it. Man, Pikachu's having it rough. Pikachu's in the inner city. He's struggling to get by. You can go any angle with it, and people are just like, what the heck am I watching? I don't know what I'm watching, but I'm going to keep going.

00:53:29 - Mitch
Giving it the semantic meaning behind electric type, ghost type, all those different Pokémon types, and putting them in those moods and then matching those moods with memes. I would want to brainstorm with you on this one.

00:57:45 - abdulshakur.abdullah
<Q>I was thinking about a viral-type video of kind of everything that the Democrats and Republicans are doing, but instead of them — just animals, so like Animal Farm. How would I make that? Would that go viral or would that be too much in the political so it would kind of get flagged and not shown unless I pay a bunch of ad money?</Q>

00:58:24 - Mitch
<A>I mean, realistically, you just need to go one side or the other side. You can't really do both sides. I say it's like commentary number one. So if you were to do it, I would separate them, because then you'll vector your page for two different kinds of people and that would work.</A>

00:59:08 - Mitch
I wanted to do a page about a bunch of people getting fired just because it does well. Like, all these people on TikTok [tool:TikTok], they're crying, they got fired. And when I catered my feed on TikTok to it, what you'll notice is there's the primary vector or primary node and the sub-nodes. So I was on a sub-node — meaning when I catered my feed to a bunch of people getting laid off, it then kind of navigated me to a certain political area of content. That's when I realized, oh, I'm optimizing for the wrong thing because it's kind of like a gateway drug for this thing is how TikTok sees it.

01:00:19 - Mitch
▶ You kind of need to see the stuff that you're doing and then try to find other videos like it, cater your feed, and then see: is this a primary node, secondary node? And also, how are they currently getting fed this information already? Because there's the idea, but there's really just what the person wants at the end of the day.

01:01:00 - Brandon Hancock
Here's what I'm pumped for — fast forward, it's going to be need to crank out some new stuff. I'm pumped for all of us to just start experimenting. Like, hey, I'm just going to try it for a week. Let's just see what happens. You might pay like 20 or 30 bucks to actually make a video, but hey, it's worth a shot just to see. It's a very cool experiment.

---

<!--SEGMENT
topic: Morgan Cook — Dashcam Analytics Project
speakers: Morgan Cook, Brandon Hancock, Paul Miller
keywords: dashcam, FFmpeg, GIS, geocode, Raspberry Pi, Starlink, heat maps, route analysis, delivery companies, video storage, OpenStreetMap, Supabase, Worker SaaS
summary: Morgan Cook describes a dashcam data analytics project that uses FFmpeg to extract frames and GIS metadata from dashcam footage, enabling searchable travel history and route anomaly detection for businesses. He outlines a Raspberry Pi-based auto-sync solution and discusses heat map visualization for identifying driver route deviations. Brandon and Paul offer technical suggestions including FFMPEG frame extraction, GIS plotting with OpenStreetMap, and AI-generated anomaly reports.
-->

01:33:54 - Morgan Cook
So I've been actually really busy with my labor job instead of my AI stuff. I haven't really done much in the last couple of weeks, and I'm looking to move and find a new apartment, so it's been a couple of busy weeks doing things other than AI.

01:34:15 - Morgan Cook
I did, however, take a look at your videos for the Worker SaaS [tool:Worker SaaS], and I like the content you've done there.

01:34:36 - Morgan Cook
I haven't done anything with it yet, but it's right down the path of two of my projects that I have coming up. One of them is about consuming dashcam content and making that more usable for the end user. Right now, most people don't use their dashcam data at all unless they get an accident.

01:35:00 - Brandon Hancock
We've actually, maybe it was the end of last week, whiteboarded with Alex, because he's having to do video analysis. We actually strategized together how to reduce cost by using a combination of FFmpeg [tool:FFmpeg] plus just regular image analysis. So you've taken a video, use FFmpeg to cut out images.

01:35:39 - Morgan Cook
One of my plans for that project — the biggest problem is actual storage space and locating information that is unique. If I drive the same road every day, I don't need that video unless something specific happened on that trip. My plan was to use FFmpeg, and there's another tool that strips out all of the geocode data and the GIS information with all the location info. So I'll pull that out and pull snapshots every 15 seconds or 10 seconds or whatever the user sets it to. That'll cut the storage down by at least a 30th.

01:36:37 - Morgan Cook
Then the video would be saved and searchable. And one of them is the fact that all the dashcam devices are Wi-Fi access points — they do not connect to an access point, they are the access point. And the problem is people get that confused. So my plan is to have another device, like a Raspberry Pi [tool:Raspberry Pi], on my network with two antennas, that as soon as I get home, I can just push my Wi-Fi button. The Raspberry Pi is going to be watching for that access point to appear, automatically connect to it, sync all the files off, and upload them to whatever the site is, process the information in the background so that they can at any time go search anything about what their travels have been.

01:37:39 - Morgan Cook
And for a business side of things, one of the biggest problems that delivery companies have is their drivers taking routes that are not part of their path, and offloading some packages that weren't meant to be offloaded. So there's the potential for some good money coming out of that.

01:38:17 - Brandon Hancock
Quick things I want to throw at you: the actual process of passing in video — if you do want to be able to ask questions about a video, that is more expensive, because you're basically embedding the video. Gemini [tool:Gemini] probably has the best models for that right now. If you're trying to do it at scale, it is on the more expensive side. You can adjust the quality and resolution to reduce some of the cost.

01:39:00 - Morgan Cook
So of consuming the video data in the AI — the AI would be used primarily to process and analyze the GIS information that's stored within the video. The video would be stored somewhere they can access it, time-coded with the GIS info. So they can ask, like, when was I ever on this street or at this location? It can pinpoint all the videos where they've been there.

01:40:35 - Morgan Cook
So Paul, were you working with some mapping stuff and plotting routes?

01:40:42 - Paul Miller
Yeah. So I was using a combination — Google have got paid services, and then they've got a free stack for doing that. So working the shortest possible distance, how long it takes given traffic at a certain time, how do you prioritize the routes.

01:41:11 - Morgan Cook
This is all actually post-route information that I'm doing. So I already have the plots. I just need to plot them and show them on the map.

01:41:20 - Paul Miller
So now I reapplied it back to the OpenStreetMap [tool:OpenStreetMap] standard. So then you could show a little snail trail.

01:41:43 - Brandon Hancock
▶ Man, you get heat maps. You could even have it make a report — literally have it make an analysis after you make the heat map to say, here's the odd behavior you might want to ask the employee about. So the person doesn't even have to visually go find what went wrong. Like, hey, what is odd? Just go ahead and tell them what's odd.

01:42:23 - Morgan Cook
It was really fun going through the first process with Patrick's little GPT tool on this project. It's been a fun project to start, but I haven't actually started coding it yet.

---

<!--SEGMENT
topic: Garron Selliken — Multi-Agent App Refactor and Deployment Planning
speakers: Garron Selliken, Brandon Hancock, alexrojas
keywords: ADK, Google AI Studio, Cursor, Gemini gem, multi-agent, router agent, digital twin, Trigger.dev, LangGraph, memory bank, MCP, GitHub, anti-gravity, agent deployment, ShipKit
summary: Garron Selliken, a nomadic developer currently in Austin heading to Mexico, describes his struggles refactoring a multi-agent conversation tracker app. He found success prototyping in Google AI Studio with Gemini 3, but faces challenges migrating to a stable codebase and planning deployment for 150 beta users in January. Brandon advises using the ShipKit digital twin markdown file as a north star for agent architecture, and recommends Trigger.dev as the deployment path, with LangGraph as a future option for more complex orchestration.
-->

01:43:40 - Garron Selliken
Well, I missed the last couple of weeks because — I don't know if I told you, but I've been nomadic for over two and a half years. I don't have a house or apartment or anything. I lived for a year on my motorcycle with Starlink [tool:Starlink]. And now I have a girlfriend, so we're heading to Mexico in her van. So we've cut my expenses down to basically like a thousand bucks a month.

01:44:30 - Garron Selliken
I'm in Austin right now. We've been snorkeling in this amazing spring outside of Austin for the day.

01:44:51 - Garron Selliken
I had a rough couple of weeks with AI, but it's coming back around. I was having trouble making the version one agent app of just a conversation tracker. I was using a Gemini gem [tool:Gemini] that I put six documents to, helping me create the prompts, and Cursor [tool:Cursor], which has my 40 example projects, all the videos, the live library of references, and then my project itself.

01:45:30 - Garron Selliken
I realized I kept adding to this one agent — it had RAG, it had persistent memory with memory bank, it had an MCP server connecting to GitHub [tool:GitHub]. So I was starting to add all these things. And I made maybe the mistake of saying, well, this seems like it should be more than one agent — seems like this should be a router with other sub-agents.

01:46:10 - Garron Selliken
So I got the idea to refactor everything and do it right. And to my astonishment, it did it. I created the prompt in the Gemini gem, we went back and forth between the examples until we had consensus, and then I said to refactor it, and then it started working and I just watched it sit there and work. I thought, there's no way this is going to work because I don't know what it's doing. And then it troubleshot two things and then the whole thing worked.

01:46:45 - Garron Selliken
I tested it, put up a whole front end and tested it. But then I think, well, this is easy. And so then I do my next project to refactor it — to tweak a bunch of stuff — and then the whole thing just floated into a million pieces.

01:47:07 - Garron Selliken
So I put it down for a few days. But then I woke up this morning, watched your two videos on Gemini and Anti-Gravity [tool:Project Anti-Gravity]. So I went to Gemini 3 [tool:Gemini 3] and I went to AI Studio [tool:Google AI Studio]. I took all my documents for the agent app that I'm building and just downloaded all the documents to it. I said, this is what I'm building, I want to mock it up. And it just gave me a great functional mockup. I mean, I have my version one working in that mockup environment now.

01:48:09 - Garron Selliken
<Q>Now the question is, how do I migrate that — which I am super happy with — from the AI Studio prototyping environment over to a stable codebase? And then also, how do I deploy it? I've got 30 beta agents waiting for me and then another hundred — 150 agents that in January will start using it.</Q>

01:50:34 - Brandon Hancock
<A>So here's how I would tackle this. A few concerns: A, how many agents do I have, and how complex are they? If it is multiple agents — like seven agents with a very particular workflow — I am a little hesitant to pull that out and start from scratch elsewhere. However, if there's like two or three agents, that's so portable. Out of curiosity, where are we at agent-wise?</A>

01:51:36 - Garron Selliken
I think there's just going to be a router and three agents. So maybe four agents total.

01:51:43 - Brandon Hancock
▶ So that, thankfully, is safe enough to where it's kind of like — you have the router agent who delegates to the three sub-experts. This is a core foundational structure that is easy for these different tools to understand. If I was you, I would not be too hesitant to say, all right, I kind of want to start over. Here's this working from AI Studio, here is a new project, I want you to make our current project copy what's working in AI Studio.

01:54:01 - Brandon Hancock
▶ Big question for you, Garron — are you using the digital twin? That markup file that's in there? Because that's one of the most important ones to keep in sync. Here's how I would tackle the problem using the tools we have at hand. It sounds like AI Studio created something that was perfect. So what I would do is go, all right, AI Studio — here's a working set of agents, they're crushing it. What I would like to do is migrate this over to our digital twin. What's so nice about our digital twin, it's just markup. It's super easy for the agent to read through and quickly make changes of like, no, no, no, here's how things should be structured. And the second we have that working, we then go, all right, we're going to make a new task where we're going to make our code reflect our digital twin.

01:55:26 - Garron Selliken
That's the secret sauce, because it helps keep things in check. Because if not, what's hard for the model is it has to understand the change, keep that in mind, understand the current state of all the agents across 10 different files, make changes, keep the change delta in mind, what's left — plus there's so much to keep up with. And the second you run out of context, you're hosed. So getting that markdown file as the north star — this is what you want to copy — it's so easy for the AI to go, am I here? No. Make changes. Am I here? No. Make changes.

01:59:11 - Brandon Hancock
▶ ADK [tool:ADK] right now — their deployment is still a pain in the butt. Beautiful for building out applications, iterating really quickly, testing locally. However, the part that begins to fall apart is deployment. Agent Engine, the core way to deploy agents in Google, they've just neglected it when it comes to ADK. So with that being said, what I would really recommend is Trigger.dev [tool:Trigger.dev]. You can copy over a lot of what you're doing with the prompt, the orchestration, and everything else, and bring it over to Trigger.dev. Trigger.dev will be your agent orchestrator, agent hosting, and do a phenomenal job. You get to watch it, it has built-in observability, they are crushing it.

02:01:40 - Brandon Hancock
Option two, if you have more time, we also have LangGraph [tool:LangGraph] coming out, but that'll probably be very beginning of January or February. So you have multiple options you can pick from.

02:02:27 - Brandon Hancock
So Biggi, to answer your question — I have not done a video about porting N8N over to ShipKit. But N8N, you can export your workflows to JSON. What's nice is it also includes the actual source code for what you're trying to do inside of N8N. And then inside ShipKit, there is something called the Task Orchestrator — basically what you could do is just say, here's my N8N code, I want to copy this, bring it into my application. Can you please break up these N8N workflows into tasks and workflows that can be used with Trigger.dev for this application?

---

=== UNRESOLVED SPEAKERS ===
- Dave Far (raw name "Dave Far" — not found in alias map)
- Mitch (raw name "Mitch" — no full name or alias provided)
- Morgan Cook (raw name "Morgan Cook" — not found in alias map)
- Garron Selliken (raw name "Garron Selliken" — not found in alias map)
- Andrew Nanton (raw name "Andrew Nanton" — not found in alias map)
- Ty Wells (raw name "Ty Wells" — not found in alias map)
- Biggi (referenced in chat only, never spoke on audio — no alias map entry)