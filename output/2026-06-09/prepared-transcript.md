=== SESSION ===
date: Not explicitly stated (references to Anthropic "Fable" release and WWDC suggest mid-June 2025)
duration_estimate: ~73 minutes
main_themes: AI agent governance and cost control (Hermes/ShipSafe platform), AI photo booth deployment strategy, digital signage SaaS business, Anthropic Claude "Fable" model release, Apple WWDC reactions, China AI chip innovation

---

<!--SEGMENT
topic: AI Agent Governance Platform Overview
speakers: Ty Wells, Paul Miller, Patrick Chouinard
keywords: AI agents, cost control, authentication, authorization, non-reversible actions, Hermes agent, ShipSafe gateway, metering proxy, BYOK, policy engine
summary: Ty Wells presents an agent governance platform (Hermes/ShipSafe) designed to give non-technical users autonomous AI agent capability while enforcing cost controls, security, authentication, and guardrails on non-reversible actions. The architecture routes all agent activity through a metering proxy and gateway. Paul Miller and Patrick Chouinard briefly discuss screen-sharing logistics before the substantive demo begins.
-->

[00:00:00] Ty Wells: But he's concerned about what it costs. You know, he sees the horror stories about agents running away, but he wants it. He doesn't want any of the complexity of it, but he wants it. He understands, I need to control my costs. That's one piece that he understands. He doesn't understand the security part of it, but that has to be there, too.

[00:00:21] Ty Wells: And then authorization and authentication has to be there, too, because you have security. And then, like I said, any non-reversible action, there needs to be some way to manage that, and that's what the authentication is there for.

[00:00:43] Ty Wells: And then be able to do things autonomously, because they want the autonomous, but it's very complex, and they don't want to understand it, and they don't really need to. And that's what this layer does for them.

[00:00:57] Paul Miller: <Q>Might this also be a marketplace in which you invite people to the existing stack and environment to then run their agents within it?</Q>

[00:01:13] Ty Wells: <A>Yeah, just put that layer that your agent runs through when it's communicating. Whatever you build, it's going to be an agent of some sort. Let it run through the layer of protection.</A>

[00:01:34] Ty Wells: Patrick, do you have a question for me or for the...?

[00:01:36] Patrick Chouinard: Actually, I just wanted to check because, Paul, you sent me a message.

[00:01:41] Paul Miller: I just wanted to make sure that you were okay for the call. Yeah, we just need to be able to do shares. I don't have the authority to do shares.

[00:01:52] Patrick Chouinard: Ask once, I'll approve it, then I'll be able to...

[00:02:09] Paul Miller: We got it, Patrick.

[00:02:18] Patrick Chouinard: Bye, guys.

---

<!--SEGMENT
topic: Hermes/ShipSafe Architecture Demo
speakers: Ty Wells, Paul Miller, Juan Torres
keywords: Hermes agent, ShipSafe gateway, metering proxy, BYOK, guarded surfaces, policy engine, non-reversible actions, cost control, agent isolation, provisioning
summary: Ty Wells screen-shares the architectural diagram of the Hermes/ShipSafe platform, explaining how agents are isolated and routed through a gateway and metering proxy. He introduces the concept of "guarded surfaces" — user-defined protection rules for non-reversible actions such as spending money or deleting data — and explains the bring-your-own-key (BYOK) model and pricing tiers. Juan Torres asks how guarded surfaces are quantified for pricing purposes.
-->

[00:02:22] Ty Wells: Yeah, I mean, you guys can read it over, but I think I explained basically the layout.

[00:02:30] Paul Miller: It's got a lot of depth, a lot to think through because it's solving so many things.

[00:02:47] Ty Wells: Yeah, it has to be. That's why I said I built it really different times because I needed different things. But it's really a full circle. If it's not a full circle, then it's really sort of useless. So that's why I had to build in all the layers and then connect them properly. And now I can throw an agent on top of that.

[00:03:37] Ty Wells: So you see here, this is the layout of it. So you've got the Hermes agent [tool:Hermes]. You've got these connections that are built into Hermes. And then you have the ShipSafe gateway [tool:ShipSafe] and the metering proxy that handles all of the transactions. But that's isolated here. Everything rolls through the gateway, the metering comes in there as well, make any connections and then you go back in. That's sort of the layout of how you would do that.

[00:04:12] Ty Wells: So who builds this and what functionality? Doesn't matter, it just needs to go through the gateway to make sure everything is good.

[00:04:36] Ty Wells: You know, they're running on a $20 plan for the hosting. And then, of course, they bring their own keys. There's a BYOK all the way through because I'm not tied in. If they drop off the platform and want to move on, they would still need to maintain their access to the platform to ShipSafe. Let's say they don't want to be a client anymore and pay the maintenance fee, then they've got to disconnect. Who wants to disconnect after you're deeply ingrained?

[00:05:23] Paul Miller: <Q>So under the pricing model, the solo user has three guarded surfaces. What's the definition of what a guarded surface is?</Q>

[00:05:38] Ty Wells: <A>The guarded surfaces are the things that you're trying to protect. You're defining what's a guarded surface. So let's say you don't want to access a certain service, or you want to say anything over a hundred bucks I want to be involved in — I want to approve that. Guarded surfaces are self-defined. It's not something that is defined up front. You decide what guarded surfaces you want to protect and that's what you protect. And those guarded surfaces are those non-reversible actions. Spending money. Something you can't get your money back. Delete a directory. Delete my entire database — that's a non-reversible action. That should be guarded. So all the horror stories you heard about agents doing wild stuff, spending a bunch of money.</A>

[00:06:55] Paul Miller: Yeah. So you set those as guarded surfaces. Everything runs through the proxy.

[00:07:00] Ty Wells: ▶ If it can't get beyond, you've got to go through the proxy to see if that fits within policy, so there's a policy engine that you define, and that's where you define your guarded surfaces. But you define these things as a client at a high level. You don't get into the weeds.

[00:07:34] Juan Torres: <Q>So how do you quantify the guarded surfaces in terms of the money stratification that I see here?</Q>

[00:07:44] Ty Wells: <A>There's no quantification on it. It's just an individual surface you're defining. So you just define a specific surface — that's one. You need something else guarded, that's two. That's how the surfaces are defined. And they will vary between businesses, between whatever actions that business is doing.</A>

---

<!--SEGMENT
topic: Platform Messaging and Onboarding Feedback
speakers: Ty Wells, Paul Miller, Bastian Venegas Arevalo, Ryan C
keywords: marketing messaging, homepage design, guarded surfaces, user onboarding, simplification, use-case examples, hooks, headline copy, agent complexity
summary: Paul Miller, Bastian Venegas Arevalo, and Ryan C give Ty Wells feedback that the platform's breadth and flexibility make it hard for new users to know where to start. The group recommends simplifying the homepage with concrete, relatable examples and strong headline hooks to reduce bounce rate. Ryan C emphasizes that the most important real estate is the above-the-fold homepage section.
-->

[00:08:25] Paul Miller: I'm thinking my only sort of practical feedback is that we're asking about this. You may need to just provide a little bit more tangible examples or some preset, real practical things that people are worried about — money, they're worried about security. And like, here's where most users start, or something like that for the pre-configured base setup.

[00:09:39] Bastian Venegas Arevalo: If something is very, very capable and it can do almost anything, it's hard to find a starting point.

[00:09:52] Paul Miller: That's the challenge, Bastian. I'd heard Bastian was saying that because it's so powerful and so flexible, sometimes when you've got a more capable, open-ended capability, people don't know where to start in terms of how you can leverage it. ▶ Even though you don't want to ring-fence it, you want to seed some examples of here's how you could start.

[00:10:44] Ty Wells: Yes, I will definitely try to figure out the best way to present that. I have got... They explained to me as a "explain it to a 10-year-old" rule, so I will definitely do that, so it's a little clearer as to how the system works.

[00:11:13] Paul Miller: Ryan's got a good thing in the chat — Ryan being Mr. Marketing. Marketing gold is being able to boil down complex stuff to simple examples that Joe Bloggs can understand.

[00:11:37] Ryan C: I think like a slider on the homepage or something tied with like five sort of big hallmark things that's really simple — like it saves me five times the amount of money, or this amount of time doing X, Y, Z. Just really, as you say, dumb it down so a five-year-old can get it. Just the big headline-y stuff. So somebody goes, ooh, cool, I'll look at more of this. Because that header bit of the website is the bit that most people hit and bounce back off of if they don't get it from that. ▶ So that's the most important part — that bit of the homepage — just what's that headline grabber that's going to get somebody to go, I'll scroll on, or I'll click onto more pages.

[00:12:33] Ty Wells: I don't like that, guys.

[00:12:36] Ryan C: I'm not saying that part is easy. It's how you figure that bit out that's the difficult bit.

[00:12:41] Paul Miller: This solves so many problems, because the gap between the agent capability and practical, real execution with commercial control, security, and the rest of it — that's the challenge we all have. That's cool stuff, Ty.

---

<!--SEGMENT
topic: AI Photo Booth Deployment Strategy
speakers: Juan Torres, Paul Miller, Ryan C
keywords: AI booth, photo booth, image generation, diffusion models, EC2, AWS CloudWatch, VPC, San Diego, B2B SaaS, event deployment, staging environment
summary: Juan Torres updates the group on his AI-powered photo booth project — an event photo booth that produces AI-transformed images — which is technically ready for field deployment. He discusses infrastructure (EC2, CloudWatch, VPC security), hardware setup (dual touchscreen), and the strategic question of whether to handle early deployments himself or hire a technician. The group advises him to run the first few events himself to document the process, build a standard operating procedure, and understand real-world friction before delegating.
-->

[00:13:10] Juan Torres: The AI Booth project [tool:AI Booth] that I'm working on, it's ready to be deployed. The only thing that I need to work on is getting the hardware ready. It's going to be a two-screen setup, touch screen. Then I have to get my media person to come with me and film part of it so I can make content on my LinkedIn and Instagram and YouTube. And then I'm trying to get someone to hire to install the AI booth installation.

[00:14:26] Juan Torres: I want the friction of reality basically crashing against my application and see where I face the weak points, where I face strengths and unforeseen consequences of things that I didn't even think about. So I'm just trying to get all the minimal requirements in order to get it out to the field.

[00:15:05] Juan Torres: I'm creating a monitoring mechanism for myself — created CloudWatch [tool:AWS CloudWatch] resources to watch the memory, CPU, RAM capacity of my EC2 instance [tool:AWS EC2]. It's just one EC2 instance. I haven't deployed into an auto-scale group because right now it seems to be working well in that staging environment. Communication between all resources within my VPC are encrypted. Strong inbound/outbound rules in order to protect those resources within my VPC.

[00:16:33] Paul Miller: <Q>What's going to be the nature of the people that would partner with you that would do the deployment end? Are they conference people? Event management people?</Q>

[00:16:56] Juan Torres: <A>Someone has to be in the field deploying the actual TV stand and installing the setup. The title I gave the position is "AI Booth Technician." A person can have not very complex tasks — delete images if deemed inappropriate, send them through email, trigger re-uploads if the inference engine gets stopped. Other than that, it's just monitoring the setup and retrieving the setup and taking it back to my home when everything's done.</A>

[00:19:25] Juan Torres: So the AI booth service is basically — when you go to a party, a social event, quinceañera, wedding, or any other events, there's a photo booth, and a lot of venues contract someone to do that. This one is like that, except that you get the original pictures and AI-transformed images.

[00:20:35] Juan Torres: Sebastian says, maybe you can get an intern, Juan.

[00:20:42] Juan Torres: ▶ If you do it yourself, you create a very strong modus operandi that you can document, and then you can pass it on to someone else.

[00:21:06] Ryan C: ▶ You iron out all the problems before you hand it off to somebody else, because if you hire somebody to do the first one and it all goes wrong, you're not on site physically to fix it. You're better off doing at least two or three to start off with yourself.

[00:22:30] Ryan C: ▶ Prove concept yourself, document everything so you have that step-by-step, and then when you bring somebody else in to offload that time, you've got a streamlined service. They have a good time, they want to keep doing it, you're offloading that to somebody else at a lower cost to you — you make a little less profit, but actually you can do more because of it.

[00:24:01] Juan Torres: The only thing is that at the first event, I'm going to have two jobs essentially — I want to monitor the EC2 instance, monitor the local computer, and monitor the expenditure being used in that event. So if I don't get someone, I do run the risk of deviating a lot of my attention away from attending to potential clients and overseeing the processes happening in the photo booth.

[00:29:49] Paul Miller: <Q>Is the first challenge getting as many people to use the technology in their event, and then scaling from a networking perspective?</Q>

[00:29:56] Paul Miller: <A>Surely that's your first challenge. You're building that use case that you'll use to potentially become a franchise-type model — here's the upside, this is how you engage people to use it. You start building all the tools that will then become what you sell. A more powerful model was not to sell to the end customer, but sell to people that have the biggest influence over the end customer network — they're already running events in your context, and this is an add-on where they can add an extra margin.</A>

[00:27:36] Juan Torres: Yeah, that's what I was actually thinking of doing — hey, do you have this event happening? Let me just install this so people can use it. I'm not going to charge you anything. Just use it so people can see it. I'll distribute my business cards and we'll see what happens.

[00:29:49] Paul Miller: ▶ Only other practical advice I would give you is when you go to those first events, don't go alone. Always have someone else come with you, because then they can step back and observe what's going on — you might get caught up in the practical, and you don't see the interaction with the customers. So don't go alone.

[00:31:00] Juan Torres: Yeah, I think B2B is a possibility because I was actually doing some research on the competition and they seem to rely on a couple of providers of this AI booth provision. I know there's an AI booth here in San Diego that is trying to do AI transformation too, but it seems to be from the same providers of AI transformation. And from what I've been able to see just from the images, it's not that dynamical. So there might be a possibility for a future B2B provider of the SaaS.

[00:32:05] Juan Torres: Potentially in two weeks, I think, for those first events.

---

<!--SEGMENT
topic: Digital Signage SaaS Platform Demo
speakers: Ryan C, Paul Miller, Juan Torres
keywords: digital signage, mini PC, retail screens, estate agents, CRM integration, remote update, flow builder, heartbeat monitoring, Chrome kiosk, Cursor, console logging
summary: Ryan C demos his digital signage SaaS platform, which runs on mini PCs attached to retail screens and is managed via a cloud dashboard. He walks through recent quality-of-life improvements including remote OTA updates, heartbeat/power-loss detection, and a diagnostic console log capture tool for debugging. He also shows the flow builder for non-estate-agent clients and the CRM-integrated property feed for estate agents. The group discusses pricing (£45/screen/month), scaling challenges with large retail chains, and the potential for international expansion.
-->

[00:32:33] Ryan C: One of the things I've been trying to scale is my digital signage business [tool:Digital Signage SaaS]. I've been building software that sits on a little mini PC that sits on the back of screens, essentially, that sit in retail stores, both internally and externally. So sitting in front windows pointing out into the street and stuff inside as well.

[00:33:03] Ryan C: One of the things I found a lot is when I'm trying to debug the local machines, I'm having to remote into the machine and then manually pull console logs out of Chrome dev tools, because the little mini PCs are essentially just really weak laptops packed into a little machine. Not knowing what I was doing at the start, I was loading 4K videos onto it, and it was degrading over time because of the onboard GPU not dealing with things properly.

[00:33:49] Ryan C: I've got nine screens up and running now. When you go into a screen, I've got full detection on power loss. They've all got heartbeats built in now where they're reporting back every couple of minutes. And if it drops — so their power goes off and they get a power cut — I'm working on building a script that auto logs back into the machines and then auto-starts the thing itself.

[00:34:53] Ryan C: ▶ The pièce de résistance is that I've added a full update feature. I can now do that remotely. I've got different versions, so as I update the machine code, I can literally go in and press update and it will automatically push that to the screen, download it on the mini PC, switch it over, run the updater, pull the files out, compress the old one into a backup — because if it fails, it'll just restore the old one — and then relaunch it all automatically. Takes about two minutes, and the screen is only down for about two seconds.

[00:36:01] Ryan C: I've got Lightweight Capture, which captures all the console events. So I can then view all of the console from the screen, copy it all, and just chuck it straight into an MD file in Cursor [tool:Cursor]. I can download that file if I want to and feed it into Cursor and say, right, have a look at this, what's going on? And then I have the ability to have a deeper capture, which I can toggle on and off, because that's a bit more taxing on the CPU and GPU on the machine, but it's useful for debugging.

[00:37:04] Paul Miller: <Q>Are these people running content that you generate from your agency, or what's the content?</Q>

[00:37:18] Ryan C: <A>It's 50-50. I've got a lot of estate agents, so I'm pulling from their CRMs, putting their property feeds on actual screens. It pulls through properties, pulls through their staff, it's got a full QR system. They can put in custom slides or even custom videos that play and intercede between the properties, they can stick in all their reviews. It syncs with their CRM every 60 minutes — available under offers, lettings and sales.</A>

[00:38:46] Ryan C: And then you've got non-estate-agency clients. This aesthetics company, for example — you've got this really cool flow builder, which is a full node builder essentially, where you can add image nodes, reviews, custom slides, you can embed HTML, and you can change how long it displays for, change the media from the media bank. This is all self-administrable — they have a client login where they can come and do this themselves.

[00:41:00] Ryan C: ▶ I charge £45 per month per screen, so all I need is 100 screens and that will be enough to live, and then everything else is a bonus after that. I'm up to nine at the moment, and that's literally just walking into stores and going, hi, you've got a screen, how much are you paying a month for that?

[00:41:25] Paul Miller: <Q>What about some of those bigger real estate agents that have got franchise, nationwide franchises?</Q>

[00:41:34] Ryan C: <A>It's how I get to the people that make the decisions in head office that's my current issue. A lot of them dive into really long, awkward, horrible contracts with competitors. The screen software business — some of the software is awful and it looks terrible, but they tie people in by two, three years, or they lease the screens to them on the condition they use their software.</A>

[00:42:16] Paul Miller: I might have some people in Australia that want this, but flick me an email.

[00:42:40] Ryan C: ▶ I've built in all the tools to be able to support it remotely, completely remotely, and if I can do the install, it's just plugging a mini PC into a screen and giving me remote access to it, and I can set it all up from here.

[00:43:13] Juan Torres: <Q>So Ryan, if you were to summarize this in one sentence or two, what does this do in summary?</Q>

[00:43:21] Ryan C: <A>It does retail screens, essentially. I provide the software that powers them and enables them to remotely manage. I build software that sits on a little computer that attaches to the back of these things via HDMI or DisplayPort, and then this cloud software talks to them.</A>

---

<!--SEGMENT
topic: Digital Signage AI Content Generation Ideas
speakers: Juan Torres, Ryan C, Bastian Venegas Arevalo
keywords: HTML generation, Claude, Nano Banana, image generation, AI content, screen templates, token cost, flow builder nodes, diffusion models, content automation
summary: Juan Torres suggests Ryan C could add AI-generated HTML slide templates as nodes in the flow builder, referencing Claude-based GitHub plugins for beautiful HTML presentations. Ryan C responds positively but raises concerns about token cost unpredictability and the non-technical nature of his client base. He suggests Nano Banana as a more cost-predictable image generation integration, and notes he currently does a manual version of this using his Google subscription.
-->

[00:45:49] Juan Torres: Have you thought of encoding or using one of the nodes to generate HTML codes? There's a GitHub set of plugins for Claude [tool:Claude] that helps with the edification of those HTML presentations to just look beautiful. They're based on specific templates. So I'm thinking, maybe you can give the user five specific templates, and based on that, the person can edify the HTML representation of that template, and in that template you can actually edit the wordings, the titles.

[00:47:29] Ryan C: <Q>So what you're saying is design your own screens, essentially?</Q>

[00:47:34] Ryan C: <A>The way I might approach that — because obviously if you're creating HTML, the token spend on that could be very different depending on what they created — I'd probably just link it up with Nano Banana [tool:Nano Banana] and have a very specific set of rules and say, right, you get five screen generations a month or whatever for a bolt-on price. And then they can go in and just tell it what they want it to be. It already has their logo and stuff like that, so it can feed in all the assets that they might need and do it that way.</A>

[00:48:20] Ryan C: ▶ I know it's not massive tokens, Bastian, but obviously there is that. It could be anything. Whereas Nano Banana, you kind of know what the per-image cost is. So I can cost it out a little bit easier. I just don't want to make it too complicated, because a lot of the people that use these don't do technology.

[00:48:51] Ryan C: It needs to be idiot-proof, if I'm being completely honest, because most of the people that are doing these are just good at the thing they do. They don't have a clue about tech.

[00:49:18] Juan Torres: ▶ Just use, you know, try for yourself maybe five templates that you know are going to modify really good HTML code or even your Nano Banana image generation, and then put them as five selections that you have for a node and see how people actually play with it. You don't even have to make it complicated for yourself.

[00:49:45] Ryan C: At the minute, I just say, right, what screens do you want? I'll give you a couple to start off with. And I just use my Google subscription to generate stuff. I get it to do a bit of research on the site and say, right, I need a couple of just generic screens I can lob on there until they tell me more specifically what they want. So I'm kind of doing a manual version of that at the minute.

---

<!--SEGMENT
topic: Anthropic Claude "Fable" Model Release
speakers: Paul Miller, Ty Wells, Ryan C, Andrew Nanton, Juan Torres
keywords: Claude Fable, Anthropic, Opus 4, reasoning effort, token cost, API access, subscription limits, security analysis, medical AI, cache invalidation, Codex
summary: Paul Miller announces Anthropic's release of the "Claude Fable" model (a cut-down version of "Mythos"), available on Claude subscriptions until June 22nd before switching to token-only API access. The group discusses the model's strengths for macro-level code refactoring, reasoning effort settings, cache invalidation behavior, and the reset of usage limits. Ryan C plans to use it intensively before the paywall kicks in, including for security reviews of his existing codebase.
-->

[00:59:16] Paul Miller: <Q>Has anyone been having a look or play with today the Mythos release that's come from Anthropic [tool:Anthropic]? So they did a big update overnight, making a cut-down part of Mythos available. There's a part of the medical side and a part of the security analysis side that is locked down. But what are they calling the model?</Q>

[00:59:57] Ty Wells: Fable.

[00:59:57] Andrew Nanton: Fable.

[01:00:00] Ty Wells: <A>Yeah. But they also say that on the 22nd, that's where they may go to API usage for Fable only.</A>

[01:00:10] Paul Miller: <A>It comes off your free, mostly subsidized allocation from the 22nd. So up until the 22nd, it's available to use with your Claude subscription [tool:Claude], but after that date, it's token only. You have to buy tokens for it. Two times — this is expensive.</A>

[01:00:37] Paul Miller: So as you guys may be familiar with my day job story, my CTO has made the deep dive into AI, and when we had our morning stand-up meeting, already half my team had already been running the model and giving feedback as to how effective it was with improving our business.

[01:01:34] Ryan C: Not at the minute, but I'll let you know next week because I'm going to try and build my entire taxi app with it in the next week before they remove it from me and make it really expensive.

[01:01:45] Juan Torres: Ryan, weren't you the guy that created the parking lot app?

[01:01:50] Ryan C: No, that's not me, but I'm going to shamelessly steal it because I've managed to find somebody that might want something similar here. Because that would be a moneymaker. I'm pretty sure he's almost at $20,000 already. I chatted with Scott last week and he said he's already nearing 20 grand and he's had it live for like three weeks.

[01:02:24] Paul Miller: So Bastian had a point there — it looks like Anthropic reset everyone's limits from today. So if you're worried that you're going to burn through a whole lot of your limits on your Claude subscription in the last two days, it looks like it was reset recently, so you've got a lot more to use potentially on Fable.

[01:02:55] Ty Wells: Yeah, I turned it on probably a couple hours ago and I was monitoring, and I went to check the usage and it was reset. So that's a setup, by the way. You're going to feel like you've got more.

[01:09:06] Paul Miller: ▶ My feedback just on the Mythos that I tested this morning: if you're wanting to jump into it, it seems better for the bigger, more macro-level task than a specific smaller problem. So if you said, look, the app has got a lot of issues, it's not getting to the overall end objective — how do we re-look at the code and amp it up by 50%? What I've been able to do with this new model is just say, look, here's where I'm at, I got stuck in all these areas, look at a macro level, how can we change the whole app's approach and fix it — and bang, done. It's able to keep thinking and working and come up with the best outcome.

[01:11:00] Paul Miller: ▶ The feedback was, you don't have to set it to the top level of thinking to get a substantial increase on the Opus model. So you could do it with "high" and still get a massive increase with what you currently have with Opus [tool:Claude Opus].

[01:11:48] Paul Miller: ▶ If you change your reasoning effort, your cache is invalidated. So stick with the same effort. Don't change the effort as you go along. My suggestion would be start with "high."

[01:12:11] Ryan C: Fable is about to get abused by me till the 22nd of June, that's for sure. I'm going to use nothing but, and I'm going to use extra reasoning, and I'm going to upgrade myself to the $200 plan and try and build a bunch of stuff in between now and then. And I'm going to get it to do a bunch of security reviews on my existing stuff and see what it can find.

[01:12:28] Paul Miller: What they're saying on security — anything on the security side, it will re-point it to Opus 4.8.

[01:12:38] Ryan C: <A>Well, they're saying that if you're trying to find exploits, it says sometimes it'll kick it in, sometimes it won't. So what I'm going to try and do is test a few different problems and see what it will kick down and what it won't, and then refine it from there.</A>

---

<!--SEGMENT
topic: AI Perception, Student Loans, and Forensic Psychiatry
speakers: Andrew Nanton, Paul Miller, Adam, Ryan C
keywords: AI perception, chatbot misconceptions, forensic psychiatry, AI guidelines, eval suite, ChatGPT, student loans, compound interest, AI adoption
summary: Andrew Nanton shares his work developing AI practice guidelines for forensic psychiatrists, noting that public and professional perception of AI remains largely limited to chatbots, with little understanding of systematic AI processes or evaluation frameworks. Paul Miller and Adam add observations about AI's practical value being best communicated through eliminating tedious tasks rather than abstract capability claims. Adam briefly recounts a failed attempt to use ChatGPT's extended thinking to solve a student loan repayment optimization problem.
-->

[00:52:06] Adam: One thing I did run into with AI-related is my daughter calls me and she's like, can you help me figure out how to repay my student loans — like what would be most advantageous where I pay the least interest? So I throw it into ChatGPT [tool:ChatGPT], whatever it is, the extended thinking. And I was surprised — ChatGPT really had a lot of trouble figuring out what to do, which I thought this would be like super easy to do with AI.

[00:53:00] Paul Miller: <Q>Did you try Claude's latest model?</Q>

[00:53:03] Adam: <A>No. I just basically started giving ChatGPT hints until it started being reasonable.</A>

[00:53:39] Adam: Well, in the US, you can have different situations where you can trigger interest to compound, or if you're very careful, you cannot trigger a compounding event.

[00:54:15] Paul Miller: So, Andrew, did you have any updates for this week?

[00:54:37] Andrew Nanton: I am continuing to work on a couple of different things, including a sort of practice guideline for forensic psychiatrists about AI use. And in doing so, I've been talking to a lot of different people and getting a lot of different perspectives. It's been interesting to see where the tide of public sentiment around AI has been — over these last few years, a bit of a rollercoaster, and I think we're back in another sort of more negative time.

[00:55:00] Andrew Nanton: What I've learned from this is that when you say AI to anybody, all they think of is a chatbot, and they really struggle with the idea of anything other than what it might look like other than a chatbot, and how a more systematic process might work. Even just approaching ideas like, oh, this is what an eval suite looks like, and how you know if things are getting better or moving backwards — that is really foreign territory to people.

[00:56:14] Paul Miller: I think it's interesting because across so many different industry types, people seem to have a real issue converting the power of what AI is to what practically that means outside the chat where most people have had familiarity with.

[00:57:38] Andrew Nanton: ▶ What are the tedious parts of your job? Because those are probably the best candidates for AI intervention.

[00:57:46] Paul Miller: Well, in my industry, where it's tracking salespeople's interactions with retailers — no one wants to go through the notes of everything that's been done. Everyone wants to know that it's been done. No one wants to read anything. No one wants to do reviews of what people have done in the week. Everyone hates quarterly or annual reviews because they somehow need to quickly delve into the depths and come up with practical examples. ▶ Doing all the boring crappy stuff and making other people look good is half of it really. But that's not selling AI — it's selling the magic of what horrible things it takes us away from.

---

<!--SEGMENT
topic: Apple WWDC Reactions and China Chip Innovation
speakers: Paul Miller, Ryan C, Juan Torres, Andrew Nanton
keywords: Apple WWDC, Gemini, Apple Intelligence, M5 Ultra, Mac Studio, AirPods EQ, Huawei 3D chip, AI diffusion models, semiconductor sanctions, China AI, smartphone restrictions
summary: The group briefly reacts to Apple's WWDC announcements, with Ryan C expressing underwhelm at the Gemini integration and delayed M5 Ultra chip release due to RAM shortages. Juan Torres raises Huawei's new three-dimensional chip as a significant breakthrough, noting that Chinese diffusion models outperform American competitors (except GPT Image 2 and Google Imagen Pro) and that US semiconductor sanctions have driven Chinese chip innovation. The conversation briefly touches on smartphone restrictions for children in schools.
-->

[01:04:17] Paul Miller: <Q>So, yeah, what did everyone think of the Apple updates? Obviously, they're coming from quite behind in the AI side of things, but with the partnership with Google.</Q>

[01:04:34] Ryan C: Scott and I were just sitting there going, please give us the M5 Ultra chip [tool:Apple M5 Ultra] with 512 gigs of RAM. I need my personal assistant. Because there were rumours they were going to — normally with WWDC, they do all this, and they're releasing a couple of new chips as well. They're going to be in the Mac Studio [tool:Mac Studio], and they did that last year with the M4. So we were really hoping, but I think the RAM shortages have kind of screwed that, so we'll get them in October, I think.

[01:05:08] Ryan C: Other than that, it was a bit underwhelming. It was like, cool, it's everything I expected it to be. You're using Gemini [tool:Gemini] because your own AI sucked. It does everything that Gemini does in a nice, pretty way within the Apple UI. They've dialed back on Glass because Glass is really annoying to use. You can finally EQ AirPods [tool:AirPods]. Thank God for that.

[01:06:00] Paul Miller: In New Zealand and Australia, you're not allowed to use smartphones at school. A lot of people thought it was going to make little difference, but it's made a massive difference in schools.

[01:07:20] Juan Torres: <Q>Have you guys heard of Huawei's new three-dimensional chip?</Q>

[01:07:28] Paul Miller: <A>Yes, yes, that looked very interesting.</A>

[01:07:35] Juan Torres: Yeah, really interesting breakthrough. I was just testing for my AI booth application, comparing and contrasting the different diffusion models and which ones I'm going to be using for the application. And other than GPT Image 2 [tool:GPT Image 2] and Google Imagen Pro [tool:Google Imagen Pro], the Chinese models decimate the American competition in the AI diffusion models. And now because of the sanctions, the Chinese have circumvented a lot of the manufacturing technology of the chips by innovating into having these three-dimensional chips, which I think is really, really interesting.

[01:08:31] Paul Miller: ▶ Well, they've had to — they've just had no other alternative, and there's a hell of a lot of innovation that's going on in China because of it, because the demand is there.

---

=== UNRESOLVED SPEAKERS ===

- **Bastian Venegas Arevalo** — appeared in the raw transcript; no canonical alias mapping was available in the SPEAKER_ALIASES context. Name passed through unchanged.
- **Adam** — appeared as "Adam" with no surname confirmed in alias map; passed through as "Adam" (surname "Chapman" appears once in transcript as a self-introduction artifact but was not confirmed in alias map).