=== SESSION ===
date: Unknown (Tuesday)
duration_estimate: ~2 hours 15 minutes
main_themes: ShipKit project updates, OpenAI agent builder review, Vercel/cloud infrastructure, agentic AI development, voice AI tools, multi-tenant architecture, LLC/business setup, custom GPT workflows, AWS/SOC 2 compliance, IDE tooling comparison

---

<!--SEGMENT
topic: Pre-meeting Casual Introductions
speakers: Tom Welsh, Marc Juretus, Paul Miller, Mitch, Ty Wells
keywords: ShipKit, GitHub Copilot, IntelliJ, PyCharm, Visual Studio Code, traveling salesperson problem, agentic capability, New Zealand, route optimization
summary: Participants exchange informal greetings and brief project updates before the meeting officially starts. Topics include Marc's work teaching GitHub Copilot integration with IntelliJ, Tom's ShipKit website work, and Paul's early description of combining agentic research with the traveling salesperson problem for retail route optimization in New Zealand.
-->

00:00:17 - Tom Welsh
Hey, Marc.

00:00:20 - Marc Juretus
Hey, Tom. How you doing, buddy?

00:00:22 - Tom Welsh
Not bad, yourself.

00:00:24 - Marc Juretus
Ah, just finished. I don't know what time it is over your way. I just pretty much checked out of work about an hour ago.

00:00:31 - Tom Welsh
11 p.m. Oh, a little different then.

00:00:53 - Marc Juretus
Working on anything interesting these days?

00:00:55 - Tom Welsh
I'm just going through the ShipKit [tool:ShipKit] stuff. I use ShipKit to update my company website, and I'm just working through some stuff with that. It went really well.

00:01:13 - Marc Juretus
Still, I got on with Patrick more of the, using the GitHub Copilot [tool:GitHub Copilot] and stuff, because they want me to do some stuff where teaching people how to use that to develop with. So I wanted to kind of see what his approach was to doing that. I have the $10 one at home, but we use the IDE IntelliJ [tool:IntelliJ]. I got to kind of bundle in GitHub Copilot with that. So I'm trying to find the best way to present that.

00:01:49 - Tom Welsh
Yeah, I used PyCharm [tool:PyCharm], which is by JetBrains.

00:01:54 - Marc Juretus
Yeah, it's not bad. It's good. I'm a Visual Studio Code [tool:Visual Studio Code] person, as far as when you're adding the plugins and all that, in my opinion. That's the one thing I think IntelliJ is better, but the other stuff, I don't see the difference.

00:02:12 - Tom Welsh
An IDE's an IDE.

00:02:15 - Tom Welsh
Hey, Paul, Mitch.

00:02:17 - Paul Miller
Hi. Howdy.

00:02:36 - Paul Miller
God, I'm loving it, but I'm still off-grid. I'm not using any of the base templates. I've got my little proprietary app, but I'm using all the cool bits in ShipKit to do components, like I added some agentic capability into my app. So I've combined traveling salesperson with the agentic research.

00:03:08 - Paul Miller
Which is interesting because you can't throw AI muscle at brute-forcing the traveling salesperson problem because you're dealing with a quantum of data that is — I think every atom in the universe is less than the combinations of the 500 retail stores just in New Zealand alone.

00:03:56 - Tom Welsh
It's the combinations for 500 stores for routing optimization.

00:04:02 - Tom Welsh
So what you're saying is, after you're done with this, you're going to have no hair.

00:04:07 - Paul Miller
Yeah, look, it's dropping out and I'm creased right now.

00:04:21 - Paul Miller
That's the first question for Brandon. It's like, where's the hair replacement?

00:04:43 - Ty Wells
Hey, guys.

00:04:44 - Tom Welsh
Hey, Ty.

00:04:45 - Paul Miller
Yeah, my app is finished. And I had a new customer randomly call and say, oh, you wouldn't happen to have an app that does this. So I already have one of the top 10 consumer goods businesses in the world giving me a purchase order for this — well, thank God it's not vaporware anymore.

00:05:06 - Ty Wells
Good, congrats.

00:05:08 - Tom Welsh
That's the hallmark of a great salesman. Create the demand, then create the product.

00:05:14 - Paul Miller
Yeah. Well, if you read the Microsoft story, that's how Bill Gates got set up with Microsoft. He sold something he didn't have and then hacked away at it.

00:05:35 - Marc Juretus
That was DOS, right?

00:05:35 - Tom Welsh
Yeah, he wrote it on a PDP-11, and hadn't booted it on a PC until the day he took it out there. Real seat of your pants.

00:05:43 - Marc Juretus
Yeah, you gotta love that testicular fortitude there, boy.

00:06:17 - Tom Welsh
That's the whole thing, wasn't it? Like Larry Ellison was stuck in a plane, so he couldn't get there in time. Oracle could be ruling the world for everything.

00:06:29 - Tom Welsh
I had dinner with Larry Ellison back in the 90s with a company I was with. He was a funny dude. Intelligent as hell, but funny.

00:06:40 - Paul Miller
They were okay to deal with in the early 90s, because I was living in the UK, and we started using Oracle [tool:Oracle] in the really early days. It was a real breakthrough, because you only had DB2 [tool:DB2] as a relational database. And Oracle would run on a Novell [tool:Novell] server, so that's what we did. And then I ended up running on a Sun box, and wow, that was amazing.

---

<!--SEGMENT
topic: Meeting Kickoff and Tom's ShipKit Website
speakers: Brandon Hancock, Tom Welsh
keywords: ShipKit, Vercel, Supabase, cybersecurity, ransomware, analytics, Vercel Marketplace, CLI, subscription model, chat app
summary: Brandon officially opens the meeting and Tom shares his progress rebuilding his cybersecurity consulting website using ShipKit. Tom describes repurposing the chat app subscription template, adding a security assessment widget, and resolving a Vercel Marketplace/Supabase conflict by creating the database directly from Vercel's storage section rather than through project creation.
-->

00:07:17 - Brandon Hancock
Yo, yo, everybody. Hey. Let's get a screenshot going. Perfect. Hope everyone's Tuesday's been awesome so far. Pasting in the schedule real fast.

00:08:03 - Brandon Hancock
So if you have questions, Tom, you can lead us off, buddy.

00:08:12 - Tom Welsh
Yeah, I've got nothing major to report. I've been working on ShipKit [tool:ShipKit], did my website with it today, been playing with it. It's pretty cool. Just repurposing it — did the chat app first, obviously, and then just see how it worked. And then just threw all that in my code, pulled the AI docs across and rules, and then said, redo my website and make it nice, which I basically did. And now I'm playing catch-up, writing collateral to put for all the links. But yeah, really impressed.

00:08:45 - Brandon Hancock
<Q>That's awesome, man. Did you decide gradient, no gradient?</Q>

00:08:48 - Tom Welsh
<A>Oh, yeah, I've got rid of the gradient. I wasn't sold on that to start with anyway. And now I'm doing the persnickety parts, like, oh, that font is different from that font. Let's fix this.</A>

00:09:00 - Tom Welsh
And one of the reasons I'm doing this is obviously there's been a whole bunch of cybersecurity stuff this year where a lot of stuff's been ransomware. There's been big bits out in the press. So I'm trying to get in the back of that and just push the services. And so I've got a small assessment thing, like five or six questions you answer. Oh, you're at risk. You want me to come and pay a visit? So, yeah. And it's got an email. So I've used your template for the chat app subscription model. I've used that as a template to then create my template.

00:09:40 - Brandon Hancock
You're cruising, man. I'm excited. As soon as you start posting it and going live and get some traffic, I would love to hear how the journey goes.

00:09:48 - Tom Welsh
Yeah, cool. And I've already had that Vercel [tool:Vercel] instrumentation on the previous website, but I've tweaked it a bit more now on the new one.

00:10:00 - Brandon Hancock
▶ Guys, just a quick heads up. Tom is wrapping up websites, so he's about to start sending traffic to it. So he's setting up Vercel Analytics [tool:Vercel Analytics] just to see, super high level, how many people are on, what pages are they going to. So it's literally like a two-click install to get some pretty nice starter analytics.

00:10:25 - Tom Welsh
Oh, and one other thing. So yesterday I was playing about with ShipKit, and I was setting up the chat app, and because I had a Vercel Marketplace purchase of Supabase [tool:Supabase], I was having problems because I set up a Supabase app. So what I've had to go through — so you go into Vercel, then instead of creating a project, go straight to storage and create a database straight off, and then that worked.

00:10:53 - Brandon Hancock
Tom hit an issue we've never seen before. So Tom's Gone Rogue is the lesson. But I'm glad you got it working.

00:11:05 - Tom Welsh
▶ In the end of the day, it's quite good because it's also then back to Vercel with the CLI, and I get to pull down all my env files quite happily.

00:11:17 - Brandon Hancock
All right. Well, please keep it — like I said, I'd love some screenshots once you start getting some launch and some traffic. That's the best feeling, man, when the internet works its power and just sends people your way.

---

<!--SEGMENT
topic: OpenAI Agent Builder Review
speakers: Brandon Hancock, AlexH
keywords: OpenAI, agent builder, Next.js, N8N, Crew AI, ADK, agent-to-agent communication, deployment, chat kit starter template, error rate
summary: AlexH asks for Brandon's assessment of OpenAI's newly launched visual agent builder UI. Brandon rates deployment ease a 10/10, comparing it to N8N's simplicity, but notes significant limitations in agent-to-agent collaboration compared to frameworks like Crew AI or Google's ADK. He also reports a ~20% error rate likely due to launch-day traffic.
-->

00:11:28 - Brandon Hancock
Alex, you're up next, buddy. What's going on?

00:11:33 - AlexH
I wasn't ready for this, but I'm just hanging today. My only question is more of a broad question. <Q>I know you posted a video on OpenAI's new agent builder, the UI builder. Just curious to hear your thoughts on it.</Q>

00:11:52 - Brandon Hancock
<A>Yeah, so high level, I am insanely impressed, first off, on ease of deployment. With it, like, it felt like N8N [tool:N8N] level simplicity for deployment — just like click and boom, you have a working deployed agent. So literally 10 out of 10 experience on the act of deployment.

The act of hooking it up to your Next.js [tool:Next.js] project, there's a starter template that they have — it's called, I think I linked it, but it's something like chat kit, but there's a chat kit starter template. And all around, it was pretty straightforward in order to get it hooked up.

The only thing that I would say is kind of a downfall right now is extensibility and workflow customizations. Like, what I mean by that is, you really don't have agent-to-agent communication. Like, that just doesn't exist. It's like agent one does its thing and then just throws everything over the wall to the next. So you're not getting as much, like, with a Crew AI [tool:Crew AI] or an ADK [tool:ADK] of allowing agents to collaborate and work on stuff — that's basically non-existent in there. It's single agents doing work, and then passing things out to saving it to state or passing it to the next. So there's not really delegation, or anything like that, what you would normally get if you were to use an ADK or a Crew AI.

So, on agentic-ness, a six, but it really makes up for it in their ease of deployment. I was shocked when I was making that video. I was like, this is how it's supposed to be. So, yeah, ▶ I think ADK really needs to step up their game is my key takeaway after playing with that. And I hope they do, because they ate their lunch in one product launch.</A>

00:14:07 - Brandon Hancock
Oh, one other thing I will say, I did detect like a 20% error rate. I have no idea why. I don't know if it's because it was right after launch, but just if you would kick it off sometimes, their stuff literally two out of 10 times would just die. No explanation. It would just die. So I'm hoping it was just a hey, we launched it a day and a half ago or a day ago, so maybe they're getting flooded. But that was a little unsettling.

▶ The cool part is, this is the worst it'll ever be. I'm sure they will soon add even more features and functionalities in there. So OpenAI [tool:OpenAI] — they're no joke. They're crushing it.</A>

---

<!--SEGMENT
topic: Vercel Fluid Compute and Tmux for LLM Chains
speakers: Brandon Hancock, Mitch
keywords: Vercel, Fluid Compute, cloud functions, LLM chain, trigger.dev, timeout limits, Tmux, terminal multiplexer, Cloud Code, Codex CLI
summary: Mitch asks whether trigger.dev or Vercel cloud functions are the right approach for chaining sequential LLM calls. Brandon introduces Vercel's Fluid Compute feature, which extends function timeouts up to 13 minutes specifically for AI/LLM workloads. Mitch then demonstrates Tmux as a productivity tool for managing multiple terminal sessions simultaneously when running parallel AI coding agents.
-->

00:14:47 - Brandon Hancock
Next up, Mitch, what's going on, dude?

00:15:32 - Mitch
My main question. So I was still working out some other stuff, but when a user creates an idea, it would run like an LLM chain — a series of events, inputs get fed to LLM, and then outputs get fed to another LLM. I was about to build it in Google Cloud Functions, but it seems like ShipKit's a bit more moving towards the trigger.dev [tool:trigger.dev] or tool. So just kind of want to stay closer to the ShipKit stack. Would that be the way to go about it, is the trigger.dev situation?

00:16:07 - Brandon Hancock
So, yeah, two things that I would look at. So, one is, I was diving into this yesterday, actually. So, when you're using Vercel [tool:Vercel], which you are, they actually have two tiers for max cloud function timeouts. One is just doing a normal cloud request — on the pro plan, that has a timeout, I believe, of five minutes. On the free tier, it's like 15 seconds, or 20, 30 seconds.

But what they have is, with Vercel Fluid Compute [tool:Vercel Fluid Compute], you can get up to 13 minutes. Because at the end of the day, you're just doing LLM calls. So I have not got to turn it on and try it out yet. But in your case, you really could, I think, do exactly what you want with this — where you're just doing LLM call, LLM call, LLM call. ▶ I think you could get exactly what you want, and you wouldn't even need to use trigger.dev.

00:17:35 - Mitch
<Q>So is it like a sub-service that they have under their tooling? So like whenever I create a Vercel project, it'd be able to add that as like a tool, kind of like their storage kind of thing?</Q>

00:17:48 - Brandon Hancock
<A>Yeah, that's exactly what's going on. It should be a very quick turn on.</A>

00:18:03 - Mitch
<Q>And it's made for LLM calls?</Q>

00:18:04 - Brandon Hancock
<A>Yeah, that's what I was saying. It's exactly for what you're trying to do, which is you're trying to talk to LLM models. You're not doing, hey, bank, or hey, auth. It is all AI calls. Because at the end of the day, all these AI calls, you make the request, and then you're just twiddling your fingers for a minute while the AI does its work. There's actually no compute happening on the server. We're just waiting for a response.</A>

00:18:51 - Mitch
And the only thing is, I love Tmux [tool:Tmux]. I'm officially on that bandwagon. When you're having so many different Cloud Code sessions, and then you have the Codex CLI [tool:Codex CLI], and then have like three different projects — I just recommend Tmux for everyone.

00:19:16 - Brandon Hancock
Mitch has given in to the AI Matrix. It's a tool called Tmux, and it's just a really nice way of creating multiple terminals side by side.

00:19:47 - Mitch
So I can just do `cd` into ShipKit for sale, and then go into Tmux. Then you can name the session. So I can say like, this task page maybe, and then I know this open code window is for the task page, and then I can do another one — you know, I have a task page task, and a drizzle task, and then I can go here and use the custom agent that Brandon's team built for the TypeScript React agent, and then have this one be for the drizzle agent, and have it be on different task documents.

00:21:06 - Brandon Hancock
It's so funny because we have gone completely full circle. In the early programming days, Tmux has been around because developers only worked in the terminal, so they were doing five or six things at the same time. Then we went to IDE, so you had one terminal, and now we're going full circle back to where it's like, oh, we're all working in Cloud Code [tool:Cloud Code], we're doing back to terminal work. So we've literally made a full circle back to the 90s.

▶ The main reason people use it is it's a really nice, convenient way to have multiple terminals running at the same time, because most default terminals, it's one chat per tab, and sometimes you just want four or six terminals just running at the same time. And it's free.

---

<!--SEGMENT
topic: Ty's Interactive AI Presentation App
speakers: Ty Wells, Brandon Hancock, Hemal Shah, Jake Maymar
keywords: ShipKit, Supabase, Drizzle, Gamma, polling, WebSockets, voice agent, Retell AI, Cal.com, Deepgram, Chamber of Commerce, real-time results, trivia, SaaS
summary: Ty demonstrates a live interactive presentation platform he built with ShipKit over the weekend for a Chamber of Commerce AI workshop. The app features real-time audience polling, Q&A submission, slide control, a trivia game, and a voice agent booking system. Brandon suggests adding a RAG-based chat interface using existing slide content as context. Jake highlights the analytics potential for investor pitches.
-->

00:22:13 - Brandon Hancock
I think next up is Ty. What cool projects are you working on, buddy?

00:22:16 - Ty Wells
Well, I'm pushing the limits. I actually started working with ShipKit [tool:ShipKit] on the weekend.

00:22:31 - Ty Wells
Well, I've got a presentation tomorrow at the Chamber of Commerce, doing an AI workshop for businesses. And so I decided I'm going to push ShipKit and see what it can do. So I will show you — I'm going to attempt to show you what I built.

00:23:08 - Brandon Hancock
Can you see my screen? Yeah, yeah, this is awesome.

00:23:12 - Ty Wells
Yeah, so I use ShipKit to build this interface where I control the slides, but I also have an interactive piece in it where I can have these different activities. So what happens is, when they come in tomorrow — assuming everything works, I just started this on the weekend — basically, when they come in, they register, there's a screen that shows basically what, like a landing page.

00:24:03 - Ty Wells
So this is the landing page that's hitting here on a second monitor, basically while the presentation is counting down. So after that, once that's done, then I go to my control here.

00:24:55 - Ty Wells
So I use ShipKit to build this interface. It's cancer awareness month — that's why the slides are in pink, just so you know — but I can pull in the slides. I generate them in Gamma [tool:Gamma], and then I pull them in, and then I can take the slides and associate an activity with that slide. So I can come in here and say, okay, we're going to poll who does ChatGPT [tool:ChatGPT], and that's going to kick off. So when they register on their phone, they basically sit in a waiting lobby on their phone.

00:25:17 - Ty Wells
And it interacts with them — like instead of me saying, hey, show me your hands of how many people use ChatGPT, right, and then did anyone use it this week and so forth. So it does this poll and they can interact with it on their phone, and then they can submit questions on their phone Q&A right up there. And then once I start the slides, I control them here. As I go to the slide with an activity, I can launch the activity so that they can interact. And then it shows real-time results of who's voting what.

00:26:02 - Ty Wells
And then I move on to the next slide when that ends. So that's my interactive presentation.

00:26:05 - Brandon Hancock
Ty, this is breaking my brain, dude.

00:26:22 - Brandon Hancock
<Q>Curiosity on polls. Are we doing polling to keep everyone in sync? Did you end up doing WebSockets [tool:WebSockets]?</Q>

00:26:36 - Ty Wells
<A>Yeah, it's polling, really — the database. The app is pulling back the data so I can set up different things that will show on that landing page.</A>

00:27:00 - Ty Wells
I want to add a chat interface in the app so that they can chat and ask questions if they want to, and get their questions answered right away rather than just being posted there — a little chat on their mobile version so that they can get their questions answered right away.

00:28:37 - Brandon Hancock
▶ The part that you could very easily do is just use the existing chat SaaS application in ShipKit, and just at the very beginning, when you're creating the system prompt, add one little database fetch right here to grab all the presentation slide content, and then just add that in as context to the beginning of chat at the system prompt level. That way, anytime anyone kicks off a conversation, it already has the entire context — they're talking to the slides. So you potentially could reuse some of the existing chat SaaS and just do one database query above, and you're golden.

00:30:40 - Ty Wells
What I have in the lobby while you're waiting before the presentation starts, I've got a link to my voice agent so they can chat with — they can talk with the voice agent and book a time for consultation if they want to.

00:30:55 - Brandon Hancock
Please, please turn this into a SaaS, like, I'm begging.

00:31:01 - Ty Wells
That's how I built it. It's a SaaS. I'm just using it for this presentation, but it's called In-Person. That's the name.

00:31:25 - Jake Maymar
The analytics will be really interesting. You know, what the people are asking, what are the questions they're asking about the slides? The polling is really interesting. But all the engagement analytics, I think, would be really interesting. And when you're shopping this around, that's kind of what investors are looking at — that sort of engagement. ▶ So having the analytics back end, I think, would really tell the story of the thing that you're building.

00:32:18 - Hemal Shah
<Q>A question on the voice agent that you mentioned. What tools and technology did you use for the voice agent?</Q>

00:32:32 - Ty Wells
<A>It's just a Retell [tool:Retell AI] agent that I've got sitting out there. And Cal.com [tool:Cal.com] for the calendar.</A>

00:32:47 - Hemal Shah
So it can schedule appointments and everything as well?

00:32:49 - Ty Wells
Yep.

00:33:13 - Brandon Hancock
I've had a ton of luck with Deepgram [tool:Deepgram]. I have not tried Retell yet, but you've added it to my list. Oh, you can actually straight up call this. That's awesome.

00:33:52 - Brandon Hancock
▶ Deepgram — it's insanely cheap and affordable. They give you $200 in credits. We've had people talk to it for dozens of hours. And it's like, oh, you've used $2. So it's super affordable.

---

<!--SEGMENT
topic: Hemal's ShipKit Setup and LLC/Business Banking Advice
speakers: Hemal Shah, Brandon Hancock, Jake Maymar
keywords: ShipKit, Cursor, Claude Sonnet, context compression, LegalZoom, LLC, S-Corp, EIN, Chase, business credit card, Georgia, single member LLC, self-employment tax
summary: Hemal shares his successful ShipKit setup using Claude Sonnet with only 50% context usage, praising Cursor's improved context compression. He then asks for advice on forming an LLC and choosing business banking. Jake recommends DIY filing over LegalZoom, and Brandon walks through the tax implications of single-member LLC vs. S-Corp, recommending Chase for business banking and a Chase Ink Business Preferred card.
-->

00:34:19 - Brandon Hancock
All right, perfect. Okay. Well, Hemal, you're up.

00:34:23 - Hemal Shah
Yeah, I mean, I started taking a deep dive into ShipKit [tool:ShipKit] videos and tutorials, going through all those things. Kudos to you, Brandon. A lot of content, great content. I cannot imagine how much time and energy you have put into this.

00:34:42 - Brandon Hancock
I think it ended up being like 400 to 600 hours. It was ridiculous.

00:34:59 - Hemal Shah
With the setup course, I was able to run the whole thing with just Claude Sonnet Thinking [tool:Claude Sonnet], I didn't have to use max million, it only used 50% context, so that worked out very nicely.

00:35:14 - Brandon Hancock
<Q>Quick add on that — did you run it with Cursor [tool:Cursor]?</Q>

00:35:18 - Hemal Shah
<A>Yes.</A>

00:35:19 - Brandon Hancock
▶ Cursor's compression has gotten so much better over the past two months, it's insane. It used to be, when you would do any compression, it's like you might as well have just started a brand new chat. Like, it was that bad. But now they're doing a really good job at it. So that makes me happy to hear, because that means it's more affordable and better results.

00:35:43 - Hemal Shah
And also, what I noticed is Cursor is also selectively doing something with the context, where I will see it consuming 50%, and then when I continue asking questions, it may drop to 47%. So they are kind of removing redundancy, removing certain things.

00:36:04 - Hemal Shah
One question I have, Brandon — I'm still going through the chat template, the next steps to set up idea generation and all that. Besides these three standard applications — chat, RAG, and agent — let's say if I'm making some e-commerce website, or some different type of application that doesn't fall into it. To start, should I just copy that prep folder and start from there?

00:36:38 - Brandon Hancock
<A>I would still use the chat project at this point. Just know the immediate next project, I'm so pumped for. It's just a vanilla, basic Next.js [tool:Next.js] application using Trigger [tool:trigger.dev]. So that will be the foundation for most non-AI projects, where you still want the speed, you still want the AI development.

▶ For example, by using trigger.dev and Next.js, we'll be able to make a voice transcription service — like a paid version of Whisperflow [tool:Whisperflow] where we're doing stuff in the background, using FFmpeg [tool:FFmpeg] to cut stuff up. We're also going to do a video shorts app. This template is going to be the catch-all for all non-RAG, AI, and agent projects.</A>

00:37:53 - Hemal Shah
And a non-technical question for the LLC — planning to open a business. I see there are a lot of online banking companies offering services versus Chase or Bank of America. <Q>Any recommendation from you or anyone for beginners?</Q>

00:38:19 - Brandon Hancock
Okay, I have thoughts. Lawyer Jake, you're up first.

00:38:22 - Jake Maymar
<A>Do not take this as legal advice. So LLC — it's just you, right? Okay, so you can basically do it for a very inexpensive amount. I went through LegalZoom [tool:LegalZoom] and I would never use them again because they upsell you so much. It was going to be almost $1,500 because there's so many upsells. ▶ The best thing to do, I think, is just use Perplexity [tool:Perplexity] — do all the research, do deep research around it. You can get pretty much all of it done. I was able to do it for almost nothing. You have to do legwork, you have to read the contracts, but it gets you up to speed with all the different requirements. And then once you do it, you file in your state. I think it's $500, and then you're done.</A>

00:39:43 - Brandon Hancock
<A>Okay, so here's what I've done — free to copy me. Set up LLC. And after that, you get a thing called an EIN, which is your tax number. From there, set up a bank account — they're going to require your EIN. I personally use Chase [tool:Chase], and ▶ if I was you, I would go ahead and set up a business credit card — you might as well go and get points.

Now, a few quick things on tax. When you're creating an LLC, you're basically going to be a sole member or single-member LLC, and at that point you're basically a freelancer, is what you get taxed at. So it is arguably one of the worst tax setups, because you're going to get taxed for self-employment tax. So you'll be making more, charging more, but taxes are gonna beat you up.

▶ What most individuals will do is instead of doing a single-member LLC, if you have a consistent income coming in, you would set up an S-Corp where you set yourself a fair wage — like I'm going to pay myself $8K a month. Whatever is left over in the business is the business's funds. The main reason with S-Corps is you get taxed once instead of getting taxed twice. You also get to control your income.

But if you're just starting out, dude, single-member LLC — it's better to go ahead and start than get super in the weeds.</A>

00:43:57 - Brandon Hancock
▶ I'll send you a referral code — it's Chase Ink Business Preferred [tool:Chase Ink Business Preferred]. That's my exact setup.

---

<!--SEGMENT
topic: Paul's Route Optimization SaaS App Demo
speakers: Paul Miller, Brandon Hancock
keywords: traveling salesperson problem, route optimization, New Zealand, Docker, Google Cloud, PostGIS, agentic workflow, ShipKit, RAG SaaS, Google Cloud Run, queue, Software as a Science
summary: Paul demos his completed beta route optimization app for New Zealand retail sales territories, explaining the mathematical complexity of the traveling salesperson problem at scale. The app uses Docker-based algorithms to generate optimized weekly routes in ~10 minutes, with an agentic AI layer for pre- and post-analysis. Brandon recommends using ShipKit's RAG SaaS GCP setup scripts and Google Cloud Run jobs for deployment, and suggests reading "Software as a Science" by Dan Martell.
-->

00:44:22 - Brandon Hancock
All right, perfect. Okay. I think next up is Paul. What's going on, Paul?

00:44:22 - Paul Miller
Well, I finally finished the beta version of my app. Let me show you — can you see my screen?

00:44:44 - Brandon Hancock
Oh my gosh, I see a beautiful looking app, if that's what you're asking.

00:44:48 - Paul Miller
Yeah, so this is New Zealand. The challenge with New Zealand is like many mountainous countries — in the middle of this island is a huge mountain chain, but the biggest mountain chain is across the South Island right through the middle here. It's bigger than the European Alps. It basically sits between the Indo-Australian plate on this side and the Pacific plate on this side, pushing up the country. So it means that it's very complex. If you want reps to go around or deliveries to go around, you have to work out not just distance, but the mountains that are in the way and the roads.

00:45:50 - Paul Miller
To give you an idea of the size of the challenge — New Zealand is a small country, about 5 million people, and there are 400 supermarkets. You're kind of thinking, well, servicing 400 supermarkets, surely you can just do that in a spreadsheet. The quantum, from a mathematical perspective, is 10 to the power of 1134. So 10 to the power of 80 is all the atoms in the universe, basically.

00:46:54 - Paul Miller
The complexity of working out how to optimize a visit route — the traveling salesperson problem [tool:Traveling Salesperson Problem] is a big problem, because you can't brute force it. Even with all the GPU capacity in the world, you can't brute force it.

00:47:00 - Paul Miller
But what I've got basically is it splits everything into territories automatically and says, all right, how many — how should we group, if I give you a list of stores, how can you group those stores and how many salespeople can you get away with? So I've got customers that come to me and say, I want to reorganize my business, but I don't know if I'm optimizing the business based on the number of people I've got to do deliveries and to service our customers.

00:47:41 - Paul Miller
So this takes — how many stores do you have to service? How much time do you need to spend in each store and how much driving time do you need? And then it works out initially what size the territory should be. Then it has this next phase — here's one I did last night. So what we've got here is it looks at each of those territories around New Zealand. The green is the time in store, the blue is the travel time, and the orange is idle time or buffer time. So it looks at the optimization level of each territory. And then I can go into a territory, and it shows me on a map, and for each visit day, where you'll travel to.

00:49:22 - Paul Miller
For some parts of more rural parts of countries, or regional areas, we can add more customers by territory, by day, or right across the whole of their selling or delivery cycle, and then re-optimize.

00:49:43 - Brandon Hancock
<Q>Business questions — did they like the sniff test? Are they like, this is awesome? Here's a fat check. Where are we at?</Q>

00:50:03 - Paul Miller
<A>Oh, I've got one customer giving me a purchase order when they just said I can do it. So they're just giving me the money on that basis — that scares the hell out of me because I'm going to make them sign something. Say, look, this is a beta product and you've got to accept that. And then I had another customer call me this morning and said, oh, could you do this? And can we buy this? And I said, well, you will be able to buy it. I've got it in beta format, but you can have it for a month for free as long as you give me feedback.</A>

00:50:43 - Brandon Hancock
That's awesome. That's congrats, man. You set yourself up perfectly.

00:50:56 - Brandon Hancock
▶ I'm literally rereading right now Dan Martell's book, "Software as a Science" [link:Software as a Science by Dan Martell]. There's no better time to read a book than when you're going through the trenches and doing what you're doing right now, because your head's so fresh with new ideas for your new project. I would 100% recommend checking that out.

00:51:35 - Brandon Hancock
<Q>Quick logistic question. You said it was a 10-minute job. Who's processing that for 10 minutes?</Q>

00:51:47 - Paul Miller
<A>I've got a number of Docker [tool:Docker] instances that are running a special algorithm program. I'm running them as local Dockers for now, and I'm going to be putting it into the Google back office stack, because I've got all those credits with them.</A>

00:52:21 - Brandon Hancock
▶ In RAG SaaS, there's one script called `gcp_setup_core.sh`, which is a script that sets up everything for Google Cloud [tool:Google Cloud]. It is overkill for what you're trying to do, but it would be phenomenal as a starting point.

Part two, we need to figure out what is going to trigger one of these jobs. What is the longest one of these jobs can run? Because certain items in Google Cloud have a hard cap at how long they can run. ▶ The safest answer and what I picked for you guys was doing Google Cloud Run Jobs [tool:Google Cloud Run Jobs], because they can run for basically forever. It's a very safe pick to use for jobs that could take 30 minutes, they could take two minutes, it doesn't matter. It's literally just the background job that's just running, and it's going to eventually return the results. And then you could set up a queue if you want to get fancy with it. All of that is literally in ShipKit in the RAG SaaS. So I would just say, take the queue and take the Cloud Run job.

00:54:28 - Paul Miller
So the other parts are — I've spent 750 US dollars on this, which is what that app is. And I know what third parties charge for this stuff. And I know globally, this is easily probably one of the best apps.

00:54:59 - Paul Miller
What I've also added into the mix is there's a lot of questions around your thinking when you're planning a route — what are my objectives, what are the things that are important about the visits, and what is the logic I want to use to keep costs low? And then at the end, you need to be able to analyze what the system has generated and say, well, is that good? Does that go against the thing?

00:55:24 - Paul Miller
So I set up an agentic workflow [tool:agentic workflow] at either end for the system to advise the tool. Given the complexity of the nature of the tool, assign this agent — you have to use the off-the-shelf offering that is, use this logic to do the TSP thing, the traveling salesperson challenge, but use these other things which are queries to the SQL database. I'm using PostGIS [tool:PostGIS], so there's that Postgres that's like geo. And it set up this agent model that looks at, well, here's the problem you're trying to solve, and this is what you could do better, and think about that before you push go.

00:56:15 - Brandon Hancock
<A>To say it back to you — what's happening is your initial 10-minute job is doing the 95% route optimization, where they end up getting a route for a week. Then, for that last mile, last 5%, because we're talking about a total of 20 to 30 spots in a week, you can then pass that to AI with your concerns, and it can do the final optimization. ▶ That is a beautiful combo, very creative. I absolutely love that, Paul.</A>

00:57:00 - Paul Miller
And I've set it up so my business analyst is going to do just some testing of the app for the next week. And then we're going to set up a Zoom call, and we will record it. I'll put the highlights together. And you can see his face — he hasn't seen it at all. He doesn't know anything about it. So I thought, I'll do the secret squirrel, and we'll get it done.

00:57:39 - Paul Miller
And I bought another subscription just this morning for ShipKit. We put it under our company one. So you'll see one coming through for Vladimir Mirkhev.

---

<!--SEGMENT
topic: Juan's AWS SOC 2 Architecture and Ngrok Demo
speakers: Juan, Brandon Hancock, Al Anthony
keywords: AWS, SOC 2, EC2, RDS Serverless, private subnet, security groups, Ngrok, Vanta, FedRAMP, microservices, agentic system, ETL, Fern API spec
summary: Juan describes building a SOC 2-compliant AWS architecture with EC2 instances for an inference engine and web app, connected via encrypted security groups in a private subnet, using Ngrok for client demos. Brandon introduces Vanta as a SOC 2 compliance tool and Al Anthony shares pricing context (~$100K+) for government-grade compliance. Brandon also recommends Fern for API spec alignment between front-end and back-end teams.
-->

00:59:15 - Brandon Hancock
All right. Awesome. Juan, you're up next, man.

00:59:18 - Juan
Can you guys hear me? One, two, three.

00:59:22 - Juan
Yeah, nothing. Just what I've been working on has been, as of last week, just cloud architecture in AWS [tool:AWS], just making it SOC 2 compliant, having the database in a private subnet, and then making the connections between the trio of instances/servers. One being, of course, the EC2 [tool:EC2] instance for the inference engine in the agentic system. One being another EC2 instance for the web app, which includes the web application, the front end, back end, divided into microservices, and then the AWS RDS Serverless [tool:AWS RDS Serverless] database. So now they're all connected. The security groups inbound rules are set for them to be able to communicate between each other in an encrypted manner.

01:00:42 - Juan
And I actually, to demonstrate some of the tests from the agentic system, I used the Ngrok [tool:Ngrok] recommendation that you made last week.

01:00:43 - Brandon Hancock
<Q>Did you like it?</Q>

01:00:44 - Juan
<A>Yeah. It's great. Did you know you could make a tunneling process from a privately-subnetted EC2 instance for anybody to be able to see a web application? So that was great — I was able to give that to my client.</A>

01:01:05 - Brandon Hancock
<Q>Okay, so SOC 2. I've actually been diving deeper into this myself over the past few weeks. So I thought SOC 2 was like, you check all the boxes and you're compliant. But it sounds like you check the boxes, then you go for an audit and the audit needs like three to six months of proof that you've been doing it. I didn't know if you had any preferred people you were picking.</Q>

01:01:57 - Juan
<A>I haven't found anyone to do the audit, but I'm setting everything up for when the audit has to be carried out for it to pass. The only thing that I have to do in order to pass through SOC 2 is have login systems for people who are going to be using the application. But that's something I wouldn't have a chance to do until the front-end and back-end people finish their portion.</A>

01:02:51 - Brandon Hancock
I saw this group — I literally got an ad for it on YouTube. It's called Vanta [tool:Vanta], V-A-N-T-A, and that's who I was eyeballing. They seem to be one of the main ones for helping with SOC 2 compliance. I've heard anywhere from $20K to $30K, but I'm not certain.

01:03:40 - Al Anthony
Brandon, sorry, I'm doing my dialysis at the moment. So I can't turn on my camera. The platform I'm building is more of a government contracting platform. So those are my requirements that I needed. I know FedRAMP [tool:FedRAMP] itself is going to cost me around half a mil to $600,000 for the license.

01:03:31 - Brandon Hancock
<Q>Is it $100K, like that's base? Or is that for like a huge company doing like $80–90K MRR?</Q>

01:09:02 - Al Anthony
<A>I'll have to really check my notes. I know FedRAMP itself is going to cost me around half a mil to $600,000 for the license. That's crazy.</A>

01:06:29 - Brandon Hancock
I want to share something really quick with you that I think you might like, especially when you're helping out a team that is multiple layers deep where there actually is a full front-end team and a full back-end team. So it's called Fern [tool:Fern], but they do a ton for you. ▶ The biggest thing that they help out with is creating an API spec. Think of an API spec as the middle layer where basically the front-end team and the back-end team both agree that, yes, this is what the API should do. Here's the data that should be returned, here's the data I'm going to pass in, and then both teams work towards the middle to actually achieve it. Fern creates that agreed-upon standard, so both of you can iterate quickly to meet in the middle. It prevents building in silo.

01:07:49 - Brandon Hancock
Also, I stand by this — such a smart dude. ▶ Please, YouTube, LinkedIn — just literally, hey, guys, here's five tips I learned about AWS this week. Even if you just started off with the most basic AWS newsletter, so many people would love that. Five Tip Friday. Coin it here first. Five tips on using AWS to build real-world AI projects in 2025. I think that would absolutely crush.

---

<!--SEGMENT
topic: Morgan's Windsurf Reference Project Workaround and Multi-Tenant Architecture
speakers: Morgan Cook, Brandon Hancock, Juan, Paul Miller
keywords: Windsurf, Cursor, Codium Ignore, gitignore, reference project, multi-tenant, Supabase, Neon, RLS, row-level security, AWS Redshift, charter schools, Next.js, subdomain routing
summary: Morgan shares a Windsurf-specific workaround for using reference projects — placing the reference project as a sibling folder rather than a subfolder to avoid gitignore conflicts. He then asks about multi-tenant database architecture for a charter school SaaS app. Brandon explains the complexity of per-tenant databases vs. shared databases with row-level security (RLS), recommending RLS as the simpler MVP approach. Paul and Juan offer AWS Redshift and RDS Serverless as alternatives for true database-per-tenant setups.
-->

01:15:38 - Brandon Hancock
I think next up was Morgan. Floor's yours, buddy.

01:15:41 - Morgan Cook
Hey guys. I use Windsurf [tool:Windsurf] as my IDE and Warp [tool:Warp] as my CLI client. But in Windsurf with your reference project concept, right, where you have a reference project inside your AI docs — Windsurf doesn't like that so much. You can add it to the gitignore, but then Windsurf doesn't even look at it. Then you can add the negation in the Codium Ignore [tool:Codium Ignore], so that it can find it, and the interactive chat will find it, but the actual background chat can't see it. So you end up with this scenario where it'll tell you it can do something, it goes to try to do it, it can't do it.

01:16:53 - Morgan Cook
So what I did — the solution was to put my reference project as a sibling to my actual project and then create a parent folder for the project as a whole. So that way it's not part of my Git structure, but the IDE can still see the entire project.

01:17:59 - Brandon Hancock
▶ So when you're in Cursor [tool:Cursor] and Windsurf, they have the concept of a Cursor Ignore file. And what you do is when you're building out reference projects, you should be able to add in a cool repo that does something you want to copy. So you could just add it in here and then update your Cursor Ignore to say, hey, I actually do want the projects in here to be accessible by the agents. But for some reason it wasn't working. So Morgan had an awesome idea to just open up the project one file level higher.

01:20:00 - Morgan Cook
Now my next question is — I've got two different projects that have — I want to run them as a service, but they need to be tenant-separate, right? So I want them to all go to the same root website to log in, but then after they're logged in, because they belong to a specific company, I want them to be either redirected to a subdomain or some way to keep the databases separate because they don't want their data to be shared with anybody else.

01:20:38 - Morgan Cook
<Q>I don't know if anybody's done any work to do this in our current stack that exists with Next.js [tool:Next.js] and Supabase [tool:Supabase].</Q>

01:21:06 - Brandon Hancock
<A>Okay, so high-level thoughts. First things first, Supabase — from my understanding, it doesn't have the initial design to do multiple databases. Like, it can do staging, it can do production, but it's all the same database moving forward. It's not tenant one, tenant two, tenant three. So Supabase is slightly out of the picture for what you're trying to do.

You could do something simple like Neon [tool:Neon], but then every time you want to have a new project, you're literally spinning up a brand new database. So you are kind of moving into the world of cloud at this point — you're going to be managing your own everything.

There are two paradigms. You can have the same front-end that leads to N number of back-end databases. If everyone gets the exact same application but they all get separate databases, that's nice, because you're managing one Next.js application and just routing it to different databases. If not, what's about to happen is you are going to, per-organization, spin up an entire virtual private cloud that has its own Next.js running, its own database running — there's a lot of stuff that you're going to have to spin up per client, and each client would get its own subdomain. Whatever you're charging for that project, I would just go ahead and double or triple it.</A>

01:23:53 - Brandon Hancock
<Q>So out of curiosity, which one is it? Is it one front-end, a bunch of different databases?</Q>

01:24:00 - Morgan Cook
<A>No, it's one front-end, and then a bunch of different clients that are using the front-end that need to maintain a separate database. The one is actually for charter schools. And so they don't want any of their content being — well, some of them don't care, but most of them don't want their content to be in the same database as somebody else's.</A>

01:24:26 - Brandon Hancock
<A>I would be curious to push back on that just because, like, data being in the same database — I mean, my Gmail is in the same Gmail database as your database. So, maybe just implement it as a soft tenant, just the same way we do RLS [tool:RLS], but at a tenant level.</A>

01:24:57 - Morgan Cook
Yeah, maybe just do it as a soft tenant — just the same way we do RLS, but at a tenant level.

01:25:00 - Brandon Hancock
▶ I mean, yeah, you could do RLS. At the end of the day, someone from one organization should never be able to fetch information from another organization. So you really could set up RLS and that just out the gate — hey, guys, it's not possible for you to query anything about this other school. I can literally show you the rule book right here. I can't break it. You can't break it.

01:25:43 - Juan
I was going to recommend maybe AWS RDS Serverless 2 [tool:AWS RDS Serverless], because that's the one I'm using right now. Serverless 2 is essentially a cluster of several databases that you can spawn up. You can create URLs for each database that are essentially the authentication method to be able to connect to the database. You would just need to modulate the inbound rules.

01:26:41 - Brandon Hancock
Paul, looking at your question — you use AWS and Redshift for each client, each has their own DB file, very cheap. Would you mind elaborating a little bit more, Paul?

01:26:55 - Paul Miller
Yeah, so it's for our reporting and dashboard client. The good thing with Redshift [tool:AWS Redshift] — it really depends on how you're going to use the databases. We're using those in more of an analytical database because Redshift's like a column-in-memory, large, hyperscale database environment. We do a database file per client because many of our clients are competitors. It's kind of one environment, but the database files are separate. And each of those clients, some of them in turn have their own customers in the database. So that's where we use database rules — each of their clients, while they share the database, you can't do a query without specifying exactly which client can do the query on.

01:28:40 - Brandon Hancock
▶ It's wild because that literally one requirement change — "put it in different databases" — cost you hundreds of hours of work. It's not like, oh yeah, I'll just click. I always love talking to clients. They're like, oh, and it would be cool if it will this? And they literally just wave their hand. And in the back of your head, you're like, oh, that is so much work that you just said.

---

<!--SEGMENT
topic: Voice AI Tools Comparison and LiveKit Latency
speakers: Morgan Cook, Ty Wells, Brandon Hancock
keywords: LiveKit, Retell AI, Deepgram, ElevenLabs, Audiovox, voice agent, latency, WebSockets, system prompt, hallucination, Windsurf, Claude
summary: Morgan asks about voice AI platforms beyond LiveKit, which he's found has latency issues. Ty compares Retell AI, Audiovox, and ElevenLabs on pricing and ease of use, noting Retell's strengths in prompt defense and handling numbers/dates. Brandon recommends reaching out to community member Maxim who solved LiveKit latency using a custom AI inference tool. The segment ends with a humorous exchange about Claude hallucinating about its own file access capabilities.
-->

01:31:10 - Morgan Cook
I had this written down before there was conversation earlier about voice and phone information. LiveKit.io [tool:LiveKit] seems to be kind of a latency problem, and so I was going to ask what other people are using for different voice AI information. Somebody had mentioned Retell AI [tool:Retell AI], and then you also mentioned Deepgram [tool:Deepgram]. <Q>Are there any others that might be useful to research a little bit?</Q>

01:31:41 - Brandon Hancock
<A>Ty, if you want to dive in, because I have strictly done computer voice to text, I have not introduced using a phone. I haven't gone deep in that.</A>

01:31:51 - Ty Wells
<A>So Retell really is a wrapper on top of — well, they have access to ElevenLabs [tool:ElevenLabs]. That's obviously the cream of the crop. Audiovox [tool:Audiovox] — they have good pricing, I've had good success with them in the past, and they continue to release updates. Audiovox, I think they were at like 5 cents a minute, which ElevenLabs could be anywhere between 18 and 22 cents a minute. So it all depends on what you're doing. But Retell is just easy if you want to put together a good prompt, a very defensive prompt in your system prompt.

▶ Make sure you add some defense into that system prompt so they don't reveal it — to protect your prompt from being revealed. And then they have some good things about working with numbers and working with dates, just pronunciations of things you can take for granted, but they do a lot there.</A>

01:33:23 - Morgan Cook
<Q>And have you noticed — which one are you using, if you don't mind me asking?</Q>

01:33:42 - Ty Wells
<A>I use both. I started with ElevenLabs and went to Audiovox and then went to Retell. Just easy to spin up a voice agent.</A>

01:33:54 - Morgan Cook
<Q>And have you done or looked at anything at all with LiveKit?</Q>

01:33:58 - Ty Wells
<A>I have not, because I just haven't had the time. Morgan, fast — Maxim was the main one who used LiveKit, if you want to reach out to him.</A>

01:34:15 - Brandon Hancock
▶ He's actively using it. And he had to use some workarounds with using LiveKit plus a custom inference AI inference tool to go faster to solve that latency problem. So he would be a wealth of knowledge on that.

01:34:34 - Morgan Cook
That's the problem right there. There's nothing else wrong with that application other than the latency in the response. It's enough that it'll put people off when they're on the phone with them.

01:35:11 - Morgan Cook
I mean, I asked Claude [tool:Claude] a question about Windsurf. It said, oh, no, I can access everything, even the stuff that's in the gitignore. I said, I call BS. Tell me what's in my `.env.local` file. And it said, oh, yeah, you're right, never mind.

01:35:29 - Brandon Hancock
Morgan's a beacon with the AI. Morgan is actively getting on AI's bad side. He's on the AI takeover hit list.

---

<!--SEGMENT
topic: Patrick's Custom GPT Voice Ideation Workflow
speakers: Patrick Chouinard, Brandon Hancock, elijahstambaugh, Prem
keywords: ChatGPT, custom GPT, ShipKit, master idea prompt, voice ideation, Cursor, GitHub Copilot, VS Code, Markdown, token cost, MCP, Perplexity, JIRA, Confluence, Atlassian, E-Myth, backward design
summary: Patrick demonstrates a custom GPT he built by splitting ShipKit's master idea prompt into three components — personality (system prompt), workflow.md, and a master idea template — enabling fully voice-driven project ideation on mobile while commuting. This approach avoids expensive Cursor tokens for non-coding tasks. Brandon and Elijah extend the concept to content creation, lesson planning, and using GitHub Copilot for Markdown editing. Patrick also recommends using MCP integrations (Perplexity, Atlassian) within VS Code for deep search and project management.
-->

01:36:00 - Brandon Hancock
All right. I think Elijah, Prem, Patrick, and I apologize if I messed up on the order.

01:36:06 - elijahstambaugh
Yeah. Just Morgan, just to say that there isn't a forgive and forget with AI yet. So just be careful because they're not going to forget.

01:36:17 - elijahstambaugh
Ty, I don't know if you've looked at Kahoot [tool:Kahoot] or Turning Technologies Clicker — both of them have audience response platforms. I think what you're building is significantly better, especially if you could add in live transcription. Imagine in a live transcription that all of a sudden it builds out a deck on some questions from the crowd — that'd be really cool.

01:36:54 - elijahstambaugh
So, Brandon, I was wondering — I know Patrick is on the call. Patrick had a call with me on Saturday, so I really appreciate that, thank you Patrick. Is that something that you guys were planning for him to present some stuff?

01:37:57 - Patrick Chouinard
Yeah. I realized that the first part, the master idea part, did not really benefit all that much from being done in Cursor [tool:Cursor] because — and you mentioned yourself, like, oh, try to talk through it, use Whisperflow and give your entire idea and all that. So in my mind I said, well, why am I going to use a very expensive Cursor token if I can actually do it somewhere else where tokens are not as expensive?

So what I've done is I took the first prompt, the master idea prompt, and I've imported it into a ChatGPT custom GPT [tool:ChatGPT Custom GPT]. But since there is a limitation on the number of characters in the system prompt, I could not put the entire prompt in there. So I've split that prompt into three parts: the personality, which I've used as a system prompt, and I've created also a workflow and a master idea template. I've split the actual workflow of the prompt into an individual file called `workflow.md` and the master idea template for the output template as another separate template.

01:41:25 - Patrick Chouinard
I've added as knowledge the workflow and the master idea template. And the workflow also references the master idea template. So what happens is when you talk verbally with that custom GPT, it actually will use the personality as you define it, but it will use the workflow as a step-by-step process that it will guide you through. So it's not as rigid as it would be in Cursor. And the nice thing is you can argue, so you can ideate, you can truly brainstorm with it. But as you go through the step, it still builds its context. And once you've went through all eight steps, at the end of the eighth step, and you say, yes, we're aligned, you've understood correctly, it will generate a master idea template out of the Markdown template file I've provided.

01:42:24 - Brandon Hancock
<A>So then I just need to take that file and import it back into Cursor. So I did the entire ideation way more naturally, and now I can go into Cursor where Cursor is at its best.</A>

01:42:39 - Patrick Chouinard
Basically, I've just moved the complexity to where it would be better addressed. And I think what Brandon really liked is, since this is now completely voice-based and can run through a mobile device, now I am able to create master ideas — and I've shared some of those master idea `.md` files with Brandon — that were created while I was driving to and from work, just chatting with my ShipKit mentor.

01:43:02 - Brandon Hancock
Guys, that's stupid. This shouldn't be allowed, you know? He literally is basically coding on the way to work. It broke my brain when he was telling me everything.

01:43:26 - Patrick Chouinard
I mean, I think everyone in the group here pretty much has access to ShipKit. If you want to share it, I'm totally blessing on sharing it. I think that'd be a cool thing. No, I absolutely don't mind. And the nice thing, by the way, doing it this way instead of with the other interface with Gemini [tool:Gemini] or Claude [tool:Claude], is that I would have to use Project in those systems, which means I would expose the files. Here, since it's a custom GPT, I can share it and nobody will have access to the system prompt.

01:44:03 - Brandon Hancock
Yeah, no, I think it is — it's so funny, because I was like, guys, internally, I'm being so creative, I'm doing all this cool stuff, and then Patrick comes out, and he's like, I built an idea in my car. And I was like, wait, you did what? You were driving to work and you did what? And I was like, oh, there's levels to this.

01:44:47 - elijahstambaugh
Now I realized I could leverage the same personality, and have multiple different workflows, or different output documents, so I can move, I can change any one of the parts without changing the entire thing. And I could probably put the workflow for selecting the name for the application, or to work on the prompt for generating a logo. Anything that is not coding, I want to move into that framework.

01:45:20 - elijahstambaugh
▶ Yeah, I absolutely love that — the name, the logo, maybe the wireframe — for most of it, you literally could just talk to most of it. And saving very expensive tokens at the same time.

01:45:49 - Brandon Hancock
▶ The main key takeaway is: you already have to know what you're trying to make as the desired output. That's step one. You have to know what you're trying to build. Then you have reference to literally, at this point, like 10, 15, 20 different documents that are all tried-and-true A+ standard prompts for creating prompts. So what you could do is: I have a reference of what creating good prompts looks like, my goal is I want to do something like this, I want an output like A, B, and C. Now that you have a reference of what a good style guide is and you have a reference of the output, you get to create a new template. Nope, that didn't do it. Here's what you did wrong. Update the template. Do it again. And you just do that like five, ten times. And you end up with a very high quality custom template to help you do that specific task over and over again.

01:51:21 - Brandon Hancock
▶ At the end of the day, what we're doing here is creating standard operating procedures. Like, that is what we're doing — we're creating SOPs for AI agents. If you were trying to teach anyone to do anything, that's our true goal with these templates. It's just an SOP for an agent to follow to give you the desired result.

01:52:15 - elijahstambaugh
If you play golf, like I do — work from the hole backwards is what I think you guys are saying, right? Your end result.

01:52:21 - elijahstambaugh
If you really want to peek into my brain, what I was trying to do — there's a book called The E-Myth [link:The E-Myth by Michael Gerber]. It's about basically building, just standardizing businesses. And I was like, how do we do that to code? That's literally the whole idea for ShipKit — my goal is any developer should be able to create the same level of project I should be able to create. And the way I'm going to achieve that is through ShipKit. It is the vehicle that gives everyone the same standard operating procedures I would use to build a project.

01:52:58 - elijahstambaugh
In education, there's a concept called backward design. You start with the end in mind, whatever your assessment is, and then work your way backwards.

01:53:11 - Prem
I think the value in one sense is the intellectual property — you doing some of this heavy thinking and being able to mirror that — that's going to be a continued value for all of us.

01:54:12 - Prem
Hey, Brandon. I just kind of saw these Cursor commands as it was playing today. Have you kind of done that? And again, you have all the templates like the prep templates under the prep templates, right — all the Markdown files. The way I've been doing is drag it and drop it here. But if you kind of create a commands folder under `.cursor`, and then move your Markdown files there, if I say backslash, and then it kind of starts showing all the commands over here, all the templates. So you don't have to drag and drop.

01:56:25 - Brandon Hancock
▶ So super fast — you don't have to drag and drop. I'll show you one thing really fast that might make your life easier. If you go into the settings button, and then same thing, index and docs where you were just at. And then if you click, it says ignore files and cursor ignore. If you click edit that — now hit, go down a line and do exclamation mark. And then hit save. Now if you go back, hit sync again — now if you do `@`, and then type in, you know, generate wireframe — now it's getting both the files. So now if I say slash, it is getting all these three files as commands.

01:58:06 - Brandon Hancock
Cool updates for you, Prem. So update one — as of literally 10 minutes ago, you just got to update that Windows RAG SaaS is good. So I'll be doing a release for that after the call tonight. Thank you guys so much for being patient on that. Heads up, the issue was the way Windows is trying to call the Google Cloud utilities file, like the gcloud CLI — you can't just say `gcloud`, you have to go find the actual path. I don't know why they made it so hard on Windows to use Google Cloud [tool:Google Cloud]. But we had to fix that and that led to a few other small things, but got the thumbs up that it's working.

01:58:53 - Prem
And then there was a new version of RAG SaaS that fixed things for text files, fixed things for Markdown files, and there were a few other things.

01:59:20 - Brandon Hancock
▶ Seriously, thank you for that detailed list. I literally was like, my friend Prem said this is broken, can you please help me fix this? And then I went through and cleaned it up for you. If you run some more stuff, please let me know — I just want to keep getting it more and more perfect for you guys. Prem has been an absolute beast on making and pushing RAG SaaS better and better, so shout out to Prem.

02:00:09 - Brandon Hancock
Here's one client update — the deprecation of text embedding for, that is the model we're using for text embeddings. And apparently I think it's June, or February, it's getting sunset.

02:00:42 - Brandon Hancock
The issue is, as of at least yesterday when I was looking at this in the tools we're using, they don't have text embedding 5 turned on. So it's the silliest thing — they're forcing you to use text embedding 4 today, but that's getting sunset in three months. You'd think they would already have it swapped.

▶ The good news is the way our project is set up, we already have everything saved to the bucket, we already have everything saved to the database. So as soon as things come out, I'll just add a new utility script in there for you guys that can rerun through everything and update it to go from 4 to 5. And the cool part is text embeddings are cheap — text embeddings are pennies of pennies. So if it was multimodal, it would be more expensive, but this will probably be like literally a 20-cent upgrade and everyone's good.

02:02:00 - Brandon Hancock
Patrick, you're up. I just want to address biggie super fast. Here's my recommendation on AI domain endings — I struggle really hard to find .com names now. I have been primarily buying .io and .ai domains just because, yes, they do cost more, but there's fewer of them. ▶ If you can find a good .com name, buy it, 100% — it's $13, $12, versus $90 or $60. And apparently if you just slap on .ai at the end, instant boost in valuation, so if you're trying to sell, that does account for something.

02:07:33 - Patrick Chouinard
And also, to come back on the multiple IDE — I've talked about GitHub Copilot [tool:GitHub Copilot] a lot, simply for one thing. It's the best editor of Markdown so far, because Cursor is awesome for coding, it doesn't do auto-complete in Markdown, GitHub Copilot does. And basically I no longer, or almost never, use Word or PowerPoint or anything — I do everything in VS Code [tool:VS Code] using GitHub Copilot, and I transfer the content in whichever presentation layer I need in the end.

02:08:26 - Brandon Hancock
<Q>Is it $8, $12? What's the price right now for Copilot?</Q>

02:08:30 - Patrick Chouinard
<A>10 bucks a month. I think you can have it for $100 a year if you take it annually. And honestly, it's 300 premium requests per month per developer, and premium is like Claude 4.5 or GPT-5. But if you take GPT-4.1 [tool:GPT-4.1] and GPT-5 Mini [tool:GPT-5 Mini], which for Markdown work are mostly sufficient — they're infinite. There's no limit. They're included at a zero multiplier, so you can use it as much as you want for $10 a month.</A>

02:09:21 - Brandon Hancock
That's awesome. So heads up — like, for a lot of the stuff I've been doing right now, I'm inside of Cursor in Markdown files. Past week has been 70% that, 30% code. So I think I need to swap to GitHub Copilot just because I'm burning through tokens that are very expensive.

02:09:49 - Patrick Chouinard
▶ Be careful, because it has a dependency on version of VS Code, and I believe that Cursor is a little bit behind the real latest version of VS Code, and then it's not going to work. So you might have a challenge there, but honestly, I always have both open on the same project.

02:10:12 - Patrick Chouinard
I took basically $20 a month subscription to multiple projects and it comes out to less than the $200 a month of any max system, but you actually get the tokens overall.

02:12:54 - Patrick Chouinard
▶ And if you connect whichever system you have using an MCP [tool:MCP], for your project management — for example, I'm doing a lot of JIRA [tool:JIRA] right now at work, or Confluence [tool:Confluence], I'm connecting through the Atlassian MCP [tool:Atlassian MCP]. So again, it's Markdown stuff being fed to other Markdown consumers. Or even if you want to ship your documentation within Notion [tool:Notion], you use a Notion MCP [tool:Notion MCP]. The fact that you can manage Markdown easily at almost no cost is incredibly powerful.

02:13:29 - Brandon Hancock
Final thing on that real fast — I was showing my wife this week how she can use Cursor, because she was starting to do some document stuff. Her opening Cursor for the first time on my computer — I was like, hey, just go do the thing you need to do, but do it in here. She was like, oh my gosh, between talking to it, and it doing the writing, and it doing web search and everything else — it is wild, the way we're doing work, blows other people's minds.

02:14:10 - Patrick Chouinard
We literally have like a full year head start or plus compared to the average workforce, which means we get 10x done compared to everyone else.

02:14:16 - Brandon Hancock
▶ Imagine now if you incorporate the Perplexity MCP [tool:Perplexity MCP] in there on top of it. So you can do a full deep search project within a VS Code/Cursor project. And basically when you're within VS Code or Cursor and you use the Perplexity MCP, it gives you web search, but it gives you deep search. Because yes, there are many that will do web search, but none of them will do deep search. So having deep search straight in your IDE is absolutely insane.

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names were not found in the SPEAKER_ALIASES context block and have been passed through unchanged:

- **AlexH** — appears at 00:11:33
- **Mitch** — appears throughout (00:03:06, 00:14:47, etc.)
- **Juan** — appears at 00:59:18
- **elijahstambaugh** — appears at 01:36:06
- **Prem** — appears at 01:54:12
- **Al Anthony** — appears at 01:08:15
- **Hemal Shah** — appears at 00:32:18
- **Jake Maymar** — appears at 00:31:25
- **Morgan Cook** — appears at 01:15:41
- **Patrick Chouinard** — appears at 01:37:57