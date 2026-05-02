=== SESSION ===
date: Unknown (transcript timestamps begin at 00:04:01, end at ~02:08:00)
duration_estimate: ~2 hours 4 minutes
main_themes: Claude Code remote control & multi-machine orchestration, agentic DevOps with AWS/Docker/Proxmox, model fine-tuning experiments, web deployment stacks (Astro/Cloudflare/Svelte), personal knowledge management (Obsidian vs. Notion), AI-assisted lead generation with Meta glasses, Azure privacy perception challenges, teaching AI to non-technical users

---

<!--SEGMENT
topic: Pre-Meeting Casual Check-In
speakers: Ty Wells, Marc Juretus
keywords: Omaha, Bahamas, golf, Allentown Pennsylvania, Billy Joel, OpenClaw, calendar automation, Dockling, RAG, Claude Code
summary: Ty and Marc exchange location updates and recreational small talk before the meeting formally begins. Marc briefly previews his ongoing Claude Code and OpenClaw projects, including a RAG-based customer service chatbot and an HR resume-ranking agent built with Dockling.
-->

00:04:01 - Ty Wells
What's up, Marc?

00:04:06 - Marc Juretus
Hey, Ty. How you doing, buddy?

00:04:08 - Ty Wells
Good, man. Played some golf today. I am exhausted.

00:04:14 - Marc Juretus
Where are you? Are you going to be in Bermuda, or are you just going there?

00:04:17 - Ty Wells
I'm in Omaha right now. I'm going to be in the Bahamas tomorrow. I'm back down.

00:04:24 - Marc Juretus
Nice. It's warming up the golf out in Omaha.

00:04:27 - Ty Wells
Uh-huh. Let's just say it was 40 degrees, but there was no wind.

00:04:33 - Marc Juretus
Yeah. I don't know if that's warm.

00:04:36 - Ty Wells
It's only when you see the crazies come out, and I'm included in that group, apparently.

00:04:41 - Marc Juretus
I was about to say, you only going to see the passion out there for that. Man, geez.

00:04:45 - Ty Wells
People that put their clubs inside from fall, from October — my clubs have been in the back of my car all season, ready to go.

00:04:57 - Marc Juretus
That's good, man. You got to have a passion, too. Escape, so good for you, brother.

00:05:01 - Ty Wells
Yeah, it's a good escape, actually. Got some grass. Getaway. Where are you at?

00:05:08 - Marc Juretus
Near Philly, in a place called Whitehall. Maybe a few miles from Allentown, Pennsylvania, if you've ever heard of it.

00:05:15 - Ty Wells
I haven't been to Allentown, but I remember Allentown. Is that based off the movie *Town*?

00:05:27 - Marc Juretus
No, but I believe that Billy Joel's song "Allentown" is about that town. That's where I grew up, but I moved to Whitehall later in life.

00:05:38 - Ty Wells
Gotcha. How's your Claude Code, your OpenClaw, going? Did you launch something?

00:05:43 - Marc Juretus
Yeah, well, I still have the OpenClaw [tool:OpenClaw] going where I send it a prompt and it'll go to my calendar and send that person information. This past week I was working on — I just keep spinning up different types of sites just for experience so I can expose what I have. So this one I pretended like I owned a high-speed internet company. I'm the president of it. I had to create 58 documents that I RAGged with Dockling [tool:Dockling] for a full-service chat and then also a resume upload with an HR agent that grades them and then either says forward, hold, or reject and sends an email. So, like Brandon said, do real-world solutions where people want to put you to use.

---

<!--SEGMENT
topic: AI Code Quality and Debugging Realities
speakers: Ty Wells, Marc Juretus, Ana P
keywords: AI-generated code, Claude Code, hallucination, debugging, stack trace, context window, AI slop, agentic agents, fitness app, dictation
summary: The group discusses the real-world quality of AI-generated code, noting that debugging and stack-trace resolution — not code generation — is the primary bottleneck developers use AI for. Ty warns about "AI slop" from lower-quality platforms and hallucination rates even in Claude Code, while Marc shares a positive experience with a fitness app that correctly mapped dictated workout summaries to exercises on the first attempt.
-->

00:06:26 - Ty Wells
▶ Do something every day to make all those monotonous things that you do better, right? You don't get any things that you dread doing. Make a list of those and solve those every day.

00:06:47 - Ty Wells
And yeah, I'm working on something to solve them for me, but with what I'm framing as an agentic — a long-running agent that can go and do what it is that I need it to do. And a lot of things can do that. I mean, a lot of platforms you can, you know, natural language, go build me this. Problem is when it builds it, it's a piece of garbage. It's AI slop. It's garbage under the hood. I mean, it's horrible. When I look at some of the code that comes out of some of these platforms, it is just crazy. And I mean, the statistics show they're spending more time fixing AI-generated code than they are writing it. And they're getting better. You know, a year ago, they were really, really bad. They're getting better every day. And Claude Code [tool:Claude Code] does a pretty good job of producing good code. But hallucination is 30% of what happens. So sometimes you're trying to squeeze that context window and boom, you've got some bugs in there. And then that propagates through the code. It's a battle, for sure.

00:08:02 - Ana P
Something that I thought was very interesting — I saw a statistic on what are people using AI for? And the top was stack trace. So basically, debugging.

00:08:16 - Ty Wells
Yeah.

00:08:17 - Ty Wells
Because a lot of people always think of, like, writing code.

00:08:20 - Ana P
▶ But that was never really the bottleneck for development.

00:08:24 - Ty Wells
Yeah.

00:08:26 - Marc Juretus
Fixing, for sure.

00:08:27 - Ty Wells
Fixing, just troubleshooting. God, that could suck up some time.

00:08:34 - Marc Juretus
When you kind of know the task that you're trying to accomplish, and you've done stuff, and you clearly put that into a prompt, it does improve it. Like, I got to admit, that fitness app I displayed to you guys — man, that wrote some pretty, I'd say about 80–85% of the code. The one that blew me away, where I thought I won't get this one right, was where I go in, and I can hit a dictate button, and you just summarize your workout. And then it maps it up to the exercises they have. And I was like, it's never going to get this right. And it got it right the first time.

00:09:07 - Ty Wells
I know. Here's what to do — I've been doing this. Every time it surprises me, I take a picture on my phone. I'm building this collage of just little wow factors. Every time Claude Code comes back with something like, hmm, you got that, huh? That's pretty good. I've been building it out. And I need to tweet all of this over the last year to show the transition — it's like the Will Smith video, right? The latest one is spectacular.

---

<!--SEGMENT
topic: Claude Code Remote Control Feature
speakers: Patrick Chouinard, Marc Juretus, Ty Wells, Ryan C
keywords: Claude Code, remote control, slash command, Tmux, Claude mobile app, voice for Claude Code, 11 Labs, CLI, Cloudflare, multi-machine
summary: Patrick introduces Claude Code's new /remote-control slash command, which allows a running Claude Code CLI session to be accessed from the Claude mobile app. He explains how he uses Tmux to keep sessions persistent and accessible from his phone. The group also discusses an upcoming voice interface for Claude Code being rolled out to 5% of users, and Marc's OpenClaw agent that was sending him unsolicited status reports.
-->

00:09:40 - Patrick Chouinard
Hey, Patrick.

00:09:42 - Ty Wells
What's up, Pat?

00:11:11 - Patrick Chouinard
I wanted to talk a little bit about something I worked on this week. It's not finalized, but it's starting to work. I'm leveraging my Claude Code [tool:Claude Code] as my operator, and I've started at the network layer, but now it's really spawning my machine. Basically, I no longer use a boilerplate Docker template. I just created a template for a Claude Code project that spawns other machines. Quite nice. So when it runs the Docker, it spins up Ubuntu or whatever — like servers online for you?

00:11:50 - Patrick Chouinard
Basically, the documentation that initialized the project contains all the information on how to harden a blank VM from the start, deploy Docker, and then start deploying the application. Basically, it started because I wanted to use the new Claude remote control functionality, and the fact that it's limited to one per machine. So I figured out how to spawn a bunch of containers with Claude Code inside them, open a session, do the remote control through a Tmux [tool:Tmux] connection, then just drop the connection but leave the session alive — and there you go.

00:12:37 - Ty Wells
Only you, Patrick. Only you, man.

00:13:06 - Patrick Chouinard
With that methodology, I have a bunch of machines that are started that have a Claude Code session running on it that I can access through my phone. Actually, I went to the barber this weekend. And for the time I was there, I developed two applications.

00:14:09 - Marc Juretus
<Q>So you're actually doing prompting from your phone, and somehow there's a connection — what do you have, some type of Cloudflare back to your PC?</Q>

00:14:19 - Patrick Chouinard
<A>No, it's a new functionality of Claude Code — in Claude Code, you can just type a slash command called `/remote-control`, and it will enable remote control of your Claude session. Then on the Claude mobile app, if you go into the code subsection, you're going to be able to select that session and continue it from your phone, but it actively runs on your machine at home.</A>

00:14:49 - Marc Juretus
But not CLI though, or is it — it's actual CLI you're running, really?

00:14:55 - Patrick Chouinard
Yeah, yep.

00:15:00 - Marc Juretus
I didn't even know they had that feature, honestly. I don't even have a Claude app. I just go into my browser. I didn't even know Claude had an app. I got to get it.

00:15:18 - Patrick Chouinard
Actually, I'm not sure if I should tell you that, but they just said that they are working on voice for Claude Code this week — that's supposed to be released to about 5% of the users.

00:15:31 - Ty Wells
Yeah, I saw that, and I'm thinking 11 Labs [tool:11 Labs], retail. I'm like, oh, my God. These guys just pop some release and just — they're making impacts.

00:15:43 - Marc Juretus
It's funny. I actually turned off my virtual — my OpenClaw — because it was getting like a girlfriend, because I had like a couple of achievables I wanted, and it kept coming at me for status reports. I was like, yeah, that's enough of you. I just turned it off. I was like, I'll get back to you another time.

00:16:11 - Marc Juretus
So that comes up in the prompt — slash remote... Really, I got to take a look at this. It's slash remote-control.

00:16:32 - Marc Juretus
Oh, slash remote-control. Yep. That's the one you mean. Yep. Oh, my God. All right. That's cool.

---

<!--SEGMENT
topic: Marc's Model Fine-Tuning Experiments
speakers: Marc Juretus, Patrick Chouinard, Juan Torres, Ana P, Morgan Cook
keywords: model fine-tuning, Google Colab, Hugging Face, Vertex AI, Gemma 1B, LoRA, scikit-learn, matplotlib, resume ranker, movie recommender, EC2, GPU, small models, training epochs
summary: Marc describes his experiments training small models using Google Colab and Hugging Face — a resume-ranking classifier and a movie preference recommender built from thumbs-up/thumbs-down data. The group advises using small models like Gemma 1B for proof-of-concept work, noting they are faster, cheaper, and better at exposing training edge cases. Patrick and Ana suggest deploying fine-tuned models on EC2 for a more professional, transferable learning experience.
-->

00:18:22 - Marc Juretus
Like I was telling Ty earlier, I'm probably going to take the exam in a couple of Saturdays — the Google AI generative leader exam. Not that it means much, but that's on my plate. I've been studying for that. But what I'm doing is — I did spin up a bogus high-speed cable company where I'm the vice president, where I did a RAG with Dockling [tool:Dockling], because I had never used Dockling before. It created 50 documents about the company, answered a bunch of questions and inventory, as well as a resume upload tool that ranked the resume and gave it either a forward, hold, or reject. And what I'm playing with now — it took 50 resume snippets and information, you put it up in Google Colab [tool:Google Colab], it spins up a model, and then you save it back to Hugging Face [tool:Hugging Face], and I'm consuming that model to either say reject, forward, or hold. So I'm kind of working on just saying, hey, if someone asked me, have you trained a model — I have, on a low level, using Google Colab and Hugging Face.

00:19:46 - Marc Juretus
<Q>Is anybody on here — have you trained models? What have you used?</Q>

00:20:03 - Juan Torres
<A>No, I've deployed an LLM in EC2s [tool:EC2] as it's big enough with the GPU, so I had to do some changes on how the GPU and the CPU work together, but never to train — not for LoRA or low-ranking kind of fine-tuning at all.</A>

00:20:35 - Marc Juretus
The other one I'm working on now — it's going to generate 100 movies for me, and I'm either going to give it thumbs up or thumbs down, and at the end, it'll give me data that I'm going to throw to Google Colab, and allegedly it'll build me a model that I could point to. And say I got a list of 20 movies, it'll tell me which ones I allegedly would like based on that 100-data-set of me saying yes or no to a bunch of movies. So just curious to see how it does.

00:21:29 - Juan Torres
<Q>Yeah, I just wanted to know why you need to fine-tune or train a model.</Q>

00:21:37 - Marc Juretus
<A>I just wanted proof of concept that I've done it. It interests me. I went halfway through a data science class on one of those online ones, learning like matplotlib [tool:matplotlib] and scikit-learn [tool:scikit-learn] and all that. But I've never really made one.</A>

00:22:09 - Marc Juretus
At the end, it actually built, but it said the version that I built, you can't expose to an API endpoint. You need to build it another way. And this is $32 later. So I was not very happy about that.

00:22:41 - Patrick Chouinard
▶ If you look at something like a Gemma 1B [tool:Gemma 1B], for example, try to look at a very, very small model. First, it's going to go a lot faster. It's going to be a lot cheaper. You're going to be able to turn around easier. And it's going to prove your point that you're able to train a model without spending too much.

00:23:00 - Ana P
▶ The other thing is, if your objective is learning, if you use a demo model like Patrick says, then you can try deploying it without — in an EC2 instance — and make the argument of, like, if you're going to be building something with very high traffic, you save money on the requests, and you get that learning experience as well from the same fine-tuned model.

00:23:44 - Patrick Chouinard
▶ I think the skills are transferable, and the fact that what you're doing actually works very well with a small model, because you're not trying to build something that's going to be cognitively extremely complex. You want a movie categorizer. That fits extremely well in a one-billion-parameter model, even a 700-million-parameter model.

00:24:06 - Marc Juretus
I will say this, though — when I was watching it as it actually ran the Python code for building the agent, it was funny watching it go through. It took the 50 pieces of data, then its accuracy on testing was 27%, then it did another epoch, then it went up to like 52%, then it went up to the 60s, and eventually it said, okay, we've hit 80-something percent, the model is at this accuracy, it's complete. So that was interesting.

00:24:39 - Morgan Cook
▶ Yeah, I was going to say, if you can build it on a smaller model, then that can actually show you the edge cases where your training is effective and not, versus when you build it on the larger model. The larger model might be taking care of a lot of the stuff that would be beneficial. You'll see more of the change from the smaller model training than a larger model training from a simple prompt to actually using your training data — it might expose more of your training metrics with a smaller model.

---

<!--SEGMENT
topic: Ty's AGI Testing and Strategic Shift
speakers: Ty Wells, Patrick Chouinard
keywords: ARC-AGI-1, ARC-AGI-2, non-transformer model, long-running agents, memory, extended sessions, software commoditization, Anthropic, Limitless device, Secure Claw, agentic AI
summary: Ty explains he has shifted focus away from building software applications toward deeper research — specifically testing his agent against ARC-AGI-1 and ARC-AGI-2 benchmarks and exploring non-transformer model architectures. He argues that software development is being commoditized and that the real opportunity lies at a lower level. He also describes using a Limitless wearable device with a trigger word to feed requirements to his Secure Claw agent while moving around his office.
-->

00:26:17 - Ty Wells
Hey, guys. Not doing much this week — well, that's a lie. Doing a lot over the last week, except doing a lot of testing. I don't know if you guys are familiar with the ARC-AGI-1 [tool:ARC-AGI-1] and ARC-AGI-2 [tool:ARC-AGI-2] testing. So I've been running some tests with my agent, trying to see how it fares with that. And I'm working on a technique for a non-transformer model. So yeah, just diving. The reason I'm doing these things that are outside of building software is because the things that we were seeing in the news — like we just talked about, right? Anthropic [tool:Anthropic] lays something out, software has been commoditized, it's been democratized, I guess, and so it's building faster, cheaper, and the quality is getting better, the security is getting better, so I don't see that as the play.

00:27:24 - Ty Wells
▶ I see the play — software will still be needed — but I'm trying to see what's around the corner, trying to get a little deeper, not really at the application level. So that's really where my focus has shifted to. If I build anything, I build it as I need it, because it's just so easy.

00:28:00 - Ty Wells
These other things — the agent that I do have meets the majority of the criteria for a long-running session, extended session, memory over multiple sessions — all the key values of what AGI is. And that's really just to build, like I said, what I need.

00:41:46 - Ty Wells
So a couple of weeks ago — and I'll be doing this again tomorrow — I have my Limitless device [tool:Limitless]. I don't know if you guys can see it. So I have a trigger word on this. My Secure Claw [tool:Secure Claw] picks it up and is building. I'm telling it to add this feature, so I'm on-site doing work and building it in when I'm doing it. By the time I actually leave and move around my offices, and by the time I get back to my desk, it's pretty much done. If it has something, it'll send me a message in Telegram [tool:Telegram], I'll tell it what to do and it'll continue on. So I'm just listening to them and summarizing and sending that off as a requirement. And it's building it as I go.

00:42:32 - Ryan C
I need one of those. That sounds amazing. So many times I'm talking to someone about an awesome project and I'm like, oh God, now I've got to go quickly and get that into the notes before I forget what I said. That'd be ideal.

00:42:47 - Patrick Chouinard
Limitless people are incredible.

00:43:00 - Ty Wells
Meta bought them but they're no longer selling the device.

00:43:07 - Patrick Chouinard
They are supporting it for a while, but they're no longer selling it. So that's why I was showing this — this is the Fieldy version. It's similar. It's not exactly the same, but it's pretty close and they're developing extremely fast.

---

<!--SEGMENT
topic: Web Deployment Stack — Astro, Cloudflare, Svelte
speakers: Morgan Cook, Patrick Chouinard, Ty Wells, Tom Welsh, Marc Juretus
keywords: Astro, Cloudflare, Wrangler, Svelte, React, Next.js, Streamlit, HTMX, static sites, CLI, CI/CD, GitHub Actions, KV, D1, R2, Proxmox
summary: Morgan asks Patrick about his Cloudflare deployment stack for a mostly-static client project. Patrick recommends Astro with Wrangler CLI, noting Claude Code is more effective with CLI tools than MCP servers. The group discusses a frontend progression from HTMX → Astro → Svelte → Next.js, and Ty advocates for CLI-only interfaces to reduce front-end testing overhead. Patrick reveals Astro is now his primary publishing platform for all written content.
-->

00:30:51 - Morgan Cook
Hello, everybody. So my question for today is — I know, Patrick, you've done some stuff up on Cloudflare [tool:Cloudflare]. I have a small project I need to do for somebody, and it's mostly static, but maybe a little bit of access to their KV model or the D1 and R2 models with Cloudflare. Did you use Astro [tool:Astro] and Wrangler [tool:Wrangler]?

00:31:18 - Patrick Chouinard
Yep.

00:31:19 - Morgan Cook
Okay, so that's a good stack right there to push something out there for a free site?

00:31:25 - Patrick Chouinard
So far, it's been working very well. Wrangler is actually — that's something I started to realize. ▶ With Claude Code, I prefer CLIs like Wrangler to MCPs. For some reason, Claude is far more effective using a CLI than using an MCP server. So you just build whatever you need, and Claude will take care of knowing how to deploy it. It will actually hold your hand configuring everything on Cloudflare.

00:32:00 - Morgan Cook
<Q>Are you pushing the Cloudflare from your workstation, or are you pushing CI/CD from GitHub?</Q>

00:32:06 - Patrick Chouinard
<A>Actually, on my part, I'm pushing directly from a VM that runs on the Proxmox [tool:Proxmox] server locally. I try to avoid GitHub Actions when I can because I don't like to pay for it if I can have my own infrastructure do the job.</A>

00:33:00 - Patrick Chouinard
▶ Basically, every site I've shared over the week — they're all Astro sites being hosted on Cloudflare.

00:33:15 - Ty Wells
Yeah, no, I was just going to add that everything I write is CLI. I don't actually write any UI-facing anything anymore. And even if I had some, I've added a CLI interface because it works a lot smoother. They can talk to each other easier, less stuff you have to test on the front end — that's usually the stuff that's breaking, right? ▶ So yeah, if you're building something, CLI is definitely the way to go.

00:33:51 - Patrick Chouinard
Yeah, I just wanted to say, if you ever need a little bit more oomph from your static website, I like Svelte [tool:Svelte]. Astro is perfect for 90% of the static framework, but if you want some active component, adding a Svelte component will give you — it's not all the way up to React [tool:React], but it does a decent job. It's where you're going to be as close to React without building an entire Next.js [tool:Next.js] application.

00:35:38 - Patrick Chouinard
▶ Basic HTMX [tool:HTMX] would be the baseline. Then I would go to Astro, and then if you want a little bit more than that, then I would go to Svelte. But then after that, it's a full .js front end.

00:36:00 - Morgan Cook
Yeah, this whole stack for this project was suggested by Claude.

00:36:06 - Patrick Chouinard
Yeah. Actually, Astro is now my publishing platform. Like, everything I write, I no longer publish PowerPoint or whatever. I just publish it as a static Astro site.

00:36:32 - Marc Juretus
<Q>Can you elaborate a little bit more on Astro? I've never heard of it.</Q>

00:36:37 - Patrick Chouinard
<A>Basically, I don't know if you heard about Hugo — there's a bunch of sites that will take Markdown as input and they will present it as a full interactive dynamic HTML page. It's static content, meaning there's no database behind it. But you have interaction — you can even get search, a bit of filtering, a bit of collapsing sections on your website, and that's all taken care of by the Astro framework.</A>

00:37:12 - Marc Juretus
So it's a step before a Next.js app, and it's probably a step better than Streamlit [tool:Streamlit], I would gather.

00:37:19 - Patrick Chouinard
▶ Exactly, yeah. Streamlit is very, very basic. Then Astro will give you a lot of theme configuration, and you can brand stuff very, very effectively. It will almost look like a Next.js site. It just doesn't have any connectivity behind it.

00:37:40 - Morgan Cook
And a lot less client-side JavaScript. It's all server-side built and deploying static content to the client.

00:37:46 - Patrick Chouinard
So if you want client-side JavaScript for components that cannot be built in advance, that's where Svelte comes into play.

---

<!--SEGMENT
topic: Heritage Plot Project and Client Pacing
speakers: Morgan Cook, Patrick Chouinard, Ty Wells, Tom Welsh, Marc Juretus
keywords: Heritage Plot, gravesite mapping, SEO, marketing research, pricing strategy, AI development speed, client bottleneck, Limitless device, Secure Claw, Telegram
summary: Morgan provides an update on Heritage Plot, his gravesite-mapping SaaS project. He has met with the main client and engaged a marketing team to research pricing and target audience. The group discusses a recurring theme: AI enables software to be built far faster than traditional business processes can keep up with, creating a bottleneck on the client/stakeholder side rather than the development side.
-->

00:38:37 - Morgan Cook
I did meet with the main client for the Heritage Plot [tool:Heritage Plot]. And collected some more specific information about what they need in the application. So I can't wait to get a few things off my plate to really dive full-time into that project.

00:39:05 - Patrick Chouinard
Actually, let me leave a little verbal note for Brandon in the video so we can review that, because I know he was very interested about knowing where that project was going, Morgan.

00:39:17 - Morgan Cook
Yeah, and I took your guys' advice and got my marketing guy doing the actual research on price break and all that kind of jazz and who to actually market to. Right out the box, so he's working on that right now. He got a little bit of preliminary data back to me on the price point. And then we'll just kind of move forward from there. See if we can't undersell all these guys a little bit or produce something that's more valuable that they really need.

00:40:08 - Ty Wells
Actually, I do have a question. How's your gravesite project going?

00:40:14 - Patrick Chouinard
Yeah, that's what Heritage Plot is.

00:40:17 - Morgan Cook
Yeah, good. So it's going good. So we're moving ahead. I've got another meeting with them this week. The thing that's slowing it down is waiting for them. It's like they don't understand how quick this stuff can happen.

00:40:30 - Ty Wells
Yeah, yeah, that is true.

00:40:36 - Morgan Cook
Used to the old slow-turning wheel. Yeah, we'll talk about it in our next weekly meeting, and we'll get back to you a month later. It's like, okay, well, I'll be on to something else by then.

00:40:49 - Tom Welsh
Yeah, so that just seems to be such a blocker. The time to market now for pieces of software is really, really quick. But what seems to be happening now is the other pillars in the business — you run into marketing and this — you know, like, oh, we'll have a meeting next week about it. Like, I'm ready to go right now.

00:41:15 - Morgan Cook
I have an SEO team that's working on the project too, and they sent some suggestions for what they would like to change on the website and wanted me to spec it out and send it back to them. And I'm like, well, if I'm going to spec it out, I'm just going to tell Claude to do it. There's no point in the communication. You're adding all kinds of friction to the process, right? I mean, by the time I explain it to you in context enough so that you can implement it correctly, I could have done the same thing with Claude and be done with the whole process.

---

<!--SEGMENT
topic: Agentic DevOps — Claude Code as Infrastructure Operator
speakers: Patrick Chouinard, Juan Torres, Tom Welsh, Morgan Cook, Ty Wells, Elena
keywords: Claude Code, Docker, Ubuntu, Proxmox, Tmux, remote control, GitHub, Kiro CLI, AWS CLI, EC2, agentic DevOps, infrastructure as context, Prometheus, Grafana, Alert Manager, Discord, Alpine, Debian, CI/CD, context engineering
summary: Patrick demonstrates his Claude Code Docker Server Setup Template — a context document that instructs Claude Code to provision, harden, and deploy a full Ubuntu server from scratch, including SSL, Docker, and Claude Code itself as a persistent operator accessible via Tmux and the Claude mobile app. Juan shares parallel experiments using Kiro CLI and AWS CLI for agentic DevOps. The group discusses "infrastructure as context" as an emerging paradigm, and Patrick describes a monitoring stack with Prometheus, Grafana, and Discord-based alerting that Claude can autonomously resolve.
-->

00:58:37 - Juan Torres
Hey, folks. I was able to finally get my landing page. Let me share it here.

00:59:29 - Patrick Chouinard
<Q>Is it me or is there any part that are clickable?</Q>

01:00:06 - Patrick Chouinard
And I'm guessing that the three tiles at the bottom are coming-soon content?

01:00:14 - Juan Torres
Oh, well, that really is just what I'm specializing in. But I do plan to add a case study or projects that display some of those skills.

01:00:40 - Ty Wells
Juan, one thing that I've been doing lately — if I build a UI now, I'm trying to restrict the viewport. So when you pull it up, what you see, you can get to everything. No horizontal scrolling. I'm just trying to stay away from the scroll, just have everything. I think I showed you guys one application where the website is the application as opposed to an actual website. It's as if you're in the app already so you don't have to scroll.

01:01:38 - Morgan Cook
<Q>You mind sharing what 3D model you used to build the background?</Q>

01:01:48 - Juan Torres
<A>Vanta.js [tool:Vanta.js]. So I picked the globe one. There's the net one, there's the cell ones.</A>

01:03:08 - Juan Torres
By the way, guys, it was really interesting. Last Saturday, I was finally developing with, I guess, agentic DevOps, so I was using Kiro CLI [tool:Kiro CLI] in order to just use natural language in order to create resources within AWS [tool:AWS]. But at the same time, simultaneously, I was using Claude Code with AWS CLI [tool:AWS CLI]. So essentially, technically speaking, you could carry out agentic DevOps by just giving your Claude Code the AWS CLI permissions — you just have to create a user with the right permissions and the right policies. And you can just basically tell it to create an EC2 instance, the security rules, inbound, outbound rules, database, network settings. It was really great. I've never tried agentic DevOps, and this really could just speed up my work.

01:04:37 - Elena
Did you try Kiro, like, not CLI, but normal, like the IDE?

01:04:41 - Juan Torres
Oh, the Kiro IDE [tool:Kiro IDE]? No, I haven't tried it.

01:04:46 - Elena
I'm using Kiro right now as an IDE. I also have Cursor [tool:Cursor], and I don't know what I like more. I think it's not much difference. But I also found that using Claude Code inside — it's still beneficial than just using Kiro agents for some reason, kind of more accurate, I would say. And Kiro has — unless you steer it very well — a tendency to create specs not like for an MVP, but like it will start putting some performance requirements, like it should be at this kind of response time. So basically it's probably good for a full-fledged project, but not for MVP.

01:06:00 - Patrick Chouinard
For DevOps? Yep. I did a bit. Well, I'm talking with DevOps people that are starting to integrate it into CI/CD. And in terms of machine provisioning, also, I have a bit of things to say a little bit later.

01:07:34 - Patrick Chouinard
So, a little project I started on the side last weekend — what it is is an architecture document that I created that I give to Claude Code when I start the creation of a new machine. So Claude Code Docker Server Setup Template. It starts from a blank Ubuntu Server, and it will configure it completely. It will do all of the hardening, the SSL configuration, the preparing the token, and preparing the connected... And it takes, at the beginning, just a couple of variables — the VM name I want to configure, the IP, the VM user, my GitHub user, because I create all the VMs as GitHub projects. I also deploy Claude Code on the VM as my operator. And now with the remote control functionality, I can leave Claude Code running in remote control. Basically, I start it through a Tmux instance and I disconnect from it. So it basically is a CLI that's long-lived on the machine, and it's available now in my mobile client. So I can always interact with it. And since Claude has been the one building the machine, it has all the context about how the machine is configured. So if I need to add a service, remove a service, change an access right, whatever — Claude is able to do it completely.

01:10:00 - Patrick Chouinard
So all the documents you're seeing here — I went through that configuration once manually with Claude, and at the end, I just said, dump everything we've done into a procedure that I can give you again to start and do that a second time on a new machine. So now I can spawn as many of those Docker servers. And inside, for my dev servers, I also started to create Docker containers that have Claude Code in them. And I create a single container per coding project with their own instance of Claude Code connected through the same way — I open Tmux, I start a Claude Code, disconnect Tmux, I'm remotely into it. So now I have like seven or eight sessions available on my mobile phone that I can connect to, or from the web client from a standard workstation outside of my house. It's fully secured connectivity, managed on the Anthropic side, so I'm not exposing anything.

01:11:26 - Juan Torres
Yeah, this is great. This is what I want to get to eventually.

01:11:33 - Tom Welsh
<Q>Sorry, Patrick — so are you starting from a Ubuntu VM already installed, or do you provision that as well?</Q>

01:11:40 - Patrick Chouinard
<A>Actually, I want to start provisioning the VM as well. For now, it's just a Proxmox server that I have that I install a blank VM on. So when Claude Code starts working on it, the only thing that's been configured is it's been updated and it has its network stack configured. That's it.</A>

01:12:00 - Tom Welsh
Yeah, because I use Ansible [tool:Ansible] to provision virtual machines under Oracle Virtual Manager. So yeah, basically command lines of like Ubuntu 24, web server, dev tools. There it is. That's my base image. And then, like you say, Claude takes over.

01:12:21 - Patrick Chouinard
Exactly. And honestly, I could have Claude Code manage the Ansible deployment as well. But the idea is, Claude is my operator — it's not as much that it does anything that I couldn't have done with a script. It's just that scripts, once I leave my desk, I have to either expose something through the web in order to manage it remotely, or like with Claude, it's an entry point that I have access to securely from my phone and I can make it do whatever the hell I need it to do remotely.

01:13:00 - Patrick Chouinard
Actually, this weekend I had it build a dev server with four containers for four different projects, it updated and integrated into my production system. And it created an entire monitoring stack with Prometheus [tool:Prometheus], Grafana [tool:Grafana], Alert Manager [tool:Alert Manager] and connected it to my own personal Discord server [tool:Discord], so it can publish all of its alerts in Discord. And next week I want to be able to go through the response from Discord, so basically I have a button in the Discord message that says, oh, you found X problem on Y server — send that to the Claude instance running on that box, so it can resolve it.

01:14:00 - Ty Wells
Yeah, that's a great setup. I may have to borrow some of that from you.

01:14:26 - Morgan Cook
<Q>So on your Ubuntu server, or your virtual machine, you're just running a Claude CLI?</Q>

01:14:34 - Patrick Chouinard
<A>Yep. I run a Claude CLI, but I connect to it through Tmux, so I can disconnect while leaving the CLI open. And inside of it, I just start `/remote-control`. So then it shows on my Claude mobile app as a session I can connect to.</A>

01:15:27 - Patrick Chouinard
▶ That way, I can have 16 of them running at the same time, which is not supposed to work with Claude Code, but works perfectly well. And from the mobile client, it doesn't care where the session is.

01:16:00 - Patrick Chouinard
What they told me is you have to use your Max account only with Claude Code and you can remote connect to only one Claude Code instance per machine. It's exactly what I'm doing. It's just that I have it on 16 machines at a time.

01:16:34 - Juan Torres
You know, I bet there's a lot of hunger for this kind of information in terms of being able to create just context engineering for DevOps work, just like you just displayed, Patrick. I've seen a lot of really smart programmers, but not a lot of people are talking about this.

01:17:13 - Patrick Chouinard
All of that comes from the fact that they've published Remote Control. And when I saw the limitation, I had to find a way to go around it without bypassing it. So I need to build multiple machines. I don't have the time to build multiple machines. Claude can build multiple machines. And there we go.

---

<!--SEGMENT
topic: Ryan's Social Platform Video Streaming and Meta Glasses Lead Gen
speakers: Ryan C, Patrick Chouinard, Tom Welsh
keywords: Cloudflare Stream, R2 bucket, 4K video, adaptive bitrate, FFmpeg, Meta glasses, mobile app, SaaS, lead generation, cold calling, image compression, internet speed detection, Claude Code
summary: Ryan describes two active projects: (1) implementing adaptive video streaming on his social platform using Cloudflare Stream to handle clients with poor internet connections, with Patrick suggesting FFmpeg as a CLI-based alternative; and (2) a new SaaS concept using Meta glasses to photograph trade vans while driving, trigger AI-powered company research, and auto-generate outreach emails — which has evolved into a full mobile app and Meta glasses application.
-->

00:47:48 - Ryan C
God, I've got so much going on. I'm driving to Amsterdam tomorrow for five days with the family. So I'm literally just trying to do about a million things at once to get some stuff finished off. My main thing that I'm trying to accomplish right now is that I'm finding on my social platform that I showed a couple of months ago — it's now operational, has clients on it — clients with a bad internet connection are struggling to stream the videos because they're all uploaded in 4K. So it turns out that having different quality selectors is a lot more complicated than it looks. So I'm using all my stuff stored in the R2 bucket [tool:Cloudflare R2] on Cloudflare, so I'm using Cloudflare Stream [tool:Cloudflare Stream] to do the various versions of it — you pay about $5 a month, I think it is, for a thousand minutes of streaming of all the different resolutions, which should be fine for what I want it to do. So I'm in the middle of just implementing that into the platform so that they have a toggle to be able to bring it down, and it should auto-detect their internet speed and put it at the resolution that is suitable for their internet.

00:49:10 - Ryan C
And then I was doing some driving at the weekend. And because I like to occasionally just make a simple website for like a builder or somebody — super simple HTML, CSS, something that's quite nice. Because I can charge them one and a half, two thousand pounds for that. Which is about two thousand seven hundred dollars. And then obviously get monthly recurring income for maintenance and servicing. So I was thinking, how do I collect these leads? And I thought, when driving — and in the UK, it's illegal to use your phone while you're driving — so I thought, oh, Meta glasses [tool:Meta glasses], they'd be quite cool. And you can take a picture with a voice command, right? So, hey Meta, take a picture. So I was thinking, okay, I'm driving along, I see a van in front of me. I can just say, hey Meta, take a picture. How do I get that to ingest into an app, send it off to AI, get it to do a bunch of research on the company, find out who the directors are, write me a reach-out email, and potentially even send it? Then I thought, okay, well, people who cold-call people might want that. Then they want a mobile app to accompany that, to take pictures with their phones and stuff. So now I've created a whole SaaS, and I've spent quite a lot of time talking back and forth with Claude, making a big old plan for it. So I'm now going to build my first mobile application, and an application for the Meta glasses.

00:51:28 - Patrick Chouinard
<Q>Actually, for your video thing that you talked about, have you looked into maybe using FFmpeg [tool:FFmpeg] with Claude Code? Because Claude is awesome at creating scripts for FFmpeg that would do all that changing of resolution automatically for you.</Q>

00:51:46 - Ryan C
<A>That's a great shout. I'll have a little look. I may be slightly too far in with what I've already started doing. If so, if I can't get that to work, I'm going to take that link out of the chat right now and bookmark it.</A>

00:52:00 - Patrick Chouinard
▶ Yeah, it's a CLI tool, so Claude is really great at creating scripts, and once they're done, it can resize, reformat. It's basically what's behind every single Premiere and all of the video management tools. They all are basically big wrappers on top of FFmpeg.

00:53:16 - Ryan C
Yeah, I'll definitely look into that if I can't make this thing work.

00:53:19 - Tom Welsh
<Q>Do you ever use the developer tools in Chrome to slow your network connection down?</Q>

00:53:25 - Ryan C
<A>Yes, but it doesn't quite do the same thing, I've found. So I've literally resorted — because I know one of my client shops where I do the screen software has a crap internet connection — I've literally gone into her shop multiple times to do tests of it to make sure it actually works on a bad internet connection, because it's not just slowing it down. There's an increased ping, and server lag, and all that kind of stuff that you get on an authentic crap internet connection, versus one where you just slow the download and upload speed down.</A>

---

<!--SEGMENT
topic: Agent Development Lifecycle and ShipKit for Training
speakers: Ana P, Patrick Chouinard, Ty Wells, Tom Welsh
keywords: AGLC, agent development lifecycle, SDLC, ShipKit, corporate training, Anthropic, Claude Code, markdown developers, software development lifecycle, agentic AI, context engineering
summary: Ana asks about resources for the Agent Development Lifecycle (AGLC) and whether ShipKit is worth purchasing as a training tool for someone leading AI at a corporation rather than building commercial products. Patrick argues the AGLC is essentially the SDLC applied to a new type of software, and recommends ShipKit as well-structured training that could be expensed as corporate training. Ty and Patrick note that at its core, AI development is still software development — they are now "markdown developers."
-->

00:54:58 - Ana P
One of the things that I'm having trouble finding is more information about the lifecycle for agent deployment. So for example, I started seeing some YouTube videos talking about something called the AGLC — so like the agent development lifecycle — and I do not know if there's any good resources to learn more about this. But my question specifically is also about ShipKit [tool:ShipKit]. I haven't actually purchased ShipKit, partially because of pricing reasons, but I also really think it might help me get that intuition from kind of like a software development end-to-end point of view for agent development. I wanted to learn from your experience — if you would indeed recommend someone to go through the tutorials on ShipKit, because I'm not going to be making projects that I'm going to sell like you guys do. I work for a corporation, but I'm leading the AI part of it, and I would like enough context to be able to lead properly.

00:56:23 - Patrick Chouinard
▶ Maybe you can check — there's some corporations that will buy training, and ShipKit is not only a bunch of samples, it is AI development training as well. So maybe you can take a look at that front if that's ever an option.

00:56:51 - Patrick Chouinard
Otherwise, honestly, agent development lifecycle — it's very... it's a marketing tactic. It's the software development lifecycle — it's just another type of software. The SDLC — there's not much to rearrange to make it into a quote-unquote agent development lifecycle. It's the same basic principle behind it.

00:57:14 - Ty Wells
Like my buddy always tells me, he doesn't like AI. He says, you're just writing software, aren't you? I'm like, yeah, basically it's software. That's the end of the day. It's still code, right?

00:57:28 - Patrick Chouinard
▶ Exactly. It's just that we're doing what I call — we're markdown developers now more than anything else. But other than that, other than the language, the principle is the same.

00:57:47 - Patrick Chouinard
▶ Well, you have an opportunity, because ShipKit is very well-structured. And I find that the way the SDLC is implemented within ShipKit when you go through the lessons, it teaches you. To migrate that to agent development would be a very little stretch. So maybe you can open the discussion at your company as training material, and then maybe they can finance it.

---

<!--SEGMENT
topic: Patrick's AI News Pipeline Commercialized
speakers: Patrick Chouinard, Juan Torres, Morgan Cook
keywords: intel.patchutech.com, AI news pipeline, Cloudflare, Postgres, Debian, Alpine, NGINX, Docker, Claude Code, refactoring, LinkedIn, consulting, personal projects, side projects
summary: Patrick shares that his personal AI news aggregation site (intel.patchutech.com) — originally built for himself with no commercial intent — was noticed by his boss on LinkedIn and is now being implemented for a client. Claude Code refactored the entire project from a Cloudflare/Debian/Postgres stack to a client-compatible NGINX/Alpine stack in about 30 minutes on the first attempt. Morgan reflects on the recurring pattern that personal side projects are often the ones that generate real commercial interest.
-->

01:21:08 - Patrick Chouinard
On my part, the only other thing I wanted to talk about this week — behind all of the DevOps stuff I've been working on and having fun with — I don't know if you guys remember, I've talked about a site called intel.patchutech.com [link:intel.patchutech.com], which is my domain name. It's basically a pipeline that gathers information about AI news and manages it automatically. Well, I built that for myself. I had no intention to commercialize or do anything with it, but I ended up talking about it at work. And today, I actually imported it to my client site, and we were going to implement a version of it for them. So there are some talks, again, with my firm as well to monetize the whole thing — but yeah, it's just basically fell into me that my boss actually saw it because I put it on LinkedIn and he said, you know what, we want that.

01:22:26 - Patrick Chouinard
And the nice thing is this was something that was working on the machine I just showed you. Basically, it's a VM that runs a bunch of Docker containers, and it was on a Debian container running Postgres [tool:Postgres]. And the site deployed through Cloudflare. So the thing is, that didn't apply internally at my client. So I simply told — I cloned my project and told Claude that the infrastructure it would be deployed into at the client site. It took about half an hour to refactor the whole project to be deployable in the client infrastructure, to rip out the whole Cloudflare, create an NGINX [tool:NGINX] container to deploy the front end, then change my Debian machine to an Alpine machine, do the whole conversion — half an hour this morning. ▶ I was quite floored about the efficiency of Claude to migrate that project. And it worked first time — first shot, one prompt, gave me a bunch of URLs, clicked on them, all worked.

01:24:00 - Patrick Chouinard
Because like I said, to me, they're like my accountant and my lawyers, and I don't have to take care of the part that I hate. So basically, whatever margin they take on me, to me, it finances that part. So that's exactly what I did this morning. The client wants this — can you arrange whatever needs to be arranged to get that going? Like, yeah, sure, no problem. After 17 years, I have no qualm about giving that to them.

01:24:44 - Morgan Cook
It's funny, in my history — I've been programming since the 1980s. And the one thing I've found is that it was always those little personal side projects that took off. The stuff we were working on that was client-paid or whatever is always just a grind. But we do that little side thing for ourselves, and it's like, okay, that's the thing that everybody wants. ▶ So it's an important thing for all of us to pay attention to the problems we're trying to solve for our own workflow, our own processes — those are the ones that other people are also trying to solve. And so if you can solve a problem for yourself, somebody out there has that same problem, and it's a good one to push out.

01:26:13 - Patrick Chouinard
▶ That's exactly why I'm here every week. Not as much to have question and answer, but to learn about new use cases, because right now there's nothing more valuable than use cases that nobody has seen yet.

---

<!--SEGMENT
topic: Azure Privacy Perception and Tenant Architecture
speakers: Andrew Nanton, Patrick Chouinard, Ty Wells, Morgan Cook, Tom Welsh
keywords: Azure, OneDrive, Azure tenant, M365, Office 365, privacy, BAA, document processing, expert witnesses, Azure Document Intelligence, Azure Content Understanding, AZ CLI, blob storage, analogy, non-technical stakeholders
summary: Andrew describes a recurring challenge: clients who trust OneDrive/M365 for sensitive data refuse to use other Azure services in the same tenant, despite there being no meaningful technical difference. Patrick and Morgan offer analogy-based communication strategies — framing the Azure tenant as a walled home office with multiple entry points — to help non-technical stakeholders understand that security is equivalent. Andrew also asks about Azure Content Understanding as a successor to Azure Document Intelligence.
-->

01:27:47 - Andrew Nanton
Yeah, I just will throw this out there, hopefully for just a short discussion. One of the things that I keep running into as I continue to iterate on this idea for the document processing for expert witnesses is that privacy is obviously really paramount, and so at this point everything is based out of Azure [tool:Azure]. I will say, having found the documentation for the AZ command line tool [tool:AZ CLI] and getting LLMs to use that instead of trying to navigate Microsoft's horrible and impenetrable enterprise AI offerings has made a world of difference. ▶ So if you're ever looking at doing anything with Azure, install that first.

01:28:55 - Andrew Nanton
Anyway, so because privacy is so paramount — many of these organizations or groups will use and trust Office 365 [tool:Office 365] to manage sensitive data, they really get very reticent about stuff that is stored in any other part of Azure's cloud. And so one of the options that I've been evaluating recently is a situation where a user starts a project, that project's files are in a folder on OneDrive [tool:OneDrive], and then all of the background processing to convert PDFs, to summarize things, to find connections between documents — all of that happens in their back end, in their Azure instance. And I'm curious if anyone has considered or approached this — am I just thinking about this in the wrong way?

01:30:31 - Patrick Chouinard
<Q>Well, from my side — Azure tenant, a tenant is a tenant. Whatever is within that tenant is under the same contractual limitation and contractual privacy that you have in your contract. There's no difference because if it sits in M365 or inside of an Azure function, it's the same thing. Technologically, it's the same thing. Contractually, it's the same. I would be curious to hear what is their argument.</Q>

01:31:08 - Andrew Nanton
<A>It's not a sound technical one. It's just a paranoia argument — they just are a lot more comfortable with, this is my OneDrive. I know OneDrive is secure. If I put files in my OneDrive, I feel okay about that. But if there's a web interface to the same Azure tenant, then — our organization will never go for that. It has to be within our Azure tenant.</A>

01:32:36 - Patrick Chouinard
▶ Yeah, actually, it's just a matter of explaining it with different visuals. If they don't have an IT department, no matter how much IT-specific detail you give them, it's going to go way over their head. Normally, when I face that type of situation, I try to visualize it in something that's good and easy to understand for them. For example — your Azure tenant is like your walled-in home office. Everything there is controlled by you, for you. It doesn't matter if it's in your desk, your M365, or if it's in the closet — as long as it's in your office, it's in your office and under your control.

01:34:25 - Morgan Cook
▶ Another simple, quick analogy with that same house concept is — look, you just have two different entry points. You have your main door, and you have your garage door, but they're both secured, and they both go to the same storage space. So you're just seeing it from two different points of view. It's like, I'm only used to going through the main door. And it's okay, well, that's fine. That's the main door. But there's also this other entry to the same content, which is still just as secure. You have the keys. Nothing's being shared to anybody else. So that's the perception and how you present it as an analogy.

01:36:09 - Andrew Nanton
Well, I guess if anyone has any specific input about Azure Content Understanding [tool:Azure Content Understanding] — I was using Azure Document Intelligence [tool:Azure Document Intelligence] and having good results with it, and it looks like Content Understanding is sort of the next iteration of that. If anyone has any experience, positive or negative, I'd be grateful for it.

01:36:44 - Patrick Chouinard
▶ Actually, another thing that I've started to do — ask Claude, or ask ChatGPT or any of the AI, like, explain that with as much analogy as possible, as if you were a complete non-tech worker. It's very good at creating analogies, even better than us, because sometimes we're so deep in the technology that there's a part we don't abstract because it's obvious for us, but it's not for them.

---

<!--SEGMENT
topic: Teaching AI to Non-Technical Users and Obsidian as Second Brain
speakers: Elijah Stambaugh, Patrick Chouinard, Morgan Cook, Andrew Nanton, Elena
keywords: Obsidian, Notion, Supabase, Claude Code, second brain, Markdown, Git, GitHub sync, terminal plugin, vector store, Kanban, context window, ShipKit, SDLC, teaching AI, prompting, full-context conversation, younger generation, ego as currency, NLP
summary: Elijah asks how to teach AI effectively to high school and college-age students, prompting a rich discussion about why older users often adapt to AI prompting faster — they are trained in full-context conversation, unlike younger users accustomed to short search queries. Patrick and Morgan recommend having students explain projects to each other first, then type that explanation directly into Claude. The session closes with an extended discussion on personal knowledge management: Patrick advocates for Obsidian with a terminal plugin running Claude Code inside the vault, synced via GitHub, as a lightweight, Markdown-native alternative to Notion or Supabase for a second brain.
-->

01:43:41 - Elijah Stambaugh
So, just thinking about how we're going to train and transfer folks. Is there some basic — there's things that people should know more so than, because it feels like once you start going down a rabbit hole, it just goes so fast. You know, I work in the education space, and I'm even thinking about high school students, or possibly into that 20-year-old timeframe. Every time I'm working on stuff, it's just so much, so many different parts to it, that it's hard to just give them the basics. I went into a class the other day, and I showed some of the kids how to use AI for a project, because the teacher asked me to come in. And next thing you know, like a half hour later, her jaw's on the floor. I only had the first phase of five phases, and it literally built out the entire thing. She was like, how did you even know what I wanted the kids to do? This was supposed to be weeks of work, and I did it in 20 minutes right in front of them in class.

01:45:31 - Patrick Chouinard
▶ I always try to get people that are starting fresh, that have never interacted with AI or very, very little, or used it as a surrogate for Google — what I try to tell them is interact with it as a collaborator. Politeness is technical, okay? This is not about the AI having feelings. It has everything to do with the fact that when you collaborate with someone, you tend to express the context clearly. You tend to express goals, express constraints clearly, express output clearly. All of that — that is the AI interaction goal.

01:47:00 - Morgan Cook
In reality, it just means that whatever you're telling them, the way you're telling them is in vector space closer to a high-quality answer. But they're not going to understand that part. So that's why I say interact with it. And that's why I've seen that a lot of older people that I train tend to start very quickly to be efficient with AI. Where younger people tend to have a little bit more difficulty starting. ▶ Older generation tends to do better for one simple reason — they've been trained to have full-context discussions with other human beings, not querying Google.

01:48:08 - Morgan Cook
▶ Along those lines, Elijah, for a classroom setting, the way I would set that up to teach it is to actually do an exercise where you have a couple of students, where one student is explaining to the other student what the project is. And whatever he says to the other student — however he explains it — is exactly how they should be typing it into Claude. The problem that Patrick is pointing out is the fact that these guys are used to doing texting — quick questions, short statements. There's no conversation. There's no explaining. So if you can get them to practice the skill of explaining how to do something or what all the details are that need to be in the project, that's where the gold of Claude is.

01:49:48 - Patrick Chouinard
▶ And that's the irony of all of this. The generation that were born talking with computers are now at a disadvantage talking with computers, because computers have actually upgraded and started talking like a human being.

01:51:10 - Patrick Chouinard
For example, my nephew just came to me and says, hey Patrick, I need to do my CV for my first summer job this summer. Can you give me a hand? No — I'm going to show you how to ask Claude how to take whatever you have as a starting point from a CV and help you improve it. Because first, it's going to do a far better job than me. Second, it's going to explain what it did. So you're going to understand what it changed and why it changed it. So you're going to learn how to do a better CV while getting a better CV. ▶ It's not something like doing his work for him — it's something that automated a task that he didn't know how to do properly, and it's something that it would serve no purpose to make him an expert into.

01:52:53 - Elijah Stambaugh
I've been using Notion [tool:Notion] for a while. Notion AI is getting better. I was on the verge of building out my own kind of Notion just for my own sake because I put so much of my brain in there — it's just my second brain. But then I see some folks talking about Obsidian [tool:Obsidian] Markdown, but then some people are talking about you should have a Supabase [tool:Supabase] database so you can vector information as well as store all the different files. So I wanted to get your guys' take on — strategically, what does the infrastructure look like for us moving forward to document our activity so that AI has the context to help us in all of our activity?

01:54:28 - Patrick Chouinard
▶ Honestly, for that one, I'll quote what ChatGPT tells me every day: stop trying to build a cathedral when the only thing you need is your summer house. You don't need a full Supabase backend to do that. Take a look at Obsidian, but use the terminal plugin to run Claude Code inside of it. Then you have full Claude Code automation within a basically Markdown store, and Claude will navigate, crawl, search, do everything it needs. You don't need a vector store. It will do all of the inference, all of the connectivity, all of the extraction of insight from within the Obsidian store. And you can also have an extension for Git, so you can publish that Obsidian vault as a Git repo on GitHub. So it's synchronized for free. It's automatically being pushed and pulled, so it's exactly as if it was a code project. And with Claude in the terminal plugin — absolutely insane.

01:56:51 - Morgan Cook
And now that Anthropic has announced today voice for Claude Code — it's just starting to be deployed to a couple of people, but it's coming — meaning you're going to be able to chat with your notes, basically, through Claude Code in Obsidian.

02:00:00 - Patrick Chouinard
▶ Just like when you run Claude from within a project folder, you have a specific project that you're working on, and you start Claude in there — that's all Claude really has access to. When you run it from within Obsidian, you start a terminal, just like you would do in VS Code, you start a terminal. And then from within that terminal, you type in `claude`, and it would start a Claude session that is relative to your vault for Obsidian. When we're talking about a vault for Obsidian, that is a very specific folder structure that is limited to what Obsidian can see. So it's not your entire hard drive — it's just the content in your notes.

02:02:00 - Andrew Nanton
I put some links in the chat for two recently released Obsidian tools. One of which lets you interact with the Obsidian application from the command line, and another one that just syncs your vault in a headless way without running the application. And so in the OpenClaw that I'm running, I set up the headless sync because it's just on a VM somewhere and I don't need to run the whole Obsidian application.

02:04:10 - Patrick Chouinard
▶ Remember that one of the biggest concepts of second brain is to reduce the friction of getting your notes in and accessing and consuming your notes. And so if you're going to put a Supabase in place that's accessible from usually one place, that means now you're limiting how easily it is to connect to all of your notes and see it from your phone or your desktop or whatever, without writing a full application to do something like that. So it's just a matter of keeping the friction as low as possible with all of that content.

02:05:21 - Patrick Chouinard
▶ I've tried to stay away from dashboards a little bit more because there's so much information we need to concentrate — when you try to summarize it into a dashboard, you tend to start missing some pieces because you have to cut, you can't put everything into a dashboard, and you always end up cutting the piece that would be useful at the time you're looking at it. So now I leave Claude Code — whatever I want to know, if I want to know where I'm standing, where is the task, what's my next task, have I forgotten to work on anything — I'll ask Claude Code. It has access to all the data, so it figures it out and it brings it just in time, just the information I need.

02:07:12 - Patrick Chouinard
▶ And since there's MCP for both Notion and Obsidian, guess what? Claude Code is a very good tool to migrate from one to the other.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block (which was not provided to this session — the template variable `{{ $('HTTP Request: Get Speaker Aliases').item.json.data }}` resolved to empty/null):

- **Ty Wells** — passed through unchanged
- **Marc Juretus** — passed through unchanged
- **Ana P** — passed through unchanged
- **Patrick Chouinard** — passed through unchanged
- **Ryan C** — passed through unchanged
- **Morgan Cook** — passed through unchanged
- **Tom Welsh** — passed through unchanged
- **Juan Torres** — passed through unchanged
- **Elena** — passed through unchanged
- **Andrew Nanton** — passed through unchanged
- **Elijah Stambaugh** — passed through unchanged

*Note: Because the SPEAKER_ALIASES map was not populated (the n8n expression did not resolve), all speaker names have been passed through as-is from the raw transcript. If canonical aliases exist, re-run normalization with the alias map populated.*