=== SESSION ===
date: Unknown (references "2026" as current year)
duration_estimate: ~2 hours 50 minutes
main_themes: OpenClaw agent security and deployment, AI-assisted development workflows, member project demos (fitness app, creator monetization platform, cemetery management SaaS, mobile Claude Code interface), AI productivity philosophy, business model strategy, formal AI verification research

---

<!--SEGMENT
topic: Pre-call chatter and personal projects
speakers: Marc Juretus, Patrick Chouinard
keywords: mobile app, Apple App Store, personal website, CV portfolio, fitness app, OpenClaw, real estate site, N8N, static site, CMS
summary: Marc and Patrick catch up before the formal call begins, discussing mobile app deployment friction with Apple, Patrick's personal portfolio website rebuild, and Marc's fitness tracking app progress. Marc describes a voice-dictation workout logging feature and the app's near-release state, while Patrick explains his custom CMS-backed static site architecture.
-->

00:00:59 - Marc Juretus
That's the only mobile app that we've deployed.

00:01:03 - Patrick Chouinard
Okay.

00:01:04 - Patrick Chouinard
And as always, Apple's a pain in the ass there.

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
My fitness app went a lot faster and that stock school app I had — it's to a point, the code that it writes, that Stanford fitness app, I could give it to somebody right now. I can honestly go in now and I can pull up someone who has a login and I can assign their active workout and then I can view their log. And like I keep talking to OpenClaw [tool:OpenClaw] and it's like, you're at a point you should be able to try to have a soft release of this.

00:03:54 - Marc Juretus
I'm like, yeah, that wasn't my objective, but it's very helpful.

00:04:00 - Patrick Chouinard
When you're giving it, like, you know, what you're trying to work on.

00:04:05 - Patrick Chouinard
But I'd be interested in looking at that because I'm starting at a new gym, actually, this week.

00:04:11 - Marc Juretus
Yeah, it's pretty slick. The thing that I like the most is, like, I have this thing where you dictate workout. So you can go in and log what you did one by one. But you can click dictate workout and say 30, and it'll map up. Say you're doing triceps — oh, he said extensions. He was doing skull crushers and this. And it logged them. And I was like, holy shit, man. Yeah, it's usable now.

00:04:44 - Patrick Chouinard
Actually, what I would need is something with vision because the problem I have is the old gym I was going to was a little family gym, like very, very small and mostly dumbbells and free weights. Now I'm going to a more commercial gym, and my biggest problem is to know how or what to do with each of the new machines, because there's like, I don't know, 20, 30 machines in there that I have no clue how to use. So I'd like something where I could just take a picture of the machine and it's like, tell me what exercise I could do on that thing.

00:05:23 - Marc Juretus
Well, you know, like the few people I do train, I say start out with three days a week if you're able to do that.

00:05:30 - Patrick Chouinard
That's what I say — do push, pull, and legs.

00:05:33 - Marc Juretus
So, you know, push will be like, you know, chest, triceps, shoulders.

00:05:40 - Patrick Chouinard
My challenge is I don't know what machine does what in the new gym.

00:05:43 - Marc Juretus
Oh, well, if you go in there, I have video demos of it. I'll send you the link. But what I like is I have exercises in there that I added, and then when you go in, say like, hey, Mark has this, but I'd like that.

00:12:00 - Patrick Chouinard
But that's why I've started more and more — the sites I'm publishing are not really applications, they're static sites, but the content can be controlled through a backend admin portal. So that's actually the pattern I'm using more and more. I have a backend portal that manages whatever gets published to the site and just pushes every time. And yeah, I'm not going to be able to do applications like that, but for static sites, it makes the static site a lot more powerful, let's say, for no cost whatsoever.

00:12:50 - Marc Juretus
Really crazy thing with the real estate site — I basically said, create me about 10, 20 realtors and about 20 properties in the Pennsylvania/New Jersey area. There's pictures of the realtors, there's the properties, the prices of the houses. I'm like, man, this is just insane.

---

<!--SEGMENT
topic: Anthropic Security launch and patent discussion
speakers: Patrick Chouinard, Ty Wells, Marc Juretus
keywords: Anthropic, Anthropic Security, patent, provisional patent, user-end applications, market disruption, Lucid Dev, Usai
summary: Patrick raises Anthropic's launch of Anthropic Security, prompting Ty to discuss the competitive threat it poses to end-user AI application developers. Ty shares that he holds a provisional patent on his work and hints at a significant pivot in his project direction since the previous week.
-->

00:08:05 - Patrick Chouinard
<Q>Hey, Ty, did you see that Anthropic [tool:Anthropic] has started Anthropic Security?</Q>

00:08:13 - Ty Wells
<A>When I saw that, I thought about you right away. Yeah, I saw that. I'm like, this is why I'm trying to get away from user end-user application stuff, because these guys will just, they can knock you out in a glancing blow. They don't even have to touch you, right? I mean, they're dropping stocks like crazy, you know, just from an announcement. So, yeah, that's going to be problematic long-term.</A>

00:08:43 - Patrick Chouinard
Well, if you have a patent for it, you could probably negotiate a pretty sweet deal if they're going into the same arena that you are.

00:08:52 - Ty Wells
Yeah, yeah, yeah. I do have a patent, a provisional patent on my stuff. But I'm actually — yeah. Here's the funny thing about it. That was a week ago. This week is a whole different story. But yes, I have a patent that I feel pretty confident in.

00:09:15 - Marc Juretus
Nice. You look confident. You're all relaxed, hand behind the head.

00:09:20 - Ty Wells
I guess it was an all-day flight, and I got in, and I woke up, and my wife woke up to go to work. So I've been up since. So I'm spent.

---

<!--SEGMENT
topic: Brandon's return and AI productivity tools update
speakers: Brandon Hancock, Patrick Chouinard, Marc Juretus, Ty Wells
keywords: MetaQuest 3, Claude Code, Codex, Gemini, PowerPoint automation, Google Ads, OpenClaw, Meta VR headset, pitch decks, YouTube
summary: Brandon returns to the group after a period away and shares his current AI productivity setup, including using a Meta Quest 3 VR headset to run 15 simultaneous Claude Code instances. He highlights Codex as a superior PowerPoint generator for pitch decks and previews an upcoming Google Ads coaching series with a former Google employee named Peter.
-->

00:14:22 - Brandon Hancock
What's up, everybody? Sorry, I got beanie hair. Welcome back.

00:14:34 - Brandon Hancock
I'm pumped to see all these familiar faces, give you all the updates. We'll definitely give people a couple of minutes to all hop on. But yeah, very excited to see you guys. All the updates since we last got to talk to you guys.

00:15:25 - Brandon Hancock
All right, guys. I've gone deep in AI. I'm just now coming out. My favorite new gadget that I have to show you guys is — I got this. It's the Meta Quest 3 [tool:Meta Quest 3], basically. So what I do is I hook it up to my Mac, and I have like 15 Claude Code [tool:Claude Code] instances at the same time on like a projector in front of me, as big as I can see. And I'm doing the work of an entire company myself. It's crazy. I have marketing. I have sales out.

00:18:00 - Brandon Hancock
Most Helpful Win. Claude Code, obviously, for all things related to code, still my favorite. Cool recommendation — I have been having to work a ton recently on creating PowerPoints for pitch decks, presentations, education content, like all sorts of stuff. Codex [tool:Codex] is by far the best PowerPoint maker I've ever dealt with. I will kick it off and it will make a 90-slide presentation for me in 30 minutes. And then I just iterate from there. But Claude Code — under no circumstance could I ever get it to do well at more than like 20 slides, and even then it would struggle.

▶ But Codex — it will, just to give you guys a heads up, because I want you guys to try it if you have to make presentations — you hook it up to Gemini [tool:Gemini] so it can make images, and then you just say go forth, here's a brain dump, go make PowerPoint slides, and it will make custom images, fit them in the PowerPoint, because Codex is very precise, it'll test to make sure it's formatted well, do it again and again and again. So I'm making every week probably close to 200 PowerPoint slides for different things I have to do, and Codex is doing all of it. So, yeah, if you're doing a pitch, Codex is the game changer.

00:19:18 - Brandon Hancock
We are hiring an ads coach for our company. His name's Peter. Awesome guy. Used to work at Google. And we're going to do like a four-week, six-week program with him where he's going to help us redo our ads. And we're just going to be sharing all of that on YouTube. So, if you kind of wanted to see behind the scenes of like, oh, cool, I have a software idea. And now I want to get traffic. How do I actually do that with Google Ads [tool:Google Ads] in 2026? This will probably be the video. So, you'll get to see his framework.

---

<!--SEGMENT
topic: Patrick's AI-powered CV and CMS portfolio site
speakers: Patrick Chouinard, Brandon Hancock
keywords: Claude Sonnet, Hostinger, CloudCode, CMS, JSON, bilingual, GitHub, OpenClaw, admin dashboard, career portfolio
summary: Patrick demos his personal portfolio website, which uses Claude Sonnet 4.6 to parse unstructured career notes and rewrite them in structured JSON in both French and English natively. He explains the custom CMS admin dashboard that pushes content to Hostinger automatically via Claude Code, and describes treating OpenClaw as a managed worker with its own GitHub account within a shared organization.
-->

00:24:00 - Patrick Chouinard
At length in the last couple of weeks on that specific subject, but yeah, so the idea is main site. But what I really love about that site — this is the public site. This is what's pushed to Hostinger [tool:Hostinger] automatically by Claude Code.

00:24:20 - Brandon Hancock
Oh, really?

00:24:20 - Patrick Chouinard
Behind the scene, I have an admin dashboard that allows me to manage all the eras I split my career into, all of the engagement, the technology, the skill, the narrative, everything here, I can update and push to the website. Basically, I created my own CMS system.

00:24:51 - Patrick Chouinard
And on top of that, when I create a new engagement — that's the part I always say documented my job experience. So now I have "Create with AI." I just grab, let's say, I have a little fake one I created just for demo, but so it's very loose, like I worked for that one from around September, very vague, nothing structured whatsoever, just explaining what I did.

00:25:17 - Patrick Chouinard
Then it's Claude Sonnet 4.6 [tool:Claude Sonnet 4.6] behind the scene that rewrites the whole thing, and it will submit the rewrite in JSON in order to fill all of this — the form — so not only the job description, but like the employer name, the client, the project, like it extracts everything, writes in both French and English as a native speaker, so it's not writing in one and translating, it's actually writing both in a native way, and it even adds notes like "employer name retained as stated."

00:28:00 - Patrick Chouinard
That I created for OpenClaw. So OpenClaw has its own GitHub [tool:GitHub] account. I have mine, and we share an organization. So everything it develops, it develops in that organization.

▶ I really manage security exactly as if it was a human worker.

00:28:14 - Brandon Hancock
Yeah, that's awesome.

---

<!--SEGMENT
topic: OpenClaw security architecture and deployment strategies
speakers: Brandon Hancock, Patrick Chouinard, Darryl Goldstein, Juan Torres
keywords: OpenClaw, prompt injection, Docker, Proxmox, Ubuntu VM, Gmail, Google Drive, Discord, Slack, Appify, LinkedIn, Mac Mini, EC2, VPC, Cloudflare
summary: The group compares approaches to deploying OpenClaw securely. Patrick describes a hardened setup using a dedicated Ubuntu VM on Proxmox, isolated Gmail, Google Drive, and Discord channels to manage context windows. Brandon shares his simpler Slack-only approach with Appify for LinkedIn research. Juan asks about AWS VPC isolation, and Darryl asks about hardware requirements.
-->

00:28:15 - Brandon Hancock
Real fast, guys, I just want to share what I'm doing with OpenClaw. Just maybe it'll strike a conversation. Patrick is definitely going down to like 10 out of 10 most secure. I probably should be doing what Patrick's doing. We all should probably do what Patrick's doing, to be honest.

▶ My poor man, lazy way — what I'm doing right now is I just have it only accessible to Slack [tool:Slack], and I'm only feeding it information I want it to have access to, and it can't do anything else. Like it doesn't have access to email, it doesn't have a WhatsApp, it has nothing else. All it has access to is an individual Slack channel.

00:29:07 - Brandon Hancock
<Q>Could it go absolutely bonkers, though, if it goes to a website that has some prompt injection stuff?</Q>

00:29:14 - Brandon Hancock
<A>Maybe. But that's how I'm doing it to automate a lot of customer research and outreach. I just have it hooked up to Appify [tool:Appify] with LinkedIn browse features. So anytime someone tries something out, we can quickly just do a sit-rep on who they are, what department they probably work for, and who's their boss, and gives us a report.</A>

00:29:50 - Patrick Chouinard
It's not, but if I had to say one thing — I did give mine an email, but it has its own, and I gave it one rule.

00:30:00 - Patrick Chouinard
▶ It only reads email coming from my email address. Anything else, it tells me there's an email, but it doesn't read it. That way, I'm avoiding the prompt injection.

00:30:10 - Patrick Chouinard
It has its own calendar. So instead of playing with my calendar, it actually creates the meeting itself, and then it invites me. It has its own machine dedicated with nothing else on it. It has its own Gmail [tool:Gmail] and Google Docs [tool:Google Docs]. So since it has Google Drive [tool:Google Drive], that's where I put all the documentation it can interact with.

▶ Try interacting with Discord [tool:Discord], because with Discord, you can very easily create multiple channels and split your context by channel, so you don't overwhelm the context window and start getting enormous amounts of money in tokens because you send 20,000 tokens in every exchange.

00:31:04 - Darryl Goldstein
<Q>Are you running on Mac Mini? What are you using to run?</Q>

00:31:09 - Patrick Chouinard
<A>It's a Ubuntu VM running on Proxmox [tool:Proxmox].</A>

00:31:17 - Brandon Hancock
I did, real fast, buy a Mac Mini [tool:Mac Mini]. I have yet to do anything with it, but the plan is to put OpenClaw on it. It's completely overkill, but I just wanted to do it.

00:31:37 - Juan Torres
<Q>Yeah, I don't know, Patrick or Brandon, what you would recommend, but I've thought of doing that for an EC2 instance, just have its own VPC, its own virtual private cloud with its own security permissions, just to be able to handle the network. But when I give it resources, like a database instance, then I'm afraid that it's going to erase it. So, how do you regularize the relationship between OpenClaw and the resources within your VPC?</Q>

00:32:25 - Patrick Chouinard
<A>If you can put a VM somewhere and even Docker Desktop [tool:Docker], I mean, that's all it needs. Isolation. It doesn't need resources. So I really don't get why everybody is going and putting that on VPS or having a monthly fee to run it. It runs on hardware.</A>

00:33:25 - Brandon Hancock
I have it running in Docker on my computer. It's just a pain because my co-founder, if my computer turns off, he's talking to OpenClaw and he's like, damn it, why is it not working? And it's because my computer is asleep. So that's why we're going to get an external device.

▶ But Juan, to answer your question, I am trying to limit the exposure of what it can do. Mine is — you consume what I give you, and you can write to a Google Drive. There's no escaping the box that I have built it in.

00:33:55 - Brandon Hancock
My biggest fear — it goes, well, I'll just be a little bit more proactive, and I'll just write the email. And then all of a sudden, it's blasting 500 clients garbage. So that is not a risk I wanted to accept. So I always just write to a Google Drive, or a Google Sheet, and then you can have an external service reach in, that is controlled programmatically and not by AI, and just look for a new thing and do what you want.

▶ But there needs to be a clear box that it can't get out of, and you want to peek in when you need something and feed it only what it needs and nothing else.

---

<!--SEGMENT
topic: Jaylen's creator monetization platform demo
speakers: Jaylen.Davis, Brandon Hancock, Darryl Goldstein, Ryan - One Stop Creative Agency
keywords: content creator platform, video monetization, fan funding, YouTube, Instagram, TikTok, subscription model, Cameo, Vimeo, community, sponsorship
summary: Jaylen demos a web app that lets content creators monetize fan video requests — fans fund a request, the creator fulfills it and keeps 90%. Brandon suggests pivoting toward a subscription community model at $50–99/month per creator. Darryl proposes adding in-app video recording for non-technical creators. The group discusses multiple monetization angles and the math of reaching revenue targets.
-->

00:36:19 - Jaylen.Davis
Okay, so yeah, basically, I came on maybe back in October or November. Mitch McCauley, he actually sent me the link. And since then, I've developed my web app tremendously. Let me share my screen.

00:36:56 - Jaylen.Davis
Yeah, basically, and since then, we've pivoted to not only — we help YouTubers. We also work with Instagrammers and TikTokers. Basically, it's just for those who might not know, it's just a platform where a content creator can monetize their video requests. So you can basically tell your fans, look, if you want me to make this particular video, I'll do it for this price. Once they fund it, you make the video and then you get paid 90%. So if someone asks Brandon to make a video about something, and let's say his price was $100, they put in the $100, he makes the video and then he receives $90. It's as simple as that.

00:37:41 - Jaylen.Davis
Yeah, so far we have about 11 people on the platform. We're making progress and I just wanted to get any feedback on any possible ideas. For creators, you guys can actually decline topics if for whatever reason you don't want to create that particular video. You set your own price when you sign up.

00:38:07 - Brandon Hancock
One quick thing — the second I saw your face hop on the call, I was like, oh, I have ideas. So, I think my main thing that I've always thought would be cool is for people to vote and downvote on ideas and me pay you a monthly subscription, 50 bucks a month. Because then it's recurring revenue and you're not at the mercy of customers. Like, it's consistent.

▶ You know, $50 a month and you build me a school where my YouTube members can come in, chat about my videos, and request future videos. Like, basically, be the blog of what YouTube is. Turn every YouTube channel into a school community automatically.

00:39:00 - Brandon Hancock
And then just tell the creator, hey, you pay me 50 bucks, 75 bucks, 99 bucks a month, and I will give you access to run this community. You're the gatekeeper, you're hosting a club, and you're dangling the keys to their own house in front of them and say, pay me 99 bucks, and I'll let you in. Much more reliable subscription model, and they're incentivized to maintain it.

00:42:00 - Brandon Hancock
What does the app have to be, and how long does it take to get there? Or, hey, if I do the founder mode, where they pay 50 bucks a month, or 100 bucks a month, how long does it take — if they do 100 bucks a month — to get to $20,000 a month? Okay, I need 200 founders at $100 a month. Boom, I just have to find 200 people on earth to give me 100 bucks a month. Such an easier problem to solve.

00:45:24 - Darryl Goldstein
<Q>So, is there a feature here where you could capture that video right from your app, as if it's on a YouTube-type video, meaning that the person making the video for you — just make it real simple — they can come on here and say, hey, Darryl, happy birthday to your mother, have a great day, and they don't have to produce anything. Capture it right here, through a recording on your app, and boom, it's done.</Q>

00:46:16 - Jaylen.Davis
<A>I get what you're saying. No, we currently don't have that feature. I believe Vimeo [tool:Vimeo] has something like that where you can basically just request a quick video from a celebrity.</A>

---

<!--SEGMENT
topic: Marc's fitness app and Google Cloud RAG demo
speakers: Marc Juretus, Brandon Hancock
keywords: fitness app, workout logging, voice dictation, exercise library, Grok, Vertex AI, RAG, Model Garden, Google Cloud, Gemini, Google Generative AI certification, stock school app, paper trading
summary: Marc demos his fitness tracking app featuring voice-dictated workout logging, an AI personal trainer with workout history access, and AI-generated exercise demo videos made with Grok. He also shows a Google Cloud RAG-powered clothing site and image generation via Model Garden. Brandon recommends Gemini for cost-effective production use and discusses Claude Code's subsidized pricing.
-->

00:47:26 - Brandon Hancock
All right. We'll keep cruising, guys. I think next up was, based on the call order, Marc. What is going on, man?

00:47:53 - Marc Juretus
So, what have I been working on? I know you guys were talking about OpenClaw. I have one. I have it on a Google virtual machine up in the cloud, running Ubuntu 22.04. What I have it doing is I talk to it in Telegram [tool:Telegram], and say I'm out at a bar or something. I can talk to command, email trainer, their name, their email. It'll send a pre-formatted email addressed to them, you know, the basic foundation of how I work out, but it taps into my calendar and shows my availability dates.

00:48:32 - Marc Juretus
Another one is I'm trying to find my son a job, and I have another one. I have, like, it pulls in a job service API, gets Indeed [tool:Indeed] and a couple others, but if I type "get jobs," whatever category, say laborer and then email, it'll email any available job listings to his email address or whoever I put in for email. And I have it for a daily motivator, but I had to drop that down to Haiku [tool:Claude Haiku], man. It was starting to run me some dough. I was like, yeah, don't leave it on Opus [tool:Claude Opus].

00:49:09 - Brandon Hancock
▶ What I recommend for applications where people use them — Gemini is the best bang for buck on capability and cost, at least that I've seen right now. So I would recommend just because, without it, it gets pretty expensive using anything related to Opus.

00:49:30 - Brandon Hancock
I mean, they just — Claude Code spoiled us. I don't know if you saw the report. They're subsidizing it — it was either 17 or 14x. So we pay $200 and they cost, I think it was like $2,800. So it's crazy how much they're eating for us to use their platform right now.

00:50:47 - Marc Juretus
I'm going to probably take the Google Generative AI exam [tool:Google Generative AI certification]. I've been up on the cloud — I spun up a RAG on Vertex AI [tool:Vertex AI], it spun up a clothing site that has a chat, and then I used the image gen from Model Garden [tool:Model Garden] to generate images, like, in the admin pool for that, just so I kind of get a feel of that, so I'm going to try to take that exam next week if I can.

00:53:25 - Marc Juretus
Can you see my screen? Yeah, so basically that's a site. That's obviously me in the corner. I have a couple of different aspects to it, but it's kind of built for stuff that I do. Like when I work out at 5am in the morning, I went ahead — like I'm doing triceps and chest — and I'm like, just pull up three random of each, so it'll go in there, it'll give me three random exercises in the basic summary of what they are.

00:54:28 - Marc Juretus
I have an exercise library that's basically all of my exercises. I have tricep pushdowns — so I made a video on Grok [tool:Grok], that's not even me, of working out. So I'll put all the exercises in for that.

00:55:40 - Marc Juretus
And then the one thing is I actually have a trainer in there. In here I have a trainer where if you say "I need a shoulder workout," it actually has access to your history and sees what you did. It says, hey man, your shoulders look like crap because you've only been doing this, that, or the other.

00:56:27 - Marc Juretus
I have a button called "Summarize Workout." And when you click on the button, instead of you going in here and manually adding each exercise, I actually give you the ability to just click on the button, summarize workout. I tested it — I would say, hey, I did three sets, tricep pulldowns for 50. And I did three sets of skull crushers for 50. It'll actually log them and go on your history and parse them out to separate exercises that I have in my database.

00:57:26 - Marc Juretus
And then I got a stock school app too, where you go in and if you take three tutorials, I give you $25,000 in paper money. It tracks it. And then I actually have a trading coach that'll go in there and say, hey, man, you went a little too heavy in tech.

00:58:00 - Marc Juretus
This is what I was telling you about for the RAG — this is going to Google Gemini, this has a RAG client, and then it has Creative Studio, where I can say I want to generate an image for running shoes, because I sell shoes, this goes up to Model Garden in Google Cloud, and it'll actually generate me an image from their Model Garden model that they have up there.

---

<!--SEGMENT
topic: AI productivity philosophy and multi-agent workflow
speakers: Brandon Hancock, Marc Juretus, Patrick Chouinard
keywords: Claude Code, Warp terminal, Meta Quest 3, token throughput, multi-agent, SEO, Codex, Accelerando, productivity mindset, shots downrange
summary: Brandon articulates his philosophy of maximizing AI token output per day as the primary productivity metric, describing his Warp terminal multi-window setup and Meta Quest 3 VR workflow for running many Claude Code instances simultaneously. He recommends the book Accelerando as a prescient description of current AI-driven societal change and encourages members to treat every idle moment as wasted AI output time.
-->

01:00:15 - Brandon Hancock
Real quick, final thing, and we'll keep cruising. Marc said it so well — it just spits out so much. So like, the way I'm measuring a good day right now is how many tokens, how often — I try to figure out how to phrase this — how many times per day was I busy generating tokens? Like, what is my idle time compared to my output time?

▶ So that's why I brought the Meta Quest 3, because right now, humans are the limiting factor for AI. Your experience is going to cut down how long it takes you to get to the same spot, maybe a week, maybe a month. But then, once we're at the same playing field, it's how long can you, per day, just shoot shots downrange using AI.

01:01:00 - Brandon Hancock
Every moment that I'm awake, I need to be shooting shots downrange, or I'm just kind of wasting time. I have marketing, sales, development, strategic outreach — I have every possible aspect of my business, and I'm just bam, bam, bam, bam, constant, every day, 24-7, because I'm moving the entire business forward on your own back, and there's nothing stopping you, minus just putting on the goggles, or just putting up 10 agents on your screen, and just shots downrange.

01:02:00 - Brandon Hancock
You can always just say like, man, I've always heard SEO is great. Okay, cool. What are the five best books on it? What are the playbooks that they offer? Apply it to my business. Fantastic. You now have work for the next day and a half on implementing SEO in your business. So it's just like, you know all the words and just go steal the best of the best, their playbooks, apply it to your business. Fantastic. You now have four chats going off on building the code, writing the blogs.

01:03:00 - Brandon Hancock
▶ If you guys want the most nerdy book, but probably one of the best descriptions of what's about to happen to us as a society, it's called Accelerando [link:Accelerando by Charles Stross, published 2005]. It came out 2005, and it's legitimately a playbook for what's happening right now. We're in the stage where us, right now, there's a few of us who are putting Meta headsets on our face and talking to AI 24-7, like, that is the first chapter. It is that, and that's where we're at.

01:25:07 - Brandon Hancock
I'm using Warp [tool:Warp] to do everything. So like, I constantly have as many windows as I possibly can to just do all the work that I'm doing. And every time I want a new window, I just hit Command+Shift+D to open up a new one, or Command+D if I want to split it. So this is what I'm doing. And I just have a script to tell Warp, like, hey, I'm ready to start working again. And it just opens up six modules, eight modules in a nice window format.

▶ I've left the editor behind, and I don't use it, unless I'm checking like one or two things. The fact that I can only open three Claude Code instances reliably and see them all in parallel — anti-gravity is the friction, which then led me to Warp. And then Warp led me to getting the Meta Quest 3, because now I can have as many screens as I want.

---

<!--SEGMENT
topic: Ty's formal AI verification and autonomous agent system
speakers: Ty Wells, Brandon Hancock
keywords: formal verification, AI hallucination, AGI, GitHub Actions, regression testing, autonomous agents, persistent memory, Usai, provisional patent, non-deterministic testing, Cypress
summary: Ty presents his renamed project Usai, a formal verification layer for AI output designed to catch logical errors and hallucinations (estimated at 30–40% of outputs). He describes using GitHub Actions for automated code verification and demonstrates a long-running autonomous agent performing self-verification. Brandon connects this to his own pain point of regression testing non-deterministic AI applications, and the two agree to connect offline.
-->

01:05:02 - Ty Wells
Okay, so basically what I'm doing here is creating a formal verification layer for all AI output because we know AI models hallucinate, right? 30 to 40% — all depends, right? How deep the context window is. Basically, it is a spell check for logic that's coming out of the model. So I did this paper basically to discuss how this is actually implemented. And I was reaching out to publish it on the archive. I did put a provisional patent on what I built.

01:07:12 - Brandon Hancock
<Q>A few things. So the thing that I want to focus on is help with testing with AI, meaning there's unit tests, cool, like I understand this function, here's the 200 ways we could use this function, here's the inputs, outputs, cool. Unit test makes sense. Then you keep going up the stack and then there's end-to-end testing, which at this point you pretty much use Cypress [tool:Cypress]. But now that things are different, it's very hard to — with AI, especially if you're building an entire application around AI — it's non-deterministic by default. So it's like, I almost want to have at the same time, 30 different users for every archetype that could happen. And every time I make a code change, I would love the ability to review, to make sure I didn't break anything. Because now that I'm getting more into production, that's the biggest issue I'm running into — I can crank out code like there's no tomorrow. But it's like, oh shit, did I break something that I built six weeks ago?</Q>

01:09:10 - Ty Wells
<A>So to answer your question, yes, that was one of my biggest issues too, right? The regression testing is just crazy. So you wanted that to happen automatically. And this does that through GitHub Actions [tool:GitHub Actions] where it verifies the code that's in there automatically. It runs it and tries to verify that code.</A>

01:09:43 - Ty Wells
So what I did was I took it a step further and wanted to try to reach AGI, right? Meaning if I have better code coming out — because AGI itself is code. And so I use my verification process to create the things that make up AGI and I'm just testing it. So I created — and I started this before OpenClaw — but it's basically the ability I've been trying to achieve for these long-running autonomous agents that have memory that persists and so forth. I built that using Usai [tool:Usai] as a verification process of the different agents to do that.

01:11:45 - Ty Wells
I have the sound on here. So I started this when we started the call after Jaylen presented. So we'll have to circle back to that and see. And I have it basically the orb just sort of progressing through different stages to show that it's — so this is actually the inaugural flight of this autonomous agent.

01:12:15 - Brandon Hancock
I like the way you're thinking about this because, I mean, yeah. How do we just make stuff reliable? I mean, you're hitting a very — I think it's the coolest part of a new problem that was just introduced to society, which we're all facing. I mean, if you look at the chat, everyone can spit out more code than they can handle at this point. And now it's just like, shoot, does it actually work? Because there's a difference from, you know, way back in the day — does the code compile, AKA, is it syntactically correct? Yes, it builds, but is it semantically or behaviorally doing what I want it to do? No, not always.

▶ Ty Wells: Yeah. And I'd love to talk to you offline. Friday would probably be the best.

---

<!--SEGMENT
topic: Python vs TypeScript for AI backends and Claude Code workflow tips
speakers: Brandon Hancock, Patrick Chouinard, Rag Ch, Morgan Cook, elijah stambaugh
keywords: Python, TypeScript, FastAPI, Flask, Dockling, RAG, Claude Code, Gemini, Codex, Warp, tmux, Claude Code agent teams, VS Code, anti-gravity editor, mermaid diagrams
summary: Brandon answers a question about Python vs TypeScript for AI backends, recommending Python for AI-specific tasks due to library maturity (e.g., Dockling for RAG). Rag Ch gets a live walkthrough of the correct Claude Code terminal workflow. Morgan Cook shares an insight that asking AI to write a function produces better results than asking it to directly generate structured output. Brandon and Elijah discuss Claude Code agent teams, tmux conflicts, and the Claude Code hooks system for enforcing task templates before coding.
-->

01:13:44 - Brandon Hancock
<Q>Elena was asking, do you think there's a difference between building a backend for GenAI on TypeScript versus Python, any benefits to one versus the other?</Q>

01:14:35 - Brandon Hancock
<A>So I prefer at this point, if I'm going to do anything related to AI, I like using Python. And I'll tell you why. It's because Python is leading the front on AI. For example, working with a client on a project, I love Dockling [tool:Dockling]. Dockling is one of my favorite embedding and chunking tools out there for building RAG applications. And it's native to Python. And we're like, but they want to do everything in TypeScript. So as a result, I was like, oh, there's a Dockling TS package. It's fake. All it does is it's a pointer to a version of you running Python somewhere else. So it's just a wrapper to shoot to a Python server somewhere else.</A>

▶ So it's like, man, at the end of the day, it's just a necessary evil of knowing two languages — TypeScript for all front-end and back-end, and then when it comes to AI-specific tasks, hey, I just need to know a little bit of Python.

01:17:01 - Morgan Cook
And it struggled for like five minutes before it came back with a response, and it gave me a JSON file, which I then dropped into my map viewer, and it was horrible. And all I did to fix it was say, make me a JavaScript function that does this exact prompt I just gave you. And it made the function, and the function works perfectly.

▶ So what I got out of that was the AIs know how to write functions and programs really well. They don't know how to implement them internally themselves. He can't run the iteration to create all the points on the plots and have the accurate output, but he can make a function that does it.

00:18:00 - Morgan Cook
▶ So if you're struggling to have AI create the proper structured document or whatever, have it make a function to do it, because it will create a beautiful function to make that happen.

01:18:28 - Brandon Hancock
When it comes to long-running jobs, if I know something's going to take 20 minutes of just iteration, iteration, iteration — Codex. I am falling in love with Codex for tasks that I just — high-precision tasks. Like, hey, it has to be precise. I don't care how long it takes. I just want it to work after 20 minutes of you doing your thing. Codex is the move. Just for quick iteration, I'm just like, bam, bam, bam, adding a feature, checking it, doing stuff — Claude Code all day, baby.

▶ But if I'm going to do a deep migration from A to B, if I'm building a PowerPoint that's idea to final presentation I can show to a customer where it's going to take 20, 30 minutes of AI iterating and looping over itself — Codex. Seriously, would recommend. You get to go so far on the $20 a month plan.

01:20:33 - Rag Ch
<Q>So, my question is, like, I see in your videos, you type somewhere here. I know you have been using Cursor, and you type here, but you seem to be using Claude Code. So, what I have been doing is, I just type here in the Claude Code terminal, and that's what I do. But I have seen — you seem to be typing here and then getting the commands and all that.</Q>

01:22:53 - Brandon Hancock
<A>So that's the first mistake. Don't use the Claude Code terminal. That's mistake one. You're just using a regular terminal. It doesn't have as many features, and that's why we don't use it.</A>

▶ The area where we code, we can actually open up a terminal there. That's the trick. That's the secret sauce. So if you go to terminal, on the top, click new terminal window. And we can just — I type in the letter C to open up Claude. And I'm just constantly like, Claude, do this, do this, do this.

01:28:00 - Patrick Chouinard
Just wanted to say, I work with more junior developers that are not yet able to split their brain 15 ways. And they don't have necessarily the amount of money it would take to run eight Claude Code instances in parallel and still have tokens at the end of the day.

▶ So what Rag is doing is pretty good also — you have your Claude Code to do the hard work, but all of your code review, all of the management stuff, you can leave it to, in this case, Gemini 2.5 Pro [tool:Gemini 2.5 Pro], just so it takes off a little bit of the pressure on your tokens and Claude. And if you want, you can — I would even say, if you have an OpenAI account, start a Codex window. Have not just eight or ten Claude Code instances — try to spread it as much as you can, so you can leverage all the tokens from all the subscriptions at one point and not overload your token. Split responsibility — Claude does one type of work, Gemini does another type of work, GPT does another type of work.

01:31:09 - elijah stambaugh
<Q>So you might have seen that Claude Code has agent teams, and to run them and see all the different agents running, you run it in iTerm2 [tool:iTerm2] and run tmux [tool:tmux] in there. So I don't know if you're familiar with that, but is that the CLI tool that you're using or referencing?</Q>

01:31:41 - Brandon Hancock
<A>I had issues with tmux — there's the shortcut keys all mess with each other, because there's Claude, which has its own shortcut keys, but because we're running an interactive CLI in another CLI, I had a lot of conflicting issues.</A>

▶ Of everything that I do — because plans are great, but I still want it to go through my process of thinking of second-order consequences, like my programming style — so I force it to write out a task document before it can do code. So if that's something of interest to you, you can always say, literally what I just said, hey, can you update our hooks to make sure that as soon as I exit plan mode, I write a new task template. That's exactly what I did, and it did it for me.

---

<!--SEGMENT
topic: Scott's mobile Claude Code interface and SOP system concept
speakers: Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com, Brandon Hancock, Patrick Chouinard
keywords: Code Anvil Mobile, Claude Agent SDK, Cloudflare tunnel, Google OAuth, internal SaaS, neural spark, Slack, 11 Labs, MCP, RLM, RAG, SOPs, AI agents, knowledge base
summary: Scott demos Code Anvil Mobile, a lightweight mobile-forward UI built on Anthropic's Agent SDK that tunnels securely back to his local machine via Cloudflare, allowing him to interact with Claude Code from his phone without using API tokens. He also describes converting his personal AI assistant into a multi-user internal SaaS for clients, and introduces the concept of Reverse Language Model (RLM) retrieval improving his morning summary report quality. The group then has a broad discussion about SOPs as the critical infrastructure for AI agents replacing human workers.
-->

01:36:42 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
Yeah. Well, just a note — the next three days I'm actually going to be finally doing it. I've been planning it where that neural spark thing that had the knowledge base and the Google tie-ins — I'm going to be adding Slack in there for that. For a couple of my clients, we're going to internal SaaS it because we're probably going to put more than just those two on it. So we'll actually create like a multi-user instead of trying to set this up individually, since there's going to be more than two.

01:38:02 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So I created the — it was like a mobile interface to get to a Claude Code instance, that's like through a secure Cloudflare [tool:Cloudflare] tunnel. I'm using the Agent SDK [tool:Anthropic Agent SDK] because I was like, look, I don't want to do full work for my phone, but I don't like their whole web desktop. I just don't like it. So I just created this thing where I'm using the Agent SDK. It's real lightweight because it's just a UI front end that I secure with Google. It has a shared secret and it has an HTTPS Cloudflare tunnel that goes back to it. And in my case, I have it on my iMac where it's legally using because I'm actually invoking it. I'm still just coding in Claude Code with the Agent SDK. So it uses my Max plan.

01:41:27 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I'm naming it Code Anvil Mobile [tool:Code Anvil Mobile], because I had it named Claude Code Mobile and I'm like, wait, I should probably — I'm going to get sued. But I was going to show like a little cool thing in here. The cool thing is, you know, it's locked to the folders where I have my app development, right? And so the neat thing is I can go around and get into any of my workspaces I've got.

01:42:48 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
So like it even gives you terminal if you want straight terminal, which is kind of fun, but here's the chat. And so it's nice to have like the UI to where like, if I put this in planning mode — and I'll show you guys this too — like it does have budget caps and turn limits, even though this doesn't use API, it's still kind of helpful if you want to have a long-running task.

01:47:09 - Brandon Hancock
<Q>As time goes on, what we're going to start seeing is companies will have less people and as a result, they will have more processes. I think companies will reduce size because if they're trying to maximize profits, they will, and they have a stable application, they will reduce headcount. And in replace of headcount, whoever was leading the team — let's say there was a sales team of 10 people. Now they're going to have two and the top two guys are going to do the work of 10. How do they achieve that? They're using agents. Well, what the hell are these agents doing? These agents are following SOPs, like you're talking about, and they're acting on systems.</Q>

01:49:43 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
I'm like teaching a client how to do stuff right now. And it comes down to the number one problem we have to solve is the context problem, which is how to do a task.

01:49:48 - Patrick Chouinard
<A>It comes down to an SOP, which is a combination of steps. So you go through this procedure — that's the actionable side. And then the left-hand side of it is the knowledge base. So what do you need to know contextually to tackle this SOP? You tackle both in order to get things to work. Now, the final thing — you have to reduce the amount of friction it takes to make SOPs, that's the hard part. Because right now you need smart people to figure out how to decompose hard problems into SOPs, which is usually C-suite, high-level manager work, and they have to know how to interface with agents and what agents can do.</A>

01:50:47 - Patrick Chouinard
The only thing I wanted to add is — I agree with you. The agent will take a lot of space, and yes, they might reduce the amount of people you need to do certain jobs. The thing is, for the company who are going to let people go in order to do that — they're going to lose what is going to become the hardest-to-replace resource. Because when you diminish the unit cost of a work item, you don't diminish the amount of work items, you increase the possibility you have because you have situations or use cases you could not afford doing because they were not profitable before. Now that the unit cost of work has dropped, those use cases become profitable so you can do them, meaning you have twice the amount of use cases.

▶ And then the only people who can guide those agents properly, train them — they are going to be the scarce resource in a short amount of time.

01:51:58 - Brandon Hancock
▶ The single most valuable skill any of us can do right now is to become an agent orchestrator and an AI systems builder. Those are the two skills that you need. On the system design, you need to be thinking like an industrial engineer, which is viewing things in bottlenecks, feedback loops, and systems. You have to analyze every process from that lens. And then once you can see it that way, then you come in as the agent orchestrator who's saying, here's how you tackle and decompose system one into steps.

01:57:47 - Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
That one thing that you reminded me of was — I haven't talked about how the RLM stuff's going, and what I've noticed so far, doing the Reverse Language Model [tool:Reverse Language Model / RLM] stuff. Now, obviously I haven't gotten to test it on the large RAG yet. But I've already noticed just turning on RLM — it made it more agentic because instead of just dumping it, like it just randomly would pull Google data in from tasks, email, calendar, try to give me this morning summary — now it's actually with the prompt, instead of just applying the prompt to the information that ends up in there, now it's getting smarter and looking for things.

▶ I noticed the quality of my morning summary reports got better in general about what it was telling me just by turning that on.

---

<!--SEGMENT
topic: Paul's AI consulting business and urgency of the current moment
speakers: Paul Miller, Brandon Hancock, elijah stambaugh, Ty Wells, Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com
keywords: AI consulting, B2B, custom development, SaaS vs custom, agent orchestration, wartime mindset, opportunity window, internet era, mobile era, Accelerando, transhumanism
summary: Paul, calling from an airport in Melbourne, describes landing a large six-month AI project for a mid-to-large business and potentially a second similar engagement, questioning whether custom B2B work is more viable than SaaS. Brandon and others respond with a passionate call to urgency, arguing the current 1–2 year window is the highest-leverage moment in a generation for AI practitioners, comparable to the early internet and mobile eras. The group debates the long-term societal trajectory of automation.
-->

02:01:00 - Paul Miller
Yeah, I'm just sitting in the terminal lounge at the gate at the moment to fly back to New Zealand from the Western Isle. So I'm over here in Melbourne doing an AI project. This is one of the ones that I kind of sold the secret sauce, and it's turned out to be this huge project from a medium-sized large business, and it's like six months of work, but I'm about to sign up a second one that looks like it's going to be of similar size.

02:01:46 - Paul Miller
So I've kind of got the engine going, and it's funny. It's looking like it's old-school development work for one company, but we can build it in a way that is repeatable for an industry. So it's weird, I'm having to rethink my thinking, like, oh, SaaS is the way, and it's about scaling it up. This is so much easier. I don't have to be doing selling. I can probably do two or three customs at the same time. And there's lots of money.

02:04:22 - Brandon Hancock
We are in wartime for before things just start getting automated and so crazy, but I know for the next year to two years, things are going to be in flux where I can still have a major impact as a human.

▶ All work done over the next two years is going to be worth 10x the amount of work that you do in five years from now. Like work done today is going to compound versus work done five years later because there's going to be 100x more people who can do the work. Right now, there's a very small 1%, 2% of the population that even understands what we're talking about on this call. So just know you have more opportunities than the competition is the least it's ever going to be right now.

02:05:34 - elijah stambaugh
The way I like to phrase it is — if you look over the past 25 years, there was the internet, there was mobile. And now there's this. You, we will not get a shot like this again for a very long time. So I'm just like, I've been waiting for this all my life to happen. And now that it's here, it's like, guys — get after it, you know? Don't think, oh, next year I'll get after it. No, it's right now. So I don't — I get pumped thinking about this. It gets me going. So I just want to stress this sense of urgency because now is the time. You'll change your life and your kids' lives too, over the next two years. This is when it happens.

02:07:00 - elijah stambaugh
I've been working with Ohio University for like three years. They've developed an emotional behavior platform. I have a tech transfer agreement. Don Davis, who's a part of this group, he's working with me. It's an equity deal. We do have eight schools that are using it. But what I'm trying to really do is build the AI team that builds the new product, not just the product, right? Because I know we have an opportunity at a market, and I know a lot of ed tech and all that. But I'd really like to get a guy like Scott or Ty. I still feel like I need a production-level person, because Dawn is like me, and we're AI-assisted developers, right?

02:08:36 - Brandon Hancock
What I see work very well is when one person is the SME on colleges, education, something, and can get deals. That's the kicker. Like that makes the dream team for that developer to pair up with. Could then the developer gets to go heads down, build the systems, build the code. And all they're doing is just going like, hey, Elijah, how did the call go this week with the 10 different people you've talked to?

▶ It's perfectly synergistic to where they're cranking out code all day, you're selling, learning what the customer needs, having those feedback conversations, and everyone's cycling to each other. That's what winning looks like.

02:09:46 - elijah stambaugh
▶ If you're B2B, you need the deal guy, because that's the moat.

02:10:42 - Brandon Hancock
Imagine if you can remove — what is the agentic development process look like in the future? Well, it's all those things we do as humans right now on product discovery, customer discovery, but just in a loop of time with agents and humans.

02:12:26 - Brandon Hancock
▶ I always like to say, if I can't, in two sentences, describe how my customers are going to make a stupid amount of money, that's always a red flag. But if I can describe it in a sentence or two of how my end user is either going to make a ton of money or save a ridiculous amount of time, then I'm like, okay, cool. It's time or money, time or money.

---

<!--SEGMENT
topic: Morgan's cemetery management SaaS demo and business strategy
speakers: Morgan Cook, Brandon Hancock, Ty Wells, Patrick Chouinard
keywords: cemetery management, D3.js, GIS, multi-tenant, Freedom of Information Act, Utah, Supabase, Vercel, SOC 2, HIPAA, compliance software, TinySeed, go-to-market, legacy software
summary: Morgan demos a cemetery management system featuring D3.js hierarchy and radial tree visualizations of burial plot structures, public search, and a Freedom of Information Act-compliant request workflow for Utah counties. Brandon and Ty enthusiastically identify it as a high-value compliance SaaS targeting legacy software incumbents, urging Morgan to sprint to first paying customer, pursue SOC 2 and HIPAA compliance via Supabase and Vercel, and consider seed funding through TinySeed or similar.
-->

02:21:10 - Morgan Cook
I do have one project that I'm working on heavily. It's a cemetery management system. And, you know, like you were just talking about with artifacts, these guys have a very specific government requirement for anytime they release information — it has to be through their state's mode of basically like a Freedom of Information Act. And so nothing's out there right now that supports that. So I'm going to put that together for them.

02:21:53 - Morgan Cook
I used the D3 [tool:D3.js] diagramming, which is a library for visualization of layers. And it was pretty cool. I have it in three different modes.

02:22:29 - Morgan Cook
So this is the main set. The users — any public — it's a multi-tenant also because all the counties are separate individual entities. But the individuals that want to come and actually look for somebody need to be able to search. And so the search is for all the cemeteries. So if I were to type in a name here — and sorry for Disney lovers, but Mickey died — and so it shows this, right? This is a mortuary — not a mortuary, but more or less a monument kind of thing where people can add their own photos and everything to it. And then it has a review process.

02:23:46 - Morgan Cook
So this shows the structure of the cemetery, right? From the cemetery to — in this case, they have sections and rows and lots. And then the individual plots. And the plot color has — it zooms in, and then each of the rows, and then each of the lots, and then the individual plot, and the plot info shows to the right here, so they can visually see it. And you can click to zoom back out. And then a radial tree — very similar structure.

02:27:17 - Morgan Cook
The data is a single table with a parent-child relationship within the table. So you have multi-level parent-child relationship in the structure, all the way down to the plot. And that was the thing that's different — one cemetery may have sections, rows, lots, and plots. Another one might have only lots and plots or some other thing that they have in there. So it's all structured based on the data that they're used to seeing.

02:28:07 - Brandon Hancock
The day and age of AI being the system of record is a huge moat. Because if you're just a wrapper around ChatGPT and there's no — why are they going to stick with you even if AI changes or gets cheaper or a competitor comes around? Like, if there's a better wrapper, you're gone. But if there's a huge system of record change, well, it's going to be a pain in the butt to go from record to record. So they stick.

▶ Second, there's a bunch of law changes. Any time a law changes or requires some complexity and you can twist the knife of being like, hey, this law goes into effect, but your current app is going to get you fined or you're going to have to hire two more people to just manually sit around all day and do this for you. Or you can just click the easy button and I have a subscription, $2,000 a month, whatever the number is, and I'll just do it for you.

02:30:28 - Brandon Hancock
What's going on in Morgan Land? I mean, what are we feeling? What's going on?

02:30:57 - Morgan Cook
On the business side of this, this is primarily for one county to get it launched, right? Because they have a need for it right now and they're going to pay for it right now. After that, though, because it has this specific requirement that the state requires for any kind of information request, then all the other counties — any state or county-run cemetery — will be of interest in having the system, right?

02:31:27 - Brandon Hancock
And I made sure that what I put in for the state was also applicable for any other kind of Freedom of Information type system because this one's specific for the state of Utah. And so they need a very specific structure for their Freedom of Information and the different rules that they have in their information request.

02:38:07 - Brandon Hancock
If I was you, I mean, final thing — this is, if you were to go through a software case study of a customer in pain, you're not giving like sugar cubes — this is a full-blown painkiller, like they're screaming in agony, because they're under the thumb of the law.

▶ So this is the perfect product, under the perfect circumstances, and now it's just like, seriously Morgan — don't sleep. Build this as quickly as possible, and just advertise like hell. Your go-to-market strategy over the next month — I'm saying, seriously, this is a month sprint that could seriously change the trajectory of your life.

02:45:10 - Brandon Hancock
<Q>I don't know if you're dealing with HIPAA, because it's kind of people's stuff, but it's not people's stuff. It's a weird gray line. If you are going to have to go down that path, happy to — I mean, I'm doing it as we speak.</Q>

02:45:18 - Brandon Hancock
<A>You're going to pay $600 a month to get the Supabase [tool:Supabase] instance that's HIPAA and SOC 2 compliant. You're going to pay the $100 static fee for Vercel [tool:Vercel] to get a static IP. Like, it's not an insane amount of money, but it's going to be more expensive. But the playbook's there. And it's just like literally a month heads down. This is the only thing you focus on. You can knock these out. Once again, it's the moat that's going to prevent anyone else from competing with you.</A>

02:49:30 - Brandon Hancock
▶ As soon as that happens, please let me know, and really — either TinySeed [tool:TinySeed] or something like that — money was given, and it has been an absolute lifesaver. And if I build fast enough, I'm going to get more contracts, and it'll just instantly replenish. So that's where you're at. So I would be very happy — as soon as dollars need to trade hands, if you can make that happen in a week or two, seriously, would love to introduce you, just because this is the exact type of business that every investor wants to invest in.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not supplied):

- **Jaylen.Davis** — passed through unchanged
- **Rag Ch** — passed through unchanged
- **Ryan - One Stop Creative Agency** — passed through unchanged
- **elijah stambaugh** — passed through unchanged
- **Paul Miller** — passed through unchanged
- **Darryl Goldstein** — passed through unchanged
- **Juan Torres** — passed through unchanged
- **Morgan Cook** — passed through unchanged
- **Scott Rippey | @scottmichaelmedia | scottmichaelmedia.com** — passed through unchanged

*(No SPEAKER_ALIASES map was provided in the context block, so all speakers are passed through as-is.)*