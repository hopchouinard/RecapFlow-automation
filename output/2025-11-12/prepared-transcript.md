=== SESSION ===
date: Not explicitly stated (references "last week," "Sunday" deadline, "November" for podcast)
duration_estimate: ~105 minutes (00:13:10 – ~01:55:00)
main_themes: AI developer community check-in; computer vision for automotive damage detection; Gemini CLI parallel agent workflows; worker SaaS pipeline with Trigger.dev and Whisper; contract/IP negotiation for freelancers; data structures interview prep; security scanning SaaS; N8N workflow debugging; image generation for home customization; WhatsApp API integration for GCP-hosted farm data

---

<!--SEGMENT
topic: Pre-Meeting Small Talk
speakers: Patrick Chouinard, Marc Juretus, Ty Wells, alexrojas
keywords: weather, Quebec, Mexico City, Celsius, Fahrenheit, daylight savings, altitude, humidity, profile picture, Nano Banana
summary: Participants exchange casual greetings and discuss weather differences across their locations — Quebec snowstorms, Georgia cold snaps, and Mexico City's mild high-altitude climate. The conversation touches on Celsius vs. Fahrenheit confusion in Canada and daylight savings time. No technical content, but establishes the community atmosphere.
-->

00:13:10 - Patrick Chouinard
Hey, Marc. How are you doing?

00:13:16 - Marc Juretus
What's up, buddy? How you doing, man?

00:13:22 - Patrick Chouinard
Did you change your emoticon, your icon, or your profile pic?

00:13:26 - Marc Juretus
I saw the long black beard.

00:13:31 - Marc Juretus
Actually, that's a picture that was from my barber that I actually had Nano Banana [tool:Nano Banana] retweaked.

00:13:44 - Ty Wells
Use the tool or lose the tool, right?

00:13:49 - Ty Wells
What's up, fellas? Yeah, I just snuck in nine holes, and I'm trying to make it back in time, running late. It's like 27, 28 degrees where I'm at.

00:14:10 - Marc Juretus
Golf ain't no option up this way.

00:14:14 - Ty Wells
Yeah, we're still 63 right now, so not a bad day.

00:14:21 - Patrick Chouinard
I drove back from work in about half a foot of snow today.

00:14:27 - Marc Juretus
You can keep that. It's funny how you get older — you start becoming an angry person, like, man, I got to shovel this crap.

00:15:00 - Patrick Chouinard
Blow its entire snow budget for the year in one day.

00:15:05 - alexrojas
You need to move to Mexico, bro. No snow. All year. Perfect weather. Well, we just have rainy season and not rainy season. The good thing about Mexico City is that we are very high in altitude — it's like 2.2 kilometers, almost 1.5 miles from sea level. So the temperature is very dry.

00:16:00 - alexrojas
Yeah, humidity kills you, man.

00:16:34 - Patrick Chouinard
I'm from Quebec. Yeah, I did the translation because we're mostly Americans. I learned both systems equally when I was younger.

00:17:00 - Patrick Chouinard
There are things that are imperial still, others that are metric. Pool temperature is going to be Fahrenheit — nobody's going to know if the pool is okay unless it's in Fahrenheit, even though the weather outside is set in Celsius.

00:17:26 - Marc Juretus
I know people say it's 100 degrees, but it's like a cool 100 without the humidity. Man, it's 100, brother. It's 100.

00:18:00 - Patrick Chouinard
People tell me, "Oh, but it's a dry heat." Yeah, my stove is also a dry heat.

00:18:18 - Patrick Chouinard
Where I am, we've seen basically every type of temperature there is. As much as we have the minus 30 in the winter, we also have the plus 40, or 100 degrees at 80% humidity in the summer.

00:18:54 - Marc Juretus
It cracks me up when they have daylight savings time. If the kids are at the bus stop, it's going to be pitch dark if you don't do that. That's one of the reasons why I'm a fan.

---

<!--SEGMENT
topic: Alex's Automotive Damage Detection Project
speakers: alexrojas, Brandon Hancock, Juan Torres, Rod Morrison, Mitch McCauley
keywords: YOLO v8, RoboFlow, computer vision, Next.js, Supabase, Gemini API, Trigger.dev, last-mile automotive, car damage detection, phone-based inference, scope reduction
summary: Alex describes a client project to digitize last-mile automotive delivery inspections using AI-powered damage detection. He explains how he scaled back from a hardware Raspberry Pi arc to a phone-based YOLO v8 model trained in RoboFlow. Brandon suggests an alternative cloud-based approach using the Gemini API video/image models via Trigger.dev, arguing it would be faster and smarter than running local models on phones.
-->

00:19:42 - Mitch McCauley
How did your call go, Alex?

00:19:47 - alexrojas
Good. Interesting. So as an update — I am closing a client. My proposal got a bit too excited and made a hybrid between software and hardware. Mitch and Brandon said it was like I went too far, and I either needed to charge double or cut the scope. So that's exactly what happened today. They were actually very grateful that I was honest about it. I said I screwed it up, talked to the experts, and lowered the scope. So now we're doing software. The nice tweak is that we're going to use a model and run it on the phones.

00:21:00 - alexrojas
A little background: these guys do the last mile for car companies. They receive cars from the trailer and need to make sure there are no aesthetic damages before delivering to the final customer. They are zero-digitalized, so I'm trying to help them start innovating. My first proposal was to make an arc with Raspberry Pis [tool:Raspberry Pi] with computer vision taking photos — which was phase two. Today I told them, hey, we need to go one step back and do the software first. The photos, we're going to run them in the phone with a trained model in RoboFlow [tool:RoboFlow], and running while the photos are being taken. After the session is over — 10 cars go down — we push everything to Supabase [tool:Supabase]. It's a Next.js [tool:Next.js] app.

00:21:52 - Patrick Chouinard
It always comes back to Next.js and Supabase.

00:22:16 - Brandon Hancock
Alex, you are first on the list. What is going on, Mr. Hardware Software AI?

00:29:46 - Juan Torres
<Q>Which vision model are you thinking of using?</Q>

00:29:50 - alexrojas
<A>I'm thinking of YOLO version 8 [tool:YOLO v8]. They have like thousands of photos of aesthetic damages. I proposed five photos per car, but we might go around eight. When the session is done, the operator takes a photo of the paper, it creates a queue of all the cars, the operator takes photos, and at the end of the car line they finish the session and everything gets sent to Supabase.</A>

00:30:56 - Brandon Hancock
So two things. One quick recap for the group: Alex found a lead through a friend, built out wireframes, helped the customer discover their true problems, and landed on a hardware solution. He pitched a price, and it turned out the work was worth almost double what he quoted. We were trying to figure out how to restructure scope so both sides win.

▶ Always bounce ideas off other developers before committing to a price — there are always blind spots, and you can easily overshoot or undershoot.

00:32:50 - Brandon Hancock
Alex, I really think we could simplify your stuff. Doing models on their phones — why not take advantage of the cloud? I don't think they have any privacy concerns; it's a car VIN number. What I would look at is using the Gemini API [tool:Gemini API], their video models. You would upload either to Google Drive [tool:Google Drive] or Supabase, provide that URL, and pass in a prompt: "What damage do you see on the car?" That could be thing one. Or, thing two, use a combination of Trigger.dev [tool:Trigger.dev] to pull out frames every quarter second — four screenshots per second — then pass all of those in parallel to any image model and say, "Look at these and come back with a damage report."

▶ Prefer cloud models over local models for this use case: they are faster, smarter, and privacy is not a concern for car VIN data.

00:34:27 - Brandon Hancock
So each picture would get a timestamp, each timestamp would result in a summary, and then you would combine all of those summaries as one.

00:35:44 - Brandon Hancock
The simplest one, Alex, is just take pictures every quarter second. Skip the video — let's just do pictures, break it up, get a report per picture, and then summarize all the reports.

00:36:13 - alexrojas
I did only say pictures, guys. I don't want to — maybe we could upgrade to videos, but let's have something running first.

00:36:15 - alexrojas
<Q>I'm going to go through the AI docs for the development to have the idea really written down and the wireframes, and then use that to make a proposal. What template should I use? And what are the things I need to pay attention to in the proposal or term agreement?</Q>

00:37:00 - Brandon Hancock
<A>Alex, shoot me an email after this and I'll share what I did for my last contract.</A>

00:37:17 - Jake Maymar
<A>I've been using Claude [tool:Claude] for contracts. The important thing is you say "I'm the contractor," because it changes the lens of how it views the contract. Make it as short as possible but retain the legal protections. The main thing is background IP. If the contract says they own everything — a Sony or Apple situation — you have to sign it or walk away. But this is an opportunity: make sure the contract is in a condition that you can actually sell it. My background IP would transfer when they sell the company, but tied specifically to that product and not iterations of it. And instead of saying no to IP transfer, say "totally cool, but at a cost."</A>

▶ Don't sign contracts under pressure — sleep on it. The difference between making real money and just enough often comes down to IP clauses.

00:40:37 - Rod Morrison
I used ChatGPT [tool:ChatGPT] to come up with Mexico market rates when building a proposal. It gave some parameters. If you're coming in low, always do a gut check just to get a sense of the going rate.

00:41:09 - alexrojas
Thank you very much, guys. They did appreciate the transparency and honesty of saying, "This is where I screwed up, but this is what you can expect."

00:41:29 - Brandon Hancock
▶ Trigger.dev is going to work amazingly with this project — it is literally the template you'll use to build all of that pipeline.

---

<!--SEGMENT
topic: Worker SaaS Pipeline Demo
speakers: Brandon Hancock, Patrick Chouinard, Jake Maymar
keywords: Trigger.dev, Whisper, Supabase, Next.js, Blob Store, real-time streaming, video transcription, AI summary, dynamic prompts, SaaS template
summary: Brandon demos a worker SaaS product in progress that uploads video to Supabase's Blob Store, hands it off to Trigger.dev for audio extraction and Whisper transcription, generates AI summaries with dynamic prompt branching, and streams all progress updates in real time. He explains the architecture and notes the template will be available to members by Sunday.
-->

00:24:39 - Brandon Hancock
Update two: I was going to give you guys a quick demo on the worker SaaS stuff. It is coming along. We're on the setup scripts and cruising for everything to go live. I go live by Sunday for you guys. Here's a high-level overview of what it does.

Behind the scenes, we're uploading to Supabase [tool:Supabase]. What it's doing is going to the Blob Store [tool:Supabase Blob Store]. Once it's in the Blob Store, we instantly throw it over to Trigger.dev [tool:Trigger.dev], which has an entire pipeline with a bunch of tasks for managing it. It's downloading the file, extracting the audio clips. Once it extracts the audio clips, it's using Whisper [tool:Whisper] to transcribe all the video chunks. So it's all happening over here in Trigger.dev — all running in the cloud.

00:25:53 - Brandon Hancock
Per usual, you get the transcript. Then the next step is the AI summary. You click it — this showcases how to kick off another Trigger.dev workflow. What's cool about this one is it shows some branching: we take in the transcript, figure out what type of input it was — did it look like meeting notes, a YouTube video, or just general? Based on that, we pass in dynamic prompts and generate summaries. That was just to showcase other ways you can use workflows.

00:26:23 - Brandon Hancock
Finally, you can talk to your stuff. A lot of people wanted to know — Patrick, or Morgan, or Jake — how to do real-time streams. This is all real-time. The progress updates were real-time. The streaming was real-time.

▶ The worker SaaS template will be available by Sunday and covers real-time streaming, Whisper transcription, dynamic prompt branching, and Trigger.dev pipeline orchestration.

00:26:56 - Brandon Hancock
We're working on wrapping up the test templates and setup scripts, trying to get it cranked out as fast as possible for you guys.

---

<!--SEGMENT
topic: Gemini CLI Parallel Agent Research Pipeline
speakers: Patrick Chouinard, Brandon Hancock
keywords: Gemini CLI, Gemini 2.5 Flash, Bash scripting, parallel agents, fan-out pattern, Astro, TSV prompts, deep research, Google Search, GitHub repo, Copilot CLI, sub-agents
summary: Patrick demonstrates a Bash-only pipeline that runs hundreds of parallel Gemini CLI agents to perform deep research across configurable topics, synthesizes results into a daily AI news site built with Astro, and self-improves its own prompts each run. Brandon explains the fan-out pattern this enables and recommends Gemini 2.5 Flash over Pro for speed and quota efficiency. Patrick also previews upcoming work on GitHub Copilot CLI and its sub-agent capabilities.
-->

00:52:54 - Brandon Hancock
Patrick, you're up next. But before you go, I want to give you credit. I hopped on a call with Patrick a little while ago and talked deeply about Gemini CLI [tool:Gemini CLI], specifically on the searching side of things. I'll have a video soon — a deep dive — and later in November there'll be a more podcast-style version with Google. I just want to give credit where credit is due.

00:53:00 - Patrick Chouinard
Actually, you're probably going to like what I have to show you this week, because you challenged me last week. I've been coding with a couple of agents last weekend and I came up with this little thing.

The site is not the big thing here. What you see is just an aggregation of a bunch of searches into a kind of daily news about AI subjects that I care about. The 21 research domains you have here for today — you have a view-search research source that shows an IDE-like interface with all of the files that were synthesized to create the daily report, and then you can dive into each one, download them, share them.

What I wanted to create is an entire pipeline made of Bash only, calling Gemini CLI [tool:Gemini CLI] repeatedly with a list of prompts hosted in a TSV file. You just update the prompts in the TSV file and a configuration for how many you want to run simultaneously. After all of that, you have a bunch of analysis prompts that do cross-validation between different subjects, find insights, and — I've created within the pipeline itself — the last step is: look at all of the prompts you've used and the results, and propose improvements for tomorrow.

▶ The pipeline self-improves its own prompts each run, so it gets better at research automatically without manual intervention.

00:55:23 - Patrick Chouinard
All of that is strictly in Bash and within an Astro [tool:Astro] frontend for the website. I'll share the URL because it is a public site — just static content, no risk. And here is the GitHub repo [link:public GitHub repo shared in chat], which is also public.

00:55:55 - Brandon Hancock
The cool thing I want to extract: at the end of the day, you can literally run Gemini CLI an infinite number of times. When Patrick's running a Bash script, he's passing in the flag to pass in a prompt and saying, "Go research this topic and save the output here." But at the exact same time, he can spin up 10, 20, 100 parallel requests using Gemini CLI. Each CLI is its own agent. So Patrick literally has a thousand agents all using Google Search [tool:Google Search] to find information on a topic.

▶ Using the fan-out pattern with Gemini CLI, you can spin up thousands of parallel research agents for roughly $20, covering an entire country's worth of business data.

00:58:03 - Patrick Chouinard
One thing that's really important: force it to use Gemini 2.5 Flash [tool:Gemini 2.5 Flash], because if you use 2.5 Pro, it's going to take forever to answer and you're going to burn through your allocation very quickly. Flash is more than enough to do simple search.

▶ Use Gemini 2.5 Flash instead of 2.5 Pro for parallel search pipelines — it is faster and far more quota-efficient.

00:58:34 - Patrick Chouinard
At work, I'm starting to work on a course about Copilot CLI [tool:GitHub Copilot CLI]. With the latest release from GitHub, they're gaining very quickly. I think they're the only one I've seen that has sub-agents except for Claude Code [tool:Claude Code]. The backend of Copilot CLI is very close to what Claude is doing. And with Agent HQ coming up — where you will be able to manage multiple agents, including Claude and Cursor and all of those from within your GitHub account — that's going to be very nice.

00:59:44 - Patrick Chouinard
I'm thinking about whether I can have something AI-generated from my ideas — basically me talking through a bot — as the only way I'd be able to publish enough content to be interesting.

---

<!--SEGMENT
topic: Code Review Automation with CLI Tools
speakers: Hemal Shah, Brandon Hancock, Patrick Chouinard, Morgan Cook
keywords: CodeRabbit, Cursor CLI, Gemini CLI, GitHub Actions, Claude Code Hooks, Ollama, Warp terminal, WSL, PowerShell, local models, code review pipeline
summary: Hemal shares his exploration of replacing the expensive CodeRabbit code review tool with a custom pipeline using Cursor CLI and GitHub Actions. Brandon suggests adding Gemini CLI as a free parallel check. Patrick recommends a lightweight Bash/Ollama setup called Terminal Intelligence for shell command assistance. Morgan discusses using Warp terminal on Windows with WSL for AI-assisted PowerShell commands.
-->

00:48:04 - Hemal Shah
I did try CodeRabbit [tool:CodeRabbit] as per our last suggestion. It's great, but it's expensive if your team is huge. So I've been playing with using Cursor CLI [tool:Cursor CLI] and GitHub Actions [tool:GitHub Actions] just to use that and provide some tokens or API keys to do the code review in that fashion. That's something I'm exploring.

00:48:43 - Brandon Hancock
Whatever prompt you make, prompts are agnostic to these different tools. Gemini CLI [tool:Gemini CLI] is also free — you have 10,000 requests per day, I can't remember the exact number. If you're going to build the long prompt to review stuff, might as well copy the prompt and just try it with Gemini CLI too. It's a free second check.

▶ Gemini CLI offers a free tier (~10,000 requests/day) that can serve as a zero-cost second code review pass alongside any paid tool.

00:49:26 - Hemal Shah
<Q>Have you tried Cursor CLI? Does it stack up with other CLIs?</Q>

00:49:32 - Brandon Hancock
<A>I've not gone with the Cursor CLI. I did way back try to do background agents with ShipKit [tool:ShipKit] and genuinely could not get it to work, so it put a bad taste in my mouth. Perfect locally on my computer, but in the cloud it fought me hard.</A>

00:50:02 - Hemal Shah
Really appreciate all your best practices videos around vibe coding and Cursor. Last week I was doing certain things and it came up with very long, huge code changes and it didn't feel right. I just told it, "Is there any better way of doing it?" And lo and behold, it came up with a very simplified answer.

▶ When AI generates overly complex code, explicitly ask "Is there a better way of doing this?" — it will often produce a dramatically simpler solution.

00:51:17 - Brandon Hancock
Please keep me posted on what you find on the CLI. I've dove into Claude Code Hooks [tool:Claude Code Hooks] — that was the furthest I've gone — but I haven't done the full pipeline stuff.

00:53:00 - Morgan Cook
I sent a message in the chat that Warp [tool:Warp] also supports a form of agent. It's not exactly what you guys are used to thinking of as agents — it's more of an agent with a profile, kind of like a system prompt and a task, where you can fire it off in multiple threads just like you can with Gemini CLI.

00:53:00 - Morgan Cook
I use Warp a lot because the new Windows command line with PowerShell prompts are so complicated and I don't have them in my memory. So I often just ask AI, "Make a PowerShell prompt out of this so I can execute it correctly." I'm also running it in WSL [tool:WSL] with Linux, going back and forth between the two frames.

01:04:15 - Patrick Chouinard
Morgan, I've posted a link in the chat. You were talking about using Warp to get information about PowerShell. If you look at the repo I sent — Terminal Intelligence [tool:Terminal Intelligence] — it's a very simple couple of scripts and aliases where you can query a local model and have it initiated with a system prompt that makes it a specialized agent in PowerShell. You can have it in any terminal and just ask, "How do I do this in PowerShell?" A couple of scripts and it does everything with a local model, which won't cost you anything. It works with Ollama [tool:Ollama] and custom Ollama models — a model plus a system prompt.

▶ Terminal Intelligence (shared in chat) provides a free, local Ollama-powered shell assistant that can be specialized for PowerShell, Bash, or any CLI language with zero API cost.

---

<!--SEGMENT
topic: Juan's Vendor Extraction AI Agent
speakers: Juan Torres, Brandon Hancock
keywords: AWS, LLM inference, SOC 2 compliance, A10 GPU, named entity recognition, 8B parameter model, vendor extraction, on-premise AI, qualitative reasoning, construction vision model
summary: Juan describes a locally hosted AWS AI solution using an 8-billion-parameter LLM on an A10 GPU to extract vendor names from documents with ~95% accuracy, outperforming traditional NER models. He discusses SOC 2 compliance advantages of not training on customer data, GPU capacity planning, and a potential new lead in construction-sector computer vision. Brandon highlights Juan's emerging niche in on-prem/cloud AI infrastructure and evaluation.
-->

00:41:58 - Juan Torres
Hey folks. Nice seeing you again. I've been out for a while. Glad to see my AAA support group here.

00:42:14 - Juan Torres
Nothing much has happened. The main piece of work — my AI solution, which is all hosted in AWS [tool:AWS] — I was actually talking to a company that has venture capital in it that is solving some similar issues, but they don't create their own inference engines. They just rely on the API of whatever models they use. Which makes it easy because you don't have to worry about the embedding model you're picking and having to worry about GPU capacity.

00:43:40 - Juan Torres
Right now I just finished — and it's not really complex — just one AI agent that automates the process of extracting vendor names, and it does it really accurately. I was struggling to increase accuracy by first trying to engage machine learning models like named entity recognition, but just having an 8-billion-parameter model [tool:8B LLM] extracting information — it takes more time, but the right prompting basically gets, I would say, almost 95% or even more of the extraction.

▶ A well-prompted 8B parameter LLM outperforms traditional NER models for vendor name extraction, achieving ~95% accuracy with no model training required.

00:44:08 - Juan Torres
This is all SOC 2 compliant because there's no model being trained. There's no training of the models — Palantir [tool:Palantir] is not going to be handling it. It's all locally hosted and measured within a GPU environment that is as economical as possible. It's an A10 GPU [tool:A10 GPU], just about the right fitness of GPU capacity for this job. When there's more handling, there's going to be a need for more GPU capacity.

00:45:03 - Juan Torres
Alex, I was asking you about the model because I may have a lead that also needs a vision model, but in the construction sector — needs to be able to identify irregularities. I'm still seeing if that's going to be something I'll be doing.

00:45:27 - Brandon Hancock
You are slowly finding yourself in a niche of infra, cloud and local/on-prem. That's definitely one pillar of what I've seen you crushing on recently. And then QA, evals, and efficiency — you are starting to really become an absolute beast on that.

▶ Specializing publicly in on-prem AI infrastructure plus QA/evals creates near-zero competition and commands top-dollar rates.

00:46:44 - Brandon Hancock
When solving problems — same as solving code problems on a whiteboard — always start with: what is the dumbest and easiest solution? I literally say this out loud because I get so excited with AI. I spent two days building an elaborate pipeline and a co-founder said, "Wait, why don't you just do this?" I fell for my own trap.

▶ Always ask "what is the dumbest, simplest solution?" before building any AI pipeline — pretend AI doesn't exist first, then layer it in at the simplest possible level.

---

<!--SEGMENT
topic: Jake's RAG Forum App and Tool Choices
speakers: Jake Maymar, Brandon Hancock
keywords: Trigger.dev, RAG, WebSockets, Supabase real-time, Resend, Mailgun, Tiptap, WYSIWYG markdown, forum, background IP, contract negotiation, Claude
summary: Jake asks whether to migrate his existing RAG forum app (using WebSockets and Supabase real-time subscriptions) to Trigger.dev, and Brandon advises against it for his current simple use case. They also compare Resend vs. Mailgun for transactional email, and Brandon recommends Tiptap as the most capable WYSIWYG markdown editor for collaborative forum post editing.
-->

01:05:40 - Jake Maymar
So yeah, Trigger.dev [tool:Trigger.dev] — very, very excited about that. Thank you, Brandon. That's awesome. <Q>So if I already have an implementation of a RAG setup, and I'm already using WebSockets, real-time subscriptions, Supabase — is it fairly easy to migrate? Or should I consider just starting over?</Q>

01:06:10 - Brandon Hancock
<A>Trigger.dev is great for streaming events when the events are coming from Trigger.dev — like uploading a video file, parsing it into images, that whole process. They have FFmpeg tools, you can save to a local file store in Trigger.dev. But if we're just using it for general streaming, it is possible but it's overkill. In your situation, you already are doing the sockets and you're listening to your database. That might be good enough. Instead of streaming events back to the front end, you're just writing to the database and reading from the database. I might not change what you have.</A>

▶ Trigger.dev is best suited for long-running background pipelines; for simple real-time database-driven streaming, existing WebSocket + Supabase subscriptions are sufficient and simpler.

01:08:42 - Jake Maymar
Yeah, I think I'll definitely use it in a phase two when things get more complicated. Simple solutions, right? I tend to overcomplicate these things. I'll even ask different models and it gives me a complex solution, and I'm like, there's got to be a simpler way.

01:09:05 - Jake Maymar
<Q>Using Resend [tool:Resend], and then was looking into Mailgun [tool:Mailgun] — is there a big major difference between the two?</Q>

01:09:21 - Brandon Hancock
<A>The only reason I was using Mailgun is to literally just send mail — event happens, send email. My needs were so straightforward I just left it at that. Half the time I'm using it for internal emails: a customer submits a complaint, Mailgun lets me know. The other half is to just email me that someone reported something needing attention.</A>

▶ For simple transactional email (event-triggered notifications), Mailgun and Resend are functionally equivalent — choose based on your existing familiarity.

01:10:10 - Jake Maymar
<Q>And editing posts — you shared before a specific plugin to make WYSIWYG markdown. Tip Tap?</Q>

01:10:26 - Brandon Hancock
<A>That's it — Tiptap [tool:Tiptap]. It's the most capable out of all of them. You can do the collaboration part, you can highlight, you can do AI going through analyzing stuff and injecting — literally nothing we could not do. It was really powerful.</A>

▶ Tiptap is the recommended WYSIWYG markdown editor for collaborative forum applications — it supports real-time collaboration, AI injection, and extensive customization.

---

<!--SEGMENT
topic: Ana's WhatsApp + GCP Farm Data Chatbot
speakers: Ana P, Brandon Hancock, Morgan Cook, Ty Wells, Juan Torres
keywords: WhatsApp API, Meta for Developers, GCP, BigQuery, ADK, Cloud Run, vector store, end-to-end encryption, authentication, coffee farm, Panama, stakeholder reporting
summary: Ana describes an early-stage project to build an AI chatbot for a Panama coffee farm that queries GCP/BigQuery data and delivers answers via WhatsApp to stakeholders. The group discusses WhatsApp's end-to-end encryption, metadata exposure, authentication via phone number whitelisting, and GCP-side SSL/HTTPS security controls. Brandon raises the question of document volume to determine whether a vector store is needed.
-->

01:11:51 - Ana P
So mine is actually pretty fast — I'm in the early stage of developing a couple of things and I want early guidance. One is potentially for a coffee farm here in Panama. I have an acquaintance who manages two farms and wants to start putting everything in GCP [tool:GCP]. The idea with AI would be for it to query all of the information that is in GCP. That's pretty easy to do with the BigQuery [tool:BigQuery] tool set that's in ADK [tool:ADK], but I'm thinking of other things to add.

The first thing I started playing around with is the WhatsApp API [tool:WhatsApp API]. In the last call, I was trying to configure a Cloud Run [tool:Cloud Run] app — you would have a web app with a chatbot. But then I realized that if I could use the WhatsApp API so that the LLM connects to WhatsApp, it would be so much easier. But I'm very concerned in terms of security of information and I'm not entirely sure how safe WhatsApp is for this.

01:13:22 - Brandon Hancock
<A>The simplest version is just creating a whitelist of like these six phone numbers that can communicate. That would probably be the level-one immediate level of security. But I don't know how easy it is to spoof a phone number — that's the only part I don't know, which would be the concern. It might be harder to spoof emails.</A>

01:13:51 - Morgan Cook
<A>For WhatsApp, I thought it's encoded point to point. As to whether or not you're getting to the right endpoint — that would be the only condition. But the app itself is end-to-end encrypted. There's no data visible from the server side. It's client to client.</A>

01:16:31 - Ty Wells
<A>WhatsApp is secure in terms of its data transmission, but its header information is available — like who you're talking to and when — but not the data being transmitted. That is exposed, but the content is secure.</A>

01:16:59 - Juan Torres
<A>You can also restrain the rules at the code level for how your server is going to communicate to WhatsApp. If you want SSL or HTTPS connectivity to the WhatsApp API, you can set them up and that should be safely compliant.</A>

▶ WhatsApp provides end-to-end encryption for message content but exposes metadata (sender, timestamp); mitigate business data risk by whitelisting phone numbers and enforcing HTTPS/SSL on the GCP server side.

01:17:24 - Brandon Hancock
<Q>How many documents are we trying to work with? Is this like one document a quarter or 10 documents every week?</Q>

01:17:39 - Ana P
<A>I do not have that information yet. We're just starting.</A>

01:17:45 - Brandon Hancock
The biggest reason I bring it up is for building out a vector store in Google Cloud — if you have a ton of information, a vector store really helps with that.

▶ Determine document volume early: high-frequency or large document sets warrant a GCP vector store, while low-volume stakeholder reporting may not need one.

---

<!--SEGMENT
topic: Mario's Home Customization Image Generation and AI Avatar Platform
speakers: Mario Polanco, Brandon Hancock
keywords: Nano Banana, Gemini image generation, image editing, HeyGen, RAG, AI avatar, Zoom integration, knowledge base, course platform, mini homes, color customization, Python, iterative image grading
summary: Mario presents two projects: (1) an image generation tool for a mini-home developer to let clients visualize wall/floor/finish options using Gemini's image editing API, and (2) an AI avatar platform using HeyGen that clones course creators, hosts RAG-powered knowledge bases, and can join live Zoom calls. Brandon walks through a three-level image generation architecture (single prompt → multi-image grading → feedback loop) and advises leveraging HeyGen's built-in knowledge base API rather than building a custom vector store.
-->

01:25:09 - Mario Polanco
I got recently proposed by a developer and an architect doing some mini home projects. They'd like to have something built so they could show examples to clients — different finishes for different parts of these little mini homes. The concept, when I asked them, was kind of like when you go to a car's website: you can pick and choose colors and finishes and interior. They want to have some limits — not fully open customization.

01:26:08 - Brandon Hancock
Especially now with Nano Banana [tool:Nano Banana] coming out — you can do anything. Mitch was on the call the other week basically taking pictures of soap in his hand and turning it into the most elegant, natural, organic background. The tools are there. What's missing is the image from the user and the proper prompts.

01:27:00 - Mario Polanco
They have some templates of the homes and figure it's going to be kind of like a color-by-number — walls are one thing, countertops are another thing — and where they can pick and choose what aspects of the home can be swapped for one of three or four colors or finishes.

01:27:33 - Brandon Hancock
That's even easier than if it were fully open. Here's what we would do — using Python [tool:Python], this is the model for generating with Nano Banana [tool:Nano Banana], the Gemini image generator. So image editing: the user uploads a picture, then we give it some editing prompts. I'll drop the Gemini image editing docs page in chat [link:Gemini image editing documentation]. That one page would tell you how to do 80% of the contract.

▶ Say yes to the contract — it is feasible with Gemini's image editing API, and the three-level architecture (single prompt → multi-image grading → feedback loop) provides a clear build path.

01:28:52 - Brandon Hancock
Level one: take an image and a prompt and just see if that works. Level two: image plus prompt, make multiple iterations, then have AI pick the best one — because it's non-deterministic, you'd make four images and have a grader pick the one that best matches the user's request. Level three: a loop — if you don't mind making the user wait a little longer, you pick the best image and then AI decides: "This one's perfect" or "We need to do it again."

▶ For a quick demo, level one (single prompt + single image) is sufficient to prove feasibility to the client before building the full grading loop.

01:30:12 - Mario Polanco
Just to follow up to what we talked about a few weeks ago — we're building an AI platform where users can make calls with an interactive embedded avatar. It'll have full features unlockable on a monthly subscription, plus built-in RAG [tool:RAG] which I'm using from the RAG bot I built two months ago. These AI avatars — we're using HeyGen [tool:HeyGen] — can also be in live Zoom calls. We're already working with some YouTubers and course creators, cloning them, feeding it scripts, and it's performing well on YouTube. We want to take it to the next level with a course model and embedding that avatar.

01:32:49 - Mario Polanco
HeyGen just launched a new version where you can create a knowledge base for that avatar and upload to it. They even have a live Zoom version that's querying that knowledge base in real time. People can ask it questions. So we're helping coaches save time — they could be hosting five webinars at one time and not have to be there.

01:33:21 - Brandon Hancock
If they already have their knowledge store built in, that's what I would stick with. If not, you're going to have to make a custom tool where when stuff comes in, you turn the conversation into multiple queries, go to your vector store, come back — and I don't know how long that's going to hold up the conversation while your avatar is just like, "I'm thinking."

▶ Use HeyGen's native knowledge base API rather than building a custom RAG pipeline — it avoids latency issues that would cause the avatar to pause mid-conversation.

01:33:57 - Brandon Hancock
The cool part is you have the course. So every time something gets uploaded to the course, trigger a background job to make sure it always gets uploaded properly to HeyGen.

---

<!--SEGMENT
topic: Security Scanning SaaS and N8N Workflow Debugging
speakers: Ty Wells, Brandon Hancock, Juan Torres, Mitch McCauley
keywords: OWASP Top 10, Lambda, security scanning, N8N, Sora, Dropbox, webhook, parallel execution limits, CodeRabbit, Canva, ChatGPT, face blurring, Python, Trigger.dev migration
summary: Ty demos his security scanning SaaS that checks repos against OWASP Top 10 vulnerabilities using AWS Lambda, and solicits beta testers. Mitch shares N8N debugging issues caused by exceeding parallel execution limits when running Sora video generation workflows, and Brandon suggests migrating to Trigger.dev. Mitch also demos a ChatGPT+Canva pitch deck workflow and a Python face-blurring script built with Cursor.
-->

01:24:35 - Ty Wells
I just got a chance to look back at my security scanning. If you guys want to test it out, you can sign up and scan your repos for potential security issues — I think you get to scan like two repos for free. I'm going to drop the link in here [link:security scanning SaaS shared in chat].

01:25:25 - Brandon Hancock
It did the full blown PDF. It did a ton. It was very cool.

01:36:19 - Juan Torres
<Q>What kind of security vulnerabilities do you test with your app?</Q>

01:36:25 - Ty Wells
<A>There's like 400 different — OWASP Top 10 [tool:OWASP Top 10], some custom ones. I'm running it on Lambda [tool:AWS Lambda]. It never really touches the site itself. Right now I'm just checking functionality: can you log in, authenticate with Google and email/password, does your scan work, do you get your vulnerabilities, do you get a prompt of how to correct those vulnerabilities.</A>

01:37:09 - Brandon Hancock
Cool thing, Ty — like taking the CodeRabbit [tool:CodeRabbit] approach of making it a GitHub app that automatically does two or three checks. They do a very good job of commenting on everything, even after you cancel the trial — they just drop little messages, even funny poems about rabbits. Once you're in the person's codebase, you're constantly reminding all the developers. Especially if you do it on a public project, that's infinite marketing forever.

01:39:49 - Mitch
Yeah, so I've been running into some issues with N8N [tool:N8N]. When I'm running the workflows, it just doesn't even save the data sometimes. When it adds to the queue, I think it's a queuing process and I'm running N8N way too hard. The workflow — for some reason when I make HTTP requests to Sora [tool:Sora], my prompt is really long, so it's impossible for it to work on the first pass, and I get an error when it gets to the Dropbox [tool:Dropbox] section because there's no file to upload. When I try to check debug and editor and unpin the data, it literally just can't show the data.

01:42:02 - Brandon Hancock
<Q>If you right-click the HTTP request, does it have something like an "on exception" or "on catch" node?</Q>

01:42:33 - Brandon Hancock
<A>None of them are failing — that's the issue. They're just passing through undefined each time. I wonder if you just exceeded the limit of what they can put in a box and they're just saying undefined. I would just do this one — test it one time instead of testing it in parallel 100 times, just to make sure: is my logic sound for one pass?</A>

01:43:30 - Brandon Hancock
Something's wrong with doing a bunch in parallel. Who's calling this webhook? That would be the next immediate question in parallel land.

01:44:47 - Brandon Hancock
I'm very curious if you're exceeding the 20 parallel tasks — what happens to the extra ones in the queue? Does it hold on to them and pass them on to work next?

▶ N8N has a parallel execution limit (~20 concurrent tasks); exceeding it causes undefined data states that are difficult to debug — consider migrating high-volume parallel pipelines to Trigger.dev.

01:45:34 - Mitch
I think it's just code getting upset at me because I'm cheating on it with N8N. The hard part about N8N without having it — it's weird that you can't just look at 100 logs. You have to click through each one and you can't see the previous state or the post state. That's the downfall of no-code tools: you give up a lot for simplicity.

01:48:31 - Brandon Hancock
You were probably among the 0.1% of all N8N developers who ever hit that, because most people don't get that far.

01:48:56 - Mitch
Hooking up Canva [tool:Canva] with ChatGPT [tool:ChatGPT] — that is some fire. When a client is asking you to do a pitch deck and you just say, "Hey, connect to Canva, here's a voice note of everything" — man, that is that good.

01:50:20 - Brandon Hancock
So basically someone was hiring editors to blur faces for videos. I was like, you can just code this up. And basically we have an input video — using Cursor [tool:Cursor] — I just said "create a plan and then do it." It used a face detection model and it worked. I think what would be cool is if instead of just the face, it blurred the whole head, because when they turn sideways the face detection loses it.

▶ Cursor can generate a working face-blurring video script from a plain-language prompt in ~15 minutes — no prior coding knowledge required for local Python scripts.

---

<!--SEGMENT
topic: Data Structures Interview Prep and Community GitHub Repo
speakers: Brandon Hancock, Alex Wilson, Patrick Chouinard, Ty Wells
keywords: AlgoExpert, NeetCode, cracking the coding interview, data structures, algorithms, systems design, Redis, rate limiting, GitHub community repo, ShipKit, Discord
summary: Brandon recommends AlgoExpert, NeetCode, and Cracking the Coding Interview to Alex Wilson who is preparing for a technical pre-screen exam. He explains the importance of data structures, algorithms, and systems design for senior engineering roles. The group also discusses creating a shared GitHub community repository for ShipKit members to contribute code, with Brandon committing to set it up by Thursday.
-->

01:18:24 - Brandon Hancock
Alex, you're up next.

01:18:27 - Alex Wilson
I did want to thank you for AlgoExpert [tool:AlgoExpert] that I'm currently working on. I don't think I'm going to make it this time around. They do have a lot of postings, so it'll help me get through the gate for the future.

01:18:48 - Brandon Hancock
So basically Alex was invited to a pre-exam. For the longest time — I went to college for electrical engineering, master's for software engineering — I never did data structures and algorithms. I had to learn this all post-college on my own. For whatever reason, the most important thing tech companies always care about is data structures and algorithms [tool:AlgoExpert] — can you solve problems logically with code?

The tool I was recommending is AlgoExpert [tool:AlgoExpert]. I've bought this three times. They have the data structures and algorithms part — videos that explain how everything works, solutions, everything else. And now it's so easy because you can just copy it over to AI and say "teach me this."

▶ AlgoExpert is the recommended starting point for data structures and algorithms interview prep — pair it with AI tools to accelerate understanding of each concept.

01:20:22 - Brandon Hancock
They also have Systems Expert. If you want to get more senior engineering level, they're going to ask you this. Basically: if our database is getting used and abused, what can we do to reduce load? Oh, we can use a cache — we use Redis [tool:Redis]. How do you handle rate limiting? What bucket strategy are we going to use? There's so many things you have to learn, and 90% of what I've learned came from this course.

There's a few others I recommend: NeetCode [tool:NeetCode] is another one, and then Cracking the Coding Interview [tool:Cracking the Coding Interview]. If you spend three months doing nothing but that, your brain's going to hurt so bad — but you're going to be solving coding problems in your sleep.

▶ For senior-level roles, supplement algorithm prep with Systems Expert content covering caching (Redis), rate limiting, and distributed systems design.

01:22:30 - Brandon Hancock
Patrick, were you able to think about a place where we could share content?

01:23:05 - Patrick Chouinard
I'm just worried a channel on Discord might be a bit limiting because there's a file size limit. I was thinking about maybe a GitHub repo where all the subscribers could actually be participants — kind of a non-open-source open-source project.

01:23:25 - Brandon Hancock
Yeah, just making a community one. Is that a community one or a ShipKit [tool:ShipKit] one more so?

01:23:39 - Ty Wells
The one that you released the code base in — couldn't you just put it in there? So if it's in there, everybody who has ShipKit has it.

01:23:46 - Brandon Hancock
The thing I was thinking about is: do I manage every pull request to allow things to go in, or do we just let it be a free-for-all? My plate is already so swamped, so it might be a free-for-all. It'll probably be on Thursday, Patrick, because I have to send out invites to everyone.

▶ A shared ShipKit community GitHub repo will be created by Thursday — members will be able to contribute code directly, likely as an open contribution model without mandatory PR review.

---

=== UNRESOLVED SPEAKERS ===

The following speaker raw names were not found in the SPEAKER_ALIASES context block (which was not provided to this session):

- **alexrojas** — participated extensively; canonical form unknown
- **Mitch McCauley** / **Mitch** — appears under both names; canonical form unknown
- **Ana P** — first name only with initial; canonical form unknown
- **Bastian Venegas Arevalo** — may be "Bastian" referenced by Brandon; canonical form unconfirmed
- **Jake Maymar** — canonical form unconfirmed
- **Juan Torres** — canonical form unconfirmed
- **Rod Morrison** — canonical form unconfirmed
- **Mario Polanco** — canonical form unconfirmed
- **Morgan Cook** — canonical form unconfirmed
- **Hemal Shah** — canonical form unconfirmed
- **Alex Wilson** — canonical form unconfirmed (distinct from "alexrojas")
- **Ty Wells** — canonical form unconfirmed

*(No SPEAKER_ALIASES map was supplied in the context block, so all speaker names are passed through as found in the source transcript.)*