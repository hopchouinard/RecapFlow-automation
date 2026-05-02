=== SESSION ===
date: Unknown (Tuesday, estimated mid-June 2025 based on content references)
duration_estimate: ~2 hours 48 minutes
main_themes: RAG application development, chunking strategies, agentic frameworks (ADK, CrewAI, LangGraph), developer tooling (Cursor, Context7, Supabase), AI replacing developers debate, LinkedIn growth tactics, client project demos, voice agents, Convex/LangSmith evaluation

---

<!--SEGMENT
topic: Pre-Call RAG and Chunking Discussion
speakers: Andrew Nanton, alexrojas
keywords: RAG, chunking, Chunky library, semantic chunking, fixed chunking, context windows, GPT-4.1 mini, Supabase, PGVector, embeddings, legal assistant
summary: Andrew and Alex discuss the Chunky library and chunking strategies for a legal RAG application Alex is building. Andrew argues that large context windows reduce the need for aggressive chunking, and recommends semantic over fixed chunking to avoid context loss at chunk boundaries. Alex describes a hybrid SQL-plus-embeddings architecture inspired by a previous community session.
-->

00:01:18 - Andrew Nanton
How's it going?

00:01:20 - alexrojas
What's up, Andrew?

00:01:21 - alexrojas
All good, all good?

00:01:24 - Andrew Nanton
Good.

00:01:25 - Andrew Nanton
How's your class going that you're teaching?

00:01:27 - alexrojas
Good. I'm actually starting next week, given that it's government.

00:01:37 - alexrojas
They need a little more extra time.

00:01:40 - Andrew Nanton
Sure, sure. No, I work part-time in a government job.

00:01:44 - alexrojas
I know how that goes.

00:01:47 - alexrojas
There is a lot of changes, no?

00:01:50 - Andrew Nanton
Well, and everything moves slowly at the best of times.

00:01:57 - alexrojas
That is the fast phase, huh?

00:02:02 - alexrojas
Hey, Andrew, actually, I was looking into the Chunky library [tool:Chunky] that you shared.

00:02:09 - alexrojas
<Q>Do you use it a lot?</Q>

00:02:12 - Andrew Nanton
<A>I've used it some. You know, I've found that since I have been poking into things more, I've been going more into actually sticking together larger pieces of context rather than splitting them up into smaller bits. But I'm not doing RAG per se, right? Like, initially, RAG was kind of relevant to my workflow because context windows were so small, but now they're so big that, at least for the stuff I'm doing.</A>

00:02:45 - Andrew Nanton
Just also because retrieval of chunks is — like, if it were perfect, then everyone would use RAG all the time because why wouldn't you? But it's that retrieval step, and now that context windows are bigger, at least for the stuff that I'm doing, there's a — but it's like — it's very manual kind of work where it's, you know, look at different intermediate products and then combine them. And so it just — for my workflow, I've been using it less. But I have used it some and found — did you run into an issue with Chunky?

00:03:21 - alexrojas
Yeah, because I actually — I'm doing a RAG application for legal consumption of, like, laws. It's for a lawyer friend. So I saw in Chunky that they have a very good semantic chunking. And now I'm using just the fixed chunks. But I haven't gotten to that point where I need to do eval, let's say. I wanted to make it — put it up and running first and then see how — use Chunky and then evaluate it versus just, like, 500-token fixed chunks.

00:04:03 - Andrew Nanton
<A>So what I would say is that given how large context windows are now, including in, you know, GPT-4.1 mini [tool:GPT-4.1 mini], which is great for a lot of stuff, that it might make more sense to look at the chunks that you're getting and split them semantically in some way. You know, whether you're bringing in PDFs or HTML, but just make sure that the boundaries of the chunks seem reasonable and make sense because you have so much context window to play with. And the consequences of shearing a chunk where you're missing context are so high that, you know, I'm definitely a big fan of — you should be looking at your data at every step of the workflow.</A>

00:05:00 - Andrew Nanton
Like, is the stuff that's going in reasonable? And if so, then you probably are going to get reasonable results. But, like, I think fixed chunking, especially with no overlap, is — because it's so much easier. ▶ You probably will get substantially better performance with very little effort by just adjusting how you're chunking.

00:05:24 - alexrojas
Okay. Yeah. I'll try it out and see how it compares.

00:05:31 - Andrew Nanton
Yeah, see what you get, right? Like, maybe what I'm saying actually makes no difference. But at least for the stuff that I'm doing, I've noticed that it tends to make a pretty big difference.

00:05:45 - alexrojas
I'm actually leveraging this super-based thing that you could do double-tagging. So I prepare SQL and embeddings. So, you know, they're tied together and the queries use both of them. Yeah, add a third, do graph RAG, why not? I'm getting ambitious here. With two, I feel I'm being ambitious.

---

<!--SEGMENT
topic: Community Announcements and Upcoming Events
speakers: Brandon Hancock, Marc Juretus, AbdulShakur Abdullah
keywords: CrewAI, Dan Martell, AI incubator, Shipkit, Interrupt conference, LangChain, guest speaker, AI business, templates
summary: Brandon opens the formal call with several announcements: a rescheduled CrewAI call with Joe, an upcoming guest session with AI incubator operator Dan Martell, and a new project called Shipkit — a template-driven toolkit for launching AI applications. He also highlights the LangChain Interrupt 2025 conference playlist as a key resource for understanding how enterprise companies build agentic systems.
-->

00:06:20 - Brandon Hancock
What's up, everybody? Hope you all have an awesome Tuesday so far. Let's do a call order. Cool updates for you guys before we kick off the day.

00:06:40 - Brandon Hancock
So I actually got sick on, like, Thursday last week, so I didn't get to do the call with Joe for Crew AI [tool:CrewAI]. So that's this Friday now. And then another one — not next Tuesday, but the following one after that — we'll probably do a guest speaker for one of our weekly coaching calls.

00:07:04 - Brandon Hancock
I don't know if y'all have heard of Dan Martell, but he basically will probably come on — super excited for this, actually — because he basically is doing a lot of AI project incubation. So we're going to talk about a bunch of topics for you guys around building AI businesses and so forth. But one of the cool things is they run an incubator, basically, is the way I would describe it. So they take in thousands of requests from all sorts of AI businesses. And one of the cool things is they're just going to kind of share, like, hey, this is exactly what we have seen, high level. Here's what makes a good AI company, bad AI company. Here's what we're looking at funding. Here's cool projects that we recommend. So very excited for that. So most likely not this Tuesday — that's right, the following Tuesday, but the one after that. So I think it's like July 1st-ish.

00:08:10 - Brandon Hancock
Actually two updates, I lied. I've been busy, man. I've been cooped up. I've just been sitting on the couch having to brainstorm.

00:08:32 - Marc Juretus
Yeah, man. I like that dude. I've actually followed a bunch of his videos already because he likes to work out like I do.

00:08:38 - Brandon Hancock
So he's a cool dude, man. Yeah, just got to meet him last week.

00:09:10 - Brandon Hancock
Marc, you and I got to actually talk about this a little bit ago, but I want to show everyone else, too. So, cool new project I'm working on next. So, long story short is, you know, last year, I did the full-stack marketing platform course to teach you guys how to build a full-stack AI application, you know, full learning experience. I learned so much about making courses. So, what I'm doing now, a new project called Shipkit [tool:Shipkit], and basically what I'm doing is templateizing the entire process of making AI applications — chat applications, RAG applications, and agentic applications. So, there's just gonna be an insane amount of templates and prompts to literally guide you from I have an idea to a production application you shipped. So, it's all gonna be copy-and-paste code. Basically, because I don't really code that much anymore — I just use AI prompts to help me do it. So I'm in the middle of building this out. So we'll definitely keep you guys posted as I make more progress.

00:10:11 - Brandon Hancock
But like I said, the whole goal is just every part of the way — I'll just show you guys — but, you know, I'm kind of building it all out as we speak right now, but everything is prompt-driven. So that's one of the main takeaways from my last course is, like, you kind of had to just watch me build the whole thing. And then after you got done, you're like, cool. Now I need to go build an application. And this one is flipping it on its head to just, like, you know, the whole goal of Shipkit is to help you launch an AI application in a week, basically.

00:11:16 - Brandon Hancock
Upcoming video — I want to do the — I don't know if you guys have got to watch this yet. Definitely want to recommend this resource if you guys haven't seen it yet. But the Interrupt series by LangChain [tool:LangChain] is probably one of the biggest hidden gems, I think, on the internet right now when it comes to building out agents and agentic applications. Interrupt 2025. Yeah, so this playlist right here — it has, I think, 11 different videos in here. Everything from Andrew Ng talking about it, how Uber is building agents, JP Morgan's building agents. So it's like they're not holding anything back — they literally walk you through, here's exactly how we are building agentic applications in some of the world's biggest companies.

00:12:19 - Al Cole
So, but that's probably the next thing — I'm LinkedIn one, Brandon, and it was insightful. They were essentially — I've got a recruiting platform on top of LinkedIn. And so they've got an AI agent, which you just give it a prompt of what you're sourcing for your talent. And it just goes out and finds the best matches based on your profile. It was pretty compelling.

00:12:42 - Brandon Hancock
And it's insane. So yeah. Seriously, thanks for sharing that. So yeah, if you guys have it, I'll drop a link in the chat. [link:LangChain Interrupt 2025 YouTube playlist]

00:13:00 - Brandon Hancock
Those are all the updates on my side, and earlier in the chat at 6:01, I dropped in the call order I'm going to go through, so Alex, you're up first, but before we start, I just want to say, Sam, I love the chicken hat, so just want to give a shout out to Sam before we kick things off.

---

<!--SEGMENT
topic: Legal RAG App Architecture and ADK Stack Decision
speakers: alexrojas, Brandon Hancock
keywords: RAG, legal assistant, ADK, Google Agent Development Kit, Next.js, Supabase, PGVector, embeddings, SQL, Vertex AI, multi-agent, LLM calls
summary: Alex presents his legal RAG application built with Next.js and Supabase, using a hybrid SQL-plus-embeddings architecture. He asks whether to adopt Google ADK for multi-agent functionality. Brandon advises that simple RAG use cases don't require full agentic architecture, recommends sticking to direct LLM calls with vector store queries, and walks through a Supabase match function for RAG retrieval.
-->

00:13:22 - alexrojas
Yeah, hey, looking forward for that Shipkit, man, that would be pretty dope.

00:13:31 - alexrojas
Yeah, I love Dan as well, man, I'm a big follower of his, so yeah, I just keep doing some YouTube editing — I think I've realized, Brandon, that you were right, I need to get an editor. It's become a nightmare for me, I'm like, I barely have time to code, and so that was a key realization. And also, I've been working on a RAG application for a legal assistant. Like I told you last time, I am trying to get my fingers wet and, you know, learn that way. So I started doing kind of, trying to grab one of your agents from a video and then modify it, and it was quite messy. So I decided to take a go at your video of how to develop it. So I went, actually, through the prompts and, you know, used Next.js [tool:Next.js] and everything. And I had a lot of learnings.

00:14:34 - alexrojas
But my specific question is, I want to develop more ADK [tool:Google ADK] agents, right? And now I ended up using the stack of Supabase [tool:Supabase]. I struggled a lot with Google authentication. I tried to be in the Google environment, Vertex AI [tool:Vertex AI]. I spent way too much time with those problems. So I just use Next.js and Supabase. And based on what Paul inspired last time, I'm doing double tagging. So I'm doing the SQL schema and the embeddings at the same time. And they are tied. So yeah, like I wanted to make that multi-agent, but that is just easier. So now I finally make everything work.

00:16:00 - alexrojas
<Q>Before I take it any further, should I focus on what stack in order to be more ADK-friendly?</Q>

00:16:04 - Brandon Hancock
<A>Good question. Okay, so I would actually, before saying just like, oh, multi-agent — I mean, when it comes to doing just general, like, level one RAG queries, like, you really don't need a full-blown agent to go deep into that path. Like, there's nothing wrong with just making a query to your vector store and just, like, getting answers back and providing it as context. Like, that's completely fine. The main reason you want to do agents is when you want to, like, you know, plan, take action, did you get the information, come back, take other action — like, that's when you want to go more agentic.</A>

00:16:57 - Brandon Hancock
▶ So, I mean, there's nothing wrong with just making multiple LLM calls to get context from your vector store, putting all of that back into a prompt and saying, like, here's some additional helpful resources. You don't always have to go agents, especially with RAG. You usually have to have a very good reason to go from single-shot LLM calls with RAG to a multi-agent solution. So, yeah, I would actually just stick right now to just straight-up LLM calls.

00:18:00 - Brandon Hancock
Really fast, here's what you do to get this to work in Supabase, so long story short, like, you're going to have a fetch — basically, you're going to make it like a — in Supabase, you can create functions that take action inside on your database, so in Supabase, I created a function called Match Artifact Sections, and basically, I just passed in the embedding, how many do I want to get back, the threshold — like, how picky am I being, how many do I want to get back — and then I added some metadata to say, like, hey, I only want to get information back for these types of artifacts. So, like, I only want to get information back on product A, or I only want to get information back on product B.

00:19:03 - Brandon Hancock
And a lot of this you can steal from this YouTube video I did a while back on Supabase. [link:Brandon Hancock Supabase RAG YouTube video] You can steal it because a lot of the same principles apply.

00:19:27 - alexrojas
Okay, perfect. Yeah, actually, I got that idea from you because Supabase allows you to do the SQL and PGVector [tool:PGVector].

00:19:39 - alexrojas
Yeah, I learned the hard way that Google Cloud Run doesn't allow PGVector. It's such a pain.

00:19:47 - Brandon Hancock
Yeah, it's a pain. So any final things I can help with? Oh, and real quick, I owe you — I can send you a link after this to a good editor. I'll connect you to a guy.

00:20:20 - alexrojas
Yeah, so thank you very much.

00:20:31 - alexrojas
Finally, I got to the connection side, and it's beautiful. As you say, it's all working. I feel like having Cursor [tool:Cursor] is like having an intern that you can exploit. Amazing.

00:20:40 - Brandon Hancock
No, it's insane. I mean, it's a cheat code.

---

<!--SEGMENT
topic: Cursor Workflow, Context7, and Spec-Driven Development
speakers: Andrew Nanton, Brandon Hancock, alexrojas, AbdulShakur Abdullah
keywords: Cursor, Context7, MCP, specification documents, implementation plans, Tauri, FastAPI, TypeScript, Python, agentic development, documentation
summary: Andrew describes his evolving development workflow — using spec docs and implementation plans rather than directly editing code — and asks about agentic coding tools like Claude Code and Codex. Brandon enthusiastically endorses Context7 as an MCP tool that gives Cursor access to 19,000 library documentation sets, dramatically improving code accuracy. The group discusses the shift toward spec-driven, AI-assisted development.
-->

00:21:24 - Andrew Nanton
So yeah, a lot of the stuff that I'm doing is, you know, because of the kinds of files that I'm working with, I'm doing a lot of working with local files on disk and almost all of the web frameworks that I've tried for that are like, there's a lot of hoops you have to jump through to work with local files. So in some of the most recent experiments that I've been doing — and I think this sort of reflects my path along doing this stuff — really the only language I know is Python, right? Like, that's the only language I know. And I'm not an expert. And so I was looking at ways to work with things locally, and I feel like more and more I'm just falling back to, as I'm developing a plan with an LLM, I'm like, well, I don't know, what do you think? Sure, we'll go with that, because if that's what you know, then you're going to be writing it anyway.

00:22:22 - Andrew Nanton
And I feel like more and more, so this most recent prototype that I'm working on is Tauri [tool:Tauri] for the, you know, like a Rust-based Electron equivalent, and TypeScript, which at least I know a little TypeScript. But I just feel like more and more the workflow that I'm falling into — which it sounds a little bit like, if I'm reading between the lines correctly for you, Brandon, more like what you're falling into at times — which is like, most of my work is in specification docs and implementation plans. I'm like, okay, update the spec, all right, what have we done? Update the implementation plan. Let's start a new chat, fresh context window, review these two, let's move on to the next step, write some tests. Tests are boring and terrible, but you don't mind writing them, so write the tests. Did you break anything? Okay. And I feel like this is kind of the groove that I'm settling into in a lot of the work that I'm doing. And I'm curious if that's true for other people, too.

00:23:30 - Brandon Hancock
I mean, real quick, for me at least, I mean, 100% spot on. I mean, that is my current workflow. I mean, the AI docs folder that I showed in that last video, I use that religiously. Like, I cannot express to you guys enough. Between AI docs, cursor rules, Context 7 [tool:Context7] — thank you, Andrew — and I can't remember who else called that one out, but if you guys haven't started to use Context 7, insanely powerful tool. What it allows you to do is — let me just actually showcase it really fast.

00:24:09 - Brandon Hancock
So basically what Context 7 does is it has all the most popular docs that you could think of, it has them actually saved as just text files. So what's amazing about this is you can set up — and you're — let me actually go to some code so I can just show you how easy it is because it is wild how easy it is. But yeah, all you do is just say, you know, set up your MCP [tool:MCP] server, just point to the remote URL, Context 7, and now any time you're chatting with your agents and you're like, hey, you're not really doing what Tailwind [tool:Tailwind] is supposed to do, here, refer back to the Tailwind documents and check out what the latest docs say on how you should update global variables for style, or so forth, you know, and the agent will go, okay, cool, I'm using Context 7, I'm looking up the library, I found it, okay, I now understand exactly how this library works, and then it just spits out correct code.

00:25:16 - Brandon Hancock
▶ So, and the fact that all it takes to get access to all the latest documents is this one line right here is honestly stupid. So, definitely, thank you, Andrew, and I cannot recommend that one enough.

00:25:38 - alexrojas
You keep it in the JSON, so if you want, you just make a list of whatever — I'll just drop it real fast. It's an MCP config and you set it up once, and unless it's a really exotic library, it's in there.

00:25:56 - Brandon Hancock
So, I'm dropping it in chat right now, just so everyone could steal it. [link:Context7 MCP config snippet] Yeah, you just — in your .cursor folder, you have MCP, which is where you're going to set up all your MCP servers, and what's nice is they have a public URL to handle everything, and that's all you have to paste. And then when you're inside Cursor, you just say, use Context 7 to look up — and like I said, it has access to Next.js, Tailwind. It has access to almost 19,000 libraries. So, if you're using any tool, it has 19,000 libraries, and it'll look it up, find it, and use it instantly to help provide context to help you build better and faster. ▶ So, cannot recommend that one enough. Cheat code, honestly.

00:26:54 - AbdulShakur Abdullah
<Q>Why do you put it in your .cursor folder and not like the MCP server folder? Or is that the same thing?</Q>

00:26:56 - Brandon Hancock
<A>Yeah, same, same.</A>

00:27:06 - Brandon Hancock
But yeah, Andrew, going back, though, to what you're doing on your development journey, cannot say it enough. I mean, at this point, I am a senior engineer who's — or whatever engineer — just looking over a bunch of other engineers, making sure they're doing the right thing. So, yeah, definitely recommend keep going down that path.

---

<!--SEGMENT
topic: Andrew's Document Processing App and Agentic Coding Tools
speakers: Andrew Nanton, Brandon Hancock, Bastian Venegas
keywords: Azure Document Intelligence, FastAPI, Tauri, Rust, Cursor, Claude Code, Codex, Winsurf, context windows, JSON, document hierarchy, agents.md
summary: Andrew demos his in-progress document processing application using Azure Document Intelligence and FastAPI, designed to handle large multi-section documents by reassembling them into a single JSON structure. He asks about agentic coding tools like Claude Code and Codex as alternatives to Cursor. Brandon shares his preference for Cursor's interactive workflow, while Bastian provides practical tips for getting more out of Codex, including the agents.md file.
-->

00:27:51 - Andrew Nanton
And I guess the last question I have is, I've noticed that in Cursor [tool:Cursor], which I've been using — I feel like Winsurf [tool:Winsurf] has kind of fallen off a little bit — I have the context windows that are available in the models are a lot smaller than they are generally available through the API, and I'm curious if anybody is having much success with things like Claude Code [tool:Claude Code] or Codex [tool:Codex] or Jules [tool:Jules] or, you know, these other more sort of overtly agentic systems, because especially I feel like as I'm moving further and further away from editing the lines of code, probably something like that makes sense, but I'm also a little nervous to kind of make the jump, because it seems like a pretty big black box.

00:28:52 - Brandon Hancock
I mean, Claude Code is probably, I think, going to be the winner in this area, because it reminds me so much of Devin [tool:Devin], to where I'm just, like, spinning off jobs, like, go do this, go do this, go do this, and then it just implements them in a PR and allows me to review them. I, my personal feedback, like, if I'm coding, I'm coding. I'm not just thinking of a few tasks and then running away — I just want to build a feature. So, I'm always just in Cursor. I have not truly seen, like, why would I not just use Cursor instead of Claude Code? I haven't had that lightbulb moment yet to, like, oh, I have the use case now to where I don't want to see my code, I just want to spin background jobs off. Like, no, I would just much rather open multiple tabs and just crank out code, where I can actively see it and iterate quicker.

00:29:52 - Bastian Venegas
<A>I have used Codex, and it's pretty good, and they also made some updates recently, the main ones being that you can now ask for a task and ask for multiple versions, so you can later decide which one you like the most, but you always need to set up this agents.md file, that it's kind of like cursor rules, that tells the agent how to — it's additional to the readme file, because it's meant for the agents and not for the humans. So, if you use that, you get a lot more out of Codex, and they also implemented a way for the agent to have access to the internet, like to download some packages that you may need, and you can also download the packages and run your tests and all that.</A>

00:31:06 - Andrew Nanton
So, you'll see here what I've gotten started. There's a couple of steps that I've put in. So for the back end, I went with FastAPI [tool:FastAPI]. I started with FastHTML, which has a lot of FastAPI sort of stuff built into it. I thought FastAPI would be too heavy. But again, like, you know, these LLMs have millions of lines of FastAPI code and zero lines of FastHTML. So even if, in theory, something lighter is a better fit, it's just easier to go with the current and let it use FastAPI because it knows it.

00:31:54 - Andrew Nanton
But yeah, watch is a local file folder. I downloaded an open library copy of Dracula because it's very similar to the documents that I get where it's like one very large document with many small sub-documents inside. I don't know if you've ever read Dracula, but it's like, you know, a series of letters and diary entries and stuff is how it's written. And so I wanted to test the splitting that Azure Document Intelligence [tool:Azure Document Intelligence] is using. So how is it defining the boundaries between these different elements? Because this is a pretty optimal version of the kind of documents that I get, and then on the back end, what I was having it do is Azure Document Intelligence chokes at 2000 pages in creating a JSON representation of the hierarchy of the document. And so I built out on the back end that it will reassemble, you know, an arbitrary length document into one giant piece of JSON, which is shockingly okay in memory still, even when it gets really large.

00:33:07 - Brandon Hancock
That's awesome. Yeah, I'd love to — like I said, the second it's like full end-to-end, like you can click through or ask questions against the documents, I'd love to see a demo. And if you learn any Rust along the way, I'd love to hear your thoughts on it.

---

<!--SEGMENT
topic: ADK Tool Return Format and Supabase RAG Functions
speakers: Marc Juretus, Brandon Hancock
keywords: ADK, Google Agent Development Kit, tool calls, dictionary return, docstring, Supabase, PGVector, Drizzle ORM, SQL, RPC, embeddings, metadata filtering
summary: Marc shares his ADK agent that calls a Chroma embedding tool but gets empty responses. Brandon diagnoses the issue: ADK tool functions must return dictionaries (not strings) and require docstrings. Brandon then demonstrates a Supabase RAG query function using Drizzle ORM migrations and remote procedure calls (RPC), including metadata filtering to scope queries to specific documents.
-->

00:33:27 - Marc Juretus
What's going on, gentlemen? Can you hear me?

00:33:37 - Marc Juretus
Still basically I was consuming Mix.js and FastAPI and Docker containers on top of still going through my Google agent stuff that I'm doing by ADK [tool:Google ADK]. But I did want to tell you, I don't know if you've ever seen an influence of Migos code. So I actually — I've actually been on the phone with him a few times for some advanced Spring Boot Java stuff. But anyways, he just reached out to me like a half hour before the phone call, and asked if I believe that AI will be replacing developers, which I know we've talked about.

00:41:25 - Marc Juretus
Alright, so here's my question. Is there a specific format that you have to return from an agent call that is able to — so basically I did, I took your advice, and I have the Chroma [tool:Chroma] embeddings going, and it's returned. So, to make a long story short, I basically embedded this document, which is from my Rallo port application, and I have it embedded. And anyways, it's this one here. So basically I made it as a class, Brandon, it says embed new, and then I did the if main just to test it locally, as opposed to when the agent calls it, right? So my question to you is — so if I run it here, which basically is just going to call the class, it's going to pass the information — it's going to the Chroma embedding, and then boom, comes back, like got all this — basically the answer is right there. It pulls it from embedding as expected, right? But the problem is now when I use ADK, and I call it, and I see that it's actually calling it, is there a specific format that I have to return it in? Because when I come in here, and I actually run the actual agent, it comes back and it finds nothing.

00:43:07 - Brandon Hancock
<A>Okay, so just a few things I'm noticing. Ideally, for ADK tool calls, you need a docstring. I'm surprised it's not complaining about that. I would have added a docstring just to say what the tool does. ▶ You want to return a dictionary. If you return a string, ADK usually wraps it into a result, but depending on what you're trying to return, it might be doing something weird. So you always want to make sure you're returning dictionaries.</A>

00:44:41 - Marc Juretus
So GetInfo2 should return a dictionary. And you want the docstring basically explaining what the tool does overall. That's getting confused.

00:44:46 - Brandon Hancock
Okay. All right. Yeah. And then I would also — GetTechInfo2 — this should return a string. It should have typings for criteria.

00:46:02 - Brandon Hancock
Next up, let's see — all right, now back to you, Mitch. The floor is yours.

00:47:32 - Mitch
So, one thing is, I saw you using, like, a Supabase edge function. Are you using that, like, over Railway [tool:Railway]?

00:47:37 - Brandon Hancock
Yep. So, it's actually different. Let me just — I'll just show you exactly what it is. I'll share my screen really fast.

00:48:00 - Brandon Hancock
So, this is a client project and — database, database functions, and then this is a public function — match artifact. Yeah, so you can kind of see what it does, but basically — this is like a database function, so there's different types inside Supabase. So this one you can see, it's like, all right, what are the arguments for this database function? Based on that, I'm actually going to perform a raw SQL query on the database, and then it just returns back the artifacts that are similar, and it's only going to return the top three, order by the most similar, limit to the top number. So this is how you do it.

00:49:07 - Brandon Hancock
Um, just real fast, you know, one of the reasons we use Drizzle [tool:Drizzle ORM] is so that we have, like, a migration history. So you can see inside of Drizzle, we've made a function right here. I'll actually paste this in chat, Mitch. But if anyone else wants it too, just let me know. But this is, like, a straightforward function to basically have, you know, perform a RAG query inside of your Supabase vector store. And it comes with this cool little extra field I added — this is where I can filter by metadata. So in my case, I only want to query a certain document. So imagine you had a hundred documents, and I'm like, no. The user's trying to chat with three of them. Here are the three IDs. That way you don't accidentally bring in something about cars if they're trying to do stuff on boats, you know.

00:50:15 - Mitch
<Q>So, if you're doing the function with Supabase, then why are you still using Drizzle on top of that?</Q>

00:50:24 - Brandon Hancock
<A>Oh, sorry, Drizzle — so Drizzle is the ORM, and, you know, it's like what helps us, like, take usual code — like our normal schema that's in TypeScript — and converts it over to an actual SQL table. What's awesome though, is you can use Drizzle to create all sorts of migration files, and in this case, I wanted to, like, not just go into the Supabase UI editor and just manually create something — I like to keep everything as code, so I can always have a log of everything I've ever done.</A>

00:51:10 - Brandon Hancock
So that's why I created a migration that I then applied to the Drizzle database. When I did that, it created a new function. So now I can always call in my code Supabase RPC — I think it's a remote procedure call, but I could be butchering that if anyone knows.

00:51:27 - Ty Wells
Remote procedure call, yeah, that goes back to the 90s.

00:51:28 - Brandon Hancock
Okay. But yeah, so basically it can perform a remote function call. And the function I'm calling is this with these arguments. So yeah. So it's a pretty cool way to actually execute raw SQL queries instead of having to do all sorts of other stuff. ▶ Pretty nice add-in from Supabase. Last thing, you just want to make sure you're probably calling it as an admin. So I have like an admin client that can perform these more advanced queries.

---

<!--SEGMENT
topic: AI Replacing Developers Debate
speakers: Marc Juretus, Brandon Hancock, Al Cole, Mitch
keywords: AI replacing developers, Cursor AI, CRUD operations, Next.js, developer agencies, post-labor economics, David Shapiro, Y Combinator, Michael Truel, LLM capabilities, freelance development
summary: Marc raises the question of whether AI will replace developers, prompted by a message from a popular coding YouTuber. Brandon, Al, and Mitch share nuanced views: AI is progressing up the stack from static sites to CRUD to backend infrastructure, teams will shrink but not disappear, and the opportunity for small one-man developer agencies charging $5K–$20K per project will grow as development costs fall.
-->

00:33:53 - Marc Juretus
I did want to tell you — he just reached out to me like a half hour before the phone call, and asked if I believe that AI will be replacing developers, which I know we've talked about. And I'm like, look, I'm kind of like, just got my feet in this a little bit, but I did — I put in the chat what I responded with, so you guys could debunk it all you want. But anyways, he was asking questions. I said, hey, dude, you ought to join our community. I mentioned you in there, but anyways, I said, you ought to join our community call, because there's a lot of cool stuff that people are doing, and these guys probably can answer the question a lot better than I can.

00:34:54 - Marc Juretus
I've been — since web, I started in 98, so from static pages to databases to content management systems to Java stuff now, but, like, some of this code that it's writing — I mean, it's kind of like my belief, like, on Tesla with the autonomous vehicles — I didn't think the autonomous vehicles would come because I thought it wouldn't be safe enough. I think it's going to get to a point where pseudocoders can just go in there with a few paragraphs and explain themselves and have an app that's functioning. I mean, obviously, guardrails would have to be in place, but that was what I wrote, so I don't know what your thoughts are on that.

00:35:26 - Brandon Hancock
So I want to do a full-blown video on this. Don't know if you guys watch David Shapiro by chance. He has a channel on, like, post-labor economics — I love that we're all nerds and watch the same thing. A lot of his thoughts on, like, post-labor economics I find so interesting. But, yeah, long story short — I mean, I'm starting to get a little bit more worried, but I'll tell you what I'm seeing. In the past, it was just static websites. That's what AI was. Now, it's gone to more CRUD. So anything that's just straight-up database operations — now that it fully understands Next.js, server actions, API endpoints — now that it's starting to do more, it's getting to the level of CRUD, which is like most startups are really just a chat section and CRUD operations. That is at the end of the day what most startups are. So it's getting pretty darn good at that. What's next is like the more advanced features, which is actually like setting up backend infrastructure and connecting it all. That's where I'm starting to say, well, like it does okay at it, but it's still not insane.

00:36:57 - Brandon Hancock
So it is definitely going up the stack, but I mean, is it going to replace developers? My main thought is I still think no, strictly because — just strictly for accountability. Like, a boss or an employer needs to be able to say, go do this, you know? So, like, I don't see — I basically see teams getting smaller, but I don't see, as a whole, like, developers just not existing, you know, because there still needs to be someone to, like — that can answer questions, take action, manage all the code.

00:37:34 - Al Cole
Have you guys heard the Y Combinator interview with Michael Truel? He's one of the founders of Cursor AI [tool:Cursor AI]. So, this is his take over the last week or two. He doesn't view where they are today as a professional level yet, meaning that — you're able to build the basic programs, but where he wants to get to is the million-line codebase, and he does not yet have that capability in what he's building. That's where he wants to get to. So he says he's probably six months away from getting that kind of reach into the codebase, but I didn't hear anything from him saying that this thing wasn't going to progressively get better.

00:38:33 - Marc Juretus
My response was — I see like two to three years, like kind of like Brandon, the way Crew AI builds the whole model for you to start up. I think it's just going to get to a point where you're going to have enough of a framework that an outlier coder could really spin up some powerful stuff.

00:39:08 - Brandon Hancock
One other thought real fast — I do think there will be a lot more work and opportunity for, like, one-off developer shops. One thought I've had recently is, like, hey, as development becomes cheaper because you can do so much more with AI, it takes so much less time. I mean, I think what's going to happen is companies will do a lot more custom solutions for their own stuff. But I think there's going to be an opportunity for just more small, one-off developer agencies to, like, almost, like, be a one-man army of, like, hey, I will build any business anything. I'll charge you $5,000 to $10,000, which is, you know, maybe $15,000, depending on the size of the business and what they're trying to do. And, like, you know, and you're just creating insane value for that company, but it's now becoming affordable. Because in the past, that same solution — two years ago would have been closer to $80,000, $100,000 just because, like, it would have taken a front-end developer, a UI/UX creator just to spin up the whole workflow, and it's, like, front-end, back-end, like, there's so much to that.

00:40:28 - Brandon Hancock
▶ So I do think things are going to become more custom. The only analogy I could think of is, like, back in the day when things are super expensive to do, you had, like, three TV channels for everyone, like, back in my parents' age. And as time has gone on, you've fractaled all the way now to where, like, TikTok, to where there's any content anywhere ever that could be possibly created, it's being created. So I think things are just going to continually fractal down to a super, super niche, and I think which opens up opportunities for you guys, as, like, being able to come in as a one-man army and work and just crank through as many $10,000 to $20,000 projects as possible.

00:46:13 - Mitch
I do have one note with the — is AI taking over coding? I was listening to this guy. I don't really know his credits. But they call him the father of LLMs or something like that. So I was curious about what his opinion was. And he said just, you know, the generative text models would be a tool that, like, an actual higher level of intelligence would use. But, like, what he designed is largely what the LLMs are using, that generative text transformation model and that stuff. And he's like, it's going to be hard to, like, take it to another level of, like, where it's at. And you can create tooling to, like, really funnel it. But it's still, at the end of the day, not going to be as good as what people would think. And, I mean, he's one of the people who helped pivot and get this whole industry moving forward, so that's who I trust a bit more than the people who have a financial gain.

---

<!--SEGMENT
topic: Lovable to Next.js Migration and Shipkit Templates
speakers: Brandon Hancock, Mitch, Paul Miller, Jake
keywords: Lovable, Next.js, Cursor, Vercel, git submodule, Shipkit, templates, Replit, DataButton, Vercel AI SDK, Railway, n8n, TypeScript
summary: Brandon demonstrates a workflow for migrating Lovable (Vite-based) projects to Next.js using a git submodule, allowing Cursor to reference both codebases simultaneously. Paul and Jake suggest this would make a high-demand YouTube video and connect it to the broader Shipkit template vision. Mitch asks about hosting backend workflows on Railway vs. Vercel functions.
-->

00:52:07 - Mitch
So, if you're doing the function with Supabase, then why are you still using Drizzle on top of that?

00:52:22 - Mitch
No, I'm just manually copying and pasting the Lovable [tool:Lovable] stuff, because it was like that free period, so I learned how — anyways, just copy and pasting that, adding that to a directory so that I can reference that in Cursor.

00:52:36 - Brandon Hancock
Real quick, I think this is a super valuable lesson. Actually, Mitch and I were talking about this, so I don't know if you guys saw in the last video on my workflow, but here's literally what I'm doing now to help speed up the process of going from Lovable, which is a Vite-based project, to transform it to a Next.js-based project. So what you do is you add a sub-module to your project. I just called mine Lovable. This is the full-blown project that I built in Lovable, and you can see it has all my components, all my FAQ. It has everything in here, but it's not made for Next.js. So then what I do is — you know, I'm making templates for this, but long story short is you can actually just call — so you could do like, hey, please recreate the components in — and then you can just call it out. So Lovable, Lovable components — and yeah, and then you can say now recreate them inside of my Next.js project over here. And this is what's so nice about this is you're not having to copy and paste, and all you've done is added a git sub-module, just like this. And now you can refer to it as much as you want when you're going from Lovable to Next.js, and then when you're done, just delete the sub-module, delete Lovable, hands are clean, and you're just working on your own project. ▶ So this is the easiest way I have found to port things over.

00:54:21 - Mitch
<Q>So like, let's say, currently I have a button that would just go to trigger a webhook to start an n8n [tool:n8n] workflow, but now that I'm kind of doing more code-heavy, would I just use Railway to do that, or do you recommend something else?</Q>

00:54:38 - Brandon Hancock
<A>Railway is awesome, but if it's all, like, you could also potentially just do it as an API function, or like a — yeah, depending on what that n8n workflow is doing, you could either just do it as code if it's all TypeScript. Like, if you can do it in TypeScript, you could do it in a regular API forward slash thing, whatever you're trying to do, or if you need it to be Python because you're doing some custom library stuff, yeah, you might have to do it over in Railway.</A>

00:55:10 - Mitch
Like, if it's hosted on Vercel [tool:Vercel], it would be on Vercel.

00:55:13 - Brandon Hancock
Yeah, it would just run as a function, yeah.

00:55:55 - Paul Miller
Just as a video suggestion, I know you touched on it very lightly, just do that, do this with the whole Lovable thing. There's a lot of people out there that have gone down the Lovable path that then want to transition from Lovable to, okay, let's do it in Cursor. Just a video on — I think it is in the hot spot with what's out there. Add it to your video list. I think that would be a hit.

00:12:44 - Brandon Hancock
I need to — I 100% need to do that. I was actually working literally today on the prompt to literally called Replicate Lovable. Because, like, the thing is, it's like — like, the goal is to, like, build the app that can create all apps — it's like franchising a business, you know, it's like you want to pick up something that you can just copy and paste a thousand McDonald's. In this case, it's like build infinite app ideas.

01:15:00 - Jake
Um, Tailwind, right? Tailwind is all templates. And so, if you have, like, a tech stack template — and there's a Y Combinator that's actually doing quite well, a couple of them, where it's, like, DataButton [tool:DataButton]. It's kind of the same concept. It's, like, basically, they have a tech stack. They basically have finished projects where you can change — yeah, this is it. So if you go to templates, you can kind of see how it all works. You just basically — so these are the templates, right? So it's got Firebase, Next.js, Stripe, Python.

01:15:44 - Brandon Hancock
No, I mean, that makes total sense. ▶ The goal with Shipkit is — a template for a RAG app, a chat app, an agentic app, a Crew AI agentic app, ADK — like, that's the goal, just to make, like, a hundred templates in there, so anytime you want to spin up a project, there's just something there for you guys. And I think everyone's coming to the same conclusion — AI, once it has context on something, it's phenomenal at tweaking and adjusting, but it just needs some initial constraints.

---

<!--SEGMENT
topic: Vendor Name Extraction Agent with Hybrid ML and LLM Architecture
speakers: Juan Torres, Brandon Hancock, Al Cole
keywords: CrewAI, ChatGPT Turbo, NER, spaCy, machine learning, PostgreSQL, MCP, agentic system, vendor recognition, hybrid architecture, ETL, tool calls
summary: Juan demos an MVP agentic system that extracts vendor names from transaction descriptions using a hybrid architecture combining CrewAI with a spaCy NER machine learning model. He asks how to connect the agent to a PostgreSQL database. Brandon recommends simple tool calls over a full MCP server for this use case. Al raises an important lifecycle question about whether data updates need to trigger reprocessing.
-->

00:55:33 - Juan Torres
So, I had the MVP for the Agentic system I was building for my client. It works. So, I have an Agentic system now that essentially goes through the description column, extracts the vendor name, and then places it into another column. And it's interesting. I still have to improve accuracy in terms of like what it identifies as the vendor name, but essentially I'm using a hybrid architecture in which part of the way it identifies the vendor name is through the LLMs. I'm using ChatGPT Turbo [tool:ChatGPT Turbo] as the model that I'm using for my Agentic system. I'm using CrewAI [tool:CrewAI] as a sequential system in order to go through the process. But then in a parallel form and in a synchronous form, it's using a machine learning model that essentially it's like the name identification model.

00:57:01 - Juan Torres
The Machine Learning NER model, which is Name Entity Recognition Models — so I'm choosing the spaCy [tool:spaCy] en_core_web_sm, which is a 15-megabyte machine learning model, and just using that additionally to the agentic system. I found out that it increased the accuracy of the vendor recognition significantly.

00:57:33 - Brandon Hancock
Oh, that's awesome.

00:57:34 - Juan Torres
Yeah, so this is what I'm working on right now, and I guess, like, my question to you guys is, since this — I feel like this is going to be good in terms of increasing probability of accuracy, either in AI engineering or machine learning engineering — but now the task is to implement this Agentic system into the database, the PostgreSQL database [tool:PostgreSQL]. The database that my client has, and so I'm thinking of how I'm going to generalize the operation of the Agentic system with the database, and maybe I'm thinking of using an MCP in order to do so, but if you all have any other recommendations or suggestions.

00:58:27 - Brandon Hancock
<A>The simplest answer is, like, if this is the only tool that you're creating right now, like, I would just make it a tool call. I think doing a full-blown MCP server where you have to set up the client server, like, I think that's overkill. So, I mean, just a straightforward tool that is, like, all the SQL commands you would want to make, such as, like, create, edit, or, you know, create, update, and row. So, I would — that's all I would do is just make general PostgreSQL tools that can connect to your database, make the operation, and commit the change. That's as deep as I would go, and you could always add those tools to Crew AI, you know, there's — I have a few actual YouTube videos on creating tools for Crew AI that I think you could probably just copy and paste to just enter Cursor and say, redo this, but, you know, I'm using a Postgres database.</A>

01:00:31 - Al Cole
And, Juan, this is Al. Just a question about the life cycle of the data itself. <Q>Are you doing a one-time pass through those tables and then pulling out the information? Or do you need to worry about updates and have some kind of trigger that reprocesses that row?</Q>

01:00:50 - Juan Torres
<A>I believe that it's going to be more on the first option. The second one can happen. It depends, right? A whole process of iterating — it's essentially, you're talking about an ETL process, right? If we're talking about the second option.</A>

01:01:28 - Juan Torres
Yeah, I don't think there's going to be outside factors changing the data.

01:01:33 - Brandon Hancock
Awesome question, Al, by the way. Thinking bigger. I love it. But seriously, congrats also on the big project. Once again, I'm very excited. You know, as you get to work on it more, it would be very cool at some point maybe to do like a lessons learned, or, you know, something like, hey, just did a huge client project. Here's a few things I learned.

01:02:10 - Juan Torres
I've never thought about the process of doing a hybrid system of using LLMs and machine learning models at the same time. So I think that's the thing that a lot of people will be interested about.

01:02:15 - Brandon Hancock
▶ I think that's very — yeah, I mean, I've never done that, but it makes total sense for, I think, what you're trying to do here.

---

<!--SEGMENT
topic: LinkedIn Growth Strategy and Content Marketing
speakers: AbdulShakur Abdullah, Brandon Hancock, Robert
keywords: LinkedIn, content marketing, lead magnets, cursor rules, giveaway posts, Ship 30 for 30, brand building, AI posts, engagement, algorithm, YouTube links
summary: AbdulShakur shares his growing LinkedIn profile focused on AI content. Brandon provides detailed tactical advice on LinkedIn growth: creating tangible free assets (cursor rules, templates, workflows) and using comment-triggered giveaways to maximize algorithmic reach. Robert asks about the LinkedIn algorithm penalty for external links, and Brandon recommends the "summarizer for a bigger brand" approach as a growth hack.
-->

01:02:42 - AbdulShakur Abdullah
For me, I've just — well, I didn't have as much time to actually code recently. But I have been kind of working on building up the LinkedIn profile, sharing AI information posts. And I'm trying to design a new kind of workflow system where you kind of feed an agent your brand or a link to your URL, and then it goes out to all the different agents and finds out what they think about your brand. So kind of giving you marketing information. I've seen a couple programs out there like that that do that, but they're all very expensive, and I was trying to make one cheaper so it would kind of use Open Router [tool:OpenRouter] so the person would be paying for their own calls so they could kind of decide how much they wanted.

01:03:59 - Brandon Hancock
<Q>That's awesome, what are you thinking about using tech-wise?</Q>

01:04:06 - AbdulShakur Abdullah
<A>Right now, I'm still so early in the process. I'm just thinking kind of what would — what's my inputs and outputs? Like, what would be the most valuable input-output? So I'm very early in that stage. Tech-wise, I probably would stay even closer to let me figure out what my prompts will be before I even go into tech.</A>

01:04:37 - Brandon Hancock
▶ Yeah, the second you get a little more clarity on, like, input-outputs, would be happy to, like — here's what I think how Crew AI would handle this, ADK would handle this, and LangGraph, I'd be happy to, like, walk you through, hey, here's what I think each framework would — how it could handle it, or if it should just be straight-up LLM calls.

01:05:20 - Brandon Hancock
Real quick, something I think would be super, super helpful. I talked about this in the accelerator program I just did, but like, if you want to explode — seriously, like, the easiest way to explode is like, build an asset, like, build a prop. Like, hey, I just — you know, I'm coding 24/7. Here are my 10 most valuable cursor rules that I use when building all Next.js projects. DM me "cursor" and I will send you my rules. Dude, that one post right there will, like, you'll get hundreds of comments because people are like, oh my god, like, I need to do this. So, cannot recommend, like, just creating an asset. Like, hey, here's 10 things or here's something. DM me and I'll give it to you for free. Because, like, people love free stuff and it just, like, creates a viral loop on LinkedIn because it sees people are commenting. So, it pushes it to more people. More people see it. It gets commented more.

01:07:33 - AbdulShakur Abdullah
<Q>Question is, what do I build?</Q> So I did get some lot of traction with this one post, where I kind of did a story and then linked and gave away the prompt, but I didn't say DM me to get the prompt, I just linked to a long article to get the prompt.

01:07:54 - Brandon Hancock
<A>▶ The trick is, you have to say, drop a comment down below with the word blank and I'll give it to you for free. Like, that's the cheat code.</A>

01:08:07 - Brandon Hancock
Yeah, literally repurposing that same thing would have — you would have like 10x'd that one post just by saying drop the word blank and I'll shoot you the prompt. That one change would have exploded it. So if you — Homework for the Week, man, please try that and let me know how many posts you get.

01:29:00 - Robert
<Q>So what's the best way to share a link to YouTube or a link to your video on LinkedIn? The reason I'm asking is because, say, for example, back in the days of Facebook, if you had two posts, one post had a link going externally versus the other post had a link to an internal Facebook post, the internal Facebook post would perform better because you're not taking the person off the platform. So basically, if I create a LinkedIn post and it has, like, a link to a YouTube video, and I put it within that post, will I get penalized by the LinkedIn algorithm because I'm taking somebody off of the LinkedIn platform?</Q>

01:29:42 - Brandon Hancock
<A>Yeah, I mean, I think the short answer is, like, yes, it does. It's not as beneficial to link outside of LinkedIn. However, if I was to link a YouTube video, the shortest way for growth or the quickest way for growth is you want to be a summarizer for a bigger brand. For example, anytime someone posts anything, and they're like, hey, I just watched Brandon's videos, here's the five things I learned, definitely recommend copying these as well, I repost it. When I was trying to grow a lot early, like, on X, that's all I would do is, like, a My First Million episode. Like, anytime I learned anything from anyone, I would just almost say, like, I just watched this amazing video, five biggest takeaways, and I would tag the person, just to say thank you. So, like, you're doing them a service, and then they, in return, you know, are usually more than happy to share.</A>

01:32:00 - Brandon Hancock
▶ And then, seriously, going back to earlier, what we were talking about with Abdul's LinkedIn approach, be a giver. Like, I cannot express how much of a difference that's going to make, and by giving, I'm giving assets, so, like, cursor rules was just an example, but, like, the more you can say, I just, like, I did all of this work, and if you just comment below, keyword, I'll give it to you for free, like, that's what every person wants ever.

---

<!--SEGMENT
topic: LangChain, LangGraph, LangSmith Evaluation and Postgres AI Ecosystem
speakers: Al Cole, Brandon Hancock, Marc Juretus, Bastian Venegas
keywords: LangChain, LangGraph, LangSmith, Supabase, Timescale, PGAI, EDB, Postgres, RAG, embeddings, evals, partner programs, enterprise, Andrew Ng, Interrupt conference
summary: Al asks for community feedback on LangChain/LangGraph/LangSmith based on what he saw at the Interrupt conference. Brandon shares his history with LangChain — finding value in React agents and RAG chunking but preferring direct LLM calls for simpler tasks — and says he needs to revisit LangGraph. Al then presents research into Postgres-native AI extensions (Timescale PGAI, EDB) as a potential enterprise partner ecosystem opportunity, arguing for value-based pricing over hourly rates.
-->

01:25:51 - Al Cole
It's going well. On my journey — I am still kind of — the way to think about my involvement so far has been kind of assessing where the tech stacks are, where the vendors are, and adopting similar tech stacks, and where there could potentially be opportunities from a business perspective. So it isn't, for me, pure tech at this point. It's also assessing kind of the industry out there.

01:26:26 - Al Cole
One thing I will say, last week I mentioned looking for tools that guide me in prompt building. I have a paid subscription to ChatGPT [tool:ChatGPT], so they had a dedicated applet for prompt engineering, which turned out to be helpful. It essentially structures questions to guide me on how to start the prompt, and then it ends up generating useful prompts. I last week was asking about evaluations and prompt management, and I got to LangSmith [tool:LangSmith], and it was really driven by all the examples I saw at the Interrupt Conference.

01:27:24 - Al Cole
<Q>Does anyone have any bad experiences adopting LangChain [tool:LangChain], LangGraph [tool:LangGraph], now even LangSmith as part of your stacks as you're going after some of these use cases?</Q>

01:27:53 - Brandon Hancock
<A>So I'll go super fast. So actually, my best video ever is on LangChain. Long story short, after working with every part of LangChain — so this was back in version 2, so this was almost a year ago at this point — the main things that I found valuable were the fact that you could create React agents and their RAG and chunking functionality. That was the main valuable pieces from the LangChain framework. And outside of that, when it actually came to just using everything else inside of LangChain, I was like, I came away with the approach of like, I should just make a direct LLM call, and then go to the next statement. And then over and over again, so I was like, a lot of this seemed to be overkill.</A>

01:28:40 - Brandon Hancock
Fast forward, LangGraph came out, and you know, this is where you start to get to use more agents, cycles, like, they just went a lot deeper. At first, I was like, man, this is so much work, building a graph, managing state. Like, there was just a lot of — but same as you, seeing this conference, I'm like, I need to revisit it to make sure my old biases are not still valid, because what they were showing was truly amazing with how far it's come. So I want to revisit it, but yeah, it does what it does very well, but I just have not touched on LangGraph in a minute, and I need to, so that's on me.

01:29:37 - Marc Juretus
It was better. We did it for a couple of months. And it's just, you have to do so many steps to get there. Because I remember when we did the crew — the guys were like, why didn't we just learn Crew in the first place? It was just funny, the chat was like five of them in a row, because you had — because we were doing the thing where you pull on a YouTube video, and then you rewrite it. That's what we did in LangChain, and it's so much easier in Crew.

01:30:01 - Al Cole
So with respect to Postgres and where it is in the AI evolution, I don't know if anyone's done work with Timescale [tool:Timescale], but their PGAI extension [tool:PGAI] is pretty powerful, and I sat through a webinar, they kind of walked through it. Effectively, what they're doing — and this is a strategy now of both EDB [tool:EDB], which is a Postgres company, and Timescale, which is also a Postgres company — is they're trying to bring the AI to the data. What they're trying to do is build into the database the capabilities to, in the case of a RAG use case, to automate the hosting of the models, the actual generating of the embeddings, and allowing you to query all from within SQL and within the database proper itself.

01:31:19 - Al Cole
And where I'm heading here, team, is I'm trying to figure out — and I think I shared this before — in terms of business models in the past that have worked well for me is being tied to partner programs. Because you get access to customers who are already committed to the platform, and they're looking for a little ingenuity that is added to what these larger vendors are supporting. So that's the reason I checked out EDB, which has got more than a quarter of the committers for Postgres. And they've, of course, got an enterprise platform. They're all in on AI now.

01:34:10 - Al Cole
▶ What they're trying to do is, one, keep your model and your logic close to your data, and two, keep your stack simple, and they emphasize the fact that data governance — we can lock all this down with permission models you're already comfortable with, so we can ensure the data doesn't go anywhere it shouldn't go.

01:37:00 - Brandon Hancock
▶ Out of pretty much all freelance projects that have come my way, 90% have been RAG-based, like, that is actually the most monetizable skill stack so far I'm seeing with AI, because it's like, there's an insane amount of knowledge, I need to take action on that knowledge with the help of AI. So just, like, if you're looking for where to get started with, like, a skill that could be — you could start charging for as quickly as possible, it is RAG-based.

01:38:44 - Brandon Hancock
The term I've heard recently — Nicholas Cole — he talked about something similar. And it's basically like finding the faucet. It's basically just like, where's the water coming from? Instead of looking for little puddles all over the ground with random customers, just go find the faucet to where the water's coming from in the first place. And that's literally just what you're saying — the big boys, they need help.

01:39:08 - Al Cole
And every company has got a help desk. Every single one of them has a help desk. And just some of what I've heard this team talk about, you probably could get an agent in there with access to a source and kind of drive a solid chatbot based on either structured data or something you can reach externally.

---

<!--SEGMENT
topic: Grant Proposal MVP Demo and Client Project Pricing
speakers: The Dharma House, Brandon Hancock, AbdulShakur Abdullah, Bastian Venegas, Al Cole
keywords: ADK, Google ADK, grant proposal, multi-agent system, Next.js, Vercel, Supabase, Firebase, GCS, React Markdown, structured outputs, Vercel AI SDK, Canvas, value-based pricing, managed services, multi-tenant
summary: AK (The Dharma House) demos a grant proposal generation MVP built with ADK, featuring an orchestrator, research, rendering, parser, and language-match agents. Brandon gives detailed feedback on improving the output (React Markdown rendering), adding database persistence, deploying to Vercel, and building toward a Canvas-like chat-with-document experience. Al delivers a valuable consulting lesson on value-based pricing using the "three whys" framework, and Bastian recommends showing intermediate agent progress steps to non-technical clients.
-->

01:47:48 - The Dharma House
It's been a couple of weeks since I've been on. But I've made some progress on the grant proposal MVP. I was chartered to create just a POC and I'll show it to you. First, I'd want to thank Bastian because I was stuck when we last talked and getting the artifact piece together and his support kind of helped me to click through. And then once I pushed it to Google Cloud, in GCS [tool:Google Cloud Storage], the Artifact Service, just made things much, much, much more simple.

01:52:00 - The Dharma House
Not for a POC, so I'll just kind of — and then, too, I think my question for the community is where to go with it? What I'm thinking is POC, V1, and then maybe like — or V0.5, and then V1, giving these three options as to, hey, here's where we get started, here's where I think a good next milestone is, and here's kind of what I think a solid V1 looks like.

01:52:34 - The Dharma House
But as you can see, just — here's the home page. There are two different ways to generate a proposal. One's a quick proposal, and you don't have to put in a lot of information to do that. And here's the output. And part of the reason I want you to see this page is because I think when we left off last time, one of the things that I was thinking about for V.5 or V.1 is what it would be to have a chat box on this page post-execution of the proposal itself to be able to maybe chat with the proposal and make some changes from here.

01:53:24 - The Dharma House
And, you know, as with all demos, there's about a 50% chance this will work and another 50% chance that we'll all experience a bug together. But it takes a couple of minutes to generate that proposal nonetheless as it's working. And I got a couple of agents. I have an orchestrator agent. So this is a small MAS. There's an orchestrator agent, a research agent, a rendering agent, and I think I have one or two others — one's a parser, and the other one is a language match agent. So one of the things that I think we intend to do here to make it kind of more than just spit out a document is it takes the funder info, it looks up info on the funder and even the fund itself. It takes the organizational info and it marries that information so that it really aligns the language of the grant itself — the proposal to the funder's request, to what the funder's looking for, for funding.

01:55:37 - Brandon Hancock
So, dude, seriously, first off, awesome. Like, just, like, just hats off, man. This is insane. Very cool. You've, you know, there's nothing cooler in my mind when, like, you have an idea, and then, like, you just build the dang thing, you know?

01:56:18 - Brandon Hancock
On your current — would you mind going back to the output of the proposal? Okay, so there is a — I need to find it for you real fast. But there is a tool that you can use to actually make the markdown output look so clean. Because, like, that's what you're outputting — markdown. However, you're visually just showing raw markdown. And that's not — you know, we want to actually show the real thing. ▶ So I am going to send you a snippet of code real fast in school that you can use to repurpose it. The most important thing is you want React Markdown [tool:React Markdown]. You'll see it in the code I sent you, but it'll make that table look really beautiful and not just raw markdown.

01:57:37 - The Dharma House
So I thought a lot about our last conversation, and it ate me up quite a bit. I agree with, like, I want to do stuff like this in the ranges that we talked about. I charged six grand to create this POC. It's funny — for a friend, it's in-house, so, you know, I didn't kick on it, but also, like, this is it. You know, it's bare bones. I haven't done anything to it, so that's why I'm like, when I present, I'll present it on Friday. I want to have, you know, two other sellable options that I'm like, all right, we could go here if this is your budget, or we could go here.

01:58:37 - Brandon Hancock
<Q>Have you tracked your time for this? How many hours did it take?</Q>

01:58:41 - The Dharma House
<A>I did not. I'm gonna say, just based on — I'd say I put 15, 20 hours in.</A>

01:58:53 - Brandon Hancock
I mean, that's awesome. I mean, that's like, if it's 20 hours, that's $300 an hour, so, like, that's insane, you know? ▶ So, on your level and expertise, minimum, I would recommend charging $100 — if you're doing a freelance project, like, if you were completely the one-man shop doing the project where you're having to do the client meetings, you're having to do all of it, you know, I would stick to $100, just because that would be the base case, but $100 to $200 is, like, the sweet spot for AI development, at least what I'm seeing right now.

02:00:06 - Brandon Hancock
So just, like, from what I've seen — usually on the 6K projects, there is some sort of deployment included. Usually a client would expect to be able to click around on their own on that. So do you have it set up to where you can go to, like, deploy to Vercel and click around?

02:01:40 - Brandon Hancock
So, it is insanely easy, like, you know, if you wanted to hop on a call this weekend, like, to put — like, let's just go, like, for what you're doing, Supabase, boom. Like, that would handle everything that you're trying to do from saving the artifacts in your document uploader. Like, total proposals — yeah. There's a proposal table. Like all of that should be in a table.

02:05:09 - Brandon Hancock
It is not crazy wild or hard to almost replicate the Canvas functionality of working with ChatGPT. But, like, you really could, on the right-hand side, go ahead and import a chat right there and make sure — all it would have to do is structured outputs. Stream-structured outputs, and you could pretty much recreate Canvas, where you go, like, basically the message — the output of the chat would have, like, a message and a document. The document is obviously what you see, and the chat would be — or the message would be like, okay, great, I'm implementing the feedback you just gave. Like, you could do that all with the Vercel AI SDK [tool:Vercel AI SDK], and I think that would be a huge value add.

02:09:37 - Bastian Venegas
Yeah, I was — well, first of all, congratulations to AK because this looks awesome. My other comment regarding, like, the demo is, like, besides Markdown, when I've shown, like, agentic applications to non-tech people, they kind of expect some intermediate output when you're having this big agentic system go through all the steps. ▶ They tend to appreciate if you can, like, say, step one is completed, now step two is completed, just so they know the application is not, like, hanging, because if you show this to me, I think it's great, but it can confuse people that are used to interact with AI through a chat that is more like real-time.

02:14:00 - Al Cole
From my years of running my own consulting practice, plus when I ran it with professional services for larger startups, a tactic I always used and coached my team to use is when you're talking to a prospect — a better way to position yourself is on the value of the solution that you're actually delivering, and the way you get there in identifying value is essentially ask the three whys, okay? You ask, why anything? In other words, do you really need this to be solved, right? That's the why anything. Why your custom solution, right, to address their problem, and then why now? Why now is, well, it's nice to have, but you're not going to get an economic buyer to actually write the check because it isn't compelling yet, okay? If you get alignment on those three, then the last question you really ask is, if I build this for you, how much revenue are you going to be able to generate with this solution, or how much are you going to be able to automate and therefore save you resources?

02:15:09 - Al Cole
▶ That helps you to get to a value statement that gets you away from the hours, because AK, what you didn't factor in in that great work you did was all the learning that you had done prior to building it. The hours don't match the effort there. So if you can get used to doing the three whys and thinking of it that way, it may steer you away from things that didn't need to get built, but when you really latch on to a pain point and they can quantify it, you won't have a problem figuring out a number to present to them.

02:17:01 - Al Cole
▶ So what I will typically do is if I see there's a lot of upside and there's some strategic importance to the business, I'll try to offer some type of a subscription model where I will keep maintaining this for them as their requirements evolve because it's so valuable. So quarterly check-ins, then we're reviewing if their initiatives have evolved at all, do they have new requirements? Are there new data sources I should be touching into? And then I'm doing some incremental work that I've already budgeted in because I have them buying into the higher tier.

---

<!--SEGMENT
topic: Agentic Browser Tools, Evals, Voice Agents, and Convex
speakers: Paul Miller, Brandon Hancock, Robert, Bastian Venegas, AbdulShakur Abdullah
keywords: GenSpark, agentic browser, Firecrawl, Manus AI, CSS overlay, vision model, LangChain Interrupt, evals, LLM as judge, Perplexity Labs, LiveKit, voice agent, phone number, interrupts, Convex, RAG, T3 chat
summary: Paul asks about agentic browser tools for scraping bot-protected retail sites. Brandon shares his failed attempt to build a browser agent and explains why context window overflow breaks most approaches. Bastian reveals that Manus AI uses CSS overlays and vision models to identify clickable elements. Bastian also summarizes key eval advice from the Interrupt conference (plan early, use LLM-as-judge, collect real user data). The segment closes with a demo of Bastian's real-time multimodal voice agent built with LiveKit and Gemini, and a discussion of Convex as a potential database alternative.
-->

01:09:55 - Paul Miller
I was doing some work this morning with — and I kind of wanted to ask how other people are finding it with the agentic browsers. So I was using one called GenSpark [tool:GenSpark], which — because I have quite a few retail sites I need to go into, and those retail sites have got all sorts of blocks and bot detectors and all sorts of stuff, and I need to pull data about what's going on with products and prices and promotions. [link:GenSparkAI website]

01:11:23 - Paul Miller
So it's, yeah, there's a few different people. So you can sort of do prompt-based searching and say things like, from this page, go out and create a CSV and get all of these outputs out of it. And you probably have to drill down into each of the lists down a couple of layers, pull the data, aggregate it back, and then save locally.

01:17:21 - Robert
<Q>The feature that Paul showed, why was it referred to as an agentic browser? It's very similar to the AI Studio interface, so I was just curious about why that was referred to as an agentic browser.</Q>

01:17:41 - Paul Miller
<A>It was more because you could prompt your way through the questions and interactions on the page, rather than just giving a script to say, go into that page, pull this data, do these steps. Like with the code that does that kind of thing. Because there's a number of ways you can go to Chromium and generate a script, but the problem is you've got to react with what's actually on the page, and this is where there's sort of agent tech, because OpenAI have got their tool Operator [tool:OpenAI Operator], but you've got to be in the pro plan to use that.</A>

01:18:34 - Brandon Hancock
So, a few things, Paul, so I actually tried to create a browser agent video for you guys, and I just kept hitting my head against the wall to get anything to work reliably. So I just dropped — like, I watched the Agent Development Kit team, they created a browser agent, and it works for your first three prompts, it works asterisk — like not a hundred percent. The main reason why is context. So, once you take a website, what they're doing is like, cool, grab the entire content of the website, grab the first 10,000 characters, throw it over to the agent, and let the agent look through it and pick the right element. That breaks so fast if you're working on like a big page.

01:19:49 - Brandon Hancock
And then a workaround is to make your own Firecrawl [tool:Firecrawl] equivalent to where you like convert the raw HTML to the information the agent needs. I got it to work a little bit, but it still wasn't good enough. So, I was like, man, this is just becoming too complex. Like, I understand why now there's so many like multi-million dollar startups trying to tackle this problem because I was like, oh, I'll just — give me an afternoon. I'll recreate Firecrawl. How hard can it be? And I quickly got overconfident. So I gave up.

01:21:00 - Brandon Hancock
▶ If any of you guys do find any, like, agentic browser tools that are, like, competent, please let me know, because I've been looking hard for one, because that is insanely powerful when it does work.

01:21:18 - AbdulShakur Abdullah
<Q>Have you seen the new Perplexity Labs [tool:Perplexity Labs]? Have you tried that one?</Q>

01:21:45 - AbdulShakur Abdullah
<A>If you have the paid version, it basically will run Perplexity like an agent, so — but you have to have the $20 a month version.</A>

01:22:39 - Brandon Hancock
So think, Paul, I think we answered all those questions. The one up — Bastian did just drop a cool comment on eval. I do think it's a really important conversation. If you want to, Bastian, kind of recap what you were saying on those talks, and then, Andrew, hopefully, it'll add more context to what you were asking.

01:22:50 - Bastian Venegas
Okay. There are two links in the chat, and they are both from the playlist that Brandon suggested by LangChain in Interrupt, and one is from Andrew Ng [link:Andrew Ng Interrupt 2025 talk], where in the second half of the talk, he discusses, like, in a general way, how they do evals, but basically the main advice is just planning early for evals and through the different parts of the development cycle so that you have sort of an initial approach where you do the human evals, and you can also use an LLM as a judge, but after that you need to plan how you will continue to evolve that with real user data — obviously anonymized — but you need to, like, get some insights on how the site is actually working for users.

01:23:57 - Bastian Venegas
And really quick, regarding the browser agents, a technique that Manus AI [tool:Manus AI] uses for this is that they initially do a visual assessment of the website, and they overlay this CSS that basically delimits every component of the website, so every button, every form, and all of that, and that helps the agent use its internal vision to inform the next steps. So it's subtle, but if you see a video from Manus, you will see that they do this for every website.

01:24:37 - Brandon Hancock
I mean, that makes total sense, because I think, like, the raw approach, it's so confusing to the model of, like, what do I actually click? Because when you're, like, click that, or click comment, there's 200 comments, which one do you want? So if they were just, like, oh, there's just — the main thing is, like, let's bring the context window from this to, like, oh, there's really 10 things you should be clicking on this page, rather than a thousand lines of HTML. So, no, that's very cool. ▶ I'd be very curious to see what their costs were for that, just because, like, you're having to use a vision model, vision model to structured output. Like, there's a lot more to that.

01:44:16 - Brandon Hancock
<Q>Have you gotten to try out Convex [tool:Convex] so far? I've been eyeing them, but I have not used them specifically because of RAG. I did not think they fully supported it yet.</Q>

01:44:32 - Bastian Venegas
<A>Yeah, from their docs, they do support it, but for brief context, Convex is a database, but it's also kind of an NPM package, and you can also self-host it. They seem to use SQL under the hood, but if you use them, you don't need an ORM because you just write regular TypeScript, and they wrote their database thing in Rust, so it's supposed to be really fast. Actually, I don't have any personal experience with Convex, but I have been following Theo's T3 chat [tool:T3 chat] development, and he actually migrated to Convex everything, and they had very good results in the end, and a lot of support from the Convex team. Like, really hands-on.</A>

01:45:36 - Brandon Hancock
▶ If you get to try it, specifically with the RAG functionality, I think I would 100% look at potentially switching. It's just like, in my head, I have, like, a checklist for an AI stack. It's like, I need to be able to do the chat functionality, and then from there, I need some way to save all my messages, and then I also, just with most modern AI applications, you probably do want to do RAG. And that's literally the main reason I have not gone down Convex yet is because I'm not only — when it comes to setting up the VectorStore, like, I understand if I automatically, like, have a text table, it might create the embedding, but the ability for me to actually, like, insert my own when I'm working with documents, I didn't know if it's capable of that, so that's literally the reason I've stayed away.

02:43:18 - Bastian Venegas
Well, this is just like a proof of concept of a real-time multimodal agent, because most of them go through, like, the text phase at some point, and this is just using Gemini [tool:Gemini], and leveraging its built-in Google search tool. So, I hope you can hear this.

02:43:51 - Bastian Venegas
I would like to know if some of my favorite artists will be touring South America during 2025 or 2026.

02:44:00 - Bastian Venegas
Yes, Dua Lipa is scheduled to bring her Radical Optimism tour to Latin America in late 2025, including a stop in Santiago, which is great news. As for The Weeknd, there...

02:45:05 - Bastian Venegas
Yeah, so that's mostly it, just to showcase that video was recorded, like, June 12th, and Brandon had uploaded his video just the day before, so it was kind of a fun way to show it was working.

02:45:27 - Brandon Hancock
Sebastian and I were working on a potential client project, and basically they wanted a voice agent. They had some certain requirements, such as they eventually wanted to scale to include phone numbers, and, you know, long story short, they're working to help out elderly patients that just want to have someone to chat with. And we were going to go with ADK at first, but with the requirement of having to use a phone number, Bastian found a really cool tool called LiveKit [tool:LiveKit], which basically allows you to have, like, all the benefits of code, like, you can code the entire workflows, everything, but it also had some background support or additional functionality to include integrating phone numbers at a later point.

02:46:28 - Bastian Venegas
Yeah, and the coolest thing is that I got to connect it to a phone number I purchased, just to test if it would work, and it doesn't — and the latency is pretty much the same, it's, I don't notice any difference, so that was very cool, and it's also a way to have access to AI, when you don't have any access to internet. You could literally call this from your phone, like, a regular phone, not even a mobile phone. So that's a cool use case.

02:47:03 - Brandon Hancock
<Q>And final question, I can't remember, so it did have interrupts or it didn't have interrupts?</Q>

02:47:08 - Bastian Venegas
<A>It does have interrupts, yeah.</A>

02:47:11 - Brandon Hancock
▶ And just a quick background, interrupts are the way — interrupt across all, like your OpenAI models, Google models — interrupt is the word and the phrase for all voice agents for it to detect the person's trying to speak over the agent and the agent needs to stop. So that's insanely important when trying to build anything real-life for voice agents is having interrupts.

---

<!--SEGMENT
topic: Session Wrap-Up, RAG Use Cases, ADK vs LangGraph, and AI Model Subscriptions
speakers: Brandon Hancock, Alex, The Dharma House, Robert, Neel More, Bastian Venegas, Al Cole
keywords: RAG use cases, fire chief documentation, SOAP format, ADK, LangGraph, global state, custom agents, GPT-4.5, Gemini, Grok, Cursor, model subscriptions, Context7, ADK documentation, portfolio building
summary: Brandon describes two concrete RAG client projects — a fire department documentation tool and a large-scale blog search engine — illustrating the most monetizable AI skill stack. The group discusses ADK vs. LangGraph tradeoffs, with Brandon noting ADK's strong global state management but lack of pure code steps as its main weakness. Robert asks about AI model subscriptions, and Brandon recommends GPT-4.5 for writing, Gemini for Google Workspace integration, and Cursor for development. Neel demos a machine learning pipeline agent with human-in-the-loop, and the group confirms Context7 has ADK documentation.
-->

01:40:35 - Alex
<Q>Brandon, just a quick question. If you don't mind sharing, what is the pain point of the RAG projects that you have sold? What is the pain point that you're solving with those RAG applications?</Q>

01:40:49 - Brandon Hancock
<A>Yeah, so first one, you know, the one for the Fire Chief. The short answer is they have to fill out documents every time they go to handle an emergency response. They have to do it in a particular format called SOAP, which is like, what was the situation? What was the plan? There's so many things I have to fill up. So in the past, you know, they would have to like, shoot, what did I do earlier today? Okay, so I walked in, lady unconscious, her face was like half not there or whatever, from like a stroke. And they have to like recall everything they did. They have to manually type it out, the vitals. They have to do so much work. Then after that, they're in their head — they just have like a bullet point, like that's the memory. Okay. Well, part two of that is whenever they go to submit this document, they have to hit certain codes or certain things in order to like properly bill.</A>

01:41:56 - Brandon Hancock
So long story short, what the RAG agent would do is it would take in the person's like brain dump of like what happened. It would understand the format it was trying to do. Based on all the keywords that they said, it would make a RAG request to two different data stores. One was to say, oh, you gave ibuprofen to a person with a stroke? Well, looking at emergency medical procedures, it looks like — you know, I'm also butchering this — but, like, it looks like this dosage is probably what you gave her. So by giving — looking at dosages and procedures, it could make their documents way more prescriptive so that the billing, like, insurance could go, oh, yeah, you gave ibuprofen, you administered this procedure. Like, we now know why we need to cover this charge. ▶ So it's looking at both sources. So really just — they can now put a bullet point list in that takes 10 seconds just talking to the computer and it generates an entire report, which, you know, usually takes 30 minutes to write. So literally two minutes instead of 30.

01:42:47 - Brandon Hancock
Second one is more just ideation. So people just want to browse large sums of data. Like, so imagine — it's almost like having your own internal Google at this point. Some people actually don't just want to get an answer back immediately. They're like, hey, I have a log repository from every creator I can think of. I have 300,000 blogs. I'm trying to now go off and put together my own small report on the best practices for, you know, raising a seed round for a company. Well, what they want to do actually is not just get back the first three results. They want to look at every blog ever that touched on that topic and almost like scroll through their own little search engine.

01:43:37 - Brandon Hancock
▶ So, yeah, so those are the two main cases I've seen very, very recently. So hopefully that's helpful. So yeah, RAG for the win on both of those, VectorStores specifically.

02:19:43 - The Dharma House
I have a version that's kind of Google-native, so I've worked on an agent that's just — that taps into the entire Google workspace, you know, plays with all of the Google tools and also has context. And I'm still kind of working on that — on the context and cache within the Google ADK system of an environment. But, you know, I still like it more than LangChain. And it was Brandon's first LangChain video that got me going down the LangChain path last December. But as I'm working in ADK, I feel like maybe the best stack is LangGraph plus Google ADK. That's — I haven't, like, added a graph to it, but I think that might be the magic stack for me, so more to come on that, guys.

02:21:12 - Brandon Hancock
So, quick to piggyback off what AK just said real fast — the main reason that would force me just out of the gate to go LangGraph is if I was working in some sort — like, a graph, obviously, like, to where, like, there was a certain cycle of events that had to happen from left to right, and there 100% had to be an atomic action that had to be performed by code. What I mean by that, if I have to, like, do something with my bank, if I have to do something with, like, an email, where I don't want to accidentally have an agent trigger that twice, that is the main reason I would go with LangGraph right now. ▶ The biggest downfall right now I see in ADK is the inability to do a code step. That's the main — that's the biggest downfall I see of ADK right now.

02:23:15 - Brandon Hancock
The state management inside of ADK — beautiful, beautiful. Like, I mean, I'll show you the background real fast. Like, at Crew AI, like, that was one of the biggest things that, like, I wanted to make easy, was state management. Because, like, in flows, like, I helped build all the state management. And, like, it is insanely important. So when I saw how ADK was doing it, it instantly got all the warm and fuzzies. Because I was like, they did it right. ▶ With the way they're doing it — because it has to be global, or else it's just not usable on bigger projects.

02:25:27 - Brandon Hancock
So y'all are going to laugh. I actually do pay the $200 for OpenAI [tool:OpenAI], strictly for GPT-4.5 [tool:GPT-4.5]. I use that to write everything. It's the best, from what I've seen — it is the best writing model. So every time I'm making presentations, as I'm, like, writing the course right now, like, it is, by far, with its context window and its ability to, like, actually just write, like a human, it is the best one, by far, for writing.

02:26:03 - Brandon Hancock
And then I literally have subscriptions to everything else. The only one I don't is I don't have a subscription to Claude Code. So, I mean, I have Super Grok [tool:Grok], I have Gemini [tool:Gemini]. Like, I have every single one of them, just because I use them for different things. I help — I work with some, like, local businesses, and doing anything with a local business, Gemini is going to be the default AI for small to medium businesses, in my opinion. Quickly because it can, you know, through Gemini, like, when you're over in AI Studio, it can instantly access all of their Google Drive documents. So, it's 10 times — it's, like, with OpenAI, great. It can do everything. It has projects. It has everything, but you're siloed. Yes, you can do, you know, you can search the web, but the thing that allows businesses to unlock an insane amount of value is their email, their calendar, and their Google Drive. Because that's how a lot of small businesses run.

02:33:43 - Neel More
Hey, I'm doing good. I was trying to share my screen. Just wanted to give a demo of the app. I was creating — okay, so this is like an app for, like, you will be running your machine learning pipeline, but before that you get the data, right? And on top of that data, I was doing the data analysis, as well as I was doing the data drift. So now, for example, this is my user prompt, okay, and this is the data — so which is had given to check around whether to do the analysis. And here, the coordinator comes as an agent for us, and it checks around, okay, no data drift is there, and whether there are duplicate columns, but as this is a sample data, you will see that there won't be any changes, and I'm giving the same file, and then it asks a human loop in this, whether you want to run your machine learning pipeline or not, and the reason is like to check whether the churning in this case, so let's say if I say yes, now only our agent will run the pipeline, but at the end, it will also get the predictions of it, like what was the outcome of it. And I wanted to create a loop event so that if the score is less, then it will go and rerun the pipeline with some hyperparameter tuning.

02:35:32 - Neel More
And so while doing this thing, I was learning a lot. So I was doing the naming mistakes, like the business mistake. I was using Cursor AI, the ChatGPT to create everything. But as the Gemini model also, right, it doesn't know the latest documentation. And it was creating their own wrappers and the patterns on top of it. And what you mentioned today, the Context 7, that's the next step I was going to try. So good you mentioned about that.

02:36:07 - Neel More
<Q>Have you used the custom agents anywhere so far? Do you got any example? Or even if you got a similar example where the custom agents can be applicable, that would be great to know.</Q>

02:36:19 - Brandon Hancock
<A>So I have not used ADK custom agents yet, but just a quick recap for everybody. Basically, what custom agents do is there's a core agent life cycle, and within a custom agent, you basically get to tap into the life cycle of an agent and, you know, do things differently. For example, if you potentially needed to do some sort of authentication is the usual example. There's a step in there to where you could have the agent authenticate before it proceeds with doing a certain task. So that's the usual example you'll see for custom agents. But yeah, short answer is no. Usually it's like the order of operations, like to solve the problem — can we just be fancy with the prompt to get it to work? The answer is no, okay, well then the usual next step I will look at is to work with the callbacks that are provided. The agent callback, tool callback, or the model callback — 90% of the time, I can get away with like, oh, I actually, before this agent kicks off, I'll update the before agent callback, I'll trigger that, alter whatever I need to do, update state, make a change, upload information, download information, whatever I need to do, I'll do that in the before agent callback. And that's 90% of the time, like you can get away with just doing that.</A>

02:40:47 - Brandon Hancock
I'm going to check real fast, too. I'm going to share my screen. Use Context 7. To the Python, the Google ADK library — and we'll see if it does it.

02:41:14 - Brandon Hancock
So, yeah, this is Context 7 in action. It's looking up the library ID. I think it found it, maybe? Oh, my gosh, it did. Yeah, that's cool, guys. It does it. It has it.

02:41:37 - Brandon Hancock
▶ So, yeah, it has everything. So, I'm hoping this is the latest version. I'm trying to figure out — what version of the Python ADK docs do you have access to in Context 7? I just want to make sure it's the latest one just because, like, they did cut that new version.

02:42:22 - Brandon Hancock
Context 7, for the win.

02:47:41 - Brandon Hancock
Okay, guys. Well, this was seriously insane call. Love to see all the cool things that you're working on. I'll post the recording — usually takes like a few minutes to process, but I'll post it here a little bit later tonight. But yeah, always love looking forward to Tuesdays to see all of you. All the cool things you're working on, and I will keep you posted on, first off, the new — speaking of interrupts — the LangChain Interrupt Conference. I'll hopefully be working on that video tomorrow. Outside of that, I will keep you posted when we lock down the Dan Martell live guest session, probably not next Tuesday, but the one after — July 1st. And I will also keep you guys posted as I work on the Shipkit, which will include a ton of templates, courses, and everything to help you guys launch AI applications.

---

=== UNRESOLVED SPEAKERS ===

The following speakers appeared in the transcript but were not found in the SPEAKER_ALIASES map provided (the map context block was empty/unpopulated at processing time):

- **Andrew Nanton** — pre-call participant, discusses RAG, chunking, document processing app
- **alexrojas** — building legal RAG app with Next.js and Supabase
- **Brandon Hancock** — call host, AI developer/educator
- **Marc Juretus** — community member, working on ADK agents
- **AbdulShakur Abdullah** — community member, building LinkedIn presence and brand monitoring tool
- **Al Cole** — community member, enterprise/consulting background, researching LangChain and Postgres AI ecosystem
- **Mitch** — community member, building app with Lovable/Next.js
- **Bastian Venegas** — community member, advanced technical contributor, built voice agent with LiveKit
- **Juan Torres** — community member, built vendor extraction agentic system for client
- **Paul Miller** — community member, New Zealand/Australia SaaS business, researching agentic browsers
- **Jake** — community member, discussed template libraries and DataButton
- **The Dharma House** — community member (AK), built grant proposal MVP
- **Aleksandr** — community member, Telegram bot with YouTube download functionality
- **Robert** — community member, learning ADK, asking about LinkedIn growth
- **Neel More** — community member, built ML pipeline agent with human-in-the-loop
- **Ty Wells** — brief comment on RPC terminology
- **Alex** — asked about RAG use cases (distinct from alexrojas)