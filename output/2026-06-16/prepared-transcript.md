=== SESSION ===
date: Not explicitly stated (weekly Wednesday meeting)
duration_estimate: ~88 minutes
main_themes: Personal loss and AI-assisted estate administration, Mythos/Fable model shutdown fallback strategies, member project updates (AI-native CRM for estate agents, KindMark positive-reputation platform, AgentOps home-lab nervous system, AI photo booth), diffusion model experimentation, adversarial AI prompting as business analysis tool, intent queue workflow for Claude Code

---

<!--SEGMENT
topic: Personal Loss and AI-Assisted Estate Administration
speakers: Patrick Chouinard, Ty Wells
keywords: Claude, estate administration, funeral home documentation, HTML timeline, government forms, bereavement workflow, AI productivity, context window, scanning documents, administrative automation
summary: Patrick Chouinard shares that he recently lost his mother and used Claude to process funeral home paperwork, government forms, and administrative tasks — reducing a two-month process to 48 hours. This segment highlights an unexpected but powerful real-world use case for AI in emotionally difficult administrative situations.
-->

[00:00:01] Patrick Chouinard: Hey, Ty.
[00:00:03] Ty Wells: Hey, Patrick.
[00:00:07] Patrick Chouinard: A little better than last week, let's say.
[00:00:10] Ty Wells: You were sick last week?
[00:00:12] Patrick Chouinard: No, I lost my mom two weeks ago.
[00:00:15] Ty Wells: Oh, I'm sorry to hear that. My condolences.
[00:00:21] Patrick Chouinard: Thank you, sir.
[00:00:23] Ty Wells: I know you used to do a lot with your mom, right? I heard you mention her a few times.
[00:00:28] Patrick Chouinard: Well, I was her caretaker.
[00:00:35] Ty Wells: How old was she?
[00:00:37] Patrick Chouinard: 88.
[00:00:39] Ty Wells: 88. It's a full life.
[00:00:41] Patrick Chouinard: Oh, yeah. No regret. It's not because you know a slap is coming that it's fun.
[00:00:48] Ty Wells: That's true. Yeah, that is actually true.

[00:01:00] Patrick Chouinard: And it's surprising how much — it sounds weird to say — but it's surprising how much Claude [tool:Claude], in this case, actually helped me for all of the administrative stuff.
[00:01:13] Ty Wells: Oh, no, that's helpful in that way. I was just telling my sister's daughter's boyfriend, there was something I didn't want to do because we do it like once every two years. I know I dread it, and they've been pressuring me to do it, and I thought, you know what, let me just drop that and say, hey, this is what I'm trying to do. Go figure out if you could — and guess what, it's done.
[00:01:47] Ty Wells: Yeah, it knows everything that you know you need to do, right? I'm sure you gave it all the great context, and so it told you exactly what to do.

[00:01:56] Patrick Chouinard: It actually knows more than I did, because what I did was I got a pile of documentation from the funeral home, I just scanned them all in, gave it to Claude, and said, like, figure out a timeline and a to-do list and everything I need to take care of, when I need to take care of it, manage all of the notifications that I need to have — took care of everything. I now have a beautiful HTML timeline with exactly where I'm at, what's going on, everything.
[00:02:29] Ty Wells: Yeah, that's sadly amazing, though.
[00:02:34] Patrick Chouinard: ▶ It took a process that took me about two months when I lost my dad 10 years ago, and reduced it to 48 hours this time.
[00:02:43] Ty Wells: Wow. I've never thought about using it in that regard, but that's actually a great use case, because when you get thrown in those types of positions, you're like, I don't know exactly what's going on.
[00:03:03] Ty Wells: You don't, yeah, you really don't — you're not in that frame of mind.

[00:03:08] Patrick Chouinard: And it went and figured out a bunch of stuff. It searched the government website to know exactly what I needed to do, when I needed to do it, which form I needed to send where — took care of everything.
[00:03:22] Ty Wells: Yeah, I saw a video — it might have been on TikTok — a guy was saying he was trying to make a change to his router, his home router. He gave Fable [tool:Fable] access, and Fable went in and rewrote the firmware and gave him every single option that was available to that router. I was like, what the...
[00:04:12] Patrick Chouinard: Yeah, that may be, and that's why I don't want to use those models to do those tasks — because yeah, it's fun this time around, you have the functionality you want. But when's the next update coming? Are you going to be monitoring that firmware to make sure that you patch it?
[00:04:35] Ty Wells: I know, that's the first thing I was like — rewrote the firmware. He's not really getting any updates. And then what do you got to do? You've got to set an agent to go get updates, and then where do you get them from? I mean, what's happening here? First of all, I'm sure it broke some protocol in rewriting the firmware. It's probably DD-WRT [tool:DD-WRT].
[00:04:57] Patrick Chouinard: ▶ Even if it did it perfectly, it's a one-stop shop — you're done. After that one, every new development, you're responsible for it from now on.
[00:05:06] Ty Wells: Yeah, when you break the rules, maintainability becomes an issue, for sure. Security becomes an issue. Everything becomes an issue.

---

<!--SEGMENT
topic: AgentOps Home-Lab Nervous System Architecture
speakers: Patrick Chouinard, Ty Wells, Juan Torres, Paul Miller
keywords: AgentOps, Hermes, NATS messaging, Uptime Kuma, Prometheus, Grafana, Alert Manager, Proxmox, scaffolding, agent orchestration, deterministic systems, open source
summary: Patrick introduces his AgentOps project — an operator-agent scaffolding layer built on top of his existing Hermes framework — which uses NATS as a message bus to centralize signals from monitoring tools like Uptime Kuma, Prometheus, and Grafana. The discussion covers the philosophy of keeping systems deterministic and only delegating decisions to AI when necessary.
-->

[00:05:19] Patrick Chouinard: Hey, Paul.
[00:05:20] Paul Miller: Guys.
[00:05:22] Ty Wells: Hey, Paul.

[00:05:29] Patrick Chouinard: Yep, operator environment is going to be something I'm going to be working on for the next couple of weeks. It's helping me take my mind off things.
[00:05:44] Patrick Chouinard: It's basically a sub-project I'm working on on top of Hermes [tool:Hermes]. I call it AgentOps [tool:AgentOps]. It's basically an operator agent scaffolding on top of the scaffolding of Hermes.
[00:05:57] Juan Torres: Oh, wow.
[00:06:00] Patrick Chouinard: Going meta again.
[00:06:09] Ty Wells: Is there any other way, Juan?
[00:06:17] Juan Torres: Systems thinking is the OG path.
[00:06:20] Ty Wells: I need to get better at that. The problem I have is they don't end.
[00:06:30] Juan Torres: The question is tolerance, right? Like, what's the level of risk and mismanagement? The precision that you need for a specific target — that's the question I was trying to grind myself into, to not over-engineer tools.
[00:06:48] Patrick Chouinard: ▶ The idea is you keep deterministic everything you possibly can and use AI decision-making only when you absolutely need to.
[00:07:02] Patrick Chouinard: ▶ That's why scaffolding development is where it's going to be for the next couple of years, because scaffolding is the deterministic part.

[00:07:14] Juan Torres: <Q>So scaffolding is not the same as harness engineering, right?</Q>
[00:07:18] Patrick Chouinard: <A>Yeah, you can see it as a harness on top of a harness, basically. Things like Hermes, OpenClaw, Claude Code [tool:Claude Code] — all of those are harnesses for the model to be able to code. So what I'm doing with AgentOps is basically a harness on top of that, that gives the model more information, more tooling, more sensory organs — even the equivalent of a nervous system.</A>
[00:07:50] Juan Torres: That sounds pretty badass.
[00:07:55] Patrick Chouinard: All with open source tools.

[00:08:00] Patrick Chouinard: The one I chose is called NATS [tool:NATS] — it's basically a messaging system. In this context, the messages are communication to and from the different sensory functionality: Uptime Kuma [tool:Uptime Kuma], Prometheus [tool:Prometheus], Grafana [tool:Grafana], Alert Manager [tool:Alert Manager] — and the subscriber is Hermes.
[00:08:42] Patrick Chouinard: ▶ That way, Hermes doesn't have to deal with 600 different message types — it just works with whatever message type comes from NATS, from the messaging platform.
[00:08:47] Juan Torres: Oh, I see what you're trying to do. Okay.

---

<!--SEGMENT
topic: Mythos/Fable Model Shutdown Discussion
speakers: Paul Miller, Patrick Chouinard, Ty Wells
keywords: Mythos, Fable model, OpenAI, model shutdown, enterprise data privacy, system prompts, fallback strategy, Opus 4.8, GPT-5.5, model availability
summary: The group discusses the sudden shutdown of the Mythos/Fable model, its implications for ongoing projects, and the privacy/enterprise concerns that made it problematic anyway. Members share their fallback strategies and emotional reactions to losing access to the model.
-->

[00:08:48] Paul Miller: Right. Good to see you back, Patrick. So I will host today, guys, so we can get all the latest insights from Patrick along the way. And from everyone else — in a week that we are still feeling very miserable about the lack of the Mythos Fable model. Oh God, the sooner that can come back, the better. But before we go into questions — does anyone know what's the latest with what people are saying on when it might be coming back, or what the plan is?

[00:09:36] Patrick Chouinard: It's speculative at this point. I mean, it's as clear as when the Strait of War move is going to be open, basically.
[00:09:54] Patrick Chouinard: But honestly, the more I read about it, the more I'm not so sad. The fact that they were keeping a lot of the information — like all the prompts and everything — from an enterprise perspective, it made it pretty much unusable from the get-go anyway.
[00:10:11] Paul Miller: Yeah. It was always going to be an issue.

[00:10:20] Paul Miller: Well, yeah, we'll have to go. It'd be good to understand when we go around the room what everyone's Plan B is. What's your fallback been now that you can't take advantage of that? I've certainly had to do some brainstorming over the last few days because I had all sorts of plans to do all sorts of amazing things, but the reality is that, yeah, it's not doable.

[00:11:00] Paul Miller: Okay, so let's start with Ryan. Oh, have we got any questions first going in? No questions this week? Okay, Ryan, how are things going in the UK?

---

<!--SEGMENT
topic: Ryan's AI-Native CRM for UK Estate Agents
speakers: Ryan C, Paul Miller, Juan Torres, Patrick Chouinard
keywords: CRM, estate agents, Rightmove, Zoopla, Meta API, WhatsApp, RAG, semantic search, Claude Opus, Higgsfield MCP, Remotion, iOS app, property portals, chunking transcripts
summary: Ryan C presents a newly built AI-native CRM platform targeting UK estate agents, featuring unified inbox aggregation across email, WhatsApp, and property portals, an AI assistant with RAG-based knowledge base, and auto-drafted responses. Built initially with Fable and iterated with Opus, the project also includes a companion iOS/Android app and a marketing website. Ryan discusses his vertical expertise, differentiation from existing CRMs, and plans for a pilot with his business partner's estate agency.
-->

[00:11:23] Ryan C: I was going to say, yeah, what have I been doing? Crikey. Started a whole new business, just because why not? It's just so easy to do so nowadays. So I built an entire...

[00:12:09] Ryan C: So I've essentially built an entire CRM [tool:CRM], AI-native CRM for estate agents in the UK that ingests all of their various incomings. It's going to interface with their email, Meta API [tool:Meta API] to bring in their WhatsApps, all the different property portals. I think you guys have like Zillow and stuff like that over there. Our equivalent of that is called Rightmove [tool:Rightmove] and Zoopla [tool:Zoopla]. So we'll pull all the incomings and push all of the properties. I'll manage all of their properties and stuff in here. So I built this whole website. Now, the nice thing is I built the entire plan and the V1 of this with Fable. And then I had to be iterating on it with Opus [tool:Claude Opus], which actually has worked out quite nicely because the baseline of it is quite good because obviously Fable did some incredible plans. And built out a rather nice app. It's built a complete native iOS and Android app, companion app. It's got a rather pretty looking website that I quite like, and I did a lot of design work on this, fiddling around with it, dialing it in. And then I built an entire assistant.

[00:13:28] Ryan C: The fun bit is the assistant. So I've created this little Mortar assistant here. And then it speaks — it's like a little demo, and then it kind of talks through this, essentially.

[00:13:51] Ryan C: So I've built this really nice little login page. I love a good login page. My favorite thing to design. And I hooked this in with Higgsfield [tool:Higgsfield] — they did the Higgsfield MCP [tool:Higgsfield MCP], and I paid for Higgsfield, so I thought, sod it, I'll just let Claude Code directly pull from Higgsfield and do all the imagery in there, so I don't have to bother. It's got a full admin set in here now, with all of the dummy data. So this is what your inbox looks like. You've got the assistant here the entire time that you can chat with and do a load of stuff with. This can do most things within the system for the user. It's got a full RAG [tool:RAG] search in here, with semantic search, and then it's got an AI search as well that can go into more of the documents and things like that. It gets to know them over time — so it builds an entire knowledge base about them over time.

[00:15:11] Ryan C: They can then request API keys that come through to us with the various different things. Because if they have somebody else building their website, for example, they can request an API key that they can then give to them. So this links in really nicely with my other business, which is obviously making websites, and my other business, which is making screens for these estate agents.

[00:15:33] Ryan C: So I'm doing this with a business partner. We've just registered for the limited company and the trademarks and everything yesterday. And yeah, I've just been literally building this and I've done like three rounds of playing around with it to make it a bit better. They'll have a full help section. I'm going to use Remotion [tool:Remotion] to do all the tutorial stuff.

[00:16:07] Ryan C: I need to generate a bunch of dummy property images, but it's just got everything in here that you could need. So I'm just iterating, adding, iterating, adding. But yeah, so that's kind of what I've been working on and then just continuing to refine the screen stuff.

[00:16:17] Paul Miller: <Q>So Ryan, what's been your response losing Fable? How have you had to recalibrate how you're doing this project without Fable?</Q>
[00:16:33] Ryan C: <A>It was at least a day where — I mean, I already hate Donald Trump, but it took it to the next level. So yeah, I mourned the loss for a day because obviously I have a whole list of things I wanted to do with it. But to be honest, Opus is good, it does what it needs to do, you just have to do more hand-holding, right?</A>

[00:17:23] Paul Miller: <Q>Have you got any customers already signed up to be your lead sort of pilot with this app?</Q>
[00:17:31] Ryan C: <A>Yeah, so my business partner owns an estate agency, so they'll be the first customer. And then I've got a couple, because obviously I do a lot of video for estate agents as well, so a lot of property videography is the other bit of my business. So I'm kind of primed chatting to a lot of these people already.</A>

[00:17:48] Ryan C: A lot of the other CRMs that are trying to integrate AI are doing bolt-ons, or they're saying, just do all of your work through the Claude chat — and as soon as you run out of context window, you're in trouble. Also, half of the CRMs don't really have an API that gives you everything you need. Whereas this is just going to be completely intrinsically interlinked. ▶ A lot of it isn't going to be AI — a lot of this is going to be built-in tools where it's going to know that if you ask this, it knows it can go here, here, here to find X, Y, Z information. It'll only reach out to Claude and the fallback would be OpenAI [tool:OpenAI], to do writing tasks — writing emails, WhatsApp responses, that kind of thing. And then when it's adding to the knowledge base, when it's chunking down data, I'm probably going to build in a specific chunking model.

[00:19:00] Ryan C: It's just jumping down into this, where then it does it by property, and then it summarizes everything, so it doesn't obviously keep all of the emails — it'll be, right, this is an email, what's the big things that we need to know about that, so it can search it.

[00:19:47] Paul Miller: <Q>Juan, you got a suggestion?</Q>
[00:19:49] Juan Torres: <Q>What's the differentiator of your application versus other CRMs?</Q>
[00:20:08] Ryan C: <A>It's that essentially you're going to have an AI chat that you can do everything with. Because a lot of stuff's very manual. And also, the main screen is this inbox here — it essentially aggregates all of your different communication channels. And a lot of time is spent responding to stuff and having to go and look for, oh, what did the solicitor say about that thing? So this person's sent something, and then in theory, it'll automatically draft the response ready to go. So you just come back, review the response, give it a tweak if you need to, and it'll learn from when you do edits. If you reject it, you put a reason in, it'll learn from that as well.</A>

[00:21:21] Ryan C: There are also a couple of different prop-tech companies that have massive amounts of data that I'm going to start piping into this as well. For example, if you sell a house in a road, you can go on and pay them to send letters to all the other houses in the road — "we've just sold number 12 for X amount of money, would you like a valuation?" I'm going to build that into here with a partnership with one of those companies. They've got an open API so I can plumb it straight in.

[00:22:06] Ryan C: I've got a list of things I want to add to it. In theory, it should just be the one hub that you drive everything from that's really easy to use and everything's sort of already ready and three-quarters of the way done for you. And this will dial itself in over time as well because it will learn from your edits.

[00:22:29] Juan Torres: <Q>Did you use the methodology similar to what Patrick did for the RAG on the calls? Because it seems that he had like a comprehensive RAG system, given that it was just one source, which was the script.</Q>
[00:22:43] Ryan C: The knowledge base is RAG'd. And Patrick, I presume you've done a RAG similar to what Scott was doing on his Neural Spark thing, right?

[00:22:56] Patrick Chouinard: Yeah, but the RAG system that was so different is the chunking, because what I was chunking is transcript, which is vastly different from files.
[00:23:09] Ryan C: So it'll be chunking email, all the communication history, and then I am going to integrate transcripts from meetings as well. If you have a Claude.md file that explains how that chunking system works, I'd be greatly appreciative of it.
[00:23:37] Patrick Chouinard: <A>Actually, it's an N8N [tool:N8N] workflow. Yeah, because I'm ingesting the transcript into N8N and it reprocesses it in order to construct it into a kind of file format by team. ▶ When you look at a transcription, you might have a question that's asked at minute three and an answer that comes at minute 33. So most of the chunk will not have the question and the answer together. So the first pass is to restructure all the information so you have linear information — so whatever got asked and when it got answered, everything is in meaningful blocks. Then you can chunk it traditionally and not have any impact on the quality of the retrieval.</A>
[00:24:39] Ryan C: Cool. That's good to know.

[00:24:41] Juan Torres: Watch his video that he did with Brendan. It's really insightful.

[00:24:48] Paul Miller: Have you seen the tool Twenty.com? [link:twenty.com] It's an open source project that's kind of a CRM — kind of rediscovered for the AI world.
[00:25:00] Paul Miller: The thinking behind the Twenty project is a group of guys got together to replace Salesforce.com [tool:Salesforce] because it's become bloated and expensive and not purposed for the AI world. And it's really gaining ground really quickly. I'm in the middle of switching our company CRM to it. It's got all of the things that you would assume in a CRM system, and because it's open source, you can bolt on other things. It's got a CLI you can interact with it, you can plug it into your chat tools as an MCP [tool:MCP], so you can get a lot more interaction right off the mark.
[00:27:36] Ryan C: I'll definitely take a look at it.

[00:27:40] Patrick Chouinard: Are they proposing Twenty.com that they're using Mythos in their chatbot?
[00:28:00] Patrick Chouinard: I just find it funny that they weren't advertising Fable — they were advertising Mythos, the model that never got released.
[00:28:07] Paul Miller: Well, it's all about the spin.

[00:28:39] Ryan C: And also, I don't even need 1% of the industry to sort myself out for the rest of my life. I could have 200 estate agents out of millions. That's all I need. That would pay my mortgage. I just need to have a group of people that like it, and can just keep adding cool stuff to it for them, and then just grow it slowly.

---

<!--SEGMENT
topic: KindMark — Positive Reputation Platform
speakers: Ty Wells, Paul Miller, Patrick Chouinard
keywords: KindMark, positive reviews, character attributes, privacy-first, geo-verification, QR code, social media automation, service workers, reputation system, fraud prevention
summary: Ty Wells introduces KindMark, a privacy-first platform for recognizing exceptional service workers through portable, character-based "kind marks" rather than monetary tips. The concept was inspired by an exceptional flight attendant encounter. The segment covers the platform's differentiation from negative-review systems, fraud mitigation via geo-checking, and automated social media content generation from submitted kind marks.
-->

[00:29:21] Paul Miller: Ty, what's happening in your world?
[00:29:23] Ty Wells: Hey, guys. Something new, as always, right? Let me put a link.

[00:29:36] Ty Wells: So I am working on a project called KindMark [tool:KindMark]. Have you ever experienced exceptional service from a service worker, and you wanted to reward them in some way? And in most cases today, what you do is you tip them, right? You give them a monetary reward. Those are non-transportable. So kind marks are really — you build up kind marks that get associated or attributed to an individual. So it's character, right? So you are patient, this person was patient, or they were truly kind, or they were forgiving, or whatever the case may be. And there's no way to really do that currently.

[00:30:34] Ty Wells: So KindMark is a way for users to actually give a kind mark. And it's privacy-first. So you can come in and submit things — "I was at whatever" — and it would pull out all of the PII stuff and say, "this person in the Western USA did this at this restaurant." And the actual individual can come in and claim these kind marks.

[00:31:07] Ty Wells: So what I'm doing is I'm pulling these representations that come in the form of reviews — Google reviews, Yelp, whatever, different sources — where people have made these identifications but really had no way to frame them and make them available. So long term, if you're looking at an individual A and an individual B and they have a kind mark standing, that would tell you where you're at.

[00:31:41] Ty Wells: Now, I'm sure the first question is, well, how do you give them a negative review? Well, I don't know — use Yelp or Google reviews or something. This is a positive platform. So if you don't want to give them a kind mark, just don't do anything, right?

[00:31:56] Ty Wells: So if you're in the back of an Uber and you have a QR code there that says, "How's the driver? Want to leave a kind mark?" — and then of course you will have the option to also tip that person as well. But it's not like, you know, use all your friends to give you kind marks — it doesn't work like that. It works over time.

[00:33:29] Ty Wells: And you know, this came up on the weekend — we traveled on Thursday and this flight attendant was exceptional. I had my wife and my son with me. I got off the plane and I talked to them and said, hey, do you guys have a way of doing this? And I know they take tips and I've seen it, I've done it and I've given them gift cards and so forth. But those things don't translate. I mean, they're there one time, they're transactional. And I watched him interact with every single passenger — he was just genuinely kind and useful. I wanted to do something, so I decided to make KindMark.

[00:34:18] Paul Miller: Well, it's also something positive for our very challenging times.
[00:34:26] Ty Wells: God, we need KindMarks. We do.
[00:34:31] Paul Miller: And if you don't have any KindMark standing, I think that says everything.

[00:34:41] Ty Wells: Well, I created all the social media accounts yesterday, and I've got an agent set up that's posting. So if you follow KindMark, or KindMark app, depending on which handle is available. There are some initial videos — I just put them out yesterday. They're pulled from real scenarios, obviously names obscured, but real situations that people did put a review on, and I just turned it into a video as to what happened. And the same thing will happen as people leave kind marks — those will be captured and displayed in videos automatically.

[00:35:41] Paul Miller: <Q>How will you deal with the process or the checking of people trying to defraud the process with leaving positive comments or trying to boost friends?</Q>
[00:35:47] Ty Wells: <A>You will have some of that, but you don't leave, you know, 10 kind marks on a certain thing. It's geo-checked and stuff in terms of things along that line that will help it try to determine. Obviously people will try, right? And if you leave marks to help somebody become kind — well, I would say the character of that person is probably not kind to start with, if that's what they're leading with. Fraud — that's probably not the platform for you.</A>

[00:36:36] Paul Miller: Well, there's always something — you're always coming up with some pretty brilliant ideas. A serial entrepreneur in terms of ideas.
[00:36:44] Ty Wells: This happened Thursday. I just started talking to the guy and he's like, there's no way to really do it.
[00:36:58] Ty Wells: And I did tip him on the way out, by the way. KindMark wasn't available, so I had to give him a monetary.

[00:37:12] Paul Miller: <Q>How have you dealt with the absence of Fable?</Q>
[00:37:23] Ty Wells: <A>It's been fine. The problem I had was I did use it to solve a couple of problems, which was great. But then as a security guy, I wanted to run some security against what I just built. The assumption is, well, Fable built it, so it's got to be good and there's no flaws in it. And I wanted to use it to check the flaws. And I couldn't do that. But it was a lot more powerful than Opus 4.8 — the UI it was generating was spectacular. And certainly the code was pretty solid as well, so I'm fine without it.</A>

[00:38:08] Paul Miller: I found an interesting thing. When I was playing with it at the end of last week, I was building an app and it magically told me that it was making a whole lot of security changes because it identified that there were gaps in what I was building. So I didn't ask for it — it just did it anyway.
[00:38:32] Ty Wells: I like that. Put some real bugs in there and see if it finds it.
[00:38:43] Paul Miller: Yeah, automatically. I know it had that block if you said to it like, "I just want to secure my own app" — it's like, oh, no, security, you've got to go to Opus. But when it actually self-checked itself — hopefully when it is back, just say, I'll just check if I'm doing anything wrong from a security standpoint.

---

<!--SEGMENT
topic: Patrick's AgentOps Deep Dive and Bereavement AI Use Case
speakers: Patrick Chouinard, Paul Miller, Juan Torres, Ty Wells
keywords: AgentOps, Hermes, NATS, Proxmox, Authentik, secret management, Infisical, Loki, GPT-5.5, Codex, MCP, home lab, infrastructure automation, Claude bereavement
summary: Patrick elaborates on his AgentOps architecture in detail — covering NATS messaging, Proxmox integration, Authentik authentication, secret management via an open-source Vault alternative, and a Loki log server for auditing. He also revisits his use of Claude for bereavement administration, noting Claude's emotional sensitivity during the process. The group discusses agent financial autonomy and ShipSafe agent payments.
-->

[00:39:34] Paul Miller: Patrick, give us the lowdown. What's happening in Montreal?
[00:39:42] Patrick Chouinard: A lot of things. It's been a very weird and tough last two weeks. But some good things came out of it, so I was debating if I was going to talk about it or not, but I think I actually hit some stuff that may make sense and could be helpful — and not the first thing you're going to think about using AI for, but I find it tremendously helpful.

[00:40:10] Patrick Chouinard: Two weeks ago, the reason why I was not here last week is I lost my mom.
[00:40:17] Paul Miller: Oh my goodness, I'm sorry.
[00:40:21] Juan Torres: Sorry to hear that, Patrick.
[00:40:23] Patrick Chouinard: Thank you, guys. But the reason I'm bringing it up is I'm pretty much the last one in the family, so all the administrative stuff has to go through me. And I'm sure you can guess that that's not the fun part, and it's definitely not something you have the brain for when that happens.

[00:40:45] Patrick Chouinard: So I went to the funeral home, they gave me a stack of paper that says, oh, you need to fill that form, by that date you need to have done that, and a bunch of stuff that you don't want to think about. I came back home, scanned the whole thing, dropped it in a Claude project and said, like, organize that for me. I don't want to think about it, but I know it has to be done. Just tell me what I need to do, when I need to do it, and whatever information you're missing to finish the task.

[00:41:14] Patrick Chouinard: I've done that work when I lost my dad 10 years ago. Took me about two months to get to where I am today. And today I've finished those two months worth of work in about 48 hours with the help of Claude. Pretty insane. It found stuff I didn't even know about. I just gave it, like, here's the paperwork I got from the funeral home. Plan this. It went to the government site, figured out a bunch of forms that I needed that was not there — it found a government insurance program that pays back when something happened. Anyway, figured out a whole bunch of things that I would have never had the brain power to search for myself.

[00:42:00] Patrick Chouinard: And now I have a beautiful interactive HTML timeline that tells me exactly what's been done, what's coming up, when I need to do what. It was the one that told me, like, okay, you know what, Patrick, now you're working on tasks that are not going to be due until August, so go sleep.
[00:42:31] Patrick Chouinard: ▶ It's never something I thought I would use AI for, but it was incredibly helpful to go through something that's really hard — it's not that you don't have the brain power for it, you just don't want to use your brain power for it.

[00:42:52] Paul Miller: Well, people have so much emotional and mental capacity to deal with certain issues at certain times. When you get these emotional things that drain you even faster, yeah, it's helpful.

[00:43:23] Patrick Chouinard: And honestly, I'm someone that's extremely pragmatic. So it's not like I was looking for emotional support. But even then, I found that Claude, in that scenario, once it knew the situation, was incredibly delicate.
[00:43:55] Paul Miller: It was impressive.
[00:43:57] Patrick Chouinard: It was impressive. Like, it really — that's the one who told me, like, okay, don't worry. This is far in the future. You don't have to worry about that one. That one you might want to take a look at because that's coming up next week. So if you don't want to be late, be thick. And it was really like, okay, now you're done. Go sleep. Come back tomorrow.

[00:44:15] Paul Miller: And that's quite a complicated ask if you think of how the hell it's dealing with the logic of that. It's like we've got enough logical issues that we throw at it with a business context, but it's far more complex with this kind of stuff.

[00:44:35] Patrick Chouinard: After that passed, I needed to occupy my mind with something else. I needed to escape into a bit of AI development.
[00:44:51] Patrick Chouinard: I got into something I've talked about earlier on in the call that I call AgentOps. Basically it is a scaffolding to go on top of the Hermes scaffolding, or any independent agent, actually, to give it a nervous system in my home lab. So basically it uses NATS, which is a messaging platform, to centralize and standardize all of the messages going between Uptime Kuma, Prometheus, Grafana, Alert Manager, Proxmox [tool:Proxmox], and standardize them in a message bus. So it's basically ESB for home lab.

[00:45:43] Patrick Chouinard: And so that way, Hermes can consume those messages. It has a full set of rules. It has a full set of skills that it can call. Those skills are also backed by a bunch of scripts, so it can intervene on my unified router, on my Proxmox hosts. It works with Authentik [tool:Authentik], so I have full authentication internally. All of the secret management is done in — basically an open source, lightweight version of what HashiCorp Vault [tool:HashiCorp Vault] is. So it's secret management. I have full API key management and full secret management. And I've basically built an MCP on top of a bunch of scripts that it can leverage.

[00:46:38] Patrick Chouinard: So it has a set of tools — it's a toolbox for Hermes in order to be made aware of what's going on in the lab through all of the monitoring and the NATS, and has the tools or the hands to actually correct things in the lab. And all of that's been built with Codex [tool:Codex], with GPT-5.5 [tool:GPT-5.5], which I found is amazing. It's good at coding stuff for terminals, even better than Opus 4.8. Opus 4.8 for applications that have a UI and a back-end system and a traditional application — yeah, very, very good. ▶ But for terminal applications and infrastructure applications, nothing beats GPT-5.5 for now.

[00:47:30] Paul Miller: <Q>Is this something you're going to be publishing with your other fabulous shared projects? Or what are you doing with your Ops app?</Q>
[00:47:45] Patrick Chouinard: <A>Yeah, well, definitely. It's just right now it's in a half-built state. I'm going to wait for it, because it can be very dangerous. I have a background in infrastructure, so I'm not too worried. I know what I'm asking it to do, and I understand the risk of what it does, so I'm okay developing it, but I would not give it out until it's actually been secured and made sure that it's not going to do some crazy stuff.</A>
[00:48:17] Patrick Chouinard: ▶ You're basically giving it the key to the castle at the end, so you have to be very careful about how it is able to ask for those keys. And that's why I have Authentik and true authentication and true secret management. I have a Loki [tool:Loki] log server also to make sure I can do full auditing of what's being done. So the tooling is way more important than the intelligence in this project.

[00:49:11] Juan Torres: <Q>Have you thought of creating, like, a small credit union account with maybe $200 and experimenting giving your agents a capacity to spend money through those means, with the limitation of not being able to spend that much money?</Q>
[00:50:08] Patrick Chouinard: <A>This is the part where I still want to have control. It can ask for it if it needs to, but right now it's managing my home lab, so nothing that it does requires money. Because if it needs an additional server, it just spins it up on Proxmox. And even once it starts to go outside — spinning something on Vercel [tool:Vercel] or Cloudflare [tool:Cloudflare] or something like that — it will run within the scope of those projects. If it requires to buy something, it would probably be API tokens. It's certainly not something that I want to give it free reign on, even with a limited budget. Because honestly, what's the point? I'm one message away. It can send me a Discord message and say, hey, I need $20 worth of API. I can do that transaction myself in 30 seconds.</A>

[00:51:36] Ty Wells: Did you look at my ShipSafe [tool:ShipSafe] agent pay? I think I — oh, you weren't here last week.
[00:51:42] Ty Wells: Yeah, it basically gives you a rechargeable account that your agent has access to, and it uses tokens to pay for stuff.
[00:51:55] Patrick Chouinard: And for other scenarios, yes. But there's very little scenario where it's going to need to buy something right now that I can't take the time to approve.

[00:52:40] Paul Miller: Thanks, Patrick, and all the best. It's a challenging time, and I can personally relate with my dad's passing as well a few weeks ago.
[00:52:52] Patrick Chouinard: It was a challenge.
[00:52:56] Juan Torres: Condolences, Paul.
[00:52:58] Paul Miller: Thanks, guys.

---

<!--SEGMENT
topic: Juan's Diffusion Model Experimentation for AI Photo Booth
speakers: Juan Torres, Paul Miller
keywords: WaveSpeed AI, diffusion models, LoRA, Stable Diffusion, Flux, Qwen-Image-2, HunyuanImage-3, Seadream 4.5, HuggingFace, image-to-image, AI photo booth, FinOps, multi-model pipeline, CLIP
summary: Juan Torres describes his experimentation with frontier diffusion models via WaveSpeed AI's desktop application to find the best image-to-image transformation models for an AI photo booth project. He evaluates models including Qwen-Image-2, HunyuanImage-3, Seadream 4.5, and Flux 2 Max, and discusses using community LoRAs from HuggingFace. He also outlines his FinOps approach to quantifying per-model costs before going live.
-->

[00:53:00] Paul Miller: Juan, what's the latest in your world?
[00:53:06] Juan Torres: Well, I've been experimenting. If you guys want to get into fusion engineering, which pays well actually — I've seen some of the job postings for fusion engineering. I'm not sure if it entails working on the AI pipeline or actually creating the inference engines that allow you to have the diffusion models in place. And diffusion models — I mean the AI models that transform images or create images or create videos, right? There's a difference between that and classical machine learning models and LLMs, right? So this is what I mean by diffusion model because of the non-regressive method that they use for the process of creating the images.

[00:54:00] Juan Torres: So what I've been experimenting with is using WaveSpeed [tool:WaveSpeed AI]'s desktop application — it's really good in terms of creating config UI workflows, but using the frontier models. So you're not just using Stable Diffusion [tool:Stable Diffusion] models with LoRAs [tool:LoRA] — LoRAs are the low-ranking adaptations that you create for open source models. And you can actually use them. You can find LoRAs from Stable Diffusion or Flux [tool:Flux] in HuggingFace [tool:HuggingFace], and reference those in the transformation of models using WaveSpeed's desktop. But the desktop allows you to just use the frontier models and experiment with different prompts and see the transformation. ▶ So it gives you kind of like a scientific methodology — an empiricist method — to see which prompts do well with which models.

[00:55:00] Juan Torres: And so far, I've been surprised. Some of the models that I've seen being really good have been mostly Chinese ones, with the exception of GPT-2 and Google Gemini Pro. But other than that, the ones that are the most dynamic are Qwen-Image-2 [tool:Qwen-Image-2], HunyuanImage-3 [tool:HunyuanImage-3], Seadream 4.5 [tool:Seadream 4.5], and to some extent, Flux 2 Max [tool:Flux 2 Max], in terms of image-to-image transformation with a prompt for that specific job.

[00:55:55] Paul Miller: An AI booth application, right? So it goes back to that.
[00:56:06] Juan Torres: So, and perhaps I should have started with that. But yeah, so that's the reason I'm making the experimentation. So far I've only relied on Seadream 4.5 and it seems that in order to have the most dynamic, the most diverse and best quality images, I will have to engage in a process of combining different models with specific scripts or even the same scripts, but with different outcomes that contribute their own aesthetic value.

[00:56:43] Juan Torres: And this week, what I'm doing is just working. I have two computation units. One is working just fine. The other one is like a really old computer back from 10 years ago. Because I'm using Vanta.js [tool:Vanta.js] Halo effect for the front end — and I think I've showed you guys the graphical display, like a halo radiating kind of purple stuff — it's having issues with that. So I might have to replace that computation unit for something that has better capacity for graphical display.

[00:57:41] Paul Miller: <Q>Are you running on your own desktops at this point? Are you running up some GPU-based servers to process the stuff, or how are you servicing this?</Q>
[00:58:01] Juan Torres: <A>WaveSpeed, WaveSpeed, WaveSpeed. I'm not creating the inference engine because it would require me to actually have a substantial amount of GPUs in order to run different models, so I'm not doing any of that. What I'm using is just the provider WaveSpeed AI. They seem to be good enough because they seem to be speeding out images rather easily. ▶ I recommend you guys try to just add maybe $20 of credit, download the desktop application and start experimenting with the transformation of images for the models that I just mentioned because they're really good.</A>

[00:59:01] Juan Torres: There is a technical question — LoRAs are model-specific, right? So you need to create one for each different image generator. Well, you can create your own LoRAs, but you can just borrow them from the community, the open source community, and you can basically use them in your workflow with WaveSpeed's desktop program. You can go to HuggingFace, and HuggingFace has a lot of LoRAs for Stable Diffusion, some are for Flux, some are for other open source models.

[00:59:49] Juan Torres: So far, I know people use OpenRouter [tool:OpenRouter]. I haven't used OpenRouter that comprehensively. Maybe I will use them mostly for LLMs.

[01:00:27] Juan Torres: I haven't placed it on the field yet. I will soon. And that would allow me to quantify the utilization of each one of the models and how much each of the models are going to cost, given that I want to engage in a multi-model AI pipeline. And I have the FinOps in my data web application to be able to quantify that. So once I integrate several models, I'm going to be able to quantify the cost that each one is going to have per event — for example, given at least three hours of running the photo booth, I'm going to be able to quantify it, have an average, and then be able to systematize how much I'm going to charge potential clients for using the AI booth.

[01:01:27] Paul Miller: <Q>How do you rank the quality of the output? Do you have any self-checks where you've got your own models looking at the outcomes of what WaveSpeed is generating?</Q>
[01:01:54] Juan Torres: <A>No, I don't have a quantification of that. It's making qualitative judgments of what I think would be something of aesthetic value to potential people. I know there's CLIP [tool:CLIP], which is a model that actually tries to assess the quality of the generation of the image. I actually had it on my first pipeline for a Stable Diffusion model that I wanted to use for this specific purpose. But I found out that just the commercially available diffusion models are really good and you don't have to do much pipeline engineering. So yeah, it's basically A/B testing of a specific image with a specific prompt.</A>

[01:03:12] Paul Miller: <Q>So are you getting closer to your pilot go-lives with getting out?</Q>
[01:03:18] Juan Torres: <A>I think so. I'm going to be meeting the person that is going to help me tomorrow. I have a basic setup that I can use right now and probably I should just send it versus a more complex setup. So I'll probably try to get it up and going this weekend or next weekend.</A>

---

<!--SEGMENT
topic: Morgan's Update and Local AI Community Event
speakers: Morgan Cook, Paul Miller
keywords: Fable model, Opus, cemetery software, county government, AI Collective, frequency co-working, local AI meetup, construction, project pipeline
summary: Morgan Cook shares a brief update on multiple ongoing projects, including cemetery management software stalled by county government bureaucracy. He also mentions attending a local AI meetup hosted by the AI Collective focused on practical AI productivity. The segment touches on the value of local AI events for networking and lead generation.
-->

[01:03:55] Paul Miller: Morgan, what's happening in your world?
[01:04:04] Morgan Cook: My world's going pretty good. Busy. Lots of projects. I had a project all lined up ready to start with Fable and went in to start it, and it was shut down. So I was very disappointed about that.
[01:04:23] Morgan Cook: On the positive side, I didn't experience the joy of it yet to understand what I lost 100%.
[01:04:30] Paul Miller: Okay, so you haven't had to worry about the workaround just yet.
[01:04:37] Morgan Cook: Yeah, I was procrastinating and thought, you know what, I better jump on this before I lose my window — and went to jump into it and it was already shut down. I was like, oh, crap. So anyways, I didn't experience any pain there. I just carried on with Opus at that point.

[01:04:57] Morgan Cook: I've got several projects still all moving a little bit further each time, but a lot of it's waiting on other people, which is frustrating to me. And then besides the AI stuff, I do construction work on the side. So tonight there's a meeting here in our local town sponsored by the AI Collective [tool:AI Collective]. And so they're going to do some — it's called Frequency Co-working and Events. And so they usually get together and show people how to do useful and productive things with AI. So I'm going to attend that, see what that's about for my local area and see if I can meet some more people around here.

[01:05:54] Morgan Cook: Cemetery software is moving along, but county government, you know.
[01:06:00] Paul Miller: Sloth. Damn bureaucrats. Yeah, that's the challenge.

[01:06:08] Paul Miller: Yeah, those events are great because often I find 50% of the time they're a greater source of getting leads and opportunities than they are getting new answers — because you're pretty well connected. You kind of underestimate what you already know on the AI side.
[01:06:34] Morgan Cook: Yeah, no, I'm really just going to socialize and get some potential work out of it. Maybe some side money on a little project here or there to help somebody along. So we'll see how it goes.

---

<!--SEGMENT
topic: Fable Fallback Strategies and Adversarial AI Prompting
speakers: Paul Miller, Patrick Chouinard, Ty Wells, Juan Torres, Morgan Cook
keywords: Fable model, Opus 4.8, GPT-5.5, Codex, adversarial prompting, Claude.md, system prompt, business analyst, devil's advocate, intent queue, by-the-way command, token management, requirements documents
summary: The group discusses strategies for working without Fable, including combining Opus 4.8 with Codex 5.5 in parallel on the same project. Patrick shares his adversarial system prompt philosophy — making Claude act as a devil's advocate business analyst — which has become one of his most-requested deliverables. Ty introduces an "intent queue" workflow using Claude Code's background worker to preserve context across sessions. The segment closes with reflections on the danger of over-delegating to powerful models at the expense of intentional planning.
-->

[01:06:57] Paul Miller: Now, I had asked if Bastian had done a little post, so he's put a little link in — and that was certainly my feedback. With Fable, I'd really got into using it a lot, so I really felt the gap and was pretty upset, directing all sorts of tweets on Twitter accordingly, but I've calmed down somewhat since then.

[01:07:28] Paul Miller: But it's interesting — a lot of people are using a combination of Opus 4.8 combined with using the best of Codex 5.5 together. So I, by default, do Opus 4.8 projects, and I use the Superpowers [tool:Superpowers] tool, and then every time that Superpowers has a juncture point where it says, "here's what I propose in terms of requirements document," I push that back into Codex and get it to validate. And it sits in the same project folder, so they're both going along in parallel in the project and getting the combined visibility and looking at the weaknesses of each other's models. ▶ But the thing I'm missing the most out of Fable is it was so much faster getting through stuff, because it kind of had the big picture, it knew where to put the effort in.

[01:09:00] Paul Miller: Now, one question I've got for all of you guys. How often are you guys seeing when your client comes to you — and this is a good old-fashioned issue that you get in the tech world going back decades — where customers will come and say, well, why isn't the program able to deal with this business logic and with this problem? Because they've never properly mapped the business logic. And somehow, because it's put on a system or it's put on AI, that it's going to solve a business logic problem that will never work. Are you all continuing to see this with the odd customer that has businesses that are run seat-of-the-pants, where CEOs are operationally keeping the business from falling over every day and then somehow think that AI will magically resolve it?

[01:10:23] Juan Torres: No.
[01:10:25] Patrick Chouinard: Absolutely not. You're absolutely not alone in there. Because the more artificial intelligence you inject into a business, the less natural intelligence seems to stay there.
[01:10:38] Paul Miller: Direct correlation. They need natural intelligence, not artificial intelligence.

[01:10:46] Morgan Cook: ▶ And remember, every time you use these AIs to solve a problem, if the process is inherently broken to begin with, the AI just amplifies the problem. It doesn't solve it. It just amplifies it and says, okay, here it is, much better. It's bigger so you can see what it is, but you have to fix the process first.

[01:11:11] Patrick Chouinard: And honestly, that's why — if there are three sentences that have been asked of me so many times that it's probably my biggest deliverable now — it's the system prompt I use with all my agents. Because my system prompt is made to make it adversarial, to make it a devil's advocate, and that has saved a lot of my clients. Because the problem is, people don't know how to state the problem. They state their intended solution to the problem. So the AI, by nature, if you tell it, "I need a system that does X, Y, Z" — fine, here's a system that does X, Y, Z. Problem is, what you need is a system that does A, B, C instead. But the AI doesn't have that business analyst tendency to say, are you really needing that solution? What's the problem you're trying to solve?

[01:12:09] Patrick Chouinard: ▶ So basically, I made mine as adversarial as possible, and it forces you to actually think. Mine will happily tell me, like, what the hell are you smoking? It's like, are you sure? What problem are you trying to solve? And it got me out of trouble a couple of times, so I know that it got a lot of my clients out of trouble.

[01:12:47] Patrick Chouinard: And bizarrely, people say, oh, no, no, no, AI has to be agreeable, otherwise it messes up engagement. Well, then tell me why all the VPs that see how my AI agent talks to me — the first thing they say is, I want that system prompt.

[01:13:00] Patrick Chouinard: It's very simple, it's just a couple of sentences, but it tells you, like, I value honesty over agreement a thousand percent. Don't tell me what I want to hear, tell me what I need to hear.
[01:13:16] Paul Miller: Yeah, and who of us who has been in IT for a while knows an agreeable business analyst that we like sitting down with? These people are naturally not agreeable — they challenge, they put their hand up.

[01:14:00] Paul Miller: <Q>Who's the bigger devil's advocate — Claude or OpenAI in your understanding, Patrick?</Q>
[01:14:07] Patrick Chouinard: <A>Oh, Claude can do some doozies when encouraged. OpenAI is good, but it's more sassy than confrontational. Claude can tell you to your face like, nope, that's dumb.</A>

[01:14:46] Patrick Chouinard: It's really short, but believe me, it will transform your interactions. And I've used that also in Claude Code, not just in the desktop application. So my coding agent tells me when I'm doing something stupid.
[01:15:00] Juan Torres: <Q>You put this in Claude.md [tool:Claude.md]?</Q>
[01:15:02] Patrick Chouinard: <A>In the Claude.md at the user level. So it's always there in every conversation. And I use it in Codex as well.</A>

[01:15:28] Paul Miller: Right. Anything else anyone else wants to bring up? Or any other stories of how you've mitigated the loss of the Fable model?
[01:15:42] Patrick Chouinard: I'm not sure we're going to see that one again. We might see GPT-5.6 [tool:GPT-5.6]. I expect to see 5.6 before we see Fable again. But the problem is now — is the government going to stop any new model that is beyond the level of the current ones? Because in a sense, if you say that Fable's too dangerous, well, any new model beyond that capability will be by that definition.

[01:16:44] Patrick Chouinard: In terms of replacing it, honestly, I've tried it, I've played with it quite a lot. It's good at analyzing, but the thing it's best at is the thing it's prevented from doing. So that's why I'm not finding it so harsh not to have it. ▶ I prefer what you're doing right now — designing with Claude, implementing with Codex, then validating, going back and forth. To me it keeps me in control, it keeps me aware of what's going on, and it gives me 98% of the way there.

[01:17:21] Patrick Chouinard: The danger, I think, with a model like Fable is you give in so much to them that you end up — after a week it's fun because hey, it did all of that work for me — but I see like three months down the road, if you don't even think about the intent beyond your ask, I'm not sure how... intention is a muscle like anything else, if you don't practice it, you'll lose it.

[01:17:54] Juan Torres: You know, I was at a meetup here in San Diego — it was supposed to be the Claude Club here in San Diego — and the guy was presenting on how to use Claude Code to generate quality code, and he was going over the tools like MCP, tooling, multiple agents, but I just feel like he wasn't even getting to the crux of one of the principal tools that you can use, which is just intentful planning and having a really intentful detailed conversation, and then documentation of the whole process. And then we were looking at his specs, and it was crazy — he was spending a crazy amount of tokens on whatever things he was doing. So it was just seeing the — and he admitted, he was kind of ADHD all over the place with his projects. For being the presenter of that club, I thought he was going to have a more structured methodology to using Claude Code. ▶ That's why I come to this meeting, because at least in this meeting, I know there's emotionally regulated people that can do feasible agentic coding.

[01:20:14] Paul Miller: ▶ Getting requirements documents really well optimized before we even start coding is a really exciting thing. Making sure that the lessons learned and the guardrails of our coding standards and our architecture frameworks are all right before we even start doing development — this is nice, because that was pretty boring stuff before.

[01:20:55] Patrick Chouinard: And to me, I would way prefer a model that is able to collaborate with me instead of doing the job for me. Basically, if I ask you a dumb thing, be intelligent enough to tell me, guide me back, or argue with me. Then I give you two sentences and you code the application. Because honestly, think about it — if you give like half a paragraph of intent and it does the whole thing, did it really build the application you had in mind? Or do you adapt your requirements based on whatever it delivers?
[01:21:33] Paul Miller: That's the problem.

[01:21:35] Ty Wells: So what I was trying to do was take advantage of the by-the-way command [tool:Claude Code by-the-way command], right? Because the context is loaded, but the context is getting full in the main session. I was trying to take advantage of it, and I couldn't save tokens, but I had a good loaded context that I could ask — like, if I'm building a feature and I wanted to, while this context was fresh, queue up another feature using that well-informed context.

[01:22:29] Ty Wells: ▶ So I built this queue system where I run the background worker, I capture that information that I want, I ask the question, I have it put the response in the prompt, and then you can use the copy button. And the copy button takes that and puts that in a file locally — once I put that in the clipboard, that queues that up for my next session. So I do that a few times, then I clear the session. And the first prompt I send, the hook brings up, "hey, you've got four items in the intent queue," and then I have those, then I can work on them. But it's like primed, ready to go. I don't have to go through and waste a lot of tokens.

[01:23:20] Patrick Chouinard: Not yet, but I will later tonight.
[01:23:24] Paul Miller: That's my learning this week.

[01:23:26] Ty Wells: I would use by-the-way all the time just because I have a question but I don't want to interrupt what it's doing, I don't want to flood the context. There's no way I can tell you — don't try to save tokens on it, because you can't. It actually costs you a little bit more tokens, but on the next feature you build from the intent queue, you're going to save tokens there because you don't have to go through that process of priming it.
[01:23:56] Ty Wells: I can give that to you guys. It looks like — so you don't have to go through what I went through to get to this point, but it works great.

[01:24:05] Paul Miller: <Q>So Ty, have you done much with Codex, or are you all in Claude?</Q>
[01:24:13] Ty Wells: <A>I only use Codex for my adversarial review, or if I needed to fix something. But I can tell you that I use GPT-5.5 to thrash out a lot of ideas. And then I tell it — just voice, because that's just so much easier — and then I tell it to give me, sometimes I say, I think I'm going to build this in Claude Code, what do you think? And then I go back and forth on that for a little bit. And then I say, okay, give me the Claude Code plan. For me, I think it plans it out better. And then I take that and I drop that in Claude, tell it to look at it, it looks at it, then I tell it, hey, give me your feedback on it, then I push it back into ChatGPT [tool:ChatGPT] to continue, and then until I'm satisfied, and then I go ahead and build it in Claude Code. So I only use Codex for adversarial review at the very end.</A>

[01:25:37] Patrick Chouinard: ▶ If you ever do something with terminal code or scripts, look at Codex — believe me, it's far, far ahead of Claude in my mind. Because every time I've done something at the command line, it's been incredible.

[01:26:00] Patrick Chouinard: I actually filled my yearly review form this year by talking to it two or three hours a day, so it knows just as much as I do about the projects I'm working on and what I would like to do and where I want to go.
[01:26:20] Paul Miller: Would your HR department be agreeing with that as an appropriate way to fill out your form?
[01:26:27] Patrick Chouinard: Oh, they know very well. I actually made it write the fact that it was writing my annual review.

[01:26:46] Patrick Chouinard: And you'll see — if you look at the community board — often when I reply, and Juan, I think you've experienced that a couple of times, is when I use my agent to help me reply to something, I will actually tell it, like, use your own voice, don't pass as me, just say it as it is, that you're working with me to answer this question.
[01:27:11] Juan Torres: It felt like you, though.
[01:27:14] Patrick Chouinard: Yeah, well, it's basically used to talking to me and exchanging with me for hours a day, so yes, it's similar. But I made it a point to say, I'm not trying to say that I'm more intelligent than anyone. No, this is AI answering with me. ▶ That's why I actually leave the AI disclosure in there.

[01:27:43] Paul Miller: Right, so anyone else have anything else to cover off before we wrap up for tonight?
[01:27:57] Juan Torres: If anyone has the chance to use — just maybe bring it up next week — Fusion, right? Yeah, Fusion is the one. Yeah, for sure. I think it would be really interesting.
[01:28:15] Paul Miller: Have a great week, guys. We'll see you next Wednesday.
[01:28:19] Ty Wells: I actually did write up the concept plan. I'll drop it in the school community. I'll put a post out there for using the by-the-way.
[01:28:28] Patrick Chouinard: Thank you, Ty.
[01:28:30] Paul Miller: Thanks, Ty. See you guys.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not populated — the template variable `{{ $('HTTP Request: Get Speaker Aliases').item.json.data }}` returned no data):

- **Patrick Chouinard** — primary technical contributor, Montreal
- **Ty Wells** — KindMark project, security background
- **Paul Miller** — meeting host
- **Juan Torres** — AI photo booth / diffusion model experimentation
- **Ryan C** — UK estate agent CRM project
- **Morgan Cook** — cemetery software, construction side work

All names have been passed through unchanged as no alias map was available to resolve canonical forms.