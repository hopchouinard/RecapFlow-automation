=== SESSION ===
date: Not explicitly stated (weekday evening session)
duration_estimate: ~2 hours 25 minutes
main_themes: N8N automation workflows, vibe coding in corporate environments, ShipKit course launch, ADK/LangChain agent development, Supabase/authentication best practices, GPU inference infrastructure, Topic Launch platform, job searching in AI field

---

<!--SEGMENT
topic: Session Opening and N8N Exploration
speakers: Patrick Chouinard, Marc Juretus, Paul Miller
keywords: N8N, Railway, webhooks, Google Drive, LangChain, Next.js, Digital Ocean, Postgres, automation, deployment
summary: The session opens with informal chat before Brandon joins. Marc shares his experience spending 6–8 hours learning N8N, deploying it to Railway, and building webhook-driven automations including a Google Drive trigger that generates AI-personalized emails. Paul discusses hosting N8N on Digital Ocean for a flat $20/month. The segment establishes N8N as a powerful rapid-prototyping tool for non-complex client work.
-->

00:01:12 - Patrick Chouinard
Hi, Marc.

00:01:33 - Marc Juretus
Hey, Patrick.

00:01:34 - Marc Juretus
Sorry, man. I was in another window.

00:01:36 - Patrick Chouinard
No issues.

00:01:38 - Patrick Chouinard
How are you doing?

00:01:40 - Patrick Chouinard
Good, good. I have some questions for the group tonight for once.

00:01:48 - Marc Juretus
That and some light humor here and there.

00:01:53 - Paul Miller
Or especially when a guy falls asleep during the call.

00:02:03 - Patrick Chouinard
Yeah, I gotta admit, I did about six or seven hours with N8N [tool:N8N] over that weekend, man.

00:02:08 - Marc Juretus
That's pretty damn powerful, man. I published my build on Railway [tool:Railway], which was surprisingly really easy to do. Them webhooks are pretty damn slick, man, I must say.

00:02:22 - Marc Juretus
And it's funny — the foundation I have from the other frameworks I learned how to use, it's funny when you use that front-end tool, how much easier they are to use because of the other stuff that you've learned.

00:02:35 - Marc Juretus
I could definitely do some stuff for some realtors or something around here because just the fact that some of the webhooks I was doing were Google Drive [tool:Google Drive] — I had it that if you entered new names and addresses, as soon as you made a change, it did a route, the webhook caught it, scrubbed the email. And you had the AI build in the context of the email and build the type of response to go back without even having a non-techie. Could obviously do that pretty simply.

00:03:03 - Paul Miller
Well, it's wonderful for that rapid prototype. Because if you're trying to pitch something, you don't want to go to the effort of having to code that back end quickly. You just want to prototype it and have a really good front end, because they get all excited about the front end.

00:03:26 - Marc Juretus
I got to admit, that's pretty slick, man. They got a whole lot of stuff built in that tool panel there. So I haven't saved my build I have up on Railway, but my question is, once it's on Railway, what charges are associated with it?

00:03:51 - Paul Miller
I'm running it on Digital Ocean [tool:Digital Ocean]. Yeah, I'm running it on Digital Ocean, so I'm spending $20. And I've got hundreds of models. It's just a flat cost.

00:04:06 - Marc Juretus
Yeah, I did Railway because I have the stuff I've been showing you with LangChain [tool:LangChain] that I built with Next.js [tool:Next.js] is Railway. So it was like a couple of clicks and it was up.

00:04:21 - Paul Miller
It doesn't need a lot of capacity. Really, it's just not a lot of RAM and a bit of disk space. The question is if you want to run a database alongside it because you might want to run an instance of Postgres [tool:Postgres], whatever, and have it tying in closely to it.

00:04:49 - Marc Juretus
Yeah, I was doing the thing where I was submitting like a form and then you answered a few questions and then it emailed you back a story about you. The agent's context was, take the person's name and their occupation, and I want you to write a three or four paragraph story, and then send it back to them. Was pretty slick.

---

<!--SEGMENT
topic: ShipKit Course Progress Update
speakers: Brandon Hancock
keywords: ShipKit, prompt-driven development, RAG template, ADK agent, chat template, Gemini CLI, LangChain, LangGraph, course launch, AI-assisted coding
summary: Brandon joins and gives a progress update on ShipKit, his upcoming prompt-driven course product. He describes a system where every template (RAG, chat, ADK agent) comes with a course, a prompt, and multiple examples. He also addresses a community question about LangChain and LangGraph demand in enterprise job postings, confirming they are highly sought-after skills.
-->

00:06:34 - Brandon Hancock
So before we kick it off, I want to show you guys what cool things I've been working on, and then we'd love to go round robin like we normally do, questions first, and then immediately after that we can hop into just general updates.

00:06:49 - Brandon Hancock
So, long story short, from dawn to dusk, knocking out ShipKit [tool:ShipKit], so I just want to show you guys a quick progress update. Everything in here, when it comes to making apps, everything is prompt-driven, which I think is so cool because one of the coolest things about it is when making apps, you're always staring at a blank screen, but now prompts do all the hard work for you, from coming up with the ideas to doing all the hard work for you.

00:07:52 - Brandon Hancock
▶ Not only is there the course, then there's the actual prompt that does all the hard work for you and walks you through it. But then to make it even easier, what I'm doing is showing how to take each template — so like to take the RAG [tool:RAG] template and convert it into an application. How to take the chat template and convert it into your own custom application. How to take the ADK agent [tool:Google ADK], convert it to your own custom application. So literally everything has a course, a prompt, multiple examples.

00:08:15 - Brandon Hancock
I'm so pumped. I think this is how all courses will be in the future. Just, I think being in AI, we're kind of ahead of the curve. I'm using it to build stuff out myself and it's so much nicer than everything else I've previously done where usually you have to do all the hard work yourself. I think there's 25 more days, guys. So a lot less sleep, a lot more work.

00:08:54 - Brandon Hancock
For ShipKit, did a few videos for Gemini CLI [tool:Gemini CLI] recently. If you guys have any questions on that, happy to dive into that one as well.

00:09:19 - Brandon Hancock
So Juan was basically asking: it seems that most industry prefers LangChain [tool:LangChain] and LangGraph [tool:LangGraph]. Do you feel like this is the case? I see the modus operandi agentic framework requested in job postings.

<A>Yeah, so definitely on bigger enterprise companies, yes, they are more in demand. So yeah, one of the big things — literally the next thing in the queue is to add in a LangChain version, just because I think it is one of the most in demand. It's just that 80K [tool:CrewAI] is so easy to get going and get using, that we definitely wanted to make it a little bit more beginner friendly, so that's why it's 80K. In the big boys, when you have more time and you understand nodes, edges, graphs, that's when LangChain really comes in.</A>

---

<!--SEGMENT
topic: Vibe Coding in Corporate Environments
speakers: Brandon Hancock, Patrick Chouinard, Paul Miller
keywords: vibe coding, Cursor, Lovable, cybersecurity, corporate governance, CICD pipeline, Platform One, Big Bang, developer onboarding, enterprise AI tools
summary: Patrick raises a real-world challenge he received 30 minutes before the call: how to integrate vibe coding tools for business users (who want a Lovable-style IDE-free experience) while satisfying cybersecurity requirements for control and governance. Brandon references the US Air Force's Platform One / Big Bang CICD pipeline approach as a model. Paul advocates for a Dragon's Den / Shark Tank facilitation model using business analysts to filter and prioritize ideas before they reach developers.
-->

00:10:08 - Brandon Hancock
And then Patrick was basically asking: <Q>how do you integrate vibe coding practices inside a corporate environment — i.e., the business user wants a Lovable experience, and CyberSec wants something that they can control, and nobody realizes that vibe coding is not magic. You still need to know what you're doing.</Q>

00:10:26 - Brandon Hancock
Yeah, so awesome question, Patrick. One of the cool things is, at the end of the day, you being on both sides of the spectrum — understanding what both teams want — one of the coolest parts is you can actually quantify what cybersecurity wants, and it literally just comes down to making an insane amount of prompts. One of the main things I like to do is the generate-critique pattern with agents, where agent one does an action, and then immediately afterwards you follow it up with a critique and do this cycle a few times.

00:12:10 - Patrick Chouinard
Honestly, their question — it's not as much that they don't think it's secure, because they understand that what would be vibe-coded is more prototype and proof-of-concept type of application, not a full-fledged production application. Certainly not by a business user. And the challenge is I love all of your templates, but they're extremely good tools for developers that use development assisted by AI, like Cursor [tool:Cursor]. I cannot give a financial analyst Cursor and say, have at it. They're looking for the Lovable [tool:Lovable] experience, the IDE-free type of development. So that's the challenge — I want to give them something, but not something they're going to break everything with.

00:13:39 - Patrick Chouinard
The challenge we have right now is all the big consulting firms are going to them and saying, oh, you're going to be left in the dust. And now management is extremely happy, they want to go forward, they have budget. How much do you need? Go, make that happen. It's like, yeah, but I want to make that happen so in six months it's still going to work.

00:14:10 - Brandon Hancock
<A>I mean, the cool part is a very small development team joined with the cybersecurity guys could do the work of what used to be 10, you know? So you're not going to get left behind as long as the few developers you are using are using the tools properly.</A>

00:16:17 - Brandon Hancock
▶ I found the name of it — it's called Platform One [tool:Platform One], and then there's two things called Party Bus and Big Bang. Big Bang is the platform that has the CICD pipeline, and it talks about exactly how they set it up to solve the problem. Every business has the exact same problem. They had six templates — these are the only allowable pipelines. From template to pipeline to deployed app, these are the only six verticals we support, and if you follow one of these, we have instructions along the way to make sure you don't break stuff. [link:Platform One / Big Bang CICD pipeline documentation]

00:17:23 - Paul Miller
So there's always been a bit of a trend — if you look at companies like Eli Lilly or Google itself, where they want to get everyone vibe coding. But then make it into an app, and we all benefit from it. And what I've seen with this — one of the most successful methodologies is, instead of stressing out your poor dev teams, get your business analysts, your SAs, so they sit as those customer-facing resources. You could do like a Dragon's Den pitch, where you consolidate down the list of cool vibe projects. Get some outside facilitators, colored bean bags, go to a cool zone with the business guys, and say, hey, what would be some really cool things? Facilitate the ideas, get it to a shortlist, and then assign a group of BA/SAs to help hone it.

00:49:30 - Paul Miller
▶ Do a Shark Tank, and you have these groups coming up — they've gone and sat on their colored beanbags, they've come in and they're pitching these ideas, and they've got the screenshots, and then you tell the Shark Tank guys, here's the criteria: is it going to increase sales, is it going to save time, save money, whatever. Then that gets the shortlist. Then you can do what Brandon's talking about in terms of building that framework.

---

<!--SEGMENT
topic: Student AI Use Case and Education Discussion
speakers: Brandon Hancock, Adam
keywords: ChatGPT, Python code generation, scheduling optimization, constraint solving, AI in education, data parsing, university scheduling
summary: Adam shares a story about his daughter using ChatGPT to solve a complex class-schedule swapping problem involving chained constraints across multiple courses. ChatGPT generated and ran Python code to find a feasible 6-class swap solution, which her academic advisor approved. The discussion broadens to the role of AI in education and the risk of students being left behind if they don't learn to use these tools.
-->

00:14:43 - Brandon Hancock
And then Adam, basically you were saying your daughter yesterday — Adam, do you want to hop in on that?

00:14:48 - Adam
Yeah, so my daughter called yesterday and she wanted her class schedule changed. She had a list of her current schedule and basically a list of how many students are in each class and each subject. And she's like, well, I'm swapping classes — swap this for that. So she basically created a chain. Let's see, chemistry for biology. Now I'm swapping math for English. And she quickly realized that after you get a chain of like four or five, you just can't hold that in your head mentally. So she couldn't figure out how to do this manually.

00:15:47 - Adam
And she's like, can I use AI? She takes all the information from her school, uploads it to ChatGPT [tool:ChatGPT]. And the problem she ran into — well, first, she didn't realize that ChatGPT can generate Python and run it.

00:16:09 - Brandon Hancock
Light bulb moment, yeah.

00:16:10 - Adam
And then she was actually pretty good. Without reading any of the code, she realized she had data input problems — the graph was cut off when she screenshotted it and stuff. But they kept saying it was infeasible. And then finally I took a look at it, and she actually had problems with the way the university listed it — the spring semester and the fall semester had the columns in different orders in the two tables. And this was confusing the parser. So once I fixed that, it generated the Python code, ran it, we had to add some more constraints, generated more Python code, ran it again, and if she swapped six classes, she could get to the schedule she wanted. She went to her advisor with that proposal, and the advisor said sure.

00:17:31 - Brandon Hancock
Yeah, I think it's insane that students — I think in China right now, at the age of like six, they have to start using AI to do stuff, which is wild, because if you're not using it, your output is drastically lower than someone who is. ▶ I hope the entire education system starts using it one way or another, because if not, we're hosed.

00:18:01 - Adam
So it seems like a big thing with education is everyone's just talking about kids cheating on stuff.

00:18:07 - Brandon Hancock
I mean, yeah. My nieces and nephews — they know AI. I have made sure of it. They will not be left behind.

---

<!--SEGMENT
topic: N8N Workflows and Marc's Portfolio Project
speakers: Brandon Hancock, Marc Juretus, Paul Miller
keywords: N8N, webhooks, Railway, Google Drive, automation, portfolio project, fake company demo, resume screening, inventory chatbot, deployment
summary: Marc gives his round-robin update, detailing his N8N experiments including Google Drive webhook triggers that auto-generate personalized emails. He outlines a portfolio project plan: a fake company website with AI-powered job application screening, interview scheduling, and inventory chatbot — designed to demonstrate AI capabilities to potential clients. Brandon affirms this as the right strategy for landing first clients.
-->

00:18:45 - Brandon Hancock
All right, Marc, you're up first, man.

00:18:57 - Marc Juretus
So what I was working on — I engulfed myself with about seven or eight hours of N8N [tool:N8N], so I was practicing with the webhooks, because if I ever try to do some work on the outside, I'm not going to build a LangChain/LangGraph flow or a complex project. I can probably accomplish something if there's some small businesses or customers that would want to work with me. So I was pretty impressed with the webhooks. I was doing the forms — having forms submit where you pass the name and where you worked, and then I had the AI write a four-paragraph story about you.

00:19:46 - Marc Juretus
I could just do this. I could probably at least prototype something for somebody if they wanted me to do some work for them. The one with the Google Drive [tool:Google Drive] was what impressed the hell out of me — where I had a sheet, you made a change to the sheet, it triggered that webhook, and then it struck out an email based on what was in the subject and the body. So I could see a ton of usages for it.

00:20:12 - Brandon Hancock
▶ It is insane how easy it is to get started with N8N and the amount of value you can add in like two hours to any business with N8N. Just because most of the time, N8N can become the glue of the business to handle everything — hey, every time this happens, trigger this — and then go build an insane automation. You can instantly, because it's already deployed, go help out anyone.

00:21:06 - Marc Juretus
After that, I obviously have the fantasy thing done. So the next thing is I want to build a bogus company where I'll have jobs listed where you apply for a job, it'll respond to the resume, see if you were qualified or not, it'll send you a bogus appointment for an interview. I'll have a chat that runs inventory as well as answers questions. So if somebody asked, what have you done with AI? Here, go to this bogus site. You can apply for a job, you can look at our inventory listing. So that's going to be my objective.

00:21:39 - Brandon Hancock
▶ You're setting yourself up for success, man, because the second you can start to do it for yourself, then you can show it to others. They're like, okay, you look competent. They throw you a small project and then you're off to the races and then you start the snowball. You're literally in the hardest part, which is showcasing that you know how to use the skills and landing that first real-world client. Everything after this gets so much easier.

---

<!--SEGMENT
topic: Webhook Data Limits and Supabase Security
speakers: Brandon Hancock, Mitch, Paul Miller
keywords: webhooks, Supabase, Drizzle ORM, row-level security, Next.js, Vercel, Firebase, data limits, REST API, JSON payload, SQL injection
summary: Mitch asks about webhook payload size limits when sending large JSON objects to trigger background jobs. Brandon recommends sending only IDs and moving data-assembly logic into the background job itself. Mitch also raises a Supabase security warning about unrestricted database access. Brandon explains that the warning applies to direct Supabase client usage, not to Drizzle ORM queries through API endpoints, and clarifies when row-level security actually matters.
-->

00:23:47 - Mitch
Yeah. It's funny how one problem becomes like eight, but my main question is: <Q>for webhooks, is there a general guideline for how much data I can send via a webhook? And Supabase, I was trying to find any resources on it, and I couldn't.</Q>

00:24:05 - Brandon Hancock
So usually, a webhook — you will tell me what you're trying to do, and then I can give some guidance. Because from my understanding, you're thinking of getting all of the data, everything in a blob, one huge JSON object, and then sending it into the webhook, is what I'm guessing.

00:24:32 - Mitch
Yes, sir.

00:24:34 - Brandon Hancock
<A>Dude, okay, so here's usually what people do. Whatever logic you had in your application that was putting together that huge step one, two, three, four, five, six, seven, they usually move that into the very first step inside their backend code. So usually, instead, what they'll do is send in the webhook like, hey, here's the job ID, here's the whatever. Then once it receives the request, then it goes, okay, I know step one is to build out that monster JSON object that had everything it needed. ▶ So usually best practice, you don't want to send an insane amount of data. However, with that said, there's nothing stopping you from sending an insane amount of data. The internet specifically, REST protocols could easily handle a few hundred kilobytes, even up to a megabyte. I know Next.js [tool:Next.js] and Vercel [tool:Vercel] itself has a one or four megabyte default stopping point.</A>

00:25:49 - Mitch
Yeah, and Supabase [tool:Supabase], because I think they're the ones sending the data too. And I think they might have a limit. So I was going to test with N8N, just real quick, instead of doing the whole Google Cloud Functions thing. And then yeah, I guess the solution is just send the IDs.

00:26:02 - Brandon Hancock
Yeah, because it sounds like you already had the logic, because it was already building it one time, so now it's just actually moving that build logic into the background job that was actually going to run it, and then you don't even have to worry about size limits because you're literally sending over like 30 characters.

00:26:21 - Mitch
And then the other question I have — Supabase has been messaging me about, oh my gosh, your databases are like unrestricted and stuff.

00:26:40 - Brandon Hancock
<A>What that means is — have you used Firebase [tool:Firebase] before by chance? So what normally happens is you can actually create a Supabase client, and a lot of times people will literally allow users to use that client throughout their application, which allows them to almost write queries and request data, which is why it's saying it's unrestricted. So if you were to create that client and allow your users to fetch information, yes, the data is unrestricted and they could get your information, they could get mine — in the user's table, they could grab everyone's information.</A>

00:27:28 - Brandon Hancock
▶ So what we're doing is we do not use the Supabase client unless it's in a pre-structured API call, a pre-structured query, or a pre-structured mutation. So there's no way the user can ever access that differently. I wish there was a button to turn it off saying like, I'm not using that feature of Supabase.

00:28:15 - Mitch
I just use Drizzle [tool:Drizzle ORM] and I have things over the REST, baby.

00:28:19 - Brandon Hancock
<A>Perfect, so you're already doing it to where the user is not using Supabase to access that table. So that's why I said I wish you could turn that off because you're safe, you don't have to worry about it.</A>

---

<!--SEGMENT
topic: ShipKit Python vs TypeScript Frontend Discussion
speakers: Brandon Hancock, Paul Miller, Mitch
keywords: ShipKit, Next.js, TypeScript, Python, Gradio, Vercel, frontend frameworks, course roadmap, LangChain, desktop apps, Whisper
summary: Paul asks whether ShipKit will support Python-based frontends for developers who are more comfortable in Python than TypeScript. Brandon explains that Next.js is the dominant standard for real-world frontend applications in 2025 and that AI models have extensive training data on it, making it easier to work with even for TypeScript newcomers. He commits to building dedicated TypeScript and Python courses post-launch, tentatively in October.
-->

00:29:02 - Brandon Hancock
And then, just to answer your question, Paul — will you provide Python path frontends as well? Could you just elaborate on this super fast, Paul? Like, are you talking about a Gradio app?

00:29:18 - Paul Miller
Yeah, well, you've got the prompt where you can say, I want TypeScript or I want to use Python. And on the video, you talked about the thing going to help with Python backends. Are you going to help with the Python frontend? Because for some of us, TypeScript — you're thinking, oh my God, I don't know if I could deal with building a TypeScript app. I'd love to build a Python app, not that it's better than TypeScript, but in a world that I understand it, with what you're doing with ShipKit [tool:ShipKit].

00:29:54 - Brandon Hancock
<A>Yeah, so the key thing here is, what is the most common real-world tool that people are using? And most, at this point, if you're trying to build a front-end application in 2025, it is done with Next.js [tool:Next.js]. I think it's an insane amount of all new real-world applications are using it, just because it's so easy to use, it's so standard, there's so many support documents — it is the standard. What's also great about it is AI truly understands Next.js this day and age, because there's so much training data on it, so it can do a much better job too. Even though TypeScript is definitely a little bit more of a steeper learning curve, AI really does handle a lot of it for you.</A>

00:30:51 - Brandon Hancock
▶ Stick with Python back-end, and come on, Paul, make the jump — it's cleaner, it's better, let's just do it.

00:31:00 - Brandon Hancock
One of the things I really want to work on post-launch is a TypeScript course for you guys, a Python course, and just a straight-up vanilla Next.js course, just because there's still a lot of people who are very strong in one area and not another. So I want to spread the knowledge — definitely will be doing that at some point. It'll probably be October, because the next 20–25 days are busy.

00:55:40 - Brandon Hancock
What I want to follow it up with is a desktop course, because so many people are building desktop apps. Whisper [tool:Whisper] — there's so many examples of a startup where all they do is just bring AI from the internet to your computer and add a shortcut key to where you're instantly accessing AI. So that paradigm is such an invaluable skill. Those are the two that come to my head for the next upcoming ones to add to ShipKit.

---

<!--SEGMENT
topic: Juan's VPN Infrastructure and GPU Inference Setup
speakers: Brandon Hancock, Juan Torres
keywords: Tailscale VPN, Windsurf, agentic IDE, NVIDIA A100, GPU inference, LLM hosting, Oculus servers, Vertex AI, token throughput, API proxy, Elastic Beanstalk
summary: Juan shares that he resolved a major connectivity issue for his client by installing Tailscale VPN binaries in a persistent filesystem on shared servers — without admin permissions — enabling him to use an agentic IDE remotely. He also built a GPU stress-testing dashboard showing 72 tokens/second throughput on an NVIDIA A100 running an 8B parameter model. The discussion covers how to expose the on-premise LLM inference endpoint to external applications via a secure authenticated proxy.
-->

00:32:05 - Juan Torres
Yeah, so last week I was able to resolve the great issue that my client was facing. I found a way to create a VPN secure connection between the Oculus server and my local computer without having administrative permissions. So what I did, I simply downloaded the binaries for the Tailscale [tool:Tailscale] VPN service inside the permanent, persistent file system within the computer through their servers. And through that, now I'm able to use Windsurf [tool:Windsurf] and an agentic IDE on the server without having to go through the barbaric primitive use of VS Code.

00:33:51 - Juan Torres
Technically speaking, they were going to charge him like $7,500 for hiring a group of three to four developers. I still have to make the API or URL infrastructure in order to make the recall to whatever application or deployment method they're going to use. But now that I have the connectivity issue resolved, I think that's going to be pretty easy.

00:34:22 - Juan Torres
Yeah, and it was such good attribution that even the owners of the servers, Oculus, they told me, hey, can you actually come over and teach us how to do this? Can you teach our co-op members how to make the connection to the agentic IDE?

00:34:43 - Brandon Hancock
I hope that's what you said — I'd be happy to for a fee.

00:35:00 - Juan Torres
And then additionally to that, I was able to create an infrastructure also to be able to test the GPU LLM infrastructure. So as you can see right there, I created a quick dashboard that allows me to stress test the GPU and then be able to assess the token utilization of the model inside the virtual environment that I'm working in. This is going to help me facilitate the process of A/B testing several models.

00:35:38 - Brandon Hancock
<Q>So I see NVIDIA A100 [tool:NVIDIA A100], average throughput 72 tokens per second. Not going to lie, I would think that would hopefully be like 300. Or is that because I'm confusing A100s and H100s?</Q>

00:36:13 - Juan Torres
<A>The tests were based on prompts. So the model that I'm using is an 8 billion parameter one. So I guess the GPU could take even more heat if it wanted to. But so far, the GPU inference of 8 billion parameters seems to be feasible — doesn't thermal throttle or anything like that.</A>

00:36:50 - Juan Torres
Just if anyone has information on developing an API URL connection that I can use for the inference to the LLM — if anyone hears anything, let me know.

00:37:06 - Brandon Hancock
<A>So my understanding — this is running in a private virtual network, and what we're trying to do is expose it to the outside world. I think you will just set up almost like a proxy, a secure proxy. And all it does is it says, hey, I'm receiving requests from the outside, I do have secure access to the private network, and I need to make sure that the person is authenticated through some sort of API key. That's probably the simplest way — every person we want to use this gets an API key, and then just in the header, we just say, do they have an API key? Great. This is now a valid request. Go forth.</A>

---

<!--SEGMENT
topic: Multi-Tenant Asset Management SaaS Architecture
speakers: Brandon Hancock, Tom Welsh
keywords: multi-tenant, Supabase, Drizzle ORM, row-level security, Firebase, database per organization, shared database, enterprise SaaS, ShipKit, asset management
summary: Tom reports using ShipKit's rules to audit his existing asset management codebase (95% compliant) and is now converting it into a multi-tenant SaaS product. He plans database-per-organization for enterprise tiers and a shared database for lower-cost tiers. Brandon and Tom discuss the security implications of shared databases, Firebase's notorious unrestricted-access vulnerability, and how Drizzle ORM sidesteps Supabase's row-level security warnings entirely.
-->

00:57:58 - Brandon Hancock
All right, Tom, you're up next, man.

00:58:12 - Tom Welsh
I just want to reiterate what Paul was saying about ShipKit [tool:ShipKit]. Absolutely awesome. I obviously signed up for it, downloaded it. I've already pulled all the rules across and thrown it into my asset management thing. Ran it, checked my code out — was 95% compliant. I thought, yeah, I'm happy with that.

00:58:48 - Tom Welsh
So on the asset management side, I'm now trying to turn it into a product. With multi-tenant — so standalone database or shared databases, basically backends. So yeah, I'm just trying to extract myself from where I was and get some current settings set up so you can actually define as you set up and go in — a web admin type interface to set up your database and everything.

00:59:23 - Brandon Hancock
<Q>Out of curiosity, are you setting up a database per organization? Like, is that what you're working towards eventually?</Q>

00:59:31 - Tom Welsh
<A>I'm going to do database per organization for enterprise. I'm going to do shared multi-tenant shared database for cheaper versions.</A>

00:59:48 - Tom Welsh
And my security head's going, I don't like shared databases. Data leaks.

01:00:07 - Brandon Hancock
<A>If you look at most recent big leaks that you see that get talked about, they're usually using Firebase [tool:Firebase]. When they were using Firebase, that rule that Mitch was just showcasing — the unsecured — it's because they literally have a Firebase client that can technically, the second it has the right key, access the entire database. And all it takes is a developer who knows, oh, I can see they're making a request to this URL — great, I can now get anything. ▶ If you just don't use Firebase, you automatically have prevented a lot of heartache. Then if you just stick to normal authorization and authentication, most stuff is pretty straightforward — is the user ID that's making the request matching the user ID of the field they're trying to access?</A>

01:01:02 - Tom Welsh
Yeah, that's right, so I was looking at row-level security on Supabase [tool:Supabase], but I haven't really dug into that much. But I take it that's just literally — you're authorized to run that query against that part of the database and that part only, so you don't get information slippage.

01:01:24 - Brandon Hancock
<A>Yeah, and it's strictly when you're using the Supabase client to access the database. And I think you're using Drizzle [tool:Drizzle ORM] — so it doesn't work. You're doing literally two different universes. I wish there was a button to just say, stop bothering me about this.</A>

01:01:49 - Brandon Hancock
▶ Here's a few things I see so valuable about this: A, enterprise — so you're starting solving rich people's problems. Literally the same app doing the same thing, just hosted for a big customer. And I'm just going to say it — it's quote-unquote a boring market. Most people are looking left, and I think you're looking right. It checks all the good boxes for really good ideas.

---

<!--SEGMENT
topic: ADK Integration with Django and Google Cloud Auth
speakers: Brandon Hancock, Ola Oyo
keywords: Google ADK, Django, Vertex AI, Google AI Studio, Docker, API key, Google Workspace, session management, property management, context-aware agents, Python
summary: Ola, a new member with a data science background, is building a property management platform on Django and wants to integrate Google ADK for context-aware chat and action-taking (e.g., updating listings via chat). He has struggled with both Vertex AI ADC authentication inside Docker and Google Workspace policy restrictions blocking API key generation. Brandon recommends embedding ADK directly in Django using the runner.run() pattern and setting VERTEX=false with a direct API key, and suggests creating a personal Google Cloud account with $5 billing to bypass organizational policy issues.
-->

01:03:23 - Brandon Hancock
All right, Ola, you're up next, buddy.

01:03:29 - Ola Oyo
Hey, Brandon. I went to bed one night trying to figure out how I was going to integrate ADKs [tool:Google ADK] into my Django [tool:Django] app. I wake up the next morning and then YouTube suggested you. So yes, it was meant to be.

01:04:03 - Ola Oyo
So I took most of last week, I dug into the ADK kit course. It was very helpful. But I think I have come to a bit of a snag. So I'm building a property management platform for estate managers, and I'm trying to integrate the aspect into it to be context aware. The service is running on Django, and I had spent a large part of last week trying to run it as a separate service. But looking at a bunch of Medium posts, they just said that it's better to integrate the ADK directly in Django. So I've kind of done that, and I'm trying to figure out, following the same ADK structure, just how to get the ADK to run in my Django application and also be context aware — talking user ID, picking up the right information from my Postgres table so that when the user hits that endpoint, they're also able to get context-aware data that's coming back.

01:05:14 - Ola Oyo
In fact, just before this call, I've been battling with GCP [tool:Google Cloud Platform], tried to get my Vertex AI [tool:Vertex AI] to work locally within my Docker [tool:Docker] container, and then I was also just trying to get the API key. I said, you know what, to hell with Vertex. I'm just going to get the API key directly. And then because I'm using my organization, Google Workspace [tool:Google Workspace] is giving me a whole bunch of challenges — policy not allowed, blah, blah, blah.

01:05:49 - Brandon Hancock
<Q>Okay, so are you trying to do option one, where you have ADK running on port 8001, Django is making a request to port 8001, and then ADK is sending back a response? Or are you saying, I'm not doing that, I'm actually in my Django application trying to have the entire ADK experience run?</Q>

01:06:32 - Ola Oyo
<A>So I'm trying to have the ADK run directly in the Django application. The problems I had with running ADK separately were authentication and having to sort of recreate all of my ORM and Django on the ADK again, just so that the ADK is context aware of the specific user and the information it should be getting from the table. So even that was just too much of a headache, and then it was like, okay, just have your ADK sit directly inside Django — it just makes it easier.</A>

01:07:34 - Brandon Hancock
<A>Yeah, I mean, both ways should work. I will say I have more experience with the separate approach. And the quick answer to solve the context issue is when you're actually creating sessions in ADK, you can actually set initial state for user ID, for whatever. So that is how I usually work around that. So I'll create a session — I'm user ID, his name is Bob, here's whatever else you want. Then whenever you start sending in messages, you pass everything in. ▶ The cool part is, if you are hosting it inside of your Django application, you never have to worry about anything with deployment, because it's in your Django app. You literally just have to call root_agent.run, and that's it.</A>

01:12:00 - Ola Oyo
One, being able to even connect to the model. I tried two methods. One was logging in directly, using my ADC to Google Cloud, having Vertex as true, and then logging in and trying to have those credentials sit directly in my Docker container. That didn't work. Next I tried was going directly to Google AI Studio [tool:Google AI Studio] and grabbing the API key. That has also given me an error based on my organizational policies for Workspace.

01:13:42 - Brandon Hancock
<A>▶ The easiest way to get it up and working is to create a project in Google Cloud, make sure you have billing set up, and the second you have billing set up, you want to make sure your environment variables are set to VERTEX equals false. And then you paste in that Google API key. That is the key — Vertex has to be equal to false for it to detect your API key.</A>

01:14:57 - Brandon Hancock
▶ Hey, even if you make a personal account and put in $5, it will last you a very, very long time, so it might be worth just to get around the headache for $5.

---

<!--SEGMENT
topic: Topic Launch Platform Demo and Creator Feedback
speakers: Brandon Hancock, Jaylen Davis
keywords: Topic Launch, YouTube content monetization, crowdfunding, Kickstarter, creator economy, ShipKit, fan-funded videos, content strategy, community voting
summary: Jaylen presents Topic Launch (topiclaunch.com), a platform where YouTube fans fund content ideas — fans set a funding threshold, the community backs it, and the creator delivers the video within 48 hours for 90% of the funds. Brandon gives candid creator feedback: the 48-hour delivery constraint is too rigid for complex technical videos, and suggests a simpler subscription model where creators post topic ideas and the community votes thumbs up/down to signal demand — which Brandon says he would pay $30/month for immediately.
-->

01:24:41 - Brandon Hancock
All right, Jaylen, you're up next, buddy.

01:24:52 - Jaylen Davis
So I spoke with you maybe a month and a half ago. Mitch sent me a link to the Zoom meeting and I spoke with you. I had a platform that I was creating that you seemed to really like. It's called Topic Launch [tool:Topic Launch]. I actually got it done. Back then I was still coding it, but I got it done and we just started — me and my business partner — creating user-generated content on Instagram. That was mostly just coming to let you know if you were interested in hopping on the platform. I actually even created an account for you.

01:25:36 - Brandon Hancock
<Q>So I cannot remember — was the goal, okay, it was funding, so it was fun topics for your favorite YouTubers?</Q>

01:25:43 - Jaylen Davis
<A>Yeah, so basically YouTubers monetize their audience by fans funding content ideas for them. So a fan creates the topic, the community — if the fan doesn't fund the topic to the fullest, the community backs the topic, and then you deliver the video. So within 48 hours you receive 90% of the funding while Topic Launch takes 10%. Very simple and straight to the point. It saves you from running out of ideas and as well as creating videos based off of ideas that you thought were going to pop and they actually flopped.</A>

01:26:16 - Brandon Hancock
No, that is awesome. I think this is a very, really good idea. But I'll just say it from the creator standpoint — even right now, if I was paid to make a video literally for the next 25 days, I couldn't. But if I was in YouTube mode, like this would be insanely, insanely helpful.

01:28:22 - Brandon Hancock
▶ Serious feedback: as the creator, just let me pay 30 bucks a month, 40 bucks a month, whatever the number is, and just allow me to put idea topics out there, and community thumbs up, thumbs down, or community suggests their own videos and thumbs up, thumbs down. Like, that is so much more valuable, because there's some times where, even if I have a sponsorship deal or whatever, I legitimately could not take on another video. But just allowing the community to let me see signal versus noise would be super helpful. If you are right now, I could not, in good faith, sign up for the current one, just because I wouldn't want to take people's money knowing I could not, most of the time, deliver on the 48-hour timeline.

01:31:39 - Brandon Hancock
▶ Shipkit.ai [link:shipkit.ai] — cannot recommend it enough for this. You have an idea, you have a very valuable idea. Now it's just building it out as fast as possible. Really would recommend to check it out, because you have an idea — let's just make it look beautiful, let's get it out to the world fast, and go forth.

---

<!--SEGMENT
topic: Next.js Hosting, LinkedIn Scraping, and MCP Compliance
speakers: Brandon Hancock, Jake Maymar
keywords: Next.js, Vercel, Netlify, WordPress, Namecheap, Mailgun, LinkedIn API, Apify, GDPR, MCP, OAuth, Serper, data scraping, compliance
summary: Jake is migrating his website from WordPress to Next.js and asks about hosting options. Brandon recommends Vercel for its seamless Next.js integration, SSR/SEO benefits, and easy custom domain setup. Jake then asks about GDPR-compliant LinkedIn profile scraping for his app (which uses LinkedIn OAuth but only receives basic profile data). Brandon and Jake discuss Apify and the LinkedIn API's limitations. Finally, Jake asks about MCP security compliance; Brandon reframes MCPs as function calls and says GDPR compliance is mainly about controlling what data you store and being able to delete it on request.
-->

01:32:57 - Jake Maymar
So first of all, the ShipKit [tool:ShipKit] is amazing. I've already written so many things using it. And I've also altered the prompts, because it's such a good starting place. And I'm like, okay, I need to just tweak this. And I can't wait to really fully dive in.

01:33:30 - Jake Maymar
I'm revisiting my website, which is WordPress [tool:WordPress], and I have a love-hate relationship with it. And I finally just decided I'm done — switching completely to Next.js [tool:Next.js]. I actually really like building things in it. And so I'm curious, what should I host it on? Because I've been looking at Netlify [tool:Netlify]. And I'm using SiteGround right now, but they don't really host Next.js. I keep hearing about Hostinger. But yeah, is there any one you would recommend?

01:34:22 - Brandon Hancock
<A>▶ I mean, the easiest one, especially if you're hosting a single project — Vercel [tool:Vercel]. You literally just say deploy app, you point to your GitHub project and it's done. It is insanely easy, how well it works. And it actually does the full process of distributing the application, because it understands, okay, this is Next.js code, so I can actually server-side render a lot of this stuff to make the static pages look better. There are so many benefits of using it. And even if you went pro to get a lot more of the additional features, it's $20 a month. But if this is your first app, on the hobby tier, which is completely free, you're going to get everything that was just mentioned.</A>

01:35:18 - Jake Maymar
<Q>But how do you do — I have my own domain and email address and all that. That's not tied to Vercel. That would be just a different thing, right?</Q>

01:35:25 - Brandon Hancock
<A>Yeah, so when it comes to setting up your own domain — here was my default ShipKit application. I added it in and it gave me a few commands to pass over to Namecheap [tool:Namecheap] where I bought the domain, and then boom, like you're now using your own URL. So it was so easy to add that. On the side of mail and stuff — you could easily just create a Google business account and set that up. I think it's like $7–$8 a month to get that business email. And then if you want to get some automated emails sent out, Mailgun [tool:Mailgun] would be my default recommendation. Very standard, very reliable.</A>

01:36:45 - Jake Maymar
I have another question. So I'm already using OAuth, already signed in with LinkedIn, so I have your name, but the problem is LinkedIn doesn't give you access to much — if you're just using the default setting where you don't have higher-level permissions, you get name, title, and image, that's it. And so what I want to do is actually get the profile information. I've been thinking about using Serper [tool:Serper], but it has to be GDPR compliant, and so it has to only be public profile. I'm just curious — because I'm not trying to get a ton of scraped information, I just need to get enough that you would see on a public profile, and it's actually the user themselves who is saying, yes, this is the data I want to bring in. I'm just saving time for them, essentially.

01:38:24 - Brandon Hancock
<A>I mean, one of the hardest parts — LinkedIn, just any site where you want to scrape anything from like a Twitter or a LinkedIn — is a huge pain. There's a specific one — if anyone else knows it off the top of their head, feel free to shout it out. So there's a couple I can throw out. There's Apify [tool:Apify], which is like, okay, but I'm worried about the compliance issues.</A>

01:40:12 - Brandon Hancock
<A>Dude, the LinkedIn API [tool:LinkedIn API] is a beast. I've had to use it before for different companies and it works very well when you're just trying to do your own post or your own profile. It's the second you want to start doing other people's stuff that — I remember I had a ton of issues.</A>

01:41:06 - Brandon Hancock
▶ I mean, I think GDPR is just, like, what data do you store about our users? And in your case, even if all I'm storing about them is their name — yes, this one other service that is not mine is getting this much data, but I'm grabbing that and that, which are public-facing. I would be curious if you did a ChatGPT deep research on it, what it would say.

01:41:38 - Jake Maymar
<Q>Is there a way to make MCPs compliant? Like I know you were talking about A2A as sort of a compliance thing. Because MCPs are definitely like Wild Wild West. How secure is an MCP?</Q>

01:42:03 - Jake Maymar
I guess the same thing — GDPR. I'm not trying to do SOC 1, SOC 2, or HIPAA or anything like that. It just needs to be fairly secure. It seems like every MCP is an MCP, so you have to kind of look at it and figure out what its vulnerability is. There doesn't seem to be a standard.

01:42:32 - Brandon Hancock
<A>▶ At the end of the day, an MCP [tool:MCP] is nothing more than a function call that has been wrapped to be accessible to agents. So the real question is, what is your underlying task doing? Whether that's scraping data, whatever that task is, we just want to make sure whatever you're storing is okay and it's okay with the logs that are generated. And from my understanding too, with GDPR, one of the big requirements is to be able to delete data too. Like if you get an email, you have so many days to delete data. So you also just need to be able to have control over your logs to make sure that you can delete them.</A>

---

<!--SEGMENT
topic: SaaS Factory App and Authentication Troubleshooting
speakers: Brandon Hancock, Never2Nervous (Lewis Louisius), Prem
keywords: Supabase, Next.js, Google Cloud Platform, OAuth, authentication, middleware, redirect URLs, Neon, Clerk, Upload Thing, SaaS, Base44, Firebase
summary: Lewis (a data science background developer) is building a SaaS factory app — a platform to automate idea-to-deployed-app pipelines with agentic marketing workflows — and has been stuck for three weeks on an OAuth routing bug after Google/GitHub login. Brandon diagnoses the likely cause as missing or misconfigured Next.js middleware that fails to consume the OAuth callback token and redirect properly. He strongly recommends migrating from raw Google Cloud Platform to Supabase for authentication, database, and blob storage, citing simplicity, cost, and built-in middleware. Prem endorses the recommendation from personal experience.
-->

01:44:45 - Never2Nervous
Hey, Brandon. So this is my first call, and I've been having some trouble with the application I'm trying to deploy. Background is in data science, so I'm a complete novice when it comes to front-end application consumer products.

01:45:17 - Never2Nervous
So the application I'm building is a SaaS factory. Pretty much the idea behind it is — some of these large corporations have the funds and resources to throw a bunch of ideas against the wall and see what sticks and then scale that idea. So I thought, what if I could template that process and automate it — give people the ability to submit ideas, have it production ready and deployed, and then I also have some agentic workflows that handle automated marketing to get the idea out there into the world. Base44 [tool:Base44] is pretty much my direct competitor.

01:46:23 - Never2Nervous
I've been having this issue with authentication. I've just been going in loops with it for like three weeks. I do Google Authenticator and GitHub Authenticator for those two options. It seems to be like a routing issue. So once you log in, it doesn't route you back to the page for some reason.

01:47:24 - Brandon Hancock
<Q>Are you using Supabase? Are you doing just Clerk? What are we doing to handle authentication?</Q>

01:47:36 - Never2Nervous
Working with Google Cloud resources in the back-end.

01:48:20 - Brandon Hancock
<A>I think you were developing your first project on hard mode. I would stay away from raw Google Cloud, unless you have to actually use it. Not that there's anything wrong with Google Cloud or AWS, but there are simpler solutions that are basically free. So like, today we've talked a ton about Supabase [tool:Supabase]. If you wanted to have a very simple app that had authentication, a database, a blob store, Supabase is awesome. If you're like, I don't like Supabase, I want to go other options — you could use Neon [tool:Neon] for your database, super generous free tier. You could use Clerk [tool:Clerk] for auth. For a blob store, there's Upload Thing [tool:Upload Thing], great choice. I think the current tech stack is automatically going to make everything harder.</A>

01:52:38 - Brandon Hancock
<A>▶ I think the issue is — when you actually get the credentials from Google, what it's doing is in the header of the response, it's including the client token, it's including so much information in the return request URL and the header, where it has the user's token, it has a page to redirect to afterwards — it has all the information set up. But if your middleware is not properly set up to handle that, it's not going to take action on all the information you get back. So then you end up in a loop where nothing actually is happening. And the reason why I keep recommending Supabase is because it comes with middleware that is set up to consume all that information and properly log you in.</A>

01:53:47 - Brandon Hancock
▶ I would just check out full-stack application videos with Auth. Because people have solved these problems in the past. Here's a playlist that literally walks through Next.js plus Supabase — I think it's video three in that series that has the exact step you need to follow. [link:Next.js + Supabase authentication tutorial playlist]

01:54:24 - Prem
I think your course — the AI full-stack marketing platform — that kind of solved a lot of problems for me. It kind of solved all the full-stack end-to-end needs for the SaaS I was building. So I just want to throw it out there.

01:55:03 - Brandon Hancock
▶ And hey, if you can wait 25 days, dude, all this will be built for you automatically. These problems are already solved in ShipKit [tool:ShipKit]. But yeah, key thing — I would just simplify. I think right now you're using very big-boy tools made for enterprise. If we could just bring it back down to stuff made for more like solo developers where it's not a team.

---

<!--SEGMENT
topic: ADK Multi-Agent Routing, Chat API Design, and Voice Assistants
speakers: Brandon Hancock, Hemal Shah
keywords: Google ADK, multi-agent, orchestrator pattern, FastAPI, server-sent events, JSON schema, chat API, Gemini Live, LiveKit, Bland AI, voice assistant, sequential agent, parallel agent, custom agent
summary: Hemal is building an interactive chatbot with rich UI elements (dropdowns, calendar pickers) that uses ADK multi-agent workflows to check completeness of user requests before executing actions. He asks about standard JSON schemas for chat request/response APIs and about routing between agents conditionally. Brandon points to Google's ADK browser-agent example as a reference for phase-based orchestrator prompts, and recommends using a ref folder pattern to guide AI in replicating patterns. For voice assistants, Brandon recommends Gemini Live library over ADK voice, and highlights LiveKit as a strong open-source option.
-->

01:38:36 - Hemal Shah
So I continued working on my kind of interactive chat application. So it's your plain text request-response, but there are rich content media on your chatbot — you can have rich HTML elements, dropdown, calendar picker to get the missing information. So a user is requesting something — I want to book a travel or something — and if the user hasn't provided all the requested information, the assistant can extract the user's intent, identify what are the missing pieces, check for completeness, and then return back with some structure — hey, give me this, give me dates, give me, if you want to travel somewhere, here is a pre-selected list of items that you can choose from.

02:12:28 - Hemal Shah
So looking into it, working with the ADK [tool:Google ADK] that you created — and I second what Ola said earlier, that if you had not created that video, I would not have learned it from Google's documentation. I find it a little bit more user-friendly, but no, that documentation is helping a lot, and ADK Web is amazing. I can test the agent — it must be multi-agent because there are multiple steps involved, like completeness check before I hit the trigger. But there were certain issues — I went into issue where I want a routing type of workflow. I know I went to sequential, parallel agent, but there's a condition: if completeness check is good, then you move for the execution; if it is not, if there are missing pieces, then I need to add more metadata around it. I was able to figure that out using some custom agent.

02:13:52 - Brandon Hancock
<A>▶ So they have a ton of examples. You just have to know where to dig for them. They have one where they did a browser agent. The orchestrator has phases — it's like phase one, gather information. When you're gathering information, you can direct to agent one, two, or three. Once you have completed phase one, move to phase two. When you're in phase two, you can route to these three agents. So they specifically call out how to, at multiple steps, route to the necessary different people. [link:Google ADK browser agent example repository]</A>

02:17:06 - Brandon Hancock
▶ Quick cheat code — what I always do is when I'm working on another project, I always make a ref folder, and then in here I would clone in this project that I just showed you and say, hey, I'm trying to make something like this. Can you help me update my prompt to look like this reference project? And this is a really quick way — you could dump in three or four projects that you like. You could dump in any YouTube videos that I've made, just dump them in there and say, I'm trying to steal this from Brandon's code, this from Google's code, and this from another project. Can you please help me make this prompt work well?

02:18:02 - Hemal Shah
<Q>So ADK will take care of all these things, but then there is a chat UI in front of it and then a chat API, which is FastAPI [tool:FastAPI]. The request-response model between UI and API — chat request, chat response. I'm wondering if there is any standard JSON model that most people are using when we send a request to the API and when the response comes back. The JSON structure that I can build on top of it.</Q>

02:18:47 - Brandon Hancock
<A>So at least in ADK land and Gemini land, they do it through parts. So a part can be a type string, and that's like a message contains parts, parts contain text, like images. Whenever you run ADK, you can literally do ADK serve API, and what that will do is actually expose endpoints to your ADK application. Technically when you do ADK Web, what's happening behind the scenes is it spins up ADK using a FastAPI, and you have access to sessions, you can trigger runs — it opens up an entire FastAPI around ADK. The two most common return types are SSE (server-sent events), which are going to stream back small chunks where it's going to say content and author — that's how you can get back a stream of data and start to build out that response. The other one is just a straight-up JSON object, which just has content and author and whatever else you want to add to it.</A>

02:22:50 - Hemal Shah
<Q>I went through your ADK voice tutorial as well. And my question is, if you want to create a voice assistant for customer support which taps into your business's ERP, CRM — there are many tools out there: 11 Labs [tool:ElevenLabs], Voiceflow [tool:Voiceflow]. Is there any recommendation — is this better than other, or a full-blown voice assistant?</Q>

02:23:35 - Brandon Hancock
<A>▶ At this point for recommendations — after building that ADK voice tutorial out, I would actually just use the straight-up Gemini Live [tool:Gemini Live] library instead, just because when you start to do agent calls to function calls, it starts to get really weird. If you're looking for no-code tools, I like Bland [tool:Bland AI]. They do a really cool one. Bastion and Maxim actually used one recently — I think it's called LiveKit [tool:LiveKit]. So you get to do some code — you get the best of both worlds. It's already a pre-created library, it works well, you can host it, you can hook it up to phones. I would actually just use what these guys are doing.</A>

---

<!--SEGMENT
topic: Job Search Support and Freelance Client Opportunities
speakers: Brandon Hancock, Alex Wilson, Never2Nervous, Adam
keywords: job search, consulting firms, fraud analyst, ShipKit, LHH outplacement, severance, hedge funds, N8N automation, Vertex AI, open source LLMs, freelancing stress
summary: Alex shares his job search progress (fraud analyst background, on severance, using LHH outplacement services) and reports successfully building an app using ShipKit prompts in about three days. Brandon and community members offer networking support — Lewis (Never2Nervous) offers to pass Alex's resume to a Big Four consulting firm, and Brandon offers to check with his wife's consulting firm (UHY). Adam shares a promising new client lead: a hedge fund headhunter who wants to automate his document-heavy ChatGPT workflow using open-source/Vertex-hosted models.
-->

01:55:34 - Alex Wilson
So, still looking for work, which is no fun.

01:55:54 - Alex Wilson
I am still going the standard — not trying to create my own work, but like, you know, find a nine-to-five, that type of stuff.

01:56:09 - Brandon Hancock
<Q>Curiosity — is it mostly LinkedIn? Is that where most of it's at?</Q>

01:56:15 - Alex Wilson
<A>Yeah, LinkedIn [tool:LinkedIn]. Because I was let go, I'm having LHH [tool:LHH] for my account with my previous employer, so they're guiding and looking over my resume, all that good stuff.</A>

01:56:38 - Alex Wilson
But ShipKit [tool:ShipKit] — I did it right away, and tested it out, and was surprised that I actually was able to spin up an app within, I think, about three days, and it actually worked. I did run into problems with the authentication, so I'm looking forward to actually having access to the repository. I think it would have made it a lot easier.

01:57:18 - Alex Wilson
I started from prompt one and went all the way through nine to create the project. I didn't actually read a lot of the stuff that it was building, I was just testing it. But it actually completely did it.

01:59:41 - Brandon Hancock
▶ I would just check out also consulting firms, because most developers are always like, I want a tech company, but with your background, you're kind of versatile. It's not just I'm this box — you actually have a wider array of skills, which would work really well in a consulting company. And there's so many of those. I can ask right after this if my wife knows anything at UHY [tool:UHY].

02:03:37 - Never2Nervous
Alex, I also work for a consulting firm, one of the Big Fours. And I can definitely get your resume in front of a human and not a robot, if you're interested.

02:04:25 - Adam
So, Brandon, I was going through your ADK tutorial, and I noticed the tutorial calls for preview versions of some of the Gemini models, and apparently they're no longer available, so I sent you a pull request.

02:05:03 - Adam
So today I just had coffee with a guy — he actually lives in my same town, found me on the internet. He's a headhunter for hedge funds. And his current process is he has a bunch of documents, and he copy-pastes prompts and documents into ChatGPT [tool:ChatGPT], gets the results and does whatever with them. And I'm like, oh yeah, that's my perfect client, right, because I can just automate all of that.

02:06:42 - Adam
One thing he's worried about is if he puts all his stuff into ChatGPT, someone's going to hack GPT and get all this data. So he's a little worried about that. So he wants to use open-source stuff, which is fine by me.

02:07:32 - Adam
I think we're going to do models hosted in like Vertex [tool:Vertex AI] or something like that.

02:08:30 - Adam
Not related to this, but I've been collaborating or planning stuff with a person who has what she's calling a fractional business development agency — basically outsourcing your sales to her. And she's going to give me a discount if I help her with her website. And I was going to use React and Flask, but now I'm thinking, hearing all the stuff, I should go with the Supabase/Next.js route instead.

02:09:31 - Brandon Hancock
<A>▶ Big recommendation I have is strictly — why I love Next.js [tool:Next.js] and Vercel [tool:Vercel] so much together is because of all of the — when you're creating pages, a lot of the time you have static pages, and for better SEO optimization to help rank better, Next.js coupled with Vercel knows how to actually serve certain aspects of your page so that when Google is crawling everything, it can actually see your static pages. Because one of the big issues when you're using just a normal React app and you're not using Next.js is everything is rendered through JavaScript. When something comes to check out your site, it's like, dude, I actually can't tell what's going on until I load and use something to render the JavaScript.</A>

02:02:06 - Brandon Hancock
So obviously, jobs my entire life until leaving Crew AI [tool:CrewAI], and then at that point, it was like, okay, it's eat what you kill kind of thing. Unless I do something valuable to the world, no money comes in. So launching courses and doing stuff and freelancing work — your stress, yes, you can make more, but I'll just be honest with you guys, it is stressful. I feel like a lot of developers don't talk about it enough. They're just like, oh yeah, it's so easy, it's so fun. No, it's free. I told my wife all the time, I'm going to have so many gray hairs by the time I actually turn 30 here in a few months. There's so much extra stress that goes to it. I wouldn't trade it for the world. I absolutely love it. But just being honest — when money's not coming in and you see your credit card bills going up, it's very stressful.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript and were not present in the SPEAKER_ALIASES context block (which was not provided to this session):

- **Adam** — last name not given; referenced as having a daughter in college and a hedge fund headhunter client lead
- **Mitch** — last name not given; working on webhook/Supabase workflows
- **Ola Oyo** — name passed through as given; building a Django-based property management platform
- **Prem** — last name not given; migrating from Vercel Postgres to Supabase
- **Hemal Shah** — name passed through as given; building an interactive ADK-based chatbot
- **Jaylen Davis** — name passed through as given; creator of Topic Launch
- **Jake Maymar** — name passed through as given; migrating from WordPress to Next.js
- **Never2Nervous** — screen name used; identified in transcript as Lewis Louisius (L-O-U-I-S-I-U-S); works at a Big Four consulting firm
- **Juan Torres** — name passed through as given; working on GPU inference infrastructure
- **Tom Welsh** — name passed through as given; building multi-tenant asset management SaaS
- **Alex Wilson** — name passed through as given; former fraud analyst, job searching