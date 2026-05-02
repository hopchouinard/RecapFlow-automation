=== SESSION ===
date: Unknown (Tuesday meeting)
duration_estimate: ~105 minutes
main_themes: Google ADK agent development, clinical trials API integration, AI coding tools comparison, Lovable app building, MCP/chatbot development, AI video/audio generation, agentic enterprise architecture, WhatsApp message mediation app

---

<!--SEGMENT
topic: Meeting Introduction and Format
speakers: Brandon Hancock, AbdulShakur Abdullah
keywords: round robin, meeting format, updates, screen sharing, ADK, group rules, new members, project updates, troubleshooting, community
summary: Brandon Hancock opens the weekly group call, explains the round-robin format where participants share project updates or request help with problems they are stuck on. AbdulShakur Abdullah is introduced as the first speaker. This segment establishes the recurring meeting structure used throughout the session.
-->

**00:00:23 - AbdulShakur Abdullah**
Hi, Brendan, how are you?

**00:00:25 - Brandon Hancock**
Well, hello, hello, how are you doing today?

**00:00:27 - AbdulShakur Abdullah**
Doing well. Awesome, awesome.

**00:00:30 - Brandon Hancock**
We'll definitely give everybody a few minutes to hop on. I know it's a busy week. Let me get everything set up notes-wise real fast, guys.

**00:00:50 - Brandon Hancock**
Well, perfect. Well, thanks, guys, for hopping on today. I was going to say, definitely, some are starting to be some new faces in the group.

**00:01:00 - Brandon Hancock**
So I'll give a quick overview before we get started just to do rules and everything and then we can dive in. So first things first, usually the way we go around the group is we kind of go round robin. So I'll drop a screenshot in the chat, basically the order of people I'm seeing on my screen. And this is the order I'll end up calling people. And usually the way we do it is we do two kind of updates. So one, if you have a cool update or topic that you'd like to talk about, feel free to bring it up. And then option two is if you're stuck on something or you just want a second pair of eyeballs on a problem that you're working on, happy to help out with that as well. So that's kind of the general gist.

**00:01:48 - Brandon Hancock**
And Abdul, you were actually first on my list today.

---

<!--SEGMENT
topic: Clinical Trials API Agent with ADK
speakers: AbdulShakur Abdullah, Brandon Hancock, Bastian Venegas
keywords: ADK, Agent Development Kit, clinical trials API, loop agents, sequential agents, exit loop, state management, Python, natural language query, medical database
summary: AbdulShakur Abdullah describes building a natural language interface to the ClinicalTrials.gov API using Google's Agent Development Kit (ADK), targeting doctors and biotech/pharma professionals who need to search trial data. Brandon Hancock recommends loop agents and exit loop functionality as the right architectural pattern for iterative research tasks, and shares his ADK crash course repository with relevant examples.
-->

**00:02:00 - AbdulShakur Abdullah**
I'm in the hot seat. So I'm working on connecting to the clinical trials API [tool:ClinicalTrials.gov API] with an agent. So I was stuck for a while on getting the agent to directly write the calls, but then I felt like I was kind of making it too complicated. So I switched to making the calls with a Python program and just having the agent pull whatever the person puts in to kind of prompt the Python program.

**00:02:38 - Brandon Hancock**
<Q>So a few quick questions. So what is the goal of what we're trying to do? And if you have any background on, like, are we using Crew, LangChain, Agent Development Kit? And if you want to screen share, too, that's totally awesome as well.</Q>

**00:02:52 - AbdulShakur Abdullah**
<A>Oh, I was using ADK [tool:Google Agent Development Kit]. The goal was basically to make it easy for people to query using natural language on any clinical trial, so I could then kind of promote that as a quick reference resource for people.</A>

**00:03:15 - AbdulShakur Abdullah**
And I don't have as much development experience, so I was actually going off of your ADK short and kind of rewriting over that.

**00:03:38 - Brandon Hancock**
<Q>So when you say people query the clinical trials, what are we trying to pull out? Just like a research report? Are we trying to answer their question and say like, oh, here's the answer to your clinical trial? Or what are we trying to do?</Q>

**00:03:47 - AbdulShakur Abdullah**
<A>So people are just trying to look at the clinical trials database where they kind of search. My end goal is eventually to have multiple different databases linked together that people in the medical field can kind of reference. So there's quite a lot of free resources out there, but for the clinical trial one, it's just, hey, I have a patient that is showing these symptoms, are there any clinical trials within 100 miles, and then it can do that search without a person trying to use the direct website.</A>

**00:04:34 - Bastian Venegas**
<Q>The goal is to enroll them in the clinical trial?</Q>

**00:04:40 - AbdulShakur Abdullah**
<A>No, no, the goal is for doctors and other groups to be able to find open or closed clinical trials. In biotech and pharma, quite a lot, we're just searching through clinical trials to see what other companies are doing, to see what trials are open. If I'm a doctor, if I have a patient that has certain symptoms, to see the trial I was monitoring, if it ended and had a good endpoint. Then once I find that out from clinical trials, I'll go see if the company published a press release about it.</A>

**00:05:24 - Brandon Hancock**
So I'm in the middle of working on the ADK crash course, and I think something that might be super helpful to what you're doing is it's called loop agents. So this will be in the crash course, but basically what would be awesome is right now the way ADK works is you submit a request to an agent and it makes a tool call. And that's kind of it — it's kind of a single shot. Did I get the answer? Cool. And just report back. But what could be really cool is inside of using a loop agent is you could set up basically two agents in sequence. So one would be like a planner agent, and the second one would be a research agent. And basically, they would work in conjunction to go off and continually research and continually iterate and make additional tool calls until it comes up with a proper plan to report.

**00:06:24 - Brandon Hancock**
So you would use a series of loop agents and sequence agents. So let me — don't worry if it's a little overwhelming, guys, just because the Masterclass — I literally just finished this today. I'm going to start recording tomorrow. But here is the important part for you guys to see. It basically has — this is like a writing version, but you can do the same with research. So what you would do is on part one, you would have a loop agent. So this is where you would have the planner and the researcher, and they would continually research over and over and over until they hit some sort of max iteration. And then afterwards, you would have it create a report that you would then give to a report agent. Like, it would have the research, and then you would pass it over to a report agent who would generate that final report to share back with references and everything.

**00:07:24 - Brandon Hancock**
<Q>Does it have to be a max iteration, or can you look for some other endpoint?</Q>

**00:07:38 - AbdulShakur Abdullah**
<A>I'm talking about, like, say, some amount of information is found, or no more new trials have been found, or something along those lines.</A>

**00:08:01 - Brandon Hancock**
And what you would do is they have this thing called exit loop. So as soon as criteria is met, you could say, like, as soon as five resources are found, as soon as three resources are found, you could call exit loop. And basically, you create a function. This function has access to state. So you would have `toolcontext.state`, and you could just check the number of resources found greater than five, great, escalate, and return. And then that's how you could stop the loop as well.

▶ **00:09:00 - Brandon Hancock**
I think the loop agent and exit loops is exactly what you should look at implementing. And if you just want a final thing, I'll just go ahead and share it with you guys. So this is basically 11 examples that I was going to cover in the tutorial, the crash course. I just dropped the repository, so there's a ton of examples in there. But yeah, so the three that you really need to look at are sequential agents, stateful agents, and then loop agents. Those are the three I would look at if I was you.

**00:10:07 - AbdulShakur Abdullah**
I mean, I am on a Windows machine, so that was annoying with the Windows quirks.

**00:10:15 - Brandon Hancock**
Yeah, no, Windows is definitely not the easiest on getting things set up, especially with Python environments and everything.

---

<!--SEGMENT
topic: Freelance AI Consulting and Business Model
speakers: Jake Maymar, Brandon Hancock
keywords: LLC, S-corp, pitching, POC, proof of concept, N8N, team formation, budget, AI consulting, freelance, contracts
summary: Jake Maymar provides a high-level update on active client pitches and a collaborative business model where individual LLCs form teams to pitch larger contracts. He explains that larger team structures unlock bigger budgets from enterprise clients. He also mentions heavy use of N8N in upcoming projects, though details remain confidential pending contract signing.
-->

**00:10:30 - Brandon Hancock**
All right, Jake, you are next up, buddy. What cool projects are we working on, man?

**00:10:35 - Jake Maymar**
So, yeah, I totally missed you guys. So, just doing a lot of pitches, you know, did a whole bunch of POCs, and now just kind of in conversations for building out different things. So, I will keep you posted, but, yeah, it's been insane.

**00:11:00 - Jake Maymar**
Yeah, they're on the West Coast, so it's the exact same time as this meeting, which is like a killer, and I've been trying to move it.

**00:11:14 - Brandon Hancock**
<Q>Is there any cool info you can share, just like high level about potential type of work, or anything like that, or is it all hush hush?</Q>

**00:11:24 - Jake Maymar**
<A>So much, well, that's the thing, it's like, there's so much, I mean, it's very, very exciting. I guess I'll say this, we're building a nice sandbox that has all these Lego pieces, and I can definitely share more once that's sort of a little bit more nailed down. Right now, I'm kind of in that weird state. As soon as I can, I will.</A>

**00:12:01 - Jake Maymar**
But I will say that there's a tremendous amount of N8N [tool:N8N] stuff. And I'm sure you guys talk about that all the time, too. But yeah, I mean, in general, nothing new to report, just a lot of exciting. And I'm really looking forward to giving you an update when things are signed.

**00:12:57 - Jake Maymar**
So basically, each individual has an LLC or an S-corp, and as an individual, when you go into a pitch, you're just the individual, so you can only get a certain size budget. But if you're a team, you can get a larger budget. And so we've sort of formed teams from these LLCs into teams, and then we go into a pitch as that company. And I think it's a pretty decent model. And sort of the way it works is basically the person that wins the job, that's who we go in as. And then we're kind of waiting on a whole bunch of different things. And then once one of those is signed, most likely everyone will gravitate towards that and then just start building that. Because the projects are big enough that it could actually sustain — but it's kind of getting to that point.

---

<!--SEGMENT
topic: AI Coding Tools Comparison
speakers: Jake Maymar, Brandon Hancock, AbdulShakur Abdullah, Sam
keywords: Cursor, Windsurf, Roo Code, Cline, Claude Desktop, GitHub Copilot, Qwen 3, OpenRouter, ESLint, Next.js, TypeScript, Azure, subscription pricing
summary: The group compares AI coding assistants including Cursor, Windsurf, Roo Code, Cline, and Claude Desktop. Discussion covers pricing models, capability differences, and workarounds for enterprise data security constraints. Brandon Hancock advocates strongly for Cursor at $20/month, while Jake Maymar and AbdulShakur Abdullah share experiences with Windsurf degradation and Roo Code's power-versus-cost tradeoff.
-->

**00:14:30 - Jake Maymar**
I'm still having problems with Next.js [tool:Next.js] TypeScript getting progress bars and getting that whole progress situation sorted out perfectly. The other thing I'm kind of curious in general is I've been using a lot of no-code solutions. I've been using Claude Desktop [tool:Claude Desktop] a lot. That's freaking amazing. And I'm curious, is everyone still using Cursor [tool:Cursor]? Is there another thing? And are there any open-source models that you are using that you find are actually pretty good for coding?

**00:15:27 - Brandon Hancock**
<A>So, I mean, I'll just answer. I am addicted to Cursor. So, that's me. Anyone else, out of curiosity, anything else?</A>

**00:15:37 - AbdulShakur Abdullah**
Well, I took a look at Roo Code [tool:Roo Code], but I didn't get too far. But I heard Qwen 3 [tool:Qwen 3] was quite good with Roo Code.

**00:15:48 - Jake Maymar**
Oh, that makes sense. Yeah, Roo Code's expensive, though. That's the only thing. What's nice about Cursor is it's got a subscription. Windsurf [tool:Windsurf] has a subscription. But Roo does some amazing stuff, but it's really expensive.

**00:16:05 - Jake Maymar**
<Q>Now how can you — oh, so then you do like OpenRouter [tool:OpenRouter] with Roo, with Qwen 3?</Q>

**00:16:13 - AbdulShakur Abdullah**
<A>Mm-hmm.</A>

**00:16:17 - AbdulShakur Abdullah**
I, to preface, I haven't gotten it to work for me, so this is just what I heard.

**00:16:25 - Jake Maymar**
Yeah, I've been using Cline [tool:Cline], and just using it with Claude, and it kills all the ESLint errors, which is really, really nice, especially the really complex ones.

**00:16:48 - Brandon Hancock**
<Q>So real quick on Roo Code. So is it, from what I'm seeing, a Cursor alternative, right?</Q>

**00:16:59 - AbdulShakur Abdullah**
<A>It's a VS Code plugin, but yeah, it's an alternative.</A>

**00:17:03 - Jake Maymar**
Yeah, Cline is kind of the capable one, and Roo is much more capable. Roo really does knock it out of the park almost every single time, but it's expensive, and that's the thing. So I'm interested in getting Qwen 3 to work, because that would be kind of nice.

**00:17:34 - Jake Maymar**
But the funny thing is, I haven't used Roo in a while, and all of these things are constantly updating. You know how I love Windsurf. It's not as good. Like, something happened, and maybe it's my files or whatever, but something happened, and I just basically — I mean, I have a subscription, and I have a low cost because I got in early. But yeah, I'm looking at Cursor as well.

**00:17:58 - AbdulShakur Abdullah**
No, I'm on Windsurf right now, but I also noticed this week that I just stopped using Windsurf. I actually started just going back and forth between Claude and Claude Desktop and pasting it into Windsurf.

**00:18:23 - Jake Maymar**
Yeah, that's exactly. And then what's the point, right? Well, Claude Desktop, what's interesting is Cline did a much better job with ESLint because they're all connected — did a much better job than Claude, which was really surprising. And maybe it's my prompt and maybe it's other things, but Claude Desktop, I'm pretty much using Claude Desktop all the time now.

**00:18:50 - Brandon Hancock**
Yeah, I mean, I don't know about you guys, but I mean, just I still cannot get off of Cursor just because — like, I use it so much, and it is so hard to go above the limit, and then even when you do, like, it's not wild for how much faster you get to move. So, yeah, I mean, the main thing is just, like, whichever one gives me the solution the fastest that I don't have to keep changing, and Cursor just seems to be industry standard at this point, and I love it. Like, I love nothing more than drinking a sip of coffee, and I'm like, build this. Here's the example doc. Here's what I want. Go.

**00:19:36 - Jake Maymar**
<Q>Brandon, is there any YouTube or links that you'd recommend me looking at just so I can get back up to date? Because I have Cursor, I have it running, but it's kind of one of those things. I have so many subscriptions, I want to limit it. How much is it a month? Like, 50 bucks a month?</Q>

**00:20:00 - Brandon Hancock**
<A>Oh, it's 20. Yeah, 20, you get 500 premium calls, unlimited cheap ones. So it's honestly a pretty good deal. And then for Gemini Pro Max, it's 5 cents per thing. So that one is getting more expensive. Yeah, 10 out of 10, would recommend it. As for resources, I need to do a video on that just because they have made a bunch of changes. You can use agents, you can ask, you can edit. There's so much going on, so I need to do that at some point.</A>

**00:26:07 - Sam**
Not a lot. I appreciate Jake's question because I was going to ask something similar about Cursor and Windsurf. I'm now going to share what you shouldn't do, but I'm using GitHub Copilot [tool:GitHub Copilot] and utilizing their bring-your-own-model feature. But I'm just connecting back on the free tier back to a resource that the company has within Azure [tool:Azure] because they're seriously concerned about data security, and it's a bit hard for me to get any leverage, so that was the best that I could do. And the funny thing is, even though I'm supplying my own model on the free tier, it still counts on their limits.

**00:26:57 - Brandon Hancock**
Out of curiosity, if you did — let me show you something really quick. If you inside Cursor did Models and if you brought your own Azure API key and set up your deployment information, I'd be very curious if you could then use some of the OpenAI models because you could in your own private Azure network that you control everything security-wise. If this would work for you, because then you're not really worried about rate limits. Might be a nice way to work around it because I know a lot of companies allow either Microsoft or AWS. Those are usually the two.

**00:28:23 - Bastian Venegas**
Inside Cursor, but not with the agent, I think. Or at least — because they don't charge you for those API calls, they limit the functionality. Or they used to.

**00:28:30 - Brandon Hancock**
<Q>Do you know what they limit, Bastian, out of curiosity? Is it strictly the agent feature?</Q>

**00:28:38 - Bastian Venegas**
<A>The agent features. The configuration you mentioned works, I've used it before, but at least the last time I checked, which was like a month ago, they didn't let you use the full agent feature. But you can use even O3 and O4 Mini — if you're on a startup plan and obviously you pay the plan, you can use pretty much every model.</A>

**00:29:11 - Brandon Hancock**
So I think what he's saying is you can't use the agent where it iterates over and over and over, but you can probably use Ask. Yeah, you can probably use Ask, which is like, hey, how would I do this? And it'll spit out the code, and it would probably just be up to you to copy and paste it in.

---

<!--SEGMENT
topic: GPT-4.1 Models and Prompt Engineering
speakers: Sam, Brandon Hancock, Bastian Venegas, Andrew Nanton
keywords: GPT-4.1, OpenAI, instruction following, million token context window, prompt organization, long context, prompt guide, structured output, Google Gemini
summary: Sam asks the group about their experience with OpenAI's GPT-4.1 models, particularly the claimed million-token context window. Brandon Hancock highlights improved instruction following as the standout improvement and references an OpenAI prompt guide shared by Andrew Nanton the previous week, which recommends repeating key instructions at both the beginning and end of long-context prompts.
-->

**00:29:36 - Sam**
<Q>Has anyone vibe-checked the GPT-4.1 models? Because I wanted to have a look at their million context window. I haven't been able to get access to it just because of work stuff. But I'm really interested to know how good they are over that million context they claim to have, and if they are any better than Google.</Q>

**00:30:01 - Brandon Hancock**
<A>So the main thing I'll mention is the biggest improvement I noticed, which they called out, was the instruction following. It actually is really good at like, hey, you need to do this, make sure you do this, and then it does it. Because I can't tell you the number of times I'll add into a model, like, please, dear God, stop doing this. And it's like, eh, I forgot, you know? So the GPT-4.1 [tool:GPT-4.1] is one of the first ones to where I clearly just say "important" and I have a bullet list of important things it should not do, and that it should do, and it actually follows. With that said, though, I haven't got to try it at the million token limit yet.</A>

**00:30:42 - Brandon Hancock**
But I did — I can't remember who brought it up last week. But OpenAI [tool:OpenAI] did drop their prompt guide. I can't remember if someone remembers who brought it up.

**00:30:49 - Bastian Venegas**
Andrew did.

**00:30:51 - Brandon Hancock**
But Andrew brought up an awesome resource last time. I'm going to drop it in the chat because it is very insightful. And the important thing Andrew showed last week, which was down at the bottom of this guide — yeah, so for instruction following, the main thing that's important once you get to longer phrases is — they said for best results, when you do get to that million token or just some of the higher ones, to put it at the beginning and end.

▶ **00:31:27 - Brandon Hancock**
Yeah. So prompt organization — they just recommend when you get long context windows to repeat some of the important instructions at the beginning and end. So just a quick point out of — because I would have never noticed that without reading this. So hopefully that's helpful.

---

<!--SEGMENT
topic: Lovable App for Civil Engineering Financial Modeling
speakers: Paul Miller, Brandon Hancock, Bastian Venegas
keywords: Lovable, Supabase, PostHog, civil engineering, land subdivision, infrastructure costs, New Zealand, SaaS, product analytics, funnel analytics, user behavior, session replay
summary: Paul Miller demonstrates a financial modeling web app built with Lovable for a civil engineer client, designed to help government economists and developers understand how various factors affect land subdivision section pricing in New Zealand. Brandon Hancock recommends PostHog for product analytics and user behavior tracking. The segment covers the build process (approximately 2.5 hours in Lovable), the workflow of using Claude/GPT to analyze a spreadsheet and generate a Lovable prompt, and plans to add Supabase authentication and usage analytics.
-->

**00:32:02 - Brandon Hancock**
Paul, you're up, my man. What's going on?

**00:32:05 - Paul Miller**
Well, I took the dive. You inspired me, Brandon, with your Lovable video, and I've been holding off and holding off. Basically, so I've got a client and he's a civil engineer, and he works with customers to look at land, like farmland, that is getting converted into subdivisions. So a lot of different factors go into that, and I've been working with him to lobby the government to make sure that we can better fund new infrastructure. Because when you build a subdivision, you've got to think about who's going to pay for the infrastructure?

**00:33:25 - Paul Miller**
So the scenario was this guy had a really good spreadsheet, but he said, oh, I'd take it through the spreadsheet. And people can play with that, but everyone knows how crappy spreadsheets are. So I thought, ah, this is what I could take through Lovable [tool:Lovable].

**00:33:45 - Paul Miller**
So before I turn it on — the use case is I'm a government economist that has no understanding of actual commercial obligations of if I go and change the cost of stuff, what's the influence on the section price for someone wanting to build a home?

**00:34:17 - Brandon Hancock**
Yep. Looks great. Dude, it kind of looks like Zillow-esque, like the little sidebar. I'm liking it.

**00:34:29 - Paul Miller**
Look, I need to do some UI/UX tweaks. But it's got a bit of work, but I'm getting some AI suggestions, and I just need to test it with the user. So one of the things that impacts the prices or impacts the equation — so the key thing for the user is what is the section price? This is New Zealand dollars, not US dollars for people freaking out. But it's what is the influence on what does the section price need to be if you change these other factors? So you start changing density from low to high, and you see all these other costs automatically start changing. You start changing the number of plots for the piece of land. You start adjusting the loan periods that influence interests. How much is the developer contributing, which again influences everything, external additional construction costs.

**00:36:00 - Paul Miller**
And then we've got some visualizations. This one down the bottom is a bit crap, but I need to tweak on that to try and make it easier for people to understand where the break-even point is. But we're hiding all of the specific details that make up the numbers below. So what's the interest rate? What's the land being purchased for? So keep that hidden out of the way, but all able to be changed for different parts of the library.

**00:36:38 - Brandon Hancock**
So this is sick. So I have a few questions for you. So tech-wise first, and then project implementation next. So you use Lovable. I'm guessing you had to go to the pro tier, right?

**00:37:00 - Paul Miller**
Look, I think the first challenge was when you're new at it, you're probably not as organized with getting efficient multiple things in one prompt. So you're going backwards and forwards. I like the version two, and I do note in your training video, you can go in and quickly edit stuff without putting that through the prompt. So I'm taking advantage of that and minimizing the number of edit trips. Because I didn't have immediate access to your GPT, which I've got now, so what I did was the client had a spreadsheet, which was the base kind of formula. So I took the spreadsheet, I put it through either OpenAI with one of their top models, or I took it through Claude [tool:Claude], and I got Claude or GPT to analyze the spreadsheet, derive all of the things that it was trying to do, and build a prompt description that then I copied into Lovable.

**00:38:16 - Brandon Hancock**
This is amazing. This is amazing.

**00:38:27 - Brandon Hancock**
<Q>Time — I know you say quick, but to get to this, what are we all in? Three, five, ten hours? How many hours to make this?</Q>

**00:38:35 - Paul Miller**
<A>Probably about six hours. But that's going to the client and saying, all right, give us feedback. Let's talk about this. Is that where you want it to be? And just going backwards and forwards. So a lot of that — that six hours isn't me sitting around Lovable trying to do it. But that's talking with the client. So it's probably Lovable time, maybe two and a half hours.</A>

**00:39:06 - Brandon Hancock**
Okay, a few other questions. Now, we have MVP up. I noticed there's a little login dude in the top right. Are you going to connect it to Supabase [tool:Supabase]? What's your game plan?

**00:39:20 - Paul Miller**
Yeah. So what I want to do is I want to connect it to Supabase. Because the guy doesn't want this — he wants to control who looks at it. And different people might be coming from different parts of the country where the base cost of land is different and the cost of building is different. And we need to be able to measure success. So for his clients, how many have used the tool? Which pages do they look at and what do they do with it? Because you kind of want to say, all right, I spent all this money and time building this for you, here's how much your clients are using it.

**00:40:21 - Brandon Hancock**
No, that's awesome. I want to share with you one thing super fast. Okay, so it's called PostHog [tool:PostHog]. So it sounds like your user wants to understand who you're building this for, what basically are user behaviors over time. And a tool like PostHog would be amazing for what you're trying to do for two reasons. One is for funnel analytics. So, like, it sounds like he has a bunch of people who are going to use it. So, like, of the people who signed in, how many of them filled out their profile, and then after that, how many of them went off and did their first search? So product analytics would be the first. And the other one that would be awesome is session replay.

▶ **00:41:53 - Brandon Hancock**
So over time, you can see like, okay, 60% of all search requests are on this one specific area. So you get to kind of look at like, oh, okay, this is a hot area. But then you can also look at like, oh, wait, out of 60% of those requests, they all came from a single user. So it's just like, oh, we have one power user who's skewing our data. Take him out. And yeah, so PostHog is what I would use as you get it built and want to add analytics. It's stupid cheap too. So yeah, 10 out of 10 recommend looking at this as well. It's like pennies.

**00:42:15 - Paul Miller**
I think using that for my main SaaS product would be quite good because it's always a challenge. It's like we've got all these customers using the SaaS service, but you don't know if they're fully using the tool and you kind of want to prompt them if they're not to say, hey, if you use that feature, that's going to give you this and give you that.

▶ **00:42:46 - Brandon Hancock**
Yeah, like I said, previous startups I've worked at — this is how we determined if we were going in the right direction, we used it to figure out if people were going to churn. The second you have analytics set up properly, my God, it's like you were blind to your app because you just knew people were on it, but how many, what were they doing? I don't know. So the second you get that implemented, it's night and day. So 10 out of 10 would recommend.

---

<!--SEGMENT
topic: MCP-Powered Chatbot with React Artifact Rendering
speakers: Bastian Venegas, Brandon Hancock
keywords: MCP, Model Context Protocol, Vercel, Next.js, React artifacts, streaming components, tool calls, ADK, A2A protocol, Grok, reasoning traces, debug panels, state management
summary: Bastian Venegas demonstrates a chatbot application forked from a Vercel template that connects to an MCP server with 11 tools covering internet access, research paper lookup, React artifact rendering, and medical case analysis. The UI renders React components inline or as side panels based on streamed tool call output. Brandon Hancock suggests exploring ADK as an alternative backend and references a highly recommended MCP crash course tutorial.
-->

**00:20:37 - Brandon Hancock**
All right, Bastian, you are up, my man. What projects have we been working on?

**00:20:43 - Bastian Venegas**
I'm working on a chatbot, so to speak, but it's more like an authentic chatbot because it's powered by the MCP server [tool:MCP] that I showed last week. So it has like 10 or 11 tools, and it's pretty cool because it renders — also renders.

**00:21:04 - Brandon Hancock**
Okay, so it's like a 30-second update on what you did.

**00:21:21 - Bastian Venegas**
Yeah, so give me a second. So I showed this last week in Claude Desktop and it has access through the MCP. But basically it's a bunch of tools that give access to internet, to researching papers, to some custom ways of thinking, basically prompts, hidden escape tools. And some stuff like to render React [tool:React] artifacts or streaming components directly into the UI. These are the 11 tools. It also optimizes the test sequence. It does some likelihood and probability calculations and stuff like that. So it's like a very specific product meant for people that work in health and need to research some clinical cases and stuff like that. And I am just porting all of the functionality to this thing I forked from Vercel [tool:Vercel] that also renders these artifacts. You can render them inline or you can render them as a side panel.

**00:22:31 - Bastian Venegas**
And for example, this is one of the custom tools — what's the weather in San Francisco and now in a graph bar, please. And this is like two different tool calls. And basically what the client detects is that it continuously parses the streamed answer. And when it detects that it's an artifact that it recognizes, it just renders it. So that's pretty cool.

**00:23:00 - Bastian Venegas**
And it also — so it can show you, like, if you use a reasoning model, it will show you the traces, depending on the model, but Grok [tool:Grok], it will show you the reasoning traces, so that's pretty fun. And something that I've found very useful is using debug panels so you don't rely completely on the console or the terminal because it gets crowded way too soon. So, like, basically, in Next.js or React apps, being able to trace your tool calls in detail and how the states are being passed, I found that pretty useful.

**00:23:48 - Brandon Hancock**
Okay, perfect. I also — you know, I'm on an ADK kick right now, so I would be very curious how easy it would be to recreate the 11-tool functionality inside of ADK, because I think you have one agent connected up to the MCP server, correct?

**00:24:07 - Bastian Venegas**
Yeah.

**00:24:09 - Brandon Hancock**
I would just be curious to see side by side how much you like the other one better.

**00:24:15 - Bastian Venegas**
I definitely want to check that out. And I think that they have this also a protocol like A2A [tool:A2A protocol] that you can actually connect the MCP to and should be easier to put it in their framework. So, yeah, that's definitely something I want to explore.

▶ **00:24:32 - Brandon Hancock**
Well, please keep us posted. You are currently our MCP resident expert. And for some of you guys who weren't around last week, I dropped a tutorial that Dave dropped — Albert — and I think it was probably one of the best MCP tutorials I've seen out there. So, just if you want some reading or some YouTube watching, it's an hour-long video, but he goes pretty deep into it. It's all Python, crash course. So yeah, definitely, if you are going into MCP, would definitely recommend checking that out.

**00:25:28 - Brandon Hancock**
That's the final thing on ADK. I really like that so far, because it comes with built-in state, which is so nice, because you can update the state before the agent call. After the agent call, the agent itself can update the state. Tools can update the state. Like, it was made with state in mind, which is pretty nice, because without state management, you have to do it yourself. And then it can get very complicated on how do you want things to interact with it.

**00:25:56 - Bastian Venegas**
Yeah. Doing anything React particularly sucks.

---

<!--SEGMENT
topic: Agentic Enterprise Architecture and Framework Selection
speakers: Sagar Passi, Brandon Hancock, Bastian Venegas
keywords: ADK, Crew AI Enterprise, agentic teams, orchestration, sequential agents, loop agents, parallel agents, MCP, SharePoint, financial services, governance, root agent, delegation, UK enterprise
summary: Sagar Passi asks for architectural guidance on deploying agentic teams for UK financial services clients, covering orchestration patterns, governance, and tool connectivity. Brandon Hancock compares Crew AI Enterprise (better for deep-pocketed clients needing on-premise, permissions, and tracing) versus ADK (better for rapid iteration and affordable deployment at $0.11/hour). He explains ADK's root agent delegation model and recommends starting with direct tool calls before adopting MCP for cross-repository tool sharing.
-->

**00:43:41 - Sagar Passi**
Doing well. How is everyone? Paul, that was amazing at the UI. Really impressed. I've been away from this group for a couple of weeks. I finally got my head — I went down the rabbit hole. And I'm getting pushed from a lot of companies in the UK on how do we implement it. So I'm here for advice from you guys on how would you recommend all the new technologies coming out there? How would you do agentic teams? What is the architecture? How do I keep this safe from a governance point of view?

**00:44:25 - Brandon Hancock**
<Q>Okay, so I'm going to ask a few quick questions. So when you say agentic teams, you are referring to — I am an organization and a business. Let's just say I'm the marketing team. And now I want help in order to manage LinkedIn posts. I want help — basically having the co-pilot through agentic apps to help out everyone on the internal team. Like that's what we're talking about.</Q>

**00:44:53 - Sagar Passi**
<A>Yep. Yep. So operations, mainly in the financial services, reinsurance, that kind of market.</A>

**00:45:00 - Brandon Hancock**
Okay. So, all right, so I'm going to give you two branches really quickly. So, if your customers have deeper pockets, I would have really explored Crew AI Enterprise [tool:Crew AI Enterprise] for a few reasons. One, they have — at least they're going down this path, I'm not sure if it's fully built in yet — but there is the ability to set up permissions and authentication around agents, which is huge. Tracing is also built in, it's very easy to track, and then outside of that, some places like on-premise solutions, and they have a factory installation. So, like, if you're working with big clients that are like, hey, I'm minimum trying to spend $20,000, $30,000 plus more, there are some factory solutions that I would look at exploring. It is more pricey — very pricey — but the data never leaves the building, and they get the benefit of agentic applications.

**00:46:08 - Brandon Hancock**
Okay, now, so that is enterprise side. For the average developer, I'm getting hyper bullish on Agent Development Kit [tool:ADK]. I really like a lot of what they're doing, specifically around pricing. It is wild how affordable it is to now build agent teams. So, time you deploy an agent, it's like 11 cents per hour per run. And that's just at runtime. So if it's up for 30 minutes and it dies, cool, you paid a nickel. You know, obviously you're paying for tokens, but like, it's dirt cheap. Like, there's no other framework that is that cheap right now for deployed agents. So, yeah, Crew is session-based, so it's somewhere around 40–50 bucks a month. And you can run up to three or five agents or crews, which is like 100X of what Google's charging. It's just hard to compete against Google because they're not making money off agents. They're making money off YouTube and search. So they're just undercutting what everyone else can do.

**00:47:21 - Brandon Hancock**
Okay, a few other things I think you would really like. One thing I have fallen in love with ADK recently is their chat functionality. Meaning you can quickly spin up agents without a UI or anything else and just give people a chat-like interface like you would do with ChatGPT [tool:ChatGPT]. Except behind the scenes, there's some hardcore agents accessing internal data, doing whatever they need to do to deliver results. And people can just chat with it like they're chatting with ChatGPT.

▶ **00:47:51 - Brandon Hancock**
Super valuable for MVPs because, yes, later on you can go off and add all the nice UI elements and get everything pretty. But for a quick MVP, that chat functionality is a game changer.

**00:48:11 - Sagar Passi**
<Q>With Crew AI or any agentic framework, how do you guys do the orchestration? You know, if I do a parallel flow or I do a team flow or a prompt chaining flow, how can I choose that dynamically with what tasks are happening?</Q>

**00:48:28 - Brandon Hancock**
<A>Okay, so they have inside of ADK a super nice feature. So they have workflow agents, and there are different types. So there are sequential agents, which are, hey, every time I call this agent, I want it to do these specific things — like task A, B, C. And then for other things, a loop agent is like what we were talking about earlier. And then parallel agents is like go off and do work at the same time. Now, to further answer your question — you were saying like, hey, how do I pick which workflow to go down? What you could do is you basically inside of ADK create a root agent and then under a root agent, you can give it multiple types of agents. So you could give a root agent, which is like, hey, your job is to always delegate tasks to everyone else. And if it's a sequential task, you could pass in a sequential agent. Or you could give it to another sub-agent group, which is a loop agent.</A>

**00:51:15 - Brandon Hancock**
Crew right now is always sequential. Unless you go to a flow, then you can get crazy. But I liked how easy it was just to say sequential agent, loop agent, parallel agent. I thought it was a pretty nice trick that ADK did.

**00:51:55 - Sagar Passi**
<Q>For all of these determined workflows, do I need to define the agent's force? These workflows — can I pick them dynamically depending on the goal?</Q>

**00:52:44 - Sagar Passi**
More like, let's say I'm in operations in a bank and then I say I need to find quarter-end reporting. My expectation would be that it would go to the finance agent, that agent would talk to the data agent to pull it from SharePoint [tool:SharePoint], for example, that would run its task in the background. Then if I say, make this record or download this document or something like that, that's another agent that's fetching it. And it's figuring out what the path is like a human would. That's my expectation from an agentic team.

**00:53:22 - Brandon Hancock**
So that's exactly what Agent Development Kit does. So like every agent comes with its own description and — under the hood, Agent Development Kit, every time it gets a call, it looks at all sub-agents that it has access to, and it goes, who would be the best to fill this job? So it feels very much like a manager. So it always looks to see who's the best one to do this job and delegates it to them.

**00:53:33 - Sagar Passi**
<Q>And then just as people want to do this, what would you recommend for connecting to these services like SharePoint? Is MCP the right way to go? Is that the standard that you would recommend?</Q>

**00:53:46 - Brandon Hancock**
<A>Okay, so the simple answer with just getting this up and running — the answer is no. Like to get it working, to start, no. Just doing a direct tool call is the easiest way to go. However, once you build up a few different agentic teams — so, like, let's say you have one marketing department agent, within that there's literally 30 agents — well, they can, that's all in one repository, so you're sharing all the code, all the tools, super easy. Now, let's say you go over to the finance department, and you make them 30 other agents. Well, now, there's probably a lot of shared tools that you want to use between the marketing agents and the finance agents, and that is at the point where sharing becomes nice. But for V1, dude, it's all in one repository, just keep it there. It's the second you get to two separate repositories where you need to share code, that's where you probably want to start looking at MCP.</A>

**00:55:28 - Sagar Passi**
<Q>So the recommendation is Agent Development Kit, not Crew AI Enterprise?</Q>

**00:55:36 - Brandon Hancock**
<A>I mean, I'd have to learn a little bit more about the customer and their needs. I mean, I'm happy to follow up on a separate call if you want to later this week to maybe give some more answers. But you could go either way. I would just need to know a little bit more about their use cases to be like, if that's a requirement, I could just go and tell you, yeah, this tool will not work or yes, this tool will work.</A>

**00:56:05 - Brandon Hancock**
Sebastian asks, is their chat feature part of open source ADK, or is it a feature of their cloud? So they actually have a nice little quick start, Bastian, where in their quick start guide, they just show you how to also easily deploy a nice front end in front of ADK.

**00:57:44 - Brandon Hancock**
Yeah, so you can see here, Bastian — I'll drop this link in the chat. But long story short, you can see they actually build a UI in front of their agents that allows you to turn ADK into an API, which is basically what you want.

**00:58:04 - Bastian Venegas**
Yeah, that's a major difference compared to Crew. I agree.

▶ **00:58:08 - Brandon Hancock**
Yeah, I will say I'm really loving ADK for how quickly it is to put it inside of another front end. Because with Crew AI, it is your job to then create wrappers around everything. And so that's — I don't like, you're forced to do enterprise, basically, for certain things, which is fine if you're going to go down that route. But if you're not, and you just want to test rapidly, ADK is really nice for rapid iteration.

**00:58:53 - Sagar Passi**
Also, I'm going to an AWS event tomorrow. So, if anyone has any questions for me to ask, I'm happy to feed back to this group. Just message me.

---

<!--SEGMENT
topic: AI Video and Audio Generation Pipeline
speakers: Richard Collier, Brandon Hancock, Jake Maymar, Bastian Venegas
keywords: Flux, ElevenLabs, OpenAI TTS, FFmpeg, B-roll, Facebook ads, audiobook, voice synthesis, cartoon animation, Gemini, structured output, reinforcement learning, thumbs up/down feedback, VLM, faceless YouTube
summary: Richard Collier demonstrates two AI-generated media projects: a cartoon-style Facebook ad pipeline using Flux for images and ElevenLabs with a custom low-stability voice for animated narration, and a multi-voice audiobook system using OpenAI's text-to-speech model with character-specific voice instructions and FFmpeg audio stitching. Brandon Hancock suggests using Gemini for video analysis to automate sound effect placement. Jake Maymar proposes a thumbs-up/thumbs-down feedback loop to improve image generation quality over time.
-->

**00:59:28 - Richard Collier**
Hey, how's it going today, man? Just a couple of calls. Like I said, I had some personal issues, but I was working on a few things. Can you see my screen?

**00:59:55 - Brandon Hancock**
I see someone drinking a smoothie.

**01:00:00 - Richard Collier**
So I've been kind of working on the B-roll agent for running little Facebook ads and stuff like that. And so I have it create these really crazy scripts and then I started using cartoons because it was a lot easier for Flux [tool:Flux] to draw them and then it didn't have to be so realistic. So I started using cartoons and I do have to do some post-editing, but I get a pretty good video right off the bat.

**01:00:35 - Richard Collier**
So I'll just play a little bit of this.

**01:00:42 - Brandon Hancock**
*"I'm tired of breakfast shakes that taste like lawn clippings and disappointment?"*

**01:00:47 - Richard Collier**
Yeah, me too. *"Check out Vast Thread Superfood, basically your morning smoothie's badass older sibling who rides a motorcycle and actually gets results. It's packed with more antioxidants than your mom's Pinterest board..."*

**01:01:08 - Richard Collier**
Yeah, so, you know, it's pretty good. Obviously, the tools are getting a lot better, so that's helping out a lot. But, yeah, I can pretty much get an ad up and running really quickly, have a really decent script. I do need to go in and kind of tweak the script to make it a lot better sometimes. But, I mean, for the most part, I'm about getting something 60% done, and then I take it in post and make it a little bit better. And, of course, I'll add transitions. I'll add sound effects and things of that nature to really polish this up into something usable for a Facebook ad.

**01:01:57 - Richard Collier**
And this other project has been a project I've been working on where I'm taking audiobooks or words and then turning them into audiobooks where you get a different voice for each character. It's using a schema, and I'm also using OpenAI's new text-to-speech model [tool:OpenAI TTS], and it's actually pretty good and not as many voices as ElevenLabs [tool:ElevenLabs], but still pretty good.

**01:02:27 - Richard Collier**
*"Buildings loom like skeletons, half-collapsed and covered in rust. Cold wind howls through broken windows. A groan echoes down the alley as a battered loudspeaker crackles to life. Sustenance and Stratton commencing. Sector 9C, line up. One per household. Tampering is punishable by purging. Dozens of unwanted, line up."*

**01:02:50 - Richard Collier**
So, it will switch voices. It will read the script all in different voices, and it will also pass different instructions. So the voices are slightly different because there's not a lot of voices. So I'm able to say, hey, this person talks with a higher pitch, or this person talks lower, or they have a southern accent or something like that. And I'm able to pass in all of these parameters. And it's pretty cheap to do this. It's only like maybe a dollar to get it to do this. This is act one of an entire series. And it's an hour and 34 minutes. And I have script parsers in here. I have the audio stitching for FFmpeg [tool:FFmpeg], where it's going to label all the voices in order. It's going to put it all together into one thing.

**01:04:06 - Brandon Hancock**
Dude, you're underselling this. This is freaking awesome. I know you've been putting in the work on this, and it is amazing.

**01:04:14 - Jake Maymar**
<Q>I was curious, can you do emotions?</Q>

**01:04:17 - Richard Collier**
<A>Yeah, so with the OpenAI, it won't always follow it, but there is an instructions parameter that you can pass in. And you can go, you know, with grief or very excited or something like that. And so it will try and match those emotions. But yes, to answer your question, yeah, there is emotion there as well.</A>

**01:04:51 - Brandon Hancock**
<Q>So for images, what was your go-to image generating tool?</Q>

**01:05:00 - Richard Collier**
<A>Flux. I'm using Flux.</A>

**01:05:11 - Brandon Hancock**
<Q>And then for audio on the other one, is it also OpenAI or is it ElevenLabs for the other one?</Q>

**01:05:19 - Richard Collier**
<A>I'm using ElevenLabs and I'm using a custom voice with crazy low stability on there so that it's so animated. It's a custom voice that over-pronounces words and makes everything just kind of weird, but it's there to just grab attention. So it's a custom voice with very low stability as the setting.</A>

**01:05:44 - Brandon Hancock**
Dude, great pattern interrupt.

**01:08:16 - Brandon Hancock**
Few ideas for just to help get this as close to 99%, 100% as possible. So, okay, so for sound effects. So in my mind, I'm like, what is a sound effect? It is something's happening on the screen at a specific time that we need to add in some, like a whoosh, a something, you know? So what would be pretty cool is in Gemini [tool:Gemini], what you can do is you can upload pretty big videos now. And you could potentially, if there's like 20, 30, 100 different sound effects that you have in a library, what you could do is say, hey, please watch this video. And what I would like for you to do is spit out a bulleted list, a time-series bulleted list of when I should include different sound effects.

▶ **01:09:15 - Brandon Hancock**
I know I would go to AIStudio.Google.com [link:aistudio.google.com]. That's what I would look at doing just strictly because you could do structured output. And I think that's something you'll need, where you just say, like, I want an array of time and audio clip. Like you could define that as the structure.

**01:10:05 - Richard Collier**
Okay, sounds good because ElevenLabs creates sound effects as well. So I thought about seeing if they were in the API and if they would be able to handle putting in sound effects where they made sense.

**01:10:34 - Brandon Hancock**
<Q>So, dude, end goal. You become the master expert of all things video and audio clips for AI. What are we doing, man? This is such a cool skill that, like, 0.00001% of the world has. How are we going to capitalize on this? What are we thinking?</Q>

**01:10:52 - Richard Collier**
<A>So right now I'm actually writing a short story. And I was going to do a whole video and kind of use this to bring out the short story and just kind of, you know, perhaps just start like a YouTube channel of just short stories that people can watch either while they drive or when they're home doing nothing. And there'll be like maybe 10, 15 scenes. And I was thinking about maybe generating audio and video and music tracks to kind of go with it. And then, you know, if it seems like it can handle stuff like that, then maybe I'll do something like what Paul did — maybe I'll do like some kind of SaaS or something like that. Because I think the only other people in the game right now for this is InVideo and they are crazy expensive.</A>

▶ **01:13:00 - Brandon Hancock**
What's more on marketing material, that's a very specialized, focused niche that would crush it. So the AI guy, his school community — he currently has 600 people in his community, 75 bucks a month. So like, you know, what is that — 45K a month. Wild. So absolutely stupid. So that's the second channel I would 10 out of 10 recommend looking at as well because it's very — he's all about making money with faceless YouTube channels, but yours would be more product-driven and more people have more money because it's a business buying it rather than an individual.

**01:14:25 - Jake Maymar**
<Q>Would it make sense to add like a reinforcement learning loop, since you understand what the end video should be, and you said it does 60%, but then you do a lot of manual work? Would it make sense to record the manual work you do, basically build a Python or some other tool to sort of record that manual work? And that way, at least you're training the system with the right data.</Q>

**01:14:53 - Richard Collier**
<A>I've been asking about it. I've been talking with GPT about it. And it says that it's absolutely possible. I have definitely been talking about it with Supabase [tool:Supabase] and trying to get something where I'm giving it a thumbs-up, thumbs-down type system and also telling it what's wrong and things of that nature. And it does say that it is possible.</A>

**01:16:27 - Jake Maymar**
I found — because I was — so I built those into all my systems. I found the fastest way to do it is a thumbs down, thumbs up, and you just do the thumbs — so when you get the image you don't like, you just thumbs down it and it just stores it. That's it. And you can put like a couple of descriptions of what didn't work about it. And then the other thing is when you get a clip that works, then that becomes basically a few-shot, right? So that becomes the prompt that you're going to use. Maybe for a VLM [tool:VLM] instead of a large language model. But the thing is, if you just do a simple thumbs down, thumbs up, that might get you closer to where you want to be without having to do all this insane, complicated systems.

---

<!--SEGMENT
topic: Expert Witness SaaS Product Testing and Loom for Documentation
speakers: Andrew Nanton, Brandon Hancock, Bastian Venegas
keywords: expert witness, forensic psychiatry, beta testing, Loom, Screen Studio, sensitive data, Gaussian blur, N8N, onboarding, product testing, documentation, video recording
summary: Andrew Nanton provides an update on a SaaS product for expert witnesses being developed with a partner, approaching initial beta testing with a small pool of tech-savvy forensic psychiatrists. Brandon Hancock advises pre-seeding the product for testers to focus feedback on the core loop rather than onboarding. The group discusses tools for recording screen walkthroughs with sensitive data redaction, landing on Screen Studio's mask/sensitive data feature as the best option for testers on Mac.
-->

**01:17:30 - Brandon Hancock**
All right. Next up, Andrew, what's going on?

**01:17:34 - Andrew Nanton**
Oh, hey, everyone. So I sent you a quick note. I don't really have any updates. I've just been doing day job. Had an interesting trial I testified in, but that has been what I've been up to. So I'm mostly just here to listen and think about happier things than my day job provides.

**01:17:59 - Brandon Hancock**
<Q>Any fun things coming up then on the horizon?</Q>

**01:18:03 - Andrew Nanton**
<A>You know, we're just still turning the wheel. Maxim and I are getting ready to open up for testing on this thing that we're working on, you know, this product for expert witnesses. And, you know, what I think is a little bit different about this is that we're — in order to ask busy professionals to test stuff, it really has to be pretty much ready for them to spend time on it. And it's just a different scenario. So, hopefully this is not a lot of time and energy misspent, but it's looking good. So I'm hoping, and once we are ready for testing and have something to show, I'm excited to show it to you all. But, yeah, I mean, all the parts and pieces are there. It's a bit like a bag of Legos at this point. I mean, they're snapping together slowly but surely, but there's not much to see.</A>

**01:18:55 - Brandon Hancock**
<Q>So is it just your network who you're just reaching out to, like friends? Or is this more cold outreach and just like, hey, we're building this cool thing?</Q>

**01:19:13 - Andrew Nanton**
<A>Yeah, yeah. At this point, it is people that I know, so I'm starting with a pretty small pool of people that I, one, can count on to have sufficient tech savvy that they're not going to freak out if they hit a 404. And maybe are tech-savvy enough to use something like Loom [tool:Loom] or some equivalent — like, hey, if you're getting something weird, can you just show me what it is? And we'll try to iron it out. And the number of people who do that and are forensic psychiatrists is — I can count them on one hand. So, yeah, that's where we're starting. And then I'm hoping that that will just be maybe a couple of weeks of testing and then we can roll it out to more like 10 or 15 people who are a little bit more mixed, probably with a fair amount of hand-holding and training about, here's how you use this thing.</A>

▶ **01:20:11 - Brandon Hancock**
I'm not sure what onboarding looks like for the product, but just a heads up — the more for those first initial users that you can auto-preload, even if it's a manual, like, hey, we seeded your entire thing for you, just so you just click in — just for those first initial users to make it as easy as possible. That's something I've seen done to make it easier, especially in more high-friction testing. You don't want them to be ranking the onboarding experience, you want them to be rating the core loop, if that makes sense. So, you know, onboarding is once we're scaling. Let's get the core thing working first.

**01:21:07 - Andrew Nanton**
And just real quick to respond to Bastian's idea about me recording some stuff — how to do things that I can send to people. I think that's a great idea. And actually, I'm trying to remember what podcast I was listening to the other day, but there was a woman who was saying she does, she builds automations in N8N [tool:N8N] for people. And she was saying she has a script set up where she records the workflow of what every step of the N8N workflow does in, and she records that in something like Loom, sends that audio and video of her describing and the images, and has that basically transcribed into a series of screenshots and descriptions — both for her and for the client she's creating it for. And I thought that was a pretty brilliant idea — you know, just record you talking through it once, and then you have not only a video, but if you prompt it right, you could have a written documentation as well, or at least an 80% start on it.

**01:22:20 - Bastian Venegas**
Yeah, in fact, today I used the feedback that Brandon sent me for a script of a video, and this is my script, this is my feedback, it works really great.

**01:22:31 - Brandon Hancock**
Loom is such a cheat code, especially Loom AI features. I don't know how I would do life without Loom. It would take 10 times as long to do everything.

**01:22:49 - Andrew Nanton**
<Q>If I can ask one quick follow-up question on that. So, some of the data that I'm hoping people will be working with when they start working with real data will be protected information. And I saw that Loom has an option where you can blur out, but it only works with the Chrome plugin, and you can only basically blur out CSS elements. Like you can't just select, blur out this portion of my capture. Does anyone know of a tool that will just let you sort of drag and select, say, you know, block out these areas? So if people are dealing with sensitive data, they can show me the behavior, but not necessarily show me their data.</Q>

**01:23:27 - Brandon Hancock**
<A>So the only thing I could think of, just a quick suggestion, is if they are on a Mac, there's Screen Studio [tool:Screen Studio]. So you can record your screen. It feels kind of like Loom. And you can go back, I believe, and just add in blocks. So like they could just physically add a block over it. It's manual. They're the ones having to do it. But the good thing about Screen Studio is it's all local on your computer until you export the final MP4. So because like with Loom, it's instant upload, which is, I think, not what they want.</A>

**01:24:29 - Bastian Venegas**
Just a quick comment, if you needed to build this, you could use Gaussian Blur [tool:Gaussian Blur], that's what they usually use to do this blurring of images, and you could detect what timestamp is the thing and just apply it to those frames. I'm sure you could do it with FFmpeg and Gaussian Blur.

**01:25:15 - Brandon Hancock**
Oh, my gosh. They have a sensitive data field. Let me share my screen. Yeah, so there's Screen Studio. When you go to — oh, mask. Yeah, you got a mask. And then what do you want to do? Do you want to highlight something or it's sensitive data? Yeah. And then you just do that. And then you can just adjust the timeline down here. So like, so you can just play it. So it's blocked, it's unblocked.

▶ **01:26:12 - Andrew Nanton**
Okay, well, yeah. I mean, any of my testers who are on a Mac, I will probably be springing to buy them a copy.

**01:26:24 - Brandon Hancock**
Yeah, they have a trial. So, I mean, they could all probably do it on the trial without having to go off and pay.

---

<!--SEGMENT
topic: WhatsApp Message Mediation App Refactor
speakers: Michal Simko, Brandon Hancock, Jake Maymar, Bastian Venegas
keywords: WhatsApp, Twilio, Next.js, OpenAI API, Vercel AI SDK, Supabase, message classification, LLM routing, structured output, modular architecture, state management, deployment, join key, co-parenting
summary: Michal Simko demonstrates a refactored WhatsApp message mediation app that classifies incoming messages as pass, rephrase, comment, or block — filtering hostile language between co-parents before forwarding. Brandon Hancock recommends splitting the single large prompt into a two-step LLM pipeline (router + specialist), switching to the Vercel AI SDK for Next.js-native API calls, and testing deployment to Vercel early to catch timeout and stateless environment issues. The segment also covers database pairing logic for connecting two phone numbers via a join key.
-->

**01:26:39 - Brandon Hancock**
All right. Michael, you are up next, man. What's going on? What fun stuff?

**01:26:43 - Michal Simko**
Hey, what's up? So, I took your advice from last week and started refactoring towards a more modular kind of approach, which took me definitely longer than I was hoping. But let me share my screen so I can show you.

**01:27:07 - Brandon Hancock**
<Q>Questions on the refactor though. Did it make sense as you were doing it?</Q>

**01:27:10 - Michal Simko**
<A>It did. Like, it was — at first when you started speaking, I was like, what does it mean? And then obviously it's one of those things that once it clicks, then it clicks. And when you were drawing it out, then it made sense. And then also when I was building it, it became even more clear. Because then you kind of understand why.</A>

**01:27:55 - Jake Maymar**
<Q>So super quick. How are you doing the refactoring? Is there like a — are you doing it through Claude or something like that, or are you doing it manually?</Q>

**01:28:09 - Michal Simko**
<A>No, I was actually doing it manually, but I did help — I mean, I built some scripts to do some of the really bigger updates. Yeah, so it was a mixture, but I'm not using Cline, I'm intending to start using Cline on this one, but for now it's been manual.</A>

**01:29:00 - Brandon Hancock**
Quick follow-up though — if he had wanted to do the refactor inside of Cursor, the easiest way he could have done it is to say, here is my current file, here's what's wrong with it. Such as, currently everything is coupled together, and I would like to decouple it. And then that little drawing I did, Michael — you could have said, here's what I'm looking to do, to where I have two abstracted files on top, one for the web, one for texting, and they sit on top of the messaging service. And it probably could have done 80% of it.

**01:29:44 - Michal Simko**
So, if I took as well the route that you told me to kind of go more the mega prompt. So I have now different — well, let me actually show the functionalities. So, hi, I'm Peter. All right, Peter, what's your name? So it starts recognizing whether this is a message to the API or whether this is something that should be — hi, how are you? So we kind of recognize the chit-chat, tell him he is an idiot, and then he will go like, oh, no, I'm going to block this. So basically I created these classic — or, you know, I can say, okay, I can pick up the kids tomorrow. It will then go, okay, well, that looks fine. And then it will forward the message to the other person, right?

**01:31:43 - Michal Simko**
Yeah, it's really true, you know, so I have, like, for instance, a rephrase. So I have either a pass, if it's clear enough and it has the logistic organization information, it will pass the message to the other person. If let's say part of the question or the text is a bit rude or has to be rephrased, it would rephrase it. So there would be, let's say — she really is useless to pick him up tomorrow. It would — okay — so it says rephrase, and then here's the clear version, and then it would say, can you pick him up tomorrow? So it would have a filter to pass on the message in a more — 

**01:32:47 - Brandon Hancock**
Dude, this is awesome. What's so funny is someone's gonna get used to talking like that, and then they're gonna text regularly, and be like, oh my god, I thought it would make it nicer.

**01:33:00 - Michal Simko**
The whole idea is — I mean, this is supposed to work over WhatsApp [tool:WhatsApp], right? So really, the next step is to get it into WhatsApp and then also audio, right? So I have already implemented the audio — the voice to text. But for now on this UI, it's only doing that. So it can rephrase or it can comment or it can block or just directly reply.

**01:33:41 - Brandon Hancock**
<Q>So on the — so I see this as the prompt. Now, when you pass it to the LLM, are you doing a structured output to be like, to showcase, oh, it was a — the action was block and here is the message?</Q>

**01:34:01 - Michal Simko**
<A>Yeah, this is what I get in the log for now. It's a JSON.</A>

**01:34:13 - Brandon Hancock**
Yeah, so the thing is, because I was looking at your prompt, and it said at the very end — at the end, it was giving it example JSON outputs, right? Yeah, you mean the action? Yeah, yeah, yeah.

**01:34:25 - Michal Simko**
I'm struggling with this one, I have to say, with the direct reply, because it cannot distinguish whether it's like a chit-chat — you just saying, hi, I'm Peter, how are you doing, whatever. Sometimes it would then think it's an okay message, and it would pass it along to the other user. And so I had to kind of give it more examples. But to be honest with you, this is a phase where I'm now at — meaning I would like to understand better how I could structure this prompt better to then also be able to more easily expand it with having other scenarios.

▶ **01:35:18 - Brandon Hancock**
So what's happening right now is like we're in programming to where it's like, okay, like, I have one Python file that's getting huge. So, like, what do I usually do when it happens? Like, you do a refactor. So, in your case, what I see whenever I'm looking at this is two things. I see a classification, and then I see a response instructions. So, if you wanted to, you could break this up into two separate LLM calls. A router, and the router will return: pass, rephrase, comment, block. The whole job of the first LLM is to determine what type of prompt this is. Then, from there, whatever you get as the output, it then gets sent over to a second LLM call, who's a specialist in responding in that format. So that is how you can break it up.

**01:36:15 - Michal Simko**
I had it like that before. But it was doing the classification inside of the code, and then I was passing it to the LLM. It was all these ifs and whatnot. It was getting too long. But then I joined it, and next step would be to separate it again.

**01:36:41 - Brandon Hancock**
Otherwise, this is going to become humongous. And the cool part is, when you split it up like that, each sub-prompt is now going to be great. Like, you could add way more in there.

**01:37:00 - Brandon Hancock**
<Q>And the only other thing — okay, what are you using for your AI library? What are we using? Are you using the AI SDK? Or what are we using to make LLM calls?</Q>

**01:37:12 - Michal Simko**
<A>LLM calls — I'm using my OpenAI API.</A>

**01:37:26 - Brandon Hancock**
Okay, yeah, I was — sorry, the thing I was curious is, inside of a Next.js application, you can use — it's called the AI SDK [tool:Vercel AI SDK], and that's what I was curious if that's what you were using to make all these requests.

**01:37:44 - Brandon Hancock**
<Q>Okay. So, well, are you — follow-up question — is all of this running in the front end or the back end?</Q>

**01:37:56 - Michal Simko**
<A>Yeah, it's on the back end.</A>

▶ **01:38:11 - Brandon Hancock**
Have you tried deploying this by chance to Vercel? The reason why is just like sometimes things work locally on your AI applications, and then you'll go to deploy it to the cloud, and it's a different beast, because locally things can run forever, but then when you deploy to Vercel to where things are stateless and purely in the cloud and have timeouts, things can hit limits. So before going too much further, you might want to do a quick deployment test and just see if you're hitting any issues. Just because I don't — if you're planning on deploying this, you might want now at the time to test deployment, rather than going super far down the road, and then be like, oh, my God, I have 200,000 lines of code. I'd much rather have it fixed when I was at 10.

**01:39:16 - Brandon Hancock**
And yeah, Vercel AI SDK — Bastian also agrees — is the way to make requests, especially if you're going to be deploying this. It's super similar to what you're already doing with making calls and everything. It's just the Next.js approved approach.

**01:39:45 - Michal Simko**
And then the next steps would be implementing the database and the memory and whatnot. Because once you're on Twilio [tool:Twilio], you just — I will have to have a way that one message sends a pairing request to another number, which then goes, I accept, because I have to then connect them somehow.

**01:40:22 - Brandon Hancock**
There's a name for this. Why can't I remember it? It's not a join key. Does anyone remember off the top of your head when you combine two IDs together with an underscore? What's the database term for that?

**01:40:35 - Brandon Hancock**
Yeah, that's what you're trying to do. Basically, like, you would have a conversations table, and a conversation at the high level is nothing more than a pairing of user one and user two. So, you would have user one ID underscore user two. Like, that's how you could look up all active conversations.

**01:41:23 - Michal Simko**
Yeah, it's a join key. Okay.

---

<!--SEGMENT
topic: Closing Updates and ADK Masterclass Preview
speakers: Brandon Hancock, AbdulShakur Abdullah, Michal Simko, Fernando Lopes Jr.
keywords: ADK Masterclass, crash course, recording, real-world examples, tutorials, community, DM, weekly cadence, content roadmap, agent automation
summary: Brandon Hancock wraps up the session with housekeeping notes, directing members to use the school community DMs for follow-up since the meeting chat disappears. He previews the upcoming ADK Masterclass (V3, simplified, recording starting the next day, targeting Friday/Saturday release) and announces a content pivot toward real-world agent automation examples rather than high-level framework tutorials.
-->

**01:42:00 - Brandon Hancock**
The progress you guys keep chugging along. Okay, perfect. I owe some of you guys some messages. I was going to send Sagar a message. Abdul, I saw you were sending some messages. If you want to just shoot me a DM in school, that's probably the best way, just because the chat here disappears.

**01:42:20 - Brandon Hancock**
Quick update for what you guys can expect throughout the rest of the week. So the ADK Masterclass [tool:ADK], it's taken longer to build, but it's good news, though. Because it took longer because I simplified things multiple times. So it's much easier to use. Like, V3 is what I'm at right now, and it's so much easier to use than what it used to be. So very excited for that to come out. We'll start recording tomorrow. I'm recording all tomorrow, all Thursday. So hopefully out by Friday, maybe Saturday at this point.

▶ **01:42:56 - Brandon Hancock**
And then outside of that, I'm going to be focusing next on a lot more just examples. So that's going after this is done. I just want to focus on as many real-world example tutorials as possible with ADK and other tools, so that's what I'll be dropping next. So moving a little bit away from the high-level tutorials and just like, I automated this for business, I automated this for business, just because I'm not seeing that much developer real-world agent stuff out there. So I think that will be a cool way to shine and give you guys some more ideas and examples that you guys can just grab for free too.

**01:43:28 - Brandon Hancock**
So, yeah, y'all are awesome. It was all — love, love Tuesdays, best day of the week. Good to see you guys. But yeah, please keep me posted on your projects and y'all crushed it and can't wait to see y'all next week, okay?

**01:43:41 - AbdulShakur Abdullah**
All right, buddy.

**01:43:42 - Brandon Hancock**
Have a good day.

**01:43:44 - Michal Simko**
Good night.

**01:43:45 - Brandon Hancock**
See you guys. Bye.

**01:43:46 - Fernando Lopes Jr.**
Thank you.

---

=== UNRESOLVED SPEAKERS ===
- Sam (last name unknown — appears as "Sam" throughout; no alias map entry found)
- Fernando Lopes Jr. (speaks only one word at close; no alias map entry confirmed)