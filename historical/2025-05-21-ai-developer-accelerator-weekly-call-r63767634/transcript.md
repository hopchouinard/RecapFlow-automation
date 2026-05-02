00:04:16 - Brandon Hancock
Yo, yo, everybody.

00:04:19 - Paul Miller
Hey, Brandon.

00:04:20 - Paul Miller
You've jumped out of Google I.O.

00:04:23 - Brandon Hancock
mode.

00:04:24 - Brandon Hancock
It actually finished in plenty of time, so all good.

00:04:29 - Brandon Hancock
I was worried.

00:04:30 - Brandon Hancock
Did you get a chance to watch them, out of curiosity?

00:04:35 - Paul Miller
I started going.

00:04:37 - Brandon Hancock
I'd love to hear your thoughts real fast before giving mine.

00:04:40 - Paul Miller
I haven't fully processed them, because I got excited.

00:04:45 - Paul Miller
I don't know if I've missed that on the keynote.

00:04:48 - Paul Miller
I got excited with that thing that was announced yesterday, where they've done the Codex equivalent, which I think they came up with the Codex equivalent, and then...

00:05:00 - Paul Miller
Open AI copied them, and now they've released it.

00:05:03 - Paul Miller
So I don't know if they've released it into live.

00:05:07 - Paul Miller
I'm on the wait list for it.

00:05:10 - Paul Miller
But yeah, I'm still processing.

00:05:15 - Paul Miller
I don't really have any immediate feedback.

00:05:18 - Paul Miller
What's your findings?

00:05:21 - Brandon Hancock
What's funny, real fast on that, they have like multiple competing products because they have Firebase Studio, which does the thing.

00:05:28 - Brandon Hancock
Then they have their coding project, like that's all Gemini.

00:05:32 - Brandon Hancock
I think the one that you're talking about, which basically also does the same thing.

00:05:37 - Brandon Hancock
So I think they're just like, we're just going to fund every innovative project internally that we can think of, and just throw everything out to the world.

00:05:44 - Brandon Hancock
And whatever people continue to play with, we will continue to support.

00:05:48 - Brandon Hancock
So I think that's what they're doing.

00:05:50 - Brandon Hancock
It would take me more tools to play with.

00:05:53 - Brandon Hancock
I will say like actionable things to work on.

00:05:58 - Brandon Hancock
Like I didn't find it.

00:06:00 - Brandon Hancock
I thought there was going to be a bunch of new stuff, but it was mostly actually upgrades, like their new video generator, then they have their new image generator.

00:06:11 - Brandon Hancock
All the APIs kind of got a new model, but yeah, I was hoping for a few new developer tools or things.

00:06:17 - Brandon Hancock
Didn't really hear any.

00:06:20 - Brandon Hancock
The only one I'm kind of pumped for is Firebase Studio.

00:06:26 - Brandon Hancock
They listened to everyone and were like, yeah, the whole point of Firebase Studio is to connect to Firebase.

00:06:32 - Brandon Hancock
We're now going to actually let you do that.

00:06:34 - Brandon Hancock
Like, which I thought was wild that they took this long to like, oh yeah, now you can do it.

00:06:39 - Brandon Hancock
So I've been trying to log in over and over and over again to actually like get involved or see if they've actually rolled it out because they said they were going to.

00:06:48 - Brandon Hancock
So no update yet, but hey, maybe in just a few minutes they will.

00:06:52 - Brandon Hancock
So I'll let you, as soon as it's up, I'll let you guys know.

00:06:58 - Brandon Hancock
But yeah, those were big takeaways.

00:07:00 - Brandon Hancock
Um, real fast, and then we can dive in, though, to the call, guys.

00:07:04 - Brandon Hancock
Always good to see you.

00:07:05 - Brandon Hancock
Everybody on the group, love all the friendly faces.

00:07:09 - Brandon Hancock
The main updates on my side this week, mostly just spending a ton of time building out a project for a client.

00:07:17 - Brandon Hancock
A ton of fun with Supabase right now.

00:07:20 - Brandon Hancock
Still stand by my earlier suggestion of, like, all the row-level security and all the other stuff that you have to set up.

00:07:28 - Brandon Hancock
It, it, it's a pain in the butt.

00:07:30 - Brandon Hancock
So, but when it works, great.

00:07:33 - Brandon Hancock
But getting it actually working, God, it's, it's, it's taken up so much time to actually just, like, I want this data to go here.

00:07:40 - Brandon Hancock
And even when you set the row-level security, it's like, oh, actually, this role itself, not even, not even user-based role, but, like, this type of user itself cannot even make this action.

00:07:51 - Brandon Hancock
So, it's, like, row-level, then, like, there's, there's row-level security, then role security, and then there's the actual authentication you do in your app.

00:07:59 - Brandon Hancock
So, it's, row

00:08:00 - Brandon Hancock
It's been kicking my butt.

00:08:01 - Brandon Hancock
So very excited to wrap that up.

00:08:04 - Brandon Hancock
I definitely have a few videos for you guys planned.

00:08:07 - Brandon Hancock
One, I would just share like, hey, this same project a year ago would have taken like weeks.

00:08:15 - Brandon Hancock
And now with Lovable, the new Gemini 2.5 Pro, absolutely love that thing.

00:08:22 - Brandon Hancock
Cursor-based rules.

00:08:24 - Brandon Hancock
I've been able to crank out what should have taken multiple weeks and like days.

00:08:28 - Brandon Hancock
So I was just going to share my workflow for knocking stuff out.

00:08:31 - Brandon Hancock
So that'll be a video later this week.

00:08:32 - Brandon Hancock
Yeah, that is everything on my side.

00:08:35 - Brandon Hancock
And we'll start going around the room.

00:08:38 - Brandon Hancock
In case this is your first time, welcome.

00:08:41 - Brandon Hancock
Basically, the lay of the land is we go round robin around the room and usually just share a wind, something interesting that you want to share with the group or if you're stuck on a problem.

00:08:54 - Brandon Hancock
And we'll happily chip in as a group.

00:08:56 - Brandon Hancock
And I'm going to really quick share the order that I'm going to call.

00:09:00 - Brandon Hancock
Help people in right now in the chat, and then we can get started.

00:09:04 - Brandon Hancock
But, Paul, you're up first, if you want to go ahead and kick things off for everybody.

00:09:11 - Paul Miller
Yeah, so I've pretty much got launched into Alpha testing with the user, my little first-level app with the FastAPI backend.

00:09:26 - Brandon Hancock
That's awesome.

00:09:28 - Paul Miller
That's working well.

00:09:30 - Paul Miller
He's about to share it with his clients at the end of today, so we've got one minor thing he's found, which I'm just going to jump into fixing, which is so easy now, because it's nice and segregated, and I don't go and stuff up the API, and that knocks onto everything else.

00:09:49 - Paul Miller
So I'm pretty excited about that.

00:09:53 - Paul Miller
No other sort of real exciting stuff other than I got distracted in my usual...

00:10:00 - Paul Miller
...

00:10:00 - Paul Miller
...

00:10:00 - Paul Miller
...

00:10:00 - Paul Miller
Way, I was out walking the dog, we live next to a park in Auckland, and we've got this lowlife who, instead of buying a garden waste sort of collection, you subscribe and they come and pick up your branches and leaves and wall clippings and stuff like that.

00:10:22 - Paul Miller
This, this individual dumps his arm branches in the park so he doesn't have to wait for someone to pick it up.

00:10:36 - Paul Miller
Not cool, man.

00:10:38 - Paul Miller
Not cool.

00:10:38 - Paul Miller
But it's been going for a couple of years, but being, being a sort of over-the-top geek, our house is surrounded by AI cameras, and it all goes to DVR system, and the last time he did it, I, I got, I got, I got him filmed doing it.

00:11:02 - Paul Miller
I sent him to the council with all the video clips for the council.

00:11:09 - Paul Miller
He didn't know that the cameras were there.

00:11:10 - Paul Miller
I think he thought, I just saw him from my car.

00:11:14 - Paul Miller
And I noticed a couple of days ago, he's done it again.

00:11:19 - Paul Miller
So instead of manually going into the Reolink NVR, I thought, oh, I could go into some kind of API because it's quite an open environment, download all the videos, analyze them, and look for his car.

00:11:37 - Paul Miller
Because I don't want to go through days of video footage.

00:11:40 - Paul Miller
So I've kicked off a little project to build an API over the VR and then build apps that I want to look at an AI app where I put a description of what I'm looking for and just get the AI to go off and go.

00:12:00 - Paul Miller
Drill the videos and find the car and find the incident.

00:12:04 - Brandon Hancock
He's pissed off the wrong nerd.

00:12:06 - Brandon Hancock
That's all I got to say.

00:12:10 - Paul Miller
It's a bit of an overkill.

00:12:14 - Paul Miller
I should be focusing on my day job, not faffing around with that stuff.

00:12:19 - Brandon Hancock
Real fast.

00:12:20 - Brandon Hancock
Quick idea.

00:12:21 - Brandon Hancock
Just the Gemini model itself, the two, I think two five flash.

00:12:28 - Brandon Hancock
I think that is now more stable.

00:12:30 - Brandon Hancock
I think you can pass videos to it and especially like just throw it in at 720p because it doesn't need to be high res to detect it.

00:12:37 - Brandon Hancock
And you could probably sift through all of that for like a couple dollars, which is wild.

00:12:42 - Brandon Hancock
So that would be, you know, how I'd recommend trying it out.

00:12:47 - Brandon Hancock
So, yeah, let me know when it works.

00:12:49 - Brandon Hancock
I'd love to a demo of it because, yeah, that's a pretty cool use of video.

00:12:56 - Brandon Hancock
Um, yeah, I'm just, I'm invested in the story now.

00:12:59 - Brandon Hancock
So please give me a post.

00:13:00 - Brandon Hancock
What happens next?

00:13:03 - Paul Miller
Thanks, Brandon.

00:13:05 - Brandon Hancock
And Bastian had a cool idea, too, of like, hey, you could actually probably do some preprocessing before you pass things up to Jim and I just to cut down on frames.

00:13:13 - Brandon Hancock
Because, like, it doesn't need to be 30 frames per second.

00:13:16 - Brandon Hancock
Probably just, like, two, three, four, five.

00:13:18 - Brandon Hancock
There's probably plenty.

00:13:20 - Brandon Hancock
So pretty cool idea.

00:13:21 - Brandon Hancock
could save our money, too.

00:13:23 - Brandon Hancock
So, yeah, that's awesome.

00:13:25 - Brandon Hancock
Thanks, Paul.

00:13:26 - Brandon Hancock
Excited.

00:13:26 - Brandon Hancock
And I'm all in, too.

00:13:30 - Brandon Hancock
All right.

00:13:31 - Brandon Hancock
Mark, you're up next, man.

00:13:33 - Brandon Hancock
What's going on?

00:13:34 - Brandon Hancock
What projects are you working on?

00:13:35 - Brandon Hancock
I owe you a message.

00:13:37 - Brandon Hancock
I just got to go back into, I got to go into my messages.

00:13:40 - Brandon Hancock
But I owe you one.

00:13:41 - Marc Juretus
No rush, man.

00:13:42 - Marc Juretus
I figure you want that syllabus of what Chris went through.

00:13:46 - Marc Juretus
So, yeah, I sent you basically the PDF that they sent us at the weekend course.

00:13:50 - Marc Juretus
So it has everything changed and stuff like that.

00:13:54 - Marc Juretus
As far as what I've been working on, I was kind of obsessed with consuming an MCP.

00:14:00 - Marc Juretus
Here I am.

00:14:00 - Marc Juretus
Inside of my Python code, as opposed to leveraging it, you know, in Claude or something like that.

00:14:05 - Marc Juretus
I was, it took me a little while to get that working and stuff.

00:14:08 - Marc Juretus
But, you know, one of the videos I've watched on that, the guy was alliterating to the fact that a lot of stuff, if you're going to do custom MCP, you can accomplish with either, you know, FastAPI or your own functions and stuff.

00:14:20 - Marc Juretus
But where it's going to go to is what he was pretty much saying that, you know, it's going to be a lot more useful in the future.

00:14:27 - Marc Juretus
I mean, it's obviously, because of all the plugins now and stuff, you can do a Claude, personal shopper, scrubbing videos and stuff like that.

00:14:34 - Marc Juretus
So, it's, that's interesting.

00:14:35 - Marc Juretus
So, I was trying to get FastAPI working because, honestly, in my day job where I do Spring Boot, I got to serve up APIs with Java Spring Boot.

00:14:44 - Marc Juretus
So, I was trying to learn the latest practices with that.

00:14:47 - Marc Juretus
So, I didn't have a lot of extra time with that.

00:14:50 - Marc Juretus
But I did have a question.

00:14:52 - Marc Juretus
As far as, say, I wanted to actually convert some, like, of my stuff to, like, a vector database that I only...

00:15:01 - Marc Juretus
And what I want to do is, so I go on to Postgres in Docker, maybe turn that on, and if I point to that tool, if I have information, I can have a tool created that can have an agent go against that only one I would need it.

00:15:13 - Marc Juretus
I wouldn't want to really push it in the cloud.

00:15:15 - Marc Juretus
So I'm wondering if I would do it in like a LangChing or LangGraph or with a crew AI or just something else that's more progressive that you would recommend.

00:15:22 - Marc Juretus
I'm just going to basically take a bunch of data, throw it all in, and I've seen there's a pretty easy way to do it with Agno as well.

00:15:29 - Marc Juretus
But what would you do if you had data that you're going to use intermittently for maybe different projects, but you'd like to be able to turn on and point to it as a tool would be my question.

00:15:38 - Brandon Hancock
Okay.

00:15:38 - Brandon Hancock
And so just to make sure I fully understand, so you are basically, you have documents that you want to put to a vector store, and you are going to be interfacing, basically making rag requests to this vector store in multiple applications, like in some through agents, some probably through like a website.

00:15:56 - Marc Juretus
Like, is it not just mainly through just mainly all agents.

00:16:00 - Marc Juretus
So I'll just.

00:16:00 - Marc Juretus
Just turn it on and have a tool pointed to it in whatever way.

00:16:03 - Marc Juretus
And, you know, I might have a combination of data, PDFs, and stuff like that.

00:16:07 - Marc Juretus
It's like my own, you know, my own knowledge base.

00:16:10 - Marc Juretus
But I was like, sometimes I want to push in the cloud, but like, hey, I want to have this on.

00:16:14 - Marc Juretus
I want to point to it.

00:16:15 - Marc Juretus
What would you use?

00:16:16 - Marc Juretus
Would you use a Langchain?

00:16:18 - Marc Juretus
Would you use Crew, Agno?

00:16:20 - Brandon Hancock
What would you do that in?

00:16:21 - Brandon Hancock
No, I mean, strictly two approaches.

00:16:24 - Brandon Hancock
One, I would just spin up a local server that connects to, so part by part.

00:16:31 - Brandon Hancock
So you need somewhere to store all the vectors.

00:16:33 - Brandon Hancock
So I would recommend like a ChromaDB is the easiest one to just spin up a local vector store in.

00:16:39 - Brandon Hancock
So I would definitely recommend if you're going to, you're going to need a vector store locally.

00:16:44 - Brandon Hancock
ChromaDB is probably one of the easiest ones to use.

00:16:47 - Brandon Hancock
There's a few other ones, but that's the one I'm most familiar with.

00:16:50 - Brandon Hancock
You could also, you did mention, I think you're pretty familiar with Postgres.

00:16:54 - Brandon Hancock
You can do that as well, but Chroma is the easiest way to make a vector store.

00:16:59 - Brandon Hancock
Like if you just want a standalone vector store.

00:17:00 - Brandon Hancock
Or ChromaDB, try not to recommend.

00:17:03 - Marc Juretus
Well, like, so you went to an agent and you typed in a question and then you say, I want to take the response to the answer I got to that.

00:17:08 - Marc Juretus
I want to store that locally in my rag and have that as my own personal, like, knowledge base is what I was trying to accomplish.

00:17:17 - Brandon Hancock
Oh, okay.

00:17:17 - Brandon Hancock
So you want to say, like, message history?

00:17:19 - Brandon Hancock
Yeah.

00:17:19 - Brandon Hancock
So in that case, I mean, either way, we still have to have the vector store.

00:17:22 - Brandon Hancock
But basically what you'd want to do is spin up either, kind of like you just alluded to a second ago, either an MCP server or you want to just spin up a generic Python fast API.

00:17:33 - Brandon Hancock
The fast API would expose, like, three endpoints, like, query and add.

00:17:38 - Brandon Hancock
mean, that's really it.

00:17:39 - Brandon Hancock
Those are the two things that you would want to set up.

00:17:42 - Brandon Hancock
And you could just create two tools in whatever agent framework you're using that knows how to use those two endpoints.

00:17:49 - Brandon Hancock
So you're basically just going to wrap that endpoint.

00:17:52 - Brandon Hancock
So I know Bastian has the most experience with MCP.

00:17:56 - Brandon Hancock
I'd love to get his thoughts on it really fast if he's back.

00:18:00 - Brandon Hancock
Jusin, if you want to hop on.

00:18:01 - Bastian Venegas
Yeah.

00:18:02 - Bastian Venegas
Actually, I just came across a repository that it's called Graffiti because it's an MCP server that implements some sort of GraphRack.

00:18:15 - Bastian Venegas
So if you're trying to explore both spaces, I will link it in the chat.

00:18:22 - Bastian Venegas
You can take a look at that.

00:18:25 - Marc Juretus
Okay.

00:18:25 - Marc Juretus
Yeah, I'll do that.

00:18:26 - Marc Juretus
I was kind of confused on what agent I would use to actually convert it to Vector.

00:18:32 - Marc Juretus
That's where I was like, I could do the PostgreSQL to Chroma, like you said, or I'll look at what you have.

00:18:37 - Marc Juretus
But I was like, what's actually the agent to use if I could prove it?

00:18:40 - Bastian Venegas
vectorize the query, the answer query.

00:18:43 - Bastian Venegas
Oh, yeah.

00:18:44 - Bastian Venegas
So that's the embedding model you can use.

00:18:47 - Bastian Venegas
We're just talking about that, Brandon.

00:18:50 - Bastian Venegas
And you can use like the text embeddings model, the three versions, which is really sufficient.

00:18:58 - Bastian Venegas
And there's also a...

00:19:00 - Bastian Venegas
Um, Google, uh, embedding model that I will link in the, in the chat as well.

00:19:08 - Marc Juretus
Okay.

00:19:09 - Marc Juretus
The, the Google one's awesome too.

00:19:10 - Brandon Hancock
Real fast, Mark, just to add onto that.

00:19:12 - Brandon Hancock
So the agent will actually know what the agent will know nothing about RAG.

00:19:17 - Brandon Hancock
That's the, that's the beauty of it.

00:19:19 - Brandon Hancock
The, all the agent knows is, Hey, whenever I want to get new information on a topic, I just make a tool call.

00:19:26 - Brandon Hancock
That is the extent that the agent knows about RAG.

00:19:30 - Brandon Hancock
All of the, the RAG service, meaning the taking in a text question from the agent.

00:19:37 - Brandon Hancock
So like the agent would pass in a raw text that the embedding of that text, uh, um, basically to embed it into like, you know, all the ones and zeros and everything else that it needs to like actually query the vector store.

00:19:48 - Brandon Hancock
All of that, that's going to happen inside the, the fast API service that you're going to stand up.

00:19:51 - Brandon Hancock
So I just wanted to like draw like a hard line, like agents, all that uses tools, those tools.

00:19:57 - Brandon Hancock
In the case of your example, the tool is just going to make.

00:20:00 - Brandon Hancock
Literally just pass a query, just a string query over to your API, and then your API is going to handle the embedding, it's going to handle making the query, and then it's going to come back with a response of like, hey, I found this chunk, this chunk, and this chunk.

00:20:16 - Brandon Hancock
Use it however you want to page it.

00:20:18 - Brandon Hancock
But once again, the agent's also only going to get back text.

00:20:21 - Brandon Hancock
It's not going to get back all the raw ones and zeros of the embedding.

00:20:29 - Marc Juretus
So, does that make sense?

00:20:30 - Marc Juretus
Yeah, yeah.

00:20:31 - Marc Juretus
And you said whenever you have front-end stuff, you, like, as far as like production, you never use like a Streamlit.

00:20:36 - Brandon Hancock
It's always like a Next.js.

00:20:38 - Brandon Hancock
Is that what you said?

00:20:39 - Brandon Hancock
Or a Streamlit, something just locally for testing that you found?

00:20:43 - Brandon Hancock
I mean, I love just using Next.js for all things.

00:20:46 - Brandon Hancock
That's how like my brain thinks.

00:20:48 - Brandon Hancock
So, Streamlit can work.

00:20:50 - Brandon Hancock
It's just like the second you want to do anything a little bit more advanced, you're kind of like, well, dang, now I just got to start over with Next.js anyway.

00:20:57 - Brandon Hancock
So, like, might as well just go with the thing.

00:21:00 - Brandon Hancock
It is scalable.

00:21:01 - Brandon Hancock
And every AI tool right now just really understands Next.js really well, too.

00:21:08 - Brandon Hancock
You'll be amazed how easy it is to get it spun up.

00:21:12 - Brandon Hancock
So, yeah, let me know if you have any other questions.

00:21:15 - Brandon Hancock
And, yeah, I think, yeah, if you end up starting to go down this path and run into any issues, if you just want to, like, do, like, a quick loom video and shoot me a DM, I'd be happy to, like, review it as well.

00:21:26 - Brandon Hancock
Just because I'm starting to get in the, starting to go into the weeds.

00:21:30 - Brandon Hancock
So, hopefully, hopefully this helps.

00:21:33 - Brandon Hancock
Finally, something I think you'd find interesting, if I have time this, by the end of the week, I want to do a ADK MCP tutorial.

00:21:40 - Brandon Hancock
So, that might be also helpful just because, like, instead of setting up the fast API server, you might also, like I said, consider MCP.

00:21:50 - Brandon Hancock
So, I'll go into that and I'll report back, too, of how easy I think it is.

00:21:54 - Brandon Hancock
Yeah, I'm getting pretty deep in your ADK stuff, though.

00:21:57 - Marc Juretus
Like, basically, I'm taking what I have in my crew for that fantasy football app I have.

00:22:00 - Marc Juretus
I'm going

00:22:00 - Marc Juretus
Converting it completely to Google ADK, and I finally got the wrappers of Kru, because I like their scrape tool and their server dev tool.

00:22:08 - Marc Juretus
I was actually able to do that embedding, and ADK was able to consume and give me output.

00:22:13 - Marc Juretus
So some of the stuff I have, I can reuse, but I want to get it completely over there with a sequential agent.

00:22:19 - Marc Juretus
So it looks like, thanks to you though, man, that  was really easy to go.

00:22:24 - Brandon Hancock
Perfect.

00:22:25 - Brandon Hancock
What's really cool, I've started to, I'd like to talk to some of the guys on the team, ADK team.

00:22:31 - Brandon Hancock
They're so responsive to feedback, like they're instantly, they're chomping at the bit to add in features.

00:22:36 - Brandon Hancock
So one of the issues you'll see with sequential agents is like, sometimes they pop out and say like, hey, do you have a question?

00:22:42 - Brandon Hancock
Which is kind of not what you want in a workflow, because like the whole point of a workflow is it just does the work, and it fits you the answer.

00:22:47 - Brandon Hancock
So like, they're looking into stuff like that, so they're hyper responsive.

00:22:51 - Brandon Hancock
So if you ever have anything, let me know, happy to pass along, because I want to make sure, I'm loving it.

00:22:55 - Brandon Hancock
So I just want to make sure, I just want to make sure it keeps getting better and better and better.

00:23:00 - Brandon Hancock
So.

00:23:00 - Brandon Hancock
Mark, you're working on all the cool stuff, so please keep me in the loop.

00:23:02 - Marc Juretus
I think this is exciting.

00:23:04 - Marc Juretus
It seems like doing Google ADK now, like I said last week, is kind of like doing Crew AI 10 months ago.

00:23:10 - Marc Juretus
Like, it's the most progressive thing in my opinion.

00:23:13 - Marc Juretus
That's just my two cents on it, but I like it a lot as well.

00:23:16 - Brandon Hancock
Awesome.

00:23:17 - Brandon Hancock
Awesome.

00:23:17 - Brandon Hancock
Well, I'm ready to see who I should put my money on for fantasy football once you have your thing done.

00:23:22 - Marc Juretus
Let me know.

00:23:23 - Marc Juretus
$5.

00:23:24 - Marc Juretus
Yeah, we got it, man.

00:23:25 - Marc Juretus
I'm in some heavy leagues, man.

00:23:27 - Marc Juretus
The one I have, the best one is a guillotine.

00:23:29 - Marc Juretus
Like, they cut whatever.

00:23:30 - Marc Juretus
Every team has the worst record.

00:23:31 - Marc Juretus
You get cut every week, and you got to make it to the end.

00:23:33 - Marc Juretus
Oh, dang.

00:23:34 - Brandon Hancock
That's brutal.

00:23:35 - Marc Juretus
Yeah, it is, man, because you're sitting there like, , I'm about to get knocked out, and you're watching my scoreboard in real time.

00:23:41 - Marc Juretus
Like, come on, man.

00:23:41 - Marc Juretus
I just need a point.

00:23:42 - Marc Juretus
I want to last another week.

00:23:44 - Brandon Hancock
That's funny.

00:23:45 - Marc Juretus
That's funny.

00:23:46 - Marc Juretus
cool.

00:23:46 - Brandon Hancock
It's deep.

00:23:48 - Brandon Hancock
Stakes are high.

00:23:49 - Brandon Hancock
Stakes are high.

00:23:49 - Brandon Hancock
Hopefully AI can help.

00:23:52 - Brandon Hancock
All right.

00:23:52 - Brandon Hancock
Perfect.

00:23:54 - Brandon Hancock
Let's see.

00:23:54 - Brandon Hancock
Alex, you're up next, man.

00:23:56 - Alex
What's going on?

00:23:58 - Alex
Hey, how you doing, guys?

00:23:59 - Alex
Really cool stuff.

00:24:00 - Marc Juretus
Mark.

00:24:00 - Marc Juretus
Thank you.

00:24:02 - Alex
So yeah, in my side, I finally got to do some editing, learning, and launched my first video of the YouTube channel.

00:24:14 - Brandon Hancock
Hey, congrats.

00:24:15 - Brandon Hancock
How can I find you?

00:24:17 - Alex
Yeah.

00:24:18 - Alex
I just shared it.

00:24:20 - Alex
It's a Spanish version of Brandon, but of course I'm starting with the very easy stuff.

00:24:25 - Alex
This is a notebook LM tutorial, following all your teachings from your personal brand AI, I think.

00:24:40 - Alex
Of course, you know, it was a lot of learning curve now.

00:24:45 - Alex
Let's see how it goes.

00:24:47 - Alex
Yeah, yeah.

00:24:48 - Alex
It's been very interesting.

00:24:49 - Alex
I ended up doing OBS for recording and CapCut.

00:24:52 - Alex
So I'm just editing myself just to get the flow and try to understand what's happening.

00:24:59 - Brandon Hancock
Dude, you already got four...

00:25:00 - Brandon Hancock
Mike, it's happening in real time.

00:25:04 - Alex
My wife and my mom.

00:25:06 - Brandon Hancock
No, hopefully you guys know.

00:25:08 - Brandon Hancock
time.

00:25:09 - Brandon Hancock
Yeah.

00:25:10 - Alex
Yeah.

00:25:10 - Alex
So, yeah.

00:25:11 - Alex
It's awesome.

00:25:12 - Alex
Yeah.

00:25:12 - Alex
It's actually very, very enjoyable.

00:25:15 - Alex
And hopefully, like, you know, keep them, keep getting the flow.

00:25:20 - Alex
And I think my question would be now that it's like out, like I actually just released it like a few minutes ago.

00:25:28 - Alex
So, what do you recommend in terms of flow?

00:25:30 - Alex
Because, like, of course, I have a lot of, like, 10 ideas of what could be my next ideas.

00:25:35 - Alex
What do you recommend every week, every two weeks?

00:25:40 - Brandon Hancock
No, great question.

00:25:41 - Brandon Hancock
So, I mean, the short answer is just the more the better.

00:25:47 - Brandon Hancock
Just because, like, what you're trying to do is just wait, like, keep producing videos until something hits.

00:25:51 - Brandon Hancock
And then once something hits and, like, takes off, you're like, okay, well, like, I'm now fully vested in, like, this topic, you know?

00:25:59 - Brandon Hancock
So, 10.

00:26:00 - Brandon Hancock
10 out of 10 would recommend just as many as you can, like minimum one a week.

00:26:04 - Brandon Hancock
If you can do more, fantastic.

00:26:06 - Brandon Hancock
The first few videos are the hardest, and then eventually you're going to get to the point to where you can, eventually you get to the point to where you can, you know, go turn through much faster.

00:26:16 - Brandon Hancock
I don't have time today, but tomorrow afternoon, I can do a quick little loom video over it with just a few pointers.

00:26:22 - Brandon Hancock
So just shoot me a DM to remind me, but yeah, I'd be happy to do like a, just a quick review with like a few pieces of feedback on the video and title and all the stuff, so.

00:26:32 - Brandon Hancock
I would appreciate that a lot.

00:26:35 - Brandon Hancock
Congrats, man.

00:26:36 - Brandon Hancock
The first one's the hardest.

00:26:37 - Alex
So you did it.

00:26:38 - Brandon Hancock
That's awesome.

00:26:39 - Alex
End to end, you did it.

00:26:40 - Brandon Hancock
That's amazing.

00:26:40 - Brandon Hancock
Absolutely love it.

00:26:41 - Alex
Congrats.

00:26:42 - Alex
Yeah, yeah.

00:26:42 - Alex
You know, maybe later on I get some people to edit or stuff, but so far it's been actually a very cool experience.

00:26:49 - Alex
Maybe start some agents, you know, in a couple of weeks, but I wanted to start with easy stuff first.

00:26:56 - Brandon Hancock
No, that's awesome.

00:26:57 - Alex
That's awesome.

00:26:58 - Brandon Hancock
Well, yeah, please, yeah, just shoot me a DM tomorrow.

00:27:00 - Brandon Hancock
That's a quick reminder.

00:27:01 - Brandon Hancock
Awesome.

00:27:02 - Alex
Thank you very much.

00:27:02 - Brandon Hancock
again, man.

00:27:03 - Alex
Thanks.

00:27:05 - Brandon Hancock
Perfect.

00:27:06 - Brandon Hancock
All right.

00:27:06 - Brandon Hancock
Next up, Juan, what's going on, man?

00:27:09 - Juan Torres
What are we working on?

00:27:12 - Juan Torres
Hey, I was able to successfully launch the ETL data pipeline through Airflow, Apache Airflow, finally.

00:27:22 - Brandon Hancock
Hey, congrats.

00:27:23 - Brandon Hancock
I know that is no small feat.

00:27:24 - Brandon Hancock
There's a lot of moving parts to that.

00:27:27 - Juan Torres
Man, yes.

00:27:28 - Juan Torres
So you were just talking about the permissions, the roles.

00:27:32 - Juan Torres
I mean, that thing, I already figured that out.

00:27:34 - Juan Torres
But the thing is that, essentially, if I actually may share my screen.

00:27:40 - Brandon Hancock
Oh, yeah, go ahead.

00:27:42 - Juan Torres
Let me send a request.

00:27:44 - Juan Torres
And then, let me see, where is my?

00:27:49 - Brandon Hancock
And real quick while you're pulling that up.

00:27:51 - Brandon Hancock
Yeah, so just to share with everyone, in case you haven't used Airflow before, it's like the OG, OG N8N, meaning like, in the past when you wanted, like, Max.

00:28:00 - Brandon Hancock
Thank

00:28:00 - Brandon Hancock
Step one, two, three, four, five to happen.

00:28:02 - Brandon Hancock
It's pretty much like Apache Airflow is like how you do it.

00:28:05 - Juan Torres
Yeah.

00:28:05 - Juan Torres
Yeah.

00:28:06 - Juan Torres
So this is, can you, can you all see my, my, my screen?

00:28:10 - Brandon Hancock
Yep.

00:28:10 - Brandon Hancock
Looks great.

00:28:12 - Juan Torres
Yeah.

00:28:12 - Juan Torres
So this is, um, and this is hosted by, uh, AWS it's called, uh, manage, uh, workflow, Apache Airflow.

00:28:24 - Juan Torres
So this is actually managed by, uh, AWS.

00:28:27 - Juan Torres
And so the launching of the ETL data pipeline in a local environment, it's not a problem really.

00:28:35 - Juan Torres
Uh, it's really easy now with, uh, agentic IDEs to construct an ETL data pipeline that goes along with your front end application.

00:28:44 - Juan Torres
And then even able to connect it to, uh, the PostgreSQL database, uh, you know, hosted in the cloud-based RDS environment with AWS was relatively easy.

00:28:57 - Juan Torres
And it was easy to give access to teammates in the project.

00:29:00 - Juan Torres
SO.

00:29:00 - Juan Torres
private.

00:29:00 - Juan Torres
SO.

00:29:00 - Juan Torres
Thank

00:29:00 - Juan Torres
Just by asking for the IP address, and then I input that as an inbound rule for my RDS database.

00:29:07 - Juan Torres
But what's really hard is the connectivity between the two applications.

00:29:14 - Juan Torres
And this is a good graph.

00:29:15 - Juan Torres
Can you guys see the diagram here?

00:29:18 - Brandon Hancock
Not yet.

00:29:18 - Brandon Hancock
I think it's just one screen.

00:29:21 - Juan Torres
Yeah, it's this one.

00:29:25 - Brandon Hancock
All I see is NYC animal complaints.

00:29:29 - Juan Torres
Oh, see.

00:29:30 - Juan Torres
Probably it's, yeah, it's based on the screen.

00:29:34 - Juan Torres
Let me see if I can change it to whole screen.

00:29:39 - Juan Torres
There we go.

00:29:40 - Juan Torres
Can you guys see it now?

00:29:42 - Brandon Hancock
Yes.

00:29:46 - Juan Torres
Is that a yes or a no?

00:29:48 - Brandon Hancock
Yes, yes.

00:29:49 - Brandon Hancock
Thank you.

00:29:52 - Brandon Hancock
Yeah, it's covered by Fathom, but the general gist of it.

00:29:56 - Juan Torres
Okay, so let me take it off.

00:29:59 - Juan Torres
So this one.

00:30:00 - Juan Torres
The Airflow Web UI can be managed by an AWS managed BPC.

00:30:06 - Juan Torres
And what a BPC, it's a virtual private cloud.

00:30:10 - Juan Torres
And this is like supposed to work in itself, but there's specific permissions that you have to give to your RDS post-sacral database.

00:30:21 - Juan Torres
And so what I had to do is move the Airflow Web UI, the Airflow environment, into a BPC that I was able to use.

00:30:33 - Juan Torres
So the change in diagram is really this.

00:30:36 - Juan Torres
So now instead of being in a different BPC, virtual private cloud, it's in the same BPC as my Amazon RDS post-sacral SQL database.

00:30:45 - Juan Torres
So they can connect directly.

00:30:48 - Juan Torres
And my Amazon Airflow environment can directly flow information into my RDS post-sacral database.

00:30:58 - Brandon Hancock
You're a full-blown infrastructure.

00:31:00 - Brandon Hancock
Structure guy now, man.

00:31:01 - Brandon Hancock
This is beautiful.

00:31:03 - Juan Torres
Yeah, no, it's a, and the reason that I wanted to do, instead of use Supabase, I wanted to use RDS, AWS directly, because I know that for future projects, I'm going to need the flexibility of having to work directly with AWS.

00:31:23 - Juan Torres
There may have been some benefits to working with, like, database infrastructure, front-end management, you know, interfaces like Supabase, but for now, I do want to deal directly with the monster, with the behemoth of AWS.

00:31:40 - Brandon Hancock
Real quick.

00:31:41 - Brandon Hancock
The only, if you, I know I took an AWS course, Maxim, if you want to share real fast, did you ever find any ones that were super helpful?

00:31:51 - Brandon Hancock
I can't remember which ones you ended up taking, just to give a few tips.

00:31:55 - Maksym Liamin
Yeah, I don't have it up right now, but I can search.

00:31:58 - Maksym Liamin
I remember, it, you were sending me somewhere.

00:32:00 - Maksym Liamin
I'll look it up.

00:32:01 - Brandon Hancock
Okay.

00:32:02 - Brandon Hancock
Yeah, there's a ton of resources on that, like, are pretty affordable, but there's, like, what you were just showing, like, there's levels to it.

00:32:10 - Brandon Hancock
So I just want to, like, if you're going all in on this, just want to, like, there's a few resources that are pretty helpful on Udemy that cost, like, near nothing.

00:32:17 - Brandon Hancock
And quick other point is, like, man, seriously, like, the amount of job, like, opportunities by being able to do this that you're exposing yourself to, like, is insane.

00:32:29 - Brandon Hancock
So, like, I know you're going a lot more on LinkedIn and sharing your journey and everything.

00:32:33 - Brandon Hancock
This would be an awesome article.

00:32:35 - Brandon Hancock
Like, just like, hey, you're just documenting your journey, posting it on LinkedIn and just almost posting it as, sharing my journey, but also sharing a couple tips for the next guy.

00:32:44 - Brandon Hancock
I think you would start to see a lot of, you could start to see some traction and potentially some job opportunities.

00:32:50 - Brandon Hancock
So, yeah, I just wanted to share that because it's pretty cool.

00:32:54 - Juan Torres
No, I've been documenting by recording my whole work in...

00:33:00 - Juan Torres
if to

00:33:00 - Juan Torres
Through OBS.

00:33:01 - Juan Torres
I'm going to be publishing a video once I'm finalized with the project.

00:33:05 - Juan Torres
Awesome.

00:33:06 - Juan Torres
One last tip.

00:33:08 - Juan Torres
So actually, this transformation, this whole cloud architecture, I'm going to have to overthrow it and reinitiate it just because Amazon MWAA Airflow Environment is quite expensive.

00:33:29 - Juan Torres
So Airflow is a really great tool for carrying massive amounts of data, but it is not very affordable specifically for the kind of jobs that only have to extract hundreds, even thousands of data points.

00:33:49 - Juan Torres
So this is the only limitation that I face with MWAA.

00:33:55 - Juan Torres
But nevertheless, this is going to be included in the video because it is a really powerful tool.

00:34:00 - Juan Torres
But just wanted to let people know the limitations of this tool, because it can be limited, especially if you want to give clients the possibility of not having to spend a lot of money in maintaining ETL data pipelines.

00:34:14 - Brandon Hancock
That is very cool.

00:34:15 - Brandon Hancock
I've only had to use it when someone else was paying the bill.

00:34:19 - Brandon Hancock
So I've never had to be like, oh, like, is this expensive?

00:34:23 - Brandon Hancock
I wasn't paying.

00:34:24 - Brandon Hancock
So good to know that it is actually expensive.

00:34:27 - Brandon Hancock
So thank you for sharing that.

00:34:28 - Brandon Hancock
Yeah, that's awesome, man.

00:34:30 - Brandon Hancock
And seriously, same thing.

00:34:31 - Brandon Hancock
Whenever you post the video, to me, I'd love to watch it and hit like and subscribe.

00:34:36 - Brandon Hancock
Perfect.

00:34:37 - Brandon Hancock
Okay.

00:34:38 - Brandon Hancock
I think next up is Maxim.

00:34:41 - Maksym Liamin
What's going on, man?

00:34:41 - Maksym Liamin
Yeah, hello, hello.

00:34:43 - Maksym Liamin
It's nice to see you all, guys.

00:34:46 - Maksym Liamin
Yeah, so in my world, in my world, do you remember that I was telling you about some like biddings that we had against a couple other teams for Nissan for like voice agents project back in in April?

00:35:00 - Maksym Liamin
So we finally got a purchase order from them.

00:35:04 - Maksym Liamin
Hey, that's amazing, man.

00:35:06 - Maksym Liamin
Now we are just thinking like if we should take it because I mean we have this project and we really want to grow it and it has a lot of potential.

00:35:14 - Maksym Liamin
So we just need to see if we want to split our attention on two different ones, but it's great.

00:35:19 - Maksym Liamin
And I mean, we already have the prototype and everything is working.

00:35:22 - Maksym Liamin
So now it needs to just in a sense scale.

00:35:26 - Maksym Liamin
Yeah, and for the other stuff, for the sales component, for the main WhatsApp bot, right now we are at 3,400 users.

00:35:35 - Maksym Liamin
we're just a little like the past week.

00:35:38 - Maksym Liamin
And we are switching the pricing finally in June because before we were on kind of a development budget.

00:35:46 - Maksym Liamin
So we just had the money that we were given every month to develop the stuff.

00:35:49 - Maksym Liamin
And now we finally started charging per dealership.

00:35:52 - Maksym Liamin
So we're going to make much more money, which is great.

00:35:55 - Maksym Liamin
And we also got the green light to go to full Latin America.

00:35:59 - Maksym Liamin
So I don't have exact date.

00:36:00 - Maksym Liamin
It's yet, but we already kind of agreed and now finishing all the legal stuff so that we can expand to everything besides Brazil and Argentina.

00:36:09 - Brandon Hancock
What's amazing, I mean, seriously, just always amazing, Maxim.

00:36:12 - Brandon Hancock
What's so cool is like you're officially feeling the power of software, meaning like once the thing works once, it's literally just like add more.

00:36:21 - Brandon Hancock
And it takes no extra work, pretty much no extra work, infinite scale, but a lot more money comes in.

00:36:26 - Brandon Hancock
So it's an infinite money glitch when done well.

00:36:29 - Brandon Hancock
And you're doing it very well.

00:36:31 - Maksym Liamin
Yeah, and the most fun part is that it runs on the $5 Cloudflare worker.

00:36:37 - Maksym Liamin
And we use free credits from Superbase, free credits from Voyage AI, free stuff for other apps from Azure.

00:36:46 - Brandon Hancock
So basically as a cost is almost zero.

00:36:49 - Brandon Hancock
What's wild is, yeah, your next expense might be upgrading to a $10 a month plan instead of five.

00:36:56 - Brandon Hancock
But outside of that, yeah, like infinite scale, it's wild.

00:36:59 - Brandon Hancock
What's really cool.

00:37:00 - Brandon Hancock
I just wanted to share something.

00:37:02 - Brandon Hancock
In real time, you were learning horizontal and vertical scaling, and you're doing it the right way because too many engineers are like, I'm going to scale to the moon.

00:37:12 - Brandon Hancock
And they spend weeks building out all these Kubernetes orchestrations.

00:37:18 - Brandon Hancock
We're going all these instances.

00:37:19 - Brandon Hancock
We're going to shard all of our data.

00:37:21 - Brandon Hancock
And it's like, dude, just throw it on one computer and just pay 20 bucks a month, and it works.

00:37:25 - Brandon Hancock
So like, you know, you're doing it the natural way and just shipping, whereas a lot of developers do the opposite.

00:37:32 - Brandon Hancock
And it takes two extra months to send out version one, and they miss all the feedback loops.

00:37:37 - Brandon Hancock
So you're doing it the right way, man.

00:37:39 - Brandon Hancock
So absolutely, absolutely love it.

00:37:40 - Maksym Liamin
I just think we value simplicity too much.

00:37:42 - Maksym Liamin
I wouldn't like to dive into Kubernetes and figure it out.

00:37:46 - Maksym Liamin
Like, I really don't want to do it.

00:37:47 - Maksym Liamin
Actually, deployment stuff.

00:37:50 - Maksym Liamin
I've also been working on the YouTube video, so I already built up the app, which is basically a 5% clone of the all functionalities that we have in the app with Andrew.

00:38:00 - Maksym Liamin
Jessica, just going to use...

00:38:00 - Maksym Liamin
It's like frontend, next.js, upload your document, it goes into blob storage, backend is Python, worker plus API, so worker takes from the blob storage, compares it into the database, sees that it's a new file, process it with Azure document intelligence, then does a summary with Azure OpenAI, and the API is just, you can regenerate the summary.

00:38:20 - Maksym Liamin
So very, very easy, like just live coded initially in like three hours, and then already deployed it also, but now finally, it took me also like a lot of hours to just deploy it again, but now I have all my comments recorded, like I have written them down, so now I'm already kind of recording each step, so redeploying again with already step-by-step kind of explanations.

00:38:42 - Brandon Hancock
What I'm very excited to see is when you record, what's so funny, because like this is going be a longer video, it's going to be packed with an insane amount of knowledge, but it's going to be a longer video, you'll have to report back on energy level, because like hour zero, the hour two, like the first hour you're like, hell yeah, like.

00:39:00 - Brandon Hancock
I'm going to crank this out, but by like, in your case, it might be three hours.

00:39:03 - Brandon Hancock
It could be four, depending on like really how deep you go.

00:39:05 - Brandon Hancock
By hour four, you're like, all right, guys, again, we're like, you know, like, it's just a straight decline.

00:39:11 - Brandon Hancock
So you'll have plenty of coffee to keep the energy levels high, but I'm very excited to see the video when you record it.

00:39:17 - Brandon Hancock
Quick question.

00:39:18 - Brandon Hancock
Also, if you don't mind sharing, just high level on the voice agent, what would it get to do?

00:39:26 - Brandon Hancock
Or just like, you know, not how you would build it, but just like, what would, what would it do?

00:39:30 - Maksym Liamin
It's actually literally the stuff that you built in your recent ADK video.

00:39:35 - Maksym Liamin
Just, I mean, when we were doing it, it was not there yet still, but it's basically for confirming the appointments for test drive.

00:39:43 - Maksym Liamin
So it takes a lot of human power to just confirm the appointments or if people have some questions that are like very little.

00:39:50 - Maksym Liamin
So we will, but like primary goal is just to call right after somebody booked it on the web page or anywhere else on the, so from the social media form.

00:40:00 - Maksym Liamin
to check

00:40:00 - Maksym Liamin
Confirm it, and then maybe call them one day before and remind them.

00:40:04 - Brandon Hancock
So this is kind of the main function.

00:40:07 - Brandon Hancock
Okay, no, that's awesome.

00:40:08 - Brandon Hancock
Yeah, think that definitely is going a little bit deeper just because voice agents were like, setting up the actual call infrastructure would probably be harder.

00:40:17 - Maksym Liamin
Yeah, here the interface is harder than the actual development.

00:40:21 - Maksym Liamin
Yeah, mean, yeah, that is the hard thing.

00:40:23 - Maksym Liamin
Getting all the numbers.

00:40:25 - Brandon Hancock
Getting all the compliance to make robotic calls.

00:40:28 - Brandon Hancock
At least in America, there are quite a few applications that take time.

00:40:33 - Brandon Hancock
They don't cost an insane amount, but they just take time to get approval.

00:40:36 - Brandon Hancock
So, yeah, very cool project.

00:40:40 - Brandon Hancock
Please keep me in the loop.

00:40:41 - Brandon Hancock
I think that one's very exciting.

00:40:42 - Maksym Liamin
Yeah, sure.

00:40:43 - Maksym Liamin
I'll let you know if we jump on it.

00:40:44 - Maksym Liamin
If yes, then as soon as I have already a more kind of prod versions, then I will demo it again here.

00:40:50 - Brandon Hancock
Oh, yeah.

00:40:51 - Brandon Hancock
All right, man.

00:40:51 - Brandon Hancock
Keep doing all the awesome projects.

00:40:52 - Maksym Liamin
I also brought another friend of mine here on the call.

00:40:56 - Maksym Liamin
So he is also my neighbor.

00:40:58 - Maksym Liamin
He lives here in Germany with me, basically.

00:41:00 - Maksym Liamin
Basically in the same building, it's Alexander, they're on the call, like I think that the order will go to him and he'll present himself, but yeah, just wanted to let you know, guys, that it's one of my players.

00:41:13 - Brandon Hancock
He didn't want to walk over one room and come back?

00:41:16 - Maksym Liamin
Awesome.

00:41:18 - Brandon Hancock
Well, Rufus, Alexander, if you want to go, and then Jake, we'll go right after this to keep things.

00:41:24 - Brandon Hancock
Alexander, if you want to hop on, welcome, welcome, man.

00:41:27 - Brandon Hancock
How are you doing?

00:41:28 - Alex
Good evening, I'm Alexander, and I only start to do something with programming, so now I'm writing in Python, and in Studium Kolek, I learn in Studium Kolek in Germany, and only in Informatic, only Java, and and

00:42:00 - Alex
I'm very bad in Java, but I try to learn this language also, and I think Python is the best language for me now, and I try to write something in Python.

00:42:16 - Alex
For example, now I write in a bot, Telegram for Telegram, and...

00:42:24 - Brandon Hancock
What do you try to get the bot to do?

00:42:27 - Brandon Hancock
Is it, like, enter, like, use AI with the bot, or what you thinking about doing?

00:42:33 - Alex
Bots can use AI, yes.

00:42:36 - Alex
I try to make a music bot that can...

00:42:43 - Alex
For example, I can write some words from text from the song, and this bot can search the song, and now then people can download, find text from from the make a playlist, also...

00:43:00 - Alex
I tried to make different effects on music.

00:43:06 - Alex
Now, today, I developed a new function.

00:43:14 - Alex
Now we can upload the sound and then do some remix with different options.

00:43:25 - Alex
Hi-fi, low speeds and other options.

00:43:29 - Alex
And this week or next week, I want to make an with Suno, one AI for music.

00:43:41 - Alex
I want to connect with a bot for creating some music in this bot, yes.

00:43:52 - Brandon Hancock
Real quick, I just wanted to call out two things.

00:43:55 - Brandon Hancock
Because I was watching the Google I.O.

00:43:58 - Brandon Hancock
today.

00:43:59 - Brandon Hancock
And they...

00:44:00 - Brandon Hancock
Launched a new thing called Lyra 2.

00:44:05 - Brandon Hancock
I think this is, let me just share my screen really fast.

00:44:09 - Brandon Hancock
But yeah, if you're kind of getting into AI and music.

00:44:13 - Brandon Hancock
Yeah, that's Toro and Moa, right?

00:44:15 - Alex
At the beginning?

00:44:17 - Brandon Hancock
I cannot remember.

00:44:20 - Alex
Okay.

00:44:23 - Brandon Hancock
But yeah, I think it's, can you try it in the studio?

00:44:27 - Brandon Hancock
Maybe, let me, one second, I'll switch accounts.

00:44:30 - Brandon Hancock
But yeah, I just, if you're, if you're starting to play more with music, I think Lyra would be something pretty cool.

00:44:37 - Brandon Hancock
Like, just came out, but yeah, if you're just looking for more ideas, yeah, for whatever reason, it's not, I don't know why it's taken so long to come out, but it should be, yeah, Models, Lyra is their music one.

00:44:52 - Brandon Hancock
Yeah, because they have Image Gen, which they made the third one.

00:44:56 - Brandon Hancock
Then Lyra is their music one.

00:44:58 - Brandon Hancock
But yeah, if you get a chance to watch the Google.

00:45:00 - Brandon Hancock
I.O.

00:45:00 - Brandon Hancock
event.

00:45:01 - Brandon Hancock
You might get to see how they're doing it, too.

00:45:03 - Brandon Hancock
So just more cool AI tools to play with as you're experimenting.

00:45:08 - Brandon Hancock
I'll drop a link in the chat so you can see this as well.

00:45:12 - Brandon Hancock
Of course, man.

00:45:13 - Brandon Hancock
No, that's awesome.

00:45:15 - Brandon Hancock
Well, if we can ever help with anything, please let us know.

00:45:19 - Brandon Hancock
There's so many cool things happening.

00:45:21 - Brandon Hancock
Love to see more people, A, going and learning about Python, how to use it with AI, every part about it.

00:45:29 - Brandon Hancock
Love to, let me know if there's anything I can ever help with.

00:45:31 - Brandon Hancock
Always, you know, always want to make sure people are learning about the goodness of AI.

00:45:36 - Alex
That's cool.

00:45:38 - Brandon Hancock
Awesome.

00:45:39 - Brandon Hancock
Awesome.

00:45:39 - Brandon Hancock
Well, thank you so much.

00:45:40 - Brandon Hancock
And also great to meet you.

00:45:42 - Brandon Hancock
Maxim, I love that you are, you, you, Cyril, you brought him in.

00:45:47 - Brandon Hancock
You have built up an army of local nerds that you are bringing in the call.

00:45:52 - Brandon Hancock
So I appreciate it.

00:45:53 - Maksym Liamin
As soon as hear somebody talking to me that they built some app themselves, so they start getting into coding.

00:46:00 - Maksym Liamin
I immediately tried to get them in.

00:46:02 - Maksym Liamin
I just need to see the enthusiasm, and then I started to give.

00:46:06 - Brandon Hancock
That's awesome, man.

00:46:07 - Brandon Hancock
Well, thank you, Maxim.

00:46:08 - Brandon Hancock
You get a referral fee for the price to join the community.

00:46:12 - Maksym Liamin
Unfortunately, it is free, but I would give you a referral.

00:46:17 - Brandon Hancock
That's awesome.

00:46:19 - Brandon Hancock
All right, perfect.

00:46:20 - Brandon Hancock
Jake, you are up next, man.

00:46:25 - Jake Maymar
Okay, so not much to report.

00:46:29 - Jake Maymar
Still in the weeds.

00:46:33 - Jake Maymar
Making some good progress.

00:46:34 - Jake Maymar
Really looking forward to showing what I'm working on.

00:46:38 - Jake Maymar
It's a lot of, like, prompt engineering, which is kind of interesting.

00:46:44 - Jake Maymar
Like, really sort of dialing in sort of the customization of the...

00:46:51 - Jake Maymar
I mean, essentially, it's just a chat bot.

00:46:54 - Jake Maymar
But the funny thing is, is really trying to dial it.

00:47:00 - Jake Maymar
Dial it in and make it as accurate as possible, which is kind of interesting.

00:47:04 - Brandon Hancock
Which model are you using right now?

00:47:07 - Jake Maymar
Well, it's kind of interesting.

00:47:09 - Jake Maymar
It's a whole bunch of different models.

00:47:10 - Jake Maymar
Some of it is Claude Sonnet.

00:47:13 - Jake Maymar
Some of it's 4.0 Mini.

00:47:15 - Jake Maymar
Some of it's 4.1.

00:47:17 - Jake Maymar
I mean, I'm using different models for different, like, sort of tool calls, essentially, and cost and performance.

00:47:26 - Jake Maymar
One of the biggest problems is performance.

00:47:30 - Jake Maymar
And trying to figure out how to kind of sort of clean up the process so I don't have to use as many models.

00:47:39 - Jake Maymar
But right now we're just trying to get it to, it's fairly complex.

00:47:45 - Jake Maymar
And the whole point is to sound not like one person, but sound like a collection of people.

00:47:52 - Jake Maymar
And those people are actually vetting the process.

00:47:56 - Jake Maymar
So it's actually hard because it's not me vetting.

00:48:00 - Jake Maymar
It's like, well, it sounds like that person.

00:48:02 - Jake Maymar
But then when you give it to that person and they run through it, they're like, well, it doesn't sound like me.

00:48:07 - Brandon Hancock
Wait, for the Reddit?

00:48:09 - Brandon Hancock
The Reddit?

00:48:10 - Brandon Hancock
Is that the torture or something different?

00:48:12 - Jake Maymar
Totally different.

00:48:13 - Jake Maymar
Yeah.

00:48:13 - Jake Maymar
Now it's a different thing.

00:48:19 - Jake Maymar
It's sort of like, it's kind of hard to explain, but it's sort of like a support group.

00:48:27 - Jake Maymar
where you go and you talk to these people and these people are very recognizable.

00:48:36 - Jake Maymar
And so they have a certain sort of personality and profile and like just the way they interact with the individual is very recognizable.

00:48:54 - Jake Maymar
And so it's a group of people, and that's what's actually really hard.

00:48:58 - Jake Maymar
If it's dialed into one person, that's.

00:49:00 - Jake Maymar
not easy, but it's fairly doable.

00:49:02 - Jake Maymar
It's just trying to get a full separation of the people.

00:49:08 - Jake Maymar
I hope I'm not being too vague.

00:49:10 - Brandon Hancock
was trying to say what it is.

00:49:14 - Jake Maymar
It's still in the works, so I can't really share anything yet.

00:49:18 - Jake Maymar
And yeah, there's some other stuff to it.

00:49:21 - Jake Maymar
But yeah, it's interesting.

00:49:23 - Jake Maymar
It's a very interesting thing.

00:49:24 - Jake Maymar
There is a voice element to it, like a live in labs kind of thing.

00:49:29 - Jake Maymar
But even that isn't really doing what we want.

00:49:32 - Jake Maymar
Actually, love to know if anyone has success with emotions, doing voice and emotions.

00:49:41 - Brandon Hancock
Um, where is he?

00:49:44 - Brandon Hancock
Is he on the call?

00:49:48 - Brandon Hancock
No, I was trying to figure out, um, where is he at?

00:49:53 - twell
I would say, okay, I cannot, um, what's right?

00:49:58 - twell
Sesame.

00:50:00 - Brandon Hancock
No.

00:50:00 - Brandon Hancock
Not Sesame, Richard.

00:50:02 - Brandon Hancock
was thinking, Richard, he is probably the most experienced when it comes to doing anything with voice.

00:50:07 - Brandon Hancock
So I was looking for Richard to see if he was on, but I don't see him today.

00:50:12 - Brandon Hancock
But no, he, I mean, he, because he's experimented with all of them.

00:50:15 - Brandon Hancock
He's done 11 labs, he's done OpenAI, and he's experimented, and I think one other one.

00:50:21 - Brandon Hancock
And then, oh, and then Sesame.

00:50:23 - Brandon Hancock
Okay, now I understand why you said Sesame.

00:50:25 - Brandon Hancock
And then Sesame is another tool that is also super, super powerful.

00:50:31 - Brandon Hancock
Would 10 out of 10 recommend, I saw a demo of it, but I haven't got to play with it.

00:50:35 - Brandon Hancock
But those are the three right now.

00:50:37 - Brandon Hancock
From my understanding, from my understanding, he ended up going out with, I think he did 11.

00:50:47 - Brandon Hancock
No, he did OpenAI.

00:50:49 - Brandon Hancock
I think he had the best luck with OpenAI.

00:50:50 - Brandon Hancock
So just, but yeah, Richard would be the man to ping if you have any like specific questions.

00:50:55 - Jake Maymar
Yeah, the thing I was, we are using OpenAI.

00:51:00 - Jake Maymar
Advanced voice.

00:51:01 - Jake Maymar
But it's, it's, it's not doing the emotions.

00:51:05 - Jake Maymar
It says the emotions, but it's not doing, not consistently doing the emotions.

00:51:10 - Jake Maymar
That's a problem.

00:51:10 - Jake Maymar
Like we want it to like, actually, like act a certain way.

00:51:16 - Jake Maymar
But a lot of times it will, sometimes it will act a certain way, but sometimes it will say, I'm sad.

00:51:22 - Jake Maymar
The person acts, you know, and it will like, basically say the emotion that, that it's supposed to be doing.

00:51:29 - Maksym Liamin
Yeah, actually the Sesame that already got mentioned is very good because we, we right now, like the demos that we have, it works with 11 labs.

00:51:36 - Maksym Liamin
And I mean, it's, it's pretty good.

00:51:38 - Maksym Liamin
But if you compare it to Sesame, it's not even close.

00:51:42 - Maksym Liamin
Yeah.

00:51:42 - Maksym Liamin
So it, it, it transfers emotions like really, really well.

00:51:46 - Maksym Liamin
So I would recommend test it out if that's, if that's the important part.

00:51:49 - Jake Maymar
Yeah.

00:51:50 - Jake Maymar
Yeah.

00:51:50 - Jake Maymar
We definitely have that on list.

00:51:51 - Jake Maymar
So let me, let me try that out.

00:51:53 - Jake Maymar
Thank you.

00:51:54 - Jake Maymar
That's very, very helpful.

00:51:56 - Brandon Hancock
Yeah.

00:51:56 - Brandon Hancock
And I'm trying to find a video for you.

00:52:00 - Brandon Hancock
I, uh, Simon, I'm gonna butcher his name, uh, Hoiberg, he, I'll just drop his channel, and then I'll try and share the video, but he made one that, uh, probably one of the most straightforward videos I've seen on, like, he was trying to replicate himself, basically, and he created his own basic, you know, Simon Ghost Rider, and it was one of the best videos I've seen on someone showcasing how to actually do a knowledge base and a, like, a trained LLM.

00:52:29 - Brandon Hancock
So, in your case, it sounded like you were having a lot of issues with people, the AI not sounding like a person.

00:52:34 - Brandon Hancock
He did a pretty good one, um, he did a pretty good one to, like, showcase actually how to do it.

00:52:41 - Brandon Hancock
You could probably, I, I cannot find it off the top of my head, I'm trying to look at this channel right now.

00:52:47 - Brandon Hancock
If I see it, I will let you, let you know, but, uh.

00:52:50 - Jake Maymar
Okay, yeah, I'll hunt through that.

00:52:51 - Jake Maymar
Thank you so much.

00:52:53 - Brandon Hancock
Um, I think he, I think it was this one.

00:52:58 - Brandon Hancock
I'm not sure.

00:52:59 - Brandon Hancock
Um,

00:53:00 - Brandon Hancock
I'm not sure, but basically, the whole model of the video was like, hey, I used to have to hire a team.

00:53:06 - Brandon Hancock
I don't now.

00:53:07 - Brandon Hancock
I just use AI to replace what would have been a team.

00:53:12 - Brandon Hancock
So I think it's that one that I just sent you, and then he talks about it in there.

00:53:15 - Jake Maymar
So pretty cool example.

00:53:16 - Jake Maymar
Nice.

00:53:17 - Brandon Hancock
Nice.

00:53:18 - Jake Maymar
Thank you.

00:53:19 - Jake Maymar
Yeah, now, just kind of mostly in the weeds right now.

00:53:24 - Jake Maymar
And the other side of it is it takes a long time to eval, because the person goes out, they run through all the different sort of test scenarios.

00:53:35 - Jake Maymar
And we record them doing it with their feedback.

00:53:39 - Jake Maymar
And then we go back and we transcribe all that to just kind of get the evals going faster.

00:53:45 - Jake Maymar
But yeah, that whole process just takes right now, it just takes too long.

00:53:50 - Jake Maymar
So we're trying to figure out how to how to get that better.

00:53:55 - Brandon Hancock
Well, it sounds like you're cruising, though.

00:53:57 - Brandon Hancock
So the second you have a demo, love to see it next week.

00:54:00 - Brandon Hancock
Whenever it's ready, man, love a demo.

00:54:02 - Jake Maymar
Yeah, definitely, definitely.

00:54:04 - Jake Maymar
Yeah, I'm looking forward to that as well.

00:54:08 - Brandon Hancock
That's awesome.

00:54:10 - Brandon Hancock
Okay, perfect.

00:54:12 - Brandon Hancock
Well, if nothing else, Asako, you are up next.

00:54:18 - Brandon Hancock
What's going on?

00:54:20 - Brandon Hancock
The other day, I know you talked about ADK.

00:54:24 - Brandon Hancock
Are we still going into ADK or what's going on?

00:54:26 - asako
Yeah, so I have two projects.

00:54:31 - asako
One is the one that Brandon just mentioned.

00:54:35 - asako
I'm going to share my screen.

00:54:41 - asako
Do you see my screen now?

00:54:44 - asako
Which is the dashboard?

00:54:46 - asako
Yeah, so I started building a dashboard for my research work.

00:54:51 - asako
What I'm doing right now is to provide an article, Google slide, and then social...

00:55:00 - asako
So media contents for investors who are interested in AI startups, so I'm making those contents about AI startups, but right now there are a lot of manual work, like copy and paste company information from spreadsheet and then copy and paste prompt from Google Docs.

00:55:21 - asako
And so I want to automate everything, and then eventually I want to sell the system to my employer.

00:55:31 - asako
Yeah, so it's Japanese, so you maybe have to understand, but it will pull all the URL and then pass those information to LLM.

00:55:46 - asako
And then my employer wanted to use multiple LLM to avoid hallucination, so generate output from multiple LLMs and then combine those.

00:56:00 - asako
And then based on the generate combined report we are making, I want to make an article in Google slide and in social media content.

00:56:13 - asako
Yes, but I'm thinking about three steps for this project.

00:56:19 - asako
For my MVP, I want to focus on text content generation.

00:56:24 - asako
And then for the second step, I want to generate slide.

00:56:27 - asako
And then third, as a third step, I want to retrieve company information automatically using agent.

00:56:38 - asako
For example, if you put the company name and it will pull funding from Crunchbase and then something like that.

00:56:46 - asako
And then text content generation seems to be pretty straightforward.

00:56:51 - asako
But I feel like slide generation is hard.

00:56:57 - asako
Like how to...

00:56:59 - asako
...

00:57:00 - asako
Get the images and then format, like crop and scale so that it will fit in the template.

00:57:08 - Brandon Hancock
Yeah, I haven't planned it yet.

00:57:11 - asako
I'm thinking about just thinking, plan it on the fly, but yeah, that's where I'm thinking about using some sort of agent.

00:57:20 - asako
And then Bastian actually suggested me to use browser base, which is like a computer use agent.

00:57:28 - asako
So I'm thinking about playing around with it to do that.

00:57:32 - asako
But yeah, that's where I'm.

00:57:35 - Brandon Hancock
No, that's awesome.

00:57:36 - Brandon Hancock
That's awesome.

00:57:36 - Brandon Hancock
So a few just like ideas.

00:57:39 - Brandon Hancock
So I have looked at a bunch of like AI slides because I just needed to make a bunch of like presentations.

00:57:47 - Brandon Hancock
I have yet to find one that does a good job.

00:57:50 - Brandon Hancock
Like, so I'm curious if anyone has any like AI slide tool that they've used that like does good work.

00:57:57 - Brandon Hancock
I mean, I'd be curious to see it and try it myself.

00:57:59 - Brandon Hancock
But

00:58:00 - Brandon Hancock
Um, I feel like if, once someone does crack that code, it's going to be wild because the amount of people that have to make slides for presentations, I mean, professionally and for side projects and everything, it's, it's wild.

00:58:11 - Brandon Hancock
So if you do find a good one, let me know.

00:58:13 - Brandon Hancock
I just haven't seen one yet.

00:58:15 - Brandon Hancock
And I think it's because of the complexity you were just mentioning, which is like playing out the content per slide, then making graphics, putting the graphics in the right spot, making them the right size.

00:58:25 - Brandon Hancock
It's it's kind of very hard and manual.

00:58:28 - Brandon Hancock
So, um, yeah, would, would be very curious to, to like, see what you ended up finding on that one because slides are hard, very hard.

00:58:37 - asako
Yeah, that's what I was assuming.

00:58:41 - asako
And what was the, what was the browser-based agent for?

00:58:45 - asako
Um, it's to, um, take a screenshot, um, from website.

00:58:50 - asako
Um, like if I give, uh, website ULN and they all automatically find relevant content and then, uh, take a screenshot from there.

00:58:59 - asako
Um.

00:59:00 - Brandon Hancock
Okay.

00:59:01 - asako
Yeah, I'm not sure if it's possible to crop images and then process complicated things, but yeah.

00:59:10 - Brandon Hancock
Yeah, that one is harder.

00:59:14 - Brandon Hancock
I mean, it's definitely doable, but yeah, there's just an insane amount of like, okay, so what is the current goal?

00:59:21 - Brandon Hancock
It's to make this slide.

00:59:22 - Brandon Hancock
What am I trying to do in this slide?

00:59:24 - Brandon Hancock
This image.

00:59:24 - Brandon Hancock
This image is too big.

00:59:26 - Brandon Hancock
Adjust.

00:59:26 - Brandon Hancock
Okay, now try it again.

00:59:27 - Brandon Hancock
Adjust.

00:59:27 - Brandon Hancock
So they're just like an insane amount of small loops that have happened over and over and over again.

00:59:33 - Brandon Hancock
I did, this is like not 100% what you're trying to do, but like maybe a PowerPoint assister you could look at doing.

00:59:43 - Brandon Hancock
There was a, from ADK, they made a cool demo to where they added a browser agent to their, basically to their, to their agent.

00:59:52 - Brandon Hancock
So they could just chat and then the agent would go off and do stuff on the internet and report back.

00:59:56 - Brandon Hancock
So, um, I don't know if that one could be helpful.

01:00:00 - Brandon Hancock
I'll have to find it and send it.

01:00:03 - Brandon Hancock
So it was on the, here, let me send it to you real quick.

01:00:06 - Brandon Hancock
One second.

01:00:08 - Brandon Hancock
I watched it the other week.

01:00:10 - Brandon Hancock
Oh, yeah.

01:00:11 - Brandon Hancock
There you go.

01:00:13 - Brandon Hancock
I just went, so, if, basically, what they did is, in that video I just shared, they used ADK to control a browser agent.

01:00:22 - Brandon Hancock
So, in that one, they used Selenium, but you could also replace Selenium with BrowserBase, and it would still be just as, just as powerful.

01:00:34 - Brandon Hancock
So, definitely recommend, like, if you're starting to go down the agent and browser path, that's a really good video to get started with, if you want to combine the two.

01:00:43 - Brandon Hancock
So, something to recommend.

01:00:45 - Brandon Hancock
Any, any, any other questions we can help with or anything?

01:00:49 - Brandon Hancock
Love that you're always cranking out apps.

01:00:51 - Brandon Hancock
You are a, a pro at cranking out apps.

01:00:53 - Brandon Hancock
I love it.

01:00:54 - asako
Thank you.

01:00:55 - asako
Um, I actually have two, uh, things that, two, two challenges.

01:01:00 - asako
Yes, one is that right now I'm doing just pass the prompt and then generate the output, but I want to make it more conversational so that if there's anything that I want to make adjustment, I can ask AI to modify.

01:01:17 - Brandon Hancock
Yeah.

01:01:18 - asako
Yeah.

01:01:20 - Brandon Hancock
So there is a concept called just an AI co-pilot, and basically it's to do exactly what you're describing.

01:01:30 - Brandon Hancock
So I think it'll become more of a common thing in applications going forward, but basically it's like making the side dash bar a co-pilot, specifically like allow whenever someone clicks on anything to ask questions about it in the side bar and make changes.

01:01:47 - Brandon Hancock
The thing that's going to be hard about that is you have to start sharing global state across components, but it is doable.

01:01:55 - Brandon Hancock
Like what you could do is like right now you have the history button and the copy button you could.

01:02:00 - Brandon Hancock
Probably add a third button, which is just like a little AI robot.

01:02:02 - Brandon Hancock
And that just brings over a side window from the right that is just an agent, a chat to where you can say like, hey, I like this.

01:02:11 - Brandon Hancock
I like where it's going, but I want to incorporate this feedback.

01:02:14 - Brandon Hancock
So, but yeah, basically just a co-pilot.

01:02:16 - asako
I see.

01:02:17 - asako
I see.

01:02:19 - asako
And then once they make changes, you can display the output in the output section too?

01:02:28 - Brandon Hancock
Yeah, there's multiple options.

01:02:29 - Brandon Hancock
So, what would happen is you would pass in the input and output that you have on the left-hand side as its context to the co-pilot.

01:02:41 - Brandon Hancock
Say like, hey, here's the original input.

01:02:42 - Brandon Hancock
Here was the original output.

01:02:44 - Brandon Hancock
Then the user would submit a change, a feedback for anything.

01:02:50 - Brandon Hancock
And then once they're done, you could probably just have an apply button.

01:02:54 - Brandon Hancock
There's two options.

01:02:55 - Brandon Hancock
Manually, just click apply and it overrides it.

01:02:58 - Brandon Hancock
Actually, two, which is harder.

01:03:00 - Brandon Hancock
There's

01:03:00 - Brandon Hancock
Is you probably do some sort of tool call, I'm not sure if this is saved to a database, but I'd probably stick to the manual apply.

01:03:06 - Brandon Hancock
wouldn't go down the LLM tool call, it's just a Yeah, that makes a lot of sense.

01:03:10 - asako
Thank you.

01:03:12 - asako
yeah, and the last question is that, um, in the Google Docs, it's easy to, um, add comments, like, if, if we want to, um, if, uh, if the radio wants to change specific wording, it's, uh, it's easy to point out, but with the dashboard, I feel like it's harder.

01:03:31 - asako
So, what is the best way to, like, add comments for?

01:03:35 - Brandon Hancock
Um, yeah.

01:03:37 - Brandon Hancock
So, you want to highlight text and add comments, or what are we?

01:03:40 - asako
Yeah, yeah, yeah.

01:03:41 - asako
I'm thinking about highlight text and add a comment.

01:03:45 - Brandon Hancock
So, going down that approach, you have to start to use, like, an actual text editor, like, because, like, right now, it's, like, text.

01:03:53 - Brandon Hancock
Yeah.

01:03:53 - Brandon Hancock
But you want to, like, actually put a text editor in there.

01:03:56 - Brandon Hancock
There's a framework.

01:03:58 - Brandon Hancock
Maxim just raised his hand.

01:03:59 - Brandon Hancock
Maxim, do you remember the framework?

01:04:03 - Maksym Liamin
The one that you worked with, the one that you used, it starts with T, I forgot, no, but that's not what I wanted to say, but I mean, oh, okay, I was like, you read my mind, go ahead, Maxim, I'll look up the framework.

01:04:19 - Maksym Liamin
Yeah, it is.

01:04:20 - Maksym Liamin
So there is a great library that we use with Andrew for our project for exactly doing the highlighting and commenting stuff.

01:04:28 - Maksym Liamin
It requires a little bit more setup than the frameworks that Brandon is looking up, because there I believe it at some point becomes paid, especially if you want like nice comments and all this kind of stuff, because they also sync it with different users and allow organizations and stuff.

01:04:42 - Maksym Liamin
But if you needed more kind of simple and more control, the library is called, I think, React PDF highlighter.

01:04:50 - Maksym Liamin
And it's very easy to build on top of it, like whatever you need.

01:04:54 - Maksym Liamin
It's very easy to integrate.

01:04:56 - Maksym Liamin
I will share the link as soon as I find, but if I'm not mistaken.

01:05:02 - asako
Thank you so much.

01:05:03 - asako
I'll take a look at the link later.

01:05:09 - Brandon Hancock
I'm looking for it, and I will send it to you whenever I find it, but yeah, it is definitely in the weeds, but I mean, it allows you to do anything.

01:05:23 - Brandon Hancock
The company I worked at, TypeShare, that's what we used because we were allowing people to manually write blog posts, and when writing blog posts, you need to highlight, underline, basically feel like you're in Microsoft Word, but in a text editor, and it also had the ability to comment, and then you could make custom nodes, which would be like a comment, you know?

01:05:44 - Brandon Hancock
So you could do all of, all of that.

01:05:46 - Maksym Liamin
Keep it up, what's the name?

01:05:49 - Brandon Hancock
Tip-tap, yeah.

01:05:50 - Brandon Hancock
Thank you, Max.

01:05:51 - Maksym Liamin
Good memory.

01:05:51 - Maksym Liamin
sent the link.

01:05:53 - Maksym Liamin
Thank you.

01:05:54 - Brandon Hancock
perfect.

01:05:54 - asako
I'll take a look at those.

01:05:57 - Brandon Hancock
You can do, you can literally do anything in there, which is.

01:06:00 - Brandon Hancock
Which is nice, so we definitely recommend, if you want to go super, yeah, actually I'm just going to leave, not saying anything else, but yeah, we definitely recommend ChipTap, you can do a lot.

01:06:14 - asako
Okay, I'll play around with this, thank you.

01:06:17 - Brandon Hancock
Perfect, perfect.

01:06:18 - asako
Yeah, oh, and then lastly, it's an advertisement, but I launched a website built with, oh, I launched a podcast website, which was built with AI, two AI bilingual agents, and a new episode will be launched tomorrow, so I'm going to drop the link.

01:06:37 - Brandon Hancock
I'm going to drop the link, I'd love to see it.

01:06:39 - asako
Yeah, if anyone can take a look.

01:06:44 - asako
Thank you, Miranda.

01:06:45 - Brandon Hancock
I'm going to Japan at the end of the year, so I need to, uh, I actually need to use this one, uh, Satora and Peter, yeah, need to, I need to learn.

01:06:54 - Brandon Hancock
All right, perfect, thank you so much, all right, we're going to keep on cruising.

01:07:00 - Brandon Hancock
Uh, let's see.

01:07:02 - Brandon Hancock
Um, twell, I don't think that, yeah.

01:07:06 - Brandon Hancock
What's your, what's, what's your first name?

01:07:08 - Brandon Hancock
I cannot, uh, I cannot remember.

01:07:14 - Brandon Hancock
Um, let me look this up real fast.

01:07:20 - Brandon Hancock
Twell, um, yeah.

01:07:25 - Brandon Hancock
Um, yeah.

01:07:26 - Brandon Hancock
Um, twell, I cannot remember your first name.

01:07:29 - Brandon Hancock
Uh, is not showing it off the top.

01:07:34 - Brandon Hancock
If you don't want to, if you want to go, I cannot remember your first name.

01:07:38 - Brandon Hancock
I apologize.

01:07:40 - Brandon Hancock
Uh, yeah.

01:07:43 - Brandon Hancock
Twell, your turn, buddy.

01:07:48 - Brandon Hancock
If not, Nate.

01:07:51 - Brandon Hancock
Uh, are you, Nate?

01:07:58 - Nate Ginn
Hi.

01:07:58 - Brandon Hancock
It's been a long time.

01:07:59 - Brandon Hancock
What's going on?

01:08:00 - Brandon Hancock
You got the doctor?

01:08:00 - Brandon Hancock
Put your shirt on today.

01:08:01 - Nate Ginn
Yeah, I was, I just had to go to the office for a little bit, but anyway, I unfortunately haven't been doing a lot of programming.

01:08:13 - Nate Ginn
It's funny when you step away and you're not doing this as a profession, right?

01:08:17 - Nate Ginn
This isn't my thing.

01:08:19 - Nate Ginn
You guys, like, I'm like, oh, man, I have to relearn the language again, almost.

01:08:23 - Brandon Hancock
Like, guys, everybody's moved on.

01:08:26 - Nate Ginn
And all of all these new things you're talking about, I'm like, oh, man, I missed out.

01:08:31 - Nate Ginn
But I just, I missed hanging out with you guys, and I just wanted to say hi and let you know I was still alive and here and things like that.

01:08:40 - Nate Ginn
I don't really have much programming things going on that I've been able to work enough on.

01:08:48 - Nate Ginn
But anyway, I just wanted to say hi.

01:08:50 - Brandon Hancock
Well, hey, no, we always love seeing you, Nate.

01:08:53 - Brandon Hancock
If you, I'll give you a quick update on things that I think you would like to see.

01:08:58 - Brandon Hancock
So, crank it.

01:09:00 - Brandon Hancock
Not websites.

01:09:00 - Brandon Hancock
So at this point, Firebase just said today that they're going to make Firebase Studio like actually finally work, meaning you now can actually deploy it back in.

01:09:13 - Brandon Hancock
So the next time you want to go to create like a full stack AI application, hopefully by the time you do that, Firebase Studio will actually do the thing it says it's going to do, which means making, you know, turning your ideas into real world AI applications is going to be easier than ever.

01:09:29 - Brandon Hancock
So definitely recommend checking that.

01:09:32 - Brandon Hancock
Other just cool things.

01:09:33 - Brandon Hancock
I don't know if you've got to play with Lovable for cranking out a website.

01:09:38 - Brandon Hancock
I'm still blown away with how easy it is.

01:09:42 - Brandon Hancock
New, just like new way to like rapidly go through projects, guys, is like take the requirements document you make with your client or yourself and then a few Excalibur mockups and Lovable just cranks it out.

01:09:57 - Brandon Hancock
Like that is always the hardest part in my opinion because I'm not.

01:10:00 - Brandon Hancock
Talented graphically.

01:10:01 - Brandon Hancock
I just cannot do it.

01:10:03 - Brandon Hancock
And it's wild how well it works.

01:10:05 - Brandon Hancock
So definitely worth testing that one out too to make some cool websites and showcase to your friends like, hey, look what I can do, guys.

01:10:13 - Brandon Hancock
So those are my two new tools, shiny objects.

01:10:17 - Brandon Hancock
I recommend playing with it if get a few free moments this week.

01:10:19 - Nate Ginn
Cool.

01:10:21 - Nate Ginn
Yeah, I have been listening to, as I'm driving all over the place right now, I've been listening to your tutorials on your ADK stuff.

01:10:30 - Nate Ginn
But I haven't been able to like actually sit down and follow them like I used to do in the good old days three months ago.

01:10:37 - Nate Ginn
But they're kind of fun.

01:10:39 - Nate Ginn
I mean, I'm excited.

01:10:41 - Nate Ginn
I wish I had like a week to just say, leave me alone and just go through all of your stuff one after the other and get back into.

01:10:49 - Nate Ginn
Get back into it.

01:10:50 - Nate Ginn
I miss it.

01:10:51 - Nate Ginn
I'll tell you.

01:10:53 - Nate Ginn
Yeah, I'm like ready to give up the doctoring thing and go to programming, but it's hard to make that big of a transition.

01:11:00 - Brandon Hancock
Welcome to the dark side, man.

01:11:02 - Brandon Hancock
Welcome to the dark side.

01:11:03 - Brandon Hancock
Would absolutely love it.

01:11:05 - Brandon Hancock
A few cool things, too, just in doctor land.

01:11:09 - Brandon Hancock
Google announced today their new Jemma model is, I think they have like a medical, a specialized medical one.

01:11:17 - Brandon Hancock
You might want to look into it a little bit more, but you might be interested in running that locally.

01:11:22 - Brandon Hancock
I'd be curious to see if you notice it does better work than some of the more open ones when it comes to answering medical questions.

01:11:29 - Brandon Hancock
Let me look it up.

01:11:30 - Brandon Hancock
But yeah, they announced it today.

01:11:33 - Brandon Hancock
I think it's Jemma Med.

01:11:36 - Brandon Hancock
But yeah, they just announced it.

01:11:40 - Brandon Hancock
Yeah, here you go.

01:11:42 - Brandon Hancock
Let's see.

01:11:43 - Brandon Hancock
Well, let me.

01:11:46 - Brandon Hancock
Yeah, it's called Med Jemma is what it's called.

01:11:52 - Brandon Hancock
AI.

01:11:53 - Brandon Hancock
I'm just going to drop in the chat.

01:11:54 - Brandon Hancock
Thank you, Bastian.

01:11:55 - Brandon Hancock
Um, but it's like focused on like anything from medical.

01:12:00 - Brandon Hancock
Well, to like medical questions, like apparently it's, it's probably, it's one of the best medical models that you can run privately.

01:12:07 - Brandon Hancock
So you're not having to share data to the cloud, which is like an insane use case.

01:12:11 - Brandon Hancock
Like that's going to be insanely valuable to use.

01:12:14 - Brandon Hancock
So we definitely recommend checking that one out if you get a chance.

01:12:18 - Nate Ginn
That one is you, if you go in there, it's not, not capturing your data that you're asking.

01:12:24 - Nate Ginn
Is that what you're saying?

01:12:26 - Brandon Hancock
More specifically, you actually will be able to, it's an, correct me if I'm wrong guys, but from my understanding, it is a model that you can run locally.

01:12:33 - Brandon Hancock
So just like Llama, like you can run locally on your computer.

01:12:37 - Brandon Hancock
You, yeah, you can do it.

01:12:38 - Brandon Hancock
Or I think what they're recommending is like, as you deploy more HIPAA compliant, like if you go cloud, you can just run this one.

01:12:47 - Brandon Hancock
So the depth, the data never leaves.

01:12:50 - Brandon Hancock
So yeah, definitely recommend, definitely recommend trying, trying it out.

01:12:53 - Brandon Hancock
I'd be curious to see if you notice that, notice the difference.

01:12:56 - Brandon Hancock
In my case, I'm like, oh, I stubbed the toe.

01:12:59 - Nate Ginn
That's like the extent of my medical.

01:13:00 - Brandon Hancock
Questions right now.

01:13:01 - Brandon Hancock
So we'd love to hear from the experts.

01:13:03 - Nate Ginn
I clip my hangnail?

01:13:06 - Brandon Hancock
Yeah, it hurts.

01:13:08 - Brandon Hancock
I've been sitting too long.

01:13:10 - Brandon Hancock
Should I stand up?

01:13:11 - Brandon Hancock
Yes, I should.

01:13:13 - Brandon Hancock
I should do more.

01:13:15 - Nate Ginn
Anyway, well, thank you guys.

01:13:18 - Brandon Hancock
Yeah, of course.

01:13:18 - Brandon Hancock
Of course.

01:13:19 - Brandon Hancock
All right.

01:13:20 - Brandon Hancock
Well, yeah, hopefully you get to sneak in some developer time here.

01:13:23 - Brandon Hancock
And obviously, if I can ever help out, let me let me know.

01:13:25 - Brandon Hancock
But yeah, hopefully I don't let work drive you crazy, man.

01:13:27 - Brandon Hancock
So I know all the org changes and everything.

01:13:31 - Brandon Hancock
So hopefully it calms down soon.

01:13:33 - Brandon Hancock
So, all right.

01:13:34 - Brandon Hancock
Perfect.

01:13:35 - Brandon Hancock
All right.

01:13:36 - Brandon Hancock
Aaron, you're up next, man.

01:13:42 - The Dharma House
Hey, team.

01:13:44 - The Dharma House
Happy, as always, to be here with you guys.

01:13:47 - The Dharma House
I'm thankful that, Brandon, you're still doing it, especially given the transition you've had in the last couple of months.

01:13:57 - The Dharma House
I've asked myself, like, how long are going to keep doing it?

01:14:00 - The Dharma House
Are you going to get...

01:14:00 - The Dharma House
I'm busy with searching after the next big thing for you that this becomes a smaller part of your life.

01:14:06 - The Dharma House
Either way, I'd be happy for you.

01:14:08 - The Dharma House
You're stuck with me, actually.

01:14:10 - The Dharma House
Cool.

01:14:11 - The Dharma House
I'm along for the journey and hoping that your world's getting so busy that you do have to juggle much or build more agents one of the two.

01:14:21 - The Dharma House
Yeah, that's it.

01:14:22 - Brandon Hancock
I'm brain bot.

01:14:24 - The Dharma House
Yeah, I'll tell you guys where I am.

01:14:27 - The Dharma House
I kind of had an opportunity to shift away from Eleanor based on an opportunity to build a tool for a client.

01:14:38 - Brandon Hancock
Oh, that's awesome.

01:14:39 - Brandon Hancock
Congrats.

01:14:40 - The Dharma House
You guys can help me walk through the process of it.

01:14:42 - The Dharma House
So I had to sign some NDAs, so I got to be careful about what I can really talk about.

01:14:48 - The Dharma House
But essentially, being asked, and right now we're just in the disco.

01:14:53 - The Dharma House
The disco is always the fun part, right?

01:14:56 - The Dharma House
Figuring out whether it's something that we can do or not.

01:14:59 - The Dharma House
But being asked to...

01:15:00 - The Dharma House
Create a grant writing agent using a company's process.

01:15:04 - The Dharma House
Like, hey, we write, we think that our grants are better because we do A, B, C, D, and E to create an outstanding grant.

01:15:12 - The Dharma House
And we're wondering if we can, we feel like it's codified enough to create, to automate it.

01:15:21 - The Dharma House
And so, yeah, what I did was I did the disco with them last week, went back, and I went right to Google ADK and put it together and just kind of started to mock it up for myself.

01:15:37 - The Dharma House
Here are a couple of things that I think are a little bit sticky.

01:15:40 - The Dharma House
They want it client-facing.

01:15:41 - The Dharma House
So as opposed to it being an internal tool, which for me makes more sense for them, they want to kind of create like a new division or not necessarily a new vertical, but they're kind of thinking about this being its own product and kind of running itself and just giving like a membership-based access.

01:16:00 - The Dharma House
says to their team, because they do a lot of different things.

01:16:06 - The Dharma House
They project manage and do several different things for people and for organizations.

01:16:10 - The Dharma House
And so they want this client-facing agent.

01:16:16 - The Dharma House
And two things.

01:16:17 - The Dharma House
One, they don't know exactly how they want it to interface.

01:16:24 - The Dharma House
And so I've been thinking through giving them ideas of how to interface.

01:16:27 - The Dharma House
And also, I could really use some support in figuring out how to set up a relationship with them.

01:16:32 - The Dharma House
Because what they want is, for me, to create an agent.

01:16:37 - The Dharma House
I kind of gave them a little, I mocked it.

01:16:39 - The Dharma House
And the only trouble I had, technically, we'll talk about next.

01:16:42 - Brandon Hancock
I kind of mentioned it in the group.

01:16:44 - The Dharma House
And it's around artifacts and around Google, ADK, and document uploads.

01:16:51 - The Dharma House
I'm not sure if anybody's run into that wall yet.

01:16:53 - The Dharma House
But we can come back to it.

01:16:56 - The Dharma House
But they want, essentially, to be able to upload documents.

01:16:59 - The Dharma House
And so...

01:17:00 - The Dharma House
so...

01:17:01 - The Dharma House
And I wanted to do that without RAG, without a RAG-based system at all.

01:17:06 - The Dharma House
it's really just pure uploading of documents and then getting a product.

01:17:13 - The Dharma House
So that's one part of it.

01:17:15 - The Dharma House
Two is I thought, cool, I'll build it.

01:17:18 - The Dharma House
I'm not sure what to price it at yet, but I think it'll probably look something like I'll build it, I'll give you a license around it, and you can do whatever you want to do with it for MVP.

01:17:27 - The Dharma House
You can shift it, change it, whatever.

01:17:31 - The Dharma House
And they came back and said, well, we want to own it.

01:17:34 - The Dharma House
We don't want to license it.

01:17:35 - The Dharma House
We want to kind of work for a hire, and you build it out, and it's our product.

01:17:40 - The Dharma House
And I'm like, well, guys, it's an MVP, and, you know, it makes the most sense to keep us along the board.

01:17:45 - The Dharma House
I've done implementations, and let's walk beside you and become partners, and, you know, we can grow it.

01:17:51 - The Dharma House
And they're kind of like, well, also, we don't want you to be able to do anything like this for anybody else for a while.

01:17:56 - The Dharma House
Like, we don't want you to rebuild our product.

01:17:59 - The Dharma House
So...

01:18:00 - The Dharma House
So...

01:18:00 - The Dharma House
And that leaves me in some land where I'm unsure of, because I'm just used to seats and, you know, some licenses.

01:18:07 - The Dharma House
And like now I feel like it's a little stickier than like I really have expertise for.

01:18:11 - The Dharma House
I'm asking for support with maybe thinking through that.

01:18:14 - The Dharma House
And the other part is, it's just this Google ADK piece.

01:18:18 - The Dharma House
It's, I like it.

01:18:22 - The Dharma House
It's cool.

01:18:23 - The Dharma House
You know, I built a document ingestion agent.

01:18:26 - The Dharma House
Yeah.

01:18:27 - The Dharma House
And so I'm like, all right, do I somehow marry this to that?

01:18:32 - The Dharma House
And that's rag based, right?

01:18:33 - The Dharma House
And in this case, they don't want it rag based, especially for MVP.

01:18:38 - The Dharma House
They just kind of want to be able to upload documents.

01:18:42 - The Dharma House
And now as I play with this, I'm thinking a rag system is actually easier.

01:18:47 - The Dharma House
I've noticed that no one's really like kicking around artifacts in these videos.

01:18:51 - The Dharma House
Like, you know, it's all seem to be rag based.

01:18:54 - The Dharma House
And I think that's because I didn't the load in uploading documents.

01:19:00 - The Dharma House
Because ADK wants a conversion from a binary file, so I started to create my document ingestion agent, like a mini kind of version of that in ADK, and I'm like, is that really the thing to do?

01:19:15 - The Dharma House
Or I was talking to a couple other developers earlier this week, who were like, hey, Mistral's got this super cool, like, upload, doc upload engine, and I think Llama Index has one as well, and maybe think about going that way and outsourcing that part of it.

01:19:34 - The Dharma House
So just asking the group what you guys think about any of those things, happy to get some feedback.

01:19:42 - Brandon Hancock
Okay, so first I want to talk pricing, then NDA, and then also, like, I don't know what was signed, what was not signed, because, like, if stuff's already signed, like, like, you know, it is what it is, like, there's nothing else we can do.

01:19:56 - Brandon Hancock
So, okay, so first off, when it comes...

01:20:00 - Brandon Hancock
comes to pricing, not gonna lie, this is a big, a bigger project.

01:20:05 - Brandon Hancock
So I want to give like levels of complexity for pricing really fast, just as like rule of thumb.

01:20:10 - Brandon Hancock
Hopefully this will be helpful.

01:20:11 - Brandon Hancock
Okay.

01:20:12 - Brandon Hancock
If you're building something like super standard, like let's just imagine a rag chatbot.

01:20:17 - Brandon Hancock
Okay.

01:20:17 - Brandon Hancock
To where it's like a custom UI authentication database blob store.

01:20:23 - Brandon Hancock
And they've already done some sort of prompting on their own.

01:20:26 - Brandon Hancock
Like they build a GPT on their own to where they've got to like, oh yeah, like I have a good idea of like what I want it to do to where like, Hey, there's no more, there's no more extra thinking to do on my end.

01:20:37 - Brandon Hancock
I pretty much just have to build the app.

01:20:39 - Brandon Hancock
You know, I'd probably minimum like six, but I'd probably go closer to eight just because like, this is like a weeks, a two weeks long project.

01:20:48 - Brandon Hancock
There's going to be a lot of hiccups and everything just like actually implementing it.

01:20:52 - Brandon Hancock
So like, I would realistically go minimum eight on like a super custom UI, everything.

01:20:58 - Brandon Hancock
Okay.

01:20:59 - Brandon Hancock
So that's that one.

01:21:00 - Brandon Hancock
All right, next level, which is like, hey, they have no idea what they want to where you're not only having to be a software engineer, but you're almost having to be like, take their job and understand the process of writing it.

01:21:14 - Brandon Hancock
Like, you're doing two jobs at that point, to where you're almost like an AI adoption consultant plus an AI engineer.

01:21:23 - Brandon Hancock
For those types of projects, it's a lot more strictly because you have to take in raw requirements, understand how their job actually works, and then implement it, which is a hard question mark, because it's like, there's probably a thousand small edge cases where they're like, oh, yeah, on these documents, you do this.

01:21:40 - Brandon Hancock
And you're like, we've been working on documents together for a month, and you've never mentioned this edge case.

01:21:45 - Brandon Hancock
I have to go back and add so much stuff, like those types of projects where it's more open-ended are a lot more challenging to face and to do and implement correctly, strictly because you have to basically understand how their job works.

01:22:00 - Brandon Hancock
You're getting a second job.

01:22:02 - Brandon Hancock
For those, I mean, you're realistically like probably 20s, like just because of like, you're going to have to go be an employee almost.

01:22:11 - Brandon Hancock
And the amount of internal prompt writing that you're going to have to do and then check and evaluate, there's just a lot more to it.

01:22:18 - Brandon Hancock
So realistically pricing probably like 20 at this point.

01:22:23 - Brandon Hancock
And that's just to help.

01:22:25 - Brandon Hancock
Yeah, I would feel comfortable doing that in the 20s is what I would what I would do.

01:22:30 - Brandon Hancock
With what you've shared so far.

01:22:33 - Brandon Hancock
Yeah.

01:22:35 - Brandon Hancock
Now, yeah, so that's what that's what I would that's what I would look at probably somewhere in the 20s and then just say like, hey, I'll charge 125 per hour, whatever, whatever, whatever you want to charge for retainer afterwards, just because like there's going to be things that they won't change.

01:22:51 - Brandon Hancock
Something around there is what I would feel comfortable with to work on this.

01:22:55 - Brandon Hancock
Okay, so that's that's pricing.

01:22:57 - Brandon Hancock
Now, the other thing that.

01:23:00 - Brandon Hancock
right side you.

01:23:00 - Brandon Hancock
I'd like to mention really fast, like when it comes to the NDA, anytime someone excludes you from the ability to do anything else in the future, I charge more.

01:23:10 - Brandon Hancock
Because like, hey, like, yeah, I'm happy to do this just for you guys.

01:23:15 - Brandon Hancock
But like, you know, I'm not going to directly copy it.

01:23:18 - Brandon Hancock
But if another client comes and asks me to do it, I am going to do it for them.

01:23:22 - Brandon Hancock
But if you want you to be 100% exclusive, and I never had the ability to work on this again for an extra year or two, then like, okay, cool.

01:23:30 - Brandon Hancock
Like, we're almost like, we, um, like, we're gonna have to pay more again, you know, so just for exclusivity is basically what it comes down to.

01:23:39 - Brandon Hancock
So that's, you know, and just framing it that way of just like, hey, this is limiting my earning potential, because of what, you know, and I'm happy to do that with you guys.

01:23:50 - Brandon Hancock
But for more, you know, just because like, yeah, so I would, I would potentially phrase that as well.

01:23:58 - Brandon Hancock
Okay.

01:23:59 - Brandon Hancock
Um...

01:24:00 - Brandon Hancock
The third question was around artifacts, right?

01:24:03 - Brandon Hancock
Kind of with ADK.

01:24:05 - Brandon Hancock
All right.

01:24:06 - Brandon Hancock
Artifacts are tricky.

01:24:08 - Brandon Hancock
So I'm going to talk artifacts versus RAG.

01:24:10 - Brandon Hancock
So RAG shines when you're making queries to the same document multiple, multiple, multiple times.

01:24:18 - Brandon Hancock
Going back to the RAG chatbot, if you're going to have a thousand users all asking questions about the same document, it makes so much sense to embed it and then reuse those embeddings to help answer questions.

01:24:30 - Brandon Hancock
If it's kind of like a one-time thing of like, hey, we're making a grant around this PDF, I might ask 10, 20 questions, but then I'm done with that.

01:24:38 - Brandon Hancock
I would stick to artifacts.

01:24:40 - Brandon Hancock
I would not go RAG.

01:24:42 - Brandon Hancock
And also when it comes to the Gemini models, you know, they can easily handle a million tokens.

01:24:48 - Brandon Hancock
So you could easily fit the whole PDF in there, plus no matter how big the PDF is, you're easily going to put that in there to answer questions.

01:24:57 - Brandon Hancock
And the hard part is...

01:25:00 - Brandon Hancock
It's not just adding that artifact, it's extracting meaningful information from it iteratively over and over and over again to generate whatever, I don't know what their grant style looks like, but I would, you know, that's like the hardest part is just continually asking that same, like using a sequential agent and some loop agents to continually extract all the meaningful parts so that the next agent can then use the extracted information to start actually writing a, start writing the grant.

01:25:32 - Brandon Hancock
That's the hard part.

01:25:33 - Brandon Hancock
So, but I mean, I, I absolutely love this use case.

01:25:37 - Brandon Hancock
If you ever want help, like going deeper into an Excalibur thing, you know, always happy to hop on a call, but this is a really awesome use case.

01:25:46 - Brandon Hancock
So I think, I think there's, there's some, like learning this skill can be applied to any, almost any professional job anywhere.

01:25:55 - Brandon Hancock
So this is a very valuable skill to learn and master.

01:25:58 - Brandon Hancock
So, um, yeah, I,

01:26:00 - The Dharma House
A couple of things.

01:26:03 - The Dharma House
So are we at the point yet where you think we could create an interface where I throw up a page and it looks something like a chat GPT page and it just saves the different grants that they've had pushed out as kind of conversations?

01:26:22 - The Dharma House
Or do I need to create you thinking like, you know, throw up some text fields and text boxes and have them fill out some information and then upload?

01:26:33 - The Dharma House
They haven't asked about interaction.

01:26:36 - The Dharma House
They just want information and information out.

01:26:39 - The Dharma House
So I'd be curious as to what the general consensus is around that, and especially maybe for control for structured outputs.

01:26:49 - The Dharma House
It might be more supportive in that way.

01:26:56 - Brandon Hancock
So how long is a grant just so we're on the same page before I give an answer?

01:27:00 - Brandon Hancock
Three pages?

01:27:00 - Brandon Hancock
Two?

01:27:01 - Brandon Hancock
Ten?

01:27:02 - The Dharma House
It can be.

01:27:03 - The Dharma House
The biggest one I've seen so far is like 25.

01:27:07 - Brandon Hancock
Okay.

01:27:08 - The Dharma House
they're probably taking about 100.

01:27:11 - The Dharma House
Their process, they're taking 100, 150 pages to create that.

01:27:17 - The Dharma House
They're pulling a lot of information from the org, from the nonprofit that they're working for, and they're pulling a lot of information from the funder, and then they have a process as to how to marry that information for a better acceptance rate.

01:27:33 - Brandon Hancock
So the short answer is with artifacts, you could also start to generate the grant.

01:27:39 - Brandon Hancock
And what's nice is you could almost chat against that artifact.

01:27:43 - Brandon Hancock
The hard part is just doing that in a UI.

01:27:46 - Brandon Hancock
Because like if it's two pages, you could easily show that in a UI.

01:27:49 - Brandon Hancock
But the second you get to 25 pages, like just managing that, you know, it's like, it's like if you had to code your whole project in one file.

01:27:59 - Brandon Hancock
That's disgusting, you know?

01:28:00 - Brandon Hancock
know?

01:28:00 - Brandon Hancock
Yeah.

01:28:00 - Brandon Hancock
Um, it's just very hard to do.

01:28:02 - Brandon Hancock
So, I mean, the, the thing that I think it could easily do is have the document in a bunch of, uh, the grant and a bunch of sections and you iterate on all the sections.

01:28:15 - Brandon Hancock
And then there's a final like combiner of some sort, but yeah, doing it.

01:28:20 - The Dharma House
And the funder's different and the grants are different.

01:28:23 - The Dharma House
So also I'm creating like, uh, like, um, uh, something to create the, the, um, the template itself.

01:28:32 - The Dharma House
We have to create the template based on the grant, on the available grant because each template or requests, requested bit of information from each funder is going to change.

01:28:43 - Brandon Hancock
So the other option, um, to, you know, this is like big boy projects of like, you know, very expensive, uh, is what we're discussing, but like, you could also kind of go back to what we were talking about with, uh, early on the, uh, the co-pilot, like what you really could do if you wanted is.

01:29:00 - Brandon Hancock
Have almost recreated a cursor-like experience to where you have the grant in the left and the chat on the right.

01:29:09 - Brandon Hancock
And basically what you're doing is having under the hood, ADK is listening to your request and updating that artifact.

01:29:17 - Brandon Hancock
Like there would be tool calls to like insert, you know, just make changes to the grant.

01:29:24 - Brandon Hancock
Bastian has dove deeper into the underlying tools.

01:29:29 - Brandon Hancock
It's almost, I mean, correct me if I'm wrong, Bastian, but it's almost like a get, under the hood, like they're doing like get changes, correct?

01:29:35 - Brandon Hancock
Or inserting stuff inside a cursor, because he could do something like that, right?

01:29:39 - Brandon Hancock
Or we'd love to hear your thoughts.

01:29:42 - Brandon Hancock
I'm sorry, what's the, what's what's the, you're writing a grant and we're trying to, we're ideating on the approach of like making it a cursor.

01:29:52 - Brandon Hancock
Like experience, but for grants to where, Hey, I don't like this section.

01:30:00 - Brandon Hancock
Fix it, you know?

01:30:01 - Bastian Venegas
Yeah, yeah.

01:30:02 - Bastian Venegas
I think the, maybe this is not the easiest way, but the way that it should ideally be done is this tool should make sense that it would be an MCP server for the company.

01:30:18 - Bastian Venegas
This is the kind of division where MCP, it's like you want to make your tools available to any agent or LLM that the user may have, and that includes tools like Cursor.

01:30:29 - Bastian Venegas
So then the Cursor agent itself is like the one that does every tool and stuff, but also is the one that refines the outputs.

01:30:41 - Bastian Venegas
And you can also like go back in the chat and all of that, that makes the user experience easier.

01:30:47 - Bastian Venegas
And there, you can do that in the, there's a public open source repo that Versaul has with an awesome UI that I linked there.

01:30:58 - Bastian Venegas
If you're using ADK.

01:31:00 - Bastian Venegas
You probably would have to fix something, but if you don't find any other options, I can definitely help you implement that.

01:31:07 - The Dharma House
Cool.

01:31:07 - The Dharma House
And you would do that for MVP?

01:31:11 - Bastian Venegas
I don't know.

01:31:12 - Bastian Venegas
If you need a user interface, you could use literally the ADK, That's enough to show the MVP, I think.

01:31:21 - The Dharma House
Well, that was my plan, was to use that, but artifacts don't serve well in that.

01:31:28 - The Dharma House
Like, it's really hard to upload a document and not have Google's parser step in even before your custom parser and throw an error because it can't.

01:31:39 - The Dharma House
It's receiving a binary file as opposed to, right now they want PDFs, PPTs, and DocX.

01:31:48 - The Dharma House
I got a basic prototype, but anytime I upload to that, I'm getting the kickback for it receiving as a binary error, even though I've built a parser, an in-house parser, it's just not.

01:32:00 - The Dharma House
It's happening fast enough, or I don't know if it's just not compatible with the ADK web.

01:32:07 - Bastian Venegas
Currently, there isn't a way to do this through a UI.

01:32:11 - Bastian Venegas
You would need to do this from a CLI environment?

01:32:18 - The Dharma House
Well, I'd like to do it from the UI, from ADK web, but the errors I'm getting, it's throwing me an error around the binary file when I upload.

01:32:28 - The Dharma House
So, for whatever reason, uploading is not native to ADK, and there still needs to be some kind of middle piece that I'm not sure.

01:32:37 - The Dharma House
Has anyone been able to upload a document through ADK web itself, or is it just because of the way that works that it's just not, it's not native, right?

01:32:47 - Brandon Hancock
I've done images.

01:32:48 - Brandon Hancock
I haven't had to do a PDF yet, so I cannot elaborate on it real fast.

01:32:54 - Brandon Hancock
Real quick, though, going back to, like, demo MVP, what I think you could potentially do as well...

01:33:00 - Brandon Hancock
Just for V1, V, really V0 at this point is do, option one is A, have a few different, like just direct LLM calls, forget agents, just three or four different LLM calls, you go figure out the template, you go figure out this, you go figure out this, then once you're done, just generate V1 of what, whatever the grant would look like.

01:33:29 - Brandon Hancock
And then just throw it into cursor, inside a cursor, just update the project rules to say like, hey, you were doing this, here's the context, here's everything else you need to know, and then just like mock what your application would do.

01:33:45 - Brandon Hancock
You know, and just say like, hey, here's what it would, here's what the, I would build towards this.

01:33:51 - Brandon Hancock
That way you get to showcase agents, or you get to show AI generating the first one, which is part one, making V1, and then for all the small edits, you would.

01:34:00 - Brandon Hancock
Just showcase it in cursor, making changes, something like that.

01:34:06 - Brandon Hancock
If I was to make a demo right now, just to show proof of concept, I would show something along those lines.

01:34:12 - Brandon Hancock
But I also, real quick, before diving too deep, I always like to make sure people have the budget because it's so funny.

01:34:21 - Brandon Hancock
The amount of times people are so excited to talk and I'm like, hey, just realistically, before either of us dive too deep into this, I just want to manage expectations and just like rough out the bat, this would most likely be a 20 to 30k project, potentially a little bit more on what you're trying to do.

01:34:38 - Brandon Hancock
Is that even in the ballpark of what you guys have budgeted for this?

01:34:43 - Brandon Hancock
Because if not, like, hey, like, you know, either we need to slim down, like, hardcore manage expectations, or just note that this project is not feasible right now.

01:34:53 - Brandon Hancock
So I think that's also important to mention.

01:34:56 - The Dharma House
Yeah, that's the discussion of my next meeting with them.

01:35:00 - The Dharma House
No, they don't want to spend a lot because it's their POC.

01:35:02 - The Dharma House
They want to POC it first and see if it's really something that they can use.

01:35:08 - The Dharma House
So they want me to just build a base MVP.

01:35:11 - The Dharma House
So that's where I'm like, I don't have a lot of information.

01:35:13 - The Dharma House
I got to continually do this discovery.

01:35:16 - The Dharma House
And I like the idea of like this adoption consultant, because it is, I'm like in very compact periods trying to learn as much about their process, their organization as I can, and then figure out in my own mind how to architect it in way that I think is best for them.

01:35:32 - The Dharma House
And that's, that's really tough.

01:35:34 - The Dharma House
Jake, I can't wait to hear what you have to say, but by all means, Brandon, please.

01:35:38 - Brandon Hancock
Yeah, Jake, if want to go.

01:35:39 - Brandon Hancock
And then afterwards, I have another alternative idea of how to tackle this for MVP.

01:35:44 - Jake Maymar
I, I, I, yeah, I love this discussion.

01:35:47 - Jake Maymar
You know, if you can figure out kind of what the budget is, what the long-term budget is, if you can take them to, you know, drinks or just go have a beer with them or whatever, that's super.

01:36:00 - Jake Maymar
Super valuable because, you know, Brandon's totally right about like 25K, 30K budget like that totally makes sense.

01:36:10 - Jake Maymar
But you could be leaving money on the table.

01:36:12 - Jake Maymar
Those grants are millions of dollars.

01:36:16 - Jake Maymar
And so, you know, you know, the organization could actually be granted millions of dollars just to do exactly what you're doing.

01:36:31 - Jake Maymar
And so, you know, there's no reason to be greedy, but just see if you can get an authentic conversation because sometimes there's more money there than, you know, you realize.

01:36:43 - Jake Maymar
But it's good to know the overall budget, like not necessarily what they would pay you, but the overall budget that they can spend.

01:36:51 - Jake Maymar
And then that gives you an idea of the longevity of the project as well.

01:36:55 - Jake Maymar
but yeah, Brandon has a really good point right up front.

01:37:00 - Jake Maymar
Find out if there is money in this, because, you know, you could have this conversation.

01:37:04 - Jake Maymar
They're like, oh, no, we're thinking $1,000.

01:37:06 - The Dharma House
Like, that's our top.

01:37:07 - Jake Maymar
And you're like, whoa, hey, well, you know, let's stay in touch.

01:37:13 - The Dharma House
Sounds like an awesome thing.

01:37:15 - The Dharma House
I mean, I haven't given them a price, but I'm sure I set a solid expectation for them where, you know, they know they're going to have to, you know, put some skin in the game even to figure out a POC.

01:37:28 - The Dharma House
But also, you know, that part about, I like it, that part about, like, especially non-competes and that other stuff.

01:37:37 - The Dharma House
I'm like, that's a lot to ask, because where do we define your business logic and then just basic agent architecture?

01:37:45 - The Dharma House
And if you're asking me that now, you know those clients who are right off the bat when they ask you that one question and you go, hmm.

01:37:52 - Jake Maymar
Yeah.

01:37:53 - Jake Maymar
Oh, that's another, that's a really good point.

01:37:56 - Jake Maymar
I'm sure Brandon's going to also bring this point up.

01:38:00 - Jake Maymar
But.

01:38:00 - Jake Maymar
The culture of the client almost never changes.

01:38:05 - Jake Maymar
So how the client deals with you in the very beginning is exactly how the relationship is.

01:38:12 - Jake Maymar
And you have to kind of decide, OK, I like that.

01:38:14 - Jake Maymar
Or, you know, maybe, you know, we'll sort of ride this out and see where it goes kind of thing.

01:38:21 - Jake Maymar
But I've found that they rarely change.

01:38:24 - Jake Maymar
And so, you know, just kind of how they're treating you is how they're continuing to treat you.

01:38:29 - Jake Maymar
And that's how I would also price it, you know.

01:38:32 - The Dharma House
Yeah, make it worse, the headache.

01:38:34 - The Dharma House
You know, I was like...

01:38:35 - Jake Maymar
Or if it's really nice, too.

01:38:37 - Jake Maymar
I mean, if it's not a headache and it's enjoyable, but they don't have a big budget, well, then that also factors in, too.

01:38:44 - Jake Maymar
So, you know, there's two sides of that coin.

01:38:47 - Jake Maymar
One last thing, and this is just a question to the team, you know, Git and doing a diff.

01:38:56 - Jake Maymar
Both of those things, you know, you see all the time, both in Cursor and Windsurf.

01:39:00 - Jake Maymar
Thanks,

01:39:00 - Jake Maymar
Is there not a repo that does this?

01:39:02 - Jake Maymar
Like, I would think by now that there'd be, like, some sort of version control Git diff thing for editing or writing or something like that.

01:39:13 - Brandon Hancock
I mean, I think it's just Git.

01:39:15 - Brandon Hancock
Like, I believe that's actually what they're doing just under the hood.

01:39:19 - Brandon Hancock
is proposing a bunch of small diffs using Git.

01:39:23 - Brandon Hancock
Like, I think that's actually what's happening.

01:39:26 - Brandon Hancock
I was actually, what I'd like to do, because, no, Jake, everything you said, yes, beautiful feedback.

01:39:33 - Brandon Hancock
Taking a step back, though, I think we even overcomplicated the MVP.

01:39:39 - Brandon Hancock
Realistically, the other suggestion right before swapping is literally just making four custom GPTs to simulate a multi-agent process.

01:39:49 - Brandon Hancock
So, like, agent one, find the template.

01:39:52 - Brandon Hancock
Agent two, do this.

01:39:54 - Brandon Hancock
Agent three, this, this, and this, just to show what it could look like.

01:39:58 - Brandon Hancock
That's kind of the direction I was thinking.

01:40:00 - The Dharma House
But, like, even just agentically, just an LLM call that's kind of breaking that process down, kind of like that.

01:40:06 - Brandon Hancock
Yeah, perfect.

01:40:07 - Brandon Hancock
And then the other thing I was going to suggest on just, like, money is, like, if these guys, same thing, doesn't work out, like, or one thing you could always do is just go upstream.

01:40:21 - Brandon Hancock
It's, like, obviously they're about to request money from someone.

01:40:24 - Brandon Hancock
So, like, whoever the grantee tour, grantor is, yeah, the funder, you could probably just ask, like, hey, you're obviously getting, you're on a mission to use this money.

01:40:39 - The Dharma House
They bought million in grants so far this year.

01:40:43 - Brandon Hancock
Yeah.

01:40:44 - Brandon Hancock
So, it's, like, you're clearly on a mission to use and deploy this capital for the benefit of the purpose of this organization.

01:40:51 - Brandon Hancock
Would you guys be interested in me building something for you guys so that it was easier, a reduced friction between people who are actually going to do the work and people who, yeah.

01:41:00 - Brandon Hancock
You know, cause that's all it is.

01:41:01 - Brandon Hancock
Like all these grants are just friction, you know?

01:41:03 - Brandon Hancock
So it's, um, would you be interested in me building something for you guys to make it easier for people to not have gatekeep deploying this money?

01:41:12 - Brandon Hancock
Cause it's probably, if the answer is yes, my God, like they clearly have the funding to do it.

01:41:17 - Brandon Hancock
So like you're solving rich people problems, which is always the best problem to solve.

01:41:21 - Brandon Hancock
And then, um, or you might quickly find out that they're like, no, we actually like the gatekeeping because.

01:41:27 - Brandon Hancock
You know, we're here just to like, cause like literally some grants are just like, Hey, like we help out the people we help out and we just had to have a formal process.

01:41:35 - Brandon Hancock
So yeah, you could probably find some, some light in there too.

01:41:38 - Brandon Hancock
So yeah.

01:41:38 - Brandon Hancock
Um, or always you can go horizontally and just say like, if this specific organization that's calling out to isn't interested in it, then you could always go to an adjacent vertical.

01:41:50 - Brandon Hancock
Cause there there's, there's, granting foundations all throughout America, you know?

01:41:54 - Brandon Hancock
So this specific one says, no, there's probably a hundred other ones that are like, yeah, we would love something like that.

01:42:00 - The Dharma House
So.

01:42:00 - The Dharma House
Yeah.

01:42:00 - The Dharma House
I mean.

01:42:00 - The Dharma House
I'm going to build a product now.

01:42:01 - The Dharma House
feel like I got to build a product no matter what.

01:42:03 - The Dharma House
I've already, like, put some hours in on it, and I thought that I'd be able to demo it for you guys in WebADK.

01:42:09 - The Dharma House
I have it.

01:42:10 - The Dharma House
Everything except that doc upload part right now is ready to demo, and I built that and probably, I don't know, I probably put seven or eight hours into it.

01:42:20 - Brandon Hancock
That's awesome.

01:42:21 - The Dharma House
Yeah, but I can't get past this artifact piece yet.

01:42:24 - The Dharma House
I'm going to go back in and try it again.

01:42:26 - The Dharma House
And I was wondering if I should just convince them to make it RAG-based and use Vertex and maybe go that route.

01:42:33 - The Dharma House
And it seems easier.

01:42:35 - The Dharma House
Is there something I just don't understand yet about uploading and the process involved with uploading a doc and why this binary thing is even a problem in the first place?

01:42:44 - Brandon Hancock
I mean, it should work.

01:42:47 - Brandon Hancock
So that's why I'm like, as you are mentioning this, I don't know why it's not working.

01:42:51 - Brandon Hancock
I'm in the same boat of, like, why is it not working?

01:42:54 - Brandon Hancock
So, yeah, this week is busy, but next week...

01:43:00 - Brandon Hancock
I'm going to be in eight more use cases of ADK.

01:43:02 - Brandon Hancock
So the second I get to applying a PDF or adding a PDF, I'll let you know my experience too.

01:43:09 - Brandon Hancock
But if you can't, so here's the hard part really fast.

01:43:15 - Brandon Hancock
Even if you do put this in Vertex, at the end of the day, you're going to be doing a RAG request, which is designed to say, there was this huge thing.

01:43:25 - Brandon Hancock
I only want small pieces of it.

01:43:27 - Brandon Hancock
So, and the whole point of the doc, the whole point of the process is read everything and then take action on everything, which is hard, which basically just nullifies RAG.

01:43:39 - Brandon Hancock
Just so that, yeah.

01:43:41 - Brandon Hancock
So you have to get it uploaded.

01:43:45 - Brandon Hancock
Yeah.

01:43:46 - Brandon Hancock
So.

01:43:47 - The Dharma House
Cause then there's kind of state, there's a little bit of state management around different pieces, parsing it out, building the template, and then rendering the grant itself.

01:43:59 - The Dharma House
Yeah.

01:43:59 - The Dharma House
It's been a fun thing.

01:44:00 - The Dharma House
The three through so far.

01:44:01 - The Dharma House
And yeah, all the help I could get around that artifact piece, if anybody has any insight on that.

01:44:08 - The Dharma House
And then again, I talked to, I kind of work side by side on Thursdays with this team that has a graph rag.

01:44:15 - Brandon Hancock
Locally, I found a team that's built a graph rag.

01:44:18 - The Dharma House
And they're doing the same thing, something very similar, but they're doing it for the construction industry.

01:44:22 - The Dharma House
And so they're using Mistral's OCR parser, because I guess it's really powerful.

01:44:29 - The Dharma House
There's a cost to it, but it handles schematics and pretty much anything you throw at it very, very well.

01:44:35 - The Dharma House
It seems to be able to just parse it.

01:44:39 - The Dharma House
But yeah, I'm really shocked that ADK doesn't have some kind of native upload of any kind of file.

01:44:46 - The Dharma House
And I could be crazy, but I've read over it a couple of times, trying to figure it out.

01:44:51 - Nate Ginn
I have a quick question about that Mistral OCR.

01:44:54 - Nate Ginn
How does it handle handwritten text?

01:44:57 - Nate Ginn
To find something that works good on handwriting text.

01:45:00 - The Dharma House
So Mistral has, I'll put the link in the chat, but it even has examples of all types of writing, all types of languages.

01:45:10 - The Dharma House
I'm not quite sure how it does it, but it has an Arabic solve.

01:45:17 - The Dharma House
And so if you write in Arabic, it'll pop up and it works pretty well.

01:45:26 - Brandon Hancock
What, real fast, Aaron, what I wanted to show you, so whenever, in the YouTube ADK video I did for generating thumbnails, I mean, are you, just out of curiosity, are you, when you're uploading files, they do need to be in a byte stream.

01:45:43 - Brandon Hancock
So, like, that's what is happening here.

01:45:46 - Brandon Hancock
But, specifically, I'm saying what type they are to help ADK understand what it's working with.

01:45:51 - Brandon Hancock
And this is what I did to get it to work.

01:45:53 - Brandon Hancock
And this is what, um, this is what they recommend here, too.

01:45:58 - Brandon Hancock
So it's like, um.

01:46:00 - Brandon Hancock
Mike, the MIME type would just change to application PDF.

01:46:03 - Brandon Hancock
So just out of curiosity, like if you swap to this approach, but just put application PDF here, that would work.

01:46:12 - The Dharma House
All right.

01:46:13 - The Dharma House
I'll take a look at that repo.

01:46:15 - The Dharma House
I really appreciate that.

01:46:18 - Brandon Hancock
The only other thing that you need to worry about, let me hop over.

01:46:26 - Brandon Hancock
Shoot.

01:46:26 - Brandon Hancock
Shoot.

01:46:26 - Brandon Hancock
There's one agent.

01:46:28 - Brandon Hancock
One second.

01:46:31 - Brandon Hancock
Let me do this.

01:46:34 - Brandon Hancock
Okay.

01:46:35 - Brandon Hancock
Real fast.

01:46:36 - Brandon Hancock
This one.

01:46:40 - Brandon Hancock
Let me just look really fast.

01:46:42 - Brandon Hancock
There's a term called callbacks, and this is what – yeah.

01:46:45 - The Dharma House
Yeah, mentioned callbacks last week, and I added a callback before and after at the start of the process and at the bottom of the process to ensure that –

01:47:00 - The Dharma House
It was rendered properly, but I'm still playing with callbacks.

01:47:03 - The Dharma House
I'm still quite fresh at it.

01:47:06 - Brandon Hancock
So the only suggestion I was going to add as well, so the area we need to add the image, or in your case, the PDF, is before calling the model.

01:47:18 - Brandon Hancock
So what you could do is look at this callback section here, and what I'm doing is saying, okay, hey, the user just clicked an ADK web.

01:47:29 - Brandon Hancock
They clicked the little attachment button, and they added three PDFs.

01:47:32 - Brandon Hancock
So what I would like you to do is, for each part in the user's message, the last message they sent, I want you to look for all parts that have inline data, because that inline data is how you attach, you know, blobs.

01:47:47 - Brandon Hancock
And we're going to say, I only want to get the ones with mime type forward slash application PDF.

01:47:53 - Brandon Hancock
And once I do that, then I would like to, where did I have it next?

01:48:01 - Brandon Hancock
What did I do with it?

01:48:04 - Brandon Hancock
I did something.

01:48:06 - Brandon Hancock
I thought you had, sorry, I'm just, I cannot remember what I did.

01:48:11 - Brandon Hancock
One second.

01:48:13 - Brandon Hancock
Da-da-da, image, callback.

01:48:18 - Brandon Hancock
Create the path.

01:48:20 - Brandon Hancock
Oh, yeah, here's, yeah, basically I would just, oh, wait, this was me saving it.

01:48:26 - Brandon Hancock
I take it back.

01:48:27 - Brandon Hancock
I take it back.

01:48:28 - Brandon Hancock
Yeah, that was me saving the file so that I could later load it with a tool.

01:48:34 - Brandon Hancock
So, like, once I just, so here was the process.

01:48:37 - Brandon Hancock
Users are going to give you PDFs to your agents.

01:48:40 - Brandon Hancock
Well, like, you need to handle that.

01:48:42 - Brandon Hancock
So what I was doing is I was instantly taking the image, in your case, the PDF, saving it locally so that later on I could load that PDF, the agent could load it whenever it needed it.

01:48:56 - Brandon Hancock
That was my approach.

01:48:57 - Brandon Hancock
So taking a PDF, save it locally.

01:49:00 - Brandon Hancock
Then whenever an agent in the future needs it, cool, I just load that PDF as an artifact.

01:49:05 - Brandon Hancock
The other option, the simplified version, was just to instead of saving it locally, then having the agent read it, is just instantly add it as an artifact.

01:49:14 - Brandon Hancock
So I might have gone a little too crazy in there.

01:49:18 - Brandon Hancock
But yeah, that whole repository, it got to work with images.

01:49:23 - Brandon Hancock
So I would assume there's maybe some lessons to steal.

01:49:26 - Brandon Hancock
So yeah, seriously, ping me if you have any future questions on this.

01:49:30 - Brandon Hancock
no, this is, love what you're doing.

01:49:32 - Brandon Hancock
I just want to make sure if anyone else has questions too before today's up, just to make sure anyone else.

01:49:37 - Brandon Hancock
So if anyone else has questions, feel free to.

01:49:39 - Nate Ginn
I actually have one more thing quick, Brandon.

01:49:42 - Nate Ginn
Yeah.

01:49:43 - Nate Ginn
I know it's getting late here, but so I, the program I wrote a long time ago that does my billing coding, it essentially puts everything into a Google Sheet program.

01:49:57 - Nate Ginn
now I want to be able to go and, like, you, extreme.

01:50:00 - Nate Ginn
Crack that data, like for instance, let's say I forgot to do my note for a day, so my line on, like Brandon Hancock came to see me, and there's no codes in there because I didn't finish, right?

01:50:15 - Nate Ginn
I want to be able to get to a point where it searches through the entire database looking for empty spots, and then essentially what would be great is it sends some kind of message to me, the provider, like whether it's an email or a text or something like that saying, hey, here's a list of all of the empty spots we have for you, here's the, you know, and extract the date of service, the patient name, and then send it to the patient.

01:50:41 - Nate Ginn
So, I don't know if the 8K stuff seems like the right place to go because it's a Google Doc, but I don't know.

01:50:47 - Brandon Hancock
What you could actually do, even simpler, there's a term called a cron job, and basically what a cron job does is it says, hey, at this time stamp, perform this function.

01:50:59 - Brandon Hancock
So, in your case.

01:51:00 - Brandon Hancock
In what we could do is have a cron job run every day at midnight.

01:51:03 - Brandon Hancock
And in your case, you could get it done with a Python script, which is pretty nice because you don't even have to touch AI.

01:51:08 - Brandon Hancock
And what it would do is like, okay, pull down Google Sheet, filter for all client meetings today where row is null.

01:51:19 - Brandon Hancock
And then it would just say, okay, Brandon Hancock did it.

01:51:23 - Brandon Hancock
Carly came.

01:51:23 - Brandon Hancock
She also came in no codes yet.

01:51:26 - Brandon Hancock
And it would just, you could use a tool like SendGrid to send you, or Mailgun.

01:51:33 - Brandon Hancock
There's plenty of mail tools that would just shoot you an email and say, and you could just pre-populate the body and say, client name, you know, needs attention.

01:51:45 - Brandon Hancock
Yeah.

01:51:46 - Brandon Hancock
And then Bastian also brings up a good point too.

01:51:49 - Brandon Hancock
N8N might be the easiest way to do that, actually, because it's deployed.

01:51:53 - Brandon Hancock
It runs 24-7, and all you have to do is just say, pull Google Sheet, run Python.

01:52:00 - Brandon Hancock
Fathom code, send email, if stuff was empty.

01:52:04 - Brandon Hancock
You could probably get it done in four nodes.

01:52:07 - Brandon Hancock
So you might want to check that one out too.

01:52:10 - Nate Ginn
What would you suggest for me to learn more about NAN?

01:52:12 - Nate Ginn
Because I have been watching a ton of videos lately that, you know, as I'm listening to them anyway.

01:52:18 - Nate Ginn
But everybody's using NAN, and my knowledge on it is what I've heard here.

01:52:25 - Brandon Hancock
Yeah, mean, honestly, I think the easiest way to do it is just to start, like, literally just use it.

01:52:31 - Brandon Hancock
Like, it is actually that straightforward, and just say, like, hey, here's what I'm, like, just in Grok or in Chen Chibouti.

01:52:39 - Brandon Hancock
Here's what I'm trying to do.

01:52:40 - Brandon Hancock
Please help me make an NAN workflow that does this.

01:52:43 - Brandon Hancock
And it'll tell you the nodes, the connections, and the Python script.

01:52:47 - Brandon Hancock
And that, like, I mean, seriously, like, if you tonight drank a cup of coffee, headphones on, you could build it tonight.

01:52:54 - Brandon Hancock
So I would, I would, for NAN, it's so simple to use, I wouldn't, no more need for tutorials.

01:53:00 - Brandon Hancock
I think you could just, yeah, just get that set up.

01:53:03 - Brandon Hancock
But yeah, the key there is a cron job with N8N.

01:53:06 - Brandon Hancock
And you got to thank Bastian for the suggestion because he was spot on.

01:53:10 - Nate Ginn
Yep.

01:53:11 - Nate Ginn
Bastian's always spot on, it seems like.

01:53:13 - Brandon Hancock
I know, seriously.

01:53:15 - Brandon Hancock
Yeah.

01:53:16 - Nate Ginn
Thanks again.

01:53:18 - Brandon Hancock
Of course, of course.

01:53:19 - Brandon Hancock
All right, guys.

01:53:20 - Brandon Hancock
Any other questions?

01:53:22 - Brandon Hancock
Anyway, we a few extra people in.

01:53:25 - Brandon Hancock
If you do want to hop on, feel free to just turn your camera on.

01:53:28 - Brandon Hancock
And happy for you to go next.

01:53:30 - Neel More
Yeah.

01:53:34 - Brandon Hancock
Hey, Neil.

01:53:38 - Neel More
Do you want to go Hi, Brandon.

01:53:39 - Neel More
I got a quick question.

01:53:41 - Neel More
Sorry, it's late night here, so my camera's not there.

01:53:44 - Neel More
And it's a very, very basic question.

01:53:45 - Neel More
I have started with the agentic AI.

01:53:48 - Neel More
I have seen your agentic AI courses, especially with the LangChain.

01:53:53 - Neel More
And I have seen then you move to the crew AI, and then you are, right now, you are working on the ADK.

01:53:58 - Neel More
So as in for the new guys, what?

01:54:00 - Neel More
What you will suggest to start with, because I know LandGraph, you got the basic clear, but I want to get it more good in the GNDK AI within the next one month or two months at the max I got it.

01:54:13 - Brandon Hancock
And so what is your suggestion or maybe for the people who are in the call, right?

01:54:19 - Neel More
How's their journey?

01:54:20 - Neel More
And as the team member mentioned about the NA8N, right?

01:54:25 - Brandon Hancock
I have seen it can also do many things in the auto you will recommend because I've seen you are full in into the ADK and I'm just wondering in that case.

01:54:33 - Brandon Hancock
No, awesome question.

01:54:35 - Brandon Hancock
So quick clarifying thing, a question before answering.

01:54:38 - Brandon Hancock
So are you, are you looking like, what are you looking to do?

01:54:43 - Brandon Hancock
Like, okay, let's just fast forward two months.

01:54:45 - Brandon Hancock
Like you said, like, you know, say you just know you're an expert at AI.

01:54:50 - Brandon Hancock
What are you looking to do next?

01:54:51 - Brandon Hancock
And then we can work backwards.

01:54:53 - Neel More
Okay, so I'll give my background.

01:54:55 - Neel More
I lost my job like six months back and I'm more into like, I got 20 years old.

01:55:00 - Neel More
experience.

01:55:00 - Neel More
I'm very good at the MLOps, so I know about the data science part, and I was just missing about this agent AI when it came to the autonomous agent, right?

01:55:10 - Neel More
So I want to add on top of my skill set, the agent AI.

01:55:15 - Neel More
That's my core aim.

01:55:17 - Neel More
And later on, what I want to do is to integrate this thing into the data science flow, right?

01:55:22 - Neel More
How it can help with the MLOps or with the LLM Ops.

01:55:26 - Neel More
That is the intention where I'm going around.

01:55:29 - Neel More
And the two months, because I can prepare for the interview, so that's one of the goals.

01:55:36 - Brandon Hancock
I gotcha.

01:55:37 - Brandon Hancock
Okay, so if the goal is to get hired, from what I have seen, a lot of companies like LengChain and LengGraph, because it's very, very technical, I've seen a lot of that.

01:55:54 - Brandon Hancock
For more personal projects and small business applications, I do think ADK right now is my favorite.

01:56:00 - Brandon Hancock
Out of the out of all of them.

01:56:02 - Brandon Hancock
But if you're looking at getting experience to land a job at a corporate company, I've laying chain seems to be would be the best one.

01:56:13 - Brandon Hancock
But out and let me explain why.

01:56:16 - Brandon Hancock
It really comes down to the ability.

01:56:19 - Brandon Hancock
It really comes down to like lane chain.

01:56:21 - Brandon Hancock
At this point, it's just a wrapper around all things AI, meaning it can, you're going to learn with lane chain, all about embeddings.

01:56:30 - Brandon Hancock
chunking, how to integrate to vector source.

01:56:33 - Brandon Hancock
like at this point, learning lane chain almost means learning everything there is about AI, because you're going to learn about making model, like calls with models.

01:56:41 - Brandon Hancock
After that, you're going to learn about how to use agents.

01:56:44 - Brandon Hancock
So you're going to learn about react agents.

01:56:47 - Brandon Hancock
So yeah, by learning lane chain and like building things with it, you will ultimately learn all those underlying skills, which is nice because like crew AI, crew AI and ADK, that are should think give do

01:57:00 - Brandon Hancock
Take away all of that, because they make it so easy to where all you're really doing is just passing in a prompt, making a few Python tools, and the agents handle the rest of the complexity for you, whereas with Langchain, you're almost dealing with the raw underlying concepts, which is probably more appealing to an employer, because, yeah, they would probably want you to, you know, oh, we want to add AI to our website.

01:57:25 - Brandon Hancock
Okay, cool.

01:57:27 - Brandon Hancock
They probably want a rag chat bot.

01:57:29 - Brandon Hancock
Well, that means, hey, under the hood, you're now learning how to make calls, embed things, and send it, yeah, work with different vector stores.

01:57:38 - Brandon Hancock
So, yeah, at the end of the day, Langchain would probably be the best one.

01:57:47 - Brandon Hancock
What I would also do real fast, so I would be curious, I'm a huge fan of, like, setting a goal and working backwards.

01:57:53 - Brandon Hancock
So, like, if there's a certain few jobs you're looking to apply, like, hey, like, let's cut out the guesswork and just...

01:57:59 - Brandon Hancock
...

01:58:00 - Brandon Hancock
Say, hey, what are they actively hiring for right now?

01:58:03 - Brandon Hancock
And just looking at the tools and they just work backwards from there.

01:58:06 - Brandon Hancock
That's, I mean, that's instead of guessing what they want, we could just look up what they want and then go all in on studying that.

01:58:13 - Brandon Hancock
That would be my, like, that's the most practical advice at least.

01:58:17 - Brandon Hancock
Any questions on any of that?

01:58:19 - Neel More
Oh, yeah.

01:58:20 - Neel More
Thanks.

01:58:20 - Neel More
Thanks a lot.

01:58:21 - Neel More
Because, yeah, so just what I'm trying to go for is more about the AI architect or agentic AI architect, those kind of roles I'm aiming for.

01:58:30 - Neel More
And I have also seen, like, they ask for LLM tuning and all this track tuning.

01:58:35 - Neel More
So that's what I'm looking for into the job descriptions, what you mentioned here in this case.

01:58:41 - Brandon Hancock
Okay, if that's the case, you might not want to go as much link chain.

01:58:45 - Brandon Hancock
What you might want to do is go and just pick an infrastructure, like a cloud platform.

01:58:52 - Brandon Hancock
It looks like commercially Azure is winning right now.

01:58:55 - Brandon Hancock
And I would focus on building some sort.

01:59:00 - Brandon Hancock
Sort of Azure course, infrastructure course, where you're going to learn about creating a, you know, where you're going learn about how you can deploy your own LLMs, interface with them in Azure.

01:59:10 - Brandon Hancock
You can also search, Azure is rolling out their agent foundry.

01:59:13 - Brandon Hancock
So that's a great way to learn how to work with deployed agents.

01:59:16 - Brandon Hancock
You can also, I mean, everything we're just describing, you can do in Azure and it's a very business oriented skill.

01:59:23 - Brandon Hancock
So I would, yeah, I would mix AI with a cloud infrastructure platform and Azure is winning from what I've seen commercially.

01:59:33 - Neel More
Thanks for big organizations.

01:59:35 - Neel More
That's great.

01:59:36 - Neel More
Because I have been working on the Vertex AIGC before last four years.

01:59:40 - Neel More
So that was one of the background I have got it.

01:59:44 - Brandon Hancock
Yeah.

01:59:44 - Brandon Hancock
Yeah.

01:59:45 - Brandon Hancock
I mean, also, I mean, the good news is once you learn how to do this in one infrastructure platform, 80% of it would probably apply to the other.

01:59:53 - Brandon Hancock
The one, you're just going to relearn some of the core, like the terminologies change, like the name of the service changes, but.

02:00:00 - Brandon Hancock
The underlying core principles of like, oh, all we're doing is fine-tuning a model.

02:00:04 - Brandon Hancock
Okay, cool.

02:00:05 - Brandon Hancock
You know, that just changes from Vertex AI over to what Azure offers.

02:00:10 - Brandon Hancock
But the core principles are the same.

02:00:12 - Brandon Hancock
So does anyone else have any ideas?

02:00:15 - Brandon Hancock
I'm just, you know, curious to see if any ideas for Neel.

02:00:25 - Brandon Hancock
Jake, do you have your hand up?

02:00:26 - Brandon Hancock
Sorry, my thing was up.

02:00:27 - Brandon Hancock
Oh, no.

02:00:28 - Brandon Hancock
Yeah, yeah, I think that would be the best one.

02:00:30 - Brandon Hancock
But yeah, and seriously, feel free to shoot me a DM at any point too if you have any other specific questions.

02:00:35 - Brandon Hancock
But I think going Azure, I just don't know any, I don't know if there's any good Azure courses right now.

02:00:43 - Brandon Hancock
Let me just look really fast.

02:00:46 - Brandon Hancock
Microsoft, they have a certificate for Azure AI fundamentals.

02:00:51 - Brandon Hancock
That might be something nice to go deep in on.

02:00:54 - Neel More
Okay, just a follow-up, right?

02:00:56 - Neel More
So thanks for answering, Brendan.

02:00:57 - Brandon Hancock
Yeah.

02:01:00 - Neel More
Yeah.

02:01:01 - Neel More
All right.

02:01:02 - Neel More
Cool.

02:01:02 - Neel More
Yeah.

02:01:02 - Neel More
Thanks, Brandon.

02:01:03 - Neel More
just want a quick follow up.

02:01:04 - Neel More
So if I got any questions, I can I'm just wondering what's the best way.

02:01:09 - Brandon Hancock
Sorry for asking a new question.

02:01:13 - Brandon Hancock
No, a DM would be perfect.

02:01:16 - Neel More
Thank you.

02:01:16 - Neel More
Thank you, everyone.

02:01:18 - Brandon Hancock
Perfect.

02:01:19 - Brandon Hancock
Perfect.

02:01:20 - Brandon Hancock
Bert, you're up next, man.

02:01:21 - Brandon Hancock
What's going on?

02:01:25 - Brandon Hancock
Oh, you read it, buddy.

02:01:29 - Bert
Oh, cool.

02:01:30 - Bert
So thank you much, Brandon.

02:01:31 - Bert
really appreciate being here on the master class and being able to observe knowledge from a lot of very experienced individuals.

02:01:38 - Bert
So my journey is that I just started doing ADK maybe about six weeks ago.

02:01:43 - Bert
just started like roughly dabbling it.

02:01:44 - Bert
But it wasn't until I found your master class last week, your three hour master class, that I really started really getting into the whole ADK thing.

02:01:51 - Bert
So they basically watching it like every day for the last like seven days, especially like the second half of it where you go over like state multi agents and everything.

02:02:00 - Bert
think.

02:02:00 - Bert
I

02:02:00 - Bert
So it's been very, very useful.

02:02:02 - Bert
So even going back to Google's own like developer course that they had with getting ADK fundamentals, just by watching your class, I was able to find like a bug and debug it because let me just quickly share my screen.

02:02:17 - Bert
I'll make this super quick.

02:02:21 - Bert
Let's see.

02:02:23 - Bert
Screen share.

02:02:25 - Bert
yeah.

02:02:26 - Bert
Okay.

02:02:29 - Bert
So yesterday when I was running the thing, I got this error over here.

02:02:34 - Bert
So the reason why I got that error is because my spidey senses started going off.

02:02:42 - Bert
And the reason was because they didn't wrap the, didn't wrap this tool here.

02:02:47 - Bert
They didn't this, that's using like a internal tool here.

02:02:50 - Bert
So you said that never use, um, an agent that uses a built in tool as a subagent.

02:02:56 - Bert
So in the original code base, which is still on, um, GitHub.

02:03:00 - Bert
I'm not trying to shame anybody here or anything.

02:03:03 - Bert
me just.

02:03:04 - Brandon Hancock
No, shame, man.

02:03:06 - Brandon Hancock
Shame.

02:03:09 - Bert
More.

02:03:10 - Bert
I'm sorry.

02:03:13 - Bert
Hold on.

02:03:14 - Bert
Sorry about this.

02:03:16 - Brandon Hancock
They dropped a new version today, 1.0.

02:03:19 - Brandon Hancock
I'm curious if that fixed it.

02:03:21 - Brandon Hancock
They did it like six hours ago.

02:03:22 - Brandon Hancock
I'm curious if that fixed it.

02:03:25 - Bert
Okay.

02:03:25 - Bert
Yep.

02:03:26 - Bert
So I've got to just show you the GitHub repo.

02:03:27 - Bert
Let me just quickly undo my camera quickly.

02:03:29 - Bert
Just to sort this.

02:03:31 - Brandon Hancock
Capture the door real fast.

02:03:33 - Brandon Hancock
But I'm trying to see the fix.

02:03:35 - Bert
Okay.

02:03:36 - Bert
And then share screen.

02:03:39 - Bert
Okay.

02:03:40 - Bert
Share.

02:03:40 - Bert
Okay.

02:03:41 - Bert
Share.

02:03:41 - Bert
So basically their GitHub repo looks like this here.

02:03:44 - Bert
So here it is.

02:03:45 - Bert
They have the script agent here.

02:03:47 - Bert
So as I mentioned, you mentioned about the tools here.

02:03:49 - Bert
So because of watching like your videos, as soon as I got that error and I looked at the tool saying, oh, that's kind of like suspicious.

02:03:54 - Bert
I was able to like wrap that in front of that agent tool and like move on.

02:03:58 - Bert
So it showed me like how.

02:04:00 - Bert
Great job, like knowledge and everything.

02:04:01 - Bert
So I really do appreciate this.

02:04:03 - Bert
So I myself am trying to pivot from being a data engineer into being an ADK developer.

02:04:09 - Bert
So basically, as I mentioned, I've just been going over the last week, I've just been going really over to really, really get into like the fundamentals of like the callbacks, the states, like how to use the runners as opposed to ADK web.

02:04:19 - Bert
So I really appreciate your masterclass video as well as like the knowledge of this master, this mastermind group as well.

02:04:27 - Bert
So thank you very much.

02:04:28 - Brandon Hancock
I appreciate it.

02:04:29 - Brandon Hancock
No, that's awesome.

02:04:31 - Brandon Hancock
Hey, thank you so much for all the kind words and love, love that.

02:04:34 - Brandon Hancock
Like, I mean, you're a now.

02:04:36 - Brandon Hancock
Like, I mean, the thing like ADK is so new, like there's certain things like you probably know more than me, you know, on certain things because like it's so new and there's so many like edge cases and everything.

02:04:47 - Brandon Hancock
So I love gear that like you're, you're taking it and you're running with it and look like building full things.

02:04:52 - Brandon Hancock
I was really curious.

02:04:54 - Brandon Hancock
What are your thoughts on this YouTube short assistant?

02:04:56 - Brandon Hancock
I haven't seen the sample yet.

02:04:58 - Brandon Hancock
So I was curious.

02:05:00 - Brandon Hancock
What does it do?

02:05:01 - Brandon Hancock
Is it a good example?

02:05:06 - Bert
Yes, it's a pretty good example.

02:05:08 - Bert
So basically they have a short script writer here, so then it's going to write in your script.

02:05:12 - Bert
And once it writes you the script, it saves it to a state.

02:05:14 - Bert
And inside of the state, then the visualizer is going to pick up the script and it's going to create visualizations based on your script.

02:05:20 - Bert
And finally the format is going to come in here and then it's going to take the visualizations as well as the script and put them together to format a video.

02:05:28 - Bert
But the thing about it is that they use this also to explain like loops similar to what you do.

02:05:32 - Bert
The reason why they need to explain like loops and sequential is because if you just say write me a script, it's just going to use the script writer because it's not going to do the whole thing because it satisfies just like writing the script as an agent.

02:05:43 - Bert
But then if you use a loop to force it to say, okay, you're going to write a script, then we're to have to use the visualizer and everything.

02:05:48 - Bert
So it's a pretty good example, except for the fact that if you actually try to run the code, it's going to fail on you because of the fact that the tool here, because they're trying to use like this.

02:06:00 - Bert
Sub-agent here as a, this like agent here, this ML sub-agent, as a sub-agent was called a built-in tool here.

02:06:07 - Bert
So I assume that when this was first created, because it was created like about six weeks ago, just after the Google Next conference.

02:06:13 - Bert
So I suspect it probably worked back then, and then they changed something in the ADK since then, probably like broke it.

02:06:19 - Bert
So that's what I probably attribute it to.

02:06:21 - Bert
But then it's good watching your videos, because as mentioned, your videos told me, okay, all I have to do is just wrap this in that agent, agent, like MLM, like whatever that object is, and then it'll work as it did within my personal code base, when I wrapped it in here as the agent as tool.

02:06:39 - Bert
So then it started working here and everything.

02:06:40 - Bert
So this is a pretty good example, but then I also, but I still like your examples much better in your masterclass.

02:06:45 - Bert
So that's not just to hype you up because you're here in person, but I do like, I do like your masterclass, like much better than this.

02:06:52 - Bert
It's like very logical to follow and everything.

02:06:56 - Brandon Hancock
Thank you so much.

02:06:57 - Brandon Hancock
And just other quick question on this.

02:06:59 - Brandon Hancock
Does it act?

02:07:00 - Brandon Hancock
Does it actually create visuals, or does it create prompts?

02:07:02 - Brandon Hancock
Does it actually use their image generation tools, that example?

02:07:07 - Bert
So I haven't got deep into using the image generation tool to run it from end to end, but then it looks like it's just using the flash here, so I'm not sure if it uses the imagine here.

02:07:18 - Bert
So it says here, combine the script from the states and the visualization concept in the state into a markdown file requested previously.

02:07:27 - Bert
So that's what it does here.

02:07:29 - Bert
So this is like the call to action here.

02:07:31 - Bert
So, yep, I guess one of the questions I had to ask you is that inside of your ADK, your prompts generally have like very, very, very detailed instructions.

02:07:42 - Bert
So did you write those instructions off the top of your head, or did you use some sort of like LLM to help you write those like detailed instructions, like feeding into the agent's objects?

02:07:52 - Brandon Hancock
I always, like at this point, I barely write code.

02:07:56 - Brandon Hancock
I'm always having cursor write it for me.

02:07:58 - Brandon Hancock
it's 90% of the time it's just, you know, talk.

02:08:00 - Brandon Hancock
Being to cursor, having cursor, because are you on a Mac or Windows?

02:08:04 - Bert
can't tell what you're on.

02:08:05 - Bert
I'm in the Mac right now.

02:08:07 - Brandon Hancock
Okay, perfect.

02:08:07 - Brandon Hancock
So you can actually update the keys to like, it's called diction.

02:08:12 - Brandon Hancock
So you can just hit like, in my case, I hit command twice and I just talk.

02:08:15 - Brandon Hancock
So I just say like, hey, I'm trying to create instructions.

02:08:18 - Brandon Hancock
Here's what I wanted to do.

02:08:20 - Brandon Hancock
Here's the ideal phases.

02:08:21 - Brandon Hancock
So yeah, it's usually just like verbalizing it and then making a few iterations.

02:08:27 - Brandon Hancock
But no, most of the instructions, I have AI write it for me.

02:08:32 - Bert
Okay, cool.

02:08:33 - Bert
Thank you much.

02:08:34 - Bert
That was the major question I had.

02:08:36 - Bert
So thank you much.

02:08:36 - Bert
I really appreciate it.

02:08:37 - Bert
So thank you much for taking your time.

02:08:40 - Brandon Hancock
Yeah, of course.

02:08:40 - Brandon Hancock
Thanks for hopping on today, Bert.

02:08:42 - Brandon Hancock
Always very cool to see what everyone's building and learning.

02:08:45 - Brandon Hancock
And if there's any specific next videos, do you want me to create for ADK?

02:08:50 - Brandon Hancock
Hey, I'm always looking for ideas.

02:08:51 - Brandon Hancock
So yeah, if anything comes up, let me know.

02:08:55 - Brandon Hancock
Happy to keep going just because like, I'm really loving the tool and want to keep making

02:09:00 - Brandon Hancock
I'm we're all learning what it can do and everything.

02:09:02 - Brandon Hancock
So I'm learning alongside you guys.

02:09:04 - Bert
Yep.

02:09:05 - Bert
And just to let you know that on LinkedIn, I put down that, because basically I'm in between jobs right now.

02:09:11 - Bert
So on LinkedIn, my current job is I just put down sabbatical, upskilling on ADKs, and just wrote down using my knowledge as a data engineer, using DAGs and everything, plus using my previous knowledge as an engineer working with web sessions in the background.

02:09:27 - Bert
Like we're merging those together for ADK.

02:09:30 - Bert
And I've already got like a couple of bites of recruiter just reaching out to me saying like, hey, we're looking for somebody who's doing ADK, like proof of concept.

02:09:38 - Bert
So just to show you that a lot of the stuff works that you're like sharing with us today.

02:09:42 - Brandon Hancock
That's amazing.

02:09:43 - Brandon Hancock
What's your last name?

02:09:44 - Brandon Hancock
I want to, we'll connect on LinkedIn.

02:09:47 - Bert
My last name is Chirwa.

02:09:48 - Bert
C-H-I-R-W-A.

02:09:51 - Brandon Hancock
C-H-R-I-W-A.

02:09:54 - Bert
Oh, it's C-H-I-R-W-A.

02:09:57 - Brandon Hancock
Oh, okay.

02:09:58 - Bert
Yeah, but my icon has a bunch of like...

02:10:00 - Bert
Books, like, together to it.

02:10:01 - Bert
So I'll definitely accept you as a LinkedIn referral.

02:10:05 - Brandon Hancock
Chirwa, okay.

02:10:07 - Brandon Hancock
Can they just Bert, first name?

02:10:09 - Brandon Hancock
It's Robert, Robert Chirwa.

02:10:10 - Brandon Hancock
And it's going to be a bunch of books.

02:10:12 - Bert
It's going to be a bunch of O'Reilly books.

02:10:14 - Bert
Old school O'Reilly books.

02:10:16 - Bert
It's a collage of old schooler light books.

02:10:18 - Brandon Hancock
Yeah.

02:10:19 - Brandon Hancock
All right, perfect.

02:10:21 - Brandon Hancock
Oh, wait, I have the wrong button.

02:10:23 - Brandon Hancock
There we go.

02:10:24 - Brandon Hancock
There we go.

02:10:27 - Brandon Hancock
we might...

02:10:30 - Brandon Hancock
Cool.

02:10:30 - Brandon Hancock
Okay.

02:10:33 - Brandon Hancock
Um...

02:10:36 - Brandon Hancock
I'm just going to...

02:10:37 - Brandon Hancock
It won't let me...

02:10:40 - Brandon Hancock
Sorry, I'm just have to, like, send...

02:10:42 - Bert
Okay.

02:10:42 - Brandon Hancock
I don't know why it's not sending.

02:10:44 - Brandon Hancock
Um, if you wouldn't mind sending me one.

02:10:47 - Brandon Hancock
For whatever reason, it's not letting me do it.

02:10:49 - Brandon Hancock
But yeah, Brandon Hancock, you'll see me on LinkedIn.

02:10:51 - Brandon Hancock
So, um, for whatever reason, it won't let me do it.

02:10:54 - Bert
Okay, cool.

02:10:54 - Bert
I'll definitely like...

02:10:55 - Bert
Thank you.

02:10:56 - Bert
Thank you so much.

02:10:57 - Bert
I appreciate it.

02:11:00 - Brandon Hancock
you.

02:11:00 - Brandon Hancock
All right.

02:11:00 - Brandon Hancock
All right, guys.

02:11:01 - Brandon Hancock
Well, hey, I got to hop off too.

02:11:03 - Brandon Hancock
But yeah, seriously, always amazing.

02:11:04 - Brandon Hancock
Get to see everybody.

02:11:05 - Brandon Hancock
So I'd love to hear what you guys are working on.

02:11:08 - Brandon Hancock
If you ever need anything, please shoot me a DM and wrapping up the freelance video, freelance project right now.

02:11:14 - Brandon Hancock
And then I'll be hopping back over to a ton of 80K videos as soon as I get some more, some more free time.

02:11:19 - Brandon Hancock
So I wish I didn't need sleep.

02:11:20 - Brandon Hancock
I'd be so much more productive for you guys, but unfortunately I do.

02:11:24 - Brandon Hancock
So, all right.

02:11:26 - Brandon Hancock
Well, hey, you guys have a great rest of your week and I'll talk to y'all soon.

02:11:28 - Brandon Hancock
Okay.

02:11:30 - Brandon Hancock
Bye, guys.

