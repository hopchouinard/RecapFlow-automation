=== SESSION ===
date: 2026-09-08
duration_estimate: 1h 46m
main_themes: token usage & subscription limits (Codex; Claude/Fable); model comparison (GPT-6/Astra vs Fable 5.1 vs GLM); AgentDeck agent observability tool; RAG agent model selection; AI-assisted ERP business advisor; local RAG document search security; finding AI consulting niches; market saturation and personal branding; lead generation tactics; member project updates (Shakur; Juan; Ryan); AI voice recorders/note-takers (Fieldy; OMI; Limitless); ChatGPT scheduled tasks and personalized news radar; context-rich prompting; anti-sycophancy AI configuration ("thinking partner; not yes man"); AI-curated news routines (weekly Kindle digest; ChatGPT morning briefing; Cloudflare publishing platform); personalization and model memory; humans as the bridge and the bottleneck ("HGI; not AGI"); Agent Deck as an AI-to-human harness; human cognitive tokens and cognitive load

<!--SEGMENT
topic: Token burning and subscription limits
speakers: Paul Miller, Patrick Chouinard, Hemal Shah, Ty Wells
keywords: Codex, Claude, Fable 5.1, token limits, weekly reset, context window, $100 max plan, OpenAI, effort setting, web search calls
summary: Opening banter about how quickly participants are burning through their Codex and Claude/Fable subscription tokens. Patrick explains that long-running sessions with large context windows consume limits fastest, and Hemal reports Fable 5.1 at high effort exhausted his five-hour limit in minutes.
-->

[00:00:22] Paul Miller: Hey, Patrick. I'm happy to host today, so if you want me to do that.
[00:00:28] Patrick Chouinard: Paul? Paul?
[00:00:34] Hemal Shah: Hey, Patrick. Hey, Paul. How are you? How was a long weekend? I don't know if Canada and New Zealand was long, but sorry.
[00:00:43] Patrick Chouinard: Yeah, but we have the same Labor Day here. But since I'm in vacation, it doesn't change a whole lot for me.
[00:00:53] Hemal Shah: Still working, huh?
[00:00:58] Patrick Chouinard: I'm burning more tokens.
[00:01:04] Hemal Shah: It's so hard to get off of the computer, you know, once things are going, you constantly want to see the progress and...
[00:01:14] Patrick Chouinard: I mean, I'm on the 100 bucks max account for Codex [tool:Codex], and I've burned through three weekly reset yesterday.
[00:01:27] Paul Miller: I was going to ask, where are all your tokens burning at the moment, Patrick?
[00:01:34] Patrick Chouinard: You're going to see that.
[00:01:46] Paul Miller: It's great having two big fancy models out there now to lay off against each other.
[00:02:03] Patrick Chouinard: Yeah, but they're definitely not the same at all.
[00:02:10] Paul Miller: And thank goodness for that. Because they can do complementary things, theoretically.
[00:02:17] Hemal Shah: I use Fable. So I have $100 max plan for Claude [tool:Claude]. I use Fable 5.1 [tool:Fable 5.1] for one of the query. And I think I put it on the effort was high. Within five minutes, it consumed my entire five hours limit. <Q>So how do you guys use Fable whenever you want to try it out?</Q>
[00:02:42] Patrick Chouinard: <A>Single run. Not long run. Because I try to avoid filling its context window. Because that's what consumes your limit. If you keep on talking when you have 500, 600, 800,000 tokens, well remember that every time it talks back, it sends back those eight to a hundred thousand tokens every time. If you ask it to do architecture as one shot as possible, that's not too bad. But if you leave it working, it's going to burn through your limit.</A>
[00:03:21] Hemal Shah: Yeah. Because it was making multiple web search calls and things like that. So I think that explains it.
[00:03:30] Ty Wells: That's what we're talking about. Six or 5.1?
[00:03:35] Paul Miller: Using both, making sure that we don't burn through the Fable tokens and Patrick's been burning through OpenAI [tool:OpenAI] tokens.
[00:03:48] Ty Wells: You know, I started doing some work on Codex two days ago. I started a couple of days ago and I'm still on it. CMUX has seen me maybe an hour over the last few days. Yeah, it's been working out well for me for what I've been doing. I've really been doing it for computer use, but it also feeds back into my queue any issues it finds, and then Claude fixes them. ▶ So I've got this little loop going here that I'm just watching TikTok and other stuff.
[00:04:33] Paul Miller: And what about the golf? How's the golf going?
[00:04:36] Ty Wells: I haven't golfed in a few days, but I'm on a sabbatical.
[00:04:42] Paul Miller: Just got to watch the handicap.
[00:04:45] Ty Wells: Well, if we don't do anything, it won't move.

---

<!--SEGMENT
topic: RAG agent model selection
speakers: Hemal Shah, Daniel Zivkovic, Paul Miller, Ty Wells, Patrick Chouinard
keywords: RAG agent, GLM 5.3, Qwen, test harness, LLM-as-judge, Gemini, OpenRouter, non-deterministic evaluation, Chinese models, cost optimization, baseline
summary: Hemal seeks recommendations for a RAG agent model after GLM 5.3 kept flipping answers across 50 test-harness cases. Daniel argues for establishing a baseline with the smartest model before optimizing cost; Paul recommends OpenRouter's task rankings; Patrick endorses GLM 5.3 Flash for cheap long-running work.
-->

[00:07:37] Paul Miller: For anyone that's new on the call, I think, Kris, you're a new chap. We have a bit of a go-round where then everyone can give us an update of where they're at and if they've got any questions.
[00:08:14] Paul Miller: Let's start with you, Hemal. How's it going?
[00:08:20] Hemal Shah: Based on last week's discussion, I continue experimenting with loop engineering for AI co-pilot. Some of the ideas that Brandon suggested. I tried using Chinese models. One interesting issue I'm finding is that I tried using GLM 5.3 [tool:GLM 5.3] for my drag agent. And for some reason, when the test harness is going through, there are like 50 questions. Each iteration, it flips its answer to a level where the test harness fails, so a coding agent is recommending me to use some different Chinese models instead of GLM 5.3, and I wanted to check with this group if there is any good recommendation, which model could be better for a rag agent that I can try.
[00:09:25] Daniel Zivkovic: <Q>Maybe your rag is broken. How do you know you're returning relevant content to the present? You know, junk in, junk out. How do you know the rag itself is good that your AI is reasoning against? Did it work with more expensive models before?</Q>
[00:09:39] Hemal Shah: So, it went through 10 iterations, and each iteration, it was flipping the answers on some of the test cases. Out of 50 test cases in the harness, it will respond with different variations to that. And that is how it is saying it is flipping too much to narrow down and come up with a proper solution. I'm using QUENT for LM as a judge [tool:LLM-as-judge], so it is a non-deterministic judge who is trying to gauge what agent is responding. But I have not tried with Gemini [tool:Gemini]. I started with Gemini or the expensive model, but it was too expensive.
[00:10:29] Daniel Zivkovic: ▶ You have to go with the baseline, like you pay first time to get the good numbers, then you optimize the price. If it never worked, you will not know.
[00:10:37] Hemal Shah: I have two variables to test.
[00:10:39] Daniel Zivkovic: Bad model or bad drag or bad prompt. Like it's just too ambiguous. Start with the smartest one. So what I learned to save on Fable was just to take it to medium thinking. But I'm not programming now. I'm restraining myself. I'm thinking how to kind of develop business. So you start with the smartest. Get the baseline you want, then you optimize by cost. That's my opinion about everybody's free.
[00:11:07] Hemal Shah: So I started with, not Fable, but I started with one of the smarter version of Gemini, but it cost me $100 just before I finished a couple of loops to really get to...
[00:11:22] Daniel Zivkovic: <Q>Did you get good results for the 100 bucks?</Q>
[00:11:26] Hemal Shah: No, it was still going through...
[00:11:28] Daniel Zivkovic: So it's not the problem with AI, you can throw it, you have junk in. So I don't know how you start your project, but I normally try to have my clients define what good looks like. They have to give me example of a good answer, and then I work backward to get that answer through AI.
[00:11:45] Hemal Shah: So I have like 50 test harnesses with good answers, good question and good answers, and trying to come up with that ideal solution. These test cases pass sales, but with expensive model, like I'm saying, it was not able to go through all the things because it already hit $100 cap that I put down. So I might have to increase that cap to really see that.
[00:12:15] Daniel Zivkovic: <Q>What is your rag? What is behind the scene? What do you use? What vector database? What index? What type of questions?</Q>
[00:12:22] Hemal Shah: It's all type of questions, adversarial questions, like random was saying, confuse Christy and good happy case scenario, more contradictory follow ups, five turn questions, things like that. It's very comprehensive test suite.
[00:12:55] Paul Miller: Hemal, maybe you just want to put a post in the forum. And we can have a look at it offline with what you're trying to do.
[00:13:05] Hemal Shah: Just from the Chinese model's perspective, QAN versus GLM 5.3, any recommendation on that for good agentic one that anybody has good success or result?
[00:13:18] Paul Miller: <A>What I tend to do with vetting them, if you go into Open Router [tool:OpenRouter], Open Router's got an index of where they rate the best ones for different tasks. Start with that, because then you can identify what currently is the best for base agentic or what's good for programming. That's quite a good independent list.</A> [link:OpenRouter model rankings]
[00:13:43] Ty Wells: Hemal, I would say you definitely have to get that first pass through on whatever model you choose to use. You've got to get at least one, because without that, it's going to be hard to... Because you said it didn't get all the way through, right? But the data that you, the results you were getting were somewhat off. They were not correct in the runs that did make it through?
[00:14:13] Hemal Shah: Yes, Ty. So the whole idea that I was experimenting with was I didn't want to give it a specific architecture. I just gave it technology stack to use Python and a few things so it doesn't keep on bouncing around. So I gave very minimal technology stack and let it, idea was to let it run loose on based on my test harness and evals, you know, come up with the ideal solution.
[00:14:37] Ty Wells: Yeah, no, I understand. But yeah, the money is probably running through there, right? And you're not sure how far it's going to go. But I mean, if I really had high confidence in that approach, I would let it run to, I mean, it's like a one shot if you get to the end, right? But you'll never know unless you let it run all the way through, but I like that approach though, it's interesting.
[00:15:07] Patrick Chouinard: ▶ If there's one [Chinese model] I can recommend, I've been using GLM 5.3 Flash [tool:GLM 5.3 Flash] a lot recently, and I'm very happy with the result. Actually, Recap Flow has now moved completely on GLM 5.3, and I went from between 80 cents and $1.10 per run — to do all the Recap and the Recap Flow post and all of the integration with the LensDB in the background — and now that I moved entirely to GLM, it's like 9 cents. Even if it's not absolutely the top tier Fable class type of model, you can leave it to run for a day or two and you're not going to get another model.
[00:16:00] Hemal Shah: Yeah, it only cost me $1. I let it run for a couple of nights versus Gemini was $100. So yes, it is super cheap.
[00:16:11] Patrick Chouinard: And the results are very nice, actually. I don't have any complaint on the result I got so far.

---

<!--SEGMENT
topic: AgentDeck agent observability tool
speakers: Patrick Chouinard, Paul Miller, Juan Torres, Ty Wells
keywords: AgentDeck, Astra, observability, Claude Code, Codex, Hermes, T3 code, token tracking, Prometheus, Grafana, Loki, alert manager, harness monitoring, multi-host
summary: Patrick demos AgentDeck, a monitoring surface he built with Astra to track all his live coding agents (Claude Code, Codex, Hermes) across hosts, showing token usage, sessions, branches, and attention requests. Juan praises its business value; Patrick describes the Prometheus/Grafana/Loki backend and plans for fleet-wide observability.
-->

[00:16:38] Patrick Chouinard: I can show a little bit of what I've done. Let's say I've overused Astra [tool:Astra] in the last two, three days. Like I was telling Paul earlier, just yesterday I went through a three-weekly reset in a single day. What I came up with — I decided that I had too many harnesses at the same time and it was getting harder and harder to keep track on what was doing what where and what needed my attention, so I created this guy called AgentDeck [tool:AgentDeck].
[00:17:30] Patrick Chouinard: Basically it monitors all of my live agents, it tracks my usage on each of them, token use — as you can see I've been using Codex a little bit more than the others. That's just a day, by the way.
[00:17:45] Paul Miller: <Q>You mentioned last week that you were going to look at using the Pi agent, is this with Pi agent or what?</Q>
[00:17:58] Patrick Chouinard: <A>Nope. This is simply, I just gave the task to Astra at a high level, and I wanted to have a monitoring or an observability surface for all of my agents. So Claude, Codex, Hermes, and including running Claude and Codex inside of T3 code. So now they're all monitored, and whenever each and every one of them has something for me, a question, a notification, it stopped and it needs my attention, I see it here. It shows in my inbox.</A>
[00:18:44] Patrick Chouinard: Right now you see I only have four finished and two interrupted, but if I go in the harness section themselves, I'll see the session. You can see I've been abusing my Codex a little bit lately, and those sessions are all completed, but I know where they are, I know how many tokens were consumed, I know which branch they were working on, and if there's unresolved attention, it would pop up so I could actually see the unresolved attention requirement, and I could reply directly in it. You see here I have two hosts, because those are not on the same machine. Codex and the Claude Code are on my main machine, but Hermes is running on a Linux VM, so they are configured independently, and I have all my settings, so I can decide for each harness what functionality is activated or not, the hosts that are activated, and what harnesses reside on each host, notification, integration status. ▶ This is not a harness to replace anything. It's an observability surface to see everything going on in the sea of harnesses and agents working in the background.
[00:20:22] Juan Torres: Hey, this is great. <Q>One of the things that I wanted to ask is why Hermes doesn't have the weekly bar of percentage of usage.</Q>
[00:20:32] Patrick Chouinard: <A>Well, it is using my Codex subscription, but the Hermes harness itself doesn't show the subscription consumption, but I see it through the Codex. And otherwise, if it's not on subscription, it's using GLM and that's direct OpenRouter API connection. So there's no subscription. Hermes there is more of the operator of my infrastructure, and Claude Code and Codex are the builder, but I'm having Fable 5.1 working on a large upgrade to the capacity of Hermes in the backend.</A>
[00:21:26] Patrick Chouinard: The reason why you don't see a lot in Claude Code is simply because I'm running — every time my session reset, I restart a run with Fable, and I'm just like, keep on, continue, continue, continue. It's just racking up using the entire available token. So probably in a day or two, I'm going to see a more complete result.
[00:22:00] Juan Torres: That's great. ▶ Honestly, I feel like a lot of businesses could benefit from having a tool just like this in order to actually create token observability. A lot of businesses are not implementing AI in their modus operandi, but I feel like this is something that, even if you're home lab, you benefit from having a degree of observability.
[00:22:31] Patrick Chouinard: And it actually accumulates the history. So I'm eventually going to be able to have a full observability dashboard with full tracking of token consumption, not only per harness, but per harness, per installation, because I'm running Claude Code installation on a lot of the VMs in my environment. So it's going to be able to monitor my entire harness operation wherever they may live in my home environment.
[00:23:09] Juan Torres: <Q>Have you thought of combining that observability with a Prometheus observability of your computer, computational environments?</Q>
[00:23:17] Patrick Chouinard: <A>Actually, there is an alert manager and there is a Prometheus server monitoring all of that and also a Loki log server. All my logs go via syslog, but it's aggregated through a Loki log server. I'm trying to aggregate as much as possible. So basically the backend is Prometheus, alert manager, Loki, Grafana, Canada, Nats, and Authentic and Trafic.</A> [tool:Prometheus] [tool:Grafana] [tool:Loki]
[00:24:11] Ty Wells: That's a solid setup. Why do I even build things?
[00:24:20] Patrick Chouinard: Yeah, but you're finishing and you're putting the nice touch on top of the rough idea I created.
[00:24:37] Paul Miller: I can't say that I've seen a rough idea that you've presented ever.
[00:24:42] Ty Wells: Your version of rough is like polished, right? It comes out of the box polished. White gloves and everything. Thanks, Patrick.
[00:24:52] Paul Miller: Did you end up doing anything with the Pi stuff you talked about last week?
[00:24:59] Patrick Chouinard: No, not this week. Let's just say that I was token maxing both Astra and Fable, so...
[00:25:06] Paul Miller: Yeah, it's a bit hard when GPT-6 came out, Astra. You weren't going to switch to looking at Pi in the weekend when you got that on the table.
[00:25:17] Patrick Chouinard: Well, it's probably going to be built by the whole custom harness and the whole connectivity to leverage it from Claude Code and from Codex through T3 code. It's probably going to be built by Astra in reality. I have just so many weekly resets to burn through.

---

<!--SEGMENT
topic: Positioning as forward-deployment engineer
speakers: Daniel Zivkovic, Paul Miller
keywords: forward-deployment engineering, consulting, prototyping, Figma, Fable 5.1 medium thinking, unknown unknowns, Anthropic Tariq, business development, India consulting firms
summary: Daniel explains he's stepping back from coding to sell — positioning himself as an AI-assisted forward-deployment engineer who prototypes with AI instead of Figma. He sustains Fable usage by using medium thinking mode and applies Anthropic's "unknown unknowns" framing to explore business directions.
-->

[00:25:55] Daniel Zivkovic: Good to see everyone. Last week, I declared I'm going to quit the addiction of coding because I started feeling like alcoholic or chain smoker, it's time to start selling. My contract ends in three months, and market is not easy what I hear from my friends, so I'm kind of preparing my fishing nets for the next big one. What I was researching is AI-assisted research, and I just put the post on my website — all big companies are talking about forward-deployment engineering, they're ramping their teams, but it's hard to change the mindset of the developers who just like to develop, cannot talk to business. ▶ So I'm trying to position myself as somebody who talks to business people, gets what they need, but helps them visualize that, because I no longer need Figma, I no longer need to be front-end developer, I can quickly prototype things with AI and tell them, what do you like more, A or B? Because they often cannot vocalize the right requirements, what they want.
[00:26:50] Daniel Zivkovic: This is like a long haul fishing trip, but I'm positioning myself as somebody who's going to work with big consulting companies, and I like to work from companies from India because nobody shows up in the office, I can sit here same day, all day, and not be kind of having to go to office three days a week.
[00:27:10] Daniel Zivkovic: So not coding, but using Fable 5.1 on a medium — that's what I didn't finish. So I'm able to sustain without maxing my Fable usage by tuning it down to medium thinking, and I still get good results, and Fable is very creative, I find, sees my blind spot, unknown unknowns, things I haven't figured out. Like, if you watch Anthropic Tariq, he has really good talks about finding your unknown unknowns, like the territory where you're going. And also, like this known unknowns, this is something when you see it, you will know it. So I'm trying to apply this principle where I'm developing different prototypes, and then figuring out which one rhymes with me. So, no coding, just contemplating planning my fishing trips for the next big customer when this one runs out.
[00:28:00] Paul Miller: Did you play with looking at OpenAI's new model?
[00:28:05] Daniel Zivkovic: No, I didn't because... I followed everything. I have this video Intel skill. Everybody has something like that. So I just have like my skill, watch YouTube videos every weekend, transcribed using Gemini. But it's using a background, it's using screen, so I see what's happening behind. And then I run different briefings, I have nuggets. I'll share that one with you as well. And it resurfaces what's important. ▶ So the consensus among the people who use Astra is that it's amazing for coding, for landing pages, but not for thinking. Fable 5.1 at medium pairs with Astra. So why spend the money? So I always use Codex, any models like GPT 5.6 and any Sol at high thinking for reviews. So even if I have the good idea with Fable, I would like a peer review for the blind spot from GPT. I'm not coding this week, so I haven't tried it. But people who said they love it, but not for thinking. It overdoes it. That's a consensus.

---

<!--SEGMENT
topic: GPT-6 vs Fable model comparison
speakers: Paul Miller, Patrick Chouinard, Daniel Zivkovic, Ty Wells
keywords: GPT-6, Astra, Fable, computer use, Theo comparison, every.to, Dan Shipper, Compound Engineering, Kieran, QA automation, Opus 5, succession paperwork
summary: Paul shares Theo's GPT-6 vs Fable comparison slide — GPT-6 has moments of coding brilliance but also dumb mistakes, while Fable is consistently good. Patrick notes Astra excelled at a 3-hour government-forms research task; Ty reports GPT-6 computer use is so good it replaced his QA hire, feeding fixes to Opus 5. Daniel shares his every.to / Compound Engineering validation source.
-->

[00:29:09] Paul Miller: Patrick, can you give me, or you've shared the access as well?
[00:29:15] Patrick Chouinard: Already gave it, approved it.
[00:29:18] Patrick Chouinard: And just to answer Daniel, actually there's one thing I've done with Astra this week that I found it did better than Fable in the thinking aspect. I have some finance stuff to be doing and taxes stuff to be doing because my mom passed away. Long story short, there's a lot of admin stuff that required drilling down into government website, finding forms, figuring out which form to send to which department. Then basically I explained the problem to Astra, gave it to the computer and say, go for it, find me all of the forms. And wonderful. Everyone I need to contact, whatever I need to do in order to get this specific thing done for the finance of the succession, it worked for about three hours, and it gave me, like, here's step one, two, three, four, five, what you need, here's the form, here's how you need to fill them, pretty much everything done.
[00:30:21] Daniel Zivkovic: That's nice, but to me, that's accounting, that's still not thinking. For me, thinking is creative thinking, when I don't know what I want. With me, most problems start with gut feeling. I have a pain, I have frustration, and I don't know, I just feel it. So that's where Fable kicks in to uncover my feeling and map into requirements, but then, I like that accounting precision. They're like, boring, short, like accountant personality, really. Precise to the point. You need it, but it's sending at the end, for me.
[00:30:52] Paul Miller: Well, Theo, just the screen I'm sharing. So Theo did a GPT-6 versus five. He's been having a good play with it and pretty outspoken in terms of what he likes and dislikes. He had a very interesting slide before this one, this is at the very end of the presentation, that he pretty much said ▶ GPT-6 [tool:GPT-6] can have moments of brilliance from a coding perspective, but comes up with lots of real dumbass things along the way, while Fable is consistently good at the top level for coding. And this is kind of where he was at, because I think like you, Daniel, I look at what other people have done, let them do all their usual experiments against their own code base before I go and risk my coding stack on it. But yeah, I was fascinated to see Theo's feedback and it seems pretty good and it's pretty confident in the way it responds, but the quality of some of the outcomes a bit...
[00:32:00] Ty Wells: I can tell you for sure that at least for me, the computer use is really, really good. Like I said, I've been running that for the last three days. I was just telling my wife, I don't think the guy I just hired — I don't think I need him. He's a QA. And I really don't need him for what he's doing in terms of QA-ing the UI, because this thing is not only doing that, but it's also coming up with potential fixes, which, like I said, I'm then giving off to Opus 5 [tool:Opus 5] to vet and implement. But, you know, if you have a UI, this is my dream team right here.
[00:32:47] Paul Miller: Well, I found it pretty good with 5.6 Sol doing that computer use. That was really good. And now this seems to go on another level. And Patrick, he's saying it sort of went off at three hours and did stuff.
[00:33:00] Daniel Zivkovic: So, I just pasted the chat in the group. Like, I do let AI watch videos for me, but there is one group I pay to be a member of. This is private video for their paid sessions for the paid members. This is every.to [link:every.to] company. I follow them because three years ago, the founder, Dan Shipper, he wasn't even a programmer. He was just a writer, a really good writer. He got me in and then he hired great developers. Kieran is the guy who created Compound Engineering Framework [tool:Compound Engineering Framework], the one I religiously use for coding. So, anything you develop goes to full-grown SDLC. So, they have early access to Fable, to ChartGP, to anything. And they play a couple weeks and then give their surveys. So, this is one of those sessions that I attended recently. So, that is kind of my human check, human in the loop validation.
[00:33:52] Paul Miller: Brilliant. It's always good to have a good benchmark. Because you could watch hundreds of videos that many of the people are... They're competing for clicks.
[00:34:02] Daniel Zivkovic: Like, now I'm converging, I'm subscribing because they're figuring they say the same thing. And mostly what they do, they go to Tariq from Anthropic, they go for Anthropic, like Boris's post, and they tell you the story. I can do that too.

---

<!--SEGMENT
topic: AI-driven ERP business advisor
speakers: Ty Wells, Paul Miller
keywords: ERP, business advisor, computer use, intent capsules, Opus 5, chart of accounts, onboarding, kiosks, Rust agent, MDM, data aggregation, webinar launch
summary: Ty describes his upcoming ERP launch on the 15th, featuring a built-in business advisor that vets new business ideas and advises existing businesses from their data before they even use the software. He also discusses a Rust agent concept for aggregating data from existing systems customers won't abandon.
-->

[00:34:22] Ty Wells: It's a little crazy here, but I'm working my way through. Really haven't been doing any actual development — maybe I've just been the human in the loop, because like I said, I'm taking the computer use output, creating my intent capsules, and Opus 5 is just picking them up and implementing them. So really, I'm just sort of monitoring them and really watching computer use my Chrome, and I see the error come up, and I just move over — that's why I need Patrick's Agent Ops, because I can move over and see that it went to Fable, and then Opus, and then process in there. I've got something similar, but probably not as polished as Patrick's.
[00:35:23] Ty Wells: I'm launching to clients on the 15th. That's when I have my webinar. So that is where I'm at. I'm just polishing, really, with computer use, just polishing the UI for what we're going to. ▶ But one thing that this ERP is doing differently is for a new person getting in business, the process of understanding what it is that you're trying to do as a business is vetted before you even get into the software. So, hey, I want to start a new business — yes, you can go to ChatGPT and you can do all of that, but if you've got the back-end already built, a full ERP, this is just the front-end. So you could sort of vet yourself and see if this is even going to make sense for you.
[00:36:18] Ty Wells: So it's a business advisor for onboarding a new business because they have nothing, they have no data, they've got no accounting set up. For an existing business, the business advisor is, okay, I see your data, I brought it in, this is where I think you could use some help. What's your goal, first of all, because that's just like we do development. Once I have that goal, now let me look at your numbers to see what needs to move to shift the needle to accomplish that goal. So that advisor is built in from the ground up off of the data. Obviously, the advice will be different and relative to the business if it's new. And then for a new business, they would be required to get certain information to vet, basically the vetting process. Will this idea work? Will this business work? And it'll be there every step of the way as they make changes, as the numbers, whatever their goals are, which can change. If they change, then the numbers have to reflect. And how do they reflect? Well, you've got to go get more sales. So, okay, what do I do there? So that business advice is built in from day one. So there's no — it has a full understanding of business and the numbers don't lie. ▶ Unless you guys know of any software working that way now out of the box, most ERPs are old school built on, this is what you get, take it or leave it. And the 80-20 rule rarely applies to the usability of the software, the actual use of it. So I'm starting for that loop to continue all along, advising the business from day one.
[00:38:10] Paul Miller: <Q>How do you deal with a customer that sort of rocks up and says, they've got some accountant that say, oh, this is the way I set up new businesses, from a setting up in the accounting part of the ERP?</Q>
[00:38:26] Ty Wells: <A>Yeah, so depending on what kind of business it is, your chart of accounts would be different for setting up, depending on the type of business that they've described. This is going to be a home cleaning business. This is going to be a whatever business. I'm going to be doing a barbershop. I could be doing a restaurant. So based on what you're trying to do, it's assisting you through the process. So let's say you did the same thing in chat, which you can do, right? And GPT or Claude, you talk back and forth. You're just coming up with the requirements for the business, but nothing's built. You have no back-end, you have nothing. You have an understanding of the business. This is the front-end, but the back-end's already built. It is just modified. It basically covers everything that you need. You just don't know what you need yet. So help me understand what your business you're trying to do, and the business advisor will guide you through. The platform's already there. Forget about the data. That's the easy part. It's that stuff up front.</A>
[00:39:32] Paul Miller: Nice. Can you just work in some front-end so it works with SAP as well? A few customers I can forward you to.
[00:39:37] Ty Wells: Trust me, I'm thinking about that simply because a lot of businesses will resist — the internal fighting. Like, we want to stick with this because it does that. So it's not just going to be price that's the determining factor. So actually, I have about 50 kiosks that we manage for this other business, Mobile Recharge, and these are in like gas stations and stuff, food stores, but remote management of them is crazy, right, because you need some sort of MDM, something. I switched the software that we originally had on there — of course I couldn't take that, so I'm rewriting my own, I've rewritten it already, but I ended up having to put a Rust agent on the device. So I was thinking about the concept of building some sort of agent that sits on the company's network to see the data — not necessarily, they can still continue to use what they use, but sort of to aggregate that data, and then bring it into this business advisory type thing. And I know data warehousing stuff, but for those people that, like, hey, we have this specific piece of software, it doesn't really work — okay, can I get any data out of it? If I can, then I can work with it, and the business advisor can advise you, right, but it has to see data, it only works on data. And what your goal is, to make those two, to make a match there. So, but that's where I'm at, guys. Hopefully, it's next Tuesday, I may be able to present because it's at 10 a.m. in the morning. So you guys will hear all about it after next Tuesday, the 15th.
[00:41:21] Paul Miller: Brilliant. That's an interesting journey. I've done a few lousy appy installs and to do it with AI, gosh, if only I had that back then.

---

<!--SEGMENT
topic: Local RAG document search help
speakers: Tim Hildenbrandt, Paul Miller, Patrick Chouinard, Ryan - One Stop Creative Agency
keywords: RAG, document search, ShipKit, JcodeMunch, Llama, local model, security testing, Claude, Codex, Opus, conflicting answers, CC security review suite, university students
summary: New caller Tim asks for help with a local-only RAG document search tool for university students, built with Claude and JcodeMunch on a ShipKit repo. He gets conflicting security advice from different models. Ryan offers his CC security review suite via direct message; Patrick notes Astra is less restrictive for security auditing.
-->

[00:41:36] Patrick Chouinard: Paul, before you go, we have Tim that asked a question that joined the call. So I don't know if we want to address this question.
[00:41:52] Paul Miller: Tim, what was the question?
[00:42:07] Tim Hildenbrandt: Sorry. I'm making a program for basically document search and kind of like RAG, but faster. The problem is I'm not really a programmer, so I need someone to look at it. But I keep running into this. ChatGPT keeps saying, you know what, you've got 10% of the code is ShipKit. And I don't know if I can show it to someone so they can give me help with it. Because I know I'm not supposed to be sharing the code.
[00:42:41] Paul Miller: Well, look, I don't know if you — I'm assuming that you've got access to the forum. You can do posts, but maybe not share the code through there. <Q>Are you using Claude Code or Codex to help write the code? And it sounds like you're using ShipKit, the ShipKit library to help you develop it. Is that the case? Or how are you writing the code?</Q>
[00:43:18] Tim Hildenbrandt: <A>For the most part, I was using Claude, actually. And I don't know if you guys are familiar with it, but I've been using JcodeMunch [tool:JcodeMunch], which has cut my code down significantly, so it's produced the amount of usage, so I'm getting a lot more use out of it. So I used one of the ShipKit repos, and I think I cut most of it out anyways. But I'm basically making something that I can use. It'll be like a local-only RAG setup that uses a Llama [tool:Llama] and a model, like a small model. And it's open. So basically I'm kind of doing help desk and document search for university students, and I've been able to cut search time down to like a tenth of what it was, and it'll get them references and original posts and like the files that came from, and it's turned out pretty good. But I've been doing all the, like I've basically just given them text in text out on my web interface, and I'm not really going to post it as a program until I've done some security testing on it, but I can't really do that well.</A>
[00:44:37] Paul Miller: So, have you asked your Claude subscription as to how you can host it in a way that can be secure and what approach it suggests you use with the security? Because starting with asking questions might be a good start.
[00:44:59] Tim Hildenbrandt: I've tried that, but the problem is I'm getting conflicting answers. So I tried it with — what am I using now? Not the top tier, Opus. So I tried it with Opus and I was getting different results than when I tried Fable. So it gave me different answers and it tried to fix different things that made a conflict somewhere else, but it never really fixed the original problem it told me I had.
[00:45:30] Paul Miller: Sorry. Ryan, did you want to jump on?
[00:45:33] Ryan - One Stop Creative Agency: Hey, Tim. I've pinged you over my email. If you wanted to ping me an email, then we can have a further chat. Obviously I've got Scott's CC security review suite [tool:CC security review suite] that I could run it through — that is a pretty advanced security and performance package essentially. I'm obviously going to have a further chat about it because I've been doing this for a little while. Before I could make videos or do any other stuff that my business does. So I just put my email address and a message to you on the chat, so feel free to reach out if you wanted something to take a look at it, I would more than happy to help.
[00:46:19] Tim Hildenbrandt: I'm kind of on the road right now, will the chat be saved somewhere I can look at it later?
[00:46:25] Patrick Chouinard: Yeah, actually, we do a summarized recap that includes material in the chat. But actually, Ryan, what I recommend, you probably should message Tim directly on the community board and that way it's going to be easy for him to try.
[00:46:49] Ryan - One Stop Creative Agency: I was going to say, I'm assuming you're in the board somewhere, so I should try and dig you out on the board and send you a message.
[00:46:57] Paul Miller: A direct message. Yeah. That's probably a good start, Tim, because it's the sort of questions I would have as well, is making sure that when you're using Claude for Claude coding, you're giving it the full context of the total library. So when you're asking the model that it has got the full context, are you using a paid Claude subscription to analyze it as well?
[00:47:25] Tim Hildenbrandt: Yeah, so I've got, actually, I have a Claude and Codex subscription. I find that Claude works better, and I'm using Codex kind of as a sanity check. I'll just ask it a question every once in a while to see if Claude's thrown me astray.
[00:47:41] Paul Miller: Okay. Well, that sounds good. ▶ Yeah, that's the right mix that most of us are using.
[00:47:49] Patrick Chouinard: From a security perspective, though, I found that Astra is, let's say, a little bit less picky about what it's validating. You can't ask it to develop hacks or anything, but in terms of security auditing, I find that it stops a lot less often than Fable does.
[00:48:19] Tim Hildenbrandt: Okay. Thanks. I'll give that a shot.
[00:48:23] Ryan - One Stop Creative Agency: I can't message you on school because you're not the right level. You have to be level two to be able to chat, apparently.
[00:48:29] Paul Miller: So maybe if you message Ryan C in the community.
[00:48:37] Ryan - One Stop Creative Agency: I think I'm on there as One Stop Creative Agency. No, I'm on as Ryan Cook.
[00:48:49] Paul Miller: Okay. No, thanks for that. Kris, how's it going?
[00:48:55] Kris Larson: Oh, hi. So...

<!--SEGMENT
topic: Kris's background and job search
speakers: Kris Larson, Daniel Zivkovic, Paul Miller
keywords: vibe coding, AI consulting, developer career, opportunity cost, over-crowded market, software shops, partnering, niche, business network
summary: Kris Larson, a long-time developer newly re-engaged with the community, asks where he can fit in the AI ecosystem and whether he can partner with others who lack software development capability. Daniel Zivkovic offers a pessimistic view that the market is overcrowded, while Paul Miller counters that deep connections to industries with real problems create niche opportunities.
-->

[00:49:00] Kris Larson: Yeah, I joined the community like a few months ago and then I got distracted over the summer with a bunch of just outside stuff and felt really bad today, I'm reading a post on LinkedIn where they're talking about how people aren't sleeping because they're so productive with the vibe coding that it's like, and the quote that grabbed me, he goes, the opportunity cost of sleeping is too high, and it's like, dude, I've been sleeping for like three months.

[00:49:41] Paul Miller: Yeah.

[00:49:43] Kris Larson: So, part of it is, you know, I've been a developer for a really long time, and I'm just now getting into AI and trying to figure out where I can fit in in this whole ecosystem — there's people selling to small businesses, there's Fortune 500, there's a million things to do, so I'm just here to get some ideas, maybe share some ideas. I was thinking, if anybody here said, hey, I want to do a thing with AI but I don't really have software development shops to be able to do it yet, I would say, hey, let's partner up and pair program the thing.

[00:50:46] Daniel Zivkovic: <Q>Kris, is this a hobby, or do you need to make money?</Q>

[00:50:49] Kris Larson: <A>I'd like to make money, let's put it that way. What I'm struggling with,</A>

[00:51:00] Daniel Zivkovic: — Daniel is where is the best opportunity to fit in. It's over-crowded. I'm like 38 years in this, and I'm lost — I keep running to stay at the same place, and at the top it's really crowded. So if you have a hobby, go for it, it's addictive, like testing whiskeys or wines.

[00:51:29] Kris Larson: Daniel, you're not giving me any warm fuzzies here.

[00:51:32] Daniel Zivkovic: There is nothing warm and fuzzy. I don't sleep. I wake up to go to washroom, and my brain is active, what should I do next? And there is no money — you just kind of keep producing products that you cannot sell.

[00:51:44] Paul Miller: A slightly different view, Kris. I've got more people asking me to do stuff than I've got time to do it. ▶ Probably the question is: in terms of your business network community and the sort of areas of contacts you have, if you've got a parallel industry connection rather than the pure "I can code" connection, there are niche opportunities. There are a lot of people getting into programming — vibe coding on steroids — and experienced developers who know what you shouldn't be doing with this code, but it's how you're connected with the people that have the problem and the concern and can leverage those communities.

[00:52:45] Paul Miller: Because I think each of us sit within different communities, but that would be my perspective. I wouldn't be pessimistic about it, but it has to be based on a deep connection to someone who actually wants to spend the money, because if you're going down the purely technical path, that's really not there.

---

<!--SEGMENT
topic: Finding untapped AI niches
speakers: Patrick Chouinard, Ty Wells, Tim Hildenbrandt, Paul Miller
keywords: niche markets, cemetery software, SEO, marketing, financial dashboards, legacy software, outdated internal systems, part names, SKU resolution, restrictive workflows, friction
summary: The group advises Kris on where opportunity lies: Patrick Chouinard points to Morgan's cemetery app as an example of serving a market nobody associates with AI, and Ty Wells describes building an AI resolve layer to translate cryptic inventory part names into customer-friendly descriptions. Tim Hildenbrandt adds that companies still run outdated internal software from the late 90s that's not hard to modernize.
-->

[00:53:10] Patrick Chouinard: I would take my inspiration on that front from Morgan. ▶ Find a niche market that nobody does and go for it. For example, he built an application for cemeteries. If there's a market nobody thinks about doing AI for, that would be it. But he's successful because he's the only one doing it. Today, if you're doing SEO, marketing, financial dashboards — forget about it, there's 3 million people doing it. Find a market nobody touches, and that's where the opportunity and the money is. ▶ Go from your own knowledge outside of IT: what do you know that you never talk about IT with? That's where your opportunities will lie.

[00:54:15] Ty Wells: Also, you have to look at opportunity as something that was restrictive in the past. If you understand the technology of what it can deliver by building — okay, what was restrictive before, and does the model's knowledge unlock that block? Think back to your own experience: remember when you were working somewhere and did this, and why did you do this? Question that — with AI now, you don't have to do that. I gave you guys this example a couple weeks ago: all of our inventory items had cryptic part names and numbers, and nobody would change the names. So I built a resolve layer that translates that into something manageable — when it goes on a quote, it's clear what it is. The customer doesn't have to call back and say, what is part XY7326? No one did it before because it was not cost effective to change all those SKU names — who would do that? But now you can easily do that. I took that bad experience plus customer feedback — emails saying, can somebody call me to explain what this quote is about — and those types of connections release the opportunities.

[00:56:27] Tim Hildenbrandt: Just from businesses I know — companies have a lot of company-specific programs they use internally, and most of them haven't been updated since the late 90s, and changing them isn't that hard, and I don't know what I'm doing. Even factories or small franchises have tons of outdated software that they're paying someone to just translate into modern functionality while they're still trying to use them.

[00:57:18] Daniel Zivkovic: Exactly.

---

<!--SEGMENT
topic: Market saturation and personal branding
speakers: Kris Larson, Daniel Zivkovic, Ryan - One Stop Creative Agency, Paul Miller
keywords: Brandon Godosi, Chris Koerner, personal branding, LinkedIn, inbound leads, fractional CXO, Instagrammification, saturation, referrals, selling
summary: Kris cites an X personality claiming $80K/month five months after pivoting to AI, and worries such advice is oversimplified. Ryan warns against the "Instagrammification" of podcast gurus, noting hidden networks and luck. Daniel discusses his Serverless Toronto experience, dwindling inbound lead quality even at 80–100K followers, and the need for developers to learn selling or find salespeople.
-->

[00:57:18] Kris Larson: There's a guy I'm following on X — Brandon Godosi — Chris Koerner interviewed him. He pivoted to AI and within five months was making 80K a month. It must go to the deep network you're talking about, because quite honestly I don't have that — my industry connections are mostly all IT. This guy just says, "go find somebody that has a problem" — it gets so oversimplified, and I'm trying to navigate through this.

[00:58:40] Daniel Zivkovic: You are really observing a problem that exists. 38 years ago we were like Pathfinders saving companies, then it became bureaucratic, specialized niche. Now it's getting polarized again. ▶ If you're an introvert liking your CICDs and coding, your job's gone. You have to have another passion — understanding of business to map their needs into IT. Whoever had the extra hobby, like mine for real estate or marketing, will survive. But if the only thing you liked is coding, goodbye to that. We need more people like Paul with connections who can start building referrals, maybe recruiting agencies — I don't mind paying commission. If Accenture makes hundreds of dollars, half of that is still hundreds of dollars. It doesn't have to be product-based, it can be service-based. ▶ I'm finding I have to learn to sell, which is hard at this age. We are all becoming salespeople, or we're looking for good salespeople to sell us and pay their commission.

[01:00:04] Ryan - One Stop Creative Agency: ▶ You've got to be careful of the Instagrammification of these people going on podcasts saying they make a million pound a month. There's a lot more to it than that, and sometimes it's complete nonsense. You look on Instagram and see all the good bits — not the divorce, not the drama. Don't get demoralized. Sometimes people get lucky, other times people have vast networks they can tap straight into — you've got to build those networks over time, especially if you're pivoting from something else.

[01:00:53] Kris Larson: That's what I figured with this one guy — he'd been around, doing fractional CXO work. He had businesses big enough where investors are asking, "what are we doing with AI? We need to do something with AI just so we can tell our investors we're doing something with AI." Here's what I can say about myself: I spent a good deal of my career doing contract work — euphemistically called consulting — across a lot of verticals. The biggest takeaway: business is still business — somebody provides value and the other person gives them money. My strength is coming into a situation and understanding how the business works. What I want somebody to tell me is: they have this business and this problem that's costing them $10,000 a month, so they'll pay somebody nicely who can fix it.

[01:06:43] Kris Larson: And you always have to work on your personal brand. There was a guy on LinkedIn who said from personal branding he had more inbound leads than outbound.

[01:07:21] Daniel Zivkovic: That takes lots of effort, it's not easy. I ran the Serverless Toronto community almost nine years — not too many videos, once a month — all I got was easier job interviews, because people say, "he knows what he's doing," so they don't question me. But there is no money — it's a hamster wheel. Even people with 80,000–100,000 followers saw the quality of inbound leads drop this summer. It's getting really, really saturated. So I want to find people who have the need and work with them or for them, like Paul. Paul, you're welcome to pass extra overflow business you cannot service.

---

<!--SEGMENT
topic: Lead generation tactics for consultants
speakers: Paul Miller, Patrick Chouinard, Kris Larson
keywords: Grok, LinkedIn connector, lead funnel, Chamber of Commerce, Rochester New York, ChatGPT brainstorming, idea surfacing, demo projects, YouTube videos, credibility
summary: Paul recommends Kris join local business associations like the chamber of commerce, and shares his tactic of using Grok's LinkedIn connector to surface what small-to-medium businesses wish they could hire for, then building small demo projects and YouTube videos to establish topical credibility. Patrick adds that daily verbal chats with ChatGPT surface unexpected AI-solvable ideas.
-->

[01:02:30] Paul Miller: <Q>Kris, have you ever thought about being part of a business association or your local chamber of commerce — a morning coffee session, a barbecue, whatever they've got going?</Q>

[01:02:58] Kris Larson: <A>Yes, that's an excellent suggestion. The easier access points are smaller towns and communities. I live in Rochester, New York — an upstate community on Lake Ontario. There is a Rochester Chamber of Commerce I could go into, but it's harder to access, costs more money, and I've found there's already somebody in there essentially trying to do what I'm doing.</A>

[01:03:55] Paul Miller: Well, you need to get out there. Patrick, any thoughts?

[01:04:01] Patrick Chouinard: It sounds really simple, but that's where a lot of my ideas come from. People tell me I have a lot of ideas — it's not a miracle. ▶ I chat with ChatGPT every single day, verbally. Not "here's my idea, let's talk about it" — I just chat. The more context I give it, sometimes it surfaces: "that reminds me of this project we worked on; maybe use that project to solve that issue." Out of frustrations and things that don't work well — that I wouldn't even think of solving with AI — it surfaces: hey, that could be solved with AI. That's where you find the idea nobody thought about, because it's not the run-of-the-mill SaaS suggestion.

[01:05:27] Paul Miller: Kris, you've had previous projects from your development days — if you'd had the AI development stack you have now, how would you redo that app better?

[01:05:44] Kris Larson: Even for AI, the businesses themselves have changed substantially, but the core is pretty much the same. Where I consider I have a strength is going in and understanding — if a business person says, I'm struggling with X, Y, Z — coming in, understanding their business, and seeing where to apply the leverage to fix it.

[01:08:16] Paul Miller: Thanks, Kris, and keep posting. It would be good for some established community members to share some of those war stories. ▶ One thing I've found useful for refreshing my lead funnel: I enjoy using the Grok bot — it's got a fabulous connector into LinkedIn that doesn't get blocked by LinkedIn. Assign Grok tasks like: what are the top five things discussed in small-to-medium-sized businesses around "I wish I could talk to someone about doing something," get that to coincide with your skill set and location, then shortlist — build basic projects that solve that, put them on your website with a couple of YouTube videos. You start with credibility that's about you, and it's topical to the people in your LinkedIn network. There's some homework — stick questions up on the forum, we've all been there. I'm in the strange situation now of having good high-paying clients; everyone wants to grab your time, and you want the ones that pay the bills. I've got one very large drinks company — every time they see me, they want to extract free knowledge out of me.

---

<!--SEGMENT
topic: Shakur update — automation and CAPTCHAs
speakers: Shakur, Paul Miller, Daniel Zivkovic, Juan Torres, Patrick Chouinard
keywords: agentic OS, CRM, outreach management, CAPTCHA, Cloudflare, browser flagging, client referrals, commission, workflow optimization
summary: Shakur reports he gave up on having AI make money autonomously and is focusing on improving his outreach workflow, considering a CRM and still unconvinced by the agentic OS. He also worked on a CAPTCHA-solving skill but Cloudflare is now flagging him even manually. The group jokes about Paul sending overflow clients their way for a 30% cut.
-->

[01:10:36] Paul Miller: Shakur, what's the latest for you?

[01:10:48] Shakur: I've pretty much given up on the AI running the make-money-on-the-side-without-me-touching-anything plan — it keeps asking me to do stuff. Started really focusing on how I can improve my workflow further. Decided I finally do need some form of visualization — maybe I should use a CRM to manage all my outreach and contacts, I don't know. I'm still not sold on the agentic OS being useful for me — maybe if I had Patrick's super polished one, I'd be ready to go. So it's all about seeing how I can optimize my outreach. I did some more work on my get-past-CAPTCHA skill that kind of automatically goes, but I haven't been able to solve the Cloudflare one — even when I tried to do it manually, Cloudflare is now flagging me, so I had to go to a different browser. If Paul wants to send some of his high-paying customers my and Kris's way, and Daniel's too, Juan's too — Paul, I'm not greedy, I'll take 30, you can have 70.

[01:13:30] Juan Torres: You guys were too thirsty.

---

<!--SEGMENT
topic: Juan's photo platform go-to-market
speakers: Juan Torres, Patrick Chouinard
keywords: photo automation, venues, country clubs, free service offer, outreach strategy, EC2, auto-scaling group, load balancer, printing capabilities, Instagram, Facebook, social media integration, event coordinators
summary: Juan describes his plan to offer his event photo platform free to mid-tier venues and country clubs to prove value, then run email campaigns and in-person visits to operations managers. He needs to productionalize from a single EC2 instance to an auto-scaling group with load balancer and is deciding whether to add printing. Patrick suggests feeding generated photos directly into venues' social media accounts; Juan sees it as a later trust-based step via email delivery.
-->

[01:13:46] Patrick Chouinard: Juan, you didn't get a chance to go yet. Have you invented or published a new platform for picture automation in venues throughout North America yet?

[01:14:05] Juan Torres: I wish. At least Napoleon Bonaparte had competent marshals under him — I'm doing everything. One non-technical aspect I wanted to go over: I started to really look into offering the service for free for middle-class, petty bourgeois, maybe bourgeois country club places, just so they can see the service in the field, because it seems to sell by itself when people actually see it. So I'm going to carry an outreach strategy — going to events of venue planners, starting an email campaign, and then visiting the places after to talk to operations managers and event coordinators of these venues and country clubs — just try to make an offer they can't deny: having the service for free so they can see it, create content, and share that content with their stakeholders. That way I solve rich people's problems, get some degree of accessibility, get my foot in the door. There's the question of whether I should have printing capabilities, because right now everything is digital, or just go with the digital capabilities I have right now. Strategically: the application isn't productionalized per se — it's an EC2 instance that hasn't been transferred to an auto-scaling group with a load balancer. That's something I have to do. If I add printing capabilities, I have a really sharp edge — a venue coordinator told me last time it would be good to have printing, which I don't think is hard to materialize. So I'll plan my outreach strategy, create a list, and start making the offer they can't deny.

[01:17:41] Patrick Chouinard: Actually, Juan, I had an idea for your project. <Q>Have you thought about talking with the venues to see if you could plug your system directly into their social media feed during events?</Q> The venue probably has an Instagram or Facebook account, and whenever you're at a venue for an event, you could feed pictures your system generates into their social media account directly — either fed directly or moderated by one of their employees — so their social media shows event pictures generated by your system live during the event. More visibility, more money.

[01:19:00] Juan Torres: That is a great idea. It will probably be a step once I gain trust — I don't think they'll give me access to their social media accounts just yet. But it's a great segue, because I already have an email capability — I can add not only the people paying for the venue but also the planner or social media person for that event, so they receive all the transformed images. Aside from creating social media myself, I share my edits so they can use whatever they see most fit for their social media campaign. I'll probably use one of my computers to create a small database with a list of potential people to reach out to.

---

<!--SEGMENT
topic: Ryan update — SEO win and AI video editing
speakers: Ryan - One Stop Creative Agency, Patrick Chouinard
keywords: estate agent website, CRM integration, SEO ranking, ChatGPT computer use, video editing, After Effects, Hermes agency, Astra, Luna, pricing plans, phone capability, Nate B. Jones
summary: Ryan launched an estate agent website with two-way CRM integration that ranked on competitive local keywords within two days. He's considering testing ChatGPT's computer-use model for basic video editing and asks if others have tried it. Patrick shares his Hermes architecture — Luna as cheap dispatcher, Astra low for high-intelligence tasks with trimmed context — recommends the $100 plan for Astra, and shares Nate B. Jones' video on prompting Astra with "recipe cards."
-->

[01:20:30] Ryan - One Stop Creative Agency: I haven't got anything world-breaking. I've got a few things I'm setting up but not allowed to share. The rest has been maintenance. I launched an estate agent's website that links directly into their CRM — a bunch of stuff, both push and pull. It's been ranking on a couple of competitive keywords in my local area on day two, above estate agents that have been established for nearly 100 years in some cases. I keep seeing people doing this computer use with the new ChatGPT model, and I'm sitting here editing a video thinking, I really should install that and see whether it can do this for me — one, save me a load of money on editors, and two, save me a load of time on basic editing like cutting up podcasts. I'm going to give that a go — if anybody has had a go at that, let me know.

[01:22:00] Patrick Chouinard: I'd be very curious whether it's really more economical, depending on the quality of editor you have.

[01:22:11] Ryan - One Stop Creative Agency: Oh, I have an incredibly good editor, but for basic stuff — depending on who's talking, that kind of thing it should be able to do. I'll test whether it can do advanced edits; I've seen people supposedly do stuff in After Effects with it that was quite good.

[01:22:36] Patrick Chouinard: ▶ What I found computer use to be really good at is figuring out how to do something when you don't know how. You're paying a whole lot for something almost deterministic, but when you launch it at an unknown problem — like figuring out which form I need to fill for a tax thing — going through an entire government website and figuring out the exact thing without prior knowledge, that's what it's amazing at. I don't know what to tell it; I just say the result is this, the base problem is that, figure out how to go from problem to solution.

[01:23:48] Ryan - One Stop Creative Agency: I'm always reticent to give Sam Altman money, but he keeps coming out with quite cool products. I'm already giving him a bit to power my Hermes agency.

[01:24:05] Patrick Chouinard: By the way, Astra low effort is absolutely insane to power Hermes, and it's not too expensive — if you put it on high, half a minute and you're done.

[01:24:23] Ryan - One Stop Creative Agency: <Q>Can I keep it on the $20 plan, or do I need to go up to the $100 plan if I move it to Astra?</Q>

[01:24:30] Patrick Chouinard: <A>If you touch Astra, yes, it's going to have to be the $100 plan for sure.</A>

[01:24:34] Ryan - One Stop Creative Agency: I'm currently getting away with the $20 plan. We've added phone capability now — I had to call my dad the other day, and he was like, what the hell's going on?

[01:24:52] Patrick Chouinard: It's quite convincing. ▶ For day-to-day interaction with Hermes, Luna is absolutely marvelous and very cheap — that's my operator, the dispatcher. Whenever I require more intelligence for a task, Luna decides to hand it to a coding profile, a design/architect profile, or whatever additional Hermes profile, and that leverages an Astra-level intelligence for that specific task — but without the entire context of my Hermes agent. The default agent that knows me, with all base memory and huge context, runs on Luna; when I can trim the context to the bare minimum, I give it Astra low.

[01:26:39] Patrick Chouinard: I'm going to post another YouTube video in the chat — this is Nate B. Jones' latest video on Astra. Very, very interesting, and the way he prompts Astra is extremely interesting — his concept of a "recipe card." That's how I got the idea for doing the tax research using Astra. Highly recommended. [link:Nate B. Jones' latest video on Astra]

---

<!--SEGMENT
topic: AI recorders — Fieldy, OMI, Limitless
speakers: Patrick Chouinard, Daniel Zivkovic, Ty Wells, Kris Larson
keywords: Fieldy, OMI, Limitless, Plod, Granola, pendant recorder, ambient recording, diarization, speaker differentiation, context cues, Hermes WebSocket, note-taking
summary: Patrick explains his Fieldy AI pendant recorder, which records 24/7 and tracks trends; a daily Hermes job mines the transcripts for new AI solution ideas. Ty uses OMI and Limitless and augments recordings with emails, screen records, and Chrome session data. Patrick prefers Fieldy because it's ambient rather than trigger-based, and both discuss diarization challenges and adding verbal context cues.
-->

[01:27:38] Patrick Chouinard: Coming back to Kris's question — another way to have ideas: I use a Fieldy AI note taker. It records me all day long; it doesn't just record audio, it tracks trends. Analyzing that is an insanely powerful way to figure out new AI solutions to build, because it's listening to your entire day. ▶ I have a job running every day on Hermes: go look at my Fieldy transcript and extract any idea that would be useful to work on, based on everything you already know about me, my projects, what I like. A lot of what I show you guys every week comes from ideas Hermes came up with based on my Fieldy recordings.

[01:28:52] Daniel Zivkovic: <Q>What is Fieldy — a device?</Q>

[01:28:55] Patrick Chouinard: <A>It's a little device, a recorder, worn as a pendant necklace — it records continuously.</A>

[01:29:12] Ty Wells: I use OMI, O-M-I — that's one. Limitless is about to expire here on the 25th, so I won't give you that one.

[01:29:49] Patrick Chouinard: The funny thing is I don't normally use the AI functionality — I use it more as a pure note-taker, and I let Hermes sift through all the material. You don't know how many times a day I have a discussion and go, oh crap, what did I do exactly? It's like, Hermes, go connect to my Fieldy — there's a WebSocket, so you can have an agent connect. I'll ask Hermes during the day, "I talked about X in my last meeting 10 minutes ago, send me the summary by email."

[01:31:03] Ty Wells: I do that all the time. I don't even care if I remember — I know there's one route to remember: just ask. My proper core ingests other signals too: my emails, my screen records, my Chrome sessions because I built an extension for that. It pushes all that together so it has the right context — otherwise it can't advise me appropriately. What am I ingesting, what's my TikTok feed — every feed I have coming in, I ingest, and then I use that to synthesize the next play.

[01:32:08] Daniel Zivkovic: <Q>Does it know when it's you talking or somebody else? Diarization is always the biggest problem — that's where I waste time transcribing calls, figuring out who said what.</Q>

[01:32:21] Patrick Chouinard: <A>After a while it won't detect every speaker, but it differentiates when I talk, when someone else talks, and when it's media I consume — if I listen to a YouTube video, it knows: this is Patrick listening to YouTube.</A>

[01:32:45] Ty Wells: I also add cues — "oh, this is a great YouTube video," "that's a funny TikTok." I add context clues to help it along, because then I'm sort of tagging: that was a YouTube video, that was a call I was on. Like "hey, I'm driving to work" — that means anything coming there isn't work dictation. It adds great value.

[01:33:27] Daniel Zivkovic: <Q>Which system do you recommend, since you've tried multiple?</Q>

[01:33:29] Patrick Chouinard: <A>Personally, I've tried Plod and Fieldy, and right now Fieldy is the one I prefer because it's ambient recording. I've seen Granola, the pocket ones — but you have to trigger them. What I love about Fieldy is it records 24/7, so I don't have to think about it; I just wear the necklace and everything is recorded.</A> It's not too expensive — I think 150 bucks a year for unlimited reporting or something.

---

<!--SEGMENT
topic: ChatGPT scheduled news radar
speakers: Patrick Chouinard, Daniel Zivkovic, Kris Larson
keywords: ChatGPT scheduled tasks, news radar, personalization, verbal conversation, memory, Quebec election, strategic voting, daily briefing, accent recognition
summary: Patrick describes his morning ChatGPT scheduled task: instead of specifying topics, he asks ChatGPT to pick news based on everything it knows about him, then has a verbal conversation about the results so the thread and memory improve daily. He applies the same pattern to Quebec election strategic-vote analysis. Daniel praises the idea, notes his own weekly personalized video briefing built with Claude Code, and says ChatGPT is the only AI that handles his accent well.
-->

[01:34:00] Patrick Chouinard: Another trick, especially with the ChatGPT interface: I have a scheduled task every morning — a news radar. Everybody's done a news radar: "give me the news about X subject." I decided to go away from that. ▶ Instead of telling it a subject, I said: based on everything you know about me, based on everything we discuss daily, figure out the news that will interest me and that are important to me every morning. I have that inside of a ChatGPT conversation — when the task executes in the morning, it has a wall of text, so I play it out loud and then have a verbal conversation with ChatGPT about the news it came up with: "that's really interesting, and I think that would connect with my project from yesterday" — and we drill in. So the conversation thread is basically not a monologue of news; it's a constant discussion thread about the news every morning. Right now in Quebec it's election season, so I have it track the election — I gave it my goal for what kind of government I want, and I said, don't tell me who to vote for; if you want the government to be constituted that way, what would be the best strategic vote in my circumscription? So every day I have a feed I can talk about, and the next day it uses our discussion to produce a better feed.

[01:36:17] Daniel Zivkovic: <Q>Is that just memory or some kind of skill you can install?</Q>

[01:36:21] Patrick Chouinard: <A>Nothing — it's just scheduled tasks. There's no skill, no building. It's just something I told ChatGPT to do, and now it does it every day.</A> And because I interact with the result every day, it builds its memory — if you just accumulate a feed and never interact, after three days it's going to be crap.

[01:37:02] Daniel Zivkovic: That's amazing. I have that personalization built into my video skill because it builds over time my preferences, and they change over time — so when it gives me briefings, they're related to what I like from all the videos it watches. But it's weekly and I have to go to Claude Code to run the project to see it. What I like with your idea: ChatGPT is the only AI that doesn't have a problem with my weird accent, that can fully understand me — Whisper is behind. That would be amazing to copy.

[01:37:34] Patrick Chouinard: And as soon as I get out of the office, I sit in the car, I go somewhere — I'm chatting with ChatGPT. Every single moment that I have, I'm always talking with ChatGPT.

[01:37:55] Daniel Zivkovic: When my wife is not around to judge me, but I look like a crazy person.

<!--SEGMENT
topic: Context & anti-yes-man prompting
speakers: Ty Wells, Patrick Chouinard, Daniel Zivkovic
keywords: context, garbage in garbage out, prompting, news feed, antithesis, tunnel vision, anti-pattern, yes man, thinking partner, base system prompt, confrontational AI, brutal feedback
summary: The group argues that context quality determines AI output quality ("garbage in, garbage out"). Ty Wells shares his technique of prompting with the antithesis of his interests to escape tunnel vision and avoid a sycophantic "yes man." Patrick Chouinard and Daniel Zivkovic describe base system prompts that force AI to be confrontational and brutal, acting as a thinking partner rather than an agreeable assistant.
-->

[01:38:03] Ty Wells: There's no judging here.
[01:38:05] Daniel Zivkovic: I know, that's why I'm here.
[01:38:07] Daniel Zivkovic: Alcoholics Anonymous.
[01:38:12] Patrick Chouinard: ▶ But yeah, the more context you give it, the best result you're going to get out of it.
[01:38:19] Patrick Chouinard: Yeah, just like when you're building something — it's the same thing, right?
[01:38:22] Ty Wells: If you give it a bad plan, garbage in, garbage out — still rules the world. You have no context, it's going to give you what it gives you, but the more context you add to it...
[01:38:33] Ty Wells: One thing I want to add, Patrick — sorry for interrupting — but the same process, except in my feed: my news feed is the antithesis of what I need to know.
[01:38:48] Ty Wells: ▶ Give me the 10 things I should know, but I don't know, based on what you know about me.
[01:38:55] Ty Wells: So it's a learning — I flip it and get a little bit of learning with it in between.
[01:39:00] Ty Wells: Yeah, because I found that if I didn't do that, then you end up in tunnel vision, because you're just feeding the beast, right?
[01:39:08] Ty Wells: And so I get the opposite.
[01:39:11] Ty Wells: And some of those things actually send off a tangent — sometimes good, sometimes bad.
[01:39:17] Ty Wells: Mostly good, though.
[01:39:20] Ty Wells: But you see what I'm saying? I'm just sort of giving it something to work with that's the anti-pattern, so that it's not just a yes man.
[01:39:31] Patrick Chouinard: Oh yeah, sure — that's the base system prompt that every single AI I talk to, I have: be annoying, be confrontational, never agree with it.
[01:39:43] Daniel Zivkovic: Don't be my yes man.
[01:39:44] Daniel Zivkovic: I need the thinking partner.
[01:39:46] Patrick Chouinard: No, exactly, exactly.
[01:39:47] Daniel Zivkovic: ▶ And I configure them to be brutal with me.

<!--SEGMENT
topic: AI-curated news & publishing
speakers: Daniel Zivkovic, Patrick Chouinard
keywords: ChatGPT, Toronto Star, weekly curation, Kindle, read aloud, weekend paper, briefing skill, DailyBase, morning news routine, Cloudflare, publishing platform, branding
summary: Daniel Zivkovic describes his Friday-evening AI curation of news (Toronto Star) that Kindle reads aloud as his weekend paper, converted from a briefing skill. Patrick Chouinard shares his morning routine of getting the news read and discussed via ChatGPT, suggests blogging the practice for branding, and reveals a work-in-progress publishing platform on Cloudflare to push chat discussions straight to publication.
-->

[01:39:52] Daniel Zivkovic: Patrick, what you do daily, I do weekly, but I like the Toronto Star [tool:Toronto Star] and paper.
[01:39:55] Daniel Zivkovic: So on Friday evening, I would create this curation — I get lists of the e—

[Editorial note: a duplicated block at 01:40:00–01:40:55, repeating the preceding exchange with shifted speaker labels, was removed as a transcription artifact.]

[01:41:00] Patrick Chouinard: And I can read them, and I can have Kindle [tool:Kindle] read them to me.
[01:41:03] Daniel Zivkovic: So that briefing from that skill converts into something that's my weekend paper.
[01:41:09] Patrick Chouinard: So I would like to go to DailyBase [tool:DailyBase], not have to wait for Saturday and Sunday to enjoy the news from the videos I didn't watch.
[01:41:18] Patrick Chouinard: I mean, in the morning now, when I wake up, first thing I go — I open ChatGPT [tool:ChatGPT], look at the news and have it read out to me, and I have a chat with it.
[01:41:27] Patrick Chouinard: That's my morning newspaper: having ChatGPT telling me about what's new and interesting.
[01:41:34] Patrick Chouinard: ▶ Blog about that. That's good for your branding.
[01:41:35] Patrick Chouinard: It's unique.
[01:41:36] Patrick Chouinard: I've never heard any influencer say that.
[01:41:40] Patrick Chouinard: Yeah, actually, I have a chat with ChatGPT about building my own publishing platform using Cloudflare [tool:Cloudflare],
[01:41:50] Patrick Chouinard: to be able to push directly from discussion to...
[01:41:53] Patrick Chouinard: Yes, yes.
[01:41:56] Patrick Chouinard: Awesome. It's in the works.

<!--SEGMENT
topic: Personalization & feeding the beast
speakers: Patrick Chouinard, Ty Wells
keywords: downtime is idea time, silly discussion, level of insight, personalization, local models, local inference, privacy, Apple Studio M5 Ultra, 512 GB RAM, hardware recommendations, pricing, feed the beast, genius in your pocket
summary: Patrick Chouinard notes that any downtime becomes idea time and that even silly discussions with the model yield surprising insight. Ty Wells gives a concrete personalization example: because the model knows he works on local models, local inference, and privacy, it flagged the upcoming Apple Studio M5 Ultra (512 GB RAM) while acknowledging its "kidney-zone" pricing. Both agree you must continuously "feed the beast" to get a genius in your pocket.
-->

[01:42:00] Patrick Chouinard: Any downtime is idea time to me.
[01:42:06] Patrick Chouinard: And it's going to know a whole bunch of things.
[01:42:09] Patrick Chouinard: And you'd be impressed what it comes up with — when you have not only very serious, detailed discussion, but when you start to have even silly discussion with it, the level of insight it can have is impressive.
[01:42:25] Ty Wells: I mean, I remember at some point it was recommending me — because it knows that I do a lot of work on local models and local inference and privacy work —
[01:42:36] Ty Wells: "Oh, there's a new Apple Studio M5 Ultra [tool:Apple Studio M5 Ultra] with 512 gig of RAM that's coming up this fall."
[01:42:49] Ty Wells: It's like, yeah, okay, cool — thanks. But I'm not looking at selling a kidney or something.
[01:42:57] Ty Wells: And now—
[01:43:00] Ty Wells: Often it will come up like, "Oh, there's this new piece of tech that got out that you might want to think about — but I know it's in the kidney-type zone of pricing, so maybe not right now."
[01:43:14] Patrick Chouinard: And it keeps those things — and that's the thing: ▶ you have to feed the beast in order for the beast to be good.
[01:43:24] Patrick Chouinard: And it's good.
[01:43:25] Patrick Chouinard: It's like having your own genius in your pocket, right?

<!--SEGMENT
topic: HGI, Agent Deck & cognitive load
speakers: Patrick Chouinard, Daniel Zivkovic, Kris Larson
keywords: HGI, AGI, bridge, Agent Deck, Astra, harness, human tokens, human-in-the-loop, cognitive subsystem, Opus, Sonnet, cognitive load
summary: Patrick Chouinard argues humans — not AI — are the limiting factor ("HGI, not AGI") and that people are the bridge connecting global information. He explains Agent Deck, coded by Astra, as the reverse harness: a way for AI to talk to humans by exposing "human tokens," treating the human-in-the-loop as an expensive, low-parallelism cognitive subsystem used only when judgment is needed, while humans must become an inference layer the AI understands. Kris Larson sums up the result as a UI optimizing human cognitive tokens ("less is more"), and the group agrees reading — not writing — is now the bottleneck, so we must ask AI to reduce cognitive load.
-->

[01:43:28] Patrick Chouinard: If you could connect the dots — oh my god, it's crazy.
[01:43:32] Patrick Chouinard: You know, getting those dots connected.
[01:43:34] Patrick Chouinard: And the capability is there.
[01:43:36] Patrick Chouinard: It's just a matter — you're the bridge.
[01:43:39] Patrick Chouinard: We are the bridge to get it all connected.
[01:43:43] Patrick Chouinard: Because think about it: information from all around the world — all of a sudden, you can put it together.
[01:43:50] Patrick Chouinard: And so now you can put it together.
[01:43:52] Patrick Chouinard: If you're able to put it together, that is the key.
[01:43:55] Patrick Chouinard: But there's no way it's going to come together on its own.
[01:44:00] Patrick Chouinard: But if you were able to put it together — there you go.
[01:44:03] Patrick Chouinard: ▶ So our own intelligence is our limitation. We are our limitation.
[01:44:06] Patrick Chouinard: It's not the AI anymore.
[01:44:10] Patrick Chouinard: Right.
[01:44:11] Patrick Chouinard: It's how far we could go.
[01:44:12] Patrick Chouinard: Yeah, absolutely.
[01:44:13] Patrick Chouinard: HGI, not AGI. H-G-I. Human.
[01:44:16] Patrick Chouinard: Human to call intelligence.
[01:44:17] Patrick Chouinard: Yeah.
[01:44:20] Patrick Chouinard: Actually, you know the Agent Deck [tool:Agent Deck] that I showed earlier?
[01:44:23] Patrick Chouinard: The way I presented that to Astra [tool:Astra] to code it, it's like — I told it, all the other harnesses are a way for humans to leverage or give tasks to AI systems.
[01:44:42] Patrick Chouinard: It's the bridge from human to AI.
[01:44:44] Patrick Chouinard: I want Agent Deck to be basically the way for AI to talk to us.
[01:44:52] Patrick Chouinard: I want it to be the harness for humans, for agents — basically the other way around.
[01:45:00] Patrick Chouinard: <Q>How do you expose the human tokens to the AI system?</Q>
[01:45:06] Patrick Chouinard: Because if you talk in its own speech, in its own way of thinking, I find it works a lot better.
[01:45:15] Daniel Zivkovic: So basically I tell it, like, you have astral-level intelligence, you have fable-level intelligence, you have Opus [tool:Opus], you have Sonnet [tool:Sonnet], you have all of those.
[01:45:23] Patrick Chouinard: <A>Well, the human in the loop is another cognitive subsystem that has very, very, very expensive tokens, that has not a lot of parallel capability — it's really, really single-driven — so you use it only when it's absolutely necessary and you need its input and its judgment.</A>
[01:45:45] Daniel Zivkovic: Otherwise, take care of it.
[01:45:49] Daniel Zivkovic: We have to become an inference layer that it can understand.
[01:45:57] Daniel Zivkovic: Mm-hmm.
[01:46:00] Patrick Chouinard: And that's how it built Agent Deck.
[01:46:03] Kris Larson: Basically, it built a UI that was targeted at making the most efficient usage of my own cognitive tokens for the job the AI was trying to achieve.
[01:46:17] Kris Larson: Less is more.
[01:46:19] Patrick Chouinard: So before, writing was difficult; now, reading is difficult.
[01:46:23] Patrick Chouinard: ▶ So we have to ask to reduce cognitive load on us.
[01:46:27] Patrick Chouinard: Yep, exactly.
[01:46:31] Kris Larson: Perfect.
[01:46:32] Patrick Chouinard: Thank you from the Lake of Ontario.
[01:46:38] Patrick Chouinard: Sorry, Kris.
[01:46:43] Patrick Chouinard: No worries.
[01:46:44] Patrick Chouinard: I'm sure they're good.
[01:46:45] Patrick Chouinard: We understand each other.
[01:46:46] Patrick Chouinard: We'll translate.

=== UNRESOLVED SPEAKERS ===
- Hemal Shah
- Daniel Zivkovic
- Juan Torres
- Tim Hildenbrandt
- Kris Larson
- Daniel Zivkovic — raw form "Daniel Zivkovic" not found in SPEAKER_ALIASES; passed through unchanged
- Kris Larson — raw form "Kris Larson" not found in SPEAKER_ALIASES; passed through unchanged