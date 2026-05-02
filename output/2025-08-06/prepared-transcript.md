=== SESSION ===
date: Not explicitly stated (references to current-week model releases suggest mid-2025)
duration_estimate: ~2 hours
main_themes: New model releases (OpenAI open-source, Claude Opus 4.1, GLM 4.5), Claude Code / Cursor usage limits and workflow strategies, RAG tooling (LlamaIndex, Kuzu, GraphRAG), N8N prototyping and client delivery, AI bubble economics, local model viability, front-end tooling (Next.js, Lovable), agentic frameworks (Google ADK, Opal), eval strategies

---

<!--SEGMENT
topic: Session Opening and New Model Reactions
speakers: Paul Miller, Patrick Chouinard, Andrew Nanton, Bastian Venegas, Marc Juretus
keywords: OpenAI open-source model, Claude Opus 4.1, LM Studio, VRAM, GTX 1080 Ti, token speed, context window, Perplexity MCP, tool calls, benchmarks
summary: The session opens with informal greetings before participants share first impressions of the newly released OpenAI open-source model and Claude Opus 4.1. Participants report running the 20B model locally on older hardware with surprisingly good performance, and note that Claude Opus 4.1 shows incremental improvements across most evals. This segment establishes the week's dominant theme of new model releases.
-->

00:00:59 - Paul Miller
Good morning, guys. Afternoon. Evening.

00:01:38 - Bastian Venegas
Hey, how are you doing, Paul?

00:01:40 - Paul Miller
Good, good. I'm the host today.

00:02:32 - Bastian Venegas
Hey, Mark.

00:02:35 - Marc Juretus
Hey, Bastian, Paul, Andrew. How are you?

00:04:32 - Patrick Chouinard
<Q>Anyone had a chance to try the new OpenAI open-source model today?</Q>

00:04:38 - Paul Miller
<A>I've downloaded it. I haven't been able to do benchmarks or anything like that. It looks pretty good, actually.</A>

00:04:49 - Andrew Nanton
<A>I fired it up in LM Studio [tool:LM Studio] and was pretty impressed, just dropping in a few really random questions. For something that runs in such a small amount of memory, I was awfully impressed.</A>

00:05:07 - Patrick Chouinard
<A>Yeah, me too. I'm running on decent hardware, but certainly not cutting edge. I ran it on two GTX 1080 Ti, so not bad in terms of VRAM, but pretty old in terms of CUDA cores. It still ran at 33 tokens per second for a 20B model, fully in VRAM.</A>

00:05:38 - Patrick Chouinard
And decent context window, too.

00:05:41 - Paul Miller
128,000 tokens, which seems pretty good.

00:05:46 - Patrick Chouinard
Sadly, I do not have enough VRAM for 128,000 tokens, but still. Tool calls ran pretty well. I tried it with the Perplexity MCP server [tool:Perplexity MCP]. No issues. So yeah, pretty impressed right now.

00:08:40 - Andrew Nanton
Sure, so I'm seeing this first question here. Has anyone tested Opus 4.1 yet? I tested it a little bit in Claude Code [tool:Claude Code], and then with some other more freeform stuff. It seems like an incremental improvement. At 4.1 it seems pretty true to its word in that it seems like maybe a little bit better, and that's what I'm seeing in the model cards. It looked like there was a step backward in one of the evals — I think it was like booking airline tickets or something — went from like 56.9 to 56, but it looked like a couple percentage improvements across almost every different kind of task, which lines up to what I'm seeing. But obviously it's only been a couple of days, and that's really anecdotal.

---

<!--SEGMENT
topic: Opal Agent Builder and Prompt Engineering
speakers: Paul Miller, Bastian Venegas, AbdulShakur Abdullah
keywords: Opal, Google Gemini, TLDraw, prompt engineering, agent workflows, Ideal Customer Profile, one-shot prompting, iterative prompting, HTML output, flow editing
summary: The group discusses Google's Opal agent-building tool, with participants noting it excels at initial one-shot flow generation but struggles with iterative editing. AbdulShakur shares a prompt-refinement workflow he uses to extract ambiguity through back-and-forth dialogue before finalising prompts. TLDraw's similar Gemini-powered diagramming feature is also mentioned.
-->

00:09:38 - Paul Miller
<Q>Has anyone got any good use cases out of Opal yet? That's the Google model that you can create agents with prompting. Bastian, have you had a play?</Q>

00:10:01 - Bastian Venegas
<A>No, I haven't used it yet. I played with a similar tool by a platform used to make drawings and schemes. It's similar to Excalidraw but it's called TLDraw [tool:TLDraw] — T-L-D-R-A-W — and they have a new free thing you can try. Google gave them a bunch of credits for Gemini [tool:Gemini], and they do a thing very similar to what Opal is trying to do, where you have these diagrams.</A>

00:10:59 - AbdulShakur Abdullah
I was just asking because I wasn't able to edit very well after the initial kind of one-shot prompt where it makes the big flow. Going in and trying to edit part of the flow to add new logic just didn't work very well for me. So I wanted to see if anyone had any tips on fixing it.

00:11:23 - Paul Miller
<A>Yeah, I just found it really good for creating really good prompts. I don't know what's in the back end of the model, but in terms of the engine, that's been pretty good.</A>

00:11:36 - AbdulShakur Abdullah
I have been using a new prompt to make prompts, which has been pretty strong for me today. I'll drop it in the chat and share that.

00:50:53 - AbdulShakur Abdullah
Yeah, so basically the prompt takes my intention and keeps pulling it out in a back-and-forth method until I have a whole workflow of what my end goal is. The idea is that it takes my rough ideas, I have a conversation back and forth, and once we both agree, it delivers what I have. Sometimes I just put in my original prompt idea, or sometimes I just start it off and tell it to wait, and then I throw in my original prompt idea. I find that just going back and forth and really pulling out all the ambiguous parts has really upped my prompting level.

▶ AbdulShakur Abdullah: Using iterative back-and-forth prompting to surface ambiguity before finalising a prompt significantly improves output quality.

00:49:31 - AbdulShakur Abdullah
One of the changes I wanted to do was — it decided to generate all the output in HTML reports, but I wanted it to give me a PDF or send it into Google Docs so I could edit it, so I didn't have to keep regenerating. But when I tried to add that feature, it just kept breaking. I gave up on that. I was like, okay, I guess it can only one-shot.

---

<!--SEGMENT
topic: Claude Code Workflow Best Practices
speakers: Andrew Nanton, Jake Maymar, Sam, Al Cole, Paul Miller
keywords: Claude Code, planning mode, context window, implementation plan, design document, rate limiting, WSL, Docker, environment variables, token burn, clarifying questions
summary: Participants share strategies for getting reliable output from Claude Code, including staying in planning mode, maintaining design and implementation plan documents, and restarting sessions when the model goes off-track. Rate limiting and token consumption on the $20 Cursor plan are flagged as growing pain points, with the group noting the previous transparency of usage dashboards has disappeared.
-->

00:12:02 - Jake Maymar
Not yet. Claude — they're doing a lot of rate limiting if you're using Claude. I'm sure you've seen that, Andrew. If you're using Claude on Open Router [tool:Open Router], or really other platforms — I think even Cursor [tool:Cursor] — I've seen some rate limiting. But smaller platforms, there's really heavy rate limiting. I'm kind of curious if anyone else is seeing that.

00:12:49 - Jake Maymar
Andrew, are you still using Claude Code?

00:12:53 - Andrew Nanton
Yeah. I've found that to be the most reliable for me. But that also, I think, says a lot about my workflow rather than it being the best possible choice, because I'm generally also doing other stuff in the background, so having something that's pretty autonomous is really useful for me. But yeah, I am noticing the same thing that everyone else is noticing — even though it's improving, it's really hard to get it to stay on the rails. It likes to just start jumping into doing all kinds of nonsense pretty quickly.

00:13:30 - Jake Maymar
Yeah, like it wrote — I was just trying to debug something and it wrote like seven debuggers on top of each other for no reason at all.

00:14:04 - Sam
Because I'm using Windows, I have to create that Linux environment and Docker. And sometimes I feel like, in that session, if it gets on the wrong track, you might as well just throw in the towel and restart the whole thing.

00:14:21 - Jake Maymar
That makes a lot of sense. There was an update — Windows did an update to WSL [tool:WSL] and it broke Docker [tool:Docker] and a whole bunch of different things, so maybe that's it.

00:15:00 - Sam
I had a funny experience — I couldn't get the environment variables to load, and then it wrote a custom script to pull environment variables, and I was like, why don't you just use the library to do it? You know, python-dotenv, that stuff. So yeah, you do have to shepherd it a bit still.

00:15:24 - Paul Miller
<Q>With the rate limit changes in Claude Code, are people finding they're going to use up the limits if you're on a max plan or the $100 plan?</Q>

00:15:51 - Bastian Venegas
<A>Officially, they will update their limits at the end of the month — I think the 27th, maybe.</A>

00:16:23 - Jake Maymar
<A>That was the thing — it used to be really clear. You used to be able to look at the Cursor dashboard and it said you had 400 or 300 or 200 left. And now it's not clear at all. And $20 lasts for like four days, if that.</A>

00:18:10 - Andrew Nanton
▶ One rule of thumb I read is: don't tell it more than twice that it's taken a wrong turn. You just have to zero out the context window and start over.

00:18:40 - Andrew Nanton
▶ If it starts trying to do weird stuff and you're trying to get it back on track, you're way better off just shutting down the session, starting a new session. Here's what I'm doing. Here's my design document — overall what I'm doing, what are all the different parts. Then I keep another file that is the implementation plan — what are the next few steps. I have it delete out the stuff as we go and add it to a development log file.

00:19:09 - Andrew Nanton
▶ I use planning mode way more than I let it write code. I always get really good results from saying "ask me any necessary clarifying questions," because otherwise it just starts making dumb assumptions.

00:19:38 - Andrew Nanton
It's like a Shift-Tab to keep it in planning mode in Claude Code. I don't take planning mode off until I'm 100% happy with it. And even then, I say: write the plan you've created into an implementation plan file that you're going to now follow. Then I'll usually compact the context window and say, read `@implementation-plan.md`, tell me what your next three steps are, let me make sure those look reasonable, then go nuts.

00:20:44 - Andrew Nanton
▶ You'll burn through way fewer tokens by staying in plan mode. I do a lot of: here is the documentation for this feature I want you to use. Or here's the URL — use Context7 [tool:Context7] to get the documentation and tell me what's the most idiomatic way to do this. Are we duplicating any functionality that already exists in this library?

---

<!--SEGMENT
topic: Context7 and MCP Tooling Discussion
speakers: Andrew Nanton, Al Cole, Bastian Venegas, Jake Maymar
keywords: Context7, MCP, GitHub repository, documentation crawling, Convex, Redis, LLM.txt, local MCP, Convex MCP, slowdown debugging
summary: The group examines how Context7 sources its documentation (by crawling GitHub repos rather than official web docs), and whether it covers deployment as well as developer content. Bastian clarifies that Context7 requires a GitHub repo URL and builds its own documentation from that. Jake raises a slowdown issue with the Convex MCP in Claude Desktop, which Bastian attributes to a possible misconfiguration rather than a fundamental bottleneck.
-->

00:21:25 - Al Cole
<Q>A quick question on Context7. I looked at it more closely today — I was looking at Redis, and I found a lot of operations/deployment information in there versus what I was thinking would be straight developer-oriented. Is that pretty common — that Context7 will span deployment information, maybe API-related information?</Q>

00:21:55 - Andrew Nanton
<A>I mean, I don't know what other people's experience has been, but for me it seems to pretty carefully only pull official docs from existing libraries. But maybe that's just what I'm asking it to do.</A>

00:22:12 - Bastian Venegas
<A>I think what it does is it crawls the GitHub repository and then builds its own documentation. Because if you try — for example, I was searching for something in Context7, it was Convex [tool:Convex], the database. They had it like one month ago, and I wanted to see if I could use the documentation from the web, because they even have an LLM.txt, so it would make sense to use that. I fed that and the documentation page URL, and it just won't let you — it will always ask for a GitHub repo, and that's what it will use to see if it needs updating or not.</A>

00:23:04 - Jake Maymar
<Q>Bastian, on that — are you seeing any slowdown? I've been using some MCPs, and I started using the Convex MCP [tool:Convex MCP] just in Claude Desktop, and it does weird stuff where it just slows down. Are you seeing that?</Q>

00:23:23 - Bastian Venegas
<A>No, not really, and it shouldn't. If you run it locally, the MCP, instead of connecting through the internet, it shouldn't be an issue. If you're doing it locally, it shouldn't be a bottleneck — it's just routing your HTTP request.</A>

▶ Bastian Venegas: Run MCP servers locally rather than connecting through the internet to avoid latency bottlenecks.

---

<!--SEGMENT
topic: RAG Tooling — LlamaIndex, Kuzu, GraphRAG, and BAML
speakers: Andrew Nanton, Jake Maymar, Bastian Venegas
keywords: LlamaIndex, LangChain, Kuzu, GraphRAG, Pydantic AI, BAML, RAG, BM25, vector retrieval, graph database, embedded database, TypeScript, Python, Convex RAG
summary: Andrew gives an in-depth comparison of LlamaIndex versus LangChain for RAG workloads, favouring LlamaIndex for its RAG-specific depth (chunkers, parsers, retrievers, hybrid retrieval). He describes his GraphRAG work using Kuzu, an embedded graph database. BAML is flagged as a promising new tool for structured data extraction. Jake raises Pydantic AI and Convex's built-in RAG as alternatives, and Bastian notes he values Convex primarily for its fast sync rather than its RAG capabilities.
-->

00:24:18 - Andrew Nanton
I have continued to crack away at LlamaIndex [tool:LlamaIndex], which if you have RAG-related stuff to do, I think is definitely worth a look. It's large and messy, and it changes really fast, and so sometimes that can be pretty frustrating. The TypeScript implementation is significantly behind the Python implementation. But they've added some interesting stuff — they have a few interesting starter projects, like a NotebookLM sort of equivalent functionality. And they also have a RAG-as-MCP, like a pretty easy connection that I haven't really had a chance to play with very much yet. The idea is it will ingest all the documents you pointed at, and then you can use that MCP to access all of the documents you've stuffed into the RAG.

00:25:22 - Andrew Nanton
What I've been working on is GraphRAG stuff using Kuzu [tool:Kuzu], which is an embedded graph database. So you don't have to run a database server for it — it's like SQLite, just a file on disk.

00:26:21 - Jake Maymar
<Q>You said LlamaIndex instead of LangChain. You like LlamaIndex because it's more stable, or just...?</Q>

00:26:29 - Andrew Nanton
<A>When I was first getting started with LangChain [tool:LangChain], it was right at the 0.2 transition and then 0.3 was right after it. A lot of it just was not making sense to me. And there's this whole LangChain Expression Language — it's not particularly Pythonic. LlamaIndex is very RAG-specific in a way that LangChain tries to be a little bit more flexible and agnostic. LlamaIndex is pretty unapologetically a RAG tool, but it has just an amazing array of things — chunkers, parsers, retrievers. If you want to combine vector retrieval plus graph retrieval, or BM25 plus vector retrieval, it has all of the tools and pieces you need for RAG, and fairly sophisticated implementations of those.</A>

00:28:03 - Jake Maymar
<Q>What about Pydantic AI? I was using that for RAG for a little bit. It did some pretty nice things on the agentic RAG side. Have you messed around with that at all?</Q>

00:28:17 - Andrew Nanton
<A>I looked at it, but I did not get very far with it. There's actually another one that one of the guys from Kuzu keeps raving about that is fairly new — called BAML [tool:BAML]. It's like the beginning of an implementation, but it's super focused on structured data extraction. It looks really cool.</A>

00:29:04 - Jake Maymar
I'm doing a lot of stuff with Convex, and I know Bastian's doing stuff with Convex. Convex does have RAG built in, but it feels kind of vanilla. I don't know how much I can augment it.

00:29:23 - Bastian Venegas
▶ I haven't used RAG yet in Convex, but if it's vanilla, I actually like it more because I don't want a platform that's too opinionated. I just want the database to be fast and sync through tRPC — that's all I want from Convex, actually.

---

<!--SEGMENT
topic: Client Delivery, N8N Prototyping, and Eval Strategies
speakers: Jake Maymar, Al Cole, Andrew Nanton, Bastian Venegas, Neel More, Adam
keywords: N8N, proof of concept, evals, LLM-as-judge, scope creep, SOC 2, HIPAA, hallucination, rubrics, client buy-in, data privacy, self-hosting, trusted advisor
summary: A rich discussion on using N8N for rapid client prototyping and the risks of scope creep when demos look deceptively simple. The group debates eval strategies — LLM-as-judge, manual spot-checks, and rubric-based scoring — and the challenge of getting clients to pay for quality assurance. Data privacy compliance (SOC 2, HIPAA) for N8N is also addressed.
-->

00:35:00 - Jake Maymar
<Q>Are you using like no-code platforms, GPTs, TypeScript, Python?</Q>

00:35:05 - Al Cole
<A>Based on my conversations with them, I was thinking of using N8N [tool:N8N] for just modelling it out, keeping it super simple. And from there, if I'm being honest, once I get a few of those built, I'll look for — if I was to automate the whole thing, would it be repeatable and would that investment make sense? I could bake in more engineering around it. So I was keeping it simple for this go-around because I figured it'd be easy to explain to them how it works.</A>

00:35:55 - Jake Maymar
▶ What's really nice about N8N is you can put it in front of a customer client on a call, and they have ideas — "oh, can we do this?" — and you can actually do it on the call. You can create a running workflow. And as soon as they have that, you've got the sale, but also now they have ownership of it, and that project often has a lot more life.

00:39:53 - Andrew Nanton
<Q>One, do you feel like there is a danger in showing people a workflow on a call that gives them the impression that if you bill them for 10 hours, you're just wasting time — because in 15 minutes you showed us a proof of concept? And question two: I've been going deeper down this rabbit hole of evals. What tools, resources, or strategies do you recommend, because it seems like that's where the buck stops?</Q>

00:40:48 - Jake Maymar
<A>I think evals is a secret sauce. The first thing — client wants to use AI, I show them a workflow that does something very simple, demonstrating we could make a workflow. But what they want to do is very complex. I say, okay, we're going to go away and come back and do it in N8N or whatever makes the most sense. A very complex 500-node thing, I'm not going to show to a client — they're going to just glaze over. Most of the time the decision maker is an executive and they just want the solution. So a lot of times N8N is a POC showing you can get something relatively close to one of the things they care about. But there's a lot of work in the background.</A>

00:42:35 - Jake Maymar
On the eval side — my old data science side. Really simple things: is it hallucinating? That's one of the big questions. Andrew, what I think is really valuable is look at fine-tuning — every fine-tuning anything has evals associated with it.

00:43:12 - Bastian Venegas
<A>I haven't built a generic eval suite, because I think the main issue is trying to get the buyer and the people who will use this excited about the opportunity. If they don't really want it, or if they have a vague idea, I would just try to build it in different phases or stages. I worry about the evals, but I basically just manually checked at the beginning, and then different versions of LLM-as-a-judge. I like rubrics for that — 0 to 5, or some things can be translated to booleans. But first you need to see what's valuable to the users, because maybe hallucination is not the most relevant, as long as the user can detect that it's hallucinating.</A>

▶ Bastian Venegas: Prioritise understanding what users actually value before designing an eval suite — hallucination tolerance varies by use case.

00:45:32 - Jake Maymar
I do LLM-as-a-judge all the time. Spot check, manual. And then I'll skip to client: "hey, here's the data, check it." And you're like, "oh, it's too much to check." Well, if you want us to check it, you have to pay for it. A lot of times they do not want to pay for evals. They want quality work, but they don't want to pay for evals.

00:45:49 - Neel More
<Q>Jake, just a follow-up question on N8N. Don't you face any data privacy issues, or do you self-host N8N?</Q>

00:45:56 - Jake Maymar
<A>It depends. N8N is SOC 2 Type 1, Type 2, and HIPAA compliant if you pay for it. So it all depends on what kind of data you're running with. A lot of times you're doing a data audit of the kind of data you have, and that really does affect the budget.</A>

---

<!--SEGMENT
topic: N8N-to-Code Conversion and LangGraph as Next Step
speakers: Al Cole, Jake Maymar, Patrick Chouinard, Andrew Nanton, Paul Miller, Marc Juretus
keywords: N8N, JSON export, Python conversion, LangGraph, Cursor, Claude Code, spec generation, MCP for N8N, node debugging, workflow templates, Patrick Chouinard
summary: Al Cole proposes using N8N's JSON export as a specification to auto-generate Python equivalents via Cursor or Claude Code, reducing reliance on N8N for production workloads. Patrick extends this by suggesting the JSON be translated into a structured spec for code generation. Jake shares an existing (but stale) MCP that builds N8N flows. The group also discusses LangGraph and Crew AI as natural next steps beyond N8N for more complex workflows.
-->

01:03:34 - Al Cole
<Q>If you thought of N8N as that prototype or small workflow tool, how hard do you think it would be to come up with a spec that ultimately went through Cursor and Claude Code that would convert the exported flows into a Python equivalent?</Q>

01:03:57 - Jake Maymar
<A>That's brilliant. I'm wondering if N8N is already sort of in the water already, but that's brilliant. Let me share this MCP — so this MCP builds N8N flows. You can use it in Cursor, you can use it in other places. It's an MCP that understands all the nodes. It's very much like Context7, but specifically for N8N.</A>

01:05:26 - Patrick Chouinard
<A>Because N8N is nothing more than JSON files anyway. Not necessarily to use it directly to code, but more use it as a spec and build yourself some templates — exactly like what Brian showed us in terms of templates. Build a prompt that will use the JSON file as a spec, translate it into a proper spec for Cursor, Claude Code, whatever. Use it as a specification and have a prompt to translate it from JSON to a proper spec for your code building.</A>

01:06:16 - Al Cole
I was trying to take the LLM out of it for deterministic reasons and just do more of a mapping of nodes and behaviour implied in the nodes based on the services you're engaging. There could be a ton of complexity there, but this could be a fun side project.

01:06:51 - Patrick Chouinard
You start with these specs and it really depends on the calibre of the LLM as to what you're going to end up with. But if you have some solid spec — and I think the templates that Brian shared last week were extremely useful specifically for that, because they give you something precise enough that leaves very little chance for deviation.

01:08:51 - Paul Miller
<Q>Do we think LangGraph is the place to take it to? Where do you go if you're going from N8N to the next level?</Q>

01:09:14 - Marc Juretus
<A>LangGraph [tool:LangGraph] is pretty powerful. I just remember when I was learning it back in February, the tools kind of sucked when you were trying to add tools within the flow, but I've heard that's gotten better. I've also done some stuff with Crew AI [tool:Crew AI].</A>

---

<!--SEGMENT
topic: ChatGPT Agent Mode and Token Cost Optimisation
speakers: Patrick Chouinard, Jake Maymar, Paul Miller, Adam, AbdulShakur Abdullah
keywords: ChatGPT agent mode, O3, scheduled tasks, cron jobs, prompt caching, GitHub Copilot, Gemini CLI, Claude Code, Cursor, token optimisation, layered tooling, markdown output, school community scraping
summary: Patrick demonstrates using ChatGPT agent mode with O3 to autonomously scrape and analyse the School community board, producing a ranked list of posts worth responding to. He details a layered token-optimisation strategy: GitHub Copilot for proto-prompts, Gemini CLI for documentation generation, and Claude Code only for final task execution. The group discusses scheduling agent tasks, prompt caching, and the 40-task-per-month limit on the $20 plan.
-->

01:15:18 - Patrick Chouinard
I did a couple of attempts using ChatGPT agent mode [tool:ChatGPT agent mode]. And basically I used it to read the board on School, go through every single post, then categorise the different posts, use its own memory of what I know and I'm interested in, do a top 10 of things I could respond to, then generate a response that it would look like what I could have answered, and then give me the top five it would recommend me to answer and propose a basic structure for an answer.

01:16:16 - Patrick Chouinard
It worked surprisingly well. It worked for 20 minutes straight before giving me an answer because it really went through the whole board and picked up everything. I'm not saying this is the use case to use the tool, but it's interesting to see that it can go through a massive amount of stuff — not just to do research, but to combine research, memory, and even understanding of its user in order to propose posts.

01:17:05 - Jake Maymar
<Q>Patrick, what tool is this? And what was the sort of cost — is that the $200 a month plan or can you run that for $20 a month?</Q>

01:17:23 - Patrick Chouinard
<A>I'm on the $20 a month plan and you have 40 of those per month.</A>

01:17:52 - Patrick Chouinard
Agent mode can be scheduled. It can be scheduled as a GPT task.

01:18:04 - Patrick Chouinard
Keep in mind that you have 40 calls per month. So if you do a cron job that runs 10 times a day, four days and you're out. And I've realised that it works very well for anything below half an hour. If you give it a long-running task that will have it churn longer than that, it starts to not be as cool after half an hour.

01:19:00 - Patrick Chouinard
▶ Don't try to get the perfect output from agent mode. Just try to get the perfect scraping. Once you have the output, then just give it to a normal LLM to process it any way you want to extract the information from there.

01:22:38 - Patrick Chouinard
▶ One thing — because of the new limits in Cursor and Claude Code — instead of burning through my Claude Code credit to do the planning, I have GitHub Copilot [tool:GitHub Copilot] with Gemini CLI [tool:Gemini CLI] in the terminal. I use Copilot to co-write my proto-prompt. When I have the prompt, I give it to Gemini CLI, and I start to create the documentation with Gemini CLI because there's almost unlimited credit there. So I will create all of my documentation, get my project where the PRD has been defined by discussing with ChatGPT verbally, then generate all of the task documentation with a composite of GitHub Copilot and Gemini CLI. And then I start to use Cursor and Claude Code to actually execute the task.

▶ Patrick Chouinard: Split token usage across as many tools as possible — Copilot for proto-prompts, Gemini CLI for documentation, Claude Code only for execution — to stay on the $20/month plan without hitting limits.

---

<!--SEGMENT
topic: AI Bubble Economics and Local Model Viability
speakers: AbdulShakur Abdullah, Jake Maymar, Patrick Chouinard, Mitch, Andrew Nanton, Neel More, Paul Miller
keywords: AI bubble, Ed Zitron, DeepSeek R1, Kimi K2, OpenAI open-source, GLM 4.5, ATI GPU, NVIDIA, quantization, mixture of experts, local models, subsidised pricing, dot-com bubble, open weights, consumer hardware
summary: AbdulShakur raises Ed Zitron's argument that foundation model providers are heavily subsidising usage and that current pricing is unsustainable. The group debates parallels with the dot-com bubble, with Jake arguing quality AI will survive a correction as quality websites did post-dot-bomb. Patrick and Andrew note that local models are rapidly improving and may handle common tasks within a year, reserving expensive cloud models for complex work. Andrew highlights GLM 4.5 Air's one-shot Space Invaders demo as evidence of local model progress.
-->

01:35:06 - AbdulShakur Abdullah
I feel like the free lunch is coming to the end of its life. I don't know how much longer they're going to keep subsidising. So unless the models get a whole lot more efficient and cheaper, I don't know how much longer we'll be able to use things like Claude Code and Cursor to our heart's content.

01:36:17 - AbdulShakur Abdullah
That video I dropped was from Ed Zitron, who keeps coming up talking about how AI is a giant bubble right now, and no one's really making any real money. Essentially we're all being subsidised for a while and it's going to end soon.

01:36:54 - Jake Maymar
<A>I do feel like we're in a bubble, and I think we've been in a series of bubbles. But this is the first time I'm seeing just across-the-board activity. There's a tremendous amount of hunger to get workflows, whether no-code or actual implementations. My question is just like the dot-bomb — there was a whole bunch of really extremely useful websites, amazing websites, and a whole bunch of garbage. And there's a lot of garbage AI. I still think the quality stuff will rise to the top, because after the dot-bomb there were still people making websites — they just had to make them the right way, commercially viable, aware of SEO. So it's like: growing, growing, growing, it collapses, then rebuilds in a structured way.</A>

01:38:25 - AbdulShakur Abdullah
Ed's whole argument is the inherent bubble is not with a lot of this surface stuff we're referring to, but it's within the foundation models — Google, Claude, ChatGPT — they're all heavily subsidising our use. Even if we're on the $200 plan, we're still costing them money because of the amount of compute and resources that go into our different requests. None of the efficiency advances like DeepSeek R1 [tool:DeepSeek R1] or Kimi K2 [tool:Kimi K2] are really driving us to the point where $20 or even $200 a month covers our costs. But would any of us be willing to pay $2,000 a month for what we're doing?

01:41:02 - Patrick Chouinard
▶ I think we're also extremely early. This has been publicly common for most people since the end of 2023 — we're not even a full two years into it. Look at where we were a year ago and where we are today. The local models coming out are not yet to the grade of Claude Code, but they're getting extremely close for something that runs on $200 to $5,000 worth of hardware. Give it another year and you're going to have something that will do most of the common stuff locally, and whatever requires the large $200–$2,000/month model will be reserved for extremely complex tasks.

01:44:37 - Andrew Nanton
There's also the OpenWeights GLM 4.5 Air [tool:GLM 4.5 Air]. I posted a link to an eval of that — the Simon Willison one — that Space Invaders demo. It was a 44 GB download, and he was running it on a MacBook with 64 GB of RAM, and it one-shot coded Space Invaders. [link:simonwillison.net] And that's all running locally.

01:45:39 - Andrew Nanton
I was seeing some speculation today that OpenAI released these open-source models in preparation for a bigger model announcement later this week — maybe GPT-5 [tool:GPT-5] or some really big step forward where it's like: these open-source ones are kind of neat, but if you're looking for something a lot more powerful, here's what you get.

01:46:22 - Andrew Nanton
With some of the quantization and mixture-of-experts models getting down into a size that could feasibly be run on consumer hardware, that's looking pretty good. And the murmurings I'm hearing about ATI's next architecture — I'm sure it'll never catch NVIDIA anytime soon, but it ought to have more oomph than Apple's GPUs. You might be able to get a board with 96 or 128 GB of RAM for not $8,000 like NVIDIA wants — maybe $3,000 or $4,000. It might look a little bit more plausible to run some actually useful models locally.

---

<!--SEGMENT
topic: Front-End Tooling, Streamlit vs Next.js vs Lovable
speakers: Neel More, Jake Maymar, Marc Juretus, Paul Miller, Prem
keywords: Streamlit, Gradio, Next.js, Lovable, FastAPI, Supabase, Railway, portfolio project, Google ADK, UI/UX, client demos, Cursor, tRPC
summary: Neel asks whether to use Streamlit/Gradio or Next.js for a data science portfolio project. Jake recommends Lovable for front-end prototyping, while Marc advocates for Next.js with Cursor for its simplicity and FastAPI integration. Paul emphasises that clients judge by UI/UX quality and that Lovable paired with a FastAPI back-end is a fast path to a polished demo. Prem confirms Cursor-generated Next.js UI exceeded expectations with minimal prompting.
-->

01:49:37 - Neel More
<Q>For data science projects, we definitely use Streamlit or Gradio for the UI. Has anyone tried Next.js, or would you recommend sticking with Streamlit or Gradio? And when you do a demo to clients, do you create a web UI in Next.js or React, or do you use Gradio or Streamlit?</Q>

01:50:14 - Jake Maymar
<A>I did a lot of stuff with Streamlit [tool:Streamlit], and I felt like my hands were tied a lot of times. Lovable [tool:Lovable] — that's kind of what I'd recommend. I highly recommend Lovable. That's going to get you pretty happy with your front end, and then figuring out your back end, you already kind of have that flow in place too.</A>

01:51:15 - Marc Juretus
<A>I use Next.js [tool:Next.js] for a lot of the little front-end stuff I'm doing. It's just so easy to use — create a directory, another page, just a TSX file. It serves it up pretty nice. I don't use vibe coding to create the actual Next project because it does it in a weird manner, but I'll just do the command line where you create it with the structure, and then from that point I'll say, "hey, in the influencers folder, page.tsx, I need you to do this and consume this FastAPI [tool:FastAPI] endpoint." It blew me away — it was pretty amazing. Everything I'm serving up is FastAPI with the back end calling the agents. Bastian helped me get it deployed on Railway [tool:Railway].</A>

01:52:23 - Paul Miller
▶ Commercially, people judge you from that UI/UX. They see a really good UI/UX and that's why I use Lovable. I got the back end with FastAPI like Marc did, but I'm just not as familiar with doing that JavaScript stuff in the front. Getting Lovable to create something and then porting that across was a really fast way to get there.

01:54:01 - Prem
▶ I was relatively new to Next.js — was on Angular and other areas — but the UI that Cursor generated was phenomenal. With very few prompts it created amazing UI. As far as the API, if you have simple CRUD applications or you've already done the heavy lifting on the API, it works like a charm. I didn't have to touch most of the UI code it generated. It kind of outdid any graphic designer I've worked with.

01:55:36 - Neel More
I know context engineering is going around. I was wondering — has anyone tried creating a RAG for your examples or code base, and then intercepting the call before it goes to the LLM, doing a RAG query, and making changes to your prompt so that you get a correct answer from the vibe coder?

01:56:49 - Andrew Nanton
<A>What I ultimately fell back to is: the context windows are so small that I find myself doing one of two things. I either say "use Context7" or I give a specific link to a specific documentation page — like a very manual kind of RAG. And sometimes if it's something I find I'm referencing a lot, I might just save it as a markdown file in the repo and edit it down to one or two pages focused on the specific feature I need.</A>

01:59:42 - Bastian Venegas
▶ Repo Prompt [tool:Repo Prompt] has an MCP server now that runs locally, and you can connect to any IDE or Claude Code or whatever. It's really cool to delegate all of the context management and searches to it. You can connect to a Cursor agent, for example, and ask it to — I mean, you want to try it at least, because I feel like it has better search tools than Cursor.

---

=== UNRESOLVED SPEAKERS ===

The following speaker names appeared in the transcript but were not present in the SPEAKER_ALIASES context block and could not be resolved:

- **Sam** (00:14:04) — participant discussing Windows/WSL/Docker environment issues with Claude Code
- **Adam** (00:30:18) — participant discussing networking events, business cards, insurance industry contact, and ChatGPT web agent
- **abhi** (00:54:40) — first-time attendee, San Francisco, exploring Google ADK for L1/L2 support automation
- **Mitch** (01:10:00) — participant working on AI video generation workflow with VO3, Gemini 2.5 Pro, Supabase, Open Router; discussing Kiro and Warp
- **Prem** (01:26:49) — participant on $20 Cursor plan, on Kiro waitlist, using Google ADK, asking about Cursor alternatives
- **asako** (01:28:03) — participant who has used Kiro, comparing it to Cursor for planning vs. coding
- **Neel More** (01:30:18) — participant using Gemini CLI, Google ADK, working on data drift detection portfolio project, asking about Trae/T-R-A-E IDE
- **StephenAmstutz** (02:00:07) — first-time attendee, networking/cloud infrastructure background, building observability platform, asking for AI news sources