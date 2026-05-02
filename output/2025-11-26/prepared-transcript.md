=== SESSION ===
date: Unknown (Tuesday, pre-Thanksgiving)
duration_estimate: ~2 hours 20 minutes
main_themes: Client proposals and sales pipeline, AI coding tools comparison (Claude Code, Anti-Gravity, Codex, Cursor), community GitHub repository launch, documentation strategy, AI video generation monetization, web scraping, Docploy self-hosting, Stripe payments, Git worktrees, Gemini deep research, HTML presentations as PowerPoint replacement

---

<!--SEGMENT
topic: Session Opening and Community Project Intro
speakers: Patrick Chouinard, alexrojas, Morgan Cook, Ty Wells, Brandon Hancock, Marc Juretus, Paul Miller
keywords: community repository, GitHub, Git workflow, fork, clone, branch, ShipKit, custom GPT, VibeCoding, pull request, automation scripts
summary: The session opens with casual chat before Patrick Chouinard introduces two pull requests he has submitted to the new ShipKit community GitHub repository. The first is a set of cross-platform scripts (Mac, Linux, Windows) to automate the Git fork-clone-branch workflow for contributors, and the second is his custom GPT agent configuration. Brandon Hancock confirms the repo is open and high-trust, encouraging contributions.
-->

00:04:59 - Patrick Chouinard
Thank you.

00:05:35 - alexrojas
How's it going, Patrick?

00:05:36 - Morgan Cook
Good, good.

00:05:39 - Patrick Chouinard
Seems to be a big week for Brendan if I look at all the videos that are coming out.

00:05:46 - Morgan Cook
Always, every week.

00:05:47 - alexrojas
Big week for you, Patrick.

00:05:52 - Ty Wells
Brendan's calling you out.

00:06:05 - Ty Wells
Yeah, think you talked about the community, community project.

00:06:14 - Patrick Chouinard
Yeah, yeah, the community project, that's right. Yep. Well, I think we've all talked about it a little bit last week, but yeah, it gave an idea in the Discord server and seems to have an interest in making it real. And it just created it. So I already have my two first pull requests waiting for his approval.

00:06:36 - Ty Wells
Nice.

00:06:42 - Patrick Chouinard
Yeah, basically, I was looking at the community project and I saw his documentation about how to upload or how to push to the community project and realized that a lot of VibeCoder might not have the habit of using Git in that way. So my first push is a set of scripts, one for Mac, one for Linux, one for Windows, that would actually automate the fork, clone, branch.

00:07:15 - Patrick Chouinard
Yeah, just like to remove friction for entry in any of those situations.

00:07:23 - Ty Wells
That's always a bonus.

00:07:30 - Patrick Chouinard
And I've also proposed the push of all the GPT agent, the custom GPT [tool:custom GPT] file that I've talked about a couple of times. Well, this is the second project I proposed to push to the community repo.

00:07:47 - Ty Wells
Keep them coming. Keep them coming. We'll soak them up.

00:08:09 - Marc Juretus
I'm in an interrogation room, man.

00:08:13 - Marc Juretus
Nah, I got a weird light setup. I got like a desk lamp that goes that way.

00:08:34 - Marc Juretus
So I'm not Two-Face from Batman, brother.

00:08:51 - Marc Juretus
A friend of mine, I used to do TV Extra work when they filmed the one with Bane. He went down in Pittsburgh for the fight scene. He was down there for like three or four days. He paid completely out of pocket for that, just to be in that movie.

00:09:21 - Paul Miller
Now the one I almost did, like I've been in a bunch of movies as an extra. The one I almost did was Captain America. That was down in Washington because I'm a huge Captain America, Spider-Man fan.

00:09:45 - Brandon Hancock
Well, hey guys, I hope everyone's having an awesome Tuesday so far. We're going to take a quick screenshot so that we got the order going in.

---

<!--SEGMENT
topic: AI Video Generator and Black Friday Course Deals
speakers: Brandon Hancock
keywords: AI video generation, Kling, Sora, video editor, Black Friday, courses, ShipKit, source code, GitHub, subscriptions, tax write-off
summary: Brandon Hancock previews an upcoming tutorial video on an AI video generator he has been building, noting it produces a two-minute video for roughly $7–$10. He also teases a Black Friday video breaking down courses he has purchased throughout his development career, and reminds members that buying annual software subscriptions before year-end is a useful tax strategy.
-->

00:09:49 - Brandon Hancock
And then while I'm pasting this in the chat real fast, guys, the AI video generator [tool:AI video generator]. So like recording it, I'm almost done. I got like an hour, two hours left of recording and it'll be good to go. But I'm a nerd and I'm absolutely loving how well it's actually like spitting out these videos. So I'm excited for you guys. I'll actually, I'll probably try and, well, it'll come out tomorrow morning. So I'll share the source code and everything as soon as it comes out. But yeah, for like seven, ten bucks, you get to create like a two-minute video. And it's just, obviously it's not insanely cheap, but the fact that that's even possible, cause like obviously back in the day, like you're paying a video editor and it's taking a month to get a two-minute video. And now it's, now it's, you know, in 20 minutes, you got a whole video, which is crazy. So I'll be sharing that out.

00:10:45 - Brandon Hancock
Yeah, those are most of the big updates on my side. So just going to keep, that video coming out tomorrow, recording another video where basically breaking down Black Friday deals, but in a different way. What I mean by that is like most people, like obviously Black Friday, cool, get gadgets at a discount. But like one of the big cheat codes I always like to do is buy courses. So I'm just going to break down all the courses I've ever bought during my like development career just to help out. I'll just break it all down just so you guys can kind of see like, hey, if you're interested in marketing, coding, mind to anything, these are the courses I bought over the years just so you guys get to kind of keep a lookout for those.

00:11:27 - Brandon Hancock
But that's everything on my side. So we'll kick it off with Alex. You're up first, buddy.

---

<!--SEGMENT
topic: Alex's Client Proposals — Lead Management and Legal Contracts
speakers: alexrojas, Brandon Hancock, Paul Miller
keywords: lead management, SMS follow-up, missed call automation, contractor, law firm, legal contracts, trigger.dev, ShipKit, Vercel, HTML pitch deck, Claude, proposal pricing, decision maker
summary: Alex Rojas shares two active client proposals: an SMS-based missed-call lead management system for contractors, and a contract generation tool for a law firm covering US, Canada, and Mexico. He demonstrates an interactive HTML pitch deck hosted on Vercel, built with Claude Code, and receives feedback from Brandon and Paul on removing overly technical database schema sections and identifying all decision-makers in the approval chain.
-->

00:11:35 - alexrojas
Hey, how you doing, guys? Yeah. Good to see you. Just, you know, like I'm in the middle of the selling process as we were discussing in the calls. Actually, today I'm sending this a second proposal. So just a bit of background for everyone. One of the projects that I am working on is in lead management, which attends like all the contractors. So what the app wants to do is like to answer through SMS. Every time there is an incoming call, that is a missed call, then the program detects the missed call and then gives follow up and try to make a booking for the contractor. That is one.

00:12:24 - alexrojas
And the other one is legal. So making like there's 10 types of contracts and they are contracts in Mexico, Canada, and the US. So you can like play around those types of combinations. And that is also like that is for a lawyer firm. And we are doing both in trigger.dev [tool:trigger.dev] as much as I can, because that's my favorite template of ShipKit [tool:ShipKit]. And yeah, you know, so I'm just in the waiting period. I have calls on Friday and on Thursday. And I just wanted to share with everyone that I've been doing, like, working with Claude Code [tool:Claude Code], these proposals in HTML, which is pretty, pretty cool.

00:13:38 - alexrojas
Okay, so this is for the company that it's in the contractor lead. You guys can see my screen, right? Yeah. Okay, so I just sent this, I put it in Vercel [tool:Vercel], so it's quite easy. It's just a link, and here we have the pitch deck, which talks about the general part, you know, executive summary, kind of like how it works, flows, I'll just scroll through it really quick, product vision, pricing, man, for $800.

00:14:16 - alexrojas
Yeah, yeah. Here we have features, kind of metrics of what we're getting, you know, but the cool stuff is that if you want to get more specialized, this one doesn't have the index, but here you can see the technical architecture that we might, that we're going to have in terms of stage. You know, I just find it really cool. Like if you want to be really more specific in one area. Yeah, like two-week timeline and, you know, like it provides a space for the client to see and see what they really like.

00:15:09 - alexrojas
That's a cool way to do contracts.

00:15:11 - Brandon Hancock
That's very cool. I'm curious to see the response of this of like, wait, what am I looking at? And then they click in it and be like, oh, this is nice. That's very cool.

00:15:26 - alexrojas
Yeah. So yeah, the other one, this is exactly the same. We have these three options and, you know, it's like a, I'll just keep in that and see how clients react. But yeah, for the lawyer, I am almost doubling the price.

00:15:40 - alexrojas
Yeah. I know they're going to be more of a pain in the ass.

00:15:46 - Brandon Hancock
Yeah. Yeah. The crazy part is, even if you double to like the 96, they're still going to be like, okay, you know, just because.

00:16:03 - Brandon Hancock
I loved how it was broken up. The database, yeah, solve rich people problems. Patrick nailed it.

00:16:13 - Brandon Hancock
Only quick two cents I would give. I know it started to go a little bit deep into database schemas. I might drop that just because it's kind of like almost speaking a foreign language to someone else. So I might drop the highly technical stuff, but the high level, what we're going to do just so they can look at it is super helpful. Like, hey, we're going to use this tech stack. It's a super standard tech stack. We're going to do this. This is also, you know, just high level. And the flow map's beautiful. So that's what I would look at. And I'll go ahead and tell you right now, the database schema is going to change. Like, you're going to show that and then instantly as you go to build, it's going to instantly change. So it's like, you know, it's going to confuse them and it's going to change. So it's like, eh, we'll just leave it out. But everything else, beautiful. Absolutely loved it.

▶ 00:16:57 - alexrojas
Yeah, definitely is going out.

00:17:22 - Paul Miller
Pardon me, trying to eat lunch at the same time, really rude. My question per the text comment, I would ask the question, who are the deciders in the client end? Because while you've got your key point person who might be a commercial person, depending on the size of the organisation, they've got the right to, fully got the approval concern in the one person. But if it's more than one person, and the components of the other people, what they need might need some addendum documents.

▶ 00:18:03 - Paul Miller
So I agree with Brandon, you know, you probably don't want to put the database schema in the core proposal document, but you may want to add it in the addendum document and think about, well, who is the audience, who is the committee that decides or approves this?

00:18:46 - Paul Miller
Just get that context. Because you kind of, the document might have to be many things to many people, and that makes it a little bit more complicated than the base approval document.

00:19:00 - alexrojas
Yeah, yeah. Yeah, I'll definitely take into consideration that the good thing of this is like, even though it's a law firm, this is one of the partners that it's doing this as a side piece, because he also doesn't want to put his name like saying like, oh, this is like, we guarantee this is going to be like the real deal. So he's just like, also like, putting in a different name and just having that. So the good thing is that I'm dealing with one decision maker as of now.

00:19:29 - Paul Miller
Yeah, but the only challenge, having once worked for Ernst & Young, it was, oh, it's just one firm. It's a one firm with 10,000 partners globally, all of which are legally obligated to themselves. So when you're dealing with a legal partner, if it's a legal partnership, he's obligated to get one of the other partners to co-sign it and to vet and approve it. So you kind of got to have it, you've got to think about that format, even though you're saying, oh, one. Yeah, yeah, no, no, we're just doing a side thing, and just give us a quote, justify it, but yeah, think about those anomalies, because the money is great with those guys, you know, they can see the value because they understand time, and the value of time because they bill per minute.

00:20:18 - alexrojas
The many heads of the snake, need to consider them all.

00:20:27 - Brandon Hancock
Yeah, yeah. Dude, please keep us posted, and I'm excited to hopefully have some money hitting the bank account soon, so we're rooting for you, buddy.

---

<!--SEGMENT
topic: Marc's Custom Shopper with Anti-Gravity and Image Generation
speakers: Marc Juretus, Brandon Hancock, alexrojas
keywords: Anti-Gravity, Cursor, Playwright, web scraping, browser automation, screenshot, scroll, ChatGPT, Google Gemini, image generation, OpenAI API, Google Cloud, Claude Code, Sonnet, Opus
summary: Marc Juretus describes building a custom web shopper using Anti-Gravity that scrapes multiple sites, evaluates items against criteria, and serves results on a Next.js page. Brandon advises treating the browser as a web driver with sequential prompting rather than per-image API calls. The conversation broadens to image generation pricing, with Brandon explaining his use of a Google Cloud API key at $0.14 per image as an alternative to subscription caps. Alex asks for a quick explainer on Anti-Gravity versus Cursor.
-->

00:20:46 - Marc Juretus
Not as much cool stuff as you nerds up here, but I've been doing some stuff. But no, seriously, the last thing I've been playing with is Anti-Gravity [tool:Anti-Gravity]. So, I downloaded it. I've been using it. So, I've been trying to make a custom shopper that goes to a variety of sites, pulls down, and tries to meet the criteria of what I'm looking for and sends me an email and also serves up a Next.js [tool:Next.js] page I can go. So I was able to do it with one site. I actually like the IDE. It's pretty cool. You do run out and you got to switch to another model. I did notice with that pretty quickly.

00:21:24 - Marc Juretus
So I'm trying to figure out my logic where it comes in and pulls in all the images from the pages I have it go to. And then it determines if it meets the criteria. <Q>If you did a shopper or something, Brandon, would you do something where you were using a description or would you have the AI read in all the images from the page and then take a look at each image and see what it seems like? Say, hey, I'm looking for a black shirt that's a V-neck. Would you go that approach or would you go strictly description?</Q>

00:21:51 - Brandon Hancock
<A>I mean, so the cool part is with Anti-Gravity, I mean, it can look at the whole page. So I would actually just do page views. Because if not, imagine there's 12 images on the page, that's 12 calls or 12 lookup calls. So I would just say, look at the page as a whole to try and find that black shirt. If you don't find said black shirt, keep scrolling down. Because if you hop into Anti-Gravity and say, hey, what are your browser tool calls? Like what do you have available? It'll list them all down. And then those are your constraints. So that's how I would tackle it to say, oh, I can see you have scroll, screenshot, and navigate and click. So knowing those are your constraints, I would then basically, you know, kind of go through the process of creating a master web page scraper prompt, where it has basically instructions like, hey, phase one, I'm going to give you an input phase and a website. And phase two, it is your job to start to scroll through and navigate the page logically using scroll, scrolls, click, screenshot, and everything else until you find it. As soon as you find it, here's what step three is, and here's what step four is. That's how I would tackle it.</A>

00:23:10 - Marc Juretus
Like, almost like here. So use a description and try to find what you're looking for. Then if it meets that, then read the image and then take it further.

00:23:24 - Brandon Hancock
The other way, Marc, that I like to do is treat it as a web driver. However, so for example, what you could do is just say, hey, here's my four-step high-level process. I'm going to have you do it. I'm going to tell you the commands to do so you can get experience doing it once. And then after you go through the process with me, save all the instructions. So here's what that would look like. You would say, hey, Anti-Gravity, open the browser and go to amazon.com. Now we're looking for a black shirt. So click in the search bar and go look for search black shirt. And scroll down until you find one. Fantastic. Take another screenshot. You can see, we can see it. Now click in, get as much information as you can, and move to the next step where we're going to write an email. So you can literally, you should never interact with a browser. All you should do is talk to Anti-Gravity, have it record the process, and then say, hey, what we just did, save it as a prompt because this is going to be your standard operating procedure for doing this in the future, is how I would tackle it.

00:24:47 - Marc Juretus
That's what I'm using, I'm using Playwright [tool:Playwright]. Playwright's what's actually pulling the page up and reading through it and then scrubbing the images. That's what I'm using for that.

▶ 00:25:06 - Brandon Hancock
Yeah, I would 100% then do, I think Cursor [tool:Cursor], you'll have great experience. Heck, you could even do it with Claude Code [tool:Claude Code] because at the end of the day, we have an agent who has a browser tool and the browser tool is going to go find everything you need. So any of those three tools can do exactly what you want.

00:25:34 - Brandon Hancock
But yeah, Claude Code guys, $100 plan. You can basically do whatever you want. It's not real. Really? Yeah. I mean, it's doing the Pokemon generation stuff and it's crazy because it's very similar to what you're doing, but it's just a lot longer. What I mean by that is at certain points, you'll see Claude Code go off and I'm in love at this point because it will understand I need to go generate 25 different images and you'll just see it run for 10 minutes. And it, unfortunately. Understand it's keeping track of what it needs to do and it stays on track. That's the part that's crazy. You'll hear AI is getting better at performing one longer job running for a very long time and staying on track. And I can confirm, like, flawed, especially, you know, Sonnet [tool:Claude Sonnet], Opus [tool:Claude Opus] can do it too. The new model they just dropped. I actually got, I don't know if you guys saw it, but their API, like their status, they've had huge issues right now. I think everyone's blowing up Opus. So even though it just came out, you kind of can't use it. At least as of two hours ago, I was having trouble.

00:26:39 - Marc Juretus
Like I do that once in a while, but I always run out like four images in either pay for ChatGPT [tool:ChatGPT]. What is the way that you do it that say you leverage what you're paying for, like with an OpenAI key or Google Gemini key? Like I've been using the vertical. What is, what's the one with Google where you can use Nano Banana? I've been using that off of my phone to generate images. Is there anything else that you would recommend? Like, say you were just, hey, I need to do another five images. I don't want to pay for ChatGPT. Maybe I can leverage one of my keys.

00:27:08 - Brandon Hancock
Yeah, so here's all of my subscriptions. $20 a month, ChatGPT, 20, Gemini [tool:Google Gemini], 100, Claude Code, Cursor, I think I have Cursor 20. That's my entire, those are all of my subscriptions. So, but when it comes to image generation, I mean, I'm actually hooked up to, in addition to the $20 a month plan, you know, I'm using, I have an actual Google Cloud project [tool:Google Cloud]. That project has an API key. So technically, I never run out of the ability to make images inside of their AI Studio [tool:Google AI Studio] because I'm paying the 14 cent per image, which is, you know, all I'm doing is image generation. Hey, that's much better than the paying 20, 60, 200 bucks, you know? So that's how I'm at least doing image generation is that way. Just paying for it straight up.

00:28:28 - alexrojas
Is it like Cursor but with agentic rules instead, like fully agentic instead of, but it's like editor, like Cursor, competitor?

00:28:43 - Marc Juretus
Yep.

▶ 00:28:44 - Brandon Hancock
It's literally Cursor, just Google made it. It's the best way I would describe it.

00:28:53 - alexrojas
Very generous, free tier.

00:28:56 - Brandon Hancock
I do like the browser window, though. That's pretty cool. They do, but it's not as good. Like what they've done, what they've done is when it comes to browser, it is the best browser experience, personally. But, you know, the kicker is if you're hardcore developing, man, that 50 credit, that 50 request for five hours kind of runs up quickly.

00:29:29 - Brandon Hancock
So I like to, I like to do it for one or two big tasks. And then I'm like, well, I kind of, I'm shot. I have to go back to Cursor, Claude Code. So I'm personally, I'm hopping between all of these constantly, just depending on what I'm trying to do.

---

<!--SEGMENT
topic: AI Model Consistency and Tool Workflow Discussion
speakers: Brandon Hancock, AbdulShakur Abdullah, Marc Juretus, Paul Miller
keywords: Claude Code, Anti-Gravity, Gemini 3, Claude Opus, Claude Sonnet, consistency, context engineering, task templates, plan mode, Anthropic, shiny object syndrome, subscriptions
summary: AbdulShakur Abdullah raises concerns about consistency in the new Gemini 3.0 model. Brandon attributes his positive experience to always providing maximum context via structured task templates. The group discusses the temptation of switching to new tools (Anti-Gravity, Gemini) versus staying productive in Claude Code. Paul Miller asks whether Anti-Gravity is mature enough to replace his current Claude Code workflow, and Brandon confirms Claude Code remains his primary tool at 80–90% usage.
-->

00:31:36 - Brandon Hancock
Abdul, I saw you had a quick question about consistency. If you want to hop on real fast.

00:32:11 - AbdulShakur Abdullah
I was just asking about a consistency that I've heard that the new 3.0 model is not as consistent. Sometimes it just makes, it either does it like beautifully or it just does weird errors.

00:32:25 - Brandon Hancock
<A>So far, personal experience, I've seen it be pretty consistent. I haven't had any issues, but like, you know, I'm, I think one thing I will always mention is just like, I'm always doing maximum context when I'm solving problems. I would be very curious if other people when they're like, oh, it's hit or miss. I would just love to see their workflow because like, I feel like we're very structured with like task templates and everything to always give it maximum context to do a task. So my experience has been nothing, but so far pretty good.</A>

00:32:57 - AbdulShakur Abdullah
<Q>So you're not going to change your workflow? Blow from Claude Code and Cursor to Anti-Gravity?</Q>

00:33:05 - Brandon Hancock
<A>So the way I'm doing it right now, I'm hopping between Claude Code and Anti-Gravity. So I'm using Anti-Gravity mostly for experimenting right now. Like I have Claude Code. Claude Code's crushing it. Like I'm not leaving Claude Code right now. I mean, just because strictly because I'm churning out so much stuff. The 50 cap, I'm just going to run past it instantly. I literally am just doing it for more experimenting just to kind of keep my pulse on the Google models and Anti-Gravity. Just because I always run out of credits is kind of my issue. But yeah, so far I've not had any consistency issues.</A>

00:33:54 - Ty Wells
Hey, guys. What am I working on? I'm working on two projects this week. One is I'm doing some gifts for my family for the holidays. I'm giving them a preloaded Fire Stick [tool:Amazon Fire Stick] with a preloaded Android app on it, and they can turn any TV into a digital frame. So they can add photos, and they can authorize other people in their family to add photos so they can take it on the go.

00:34:49 - Ty Wells
Yeah, just a little, you know, 20 bucks for a Fire Stick on Black Friday, and just the software to run it, host all their pictures. Because we bought a digital frame and we notice everybody just watches the pictures when they come over. That's all they're doing. They're watching the pictures. So we're going to give them their own digital frame.

00:35:41 - Ty Wells
The other one is actually a ShipKit one, but it's not ready yet.

00:35:47 - Brandon Hancock
Oh, you got me interested. What we got?

00:35:48 - Ty Wells
It's actually a ShipKit one. I think you guys are going to like that one.

00:35:53 - Brandon Hancock
Any teasers you can drop?

00:35:53 - Ty Wells
Let's just say I've taken Patrick's idea and 10X'd it.

00:36:01 - Brandon Hancock
Oh, some competition.

00:36:19 - Brandon Hancock
Do you think we'll have a demo Tuesday? Next Tuesday?

00:36:21 - Ty Wells
Yeah, yeah, for sure.

00:38:51 - Paul Miller
So I made the move to Claude Code, and then, oh, God, you have to put the bloomin' Anti-Gravity up there. So, look, can I have some guidance? Because it took me ages to get to Claude Code. I do not want to move to the new shiny thing, you guys can be on the bleeding edge. I love the video, Brandon. That was good. And I'm seeing positive things, people talking about Anti-Gravity. But am I right to assume it's still pretty early days? I know you were bold in saying, well, you were moving it to, but you're still very much into your Claude Code. <Q>Where would you position Anti-Gravity right at this time?</Q>

▶ 00:40:30 - Brandon Hancock
<A>Yeah, mean, so I'm, I mean, Claude Code is my primary, using it 80 to 90% of the time. I'm mostly just using Anti-Gravity for, like I was mentioning to Abdul earlier, just like, I want to continue testing with it. So like, every day I'm churning out code nonstop. So it's just like, every 10th time, I'm like, hey, let's just see what Anti-Gravity can do for this. But Claude Code is my primary mover for everything, genuinely everything at this point. And I literally, I never hit limits. Like that's the part that keeps blowing my mind for a hundred bucks. So, but yeah, but I agree. Shiny object, it's a real thing. And last week was Gemini. Now it's open. I swear we get no free time.</A>

---

<!--SEGMENT
topic: Documentation Strategy for Existing SaaS Codebase
speakers: Paul Miller, Brandon Hancock, Patrick Chouinard
keywords: documentation, GitHub Copilot, CI/CD pipeline, Mintlify, ShipKit generate-diagram prompt, Claude Code, Copilot CLI, markdown, automated documentation, pull request, code review, Confluence
summary: Paul Miller asks for recommendations on a documentation tool that integrates with GitHub, after years of undocumented institutional knowledge in a 10-year-old SaaS product. Patrick Chouinard recommends GitHub Copilot CLI in the CI/CD pipeline for automated documentation augmentation, and shares that the ShipKit "generate diagram" prompt produced 18,000 lines of documentation in a single two-hour Claude Code run. Brandon adds that Mintlify is used in their repo and describes a PR-triggered workflow that auto-proposes doc updates whenever code changes are merged.
-->

00:41:27 - Paul Miller
So for the day job, we grew our SaaS business. We're 10 years in. And we were working on the basis of a lot of knowledge and IP sits in the heads of pretty much our dev team hasn't gone anywhere. So that's still there. They're very loyal. We look after them. We feed and water them. But the thing that we haven't done a good job on is documentation. And documentation, of course, starts with good functional documentation, user documentation that flows into, or how does that tie into the app side of things. And we're wanting to implement a good documentation strategy. My initial logic, and using the wisdom of AI, of course, because AI solves all the world's issues, we're already using GitHub [tool:GitHub] for where the code is. It would be logical to tie in documentation alongside the code. <Q>What documentation tools, and not, look, we used Jira [tool:Jira], but Confluence [tool:Confluence], like we hated, we tried it a few years ago, it's terrible, it was expensive, and it was pretty useless. Does anyone use anything that ties nicely into GitHub on the documentation side of things that they've had experience with, or you would recommend?</Q>

00:43:08 - Brandon Hancock
I want to throw this to Patrick to see if he has ideas. But my quick initial question, though, is are you talking about, hey, I'm trying to keep up with the documentation for this issue before we actually start to kick off the work? Or are you saying like for all future work? Or are you talking about just like, no, I want to document the entire current stack?

00:43:30 - Paul Miller
Entire current stack. So the challenge that I've got that I'm trying to solve is the dev team has said the quality of the documentation around change that goes into a work request is not good enough. The problem is the people writing that request don't have enough information on what is the base process that they're trying, changing that they want to change. So you've got to say, well, component by component, let's start with looking at giving the depth of documentation to everything, but we'll start in certain sub-areas first.

00:44:35 - Patrick Chouinard
<A>Actually, Paul, what I've done internally for that, because we had the same issue, there's tons of third-party that developed for us, and there's an inconsistency in documentation. And honestly, GitHub Copilot [tool:GitHub Copilot] is quite good in there for some very simple reasons. First, it's a GitHub tool itself, so it's very well integrated. The agent already lives on the platform, and Copilot CLI [tool:GitHub Copilot CLI] is an awesome companion for your CI/CD pipeline to do automated documentation. So the first time when you have nothing, it might not be powerful enough automatically. One thing I found is one of the prompts from ShipKit, actually the generate diagram, is absolutely insane to create the first draft documentation if you have none in a project. But then you can easily craft a prompt to pass on to Copilot CLI called headless in your CI/CD pipeline to augment that existing document constantly every time you go through a check-in.</A>

00:45:58 - Brandon Hancock
Yeah, I want to add on to that real fast to share. Here we are, a Cray Repo. So right in the core crux of it, we have a Docs folder. So the Docs folder, under the hood, we use a tool called Mintlify [tool:Mintlify], and it's like a really nice way, it's like a beautiful document editor or document viewer. And what was really cool, the way we actually structured stuff, is just doubling down on what Patrick was sharing. But in our actual CI/CD pipeline, what we were doing is we actually, very similar to what Patrick was recommending, we would always have a PR, we would always have a crew, analyze the change. That change would then look at the corresponding section in the docs and recognize, did anything, is anything missing here? Because if it is, we now need to update it. So this is how we would, like, no one likes to write docs, you know, and sometimes, yes, it's important to, like, hey, the AI's not fully capturing it, but it was always a great first stab at making the document change. It would create a new PR to say, hey, based on this code issue that was just issued and merged in, here's a new issue to add in the appropriate docs to reflect this, the doc change to reflect the code changes. That way, they were both kind of living instances or living, you know, living pieces of code, but that's how we were tackling it.

▶ 00:47:46 - Brandon Hancock
But the core is just going back to what Patrick's saying is that initial document set, that, like, that has to exist. So just structuring that out is going to be the hard one. And I think it's literally called generate diagram is the markdown file. And that's the one that will actually do a lot of the heavy lifting.

00:48:07 - Patrick Chouinard
Basically, I've called it with a prompt asking it to crawl my entire repo, and it ran for literally two hours straight, and it pumped out about 18,000 lines of documentation in one year.

00:48:22 - Patrick Chouinard
That's crazy.

▶ 00:49:01 - Brandon Hancock
So this, the problem I want to like quickly just dive into with what you're about to do, Paul, what I would recommend for whoever is going to set up these initial docs, what I would recommend them to do is to go through the process once manually and kind of follow that master process I had in a Claude Code video where you basically manually do the task, then you have the AI watching, like you're having the AI do the task, so you're, and what you're going to do is start to say, great, so you saw how for this subsection of the code, this is what the inputs were, you saw all the custom instructions I did, and you have the final output. Now I want to start to replicate that process across all verticals of our code base, and what's nice about this is you only have to do the process once properly, then you can do it at scale with AI. So whoever is going to be doing this in your company, seriously, like that master video is what I would really recommend to do because like there's no reason they should be doing it more than once, especially when you know you're going to have do this 20 times or 15 times, however big the code base is. And once again, this is a phenomenal opportunity to use Claude Code. Heck, once you do it once, kick off 15 background jobs to do it for all the different verticals just to do it at scale.

---

<!--SEGMENT
topic: OpenAI Codex vs Claude Code — Model Comparison and Plan Mode
speakers: Andrew Nanton, Brandon Hancock, Juan Torres
keywords: Codex, Claude Code, Anthropic, OpenAI, PySide, GUI, plan mode, context engineering, vibe-coding, Claude Sonnet, GPT models, automation, markdown SOPs, AI workforce
summary: Andrew Nanton shares his experience switching from Claude Code to OpenAI Codex for a messy PySide GUI codebase, finding Codex more reliable for that specific project despite needing more explicit instructions. He notes the absence of a native plan mode in Codex, which he worked around by prompting it not to change code until a plan was confirmed. Brandon connects this to a Nate B. Jones YouTube analysis comparing OpenAI, Anthropic, and Google models. Juan Torres asks about automating recurring tasks, and Brandon describes his weekly practice of creating one new markdown SOP file to build an AI workforce.
-->

00:50:33 - Brandon Hancock
Real fast, Andrew brought up some cool points on using Codex [tool:OpenAI Codex]. I would love to hear your experience on Codex, Andrew, just because like I've just kind of fallen out of love with ChatGPT stuff. But hey, maybe you can turn me around, man.

00:50:51 - Andrew Nanton
No, so the problem I was running into was, so I really like Claude and Claude's my favorite model or like Anthropic's [tool:Anthropic]. My favorite provider. Yeah. Because I feel like in general, it knows what I mean rather than what I said, which I feel like the GPT models often need very, very explicit instructions to get the results that I want. And that can be good or bad, right? Like, I mean, that can work against you. But I was really, I was going back to my PySide [tool:PySide] local GUI application. And when I was asking Claude to work on it, Claude Code, it would, it just, it would make some progress, one step forward, two steps back. would break things, you know, it just was never really getting the results that I wanted. And I thought, well, okay, you know, I, that's why I only sign up for a month at a time for these things, because they change so fast. And I'd heard some pretty good things about Codex. So I thought, okay, I'll give that a shot. And I did definitely have to give it more information. I mean, it took more hand-holding before I kind of gave it a task, but on that code base that, you know, was largely vibe-coded, and I'll tell you, it's kind of a mess, Codex was just nailing it every time. I mean, I would give it a, you know, fairly complicated task. I almost always follow up with something like, ask me, you know, for any clarification if something's not apparent, and that prevents it from making really kind of boneheaded assumptions about things. I used it a bunch last month, and it got great results. I really missed Claude's planning mode, but it's worth a look if you're banging your head against something that Claude is not doing a good job with. It's worth a try.

00:52:50 - Brandon Hancock
It's so funny you said that, because as you were talking, I was like, does Codex have a plan mode? Because I was like, that's one of my favorite features of Claude Code. Because it helps keep it on track and really define like, hey, I want to make sure that we are clear on these four points before I proceed. So that's interesting that they don't have that. It seems like a no-brainer.

00:53:14 - Andrew Nanton
Maybe they've added it. It's been a few weeks. I've just been totally swamped and traveling a lot with work. But I was kind of doing a, you know, dollar store plan mode by saying, you know, don't change any code yet. You know, show me a plan or, you know, show me exactly what you plan to do before you change any code. And it will do that. But I mean, it just needs plan mode. It's clearly the way to go.

00:53:53 - Brandon Hancock
Real fast, Juan, if you want to go and then I want to share, talk about a quick video that I just pasted in chat.

00:53:58 - Juan Torres
I just wanted to ask, when you, I've been trying to implement your modus operandi of just every time you have to find a way to automate a procedure in your whole code pipeline. I try to put it on the, you know, rules and commands with Cursor. But is that usually what you do, when you find that you have to automate specific tasks, you just put it under those specific MDs or what else do you do?

▶ 00:54:27 - Brandon Hancock
<A>Yeah, it is, it is strictly I'm creating constantly like once a week. I'm like, my goal every week is to automate a new task. I don't know what it is, but I just know every week I'm going to build a new AI employee, which means I'm going to create a new markdown file, which has just a bunch of standard operating procedures of like, here's what I'm going to give you as the input. Here's the seven steps I want you to follow. And step two, I definitely need to be involved for some human in the loop to confirm your decision before you go through the next five steps. But that's constantly what I'm doing. So for my email autoresponder, it knows how to read my inbox. It knows how to respond. It knows how to, you know, it does everything that I want. So every week I'm just creating one new markdown file to help automate something in one of my businesses is how I'm tackling it. And it's crazy, guys. Like after, you know, doing this for a month or two, you end up basically building out a small AI workforce. Like it's crazy. And then you eventually just like, man, like I'm moving so fast. Like it kind of frees up your mind to like, well, what are the next big things? So it's crazy what happens when you get rid of all the busy work, what starts to happen.</A>

00:55:35 - Brandon Hancock
And really, really fast, I want to drop two things. I just dropped a YouTube video in the chat. His name's Nate B. Jones [link:Nate B. Jones YouTube channel]. Phenomenal breakdown of more deep dive engineering models. And it really is all things AI. So if you get a chance to check out his channel, I've been absolutely loving it. And he covered that exact topic that we were just, Andrew, you kind of brought up with going through, you know, the OpenAI models versus the Claude models versus the Google models and did a really good analysis. And the core takeaway, actually, Andrew, you should make your videos because your conclusion was very similar to his. ChatGPT is phenomenal. If you give it perfect instructions, it just doesn't. It is phenomenal at it. It was the saying for Anthropic, it was okay with working with unstructured, messy stuff. Like, it would just still do its best. But Gemini was kind of in the middle on, like, solving bigger problems and still working through it. So he had a very similar breakdown to what you said, Andrew. So I think it's kind of becoming apparent, like, each one fits a different type of problem at this point.

▶ 00:56:54 - Brandon Hancock
Second thing, I just thought of this. I probably need to mention this to everybody. Going back to how I was going to make a Black Friday video. Seriously, if you guys have businesses, I definitely recommend. This is the time of the year to buy annual subscriptions to everything to reduce your tax burden. I just literally reminder to myself, I have so many subscriptions to annually buy after this, so I'm probably going to go all in on the Claude Code for the year, just because I'm going to pay anyway, might as well get the tax write-off.

---

<!--SEGMENT
topic: Claude Opus 4.5 Release and Claude Code Usage Limits
speakers: HP (Scott), Brandon Hancock
keywords: Claude Opus 4.5, Claude Sonnet 4.5, Claude Code, Anthropic, usage limits, model caps, status page, thinking mode, agentic behavior, API status, Git worktrees, Supabase
summary: Scott (HP) reports that Anthropic released Claude Opus 4.5 with significantly relaxed usage caps, which he has been using heavily since the previous day with only 10% of his weekly limit consumed. He and Brandon discuss the confusing way Anthropic presents Opus versus Sonnet usage quotas. Scott also shares the Anthropic status page (status.claude.com) as a useful tool for diagnosing API outages, and asks Brandon about a Git worktrees tutorial he had mentioned previously.
-->

00:57:30 - HP
Yeah, yeah. Yeah, I just got probably just a couple comments, and then I had one quick question for you. But yeah, it was so funny, because we were on the ShipKit call yesterday, and I literally got back to my desk, and all of a sudden, I realized Opus 4.5 [tool:Claude Opus 4.5] came out, and I'm getting all the videos, and I was on it already in Claude Code, and I'm like, what's happening? Like, I've been, I mean, because I used to use Opus 4.1, like, I don't care what anybody says, Sonnet 4.5 was a great leap forward, and with Thinking Mode, it was great at coding, but there were still some things that I needed to use Opus for. It is better, but it was like they capped us so hard I could run through it in like an afternoon. It was so bad. And I've been in it like this is great. They listened. They need to keep it this way. They better because I even filled out a survey once and I said, I'm like, we need more Opus. What are you doing to us? I'm like, you know, and I've been in it. I mean, I'm at 10% usage for the week in all models and have touched Sonnet 1%. That still won't move if I'm in Opus the whole time. And I've been in it since yesterday. So the limit is really, really good. And I'm loving it. It's like kicking off its own agents to like go explore code bases and everything. Like it's really got some cool agentic stuff in it that I've noticed that's by default, that's a lot different.

00:58:44 - Brandon Hancock
Do you, what is, I just saw this note because it came out, what, yesterday? Yeah. So we've increased your limits and removed the Opus cap. So here was my question because I just haven't had enough time to research it today. So for Opus, we basically, like it, it looked like in the past, you know, it was, you had a Sonnet option and then down here you had an Opus one. And with Opus, like you're saying, Scott, like you would use it six times and it's like, oh, you're done.

00:59:14 - HP
Now it seems like all models is taking Opus and Sonnet usage, but yet it's really confusing how they do this. I wish they would give you Opus and Sonnet and that's it. And you could see it, right? It makes no sense to me how they lump it. So it's like they switched it around. So the Sonnet only is the Sonnet only, but I know that counts towards all models, but I'm like, where in there does my Opus run out? So I'm a little confused about that too.

00:59:57 - HP
This status.claude.com [link:status.claude.com]. This is how I, like, and you can sign up for email alerts, but, like, anytime there's any issues with any of the API or code or AI, like, I just know. I'm like, if I'm starting to get funky things, I go here, like, that issue that happened today, I was like, oh, man, and I went and looked, and I'm like, oh, yeah, I'm just going to wait until I see they've put a fix in place in their monitoring. When they do, I test it. Oh, if it works, I keep working. If not, I wait until they say it's resolved. So that's a handy little thing if nobody's seen that.

▶ 01:01:23 - Brandon Hancock
But basically there was a really cool video where, yeah, worktrees. And I figure people might like that one anyway, if they want to get into it. Yeah. But yeah, long story short, guys, there's a, if you're not, there's a, there's a concept called worktrees [tool:Git worktrees] with Git. So it basically almost creates a second version of your project. But what's awesome about it is you can actually work on projects to where they don't conflict with each other. So like each feature, instead of getting a branch, well, you can only have one branch checked out at a time. But what's nice is you can have infinite number of worktrees to where you can actively almost spin up the code, have it working in multiple different areas.

01:02:04 - HP
I actually saw you can connect it. And so you can do like a dev version of your database we were talking about too. And I'm like, my brain's like, I need to figure this out.

---

<!--SEGMENT
topic: ShipKit Community Repo Merge and Gemini Deep Research Demo
speakers: Patrick Chouinard, Brandon Hancock, Paul Miller
keywords: ShipKit community repository, GitHub, Anti-Gravity, Gemini CLI, Gemini 3 Pro, deep research, web search, school community, sequential questioning, prompt engineering, custom GPT, pull request, bootstrap script
summary: Brandon merges Patrick's two pull requests live: cross-platform Git bootstrap scripts and a custom GPT configuration. Patrick then demonstrates using Gemini 3 Pro CLI to crawl the ShipKit school community, surface the top 10 AI development questions, and generate a fully cited, post-ready answer — all in a single three-minute session. Brandon shares a parallel use case where he used the same Gemini deep-research approach to find fire chiefs across multiple US cities at scale.
-->

01:05:53 - Brandon Hancock
I think next up, going back to our picture, it goes Patrick. Patrick, you're up next, man.

01:06:01 - Patrick Chouinard
Yep. So, by the way, thank you for the community repo.

01:06:07 - Brandon Hancock
It's so funny, Patrick, because I can't remember what day I did it this week, but I was like, I have to step up for Patrick. Patrick's crushing it. I have to match Patrick's energy. So I have my list, I swear it never shrinks, but I was like, I got to shuffle stuff. Patrick needs me. So, yeah, so I had to come through on that.

01:06:29 - Patrick Chouinard
But great idea. And if you look at it, you're going to see that there's two pull requests waiting for your approval.

01:06:35 - Brandon Hancock
Oh, okay. So the way it's made, Patrick, just go ahead and push or pull. I made it to where there's no restrictions, just because I want you guys to, like, everyone has their own little folder, and it's a great way just to make sure everyone gets to contribute, just because, like, so far, everyone has been super respectful in the community. Thank you all for being phenomenal. So, I just, like, why we still have, like, high trust, high trust community, like, you. Thank you. Everyone just do your own stuff.

01:07:00 - Patrick Chouinard
Now that I say that, though, someone's going to come in and be like, delete.

01:07:09 - Patrick Chouinard
No, but basically, the two things that I created, the first one is I took your quick start guide, which basically you said how you want people to interact with the community, the repo. And I actually tried Anti-Gravity to use that script to actually create a script first in ZSH to basically implement the quick start. So it does the forking, it does the branching, everything. So you have a script that bootstraps your interaction with the community, and then I actually asked Anti-Gravity to create the Linux version and the PowerShell. The reason why I split Mac and Linux is because that script doesn't only manage that part, but it also manages the installation of every component needed. On Mac, it will update through, it will install the GitHub CLI [tool:GitHub CLI], all of those things. Same thing on the other platform. So basically, it's a one-stop shop. You run it, you give it your name, and you give it your project name, and it does everything.

01:08:41 - Brandon Hancock
That's the most ShipKit thing I've ever heard, and I'm upset at myself for not automatically adding that. So thank you, Patrick.

01:08:53 - Patrick Chouinard
And the second one is basically all the code for the custom GPT. So basically now it's going to be on the community repo. And I've started to discuss with that same custom GPT, planning the next two or three pull requests for that community.

01:09:15 - Brandon Hancock
That's awesome. I'm actually going to go ahead and merge both these in as we speak.

01:09:30 - Brandon Hancock
Yeah. So main thing inside of ShipKit, basically Patrick had an awesome idea of like, hey, like all of you guys keep on working awesome on awesome projects. There's multiple times where someone's doing something and like, well, hey, what's the easiest way to get this over to you guys? So we have a new community tab in here to where basically everyone's going to be able to just add like their own folder in here and just start to share resources.

01:10:51 - Patrick Chouinard
Yeah, the other thing I wanted to say is you know very well the whole process I had to use Gemini CLI [tool:Gemini CLI] as a search agent. Well, this week I had put my name on a wait list to get access to Gemini 3 Pro [tool:Gemini 3 Pro] in Gemini CLI. And I was blessed by the Google gods and I got in. So something else I tried with it, and that one was fun, is I actually gave it the prompt, do an in-depth search of, and I gave the school AI developer accelerator. And analyze all the posts in the community based on the results surface, the top 10 genuine AI development questions from the AI developer accelerator community. Include a link to the source thread of the question. Propose a complete and detailed answer to the top AI development question. The answer must be detailed enough to be postable on the community site. Your answer should include link back to the user's original question, as well as link to the citation to all the information used in the answer. And it actually did it.

01:12:09 - Brandon Hancock
What? What? So what did it do? Do you have the final? We're all in suspense, man.

01:12:23 - Patrick Chouinard
There we go. And while you're pulling that up, Patrick, so Patrick shared that awesome idea of using Gemini as a deep researcher. And I just want to go ahead and share with the group, seriously, if you're ever thinking about doing research across the web, it is so powerful. Quick two-second background. I used it. We needed to find fire chiefs across the nation. And using kind of a high-level overview of what Patrick told me to do, it worked perfectly. I did the process manually for one city, where I put in a city, and I went through, found the results of like, here's what's a good result. Here's what's a bad result. And basically taught the agent how to do the search for a city. And the second you can do it successfully for one city and define what you want as the output, there's nothing stopping you from kicking off 100 instances of Gemini to do deep research across all major cities.

01:13:35 - Patrick Chouinard
Yep. So that's basically what I did again. It's just because deep research, it's not really deep research, it's wide research. It's basically researching a lot of things simultaneously, but it was still a search prompt that's got automated a thousand times. This one, it actually has to go through. And by the way, it's found items that were not just on the first page, so it truly browsed the community, found some interesting questions, and you see here the top 10 AI development questions it found, and based on that, it then actually proposed a full and very detailed answer to the question with links back to what it found in one go.

01:14:29 - Brandon Hancock
How long did it take out of curiosity? Because that's crazy that it did that much in a single go.

01:14:36 - Patrick Chouinard
Agent active, like three minutes.

01:14:39 - Brandon Hancock
Seriously? Yeah, you have it here.

01:14:45 - Brandon Hancock
You see the total number of tokens and the number of time? This is the only thing that session did. So opened it, posted the prompt, run it, exit. That's crazy.

---

<!--SEGMENT
topic: HTML Presentations as PowerPoint Replacement and Deck AI Forge Project
speakers: Patrick Chouinard, Brandon Hancock, Elijah, Paul Miller, Juan Torres, AbdulShakur Abdullah
keywords: HTML presentations, PowerPoint, Gamma, Gemini, Claude, prompt engineering, sequential questioning, Deck AI Forge, Notebook LM, JSON intermediate format, Markdown, static hosting, GitHub Pages, Vercel, enterprise branding, GPT-4.1 Mini, Gemini Flash
summary: Patrick demonstrates a Gemini-native interactive HTML prompt-engineering tool he built in five minutes during the call, which uses a "sequential questioning" methodology and includes an "Optimize with Gemini" button. He then introduces Deck AI Forge, a pipeline that converts raw text → Markdown → JSON → branded HTML presentations, positioning it as an enterprise alternative to PowerPoint and Gamma. The group discusses hosting options (GitHub Pages, Vercel, Hostinger), cost efficiency using small models (GPT-4.1 Mini, Gemini Flash), and the broader archetype of structured AI pipelines with intermediate formats.
-->

01:15:27 - Patrick Chouinard
And the last thing I want to share is, and I'm sorry for this one, the interface is going to be in French, but it's something I'm doing for the job. Basically, I had a prompt that I worked on for months that I, it's basically, I call it sequential questioning. It's basically a prompt that asks you what you need to do in order to implement a prompt. So it's questioning you to help you create the best possible prompt, but it's a process you have to go through. So what I did is I posted in Gemini and asked Gemini, like, use this as a premise, but now build an interface that embodies what this prompt does. So it's a very short original prompt that just says, embody what this prompt is supposed to be doing. And the result of that is...

01:16:31 - Brandon Hancock
Dude, I didn't know you were multilingual. That's awesome.

01:16:35 - Patrick Chouinard
So basically what this is, is a complete page. And I know it's French, but basically it explains the seven components of a prompt, that it needs an identity, an objective, steps, instruction, constraint. All of those are interactive. The type of tasks that can be done by a prompt, manage the complexity, quality, and principle. And then the prompt generator, which originally was simply like you type a step and it starts to create it here. You could ask tonality, all of that, but that was static. So it's basically just a form that creates a structured document. But in Gemini, now you have this little button that says add Gemini feature. And what that did is it added an "optimize with Gemini" button, which you run. It actually calls Gemini, looks at this, figured out that it's a prompt, and it optimized the content of the prompt.

01:17:40 - Brandon Hancock
You're prompting to improve your prompts. That is meta next level. And I bet it works phenomenally. Like that's the crazy part.

01:17:49 - Patrick Chouinard
The only thing is you cannot take it out of the Gemini interface because you will lose the connected Gemini. The rest will work because it's just a static HTML page. But the connected Gemini only works when you're in Gemini, but still pretty insane that you can. And that, by the way, this example, I wrote it while we were talking on the call. It took literally like five minutes to get that done.

01:18:17 - Brandon Hancock
That's crazy. That's crazy. It's wizardry. That is wizardry, man.

01:18:21 - Patrick Chouinard
Because now whenever I need to send information to people, I no longer send them PowerPoint [tool:PowerPoint]. I go into either Gemini or Claude and just say, this is the information I want to share. Build it into a self-hosted HTML page. I send the HTML file, open it in your browser. You have everything. It's interactive. It's going to show every information I need. No need to construct it. Just write it in HTML.

01:18:49 - Brandon Hancock
PowerPoint is going to be dead. There's no reason it should exist anymore, especially because I'll literally exactly what you're saying. Because my wife, she's a consultant. The amount of time they have to spend creating all these different PowerPoints for the pitch, the contract, like the amount of like, no, it's just like, here's everything about our company. Here's everything about this customer. Generate this, go forth. Like, that's what it should be, you know, because it just, it takes so much time for no reason.

01:19:28 - Patrick Chouinard
Yeah, it's funny you say that because I just started a project with ShipKit called Deck AI Forge [tool:Deck AI Forge], which is basically that is you input it. I inspired myself from Notebook LM [tool:Notebook LM]. It's you input raw text, it reformats it into a slide format in Markdown, you validate it, tweak it when you're happy, set generate, it transforms it into JSON, and then output it in HTML. A little bit like what Gamma [tool:Gamma] does, but Gamma is a design tool. Here, what I wanted is something for the enterprise where you have a template that is branded that will always be exact. It's identical. You just put content in and it spits out presentation in the format of the enterprise.

01:20:09 - AbdulShakur Abdullah
And you guys tried Claude's generation, PowerPoint generation? I know Claude was doing PowerPoint generation too.

01:20:18 - Patrick Chouinard
But that's the thing. I avoid PowerPoint because, first of all, it's incredibly hard to have something consistently good. And it never looks as good as an HTML page.

01:20:30 - Patrick Chouinard
And honestly, a lot of people were telling me originally, oh, yeah, but it's HTML, it's coding, people are not going to like that. Are you actually opening your PPTX in Notepad? Yeah. This, you double click on it instead of opening PowerPoint, it opens your browser and you have all the information you need in a format that they can consume. And it's interactive on top of that. And it's disposable too.

01:20:58 - Ty Wells
Yeah, exactly.

01:21:00 - Patrick Chouinard
And you don't have to worry about building any platform around it. There's no platform. It's interactive. It can be dynamic, but it's self-contained into a single HTML. It can run everywhere. There's no security risk of exfiltration or anything. So, yeah. To me, it's a better format than PowerPoint. And that's what I want in a pipeline that's going to create it automatically.

01:22:14 - Patrick Chouinard
Is you don't need big models. GPT-4.1 Mini [tool:GPT-4.1 Mini] does marvel to summarize and reorganize content into a deck form. And then Gemini Flash [tool:Gemini Flash] does marvel to dump it into an HTML form. So it's dirt cheap to run. And because you cannot have good result if you want the AI to design your tool. Yeah, you need big models to have good design. But here I don't want design. I'm going to give it a template and use it. That's it.

01:22:48 - Brandon Hancock
Juan, I saw you had your hand up, man.

01:22:52 - Juan Torres
Yeah, no, that's an amazing idea. So I guess the constraint in this productionization of HTML presentations would be agentic engineering, wouldn't it?

01:23:02 - Patrick Chouinard
Yeah, it is. Yeah, yeah. But actually, again, the whole pipeline is something I've designed talking to my AI assistant. So I have a custom GPT that I use and I talk to all the time. And basically, especially since 5.1, ChatGPT for that usage is absolutely insane. With the personality tweak, I can talk to it for hours and now it has, and it remembers all of my ideas. It now does referencing across the discussion. So I start a new project and says, oh, you know, you work on something similar two days ago. Do you want to start over from that point? Yeah, sure, go. And then I dump that into a spec kit or a ShipKit infrastructure to build it once the ideation has been done talking to a model.

01:23:58 - Elijah
I just did something very similar. I've been building out some content that I want to present, and I ended up creating in that a slide deck, basically, in the interface. But I was wondering how I was going to do that when I do my recordings, because people may end up getting my Vercel app link and then being able to go to my site. I really don't want them to have access to it. So I was wondering how I was going to share it. But you hit the nail on the head by doing this. Thank you so much for the idea. And then also, like, there's no reason why, if you think about kids or people, there's no reason why we don't have our own branded presentation style that we'll be able to present all of our ideas for our life.

01:25:15 - Patrick Chouinard
Basically, use Gamma as the designer of your template, and once you have it, just feed it to a pipeline like I built, and create thousands of them just templated the same way.

01:25:29 - Brandon Hancock
Final thing I want to share, Patrick, so this is what is going to be coming out in the new video very soon, and I'll be sharing, but like, what's crazy is the exact same workflow process of like coming up with an AI-generated video, this is the same archetype of a problem, whereas mine is I give an input of a Pokemon, and it goes through a process that I've tweaked like a thousand times to get a good video at the end. And what's crazy is what you're doing, it's the exact same, it's like I have a rough outline. And for a presentation, my ideas are cluttered. Now I need you to help me refine my ideas in a structured way. I need you to maybe do a little bit of research, put it into a slide, break it up, make it nice and pretty, and then at the end, spit out a presentation. Like, that's cool. I really, really like these types of problems because this is where you get a ton of leverage because this would normally take forever. But now with these long automated workflows, AI workflows, like, you start to unlock a lot of these really cool use cases.

▶ 01:26:41 - Patrick Chouinard
Yeah, basically the idea is the intermediate format. It's, you get from raw text to an intermediate format because to me, I want to see it in Markdown so I can tweak it. But before I send it to HTML, I have a standardized JSON in the middle because the idea is once you have the JSON, the output is whatever you want. For now, it's HTML, but it could be PDF. It could be any output I want based on that intermediate format.

01:27:18 - Elijah
So if you wanted to host those pages, though, what would be the best way to host them if you did want to? So you're sending a file that somebody just double-clicks and opens, but what if you just wanted them to hit your own web page as an HTML web page?

01:27:18 - Patrick Chouinard
Any hosting platform. It doesn't require any server infrastructure. It's a self-hosted web page that doesn't have any dependency.

▶ 01:29:34 - Patrick Chouinard
Just put it in GitHub and use the GitHub Pages [tool:GitHub Pages] and it would work perfectly and free.

01:29:45 - Brandon Hancock
Also earlier, Biggi was talking about Hostinger [tool:Hostinger]. That would be a phenomenal option for this to where you're just dumping the static assets to elijah.com forward slash customer presentation six. You know, you could do that as well.

---

<!--SEGMENT
topic: Docploy Self-Hosting, Stripe Payments, and Juan's Vendor Extraction Agent
speakers: Paul Miller, Tom Welsh, Brandon Hancock, Juan Torres, AbdulShakur Abdullah
keywords: Docploy, Hostinger, VPS, Vercel, Supabase, self-hosting, Stripe, ACH payments, subscriptions, vendor extraction, general ledger, NLP, Regex, agentic workflow, SOC 2, AWS, web scraping, Crawl4AI
summary: The group addresses Biggi's question about Docploy as a Vercel/Supabase replacement: Paul and Tom confirm they are using it via a Hostinger VPS with pre-configured Docploy, deploying apps via SSH and GitHub connection. AbdulShakur asks about setting up recurring client payments; Brandon recommends Stripe with ACH to avoid credit card fees. Juan Torres reports his vendor-name extraction agent has reached 95–98% confidence using exclusion rules and a validator agent, and shares an AWS SOC 2 architecture video. Tom Welsh describes his Dung Beetle scraping project, now featuring per-user async scrape queues, and discusses a CSS specificity bug caused by Crawl4AI's bundled styles.
-->

01:02:39 - Brandon Hancock
Biggi asked any new opinions or experiences with Docploy [tool:Docploy]? And is my understanding correct that it can replace my Vercel and Supabase subscription? Still trying to figure it out. Yeah, I was gonna say, Tom, Paul, do you guys have any quick updates on that one?

01:03:00 - Paul Miller
Yeah, I'm still using it heavily. Tom, have you started going into it as well? Because you're Mr. Host-it-yourself.

01:03:09 - Tom Welsh
Yeah, I might be. But yeah, I've been sitting there. Yeah, no, I've got it installed locally, but I'm just having issues with me, you know, actually reading the documentation, just trying to jump in and keep reinstalling it because I keep buggering it up. But I would definitely go and buy the Hostinger thing if you can get a subscription on it. I just want to play with it straight off here to start with. It seems great. I've got to get integrated and it works quite happily with that. I just haven't moved the virtual part across yet.

01:03:48 - Paul Miller
The context Tom was talking about was if you go to Hostinger, they have a host pre-configured with Docploy. So you can say, oh, I'm going to start with setting up a VPS host that then enables me to run sub-VPS hosts that then act as like a Vercel backend, and then you set it up from there. So you'd SSH into the Docploy running on that host, and then you would connect back to your GitHub, or just upload your whole code, published code, and then it automatically deploys that out into Docploy, just like you would do into Vercel. So if anyone's got questions, just DM me through the school community, happy to answer it. I'm using it live, I've got a number of clients that have got different servers on it, and I'm loading up all sorts of stuff on it now.

01:05:01 - Brandon Hancock
Real fast, Scott, just going back to you really quickly. I kept saying the wrong word. It was worktrees, not subtrees. So I can't find it, but this one, there's a few videos on it. It is such a popular topic. I unfortunately missed the window to make a video on it, but, oh, it's this one. It's this video right here. I'll drop it in chat. This is the one that I watched. He broke it down so clearly.

01:30:12 - Brandon Hancock
Wait, no. Paul, you already went. Wait. Sorry. I got to take that order. Juan.

01:30:19 - Brandon Hancock
Hey, folks.

01:30:22 - Juan Torres
Nothing much. Just finalizing last features on the GenTech extraction of the vendor names. It's reaching really good percentages of confidence. I was looking at what the standard is in the industry, and it's, like, around 80% confidence level. And for super detail, well-done jobs, it's about the 90 percentile. And I'm on the 95, 98% confidence level at this point. Because what I did, I just added a validator agent that essentially the first agent is the extractor agent. So it extracts the vendor names and it has really good extraction levels, but in its context. So I simply added before the extraction process, you can add vendors, company names, and entities, companies, and individuals that you want to exclude from the extraction process. Because oftentimes in general ledgers, what you have is the name of the CEO coming up a lot of times. And it can confuse that CEO as a potential vendor when in actuality, the CEO went to eat at Subway. And in this case, Subway was the vendor, right? And so now through, and I had to do this because the front end engineer is not moving fast enough for me to start deploying this feature. So I just did it on the web application. So I just basically added those features for then the validator to use those as exclusion rules in order to basically get that context engineering into the agentic system. And, you know, the context engineering is simply you just put a bracket and basically set a rule around a particular variable, right? Because the bracket represents the variable that you're putting into the UI. So now that's and then together with the creation of a list of original vendor names that basically accounts for every time there is a naming of a specific vendor, then the validator has a second tool, which is reference names that have already been identified through the general ledger. And so it goes quickly go through that list and confirms the weight of a specific vendor. And I've used all the Regex [tool:Regex], Weezy, and NLP tools in order to help the validator just have a good confidence level at this point.

01:33:17 - Juan Torres
Super quick question for you. So I can't remember, this is a client contract project, right? Not your own startup? This is for them?

01:33:26 - Juan Torres
Yeah, no, this is a contract. So this is not my code. This is not proprietary to me.

01:33:33 - Brandon Hancock
Oh, I gotcha. Dude, out of curiosity, because once you start to get to those high levels of confidence, how much time are you saving them? Because that's the part that I know, love the idea of omitting, the way you're tackling this, I love it. I'm just curious to see the impact of once you get this working, what's going to happen?

01:33:52 - Juan Torres
Hours. They don't have to do it manually. This is just a click of a button and it does it automatically.

01:34:01 - Juan Torres
So there's no manual. The accountant never has to do anything. He doesn't even have to validate anything at this point.

01:35:29 - Juan Torres
I also wanted to share this video that I created. I didn't share it last time. I forgot about it, but it's usually how now I'm going about creating my AWS [tool:AWS] architecture in order to be SOC 2 [tool:SOC 2] compliant. So this is, usually it entails, you know, an AWS VPC with a database, an inference engine, EC2 instance, and EC2 instance, or an elastic Beanstalk to deploy the web application. So just wanted to share it, see if people find it useful.

01:36:09 - Brandon Hancock
I 100% need this. So I'm already saving this to watch as well. We, at the very beginning of 2026, have to go through this exact process. So this is insanely helpful.

01:36:38 - Brandon Hancock
Well, I think our list, we've checked. I saw Jake just had a hop off. So I think we'll go Adam, Abdul, Mitch.

01:43:27 - AbdulShakur Abdullah
So, so the, in terms. If I want to just quickly get a month-to-month payment from a client, what are you using to set that up?

▶ 01:47:09 - Brandon Hancock
<A>So Stripe [tool:Stripe] is by far one of, I mean, Stripe's phenomenal. And you can actually, if you don't want to like do a full-blown website, you can always, inside of Stripe, you can actually set up a subscription. And basically, you'll just send them directly to an invoice page. So you'll basically say like, hey, we're setting up customer ABC contract. And then you can just manually send a recurring invoice. So they pay once on that checkout page that you send over to them. And then on the back end, Stripe's automatically going to just charge that credit card every month. So if you ever want to do like a retainer or if you ever want to like do, hey, yeah. I mean, basically, if ever want to do a retainer, that's the easiest way to do it. And only gotcha is ideally you would probably want them to pay, especially if it's a direct company, not with a credit card. Only allow ACH just because Stripe's going to take a three and a half percent fee. If the customer does it with a credit card, if you say that they could only do it with the ACH bank login, then, you know, you don't pay anything, basically. Stripe's super generous on like the first 200 ACH payments. So it adds up. So that's just a quick word to the wise.</A>

01:49:19 - Tom Welsh
Hey guys, no big deal for me. On the Stripe thing, I literally just picked up a client today. Hey, my handyman goes around and said, oh, I'm doing some automated payments. He goes, Stripe's your friend? I threw up my Dung Beetle page, just literally the ShipKit page. He goes, like this, you mean? He goes, how did you do that? I go, I can do it for you. Yeah, he's really good at painting, but he's really bad at websites. Yeah, it sounds like a good partnership. You paint my house, I'll make your website.

01:50:05 - Tom Welsh
So, as you all know, I've got my Dung Beetle thing going on, and a couple of weeks back, I did a flippant comment on Sunday going, ah, I've just moved my back, I've just went full stack, front end, back end, moved my database to the back end, jobs are good. And I've now spent two weeks fighting all the little vagaries that's created to get me to a fight, and I'm now working, fighting forward. So, today I've created individual user scrape queues, so a user can log in, send a scrape, piss off, go do something else, come back whenever he wants, click on the scrape, and there it is, in all its glories, all the scrape data, fully detached, tells you how much stuff's come back, and, yeah, keeps it all there. And what it's done is, I actually went back through all the stuff I've done, I've got about 25 or 30 scripts sitting there, so I'm really happy with that.

01:51:00 - Tom Welsh
I also ran into issues where Crawl4AI [tool:Crawl4AI] is one of the packages I'm using. It's got its own CSS stuff inside it. So I was running out of scoping and specificity issues where I had a modal thrown up in the screen and all my components were at the side of it. It took about 30 minutes before the AI said, oh, yeah, it's a specificity issue. Like a new rule. So, yeah, that was a crack. That was today's finding.

01:51:31 - Brandon Hancock
Out of curiosity, because on that fix, I was very curious. Did you just have to wrap everything in like a sub page? Like, did you have to just wrap everything? How did you make sure it didn't scope creep out?

01:51:43 - Tom Welsh
I don't know. The AI did it.

01:51:48 - Brandon Hancock
That's funny. Don't question it, man.

01:53:33 - Brandon Hancock
Tom, anything else going on that we can help with? It sounds like you're keeping yourself busy.

---

<!--SEGMENT
topic: AI-Generated Facebook Video Monetization — Mitch's Channel
speakers: Mitch, Brandon Hancock, AbdulShakur Abdullah, Juan Torres
keywords: Facebook monetization, AI video generation, Sora, Kling 2.5, Krea AI, bounce rate, completion rate, ad placement, content strategy, pattern interrupt, sequential chaining, custom GPT, Claude projects, video automation, SaaS, background jobs
summary: Mitch shares that his AI-generated Facebook video channel has surpassed 4 million views, with individual videos reaching 1.3–1.7 million views and monthly revenue doubling unexpectedly. He explains Facebook's shift from mid-video to end-of-video ads and the importance of minimizing bounce rate over completion rate. Brandon previews the upcoming Pokemon AI video generator source code release and frames it as a template for long-running AI workflow SaaS products. The group discusses Sora vs. Kling 2.5 pricing, content niche strategy, and how Mitch's manual two-hour editing process could be partially automated.
-->

01:56:38 - Mitch
You know, I was just logging on, you know, and I was looking at my feed and I saw this Charizard. This little guy beating up on the young one. And then all of a sudden, I saw this little Charmander turn into a Charizard. Blast. I see. Thank you. I was, once again, 2 a.m. last night, just like, just so excited playing with Pokemon. I was like, man, I'm like, this is, this is happiness. When I was a little kid growing up, I was a Pokemon fan. Nothing's changed. I'm now just 30 doing the same thing, except with AI.

01:57:45 - Brandon Hancock
No, I've been good. It's crazy, because basically, yesterday I was like, oh, like, cool, I made my first, you know, decent chunk of change, and then the next. Hey, like it just doubled because the videos, yeah, all the videos, they went viral again. You know, I thought like I was pretty good at like a hundred, 800K and then it went to like 1.7 million and another one went to like 1.3 million. No, I went to like 900K views. Oh, nice. Mitch sends me screenshots of these things happening and every time I'm just like, damn, like this is unreal.

01:58:30 - Brandon Hancock
How many different channels do you have?

01:58:33 - Brandon Hancock
I only personally have one. Yeah. But all on Facebook, right? Yeah, all Facebook. Generated content. Yeah.

01:58:44 - Mitch
A few things real fast. Here's what I love about what Mitch is doing. He has picked something he has an unfair advantage on. His understanding of just story arcs, what gets people attention. Like seriously, 10 out of 10 on that. That's skill. Like literally haven't met anyone else that understands content as well as Mitch. And when it comes to like monetization, Mitch has found a really cool niche within Facebook. And what I love about it is it doesn't cap his ability to earn. It's leveraged. As long as people watch stuff on Facebook, there's nothing stopping, like you said, just doubling a paycheck without any additional work on Mitch's behalf. Like he does it once and there's unlimited upside. Like that is the coolest ways to make money. So I get so excited every time I see these charts just double.

01:59:41 - Mitch
Yeah. And I did have something to share with the class, so to speak, is I've been really trying to dive into like there is a Facebook, like I will just call it monetization point one point oh and then two point oh. And I was talking with my business partner about this and I think we've kind of really hammered it down, which is really what Facebook looks for more than anything is bounce rate, meaning does your video like have someone bounce off the platform? Because even if you have like a high completion rate, well, I'll tell you about a couple of steps, which is they used to like have in-video ads or mid-video ads, meaning if you were to watch a video halfway through the video, it would roll an ad. And now it doesn't roll an ad until the very end of the video. So like, yes, you want like a good completion rate, but realistically, even if you have a good completion rate, and it has them feeling like satiated, you're actually like getting them off the platform. And so you're really wanting to like create like this limitless demand. And that's like why those food videos do so good. That's why like those dog videos do so good is because like you can't get enough of them, like you are always hungry for more kind of thing. And so now it's like we're trying to engineer that need.

02:01:24 - Mitch
And then also when your videos do a really good job of meshing together, meaning when you create that need, when one of my videos go viral, two other ones go semi-viral because they're the thing that gets played shortly after in a different session or whatever.

02:01:32 - Brandon Hancock
So I want to ask questions on this because like, so from YouTube, what my understanding is, it's like, okay, I do a video on a topic. At the end of the video, I know at the end, if you have watched this video and you're going to implement it, you're most likely going to have these three next problems, which is so easy on a YouTube platform to say like, hey, and if you implement everything I said, the next thing you're going to run into is, you know, automating this. So you're definitely going to check out this video next. <Q>I'm curious how you tackle that from a Facebook perspective, because it's not as how-to, it's not as educational, it's more entertainment based, you know? So it's like, how do they even know what else is next from you?</Q>

02:02:04 - Mitch
<A>No, it's a separate video entirely. Like, even auditing, like, a feed that I generated for myself, right? I was like, I watched someone who was doing, like, a lot of Outback cooking videos, like Southern Louisiana cooking, you know, and, like, you're seeing them, like, put up, like, the whole, you know, giant. And so I watched that full video, watched the ad, it's like, okay, cool, and then I went, like, three videos down, signed up to one of their videos. It was another cooking video, right? It was different, but it's still giving me that satiated desire of, like, what I'm wanting. So if someone, like, likes the cop videos, then it's like, well, then it's injustice. You know, if someone watches dog videos, it's oxytocin, you know? So, like, all those different things, you kind of have to, like, see, like, what it is. What they really want. Got to deal with that drug.</A>

02:03:16 - Mitch
Do you want to get onto any other platform or stick on just Facebook?

02:03:45 - Brandon Hancock
Maybe some other platform eventually, but I'm just trying to make more videos right now. It's to the point where I'm, like, you know, I'm, like, okay, this is considerable, so I just need to put more time into it and focus. It's on, like, currently what's doing. I think I'm close to 4 million or something, 4 million views so far.

02:04:08 - Brandon Hancock
That's insane. Well, hey, real fast, what I want to do is send you, do you know who Jake Tran is? He makes the, like, Faceless video YouTube channel [link:Jake Tran YouTube channel]. He had a phenomenal interview at one point where he dissected how he was going to differentiate and just explode. And he had a really cool exercise of breaking down exactly how he did it. I'm going to send it to you. I think this is the one, but I would look at what he did just to see if there's anything that could be helpful.

02:05:55 - Mitch
Yeah, I just wanted to ask, so what can I, is this AI generated content? Yeah, with Sora [tool:Sora]. Oh, cool, cool. So are you manually prompting each process? Every clip, yep, textogen. Let me ask you this. I'm curious. <Q>Have you thought of using agentic systems to automate the process of prompting?</Q>

02:06:23 - Mitch
<A>I mean, it's kind of agentic now. I just do sequential chaining. But you would kind of laugh at my system if you saw it. You'd be like, wow, like, this dude's on these AI calls and, like, this is the system? Like, really? But, yeah, no, it's just, like, a couple of custom GPTs or Claude projects, and I just, like, copy and paste and then, you know, get the results. And then one of the videos I went through, like, the process where it's just, like, I take a series of clips and then take the contents with each clip and then make a request, you know, to the Sora API each time. For each clip.</A>

02:07:06 - Brandon Hancock
I think, though, it would be really good. Like if someone looked over it and was managing it, like, yeah, no, like Brandon's process is definitely better than mine. But mine is just way more like, like shut up AI, just do this, you know, like get out your way. But yeah.

02:07:36 - Brandon Hancock
So what I'm super excited for, Mitch, like I said, dude, this one, this whole thing has been for you. Like I'm pumped to see where you take this video generator because like because you're going to see a lot of the stuff that you're doing. You don't even have to build a full blown SaaS for like at the end of the day, what do we need to do? We need an agent who is a phenomenal expert at understanding how to create content like what you're doing. And everything you're saying, like, you already have the know-how on what you want in each time. So it's like, why are we not documenting, here's what you did right, here's what you did wrong, and just keep improving these SOPs over and over and over again? Because, like, this is truthfully, like, realistically, this is generation 80. Like, I have improved each one of these seven steps dozens of times because they were not doing good. They weren't doing good. Then they finally got good enough to pass from step one to step two. And then it's, you know, it's just a continual iteration process. And what's sick now with Gemini, Gemini's phenomenal at understanding videos. So you really could pass the video into Gemini. You could then pass in your prompts and saying, like, hey, here was my seven-step process. What's going wrong? Like, there's so many cool things that you can do to use AI, to improve AI, to start automating the process.

02:09:00 - Mitch
So much, like how you said, like, I think you're doing stuff a little bit manual right now. I'm very excited to see if you kind of follow what's in the video, but just apply it for your own use case to see how quickly you can make stuff. Because like, kind of like we were talking about the other day, like, dude, what happens if you did five videos a day? Like, what would that look like for income, you know?

02:09:27 - Mitch
Yeah, the reason why I'm not giving away the page to everyone is just because I noticed it throws off the vector of the page, but in short, it's like cop videos. And the cop just does like crazy stuff, like to start out the frame. So like, it'll see like a painter painting, just kicks the paint can.

02:09:44 - AbdulShakur Abdullah
Dude, that's a pattern interrupt.

02:09:46 - AbdulShakur Abdullah
Yeah. Or like, sees a bookstore. They like, they have a place booked. Just places all the books. Or, I don't know. So, yeah, like, sees someone, like, slams the door, like. Stop right there.

02:10:15 - Brandon Hancock
Biggi, real fast to answer your question. Yeah, so on the, I was wondering about the Pokemon brand, will this only be for demo purposes or I can publish it? I mean, there's full blown, so you'll see in the YouTube video I'm about to publish, like, I'll just show the screen real fast. So you guys can see what I'm doing. Because there are full blown YouTube channels that, oh, shoot, one second. Let me pull it up. Yeah, so, like, I'll just show what I did for inspiration. Just because, like, the second you kind of see the monetization opportunity, it's, like, hard to unsee. This was the channel. Like, it exists right now. They do a video in sprints, and then sometimes they stop. So you can see they've made one video over the past month, and the channel's bringing in $4,000 to $12,000 a month in ads.

02:16:14 - Mitch
And this is on one platform. And, like, everything you're seeing there, like, that is 100% AI generated. So, like, ideally, you know, you're going to see with the thing that I'm dropping for you guys tomorrow, it takes 10, like, if you just let it run once, it costs $7 to $10 to make a whole clip. But, obviously, some of these clips aren't perfect. Like, my Charizard looked like it had fire coming out of its butt instead of its tail at one point. So, like, obviously for that, you would want to regenerate it. So that's another $0.30 or something like that, $0.40.

02:16:43 - Brandon Hancock
But at the end of the day, like, hey, if you know you're going to monetize it, like what Mitch is doing or what these other channels are doing, hey, just to get there faster, for every time I'm going to generate a video clip, I'm just going to generate four so that I can pick the one that's best. Instead of right now, it's one, I manually do it again, you know, so there's so many ways you can do it faster.

02:17:11 - Brandon Hancock
I was going to say one thing is with your video gen model, it's way cheaper than Sora. So like, you know, the other thing, Abdul brought this up, it's like, how long does it take for you to make your first dollar? It's like, yeah, if I were to do this with AI videos, I'd have to invest close to like $400 before I would even get like monetized, you know, so as far as AI credits. So with yours, it's like, no, like way cheaper, you know, to actually get going.

▶ 02:17:46 - Brandon Hancock
So Biggi, so to make the two minute video with audio, with audio, video, and narration, it was $7 to make the full video. There's ways you could do it cheaper. Obviously, I'm using Krea AI [tool:Krea AI], you could use the other one, just regular, but like, you could also use some of the dumber AI generating videos. Which are half the cost. So the thing I did was pretty middle of the road on all things prices. So, but you could also go to what Mitch is talking about for video generation and his is, I think mine was like 40 cent per 10 second clip. And I think yours is like, do you know how long yours is for a clip?

02:18:22 - Mitch
It's close to five. No, it's like $7 a clip. Sorry, when I say a clip. Oh, okay. Sorry. When I say a clip, I'm talking about 10 seconds. So 10 seconds for me is 42 cent.

02:18:56 - Mitch
There's so many cool ways to make money with AI. I think, I don't know how long these, each one of these opportunities exist. But like, if you don't mind, kind of getting into that unknown play area, spending some money up front to test it yourself and learn and become the expert, like, seriously, like how many people are there on earth doing what Mitch is doing? A thousand, maybe a few thousand, but like, okay, cool. That's so much easier for a competition pool than software engineering right now. And I'm sure he's making more than a software engineer is. So like, that's crazy, you know, it just comes down to being really good at making AI videos, which, in a month, like, of full hard work, I'm sure, like, you could get pretty dangerous with it, you know?

02:19:36 - Brandon Hancock
So yeah, it's just a very cool time to be alive. I always question, why am I not doing X, or Y, or Z? And Mitch makes me question my life choices very regularly.

02:19:46 - Brandon Hancock
You know, the comment section was hilarious, because the one where the officer kicked over the paint, someone wrote a comment that said, and I quote, we need more cops like this. Like, what? I was like, what? I got it? What? That was the most hilarious comment I ever read. I was like, I guess you're supposed to see chaos.

02:20:09 - Mitch
Yeah, I was just doing the math, like a full clip, like a full three minute clip you think is just three minutes, but it's really like six minutes. And so 10 cents a second for a six minute clip is what you got down to, yeah, to three.

02:20:35 - Brandon Hancock
Yeah, no, it's a cool time to be alive guys. So, but definitely, definitely gone over. But yeah, Mitch, like I said, excited for you to see it tomorrow. Would love to hear your feedback on it. Happy to help if there's anything I can. And then obviously, one of the big promises I had for you guys was, and why I was so excited to work on the system is like, hey, you get the full system for free. You can run it on your local computer, but it also sets it up very nicely to kind of fall into the architect, the problem archetype of long, long running background jobs. So it will get added as a worker SaaS walkthrough video to where you get to see, hey, I built out a really cool AI workflow that works perfectly. I nailed the prompts. I nailed the entire sequence. Now, how do I bring that to a like production AI application so that others can use it to like, like literally Mitch, if he wanted to, at some point could not only just do the thing himself, but he could sell the system to others to where, yeah, like there's, there's so many cool, cool things that you could do.

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names appeared in the transcript and were not present in the SPEAKER_ALIASES map provided (which was empty/unavailable at processing time):

- **Patrick Chouinard** — active contributor, Git scripts and custom GPT author
- **alexrojas** — client proposals (lead management, legal contracts)
- **Morgan Cook** — brief appearance, session opening
- **Ty Wells** — digital frame gift project, teased ShipKit project
- **Brandon Hancock** — host/facilitator
- **Marc Juretus** — Anti-Gravity custom shopper project
- **Paul Miller** — SaaS documentation strategy, Docploy user, Auckland-based
- **AbdulShakur Abdullah** — model consistency question, ShipKit firewall issue
- **HP** (also referred to as **Scott**) — Claude Opus 4.5 update, status page tip
- **Andrew Nanton** — Codex vs Claude Code comparison, PySide GUI project
- **Juan Torres** — vendor extraction agent, AWS SOC 2 architecture
- **Adam** — API-first dissertation review, Anti-Gravity experimentation
- **Tom Welsh** — Dung Beetle scraping project, Docploy/Hostinger user
- **Mitch** — Facebook AI video monetization channel
- **Elijah** — HTML presentation hosting question
- **Mark E** — brief audio cameo
- **Prem** — dropped a link in chat (no spoken lines resolved)
- **Biggi** — questions in chat about Docploy and Pokemon brand usage (no spoken lines resolved)
- **Jake** — mentioned as having hopped off; no spoken lines