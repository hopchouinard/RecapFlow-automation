=== SESSION ===
date: Unknown (Tuesday, mid-December, estimated 2024)
duration_estimate: ~108 minutes
main_themes: AI-assisted development tools (Claude Code, ShipKit, Cursor), social media automation with facial recognition, AWS infrastructure security and agentic DevOps, knowledge graph / vector-store CV builder, non-technical founder seeking technical co-founder, package manager conflicts in React projects

---

<!--SEGMENT
topic: Pre-call Casual Check-in
speakers: Patrick Chouinard, Marc Juretus, Ty Wells
keywords: Brendan, Japan, Claude Code Max, token limits, Limitless, Meta acquisition, remote work, Montreal, AI platform evaluation
summary: Participants gather before the formal call begins. Patrick is hosting in place of Brendan, who is traveling in Japan. Conversation covers token-limit frustrations with Claude Code, the Limitless wearable being acquired by Meta, remote-work policies, and Patrick's work evaluating AI platforms (OpenAI, Anthropic, Google) for his employer.
-->

00:10:00 - Patrick Chouinard: How's it going, man?

00:10:01 - Marc Juretus: How's my buddy going?

00:10:03 - Marc Juretus: Good, good. Got on a little early. I wasn't on the last couple on Mondays. That's real rough for me, man. So I can make this one.

00:10:14 - Patrick Chouinard: It's like I see what my AI family's up to. Yeah, but today you're going to be stuck with me. Are you running it?

00:10:22 - Marc Juretus: Yeah, Brendan is still in Japan.

00:10:30 - Patrick Chouinard: He actually asked me just yesterday if I could run the call.

00:12:40 - Patrick Chouinard: Right now, this week I'm on vacation, so a little bit more relaxed. But for work, I'm working on testing out the new potential AI platform to be used at my company.

00:13:00 - Patrick Chouinard: We have an account for OpenAI [tool:OpenAI], Anthropic [tool:Anthropic], Google [tool:Google], and a bunch of others, and we need to test them out and create a testing framework to make sure we've assessed them based on all the feedback we got from users and all the projects in the making for the next year and what will best address all of those.

00:13:19 - Patrick Chouinard: Predicting AI a year in advance is not a simple task.

00:13:26 - Marc Juretus: <Q>Of the ones you named, which ones do you tend to migrate towards more, like for usage?</Q>

00:13:34 - Patrick Chouinard: <A>▶ Honestly, it looks like it's going to be a mixture of a couple, not a single, because tying yourself to a single platform for an extended period of time is way too risky right now.</A>

00:19:53 - Patrick Chouinard: My own personal gift for myself is a Claude Code Max [tool:Claude Code Max] subscription for the month of December.

00:20:05 - Patrick Chouinard: At $100 a month, just a higher token rate, a higher limit, so I don't have to stop and wait for my limit to reset.

00:20:20 - Ty Wells: That is annoying, isn't it? Normally, yes.

00:20:27 - Ty Wells: If you do what I do, you're going to run into it. I spent more money in overages last month than I did on my plan. I'm on the $200 max. I just had to get something done.

00:22:09 - Patrick Chouinard: Oh, and Ty, I see you have the Limitless [tool:Limitless]. You've seen that they have, what, one year left now? They've been bought by Meta?

00:22:21 - Ty Wells: Yeah, yeah, I saw that. I guess I've got a year to come up with my own solution.

00:22:29 - Patrick Chouinard: That's the approach I've been taking. If there's something out there that I don't have or I need, I just build it as part of the process.

---

<!--SEGMENT
topic: Non-Technical Founder Seeking Technical Partner
speakers: Garron Selliken, Patrick Chouinard, Paul Miller, Prem
keywords: real estate CRM, Google AI Studio, ShipKit, technical co-founder, SaaS, prototype, brokerage, MVP, scope management, evangelist role
summary: Garron Selliken, a 30-year real estate veteran, describes his frustration as a non-programmer trying to build a real estate CRM. He used Google AI Studio to mock up his concept and is now seeking a technical partner rather than trying to build it himself. Paul Miller and Prem offer perspectives on staying lean and finding co-founders within the community.
-->

00:26:16 - Garron Selliken: Yeah, I missed the last couple of weeks. I'm traveling in Mexico with my girlfriend in our van, and I had Starlink [tool:Starlink] issues. But I've come to the conclusion that I, as a non-programmer, can't quite build what I need to build. The learning curve is too high to get me to my application.

00:27:00 - Garron Selliken: I built pretty robust, large software applications in the past as the designer, but I had programmers that worked for my company, and so I find this process very frustrating because I can see what I want to build and I can't quite get there, and I'll be caught in a loop of troubleshooting for a week.

00:27:18 - Garron Selliken: So I actually went to Google AI Studio [tool:Google AI Studio], and I was able to mock up the version of the app that I want to build. And it works. But I have no idea how to get that to anything.

00:27:40 - Garron Selliken: I currently have coaching clients that I coach every week. I have a brokerage and a partner, Scott. I demoed it for him the other day, and he's like, okay, let's build it. So I am now looking at what is the process to pay someone to build it, or partner with someone, or bring in a technical partner with Scott and I to be able to get the working prototype into the 150 agents' hands that we have at his brokerage, and then launch it out into the world.

00:28:43 - Garron Selliken: I can build a prototype, I can test it, I can get my hands on it, I can play with it enough to know that the idea is valid and to show it to the other people that I have in the industry to get that verification. But at this point, I couldn't be the technical person. It's probably stupid for me to be that anyway, because I really should be the evangelist and do what I've always done — promote it and take it out into the world.

00:29:23 - Garron Selliken: What I did before was went and raised a million dollars and hired people and got an office and my overhead went to 80 grand a month and then we sold something and pretty soon my overhead was $200,000 a month and I'm never doing that again. ▶ The promise of AI for me was a small team of three or four people duplicating what my 20-person team did before and still having a life while developing stuff.

00:30:07 - Paul Miller: Yeah, no, I hear you, Garron. I went down the same path as you — raised like a million bucks and have a team. I still have that business. The ARR is going up and up, but it's the old school. And I started that one 10 years ago.

00:31:00 - Paul Miller: I probably held a similar view to yours until I really got into the ShipKit [tool:ShipKit] product and into Claude Code [tool:Claude Code], because I thought initially I'd just do a proof of concept, just to make sure that I could sense-check it with the customers that I'm pitching to, but I found you can nearly get to the Nirvana with AI now.

00:31:42 - Paul Miller: <Q>Have you got into ShipKit or doing any of that yet?</Q>

00:31:45 - Garron Selliken: <A>No, I haven't done ShipKit yet. I took Brandon's code and the task templates and did that and started with all the examples. I built a GitHub library and used that as my reference.</A>

00:33:58 - Patrick Chouinard: ▶ If you want your team of three or four people, the idea is that you don't need less skill set, you just need less of each skill set. Basically, it's a multiplier. It's not a replacement. So you need a developer — he's going to do the job of six of them. You need an evangelist — he's going to do the job of six of them. That's what AI is going to bring.

00:34:36 - Prem: So, Garron, I think you can still — I am kind of more of a technical person. I'm coming from the other side. I just put in the first SaaS application. And I'm trying to get people to sell and whatnot. So I think there might be other people like me, and I would like to kind of partner with you. So again, there might be other people in this community who want to partner with you.

00:35:11 - Prem: I've used ShipKit [tool:ShipKit] to kind of be where I am. Basically, I have always wanted to launch a SaaS application, and I was able to launch my first SaaS application in three months because of ShipKit and this group.

00:37:15 - Prem: ▶ And if it's ShipKit, it's 100x, I would say — you have all the bells and whistles and it builds on top of it.

00:37:32 - Prem: The thing is, when I launched the first application, it's about keeping the scope, because every day I want to develop something rather than just getting it out there. So I need to put a time box to say I'm going to get this to production and then work on bells and whistles.

00:38:04 - Garron Selliken: Yeah, Prem, I'd love to connect with you. I'll just shoot my email address in the chat.

---

<!--SEGMENT
topic: Kiosk App Middleware Breakthrough
speakers: Ty Wells, Patrick Chouinard, Marc Juretus
keywords: kiosk application, middleware, bill acceptor, hardware integration, reverse engineering, communication layer, web-driven app, Limitless hardware
summary: Ty Wells shares a breakthrough in reverse-engineering the communication layer between a web-driven kiosk application and its hardware bill-acceptor middleware. With this solved, hardware integration is now on his roadmap. He previews a Christmas demo for the following week.
-->

00:38:22 - Ty Wells: Hey, guys. Been traveling as well this week. So everything on pause, but I did make a breakthrough last week. I actually labeled it "breakthrough."

00:38:37 - Ty Wells: I was able to, working with this kiosk application that I'm redoing — I was able to refactor or reverse-engineer the communication layer between the kiosk and the — it's a web-driven app, but it needs this middle layer, middleware layer to be able to process bills as they're entered into the kiosk and they're stacked and so forth.

00:39:05 - Ty Wells: So I was able to break that before I left last week. So I was proud of that. ▶ So now hardware is on my list. It's limitless now — no pun intended.

00:39:25 - Ty Wells: Nothing much this week, just deploying. Nothing to show this week, guys. Sorry.

00:39:47 - Ty Wells: I'll do something for Christmas. Something crazy.

---

<!--SEGMENT
topic: ShipKit Setup Questions — RAG, Templates, IDEs
speakers: Lan, Patrick Chouinard, Ty Wells
keywords: ShipKit, RAG template, simple chat, Python, Anti-Gravity IDE, Cursor, Claude Code, VS Code, GitHub email, context window, AI Docs refs folder
summary: A new ShipKit learner named Lan asks a series of practical setup questions: whether a Python chat template exists, how to combine RAG and chat functionality, how to adapt ShipKit templates for the Anti-Gravity IDE, and whether the GitHub email must match the IDE email. Patrick and Ty provide detailed guidance on starting from the most complex template and using Claude Code in the terminal.
-->

00:40:28 - Lan: So I actually started to learn ShipKit [tool:ShipKit] in the past few days, and I do have a couple of questions.

00:40:38 - Lan: <Q>For the chat SaaS or simple chat, there is no Python template anymore, but my application is Python-based. So I'm just trying to see if we're going to have some update on that, or that's on purpose, or should I use that chat simple or chat SaaS to begin with?</Q>

00:41:11 - Patrick Chouinard: <A>That's going to be something for Brandon. Brandon is away in vacation this week and next week. I don't have any view on what's coming in the ShipKit pipeline.</A>

00:41:39 - Lan: <Q>If I would like to build an application that has both chat function as well as RAG function, how do I set it up and use the template? Should I use both templates or just one template?</Q>

00:42:00 - Patrick Chouinard: <A>▶ That's actually something I worked on myself this week. When you do have both, I take the template that takes care of the highest level of complexity. In this case, RAG is far more complex than the simple chat, so I start from the more complex template, and then just modify it to add — because honestly, the RAG template already has a basic chat functionality to talk with your documentation. In my case, I wanted to have multiple models available, so I've added that functionality back in.</A>

00:43:00 - Patrick Chouinard: ▶ Make sure that the first step, when you actually define your intent for the application, is going to be where all the magic happens. So put as much information in the first step as possible — the templates will guide you properly to add the functionality.

00:43:29 - Lan: <Q>I'm currently using Anti-Gravity as my IDE, but I noticed that we don't have a template for Anti-Gravity. So I'm wondering whether I can copy the agents setup within Claude agents directly to Anti-Gravity's agent, and so that I can use it, or should I give up on Anti-Gravity and use something else?</Q>

00:44:04 - Patrick Chouinard: <A>▶ Based on both, I would say the Cursor [tool:Cursor] template might be a little bit closer, because Anti-Gravity [tool:Anti-Gravity] is nothing else than a fork of VS Code [tool:VS Code], and the Cursor template is basically just using the prompt file directly. The only thing you're losing, quote-unquote, is all of the cursor rules.</A>

00:45:20 - Patrick Chouinard: I know that Brandon is using Anti-Gravity a lot, so I don't want to talk for him, but I wouldn't be surprised if there is eventually some adaptation for Anti-Gravity in the future.

00:46:29 - Patrick Chouinard: <A>▶ The easiest way is always to go with the platform on which the template has been built. It has been built on top of Claude Code [tool:Claude Code] and Cursor. My personal recommendation: I would focus a little bit more on Claude Code simply because Claude Code has a revolving five-hour window and Cursor has a fixed $20 a month. So if you go over, you go into paying, and it resets only at the end of the month. With Claude, if you're willing to wait a little bit, even with a simple Pro account, you get your five-hour window, do everything you can, and then just wait for the reset — a reset comes in a couple of hours, not the next month.</A>

00:47:34 - Lan: <Q>So just to your point — I do use Claude Code in Anti-Gravity. So you're saying I don't have to do any additional setup at all?</Q>

00:47:44 - Patrick Chouinard: <A>▶ At that point, build all of your markdown with Claude Code. And if you truly want to leverage Anti-Gravity, just have it implement things or do things based on the markdown that's been created already by Claude Code that has already leveraged all of the templates.</A>

00:48:16 - Ty Wells: ▶ All I do is, if I need any code, I just reference that code. Starting with the highest complexity — which is definitely the RAG — and then I just reference that code, like, "hey, I want to bring that chat into this project," and I just point to where it is and Claude Code will bring in at least the pieces that you want.

00:48:55 - Patrick Chouinard: ▶ There is a folder in the project template under AI Docs called `refs`. If you put the simple chat project inside of that directory, then you can use the rest of the template to leverage it as information in order to add the simple chat functionality on top of the RAG template.

00:49:27 - Lan: <Q>When I studied ShipKit, I do see Brandon actually referred to specific sets of documents. So that means we need to have at least a basic understanding of the structure of those documents. Is that mandatory, or can we just let code go wild without understanding much?</Q>

00:50:11 - Patrick Chouinard: <A>▶ I don't think you need to read them line by line before you actually start to do something. I do make sure that I have a high-level understanding of each. And guess what — you're working with AI. It's just text. So worst case scenario, if you're not sure, just ask your AI — Claude or Cursor or whichever it is — to just summarize and explain the template for you. So you don't have to read through a thousand lines, but you have a good high-level understanding of what they do.</A>

00:51:10 - Lan: <Q>I'm trying to use a different email for my IDE because I probably get more context window out of it. However, I noticed that I have difficulty pulling files from GitHub. Does the email for the IDE have to be the same as the email I use on GitHub?</Q>

00:51:36 - Patrick Chouinard: <A>▶ For ShipKit, yes, it does.</A>

---

<!--SEGMENT
topic: Claude Code vs. Cursor — IDE Integration Debate
speakers: Patrick Chouinard, Hemal Shah, Prem, Ryan - One Stop Creative Agency
keywords: Claude Code, Cursor, VS Code extension, Anti-Gravity, terminal, multi-agent, sub-agents, Vercel AI SDK, feature parity, task-driven development
summary: Hemal Shah asks about the practical differences between using Cursor alone versus Claude Code with Cursor, particularly for teams adopting AI-assisted coding. Patrick explains the architectural advantages of Claude Code's sub-agent scaffolding. Prem demonstrates the Claude Code VS Code extension GUI, and Ryan notes it breaks with complex multi-agent setups, recommending the terminal for production agent workflows.
-->

00:55:52 - Hemal Shah: Hello everyone. I was out for the last couple of weeks. I have a couple of questions. One is around chatbot templates. I know ShipKit has a chat simple and a few templates, but I'm looking for something for a company where it's going to be used by other developers. I don't want to use this particular ShipKit template. I'm looking for some open-source template because that source code is going to be accessible for a larger audience and there are licensing constraints. So my question — has anybody used open-source chat templates? AI chat templates? Any recommendation there — Vercel AI SDK [tool:Vercel AI SDK], Next.js chat template, Rasa [tool:Rasa]?

00:56:53 - Ty Wells: I've built all mine from scratch, but it's not rocket science. ▶ Check the likes on the repo to see what the feedback is, and then the issues too — that's usually what I go by. I'm not reinventing the wheel on any project. Whatever one you're comfortable with and has the least amount of issues, go with that.

00:58:41 - Hemal Shah: With ShipKit, I know Brandon is using Vercel AI SDKs [tool:Vercel AI SDK] on some of those projects. So I'll probably start there and then check a few others.

00:59:01 - Hemal Shah: <Q>Anti-Gravity [tool:Anti-Gravity] launched a little while ago. I'm with Cursor still. I find with Cursor IDE it's very easy for a newbie or new engineer to come up to speed working in this world with templates and task-driven development. With Claude Code, it's more terminal-driven. A few of you mentioned you're using Claude Code with Cursor. Any recommendation on just using Cursor by itself versus using a plugin with Claude? Is the feature functionality very similar?</Q>

01:00:10 - Patrick Chouinard: <A>It's not as much Claude with Cursor. If you use Claude in the terminal of Cursor, you have the full-feature Claude Code, no problem. If you use the VS Code extension of Claude, it's pretty good, but it doesn't have all of the same functionality implemented just yet. Not all of the slash commands are there and not all of the base functionality are there. They're getting there, but it's fast-evolving.</A>

01:00:50 - Patrick Chouinard: ▶ My basic setup is: I have my list of files, I have my Claude window, I have my editor where I see my plan always open, then I have the Cursor window simply to do debugging. Every time I commit something, it checks, and if it finds something, I let it debug, and while I continue working with Claude. That circle seems to work pretty much the best so far.

01:01:37 - Hemal Shah: <Q>Main reason for Claude over Cursor — is it mainly the cost, or besides licensing, are there other reasons?</Q>

01:01:46 - Patrick Chouinard: <A>▶ The cost is a big thing, but the whole scaffolding inside of Claude Code is really next level right now. Just the number of sub-agents it allows you to manage at any one time, all of the custom commands you can put in, all of the skills. The only one that does everything right now is Claude Code. I wouldn't be surprised in three to six months that they're pretty much going to have all of that.</A>

01:02:29 - Prem: Just to add to Hemal's point — with Claude Code, I know initially the terminal was more of a command prompt. I don't know if you've used the latest one where it is not a command prompt, but it is a window overlay within Cursor. Let me quickly share my screen.

01:03:35 - Prem: [Shares screen] So this is what — basically it kind of takes you from a terminal experience where you can type in and see all the things in a graphical way, rather than the whole terminal settings way. This pretty much offers the same as the Cursor chat window, and this works a similar way within VS Code as well. So if you already have VS Code, you don't need to pay for Cursor as a dumb IDE — you can completely switch over to Claude Code within an existing IDE.

01:04:22 - Patrick Chouinard: ▶ It has a lot of them, but it's not yet feature parity.

01:04:31 - Ryan - One Stop Creative Agency: It also breaks with agents as well. I found some of my agents just didn't want to get called or work within that at all. So I dabbled with it at the start, it worked fine for a bit, then they didn't update to it, and it just didn't call half my agents. So back to the terminal then.

01:05:17 - Patrick Chouinard: ▶ As soon as you get into multi-agent scenarios and things like that, you need to go back to the terminal for now.

---

<!--SEGMENT
topic: Social Media Automation App Demo
speakers: Ryan - One Stop Creative Agency, Patrick Chouinard
keywords: social media automation, facial recognition, AWS Rekognition, Publer, Postbone, Anthropic SDK, TypeScript, estate agency, property management, brand discovery quiz, Granola, content scheduling, Claude
summary: Ryan demonstrates significant new features added to his social media automation SaaS: AWS Rekognition-powered facial recognition that tags team members in uploaded photos, an estate agency mode that pulls property listings and auto-generates posts, a Publer backend integration for scheduling, and a brand discovery voice quiz. He has his first paying client onboarded.
-->

01:05:31 - Ryan - One Stop Creative Agency: Hello, guys. Those who've been on the last couple of weeks have kind of been sharing my progress building a social media automation app. And I've made quite a bit of progress from last week, and I made a point to try and get a bunch of stuff in before this call.

01:05:52 - Ryan - One Stop Creative Agency: I've managed to ram in facial recognition. I can't remember who it was last week, but thank you for recommending AWS Rekognition [tool:AWS Rekognition]. Apart from AWS being a bit of a pig on the back end, I've got that all integrated and working, so it scans every single image you upload against the team in that particular client, and then tags the images with the people that are in there.

01:06:00 - Ryan - One Stop Creative Agency: I've also added an estate agency mode, because a lot of my clients are estate agents — real estate agents — so I've got it integrated into their property management systems, so when they instruct a new property, it automatically pulls through all the property details, photos, all that stuff, and then can create a post directly.

[Ryan shares screen]

01:06:44 - Ryan - One Stop Creative Agency: I've added a whole team section down here, where you can put in all of the team members, upload their images, full body, face, a bit about them and stuff that gets pulled into the AI that's writing stuff. And then when you upload a bit of media — WAC upload file — it adds it directly in here, and the team members thing pops up. Give it a second — and then, if I give it a little refresh, there you go. ▶ So it automatically detects with a percentage certainty those three guys who are the owners of the company are in that photo, and then that feeds into the AI if I want to make a post about it.

01:08:00 - Ryan - One Stop Creative Agency: I've also given it access to their property portal. For any new stuff they list, it'll pull it through automatically. If I wanted to just create a post out of that property, we'll create a gallery, generate the post content using Claude [tool:Claude] with a system prompt, then the client prompt pulls through all of the information about the property, writes the whole thing, and then I can go ahead and schedule it for whenever I want, and that just slings it straight in with the first five photos of that particular property.

01:08:57 - Ryan - One Stop Creative Agency: I've changed the back end to use Publer [tool:Publer] — I don't know how to say it — because they allow you to do more cool stuff than the previous one I was using, Postbone [tool:Postbone]. And I've got now two different options with all the linked-up stuff in there.

01:09:00 - Ryan - One Stop Creative Agency: I've also got it to pull reviews through, and I can create review posts as well from their reviews. It will generate the post caption, and also send it off to Google, use Nano Banana 3 Pro, and integrate the background image, then overlay the text onto it, and auto-size it.

01:10:00 - Ryan - One Stop Creative Agency: ▶ The whole point of this — that's just all the kind of manual stuff you can do — but the idea is you can actually generate a month's worth of content, and then it'll generate weekly on top of that month, moving forward, from the media that's uploaded. So as long as you keep feeding it lots of media, it will just write social media posts for you. It has a full knowledge base and brand voice guidelines, context, do's and don'ts, custom AI instructions — all of that stuff feeds through.

01:10:25 - Ryan - One Stop Creative Agency: I made this brand discovery quiz, so rather than me having to record them on a call asking a bunch of questions to fill in this brand voice and brand context — the idea being it's now got a really nice quiz. They can use their voice — I can say ya-ya-ya, pause for a second, and then it puts it in there. It saves each one as you go, so it's got a 30-day token on this so they can come back to it.

01:11:00 - Ryan - One Stop Creative Agency: ▶ In theory, this should be like a real in-depth dive, and then that will feed back into Claude, once I've completed the whole thing, and populate the brand voice and the brand context and background.

01:11:18 - Patrick Chouinard: <Q>Did you manage to put the integration for all of the social media posting services, or did you have integration for one or something like that?</Q>

01:11:32 - Ryan - One Stop Creative Agency: <A>Yeah, I started with one, a company called Postbone. They interface with the APIs of platforms for you, because I figured it wasn't worth me actually trying to integrate directly with Meta and all of that, because they change so often I'd just be constantly trying to keep up with that. So I let them do that, I'd integrate with them. There are some limitations on posting length and stuff on Reels, but that's why I changed or added the Publer option because it has a slightly longer amount and allows you to upload a custom thumbnail.</A>

01:12:22 - Ryan - One Stop Creative Agency: ▶ The idea being that I can at scale onboard clients into there and try to build a little SaaS business of my own. I just did an onboarding manually and it took me the entire day of recording on Granola [tool:Granola], each of those 75 questions of the poor business owner that wanted to kill me by the end of it. So that quiz link will hopefully help in the future.

01:13:00 - Ryan - One Stop Creative Agency: It's using the Anthropic SDK [tool:Anthropic SDK], the TypeScript one, to obviously generate all the written content, and yeah, I'm coding it with Claude Code, obviously, within Cursor, within the terminal in Cursor.

---

<!--SEGMENT
topic: Claude Code as Headless Background Task Processor
speakers: Patrick Chouinard, Jake Maymar, Ryan - One Stop Creative Agency
keywords: Claude Code headless, background processing, YOLO mode, N8N, NetworkChuck, ngrok, local agent, cron job, MCP, skills, agent scaffolding
summary: Patrick describes using Claude Code in headless/YOLO mode as a local background task processor — essentially a pre-built agent that can be triggered to run tasks autonomously without building custom agent scaffolding. Jake asks about exposing this via ngrok for web use, and Patrick references a NetworkChuck video showing Claude Code integrated into an N8N workflow.
-->

01:13:25 - Patrick Chouinard: On local application, I've started to integrate Claude Code itself in the backend function. Because you can call that headless, so it does a lot more than just calling the SDK by itself — you can just give it a task, go do this, then save the result in a file, then reprocess it, then grab all the files and do another process. So you can let it work in the backend as a basically local Claude task — if you want.

01:14:03 - Patrick Chouinard: ▶ Obviously, you don't want to have that as an application that you provide to others, but for internal backend processes, it works pretty well.

01:15:30 - Patrick Chouinard: I use Claude Code as a background task processor for local applications, not for web applications, obviously, not for SaaS applications, but for anything local. ▶ I love to use Claude Code headless as a background processor for stuff.

01:15:50 - Jake Maymar: <Q>Is there any way to, like, ngrok [tool:ngrok] or something like that where you could actually have your system run a local — can a system actually run a local Claude Code instance and expose it?</Q>

01:16:03 - Patrick Chouinard: <A>Then you get into building your own agent scaffolding. I just leverage it locally because it gives me a fully functional agent out of the box with me having to do pretty much nothing. So imagine that you have your own agent pre-built that you can just give instructions to and it's going to go and do it. But again, you have the limitation that it has to run locally. And if you want to have it run in the background, you have to have it run in kind of YOLO mode. So you have to be very careful and control the prompt that it's allowed to execute because it will do anything you ask for in that mode. ▶ So I would never expose that as a SaaS for that specific reason. I'm the one who knows which prompt I will allow it to run automatically in the backend.</A>

01:17:00 - Jake Maymar: I was almost thinking you would get like an email or some sort of notification and then just run that job and then send that job to a location.

01:17:24 - Patrick Chouinard: ▶ Actually, there is a video where NetworkChuck [link:NetworkChuck YouTube channel] does exactly that — includes Claude Code inside of an N8N [tool:N8N] workflow and does all of the messaging.

01:17:37 - Jake Maymar: Oh, very cool. Okay. Thank you. That's awesome, Patrick.

---

<!--SEGMENT
topic: React Security Patches and Package Manager Conflicts
speakers: Morgan Cook, Patrick Chouinard, Jake Maymar, Ty Wells
keywords: React security vulnerability, PNPM, NPM, lock file conflict, Vercel, Next.js 15, Next.js 16, dependency resolution, Trigger.dev, dash cam video processing
summary: Morgan Cook describes resolving a React dependency conflict caused by mixed NPM and PNPM lock files across multiple projects, and patching recent React security vulnerabilities. The group discusses PNPM as the preferred package manager (used internally by Vercel), and whether anyone has migrated to Next.js 16 yet. Morgan also previews upcoming work on dash cam video processing and a Trigger.dev agent workflow.
-->

01:18:46 - Morgan Cook: Hey guys, how's everybody doing? I've just been chunking along, dealt with a React bug this last couple of weeks. I have like four or five sites I had to update and one of them was way far behind. So I had to update a lot and then fix a few dependency issues.

01:19:26 - Morgan Cook: I'm excited to go try the Trigger.dev [tool:Trigger.dev] agent workflow and see how that works for the one project that I have that really needs that.

01:19:46 - Morgan Cook: One of them is processing video from dash cams. And the other one — I want to use it more for the connectivity and network. We're working to get past doing broadcast, so issue a message to Trigger, and Trigger will issue a message out to the subscribed clients without having to use JavaScript to maintain a connection and doing polling.

01:20:32 - Ty Wells: <Q>Morgan, I was just curious what your React error was, because it's always good to share errors.</Q>

01:20:47 - Morgan Cook: <A>Yeah, so what I had was — because I had so many projects, I couldn't remember — in the initial state, I didn't have the right package manager. One of them was using NPM [tool:NPM] and one of them was using PNPM [tool:PNPM], and so it creates a different lock store. And for some reason, this one project had both lock stores in it, which means at some point I switched back and forth. And so then that created a dependency error, because the NPM version was pulling some package that required a sub-dependency, and that sub-dependency was at a different version level. So what I did was basically just get rid of all my lock files and reset my package file to specifically specify the versions that I needed, and switched everything on that project over to PNPM.</A>

01:22:24 - Jake Maymar: ▶ I've noticed that Claude likes PNPM.

01:22:32 - Morgan Cook: Well, I noticed that Claude likes it. And also, I did a little bit of research — Vercel [tool:Vercel] uses PNPM internally. ▶ So if we're hosting on Vercel, it might be easier to do it with PNPM instead of just NPM.

01:23:10 - Patrick Chouinard: <Q>And when you talk about React issue, were you also talking about the couple of little React security issues that popped out last week?</Q>

01:23:20 - Morgan Cook: <A>Yeah, exactly. The mysterious package load that could give you root access to the server. So I wanted to get those patched up. I just wanted to make sure I had it up to date so that I was not seeing the warnings anymore. Because every time I logged into my dashboard, it was like "your site isn't safe."</A>

01:24:01 - Patrick Chouinard: <Q>Is anybody doing any projects yet with Next.js 16 [tool:Next.js]?</Q>

01:24:09 - Patrick Chouinard: Still with 15 on my side.

01:24:14 - Morgan Cook: Everybody's still on 15? I'm scared. I have a non-client app that I need to work on that's just personal things. So I'll probably use that as my sandbox to go test that out and see what kind of changes there are — the middleware and the proxy layer changes. So it's going to be a little bit of a mental challenge to jump through some of the hoops to see what's different.

---

<!--SEGMENT
topic: AWS Infrastructure Security and Agentic DevOps
speakers: Juan Torres, Patrick Chouinard, Paul Miller, Prem, Elena
keywords: AWS EC2, VPC, private subnet, IAM permissions, AWS CLI, Claude skills, MCP servers, DevOps agent, cloud architecture automation, jump box, Boto, CloudFormation, cron job
summary: Juan Torres describes hardening a client's AWS EC2 instance by moving it to a private subnet and removing public IPs in response to the React vulnerability. He then proposes using an EC2 instance with broad IAM permissions as an agentic resource manager for cloud architecture. Patrick recommends wrapping AWS CLI commands as Claude skills instead, and Paul describes building a dashboard to track AWS service state. Prem cautions against adding unnecessary EC2 management overhead.
-->

01:25:26 - Juan Torres: Hey, folks. How are you guys doing?

01:25:44 - Juan Torres: Right now the structure of my project — the project that I'm working for this client — it's within the AWS VPC [tool:AWS VPC], which is its own network. The initial architecture is there are two microservices in an EC2 instance, but I created this EC2 instance — a server, a virtual computer environment — for the backend and the frontend engineers to basically create the web application.

01:26:37 - Juan Torres: Given the threat of the React vulnerability that just came out, I immediately got them to update to the new React patch versions. And then I moved — I cloned the EC2 instance from a public subnet and moved it to a private subnet, got rid of the public IP. So essentially it's enclosed in a private subnet and it has no public IP. I switched some of the SSH connections — the SSH connection was already encrypted, but I'm just going to further seal it off by taking away some inbound rules that are not necessary anymore.

01:27:30 - Patrick Chouinard: Yep. A good thing to do.

01:27:36 - Juan Torres: <Q>Have any of you had experience with — because right now part of the reason I can move fast with the deployment of projects is because I just SSH into the EC2 instance and I can just deploy and test. Have any of you created an EC2 instance to use it as an oracle of resource management within a VPC? What I mean is you use an EC2 instance and give it IAM permissions to be able to create database resources, EC2 resources, maybe even network capacities — and essentially, since you're using your Cursor, whatever agentic IDE you have, if you download the AWS CLI [tool:AWS CLI] within the EC2 instance, you can start commanding the development of resources within the VPC.</Q>

01:29:19 - Paul Miller: <A>What you can do, Juan, is there's sort of a sub-pseudo language for DevOps, running through the CLI stuff, where you could set up a nice little agent with your code, with Claude, to manage turning on and turning off servers. I was getting Amazon builds of services I thought were off. So I built a dashboard that is tracking what was going on, what was going off, and managing all of that. ▶ If you have the CLI instance going, there's some control language that you can push through CLI, some Boto [tool:Boto] stuff that can control that. And it's a really useful way to run things up and run things down if you're really in the Amazon space.</A>

01:30:47 - Elena: <Q>Can you repeat the agent name? And I know that AWS released recently a DevOps agent. I haven't tried, but I'll look it up.</Q>

01:31:00 - Paul Miller: If you get the AWS CLI stuff, as part of the Amazon stack there's a part that manages turning on and off instances. It's that part of the stack that you need to run with CLI, but let me look it up and I'll put it in the chat.

01:32:14 - Juan Torres: I was thinking that maybe that's a way to facilitate even the process of cloud architecture — you can start speaking of agentic capacities for cloud architecture, because then you can just basically tell Cursor, "hey, create an EC2 instance, choose Ubuntu as the operating system," blah, blah, blah.

01:32:38 - Patrick Chouinard: ▶ By the way, there are a bunch of MCP servers [tool:MCP] for managing the AWS environment also. And if you find that part too heavy, you could do a very light wrapping of the AWS CLI using Claude skills — that might be even more efficient if you want to really point on strategic functionality, and then build yourself an agent that uses all those skills.

01:33:10 - Prem: ▶ From your thing rather than getting on an EC2 — ideally the moment you have an EC2 or anything like that, it's another layer that needs to be tightened down, rather than using managed services. The more you get into managed services rather than having a VM, then you need to keep it updated and so on. So I would avoid if possible — just my thought.

01:33:44 - Juan Torres: That is actually a really good argument. I was thinking about it, but then I thought about maybe for security reasons I wanted to containerize the capacity, raise boundaries.

01:34:10 - Prem: The only reason we go to a thing like a jump box is where we kind of put all the resources underneath that, so it just offers one more level of getting in and then controlling all the other resources through that. But if that's not a concern, then probably you can build everything using it. ▶ There's no reason to pay for another EC2 if you can really just call the CLI.

01:35:10 - Patrick Chouinard: ▶ If you have the CLI, just wrap whichever functionality you need inside of a Claude skill and give those Claude skills to an agent and build yourself a local DevOps agent running for you. And I would go with Prem — I would not build that as an EC2 instance because it adds a whole lot of management where you could actually run that as a headless Claude Code functionality locally on your machine, so it would even run as a cron job to do a check every X amount of time and leverage those functionalities easily.

01:36:10 - Patrick Chouinard: ▶ And by the way, if you wanted a trick to build those easily — find the GitHub project that contains the documentation for, for example, Claude — Claude has a documentation GitHub project, same thing for Cursor, same thing for all of them. Import it as a reference in your project, and then just leverage it. If you want to build the best skills for Claude, if you have the Claude documentation project as a sub-module, you can just reference it and say, "go take a look at the documentation in there, build me a skill that will do X, Y, Z with this CLI based on the best practices you can find in the repo."

01:39:05 - Patrick Chouinard: <Q>Prem, you had a question?</Q>

01:39:07 - Prem: <Q>When you say "refer documentation" — are you saying something different, like using Context7 [tool:Context7] as an MCP, rather than what you're suggesting to refer documentation? Just curious.</Q>

01:39:25 - Patrick Chouinard: <A>▶ Context7 is for API reference. So if you want to talk to a system that already exists, yes, awesome. What I'm talking about is, if you want to build something on top of Claude Code, on top of GitHub Copilot [tool:GitHub Copilot], on top of any of those — the best thing is if you include them as a sub-module. Using it as a sub-module, you can create yourself an agent within your project that keeps those sub-modules up to date every single time you reload a project, meaning that you're always going to have the latest and greatest documentation without having to do what Context7 has done in the back end, because you're using GitHub functionality to keep that documentation up to date.</A>

---

<!--SEGMENT
topic: Personal CV Knowledge Graph Builder Demo
speakers: Patrick Chouinard, Juan Torres, Ty Wells, Lan, Paul Miller
keywords: knowledge graph, vector store, RAG, CV builder, Open Router, Gemini, entity extraction, Astro, Cloudflare, GitHub Actions, second brain, HR tool, job description matching, ShipKit RAG template
summary: Patrick demos his vacation project: a personal CV knowledge graph application that ingests a CV, decomposes it into typed entities (experience, skills, projects, etc.) using AI, stores them in a vector database, and allows chat-based updates and job-description-aligned CV regeneration. He plans to extend it into an HR tool for his employer and eventually publish a personal website via Astro and Cloudflare Pages. The group discusses its potential as a "second brain" foundation and an RFP-response accelerator.
-->

01:40:57 - Patrick Chouinard: Maybe I'm going to just do a little sharing on my own. The one project I've been working on during my vacation — I decided to build myself a project for my own: a career knowledge graph.

01:41:26 - Patrick Chouinard: It's basically — I want to rebuild my own personal website that is a way to publish my own CV and all of that. And after thinking about it, I realized that my CV is just a bunch of entity assets reassembled together and could be reassembled for many purposes. And the one thing I hate is whenever my employer comes to me and says, "oh, we have to respond to an RFP, could you send us the version of your CV, but specifically for this scenario?" — and I mean, it's an insane amount of waste of time.

01:42:10 - Patrick Chouinard: [Shares screen] I have an import functionality where I could drop a finished CV. It's going to send it to be evaluated by a bunch of prompts in the back end that's going to decompose the CV into entities — that is experience, projects, skills, a bunch of things. It will post them for review. So you see, you can have experience, project, achievement, skills, education, bio, philosophy, work ethic, interest, strength, goal, others. And it will allow me to review what it found in the CV, update it, modify it, and once I'm done, I can approve it, and that's loaded into a vector store in the back end.

01:43:25 - Patrick Chouinard: I have an intake chat. So basically here I can say, "oh, I'm going to add a new project," so it gives me a start, and then we have a discussion. The back and forth actually ends up allowing me to decide, "okay, now we've defined it enough, write it back to the vector store." So basically it will reformat it as a new project, a new skill, a new promotion, whatever I want, but I don't have to structure it — I just give it the information, it will format it for me.

01:44:11 - Patrick Chouinard: And then I'll be able to extract a CV — rebuild a document to be given to my employer. And the job output — that one is not built yet — this is the big part: whenever they send me a job description, they want to see, does your CV match that? ▶ Just post the job description, it's going to decompose it, it's going to query the vector database, rebuild a version of the CV specifically towards that job description.

01:45:03 - Patrick Chouinard: And finally, the publish function — the goal here is it will build the website in Astro [tool:Astro] as a static site with all my information. This application being the backend that I manage. The front end that is going to be on the internet — my personal website — is going to be what's deployed. I leverage GitHub Actions [tool:GitHub Actions] in the back end to build and publish to Cloudflare [tool:Cloudflare].

01:45:42 - Patrick Chouinard: So yeah, this is an implementation basically between the RAG and a chatbot, because I wanted Open Router [tool:Open Router] in there, and the RAG is only using Gemini [tool:Gemini], so I had to bring all the Open Router functionality plus the chat. And the settings and configuration — right now I preload all of my models. I made the configuration allowing me to have eight different models for the different steps in the process. So I can say that for the intake, I want the chat model that's going to be fast; it doesn't need to be extremely brilliant. For the digestion of the CV, I want something a lot more structured. ▶ So I managed to have all the models that can be leveraged, and also it's not killing speed and it's not killing my budget either by taking the most intelligent model for everything.

01:47:18 - Patrick Chouinard: <Q>Does it connect the description of the job in order to transform the restructuring of the CV?</Q>

01:47:29 - Patrick Chouinard: <A>Not yet, but that's the goal — that I could submit a job description and it will give me my CV aligned as much as possible. ▶ The goal is I don't want to invent any information. I just want to pick through my CV content everything that applies to that job description. Basically, my CV is now a vector database, so I can query it and think about it, add it, multiply it, transform it any way I want.</A>

01:48:15 - Ty Wells: <Q>How much time does it save you?</Q>

01:48:18 - Patrick Chouinard: <A>I'm going to be able to tell you once I have fully materialized the solution, but knowing that every month I spend at least three or four hours on that every month, and it's the part of the month I hate the most — just one hour less doing that manually is going to be worth 20 hours to build it.</A>

01:49:06 - Patrick Chouinard: ▶ I'm building it for myself as a proof of concept, but the idea is I want to reuse it internally at the company I work for. I want that to become basically an HR tool for them — so they can internalize a vector database of all their resources, not just having a CV database, but a vector database of the resources that they have.

01:53:19 - Patrick Chouinard: ▶ Everybody's talking about "second brain, second brain, second brain," and you hear that a thousand times a day. The problem is the implementation of second brain today is just the memory module, and a second brain is far more than that. You need your neocortex, you need all of the parts of the brain to work together. This is a very, very basic but a start — so I don't start with just text, I start with a vector store. And then you can build a lot more intelligence on top of a vector store than you could on just a static amount of text.

01:54:10 - Patrick Chouinard: ▶ By defining a knowledge graph behind the scene with all of the entities — and this is also something that I'm building in there to have a full knowledge graph so I can navigate the knowledge space as well — you can define that this type of entity is part of the CV, those are not, they're just background information, and continue on building.

01:54:53 - Paul Miller: Thanks for hosting, Patrick.

01:54:57 - Patrick Chouinard: My pleasure. And you're going to be stuck with me also next week, but after that we have the grand return of Brendan.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names were not found in the SPEAKER_ALIASES context block (which was not provided) and have been passed through unchanged:

- **Lan** — asks multiple ShipKit setup questions
- **Elijah** — brief appearance at 00:26:03, no substantive content
- **Elena** — asks about AWS DevOps agent at ~01:30:47
- **Prem** — multiple substantive contributions throughout; full surname not provided
- **Hemal Shah** — multiple substantive contributions; passed through as-is
- **Juan Torres** — multiple substantive contributions; passed through as-is
- **Morgan Cook** — multiple substantive contributions; passed through as-is
- **Jake Maymar** — multiple substantive contributions; passed through as-is
- **Paul Miller** — multiple substantive contributions; passed through as-is
- **Garron Selliken** — multiple substantive contributions; passed through as-is
- **Ryan - One Stop Creative Agency** — passed through as-is (display name, not a personal name)