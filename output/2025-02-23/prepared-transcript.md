=== SESSION ===
date: Unspecified (references March 4th launch date)
duration_estimate: ~95 minutes
main_themes: AI tooling and model selection for coding (Cursor, Claude, O3 mini, DeepSeek), LinkedIn lead generation via content flywheels, multi-LLM app development (OpenRouter, LiteLLM, AI Suite), AI personal branding strategy, B-roll video generation agent (Slack + ElevenLabs + FFmpeg + Luma Labs), AI automation consulting business launch, content strategy coaching

---

<!--SEGMENT
topic: Session Open and Current Projects
speakers: Brandon Hancock, Tom Welsh
keywords: Cursor, Claude, Sonnet 3.5, DeepSeek, O3 mini, AI Authority Accelerator, prompting, coding projects, context window, Command Enter
summary: Brandon and Tom open the session with informal catch-up. Tom describes struggling with multi-shot fixes in Cursor using Claude Sonnet 3.5 and asks about switching to DeepSeek or O3 mini. Brandon demonstrates Cursor's Command Enter feature for full-codebase context retrieval and explains its 200,000-token context window advantage.
-->

**00:00:09 - Brandon Hancock**
Good morning, Tom.

**00:00:44 - Brandon Hancock**
My goal was to start focusing more on the AI Authority Accelerator [tool:AI Authority Accelerator].

**00:00:52 - Brandon Hancock**
So I think I was probably going to do one or two more, and then probably call it quits just because I have to do so much recording for the other stuff.

**00:01:00 - Tom Welsh**
It's honestly — I'm like, dude, you have no idea, I'm so excited for it to happen. At the same time it's like PTSD from doing the last course, recording so many hours. I've been at my PC since eight o'clock this morning just working on stuff. I meet over ten o'clock tonight and then I'll be good. Then get up at five in the morning, go to London. I'm currently working to take myself out of influence operation stuff, cyber stuff that I used to do.

**00:02:05 - Brandon Hancock**
<Q>How many current projects are going at the same time?</Q>

**00:02:10 - Tom Welsh**
<A>I've got the travel one, I've got the record one, I've got the major client, I've got the one I go to every day in London, and then I've got that one that's the mergers and acquisitions. So five.</A>

**00:03:00 - Tom Welsh**
I'm just experimenting with prompting and Cursor [tool:Cursor] just now and trying to get that down. My prompting still isn't the best because I'm not getting one-shot fixes — I'm getting five, six, or seven fixes. It'll fix it, then it'll break it, then it'll fix it again. I'm using Claude Sonnet 3.5 [tool:Claude Sonnet 3.5] just now, but DeepSeek [tool:DeepSeek] seems to be better. Maxim has been using it for his projects and he's only using O3 mini [tool:O3 mini] now, so a few people have started converting fully to just that.

**00:04:53 - Brandon Hancock**
▶ Let me know what you think of O3 mini because I love it. It takes a little bit — there is a small pause, it's not as fast on the initial thought process — but it really does a really good job.

**00:05:19 - Brandon Hancock**
▶ Whenever you submit the prompt, you can usually just press Enter, which looks at whichever files you specifically call out. If you do Command Enter, it grabs all files that are relevant — it searches through your codebase based on your prompt.

**00:05:36 - Brandon Hancock**
▶ Because it has such a huge context window, I always give it too much information. Its context window is 200,000 tokens. So that's my go-to, just so it's like — normally I'll say "fix this," but "fix this" really means I also need you to look at these three other files as well, because that's where the issue is. And it usually does a pretty good job.

**00:05:49 - Tom Welsh**
100%, because that's what I'm finding with Claude too. I'm handing it globals and layout TSXs, and it's like going, "I've got these three nice files but not the rest of the codebase as a whole," and that's what you really want, isn't it?

---

<!--SEGMENT
topic: LinkedIn Lead Generation Strategy
speakers: Brandon Hancock, delvis, Christopher Marin
keywords: LinkedIn, lead generation, engagement flywheel, comment magnet, content strategy, impressions, inbound leads, B2B, Alexandra, automation templates
summary: Brandon shares a case study of a team member (Alexandra) who generated four booked client calls within 24 hours using a LinkedIn comment-magnet post offering a free AI automation template. The group discusses how LinkedIn's algorithm rewards high-engagement posts and how this strategy creates a content flywheel linking YouTube videos, templates, and LinkedIn posts.
-->

**00:10:17 - Brandon Hancock**
The kicker is to do an application at the very end once they're live, just because there are some people I can't help. If they're not making content about AI, I don't want them joining — I can't actually help them.

**00:10:45 - Brandon Hancock**
Quick updates: Orlando, poor guy, got the flu. And Alexandra — one of her potential clients flew in from New York, so she's off hanging out with him right now.

**00:11:06 - Brandon Hancock**
I wanted to show you guys something awesome, just so you can take inspiration from it. What she was doing was creating automations and she started to want to help recruiters and get more automation clients. So she started putting together a LinkedIn post [tool:LinkedIn], kind of copying what we briefly talked about last time.

**00:11:38 - Brandon Hancock**
▶ She did an AI post — she's testing a mixture of agents — and she said "comment MOA below if you want to get access to this," which is the perfect hook because it explodes. People want a quick template they can download, and if you are trying to get a bunch of leads in your network super fast, this works.

**00:12:24 - Brandon Hancock**
In 24 hours — hundreds of comments ago — she already had four clients who booked calls with her. One post, that much exposure, four calls. And it's doubled since we looked at it yesterday evening.

**00:12:47 - Brandon Hancock**
▶ It's all a flywheel: make the YouTube video, and as a byproduct you get a template. By making the template you can repost it on LinkedIn. Once you post it on LinkedIn, you get hundreds of views. I just wanted to share that because she was hesitant, and then it just exploded. So now she's like, "I will do this forever going forward."

**00:13:20 - delvis**
<Q>Do you know by chance how many followers she has on LinkedIn?</Q>

**00:13:24 - Brandon Hancock**
<A>I can check real fast. I had 2,500 total connections and mine got around 250 comments. So there's a chance she has a few more connections, but it's roughly like 10% of whatever your follower base is — that's the rough number.</A>

**00:14:13 - Brandon Hancock**
▶ The reason why it works so well is: what does LinkedIn want to show? LinkedIn wants to show posts that are getting tons of engagement. This is the quickest way to get an insane amount of engagement, because you're giving away something completely for free. If you're using it to provide value to people and actually give them an asset they can take away, it's cheating on LinkedIn — that's really what it comes down to.

**00:15:09 - Christopher Marin**
I think follower count does matter to a degree. I ran social media at my last company — a B2B company — and right after LinkedIn introduced newsletters, we added one and had like 500,000 people sign up in the first month or so, just because our account had lots of people linked to it.

**00:17:25 - Brandon Hancock**
▶ It starts off slow and then exponentially takes off. The first 10 minutes, first 30 minutes, it was nothing. Then by hour two it was like four comments, then 10 comments, 20 comments an hour, 100 comments an hour. Once LinkedIn sees it's getting traffic, it just causes it to go. So it's a cool little flywheel.

**00:17:50 - delvis**
It almost seems like the more engagement, the more comments, the more LinkedIn gives impressions — it kind of builds up.

**00:17:25 - Brandon Hancock**
<A>Exactly. It just slowly starts off and then exponentially takes off.</A>

---

<!--SEGMENT
topic: Multi-LLM App Development and Content Fusion
speakers: Christopher Marin, Brandon Hancock, Tom Welsh
keywords: OpenRouter, LiteLLM, OpenAI Assistants, Gemini, ChatGPT, content fusion, multi-model synthesis, context window, LangChain, CrewAI, wisdom of crowds
summary: Christopher demos his custom multi-LLM app featuring a "Content Fusion" feature that sends a single prompt to multiple models and synthesizes their outputs. The group discusses API routing via OpenRouter versus direct connections, LiteLLM's role in abstracting provider differences, and the tradeoffs of tool-calling support across providers.
-->

**00:20:18 - Christopher Marin**
I'm just plugging away at my little app. I've had fun with it. I added a couple of new features this week. The one I'm showing here is Content Fusion [tool:Content Fusion], which I think is kind of fun. Basically you put in a prompt, you have multiple models and/or personas selected, it sends the prompt to them, they give their responses, and then the one at the bottom takes all of those responses and synthesizes them into a hopefully better solution that takes into account everything they came up with.

**00:21:22 - Brandon Hancock**
<Q>Could you share a concrete example of what that means?</Q>

**00:21:25 - Christopher Marin**
<A>A lot of the work here is what I find myself doing — I wonder what Gemini [tool:Gemini] would say about this, I wonder what ChatGPT [tool:ChatGPT] would say about it. They all seem to have their strengths. Sometimes I like to mix and match from different outputs from different systems. Some models are actually doing voting — if multiple models say this is the case, go with this. The idea here is you get outputs from multiple ones, and the bottom one tries to synthesize everything into one that takes into account all the different aspects.</A>

**00:22:30 - Brandon Hancock**
<Q>Have you run into any context window issues, out of curiosity?</Q>

**00:22:40 - Christopher Marin**
<A>Not yet. I have the default set to GPT-4o, which I think is decent. The idea is for it not to be a large back-and-forth. I should look into mitigations just in case.</A>

**00:23:23 - Brandon Hancock**
<Q>Did you end up going OpenRouter [tool:OpenRouter] to connect to all of them?</Q>

**00:23:30 - Christopher Marin**
<A>OpenRouter is what I started with, but I added a direct connection to Anthropic and also an OpenAI Assistants [tool:OpenAI Assistants] approach because I have some OpenAI assets I've shared that I like, so I wanted to incorporate those.</A>

**00:24:31 - Tom Welsh**
That's quite interesting. I've done something similar — I went to Cursor, pulled down all the models, synthesized two or three together to get the best kind of prompt coming out of them. Some similar lines, usually somewhat neater than mine though.

**00:24:28 - Christopher Marin**
It's a wisdom-of-the-crowd approach, right?

**00:25:00 - Christopher Marin**
Another one that's similar — this is based on an app I built. As a marketer I think it's very useful. I have a headline, I have some piece of content, I just want to get different options. So this Content Remix [tool:Content Remix] app gives you variations of that content, and you can control how many variations you want, change the style, word size, whatever — it's just a quick way to get different iterations.

**00:25:26 - Brandon Hancock**
<Q>Under the hood, did you end up going LiteLLM [tool:LiteLLM] to handle all the different chat protocols with all these different LLM providers, or are you raw-handling it?</Q>

**00:25:34 - Christopher Marin**
<A>For OpenRouter, just straight. I know CrewAI [tool:CrewAI] uses LiteLLM. As far as I can see, CrewAI doesn't support OpenAI Assistants.</A>

**00:26:01 - Brandon Hancock**
<A>Right now we've used LiteLLM because it's the easiest way to connect to everything and it has tool-calling built in. When you start to push these models to their limits — going from direct messages to tool-calling, structured responses — each provider does it differently, and LiteLLM handles all of that and provides utility checks like "yes, this model does support tool-calling." That was the main call: ease and safety.</A>

---

<!--SEGMENT
topic: AI Suite and Tool-Calling Simplification
speakers: Brandon Hancock, Christopher Marin, Tom Welsh
keywords: AI Suite, Andrew Ng, LiteLLM, tool calling, JSON schema, decorators, small agents, function passing, open source, college developers
summary: Brandon introduces Andrew Ng's open-source AI Suite library as an emerging alternative to LiteLLM, highlighting its simplified tool-calling API that auto-generates JSON schemas from plain Python functions. The group discusses LiteLLM's complex init file and the tradeoffs of being first to market versus iterative improvement.
-->

**00:27:00 - Brandon Hancock**
This one's made by Andrew Ng [tool:Andrew Ng]. It's called AI Suite [tool:AI Suite]. It's open source, it's free, and they're cruising on it.

**00:27:16 - Brandon Hancock**
▶ LiteLLM is newer, but I think AI Suite is going to make things even simpler eventually. They're basically going to take the best features of LiteLLM and make them even easier. They're not there yet, but they're getting there.

**00:27:42 - Brandon Hancock**
▶ The one thing that's so cool — they make tool-calling so easy. In the past, working with libraries like LiteLLM, you have to have a schema. But if you're just like, "hey, I just want to quickly spin up an agent and have it use tools," they make it so easy now. You can literally just pass in a function, create the client, and pass in the tool. It auto-generates all the schema under the hood. So much nicer, because that schema is a pain to generate.

**00:28:48 - Tom Welsh**
That's the issue of being first to market like LiteLLM. You bring it out, people see what you've done and go, "that's quite cool," and then they improve it a little bit more. Andrew Ng is quite cool.

**00:29:02 - Christopher Marin**
<Q>This versus small agents, which I know uses LiteLLM under the hood — what would be your take?</Q>

**00:29:14 - Brandon Hancock**
<A>I want to play with AI Suite so badly. I have not got to yet, but from my understanding, when it comes to tools, I still think you have to use LangChain [tool:LangChain] tools or CrewAI tools. Or I guess they have their own tool providers. I haven't played with it yet, but I'm so excited to.</A>

**00:30:19 - Christopher Marin**
I read an article about LiteLLM and how it was developed very quickly by college students who didn't necessarily have full-time experience. Someone was making particular fun of the init file, which has close to a thousand lines of code just to import a bunch of libraries — about equivalent to the whole small-agents library itself.

**00:30:47 - Brandon Hancock**
Dude, it is why — because we have to constantly go through the LiteLLM stuff to figure out why something is behaving interestingly. It's usually not for base cases. For basic LLM calls they absolutely crush it. But yeah, digging through that init file — I was like, this is wild. But hey, two college kids making it — hats off to them. I was not making that kind of cool stuff in college.

---

<!--SEGMENT
topic: Content Strategy Coaching for Chris and Tom
speakers: Brandon Hancock, Christopher Marin, Tom Welsh
keywords: Andrej Karpathy, LLM explainer video, YouTube content strategy, authority statement, AI marketing, cybersecurity, personal brand, niche selection, content quality vs quantity
summary: Brandon coaches Christopher and Tom on YouTube content strategy. For Christopher, he recommends combining AI and marketing automation as a niche, documenting real workplace automation projects. For Tom, he highlights the unfair advantage of 30+ years in cybersecurity and infrastructure as a content differentiator, and advises both on establishing authority statements before producing content.
-->

**00:32:00 - Christopher Marin**
There's Andrej Karpathy [tool:Andrej Karpathy] — I don't know if I'm saying his name right, he's the OpenAI [tool:OpenAI] guy. He did a video a couple of weeks ago on just "here's how LLMs are built from the ground up." [link:Andrej Karpathy LLM explainer video]

**00:32:27 - Christopher Marin**
What's funny — you see some of the comments there — there's no flashy graphics, it's not terribly polished, but the quality of the content is amazing and useful. So I guess I'd rather do fewer, higher-quality things than high-volume.

**00:33:04 - Brandon Hancock**
<Q>Quick thought on that — to pull off the raw lecture style, what do you need?</Q>

**00:33:10 - Brandon Hancock**
<A>▶ To pull that off, you have to be an expert. That's how they get away with just a raw lecture or a Loom video — you either know their name, so people are like "oh, I'm going to listen." That's when you've done it. But most mortals have to say "hey, I'm so-and-so, over the past few years, big flashy number, this many dollars, this many clients" — something to prove that what you're about to say is worth listening to.</A>

**00:34:13 - Brandon Hancock**
▶ If you want to go down that style, totally doable, just know you will have to hone in on two things: one, your authority statement going into the video; and two, your channel content will always have to center around that authority statement.

**00:35:36 - Brandon Hancock**
▶ My thoughts for you, Chris: what I think I would watch on your channel would be the combination of AI, marketing, and coding. Like, "I'm going to automate every task in my marketing business and I'm going to take you on the journey and share everything." You win because A, you're providing value at your company; B, you're sharing it online; and the amount of other marketing places that would say "I will pay you so much money to help bring exactly what you just did, but customized to us" — that's so easy.

**00:36:38 - Brandon Hancock**
▶ All you have to do is document the journey: "I set out this week to automate this marketing task at this company. I built this agent, I coded this up, and now it works. And I'm going to give everything away for free." The amount of marketing CEOs that would watch that and go, "this guy knows what he's doing, I'd love to have him" — and also the number of beginner-level marketing people who'd say, "can you please teach me how to do this so I can start doing it at my job?" You win twice doing that.

**00:37:33 - Tom Welsh**
I'm 30-plus years infrastructure cybersecurity [tool:cybersecurity] guy who's gotten into AI coding and stuff in the past four or five years. I did a Python course at Stanford during COVID. I've pushed it since then. So I could go from beginner to where I am now and just walk through the steps of getting there. That's how you package it and send it out to get views.

**00:38:30 - Brandon Hancock**
▶ For you, Tom — the fact that you're landing all these security jobs, that is your unfair advantage, and that's what I would lean into. When you're doing the jobs, how are you doing it faster with AI? How are you landing clients with AI? How are you getting speaking opportunities with AI? I personally have not seen many people bring up security — actual people working on security at companies — and AI. Cybersecurity used to be two people at the company I used to work for, and then more contracts came in and cybersecurity outnumbered every other engineer because the government is just hand-over-fist money at cybersecurity. It's a booming field.

**00:42:09 - Brandon Hancock**
▶ AI, cybersecurity, and then I don't know what you want to pick for your third topic — money-making, freelancing, software development, infrastructure — but those three I think would be your unfair advantage.

---

<!--SEGMENT
topic: Delvis AI Automation Consulting Launch
speakers: Brandon Hancock, delvis, Richard Collier
keywords: AI automation consulting, digital marketing agency, niche selection, cold outreach, Instantly, social proof, testimonials, lead generation, Make, Go High Level, Airtable, website vs no website
summary: Delvis shares plans to exit his digital marketing agency and launch an AI automation consulting business targeting marketing agencies. Brandon and Richard advise on prioritizing client results and testimonials over branding and websites, recommend cold outreach via Instantly, and discuss the importance of solving revenue-generating problems to command higher fees.
-->

**00:42:33 - delvis**
I own a digital marketing agency right now — we mostly focus on email marketing, PPC, and some web development. The last few months I've been trying to get out of that business. I'm in the process of selling off my portion and moving into AI. I'm in the process of launching AI automation consulting and eventually a development agency.

**00:43:23 - delvis**
Right now I just started doing branding. Next steps will be figuring out what the service is. I do have a niche — it's the same as what I was doing before. I'm going to niche into marketing agencies, automating processes within marketing agencies, because I understand a lot of the crap that goes on in agencies.

**00:44:00 - Brandon Hancock**
▶ Automating internal operations — love it. A combination of Make [tool:Make], Go High Level [tool:Go High Level], and Airtable [tool:Airtable] could really automate a ton of stuff. Another vertical I see absolutely crushing right now is cold outreach. Helping businesses with cold outreach — I just dropped you a video from Instantly [tool:Instantly]. [link:Instantly cold outreach YouTube channel]

**00:46:11 - Brandon Hancock**
▶ The reason I like it is that it's so directly tied to them making money. People are always willing to pay more if the problem you're solving is directly related to them making money.

**00:46:45 - delvis**
To be honest, that is the problem that most businesses have — lead generation. All suffer from getting enough leads or even qualified leads.

**00:47:42 - delvis**
The business idea I have — because right now there's a huge gap between AI and business — is to structure it as consultation first, then consultation leads to projects, and eventually third, templating the processes and reselling those processes over and over again.

**00:48:22 - delvis**
A specific one is social media content generation — building agents that build out a social media content team for a business. Then templating that. Because if this agency needs it, another agency is going to need it too.

**00:48:57 - Brandon Hancock**
▶ The more you can do a thing and then sell the same thing — it's cheating. If in your business you're automating all your content generation with AI, you then are the example. "You've obviously fallen into my content flywheel. Jokes on you — I used AI to do everything. But now that you're here, I'd be happy to teach you how to do it in your company as well. Heck, I could do it for you."

**00:50:09 - delvis**
I see it as an advantage — my agency today has over 100 clients. So I already have a list of clients to pitch for automation services.

**00:50:34 - Brandon Hancock**
▶ If this is your first time going in and building out the AI plumbing inside of one of these businesses, I'm a bigger fan of not charging as much to start, just because I want that raving fan testimonial. That one testimony keeps paying dividends — "hey, talk to my friend that I helped, they are so happy to hop on the phone with the next guy and say he is the man, hire him."

**00:53:00 - Brandon Hancock**
▶ Getting concrete: I'm a big fan of no brand and just do the work to start. Let LinkedIn and wherever you want to get clients be your social media page, because we are trying to reduce the amount of friction between you getting deals and clients. Every action should either get you a new client or get results for an existing one.

**00:57:00 - Brandon Hancock**
▶ Think about the customer journey — how is someone going to find the website? When you're starting from zero, most likely they're going to be reached out to through cold outreach, word of mouth, or they're one of your existing clients. If they fall into those three buckets, why have them go to the website when they should just be getting on the phone with you? A website is there when you want to showcase authority and when you have so much business that you're saying "fill out an application and I'll get to you when I can."

**00:58:19 - Richard Collier**
▶ I've sold a lot of clients without a website. One thing I do learn is the audience — what sorts of ways I can talk to them and what sorts of things they respond to. With AI, clients are just not sure what they need. They think they need this and they really need a chatbot. They think they need something else and they really need a Make automation. So the best thing is getting on the phone with you — maybe a structured calendar page or a Calendly-type page may work best when first starting out.

---

<!--SEGMENT
topic: Richard's B-Roll Video Agent in Slack
speakers: Richard Collier, Brandon Hancock, Christopher Marin
keywords: Slack, ElevenLabs, FFmpeg, Luma Labs, Shopify, B-roll agent, video generation, socket mode, ngrok, deployment, Railway, Neon, Docker, Dropbox, S3, content pipeline
summary: Richard demos a Slack-based B-roll video generation agent that pulls topics, scripts, blog posts, or products from his Shopify store and produces AI-generated videos using ElevenLabs for voiceover and FFmpeg for assembly. Brandon advises on deployment path (ngrok → Docker → Railway), database migration to Neon, and blob storage via Dropbox or S3. The group also discusses prompt safety filtering to prevent inappropriate image generation.
-->

**01:01:07 - Richard Collier**
So basically what I did was I hooked the B-roll agent [tool:B-roll agent] up to my Slack [tool:Slack] and everything. Right now I'm running in socket mode. The question I have is exposing this via ngrok [tool:ngrok].

**01:02:31 - Brandon Hancock**
<Q>What does ngrok actually do?</Q>

**01:02:31 - Brandon Hancock**
<A>▶ The issue is: you have servers actually on the internet, and then you have your local machine at IP address 127.0.0.1 — that means localhost, that means "self." So all these servers are like, "wait, how do I talk to localhost?" What ngrok does is it's basically port forwarding — send stuff to ngrok at this IP address and it'll forward it to where it needs to go. It just allows the internet to talk to our local computers.</A>

**01:03:07 - Richard Collier**
<Q>Does the computer still need to be on for ngrok to work?</Q>

**01:03:13 - Brandon Hancock**
<A>▶ Yes. If you are running this locally on your computer, the second your computer turns off, nothing will work. That's where you usually have to deploy it to a Docker container. The next step would be deploying this actual program to something like Railway [tool:Railway], so it's just running 24/7 waiting to be hit by a Slack webhook.</A>

**01:04:07 - Richard Collier**
I hooked this up to Slack and got it going. Now I have my B-roll agent in here. It asks me if I want to use a topic or a script. I can give it a topic, or I can give it a script I wrote myself. I also have it pulling blog posts from my Shopify store [tool:Shopify]. If I select blog posts, it pops up a modal with my first 25 blog posts. I select one and it starts making a video out of that blog post — changing the blog post to a video. I also have it set up to pull products directly from my site, with prices, so it gives a call to action.

**01:05:54 - Richard Collier**
What I'm having a problem with is the parser in the script. It did parse it but it truncated. The audio from ElevenLabs [tool:ElevenLabs] cuts off — a six-second clip just cuts off mid-sentence. The line is there but for some reason it's cleaning too much.

**01:10:09 - Richard Collier**
Basically we have our Slack command. When we drop our Slack command in the channel, it starts running the script generator, the text cleaner, the image generator, and then the video processor. It runs those with ElevenLabs and FFmpeg [tool:FFmpeg]. It takes the script, registers it down into one-line sentences, creates the image, the video, and the voiceover for that sentence. Then FFmpeg assembles it. The process repeats until the video is done — in this case there were 10 clips.

**01:12:28 - Brandon Hancock**
<Q>What's the end goal — is this to start allowing other people to buy this, or is this strictly an internal tool?</Q>

**01:12:37 - Richard Collier**
<A>The second one — it's making my life easier. I'm driving a truck so creating content is somewhat difficult. When I'm done, I'm 80-90% done with the content, I add transitions and sound effects, and then it's ready to be put out. The end goal is to have a ton of agents within my Slack channel that I can message to start workflows — for writing blogs, running analysis, things like that.</A>

**01:13:28 - Brandon Hancock**
▶ If this is your tool, totally makes sense to just keep it running on your own computer. The next level would be actually deploying this program to something like Railway, so it's just running 24/7 waiting to be hit by a Slack webhook. But until you're at the point where it stinks to keep running this in the background, if you can just keep your laptop up and let it do its thing, that's fine.

**01:19:13 - Brandon Hancock**
▶ Step one: anything that's a database, let's move it over to Neon [tool:Neon] — that's the cheapest free SQL database. Step two: we want to containerize your application with Docker [tool:Docker]. Before Docker, I would put blob store — as you're producing content, you want it stored somewhere else. Once it's done, either delete it or move it. You could use Dropbox [tool:Dropbox] pre-signed URLs, Google Drive [tool:Google Drive] with tokens, or get fancy and start using S3 [tool:S3] to store your stuff.

**01:16:00 - Christopher Marin**
If you want to have different video providers at some point, Google just released Veo 2 [tool:Veo 2] finally. It's very expensive, but you can get it through fal.com [tool:fal.com]. [link:fal.com] I was playing with it — it does very high quality. Even some of the things that Sora [tool:Sora] misses in terms of physics, it actually nails pretty well.

**01:24:51 - Brandon Hancock**
<Q>Any suggestions on how to prompt a model to prompt a model so we don't have some of these issues with inappropriate images?</Q>

**01:25:00 - Brandon Hancock**
<A>▶ Whatever prompt you're using right now — take that prompt and pass it over to a prompt reviewer and just say, "hey, anywhere in here, did it say anything not safe for work?" If so, tweak it. You're basically adding a not-safe-for-work filter — just review the raw prompt before passing it over to Luma Labs [tool:Luma Labs] and all these places.</A>

**01:27:31 - Brandon Hancock**
▶ I love how right now you have a few e-commerce people interested. Let's get that number to 10 people just paying you — however they pay, even through Stripe or PayPal, even using it in the most odd way via Slack to start. That's fine, because you're getting proof of concept and paying customers. Once we know that's happening, then we can have the conversation about how we turn this into a nice full-stack application. Could keep it in Slack, could be a WhatsApp add-on, could be a website — there are a bunch of ways we could take this. But the important part is getting those 10 people using it.

**01:28:04 - Richard Collier**
The reason I chose Slack is because I was trying to get a framework going where there's like a CEO and then an army of agents. Slack kind of actually handles that — it has the memory, it has an internal dialogue of messages they can see. Why cram all this into one framework when I can just make a separate framework with a CEO and throw him in the Slack channel and he can see what's going on and give direction without needing to handle so many messages internally inside of the code itself? I remember Sam Altman saying there's going to come a point where there's going to be a billion-dollar company with like one person in it. That's what made me build out in Slack — like a team of people collaborating.

---

<!--SEGMENT
topic: AI Authority Accelerator Launch and Personal Brand Q&A
speakers: Brandon Hancock, delvis, Tom Welsh
keywords: AI Authority Accelerator, personal brand, email course, content pillars, niche selection, monetization levels, AI wave, YouTube, LinkedIn, The War of Art, March 4th launch
summary: Brandon outlines his upcoming AI Authority Accelerator cohort launching March 4th, describing it as a master class on building an AI-focused personal brand. He explains the distinction between a regular personal brand and an AI personal brand (AI as core subject plus AI as production tool), and discusses the three-pillar content strategy and monetization levels. Delvis asks a clarifying question about what differentiates an AI personal brand.
-->

**01:30:41 - Brandon Hancock**
Quick updates on my side. Main thing I've been working on is getting ready to launch the AI Authority Accelerator [tool:AI Authority Accelerator]. This is basically where I'm going to focus on helping people build AI personal brands so they can go off and start landing their first clients organically.

**01:31:10 - Brandon Hancock**
This will be an actual email educational course going out on the fourth — March 4th. I'll be sending an all-call to everyone of like, "hey, if you are interested in this, let me know." It's basically a master class on everything that goes into creating an AI personal brand and what you need to do at each step along the way.

**01:31:36 - Brandon Hancock**
▶ My favorite two pillars are the last two. Pillar four is all about: once you have a niche, you've done content, and you're networking, how do you actually start making money? It breaks it down into levels — how to start at level one, why that approach works, how you scale to level two once you max out level one, and eventually how you scale to level three.

**01:32:08 - delvis**
<Q>I know there are a lot of people that sell personal branding help. What's the difference between that and an AI personal brand?</Q>

**01:32:26 - Brandon Hancock**
<A>▶ The core pillar of what makes a difference is that the core subject you discuss is AI plus two other things. So the subject you talk about actually has to be AI, and then the other core mechanism is that we're using AI at each point along the way to help us out with everything. So we talk about AI and we use AI. In Chris's example, he would use AI plus marketing plus either software or something else. That's why people would come to Chris to learn how he's replacing or automating a task at his marketing company.</A>

**01:33:23 - Brandon Hancock**
▶ Regular personal brands are obviously great, but we're trying to ride the wave that is exploding — which is AI. The demand is here and the supply is here. We're just trying to let people know we are available to help. Regular personal brands are harder to grow because you're not riding any waves, but with this one we are, and it just makes your life so much easier.

**01:33:58 - Brandon Hancock**
I also don't know how long the wave will be here — is it two more years? I don't know. So that's why while this is all working so well, I just want to help people. I think people are going to be amazed how many opportunities just come their way the second they start opening themselves up to opportunities online.

**01:34:48 - Brandon Hancock**
▶ Final thing — I shot you a link to that book, *The War of Art* [tool:The War of Art]. It talks about the board of resistance and it's one of my favorite books. I've read it like three times. It's also a great audiobook — the narrator has a cool voice — so if you're going on walks, that's how I like listening to it.

---

=== UNRESOLVED SPEAKERS ===

- **delvis** — Raw name "delvis" appears in the transcript. No canonical form found in the alias map. Passed through unchanged.