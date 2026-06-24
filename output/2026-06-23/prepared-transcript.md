=== SESSION ===
date: Unknown (transcript references "tomorrow" as Saint-Jean-Baptiste Day, June 24, suggesting session date ~June 23)
duration_estimate: ~90 minutes
main_themes: Personal AI use for bereavement administration, Claude Code agentic loops for infrastructure refactoring, AI-powered video production pipeline, Hermes agent framework with Workspace UI, intent queue / voice-to-code workflow, Proxmox home lab infrastructure, local LLM hardware constraints, model benchmarking discussion

---

<!--SEGMENT
topic: Session Open & Personal Context
speakers: Patrick Chouinard, Scott Rippey, Ty Wells, Juan Torres, Ryan C
keywords: Saint-Jean-Baptiste, Quebec, Focusrite, Brandon, bereavement, session attendance, fireworks, French colonialism, Catholic heritage
summary: The group opens with audio troubleshooting, attendance check, and light social conversation about Quebec's Saint-Jean-Baptiste national holiday and its Catholic roots. Patrick signals he has been personally distracted due to a family bereavement, setting context for his later update.
-->

[00:03:36] Patrick Chouinard: Hey, Scott.
[00:03:39] Scott Rippey: Oh, here we go.
[00:03:51] Scott Rippey: Hold on. Change my audio.
[00:03:58] Scott Rippey: There we go.
[00:04:02] Scott Rippey: It's like, my Focusrite [tool:Focusrite], I got one of those little Focusrite things because I got XLRs in, but it's been acting up lately where I got to keep unplugging it and plugging it in, the USB, because it's like... the sound isn't coming on.
[00:04:17] Scott Rippey: So nothing from Brandon, huh?
[00:04:19] Patrick Chouinard: No, actually, I should probably have texted him, but let's just say that the last couple of weeks were a bit more busy than usual.
[00:04:38] Scott Rippey: I got a couple of things I'm saving for when he's on just because I want his opinion on it too, but I do have something I'll kind of show today — a reminder about something I showed before with a repo that some people might want a reminder on. I've got more of an example now.
[00:05:00] Ty Wells: Hey guys, what's going on?
[00:05:04] Patrick Chouinard: No golf today?
[00:05:07] Ty Wells: Actually, I golfed this morning. I'm exhausted. I had to come home and take a nap.
[00:06:00] Juan Torres: He did not get invited to his own group.
[00:06:41] Patrick Chouinard: When you train someone to wait for you to call, then you don't, you stop checking. I've been doing it for the last couple of months.
[00:07:09] Patrick Chouinard: By the way, if you hear some fireworks in the background, it's just because it's going to be the festivity. It's the national holiday tomorrow here in Quebec.
[00:07:24] Juan Torres: Independence?
[00:07:28] Patrick Chouinard: Quebec is just — we call it Saint-Jean-Baptiste. It's based on John the Baptist as the patron saint of Quebec.
[00:07:40] Juan Torres: Quebec has a really, really religious background if you go back a couple of decades.
[00:07:46] Patrick Chouinard: Pretty much all of our festivities are religious-based.
[00:07:50] Juan Torres: Catholic?
[00:07:52] Patrick Chouinard: Yeah. All of our cities are named after saints. Part of our streets are named after saints, but there's nobody in any church, so it's kind of weird.
[00:08:14] Juan Torres: The residues of French colonialism.
[00:08:23] Ryan C: You wouldn't see the British doing that. We were pretty quiet.
[00:08:31] Patrick Chouinard: There's a couple of battles that say otherwise here in Quebec.
[00:08:36] Ryan C: Oh, we just forget about those.

---

<!--SEGMENT
topic: Claude for Bereavement Administration
speakers: Patrick Chouinard, Juan Torres
keywords: Claude, bereavement, eulogy, administrative tasks, forms, emails, AI efficiency, funeral process, A/B testing, personal productivity
summary: Patrick shares how he used Claude to manage nearly all administrative tasks following his mother's passing — forms, submissions, and emails — completing in 48 hours what took two months when his father died ten years earlier. This segment highlights a deeply personal and unexpected high-value use case for AI assistance.
-->

[00:08:54] Patrick Chouinard: Maybe I'm going to give you a little bit of a heads up of what I've been working on. Obviously, I've been working on a lot of stuff not AI-related, but basically — for those who weren't there last week — I lost my mom three weeks ago, so I ended up having to do a whole lot of administrative work. Weirdly enough, Claude [tool:Claude] has been extremely helpful, and I realized that I could leverage it to take a lot off my plate. It basically managed the entire funeral process.
[00:09:39] Patrick Chouinard: Everything that was emotional — all the writing for the eulogy, all of that I took care of — but everything that was forms, submissions, emails, personal calls, all of that Claude handled like a hundred percent of it.
[00:10:00] Patrick Chouinard: We almost did A/B testing, because I'd done this for my dad ten years ago — took me about two months to go through everything that needed to happen. For my mom, it took 48 hours because it was assisted. So weird place to leverage AI, but it was actually extremely helpful.
[00:10:31] Patrick Chouinard: It reminded me of a lot of things I would have completely forgotten and that would have been quite catastrophic if I did forget, and took care of them. It actually looked at the material I made for my dad ten years ago — I still had it on my computer — found the material, reused it, and gave me ideas to build the same thing for my mom.
[00:11:00] Juan Torres: Yeah, it's samples.
[00:11:07] Patrick Chouinard: ▶ We can say anything we want about the fact that it's just a tool, but sometimes it's a tool that can surprise you in its efficiency, even in the extremely hard realm of personal loss.

---

<!--SEGMENT
topic: Agent Ops & Claude Code Loop Refactoring
speakers: Patrick Chouinard, Ty Wells
keywords: Agent Ops, Hermes, Claude Code, slash loop, codex validator, MCP server, home lab, token usage, human-in-the-loop, agentic iteration, infrastructure as code
summary: Patrick describes refactoring multiple disconnected projects — Agent Ops, an operator harness for Hermes, and an MCP server — into a single well-structured repository using Claude Code's /loop command combined with a codex validator inner loop. The 48-hour human-validated run produced a fully documented AI infrastructure toolbox, demonstrating nested agentic loops with quality gates.
-->

[00:11:28] Patrick Chouinard: Do you remember I told you I was building something I called Agent Ops, which was basically an operator harness for Hermes [tool:Hermes] to manage my home lab? Well, I realized it was growing a little bit all over the place — I need to add this functionality, I'm going to try to merge those two, I'm going to build an MCP server [tool:MCP server]. I ended up with a bunch of disconnected tools.
[00:12:07] Patrick Chouinard: I was looking for something to try the slash loop on. So what I did is I copied every single repo into a single directory root and launched loop to refactor every single subproject into one main project to tie into Hermes — basically a Hermes-type toolbox, but well-structured, well-architected, well-documented.
[00:12:40] Patrick Chouinard: It's been running for around 48 hours now, and the repo is getting impressively well-structured so far.
[00:13:10] Patrick Chouinard: I coupled that loop — I did two loops. I had the slash loop [tool:Claude Code /loop] with a goal it tries to achieve, but within that loop it was using the codex validator [tool:codex validator], the code review. So at every iteration of the loop, it called codex, which itself looped a bunch of times to correct all the mistakes it found, before Claude tried to do another iteration of loop.
[00:13:50] Ty Wells: <Q>How many tokens are you in at 48 hours?</Q>
[00:13:55] Patrick Chouinard: <A>It's not too bad because it's a human-validated loop, so basically at every iteration it asked me — so I'm probably the thing that slowed it down a little bit.</A>
[00:14:07] Ty Wells: Come on, you're getting in the way, Patrick. Let it ride. Put it all on black and go.
[00:14:17] Patrick Chouinard: Would love to do that, but — no, it asked some very good questions and there's something where I diverted from the way it was going, so it was very beneficial to be in the loop. Once it's at iteration 30 or something, it was going in ways I would not have thought about. But once I read what it did, it made a whole lot of sense.
[00:14:43] Patrick Chouinard: ▶ Now I have a fully documented AI infrastructure, but with a toolbox on top of it for my agent to continue taking care of it and making it evolve in the future. It's not just a plug-in — it's really a full harness on top of Hermes.

---

<!--SEGMENT
topic: AI Video Production Pipeline & YouTube Channel Launch
speakers: Scott Rippey, Juan Torres, Ty Wells, Patrick Chouinard
keywords: Higgsfield, Eleven Labs, HeyGen, Kling, Nano Banana, Remotion, FFmpeg, Claude Code, MCP, B-roll, avatar, voice clone, Pixar style, Building With Reason, YouTube channel
summary: Scott demonstrates his AI-powered video production pipeline used to launch a new YouTube channel called "Building With Reason," featuring a Pixar-style avatar. The pipeline integrates Claude Code with Higgsfield, Nano Banana for images, Kling for animation, Eleven Labs V3 for voice cloning, HeyGen for avatar lip-sync, Remotion for assembly, and FFmpeg for audio leveling — all orchestrated through MCP and CLI tools with a gate-check loop for quality control.
-->

[00:15:37] Patrick Chouinard: Scott, what did you have for us this week?
[00:15:40] Scott Rippey: I'm going to show this one tonight, but I'll probably show it again when we get a larger group. Do you remember that video repo I did? The video generator?
[00:15:54] Juan Torres: Yeah.
[00:15:55] Scott Rippey: That kind of combines a lot of different tools like Higgsfield [tool:Higgsfield] and Eleven Labs [tool:Eleven Labs]. But using some local stuff like FFmpeg [tool:FFmpeg], Remotion [tool:Remotion] — I actually added in HeyGen [tool:HeyGen] as well because I had a different pipeline for doing that for a customer. I ended up launching a YouTube channel today that is AI-based, but it's taught by my avatar, and it's all Pixar style.
[00:16:30] Scott Rippey: I'm a film guy, right? I produce videos for people — that's what I used to do a lot of before I got into development. I thought this was kind of a cool thing because nobody — like some people are doing it, but not really in our space. I just wanted to do it as something fun. I took this repo because the thing about this repo is it kind of just ramps you up into hooking everything up, but then you can make it your own.
[00:17:00] Scott Rippey: It's using Nano Banana [tool:Nano Banana] for all my images that I'm popping up, and I'm creating all the SFX and the voice clone in Eleven Labs, and then HeyGen — you just literally upload the photo and it creates your avatar. Like, it's so easy.
[00:20:43] Juan Torres: <Q>Which model are you using for the generation of the images?</Q>
[00:20:54] Scott Rippey: <A>It's all Nano Banana through Higgsfield. When you're in Claude Code and you're telling it what you want, and then it writes the prompting — if you're very specific, it's so good at getting better and better images, and my characters are all consistent. I can literally have it regenerate something and everything stays the same, and then it'll change something else. It's all running through Claude Code [tool:Claude Code] into Higgsfield using the Nano Banana model for images — all the images are Nano for thumbnails, for characters, for the starting things before I animate them. I'll even create those in Nano first, and then it'll send it to Kling [tool:Kling] to animate.</A>
[00:22:22] Juan Torres: <Q>So do you create the images, and then for the dialogue, animate them in that coordination?</Q>
[00:22:31] Scott Rippey: <A>So the dialogue part is super easy. I write the script, and then when the script is ready, I send that through — I have a quick clone in Eleven Labs. It's gotten so good. If you use the V3 engine now, it strips out all the break stuff. You send it the text, it has been 100% perfect in figuring out intonations and rounding sentences. I was using V2 with my old pro clone and it was saying stuff wrong. Quick clone now with the V3 engine and it just gets it.</A>
[00:23:10] Scott Rippey: Once that audio comes down, Claude Code then goes — once I agree, it's like, yep, that's good — all it does is send that to HeyGen and it sends a background, because I make the backgrounds in Nano too. It can tell HeyGen to use this background and then cut out the avatar. All you do is upload a picture to HeyGen of your character for the avatar feature. And all of a sudden I have all these different avatars.
[00:25:17] Scott Rippey: <Q>How do you add the scenes where you see the explosion?</Q> — [answering Juan's question]
[00:25:25] Scott Rippey: <A>So I get my whole take back, and the intro and outro I already have built — Remotion puts those on the end for me. When I get back the avatar and the voice from HeyGen, I have no B-roll yet. It has the script. I examine the script, and I say, hey, I want to create an image in Nano Banana of like — I want this AI agent smacking into a stop sign — and then I need a screeching sound from Eleven Labs. It knows to do that. I plan out my scenes, and then what it does is cool: even though it comes back in 4K, as I'm working through this, it does quick things in 1080p and gives me a preview. I sign off on it and move on before it generates the entire video in 4K with all the overlays.</A>
[00:27:34] Juan Torres: <Q>So you're using Claude Code with a tool to identify portions of your script to then generate the B-roll?</Q>
[00:27:41] Scott Rippey: <A>I mean, it's not even a tool — I'm literally looking at it. When I was writing the "Just Loops" one, I've got the voiceover, and I just go through here and look, and I go, all right, when I say this, let's do this, and it starts working on it for me, and then it pops up a preview for me in QuickTime, and I just watch it and go yes or no. The tool is the whole repo together, because it has all of the tools Claude Code can call to do anything I need it to do — between the models to generate things, to Remotion to move things around, to FFmpeg to level audio.</A>
[00:28:43] Scott Rippey: ▶ I even added a loop to this now where there's a gate check before it does anything for me — it checks everything, because I was finding that every once in a while I'd have a glitch here and there. Now I've got a gate to get rid of common issues before I even see it.
[00:29:01] Juan Torres: <Q>So Claude Code has CLI access to Higgsfield, right?</Q>
[00:29:06] Scott Rippey: <A>MCP, CLI, depending on the tool. Most of them are MCP.</A>
[00:29:23] Scott Rippey: <Q>Which model are you using for the generation of the videos for your B-rolls?</Q> — [answering Juan]
[00:29:20] Scott Rippey: <A>That's Kling. Those animations are Kling. Higgsfield is just nice because it's a $50 plan where I have access to all these models. I'm primarily using Kling for animations and Nano for the reference image for the animations, as well as images I'm using in there.</A>
[00:29:39] Scott Rippey: ▶ It's just such a good pipeline. It knows the purpose of this thing. It knows the YouTube channel. It knows my voice. It knows the pipeline. And you can see I've got channel identity, voice for how I talk, a pipeline. So every time I open this thing, the Claude.md points to these things, and it just gets more and more streamlined the more I use it.
[00:31:42] Scott Rippey: I don't even think I've had this much fun in a while, and I'm finally doing a YouTube channel. I never thought I would be, but this is the way to do it for me.
[00:32:23] Patrick Chouinard: Talking about the YouTube channel you created — it reminded me of another channel. I don't know if you've heard about the channel Claudius Papyrus.
[00:32:35] Scott Rippey: I don't think I've ever seen it.
[00:33:07] Patrick Chouinard: Basically, he says he's not affiliated with Anthropic or Claude, but he's powered by it. So basically it's as if Claude was having a YouTube channel.
[00:33:27] Scott Rippey: Yeah, I love his interpretation of the Claude character. That's so funny.

---

<!--SEGMENT
topic: Code Quality & Security Review System Tease
speakers: Scott Rippey, Patrick Chouinard, Juan Torres
keywords: code review, security review, Codex, model agnostic, observability, reportability, git hooks, dashboard, multi-vendor, multi-model
summary: Scott briefly teases a forthcoming demo of a model-agnostic code quality and security review system he has built, featuring git push hooks, a settings database, a reporting dashboard, and multi-vendor/multi-model support including Codex. He defers the full demo until Brandon is present.
-->

[00:35:38] Scott Rippey: I'll show this again. I want to wait until Brandon's here only because I want him to see this. I have something that I built — it's an observable way of seeing security review, code review, two vendors, three models.
[00:35:59] Scott Rippey: Yes, Codex [tool:Codex] is in. It's all legal because it's all happening. I have a whole system of hooks for every time I push that's pulling settings from a database and a dashboard that also then reports.
[00:36:20] Scott Rippey: ▶ I got a really cool thing that I built — probably the best thing I think I've ever built for anybody — and this is what I'm going to keep using, and it's model agnostic. I got a cool system for code quality and security reviews, with observability and reportability. I can't wait to show that.

---

<!--SEGMENT
topic: AI Photo Booth & Proxmox Infrastructure Advice
speakers: Juan Torres, Patrick Chouinard, Ty Wells
keywords: AI photo booth, image-to-image, multi-model inference, Google Imagen Pro, dual boot, WSL, Proxmox, Ubuntu, Windows 11, TrueNAS, PBS, Proxmox Backup Server, LXC containers, NAS, Synology
summary: Juan updates on his AI photo booth event service — a real-time image transformation system for parties — and discusses hardware setup including a dual-boot Windows/Ubuntu machine. Patrick recommends Proxmox as a superior alternative to dual-booting, explaining VM portability, LXC containers, and the Proxmox Backup Server (PBS). Ty confirms he is already using Proxmox on Patrick's earlier recommendation.
-->

[00:36:46] Juan Torres: For me, what I have going on — I haven't had the AI booth application up into the field. What I'm trying to build is a service for parties and events where I deploy a couple of screens and cameras to transform, in real time, normal images taken with a camera into AI-generated images depending on styles.
[00:37:22] Juan Torres: Last week I had to do a lot of hardware setup, changing one computer from another. I got it from OfferUp, basically got rid of the current operating system, cleaned it up, reinstalled Windows 11 [tool:Windows 11], and I'm going to install Ubuntu to have a dual-boot system.
[00:38:12] Juan Torres: This week, what I think I'm going to do — just because there are some personal issues I have to resolve — is create a multi-model inference engine, in which I have several models to do image-to-image transformation, including Google Imagen Pro [tool:Google Imagen Pro] as one of them.
[00:38:40] Patrick Chouinard: <Q>Why do you install dual-boot Windows and Ubuntu instead of using WSL?</Q>
[00:38:55] Juan Torres: <A>Because even if you have WSL [tool:WSL], it's basically on top of Windows. The main purpose of creating a dual-boot system is to have an operating system that does not require Windows. Windows is too unreliable for me, plus all the processes.</A>
[00:39:38] Patrick Chouinard: ▶ Then maybe something else to take into consideration — using Proxmox [tool:Proxmox] and spawning those two as VMs. So then you don't have to dual-boot; you can just switch from one VM to the other. If you need as much power as possible, you shut one down, play in the other. Basically, they're both independent machines that eventually, if you get other hardware, you could just transfer away.
[00:40:36] Juan Torres: <Q>Okay, so how would that look if I wanted to — would I have to basically set it up in BIOS?</Q>
[00:40:45] Patrick Chouinard: <A>No, you just install Proxmox as the OS. It's a Linux distribution — light, because it's made to be a platform. Then you just start both machines, and you can even connect to it and see the machine within the web interface of Proxmox itself.</A>
[00:42:19] Patrick Chouinard: I installed the bare-bone Proxmox on a mini PC — a Ryzen 5 with 32 gigs of RAM — gave SSH rights to my workstation, and told Claude Code: here's the machine, go at it. It actually created the proper template, spawned all the machines, configured them, deployed Authentik [tool:Authentik], deployed Traefik [tool:Traefik], deployed all of the network services for me, configured them to work together. All infrastructure as code, all guided by Claude Code in the backend.
[00:43:21] Patrick Chouinard: ▶ The nice thing is Proxmox also supports its own type of container called LXC container [tool:LXC]. So you can have Docker containers inside your Linux VM, but you can also have native containers on Proxmox itself — even lighter than a full VM. You can have a bunch of them and keep some shut down, just bring them up whenever you need them. You basically build yourself a full library of services and spin them up whenever you need them.
[00:44:05] Patrick Chouinard: Another service I find very helpful with that is PBS — Proxmox Backup Server [tool:Proxmox Backup Server]. Heads-off, you just create the backup job. It runs in the background, takes snapshots of all your VMs. If anything happened, you can recover from one of those backups. You can set policies — seven days, four weeks, one year — exactly the setup you want, and it's built in.
[00:44:51] Patrick Chouinard: ▶ If you ever get a NAS, one thing nice is you install TrueNAS [tool:TrueNAS] on it and then spawn PBS as one of the VMs on TrueNAS, and it uses the local storage for backups.
[00:46:00] Patrick Chouinard: ▶ If you present storage from your NAS to Proxmox, the nice thing is the day you get a second node, they can then share the storage, meaning you can do live migration — a machine being migrated from one node to the other without ever shutting down. And Claude Code can do that for you.
[00:46:49] Patrick Chouinard: That's exactly the toolkit I'm trying to give Hermes. So when it receives a message from Alert Manager saying this machine's not working well because the host is out of RAM, it can start a live migration and push it to another host that has enough RAM available.

---

<!--SEGMENT
topic: Intent Queue & Voice-to-Code Workflow (CodeTalk)
speakers: Ty Wells, Scott Rippey, Juan Torres, Patrick Chouinard
keywords: intent queue, context window, Claude Code, ChatGPT voice, PRD, PipeCat, CodeTalk, voice agent, local models, Proxmox, repository conversation, agentic workflow, hooks
summary: Ty presents his "intent queue" system — a mechanism that captures development intent as micro-language capsules when context is below 40%, queues them, and replays them at the start of fresh Claude Code sessions via hooks. He then describes a conceptual "CodeTalk" project for voice-based conversational interaction with a codebase (using PipeCat and local models on Proxmox) to generate intent capsules while mobile. Scott expresses strong interest and shares a complementary Claude PRD-generation project.
-->

[00:47:17] Ty Wells: I posted something in the community last week after the call for the intent queue. The gist is — when the context is primed, I want to take advantage of that context using the "by the way" command to capture the intent for the next feature or whatever.
[00:47:54] Ty Wells: I went a step further. There's a doc out there for it that you can bring into your repo. Basically it captures intent at the time when the context is under 40%, and then you could use that to build a queue. Those intent capsules go into a queue, and when you start cold in your next Claude session, the first thing that happens is it shows you the queue on a hook. It shows you what's in the queue, and it will — it's a terse micro-language that will then be able to run that intent, whatever that was, without losing a beat.
[00:48:29] Ty Wells: ▶ I've been running that like crazy. That's all I do now. I just grab it while the iron's hot, queue that up, and start a fresh session. The only thing I want now is to have that auto-run, because really the only thing I'm doing is clearing the session — the queue is starting, just run the queue, and I'm saying, yeah, go ahead. So it's a lot of manual interaction. That's a work in progress.
[00:49:20] Ty Wells: The other one — when I'm driving, I often use ChatGPT [tool:ChatGPT] just to hash out ideas, do a memory dump, go back and forth. At the end I generate a PRD out of it, and then I actually take the PRD, dump it into the intent queue, it builds the queue, the capsules, and then let it run.
[00:50:00] Ty Wells: But what I want to do is talk to my code in the same way. Let's say I'm driving or I'm on the golf course. I don't want to have to chat like a remote control session. I want to get in a conversation about the code — just about the code, not to change anything, not to fix anything. So I'm working on this thing called CodeTalk [tool:CodeTalk] — basically a conversational interface with your repository, through conversation rather than chat — and then create intent capsules and queue them up.
[00:51:23] Scott Rippey: No, but now I'm going to go build it, because I like that idea.
[00:51:34] Scott Rippey: All this really is at the root of it — it's literally just building an AI voice agent that is trained in principles and how you like to code. If it has the ethos of everything it should have, and then it has access to everything, you can just have these conversations and it can riff on looking at your code and analyze. ▶ It's not like it has to do any work. It just needs to know the ethos of how it's going to examine the code. If you build that right, then that's not a hard thing to do at all.
[00:52:22] Ty Wells: My Proxmox where I'm running my local models — I'm using those to communicate with my repo because you want to be careful about exposing private repos to other models. I'll clone the repo down, talk to it, check this feature, whatever I need to communicate with that repo — and then potentially queue things up. But I want to do that through voice. It makes me a little more mobile.
[00:53:29] Ty Wells: Yeah, I'm using PipeCat [tool:PipeCat]. I've got it — they're probably going to be there by the end of the day.
[00:54:33] Ty Wells: CodeTalk. That's the name I've got.
[00:54:37] Scott Rippey: Oh yeah, no — I'll just keep it internal anyway. I'll call it something dumb.
[00:55:27] Scott Rippey: Before I forget, Ty — email me because I have something you might like. I have a Claude project that I use for creating PRDs. My whole thing is I love to have chats and formulate ideas, and I usually do it with Claude in the car. I have a whole project architecture built very strongly for creating PRDs. And then when I have that, I go into Claude Code and have it break out and build phases and keep going. ▶ You might want to check that out because it's easy to just make a little project and try shoving your next idea through it.

---

<!--SEGMENT
topic: Hermes Workspace UI Deep Dive
speakers: Patrick Chouinard, Scott Rippey, Ty Wells, Juan Torres
keywords: Hermes, Hermes Workspace, OpenWebUI, Authentik, Traefik, Tailscale, SSO, Infisical, secret management, OLAMA, LM Studio, MLX, GGUF, agent swarm, Conductor, Kanban, memory management, profiles, IronClaw, OpenClaw, Postgres
summary: Patrick demonstrates the Hermes Workspace UI — an open-source web interface layered on top of the Hermes agent framework — showing features including a Kanban task board, Conductor agent swarm visualizer, memory management, cron scheduling, multi-profile/identity support, and MCP integration. He describes his full self-hosted stack: Proxmox VMs, Traefik reverse proxy, Authentik SSO, Tailscale VPN, Infisical secret vault, and internal TLS — replacing Discord, Telegram, and OpenWebUI entirely.
-->

[00:55:33] Patrick Chouinard: Honestly, I've stopped using Telegram and Discord now for a couple of weeks, since I've installed Hermes Workspace [tool:Hermes Workspace].
[00:55:37] Ty Wells: Tell us more. What have we got here? Show us some stuff.
[00:55:40] Scott Rippey: Patrick, are you saying I should pivot a little bit into integrating that into my IronClaw [tool:IronClaw] setup instead of Discord?
[00:55:49] Patrick Chouinard: Yeah, it could actually, because it's a public repo. Let me show you what it looks like.
[00:57:03] Patrick Chouinard: So, yep, this is Hermes through the Hermes Workspace interface. As you can see, I only have one model connected, but if I wanted, you can manage effort, switch the model, do attachments, do voice dictation. Although internally I still use Whisperflow [tool:Whisperflow], but it does support it. You can search through past chats. You have a dashboard that tracks all of your usage, chat, your files.
[00:57:59] Juan Torres: <Q>Wait — is this something you created or is this from the workspace?</Q>
[00:58:00] Patrick Chouinard: <A>That's the Hermes Workspace project I sent the link to. It's just installed on top of Hermes. It really makes all the difference in the world.</A>
[00:58:09] Scott Rippey: Yeah, it's nice because I was manually creating dashboard stuff over IronClaw and deploying it myself.
[00:58:18] Patrick Chouinard: Yeah, this is out of the box. You can see all the cron jobs it's scheduled for itself — you can look at, edit, play.
[00:58:30] Scott Rippey: Has a Kanban board for tasks.
[00:58:33] Patrick Chouinard: ▶ So you just drop a task and it will automatically start moving it through the Kanban board.
[00:58:47] Juan Torres: <Q>What is Conductor supposed to do?</Q>
[00:58:48] Patrick Chouinard: <A>Conductor is basically its implementation of agent swarm. Whatever task you give it, it will spawn an agent swarm to take care of it. And it shows you visually the little agents working.</A>
[01:00:10] Patrick Chouinard: You caught me mid-migration, actually. I'm putting Authentik in front of it and it hasn't completed the migration yet. The web service can be HTTPS internally because I'm using an internal CA to authenticate it. And I can even front it with an OpenID — like Authentik [tool:Authentik]. So it has centralized SSO on my internal network through Authentik.
[01:01:03] Patrick Chouinard: You have Conductor, which is a little bit like — you just drop an idea and it will churn through it for a long time. You have a full dashboard, you have memories.
[01:01:10] Scott Rippey: <Q>How does Hermes do with the identity of itself — can you set the identity of itself and yourself, similar to in the Claude system prompt?</Q>
[01:01:17] Patrick Chouinard: <A>You can do more than that. You can set up multiple identities for Hermes and interact with whichever one you want, or use them as a swarm.</A>
[01:01:30] Patrick Chouinard: ▶ It doesn't have a public skill repo. It bases everything on the skills that come with the workspace, plus its skill builder. So basically: don't download skills, build them.
[01:01:47] Patrick Chouinard: From a security point of view, honestly, to me, far superior. Even out of the box it has a well-structured ENV file, and it's ready to wire into secret management. Internally I used Infisical [tool:Infisical] for secret management — a vault — and it plugged in directly to Hermes. So now Hermes is feeding its secrets directly from Infisical. No API key on disk, no login, no nothing. All the secrets are in the vault.
[01:04:23] Patrick Chouinard: ▶ Hermes can leverage either OLAMA [tool:OLAMA] or LM Studio [tool:LM Studio], which means your inference doesn't have to run locally on the same machine as Hermes. So your Mac could still be your inference box, just serving them all through OLAMA.
[01:05:00] Scott Rippey: OLAMA does not run MLX [tool:MLX], though. OLAMA only runs the GGUF [tool:GGUF] stuff. But LM Studio does run MLX.
[01:05:09] Patrick Chouinard: So it does both, then.
[01:05:15] Scott Rippey: You've piqued my interest enough — I'm going to have to take a hard look at it.
[01:05:22] Patrick Chouinard: By the way, what I've shown you — the Hermes Workspace — this is just a project that goes on top of Hermes. It's not Hermes itself. It's basically a UI++ on top of Hermes. And that's why now I don't use OpenClaw [tool:OpenClaw] anymore, and I don't use Discord or anything like that, because now it has its full web UI. I just connect through Tailscale [tool:Tailscale], and I have the local web client on my phone.
[01:06:10] Patrick Chouinard: ▶ I do Tailscale to a Traefik reverse proxy that implements my local certificate that has been copied to my phone, and it does the authentication through Authentik. So it's a full SSO encrypted path through a native web interface on mobile, running completely inside my internal infrastructure off a couple of mini PCs I bought off Amazon.
[01:06:40] Juan Torres: Tailscale is such an underrated tool.
[01:07:00] Patrick Chouinard: Use Traefik. Use an internal reverse proxy because that's my only target internally. The only ingress in my whole network is the reverse proxy. It does the routing to whichever machine I need internally afterward.
[01:07:19] Juan Torres: <Q>Don't quite get it.</Q>
[01:07:19] Patrick Chouinard: <A>A reverse proxy — it's one machine that every single request goes through. Since I come in with, let's say, hermes.patchotech.lab, which is my internal domain, the reverse proxy takes that and says, oh, that address is mapped to machine123, so I'm going to redirect that to machine123. The point of entry is always the reverse proxy.</A>
[01:08:00] Juan Torres: So it's like a bastion server?
[01:08:01] Patrick Chouinard: Yeah, if you want. ▶ From a Tailscale point of view, you're only ever hitting a single machine. And you hit it with a fully qualified domain name that is only viable once you're connected through Tailscale. No cloud computing required. It's basically a private cloud built internally on very little hardware.
[01:09:04] Patrick Chouinard: That way — no more Telegram, no more Discord, no more anything. Just direct connectivity of the full power of Hermes.

---

<!--SEGMENT
topic: Ryan's Store Backend & Claude 4 Fable Discussion
speakers: Ryan C, Scott Rippey, Patrick Chouinard, Juan Torres, Ty Wells
keywords: Resend, Recounts, CRM, estate agents, slash goal, smoke test, rubric check, Claude 4 Fable, Sonnet 5, Opus 4, GLM, DeepSeek, benchmarks, token cost, agentic scaffolding
summary: Ryan describes a deadline crunch building a store backend with Resend and Recounts, plus a V4 sweep of a real estate CRM using /goal with rubric checks. Scott recounts his intensive experience with Claude 4 Fable before it was pulled — running 50+ parallel agents for scaffolding with impressive quality results but high token burn. The group briefly discusses upcoming Sonnet 5, GLM models, DeepSeek, and the reliability of AI benchmarks.
-->

[00:10:10] Patrick Chouinard: Ryan, anything to showcase from the darkness of your office?
[00:10:33] Ryan C: I'm literally just building out an entire back end of a store where I may have been telling them it was pretty much done, because I thought I had about three more weeks than I did. And then they're like, oh, can we see it all tomorrow? So I've been sat here for six hours building out the back end of this thing, hooking up Recounts [tool:Recounts], Resend [tool:Resend], a whole bunch of other stuff.
[00:11:22] Ryan C: I did a V4 sweep of the CRM that I'm building for estate agents, which was huge. I did that on a slash goal, did a massive planning document, and then did a slash goal for it to go through and do it with a rubrics check at the end. And Scott, I've just remembered that you told me to do a smoke test, and I completely forgot to tell it to do that, so no doubt there'll be a V5 when it finishes everything I asked it to do for V4.
[00:12:20] Scott Rippey: I completely forgot — because you just reminded me when you said smoke test — some of this stuff I missed. I went completely bananas on Claude 4 Fable [tool:Claude 4 Fable] when I had it. I burned through so much stuff. I had an SOP application I was building — I had a great plan, all these phases left, like eight phases. I'm like, well, I'm going to run Fable on this thing. I set that thing on auto and let it roll just to scaffold it up to the MVP. I could only run two phases and stop — two phases would burn my five-hour window. Because when it starts going, the amount of looping and tests — I gave it all the goals and the rubric stuff. At one point I think it had 50-some agents going, and I went, no wonder my tokens are gone.
[00:13:30] Scott Rippey: ▶ Obviously we can't do security stuff with it because of the guardrails, so it was useless for that, but as a planning and scaffolding tool — very quickly and more accurately — there was way less to fix at the end. I didn't have to babysit it as hard. Opus is great, but that was impressive to me. I ran that thing hard for three days before they yanked it.
[00:14:16] Patrick Chouinard: Not everybody was happy. But we'll see a similar model probably coming up in the next couple of days or weeks.
[00:14:29] Scott Rippey: Also, Sonnet 5 [tool:Sonnet 5] — the new Sonnet's about to hit, and supposedly it's better than Opus 4, so we'll just see. It'd be nice if it wasn't, because it's cheaper.
[00:14:45] Juan Torres: <Q>Have you guys tried GLM 5.2? I'm supposed to have better metrics than Opus 4 or something like that?</Q>
[00:14:57] Ty Wells: Who's going to look into that, Juan?
[00:15:01] Juan Torres: <A>I've been thinking of downloading the GLM [tool:GLM] IDE just to try out their whole infrastructure and try the model, but I haven't had the chance. It just seems weird because all the Chinese models are outperforming the American models by like 5 or 10 percentile. It's like a jab in the nose of the American AI infrastructure. I'm pretty sure the Chinese Communist Party has a strategy to keep outpacing American AI — it happened with the DeepSeek [tool:DeepSeek] thing, just outsmarting ChatGPT at the time by a certain percentile.</A>
[00:16:00] Scott Rippey: ▶ I also think a lot of benchmarks are benchmarks — they're very lacking. When you start looking into benchmarks, a lot of it's not even the correct stuff being benchmarked. It's pretty basic. I don't even take benchmarks seriously anymore.
[00:16:21] Juan Torres: And it's supposed to be at one-fifth of the cost.
[00:16:22] Scott Rippey: Cost is good, though.

---

<!--SEGMENT
topic: Local LLM Hardware & AirLLM Layer-Loading Library
speakers: Patrick Chouinard, Scott Rippey, Ty Wells, Juan Torres, Morgan Cook
keywords: AMD Halo, Apple Silicon, shared memory, Mac Studio, Mac Mini, MLX, GGUF, 70B parameters, context window, 512GB RAM, AirLLM, layer-loading, consumer hardware, Raspberry Pi, local inference, open source Python
summary: The group discusses hardware constraints for running local LLMs — regretting not buying higher-memory Apple Silicon before shortages — and the trade-off between model size and context window. Morgan Cook introduces AirLLM, an open-source Python library that loads LLM layers sequentially rather than all at once, enabling 32B+ models to run on consumer hardware with limited RAM. The AMD Halo device with 128GB shared memory is also mentioned as a promising new option.
-->

[00:24:51] Ty Wells: <Q>Did anybody look at that AMD device — I can't remember the name, Halo maybe?</Q>
[00:24:54] Patrick Chouinard: <A>Yeah, the one that's supposed to be in the same class as Apple Silicon with shared memory?</A>
[00:25:03] Ty Wells: Yeah, 128 gig shared. Anybody know the price? I meant to look.
[00:25:10] Patrick Chouinard: With memory prices these days, with 128 gig, it must be eye-watering.
[00:25:17] Ty Wells: I'm glad I got my MacBook. Somebody told me, get 128. I was like, I don't need all of that. And I got the 128. This was late December last year.
[00:25:38] Scott Rippey: I got a decent amount — I think I got 64 on it, but I should have gone higher. I was never thinking about running local models for coding at some point, because they're closing the gap. Why didn't I do it before everything was shorted?
[00:26:00] Patrick Chouinard: If I would have known, I would have bought a 512-gig Mac Studio [tool:Mac Studio].
[00:26:09] Scott Rippey: Oh yeah. Because 512 will get you very close to the Frontier class — pretty much almost right there. You've got room to run it. And you can't get anything with that on a Mac now.
[00:26:23] Patrick Chouinard: My thinking is not necessarily to run Frontier class. With 512 gig, you can have context. ▶ I prefer to have a 70 billion parameter model, which is still pretty intelligent, and give it a 256k context window. Because if you run a trillion-parameter model, you're going to need all of your memory just to load the model.
[00:28:16] Patrick Chouinard: Just before we leave — Morgan, I see you connected. Did you want a chance to say or show something?
[00:28:27] Morgan Cook: No, I don't have anything to present this week. I did find one thing that kind of adds to what you guys were talking about. There's a new local model engine called AirLLM [tool:AirLLM], and it's a Python engine that can load a 32 billion model. The way it does it — instead of loading the entire thing in memory at one time, it loads each of the layers of the LLM model tree in a route loop kind of process. So it'll process the first layer, swap out, load the next layer, process it, swap out, load the next layer, until it gets to the end of the chain.
[00:29:20] Morgan Cook: I haven't installed and tested it yet, but it's supposed to be workable and faster than a model just loading completely in memory when you have a limited amount of memory. ▶ Its intent is to run on smaller devices and still be able to process through all the chain. That's something that might be worth looking at. I'll see if I can find the link to put in.
[00:29:34] Patrick Chouinard: Yep, that'd be very nice. We're always constrained by memory, no matter how much memory we have.
[00:30:03] Morgan Cook: It's actually a GitHub repository — an open-source Python library designed to run massive large language models on consumer hardware. [link:AirLLM GitHub repository - open source Python library for running large LLMs on consumer hardware]
[00:31:01] Morgan Cook: I did see that one — the new box that mimics the Mac Mini. That looks really nice, the shared memory one.
[00:31:11] Patrick Chouinard: To me, as much as it's copying the Mac Mini, it's just finally shared memory on some other platform.
[00:31:19] Morgan Cook: ▶ The hardware companies are starting to really identify the fact that we need more hardware that runs local. RAM used to be cheaper than VRAM, but I'm not sure how true it is today. None of the chips are cheap. You can't even get a Raspberry Pi anymore that doesn't cost a normal way.
[00:31:50] Patrick Chouinard: That's why I'm leveraging all the mini PCs I was able to get before all of that.

---

=== UNRESOLVED SPEAKERS ===

- **Morgan Cook** — raw name "Morgan Cook" does not appear in the supplied SPEAKER_ALIASES map; passed through unchanged.