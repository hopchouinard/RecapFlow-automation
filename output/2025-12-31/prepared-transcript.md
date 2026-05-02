=== SESSION ===
date: Unknown (post-Christmas, pre-New Year 2025/2026)
duration_estimate: ~110 minutes
main_themes: AI coding tools and model selection, client project updates, ShipKit workflow automation, local models and desktop app development, AI video content monetization, freelance pricing and delivery strategy
===

<!--SEGMENT
topic: Claude Code Usage and Model Selection
speakers: Marc Juretus, scottrippey, Brandon Hancock
keywords: Claude Code, Claude Max plan, Cursor, GitHub Copilot, Claude Opus, Claude Sonnet, Anthropic, API usage, Claude Desktop, parallel tasks
summary: The group discusses their Claude Code usage patterns, subscription tiers, and model preferences. Scott describes hammering the doubled Christmas usage limits, while Marc shares his first experience with Claude Code and API credit exhaustion. Brandon advocates for Claude Opus over Sonnet for faster, higher-quality results in coding workflows.
-->

00:00:00 - Marc Juretus
Studio.

00:00:00 - Marc Juretus
So yeah, I realized that real quick.

00:00:02 - Marc Juretus
I think my max was three.

00:00:04 - Marc Juretus
I used up $3.33 and I was done.

00:00:07 - scottrippey
I'm telling you guys, if Brandon hit it on the head — like if you're trying to code a ton, like if you hit a $100 max plan and have a backup, you can use Cursor [tool:Cursor] or VS Code, whatever, as your IDE.

00:00:20 - scottrippey
But like, if you have a backup plan for 20 bucks and you hit a max plan of $100, you can just hammer the crap out of it.

00:00:30 - Marc Juretus
I have a $20 Cursor and I have the $10 GitHub one.

00:00:34 - scottrippey
Like, I would chew that up in four hours. Easily.

00:00:40 - Marc Juretus
What are you spending up, man? You cracking some algorithms or something?

00:00:43 - Marc Juretus
I mean, I'm coding all day, every day.

00:00:46 - scottrippey
So I've got a lot of apps I'm working on for customers, but the cool thing about Claude [tool:Claude] was that they gave everybody doubles.

00:00:55 - scottrippey
So I'm actually on the $200 plan, which is ridiculous. I probably could go to $100, but I use Claude Desktop [tool:Claude Desktop] all day long as well as my assistant companion for things when I'm planning stuff, and I use Claude Code [tool:Claude Code], and I use it in Cursor's IDE, but it's funny because they doubled from Christmas to New Year's.

00:01:17 - scottrippey
They gave everybody on a max plan — $100 or $200 — double the output, and I'm like, there's no way. Challenge accepted, but I can't even touch it.

00:01:25 - scottrippey
I've been coding all day every day, and it's like, I'm at like 7%.

00:01:31 - scottrippey
What's up, guys?

00:01:33 - Brandon Hancock
Hope everyone has had an awesome Christmas so far. Definitely have missed you guys.

00:01:41 - Brandon Hancock
It has been weird not grinding, because I was on like a four-month grind, just constant, and the second I wasn't, my brain was like broken. Like, what do I do? I feel like I should be on my laptop right now, so I definitely have a — I'm addicted to my laptop. It's official.

00:02:04 - Brandon Hancock
But no, good to see everyone. Hope everyone had a good break. Pumped to hear everything y'all been up to as we go around Robin.

00:02:10 - Brandon Hancock
Let me take a quick screenshot of call order and then we'll start ripping.

00:02:18 - Brandon Hancock
And also huge shout out to Patrick for holding down the fort while I was drinking way too much sake.

00:02:35 - Marc Juretus
Well, all I'm really doing right now — I was just talking to the guys — I've really never used Claude Code before, but I must know all of them. So I've been playing around with that today.

00:02:45 - Marc Juretus
And I was telling them the API usage, boy, that went real quick. And it was to the point where I couldn't even log out because when I tried to type a Claude command — like `claude logout` — so I could log in and reset it to the paid plan, I'm locked out.

00:03:06 - Marc Juretus
But yeah, it was a pretty good experience. I had to spin up a Next.js application with a FastAPI back end, and it was pretty nice. I can see why you guys use that a lot.

00:03:16 - Marc Juretus
Because what are you mostly using, just out of curiosity? Cursor, and I do a little bit with GitHub Copilot [tool:GitHub Copilot], but it's primarily Cursor. I think it's a $20 or $22 plan or something like that?

00:03:27 - Brandon Hancock
Yeah. Yeah, it's primarily what I use.

00:03:29 - Marc Juretus
But it's a little different — down there in the terminal type, it is a little different experience, though.

00:03:34 - Brandon Hancock
<Q>And which model, out of curiosity? Are you an Opus man? Are you a Sonnet man?</Q>

00:03:43 - Marc Juretus
Sonnet. Why would you recommend using Opus?

00:03:49 - Brandon Hancock
<A>I honestly just default to Opus unless I'm doing smaller work. I've really loved Opus recently. And in Claude Code you basically get — I don't think it costs that much more to use, at least if you're in Claude Code. I think it's a decent price. So I've liked it just to get to the answers faster.</A>

00:04:13 - Brandon Hancock
▶ So yeah, another reason to use Claude Code, man.

00:04:16 - Marc Juretus
Well, I use it for Anthropic [tool:Anthropic], like for my desktop, and I want to ask general questions. Like I don't really use ChatGPT [tool:ChatGPT] on my phone a lot. So I was like, let me see what it's like for that experience. So it's pretty good. I gotta admit, I like it.

00:04:28 - Marc Juretus
<Q>I understand why — why do you use it more than other ones? Or is it pretty much weighed in that direction? You kind of bounce whatever you have free credits on, or is there specific stuff you do on Claude?</Q>

00:04:40 - Brandon Hancock
<A>No, I mean, just with Claude Code — between the parallel task, the ability to parallel task, background jobs, plan mode, in combination with task templates. And just the fact that I can pay $100 a month, basically unlimited for my use case. That's the main reason why.</A>

---

<!--SEGMENT
topic: Hugging Face and Specialized Models
speakers: Marc Juretus, Brandon Hancock, Andrew Nanton
keywords: Hugging Face, custom models, OCR, PII detection, embedding models, DeepGram, medical transcription, speech-to-text, named entity recognition
summary: Marc asks whether members use Hugging Face models in development. Andrew confirms using narrow, purpose-built Hugging Face models for OCR, layout parsing, and PII detection. Brandon shares that the only custom model in his startup is DeepGram's medical speech-to-text model for accurate transcription of clinical terminology.
-->

00:04:44 - Brandon Hancock
<Q>Who else had to use a custom Hugging Face [tool:Hugging Face] model for anything?</Q>

00:05:03 - Andrew Nanton
<A>Sorry, I've grabbed a few models from Hugging Face for things like OCR or layout models or really custom embedding models. A couple of times I grabbed some for models that will find personally identifiable information. So for really narrow, case-specific stuff, that seems to be where things end up — but not for general purpose things, just for these really narrow, built-for-purpose models.</A>

00:06:35 - Brandon Hancock
<A>Real fact, Marc — the only custom model I'm actually using at all for the startup we're working on is through DeepGram [tool:DeepGram]. They have a custom medical model. So when people are talking and using all the different acronyms, it's not trying to auto-correct it to English. It was already trained on all the potential psycho-medical terminology — like IB and all these things. It's like, oh, I know what that word means when I'm transcribing speech to text. That's the only one I'm using. And it's doing really good.</A>

00:07:14 - Brandon Hancock
▶ So if you're ever doing any voice stuff, DeepGram is the way to go.

---

<!--SEGMENT
topic: Parking App and GitHub Branching
speakers: scottrippey, Brandon Hancock
keywords: parking app, Stripe, Twilio, Supabase, Netlify, GitHub branching, dev environment, production environment, SMS alerts, QR code
summary: Scott describes building a parking management app for a gym owner in Grand Rapids, Michigan, covering payment via Stripe, SMS alerts via Twilio, and a dev/production branching setup in GitHub and Netlify. Brandon reinforces the value of proper branching to protect production, and mentions another community member (Bastian) who built a similar parking app.
-->

00:08:07 - Brandon Hancock
All right, I think next up on the call order was Scott. So what's going on, Scott? Long time no see, man.

00:08:22 - scottrippey
Yeah, so things are going pretty good. I just developed a parking app for a gym owner up in Michigan, where I used to be from — I'm in North Carolina now. It's kind of this thing where he's been — like he's prime real estate downtown, and he has probably the best group fitness space on the planet. Like it's insane. He's got this crazy building with all these different rooms and two levels in downtown Grand Rapids, Michigan.

00:09:00 - scottrippey
And so he's prime parking for events. Like he bought the building with some investors just before the city was trying to squeeze them out. And so he's got this thing now where he's losing like half his money from parking for events and stuff. Because there's amphitheaters, there's all sorts of events downtown.

00:09:23 - scottrippey
So he's a good friend of mine. And I started building them something. I finally learned the branching in GitHub [tool:GitHub]. I actually have a whole dev instance, which was so much fun to learn — okay, now that I want to test things and something's live, even though it's not live yet for him, I need to learn this.

00:09:45 - scottrippey
So I have a whole thing where there's a second Supabase [tool:Supabase] instance, the variables in Netlify [tool:Netlify] have the different branching stuff. Stripe [tool:Stripe] has a whole test mode for payments, which is great. So you can test everything with fake card numbers.

00:10:03 - scottrippey
We're waiting for the Twilio [tool:Twilio] campaign to be approved for the text alerts. That's the only thing left to test. Everything else is working brilliantly. It's all ready and set.

00:10:17 - scottrippey
He can set his hourly rate, his event pricing, a calendar, and he has a panic override button where if he forgets about something, there's a hierarchy of pricing. So that's been a fun one. We're just waiting for Twilio to hook in.

00:10:35 - scottrippey
But that was a great learning experience on the branching. It's huge.

00:10:41 - Brandon Hancock
Yeah, so two things on that. There's nothing better than when you finally get it set up. It's like a relief is lifted off — the anxiety of like, I'm way less likely to break production. Way less likely. And that feels fantastic.

00:10:57 - Brandon Hancock
And then the other cool thing — so Bastian, I think he was on the call. He actually helped my friend build a parking app where I live. So he might have a few pointers of like cool services or anything that was used, if you needed anything.

00:11:23 - scottrippey
Oh, sweet. Yeah, I'll hit you up on the side for sure.

00:11:26 - scottrippey
It's cool because he's not really policing it. We're not doing an amount of spots that are filled. He's got like 70-some spots — the gym doesn't get used at night. So it's kind of like he'll check it once in a while. But all we're collecting is a phone number and a license plate. And then obviously payment through Stripe.

00:11:55 - scottrippey
Towing somebody is more problem than it's worth. So it's a pretty easy job to build this one where we don't have to track spots. We're just creating the system for people to use. And he basically makes a killing off of it, which is insane. Because the person — he's using some app now, and the guys there half the time doing VIP parking take like half the money. He's like, yeah, we need to dump this.

00:12:30 - Brandon Hancock
I'll only charge you 45%.

00:12:34 - scottrippey
Well, it was a good project for me. I'm making a lot up front, but I'm also going to get quite a bit in perpetuity, which is nice. He's a good friend. So yeah, we're doing a little profit sharing on that.

00:12:47 - Brandon Hancock
That's awesome, man. Congrats. That always feels good — when you get a project out in real life, and you instantly get to see the monetary result. He's instantly making money, and you're instantly making money. That feels good. Incentives are aligned.

---

<!--SEGMENT
topic: Baja Tourism Pass App Pitch
speakers: scottrippey, Brandon Hancock
keywords: tourism app, Baja California, QR code, bilingual app, Stripe, PostHog, analytics, MVP, $25k project, recurring revenue, restaurant deals
summary: Scott describes pitching a $25K tourism discount pass app for Baja California, Mexico — a QR-code-based platform offering tiered deals at restaurants and events for locals and tourists. Brandon suggests using PostHog for behavioral analytics and location tracking, and encourages Scott to join the next ShipKit call to plan the analytics architecture.
-->

00:13:00 - scottrippey
The two big things are that right now, and I am in talks with somebody who's in the Baja California, Mexico space, who's doing a tourism pass app. I have pitched them basically a $25K project with maintenance probably at the $750 mark per month, especially starting out with the things we need to do.

00:13:27 - Brandon Hancock
That's awesome, man.

00:13:29 - scottrippey
It's basically a deal — they've got investors. It's basically a friend of mine who's from Australia, who was there with two other people, and none of them are Mexico natives, but they've got a lot of connections. We planned it out over like three different sessions, and I pitched them. I'm just kind of waiting to hear if we're going to do it or not, because even at $25K, it's cheaper than they're going to get from a dev team.

00:14:00 - Brandon Hancock
<Q>Out of curiosity, what would you actually — in four sentences — what would you actually be building?</Q>

00:14:07 - scottrippey
<A>So this app is basically a QR code at restaurants and events. They have two different tiers where they make their money off people signing up and getting a deal at a restaurant or an event or money off stuff. Then they also have a partnership level where they'll only have maybe 10 to 12 partners — like airlines, cruise ships, things like that — where they get a kickback. And so it's basically this thing where people — not just locals, they are looking at locals, so it's going to be bilingual — but also people coming in, and they'll have day pass, week pass, year passes for people that are living down there the whole time.</A>

00:14:53 - scottrippey
And so it's just like a way to save money on events, restaurants, things like that.

00:15:00 - Brandon Hancock
And nobody has actually done that in the area, which is...

00:15:02 - scottrippey
What they're finding, which is wild to me. Yeah. So it's a huge opportunity.

00:15:06 - Brandon Hancock
I love projects like that because it's very clear what you need to do. It also would be very clear to build some query dashboards and stuff for them to easily see how much people are using it so that they can easily change up marketing or anything like that. Like your role in that will hopefully be really straightforward.

00:16:23 - Brandon Hancock
▶ Rufesca, what I would love to do — I don't know if you're free tomorrow for the 10 a.m. ShipKit call — but I would love to talk to you about some ideas around PostHog [tool:PostHog] because they do a really good job of tracking, even if you don't get the customer's ID or email exactly. You can easily track where they scanned and their whole lifecycle with the application. So whenever they do put in their email, you'll be able to tie locations to devices. You can do some really cool analytics.

00:16:57 - scottrippey
I'll make sure I'm on that one. Because this is something where I've considered — I think I'm going to actually code this thing from scratch, like even that part, because we're going to generate QR codes, we're going to track per restaurant, they're going to scan it in. I feel like I'm going to probably custom code this whole thing, but I definitely want to talk about this, because if there's something I can plug in, I don't want to reinvent the wheel.

00:17:25 - Brandon Hancock
Yeah, we'll go deeper tomorrow. Very awesome opportunity. I always love to hear when you guys are about to get a nice payday.

00:17:41 - scottrippey
2026, man — I shifted into this from the IT world to video to this. It's paying off because I've got some connections. It's happening. It's like, alright, this next year is just all development, man. I'm geeked.

---

<!--SEGMENT
topic: Billion-Dollar One-Person Business and AI Automation
speakers: Ty Wells, Brandon Hancock
keywords: Claude Max plan, sub-agents, parallel sessions, fire photo app, Calendly clone, autonomous OS, customer acquisition, milestone planning, billion-dollar company, AI agents
summary: Ty shares his progress toward a "billion-dollar one-person business" concept, using Claude Max plan credits to clone tools like Calendly and build an autonomous operating system that finds customers, drafts emails, and follows up until conversion. Brandon discusses the principle of building software tied directly to monetary outcomes as the clearest path to high-value SaaS.
-->

00:18:07 - Brandon Hancock
All right. It looks like Ty, you're up, man. Dude, I have been out of the loop for two weeks, so I feel like you might have recreated Google. You might have made your own AI model. What did I miss?

00:18:20 - Ty Wells
Actually, you know, okay, not this week. No, I was really just challenged to use all of my 2X plot codes. I'm at 78%, so I've got a couple.

00:18:37 - Ty Wells
No, I think Patrick said he blew his.

00:18:40 - Brandon Hancock
Seriously? That's awesome, guys. It's going to hurt because they're getting us addicted to these higher usages. And then on Thursday, when it goes back to regular, we're like, oh God, my wallet.

00:18:55 - Ty Wells
I've had it multiple times. But what I did is I got actually two Max plans. So when I hit that, I just run to the next one and I sort of switch different projects on different ones.

00:19:09 - Brandon Hancock
Are they both $200?

00:19:10 - Ty Wells
Yeah. I've got nine sessions running right now. So I mean, if that tells you anything.

00:19:18 - Brandon Hancock
Quick thing, real fast. I think they've — I love what they've done — because I don't know if you guys have noticed this, but with Opus specifically, I'm having tasks run for like 10, 15, 20 minutes, sometimes churning through tokens, and it crushes it every time. But it's like, dang, that was just 20–25,000 tokens in a few minutes. So because they've made it so much better, it can run for so much longer, which means we're hitting limits faster. So I don't know how I feel about it, but I'm noticing that happen.

00:19:53 - Ty Wells
Yeah, I am for sure. Especially with sub-agents [tool:Claude sub-agents].

00:19:58 - Ty Wells
Last week I talked about my billion-dollar single-person business, and I sort of worked my way back on that one if you guys were on the call last week. Still working on that project.

00:20:26 - Ty Wells
But no, it's that fire photo project. I think I dropped the link in last week. Just dropped it in the chat.

00:20:45 - Ty Wells
But since I was burning through some projects, I decided I'm going to clone a few projects. Like Calendly [tool:Calendly] — I rebuilt that for the operational side. But I used it now to integrate into my own thing. I don't need Calendly anymore.

00:21:09 - Ty Wells
Yeah. So basically what I worked on was I used those credits to build a serious cloning tool.

00:21:17 - Brandon Hancock
Cloning of software?

00:21:23 - Ty Wells
Yeah. So that's basically what I've got. So I can't show it just yet because it's still — I'm putting a UI on it — but hopefully maybe next week or the week after. But if you're using a piece of software and you want — because I'm testing it really — so I was testing, building other things for other people. So if you want something that you like, I can build you a repo and you can take it from there. And I mean, it sounds good, but it seems — for what I'm doing, I'm talking production ready. It builds up everything, builds all the connections, runs all the tests, does everything and just produces the repo for you.

00:22:09 - Brandon Hancock
That's awesome. Spin it up.

00:22:09 - Ty Wells
Of course, my Supabase bills go up because every time I spin one up, there's a database — it automatically spins up a Supabase.

00:22:22 - Brandon Hancock
Dude, Supabase is going to start sending you a shirt soon.

00:22:45 - Brandon Hancock
I do want to add — just on the topic of billion-dollar software companies, because I've been thinking about this. I just love that concept. Like, it's a cool thought experiment. What would I actually have to do to do that?

00:23:08 - Brandon Hancock
So here's kind of what we're focusing on for our stuff and what I'm noticing. ▶ I think the closer you are to the money for any industry, the more likely you are to just get paid an absurd amount of money. So for example, if there's any task or process in a business that is standardized and repeatable and delivers a monetary outcome, that's gold, absolutely gold.

00:23:28 - Brandon Hancock
So like in our case, what we're focusing on is SOAP reports. SOAP reports basically are the way that fire departments and ambulances can get paid — and not just get paid a couple of dollars. It's the difference between them getting reimbursed for many thousands of dollars or losing thousands of dollars. So it's like a very clear — if it works well, they make money, or they lose money. So it's right on the money.

00:24:00 - Brandon Hancock
▶ So if there's any, in any industry, if you guys ever see that type of workflow where there's money at the end of an actual tangible outcome, that's gold. And I cannot stress enough — please tackle those opportunities as much as you can.

00:24:17 - Brandon Hancock
Because I don't know if you guys watch Alex Becker — love his recent software talks. And he talks about it like, if you turn off your service and people aren't screaming, it might not be the right software project. Because if you turn your service off and they start losing money, they're gonna knock on your door like, dear God, please turn this back on.

00:24:50 - Brandon Hancock
▶ So I think that's a really cool rule of thumb to make sure you're hitting the right type of projects — automating tangible outcomes, products and deliverables that are tied to money.

00:25:11 - Ty Wells
Yeah, one thing I'll add to that — so I built an OS for this Firephoto project that does — let's say, okay, I need to have X amount of customers by the end of January. So instead of me going and finding the customers, I'm just having it build, go find the customers, draft the email, customize it to them, send it to them, follow up with them, do whatever you need to do until they convert.

00:25:47 - Ty Wells
So I've got one guiding document to this billion dollars. And I'm working through that document, trying to hit those milestones. So if I'm short on a milestone, it's — okay, this is what needs to be done. Do I need to do it? No, you go do it.

00:26:19 - Brandon Hancock
I love that. Ty, that's sick. Instead of a plan to solve one individual feature, it's the plan solving a billion-dollar problem versus like, hey, implement this small bug. That's a sick idea.

00:26:43 - Brandon Hancock
Please keep us posted, dude. I would love — I don't know if you've seen on X, people do like the status bar of where they're at. I would love for yours to be like $1 billion in monthly little updates as it's incrementing. I think that would be sick.

---

<!--SEGMENT
topic: Prompt Weaver Tool and ShipKit Workflow Skills
speakers: Patrick Chouinard, Brandon Hancock
keywords: Prompt Weaver, prompt library, ShipKit, Claude Code, Gemini Flash, GPT-4.1, UltraThink, task templates, roadmap, confidence check, AI-assisted development, model selection
summary: Patrick demos "Prompt Weaver," a custom prompt library tool with AI-assisted prompt creation, structured editing, documentation generation, and a GitHub-like forking system for certified prompts. He also shares new ShipKit workflow skills covering dependency analysis, implementation loops with confidence checks, and automated roadmap updates. Brandon shares his current model preference shift from GPT-4.1 to Gemini 2.0 Flash for production AI applications.
-->

00:27:31 - Brandon Hancock
All right. Patrick, you're up next, buddy. Thank you once again for holding down the fort. We'd love to hear what you've been up to.

00:27:45 - Patrick Chouinard
Yep. Actually, I've been ShipKitting the whole way through.

00:27:55 - Patrick Chouinard
And the one I worked on this week — basically I worked on something I called Prompt Weaver [tool:Prompt Weaver]. Basically, it's an enhanced prompt library. It's something that I've seen the need for in my daily work every day and I have never seen one implemented the way I wanted. So I basically said, screw it, I'm going to do it myself.

00:28:37 - Patrick Chouinard
So it's far from finished. I'm still in the implementation phase, but basically what it does is it starts from a simple chat. But the big functionality is the fact that you can create your prompts in an assisted fashion. So we named them as "spiked" prompts.

00:29:00 - Patrick Chouinard
Then here you can either do an intention-based approach — so you just drop the intention, and you have ghost text to show the user what they could create — and Extract Structure will basically call a prompt in the backend that will transform your intention into a structured prompt. Or you can go in Structure Mode and do every section yourself and have the ability to improve them using AI in the backend.

00:29:32 - Patrick Chouinard
Basically what that does is it sends everything you have, but it's specified to improve the section you're working on at the moment.

00:29:42 - Brandon Hancock
That's awesome.

00:29:43 - Patrick Chouinard
And when you're in Structure Mode, you also have the AI Assist, which allows you to generate documentation. So once your prompt is completely done, you can have full documentation that goes with it. You can check for guardrails or improve the prompt you've created.

00:30:06 - Patrick Chouinard
That's awesome.

00:30:10 - Brandon Hancock
<Q>So behind the scenes, just out of curiosity, on the AI assistant side, what are we using in the background? Are you a Gemini guy? Are you a GPT guy?</Q>

00:30:25 - Patrick Chouinard
<A>Oh, all of them. Basically, you can set the execution model for each and every prompt. So every step — if it's just improving a little bit of text, I'm going to choose a specific model. If I'm modifying an entire prompt, I'm going to use another one. But basically I can use an execution model for each and every prompt.</A>

00:31:39 - Patrick Chouinard
And those are all shareable. So people are going to be able to see those prompts through the certified prompt section. They can star them. They can fork them and bring them into their own library. And start improving them and working on them. So it's basically a kind of GitHub repo of prompts that have all the tools to enhance them, document them, and improve their lifecycle.

00:32:13 - Brandon Hancock
That's awesome. Quick, just for the group — cool lessons or things I've been learning over the past couple of days.

00:32:21 - Brandon Hancock
Context: I love when building AI applications — my favorite model for instruction following was GPT-4.1 [tool:GPT-4.1]. That's been my go-to model for close to a year now, basically since it came out. It's a non-thinking model, phenomenal cost, speed, and intelligence all around. And a 1 million token context window — my favorite.

00:32:46 - Brandon Hancock
I have not swapped any of our projects or startup projects off that model until Gemini 2.0 Flash [tool:Gemini 2.0 Flash]. This is the time that I'm actually swapping — I haven't fully pulled the trigger, I'm still running some tests — but Gemini 2.0 Flash on low thinking produces the same quality results, it's cheaper, and with only a hair slower, just because there's a thinking model, so it does have one extra step before it starts to stream the results.

00:33:00 - Brandon Hancock
▶ So if you're doing any type of application where you're continually delivering results and you don't want to blow through the budget, you're roughly looking at like one to two pennies per answer for your users, and it's really high quality results. So just wanted to share that lesson — picking the right models for development versus for your actual applications, two different worlds.

00:33:57 - Patrick Chouinard
Fully agree. I code with Claude, but I implement things that use Gemini [tool:Gemini].

00:34:07 - Brandon Hancock
Yeah. They've — yeah.

00:34:21 - Patrick Chouinard
And basically while doing this, I realized that I was copy and pasting the same instruction over and over and over again in the implementation phase. So I decided to create a set of skills to add on top of my ShipKit [tool:ShipKit]. And I've put it in the community repo, if you want to take a look at it.

00:34:56 - Patrick Chouinard
Basically you have a pre-section skills — analyze the phase for dependency and implementation order. So it goes into the roadmap and reorders the roadmap to make sure it can be done as parallel as possible and all in the right order.

00:35:09 - Patrick Chouinard
Subsection task — it starts the implementation loop with a bunch of impact analysis. So basically, you know, when you start, it starts by asking questions. You say, ask me any question you need. Well, I build that into a skill instead.

00:35:28 - Patrick Chouinard
It asks the question. It proposes a choice answer. It recommends one. You do your selection. It goes on. You do your code preview. And after that, you go to a confidence check. So it checks everything. And if it's not 95% plus confident in the implementation, it will ask additional questions. Then it does the code review, status update, updates the task and updates the roadmap. And finally, it pushes everything.

00:36:01 - Brandon Hancock
This, Patrick, per usual, absolutely beautiful. Love it. You are taking ShipKit to its ultimate extreme and every time it just blows my mind.

00:36:16 - Brandon Hancock
Quick thing I've really been experimenting with recently that I think you might like to try. In that confidence section, I've been doing it manually right now, but I love using UltraThink [tool:UltraThink] for that final check. I basically — if you type UltraThink into Claude Code, it just thinks more than normal. And I've been loving that as my final check before saying, go forth and implement, just to make sure — like you said — I want you to be confident and think about this before you implement it.

00:37:00 - Patrick Chouinard
Yeah, and I would probably think about that. The only thing is since I implement one subsection at a time, the context is not large enough to require that, and I do multiple checks. So basically when I start implementing, the first thing it does is ask questions, and it asks to be more precise and to add some more context. Then it adds the high-level code example. Then I do the validation.

00:37:22 - Patrick Chouinard
But every time, I also backfill the roadmap and the task document and update it to become my working memory. So I could crash my computer and restart at any point, and anyone knows exactly where I am because I'm saving everything that's necessary for the context into the task and the roadmap.

00:37:43 - Patrick Chouinard
So doing it like that — and also there's guardrails in my prompts that specify to make sure that it does not change settled work unless it asks me for a change request. So that has saved me from destroying my database in the middle of a run or something like that.

00:38:03 - Brandon Hancock
Yeah, no, I love that. No, that totally makes sense. I mean, you basically are doing UltraThink, it sounds like, with the amount of validation you're doing multiple times.

00:38:14 - Brandon Hancock
Real quick — I think Patrick said something that's super, super important to mention. ▶ The reason I love creating tasks is because there's an actual artifact in case something goes wrong at any time. There's something tangible to come back to. Having the normal Claude Code plans or the Cursor plans, they're so hard to find. The names don't match the actual feature that was implemented. So it's very hard to come back to say, please pick up where you left off, because it doesn't know exactly where it left off. But the second you have a task template with action items and checkboxes, it's so easy to resume work.

00:38:58 - Brandon Hancock
Final thing, Patrick. One other quick thing I've been experimenting with — after it does the test and the final implement, one thing I always do afterwards is say, please go back and update the initial task document, just so everything is always captured. Like you could basically follow the task to figure out how I built the app.

00:39:37 - Patrick Chouinard
This is the status update skill that does that. Because every time I finish, I go update — but not just do the check mark. I include all of the decisions that have been taken, all of the reason behind every decision. It's really the project memory. So everything is backfilled.

00:39:53 - Patrick Chouinard
Now, my next step is I want to create an agent that's going to wrap all of those skills. So I can just start the agent. It's going to ask me a question when it has to ask me a question. Otherwise, it will be implementing independently.

00:40:10 - Brandon Hancock
Patrick, I absolutely love it. It's so funny — I've been experimenting manually, but you already have it in a beautiful prompt. Absolutely crushing it.

00:40:20 - Patrick Chouinard
Basically, I just listened to your video and implemented it into a skill.

---

<!--SEGMENT
topic: Codex CLI, Go Desktop Apps with Wails, and Local Development
speakers: Andrew Nanton, Brandon Hancock
keywords: Codex CLI, OpenAI Codex, Claude Code, Go language, Wails framework, Electron, Python packaging, PySide6, local file system, cross-platform, desktop apps, Playwright
summary: Andrew shares his preference for the Codex CLI agent over Claude Code for certain tasks, noting it handles environment context (like mise-en-place) without extra nudging. He then introduces the Wails framework for building cross-platform desktop apps in Go, explaining why Go's explicitness and backward compatibility make it easier for LLMs to reason about compared to Python or TypeScript.
-->

00:41:11 - Brandon Hancock
All right. A call order — it goes Andrew, Tom, Morgan, then Mitch, then Ryan. So floor is yours, Andrew. What's going on, man?

00:41:16 - Andrew Nanton
Well, yeah, it's been a while. Been real busy with other more boring stuff, but a quick update about what I've been playing with here recently.

00:41:25 - Andrew Nanton
So I'm still feeling like I'm getting better results out of the Codex CLI [tool:Codex CLI] agent than Claude.

00:41:32 - Brandon Hancock
Okay.

00:41:33 - Andrew Nanton
So I'm playing with both of them. And I mean, you know, I switch back and forth and sometimes one gets stuck, but it seems like a lot of times Claude will — for example, I was doing something recently and it gave me some suggestions of things I could do. But it missed that I was using mise-en-place [tool:mise-en-place] to manage the environment and stuff. Stuff that Codex just doesn't seem to slip on. It just seems to catch stuff without the extra nudge that Claude sometimes needs.

00:42:09 - Andrew Nanton
So I've been pretty impressed with that.

00:42:14 - Brandon Hancock
<Q>Andrew, quick question. Just because I've kind of picked Claude Code as my go-to — and the reason why was when I was using the GPT models, it felt slow. Has it gotten faster in your opinion?</Q>

00:42:30 - Andrew Nanton
<A>It's been pretty fast for me, but like you were saying, the other thing that has happened is that because it tends to run a few steps at a time, it's just like if it's running for 10 minutes, if it's an extra 10 seconds, maybe I'm just not noticing it. But that has also always been my workflow — I'm usually splitting my attention between a few different things. And so it's cranking away in the background and I check in on it from time to time. So I think I've been less sensitive to the latency.</A>

00:43:00 - Andrew Nanton
But I mean, I'm just using it on the $20 a month plan because I switched back over to that and I've been poking at it and I've been liking it.

00:43:10 - Andrew Nanton
I'm still kicking around some of the ideas that I've had about a local application. Before I was trying to do PySide6 [tool:PySide6] and it's like a QT framework — it is fine, I mean, I don't understand any of it, so there's that. But also trying to package up and distribute anything Python is just a hot mess. Yeah, wheels, eggs — it's all ridiculous. It's bad, it's real bad.

00:43:41 - Andrew Nanton
So when I was giving this another run and trying out some of these new tools, I thought, well, I'm not really writing much of it anyway. So why don't I see how far I can get with Go [tool:Go], which will package it all up into a single executable for every platform. And I found a framework called Wails [tool:Wails], W-A-I-L-S, and version three is in alpha.

00:44:13 - Brandon Hancock
I'll put a link if you could — I'd like to see it.

00:44:17 - Andrew Nanton
Yeah. So I mean, it basically just brings up a WebKit view or a WebView, whatever web renderer is native to that platform. So it's pretty lightweight. It compiles down to just about nothing. You can — it has a few different templates where you can start it up as a React front-end or a Vanilla front-end or Svelte or whatever you feel like you might want.

00:44:47 - Andrew Nanton
And I think maybe because Go is so explicit and kind of clunky in some ways — for me to read it, coming from someone who mostly knows Python — it seems really easy for the models to reason about. And so I've had actually pretty great luck with it.

00:45:11 - Andrew Nanton
▶ And it's explicitly very tied to backward compatibility. So even outdated documentation — which tends to make Python and TypeScript and everything else just explode immediately if your documentation is a month out of date — so anyway, throwing it out there as something to take a poke at, if anyone else has had an urge to do something locally, because the libraries are good. It's a big standard library and LLMs seem to write it just fine.

00:45:44 - Andrew Nanton
You can do the whole front end in Lovable [tool:Lovable] or whatever, if you feel like, and just bring it in.

00:45:53 - Brandon Hancock
<Q>So quick question, just to make sure I understand. So Go is basically just an actual executable, but then what you called out with Wails is basically just running a website or that's kind of getting wrapped, or is it actually like a full-blown desktop — what's actually happening? I guess I'm not sure how the UI is actually getting presented.</Q>

00:46:24 - Andrew Nanton
<A>Sure. So I mean, as far as I understand it, it's very similar to Electron [tool:Electron], in that in a dev environment, you can connect to a URL and a web host and look at it, and then it just packages all that up, and it has some kind of internal web server inside there — like an Electron app does — that isn't exposed to anything else in the system. But then you can use stuff like Playwright [tool:Playwright] or whatever you want to do to look at your UI or help you do other stuff, because when you're running in dev, it's all just a web server.</A>

00:47:00 - Brandon Hancock
Hey, that's awesome.

00:47:24 - Brandon Hancock
<Q>So my question is, why not use Electron? I haven't touched Electron since 2018. What was your thoughts? Was it just the model struggled with it? This one just is doing better and faster?</Q>

00:47:42 - Andrew Nanton
<A>Sure. Well, the main reason is I need clean, rapid access to the local file system. And you can make that happen by jumping through some hoops in Electron, but it seems like there's always — with JavaScript and trying to access the native file system, at least through that intermediary — unless you're just running Node directly, it's always like, well, we'll try. And so I needed something a little more straightforward, and this has been good for that.</A>

00:48:15 - Brandon Hancock
That's awesome. Okay, I have to keep that in mind. I remember back in the day when I had it all manually — God, it was breaking my brain. I haven't done Electron plus AI yet, so I'm curious to try it out.

00:48:49 - Andrew Nanton
And I mean, I think really just the Python back-end — trying to get Python distributed cross-platform was really the killer, especially through a web-based platform where I wanted local file system access. It was just too much. But one of the nice things about Wails is, if there isn't a Go library, there's probably a TypeScript library. And you can have both. So it's pretty slick.

00:49:02 - Brandon Hancock
▶ No, I am 100% — the second you said distributing local Python packages to other people, dude, it's possible, I've done it before, but I just literally couldn't even tell you how I did it. I just tried a thousand things until it worked. It's a nightmare. So I feel your pain on that. But dude, absolutely crushing it and great find on the local development. I have not used Go that way. I've only used Go for backend servers, but that's a really cool use case.

---

<!--SEGMENT
topic: Freelance Delivery, ShipKit Licensing, and Trigger.dev Use Cases
speakers: Elijah, Brandon Hancock
keywords: ShipKit, Trigger.dev, freelance pricing, client delivery, vibe coding, AI-assisted developer, equity vs payment, background jobs, retry logic, sequential workflows, SaaS delivery
summary: Elijah asks two questions: how to deliver client software built with ShipKit, and how ShipKit licensing works for selling projects. Brandon clarifies that the only rule is keeping AI docs out of the GitHub repo. He also advises against working for equity promises, recommends getting paid upfront, and gives a concise explanation of when to use Trigger.dev for long-running background jobs versus simpler in-line AI pipelines.
-->

00:49:41 - Brandon Hancock
Elijah, if you want to, I know you said you have a few minutes — if you want to hop in, buddy.

00:49:42 - Elijah
I appreciate that. Happy New Year, everybody. Good to see you.

00:49:46 - Elijah
So I have been building like crazy, got Trigger [tool:Trigger.dev] running, and feel like the world is going to be revolutionized one way or the other.

00:50:04 - Elijah
My question is, I have a prospective client and I will be very transparent with them that I'm not a developer — that this is going to be a vibe-coded project. They want to build an application and they want to maybe turn it into a SaaS. I know I could build it with ShipKit, right? They were looking more at the automation side with n8n [tool:n8n] in that.

00:50:34 - Elijah
But my question is two things. One is, if I do it for them — whether or not I want to participate in the company, or I just want to have them pay me for the software — what do I do to deliver it to them? And then the second part of that is, I am building some stuff that I will plan to sell as a company. How do I do that between me and you with ShipKit, because I know you're allowing us to build and sell these things, but I'm just trying to understand how that actually works in the code base.

00:51:16 - Brandon Hancock
<A>So let me answer the second question first. So yeah, if you're wanting to build something — pretty much the only rule was just the AI documents. If you could just add those to the `.gitignore`, that's the simplest rule of thumb. Feel free, whatever you build — the source code's theirs. Just if you could keep the AI docs out of the GitHub repo, that would be the main thing.</A>

00:51:47 - Brandon Hancock
And then can you repeat the first question, please?

00:51:55 - Elijah
Yeah, so similarly, if somebody says, hey, I want you to build this software for me. They may need support, right — which I'm going to have capacity constraints at some point — and I'm going to be transparent with them, it's not like I'm saying I'm a full-stack developer. I can vibe-code, I can get this thing running for you. And they would pay me, I would deliver the software to them. Is it the same thing — just take out the AI docs?

00:52:22 - Brandon Hancock
<A>Yeah. Because other people have been selling this in this community, right? Yeah, yeah, exact same thing. The only thing I would do if I was you — I don't know how much I would just say, like, I'm a vibe-coder. I would maybe look at it from a different lens — like, I don't know, you're going to deliver the result, or you're not going to charge them. Like, that's the answer. So I would — you know — it's like, I will get you this result, and if I do it, I expect this pay.</A>

00:53:05 - Brandon Hancock
If I have someone doing gardening and the guy goes, I'm not a gardener, but I can make the garden look nice for you — I don't care. Did you deliver the outcome or not? How you did it?

00:53:12 - Brandon Hancock
▶ I wouldn't sell yourself short. That's what I'm trying to say. But then also at the same time, I would make sure you do deliver high quality results and make it easy to maintain, which ShipKit is set up in a really maintainable way, especially when you set up the production and development environment. So I think you're going to deliver way over what a typical just-pull-a-guy-out-of-high-school vibe-coder would. I feel like you're going to deliver something way better because you know how to do a production environment, a development environment, and you have the proper project structure.

00:54:00 - Brandon Hancock
Yeah, and then final thing — going back to what Elijah was saying — I know you said you might want to build something for them and then become part of the team.

00:54:11 - Brandon Hancock
▶ I would — I'm a huge proponent of do work and get paid to do work. And if they like it and want more, then get hired. I would not do work with a promise of future equity. Because not — 99% of the time when I've seen it happen, you just don't get paid. And that's the worst feeling because you did all this work and then your ability to get paid is out of your control. It's in the company's hands. And that's just the worst feeling. It kind of sets both of you up for failure. So if they value your work, make sure they pay up front, then talk about joining the company afterwards.

00:55:22 - Brandon Hancock
Yeah, just crash course real fast for everyone on Trigger — super fast. ▶ It is a phenomenal tool to use for long-running background jobs or sequential workflows where you don't want to worry about retry logic, queues, anything like that. Trigger absolutely crushes it. So my rule of thumb is like, if I'm doing anything that takes over a minute, instantly I'm like, by default, I have to use Trigger. Or if I'm doing something that has very clear step A, B, C, D, E, and there's potential for things to fail, I like to use Trigger.

00:55:56 - Brandon Hancock
Now, when I don't use Trigger — like I'll give you a real world example. Right now, for the startup, whenever we're trying to answer questions for our customers — like to create those reports — right now we have multiple steps of AI: we have a categorizer, we have a generator, we have a reviewer, we have something else. All of that is getting done in under a minute, and it's taking max 30 seconds. So there's no reason for us to put that over inside of Trigger, because it's just four steps A, B, C, D, and they all flow together. And if it fails, we actually just say, hey, something went wrong, please try again. We don't want any retries. If we did, then I might think about using Trigger. But yeah, I mostly use it just for long-running background jobs. Anything else can potentially be overkill.

---

<!--SEGMENT
topic: Local Models, Phi-4 Benchmarking, and Privacy-First AI Architecture
speakers: Tom Welsh, Brandon Hancock, Bastian Venegas Arevalo, Patrick Chouinard, Andrew Nanton
keywords: Phi-4, local models, Ollama, LLM benchmarking, Dung Beetle, Playwright, web scraping, bot detection, Nike site, Mac Mini, MCP, PII redaction, LLM Guard, Hugging Face, privacy, on-device AI
summary: Tom shares experiments with local models including Phi-4, using it as an AI judge to evaluate real-world comprehension, coding, and logic questions — finding nano models optimized for benchmarks underperform on real tasks. He also solves a long-standing web scraping challenge for his Dung Beetle project using Claude web chat. Patrick describes a privacy-first architecture using a local small model that calls large cloud models as tool functions via MCP, designed for an Alzheimer's patient assistant. Andrew mentions LLM Guard as a locally-runnable PII detection library.
-->

00:58:01 - Tom Welsh
Hey, Brandon, welcome back. Dude, I like your millionaire quote, man.

00:58:30 - Tom Welsh
So I've been playing about really with local models quite a lot recently. Did a Medium post a little while back about using Phi-4 [tool:Phi-4] as an AI judge of a bunch of real-world questions. So it was a comprehension question, a coding question, and a logic question.

00:58:51 - Brandon Hancock
<Q>Wait, which model?</Q>

00:58:56 - Tom Welsh
<A>Phi-4, P-H-I-4. It's a local model, I think it's Microsoft.</A>

00:59:00 - Brandon Hancock
Do you have a link to it? I would like to look at it.

00:59:09 - Tom Welsh
Yeah, so basically I just tested a bunch of local models using that as the judge and took myself completely out of the loop. And it was quite interesting to see from what the specs say on how the benchmark LLMs start to put it against real-world type questions. Like, I've got 20 sheep and nine are left behind. How many sheep have I got? And it's really stupid how some of the models can't even work out the answer with the answers on their face. And the same with some of the logic.

00:59:54 - Tom Welsh
And then some of these nano models came out recently and they had ridiculous throughputs. Again, it looks like they're built to hit benchmarks — they're not necessarily built to do the real work. Since you put them under real-world testing scenarios, they don't perform as well. They're like, oh, we're going to get 200 plus tokens a second, and I'm going, well, I'm getting 48 on a real-world question.

01:00:21 - Tom Welsh
So yeah — optimize for benchmarking versus optimize for work.

01:00:26 - Brandon Hancock
<Q>How big is this model, out of curiosity? I'm trying to see the size.</Q>

01:00:32 - Brandon Hancock
I think the one I have is 3 billion.

01:00:37 - Tom Welsh
I think it's a mixture of experts. No, it's not a mixture of experts.

01:00:43 - Bastian Venegas Arevalo
The guy started Microsoft originally, and the dataset was supposedly really well distilled. And so they had the training data to make it reason, potentially, before the thinking models.

01:01:00 - Tom Welsh
So yeah, we've been playing with that, and then client work got in the way — picked up a stupid WordPress thing, which is doom and gloom. Why do people use WordPress in this day and age?

01:01:12 - Tom Welsh
Well, currently it's mine.

01:01:18 - Brandon Hancock
One thing that I'm really, really looking forward to is whenever websites — like whenever it becomes a thing where all devices, Macs, iPhones, Androids — when everyone's running their own local models, and through your website, you can use the local model on the client. I'm so pumped for that, just to do small tasks. Like, for example, we have a PII/PHI blocker, and we're having to do all sorts of regex and other things — it's very gross, what has to be done. And we want to keep everything on the client, on the person's device. But the second it becomes common for all modern devices to have a local model that you can access, that's going to be a game changer. I definitely think that's going to happen in like 2028, but until then, as these models get smaller and devices get stronger, I think that's going to end up happening.

01:02:19 - Tom Welsh
The other thing I found quite interesting — so I'm still working on Dung Beetle [tool:Dung Beetle]. I was having a problem pulling the Nike site. So the Nike site's my North Star to get things working, because it's got infinite scroll and you can't pick stuff up, and it's got mad bot detection. And I was using Claude Opus in Cursor to try and get past it, and I could not get around it. And I literally threw the same question into Claude — just like web-based — and it threw together a Playwright [tool:Playwright] script and bish-bash-bosh. I can now scrape 685 traders off the non-stop scrolling page.

01:03:08 - Tom Welsh
So I'm now going to take this code and put it into the AI Docs reference code, and then try to plug that back into Claude Code again. And it started into the Cursor. So yeah, it was quite interesting how the same model couldn't get the same answer. One was — yeah, it was mad. I was like, what happens if I do it this way? And like, bish — like, first time, straight through script and all set. And I was like, two weeks I've been trying to get this working. And you've done it in five minutes. But thank you very much.

01:03:44 - Brandon Hancock
Yes, I won't complain, I'll just be amazed and frustrated.

01:04:01 - Patrick Chouinard
So basically, just a little comment on what you were talking about — having local smaller models running a bunch of things. Something I've been trying or fiddling with — nothing in production level yet at all — but I'm trying to have a small model that is using a larger model online as a tool, basically as a function call.

01:04:30 - Patrick Chouinard
So, interacting with the local small model for day-to-day chat, but whenever something is beyond its capability, it would call a GPT, Gemini, or Claude, as if it was a tool, and just wrap the answer.

01:04:47 - Brandon Hancock
Oh, that's cool.

01:04:52 - Patrick Chouinard
I'm working on something for my mom — she has Alzheimer's — and I wanted to build something for her. As a chatbot that's highly secured and has a ton of privacy, but with the ability to go get more important or outside information outside of the local model, if need be. And I find that it hasn't maybe worked yet, but I'm dabbling in using a model as a tool for another model, basically.

01:05:24 - Brandon Hancock
That's cool. Patrick, just going on that — awesome use case. Sorry to hear that. I think one cool thing you could do is just always use that local model to redact any PII — like if Patrick's social security number is blank, you know, like that doesn't actually need to go out to the internet. So I do think that could be just like — it always defaults to calling the big models, but they're just a redaction step.

01:06:00 - Patrick Chouinard
Yeah, and to answer Scott's question — yeah, the idea is to do it through an MCP [tool:MCP]. And as part of the MCP workflow, yeah, there would be a PII redaction step in there, specifically not to share any information outside. But yeah, just basically use the large model as a function call, that's it.

01:07:12 - Brandon Hancock
Real fast, I want to follow up what Andrew was asking. So when it comes to LLM Guard [tool:LLM Guard], the main thing that I was trying to do is basically prevent any information ever leaving the client. So that was the reason why we did not look at any external services, because it defeated the purpose — we then had to leave our machine, go to a different server, then come back to say what was good or bad. So the current solution was just to use basically some very complex regex stuff.

01:08:04 - Andrew Nanton
Sure, but so I — in an earlier iteration of this project, I put LLM Guard in there and it actually does run locally. There's a lot — you can — yeah, I'll send you a link to a repo where I set that up.

01:08:19 - Brandon Hancock
<Q>So it is local?</Q>

01:08:22 - Andrew Nanton
<A>Yeah, because you can grab — it's hard to figure out, because the documentation's not great, what the most recent tiny little Hugging Face model is the best choice for figuring out — for named entity recognition, basically. But anyway, I'll send it over.</A>

01:08:42 - Brandon Hancock
That's awesome. Yeah, if you could, because that was such a headache, trying to get it to work, and it's still at like 90% — it's still not perfect. But no, that would be huge. Yeah, seriously, thank you. That's awesome.

---

<!--SEGMENT
topic: API Key Management with Doppler and WindSurf IDE Updates
speakers: Morgan Cook, Brandon Hancock
keywords: Doppler, API key management, environment variables, WindSurf, GPT-4.1, Gemini Flash, Warp, task-driven development, context window, large codebase, branching
summary: Morgan introduces Doppler as a solution for securely managing API keys across multiple projects and team members, solving the problem of losing access to keys when switching machines. He also shares updates on WindSurf IDE's improved token usage display and notes that GPT-4.1 is currently free in WindSurf. Brandon reinforces task-driven development as the key strategy for managing large codebases without losing context.
-->

01:09:00 - Brandon Hancock
I think next up was Morgan. What's going on, man?

01:09:07 - Morgan Cook
How's everybody doing?

01:09:09 - Brandon Hancock
Hey, doing good, man. How about you?

01:09:11 - Morgan Cook
Feels good.

01:09:14 - Morgan Cook
I was going to mention something for Scott, if he's still on. So one of the things that I've been looking at is Doppler [tool:Doppler] — and Doppler is an API keys manager for all your projects.

01:09:38 - Morgan Cook
My fear that sent me down this path was if I lose my development machine or something, I don't have my local environments backed up somewhere, then I need to figure out how to find my keys again and it's a pain in the butt. So I started looking around to see if there was some way to store this. And Doppler actually is a really good solution for multiple things.

01:10:01 - Morgan Cook
One, it's a vault. And two, it's a way to easily access the key without having it stored anywhere except for in the same vault where it belongs. So it's not checked into GitHub or anything like that. And you can share it amongst all of your other developers if you want to have somebody look at a project and start using it. You don't have to copy your local environment variables and send them off to them so that they can install and test it locally.

01:10:29 - Morgan Cook
It's a really convenient way to store the API keys. I have like five projects going and it's just like, which key do I need to use where?

01:10:51 - Morgan Cook
▶ And the developer license for like a single developer is free. And I think you can share it with up to like five different people to access the same project. And then also for your deployment — like Scott, who got branching figured out — well, sometimes you've got to have different keys for your branch versus your live site. So lots of scenarios where it actually is a benefit.

01:11:53 - Morgan Cook
So just something I found over the past couple of weeks and thought I might share it with everybody.

01:12:03 - Morgan Cook
I use WindSurf [tool:WindSurf] for my main IDE and they've been going through lots of little changes. They finally have a nice display for their tokens used and when I run out of tokens for a specific model or something. So that's been kind of nice.

01:12:24 - Brandon Hancock
<Q>What's the current plan rate out of curiosity? I haven't checked in on WindSurf in a minute.</Q>

01:12:29 - Morgan Cook
<A>You know, I'm not sure. My last bill was $15 a month, but it might be more than that if you're signing up. I don't know if that was something that I had locked in because of my subscription, but I think it's around $15 to $20 per month for the fee. But they have a lot of the models that are listed as free. Yeah, so all like — GPT-4.1 [tool:GPT-4.1] is all free right now.</A>

01:13:08 - Brandon Hancock
Oh, really? Oh, dang, that's a steal.

01:13:12 - Morgan Cook
And Gemini Flash is like half a cost, whatever that is — 0.5. So I mean, they're introducing the models, and then you've got to use them for a little bit till they get you hooked, and then the price goes up.

01:13:33 - Brandon Hancock
Yeah, that's how they get you, man. They're AI drug dealers.

01:13:41 - Morgan Cook
Anyway, so it's been going pretty good.

01:13:42 - Brandon Hancock
Any cool projects in Morgan Land?

01:13:45 - Morgan Cook
Well, one of the things — I have a pretty good-sized project, and one of the things that has been killing some of my context is just the size of the project. And so I've been trying to figure out ways to make sure my tasks are well-defined and narrow so it doesn't try to use the entire thing, but at the same time, I want to make sure that it understands the main idea. So sometimes I'll throw that in if it starts to get lost or wander. So that's the only thing — it's like sometimes you burn through the tokens fairly quick. And I'm not sure if it's a WindSurf thing of throttling, but it may be. I've got to try with Warp [tool:Warp] also for the IDE — yeah, I'm going to try with some of those to see if there's the same problem there.

01:14:40 - Brandon Hancock
▶ Yeah, biggest tip always for large codebases is — in one session, create the task, and in session two, implement the task. That's always kind of like — one's the thinker, where you literally run UltraThink to where — just like you said — hey, make sure you fully understand the codebase, the connections, and everything, fully come up with the task, be confident that your solution that you're proposing will achieve the objective, then make the task and chat to implement. So you have like a thinker and a doer. That way, when you are doing, it's not just doing step one out of 10 and then instantly having to compact.

01:15:24 - Brandon Hancock
Also, at the end of the day, if you are using task-based driven development, hey, it doesn't matter if it does compact the conversation — it will always realign. It's just waiting for that 20–30 seconds for it to do the compact is kind of a buzzkill. So if you are trying to go speed mode, just hop over to a new session and say, implement this. Always a good way to save 30 seconds.

01:15:54 - Morgan Cook
Yeah, no, and I always maintain a task document. So even if it has a total lobotomy, it's easy to jump right back to the end where it was left off.

01:16:04 - Brandon Hancock
Okay. That's awesome, man. Is this a paid project? Your own project?

01:16:12 - Morgan Cook
This one is a paid project. I haven't had a lot of time to work on my own project, which is what I needed Trigger for. So I haven't really had a chance to jump into Trigger yet. Because I've been focused on this other project for a while.

---

<!--SEGMENT
topic: AI Video Automation, Replicate Models, and Content Monetization
speakers: Mitch, Brandon Hancock, scottrippey, Ryan - One Stop Creative Agency
keywords: Replicate, ElevenLabs, Sora, AI video, face detection, lip sync, speaker diarization, content automation, police body cam, YouTube monetization, Ponder, video editing AI, AI content pipeline
summary: Mitch describes his automated AI video production pipeline: generating clips with Sora, transcribing with ElevenLabs, running face detection and lip-sync verification via a Replicate model, and batch-processing overnight. One video hit 10 million views. Ryan mentions Ponder as an early-stage AI video editing tool. Brandon encourages Mitch to consider going full-time on the business, noting the scalable, asset-based revenue model.
-->

01:17:44 - Brandon Hancock
I think, Mitch, you're up next, buddy. I'm so excited to see what you have cooking.

01:17:52 - Mitch
Oh, I did nothing. I didn't do anything.

01:18:00 - Mitch
So I was kind of dark. Just now I was like, oh yeah, there's the calls. Let me show up.

01:20:16 - Mitch
But yeah, as far as my stuff, man — I was hopping in because I was like, these people are gonna be interested. Basically, I was kind of nerding out over a bunch of different stuff. One thing I wanted to share with the class is I've been using Replicate [tool:Replicate] a lot. Replicate has been really nice because I get to run those custom models. And so basically, what happens is like when I generate a bunch of these clips on Sora [tool:Sora] — I need to actually see who the heck is talking. And there's this custom AI model that I just linked here. And so basically, it's a really cool ML model where it identifies faces, tracks those faces. And it creates like a strength score of like, who's talking for what things.

01:21:07 - Brandon Hancock
Oh, that's cool.

01:21:08 - Mitch
Yeah. So basically, I take a clip and then I process it through ElevenLabs [tool:ElevenLabs] transcription tooling because it's like one of the lowest error rates and the fastest speed.

01:21:20 - Mitch
And then it gives me the specific — I went through so many errors of implementing this, by the way — because basically how this ML thing works is, if you send a clip and they're not talking, like it compresses on itself and it fails and then it just shuts down everything. So I was like, why is it not detecting the faces? And I was like, oh, it's probably because they're not talking. So I have to take the ElevenLabs transcript and then get what speaker is supposed to be talking. Anyways, I have the clip contents and then I extract who's supposed to be saying what. And then I understand, is that supposed to be on screen or off screen? And then for those specific things — I'm like, okay, is the lip sync on for the on-screen person? Is this supposed to be said by that person? And then basically for all those things, I have to edit the video programmatically to take those specific dialogue parts and only send that specific video to the ML model on Replicate.

01:22:19 - Brandon Hancock
Yeah.

01:22:21 - Mitch
And I've made a bunch of efficiency boosts too. So like, I was really sending the whole MP4 file to ElevenLabs. I was like, why am I doing this? Just send the MP3 file — that sped it up a lot too.

01:22:35 - Mitch
But basically what happens now — it would take me such a long time to make an idea because I have to wait for all these APIs to run. And I'm still working on the prompts to get the videos to be really good. It's a way more complicated process than I thought, but one video did hit 10 million views. So that was awesome.

01:22:54 - Brandon Hancock
That's awesome, man. Seriously. Congrats. What was — do I want to know the topic of the video?

01:23:02 - Mitch
I'll send it to you after if you want. But yeah — I think it's like 20 million views net as far as the overall account. And what was I gonna say on top of that — oh yeah, I just run a simple shell command to run like five to ten different ideas while I sleep. So now when I wake up, it's already checked, it already generated all the clips, tested all the clips, everything. And so now I can just wake up and it's all done. The editing is another thing, but now editing is so much easier with it.

01:23:56 - Mitch
But yeah, that's like the main stuff I've been working on. So I have questions — for the Replicate model, what's the cost for that? Because I'm looking at it and it says it looks like it's three cents to run, but that seems very low.

01:24:24 - Mitch
Yeah, it's around like three cents. Three cents a clip.

01:24:29 - Brandon Hancock
Seriously. Yeah.

01:24:31 - Mitch
That's crazy.

01:24:31 - Brandon Hancock
Okay. I was curious if it was going to be like — I mean, you've seen with video costs, like producing the AI videos is a monster. So that's why I was curious for analyzing the video, if it was also going to blow out the cost. But that's insanely affordable.

01:24:47 - Mitch
Yeah, it's crazy, right? So it's like three cents a video, but my usage for this month — and I just started this like maybe a week ago — is like $52.

01:24:57 - Brandon Hancock
Dang. Yeah. So out of curiosity, what's the cost for a day — like you go to bed, you run your script, what's the cost for that? Are you looking at a $100 bill? A $50 bill?

01:25:15 - Mitch
I'll just say the profitability is definitely there. So I don't even look at the bill. I'm just like, okay, like whatever it is, I'll make up for it.

01:25:22 - Mitch
What's crazy is — I mean, I haven't posted today or yesterday, but I'm still making a surprisingly good amount of money where I'm like, dang, like, that's crazy.

01:25:34 - Brandon Hancock
That's awesome. I think — I mean, I love videos because you produce a tangible asset once. And indefinitely, as long as that content gets served — which might get another spike six months from now — you make money. ▶ I cannot say enough how much I love these types of projects where you do the hard work once, pay the fixed cost once, and then there's unlimited upside. I love those types of businesses.

01:27:00 - Mitch
Just like trying to get this page on lock and then probably add another page. Because these cop videos — when I'm making fake AI cop videos, they're difficult to work with. A lot goes into it. I just want like more simple stuff. I have a friend who basically generates a bunch of different AI videos and they run meta ad tests on them and they just see which one works the best and then they post that on their own. So like they spend like $5 a video, they just produce a crap ton of them. And then there's like 20 different versions for one video, but all of those videos — they'll probably make maybe like $200, $300 per successful video.

01:27:51 - Brandon Hancock
Cause like, I think, A, you already have a lot automated. And then I think the part that's cool too is like — editing is the next part, the next hardest part, but hiring someone on Upwork to do that — that's the next bottleneck. And then at that point, it's like, dude, you literally just have an army of editors, and at that point, it's just — you have a full machine, you have the entire machine operated, and everything is leveraged. I love that. I'm very excited.

01:28:25 - Mitch
You know, one idea that I had — it's not for me, but I know somewhere down the line, someone's gonna make a Cursor for editing videos. Because like, with the tools that I'm doing, you can just track the dialogue, track the lip sync, do all these different things — you can do embeddings of each thing, so if the embeddings are too similar, you can just cut out the other. Eventually someone's gonna do it. Not me, but yeah, I'm excited for that time.

01:29:00 - Ryan - One Stop Creative Agency
Check out Ponder [tool:Ponder]. I was an alpha tester with them because I do a lot of video work. I'm mainly doing real estate stuff at the moment. They're working with Ryan Serhant over in New York — the real estate guys with the Netflix show. Yeah, I've done some stuff with them. It's very early stages at the moment but it has promise. You can just chat with it, tell it what you want, and there's a kind of AI chat in there. You feed in all your clips, feed in your audio file, and it produces something. The stuff I put in there and was playing around with — it's not usable at the end currently, but it's massively improved from the time I was using it from the first one to the last one I did with them. I did a call with Tim, actually, who is one of the founders there. But they've got quite a lot of VC capital behind them, so I think they'll probably make a good go of it.

01:30:05 - Mitch
I appreciate it, Ryan. Thank you.

01:30:07 - Brandon Hancock
And then the one last note I have, Brandon — if AI is like a drug, does that make you a distributor?

01:30:14 - Brandon Hancock
100%. Intent to distribute. You get extra heavy charges then, man.

01:30:28 - Brandon Hancock
Dude, real fast, going back to your business model — I love it. I just think it's — just watching on the sidelines as you do this. Dude, please, please, please. I know, obviously, you have a day job right now, but like, I really would love to see what a 100% focused Mitch on this looks like over the course of a year. Like, I think you easily could — not easily, like, it's gonna take a ton of work, obviously. But building out the teams, building out the systems, going all in on this — maybe in March, maybe in April, when some more capital and the bank is built up. Dude, I would love to watch that journey. I think there's nothing stopping it from going from whatever 15 a month that you said was the goal, to literally 100. There's literally — every problem is solvable in that, between the business at 15 and 100.

01:31:21 - Mitch
I definitely agree. I'm thinking about the same things too, for sure. And I'm definitely ready to make the move too. I'm just like — yeah, probably February and March, and we'll see.

01:32:01 - Mitch
Yeah, I make AI police body cam videos.

01:32:06 - Brandon Hancock
Very cool. I was wondering.

---

<!--SEGMENT
topic: Social Media Management App and Retail Screen SaaS
speakers: Ryan - One Stop Creative Agency, Brandon Hancock
keywords: social media app, facial recognition, Google image generation, brand induction quiz, PostHog, Nano Banana, retail screen software, SaaS, e-commerce, Stripe, comment automation, content scheduling
summary: Ryan shares that he has nearly completed a custom social media management app featuring facial recognition, AI content generation, brand voice onboarding, and automated comment response drafting. He also describes plans for a retail screen SaaS product for estate agents and aesthetics companies. Brandon encourages Ryan to focus on scaling the social media app rather than spreading to new projects, and shares a lesson from building a similar restaurant kiosk product pre-AI.
-->

01:35:31 - Ryan - One Stop Creative Agency
Welcome back, Brandon. I'll say that Patrick did a fantastic job deputizing in your absence. Been a couple of good calls. Patrick's a GOAT.

01:35:47 - Ryan - One Stop Creative Agency
I've just been cracking on. I don't know if you remember, I've been building that social media app. And I'm literally finishing it this evening. I'm adding in one final feature that I want to add in for myself — I can just select the post, put in the comment, and have it generate a response that I can just copy and paste into their social media. Because with the publisher agent that I've decided to API into, I can't pull the comments back in. But I'm lazy, and I hear a lot of these places and people that I'm managing the social media for — I don't have a clue really about their industry — and I want it to be able to bring all that context in and give me a response I can just copy and paste and do them on behalf of them.

01:36:24 - Brandon Hancock
So two things — A, congrats buddy, that's so exciting. Whenever you have an idea for something and then you bring it to life — coolest feeling on earth, especially when it's like, holy sh**, it's actually working. And second thing — we're so spoiled. We're like, damn, I have to do five minutes of work. It's so funny, because without it, it takes you hours. But it's just so funny how our goal is to automate everything to where you don't have to do any work, and it's whenever you're like, damn, I have to do five minutes of work. But in the grand scheme of things, 99% is automatic.

01:37:01 - Ryan - One Stop Creative Agency
That is so exciting. And in theory, under the SLAs I've got with them, I have to do a bunch of hours worth of responding to comments and messages and stuff like that. So if I can — and I'm going to have five to 10 to 20 clients in there, which will be the thing that then gets me up to kind of $20K, $30K monthly revenue, which would be cool.

01:37:24 - Ryan - One Stop Creative Agency
So once that's kind of moving in the right direction, I'll obviously add more features and stuff in. But it's got — it's using facial recognition. It's scanning everything as it comes in, tagging team members, all that sort of stuff in their content banks. Got fully integrated Google Nano Banana [tool:Nano Banana] image generation and tweaks and editing and all that sort of stuff. It's obviously writing all the content for me. All I have to do is show up once a month and shoot the content for them for an additional fee and then load it all in there. Even got it to do a brand induction quiz as well that I can send them now as a link to a token — takes them through a bunch of questions that helps me understand their business, get their brand voice, and they can talk to it, rather than having to type, which is quite cool.

01:38:06 - Ryan - One Stop Creative Agency
So I've added quite a lot in the last two, three weeks, but just been getting it to a point where it works properly. And I've just onboarded the first client onto it — that I'll be shooting the first content for in the first week of January. So if it all goes horribly wrong and doesn't work, then I'll come back and let you know at the end of January.

01:38:34 - Ryan - One Stop Creative Agency
And then the next thing I'm working on is building retail screen software — stuff to go in the front of retail shops for an aesthetics company and an estate agency. That'll be my next project. I've already built one for an estate agency, so I have a base. I'm just going to rip that code base and just add to it, and I want to make it SaaS so it can be controlled centrally. And then the little mini Windows machines that I'm sticking to the back of their TVs in their windows can just be tokenized. I can literally just put a token in, and it just talks to the cloud and pulls the content every 15 minutes from a SaaS application.

01:39:01 - Brandon Hancock
<Q>So quick question for you. I'd love to challenge focus. So out of curiosity, is there a reason why not focus more on the social media thing that you're just building and crushing — why cap at 30? Like, you said the goal is to get up to $30K a month. Is there a goal to hit 30, pause, and focus on the next thing, versus just keep focusing on that?</Q>

01:39:32 - Ryan - One Stop Creative Agency
<A>A couple of things. ADHD. So my mind is in a million different places at once. So I struggle with doing one thing. So hence I'm doing a lot of videography, which is kind of paying the bills at the moment. And then this social thing will hopefully be the thing that then just covers everything. And then everything else is a bonus. The screen thing came up by accident. I was just sat in one of my real estate agents' offices and somebody came in and tried to sell them the screen solution. And then I was like, hmm, I can do that. And I can do that cheaper.</A>

01:40:00 - Ryan - One Stop Creative Agency
I'm enjoying it, and then I've just put it on my portfolio, and I had about 15 incoming inquiries for various screens. So I just went into it, and I'm going to probably make — set that up as a pay-per-month type thing as well. It'll be a lot less, I'll have to get a lot more people onto it — it'll have a setup fee, and then monthly recurring revenue for that as well.

01:41:20 - Brandon Hancock
So real fast, Ryan, just one quick comment on that. So whenever — so I did something similar for restaurants back in the day, but it was more focused around the point of sale, so it was connecting the point of sale to a display — like a front-of-house thing — and it would just show most popular items, here's how many people tried the new special, just for social proof.

01:41:49 - Brandon Hancock
The quick lessons I learned — just things to keep on your mind too. The thing that most people needed was actually just graphics. So this was pre-AI, so what people needed the most was graphics, and I was like, wait, I'm actually — every time I sell a kiosk, the second order thing that has to be sold is a graphics person. And then I started to do the math, and then I was like, damn, I'm actually selling my thing for a hundred bucks a month. But the graphics person, by the time they do all the graphic work, they're making hundreds a month. So I was actually making my graphics person really rich. Because I was having to do the sales, do the leads, secure the client, and then the graphics person was making way more than I was.

01:42:55 - Ryan - One Stop Creative Agency
This was way back before AI image generation existed, because now maybe you can do that.

01:43:00 - Ryan - One Stop Creative Agency
You know, with all the new models, I have a graphic designer already that I use for years that does all my stuff. And I've got a few screens already made up for the clients from my designer. And then I've taken them into AI and said, right, I want a screen that does this. And the way that Nano Banana deals with text is incredible. So it's pumping me out really usable stuff. So yeah, I reduce the ongoing stuff by getting the initial kind of set done by my graphic designer, and then the rest of it I can charge the client still and get it generated with AI. So it's a win-win.

01:44:00 - Brandon Hancock
Dude, awesome. Well, Ryan, you're absolutely crushing it. We're rooting for you on — keep growing the agency — slash automated agency at this point, really. So yeah, please keep posted on all the adventures, man. And good luck on raking in the dough, buddy. Sounds like you've got a good system set up.

---

=== UNRESOLVED SPEAKERS ===
- Bastian Venegas Arevalo (passed through unchanged; not found in SPEAKER_ALIASES map)
- Elijah (no last name provided; passed through unchanged)
- Mitch (no last name provided; passed through unchanged)
- Tom Welsh (passed through unchanged; not found in SPEAKER_ALIASES map)
- Ty Wells (passed through unchanged; not found in SPEAKER_ALIASES map)