=== SESSION ===
date: unknown (Tuesday community call)
duration_estimate: ~2 hours 40 minutes
main_themes: AI development tools and frameworks, second-brain/PKM systems, Convex backend, Kimi K2 and Chinese AI models, OpenAI Agents browser automation, Cursor cost management, CrewAI Enterprise debugging, ADK vs LangGraph comparison, micro-SaaS opportunity window, superintelligence and post-labor economics

---

<!--SEGMENT
topic: Opening Chat and Limitless Pendant
speakers: AbdulShakur Abdullah, Bastian Venegas, Tom Welsh, Ty Wells
keywords: Limitless, AI pendant, transcription, API, Otter, Noda, AppSumo, lifetime deals, voice recording, meeting notes
summary: The session opens with informal check-ins. Bastian introduces the Limitless AI pendant, which records conversations and produces transcriptions via API. Discussion pivots to voice-recording tools including Otter and Noda, and the group reflects on how the rise of AI has reduced the appeal of AppSumo lifetime deals since many features can now be self-built.
-->

**00:00:59 - AbdulShakur Abdullah:** Hey, how's it going, guys?

**00:01:58 - Ty Wells:** Okay.

**00:02:00 - AbdulShakur Abdullah:** Hey, Vashem.

**00:02:03 - Bastian Venegas:** Hey, guys.

**00:02:09 - AbdulShakur Abdullah:** Vashem, what project are you working on these days?

**00:02:17 - Bastian Venegas:** I'm doing something with Limitless. [tool:Limitless] I'll show you a screenshot.

**00:02:30 - Tom Welsh:** Hey, all.

**00:02:40 - AbdulShakur Abdullah:** How's it going in the UK?

**00:02:47 - AbdulShakur Abdullah:** The UK government doesn't want you to know.

**00:02:49 - Tom Welsh:** Still going okay, even though I was muted.

**00:03:41 - AbdulShakur Abdullah:** <Q>What is a Limitless conversation?</Q>

**00:03:47 - Bastian Venegas:** <A>It's an AI pen that basically records everything and writes a transcription. And you can do an API.</A>

**00:03:59 - AbdulShakur Abdullah:** That's cool.

**00:07:46 - Jake Maymar:** Hey, welcome.

**00:07:56 - AbdulShakur Abdullah:** You know, since the age of AI really took off, I have not purchased any AppSumo [tool:AppSumo] deals. I was actually thinking to myself, who's still buying them when a lot of these things you can quickly spin up yourself now?

**00:08:11 - Jake Maymar:** Yeah, I think that was just like a very short runway.

---

<!--SEGMENT
topic: Personal Knowledge Management and Second Brain Tools
speakers: Ty Wells, AbdulShakur Abdullah, Jake Maymar, Brandon Hancock
keywords: second brain, Obsidian, Notion, Otter, Airtable, Siri shortcut, prompt database, PKM, note-taking, task management
summary: Ty Wells raises a practical problem: capturing fleeting ideas and prompts across multiple projects without losing them. The group discusses tools including Otter, Obsidian, and Notion as second-brain solutions. Brandon Hancock advocates for Notion as his primary PKM, and the conversation establishes the need for contextual awareness across a personal knowledge base.
-->

**00:04:39 - Ty Wells:** <Q>So I've got a question for you guys. I've got like juggling so many different things, and stuff falls between the cracks. I use a Siri shortcut to record things because I'll always have my phone, but will I actually turn and look at that? Right now it just puts it in an Airtable [tool:Airtable] database. I need something to remind me to go look at it and tie it to a specific project. Is anybody using anything to help manage that?</Q>

**00:06:00 - AbdulShakur Abdullah:** <A>A while back, I was using Otter. [tool:Otter]</A>

**00:06:11 - AbdulShakur Abdullah:** I stopped because I found this lifetime deal for this Noda app [tool:Noda]. I got a lifetime deal for that one. So I haven't paid for that for several years, and it's still recording for me. But I do still sometimes use Otter from my phone because it is a lot better. And since the age of AI, they've added a lot of features where you can search through different conversations. You can get action items sent to you.

**00:07:07 - AbdulShakur Abdullah:** I'm saying they've added a lot of features in this last year, giving it the ability to do more. I personally haven't used them because I still have the one that I have the lifetime deal for.

**00:08:30 - Jake Maymar:** <Q>So are you looking for like open source? What are you trying to do?</Q>

**00:08:34 - Ty Wells:** <A>I'm trying to organize my projects and my notes and so forth, but not just to record it at some point, but to offer a follow-up with me. I may have like a great prompt or something that I put in my prompt database and I forget it. I need something to be contextually aware that, hey, do you have something like this already?</A>

**00:09:28 - Jake Maymar:** Yeah, no, I think that's really smart. I've been trying to build this. I've been calling this the second brain. And kind of working with other friends to sort of figure out the best way to do this. It's gotten a lot easier.

**00:10:40 - Jake Maymar:** So there was — Obsidian? [tool:Obsidian]

**00:11:05 - Brandon Hancock:** Notion [tool:Notion] is my go-to, my baby. It's how I remember everything in my life. And now that they got Notion AI, you know all about it.

---

<!--SEGMENT
topic: Brandon's ShipKit Templates and ADK Demo
speakers: Brandon Hancock, AbdulShakur Abdullah, Bastian Venegas
keywords: ShipKit, task templates, GitHub repo, Next.js, ADK, Google Agent Development Kit, multi-agent, cursor rules, Presentify, serial entrepreneur
summary: Brandon Hancock shares a task template freebie from his GitHub repo, designed for full-stack Next.js projects, available for 24 hours. He then attempts a live demo of his ADK (Google Agent Development Kit) ShipKit template, which shows a multi-agent system with a real-time timeline of agent activity. The demo encounters a database configuration error but the concept and roadmap are explained.
-->

**00:11:36 - Brandon Hancock:** So, what I'm doing real fast — dropping this in chat. I've been talking a bunch about task templates. I went ahead and I'm actually going to be recording a video on task templates tomorrow. In that GitHub repo [link:GitHub repo shared in chat], I'll share my screen so you guys can see it. I'm sharing, just as a nice freebie, the task template.

**00:12:00 - Brandon Hancock:** ▶ This literally is the thing I've been using to help build out all of my full-stack, web-based projects — Next.js [tool:Next.js]. This thing just absolutely crushes it. So feel free, download it, use it. I'll be adding cursor rules [tool:Cursor Rules] at some point to this as well. This will be in here probably for the next 24 hours.

**00:12:46 - Brandon Hancock:** All three templates that I've been working on for ShipKit [tool:ShipKit] — all templates are there, pretty much working. Just needs a few final pieces of cleanup. So the ADK [tool:Google ADK] one is working.

**00:14:07 - AbdulShakur Abdullah:** <Q>How is it different from Greg Eisenberg's idea validator thing? What's the distinguishing feature?</Q>

**00:14:16 - Brandon Hancock:** <A>So this is more of a template that just shows how to use ADK. The insane value is more of just — it's literally a copy-and-paste ADK clone.</A>

**00:15:21 - Brandon Hancock:** So this is basically the ADK thing. Basically, you get to use agents. So it's a multi-agent system fully set up. It shows in real time a timeline of what's going on in agent land. So you get to see in your app who's doing what, how it's working. And it looks really, really clean. ▶ So if you're working on workflows at all, where you want to automate things for your users, ADK workflows are insanely good.

**00:17:18 - Brandon Hancock:** So the guys who made Presentify [tool:Presentify] — I got to connect with him. I'll actually get to do a video with him. He's almost like a serial entrepreneur. He's made so many productivity tools, everything from Screenie to Deduce to Presentify. So he's made basically tons of applications. If there's any questions you guys have, I'll make a post right after today's call.

---

<!--SEGMENT
topic: Gemini CLI with Cursor and Parallel Coding Workflow
speakers: Brandon Hancock, Tom Welsh
keywords: Gemini CLI, Cursor, Claude Code, parallel tasks, tab limit, token burn, manager mindset, AI coding workflow, vibe coding, productivity
summary: Tom Welsh asks about using Gemini CLI alongside Cursor, referencing Brandon's video. Brandon explains his workflow of running multiple Gemini CLI or Claude Code terminal sessions in parallel to overcome Cursor's tab limit, enabling him to manage five to six coding tasks simultaneously as a reviewer rather than a coder. He notes Cursor has since raised its tab limit, reducing the need for this workaround.
-->

**00:19:34 - Brandon Hancock:** Tom, I saw you had a question. Could you talk a bit more about Gemini CLI [tool:Gemini CLI] plus Cursor [tool:Cursor]? You touched on it in your video but didn't go too much into it.

**00:19:48 - Tom Welsh:** <Q>Yeah, was basically just wondering — it looked like you're alluding to you could put Gemini AI into Cursor and use Cursor to interrogate Gemini CLI, with a whole bunch of other stuff working along with the tools that are already inside Gemini. Am I down the wrong track?</Q>

**00:20:07 - Brandon Hancock:** <A>No, that was pretty darn close to what I was suggesting in the video. When I recorded that video, the main limitation of Cursor is that it only allowed you to do three tabs at the same time. So in order to get five, six, seven — because I'm always just cranking out multiple things at once — the workaround is to use Gemini CLI or Claude Code [tool:Claude Code] and just opening it down in the terminal. That's how I was getting to work on five or six tasks in parallel to where I became more of a manager rather than a coder.</A>

**00:20:48 - Brandon Hancock:** ▶ At this point, you should never be writing another line of code. It's always review, review, clarify, review, approve.

**00:21:08 - Brandon Hancock:** Now at this point, I just have five or six of these up at once because Cursor bumped the limit. So I really haven't seen a need to use the terminal anymore, except when Cursor craps the bed. On Friday, they broke it for a little bit — you could ask it anything and it would take 30 attempts to just do it. And they were glad to burn your tokens while they made a mistake.

---

<!--SEGMENT
topic: Opal by Google and N8N Workflow Builder Updates
speakers: Brandon Hancock, Paul Miller, AbdulShakur Abdullah, Jake Maymar, Ty Wells, Al Cole
keywords: Opal, Google, N8N, agentic workflow, no-code, workflow builder, MCP, natural language workflow, Zapier alternative, voice-to-workflow
summary: Paul Miller shares his experience with Opal, Google's new agentic workflow tool, noting it maps out agentic flows from a plain-language task description without requiring code. The group discusses whether Opal threatens N8N, and Jake Maymar reveals N8N is imminently releasing a natural-language front-end for building workflows. The segment also covers using Claude Desktop's MCP integration as a workaround for building N8N flows.
-->

**00:21:50 - Brandon Hancock:** Paul, Q2 — have you got to play with Opal? [tool:Opal]

**00:22:00 - Paul Miller:** <A>Yeah, I think the cool thing with it is you can look at the prompts that it creates as you put something together. I raised a point last week about how you can boost your CRM with understanding your opportunities and doing some deep research about that, and then put that together as a pitch document for your business. You name your business, and it created all the steps for it, and the prompts were really quite clever in the way that it thought it out. So it's like you give it a task, but it will map out how you should set up your agentic flow to deliver it without having to do any code.</A>

**00:23:14 - Paul Miller:** Yeah, you have to use a personal account. You've got to be VPN'd into the U.S. to use it as well.

**00:24:06 - Brandon Hancock:** Did Opal kill N8N? [tool:N8N] I don't know, just because it's super easy to make workflows. Obviously, they're not as advanced as N8N, but the way I've seen it, where you can just talk and it updates — it's wild to me that N8N has not done that yet.

**00:24:32 - Jake Maymar:** N8N is about to do that. In a couple weeks.

**00:24:38 - Ty Wells:** Ooh, that stings — Google beat them.

**00:24:44 - Jake Maymar:** There's an MCP also that you can just basically build out workflows, but it's not very good. That's the problem.

**00:24:53 - Ty Wells:** Yeah, they're putting their front end so you can basically prompt, and it'll build the workflow. That's what they're doing.

**00:25:00 - Al Cole:** You have the same thing with MCP and automation as well, right? You can essentially, in Claude [tool:Claude], build out your flows.

---

<!--SEGMENT
topic: Convex Backend Framework Deep Dive
speakers: Brandon Hancock, Bastian Venegas, Jake Maymar, Tom Welsh, Al Cole
keywords: Convex, Supabase, React, TypeScript, real-time, Chef, Drizzle, PlanetScale, file storage, blob store, Theo, backend-as-a-service, type-safe
summary: Bastian Venegas demonstrates his Limitless pendant project built on Convex, explaining how it provides real-time database reactivity, TypeScript-native schema definition, and a tightly integrated React backend. Brandon and the group compare Convex to Supabase, discuss the Chef scaffolding tool, pricing, file storage capabilities, and reference YouTuber Theo's strong advocacy for Convex. The segment covers practical tradeoffs versus Supabase for AI-native full-stack projects.
-->

**00:25:26 - Brandon Hancock:** Real fast, Jake was asking thoughts on Convex. [tool:Convex] Bastian, would you mind sharing your screen?

**00:26:05 - Brandon Hancock:** Okay, so Convex — what is it? Why is it cool? It's got an insane amount of traction recently from Theo [tool:Theo (YouTube)]. If you're not watching him on YouTube, he is the GOAT. He has been going all in on Convex recently. ▶ Basically, it just simplifies the way back-end and front-end are connected. Everything's type-safe, there's real-time connections, and there's a ton of benefits of using it. It's like Supabase [tool:Supabase], but a little bit more clean.

**00:26:49 - Bastian Venegas:** <A>Yeah, it's exactly what you're saying. The mission is like the missing part of your React backend. It really feels like real time. You kind of just set it and forget it in terms of having to refresh the pages every time the state changes or the database is updated. You just see it appearing in real time. And you can also build functions here that interact directly with the database. All of your database lives in this Convex folder. And here you have the schema, which is all just TypeScript. This feels similar to using Drizzle [tool:Drizzle] maybe, but the user experience is very different.</A>

**00:27:54 - Bastian Venegas:** This is using my Limitless pendant. It's fetching the data from the API, and then the database is actually the one that's processing all of these transcriptions — to extract if there is a to-do, a reminder, a meeting, or whatever. You can scaffold the initial project in this tool that they have called Chef. [tool:Chef] They also provide this cursor rules file, particularly for the database, and you can just add this like you would add any markdown file to the context.

**00:29:54 - Tom Welsh:** <Q>Bastian, did you say that had Chef in it? Is that the configuration line?</Q>

**00:30:04 - Bastian Venegas:** <A>Chef is the tool — like you would say Lovable [tool:Lovable], but it's their thing. They build a byte application similar to what Lovable does. But they also add this Convex folder where everything that has to do with the database lives.</A>

**00:31:12 - Brandon Hancock:** Just looking at the pricing real fast, guys — it is actually really affordable, because I think Supabase is close to $20 a month for something very similar.

**00:31:47 - Brandon Hancock:** <Q>I would be curious if they have a blob store, because whenever I looked at picking an AI stack, I was like, I need one place to put my cloud functions, my vector store — it needs to have everything. When I was looking, it didn't have a blob store, so I stopped going down the Convex path.</Q>

**00:32:16 - Jake Maymar:** <A>Yeah, they do have some kind of file storage.</A>

**00:32:48 - Brandon Hancock:** ▶ I can also drop a video to what Theo was saying about it, because he uses it religiously. [link:Theo YouTube video on Convex shared in chat]

---

<!--SEGMENT
topic: Community and Content Strategy — School, Prompts, YouTube Growth
speakers: Brandon Hancock, AbdulShakur Abdullah, Jake Maymar
keywords: School community, prompt library, YouTube, LinkedIn, content strategy, value ladder, Dan Coe, Alex Hormozi, free community, audience building, top of funnel
summary: Brandon explains why he made his School community free — as a long-term relationship and opportunity play — and advises Abdul on building a prompt library community. Brandon outlines a content flywheel strategy: publish free value on social media, use engagement as signal, then climb the value ladder from tweets to YouTube to courses to consulting. He cites Dan Coe's framework for validating content ideas before investing in paid products.
-->

**00:33:18 - Brandon Hancock:** Abdul, you were curious — I wanted to know how come you made the School [tool:School] community free. I'm asking because you were thinking about making one around prompts.

**00:33:35 - Brandon Hancock:** Main reason I made School free was basically a long-term play. I've gotten so many cool opportunities. Like, it's worth the $99 to me to just get to meet and make all these cool connections. So literally if nothing more than that, it's infinitely paid for itself for years.

**00:34:50 - AbdulShakur Abdullah:** So I was thinking — I was kind of getting tired of jumping on all these different tools where I stick all of my different prompts to find them. So I made, well, I'm making a prompt library where I can just throw them all in there. And then I was like, oh, it'd be really nice if other people could kind of throw their prompts in there too and have like a community prompt library. I thought about charging for the prompt library. Then I was like, no, I don't really want to charge because I want people to put their prompts in there and share. And I want the best prompts to float to the surface. So then I thought, okay, well, how can I afford to sustain the prompt library? And then I was like, maybe I'll have a School community that branches off where I get people to come and show how to really engineer really strong prompts.

**00:35:52 - Brandon Hancock:** ▶ For the first year, really two years, I was like, don't charge for a single thing. Give everything away for free, be valuable. And then in return, you will get growth. Even though it's highly uncomfortable where you're like, holy crap, this is the best thing I've built and I'm just giving it away for free on YouTube — it feels wrong, but you're going to build something else that's even better.

**00:37:12 - Brandon Hancock:** ▶ Use social media as the testing bed for traction. If it gets traction, double down and keep doubling down. Dan Coe [tool:Dan Coe] basically had a really cool insight: if you can share a tweet and it is insanely valuable, you'll get a ton of traction. Cool — that's social proof that you probably need to make a deeper dive on YouTube. Does the YouTube video do well? Okay, cool — that means you could either do a small course around it. Oh, the course is doing well? Cool — that means you could do consulting around it. By using social proof, you can keep going up the value ladder.

---

<!--SEGMENT
topic: Kimi K2 Chinese AI Model and Cost Arbitrage
speakers: Juan Torres, Brandon Hancock, Paul Miller, Jake Maymar
keywords: Kimi K2, Chinese AI models, OpenAI, API endpoint, Base10, H100, open source, cost comparison, Anthropic, Claude Code pricing, token cost
summary: Juan Torres advocates for Kimi K2, a Chinese open-source model he finds comparable to OpenAI's premium $20/month models, available free via web interface. Paul Miller adds that Kimi K2 can be used as a drop-in backend for Claude Code at roughly 80% lower cost than Anthropic. Brandon references Base10.co as the hosting provider Maxim used for production voice agent deployment, noting the model requires approximately 10 H100 GPUs.
-->

**00:38:53 - Juan Torres:** So, I've used Kimi K2 [tool:Kimi K2], and it's really powerful. I've just used the cloud version. And it has, I would say, the same prowess as OpenAI's [tool:OpenAI] $20 premium models. I'm telling you guys, you've got to really see the Chinese AI models. They're really powerful. They're going to out-compete the monopolies here in the U.S. sooner or later. ▶ So I would recommend you guys try it out. Kimi K2.

**00:39:33 - Brandon Hancock:** Maxim is the only one that I've known who's actually used it in a production setting, and he was using it for quick decision-making for his voice agent. And it was the only open-source model that was fast enough, smart enough to actually be on par with like a Claude or an OpenAI.

**00:40:04 - Juan Torres:** <Q>Not even deployed on AWS. It's just like the link that I just shared with you. You can create an account there and start using it. And it has a pretty decent, I would say even like, agentic modality without having to actually use it. And it uses the same formatting that Perplexity [tool:Perplexity] has in order to web search everything. The only thing is that in order to finish the task, it takes a pedantically large amount of time to finish a report. But I mean, it's free.</Q>

**00:41:18 - Brandon Hancock:** Base 10 [tool:Base10.co]. [link:base10.co] That's how he was doing it. Because it takes like 10 H100s synced out — it's a monster. It takes almost a terabyte of memory, so 10 H100s put together.

**00:41:57 - Paul Miller:** <A>Yeah, so you point it — instead of it going to Anthropic, using up all the Anthropic stuff — you point it to a Kimi K2 host, and it uses Kimi K2 instead of Anthropic.</A>

**00:42:45 - Paul Miller:** ▶ Kimi K2 is really good. It's at least 80% less cost than Claude.

---

<!--SEGMENT
topic: Cursor Costs, Claude Code Pricing, and Token Arbitrage Strategies
speakers: Brandon Hancock, Mitch, Jake Maymar, Sam, Al Cole, AbdulShakur Abdullah
keywords: Cursor, Claude Code, Warp, token cost, pro plan, billing, parallel tasks, task documents, PRD, spec design, Claude Desktop, rate limiting, cost management
summary: The group digs into the real-world costs of AI coding tools. Brandon reveals he spent ~$220 in a month on Cursor running three parallel projects. The group shares strategies to reduce token spend: using Warp terminal as a free alternative for executing task documents generated in Cursor, using Claude Desktop for PRD/spec design before bringing work into Cursor, and structuring task documents to minimize redundant context. Jake notes Claude Code's $200/month plan is effectively unlimited but that Anthropic is clamping down due to Swarms abuse.
-->

**00:42:16 - Mitch:** The reason why I'm asking is because I was putting a hurt on my wallet, and I was like, okay, what other tools can I use instead? And Bastian put me on — what is it?

**00:42:37 - Brandon Hancock:** Warp. [tool:Warp]

**00:42:39 - Brandon Hancock:** Warp's pretty good, too. I think I also — this is not 100% accurate because I do have someone also on my account — so it's probably not that much. It's mostly me. I'm working on three projects in parallel, and I'm working like 12 hours. So it's just a matter of using AI that much in a day.

**00:43:19 - Al Cole:** <Q>Well, isn't Claude Code bearing down now on usage? I saw that come out. It's kind of like what Uber was — Uber was a cheap ride until the VC said, it's time to start paying guys.</Q>

**00:44:00 - Jake Maymar:** <A>You have to do the $200 plan. To use Claude Code, you have to basically pay $200 a month. They basically — and it's unlimited at that point — but the reason why they're tamping down is because Reuven released Swarms, and Swarms will spin up 100,000 units and burn through stuff. And of course, it's only $200.</A>

**00:44:49 - Mitch:** ▶ Using Cursor to make the documents — so like the task document, the initial message — then I just send that to Warp. So instead of using Cursor to do it, you just use the credits from Warp, and they're way more lenient on it. So you can have Cursor do all the planning, because Warp doesn't have the rules and all that other stuff. So you just ask it, like, hey, what are the rules that are needed? Create the initial message and the task document, and you can save probably like $100.

**00:49:50 - Al Cole:** I did my spec design with Claude Desktop [tool:Claude Desktop], and that got me a good ways along, and then brought that into Cursor. And I seem to be under the radar in the burn rate compared to you guys.

**00:50:23 - Jake Maymar:** But yeah, with Warp, you can have multiple chat threads at once, so I had like six going on.

---

<!--SEGMENT
topic: Sequential Thinking MCP and Context7 MCP Server
speakers: Jake Maymar, Brandon Hancock
keywords: sequential thinking MCP, MCP server, Context7, time MCP, model context protocol, GPT-4o mini, o3, reasoning, Cursor, Kiro, token cost, web search
summary: Jake Maymar recommends the Sequential Thinking MCP server, which breaks complex tasks into smaller subtasks recursively, effectively boosting the reasoning capability of cheaper models like GPT-4o mini to near o3 quality. Brandon shares his current MCP setup in Cursor: Context7 for documentation retrieval and a time server to prevent date-related errors in web searches and task logging. Both tools are highlighted as high-leverage, low-cost additions to any AI coding workflow.
-->

**00:59:29 - Brandon Hancock:** Excellent questions. Jake, has anyone used OpenAI Agents [tool:OpenAI Agents] yet? Do you want to hop on, share a little bit more what you're thinking?

**01:08:27 - Jake Maymar:** Super quick — MCPs. If you're not using sequential thinking [tool:Sequential Thinking MCP], it's freaking awesome. ▶ You can take a GPT-4o mini model and make it o3 capable. Seriously.

**01:08:53 - Jake Maymar:** Yeah, it's really awesome. Because you know me and the cheapest model possible. But yeah, sequential thinking — freaking awesome. The basic idea is you ask it a really complex task, and it sits there and it breaks that complex task into smaller tasks. And then if it's still complex, it breaks it again. But it does a really good job. Like, to me, this is like a major thing — this with Kimi K2 — crazy.

**01:09:32 - Brandon Hancock:** <Q>How fast is it spitting out? Like, if I just go straight Cursor code using Claude, how fast is that versus using this thinking server?</Q>

**01:09:33 - Jake Maymar:** <A>It's slower. It's definitely slower. But results, right? Like, do you want to spend a couple of hours crafting a prompt, or do you just want to write a simple sentence that's complex and then it thinks about it and it will ask you questions and it will think about it and it will ask you some more questions and then it will do some searching? It's really, really powerful. It's almost agentic, but not.</A>

**01:10:10 - Jake Maymar:** ▶ It's an MCP. So it works in Cursor, it works in Kiro [tool:Kiro], anything that runs an MCP. The only thing is be careful — if you're paying tokens, because it can just sit there and think for quite a while. So you want to use it on some sort of prepaid situation, not a token situation.

**01:10:36 - Brandon Hancock:** The main two MCP servers I have set up right now in Cursor: Context7 [tool:Context7] and literally just a time one. I cannot tell you how many issues I've run into with just regular time issues. ▶ I'm like, use the time tool to get the current time. And that helps with everything — when doing searches on stuff to make sure it's not finding something from three years ago. It's also making sure whenever it's marking off a task with the date, it's like, oh, I knocked it off on July 29th. This one command literally saved me so much heartache.

---

<!--SEGMENT
topic: OpenAI Agents Browser Automation — Live Shopping Demo
speakers: Ty Wells, Brandon Hancock, Jake Maymar, Paul Miller, AbdulShakur Abdullah
keywords: OpenAI Agents, browser automation, shopping cart, Shields.com, agentic browsing, $200 plan, Perplexity browser, fishing trip, travel planning, web agent
summary: Ty Wells shares a live example of using OpenAI Agents to autonomously browse Shields.com, research fishing gear for a Manitoba trip, and build a shopping cart — completing the task in 11 minutes before handing off for checkout. Jake describes a demo where the agent researched and presented guitar purchase options including financing. Paul shares using it for Silicon Valley event planning. The group discusses access requirements (US-only, $200 plan) and compares it to Perplexity's browser agent.
-->

**00:59:33 - Brandon Hancock:** Jake, has anyone used OpenAI Agents yet? Do you want to hop on, share a little bit more what you're thinking?

**00:59:35 - Jake Maymar:** Well, yeah, I just saw the announcement. It sounds pretty amazing. I just haven't had a chance to even check it out. So I'm curious to see. The demo that I saw is the one with the Neuron newsletter. They walked through basically — one of the guys wanted to buy a guitar, and he had looked for it, and he says, I'm looking for this specific guitar, I want it in this range, I want it in a payment plan, and I want — he had a whole bunch of specs. So he gave it to the agent, and he watched the agent essentially find the guitars that he was looking for. Found the results, created a very convincing sort of presentation for his wife to buy the guitar.

**01:01:08 - Ty Wells:** I actually used it just before this call. So I'm going fishing in northern Manitoba next Saturday, and I needed to go to Shields, which is a sports thing, to get some stuff. So I told it, I'm going fishing for walleye, northern pike. I said, hey, what's hot out there right now? It came back with a list of lures and jigs and spinners. And I said, okay, that looks good. Go to Shields.com [link:shields.com] and put those items in my cart and let me know when it's ready to check out. I literally did it. You could see it doing it. And then I took control, I went in, I put in my credit card information, and I submitted it, and stuff's going to be there Friday.

**01:02:15 - Ty Wells:** It said it took 11 minutes. ▶ What I find is you have to be specific as to where you want to go. Like, give it a direct website. Don't say find a site where you can buy lures — then it's going to search. To speed it up, I wanted it to go to Shields, so I went to Shields and filled my cart. You can watch it fill the cart, find the item, search, figure out where the tabs are, where the buttons are to click.

**01:02:56 - AbdulShakur Abdullah:** They're slowly rolling out to all the lower tiers.

**01:05:28 - Paul Miller:** Yeah, no, I tried it as well last week. I got it to come up with an alternative future date and said, look, if you're going to do an event in Silicon Valley around the state, cost it out, work out a side conference for a mini group, cover the flights from New Zealand, and get a good deal. It was pretty good on the travel thing, but then I used it for some other projects and it wasn't so good.

---

<!--SEGMENT
topic: CrewAI Enterprise Deployment Debugging
speakers: Brandon Hancock, Gopal Seshadri, Bastian Venegas
keywords: CrewAI Enterprise, HTTP 500 error, deployment, inputs endpoint, YAML config, kickoff method, flow, state, screenplay, API, Supabase
summary: Gopal Seshadri shares a screen to debug an HTTP 500 error when deploying a screenplay-writing multi-agent flow to CrewAI Enterprise. Brandon walks through the deployment logs and identifies that the inputs endpoint returns an empty array, indicating the crew is not configured to expose its required inputs. Bastian suggests a YAML configuration fix. Brandon connects Gopal with the CrewAI team for further support.
-->

**00:53:43 - Brandon Hancock:** Gopal said, I'm having trouble deploying my flow into CrewAI Enterprise [tool:CrewAI Enterprise], but when I try kicking it off, I'm getting an HTTP 500 internal server error. When I try to retrieve the inputs for the flow, I'm getting an empty array. Gopal, would you mind doing a quick screen share?

**00:54:20 - Brandon Hancock:** What I'm guessing is something is failing silently during the deployment. The usual culprits are: you have the project folder structure set up not how they expect it, or you're trying to do some sort of interpolation where you're expecting a key but the key's not provided. That's like 80% of the time, it's usually those two errors.

**00:56:34 - Brandon Hancock:** So it actually shows logs. It's paused. It's online, so it's running as we speak. What was the issue you're saying? What would happen?

**00:55:59 - Gopal Seshadri:** So when I come here to give kickoff, and then I say input — I'm actually having a series of inputs, like five, six inputs — which I'm passing as a dictionary to the kickoff method within the flow, and then the kickoff method is invoked within the main. So everything is boilerplate. I didn't code anything.

**00:56:34 - Brandon Hancock:** So you said it says input forward slash inputs and request — send request? So this is what it was returning — empty. <A>What that's telling me is normally what should happen is it should actually return a list of like, you need to provide first name, you need to provide this. So that tells me the crew is not configured properly.</A>

**00:58:00 - Brandon Hancock:** There are hard-coded inputs, and I cannot remember off the top of my head how you tell CrewAI, I need these inputs. Out of curiosity, anyone remember?

**00:59:07 - Gopal Seshadri:** I tried to read through the documentation, but I didn't find anywhere how I can send an input from my external API to the crew.

**00:59:15 - Brandon Hancock:** Would you mind sending me a DM with your email and I'll just connect you with someone on the team and they can help?

**01:07:53 - Brandon Hancock:** Gopal, Bastian had a few extra suggestions for you on the YAML setup. Yeah, the YAML config file — that's the secret sauce.

---

<!--SEGMENT
topic: Ty Wells' Agent Hub Project Demo
speakers: Ty Wells, Brandon Hancock, Jake Maymar
keywords: Agent Hub, Lovable, Supabase, webhook, multi-agent, orchestrator, MCP server, router agent, A2A, agent-to-agent, mobile app, security, alpha testing
summary: Ty Wells demos his Agent Hub application built in Lovable — a platform that connects multiple AI agents via webhooks into a unified chat interface with an orchestrator routing messages. The system supports group chats with multiple agents, custom commands, and MCP server integration. Brandon and Ty discuss the architecture: a central router agent delegating to specialized agents, and the natural evolution toward A2A (Agent-to-Agent) protocol for fully autonomous inter-agent communication.
-->

**01:12:24 - Brandon Hancock:** All right, Ty, you're up first, man.

**01:12:37 - Ty Wells:** Okay. This is the Agent Hub. So basically what it is — your ability to connect all of your workflows, all of your agents, and be able to chat with them, tie them all together. So you'd set up your agent, it's got a sort of walkthrough here of how you set up your agent. A little description. And you set up your webhook — basically it's a webhook — your credentials for that agent and so forth. And then you can take those agents and you can include them in the chat. So you can have multiple agents in that chat, and those agents do whatever you set them up to do.

**01:13:48 - Ty Wells:** So like here, I've got a chat called Du Bois, I've got a couple of agents in here — Reddit stuff, a code helper, and whatever — and then I could communicate back and forth with that agent. For any of those agents, I've got like an orchestrator, basically, that connects all of those agents. So these are all agents that help for different things — media advisor prompt, you know — so I build whatever I need, and then I tie them together. And then I'm just introducing some MCP servers that we can pull in.

**01:14:33 - Brandon Hancock:** So a few questions. I see we're in Lovable [tool:Lovable]. Is it working for you? Issues?

**01:14:41 - Ty Wells:** It's gotten a lot better, a lot quicker, and I don't have to touch the code as much. I haven't actually had to bring this out of Lovable, which is great.

**01:15:42 - Ty Wells:** Supabase [tool:Supabase], yeah, for storage, for storage buckets, and for the relational database. And for some functions, some functionality.

**01:16:51 - Brandon Hancock:** <Q>And out of curiosity, for agent orchestration — are you just like, do you have a central router agent that's taking it in and then distributing it?</Q>

**01:17:04 - Ty Wells:** <A>We've got a central router that's taking it, and that's what I'm tweaking. I'm fine-tuning that. You know, and you can call an agent directly, even if it's in a group chat. Or you can write custom commands and add it to your group chat.</A>

**01:17:48 - Brandon Hancock:** ▶ I think what's going to happen — if you just keep pushing that to its natural end state, each agent eventually will be running on its own, and you'll end up using A2A [tool:A2A Protocol] to connect everything. Because each agent just needs to be running and be able to take in a history of messages, answer it, and then return the result.

**01:18:32 - Brandon Hancock:** If you end up doing more A2A stuff too, please let me know what you think, just because they're constantly adding new stuff. It's a little complicated right now, but it is very powerful.

---

<!--SEGMENT
topic: LangGraph vs ADK vs CrewAI Framework Comparison
speakers: Brandon Hancock, Marc Juretus, Patrick Chouinard, Bastian Venegas
keywords: LangGraph, LangChain, ADK, CrewAI, structured outputs, Pydantic, multi-agent, production stability, tools API, streaming, state management, agentic framework, fantasy football
summary: Marc Juretus discusses frustrations with prompt formatting for his fantasy football LangChain agent and asks whether to continue with LangGraph or wait for ADK to stabilize. Brandon recommends Pydantic structured outputs with validation as a fix for formatting issues. The group debates framework maturity: LangGraph is considered most production-ready, ADK has the best developer experience but still has bugs in complex streaming/state scenarios, and CrewAI's task-based approach suits simpler sequential pipelines. Patrick introduces a Rosetta Stone concept for translating agent artifacts across frameworks.
-->

**01:19:03 - Brandon Hancock:** Marc, you're up next, man. What cool things are we working on this week?

**01:20:02 - Marc Juretus:** I was messing around with prompts and it can sometimes be rage-inducing. Long story short, my little fantasy thing where I'm returning numbers — players by position — I had the hardest time getting it to put a number before, like prefacing it with one, and then returning in the format I want where I want an abbreviated team. I was like, man, this is annoying. I've tried a bunch of different things. It was two hours deep on that.

**01:20:37 - Brandon Hancock:** <Q>So you're using LangGraph [tool:LangGraph], correct, for that?</Q>

**01:20:44 - Marc Juretus:** <A>No, I'm using just basic LangChain [tool:LangChain]. I'm not really doing a flow.</A>

**01:20:51 - Brandon Hancock:** ▶ The main thing I was going to bring up is structured outputs. You could do something like this — say you had a special number, like it had to be in a specific format. You could either break it up into separate keys — so like, if this was the position, this is the person's name, and this is like the odds — one way is just to break that up into separate fields so you're not overcomplicating that value. Option two is keep it how it is toward a more complicated output. And then I believe with Pydantic [tool:Pydantic], you could add in validation to ensure that it follows a certain regex format or something, and it will keep doing it until it gets it right.

**01:22:35 - Marc Juretus:** So right now I'm starting to look at MCP containers in Docker [tool:Docker]. So I'm trying to consume the YouTube transcript one just for now, just for proof of concept. And the other thing I want to tackle — I'm generating a lot of MD files. Is it best to use like a Notion or a Confluence for that?

**01:23:08 - Patrick Chouinard:** <A>Confluence is more of a corporate solution than an individual solution. So either Notion or Obsidian are perfect for individual users.</A>

**01:26:22 - Marc Juretus:** So I saw you kind of mentioned it last week about ADK [tool:ADK], and it seems like they make these cool things and they break something. Would a better valuation of my time be to get a bunch of products out just so I get used to using LangGraph, LangChain? Because it's completely stable, and then maybe revisit ADK in three to six months where maybe their framework's a little bit more stable.

**01:26:36 - Brandon Hancock:** <A>I'm so torn on it myself. I love how easy it is to set up a multi-agent workflow. However — big asterisk — I keep finding bugs. Like, last night at midnight, I was like, guys, in streaming mode versus not streaming mode, this breaks. They're making a ton of progress. So I'm still very bullish on the product. But yes, I'm pushing it to its absolute limits. For just general agent one does something and passes it to agent two — they've nailed that. That workflow, they've absolutely nailed. In my case, it's complex stuff — that's where it's not stable.</A>

**01:29:17 - Brandon Hancock:** ▶ Truthful answer: I wrote off LangGraph for a very long time because it was too complex in V2. But now, after watching a lot of their Interrupt 2025 and stuff, I'm back to — I think LangGraph's awesome. I think for production, LangGraph is the best one right now. I think for user experience, ADK is the best. So I'm hoping ADK, literally two months, it is going to be the go-to one. But they're getting there. They're not there yet.

---

<!--SEGMENT
topic: Patrick's GitHub Copilot Training Generation Workflow
speakers: Patrick Chouinard, Brandon Hancock, Bastian Venegas
keywords: GitHub Copilot, MCP, Perplexity, GitHub MCP, Fetch tool, release notes, training generation, CrewAI, ADK, Rosetta Stone, agentic framework translation, VS Code, template technique
summary: Patrick Chouinard demonstrates a prompt-only workflow built entirely in GitHub Copilot agent mode that automatically retrieves VS Code release notes via GitHub MCP, extracts features, and generates structured training materials and resource kits using Brandon's template technique — all without a single line of code. He plans to migrate to CrewAI or ADK once prompts are perfected. He also introduces a Rosetta Stone concept: a translation matrix mapping equivalent concepts (sub-agent, task, instruction, prompt) across different agentic frameworks.
-->

**01:43:36 - Patrick Chouinard:** By the way, just a little something. I posted a link. You can try that for your cost for Claude Code usage. It's a CLI tool that will give you a full panel of everything you've used — which model, token, everything. [link:Claude Code cost CLI tool shared in chat]

**01:44:20 - Patrick Chouinard:** I've remembered that I said that I wanted to build something to create training automatically out of release notes. So this is what I came up with. It's still rough. I still need to tweak the prompt to get some good quality output, but it's doing the job right now, and this whole workflow is strictly within GitHub Copilot [tool:GitHub Copilot]. I'm just using Saved Prompt in GitHub Copilot with the proper tool usage, leveraging a couple of MCP servers like Perplexity [tool:Perplexity MCP], GitHub [tool:GitHub MCP], and the Fetch Tool.

**01:45:15 - Patrick Chouinard:** The first one actually goes and retrieves the release note for VS Code. So it basically gets the latest version number and uses the MCP server for GitHub to download the markdown file. Then the next one extracts the features. So it analyzes the entire release note, extracts the list of features. Then I use the list of features to generate training and generate resource kit. Resource kits are basically all of the exercises and the demos and all of the files that are going to be used during those.

**01:46:11 - Patrick Chouinard:** Once I finalize the prompt and they all work well, that's when I'm going to try to move it probably to something like CrewAI [tool:CrewAI]. I just want to get the prompt to do what I want perfectly without having to deal with all of the plumbing, and I'll do the plumbing last.

**01:48:03 - Patrick Chouinard:** ▶ Yeah, I've already created two full — and obviously I'm leveraging your template technique, so every feature is based on a template that needs to be filled, same thing for the resource kit. The training I've already created for the last two versions of GitHub Copilot. Structurally, it's completely sound and complete. It's just a matter of tweaking the prompt. And all of that without a single line of code — only prompt over prompt over prompt.

**01:49:32 - Patrick Chouinard:** Actually, you're going to like that. That's something else I'm working on on the side. I've started to map out all the agentic artifacts. And I based myself on Claude's Code sub-agent framework as the basis. And then I try to create a matrix of what each component maps to in all the other agentic frameworks — to see if I can get to a point where I could translate the artifact from one framework to another. Can I build a Rosetta Stone to transfer from Claude Code, Gemini CLI, GitHub Copilot, CrewAI, LangGraph?

**01:51:21 - Patrick Chouinard:** I realized that what someone calls a sub-agent, another one calls a chat mode, another one calls an agent definition. And whatever one calls a prompt, another one calls an instruction, and the other one calls a task. So there's kind of equivalency. So if I can move between them, just stating in a transfer matrix what changed between the different agentic frameworks?

**01:52:06 - Bastian Venegas:** It's a product from AgentOps [tool:AgentOps]. They build this translation layer, and they use it to scaffold agentic workflows really quickly for their clients. I mainly wanted to just highlight how difficult it is. But when I dove into that repo, I got a better understanding of what are those equivalent layers that Patrick was mentioning.

---

<!--SEGMENT
topic: PipeDrive CRM Automation with N8N and MongoDB
speakers: Paul Miller, Brandon Hancock
keywords: PipeDrive, N8N, MongoDB, CRM, automation, Python, Cursor, Claude Code, $200 plan, Upwork, DevOps, onboarding workflow, data pipeline
summary: Paul Miller describes his effort to augment PipeDrive CRM with N8N workflows — copying records to MongoDB for parallel AI analysis of sales opportunities. He finds N8N's MongoDB mapping complex and sometimes prefers writing Python scripts in Cursor. He has canceled his OpenAI $200 plan in favor of Claude Code's $200 plan. Brandon recommends hiring N8N specialists on Upwork at $30–40/hour to build out workflow infrastructure, and suggests having two contractors review each other's work for CRM-critical automations.
-->

**01:53:14 - Paul Miller:** Well, other than playing around with some shiny new things — so I gave the Opal thing a go, and that was interesting. You guys might remember last week I had the — where I was wanting to make my CRM more useful. I didn't really want to change our CRM, because we used PipeDrive [tool:PipeDrive], and we kind of got all the deals in there. I didn't want to go and migrate again from that. But what I've been able to do is work with PipeDrive, and move things in and out of that with N8N, and it's really quick.

**01:54:18 - Paul Miller:** I'm taking a copy. So my master truth sits in the CRM. And then I kind of wanted to have some parallel exercises of — analyze all the customers I've got sitting in the CRM, see what opportunities there are to research what I should be pitching to them next, how I can get them through another gate in the sales process. And I got it to copy records into Mongo [tool:MongoDB] and it's just a really simple thing. But I've spent two days trying to map some of the Mongo things. It's just faster for me just to jump into Cursor and write the code than some of the exercises.

**01:55:30 - Paul Miller:** I went and made the jump for the $200 plan. So I've canceled my OpenAI $200 plan because I thought the Agents thing was pretty mediocre — certainly not worth the $200. But I'm going to go full speed into the $200 Claude Code plan.

**01:56:19 - Brandon Hancock:** ▶ Just quick update — previous startups I worked at, a lot of times they'll just hire to build out those N8N workflows. You can find some really talented guys, $30 to $40 an hour, give them a week, and they literally will have the entire infrastructure of your company set up and running in N8N. I would 100% look at that. If you're ever doing an Upwork [tool:Upwork] job post, I'm happy to share exactly how I do it.

---

<!--SEGMENT
topic: Mitch's Full-Stack AI Content App with N8N Integration
speakers: Mitch, Brandon Hancock
keywords: Lovable, Supabase, N8N, LLM pipeline, Google Veo, content generation, job status, webhook, project management, full-stack, vibe coding, Warp, Kiro, theme page
summary: Mitch demos a multi-tenant content generation app built in Lovable with Supabase — supporting organizations, projects, content types, and LLM configuration per project. He asks how to integrate N8N for the actual LLM calls without running them in the app. Brandon outlines an architecture: the front-end handles CRUD only, N8N handles long-running LLM pipelines triggered by status changes, and a job status table tracks attempts, errors, and completion for front-end polling. Mitch also shares a tip about using a theme reference page in Lovable for consistent UI.
-->

**01:34:36 - Brandon Hancock:** I think next up, Mitch, what's going on, buddy?

**01:35:40 - Mitch:** Oh, yeah — it's like different organizations that have different projects. Different projects have different content types, different pages. And then basically you can add a new configuration, change the model, all the temperature and such. And then for the master prompts — it will then use the models from the LLM base that you'll select in the edit and then you'll be able to add the contents.

**01:36:10 - Mitch:** Basically the user will come in here — here's this idea, here's the expected number of clips, and this is the actual description that we give to kind of streamline the LLM calls. And then we'll have the final clips and they can view it all here and download it and kind of copy and paste, because Google Veo [tool:Google Veo] — the only real way to profitably use it is just to copy and paste it into their flow.

**01:37:07 - Mitch:** <Q>I don't really want the actual LLM calls to be on the app. I was hoping to just do it on N8N. And then I guess the main thing would be including the project ID. So basically when someone creates an idea refinement, it's going to be underneath a project, and then that project ID would then — what's the best way to use N8N in this instance with just maybe doing a webhook?</Q>

**01:37:47 - Brandon Hancock:** <A>Okay, so if I was building this, and I was like, man, I want N8N to do my long-running workflows — if it takes more than five minutes, you're kind of in no-man's land. So if I was in your shoes, what I would be doing is the front-end website is nothing more than CRUD. So what I mean by that is I am creating organizations, I'm creating templates, I'm storing prompts, and I'm storing it all in a very nice relational structure. Once I grab all prompts, I'll be able to see what ideas they connect to. So with one project ID, I should be able to download everything I need.</A>

**01:38:50 - Brandon Hancock:** ▶ And that's going to be super important, because eventually, when you hop over to your N8N workflow, you're going to go — cool, the user said project one, change from status draft to ready. Now that it's ready, now I'm going to go download everything, get the prompts, everything that I need, and then start working through it. However you're going to do the LLM calls. And then all it's going to do is — because you're using Supabase — it's going to just make queries to Supabase. ▶ You need probably two or three extra fields on a project — or make another table called project job status. All it's going to have is the number of attempts, error messages, and status. So complete, fail. And that's how I would tackle it. So you're just going to pull everything down, go to the N8N pipeline. If it fails, update the job status. If it succeeds, update it to succeed. And then on the front end, you can just be like, cool, I'm on project one, two, three — I'm going to continually poll to see what is the status of this job.

**01:40:31 - Mitch:** Oh, and I forgot to share one thing with you. I should add this to that Notion doc you gave me — which is a Lovable theme. But yeah, it's really helpful to have a theme page when you're building this out. You just reference it and say, hey, I want it to be this theme. ▶ So just one thing to have when building their own thing out is to probably have that as part of the setup process.

---

<!--SEGMENT
topic: Asako's AWS Developer Advocate Content Strategy
speakers: asako, Brandon Hancock
keywords: AWS, Strands Agents, A2A, developer advocate, content strategy, YouTube, LinkedIn, blog, Kiro, early adopter, personal brand, Bedrock, voice agents, video AI
summary: Asako shares her job search for a developer advocate role and her strategy of going all-in on AWS content — specifically Strands Agents and A2A implementation — to build a differentiated portfolio. Brandon endorses the single-platform focus strategy and outlines a monthly content roadmap: agents, then voice, then video on AWS. He strongly advocates for YouTube over blog posts for discoverability, and frames early adoption of Strands as a stock-buying opportunity — painful now but high-reward when the framework matures.
-->

**02:02:24 - Brandon Hancock:** Osaka, you're up next, man. What cool things have you been up to recently?

**02:02:31 - asako:** I've been actually looking for a new role as a developer advocate. Honestly, the market has been really tough, but one feedback that I got that I was missing was the longer form content, like tutorial or thought leadership type of blog content. So I decided to start posting those kinds of content. And I decided to go all in on AWS because you, Brandon, have a lot of excellent content around Google.

**02:03:09 - Brandon Hancock:** Oh, God, we're competition now.

**02:03:16 - Brandon Hancock:** ▶ Picking one platform and then just going — you are going to be able to go so much deeper. Instead of competing against every AI product ever — no, this is my stack. It's an enterprise stack. Everyone's using it. You're going to open yourselves up for so many cool opportunities. So right off the bat, beautiful decision.

**02:03:49 - asako:** So far I launched how to build multi-agents using Strands Agents [tool:Strands Agents]. And then also how to implement A2A using Strands Agents. And then this week I still don't have an idea. I wanted to test out Kiro, but I'm still on a wait list.

**02:04:26 - Brandon Hancock:** ▶ I think the angle first of like getting your foot in the door on Strands is awesome because I think there's not enough content around it. I mean, I know they launched it a month ago, maybe two at this point. I haven't got to hear much about it. So I think you diving deep into that is going to be huge. Obviously, it's a win-win because you need exposure, they need exposure. So I think it'll hopefully lead, after like a month of work, to some new opportunities.

**02:06:00 - Brandon Hancock:** ▶ I mean, hey, it's a cool thing about becoming an early adopter — by the time it does hit, your content is going to be the go-to source. It's like buying a stock. By being an early adopter, yes, you're going to have the most turmoil going through it. But eventually, by being that early adopter, it's going to open doors.

**02:06:44 - Brandon Hancock:** ▶ What I would do in your spot is: I'm going to become the world's best AWS AI developer. That is my North Star. And then I tackle it in chunks. This month, I'm going all in on agents. Next month, I'm going to go all in on voice. The following month, I'm going to go all in on video with AWS. You just pick a category in that bucket and become the best expert on it, and then just publish content.

**02:08:52 - Brandon Hancock:** ▶ I cannot express the power of YouTube because a quick 20-minute video — you've already done the hard work. You built the project, you got it deployed. And then literally just turning it into Excalidraw drawings and just talking over some code. YouTube just has an insane growth mechanism that is hard to do on your own blog. LinkedIn is good — it's just LinkedIn is really powerful for snippets of value. You're doing longer-form projects, which equals longer-form videos. So I would 100% say YouTube is where I see a ton of growth for you.

---

<!--SEGMENT
topic: AI Industry Positioning, Micro-SaaS Opportunity, and Superintelligence
speakers: Ty Wells, Brandon Hancock, Jake Maymar, Tom Welsh, Patrick Chouinard, Marc Juretus
keywords: micro-SaaS, superintelligence, post-labor economics, AI 2027, David Shapiro, capital accumulation, personal brand, chief AI officer, abundance mindset, community, vibe coding, production-grade code, AI window
summary: Ty Wells prompts a group reflection on where this community sits relative to the broader AI adoption curve. The discussion covers: the gap between AI practitioners and newly-appointed chief AI officers who don't use the tools; the two-to-three year window to capitalize before AI commoditizes development; the micro-SaaS explosion of small targeted applications; Patrick's point that vibe-coded apps create a new job category of production-grade refactoring; Jake's abundance mindset and community-as-competitive-advantage thesis; and Brandon's reference to the AI 2027 paper and David Shapiro's post-labor economics framework.
-->

**02:09:49 - Ty Wells:** <Q>I've posed this question over this week to other groups that I'm in — like the level we're at versus the rest of everybody else, what are they doing? Are they like not doing anything? It just feels like we're so far ahead and I'm just trying to gauge where are we really at. Because obviously all the big players are doing stuff, people are building stuff, but they're not in these communities. So I'm trying to figure out — are we in the right spot? Are we heading in the right direction in terms of — are we way ahead?</Q>

**02:11:22 - Jake Maymar:** <A>Well, I was just going to mention — all the major banks are now hiring a chief AI officer. That's a pretty big indicator, a pretty big signal. So we're at an inflection point. What I feel is that's really positive, because I remember not too long ago, beginning of this year, people were like, GenAI, who's using that, you know, hallucinations. I always look for signals in the market. And I know a lot of people that are coming to me and going, hey, you've been messing with AI, what can you do with it?</A>

**02:12:46 - Tom Welsh:** <A>Yeah, I think we are — I wouldn't say we're bleeding edge, we're definitely cutting edge. We're trying the technologies, we're using them on a daily basis. I think the knowledge in this group is phenomenal. From the interviews with BT and other discussions I've had — I've got friends in finance in the city who are bringing on chief AI officers, but these people that are coming in as chief AI officers are old-school CTOs and C-Risk people. They're not actually AI people.</A>

**02:13:33 - Jake Maymar:** That's a really, really great point. They're not using the technology. A lot of these chief AI officers — they were chief science officers, CTOs, all these different CXOs. They're not using the technology. And if they are, great. But I still think we have an advantage because they're going to need us.

**02:14:14 - Brandon Hancock:** ▶ I mean, in my head, it's just — apply what's happening to code right now to every industry. The part that's wild about most other industries is the amount of person-to-person communication that's just about a meeting to then set up another thing. There's just so much genuine waste. So I think they're very far behind. Any document, any artifact that is produced by an organization — they're wild if they're not using an agent to produce that right now.

**02:15:56 - Brandon Hancock:** I was helping out a fire chief to basically help them do stuff. Fire departments — government — one of the last adopters of anything. They have zero incentive to improve. Except — hey, does this actually make my guys' life easier? Literally just been able to work with him to update their current processes to use AI. And they're like, oh my God, this used to take 20 minutes per report. It now takes two. So it's a 10x multiplier.

**02:17:00 - Brandon Hancock:** ▶ I genuinely think there's like a two-to-three year window to really dominate before AI just gets so good that we're not even needed. I actually just dropped a video in the chat — it's called AI 2027. [link:AI 2027 YouTube video shared in chat] There was a paper, but there's a cool video where the guy kind of narrates through it. I definitely recommend checking that out.

**02:21:00 - Brandon Hancock:** ▶ I think we are on the verge of like a micro-SaaS explosion of individual small solutions to where you build it, the app generates between 10 to 30K a month. And then cool, you do another one, and then you do another. Instead of having huge monoliths of big applications, it's going to be a bunch more smaller ones.

**02:22:00 - Patrick Chouinard:** AI is just another layer of abstraction. I'm not seeing this completely stealing jobs. It's going to create a whole lot of jobs, actually, because when you make something more simple — those tools like Lovable, like Bolt, like all of those — they enable a whole lot of people who don't know what they're doing to create apps that they think are production-ready, but they have no concept of what's production-ready. ▶ So it creates a whole lot of jobs for guys like me to come back behind them and actually correct all of the slop that they created.

**02:23:06 - Brandon Hancock:** ▶ I can't remember if someone else told me this, but basically a new job title for senior developers is literally just going to be like turning Lovable apps into actual production-grade. Everyone else is building these MVPs, and they're getting so excited. And then they're like, okay, cool — now I need a real engineer to actually come in and make this an actual application. That is a full-blown job title — AI slop to production-ready code. And you could easily turn that into a LinkedIn tagline and easily start securing some deals that are pretty sizable — 30, 40, 50, 60K deals.

**02:30:33 - Brandon Hancock:** Quick, the final channel I just wanted to drop — David Shapiro [tool:David Shapiro], because he talks about this a ton. He writes books and it's called post-labor economics. The general consensus is: what happens when labor goes away? Because up until now, your ability to go contribute to society to generate value — that is how you gain capital. But what happens when labor, that pillar, goes away? Meaning you can't contribute faster than AI. ▶ That's why I'm like — okay, well, if I'm about to lose my labor pillar, I need to gain as much capital as possible in this three-year period before you lose it.

**02:36:44 - Jake Maymar:** ▶ I've consciously started doing this — I've surrounded myself with communities that have a mindset around abundance. So you want to share. And I'm really inspired by Brandon. My wife was listening to this call and she's like, that's a lot of really kind people. The key piece is you surround yourself with people that are willing to share. And that way you don't have to keep all the knowledge and you don't have to keep up to date. Because Brandon's sharing, Bastian's sharing — everyone shares on this call and all the boats actually rise together.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were NOT found in the SPEAKER_ALIASES context block (which was not provided in this session):

- **asako** — appears as `asako` in the raw transcript; canonical form unknown
- **Sam** — appears briefly at 00:08:59 and 00:46:55–00:48:51; no alias map provided to confirm
- **Al Cole** — appears multiple times; cannot confirm canonical form without alias map
- **Juan Torres** — appears multiple times; cannot confirm canonical form without alias map
- **Marc Juretus** — appears multiple times; cannot confirm canonical form without alias map
- **Paul Miller** — appears multiple times; cannot confirm canonical form without alias map
- **Patrick Chouinard** — appears multiple times; cannot confirm canonical form without alias map
- **Mitch** — appears multiple times with no surname; cannot confirm canonical form
- **Gopal Seshadri** — appears multiple times; cannot confirm canonical form without alias map
- **Jake Maymar** — appears multiple times; cannot confirm canonical form without alias map
- **Tom Welsh** — appears multiple times; cannot confirm canonical form without alias map
- **Ty Wells** — appears multiple times; cannot confirm canonical form without alias map
- **Bastian Venegas** — appears multiple times; raw transcript uses "Vashem" as a spoken alias; cannot confirm canonical form without alias map
- **Brandon Hancock** — appears as primary host throughout; cannot confirm canonical form without alias map
- **AbdulShakur Abdullah** — appears multiple times; cannot confirm canonical form without alias map

*Note: The `SPEAKER_ALIASES` context block resolved to an empty/null value (`{{ $('HTTP Request: Get Speaker Aliases').item.json.data }}`), so all speaker names have been passed through unchanged from the raw transcript and all are listed here as unresolved.*