=== SESSION ===
date: unknown (transcript timestamps span 00:08:00–02:10:24)
duration_estimate: ~2 hours
main_themes: ShipKit template onboarding, agentic workflow development, enterprise AI evaluation, social media automation SaaS, automotive WhatsApp/voice agents, compliance/certification, kiosk applications, personal AI infrastructure, consulting disruption, travel planning tools, local models and tooling

---

<!--SEGMENT
topic: Session Opening and ShipKit Onboarding
speakers: Patrick Chouinard, Brandon Hancock
keywords: ShipKit, custom GPT, template selection, onboarding, Claude Code, Discord, RAG template, TinySeed, startup, prompt engineering
summary: Patrick shares work-in-progress on a custom GPT that analyzes ShipKit codebases to recommend which template to use for a given project, addressing a chicken-and-egg onboarding problem. Brandon provides context on his TinySeed acceptance and a passport emergency that disrupted travel plans, then endorses Patrick's approach and commits to overhauling the ShipKit onboarding experience upon return.
-->

00:08:38 - Patrick Chouinard
Hey, Brandon.

00:08:40 - Brandon Hancock
Yo, yo, what's going on, Patrick?

00:08:45 - Patrick Chouinard
Still, I'm actually working on something that popped up in Discord today.

00:08:51 - Brandon Hancock
Oh, what was it?

00:08:54 - Patrick Chouinard
The request to have a way to, out of the first prompt, identify which template it should be used with.

00:09:03 - Patrick Chouinard
So I've cloned all of your repo, and right now I'm analyzing it to create a file that will contain that, that I will add to my custom GPT [tool:custom GPT].

00:09:14 - Brandon Hancock
Oh, that's sick. Which — interesting — no, that makes sense. Because that was one of the issues I ran into, was like, it's a chicken-and-the-egg issue: oh, download the prompt, or download the project to get the prompts.

00:09:35 - Brandon Hancock
Are you thinking a community thing, or were you thinking put it in your GPT?

00:09:40 - Patrick Chouinard
▶ Yeah, I'm going to put it in my GPT, but I'm also going to publish the updated code in the community as well.

00:09:54 - Brandon Hancock
It's funny. I've been so swamped. Just a quick update before we dive in. So I think I mentioned to you guys a little while ago, I got accepted into TinySeed [tool:TinySeed] for a startup, which was kind of based off the RAG template [tool:RAG template], and so we literally all week have been traveling to do a kickoff. I was supposed to be gone today — except my wife's passport expired, so we realized that yesterday at 10am, and we were supposed to fly out today at 10am. So we had to sprint to the passport embassy, but we got it, so we get to fly out tomorrow. Very stressful 24 hours, but it's all figured out.

00:10:52 - Brandon Hancock
Thanks for being flexible on adjusting for a Monday call. Patrick, you're up first, so if you want to kick us off, we'd love to hear what you've been up to.

00:11:15 - Patrick Chouinard
Well, basically, you've heard what I've been up to in the last couple of hours. It's something that popped up in Discord today, like mid-afternoon.

00:11:30 - Brandon Hancock
▶ No, 100% needs to exist. The second we get back, I really want to redo the onboarding experience to answer that question — literally probably have some training on, like, what template should I use? Just so you could ask ShipKit [tool:ShipKit] itself which one to use for this project, and have it tell you.

00:11:46 - Patrick Chouinard
Yeah, well, you're probably going to be able to steal a couple of lines of what I put in the custom GPT to do that. All the files I'm extracting — basically I'm analyzing each codebase and extracting the information, specifically what I asked Claude Code [tool:Claude Code]: extract all the information and put it in a file, the information that's going to be needed for another agent to be able to read and define which template to use to implement a project.

00:12:20 - Brandon Hancock
That's going to be awesome. Thank you so much for diving in, Patrick. Anything we can help with on Ayura?

---

<!--SEGMENT
topic: Enterprise AI Platform Evaluation
speakers: Patrick Chouinard, Brandon Hancock
keywords: enterprise license, OpenAI, Anthropic, Gemini, Perplexity, token pool, provider evaluation, multi-provider strategy, confidence scoring, Claude Code
summary: Patrick describes leading an enterprise-wide evaluation of all major AI platforms — OpenAI, Anthropic, Gemini, Perplexity — noting that enterprise agreements include tools and capabilities absent from public tiers. He outlines a confidence-scoring framework that tracks providers daily and adjusts scores up or down based on new information, avoiding long-term lock-in to any single provider.
-->

00:12:30 - Patrick Chouinard
There's one part that's job-related. I have to be careful about how much I share, but basically I'm going to end up with an enterprise license for all of the major platforms in order to do an evaluation. So that's OpenAI [tool:OpenAI], Anthropic [tool:Anthropic], Gemini [tool:Gemini], Perplexity [tool:Perplexity], all of them.

00:12:57 - Brandon Hancock
<Q>Is this more of a — your company has a set of tasks that you want to evaluate each one against, to figure out which one's the right one for the right task?</Q>

00:13:08 - Patrick Chouinard
<A>That's the part I have to be careful about not going into too much detail, but let's just say I'm going to have to evaluate every single aspect of every single platform in their enterprise version. And I've already realized that there's a bunch of stuff in the enterprise version that is not present in the public version.</A>

00:13:38 - Brandon Hancock
Hey, after you go through that, I'm sure there's going to be a ton of golden nuggets. So if there's anything — if you're like, hey, this is the model for enterprise, don't ask questions, just use this — that would be very helpful.

00:13:44 - Patrick Chouinard
I don't think that's going to be the answer. Enterprise agreements are different because they come with a bunch of tools and assets on top. And I don't think — with the speed at which the market is changing right now — that it makes sense to bind yourself to a single provider for any length of time. ▶ So have an agreement with most of them, just decide where you send your tokens at any point in time.

00:14:31 - Patrick Chouinard
Basically, what I'm building — and I've been at it for only two days — is basically the Gemini search agent that you've been working on? I've actually tried it with Claude Code. Incredibly, it's far more powerful than Gemini CLI [tool:Gemini CLI] to do that.

00:14:55 - Brandon Hancock
Real fast, guys — what Patrick's talking about: you can basically create your own custom research where you come up with a ton of search terms and kick off dozens of agents at the same time to go off and search a bunch of different terms in parallel and basically put together findings. It was like a really cool custom way of doing deep research. Patrick was using Gemini CLI because you get access to Google search. But I'm pumped to try it now with Claude Code to see if it works even better.

00:15:41 - Patrick Chouinard
▶ Claude Code has a way to mix web search and fetch with web scraping. And the way we structured the prompt, it's basically analyzing every provider every day and gathering the information so we can have an evolution curve to see which provider becomes interesting — it tracks everything: news about Code Red, something Sam Altman said, the release of a new model. Actually, I learned doing that today that ChatGPT 5.2 is going to be released tomorrow.

00:16:38 - Patrick Chouinard
It's basically the inverse of deep research. Deep research is a drill — one subject, very in depth and in detail. This one is horizontal.

00:16:49 - Brandon Hancock
Oh, go wide. I see what you're saying.

00:16:53 - Patrick Chouinard
Exactly. And basically, when you have no limit on tokens that you pay for yourself, it's incredible what you can do with the tool.

00:17:06 - Brandon Hancock
<Q>Patrick, are you on the $100 plan or the $200 plan?</Q>

00:17:08 - Patrick Chouinard
<A>Personally I'm on the $100 plan, but the enterprise ones are unlimited. You basically buy a token pool that is used by all the users of the agreement.</A>

00:17:39 - Patrick Chouinard
So right now I just wrote the prompt to do that, but I also want to write a lot of internal analysis. We're going to dump all of our business requirements into that project, and I want to leverage cross-analysis between the result of the search and — basically we decided to start with the conclusion, with a degree of confidence. Every day we run all the searches, we will update the confidence level either up or down. ▶ If we go down below a threshold, we're going to scrap the solution and change our approach. If we go up over a certain threshold, we're going to state that this is the adopted one and go with it.

00:18:22 - Brandon Hancock
Dude, I love that you're leading the enterprise adoption at your company. It's very cool to hear what's going on in the real world at scale. Please keep us in the loop, Patrick.

---

<!--SEGMENT
topic: Scott's Parallel Agent Morning Summary App
speakers: scottrippey, Brandon Hancock
keywords: parallel agents, aggregator pattern, Anthropic TypeScript SDK, Google APIs, Claude, Haiku, Sonnet, Trigger.dev, Next.js, Netlify, prompt engineering, context window management
summary: Scott demonstrates a personal productivity app that runs multiple AI agents in parallel — course summary, follow-up check, and relationship check — each with its own context window, then aggregates results. Built on the Anthropic TypeScript SDK with Google API integrations for email, calendar, and tasks, the app also features a chat interface with prompt improvement suggestions and scoring. The segment covers context window management strategies and the decision not to use Trigger.dev for this internal tool.
-->

00:19:18 - scottrippey
Hey guys. So yeah, nothing much here other than — let me share and show you what we were talking about online. One of the ShipKit calls was the parallelization and the aggregator and that whole thing in my app.

00:19:39 - Brandon Hancock
Scott's building a really cool agent tool to help automate a lot of what he's pulling up right now. He has built out a bunch of different agents to automate parts of his day. What you can see right now is a very cool morning summary — basically each one of those different agents does a different thing. We were brainstorming together how we can speed things up. We talked about using a tool called Trigger.dev [tool:Trigger.dev], and they make it super easy to do a bunch of agentic workflows. So, dude, how did it go? Were you able to dive deeper into it?

00:20:14 - scottrippey
Yeah. So basically what I did was I was thinking about doing something in parallel and I just took a screenshot of a workflow from Trigger.dev to give it extra context when I was building this. So we're not using Trigger.dev at all — this is still internal. But the cool thing now is this is all in one. Because I remember before I had this as its own thing and relationship check was its own thing. What we were talking about was: why don't we make this where the course summary, the follow-up check, and the relationship check all run in parallel at the same time with our own API calls.

00:20:55 - scottrippey
I can see the hard-coded system prompts because I wanted to see them. I've got Claude APIs [tool:Anthropic TypeScript SDK] hooked into this where I have a big system prompt, and I can suggest improvements. This is like my system prompt for chatting in this side window against everything, where I can go, hey, what are my tasks for the week? I've got Google APIs [tool:Google APIs] plugged into this, so I can get emails, meeting notes, tasks, all kinds of stuff.

00:21:50 - scottrippey
You can have your four favorite prompts just sitting here and name them whatever you want. That's Haiku [tool:Claude Haiku], that's Sonnet 4.5 [tool:Claude Sonnet 4.5]. You can upload more context here if you want to do more than your system prompt. I actually have two different email signatures, I can make one or the other active even within the same chat. I can have this actually send email, send out meeting invites — it'll do it all from the chat.

00:22:35 - scottrippey
<Q>Quick question — on the emails, are you using an SMTP tool, coded yourself, API calls, what's going on?</Q>

00:22:47 - scottrippey
<A>So all of this is built on the Anthropic SDK, the TypeScript one — it's like the agent tool call on this — and the Google APIs. So I'm basically using those two together. I'm hooked right into my Google APIs. I got the secrets from Google Console. I'm not using any MCP in this.</A>

00:23:16 - scottrippey
The cool thing I did, Brandon, was: if we're in here doing this, I can still put in some custom behavioral instructions that add to the aggregator at the end after it all comes in. So I can be like, hey, prioritize this or do that — just some extra little behavioral guidelines. And when you suggest improvements, it'll actually give you different options and you can click them, and it'll start giving you a score.

00:24:00 - scottrippey
The next step — what you and I were talking about — is combining this with the other thing we saw on Trigger.dev: doing a loop for quality, a pass-fail, and then some sort of loop when it gets to the aggregator.

00:24:28 - Brandon Hancock
So if you guys are ever working on a task where you basically want the AI to just continue to work on itself, one of the easiest patterns to do is this one — where you have one agent do work (the generator, the worker bee), then you have an evaluator who's basically saying, hey, that worked, or no, it didn't. And if it doesn't work, we also provide feedback, so that whenever it comes back to the other agent after the full loop, it's going to say, hey, try again, but here's additional feedback on what you need to do differently. ▶ It takes a little bit longer, but it produces really high-quality results. So if you're working on nebulous tasks and you just want to make sure you get high-quality results, this is a really cool way to have the agents work and critique, work and critique, until they get the desired output.

00:26:06 - Brandon Hancock
<Q>Scott, quick question — what happens if the output from all of your parallel tasks exceeds the context window? Have you run into that?</Q>

00:26:43 - scottrippey
<A>So I have hard-coded a few things and there are certain things I put as settings. I was running into that problem — it was actually timing out because of that. Before I started doing this parallel thing, it was trying to do like a hundred emails, or a hundred days. I was like, no, I only need like the last seven days. So I have all these parameters where it's never going to be so much data that'll fill up the context window. It only does meeting notes if it applies to something, and those are summaries, not full transcripts. And by splitting them into separate calls, each of them has their own context window now.</A>

00:29:32 - scottrippey
<Q>Are you using Vercel AI SDK and then using Claude Code, or are you specifically using Claude's SDK?</Q>

00:29:46 - scottrippey
<A>▶ It's basically just a standard TypeScript Next.js [tool:Next.js] application — no Vercel SDKs or anything. It's just the Claude Anthropic TypeScript SDK. It's not the agent SDK — I got confused about that. The agent SDK I think is for more things like Claude Code.</A>

---

<!--SEGMENT
topic: Ryan's Social Media Automation SaaS
speakers: Ryan C, Brandon Hancock, scottrippey
keywords: social media automation, Nano Banana, image editing, Cloudflare R2, Supabase, Netlify, Claude, brand voice, client approval workflow, GitHub, task-based development
summary: Ryan demos a social media management platform that generates a month of posts using Claude, allows AI-powered image retouching via Nano Banana 3 Pro, and stores media in Cloudflare R2. The app supports client-side approval and amendment workflows. Discussion covers Claude Code going rogue by changing undocumented code, the importance of task-based development with artifacts, and using git commit shortcuts to preserve history.
-->

00:33:26 - Ryan C
I'm currently doing extra lots of battle with Netlify [tool:Netlify] and Claude Code because it keeps failing to build something that it was building perfectly fine earlier today. It's changed something I didn't ask it to, and now I can't figure out what has changed. So I'm currently smashing my head against the brick wall.

00:33:47 - Ryan C
But I've made quite a lot of progress on my social app. Last time I talked about it, I was working on building an application to automate social media posts. And Scott has already told me off today for this, but I'm reaching and singeing my fingers and my hair. I'm one of those people that has lots of ideas and I go, oh, that's cool, I'll just add it. So I've now integrated Google and Nano Banana 3 Pro [tool:Nano Banana 3 Pro] to do retouching and complete image generation all within the application with a full preview shown, and then accepting and overriding of the original image if I want to keep that.

00:34:37 - Ryan C
It saves me having to pull it out and edit it in Photoshop [tool:Photoshop] and then put it back in. I can just edit it in the platform.

00:34:49 - Brandon Hancock
<Q>So you're saying something changed with a model?</Q>

00:34:56 - Ryan C
<A>No — Claude Code has changed something in the back end of how I was API-ing into it and it's broken it. It's now going around in the doom loop trying to figure out what it is. I may have been back to the conversation about 15 times today, and it's now hallucinating. So I need to clear that down and get it to start thinking about it again from scratch.</A>

00:35:11 - Brandon Hancock
▶ Super fast, two tips on the software development life cycle approach. The way I'm building out all startups is I do everything task-based, where I end up creating an artifact of: here's the task, here's the plan, here's the code changes, here's the test. That way for each change there's an artifact associated with it. So if I ever have to go back, I mean, ideally you're committing along the way, but if not...

00:36:15 - Ryan C
So this is the dashboard and this is the demo company. When I press "generate first month," that all links in with Claude. It generates a month's worth of posts from the stuff that's uploaded in the content bank. You can upload galleries in here and stuff to post to Instagram [tool:Instagram]. All that fun stuff. You can download it. And that's all linked up with Cloudflare [tool:Cloudflare R2] as the bucket to hold all of this.

00:36:57 - Ryan C
And then if you go into something like this, press edit, you've got "enhance with AI" in here. I've had it change a uniform to blue multiple times, and then the preview will pop up there, and the idea being I could save the preview and just overwrite the other one in the database.

00:37:28 - Ryan C
Nano Banana is literally it on the image side. Claude [tool:Claude] for any social media writing — I've got a big prompt system where I'm doing system prompt, then framework, then client stuff. I've got a whole load of client information in the background that it pulls in as part of the client prompt: brand voice, brand context, all that sort of stuff. And then it feeds through the images and all the descriptions so Claude knows what it's looking at to write the prompts. It pushes through to the client side — the client can then approve or request an amendment, which then sends it back to Claude to amend with some notes they put in.

00:38:22 - Brandon Hancock
<Q>Are you a Supabase man? What are you using for your blob store?</Q>

00:38:32 - Ryan C
<A>I'm just a Scott Acolyte here, so I use everything he uses. GitHub to Netlify, Supabase [tool:Supabase] for database, Netlify to build it, and Cloudflare R2 for media. I don't want to smash my Supabase, so I've set up a Cloudflare R2 bucket for all the media, which works perfectly.</A>

00:39:23 - Brandon Hancock
▶ One thing, Ryan — I just make instructions like a one-time thing, a prompt, and basically you get to commit faster. Anytime I'm coding, I can just do `git workflow commit` and it just instantly looks at all the changes and does it all. So it's super easy — I just make a Claude command to kick off the workflow to commit the changes, and then I go back to working. Just fire and forget it to at least commit, so you can always go back in case something goes wrong.

00:40:46 - scottrippey
I literally just say, "hey, commit this to GitHub" — that's literally all we do. And it always picks good messages.

00:41:34 - Brandon Hancock
▶ Ryan, you're doing this textbook. You have a service you're already offering right now that's generating money — that's all the proof you need. So now it's just: instead of me doing all the work, why don't I build systems to do it for me? A lot of times it's very easy to forget it's software as a service — does the service actually provide value? Ryan's done that, so now it's: cool, now I'm going to throw in the software.

---

<!--SEGMENT
topic: Maksym's Automotive WhatsApp and Voice Agents
speakers: Maksym Liamin, Brandon Hancock, Ryan C
keywords: WhatsApp chatbot, voice agent, automotive, Nissan, Mazda, Infiniti, RAG, LiveKit, Kimi K2, CRM, Salesforce, lead tracking, B2B, Mexico City
summary: Maksym shares progress on AI-powered WhatsApp and voice agents deployed for automotive clients Nissan, Mazda, and Infiniti in Mexico, now serving ~8,000 users. The system handles pricing queries, photos, videos, and technical sheets for both salespeople and end customers. A new lightweight CRM feature captures leads via simple WhatsApp messages and sends real-time reminders, replacing end-of-month data dumps. Brandon suggests a sales training voice agent as an adjacent product opportunity.
-->

00:44:32 - Maksym Liamin
Hi, how are you doing? I'm in Mexico. I finally set up, did all my papers, rented the flat — I have my temporary residence now for one year, and then can extend it up to four.

00:45:08 - Brandon Hancock
So, dude, Maksym, last time we talked you were doing a ton of cool RAG stuff. You were also starting to get into voice — LiveKit [tool:LiveKit], Kimi K2 [tool:Kimi K2], with some self-hosted stuff. What's been going on?

00:45:25 - Maksym Liamin
Yeah, so we keep working with Automotive. We onboarded two more clients, which is Mazda and Infiniti. We have one solution that was already working — if you remember, we were doing it with Nissan. It has, cumulatively, around 8,000 users right now. It's for salespeople — basically field sales. It's a chatbot in WhatsApp [tool:WhatsApp] that you can ask any questions on pricing, it gives you credit data, photos, videos of the cars, whatever it is, all different colors, and it answers you. The other application is client-facing — basically the same, but now without a salesperson. You just talk to a WhatsApp contact and it gives you all the information on pricing, crediting, photos, videos, technical sheets. And you can also call it, so it also works as a voice agent and can give you the same info via voice.

00:46:31 - Brandon Hancock
<Q>For the voice side — do they still have sales agents at all, or are they trying to get rid of them?</Q>

00:46:38 - Maksym Liamin
<A>No, it's still in — it's very big companies. These kinds of products are still in early testing. They send us leads, maybe 300 to 500 people per week. But obviously it's nothing in comparison to full capacity. We still need to do a lot of checks and tests, and maybe in the next year we can have it fully working, but it's somewhere in the middle of beta.</A>

00:47:17 - Brandon Hancock
▶ Cool idea one — either add to your current one or build a second SaaS: a tool to train the sales guys. A lot of times guys aren't following the scripts, they're not handling objections well. You want to practice against an LLM that costs a few dollars for a call rather than losing a customer that could have been worth thousands. You're already in the market, you already have great connections with these customers — you really could start to make a sales voice training platform. You're basically building a portfolio of products around a very profitable customer.

00:49:08 - Maksym Liamin
Yeah, that's a great idea. Actually, talking about business ideas — we recently also introduced a kind of CRM [tool:CRM] to our tools, all the salesperson-facing tools. The point is that all these companies have CRMs like Salesforce [tool:Salesforce] or in-house built CRMs, but nobody really uses them — only at the end of the month, in the last day, because they get paid based on what they put in. So we started incorporating lead tracking to have it very easy and simple for them: they just send a name, phone number, and car of interest, and it's already registered in the system. They can query those and check follow-ups.

00:50:00 - Maksym Liamin
▶ The biggest advantage is that now these companies actually see what their salespeople are doing throughout the whole month, not just at the very last moment. There's a full progression. We have direct reminders in WhatsApp that come to their phone and tell them when to do what they put in.

00:52:00 - Maksym Liamin
Actually, last week — do you know a company called Poke? It's like an iMessage companion. It's a company from San Francisco. They do all kinds of things with your emails and calendars and automate it — like a personal assistant. They're in a very early stage, but they got big investments in SF. So we took their idea literally last Thursday, built it so it was ready on Friday, and went to some schools because we've been recently invited to universities to give talks. And yeah — it connects to your calendars, Booking.com, whatever you connect with, and can do a lot of stuff, all via iMessage [tool:iMessage].

00:53:27 - Maksym Liamin
We basically decided to try something like this here in Mexico. It's a first attempt at B2C, because we've been always working B2B with these big industrial companies. We went first time B2C to some schools where we've been giving talks to entrepreneurship students, and then we got our first batch of beta testers. It connects to Gmail, you can connect it to multiple accounts, you can send emails, forward, reply, schedule events, get notifications for your reminders, connect to documents, ask questions about documents in Google Drive.

00:56:00 - Ryan C
If you're ever in the UK, give us a shout, because I know the directors at Renault. I used to be an account director at Renault, so I know a lot of people over there. I know the managing director of UK Renault, and he runs some of Europe as well. And their CRM system sucks, so I know he's always on the lookout for stuff.

---

<!--SEGMENT
topic: George's GRC Automation SaaS Concept
speakers: George Kurian, Brandon Hancock
keywords: GRC, compliance, audit, policy automation, agentic workflow, worker SaaS template, Supabase, Next.js, Trigger.dev, RAG, VectorStore, SMB, enterprise
summary: George, a first-time caller, describes plans to automate governance, risk, and compliance (GRC) workflows — aligning regulatory policies to application-level audit evidence — using agentic pipelines. Brandon recommends the worker SaaS template for sequential workflows and outlines the core ShipKit tech stack (Supabase, Next.js, Trigger.dev, Google Cloud VectorStore). Discussion emphasizes starting with a specific customer persona and mapping their daily tasks to identify automation opportunities.
-->

00:56:47 - George Kurian
So yeah, this is the first time I'm really joining the call. I started using the product recently. I do some GRC work. Part of that is helping SMBs put together their policies and standards and a lot of that stuff, and I want to automate that with an agentic workflow — getting their regulatory alignment with the policy and then driving a lot of the underlying standards and procedures off of that.

00:57:30 - Brandon Hancock
What you're doing is the wave that is about to happen. It kind of started off in N8N [tool:N8N] land of, like, oh, make an automation. N8N was great at that, but now that these tools have become so much easier to use, there are so many more tools and frameworks — it has become so much easier to actually just build an actual SaaS around it. ▶ Companies are spending, like, half a million dollars a year just on doing reviews, and AI could do that — the entire true cost for the whole year might be $50 in AI credits. So that is a 100x delta between what AI can do versus manual tasks. This is what 2026 is going to look like.

00:58:47 - Brandon Hancock
▶ I could say the worker SaaS template [tool:worker SaaS template] is the right template for what I think you're about to start doing, where you're going to be kicking off a bunch of sequential workflows — do A, then B, then C, then D. Here's the input, here's the output. That's the approach you're talking about.

00:59:15 - George Kurian
Like, one is just putting together the workflow that will generate the documentation. And then there's all the evidencing that auditors usually use based off of that documentation. The idea is that there's a ton of tools right now that companies have bought that basically use APIs to gather information and put it in a data lake. But they don't have the context of where in the audit the evidence they've collected lines up, because they don't know the application very well. Most of these audits are aligned to the application. So I'm going to start all the way on the left-hand side with a lot of the policy and make sure everything is aligned first, and then start working with maybe a couple of different areas on the infrastructure side to collect information and create a new repository, and then use that to surface all the evidence.

01:00:50 - Brandon Hancock
▶ One other quick alternative approach: almost look at the customer — pick a specific customer, a specific job role. The more concrete we can break down what they do in a day — a quick matrix of what they do, how much time they spend per task per day — you almost come up with a matrix of: here are the 20 things they do, and these bottom five take up so much of their time and are easy to automate. Those are the best low-hanging fruits to tackle.

01:02:22 - Brandon Hancock
▶ In ShipKit, the main tech stack we use and recommend for everything — it checks all the boxes for 90% of people — is Supabase [tool:Supabase] because it is Auth, Database, and Blob Store. Then Next.js [tool:Next.js] for the actual tech stack. And then we usually add supplementary tools depending on what you want. If it's a RAG, we need a VectorStore [tool:Google Cloud VectorStore] — we already have one built for you on Google Cloud, automates the whole process. If you need a bunch of background tasks, Trigger.dev [tool:Trigger.dev].

---

<!--SEGMENT
topic: Ty's Kiosk App, Personal AI Infrastructure, and Hackathon Projects
speakers: Ty Wells, Brandon Hancock, scottrippey, Glenn Marcus, Tiran Dagan
keywords: kiosk, Windows application, Rust, Claude Code, VPS, Docker, ElevenLabs, voice agent, PECAN AI, machine learning, XGBoost, Fire Stick, AWS Rekognition, Whisperflow, parallel agents
summary: Ty shares three projects: a Windows kiosk application built with Rust via Claude Code and deployed through GitHub Actions; a remote personal AI coding assistant running Claude Code on a VPS with Docker, accessible from mobile with ElevenLabs voice feedback; and a PECAN AI-style ML prediction platform for SMB data. Glenn contributes kiosk industry expertise from his NetKey/NCR background. Discussion covers Mac setup tips, parallel agent token burn rates, and voice-to-code workflows.
-->

01:03:19 - Brandon Hancock
All right, Ty, what's up, man?

01:03:27 - Ty Wells
I've got more questions than I have show-and-tell. I finally got a MacBook. So if you have any guidance on setting up the environment, that'd be great. I'm not a Mac person at all — I'm Windows.

01:03:50 - Brandon Hancock
▶ The main things I would recommend buying instantly: Presentify [tool:Presentify], eight bucks; Amphetamine [tool:Amphetamine], six dollars — it keeps your computer on so it doesn't always close out; and Magnet [tool:Magnet]. So what I can do is hit Control-Option and I can just move stuff around on my screen. The second you get used to those Magnet shortcuts, oh my God, it's so beautiful.

01:04:44 - Ty Wells
I'm working on a couple of projects. I haven't gotten back to ShipKit Studio because I'm in a hackathon. The other question I had was: I'm building a kiosk application for my business — we have like 50 kiosks and I'm adding voice to it, but I'm rewriting the entire application. They run on Windows machines. I'm building this in Next.js for the event space. <Q>Is there a way to build a Windows application through Claude Code?</Q>

01:05:34 - Brandon Hancock
<A>Electron [tool:Electron] is like the first thing that comes to my mind for making desktop applications that work for Windows or Mac. And compiled Python — there's a tool that lets you convert Python to executables for both Linux and Windows.</A>

01:06:00 - Ty Wells
What I did was I built a Rust [tool:Rust] application through Claude Code, deployed it over GitHub Actions [tool:GitHub Actions], and just downloaded from there. So I never touched any other environment outside of Claude Code to build that, because it needs a launching application that launches the kiosk software, which then obviously is a web view of the kiosk that's running.

01:07:00 - Brandon Hancock
What you usually do is you can update your systemd records so that whenever the system boots, it can auto-start certain applications. You can turn off other background processes. ▶ Ideally, whenever the computer boots up, you turn off the bottom Windows bar, make the background the company logo so it looks like a loading screen while your application is booting up. Then your application launches. Not only does the systemd record say auto-launch, but it also says: if this crashes under any circumstances, always force reboot.

01:07:53 - Tiran Dagan
Just setting up a virtual machine that's configured — you have an image that you can reload in case something happens.

01:08:47 - Ty Wells
Okay, so this is what we're building. I don't know if you guys are familiar with PECAN AI [tool:PECAN AI]. They're data modeling, machine learning, for predictions. So we're doing this — it allows small businesses to go ahead and do predictions on their data for different use cases. Like customer — typical stuff that Amazon and stuff do, presenting options to buy this or that. So that's what the platform is about.

01:10:00 - Ty Wells
So I've got some data actually from that kiosk that I'm trying to — since I'm rebuilding it — I'm trying to present the next possible thing that they should purchase. Machine learning obviously does regressions and classifications, so it would take that data and try to regress it to come up with patterns. I can choose a use case — in this case it would be like product recommendation. Then it will learn that data through regression models, probably XGBoost [tool:XGBoost] for the most part — it's a combination of models depending on the use case. And then I can make predictions off of it: will this customer churn, or that sort of thing.

01:12:12 - Ty Wells
▶ This is an expensive effort for enterprise. So we're building this for SMBs. Small businesses don't really do anything with their data — their customers come in, they buy what they buy, but they don't really take advantage of that data and use it to predict, to reach out to that customer and say, hey, we saw you purchase X amount ago, we have this new product.

01:13:04 - Tiran Dagan
▶ If you haven't done it, you should build a bridge to SAP [tool:SAP]. SAP is entering into the SMB market. The $1,000-sized companies might be the sweet spot for you.

01:13:21 - Ty Wells
I'll share one other quick thing. I don't know if you guys are familiar with Daniel Messer's personal AI infrastructure? Basically, this is my ability to chat with — it's a remote coding agent, if you will, because I work on multiple projects. But every time I leave my computer, it's over — you can't do anything from my phone. So this is connected to a VPS [tool:VPS] that has Claude Code on it, that has Docker [tool:Docker] on it. I can pull down my repos to that instance on the VPS, and then communicate with that.

01:14:38 - Ty Wells
Files plus tools, plus agents, plus skills — I've got all these agents here I can call on to do whatever. Claude's streaming back over, tracking that stuff. I've got as many skills as I want. He uses something called Fabric [tool:Fabric], which is similar to a skill. And then I've built in a voice too. I've got an ElevenLabs [tool:ElevenLabs] voice that I can have play back. Like if I'm driving and it comes back and says, this is an issue, I can respond via voice and say, okay, we'll do this or that.

01:16:34 - Ty Wells
<Q>Are you thinking just like, hey, this is my unfair advantage? Or are you thinking, oh, I could maybe turn this into something else?</Q>

01:17:05 - Ty Wells
<A>I know there are privacy concerns. Really, it's for me because it helps me continue to be effective no matter where I'm at. I can check in just like I check my email, see that a particular project needs a response, send that off, and have it continue doing what it needs to do.</A>

01:18:36 - Ty Wells
Can tell you, Anthropic is doing something right, because yesterday I burned through $300 — I was over my limits, just last evening.

01:18:55 - Brandon Hancock
<Q>How did you do that, just out of curiosity?</Q>

01:18:59 - Ty Wells
<A>Parallel agents. I had four projects going, and I had parallel agents — probably about three different agents with sub-agents. I was just watching, all I was doing was refreshing my usage page, and it was just churning through the tokens.</A>

01:19:25 - Ty Wells
I think that's a badge of honor, man. The amount of work that got done — I got it all done last night, as opposed to stretching it out.

01:19:42 - Brandon Hancock
So, Glenn, you mentioned you used to work at NetKey, a kiosk management company?

01:20:16 - Glenn Marcus
My knowledge is about 20 years old now. But back when we were doing it, it was all Windows-based. The poor tenants of the platform were: being able to lock down a computer — a Windows machine sitting out on a store floor, people are going to try to hack in. So we were doing kernel modifications and OS modifications to lock down the device. Fleet management was a big deal. We had Target with 9,000 kiosks nationwide. Being able to remotely control, reboot, update, check status of all those — before we had any Google Analytics — was always a big challenge. We also bought a digital signage company. ▶ All the signs in Times Square were actually being run by my software — 80% of all Times Square screens are running on our software. We revamped their software, then sold to NCR [tool:NCR] for a nice little exit.

---

<!--SEGMENT
topic: Tiran's Portfolio of AI Tools
speakers: Tiran Dagan, Brandon Hancock, Patrick Chouinard, Elijah
keywords: CV Refinery, resume ATS, consulting disruption, Prepper tool, Sherpa Cow, travel planning, Picasa, Dropbox, face recognition, Supabase, markdown to HTML, ShipKit prompts, LinkedIn scraping
summary: Tiran presents four projects: CV Refinery (resume-to-job analysis with iterative Q&A to build a personal fact repository and a LinkedIn scraper extension); a Prepper emergency planning tool being redesigned after ShipKit prompt sessions; a consulting report-to-interactive-app converter that disrupts traditional PowerPoint deliverables; and Sherpa Cow, a trip planning app with sequential/parallel itinerary workflows. Patrick suggests CV Refinery as a B2B tool for consulting firms' RFP CV reformatting. Tiran also shares a Picasa-inspired photo gallery app using Dropbox and AI face recognition.
-->

01:41:34 - Tiran Dagan
So I'm throwing in a little intro about myself. I've been in all of these big companies — Cognizant, IBM, Ernst & Young. I had 400 engineers working for me at Cognizant. It will take them a month or two to build a tiny prototype that I can do myself in a matter of minutes today. It's just amazing.

01:42:15 - Tiran Dagan
Here are a couple of projects. One of them is this resume tool that I've built, CV Refinery [tool:CV Refinery]. It goes to address the fact that people find it hard to bubble up above the ATS [tool:ATS] filter. So it analyzes a resume against a job — you upload the job, and then you analyze your specific resume to that specific job, and you get very detailed analysis: why are you a good fit, where are the gaps, what are the things you should do to your resume.

01:42:56 - Tiran Dagan
What I didn't share yesterday was that it also collects facts about you from your resume and from Q&As that the tool starts to ask you. So if I want to apply to this job, it'll say: you have to address some gaps, answer these questions, and then I'll build you a better resume. It creates a new resume, changes the bullets and the wording, and incorporates the information you provided. If you do this 10 or 15 times, you're building a repository that I'm collecting in the background so you can see all of the facts it knows about you.

01:43:35 - Tiran Dagan
I've been building a tool that allows you to scrape directly from LinkedIn [tool:LinkedIn], so if you see a job, you click onto the CV Refinery tool and it brings the job in, click "Send to CV Refinery," it starts a job to ingest the job.

01:43:52 - Tiran Dagan
Another one — I think I shared this yesterday — is this Prepper tool [tool:Prepper tool]. And I have to give kudos to you. ▶ ShipKit is a game changer. It's un-freaking-believable. I spent the entire day today with my partner on this project, and it completely changed our thinking, the ideas that it threw out. We're going to change. Also, we have a beautiful logo, thanks to your prompts, and a completely new UI. It correctly told me that this color scheme is a little too dark and warning and scary — I need to use some different colors.

01:44:45 - Tiran Dagan
This tool — you put in a couple of parameters or things that you're worried about that you want to plan. Where do you live? I'm in London. It's me and my wife and our child. We want to plan for one month of bugging in, and I have a budget of $2,000. It initiates a plan — the AI goes and builds an entire report: here are the supplies you need, here is a map of escape routes with the benefits and challenges of each choice, here are some resources for you to learn, skills you should build to be prepared for this.

01:45:52 - Tiran Dagan
Another one — this is really cool, because I come from consulting. Consulting is about to be the biggest disrupted industry — and I'm not talking about IT consulting, but actual consulting: strategy, ops, et cetera. This is an example of something I did. I obviously used AI to help me build a sample analysis. This was a pitch for why you need to have a chief AI officer. But what we ended up doing is building a tool that converts a markdown report to a clickable interactive application [tool:markdown-to-HTML converter]. So you have that text, and now in five minutes you spin out an entire site that lets executives drill into your analysis.

01:47:00 - Tiran Dagan
<Q>Going back to consulting — are you thinking it's more going to disrupt it on the thinking and planning, more on the output deliverables, the whole process?</Q>

01:47:19 - Tiran Dagan
<A>There are two phases. One is the report generation. Once I've generated the report and crafted the prompts I want, the report is usually something that enhances and supports a report we're actually doing — because the consultancy I have is a loose-knit collection of C-suite folks who bring in their expertise. This brings in the data overlay and market research. And then, now you have a report — what do you do? You spend days a week creating a beautiful PowerPoint. ▶ The report we generate is essentially a markdown-to-HTML converter, but it's taking that and turning it into drill-down graphics. I let the AI choose what to do with it — I just instruct it to create beautiful visuals and drill-downs, focusing on the outcome and not on the format.</A>

01:49:08 - Patrick Chouinard
<Q>About your CV Refinery — have you ever thought about proposing that to consulting firms? Because they spend an insane amount of time reformatting CVs to be submitted as part of RFPs or client requests.</Q>

01:49:27 - Tiran Dagan
<A>Patrick, I'm going to give you a big hug. I love that idea. Coming from consulting, I know exactly what you're talking about. As a partner, you've already picked the team you're going to have, and usually you don't have any control over it — whoever is available is on the bench — but you have to convince the client that this is the right team. It's not even a matter of modifying the CV. It's just presenting it in a way that matches whatever they request. So I see your system being used as consuming the request from the client and just selecting whatever's in the CV of the user and matching and then presenting it in a form that matches the request.</A>

01:50:35 - Tiran Dagan
Another one is more for fun — Sherpa Cow [tool:Sherpa Cow]. The concept: how do you create a trip? I couldn't find any real good trip organizers. What I wanted to do is plan for it — you're going to Japan, you want to plan essentially mini trips. What does my day look like? Your trips have to have some flexibility: here are some things I'm going to do in sequence, but when we have lunch, I want to know what are my five options so I can choose on the spot. I borrowed from the world of IT — it's essentially a workflow, so a workflow can have fixed sequences and flexible options. When you're looking at the itinerary, you can see what is sequential and what is parallel options.

01:53:24 - Brandon Hancock
<Q>What does — here's the hardest part for when we were going through — we just didn't know what's there, if that makes sense. That was our problem.</Q>

01:53:34 - Tiran Dagan
<A>I didn't build that yet. This needs a lot more refinement — more kind of packages and maybe community-based recommendations. The future iteration is creating lists, sharing lists, et cetera. But I'm finding that there are some other concepts that have more immediate monetization opportunities, so I'm focusing on them.</A>

01:54:24 - Tiran Dagan
And the last fun thing — do you guys remember Picasa [tool:Picasa]? It was an amazing product. It was a client app that sat on top of any folder you wanted, indexed your photos. My brother — he's a surgeon — his daughter had her bat mitzvah, and he used ChatGPT to try to build a website. So it dawned on me: we're missing something like a Picasa. He had all of his photos in Dropbox [tool:Dropbox], so I went and did a one-day project — a photo gallery. Essentially, it erects a website for you from a folder you have in Dropbox. It goes through all the photos and the folders and gives you everything. Dropbox API is extremely slow, so it goes through a process of caching in Supabase. And then I'm using AI to do face recognition and automatic identification of faces. ▶ All he has to do is assign a name. People visiting the photo gallery can come in and say, I want to see all the photos that have Ram in them, and boom, you're done.

01:58:15 - Tiran Dagan
What I did — since I already built a lot of features and already had a PRD — I took the PRD into a new prompt, and then I took the questions that ShipKit is asking. One of the questions is: define who are you talking to and what problem are you solving for? So I asked the AI to answer that for my existing documents, and then I got these massive responses to plug in and got some really fascinating results.

01:59:08 - Brandon Hancock
What you did — that metaskill — absolutely crushed it. If you were to extrapolate, what's funny is how earlier we had that generate-critique pattern where the AI agents are doing it. Dude, you were just the critiquer. You were forcing it to think and generate and you were saying, nope, again, again. That is awesome.

---

<!--SEGMENT
topic: Voice Agent Model Selection and CASA 2 Certification
speakers: Maksym Liamin, Ty Wells, Carlos Aguilar, Brandon Hancock, Ryan C
keywords: voice agent, latency, tool calls, GPT-4o mini, Kimi K2, OpenAI real-time API, ElevenLabs, CASA 2, Google OAuth, SOC 2, Vanta, compliance, cybersecurity certification
summary: Discussion covers the trade-off between latency and tool-call capability in voice agent model selection. Ty reports ~45ms latency using GPT-4o mini with ElevenLabs. Maksym has been using Kimi K2 in production and is open to trying GPT-4o mini or the new OpenAI real-time model. Separately, Maksym asks about CASA Tier 2 certification required by Google for OAuth apps with restricted scopes; Brandon describes the SOC 2 process via Vanta and the cost structure (~$7k platform + ~$7k audit).
-->

01:27:50 - Brandon Hancock
Maksym, any suggestions for voice? I've only really gone deep in ElevenLabs [tool:ElevenLabs].

01:28:06 - Maksym Liamin
<Q>That's the last one I've used. You're referring to a model that can do tool calls, right? That was the main reason? And that has around 40 milliseconds of latency, not more?</Q>

01:28:25 - Maksym Liamin
<A>When you pick smarter LLMs, then suddenly they are too latent. When you pick ones that are very fast, then they cannot do tool calls properly. So it's always a trade-off.</A>

01:28:32 - Ty Wells
▶ GPT-4o mini [tool:GPT-4o mini] seems to work well for me as the balance on ElevenLabs for tool calls and low latency. I think it's around 45 milliseconds.

01:28:53 - Maksym Liamin
I haven't tried GPT models in a long time — last time was in June, but they were very slow for the use case. So I went on to try more open-source LLMs that are hosted and quantized properly, and went with Kimi K2 [tool:Kimi K2], which seemed to work very well. Still until this time we use it in production. But definitely if it's actually 45 milliseconds of latency, I will give GPT-4o mini a try.

01:29:33 - Carlos Aguilar
There is a new model for OpenAI. It's GPT real-time [tool:OpenAI real-time API]. It's recommended for voice. I was just reading about voice agents two days ago and they recommend it if your use case is voice.

01:30:05 - Maksym Liamin
I may have to try that too. Thank you.

01:30:08 - Brandon Hancock
▶ If you guys do get to try that, please let me know and share with the group so everyone collectively gets smarter.

01:30:23 - Maksym Liamin
Another quick question — I know that you work a lot with the guys from Google. We are currently looking to get a CASA 2 [tool:CASA Tier 2] certification, a cybersecurity certification from Google. Do you know anybody who could help with it or have you heard anything about it?

01:31:01 - Maksym Liamin
<A>It's basically when you use OAuth to give access to Gmails, calendars, drives, and everything, and you have this consent screen where you select scopes. If you have restricted permissions, they ask you for this certification so that you can use it in production. Right now we're limited to 100 beta testers, and we're already close to getting that number, so we need to find a way to get this certification fast enough.</A>

01:31:29 - Brandon Hancock
The main certification platforms we've looked at recently: Accommodation, Vanta [tool:Vanta], and a few others. Those are for SOC 2 [tool:SOC 2], which sounds very similar to what you're describing. ▶ They basically give you the checklist, run all the tests, and help connect you with the auditor who gives you the stamp and seal of approval. You're roughly going to pay $7k for Vanta, or maybe a little bit more depending on complexity, and another $7k for the audit itself.

01:33:00 - Brandon Hancock
SOC 2 is different — you can get SOC 1, which is compliant today at the time of the test, and then there's SOC 2, which is continuous monitoring. That takes about six months — they basically look at your logs for six months to verify you've been doing things properly for a long time.

01:34:04 - Ryan C
I was speaking to a guy who runs a big software company over here, and he said there's a lot of it that you can sort of indemnify away. ▶ Some of it, they come to you and say, this is an issue, and you can literally just go, yes, we are aware, and we're happy to take the risk that that is a potential flaw. So you don't have to be completely watertight and tick every single box. That could save you some time and pain.

---

<!--SEGMENT
topic: Local Models, Tooling, and LinkedIn Outreach Strategy
speakers: Brandon Hancock, Patrick Chouinard, Tiran Dagan, Elijah, Bastian Venegas Arevalo
keywords: local models, Qwen3 Coder, OpenCoder, Ollama, Gemini CLI, Claude Code, Appify, LinkedIn, Linked Helper, B2B outreach, ShipKit onboarding, Windsurf, Cursor, anti-gravity IDE
summary: Patrick recommends Qwen3 Coder and OpenCoder (an open-source Claude Code equivalent) for local model experimentation. Brandon describes his parallel Gemini CLI research pipeline for finding medical chiefs across US cities, and plans to enhance it with Appify for LinkedIn scraping. Elijah introduces Linked Helper as a LinkedIn automation tool used by a podcast host in the community. Tiran shares a LinkedIn long-game B2B outreach strategy. The session closes with discussion of ShipKit onboarding improvements, the Windsurf/Cursor/Claude Code IDE workflow, and upcoming video walkthroughs.
-->

01:24:41 - Brandon Hancock
Patrick, you were dropping some model suggestions. I do think I want to try out a local model. Which one were you saying?

01:24:48 - Patrick Chouinard
Qwen3 Coder [tool:Qwen3 Coder]. But if they have maybe a 14B, because 32B will be a little bit big.

01:26:00 - Patrick Chouinard
For the one you were selecting, just check for maybe a smaller quantization. ▶ As long as it fits within your 24 gigs of RAM, you should be OK. It's not going to be fast, but it's going to work.

01:26:39 - Patrick Chouinard
And actually install it through using OpenCoder [tool:OpenCoder]. It's basically Claude Code open source.

01:27:02 - Patrick Chouinard
▶ OpenCoder is basically Claude Code, but for open models.

01:27:22 - Patrick Chouinard
Or guess what? Just ask Claude to tell you how to install OpenCoder. It actually will give you a step-by-step.

01:35:17 - Brandon Hancock
PH, just to go back to your question real fast on the CLI scraper I made. Basically, he was asking: can you explain the CLI scraper you made when I was a guest on the Google Channel? So what we were doing is we were basically trying to find all medical chiefs throughout America. The workflow I was doing: I created a seed file with the 500 biggest cities in America. Per city, I would kick off — I would do `gemini -p` and pass in a prompt, and the prompt was basically a long file of: phase one, you find this; phase two, find this; phase three, verify this; phase four, analyze. I would just pass that into Gemini CLI [tool:Gemini CLI], which is at the end of the day an agent that has Google search. So I could end up kicking off 10, 15, or 20 deep searches per city at a time.

01:36:34 - Brandon Hancock
Now, even though it is Google search, it does not do things such as LinkedIn, which was the biggest obstacle. ▶ So I'm going to be trying to do it again using Appify [tool:Appify]. It costs money to actually pull people's LinkedIn stuff, but I think it's going to be worth it — roughly $30 to do an insane amount of scrapes. Then once I have the initial seed data with names, emails, profiles, I'm going to kick off Gemini CLI again per person to go off and do a deeper search.

01:37:31 - Brandon Hancock
And Patrick did say — actually using Claude Code was performing better, giving better results than Gemini CLI. So I haven't got to try it myself, but Patrick is the thought leader on this, and I'm excited to try it out with Claude Code to see if it does even better.

01:37:51 - Patrick Chouinard
▶ Claude Code works better. Costs more, but works better.

01:38:06 - Elijah
One thing there too, Brandon — I don't know if you've used Linked Helper [tool:Linked Helper]. Dawn Davis, who's a part of the ShipKit community, who's been working on the podcast — he is the one that showed me that. He's got the number one life science podcast right now, and it does all the LinkedIn search help for him. He's got a whole automation that brings people into his podcast, does the research on them, tees it up for his podcast, and he just shows up.

01:38:48 - Brandon Hancock
I am literally sending this to my partner right now, because that is a very cool tool. My partner is the one doing those 20 LinkedIn outreaches.

01:39:13 - Brandon Hancock
▶ Guys, seriously, if you are going into enterprise land where there are bigger deals, the best way is a long play, but it's almost a guarantee: over the course of a year, connect consistently with your desired target customers. Throughout the year, connect with as many as you can, talk about the subject on LinkedIn, so whenever they do connect with you, they see you as a thought leader. Don't ask instantly for, can I sell you this? If you're doing 20 invites a day over the course of a year, the amount of connections you're going to have with every single customer you want is unreal.

01:41:00 - Tiran Dagan
▶ Don't sleep on LinkedIn connections if you're going to go into B2E — B2B, but more specifically business enterprise or business to government. These connections are super invaluable. It's just one playbook to have in your head to try, but it's working out really well for us right now.

02:00:28 - Brandon Hancock
So the two biggest things that are happening to ShipKit when I get back: redo the onboarding — y'all provided so much awesome feedback on tips and tricks, so the onboarding just needs to be improved. And then help people pick the project — just like how Patrick mentioned, actually pick which template to use, and also just kind of help guide people of like, everyone's coming in with a different journey. Hey, I just want to learn first. Some people: I just want to build first.

02:05:26 - Brandon Hancock
▶ The way I'm using it: I use Windsurf [tool:Windsurf] (anti-gravity) as my editor for 10% of the time when I'm doing something visual. The other 90%, it's all Claude Code. That is my current work paradigm. In the new worker SaaS walkthrough, you'll see me doing that — hopping between Windsurf specifically to use Gemini 2.5 Pro [tool:Gemini 2.5 Pro] with all the new cool tools they have, but 90% of the time I'm just doing Claude Code.

02:07:10 - Brandon Hancock
And then the way, because I'm using Windsurf — Windsurf does their own memory management, so as you're working with the project, it's learning lessons about your coding style. So it's a little bit more agentic learning — it's like a curve. To start off, you're not going to get the best results, but as time goes on, Windsurf gets smarter.

02:09:29 - Bastian Venegas Arevalo
Since you're using Claude Code in the IDE, I sent in WhatsApp a screenshot of an extension called Claude Code Usage or something like that. It should do exactly what you wanted to know — how much session time you have left and all of that.

02:10:01 - Brandon Hancock
The issue I was wanting to look at is I wanted to know how much tokens I was using, because normally right now I'm typing in `usage` all the time to see where I'm at. But what I would love to do instead is just use what you can use with status line. ▶ Everyone in Claude Code has status line — you can potentially set it up to where it will actually change stuff down here in the terminal.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript and were not present in the SPEAKER_ALIASES context block (which was not supplied):

- scottrippey (passed through unchanged)
- Glenn Marcus (passed through unchanged)
- Ryan C (passed through unchanged)
- Maksym Liamin (passed through unchanged)
- George Kurian (passed through unchanged)
- Ty Wells (passed through unchanged)
- Tiran Dagan (passed through unchanged)
- Elijah (passed through unchanged)
- Carlos Aguilar (passed through unchanged)
- Bastian Venegas Arevalo (passed through unchanged)
- Juvenal A. Silva Jr. (passed through unchanged; single timestamp only)