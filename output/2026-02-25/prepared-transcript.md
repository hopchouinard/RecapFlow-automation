=== SESSION ===
date: Not explicitly stated (references "2026" as current year)
duration_estimate: ~2 hours 50 minutes
main_themes: OpenClaw agent security and deployment, AI-assisted development workflows, member project demos (fitness app, YouTube monetization platform, cemetery management SaaS, Code Anvil Mobile), AI tooling comparisons (Claude Code, Codex, Gemini, Warp), formal AI verification/AGI research, business strategy and SaaS monetization, future of work and AI automation

---

<!--SEGMENT
topic: Pre-call chatter and personal projects
speakers: Marc Juretus, Patrick Chouinard
keywords: mobile app, Apple App Store, personal website, CV portfolio, fitness app, OpenClaw, N8N, static site, CMS, Hostinger, real estate site, Google Sheets
summary: Marc and Patrick catch up before the formal call begins, discussing mobile app deployment friction with Apple, Patrick's personal portfolio website rebuild, and Marc's fitness tracking app progress. Marc notes his fitness app has reached a near-releasable state with voice-dictated workout logging, while Patrick describes building a static site with an admin-controlled CMS backend.
-->

00:00:59 - Marc Juretus
That's the only mobile app that we've deployed.

00:01:03 - Patrick Chouinard
Okay.

00:01:04 - Patrick Chouinard
And as always, Apple's a pain in the rear there.

00:01:08 - Patrick Chouinard
As always, man.

00:01:10 - Marc Juretus
That was always a blast for that crap.

00:01:12 - Patrick Chouinard
That's the fun about the corporate world.

00:01:14 - Patrick Chouinard
We don't have to deal with Apple.

00:01:18 - Patrick Chouinard
Or the Android App Store.

00:01:20 - Marc Juretus
Ah, yeah.

00:01:21 - Marc Juretus
Ain't that the truth, man.

00:01:23 - Patrick Chouinard
Because everything is internal.

00:01:24 - Patrick Chouinard
So we have our own app store.

00:01:27 - Patrick Chouinard
<Q>What are you working on these days?</Q>

00:01:31 - Patrick Chouinard
For the job, it's still the same thing.

00:01:33 - Patrick Chouinard
We're still in evaluation mode across a platform.

00:01:36 - Patrick Chouinard
But personally, I just decided to revamp my own personal website.

00:01:42 - Marc Juretus
Nice.

00:01:44 - Patrick Chouinard
I wanted to put my CV online in a form that's more interesting than just a plain CV.

00:03:01 - Patrick Chouinard
<A>Right now, there's just two sites that I decided were quality enough to showcase, but as I'm creating them, they're just going to be accessible through my personal website as a subdomain of my main domain name. So easier on the naming things and easier whenever I want to showcase something, I just give people the address of my site and that's it.</A>

00:03:24 - Marc Juretus
My fitness app went a lot faster and that stock school app I had — it's to a point, the code that it writes, that fitness app, I could give it to somebody right now. I can honestly go in now and I can pull up someone who has a login and I can assign their active workout and then I can view their log. And like I keep talking to OpenClaw [tool:OpenClaw] and it's like, you're at a point you should be able to try to have a soft release of this.

00:03:54 - Marc Juretus
I'm like, yeah, that wasn't my objective, but it's very helpful.

00:04:00 - Patrick Chouinard
When you're giving it, like, you know, what you're trying to work on.

00:04:05 - Patrick Chouinard
But I'd be interested in looking at that because I'm starting at a new gym, actually, this week.

00:04:11 - Marc Juretus
Yeah, it's pretty slick. The thing that I like the most is, like, I have this thing where you dictate workout. So you can go in and log what you did one by one. But you can click dictate workout and say what you did — say you're doing triceps, skull crushers and extensions — and it'll map them up and log them. And I was like, holy cow, man. Yeah, it's usable now.

00:04:44 - Patrick Chouinard
Actually, what I would need is something with vision because the problem I have is the old gym I was going to was a little family gym, like very, very small and mostly dumbbells and free weights. Now I'm going to a more commercial gym, and my biggest problem is to know how or what to do with each of the new machines, because there's like 20, 30 machines in there that I have no clue how to use. So I'd like something where I could just take a picture of the machine and it's like, tell me what exercises I could do on that thing.

00:05:23 - Marc Juretus
Well, you know, like the few people I do train, I say start out with three days a week if you're able to do that.

00:05:30 - Patrick Chouinard
That's what I say — do push, pull, and legs.

00:05:33 - Marc Juretus
So, you know, push will be like chest, triceps, shoulders.

00:05:40 - Patrick Chouinard
My challenge is I don't know what machine does what in the new gym.

00:05:43 - Marc Juretus
Oh, well, if you go in there, I have video demos of it. I'll send you the link. You can play around and log in.

---

<!--SEGMENT
topic: Anthropic Security launch and patent discussion
speakers: Patrick Chouinard, Ty Wells, Marc Juretus
keywords: Anthropic, Anthropic Security, provisional patent, end-user applications, market disruption, stock impact, Lucid Dev, Usai, formal verification, AI hallucination
summary: Patrick raises Anthropic's launch of Anthropic Security, prompting Ty to discuss the competitive threat to end-user AI application developers and his own provisional patent on a formal verification layer for AI output. Ty explains his strategic pivot away from consumer-facing apps toward infrastructure-level tooling.
-->

00:08:05 - Patrick Chouinard
Hey, Ty, did you see that Anthropic [tool:Anthropic] has started Anthropic Security [tool:Anthropic Security]?

00:08:13 - Ty Wells
When I saw that, I thought about you right away.

00:08:16 - Ty Wells
Yeah, I saw that. <A>I'm like, this is why I'm trying to get away from end-user application stuff, because these guys will just — they can knock you out in a glancing blow. They don't even have to touch you, right? I mean, they're dropping stocks like crazy just from an announcement. So, yeah, that's going to be problematic long-term.</A>

00:08:43 - Patrick Chouinard
<Q>Well, if you have a patent for it, you could probably negotiate a pretty sweet deal if they're going into the same arena that you are.</Q>

00:08:52 - Ty Wells
Yeah, yeah. I do have a provisional patent on my stuff. But I'm actually — yeah. Here's the funny thing about it. That was a week ago. This week is a whole different story. But yes, I have a patent that I feel pretty confident in.

00:09:42 - Marc Juretus
I think I'm going to take the Google Generative AI Leader course. Not that it's going to add a lot to me, but it looks like something on a resume, you know, is the only reason.

00:09:55 - Patrick Chouinard
Yeah, then you can use the course to build a resume site like I did last weekend.

---

<!--SEGMENT
topic: N8N versus Claude for automation workflows
speakers: Marc Juretus, Patrick Chouinard
keywords: N8N, Claude, automation, real estate site, Google Sheets, local VM, tokens, cost, Supabase, static site, CMS backend, Vertex AI
summary: Marc describes building a real estate demo site and raises the question of whether N8N is still necessary given Claude's growing agentic capabilities. The group discusses the cost trade-off between N8N running locally at zero marginal cost versus Claude consuming tokens on every interaction, concluding N8N remains valuable for complex, cost-sensitive flows.
-->

00:10:00 - Marc Juretus
Oh, I built, you know what I built today? Because I'm off all week, so I'm really screwing around. I built a real estate site because there's a couple of realtors that actually have asked me about it. And what I would do is I would create like a Google Sheet [tool:Google Sheets]. And if they had a contact, the N8N [tool:N8N] inflow would see, oh, new contact — this is what you're looking for — it's scanning the properties, and if it's a match, send them an email.

00:10:26 - Marc Juretus
<Q>But it's funny, like, what is your mindset on that now? Because the guy that I took the long course with for six months, I was just watching a video of his he just put out and he was discussing, do you even need N8N now with what Claude's doing?</Q>

00:10:43 - Marc Juretus
He said, as of now, you do because there's very complex flows. But not only about complex flows, it's about the fact that N8N run on a local VM costs you zero compared to Claude [tool:Claude] who costs you tokens every single time.

00:12:00 - Marc Juretus
And it's just — it's cool you could do that, to have like a dev area, but man, my machine ain't that powerful to have like three or four different Supabase [tool:Supabase] apps running locally.

00:12:12 - Patrick Chouinard
<A>But that's why I've started more and more — well, the sites I'm publishing are not really applications, they're static sites, but the content can be controlled through a backend admin portal. So that's actually the pattern I'm using more and more. I have a backend portal that manages whatever gets published to the site and just pushes every time. And yeah, I'm not going to be able to do applications like that, but for static sites, it makes the static site a lot more powerful for no cost whatsoever.</A>

00:12:50 - Marc Juretus
Really crazy thing with the real estate site — I basically said, create me about 10, 20 realtors and about 20 properties in the Pennsylvania/New Jersey area. There's pictures of the realtors, there's the properties, the prices of the houses. I'm like, man, this is just insane.

---

<!--SEGMENT
topic: Brandon's return and AI productivity setup
speakers: Brandon Hancock, Patrick Chouinard, Marc Juretus, Ty Wells
keywords: MetaQuest 3, Claude Code, Codex, Gemini, PowerPoint automation, Google ads, OpenClaw, Meta headset, parallel agents, pitch decks, YouTube
summary: Brandon returns from an extended absence and shares updates including using a Meta Quest 3 headset to run 15 simultaneous Claude Code instances, using Codex for automated PowerPoint generation, and plans to document a Google Ads coaching engagement on YouTube. He frames his productivity philosophy around maximizing token-generating time.
-->

00:14:22 - Brandon Hancock
What's up, everybody? Sorry, I got beanie hair.

00:14:34 - Brandon Hancock
I'm pumped to see all these familiar faces, give you all the updates. We'll definitely give people a couple of minutes to all hop on. But yeah, very excited to see you guys.

00:15:27 - Brandon Hancock
All right, guys. I've gone deep in AI. I'm just now coming out. My favorite new gadget that I have to show you guys is — I got this. It's the Meta Quest 3 [tool:Meta Quest 3], basically. So what I do is I hook it up to my Mac, and I have like 15 Claude Code [tool:Claude Code] instances at the same time on like a projector in front of me, as big as I can see. And I'm doing the work of an entire company myself. It's crazy. I have marketing. I have sales out.

00:18:00 - Brandon Hancock
Most Helpful Win. Claude Code, obviously, for all things related to code, still my favorite. Cool recommendation — I have been having to work a ton recently on creating PowerPoints for pitch decks, presentations, education content, like all sorts of stuff. ▶ Codex [tool:Codex] is by far the best PowerPoint maker I've ever dealt with. I will kick it off and it will make a 90-slide presentation for me in 30 minutes. And then I just iterate from there. But Claude Code under no circumstance could I ever get it to do well at more than like 20 slides, and even then it would struggle.

00:18:37 - Brandon Hancock
▶ But Codex — just to give you guys a heads up, because I want you guys to try it if you have to make presentations — you hook it up to Gemini [tool:Gemini] so it can make images, and then you just say go forth, here's a brain dump, go make PowerPoint slides, and it will make custom images, fit them in the PowerPoint, because Codex is very precise, it'll test to make sure it's formatted well, do it again and again and again. So I'm making every week probably close to 200 PowerPoint slides for different things I have to do, and Codex is doing all of it. So, yeah, if you're doing a pitch, Codex is the game changer.

00:19:18 - Brandon Hancock
We are hiring an ads coach for our company. His name's Peter. Awesome guy. Used to work at Google. And we're going to do like a four-week, six-week program with him where he's going to help us redo our ads. And we're just going to be sharing all of that on YouTube. So, if you kind of wanted to see behind the scenes of like, oh, cool, I have a software idea and now I want to get traffic — how do I actually do that with Google Ads [tool:Google Ads] in 2026? This will probably be the video.

---

<!--SEGMENT
topic: Patrick's AI-powered CV portfolio and CMS
speakers: Patrick Chouinard, Brandon Hancock
keywords: Claude Sonnet, Hostinger, GitHub, CMS, JSON, bilingual, French English, career portfolio, admin dashboard, CloudFlare, OpenClaw GitHub account
summary: Patrick demos his personal career portfolio website, which uses Claude Sonnet to parse freeform job experience notes and rewrite them in structured JSON for both French and English, populating a custom CMS. He also describes giving OpenClaw its own GitHub account within a shared organization, treating it with the same access controls as a human employee.
-->

00:24:00 - Patrick Chouinard
The idea is main site. But what I really love about that site — this is the public site. This is what's pushed to Hostinger [tool:Hostinger] automatically by Claude Code.

00:24:20 - Brandon Hancock
Oh, really?

00:24:20 - Patrick Chouinard
Behind the scene, I have an admin dashboard that allows me to manage all the eras I split my career into, all of the engagement, the technology, the skill, the narrative, everything here — I can update and push to the website.

00:24:40 - Patrick Chouinard
▶ Basically, I created my own CMS system. And on top of that, when I create a new engagement — that's the part I always say documented my job experience — so now I have "Create with AI." I just grab, let's say, I have a little fake one I created just for demo, but it's very loose, like I worked for that one from around September, very vague, nothing structured whatsoever, just explaining what I did.

00:25:17 - Patrick Chouinard
▶ Then it's Claude Sonnet [tool:Claude Sonnet] behind the scene that rewrites the whole thing, and it will submit the rewrite in JSON in order to fill all of this — the form — so not only the job description, but like the employer name, the client, the project, like it extracts everything, writes in both French and English as a native speaker, so it's not writing in one and translating, it's actually writing both in a native way, and it even adds notes.

00:28:00 - Patrick Chouinard
That I created for OpenClaw. So OpenClaw has its own GitHub account [tool:GitHub]. I have mine, and we share an organization. So everything it develops, it develops in that organization.

00:28:10 - Patrick Chouinard
▶ I really manage security exactly as if it was a human worker.

---

<!--SEGMENT
topic: OpenClaw security architecture and deployment
speakers: Brandon Hancock, Patrick Chouinard, Darryl Goldstein, Juan Torres
keywords: OpenClaw, prompt injection, Slack, Google Drive, Gmail, Discord, Ubuntu, Proxmox, Docker, Mac Mini, EC2, VPC, Telegram, email isolation, calendar, context window
summary: The group compares approaches to deploying OpenClaw securely. Patrick describes a hardened setup using a dedicated Ubuntu VM on Proxmox, isolated Gmail, Google Drive, and Discord channels per context. Brandon shares his simpler Slack-only containment approach. Juan asks about AWS VPC isolation. Key recommendations include email whitelisting, dedicated calendars, and using Discord channels to manage context windows.
-->

00:28:15 - Brandon Hancock
Real fast, guys, I just want to share what I'm doing with OpenClaw. Just maybe it'll strike a conversation. Patrick is definitely going down to like 10 out of 10 most secure. I probably should be doing what Patrick's doing. We all should probably do what Patrick's doing, to be honest.

00:28:32 - Brandon Hancock
My poor man, lazy way — what I'm doing right now is I just have it only accessible to Slack [tool:Slack], and I'm only feeding it information. Like it's being fed the information I want it to have access to, and it can't do anything else. Like it doesn't have access to email, it doesn't have a WhatsApp, it has nothing else. All it has access to is an individual Slack channel.

00:29:03 - Brandon Hancock
So that's my poor man way about making sure it doesn't do anything crazy. <Q>Could it go absolutely bonkers, though, if it goes to a website that has some prompt injection stuff?</Q>

00:29:14 - Brandon Hancock
Maybe. But that's how I'm doing it to automate a lot of customer research and outreach. I just have it hooked up to Apify [tool:Apify] with LinkedIn browse features. So anytime someone tries something out, we can quickly just do a sit-rep on who they are, what department they probably work for, and who's their boss, and gives us a report.

00:29:50 - Patrick Chouinard
It's not, but if I had to say one thing — I did give mine an email, but it has its own, and I gave it one rule.

00:30:00 - Patrick Chouinard
▶ It only reads email coming from my email address. Anything else, it tells me there's an email, but it doesn't read it. That way, I'm avoiding the prompt injection.

00:30:10 - Patrick Chouinard
It has its own calendar. So instead of playing with my calendar, it actually creates the meeting itself, and then it invites me.

00:30:23 - Patrick Chouinard
It has its own dedicated machine with nothing else on it. It has its own Gmail and Google Docs [tool:Google Docs]. So since it has Google Drive [tool:Google Drive], that's where I put all the documentation it can interact with.

00:30:37 - Patrick Chouinard
▶ Try interacting with Discord [tool:Discord], because with Discord, you can very easily create multiple channels and split your context by channel, so you don't overwhelm the context window and start spending enormous amounts of money in tokens because you send 20,000 tokens in every exchange.

00:31:04 - Darryl Goldstein
<Q>Are you running on Mac Mini? What are you using to run?</Q>

00:31:09 - Patrick Chouinard
<A>It's a Ubuntu VM running on Proxmox [tool:Proxmox].</A>

00:31:17 - Brandon Hancock
I did, real fast, buy a Mac Mini [tool:Mac Mini]. I have yet to do anything with it, but the plan is to put OpenClaw on it. It's completely overkill, but I just wanted to do it.

00:31:37 - Juan Torres
<Q>Yeah, I don't know, Patrick or Brandon, what you would recommend, but I've thought of doing that for an EC2 instance [tool:AWS EC2], just have its own VPC, its own virtual private cloud with its own security permissions, just to be able to handle the network. But when I give it resources, like a database instance, then I'm afraid that it's going to erase it. So how do you regularize the relationship between OpenClaw and the resources within your VPC?</Q>

00:32:25 - Patrick Chouinard
<A>If you can put a VM somewhere and even Docker Desktop [tool:Docker] — that's all it needs. Isolation. It doesn't need resources. So I really don't get why everybody is going and putting that on VPS or having a monthly fee to run it. It runs on hardware.</A>

00:33:25 - Brandon Hancock
I have it running in Docker on my computer. It's just a pain because my co-founder, if my computer turns off, he's talking to OpenClaw and he's like, damn it, why is it not working? And it's because my computer is asleep. So that's why we're going to get an external device.

00:33:34 - Brandon Hancock
▶ Juan, to answer your question, I am trying to limit the exposure of what it can do. Mine is — you consume what I give you, and you can write to a Google Drive. There's no escaping the box that I have built it in.

00:33:55 - Brandon Hancock
I almost just want to have — I don't want OpenClaw to have the ability to send an email. We have it doing so much customer research. My biggest fear is it goes, well, I'll just be a little bit more proactive, and I'll just write the email. And then all of a sudden, it's blasting 500 clients garbage.

00:34:22 - Brandon Hancock
▶ I always just write to a Google Drive or a Google Sheet, and then you can have an external service reach in — that is controlled programmatically and not by AI — and just look for a new thing and do what you want. But there needs to be a clear box that it can't get out of, and you want to peek in when you need something and feed it only what it needs and nothing else.

---

<!--SEGMENT
topic: Jaylen's content creator monetization platform
speakers: Jaylen Davis, Brandon Hancock, Darryl Goldstein, Ryan - One Stop Creative Agency
keywords: YouTube, TikTok, Instagram, content creator, video request, monetization, subscription model, fan funding, Vimeo, in-app video recording, community platform, School, revenue model
summary: Jaylen demos his web app that lets content creators monetize fan video requests — fans fund a request, the creator fulfills it and receives 90%. Brandon suggests pivoting toward a recurring subscription community model similar to School, while Darryl proposes adding in-app video recording for non-technical creators. The group debates monetization math and go-to-market angles.
-->

00:36:19 - Jaylen.Davis
Okay, so yeah, basically, I came on maybe back in October or November. Mitch McCauley, he actually sent me the link. And since then, I've developed my web app tremendously. Let me share my screen.

00:36:56 - Jaylen.Davis
Yeah, basically, and since then, we've pivoted to not only — we help YouTubers. We also work with Instagrammers and TikTokers. Basically, it's just a platform where a content creator can monetize their video requests. So you can basically tell your fans, look, if you want me to make this particular video, I'll do it for this price. Once they fund it, you make the video and then you get paid 90%. So if someone asks Brandon to make a video about something, and let's say his price was $100, they put in the $100, he makes the video and then he receives $90. It's as simple as that.

00:37:41 - Jaylen.Davis
Yeah, so far we have about 11 people on the platform. We're making progress and I just wanted to get any feedback on any possible ideas. For creators, you guys can actually decline topics if for whatever reason you don't want to create that particular video. You set your own price when you sign up.

00:38:07 - Brandon Hancock
One quick thing — the second I saw your face hop on the call, I was like, oh, I have ideas. So, I think my main thing that I've always thought would be cool is for people to vote and downvote on ideas, and me pay you a monthly subscription, 50 bucks a month. Because then it's recurring revenue and you're not at the mercy of customers. Like, it's consistent.

00:38:38 - Brandon Hancock
▶ You know, $50 a month and you built me a School [tool:School] where my YouTube members can come in, chat about my videos, and request future videos. Like, basically, be the blog of what YouTube is. Turn every YouTube channel into a school community automatically. And then just tell the creator, hey, you pay me 50 bucks, 75 bucks, 99 bucks a month, and I will give you access to run this community.

00:39:43 - Brandon Hancock
I will say just for number-wise, most audiences like to do a sponsored video. I always like to see where the math goes. Like, what does the app have to be, and how long does it take to get there? Or, hey, if I do the founder mode, where they pay 50 bucks a month or 100 bucks a month — how long does it take, if they do 100 bucks a month, to get to $20,000 a month? Okay, I need 200 founders at $100 a month. Boom, I just have to find 200 people on earth to give me $100 a month. Such an easier problem to solve.

00:45:24 - Darryl Goldstein
<Q>So, is there a feature here where you could capture that video right from your app, as if it's on a YouTube-type video, meaning that the person making the video for you — just make it real simple — they can come on here and say, hey, Darryl, happy birthday to your mother, have a great day, and they don't have to produce anything? Capture it right here, through a recording on your app, and boom, it's done.</Q>

00:46:14 - Jaylen.Davis
<A>I get what you're saying. No, we currently don't have that feature. I believe Vimeo [tool:Vimeo] has something like that where you can basically just request a quick video from a celebrity.</A>

00:46:29 - Darryl Goldstein
You have to solve the technical part, but I'm talking about feature-wise — it might make it easy for people that are paying, for the person who has to create the video. Maybe they're not a content creator necessarily. They don't know how to set up everything, but they can come here right with the camera.

---

<!--SEGMENT
topic: Marc's fitness and stock school apps demo
speakers: Marc Juretus, Brandon Hancock
keywords: fitness app, workout logging, voice dictation, exercise library, Grok, AI trainer, stock school, paper trading, Vertex AI, Google Cloud, Model Garden, RAG, Gemini, Google Generative AI certification
summary: Marc demos his fitness tracking app featuring voice-dictated workout logging, an AI trainer with workout history access, and AI-generated exercise demo videos made with Grok. He also shows a stock school app with paper trading and an AI coaching feature. Brandon recommends Gemini for cost-sensitive use cases and notes Claude Code's subsidized pricing.
-->

00:47:26 - Brandon Hancock
What is going on, man?

00:47:53 - Marc Juretus
So, what have I been working on? I know you guys were talking about OpenClaw. I have one. I have it on a Google virtual machine up in the cloud, running Ubuntu 22.04. What I have it doing is I talk to it in Telegram [tool:Telegram], and say I'm out at a bar or something. I can talk to command, email trainer, their name, their email. It'll send a pre-formatted email addressed to them — the basic foundation of how I work out — but it taps into my calendar and shows my availability dates.

00:48:32 - Marc Juretus
Another one is I'm trying to help my son find a job, and I have another one — it pulls in a job service API, gets Indeed [tool:Indeed] and a couple others, but if I type "get jobs, whatever category," say laborer and then email, it'll email any available job listings to his email address or whoever I put in for email.

00:48:48 - Marc Juretus
And I have it for a daily motivator, but I had to drop that down to Haiku [tool:Claude Haiku], man. It was starting to run me some money. I was like, yeah, don't leave it on Opus [tool:Claude Opus]. I'll tell you that.

00:49:00 - Brandon Hancock
▶ What I recommend for applications where people use them — Gemini is the best bang for buck on capability and cost, at least that I've seen right now. So I would recommend just because, without it, it gets pretty expensive using anything related to Opus.

00:49:27 - Brandon Hancock
I mean, they just — Claude Code spoiled us. I don't know if you saw the report. They're subsidizing it — it was either 17 or 14x. So we pay $200 and they cost, I think it was like $2,800. So it's crazy how much they're eating for us to use their platform right now.

00:50:23 - Marc Juretus
I'm going to probably take the Google Generative AI exam [tool:Google Generative AI certification]. I've been up on the cloud — I spun up a RAG on Vertex AI [tool:Vertex AI], it spun up a clothing site that has a chat, and then I used the image gen from Model Garden [tool:Google Model Garden] to generate images, like, in the admin pool for that, just so I kind of get a feel of that.

00:53:43 - Marc Juretus
Can you see my screen? Yeah, so basically that's a site. I have a couple of different aspects to it, but it's kind of built for stuff that I do. Like when I work out at 5am in the morning, I went ahead — like I'm doing triceps and chest — and I just pull up three random exercises of each, so it'll go in there, it'll give me three random exercises and the basic summary of what they are.

00:54:28 - Marc Juretus
I have an exercise library that's basically all of my exercises. And I did make a video on Grok [tool:Grok] — that's not even me — of working out. So I'll put all the exercises in for that.

00:55:03 - Marc Juretus
The crap that blows me away that I didn't have to write was — this is my workout plan. And this is, if I were to say you were my client, Brandon, I would come in here, I would create a workout for you. And then I can go into the admin tool and I can just say — I can view your workout and I can modify it so that when you pull it up you see, hey, Monday you do chest and tris and then you do these exercises.

00:55:40 - Marc Juretus
And then the one thing is I actually have a trainer in there. In here I have a trainer where if you say "I need a shoulder workout," it actually has access to your history and sees what you did. It says, hey man, your shoulders look like crap because you've only been doing this, that or the other.

00:56:27 - Marc Juretus
And the one that blew me away the most was — say I'm in here and I want to add to workout. I have a button called "Summarize Workout." And when you click on the button, instead of you going in and manually logging each exercise, I actually give you the ability to just click on the button and say, hey, I did three sets of tricep pulldowns for 50, and I did three sets of skull crushers for 50. It'll actually log them and go on your history and parse them out to separate exercises that I have in my database.

00:57:16 - Marc Juretus
And then I got a stock school app too, where you go in and if you take three tutorials, I give you $25,000 in paper money. It tracks it. And then I actually have a trading coach that'll go in there and say, hey, man, you went a little too heavy in tech.

---

<!--SEGMENT
topic: AI development workflow and productivity philosophy
speakers: Brandon Hancock, Patrick Chouinard, Marc Juretus, Rag Ch, elijah stambaugh
keywords: Claude Code, Warp terminal, Codex, cursor, anti-gravity, tmux, parallel agents, keyboard shortcuts, token throughput, Meta Quest 3, Python, TypeScript, FastAPI, Dockling, RAG
summary: Brandon shares his evolved coding workflow using Warp terminal with multiple parallel Claude Code instances, abandoning the IDE editor in favor of terminal-first development. He recommends Codex for long-running high-precision tasks and Claude Code for rapid iteration. Patrick advises spreading workloads across Claude, Gemini, and GPT subscriptions to manage token costs. Rag asks about Claude Code terminal setup and Mermaid diagram extensions.
-->

00:51:28 - Brandon Hancock
Can I, real fast, while you're pulling that up, Marc — awesome YouTube video that I just watched today. It's the latest My First Million episode. They just talked to the guy who runs the Starter Story YouTube channel, and he just breaks down the best trends he sees right now. And a lot of them just come down to making apps on the App Store, strictly because — the brain-breaking thing that they talked about is they make content on YouTube, so they just create 10 ideas on shorts to figure out which one of these app ideas goes viral. And they never built the app. They just faked it like they have an app built. And then if a video takes off, they're like, oh crap, go build the app. ▶ Because software is never the bottleneck. Attention has always been the bottleneck that then gets driven into an app. [link:My First Million / Starter Story YouTube episode]

01:00:19 - Brandon Hancock
Real quick, final thing, and we'll keep cruising. Marc said it so well — it just spits out so much. So like, the way I'm measuring a good day right now is how many times per day was I busy generating tokens? Like, what is my idle time compared to my output time? So that's why I brought the Meta Quest 3, because right now, humans are the limiting factor for AI.

01:01:00 - Brandon Hancock
▶ But then, once we're at the same playing field, it's how long can you, per day, just take shots downrange using AI, and every time you take an action, can you build a system to make it, to get leverage for future actions? So the more I keep thinking about AI, I'm like, literally every moment that I'm awake, I need to be shooting shots downrange, or I'm just kind of wasting time.

01:14:24 - Brandon Hancock
So I prefer at this point, if I'm going to do anything related to AI, I like using Python [tool:Python]. And I'll tell you why. It's because Python is leading the front on AI. For example, working with a client on a project, I love Dockling [tool:Dockling]. Dockling is one of my favorite embedding and chunking tools out there for building RAG applications. And it's native to Python. And we're like, but they want to do everything in TypeScript. So as a result, I was like, oh, there's a Dockling TS package. It's fake — all it does is it's a pointer to a version of you running Python somewhere else.

01:15:23 - Brandon Hancock
▶ The key thing here is just like, okay, I need to make a Python application and just asking AI, what are the core things I need to know? I need to run it. It needs to be able to receive and send requests. So I need to run it on somewhere like Railway [tool:Railway] to run it. Cool. FastAPI [tool:FastAPI] or Flask [tool:Flask]. So just knowing the three or four words to make you dangerous, to build a modern Python application.

01:18:28 - Brandon Hancock
▶ One thing I do just want to mention — when it comes to long-running jobs, if I know something's going to take 20 minutes of just iteration, iteration, iteration, Codex. I am falling in love with Codex for tasks that have to be precise. I don't care how long it takes. I just want it to work after 20 minutes of you doing your thing. Codex is the move. Just for quick iteration — I'm just like, bam, bam, bam, adding a feature, checking it, doing stuff — Claude Code all day, baby.

01:21:15 - Brandon Hancock
Okay, so here's the main things that I would watch if I was you. So the most important one is the editor setup, where I break through exactly how to set up all the different commands, where when I'm coding, I have 15 or 10 different Claude Code instances up, and I'm using my keyboard for everything. My hands never leaving the keyboard.

01:22:53 - Brandon Hancock
So first mistake — don't use the Claude Code terminal. That's mistake one. You're just using a regular terminal.

01:25:07 - Brandon Hancock
I'm using Warp [tool:Warp] to do everything. And I just have a script to tell Warp, like, hey, I'm ready to start working again. And it just opens up six modules, eight modules in a nice window format. And then anytime I want to actually go look at a file, I basically just off to the side have cursor [tool:Cursor] opened just to look at a file, but I'm not in the editor anymore. I've left the editor behind.

01:27:53 - Patrick Chouinard
▶ Just wanted to say — I work with more junior developers that are not yet able to split their brain 15 ways. And they don't have necessarily the amount of money it would take to run eight Claude Code in parallel and still have tokens at the end of the day. So what Rag is doing is pretty good also — you have your Claude Code to do the hard work, but all of your code review, all of the management stuff, you can leave it to, in this case, Gemini 2.5 Pro [tool:Gemini], just so it takes off a little bit of the pressure on your tokens and Claude. And if you want, you can — I would even say, if you have an OpenAI account, start a Codex window. Have not just eight or ten Claude Code — try to spread it as much as you can, so you can leverage all the tokens from all the subscriptions at one point and not overload your token budget.

01:29:00 - Patrick Chouinard
▶ Split responsibility — Claude does one type of work, Gemini does another type of work, GPT does another type of work.

---

<!--SEGMENT
topic: Ty's formal AI verification system and AGI research
speakers: Ty Wells, Brandon Hancock
keywords: formal verification, AI hallucination, AGI, GitHub Actions, regression testing, autonomous agents, persistent memory, Usai, provisional patent, non-deterministic testing, Cypress, unit testing, end-to-end testing
summary: Ty presents his renamed project Usai, a formal verification layer for AI output designed to catch logical errors and hallucinations (estimated at 30–40% of outputs). He describes it as a "spell checker for logic" built on GitHub Actions, extended to support long-running autonomous agents with persistent memory. Brandon connects this to his own pain point of regression testing non-deterministic AI applications.
-->

01:05:02 - Ty Wells
We — I'm going to show you today, so...

01:05:13 - Ty Wells
Check it out. Try Lucid Dev [tool:Lucid Dev].

01:05:18 - Ty Wells
Yeah, actually, that was a week ago. I was telling Patrick that things have shifted since then. So I had to change the name from Lucid. It's — I had to change it to Usai [tool:Usai].

01:05:34 - Ty Wells
You guys can come and look at it yourself. But I'll just give you a quick check of where this is. You can just read that first page and tell me if it makes any sense to you.

01:06:00 - Ty Wells
Okay, so basically what I'm doing here is creating a formal verification layer for all AI output because we know AI models hallucinate, right? 30 to 40% — all depends, right? How deep the context window is. ▶ Basically, it is a spell checker for logic that's coming out of the model. So I did this paper basically to discuss how this is actually implemented.

01:06:40 - Ty Wells
And I was reaching out to publish it on the arXiv [tool:arXiv]. I did put a provisional patent on what I built.

01:07:06 - Ty Wells
Can I actually tell you my biggest problem that I'm running into right now?

01:07:17 - Brandon Hancock
<Q>Because it's kind of along the same lines, but coming out from a different perspective. So the thing that I want to focus on is help with testing with AI — meaning there's unit tests, cool, like I understand this function, here's the 200 ways we could use this function, here's the inputs, outputs, cool. Unit test makes sense. Then you keep going up the stack and then there's end-to-end testing, which at this point you pretty much use Cypress [tool:Cypress]. But now that things are different, it's very hard — with AI, especially if you're building an entire application around AI, it's very non-deterministic by default. So it's like, I almost want to have at the same time 30 different users for every archetype that could happen. And every time I make a code change, I would love the ability to review to make sure I didn't break anything. Because now that I'm getting more into production, that's the biggest issue I'm running into — I can crank out code like there's no tomorrow, but it's like, oh crap, did I break something that I built six weeks ago?</Q>

01:09:10 - Ty Wells
<A>So to answer your question, yes, that was one of my biggest issues too, right? You just — the regression testing is just crazy. So you wanted that to happen automatically. And this does that through GitHub Actions [tool:GitHub Actions] where it verifies the code that's in there automatically. It runs it and tries to verify that code.</A>

01:09:43 - Ty Wells
So what I did was I took it a step further and wanted to try to reach AGI, right? Meaning if I have better code coming out — because AGI itself is code. And so I use my verification process to create the things that make up AGI and I'm just testing it. So I created — and I started this before OpenClaw — but it's basically the ability I've been trying to achieve for these long-running autonomous agents that have memory that persists and so forth. I built that using Usai as a verification process of the different agents to do that.

01:11:40 - Ty Wells
So this is actually the inaugural flight of this autonomous agent. So we shall see what comes to the end of that.

01:12:15 - Brandon Hancock
I like the way you're thinking about this because, I mean, yeah. How do we just make stuff reliable? I mean, you're hitting a very — I think it's the coolest part of a new problem that was just introduced to society, which we're all facing. I mean, if you look at the chat, it's everyone can spit out more code than they can handle at this point. And now it's just like, shoot, does it actually work? Because there's a difference from way back in the day — does the code compile, AKA, is it syntactically correct? Yes, it builds, but is it semantically or behaviorally doing what I want it to do? Not always.

---

<!--SEGMENT
topic: Scott's Code Anvil Mobile and SOP system concept
speakers: Scott Rippey, Brandon Hancock, Patrick Chouinard
keywords: Code Anvil Mobile, Claude Agent SDK, Cloudflare tunnel, Google OAuth, internal SaaS, multi-user, Slack, 11 Labs, MCP, neural spark, knowledge base, SOP, AI agents, RLM, RAG, morning summary
summary: Scott demos Code Anvil Mobile, a lightweight mobile-forward UI built on Anthropic's Agent SDK that tunnels securely back to his local Claude Code instance via Cloudflare, allowing him to kick off coding tasks from his phone. He also discusses converting his personal AI assistant into a multi-user internal SaaS for clients, and shares early results from implementing Reverse Language Model (RLM) techniques to improve morning summary report quality.
-->

01:36:42 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Yeah. Well, just a note — I think I had talked about this, but the next three days I'm actually going to be finally doing it. I've been planning it where that neural spark thing that had the knowledge base and the Google tie-ins — I'm going to be adding Slack in there for that. For a couple of my clients, we're going to internal SaaS it because we're probably going to put more than just those two on it. So we'll actually create like a multi-user instead of trying to set this up individually.

01:37:26 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So right now I'm just planning everything because I'm going to be in there coding for the next three days in their office, kind of getting them set up because it needs to be easier now — they can create a user on the back end, and then when they log in from their team, they can connect their 11 Labs [tool:11 Labs] voice, they can connect their Google accounts, they can connect the Slack accounts. So it's not hard coded, like with me, because I'm just — you know, this whole thing was just built for me.

01:38:02 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
And the cool part about it was — the one thing I didn't think of was like, one guy is on an earlier version of this that just had the knowledge base. And I was like, wait a minute, if I'm going to turn this into an internal SaaS, and MCP [tool:MCP] is an anonymous connection by default — I came up with this way where they'll have a way they can generate like an MCP token that's just theirs for the database, that'll put them right where they need to be, so that's just a line I got to put in their MCP reference.

01:39:02 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I'm using the Agent SDK [tool:Anthropic Agent SDK] because I was like, look, I don't want to do full work for my phone, but I don't like their whole web desktop. I just don't like it.

01:39:29 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I just created this thing where I'm using the Agent SDK. It's real lightweight because it's just a UI front end that I secure with Google. It has a shared secret and it has an HTTPS Cloudflare [tool:Cloudflare] tunnel that goes back to it. And in my case, I have it on my iMac where it's legally using — because I'm actually invoking it. I'm still just coding in Claude Code with the Agent SDK. So it uses my Max plan.

01:41:27 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I was talking to Patrick the other day about this and I'm going to share my screen. I was like, I need to change the name because I'm sharing this as a public repo for people too. So I'm naming it Code Anvil Mobile [tool:Code Anvil Mobile], because I had it named Claude Code Mobile and I'm like, wait, I should probably — I'm going to get sued.

01:42:03 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So under start coding, I'm just trying to basically create a fun UI using Anthropic's official Agent SDK for as much of the functionality you can do through this. So like it even gives you terminal if you want straight terminal, which is kind of fun, but here's the chat. And so it's nice to have like the UI — if I put this in planning mode — it does have budget caps and turn limits, even though this doesn't use API, it's still kind of helpful if you want to have a long-running task.

01:43:20 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Like there it is — see, and then pops up the plan and this will scroll on your phone and everything. Yeah, so I mean, it's fun. It works really well. It's secure. So I'll send you guys this one now. I changed the name and everything. I will by tomorrow — the readme is up to date, but I haven't merged the latest.

01:57:47 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
That one update though — yeah, that one thing that you reminded me of was I haven't talked about how the RLM stuff's going, and what I've noticed so far doing the Reverse Language Model [tool:RLM] stuff. Now, obviously I haven't gotten to test it on the large RAG yet because that's me getting these guys into the internal SaaS. But I've already noticed just turning on RLM — which is like more how they were testing it in that paper I read — just using it in the morning summary report. Now it's actually getting smarter and looking for things. ▶ I noticed the quality of my morning summary reports got better in general about what it was telling me just by turning that on.

---

<!--SEGMENT
topic: Future of work, AI automation, and societal impact
speakers: Brandon Hancock, Patrick Chouinard, Ty Wells, Scott Rippey, elijah stambaugh
keywords: agent orchestration, SOP, industrial engineering, automation, AGI, Accelerando, transhumanism, SpaceX, data centers, B2B, wartime urgency, opportunity window, AI drug dealers, feedback loops
summary: A wide-ranging philosophical discussion about the near and long-term impact of AI on work and society. Patrick argues that reducing unit costs of work expands the total volume of work rather than eliminating it, making human orchestrators more valuable. Brandon frames the current moment as a once-in-a-generation opportunity window comparable to the internet and mobile revolutions, recommending the 2005 sci-fi novel Accelerando as a prescient roadmap.
-->

01:47:25 - Brandon Hancock
As time goes on, what we're going to start seeing is companies will have less people and as a result, they will have more processes.

01:47:56 - Brandon Hancock
I think companies will reduce size because if they're trying to maximize profits and they have a stable application, they will reduce headcount. And in replace of headcount, whoever was leading the team — let's say there was a sales team of 10 people — now they're going to have two, and the top two guys are going to do the work of 10. How do they achieve that? They're using agents. Well, what the hell are these agents doing? ▶ These agents are following SOPs, and they're acting on systems — their CRM, LinkedIn Sales Navigator — but they're doing things in a structured format, like an SDR would do, automatically.

01:50:47 - Patrick Chouinard
The thing is, for the company who are going to let people go in order to do that — they're going to lose what is going to become the hardest-to-replace resource. Because when you diminish the unit cost of a work item, you don't diminish the amount of work items — you increase the possibility you have, because you have situations or use cases you could not afford doing because they were not profitable before. Now that the unit cost of work has dropped, those use cases become profitable so you can do them, meaning you have twice the amount of use cases.

01:51:41 - Patrick Chouinard
And then the only people who can guide those agents properly, train them — they are going to be the scarce resource in a short amount of time. Because you're right, agents will start to do a lot of the job, meaning that people who have done the job manually are going to be scarcer and scarcer as we go along. So our value will increase because of that.

01:52:00 - Brandon Hancock
▶ I mean, what's going to happen is — at least how I foresee this — the single most valuable skill any of us can do right now is to become an agent orchestrator and an AI systems builder. Those are the two skills that you need to think about. On the system design, you need to be thinking like an industrial engineer, which is viewing things in bottlenecks, feedback loops, and systems. You have to analyze every process from that lens. And then once you can see it that way, then you come in as the agent orchestrator who's saying, here's how you tackle and decompose system one into steps.

01:53:35 - Ty Wells
The problem is you're going to have a problem training new junior resources to replace the senior that are going away, because there is no more junior work to be done because you've abstracted it in that scenario. So that's going to be the challenge of the next generation — figure out how do you train people on systems that the AI is trained instantly on.

01:56:22 - elijah stambaugh
▶ Seriously, if you get a chance this week, guys, read Accelerando [link:Accelerando by Charles Stross, 2005]. It is one of the best books describing exactly what Elijah is talking about, but they show exactly how it plays out.

02:05:16 - Brandon Hancock
▶ We are in wartime for before things just start getting automated and so crazy, but I know for the next year to two years, things are going to be in flux where I can still have a major impact as a human. All work done over the next two years is going to be worth 10x the amount of work that you do in five years from now. Like work done today is going to compound versus work done five years later because there's going to be 100x more people who can do the work. Right now, there's a very small 1%, 2% of the population that even understands what we're talking about on this call.

---

<!--SEGMENT
topic: Morgan's cemetery management SaaS demo and business strategy
speakers: Morgan Cook, Brandon Hancock, Ty Wells, Patrick Chouinard
keywords: cemetery management, D3.js, GIS, multi-tenant, Supabase, Vercel, Freedom of Information Act, FOIA, Utah, SOC 2, HIPAA, compliance, TinySeed, go-to-market, legacy software, government compliance, SaaS pricing
summary: Morgan demos a cemetery management system featuring D3.js hierarchy and radial tree visualizations of burial plot structures, public search, and a Freedom of Information Act compliance module specific to Utah state law. Brandon and Ty identify it as a high-value B2B SaaS opportunity targeting government-run cemeteries with legacy software, urgent compliance pain, and a repeatable multi-county go-to-market. Brandon urges immediate outreach and mentions TinySeed as a potential investor.
-->

02:21:10 - Morgan Cook
I do have one project that I'm working on heavily. It's a cemetery management system. And, you know, like you were just talking about with artifacts, these guys have a very specific government requirement — for anytime they release information, it has to be through their state's mode of basically like a Freedom of Information Act. And nothing's out there right now that supports that. So I'm going to put that together for them.

02:21:40 - Morgan Cook
One of the things I did was I used the D3 [tool:D3.js] diagramming, which is a library for visualization of layers.

02:22:29 - Morgan Cook
So this is the diagramming. This shows the structure of the cemetery, right? From the cemetery to — in this case, they have sections and rows and lots. And then the individual plots. And the plot color has — you can click to zoom back out, and then a radial tree — very similar structure, you have the cemetery, each of the sections, and as you drill into these, it's selective, there's too much information to show the entire tree in one diagram.

02:27:00 - Morgan Cook
The data is a single table with a parent-child relationship within the table. So you have multi-level parent-child relationship in the structure, all the way down to the plot. And that was the thing that's different — one cemetery may have sections, rows, lots, and plots. Another one might have only lots and plots or some other thing that they have in there. So it's all structured based on the data that they're used to seeing.

02:28:02 - Morgan Cook
And county to get it launched, right? Because they have a need for it right now and they're going to pay for it right now. After that, though — because it has this specific requirement that the state requires for any kind of information request — then all the other counties, any state or county-run cemetery, will be of interest in having the system.

02:29:27 - Brandon Hancock
▶ The day and age of AI being the system of record is a huge moat. Because if you're just a wrapper around ChatGPT and there's no — why are they going to stick with you even if AI changes or gets cheaper or a competitor comes around? Like, if there's a better wrapper, you're gone. But if there's a huge system of record change, well, it's going to be a pain in the butt to go from record to record. So they stick.

02:30:26 - Brandon Hancock
▶ Second, there's a bunch of law changes. Any time a law changes or requires some complexity and you can twist the knife of being like, hey, this law goes into effect, but your current app is going to get you fined or you're going to have to hire two more people to just manually sit around all day and do this for you — or you can just click the easy button and I have a subscription, $2,000 a month, whatever the number is, and I'll just do it for you.

02:37:33 - Brandon Hancock
<Q>When does the law go into effect? How long?</Q>

02:37:34 - Morgan Cook
<A>It's in effect. It's already in effect and they're struggling.</A>

02:37:38 - Brandon Hancock
<Q>Are they getting fined actively?</Q>

02:37:41 - Morgan Cook
<A>No, because what they're doing right now is not giving any information out.</A>

02:38:07 - Brandon Hancock
▶ If I was you, I mean, final thing — this is a full-blown painkiller, like they're screaming in agony, because they're under the thumb of the law. So this is the perfect product, under the perfect circumstances, and now it's just like, seriously Morgan, don't sleep. Build this as quickly as possible, and advertise like hell. Your go-to-market strategy over the next month — seriously, this is a month sprint that could seriously change the trajectory of your life.

02:45:10 - Brandon Hancock
You're going to pay $600 a month to get the Supabase [tool:Supabase] instance that's HIPAA and SOC 2 compliant. You're going to pay the $100 static fee for Vercel [tool:Vercel] to get a static IP. Like, it's not an insane amount of money, but it's going to be more expensive. But the playbook's there.

02:49:30 - Brandon Hancock
▶ As soon as dollars trade hands, please let me know — and really, like, either TinySeed [tool:TinySeed] or something like that — money was given, and it has been an absolute lifesaver for us. And if I build fast enough, I'm going to get more contracts, and it'll just instantly replenish. So I would be very happy to introduce you, just because this is the exact type of business that every investor wants to invest in.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not supplied in this session):

- **Jaylen.Davis** — passed through unchanged
- **Rag Ch** — passed through unchanged
- **elijah stambaugh** — passed through unchanged
- **Ryan - One Stop Creative Agency** — passed through unchanged
- **Darryl Goldstein** — passed through unchanged
- **Juan Torres** — passed through unchanged
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** — passed through unchanged
- **Morgan Cook** — passed through unchanged
- **Paul Miller** — passed through unchanged
- **Ty Wells** — passed through unchanged
- **Brandon Hancock** — passed through unchanged
- **Marc Juretus** — passed through unchanged
- **Patrick Chouinard** — passed through unchanged

*(No SPEAKER_ALIASES map was provided in the `{{ $('HTTP Request: Get Speaker Aliases').item.json.data }}` context block — all names were passed through as-is.)*