00:00:59 - Paul Miller
Thank Good morning, guys.

00:01:33 - Paul Miller
Afternoon.

00:01:34 - Paul Miller
Evening.

00:01:38 - Bastian Venegas
Hey, how are you doing, Paul?

00:01:40 - Paul Miller
Good, good.

00:01:41 - Paul Miller
I'm the host today.

00:01:43 - Andrew Nanton
Okay.

00:01:45 - Andrew Nanton
Great.

00:01:46 - Bastian Venegas
I was going to do that, actually.

00:01:49 - Paul Miller
So can I ask the two of you to, we'll do the question thing first, but if you can be the wisdom.

00:01:59 - Paul Miller
Awesome.

00:02:04 - Bastian Venegas
I'm happy to help if there's anything I can make up.

00:02:08 - Paul Miller
I think between Andrew and yourself, I think we should be able to cover off the questions, and then we can do the go-around.

00:02:20 - Andrew Nanton
I feel like my knowledge is pretty narrow, but I'm happy to jump in if it's something I can help with.

00:02:32 - Bastian Venegas
Hey, Mark.

00:02:34 - Bastian Venegas
Hey, Mark.

00:02:35 - Marc Juretus
Hey, Bastian, Paul, Andrew.

00:02:38 - Marc Juretus
How are you?

00:02:40 - Andrew Nanton
Just peachy, man.

00:02:41 - Marc Juretus
Another day in the books so far, work-wise.

00:02:44 - Marc Juretus
How about you?

00:02:46 - Andrew Nanton
Can't complain.

00:02:49 - Paul Miller
Good, good.

00:02:51 - Paul Miller
Hello, Patrick.

00:04:05 - Paul Miller
All right.

00:04:32 - Patrick Chouinard
Anyone had a chance to try a new OpenAI open source model today?

00:04:38 - Paul Miller
I've downloaded it.

00:04:40 - Paul Miller
I haven't been able to do benchmarks or anything like that.

00:04:44 - Paul Miller
It looks pretty good, actually.

00:04:49 - Andrew Nanton
I fired it up in LM Studio and was pretty impressed, just dropping in a few really random questions.

00:04:56 - Andrew Nanton
So, I mean, it's nothing like a comprehensive kicking.

00:04:59 - Andrew Nanton
But, I mean, for something that runs in such a small amount of memory, I was awfully impressed.

00:05:07 - Patrick Chouinard
Yeah, me too, because, I mean, I'm running on decent hardware, but certainly not cutting edge.

00:05:15 - Patrick Chouinard
I ran it on two GTX 1080 Ti, so not bad in terms of ERAM, but pretty old in terms of CUDA core.

00:05:24 - Patrick Chouinard
And it still ran at, what, 33 token per second for a 20B model, fully in VRAM.

00:05:37 - Patrick Chouinard
Pretty impressed.

00:05:38 - Patrick Chouinard
And decent context window, too.

00:05:41 - Paul Miller
128,000 tokens, which seems pretty good.

00:05:46 - Patrick Chouinard
Sadly, do not have enough VRAM for 128,000 tokens, but still.

00:05:54 - Patrick Chouinard
Tool call ran pretty well.

00:05:57 - Patrick Chouinard
I've tried it with the Perplexity MCP server.

00:06:00 - Patrick Chouinard
And no issues.

00:06:02 - Patrick Chouinard
So yeah, pretty impressed right now.

00:06:06 - Paul Miller
Right.

00:06:07 - Paul Miller
So should we get started?

00:06:08 - Paul Miller
So guys, welcome.

00:06:10 - Paul Miller
Brandon is on vacation.

00:06:13 - Paul Miller
So he's asked me to host this morning, well, this morning, my time, this afternoon, US time, and the evening in Europe.

00:06:27 - Paul Miller
So welcome, welcome, everybody.

00:06:30 - Paul Miller
I think we'll, I've got a few people that have offered to be there for the initial question round.

00:06:40 - Paul Miller
So for those that haven't been on the call before, welcome.

00:06:46 - Paul Miller
What we'll do is we'll get everyone to, if you've got any questions you want to post, Bastion, Andrew, have said that they'll step up to help.

00:07:00 - Paul Miller
Let answer some of the technical questions, and then we can sort of do a round-robin, see how everyone's going.

00:07:07 - Paul Miller
I'm really excited to see what people have thought about the new models that have come out today.

00:07:15 - Paul Miller
I think it's not just OpenAI, there's some other ones that are about to come out as well, so I'm pretty excited to talk about that and see what people have found and what everyone's up to this week.

00:07:28 - Paul Miller
So, do you want to post the questions in the chat, and then let's do the round-robin after that.

00:07:43 - Paul Miller
Has anyone got any specific questions, or shall we jump on the go-round?

00:07:54 - Paul Miller
Okay, I'm not seeing anything specifically, what's happening here?

00:08:20 - Paul Miller
Okay, so let's do the go-around.

00:08:24 - Paul Miller
Oh, sorry, having some technical issues at this end.

00:08:28 - Paul Miller
Not normally seeing the...

00:08:33 - Paul Miller
Okay, Andrew, do you want to start?

00:08:36 - Paul Miller
Do you want to start today?

00:08:40 - Andrew Nanton
Sure, so I'm seeing this first question here.

00:08:43 - Andrew Nanton
Has anyone tested Opus 4.1 yet?

00:08:46 - Andrew Nanton
I tested it a little bit in Claude Code, and then with some other more freeform kind of stuff.

00:08:52 - Andrew Nanton
It seems like an incremental improvement.

00:08:57 - Andrew Nanton
At 4.1 seems pretty...

00:09:00 - Andrew Nanton
Pretty true to its word in that it seems like maybe a little bit better, and that's what I'm seeing in the model cards.

00:09:07 - Andrew Nanton
It looked like there was a step backward in one of the evals.

00:09:11 - Andrew Nanton
I think it was like booking airline tickets or something like that.

00:09:14 - Andrew Nanton
went from like 56.9 to 56 or something, but it looked like a couple percentage improvements across almost every different kind of task, which lines up to what I'm seeing.

00:09:27 - Andrew Nanton
But obviously, it's only been a couple of days, and that's really anecdotal.

00:09:34 - Paul Miller
Cool.

00:09:38 - Paul Miller
Has anyone sort of seen with Opal, anyone got any good use cases out of Opal yet?

00:09:46 - Paul Miller
So that's the Google model that you can create agents with prompting.

00:09:54 - Paul Miller
What's people seeing around that?

00:09:57 - Paul Miller
Bastian, have you had a play?

00:10:01 - Bastian Venegas
No, I haven't used it yet.

00:10:03 - Bastian Venegas
I played with a similar tool that's by a platform that's used to make like drawings and schemes.

00:10:12 - Bastian Venegas
It's similar to Excalibur, but it's called TLDraw, like T-L-D-R-Draw, and they have a new like free thing you can try.

00:10:24 - Bastian Venegas
I will try to search for the link, but basically Google gave them a bunch of credits for Gemini, and they do a thing that's very similar to what Opal is trying to do, where you kind of have like these diagrams, and you have, for example, or just give me a second, and I will pull it up.

00:10:43 - Bastian Venegas
You can continue.

00:10:45 - Bastian Venegas
Maybe someone has actually used Opal.

00:10:50 - Paul Miller
Anyone that's used Opal?

00:10:54 - Paul Miller
I've had a play myself.

00:10:57 - Paul Miller
I used it.

00:10:59 - AbdulShakur Abdullah
That's why I

00:11:00 - AbdulShakur Abdullah
I just asking, because I wasn't able to edit very well after the initial kind of one-shot prompt where it makes the big flow, going in and trying to edit part of the flow to add new logic.

00:11:14 - AbdulShakur Abdullah
It just didn't work very well for me.

00:11:16 - AbdulShakur Abdullah
So I wanted to see if anyone had any tips on fixing it.

00:11:23 - Paul Miller
Yeah, well, I just found it really good for creating really good prompts.

00:11:28 - Paul Miller
I don't know what's in the back end of the model, but in terms of the engine, that's been pretty good.

00:11:36 - AbdulShakur Abdullah
I have been using a new prompt to make prompts, which has been pretty strong for me today.

00:11:44 - AbdulShakur Abdullah
I'll drop it in the chat and share that.

00:11:47 - AbdulShakur Abdullah
Good.

00:11:48 - Paul Miller
Thank you.

00:11:50 - Paul Miller
Okay, so thanks, Bastian.

00:11:54 - Paul Miller
Anyone using code swarms?

00:12:02 - Jake Maymar
Not yet.

00:12:03 - Jake Maymar
Yeah, it's interesting.

00:12:04 - Jake Maymar
So Claude, they're doing a lot of rate limiting if you're using Claude.

00:12:09 - Jake Maymar
I'm sure you've seen that, Andrew.

00:12:13 - Jake Maymar
And it's really interesting.

00:12:15 - Jake Maymar
If you're using Claude on, like, Open Router, if you're using Claude on really other platforms, not...

00:12:26 - Jake Maymar
I think even Cursor, I've seen some rate limiting.

00:12:29 - Jake Maymar
But smaller platforms, there's, like, really heavy rate limiting.

00:12:34 - Jake Maymar
I'm kind of curious if anyone else is seeing that.

00:12:41 - Jake Maymar
No.

00:12:43 - Jake Maymar
And the other question is, well, I guess, it...

00:12:49 - Jake Maymar
Andrew, are you still using Claude?

00:12:51 - Jake Maymar
Claude code?

00:12:52 - Jake Maymar
I am.

00:12:53 - Andrew Nanton
Yeah.

00:12:53 - Andrew Nanton
Yeah.

00:12:54 - Andrew Nanton
I've found that to be the most reliable for me.

00:12:58 - Andrew Nanton
But that also, I think, says a lot.

00:13:00 - Andrew Nanton
I about my workflow, rather than it being the best possible choice, because I'm generally also doing other stuff in the background, so having something that's pretty autonomous is really useful for me.

00:13:13 - Andrew Nanton
But, yeah, I am noticing the same thing that everyone else is noticing, which is that even though it's improving, it's really hard to get it to stay on the rails.

00:13:24 - Andrew Nanton
It likes to just start to jump into doing all kinds of nonsense pretty quickly.

00:13:30 - Jake Maymar
Yeah, yeah, like it wrote, like I was just trying to debug something, and it wrote like seven debuggers on top of each other for no reason at all.

00:13:44 - Jake Maymar
And I was like, why are you doing this?

00:13:46 - Jake Maymar
And then it couldn't see the code, and I was like, just point out pieces of code, and it couldn't do it.

00:13:52 - Jake Maymar
And I was like, this is so weird.

00:13:54 - Jake Maymar
So, yeah, I'm having some strange issues with Claude Code, Claude.

00:14:00 - Jake Maymar
In general, so.

00:14:01 - Jake Maymar
I've had a similar experience.

00:14:04 - Sam
I don't know, like, because I'm using Windows, I have to create that, like, Linux, and then, and Decord.

00:14:10 - Sam
And sometimes I feel like, in that session, we'll call it, if it gets in the wrong, if it starts on the wrong track, you might as well just, like, throw in the towel and almost, like, restart the whole thing.

00:14:21 - Jake Maymar
That makes a lot of sense, because there was an update.

00:14:25 - Jake Maymar
So, I'm on Windows, but also, I have a dual boot to Linux, and it's such a pain to switch, because I have all my stuff on Windows, but maybe that's the issue.

00:14:39 - Jake Maymar
Because there was, like, an update, you know how Windows always does updates, it did an update to WSL, and it broke Docker, and it broke a whole bunch of different things, so maybe that's it.

00:14:50 - Jake Maymar
Thank you.

00:14:52 - Sam
Because I had a funny experience, I think it was yesterday, I was, I couldn't get the environment variables to load, and then I was like, I think I know this.

00:15:00 - Sam
Solution, and then I was like, hey, this isn't working, and then it wrote like a custom script to like pull environment variables, and I was like, why don't you just use the library to do it, and it's like, oh, okay.

00:15:14 - Sam
You know, what is it, the python dot, you know, dot TV, that stuff, so yeah, you do have to kind of shepherd it a bit still.

00:15:24 - Paul Miller
So, with the rate limit changes in Claude Code, I know, I understand that those new rate limits kick in, is it at the end of this month, or they come in straight away?

00:15:40 - Paul Miller
Are people finding that they're going to use up the limits if you're on a max plan or the $100 plan?

00:15:51 - Bastian Venegas
Officially, they will update their limits in, I think, at the end of the month, like 27th, maybe.

00:16:02 - Paul Miller
Okay.

00:16:03 - Paul Miller
Did we work out a way to understand how much we're using at the moment?

00:16:11 - Paul Miller
Because I know on the call last week, we talked about it was not clear to understand what the burn rate is.

00:16:20 - Jake Maymar
So that was the thing is that used to be really clear.

00:16:23 - Jake Maymar
Like you used to be able to look at the dashboard, the cursor dashboard.

00:16:26 - Jake Maymar
No, it said you had like, you know, 400 or 300 or 200 left.

00:16:32 - Jake Maymar
And now it's not clear at all.

00:16:35 - Jake Maymar
And 20 bucks, I agree with Bastian, lasts for like four days, if that.

00:16:41 - Jake Maymar
And they're just using, and I've tried Gemini, like Gemini 2.5.

00:16:48 - Jake Maymar
Before this update, I could run it for like months and there was no issue.

00:16:52 - Jake Maymar
Now, if I'm running any model, it seems like it lasts for about like four days.

00:16:57 - Jake Maymar
And then that's the end of my subscription.

00:17:00 - Jake Maymar
So I'm curious if anyone's using Max.

00:17:05 - Paul Miller
Abdul?

00:17:06 - Paul Miller
I was just saying, I think our free lunch is over.

00:17:09 - Jake Maymar
Yeah.

00:17:10 - Jake Maymar
Yeah.

00:17:11 - Al Cole
Someone was showing me a breakdown.

00:17:14 - Al Cole
I don't know how they got it, but it was what we were getting versus what they were paying.

00:17:20 - Al Cole
And it reminded me a lot of those early days of Uber where a lot of those rides were fairly inexpensive.

00:17:25 - Al Cole
And there was a Delta.

00:17:27 - Al Cole
They are trying to bring it at least to break even, which is raising all of our fees.

00:17:36 - Al Cole
And so I don't know if this team is running multiple agents in the same session, but I find that with the, is it maxed $100 a month with CloudCode?

00:17:47 - Al Cole
That seems to be okay with linear development for me.

00:17:51 - Al Cole
I can get a good day of development out of it, but I'm not running multiple agents at the same time.

00:17:56 - Al Cole
I tend to pay attention to what it's doing.

00:17:58 - Al Cole
And as mentioned.

00:18:00 - Al Cole
mentioned earlier, it will occasionally just completely take a detour, and I've got to jump in and, you know, get it back on track.

00:18:10 - Andrew Nanton
I mean, one rule of thumb that I read is, you know, don't tell it more than twice that it's, you know, taken a wrong turn.

00:18:18 - Andrew Nanton
You just, you got to just zero out the context window and start over.

00:18:24 - Al Cole
Oh, interesting.

00:18:25 - Al Cole
Okay.

00:18:25 - Al Cole
Yeah.

00:18:26 - Andrew Nanton
I mean, and that has been my, anecdotally, also, that's been my experience.

00:18:29 - Andrew Nanton
Like, if it starts, if it starts trying to do weird stuff, and you're trying to, like, get it back on track, you're way better off just, you know what, just shut down this session, start a new session.

00:18:40 - Andrew Nanton
Here's what I'm doing.

00:18:41 - Andrew Nanton
Here's, here's my design document here.

00:18:44 - Andrew Nanton
Like, because that's the other thing I do is I keep a design document, which is, like, overall what I'm doing with, like, what is this supposed to be, and what are all the different parts.

00:18:53 - Andrew Nanton
Then I keep another file that is the implementation plan, which is, you know, what are the next few steps of what we're

00:19:00 - Andrew Nanton
doing in this project.

00:19:01 - Andrew Nanton
And I have it delete out the stuff as we go in this implementation plan and add it to a development log file.

00:19:09 - Andrew Nanton
But I use the planning mode way more than I let it write code.

00:19:16 - Andrew Nanton
And I always be sure, I get really good results from saying, ask me any necessary clarifying questions, because otherwise it just starts making dumb assumptions that have me tearing my hair out.

00:19:28 - Andrew Nanton
And sometimes it asks me, you know, 50 follow up questions.

00:19:31 - Andrew Nanton
But honestly, if I can't answer those questions, I deserve what I get out of that.

00:19:35 - Andrew Nanton
And so, you know, just saying like, okay, let's plan.

00:19:38 - Andrew Nanton
I want to do this.

00:19:40 - Andrew Nanton
Okay, tell me what your plan is.

00:19:42 - Andrew Nanton
And you can keep it.

00:19:43 - Andrew Nanton
It's like a shift tab to keep it in planning mode and cloud code.

00:19:47 - Andrew Nanton
And so like, I don't, I don't take planning mode off until I'm 100% happy with it.

00:19:51 - Andrew Nanton
And even then, I don't just let it code.

00:19:54 - Andrew Nanton
I say, okay, write the plan that you've created an implementation plan file.

00:20:00 - Andrew Nanton
That you're going to now follow.

00:20:01 - Andrew Nanton
And so, and then, you know, I'll usually just clear out the context window or at least compact it and say, read implementation plan, you know, do the at mention, read at implementation plan dot markdown.

00:20:12 - Andrew Nanton
Tell me what your next three steps are.

00:20:15 - Andrew Nanton
Let me make sure that those look reasonable to me, then go nuts.

00:20:19 - Andrew Nanton
So I spend a ton of time in the planning phase, and really push it to ask me clarifying questions, because a lot of times they're questions I haven't really thought through that carefully yet.

00:20:32 - Andrew Nanton
And it's perfectly good if you say, well, I don't know, give me three suggestions, because I don't really know what might be the best way to go.

00:20:38 - Andrew Nanton
But then, you know, once you pick one, I've found that that workflow is very effective.

00:20:44 - Al Cole
Super.

00:20:45 - Andrew Nanton
And you'll burn through way, way fewer tokens by, like, the plan mode, know, that's not a massive amount of tokens, you know, that you're, and you're really just trying to, like, figure out, hey, you know, let's come up with a game plan that we both agree with that seems sane and reasonable.

00:21:00 - Andrew Nanton
And I do a lot of, here is the documentation for this feature that I want you to use when you're implementing this.

00:21:06 - Andrew Nanton
Or, you know, here's the URL.

00:21:10 - Andrew Nanton
Use context seven to get the documentation and tell me, you know, what's the most idiomatic way to do this?

00:21:16 - Andrew Nanton
Are you sure we're not duplicating any functionality that already exists in this library, et cetera?

00:21:23 - Andrew Nanton
And anyway, that's my.

00:21:25 - Al Cole
A quick question on context seven.

00:21:27 - Al Cole
I looked at it more closely today.

00:21:29 - Al Cole
I was looking at Redis, by the way, I have a background with Redis.

00:21:32 - Al Cole
And I found a lot of operations deployment information in there versus I was thinking it was going to be straight developer oriented.

00:21:44 - Al Cole
Is that pretty common that context seven will span deployment information, maybe API related information?

00:21:55 - Andrew Nanton
I mean, I don't know what other people's experience has been, but for me, it seems to.

00:21:59 - Andrew Nanton
It's good.

00:21:59 - Andrew Nanton
.

00:22:00 - Andrew Nanton
Pretty carefully only pull official docs from existing libraries, but maybe that's just what I'm asking it to do.

00:22:09 - Bastian Venegas
Maybe I'm just not asking enough deployment-related stuff.

00:22:11 - Bastian Venegas
don't know.

00:22:12 - Bastian Venegas
I think actually what it does is it crawls the GitHub repository, and then it builds its own documentation.

00:22:21 - Bastian Venegas
Because if you try to, for example, I don't remember what library it was, but I was searching for something in context 7.

00:22:28 - Bastian Venegas
Oh, yeah, it was Convex, the database.

00:22:32 - Bastian Venegas
So they had it like one month ago, and I wanted to see if it was, if I could use the documents, the documentation, I mean, from the web, because they even have an LLM.txt, so it would make sense to use that.

00:22:49 - Bastian Venegas
So I fed that and the documentation page, like the traditional URL, and it just won't let you, because it will always ask for a GitHub repo, and that's what it will...

00:22:59 - Bastian Venegas
Yeah, will for a GitHub repo.

00:22:59 - Bastian Venegas
Thank

00:23:00 - Bastian Venegas
See if it needs updating or not.

00:23:03 - Jake Maymar
Okay.

00:23:04 - Jake Maymar
So, Bastian, on that, are you seeing any slowdown?

00:23:08 - Jake Maymar
I've been using some MCPs, and I started using the Convex MCP just in Cloud Desktop, and it does weird stuff where it just slows down.

00:23:17 - Jake Maymar
Are you seeing that, or is that, you know, I'm sure something's really wrong with my machine at this point.

00:23:23 - Bastian Venegas
No, not really, and it shouldn't.

00:23:25 - Bastian Venegas
I mean, if you run it, like, locally, the MCP, instead of connecting through the internet, it shouldn't be an issue.

00:23:33 - Bastian Venegas
Yeah, it's running locally.

00:23:35 - Jake Maymar
Let me double check that.

00:23:35 - Bastian Venegas
It shouldn't be a bottleneck if you're doing it locally, just, like, to basically route your HTTP request.

00:23:44 - Jake Maymar
Yeah, I'll double check that.

00:23:46 - Jake Maymar
Maybe something weird got wonky or something.

00:23:49 - Jake Maymar
Great point.

00:23:51 - Paul Miller
Right, well, let's switch to the update from everyone I've got on my list.

00:23:59 - Paul Miller
check that.

00:24:00 - Paul Miller
The first four being Andrew, Jake, Adam, Al, and then I'll get the next four.

00:24:09 - Paul Miller
Andrew, do you want to give us an update on how your week has gone and what your AI news is?

00:24:18 - Andrew Nanton
Sure.

00:24:19 - Andrew Nanton
I'll be real quick because it's been fairly uneventful with the other stuff going on in my other job.

00:24:26 - Andrew Nanton
But I have continued to crack away at Llama Index, which if you have RAG-related stuff to do, I think is definitely worth a look.

00:24:38 - Andrew Nanton
It's large and messy, and it changes really fast, and so sometimes that can be pretty frustrating.

00:24:44 - Andrew Nanton
And the TypeScript implementation is significantly behind the Python implementation.

00:24:50 - Andrew Nanton
But they've added some interesting stuff.

00:24:52 - Andrew Nanton
They have a few interesting starter projects as well, like a Notebook LM sort of equivalent functionality.

00:24:59 - Andrew Nanton
don't know no.

00:24:59 - Andrew Nanton
Why?

00:25:00 - Andrew Nanton
And they also have like a RAG as MCP, like pretty easy connection that I haven't really had a chance to play with very much yet.

00:25:08 - Andrew Nanton
But the idea is, you know, it will ingest all the documents that you pointed at, and then it will function.

00:25:13 - Andrew Nanton
You can use that MCP to access all of the documents that you've stuffed into the RAG.

00:25:19 - Andrew Nanton
So I've been pretty impressed with it.

00:25:22 - Andrew Nanton
What I've been working on is GraphRAG stuff using Kuzu, which is, I talked about maybe like a year ago now, it's an embedded graph database.

00:25:34 - Andrew Nanton
So you don't have to run a database server for it.

00:25:38 - Andrew Nanton
You know, it's like, it's like SQLite or something.

00:25:41 - Andrew Nanton
It's just a file on disk.

00:25:43 - Andrew Nanton
And so that's been, that's been pretty interesting trying to get that, that going.

00:25:48 - Andrew Nanton
But that's, that's what I got.

00:25:50 - Paul Miller
Cool.

00:25:52 - Paul Miller
Jake?

00:25:56 - Jake Maymar
So we finished up the data ingestion.

00:26:00 - Jake Maymar
Distraction Tool.

00:26:01 - Jake Maymar
And that was a success, which is pretty cool.

00:26:03 - Jake Maymar
Now I'm working on some other stuff.

00:26:09 - Jake Maymar
Yeah, I think the thing is, is actually, I was going to ask Andrew this question.

00:26:17 - Jake Maymar
So you said Lama Index instead of Langchain.

00:26:21 - Jake Maymar
You like Lama Index because it's more stable or just?

00:26:27 - Andrew Nanton
So I guess there's a couple of reasons.

00:26:29 - Andrew Nanton
mean, one is because when I was first getting started with Langchain, it was right between the 0.2.

00:26:36 - Andrew Nanton
Well, it was right at the 0.2 transition and then 0.3 was right after it.

00:26:40 - Andrew Nanton
And a lot of it just was not making sense to me.

00:26:43 - Andrew Nanton
And it wasn't really making sense to anyone as far as I could tell.

00:26:46 - Andrew Nanton
And then there's this whole Langchain expression language.

00:26:49 - Andrew Nanton
You know, it doesn't, it's not particularly Pythonic.

00:26:53 - Andrew Nanton
I just, I looked at it and I played with it for a little while and Langchain really seemed to be the hot thing.

00:27:00 - Andrew Nanton
But then when I found Llama Index, I guess I would say the thing about Llama Index is that it's very RAG-specific in a way that Langchain, you know, tries to be a little bit more flexible and, you know, agnostic in terms of application.

00:27:14 - Andrew Nanton
Llama Index is pretty unapologetically a RAG tool, but it has just an amazing array of things like, you know, like chunkers and parsers and, you know, retrievers, if you want to add.

00:27:28 - Andrew Nanton
If you want to, like, for example, combine vector retrieval plus graph retrieval, but maybe you want to do, you know, like, you know, BM25 plus vector retrieval, and then you want to, like, it has all of the tools and pieces that you need for RAG, and it has fairly sophisticated implementations of those.

00:27:47 - Andrew Nanton
It also has a lot of half-completed, there's, like, bodies littered everywhere around that thing, it just is, like, you know, it's, like, half-implemented stuff still, but, yeah, at least for...

00:27:59 - Andrew Nanton
Thank

00:28:00 - Andrew Nanton
I think it's absolutely worth a look.

00:28:02 - Jake Maymar
That's great.

00:28:03 - Jake Maymar
What about Pydantic AI?

00:28:08 - Jake Maymar
I was using that for RAG for a little bit.

00:28:10 - Jake Maymar
It did some pretty nice things.

00:28:13 - Jake Maymar
The agentic RAG sort of side of things.

00:28:15 - Jake Maymar
Have you messed around with that at all?

00:28:17 - Andrew Nanton
I looked at it, but I did not get very far with it.

00:28:22 - Andrew Nanton
And there's actually another one that I'm going to put in here that one of the guys from Kuzu just keeps absolutely raving about that is fairly new.

00:28:35 - Andrew Nanton
But it looks like it might be worth poking at, called BAML.

00:28:43 - Andrew Nanton
It's like the beginning of an implementation, but it's super duper focused on structured data extraction.

00:28:50 - Andrew Nanton
And it looks really cool.

00:28:54 - Andrew Nanton
But I didn't really get very far with Pydantic AI.

00:28:58 - Jake Maymar
And then the other thing is, is...

00:29:00 - Jake Maymar
Doing a lot of stuff with Convex, and I know Bastian's doing stuff with Convex.

00:29:05 - Jake Maymar
Convex does have RAG built in, but it feels, it's not vanilla, but it feels kind of vanilla.

00:29:12 - Jake Maymar
I don't know how much I can, like, augment it, but that's kind of the thing I've been looking at right now, just because Convex is a really nice tool.

00:29:23 - Bastian Venegas
Yeah, it's great.

00:29:24 - Bastian Venegas
I haven't used RAG yet, but I liked it enough as to pay for one month, and you get a bunch of credits for the agent as well.

00:29:35 - Bastian Venegas
It's like 20 bucks or 25, and RAG is in my to-do list to try, but if it's vanilla, I actually like it more because I don't want a platform that's too opinionated.

00:29:48 - Bastian Venegas
I just want the database to be fast and sync, like, through trpc, and that's all I want from Convex, actually.

00:29:57 - Jake Maymar
Nice.

00:29:58 - Jake Maymar
Okay.

00:29:58 - Jake Maymar
Yeah, that makes sense.

00:29:59 - Jake Maymar
That definitely-

00:30:00 - Jake Maymar
makes sense.

00:30:06 - Paul Miller
I'll share, is the Kuzu the one that I was sharing?

00:30:11 - Andrew Nanton
Yes.

00:30:12 - Andrew Nanton
Yeah.

00:30:13 - Andrew Nanton
Yeah.

00:30:14 - Paul Miller
Yeah.

00:30:14 - Paul Miller
Brilliant.

00:30:17 - Paul Miller
Cool.

00:30:18 - Paul Miller
Adam.

00:30:19 - Paul Miller
Yeah.

00:30:20 - Adam
Yeah.

00:30:21 - Adam
So I went to a couple of networking events.

00:30:24 - Adam
I met a bunch of people, got a huge amount of business cards.

00:30:27 - Paul Miller
Oh, wow.

00:30:29 - Adam
Now I'm on a bunch of people's email lists.

00:30:34 - Adam
One thing I learned from meeting, I guess I'd call the normies, is it was very hard to explain to them what an agent was.

00:30:44 - Adam
So I'm going to work on a demo that I can send out to hopefully some potential clients.

00:30:49 - Adam
I also did try using the chat GWT, you know, the web agent, and it does clip Kuzu.

00:31:00 - Adam
coupons.

00:31:01 - Adam
So that's handy.

00:31:04 - Paul Miller
So the networking events you went on, were they more to get clients than network with other people that are doing stuff with AI?

00:31:13 - Adam
Yes, right.

00:31:14 - Adam
To get clients.

00:31:15 - Adam
And I was also trying to hope I could find someone that's like a value-added reseller.

00:31:21 - Adam
Like one of the guys owns an insurance company, and he seemed to be pretty pumped, like maybe he could work with me on something that could sell into the insurance company.

00:31:33 - Adam
He was telling me that their AI agents are just a disaster that they're buying off the shelf.

00:31:41 - Paul Miller
Yeah, well, that's always good if you can get into an industry vertical.

00:31:46 - Paul Miller
And did the insurance guy, do they have a broker model where people sell their policies and clip the ticket?

00:31:56 - Adam
he's an independent broker, but he's part

00:32:00 - Adam
He's of an organization that provides what he called a chat GTP wrapper that basically, I guess, other brokers that are part of his organization are buying.

00:32:16 - Paul Miller
Cool.

00:32:18 - Paul Miller
Well, that's, yeah, you kind of need to get out there.

00:32:21 - Paul Miller
You've got all those business cards.

00:32:23 - Paul Miller
Have you got, did you clarify in terms of the approach you're going to take to turn these into opportunities?

00:32:32 - Paul Miller
Have you got some niche stuff that you want to go for with these guys?

00:32:38 - Adam
No, it seems to be kind of a big blank slate on how to actually make this into a success.

00:32:46 - Paul Miller
Well, it's whoever's going to put the money on the table is the starting point.

00:32:51 - Paul Miller
With these things, a lot of people are quite happy to suck your brain in terms of take up all the knowledge.

00:33:00 - Paul Miller
It's the ones that want to pay for it, are a good place to start.

00:33:05 - Adam
Yes, yeah.

00:33:07 - Adam
Cool.

00:33:08 - Paul Miller
Thanks, Adam.

00:33:09 - Paul Miller
Al, how's it going?

00:33:11 - Al Cole
Going well, thank you.

00:33:12 - Al Cole
Going well.

00:33:14 - Al Cole
So I have been, so the two paths here.

00:33:19 - Al Cole
One is some enterprise play through my network that I'm cultivating.

00:33:25 - Al Cole
Quite frankly, the month of August is not where you do a lot of lead generating in your accounts.

00:33:30 - Al Cole
So that'll be more of a September fall play.

00:33:33 - Al Cole
So in the interim, I've been tapping people that I have personal relationships with that are running digital marketing services, property management services, and an HVAC service.

00:33:44 - Al Cole
And I pitched them all that I'd love to get in and understand their business a little bit and see if I can help with some automation, agentic or otherwise.

00:33:57 - Al Cole
And that's worked.

00:33:59 - Al Cole
So I'm...

00:34:00 - Al Cole
I'm getting in the door for the property management and the digital marketing side, and all of them are so freaking busy, they don't have time to follow the tech.

00:34:12 - Al Cole
So what I'm going to do is just basic analysis, understand where I could get some quick wins with them, and start some automation.

00:34:22 - Al Cole
My first step in the process, because I don't have expertise in these domains, is figuring out what API services would be best suited for each of these.

00:34:32 - Al Cole
And then I'm going to slowly build it up.

00:34:34 - Al Cole
And my goal here, honestly, is just to get a better handle on the tooling and what the possibilities are.

00:34:40 - Al Cole
So that's where I'm at.

00:34:42 - Al Cole
And so this is just evolving.

00:34:45 - Al Cole
I've got my first meetings this week, and I expect they'll develop over the next couple of weeks.

00:34:50 - Paul Miller
Jake, did you have something great?

00:34:52 - Paul Miller
Yeah, so are you using like, what platforms are you using?

00:34:57 - Jake Maymar
Are you using like no-code platforms or?

00:35:00 - Jake Maymar
Are you doing like GPTs?

00:35:03 - Jake Maymar
Are you doing TypeScript, Python?

00:35:05 - Al Cole
So it's interesting because based on my conversations with them, I was thinking of using NAN, Nomation, for just modeling it out, keeping it super simple, right?

00:35:16 - Al Cole
yeah, Absolutely.

00:35:18 - Al Cole
And from there, if I'm being honest with this group, once I get a few of those built, then I'll look for, you know, if I was to automate the whole damn thing, would it be repeatable and would that investment make sense, right?

00:35:31 - Al Cole
And I could bake in more engineering around it.

00:35:34 - Al Cole
So I was keeping it simple for this go around because I figured it'd be easy to explain to them how it works.

00:35:39 - Al Cole
And then it's easy to maintain and I'll see how it develops.

00:35:44 - Al Cole
But I would be curious, even though I'm focused more on the enterprise side, if there's some repeatable plays here.

00:35:50 - Al Cole
I got to imagine there are plenty of businesses that have got similar problems.

00:35:54 - Jake Maymar
Definitely.

00:35:55 - Jake Maymar
And what's really nice about N8N is you can put it in front of exactly.

00:36:00 - Jake Maymar
or a customer client, and they have ideas.

00:36:03 - Jake Maymar
They're like, oh, can we do this?

00:36:05 - Jake Maymar
And you can actually do it on the call.

00:36:07 - Jake Maymar
And so you can actually create a running workflow.

00:36:11 - Jake Maymar
I mean, some of these get really complex.

00:36:12 - Jake Maymar
I've seen some with like 500 nodes.

00:36:15 - Al Cole
And that's where I'm coming where it might make sense to pull it into our engineering shops and do something.

00:36:20 - Al Cole
But I think it's a great place to start, right, to get some early wins.

00:36:25 - Al Cole
And then I'm hoping I get the relationships developed to the point where the complexity is such that it justifies pulling it into a more, let's say, valuable engineering effort.

00:36:36 - Jake Maymar
The other advantage is you get buy-in when the client actually sees a success.

00:36:43 - Jake Maymar
Like again, on the call, I'll use N8N as like just kind of POCs to just kind of knock out ideas.

00:36:51 - Jake Maymar
And once the client sees that and they're like, hey, can I add this node?

00:36:54 - Jake Maymar
I don't really want that.

00:36:55 - Jake Maymar
Can I do this?

00:36:56 - Jake Maymar
Oh, I can do that?

00:36:57 - Jake Maymar
that.

00:36:58 - Jake Maymar
And as soon as they have that.

00:37:00 - Jake Maymar
It's like, one, you've got the sale, but also, two, now they have ownership of it, and that project often has a lot more life.

00:37:10 - Al Cole
Great, great feedback.

00:37:11 - Al Cole
I appreciate that.

00:37:13 - Paul Miller
Al, have you had a look at, for some of the clients you're talking to in the property management space, have you gone through some of their Google reviews?

00:37:25 - Paul Miller
Apify have got some great links for Google reviews, and it gives a lot of feedback with looking at the people you're talking to, and maybe their largest competitors, to look at, well, what do customers complain about the most when they're dealing with property management companies?

00:37:43 - Al Cole
And it's interesting.

00:37:45 - Al Cole
So this is super helpful.

00:37:46 - Al Cole
I just noted it.

00:37:46 - Al Cole
Thank you for that.

00:37:47 - Al Cole
So the owner that I'm talking to, they want to identify properties that they want to potentially buy, or...

00:38:01 - Al Cole
Assume, you know, maintenance ownership over.

00:38:05 - Al Cole
So he's right now at the kind of the front of the funnel where he's looking for something to add to his portfolio.

00:38:11 - Al Cole
That's where he wants me to start.

00:38:12 - Al Cole
And initially he gave me an outline and it seemed pretty straightforward, but now he wants to factor in, you know, are there mortgages?

00:38:19 - Al Cole
What's their income levels?

00:38:21 - Al Cole
I mean, things I haven't chased APIs this way.

00:38:23 - Al Cole
So this is part of my research now is trying to figure out where I might be able to source data on some of these owners.

00:38:30 - Al Cole
and give them some feedback.

00:38:32 - Paul Miller
Yep.

00:38:33 - Paul Miller
Yep.

00:38:34 - Paul Miller
Have you, have you done, done the old throw it into deep learning and get, get the Google deep learning or, or equivalent model?

00:38:44 - Al Cole
Yeah.

00:38:44 - Al Cole
So that's exactly where I'm going to end up.

00:38:47 - Al Cole
But right now what I'm finding is every email we exchange, I find the scope changing a little bit.

00:38:52 - Al Cole
So I'm going to nail them down.

00:38:53 - Al Cole
Yeah.

00:38:54 - Al Cole
And then when I get a snapshot, he feels pretty good about it.

00:38:57 - Al Cole
That's exactly what I was thinking.

00:38:58 - Al Cole
That's great advice.

00:38:59 - Al Cole
Thank you.

00:39:00 - Al Cole
I appreciate that.

00:39:01 - Al Cole
That's a great point about the scope.

00:39:04 - Jake Maymar
That's one of the biggest issues I have right now is everything is possible.

00:39:09 - Jake Maymar
And the client really believes AI is the silver bullet or basically this time anything is possible.

00:39:16 - Jake Maymar
And so getting them to basically create a realistic scope.

00:39:24 - Jake Maymar
And then unfortunately, they're getting more and more savvy with what can be done.

00:39:30 - Jake Maymar
Quickly, but the problem is not what can be done.

00:39:33 - Jake Maymar
It's the evals.

00:39:35 - Jake Maymar
That's the hard part, making sure that this stuff is actually doing what it's supposed to do.

00:39:41 - Jake Maymar
And with real client data, that's the hard part, like getting it up and running.

00:39:45 - Jake Maymar
That's pretty straightforward, even somewhat scaling, but making sure that it's actually doing what it's doing.

00:39:51 - Jake Maymar
That's the hard part.

00:39:52 - Jake Maymar
Yeah, go ahead, Andrew.

00:39:53 - Andrew Nanton
Yeah, I want to ask two quick follow up questions.

00:39:56 - Andrew Nanton
One, do you feel like there is a danger in showing people...

00:39:59 - Andrew Nanton
...

00:39:59 - Andrew Nanton
...

00:40:00 - Andrew Nanton
A, you know, knocking together a workflow on a call that gives them the impression that, you if you bill them for 10 hours, you're just, you know, wasting time and running up a bill because, well, in 15 minutes, you showed us a proof of concept and it showed.

00:40:15 - Andrew Nanton
So that's, that's question one.

00:40:16 - Andrew Nanton
And then question two is, I've been sort of going deeper and deeper down this rabbit hole of evals.

00:40:23 - Andrew Nanton
And I'm curious what tools, resources, whatever you recommend, how you are dealing with evals, because it seems like that's sort of the, the, like, where the buck stops, right?

00:40:35 - Andrew Nanton
Like, I mean, there's a lot of promises made, but like where the buck stops is evals.

00:40:39 - Andrew Nanton
And, and I don't, I feel like I don't have a great strategy yet.

00:40:44 - Andrew Nanton
I think, honestly, I think evals is a secret sauce, right?

00:40:48 - Jake Maymar
You know, we're always talking about our IPs.

00:40:49 - Jake Maymar
I think evals is a secret sauce.

00:40:52 - Jake Maymar
I'm totally sure I share all the stuff that I use.

00:40:56 - Jake Maymar
The first thing is a really great point.

00:41:00 - Jake Maymar
So client wants to use AI.

00:41:05 - Jake Maymar
I show them a workflow that does something very simple, demonstrating that we could make a workflow that does something very simple.

00:41:14 - Jake Maymar
But what they want to do is very complex.

00:41:17 - Jake Maymar
And I say, OK, we're going to go away and we're going to come back and we're either going to do it in N8N or whatever makes the most sense.

00:41:24 - Jake Maymar
But a very complex, like 500 node or 2000 node thing, I'm not going to show.

00:41:31 - Jake Maymar
I could show that to client, but they're going to just, you know, glaze over.

00:41:35 - Jake Maymar
Most of the time, the decision maker is an executive and they don't really care.

00:41:40 - Jake Maymar
They just want the solution.

00:41:41 - Jake Maymar
And so a lot of times the N8N is a POC showing that you can actually get something relatively close to one of the things they care about.

00:41:54 - Jake Maymar
But there's a lot of work in the background.

00:41:57 - Jake Maymar
You're right, though, because a lot of times they go, oh.

00:42:00 - Jake Maymar
If it's that easy, can we do this, this, this?

00:42:02 - Jake Maymar
And that's part of the scope problem that I'm running into.

00:42:05 - Jake Maymar
So I don't know.

00:42:06 - Jake Maymar
Again, I'm always trying to learn the best practices for these things because my sort of position is trusted advisor.

00:42:17 - Jake Maymar
I try my best not to sell.

00:42:19 - Jake Maymar
I try my best to advise and have authentic conversations because I genuinely want to build things that create true impact.

00:42:29 - Jake Maymar
And that's the eval side, too.

00:42:31 - Jake Maymar
So the eval side is, you know, my old data science side, right?

00:42:35 - Jake Maymar
And at least then it's a little bit more deterministic.

00:42:40 - Jake Maymar
Really simple things.

00:42:41 - Jake Maymar
Is it hallucinating, right?

00:42:43 - Jake Maymar
That's one of the big questions.

00:42:45 - Jake Maymar
But yeah, there's a whole bunch of different sort of metrics that you can get into that.

00:42:51 - Jake Maymar
Andrew, what I think is really valuable is look at fine tuning.

00:42:55 - Jake Maymar
Every fine tuning anything has evals associated with it.

00:43:01 - Jake Maymar
So hopefully that's helpful.

00:43:02 - Jake Maymar
And Bastian has a lot of really great tips on the eval side too.

00:43:09 - Jake Maymar
Not to put them on spot.

00:43:12 - Bastian Venegas
I can share something, but I haven't built a suite to evaluate something like generic or something like that, because I think the main issue is trying to get the buyer and the people who will use this excited to, for the opportunity, like almost making them want it.

00:43:34 - Bastian Venegas
And if they don't really want it, or if they have like a vague idea, I would just try to build it in different like phases or stages.

00:43:42 - Bastian Venegas
And like Brandon has suggested before, just asking the client, how do you see this application in the next, I don't know, six months, 12 months?

00:43:51 - Bastian Venegas
Like, and, and being realistic also about, uh, how the budget might evolve, because if the most of.

00:44:00 - Bastian Venegas
People are not enterprise people, but there are entrepreneurs that want to do a SaaS as their business, and they hire you just to build the MVP.

00:44:12 - Bastian Venegas
And the value you can bring is actually giving them something that works, that users can actually start using right now instead of months, just to iterate with the ones who will use it, even if it's a traditional SaaS or B2B or whatever.

00:44:27 - Bastian Venegas
And then I worry about the evals, but I basically just manually was at the beginning, and then different versions of LLM as a judge.

00:44:37 - Bastian Venegas
And I like rubrics for that, like 0 to 5, or some things can be measured actually, or can be translated to booleans, but it really depends on what you're trying to solve.

00:44:49 - Bastian Venegas
But first you need to see what's valuable to the users, because maybe hallucination is not the most relevant, as long as the user can detect.

00:45:00 - Bastian Venegas
I that it's hallucinating, for example.

00:45:02 - Bastian Venegas
So, yeah, it depends.

00:45:05 - Bastian Venegas
That's a great point.

00:45:06 - Jake Maymar
And you're totally right about what the client will bear.

00:45:09 - Jake Maymar
I do LLM as a judge all the time.

00:45:13 - Jake Maymar
Spot check, manual.

00:45:15 - Jake Maymar
And then I'll skip to client.

00:45:17 - Jake Maymar
Like, hey, here's the data.

00:45:20 - Jake Maymar
Check it.

00:45:22 - Jake Maymar
You know, and you're like, oh, it's too much to check.

00:45:25 - Jake Maymar
Well, if you want us to check it, you have to pay for it.

00:45:28 - Jake Maymar
Because that's the problem is a lot of times they do not want to pay for evals.

00:45:32 - Jake Maymar
They want quality work, but they don't want to pay for evals.

00:45:35 - Jake Maymar
At least that's what I'm finding.

00:45:37 - Jake Maymar
So, but that's great, Bastian.

00:45:39 - Jake Maymar
I think that's fantastic.

00:45:40 - Jake Maymar
And then, Andrew, these are awesome.

00:45:42 - Jake Maymar
I'll definitely look into these.

00:45:45 - Neel More
Jake, just a follow-up question on N810.

00:45:49 - Neel More
Don't you face any data privacy, or do you do a self-hosting of the N810?

00:45:54 - Jake Maymar
It depends.

00:45:56 - Jake Maymar
So, N810 is SOC 2, Type 1, Type 2, and...

00:46:00 - Jake Maymar
HIPAA compliant if you pay for it.

00:46:02 - Jake Maymar
So it all depends on kind of what kind of data you're running with, right?

00:46:07 - Jake Maymar
So a lot of times you're doing a data audit of the kind of data you have, and then you're deciding that really does affect the budget, right?

00:46:18 - Jake Maymar
And so, you know, maybe there's a way to move this over here and this over here, and then this piece that has very sensitive data, we're going to treat it differently.

00:46:30 - Jake Maymar
But yeah, N8N is SOC 2, Type 1, Type 2, and HIPAA, but you have to pay for it.

00:46:36 - Neel More
Okay, thanks a lot.

00:46:38 - Jake Maymar
Cool.

00:46:39 - Paul Miller
Thanks, Al.

00:46:40 - Paul Miller
Moving on to Abdul.

00:46:42 - Paul Miller
How's it going, Abdul?

00:46:45 - AbdulShakur Abdullah
Going all right.

00:46:46 - AbdulShakur Abdullah
So I currently am working on a project with Opal, trying to get it to run through a series of questions, and at the end it generates your

00:47:00 - AbdulShakur Abdullah
Ideal Customer Profile, because I got a client who wants me to basically find potential leads for them that they can have like customer discovery calls.

00:47:12 - AbdulShakur Abdullah
So they're an international client out of Korea.

00:47:15 - AbdulShakur Abdullah
They want to come have a bunch of meetings set up where they can talk to people in key environmental industry, pharmaceutical industry, on their particular technology.

00:47:31 - AbdulShakur Abdullah
So I was trying to quickly understand, okay, what exactly does your product do?

00:47:38 - AbdulShakur Abdullah
Because they only gave me like a one sentence description saying that it's a membrane filter that is low energy, low temperature.

00:47:50 - AbdulShakur Abdullah
And then I was like, okay, well, I don't even know where to start for who your client would be, but I put together.

00:48:00 - AbdulShakur Abdullah
Like a workflow that searched throughout the internet, pulled together, and actually they told me, oh, that's pretty close to who we want to talk to.

00:48:12 - AbdulShakur Abdullah
Basically, it only missed one aspect of desalinization.

00:48:19 - AbdulShakur Abdullah
I was like, oh, all right.

00:48:20 - AbdulShakur Abdullah
I guess it was right.

00:48:23 - AbdulShakur Abdullah
What do want?

00:48:24 - AbdulShakur Abdullah
But then when I tried to go and edit it, it just kept running into issues.

00:48:27 - AbdulShakur Abdullah
That's why I was asking if anyone...

00:48:30 - AbdulShakur Abdullah
Because I wanted to add some more capability to it and features.

00:48:34 - AbdulShakur Abdullah
But, yeah.

00:48:36 - AbdulShakur Abdullah
Is it time to move it to N18?

00:48:40 - AbdulShakur Abdullah
I don't know.

00:48:41 - AbdulShakur Abdullah
I mean, I like Opal.

00:48:43 - AbdulShakur Abdullah
And I like...

00:48:46 - AbdulShakur Abdullah
I like the costs and stuff.

00:48:49 - AbdulShakur Abdullah
I find it easy to play with.

00:48:51 - AbdulShakur Abdullah
Yeah.

00:48:52 - AbdulShakur Abdullah
The free cost.

00:48:53 - Jake Maymar
Is it SOC 2?

00:48:56 - Jake Maymar
What's the...

00:48:57 - Jake Maymar
Is it compliant?

00:49:00 - Jake Maymar
I don't know if it's compliant right now.

00:49:02 - AbdulShakur Abdullah
Right now, they just say it's experimental.

00:49:04 - Jake Maymar
Okay, fair enough.

00:49:05 - Jake Maymar
Yeah, use all the data for training, so you've just got to watch that.

00:49:10 - AbdulShakur Abdullah
Okay, so I don't think I can actually kind of put it into production.

00:49:17 - AbdulShakur Abdullah
They still don't let you have a business account with it, so you have to use your personal account too.

00:49:24 - AbdulShakur Abdullah
But I find it very easy to quickly throw something together.

00:49:28 - AbdulShakur Abdullah
Now, is it usable?

00:49:30 - AbdulShakur Abdullah
No, it's not.

00:49:31 - AbdulShakur Abdullah
Then I also, one of the changes I wanted to do was it generate, it decided to generate all the output in HTML reports, but I wanted it to give me a PDF or give me, send it into Google Docs so I could edit it some, so I didn't have to keep regenerating.

00:49:53 - AbdulShakur Abdullah
But when I tried to add that feature onto it, it just kept breaking.

00:49:59 - AbdulShakur Abdullah
I don't I I don't just...

00:50:00 - AbdulShakur Abdullah
Gave up on that, and I was like, okay, well, I guess it can only one shot.

00:50:06 - Paul Miller
Have you found some good prompts in it that you might be able to reuse?

00:50:10 - AbdulShakur Abdullah
I did.

00:50:11 - AbdulShakur Abdullah
I did find good prompts, but I would say that, I don't know if you saw what I shared earlier, the new prompting method that I have has been working pretty well for me.

00:50:25 - AbdulShakur Abdullah
So if you give me share screen power, I'll share it.

00:50:31 - Paul Miller
Yep, hold on.

00:50:35 - Paul Miller
Okay.

00:50:43 - AbdulShakur Abdullah
Let's see.

00:50:47 - AbdulShakur Abdullah
Screen.

00:50:48 - AbdulShakur Abdullah
All right.

00:50:53 - AbdulShakur Abdullah
Yeah, so basically, the prompt kind of takes my intention, and it keeps.

00:51:00 - AbdulShakur Abdullah
Pulling it out in like a back and forth method until I have kind of a whole workflow of what my end goal is.

00:51:10 - AbdulShakur Abdullah
So the idea is that it takes my rough ideas, I have a conversation back and forth, and let me change it so it's not wrapped.

00:51:22 - AbdulShakur Abdullah
I have a rough idea back and forth, and then once we both agree, it delivers what I have.

00:51:29 - AbdulShakur Abdullah
So it starts off, sometimes I just put in my original prompt idea in there, or sometimes I just start it off and tell it to wait, and then I throw it my original prompt idea.

00:51:43 - AbdulShakur Abdullah
But I find that just going back and forth and it kind of really pulling out all the ambiguous parts has really upped my prompting level.

00:51:56 - AbdulShakur Abdullah
So I have a couple of very...

00:51:59 - AbdulShakur Abdullah
very...

00:52:00 - AbdulShakur Abdullah
Very long prompts and workflows that I've been working on for that.

00:52:03 - AbdulShakur Abdullah
So I took my original workflow and then made it into a pretty long prompt that I still haven't tested yet.

00:52:18 - AbdulShakur Abdullah
So that's my kind of prompt maker.

00:52:23 - Jake Maymar
these into agents at all?

00:52:26 - AbdulShakur Abdullah
This one?

00:52:28 - Jake Maymar
Yeah, like, how do you, do you, is this like a one-off?

00:52:31 - Jake Maymar
Do you put this in like a GPT or do you put this, like, how do you deploy?

00:52:36 - AbdulShakur Abdullah
I usually copy this if I want to make a new prompt.

00:52:41 - AbdulShakur Abdullah
And then I'll go back and forth with Gemini or ChatGPT or Cloud, whichever.

00:52:49 - AbdulShakur Abdullah
This week I've been, I've been very big in Gemini.

00:52:54 - AbdulShakur Abdullah
Whichever I'm feeling at the moment.

00:52:57 - AbdulShakur Abdullah
And then kind of go back and forth with it.

00:53:00 - AbdulShakur Abdullah
But then from once I get the prompt, then I've been taking over and throwing it in Opal.

00:53:09 - AbdulShakur Abdullah
And I've made a few in Opal, but the only one that's kind of usable right now, I'd say, is the ideal customer one, and it still needs some edits on it, but I'm not happy with it just yet.

00:53:23 - AbdulShakur Abdullah
So I think I might have to take it to NAN, but at the same point, the whole reason behind it was, can I quickly, from the little bit of description I have with the client, figure out who they want to meet, so I can start getting those meetings together for them, because that's the contract.

00:53:45 - Jake Maymar
Nice.

00:53:46 - Jake Maymar
Brilliant.

00:53:49 - Paul Miller
Cool.

00:53:50 - AbdulShakur Abdullah
Speaking of, if anyone is in environmental or pharmaceuticals and wants to have a...

00:54:00 - AbdulShakur Abdullah
Conversation with a Korean company.

00:54:01 - AbdulShakur Abdullah
Let me know.

00:54:05 - Paul Miller
Cool.

00:54:06 - Paul Miller
Post it up on the school community as well, Abdul.

00:54:11 - Paul Miller
We'll get the guys in the European time zone as well.

00:54:15 - AbdulShakur Abdullah
Oh, I do need to.

00:54:17 - AbdulShakur Abdullah
They're looking for only Americans.

00:54:20 - Paul Miller
Okay.

00:54:21 - Paul Miller
Well, put it up there.

00:54:24 - AbdulShakur Abdullah
Cool.

00:54:24 - AbdulShakur Abdullah
Thanks, Abdul.

00:54:26 - Paul Miller
Now, is it Arby?

00:54:30 - Paul Miller
Did you want to jump on?

00:54:35 - Paul Miller
No.

00:54:36 - Paul Miller
Hey, everyone.

00:54:38 - Paul Miller
Hey, welcome.

00:54:40 - Paul Miller
Thank you.

00:54:40 - abhi
Thank you.

00:54:41 - abhi
This is my first time on this.

00:54:43 - abhi
And quite honestly, I do not know the working, you know, how we are working on this call.

00:54:50 - abhi
And I was not expecting that you'll call my name.

00:54:54 - Paul Miller
So, look, we have a little bit of an update.

00:54:57 - Paul Miller
We use this as a chance for everyone to.

00:55:00 - Paul Miller
Have a little update on what you're doing in the AI world.

00:55:03 - Paul Miller
And if you've got any questions for the community, we're happy to help.

00:55:08 - Paul Miller
So maybe if you just start with a bit of an intro and why are you excited about AI and why have you joined the forum?

00:55:17 - abhi
Absolutely.

00:55:18 - abhi
So Abhi, go on this side.

00:55:20 - abhi
I'm in San Francisco, California area, and I have been technical throughout my life, more than two decades of experience.

00:55:30 - abhi
Before I turned into people leader, but now with AI coming back, I feel like I want to get ahead.

00:55:38 - abhi
I want to learn what's new so that I can make sure that I drive the business in the right direction.

00:55:46 - abhi
And lately, of course, I'm trying out different frameworks, agentic framework to see how it can help.

00:55:59 - abhi
All right.

00:56:00 - abhi
And right now, at the moment, I am exploring Google ADK.

00:56:05 - abhi
And that's how I got introduced to this community because I did the masterclass associated with this community.

00:56:14 - abhi
At this moment, I have a small team of couple of devs where we are creating a POC to see if we can have, or if we can create an agent which can automate some of the tasks around L1, L2 support in technical area.

00:56:38 - abhi
You know, some kind of agent which can be integrated with ServiceNow, Jira, learn some of the existing issues, reoccurring issues, and autonomously can fix those issues as and when those come.

00:57:00 - abhi
It's kind of, you know, increasing the productivity of the L1, L2 technical staff.

00:57:05 - abhi
So that's the idea, but right now I'm in planning and designing state where I'm trying to learn what are there in market, you know, which DB works better, which platform works better, which framework works better.

00:57:26 - abhi
So that's where I am in my journey.

00:57:31 - abhi
Brilliant.

00:57:31 - Paul Miller
Brilliant.

00:57:32 - Paul Miller
Thanks.

00:57:33 - Paul Miller
Welcome.

00:57:34 - Paul Miller
Feel free outside the call times to post on the school community.

00:57:39 - Paul Miller
We've got a lot of people doing very similar things or fields where we might be able to help.

00:57:46 - Paul Miller
And the cool thing is you're tapping into technologies and APIs that are quite accessible, that others have worked with as well, but welcome.

00:57:56 - Paul Miller
Thank you.

00:57:57 - abhi
Thanks, everyone.

00:57:58 - abhi
you.

00:57:59 - abhi
So...

00:57:59 - abhi
So...

00:57:59 - Paul Miller
...

00:57:59 - Paul Miller
...

00:58:00 - Paul Miller
So next on the list, Mark, because we've got people want to sit it out this time.

00:58:08 - Paul Miller
Mark, how are you going?

00:58:13 - Marc Juretus
I was playing around.

00:58:15 - Marc Juretus
So my latest thing is I'm basically playing around with the MCP containers up in Docker.

00:58:21 - Marc Juretus
So I have, I'm just consuming the one that does a YouTube transcript.

00:58:25 - Marc Juretus
So I'm just building an app right now that I will have Superbase feed a bunch of checkboxes.

00:58:32 - Marc Juretus
And when I pull the app up, whatever checkbox I select of the influencer, it'll list the latest video that it has.

00:58:39 - Marc Juretus
It's five minutes or more description, this and that.

00:58:42 - Marc Juretus
So, you know, be able to pull up on the phone.

00:58:43 - Marc Juretus
So I can basically pull up the app, select whatever influencers I want to see if they have a new video and display it.

00:58:49 - Marc Juretus
It's just for me trying to have a library of LangChain stuff that's out that I can show people that I do.

00:58:54 - Marc Juretus
But now as I keep seeing these calls, I see Al out here making moves and this and that.

00:58:59 - Marc Juretus
I guess I better...

00:59:00 - Marc Juretus
Start consuming some of these no-codes, like NANs, and seeing if I can build some frameworks, because from what I know with this, it seems like that's a no-brainer just to know one.

00:59:10 - Marc Juretus
And I think Jake had said about it's a good way to build out before you actually write code, building something up there for proof of concept to show the customer.

00:59:18 - Marc Juretus
So that's interesting on me right now.

00:59:22 - Jake Maymar
Also, Mark, the thing is, is you can burn a lot of time coding it, whereas NAN, it's got all these nodes you just drop in, you're like, oh.

00:59:32 - Jake Maymar
And then if you're going to use that, you can code that up, but you actually see value in it, so it saves a lot of time.

00:59:39 - Jake Maymar
You know, you can hook these things up so fast, it's insane.

00:59:43 - Jake Maymar
And the thing I like about NAN is once you hook it up once, it's hooked up, you know.

00:59:48 - Jake Maymar
I mean, again, it takes a long time to get everything authorized and get the APIs and get everything set up.

00:59:55 - Jake Maymar
But once you get it set up, it's there, and then you just drop that node in, and it feels like magic.

01:00:00 - Jake Maymar
Once you get through the whole process of setting it up to begin with.

01:00:03 - Jake Maymar
Yeah, I'll find a video on it and see what I can learn with that.

01:00:07 - Marc Juretus
But that is interesting to Like what I know right now, I should try to see if maybe I can get a couple of customers where I can automate a process up.

01:00:14 - Marc Juretus
I'm not thinking outside of the box.

01:00:16 - Marc Juretus
I'm staying in this code thing, trying to develop all these apps, but I should keep my options open.

01:00:20 - Marc Juretus
So you guys are definitely putting me in the right direction on that.

01:00:24 - Marc Juretus
So and after this stuff I've learned with that, the N8th N shouldn't be too big an issue at all.

01:00:28 - Jake Maymar
Yeah, it's pretty straightforward.

01:00:30 - Jake Maymar
The one key piece I'll tell you is as soon as you get to sort of closer to enterprise, it can break catastrophically and it's very hard to debug, very hard.

01:00:45 - Jake Maymar
So be wary of that because each node has to be tested.

01:00:50 - Jake Maymar
And if something changes, it's very hard to troubleshoot it.

01:00:55 - Jake Maymar
At least that's my personal experience.

01:00:58 - Jake Maymar
think it's better results.

01:00:59 - Jake Maymar
But.

01:01:00 - Jake Maymar
But just keep in mind, let's say you have 500 nodes or 200 nodes or maybe just 10, and it's bringing in information.

01:01:07 - Jake Maymar
It's really nice because you can see what comes in and what comes out.

01:01:11 - Jake Maymar
But the problem is, if you get into a situation where it's really hard to debug that particular thing, it's hard to find a solution, I guess.

01:01:20 - Jake Maymar
So that's the only thing to just be kind of aware of.

01:01:24 - Jake Maymar
What's like a simple flow, if you don't mind me asking, that maybe you did for a customer that was not a lot to it, but just an example.

01:01:32 - Jake Maymar
yeah.

01:01:32 - Jake Maymar
So a customer wanted to basically have a Gmail trigger, so they get a specific email with a certain subject line, and they wanted to route it to a specific box.

01:01:43 - Jake Maymar
Thanks a bunch of them.

01:01:44 - Paul Miller
Right?

01:01:45 - Jake Maymar
Super simple.

01:01:47 - Jake Maymar
Okay.

01:01:48 - Marc Juretus
And then the last thing I would probably say is, like, you guys are talking about that.

01:01:52 - Marc Juretus
I'm starting to notice that with my cursor.

01:01:54 - Marc Juretus
I have it set to auto, but I took the, like, I had to go from the free to the 20.

01:01:59 - Marc Juretus
Now I'm...

01:02:00 - Marc Juretus
I'm already at, I put a threshold at 50, and I'm already at 27.

01:02:03 - Marc Juretus
So I'm starting to notice that.

01:02:05 - Marc Juretus
Do you guys, when you use Cursor, do you generally use auto, or do you use a specific model when you're using it, if you're using Cursor?

01:02:13 - Jake Maymar
Well, I use, I use Sonnet.

01:02:15 - Jake Maymar
I was using Claude Sonnet, and like, like Bastian says, you burn through it in four days.

01:02:20 - Jake Maymar
So, like, I was using it for months, and very, very happy, and it was the go-to solution.

01:02:26 - Jake Maymar
And, um, I was using, uh, Gemini 2.5, and really happy, and it was a go-to solution.

01:02:32 - Jake Maymar
But now, whatever changed with Cursor, it's harder, um, and I'm on 20 bucks a month, and now it's, I'm looking for something else.

01:02:42 - Jake Maymar
Really?

01:02:43 - Jake Maymar
Well, I like Cursor a lot, but if I only get to use it for four days, that's, you know, I don't know.

01:02:49 - Marc Juretus
Yeah, yeah, no, no, I understand, but I've just, like, noticed that myself.

01:02:53 - Marc Juretus
I'm like, wow, I'm already over at the 20, I'm at 27.

01:02:56 - Marc Juretus
And it's going to shut me off, because I have that threshold set at 50, so.

01:03:00 - Marc Juretus
I'm starting to watch.

01:03:01 - Marc Juretus
I keep hearing you guys talk about that.

01:03:03 - Marc Juretus
Now I'm noticing I'm using a lot more tokens.

01:03:06 - Marc Juretus
Jake, I have a question for you.

01:03:08 - Al Cole
was thinking about this.

01:03:11 - Al Cole
If you thought of NAN as kind of that prototype or maybe small workflow kind of tool, how hard do you think it would be to come up with a spec that ultimately went through Cursor and Cloud Code that would convert the exported flows into a Python equivalent?

01:03:32 - Al Cole
That's a great idea.

01:03:34 - Jake Maymar
Yeah, that's a great idea.

01:03:35 - Al Cole
Part of me says you prototype the thing.

01:03:38 - Al Cole
It's a great way to showcase a starting point.

01:03:41 - Al Cole
And then you get a tool that then says, now we're turning this in engineering.

01:03:45 - Al Cole
So that's the way I pitch it.

01:03:46 - Al Cole
I pitch it that I'm prototyping this thing.

01:03:49 - Al Cole
But for reliability, I'm going to give you a service that's going to be rock solid and easy to troubleshoot.

01:03:55 - Jake Maymar
Yeah, that's brilliant.

01:03:57 - Jake Maymar
That's that's actually so brilliant.

01:03:58 - Jake Maymar
I'm wondering if NAN is.

01:04:00 - Jake Maymar
Already sort of, you know, I wonder if that's sort of in the water already, but that's, that's brilliant.

01:04:04 - Jake Maymar
Let me share this MCP.

01:04:07 - Jake Maymar
So this MCP does not work, but it's worth kind of looking at.

01:04:12 - Jake Maymar
I'm not going to say it doesn't work completely, but what this MCP does is it builds N8N flows.

01:04:19 - Jake Maymar
So you can, you can basically use it in cursor, you can use it in plot, you can use it other places, but it's an MCP that, that understands all the nodes.

01:04:28 - Jake Maymar
And theoretically, oh, here it is.

01:04:31 - Jake Maymar
Is this it?

01:04:35 - Jake Maymar
Let's see.

01:04:37 - Jake Maymar
Sorry, just trying to find it really quick.

01:04:39 - Jake Maymar
I have too many links.

01:04:45 - Jake Maymar
But this MCP basically builds out, it understands all the nodes.

01:04:51 - Jake Maymar
It's very much like context 7, but specifically for, oh, here it is, I found it.

01:04:55 - Jake Maymar
So this, but the problem is...

01:04:59 - Jake Maymar
is...

01:05:00 - Jake Maymar
It doesn't work anymore.

01:05:00 - Jake Maymar
At least for me, it doesn't seem to work.

01:05:04 - Jake Maymar
But I love that idea.

01:05:06 - Jake Maymar
What you're suggesting is you...

01:05:09 - Jake Maymar
So my thought is, well, now I have all these nodes, then I can reverse engineer it that way.

01:05:14 - Jake Maymar
So, yeah, I think it's a really good idea.

01:05:18 - Paul Miller
Patrick, have you got something to add on that?

01:05:21 - Patrick Chouinard
Yeah, actually, I was just thinking, and maybe we could actually...

01:05:26 - Patrick Chouinard
Because N8N is nothing more than the JSON files.

01:05:29 - Al Cole
Anyway.

01:05:30 - Al Cole
Correct.

01:05:30 - Al Cole
The way I've seen it, right.

01:05:31 - Al Cole
It seems like everything is there, right?

01:05:34 - Patrick Chouinard
mean...

01:05:34 - Patrick Chouinard
Exactly.

01:05:34 - Patrick Chouinard
But not necessarily to use it directly to code, but more use it as a spec and actually build yourself some templates, exactly like what Brian showed us in terms of templates.

01:05:51 - Patrick Chouinard
Build a prompt that will use the JSON file as a spec, translate it in...

01:06:00 - Patrick Chouinard
to a proper spec for cursor, cloud code, whatever, but use it as a specification and have a prompt to translate it from JSON to a proper spec for your code building.

01:06:14 - Al Cole
That's another way to get there.

01:06:16 - Al Cole
I was trying to take the LLM out of it for deterministic reasons and just do more of a mapping of nodes and behavior that's implied in the nodes based on the services you're engaging.

01:06:29 - Al Cole
There could be a ton of complexity there, but this could be a fun side project.

01:06:35 - Al Cole
I may fiddle with this a bit to see how much of it I can constitute.

01:06:39 - Al Cole
Your idea is a good one.

01:06:41 - Al Cole
It's just my problem is kind of what we started with.

01:06:44 - Patrick Chouinard
You start with these specs and it really depends on the caliber of the LLM as to what you're going to end up with, right?

01:06:51 - Patrick Chouinard
For the creation, for the coding part, yeah.

01:06:54 - Patrick Chouinard
But again, if you have some solid spec, and I think that the template that Brian have Bizim solid

01:07:00 - Patrick Chouinard
shared last week were extremely useful, specifically for that, because they give you something that's precise enough that leaves very little chance for deviation.

01:07:12 - Patrick Chouinard
Well, Andrew's contribution here has got a jumpstart.

01:07:16 - Patrick Chouinard
This is pretty, this a start.

01:07:18 - Jake Maymar
That's amazing.

01:07:19 - Jake Maymar
Like, you definitely find the links.

01:07:22 - Jake Maymar
That's amazing.

01:07:24 - Al Cole
So cool.

01:07:25 - Al Cole
I was just curious if someone had already done it.

01:07:27 - Andrew Nanton
It looks like it hasn't been touched in a few months, and I'm guessing you wouldn't want to, you wouldn't want to trust that code too much, but I was just curious.

01:07:35 - Al Cole
one way to solve it, right?

01:07:37 - Al Cole
It would be one way to approach it.

01:07:40 - Patrick Chouinard
Amazing.

01:07:43 - Al Cole
Because I prefer to bring this in, I mean, if it was trying to be production worthy, I, especially what you shared, Jake, right?

01:07:53 - Al Cole
This thing, NAN will get challenged depending on the complexity of workflows.

01:08:00 - Al Cole
From what you were saying, and the troubleshooting is tough, but not tough if we had a Python equivalent.

01:08:04 - Jake Maymar
I mean, the reason why N8N is scaling is the copy and paste capability.

01:08:10 - Jake Maymar
That's it, right?

01:08:12 - Jake Maymar
Like every other one of these no-code platforms, it's hard.

01:08:16 - Jake Maymar
The copy and paste doesn't retain the JSON, so it doesn't actually retain the linkage.

01:08:23 - Jake Maymar
And I don't know how much of the linkage is retained.

01:08:27 - Jake Maymar
I mean, I think you still have to set it up, but if you could actually copy and paste and retain like all of the API auth and all that stuff with the node itself, man, that would be amazing.

01:08:43 - Jake Maymar
Yeah, yeah.

01:08:44 - Al Cole
I'll have to do some research on it, but this looks like a fun side project.

01:08:48 - Paul Miller
I'm going to do a little research.

01:08:49 - Paul Miller
Andrew, thank you for that.

01:08:50 - Paul Miller
Yeah.

01:08:51 - Paul Miller
Guys, do we think Landgraf is the place to take it to?

01:08:58 - Paul Miller
Because I know Brandon's...

01:09:00 - Paul Miller
And Brandon's quite a fan of it.

01:09:05 - Paul Miller
So where do you go if you're going from NAN to the next level?

01:09:12 - Marc Juretus
So NAN is just basically like a flow.

01:09:14 - Marc Juretus
Is it basically a flow process where it goes from jump to jump to jump?

01:09:17 - Marc Juretus
Yeah, because that's what I do with Crew AI for one of my fantasy summaries, and I've done some stuff with Landgraf.

01:09:23 - Marc Juretus
Landgraf is pretty powerful.

01:09:24 - Marc Juretus
I just remember when I was learning it, and this is back in February when I was using it, was the tools kind of sucked when you were trying to add tools within the flow, but I've heard that's gotten better.

01:09:36 - Marc Juretus
I haven't played with it as of late.

01:09:37 - Marc Juretus
I've just been using standard, but it's going to do the same thing, and it really isn't that difficult, to be honest with you.

01:09:47 - Paul Miller
Cool.

01:09:48 - Paul Miller
I think we've lost a couple off the call.

01:09:53 - Paul Miller
We'll go to Mitch next.

01:09:57 - Paul Miller
Thanks, Mark.

01:10:00 - Mitch
Yo, nothing too much.

01:10:04 - Mitch
Just maintaining that same project.

01:10:08 - Mitch
I don't want to show the EMV.

01:10:15 - Mitch
Yeah, so I'm just trying OpenCode.

01:10:18 - Mitch
It's a specific console-based version of Cursor.

01:10:23 - Mitch
I've been liking it.

01:10:26 - Paul Miller
Just testing that out.

01:10:30 - Mitch
What model are you plugging into it?

01:10:33 - Mitch
Oh, three.

01:10:34 - Mitch
Yeah, I got some serious credits to burn.

01:10:36 - Mitch
think it's like $800 in credits to burn.

01:10:40 - Jake Maymar
Nice.

01:10:41 - Jake Maymar
Yeah.

01:10:42 - Mitch
And then, yeah, just running through this.

01:10:48 - AbdulShakur Abdullah
Do you want to share some credits?

01:10:50 - AbdulShakur Abdullah
Open the credit donations.

01:10:53 - Mitch
Well, A, I might hit you up on that just because, what is it?

01:10:59 - Mitch
don't mean, there's Okay.

01:10:59 - Mitch
Bye,ら.

01:10:59 - Mitch
So, Bye Bye, Bye,

01:11:00 - Mitch
They expire like in October.

01:11:02 - Mitch
I didn't know they could expire.

01:11:03 - Mitch
I was like, that's pretty lame.

01:11:06 - Mitch
But, oh, oh wait, no, it's not.

01:11:08 - Mitch
I changed the content kit.

01:11:09 - Mitch
But anyways, this is going good.

01:11:11 - Mitch
I just need to do the back-end job handling.

01:11:15 - Mitch
So working on that.

01:11:17 - Mitch
Oh, I guess it went back to the, I've shared this before, but basically it's a workflow process for people to create an idea.

01:11:25 - Mitch
So they'll have an idea name, number of clips that are going to be in the idea for the AI VO3 video gen, and then this is what we actually input as the story.

01:11:35 - Mitch
Now I've actually integrated the different rows of different ideas.

01:11:39 - Mitch
Then those go through the master prompt sequentially, and then those outputs route back into each other.

01:11:46 - Mitch
And then we'll have a final clips page where people can view the clips, download the clips, and we can copy and paste them to then manually input into VO3 because their API is ridiculously expensive, and yeah.

01:12:01 - Mitch
But yeah, that's what I have, and then working on some other smaller stuff, but I'm not the most excited about doing the Google Cloud Functions.

01:12:11 - Mitch
I prefer to do NNN or doing...

01:12:15 - Mitch
Anyways, but that's what I'm doing next is a super-based webhook into Google Cloud Function to then do the API calls via Open Router to create the clips.

01:12:27 - Mitch
So that's what I'm working on.

01:12:30 - Jake Maymar
Cool.

01:12:31 - Paul Miller
So is the back-end all OpenAI stuff, or what are you plugging into the tool?

01:12:40 - Mitch
So the back-end is super-based.

01:12:45 - Mitch
Oh, like the back-end MLMs?

01:12:47 - Paul Miller
Yeah.

01:12:49 - Mitch
Yeah, we're using Gemini 2.5 Pro just because it has the best amount of context, and our prompts are like 80 pages long.

01:13:00 - Mitch
So yeah.

01:13:02 - Mitch
And I really do like his chain of thought process.

01:13:04 - Mitch
Like it does a really good job of like, actually, like, hey, am I doing all the things that I should be doing?

01:13:10 - Mitch
Whereas like, some other ones will be like, oh, like, you know, I need to think for myself.

01:13:16 - Mitch
And I was like, I don't want you to think for yourself, actually.

01:13:18 - Mitch
So please don't do that.

01:13:20 - Mitch
So but yeah, and then just some smaller stuff, like, we've noticed that the social platforms, they look at like, the key frames.

01:13:31 - Mitch
So they'll take a video, compress it down, and then like break it into like 30 individual frames for the entire video, and then kind of submit that to like their image analysis tool.

01:13:41 - Mitch
So kind of creating an image analysis tool of my own, so I can see how good or bad we're doing with displaying our videos.

01:13:50 - Mitch
So just some other smaller stuff that I'm working on.

01:13:53 - Mitch
But yeah, here soon, I'll be making a lot of AI junk videos.

01:14:01 - Mitch
How do you find the costs with Gemini with working with video content?

01:14:07 - Mitch
How do you?

01:14:10 - Mitch
Oh, like for VO3?

01:14:12 - Mitch
Yeah.

01:14:14 - Mitch
It's on the API.

01:14:16 - Mitch
It's like certain costs per second, but it's ridiculous.

01:14:18 - Mitch
think it's like a dollar for a five second clip or something crazy.

01:14:22 - Paul Miller
Okay.

01:14:22 - Paul Miller
Yeah.

01:14:23 - Paul Miller
I think there's VO3 fast, which is better.

01:14:26 - Mitch
A lot of the Chinese models, like they're coming up.

01:14:30 - Mitch
Um, which is good, you know, but at the same time, now I need a virtual machine.

01:14:37 - Mitch
Now I need to make the API to then connect to the virtual machine.

01:14:40 - Mitch
And then there's all that fun stuff.

01:14:42 - Mitch
So, yeah.

01:14:45 - Mitch
Cool.

01:14:46 - Paul Miller
Comfy UI looks pretty promising though, but yeah, it's a, it's funny.

01:14:50 - Mitch
It's like the video side is like what everyone doesn't really focus on.

01:14:54 - Mitch
Like everyone's kind of like in the, doing the work stuff.

01:14:58 - Mitch
So that brings some different.

01:15:02 - Jake Maymar
That's cool.

01:15:04 - Paul Miller
Cool.

01:15:05 - Paul Miller
Patrick, what's the line from you?

01:15:10 - Patrick Chouinard
I didn't move as much as I wanted this week.

01:15:13 - Patrick Chouinard
A lot of other stuff going on.

01:15:14 - Patrick Chouinard
But I did a couple of things that are interesting.

01:15:18 - Patrick Chouinard
I did a couple of attempts using ChatGPT agent mode.

01:15:23 - Patrick Chouinard
Try to find some interesting use case.

01:15:26 - Patrick Chouinard
And there's one I've posted on the board about, but I've pushed it a little bit further.

01:15:33 - Patrick Chouinard
And basically, I've used it to read the board on school, go through every single post, then categorize the different posts, use its own memory of what I know and I'm interested in, do a top 10 of the thing that I could respond to, then submit, or not submit, but generate a response that I've Thank

01:16:00 - Patrick Chouinard
It would look like what I could have answered, and then give me the top five that it would recommend me to answer and propose a basic structure for an answer.

01:16:16 - Patrick Chouinard
And it worked surprisingly well.

01:16:19 - Patrick Chouinard
worked for 20 minutes straight before giving me an answer because it really went through the whole board and pick up everything.

01:16:29 - Patrick Chouinard
So I'm not saying that this is the use case to use the tool, but it's interesting to see that it can go through massive amount of stuff, not just to do research, but to combine research, memory, and actually even understanding of its user in order to propose posts.

01:16:52 - Patrick Chouinard
So basically, I would have never had time to read all the pages of all the posts on the board.

01:16:56 - Patrick Chouinard
It did it for me and told me, like, those are the stuff.

01:17:00 - Patrick Chouinard
I think you would be interested in, and you might have something interesting to contribute.

01:17:05 - Jake Maymar
So Patrick, what pool is this?

01:17:08 - Jake Maymar
Sorry.

01:17:09 - Patrick Chouinard
ChatGPT agent mode.

01:17:10 - Jake Maymar
Oh, this is agent mode.

01:17:12 - Jake Maymar
That's excellent.

01:17:13 - Jake Maymar
And what's the, I mean, if you don't mind me sharing, what was the sort of cost?

01:17:17 - Jake Maymar
Like, is it, is that the one that's 200 a month or does it, or can you run that for the 20 bucks a month?

01:17:23 - Patrick Chouinard
I'm with the 20 bucks a month and you have 40 of those per month.

01:17:28 - Jake Maymar
Oh, nice.

01:17:29 - Jake Maymar
And actually, if you want, I can even share my screen.

01:17:35 - Jake Maymar
Yeah, because I was so curious about this.

01:17:37 - Jake Maymar
I wanted to see kind of where, where it really excelled and where it broke.

01:17:43 - Jake Maymar
But I mean, the question is, could you do a cron with this?

01:17:48 - Patrick Chouinard
Yeah, actually, agent mode can be scheduled.

01:17:52 - Jake Maymar
Oh, wow.

01:17:53 - Jake Maymar
You can use it as scheduled task.

01:17:55 - Jake Maymar
Cool.

01:17:57 - Jake Maymar
And as you can see.

01:17:58 - AbdulShakur Abdullah
Yeah.

01:17:59 - AbdulShakur Abdullah
And that's what.

01:17:59 - Patrick Chouinard
Yeah.

01:18:00 - Patrick Chouinard
Yeah, well, keep in mind that you have 40 calls per month.

01:18:04 - Patrick Chouinard
So if you do a crotch job that runs 10 times a day, four days you're going be out.

01:18:11 - Patrick Chouinard
And I've realized that it works very well for anything below half an hour.

01:18:16 - Patrick Chouinard
So if you give it a long running task that will have it churn longer than that, it starts to not be as cool after half an hour.

01:18:26 - Paul Miller
What about the quality of the output of it?

01:18:30 - Paul Miller
Is it coming in a structured format, a consistent structured format?

01:18:34 - Patrick Chouinard
Well, I'm going to show you.

01:18:35 - Patrick Chouinard
This is the small little prompt that I gave it.

01:18:39 - Patrick Chouinard
And I've realized that you have to give it a very long prompt if you want to do something useful with it.

01:18:44 - Patrick Chouinard
So you're an expert in information aggregator, blah, blah, core capability, operational constraint, user profile and expertise.

01:18:54 - Patrick Chouinard
So basically what I'm interested in value proposition, task execution workflow.

01:19:00 - Patrick Chouinard
So, and by the way, O3 came up with the prompt after a discussion with it.

01:19:05 - Patrick Chouinard
So, I've asked O3 to research itself and then come up with a structured prompt.

01:19:13 - Patrick Chouinard
Again, even tool requirement.

01:19:14 - Patrick Chouinard
Yep.

01:19:16 - Paul Miller
So, that's your prompt.

01:19:18 - Paul Miller
What about the output that you're asking for it to come out of that?

01:19:21 - Paul Miller
Yep.

01:19:22 - Patrick Chouinard
So, I think you have the read date and the output is this.

01:19:28 - Patrick Chouinard
And that's because I've asked it for an output in the markdown.

01:19:34 - Patrick Chouinard
But it respected the structure that's defined somewhere here.

01:19:40 - Patrick Chouinard
So, you see the report structure is here.

01:19:43 - Patrick Chouinard
And it did respect it perfectly well.

01:19:47 - Patrick Chouinard
Cool.

01:19:48 - Patrick Chouinard
Yeah, the markdown output.

01:19:49 - Patrick Chouinard
Did you think about using something like Appify in their school community plugins?

01:19:59 - Patrick Chouinard
No.

01:20:00 - Patrick Chouinard
Actually, I just wanted to try something that would work, like one prompt, do the job, and come out with something that I can use.

01:20:08 - Patrick Chouinard
I'm going to try to connect all of it.

01:20:10 - Patrick Chouinard
The next thing is probably going to, because I've seen that it's available through the API, so I'm going to see if I can do something from the API and not from the interface, but the result is actually pretty impressive.

01:20:25 - Adam
Do you know for cron jobs how passwords work?

01:20:28 - Adam
Because normally, right, you don't put the passwords in, and the agent stops and has the user type in the password.

01:20:37 - Patrick Chouinard
No, actually, the agent here will use, because I, for example, for school, I did not have to log in.

01:20:46 - Patrick Chouinard
It used my open session.

01:20:53 - Adam
Oh, yeah.

01:20:55 - Adam
Yeah, so didn't have to log in, didn't have to provide anything.

01:20:59 - Adam
Oh, because you had had Oh,

01:21:00 - Adam
The session open on your browser.

01:21:02 - Patrick Chouinard
Got it.

01:21:02 - Adam
Okay.

01:21:03 - Patrick Chouinard
Exactly.

01:21:04 - Paul Miller
Bastian had a question.

01:21:06 - Paul Miller
Can you schedule this as a GPT task?

01:21:09 - Patrick Chouinard
Yep.

01:21:10 - Patrick Chouinard
Exactly.

01:21:11 - Patrick Chouinard
It can be scheduled as a GPT task.

01:21:15 - Paul Miller
Cool.

01:21:17 - Patrick Chouinard
So, yeah, that's starting to be something that is useful because you have a full workflow that can be scheduled and run at specific times.

01:21:24 - Patrick Chouinard
yeah.

01:21:26 - Paul Miller
Brilliant.

01:21:27 - Paul Miller
Oh, no.

01:21:28 - Jake Maymar
You know, I wonder if you could, you know, I'm trying to figure out how I could optimize this.

01:21:35 - Jake Maymar
So, you know, prompt caching as well as, you know, identify the things that are repeating, like maybe parts of the prompt are repeating so that I could just almost essentially cache it so that it would do this one scrape and then it would just apply this thing.

01:21:53 - Jake Maymar
Yeah, that's cool.

01:21:55 - Jake Maymar
Yeah, exactly.

01:21:56 - Patrick Chouinard
Exactly.

01:21:57 - Patrick Chouinard
And that's the interesting thing is don't.

01:22:00 - Patrick Chouinard
Try to get the perfect output.

01:22:01 - Patrick Chouinard
Just try to get the perfect scraping and doing.

01:22:06 - Patrick Chouinard
So basically, if you can get the output to a point where you've gathered everything that would require login or would require interaction or code, once you have the output, then just give it to a normal LLM to process it any way you want to extract the information from there.

01:22:26 - Patrick Chouinard
And you're going to see that everything I do is always layered that way.

01:22:29 - Patrick Chouinard
For example, I noted the discussion before about the new limits in Cursor and CloudCode and things like that.

01:22:38 - Patrick Chouinard
One thing, because the other project, I still have my automated training generator that I'm working on.

01:22:44 - Patrick Chouinard
Well, instead of burning through my CloudCode credit to do the planning, I have GitHub Copilot with Gemini CLI in the terminal.

01:22:57 - Patrick Chouinard
I actually actually used...

01:23:00 - Patrick Chouinard
Use Copilot to co-write my proto-prompt.

01:23:04 - Patrick Chouinard
So basically when I state, oh, I need you to help me create a prompt that will do X, Y, Z, that's what I call the proto-prompt.

01:23:12 - Patrick Chouinard
So I let GitHub Copilot auto-complete for me.

01:23:16 - Patrick Chouinard
When I have the prompt, I then give it to Gemini CLI, and I start to create the documentation with Gemini CLI because basically there's almost unlimited amount of credit down there.

01:23:25 - Patrick Chouinard
So it's not as good as Claude for coding, but to create documentation, it's perfectly good, especially if you use templates.

01:23:35 - Patrick Chouinard
So I will create all of my documentation.

01:23:40 - Patrick Chouinard
I will get my project where the PRD has been defined by discussing with ChatGPT verbally.

01:23:46 - Patrick Chouinard
Then I will generate all of the task documentation with a composite of GitHub Copilot and Gemini CLI.

01:23:56 - Patrick Chouinard
And then I will start to use...

01:24:00 - Patrick Chouinard
I Cursor and CloudCode to actually execute the task.

01:24:04 - Patrick Chouinard
So CloudCode will execute the task, and I will use the Cursor token to do the last little step if I have debugging on specific component.

01:24:16 - Patrick Chouinard
So I try to split the token usage on as many tools as possible.

01:24:21 - Patrick Chouinard
So I end up having only $20 a month subscription and never going to the $100 or the $200.

01:24:36 - Patrick Chouinard
So yeah, just use as many tools as possible in wherever they fit the best.

01:24:42 - Patrick Chouinard
So what projects are you working on?

01:24:45 - Mitch
I know you said a couple.

01:24:48 - Mitch
Are those your main projects?

01:24:51 - Mitch
They're my main personal project because at work, I work in a very corporate environment, and we only have a GitHub copilot.

01:24:59 - Mitch
Gotcha.

01:25:00 - Patrick Chouinard
I'm more into training and R&D, so I don't have like specific coding project, but on my own time to actually keep up to date because basically all the developers are asking me how to use AI to benefit their job.

01:25:16 - Patrick Chouinard
So although I'm not per se a developer, I do have to do it a little bit if I want to tell them something intelligent.

01:25:23 - Patrick Chouinard
And that's why I'm here every week to collect as many use cases as I possibly can to create new training for them based on real live use cases.

01:25:34 - Mitch
Sounds like your project.

01:25:37 - Patrick Chouinard
Exactly.

01:25:37 - Patrick Chouinard
Building documentation and building training out of thin air is basically my project.

01:25:43 - Mitch
I don't know, You know, you might need to start a YouTube channel.

01:25:46 - Mitch
Might need to compete with Brandon a bit, you know, show him a thing or two.

01:25:51 - Patrick Chouinard
Time is my main challenge right now because this call is pretty much as much as I can devote.

01:26:00 - Patrick Chouinard
Outside of work.

01:26:00 - Patrick Chouinard
So if not, honestly, I've always said that the day I retire, I'm going to open a YouTube channel and have fun.

01:26:07 - Patrick Chouinard
You'd be good.

01:26:08 - Mitch
You'd be good.

01:26:09 - AbdulShakur Abdullah
These people are doing it because they're too...

01:26:13 - Jake Maymar
Sorry?

01:26:16 - AbdulShakur Abdullah
I'll subscribe.

01:26:20 - Patrick Chouinard
Thank you.

01:26:20 - Patrick Chouinard
I'm going to try to post as much as I possibly can in the community.

01:26:24 - Patrick Chouinard
And I've even stopped doing the blog and start creating repo instead.

01:26:30 - Patrick Chouinard
I realized that dumping Markdown in the repo works 20 times better for the community I'm interacting with than just writing a blog.

01:26:42 - Patrick Chouinard
Exactly.

01:26:44 - Paul Miller
Cool.

01:26:44 - Paul Miller
Thanks, Patrick.

01:26:46 - Paul Miller
Prem, what's happening in your world?

01:26:49 - Paul Miller
Yeah, nothing much.

01:26:51 - Prem
I'll continue to work on the project that I kind of showed a couple of weeks back.

01:26:57 - Prem
Again, the reason, the main reason I...

01:27:00 - Prem
Joined the call is to kind of talk about Cursor.

01:27:02 - Prem
I know there was a lot of discussion about, you obviously I saw a lot of slowdown with, you know, Cursor in general.

01:27:10 - Prem
And I know a few weeks back we looked at, you know, Kero and obviously now I'm still in waitlist and I didn't get the invite yet, but wanted to kind of, you know, pick your brains on did anybody kind of, because of the limitations with Cursor and so on, I'm in the $20 plan.

01:27:27 - Prem
But, you know, did anybody kind of move on to plot code or something like that, or, you know, still kind of, I think it's probably a stage where we need to kind of wait and watch which might be the route to kind of go to.

01:27:40 - Prem
I just want to kind of, I know a lot of discussions have already happened, so I kind of get an idea.

01:27:44 - Prem
But, you know, that's, you know, the main question I had to kind of join in today, if anybody kind of taken the journey or moved away from Cursor at this point.

01:27:55 - Paul Miller
Asako, did you have a go with Kero over the last week?

01:27:59 - Paul Miller
Thank you.

01:28:00 - Paul Miller
Did you want to share how you found it?

01:28:03 - asako
Yeah, sure.

01:28:05 - asako
Yeah, I've been using Curo and I liked it because it tells you the detailed plan.

01:28:13 - asako
Like, for example, if you want to implement a system, it tells you what kind of algorithm it's planning to implement.

01:28:24 - asako
So before I start coding, you have a much better idea on, like, what you'll be building.

01:28:32 - asako
So it's easier to correct the direction before I start building.

01:28:40 - asako
You haven't had a good play with the coding side, just the planning?

01:28:46 - asako
Sorry, what was your question again?

01:28:48 - Paul Miller
With Curo, how have you found the coding part of it instead of using cursor or chord code?

01:28:59 - asako
For...

01:29:00 - asako
Coding, I would say it gives me a very long lines.

01:29:05 - asako
Like it gives me like too many fallbacks that I don't really need.

01:29:12 - asako
So like in that sense, like it's more targeted towards like production level.

01:29:19 - asako
And then if you want to just mock up, it may be like you might do like too much.

01:29:25 - asako
But I happen to use the cursor a lot, so I can already do a direct comparison.

01:29:31 - Paul Miller
Okay.

01:29:32 - Paul Miller
Bastian, have you, did you end up having a go with Kiro in the last week?

01:29:40 - Bastian Venegas
No, not much because I'm working like in really specific sections of a code base.

01:29:47 - Bastian Venegas
So I'm mostly just studying.

01:29:50 - Bastian Venegas
You don't want to jump around.

01:29:54 - Paul Miller
Okay.

01:29:55 - Paul Miller
Okay.

01:29:56 - Paul Miller
So, yep.

01:29:58 - Paul Miller
So do we.

01:30:00 - Paul Miller
have any preferences outside Cursor that people are getting into now that these limits are coming through?

01:30:09 - Paul Miller
What's the main tools that people are using outside Cursor and Claude code?

01:30:16 - Neel More
Yeah, so I will go with Patrick.

01:30:18 - Neel More
So I'm using Gemini CLI a lot.

01:30:20 - Neel More
So because for the last three weeks, I was doing heavily the wipe coding.

01:30:24 - Neel More
And this Cursor AI changed the plan, and within like four hours or six hours, everything was getting completed for me.

01:30:32 - Neel More
And so Gemini CLI work, but the Gemini Pro, okay, once it switch on to the Gemini Flash, right, it loses the context, and then you have to give it one more time.

01:30:41 - Neel More
But Gemini CLI has a bigger problem of replacing the strings from the files, and sometimes it deletes the old code also.

01:30:49 - Neel More
So that's the biggest bug, and I think they are trying to solve it from last one and a half month, but they are not able to do.

01:30:56 - Neel More
But my backup is right now Gemini CLI.

01:30:59 - Neel More
I read it.

01:31:00 - Neel More
about people are using cloud code, I need to try out that, and I didn't get, I'm also on the waiting list for the key role, and I heard one more, one more, this thing, AI assistant code, it's Trae, or I don't know how to pronounce, it's T-R-A-E, so I was wondering anyone has used that also, so that will be great to know, but coming back, I'm using Gemini's CLL a lot.

01:31:26 - Paul Miller
Try code, oh, it's a plugin, and then, Let me share the link, please, yeah.

01:31:40 - Paul Miller
Put the link on the chat.

01:31:42 - Neel More
Yeah, this is the one, yeah, I was thinking of using this one also, but I have not tried.

01:31:49 - Neel More
I tried.

01:31:49 - Neel More
All right.

01:32:00 - Neel More
And I haven't tried the open code, what Mitch was suggesting, so I may have to look around it also.

01:32:06 - Paul Miller
Mitch, did you want to talk about the one you were talking about?

01:32:10 - Mitch
Sure.

01:32:11 - Mitch
But open code is more like you input your own API keys.

01:32:14 - Mitch
I don't think people are into that one too much.

01:32:19 - Mitch
But I know you can put open code into Claude.

01:32:22 - Mitch
But no, so I can share the Kuro.

01:32:30 - Mitch
So this is what someone was talking about with the Kuro.

01:32:36 - Mitch
So Kuro breaks things down so you can have an MCP server.

01:32:40 - Mitch
And when you have it do a task, it'll break it down into the requirements design task list.

01:32:46 - Mitch
So it's just a helpful format.

01:32:49 - Mitch
You can even use this for a cursor similarly.

01:32:51 - Mitch
But that's why Kuro is pretty nice.

01:32:54 - Mitch
So it first does the requirements, then moves into design, and then task.

01:32:58 - Mitch
And then it kind of does the, you know, when...

01:33:00 - Mitch
This happens, this happens, you know, it uses that specific, I think it's like PRD workflow, but, and then, yeah, the other one is warp.

01:33:09 - Mitch
Warp is really nice.

01:33:11 - Mitch
I've been using it a lot.

01:33:13 - Mitch
I basically come into Kuro, and then I create the task list.

01:33:17 - Mitch
So I'll like take my notes of like where the overall project is at, and then kind of say what's completed, what's not.

01:33:27 - Mitch
And then have like a plan for what I want to do and integrate and say, hey, okay, like, let's do this into tasks.

01:33:35 - Mitch
Here's the templates that I have.

01:33:36 - Mitch
Here's the task.

01:33:38 - Mitch
And then use this task.

01:33:40 - Mitch
And then, yeah, start the task on a different tab.

01:33:43 - Mitch
So open up any different tabs.

01:33:44 - Mitch
Each of these is a task.

01:33:45 - Mitch
And you just, man, it will like pump out code.

01:33:49 - Mitch
So, yeah.

01:33:51 - Mitch
And it's really like lenient on the usage.

01:33:56 - Mitch
So, but I haven't tried since.

01:34:00 - Mitch
They kind of slowed it down, but Warp is paying for the fees, so, you know, it's coming out of their pocket, so not yours.

01:34:10 - Mitch
Deep now, and then it'll hit you later.

01:34:13 - Mitch
Yeah, yeah, but I mean, we're all addicts at this point, so, you know, it's like we just got to switch to a different supplier, you know, if they have a cheaper product, you know.

01:34:22 - Jake Maymar
I'm so curious to see when it's going to be, like, on-prem, when we'll be running, because open source just isn't there yet, but KimiK2 was pretty exciting, but, I mean, you could have a monster machine to run that thing.

01:34:37 - Paul Miller
Yeah, yeah, indeed, indeed.

01:34:41 - Mitch
But even then, right, I mean, you could just still use the warehousing, or, like, you know, the large LLM providers, or third-party providers, they just haven't integrated to the tools yet, right?

01:34:52 - Mitch
I would say, I personally wouldn't want to locally run it.

01:34:55 - Mitch
I'd personally just rather use, you know, some other virtual machine, right, so.

01:35:01 - AbdulShakur Abdullah
I feel like the free lunch is coming to the end of the life.

01:35:06 - AbdulShakur Abdullah
I don't know how much longer they're going to keep subsidizing.

01:35:10 - AbdulShakur Abdullah
So unless the models get a whole lot more efficient and cheaper, I don't know how much longer we'll be able to use things like Cloud Code and Cursor to our heart's content.

01:35:25 - Neel More
Yeah, I tried to do the local development here, but even I got a 32 GB of RAM, a few things were not running as expected, and I gave up immediately.

01:35:34 - Neel More
I thought I was wasting a lot of time, and I moved to Gemini CLI.

01:35:38 - Neel More
At least some work I was able to do it, so I didn't spend a lot of time.

01:35:42 - Neel More
I will go back to it, but I think not sooner.

01:35:45 - Neel More
think let's see after three or six months, I will say.

01:35:48 - Jake Maymar
Yeah, I totally agree.

01:35:50 - Jake Maymar
I really, really tried to get the open source thing to work, fine-tuning and trying to get stuff.

01:35:55 - Jake Maymar
No, no, it just makes sense to just use API.

01:36:00 - Jake Maymar
And, and, and, uh, the main, main providers.

01:36:03 - Jake Maymar
Correct.

01:36:04 - Neel More
And also the LLM's call fail, uh, in this case, if you don't have a powerful LLM or a good reasoning one.

01:36:10 - Neel More
So LLM calls were failing out.

01:36:12 - Neel More
So I was not able to use at all in this case.

01:36:15 - AbdulShakur Abdullah
That video I dropped was from this guy.

01:36:17 - AbdulShakur Abdullah
I just came across my feed, Ed Zitron, who he's very, uh, he just keeps coming up, talking about how AI is a giant bubble right now.

01:36:30 - AbdulShakur Abdullah
And, and kind of, uh, no one's really making any real money.

01:36:35 - AbdulShakur Abdullah
And essentially, uh, we're all being kind of, uh, subsidized for, for a while and it's going to end soon.

01:36:45 - AbdulShakur Abdullah
So that's why I was asking if anyone's come across him and what they think about, um, what he's, he's saying.

01:36:52 - AbdulShakur Abdullah
Well, it's, it's kind of interesting.

01:36:54 - Jake Maymar
So, um, I do feel like, um, and the.

01:37:00 - Jake Maymar
This is not very popular, but, you know, the dot referencing websites and watching how the, you know, basically the dot com and then the dot bomb.

01:37:12 - Jake Maymar
I totally agree.

01:37:13 - Jake Maymar
We're in a bubble and I think we've been a series of bubbles, but this is the first time I'm seeing just across the board activity.

01:37:21 - Jake Maymar
Like there is a tremendous amount of hunger to get workflows, whether no code or actual implementations and initiatives.

01:37:32 - Jake Maymar
Like there's, there seems to be a lot of money.

01:37:34 - Jake Maymar
There seems to be a lot of interest and, and, and conversation about it.

01:37:38 - Jake Maymar
My question is just like the dot bomb, there was a whole bunch of really extremely useful websites, amazing websites, and there's a whole bunch of garbage.

01:37:49 - Jake Maymar
And there's a lot of garbage AI, like a tremendous amount of garbage AI.

01:37:55 - Jake Maymar
And I still think that the quality stuff will rise to the top because after the.

01:38:00 - Jake Maymar
Dot bomb.

01:38:00 - Jake Maymar
are still people making websites.

01:38:02 - Jake Maymar
They just had to make websites the right way.

01:38:06 - Jake Maymar
And they had to, you know, had them be commercially viable and be aware of SEO and be aware of all these restrictions.

01:38:14 - Jake Maymar
So kind of what I see it is, it's like, it's like growing, growing, growing, and it collapses.

01:38:19 - Jake Maymar
But then it sort of rebuilds in a structured way.

01:38:21 - Jake Maymar
And I think that's what's going to happen next.

01:38:23 - AbdulShakur Abdullah
I mean, I've seen that argument.

01:38:25 - AbdulShakur Abdullah
And, and I originally, I was on that camp too.

01:38:29 - AbdulShakur Abdullah
But, um, Ed, his, his whole argument is the, the, the inherent, um, bubble is not with a lot of this stuff on the, the surface that we're, we're actually referring to right now, but it's within the foundation models that, like Google, Claude, um, ChatGPT, they're all, um, heavily subsidizing our use.

01:38:56 - AbdulShakur Abdullah
And even if we're on the $200 plan.

01:39:00 - AbdulShakur Abdullah
And we're still costing them money just because of the amount of compute and resources that go into our different requests.

01:39:12 - AbdulShakur Abdullah
So like the people arguing against them are saying, well, you know, we had some advancements like when DeepSeq R1 came out kind of using more efficiency.

01:39:27 - AbdulShakur Abdullah
We had some advances in terms of Kimi-K2, a couple of other ones as well, but none of those are really driving us to the point where for the amount of use that we're doing, 20 bucks a month is going to cover kind of our costs, so, or even 200 bucks a month.

01:39:49 - AbdulShakur Abdullah
But would any of us be willing to pay like 2,000 bucks a month for what we're doing?

01:39:56 - Jake Maymar
Yeah, that's a great, that's a really great.

01:39:59 - Jake Maymar
Yeah.

01:40:00 - AbdulShakur Abdullah
Yeah, what does it max out?

01:40:02 - AbdulShakur Abdullah
Yeah, I mean, I'm at the point where I want to pay 200 bucks a month, but I don't want to pay it to all the different platforms, so I'm like, okay, is there one, like, which one, come on, guys, tell me which one should be the one that I should do, and a couple of times I'm very close to hitting it on Claude, but then I hear some feedback from you guys, I'm like, no, no, no, and then ChatGPT comes out with something really new, and I'm like, okay, I should wait more, so I haven't, I actually haven't pulled the trigger on any of the 200 bucks a month plans, and I'm still kind of just waiting, and I feel like I'm also quite a power user in terms of the amount on it, and if I'm like that, like, how many other people are going to not be willing to pay?

01:40:54 - Paul Miller
Right, we'll just take one more comment from Patrick, then we'll move on to Neil.

01:40:59 - Paul Miller
Patrick?

01:41:00 - Paul Miller
Yep, thank you.

01:41:02 - Patrick Chouinard
If I had something to say on that one is I think we're also extremely early.

01:41:08 - Patrick Chouinard
We feel like we've been doing that for years.

01:41:12 - Patrick Chouinard
But remember that this has been publicly common for most people since the end of 2023, in reality.

01:41:20 - Patrick Chouinard
So we're not even a full two years into it.

01:41:23 - Patrick Chouinard
So right now it moves incredibly fast.

01:41:26 - Patrick Chouinard
But look at where we were a year ago and where we are today.

01:41:30 - Patrick Chouinard
I mean, the local models coming out, they're not to the grade of cloud code yet.

01:41:35 - Patrick Chouinard
But they're getting extremely close for something that runs on $200 or $2,000 to $5,000 worth of hardware.

01:41:46 - Patrick Chouinard
So give it another year at the speed it goes and you're going to have something that will do most of those.

01:41:53 - Patrick Chouinard
And that may be where we're going is most of the common stuff that's quote unquote easy for LLM.

01:42:00 - Patrick Chouinard
Will be done locally, and whatever requires the large $200, $2,000 a month model will be reserved for extremely complex tasks that requires those models.

01:42:12 - Patrick Chouinard
But I think the theory of where we run what will be, what's going on, more than, oh, I need to buy this service and run everything there.

01:42:24 - Mitch
Can I go real quick, Paul, just to respond?

01:42:27 - Paul Miller
Go for it, Okay.

01:42:29 - Mitch
I was going say the main caveat with the .com versus now is I posted a video.

01:42:36 - Mitch
We're at an AI Cold War, so there's no way that the U.S.

01:42:41 - Mitch
is just going to let us get behind.

01:42:43 - Mitch
So they're going to die on everything to make sure that that happens.

01:42:48 - Mitch
We completely just looked away from copyright law, and then someone who wanted to bring that out to the public got straight murked.

01:42:57 - Mitch
So, yeah, I mean, it's pretty clear.

01:43:01 - Mitch
Where the U.S.

01:43:02 - Mitch
stands on things.

01:43:03 - Mitch
So, yeah, there's no way.

01:43:06 - Paul Miller
This is the week for announcements.

01:43:09 - Paul Miller
We've got a whole lot of announcements coming out this week from major U.S.

01:43:13 - Paul Miller
companies on this.

01:43:14 - Paul Miller
It'll be fascinating to see.

01:43:16 - Paul Miller
Have many of you played, I know, in one of those forums that there's a model that they reckon might be the next open AI paid one?

01:43:31 - Paul Miller
The question is, was it the paid one or the public one being tested?

01:43:36 - Paul Miller
I suppose we'll all know in the next few days because there's also a new Google model that's about to come out.

01:43:42 - Paul Miller
So, you're talking about the open source, open AI model that was on the leaderboards?

01:43:49 - Paul Miller
Is that the one you're talking about?

01:43:50 - Paul Miller
Well, they're suspecting it might be open AI, but it might not be because there was some mention that it could be a QIN model because of the...

01:44:00 - Paul Miller
The average token size.

01:44:03 - Jake Maymar
Yeah, I think it was a Quinn model.

01:44:06 - Jake Maymar
But I don't know.

01:44:08 - Jake Maymar
I mean, I saw it.

01:44:10 - Jake Maymar
The Quinn stuff is pretty good.

01:44:11 - Jake Maymar
You can actually code with it.

01:44:13 - Jake Maymar
Like, you can actually code with the...

01:44:15 - Jake Maymar
So one of the projects I worked on, I had to have an open source model, and I ended up using Gemma and Quinn.

01:44:27 - Jake Maymar
And Quinn did a really good job.

01:44:29 - Jake Maymar
I was really impressed with it.

01:44:31 - Jake Maymar
I wouldn't use it for a lot of things, but for that, it worked really well.

01:44:37 - Andrew Nanton
And there's also that OpenWeights GLM 4.5 Air.

01:44:43 - Andrew Nanton
I posted a link to an eval of that, the Simon Willison one, that Space Invaders demo.

01:44:51 - Andrew Nanton
So it was a 44 gig download, and he was running it on a MacBook with 64 gigs of RAM.

01:44:57 - Andrew Nanton
And it one-shot coded...

01:44:59 - Andrew Nanton
I did.

01:45:00 - Andrew Nanton
Space Invaders.

01:45:02 - Andrew Nanton
So, I mean, and that's all running locally.

01:45:05 - Andrew Nanton
think it took a good while to chew on it.

01:45:09 - Andrew Nanton
But I agree with you.

01:45:11 - Andrew Nanton
think things are starting to get interesting in the local model space in a way that a year ago, you know, I looked at them because the privacy and cost was obviously really compelling.

01:45:24 - Andrew Nanton
But, I mean, you know, unless your time is free, then it's not very compelling if the output is garbage.

01:45:31 - Andrew Nanton
And it just was not, it was not compelling.

01:45:33 - Andrew Nanton
And I feel like now maybe for some basic stuff, it's starting to get there, which is interesting.

01:45:39 - Andrew Nanton
You know, I was seeing some speculation today that OpenAI released these open source models in preparation for, you know, a bigger model announcement later this week.

01:45:50 - Andrew Nanton
You know, not to sort of steal any of that thunder, but just like maybe, maybe perhaps we'll expect a follow on announcement with their, with GPT-5 or some, you know, really big.

01:46:00 - Andrew Nanton
Step forward where it's like, okay, well, these open source ones are kind of neat.

01:46:04 - Andrew Nanton
But if you're looking for something a lot more powerful, then here's what you get.

01:46:10 - Andrew Nanton
But it seems like there's been a number of labs with these open weight models that are starting to get plausible in terms of can actually be run on consumer hardware.

01:46:22 - Andrew Nanton
Because if you have like a 405 billion weight model, I mean, that's great that it's open weight, but that's not helping me, right?

01:46:29 - Andrew Nanton
Like I don't have the hardware and no one does.

01:46:31 - Andrew Nanton
So who cares whether it's open weight, it's not terribly useful.

01:46:35 - Andrew Nanton
And then, but I mean, with some of the quantization and like mixture of experts models getting down into a size that could feasibly be run on a on consumer hardware, that's looking pretty good.

01:46:48 - Andrew Nanton
And the murmurings that I'm hearing about ATI's next architecture is that, you know, I'm sure it'll never catch NVIDIA anytime soon.

01:46:59 - Andrew Nanton
But I mean, it.

01:47:00 - Andrew Nanton
It ought to have more oomph than Apple's GPUs, which have been, you know, their real selling point is that you can get a lot of RAM stuck to it.

01:47:10 - Andrew Nanton
They're not super fast, but you can run these big models, but, you know, even if you run them a little bit slowly, but I suspect we'll be seeing some pretty interesting stuff out of ATI.

01:47:20 - Andrew Nanton
It sounds like, you know, maybe you might be able to get a board with 96 or 128 gigs of RAM on it for, you know, not $8,000 like NVIDIA wants.

01:47:33 - Andrew Nanton
I mean, it'll probably still be $3,000 or $4,000.

01:47:36 - Andrew Nanton
I don't think it's going to be anything to sneeze at, but, you it might look a little bit more plausible to be able to run some actually useful, plausible models locally.

01:47:46 - Paul Miller
What, has anyone been using the Horizon models?

01:47:51 - Paul Miller
So those were some of the test ones that came out in the last week that we thought might be Quinn, because they seem really good on this.

01:48:00 - Paul Miller
On the dev side, well, I think we'll potentially see it, was Horizon, there was an alpha, but it's a beta now, but it's worth having a look at that on the open forum.

01:48:13 - Paul Miller
But Neel, what's been happening?

01:48:18 - Neel More
Yeah, so I was already lots of active in this chat, so I'm working on the portfolio project, which is a data science project, which detects the data drift.

01:48:30 - Neel More
And then I use the agents for the investigation and creating the strategy.

01:48:33 - Neel More
So that's the portfolio project I have been working from last three weeks, and that's where I was doing heavily the wipe coding.

01:48:40 - Neel More
In this case, I'm using Google ADK, and I learn a lot from this thing.

01:48:45 - Neel More
And I think you have been through all these phases before me, but sometimes I was stuck in a few of the problems, but one model was not solving it, and it always had to switch to some other.

01:49:00 - Neel More
The best part of it.

01:49:02 - Neel More
Also, what Brandon used to show in one of this call, he showed us the interaction flow or the workflow of the development, right?

01:49:09 - Neel More
And that's how you learn.

01:49:11 - Neel More
So whenever you make a mistake, create a file or add as a rule, that worked a lot better.

01:49:16 - Neel More
And now later on, like after five or two weeks, I started getting better off so that I can rely on the web coding.

01:49:24 - Neel More
I'll do a demo or definitely within one week or two weeks of that, what I have done so far.

01:49:30 - Neel More
So it's just a backend which I had created and just finished the documentation today, just before this call.

01:49:35 - Neel More
One question I got for the team, right?

01:49:37 - Neel More
For the data science projects, we definitely use a Strimlet or Gradio for the UI.

01:49:44 - Neel More
Has anyone tried with the NextJs or would you just recommend just to stick with Strimlet or Gradio?

01:49:52 - Neel More
I'm just asking for the opinion.

01:49:54 - Neel More
Or maybe in the wider, the question is like whenever you do a demo to any clients,

01:50:00 - Neel More
Do you really create a web UI nexus or something like React, or do you try to use this Gradio or Streamlit?

01:50:07 - Neel More
I'm just wondering.

01:50:12 - Paul Miller
Jake?

01:50:13 - Paul Miller
So, yeah.

01:50:14 - Jake Maymar
So, okay, so I did a lot of stuff with Streamlit, and I felt like my hands were tied a lot of times, and I kind of got a little frustrated with it.

01:50:25 - Jake Maymar
Lovable, right?

01:50:27 - Jake Maymar
Like, that's kind of what, and Paul did some really cool lovable stuff.

01:50:30 - Jake Maymar
I highly recommend Lovable.

01:50:34 - Jake Maymar
Yeah, that's, that I think is going to get you pretty happy with your front end, and then figuring out your back end, you already kind of have that flow already in place, too.

01:50:43 - Jake Maymar
But yeah, that's what I would do.

01:50:45 - Jake Maymar
I, you know, Streamlit's great for sort of like spinning something up, but honestly, everything's gotten pretty easy to do at this point.

01:50:54 - Paul Miller
The front end side of things have gotten pretty, I mean, fairly straightforward, right?

01:50:58 - Jake Maymar
Like, it's kind of like you...

01:51:00 - Jake Maymar
Get it to a certain point, it's when you start refining it, that's where you get all the headaches.

01:51:05 - Jake Maymar
But just getting it to sort of a semi-decent state, I like lovable.

01:51:13 - Neel More
Okay, thanks so much, Jake.

01:51:15 - Marc Juretus
I like the next, I use the next, I'm sorry, I use the next.js for a lot of the little front-end stuff I'm doing, not to the extent of Jake, but it's just so easy to use when you just, you know, create a directory, another page, just TSX file.

01:51:28 - Marc Juretus
It serves it up pretty nice, so I'm actually a big fan of the next.js front-end.

01:51:33 - Paul Miller
What do you create it in, Marc?

01:51:35 - Paul Miller
Do you just prompt it through cursor and build it that way, or how are you using it?

01:51:39 - Marc Juretus
I will say this, I don't use the vibe to create the actual next project, because it does it in a weird manner, but I'll just do the command line where you create it, where you have the structure, and then from that point, I'll say, hey, in the influencers folder, page TSX, I need you to do this, and I need you to consume this fast API endpoint.

01:51:59 - Marc Juretus
And, uh, come Come

01:52:00 - Marc Juretus
It of blew me away.

01:52:00 - Marc Juretus
was actually, it's pretty amazing.

01:52:03 - Marc Juretus
I was impressed.

01:52:04 - Marc Juretus
I thought I was going to have to massage and it looks pretty nice.

01:52:07 - Marc Juretus
know, when I'm, you know, I helped Bastian help me get it deployed on Railway.

01:52:11 - Marc Juretus
You just had to create the front end and the back end directory for the two different parts of the app.

01:52:16 - Marc Juretus
Everything I'm serving up is FastAPI with the back end calling the agents.

01:52:23 - Paul Miller
Yeah, Neil, my recommendation, look, I think commercially, you really want to get people excited with the application you're putting through, but not to sort of cast negativity on the thinking of many customers, but people judge you from that UI, UX.

01:52:43 - Paul Miller
And they see a really good UI, UX that maybe, that's why I use Lovable.

01:52:51 - Paul Miller
I got the back end with FastAPI like Marc did, but I'm just not as familiar with doing that JavaScript stuff in the front.

01:53:00 - Paul Miller
I just want to get a really good architected back end and getting lovable to create something and then porting that across.

01:53:07 - Paul Miller
It was a really fast way to get there.

01:53:12 - Neel More
If you don't want to put the effort into that early on.

01:53:15 - Neel More
Yeah.

01:53:17 - Neel More
Thanks for letting me know because I was in a dilemma because this is my portfolio project to get a job in this case.

01:53:23 - Neel More
And that's why I was checking around where should I spend more time?

01:53:28 - Neel More
Because everyone is asking nowadays nextjar.js what I thought.

01:53:32 - Neel More
And also, like, I'm sticking to Google ADK because in the job market, it's LandGraph or Autogen is going around or Crew AI.

01:53:40 - Neel More
But I don't want to switch to any other platform because I want to get very good at one thing at a time.

01:53:46 - Neel More
And the concepts remains the same at the end.

01:53:49 - Neel More
Just trying my best to complete this portfolio project.

01:53:52 - Neel More
And then later on, I will hop on to see the other projects, how it goes around in this case.

01:53:57 - Paul Miller
Brain didn't get something great?

01:53:59 - Paul Miller
Yeah.

01:54:01 - Prem
So just to add to what Marc mentioned, again, Next.js is, you know, I would highly recommend, again, using the cursor.

01:54:08 - Prem
Again, I was relatively new to Next.js, was on Angular and other areas, but the UI that it generated was, like, phenomenal.

01:54:17 - Prem
again, you know, I had great experience, you know, with very few prompts, it created amazing UI, you know, and as far as the API, know, if you have, like, simple CRUD applications and so on, or you have the API where you've already done the heavy lifting, it works like a charm.

01:54:33 - Prem
Like, I didn't have to touch anything, you know, most of the work that I did was, like, for specific cases, like chunking and, like, kind of, behind the thing.

01:54:40 - Prem
That's where I saw a lot of problems.

01:54:42 - Prem
So, you know, I haven't had to touch, like, most of the UI code it generated.

01:54:46 - Prem
It kind of outdid, like, any graphic designer, you know, I worked with.

01:54:51 - Prem
So, you know, highly recommend using Cursor, you know, if you already have Cursor, know, just to kind of do the UI.

01:54:57 - Marc Juretus
And if you implement the super base, like...

01:55:00 - Marc Juretus
I'm doing a lot of stuff where I'm like, all right, I don't even want to have back end with a database.

01:55:04 - Marc Juretus
I'm leveraging Superbase.

01:55:06 - Marc Juretus
And the thing that really blew me away is I was having some friends test some of the apps I have exposed.

01:55:11 - Marc Juretus
And I was like, I don't really like leaving this out here like this.

01:55:15 - Marc Juretus
So I threw in the Superbase authentication and said, you can't get to certain pages unless you're authenticated.

01:55:23 - Marc Juretus
And once again, the cursor wrote the code pretty dead on.

01:55:26 - Marc Juretus
So it was pretty impressive.

01:55:28 - Paul Miller
Brilliant.

01:55:30 - Paul Miller
Cool.

01:55:30 - Marc Juretus
Definitely, I'll give you a try.

01:55:32 - Neel More
And one more thing is like, I know this context engineering is going around.

01:55:36 - Neel More
Where I was struggling with the wipe coding was more about the context in this case.

01:55:40 - Neel More
And I got the ADK examples.

01:55:42 - Neel More
I put that into my code repo.

01:55:45 - Neel More
It worked like a charm for a few things, but still it was not working as per my expectation.

01:55:51 - Neel More
And I was wondering, has anyone tried something like that?

01:55:54 - Neel More
Creating a rack for your examples or for the code base and later on, trying to use.

01:56:00 - Neel More
Use from the wipe coder and intercepting the call before it goes to the LLM and do a rack query and then make changes to your prompt so that you get the correct or very good answer.

01:56:12 - Neel More
So someone has tried this thing or I'm thinking too much or there are already solutions here.

01:56:17 - Paul Miller
I tried it, but maybe a suggestion might be there's a couple of tools out there to do it, but it'd be great if one of the tools is like an MCP server.

01:56:27 - Paul Miller
So it's self-hosted MCP server saying that, hey, I want to do this library or I want to do this routine.

01:56:36 - Paul Miller
Has anyone done anything kind of with that in terms of referring to your own code?

01:56:45 - Andrew Nanton
I tried with something a little more automated.

01:56:49 - Andrew Nanton
I'm trying to remember which one it was.

01:56:50 - Andrew Nanton
It was something that, and this was a little while ago, so I'm sure they've gotten better.

01:56:54 - Andrew Nanton
Um, but what I ultimately fell back to is, um, I just, the.

01:57:00 - Andrew Nanton
The context windows are so small that I find myself doing one of two things.

01:57:05 - Andrew Nanton
I either say use context seven or I give a specific link to a specific documentation page like an example or the documentation of the specific feature that I want to use, like a very manual kind of rag.

01:57:22 - Andrew Nanton
And then the last thing that I do is sometimes if it's something that I find I'm referencing a lot, I might just save it as a markdown file in the repo and say, you know, and like maybe delete out some of the examples or text that I don't need.

01:57:36 - Andrew Nanton
So I'm saving a little bit of context window size, but, you know, just kind of edit down one or two pages.

01:57:41 - Andrew Nanton
Like if I'm focused on one specific feature, I might use some combination of those techniques.

01:57:48 - Andrew Nanton
Like if I can't just do it with context seven and have it just work, then I might be, here's a specific page, read this, revise your plan based on what you read on this page.

01:57:58 - Andrew Nanton
Okay, what are you going to do differently?

01:58:00 - Andrew Nanton
And I keep iterating through, and you know, this again, I think Kiro code has something like this, but using Claude code, I'm staying in plan mode this whole time.

01:58:09 - Andrew Nanton
I'm feeding a documentation.

01:58:11 - Andrew Nanton
Okay, show me your plan.

01:58:12 - Andrew Nanton
All right, that looks a little weird.

01:58:14 - Andrew Nanton
Look at this documentation, revise your plan.

01:58:16 - Andrew Nanton
Okay, tell me what you're going to do now.

01:58:18 - Andrew Nanton
That looks too complicated.

01:58:19 - Andrew Nanton
We don't need to do steps six through 15.

01:58:23 - Andrew Nanton
But okay, let's focus on those first four steps, you know, those kinds of and just keep going kind of around and around like that.

01:58:28 - Andrew Nanton
So anyway, that's my, that's my, thanks, Adam, in this case.

01:58:34 - Paul Miller
Bastian was suggesting repo, repo prompt.

01:58:38 - Paul Miller
Is that right?

01:58:42 - Bastian Venegas
Yeah, it has an MCP and you can see that it has a, like a file explorer at the left side and you can copy all of the, the contents of all the files and formats them in a, And next time.

01:59:00 - Bastian Venegas
L or whatever format you want.

01:59:02 - Bastian Venegas
And it has a bunch of uses, but the main thing is it has an MCP server now that runs locally, and you can connect to any IDE or cloud code or whatever.

01:59:13 - Bastian Venegas
It's really cool to delegate all of the context management and searches to the...

01:59:22 - Bastian Venegas
You can delegate to an agent that works inside this tool, and then you can use your subscription to cloud code, or open router to a or whatever, and you can also connect to, like, to a cursor agent, for example, and just, like, ask it to...

01:59:39 - Bastian Venegas
I mean, you want to try it at least, because I feel like it has better search tools than cursor.

01:59:47 - Bastian Venegas
That being said, like I posted a few minutes ago, they made an update to the way that they do semantic search and all of that, so maybe it's better now, but I don't know.

01:59:57 - Bastian Venegas
Mm-hmm.-hmm.

01:59:59 - Paul Miller
Yeah.

01:59:59 - Paul Miller
Cool.

01:59:59 - Paul Miller
Yeah.

02:00:00 - Paul Miller
Cool.

02:00:01 - Neel More
Thank you.

02:00:01 - Neel More
Thank you, guys.

02:00:02 - Paul Miller
Yeah.

02:00:03 - Neel More
Really happy to have for that.

02:00:04 - Paul Miller
Stephen.

02:00:07 - StephenAmstutz
Hi, everybody.

02:00:08 - StephenAmstutz
That's my first time joining Nicole, but I've been on the community for maybe a couple of months now.

02:00:13 - StephenAmstutz
I've been working my way through the, I did the MCP Masterclass first.

02:00:18 - StephenAmstutz
That's how I found the community.

02:00:21 - StephenAmstutz
And then I've been looking at the MCP A2A RAG and kind of working my way through them.

02:00:28 - StephenAmstutz
My background's in networking, infrastructure, and cloud infrastructure.

02:00:34 - StephenAmstutz
And then there was a topic came up this week around identity, which is something I also have an interest in.

02:00:40 - StephenAmstutz
So that was kind of my reason for joining, I suppose.

02:00:45 - StephenAmstutz
Built a couple of kind of rough things for myself, but looking at, in my company, we're building an observability platform.

02:00:54 - StephenAmstutz
And looking at how I can use Egentic.

02:00:58 - StephenAmstutz
Egentic.

02:00:58 - StephenAmstutz
And Egentic.

02:00:58 - StephenAmstutz
of use Egentic.

02:01:00 - StephenAmstutz
I guess frameworks to help that.

02:01:03 - StephenAmstutz
So things like correlation, root cause analysis, suggested recommendations for resolving problems, those kinds of things.

02:01:13 - StephenAmstutz
So really getting my head around the technology at the moment, I suppose, but definitely found this group very useful.

02:01:19 - Paul Miller
Cool.

02:01:20 - Paul Miller
Any particular questions you want to put out to the community?

02:01:25 - StephenAmstutz
Not as yet.

02:01:27 - StephenAmstutz
I guess as I start building out some examples other than the kind of YouTube labs that I've been through, then I might have some.

02:01:41 - StephenAmstutz
Otherwise, yeah, there was one question, actually.

02:01:45 - StephenAmstutz
You guys were talking about all of the releases this week.

02:01:49 - StephenAmstutz
Is there a source you go to for rumours of things that are going to be released or alternately as things are being released?

02:01:59 - StephenAmstutz
I

02:02:00 - StephenAmstutz
I kind of stumbled across, I can't remember if was Google Next or Google I.O.

02:02:06 - StephenAmstutz
earlier this year, which is what got me looking at ADK to start with.

02:02:11 - StephenAmstutz
But that was like a lucky stumble because I work in Google Cloud.

02:02:16 - StephenAmstutz
But yeah, any sources like that, I guess.

02:02:20 - Paul Miller
Well, from my perspective, there's a few of the YouTube channels, the key YouTube channels that we tend to follow.

02:02:33 - Paul Miller
There's a few guys that rush to get out new videos, but there's ones that people kind of make the right call and they have a good play with them.

02:02:44 - Paul Miller
Does anyone want to have a sort of shout out as I look through my list?

02:02:49 - Paul Miller
I know there's a chap, Sam, who's based out of Singapore.

02:02:57 - Paul Miller
I think he's an Australian.

02:03:00 - Paul Miller
Guy, who does a very good one, quite balanced, very neutral.

02:03:07 - Paul Miller
I've stuck it in the chat.

02:03:10 - Paul Miller
Thank you.

02:03:12 - Paul Miller
Who else would everyone recommend in terms of good?

02:03:15 - Paul Miller
I'll say Simon Wilson.

02:03:19 - Paul Miller
Andrew's put one in the chat there as well, simonwilson.net.

02:03:24 - Paul Miller
Thank you.

02:03:26 - Paul Miller
Yeah, there's a few big ones, but if you want to...

02:03:30 - Paul Miller
Cole Medin does some good stuff.

02:03:34 - Paul Miller
I've seen him.

02:03:35 - StephenAmstutz
Yes, I have seen him.

02:03:37 - Paul Miller
Yep, and prompt engineer, Mohamed, he's a PhD in AI, takes quite a different approach looking at the stack.

02:03:51 - Paul Miller
He's been quite interesting, but yeah, you kind of do the rounds.

02:03:59 - Paul Miller
No, Thank

02:04:00 - Paul Miller
And I think if you focus on looking more at your subscription output than what YouTube generates that they think you want to watch, you can get the quality out of it.

02:04:15 - Paul Miller
Because you spend all day watching YouTube and you just get people reading off the website or copying off other people, but you want the core people that test it and they give you the feedback.

02:04:27 - Paul Miller
I think this week's going to be really interesting in terms of what's good, but like I was looking this morning, the OpenAI model came out.

02:04:35 - Paul Miller
Everyone just read it off the website.

02:04:37 - Paul Miller
There was no one that had run it through their benchmarks to say, well, look, are those models any good?

02:04:43 - Paul Miller
You've got them released through Olama and you've got them on a number of the hosts, including Amazon and Azure hosting it.

02:04:54 - Paul Miller
But where's the benchmarks?

02:04:56 - Paul Miller
Where do you go to decide if you want to use

02:05:00 - Paul Miller
Who's it is the question that I'd be asking.

02:05:04 - StephenAmstutz
No, that's really helpful.

02:05:05 - StephenAmstutz
Thank you.

02:05:06 - StephenAmstutz
And all of the tools that were mentioned today.

02:05:09 - StephenAmstutz
Yeah, I don't know where to start really, but very useful.

02:05:11 - StephenAmstutz
Thank you.

02:05:12 - Paul Miller
Yeah, and look, have a look.

02:05:15 - Paul Miller
Every week, Brandon's on vacation this week.

02:05:19 - Paul Miller
Every week, Brandon will save this message and he writes it up in terms of, well, the system writes it up, the AI writes it up in terms of the highlights and the bullet points.

02:05:28 - Paul Miller
It's worth going back through a few of the previous calls, if you haven't already, and seeing where some of the highlights have been, because it's a real goldmine of information, as Patrick was analysing with his team.

02:05:47 - StephenAmstutz
Perfect.

02:05:48 - StephenAmstutz
Thanks a lot.

02:05:49 - Paul Miller
So, anyone else before we wrap up?

02:05:56 - Paul Miller
Okay, guys.

02:05:58 - Paul Miller
Well, thank you.

02:06:00 - Paul Miller
Thank you.

02:06:00 - Paul Miller
Thank you for your input today.

02:06:03 - Paul Miller
Hopefully Brandon got through his night dive without stressing out too much and he managed to unplug and didn't annoy his wife with getting too much in the tech while he was in the Caribbean.

02:06:21 - Paul Miller
So thanks, everyone, for chipping in and have a wonderful week and really looking forward to getting everyone's input on these new models and what we should be using going forward.

02:06:34 - Marc Juretus
Thanks for moderating, man.

02:06:35 - Marc Juretus
much appreciate it.

02:06:37 - Prem
It was an amazing job.

02:06:38 - Marc Juretus
Thanks, guys.

02:06:39 - Paul Miller
Thank you both.

02:06:40 - Neel More
Have a great night and have a great week.

