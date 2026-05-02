=== SESSION ===
date: Unknown (Tuesday weekly call)
duration_estimate: ~115 minutes (00:07:16 – 02:03:56)
main_themes: OpenClaw agent setup and security, Claude Code mobile interface, AI news pipeline with Brave/Perplexity, ShipKit licensing and Git history management, new AI models (Claude Sonnet 4.6, Opus), hallucination detection tool (Lucid), congressional trading tracker app, meal planning app, client acquisition strategies, community reflection

---

<!--SEGMENT
topic: Pre-call Smalltalk and Introductions
speakers: Patrick Chouinard, Marc Juretus, Ty Wells, Paul Miller, Morgan Cook, Jake Maymar, Ana P
keywords: OpenClaw, Google Cloud VM, security, prompt injection, Telegram, Brandon, EMS project, hosting handoff, Paul Miller hosting
summary: Participants exchange casual greetings and weather chat before transitioning to housekeeping. Marc mentions spinning up OpenClaw on a Google Cloud VM; Patrick warns about prompt injection risks with email-connected agents. Paul Miller takes over hosting duties while Brandon is away on a dev project, and the group confirms Brandon will return next week.
-->

00:07:16 - Patrick Chouinard
Hey, Marc.

00:07:20 - Marc Juretus
What are you seeing here, Patrick?

00:07:24 - Patrick Chouinard
How's it going?

00:07:26 - Patrick Chouinard
You good?

00:07:26 - Marc Juretus
And yourself? How was your day?

00:07:32 - Patrick Chouinard
The winter is starting to wane a little bit, and we're getting just above freezing.

00:07:41 - Marc Juretus
I was watching a video recently of — I forgot what the area is in Siberia. It's Yuga something or whatever, but it can go for stretches of minus 80. I'm like, man, I don't care what I got to do. I got to find a way to move out of there, man.

00:08:05 - Marc Juretus
I'll find some way to save some money and get out of there, man.

00:08:12 - Patrick Chouinard
The worst I've ever experienced was minus 53 with windchill.

00:08:18 - Marc Juretus
The funniest thing was how casual she was. She only had like one fridge. She had frozen a bag with frozen milk hanging out her window to stay frozen. And when she was making coffee, Patrick, she would chop some off and just drop it in.

00:09:00 - Patrick Chouinard
I actually ran into a situation that might be interesting. Nothing is built. I thought about it on my way back from work, but we'll see.

00:09:13 - Marc Juretus
I did spin up an OpenClaw [tool:OpenClaw], just to be like the rest of you guys. I got it doing some stuff already. I spun up a virtual machine up on Google [tool:Google Cloud VM], though. I think it's in boot 224.

00:09:27 - Patrick Chouinard
▶ Yeah, but be very careful about security. Make sure it's ironclad that nobody else than you can access that box.

00:09:36 - Marc Juretus
Yeah, well, it's allegedly locked down to that key to my Telegram [tool:Telegram]. So I've checked just about everything, and the only thing I got on there is like, I created an MJuretus agent. It's not my regular Gmail, just limited stuff on there.

00:10:00 - Marc Juretus
Well, look at the website I've published.

00:10:05 - Patrick Chouinard
I've listed everything I did to secure mine. Let me grab the address again.

00:10:18 - Patrick Chouinard
It's one thing I like about having it up in the Google Cloud. I could just turn the server off at any time.

00:10:27 - Patrick Chouinard
<Q>Yeah, it's not just about servers. It's about what the agent is capable of doing.</Q>

00:10:36 - Marc Juretus
<Q>Oh, so you're more concerned about being hacked, or it running rogue on you?</Q>

00:10:40 - Patrick Chouinard
<A>Prompt injection. You have it connected to an email. So if you don't put some rules in place to say only read and reply to email from me or from myself or something like that, somebody could decide to send an email with a prompt within the email and the agent will read it and do it. Just an example, but there's tons of things to take care of to make sure that it is very powerful, but it is very dangerous if not properly configured.</A>

00:11:25 - Patrick Chouinard
We'll see what happened now that it's been basically acquired by OpenAI [tool:OpenAI].

00:11:27 - Marc Juretus
No, they didn't buy the product, but they actually hired the creator of OpenClaw.

00:11:38 - Marc Juretus
It's supposed to stay open source.

00:11:41 - Patrick Chouinard
We'll see. But yeah, it's basically now an OpenAI product.

00:11:45 - Marc Juretus
I got it doing two things now. Because I train people once in a while, gym stuff. If I type the word "email trainer," their name, and then "email," it basically injects a pre-template email. Hey, Patrick, and then at the bottom, it sends an email to him and shows my availability from Cal.com [tool:Cal.com].

00:12:10 - Marc Juretus
And then the other one is I connected a jobs API [tool:jobs API]. So if I do "get jobs," then the next parameter is like "laborer," then the last parameter is "email." It'll send an email from the API, which supposedly pulls from Indeed [tool:Indeed] and sends you a list of jobs matching my criteria. So that's all I've done so far.

00:12:30 - Patrick Chouinard
▶ I hear you about the email injection. I've got to check that out. Yeah, not that it's a huge risk, but it is one. So I might as well protect you from it right away.

00:12:44 - Marc Juretus
I saw that the bare minimum for OpenClaw is 2 GB of RAM or something like that. And the virtual machine I spun up is 1 GB. The 2 GB is $12, the 1 GB is $7.

00:13:07 - Patrick Chouinard
▶ Honestly, for this level of use, you could run it off of a Raspberry Pi [tool:Raspberry Pi].

00:13:22 - Patrick Chouinard
And Morgan, I saw your question also in the school, so we'll see if we can give you the answer you're seeking.

00:13:59 - Morgan Cook
The client wants to bring on some other resources. So now I've got to figure out how to pull myself out of the ShipKit [tool:ShipKit] pattern.

00:14:18 - Patrick Chouinard
Hey, Paul.

00:14:30 - Paul Miller
How's it going? Good, good.

00:14:33 - Patrick Chouinard
So you can take a passenger seat today, Patrick.

00:15:08 - Patrick Chouinard
Where is Brandon?

00:15:14 - Marc Juretus
I forgot — he said he's just not attending because he's got other stuff going on?

00:15:23 - Patrick Chouinard
To my knowledge, he's just working on his own project right now for the EMS stuff. Yeah, it's sucking a lot of his time.

00:15:31 - Paul Miller
Patrick and I said, look, we're keen to keep the call going while he's distracted on the short term on his dev project. Because I think we all get benefit from the call and we don't want to lose the community.

00:15:55 - Patrick Chouinard
▶ Yeah, and he should be back next week, actually, for his once-a-month go.

---

<!--SEGMENT
topic: Productivity, Debugging Habits, and Coding Fatigue
speakers: Marc Juretus, Paul Miller, Patrick Chouinard, Jake Maymar, Ana P, Morgan Cook
keywords: debugging, diminishing returns, version control, Git, code loss, rewriting code, sleep deprivation, productivity, mental state, control-Z
summary: The group shares personal anecdotes about working extremely long hours on technical problems, the dangers of coding while fatigued, and the counterintuitive benefits of losing work and starting fresh. Key takeaways include recognizing diminishing returns, using version control discipline, and the cognitive value of rewriting code from scratch.
-->

00:17:00 - Patrick Chouinard
Let's just say that I was a lot younger at the time. I wouldn't be able to do that today.

00:17:11 - Marc Juretus
My all-time record so far is 60 hours.

00:17:18 - Paul Miller
Yeah, I got up to about 36 without sleeping, and that was in my younger years as well.

00:17:28 - Patrick Chouinard
I do not recommend it. Your brain just stops.

00:17:34 - Marc Juretus
I kind of meant working on, like, I'm playing around with something in AI, and it's like, damn, it's been 11 hours.

00:17:46 - Patrick Chouinard
I'm talking about creating a single document for a client.

00:17:58 - Patrick Chouinard
The AI thing, you can kind of lose track of time. You can really end up in the matrix and there's all like numbers around you.

00:18:07 - Marc Juretus
My problem is, when something is not working, I can't just walk away — it's got to be in a state that drives me absolutely nuts. It's like there's an orphan process in your mind, not letting you sleep.

00:18:20 - Jake Maymar
But I also learned that if it's broken and it gets more broken, then I need to walk away. Because I'm tired.

00:18:32 - Paul Miller
Yeah, the whole diminishing returns thing.

00:18:39 - Jake Maymar
And sometimes — this isn't totally related to AI at all — but sometimes it just needs a reboot of my computer. Like I've run into bugs and I cannot figure out where the bug came from, and it was just the machine's been on too long, basically, and it just needs a restart.

00:19:00 - Jake Maymar
▶ The other thing is that supposedly the brain continues working on the problem even after you've stepped away. It's actually better to go for a walk or just do something else that's not related, and it kind of solves itself more often than not.

00:19:22 - Ana P
I started forcing myself to stop because more than once — I've never done 30-plus hours like Paul. My record was almost two all-nighters. And I remember one of my friends was like, "You look like you're staring at a void. Something is definitely wrong."

00:20:00 - Jake Maymar
Yeah, when you start seeing tunnel vision, that's when you stop.

00:20:03 - Marc Juretus
▶ My rule usually with stuff for work is three Control-Z's, because you broke the code and need to go back. If I get three Control-Z's, it's time to cut it, brother. Before, like you said, Jake, you do some real bad things.

00:20:18 - Jake Maymar
No, like bad, bad, horrible things. I've actually done something so bad that I had to essentially go back a branch, just lose an entire branch of work.

00:20:36 - Morgan Cook
I learned from a bad experience of not having battery backup power and losing hours of code and then having to rewrite it.

00:20:48 - Paul Miller
▶ Oftentimes, the second stab at it is much better.

00:20:53 - Jake Maymar
Don't take them as negatives.

00:20:55 - Morgan Cook
I mean, you have this plan, right, and you execute it, but you keep running into these problems. If somebody comes and wipes that out for you and you have to start over, now you already have in your mind a good mindset about what things work and what things don't. So it's quicker to get to an end product that is actually what you intend to write.

00:21:16 - Jake Maymar
It's a really, really good point. You are cursing the whole time, but you're right — when you rewrite it the second time, you're mad, but you already coded this crap.

00:21:26 - Morgan Cook
Yeah, but this time I can do this part right because I know how to do it.

---

<!--SEGMENT
topic: Call Kickoff and Weekly Updates Overview
speakers: Paul Miller, Patrick Chouinard, Jake Maymar
keywords: Claude Sonnet 4.6, Opus, OpenAI, OpenClaw creator hired, new models, weekly updates format, business contracts, AI engineering, healthcare, cybersecurity, educational platform
summary: Paul Miller formally opens the call, thanks Patrick for hosting the prior two weeks, and sets the agenda: each participant shares what they built or shipped and what blocked them. Paul teases a business update on signing new contracts. Jake gives his update, noting multiple active projects (healthcare, cybersecurity, two educational platforms) and reacts to Anthropic's Claude Sonnet 4.6 release and the OpenClaw creator joining OpenAI.
-->

00:21:39 - Paul Miller
So, hello everyone. I'll be hosting the call this week. Brandon is back next week. I'd like to thank Patrick for the last two weeks. Very hard trying to run this and being actively involved as well. Patrick, you did a fabulous job. I found the last two sessions were really, really engaging.

00:22:19 - Paul Miller
I'll give a little update with what I'm up to. And just as a teaser, I'm going to talk about the business side of things and how I've gone with signing up new contracts and the latest lessons on that, because I seem to have more contracts than I've got time to do.

00:22:57 - Paul Miller
I'd love to sort of give away any insights, because a few of us have got that funnel thing going. Now we know how to code really quickly and effectively. We know how to do the business thing really effectively. It's like, well, what else is there?

00:23:14 - Paul Miller
What I'd like to do — when you cover off your update, it'd be good if everyone talks about what thing did you build or ship this week, and what thing was a blocker?

00:23:38 - Paul Miller
And of course, we have new models that have come out this week. Even just today, Claude [tool:Claude] has come out with Sonnet 4.6 [tool:Claude Sonnet 4.6], following Opus the other week, and OpenAI's got some new ones. It'd be good to hear if anyone's played with some of the new models, because some open-source models have come out as well, which look pretty good.

00:24:12 - Paul Miller
But Jake, do you want to start?

00:24:17 - Jake Maymar
I wish I had shipped. I basically seem to be landing more and more work without shipping things. I think that's good. But I can't wait to share all the stuff I'm working on. The healthcare project is going quite well. I'm very excited about that. The cybersecurity thing is going well. The educational platform is going well. The other educational platform is going well. And now this sort of "Claude in a box" thing is also really interesting.

00:24:57 - Jake Maymar
And on a side note, I'm very curious. Anthropic [tool:Anthropic] released Sonnet 4.6 with a 1-million-token context window, which is pretty cool. I think it's also Opus with 1 million, but I bet you have to really pay for it.

00:25:18 - Jake Maymar
But I'm very curious about the whole — the creator of OpenClaw joining OpenAI. I thought that was very interesting, and I was really surprised because I'm an Anthropic fan, right? And unfortunately, I feel like they really missed it by basically doing a cease and desist instead of saying, "Hey, why don't you join us?"

00:25:47 - Paul Miller
Yeah. There's been some interesting debate on that. It was pointed out that the guy whose product it was — he was not doing this for money, but I'm sure a lot of money was tangled, and this is a project that he's driven himself. 80 days in, he's been able to sell. It just sounds fascinating. It's so 2026.

00:27:00 - Jake Maymar
AI definitely brings up a lot of existential conversations. I mean, we all know where this is going. And 2026 is pretty wild. I think it's a pretty cool time to do moonshots, right? I've already talked to a couple of my friends and they're like, "Yeah, I did OpenClaw, I did all these different things, I've shipped all these things, I'm bored." And I'm like, wow, like that's crazy that we got to a point where they felt like they've done everything. Moonshots — we can actually start really trying to fix things, like fix the plastic in the water, fix air contamination. When there were the LA fires, there were all those different students — data science, machine learning, some AI guys — making all those apps for tracking the fires and the air quality. Well, now the whole world has these tools. We can make some amazing stuff.

00:28:19 - Jake Maymar
I know Patrick's doing OpenClaw. Paul, you're doing OpenClaw, right?

00:28:29 - Paul Miller
Yeah. Look, I was having a play with it. I got a bit concerned about the security side of things. I want to do the ultimate assistant — the home assistant that hovers over CRM, that hovers over coaching, that looks at your email, that looks at your text, that looks at your life objectives, and it's managing stuff. I'm still in multiple minds as to how you do that, but you give people comfort around the security. You make sure that the human is in the middle, but the AI is doing the boring crap.

---

<!--SEGMENT
topic: AI Model Hype, Transformers, and Technology Adoption
speakers: Jake Maymar, Scott Rippey, Paul Miller
keywords: transformer architecture, AGI, predictive analysis, LLM, OpenAI, Google, compute scaling, Sam Altman, large world models, LeCun, spatial data, sensor arrays, enterprise AI adoption, Mark Cuban
summary: Scott pushes back on AI hype, arguing current LLMs are fundamentally predictive transformer-based systems, not AGI. Jake acknowledges the limitation but highlights rapid improvement and emerging non-token architectures. Paul references Mark Cuban's observation that AI adoption is bottlenecked by business-side leadership rather than technology readiness, with smaller agile businesses leading the way.
-->

00:30:33 - Scott Rippey
It's all hype. Right now. Because when you understand what a transformer [tool:transformer architecture] is and how that's how OpenAI built it off Google's transformer, it's like — this is predictive. It's not AGI, it's nowhere close. It's just predictive analysis. That's all this is. And they're all trained differently, so we get different responses. And everybody keeps hyping models, and nothing's really changing. Altman started the whole thing with "throw compute at it," which I'm glad people are finally starting to try to make the models better without compute. So we're seeing some of that now. But still, it's just predictive. That's all it is.

00:31:30 - Jake Maymar
I know it's predictive, but it's so much better than it was. And I think the tool use and it being better than it was, even though it's predictive — and some parts of it are becoming deterministic — what is wild is they still don't understand how it works, though.

00:31:50 - Scott Rippey
Like, I may say this and be like, yes, I understand this. But I'm also like, they don't know. I don't know. None of us know how this actually works.

00:32:01 - Jake Maymar
Well, especially when it switches from tokens to other things, right? Like Bastian was sharing some different white papers and demos. And I know LeCun [tool:LeCun/Meta] is working on large world models, I think. There's so many things. But I do think it's very interesting once it gets into spatial information and sensor data — sensor arrays and training off that rather than just tokens. But I don't quite understand how it's going to do that if everything's already built on this.

00:32:41 - Paul Miller
I think there was a great question because I keep getting challenged by people on this thing. It's like "AI is not there" and "AI is this and AI is that." Mark Cuban raised a good thing about six months ago — we're waiting for the business-side people to engage with it and drive it. And the smaller the business, the more capable they seem to be. It's some of those bigger ones — like hospitals. The government had come to me and said, "Well, why aren't they using AI better?" And it's like, well, it's the nature of change. They weren't using personal computers well back in the 90s. This is how technology change occurs with these industry types.

00:34:40 - Paul Miller
▶ It's the small, agile businesses. It's the stuff that Patrick's dealing with, with his challenges in that big organization. This is the change — but it's that mindset of convincing people in these organizations and leading those teams and coming up with those ideas.

---

<!--SEGMENT
topic: ShipKit Licensing, Git History, and NPM Package Strategy
speakers: Morgan Cook, Scott Rippey, Patrick Chouinard, Jake Maymar, Paul Miller, Bastian Venegas Arevalo
keywords: ShipKit, Git history, GitHub, .gitignore, NPM package, Claude Code, Claude.md, skills, slash commands, MCP, agents, licensing, repo management, GSD project
summary: Morgan raises a practical problem: a client project built with ShipKit (Brandon's licensed toolkit) now needs to be shared with third-party contractors, requiring removal of licensed code from Git history. The group discusses solutions including dual-repo setups with clean history, .gitignore strategies, and Patrick's novel idea of packaging Claude artifacts as NPM packages for easy installation and removal — a pattern that also solves the licensing isolation problem.
-->

00:35:21 - Paul Miller
We had Morgan with a question. Patrick, I'll ask you to jump in just in terms of ShipKit [tool:ShipKit]. Morgan, did you want to just talk through what you were asking about?

00:35:39 - Morgan Cook
Yeah, so what I have is a client and I've been working on a website for them using the tools in ShipKit. I didn't use ShipKit's pre-built models. I just started with a new project using ShipKit. And so along the way, I had checked all that into source because I wasn't planning on ever sharing necessarily the source with anybody else, but now the client wants to bring on some other people to do search engine optimization and a bunch of other stuff for them, and so now I got to share the project, but I need to pull ShipKit out of it. And I can't just pull it out and submit it because the history is all there, right? So the GitHub [tool:GitHub] history — they could just go back and pull the GitHub history, so I'd have to make the modifications and push back into history to clear all those commits, and there's probably about 70 or so commits.

00:36:54 - Scott Rippey
<A>You can have Claude Code [tool:Claude Code] do that, by the way. I have a private and a public repo for an app that I wanted to share, and it actually wrote me a script that only when it publishes to the public, there's no version history. It's like just what you pushed. So really easy to do if you want to. You're basically in that scenario setting up two separate repos in GitHub.</A>

00:37:23 - Scott Rippey
Two separate repos, same code base locally.

00:37:31 - Bastian Venegas Arevalo
And the new one just has a clean Git history. It doesn't include any of what was set. Or you can do it in just like two or three commits that you cherry-pick. But basically it's a new Git history.

00:37:45 - Scott Rippey
▶ So basically the script that I have that Claude Code wrote me will, every time I push to the public, I want it to be one version, no history ever.

00:39:00 - Morgan Cook
It's not just the AI docs folder. It's now because all of the Claude Code skills include ShipKit stuff as well.

00:39:08 - Paul Miller
Okay. Yeah, yeah.

00:39:09 - Morgan Cook
So I got to pull, to honor Brandon's license agreement, I got to pull all that out before I make it public.

00:39:17 - Scott Rippey
I do want to send a link to you guys in the chat again for this, because this is like something based off India Dev Dan, with somebody that we talked about before, where skills became hot and everybody's like, everything has to be a skill. No — there are slash commands, prompts, skills, agents, MCP [tool:MCP]. Like it all kind of has a purpose, but there is some overlap. And it's like understanding when to use what. I kind of made a whole document on that. Not everything should be a skill — that's something repeatable that you're going to do all the time.

00:40:00 - Patrick Chouinard
Not lately, because they removed slash commands, and they merged them into skills now.

00:40:04 - Scott Rippey
I know, yeah. So slash commands are kind of skills now, because I've noticed that, where it's like, "oh, loading a skill." I'm like, but that's my slash command. What's happening right now?

00:40:17 - Jake Maymar
I was just going to say, Morgan, if you put it into `.claude`, and then I just basically remove it. So all my skills, all my slash commands, everything is in `.claude`. The only thing that's not is the `claude.md`, but everything else — all the task documents, just everything. And so that way, when I need to delete it, I just point at that one folder, and now I don't have to worry.

00:40:47 - Morgan Cook
Well, so this project initiated before I was on `.claude`, so I was in a different framework, and I was using the AI docs folder with the `@` reference to Brandon's files for the ShipKit tools. And so at some point, I had converted to Claude Code. So there's some history to this project.

00:41:15 - Jake Maymar
Yeah, that sounds complex. But it seems like Claude Code could do it and do basically a visualization of what it does.

00:41:24 - Patrick Chouinard
It's going to cost a couple of tokens, but it will definitely do the job.

00:41:31 - Morgan Cook
The main thing I was trying to get from the group is just some ideas about how should we be setting up these projects where we have licensed skills or licensed source that we don't want to have in our public shared version of the project. What's the best way in doing that in GitHub or any other repository?

00:42:01 - Scott Rippey
▶ Just either get ignored. I mean, that's really what it is. Where's your documentation live? What's in `.gitignore`? That's all it is. Organization. That's it.

00:42:49 - Paul Miller
It's the problem that these projects evolve out of something that, over time, it's great in hindsight, but it's coming back and fixing it.

00:43:08 - Morgan Cook
The analogy I explained to the client was, look, it's like I've got a car and I've got like five different toolboxes inside the trunk, and you want to loan the car out, I need to get those tools out of the trunk, right?

00:43:23 - Scott Rippey
And it's like, they're bolted in right now.

00:55:15 - Patrick Chouinard
Morgan's question got me thinking, because I was talking about that with ChatGPT [tool:ChatGPT] on my way back from work about something very specific, because I'm building a whole lot of skills and agents and plugins and hooks for Claude Code right now, even for my day job. And I was trying to figure out a way how to publish them in a sense. I was looking at how do I push that into others' repos in the business. And basically, we came up with something that's quite interesting — never thought about using it for that, but creating an NPM package [tool:NPM] of Claude artifacts and deploying them that way. Because then you can have them configured, you can have it insert stuff like a primer into a `claude.md`, decide which skill you wanted to deploy instead of dealing with some module and cloning half of a repo. Build an NPM package and just install it as a dependency.

00:56:31 - Patrick Chouinard
▶ So that would also isolate and resolve Morgan's problem because then if you deploy all of that as an NPM package, it gets really easy to be removed.

00:56:47 - Morgan Cook
So one package that's doing that very thing in injecting into Claude is that GSD project [tool:GSD project]. He has an NPM installer that installs and installs into the `claude.md` step-through commands and everything else.

00:57:14 - Morgan Cook
Right. Doing it that way would make a lot of sense.

00:57:19 - Patrick Chouinard
You could even say, I have my brand kit, for example, for any web project I work on. Well, let's make an NPM package and deploy it like that. So your AI has all the artifacts it needs to respect the brand, and so on and so forth. The idea is anything you want to insert into your project — I know that usually it's not documentation per se, but now the documentation is executable, so why not?

00:59:00 - Patrick Chouinard
▶ So you have a tool that installs itself, teaches itself, integrates itself into your project.

00:59:16 - Patrick Chouinard
▶ Use AI to help you use AI.

---

<!--SEGMENT
topic: Patrick's AI News Pipeline — Admin Dashboard Demo
speakers: Patrick Chouinard, Jake Maymar, Juan Torres, Paul Miller, Scott Rippey
keywords: news pipeline, Brave Search, Perplexity Sonar Pro, OpenRouter, enrichment, admin dashboard, pipeline automation, deterministic workflow, RAG, feedback loop, article quality grading, budget management, OpenClaw scaffolding
summary: Patrick demos his sixth-iteration AI news pipeline, now featuring a full admin dashboard for managing article ingestion, enrichment via Perplexity Sonar Pro, budget tracking, and quality feedback. He explains the architecture: Brave Search finds URLs, Perplexity writes enriched articles with citations, and a feedback/grading loop improves source selection over time. The pipeline was scaffolded by OpenClaw from a Telegram message and then refined with Claude Code. Patrick also shares his workflow philosophy: prototype with Claude Code, productionize with the Anthropic Agent SDK.
-->

00:45:45 - Patrick Chouinard
So this week, I created my sixth version of a news pipeline. I think I got the right approach now.

00:47:00 - Patrick Chouinard
I also created an admin view, which allows me to manage the actual platform. So now I see the total number of artifacts that have been collected, enriched. This is basically which ones have been enriched by Perplexity [tool:Perplexity]. It found 64 today — this is the daily brief. It manages my budget for Perplexity and OpenRouter [tool:OpenRouter], and I have a little bit of quick action. This is the full pipeline. I can replay or run any part of the pipeline or the full pipeline, which will discover, ingest, enrich, make the brief, export the site, build it, and deploy.

00:49:00 - Patrick Chouinard
I can edit any individual article — which provider does it talk about, what bucket is it in, the summary, the editorial, the Perplexity stuff, the citations, and I can even go in, give some feedback — is it high quality, irrelevant, whatever. So all of this tracks how I grade whatever has been found, so it will hopefully evolve over time and improve over time.

00:49:32 - Scott Rippey
Patrick, I love this, because it's like a true engineer search log — everything you've got in there, like building in the back end.

00:49:41 - Patrick Chouinard
For all of the models that are being used to power this, I can even manage my API keys and the full log of execution. So this is in the back end, not shown to the user, compared to the front end.

00:51:00 - Patrick Chouinard
This will become a kind of central source of information that I can cross-reference with any and all aspects of everything else I'm doing.

00:51:09 - Jake Maymar
It's amazing. It's really, really amazing. I'm curious — are you doing the RAG pipeline? When you say enrichment, you're basically adding on top sort of meta information?

00:51:38 - Patrick Chouinard
<A>There's not even RAG in there. It's just searching and enriching — meaning Brave [tool:Brave Search] gave me a hyperlink about a subject I'm searching about. Then I just give that to Perplexity, and Perplexity writes a full article and enriches it with additional citations. Nothing more complicated than that.</A>

00:52:00 - Patrick Chouinard
This is something I gave to OpenClaw to create, and it created the very basic scaffolding — it was ugly at first when it was created, but then I just took it, gave it to Claude Code, and just made it more beautiful and more modern, and I started to build on top of it. But the scaffolding of the base project — entirely OpenClaw out of a text message and Telegram.

00:52:44 - Juan Torres
<Q>One of the things that I wanted to ask you, Patrick, is — I know you're saying that you're using Brave, but is Brave better than Tavily [tool:Tavily]? Because I've used Tavily before for news generation in the financial sector.</Q>

00:53:04 - Patrick Chouinard
<A>I'm using them for two different things. Tavily is a competitor more with Perplexity in a sense — it's more of a, it will write the article, it will write the AI output. I'm using Brave basically just as a Google search. The only thing I want from it is I gave it a subject and it gives me, "Oh, here's where I found that subject being discussed." Like here are sites that you can take a look at, and it has the brief little excerpt of one or two sentences. That's it. You could go with the full AI search and everything, but it becomes costly very, very quickly. Right now on the free plan, I'm good just to get my results. And that's all I need because then I'll get Perplexity Sonar [tool:Perplexity Sonar Pro] to do the actual enrichment.</A>

00:54:09 - Juan Torres
<Q>Which agentic system are you using?</Q>

00:54:12 - Patrick Chouinard
<A>No, this is pure — here's a list of subjects, Brave gives me sources where I can find those, and out of those, Perplexity goes and enriches it. That's it, that's all. And the agentic part is my feedback — upvote, downvote, and tagging with "this is high value, this is low value." And this is what I give to the weekly analysis that will then alter the list of subjects being searched and even the sources being used. If a source has been tagged as low value, it's going to be removed from future endeavors.</A>

00:54:49 - Patrick Chouinard
▶ So I try not to get agents everywhere just for the sake of getting agents everywhere. Whenever I can do something deterministic, I'll always stick with that.

00:55:10 - Paul Miller
<Q>What's your blocker been this week, Patrick?</Q>

00:55:15 - Patrick Chouinard
<A>Time.</A>

00:57:47 - Paul Miller
<Q>What version of Sonar are you using, Patrick?</Q>

00:57:52 - Patrick Chouinard
<A>Right now I'm using Sonar Pro because, again, it's just to write the excerpt. I don't need Sonar Reasoning Pro or anything like that.</A>

00:59:00 - Patrick Chouinard
▶ Prototype with Claude Code, put it in production with the Agent SDK [tool:Anthropic Agent SDK].

---

<!--SEGMENT
topic: Claude Code Mobile Interface — Scott's Open-Source Tool
speakers: Scott Rippey, Paul Miller, Juan Torres, Jake Maymar, Patrick Chouinard
keywords: Claude Code mobile, Anthropic Agent SDK, Cloudflare Tunnel, Google login, GitHub repo, TypeScript SDK, context window status line, background reconnect, Tailscale, mobile development, PRD documents, Claude Desktop
summary: Scott shares an open-source GitHub repo providing a mobile web interface for Claude Code, built using the Anthropic Agent SDK rather than a simple chat wrapper. It supports full Claude Code functionality (skills, MCPs, agents, Git branching) from a phone browser, secured via Cloudflare Tunnel and Google login. He discusses the background reconnect challenge and contrasts his approach with OpenClaw. Patrick shares his complementary workflow: prototype in Claude Code, then convert to the Agent SDK for production.
-->

00:59:25 - Paul Miller
So Scott, what's happening in your world?

00:59:30 - Scott Rippey
So I've got something to share with you guys that actually, if you guys want to take it, I have a GitHub repo. So let me share my screen.

00:59:53 - Scott Rippey
Do you guys see the Claude Code Mobile [tool:Claude Code Mobile]? Yep.

01:02:01 - Scott Rippey
So I have an open GitHub repo I'll put in the chat for you guys. If you guys want this, it's something where you can set this up for yourself. It's secure. You just have to set up the Google login [tool:Google OAuth], Cloud Console, Cloudflare Tunnel [tool:Cloudflare Tunnel]. You just have to do a few things to secure this. But this is just a great way to do some work from your phone when you're thinking of something. Because I didn't want to do the whole Claude Code web thing. I just don't like how that works. It's not the way my brain works.

01:02:43 - Scott Rippey
And see, it touches the tokens too, which is nice. So I wanted to know because there's a status line now in Claude Code where you can actually — I don't know if you guys know this — you can actually have a little status line in your Claude Code instance that tells you where you're at in your context window. But you have to install it.

01:03:12 - Paul Miller
<Q>Have you tried it with Tailscale [tool:Tailscale]? In terms of, it's a lot easier to do VPN stuff with Tailscale?</Q>

01:03:26 - Scott Rippey
<A>I mean, I just picked Cloudflare because I'm not doing a VPN. I'm doing a tunnel that's HTTPS, so it's not really actually a VPN. I've heard of that one too. I just didn't need to go that route.</A>

01:03:47 - Juan Torres
Yeah, actually, that was my question too, because I've been using Tailscale for a long time — well, six months now. And it's pretty dynamic because, especially when you're working with a team, you can add several servers, several computers. But yeah, I just wanted to ask if Cloudflare was a similar technology.

01:04:14 - Juan Torres
Another thing I wanted to ask — I can think of this as a way to keep developing the project: for example, I'm driving by and I have an idea for a feature that I want to add to my development environment, and I can use my phone. I don't know, Telegram or something — you can just tell your specific tunneling solution to create that specific MD file, save it into your docs within the specific folder, and then once you get back.

01:04:49 - Scott Rippey
<A>Yeah. So this is an application — this is a front end developed specifically with the Claude Code Agent Anthropic SDK [tool:Anthropic Agent SDK]. So you are logging in to use Claude Code on a web mobile version of this. This is not me doing an OpenClaw thing like doing a chat. This is actually like an actual application hooking directly into your Claude Code instance, if that makes sense.</A>

01:05:21 - Scott Rippey
▶ This is meant to be like a mobile way to be legitimate Claude Code. Like it's just, I want to have the same access I do on my computer on my phone. So you would actually have access to my skills, my MCPs, my agents.

01:05:47 - Juan Torres
<Q>Are you actually using it to start developing or just putting in your ideas?</Q>

01:05:48 - Scott Rippey
<A>Both. Like sometimes I'll have an idea and I'll be like, I'm just going to start building on my phone. I have projects in Claude Desktop [tool:Claude Desktop] that I use to do PRD documents — product requirement documents. So I'll come up with a plan on my phone, and then I'll just pump it into my mobile app now and I'll start building. I'm always going to finish the app on my computer, right? But just get it going. When you think of something, you just get Claude Code working for you. When you're not on your computer, finish it later, just get it working.</A>

01:06:34 - Juan Torres
And then after you create — I imagine you have Git CLI installed. So you create a branch.

01:06:42 - Scott Rippey
It has all the same functionality. So like if I wanted to do a branch — a lot of times some of my apps have a dev branch, a Git work tree that's a dev branch. Everything works the same. So whatever I open is where I'm in, and you can push to Git, you can be in a different branch.

01:07:07 - Paul Miller
Yeah, Scott, this is awesome.

01:07:09 - Jake Maymar
My question is, so I have 50 of these running. And right now, I've updated the little display in terminal. So it does the little animation and it tells you what it's working on. And I like the status line because the status line says what model as well as how much the context window is.

01:07:41 - Scott Rippey
If I like — because I see a lot of value just being able to look at my phone — but I am constantly looking for the animation and wherever it stopped, I have to basically put it. And so what I'm testing right now on this is — at first, obviously, if I went out of the browser and went back, it would have an error. It wouldn't tell me what it was doing in the background. And so I think I have that worked out. I have to test this.

01:08:12 - Scott Rippey
So the cool thing about this is I'm going to have version history on it, like I already do now. So if you guys see, I'll actually have updates on the public repo. So as I fix things, I will post it to the public repo.

01:08:27 - Scott Rippey
▶ So yeah, that's one thing where like, you want to be able to, if your screen goes off, or you go to another app, it needs to keep connecting in the background, which is the whole browser reconnect thing, right?

01:08:41 - Scott Rippey
I will say, all of the logging and what it's telling you it's doing, if you're in the app, is excellent. So like, it's actually better than Claude Code. Like their Agent SDK is so good. I'm like, why don't they put this in the terminal?

01:09:09 - Scott Rippey
They created Claude Code to be like, you can adapt this and change it and do whatever you want — nobody would work in this the same. Their whole goal is, you just put this into your own workflow. And so that's why I love the fact they have the SDKs, and they're really great. Because I would use the TypeScript SDK [tool:Anthropic TypeScript SDK] in applications for API calls, but this is the first time I got to use the Agent SDK, which is like Claude Code functionality, basically, to make this app.

01:09:44 - Scott Rippey
I mean, they give us access to everything. Like, I really love — that's why I keep saying I'm an Anthropic shill. They're not perfect, but they give us access, and they're transparent, and I like it.

01:10:00 - Jake Maymar
That was why I was disappointed with the OpenClaw situation, because I was like, man, that would have been amazing, having those two things together.

01:10:11 - Scott Rippey
Yeah, I think, long and short of it — OpenClaw is where it's going, in a large sense: hooking a lot of things in, having context, having a light database, all this stuff, heartbeats, like everything. But it was released way too soon to the general public, and it was a cluster. Like, everybody got hacked. It was a release issue, I think — because it was just a guy releasing a GitHub repo, and it went viral. I don't think he thought it was going to go viral.

01:11:00 - Scott Rippey
▶ I do actually think apps are not going to go away. I think we're still going to have AI engineers. I consider myself an AI engineer. I have an IT background, but I don't know how to code from scratch, but I can read code. I can understand tech stacks. I feel like the AI engineer is never going to go away. We're going to have to direct things. We're going to have to build applications. But I do see things like OpenClaw at some point where some apps may not necessarily be needed because a user could almost use something like that to just make something — they don't realize they're making an app. They're just like, do this function. They're basically using Claude Code as an agent because it's agentic by nature.

01:13:00 - Patrick Chouinard
▶ And once I have it working and it's stable, then I use Claude Code to convert all of its skills and all of the structure I put in the project into a Claude Agent with the Claude Agent SDK to basically make it production. So I prototype with Claude Code, I put it in production with the Agent SDK.

01:13:20 - Scott Rippey
Oh, dude, that's killer. I love that.

---

<!--SEGMENT
topic: Member Project Updates — Tom, Juan, and Client Acquisition
speakers: Tom Welsh, Juan Torres, Scott Rippey, Ana P, Jake Maymar, Paul Miller
keywords: Cursor, Claude Code, GoCardless, Stripe, Next.js, HTML, subscriptions, donations, Tailscale, data engineering, AI ops, LLM ops, ETL, agentic ETL, AWS EC2, YouTube content strategy, brand voice, San Diego tech community, sales funnel
summary: Tom shares his week building small apps, converting his CV to a website with Cursor, and evaluating GoCardless vs. Stripe for a military regiment donation site. Juan announces completion of his automation tool and plans to pivot toward client acquisition via YouTube content and local San Diego tech presentations, focusing on his niche of agentic ETL and AI ops on AWS. Scott and Ana offer advice on authentic client acquisition strategies and the value of an opinionated content voice.
-->

01:13:51 - Paul Miller
Tom, Tom, you have the con.

01:13:55 - Tom Welsh
Cool. How is everyone? I'm on 22 hours awake. Got up at 2am this morning. What have I been up to? I've just been literally just playing and learning and playing. After churning out just little apps, I've written myself a little journal. I've done an online CV type — converted my CV completely into a website using Cursor [tool:Cursor] this week.

01:14:28 - Tom Welsh
Also, I found quite an interesting nav bar on a marketing page and then went off and recreated it with Next.js [tool:Next.js], 480 megs, and then did an HTML5 version at 15k, which looks exactly the same, does exactly the same. It's like, yeah, sometimes it's good not to go and use these massive big tools, just go and do it old school.

01:14:58 - Tom Welsh
So I'm looking at — we've been using Stripe [tool:Stripe] quite a lot, and I'm doing a site for my old military regiment, and we're looking at getting donations and subscriptions and getting it paid in easily, and I found a site called GoCardless [tool:GoCardless], which basically just sets up automatic direct debits and manages all that. So it's proving a bit more challenging than using Stripe, because obviously there's a lot less documentation around it, but it's got legs — it's quite good for subscriptions. But for donations-wise, I think I'm still going to have to go the Stripe way, because the issue we've got is, if you've got like £500,000 coming in, with Stripe, that's £15,000 commission taken off you. And GoCardless, which is direct debit only, is much, much better for subscriptions.

01:16:20 - Tom Welsh
Apart from that, nothing really. I'm really just stuck in Cursor now. I've not made the switch to Claude Code.

01:16:36 - Paul Miller
<Q>Are you getting whacked on the cost, though?</Q>

01:16:37 - Tom Welsh
<A>Nope. I've never busted it, which is weird. Yeah, I've ended up in some AI gold mine somewhere where I can code all day and not pay anything for anything apart from a $20 subscription. I'm using 4.5, and yeah, it's just weird. No idea how I'm getting missed. I'm in some AI golden hole. I don't want to say anything about it to anybody because I might end up paying thousands.</A>

01:17:27 - Juan Torres
I'm pretty much done with my automation tool. So I just finalized it last week. So now my hands are more free. Now I have to look for new clients. I think I'm going to start creating more videos and get the sales funnel going to have something similar to what Brandon has developed.

01:19:00 - Juan Torres
Before doing AI engineering, I was doing data engineering, and so what my work allows me to do right now is be able to compound AI engineering on data engineering through agentic ETL [tool:agentic ETL], which is basically enriching data through LLMs — for example, in this project, extracting named entities from the description columns in general ledgers. So I'm thinking of doing a project just like that, and then going throughout the several San Diego tech groups and start presenting to start getting clients locally.

01:20:00 - Scott Rippey
It's always interesting seeing how people try to get business. I went through this — I was an IT person for like a senior consultant for like 14 years, and I left the business and started a video consulting, basically production business on my own. And it's funny, because I did video, which you would think is marketing, which it is. But I didn't really advertise for myself that way. Like I was still an in-person networker. Everybody's got their own thing, right? Like some people are comfortable with cold calling, some people cold emails. ▶ Do what's authentically you. And you will get the business. Just don't force yourself down a path that you're uncomfortable with, because it won't work.

01:21:00 - Juan Torres
And one of the things that I've been wanting to do more is YouTube content generation, not because I don't feel comfortable presenting, but because I feel like if I do create more videos, I'll have more mobility in terms of the wide network of people that could see me. So I don't have to live in San Diego, for example, if I wanted to move to another city or another country.

01:22:54 - Ana P
So I was going to say that videos are a great tool, but if you would like my two cents — in tech, people who are hiring, or at least people who have very technical profiles, can differentiate between noise and a quality developer. And if you're looking for getting clients or having the mobility you mentioned, I think the best you can aim at is also introducing that side of you to the content you're producing. ▶ Have your opinionated voice about what's happening, and let your experience show.

01:25:00 - Juan Torres
You're actually encouraging me to do something that's very innate to me. I don't think I'm a naturally very disagreeable person, but I like to drop my opinion on people sometimes when I do disagree. One of the things that I feel passionate about is the utilization of AWS [tool:AWS], because I've seen a lot of people that utilize other platforms that are easier to use in order to deploy AI production models. And so I think for me, if I were to pick a niche in which I do feel passionate about, it will be AI ops — not only LLMOps [tool:LLMOps], MLOps, but actually how do you interact with middleware to be able to then interact with the EC2 instance [tool:AWS EC2] to deploy a model to operate within the EC2 instance and start creating a production-ready AI product. And I think a lot of people are not doing that because a lot of people are feeling comfortable with code, but they're not comfortable with the cloud technology and the networking that cloud technology implies.

01:27:22 - Jake Maymar
Juan, you just nailed it. If you go deep on that — we were on a call right before this talking exactly about that. And that's very rare that anyone talks about that. So you just talk about this just a little bit, that's going to get people excited — enterprise people very, very excited.

01:27:54 - Jake Maymar
And then what I've been doing is I basically gave Claude everything — just kind of everything about me, brand voice and background and my preferences and just everything. And then I said, "All right, now know me. Why don't you do tremendous deep research on what's effective, what's out there that would possibly appeal to me? And you already know me. And then how should I advertise? Who should I interact with?" And it's been really good. ▶ I'd highly recommend doing something like that.

01:28:38 - Scott Rippey
Jake just reminded me of something. I'll put this in the chat. Like this is old, old stuff. Before I got into AI, when I was working on stuff for my video business, I created a lot of frameworks and I have a file and a prompt that you will attach — obviously best in Claude, but it works anywhere — that helps you create a file that helps your brand. So that anytime you're writing, if you're trying to do posts, whatever it is, if you're writing something with AI, it knows — it gets you a lot closer to your actual brand voice. It's a "Build a Better Voice" framework that I created. I just used this for a real estate agency and gave it to all their agents and they just ate it up. It takes 45 minutes to an hour to go through. It will ask you enough questions where it's really, really deep, and it's a file you just attach then whenever you're writing in the LLM.

---

<!--SEGMENT
topic: Lucid — Hallucination Detection Tool Demo
speakers: Ty Wells, Jake Maymar, Juan Torres, Paul Miller, Ana P, elijah stambaugh
keywords: Lucid, hallucination detection, LLM verification, SWE benchmark, patent pending, arXiv, academic endorser, CLI, code verification, transformer limitations, trylucid.dev, red teaming, IP protection
summary: Ty Wells demos Lucid, a tool he's building to detect and fix hallucinated code generated by LLMs, running as a CLI layer that evaluates code as it's written. He walks through benchmark tests on trylucid.dev and discusses the patent-pending status. The group discusses the challenge of getting an academic endorser to publish on arXiv, and Ana P offers to connect Ty with a PhD contact in electrical engineering.
-->

01:31:14 - Ty Wells
Scott, thanks for the transition about hallucination into what I'm going to show this week. It adds a perfect combination. You may hear some noise, I'm having a dinner party. I snuck away.

01:31:35 - Ty Wells
Okay, I think I spoke about Lucid [tool:Lucid] a while back. Basically, it's a layer, the way I see it, to help reduce hallucinations in any code that AI generates. And so I ran it through some tests. I put it on the SWE benchmark [tool:SWE benchmark] to run some benchmark tests to prove, basically, that the models are going to hallucinate — that's proven already. The articles that are referenced, but what it proves is that with the right set of data values, we can locate and extract the hallucinated part of the code and fix it.

01:32:35 - Ty Wells
So if you come on trylucid.dev [link:trylucid.dev], you can see here. So I'll walk you through. I'm presenting it to another community here on Friday. And so instead of me doing a separate presentation, I just built it into the site. And these are tests that are done — all the benchmarks and everything there — that basically say...

01:34:05 - Juan Torres
<Q>So essentially, it's based on kind of like dialectical red teaming against the code base that you have on your GitHub repository, right? So in that sense, does it work only as a result, as a function of having in your GitHub repository, or can you have a counter red teaming would leave in your Claude Code as it's finalizing the process?</Q>

01:34:33 - Ty Wells
<A>It's countering when you're — like, I'm running it through a CLI [tool:CLI]. So as the code's being written, I am evaluating, assessing that code, and finding the hallucinated parts, and rewriting the code, and delivering to you the fully functional code. So like I said, you can go in here and grab any function you have anywhere, toss it in here, and check it and see. It's really about verification, right? Can the output be verified?</A>

01:35:34 - Jake Maymar
Yeah, this is cool, Ty. This is great. Very cool. I think it's a game changer.

01:35:38 - Ty Wells
I think it's a game changer. It's a layer. It's a layer for the LLMs. But even — I think Scott was talking about the transformer — I'm looking at trying to do something with that to get beyond those scaling limitations using itself. So a lot of dog-fooding going on here.

01:37:00 - Paul Miller
<Q>Is it time to publish it to X, and then 80 days, sell it to OpenAI for a billion dollars?</Q>

01:37:07 - Ty Wells
<A>Well, it is, but if I put it on there — I was going to. I changed my mind, and I said I would take a different path, because although I have the patent now, I can do it. I'm not in academia. I need an endorser. I need somebody that has published something in the CS space in the last, I think, five years. So if you know anybody, let me know.</A>

01:37:48 - Ty Wells
But yes, you're absolutely right, Paul. If I do that — and a billion's not going to be enough, sorry. I mean, if you can grasp what the product is.

01:38:06 - Jake Maymar
This is amazing. So, Ty, you're trying to get ahold of academia to get white papers?

01:38:10 - Ty Wells
Yes, to get to post the article. Because I have the patent pending, I feel comfortable I can post the paper. But it's already up there. I just need an endorser.

01:38:23 - Paul Miller
So I know that Maxim had done some of the stuff last year. So maybe just like a message through to Brandon and ask him if you haven't already, because I think we knew someone.

01:38:48 - Juan Torres
<Q>Isn't there a problem with reading the intellectual property for code?</Q>

01:39:00 - Ty Wells
<A>There is a risk, but the algorithm that I have, I think it's clearly definitive — not broad like an idea. This is the secret sauce. You can put it together, but you can't put together all of the ingredients. So I feel confident that that's not going to be an issue. I mean, I don't think the tech exists today. I know people are working on it, but I don't think anybody has published anything. I didn't find anything that was published.</A>

01:40:56 - elijah stambaugh
I don't fully understand it, but I do know somebody in academia that I can connect you to.

01:41:03 - Ana P
He's got his PhD in Electrical Engineering and Image Processing. So I sent you a message with my email.

01:41:14 - Ty Wells
Okay, perfect. I'll reach out.

01:41:22 - Ty Wells
Thanks. I'm going to have to leave you guys with that. I gotta get back to my dinner party.

---

<!--SEGMENT
topic: Ana's Projects — Congressional Trading Tracker and Meal Planner App
speakers: Ana P, Juan Torres, Tom Welsh, Paul Miller, Patrick Chouinard, Scott Rippey
keywords: Quiver Quants, congressional trading, Yahoo Finance, Cloud Run, D3, NVIDIA, ETFs, mutual funds, retail investors, mind diet, Alzheimer's prevention, meal planner, Apify, web scraping, iOS app, Amazon affiliate, Google Cloud Run, financial data API
summary: Ana presents two personal projects: (1) a congressional trading tracker that pulls disclosure data from the Quiver Quants API, enriches it with Yahoo Finance, and visualizes top-held tickers and sectors for retail investors, deployed on Google Cloud Run; (2) a meal planning app based on the MIND diet, featuring an AI assistant ("Mindy") for meal organization and grocery cost optimization. The group suggests adding candlestick charts, historical backtesting, and using Apify for grocery price scraping.
-->

01:41:31 - Ana P
Hi, I'm not sure how I'm going to follow that. But I do have a couple of projects that I can show you. The first is something that I haven't incorporated AI into yet. And the second is something that I'm currently building. So first, in my case, the projects I'm building are for personal use.

01:41:59 - Ana P
And one is — financial advice, but at the same time like take it with a grain of salt. It's a bit controversial in that I'm consuming data from Quiver Quants [tool:Quiver Quants], which is an API that parses information from the disclosure that people in Congress make for the assets that they buy. And the main idea of my project is they know better. They have so much more information of how the markets are moving. They have a better grasp of how the future might look. And I'm counting on one, potentially their education, and two, the fact that they can afford financial advice that I cannot. So the main thing I'm doing is grabbing the data from this API and summarizing it.

01:43:00 - Ana P
So I'm trying to make it as least controversial as possible. I can show you the final results that I have. I wanted to say, in the last three years, in terms of asset types — stocks, ETFs, and mutual funds — what are the tickers or assets that they currently hold the most, so things that they have bought and they haven't sold, and looking at that as a pool. I'm not touching the name of the congressperson — I'm showing you the pooled amounts. And then the second part where AI would come in is I want to add a little section for retail investors — for people who do it for their personal portfolios — where they can, for example, put in their ETFs and ask: is it diversified enough? And having as a reference point the holdings that people in Congress have.

01:44:13 - Ana P
Just one second, bear with me. And any feedback, I'll be glad to hear.

01:44:50 - Ana P
So here it is. It's really just — I have just the little summary. This website reports on congressional trading activity to hold retail investors identify attractive assets. The below analysis pulls together trades disclosed by US Congress members in the last three years and informs on top tickers and positive net transactional balance to date. The report below excludes anything that's a derivative because that's too complex to include here, and I'm also grabbing more information on the tickers from Yahoo Finance [tool:Yahoo Finance], so anything that is not in Yahoo Finance, I cannot report on.

01:45:32 - Ana P
And then in terms of stocks, the first one is NVIDIA, followed by one that has a ticker "Watt," but I don't know exactly what it is. This made sense to me — NVIDIA being at the top made sense to me. And then if you go to top industries, you see semiconductors specifically, then banks, diagnostics and research, and then software applications and software infrastructure. And then you have the same for top ETFs, which this one is something related to cryptocurrency, which I thought was interesting. And then you have the top mutual funds.

01:46:12 - Juan Torres
And then I have a little disclosure at the end, just explaining the data sources, the intended audience. So it's trying to be very safe — just retail investors, buy and hold, and then a Nugget of Wisdom by Kevin O'Leary, which is like avoid having more than 5% in any asset, avoid having more than 20% in any sector, and diversify in geographical markets as well.

01:46:39 - Juan Torres
And then I want to add a little chat here with a little robot where you can say, "Oh, but if I want to look at S&P and this with these weights, like how does that look compared to this?" So kind of like you can play around a little.

01:47:00 - Ana P
My main goal was I wanted to play with deploying with Cloud Run [tool:Google Cloud Run]. And I wanted to do something that was just a bit interesting.

01:47:10 - Juan Torres
No, yeah, this is great. And like I said, Quiver Quants — they're some of the most scientific materialist analyzers of investment, especially when they analyze politicians' investments. And you can actually make really interesting investment decisions based on that, like the decisions by Nancy Pelosi, for example.

01:47:36 - Juan Torres
<Q>One of the questions that I wanted to ask you is, I've used Yahoo Finance before for other projects. And it's great because it's free. But since it's more like an open source stock performance review, sometimes the code changes a lot. And so I have to go back and try to regenerate it. Have you found any issues with that? And if so, are you thinking of maybe using another technology?</Q>

01:47:56 - Ana P
<A>I'm using very, very little. The information that Yahoo Finance I'm extracting is only the information on the industries, and in the case of the mutual funds, I have another view that aggregates the insights of the ETFs as well, and that's basically all that I'm consuming from them. But yeah, it's very open source, and the data is incomplete for mutual funds — at least a large percentage has incomplete data. It's a negative point, but it's what it is. It's free.</A>

01:49:00 - Tom Welsh
<Q>Ana, have you thought about doing, sort of looking back in time, and comparing the indicators versus the market change, and sort of comparing it?</Q>

01:49:07 - Ana P
<A>I had not. That's something that I might add to this little project. For me, my objective right now is to iterate fast, because that helps you to learn faster. So I wanted to do something like open it and close it. But for a second iteration, that's something that I would consider and I had not thought about it. So thank you so much.</A>

01:50:00 - Ana P
Yeah, is really cool. I just want to say, are you going to put any charts on that, like candle charts or something, just for this three, six, one year, five year yields on what's going on, so you can actually see the candlesticks and see where they're moving.

01:50:13 - Ana P
Yeah. Because that makes some really good stuff. It gets you into a bit of graphing as well, playing with the GS graph or whatever.

01:50:20 - Ana P
Yeah, that's a good idea. I might. Again, I will grow this. And that's something that definitely will add value — being able to know how they have performed in the past.

01:50:36 - Ana P
Yeah, I used to work for a company called CMC Markets [tool:CMC Markets], which is an online trading platform, and graphs were a big seller and the visuals are great. So yeah, definitely worth looking at.

01:50:49 - Ana P
And then the second one that I'm working on is kind of like a meal planner that will help the user organize their meals. My objective in here is really for my dad. So I want to make an app to help him eat more healthy and also for me. And then as I've been talking to people, I have received the feedback of like, "If you build this, I would use it." My idea is to use something that's called the MIND diet [tool:MIND diet]. So it's supposed to like prevent Alzheimer's and other things. And it's very easy to follow. And I want to have a robot and AI that organizes everything for you. But at the same time, it doesn't go away. So you have the app and you have this was your meal plan, this is your progress, and you can track everything there very easily. And the part that I want to add for me is the part to help you with optimizing your spending for the grocery store.

01:53:00 - Scott Rippey
More or less on track. Hopefully I can show you guys something next meeting.

01:53:26 - Paul Miller
<Q>Ana, have you looked at using Apify [tool:Apify] for getting price data from maybe a couple of different supermarkets to help ground the costing of the recipes and the pricing?</Q>

01:53:51 - Ana P
<A>I had not considered it. I'm going to write it down. I didn't know that website, so I will.</A>

01:53:55 - Scott Rippey
▶ Yeah. So for scraping, Apify is legit. If I was going to scrape any data, I would go there, because they have predetermined actors, and you can customize them. I would not scrape with anything else, honestly. That's amazing. Just keeps it really straightforward, and then you don't have to think about the website scraping part and any of that stuff, and you just get the data and set it up.

01:54:26 - Patrick Chouinard
Great stuff, Ana. Also, just want to say, hit me up on the side if you ever want to talk — I'm a nutrition nerd, like fitness and health, so if you ever want to talk about some of that stuff for your app, hit me up.

01:54:37 - Ana P
No, I would actually really like your feedback. I'm trying to make it very funny. It's like, it's the MIND diet, so the AI is called Mindy. I might play with potentially publishing on iOS if it works, but we'll see.

---

<!--SEGMENT
topic: Claude Code /insights Command and Closing Reflections
speakers: Patrick Chouinard, Paul Miller, Jake Maymar, Scott Rippey, Tom Welsh, Morgan Cook
keywords: Claude Code /insights command, usage analysis, workflow optimization, skills, hooks, community value, Brandon, weekly call, Discord, open-source community, AI pace of change
summary: Patrick highlights the new /insights slash command in Claude Code, which analyzes a month of usage and generates personalized workflow improvement recommendations and skills. The group closes with reflections on the unique value of this weekly call — its open knowledge-sharing culture, multi-domain perspectives, and the quality of the core group that consistently shows up — contrasting it with the largely inactive broader community of 11,000 members.
-->

01:55:19 - Paul Miller
Yeah, actually, one little thing I wanted to mention — maybe it's me who just discovered it, but I don't know if you've seen the new `/insights` command [tool:Claude Code /insights] inside of Claude Code. Anybody who hasn't tried it, please do right now.

01:55:35 - Paul Miller
▶ This is absolutely amazing. It analyzes your last month of usage of Claude Code, comes up with recommendations — what you do right, what you could improve on — and it gives you a whole lot of skills that you could build, and it will build them for you to improve your workflow, if you need to add a hook somewhere. Anyway, it's a full analysis of your usage with one slash command. Honestly, for anyone who hasn't tried it, do it now. You're going to absolutely love it.

01:56:08 - Paul Miller
Super cool. Yeah, for sure. Thanks, Patrick.

01:56:14 - Jake Maymar
Always full of knowledge bombs. Who would like to jump on next? Or is everyone good for today?

01:56:30 - Paul Miller
Okay, we'll take that as a yes. Thank you for putting up with my hosting this week. Next week, we will have Brandon returning. We'll probably have a whole lot of new models appearing, and we might actually hear what the payout price was for ClaudeBot, but we'll see. Everyone, enjoy the week, and have a great day.

01:57:01 - Scott Rippey
Paul, do you want me to publish the summary of the meeting?

01:57:08 - Paul Miller
Yeah, that would be good. Thank you, Patrick.

01:57:12 - Scott Rippey
I was going to say, for people watching the video, they don't get the links. So if we put links in the chat on the side here.

01:57:30 - Jake Maymar
Yeah, so we export that.

01:57:37 - Scott Rippey
I'll put the summary of the meeting and if you want Paul to add in the comment.

01:57:55 - Scott Rippey
I feel like the group isn't busy at all, but like those of us that always show up on these calls — it's the same guys every time and girls. It's like, it's like the same people. I'm like, I've never been in a school group that's so dead, yet these calls are the best. I'm like, what is going on with this? Nothing happens in the group, but these are my favorite calls by far.

01:58:22 - Scott Rippey
I think it's just kind of what you were talking about — what organically forms. I'm sure that there's probably something going on with the school, but in all fairness, this is the call I don't want to miss. Because I'm in an NNN group for Nate Herc, and I'm kind of going to leave that one. I'm paying for that one. But I'm like, the fact that Brandon has a free group, but these calls are — I mean, granted, I know, obviously, thanks to Patrick and Paul for doing this. But it's like, still, there's so much value — once a week, for a couple hours talking about this stuff and seeing what people are doing. This is like so much more my speed, the way I think about things. And it's not focused on just one platform.

01:59:30 - Paul Miller
Yeah, I totally agree. And it's kind of interesting. I'd be really curious to look at the metrics and see how many people watch the videos. Because I feel like people are missing out, man. I feel like nobody knows — like these calls are gold to me.

02:00:00 - Scott Rippey
We all know what everyone brings to it and the perspective that comes out of the conversations.

02:00:06 - Jake Maymar
It's just coming from so many different angles. And I kind of think this moves so fast — the AI world. Tech used to be you could take your time, you could go to a conference, you could read a paper, you could gain your comfort around the change. But you just can't do that when it moves so quickly in this field.

02:00:32 - Scott Rippey
I've been in tech for many decades, but without having this kind of forum with the wise heads that appear, I find it quite challenging. And everyone's also taking it from another perspective as well.

02:00:54 - Scott Rippey
▶ I also think Brandon attracts the right kind of people. Like the fact that this is still the same kind of thing, without him being here, speaks volumes to me.

02:01:10 - Scott Rippey
It's that willingness to share. Because what we share is gold. Like there's a lot of value on this call.

02:01:16 - Tom Welsh
And I think that's kind of the difference. Because I'm on a whole bunch of different calls. But this is the call I really try not to miss. I don't care if it's people who are — I don't want people to be intimidated by knowing as much as some of us may know. None of us are perfect. But there are all levels of experience. And I love hearing about somebody who's like trying to figure it out at the start. Some of us are sharing gold, whatever. It's just such a good environment.

02:02:00 - Scott Rippey
With a lot of different expertise, too, from different fields.

02:02:05 - Tom Welsh
Everybody comes from a different arena, which I really think helps perspective-wise.

02:02:15 - Tom Welsh
I would also say, I would like the 11,000 people just to turn up as well, because then we'd be overwhelmed, you know?

02:02:23 - Paul Miller
Yeah. I think the core group that's in here now, like you say, it's pretty regular every week who turns up. For a group of 11,000 members, the forum is really dead. I think I'm the only poster there.

02:02:46 - Paul Miller
I'm like, Nate's group is, I think, smaller, and I'm like, how are people way more engaged? But these — yeah, this is still the best call I've ever been on. Every time we do it, I'm like, I don't get it.

02:03:04 - Scott Rippey
Yeah, I think a lot of it comes from the YouTubers where they watch Brandon's videos, which are really, really good, and they come to see some information. There's no information there, so they just lurk. And it's pretty much the same in the Discord channel. It's really quiet.

02:03:21 - Scott Rippey
Well, I think Brandon's approach on the videos seems to be he's happy to share. He's happy to give away. And that's what he's brought to these calls — where he's happy to give, he's happy to share, he's happy to give away. And then when the lead person's trying to do that, and he goes around and encourages everyone else to do that, then it's a very open forum. And a lot of those calls are quite, "Oh, well, you have to pay this for that," or "No, we're not hearing that." And yeah, not the same.

02:03:56 - Patrick Chouinard
Yeah, he genuinely wants to help people, and he has really good advice.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript and were not resolvable via the alias map:

- **Bastian Venegas Arevalo** — appears once at 00:37:31; may be the same person as "Bastian" referenced elsewhere in the transcript
- **elijah stambaugh** — appears at 01:39:56–01:40:11; transcript attribution appears garbled (lines attributed to elijah stambaugh repeat content already attributed to Ty Wells, suggesting a transcription error)
- **Jake Maymar** — passed through unchanged; not confirmed in alias map
- **Ana P** — passed through unchanged; last name not provided in transcript
- **Juan Torres** — passed through unchanged; not confirmed in alias map
- **Tom Welsh** — passed through unchanged; not confirmed in alias map
- **Ty Wells** — passed through unchanged; not confirmed in alias map
- **Morgan Cook** — passed through unchanged; not confirmed in alias map