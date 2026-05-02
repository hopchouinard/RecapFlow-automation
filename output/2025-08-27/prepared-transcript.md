=== SESSION ===
date: unknown (transcript does not specify)
duration_estimate: ~2 hours 25 minutes
main_themes: N8N automation workflows, vibe coding in corporate environments, ShipKit course launch, ADK (Agent Development Kit) integration, Supabase/database security, Next.js hosting, LinkedIn scraping/GDPR, voice assistants, job searching, Topic Launch platform demo

---

<!--SEGMENT
topic: Session Opening and N8N Exploration
speakers: Patrick Chouinard, Marc Juretus, Paul Miller
keywords: N8N, Railway, webhooks, Google Drive, LangChain, Next.js, Digital Ocean, Postgres, automation, prototype
summary: The session opens with informal chat before diving into Marc's hands-on N8N experimentation over a weekend. Marc describes deploying an N8N instance to Railway and building webhook-driven automations including a Google Drive trigger that generates AI-written emails. Paul shares his own N8N setup on Digital Ocean at a flat $20/month cost and discusses infrastructure considerations.
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

00:01:42 - Patrick Chouinard
I have some questions for the group tonight for once.

00:01:46 - Patrick Chouinard
That's what we're kind of here for.

00:01:48 - Marc Juretus
That and some light humor here and there.

00:01:53 - Paul Miller
Or especially when a guy falls asleep during the call.

00:02:03 - Patrick Chouinard
Yeah, I gotta admit, I did about six or seven hours with N8N [tool:N8N] over that weekend, man.

00:02:08 - Marc Juretus
That's pretty damn powerful, man. I published my build on Railway [tool:Railway], which was surprisingly really easy to do.

00:02:18 - Marc Juretus
Them webhooks are pretty damn slick, man, I must say.

00:02:22 - Marc Juretus
And it's funny, like the foundation I have from the other frameworks I learned how to use — it's funny when you use that front-end tool, how much easier they are to use because of the other stuff that you've learned.

00:02:35 - Marc Juretus
I could definitely do some stuff for some realtors or something around here because just the fact that some of the webhooks I was doing were Google Drive [tool:Google Drive] — I had it that if you entered new names and addresses, as soon as you made a change, it did a route, the webhook caught it, scrubbed the email, and you had the AI build in the context of the email and build the type of response to go back without even having a non-techie involved.

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
Yeah, I was doing the thing where I was submitting like a form and then you answered a few questions and then it emailed you back a story about you. The agent's context was: take the person's name and their occupation, and I want you to write a three or four paragraph story, and then send it back to them. Pretty slick.

---

<!--SEGMENT
topic: Vibe Coding in Corporate Environments
speakers: Patrick Chouinard, Brandon Hancock, Paul Miller
keywords: vibe coding, Lovable, Cursor, cybersecurity, corporate governance, CI/CD, Platform One, business users, MCP, VS Code
summary: Patrick raises a freshly assigned challenge: integrating vibe coding tools into a large corporate environment where business users want no-code experiences (like Lovable) but cybersecurity demands control. Brandon and Paul offer frameworks including a generate-critique agent pattern and the US government's Platform One/Big Bang CI/CD pipeline approach as inspiration for governed deployment pipelines.
-->

00:05:18 - Patrick Chouinard
I've been put in the position of managing the integration of vibe coding, but in a corporate environment — managing between the desire of the business to put coding tools like Lovable [tool:Lovable] in the hands of business users, but with cybersecurity saying, wait, we want to control that thing.

00:05:51 - Paul Miller
Oil and water, I think.

00:06:04 - Paul Miller
Oh, well, you're on the right call.

00:10:14 - Brandon Hancock
And Patrick was basically asking: how do you integrate vibe coding practices inside a corporate environment — i.e., the business user wants a Lovable experience, and CyberSec wants something that they can control, and nobody realizes that vibe coding is not magic. You still need to know what you're doing.

00:10:26 - Brandon Hancock
One of the cool things that I think you can do is — at the end of the day — what you can actually quantify what cybersecurity wants, and it literally just comes down to making an insane amount of prompts. One of the main things I like to do is the generate-critique pattern with agents, where agent one does an action, and then immediately afterwards you follow it up with a critique, and then you do this cycle a few times.

00:11:42 - Brandon Hancock
You could have a cybersecurity guy come up with what he initially needs, generate an analysis of the application that they built, come up with cybersecurity critiques of it, implement the changes, and go through it a few times. Because that is one of the easiest ways to make sure that you get their requirements out of their head.

00:12:10 - Patrick Chouinard
Honestly, their concern is not as much that they don't think it's secure — because they understand that what would be vibe-coded is more prototype and proof-of-concept type of application, not a full-fledged production application. Certainly not by a business user.

00:12:37 - Patrick Chouinard
▶ I cannot give a financial analyst Cursor [tool:Cursor] and say, have at it. They're looking for the Lovable experience, the IDE-free type of development. So that's the challenge — I want to give them something, but not something they're going to break everything with.

00:13:07 - Brandon Hancock
I don't know if agents are fully there yet to where they can just build an entire application that is perfect, that meets what cybersecurity wants. It's definitely not there yet, but it 100% is going in that direction.

00:13:45 - Patrick Chouinard
The challenge is all the big consulting firms are going to them and saying, you're going to be left in the dust. And now management is extremely happy, they want to go forward, they have budget. How much do you need? Go, make that happen. But I want to make that happen so in six months it's still going to work.

00:14:10 - Brandon Hancock
▶ A very small development team joined with the cybersecurity guys could do the work of what used to be 10, you know? You're not going to get left behind as long as the few developers you are using are using the tools properly.

00:41:01 - Patrick Chouinard
The main thing I've been working on — before they asked me that — I was already working with the business to integrate MCP [tool:MCP] integration in tools. And I was working on vibe coding in a corporate environment using Visual Studio Code [tool:VS Code]. But now today they just flipped the script and said, you have the budget you need, just tell us which tool to buy and go.

00:42:13 - Brandon Hancock
So I used to work for the government, and the government actually has a process for allowing individuals — like government employees — to deploy applications that can be used by airmen. Their whole process actually revolved around making sure people used proper containers, and they did an insane amount of work in CI/CD pipelines. The goal was: if I make a CI/CD pipeline that has enough checks — make sure people didn't leak environment variables — then the lowest denominator of a developer shouldn't be able to break something. That was their standard.

00:45:26 - Brandon Hancock
▶ It's called Platform One [tool:Platform One], and there's two things called Party Bus and Big Bang. Big Bang is the platform that has the CI/CD pipeline. They had six templates — these are the only allowable pipelines. From template to pipeline to deployed app, these are the only six verticals we support. [link:Platform One / Big Bang public repositories]

00:47:23 - Paul Miller
Having worked for quite a few very large corporates — Ernst & Young, Suntory — I can understand. One of the most successful methodologies I saw is: instead of stressing out your poor dev teams, get your business analysts, your SAs, so they sit as those customer-facing resources. Do a Dragon's Den pitch — what you'd call a Shark Tank — where you consolidate down the list of cool vibe projects. Facilitate the ideas, get it to a shortlist, and then assign a group of BA/SAs to help hone it.

00:50:12 - Patrick Chouinard
It's just that normally the BA and the PO always use the "it's not in the budget" excuse. This time it's like open budget — do whatever you want. So how do I temper the business not to spend stuff that's not going to come back as value?

00:51:39 - Paul Miller
▶ Do a Shark Tank, and you have these groups coming up pitching ideas. Tell the Shark Tank guys, here's the criteria: is it going to increase sales, save time, save money? Then that gets the shortlist. Then you can do what Brandon's talking about in terms of building that framework.

---

<!--SEGMENT
topic: ShipKit Course Launch Update
speakers: Brandon Hancock, Paul Miller, Tom Welsh, Alex Wilson, Jake Maymar
keywords: ShipKit, prompt-driven development, RAG template, ADK agent, LangChain, Next.js, course launch, roadmap generation, TypeScript, Python
summary: Brandon provides a progress update on ShipKit, a prompt-driven course and boilerplate toolkit for building AI applications. He describes its template-based approach covering RAG, chat, and ADK agent patterns. Multiple attendees share positive early feedback, and Brandon outlines upcoming additions including LangChain templates, a TypeScript course, and a Python course.
-->

00:06:34 - Brandon Hancock
So before we kick it off, I want to show you guys what cool things I've been working on. Long story short, from dawn to dusk, knocking out ShipKit [tool:ShipKit], so I just want to show you guys a quick progress update.

00:07:16 - Brandon Hancock
Everything in here, when it comes to making apps, is prompt-driven, which I think is so cool — because one of the coolest things about making apps is you're always staring at a blank screen, but now prompts do all the hard work for you, from coming up with the ideas to doing all the hard work for you.

00:07:52 - Brandon Hancock
▶ Not only is there the course, there's the actual prompt that does all the hard work for you and walks you through it. And then to make it even easier, I'm showing how to take each template — the RAG template [tool:RAG], the chat template, the ADK agent [tool:ADK] — and convert it into your own custom application. So literally everything has a course, a prompt, and multiple examples.

00:08:15 - Brandon Hancock
I think this is how all courses will be in the future. I think being in AI, we're kind of ahead of the curve.

00:08:54 - Brandon Hancock
For ShipKit, I also did a few videos for Gemini CLI [tool:Gemini CLI] recently. If you guys have any questions on that, super happy to dive into that one as well.

00:29:54 - Paul Miller
I downloaded ShipKit and watched the video. Wow. I'm just so excited. I've just got to create time to have a go at that. I love what ShipKit's all about, and I love the methodology and how you've concentrated it nicely into the product.

00:30:33 - Brandon Hancock
One of the things I really want to work on post-launch is a TypeScript [tool:TypeScript] course for you guys, a Python course, and just a straight-up vanilla Next.js course, just because there's still a lot of people who are very strong in one area and not another. That'll probably be October, because the next 20–25 days are busy.

00:57:59 - Tom Welsh
I just want to reiterate what Paul was saying about ShipKit. Absolutely awesome. I obviously signed up for it, downloaded it. I've already pulled all the rules across and thrown it into my asset management thing. Ran it, checked my code — it was 95% compliant. I thought, yeah, I'm happy with that.

01:57:11 - Brandon Hancock
The thing that I think you're going to like so much better — the biggest one I just added — is it makes a roadmap. Going from a rough idea, getting all the core ideas out of your head and into a system, what this does is it takes everything you just thought of and turns it into a roadmap. Phase two, authentication — it walks you through it. You just copy and paste: "I'm on phase three," paste, and now it's like, make a task template to do this. It actually lays out the next steps too.

01:31:39 - Brandon Hancock
▶ Shipkit.ai [link:shipkit.ai] — if you're looking to just build faster, I really would recommend ShipKit, because you have an idea, you have a very valuable idea. Let's just make it look beautiful, let's get it out to the world fast, and go forth.

---

<!--SEGMENT
topic: LangChain vs. Other Frameworks for Enterprise
speakers: Brandon Hancock, Juan Torres
keywords: LangChain, LangGraph, ADK, N8N, agentic frameworks, enterprise, job postings, nodes, edges, graphs, beginner-friendly
summary: Brandon addresses Juan's pre-submitted question about whether LangChain and LangGraph dominate enterprise job postings. He confirms LangChain is highly in-demand at larger companies and explains why ShipKit starts with simpler frameworks before introducing LangChain, which requires understanding nodes, edges, and graphs.
-->

00:09:19 - Brandon Hancock
So Juan was basically asking: it seems that most industry prefers LangChain [tool:LangChain] and LangGraph [tool:LangGraph]. Do you feel like this is the case? I see the modus operandi agentic framework requested in job postings.

00:09:38 - Brandon Hancock
<Q>Is LangChain and LangGraph the dominant framework in enterprise job postings?</Q>

<A>Yeah, definitely on bigger enterprise companies, yes, they are more involved and probably more in demand. So one of the big things — literally the next thing in the queue — is to add in a LangChain version, just because I think it is one of the most in-demand. It's just that N8N is so easy to get going and get using, that we definitely wanted to make it a little bit more beginner-friendly, so that's why it's first. In the big boys, when you have more time and you understand nodes, edges, graphs, that's when LangChain really comes in.</A>

---

<!--SEGMENT
topic: Student AI Use Case and Education
speakers: Adam, Brandon Hancock
keywords: ChatGPT, Python code generation, scheduling optimization, constraint solving, education, AI literacy, data parsing
summary: Adam shares a story about his daughter using ChatGPT to solve a complex class-scheduling optimization problem involving chained swaps across multiple courses. ChatGPT generated and ran Python code to find a feasible six-swap solution, which her academic advisor approved. The discussion broadens to AI literacy in education and the risk of students being left behind.
-->

00:14:33 - Brandon Hancock
And Adam, basically you were saying — I guess your daughter yesterday — Adam, do you want to hop in on that?

00:14:48 - Adam
Yeah, so my daughter called yesterday and she wanted her class schedule changed. She had a list of her current schedule and basically a list of how many students are in each class and each subject. She's swapping classes — swap this for that — but she quickly realized that after you get a chain of like four or five, you just can't hold that in your head mentally.

00:15:47 - Adam
So she couldn't figure out how to do this manually. She takes all the information from her school, uploads it to ChatGPT [tool:ChatGPT]. And the problem she ran into — well, first, she didn't realize that ChatGPT can generate Python and run it.

00:16:09 - Brandon Hancock
Light bulb moment, yeah.

00:16:10 - Adam
And then she was actually pretty good. Without reading any of the code, she realizes that she had data input problems — the graph was cut off when she screenshotted it and stuff. But they kept saying it was infeasible. And then I looked, and she actually had problems with the way the university listed it — the spring semester and the fall semester had the columns in different orders in the two tables. This was confusing the parser.

00:17:00 - Adam
So once I fixed that, it generated the Python code, ran it, we had to add some more constraints, generated more Python code, ran it again, and if she swapped six classes, she could get to the schedule she wanted. She went to her advisor with that proposal, and the advisor said sure.

00:17:31 - Brandon Hancock
▶ I think in China right now, at the age of like six, they have to start using AI to do stuff. If you're not using it, your output is drastically lower than someone who is. I hope the entire education system starts using it, one way or another, because if not, we're hosed.

00:18:07 - Adam
It seems like a big thing with education is everyone's just talking about kids cheating on stuff. But the kids just figure out how to do things.

---

<!--SEGMENT
topic: N8N Workflows and Deployment for Client Work
speakers: Marc Juretus, Brandon Hancock, Paul Miller
keywords: N8N, Railway, webhooks, Google Drive, automation, prototype, small business, fantasy draft, deployment
summary: Marc gives a detailed update on his N8N weekend deep-dive, describing webhook automations including a Google Drive trigger for email generation and a form-to-story pipeline. He outlines his plan to build a demo "fake company" site showcasing AI capabilities — job applications, resume screening, inventory chat — to use as a portfolio for prospective clients. Brandon reinforces N8N's value as rapid-prototype glue for businesses.
-->

00:18:45 - Brandon Hancock
Marc, you're up first, man.

00:18:57 - Marc Juretus
So what I was working on — I engulfed myself with about seven or eight hours of N8N, so I was practicing with the webhooks, because if I ever try to do some work on the outside, I'm not going to build a LangChain/LangGraph flow or a complex project. I can probably accomplish something if there's some small businesses or customers that would want to work with me.

00:19:22 - Marc Juretus
I was pretty impressed with the webhooks. I was doing the forms — having forms submit where you pass the name and where you worked, and then I had the AI write a four-paragraph story about you. I see a lot of capabilities with that.

00:19:52 - Marc Juretus
The one with the Google Drive was what impressed the hell out of me — where I had a sheet, you made a change to the sheet, it triggered that webhook, and then it struck out a custom email based on what was in the subject and the body. I could see a ton of usages for it.

00:20:12 - Brandon Hancock
▶ It is insane how easy it is to get started with N8N and the amount of value you can add in like two hours to any business with N8N. N8N can become the glue of the business to handle everything — every time this happens, trigger this — and then go build an insane automation.

00:21:06 - Marc Juretus
After that, I obviously have the fantasy thing done. So the next thing is I want to build a bogus company where I'll have jobs listed where you apply for a job, it'll respond to the resume, see if you were qualified or not, it'll send you a bogus appointment for an interview. I'll have a chat that runs inventory as well as answers questions. So if somebody asks, what have you done with AI? Here, go to this bogus site. You can apply for a job, look at our inventory listing.

00:21:38 - Brandon Hancock
▶ You're setting yourself up for success, man, because the second you can start to do it for yourself, then you can show it to others. They're like, okay, you look competent. They throw you a small project and then you're off to the races. You're literally in the hardest part — showcasing that you know how to use the skills and landing that first real-world client. Everything after this gets so much easier.

---

<!--SEGMENT
topic: Webhook Data Limits and Supabase Security
speakers: Mitch, Brandon Hancock
keywords: webhooks, Supabase, Drizzle, row-level security, Firebase, Next.js, Vercel, JSON payload, API endpoints, database security
summary: Mitch asks about webhook payload size limits when sending large JSON objects to trigger background workflows, and also raises a Supabase warning about unrestricted database access. Brandon explains best practice is to send only IDs via webhook and reconstruct data server-side, and clarifies that Supabase's RLS warning is irrelevant when using Drizzle ORM through structured API endpoints rather than the Supabase client directly.
-->

00:22:28 - Brandon Hancock
All right, Mitch, you are up next.

00:23:47 - Mitch
My main question is: for webhooks, is there a general guideline for how much data I can send via a webhook? And Supabase [tool:Supabase] — I was trying to find any resources on it, and I couldn't.

00:24:12 - Brandon Hancock
<Q>How much data can you send via a webhook, and what are Supabase's limits?</Q>

<A>Usually, a webhook — whatever logic you had in your application that was putting together that huge JSON object — you usually move that into the very first step inside your backend code. So instead, what you'll do is send in the webhook with just, hey, here's the job ID, here's whatever. Then once it receives the request, it goes, okay, I know step one is to build out that monster JSON object. Usually best practice: you don't want to send an insane amount of data. However, the internet specifically — REST protocols — could easily handle a few hundred kilobytes, even up to a megabyte. I know Next.js and Vercel [tool:Vercel] itself has a one or four megabyte default stopping point.</A>

00:25:56 - Mitch
Yeah, and Supabase, because I think they're the ones sending the data too. And I think they might have a limit. So I was going to test with N8N just real quick, instead of doing the whole Google Cloud Functions thing. And then yeah, I guess the solution is just send the IDs.

00:26:02 - Brandon Hancock
▶ Yeah, because it sounds like you already had the logic, because it was already building it one time, so now just actually move that build logic into the background job that was actually going to run it, and then you don't even have to worry about size limits because you're literally sending over like 30 characters.

00:26:21 - Mitch
And then the other question I have — Supabase has been messaging me about, oh my gosh, your databases are like unrestricted.

00:26:40 - Brandon Hancock
<Q>What does Supabase's "unrestricted database" warning mean?</Q>

<A>What normally happens is you can create a Supabase client, and a lot of times people will literally allow users to use that client throughout their application, which allows them to almost write queries and request data — which is why it's saying it's unrestricted. So if you were to create that client and allow your users to fetch information, yes, the data is unrestricted and they could get your information, they could get mine, they could grab everyone's information from the users table.</A>

00:27:42 - Brandon Hancock
▶ What we're doing is we do not use the Supabase client unless it's in a pre-structured API call, a pre-structured query, or a pre-structured mutation. So there's no way the user can ever access that differently. I wish there was a button to turn it off saying, I'm not using that feature of Supabase.

00:28:15 - Mitch
I just use Drizzle [tool:Drizzle] and I have things over REST.

00:28:28 - Brandon Hancock
▶ Perfect — so you're already doing it to where the user is using Drizzle to make a request to your backend database. You're not using the Supabase client to access that table. So that's why I said I wish you could turn that off — because you're safe, you don't have to worry about it.

---

<!--SEGMENT
topic: Next.js Hosting Options and Python Frontend Question
speakers: Paul Miller, Brandon Hancock
keywords: Next.js, Python, TypeScript, Vercel, Gradio, ShipKit, server-side rendering, SEO, frontend frameworks, hosting
summary: Paul asks whether ShipKit will support Python-based frontends for developers who are more comfortable in Python than TypeScript. Brandon explains why Next.js is the dominant standard for production frontend applications in 2025, noting AI models have extensive training data on it, while committing to future Python and TypeScript standalone courses.
-->

00:29:02 - Brandon Hancock
And then, just to answer your question, Paul — will you provide Python path frontends as well?

00:29:14 - Paul Miller
<Q>Will ShipKit support Python frontends, like Gradio or similar, for developers who prefer Python over TypeScript?</Q>

<A>Yeah, so the key thing here is what is the most common real-world tool that people are using. And most — at this point, if you're trying to build a front-end application in 2025, it is done with Next.js. I think it's an insane amount of all new real-world applications are using it, just because it's so easy to use, it's so standard, there's so many support documents. What's also great about it is AI truly understands Next.js this day and age, because there's so much training data on it, so it can do a much better job too. Even though TypeScript is definitely a little bit more of a steeper learning curve, AI really does handle a lot of it for you.</A>

00:30:51 - Brandon Hancock
▶ Stick with Python back-end, and come on, Paul, make the jump — it's cleaner, it's better, let's just do it.

00:31:00 - Brandon Hancock
One of the things I really want to work on post-launch is a TypeScript course for you guys, a Python course, and just a straight-up vanilla Next.js course. That'll probably be October, because the next 20–25 days are busy.

---

<!--SEGMENT
topic: Juan's VPN and GPU LLM Infrastructure
speakers: Juan Torres, Brandon Hancock
keywords: Tailscale, VPN, Windsurf, GPU, NVIDIA A100, LLM inference, Vertex AI, Elastic Beanstalk, Vercel, API proxy, token throughput, Oculus servers
summary: Juan shares a breakthrough: he established a VPN connection to a client's server using Tailscale binaries without admin permissions, enabling use of an agentic IDE remotely. He also built a GPU stress-testing dashboard showing 72 tokens/second throughput on an NVIDIA A100 running an 8B parameter model. The discussion covers how to expose the on-premise LLM inference endpoint to external applications via a secure API proxy.
-->

00:31:56 - Brandon Hancock
Juan, you're up next, buddy.

00:32:05 - Juan Torres
Yeah, so last week I was able to resolve the great issue that my client was facing. I found a way to create a VPN secure connection between the Oculus server and my local computer without having administrative permissions. What I did — I simply downloaded the binaries for the Tailscale [tool:Tailscale] VPN service inside the permanent, persistent file system within the computer through their servers. And through that, now I'm able to use Windsurf [tool:Windsurf] and an agentic IDE on the server without having to go through the primitive use of VS Code.

00:33:51 - Juan Torres
Technically speaking, they were going to charge him like $7,500 for hiring a team of three to four developers. I still have to make the API or URL infrastructure in order to make the recall to whatever application or deployment method they're going to use. But now that I have the connectivity issue resolved, I think that's going to be pretty easy.

00:34:22 - Juan Torres
Yeah, and it was such good attribution that even the owners of the servers — Oculus — told me, hey, can you actually come over and teach us how to do this? Can you teach our co-op members how to make the connection to the agentic IDE?

00:34:43 - Brandon Hancock
I hope that's what you said: I'd be happy to — for a fee.

00:35:00 - Juan Torres
Additionally, I was able to create an infrastructure to be able to test the GPU LLM infrastructure. So I created a quick dashboard that allows me to stress test the GPU and then be able to assess the token utilization of the model inside the virtual environment. This is going to help me facilitate the process of A/B testing several models.

00:35:45 - Brandon Hancock
<Q>I see NVIDIA A100 [tool:NVIDIA A100], average throughput 72 tokens per second — is that expected? I would think that would hopefully be like 300.</Q>

<A>The tests were based on prompts. The model I'm using is an 8 billion parameter one. So I guess the GPU could take even more heat if it wanted to. But so far, the GPU inference of 8 billion parameters seems to be feasible — doesn't thermal throttle or anything like that.</A>

00:36:50 - Juan Torres
If anyone has information on developing an API/URL connection that I can use for the inference to the LLM, let me know.

00:37:06 - Brandon Hancock
<Q>So this is running in a private virtual network, and we're trying to expose it to the outside world?</Q>

<A>I think you will just set up almost like a proxy — a secure proxy. All it does is say, hey, I'm receiving requests from the outside, I do have secure access to the private network, and I need to make sure that the person is authenticated through some sort of API key. Every person we want to use this gets an API key, and then just in the header, we say, do they have an API key? Great, this is now a valid request. Go forth.</A>

00:39:24 - Brandon Hancock
▶ Please keep us posted. If next week you could do a demo or wireframes of how you're setting it all up, I think that could be a really cool quick overview of how it all works.

00:39:54 - Juan Torres
What I could do is get credits from the server providers to an A100 GPU, and then rerun this whole thing on my own server, on my own computer, and then just record the whole process for YouTube.

---

<!--SEGMENT
topic: ADK Integration with Django Application
speakers: Ola Oyo, Brandon Hancock
keywords: ADK, Google Agent Development Kit, Django, Vertex AI, Google AI Studio, Docker, GCP, Python, property management, session management, context-aware agents
summary: Ola, a new attendee building a property management platform, describes integrating Google's ADK directly into a Django application rather than running it as a separate microservice. Key challenges include authenticating to Vertex AI within Docker and handling Google Workspace policy restrictions on API key generation. Brandon recommends embedding ADK in Django using the runner.run() pattern and setting Vertex AI to false to use a direct API key.
-->

01:03:23 - Brandon Hancock
Ola, you're up next, buddy.

01:03:29 - Ola Oyo
Hey, Brandon. I went to bed one night trying to figure out how I was going to integrate ADK [tool:ADK] into my Django [tool:Django] app. I wake up the next morning and YouTube suggested you. So yes, it was meant to be.

01:04:03 - Ola Oyo
So I took most of last week, I dug into the ADK kit course. It was very helpful. But I think I have come to a bit of a snag. I'm building a property management platform for estate managers, and I'm trying to integrate the aspect into it to be context-aware. The service is running on Django, and I had spent a large part of last week trying to run it as a separate service. But looking at a bunch of Medium posts, they said it's better to integrate the ADK directly in Django.

01:04:58 - Ola Oyo
Just before this call, I've been battling with GCP [tool:GCP], tried to get my Vertex AI [tool:Vertex AI] to work locally within my Docker [tool:Docker] container, and then I was also just trying to get the API key. I said, you know what, to hell with Vertex. I'm just going to get the API key directly. And then because I'm using my organization, Google Workspace [tool:Google Workspace] is giving me a whole bunch of challenges — policy not allowed, blah blah blah.

01:05:49 - Brandon Hancock
<Q>Are you trying to run ADK on a separate port and have Django call it, or are you trying to embed ADK entirely inside Django?</Q>

<A>So it's the latter — I'm trying to have the ADK run directly in the Django application.</A>

01:07:00 - Ola Oyo
While I was trying to run the ADK separately, the problems I had were authentication and having to recreate all of my ORM and Django on the ADK again, just so that the ADK is context-aware of the specific user and the information it should be getting from the table. So even that was just too much of a headache, and then it was like, just have your ADK sit directly inside Django — it just makes it easier.

01:07:34 - Brandon Hancock
▶ The quick answer to solve the context issue is when you're actually creating sessions in ADK, you can actually set initial state — user ID, whatever. So I'll create a session, I'm user ID, his name is Bob, here's whatever else you want. Then whenever you start sending in messages, you pass everything in as, you know, working for user, username — like greet, make sure you greet the person.

01:08:48 - Brandon Hancock
▶ The cool part is, if you are hosting it inside of your Django application, you never have to worry about anything with deployment, because it's in your Django app. You literally just have to call `runner.run`, and that's it. You're going to create a session, and once you have a session, you're just going to call this. You don't have to handle these events to start to stream out through an API call back to your Django app.

01:13:00 - Brandon Hancock
<Q>How do I get past the Vertex AI authentication issue in Docker?</Q>

<A>The easiest way to get it up and working is to create a project in Google Cloud, make sure you have billing set up, and then set your environment variables to `VERTEX_AI=false`. Then paste in that Google API key. Vertex has to be equal to false for it to detect your API key.</A>

01:14:57 - Brandon Hancock
▶ Hey, even if you make a personal account and put in $5, it will last you a very, very long time. So it might be worth just getting around the headache for $5.

01:16:44 - Ola Oyo
And you know, real great work on what you've done on ADK, because I went through the Google modules, and they're nowhere close to what you put out, to be honest. So they should be paying you.

---

<!--SEGMENT
topic: Multi-Tenant SaaS Architecture and Database Migration
speakers: Tom Welsh, Prem, Brandon Hancock
keywords: multi-tenant, Supabase, Drizzle, Vercel Postgres, row-level security, Firebase, enterprise database, Clerk, WorkOS, Auth0, blob storage, pre-signed URLs
summary: Tom describes converting his asset management tool into a multi-tenant SaaS product with per-organization databases for enterprise and shared databases for lower tiers. Prem discusses migrating from Vercel Postgres to Supabase and asks about Clerk vs. Supabase auth for organization management. Brandon explains Supabase's RLS warning in context of Drizzle usage, covers blob storage security with pre-signed URLs, and recommends WorkOS for enterprise SSO and organization management.
-->

00:58:00 - Brandon Hancock
All right, next up is Tom.

00:58:12 - Tom Welsh
I just want to reiterate what Paul was saying about ShipKit. Absolutely awesome. I've already pulled all the rules across and thrown it into my asset management thing. Ran it, checked my code — it was 95% compliant.

00:58:48 - Tom Welsh
On the asset management side, I'm now trying to turn it into a product. With multi-tenant — so stand-alone database or shared databases, basically, for backends. I'm trying to extract myself from where I was and get some current settings set up so you can actually define as you set up and go in — like a web admin type interface to set up your database and everything.

00:59:27 - Brandon Hancock
<Q>Are you setting up a database per organization?</Q>

<A>I'm going to do database per organization for enterprise. I'm going to do shared multi-tenant shared database for cheaper versions.</A>

00:59:52 - Tom Welsh
And my security head's going, I don't like shared databases. Data leaks.

01:00:07 - Brandon Hancock
If you look at most recent big leaks that get talked about, they're usually using Firebase [tool:Firebase]. When they were using Firebase, that rule — the unsecured one — it's because they literally have a Firebase client that can technically, the second it has the right key, access the entire database. All it takes is a developer who knows, oh, I can see they're making a request to this URL, great, I can now get anything.

01:01:02 - Tom Welsh
Yeah, so I was looking at row-level security on Supabase, but I haven't really dug into that much. But I take it that's just literally — you're authorized to run that query against that part of the database and that part only, so you don't get information slippage.

01:01:24 - Brandon Hancock
▶ Yeah, and it's strictly when you're using the Supabase client to access the database. And I think you're using Drizzle, which — so it doesn't apply. You're literally in two different universes.

01:17:20 - Prem
What I did was I moved from Vercel [tool:Vercel] as the database and moved it to Supabase. I'm using Drizzle ORM. So the role-level security disabled is a constant thing I get in Supabase. I assume — as long as I'm using Drizzle ORM and my API endpoints take care of the security — it should be fine?

01:18:09 - Brandon Hancock
<Q>What should I consider when migrating from Vercel Postgres to Supabase?</Q>

<A>High level — it's more affordable. Vercel's blob storage fees are pretty high now that they're out of beta. And their database hours per month was very low, which made it a more expensive option. So no, I think you're going to love the Supabase experience much more. Security risk — as long as you're using Drizzle to make structured queries to your database, and before that Drizzle command is sent off, A, is the person authenticated? And B, are they authorized to make the request? Check, check. You're great to go.</A>

01:19:31 - Brandon Hancock
▶ When you are using Supabase, there's a concept of pre-signed URLs. Before generating a pre-signed URL, you want to make sure the person asking to get the blob is allowed to do it. Then you're good.

01:20:24 - Prem
I started using Clerk [tool:Clerk] for user authentication and user management. And I saw that Supabase has user processes as well. One of the things I've found is Clerk has more like user and organization management — like if you want to have users and organizations — they have new features. That's the reason I'm sticking with Clerk. Do you have any inputs on Supabase versus Clerk for user management?

01:21:13 - Brandon Hancock
<Q>Should I use Clerk or Supabase auth for organization management?</Q>

<A>Clerk is definitely adding a lot. I'm a big fan of simplicity just because — what is, are all the additional benefits worth the extra effort? Most of the time, really, you just want people to be able to log in. Supabase allows you to do Google, GitHub — it allows you to do all of them. Or you could actually add in Auth0 [tool:Auth0] and WorkOS [tool:WorkOS]. I think Supabase also has an integration for Clerk, to where you can actually hook up Clerk to work with Supabase.</A>

01:23:10 - Brandon Hancock
▶ Final recommendation: I've heard nothing but amazing feedback on WorkOS. I believe they already have enterprise SSO set up. They also have organizations. Before you make a pick, I would 100% look at setting that up, doing a side-by-side. It is more expensive, it is more enterprise grade. WorkOS is probably one of the best options if you're going to go down that path.

---

<!--SEGMENT
topic: Topic Launch Platform Demo and Creator Feedback
speakers: Jaylen Davis, Brandon Hancock
keywords: Topic Launch, YouTube, content creation, crowdfunding, Kickstarter, creator economy, ShipKit, community voting, monetization, Instagram
summary: Jaylen demos Topic Launch (topiclaunch.com), a platform where fans fund YouTube video ideas — fans propose topics, set funding thresholds, and creators receive 90% of funds upon delivery within 48 hours. Brandon provides detailed creator-perspective feedback, suggesting a subscription-based community voting/signal model would be more practical than the current commission-based funding model, as creators often cannot commit to arbitrary topics on short timelines.
-->

01:24:41 - Brandon Hancock
Jaylen, you're up next, buddy.

01:24:52 - Jaylen Davis
So I spoke with you maybe a month and a half ago. I have a platform that I was creating that you seemed to really like. It's called Topic Launch [tool:Topic Launch]. I actually got it done. Me and my business partner just started creating user-generated content on Instagram.

01:25:23 - Jaylen Davis
That was mostly just coming to let you know if you were interested in hopping on the platform. I actually even created an account for you.

01:25:30 - Brandon Hancock
<Q>What URL do I go to?</Q>

<A>Topiclaunch.com [link:topiclaunch.com]</A>

01:25:43 - Jaylen Davis
Basically, YouTubers monetize their audience by fans funding content ideas for them. A fan creates the topic, the community backs the topic if the fan doesn't fund it to the fullest, and then you deliver the video. Within 48 hours you receive 90% of the funding while Topic Launch takes 10%. Very simple and straight to the point. It saves you from running out of ideas and from creating videos based off of ideas that you thought were going to pop and they actually flopped.

01:28:16 - Brandon Hancock
Yeah, it's like Kickstarter [tool:Kickstarter], but for actual YouTube content. I absolutely love the idea.

01:28:34 - Brandon Hancock
Main qualms — serious feedback: for example, the Django video. It would be hard if I was asked, hey, for $400, make a Django video. That would take me forever to spin back up on Django, then do it. So like, serious feedback — dude, let me, as the creator, just pay 30 bucks a month, 40 bucks a month, whatever the number is, and just allow me to put idea topics out there, and community thumbs up, thumbs down, or community suggests their own videos and thumbs up, thumbs down.

01:29:09 - Brandon Hancock
▶ That is so much more valuable, because there are some times where, even if I have a sponsorship deal, for the next week I'm busy working on that video. I legitimately could not take on another video. But just allowing the community to let me see signal versus noise would be super helpful.

01:29:46 - Brandon Hancock
I wouldn't want to take people's money knowing I could not, most of the time, deliver on the timeline. And I would hate to set false expectations of like, oh yeah, I'll make a video on anything — because a lot of times people ask about topics that are outside my channel umbrella.

01:30:09 - Brandon Hancock
▶ Just letting it be pure thumbs up, thumbs down would be insanely helpful. And a creator paying $30 a month — that easily would pay for that.

01:30:37 - Jaylen Davis
<Q>If I just so happen to eventually pivot to that way of the website — is there something that you would sign up for?</Q>

<A>Dude, give you 30 bucks right now. Yeah.</A>

01:32:00 - Brandon Hancock
▶ As a creator right now, I have to guess — does the community want a LangGraph video? Do they want an ADK video? Do they want a deeper dive into ADK? You literally take the guesswork out of content creation, which is beautiful. Right now I have to look at comments, there's so much work that goes into getting a sense for what direction people want to go. This would just be: I literally just look at the top two and I'm like, cool, I'm making video one today.

---

<!--SEGMENT
topic: Next.js Hosting, LinkedIn Scraping, and MCP Compliance
speakers: Jake Maymar, Brandon Hancock
keywords: Next.js, Vercel, Netlify, WordPress, Namecheap, Mailgun, LinkedIn API, Apify, GDPR, MCP, OAuth, scraping, domain setup
summary: Jake asks about hosting options for migrating from WordPress to Next.js, and Brandon recommends Vercel for its seamless Next.js integration, SSR/SEO benefits, and easy domain setup. Jake then raises two compliance questions: how to scrape LinkedIn public profiles in a GDPR-compliant way (exploring Apify and other scrapers), and whether MCPs can be made GDPR-compliant. Brandon explains MCP compliance reduces to controlling what data is stored and ensuring log deletion capability.
-->

01:32:45 - Brandon Hancock
It looks like Jake was next.

01:32:59 - Jake Maymar
First of all, the ShipKit is amazing. I've already written so many things using it. And I've also altered the prompts — it's such a good starting place.

01:33:30 - Jake Maymar
I'm revisiting my website, which is WordPress [tool:WordPress], and I finally just decided I'm done — switching completely to Next.js. I actually really like building things in it. So I'm curious, what should I host it on? I've been looking at Netlify [tool:Netlify]. And I'm using SiteGround right now, but they don't really host Next.js. I keep hearing about Hostinger [tool:Hostinger]. Is there any one you would recommend?

01:34:22 - Brandon Hancock
<Q>What hosting platform should I use for a Next.js site migrating from WordPress?</Q>

<A>The easiest one, especially if you're hosting a single project — Vercel. You literally just say deploy app, you point to your GitHub project and it's done. It actually does the full process of distributing the application, because it understands this is Next.js code, so it can actually server-side render a lot of this stuff to make the static pages look better. Big fan of Vercel. And even if you went pro to get a lot more additional features, it's $20 a month. But if this is your first app, on the hobby tier — completely free — you're going to get everything.</A>

01:35:25 - Brandon Hancock
▶ When it comes to setting up your own domain — here was my default ShipKit application, I added it in, it gave me a few commands to pass over to Namecheap [tool:Namecheap] where I bought the domain, and then boom, you're now using your own URL. For mail — you'll create a Google business account and set that up. I think it's like $7–$8 a month to get that business email. And then if you want to get some automated emails sent out, Mailgun [tool:Mailgun] would be my default recommendation.

01:36:45 - Jake Maymar
I'm already using OAuth, already signed in with LinkedIn [tool:LinkedIn], so I have name, title, and image. But LinkedIn doesn't give you access to much with default permissions. I actually want to get the full profile information. I've been thinking about using Serper [tool:Serper], but it has to be GDPR-compliant, so it has to only be public profile data. I'm curious if you're aware of a good approach.

01:38:24 - Brandon Hancock
<Q>Is there a GDPR-compliant way to scrape LinkedIn public profile data?</Q>

<A>There's a specific one — I'm drawing a blank for the name. There's Apify [tool:Apify], which is like okay, but I'm worried about the compliance issues. The LinkedIn API is a beast. It works very well when you're just trying to do your own post or your own profile. It's the second you want to start doing other people's stuff that I remember having a ton of issues. I would be curious if you did a ChatGPT deep research on it — what it would say about GDPR compliance for public profile scraping.</A>

01:41:38 - Jake Maymar
<Q>Is there a way to make MCPs GDPR-compliant? Because MCPs are definitely like Wild Wild West.</Q>

<A>At the end of the day, an MCP [tool:MCP] is nothing more than a function call that has been wrapped to be accessible to agents. So the real question is: is your underlying task — whether that's scrape data or whatever — storing things that are okay? And it's okay with the logs that are generated. With GDPR, one of the big requirements is to be able to delete data too. If you get an email, you have so many days to delete data. So you also just need to have control over your logs to make sure that you can delete them.</A>

01:43:35 - Jake Maymar
That's actually really, really helpful. Because yeah, I was just trying to get my head around it and understand that a little bit more.

---

<!--SEGMENT
topic: SaaS Factory App and Authentication Debugging
speakers: Never2Nervous (Lewis), Brandon Hancock, Prem
keywords: SaaS factory, Next.js, Google Cloud, Supabase, authentication, OAuth, middleware, GitHub OAuth, Google OAuth, Neon, Clerk, Upload Thing, Base44
summary: A new attendee (Lewis, data science background) describes building a SaaS factory platform — similar to Base44 — that takes submitted ideas, generates production-ready apps, and handles automated marketing. He has been stuck for three weeks on an OAuth routing bug after Google/GitHub login. Brandon diagnoses the likely issue as missing or misconfigured Next.js middleware that fails to consume the OAuth response headers, and recommends migrating to Supabase auth for its built-in middleware.
-->

01:44:45 - Never2Nervous
Hello, everyone. Hey, Brandon. So this is my first call, and I've been having some trouble with the application I'm trying to deploy.

01:45:03 - Never2Nervous
Background is in data science, so I'm a complete novice when it comes to front-end application consumer products.

01:45:17 - Never2Nervous
The application I'm building is a SaaS factory. Pretty much the idea behind it is: some of these large corporations have the funds and resources to throw a bunch of ideas against the wall and see what sticks. What if I could template that process and automate it — give people the ability to submit ideas, have it production-ready and deployed, and I also have some agentic workflows that handle automated marketing to get the idea out there into the world.

01:46:08 - Never2Nervous
Base44 [tool:Base44] is pretty much my direct competitor.

01:46:23 - Never2Nervous
I've been having this issue with authentication. I've just been going in loops with it for like three weeks. I do Google Authenticator and GitHub Authenticator for those two options. It seems to be like a routing issue — so once you log in, it doesn't route you back to the page for some reason.

01:47:24 - Brandon Hancock
<Q>What's the tech stack?</Q>

<A>Next.js, Google Cloud for the database — I spun up a database in Google Cloud Platform.</A>

01:48:20 - Brandon Hancock
<Q>What's causing the OAuth routing loop after login?</Q>

<A>I think the issue is when you actually get the credentials from Google, what it's doing is in the header of the response, it's including the client token, it's including so much information in the return — the user's token, a page to redirect to afterwards — it has all the information set up. But if your middleware is not properly set up to handle that, it's not going to take action on all the information you get back. So then you end up in a loop where nothing actually is happening. The reason why I keep recommending Supabase is because it comes with middleware that is set up to consume all that information and properly log you in.</A>

01:48:41 - Brandon Hancock
▶ I would stay away from raw Google Cloud unless you have to actually use it. There are simpler solutions that are basically free. If you wanted a very simple app that had authentication, a database, a blob store — Supabase [tool:Supabase] is awesome. If you don't like Supabase, you could use Neon [tool:Neon] for your database — super generous free tier. You could use Clerk for auth. For a blob store, Upload Thing [tool:Upload Thing] is a great choice.

01:53:47 - Brandon Hancock
▶ I would just check out full-stack application videos with auth. People have solved these problems in the past. I would watch — here's a playlist that literally walks through Next.js plus Supabase. I think it's video three in that series that has the exact step you need to follow. [link:Next.js + Supabase full-stack playlist]

01:54:24 - Prem
I think your course on the AI full-stack marketing platform solved a lot of problems for me. It kind of solved all the full-stack, end-to-end needs for the SaaS I was building. So I just want to throw it out there.

01:55:03 - Brandon Hancock
▶ Hey, if you can wait 25 days, dude, all this will be built for you automatically. These problems are already solved in ShipKit. Key thing — I would just simplify. Right now you're using very big-boy tools made for enterprise. If we could just bring it back down to stuff made for more like solo developers, that would help a lot.

---

<!--SEGMENT
topic: ADK Multi-Agent Routing and Voice Assistant Options
speakers: Hemal Shah, Brandon Hancock, Tom Welsh
keywords: ADK, multi-agent, sequential agent, parallel agent, orchestrator, FastAPI, server-side events, JSON, LiveKit, Gemini Live, Bland AI, 11 Labs, voice assistant, chat UI, routing
summary: Hemal describes building a rich interactive chatbot with structured HTML responses (dropdowns, calendar pickers) using ADK multi-agent workflows, including a completeness-check routing pattern. Brandon points to Google's ADK browser agent example as a reference for phase-based orchestrator prompts. Hemal also asks about standard JSON schemas for chat API communication and voice assistant tool recommendations; Brandon recommends LiveKit for voice and suggests using Gemini Live directly over ADK's voice wrapper.
-->

02:11:32 - Hemal Shah
Yeah, I'll be quick. I continued working on my interactive chat application. So it's your plain text request-response, but there are rich content media on your chatbot — you can have rich HTML elements, dropdown, calendar picker to get the missing information.

02:11:57 - Hemal Shah
So a user is requesting something — I want to book a travel or something — and if the user hasn't provided all the requested information, the assistant can extract the user's intent, identify what are the missing information, check for completeness, and then return back with some structure — hey, give me this, give me dates, give me, if you want to travel somewhere, here is only a pre-selected list of items that you can choose from.

02:12:28 - Hemal Shah
So looking into it, working with the ADK [tool:ADK] that you created — and I second what Ola said earlier, that if you had not created that video, I would not have learned it from Google's documentation.

02:12:45 - Hemal Shah
I went into an issue — I want a routing type of workflow. I know I went to sequential, parallel agent, but there's a condition: if completeness check is good, then you move for the execution; if they are missing information, then I need to add more metadata around it. I was able to figure that out using some custom agent.

02:13:46 - Brandon Hancock
▶ They have a ton of examples — you just have to know where to dig for them. There's one or two that would be really helpful. They have an orchestrator that has phases — it's like phase one, gather information. When you're gathering information, you can direct to agent one, two, or three. Once you have completed phase one, move to phase two. When you're in phase two, you can route to these three agents. So they specifically call out how to route to the necessary different people at multiple steps. [link:Google ADK browser agent example repository]

02:17:06 - Brandon Hancock
▶ Quick cheat code: when I'm working on another project, I always make a `ref` folder, and then in here I would clone in this project and say, hey, I'm trying to make something like this. Can you help me update my prompt to look like this reference project? You could dump in three or four projects that you like — heck, you could dump in any YouTube videos I've made — and say, I'm trying to steal this from Brandon's code, this from Google's code, and this from another project. Can you please help me make this prompt work well?

02:18:02 - Hemal Shah
<Q>Is there a standard JSON model that most people are using when sending a request to a chat API and getting a response back — a JSON structure I can build on top of?</Q>

<A>At least in ADK land and Gemini land, they do it through parts. A part can be a type string — a message contains parts, parts contain text, images, etc. When you run ADK, you can literally do `adk serve api`, and what that will do is actually expose endpoints to your ADK application. When you do `adk web`, what's happening behind the scenes is it spins up ADK using FastAPI [tool:FastAPI], and you have access to sessions, you can trigger runs — it opens up an entire FastAPI around ADK. The two most common return types are SSE (server-side events), which stream back small chunks with content and author, and a straight-up JSON object which just has content and author.</A>

02:22:54 - Hemal Shah
<Q>For voice assistants for customer support that tap into ERP/CRM — there are many tools like 11 Labs [tool:11 Labs], VoiceFlow [tool:VoiceFlow] — is there a recommendation for a full-blown voice assistant?</Q>

<A>After building that ADK voice tutorial out, I would actually recommend using the straight-up Gemini Live [tool:Gemini Live] library instead, just because when you start to do agent calls to function calls, it starts to get really weird with ADK voice. If you're looking for no-code tools, I like Bland [tool:Bland]. But Bastion and Maxim actually used one recently — I think it's called LiveKit [tool:LiveKit]. You get to do some code, it's already a pre-created library, it works well, you can host it, you can hook it up to phones. I would actually just use what these guys are doing.</A>

---

<!--SEGMENT
topic: Job Search Support and Freelance Client Wins
speakers: Alex Wilson, Brandon Hancock, Never2Nervous, Adam
keywords: job search, fraud analyst, consulting firms, ShipKit, severance, LHH, hedge funds, N8N automation, Vertex AI, open source LLMs, Next.js, SEO
summary: Alex shares his job search progress (fraud analyst background, on severance, using LHH outplacement services) and early success building an app with ShipKit. Brandon and Lewis (Never2Nervous) offer networking help including a consulting firm referral. Adam shares a promising new client lead — a hedge fund headhunter who wants to automate his document-heavy ChatGPT workflow using open-source/private models — and asks about tech stack recommendations for a separate NDA-bound freelance website project.
-->

01:55:34 - Alex Wilson
So, still looking for work, which is no fun.

01:55:44 - Brandon Hancock
Dude, so walk me through the journey — where are we at, where are we going, and how are you feeling, most importantly?

01:55:56 - Alex Wilson
I feel all right. I am still going the standard — not trying to create my own work, but like, you know, find a nine-to-five. So it's not fun, but it's happening.

01:56:09 - Brandon Hancock
<Q>Is it mostly LinkedIn? Is that where most of it's at?</Q>

<A>Yeah, LinkedIn. Because I was let go, I'm having LHH [tool:LHH] for my account with my previous employer, so they're guiding and looking over my resume, all that good stuff.</A>

01:56:38 - Alex Wilson
ShipKit — I did it right away, and tested it out, and was surprised that I actually was able to get an app within, I think, about three days, and it actually worked. I did run into problems with the authentication, so I'm looking forward to actually having access to the repository. I think it would have made it a lot easier.

01:57:18 - Alex Wilson
I started from prompt one and went all the way through nine to create the project. I didn't actually read a lot of the stuff that it was building, I was just testing it. But it actually completely did it.

01:59:02 - Brandon Hancock
Lewis just mentioned they're always hiring too. So hey, it's cool to be in a network of developers.

01:59:17 - Alex Wilson
I was a fraud analyst in my last career. So financial analyst. I don't want to stick with banking and whatnot. And obviously I'm interested in AI and that kind of stuff. So I'd kind of like to find a small company — founders and whatnot — and just kind of watch it grow.

02:00:02 - Brandon Hancock
▶ I would just check out consulting firms because most developers are always like, I want a tech company, but with your background, you're kind of versatile. It's not just I'm this box. You actually have a wider array of skills, which would work really well in a consulting company.

02:03:37 - Never2Nervous
Alex, I also work for a consulting firm, one of the Big Fours. And I can definitely get your resume in front of a human and not a robot, especially if you're interested.

02:04:25 - Adam
So today I just had coffee with a guy — he's a headhunter for hedge funds. His current process is he has a bunch of documents, and he copy-pastes prompts and documents into ChatGPT, gets the results, and does whatever with them. And I'm like, oh yeah, that's my perfect client, right? Because I can just automate all of that.

02:05:43 - Adam
He's going to send me what his long-term AI goal is and then a list of low-hanging fruit. I'm a little nervous because I'm thinking if I just slam dunk this project, he can introduce me to all his hedge fund buddies.

02:06:42 - Adam
One thing he's worried about is if he puts all his stuff into ChatGPT, someone's going to hack it and get all this data. So he's a little worried about that. He wants to use open-source stuff.

02:07:32 - Adam
I think we're going to do models hosted in like Vertex [tool:Vertex AI] or something like that.

02:08:45 - Adam
I was going to use React and Flask, but now I'm thinking — hearing all the stuff — I should go with the Supabase/Node.js route instead.

02:09:31 - Brandon Hancock
<Q>Should I use React/Flask or Next.js/Supabase for a client-facing website with a landing page and sign-up?</Q>

<A>Big recommendation: why I love Next.js and Vercel so much together is because of all the — when you're creating pages, a lot of the time you have static pages, and for better SEO optimization to help rank better, Next.js coupled with Vercel knows how to actually serve certain aspects of your page so that when Google is crawling everything, it can actually see your static pages. One of the big issues when you're using just a normal React app and not Next.js is everything is rendered through JavaScript. When something comes to check out your site, it's like, I actually can't tell what's going on until I load and use something to render the JavaScript.</A>

02:10:44 - Brandon Hancock
▶ Big, big, big recommendation: Next.js. The second you use it, it is very hard to go back. Once it clicks, it's just so hard to go back.

02:11:03 - Adam
She's already had me sign an NDA on it, so yeah.

02:11:10 - Brandon Hancock
Okay, never mind, don't share.

---

=== UNRESOLVED SPEAKERS ===

- **Mitch** — last name not provided in transcript; passed through unchanged.
- **Adam** — last name not provided in transcript; passed through unchanged.
- **Never2Nervous** — apparent username/handle; identified in transcript as "Lewis Louicius" (L-O-U-I-S-I-U-S) but raw speaker label is "Never2Nervous"; passed through unchanged.
- **Prem** — last name not provided in transcript; passed through unchanged.
- **Ola Oyo** — name confirmed in transcript; passed through unchanged (not in alias map).
- **Hemal Shah** — name confirmed in transcript; passed through unchanged (not in alias map).
- **Jaylen Davis** — name confirmed in transcript (rendered as "Jaylen.Davis" in raw); passed through unchanged.
- **Jake Maymar** — name confirmed in transcript; passed through unchanged (not in alias map).
- **Tom Welsh** — name confirmed in transcript; passed through unchanged (not in alias map).
- **Juan Torres** — name confirmed in transcript; passed through unchanged (not in alias map).