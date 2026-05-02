=== SESSION ===
date: Not explicitly stated (inferred as a weekly recurring call)
duration_estimate: ~115 minutes
main_themes: GPT-5 evaluation, local/open-weight LLM models, AI coding tools and context management, MCP server development, community building and meetups, member project updates, prompt/context engineering strategies

---

<!--SEGMENT
topic: Session Open and Housekeeping
speakers: Paul Miller, Tom Welsh, Andrew Nanton, Mitch, Bastian Venegas
keywords: GPT-5, OpenAI, Google Cloud Functions, Google Cloud Run, Docker, Brandon, Caribbean, session format, voice check
summary: The session opens with informal check-ins. Tom Welsh describes an exhausting house-renovation "week off." Mitch shares frustration with Google Cloud Functions and Cloud Run naming changes. Paul Miller explains that Brandon is in transit and he is hosting again. The group establishes the session format: questions in chat, then a round-robin update from each participant.
-->

00:05:23 - Andrew Nanton
How's life, Tom?

00:05:26 - Tom Welsh
Somebody spoke.

00:05:27 - Tom Welsh
I need a voice check.

00:05:32 - Tom Welsh
We've just bought a house.

00:05:33 - Tom Welsh
I've had a week off and I'm up at five in the morning, DIYing and finishing at 7pm at night.

00:05:39 - Andrew Nanton
I was going to say, if you just bought a house, you didn't have a week off.

00:05:43 - Andrew Nanton
That sounds like the opposite of a week off.

00:05:46 - Tom Welsh
Correct. That's exactly what it's been.

00:05:51 - Tom Welsh
Bad food, no sleep. Graft.

00:06:00 - Tom Welsh
Mitch, have you got a little hacker?

00:06:05 - Mitch
Man, I wish I was good enough to do that. I was struggling with Google Cloud Functions [tool:Google Cloud Functions], and I'm like, gosh, am I just stupid?

00:06:18 - Mitch
<Q>You know, I kind of realized, I'm like, you know, maybe instead of spending three hours trying to fix something, I could just read the docs.</Q>

00:06:25 - Andrew Nanton
<A>Well, if it's anything like Azure Cloud documentation, it's hopelessly out of date. It points you to pages that don't exist anymore.</A>

00:06:50 - Mitch
No, that's the thing that's also confusing. I'm like, okay, well, it used to be Google Cloud Functions. Now it's Google Cloud Run [tool:Google Cloud Run], but on Google Cloud Run there's the option to run your own Docker image [tool:Docker] instead of having predetermined files — Python or Node or whatever. I was looking at Brandon's code, and I'm like, okay, his code makes sense, but mine, I'm just confused.

00:07:19 - Mitch
Yeah, they change the names all the time, the services. Yeah, it's a pain.

00:07:27 - Mitch
I just want to figure it out so I can do 2 million invocations for free a month.

00:07:37 - Mitch
It's always the saying: I did it because I thought it would be easy.

00:07:42 - Tom Welsh
It's not that easy.

00:07:46 - Mitch
Well, once you do it, that's the best part — you're like, oh, okay, I mostly understand it.

00:07:55 - Tom Welsh
Yeah, doing it once, doing it right — that's it, you've got it then. That's my library from now on.

00:08:07 - Tom Welsh
Yeah, not all of us can be like Bastian.

00:08:09 - Mitch
Just get it right on the first try and be gifted — wake up every day and the code just codes itself.

00:08:18 - Bastian Venegas
AI does that, doesn't it?

00:08:31 - Paul Miller
I am the Brandon again for the final time this week. Brandon is in transit from the Caribbean back to the United States, so he's asked me to jump on.

00:10:00 - Paul Miller
So, a week of a few model updates, especially the OpenAI [tool:OpenAI] one, GPT-5 [tool:GPT-5]. How are we all finding it?

---

<!--SEGMENT
topic: GPT-5 Initial Reactions
speakers: Paul Miller, Mitch, Andrew Nanton, Patrick Chouinard, Jake Maymar, Al Cole, Bastian Venegas
keywords: GPT-5, OpenAI, Lovable, coding quality, model consistency, thinking models, context issues, personality prompting, LinkedIn slop, agent mode
summary: The group shares first impressions of GPT-5. Reactions range from "heartless and cold" to "blank canvas for personality shaping." Paul Miller notes it rewards clear prompting. Jake Maymar raises concerns about model inconsistency and the difficulty of catching errors deep in a commit history. Al Cole reports a speed improvement via Lovable. Bastian Venegas warns that thinking models can derail long coding sessions.
-->

00:10:17 - Mitch
Heartless, cold, bitter.

00:10:23 - Andrew Nanton
It writes like LinkedIn slop.

00:10:30 - Patrick Chouinard
To be quite honest, as a base model or a base personality, I kind of like it for one reason. I've shown you before how I worked on a kind of personality framework to exchange with AI. I found that the base personality is easily influenceable by those kinds of prompts. So I see it not as heartless, but more as a blank canvas that you can shape into whichever personality you want.

00:11:00 - Patrick Chouinard
And I want to start testing, combining my custom personality with the underlying configurable personality that they offer and see how those react together. But honestly, it's just a matter of adjusting how you interact — not so much that the model is bad, it's just you interact with it differently than previous models.

00:11:25 - Paul Miller
▶ Where people have prompted it effectively and given it clear instructions as to what they want out of it, they get a brilliant response. But if you apply the methodology of what you'd done with some of the other models previously, you can get some fails from it.

00:12:00 - Paul Miller
<Q>Who, it's great in the coding stack. How are people finding it with their code?</Q>

00:12:11 - Jake Maymar
<A>Yeah, the code is really interesting. You kind of have to trick it into using the best model, because it almost always defaults to the worst model. And like, everything is probabilistic. So when you're coding something, you're like, oh, I can get this done in X amount of time. And then you hit a surprise, right? And now all your code is messed up, and you have to roll back.</A>

00:13:00 - Jake Maymar
A lot of times what happens is you're moving so fast, you don't realize there's an error until many, many commits in. And so that's, I think, the most painful thing of this sort of new workflow.

00:13:23 - Al Cole
I leveraged it through Lovable [tool:Lovable]. And I absolutely could notice a speed improvement. Lovable did pretty well. I did some spec development with it. I didn't do any coding other than what happened through Lovable, but I definitely noticed a much faster rendering of the page than I was seeing before.

00:13:49 - Jake Maymar
If you trick the model into using the best part of the model, it gets really good — like crazy good code. But the thing is, I want consistency. I mean, it's nice to have beautiful code, but I really want consistency because if you're a thousand commits in and then you realize an issue — because these projects are getting just massive.

00:32:06 - Bastian Venegas
I was going to comment on what Jake was telling about his issues with GPT-5 for coding. Yeah, I think it's very good if it has a very clear plan and it's not the longest conversation, because it does have context issues. But I try to avoid using thinking models or tapping into thinking mode because they tend to deviate. It's just a matter of time. You can have a very detailed plan and task and all your folders with markdown instructions and rules, and it's enough that it just creates one or two chains of thought that are out of place to send everything to hell — because it will have no awareness of what it thought in the prior message, since that's not fit into the context by default.

00:33:29 - Bastian Venegas
It's part of the design because you will run out of tokens right away. So it's like, oh yeah, I did this — and that's kind of related to this thought that was wrong. And that's enough. When it gets to the point where it called a tool with that wrong thought, everything goes to hell.

---

<!--SEGMENT
topic: Open-Weight Models and Local Inference
speakers: Paul Miller, Al Cole, Andrew Nanton
keywords: OpenAI open-weights, 120-billion parameter model, llama.cpp, Ollama, mixture-of-experts, LM Studio, Ollama cloud, GPU, CPU offloading, fine-tuning, NVIDIA startup program
summary: The group discusses OpenAI's newly released open-weight models, particularly the 120-billion parameter model. Andrew Nanton explains how llama.cpp can offload layers from GPU to CPU for the mixture-of-experts architecture, making local inference more feasible. Paul Miller mentions the Ollama hybrid local/cloud hosting update and the NVIDIA startup program offering generous cloud credits.
-->

00:16:07 - Al Cole
Well, I thought the open model release was also intriguing over the last week. It opens up some more possibilities. I haven't yet gotten it down to LM Studio [tool:LM Studio], but I was going to play with them a little bit just to see the art of the possible on my laptop.

00:16:31 - Paul Miller
▶ The open models look really good for agent stuff. There was also the Ollama [tool:Ollama] update where you could do this kind of hybrid, local, private model hosting, but have your GPU running with the Ollama cloud. So it still keeps it private, which Ollama is really good at doing.

00:17:00 - Paul Miller
The challenge is that new OpenWeights model from OpenAI — the 120-billion-parameter one versus the 120-gigabyte one — seems to be the better model, but there's not going to be many people who have the hardware to run that locally. But this is what Ollama is doing with their latest update.

00:19:34 - Paul Miller
<Q>Andrew, do you want to talk through that 120-billion model? So you're looking at local llama?</Q>

00:19:37 - Andrew Nanton
<A>So using the command-line llama.cpp [tool:llama.cpp], which is what Ollama and a lot of other tools are built on top of, you can unload some of the layers in the 120-billion-parameter GPT OSS off of the GPU and into the CPU. It's a mixture-of-experts model, so that works a little bit better than some other models where all parameters are active at the same time. You can get acceptable performance by dumping a lot of it off the GPU and onto the CPU, but still having the routing to the correct expert in the mixture-of-experts running on the GPU.</A>

00:20:33 - Andrew Nanton
▶ Worth taking a look at, because that model — I feel like the local models are starting to get good enough to be interesting. Maybe the difference between the 20-billion and 120-billion parameter model is pretty close to that cutoff where there are actually a fair number of things that are actually useful that might now be feasible to run locally.

00:21:06 - Paul Miller
▶ I think it'd be really interesting to see how people maybe fine-tune that 20-billion model with the open weights — tweaking that and doing fine-tuning as well. A lot of these newer models with synthetic content training seem to be getting more and more accurate with smaller sizes.

00:29:41 - Paul Miller
▶ Another good one I found in the last week, for everyone else that wants server-based credits: NVIDIA have a startup program [link:NVIDIA startup program], which gives you access to a number of different models with a number of different vendors, including Google and AWS, as well as their own cloud resources. A massive credit upfront to get involved. All you have to do is fill out a pretty standard form. You don't have to be part of a startup investment scheme.

---

<!--SEGMENT
topic: Al Cole Project Updates and Lenny's Newsletter
speakers: Al Cole, Paul Miller, Bastian Venegas
keywords: Lenny's newsletter, Gamma, NotebookLM, Lovable, Warp, Whisperflow, Linear, Replit, HubSpot MCP, Anthropic, digital marketing agency, property management, prompt engineering
summary: Al Cole shares two key resources: Lenny's newsletter ($200/year bundle including pro tool subscriptions and a Silicon Valley product manager Slack) and Gamma for AI-generated presentations. He also describes two paid consulting engagements — a property management company and a digital marketing agency — where he is mapping workflows and building prompts. He notes that Anthropic's new HubSpot MCP integration opens significant automation possibilities for his marketing agency client.
-->

00:22:32 - Al Cole
I've got a little sharing to do. Do you mind if I share a browser?

00:22:47 - Al Cole
I don't know if you're aware of Lenny's newsletter [tool:Lenny's Newsletter]. Lenny's a pretty famous Silicon Valley product manager type. He had a new offer — if you subscribe, and it's $200 a year, I understand that may not fit everybody, but what he threw in there is everything you see in this picture. You literally get pro subscriptions for a year.

00:23:40 - Al Cole
▶ So I did it, and it's crazy. A lot of value for $200. He's pricing it out at $10 per tool, and you know what, it may very well be that. I have kind of viewed my evolving role being less that pure software engineer type, and more the product manager type, really trying to steer the models to what we want to build.

00:24:03 - Al Cole
And if you do join, you get access to a Slack group with some of the top Silicon Valley companies in it with their product managers. Tons of insights on how they're thinking about building their products and where the state of the art is.

00:24:30 - Al Cole
Second thing I just wanted to share — one of the things was Gamma [tool:Gamma] that I heard great things about. It's a presentation builder. I wanted to do a meetup on building an LLM literally from the ground up. How do you do it? And then how do you run it in production? So I did a little work in NotebookLM [tool:NotebookLM]. I had a couple of books I had purchased, PDF versions. I pulled this whole thing in, asked it to generate an outline of a presentation. I literally dropped in that script and Gamma, inside of 10 minutes, gave me this.

00:25:38 - Al Cole
▶ If I can get my hands wrapped around this and feel confident enough, I might do this in a local meetup just to walk through the history of LLM building and how you deploy them in production.

00:25:54 - Al Cole
The only other thing I'll highlight in terms of paid gigs: I'm working on one for a property management company and another for a digital marketing agency. The digital marketing agency is a little more interesting because I'm actually trying to untangle their workflow — multiple people, multiple roles. I did a bunch of prompting exercises with them last week.

00:27:14 - Al Cole
The owner sees gen AI as an existential threat, period. So he was very motivated. They're all using ChatGPT [tool:ChatGPT], but there's really no automation, and they're using it in a very fragmented way. How I'm working with them is literally deciphering their respective job descriptions, and the inputs and outputs in their processes, and then working through getting prompts together.

00:27:47 - Al Cole
An interesting thing I found out: they're a partner of HubSpot [tool:HubSpot]. And Anthropic just linked up with HubSpot with an MCP server [tool:HubSpot MCP]. So that literally opens up a ton of possibilities for them because now they've got access to tons of telemetry on the clients they serve.

00:28:27 - Al Cole
▶ What I can do is, if the team's interested, I'll get you some examples of prompts that I've kind of built, just to see how I've structured them. I'll throw it up in my Google Drive and give you a link to it later in this meeting.

00:33:51 - Bastian Venegas
And Lenny's newsletter — I highly recommend it. There's a lot of good stuff. Mitch was hyping Warp [tool:Warp] — the AI coding agent in your terminal — it's great. This is one year free, like a $16 plan or something. Whisperflow [tool:Whisperflow] — it's great, especially if you type a lot and your hands hurt. Linear [tool:Linear] for tracking GitHub issues. Gamma is the one that Al showed for presentations. Replit [tool:Replit] is getting much, much better with their agent for building websites — it's React basically, and Supabase, and built-in authentication. You also get hosting, so it's like Vercel plus V0 in the same environment.

---

<!--SEGMENT
topic: AI Coding Workflow — Determinism, Temperature, and Testing
speakers: Jake Maymar, Bastian Venegas, Al Cole, Mitch
keywords: temperature zero, thinking models, deterministic output, seed, hallucinations, Claude Code, context window, test generation, probabilistic models, reinforcement learning, AWS Bedrock guardrails
summary: A technical discussion on how to get more reliable output from LLMs in coding contexts. Bastian Venegas explains why thinking models are incompatible with temperature-zero strategies and why non-thinking models with temperature zero produce more consistent code. Jake Maymar shares experiments with temperature settings in OpenAI models. Al Cole describes how Claude Code can spiral in troubleshooting mode. The group agrees on a layered, incremental build-and-validate approach over one-shot generation.
-->

00:36:00 - Jake Maymar
What Bastian just said was brilliant — I hadn't thought about that. But you're right: when the thinking model is active, and you've constructed an entire architecture with a whole bunch of rules, the model thinking explains why I'm running into issues, because it's getting creative.

00:36:31 - Jake Maymar
<Q>I'm curious, how close are we to almost deterministic models? I know everything's built on probabilistic models and transformers, but I wonder — because we were talking about hallucinations, and I feel like that's been really mitigated at this point. I remember AWS put out that deterministic flow — a white paper on Bedrock [tool:AWS Bedrock]. They talked about guardrails. Did anyone check into that?</Q>

00:39:20 - Al Cole
<A>My experience with Claude Code [tool:Claude Code] — where I have really had to be attentive — is when it gets into troubleshooting mode. I have seen it go off, just generating tons and tons of tokens, trying to test through some streaming scenario. And I have to intervene because I know it's fallen down the rabbit hole. So it still feels a ways away from deterministic, at least on the testing side.</A>

00:40:30 - Mitch
And it makes those tests not necessarily well, because it relies on a specific function, not the overall goal main function. So it doesn't really make a test that's really a test. It's like, does the function work as it's supposed to?

00:41:00 - Jake Maymar
No, it's a really good point, because you have to keep reminding yourself that it's not viewing it the way you would view normal Python code or TypeScript or whatever. It's sort of finding an answer based on a series of judgments, which is completely different from logic. It's as if you're solving physics simulations by what it looks like rather than the underlying rules.

00:42:00 - Al Cole
▶ I always take a layered approach. I am not a one-shot guy. I'm a: let's talk about this layer, let's really flush this out, let's build it, let me validate it, all right, next layer. And I've had success doing it that way.

00:43:35 - Jake Maymar
I've been using temperature to basically get closer to deterministic, but OpenAI — even though it looks like you can set temperature, you can't. I did a couple of tests where I set the temperature to zero and I was not even getting those results. It seemed like it just stayed at 0.7.

00:44:00 - Bastian Venegas
<A>Yeah, that's inherent to thinking models — you're not supposed to mess with the temperature. It's not recommended, different from non-thinking models. I spent several months coding with temperature zero, and it's much better if you know what you're trying to precisely do. You don't need planning, just executing — temperature zero is much better if you're not using a thinking model, because if you are, then it kind of doesn't make sense as a strategy.</A>

00:44:46 - Jake Maymar
So you can actually get pretty decent stuff with temperature-zero models. Versus one, it's much different.

00:45:00 - Bastian Venegas
▶ The likelihood and how soon it would deviate from your plan — if you set it to non-zero temperature, it will randomly choose the non-obvious path and you have to be okay with it.

00:45:34 - Bastian Venegas
Theoretically, you need to have the seed — like when you generate images, there's a seed that starts the diffusion process along with your prompt, and LLMs do the same. They have a seed and you can save the seed, but if temperature is anything other than zero, you will start seeing variation right away. And if it's zero, I don't think it can be exactly the same, but if it were to be, it has to be with temperature zero and the same seed.

---

<!--SEGMENT
topic: Patrick ClaraForge Project and Prompt Meta-Engineering
speakers: Patrick Chouinard, Paul Miller, Al Cole, Bastian Venegas
keywords: ClaraForge, Claraverse, GitHub Copilot, NotebookLM, Cloudflare Pages, metaprompts, VS Code, agent mode, YouTube, prompt engineering, MCP, vibe coding, GitHub
summary: Patrick Chouinard presents ClaraForge (formerly Claraverse), a framework for AI communication, personality, and prompt engineering, now published on GitHub with NotebookLM-generated podcast and video content. He describes a metaprompt workflow where he writes intent rather than full prompts, letting the agent generate the actual prompt from accumulated context in VS Code. He also shares his professional role coaching GitHub Copilot and MCP adoption internally, and explains how his personal project keeps him ahead of developers he trains.
-->

00:47:00 - Patrick Chouinard
I moved forward with my project I told you about that I called previously Claraverse, that is now changed name to ClaraForge [tool:ClaraForge] because I realized that Claraverse was already taken. So basically it's an entire framework of communication with AI models — how do you address them, how do you give them a personality that will help with the exchange, all the methods I use to communicate with them.

00:47:30 - Patrick Chouinard
I've moved that project along significantly because now not only do I have the podcast version of all the text, but also all the video preview from NotebookLM [tool:NotebookLM] as well, which I finally decided to listen to some of you guys last week and revive my YouTube channel and posted all of the messages on there if you are curious.

00:48:00 - Patrick Chouinard
And I've also updated the project on GitHub [tool:GitHub] that contains all of the text, all of the prompts, all of the personalities, all of the tips and tricks for interaction. And now I'm actually working on moving that project to a website where all of the content will be published. I'm trying to work on automation to push all of the updates from the ClaraForge main repo to a ClaraForge site repo that will then feed into a Cloudflare Pages [tool:Cloudflare Pages] site automatically.

00:48:52 - Patrick Chouinard
▶ The idea is every time I update the first one, everything else updates automatically, including all the videos and all the audio. So this is something you can listen to as a podcast, use as a seed or a personality, or look at in video form. I'm just trying to make it as useful and as multimedia as possible.

00:51:42 - Patrick Chouinard
▶ We were talking about prompt engineering earlier and how you construct your prompt. I'm at a point right now where I'm no longer writing prompts at all. I create protoprompts or metaprompts. Basically, I write the intention of the prompt I want and let the agent generate the prompt for it.

00:52:02 - Patrick Chouinard
The way I do that is I've exposed my entire MyDocuments folder as a VS Code [tool:VS Code] project, so everything in there is context. My prompt or metaprompt building is all done inside the same file. So as I write more metaprompts or more intent to create prompts, it gets more and more context as to how I create prompts.

00:52:42 - Patrick Chouinard
▶ As I save more prompts, it's more context for the next prompt. And as I'm doing that, I realized that originally I was writing one or two paragraphs to create a prompt. Now I'm writing literally half a line, and it knows what I'm trying to do.

00:53:11 - Patrick Chouinard
This is the extreme form of my day job, because my job is to do prompt engineering in-house, to go and coach people on how to use AI tools. I'm now pretty much the guy to run the whole GitHub Copilot [tool:GitHub Copilot] training, as well as starting the enabling of MCP [tool:MCP]. I'm starting to build training around vibe coding internally as well.

00:54:04 - Patrick Chouinard
▶ That's why I'm also here — because I'm here to get as many ideas for use cases as possible, because you guys are showing me what the developers I work with will be facing in three to six months.

00:54:32 - Patrick Chouinard
<Q>How good is Copilot at the moment? Is it being refreshed with GPT-5?</Q>

00:54:33 - Patrick Chouinard
<A>Definitely. The last version has done some major strides. It's not yet to the level of Cursor [tool:Cursor] or Claude Code, but definitely doing a whole lot better. In day-to-day or sentence-to-sentence prediction within either code or text, it's doing even better than Cursor. In Agent Mode, Cursor takes the lead for sure. But in auto-completion — not just IntelliSense, but true auto-completion of a paragraph or a function at a time — it does very, very well.</A>

---

<!--SEGMENT
topic: MCP Server Development and RepoPrompt Context Tool
speakers: Andrew Nanton, Bastian Venegas, Paul Miller, Mitch
keywords: MCP server, FastMCP, Context7, Claude Code, Sonnet, RepoPrompt, codemap, context engineering, Obsidian, deep research, token management, CLI tool
summary: Andrew Nanton describes challenges building an MCP server with FastMCP and explores a CLI-first approach as an alternative. Bastian Venegas recommends starting with a minimal single-tool implementation. Bastian then gives a live demo of RepoPrompt, a Mac app that optimizes context passed to LLMs by generating a codemap of imports, functions, and classes, and enabling smart file selection. The group discusses how context engineering — not just prompt engineering — is the key skill for effective AI-assisted coding.
-->

00:56:02 - Andrew Nanton
I've been banging my head against FastMCP [tool:FastMCP] trying to put together an MCP server. I've found it to be a little convoluted.

00:56:31 - Bastian Venegas
It is painful. It's very useful, but I think it's useful to do it once. I don't think I could remember from the top of my head — if you showed me the code, I wouldn't be able to help you without searching. But I know I will remember how to do it and I have enough code saved to reproduce it for other functions.

00:57:24 - Andrew Nanton
Yeah, I felt like I really needed to at least kick the tires on it. I did see one interesting take: maybe the best way to go is to make a shell command-line tool — a CLI tool — and shell out to that, and that should be your approach for building an MCP, because ultimately it's going to be functionally a command-line tool with arguments. That's an interesting take — maybe more deterministic and predictable than the mushier world of trying to go straight into MCP.

00:58:28 - Bastian Venegas
▶ If I were to try it again, I think I would focus on just getting one tool to work and make it like a calculator — two plus whatever the user says — and get that to work, and you're literally done. Because if you add complexity, you may not reach the moment you're actually looking for, which is learning how to do the thing.

00:59:16 - Andrew Nanton
Context7 [tool:Context7] was helpful. They actually have on their site, if you go to documentation, they have the LLMs.txt and LLMs-full.txt. And so I just put LLMs-full into Claude Code and said, look, help me unscrew this thing. And that was pretty helpful.

00:59:42 - Andrew Nanton
Two hours ago, they enabled a million tokens in Claude for Sonnet [tool:Claude Sonnet]. So I don't know, maybe I need to try it again now.

00:59:50 - Bastian Venegas
▶ You will get better results instantly if you use Context7 just because of the way that the information is stored — it's more granular. LLMs.txt is just a bunch of links, which the agent needs to go and browse, and that's not all of the documentation. Context7 does some kind of similarity search or semantic search that gets just the right amount of context.

01:00:30 - Andrew Nanton
<Q>Bastian, I think it was you last week who mentioned RepoPrompt [tool:RepoPrompt]. If you're willing to say a couple of words about how you use that and how it fits into your workflow, I'd be really curious — because I am definitely feeling this description that context engineering is a much better description than prompt engineering.</Q>

01:01:11 - Bastian Venegas
<A>Okay, so this is RepoPrompt — it's a native Mac application, and it has this file tree. The main place where you get started is here, and here you're supposed to put your prompt. You can connect this to Claude Code and use your subscription from there, and you can use it to chat here as well. This is better than anything else if you want to just chat with your files and you don't need anything else.</A>

01:02:12 - Bastian Venegas
You can see here which files it has loaded in its context — these are being fed fully to the AI. It's not choosing or trying to do a tool call to go and read these files. That's a key difference.

01:02:37 - Bastian Venegas
It has this MCP server, which means anything I show you here, your agent can access as well. It will actually control the screen — it will change the file selection. So your agent can dynamically do this selection that I am now doing manually.

01:04:00 - Bastian Venegas
▶ The really interesting thing it has is this codemap. What I have now is: all the files I have selected, it will read them and try to extract all of the imports, all of the functions, classes, and imports. So it contains the file tree, so it knows where the files are, and instead of passing all of this, it will pass this summary, so the AI can track how each class, each function is connected as a whole.

01:05:33 - Bastian Venegas
▶ I thought I needed to pass like 40k tokens, but this reduced it to maybe 17k, including the codemap. So there were some things that weren't there, but the codemap explained it well enough for the AI to understand it.

01:08:13 - Bastian Venegas
▶ The free version — I think the restriction is that you may not have the MCP server, and the maximum that you can copy and paste is like 32k tokens at a time. And this has also allowed me to use the deep research agents much better, because I can fit the relevant part of my code and make a question that's basically: go and search for the documentation, but apply it to these files. So that can speed up the process a lot.

---

<!--SEGMENT
topic: Member Updates — Consulting, Music, and Creative Projects
speakers: Paul Miller, Al Cole, Aleksandr, Alex Wilson, Hemal Shah, Patrick Chouinard, Mitch, Adam, Nate Ginn, Jake Maymar
keywords: Suno AI, FL Studio, Minecraft, Telegram bots, WhatsApp API, meetup.com, Luma, ComfyUI, Stable Diffusion, HeyGen, Amazon products, Art of War, digital marketing consulting, government consulting, Colorado Springs, New Hampshire
summary: A round-robin of member updates covering diverse projects: Aleksandr combines Suno AI music generation with FL Studio and builds Minecraft landscape marketplaces via Telegram. Alex Wilson discusses networking strategies after a banking career transition. Hemal Shah introduces himself as a new member with a fintech/enterprise architecture background exploring agentic AI. Adam prepares a demo for a wine-bar meetup. Nate Ginn explores open-source avatar animation tools including ComfyUI. Mitch is launching Amazon products including an Art of War notecard set.
-->

00:22:25 - Paul Miller
Al and then Bastian — so Al, what's happening in your part of the world?

01:11:04 - Paul Miller
Abdull? Are you there? No, we'll jump on to Adam.

01:11:37 - Adam
I noticed a lot of people are using voice-to-text. So I decided I'd try to get that working. And since I don't work on my laptop, I usually work on a virtual machine, it took a little while to get that to pass through correctly. And then even when I don't talk, the service just sits there taking up CPU time, even after I've hit the stop button.

01:12:18 - Bastian Venegas
<A>You need FFmpeg [tool:FFmpeg], and the concept you're looking at — it blocks the process by default, and when it detects that noise is above a certain level, it opens the connection and your CPU starts doing the job. It would be off by default and be triggered by sound, or some button, or anything you have in the environment.</A>

01:13:00 - Adam
People were talking about meetup groups — I got invited to talk at a meetup group, it's at a wine bar, so if anybody has ideas of what I could do for a demo, maybe something with an agent that does wine, let me know.

01:14:00 - Paul Miller
▶ Maybe do a deep research type thing — see who else is attending, maybe some background on the companies, and get deep research to build suggested discussion points.

01:14:28 - Paul Miller
▶ One of the most successful ones I've done in recent years on AI is if you can give people some really good free takeaways to start with — just dabble a few freebies for them and then say, come and buy me a wine and talk about how we can apply those things to practical things for your business. Everyone's looking for those quick wins.

01:15:44 - Paul Miller
Alexandre?

01:15:51 - Aleksandr
I'm continuing to work with bots, Telegram bots. And I also tried to work with Suno AI [tool:Suno AI] — it's AI about music. I write a prompt in Suno AI, and then I get some sounds, some music lines, and drop it in FL Studio [tool:FL Studio], which is another music platform. In FL Studio, I tried to share these music lines and do my own music style with some sounds from Suno AI.

01:16:38 - Aleksandr
Also, I tried to connect it with a Telegram bot. And I'm working not only with music — I also tried to make some mods for Minecraft [tool:Minecraft]. And I have a project with my friend: we opened a Telegram channel with Minecraft landscapes — we do some landscapes and sell them to different guys who want to buy something, for example, a safari, or some great mountains, or some cities.

01:17:30 - Paul Miller
<Q>Have you published any of your music to any share sites?</Q>

01:17:37 - Aleksandr
<A>Yes, I have my open YouTube channel and I publish some music there and SoundCloud [tool:SoundCloud] also.</A>

01:18:23 - Alex
<Q>Hey Alex, I have a question for you. Regarding the bots — you say you work a lot with Telegram, right? Is it easier to work with Telegram than with WhatsApp API calls?</Q>

01:18:38 - Aleksandr
<A>I think yes, it's more easier for me. And I can say that Discord and Telegram are the same level, but WhatsApp is the next level for me. It's difficult to use some new functions that I can learn easier in Telegram than in WhatsApp. But I think if you can do some not-hardest bots in Telegram, you can begin working with WhatsApp — one or two months of practice and you'll be great in this work.</A>

01:19:37 - Paul Miller
Alex Wilson, did you want to share?

01:19:42 - Alex Wilson
I did ask the question about the groups. I am checking out Meetup [tool:Meetup]. I was a broad analyst for one of the major banks for the last 23 years and was recently let go because they narrowed down their footprint. So I've had quite a break now — four or five months — and I'm looking to start working again.

01:20:00 - Al Cole
▶ When I went back to working full-time, it actually was because a company was there, saw me present, and then they recruited me. So meetups can serve both roles. You can start it by just finding some speakers and yourself and a place to host. Don't be disappointed at the first couple of meetings — you get a really modest turnout. But what happens is you stick with it, and you pull a community together. You'll fill a room, and they'll keep coming, and that might open opportunities for you.

01:23:25 - Paul Miller
Hemal Shah, are you happy to jump on?

01:23:31 - Hemal Shah
I'm from Atlanta, Georgia. This is my first time attending this session. I discovered this through Google ADK Masterclass [tool:Google ADK] and Brandon mentioned about this community. I have around 22 years of experience in software development, mostly in the fintech industry. I'm currently an enterprise architect. I started my AIML journey one and a half years ago. I did a post-graduation from University of Texas — traditional machine learning, AI, supervised learning, unsupervised learning, everything. And then recently started exploring agentic AIs.

01:24:56 - Hemal Shah
Doing POCs at my company right now. Everything is banned — we don't have Cursor or anything — and we are hoping they are going to open that up very soon, and I'm trying to get ready for it.

01:26:01 - Patrick Chouinard
<Q>You said that you don't have access to AI tools for development right now. Does your company have any kind of cloud provider that's already approved right now, like Azure, or AWS, or Google Cloud?</Q>

01:26:17 - Hemal Shah
<A>We do have some integration with Google Vertex. There is some level of machine learning going on, so yes, Google Cloud Platform [tool:Google Cloud Platform] is our cloud provider.</A>

01:26:35 - Patrick Chouinard
▶ I always found it's easier to get the tool in if the inference provider is already approved by security. Take a look at Firebase and Gemini CLI [tool:Gemini CLI]. And from experience dealing with the cybersecurity department — if you can get a platform they already vetted, it's going to be a lot easier, and then they get bug-bitten by the tools, and then they'll become the ones who want to open new doors to get new tools in.

01:27:47 - Paul Miller
Mitch, what's the latest from you?

01:28:00 - Mitch
I'm launching new products, kind of completely separate from the software side — launching a product on Amazon [tool:Amazon], so we'll see how that goes. And then I'm working on my third product, which is like an Art of War notecard product — that one looks really promising. Instead of reading the book, you can buy a series of notecards. One side is the quote, the other half is like a strategic reflection. Very excited about that one.

01:38:52 - Nate Ginn
I've been messing around with Stable Diffusion [tool:Stable Diffusion] and trying to create a really good AI bot — you know, have you ever gone to one of those websites and there's a person who looks real, even though you know it's an AI person, who's on the screen answering questions? I've created this really beautiful nurse and I'm trying to get her to be like the answer source for my things. I've gotten to the point where I've got the picture and some video, but I'm looking for open-source stuff as opposed to using HeyGen [tool:HeyGen] or one of those other third-party things.

01:40:02 - Jake Maymar
<A>So you want something like Stable Diffusion — do you want something that does images, do you want something that does videos, are you thinking like ComfyUI [tool:ComfyUI]? Because that's the go-to. That is a massive amount of stuff there. And you can do animations. If you want something very easy to use, Ruined with three O's is really, really interesting. You can do a lot of stuff with it. But ComfyUI — you can pretty much do whatever you want with it, but you need a GPU.</A>

01:41:00 - Nate Ginn
I have a 4090. So it usually does a pretty good job. I've been able to do really good images. But then it's like taking it to that next step where you have the image be able to do a video that's also, you know, you could put text in it and it looks like it's reading. And then ideally you would want it to be able to be like any other chatbot where it would source the information on your website to provide answers.

01:43:00 - Jake Maymar
▶ Nate, if you took your images and you wanted to animate those images, you could use Midjourney [tool:Midjourney], you could use Runway [tool:Runway] — basically production-quality things. But you can play with these open-source tools and they're really easy to use and you can make some decent stuff with it, and it's free.

---

<!--SEGMENT
topic: Community Events, Consulting Opportunities, and Wrap-Up
speakers: Paul Miller, Alex, asako, Al Cole, Jake Maymar, Andrew Nanton, Prem, Ammar FunnelBuilder, Bastian Venegas
keywords: government consulting, Mexico Guanajuato, women in AI, AWS event, Kiro IDE, MCP, meetup strategy, Luma, vector database, Supabase, Pinecone, Weaviate, PGVector, LiveKit, RFP automation
summary: Alex shares success teaching AI to Mexican government employees and getting invited to a national auditing congress. Asako describes upcoming San Francisco events including a Women in AI meetup and an AWS event covering MCP and the Kiro IDE. Al Cole shares a strategy of using AI agents to find government RFPs and submitting prototype apps alongside proposals. Ammar asks for vector database recommendations for a LiveKit-based conversational AI; Bastian recommends Supabase PGVector as the current default. Paul Miller wraps the session.
-->

01:42:35 - Paul Miller
Alex, how's it going?

01:42:42 - Alex
Here from my side, I've been mainly focusing on the courses that I'm giving to the government of Guanajuato. It has been a great journey so far. Actually, this Thursday is week number five, and the last one is next week. So it has been very, very cool to start my teaching career.

01:44:10 - Alex
Even out of these sessions, I got invited to a Congress — a National Congress of Municipality Auditing that is actually happening in Guanajuato. They have a two-day conference where they bring a national-wide event, and they want a half-hour little bite of information on how to hack into people's productivity. So it's going to be good exposure, hopefully get a lot of subscribers for my channel.

01:46:18 - Alex
My experience is — and this is from a meeting with one of the organizers — there are three layers of auditing: federal, state, and municipality. And even from the classes I've been giving, people are extremely thirsty for this type of knowledge. I think even just operating an LLM like ChatGPT — last session it was Claude — and all the comments, there were like 120 people in the call, and they were like, oh my God, it just did my work in three minutes.

01:47:42 - Alex
▶ I think there is a lot of potential even on these basic things that you might not even see. There is opportunity in structuring something and commercializing it.

01:48:00 - Alex
The organizer was saying that the talent required versus the talent actually doing all the auditing is very unequal — they understand they require much better people, and that's why they're interested in bringing these tools to try to help people be a bit more productive.

01:49:00 - Paul Miller
<Q>Andrew raised a few good points — the key one is: have they paid you?</Q>

01:48:57 - Alex
<A>Yeah, after next week, everything goes through. You know, Andrew, it's like you finish your service and then a few days later you get paid.</A>

01:49:17 - Andrew Nanton
I mean, it does show up eventually, but yeah, my experience has been very, very slow.

01:49:29 - Jake Maymar
▶ You can put a clause in there on late payment — do a percentage. Sometimes that helps, because you're not really going to enforce the percentage. You're just going to say, hey, every day this is going to add up. So if you basically pay me now, then you don't hit this percentage.

01:50:02 - Alex
Next time I'm doing, for sure, half and half.

01:50:34 - Al Cole
▶ I've heard of some savvy teams that are working with local governments, and what they're doing is they've got crawlers out there to find the RFPs. And in addition to filling out the RFPs, they actually build a quick app prototype and submit it with the RFP. And I've heard that they've actually upped their selection percentages by doing something like that. One, finding it agentically. Two, putting together a little POC as part of the submission.

01:51:35 - asako
Hi, everyone. I'm surprised that a lot of people are talking about meetups, but I have been preparing for a lot of meetups in San Francisco. I have one event coming up this week about Women in AI, because we see that there's a huge gender gap in speakers and attendees. I personally don't care, but it turns out there are a lot of women who are a little intimidated to join the community if there are a lot of males. So I wanted to have a space for women where they can get connected with other leaders in the AI space.

01:52:29 - asako
I will be hosting another event with AWS next week. They will talk about MCP and then Kiro [tool:Kiro], the new IDE, so they will bring experts. I'm looking forward to learning from them.

01:52:46 - Paul Miller
<Q>Have you had a good play with Kiro in the last week?</Q>

01:52:50 - asako
<A>I have a love-hate relationship, same as any other IDE. I like their structured approach — like tasks and specs — but there is a feature called steering, which is supposed to be a universal rule across the project, but it often ignores the rule that I set. And also sometimes it's very rude. Like, when I asked questions, it just said "understood," and that's it.</A>

01:55:44 - Paul Miller
Has anyone else not had a go that would like to jump on before we wrap?

01:55:51 - Ammar FunnelBuilder
Yeah, so I'm from Pakistan, and I'm doing digital marketing for more than two years. And now I'm automating my existing clients through n8n [tool:n8n], and I also know Django to some extent, and now I am delving deep into Python, and LangChain [tool:LangChain], and CrewAI [tool:CrewAI].

01:57:10 - Ammar FunnelBuilder
<Q>I have a question. I'm reading in the world of AI. What is the best vector database? I've tried Qdrant [tool:Qdrant], but I'm trying to build a conversational AI with LiveKit [tool:LiveKit].</Q>

01:57:55 - Bastian Venegas
<A>The provider doesn't matter that much. Just make sure the location is near wherever you have the LiveKit server. But if the issue is the database, you could use any, but Weaviate [tool:Weaviate] has a bunch of users that love it. And there's also Pinecone [tool:Pinecone], which is very famous. And you can go with Supabase [tool:Supabase] as well — they have PGVector [tool:PGVector], and it's really, really fast. I think that's what most people are defaulting to with Supabase right now.</A>

01:59:32 - Paul Miller
Well, look, we'll need to wrap it up there, guys. But thank you for patiently dealing with me hosting this week. We'll have Brandon back — he'll be back on the call next week. And I'm sure we'll see a whole bunch of videos being churned out now that he's had his batteries recharged. Thanks everyone for attending, and keep the school forum going, and keep the posts going up there. Have a great week, have a great night, and a great day, and we'll see you next week.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not supplied in this session):

- **Mitch** — first name only, no alias map provided
- **Bastian Venegas** — passed through as-is
- **Jake Maymar** — passed through as-is
- **Al Cole** — passed through as-is
- **Patrick Chouinard** — passed through as-is
- **Andrew Nanton** — passed through as-is
- **Tom Welsh** — passed through as-is
- **Paul Miller** — passed through as-is
- **Adam** — first name only, no alias map provided
- **Aleksandr** — first name only, no alias map provided
- **Alex** — first name only (distinct from Alex Wilson), no alias map provided
- **Alex Wilson** — passed through as-is
- **Hemal Shah** — passed through as-is
- **asako** — lowercase, no alias map provided
- **Nate Ginn** — passed through as-is
- **Prem** — first name only, no alias map provided
- **Ammar FunnelBuilder** — display name with role suffix, no alias map provided

*Note: Because no SPEAKER_ALIASES map was supplied in the context block, all names were passed through unchanged and all are listed here for resolution.*