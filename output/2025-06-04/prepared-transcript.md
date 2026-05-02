=== SESSION ===
date: Not explicitly stated (Tuesday evening, inferred from context)
duration_estimate: ~2 hours 28 minutes (00:07:10 – 02:35:11)
main_themes: Python dependency management, MCP server troubleshooting, Cursor AI workflow tips, Google ADK framework, AI agent frameworks comparison, freelance pricing strategy, on-premise LLM deployment, document extraction tools, content creation strategy, community project showcases

---

<!--SEGMENT
topic: Session Opening and Python Tooling
speakers: Marc Juretus, Tom Welsh, Andrew Nanton, Brandon Hancock
keywords: UV, pip, Poetry, Conda, Python dependency management, Cursor rules, .cursor/rules, virtual environments, context window, FastMCP
summary: Participants exchange greetings and discuss Python package/dependency management tools, comparing UV, pip, Poetry, and Conda. The conversation transitions into a discussion of Cursor's .cursor/rules deprecation and the tradeoffs of granular rule files versus monolithic configurations. Brandon opens the formal session and shares a quick update on recent content.
-->

00:07:10 - Marc Juretus
Hey, how are you doing? Good to see you. Not bad.

00:07:14 - Tom Welsh
Yourself?

00:07:15 - Marc Juretus
I can't complain. Another day of work in the books. Back with my second family here, so here we are.

00:07:24 - Tom Welsh
How are you, Andrew?

00:07:32 - Andrew Nanton
Doing all right, thank you. Yeah, just staying real busy with other work, but I'm excited to get back into a little more programming sooner rather than later.

00:07:44 - Tom Welsh
So I'm waiting to fall asleep. It's like 11pm here. I've been up since five this morning.

00:08:07 - Tom Welsh
Yeah, didn't realize the `.cursor/rules` had been deprecated as much. I started doing the `.cursor/rules` part, Andrew, and I was interested you said that because you had uploaded my `.cursor/rules` file as well.

00:08:23 - Andrew Nanton
Yeah, I mean, I'm sort of of two minds about it, right? Because having it broken into something more granular on some level makes a lot of sense, but it's a lot harder to reuse because it's all these little fragments and they're everywhere.

00:08:36 - Tom Welsh
And you've got to get your own kind of naming convention. I mean, you go like role, so you develop a role marketer, role this and role that.

00:08:46 - Andrew Nanton
Yeah, yeah, it seems a little over-engineered to me. And then when I use that generate function that it has, which I appreciate because I didn't want to make a bunch of these little tiny files, it's like six pages. I gave it like — use UV to manage Python dependencies and `uv run` to run. And then it gives me like this six-page thing that it's cramming into the context window.

00:09:12 - Tom Welsh
It's like, well, why? That's nonsense.

00:09:17 - Marc Juretus
It's funny, I had to think twice what UV was. When did UV come out?

00:09:26 - Andrew Nanton
Yeah, well, I guess I've never heard anyone say it out loud.

00:09:32 - Marc Juretus
I do, it's definitely an improvement over Conda, in my opinion.

00:09:37 - Andrew Nanton
Oh, man, I would never go back.

00:09:43 - Tom Welsh
I still keep falling back to pip, well, depending. And I was getting into Poetry, that was going quite well. You brought up UV, and UV was really cool.

00:10:00 - Andrew Nanton
You can use pip from UV if you want.

00:10:04 - Andrew Nanton
▶ I love how when you go to the folder, you're done. Like, there's one step. You know, all your dependencies are there, and you don't have to activate the virtual environments.

00:10:16 - Marc Juretus
You have to put the version numbers in so easily in UV, you know, if you want a specific version of a dependency.

00:10:25 - Tom Welsh
Hey, Brandon.

00:10:26 - Brandon Hancock
Hey, guys. Thank y'all for hopping on. We're crushing it. People keep hopping on — a busy night. I'm loving it.

00:10:36 - Brandon Hancock
Well, real quick on the Python dependency train talk — literally same thing as you guys. I hop between all of them. If I'm playing around locally, pip for days, but the second I have to be more productized, yeah. At this point, I'm going pretty much UV for everything. But that's my quick split for how I'm doing it.

00:11:00 - Brandon Hancock
But what we can do is I'm going to take a quick screenshot to show you guys the call order for tonight. A bunch of new faces — so excited to see everybody hopping on. Just a quick heads up for the usual way we approach this: we just go around the room based on the screenshot order I'm putting in the chat right now, and usually try to keep it around six to eight minutes just so everyone has time. Usually just sharing a quick win or a problem that you're working on and you're stuck. And as a group, we're all happy to help.

00:11:37 - Brandon Hancock
Quick updates on my side. So I dropped that MCP video on the weekend. And then this week is all about the A2A framework [tool:Google Agent-to-Agent (A2A)]. So pretty excited to work on that one for you guys. If you have any questions about it, happy to discuss. But quick thing I did get to learn — it's not insanely stable yet. I thought agent-to-agent was already standardized, but it is not actually yet. So Google is still in the middle of reaching a version one. Some of the core principles are the same, but the actual implementation is not yet. So I got to talk to them this week, and yeah, it's not 100% stable yet. So that was just a shocking fact to me. I'm going to do a video on the core basics that aren't going to change, but all the exact implementations of security and making sure people don't abuse your agents — a lot of that's still getting figured out with A2A.

---

<!--SEGMENT
topic: MCP Server Troubleshooting on Windows
speakers: Marc Juretus, Brandon Hancock, Bastian Venegas
keywords: MCP, Model Context Protocol, Windows, NPX, Node.js, FastMCP, Airbnb MCP, Google Maps MCP, filesystem MCP, subprocess transport, logging
summary: Marc describes a recurring "NotImplemented" error when trying to run MCP servers on Windows, affecting multiple MCP packages including Airbnb, Google Maps, and the local filesystem server. Brandon and Bastian diagnose the likely cause as NPX not resolving to the correct Node.js executable path on Windows, and Brandon recommends enabling server-side logging and trying the FastMCP library for easier setup.
-->

00:13:06 - Brandon Hancock
Mark, you're up first.

00:13:15 - Marc Juretus
Yeah, I mean, everything I'm working on right now, I was trying to just polish up on my FastAPI [tool:FastAPI] and Next [tool:Next.js]. So I got it to a point where I'm savvy enough that I maybe start building upon that instead of using Streamlit [tool:Streamlit]. But where I'm stuck is with MCP [tool:MCP], you know, I went through your tutorials and stuff, and it seems to possibly be like some type of Windows issue. I see a couple people on the board. I think I posted a question to the board about it. Basically, what was happening is every time I would try to run it, it would just fail and give me an error.

00:13:58 - Marc Juretus
Yeah. So basically, the error says "NotImplemented" — and line 524, `make_subprocess_transport`, raise `NotImplemented`. Now, tried your demo as well as the Google Maps one on their site, on the Google Agent site, as well as their filesystem one. And I have basically the same error.

00:14:17 - Brandon Hancock
<Q>Is it a Google ADK error or is it an MCP error? Does it say which one?</Q>

00:14:24 - Marc Juretus
<A>It just basically says "NotImplemented."</A>

00:15:01 - Brandon Hancock
And while you're pulling that up, one thing I just dropped in the chat, guys. So I didn't want to make the video take forever for MCP, but a lot of what I showed you guys in part three when I was showing you guys how to set up your own local MCP server, it was more manual to where you guys were learning how to create the request that was going to receive to do the two main functions of an MCP server, which is call a function and list functionality. ▶ If you don't want to do all of that, the FastMCP library [tool:FastMCP] that I just put a link into makes it so much easier. You just have to put a tool decorator around the actual tools that you want your agents to call. Works really well. So I would definitely recommend checking that out as well if you want a little bit more of a smooth setup.

00:15:54 - Marc Juretus
So you can see my screen? Yeah. And this is basically the error. It's an MCP toolset server fails. That's exactly what I'm getting. You know, I went through and I actually did a rebuild and I went back to like the simplest one, which was a filesystem one, and I get it for every project that I try to call.

00:16:10 - Brandon Hancock
Okay, one thing that I would recommend doing is — the biggest issue of working with the MCP server is like, you can't really see what's going on and you have to set up logs. So let me pull mine up really fast. ▶ One thing I would recommend doing is in your server, setting up this logging path right here, and what it's going to do is allow you afterwards to see exactly where things went wrong as the server was running. So you can kind of see exactly like, oh, it's at the tool call, and it might just give a little bit more additional information than what you're currently getting.

00:17:19 - Brandon Hancock
I would also — I saw you're using one for Airbnb — I would try potentially a different package, like the Notion one, because I know for sure Notion works. Some of the other MCP files are not as stable as one would expect. So it could just be the Airbnb MCP server you're trying to spin up.

00:18:18 - Brandon Hancock
Bastian just dropped a really good tip that you might want to do, which is like your NPX might not be running from the proper location. So if you want to check chat, Bastian pointed out a really good way to where you can actually point to the specific Node executable that will actually trigger everything. Yeah, seriously, thank you, Bastian, for dropping that. Darn Windows. See, man, everybody's got to get a Mac. That's the problem solved.

00:19:07 - Brandon Hancock
Yeah, seriously, ping us if it keeps having an issue, but I'm 99% sure that solution that Bastian dropped is most likely to fix it.

---

<!--SEGMENT
topic: Cursor AI Workflow Tips and Model Comparisons
speakers: Andrew Nanton, Brandon Hancock, Richard Richard
keywords: Cursor, Gemini 2.5, Claude, LLM, plan approval, feature branches, context window, ultra-think, prompting strategy, task planning, community thread
summary: Andrew shares his experience using Gemini inside Cursor versus Claude, noting Gemini performs better with large file contexts but can loop on broader tasks. The group discusses prompting strategies including plan-before-execute, writing plans to separate files, and giving the model multiple options. Richard introduces the "ultra-think" technique for unsticking looping models. Brandon highlights a community thread with 31 Cursor tips.
-->

00:19:16 - Brandon Hancock
All right, Andrew, you're up next, man.

00:19:21 - Andrew Nanton
What cool project have I been working on? Well, Maxim and I have been working on our stuff together. And working on some prompt engineering stuff when I have time and getting more familiar with structured outputs and evals and how all those things fit together.

00:19:49 - Andrew Nanton
I started your ADK video, and I'm excited to get further into it. I have been using Gemini [tool:Gemini] more in Cursor [tool:Cursor] — it's good, but I still find, and it may just be me, but I still find it chasing its tail more than Cursor. Like sometimes it'll apply a fix, and then it'll go back and undo what it did. I'm just getting better results from Claude [tool:Claude], generally speaking, but I do definitely feel like if I need to look at a bunch of files at once, if things are getting really complicated, that huge context window is really big. And this is like — I would say 20% of the time, it doesn't get as good results for me as Claude does for me personally. But a lot of the time, it's really good, and it's definitely faster, so I'll be using it more, I think.

00:20:48 - Brandon Hancock
I wish — I'm glad you brought that up — I wish we could see how each of us prompted. Like I would be very curious what you're asking versus what I'm asking, just because there could just be the way I'm asking questions. Versus you, like your style could be more Cursor or Claude-esque. Right now, me and Gemini have become one. I don't know what it is, but it is the one that's treating me the best right now. But I will say, I know what you are talking about with it — yeah, that 10%, it's like, oh, you probably wanted this. No, like, didn't even ask for that. <Q>How broad of changes are you asking for? Like, when it fails, is it a broad request, or is it a simple request that's failing?</Q>

00:21:49 - Andrew Nanton
<A>It's something bigger, like, the more focused I am, everything seems to work fine when I'm focused on something narrow, which is really how I ought to be working. It's when I try to do too much.</A>

00:22:06 - Andrew Nanton
▶ I picked up a few good things from that Cursor thread in there. Definitely one of the things I do — I noticed Tom has the same approach that I have had — which is: make a plan, tell me your plan, don't do anything until I approve your plan. I usually also throw in, give me a couple of options. And sometimes the options are like, I could fix it or not fix it. But I'm never sad that I've included that as a possibility because sometimes it's like, well, I could make six more files and make this super complicated, or I could just do this one simple thing.

00:22:48 - Andrew Nanton
▶ And then when I've been doing bigger things, someone else in there suggested have it write out to another file to make a plan. And I find that super helpful — one that I can keep referring back to and iterating on. And I've sometimes had a few different LLMs look at it, like, okay, review this, tell me what you think, any way we can simplify this, what can be replaced with libraries, et cetera. And I've found that to be a really useful technique as well.

00:23:43 - Brandon Hancock
▶ The plan output — absolute cheat code — and the plan approval, just to make sure like, hey, before you go wild destroying my code, let's make sure we're on the same page. Absolutely love those two. The other one — the reason Gemini gives me so few errors is because instead of tackling one monster task at a time, I'm almost telling it the thing I would do next. And I'm like, okay, move this here, move this here. So I'm like constantly passing in screenshots if need be. I'm passing in doodles. So that's another thing that I do all the time, especially for UI stuff.

00:25:35 - Brandon Hancock
Richard, I saw you had your hand up, buddy.

00:25:38 - Richard Richard
Hey, how's it going, everyone? I just wanted to drop real quick that this little weird thing that people have been doing — I thought it was kind of like crap — but just telling the model to **ultra-think** when it's going in loops like that seems to get it unstuck. And so yeah, I have tried this out, and it works great. I also document when it is going in loops just to kind of point that out and then say, hey, like, you know, you're kind of going in loops with this, this, this, this — ultra-think — and it seems to just unstick it. So just try it out.

00:26:17 - Brandon Hancock
I'll have to try that. Yeah, I haven't seen that one yet, but that's funny. Like, hey, if it works, it works. Can't argue it, you know.

00:25:00 - Brandon Hancock
Yeah, this thing is a wealth of knowledge. So I'm pumped to do our first community-driven video here super soon and give all the necessary shout-outs. So far, yeah, 31 comments — literally a ton of ideas on how you can better use Cursor. So I'll drop a link and put it in chat.

---

<!--SEGMENT
topic: Tom's Projects and DeepSeek Model Discussion
speakers: Tom Welsh, Brandon Hancock
keywords: DeepSeek, Ollama, Gemini, Claude, Cursor, VMware, web architecture, load balancing, caching, Medium article, image recognition, military aircraft
summary: Tom shares two projects: experimenting with AI image recognition on satellite/aerial photos of Russian airfields (finding models 90% wrong on aircraft identification), and building a three-tier web architecture (frontend, caching, load-balanced database) inspired by a Medium article on scaling. The group briefly discusses the new DeepSeek coding model and whether it's worth trying locally via Ollama.
-->

00:27:54 - Tom Welsh
Hey, hi, everyone. So yeah, this week, I've not been doing much programming-wise, but I've been playing about with my virtual machines — quite entertaining, doing automatic builds and just scripting building of that. I used some of Cursor to build out some of the VMware box stuff for that, which is quite cool.

00:28:12 - Tom Welsh
What I have found quite interesting this week was after Ukraine did a bit of blitzing in Russia, I did some plane spotting for basic image stuff, and it was quite interesting to take snippets of the airfields and then go identify these planes on the runways. And obviously, they were Backfires and whatever, and you chucked it in. And they would get it 90% wrong most of the time — and that's talking Gemini, Perplexity, and Claude. Like, Flankers were coming out of things like, oh, they're MiG-25 Foxbats, like, no, they're not. And it might be down to just scaling, because I didn't see the whole runways — you've got a bit of concrete with planes on it. But yeah, found that image checking of that kind of stuff, which I thought would have been quite easy, didn't come out quite as well as I expected.

00:29:04 - Brandon Hancock
<Q>Did you give it any context, or was it just like a straight raw picture and like label this?</Q>

00:29:09 - Tom Welsh
<A>Yeah, literally I went, here's an airfield with some planes on it. What are they? Give me the NATO designations. And yeah, basically pretty free form. And I pulled back some Russian planes, which was good. But on one Russian airfield, found some F-16s — and I go like, no, you're completely wrong there for a start.</A>

00:29:33 - Brandon Hancock
Yeah, that's not even logical.

00:30:51 - Brandon Hancock
<Q>Has anyone got to try the new DeepSeek model for coding? Just out of curiosity.</Q>

00:31:00 - Brandon Hancock
Because at this point — okay, all right. I was just curious just because, like, I tried the original one for coding, and it just took a very long time, and all the other ones just did better. So I was just curious because I know it's supposed to be one of the best ones right now.

00:31:19 - Tom Welsh
I'll definitely check that out. You've got a link for that one? I'm going to pull it down and try it in Ollama [tool:Ollama].

00:31:24 - Brandon Hancock
I mean, it's a monster of a model. The new one? Is that four or five billion or something? It's DeepSeek [tool:DeepSeek] one but an update, correct? Because they haven't fully done R2 yet.

00:31:52 - Tom Welsh
They're not getting dust. Basically, I created a three-tier — well, web front-end caching layer, database backend, load balanced — so I've got this stuff flying everywhere, and this all came off the back of somebody else's post where they were throwing millions of requests. I thought, yeah, let's just try that at home, why don't we? So I just built it up and taught myself a bit more.

00:32:15 - Brandon Hancock
Based off that Medium article you did, is that what you're referring to?

00:32:20 - Tom Welsh
Yeah, I think it was part of that, yeah. That was the bottlenecks one.

00:32:27 - Brandon Hancock
Yeah, Tom linked a really awesome post the other day, guys. It's on Medium, but basically it just goes deeper into web architecture, and if you're interested in that, I thought that was a phenomenal article just to kind of explain, almost from a practical sense of, as you scale, like, what to look at and think about. [link:Medium article on web architecture bottlenecks]

---

<!--SEGMENT
topic: On-Premise LLM Deployment Client Opportunity
speakers: Juan Torres, Brandon Hancock, Jake Maymar, Tom Welsh, Andrew Nanton
keywords: LLM deployment, on-premise GPU, NVIDIA A100, Ollama, RAG, fine-tuning, vector store, multi-tenant, data security, SloTH, discovery call, pricing, HIPAA
summary: Juan describes a potential client who wants to deploy open-source LLMs on NVIDIA A100 GPUs at a co-working space (Oculus), including RAG, fine-tuning, and model training. Brandon and the group advise doing a thorough discovery call first, scoping minimum viable functionality for V1, using tools like SloTH for fine-tuning, and being cautious about multi-tenant data security. The consensus is to get a foot in the door with simpler functionality before expanding scope.
-->

00:33:37 - Juan Torres
So I have a presentation tomorrow with the engineering group. I already decided that I'm going to use the real system. So for the new use analysis of the vector...

00:33:54 - Juan Torres
So he wants to deploy LLMs [tool:LLM] in a server that is being hosted by Oculus. Oculus is kind of like a WeWork kind of environment in which you can rent offices. And recently, they installed NVIDIA-based computers in order to be able to allow them to host their own LLMs in there. And I think NVIDIA and Uber are kind of partnering up in order to establish these servers throughout several places. So he was getting in contact with me to deploy the LLMs. Their servers seem to be very powerful, and they don't seem to have limitations as to which models can be hosted in those servers.

00:35:57 - Juan Torres
The issue is that he seems to want a lot from the deployment of the LLMs. He wants a RAG database. And he wants the fine-tuning and the training of the models. And so, like, I have no experience in fine-tuning and training the models. I do have a person that has experience in fine-tuning machine learning models and training machine learning models and fine-tuning LLMs. But I will have to bring him in in order to be able to do this work because my experience is mainly within engineering, right? So I'm just wondering, like, this is a lot of components working together for what he's trying to do. And I wanted to ask you guys, like, what would you do in terms of pricing this kind of service?

00:36:55 - Brandon Hancock
So I want to say it back to you to make sure I'm on the same page. So basically, he's renting one of these monster GPUs — or maybe a few of them — on premise. And what he's trying to do is say, all right, anyone who's at one of our co-working spaces, you can use one of these models. More specifically, it's almost like you have a Vertex AI [tool:Vertex AI] where there's a front end that has, you know, you're controlling all of the H100s or A100s on the back end.

00:37:34 - Brandon Hancock
Okay, so here's what is easy, here's what's hard. Running on that server, just regular Ollama, and then exposing it to the network, giving people a chat window, and they can pick which model they want to chat with. So they get all the DeepSeeks, they get all of the large, huge open-source models. That, pretty straightforward. So if he wants that done, I mean, you're really just creating like a login page, a UI. And then you're making requests to that monster machine. That part's pretty straightforward.

00:38:06 - Brandon Hancock
Setting up RAG, I'm not sure. Like, it'd be awesome if he could explain some more of this functionality to you. So, like, hey, dude, let's just — it's two months, it's three months into the future, this app's working perfect. What are people doing? Like, are people dropping in documents? And then, like, is this to where they're dropping in documents and then asking questions about their own stuff? Or, like, is this actually supposed to be mostly primarily a model training service? Because once you start to get into some of the model training stuff, that's out of scope of what I'm comfortable with.

00:38:44 - Brandon Hancock
It's something — I can't remember it, Bastian, maybe you can remember — but it's an animal name. But basically, it allows you to train models, your llamas and all those. Allows for fine-tuning locally.

00:40:57 - Brandon Hancock
If you are having to do some fine-tuning, I'm — SloTH [tool:SloTH]. I've heard amazing things about them. So basically you would just take a large CSV file of like query-type-of-answer and you could probably train it on his stuff. It is open source. It's free to use. They have a ton of documentation, but this is what I would use. And like I said, it works with all the new models.

00:41:36 - Tom Welsh
And also you've got to look at separation for if you're doing multi-tenant on these A100s. Because cross-pollination of data is a big no-no. As Andrew would say in the HIPAA land, putting stuff up there, you want to know your data is secure. That's the biggest thing nowadays is keeping data secure on an online service.

00:44:11 - Brandon Hancock
▶ Today I would just go in more discovery mode before offering any prices. Just because, like, this could be pretty straightforward or like, oh my god, an insane amount of work. I just don't want you to accidentally overcommit to something that's like, oh, I charged 5K and it was really a 50K job.

00:44:37 - Tom Welsh
▶ Get your foot in the door on something simple, then grow the product from there. Product's got a life cycle.

00:44:45 - Brandon Hancock
Totally agree.

---

<!--SEGMENT
topic: Freelance AI Project Pricing Strategy
speakers: sam, Brandon Hancock, Tom Welsh
keywords: pricing, milestones, SaaS, RAG application, agentic workflow, prompt engineering, discovery, hourly rate, fixed cost, Supabase, evals, Loom video
summary: Sam asks how to price a specialized internal web application (a report-drafting tool) for a family contact's business. Brandon provides a detailed pricing framework: fixed upfront cost (suggesting ~$20K for this scope), milestone-based payment structure with a two-week testing window, and hourly rates post-launch (~$120–$150/hr). He emphasizes the dual role of AI developer and AI consultant, the importance of extracting client processes via Loom recordings, and building a prompt management interface to reduce deployment friction.
-->

00:44:51 - Brandon Hancock
All right, Sam, you're up next, man.

00:44:54 - sam
Hey, hey, hey. I have a question along the similar lines, but nowhere near as complicated a project.

00:45:23 - sam
So as context, I'm developing — it's the same project, but I'm just thinking about how to do pricing for it. So obviously, I feel like I'm going to charge development time to do it. And then the ongoing, like a subscription fee for the user as well, because I'll be covering a lot of the hosting kind of stuff. So, as a really high-level picture, it would basically be like a web app where they go in and they use it kind of like a GPT, but they'll be highly specialized tooling, which is where their value will be for them.

00:46:06 - Brandon Hancock
<Q>So can I say back to you real fast? So you're building a web application that's a chat application that has access to proprietary tools, correct? Like that's the high level? And then question is, when it comes to pricing, how to price it?</Q>

00:46:27 - sam
<A>Yeah. So obviously, I would just pass on all the infrastructure costs, but do you think we should mark up on usage as well? So when they do — or like if the tool's quite essentially a chain — do we charge per run of the chain and margins and that kind of thing?</A>

00:46:48 - Brandon Hancock
So we'll do a rapid fire series of questions just to like make, so you can kind of see what I'm thinking. So is this for a family member or friend?

00:46:59 - sam
Yeah. Well, yeah, it's a family contact, but it's a full business arrangement, it will be.

00:47:04 - Brandon Hancock
<Q>Are they going to be using this application on their own, or is this something they're trying to white label? Like, is this an internal tool, a tool that they're using and exposing externally? What's the scope?</Q>

00:47:16 - sam
<A>It's internal, yeah. It'll be internal.</A>

00:47:18 - Brandon Hancock
<Q>And then outside of that, how big is the company, and how much have they talked budget at all for this?</Q>

00:47:27 - sam
<A>Budget is an issue — they're more interested in a quality product.</A>

00:47:34 - Brandon Hancock
<Q>And what problem is it actually solving for the business?</Q>

00:47:37 - sam
<A>It's that drafting report.</A>

00:47:42 - Brandon Hancock
Okay, yeah, so I mean, like, so I mean, for these types of projects, like, usually what I like to do is I fix cost up front, because I would rather secure all the money up front and then charge on just development rates later on or bundling things in phases.

00:48:09 - Brandon Hancock
So let me just give you an example. So for your initial project, here's my understanding of it. It is basically like you're building an application that's going to be used by multiple users in that organization. So there's going to be some sort of login, authentication, potential role access levels. There's going to be the actual, all the proprietary like prompts. <Q>Are you managing the prompts? Are they managing the prompts?</Q>

00:48:35 - sam
<A>No, I'll be managing all the kind of infrastructure and that kind of stuff.</A>

00:48:44 - Brandon Hancock
So the reason why I'm asking is because like — and this is like a cool concept guys — but like we have to wear multiple hats. We have to wear the AI developer hat, which is like building the thing. But then we also have to wear the AI consultant hat, which is basically like extracting processes from their head and then putting it into actual prompts. And a lot of people overlook that skill and they're like, oh yeah, I'll just build an app. But if the person doesn't tell you what you want, like, that's going to take a ton of time to observe their processes. You're going to have a thousand questions. There's going to be a ton of feedback cycles.

00:49:24 - Brandon Hancock
▶ One dynamic way you can do it is always just create like a prompt interface to where they can pass in prompts and they can adjust it. The admin, so you're not always being stuck on the hook for deploying a whole new application to test a prompt. You could save prompts to a database and allow them to tweak it. That's always a quick workaround.

00:49:51 - Brandon Hancock
▶ But yeah, going deeper into this, if you're building this for a real world business, they're going to expense this. It's going to make them more productive. I would — tens of thousands is probably what I would charge. I mean, I would like just roughly, I'd probably do 20 without knowing more scope.

00:50:13 - Brandon Hancock
▶ I broke it up into three milestones. I did a basically a 15% down payment — like, hey, for me to even start this, I want to know you're involved. 15% just to start, probably go up to 20%. Then I broke it down into — because it was a smaller project, 8K — I did a part two, which is I'll build the application, then pay me the next 5K, and then you have two weeks to test the application to make sure it's perfect. During those two weeks, if you have any small adjustments, I'll do it under the initial budget, but once the two weeks is up, you owe the final $1,000, and then after that, it's an hourly rate. So it just aligned incentives, worked really well for both of us, everybody won.

00:51:00 - Brandon Hancock
▶ And then what's going to happen is eventually you're going to, those hourly rates, it's just going to be to improve Phase 1. Eventually they're going to want a big thing, and that's when you do Phase 2. Another high 5, 10, 15, 20K project.

00:52:00 - sam
That in itself could be another entire project that you'd have to price up. So it's like, hey, look, this saves you money if I give you this window and you tell me what's wrong, as opposed to if you want me to do that, then that's going to be another $10,000 or $15,000 because that's in itself is another AI system that I'd have to develop.

00:53:19 - Brandon Hancock
▶ And then the one thing I just saw recently on an email chain is to turn the work on them as much as you possibly can. So, for example, when they're describing manual processes, just have them bullet out or record Loom videos and send it to you, preferably just Loom videos so you can actually see what's going on. That is one of the biggest cheat codes to help you actually understand the process in as much detail as possible.

---

<!--SEGMENT
topic: Maksym's Nissan Dealership AI Tool Progress
speakers: Maksym Liamin, Brandon Hancock, Bastian Venegas
keywords: WhatsApp, Nissan, GPT-4o, financing recommendation engine, structured outputs, multi-tenant, advertisement, beta, legal compliance, foot-in-the-door
summary: Maksym shares updates on his WhatsApp-based AI tool for Nissan dealerships, now presented on Nissan's global internal network. He describes a new financing recommendation engine that asks salespeople two poll questions and recommends the best financing plan from a partner bank. The group discusses legal compliance considerations, the importance of CYA documentation during beta, and how continued feature additions demonstrate the value of getting a foot in the door with clients.
-->

00:54:57 - Brandon Hancock
Next up is Maksym.

00:55:01 - Maksym Liamin
Hey guys, how are you doing?

00:55:05 - Maksym Liamin
Yeah, so I'm in Bulgaria right now. Here it's like, it's even later than normally in Germany. So I had a birthday recently, so I spent it with my parents here.

00:55:46 - Maksym Liamin
And yeah, from the news — there is just a lot of stuff, a lot of work now at the beginning of the month. So we just got the new offers for like credit and financing. So literally, as we speak, I'm plopping in numbers from like tens of thousands of rows of Excel spreadsheets. For the offers, like offers of the month and like trading options, like the financial plans and all that kind of stuff.

00:56:33 - Maksym Liamin
And then from such news, today we got presented by the Nissan global network. We had a broadcasting in their internal network. So we got — our tool got presented. We got some new users there.

00:57:00 - Maksym Liamin
And also we started giving kind of advertisement places inside of our tool. So just yesterday we finished a kind of demo that we're doing for one of the banks that also has a financing option in Nissan — that we not only just say that, yeah, it's available, because right now the functionality is that like you can ask, for example, for Sentra for this specific trim, there are this kind of financing options that are available, right? But then now we added kind of a recommendation engine. So basically a salesperson will answer like two polls and then — if it's complex and maybe some more details — then we will recommend like the best kind of financing option that comes from the bank.

00:57:53 - Brandon Hancock
<Q>That's cool. So does it, how detailed does the advertisement get, like does it map out like a full-on report to send over to the user, or is it just like, hey, you should do that 8% financing?</Q>

00:58:04 - Maksym Liamin
<A>Yeah, I mean, it goes pretty detailed, yeah, so it's heavily dependent on occupation, like specifically if he is like a taxi driver or entrepreneur, it's very different from like a normal employee. It also goes a lot into kind of like credit history, if like the user has good credit history and those kind of stuff, and then a couple more questions maybe about like monthly income or something like this. Dependent on the plan because they all are very different, and then like it just kind of minimizes the options and throws you the best one.</A>

00:58:40 - Brandon Hancock
<Q>And is it all in WhatsApp [tool:WhatsApp], or are we now in web land?</Q>

00:58:45 - Maksym Liamin
<A>No, never web.</A>

00:59:03 - Maksym Liamin
It's actually pretty concise. I mean, the questions that we ask — we literally mapped it very good and very easy so that it's not even — like you don't even need to type, it's just a poll that you click, and then the final message, it's like either one or two plans, and we summarized them pretty much so that it looks good, and then you can ask for more details, and then we already kind of send the monster message.

00:59:30 - Brandon Hancock
<Q>For a quick model question — are you using GPT-4o? What was your go-to model right now for most of these chat conversations?</Q>

00:59:34 - Maksym Liamin
<A>Yeah, we use GPT-4o [tool:GPT-4o].</A>

01:01:02 - Brandon Hancock
▶ Final thing, just — would — make sure you send an email of some sort, just to CYA, cover your ass. I'm just, like, hey, like, I'm just doing what you guys have recommended. Like, I, under no circumstances, am saying, like, is this following all the proper legal procedures? Like, I'm just showing information on your website to them. I cannot guarantee that what's being shown is — I'm just scraping data and showing the data, you know?

01:01:47 - Brandon Hancock
▶ And like, Maksym is a beautiful example of what we've been saying of, like, hey, like, just, once you get your foot in the door, there's always more work. So this is the third or fourth thing you've continued to add to help out. So, yeah, this is awesome. So just do a great job, foot in the door, and then more work will come once these businesses see the magic of AI.

---

<!--SEGMENT
topic: Agentic Document Extraction Tool Demo
speakers: Bastian Venegas, Brandon Hancock, Andrew Nanton
keywords: document extraction, agentic OCR, Andrew Ng, bounding boxes, coordinates, markdown, JSON, medical documents, Azure Document Intelligence, handwriting, open source, three cents per page
summary: Bastian demonstrates a new agentic document extraction tool (associated with Andrew Ng) that uses spatial coordinate-based ordering to intelligently parse complex documents including handwritten forms and medical reports. The tool processes documents up to 50 pages in a playground, outputs structured markdown and JSON with bounding box coordinates, and reduced processing time from 2 minutes to 8 seconds. Andrew compares it favorably to Azure Document Intelligence, noting the visual quality of results is superior even if pricing differs.
-->

01:02:21 - Brandon Hancock
Bastian, you're up next, man.

01:02:23 - Bastian Venegas
Yeah, first, I want to say congratulations to Maksym on both his birthday and how good he's doing at work.

01:02:53 - Bastian Venegas
I just wanted to show a tool for agentic document extraction since there are always people interested in that. And this is this one is by Andrew Ng [tool:Andrew Ng document extraction tool], who's really famous in the space. There is an ad for this in his LinkedIn profile that kind of goes into more detail, but I just wanted to show like the stock images they have here in the playground.

01:03:24 - Bastian Venegas
So for example, this is a statement for an accident and you can see that this — why they call it like agent extraction — is because first there's an agent that kind of decides what's the order that you will be reading the document and then they perform the different extractions about every field. So they kind of have that way to make sense of the stuff when they're rendered here on this right side in markdown.

01:04:00 - Bastian Venegas
You have some ways of kind of representing these graphics, because there is like the vehicle illustration and the spatial relationship, so even though it's not the image, they are describing what it interprets like in this very context, specifically. There's also that represented as a flowchart, so I found that pretty cool. You can also get it as a JSON, and I noticed they have like this box, that's probably the coordinates for each one of these bounding boxes, so you have like a very specifically specific way of knowing where to look for this text, so I guess that's probably vital to the whole document understanding.

01:05:00 - Bastian Venegas
And here you can chat with the document, which I haven't tried, but the sample prompts are, I guess, suggestions based on what the agents extracted, so it's kind of pretty useful out of the box. So I found that, and they say their processing time went from like two minutes to like eight seconds, I guess, per document, but you can put that document up to 50 pages in this playground.

01:05:30 - Bastian Venegas
And here is one from a medical document, really quickly, but it also basically does the same — like figures out the order in how to read this, and then it's even like describing what the images from these tissues are showing, like what's the thing, why do they have this color, where's the nuclei and all the stuff. And then the report — like this is a real use case for a document that you would need to digitize for every patient. It should be available to all of them. Basically, it shouldn't be ever like captured in a particular database from a provider.

01:06:18 - Brandon Hancock
That's amazing because, I mean, literally for like the past year, it was like, well, like if it's handwriting on a sheet of paper, you're just hosed, you know, like that was kind of just — unless it was like a very blank PDF page, you could go Docling [tool:Docling], obviously Docling crushed it for free. But the second it was like a real life form where the user signed in or like added stuff, you were hosed. So that is — my mind is blown right now because like we've all been waiting literally for that to pop up. And the fact that like it's three cents a page — like, yeah, that's a little costly, but like it's either that or you don't get it done.

01:07:04 - Bastian Venegas
Like, you can also have a pipeline that for some type of documents goes just Docling and that's enough. For example, I understand that Maksym did that basically with all of these documentations from cars and everything. And they have an API, so there's no — it's just like, hook it up and it's done.

01:07:38 - Andrew Nanton
Yeah, I got pretty good results from Azure Document Intelligence [tool:Azure Document Intelligence], for the documents I was doing. The layout model is — I'm trying to remember — the straight OCR is 10 times less expensive than the layout model.

01:08:37 - Andrew Nanton
<A>Well, no matter what the price difference is, I don't think that we were getting results like that. What they were just showing looked really impressive.</A>

01:09:00 - Bastian Venegas
I also find really interesting is this — it's very kind of evident and explicit how they're doing the core structure of what they uncovered here. It's pretty clear — they just proven, like, identifying spatially with coordinates is like a step of the document extraction, like, for this complex document. ▶ So I think there will be a little time before an open source alternative shows up.

---

<!--SEGMENT
topic: N8N vs Make, Supabase vs Firebase, and Workflow Tool Selection
speakers: alexrojas, Brandon Hancock, Bastian Venegas
keywords: N8N, Make.com, Ollama, Ngrok, Supabase, Firebase, Firestore, Postgres, Neon, Drizzle ORM, vector store, RAG, sentiment analysis, Google Forms, Google Sheets, government course
summary: Alex asks whether to use Make or N8N for a simple citizen survey sentiment analysis pipeline (Google Form → Google Sheet → LLM sentiment → report) for a government course in Guanajuato. Brandon recommends N8N for anything beyond a single LLM call, and Bastian explains how to expose Ollama locally via `ollama serve` as an API endpoint for either tool. Alex also asks about Supabase vs Firebase for ADK projects; Brandon explains his preference for Postgres/Supabase over Firestore's NoSQL model, and notes Neon as an alternative.
-->

01:10:07 - Brandon Hancock
All right, Alex, you are up next, man.

01:10:27 - alexrojas
I have an actual specific question. Do you remember, guys, I told you I had a gig coming? For a course for the government of a state, Guanajuato. So, I've been doing some research on your videos, Brandon, which — I don't know how the YouTube email automator slipped through the cracks. I cannot believe I hadn't seen it before.

01:11:00 - alexrojas
It's a very simple, because it's government people, we need to stick to as much free things as we can, you know? So the specific question that I had is Make [tool:Make.com] versus N8N [tool:N8N]. I saw the video that you used, Brandon. You used Make for one of your videos. We could actually use your coupon for one month for free of Make.com. That would be one option. And what I wanted to ask is, this is a very simple flow that I'm going to be showing. It's just a citizen survey where you have a Google Form. It gets into the Google Sheet. And then we do a little of a sentiment analysis, whether the feedback was positive or negative. It gets to — and it could be another Google Sheet that goes here. And then a little final report connected to Google Sheets. So Make versus N8N, what do you recommend?

01:12:50 - Brandon Hancock
<A>Yeah. So if you are doing a single shot LLM call — like taking this exception, listen for changes, every time you find a change, find the row that was changed, look at the text, make an LLM call, save the result — if it's as simple as that, a single, always very simple, straightforward, Make is really nice just for its simplicity. ▶ However, if you're going to do anything that involves just any more than zero logic, N8N is pretty much the way to go.</A>

01:13:39 - alexrojas
Yeah, actually, in N8N, I'm able to do, in one of my agents, I do a local call to Ollama [tool:Ollama] by using Ngrok [tool:Ngrok]. So, I do everything local. <Q>Can you do the same for Make? Because, you know, I don't want these, like, the students to be paying for an API call. I would rather just do a server.</Q>

01:14:00 - Brandon Hancock
<A>I mean, yes, you could always make an HTTP call, but I can't remember — like, when it comes to actually using agents, I don't think Make's agents are as far advanced as N8N's agents. So, yeah, I don't know if they support Ollama. I know they do support just like the big boys, like straight up ChatGPT or Claude, but I don't think they do all the extra fancy stuff.</A>

01:14:27 - alexrojas
Then I'll try to do it with Ollama and Ngrok. And one more question, Brandon — you use a lot of Supabase [tool:Supabase] instead of Firebase [tool:Firebase] in several videos, like for vector stores. I don't know if I'm using ADK, would it be better to go to Firebase instead of Supabase?

01:14:53 - Brandon Hancock
<A>Yeah. So it depends really what you're doing. And I can just tell you that the main reason I use Supabase is I really just want a Postgres database. So that's the main thing that I want. So I just want to have a schema where I have a SQL database to where I can basically just say, like, I have tables. Here's what tables do. I just like structured data. When I was starting out doing a lot of web development, I loved Firestore for the document collection type of style. But as applications grow, the NoSQL practices — you want to write data where you read it, so you end up with a lot of data redundancy. So then things like you, internally as a developer, have to manage a lot more. So that's why I'm just like, I will make a simple SQL, I'll have a simple schema.ts file, and I will use Drizzle [tool:Drizzle ORM] to push the schema to my Postgres database. And it doesn't have to be Supabase. You could use Neon [tool:Neon] if you don't want to go to Supabase, and it would work just as well because Postgres as a whole, now, once you allow it to start doing vectors, you're good.</A>

01:20:18 - Bastian Venegas
Quick comment on the Make side — you can, as Brandon said, you can use HTTP requests. And if you're running Ollama through the CLI, there's a command `ollama serve`, and some instructions there I put in that picture, and you can expose it just as an API endpoint that you connect to Make, if you decide to go that way.

01:20:18 - Brandon Hancock
▶ Yeah, I think just copying your Ngrok approach, Alex, is a great suggestion.

---

<!--SEGMENT
topic: Google ADK Deep Dive — Artifacts, State, FastAPI Integration
speakers: Elad Weinstein, Brandon Hancock, Bastian Venegas
keywords: Google ADK, artifacts, in-memory session service, runner, ADK Web, callbacks, FastAPI, Streamlit, LangGraph, LangChain, CrewAI, byte stream, PNG, tool context, research assistant, EDA, CSV
summary: Elad, a university student in Cyprus building a research assistant for a non-profit (CSV → EDA → descriptive analysis), asks why ADK Web ignores his runner and artifact/state initialization. Brandon explains that ADK Web only looks for the root agent, not the runner, and recommends using before_agent callbacks to initialize state. He also demonstrates the correct way to save artifacts (reading as byte stream, using Parts.from_bytes), and shares a newly discovered ADK FastAPI integration function that wraps an ADK app as a FastAPI endpoint, simplifying deployment.
-->

01:20:41 - Brandon Hancock
All right, Elad, is that how you say it? Nice to meet you, man, how you doing, how can we help?

01:20:45 - Elad Weinstein
Thank you, Brandon, thank you, everyone — it was worth staying awake until 2 a.m., so.

01:21:03 - Elad Weinstein
So I'm currently doing a kind of university project for a non-profit research institute. So me and my team, we thought of kind of making like a research assistant that will be able to take raw database, raw data like CSV or Excel file and handle the whole process until writing, let's say, a fair descriptive analysis for an academic article. Like taking the data, like doing some basic EDA, then wrapping it up to a kind of, let's say, a review for the researcher, and then do some data manipulation to understand what is the standardized data manipulation, which is accepted in the same research institute, and then continue the process until writing this descriptive data analysis.

01:21:49 - Elad Weinstein
And I found it quite hard using all other systems like LangGraph [tool:LangGraph] or LangChain [tool:LangChain] or any other systems. Haven't tried CrewAI [tool:CrewAI], I have to be honest. But when I saw your crash course of Google ADK [tool:Google ADK], I'm not one of the YouTube survivors, so usually I'm cutting off after 30 minutes of courses, but this time it was a full pleasure of three hours.

01:22:22 - Elad Weinstein
And the only problem that I had was the artifacts. So I also saw another YouTube video that you had with the YouTube scraper with the thumbnails. And I saw that you did some artifacts there. Anyway, so I have the root agent, the dependencies and all the framework as you showed. And then I'm initializing a runner on the main.py. I wrote it on the thread on the community. And I initialized an in-memory session service and also an in-memory artifact service. Which I assigned to the runner. But for some reason, when I run ADK Web and I run the agent, I don't see not the state and also not the artifact. So I created an initial state with one key, a username. I don't see also this one. So it's like when I run ADK Web, it doesn't compile the runner with it for some reason.

01:23:23 - Brandon Hancock
<A>So quick heads up. ADK Web, when you run the CLI command, all it looks for is the root agent. It does not look at the runner at all. So if you were trying to do something with a runner, you can't do it. There is a workaround, though, and I'm happy to tell you how to do it. ▶ Basically, what you want to do is take advantage of callbacks. Specifically, if you're trying to do something super high level, you want to make an agent callback. And let's just say in that agent callback, you just went to set default date, initial state. So you could say like, hey, does this key exist? Like, is it none? If so, put in this value. Otherwise, just skip this. Like you could literally just put in state, you could put initialized. And then just to start, you would check if initialized is there. If it is — sorry, if it's not — put in all the initial state, and then swap the flag to true. That way, it won't accidentally reinitialize the state over and over and over again. So that's a quick way to get around not having to go set up a runner.</A>

01:25:40 - Brandon Hancock
Yeah, real quick on artifacts. I got to talk to them earlier this week. I told them the same thing. I was like, artifacts are hard. Like, it doesn't work. You can't tell. It looks like I did it, but it's not doing it. So I complained to them on Monday. So hopefully they're going to change something. But I do have an example.

01:26:28 - Brandon Hancock
Okay, so here's — I was working on a browser agent video for you guys. And basically, same thing, I wanted my browser agent to look at it, take a screenshot and look at it. So the key thing is, have a nice folder to save all your stuff. What you're going to do is have your driver — this was a web scraper — it was going to save the screenshot to a file path. And then now, what we need to do is prepare to read in that saved artifact to our ADK agent. ▶ So this is the only way I can get it to work — with opening a file and then just assigning the byte stream to image bytes. Once you have saved it, like once you are opening the file and you're looking at the byte stream, I then create a new artifact. So you do `Parts` — this is coming from the Gen AI kit — I'm creating this part from bytes, because that's what we're doing right here. And then you just pass in the type of data and then the MIME type. And in my case, was saving everything as a PNG file, so it was able to work. Once you do that, all you need to do is then do your `save_artifact` right here. So `tool_context.save_artifact`, give it a name, and then you can pass that artifact in right here. This is — I played with this like two hours trying to get it to work, because literally the same issue you're running into. So this one line doing this where I read in the byte stream and then do the `from_bytes` — this was the trick.

01:28:40 - Brandon Hancock
So just to say back to you — so you're saying if I create, like I do the web deployed version of ADK to where I have a runner that's sitting in front calling ADK, correct? You're saying about that approach, like how do we get artifacts working in there?

01:29:17 - Brandon Hancock
So let me show you something really fast. I'm just going to show you one of the best tutorials. But basically, all you're trying to do is just wrap your application in an API. And I don't know why they've made it so hard to find. But basically, all you're trying to do is just wrap your application in an API.

01:32:00 - Brandon Hancock
That's why I couldn't find the old one. ▶ They made a new function that turned your ADK application into a FastAPI endpoint, which is so much nicer than what it used to be because in the past, you had to set up the endpoints to run it, get the state. Like, there was so much that you had to do, but now, yeah, FastAPI. So, yeah, I would just follow this. [link:Google ADK FastAPI deployment documentation]

01:32:55 - Brandon Hancock
They're changing stuff literally weekly, so it's harder to recommend something just because they're trying to improve as fast as possible.

---

<!--SEGMENT
topic: Agent Framework Selection, Multi-Agent Marketing App, and ADK vs LangGraph
speakers: Kanav Arora, Brandon Hancock, alexrojas, Neel More, Robert
keywords: Google ADK, LangGraph, LangChain, CrewAI, multi-agent, sequential agents, parallel agents, web scraping, Firecrawl, vector store, Gemini 2.5, RAG, ACM, UCSB, PwC, marketing automation, Cursor workflow, master plan, task plan
summary: Kanav, president of ACM at UCSB, describes building a multi-agent marketing platform for local businesses (web scraping Yelp/Google reviews, multimodal content generation with VO3) and asks which agent framework to use for integration. Brandon explains the three types of AI applications (chat, RAG, agentic) and recommends ADK for hybrid chat+workflow use cases, while noting LangGraph is more enterprise-established. Neel and Robert ask follow-up questions about the Cursor master plan/task plan workflow and ADK vs LangGraph for new developers. Brandon strongly recommends ADK for beginners.
-->

01:42:36 - Brandon Hancock
Kanav, man, you're up next.

01:42:43 - Kanav Arora
Just to give you some context, I joined the course a few months ago, but recently, last week, grinded it out and finished the AI marketing. I'm a third-year undergrad at UCSB, and the reason why I started the course was, so we worked with multiple local companies and startups to solve AI solutions, or any software solutions, to be fair, and one of the most common ones that we heard was, oh, marketing is a real pain, can you guys help us out to do it, and that's why I started the program.

01:43:33 - Kanav Arora
Do you know ACM, Association of Computing Machinery? It's like a national student chapter — one of the biggest computer science organizations in US colleges. I'm the president of the ACM, UCSB student chapter. So we work with multiple companies. We are working with PwC right now to build them an AI financial forecasting platform. So we just work with multiple, so to give students exposure to work on real world problems, and companies get like a cheaper and like a place to explore different opportunities.

01:44:22 - Kanav Arora
And as I said, we were trying to — one of the most common problems we heard from local companies when we worked with them was, marketing is a real pain, right? They don't have the money to go and hire full-scale marketing agencies, and the current tools online aren't really that good. So I started trying to build a multi-agentic tool to basically build and post out marketing content. And then I came across your course, and I started doing that one, and it really helped.

01:45:28 - Kanav Arora
So, yeah, it was something pretty basic — completely what you did and then added and modified features to make it more specific for local businesses. In fact, I just started last week and just grinded it out completely over the weekend.

01:45:39 - Kanav Arora
And yeah, what I was thinking was I wanted to add more features. I wanted to add a couple of agents for, like, web scraping and searching, for example. Let's say there's a local restaurant and they want to — the owner just talks to the chat for a minute. I wanted to go and scrape the entire internet for local Yelp reviews or Google Maps reviews and get those reviews to add context to the marketing, get information about what local other marketing campaigns have been like, and then basically add more context for them to go and post out the marketing content and then make it multimodal — instead of just text, I wanted to add — right now with VO3 [tool:VO3] and like so many other cool Stability AI features, the content can be more than text.

01:46:30 - Kanav Arora
<Q>So I just wanted to ask a couple of questions. One, how would you just like — what framework to use or like how to integrate it into a current system? Because I've done a lot of projects of using these multi-agent orchestrators, but never integrated into your application. And before I start, I want to get your understanding about what do you think is a good one with integration? I think you had mentioned that Google ADK has a bunch of issues with application layer stuff, but in general, what would you suggest for a case?</Q>

01:46:58 - Brandon Hancock
<A>So, dude, absolutely love that you were cranking out all this code in college and just absolutely getting after it. I love the entrepreneurial spirit, man. So, but on the technical side of things — the application that, like, the AI marketing platform, one that you're building, is more of a process automation, like, using LLMs to automate a process. Like, that is that workflow. So, real quick, just taking a step back, there's really three different types of applications in the AI space right now. There's just, like, pure AI chat. So, there's some sort of special prompt to where the user's talking to that prompt. It's multimodal. Life's good. Okay, in the middle, there's RAG applications. That's usually the second major type you're going to see. The third type is going into agentic applications. When, if you break that apart, there's two major types of agentic applications. First, there is the workflow types to where it is just constant, like I give an input, and then it goes A, B, C, D, gives me an output. That's like the workflow. That's traditionally CrewAI. That's what you could expect to see. CrewAI is a workflow automation toolkit or agentic tool. Now, Langraph also kind of falls into that as well, I'd say workflow. Now, going off of what you just said of like you wanted the user to be able to like chat, I'm now an insane fan of ADK, strictly to do what you just said to where it's actually a hybrid. Like I want to be able to chat with the agent to go say like, hey, I'm looking to see what's happening in the local market. Can you explore for me? The chat agent goes, yeah, I can, and delegates that work to a like local research agent who first scrapes Yelp, Google. And then something else, and then reports the results back. So I'm a huge fan of ADK for that reason because it's like you get all the benefits of chatting and you get the ability to do those workflow agents, like the sequential agents.</A>

01:53:25 - Kanav Arora
<Q>Yeah, the only main question that comes down to it — I think it's hard because I started with LangChain and there's so many new tools every day that come out. I'm not sure, okay, now this is out, should I switch to the new tool right now? How do you decide which tool to use and how to switch, when's the right time to switch, or stuff like that?</Q>

01:53:43 - Brandon Hancock
<A>Real quick, are you good with LangGraph or specifically LangChain? I mean, if you've used version 3 of LangChain and LangGraph, I mean, if that's what you're familiar with, like, you're not going to go wrong continuing to use it. There's definitely not a wrong answer. I mean, there are some, like, fundamental requirements. Like, if you need chat, I would not use CrewAI because they're just not, like, a chat-based system. They're more of a, like, workflow-based system. So that takes them out of the loop. But if you are doing that and workflow, the last two you have are ADK and LangGraph. I will say, if you were just starting out and I was to pick one, I'd say ADK. But if you already have experience with one, I mean, seriously, you can't go wrong with LangGraph. They're probably the more enterprise-y example right now just because they've been so established. So, and especially, like, you being in school, man, like, the amount of bigger companies that are using LangGraph because, you know, LangChain's been out since ChatGPT came out — so it is the dominant one in play right now. So if you're trying to go more enterprise-y, yeah, I would definitely say stick to LangGraph then.</A>

01:55:43 - Brandon Hancock
All right, Alec, you're up next, man.

[Aleksandr's Telegram bot segment follows — see next segment]

01:59:30 - Brandon Hancock
Neel, any final questions?

02:00:00 - Neel More
No, that was a great demo. And also, like, for this master and the task plan, right? Have you tried the task master or are you using any specific tool for creating this? From master to the task plan?

02:00:28 - Brandon Hancock
Oh, no. I mean, it's mostly just me talking into — let me just show my screen really fast. So, like, usually when I'm working on creating a master plan, at this point, I would have pasted in — I'm using, I'm always — I cannot tell you enough, guys — I'm always using Gemini 2.5 Pro [tool:Gemini 2.5 Pro]. The context on this thing is insane, which is crucial for creating your master plan. ▶ And what I'm usually doing is taking a screenshot, pasting it in, and then I'm just like talking. So like, I'll do this, like, hey, I'm trying to come up with a master plan that I'm going to continually reference throughout the project as I'm creating this web application for a client. As you can see, I've uploaded a requirements document. I've uploaded screenshots of wireframes, yada, yada, yada. Here's what's happening in the wireframes. And then like, I literally will just talk for like four to five minutes straight to say, create the initial draft. And then I'm going to review your initial draft. And we're going to plan things out together for the structure of the application.

02:29:26 - Brandon Hancock
▶ Also — I'm a dummy, I'm so sorry — that whole time I was showing this, it didn't share my screen. But yeah, are you on a Mac? If you're on a Mac, what you can do is update your keyboard to where you just hit command twice, and you can start talking into Cursor. So this is a tip I always do — so I don't, like, as a software developer, it's kind of sad, because I never code anymore, and I never type — I'm always just talking. And taking screenshots, and narrating, almost like I'm talking to employees. So that's how I'm able to get stuff done so much faster.

02:31:16 - Brandon Hancock
▶ Yes. And a few quick reasons why ADK. It is insanely easy to start creating agents, because you really just make an agent.py file, and boom, you run `adk web`, and you're chatting with an agent. Insanely easy to spin up. And when you want to start to do most basic workflows, they have the core raw ingredients you need. Sequential agents, loop agents, and parallel agents. And which is what you need to do 99% of the time. Now, LangGraph, if you're going to do some really complicated stuff to where it's like branching and circles — yes. But for most workflows, it usually follows one of those raw patterns to where you're looping through something, you're doing five tasks at the same time. So for 90% of what you're going to be doing as a developer, ADK is crushing it right now with how straightforward it is to start taking action and testing it out.

---

<!--SEGMENT
topic: Content Strategy, New Tools, and Session Wrap-Up
speakers: AbdulShakur Abdullah, Brandon Hancock, Richard Richard, Robert, Neel More, Aleksandr
keywords: YouTube content strategy, vibe marketing, listicle, how-to video, newsjacking, factory.ai, napkin.ai, AI consultant, SaaS pricing, Telegram bot, Railway, cookies, environment variables, ADK playlist, A2A, artifacts, deployment
summary: AbdulShakur asks about content strategy for a vibe marketing YouTube channel; Brandon outlines a progression from welcome video → listicle → how-to → newsjacking → frameworks. Richard introduces napkin.ai for generating presentation diagrams and discusses an AI playbook SaaS concept for businesses. Aleksandr demos a Telegram bot with Spotify/SoundCloud/YouTube download features and admin broadcast panel, troubleshooting Railway cookie deployment issues. Robert and Neel discuss the Cursor master plan/task workflow and ADK playlist. Brandon closes with upcoming content plans: A2A, artifacts, and ADK deployment videos.
-->

01:33:24 - Brandon Hancock
Abdul, you're up next, man. Loving the shades.

01:33:27 - AbdulShakur Abdullah
I had my pupils dilated, so I can't really see very well.

01:33:41 - AbdulShakur Abdullah
So today has kind of been a non-work day. I have kind of two questions, two parts. One is how do you go about kind of planning out your content strategy and what you're going to release and do videos on? Because I'm trying to plan mine out now. I'm running into this, oh, I'd love to do that, but no, would that even work, or would people like that, and just the whole circle around, where then I feel like I'm not going anywhere.

01:34:12 - Brandon Hancock
Dude, so it's so funny you say this, because like, so I just wrapped up the AI Authority Accelerator, and like, there's an insane amount of complexity you can go into to like, picking how to start, what to start on. Let me give you the short answer. Okay, so you want to pick an avatar first. I'm assuming you're talking about wanting to help AI developers, who I'm assuming you're wanting to focus on, or are you targeting someone different?

01:34:41 - AbdulShakur Abdullah
So I decided to target on people who want to use Vibe Marketing, so how to build those tools in a regulated environment. That's my current focus.

01:35:06 - Brandon Hancock
So let me give you, in two minutes, let me give you the entire crash course of the AI Authority Accelerator. Okay, so week one, I had everyone make a quick welcome video where they basically just said to the world, hey, here's who I am. Here's what I'm going to be talking about on this channel. Here's why you should listen to me. Here's what you can expect next. And that was just a quick video just so you can get reps working on creating content. Literally, it's a one-minute video.

01:35:44 - Brandon Hancock
From there, we do our first listicle. With a listicle, what we focus on is just like, we just want another rep of making a 15-minute video. We're not solving the world in a single video. We're doing a listicle, which is basically just like five tips, five examples, five tools, five whatever, but just a quick video. Don't go super deep. It's just it gets another rep of making a YouTube video.

01:36:08 - Brandon Hancock
From there, we go into how-to videos to where you're going to teach people how to solve a single problem. And when I mean a single problem, I really mean a single problem. So like, for example, in yours, like vibe marketing, like how to — just how do you want to solve a single problem? Because what can happen is like, some people are like, oh, how to build your first AI application. Well, that is an insanely big how-to, you know, because there's like 30 videos under that. So if you do find yourself solving too big of a high-level problem, cool, just go one level deeper and then focus on that.

01:36:52 - Brandon Hancock
From there, there's a bunch of other things you can do. Newsjacking. So if something cool happens with vibe marketing, talk about it. But the other thing that you can do is frameworks. So there's a framework that you find. So how like Bastian just showed us that really cool tool — like I 100% am like, I need to make a video on that. So like anytime a new tool comes up, give a demo on it, give an update on it and show people how to use it.

01:37:13 - Brandon Hancock
▶ So yeah, that's what I would do. I just would like — just go ahead and like — I know this is like the worst advice, but I would just start. We can talk more about it later too next week. But like, I would just pick one that you could do in 15 minutes because you're never — it is not a — people think home runs when they think on YouTube, worst way to think about it. It is no, Mr. Consistent. So he who makes one to two videos every week for a very long time wins because you're not really competing against others. You're just competing against yourself because everyone else quits. So as long as you just don't stop, like you're going to get a lot of traction.

01:39:00 - AbdulShakur Abdullah
In this new tool that came out, factory.ai [tool:factory.ai] — can you see my screen? So apparently it is one of the AI kind of building agents that just came. It's been out for a bit, but it's kind of been very closed beta. Where they're only working with enterprise clients. So they just decided to open it up to everyone outside of enterprise clients. So it has — they go about doing it in terms of droids. Where you, first you're teaching how to use this product droid. Your product droid that actually tells you how to plan the different features, create, manage. Your knowledge droid. Your coding droid and your reliability droid.

01:40:09 - AbdulShakur Abdullah
So I did have a request. <Q>Could you do a battle video where you kind of put all the different coding tools to the test? Like who can one-shot the best?</Q>

01:40:23 - Brandon Hancock
Yeah, that's crazy. So out of curiosity, so $40 a month per team or per seat. Do they have a video of what it does? Because like, that's like the hard part about like all these tools is like, I just want a video demo of it working.

01:41:00 - AbdulShakur Abdullah
But the Next Wave podcast, they did a little intro video on it where he prompted it, and then at the end, they had a working demo of, like, a DocuSign clone. [link:Next Wave podcast - factory.ai demo]

01:55:46 - Aleksandr
Hi, nice to meet you. Thank you for the opportunity to explain about my bots. And now I continue to work. With some functions, I add some new things, and now I developed some new very big things, because now people who use my bot can download different music from Spotify or SoundCloud or YouTube for free.

01:57:03 - Aleksandr
First of all, I'd like to start with YouTube. You can see this beautiful YouTube channel, yeah, and we can make a link from this YouTube video. Send my bot. Only send a link, and you can download the audio from this video or different categories.

01:57:52 - Aleksandr
But I have a very big problem with a new function. I added some cleanup function to remove some not-used cookies and useless information from my bot to make not so big files inside, but this collection cleaned all my cookies that used in this Railway [tool:Railway] and now I can't — only today I have this problem.

01:59:40 - Brandon Hancock
Just real quick, just to make sure you're saving those as your cookies. ▶ I would not save those to GitHub. I would usually just save those as environment variables if possible. Because, like, for whatever reason, if you actually save it to a public repo, some things could go wrong.

02:02:03 - Aleksandr
In my admin account, I can make a panel that I can make a text, photo, or audio, or video, and then I can send to all people that use my bot.

02:02:21 - Brandon Hancock
Dude, this is awesome. Well, hey, please keep up with the progress, and yeah, I'd love to see next week if you're able to get it fully deployed on Railway and working with the cookies.

02:14:44 - Richard Richard
Also, I just wanted to leave you with this tool. I don't know if anybody uses napkin [tool:napkin.ai]. It is free, but it will like take and make little things for your presentation. Like, you give it like a little prompt and it makes these little diagrams. I mean, it's so cool. Like, I mean, you can add them to your PowerPoint. You can add them to your proposals for your clients. And right now, if I'm not mistaken, it's still free. So, but it is a really amazing little tool, a good little gem that you guys can use. And like I said, you can add it into any presentation. If you were doing like deep research for a company and you wanted to present a really nice looking report with infographics, then this is where you — yeah, it's sick. [link:napkin.ai]

02:15:34 - Brandon Hancock
▶ If you wouldn't mind doing a post on this, just like a quick, like, three sentence post of like, hey guys, this thing is amazing. And like a quick screenshot of like, hey, it's free to get these kind of stuff.

02:34:09 - Brandon Hancock
I have a few things coming up next. Like I want to do A2A. I think you guys are really going to like that. It is a little bit more complex, but it's crazy how powerful it is once it's set up. Artifacts is another one in deployment. So those are the main three that I have on the ADK frame that I'll continue to add to that playlist. And seriously, if you guys have other ideas or feedback or questions, let me know. And I'm always happy to crank out more content.

02:35:00 - Brandon Hancock
Happy birthday to Maksym and great to work on your business. Thanks. Bye, guys.

---

=== UNRESOLVED SPEAKERS ===

- **sam** — raw name "sam" not found in SPEAKER_ALIASES map; passed through unchanged
- **Richard Richard** — raw name "Richard Richard" not found in SPEAKER_ALIASES map; passed through unchanged
- **Robert** — raw name "Robert" not found in SPEAKER_ALIASES map; passed through unchanged
- **alexrojas** — raw name "alexrojas" not found in SPEAKER_ALIASES map; passed through unchanged
- **Aleksandr** — raw name "Aleksandr" not found in SPEAKER_ALIASES map; passed through unchanged
- **Jake Maymar** — raw name "Jake Maymar" not found in SPEAKER_ALIASES map; passed through unchanged
- **Elad Weinstein** — raw name "Elad Weinstein" not found in SPEAKER_ALIASES map; passed through unchanged
- **AbdulShakur Abdullah** — raw name "AbdulShakur Abdullah" not found in SPEAKER_ALIASES map; passed through unchanged
- **Kanav Arora** — raw name "Kanav Arora" not found in SPEAKER_ALIASES map; passed through unchanged
- **Neel More** — raw name "Neel More" not found in SPEAKER_ALIASES map; passed through unchanged
- **Juan Torres** — raw name "Juan Torres" not found in SPEAKER_ALIASES map; passed through unchanged
- **Bastian Venegas** — raw name "Bastian Venegas" not found in SPEAKER_ALIASES map; passed through unchanged
- **Maksym Liamin** — raw name "Maksym Liamin" not found in SPEAKER_ALIASES map; passed through unchanged