=== SESSION ===
date: Unknown (references "2026" as current year)
duration_estimate: ~2 hours 50 minutes
main_themes: OpenClaw agent security and deployment, AI-assisted development workflows, member project demos (fitness app, creator monetization platform, cemetery management SaaS, mobile Claude Code interface), AI tool comparisons (Claude Code vs. Codex vs. Gemini), formal AI verification/testing, business model strategy, future of AI and agent orchestration

---

<!--SEGMENT
topic: Pre-call chatter and personal projects
speakers: Marc Juretus, Patrick Chouinard
keywords: mobile app, Apple App Store, personal website, CV portfolio, fitness app, OpenClaw, static site, CMS, Hostinger, real estate site, N8N, Google Sheets
summary: Marc and Patrick chat before the main call begins, discussing mobile app deployment friction with Apple, Patrick's personal website revamp to showcase his CV interactively, and Marc's fitness tracking app built with OpenClaw that has reached near-releasable quality. They also touch on Marc's real estate site prototype and the question of whether N8N is still needed given Claude's expanding capabilities.
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
My fitness app went a lot faster and that stock school app I had — it's to a point, the code that it writes, that Stanford fitness app, I could give it to somebody right now.

00:03:36 - Marc Juretus
I can honestly go in now and I can pull up someone who has a login and I can assign their active workout and then I can view their log.

00:03:46 - Marc Juretus
And like I keep talking to OpenClaw [tool:OpenClaw] and it's like, you're at a point you should be able to try to have a soft release of this.

00:03:54 - Marc Juretus
I'm like, yeah, that wasn't my objective, but it's very helpful.

00:04:00 - Patrick Chouinard
When you're giving it, like, you know, what you're trying to work on.

00:04:05 - Patrick Chouinard
But I'd be interested in looking at that because I'm starting at a new gym, actually, this week.

00:04:11 - Marc Juretus
Yeah, it's pretty slick. The thing that I like the most is I have this thing where you dictate workout. So you can go in and log what you did one by one. But you can click dictate workout and say 30, and it'll map up. Say you're doing triceps — skull crushers and this — and it logged them. And I was like, holy cow, man.

00:04:44 - Patrick Chouinard
Actually, what I would need is something with vision because the problem I have is the old gym I was going to was a little family gym, like very, very small and mostly dumbbells and free weights. Now I'm going to a more commercial gym, and my biggest problem is to know how or what to do with each of the new machines, because there's like 20, 30 machines in there that I have no clue how to use.

00:05:16 - Patrick Chouinard
▶ So I'd like something where I could just take a picture of the machine and it tells me what exercises I could do on that thing.

00:05:23 - Marc Juretus
Well, you know, like the few people I do train, I say start out with three days a week if you're able to do that.

00:05:30 - Patrick Chouinard
That's what I say — do push, pull, and legs.

00:05:33 - Marc Juretus
So, you know, push will be like chest, triceps, shoulders.

00:05:40 - Patrick Chouinard
My challenge is I don't know what machine does what in the new gym.

00:05:43 - Marc Juretus
Oh, well, if you go in there, I have video demos of it. I'll send you the link.

00:07:00 - Patrick Chouinard
Against, like, what I call Instagram girls that just go there to film themselves instead of actually training.

00:07:07 - Marc Juretus
That's why I have a pretty full gym in my house right now, man.

00:03:01 - Patrick Chouinard
Right now, there's just two sites that I decided were quality enough to showcase.

00:10:26 - Marc Juretus
But it's funny — like, what is your mindset on that now? Because the guy that I took the long course with for six months, I was just watching a video of his he just put out and he was discussing, do you even need N8N [tool:N8N] now with what Claude's doing? So that's the latest thing.

00:10:43 - Marc Juretus
He said, as of now, you do because there's very complex flows. But not only about complex flows, it's about the fact that N8N run on a local VM costs you zero compared to Claude who costs you tokens every single time.

---

<!--SEGMENT
topic: Anthropic Security launch and patent discussion
speakers: Patrick Chouinard, Ty Wells, Marc Juretus
keywords: Anthropic Security, provisional patent, Lucid Dev, Usai, end-user applications, market disruption, stock impact, AI security, announcement
summary: Patrick raises Anthropic's launch of Anthropic Security, prompting Ty to discuss how large AI companies can disrupt smaller end-user application businesses with a single announcement. Ty shares that he holds a provisional patent on his own work in a related space and that the competitive landscape has shifted significantly within a week.
-->

00:08:05 - Patrick Chouinard
<Q>Hey, Ty, did you see that Anthropic has started Anthropic Security [tool:Anthropic Security]?</Q>

00:08:13 - Ty Wells
<A>When I saw that, I thought about you right away. Yeah, I saw that. I'm like, this is why I'm trying to get away from end-user application stuff, because these guys will just — they can knock you out in a glancing blow. They don't even have to touch you, right? I mean, they're dropping stocks like crazy just from an announcement. So, yeah, that's going to be problematic long-term.</A>

00:08:43 - Patrick Chouinard
Well, if you have a patent for it, you could probably negotiate a pretty sweet deal if they're going into the same arena that you are.

00:08:52 - Ty Wells
Yeah, yeah, yeah. I do have a provisional patent on my stuff. But I'm actually — yeah. Here's the funny thing about it. That was a week ago. This week is a whole different story. But yes, I have a patent that I feel pretty confident in.

00:09:36 - Marc Juretus
Yeah, I was telling him I've been doing kind of like you guys all the weekend and night stuff. I think I'm going to take that Google Generative AI Leader course [tool:Google Generative AI Leader certification]. Not that it's going to add a lot to me, but I can actually — it looks like something on a resume, you know, is the only reason.

00:09:55 - Patrick Chouinard
▶ Yeah, then you can use the course to build a resume site like I did last weekend.

---

<!--SEGMENT
topic: Brandon's return and AI productivity setup
speakers: Brandon Hancock, Patrick Chouinard, Marc Juretus, Ty Wells
keywords: MetaQuest 3, Claude Code, Codex, Gemini, PowerPoint generation, Meta VR headset, parallel agents, pitch decks, Google Ads, OpenClaw, productivity
summary: Brandon returns to the group after a period away and shares his current AI-powered workflow, including using a Meta Quest 3 headset to run 15 simultaneous Claude Code instances. He highlights Codex as his top tool for generating large PowerPoint presentations and announces an upcoming Google Ads coaching series with a former Google employee named Peter.
-->

00:14:22 - Brandon Hancock
What's up, everybody? Sorry, I got beanie hair.

00:14:34 - Brandon Hancock
I'm pumped to see all these familiar faces, give you all the updates.

00:15:25 - Brandon Hancock
All right, guys. I've gone deep in AI. I'm just now coming out. My favorite new gadget that I have to show you guys is — I got this. It's the Meta Quest 3 [tool:Meta Quest 3], basically. So what I do is I hook it up to my Mac, and I have like 15 Claude Code [tool:Claude Code] instances at the same time on like a projector in front of me, as big as I can see. And I'm doing the work of an entire company myself. It's crazy. I have marketing. I have sales out.

00:18:01 - Brandon Hancock
Most Helpful Win. Codex [tool:Codex], obviously, for all things related to code, still my favorite. Cool recommendation — I have been having to work a ton recently on creating PowerPoints for pitch decks, presentations, education content, like all sorts of stuff.

00:18:16 - Brandon Hancock
▶ Codex is by far the best PowerPoint maker I've ever dealt with. I will kick it off and it will make a 90-slide presentation for me in 30 minutes. And then I just iterate from there.

00:18:31 - Brandon Hancock
But Claude Code — under no circumstance could I ever get it to do well at more than like 20 slides, and even then it would struggle. But Codex — it will, just to give you guys a heads up, because I want you guys to try it if you have to make presentations — you hook it up to Gemini [tool:Gemini] so it can make images, and then you just say go forth, here's a brain dump, go make PowerPoint slides, and it will make custom images, fit them in the PowerPoint, because Codex is very precise, it'll test to make sure it's formatted well, do it again and again and again.

00:19:00 - Brandon Hancock
▶ Every week, probably close to 200 PowerPoint slides for different things I have to do, and Codex is doing all of it. So, yeah, if you're doing a pitch, Codex is the game changer.

00:19:18 - Brandon Hancock
Final thing, just coming up for what you guys can expect soon. We are hiring an ads coach for our company. His name's Peter. Awesome guy. Used to work at Google. And we're going to do like a four-week, six-week program with him where he's going to help us redo our ads. And we're just going to be sharing all of that on YouTube. So, if you kind of wanted to see behind the scenes of like, oh, cool, I have a software idea. And now I want to get traffic. How do I actually do that with Google Ads [tool:Google Ads] in 2026? This will probably be the video.

---

<!--SEGMENT
topic: Patrick's AI-powered CV and CMS portfolio site
speakers: Patrick Chouinard, Brandon Hancock
keywords: Claude Sonnet, CMS, Hostinger, CloudFlare, GitHub, OpenClaw, JSON, bilingual content, admin dashboard, career portfolio, CV automation
summary: Patrick demos his personal portfolio website, which uses a custom-built CMS admin dashboard to manage career history and push updates automatically to Hostinger via Claude Code. A key feature uses Claude Sonnet to parse loosely written job notes and rewrite them in structured JSON in both French and English natively. Patrick also describes treating OpenClaw as a managed worker with its own GitHub account within a shared organization.
-->

00:24:00 - Patrick Chouinard
At length in the last couple of weeks on that specific subject, but yeah, so the idea is main site. But what I really love about that site — this is the public site. This is what's pushed to Hostinger [tool:Hostinger] automatically by Claude Code.

00:24:20 - Brandon Hancock
Oh, really?

00:24:20 - Patrick Chouinard
Behind the scene, I have an admin dashboard that allows me to manage all the eras I split my career into, all of the engagements, the technology, the skill, the narrative, everything here — I can update and push to the website.

00:24:40 - Patrick Chouinard
▶ Basically, I created my own CMS system.

00:24:44 - Patrick Chouinard
And on top of that, when I create a new engagement — that's the part I always say documented my job experience. So now I have "create with AI." I just grab — let's say I have a little fake one I created just as a demo — it's very loose, like I worked for that one from around September, very vague, nothing structured whatsoever, just explaining what I did.

00:25:17 - Patrick Chouinard
Then it's Claude Sonnet [tool:Claude Sonnet] behind the scene that rewrites the whole thing, and it will submit the rewrite in JSON in order to fill all of this — the form — so not only the job description, but like the employer name, the client, the project — it extracts everything, writes in both French and English as a native speaker, so it's not writing in one and translating, it's actually writing both in a native way.

00:28:00 - Patrick Chouinard
That I created for OpenClaw. So OpenClaw has its own GitHub [tool:GitHub] account. I have mine, and we share an organization. So everything it develops, it develops in that organization.

00:28:10 - Patrick Chouinard
▶ I really manage security exactly as if it was a human worker.

00:28:14 - Brandon Hancock
Yeah, that's awesome.

---

<!--SEGMENT
topic: OpenClaw security and deployment strategies
speakers: Brandon Hancock, Patrick Chouinard, Darryl Goldstein, Juan Torres
keywords: OpenClaw, prompt injection, Gmail, Google Drive, Discord, Proxmox, Ubuntu VM, Docker, Slack, Appify, LinkedIn, email isolation, calendar, security sandboxing
summary: The group compares approaches to deploying OpenClaw securely. Patrick describes a hardened setup with a dedicated Ubuntu VM on Proxmox, isolated Gmail (read-only from his address), a separate calendar, and Discord for context-segmented communication. Brandon shares his simpler approach of limiting OpenClaw to a single Slack channel and Google Drive writes only. Juan raises questions about AWS VPC isolation, and Darryl asks about running on a Mac Mini.
-->

00:28:15 - Brandon Hancock
Real fast, guys, I just want to share what I'm doing with OpenClaw. Just maybe it'll strike a conversation.

00:28:22 - Brandon Hancock
Patrick is definitely going down to like 10 out of 10 most secure. I probably should be doing what Patrick's doing. We all should probably do what Patrick's doing, to be honest.

00:28:32 - Brandon Hancock
My poor man, lazy way — what I'm doing right now is I just have it only accessible to Slack [tool:Slack], and I'm only feeding it information. Like it's being fed the information I want it to have access to, and it can't do anything else. Like it doesn't have access to email, it doesn't have a WhatsApp, it has nothing else. All it has access to is an individual Slack channel.

00:29:03 - Brandon Hancock
So that's my poor man way about making sure it doesn't do anything crazy. <Q>Could it go absolutely bonkers, though, if it goes to a website that has some prompt injection stuff?</Q>

00:29:14 - Brandon Hancock
Maybe. But that's how I'm doing it to automate a lot of customer research and outreach. I just have it hooked up to Appify [tool:Appify] with LinkedIn browse features. So anytime someone tries something out, we can quickly just do a sit-rep on who they are, what department they probably work for, and who's their boss, and gives us a report.

00:29:50 - Patrick Chouinard
It's not, but if I had to say one thing — I did give mine an email, but it has its own, and I gave it one rule.

00:30:00 - Patrick Chouinard
▶ It only reads email coming from my email address. Anything else, it tells me there's an email, but it doesn't read it.

00:30:06 - Brandon Hancock
Oh, okay.

00:30:07 - Patrick Chouinard
▶ That way, I'm avoiding the prompt injection. It has its own calendar. So instead of playing with my calendar, it actually creates the meeting itself, and then it invites me.

00:30:23 - Patrick Chouinard
It has its own machine dedicated with nothing else on it. It has its own Gmail [tool:Gmail] and Google Docs [tool:Google Docs]. So since it has Google Drive [tool:Google Drive], that's where I put all the documentation it can interact with.

00:30:37 - Patrick Chouinard
▶ Try interacting with Discord [tool:Discord], because with Discord you can very easily create multiple channels and split your context by channel, so you don't overwhelm the context window and start getting enormous amounts of money in tokens because you send 20,000 in every exchange.

00:31:04 - Darryl Goldstein
<Q>Are you running on a Mac Mini? What are you using to run?</Q>

00:31:09 - Patrick Chouinard
<A>It's a Ubuntu VM running on Proxmox [tool:Proxmox].</A>

00:31:17 - Brandon Hancock
I did, real fast, buy a Mac Mini [tool:Mac Mini]. I have yet to do anything with it, but the plan is to put OpenClaw on it. It's completely overkill, but I just wanted to do it.

00:31:37 - Juan Torres
<Q>Yeah, I don't know, Patrick or Brandon, what you would recommend, but I've thought of doing that for an EC2 instance, just have its own VPC, its own virtual private cloud with its own security permissions, just to be able to handle the network. But when I give it resources, like a database instance, then I'm afraid that it's going to erase it. So how do you regularize the relationship between OpenClaw and the resources within your VPC?</Q>

00:32:25 - Patrick Chouinard
<A>If you can put a VM somewhere — and even Docker Desktop, that's all it needs. Isolation. It doesn't need resources. So I really don't get why everybody is going and putting that on a VPS or having a monthly fee to run it. It runs on hardware.</A>

00:32:50 - Brandon Hancock
Patrick is thinking about this logically. I definitely got fanboyed into a Mac. I just got excited.

00:33:10 - Brandon Hancock
I have it running in Docker [tool:Docker] on my computer. It's just a pain because my co-founder — if my computer turns off, he's talking to OpenClaw and he's like, damn it, why is it not working? And it's because my computer is asleep. So that's why we're going to get an external device.

00:33:25 - Brandon Hancock
Juan, to answer your question — I am trying to limit the exposure of what it can do. Mine is: you consume what I give you, and you can write to a Google Drive. There's no escaping the box that I have built it in.

00:34:00 - Brandon Hancock
▶ I almost just want to have — I don't want OpenClaw to have the ability to send an email. We have it doing so much customer research. My biggest fear is it goes, well, I'll just be a little bit more proactive, and I'll just write the email. And then all of a sudden, it's blasting 500 clients garbage.

00:34:35 - Brandon Hancock
▶ There needs to be a clear box that it can't get out of, and you want to peek in when you need something and feed it only what it needs and nothing else.

---

<!--SEGMENT
topic: Jaylen's creator monetization platform demo
speakers: Jaylen.Davis, Brandon Hancock, Darryl Goldstein, Ryan - One Stop Creative Agency
keywords: content creator platform, video monetization, fan funding, YouTube, TikTok, Instagram, subscription model, Cameo-style video, community, topic voting, revenue model
summary: Jaylen demos his web app that lets content creators monetize fan video requests — fans fund a requested video, and the creator earns 90% upon delivery. Brandon suggests pivoting toward a subscription community model (similar to School) for recurring revenue, and Darryl proposes adding in-app video recording so non-technical creators (like athletes) can fulfill requests without external tools.
-->

00:36:19 - Jaylen.Davis
Okay, so yeah, basically, I came on maybe back in October or November. Mitch McCauley, he actually sent me the link. And since then, I've developed my web app tremendously. Let me share my screen.

00:36:56 - Jaylen.Davis
Yeah, basically, and since then, we've pivoted to not only — we help YouTubers. We also work with Instagrammers and TikTokers [tool:TikTok]. Basically, it's just for those who might not know, it's just a platform where a content creator can monetize their video requests. So you can basically tell your fans, look, if you want me to make this particular video, I'll do it for this price. Once they fund it, you make the video and then you get paid 90%.

00:37:33 - Jaylen.Davis
So if someone asks Brandon to make a video about something, and let's say his price was $100, they put in the $100, he makes the video and then he receives $90. It's as simple as that. Yeah, so far we have about 11 people on the platform. We're making progress and I just wanted to get any feedback on any possible ideas.

00:38:07 - Brandon Hancock
One quick thing — the second I saw your face hop on the call, I was like, oh, I have ideas. So, I think my main thing that I've always thought would be cool is for people to vote and downvote on ideas and me pay you a monthly subscription, 50 bucks a month.

00:38:28 - Brandon Hancock
▶ I mean, that's because then it's recurring revenue and you're not at the mercy of customers. Like, it's consistent.

00:38:35 - Brandon Hancock
You know, $50 a month and you built me a school where my YouTube members can come in, chat about my videos, and request future videos. Like, basically, be the blog of what YouTube is. Be the school. Turn every YouTube channel into a school community automatically.

00:39:00 - Brandon Hancock
And then just tell the creator, hey, you pay me 50 bucks, 75 bucks, 99 bucks a month, and I will give you access to run this community.

00:45:24 - Darryl Goldstein
<Q>So, is there a feature here where you could capture that video right from your app, as if it's on a YouTube-type video, meaning that the person making the video for you — just make it real simple — they can come on here and say, hey, Darryl, happy birthday to your mother, have a great day, and they don't have to produce anything. Capture it right here through a recording on your app, and boom, it's done.</Q>

00:46:14 - Jaylen.Davis
<A>I get what you're saying. No, we currently don't have that feature. I believe Vimeo [tool:Vimeo] has something like that where you can basically just request a quick video from a celebrity.</A>

00:46:29 - Darryl Goldstein
You have to solve the technical part, but I'm talking about functions. Feature-wise, it might make it easy for people that are paying — for the person who has to create the video. Maybe they're not a content creator necessarily. They don't know how to set up everything, but they can come here right with the camera.

00:47:01 - Jaylen.Davis
Okay, I appreciate that.

00:47:05 - Brandon Hancock
▶ Main thing is just seriously — who's actively trying, where's the friction already at? Like who's trying to give away money and why can't they give it to these YouTubers? And you're going to find it's usually mostly businesses.

---

<!--SEGMENT
topic: Marc's fitness and stock school app demos
speakers: Marc Juretus, Brandon Hancock
keywords: fitness app, workout logging, voice dictation, exercise library, Grok, AI trainer, stock school app, paper trading, Vertex AI, RAG, Model Garden, Google Cloud, Google Generative AI certification
summary: Marc demos his fitness tracking app featuring voice-dictated workout logging, an AI personal trainer with access to workout history, and AI-generated exercise demo videos made with Grok. He also shows a stock school app with paper trading and an AI trading coach. Brandon recommends Gemini for cost-effective token usage and highlights Claude Code's subsidized pricing. Marc also discusses plans to take the Google Generative AI certification exam.
-->

00:47:26 - Brandon Hancock
Mark, what is going on, man?

00:47:53 - Marc Juretus
So, what have I been working on? I know you guys were talking about OpenClaw. I have one. I have it on a Google virtual machine up in the cloud, running Ubuntu 22.04. What I have it doing is I talk to it in Telegram [tool:Telegram], and say I'm out at a bar or something. I can talk to command, email trainer, their name, their email. It'll send a pre-formatted email addressed to them — the basic foundation of how I work out — but it taps into my calendar and shows my availability dates.

00:48:29 - Marc Juretus
Another one is I'm trying to get my son a job, and I have another one. I have it pull in a job service API, gets Indeed [tool:Indeed] and a couple others, but if I type "get jobs, whatever category," say laborer and then email, it'll email any available job listings to his email address or whoever I put in for email.

00:48:52 - Marc Juretus
And I have it for a daily motivator, but I had to drop that down to Haiku [tool:Claude Haiku], man. It was starting to run me some dough. I was like, yeah, don't leave it on Opus [tool:Claude Opus].

00:49:00 - Brandon Hancock
▶ What I recommend for applications where people use them — Gemini [tool:Gemini]. Gemini is the best bang for buck on capability and cost, at least that I've seen right now.

00:49:27 - Brandon Hancock
I mean, they just — Claude Code spoiled us. I don't know if you saw the report. They're subsidizing it — it was either 17 or 14x. So we pay $200 and they cost, I think it was like $2,800. So it's crazy how much they're eating for us to use their platform right now.

00:49:55 - Brandon Hancock
▶ You are getting God-level capabilities for pennies. And even though it doesn't feel like pennies, because $200 is not nothing — it should be, for what we're getting, and they're just eating it to get us addicted. They're all AI drug dealers.

00:50:23 - Marc Juretus
But anyways, I'm going to try — I'm going to probably take the Google Generative AI exam. So I've been up on the cloud. I spun up a RAG on Vertex AI [tool:Vertex AI], it spun up a clothing site that has a chat, and then I used the image gen from Model Garden [tool:Model Garden] to generate images in the admin pool for that, just so I kind of get a feel of that.

00:51:05 - Marc Juretus
I do have the fitness site. I actually think — I may start using it, because this Claude has gotten to the point where it's writing code that's just ridiculous, man.

00:53:43 - Marc Juretus
Can you see my screen? Yeah, so basically that's a site. I have a couple of different aspects to it. Like when I work out at 5am in the morning, I went ahead — like I'm doing triceps and chest — and I'm like, just pull up three random of each, so it'll go in there, it'll give me three random exercises in the basic summary of what they are.

00:54:28 - Marc Juretus
I have an exercise library that's basically all of my exercises. And I don't know how far I'll take it, Brandon, but I do have — I was showing these cats on here before — I have tricep pushdowns, so I made a video on Grok [tool:Grok] — that's not even me — of working out.

00:55:40 - Marc Juretus
And then the one thing is I actually have a trainer in there. If you say "I need a shoulder workout," it actually has access to your history and sees what you did. It says, hey man, your shoulders look like crap because you've only been doing this, that, or the other.

00:56:27 - Marc Juretus
Here's the one that blew me away the most. I have a button called "summarize workout." And when you click on the button — instead of you going in here and manually adding — I actually give you the ability to just click on the button, summarize workout. And I tested it. I would say, hey, I did three sets, tricep pulldowns for 50. And I did three sets of skull crushers for 50. It'll actually log them and go on your history and parse them out to separate exercises that I have in my database.

00:57:16 - Marc Juretus
And then I got a stock school app too, where you go in and if you take three tutorials, I give you $25,000 in paper money. It tracks it. And then I actually have a trading coach that'll go in there and say, hey, man, you went a little too heavy in tech.

00:58:00 - Marc Juretus
This is what I was telling you about for the RAG — this is going to Google Gemini, this has a RAG client, and then it has Creative Studio, where I can say I want to generate an image for running shoes, because I sell shoes. This goes up to Model Garden in Google Cloud, and it'll actually generate me an image from their Model Garden model.

00:58:32 - Brandon Hancock
▶ Dude, look at you needing a certification — you're cranking out apps left and right, dude. Poo-poo the certification, man, you got this in the bag.

---

<!--SEGMENT
topic: Ty's formal AI verification system and autonomous agents
speakers: Ty Wells, Brandon Hancock
keywords: formal verification, AI hallucination, AGI, autonomous agents, GitHub Actions, regression testing, Usai, provisional patent, Claude Code, non-deterministic testing, Cypress, unit testing
summary: Ty presents his project Usai (formerly Lucid Dev), a formal verification layer for AI output that acts as a "spell check for logic" to catch hallucinations. He describes using GitHub Actions to auto-verify code and extending this into a framework for long-running autonomous agents with persistent memory. Brandon connects this to his own pain point of regression testing non-deterministic AI applications, and they agree to connect offline to discuss further.
-->

00:05:02 - Ty Wells
Okay, so basically what I'm doing here is creating a formal verification layer for all AI output because we know AI models hallucinate, right? 30 to 40%, all depends — how deep the context window is. Basically, it is a spell check for logic that's coming out of the model.

00:06:30 - Ty Wells
So I did this paper basically to discuss how this is actually implemented. And I was reaching out to publish it on the archive. I did put a provisional patent on what I built.

00:07:10 - Brandon Hancock
So a few things. Can I actually tell you my biggest problem that I'm running into right now?

00:07:17 - Brandon Hancock
The thing that I want to focus on is help with testing with AI — meaning there's unit tests, cool, like I understand this function, here's the 200 ways we could use this function, here's the inputs, outputs, cool. Unit test makes sense. Then you keep going up the stack and then there's end-to-end testing, which at this point you pretty much use Cypress [tool:Cypress].

00:07:58 - Brandon Hancock
But now that things are different, it's very hard — with AI, especially if you're building an entire application around AI, it's very non-deterministic by default. So it's like, I almost want to have at the same time 30 different users for every archetype that could happen.

00:08:38 - Brandon Hancock
▶ Because now that I'm getting more into production, that's the biggest issue I'm running into — I can crank out code like there's no tomorrow. But it's like, oh crap, did I break something that I built six weeks ago?

00:09:10 - Ty Wells
<A>So to answer your question, yes, that was one of my biggest issues too, right? The regression testing is just crazy. So you wanted that to happen automatically. And this does that through GitHub Actions [tool:GitHub Actions] where it verifies the code that's in there automatically. It runs it and tries to verify that code.</A>

00:09:43 - Ty Wells
So what I did was I took it a step further and wanted to try to reach AGI, right? Meaning if I have better code coming out — because AGI itself is code. And so I use my verification process to create the things that make up AGI and I'm just testing it.

00:10:13 - Ty Wells
So I created — and I started this before OpenClaw — but it's basically the ability I've been trying to achieve: long-running autonomous agents that have memory that persist and so forth. I built that using this as a verification process of the different agents to do that.

00:11:40 - Ty Wells
It's going through all of the steps, marking all the claims — what this is supposed to do is actually doing what it's supposed to do — verifying those claims and fixing anything that fails the test. Here it's running functional tests. That's been running for 20-some minutes. But it's doing all of that — making decisions, using tools or creating tools as it needs them.

00:12:15 - Brandon Hancock
I like the way you're thinking about this because — I mean, yeah. How do we just make stuff reliable? I mean, you're hitting a very cool part of a new problem that was just introduced to society, which we're all facing. I mean, if you look at the chat, it's everyone can spit out more code than they can handle at this point. And now it's just like, shoot, does it actually work?

00:12:52 - Brandon Hancock
▶ There's a difference from way back in the day: does the code compile — AKA, is it syntactically correct? Yes, it builds. But is it semantically or behaviorally doing what I want it to do? No, not always. So I think that's where you're coming in at that second layer too, which is awesome.

00:12:58 - Ty Wells
Yeah. And I'd love to talk to you offline. Friday would probably be the best.

---

<!--SEGMENT
topic: Python vs TypeScript for AI backends and Claude Code workflow
speakers: Brandon Hancock, Patrick Chouinard, Rag Ch, Morgan Cook, elijah stambaugh
keywords: Python, TypeScript, FastAPI, Flask, Dockling, RAG, Claude Code, Codex, Warp terminal, cursor, anti-gravity, parallel instances, editor setup, tmux, Claude Code agent teams
summary: Brandon answers a question about Python vs TypeScript for AI backends, recommending Python for AI-specific tasks due to library maturity (e.g., Dockling for RAG). He then demonstrates his Claude Code multi-instance workflow using Warp terminal instead of the built-in editor, showing how to maximize parallel coding throughput. Morgan shares a key insight that AI writes functions better than it executes prompts directly. Elijah mentions Claude Code agent teams running in tmux.
-->

00:14:15 - Brandon Hancock
So Elena was asking, <Q>do you think there's a difference between building a backend for GenAI on TypeScript versus Python, any benefits to one versus the other?</Q>

00:14:35 - Brandon Hancock
<A>So I prefer at this point, if I'm going to do anything related to AI, I like using Python. And I'll tell you why. It's because Python is leading the front on AI. For example, working with a client on a project, I love Dockling [tool:Dockling]. Dockling is one of my favorite embedding and chunking tools out there for building RAG applications. And it's native to Python.</A>

00:14:56 - Brandon Hancock
And we're like, but they want to do everything in TypeScript. So as a result, I was like, oh, there's a Dockling TS package. It's fake. All it does is it's a pointer to a version of you running Python somewhere else. So it's just a wrapper to shoot to a Python server somewhere else.

00:15:23 - Brandon Hancock
▶ So it's like, man, at the end of the day, it's just a necessary evil of knowing two languages — TypeScript for all front-end and back-end, and then when it comes to AI-specific tasks, hey, I just need to know a little bit of Python.

00:15:51 - Brandon Hancock
▶ Just knowing the three or four words to make you dangerous to build a modern Python application — Fast API [tool:FastAPI] or Flask [tool:Flask]. So just knowing the three or four words to make you dangerous.

01:17:01 - Morgan Cook
And it struggled for like five minutes before it came back with a response, and it gave me a JSON file, which I then dropped into my map viewer, and it was horrible. And all I did to fix it was say, make me a JavaScript function that does this exact prompt I just gave you. And it made the function, and the function works perfectly.

01:17:34 - Morgan Cook
▶ So what I got out of that was the AIs know how to write functions and programs really well. They don't know how to implement them internally themselves, right? He can't run the iteration to create all the points on the plots and have the accurate output, but he can make a function that does it.

01:17:50 - Morgan Cook
▶ So if you're struggling to have AI create the proper structured document or whatever, have it make a function to do it, because it will create a beautiful function to make that happen.

01:18:21 - Brandon Hancock
Real fast, to add on — when it comes to long-running jobs, if I know something's going to take 20 minutes of just iteration, iteration, iteration — Codex. I am falling in love with Codex for tasks that I just — high-precision tasks. Like, hey, it has to be precise. I don't care how long it takes. I just want it to work after 20 minutes of you doing your thing.

00:19:57 - Brandon Hancock
▶ You get to go so far on the $20 a month plan — it is wild what they're throwing in on Codex nowadays.

01:20:32 - Rag Ch
<Q>So, what I'm doing is I just type here in the Claude Code terminal, and that's what I do. But I have seen — you seem to be typing here and then getting the commands and all that. So I just wanted to see what I need.</Q>

01:22:53 - Brandon Hancock
<A>So that's the first mistake. Don't use the Claude Code terminal. That's mistake one. You're just using a regular terminal. It doesn't have as many features, and that's why we don't use it.</A>

01:25:07 - Brandon Hancock
I'm using Warp [tool:Warp] to do everything. And I just have a script to tell Warp, like, hey, I'm ready to start working again. And it just opens up six modules, eight modules in a nice window format. And then anytime I want to actually go look at a file, I basically just off to the side have cursor [tool:Cursor] opened just to look at a file, but I'm not in the editor anymore — I've left the editor behind.

00:26:34 - Brandon Hancock
▶ Always eliminate friction. That's our job, guys. Eliminate friction, talk to AI as fast as you can.

01:31:29 - elijah stambaugh
You might have seen that Claude Code has agent teams, and to run them and see all the different agents running, you run it in iTerm2 [tool:iTerm2] and run tmux [tool:tmux] in there. So I don't know if you're familiar with that, but is that the CLI tool that you're using?

01:33:41 - elijah stambaugh
I will say that the agent teams are pretty freaking amazing, the way that they work. So just seeing that in tmux when they run — and I agree that it's not very good navigation, unfortunately.

01:34:11 - elijah stambaugh
I saw a podcast with Peter Steinberger, the Claude Code guy, and he said he had like 15 or 20 running at the same time. He had seven Claude Code Max subscriptions, like, over the past six months. He had said he had seven Max subscriptions running and all of that running at the same time.

01:34:39 - Brandon Hancock
▶ You could buy three huge curved monitors or just buy the Metas, and you'd save money buying this, and you could work in your living room anywhere.

---

<!--SEGMENT
topic: Scott's mobile Claude Code interface and SOP system concept
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Brandon Hancock, Patrick Chouinard
keywords: Code Anvil Mobile, Claude Agent SDK, Cloudflare tunnel, Google OAuth, MCP, internal SaaS, neural spark, Slack, 11 Labs, RLM, RAG, SOP system, agent orchestration, knowledge base
summary: Scott demos Code Anvil Mobile (formerly Claude Code Mobile), a lightweight mobile-forward UI built on Anthropic's Agent SDK that tunnels securely back to his local machine via Cloudflare, allowing him to interact with Claude Code from his phone. He also discusses converting a personal knowledge-base tool into a multi-user internal SaaS for clients, and the group has a broader discussion about SOP systems as critical infrastructure for AI agents and the future of work.
-->

01:36:47 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Yeah. Well, just a note — the next three days I'm actually going to be finally doing it. I've been planning it where that neural spark thing that had the knowledge base and the Google tie-ins — I'm going to be adding Slack in there for that. For a couple of my clients, we're going to internal SaaS it because we're probably going to put more than just those two on it. So we'll actually create like a multi-user instead of trying to set this up individually.

01:37:26 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So right now I'm just planning everything because I'm going to be in there coding for the next three days in their office, kind of getting them set up because it needs to be easier now — they can create a user on the back end, and then when they log in from their team, they can connect their 11 Labs [tool:11 Labs] voice, connect their Google accounts, connect the Slack accounts.

01:39:02 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I'm using the Agent SDK [tool:Anthropic Agent SDK] because I was like, look, I don't want to do full work for my phone, but I don't like their whole web desktop. I just don't like it.

01:39:29 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I just created this thing where I'm using the Agent SDK. It's real lightweight because it's just a UI front end that I secure with Google. It has a shared secret and it has an HTTPS Cloudflare [tool:Cloudflare] tunnel that goes back to it. And in my case, I have it on my iMac where it's legally using because I'm actually invoking it. I'm still just coding in Claude Code with the Agent SDK. So it uses my Max plan.

01:41:27 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I'm naming it Code Anvil Mobile [tool:Code Anvil Mobile], because I had it named Claude Code Mobile and I'm like, wait, I should probably — I'm going to get OpenClaw or ClaudeBot and get sued.

01:42:48 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So for this, I'll just show you guys — we'll just do a little — this is a blank, just to show you like, there's nothing in here, right? Blank directory. And I'm just like, I'm just going to test planning mode, write me a small plan. So this is kind of what it looks like — just so you guys can kind of see the real-time streaming with the thinking.

01:43:11 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
And this is mobile-forward. I'm on my desktop here, but I mean, this thing looks great on the phone. It's built for just the phone.

01:45:22 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
<Q>One question I have for you, Scott — going back to client stuff. Last time we talked, there was a big item in the pipeline. How are things on the client side?</Q>

01:45:39 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
<A>Yeah, client side stuff's good. Some of the big stuff is still kind of just waiting in the wings. Like that one big one I was waiting on isn't a dead thing, but I think we're just kind of delayed. I've obviously got some stuff like the guys I'm SaaSing with — they're my monthly clients where I'm getting paid monthly on the first of every month.</A>

01:46:21 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I do have an idea for an SOP system that actually helps companies create SOPs with AI — kind of like this thing where I actually have a friend and two different friends in marketing that actually may be my pipeline to push this out. And we may white-label it or something through each of those guys. It's kind of the system. I haven't built it, but I have it all planned out. It makes sense to me — just a way to input data to help create SOPs with AI and then you can version them, and then you've got an admin backend, but then you've got your front end for people where they can ask questions against all the SOPs.

01:47:15 - Brandon Hancock
▶ As time goes on, what we're going to start seeing is companies will have less people and as a result, they will have more processes.

01:48:03 - Brandon Hancock
I think companies will reduce size because if they're trying to maximize profits and they have a stable application, they will reduce headcount. And in place of headcount, whoever was leading the team — let's say there was a sales team of 10 people. Now they're going to have two, and the top two guys are going to do the work of 10. How do they achieve that? They're using agents. Well, what the hell are these agents doing? These agents are following SOPs, like you're talking about, and they're acting on systems.

01:49:43 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I'm like teaching a client how to do stuff right now. And it comes down to the number one problem we have to solve is the context problem, which is how to do a task.

01:49:45 - Patrick Chouinard
It comes down to an SOP, which is a combination of steps. So you go through this procedure — that's the actionable side. And then the left-hand side of it is the knowledge base. So what do you need to know contextually to tackle this SOP?

01:50:06 - Patrick Chouinard
▶ You tackle both in order to get things to work. And you're tackling 50% of the problem, which is the SOP. Now, the final thing — you have to reduce the amount of friction it takes to make SOPs. That's the hard part.

01:50:30 - Patrick Chouinard
▶ Right now you need smart people to figure out how to decompose hard problems into SOPs, which is usually C-suite, high-level manager work, and they have to know how to interface with agents and what agents can do.

---

<!--SEGMENT
topic: Future of AI, agent orchestration, and societal impact
speakers: Brandon Hancock, Patrick Chouinard, Ty Wells, elijah stambaugh, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: agent orchestration, AI automation, Accelerando, singularity, transhumanism, industrial engineering, bottlenecks, feedback loops, opportunity window, wartime urgency, SpaceX, AGI
summary: The group engages in a wide-ranging discussion about the future trajectory of AI automation. Patrick argues that reducing unit cost of work expands the total volume of work rather than eliminating jobs, making skilled agent orchestrators the scarcest resource. Brandon frames the next two years as a critical window of opportunity, comparing it to the early internet and mobile eras. He recommends the 2005 sci-fi novel Accelerando as a prescient roadmap for what's unfolding.
-->

01:51:55 - Brandon Hancock
▶ The single most valuable skill any of us can do right now is to become an agent orchestrator and an AI systems builder. Those are the two skills that you need to think about. On the system design, you need to be thinking like an industrial engineer — viewing things in bottlenecks, feedback loops, and systems. You have to analyze every process from that lens.

01:52:36 - Patrick Chouinard
The only thing I wanted to add is — I agree with you. The agent will take a lot of space, and yes, they might reduce the amount of people you need to do certain jobs. The thing is, for the company who are going to let people go in order to do that — they're going to lose what is going to become the hardest-to-replace resources. Because when you diminish the unit cost of a work item, you don't diminish the amount of work items — you increase the possibility you have, because you have situations or use cases you could not afford doing because they were not profitable before.

01:51:21 - Patrick Chouinard
▶ Now that the unit cost of work has dropped, those use cases become profitable so you can do them, meaning you have twice the amount of use cases. And then the only people who can guide those agents properly, train them — they are going to be the scarce resource in a short amount of time.

01:53:12 - Ty Wells
▶ The problem is you're going to have a problem training new junior resources to replace the seniors that are going away, because there is no more junior work to be done because you've abstracted it in that scenario. So that's going to be the challenge of the next generation — figure out how do you train people on systems that the AI is trained instantly on.

01:56:22 - elijah stambaugh
▶ Seriously, if you get a chance this week, guys, read Accelerando [link:Accelerando by Charles Stross, 2005]. It is one of the best books describing exactly what Elijah is talking about, but they show exactly how it plays out.

01:57:00 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
That's why I would go biblical and say in Ecclesiastes, it says, there's nothing new under the sun, right? So from a biblical standpoint, I don't think we're going to get to transhumanism, but that's my personal opinion.

02:04:22 - Brandon Hancock
▶ We are in wartime before things just start getting automated and so crazy, but I know for the next year to two years, things are going to be in flux where I can still have a major impact as a human.

02:04:44 - Brandon Hancock
▶ All work done over the next two years is going to be worth 10x the amount of work that you do in five years from now. Like work done today is going to compound versus work done five years later because there's going to be 100x more people who can do the work.

02:05:34 - elijah stambaugh
▶ If you look over the past 25 years, there was the internet, there was mobile. And now there's this. You will not get a shot like this again for a very long time. So I'm just like, I've been waiting for this all my life to happen. And now that it's here — get after it. Don't think, oh, next year I'll get after it. No, it's right now.

---

<!--SEGMENT
topic: Morgan's cemetery management SaaS demo and business strategy
speakers: Morgan Cook, Brandon Hancock, Ty Wells, Patrick Chouinard
keywords: cemetery management, SaaS, D3 visualization, Freedom of Information Act, Utah, multi-tenant, Supabase, Vercel, SOC 2, HIPAA, GIS mapping, compliance software, go-to-market, TinySeed, legacy software
summary: Morgan demos a cemetery management system featuring D3 hierarchy and radial tree visualizations of burial plot structures, a public search interface, and a Freedom of Information Act-compliant request workflow for Utah counties. Brandon and Ty enthusiastically validate the business model — compliance-driven, repeatable across counties and states, targeting legacy software incumbents — and urge Morgan to pursue investment (TinySeed) and accelerate go-to-market immediately.
-->

02:21:10 - Morgan Cook
I do have one project that I'm working on heavily. It's a cemetery management system. And, you know, like you were just talking about with artifacts, these guys have a very specific government requirement for anytime they release information — it has to be through their state's mode of basically like a Freedom of Information Act. And so nothing's out there right now that supports that. So I'm going to put that together for them.

02:21:38 - Morgan Cook
One of the things I did was I used the D3 [tool:D3.js] diagramming, which is a library for visualization of layers.

02:23:46 - Morgan Cook
So this shows the structure of the cemetery, right? From the cemetery to — in this case, they have sections and rows and lots. And then the individual plots. And the plot color has — you can click to zoom back out, and then a radial tree — very similar structure.

02:27:17 - Morgan Cook
The data is a single table with a parent-child relationship within the table. So you have multi-level parent-child relationship in the structure, all the way down to the plot. And that was the thing that's different — one cemetery may have sections, rows, lots, and plots. Another one might have only lots and plots.

02:28:02 - Morgan Cook
And county to get it launched, right? Because they have a need for it right now and they're going to pay for it right now.

02:28:07 - Brandon Hancock
Awesome. So after that, though, because it has this specific requirement that the state requires for any kind of information request, then all the other counties — any state or county-run cemetery — will be of interest in having the system, right?

02:30:01 - Brandon Hancock
▶ The day and age of AI being the system of record is a huge moat. Because if you're just a wrapper around ChatGPT and there's no — why are they going to stick with you even if AI changes or gets cheaper or a competitor comes around? But if there's a huge system of record change, well, it's going to be a pain in the butt to go from record to record. So they stick.

02:30:26 - Brandon Hancock
▶ Any time a law changes or requires some complexity and you can twist the knife of being like, hey, this law goes into effect, but your current app is either going to get you fined or you're going to have to hire two more people to just manually sit around all day and do this for you — or you can just click the easy button and I have a subscription, $2,000 a month, whatever the number is, and I'll just do it for you.

02:42:00 - Morgan Cook
I did a lot of research on all the competitors, and I had Claude go out and find me every feature that every competitor had, and we worked that into what is necessary for my MVP, including all of their main features. And I found a couple where I was able to get into their user group and find out all of the requests that are being made to them, so I made sure those features were in here — to make sure that I already have what the competitors are being asked to make.

02:42:31 - Brandon Hancock
▶ What's so funny is you're competing against people who are developing like it's 2015. Like, who in the cemetery software development space is like, man, I love AI development? So like, dude, this is — in the boring, quote-unquote boring niches — this is the stuff that gets me excited, because no one's looking at this.

02:45:10 - Brandon Hancock
You're going to pay $600 a month to get the Supabase [tool:Supabase] instance that's HIPAA and SOC 2 compliant. You're going to pay the $100 static fee for Vercel [tool:Vercel] to get a static IP. Like, it's not an insane amount of money, but it's going to be more expensive. But the playbook's there.

02:49:30 - Brandon Hancock
▶ As soon as dollars trade hands, please let me know — and really, like, either TinySeed [tool:TinySeed] or something like that — money was given, and it has been an absolute lifesaver for us. And if I build fast enough, I'm going to get more contracts, and it'll just instantly replenish. So that's where you're at. I would be very happy to introduce you, just because this is the exact type of business that every investor wants to invest in.

02:50:37 - Brandon Hancock
▶ You are following the SaaS founder playbook perfectly. You spread yourself thin at first, spaghetti against the wall. Holy crap. I have a golden goose in front of me. Kill everything else and go all in.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not supplied), and therefore have been passed through unchanged:

- Jaylen.Davis
- Rag Ch
- Ryan - One Stop Creative Agency
- elijah stambaugh
- Darryl Goldstein
- Juan Torres
- Morgan Cook
- Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
- Paul Miller