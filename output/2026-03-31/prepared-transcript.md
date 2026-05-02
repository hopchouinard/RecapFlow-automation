=== SESSION ===
date: 2026-03-31
duration_estimate: ~120 min
main_themes: [Claude Code plugin ecosystem (Codex plugin, Lab/LabSync, Claude Speak), AI labor-market impact + advising youth (cybersecurity, BA skills), scope creep + project discipline in agentic dev, compliance landscape (ISO, SOC 2, HIPAA, Vanta), RAG/RLM/re-ranker layering, local-AI infrastructure on repurposed gaming PCs (Proxmox, Tailscale, Twingate)]
===

<!--SEGMENT
topic: pre-meeting catch-up + research-loop tool intro
speakers: Patrick Chouinard, Marc Juretus, Paul Miller
keywords: automated search agent, daily reasoning, RSS-style research loop, stock screening with RSI, Reddit follow-up research, recap flow, hobby = AI
summary: Patrick describes the research-loop tool he's deploying at his client — automated search agent that discovers subjects, dedupes, deep-researches, scores results, and reasons across findings with a daily human-feedback loop. Marc riffs on using the same idea to monitor stocks (200-day average + RSI, Reddit corroboration, narrow 5 picks down to 2 daily). Paul joins; small joke that AI is Patrick's only hobby.
-->

[00:00:47] Patrick Chouinard: Hey, Marc, how's it going?
[00:00:53] Marc Juretus: Pretty good, Mr.
[00:00:54] Marc Juretus: Patrick, and you?
[00:00:55] Patrick Chouinard: Good, good.
[00:00:56] Patrick Chouinard: Good.
[00:01:01] Marc Juretus: How was your day, brother?
[00:01:05] Patrick Chouinard: Busy.
[00:01:08] Patrick Chouinard: Now that I'm implementing my research loop at my client, let's say that there's a lot of stuff to do.
[00:01:26] Marc Juretus: Well, I don't know why I'm not remembering.
[00:01:29] Marc Juretus: What's the 10-second summary of what it does?
[00:01:33] Patrick Chouinard: Oh, it's an automated search agent that I have a back-end where you can manage all of the search subject that you want [tool:research-loop agent].
[00:01:43] Patrick Chouinard: It discover the subject first, and then it dedupe all of the information it found.
[00:01:50] Patrick Chouinard: Then it go in deep and do detailed research about each subject.
[00:01:55] Patrick Chouinard: Track all of that into a database, allow you to rate the quality of
[00:02:00] Patrick Chouinard: Each result or incite it to do more research of one type versus another and discard other search.
[00:02:08] Patrick Chouinard: What's it searching against?
[00:02:11] Patrick Chouinard: The internet.
[00:02:13] Marc Juretus: Oh, just the internet in general.
[00:02:14] Marc Juretus: I thought you had a data source from a company.
[00:02:17] Marc Juretus: It could be.
[00:02:18] Patrick Chouinard: That's one of the things that we want to add to it.
[00:02:20] Patrick Chouinard: Right now it just does web search, but we want to enable it to be connected to different data source, private data source, private source systems, things of that nature.
[00:02:30] Patrick Chouinard: But all under the idea that you gather the information, present it in a nice visual way to people on a daily basis.
[00:02:37] Patrick Chouinard: ▶ You can even put in some way of notifying people whenever a new information is, and you can do cross analysis of your result also.
[00:02:47] Patrick Chouinard: So if you find a lot of result pointing towards something, some change in whatever market you're following, well, you can have AI reason about that change.
[00:02:58] Patrick Chouinard: So not only only finding.
[00:02:59] Patrick Chouinard: ▶ Information, but reasoning about the information it finds and get human feedback to improve the result on a daily basis.
[00:03:07] Marc Juretus: Nice.
[00:03:10] Marc Juretus: That's the thing about this, man.
[00:03:12] Marc Juretus: You can go in whatever direction you want to do so many different things, man.
[00:03:17] Marc Juretus: That's one of my biggest problems where I just don't dial into something as a whole.
[00:03:23] Marc Juretus: I do a lot of trading with stocks and stuff.
[00:03:26] Marc Juretus: And there's different measurables.
[00:03:29] Marc Juretus: To make a long story short, you can have a monitor if a stock's over 200, it's 200-day average, and it's RSI, which is its strength.
[00:03:36] Marc Juretus: ▶ I want it to go out every day, find me five that it likes, and then also do additional research, like you were stating, like, all right, I want you to go to Reddit.
[00:03:44] Marc Juretus: I want you to go here.
[00:03:46] Marc Juretus: And then I want you to narrow that five down to two you like.
[00:03:50] Marc Juretus: You just go all day.
[00:03:53] Patrick Chouinard: Yep.
[00:03:55] Patrick Chouinard: Hey, Mr.
[00:03:56] Patrick Chouinard: Paul.
[00:03:58] Paul Miller: Hey, guys.
[00:03:59] Paul Miller: How's it going?
[00:03:59] Marc Juretus: No, this guy.
[00:04:02] Marc Juretus: We don't get him every week, but when we get him, he's here, right, Paul?
[00:04:06] Paul Miller: Yeah, no, I missed last week.
[00:04:08] Paul Miller: That would have been nice to hear from Brandon, but luckily we've got the video recording, so that's all good.
[00:04:14] Marc Juretus: This meeting is being recorded.
[00:04:16] Patrick Chouinard: Yep, and Master Paul is leading the show tonight.
[00:04:20] Marc Juretus: Oh, man.
[00:04:21] Paul Miller: Yeah.
[00:04:22] Marc Juretus: Good hands.
[00:04:29] Patrick Chouinard: You've seen the video, but did you look also at what RecapFlow created last week?
[00:04:36] Paul Miller: Yeah, yeah, that was interesting.
[00:04:41] Patrick Chouinard: I'm dialing it in slowly.
[00:04:45] Paul Miller: Yeah, that's a cool tool, that.
[00:04:55] Patrick Chouinard: Yeah, and I have a couple of things to try this week, also, or to showcase.
[00:05:00] Patrick Chouinard: This week, like every time I get by Friday night and I'm like, what the hell am I going to show next weekend by Tuesday?
[00:05:09] Patrick Chouinard: I'm like, crap, I have too much stuff to show.
[00:05:13] Paul Miller: Well, yeah, at least with me hosting it, you'll have a better chance to take us through and we all enjoy your run through.
[00:05:21] Paul Miller: So that's going to be cool.
[00:05:24] Marc Juretus: You didn't get a hobby, Patrick.
[00:05:28] Paul Miller: No, no, no.
[00:05:30] Marc Juretus: I guess that one is called AI.
[00:05:33] Paul Miller: Yeah, what am I saying?
[00:05:35] Paul Miller: Yeah, we're quite happy with this hobby.
[00:05:37] Marc Juretus: Leave it, Marc.
[00:05:40] Patrick Chouinard: I was going to say, I think I do have one.
[00:05:46] Marc Juretus: What's the longest you stayed in that chair?
[00:05:49] Marc Juretus: About 18?
[00:05:51] Marc Juretus: In this one or ever?
[00:05:56] Marc Juretus: Well, you told me that before when you had a downtime, so that's not applicable.
[00:06:00] Marc Juretus: I mean, like, just working on something and refusing to quit until it works.
[00:06:05] Patrick Chouinard: Lifetime, I actually would say my worst session was about 36, 37 hours straight.
[00:06:16] Marc Juretus: Yeah, but that was when something was down, right, at your job, right?
[00:06:21] Marc Juretus: Isn't that what you stated?
[00:06:22] Patrick Chouinard: Yeah, yeah, yeah.
[00:06:23] Marc Juretus: I'm talking about working on something on AI for fun.
[00:06:26] Marc Juretus: Oh, for fun?
[00:06:27] Marc Juretus: Yeah, that's what I meant.
[00:06:29] Patrick Chouinard: 12, 13?
[00:06:30] Marc Juretus: Yeah.
[00:06:31] Marc Juretus: That's easy.
[00:06:34] Paul Miller: And you don't even know that time's going past is a scary thing.
[00:06:37] Marc Juretus: No, you don't.
[00:06:39] Marc Juretus: Because I'm OCD, and if it's broke, I can't go to bed.
[00:06:43] Marc Juretus: It's bad, man.
[00:06:44] Paul Miller: Exactly.
[00:06:45] Marc Juretus: It's bad.
[00:06:47] Patrick Chouinard: Actually, token has been the thing that sent me to bed most often, like running out of them.
[00:06:52] Patrick Chouinard: But with what I started using this week, mixing codex and Claude Code in the same session.
[00:06:59] Patrick Chouinard: bad.
[00:06:59] Patrick Chouinard: Yeah.
[00:07:00] Patrick Chouinard: I doubled my token, and not a good thing for my sleep hours.
<!--SEGMENT
topic: Anthropic source leak + npm hack + insider-threat reality
speakers: Ty Wells, Patrick Chouinard, Paul Miller, Marc Juretus
keywords: Anthropic Claude Code leak, npm supply chain hack, Mythos security model irony, AI agents finding vulnerabilities, Ernst & Young 70% insider stat, disgruntled employee, missing eject button
summary: Ty notes the Claude Code source got leaked at 4am. Patrick is more worried about the npm supply-chain hack. Group agrees AI agents that find vulnerabilities will only accelerate the problem (time + energy + tokens = unlimited offense). Paul flags the irony that Anthropic's Mythos model was supposed to deliver security insights. Marc raises insider-threat percentage — Paul cites Ernst & Young's 70% disgruntled-employee figure and missing offboarding eject button as the typical pattern.
-->

[00:07:05] Ty Wells: Hi, guys.
[00:07:07] Marc Juretus: What's up, Ty?
[00:07:09] Paul Miller: Hey, Ty.
[00:07:11] Ty Wells: Hey, Paul.
[00:07:13] Ty Wells: What's going on today, other than Claude Code, CLI code?
[00:07:20] Patrick Chouinard: Well, now you can install Codex as a tool inside of Claude Code.
[00:07:25] Paul Miller: Yeah, that was a cheeky move.
[00:07:28] Ty Wells: No, I'm talking about the leak.
[00:07:31] Paul Miller: Oh, yeah, that was bad.
[00:07:35] Ty Wells: The Claude Code source code got leaked [tool:Claude Code leak].
[00:07:38] Patrick Chouinard: Yeah.
[00:07:39] Paul Miller: Oh, is this a recent leak in the last 24 hours, Ty?
[00:07:43] Ty Wells: Yeah, that was this morning at like 4 a.m.
[00:07:47] Patrick Chouinard: But to be honest, I'm more worried about the hack of npm [tool:npm hack].
[00:07:52] Paul Miller: Yeah, that's a big boy, too.
[00:07:54] Paul Miller: bad one.
[00:07:55] Ty Wells: Yeah, that, yeah, I got on that right away.
[00:07:59] Paul Miller: right.
[00:07:59] Paul Miller: All
[00:08:00] Paul Miller: Yeah.
[00:08:01] Paul Miller: You get your DevOps agents proactively going through each of your servers as a task.
[00:08:08] Paul Miller: Because you've got that cool app that does that already off the shelf, don't you, Ty?
[00:08:13] Ty Wells: Yep.
[00:08:14] Ty Wells: Yep, I do.
[00:08:16] Ty Wells: Got to keep an eye on those things.
[00:08:18] Ty Wells: But, you know, that's going to happen.
[00:08:20] Ty Wells: It's only going to get worse.
[00:08:21] Ty Wells: I'm not going to lie, guys.
[00:08:22] Ty Wells: I don't mean to be doom and gloom, but it's just so easy, right?
[00:08:26] Ty Wells: It's just so easy to go after this stuff.
[00:08:29] Ty Wells: Not intentionally, but accidentally.
[00:08:31] Ty Wells: Find these things, and if you get in the wrong hands as anything, they'll exploit it and blow things up.
[00:08:39] Marc Juretus: Plus the ability of an agent running all the time to find stuff.
[00:08:43] Marc Juretus: You're not going to die.
[00:08:45] Marc Juretus: It's the way around it.
[00:08:47] Ty Wells: Yep.
[00:08:47] Ty Wells: Time and energy.
[00:08:48] Ty Wells: That's all you need.
[00:08:49] Ty Wells: And now you've got that.
[00:08:50] Ty Wells: Unlimited time and energy, right?
[00:08:52] Ty Wells: And tokens.
[00:08:53] Paul Miller: Well, the interesting thing with the leak of the last leak of Anthropic
[00:09:00] Paul Miller: Patrick's mythos model is one of its key things that it was delivering was security insights and proactive prevention and stuff [tool:Mythos].
[00:09:11] Paul Miller: Yes.
[00:09:12] Ty Wells: A little irony there.
[00:09:14] Paul Miller: Yeah.
[00:09:15] Paul Miller: Yeah, totally.
[00:09:17] Marc Juretus: Is it generally when people say leak or hack, it always comes down to 90% of the time a former disgruntled employee?
[00:09:25] Ty Wells: You know, the inside threat is real, but a lot of times it's accidental.
[00:09:31] Ty Wells: mean, God, we really stick all day long.
[00:09:34] Paul Miller: Well, it's interesting to say that, Marc.
[00:09:37] Paul Miller: ▶ I used to work at Ernst & Young, and from an Ernst & Young audit perspective, 70% of the time all leaks were disgruntled employees.
[00:09:49] Marc Juretus: Well, I was a little high on that, but it's just like, hey, they got hacked.
[00:09:52] Marc Juretus: No, they didn't hack that encryption.
[00:09:53] Marc Juretus: They had an employee that got fired and access they did not turn off and game on.
[00:09:59] Paul Miller: Let's Let's Let's
[00:10:00] Paul Miller: Yeah, they don't have the best corporate culture within their organization, so some people say.
[00:10:08] Marc Juretus: ▶ Yeah, well, I believe enough people don't have that eject button.
[00:10:12] Marc Juretus: Like, the employee's gone, go through everything they have access to with a script in some sort.
[00:10:17] Marc Juretus: Take, remove every AD group, you know what mean?
[00:10:20] Marc Juretus: Everything.
[00:10:21] Marc Juretus: They will get to it.
[00:10:22] Marc Juretus: Okay, you see how that works out for you.
[00:10:27] Paul Miller: All right.
<!--SEGMENT
topic: Paul opens the meeting + week's news roundup
speakers: Paul Miller, Patrick Chouinard
keywords: weekly news roundup, Anthropic leak, Sora shutdown, SPUD model, Shopify layoffs, Agentex storefronts, virtual entity open-source model
summary: Paul takes hosting duties. Quick news roundup: new models out, Anthropic source leak, OpenAI shutting down Sora to free compute for upcoming SPUD model release in 2-3 weeks, Shopify layoffs, Agentex storefronts, and a new open-source model for managing virtual entities. Sets up Patrick's demo.
-->

[00:10:28] Paul Miller: Shall we get started?
[00:10:30] Paul Miller: So guys, I am the host this week.
[00:10:34] Paul Miller: Thank you, Patrick, for running the other weeks and Brandon last week.
[00:10:40] Paul Miller: This will give us a good chance for Patrick to run through some of the cool projects that he's doing, plus everyone else getting the update on.
[00:10:51] Paul Miller: I'll just take a screenshot of where we are now.
[00:10:57] Paul Miller: Do we have any, any, any,
[00:11:00] Paul Miller: questions, Patrick, that have come through?
[00:11:05] Patrick Chouinard: Nope, not this week.
[00:11:09] Paul Miller: So I'll kick off then a lot of updates, even right up until now in the last week.
[00:11:20] Paul Miller: We've got new models that have come out.
[00:11:23] Paul Miller: We've got the leap from Anthropic, or the last leap from Anthropic, OpenAI, shutting down Sora to make way for a new model that's going to be released in the next two to three weeks [tool:SPUD].
[00:11:38] Paul Miller: So-called SPUD, I think it's called.
[00:11:42] Paul Miller: More layoffs, Shopify, Agentex storefronts, and all sorts of other releases [tool:Agentex].
[00:11:50] Paul Miller: But, and those, and that model, there seems to be a new open source model.
[00:12:00] Paul Miller: for managing virtual entities.
[00:12:03] Paul Miller: I can't remember what it was called, but it seems pretty good.
[00:12:08] Paul Miller: Be cool if anyone's got into that and got any stories to share about using that.
[00:12:16] Paul Miller: But let's get into it.
[00:12:21] Paul Miller: Hold on.
[00:12:22] Paul Miller: Let's...
[00:12:23] Paul Miller: So, Patrick, you are first on the video list.
[00:12:31] Paul Miller: Do you want to do your big share?
<!--SEGMENT
topic: Patrick demo — Codex plugin + Lab/LabSync + Claude Speak
speakers: Patrick Chouinard, Paul Miller, Ty Wells
keywords: Codex plugin for Claude Code, adversarial code review, Lab website, Lab Sync, AI personality plugin, Claude Speak, GPT-4o Mini TTS, ElevenLabs cost comparison, end-of-conversation hook, mid-flow speak skill, $1/day OpenAI cost
summary: Patrick walks through three things from his weekend. (1) Just installed a Codex plugin for Claude Code — Codex handles code review and adversarial review, freeing Claude Code tokens for creation. (2) Built a 'Lab' aggregator site for all his sub-website projects, with LabSync to push registrations to the marketplace + the lab site from a single GitHub repo. (3) Claude Speak — a hook that reads the last conversation block aloud via GPT-4o Mini TTS (chose it over ElevenLabs because of cost; ~$1 of OpenAI for an entire weekend of usage). It also exposes a mid-turn speak skill so Claude can interrupt and request attention.
-->

[00:12:34] Patrick Chouinard: Sure, why not?
[00:12:37] Patrick Chouinard: First, the last thing I did prior to the call is installing this.
[00:12:44] Patrick Chouinard: I just put it in the chat.
[00:12:46] Patrick Chouinard: Basically, Codex plugin for Claude Code [tool:Codex plugin].
[00:12:55] Patrick Chouinard: Basically, it's a good way for me to save tokens so I can let Codex...
[00:13:00] Patrick Chouinard: Next, do all of the code review, adversarial code review, all of what it's good at, basically, and leave the token, the creation token to Claude Code [tool:adversarial code review].
[00:13:12] Patrick Chouinard: So haven't tested it yet.
[00:13:14] Patrick Chouinard: I just installed it, but I'm certainly going to let you guys know how it goes.
[00:13:20] Patrick Chouinard: But so far from what I've reviewed, it seems pretty interesting.
[00:13:27] Patrick Chouinard: Second, my little project fun.
[00:13:32] Patrick Chouinard: As you know, in the last couple of weeks, I've created a bunch of plugins and I've been working a lot around, like, how can I increase Claude Code capability for myself and make it more useful?
[00:13:46] Patrick Chouinard: And I started to see that it was going everywhere at once and it was not easy to try to keep track of all of those projects.
[00:13:56] Patrick Chouinard: right, so excited to...
[00:13:59] Patrick Chouinard: Decided to...
[00:14:00] Patrick Chouinard: Bring them all together, let's see, oh boy, too many screens open, there we go, okay, so in my, this is my personal site, but in the ecosystem, I created a new, a new one called Lab, Lab, so if I go to Lab, basically this is everything I, it's all projects that are too small to have their own website, but that deserves to be documented somewhere and tracked, so every single little project that I've created is linked to the Lab, and it's either a plugin, others, so those are peripheral, and when I get the time to create skills, MCP or workflow, they're also going to be tracked in here [tool:Lab].
[00:15:00] Patrick Chouinard: You can go to them directly through the constellation here or actually navigate through the registry card at the bottom.
[00:15:11] Patrick Chouinard: So the one I have right now, I've talked to you about AI personality, I think, last week.
[00:15:17] Patrick Chouinard: So basically those are personality you can deploy through script to all of your coding agent or web client.
[00:15:26] Patrick Chouinard: Status line and, oh, another one I created is Claude Speak [tool:AI personality].
[00:15:31] Patrick Chouinard: This one is brand new from this week [tool:Claude Speak].
[00:15:33] Patrick Chouinard: It was fun using Whisperflow to talk to Claude Code, but I realized that sometimes it goes on and works for 10 minutes.
[00:15:41] Patrick Chouinard: So when it comes back, I don't see it and it stays there and I'm wasting time that I could use to continue.
[00:15:49] Patrick Chouinard: So I decided to give it a voice.
[00:15:50] Patrick Chouinard: So basically I'm using GPT-4o Mini TTS [tool:GPT-4o Mini TTS].
[00:15:57] Patrick Chouinard: What I found that was the cheapest...
[00:16:00] Patrick Chouinard: With a decent quality right now, I've considered ElevenLabs, but it was way too expensive [tool:ElevenLabs].
[00:16:07] Patrick Chouinard: And basically it's a hook that captures the end of a conversation for the passive voice.
[00:16:12] Patrick Chouinard: So the last block of comment that Claude state in the Claude Code flow, it will speak out right.
[00:16:20] Patrick Chouinard: And I also gave it a speak skill, which I made it aware of.
[00:16:25] Patrick Chouinard: Meaning if it thinks it needs to get my attention mid-flow, it can actually call in the speaking functionality.
[00:16:36] Patrick Chouinard: And I've published it as a skill, as a plugin.
[00:16:40] Patrick Chouinard: So basically you can go to my marketplace, which is documented on the site as well, with all the information on how to install it.
[00:16:50] Patrick Chouinard: So basically I created the lab as some place where everything I work from is published.
[00:16:56] Patrick Chouinard: And you even have something called LabSync, which is in-
[00:17:00] Patrick Chouinard: So it's not deployed, but what that is is a tool that allows me to connect everything together [tool:LabSync].
[00:17:11] Patrick Chouinard: So basically, if I create a new plugin, I document it in LabSync and it will push it to the marketplace, push it to the lab website, and do all the connection together.
[00:17:23] Patrick Chouinard: And it looks like this.
[00:17:26] Patrick Chouinard: So here, I haven't loaded every skill yet, but as I'm creating them, it makes sure that it's published correctly.
[00:17:35] Patrick Chouinard: It's synced correctly to all of the target.
[00:17:39] Patrick Chouinard: I have a log of every push that I made.
[00:17:42] Patrick Chouinard: ▶ You can register a new tool just by giving the GitHub repo, detect and register.
[00:17:48] Patrick Chouinard: It reads the readme file, it creates the page for the lab, it creates the JSON for the marketplace, and it syncs everything.
[00:17:58] Patrick Chouinard: And all prompts.
[00:18:00] Patrick Chouinard: are visible and editable at runtime, plus the model are also editable at runtime.
[00:18:09] Patrick Chouinard: So those are the little thing that got my weekend going.
[00:18:16] Patrick Chouinard: But the other one I wanted to quickly show you guys is loudspeak because I think it's pretty interesting.
[00:18:26] Patrick Chouinard: And let me see.
[00:18:27] Patrick Chouinard: I hope I'm going to build a share sound.
[00:18:33] Patrick Chouinard: Go.
[00:18:42] Patrick Chouinard: Hear it.
[00:19:06] Patrick Chouinard: I just told him, like, yeah, can you use your voice and speak, please?
[00:19:09] Patrick Chouinard: By the way, you have an audience.
[00:19:14] Ty Wells: It sounds like a hedge.
[00:19:35] Patrick Chouinard: Oh, fun.
[00:19:36] Patrick Chouinard: Always when you do a demo that it decided to work.
[00:19:40] Patrick Chouinard: But it's always the equation.
[00:19:44] Paul Miller: The more eyes, the more risk that doesn't work.
[00:19:48] Patrick Chouinard: The sad part is it actually worked the entire weekend, like multiple times.
[00:19:54] Patrick Chouinard: I've, uh, but let's see if, uh,
[00:20:00] Patrick Chouinard: I'm going to try.
[00:20:01] Ty Wells: Is your microphone in use causing it, or are you tested it with your microphone in use?
[00:20:05] Patrick Chouinard: Nah, that might be it.
[00:20:07] Patrick Chouinard: That's probably the fact that my mic is always on.
[00:20:11] Patrick Chouinard: Yeah.
[00:20:11] Patrick Chouinard: Anyway.
[00:20:13] Patrick Chouinard: Okay.
[00:20:14] Patrick Chouinard: But I'm getting, you get the point.
[00:20:16] Patrick Chouinard: The idea is it can call the voice, the speak service, and it will speak out loud mid-turn, or at the end of the turn, it will read the last paragraph.
[00:20:26] Patrick Chouinard: ▶ And in terms of cost, because you have to give it an OpenAI API key, I've worked on it all day, Sunday, and burned through multiple five-hour limit on Claude Code, and it cost me about a dollar worth of OpenAI.
[00:20:44] Patrick Chouinard: So it's really, really cheap.
[00:20:48] Paul Miller: Wow.
[00:20:49] Ty Wells: So that's incredible, Patrick.
[00:20:51] Ty Wells: You know I'll be working with this here.
[00:20:53] Ty Wells: I've got the next hour and a half, two hours, and then I'll be, I'll probably be working on it here in a second.
[00:20:58] Ty Wells: One question I've got for you.
[00:21:00] Ty Wells: The mid-speak, is that like a by-the-way slash command?
[00:21:05] Ty Wells: Is it interrupting mid-speak to tell you, or...?
[00:21:09] Patrick Chouinard: It's actually a skill.
[00:21:10] Patrick Chouinard: So it's a skill, and you write in the CLAUDE.md file the fact you inform it that it has that skill.
[00:21:19] Patrick Chouinard: ▶ So if there is something that requires your attention, if it has a question mid-turn or something, it will just be...
[00:21:25] Patrick Chouinard: Welcome to the show.
[00:21:27] Patrick Chouinard: I'm a friendly neighborhood AI assistant.
[00:21:29] Patrick Chouinard: I've got a voice now, so buckle up.
[00:21:32] Patrick Chouinard: What are we working on today?
[00:21:34] Ty Wells: Okay, so I'm little bit late, but decided to answer finally.
[00:21:40] Patrick Chouinard: When I don't have 30,000 different things open at the same time, it's pretty much real-time.
[00:21:46] Patrick Chouinard: But you've seen what it said.
[00:21:51] Patrick Chouinard: You've seen that there's personality behind it.
[00:21:54] Patrick Chouinard: That's because it also has my AI personality pushed into Claude Code.
[00:21:58] Patrick Chouinard: So...
[00:22:00] Patrick Chouinard: It's made to be confrontational and it's a development assistant, so I don't want it to say all of my ideas are the best thing that ever happened to God's green earth.
[00:22:12] Patrick Chouinard: ▶ I mean, I want it to be challenging me, so that's why I gave it that personality.
[00:22:18] Paul Miller: Brilliant stuff, Fred.
[00:22:19] Patrick Chouinard: So that was my weekend.
[00:22:23] Paul Miller: Is it still snowing and really cold up there in Canada?
[00:22:28] Paul Miller: Is this the reason why we're seeing so much coming out of your tech lab?
[00:22:34] Patrick Chouinard: No, actually, that's just me.
[00:22:36] Patrick Chouinard: It was like 12 Celsius this weekend, so what, 50, 55?
[00:22:46] Patrick Chouinard: No, it's just me.
[00:22:47] Patrick Chouinard: I don't like to go outside.
[00:22:51] Paul Miller: Wow.
[00:22:53] Paul Miller: Okay.
[00:22:55] Paul Miller: Thanks, Patrick.
[00:22:57] Paul Miller: So next on on the...
<!--SEGMENT
topic: Marc's interview prep — AI impact on jobs + advising youth
speakers: Marc Juretus, Patrick Chouinard, Ty Wells, Morgan Cook
keywords: AI impact on jobs, knowledge work, decision-tree work, cybersecurity career path, blue-collar resilience, plumbing/electrical for data centers, programming as markdown programming, programming != syntax
summary: Marc is prepping for an AI workshop and asks the group two questions. (1) Which fields/jobs will be most impacted by AI? Patrick: better question is which won't be. Ty: knowledge work where steps are decision-tree-able. (2) What would you advise a young person entering the workforce? Ty: cybersecurity, plus blue-collar service jobs (plumbing, carpentry, data-center electrical/water-cooling). Patrick disagrees on excluding programming: 'You'll be a markdown programmer, but you still need that skill — building isn't about syntax, it's about ideas, structure, workflow, loops.'
-->

[00:23:00] Paul Miller: The, um, on the, on the talk list is, uh, Marc.
[00:23:05] Paul Miller: Um, how's it going, Marc?
[00:23:08] Marc Juretus: Oh, good.
[00:23:09] Marc Juretus: I don't really have, uh, one of my Patrick demos to show tonight, but, um, I'm supposed to do a demo to like, you know, like a small group, or a friend of mine does a lot of training with tech stuff, so he wanted somebody to come and talk about AI for a small group of people.
[00:23:22] Marc Juretus: So, two questions I'd like to ask the group that I have my opinion on it, but I'd like to hear you guys because you are brilliant minds.
<Q>[00:23:30] Marc Juretus: Um, two of them would be, which the question I know that's going to be presented is what fields jobs do you believe will be the most impacted by AI and in what time span?</Q>
[00:23:42] Marc Juretus: Feel free anybody to jump in on that.
[00:23:44] Marc Juretus: I'm just going to take some notes against what I have and what you guys say.
<A>[00:23:49] Patrick Chouinard: I would tend to say the question is more which one will not be impacted by AI at this point.</A>
[00:23:55] Marc Juretus: Okay.
[00:23:57] Ty Wells: ▶ I would say knowledge work.
[00:23:59] Ty Wells: You said impact.
[00:23:59] Ty Wells: impact.
[00:23:59] Ty Wells: Thank
[00:24:00] Ty Wells: Knowledge work, like, you know, things where you follow steps to do, if you can create a skill of it, right, do step A and then B in the decision tree, and you're just clicking through the process, right, on your computer, that's where your work is in terms of, when I say knowledge work, you're not making any judgment calls in your workload, then you're on the list.
[00:24:30] Ty Wells: For sure.
<Q>[00:24:31] Marc Juretus: And then next one would be, I know I'll be asked, as I have a young son or daughter that wants to go into tech field, would you advise them to do so, or go to more, obviously, blue collar items?</Q>
[00:24:45] Marc Juretus: And if you would push them towards tech, what direction would you push them in?
[00:24:51] Ty Wells: ▶ For me, it would be cyber security, if it go in tech, I would go, you got to defend against everything that Patrick just built, right?
[00:24:59] Marc Juretus: me, Okay.
[00:24:59] Marc Juretus: Okay.
[00:25:00] Ty Wells: Or that we build every day.
[00:25:02] Ty Wells: Cybersecurity, for sure.
[00:25:04] Ty Wells: And with the assistance of, you know, Claude or, you know, some sort of AI to help, you know, help you in that process.
[00:25:12] Ty Wells: That's what I would say.
[00:25:13] Ty Wells: ▶ And then service jobs, of course, you know, plumbing, carpentry, things that require physical labor that are, you know, of high demand.
[00:25:21] Ty Wells: Those would be, you know, working in data centers, building them, that sort of thing.
[00:25:28] Morgan Cook: The fields for the data center are going to be plumbing for all the water cooling and electrical for running all the network wiring and electricity for the servers.
[00:25:37] Morgan Cook: So those are two really major fields right now that will go through it.
[00:25:43] Marc Juretus: I've actually thought with the cybersecurity, as you said, Ty, and obviously the service jobs you were just mentioning, but I'm like, I wouldn't push anybody towards programming or system administration at this point.
[00:25:53] Marc Juretus: Right?
[00:25:54] Marc Juretus: Would you agree?
[00:25:55] Patrick Chouinard: No, actually.
[00:25:57] Marc Juretus: Okay.
[00:25:58] Patrick Chouinard: It's the programming.
[00:26:00] Patrick Chouinard: ▶ You're be basically a markdown programmer, but you still need that skill.
[00:26:06] Patrick Chouinard: Knowing how to build is not about syntax.
[00:26:09] Patrick Chouinard: It's about ideas, structure, workflow, loops.
[00:26:13] Patrick Chouinard: Those still require someone.
[00:26:15] Patrick Chouinard: Claude is awesome to implement those.
[00:26:18] Patrick Chouinard: It's incredibly bad right now at creating those workflows.
[00:26:22] Patrick Chouinard: So you still need someone at the helm.
[00:26:25] Marc Juretus: I think the question that would be is in two to three years, is it still going to be that way, Patrick?
[00:26:31] Paul Miller: Yeah.
[00:26:31] Marc Juretus: Will be.
[00:26:32] Marc Juretus: I think they'll fix all of that and then some.
[00:26:35] Marc Juretus: Sorry, Paul.
<!--SEGMENT
topic: BA skills gap + subjective thinking + IT cyclical mainframe analogy
speakers: Paul Miller, Ty Wells, Marc Juretus, Morgan Cook, Patrick Chouinard
keywords: BA skills, business analytics, asking questions, ADHD-tuned student assistant, OECD education study, teacher aid, reporting automation, IT mainframe-PC-cloud cycle, structurally-identical-but-faster cycle, Microsoft/Apple founder analogy
summary: Paul observes that interns can't ask questions even though tools are good at answering them — the gap is BA-style problem framing. Ty agrees: the missing thing is subjective experience — Gen Z grads need to study things they don't care about to build cross-angle thinking. Paul shares OECD-wide study findings: AI in education converges on personalized student-assistant + teacher-reporting automation. Patrick offers his mental model: IT is cyclical (mainframe → PC → cloud → AI = same dumb-terminal-to-shared-machine pattern), and the cycle just runs faster each iteration.
-->

[00:26:36] Paul Miller: Well, yeah, I think it's interesting, Marc, because we had some interns that were in the middle of their college education at the moment come and help my sort of base business.
[00:26:53] Paul Miller: And the thing that was frustrating for me being part of this forum and this group.
[00:26:59] Paul Miller: ...
[00:26:59] Paul Miller: ...
[00:26:59] Paul Miller: ...
[00:27:00] Paul Miller: ▶ You've got some really smart young people, but they come into the workplace not understanding how to ask questions, and I think we've got some really powerful tools that are really good at answering questions, but we don't have people thinking about the questions, and if I think back to some of the skills that are the most useful that I've got now in working with AI projects, and working with many customers that want to spend the money now, and probably over the next two to three years, beyond that it's very hard to know, it's what are the questions that you would ask in a business analytics type way?
[00:27:47] Paul Miller: So what's the problem you actually have?
[00:27:51] Paul Miller: What are the insights in your business, and where are the barriers for you to make money?
[00:27:59] Paul Miller: got see.
[00:27:59] Paul Miller: I That's
[00:28:00] Paul Miller: Where are the barriers with how your business works on a process side?
[00:28:06] Paul Miller: You know, what are the steps and the core ways to run your business?
[00:28:10] Paul Miller: I've got a number of people that are entrepreneurs that have built different types of businesses.
[00:28:18] Paul Miller: And we're not talking tech businesses.
[00:28:20] Paul Miller: We're talking typical normies type businesses from engineering to logistics where people have built business entities and they want to sell their business.
[00:28:32] Paul Miller: But the CEO, the president of the company has got all of this stuff in his head or her head with the running of that business.
[00:28:43] Paul Miller: And how is she or he going to be giving, well, packaging that up so they can sell their business to someone else to take it on?
[00:28:52] Paul Miller: And where is the skill set for interacting with that person and driving this?
[00:29:03] Paul Miller: ▶ It's, for me, with a lot of younger people now, they're not asking the right questions to work with those people, and it's old-school BA-type knowledge is what I think is missing.
[00:29:17] Paul Miller: Does anyone else agree with that?
[00:29:20] Paul Miller: Absolutely.
[00:29:22] Ty Wells: I think subjective experience is what's missing, meaning your own personal experiences.
[00:29:30] Ty Wells: The things that you learn during your life, I think those add value.
[00:29:35] Ty Wells: Now, for Gen Z, obviously, they've got a whole different set of subjective thinking.
[00:29:43] Ty Wells: I think you have to understand that.
[00:29:48] Ty Wells: I said knowledge work, right?
[00:29:51] Ty Wells: And that's more like skill work, like computer skill work when I said knowledge work.
[00:29:58] Ty Wells: But I think you need...
[00:30:00] Ty Wells: They look at things for the future, for your son, and even for my four, I think they have to look at it more from every possible angle.
[00:30:11] Ty Wells: ▶ So they need to increase their knowledge to get that subjective thinking, which means you cannot go for a BS or a BA or whatever and that be it.
[00:30:23] Ty Wells: You have to go way outside of that and encompass as much knowledge as you can so you can build that subjective thinking, because that then brings you to a point where you're thinking a completely different way, because that's what I think you're going to need.
[00:30:37] Ty Wells: You can't just, you know, those typical paths of a career when you graduate are not going to exist, right?
[00:30:44] Ty Wells: They're going to be completely different.
[00:30:46] Ty Wells: And to get there, you have to be thinking differently.
[00:30:48] Ty Wells: So now would be the time to start thinking because we're creatures of habit, right?
[00:30:53] Ty Wells: We're just doing down that path.
[00:30:56] Ty Wells: We've got that tunnel vision.
[00:30:57] Ty Wells: You have to be thinking from every single angle.
[00:31:00] Ty Wells: ▶ And especially the things that you don't care about, especially the subject matter that you have no interest in, those are the things you need to focus on.
[00:31:10] Ty Wells: Because obviously the things that you like, you will pursue those.
[00:31:13] Ty Wells: The things that you do not like or you choose not to, you choose, I say that carefully, you choose not to take those of the things you need to write down and focus on those things, because the other things you're comfortable with.
[00:31:27] Marc Juretus: Yeah, mean, I'm going to become an approach like, you need to adopt and create.
[00:31:31] Marc Juretus: And if you're going come in here with the mindset that, hey, this is a fad, this, or the other.
[00:31:35] Marc Juretus: No, this isn't like in the dot-com when a lot of us got all of our starts where you could find a job anywhere.
[00:31:41] Marc Juretus: And if you got lucky enough where they gave you a bunch of founder shares and it was a major company, might not even be working anymore.
[00:31:46] Marc Juretus: That game has changed right now with this technology.
[00:31:49] Marc Juretus: It's going to be like, hey, I want you to go home.
[00:31:52] Marc Juretus: A lot of people have issues with power rate, like for their energy.
[00:31:55] Marc Juretus: Write yourself a little agent that goes out and takes your rate and what the current rates are.
[00:32:00] Marc Juretus: See if they can find one.
[00:32:01] Marc Juretus: Find something that's a part of your day that you at least adopt and you can speak intelligently on it.
[00:32:05] Marc Juretus: And, you know, even as far as learning, like, there's no reason to not know anymore.
[00:32:10] Marc Juretus: Like, you can go to Gemini, whatever one.
[00:32:12] Marc Juretus: I use Gemini a lot when I want to try to learn something new.
[00:32:15] Marc Juretus: You know, establish me a curriculum and let's do day one.
[00:32:18] Marc Juretus: And you can even set the tone.
[00:32:19] Marc Juretus: I want you to be aggressive and yell at me.
[00:32:21] Marc Juretus: There's no reason to not know.
[00:32:23] Marc Juretus: So that's going to be about my approach.
[00:32:25] Marc Juretus: And then probably the last question is, and I know you guys would keep going here is, the people that do exist in the industry, do you see them having two to three agents, personal agents to assess them during their work day?
[00:32:39] Marc Juretus: And three to five.
[00:32:40] Marc Juretus: Like, I'm going to have this, but I don't actually do this.
[00:32:43] Marc Juretus: I talk to my agent that talks to that.
[00:32:46] Marc Juretus: I'm just facilitating them.
[00:32:47] Marc Juretus: Do you see that as part of the future is my last question.
[00:32:52] Paul Miller: But Morgan, you had something you're wanting to raise?
[00:32:56] Morgan Cook: Yeah, yeah.
[00:32:56] Morgan Cook: So my, I work.
[00:33:00] Morgan Cook: with my ex-wife on occasion.
[00:33:01] Morgan Cook: She's not a computer person by any means, but she has some really good skills.
[00:33:08] Morgan Cook: And she has proven to me that somebody with those skills without programming can make a lot of progress using AI.
[00:33:20] Morgan Cook: And she has used all of her other communication skills in chatting with ChatGPT.
[00:33:25] Morgan Cook: And, you know, not just asking questions about where's the next talk will stand, but really in-depth questions, right?
[00:33:33] Morgan Cook: Knowing how to ask the questions, back to that same kind of thing is like the youngsters do not know how to ask the questions.
[00:33:39] Morgan Cook: They don't know how to think past, you know, one or two stages of questioning.
[00:33:44] Morgan Cook: That's the biggest skill with AI in working in this.
[00:33:49] Morgan Cook: And we've seen it all with our own stuff.
[00:33:51] Morgan Cook: When you ask a simple question, you usually get the worst answer possible.
[00:33:55] Morgan Cook: You you got to give a really clean context about what you want, what your discussion is.
[00:34:00] Morgan Cook: Now, to your third question that you just asked, what was it again, I forgot?
[00:34:08] Marc Juretus: So basically, they're going to ask, okay, say we survive this space and I'm working, what's going to, you believe in three to five, what will be a part of my workday system in my job?
[00:34:18] Marc Juretus: Will you be working with agents?
[00:34:20] Marc Juretus: Like, my thing is, I think there's going to be eight times the number of agentic agents running on their own purchasing this, that, and that.
[00:34:27] Marc Juretus: I'm very into crypto space.
[00:34:28] Marc Juretus: I think a lot of stuff is going to be being done behind the scenes.
[00:34:30] Marc Juretus: But my point is, will they have agents that they will be working with all day as part of their workday in three to five years?
[00:34:38] Morgan Cook: I think the simplest answer is yes.
[00:34:41] Morgan Cook: And it starts with simply, you know, their first agent of ChatGPT is the first one.
[00:34:46] Morgan Cook: They're going to communicate with that constantly throughout the day.
[00:34:50] Marc Juretus: Yeah.
[00:34:50] Morgan Cook: Either to generate artifacts or to process an artifact or eventually learn how to create an agent to do the work for them.
[00:34:58] Morgan Cook: So I think, yeah.
[00:35:00] Morgan Cook: Yeah, that's a very valid thing to look at there.
[00:35:03] Paul Miller: Well, it's funny you suggest that, Marc.
[00:35:07] Paul Miller: I got tasked by the New Zealand government to look at education, how the world is using across the OECD, AI across education.
[00:35:20] Paul Miller: ▶ And there's two common things that all governments across the OECD is doing with AI with education, one of which is using AI that is personalized to each student to be a student assistant, so a teacher aide.
[00:35:44] Paul Miller: So, yeah, like Morgan, I agree, everyone will have their kind of AI that they interact with.
[00:35:52] Paul Miller: But the reality is that that AI will be tuned for where the deficits are for each of those people.
[00:35:59] Marc Juretus: That's right.
[00:36:00] Paul Miller: I think you're on to it, because about a third of the script, we're all ADHD-focused people, and while that's got a lot of upside with certain things, it's got known downside.
[00:36:20] Paul Miller: And with known downside, and an agent that knows your downside, it can then optimize around the things that you're not able to do.
[00:36:29] Paul Miller: Now, the other thing with that education study that I did was you've got this teacher aid that helps every student, because every student's on their own journey, they've got the skills, and they've got the deficits, or a learning difficulty, or a learning style that they like, that they maximize their input from.
[00:36:50] Paul Miller: The other thing is the reporting for teachers, because you need to communicate with education authorities.
[00:36:59] Paul Miller: some of the lifetime know that everyone points for And pretty
[00:37:00] Paul Miller: Parents, other people that are part of the education system, and teachers don't want to have to spend their time being admin workers, just as average workers, sorry, let me just get rid of that.
[00:37:14] Paul Miller: Average workers don't want to do that either.
[00:37:18] Paul Miller: So I think it's those, for me, it's those two skills.
[00:37:23] Paul Miller: Patrick, did you have something to add?
[00:37:26] Patrick Chouinard: ▶ Yeah, basically, yes, they will have to interact with agents, but if you want a mental model that I work with, IT is cyclical, okay?
[00:37:36] Patrick Chouinard: We're always doing the same thing over and over again.
[00:37:38] Patrick Chouinard: Look at how IT got introduced in the business.
[00:37:42] Patrick Chouinard: First, you had mainframe with dumb terminals.
[00:37:45] Patrick Chouinard: Everybody was working off of the same shared machine.
[00:37:48] Patrick Chouinard: Right now, we have our dumb terminal, the application we're using to interact with AI that goes to a centralized machine to do some treatment and return you information.
[00:37:59] Patrick Chouinard: internet.
[00:37:59] Patrick Chouinard: important in and Okay,
[00:38:00] Patrick Chouinard: At the time, most people did not know how to interact.
[00:38:03] Patrick Chouinard: They had the idea that computers were cool, but most didn't know how to use them.
[00:38:08] Patrick Chouinard: A couple of them were specialists and used them heavily.
[00:38:12] Patrick Chouinard: They become the founder of the Microsoft and Apple of this world.
[00:38:15] Patrick Chouinard: Now you're doing the exact same thing.
[00:38:18] Patrick Chouinard: have a bunch of nerds that love to play with those tools, but most people find them cool, but don't necessarily understand them yet.
[00:38:25] Patrick Chouinard: But they will become more and more prevalent, and you're going to move to the PC era where more people will have local models that are going to be personal, personalized, and then we're going to end up restarting the cycle a couple of years from now.
[00:38:42] Patrick Chouinard: ▶ The cycle is getting faster, but structurally it's identical.
[00:38:49] Marc Juretus: Yep.
[00:38:50] Marc Juretus: Yeah, appreciate it, guys.
[00:38:51] Marc Juretus: I started working on slides, but those are like three questions.
[00:38:54] Marc Juretus: was like, let me bounce it off of you guys before I start finalizing what I'm writing.
[00:38:59] Marc Juretus: you.
<!--SEGMENT
topic: Robotics tangent — Tesla Dojo + general-purpose packing robots
speakers: Marc Juretus, Paul Miller, Ty Wells
keywords: Tesla Optimus, Dojo network, continuous-learning across robots, $20-30K general-purpose packing robot, Bezos returning to robotics, less than 5 years to mainstream, Unitree $13K humanoid
summary: Marc points to Tesla + Bezos pushing robotics. Paul cites a manufacturing friend's $20-30K trainable general-purpose packing robot already in supply lines (less than the cost of one employee, 24h operation). Ty: the mechanical part is already there — software is the gating factor and is moving fast — robotics is mainstream in less than 5 years (probably ~2). Marc highlights Tesla Dojo's network-level continuous learning ('teach one robot to fry an egg, all robots know how').
-->

[00:39:00] Marc Juretus: Yeah, different day and age, all I can say is you better adopt.
[00:39:04] Paul Miller: Yeah, it's hard to say what's going to be around in three years as well.
[00:39:10] Paul Miller: You know, if you've got a kid going into college now, yeah, I think having those skills of asking questions, maybe sort of political science, that kind of challenges thinking, or the arts, or I don't know, whatever, philosophy.
[00:39:30] Marc Juretus: And then we have the whole robotics thing.
[00:39:32] Marc Juretus: Like, I'm into investing pretty heavy, so I obviously follow Elon with Tesla and stuff like that.
[00:39:36] Marc Juretus: But now, what's his name, now came out of retirement, Bezos from Amazon, he's getting in that space.
[00:39:42] Paul Miller: Robotics.
[00:39:43] Marc Juretus: So where is that going?
[00:39:45] Marc Juretus: Because if he's coming out to play between those two and, you know, some of other advancements with that, where is that in five years?
[00:39:51] Marc Juretus: I think that's going to be a little longer until it gets better.
[00:39:54] Paul Miller: Well, interesting to say that, I have, I've got a friend of mine that says,
[00:40:00] Paul Miller: ▶ It's in a manufacturing business, and for quite a reasonable cost at the moment, you can get a general-purpose robotics tool that does packing and handling on the supply line for about $20,000 $30,000, and the cost of those general-purpose trainable tools are getting pretty crazy now.
[00:40:22] Paul Miller: Now it's reducing and reducing, and the ability to be able to challenge it, train it, is making it approachable for many people instead of workers.
[00:40:33] Paul Miller: You can have them 24 hours a day working and packing all your boxes and stuff for something that's less than the cost of an average employee.
[00:40:42] Ty Wells: ▶ I think robotics is definitely going to be way less than five years, Marc.
[00:40:50] Ty Wells: You know, the software is driving that.
[00:40:52] Ty Wells: I think the mechanical part of it, it's already there.
[00:40:57] Marc Juretus: Oh, yeah.
[00:40:58] Ty Wells: think it's the software that's...
[00:41:00] Ty Wells: know, I'm going to drive it because that's more spatial, right, like being aware of surroundings, you know, something slightly off and so forth.
[00:41:08] Ty Wells: So I think the software is going to get there.
[00:41:10] Ty Wells: Software is moving way faster than the mechanical part of it, but less than five years for sure.
[00:41:17] Ty Wells: I would say more like two.
[00:41:19] Marc Juretus: Well, I'm saying smooth and it's a part of our day to day.
[00:41:23] Marc Juretus: Like I follow that with a few stocks that I invest in with that.
[00:41:26] Marc Juretus: But just like, for example, I don't want to take too long on this call, but like with Tesla.
[00:41:29] Marc Juretus: ▶ But his robots, because it's on that dojo network, you teach your robot how to fry an egg because they're all on that same network.
[00:41:36] Marc Juretus: Now all the robots know how to fry an egg.
[00:41:38] Marc Juretus: So it's continuous learning across all of the robots.
[00:41:42] Marc Juretus: It's like, where is that going to go?
[00:41:43] Marc Juretus: These robots are learning more each day.
[00:41:45] Marc Juretus: just, you know, it's going to be an interesting world in about three to five, but I agree with you.
[00:41:50] Marc Juretus: They'll be more prevalent in two years used.
[00:41:55] Paul Miller: Cool.
[00:41:56] Marc Juretus: Thank you.
[00:41:57] Marc Juretus: Thank you everybody.
[00:41:58] Marc Juretus: Sorry for taking too much time.
[00:42:00] Paul Miller: That problem, that was good, good stuff.
[00:42:03] Paul Miller: Ty, you're next.
<!--SEGMENT
topic: Ty — FaceGate web-native Face ID auth update
speakers: Ty Wells, Marc Juretus
keywords: FaceGate, web-native Face ID, drop-in authentication, time-and-attendance for guards, multi-user-on-single-device clock-in, screen recording feedback widget
summary: Ty's FaceGate site is up — drop-in Face ID web-native authentication. Built primarily for guard shifts (multiple guards clocking in/out on a single shared device for time-and-attendance). Ty mentions his standard practice of embedding a screen-recording-with-voice feedback widget on every test app for bug capture.
-->

[00:42:06] Ty Wells: Hey, guys.
[00:42:07] Ty Wells: Yeah, I saw that, Patrick, that robot for that Unitree for 13 grand, under 13 grand [tool:Unitree].
[00:42:16] Ty Wells: Just to cap off what Marcus was saying is that it is, I mean, look what Patrick did over the weekend.
[00:42:25] Ty Wells: Let's just use that as an example, right?
[00:42:27] Ty Wells: What we present every week, it's just crazy.
[00:42:31] Ty Wells: Today, I was supposed to present FaceGate, but I have been swamped [tool:FaceGate].
[00:42:35] Ty Wells: But the site is up.
[00:42:37] Ty Wells: You guys can go and test it out yourself and actually give me some feedback.
[00:42:42] Ty Wells: There's one thing I'm going to add on there.
[00:42:43] Ty Wells: I don't think I have.
[00:42:45] Ty Wells: Let me just double check, see if I have the feedback option on there.
[00:42:51] Ty Wells: I do, I'll send the link.
[00:42:52] Ty Wells: Otherwise, just give me after this call to do it.
[00:42:56] Ty Wells: I just want to make sure because that's the way you.
[00:42:58] Ty Wells: don't want add that message.
[00:42:58] Ty Wells: Let use Remember
[00:43:00] Ty Wells: ▶ No, don't have that on there yet, but what it does is it allows you to record your screen.
[00:43:07] Ty Wells: I put that on all my apps that I'm testing.
[00:43:11] Ty Wells: It's not there.
[00:43:12] Ty Wells: I haven't put the link there, but you'll see a little purple icon.
[00:43:15] Ty Wells: You can give feedback, but it'll record the screen, what you're doing.
[00:43:18] Ty Wells: That's how we track the bugs, and you can use your voice to record it and then send it off, and that way I can fix whatever issues you run into.
[00:43:26] Ty Wells: But it's pretty solid.
[00:43:28] Ty Wells: It's Face, for those that weren't here last week, it's Face ID recognition [tool:Face ID].
[00:43:33] Ty Wells: I don't know if I shared anything last week that's web-native, so you can drop it as an authentication system into any platform.
[00:43:42] Ty Wells: And the reason I need it is because...
[00:43:45] Ty Wells: Did I explain this last week?
[00:43:47] Ty Wells: I don't want to reiterate.
[00:43:49] Ty Wells: Okay.
[00:43:49] Ty Wells: I just needed it for the guards that use a single device, multiple guards that clock in and clock out for time and attendance, and so I needed a way for them to easily do that and then also access their...
[00:44:02] Ty Wells: I'm going to drop the URL after I add the feedback, because I want that there, so you can send me feedback if you run into any issues.
[00:44:11] Ty Wells: Okay.
[00:44:13] Marc Juretus: Definitely.
[00:44:14] Ty Wells: That's all I've got.
[00:44:15] Ty Wells: Short day for me.
[00:44:17] Marc Juretus: Thanks for the cloud material, too, Ty, by the way.
[00:44:19] Marc Juretus: I appreciate that, man.
[00:44:20] Ty Wells: Oh, yeah.
[00:44:21] Ty Wells: Well, I wish I had that cloud.
[00:44:23] Ty Wells: I think I dropped the link for that, that cloud anthropic architect tool so you can learn about their architecture.
[00:44:32] Ty Wells: It would have been good now that I have the actual code base.
[00:44:37] Ty Wells: I can then now throw that in there.
[00:44:39] Ty Wells: That gives me more.
[00:44:40] Ty Wells: I wish I had that when I was going through all of their material.
[00:44:43] Ty Wells: Could have saved me some time, but that's actually solidifying what my understanding of how they're doing it.
[00:44:49] Ty Wells: I actually can see how it's being done, which is wonderful.
[00:44:54] Paul Miller: Brilliant.
[00:44:55] Paul Miller: Thanks, Ty.
[00:44:56] Paul Miller: Scott?
<!--SEGMENT
topic: Scott's AI News Digest — RSS aggregator, Haiku, daily blog with semantic search
speakers: Scott Rippey, Juan Torres, Paul Miller
keywords: AI News Digest email, RSS aggregation, Haiku for cheap summarization, story-thread continuity context, Resend email tracking, blog with RAG semantic search, key takeaway / why it matters / practical takeaway sections, banking-sector research-analyst footnote pattern
summary: Scott shares his AI News Digest: combines RSS feeds, runs them through Haiku (Sonnet was overkill, Haiku is super cheap and capable enough), de-dupes story threads with prior-context awareness, and now also publishes as a blog with RAG-backed semantic search. Each story has 'key takeaway / why it matters / practical takeaway / sources'. Juan suggests consolidating sections into one report with Chicago-style footnotes (the banking-sector research-analyst pattern Juan used previously). Scott prefers stories broken out for easier digestion.
-->

[00:44:59] Scott Rippey: Not too many things.
[00:45:00] Scott Rippey: Thanks.
[00:45:02] Scott Rippey: I've been still working on versioning that Ironcloth thing.
[00:45:05] Scott Rippey: I've been going back and forth with Patrick a little bit on that.
[00:45:08] Scott Rippey: Actually, Patrick, I think I have to send you the complete 4.2 now.
[00:45:11] Scott Rippey: don't think I've sent you one since three, but I actually have, you know, while I'm waiting for my Mac Mini, I actually do have a marketing friend of mine that wants to pay me to set this up, and he actually bought like a used M1 with 32 gigs.
[00:45:27] Scott Rippey: So there's a possibility I could be running through a test, like before I even get mine and rope you into that.
[00:45:33] Scott Rippey: I might be able to see a run through just to see what happens, you know?
[00:45:37] Scott Rippey: So I'll let you know, you know, what happens with that, because I'll probably get on some sessions with him to do that remotely.
[00:45:43] Scott Rippey: He's not in my area, so he's up in Michigan.
[00:45:46] Scott Rippey: But other than that, I think you guys that wanted the AI News Digest have been getting it.
[00:45:53] Scott Rippey: I did.
[00:45:57] Scott Rippey: Oh, let's see.
[00:45:58] Scott Rippey: got a request to share my screen.
[00:46:02] Ty Wells: God, forgot to drop my email.
[00:46:03] Ty Wells: I'm going to drop it the chat.
[00:46:04] Ty Wells: can add me to that.
[00:46:06] Ty Wells: Yep.
[00:46:06] Scott Rippey: Perfect.
[00:46:06] Scott Rippey: I was going show you guys, too.
[00:46:07] Scott Rippey: I added something that was kind of nice that I didn't, that I did, I think, yesterday.
[00:46:13] Scott Rippey: There we go.
[00:46:14] Scott Rippey: I can share my screen.
[00:46:16] Scott Rippey: All right.
[00:46:18] Scott Rippey: So now we're doing that.
[00:46:21] Scott Rippey: I actually, you guys might have noticed I sent out two the other day because I broke the attachment with the voice on it because I actually was messing with Resend and I wanted to add I actually start seeing if you guys were getting it, making sure they weren't bouncing back and they were getting open and stuff [tool:Resend].
[00:46:34] Scott Rippey: So that actually was a pretty cool feature I put in there, but so I sent it twice and fixed that.
[00:46:39] Scott Rippey: But I did add, and I'll drop the link in here.
[00:46:42] Scott Rippey: I added, I mean, I like getting emails.
[00:46:45] Scott Rippey: It's great to have it, but if you ever want to, I created a blog out of this.
[00:46:48] Scott Rippey: Now it's doing both.
[00:46:51] Scott Rippey: And so now that you can actually go through there and browse every single one and then the new ones are going to have audio on it now because I wasn't keeping that before.
[00:46:59] Scott Rippey: So you can actually, actually,
[00:47:00] Scott Rippey: Like see it at a glance and go through and browse, but it also does have semantic searching because this is a rag database that I've done with this [tool:RAG].
[00:47:08] Scott Rippey: So kind of a nice little thing.
[00:47:10] Scott Rippey: I'll drop it in there in case anybody wants to just search or browse through stuff, but I'm just going to let that keep history.
[00:47:15] Scott Rippey: I'm going to let that just build.
[00:47:17] Scott Rippey: I might end up putting some AdSense on it or something.
[00:47:19] Scott Rippey: Ryan was giving me that idea just because it's a good site that I could have out there for that.
[00:47:25] Scott Rippey: But that's about it.
[00:47:28] Scott Rippey: If anybody else wants that AI Digest, I'll drop your email in there and you'll get that with the audio recording that you can listen to as well if anybody missed that.
[00:47:37] Juan Torres: Hey, Scott.
[00:47:39] Juan Torres: Is the current agentic system for news generation set up to create a report for each link?
[00:47:47] Juan Torres: Is that how you set it up?
[00:47:50] Scott Rippey: No.
[00:47:50] Scott Rippey: So what I'm doing is I have RSS feeds that I'm combining and what I'm doing is I've got a system prompt and I'm just using Haiku [tool:RSS] [tool:Haiku].
[00:47:57] Scott Rippey: This thing's so cheap and it does so well.
[00:47:58] Scott Rippey: Like I did not need Sonnet for
[00:48:00] Scott Rippey: ▶ I mean, Haiku did a great job of, it's just consolidating news sources, and it won't repeat a story or show it more than once, but it will keep doing development, because a lot of times there's developments on these, so like you'll see the kind of threads over days where like the stories continue to develop, and I have some of that context, not just the titles being sent to Haiku, so it knows, hey, you we've already kind of touched on this, so you don't need to repeat that, because you might see the same news thing different days in different, you know, feeds, so it's set to not be too repetitive.
[00:48:28] Scott Rippey: But all I'm doing is just combining, I'm just summarizing, combining information from RSS feeds, because I was tired of reading emails all over the place for my AI news, so that's all this is.
[00:48:37] Juan Torres: ▶ So what I was mentioning more than anything, it was like, because I see the key takeaways, and then why it matters, and then practical takeaway, right?
[00:48:48] Juan Torres: So, and then I see the source, so I'm imagining that each one of those sections is kind of like a summary of the link article that it has as a source.
[00:48:56] Scott Rippey: Is that correct?
[00:48:58] Scott Rippey: Yeah, so, well...
[00:48:59] Scott Rippey: so...
[00:49:00] Scott Rippey: Each one of those could have one source, have two, could have four sources, it is combining all of the information and it is basically creating those sections based on however many sources it had for that story.
[00:49:11] Scott Rippey: A lot of times there's two or three articles talking about the same thing and I'm just kind of compiling all the information so I don't miss an important fact on something.
[00:49:20] Juan Torres: Have you thought of combining all of them into one report?
[00:49:26] Scott Rippey: It is one report, it comes out daily.
[00:49:29] Juan Torres: But I mean like, because when I used to be a research analyst, I will have like several links, like here's like maybe six, eight of them, right?
[00:49:39] Juan Torres: And I will just create one report out of them instead of like segmenting them.
[00:49:43] Juan Torres: So what I'm thinking as a previous research analyst is you just, you know, create a key takeaway sections of all eight, ten sources.
[00:49:54] Juan Torres: And then you, you can create a summary paragraph and then you get into the details of each one of them.
[00:49:59] Juan Torres: them again, but if
[00:50:00] Juan Torres: ▶ And actually, in one of the agentic systems for news generations in the banking sector, what I did is that for each one of our paragraphs, I just created a footnote or like a kind of like a Chicago-style hyperlink number that you can click on basically next to the sentence where we end it.
[00:50:21] Juan Torres: And it was something that I thought it was a good summarization of everything.
[00:50:27] Scott Rippey: Yeah, I like to have it broken up for me.
[00:50:30] Scott Rippey: That's just my preference.
[00:50:31] Scott Rippey: I actually prefer not that way, even though that's cool if other people like that.
[00:50:35] Scott Rippey: I like having my stories broken out.
[00:50:37] Scott Rippey: It's easier for me to digest and focus on something.
[00:50:39] Scott Rippey: So, yeah, that's just my preference.
[00:50:42] Paul Miller: Scott, have you thought about feeding in some of the feedback from X?
[00:50:48] Paul Miller: So, if the community's out there talking about some of the news that you've got, you can seed it with what's being discussed on X as well.
[00:50:59] Scott Rippey: I'm just trying to keep
[00:51:00] Scott Rippey: Make this lean and mean, I'm not trying to make this anything, I have a tendency to want to make it like something crazy and that would be all cool, but this is literally like, I just need 10-15 minutes a day to keep on top of like all the major stuff and it's, I'm not, so that's very, very focused purpose for this without getting too in the weeds.
[00:51:18] Paul Miller: Yeah, I think I would love, I'd love to get on it.
[00:51:22] Paul Miller: Can you share your URL so we can add our email addresses?
[00:51:29] Scott Rippey: You'll, you'll, you'll have to send me the email to add for the digest in the chat here and I'll add you in, but I'll send the, also the blog so you guys can browse the blog too.
[00:51:37] Scott Rippey: But yeah, I don't have a sign up on there.
[00:51:38] Paul Miller: Okay.
[00:51:39] Scott Rippey: Yeah, I'm kind of keeping it to people I know, but I put the blog out there publicly.
[00:51:43] Paul Miller: Okay.
[00:51:45] Paul Miller: I'll send it.
[00:51:47] Scott Rippey: I'll drop that at you.
[00:51:48] Scott Rippey: But that's all I got.
[00:51:49] Paul Miller: Brilliant.
[00:51:52] Paul Miller: Thanks, Scott.
[00:51:54] Paul Miller: We'll hand over to Ryan.
<!--SEGMENT
topic: Ryan — website rebuild + hedge-fund expense software + ISO/SOC2 path
speakers: Ryan C, Paul Miller, Jake Maymar
keywords: creative agency website rebuild, 3D scroll animations, hedge-fund expense management software, ancient accounting software replacement, ISO compliance vs SOC 2 vs HIPAA, Vanta, strategic cloud-partner piggyback, Xero integration, accountant background, £600/user pricing for hedge-fund vertical
summary: Ryan rebuilt his creative-agency website with 3D scroll animations. Bigger project: a friend just promoted to FD of a London hedge fund asked Ryan to replace their ancient expense-management accounting software. Ryan plans ISO compliance (lower bar than SOC 2 / HIPAA) since he integrates with Xero rather than building statutory accounts. Jake suggests Vanta for compliance tooling, AWS/Azure/Google Cloud strategic partnerships (defense → Azure, financial → likely Azure), full-time CISO + DevOps for that vertical. Ryan plans £600/user for hedge fund vertical — niche, small (20-30 users) but lucrative.
-->

[00:51:56] Paul Miller: How's it going, Ryan?
[00:51:58] Ryan C: Music has been.
[00:51:59] Ryan C: Music has been.
[00:52:00] Paul Miller: It's while since I've been able to speak on one of these things where I haven't just had you guys on in the background and then fallen asleep while listening to it.
[00:52:07] Ryan C: It's really late here, and then I get berated by Scott that he said things on here that I needed to hear and was snoring away when he said them.
[00:52:18] Ryan C: We need to get him going earlier.
[00:52:21] Ryan C: What have I been doing?
[00:52:22] Ryan C: Christ, too much.
[00:52:24] Ryan C: Loads of different projects going on, which has been good.
[00:52:27] Ryan C: It's good to get back on one of these, actually, properly.
[00:52:31] Ryan C: I decided on a whim on Sunday evening that I'd redo my whole website for my creative agency.
[00:52:38] Ryan C: So that's essentially been what I've been doing till four o'clock in the morning, the last three.
[00:52:45] Ryan C: It's really addictive when you get going on something, especially when it's something for your business.
[00:52:49] Ryan C: It's quite fun.
[00:52:50] Ryan C: So I've been mucking around with 3D animated websites [tool:3D scroll animations].
[00:52:54] Ryan C: So when you do scroll, there's like scroll animations and stuff going down the page.
[00:52:58] Ryan C: And it handles it surprisingly well.
[00:53:00] Ryan C: So I've designed something pretty cool.
[00:53:02] Ryan C: It should be done by next week's session, so I'm just devving it locally at the moment, and I'm not on the machine that I'm devving it on, so otherwise I would share what I've done so far, but I'm just working my way through it and improving it, tweaking it, making it better.
[00:53:20] Ryan C: And then I've got a couple of big things coming up.
[00:53:25] Ryan C: I've managed to get a, one of friends has just been promoted to being the financial director of a massive hedge fund in London, and he's got some accounting software that is ancient and rubbish that they use to do various expenses related things.
[00:53:46] Ryan C: So he's asked me to come up with a bit of software to essentially do it better.
[00:53:53] Ryan C: Obviously, the fun thing, and I'll, I'll have a chat with Brandon about this next time he's on one of these and probably ping him an email.
[00:53:59] Ryan C: Is Yeah.
[00:53:59] Ryan C: Is Yeah.
[00:54:00] Ryan C: You need to be ISO compliant and potentially HIPAA compliant as well because you're dealing with obviously multi-million, sometimes multi-billion pound transactions, accounts, sensitive information that can move markets, that kind of stuff [tool:ISO compliance].
[00:54:14] Ryan C: So I'm getting into the weeds of all of that at the moment with just doing like early stage research, figuring out what I need to build, where I need to build, all that fun stuff.
[00:54:23] Ryan C: So that could be huge because we'll test pilot it with his hedge fund and hedge funds are a tiny little community and they will talk.
[00:54:32] Ryan C: So if we get something that literally kicks the crap out of this bit of software that exists, that could be a real money spinner, hopefully, but I'm along with that.
[00:54:41] Paul Miller: Ryan, you might want to get some feedback from Jake and there's a few other guys on here doing the HIPAA compliant stuff.
[00:54:49] Paul Miller: Just for some ideas on some things because we did have a session talking about back-ends and HIPAA compliance.
[00:55:00] Paul Miller: And what you need to do to do that about a month ago.
[00:55:05] Paul Miller: Jake, did you have any suggestions where Ryan might want to start with getting his app authenticated and protected?
[00:55:17] Jake Maymar: Yeah.
[00:55:18] Jake Maymar: I mean, you can do like SOC 2 Type 1 is sort of that process [tool:SOC 2 Type 1].
[00:55:23] Jake Maymar: There's a whole bunch of different things.
[00:55:25] Jake Maymar: I know Brandon's mentioned Vanta in the past [tool:Vanta].
[00:55:28] Jake Maymar: That's kind of the go to.
[00:55:30] Jake Maymar: There's a couple different solutions, third party solutions for that.
[00:55:34] Jake Maymar: ▶ You can also piggyback on to partners, you know, so if there's already a partner that's SOC 2 compliant and you can host using their system, that's another way to do it.
[00:55:49] Jake Maymar: Common ways is, you know, do that, have a strategic partnership like incubator or or uh
[00:56:01] Jake Maymar: Like, pick sort of what cloud provider you want, whether it's AWS, Azure, or Google Cloud, and each one of them have their own sort of setup, and you'll probably want to research and see which preference they have.
[00:56:14] Jake Maymar: If they're financial, they're probably going to be Azure, but, you know, it just depends.
[00:56:20] Jake Maymar: ▶ You know, everyone uses everything, so, you know, there's not a definite thing, but I think strategic partnerships, especially with, like, hedge funds, I think is a really good thing, because they often have them, and they often have preferences of technology stacks.
[00:56:38] Jake Maymar: So they're like, we want to do Google Cloud, or we want to do Azure, or we want to do AWS.
[00:56:45] Jake Maymar: Now, if it's, like, a lot of defense companies like Azure, like, that's kind of their go-to.
[00:56:53] Jake Maymar: So it might be similar for financial.
[00:56:55] Jake Maymar: Other catch is, though, is cybersecurity is getting pretty...
[00:57:00] Jake Maymar: It's wild.
[00:57:00] Jake Maymar: I mean, I'm sure you saw the hacks and the stuff going on.
[00:57:04] Jake Maymar: ▶ You might want to do some research on that and make sure you have a very qualified CISO security officer as well as a DevOps, full-time DevOps person, because getting into, I mean, Juan knows this, getting into, you know, that financial vertical, it's, there's a lot of compliance, like a lot of stuff.
[00:57:30] Jake Maymar: So, yeah, there's a lot of regulation.
[00:57:32] Jake Maymar: Actually, it's, I think, kind of the hardest, but it was also the most advanced in machine learning and also now in AI.
[00:57:40] Ryan C: Yeah, well, I've got a financial background, so I've got a, I'm a qualified accountant.
[00:57:44] Ryan C: So, I understand, I understand a lot of the stuff that comes around that, because I had to, to get my, my qualifications.
[00:57:51] Ryan C: Oh, that's great.
[00:57:52] Ryan C: it's a bit of an edge on that front.
[00:57:54] Ryan C: It's more just the compliance on the software side that I just got, I've done a ton of research.
[00:57:59] Ryan C: I don't think I need to.
[00:58:00] Ryan C: If as far as HIPAA or even SOC, I think I just need to be ISO compliant for what we're doing, because I'm not building statutory accounts.
[00:58:07] Ryan C: If I went that far, because it could do that, I could do that within the app, because that would probably solve an even bigger problem.
[00:58:14] Ryan C: But it's more just going to be around expenses and then linking into something like Xero, which is going to build the statutory account [tool:Xero].
[00:58:20] Ryan C: So I think I can get away with ISO, which obviously is a lesser of all of those things to have to worry about.
[00:58:25] Jake Maymar: Yeah, and to be fair, it's a gray area too, right?
[00:58:28] Jake Maymar: Like, if you're basically building it in a smart way, you can avoid a lot of the audit trips, right?
[00:58:37] Jake Maymar: And the pen testing and all that other stuff, and that's where it gets kind of crazy.
[00:58:41] Jake Maymar: But you're right, if you go ISO, that's a much lower bar.
[00:58:46] Jake Maymar: And yeah, especially if you're really smart about the architecture, yeah, you should be able to do that.
[00:58:52] Ryan C: ▶ And I read that you can get relevant insurances as well, because with ISO, you can go, I'm aware that that's an exploit, and I'm going to miss
[00:59:00] Ryan C: I'm against that by getting an insurance policy that if someone does that, that will pay out.
[00:59:04] Jake Maymar: Yeah, that's the best way to do it, too.
[00:59:07] Ryan C: With the trickiest stuff that is going to require a lot of time or money, to start off with that may be where we land, and then I'll patch those things as I get user base and money coming in from that perspective, probably.
[00:59:19] Paul Miller: Well, good on you, Ryan, getting involved in such a slow-moving conservative space, because often the IT teams in these banks are blimmin' useless in terms of being agile and coming up with this stuff.
[00:59:35] Ryan C: I don't think I'm going to target banks, because I admit I'm in a fortunate position, because as they say, it's about who you know, not generally what you know.
[00:59:43] Ryan C: Exactly.
[00:59:44] Ryan C: luckily, I grew up with this guy, and he's, yeah, the FD has just quit, and he's been put into the FD position at quite a young age at a big old hedge fund.
[00:59:56] Ryan C: So now he calls the shots, really, from that perspective.
[01:00:00] Ryan C: ▶ So, you know, I'm lucky in that I'm probably going to get to be able to test with his hedge fund, and then we're going to probably just really hone in on the hedge funds because there's obviously an absolute shed load of money in that thing, and you've got, you know, hedge funds tend to be between 20 to 30 people running them, you do a pay per user model, you know, you can charge like £600 a month per user for stuff like this, just specifically in the hedge fund niche, they pay obscene amounts of money for for software.
[01:00:31] Ryan C: So, yeah, I think, I think that'll, do me.
[01:00:34] Ryan C: I just need enough money to retire to Barbados and, you know, pay the bills.
[01:00:38] Paul Miller: Yeah.
[01:00:38] Paul Miller: Or, or, or, join Ty and, where, where Ty often is.
[01:00:45] Ryan C: And I've got the awesome stuff running through screen software that I've been kind of adding stuff to, the social software I've been adding stuff to.
[01:00:55] Ryan C: Um, and then I've got a few other websites on the go.
[01:00:58] Ryan C: That's really the big stuff.
[01:01:00] Paul Miller: Great stuff.
[01:01:01] Paul Miller: It's those industry verticals are the way to go.
[01:01:05] Paul Miller: If you can get in that space and have a deeper discussion with someone that's right in the middle of it, that it's most of the time it's very practical problems, but having another person thinking outside the box is great.
[01:01:23] Ryan C: The actual application itself is a super simple problem to fix.
[01:01:27] Ryan C: It's just all the stuff that comes around that enables them to actually use it in the first place is the problem, rather than, for me anyway, I can build the thing they want.
[01:01:38] Ryan C: It's just all the other stuff.
[01:01:41] Ryan C: All the non-fun stuff.
[01:01:42] Ryan C: Cool stuff.
[01:01:45] Paul Miller: Okay, Ryan, thanks for that.
<!--SEGMENT
topic: Juan — managing difficult clients + diffusion-model project hardening
speakers: Juan Torres, Paul Miller, Patrick Chouinard, Ryan C, Morgan Cook, Jake Maymar
keywords: non-technical client management, project-manager-vs-engineer responsibilities, FinOps cost control, diffusion model project, private subnet, encrypted resources, dev/staging/prod automation, AI as email-emotion buffer, Whisperflow, blunt-then-rewrite prompt pattern
summary: Juan vents about a client who blames his engineers for issues caused by the project manager's missing responsibilities — the third DevOps engineer cycled out for the same reason. On his own diffusion-model project, Juan's not aiming for SOC 2 (FinOps cost of full login auditing too high) but everything's in private subnets with encrypted comms; one-click dev→staging→prod automation is in flight. The thread pivots to AI as an email-emotion buffer: Patrick, Ryan, Morgan, and Jake all admit running drafts through Claude/Copilot to strip emotion before sending. Patrick: 'Every email goes through Claude. My blood pressure thanks me.'
-->

[01:01:48] Paul Miller: Juan, anything to add and anything, what's going on in your space?
[01:01:57] Juan Torres: Well, trying to...
[01:02:01] Juan Torres: Manage, you know, customers.
[01:02:04] Juan Torres: What is it called?
[01:02:06] Juan Torres: Not, you know, lack of proper management, right?
[01:02:12] Juan Torres: It's one of the skills that you have to handle, you know, when they're trying to, like, point your finger and it's like the responsibility of the product manager to manage things.
[01:02:21] Juan Torres: ▶ So I had to, right now, before getting to a call, I just had to set my client straight and tell them, hey, this is the responsibility of the project manager to resolve issues if his endpoints are not properly passing filtering information to my agentic system, he's the one that is supposed to handle it.
[01:02:42] Juan Torres: So I had a, you know, conversation, a necessary conversation with him, just because they don't A lot of the times, the non-technical clients, they don't know what's going on.
[01:02:58] Juan Torres: And, and they, they
[01:03:00] Juan Torres: He let emotions take the best out of their rationale and they try to, you know, take blame on people that they're not supposed to.
[01:03:10] Juan Torres: In fact, I would say that this client got rid of, I mean, one of the best front-end engineers that I know because this front-end engineer did DevOps and knew how to do DevOps.
[01:03:25] Juan Torres: And then he has been cycling through the DevOps.
[01:03:29] Juan Torres: He got rid of her, then he got another one, they got rid of her, and then he's on his third one.
[01:03:38] Juan Torres: And so he has, you know, like, you know, he goes into the psychosis moments, right?
[01:03:45] Juan Torres: So, and I've been able to survive because I've done a pretty good job.
[01:03:50] Juan Torres: And, like, I am, like, crucial to the project, so even if he goes through a psychosis, he knows that he cannot get rid of me.
[01:03:57] Juan Torres: Um, but, uh...
[01:03:59] Juan Torres: uh...
[01:03:59] Juan Torres: ...
[01:04:00] Juan Torres: And, but yeah, no, it's just really interesting having to handle, you know, these people.
[01:04:10] Juan Torres: And then on the other bright side, I'm on the project with the diffusion models.
[01:04:16] Juan Torres: ▶ I am trying to be as disciplined as I can, and having, I'm not going to say this is a SOC 2 compliant application, because there's a lot of the login mechanisms that I'm not taking track of, like, particularly when developers log in, when users log in, just because that would take, I would have to carry some FinOps to be able to account for, like, all the costs that having login information, you know, is going to cost on my project in terms of having it saved in my S3 bucket.
[01:04:51] Juan Torres: So, in that sense, it's not very SOC 2 compliant.
[01:04:55] Juan Torres: But networking, it's pretty solid.
[01:04:58] Juan Torres: Everything is...
[01:04:59] Juan Torres: Uh...
[01:04:59] Juan Torres: Uh...
[01:04:59] Juan Torres: Uh...
[01:05:00] Juan Torres: That it's not supposed to be client forwarding.
[01:05:02] Juan Torres: It's in a private subnet.
[01:05:03] Juan Torres: The communication between all the resources is encrypted.
[01:05:07] Juan Torres: ▶ My connection to the resources within AWS is encrypted.
[01:05:12] Juan Torres: So there's just no way for an incompetent hacker to try to hack into my system.
[01:05:21] Juan Torres: ▶ And I'm trying to regiment a strict, disciplined deployment pipeline by essentially having my development environment, being the development environment, having my staging environment, just being the proper EC2 instance that I'm working with, and then automating that towards the deployment of the application into an automated skill group when the application is ready to go.
[01:05:48] Juan Torres: And I'm trying to automate the whole process, like development, staging, and production, with one click of the button.
[01:05:57] Juan Torres: um
[01:06:00] Juan Torres: And what else?
[01:06:01] Juan Torres: I think that's it.
[01:06:02] Paul Miller: Yeah.
[01:06:04] Paul Miller: Cool stuff.
[01:06:05] Paul Miller: Do you find, I was thinking about what you were saying with the user side of things, and I don't know, dealing with those challenging users or dealing with the users that are just the real pain in the  types, right when you're trying to juggle all sorts of cool stuff, do you have, do you have your either at a minimum, do you have your own sort of project, space in Claude where you're dealing with those specific users or you have an outward-focused user AI entity that you're running in a Claude Code CLI that you're feeding copies of the conversations you're having with the user?
[01:06:48] Paul Miller: Because I don't know, like many of you, I've got a little Limitless device recording all conversations, capturing some of the  that goes on with calls that I get.
[01:06:59] Paul Miller: Um...
[01:07:00] Paul Miller: Or emails, just getting it to read the emails from certain customers so it's proactively removing the emotion that you need to be able to put in with dealing with these fools.
[01:07:14] Paul Miller: Is that part of your focus, Juan?
[01:07:19] Juan Torres: I try to be as disciplined as I can and face-forward client discomfort, right?
[01:07:26] Juan Torres: So I don't create those buffers.
[01:07:32] Juan Torres: But I try to give people the benefit of the doubt at the beginning to see if it's really an issue and try to ameliorate it.
[01:07:44] Juan Torres: But after seeing a pattern of just lack of leadership in the project, that's when I have to really put on a wall and tell them, hey, this is not me.
[01:07:58] Juan Torres: That you have to really talk to me
[01:08:00] Juan Torres: Project Manager or deal with it yourself because you're just basically shooting yourself in the foot by not actually like facing the actual issue and then not even facing the actual issue, not willing to try to understand what the issue is, right?
[01:08:14] Juan Torres: Because I understand you're not a technical expert and to some extent you shouldn't be because you're leading that project to your project manager to be able to manage like contradictions within the code, within the software engineering, within the architecture.
[01:08:29] Juan Torres: So don't get your AI, you know, engineer to try to resolve issues above his pay grade.
[01:08:36] Juan Torres: So in a sense, has like, it's a contradiction between inability to listen and, you know, inability to learn, right?
[01:08:45] Juan Torres: So that's one of the things.
[01:08:47] Juan Torres: So I just, you know, after benefit of the doubt, I just go for my gut feeling and, you know, tell him what he needs to listen to.
[01:08:55] Paul Miller: Patrick?
[01:08:55] Paul Miller: Patrick?
[01:08:56] Patrick Chouinard: Well, there, that's something that...
[01:09:00] Patrick Chouinard: ▶ Paul, when you said that you use AI to filter, yes, yes, definitely, and believe me, Juan, do that, it's going to be a miracle for your blood pressure, because now there's not a single email that goes from my desk that hasn't gone through Claude, because now I have no filter anymore.
[01:09:21] Patrick Chouinard: I just tell Claude, I read the email, tell Claude, like, tell that effing moron that I'm as blunt as I want, and Claude rewrites it, then he writes a perfectly politically correct email, exactly the tone that needs to land perfectly with the user, and my blood pressure doesn't run up anymore.
[01:09:42] Ryan C: I'm I'm not the only one doing that, Patrick.
[01:09:44] Ryan C: Every time I'm some idiot, I'm like, this  moron, just deal with this, give me something that I can actually send back to them.
[01:09:52] Patrick Chouinard: Exactly.
[01:09:53] Paul Miller: At any time of day or night.
[01:09:57] Morgan Cook: My business partner and I used to do that, we would write.
[01:10:00] Morgan Cook: ▶ Write the email that you want to write to get the emotion out of the way, and then rewrite it so that you can send it appropriately.
[01:10:05] Morgan Cook: And now we don't have to do that no more.
[01:10:06] Morgan Cook: We got Claude.
[01:10:07] Morgan Cook: That's perfect.
[01:10:08] Patrick Chouinard: Exactly.
[01:10:08] Patrick Chouinard: Exactly.
[01:10:09] Patrick Chouinard: I mean, it's to the point where even in teams, sometimes it's Claude or Copilot that actually writes the message.
[01:10:18] Jake Maymar: ▶ And it's interesting on the leak, they revealed that they're actually, they detect if you're basically cussing at it, mostly out of frustration, but they actually detect if you're cussing at it and, and they sort of monitor it and try and understand what, what the context is.
[01:10:36] Jake Maymar: So, you know, cause I mean, that's just a normal way of talking to systems as well.
[01:10:42] Patrick Chouinard: There must be a couple of server rackets.
[01:10:46] Ryan C: They've got, they've got a  stack of hard drives with my, uh...
[01:10:50] Patrick Chouinard: mean, I'm pretty sure there's a couple of, uh, racket and tropic that has targeted that says, talk to this guy's user.
[01:10:57] Patrick Chouinard: .
[01:11:00] Juan Torres: I'll think about the buffers.
[01:11:03] Patrick Chouinard: Honestly, it's liberating.
[01:11:06] Patrick Chouinard: You're not going to want to do it any other way anymore because you can truly speak your mind exactly how you intend it, and you know it's never going to get you in trouble.
[01:11:16] Paul Miller: Brilliant.
[01:11:17] Paul Miller: Thanks, Juan.
<!--SEGMENT
topic: Morgan — quick week update + constellation graph tooling
speakers: Morgan Cook, Patrick Chouinard, Ty Wells
keywords: Heritage Plot county data delay, GIS data waiting, week of physical labor, constellation graph implementation, superpowers brainstorming, front-end-designer skill, 7 parallel projects
summary: Morgan spent the week on physical labor (rental property repairs). Heritage Plot is blocked waiting on county GIS data (county has its own IT issues). Asks Patrick what tool he used for the lab-website constellation graph — Patrick: superpowers brainstorming + front-end-designer skill, with a JS library underneath for the graph render itself.
-->

[01:11:19] Paul Miller: Morgan, you're up.
[01:11:21] Paul Miller: What's happening in your world?
[01:11:24] Morgan Cook: Yeah, last week I spent a lot of time doing my physical labors.
[01:11:29] Morgan Cook: My property manager has a couple of rentals that became vacant and needed some repair work.
[01:11:36] Morgan Cook: So I spent the past weeks doing construction and repair work.
[01:11:41] Morgan Cook: So I'm back onto my software side of things right now.
[01:11:44] Morgan Cook: So it'll be good this week.
[01:11:45] Morgan Cook: Hopefully I make some more progress.
[01:11:47] Morgan Cook: ▶ Heritage plot is moving along.
[01:11:49] Morgan Cook: I finally made contact again with the county that is requesting that, and they are suffering some other IT issues, so I can't get the GI.
[01:11:59] Morgan Cook: about about have in We go to www.cmsmit
[01:12:00] Morgan Cook: I asked information from them that I'm requesting at this point, but it will come.
[01:12:04] Morgan Cook: He just has to dig the information up and send it to me, so he's been too busy with other things for that.
[01:12:12] Morgan Cook: I've got about seven projects right now that are out there and in some state of needing more attention, so I'm just cycling through all those as I wait for new information from the Heritage Plot one.
[01:12:26] Morgan Cook: That's the one I really want to get off the ground.
[01:12:31] Morgan Cook: And that's about it.
[01:12:33] Morgan Cook: Not anything to show this week.
[01:12:35] Morgan Cook: haven't been doing much programming work, so be on it this week for hopefully have something to show next week.
[01:12:42] Morgan Cook: Patrick, if you're still around, what was the UI tool that you were using for your constellation display?
[01:12:50] Patrick Chouinard: Oh, just Claude Code with front-end designer [tool:front-end-designer skill].
[01:12:54] Paul Miller: Let's go.
[01:12:55] Morgan Cook: wasn't a library or anything?
[01:12:57] Patrick Chouinard: Nope.
[01:12:58] Patrick Chouinard: Actually, well, it's two...
[01:13:00] Patrick Chouinard: It's a superpowers with brainstorming and the skill called front-end designer [tool:superpowers].
[01:13:08] Morgan Cook: Because with your constellation display of all of your lab nodes, okay.
[01:13:16] Patrick Chouinard: Yeah, basically, a superpowers in brainstorming mode helps me structure my idea and front-end designer takes those and propose implementation.
[01:13:29] Patrick Chouinard: So, actually, it's a library.
[01:13:31] Patrick Chouinard: I'm going to dig into the website itself, but there's a library that takes care of the constellation itself.
[01:13:40] Morgan Cook: All right, yeah.
[01:13:44] Ty Wells: Morgan, you had actual work this week, like me?
[01:13:48] Ty Wells: Like, we had to do, like, real work?
[01:13:50] Ty Wells: That was, it's been a tough week for me, and it's only Tuesday.
[01:13:54] Morgan Cook: Part of the physical world, not part of the digital world, you know?
[01:13:57] Ty Wells: This is what I'm saying.
[01:13:58] Paul Miller: Yeah, exactly.
[01:14:01] Paul Miller: End of the quarter, you kind of need to chase those people that haven't paid the bills and staff and tax and all that, all the rest of it.
[01:14:11] Ty Wells: Yeah, taxes, yeah, I've been working on those.
[01:14:16] Morgan Cook: So that's where I've been this last week, and we'll see where we end up next week.
[01:14:23] Paul Miller: Thanks, Morgan.
<!--SEGMENT
topic: Jake — scope creep on steroids + multi-tenant ask + adoption-thumbs cycle
speakers: Jake Maymar, Paul Miller, Juan Torres, Patrick Chouinard, Ty Wells
keywords: scope creep steroids, AI overconfidence on project intake, evals, thumbs-up/thumbs-down cycle, customers get used to success, 80→90→95% feels impossible, single-tenant→multi-tenant ask, OpenClaude vs secure systems, code freeze ignored during pitch, OKR-only filtering
summary: Jake is overwhelmed by his own pipeline — every project he took on because of AI confidence is now succeeding, getting customers, and demanding multi-tenant + harder features. Adoption pattern: clients are thrilled at first, then thumbs-down once they get used to the magic and want more. Reaching 80% is easy; 90% painful; 95% feels impossible. Jake spends most of his time fighting scope creep and filtering Jira tickets to OKR-only critical path. He even survived a major investor pitch where the team kept coding during his code freeze ('app creep' = Paul's term: scope creep made tangible because building is now nearly free).
-->

[01:14:25] Paul Miller: Jake, how's it going?
[01:14:31] Jake Maymar: Just crazy busy.
[01:14:33] Jake Maymar: Just, yeah, it's just nuts.
[01:14:36] Jake Maymar: It just, I think all of these, so I'm doing some work for a company that needs to be very secure, and all these different leaks around AI is causing a headache for sure.
[01:14:51] Jake Maymar: I really did find the Claude leak really interesting, though.
[01:14:56] Jake Maymar: There was a lot of really interesting things in that leak.
[01:14:59] Jake Maymar: much more抵d on
[01:15:01] Jake Maymar: Scott just shared a great link for the Reddit.
[01:15:03] Jake Maymar: I think it's definitely worth going through.
[01:15:05] Jake Maymar: That was much better than what I was looking at.
[01:15:09] Jake Maymar: Yeah, I'm working on a lot of projects.
[01:15:12] Jake Maymar: I think too many projects.
[01:15:14] Jake Maymar: I'm just trying to figure out, like, I would have never taken on these projects if I didn't have AI.
[01:15:20] Jake Maymar: And I think I got overconfident.
[01:15:23] Jake Maymar: Yeah, it's not that any of them are, they're all going well.
[01:15:27] Jake Maymar: It's just that's the problem.
[01:15:28] Jake Maymar: They're all going well.
[01:15:29] Jake Maymar: And they're all getting customers, and they're all getting much more complex.
[01:15:35] Jake Maymar: And everything's moving to prod a lot faster than I thought.
[01:15:39] Jake Maymar: I kept thinking I could, you know, not get to prod so quickly.
[01:15:45] Jake Maymar: But yeah.
[01:15:46] Jake Maymar: So I'm looking forward to showing you guys something someday.
[01:15:55] Jake Maymar: That's too, Paul, like, like, I'm still chasing the money, right?
[01:15:59] Jake Maymar: Like, so some are
[01:16:00] Jake Maymar: And some are, you know, uh, they're gonna, they're gonna send me the, the, uh, the second payment and all that, you know, classic stuff.
[01:16:09] Jake Maymar: Right.
[01:16:09] Jake Maymar: And so, um, and some are still in like contract negotiation.
[01:16:13] Jake Maymar: Like, yeah, so it's a very interesting world.
[01:16:19] Jake Maymar: Um, everything's going well, though.
[01:16:22] Jake Maymar: Like everything's, you know, really interesting and exciting and, um, doing a lot of, um, evals on responses.
[01:16:32] Jake Maymar: I'd spend most of my time on that.
[01:16:35] Jake Maymar: So you have these long form agentic systems and basically doing evals on that.
[01:16:40] Jake Maymar: Um, and there's a whole bunch of neat tools you can use.
[01:16:44] Jake Maymar: And I kind of spun on my own, but, um, it's very interesting because one of the solutions is a fairly long solution, fairly long prompt, and you get a solution out of it.
[01:16:58] Jake Maymar: Um, client was,
[01:17:00] Jake Maymar: I lots of thumbs down, lots of negative comments, took that in, did a full eval, redid the whole system, everyone was happy, tons of love-its, tons of thumbs up, lots of really good comments.
[01:17:16] Jake Maymar: I was like, all right, this is fantastic.
[01:17:19] Jake Maymar: And then nothing changed.
[01:17:21] Jake Maymar: Like, I didn't change my codebase, didn't change anything.
[01:17:23] Jake Maymar: And then all of a sudden, just lots of thumb downs, and lots of bad comments.
[01:17:28] Jake Maymar: And I was like, what happened?
[01:17:29] Jake Maymar: Like, you guys are loving it.
[01:17:31] Jake Maymar: ▶ And I noticed this really interesting pattern where people get used to success.
[01:17:36] Jake Maymar: And so they want it to be better.
[01:17:38] Jake Maymar: So at first, they were totally thrilled, because it was like shiny and new and exciting.
[01:17:43] Jake Maymar: And it was doing everything you do.
[01:17:44] Jake Maymar: And then they kind of looked around like, wait a second, it doesn't do this, and it doesn't do this.
[01:17:48] Jake Maymar: And so, so then I added all those capabilities, and I got a lot of negative things and a lot of thumbs down.
[01:17:55] Jake Maymar: And so I had to like roll back and figure out how to, because like finding that back
[01:18:00] Jake Maymar: ▶ Because getting 80%, that's easy, right?
[01:18:05] Jake Maymar: And then getting 90% is like, oh man, that's insane.
[01:18:09] Jake Maymar: And then getting to like 95%, it feels impossible.
[01:18:13] Jake Maymar: It just feels impossible because things are moving so quickly.
[01:18:17] Jake Maymar: There's so many different voices.
[01:18:19] Jake Maymar: There's so many different customers.
[01:18:20] Jake Maymar: Customers get used to it.
[01:18:22] Jake Maymar: And so a customer that liked it one week has changed their mind, doesn't like it.
[01:18:26] Jake Maymar: A customer that didn't like it one week has changed their mind.
[01:18:29] Jake Maymar: And likes it.
[01:18:30] Jake Maymar: So that's kind of the world I'm living in.
[01:18:34] Paul Miller: When you have these opportunities that come along, do you, of course, you've got all the exercise you go through with the customer about what they're trying to do and what's the kind of big vision about what they might want.
[01:18:50] Paul Miller: Do you counter that with deep research about what tools are doing in that space?
[01:18:59] Paul Miller: Yeah.
[01:19:00] Paul Miller: And feedback from users in terms of those external forums where they've gone and put the things they've shared, all the thinking about, all of that stuff as well.
[01:19:10] Jake Maymar: So this is what's so interesting, Paul.
[01:19:13] Jake Maymar: I get to a finished product almost immediately, and they're absolutely, totally thrilled.
[01:19:19] Jake Maymar: And then we start looking at features on top, right?
[01:19:23] Paul Miller: And the first couple of features, they're thrilled.
[01:19:26] Jake Maymar: They're absolutely, totally thrilled.
[01:19:28] Jake Maymar: But then they start adding features that are, like, real hard problems.
[01:19:34] Jake Maymar: Like, not sure you can do this kind of situation.
[01:19:39] Jake Maymar: And, you know, of course, they're willing to pay, you know, and they're willing to work with me.
[01:19:44] Jake Maymar: And they're, you know, it's gone from a fairly complex thing, agentic flow, to a much more complex thing, right?
[01:19:53] Jake Maymar: Which then there's, like, lot of team interaction, a whole bunch of other things.
[01:19:57] Jake Maymar: And so what happens is...
[01:19:59] Jake Maymar: ...
[01:19:59] Jake Maymar: ...
[01:20:00] Jake Maymar: Just the project gets complex and I honestly wouldn't take on something like that.
[01:20:05] Jake Maymar: I wouldn't take on a really, really hard problem.
[01:20:08] Jake Maymar: But the problem is I feel like, well, I'm so close.
[01:20:11] Jake Maymar: Like I'm so close.
[01:20:12] Jake Maymar: And I get 80% of that insanely hard problem solved.
[01:20:19] Jake Maymar: And then I, I just can't get the rest.
[01:20:22] Jake Maymar: Like, like there's, there's like impediments that are just, I mean, that's why they're hard problems, right?
[01:20:27] Jake Maymar: They're like, surprise.
[01:20:29] Jake Maymar: I mean, we're trying to solve things that are just like, need new hardware, need new architecture systems, need, you know what I mean?
[01:20:41] Jake Maymar: And, and I'll explain that to them.
[01:20:43] Jake Maymar: And they're like, yeah, but you did all of these other things.
[01:20:46] Jake Maymar: And I'm like, yes, you know, and then of course they're looking around all the height too, right?
[01:20:52] Jake Maymar: The open clause and all these other things.
[01:20:54] Jake Maymar: And, and I'm like, those aren't secure.
[01:20:56] Jake Maymar: Like they have to be secure.
[01:20:57] Juan Torres: So doing this in a very secure way.
[01:21:00] Juan Torres: Sustainably.
[01:21:01] Paul Miller: Yeah.
[01:21:02] Jake Maymar: ▶ Perfect example, like I did this single-tenant thing, very robust, very secure, did amazing things, everyone was really happy, and they're like, okay, now we want multi-tenant.
[01:21:13] Jake Maymar: And I'm like, oh, that's...
[01:21:19] Jake Maymar: Yeah, that's like, you know, and yeah.
[01:21:23] Jake Maymar: So anyway, that's the headache I'm living with, not to complain too much.
[01:21:27] Jake Maymar: It's interesting you say that.
[01:21:30] Paul Miller: I had a catch-up.
[01:21:33] Paul Miller: So about 12 years ago, well, more than 12 years ago, 15 years ago, when iOS really, for iPad, really started to be building smart apps on iPads.
[01:21:49] Paul Miller: It was the real go-to at the time.
[01:21:53] Paul Miller: And I, um, I said, I hired these two young guys who knew...
[01:22:00] Paul Miller: They how to write on the iOS stack.
[01:22:02] Paul Miller: They really got it.
[01:22:04] Paul Miller: They got it from the UI, UX and what the tool could do.
[01:22:08] Paul Miller: And we pretty much changed the world with how consumer goods businesses use these devices for their field teams.
[01:22:18] Paul Miller: And a very large bottler who happens to be close to where Brandon lives, who I won't mention on the call, but it's now their default model around the world for selling their product.
[01:22:32] Paul Miller: And it was a game changer.
[01:22:33] Paul Miller: And Apple got excited and wanted to hire everyone into Apple.
[01:22:38] Paul Miller: And we knew their culture was pretty bad, so we thought, no way.
[01:22:41] Paul Miller: But it changed the way people did what they do.
[01:22:47] Paul Miller: And back then, the restriction was time and money.
[01:22:53] Paul Miller: So you couldn't build every feature.
[01:22:57] Paul Miller: You had to focus on, well, what are the features?
[01:22:59] Paul Miller: And, course,
[01:23:00] Paul Miller: What you're going to use and what's the way the users unlock those features to deliver the business benefit that the project's trying to achieve?
[01:23:09] Paul Miller: Now, I caught up with one of these young guys who kind of looked 12 at the time.
[01:23:15] Paul Miller: I think they were in their early 20s and they've done really well and lots of money and now have got families of their own and young kids and want to balance the work-life thing.
[01:23:25] Paul Miller: Now, he's got the mindset of, well, we've got the money, we can do everything with AI.
[01:23:32] Paul Miller: You come along to the customer now, you want to put the restriction on them to say, well, we could code everything and you've coded everything for them.
[01:23:44] Paul Miller: You need to get them focused on saying, well, what is that business objective?
[01:23:49] Paul Miller: Let's just get that business objective across the line that you want to be able to do.
[01:23:53] Paul Miller: But because you've shown them the magic and how quickly you can move, you can't lock and load them down.
[01:23:59] Paul Miller: It's like
[01:24:00] Paul Miller: I've got the same thing.
[01:24:03] Paul Miller: I don't know, Patrick, you're still there.
[01:24:05] Paul Miller: You've got that blimmin' corporate that you're looking after and everyone wants to be blimmin' startup gurus and they've just got to run a business.
[01:24:15] Paul Miller: Have you worked out how to keep people calm and focused so you can actually get projects done like Jake's dealing with?
[01:24:25] Paul Miller: Because I don't know the answer.
[01:24:28] Paul Miller: Once you show them how you can do the magic with the secret sauce, how do you control it now?
[01:24:36] Jake Maymar: It's even more interesting.
[01:24:39] Jake Maymar: Not to cut you off, Patrick, because I definitely want to hear what you're going to say, but one other thing that I think was really interesting.
[01:24:46] Jake Maymar: So I was overwhelmed.
[01:24:48] Jake Maymar: I didn't have enough time.
[01:24:50] Jake Maymar: I didn't have enough bandwidth.
[01:24:51] Jake Maymar: I'm not saying I have that now, but I'm just saying that I have to prioritize everything now.
[01:24:58] Jake Maymar: Whereas before I had a little bit of wiggle room.
[01:25:00] Jake Maymar: I'm using AI a tremendous amount just for time management, really.
[01:25:05] Jake Maymar: Oh, but what I wanted to say is this.
[01:25:08] Jake Maymar: When the clients started using the systems, either Claude Code or different types of OpenClaude or whatever it was, it really changed the conversation as well.
[01:25:22] Jake Maymar: And that was a really, really interesting thing.
[01:25:25] Paul Miller: Yeah.
[01:25:27] Jake Maymar: Because they're implementing, and I know Patrick has talked about this, where they're implementing systems that are not secure, but they're kind of getting very, very close to what they want.
[01:25:38] Jake Maymar: And then they want me to take that.
[01:25:41] Jake Maymar: So one of the examples is I had five different GitHub repos that I needed to consolidate into one.
[01:25:48] Jake Maymar: I had to make sure that they all played nice together and kept the results that they were getting on an individual basis.
[01:25:58] Paul Miller: Oh.
[01:25:59] Paul Miller: .
[01:26:00] Paul Miller: And they didn't stop development.
[01:26:04] Jake Maymar: So we had a major, major pitch to an investor.
[01:26:08] Jake Maymar: No one stopped any sort of development, even though I said we need to freeze the code.
[01:26:14] Jake Maymar: I will say it was a success.
[01:26:16] Jake Maymar: We landed it.
[01:26:17] Jake Maymar: It was a huge...
[01:26:18] Jake Maymar: I definitely lost even more hair.
[01:26:23] Jake Maymar: But yeah, I mean, it was a huge success.
[01:26:26] Jake Maymar: We landed it.
[01:26:29] Jake Maymar: And I learned a lot from it, but I've never been in that situation before where people are still basically coding as I'm consolidating everything together.
[01:26:40] Jake Maymar: I did a code freeze myself, but the problem is it didn't sync with their outputs that they were getting.
[01:26:49] Jake Maymar: And that was an issue that I ran into.
[01:26:52] Jake Maymar: Does that make sense, what I'm saying?
[01:26:54] Paul Miller: Yeah.
[01:26:55] Paul Miller: Yeah.
[01:26:56] Jake Maymar: Yeah.
[01:26:56] Paul Miller: I think the old fashioned scope creep.
[01:27:00] Paul Miller: ▶ has now become so tangible, because coding can be done so quickly, that scope creep is now app creep.
[01:27:10] Paul Miller: Oh, it's, yeah, it's system creep.
[01:27:12] Jake Maymar: And the thing is, what I do now, I spend most of my time fighting against scope creep.
[01:27:19] Jake Maymar: Like, I spend most of my time, like, is this a critical business need?
[01:27:24] Jake Maymar: I have so many calls where I say, is this a critical path?
[01:27:28] Jake Maymar: ▶ Like, all these Jira tickets, all these different tickets, I'm like, okay, we are only focused on critical path, and we are only focused on OKRs.
[01:27:38] Jake Maymar: If this is not affecting an OKR, why do we even care at this point?
[01:27:43] Jake Maymar: Like, that feature, because I have actually implemented entire systems that were thrown away.
[01:27:51] Jake Maymar: Like, just completely thrown away systems, and you're like, I actually really liked, oh, oh, and that's, oh, I know I'm going too long.
[01:27:59] Jake Maymar: me.
[01:27:59] Jake Maymar: things.
[01:27:59] Jake Maymar: I I You
[01:28:00] Jake Maymar: I've had entire systems implemented, thrown away, and then they wanted to bring it back.
[01:28:06] Jake Maymar: And then brought back the whole system again after we went down the path.
[01:28:11] Paul Miller: Yeah, I am fighting a lot of different things.
[01:28:14] Jake Maymar: I mean, it's not like, you know, yeah, but that's, that's the things I'm fighting with.
[01:28:20] Paul Miller: Yeah, I hear your pain.
[01:28:24] Paul Miller: I think this is very common.
[01:28:27] Juan Torres: Why do I feel that good leadership is the exception, not the norm?
[01:28:32] Jake Maymar: It's hard, though, Juan.
[01:28:33] Jake Maymar: mean, that's the thing.
[01:28:35] Jake Maymar: You have, you have people that have wanted to have these skills, very smart people, very good at what they do, subject matter experts.
[01:28:44] Paul Miller: Yeah.
[01:28:45] Jake Maymar: A little bit of development or actually very, very good developers, but they want to work with me.
[01:28:51] Jake Maymar: I have certain capabilities that they really want.
[01:28:55] Jake Maymar: Like I can do evals really well, data science, blah, blah, blah.
[01:28:58] Jake Maymar: Right.
[01:28:59] Jake Maymar: So.
[01:28:59] Paul Miller: Hello.
[01:29:01] Jake Maymar: They get it almost, they get the, you know, the ball almost, you know, I'm bad at sports, but down almost to a touchdown, right?
[01:29:10] Jake Maymar: Like they get it almost to a touchdown, but they just need to get it that little farther.
[01:29:15] Jake Maymar: And I can do that most of the time, right?
[01:29:17] Jake Maymar: I can pick it up, I can take it, I can definitely, you know, make it a success.
[01:29:23] Jake Maymar: But yeah, it's, it's really, really hard, because everything's accelerating.
[01:29:28] Jake Maymar: And it just keeps getting faster and faster.
[01:29:30] Jake Maymar: I got on a call, and my friend was showing me, he was showing me a report what he did, basically, the weekend, and then the last hour.
[01:29:42] Jake Maymar: And it was all of these systems that he had created, like, like, like Patrick, and like a lot of you guys, right?
[01:29:48] Jake Maymar: But it was like the last hour.
[01:29:51] Jake Maymar: And he had already run through like, I think three Claude Code subscriptions.
[01:29:57] Jake Maymar: I was like, what are you doing?
[01:30:00] Jake Maymar: Like, this is insane, right?
[01:30:01] Jake Maymar: And of course, so anyway, I sound like I'm complaining.
[01:30:04] Jake Maymar: I'm just trying to keep up with the pace of this stuff.
[01:30:08] Jake Maymar: Oh, and that's the thing.
[01:30:10] Jake Maymar: None of these things, mean, knock on wood, are failures.
[01:30:14] Jake Maymar: Like, they're all successes.
[01:30:16] Jake Maymar: That's actually the problem.
[01:30:18] Jake Maymar: The problem is that they're successes, right?
[01:30:21] Jake Maymar: So it just keeps accelerating and getting more and more and more complex.
[01:30:25] Jake Maymar: So anyway, I'm done talking.
[01:30:27] Jake Maymar: I'd love to hear you guys' thoughts.
[01:30:28] Jake Maymar: Yeah, please help.
<!--SEGMENT
topic: Patrick gym anecdote + free advice tactic
speakers: Patrick Chouinard, Ty Wells, Jake Maymar, Juan Torres, Morgan Cook
keywords: gym owner building app with Claude Code, no tech-stack awareness, AWS bill surprise warning, GitHub Actions cost, superpowers code-review + security-code-review skills, OAuth offload, plumbing-vs-value framing, free gym membership trade
summary: Post-workout, Patrick discovered his gym's owner is building an internal app with Claude Code without knowing his own tech stack. Patrick walked him through asking Claude what stack it deployed (AWS, GitHub Actions — billable surprises coming), recommended the superpowers /code-review and /security-code-review skills aggressively, and pushed him to swap his home-rolled auth for Google/Meta OAuth ('that's plumbing, brings no value'). Patrick walks out with a free gym membership. Patrick's framing for Jake: difficult clients ARE the business — they create the problems you exist to solve.
-->

[01:30:31] Patrick Chouinard: ▶ Jake, everything you describe right now is the reason you're making money.
[01:30:35] Patrick Chouinard: If they were not doing that, you wouldn't be making money.
[01:30:39] Patrick Chouinard: Because honestly, they create the problem that you're there to build them to solve.
[01:30:44] Patrick Chouinard: So I love guys like that.
[01:30:46] Patrick Chouinard: And in the enterprise, mean, that's why I kept my mandate for five years, because I was surrounded by people who kept creating problems I could solve.
[01:30:57] Patrick Chouinard: Yeah, that's true.
[01:30:59] Patrick Chouinard: They're my biggie.
[01:31:01] Juan Torres: Yeah, that's very, very true.
[01:31:04] Patrick Chouinard: That's really it.
[01:31:05] Patrick Chouinard: I love those guys.
[01:31:06] Patrick Chouinard: Create as many problems as you want.
[01:31:08] Patrick Chouinard: I mean, you're making sure that I have a job for the rest of my life.
[01:31:11] Juan Torres: That is so true.
[01:31:14] Patrick Chouinard: Exactly.
[01:31:16] Patrick Chouinard: It's still painful, though.
[01:31:17] Jake Maymar: It's still painful.
[01:31:20] Jake Maymar: You have to look at it as an opportunity.
[01:31:22] Jake Maymar: Yeah, that's true.
[01:31:23] Jake Maymar: It is an opportunity.
[01:31:24] Ty Wells: Yeah, you got to brush it off.
[01:31:27] Ty Wells: Refrain it.
[01:31:29] Ty Wells: Yeah, it's horrible with clients we can do.
[01:31:32] Ty Wells: That's why I don't like clients.
[01:31:34] Ty Wells: But you sort of have to run them through.
[01:31:37] Ty Wells: No, I'm serious.
[01:31:37] Ty Wells: I'm selective in my clients because the scope is a scope and that's going to be it right there.
[01:31:43] Ty Wells: Now, you have to go back on the list to see if we're going to extend anything or change anything.
[01:31:50] Ty Wells: Oh, smart.
[01:31:51] Ty Wells: That is what it is.
[01:31:54] Ty Wells: It's like trying to get in to see a doctor that's really, really good.
[01:31:57] Ty Wells: You know, you just got to wait your turn to get there.
[01:32:00] Ty Wells: If you want it, because you can get it done.
[01:32:02] Ty Wells: You can get it done.
[01:32:03] Ty Wells: Well, you can get it done really fast, but it's going to take you a minute to get there.
[01:32:07] Ty Wells: And that's, that's the way I take it.
[01:32:08] Ty Wells: Plus it, it increases your value, right?
[01:32:11] Ty Wells: It's, you know, that's, if there's a demand, it's a simple economics of things, right?
[01:32:16] Ty Wells: You, you definitely create the, the value right out of the box.
[01:32:19] Ty Wells: That's, that's true.
[01:32:21] Jake Maymar: That's actually true.
[01:32:22] Patrick Chouinard: I'll give you an example, Jake, of something that happened to me like yesterday.
[01:32:27] Patrick Chouinard: Okay.
[01:32:28] Patrick Chouinard: I, I, because I run after those clients.
[01:32:30] Juan Torres: I love those guys.
[01:32:32] Patrick Chouinard: I was, I was at the gym.
[01:32:34] Patrick Chouinard: Okay.
[01:32:35] Patrick Chouinard: No, no relation to AI whatsoever.
[01:32:39] Patrick Chouinard: Uh, the guy at the reception just told me that the owner is building an internal application for them using Claude Code.
[01:32:47] Patrick Chouinard: So I went and sit down with him because he was there.
[01:32:50] Patrick Chouinard: We, we chat for an hour.
[01:32:52] Patrick Chouinard: The guy, has no knowledge of how to code.
[01:32:55] Patrick Chouinard: ▶ He just knows how to talk to Claude Code and he built a decent.
[01:33:00] Patrick Chouinard: It was not bad, but when I asked him, like, what's the tech stack behind it?
[01:33:06] Patrick Chouinard: I don't know.
[01:33:07] Patrick Chouinard: Okay.
[01:33:08] Patrick Chouinard: Uh, what database do you use?
[01:33:10] Patrick Chouinard: I don't know.
[01:33:13] Patrick Chouinard: So basically I've asked him, like, ask this to Claude, like ask for the tech stack.
[01:33:17] Patrick Chouinard: As it shows the tech stack.
[01:33:20] Patrick Chouinard: It's like, okay, how long have you been doing that?
[01:33:22] Patrick Chouinard: About three weeks.
[01:33:23] Patrick Chouinard: Okay.
[01:33:24] Patrick Chouinard: So you haven't received your first bill yet.
[01:33:25] Jake Maymar: ▶ Yeah.
[01:33:28] Patrick Chouinard: Look, this is AWS, AWS, AWS, those you pay for.
[01:33:31] Jake Maymar: Oh no.
[01:33:32] Patrick Chouinard: Look, GitHub Actions.
[01:33:34] Patrick Chouinard: Those you pay for.
[01:33:36] Patrick Chouinard: Go take you, go check your bill.
[01:33:38] Patrick Chouinard: Okay.
[01:33:38] Jake Maymar: I know he wasn't too bad.
[01:33:40] Patrick Chouinard: He's still building.
[01:33:41] Patrick Chouinard: So it's not like he views stuff that was incredibly expensive, but it's like, there's a cost behind that.
[01:33:47] Patrick Chouinard: Go take a look.
[01:33:48] Patrick Chouinard: Okay.
[01:33:48] Patrick Chouinard: Because you're going to get a surprise if you don't do that.
[01:33:51] Jake Maymar: Yeah.
[01:33:51] Patrick Chouinard: After that, I've shown him because he was already using superpowers.
[01:33:55] Patrick Chouinard: Great for him.
[01:33:56] Patrick Chouinard: But I saw there's two skills in there that you might not have used.
[01:34:00] Patrick Chouinard: code review and security code review [tool:code review skill] [tool:security code review skill].
[01:34:02] Patrick Chouinard: Use them aggressively because you have no idea what you're doing.
[01:34:06] Patrick Chouinard: At least protect yourself from the most obvious things.
[01:34:10] Patrick Chouinard: Second, you're doing your own auth.
[01:34:12] Patrick Chouinard: And honestly, it was not badly done for own brew stuff.
[01:34:17] Patrick Chouinard: But still, I told them, why are you doing that?
[01:34:20] Patrick Chouinard: ▶ Give that to Google OAuth, meta authentication.
[01:34:24] Ty Wells: Like, don't do that for a business.
[01:34:27] Patrick Chouinard: ▶ That's plumbing.
[01:34:28] Patrick Chouinard: That brings no value to your application.
[01:34:31] Patrick Chouinard: All of that, and guess what?
[01:34:33] Patrick Chouinard: ▶ Now I have a free gym membership.
[01:34:36] Juan Torres: Yeah, that's great.
[01:34:38] Ty Wells: I was gonna say, there's gotta be some free membership in there somewhere.
[01:34:41] Ty Wells: Yeah, That's an hour of your time.
[01:34:42] Juan Torres: Wow.
[01:34:43] Juan Torres: Did you do your workout in the end, or you didn't get a chance?
[01:34:48] Patrick Chouinard: that was after my workout.
[01:34:49] Paul Miller: Okay.
[01:34:50] Patrick Chouinard: Wow.
[01:34:51] Juan Torres: He didn't even work out.
[01:34:52] Juan Torres: He was just coding again.
[01:34:54] Patrick Chouinard: Well, actually, I was talking with Claude Code on my phone at the same time, so...
[01:34:59] Jake Maymar: It's...
[01:35:00] Jake Maymar: It's so hard, Patrick, because for the longest time I've worked with a lot of these people that are my clients, I am very careful with the clients that I pick, and a lot of them were really kind of, they wanted to do certain things for so long, we talked about them for years, and now they can do them, and they're all different verticals, they're all different things, and what's really cool is if I can finish this and pull it off, they all work together.
[01:35:24] Jake Maymar: So all the different platforms actually, it's just a nice sort of, yeah, exactly, they kind of all work together very well, even though they're completely different verticals, they don't know this, but the idea is then they could all work together, right, that's, you know, sort of the plan.
[01:35:46] Jake Maymar: But yeah, I, it's just a, it's just, it's really, I really do like building things that people are really excited about, you know, they've had this thing, this idea.
[01:36:00] Jake Maymar: And now with AI, they can actually do it, which is amazing.
[01:36:05] Patrick Chouinard: But yeah.
[01:36:05] Patrick Chouinard: But that's the You let them start, and then you save them thousands of dollars with a couple of warnings, and now they're going to respect you forever and ask you for an idea every single time.
[01:36:16] Patrick Chouinard: And you get free stuff out of it, or a job, depending on who they are and what they do.
[01:36:21] Jake Maymar: Yeah, great point.
[01:36:24] Morgan Cook: Yeah, the gym manager will be back with you, Patrick, soon.
[01:36:28] Patrick Chouinard: I know.
[01:36:28] Juan Torres: Nah.
[01:36:29] Juan Torres: Yeah.
[01:36:30] Juan Torres: Probably.
[01:36:31] Patrick Chouinard: I have no problem with that.
[01:36:32] Jake Maymar: Unlimited gym membership.
[01:36:36] Patrick Chouinard: Sounds like an onboarding right there.
[01:36:38] Ty Wells: Like, hey, yeah, I was just helping, but now I'm going to have to take you to the flow because I work with this company, and there you go.
[01:36:45] Ty Wells: Then you can shovel them off the junior day.
[01:36:47] Patrick Chouinard: Oh, if he needs consulting services, yeah, absolutely.
[01:36:50] Ty Wells: have the card for my company in my back pocket, and you're nice.
[01:36:54] Ty Wells: Absolutely.
[01:36:55] Patrick Chouinard: But for one hour, a gym membership, I'm not complaining.
[01:36:59] Patrick Chouinard: the kidding.
[01:36:59] Patrick Chouinard: Yeah,
<!--SEGMENT
topic: RAG vs RLM vs re-ranker layering
speakers: Jake Maymar, Paul Miller, Ty Wells, Patrick Chouinard, Scott Rippey
keywords: RAG persistence, GraphRAG, RLM (reasoning loop), Cohere re-ranker, layering pattern, small-corpus RAG dying, agentic-loop substitute under 1000 documents, large-library RAG still required
summary: Jake asks if RAG is going away. Group consensus: large-corpus RAG isn't going anywhere; small-corpus RAG (under ~1000 docs) IS being replaced by big context windows + agentic search loops. The layering stack is RAG first, then re-ranker (Cohere is fast, real value at moderate scale), then RLM-style reasoning loops only when corpus is huge enough to justify the latency cost.
-->

[01:37:00] Jake Maymar: Oh, I do have one question for the group.
[01:37:03] Jake Maymar: So, you know, we still use a lot of RAG, right?
[01:37:06] Jake Maymar: I mean, that's kind of the go-to, I'm assuming at this point, right?
[01:37:09] Jake Maymar: Google released their new thing.
[01:37:13] Jake Maymar: I mean, there's so many different sort of RAG things and then sort of the next thing that's going to replace RAG [tool:GraphRAG].
[01:37:19] Jake Maymar: So GraphRAG, you know, rerank, all that stuff, right? [tool:RLM]
[01:37:22] Jake Maymar: I'm talking about all the different RAG systems.
[01:37:25] Jake Maymar: Is there on the horizon with all these leaks and all these conversations, an alternative that actually is going to come out?
[01:37:32] Jake Maymar: Or are we just going to keep using RAG?
[01:37:41] Paul Miller: Well, I don't think RAG is going anywhere.
[01:37:43] Ty Wells: ▶ Anytime soon, there will be some variations, but I don't see any other way that you can take a massive amount of data and be able to semantically search, you know, other than adding some, you know, your regular, typical.
[01:38:00] Ty Wells: Search the combination of the two, and yeah, I mean, I don't see it.
[01:38:05] Patrick Chouinard: ▶ small RAG system are going away.
[01:38:07] Patrick Chouinard: Like the one that were personal or very small amount, like below a thousand documents and the stuff that, yeah, you used to have to do that with RAG.
[01:38:18] Patrick Chouinard: Now, context window are big enough, an agentic loop that can search through folders and do most of those.
[01:38:24] Patrick Chouinard: But large library, you can get away from You guys remember what I was doing with that one thing that I put in NeuralSpark was that it's just a layer.
[01:38:31] Scott Rippey: RAG's the first layer.
[01:38:33] Scott Rippey: And then building on top of that, mean, re-rankers, the whole RLM loop, like a loop like Patrick was just talking about [tool:re-ranker].
[01:38:39] Scott Rippey: I mean, that kind of stuff, when you start getting more and more massive amounts of data can just help bolt on, you know, as another layer.
[01:38:45] Scott Rippey: Just trying to funnel it down.
[01:38:48] Jake Maymar: So, Scott, what do you think of the RLM stuff?
[01:38:51] Jake Maymar: You've had it for a while.
[01:38:52] Scott Rippey: I'm sure you've done evals on it.
[01:38:54] Scott Rippey: What do you think?
[01:38:55] Scott Rippey: I really like it, but obviously it's got to be for certain use cases, meaning like...
[01:38:59] Scott Rippey: ...
[01:38:59] Scott Rippey: ...
[01:38:59] Scott Rippey: Thank
[01:39:00] Scott Rippey: Just even with RAG, you don't really need RAG until you get like over a certain amount of data where AI is having a hard time, you know, determining intent.
[01:39:08] Scott Rippey: Well, I probably won't turn on RLM, even for my guy that's got a ton of information that I put him on it.
[01:39:13] Scott Rippey: I'm like, the RLM is really good for like the Google side of that, where it's going to run a report and it'll run for a few minutes and it'll smartly kind of pull everything together.
[01:39:22] Scott Rippey: But it's also kind of still even overkill for RAG, think, until you get to something so massive I haven't seen yet.
[01:39:27] Scott Rippey: Like, so, but I've got it so I can turn it on and off and all these different aspects to kind of test and see and, you know, it's like I don't need to add 15 seconds on a RAG search when my data isn't that big, you know, the re-ranking does a lot, re-ranking's quick.
[01:39:39] Scott Rippey: I think that, I think that as a layer two, using something like Cohere for a re-ranker really does help when you get to a certain, I think that's like the first thing to try before you get to these longer things, you know, but, you know, just, it's just figuring out where everything kind of fits and when it's useful to turn on and when it's overkill, right? [tool:Cohere]
[01:39:56] Jake Maymar: Like, yeah, yeah, yeah, I agree.
[01:39:59] Jake Maymar: That makes a lot of sense.
[01:40:00] Jake Maymar: Just even with RAG, you don't really need RAG until you get like over a certain amount of data where AI is having a hard time, you know, determining intent.
[01:40:08] Paul Miller: Well, I probably won't turn on RLM, even for my guy that's got a ton of information that I put him on it.
[01:40:13] Paul Miller: I'm like, the RLM is really good for like the Google side of that, where it's going to run a report and it'll run for a few minutes and it'll smartly kind of pull everything together.
[01:40:22] Paul Miller: But it's also kind of still even overkill for RAG, think, until you get to something so massive I haven't seen yet.
[01:40:27] Paul Miller: Like, so, but I've got it so I can turn it on and off and all these different aspects to kind of test and see and, you know, it's like I don't need to add 15 seconds on a RAG search when my data isn't that big, you know, the re-ranking does a lot, re-ranking's quick.
[01:40:39] Paul Miller: ▶ I think that, I think that as a layer two, using something like Cohere for a re-ranker really does help when you get to a certain, I think that's like the first thing to try before you get to these longer things, you know, but, you know, just, it's just figuring out where everything kind of fits and when it's useful to turn on and when it's overkill, right?
[01:40:56] Paul Miller: Like, yeah, yeah, yeah, I agree.
[01:40:59] Morgan Cook: That makes a lot of sense.
[01:41:00] Morgan Cook: Yeah.
[01:41:00] Morgan Cook: Okay.
[01:41:00] Morgan Cook: That's it.
[01:41:01] Morgan Cook: That's it.
[01:41:01] Morgan Cook: I've talked too much.
[01:41:04] Morgan Cook: So one question from me.
<!--SEGMENT
topic: Native iOS + Android with offline sync — research request
speakers: Paul Miller, Jake Maymar, Ty Wells
keywords: React Native vs native, offline DB sync framework, Xcode + Claude Code setup, ShipKit guardrails for iOS, Android tooling gap, Worka.ai starter, deep research recommendation
summary: Paul asks for the group's experience with native iOS+Android apps with offline sync. Jake/Ty discuss React-Native frameworks, Xcode + Claude Code workflows (brittle but workable with ShipKit-style guardrails), and Android tooling being less mature. Recommendation: deep research on starred GitHub repos for current best stacks rather than picking one blindly.
-->

[01:41:06] Jake Maymar: I had a client wanting to have Android and iOS native apps that had offline sync.
[01:41:18] Jake Maymar: What have you guys done in that side?
[01:41:23] Jake Maymar: Because I've started down the React path of getting React to build an app and then apparently there's some frameworks you can use that'll deploy it natively with an offline kind of database that can sync [tool:React Native].
[01:41:40] Jake Maymar: What's other people done in that space with Claude?
[01:41:48] Jake Maymar: I've done a bit of research on that because I have to do the same thing with one of my projects.
[01:41:54] Jake Maymar: It needs both apps available.
[01:41:56] Jake Maymar: I'm not sure about going truly native.
[01:42:00] Jake Maymar: On both of them, I was going to use Worka.ai to start with to get a base going and then decide at that point to go into a native app for the iOS specifically [tool:Worka.ai].
[01:42:13] Jake Maymar: Yeah.
[01:42:13] Jake Maymar: Okay.
[01:42:14] Jake Maymar: So if you want, you can use Xcode with Cloud, with Claude Code, but it's a setup [tool:Xcode + Claude Code].
[01:42:19] Jake Maymar: You got to do a setup and you got to kind of, you know how like ShipKit has all the guardrails and all that stuff? [tool:ShipKit]
[01:42:25] Paul Miller: You want to basically find, there's tons of repos, just kind of find like a Xcode.
[01:42:33] Jake Maymar: And actually it might've changed by now, but I would, I would look, if you're going native, then you, and you're going to do iOS, you'll probably want to be in that area.
[01:42:43] Jake Maymar: I think.
[01:42:44] Paul Miller: Yeah.
[01:42:44] Paul Miller: But, but Fathia.
[01:42:47] Jake Maymar: Yeah.
[01:42:48] Jake Maymar: Yeah.
[01:42:48] Jake Maymar: Cause it's, it's, it's kind of brittle, like it's, it doesn't fully understand it.
[01:42:57] Paul Miller: So you really need to understand a lot of it.
[01:43:01] Paul Miller: And then it does a really good job.
[01:43:03] Paul Miller: That's why I'm saying there's probably repos now.
[01:43:05] Paul Miller: Because a lot of my friends do, they're iOS developers, specifically Xcode, as well as like Swift and all that stuff.
[01:43:14] Ty Wells: So they're really comfortable in that.
[01:43:16] Paul Miller: And so they've built really solid systems similar to Shipkit, but specifically for iOS.
[01:43:24] Paul Miller: Now Android, I don't know.
[01:43:25] Paul Miller: It's a good question.
[01:43:28] Paul Miller: Okay.
[01:43:29] Paul Miller: Maybe build some skills to save that once I've got the repo that works.
[01:43:37] Paul Miller: ▶ I would honestly just do a deep research, look for the get repos out there that are starred and well-liked.
[01:43:44] Paul Miller: And I think most likely you're going to find answers because this stuff moves so quickly.
[01:43:49] Paul Miller: I'd be shocked if there's not already a really nice set of tools.
[01:43:55] Jake Maymar: Brilliant.
[01:43:56] Jake Maymar: Cool.
[01:43:57] Jake Maymar: Thank you.
[01:43:58] Jake Maymar: Okay.
<!--SEGMENT
topic: wrap of therapy session + scope-creep discipline
speakers: Jake Maymar, Paul Miller, Alex Rojas
keywords: therapy session, decision matrix transcript review, North Star alignment, critical business needs, C-level shiny-object problem, Claude Code system to score client transcripts
summary: Group jokingly calls the discussion their therapy session. Alex Rojas joins; Paul reflects that the new world demands old-school discipline — push back on every request with 'what's the business driver?'. Alex shares that he has a Claude Code system that scores his client-call transcripts against a critical-needs decision matrix and surfaces drift away from the project's North Star.
-->

[01:43:59] Jake Maymar: Anyone else?
[01:44:00] Jake Maymar: want to grab the mic, or have we covered everything this week?
[01:44:08] Jake Maymar: I think our therapy session is concluded.
[01:44:14] Jake Maymar: Yeah.
[01:44:14] Jake Maymar: I have some things I've got to work on, some action items I've got to recover myself on today.
[01:44:21] Jake Maymar: Yeah, indeed.
[01:44:23] Jake Maymar: I'm glad you brought it up, though, Jake.
[01:44:29] Paul Miller: We're in this kind of new world.
[01:44:31] Paul Miller: ▶ I think having that discipline that we used to have, where you push people back to, well, what's the business driver here?
[01:44:47] Alex Rojas: What's the objective of this project?
[01:44:49] Alex Rojas: Because the scope creep is on steroids now.
[01:44:53] Alex Rojas: I agree.
[01:44:54] Alex Rojas: And so I actually have made a Claude Code system, I guess.
[01:44:59] Alex Rojas: Yeah, Okay.
[01:45:04] Alex Rojas: ▶ I'll have a conversation with a client, and I run my transcript through that first, and then it helps me kind of basically do a decision matrix around that, and see if it's still sort of pointing to the North Star, if it's, you know, basically critical business needs, but it's amazing, some people, they don't want to do business needs, they want shiny objects.
[01:45:28] Alex Rojas: Yeah, and when it's the, when it's your C-level people that are funding and signing off the project, even harder to It's very true.
[01:45:41] Alex Rojas: Alex, join the call, did you have anything you wanted to raise and share?
[01:45:47] Alex Rojas: Alex, good to see you.
[01:45:48] Alex Rojas: Hey guys.
[01:45:50] Alex Rojas: Yeah, it's been some time.
[01:45:52] Alex Rojas: Yeah.
<!--SEGMENT
topic: Alex's local-AI workshops + boutique-finance demand
speakers: Alex Rojas, Patrick Chouinard, Ty Wells, Morgan Cook
keywords: AI tool workshops, small boutique finance offices, 8-10 person teams, $1000-1200 per 4-hour workshop, executives sold by live agent + cron + Telegram demo, local Linux model server (Qwen 3.5 8B), data sovereignty pitch, OpenClaude + cron + Telegram bot
summary: Alex Rojas runs 4-hour AI tool workshops ($1000-1200) for 8-10 person boutique-finance offices. Sales pitch lands when participants see a live OpenClaude agent + cron job + Telegram bot demo in the closing hour. Alex is now also building a local Linux server with Qwen 3.5 8B (running on his old gaming PC: GeForce RTX 2070 + Core i7 9th gen, on Pop!_OS for friendlier CUDA support) — building a 'nothing leaves your network' product for finance clients caring about data sovereignty.
-->

[01:45:54] Alex Rojas: Yeah, so I just, a little update for everyone.
[01:45:57] Alex Rojas: I've been doing a lot of, um,
[01:46:00] Alex Rojas: Workshops on AI tools, specific for, like, small boutiques, I think what you guys have said a lot in the call, it is true that, you know, everyone's getting these superpowers, some way or another, the workshops that I've been giving, it's like small boutique offices, like small operations, maybe eight to 10 people, and they're specialized in finance, and yeah, they have really seen their workflows changed [tool:AI tool workshops].
[01:46:36] Alex Rojas: Many of them are like, they're usually like two days long, and many of them are like, you know, I'm going to be out of a job in a matter of months, but like, part of these things is like, no guys, like people that don't know how to use these tools are going to get out of the work market.
[01:46:58] Alex Rojas: But somehow, you know, that has
[01:47:00] Alex Rojas: ▶ has been brought in a lot of demand, a lot of my time, and I'm also, like, after taking these workshops, I have developed a lot of these local models, following Juan's example.
[01:47:17] Alex Rojas: Also, he gave me some good advice.
[01:47:19] Alex Rojas: So now I have, like, a Linux server, and I'm trying to develop, because a lot of these questions of executives were always like, oh, what about the data, you know?
[01:47:31] Alex Rojas: What about the data?
[01:47:33] Ty Wells: And, you know, that's where the enterprise accounts, but I'm also exploring these, trying to go local.
[01:47:42] Ty Wells: I'm doing Qwen 3.5, and, you know, took my gaming PC and used it as because I shifted from gaming to having it like the AI hub, and it's been amazing.
[01:47:56] Ty Wells: Like, it's pretty cool.
[01:47:57] Alex Rojas: So I'm trying to develop, like, a product.
[01:48:00] Alex Rojas: So to tell them, like, hey, guys, I can set this system and nothing is going out of your network.
[01:48:09] Alex Rojas: ▶ So I think, like, somehow, like, in all these, what you have said, like, this data sovereignty, like this privacy, it's going to be relevant for, like, certain industries.
[01:48:22] Alex Rojas: And, you know, I want to keep up with, with that and, you know, hopefully get a product ready to, you know, for clients.
[01:48:34] Alex Rojas: So I've got a quick question for you.
[01:48:36] Alex Rojas: You're, I was trying to find a good use for my gaming PC that I no longer use because I switched to a Mac book and that's all I use.
[01:48:45] Alex Rojas: So it's just sitting there churning.
[01:48:47] Alex Rojas: What are your specs on there?
[01:48:48] Alex Rojas: And are you running the 122 billion parameter one or the nine?
[01:48:52] Alex Rojas: I'm actually in the, the 8 billion parameter.
[01:48:56] Alex Rojas: Okay.
[01:48:56] Ty Wells: And it's, it works amazing for, um.
[01:49:00] Ty Wells: You know this Whisperflow app?
[01:49:02] Ty Wells: Yeah.
[01:49:02] Alex Rojas: I built my own Whisperflow with Qwen, and it's amazing, like, you just need, I do use as the, I restarted with Pop!_OS, I don't know if you know it, instead of Ubuntu.
[01:49:17] Ty Wells: Okay.
[01:49:18] Alex Rojas: So it's like a version that it's more, it's a Linux version that it's, yeah, it's kind of friendlier for AI.
[01:49:27] Ty Wells: Okay.
[01:49:29] Ty Wells: For CUDA.
[01:49:30] Ty Wells: And...
[01:49:30] Ty Wells: How many, how many gigs of RAM you have?
[01:49:32] Ty Wells: What kind of graphics card are you using, the GPU or the CPU?
[01:49:36] Ty Wells: What do you...?
[01:49:36] Ty Wells: Yeah, have a GeForce RTX 2070 [tool:GeForce RTX 2070].
[01:49:40] Ty Wells: It's actually a bit old, maybe eight, eight years old.
[01:49:44] Alex Rojas: Okay.
[01:49:45] Ty Wells: So it's Core i7 and ninth generation.
[01:49:50] Paul Miller: Yeah, it's, but it's surprisingly, like, very good, you know, like, for this experience.
[01:49:56] Paul Miller: I think I've found a solution.
[01:49:58] Paul Miller: Yeah, because I use Whisperflow every...
[01:50:00] Paul Miller: Constantly, so that's what I could pop in there, and I've got a, I think I have a 4070 in there, so that should be able to handle that with probably 64 gigs or something.
[01:50:13] Paul Miller: Yeah, if you want, you know, because it was, I was surprised when it worked.
[01:50:20] Paul Miller: I can send you an MD file.
[01:50:23] Paul Miller: I just, like, hey, you know, send me the MD file with all the stack that I used.
[01:50:27] Paul Miller: So if I want to, like, implement these in some other machine.
[01:50:30] Paul Miller: Yeah, no, it's just on and I don't use it at all.
[01:50:33] Paul Miller: I don't even touch it.
[01:50:34] Paul Miller: I don't even touch my monitor that I have next to it, but I, that's a good use case in there.
[01:50:38] Paul Miller: I will definitely, because my, I run the 122 on my MacBook and it, it runs fine.
[01:50:44] Paul Miller: Okay.
[01:50:44] Paul Miller: But, you know, it's, I'm doing other stuff too.
[01:50:47] Paul Miller: So I would, I would prefer to put that over on.
[01:50:50] Paul Miller: That's a good idea.
[01:50:53] Paul Miller: One of the things I found, thanks, Alex.
[01:50:57] Paul Miller: It's that, that's a, that's a great idea.
[01:50:59] Paul Miller: you.
[01:50:59] Paul Miller: you.
[01:50:59] Paul Miller: It's not.
[01:51:00] Paul Miller: Something I've done as well, one of the things I found, and I had the same issues, I think you must have, when you selected the version of Linux, because Linux can be quite, not behave with the CUDA drivers, I ended up taking my dev box and making it into a large physical kind of VPS server instance.
[01:51:26] Morgan Cook: I run Dokploy on that, but Dokploy is pointing to the hardware, it knows that there's a CUDA-capable graphics card on the hardware, and then I just create a whole lot of Docker instances of LLMs or whatever I want to run locally, and then they all have access to that GPU.
[01:51:53] Alex Rojas: If you've got apps that want to do that, and then you can...
[01:52:00] Alex Rojas: can build stuff locally and then deploy them to VPSs that have got GPU access.
[01:52:05] Alex Rojas: It kind of sets up a nice little playground.
[01:52:08] Alex Rojas: So not only are you reusing your GPU locally, but you've got something that you can then deploy to a live environment without having to sort of burn through GPU dollars.
[01:52:21] Alex Rojas: Morgan, you had your hand up.
[01:52:27] Alex Rojas: A question for Alex about his workshops.
[01:52:31] Alex Rojas: How receptive are all the boutique shops in those workshops and how much are they willing to pay, if you don't mind sharing that?
[01:52:39] Alex Rojas: And is there a potential for any kind of service upgrades or expansion?
[01:52:45] Alex Rojas: Yeah, I think the way that I've gotten through, it's through word of mouth.
[01:52:50] Alex Rojas: Kind of these AI tools through the postings, LinkedIn, and also network of friends.
[01:52:58] Alex Rojas: So...
[01:52:59] Alex Rojas: So...
[01:53:00] Alex Rojas: I got in touch with the, it has been, like, top executives, like, meaning, like, partners of the firms, are, are the, were the ones, like, driving these initiative, so, you know, that facilitates a lot of things, maybe initially they're, like, a bit, like, you know, like, this guy's gonna come, and, you know, but once we see, like, things in action, then they are all, like, wow, this is amazing, then the ball is rolling, and, for instance, what I do with, in the last one hour or two hours, we set up an agent, an OpenClaude agent, and we just make, like, a couple of cron jobs for the office, that, you know, and then everyone compared to their, to the bot of Telegram, and I think when, when they see that happen,
[01:54:00] Alex Rojas: They, that's when they are like sold.
[01:54:02] Alex Rojas: Uh-huh.
[01:54:03] Alex Rojas: Like, well, this is amazing.
[01:54:05] Alex Rojas: ▶ And I'm doing a four hour courses for a thousand, no, we have like a thousand and two, $1,200.
[01:54:18] Patrick Chouinard: Approx, I would say.
[01:54:20] Patrick Chouinard: And that is like for four hours.
[01:54:22] Patrick Chouinard: I think there could be more follow ups, but like, um, um, I think you enter a lot in this client, um, you know, whatever the, what Ty was saying about the customers, you know, like all these little things fell and I need to SSH into the, into their machine.
[01:54:42] Patrick Chouinard: And, uh, it takes a lot of time.
[01:54:45] Patrick Chouinard: So to be honest, I have, I haven't explored the, the follow on things.
[01:54:50] Patrick Chouinard: I'm more like, maybe I just have these material ready.
[01:54:53] Patrick Chouinard: The next one, it's like, it's easier, but, uh, maybe specific solution could be good for,
<!--SEGMENT
topic: repurposing gaming PCs — Proxmox + Dokploy + Tailscale + Twingate vs VPN
speakers: Patrick Chouinard, Alex Rojas, Ty Wells, Paul Miller
keywords: Proxmox hypervisor, Dokploy, Tailscale, Twingate (preferred over VPN), Caddy vs Traefik reverse proxy, Prometheus + Grafana monitoring, gaming PC as AI hub, only ~0.1% compute for plumbing, CUDA passthrough
summary: Patrick recommends Proxmox over Dokploy as the baseline for a repurposed gaming PC AI server: Claude Code knows how to drive its CLI, supports auth/reverse-proxy/VPS, and the plumbing infrastructure uses ~0.1% of a gaming machine's compute leaving everything else for the AI. Add Prometheus + Grafana for free dashboards, then expose via Tailscale (or Twingate for tighter access — pin to specific IPs only, vs VPN's open-network model). Alex describes his setup that calls his gaming PC over Tailscale only for specific jobs, keeping the model dormant otherwise.
-->

[01:55:00] Patrick Chouinard: I'm getting a follow-on, but yeah, that's a prox, what I've done and prices.
[01:55:12] Patrick Chouinard: Patrick, you had a...
[01:55:15] Patrick Chouinard: Yeah, actually, I just wanted to bounce on what you said about the gaming computer being repurposed for those.
[01:55:24] Patrick Chouinard: I love the idea, and obviously mine has been under my desk doing that for a while.
[01:55:31] Patrick Chouinard: But if I can recommend something, I love Proxmox as a platform for games, because, yes, Dokploy is awesome, but Proxmox, it's a real baseline for an infrastructure [tool:Proxmox].
[01:55:45] Patrick Chouinard: Claude has access, there's a good CLI, so Claude can do a whole lot of things for you directly, Claude Code, I mean.
[01:55:53] Patrick Chouinard: And on top of that, it gives you a platform to do, yes, the AI stuff, so you can get...
[01:56:00] Patrick Chouinard: You access to the GPU and create your VPS for OpenClaude and all of that, but those needs infrastructure, they need auth, they need reverse proxy, and Proxmox is awesome to deploy those service, there's boilerplate everywhere, Claude Code knows how to deploy those things easily [tool:Dokploy].
[01:56:20] Alex Rojas: ▶ So it's one interface, one place, you can have everything running on it, and the vast majority of the plumbing infrastructure you're going to deploy will use 0.1% of the compute power of a good gaming machine.
[01:56:35] Alex Rojas: So it leaves everything else for the AI.
[01:56:38] Alex Rojas: You throw a Prometheus and Grafana on there and you have graph for your own infrastructure and dashboards and everything, alerts all out of the box that you can do in a week [tool:Prometheus] [tool:Grafana].
[01:56:50] Alex Rojas: And then add it to Tailscale so you can access it remotely [tool:Tailscale].
[01:56:57] Alex Rojas: Tailscale or Twingate, depending.
[01:57:00] Alex Rojas: that's still VPN.
[01:57:02] Alex Rojas: ▶ VPN, I'm not a huge fan.
[01:57:05] Alex Rojas: It's way too open.
[01:57:06] Alex Rojas: love Twingate [tool:Twingate].
[01:57:06] Alex Rojas: You pointed that this is the IP you have access to.
[01:57:09] Alex Rojas: That's it.
[01:57:09] Alex Rojas: That's all.
[01:57:11] Alex Rojas: Yeah.
[01:57:12] Alex Rojas: What's the name of the tool?
[01:57:14] Alex Rojas: Twingate.
[01:57:15] Alex Rojas: No, the previous...
[01:57:17] Alex Rojas: Oh, Proxmox.
[01:57:19] Alex Rojas: Or Proxmox.
[01:57:20] Alex Rojas: Yeah, Proxmox.
[01:57:21] Patrick Chouinard: Okay.
[01:57:22] Patrick Chouinard: But actually, I do the same.
[01:57:25] Patrick Chouinard: I do...
[01:57:26] Patrick Chouinard: Actually, I started like deploying everything in VPS.
[01:57:30] Patrick Chouinard: Instead of Vercel and use Tailscale to control like the remote computers in the client.
[01:57:38] Patrick Chouinard: And then like I do like kind of a cluster.
[01:57:40] Alex Rojas: ▶ So all the apps that I post, they call to my gaming PC for certain jobs only.
[01:57:48] Ty Wells: And yeah, exactly through Tailscale.
[01:57:51] Ty Wells: And it is amazing, especially because like, I don't know how he does that, but...
[01:57:59] Patrick Chouinard: physically
[01:58:00] Patrick Chouinard: For certain jobs, it only calls the computer for the specific job.
[01:58:05] Alex Rojas: It's not that the model is always up and running, and it's pretty...
[01:58:11] Patrick Chouinard: I think that's a CUDA system, and it has worked pretty well.
[01:58:15] Alex Rojas: So, yeah, a lot to experiment.
[01:58:19] Alex Rojas: I'll check that out, Patrick, there.
[01:58:22] Ty Wells: Well, now that we all have an experienced operator that we pay $100 a month for, I mean, it's not worth not doing it.
[01:58:32] Ty Wells: You don't need to be an infra mastermind anymore to build those environments.
[01:58:38] Ty Wells: Claude can take on for you on those.
[01:58:42] Ty Wells: Yeah, totally agree.
[01:58:44] Alex Rojas: Good stuff, Alex.
[01:58:46] Paul Miller: Patrick, I'll be reaching out to you because when I get back to Omaha, I will definitely be putting that gaming PC to use.
[01:58:52] Paul Miller: The only reason I...
[01:58:53] Paul Miller: Actually, I do have a VPN into it.
[01:58:55] Patrick Chouinard: Oh, I will, so I may reach out to you before I get back.
[01:58:59] Patrick Chouinard: Yeah, it prompts mine.
[01:59:00] Patrick Chouinard: Create a reverse proxy, tailscale into that, and then that's it.
[01:59:06] Patrick Chouinard: Yeah.
[01:59:06] Patrick Chouinard: That reverse proxy, it's Caddy, right? [tool:Caddy]
[01:59:09] Patrick Chouinard: Caddy is also a tool for...
[01:59:11] Patrick Chouinard: Yeah, there's that.
[01:59:13] Patrick Chouinard: Personally, I prefer Traefik, but.. [tool:Traefik].
[01:59:16] Patrick Chouinard: Okay.
[01:59:17] Patrick Chouinard: Yeah.
[01:59:19] Patrick Chouinard: You're going to have fun, Ty.
[01:59:21] Patrick Chouinard: I'm just burning power right now.
[01:59:23] Patrick Chouinard: I'm just burning energy.
[01:59:25] Paul Miller: It's like I got a data set under my desk and not making any value out of it, so I'll be fixing that.
[01:59:30] Paul Miller: Where do you think my OpenClaude is installed?
[01:59:33] Paul Miller: Oh, yeah, I know.
[01:59:34] Patrick Chouinard: That's where you talk about it all the time, and I'm thinking, I've got this box under my desk, I'm not doing anything with.
[01:59:41] Ty Wells: I am definitely putting that to use.
[01:59:43] Patrick Chouinard: Yep.
[01:59:44] Patrick Chouinard: Oh, yeah, man.
[01:59:46] Ty Wells: Yeah.
[01:59:46] Ty Wells: Brilliant.
[01:59:47] Ty Wells: Thanks, guys.
[01:59:49] Ty Wells: We'll wrap it up.
[01:59:50] Ty Wells: We'll wrap it up there.
[01:59:52] Patrick Chouinard: Have a great week, and I look forward to catching up next week.
[01:59:56] Patrick Chouinard: Yep.
<!--SEGMENT
topic: everything-claude-code repo + wrap-up
speakers: Patrick Chouinard, Ty Wells, Paul Miller
keywords: everything-claude-code, Anthropic hackathon winner, hundreds of agent plug-in skills, system that upgrades Claude Code, recently released
summary: Patrick highlights everything-claude-code — an Anthropic hackathon winner with hundreds of agent plug-in skills tied together as a system that upgrades Claude Code, not just a library. Patrick puts the link in chat. Brief signoff.
-->

[01:59:57] Patrick Chouinard: Just, guys, go take a look at the link.
[02:00:00] Patrick Chouinard: Yeah, I've put for everything Claude Code.
[02:00:03] Patrick Chouinard: That's something I forgot to mention.
[02:00:05] Patrick Chouinard: It's absolutely insane.
[02:00:07] Ty Wells: It's a project that came out of hackathon in Entropic, and they created something that has like hundreds of agent plug-in skills, but all tied together [tool:everything-claude-code].
[02:00:20] Ty Wells: It's not just a library.
[02:00:21] Ty Wells: ▶ It's really a system that upgrades Claude Code.
[02:00:25] Ty Wells: I'm going through it right now.
[02:00:27] Ty Wells: It's pretty incredible.
[02:00:28] Ty Wells: So is there a site connected to it?
[02:00:32] Patrick Chouinard: So if we look up everything Claude Code?
[02:00:35] Paul Miller: Yeah, actually, I put the link in the chat.
[02:00:38] Paul Miller: So they just released the winner?
[02:00:40] Paul Miller: This is just the winner just coming out from when they have the hackathon?
[02:00:44] Paul Miller: I don't think it's just just released, but it's within a month or two max.

=== UNRESOLVED SPEAKERS ===
- Ryan C (appears 58 times, example: "Music has been.")
- Scott Rippey (appears 78 times, example: "Not too many things.")
===