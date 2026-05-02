00:00:23 - AbdulShakur Abdullah
Hi, Brendan, how are you?

00:00:25 - Brandon Hancock
Well, hello, hello, how are you doing today?

00:00:27 - AbdulShakur Abdullah
Doing well.

00:00:28 - AbdulShakur Abdullah
Awesome, awesome.

00:00:30 - Brandon Hancock
We'll definitely give everybody a few minutes to hop on.

00:00:34 - Brandon Hancock
I know it's a busy week.

00:00:36 - Brandon Hancock
Let get everything set up notes-wise real fast, guys.

00:00:43 - Brandon Hancock
Awesome.

00:00:46 - Brandon Hancock
Yeah, well, we can get something to set up.

00:00:50 - Brandon Hancock
Well, perfect.

00:00:50 - Brandon Hancock
Well, thanks, guys, for hopping on today.

00:00:55 - Brandon Hancock
I was going to say, definitely, some are starting to be some new faces in the group.

00:01:00 - Brandon Hancock
Bye.

00:01:00 - Brandon Hancock
Thank

00:01:00 - Brandon Hancock
So I'll give a quick overview before we get started just to do rules and everything and then we can dive in.

00:01:06 - Brandon Hancock
So first things first, usually the way we go around the group is we kind of go round robin.

00:01:13 - Brandon Hancock
So I'll drop a screenshot in the chat, basically the order of people I'm seeing on my screen.

00:01:21 - Brandon Hancock
And this is the order I'll end up calling people.

00:01:24 - Brandon Hancock
And usually the way we do it is we do two kind of updates.

00:01:28 - Brandon Hancock
So one, if you have a cool update or topic that you'd like to talk about, feel free to bring it up.

00:01:34 - Brandon Hancock
And then option two is if you're stuck on something or you just want a second pair of like eyeballs on a problem that you're working on, happy to happy to help out with that as well.

00:01:43 - Brandon Hancock
So that's kind of the general gist.

00:01:48 - Brandon Hancock
And Abdul, you were actually first on my list today.

00:01:52 - Brandon Hancock
I'm about to drop it in the chat.

00:01:53 - Brandon Hancock
For some reason, my my computer is just fighting me.

00:01:57 - Brandon Hancock
But yeah, if you want to go first, man, would love to hear what you're working on and how.

00:02:00 - AbdulShakur Abdullah
How are going to help?

00:02:01 - AbdulShakur Abdullah
I'm in the hot seat.

00:02:03 - AbdulShakur Abdullah
So I'm working on connecting a clinical to the clinical trials API with an agent.

00:02:13 - AbdulShakur Abdullah
So I was stuck for a while on getting the agent to directly write the calls, but then I felt like I was kind of making it too complicated.

00:02:25 - AbdulShakur Abdullah
So I switched to making the calls with a Python program and just having the agent pull whatever the person puts in to kind of prompt the Python program.

00:02:38 - Brandon Hancock
So a few quick questions.

00:02:40 - Brandon Hancock
So what is the goal of what we're trying to do?

00:02:43 - Brandon Hancock
And if you have any, like, background on, like, are we using Cray, Langchain, Agent Development Kit?

00:02:49 - Brandon Hancock
And if you want to screen share, too, that's totally awesome as well.

00:02:52 - AbdulShakur Abdullah
Oh, I was using ADK.

00:02:56 - AbdulShakur Abdullah
The goal was basically to...

00:03:00 - AbdulShakur Abdullah
To make it easy for people to query using natural language on any clinical trial, so I could then kind of promote that as a quick reference resource for people.

00:03:15 - Brandon Hancock
Yeah.

00:03:15 - AbdulShakur Abdullah
And I don't have as much development experience, so I was actually going off of your ADK short and kind of rewriting over that.

00:03:30 - Brandon Hancock
Okay, awesome.

00:03:31 - Brandon Hancock
So when you say people query the clinical trials, what are we trying to pull out?

00:03:38 - Brandon Hancock
Just like a research report?

00:03:39 - Brandon Hancock
Are we trying to answer their question and say like, oh, here's the answer to your clinical trial?

00:03:44 - Brandon Hancock
Or what are we trying to do?

00:03:47 - AbdulShakur Abdullah
So people are just trying to look at the clinical trials database where they kind of search.

00:03:54 - AbdulShakur Abdullah
My end goal is eventually to have multiple different databases.

00:03:59 - AbdulShakur Abdullah
My

00:04:00 - AbdulShakur Abdullah
A link together that people in the medical field can kind of reference, so there's quite a lot of free resources out there, but for the clinical trial one, it's just, hey, I have a patient that is showing these symptoms, are there any clinical trials within 100 miles, and then it can do that search without a person trying to use the direct website and reference and pull it up.

00:04:30 - Brandon Hancock
So the goal is to enroll them in the clinical trial, right?

00:04:34 - AbdulShakur Abdullah
What?

00:04:34 - AbdulShakur Abdullah
What was that?

00:04:35 - Bastian Venegas
The is to, the goal is to enroll them in the clinical trial?

00:04:40 - AbdulShakur Abdullah
No, no, the goal is for doctors and other groups to be able to find open or closed clinical trials.

00:04:52 - AbdulShakur Abdullah
In biotech and pharma, quite a lot, we're, we're just searching through clinical trials to see what other companies are

00:05:00 - AbdulShakur Abdullah
Things are doing to see what trials are open if I'm a doctor, if I have a patient that has certain symptoms, to see the trial I was monitoring, if it ended and had a good end point.

00:05:13 - AbdulShakur Abdullah
Then once I find that out from clinical trials, I'll go see if the company published like a press release about it.

00:05:19 - AbdulShakur Abdullah
So let me, I want to say one thing over to you.

00:05:24 - Brandon Hancock
So I'm in the middle of working on the ADK crash course, and I think something that might be super helpful to what you're doing is it's called loop agents.

00:05:38 - Brandon Hancock
So this will be in the crash course, but basically what would be awesome is right now the way ADK works is you submit a request to an agent and it makes a tool call.

00:05:48 - Brandon Hancock
And that's kind of it, like it's a, it's kind of a single shot.

00:05:52 - Brandon Hancock
Did I get the answer?

00:05:53 - Brandon Hancock
Cool.

00:05:53 - Brandon Hancock
And just report back, but what could be really cool is inside of, uh, using a loop agent is.

00:06:00 - Brandon Hancock
You could set up basically two agents in sequence.

00:06:06 - Brandon Hancock
So one would be like a research agent or a planner agent, and the second one would be a research agent.

00:06:12 - Brandon Hancock
And basically, they would work in conjunction to go off and continually research and continually iterate and make additional tool calls until it comes up with a proper plan to report.

00:06:24 - Brandon Hancock
So you would use a series of loop agents and sequence agents.

00:06:29 - Brandon Hancock
So let me – don't worry if it's, like, a little overwhelming, guys, just because, like, Masterclass – literally just finished this today.

00:06:36 - Brandon Hancock
I'm going to start recording tomorrow.

00:06:39 - Brandon Hancock
But here is the important part for you guys to see.

00:06:43 - Brandon Hancock
It basically has – this is, like, a writing version, but you can do the same with research.

00:06:50 - Brandon Hancock
So what you would do is on part one, you would have a loop agent.

00:06:56 - Brandon Hancock
So this is where you would have the, like, planner and

00:07:00 - Brandon Hancock
And the researcher, and they would continually research over and over and over until they hit some sort of max iteration.

00:07:07 - Brandon Hancock
And then afterwards, you would have it create a report that you would then give to, like, a report agent.

00:07:14 - Brandon Hancock
Like, it would have the research, and then you would pass it over to a report agent who would generate that final, the final report to share back with, like, references and everything.

00:07:24 - Brandon Hancock
Does it have to be a max iteration, or can you look for some other endpoint?

00:07:31 - Brandon Hancock
Yeah, so when you say another endpoint, are you talking about another, like, database, or what are we talking about?

00:07:38 - AbdulShakur Abdullah
I'm talking about, like, say, like, some amount of information is found, or no more new trials have been found, or something along those lines.

00:07:53 - Brandon Hancock
Yeah, and also.

00:07:54 - Brandon Hancock
Oh, a bunch of, which lot of features,

00:08:00 - Brandon Hancock
This is found.

00:08:01 - Brandon Hancock
And what you would do is they have this thing called exit loop.

00:08:04 - Brandon Hancock
So as soon as criteria is met, you could say, like, as soon as five resources are found, as soon as three resources are found, you could call exit loop.

00:08:14 - Brandon Hancock
And let me just show you what this looks like.

00:08:16 - Brandon Hancock
And don't worry, like, I am working on something like this.

00:08:20 - Brandon Hancock
But basically, you create a function.

00:08:23 - Brandon Hancock
This function has access to state.

00:08:25 - Brandon Hancock
So, yeah, you would have toolcontext.state, and you could just check the number of resources found greater than five, great, escalate, and return.

00:08:37 - Brandon Hancock
And then that's how you could stop the loop as well.

00:08:39 - Brandon Hancock
So there's so much more that you could do in ADK, so I'm absolutely loving it.

00:08:45 - Brandon Hancock
But, yeah, what I think would be cool is just because I want to make sure everyone has time to go in.

00:08:50 - Brandon Hancock
But, yeah, I think what would be cool is if next time, if you want to incorporate some of this feedback, and if you just want to, like, share code, we could happily go through it and debug it.

00:09:00 - Brandon Hancock
But...

00:09:00 - Brandon Hancock
I think the loop agent and exit loops is exactly what you should look at implementing.

00:09:07 - Brandon Hancock
I think you'll really like it.

00:09:09 - Brandon Hancock
And if you just want a final thing, I'll just go ahead and share it with you guys.

00:09:13 - Brandon Hancock
So this is basically, I put together 11 examples that I was going to, these are the examples I'm going to cover in the tutorial, the crash course.

00:09:23 - Brandon Hancock
I just dropped the repository, so there's a ton of examples in there.

00:09:27 - Brandon Hancock
So if you guys want to go ahead and start looking at some of the like basic all the way to like the workflows at the end, you cannot check there.

00:09:36 - Brandon Hancock
Let me just, just so you guys can see, I'll just show you.

00:09:39 - Brandon Hancock
But yeah, so like the, the two that, or the three that you really need to look at are sequential agents, stateful agents, and then loop agents.

00:09:51 - Brandon Hancock
Those are the three I would look at if I was you.

00:09:54 - AbdulShakur Abdullah
Thank you.

00:09:56 - Brandon Hancock
So perfect.

00:09:56 - Brandon Hancock
Yeah, of course.

00:09:57 - Brandon Hancock
Happy to help.

00:09:57 - Brandon Hancock
No, I'm excited.

00:09:58 - Brandon Hancock
Please shoot me some DMs with progress.

00:10:00 - AbdulShakur Abdullah
Updates, because I'm loving ADK so far, so I want to hear how you like it as well.

00:10:05 - Brandon Hancock
So, perfect.

00:10:07 - AbdulShakur Abdullah
I mean, I am on a Windows machine, so that was annoying with the Windows quirks.

00:10:15 - Brandon Hancock
Yeah, no, Windows is definitely not the easiest on getting things set up, especially with, like, Python environments and everything.

00:10:24 - Brandon Hancock
So, yeah, seriously, and welcome to the call, man.

00:10:27 - AbdulShakur Abdullah
Super excited to have you here.

00:10:28 - AbdulShakur Abdullah
Thank you.

00:10:28 - AbdulShakur Abdullah
Thank you, you.

00:10:30 - AbdulShakur Abdullah
Of course.

00:10:30 - Brandon Hancock
All right, Jake, you are next up, buddy.

00:10:32 - Brandon Hancock
What cool projects are we working on, man?

00:10:35 - Jake Maymar
So, yeah, I totally missed you guys.

00:10:38 - Brandon Hancock
We missed you.

00:10:39 - Jake Maymar
Yeah, yeah, thank you.

00:10:43 - Jake Maymar
So, just doing a lot of pitches, you know, did a whole bunch of POCs, and now just kind of in conversations for building out different things.

00:10:55 - Jake Maymar
So, I will keep you posted, but, yeah, it's been insane.

00:11:00 - Jake Maymar
Okay.

00:11:00 - Jake Maymar
Well,

00:11:00 - Jake Maymar
Yeah, the, they, they're, they're on the West Coast, so it's the exact same time as this meeting, which is like a killer, and I've been trying to like move it.

00:11:14 - Brandon Hancock
So is there, is there any cool info you can share, just like high level about potential type of work, or anything like that, or is it all hush hush?

00:11:24 - Jake Maymar
So much, well, that's the thing, it's like, there's so much, I mean, it's very, very exciting.

00:11:32 - Jake Maymar
I guess I'll say this, we're, we're building a nice sandbox that has all these Lego pieces, and I can definitely share more once that's sort of a little bit more nailed down.

00:11:46 - Jake Maymar
But yeah, I mean, I wish I could share more.

00:11:49 - Jake Maymar
Right now, I'm kind of in that weird state.

00:11:52 - Jake Maymar
As soon as I can, I will, I'm so looking forward to sharing more stuff.

00:11:56 - Brandon Hancock
Dude, you got me interested, and this is just a tease, this is a tease, dude.

00:12:00 - Jake Maymar
No, I know.

00:12:01 - Jake Maymar
But I will say this, that, and I know, I'm just checking in, and I'm like coming up for air and like learning about all these things that like ADK is brand new to me.

00:12:11 - Jake Maymar
I'm like, oh, wow, that's a new thing.

00:12:14 - Jake Maymar
But I will say that there's a tremendous amount of N8N stuff.

00:12:19 - Jake Maymar
And I'm sure you guys talk about that all the time, too.

00:12:24 - Jake Maymar
But yeah, I mean, in general, nothing new to report, just a lot of exciting.

00:12:29 - Jake Maymar
And I'm really looking forward to giving you an update when things are signed.

00:12:34 - Brandon Hancock
Okay, I guess.

00:12:35 - Brandon Hancock
All right.

00:12:35 - Brandon Hancock
Well, we're going to hold you to it.

00:12:37 - Brandon Hancock
And I'd love if, you know, whenever it is signed, like update on how they found you, how conversations went, cool stuff you get to build.

00:12:46 - Brandon Hancock
I think that would be a ton of cool information to share with the group, just because I know a lot of people are also looking to, to get into more, you know, selling services and everything like this.

00:12:55 - Jake Maymar
I can actually share some of those things.

00:12:57 - Brandon Hancock
Okay.

00:12:58 - Jake Maymar
So.

00:13:00 - Jake Maymar
So basically, each individual has an LLC or an S-corp, and as an individual, when you go into a pitch, you're just the individual, so you can only get a certain size budget.

00:13:15 - Jake Maymar
But if you're a team, you can get a larger budget.

00:13:19 - Jake Maymar
And so we've sort of formed teams from these LLCs into teams, and then we go into a pitch as that company.

00:13:30 - Jake Maymar
And I think it's a pretty decent model.

00:13:33 - Jake Maymar
And sort of the way it works is basically the person that wins the job, that's who we go in as.

00:13:46 - Jake Maymar
And then we're kind of waiting on a whole bunch of different things.

00:13:51 - Jake Maymar
And then once one of those is signed, most likely everyone will gravitate towards that and then just start building that.

00:13:57 - Jake Maymar
Because the projects are big enough.

00:14:00 - Jake Maymar
Fathom that it could be it could actually like sustain but but it's kind of getting to that point and yeah so hopefully that's helpful.

00:14:11 - Brandon Hancock
don't know kind of I think it'll once talk more about like the actual project and the contents of it.

00:14:17 - Brandon Hancock
think it'll make more sense.

00:14:18 - Brandon Hancock
But yeah, no, I'm excited.

00:14:20 - Brandon Hancock
Go make those dollars, man.

00:14:22 - Brandon Hancock
I'm excited.

00:14:23 - Brandon Hancock
I'm excited to hear it.

00:14:24 - Jake Maymar
Frost.

00:14:26 - Brandon Hancock
Perfect.

00:14:26 - Brandon Hancock
Anything we can help with?

00:14:28 - Jake Maymar
Oh my god.

00:14:30 - Jake Maymar
So yeah, and this is this is I'm embarrassed to point this out, but I'm still having problems with Next.js TypeScript getting progress bars and getting that whole progress situation sorted out perfectly.

00:14:52 - Jake Maymar
I don't know that that's the main one, but that I think I'd have to kind of go in and share my screen and kind of go through a list of processes.

00:15:00 - Jake Maymar
The other thing I'm kind of curious in general is I've been using a lot of, like, no-code solutions.

00:15:06 - Jake Maymar
I've been using Claw Desktop a lot.

00:15:09 - Jake Maymar
That's freaking amazing.

00:15:12 - Jake Maymar
And I'm curious, is everyone still using Cursor?

00:15:15 - Jake Maymar
Is there another thing?

00:15:18 - Jake Maymar
And are there any open-source models that you are using that you find are actually pretty good for coding?

00:15:27 - Brandon Hancock
So, I mean, I'll just answer.

00:15:28 - Brandon Hancock
I am addicted to Cursor.

00:15:30 - Brandon Hancock
So, that's, I mean, that's me.

00:15:32 - Brandon Hancock
Anyone else, out of curiosity, anything else, Wild?

00:15:37 - AbdulShakur Abdullah
Well, I took a look at RueCode, but I didn't get too far.

00:15:42 - AbdulShakur Abdullah
But I heard Quinn3 was quite good with RueCode.

00:15:46 - Jake Maymar
Oh, that makes sense.

00:15:48 - Jake Maymar
Yeah, RueCode's expensive, though.

00:15:50 - Jake Maymar
That's the only thing.

00:15:51 - Jake Maymar
What's nice about Cursor is it's got, like, a subscription.

00:15:55 - Jake Maymar
Windsurf has a subscription.

00:15:56 - Jake Maymar
But Rue does some amazing stuff, but it's really expensive.

00:16:00 - Jake Maymar
Yeah, that's why with the open, if you use the open source model.

00:16:05 - Jake Maymar
Ah, gotcha.

00:16:06 - Jake Maymar
Now how can you, oh, so then you do like open router with Rue, with Quinn 3.

00:16:13 - AbdulShakur Abdullah
Mm-hmm.

00:16:14 - AbdulShakur Abdullah
Got it.

00:16:15 - Jake Maymar
That makes sense.

00:16:16 - Jake Maymar
Okay, yeah.

00:16:17 - AbdulShakur Abdullah
I, to preface, I haven't gotten it to work for me, so this is just what I heard.

00:16:24 - Jake Maymar
That's fair.

00:16:25 - Jake Maymar
Yeah, I've been using, uh, Klein, um, and, uh, just using it for, um, uh, with Claude, and it's, it kills all the, uh, ESLint errors, which is really, really nice, especially the really, really complex ones.

00:16:43 - Jake Maymar
Um, uh, I don't know.

00:16:45 - Jake Maymar
I don't know if that's helpful or not.

00:16:48 - Brandon Hancock
Yeah.

00:16:48 - Brandon Hancock
So real quick on Rue code.

00:16:50 - Brandon Hancock
So is it, I mean, from what I'm seeing, it cursor alternative, right?

00:16:55 - AbdulShakur Abdullah
Is that the, the, it's a, it's a decline.

00:16:59 - AbdulShakur Abdullah
Um, it's, uh, via.

00:17:00 - AbdulShakur Abdullah
Yes, code, plug-in, but yeah, it's an alternative.

00:17:03 - Jake Maymar
Yeah, Klein is kind of the capable one, and Rue is much more capable.

00:17:12 - Jake Maymar
Rue really does, like, knocks it out of the park almost every single time, but it's expensive, and that's the thing.

00:17:19 - Jake Maymar
So I'm interested in getting Quen 3 to work, because that would be kind of nice.

00:17:24 - Jake Maymar
But the funny thing is, I haven't used Rue in a while, and all of these things are constantly updating, and you know how I love Winsurf.

00:17:34 - Jake Maymar
It's not as good.

00:17:35 - Jake Maymar
Like, something happened, and maybe it's my files or whatever, but something happened, and I just get, I just basically, I mean, I have a subscription, and I have a low cost, because I got in early.

00:17:48 - Jake Maymar
But yeah, I'm looking at Cursor as well, and just kind of looking around to see what solutions are out there.

00:17:56 - Jake Maymar
I guess everyone uses Cursor, right?

00:17:58 - AbdulShakur Abdullah
No, I'm on Winsurf.

00:18:00 - AbdulShakur Abdullah
very

00:18:00 - AbdulShakur Abdullah
Right now, but I also noticed this week that it's been, I just got a new update today.

00:18:07 - AbdulShakur Abdullah
I haven't played around with it too much, but I noticed that I just stopped using Windsurf.

00:18:13 - AbdulShakur Abdullah
actually started just going back and forth between Claude and the cloud or on my desktop and pasting it into Windsurf.

00:18:23 - Jake Maymar
Yeah, that's exactly.

00:18:24 - Jake Maymar
Well, I mean, that's.

00:18:26 - Jake Maymar
And then what's the point, right?

00:18:28 - Jake Maymar
Exactly, exactly.

00:18:29 - Jake Maymar
Well, Claude Desktop, what's interesting is, is Klein did a much better job with ESLint because they're all connected, did a much better job than Claude, which was really surprising.

00:18:41 - Jake Maymar
And maybe it's my prompt and maybe it's other things, but Claude Desktop, I'm pretty much using Claude Desktop all the time now.

00:18:50 - Brandon Hancock
Final thing for moving on.

00:18:53 - Brandon Hancock
Yeah, I mean, I don't about you guys, but I mean, just I still cannot get it off of Cursor just because let me just share.

00:19:00 - Brandon Hancock
Really?

00:19:00 - Brandon Hancock
Like, I use it so much, and, like, it is so hard to go above the limit, and then even when you do, like, it's not wild for how much faster you get to move.

00:19:11 - Brandon Hancock
So, yeah, I mean, I mean, the main thing is just, like, whichever one, the main thing I want to keep in mind is, like, whichever one gives me the solution the fastest that I don't have to keep changing, and Cursor just seems to be industry standard at this point, and I love it.

00:19:24 - Brandon Hancock
Like, I love nothing more than drinking a sip of coffee, and I'm like, build this.

00:19:29 - Brandon Hancock
Here's the example doc.

00:19:30 - Brandon Hancock
Here's what I want.

00:19:31 - Brandon Hancock
Go.

00:19:31 - Brandon Hancock
Nothing makes me happier than it working for me.

00:19:34 - Brandon Hancock
So, yeah, Cursor, man.

00:19:36 - Jake Maymar
So, Brandon, is there any, like, sorry, I was messing with Cursor a back.

00:19:42 - Jake Maymar
Is there any, like, YouTube or links that you'd recommend me looking just so I can get back up to date?

00:19:49 - Jake Maymar
Because I have Cursor, I have it running, but it's kind of one of those things.

00:19:54 - Jake Maymar
I have so many subscriptions, I want to, like, limit it.

00:19:57 - Brandon Hancock
How much, oh, and how much is it a month?

00:19:59 - Jake Maymar
It's, like, 50 bucks a month, or?

00:20:00 - Brandon Hancock
Oh, it's 20.

00:20:01 - Jake Maymar
Okay, that's pretty good.

00:20:04 - Brandon Hancock
Yeah, 20, you get 500 premium calls, unlimited, cheap ones.

00:20:08 - Brandon Hancock
So it's honestly a pretty good deal.

00:20:10 - Brandon Hancock
And then for the Gemini Pro Max, it's 5 cent per thing.

00:20:15 - Brandon Hancock
So that one is getting more expensive.

00:20:18 - Brandon Hancock
yeah, 10 out of 10, would recommend it.

00:20:20 - Brandon Hancock
As for resources, I don't.

00:20:22 - Brandon Hancock
I need to do a video on that just because they have made a bunch of changes.

00:20:26 - Brandon Hancock
You can use agents, you can ask, you can edit.

00:20:28 - Brandon Hancock
There's so much going on, so I need to do that at some point.

00:20:31 - Brandon Hancock
But yeah, so all right, we're going to keep cruising.

00:20:34 - Brandon Hancock
Yeah, keep us in the loop, Jake.

00:20:36 - Jake Maymar
Excited.

00:20:36 - Jake Maymar
Definitely.

00:20:37 - Brandon Hancock
right, Bastian, you are up, my man.

00:20:39 - Brandon Hancock
What projects have we been working on?

00:20:43 - Bastian Venegas
I'm working on a chatbot, so to speak, but it's more like an authentic chatbot because it's powered by the MCP server that I showed last week.

00:20:52 - Bastian Venegas
So it has like 10 or 11 tools, and it's pretty cool because it renders, also renders

00:21:00 - Bastian Venegas
So I'll just briefly show my screen.

00:21:04 - Brandon Hancock
Okay, So it's like a 30-second update on what you did.

00:21:16 - Bastian Venegas
Yeah, so yeah, give me a second.

00:21:21 - Bastian Venegas
So I, last week I showed this in cloud desktop and it has access through the MCB.

00:21:31 - Bastian Venegas
Oh, it needs to load.

00:21:33 - Bastian Venegas
But basically it's a bunch of tools that give access to internet, to researching papers, to some custom like ways of thinking, basically prompts, hidden espace tools.

00:21:47 - Bastian Venegas
And some stuff like to render React artifacts or streaming components directly into the UI.

00:21:55 - Bastian Venegas
these are the 11 tools.

00:21:58 - Bastian Venegas
It also optimizes the test sequence.

00:22:00 - Bastian Venegas
It does some likelihood and probability calculations and stuff like that.

00:22:04 - Bastian Venegas
So it's like a very specific product meant to people that work in health and need to research some clinical cases and stuff like that.

00:22:13 - Bastian Venegas
And I am just porting all of the functionality to this thing I forked from Vercel that it also renders like these artifacts.

00:22:26 - Bastian Venegas
You can render them in line or you can render them as a side panel.

00:22:31 - Bastian Venegas
And for example, this is one of the custom tools I, well, this is not very interesting because it only has one data point, but what's the weather in San Francisco and now in a graph bar, please.

00:22:41 - Bastian Venegas
And this is like two different tool calls.

00:22:45 - Bastian Venegas
And basically what the client detects that there's, it continuously parses the streamed answer.

00:22:52 - Bastian Venegas
And when it detects that it's an avatar that it recognizes, it just renders it.

00:22:57 - Bastian Venegas
So that's pretty cool.

00:22:59 - Bastian Venegas
And it also...

00:23:00 - Bastian Venegas
So it can show you, like, if you use a reasoning model, it will show you, like, the traces, depending on the model, but Glock, it will show you the reasoning traces, so that's pretty fun.

00:23:11 - Bastian Venegas
And something that I've found very useful is, like, well, this may be basic, but using, like, debug panels so you don't rely completely on the console or the terminal because it gets crowded way too soon when you just copy and paste everything that you're getting from the terminal.

00:23:27 - Bastian Venegas
So, like, basically, in Next.js or React apps, like, being able to trace your tool calls in details and how the states are being passed, I found that pretty useful.

00:23:40 - Bastian Venegas
But, yeah, next week I have more to share, but right now I'm trying to debug the extra functionalities I introduced.

00:23:48 - Brandon Hancock
Okay, perfect.

00:23:50 - Brandon Hancock
I also, you know, I'm on an 80K kick right now, so I would be very curious how...

00:23:57 - Brandon Hancock
how easy it would be to recreate the 11Tool phone.

00:24:00 - Brandon Hancock
Functionality inside of ADK, because I think you have one agent connected up to the MCP server, correct?

00:24:07 - Bastian Venegas
Yeah.

00:24:08 - Brandon Hancock
Okay.

00:24:09 - Brandon Hancock
Yeah.

00:24:09 - Brandon Hancock
I would just be curious to see side by side how much you like the other one better.

00:24:15 - Bastian Venegas
I definitely want to check that out.

00:24:17 - Bastian Venegas
And I think that they have this also a protocol like A2A that you can actually connect the MCP to and should be easier to put it in like their framework.

00:24:29 - Bastian Venegas
So, yeah, that's definitely I want to explore that.

00:24:32 - Brandon Hancock
Okay, dude, perfect.

00:24:33 - Brandon Hancock
Well, please keep us posted.

00:24:34 - Brandon Hancock
are currently our MCP resident expert.

00:24:36 - Brandon Hancock
And for some of you guys who weren't around last week, I dropped a tutorial that I saw a few weeks ago.

00:24:46 - Brandon Hancock
Dave dropped it, Albert, and I think it was probably one of the best MCP tutorials I've seen out there.

00:24:52 - Brandon Hancock
So, just if you want some reading or some YouTube watching, it's an hour-long video, but he goes pretty deep into it.

00:24:59 - Brandon Hancock
It's all Python, Crash Course.

00:25:00 - Brandon Hancock
So yeah, definitely, if you are going into MCP, would definitely recommend checking that out.

00:25:05 - Brandon Hancock
So, perfect.

00:25:07 - Brandon Hancock
Any things we can help with, though?

00:25:09 - Brandon Hancock
Question?

00:25:09 - Brandon Hancock
you just need more time of the day to work?

00:25:13 - Bastian Venegas
Yeah, that's it.

00:25:14 - Bastian Venegas
Now I have to give you what's failing now, and I'm just getting used to...

00:25:21 - Bastian Venegas
I mean, states are kind of hard, but yeah.

00:25:26 - Brandon Hancock
Yeah, I feel you.

00:25:28 - Brandon Hancock
That's the final thing on ADK.

00:25:30 - Brandon Hancock
I really like that so far, because it comes with built-in state, which is so nice, because you can update the state before the agent call.

00:25:38 - Brandon Hancock
After the agent call, the agent itself can update the state.

00:25:41 - Brandon Hancock
Tools can update the state.

00:25:42 - Brandon Hancock
Like, it was made with state in mind, which is pretty nice, because without state management, you have to do it yourself.

00:25:51 - Brandon Hancock
And then it can get very complicated on how do you want things to interact with it.

00:25:56 - Bastian Venegas
Yeah.

00:25:56 - Bastian Venegas
Doing anything React particularly sucks.

00:25:58 - Brandon Hancock
Yeah.

00:26:00 - Brandon Hancock
I got you.

00:26:00 - Brandon Hancock
Perfect.

00:26:01 - Brandon Hancock
All right.

00:26:01 - Brandon Hancock
Well, next up, Sam, what's going on, buddy?

00:26:07 - Sam
Not a lot.

00:26:07 - Sam
I appreciate Jake's question because I was going ask something similar about Cursor and Winsurf.

00:26:12 - Sam
I'm now going to share what you shouldn't do, but I'm using GitHub Copilot and utilizing their bring your own model feature.

00:26:21 - Sam
But I'm just connecting back on the free tier back to a resource that the company has within Azure because they're so...

00:26:31 - Sam
They're seriously concerned about data security, and it's a bit hard for me to get any leverage, so that was the best that I could do.

00:26:37 - Sam
And the funny thing is, even though I'm supplying my own model on the free tier, it still counts on their limits.

00:26:44 - Sam
So when I'm hitting up, they must just haven't developed it yet because it's a free tier.

00:26:51 - Brandon Hancock
Oh, I gotcha.

00:26:52 - Sam
So you're hitting at it.

00:26:55 - Sam
Yeah.

00:26:55 - Brandon Hancock
Out of curiosity, if you did...

00:26:57 - Brandon Hancock
Let me show you something really quick.

00:26:58 - Brandon Hancock
I'm just curious.

00:27:00 - Brandon Hancock
Let me move my screen around.

00:27:03 - Brandon Hancock
If you did this, I'm curious if this would work.

00:27:07 - Brandon Hancock
I'm going to show my screen really quickly.

00:27:09 - Brandon Hancock
Share.

00:27:11 - Brandon Hancock
Share.

00:27:12 - Brandon Hancock
Okay, cool.

00:27:13 - Brandon Hancock
So if you inside a cursor did models and if you brought your own like Azure API key and set up like your deployment information, I'd be very curious if you could then use some of the open AI models because you could in your own private Azure network that you control everything security wise, if this would work for you because then, you know, the second you have this, you can use open AI.

00:27:42 - Brandon Hancock
And at that point, you're not really worried about rate limits.

00:27:45 - Brandon Hancock
Might be a nice way to work around it because I know a lot of companies like they allow either Microsoft or AWS.

00:27:53 - Brandon Hancock
Those are usually the two, so I would be curious if you could start to use these and this is how you get to this setting.

00:28:01 - Brandon Hancock
So, just an idea.

00:28:03 - Sam
I have a fiddle with that.

00:28:04 - Sam
don't think that, yeah.

00:28:06 - Sam
As long as it's going, I can say it's going there with my hand and my heart, they should be fine with it.

00:28:11 - Sam
The only other critical I have is...

00:28:12 - Bastian Venegas
inside Cursor, but not with the agent, I think.

00:28:16 - Bastian Venegas
Or at least, because they don't charge you for those API calls, they limit the functionality.

00:28:23 - Bastian Venegas
Or they used to.

00:28:24 - Brandon Hancock
Do you know what they limit, Bastian, out of curiosity?

00:28:28 - Bastian Venegas
What, what cursor limits or Azure?

00:28:30 - Brandon Hancock
Yeah, so if you do use the API, like I showed, do you know what they limit?

00:28:35 - Brandon Hancock
Is it strictly the agent feature?

00:28:38 - Bastian Venegas
The agent features.

00:28:39 - Brandon Hancock
Oh, yeah.

00:28:41 - Bastian Venegas
The configuration you mentioned works, I've used it before, but at least the last time I checked, which was like a month ago, they didn't let you use the full agent feature.

00:28:52 - Brandon Hancock
I got you.

00:28:54 - Bastian Venegas
But you can use even O3 and O4 Mini, they're, they're, if you're like startup trades and obviously...

00:29:00 - Bastian Venegas
You pay the plan, you can use pretty much every model.

00:29:03 - Brandon Hancock
So I think what he's saying is you can't use the agent where it iterates over and over and over, but you can probably use ask.

00:29:11 - Brandon Hancock
Yeah, you can probably use ask, which is like, hey, how would I do this?

00:29:15 - Brandon Hancock
And it'll spit out the code, and it would probably just be up to you to copy and paste it in.

00:29:19 - Brandon Hancock
So it's probably, it's not obviously as nice as the agent feature, but it definitely would probably be easier than what you currently It's than like a tablet, it's like, at least you have the thing in your actual code base, and it can read the files.

00:29:34 - Sam
I'll do that one.

00:29:36 - Sam
The only other question I had is anyone, has anyone vibe checked the GPT 4.1 models?

00:29:44 - Sam
Because I wanted to have a look at, they claim their million context window, I haven't been able to get access to it just because of, you know, work stuff.

00:29:52 - Sam
But I'm really interested to know how good they are over that million context they claim to have, and if they are any better than Google.

00:30:01 - Brandon Hancock
So the main thing I'll mention is the biggest improvement I noticed, which they called out, was the instruction following.

00:30:08 - Brandon Hancock
It actually is really good at like, hey, you need to do this, make sure you do this, and then it does it.

00:30:15 - Brandon Hancock
Because I can't tell you the number of times I'll add into a model.

00:30:18 - Brandon Hancock
Like, please, dear God, stop doing this.

00:30:20 - Brandon Hancock
And it's like, eh, I forgot, you know?

00:30:23 - Brandon Hancock
So the 4.1 is one of the first ones to where I clearly just say like important.

00:30:28 - Brandon Hancock
And I have bullet list of important things it should not do, and that it should do, and it actually follows.

00:30:33 - Brandon Hancock
With that said, though, I haven't got to try it at the million token limit yet.

00:30:38 - Brandon Hancock
But I did, I can't remember who brought it up last week.

00:30:42 - Brandon Hancock
But they, OpenAI did drop their prompt guide.

00:30:45 - Brandon Hancock
I can't remember if someone remembers who brought it up.

00:30:49 - Bastian Venegas
Andrew did.

00:30:51 - Brandon Hancock
But Andrew brought up an awesome resource last time.

00:30:53 - Brandon Hancock
I'm going to drop it in the chat because they, it is very insightful.

00:30:59 - Brandon Hancock
And I'm going to call.

00:31:00 - Brandon Hancock
Oh, the important thing Andrew showed last week, which was down at the bottom of this guide.

00:31:07 - Brandon Hancock
Yeah, so for instruction following, the main thing that's important once you get to longer phrases is to – they said for best results, when you do get to that million token or just like some of the higher ones, to put it at the beginning and end.

00:31:24 - Brandon Hancock
Let me look at this real fast.

00:31:27 - Brandon Hancock
Yeah.

00:31:27 - Brandon Hancock
So prompt organization, they just recommend when you get long context windows to read some of the important instructions at the beginning and end.

00:31:37 - Brandon Hancock
So just a quick, you know, a quick point out of – because I would have never noticed that without reading this.

00:31:43 - Brandon Hancock
So hopefully that's helpful.

00:31:46 - Brandon Hancock
But yeah.

00:31:48 - Sam
Yeah, that's excellent.

00:31:51 - Brandon Hancock
All right, perfect.

00:31:52 - Brandon Hancock
Thank you.

00:31:52 - Brandon Hancock
Oh, of course, of course.

00:31:54 - Brandon Hancock
Yeah, like I said, shout out to Andrew for calling that one out.

00:31:56 - Brandon Hancock
So, um, okay, great.

00:31:59 - Brandon Hancock
Um, all right.

00:32:00 - Brandon Hancock
So let's keep on cruising, guys.

00:32:02 - Brandon Hancock
Paul, you're up, my man.

00:32:03 - Brandon Hancock
What's going on?

00:32:05 - Paul Miller
Well, I took the dive.

00:32:08 - Paul Miller
You inspired me, Brandon, with your cool, lovable video, and I've been holding off and holding off.

00:32:18 - Paul Miller
Basically, so I've got a client and kind of operates in a similar space.

00:32:23 - Paul Miller
It's one of the things that Sam is focused on.

00:32:28 - Paul Miller
So he does, he's a civil engineer, and he works with customers to look at land, like farmland, that is getting converted into subdivisions.

00:32:44 - Paul Miller
So a lot of different factors that go into that, and I've been working with him to lobby the government to make sure that we can better fund new infrastructure.

00:32:56 - Paul Miller
Because when you build a subdivision, you've got to think about.

00:33:00 - Paul Miller
Well, who's going to pay for the infrastructure?

00:33:02 - Paul Miller
The people that already have houses with pipes and wires and all the rest of it, they don't want to pay for other people's new infrastructure.

00:33:11 - Paul Miller
And when you're buying a new house, some new subdivision, you don't want all those costs up front because it's pretty blooming expensive to buy a house everywhere in the developed world, at least.

00:33:25 - Paul Miller
So the scenario was this guy had a really good spreadsheet, but he said, oh, I'd take it through the spreadsheet.

00:33:32 - Paul Miller
And people can play with that, but everyone knows how crappy spreadsheets are.

00:33:36 - Paul Miller
So I thought, ah, this is what I could take through, lovable.

00:33:40 - Brandon Hancock
So if I can just share my screen, I'll show you how it you built it.

00:33:45 - Brandon Hancock
Oh, heck yeah.

00:33:46 - Paul Miller
I built it.

00:33:47 - Paul Miller
So before I turn it on, so the use case is I'm a government economist that has no understanding of actual commercial obligations of if I go and change the cost.

00:34:00 - Paul Miller
Most of stuff, what's the influence on the section price for someone wanting to build a home?

00:34:07 - Paul Miller
So let me just share that with you.

00:34:11 - Paul Miller
Let's see if share the right screen.

00:34:13 - Paul Miller
Here we go.

00:34:14 - Paul Miller
Right.

00:34:15 - Paul Miller
Can you see my screen?

00:34:17 - Brandon Hancock
Yep.

00:34:17 - Brandon Hancock
Yep.

00:34:18 - Brandon Hancock
Looks great.

00:34:19 - Brandon Hancock
Dude, it kind of looks like Zillow-esque, like the little sidebar.

00:34:22 - Paul Miller
I'm liking it.

00:34:23 - Paul Miller
Yeah.

00:34:23 - Paul Miller
Yeah.

00:34:24 - Paul Miller
Look, I need to do some UI, UX tweaks.

00:34:29 - Paul Miller
Probably from a UX perspective, but it's got a bit of work, but I'm getting some AI.

00:34:36 - Paul Miller
The AI's made a few suggestions, and I just need to test it with the user.

00:34:40 - Paul Miller
So one of the things that impacts the prices or impacts the equation, so the key thing for the user is what is the section price?

00:34:50 - Paul Miller
This is New Zealand dollars, not US dollars for people freaking out, thinking, what the hell this island is?

00:34:56 - Paul Miller
How expensive is it?

00:34:58 - Paul Miller
But it's what is the...

00:35:00 - Paul Miller
Influence on what does the section price need to be if you change these other factors?

00:35:07 - Paul Miller
So you start changing density from low to high, and you see all these other costs automatically start changing.

00:35:15 - Paul Miller
You start changing the number of plots for the piece of land.

00:35:21 - Paul Miller
You start adjusting the loan periods that influence interests.

00:35:27 - Paul Miller
How much is the developer contributing, which again influences everything, external additional construction costs.

00:35:35 - Paul Miller
So the government is saying, oh, we can do this, we'll drop the market, and then suddenly the price of land will become cheaper.

00:35:42 - Paul Miller
It's like, well, that's only one factor.

00:35:46 - Paul Miller
And then you've got all of these different factors.

00:35:48 - Paul Miller
So say if you're a wealthy entrepreneur, you buy a large block of land, and you convert it into house lots.

00:35:59 - Paul Miller
So say

00:36:00 - Paul Miller
Sell individually and put all the infrastructure in.

00:36:02 - Paul Miller
This is the kind of commercials that you need to be able to look at.

00:36:06 - Paul Miller
And then we've kind of got some visualizations.

00:36:08 - Paul Miller
This one down the bottom is a bit crap, but I need to tweak on that to try and make it easier for people to understand where the break-even point is.

00:36:18 - Paul Miller
But we're hiding all of the specific details that make up the numbers below.

00:36:25 - Paul Miller
So what's the interest rate?

00:36:27 - Paul Miller
What's the land being purchased for?

00:36:30 - Paul Miller
So keep that hidden out of the way, but all able to be changed for different parts of the library.

00:36:38 - Brandon Hancock
So this is sick.

00:36:40 - Brandon Hancock
So I have a few questions for you.

00:36:43 - Brandon Hancock
So tech-wise first, and then project implementation next.

00:36:47 - Brandon Hancock
So you use Lovable.

00:36:50 - Brandon Hancock
I'm guessing you had to go to the pro tier, right?

00:36:52 - Brandon Hancock
So probably.

00:36:54 - Brandon Hancock
Okay.

00:36:55 - Brandon Hancock
Are you still under the 100 limit?

00:36:56 - Brandon Hancock
Or where are you at?

00:36:57 - Brandon Hancock
Or did you have to go back scale?

00:37:00 - Brandon Hancock
Did you?

00:37:00 - Paul Miller
Look, I think the first challenge was when you're new at it, you're probably not as organized with getting efficient multiple things in one prompt.

00:37:11 - Paul Miller
So you're going backwards and forwards.

00:37:13 - Paul Miller
I like the version two, and I do note in your training video, you can go in and quickly edit stuff without putting that through the prompt.

00:37:21 - Paul Miller
So I'm taking advantage of that and minimizing the number of edit trips.

00:37:28 - Paul Miller
Because I didn't have immediate access to your GPT, which I've got now, so what I did was the client had a spreadsheet, which was the base kind of formula.

00:37:42 - Paul Miller
So I took the spreadsheet, I put it through, I actually put it through either OpenAI with one of their top models, or I took it through Claude, and I got...

00:38:00 - Paul Miller
A clawed to analyze, clawed a GPT to analyze the spreadsheet, derive all of the things that it was trying to do, and build a prompt description that then I copied into Lovable.

00:38:16 - Brandon Hancock
This is amazing.

00:38:19 - Brandon Hancock
This is amazing.

00:38:20 - Paul Miller
This is awesome.

00:38:21 - Paul Miller
It was so quick to get to that.

00:38:25 - Paul Miller
A few more questions for you.

00:38:26 - Brandon Hancock
Time.

00:38:27 - Brandon Hancock
I know you say quick, but to get to this.

00:38:29 - Brandon Hancock
What are we all in?

00:38:31 - Brandon Hancock
Three, five, ten hours?

00:38:32 - Brandon Hancock
How many hours to make this?

00:38:35 - Paul Miller
Probably about six hours.

00:38:37 - Brandon Hancock
Six hours?

00:38:38 - Brandon Hancock
But still, that's crazy.

00:38:39 - Paul Miller
But that's going to the client and saying, all right, give us feedback.

00:38:45 - Paul Miller
Let's talk about this.

00:38:47 - Paul Miller
Is that where you want it to be?

00:38:49 - Paul Miller
And just going backwards and forwards.

00:38:51 - Paul Miller
So a lot of that, so that's not, that six hours isn't me sitting around lovable to try and do it.

00:38:58 - Paul Miller
But that's talking with the client and just.

00:39:00 - Brandon Hancock
Getting their feedback.

00:39:01 - Paul Miller
So it's probably lovable time, maybe two and a half hours.

00:39:05 - Paul Miller
That's awesome.

00:39:06 - Paul Miller
That makes me so happy.

00:39:08 - Brandon Hancock
Okay, a few other questions.

00:39:09 - Brandon Hancock
Now, we have MVP up.

00:39:13 - Brandon Hancock
I noticed there's a little login dude in the top right.

00:39:16 - Brandon Hancock
Are you going to connect it to Superbase?

00:39:19 - Paul Miller
What's your game plan?

00:39:20 - Paul Miller
Yeah.

00:39:21 - Paul Miller
So what I want to do is I want to connect it to Superbase.

00:39:25 - Paul Miller
I want to, because the guy doesn't want this, he wants to control who looks at it and put in, so different people might be coming from different parts of the country where the base cost of land is different and the cost of building is different.

00:39:44 - Paul Miller
And we need to be able to measure success.

00:39:47 - Paul Miller
So for his clients, how many have used the tool?

00:39:53 - Paul Miller
Which pages do they look at and what do they do with it?

00:39:57 - Paul Miller
Because you kind of want to say, all right, I'll spend all this money and time building this.

00:40:00 - Paul Miller
For you, here's how much your clients are using for it.

00:40:03 - Paul Miller
So then it's kind of self-fulfilling as a SaaS tool that you say, well, ah, you know, you're actually getting the benefit.

00:40:10 - Paul Miller
This client got to this point.

00:40:11 - Paul Miller
So when you ring them up and pop them through the next stage, you've got the context that they've actually used the tool or they haven't.

00:40:20 - Brandon Hancock
No, that's awesome.

00:40:21 - Brandon Hancock
I want to share with you one thing super fast.

00:40:24 - Brandon Hancock
I'm going to stop sharing your screen, but I think this would be super helpful.

00:40:30 - Brandon Hancock
Let's show.

00:40:31 - Brandon Hancock
Okay, so it's called PostHog.

00:40:33 - Brandon Hancock
So it sounds like your user wants to understand who you're building this for, what, basically, what are user behaviors over time.

00:40:44 - Brandon Hancock
And a tool like PostHog would be amazing for what you're trying to do for two reasons.

00:40:51 - Brandon Hancock
One, let me zoom in, is for funnel analytics.

00:40:54 - Brandon Hancock
So, like, it sounds like he has a bunch of people who are going to use it.

00:40:57 - Brandon Hancock
So, like, of the people who signed in, how many of.

00:41:00 - Brandon Hancock
One them filled out their profile, and then after that, how many of them went off and did their first search?

00:41:05 - Brandon Hancock
So product analytics would be the first.

00:41:08 - Brandon Hancock
And the other one that would be awesome is, let me see if they have a quick example.

00:41:13 - Brandon Hancock
I mean, session replay is nice.

00:41:16 - Brandon Hancock
Where is it at?

00:41:17 - Brandon Hancock
There's one other feature.

00:41:20 - Brandon Hancock
It might be the web analytics.

00:41:22 - Brandon Hancock
I can't remember off top of my head, but long story short, you can record post.

00:41:27 - Brandon Hancock
So every time someone does a search, you can look up where they searched and different parameters.

00:41:33 - Brandon Hancock
So over time, you can see like, okay, 60% of all search requests are on this one specific area.

00:41:40 - Brandon Hancock
You know, so you get to kind of look at like, oh, okay, this is a hot area.

00:41:44 - Brandon Hancock
But then you can also look at like, oh, wait, out of, you know, 60% of those requests were about this one search area, but they all came from a single user.

00:41:53 - Brandon Hancock
So it's just like, oh, we have one power user who's skewing our data.

00:41:56 - Brandon Hancock
Take him out.

00:41:57 - Brandon Hancock
You know, so there's, there's, and yeah, so post hoc is.

00:42:00 - Brandon Hancock
It's what I would use as you get it built and want to add analytics.

00:42:04 - Brandon Hancock
It's stupid cheap too.

00:42:06 - Brandon Hancock
So yeah, 10 out of 10 recommend looking at this as well.

00:42:10 - Brandon Hancock
I mean, it's like pennies.

00:42:11 - Brandon Hancock
It's pennies of pennies, you know?

00:42:13 - Brandon Hancock
Yeah.

00:42:15 - Paul Miller
I think using that for my main SaaS product would be quite good because it's always a challenge.

00:42:22 - Paul Miller
It's like we've got all these customers using the SaaS service, but you don't know if they're fully using the tool and you kind of want to prompt them if they're not to say, hey, if you use that feature, that's going to give you this and give you that, especially at that price.

00:42:38 - Paul Miller
Yeah.

00:42:39 - Brandon Hancock
It's so funny.

00:42:40 - Brandon Hancock
Thank you, Bastian.

00:42:40 - Brandon Hancock
We caught out the same thing at the same time.

00:42:42 - Brandon Hancock
That's funny.

00:42:44 - Brandon Hancock
I was just looking at chat.

00:42:45 - Brandon Hancock
But yeah, last thing on that.

00:42:46 - Brandon Hancock
I mean, previous startups I've worked at, this is how we, not Postdoc specifically, but a tool just like it.

00:42:52 - Brandon Hancock
This is how we determined, like, if we were going in the right direction, we used it to figure out if people were going to churn.

00:42:58 - Brandon Hancock
The second you have analytics set up properly.

00:43:00 - Brandon Hancock
My God, it's like you were blind to your app because you just, you knew people were on it, but how many, what were they doing?

00:43:06 - Brandon Hancock
I don't know.

00:43:07 - Brandon Hancock
I just know I'm getting a bill every month because people keep trying to do stuff, but what's going on?

00:43:12 - Brandon Hancock
I have no idea.

00:43:13 - Brandon Hancock
So the second you get that implemented, it's night day.

00:43:15 - Brandon Hancock
So 10 out of 10 would recommend.

00:43:18 - Paul Miller
Brilliant, brilliant.

00:43:19 - Paul Miller
Well, thanks again.

00:43:20 - Paul Miller
You inspired me and actually built something for once.

00:43:26 - Brandon Hancock
Well, tell Lovable.

00:43:28 - Brandon Hancock
So they, uh, they give me another, uh, sponsored video, please.

00:43:31 - Paul Miller
You know, I'll do something in Twitter.

00:43:34 - Brandon Hancock
Yeah, perfect.

00:43:35 - Paul Miller
Thanks.

00:43:36 - Paul Miller
Thanks.

00:43:36 - Brandon Hancock
Thanks, Paul.

00:43:37 - Brandon Hancock
All right.

00:43:38 - Brandon Hancock
Uh, Sagar, you're up next, buddy.

00:43:40 - Brandon Hancock
What's going on?

00:43:41 - Sagar Passi
Doing well.

00:43:42 - Sagar Passi
How is everyone?

00:43:44 - Sagar Passi
Paul, that was amazing at the UI.

00:43:45 - Sagar Passi
Really impressed.

00:43:47 - Brandon Hancock
definitely got a copy a bit of that.

00:43:49 - Sagar Passi
Um, I've been away from this group for a couple of days or weeks.

00:43:54 - Sagar Passi
Um, I finally got my head.

00:43:57 - Sagar Passi
I've got my, I went down the rabbit hole.

00:44:00 - Sagar Passi
Oh.

00:44:00 - Sagar Passi
It's.

00:44:00 - Sagar Passi
And I'm getting pushed from a lot of companies in the UK on how do we implement it.

00:44:07 - Sagar Passi
So I'm here for advice from you guys on how would you recommend all the new technologies coming out there?

00:44:15 - Sagar Passi
How would you do agentic teams?

00:44:17 - Sagar Passi
What is the architecture?

00:44:19 - Sagar Passi
How do I keep this safe from a governance point of view?

00:44:22 - Sagar Passi
And all is please tell me what to do.

00:44:25 - Brandon Hancock
Okay, so I'm going to ask a few quick questions.

00:44:28 - Brandon Hancock
So when you say agentic teams, you are referring to I am an organization and a business.

00:44:34 - Brandon Hancock
Let's just say I'm the marketing team.

00:44:35 - Brandon Hancock
And now I want help in order to manage LinkedIn posts.

00:44:40 - Brandon Hancock
I want help, you know, all the operations I would normally do, you know, basically having the co-pilot for through agentic apps to help out everyone on the internal team.

00:44:51 - Brandon Hancock
Like that's what we're that's what we're talking about.

00:44:53 - Sagar Passi
Yep.

00:44:53 - Sagar Passi
Yep.

00:44:54 - Sagar Passi
So operations, mainly in the financial services, reinsure that kind of market.

00:45:00 - Brandon Hancock
Okay.

00:45:00 - Brandon Hancock
So, all right, so I'm to give you two branches really quickly.

00:45:04 - Brandon Hancock
So, if your customers have deeper pockets, I would have really explored Crew AI Enterprise for a few reasons.

00:45:15 - Brandon Hancock
One, they have, at least they're going down this path, I'm not sure if it's fully built in yet, but there is the ability to set up permissions and authentication around agents, which is huge, tracing is also built in, it's very easy to track, and then outside of that, some places like on-premise solutions, and they have a factory installation.

00:45:40 - Brandon Hancock
So, like, if you're working with the big clients that are like, hey, I'm minimum trying to spend $20,000, $30,000 plus more, you know, there's some factory solutions that I would look at exploring.

00:45:53 - Brandon Hancock
It is more pricey, like very pricey, but the data never leaves the building, and they get the benefit of agentic application.

00:46:00 - Brandon Hancock
Which is like, it's a requirement for some big organizations.

00:46:04 - Brandon Hancock
Okay, now, so that is enterprise side.

00:46:08 - Brandon Hancock
For the average developer, I'm getting hyper bullish on agent development kit.

00:46:14 - Brandon Hancock
I really like a lot of what they're doing, excuse me, specifically around pricing.

00:46:20 - Brandon Hancock
It is wild how affordable it is to now build agent teams.

00:46:24 - Brandon Hancock
Meaning you can now, or just agents in general.

00:46:28 - Brandon Hancock
So, time you deploy an agent, it's like 11 cent per hour per run.

00:46:33 - Brandon Hancock
Or, yeah, per, yeah, per use, oh, sorry, I'm gonna say this again.

00:46:37 - Brandon Hancock
It's 11 hours, it's 11 cent per hour.

00:46:40 - Brandon Hancock
And that's just at runtime.

00:46:42 - Brandon Hancock
So if it's up for 30 minutes and it dies, cool, you paid a nickel.

00:46:45 - Brandon Hancock
You know, obviously you're paying for tokens, but like, it's dirt cheap.

00:46:48 - Brandon Hancock
Like, there's no other framework that is that cheap right now for deployed agents.

00:46:53 - Brandon Hancock
So, yeah, mean, crew is session-based, so it's 50, 40, somewhere bucks a month.

00:46:58 - Brandon Hancock
And you can run up to three.

00:47:00 - Brandon Hancock
Three or five agents or crews, which is like 100X of what Google's charging.

00:47:07 - Brandon Hancock
It's just hard to compete against Google because they're not making money off agents.

00:47:10 - Brandon Hancock
They're making money off YouTube and search.

00:47:12 - Brandon Hancock
So they're just undercutting what everyone else can do.

00:47:13 - Brandon Hancock
So as a developer, though, I appreciate the cheapness.

00:47:18 - Brandon Hancock
So I do really, really like that.

00:47:21 - Brandon Hancock
Okay, a few other things I think you would really like.

00:47:25 - Brandon Hancock
One thing I have fallen in love with ADK recently is their chat functionality.

00:47:30 - Brandon Hancock
Meaning you can quickly spin up agents without a UI or anything else and just give people a chat-like interface like you would do with ChatGPT.

00:47:39 - Brandon Hancock
Except behind the scenes, there's some hardcore agents accessing internal data, doing whatever they need to do to deliver results.

00:47:47 - Brandon Hancock
And people can just chat with it like they're chatting with ChatGPT.

00:47:51 - Brandon Hancock
Super valuable for MVPs because, yes, later on you can go off and add all the nice UI elements and get everything pretty.

00:47:57 - Brandon Hancock
But for a quick MVP, that chat functionality.

00:48:00 - Brandon Hancock
It is a game changer.

00:48:03 - Brandon Hancock
Let me see if there's anything else.

00:48:05 - Brandon Hancock
If you have a few questions off of anything I've said, I'm happy to keep going, too.

00:48:11 - Sagar Passi
With the CREI or any agentic framework, how do you guys do the orchestration?

00:48:18 - Sagar Passi
You know, if I do a parallel flow or I do a team flow or a prompt chaining flow, how can I choose that dynamically with what tasks are happening?

00:48:28 - Brandon Hancock
Okay, so I'm going to share a screenshot really fast, and I will show you, okay, so I'm to go, I'm basically in the ADK, let me just, agent, so like I said, crash course coming out soon, this specific question will get answered, but let me show you.

00:48:50 - Brandon Hancock
Okay, so they have, inside of ADK, a super nice feature, where is it at, sorry guys, I'm just.

00:49:00 - Brandon Hancock
I'm trying to look for their docs.

00:49:02 - Brandon Hancock
Get started.

00:49:07 - Brandon Hancock
Agents.

00:49:10 - Brandon Hancock
Okay, here it is.

00:49:11 - Brandon Hancock
Okay, so the thing you're looking for specifically within agents is workflow agents, and there are different types.

00:49:18 - Brandon Hancock
So there are sequential agents, which are, hey, every time I call this agent, I want it to do these specific things.

00:49:26 - Brandon Hancock
Like I want it to do task A, B, C.

00:49:28 - Brandon Hancock
So think a crew.

00:49:29 - Brandon Hancock
I want it to do A, B, C.

00:49:31 - Brandon Hancock
And then for other things, a loop agent is like what we were talking earlier.

00:49:37 - Brandon Hancock
Oh, wait, sorry, I'm not sharing my screen.

00:49:39 - Brandon Hancock
Here, wait, sorry.

00:49:39 - Brandon Hancock
One second.

00:49:41 - Brandon Hancock
Sorry, let me, here, wait, one second.

00:49:42 - Brandon Hancock
My thing's messing up.

00:49:43 - Brandon Hancock
One second.

00:49:53 - Brandon Hancock
I got a new, I did an update, and it has destroyed my sharing abilities.

00:49:58 - Brandon Hancock
Never update a Mac is the lesson.

00:50:00 - Brandon Hancock
Unlearned.

00:50:00 - Brandon Hancock
But okay, so it should be sharing.

00:50:02 - Brandon Hancock
Can you see it, guys?

00:50:03 - Sagar Passi
Yep.

00:50:04 - Sagar Passi
Okay, perfect.

00:50:04 - Brandon Hancock
So yeah, so sequential agents, this is task ABC.

00:50:08 - Brandon Hancock
Loop agent is continually attempt to do the same thing until you get a result.

00:50:14 - Brandon Hancock
So this is what Abdul, we were working about earlier for him, which is like continually research until you get an answer.

00:50:21 - Brandon Hancock
And then parallel agents is like go off and do work at the same time.

00:50:25 - Brandon Hancock
Now, to further answer your question, you were saying like, hey, how do I pick which workflow to go down?

00:50:35 - Brandon Hancock
I think this one might do it.

00:50:40 - Brandon Hancock
Yeah.

00:50:41 - Brandon Hancock
So what you could do is you basically inside of ADK is you create a root agent and then under a root agent, you can give it multiple types of agents.

00:50:53 - Brandon Hancock
So you could give a root agent, which is like, hey, your job is to always delegate tasks to everyone else.

00:50:58 - Brandon Hancock
And if it's a sequential task.

00:51:00 - Brandon Hancock
You could pass in a sequential agent to where it always does step one, then step two, or you could give it to another sub agent group, which is a loop agent.

00:51:11 - Brandon Hancock
So I've really liked the dynamic ability of it.

00:51:15 - Brandon Hancock
So it's not like in real time figuring out if it's going, you know, sequential or loop.

00:51:21 - Brandon Hancock
It's just you kind of have some predetermined workflows that you get to set up.

00:51:25 - Brandon Hancock
And you have one master root agent who's passing to some sequential ones, to some loop ones.

00:51:31 - Brandon Hancock
Sometimes it'll do A, then B.

00:51:33 - Brandon Hancock
So super powerful.

00:51:35 - Brandon Hancock
Crew right now is always, right now crew is always sequential.

00:51:43 - Brandon Hancock
Unless you go to a flow, then you can get crazy.

00:51:46 - Brandon Hancock
But I liked how easy it was just to say sequential agent, loop agent, parallel agent.

00:51:51 - Brandon Hancock
I thought it was a pretty nice trick that ADK did.

00:51:55 - Sagar Passi
For of these determined workflows, do I need to define the agent's force?

00:52:00 - Sagar Passi
These workflows, can I pick them dynamically depending on the goal?

00:52:05 - Brandon Hancock
So what's nice is you can pass in, let me just show you something really quick too.

00:52:10 - Brandon Hancock
All right, I'm going to go back.

00:52:11 - Brandon Hancock
So depending on the goal, it's like, let's go look at a post reviewer agent.

00:52:19 - Brandon Hancock
So like, obviously the goal of this agent is to write LinkedIn posts, but like kind of how like you can do with Crew AI and some other agent frameworks is like, you can just pass in variables, so you can kind of change the goal or what it needs to do by passing a different information.

00:52:38 - Brandon Hancock
So, you know, like sometimes, yeah.

00:52:40 - Brandon Hancock
Is this what you're talking about or am I off subject?

00:52:44 - Sagar Passi
More like, let's say I'm in operations in a bank and then I say I need to find quarter-end reporting.

00:52:55 - Sagar Passi
My expectation would be that it would go to, you know, the finance agent, that agent.

00:53:00 - Sagar Passi
If would talk to the data agent to pull it from SharePoint, for example, that would run its task in the background.

00:53:05 - Sagar Passi
Then if I say, I don't know, make this record or download this document or something like that, that's another agent that's fetching it.

00:53:17 - Sagar Passi
And it's figuring out what the path is like a human would.

00:53:20 - Sagar Passi
That's my expectation from an agentic team.

00:53:22 - Brandon Hancock
So that's exactly what Agent Development Kit does.

00:53:26 - Brandon Hancock
So like every agent comes with its own description and, I mean, I'll just share it really quickly.

00:53:33 - Sagar Passi
And then just as people want to do this, what would you recommend for connecting to these services like SharePoint?

00:53:40 - Sagar Passi
Is MCP the right way to go?

00:53:43 - Sagar Passi
Is that the standard that you would recommend?

00:53:46 - Brandon Hancock
Okay, so, all right, so I'm going to give a few takes on this.

00:53:52 - Brandon Hancock
The simple answer with just getting this up and running, the answer is no.

00:53:57 - Brandon Hancock
Like to get it working, to start, no.

00:53:59 - Brandon Hancock
Just doing a.

00:54:00 - Brandon Hancock
Direct Tool Call is the easiest way to go.

00:54:03 - Brandon Hancock
However, once you build up a few different, once you build up a few different, like, agentic teams, so, like, let's say you have one marketing department agent, within that, there's literally 30 agents, okay?

00:54:19 - Brandon Hancock
Well, they can, that's all in one repository, so you're sharing all the codes, all the tools, super easy.

00:54:25 - Brandon Hancock
Now, let's say you go over to the finance department, and you make them 30 other agents.

00:54:30 - Brandon Hancock
Well, now, there's probably a lot of shared tools that you want to use between the marketing agents and the finance agents, and that is at the point where sharing becomes nice.

00:54:41 - Brandon Hancock
But for V1, dude, it's all in one repository, just keep it there.

00:54:46 - Brandon Hancock
It's the second you get to two separate repositories where you need to share code, that's where you probably want to start looking at MCP.

00:54:56 - Brandon Hancock
Okay, I want to show you this really quick, just because I think it's, well,

00:55:00 - Brandon Hancock
I actually won't go to it because it's too detailed right now.

00:55:03 - Brandon Hancock
But under the hood, agent development kit, every time it gets a call, it looks at all sub-agents that it has access to, and it goes, who would be the best to fill this job?

00:55:14 - Brandon Hancock
So it feels very much like a manager.

00:55:17 - Brandon Hancock
So it always looks to see who's the best one to do this job and delegates it to them.

00:55:23 - Brandon Hancock
So all that delegation, yeah, it just does it under the hood.

00:55:27 - Brandon Hancock
So that's what I would look at.

00:55:28 - Sagar Passi
So the recommendation is agent development kit, not crew AI enterprise.

00:55:36 - Brandon Hancock
I mean, I'd have to learn a little bit more about the customer and their needs.

00:55:41 - Brandon Hancock
I mean, I'm happy to follow up on a separate call if you want to late this week to maybe give some more answers.

00:55:47 - Brandon Hancock
But you could go either way.

00:55:50 - Brandon Hancock
I would just need to know a little bit more about their use cases to be like, if that's a requirement, if they gave you a requirement, I could just go and tell you, yeah, this tool will not work or yes, this.

00:56:00 - Brandon Hancock
This tool will work.

00:56:02 - Brandon Hancock
So it just depends what they're trying to do.

00:56:05 - Brandon Hancock
Okay, a few questions that popped up really fast.

00:56:08 - Brandon Hancock
Sebastian asks, is their chat feature part of open source ADK, or is it a feature of their cloud?

00:56:15 - Brandon Hancock
So they actually have like a nice little quick start, Sebastian, where in their quick start guide, they just show you how to also easily deploy a nice front end in front of ADK.

00:56:24 - Brandon Hancock
So you could get something pretty similar.

00:56:27 - Bastian Venegas
My question was basically if you can modify the chat if you want it, or is it just?

00:56:33 - Brandon Hancock
No, yeah, it is, I'll just show you really quickly.

00:56:38 - Brandon Hancock
I have read these documents so many times, guys.

00:56:42 - Brandon Hancock
I could start to recite certain things in my sleep, which, hey, I guess that's a good thing to have.

00:56:51 - Brandon Hancock
Okay, share, share.

00:56:53 - Brandon Hancock
Okay.

00:56:55 - Brandon Hancock
All right, get started, quick start, then within quick, sorry, this is the...

00:57:00 - Bastian Venegas
The tutorial.

00:57:03 - Brandon Hancock
Yeah, I think it's the tutorial one.

00:57:06 - Brandon Hancock
Start learning.

00:57:07 - Brandon Hancock
They actually just changed the docs.

00:57:09 - Brandon Hancock
They dropped a new version this week.

00:57:13 - Brandon Hancock
But I believe it is here where they do a fast API.

00:57:18 - Brandon Hancock
Okay, no, I know we're dead.

00:57:22 - Brandon Hancock
Yeah, so you can see here, Bastian, I'll drop this chat or this link in the chat.

00:57:27 - Brandon Hancock
But long story short, you can see they actually build a UI in front of their agents that allows you to, like, turn ADK into a – to turn your agents into an API, which is basically what you want.

00:57:42 - Bastian Venegas
So you can see they have agents.

00:57:44 - Brandon Hancock
They create a session.

00:57:45 - Brandon Hancock
Once you have a runner, all you need to do now is start making requests to that runner.

00:57:50 - Brandon Hancock
And then once you get – then you'll get back answers that you can start showing to your user.

00:57:55 - Brandon Hancock
So I'm going to drop this – oops, sorry.

00:57:57 - Brandon Hancock
I'm going to drop this in the the chat.

00:58:00 - Bastian Venegas
Yeah, that's a major difference compared to Krupp.

00:58:04 - Bastian Venegas
I agree.

00:58:05 - Brandon Hancock
I start holding the first API right away.

00:58:08 - Brandon Hancock
Yeah, I will say I'm really loving ADK for how quickly it is to put it inside of another, like a front end.

00:58:17 - Brandon Hancock
Because with Krupp.ai, it is your job to then create wrappers around everything.

00:58:23 - Brandon Hancock
And, yeah, so that's, I don't like, you're forced to do enterprise, basically, for certain things, which is fine if you're going to go down that route.

00:58:32 - Brandon Hancock
But if you're not, and you just want to test rapidly, ADK is really nice for rapid iteration.

00:58:37 - Brandon Hancock
So, okay.

00:58:38 - Brandon Hancock
Any final things, Sagar, before we're on?

00:58:42 - Sagar Passi
I know that's been helpful.

00:58:43 - Brandon Hancock
Thank you.

00:58:44 - Brandon Hancock
All right, perfect.

00:58:45 - Brandon Hancock
All right, well, keep us posted.

00:58:46 - Brandon Hancock
It sounds like you got a lot of cool opportunities coming up.

00:58:48 - Brandon Hancock
So, yeah, please keep us in the loop.

00:58:50 - Brandon Hancock
This is very exciting.

00:58:52 - Brandon Hancock
I will do.

00:58:53 - Sagar Passi
Also, I'm going to an AWS event tomorrow.

00:58:56 - Sagar Passi
So, if anyone has any questions for me to ask, I'm happy to feed back to this group.

00:59:00 - Sagar Passi
Just message me.

00:59:02 - Sagar Passi
Okay, awesome.

00:59:03 - Brandon Hancock
Dude, please record.

00:59:04 - Brandon Hancock
That'll be a ton of fun.

00:59:05 - Brandon Hancock
All right.

00:59:07 - Brandon Hancock
Up next in the screenshots, let's see.

00:59:12 - Brandon Hancock
Fernando, it looked like you were up next.

00:59:15 - Brandon Hancock
I think Ty dropped out.

00:59:18 - Brandon Hancock
If you want to hop on.

00:59:21 - Brandon Hancock
I can't remember if he left or not.

00:59:23 - Brandon Hancock
If not, Richard, you're up.

00:59:28 - Brandon Hancock
What's going on?

00:59:31 - Richard Collier
Hey, how's it going today, man?

00:59:33 - Richard Collier
Just a couple of calls.

00:59:34 - Richard Collier
Like I said, I had some personal issues, but I was working on a few things.

00:59:43 - Richard Collier
And do you mind if I share my screen really quick?

00:59:46 - Brandon Hancock
Of course.

00:59:46 - Brandon Hancock
I'm going to share here.

00:59:52 - Richard Collier
Can you see my screen?

00:59:55 - Brandon Hancock
I see someone drinking a smoothie.

00:59:58 - Richard Collier
Yes.

01:00:00 - Richard Collier
So I've been kind of working on the B-roll agent for running like little Facebook ads and stuff like that.

01:00:07 - Richard Collier
And so I have it create like these really like crazy scripts and then I started using cartoons because it was a lot easier for Flux to draw them and then it didn't have to be so realistic.

01:00:22 - Richard Collier
So I started using cartoons and I do have to do some post-editing, but I get a pretty good video right off the bat.

01:00:34 - Richard Collier
So I'll just play a little bit of this.

01:00:35 - Richard Collier
I don't know if you guys will be able to hear it.

01:00:42 - Brandon Hancock
I'm tired breakfast shakes that taste like lawn clippings and disappointment?

01:00:47 - Richard Collier
Yeah, me too.

01:00:48 - Richard Collier
Check out Vast Thread Superfood, basically your morning smoothies badass older sibling who rides a motorcycle and actually gets results.

01:00:57 - Richard Collier
It's packed with more antioxidants than your mom's pin

01:01:00 - Richard Collier
Mattress Board has DIY recipes.

01:01:02 - Richard Collier
Strawberry.

01:01:05 - Richard Collier
That is awesome, dude.

01:01:08 - Richard Collier
Yeah.

01:01:08 - Richard Collier
That's so cool.

01:01:11 - Richard Collier
Yeah, so, you know, it's pretty good.

01:01:15 - Richard Collier
Obviously, the tools are getting a lot better, so that's helping out a lot.

01:01:20 - Richard Collier
But, yeah, I can pretty much get an ad up and running really quickly, have a really decent script.

01:01:28 - Richard Collier
I do need to go in and kind of tweak the script to make it, you know, a lot better sometimes.

01:01:33 - Richard Collier
But, I mean, for the most part, I'm about getting something 60% done, and then I take it in the post and make it a little bit better.

01:01:42 - Richard Collier
And, of course, I'll add transitions.

01:01:43 - Richard Collier
I'll add, you know, sound effects and things of that nature to really polish this up into something usable for a Facebook ad.

01:01:51 - Richard Collier
But that is what I've been working on, on one project.

01:01:57 - Richard Collier
And this other project has been a.

01:02:00 - Richard Collier
A project I've been working on where I'm taking audiobooks or words and then turning them into audiobooks where you get a different voice for each character.

01:02:12 - Richard Collier
It's using like a schema, and I'm also using OpenAI's new text speech model, and it's actually pretty good and not as many voices as Eleven Labs, but still pretty good.

01:02:25 - Richard Collier
But I'll play a little bit of this.

01:02:27 - Richard Collier
This is just a clip.

01:02:28 - Richard Collier
Buildings loom like skeletons, half-collapsed and covered in rust.

01:02:32 - Richard Collier
Cold wind howls through broken windows.

01:02:35 - Richard Collier
A groan echoes down the alley as a battered loudspeaker crackles to life.

01:02:39 - Richard Collier
Susten and Stratton commencing.

01:02:41 - Richard Collier
Sector 9C, line up.

01:02:43 - Richard Collier
One per household.

01:02:45 - Richard Collier
Tampering is punishable by purging.

01:02:48 - Richard Collier
Dozens of unwanted, line up.

01:02:50 - Richard Collier
So, it will switch voices.

01:02:54 - Richard Collier
It will read the script all in different voices, and it will also pass different instructions.

01:02:59 - Richard Collier
So the voice...

01:03:00 - Richard Collier
The are slightly different because there's not a lot of voices.

01:03:04 - Richard Collier
So I'm able to say, hey, this person talks with like a higher, you know, pitch, or this person talks lower, or they have like a southern accent or something like that.

01:03:14 - Richard Collier
And I'm able to pass in all of these parameters.

01:03:16 - Richard Collier
And it's pretty cheap to like do this.

01:03:20 - Richard Collier
It's only like maybe like a dollar to get it to do this.

01:03:23 - Richard Collier
This is an act one of an entire series.

01:03:26 - Richard Collier
And it's an hour and 34 minutes, as you can see.

01:03:29 - Richard Collier
And, you know, it just goes in there and does it.

01:03:32 - Richard Collier
And I have script parsers in here.

01:03:37 - Richard Collier
I have the audio stitching for FFmpeg, where it's going to label all the voices in order.

01:03:44 - Richard Collier
It's going to put it all together into one thing.

01:03:48 - Richard Collier
So, mean, it's an interesting, you know, use case.

01:03:50 - Richard Collier
And it's pretty good so far.

01:03:53 - Richard Collier
it's still working.

01:03:55 - Brandon Hancock
Dude, you're underselling this.

01:03:57 - Brandon Hancock
This is freaking awesome.

01:03:59 - Brandon Hancock
I know you've been putting in the work.

01:04:00 - Brandon Hancock
Work on this, and it is amazing.

01:04:03 - Brandon Hancock
So I have a few nerdy questions for you.

01:04:06 - Brandon Hancock
Sure.

01:04:08 - Brandon Hancock
So Jake, sorry, you had your hand up first if you want to go.

01:04:10 - Jake Maymar
Oh, I was just, I mean, yeah, this is amazing.

01:04:14 - Jake Maymar
I was curious, can you do emotions?

01:04:17 - Richard Collier
Yeah, so with the OpenAI, it doesn't, I mean, it won't always follow it, but what I, there is an instructions parameter that you can pass in.

01:04:29 - Richard Collier
And we kind of go, you know, with grief or, you know, very excited or something like that.

01:04:35 - Richard Collier
And so it will try and match those emotions.

01:04:38 - Richard Collier
But yes, to answer your question, yeah, there is emotion there as well.

01:04:43 - Jake Maymar
Yeah, this is amazing.

01:04:44 - Jake Maymar
This is totally amazing.

01:04:46 - Brandon Hancock
So I'm going to go video first.

01:04:49 - Brandon Hancock
So, okay, so a few questions.

01:04:51 - Brandon Hancock
So for images, what was your, what did you end up picking as your go-to image generating tool?

01:04:59 - Brandon Hancock
I can use influence.

01:05:00 - Richard Collier
Flux.

01:05:00 - Richard Collier
I'm using Flux.

01:05:02 - Brandon Hancock
Okay.

01:05:03 - Brandon Hancock
And then when it comes to price, I mean, it's pretty affordable, right, from my understanding?

01:05:08 - Richard Collier
It's very affordable.

01:05:09 - Richard Collier
Yeah.

01:05:11 - Brandon Hancock
And then for audio on the other one, is it also OpenAI or is it 11 labs for the other one?

01:05:19 - Richard Collier
I'm using 11 labs and I'm using a custom voice with like crazy low stability on there so that it's so animated.

01:05:27 - Richard Collier
So it's like, hey, are you tired of doing it?

01:05:28 - Richard Collier
You know what mean?

01:05:29 - Richard Collier
It's very animated.

01:05:31 - Richard Collier
I love it.

01:05:31 - Richard Collier
Yeah, it's a custom voice that over-pronounces words and makes everything just, you know, kind of weird, but it's there to just grab attention.

01:05:40 - Richard Collier
So it's a custom voice with very low stability as the setting.

01:05:44 - Brandon Hancock
Dude, great pattern interrupt.

01:05:46 - Brandon Hancock
Great pattern interrupt.

01:05:47 - Brandon Hancock
And then would you mind hopping back screens?

01:05:50 - Brandon Hancock
Because I wanted to point out two things.

01:05:53 - Richard Collier
On the video?

01:05:55 - Richard Collier
Yeah.

01:05:56 - Richard Collier
Okay.

01:05:56 - Brandon Hancock
The video, yeah.

01:05:59 - Brandon Hancock
Okay.

01:06:00 - Brandon Hancock
So on.

01:07:00 - Richard Collier
Based on whether or not if I need to change the way something is being said or if the image sucks or, you know, whatever, I'll just cut it out and then, you know, put it back in.

01:07:09 - Brandon Hancock
Okay.

01:07:10 - Brandon Hancock
All around, I mean, it's absolutely beautiful.

01:07:12 - Brandon Hancock
So that's why I was just curious, like, how much manual work was done.

01:07:16 - Brandon Hancock
But the fact that it does all that is wild.

01:07:18 - Richard Collier
Yeah, Yeah, about 60% done.

01:07:21 - Richard Collier
And, you know, I mean, like, if I was to leave it like this, I mean, it would be okay.

01:07:25 - Richard Collier
But by me adding, you know, the, I had to add the score track, which is the music track.

01:07:31 - Richard Collier
So that doesn't come from the coder at all.

01:07:34 - Richard Collier
So I have to find that, put that in there.

01:07:37 - Richard Collier
And then I'll be adding sound effects and transitions, which, you know, take some time manually.

01:07:44 - Richard Collier
But as far as like, not needing to look for all these images and kind of figure out what I'm going to write, the writing is done for me.

01:07:52 - Richard Collier
The voice is done for me.

01:07:54 - Richard Collier
All the images is done for me.

01:07:56 - Richard Collier
The video creations are done for me.

01:07:59 - Richard Collier
I do need to, you know, pack.

01:08:00 - Richard Collier
Catch in different pieces of video where I didn't like it or something like that.

01:08:04 - Richard Collier
But other than that, everything is kind of done for me until I really go in and start fine-tuning it to make it, you know, a better ad.

01:08:13 - Richard Collier
So about 60% done.

01:08:16 - Brandon Hancock
That's awesome.

01:08:16 - Brandon Hancock
Few ideas for just to help, like, get this as close to 99%, 100% as possible.

01:08:22 - Brandon Hancock
So, okay, so for sound effects.

01:08:24 - Brandon Hancock
So in my mind, I'm like, what is a sound effect?

01:08:27 - Brandon Hancock
It is something's happening on the screen at a specific time that we need to add in, you know, some, like a whoosh, a something, you know?

01:08:35 - Brandon Hancock
So what would be pretty cool is in Gemini, what you can do is you can upload pretty big videos now.

01:08:43 - Brandon Hancock
And you could potentially, if there's, like, 20, 30, 100 different sound effects that you have, like, in a library, what you could do is say, hey, please watch this video.

01:08:52 - Brandon Hancock
And what I would like for you to do is spit out a bulleted list, a time series bulleted list of when I should include different.

01:09:00 - Brandon Hancock
Different sound effects, you know, so like that way, it's just once again, just easy copy paste of like when you need to add what where could potentially save some time to try that Gemini Gemini is what you need to do for that one.

01:09:15 - Brandon Hancock
I think it's a what's the what's the link?

01:09:20 - Brandon Hancock
And Bastian had some suggestions for you, too.

01:09:23 - Richard Collier
Okay, yeah, that's really awesome.

01:09:25 - Richard Collier
Is it the studio Gemini or is it the from the website where there where there are other models reside?

01:09:35 - Richard Collier
Or is it the 2.5?

01:09:37 - Brandon Hancock
I know I would go to AISTudio.Google.com.

01:09:41 - Richard Collier
Okay.

01:09:42 - Brandon Hancock
That's that's what I would look at doing just strictly because you could do structured output.

01:09:48 - Brandon Hancock
And I think that's something you'll need to where you just like you could just say, like, I want an array of array of time audio clip.

01:09:58 - Brandon Hancock
Like you could you could define that as the structure.

01:10:00 - Brandon Hancock
And there's quite a few other things that you could do in there.

01:10:05 - Richard Collier
Okay, sounds good because Eleven Labs creates sound effects as well.

01:10:11 - Richard Collier
So I thought about seeing if they were in the API and if they would be able to handle, you know, putting in sound effects where they made sense.

01:10:18 - Richard Collier
But I'm like, I don't know if it's going to, you know, do it.

01:10:21 - Richard Collier
But I mean, I'm definitely going to try the Gemini and see about that and then kind of go from there.

01:10:27 - Richard Collier
So, yeah, that's really good.

01:10:29 - Richard Collier
Thank you.

01:10:30 - Brandon Hancock
All right, final question I have before finishing nerding up.

01:10:33 - Brandon Hancock
So, dude, end goal.

01:10:34 - Brandon Hancock
You become the master expert of all things video and audio clips for AI.

01:10:41 - Brandon Hancock
What are we doing, man?

01:10:42 - Brandon Hancock
This is such a cool skill that, like, 0.00001% of the world has.

01:10:48 - Brandon Hancock
How are we going to capitalize on this?

01:10:50 - Brandon Hancock
What are we thinking?

01:10:52 - Richard Collier
So right now I'm actually writing a short story.

01:10:56 - Richard Collier
Um, and I was going to do a whole video and, uh...

01:11:00 - Richard Collier
Here

01:11:00 - Richard Collier
And kind of use this to bring out the search story and just kind of, you know, perhaps just start like a YouTube channel of just short stories that people can watch either while they drive or, you know, when they're home doing nothing or, you know, whatever.

01:11:15 - Richard Collier
And there'll be like maybe, you know, 10, 15 scenes.

01:11:20 - Richard Collier
And I was thinking about, you know, maybe generating, you know, audio and video and music tracks to kind of go with it and then kind of go from there.

01:11:29 - Richard Collier
And then, you know, if it's, if it seems like it's, you know, can handle stuff like that, then maybe I'll do something like what Paul did.

01:11:35 - Richard Collier
By the way, good job, buddy.

01:11:37 - Richard Collier
That was a really nice website you did with Lovable.

01:11:40 - Richard Collier
I'm, you know, maybe I'll, maybe I'll do like some kind of sass or something like that.

01:11:45 - Richard Collier
Because I think the only other like people in the game right now for this is in video and they are crazy expensive.

01:11:54 - Brandon Hancock
Mm-hmm.

01:11:55 - Brandon Hancock
Yeah.

01:11:56 - Brandon Hancock
No, it is, it is wild how much they charge.

01:11:59 - Brandon Hancock
I, um, I.

01:12:00 - Brandon Hancock
I, real quick, if you do a YouTube style, I just dropped a channel that I think you might like for inspiration, um, and I'm trying to find one other, there's like AI YouTube guy, I cannot remember his name, if I see it, I'd recognize it, um, I will find it, I will send it to you, but he, uh, he, he basically was teaching people how to make, like, full-blown YouTube videos, but if yours is, yeah, it's literally just AI guy, okay, that's even easier, um, but the two, the two channels I just dropped, like, one is about him doing, um, faceless YouTube videos all in, with AI, and this, uh, and the other one is just like a bunch of random tutorials on everything for, uh, related to, basically, image and video, but it's not as much, uh, it's not as much, um, it's not as focused, it's just, here's every tutorial ever that you could think of, so, you know, if you're

01:13:00 - Brandon Hancock
What's more on marketing material, that's a very specialized, focused niche that would crush it.

01:13:07 - Brandon Hancock
Because I don't know if really quick – where's this guy's thing?

01:13:12 - Brandon Hancock
I just want to show you numbers because this is crazy.

01:13:15 - Brandon Hancock
So the AI guy, his school community – oh, where's it at?

01:13:21 - Brandon Hancock
He makes so much money.

01:13:22 - Richard Collier
Thank you, Bastian.

01:13:24 - Richard Collier
This is a very detailed comment that you have down here.

01:13:28 - Richard Collier
I'm copying and pasting it now to definitely look into this with the metadata.

01:13:33 - Bastian Venegas
Thanks, Bastian.

01:13:34 - Bastian Venegas
I appreciate it.

01:13:36 - Bastian Venegas
You're welcome.

01:13:38 - Brandon Hancock
I'm pulling up for you real fast, Richard.

01:13:42 - Brandon Hancock
I think it's the AI guy?

01:13:44 - Brandon Hancock
Yeah.

01:13:44 - Brandon Hancock
So he currently has 600 people in his community, 75 bucks a month.

01:13:49 - Brandon Hancock
So like, you know, what is that, 4,500 a month?

01:13:54 - Brandon Hancock
Wild.

01:13:54 - Brandon Hancock
Yeah, 45K, sorry.

01:13:55 - Brandon Hancock
Not 100, 45K a month.

01:13:57 - Brandon Hancock
So absolutely stupid.

01:13:59 - Brandon Hancock
So that's second channel.

01:14:00 - Brandon Hancock
I would 10 out of 10 recommend looking at his as well because it's very, like, it's, he's all about making money with faceless YouTube channels, but yours would be, you know, more, more product driven and more people have more money because it's a business buying it rather than like an individual.

01:14:14 - Brandon Hancock
So absolutely love it.

01:14:16 - Brandon Hancock
All right.

01:14:17 - Brandon Hancock
Yeah, we'll keep cruising, but that was, dude, still on the show, man.

01:14:21 - Brandon Hancock
Absolutely amazing.

01:14:23 - Brandon Hancock
Jake, if you want to go real quick.

01:14:25 - Jake Maymar
Yeah, yeah.

01:14:27 - Jake Maymar
Would it make sense to add like a reinforcement learning?

01:14:30 - Jake Maymar
Luke, since your, your, you understand what the end video should be, and you said it does 60%, but then you do a lot of manual work.

01:14:39 - Jake Maymar
Would it make sense to record the manual work you do basically build the Python or some other tool, uh, to sort of record that manual work?

01:14:48 - Jake Maymar
And that way, at least you're training the system with the right data.

01:14:53 - Richard Collier
And then I've been asking about it.

01:14:56 - Richard Collier
Um, I've been and talking with, uh, GPT about it.

01:15:00 - Richard Collier
And it says that it's absolutely possible, but of course, like, you know, we say, like, it will absolutely tell you you can do anything, you know what mean?

01:15:08 - Brandon Hancock
And then you start doing it, and it's like, oh, well, why did you think that, you know?

01:15:13 - Richard Collier
But yeah, no, I have definitely been talking about it with, like, Super Bass and, like, trying to get something where I'm giving it, like, a thumbs-up, thumbs-down type system and also telling it what's wrong and things of that nature.

01:15:25 - Richard Collier
And it does say that it is possible.

01:15:28 - Richard Collier
From what it is telling me on how I would go about doing it, it sounds plausible.

01:15:33 - Richard Collier
I just need more time in the day in order to do something like that.

01:15:38 - Richard Collier
But yeah, for sure, absolutely, and a great suggestion.

01:15:40 - Richard Collier
I am looking into that, and I will try and, you know, hasten that process to be able to get it to do a little bit more and a little less garbage, you know?

01:15:50 - Richard Collier
But there's a lot of moving parts that I don't control.

01:15:52 - Richard Collier
Like, I can't, you know, control what I get back from Flux if it decides to generate garbage.

01:16:00 - Richard Collier
You know, it's just going to do that whenever it feels like it.

01:16:02 - Richard Collier
And, you know, same thing with any of the video rendering softwares.

01:16:07 - Richard Collier
It will just render garbage anytime it feels like it.

01:16:10 - Richard Collier
So that is always going to – that is part of that why it's not, you know, a higher percentage because I will need to go in and out and take, you know, things out that I don't 100% control and never will, you know what I mean?

01:16:25 - Richard Collier
So – but, yeah, great suggestion for sure.

01:16:27 - Jake Maymar
I found – because I was – so I built those into all my systems.

01:16:32 - Jake Maymar
I found the fastest way to do it is a thumbs down, thumbs up, and you just do the thumbs – so when you get the image you don't like, you just thumbs down it and it just stores it.

01:16:43 - Jake Maymar
That's it.

01:16:43 - Jake Maymar
And you can put, like, a couple of descriptions of what you didn't – what didn't work about it.

01:16:48 - Jake Maymar
And then the other thing is when you get a clip that works, then that becomes basically a few shot, right?

01:16:57 - Jake Maymar
So that becomes the prompt that you're going to use.

01:16:59 - Jake Maymar
is maybe –

01:17:00 - Jake Maymar
For a VLM instead of a large language model.

01:17:03 - Jake Maymar
But the thing is, is if you just do a simple thumbs down, thumbs up, that might get you closer to where you want to be without having to do all this insane, complicated systems.

01:17:21 - Jake Maymar
All right.

01:17:22 - Brandon Hancock
Awesome.

01:17:23 - Brandon Hancock
Yeah, that's literally amazing.

01:17:25 - Brandon Hancock
Seriously, that was awesome.

01:17:27 - Brandon Hancock
I'm excited to see where this keeps going, too.

01:17:29 - Brandon Hancock
All right.

01:17:30 - Brandon Hancock
Next up, Andrew, what's going on?

01:17:34 - Andrew Nanton
Oh, hey, everyone.

01:17:36 - Andrew Nanton
So I sent you a quick note.

01:17:37 - Andrew Nanton
I don't really have any updates.

01:17:39 - Andrew Nanton
I've just been doing day job.

01:17:42 - Andrew Nanton
Had an interesting trial I testified in, but that has been what I've been up to.

01:17:47 - Andrew Nanton
So I'm mostly just here to listen and think about happier things than my day job provides.

01:17:52 - Andrew Nanton
So thanks for letting me sit in.

01:17:54 - Brandon Hancock
Yeah, of course.

01:17:55 - Brandon Hancock
Oh, of course.

01:17:58 - Brandon Hancock
Any fun?

01:17:59 - Brandon Hancock
Well, I will ask any fun things.

01:18:00 - Brandon Hancock
Things coming up then on the horizon?

01:18:03 - Andrew Nanton
You know, we're just still turning the wheel.

01:18:05 - Andrew Nanton
Maxim and I are getting ready to open up for testing on this thing that we're working on, you know, this product for expert witnesses.

01:18:15 - Andrew Nanton
And, you know, what I think is a little bit different about this is that we're, in order to ask busy professionals to test stuff, it really has to be pretty much ready for them to spend time on it.

01:18:26 - Andrew Nanton
And it's just a different scenario.

01:18:29 - Andrew Nanton
So, mean, hopefully this is not a lot of time and energy misspent, but it's looking good.

01:18:36 - Andrew Nanton
So I'm hoping, and once we are, you know, ready for testing and have something to show, I'm excited to show it to you all.

01:18:44 - Andrew Nanton
But, yeah, I mean, all the parts and pieces are there.

01:18:47 - Andrew Nanton
It's a bit like a, you know, bag of Legos at this point.

01:18:50 - Andrew Nanton
mean, they're snapping together slowly but surely, but there's not much to see.

01:18:55 - Brandon Hancock
Yeah, and then real quick, so I just have like, you know, questions when it comes to.

01:19:00 - Brandon Hancock
Like testing.

01:19:00 - Brandon Hancock
So is it just your network is now the who you're just reaching out to, like friends?

01:19:05 - Brandon Hancock
Or is this more cold outreach and just like, hey, we're building this cool thing.

01:19:09 - Brandon Hancock
I see you're, you know, in the same space.

01:19:12 - Brandon Hancock
Or what are we doing?

01:19:13 - Andrew Nanton
Yeah, yeah.

01:19:14 - Andrew Nanton
At this point, it is people that I know, you know, so I'm starting with a pretty small pool of people that I, one, can count on to have sufficient tech savvy that they're not going to freak out if they had a 404.

01:19:30 - Andrew Nanton
Um, and, uh, then, um, and, and maybe are tech savvy enough to use something like Loom or, you know, some equivalent, like, Hey, if you're getting something weird, can you just show me what it is?

01:19:42 - Andrew Nanton
And we'll, we'll try to iron it out.

01:19:43 - Andrew Nanton
And the number of people who do that and are forensic psychiatrists is a, it's a, I can count them on one hand.

01:19:49 - Andrew Nanton
So, um, yeah, that's where we're starting.

01:19:52 - Andrew Nanton
And then, um, but I'm hoping that that will just be, you know, maybe a couple of weeks of testing and then we can roll it out to more like.

01:20:00 - Brandon Hancock
that's that's

01:20:00 - Andrew Nanton
10 or 15 people who are a little bit more mixed, probably with a fair amount of hand-holding about, and training about, here's how you use this thing, and then we should be good to go.

01:20:11 - Brandon Hancock
Awesome.

01:20:11 - Brandon Hancock
Yeah, please, I mean, awesome.

01:20:13 - Brandon Hancock
the rollout, I will, so a just, like, quick ideas, feedback, or for things to help.

01:20:20 - Brandon Hancock
I'm not sure what onboarding looks like for the product, but just a heads up, like, the more for those first initial users that you can, like, auto-preload, even if it's a manual, like, hey, we seeded your entire thing for you, just, so you just click in, you know, just for those first initial users to make it as, like, easy as possible.

01:20:42 - Brandon Hancock
That's something I've seen done to make it easier, especially in, like, more high-friction testing, you know.

01:20:49 - Brandon Hancock
You don't want them to be ranking the onboarding experience, you want them to be rating the core loop, if that makes sense.

01:20:55 - Brandon Hancock
So, you know, onboarding is once we're scaling.

01:20:59 - Brandon Hancock
Let's get the core.

01:21:00 - Brandon Hancock
Fourth thing, work at first, you know?

01:21:02 - Brandon Hancock
So, yeah, that's just a quick idea I had as well.

01:21:06 - Brandon Hancock
Yeah, thank you.

01:21:07 - Andrew Nanton
And just real quick to respond to Bastian's idea about, you know, me recording some stuff, you know, how to do things that I can send to people.

01:21:15 - Andrew Nanton
I think that's a great idea.

01:21:17 - Andrew Nanton
And actually, I'm trying to remember what podcast I was listening to the other day, but there was a woman who was saying she does, she builds automations in N8N for people.

01:21:26 - Andrew Nanton
And she was saying she has a script set up where she records the workflow of what every step of the N8N workflow does in, and she records that in something like Loom, sends that audio and video of her describing and the images, and has that basically transcribed into a series of screenshots and descriptions of, oh, here's what all the different parameters do, know, here's what all the settings are for, both for her and for the class.

01:22:00 - Andrew Nanton
Client she's creating it for, you know, just so for her own reference later, but also, and I thought that was a pretty brilliant idea, you know, just record you talking through it once, and then you have not only a video, but if you prompt it right, you could have a written documentation as well, or at least an 80% start on it.

01:22:20 - Bastian Venegas
Yeah, in fact, today I used the feedback that Brandon sent me for a script of a video, and this is my script, this is my feedback, it works really great.

01:22:31 - Brandon Hancock
Loom is such a cheat code, especially Loom AI features.

01:22:35 - Brandon Hancock
I don't know how I would do life without Loom.

01:22:39 - Brandon Hancock
It would take 10 times as long to do everything.

01:22:41 - Brandon Hancock
So, that's funny that you did that.

01:22:45 - Andrew Nanton
Always working smarter.

01:22:46 - Andrew Nanton
If I can ask one quick follow-up question on that.

01:22:49 - Andrew Nanton
So, some of the people, some of the data that I'm hoping people will be working with when they start working with real data will be protected information.

01:22:57 - Andrew Nanton
And I saw that Loom has an option.

01:23:00 - Andrew Nanton
And

01:23:00 - Andrew Nanton
Where you can blur out, but it only works with the Chrome plugin, and you can only basically blur out like CSS elements.

01:23:06 - Andrew Nanton
Like you can't just select, blur out this portion of my capture.

01:23:11 - Andrew Nanton
Does anyone know of a tool that will just let you sort of drag and select, say, you know, block out these areas?

01:23:20 - Andrew Nanton
So if people are dealing with sensitive data, they can show me the behavior, but not necessarily show me their data.

01:23:27 - Brandon Hancock
So the only thing I could think of, just a quick suggestion, is if they are on a Mac, they're Screen Studio.

01:23:35 - Brandon Hancock
So you can record your screen.

01:23:37 - Brandon Hancock
It feels kind of like Loom.

01:23:39 - Brandon Hancock
And you can go back, I believe, and just add in blocks.

01:23:43 - Brandon Hancock
So like they could just like physically add a block over it.

01:23:49 - Brandon Hancock
It's manual.

01:23:49 - Brandon Hancock
They're the ones having to do it.

01:23:51 - Brandon Hancock
But, you know, the good thing about Screen Studio is it's all local on your computer until you export the final MP3.

01:23:58 - Brandon Hancock
So because like with Loom, it's instant.

01:24:00 - Brandon Hancock
It's instant download, upload, which is, I think, not what they want.

01:24:04 - Andrew Nanton
It's good, but not what I need.

01:24:06 - Brandon Hancock
Yeah, saying you're doing sensitive stuff, yeah.

01:24:08 - Brandon Hancock
I can peek really fast, too, in Screen Studio, just to make sure I'm not lying to you.

01:24:15 - Brandon Hancock
Hide.

01:24:16 - Brandon Hancock
Yeah, I'll go open up a project really fast and see, just to make sure it is possible.

01:24:21 - Andrew Nanton
Yeah, thank you.

01:24:22 - Andrew Nanton
Well, I guess I have more to say than I thought.

01:24:25 - Brandon Hancock
Of course, of course.

01:24:29 - Bastian Venegas
Just a quick comment, if you needed to build this, you could use Gaussian Blur, that's what they usually use to, like, do this blurring of images, and you could, like, it depends on the problem, but you could detect, like, what timestamp is the thing and just apply it to those frames.

01:24:47 - Bastian Venegas
I'm sure you could do it with fmpeg and Gaussian Blur, like, I'm sure Richard could do it.

01:24:55 - Andrew Nanton
Yeah, well, and, you know, part of the trick, though, is that I'm asking testers to do it, and, you know, some of them...

01:25:00 - Andrew Nanton
We'll be more tech-savvy than others, and I think if it takes more than a couple of clicks, I mean, frankly, even asking them to, like, fence out different areas to blur is, we're already probably getting to the limit of what I could ask.

01:25:12 - Andrew Nanton
Yeah, so.

01:25:15 - Brandon Hancock
I, no, I apologize.

01:25:16 - Brandon Hancock
I'm, I'm in the, I'm in, uh, oh, wait.

01:25:22 - Brandon Hancock
Oh, my gosh.

01:25:23 - Brandon Hancock
They have a sensitive data field.

01:25:25 - Brandon Hancock
Let me share my screen.

01:25:25 - Brandon Hancock
I'll just, uh, it's even better than we thought, man.

01:25:28 - Brandon Hancock
Yeah, so there's a screen, a screen studio.

01:25:31 - Brandon Hancock
Um, I just recorded, uh, I was just sending a message to Sagar really fast.

01:25:36 - Brandon Hancock
But, like, what you could do is, um, oh, I have too many things open.

01:25:42 - Brandon Hancock
Um, but when you go to, um, where is it at?

01:25:49 - Brandon Hancock
I just had it, sorry.

01:25:52 - Brandon Hancock
Oh, gosh.

01:25:53 - Brandon Hancock
Oh, mask.

01:25:54 - Brandon Hancock
Yeah, you got a mask.

01:25:55 - Brandon Hancock
Uh, and then what do you want to do?

01:25:58 - Brandon Hancock
Do you want to highlight something or it's sensitive data?

01:26:00 - Brandon Hancock
Yeah.

01:26:00 - Brandon Hancock
And then you just like, do that.

01:26:02 - Brandon Hancock
And then you can just adjust the timeline down here.

01:26:05 - Brandon Hancock
So like, so you can just play it.

01:26:07 - Brandon Hancock
So it's blocked, it's unblocked.

01:26:09 - Brandon Hancock
Yeah.

01:26:11 - Brandon Hancock
So, yeah.

01:26:12 - Andrew Nanton
you.

01:26:12 - Andrew Nanton
Okay, well, yeah, yeah.

01:26:14 - Andrew Nanton
I mean, any of my testers who are on a Mac, I will, I will probably be springing to buy them a copy.

01:26:22 - Brandon Hancock
Yeah, I'll do that.

01:26:24 - Brandon Hancock
Perfect.

01:26:24 - Brandon Hancock
Yeah, they have, yeah, they have, it's, it's pretty, they have a trial.

01:26:27 - Brandon Hancock
So, I mean, they could all probably do it on the trial without a, without having to go off and pay.

01:26:33 - Brandon Hancock
So, we recommend.

01:26:34 - Brandon Hancock
Okay.

01:26:35 - Brandon Hancock
Awesome.

01:26:36 - Brandon Hancock
All right.

01:26:38 - Brandon Hancock
Okay.

01:26:38 - Brandon Hancock
All right.

01:26:39 - Brandon Hancock
Michael, you are up next, man.

01:26:41 - Brandon Hancock
What's going on?

01:26:43 - Brandon Hancock
What fun stuff?

01:26:43 - Michal Simko
Hey, what's up?

01:26:45 - Michal Simko
So, I took your advice from last week and started refactoring towards a more modular kind of approach, which took me definitely longer than I was hoping.

01:27:00 - Michal Simko
Uh, but let me share my screen so I can...

01:27:06 - Brandon Hancock
Questions on the refactor though.

01:27:07 - Brandon Hancock
Did it make sense as you were doing it?

01:27:09 - Michal Simko
It did.

01:27:10 - Michal Simko
No, it was.

01:27:10 - Michal Simko
Like, it was, yeah, once you were...

01:27:12 - Michal Simko
At first when you started speaking, like, I was like, what does it mean?

01:27:15 - Michal Simko
And then obviously it's one of those things that it's like, once it clicks, then it clicks.

01:27:19 - Michal Simko
And, but when you were drawing it out, then it made sense.

01:27:21 - Michal Simko
And then also when I was building it, it became even more so, you know, clear.

01:27:25 - Michal Simko
Because then you kind of understand why, you know, yeah, it just becomes more material.

01:27:32 - Michal Simko
Uh, but let me fire it up and show you.

01:27:37 - Michal Simko
And I took as well your advice when you were saying to use the one, like one window next to the other, like the two chat windows next to each other.

01:27:46 - Michal Simko
So I'll, I did that.

01:27:49 - Michal Simko
And, um...

01:27:52 - Brandon Hancock
While you're pulling it up, I think Jake has a quick question.

01:27:54 - Michal Simko
Yep.

01:27:55 - Jake Maymar
Yeah.

01:27:55 - Jake Maymar
So super quick.

01:27:57 - Jake Maymar
Um, uh, how, uh, how are you doing the refactoring?

01:28:00 - Jake Maymar
Is there like a, I'll have to check the last meeting, but are you doing it through Claude or something like that, or are you doing it manually?

01:28:09 - Michal Simko
No, I was actually doing it manually, but I was, I, because I wanted to understand it, and so I was doing it manually, but I did help, I mean, I built some scripts to do some of the really like bigger updates.

01:28:26 - Michal Simko
Um, yeah, so it was, it was a mixture, but I wasn't, I'm, for now I'm not using Klein, I'm, I'm, intending to start using Klein, uh, on this one, but, uh, for now it's, it's a bit, yeah, it's been manual.

01:28:41 - Jake Maymar
No, that's great.

01:28:44 - Brandon Hancock
Quick follow-up though, for what, uh, Jake, if you are, if he had wanted to do the refactor inside of a cursor, the easiest way he could have done it, is to say, here is my current file, here's what's wrong with it.

01:29:00 - Brandon Hancock
Such as the, like, currently everything is coupled together, and I would like to decouple it, and then that little drawing I did, Michael, you could have, like, here's what I'm looking to do, to where I have two abstracted files on top, one for the web, one for text, or texting, and they sit on top of the messaging service.

01:29:23 - Brandon Hancock
And it, it probably could have done 80% of it, but then, going back to it, he would have had to, like, probably done some manual things at the end, just because of, like, um, it's not always perfect, and you need a human to review, but if, to speed it up, I think it's another thing, if you're like, you know, for me, the objective also is to learn, right?

01:29:44 - Michal Simko
So, I, I, it, it, somehow, it would take away some of the learning, and it, that's why it took longer, and I'm fine with it, you know, I'm not in a hurry or anything, and so there's no, like, time for sure on this.

01:29:56 - Michal Simko
Um, but basically, uh, now, so, if.

01:30:00 - Michal Simko
I took as well the route that you told me to kind of go more the kind of like the mega prompt.

01:30:09 - Michal Simko
So I have now like different, well, let me actually show the functionalities.

01:30:18 - Michal Simko
So, hi, I'm Peter.

01:30:23 - Michal Simko
All right, Peter, what's your name?

01:30:27 - Michal Simko
So it starts recognizing whether this is like, you know, whether this is a message to the API or whether this is something that should be, hi, how are you?

01:30:47 - Michal Simko
So we kind of recognize the chit chat, tell him he is an idiot, and then he will go like, oh, no, I'm going to block this.

01:30:57 - Michal Simko
So basically I created like these, you know, classic.

01:31:01 - Michal Simko
Or, you know, I can say, okay, I can pick up the kids tomorrow.

01:31:08 - Michal Simko
It will then go, okay, well, that looks fine.

01:31:11 - Michal Simko
And then it will forward the message to the other person, right?

01:31:14 - Michal Simko
So I'm kind of at this stage.

01:31:16 - Michal Simko
Still, very simple.

01:31:17 - Michal Simko
You know, I started, like, testing it on Twilio, as I told you, but then I kind of stopped and I went up, you know, hashed out the logic here first.

01:31:31 - Brandon Hancock
I didn't know it would also be able to pass along messages.

01:31:35 - Michal Simko
I, like, I thought it was a full-on mediator.

01:31:38 - Brandon Hancock
I thought it was strictly, like, okay, that's so cool.

01:31:42 - Brandon Hancock
Great idea.

01:31:43 - Brandon Hancock
Great idea.

01:31:43 - Michal Simko
Yeah, it's really true, you know, so I have, like, for instance, as well, a rephrase.

01:31:48 - Michal Simko
So I have either a pass, if it's enough, if it's clear enough, and it has, like, the logistic organization information that it will pass, you know, it will pass the message to the other person.

01:32:00 - Michal Simko
If

01:32:00 - Michal Simko
Let's say part of the question or the text is, you know, a bit rude or the, you know, it has to be rephrased and it would rephrase it.

01:32:08 - Michal Simko
So there would be, let's say, um, um, she really, I don't know, she really, she really is useless to pick him up tomorrow.

01:32:27 - Michal Simko
It would, oh , okay, uh, there we go.

01:32:32 - Michal Simko
So it says rephrase, and then here's the clear version, and then he would say, can you pick him up tomorrow?

01:32:38 - Michal Simko
So it would, it would, it would have a filter, you know, to pass on the message in a more, you know, uh.

01:32:47 - Michal Simko
Dude, this is awesome.

01:32:49 - Brandon Hancock
What's so funny is someone's gonna get used to talking , and then they're gonna text regularly, and be like, oh my god, I thought it would, I thought it would make it nicer.

01:32:59 - Michal Simko
Yeah, well, I mean.

01:33:00 - Michal Simko
The whole idea is, you know, I mean, this is supposed to work over WhatsApp, right?

01:33:05 - Michal Simko
So really, the next step is to get it into WhatsApp and then also audio, right?

01:33:10 - Michal Simko
So I have, like, I already implemented the audio, like the, you know, the voice to text, but for now on this UI, it's only doing that.

01:33:22 - Michal Simko
So it can rephrase or it can comment or it can block or just directly reply.

01:33:32 - Brandon Hancock
And so, yeah, I mean, it's baby steps, but it's getting somewhere.

01:33:39 - Brandon Hancock
No, that's amazing.

01:33:40 - Brandon Hancock
A few questions for you.

01:33:41 - Brandon Hancock
So on the, so I see this as the prompt.

01:33:43 - Brandon Hancock
Now, when you pass it to the LLM, are you doing a structured output to be like, to showcase, oh, it was a, the action was block and here is the message.

01:33:56 - Brandon Hancock
So, or, okay.

01:34:00 - Brandon Hancock
Okay.

01:34:01 - Michal Simko
Yeah, this is what I get in the log for now, but I could.

01:34:04 - Michal Simko
Okay.

01:34:05 - Brandon Hancock
It's a JSON.

01:34:08 - Brandon Hancock
Yeah, so the thing is, because I was looking at your prompt, and it said at the very end.

01:34:13 - Brandon Hancock
Yeah.

01:34:13 - Brandon Hancock
At the end, it was giving it example JSON outputs, right?

01:34:20 - Brandon Hancock
Yeah, you mean the action?

01:34:22 - Brandon Hancock
Yeah, yeah, yeah.

01:34:23 - Michal Simko
That's for the direct reply.

01:34:25 - Michal Simko
I'm struggling with this one, I have to say, with the direct reply, because it doesn't, it cannot distinguish whether, whether it's like a chit-chat, you just saying, hi, I'm Peter, how are you doing, whatever.

01:34:38 - Michal Simko
Sometimes you would then think it's an okay message, and it would pass it along to the other user.

01:34:43 - Michal Simko
And so I had to kind of like give it more examples.

01:34:47 - Michal Simko
but to be honest with you, I'm, this is a, this is a phase where I'm now, now at, meaning I would like to understand better how I could, like, you know, I'm going to look at how to structure this prompt better to then also

01:35:00 - Michal Simko
Be able to then more, like, easier expand it with having other scenarios, you know?

01:35:05 - Michal Simko
So that was actually, that's where I stopped now, looking at the structure.

01:35:13 - Michal Simko
I think it was something I wanted to ask you, like, yeah, I don't know.

01:35:18 - Brandon Hancock
So what's happening right now, so it's like we're in programming to where it's like, okay, like, I have one Python file that's getting huge, okay?

01:35:28 - Brandon Hancock
So, like, what do I usually do when it happens?

01:35:30 - Brandon Hancock
Like, you do a refactor.

01:35:32 - Brandon Hancock
So, in your case, what I see whenever I'm looking at this is two things.

01:35:37 - Brandon Hancock
I see a classification, and then I see a response instructions.

01:35:43 - Brandon Hancock
So, if you wanted to, you could break this up into two separate LLM calls.

01:35:48 - Brandon Hancock
A router, and the router will return, pass, rephrase, comment, block.

01:35:54 - Brandon Hancock
It, all it, the whole job of the first LLM is to determine what type of prompt this is.

01:36:00 - Brandon Hancock
Then, from there, whatever you get as the output, it then gets sent over to a second LLM call, who's a specialist in responding in that format.

01:36:11 - Brandon Hancock
So that is how you can break it up.

01:36:14 - Michal Simko
I had it like that.

01:36:15 - Michal Simko
I had it like that before.

01:36:17 - Michal Simko
But it was doing the classification inside of the code, and then I was passing it to the LLM.

01:36:24 - Michal Simko
I'm like, no, it was impossible.

01:36:26 - Michal Simko
It was all these ifs and whatnot.

01:36:27 - Michal Simko
It was getting too long.

01:36:28 - Michal Simko
But then I joined it, and next step would be to separate it again.

01:36:35 - Michal Simko
So I had, yeah, I see what you're saying, and definitely that's the next step.

01:36:41 - Brandon Hancock
Otherwise, this is going to become humongous.

01:36:44 - Brandon Hancock
And the cool part is, is when you split it up like that, each sub-prompt is now going to be great.

01:36:52 - Brandon Hancock
Like, you could add way more in there, you know?

01:36:54 - Michal Simko
Yeah.

01:36:56 - Brandon Hancock
Yeah, so that would be just something I would look at.

01:37:00 - Brandon Hancock
good.

01:37:00 - Brandon Hancock
And the only other thing, okay, what are you using for your AI library?

01:37:05 - Brandon Hancock
What are we using?

01:37:06 - Brandon Hancock
Are you using the AI SDK?

01:37:08 - Brandon Hancock
Or what are we using to make LLM calls?

01:37:12 - Michal Simko
LLM calls, I'm using, I don't know, what do you mean?

01:37:20 - Michal Simko
I'm using, yeah, I'm using my OpenAI API.

01:37:24 - Brandon Hancock
What do you mean?

01:37:26 - Brandon Hancock
Okay, yeah, I was, sorry, the thing I was curious is, is like, inside of a Next.js application, you can use, it's called the AI SDK, and that's what I was curious, if that's what you were using to make all these requests.

01:37:41 - Michal Simko
No.

01:37:43 - Brandon Hancock
Okay.

01:37:44 - Brandon Hancock
So, well, are you, follow-up question, is all of this running in the front end or the back end?

01:37:56 - Brandon Hancock
Where, yeah, it's on the back end.

01:38:00 - Brandon Hancock
Okay.

01:38:00 - Brandon Hancock
Here.

01:38:03 - Michal Simko
And then the web app is here.

01:38:08 - Brandon Hancock
Other questions for me.

01:38:11 - Brandon Hancock
Have you tried deploying this by chance to Purcell?

01:38:16 - Michal Simko
No.

01:38:17 - Michal Simko
Okay.

01:38:18 - Brandon Hancock
The reason why is just like sometimes things work locally on your AI applications, and then you'll go to deploy it to the cloud, and it's a different beast, because locally things can run forever, but then when you deploy to Vercel to where things are stateless and purely in the cloud and have timeouts, things can hit limits.

01:38:36 - Brandon Hancock
So before going too much further, you might want to do a quick deployment test and just see if you're hitting any issues.

01:38:44 - Brandon Hancock
Just because I don't, like, if we're going to hit a, if you're planning on deploying this, you might want now at the time to test deployment, rather than going super far down the road, and then be like, oh, my God, I have 200,000 lines of code.

01:38:59 - Brandon Hancock
I'd much rather what it

01:39:00 - Brandon Hancock
Fixed this when I was at 10, you know, so I would test it sooner than later.

01:39:04 - Brandon Hancock
And, yeah, and then Vercel AI SDK, yeah, Bastion also agrees, is the way to make requests, especially if you're going to be deploying this.

01:39:16 - Brandon Hancock
I'll show you the, I'll drop a link for you.

01:39:19 - Brandon Hancock
It's super, it's super similar to what you're, what you're already doing with making calls and everything.

01:39:27 - Brandon Hancock
Um, it's just the Next.js approved approach.

01:39:32 - Brandon Hancock
So, um, cool.

01:39:35 - Michal Simko
Well, yeah, plenty, too.

01:39:38 - Michal Simko
And then the next steps would be, uh, implementing the database and, like, the memory and whatnot.

01:39:45 - Michal Simko
But I didn't get, I was hoping that I'll get there, but it was just taking, and then I started building this, like, a pairing thing.

01:39:52 - Michal Simko
Because once you, so basically how I want to do it is once you're on, on, you know, Twilio, you just...

01:40:00 - Michal Simko
Yeah, I will have to have a way that one message sends a pairing request to another number, which then goes, I accept, because I have to then, you know, at that level, I have to connect them somehow.

01:40:12 - Michal Simko
So, yeah, I started kind of doing these things as well.

01:40:18 - Michal Simko
There's a name for this.

01:40:19 - Brandon Hancock
Why can't I remember it?

01:40:22 - Brandon Hancock
It's not a join key.

01:40:24 - Brandon Hancock
Does anyone remember off the top of your head when you combine two IDs together with, like, an underscore?

01:40:29 - Brandon Hancock
What's the database term for that?

01:40:33 - Brandon Hancock
Yeah, that's what you're trying to do.

01:40:35 - Brandon Hancock
Basically, like, you would have a chat.

01:40:38 - Brandon Hancock
You would have a chat or a conversations, and a conversation at the high level is nothing more than a pairing of user one and user two.

01:40:47 - Brandon Hancock
So, you would have user one ID underscore user two.

01:40:50 - Brandon Hancock
Like, that's how you could look up all active conversations.

01:40:53 - Brandon Hancock
Yeah, it is concatenating, but it's, like, a database-specific thing.

01:40:58 - Brandon Hancock
Oh, God.

01:40:59 - Brandon Hancock
Oh, God.

01:41:00 - Brandon Hancock
I'm embarrassing myself right now.

01:41:04 - Brandon Hancock
Let's see really fast.

01:41:07 - Brandon Hancock
I think it's a join key.

01:41:10 - Brandon Hancock
Indeed.

01:41:13 - Brandon Hancock
I'm just double-checking it.

01:41:14 - Brandon Hancock
But that's what you need to look at implementing, potentially.

01:41:19 - Brandon Hancock
The second opening I get back to me, I will let you know.

01:41:23 - Michal Simko
Yeah, it's a join key.

01:41:25 - Michal Simko
Okay.

01:41:27 - Brandon Hancock
Perfect.

01:41:28 - Brandon Hancock
Yeah, that's what I would, yeah.

01:41:29 - Brandon Hancock
Okay.

01:41:31 - Brandon Hancock
All right, any final things I can help with beforehand?

01:41:37 - Michal Simko
Or it sounds like you're busy.

01:41:39 - Michal Simko
Yeah, yeah, no, I I'm loving it.

01:41:41 - Michal Simko
And thank you for the next, yeah, next steps.

01:41:46 - Michal Simko
And next week I'll show you the progress.

01:41:50 - Brandon Hancock
All right, heck yeah, man.

01:41:51 - Brandon Hancock
I love it, I love it.

01:41:52 - Brandon Hancock
And this was a sick demo, by the way.

01:41:54 - Brandon Hancock
We got some treats today.

01:41:56 - Brandon Hancock
This was amazing with all the awesome things you guys are working on.

01:41:59 - Brandon Hancock
Yeah, excited to see all the...

01:42:00 - Brandon Hancock
The progress you guys keep chugging along.

01:42:03 - Brandon Hancock
Okay, perfect.

01:42:05 - Brandon Hancock
I owe some of you guys some messages.

01:42:07 - Brandon Hancock
I was going to send Sagar a message.

01:42:09 - Brandon Hancock
Abdul, I saw you were sending some messages.

01:42:11 - Brandon Hancock
If you want to just shoot me a DM in school, that's probably the best way, just because the chat here disappears.

01:42:20 - Brandon Hancock
Quick update for what you guys can expect throughout the rest of the week.

01:42:23 - Brandon Hancock
So the ADK Masterclass, it's taken longer to build, but it's a good news, though.

01:42:30 - Brandon Hancock
Because it took longer because I simplified things, like, multiple times.

01:42:33 - Brandon Hancock
So it's, like, much easier to use.

01:42:35 - Brandon Hancock
Like, V3 is what I'm at right now, and it's so much easier to use than what it used to be.

01:42:39 - Brandon Hancock
So very excited for that to come out.

01:42:41 - Brandon Hancock
We'll start recording tomorrow.

01:42:43 - Brandon Hancock
I'm recording all tomorrow, all Thursday.

01:42:45 - Brandon Hancock
So hopefully out by Friday, maybe Saturday at this point.

01:42:49 - Brandon Hancock
And then outside of that, I'm going to be focusing next on a lot more just examples.

01:42:56 - Brandon Hancock
So that's going after this is done.

01:42:59 - Brandon Hancock
I just want to focus on...

01:43:00 - Brandon Hancock
As many real-world example tutorials as possible with ADK and other tools, so that's what I'll be dropping next.

01:43:07 - Brandon Hancock
So moving a little bit away from the high-level tutorials and just like, I automated this for business, I automated this for business, just because I'm not seeing that much developer real-world agent stuff out there.

01:43:19 - Brandon Hancock
So I think that will be a cool way to shine and give you guys some more ideas and examples that you guys can just grab for free too.

01:43:25 - Brandon Hancock
So that's where we're going.

01:43:28 - Brandon Hancock
So, yeah, y'all are awesome.

01:43:30 - Brandon Hancock
It was all, love, love Tuesdays, best day of the week.

01:43:33 - Brandon Hancock
Good to see you guys.

01:43:34 - Brandon Hancock
But yeah, please keep me posted on your projects and y'all crushed it and can't wait to see y'all next week, okay?

01:43:41 - AbdulShakur Abdullah
All right, buddy.

01:43:42 - Brandon Hancock
Have a good day.

01:43:44 - Michal Simko
Good night.

01:43:44 - Brandon Hancock
See you guys.

01:43:45 - Michal Simko
Bye.

01:43:45 - Brandon Hancock
Bye.

01:43:46 - Fernando Lopes Jr.
Thank you.

