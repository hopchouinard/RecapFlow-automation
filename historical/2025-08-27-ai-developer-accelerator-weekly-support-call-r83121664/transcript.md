00:01:12 - Patrick Chouinard
Hi, Marc.

00:01:33 - Marc Juretus
Hey, Patrick.

00:01:34 - Marc Juretus
Sorry, man.

00:01:34 - Marc Juretus
I was in another window.

00:01:36 - Patrick Chouinard
No issues.

00:01:38 - Patrick Chouinard
How are you doing?

00:01:40 - Patrick Chouinard
Good, good.

00:01:42 - Patrick Chouinard
I have some questions for the group tonight for once.

00:01:46 - Patrick Chouinard
That's what we're kind of here for.

00:01:48 - Marc Juretus
That and some light humor here and there.

00:01:53 - Paul Miller
Or especially when a guy falls asleep during the call.

00:01:56 - Marc Juretus
That was great, man.

00:01:57 - Paul Miller
We want to see that virtual popcorn.

00:02:03 - Patrick Chouinard
Yeah, I gotta admit, I did about six or seven hours with N8N over that weekend, man.

00:02:08 - Marc Juretus
That's pretty damn powerful, man.

00:02:10 - Marc Juretus
I published my build on Railway, which was surprisingly really easy to do.

00:02:18 - Marc Juretus
Them webhooks are pretty damn slick, man, I must say.

00:02:21 - Marc Juretus
Yeah.

00:02:22 - Marc Juretus
And it's funny, like the foundation I have from the other frameworks I learned how to use, it's funny when you use that front-end tool, how much easier they are to use because of the other stuff that you've learned.

00:02:33 - Paul Miller
Yeah.

00:02:35 - Marc Juretus
I could definitely do some stuff for some realtors or something around here because just the fact that some of the webhooks I was doing were Google Drive, I had it that, you know, if you were in new names and addresses, as soon as you made a change, it did a route, the webhook caught it, scrubbed the email.

00:02:52 - Marc Juretus
Yeah.

00:02:52 - Marc Juretus
And you had the AI build in the context of the email and build the type of response to go back without even having a, you know, a non-techie.

00:03:00 - Marc Juretus
Could obviously do that pretty simply.

00:03:02 - Marc Juretus
Yeah.

00:03:03 - Paul Miller
Well, it's wonderful for that rapid prototype.

00:03:06 - Paul Miller
Because if you're trying to pitch something, you don't want to go to the effort of having to code that back end quickly.

00:03:12 - Paul Miller
You just want to prototype it and have a really good front end, because they get all excited about the front end.

00:03:21 - Marc Juretus
Yeah, that's pretty, I got to admit, that's pretty slick, man.

00:03:24 - Marc Juretus
They got a whole lot of stuff built in that tool panel there.

00:03:26 - Marc Juretus
So I haven't saved my build I have up on railway, but my question is, once it's on railway, what charges are associated with it?

00:03:37 - Marc Juretus
That's where I'm uncertain.

00:03:40 - Marc Juretus
Like, I know a lot of people are complaining about it when you run it off of their site or whatever.

00:03:44 - Marc Juretus
But if you deploy it somewhere, are the changes as applicable?

00:03:49 - Marc Juretus
That I don't know.

00:03:51 - Paul Miller
I'm running it on, what's that, Ocean?

00:03:55 - Paul Miller
A digital Ocean.

00:03:57 - Paul Miller
Yeah, I'm running it on a digital Ocean, so I'm spending $20.

00:04:00 - Paul Miller
And I've got hundreds of models.

00:04:03 - Paul Miller
It's just a flat, flat cost.

00:04:05 - Paul Miller
That's good.

00:04:05 - Marc Juretus
That's good.

00:04:06 - Marc Juretus
Yeah, I did Railway because I have the stuff I've been showing you with Langchain that I built with Next.js is Railway.

00:04:13 - Marc Juretus
So, but yeah, it was like a couple of clicks.

00:04:15 - Marc Juretus
That was it.

00:04:16 - Paul Miller
It was up.

00:04:17 - Marc Juretus
And then I was like, damn, I might as well start throwing some webhooks in here.

00:04:21 - Paul Miller
It doesn't need a lot of capacity.

00:04:24 - Paul Miller
Really, it's just, it's not a lot of RAM and a bit of disk space.

00:04:28 - Paul Miller
The question is if you want to run a database alongside it because you might want to run an instance of Postgres, whatever, and have it tying in closely to it.

00:04:44 - Marc Juretus
Yeah.

00:04:46 - Marc Juretus
Yeah, that was, yeah, it's pretty slick, man.

00:04:49 - Marc Juretus
And it's like, you know, yeah, I was doing the thing where I was submitting like a form and then you answered a few questions and then it emailed you back a story about you.

00:04:59 - Marc Juretus
Like, you know.

00:04:59 - Marc Juretus
The agent's context was, take the person's name and their occupation, and I want you to write a three or four paragraph story, and then send it back to them.

00:05:08 - Marc Juretus
was pretty slick.

00:05:09 - Marc Juretus
Cool.

00:05:18 - Patrick Chouinard
I'm going to have an interesting one for the group tonight.

00:05:23 - Paul Miller
Good.

00:05:23 - Paul Miller
We like interesting.

00:05:25 - Paul Miller
Yep.

00:05:26 - Patrick Chouinard
I've been put in the position of managing the integration of VibeCoding, but in a corporate environment, and manage between the desire of the business to put coding tools lovable in the end of business user, but with cybersecurity, it says, wait, we want to control that thing.

00:05:51 - Paul Miller
Oil and water, I think.

00:05:55 - Patrick Chouinard
You're kind of the scariest thing.

00:06:00 - Patrick Chouinard
Yeah, actually, the request came in about half an hour ago, so.

00:06:04 - Paul Miller
Oh, my goodness.

00:06:05 - Paul Miller
Oh, well, you're on the right call.

00:06:09 - Patrick Chouinard
Exactly my thought.

00:06:11 - Patrick Chouinard
The first thing I thought when I said, okay, that came in the right day of the week.

00:06:17 - Paul Miller
Hey, Brandon.

00:06:19 - Paul Miller
Hello, hello, gang.

00:06:20 - Brandon Hancock
All right, let's get everything set up real fast.

00:06:24 - Brandon Hancock
All right, go.

00:06:27 - Brandon Hancock
Hope everyone's had an awesome week so far.

00:06:30 - Brandon Hancock
Let's see.

00:06:32 - Brandon Hancock
Okay, awesome.

00:06:34 - Brandon Hancock
Okay, cool.

00:06:34 - Brandon Hancock
So before we kick it off, I want to show you guys what cool things I've been working on, and then we'd love to go, you know, round robin like we normally do, questions first, and then immediately after that we can hop into, you know, just general updates, see all the awesome things you guys are working on.

00:06:49 - Brandon Hancock
So, long story short, from the moment for ShipKit.

00:06:59 - Brandon Hancock
So I want to show you guys.

00:07:01 - Brandon Hancock
Oh, can y hear me?

00:07:03 - Brandon Hancock
Yeah.

00:07:04 - Patrick Chouinard
Now we can.

00:07:04 - Patrick Chouinard
We just lost you for a couple seconds.

00:07:06 - Patrick Chouinard
Okay, perfect.

00:07:08 - Brandon Hancock
But yeah, long story short, from dawn to dusk, knocking out Shipkit, so I just want to show you guys quick progress update.

00:07:14 - Brandon Hancock
So it's cool.

00:07:16 - Brandon Hancock
Everything in here, when it comes to making apps, I just want show you guys, everything is prompt-driven, which I think is so cool because one of the coolest things about it is when making apps is, you know, you're always staring at a blank screen, but now what's sick is prompts do all the hard work for you, from like coming up with the ideas to, you know, doing all the hard work for you.

00:07:39 - Brandon Hancock
So what is cool about it is, because I want to make sure you guys absolutely crush it.

00:07:44 - Brandon Hancock
So not only is there the course, then there's the actual prompt that does all the like hard work for you and walks you through it.

00:07:52 - Brandon Hancock
But then to make it even easier, what I'm doing is showing how to take like each template.

00:07:58 - Brandon Hancock
So like...

00:08:00 - Brandon Hancock
to take the RAG template and convert it into an application.

00:08:03 - Brandon Hancock
How to take the chat template and convert it into your own custom application.

00:08:07 - Brandon Hancock
How to take the ADK agent, convert it to your own custom application.

00:08:09 - Brandon Hancock
So like literally everything has like a course, a prompt, multiple examples.

00:08:14 - Brandon Hancock
So I don't know.

00:08:15 - Brandon Hancock
I'm so pumped.

00:08:15 - Brandon Hancock
I think this is how all courses will be in the future.

00:08:20 - Brandon Hancock
Just, you know, I think being an AI, we're kind of like ahead of the curve.

00:08:24 - Brandon Hancock
But yeah, so it's definitely, definitely like it, like I'm using it to like build stuff out myself.

00:08:31 - Brandon Hancock
I'm like, man, this is so much more nice than everything else I've previously done where usually you have to do all the hard work yourself.

00:08:37 - Brandon Hancock
So absolutely, it's a ton of work, but I think you guys are really going to like it.

00:08:41 - Brandon Hancock
It's coming along insanely well.

00:08:42 - Brandon Hancock
So just need to do this.

00:08:44 - Brandon Hancock
I think there's 25 more days, guys.

00:08:46 - Brandon Hancock
So a lot less sleep, a lot more work.

00:08:48 - Brandon Hancock
And yeah, keep grinding.

00:08:50 - Brandon Hancock
So, but yeah, that's everything on my side.

00:08:54 - Brandon Hancock
For ShipKit, did a few videos for Gemini CLI recently.

00:08:58 - Brandon Hancock
If you guys have any questions on that, super.

00:09:00 - Brandon Hancock
happy to dive into that one as well, but if not, what I'm going to do, take a quick screenshot here, and then we will just go in this order, and so we'll go in the order that I'm dropping in right now once we get past questions, but we'll hop into questions super fast.

00:09:19 - Brandon Hancock
So Juan was basically like, it seems that most industry prefer LangChain and LangGraph.

00:09:24 - Brandon Hancock
Do you feel like this is the case?

00:09:26 - Brandon Hancock
I see the modus operandi agentic framework requested in job postings.

00:09:32 - Brandon Hancock
Yeah, so definitely on bigger enterprise companies, yes, they are more involved.

00:09:38 - Brandon Hancock
They are probably more in demand.

00:09:40 - Brandon Hancock
So yeah, one of the big things, like literally the next thing in the queue is to add in a LangChain version, just because I think it is one of the most in demand.

00:09:50 - Brandon Hancock
It's just 80k, it is so easy to get going and get using, that we definitely wanted to make it a little bit more beginner friendly, so that's why it's 80k.

00:10:00 - Brandon Hancock
In the big boys, when you have more time and everything, and you understand nodes, edges, graphs, that's when Langchain really comes in.

00:10:08 - Brandon Hancock
And then Patrick was basically asking, how do you integrate vibe coding practices inside a corporate environment, i.e.

00:10:14 - Brandon Hancock
the business user wants a lovable experience, and CyberSec wants something that they can control, and nobody realizes that vibe coding is not magic.

00:10:23 - Brandon Hancock
You still need to know what you're doing.

00:10:24 - Brandon Hancock
Yeah, so awesome question, Patrick.

00:10:26 - Brandon Hancock
I mean, one of the cool things that I think that you can do is, like, at the end of the day, you know, I think you being on both sides of the spectrum of, like, understanding what both teams want, I mean, one of the coolest parts is, like, what you can actually quantify what cybersecurity wants, and, like, it literally just comes down to making an insane amount of prompts.

00:10:48 - Brandon Hancock
So one of the main things that I just added to, you know, the ShipKit course was when we go from, like, hey, we've come up, I'm going to to show you real fast, because I think this is the easiest way to show it.

00:10:59 - Brandon Hancock
So you

00:11:00 - Brandon Hancock
can hopefully steal it for your stuff too.

00:11:02 - Brandon Hancock
One second, I'll share.

00:11:05 - Brandon Hancock
But yeah, so like one of the main things that I like to do is if you watch all my recent ADK videos, I'm a huge fan of doing the generate critique pattern with agents to where agent one does action.

00:11:19 - Brandon Hancock
And then immediately afterwards, you follow it up with a critique and then you do this cycle a few times.

00:11:25 - Brandon Hancock
Well, you know, what you could do, because like that's exactly what I did in this document.

00:11:30 - Brandon Hancock
I'll just show you real fast, critique.

00:11:31 - Brandon Hancock
Yeah.

00:11:32 - Brandon Hancock
So basically you do a critique.

00:11:34 - Brandon Hancock
Yeah.

00:11:35 - Brandon Hancock
So basically what you do is you could have a cybersecurity guy and he would come up with what he initially needs.

00:11:42 - Brandon Hancock
And what it could do is like generate an analysis of the application that they built, come up with a cybersecurity, you know, come up with a cybersecurity critiques of it, implement the changes and go through it a few times.

00:11:54 - Brandon Hancock
Because that is one of the easiest ways to like make sure that you get their requirements out of their head.

00:11:59 - Brandon Hancock
Yeah.

00:12:00 - Brandon Hancock
Because that's one of the worst parts about working with cybersecurity teams is they're like, it's not secure.

00:12:04 - Brandon Hancock
And then you go, okay, well, how do I make it secure?

00:12:07 - Brandon Hancock
And they're like, well, and then, yeah, I don't know.

00:12:10 - Brandon Hancock
feel like it...

00:12:10 - Patrick Chouinard
Honestly, their question, it's not as much as they don't think it's secure because they understand that what would be vibe-coded is more prototype and proof-of-concept type of application, not full-fledged production application.

00:12:25 - Patrick Chouinard
Certainly not by business user.

00:12:26 - Patrick Chouinard
And the challenge is I love all of your template, but they're extremely good tools for developer that use development assisted by AI, like Cursor.

00:12:37 - Patrick Chouinard
I cannot give a financial analyst Cursor and say, have at it.

00:12:42 - Patrick Chouinard
They're looking for the lovable experience, the IDE-free type of development.

00:12:48 - Patrick Chouinard
So that's the challenge that I have is I want to give them something, but not something they're going to break everything with.

00:12:56 - Patrick Chouinard
So what cybersecurity wants is the tool that they can control.

00:13:00 - Patrick Chouinard
We can talk afterward about all the spec that they need to respect.

00:13:06 - Brandon Hancock
I gotcha.

00:13:07 - Brandon Hancock
Yeah, mean, that's like the, yeah, no, that's a very interesting point to bring up because like, I don't know if agents are fully there yet to where like, they can just build an entire application that is like, perfect, you know, that meets what cybersecurity wants, what the front end guys towards super easy.

00:13:24 - Brandon Hancock
It's definitely not there yet, but I mean, it 100% is going in that direction, but you know, it's kind of like, if you're not a car mechanic, you can't just go fix a car.

00:13:35 - Brandon Hancock
Like, you know, like you can't just go build a car, like, and I can't just build it.

00:13:39 - Patrick Chouinard
Yeah.

00:13:39 - Brandon Hancock
So the challenge we have right now is all the big consulting firm are going to them and say, oh, you're going to be late.

00:13:45 - Patrick Chouinard
You're going to be late.

00:13:46 - Patrick Chouinard
You need to do that.

00:13:47 - Patrick Chouinard
Or you're going to be left in the dust, but Hey, yes.

00:13:51 - Patrick Chouinard
Okay.

00:13:51 - Patrick Chouinard
And now the management is extremely happy.

00:13:55 - Patrick Chouinard
They want to go forward.

00:13:56 - Patrick Chouinard
They want to, they have budget.

00:14:00 - Patrick Chouinard
How much do you need?

00:14:01 - Patrick Chouinard
Go, make that happen.

00:14:03 - Patrick Chouinard
It's like, yeah, but I want to make that happen so in six months it's still going to work.

00:14:08 - Brandon Hancock
Right, right.

00:14:09 - Brandon Hancock
I mean, yeah.

00:14:10 - Brandon Hancock
I mean, the cool part is a very small development team joined with the cybersecurity guys could do the work of what used to be 10, you know?

00:14:18 - Brandon Hancock
So, like, you're not going to get left behind as long as you're the few developers that you are using are using the tools properly.

00:14:25 - Brandon Hancock
You know, I wouldn't say left behind.

00:14:27 - Brandon Hancock
I definitely think they could, paired with the right tools, do it.

00:14:31 - Brandon Hancock
An insane amount of awesome work.

00:14:33 - Brandon Hancock
And then, Adam, basically you were saying, I guess your daughter yesterday, I'm trying to read the thing.

00:14:43 - Brandon Hancock
Yeah, Adam, do you want to hop in on that?

00:14:45 - Brandon Hancock
I'm curious what you were saying.

00:14:46 - Brandon Hancock
I mean, I'm just cool to hear what is happening.

00:14:48 - Adam
Yeah, so, yeah, my daughter called yesterday and she's like, well, I want my class schedule and she wanted it changed.

00:15:00 - Adam
From what she had.

00:15:01 - Adam
And so she had a list of her current schedule and basically a list of how many students are in each class and each subject.

00:15:10 - Adam
So like a school breakdown kind of thing.

00:15:14 - Adam
And she's like, well, I'm swapping classes, swap this, but this, she's all.

00:15:18 - Adam
But so he basically created a chain, right?

00:15:20 - Adam
So I'm swapping class.

00:15:23 - Adam
Let's see chemistry for biology.

00:15:24 - Adam
Now I'm swapping class for, so now after that, I'm going to swap math for English kind of thing.

00:15:34 - Adam
And she quickly realized that, okay, after you get a chain of like four or five, you just can't hold that in your head mentally, right?

00:15:42 - Adam
So she couldn't figure out how to do this manually.

00:15:46 - Adam
And she's like, can I use AI?

00:15:47 - Adam
She's trying to use AI for this.

00:15:51 - Adam
And so she takes all the information from her school, uploads it to ChatGPT.

00:15:58 - Adam
And the problem she...

00:16:00 - Adam
Ran into, well, first, she didn't realize that ChatGPT can generate Python and run it.

00:16:06 - Brandon Hancock
So that was kind of the eye-opener for her.

00:16:08 - Brandon Hancock
bulb moment, yeah.

00:16:09 - Brandon Hancock
Yeah, light bulb moment.

00:16:10 - Adam
And then she was actually pretty good.

00:16:12 - Adam
Without reading any of the code, she realizes that she had data input problems, like the graph was cut off when she screenshotted it and stuff.

00:16:23 - Adam
But she eventually, they kept on saying it was infeasible.

00:16:30 - Adam
And then finally, I'm like, well, I got to go to dinner.

00:16:33 - Adam
I'll take a look at this.

00:16:36 - Adam
And I looked, and she actually had problems with, not her prompts, but her problem was, the way the university listed it up was the, of course, now I'm just rambling on, but the spring semester and the fall semester, they made the columns different orders in the two.

00:17:00 - Adam
And this was confusing the parser, so once I fixed that, that generated the Python code, ran it, we had to add some more constraints, generated more Python code, ran it again, and if she swapped six classes, she could get to the schedule she wanted, and she went to her advisor with that proposal, and the advisor said sure, and so now she's got the schedule she That's awesome.

00:17:31 - Brandon Hancock
Yeah, I think it's insane that students, like, I think in China right now, at the age of like six, they have to start using AI to do stuff, which is wild, because like, you know, if you're not using it, your output is drastically lower than someone who is using it, and yeah, that is wild, so I think, I hope more and more people, like, I hope all, the entire education system starts using it, one way or another, because if not, I mean, we're hosed.

00:18:00 - Brandon Hancock
Yeah.

00:18:01 - Adam
So it seems like a big thing with education is everyone's just talking about kids cheating on stuff.

00:18:07 - Adam
Yeah.

00:18:07 - Adam
But the kids just, they figure out how to do things.

00:18:11 - Brandon Hancock
I mean, yeah.

00:18:11 - Brandon Hancock
I mean, yeah, we can, I mean, we can dive into the education side of it, but yeah, I mean, I, no.

00:18:17 - Brandon Hancock
My, everyone in my family, if like one of my nieces and nephews, they know AI.

00:18:22 - Brandon Hancock
I have made sure of it.

00:18:24 - Brandon Hancock
They will not be left behind.

00:18:26 - Brandon Hancock
But yeah.

00:18:27 - Brandon Hancock
But yeah, guys, if no more questions, what we can do is we'll just start going round Robin and would love to hear all the awesome things you guys have been working on.

00:18:34 - Brandon Hancock
And if you are stuck on anything or we can help with anything, hey, that's what we're here for.

00:18:39 - Brandon Hancock
So I'm dropping a few more people joined.

00:18:40 - Brandon Hancock
So I'm dropping in the updated order in the chat right now.

00:18:45 - Brandon Hancock
So yeah.

00:18:45 - Brandon Hancock
It looks like, Marc, you're up first, man.

00:18:51 - Marc Juretus
Sorry, I had to turn the audio on.

00:18:54 - Marc Juretus
I'm technically challenged.

00:18:57 - Marc Juretus
So yeah.

00:18:57 - Marc Juretus
So what I was working on, I was talking to Paul earlier.

00:18:59 - Marc Juretus
So.

00:18:59 - Marc Juretus
helpful.

00:18:59 - Marc Juretus
I'm Thank you.

00:19:00 - Marc Juretus
So I engulfed myself with about seven, eight hours of N8N, so I was practicing with the webhooks, because if I ever try to like do some work on the outside, I'm not going to build a Langchain Langraft flow or like a complex project, I can probably accomplish something if there's some small businesses or customers that would want to work with me.

00:19:20 - Marc Juretus
So I was pretty impressed with the webhooks.

00:19:22 - Marc Juretus
I was doing the forms, I was having forms submit where you pass the name and, you know, where you worked, and then I had it right, like, had the AI write, like, a four-paragraph story about you, bogus.

00:19:33 - Marc Juretus
So I see a lot of capabilities with that, and I was telling Paul, because of my foundational known crew, Lang and all that, was, it's, you can really run with that stuff where, well, I don't have to write a library, I don't have to write a class, I could just do this.

00:19:46 - Marc Juretus
I could probably at least prototype something for somebody if they wanted, you know, me to do some work for them.

00:19:52 - Marc Juretus
Real, like that, like the one with the Google Drive was impressed the hell out of me where I had a sheet.

00:19:56 - Marc Juretus
You made a change to the sheet, it triggered that webhook.

00:19:59 - Marc Juretus
It

00:20:00 - Marc Juretus
And then customs struck out an email based on what was in the subject in the body.

00:20:04 - Marc Juretus
So I could see a ton of usages for it.

00:20:06 - Marc Juretus
So it's just good to know the front end stuff.

00:20:09 - Marc Juretus
So, um, but no, sorry, go ahead.

00:20:12 - Brandon Hancock
No, I'll just say it is insane how, how easy it is to get started with N8N and the amount of value you can add in like two hours to any business with N8N.

00:20:21 - Brandon Hancock
Just because most of the time, like it's the glue, N8N can become the glue of the business to handle everything you're saying.

00:20:28 - Brandon Hancock
Hey, every time this happens, trigger this literally and then go build an insane automation.

00:20:32 - Brandon Hancock
So, no, uh, I definitely think a very cool, very cool skill to learn.

00:20:37 - Brandon Hancock
Um, and you can instantly because it's already deployed, go help out anyone.

00:20:40 - Brandon Hancock
So, no, awesome.

00:20:42 - Brandon Hancock
Yeah.

00:20:43 - Marc Juretus
I think time very well spent.

00:20:44 - Brandon Hancock
Yeah.

00:20:45 - Marc Juretus
I published it too.

00:20:46 - Marc Juretus
So I want to go up and play with it.

00:20:47 - Marc Juretus
So I actually published, uh, up to Railway.

00:20:49 - Marc Juretus
So I have an app up there, but I want to start, uh, you know, build some stuff up there.

00:20:53 - Marc Juretus
And, uh, I would say Paul claims that it was 20 bucks a month to, to have that hosted.

00:20:58 - Marc Juretus
It up there.

00:20:58 - Marc Juretus
So I want to play with that.

00:21:00 - Marc Juretus
So, I have an instance that's actually accessible from the outside.

00:21:03 - Marc Juretus
After that, I obviously have the fantasy thing done.

00:21:06 - Marc Juretus
So, the next thing is I want to build a, like I've said this before, I want to build a bogus company where I'll have jobs listed where you apply for a job, it'll respond to the resume, see if you were qualified while you weren't or not, it'll send you a bogus appointment for an interview.

00:21:21 - Marc Juretus
I'll have a chat that runs inventory as well as answers questions.

00:21:24 - Marc Juretus
So, if somebody was asked, what have you done with AI?

00:21:27 - Marc Juretus
Here, go to this bogus site.

00:21:28 - Marc Juretus
You can join as, you know, you can can apply for a job.

00:21:31 - Marc Juretus
can look at our, you know, our inventory listing, this and that.

00:21:33 - Marc Juretus
So, that's going to be my objective.

00:21:35 - Marc Juretus
Like, hey, what have you done?

00:21:36 - Marc Juretus
Here you go.

00:21:37 - Marc Juretus
And that's awesome.

00:21:38 - Marc Juretus
Yeah.

00:21:39 - Brandon Hancock
You're setting yourself up for success, man, because like the second you can start to do it for yourself, then you can show it to others.

00:21:44 - Brandon Hancock
They're like, okay, you look competent.

00:21:46 - Brandon Hancock
Yeah.

00:21:46 - Brandon Hancock
You know, they throw you a small project and then you're off to the races and then you start the snowball, man, because, hey, I've done it for this guy.

00:21:53 - Brandon Hancock
can do it for you.

00:21:54 - Brandon Hancock
So, you're literally in the hardest part, I dare say, which is showcasing that you know how to use the skills.

00:22:00 - Brandon Hancock
And landing that first, you know, first real world client of some sort to help out.

00:22:04 - Brandon Hancock
So this is, this is, this is the hardest part.

00:22:07 - Brandon Hancock
Everything after this gets so much easier.

00:22:09 - Brandon Hancock
So, uh, don't give up, man.

00:22:10 - Brandon Hancock
This is a, this is exciting.

00:22:12 - Marc Juretus
Yeah.

00:22:13 - Marc Juretus
Um, I got, I'm cutting out about 630.

00:22:15 - Marc Juretus
have a fantasy draft tonight at seven with the guys from work.

00:22:17 - Marc Juretus
So it's that time of year.

00:22:19 - Marc Juretus
So.

00:22:21 - Brandon Hancock
All right.

00:22:21 - Brandon Hancock
Well, you'll have to keep us posted on how that goes too.

00:22:24 - Marc Juretus
Yeah.

00:22:24 - Marc Juretus
Yeah.

00:22:24 - Marc Juretus
Yeah.

00:22:24 - Marc Juretus
We'll see.

00:22:25 - Marc Juretus
All right.

00:22:26 - Brandon Hancock
Perfect.

00:22:26 - Brandon Hancock
Uh, of course.

00:22:28 - Brandon Hancock
All right, Mitch, you are up next.

00:22:30 - Brandon Hancock
I should have brought my hat.

00:22:32 - Brandon Hancock
Alex Sermozzi all the way.

00:22:33 - Brandon Hancock
Have you got to read, uh, the money models yet?

00:22:36 - Mitch
No, no, I have not.

00:22:38 - Mitch
But, uh, someone sent me over the playbooks and stuff.

00:22:42 - Mitch
I haven't even read those, but they seem to be good.

00:22:45 - Mitch
I gotcha.

00:22:46 - Brandon Hancock
I will say just like side note.

00:22:48 - Brandon Hancock
So many people, whenever a hundred million leads and a hundred million offers came out, so many people talked about like I'm using this book to do blank.

00:22:56 - Brandon Hancock
I haven't heard anything yet on the new one.

00:22:58 - Brandon Hancock
So I'm just curious if if I'm I'm I

00:23:00 - Brandon Hancock
Is it, is it too technical?

00:23:01 - Brandon Hancock
Does it not a, I don't know, maybe I just need to, um, dive deeper into it.

00:23:05 - Brandon Hancock
It's for, uh, established businesses, right?

00:23:07 - Mitch
So it's like you're currently having one money model that works well, now it's like figuring out how to take your current offer and then make like a smaller offer, know, a downsell offer, upsell offer, you know, you sell, I don't know.

00:23:22 - Brandon Hancock
I guess, I guess they're winning, so they don't want to talk about it.

00:23:25 - Brandon Hancock
So no one, no one steals their ideas.

00:23:27 - Brandon Hancock
So I guess it makes sense.

00:23:29 - Mitch
Yeah.

00:23:30 - Mitch
I think, I think the people who naturally talk right on social media, it wouldn't be as valuable for them versus like a genuine business more so.

00:23:39 - Mitch
Yeah.

00:23:40 - Brandon Hancock
No, I agree.

00:23:41 - Mitch
That's a good point.

00:23:41 - Brandon Hancock
But yeah, dude, what's up?

00:23:42 - Brandon Hancock
What are we working on?

00:23:43 - Brandon Hancock
I know you were cranking out some, some awesome workflows.

00:23:47 - Mitch
Yeah.

00:23:47 - Mitch
It's funny how one problem becomes like eight, but my main question is, so for like webhooks, is there a, a general guideline for how much data I can send via a webhook via for much data they're

00:24:00 - Mitch
And Supabase, I was trying to find any resources on it, and I couldn't.

00:24:05 - Brandon Hancock
So, okay, so usually, a webhook, you will tell me what you're trying to do, and then I can give some guidance.

00:24:12 - Brandon Hancock
Because from my understanding, you're trying to kick off a project, correct?

00:24:15 - Brandon Hancock
Like an AI workflow to go off and perform actions.

00:24:19 - Brandon Hancock
So where you, my understanding is, I'm just going to guess, is you were thinking of, like, getting all of the data, everything in a blob, and one huge JSON object, and then send it into webhook, is what I'm guessing.

00:24:32 - Mitch
Yes, sir.

00:24:34 - Brandon Hancock
Dude, okay, that's, so here's usually what people go and do.

00:24:40 - Brandon Hancock
Whatever logic you had in your application that was putting together that huge, like, step one, two, three, four, five, six, seven, they usually move that into, like, the very first step inside their backend code.

00:24:55 - Brandon Hancock
So usually, instead, what they'll do is, like, send in the webhook, like, hey.

00:24:59 - Brandon Hancock
be.

00:24:59 - Brandon Hancock
Yeah.

00:24:59 - Brandon Hancock
can Yeah.

00:24:59 - Brandon Hancock
Now, All I'm my

00:25:00 - Brandon Hancock
Here's the job ID, here's the whatever.

00:25:03 - Brandon Hancock
Then once it receives the request, then it goes, okay, I know step one is to build out that monster JSON object that had everything it needed.

00:25:12 - Brandon Hancock
So usually best practice, you don't want to send an insane amount of data.

00:25:17 - Brandon Hancock
However, with that said, there's nothing stopping you from sending an insane amount of data.

00:25:22 - Brandon Hancock
Like, you know, the internet specifically, like REST protocols could easily handle a few hundred kilobytes, even, I can't remember if you can go up to a megabyte.

00:25:31 - Brandon Hancock
I know, I know Next.js and Vercel itself, I think has a one or four megabyte default stopping point.

00:25:37 - Brandon Hancock
So it actually depends what Vercel allows at this point.

00:25:41 - Brandon Hancock
So that would, that's what I would look at.

00:25:44 - Mitch
Yeah, and Supabase, because I think they're the ones sending the data too.

00:25:49 - Mitch
And I think they might have a limit.

00:25:50 - Mitch
So I was going to test with NADNC, just real quick, instead of doing the whole Google Cloud Functions thing.

00:25:56 - Mitch
And then, yeah, I guess the solution is just send the IDs.

00:26:02 - Brandon Hancock
Yeah, because it sounds like you already had the logic, because it was already building it one time, so now it's just like actually just move that build logic into the background job that was actually going to run it, and then you don't even have to worry about size limits because you're literally sitting over like 30 characters, you know?

00:26:18 - Mitch
Perfect.

00:26:18 - Mitch
And then the other question I have is actually in the chat.

00:26:21 - Mitch
So Superbase has been like messaging me about like, oh my gosh, your databases are like unrestricted and stuff.

00:26:28 - Mitch
I'm going to hack you, dude.

00:26:29 - Brandon Hancock
We're all going to hack you as soon as this calls over.

00:26:31 - Mitch
Uh-oh.

00:26:31 - Mitch
Well, here's my IP address in case you guys don't have it.

00:26:35 - Brandon Hancock
Thank you for making our lives easier.

00:26:37 - Mitch
Okay.

00:26:37 - Mitch
So let me clear this up.

00:26:39 - Brandon Hancock
I hate that they do this.

00:26:40 - Brandon Hancock
Okay.

00:26:41 - Brandon Hancock
What that means is, have you used Firebase before by chance?

00:26:45 - Mitch
No.

00:26:46 - Mitch
I've heard that's a good thing.

00:26:48 - Mitch
I haven't used Firebase, but I don't know.

00:26:49 - Brandon Hancock
So what normally happens is you can actually create like a Superbase client, and what a lot of times...

00:27:00 - Brandon Hancock
It's like people will literally like allow users to use that client throughout their application, which allows them to almost write queries and like request data, which is why it's saying it's unrestricted.

00:27:12 - Brandon Hancock
So if you were to create that client and allow your users to like fetch information, yes, the data is unrestricted and they could get your information, they could get mine, you know, in the user's table, they could grab everyone's information.

00:27:25 - Mitch
So, especially if they figured out which, yeah.

00:27:28 - Brandon Hancock
So what we're doing is we do not use Supabase client unless it's in a pre-structured API call, a pre-structured query or a pre-structured mutation.

00:27:42 - Brandon Hancock
So like there's no way the user can ever access that differently.

00:27:47 - Brandon Hancock
So you, I hate that they do that.

00:27:50 - Brandon Hancock
I wish there was a button to turn it off saying like, I'm not using that feature of Supabase.

00:27:53 - Brandon Hancock
Therefore, I don't care.

00:27:56 - Brandon Hancock
But yeah, if you want to share how you are using Supabase.

00:28:00 - Brandon Hancock
We can look at it together real fast, but long story short, if you're doing stuff like, are you using API endpoints more?

00:28:07 - Brandon Hancock
Are you using cloud server functions?

00:28:10 - Brandon Hancock
What are you mostly doing to go from Next.js to Supabase?

00:28:14 - Brandon Hancock
What does that look like?

00:28:15 - Mitch
I just use Drizzle and I have things over the rest, baby.

00:28:19 - Mitch
Okay, so you're probably doing like Drizzle, Table, and then you're like, give me the user and this table, which is perfect.

00:28:28 - Brandon Hancock
Perfect, so that you're already doing it to where like, the user is not, like they're using Drizzle, like that's the key thing here, like they're using Drizzle to make a request to your backend database.

00:28:38 - Brandon Hancock
So once again, like you're not using Supabase to access that table.

00:28:42 - Brandon Hancock
So that's why I said I wish you could, I wish you could turn that off because you're safe, you don't have to worry about it.

00:28:49 - Brandon Hancock
Cool, yeah.

00:28:50 - Mitch
So we won't be hacking you today, maybe tomorrow, but not today.

00:28:54 - Brandon Hancock
Oh, wow.

00:28:55 - Mitch
Okay, well, I'll change my schedule.

00:28:57 - Brandon Hancock
I'll change my schedule I guess not.

00:29:00 - Mitch
But yeah, cool, I'm good.

00:29:01 - Mitch
Okay, perfect.

00:29:02 - Brandon Hancock
And then, just to answer your question, Paul, will you provide Python path frontends as well?

00:29:12 - Brandon Hancock
Could you just elaborate on this super fast, Paul, what mean?

00:29:14 - Brandon Hancock
Like, are you talking about like a Gradio app?

00:29:18 - Paul Miller
Yeah, well, you've got the prompt where you can say, I want TypeScript or I want to use Python.

00:29:25 - Paul Miller
And on the video, you talked about, oh, the thing's going to help with Python backends.

00:29:30 - Paul Miller
Are you going to help with the Python frontend?

00:29:32 - Paul Miller
Because for some of us, like TypeScript, you're thinking, oh my God, I don't know if I could deal with building a TypeScript app.

00:29:39 - Paul Miller
I'd love to build a Python app using, not Gradio, but sort of beta Python type.

00:29:47 - Paul Miller
Not that it's better than TypeScript, but in a world that I understand it with what you're doing with Shipkit.

00:29:54 - Brandon Hancock
Yeah, so I mean, the key thing here is like, what we're trying to do is like, what is the most common?

00:30:00 - Brandon Hancock
I real-world tools that people are using, and most, I mean, at this point, if you're trying to build an application, like a front-end application in 2025, it is done with Next.js, like, we could probably look up a chart, but I think it's like, it's an insane amount of all new real-world applications are using it, just because it's so easy to use, it's so standard, there's so many support documents, like, it is the standard.

00:30:25 - Brandon Hancock
What's also great about it is, like, AI truly understands Next.js this day and age, because there's so much training data on it, so it can do a much better job, too, so, like, even though, even though the, you know, even though TypeScript is definitely, like, a little bit more, like, there is a steeper learning curve, I mean, AI can really does handle a lot of it for you, so, yeah.

00:30:51 - Brandon Hancock
Right, so stick with Python back-end, and come on, Paul, make the jump, it's cleaner, it's better, let's just do it.

00:30:59 - Brandon Hancock
100%, and...

00:31:00 - Brandon Hancock
Dude, one of the things I really want to work on post-launch is I really want to do a TypeScript course for you guys, a Python course, and just a straight up Vanilla Next.js course, just because I still think, like what you're saying, Paul, like there's still a lot of people who are like very strong in one area and not another, so I want to like spread the knowledge, so definitely we'll be doing that at some point.

00:31:24 - Brandon Hancock
So yeah, it'll probably be, it'll probably be October, because the next 20, 25 days are busy, but those are big things I want to work on.

00:31:33 - Brandon Hancock
So I think that'll be super helpful.

00:31:36 - Brandon Hancock
And yeah, thank you, Mitch, on the templates.

00:31:41 - Brandon Hancock
All right, yeah, they're, they're insane.

00:31:43 - Brandon Hancock
I just, quick update.

00:31:46 - Brandon Hancock
Well, I won't go into that.

00:31:48 - Brandon Hancock
All right, we'll go next.

00:31:49 - Brandon Hancock
Juan, you're up next, buddy.

00:31:56 - Brandon Hancock
I think we can hear you.

00:31:57 - Brandon Hancock
It's kind of quiet.

00:32:00 - Brandon Hancock
Oh, really?

00:32:00 - Juan Torres
Okay, I'm going to speak louder.

00:32:02 - Brandon Hancock
Yeah, I can hear you.

00:32:04 - Brandon Hancock
Yeah, cool.

00:32:05 - Juan Torres
Yeah, so last week I was able to resolve the great issue that my client was facing now.

00:32:13 - Juan Torres
Hey, that's awesome.

00:32:14 - Juan Torres
Congrats, man.

00:32:16 - Juan Torres
Yeah, yeah.

00:32:17 - Juan Torres
Well, I found a way to create a VPN secure connection between the Oculus server and my local computer.

00:32:30 - Juan Torres
without having administrative permissions.

00:32:32 - Juan Torres
So what I did, I just simply downloaded the binaries for the tailscale VPN service inside the permanent, persistent file system within the computer through their servers.

00:32:48 - Juan Torres
And through that, now I'm able to use Winserve and agentic IDE on the server without having to go through the barbaric primitive use of BS code.

00:32:59 - Juan Torres
Stop행ing we'd know.

00:33:00 - Brandon Hancock
Andrew.D.: Dude, real fast, I don't know if you guys have had to do this, but I think Claw or Cursor the other day, for whatever reason, think two weeks ago, just broke, and I had to program the old way.

00:33:15 - Brandon Hancock
Guys, I felt like a toddler, learning how to walk for the first time.

00:33:20 - Brandon Hancock
I knew what I wanted to do, but I just haven't had to manually type out that amount of code in such a long time, so I was like, I'm done.

00:33:27 - Brandon Hancock
Like, I could spend the next three hours coding normally, or I could come back at the end of the day, hopefully it's crossed, and knock it all out in 20 minutes.

00:33:35 - Brandon Hancock
So I was like, forget this, but yeah, it's just, I don't know if y had that experience, but it's very humbling, very quickly, how addicted I am to this stuff.

00:33:43 - Brandon Hancock
So, but yeah, it just made me laugh when you said you're having to go old school.

00:33:48 - Juan Torres
So, so, oh, go ahead.

00:33:51 - Juan Torres
Yeah, technically speaking, I say, like, because they were going to charge him, like, seven, 7,500 for, you know, hiring, like, a good thing.

00:34:00 - Juan Torres
I of three to four developers.

00:34:04 - Juan Torres
I still have to make the API or URLs infrastructure in order to make the recall to whatever application or, you know, deployment method they're going to use.

00:34:16 - Juan Torres
But now that I have the connectivity issue resolved, I think that's going to be pretty easy.

00:34:21 - Juan Torres
That's awesome.

00:34:22 - Brandon Hancock
Well, congrats, man.

00:34:23 - Juan Torres
Yeah, and it was such, like, good attribution that even the owners of the servers, Oculus, they told me, hey, can you actually, like, come over and teach us how to do this?

00:34:35 - Juan Torres
Can you teach, like, our co-op members how to, like, make the connection to the Agentic ID?

00:34:42 - Juan Torres
I'd be happy to for a fee.

00:34:43 - Brandon Hancock
I hope that's what you said.

00:34:45 - Juan Torres
Hey, well, you know, if I can actually teach them how to do this, I can maybe get more clients that are actually in that server so I can basically, you know, expand with those individuals.

00:34:58 - Juan Torres
much, much, so, sort but question.

00:35:00 - Juan Torres
And then additionally to that, I was able to create an infrastructure also to be able to test the GPU LLAMP infrastructure.

00:35:11 - Juan Torres
So as you can see right there, I created like a quick dashboard that allows me to stress test the GPU and then be able to assess the token utilization of the model inside the virtual environment that I'm working in.

00:35:28 - Juan Torres
That's awesome.

00:35:29 - Juan Torres
this is going to help me facilitate the process of A-B testing several models, if that's what I want to do.

00:35:37 - Juan Torres
Quick question.

00:35:38 - Brandon Hancock
Yeah.

00:35:39 - Brandon Hancock
So I see NVIDIA A100, average throughput 72 tokens per second.

00:35:45 - Brandon Hancock
Dude, not going to lie, I would think that would hopefully be like 300.

00:35:50 - Brandon Hancock
Or is that because I'm confusing A100s and H100s?

00:35:57 - Juan Torres
For the token utilization, you mean?

00:35:59 - Brandon Hancock
Uh, throughput.

00:35:59 - Brandon Hancock
Siri sound.

00:35:59 - Brandon Hancock
Yeah.

00:35:59 - Brandon Hancock
Goingpi.

00:36:00 - Brandon Hancock
So it's, like, how many tokens per second can be processed?

00:36:03 - Brandon Hancock
Because I think, like, a MacBook could do, like, in the 20s.

00:36:08 - Juan Torres
I mean, the tests were based on prompts.

00:36:13 - Juan Torres
So the model that I'm using is, say, 8 billion parameter one.

00:36:17 - Juan Torres
So I guess the GPU could take even more, you know, heat if it wanted to.

00:36:26 - Juan Torres
But so far, the GPU inference of 8 billion parameters seems to be feasible, know, doesn't thermal throttle or anything like that.

00:36:35 - Juan Torres
Yeah.

00:36:36 - Brandon Hancock
Dude, you are in hardware land, and I respect it.

00:36:38 - Brandon Hancock
A little out of my wheelhouse, but that's awesome.

00:36:42 - Brandon Hancock
Dude, anything else we can help with?

00:36:44 - Brandon Hancock
It sounds like you're crushing it.

00:36:45 - Brandon Hancock
mean, these are the best kind of updates when things are going well.

00:36:47 - Brandon Hancock
So we're excited for you.

00:36:50 - Juan Torres
Yeah, just if anyone has information on developing an API, URL connection that I can use for the inference to the LLM.

00:36:59 - Juan Torres
Go.

00:36:59 - Juan Torres
Go.

00:36:59 - Juan Torres
Go.

00:37:00 - Juan Torres
You know, if anyone hears anything, let me know.

00:37:03 - Brandon Hancock
I mean, so like, just maybe this dumb question.

00:37:06 - Brandon Hancock
So my understanding, this is running in a private virtual network, correct?

00:37:12 - Brandon Hancock
And what we're trying to do is expose it to the outside world.

00:37:15 - Brandon Hancock
Is that what we're doing?

00:37:17 - Brandon Hancock
How are they running it?

00:37:18 - Juan Torres
Is it on premise right now?

00:37:20 - Brandon Hancock
Right?

00:37:20 - Brandon Hancock
It's all on prem?

00:37:23 - Juan Torres
Yeah, I am hypothesizing that they're using it in their own servers.

00:37:29 - Juan Torres
What's going to have to happen at one point is that they're going to deploy it Elastic Beanstalk or Vercel.

00:37:35 - Juan Torres
And the end users are going to make recalls that are going to make, you know, make inference calls directly to the LLM that has been hosted in the Oculus servers.

00:37:48 - Juan Torres
So there needs to be, of course, like a handshake, you know, handshake connection between the server that is hosting the application and then the server that is...

00:38:01 - Juan Torres
So I just need to make that bridge jump between both.

00:38:06 - Juan Torres
Yeah.

00:38:07 - Brandon Hancock
I don't think that will hopefully be too insanely hard.

00:38:10 - Brandon Hancock
Like, I think you will just set up almost like a proxy, like a secure proxy.

00:38:15 - Brandon Hancock
And all it does is it says like, hey, I'm receiving requests from the outside.

00:38:19 - Brandon Hancock
I do have a secure access to the private network.

00:38:23 - Brandon Hancock
And I need to make sure that the person is authenticated through some sort of API key.

00:38:29 - Brandon Hancock
That's generated.

00:38:31 - Brandon Hancock
Like, that's probably the simplest way is just to say like, hey, every person we want to use this gets an API key.

00:38:37 - Brandon Hancock
And then just in the header, we just say, do they have an API key?

00:38:41 - Brandon Hancock
Great.

00:38:42 - Brandon Hancock
This is now a valid request.

00:38:44 - Brandon Hancock
And go forth.

00:38:46 - Brandon Hancock
Could be oversimplifying it, but that could be a good starting point.

00:38:49 - Juan Torres
Yeah.

00:38:50 - Juan Torres
I mean, most likely it will not be divided per individual.

00:38:54 - Juan Torres
Because it will have to be, well, I mean, the authentication process of accessing.

00:38:59 - Juan Torres
a thing.

00:38:59 - Juan Torres
If want

00:39:00 - Juan Torres
The account, of course, is authenticated, but once you rent, there needs to be, in my, like, vision, it has to be generalized the access to LLM once they're authenticated into the application.

00:39:14 - Juan Torres
But I think, like, a URL method could resolve the issue.

00:39:19 - Juan Torres
It doesn't have to be specifically an API.

00:39:22 - Brandon Hancock
Dude, well, please keep us posted.

00:39:24 - Brandon Hancock
Yeah, I think I would love if next week, as you keep diving into this, if you have, like, a cool demo or, like, if you generate any, like, wireframes of, like, here's how you're setting it up, I think that could be a really cool, like, quick, hey, guys, and here, here's how I set this all up in five minutes, just, like, a quick wireframe overview.

00:39:41 - Brandon Hancock
I think that would be cool next week, if, if you get to it next week, but I think that would just be cool to see how it all works.

00:39:47 - Juan Torres
Yeah, I think a YouTube video on the, you stress testing of the LLM and the GPU could be really great.

00:39:54 - Juan Torres
It's great idea, too.

00:39:55 - Juan Torres
What I could do is, yeah, get credits if I'm going to do...

00:40:00 - Juan Torres
Like a presentation of this, get the server providers to give me credits to an 8100 GPU, and then from there reruns this whole thing on my own server, on my own computer, and then just record the whole process.

00:40:17 - Brandon Hancock
Dude, you know I am pro YouTube, so I absolutely love the idea.

00:40:20 - Brandon Hancock
hell yeah.

00:40:21 - Brandon Hancock
Dude, well awesome, please keep us in the loop, and yeah, if you end up recording that video, please send it over so I can watch it and hit like and subscribe, okay?

00:40:29 - Juan Torres
Thank you.

00:40:30 - Juan Torres
Perfect.

00:40:30 - Brandon Hancock
All right, Patrick, you're up next, man.

00:40:32 - Brandon Hancock
What is going on?

00:40:33 - Brandon Hancock
What cool prompts we working on?

00:40:35 - Brandon Hancock
Cool work stuff.

00:40:36 - Brandon Hancock
What's going on?

00:40:39 - Patrick Chouinard
Well, the last week I was a bit busy with other things, so I didn't have as much time as I want to work on my side project.

00:40:48 - Patrick Chouinard
But today, this brick just fell on me.

00:40:51 - Patrick Chouinard
It's an interesting scenario, but it just, it happened like half an hour before the call, so I was pretty happy that it was on the right day of the week.

00:40:59 - Patrick Chouinard
Nice.

00:40:59 - Patrick Chouinard
so I could

00:41:00 - Patrick Chouinard
Ask the right people.

00:41:01 - Patrick Chouinard
Hey, that's what we're here for.

00:41:03 - Patrick Chouinard
But yeah, the main thing I've been working because before they asked me that, I was already working with the business to integrate MCP integration in tools.

00:41:14 - Patrick Chouinard
And I was working on vibe coding, but experience of vibe coding in a corporate environment using Visual Studio.

00:41:23 - Patrick Chouinard
So it was still in VS Code environment, so somebody that has a bit of a background.

00:41:28 - Patrick Chouinard
But now, today, they just flip the script and say, oh, you have the budget you need, just tell us which tool to buy and go.

00:41:35 - Patrick Chouinard
It's like, okay.

00:41:38 - Patrick Chouinard
Hey, that's nice.

00:41:41 - Patrick Chouinard
Yeah, let's just say I'm used to be on the other side of trying to convince them to spend money.

00:41:46 - Patrick Chouinard
It's something else to be on the side of, yes, I want to spend your money, but I want to spend it correctly so you don't regret it in three months, you know?

00:41:54 - Brandon Hancock
Right.

00:41:55 - Brandon Hancock
Yeah, what the heck was Patrick thinking?

00:41:56 - Brandon Hancock
Yeah, we want our money back.

00:41:59 - Brandon Hancock
Thank

00:42:00 - Brandon Hancock
Exactly.

00:42:01 - Patrick Chouinard
Too much enthusiasm is just as dangerous as not enough, let's say.

00:42:05 - Brandon Hancock
Can I give you a two-second background on how previous companies did applications?

00:42:13 - Brandon Hancock
So, used to work for the government, and the government actually has a process for allowing individuals, like government employees, to deploy applications that can be used by airmen.

00:42:26 - Brandon Hancock
So, anyone in the Air Force, basically.

00:42:29 - Brandon Hancock
And, long story short, their whole process actually revolved around making sure people used proper containers, and they did an insane amount of work in CICD pipelines.

00:42:41 - Brandon Hancock
That's actually where 80% of the magic was, to where the goal was, is if I make a CICD pipeline that has enough, you know, make sure people didn't leak environment variables, make sure people didn't do A, B, or C.

00:42:56 - Brandon Hancock
If you have enough checks in there, there, then...

00:43:00 - Brandon Hancock
The goal is to, like, the lowest denominator of a developer shouldn't be able to break something.

00:43:06 - Brandon Hancock
That was their standard.

00:43:08 - Brandon Hancock
So if it can get through this entire pipeline that we have set up and it deploys successfully, there's no issues, then we as a company or the government will review it and do one final co-check internally as a development team and allow them to ship.

00:43:23 - Brandon Hancock
But that was their way to where they focused on, like, if we create a pipeline that we certify, if you get through this, you're good.

00:43:30 - Brandon Hancock
It just cuts out a lot of the noise and sets standards.

00:43:36 - Brandon Hancock
So that's how the government approached it.

00:43:39 - Brandon Hancock
I can think about, they had a specific name for it.

00:43:45 - Brandon Hancock
I'll have to remember, this was like four or five years ago, or I'll have to remember what they did, but there was an actual name.

00:43:49 - Brandon Hancock
So you could probably, I think a lot of it's public, to be honest, but you could just steal a lot of inspiration from it and implement it in your own company.

00:43:58 - Brandon Hancock
But that's how others do

00:44:00 - Patrick Chouinard
I understand the concept, and I understand what I want to do, but the thing is, in those concepts is you have already experts, okay, that can implement those 10.

00:44:09 - Patrick Chouinard
That's you.

00:44:12 - Patrick Chouinard
Yeah, but it's a company with over 6,000 employees and over about 500 devs, so I'm not going be the lead for all of them at once.

00:44:22 - Patrick Chouinard
The idea is, I need the dev to be on board, because right now the dev are not using AI-assisted development tools as much, or they're using it to ask questions.

00:44:34 - Patrick Chouinard
They're not, they're very far from VibeCoding, and they're miles away from what you guys are doing.

00:44:40 - Patrick Chouinard
So I need to bring them up to speed so they can develop the specs and the instruction files and the templates to give to the VibeCoder.

00:44:50 - Patrick Chouinard
So the VibeCoder starts in an already supervised environment, if you want.

00:44:58 - Patrick Chouinard
Because right now...

00:45:00 - Patrick Chouinard
They just, the management is just like, oh, we want to start that, like, tomorrow.

00:45:04 - Patrick Chouinard
How can we start having Vibecoders tomorrow?

00:45:06 - Patrick Chouinard
Well, if you give a lovable to business user tomorrow, you're going to have application developed in a thousand tech stack, so.

00:45:16 - Brandon Hancock
Right, and I found the name of it, if you want to steal it, I'll send, I'll drop a screenshot in the chat.

00:45:26 - Brandon Hancock
But long story short, it's called Platform One, and then there's two things called, one is Party Bus, and another one is Big Bang.

00:45:33 - Brandon Hancock
Big Bang is the platform that has the CICD pipeline, and it talks about exactly how they set it up to solve the, like, every business has the exact same problem.

00:45:45 - Brandon Hancock
We have developers, everyone's trying to do different things, and the way they said it was like, no, you can make a Next.js app, you can make a certain type of, like, a Flask app.

00:45:55 - Brandon Hancock
Like, they had six templates.

00:45:57 - Brandon Hancock
These are the only allowable pipelines.

00:46:00 - Brandon Hancock
From template to pipeline to deployed app, these are the only six verticals we support, and if you follow one of these, we have instructions along the way to make sure you don't break stuff and accidentally do something you don't want.

00:46:12 - Brandon Hancock
It was a huge endeavor, though.

00:46:13 - Brandon Hancock
That's the only kicker.

00:46:15 - Brandon Hancock
But, you know, the government has tens or hundreds of thousands of employees, so they had to solve this at a huge scale.

00:46:20 - Brandon Hancock
But if you click on that, they actually have repositories that you could look at.

00:46:26 - Brandon Hancock
A lot of them, you don't have to be in the DoD to access, but other ones you do.

00:46:31 - Brandon Hancock
But just, I think it could be like, you could show up at work tomorrow and be like, guys, I have a plan.

00:46:36 - Brandon Hancock
Don't ask me how we got it, but I know what we're doing.

00:46:40 - Patrick Chouinard
The thing is just, I'm Canadian though, so for DoD documentation in the state might be a little bit difficult.

00:46:47 - Brandon Hancock
I gotcha.

00:46:48 - Brandon Hancock
Yeah, but yeah, hopefully that helps, and hopefully you can see what the government did.

00:46:54 - Brandon Hancock
Because like I said, they did a really good job documenting everything.

00:46:58 - Brandon Hancock
Like, I used to work in this religion.

00:47:00 - Patrick Chouinard
So I would recommend checking it out.

00:47:02 - Brandon Hancock
I will drop a, let me just drop the link, copy link.

00:47:07 - Brandon Hancock
So if you guys want to check it out, here's an awesome presentation.

00:47:12 - Brandon Hancock
And yeah, I can actually just share the whole chat.

00:47:15 - Brandon Hancock
One second.

00:47:16 - Brandon Hancock
Paul, I saw you had your hand up.

00:47:18 - Brandon Hancock
If you want to hop on in.

00:47:21 - Paul Miller
Ian, it's an interesting challenge.

00:47:23 - Paul Miller
And having worked for, in a previous life, for quite a few very large corporates from Ernst & Young reporting to New York and Suntory.

00:47:36 - Paul Miller
It's, I can understand.

00:47:38 - Paul Miller
So, so there's a, there's always been a bit of a trend.

00:47:41 - Paul Miller
If you look at companies like Eli Lilly or Google itself, where they go and say they want to get everyone, you know, vibe is the latest description, but coming up with these brilliant ideas, like you're a small business.

00:47:57 - Paul Miller
So use that innovation on a small business.

00:48:00 - Paul Miller
But then make it into an app, and then we all benefit from it.

00:48:04 - Paul Miller
And what I've seen with this, and I've been involved with many of these programs, and one of the most successful methodologies that I saw is more, instead of getting, stressing out your poor dev teams, get your business analysts, your SA's, so they sit as those customer-facing resources.

00:48:28 - Paul Miller
So you could do like a Dragon's Den pitch, where you consolidate down the list of vibe, of cool vibe projects.

00:48:37 - Paul Miller
So get some outside facilitators, colored bean bags, go to a cool zone, get in the zone with the business guys, and saying, hey, what would be some really cool things?

00:48:49 - Paul Miller
Facilitate the ideas, facilitate get it to a shortlist, and then assign a group of BA essays to help.

00:48:59 - Paul Miller
down ground.

00:49:00 - Paul Miller
Hone it, but at the same time have some, then you can target which web services or APIs or concentrated stuff that you want to make available for those guys, because the biggest issue from a corporate level that your business is looking at is they want the pace, they want to have the best of what's going on, but you think of that funnel of content coming to your poor dev team, I know you want them to blim and code a bit better.

00:49:30 - Paul Miller
Hone use some tools, but jeepers, that's like anarchy land, but your BASAs, they've got to be able to temper this because one of the biggest issues, and it's not a new thing, is this whole where the users go off and they create some spreadsheet or they build some app on something and then suddenly a whole department is running on this thing and you're getting your tech stack.

00:49:59 - Paul Miller
Hone it, it, Hone

00:50:00 - Paul Miller
Is being diverted, and the business needs to work at the rate that the business needs to work at, but it can be facilitated, it can be focused, and it can be managed.

00:50:11 - Patrick Chouinard
Absolutely.

00:50:12 - Patrick Chouinard
It's just that normally the BA and the PO always use the, yeah, but it's not in the budget.

00:50:19 - Paul Miller
This time it's like open budget, do whatever you want and go for it.

00:50:22 - Patrick Chouinard
like, okay, how do I temper the business not to basically spend stuff that it's not going to come back as value?

00:50:31 - Patrick Chouinard
They're not going to have any ROI if they do it the way they're trying to do it right now.

00:50:36 - Paul Miller
So it's really rare you tell the business, don't spend money.

00:50:39 - Paul Miller
Oh, no, no.

00:50:40 - Paul Miller
Look, it's a wonderful opportunity.

00:50:42 - Paul Miller
And for me, it's sprung board.

00:50:44 - Paul Miller
My base day job came out of exactly that workshop.

00:50:49 - Paul Miller
The business said, we want to change the game and what we do in the field, and we need a tool to drive it.

00:50:55 - Paul Miller
And then we all got a group together, but the business needs to sit.

00:51:00 - Paul Miller
And like do a, they call it Dragon's Den in the UK, what's the?

00:51:07 - Patrick Chouinard
Shark Tank.

00:51:08 - Brandon Hancock
Shark Tank.

00:51:09 - Paul Miller
So do a Shark Tank, and you have these groups coming up, they've gone and sat on their coloured beanbags, they've come in and they're pitching these ideas, and they've got the screenshots, and then you tell the Shark Tank guys, here's the criteria, is it going to increase that?

00:51:29 - Paul Miller
Shark we've got all the money, but we're going to put the money in, is it going to increase sales, is it going to save time, save money, whatever, then that gets the shortlist.

00:51:39 - Paul Miller
Then you can do what Brandon's talking about in terms of building that framework, because you wouldn't want to build it for the whole Bloomin' stack that you've got.

00:51:51 - Brandon Hancock
Yep.

00:51:52 - Brandon Hancock
Any final things we can help with Patrick?

00:51:53 - Brandon Hancock
know it's easy for us to, I know you're in the thick of it, so that's the hardest part.

00:51:58 - Brandon Hancock
But it's, you obviously have way more

00:52:00 - Brandon Hancock
More context than we do, but no, Paul brought up a ton of awesome points, but hopefully something was helpful.

00:52:06 - Patrick Chouinard
Done.

00:52:07 - Patrick Chouinard
Believe me.

00:52:08 - Brandon Hancock
All right.

00:52:08 - Brandon Hancock
Perfect.

00:52:09 - Brandon Hancock
Speaking of, Paul, you're up next, man.

00:52:13 - Paul Miller
Well, I had two phone calls just then.

00:52:16 - Paul Miller
Customers dropping out of the sky that want to buy our product.

00:52:20 - Paul Miller
It's...

00:52:20 - Paul Miller
That's the best feeling ever.

00:52:22 - Brandon Hancock
It's taken nearly 10 years, but...

00:52:28 - Brandon Hancock
Overnight success.

00:52:32 - Paul Miller
Overnight success, 10 years in the making.

00:52:38 - Paul Miller
I'm not the best salesperson, but I just have to answer the phone and follow a script now, and my biggest focus at the moment is just looking at...

00:52:50 - Paul Miller
So I talked about last week, I do some little politics stuff on the side, and I set up a nice little N8N flow.

00:52:58 - Paul Miller
I can't demonstrate it just today.

00:52:59 - Paul Miller
was just

00:53:00 - Paul Miller
But it's going really well, I need to make my N8N flow cover for my calls.

00:53:07 - Paul Miller
So one of the best things that I've done was your recommendation on the Limitless device.

00:53:14 - Brandon Hancock
Heck yes, man.

00:53:15 - Paul Miller
Because I constantly get these blimmin', I constantly get these phone calls and I think at the end of the day, oh, I've got to write up this, I've got to do that proposal, I've got to do this thing.

00:53:26 - Paul Miller
I had this coffee meeting, had three coffee meetings yesterday, had to seriously get into the decaf because my mind would have blown up.

00:53:36 - Paul Miller
But I think my challenge is to focus on getting a practical process and a workflow with that.

00:53:46 - Paul Miller
We're going to hire a sales guy, but I need to be more productive.

00:53:50 - Paul Miller
And the junior sales person that's going to come on, they're going to need something to tap into to understand as well.

00:53:57 - Paul Miller
So that's kind of where...

00:54:00 - Paul Miller
Where I'm at, but yeah, Limitless.ai.

00:54:03 - Paul Miller
Tim It's real fast.

00:54:07 - Brandon Hancock
If you want to take that further, Bastion actually started playing with recently creating some developer tools around the API.

00:54:14 - Paul Miller
Tim would be cool.

00:54:18 - Brandon Hancock
Yeah, so like, I mean, setting up some workflows to automatically email a person on your team if certain things get said, like it's basically Limitless happens, then it records, classifies and delegates out to a team member.

00:54:28 - Brandon Hancock
Tim could 100% look at that.

00:54:31 - Brandon Hancock
It was a very quick setup.

00:54:33 - Brandon Hancock
Like they already have the APIs already hooked up.

00:54:35 - Brandon Hancock
It's just connecting it to N8N.

00:54:37 - Brandon Hancock
So, 100% do it.

00:54:38 - Brandon Hancock
The only gosh is, Paul, you can't say anything that'll get you fired, because it's listening to everything.

00:54:46 - Brandon Hancock
Tim don't accidentally send something to your secretary that was meant for your wife.

00:54:50 - Brandon Hancock
That's the only recommendation.

00:54:53 - Brandon Hancock
You smelled great today.

00:54:55 - Marc Juretus
Tim Cynova You smelled great today.

00:54:57 - Marc Juretus
Cynova Or I'm talking to the dog.

00:55:00 - Paul Miller
But it could be misconstrued.

00:55:01 - Paul Miller
Andrew That's so funny.

00:55:04 - Brandon Hancock
Andrew But yeah, that's awesome.

00:55:06 - Brandon Hancock
Congrats.

00:55:07 - Paul Miller
Look, I downloaded the ShipKit and watched the video.

00:55:14 - Paul Miller
Wow.

00:55:15 - Paul Miller
Wow.

00:55:15 - Paul Miller
I'm just so excited.

00:55:16 - Paul Miller
I've just got to create time to have a go at that.

00:55:20 - Paul Miller
I'm pretty excited.

00:55:21 - Paul Miller
I love what the ShipKit's all about, and I love the methodology and how you've concentrated it nicely into the product, so I'm excited about using that.

00:55:33 - Brandon Hancock
Andrew I would just like to add on to it, because I get pumped, because in my head, I have a thousand things I want to build, like Langchain.

00:55:40 - Brandon Hancock
We've talked about that.

00:55:40 - Brandon Hancock
What I want to follow it up with is a desktop course, because so many people are building desktop apps.

00:55:46 - Brandon Hancock
Whisper.

00:55:47 - Brandon Hancock
I mean, there's so many examples of a startup where all they do is just bring AI from the internet to your computer, and they just add a shortcut key to where you're instantly accessing AI.

00:55:57 - Brandon Hancock
So that paradigm is such

00:56:00 - Brandon Hancock
such an invaluable skill, so like those are the two that come to my head for the next upcoming ones to add to ShipKit, but yeah, they're just, there's so many cool, it's the coolest time to be alive, that's, I wish I didn't need to sleep, I'm the opposite of you, I am doubling down on coffee right now, I literally, non-stop, so it's the only way it's gonna get done, but afterwards, afterwards I will, I will cut back.

00:56:23 - Marc Juretus
What's the most cups you've had in a day, Brandon?

00:56:25 - Marc Juretus
I've actually, I don't know, the amount of nicotine and caffeine I've had in a day, the limit does not exist.

00:56:31 - Brandon Hancock
You smoke?

00:56:32 - Brandon Hancock
No, like little, little...

00:56:34 - Brandon Hancock
Oh, okay, I got you.

00:56:36 - Marc Juretus
Only European stuff, don't look like a smoker, though, man.

00:56:38 - Brandon Hancock
No, the, the European stuff is the good, is the good stuff, the, the American stuff makes me sick, so, but yeah, and it's so funny, I'm on the babiest limit, I, I call it, my, my friends and I, we, we refer to ourselves as, as  when it comes to, to nicotine, because we can't handle it, but, but we, we at least, uh, so we get the babies to mouth.

00:56:58 - Brandon Hancock
Uh.

00:56:59 - Brandon Hancock
Uh.

00:57:00 - Brandon Hancock
Yeah, caffeine, nicotine, and I could go forever.

00:57:02 - Brandon Hancock
That's the current, that's how ShipKit's getting built.

00:57:04 - Brandon Hancock
If you're curious of what it's fueled on, that is it.

00:57:08 - Brandon Hancock
So.

00:57:09 - Brandon Hancock
Next up, Adderall.

00:57:11 - Marc Juretus
I draw the line there, but everything else, I will do.

00:57:15 - Brandon Hancock
I think I'd get addicted.

00:57:17 - Brandon Hancock
But yeah, Paul, but I do want to go back to what you're saying, though.

00:57:20 - Brandon Hancock
Seriously, congrats on the customers.

00:57:21 - Brandon Hancock
I know, I mean, I just like, main thing I want to double click on is like, you've put in so much work for so long.

00:57:27 - Brandon Hancock
And it's just, it's like opportunity hits you in the, like, you just opened yourself to so many opportunities.

00:57:32 - Brandon Hancock
And I know some changes with your competitors, but now it's like officially happening of like, people are just, like you said, falling into your, falling into your lap.

00:57:39 - Brandon Hancock
So, right place, right time, but you just took a lot of hard work to get there.

00:57:43 - Brandon Hancock
So, awesome, man.

00:57:44 - Brandon Hancock
Really, really excited for you.

00:57:46 - Brandon Hancock
Fingers crossed on an exit.

00:57:47 - Brandon Hancock
Fingers crossed on an exit.

00:57:49 - Paul Miller
Next year, maybe.

00:57:51 - Paul Miller
Heck yeah.

00:57:52 - Brandon Hancock
Awesome.

00:57:52 - Brandon Hancock
All right.

00:57:53 - Brandon Hancock
Well, cool.

00:57:53 - Brandon Hancock
Well, thanks, Paul.

00:57:54 - Brandon Hancock
And it looks like next up is Tom.

00:57:58 - Brandon Hancock
Very nature-esque.

00:58:00 - Brandon Hancock
Today, very zen.

00:58:02 - Tom Welsh
I've got an how that got there.

00:58:06 - Tom Welsh
It's just, it's there.

00:58:08 - Tom Welsh
Hey, set in the mood.

00:58:09 - Brandon Hancock
But what's going on in Tomland?

00:58:12 - Tom Welsh
I just want to reiterate what Paul was saying about ShipKit.

00:58:15 - Tom Welsh
Yeah, absolutely awesome.

00:58:16 - Tom Welsh
I obviously signed up for it, downloaded it.

00:58:19 - Tom Welsh
I've already pulled all the rules across and thrown it into my asset management thing.

00:58:25 - Tom Welsh
Ran it, say, checked my code out.

00:58:26 - Tom Welsh
was 95% compliant.

00:58:28 - Tom Welsh
I thought, yeah, I'm happy with that.

00:58:30 - Tom Welsh
Hey, that's pretty good.

00:58:31 - Tom Welsh
doing?

00:58:31 - Brandon Hancock
Yeah, I was most impressed.

00:58:34 - Tom Welsh
And in fact, I found lots of those N's.

00:58:36 - Tom Welsh
I love your NEMDC.

00:58:37 - Tom Welsh
I've got that written elsewhere, but just wasn't picking up properly.

00:58:41 - Tom Welsh
But yeah.

00:58:42 - Tom Welsh
So yeah, I really look forward to the course.

00:58:45 - Tom Welsh
Thanks, Tom.

00:58:46 - Brandon Hancock
I appreciate it.

00:58:47 - Tom Welsh
Just basically just playing with it.

00:58:48 - Tom Welsh
So on the asset management side, I'm now, having played with it and had my mad moment with it, but I'm now trying to turn it into a product.

00:58:59 - Tom Welsh
Congrats.

00:58:59 - Tom Welsh
Regress.

00:59:00 - Tom Welsh
With multi-tenant and, oh, that's the enterprise, so stand-alone database or shared databases, basically, backends.

00:59:09 - Tom Welsh
So yeah, I'm just trying to extract myself from where I was and get some current settings set up so you can actually define as you set up and go in.

00:59:17 - Tom Welsh
A like, I would say, a web admin type interface to set up your database and everything.

00:59:23 - Tom Welsh
But yeah.

00:59:23 - Tom Welsh
So out of curiosity, are you setting up a database per organization?

00:59:27 - Brandon Hancock
Like, is that what you're working towards eventually, or...?

00:59:31 - Tom Welsh
I'm going to do database per organization for enterprise.

00:59:35 - Tom Welsh
I'm going to do shared multi-tenant shared database for cheaper versions.

00:59:44 - Tom Welsh
Okay.

00:59:45 - Brandon Hancock
No, I mean, I think that's a really cool idea.

00:59:48 - Tom Welsh
And my security head's going, I don't like shared databases.

00:59:52 - Tom Welsh
Data leaks.

00:59:53 - Tom Welsh
Right.

00:59:54 - Brandon Hancock
I can see Paul Grimace already.

00:59:56 - Tom Welsh
What's wrong with giving you data to see competitors, Paul?

00:59:59 - Tom Welsh
Paul...

00:59:59 - Tom Welsh
She's got deal.

00:59:59 - Tom Welsh
got a deal.

00:59:59 - Tom Welsh
She's got a deal.

00:59:59 - Tom Welsh
Thank

01:00:00 - Tom Welsh
Yeah, what could go wrong?

01:00:01 - Brandon Hancock
What could go wrong?

01:00:02 - Tom Welsh
Yeah, what could possibly go wrong?

01:00:04 - Brandon Hancock
Yeah, I mean, good and bad.

01:00:07 - Brandon Hancock
mean, if you look at most recent big leaks that you see that get talked about, they're usually using Firebase.

01:00:15 - Brandon Hancock
When they were using Firebase, that rule that Mitch was just showcasing the unsecured, it's because they literally have a Firebase client that can technically, the second it has the right key, access the entire database.

01:00:27 - Brandon Hancock
And all it takes is a developer who knows, oh, I can see they're making a request to this URL, great, I can now get anything.

01:00:35 - Brandon Hancock
Like, that's all it takes.

01:00:36 - Brandon Hancock
So, if you just don't use Firebase and boom, you automatically have prevented a lot of heartache.

01:00:42 - Brandon Hancock
then, I mean, if just stick to normal authorization and authentication, most stuff is pretty straightforward of like, at least just from what I've seen of just like, is the user ID that's making the request match the user ID of the field they're trying to Yeah.

01:00:58 - Brandon Hancock
Yeah.

01:00:59 - Tom Welsh
Yeah.

01:00:59 - Tom Welsh
Yeah.

01:01:00 - Brandon Hancock
And I think you're already doing a lot of that, so I think, oh, you know.

01:01:02 - Tom Welsh
Yeah, that's right, so I was looking at the role level security, well, I wasn't looking, I've heard about the role level security on Supabase, but I haven't really dug into that much.

01:01:10 - Tom Welsh
But I take you, that's just literally, you're authorized to run that query against that part of the database and that part only, so you don't get information slippage.

01:01:19 - Tom Welsh
Yeah, and it's strictly when you're using the Supabase client to access the database.

01:01:24 - Tom Welsh
Right.

01:01:25 - Tom Welsh
And I think you're using Drizzle, which- am, I am.

01:01:29 - Tom Welsh
So it doesn't work.

01:01:29 - Brandon Hancock
you're doing, literally, I mean, these are two different universes, like, so you're, like I said, I wish there was a button to just say, stop bothering me about this, but, you know, I guess they don't want to get on the news like Firebase for people leaking stuff, so I guess it's a catch-all.

01:01:45 - Brandon Hancock
Yeah, cool.

01:01:47 - Tom Welsh
Yeah, that's what I'm up to.

01:01:48 - Tom Welsh
That's awesome.

01:01:49 - Brandon Hancock
Well, hey, if I can help out with anything on that, please let me know.

01:01:52 - Brandon Hancock
Also, mean, I mean, you were setting yourself up, like, here's a few things that I see so valuable about this, like, A, enterprise, so you're starting.

01:02:00 - Brandon Hancock
Solving rich people's problems, so literally the exact same app doing the exact same thing, just hosted for a big customer, you're at a zero, you know, to whatever you were going to do, so like, I absolutely love what you're going, and I'm just going to say it, like, it's quote unquote a boring market, you know, like, most people are like, AI video shorts and all this other stuff, and like, we're, everyone's looking left, and I think you're looking right, and I think this, yeah, I just get very excited about, it checks all the good boxes for really good ideas.

01:02:30 - Brandon Hancock
So, very excited.

01:02:31 - Brandon Hancock
Would love, at some point next week, if you could do a, if it's possible, to do a demo of all the cool changes you've made.

01:02:37 - Brandon Hancock
Would love to see what the updated version looks like.

01:02:40 - Brandon Hancock
I'd like to say I've done lots of cool changes, but I haven't.

01:02:42 - Tom Welsh
done a little bit on the Mac, and the majority of stuff's just writing stuff down as the thoughts come in.

01:02:47 - Tom Welsh
And then, I've had a, I've a bit of a hiatus on the coding side for the past two weeks.

01:02:53 - Tom Welsh
Something to do with moving house, I think, has got a lot to do with it.

01:02:58 - Brandon Hancock
Yeah, they're going to take up all your time.

01:03:00 - Brandon Hancock
Well, hey, well, the second you get back to coding, we'd love to see an update.

01:03:03 - Tom Welsh
definitely.

01:03:05 - Tom Welsh
All right.

01:03:05 - Brandon Hancock
Perfect.

01:03:06 - Brandon Hancock
And namaste to in your natural grass habitat, man.

01:03:10 - Brandon Hancock
Thanks.

01:03:11 - Tom Welsh
The grass habitat's gonna become big now, I think.

01:03:14 - Tom Welsh
I love it.

01:03:15 - Tom Welsh
All right.

01:03:16 - Brandon Hancock
Perfect.

01:03:17 - Brandon Hancock
Cheers, Bye.

01:03:18 - Tom Welsh
Cheers, man.

01:03:20 - Brandon Hancock
Ola, probably butchered that.

01:03:22 - Brandon Hancock
You're up next, buddy.

01:03:23 - Brandon Hancock
And please correct me.

01:03:27 - Ola Oyo
Hey, Brandon.

01:03:29 - Ola Oyo
No, that's fine.

01:03:30 - Ola Oyo
Ola is fine.

01:03:31 - Ola Oyo
Not a problem.

01:03:33 - Brandon Hancock
I feel like I was saying, hey, you know?

01:03:35 - Brandon Hancock
So, like, hola.

01:03:37 - Ola Oyo
Yeah, a lot of people go, like, hola, hola.

01:03:39 - Ola Oyo
Like, okay, yeah.

01:03:41 - Brandon Hancock
Yeah, so you probably get that a lot.

01:03:43 - Brandon Hancock
But, hey, dude, welcome to the call.

01:03:45 - Brandon Hancock
How can we help out?

01:03:47 - Ola Oyo
Yeah, thanks, Brandon.

01:03:48 - Ola Oyo
I went to bed one night trying to figure out how I was going to integrate ADKs into my Django app.

01:03:55 - Ola Oyo
I wake up the next morning and then YouTube suggested you.

01:03:58 - Ola Oyo
I'm like, yes.

01:03:59 - Ola Oyo
I'm I'm

01:04:00 - Ola Oyo
So, yes, it was meant to be.

01:04:03 - Ola Oyo
So I took most of last week, I dug into the ADK kit course.

01:04:10 - Ola Oyo
It was very helpful.

01:04:12 - Ola Oyo
But I think I have come to a bit of a snag.

01:04:15 - Ola Oyo
So I'm building a property management platform for estate managers, and I'm trying to integrate the aspect into it to be context aware.

01:04:28 - Ola Oyo
Okay.

01:04:29 - Ola Oyo
The service is running on Django, and I had spent a large part of last week trying to run it as a separate service.

01:04:37 - Ola Oyo
But looking at a bunch of Medium posts, they just said that, look, it's better to integrate the ADK directly in Django.

01:04:44 - Ola Oyo
So I've kind of done that, and I'm trying to like figure out, following the same ADK structure, just how to get the ADK to run in my Django application and also be context aware.

01:04:58 - Ola Oyo
of, you know, just like you guys were talking about.

01:05:00 - Ola Oyo
I'm talking user ID, picking up the right information from my progress table so that when the user hits that end point, they're also able to get context aware data that's coming back.

01:05:14 - Ola Oyo
In fact, just before this call, I've been battling with GCP, tried to get my Vertex AI to work locally within my Docker container, and then I was also just trying to get the API key.

01:05:27 - Ola Oyo
I said, know what, to hell with Vertex.

01:05:29 - Ola Oyo
I'm just going to get the API key directly.

01:05:31 - Ola Oyo
And then because I'm using my organization, Google Workspace is giving me a whole bunch of challenges, you know, policy not allowed, blah, blah, blah.

01:05:41 - Ola Oyo
So, I mean, those are the major headaches I'm kind of like having now.

01:05:44 - Ola Oyo
How do I make my AD context aware to fit into my Django application?

01:05:49 - Brandon Hancock
Okay, perfect.

01:05:50 - Brandon Hancock
So let me share screen.

01:05:51 - Brandon Hancock
I have a few quick questions to make sure we're on the same page.

01:05:53 - Brandon Hancock
Okay, so are you trying to do like option one?

01:05:59 - Brandon Hancock
information?

01:05:59 - Brandon Hancock
Okay.

01:05:59 - Brandon Hancock
Let's Just Thank

01:06:00 - Brandon Hancock
Where you have like, Django run, like you have ADK running on port 8001, Django is making a request to port 8001, and then ADK is sending back a response?

01:06:13 - Brandon Hancock
Or are you saying, I'm not doing that, I'm actually like, in my Django application, I'm trying to have the entire ADK experience run?

01:06:27 - Brandon Hancock
Which route are we going?

01:06:29 - Brandon Hancock
Or do you care?

01:06:30 - Brandon Hancock
Or are looking for advice?

01:06:32 - Ola Oyo
So it's the lots are actually, so I'm trying to have the ADK run directly in the Django application.

01:06:39 - Ola Oyo
Okay.

01:06:40 - Brandon Hancock
Okay.

01:06:40 - Brandon Hancock
And just out of curiosity, for simplicity, is that, I know you said you saw some Medium posts that recommended it.

01:06:50 - Brandon Hancock
Did they dive into why?

01:06:52 - Brandon Hancock
I would just be curious to hear some, a little bit more background, potentially.

01:06:56 - Brandon Hancock
Yeah.

01:06:57 - Ola Oyo
So they didn't dive specifically into why.

01:06:59 - Ola Oyo
So

01:07:00 - Ola Oyo
But while I was trying to run the ADK separately, like you've drawn it here, the problems I had were authentication and having to sort of recreate all of my ORM and Django on the ADK again, just so that the ADK is context aware of the specific user and the information it should be getting from the table.

01:07:22 - Ola Oyo
So even that was just too much of a headache, and then it was like, okay, after doing a bit of research, was like, just have your ADK sit directly inside Django, it just makes it easier.

01:07:33 - Ola Oyo
Okay.

01:07:34 - Brandon Hancock
Yeah.

01:07:34 - Brandon Hancock
So, yeah, I mean, both ways should work.

01:07:40 - Brandon Hancock
I will say I have more experience with this one.

01:07:43 - Brandon Hancock
And the quick answer to solve the context issue is when you're actually creating sessions in ADK, you can actually set initial state for user, user ID for whatever.

01:08:00 - Brandon Hancock
So you want upon creating the session.

01:08:03 - Brandon Hancock
So that is how I usually work around that.

01:08:07 - Brandon Hancock
So I'll create a session, I'm user ID, his name is Bob, here's the, you know, whatever else you want.

01:08:14 - Brandon Hancock
Then whenever you start sending in messages, you know, you pass everything in as, you know, like you're working for user, username, like greet, you know, make sure you greet the person, you know?

01:08:28 - Brandon Hancock
So that's how most of the time I've gone about it.

01:08:32 - Brandon Hancock
And then what's nice about it is then it's, you know, you're just getting back stuff in, you know, server-side events.

01:08:39 - Brandon Hancock
Now, with that being said, streaming right now with ADK is very weird.

01:08:48 - Brandon Hancock
So out of curiosity, are you trying to use, are you trying to use ADK as a chat application or like a workflow to where it's automating three steps in a row and spitting back a result?

01:08:58 - Brandon Hancock
Which, which, which, which.

01:09:01 - Ola Oyo
So I'm trying to use it for two things, as a chat application, and then also to be able to take actions.

01:09:09 - Ola Oyo
So like, say for example, a user wants to update a property listing through chatting directly with the ADK.

01:09:19 - Ola Oyo
You know, if it says, hey, you know, update XYZ building, then, you know, the ADK should know, okay, this endpoint exists to update based on this ID for this building, and that's the authentication, and be able to do that.

01:09:32 - Ola Oyo
So it's kind of like, you know, both where it's, you know, seamless.

01:09:36 - Ola Oyo
You can just chat with the ADK, and it does everything, and it's also context-aware.

01:09:40 - Ola Oyo
Because it can connect directly with the ADK.

01:09:43 - Ola Oyo
I gotcha.

01:09:44 - Brandon Hancock
Yeah, so this, I mean, I guess, whether you host it over here, or you run it locally here, the same, you're going to have to do the exact same thing.

01:09:54 - Brandon Hancock
It just, the only thing that's going to change is, are you getting stuff back in an API?

01:09:59 - Brandon Hancock
I record-

01:10:00 - Brandon Hancock
Will a server-side events, or are you getting it, or are you using the ADK library?

01:10:04 - Brandon Hancock
So let me just show you something really fast, so agent, I think we'll go here.

01:10:12 - Brandon Hancock
So for example, if you are using, let's see, there's a quick one, let me check something really fast.

01:10:28 - Brandon Hancock
But there's a few examples of showing how to run it, I think it's in here, I just want to find it real fast, so I'm not pointing you astray.

01:10:42 - Brandon Hancock
So the cool part is, is if you are hosting it inside of your Django application, you never have to worry about anything with deployment, because it's in your Django app, you know?

01:10:54 - Brandon Hancock
So you literally just have to call the root-agent.run, and that's what...

01:11:00 - Brandon Hancock
That's I was trying to find for you really fast, because that's the part that's going to be super nice, like you're going to create a session, and once you have a session, you're going to just be able to call this, like this is as far as you have to go, because you're hosting ADK inside of your application, like you don't have to handle these events then to start to stream out through an API call back to your Django app, like you literally just have to do this, so definitely see the simplicity in keeping it inside, so yeah, yeah, I actually, after talking to it more, I really like this approach, instead of deploying it.

01:11:42 - Brandon Hancock
So, questions, I know I've covered a few different things, what is, is there a specific issue that I could help with, calling it out, I'd be happy to like pull it to the right spot maybe, or share some like ideas or anything.

01:11:56 - Ola Oyo
I mean, I guess, two of the many issues I'm having right now is...

01:12:00 - Ola Oyo
One, being able to even connect to the model.

01:12:05 - Ola Oyo
Again, because I'm testing this locally on Docker, I tried two methods.

01:12:12 - Ola Oyo
One was logging in directly, using my ADC to Google Cloud, having a vertex as one or true, and then logging in and trying to have those credentials sit directly in my Docker container.

01:12:27 - Ola Oyo
That didn't work.

01:12:29 - Ola Oyo
Next I tried was going directly to, I think it's the App Engine, is it?

01:12:35 - Ola Oyo
Yeah.

01:12:36 - Ola Oyo
Yeah, Google AI Studio, and grabbing the API key.

01:12:40 - Ola Oyo
That has also given me an error based on my organizational policies for Workspace.

01:12:46 - Ola Oyo
Again, I'm the only one using Google Workspace because it's by companies.

01:12:49 - Ola Oyo
It's a bit weird.

01:12:51 - Brandon Hancock
Let me just share real fast the quick way to do it.

01:12:55 - Brandon Hancock
So you'll do the fastest way to get it up and working if you're not allowed.

01:13:00 - Brandon Hancock
So to do like the Google Cloud login, where you sync your local computer to, you know, the cloud, set the project, enable Vertex AI, the easiest way to get it working is, did they change this?

01:13:13 - Brandon Hancock
AI Studio.

01:13:17 - Brandon Hancock
Let's see if this works.

01:13:18 - Brandon Hancock
Yeah.

01:13:18 - Brandon Hancock
So the easiest way to get it up and working is to create in Google Cloud, so like GCP, you know, you'll create a project in Google Cloud, Google Cloud.

01:13:28 - Brandon Hancock
So yeah, you probably, you probably already done this.

01:13:31 - Brandon Hancock
Then you come in here, make sure you have billing set up.

01:13:35 - Brandon Hancock
And the second you have billing set up, you want to make sure your environment variables are set to Vertex equals false.

01:13:42 - Brandon Hancock
And then you paste in that Google API key.

01:13:46 - Brandon Hancock
That is the, but Vertex has to be equal to false for it to detect your API key.

01:13:52 - Ola Oyo
Yeah.

01:13:52 - Ola Oyo
Yeah.

01:13:53 - Ola Oyo
Yeah.

01:13:54 - Ola Oyo
yeah, that's, mean, that's, yeah.

01:13:55 - Ola Oyo
Yeah.

01:13:56 - Ola Oyo
So the current ishram gets in just trying to use the API key.

01:13:59 - Ola Oyo
and up.

01:13:59 - Ola Oyo
Thank so

01:14:00 - Ola Oyo
He's actually a policy error.

01:14:02 - Ola Oyo
So I have to go to my IAM and then my policies.

01:14:05 - Ola Oyo
And then I specifically gone to, this is called, it's the Vertex Gen AI, sorry, just one second.

01:14:20 - Ola Oyo
Yeah, so it's Vertex Gen AI, I'm trying to allow all models.

01:14:24 - Ola Oyo
I've given it about five, 10 minutes to propagate.

01:14:27 - Ola Oyo
And then I put in a line in there to actually allow all the AI Gen, all the Gen AI models, and I'm still guessing an error.

01:14:34 - Ola Oyo
Because I noticed, you know, on the YouTube videos, you did use a workspace email.

01:14:40 - Brandon Hancock
Yeah.

01:14:41 - Brandon Hancock
Yeah.

01:14:41 - Brandon Hancock
Yeah.

01:14:41 - Brandon Hancock
Everything's under.

01:14:42 - Brandon Hancock
Yeah.

01:14:43 - Ola Oyo
Did you have to do any policy changes or just.

01:14:47 - Brandon Hancock
Just enable Vertex AI and then it was good to go.

01:14:51 - Brandon Hancock
So.

01:14:51 - Brandon Hancock
Yeah.

01:14:52 - Ola Oyo
That's a head scratch.

01:14:52 - Ola Oyo
So I guess it's something I'm just going to have to sit down.

01:14:57 - Brandon Hancock
Hey, even if you make a personal account and put in $5.

01:14:59 - Brandon Hancock
two, one.

01:15:00 - Brandon Hancock
It will last you a very, very long time, so it might be worth just to get around the headache, the $5.

01:15:06 - Ola Oyo
Yeah, I'm considering that, actually.

01:15:10 - Ola Oyo
But yeah, that's my headache for the week, and that's why I'm here.

01:15:18 - Brandon Hancock
Well, hey, well, please keep me posted if it keeps giving you issues, but yeah, that's just very weird.

01:15:23 - Brandon Hancock
And please keep me posted, too, on the, like, adding it inside Django.

01:15:27 - Brandon Hancock
That's going to save, because you're already in Python land, you literally, like you just saw in running it, it's just going to be, you know, the, once you create the session, you're just going to call run, and as events come back, you're just going to add them to your application.

01:15:42 - Brandon Hancock
So that's going to work, that's going to make your life so much easier.

01:15:43 - Brandon Hancock
No deployment.

01:15:44 - Brandon Hancock
That's the, that's the best part.

01:15:46 - Ola Oyo
Yeah, I will check that out.

01:15:48 - Ola Oyo
Do you have, by any chance, any videos coming out on like ADK and Django integration anytime soon?

01:15:55 - Brandon Hancock
So I'm not that much of a Django man.

01:15:59 - Ola Oyo
I'm more

01:16:00 - Brandon Hancock
Or Next.js, so I'm of the camp of having to go Next.js, reaches out to port 8001, get back an answer, and add it back to the Next.js application.

01:16:10 - Brandon Hancock
So yeah, not much Django.

01:16:14 - Brandon Hancock
It was the first one I learned, though.

01:16:16 - Brandon Hancock
It was like the first full-stack framework.

01:16:17 - Ola Oyo
So, but that was a minute ago.

01:16:20 - Brandon Hancock
So I'm very, yeah, I know some of the core concepts, but oh God, I'm rusty.

01:16:24 - Brandon Hancock
Like 2015, so a decade ago.

01:16:25 - Brandon Hancock
So, I'm very rusty.

01:16:29 - Brandon Hancock
So, yeah.

01:16:31 - Brandon Hancock
But yeah, thanks a lot.

01:16:33 - Ola Oyo
And you know, real great work on what you've done on ADK, because I went through the Google modules, and they're nowhere close to what it is you put out, to be honest.

01:16:44 - Ola Oyo
So they should be paying you.

01:16:46 - Brandon Hancock
Hey, let me screenshot this and send it to them.

01:16:50 - Brandon Hancock
That's what I need to do.

01:16:50 - Brandon Hancock
I'd love a Google paycheck.

01:16:53 - Brandon Hancock
I would love one of those.

01:16:54 - Brandon Hancock
So, it's nothing yet, but hey, one day maybe.

01:16:58 - Brandon Hancock
perfect.

01:16:58 - Brandon Hancock
Hey, good luck on all things Django.

01:17:00 - Brandon Hancock
Please keep us posted.

01:17:01 - Brandon Hancock
We'd love to see any update next week, okay?

01:17:03 - Ola Oyo
Yeah, thanks a lot.

01:17:05 - Ola Oyo
I might be heading out soon.

01:17:06 - Ola Oyo
This is like past 12 of my time.

01:17:08 - Ola Oyo
So, but, you know, great piece in all.

01:17:09 - Brandon Hancock
Yeah, thanks.

01:17:10 - Ola Oyo
Awesome.

01:17:11 - Brandon Hancock
Perfect.

01:17:11 - Brandon Hancock
All right.

01:17:12 - Brandon Hancock
Well, great.

01:17:12 - Brandon Hancock
Prim, you're up next, man.

01:17:14 - Brandon Hancock
What awesome projects we working on.

01:17:15 - Prem
How can we help?

01:17:17 - Prem
Hey, Brandon.

01:17:18 - Prem
Good to see you back.

01:17:20 - Prem
So again, what I was showing you a project, I kind of, what I did was I want to kind of make it move from Vercel.

01:17:28 - Prem
I was using Vercel as the database and I moved it to Supabase.

01:17:32 - Prem
And I think some of the questions that were asked, you know, was kind of related to the same question.

01:17:37 - Prem
Again, I'm using Drizzlewarum.

01:17:40 - Prem
So, but then this, you know, the role level security is disabled, is a constant thing I get in Supabase.

01:17:47 - Prem
I assume like, you know, you kind of answered that question where as long as they're using, you know, Drizzlewarum and kind of how my APA endpoints kind of take care of the security, it should be fine.

01:17:58 - Prem
And so I just want to get your thoughts.

01:18:00 - Prem
Anything about moving from Vercel, you know, things to consider while moving from Vercel, Postgres, to Superbase, anything?

01:18:09 - Brandon Hancock
No, I mean, I mean, high level, I think, A, it's more affordable.

01:18:13 - Brandon Hancock
So I definitely like the call on making the move because you're hosting, like, Vercel, it was kind of disappointing.

01:18:21 - Brandon Hancock
They had a chance to, like, be the best option because, like, they had a chance to be the best.

01:18:27 - Brandon Hancock
I still use them religiously, but only for hosting the Next.js application.

01:18:33 - Brandon Hancock
But, like, their blob storage fees are pretty high at this point.

01:18:37 - Brandon Hancock
In beta, they were really cheap, but now they're out of beta.

01:18:40 - Brandon Hancock
It's pretty expensive.

01:18:42 - Brandon Hancock
And their database hours per month was very low, which made it a more expensive option.

01:18:49 - Brandon Hancock
So, no, I think you're going to love the Superbase experience much more.

01:18:53 - Brandon Hancock
Security risk, just to dive into that.

01:18:55 - Brandon Hancock
I mean, as long as you are doing, like, what we've talked about so far of, like...

01:19:00 - Brandon Hancock
I'm using Drizzle to make structured queries to my database.

01:19:04 - Brandon Hancock
And before that Drizzle command or query or mutation is sent off, A, is the person authenticated?

01:19:10 - Brandon Hancock
And B, are they authorized to make the request?

01:19:13 - Brandon Hancock
Like that is check, check.

01:19:14 - Brandon Hancock
You're great to go.

01:19:16 - Brandon Hancock
The main issue, and I could pull up a code snippet at some point, but like there's strictly like Supabase does allow you with your service account keys to actually make changes to the database.

01:19:26 - Brandon Hancock
And that's when you have to worry about real-level security.

01:19:29 - Brandon Hancock
You're not worrying about that.

01:19:31 - Brandon Hancock
Are you, out of curiosity though, are you doing any blob storage in Supabase?

01:19:35 - Prem
Uh, yes.

01:19:36 - Prem
Yeah, I was, uh, you one of the things I had problem with, uh, Versal initially was, you know, it did not have, private like blobs that can be stored up.

01:19:45 - Prem
So that was one of the problems and that's one of the reasons, again, to kind of move to Supabase, um, you know, um, because again, it did not have a good security model for the blob storage.

01:19:56 - Brandon Hancock
Yeah.

01:19:57 - Brandon Hancock
The, um, main thing I was going to say, when you are using Supabase,

01:20:00 - Brandon Hancock
DupaBase, there's a concept of pre-signed URLs, so before generating a pre-signed URL, you want to make sure the person asking to get the blob before you make the pre-signed URL is allowed to do it, but then you're good, because you're probably going to get some issues as well on the blobs, so they're just trying to cover, you know, it was a CYA, cover your , so, but you're good.

01:20:24 - Prem
I just have one other follow-up question in terms of using, and I started using Clerc, you know, for, you know, user authentication, or kind of basically user management, and I saw that Superbase is having, you know, user process well, and one of the things that I've found so far is Clerc has more like, you know, user and organization, like management, like let's say if you want to kind of have users and and organizations kind of, they have new features, so that's the reason I'm kind of sticking with Clerc.

01:21:00 - Prem
Do you have any inputs on that or like, you where you want to kind of have users and then organizations associated with that?

01:21:07 - Prem
Any thoughts on, you know, Supabase, using Supabase versus Clurk for user management?

01:21:13 - Brandon Hancock
Yeah, so Clurk is definitely adding a lot of, I can't remember if Clurk has added this in yet, or if I'm thinking of Auth0 or WorkOS, but they have it to where you can mock Bing users in the, like, if you came to me and you're like, dude, my app's not working.

01:21:29 - Brandon Hancock
Well, I think what, it's either WorkOS, it's one of them.

01:21:33 - Brandon Hancock
They allow you to sign in as your user and go throughout the application on their behalf, which is a pretty cool feature because you get to actually, like, log in and do stuff on your user behalf, which is, like, a really cool feature.

01:21:45 - Brandon Hancock
Now, with that being said, I'm a big fan of simplicity just because, like, what, I always ask myself, like, what is, are all the additional benefits worth the extra effort?

01:21:59 - Brandon Hancock
And, mean, most-

01:22:00 - Brandon Hancock
So time, really just want people to be able to log in, Supabase allows you to do the Google, GitHub, it allows you to do all of them, or you could actually add in Auth0 and WorkOS.

01:22:08 - Brandon Hancock
I think Supabase also has an integration for Clerk, to where you can actually hook up Clerk to work with Supabase.

01:22:17 - Brandon Hancock
Yeah, they actually have that too.

01:22:19 - Brandon Hancock
So, I mean, even if you do go with Clerk, that's also totally, you can still have it work.

01:22:26 - Brandon Hancock
But yeah, out of, you know, I don't, unless there's a specific feature that you're like, I have to have this, maybe the organizations.

01:22:34 - Brandon Hancock
That's the only one.

01:22:35 - Brandon Hancock
But isn't it pretty expensive for Clerk organizations?

01:22:37 - Brandon Hancock
Or am I, I can't remember what it ended up costing.

01:22:40 - Brandon Hancock
No, it's, it's not much again, for the organization piece.

01:22:45 - Prem
You know, again, it's kind of more in beta, the organization stuff in Clerk.

01:22:51 - Prem
So, but again, Supabase does not have it in, at least in their timeline right now.

01:22:57 - Prem
So, that's the reason.

01:22:58 - Prem
Again, that's one of the critical.

01:23:00 - Prem
The features I'm kind of looking for, for the application I'm trying to build.

01:23:03 - Prem
So that's why I'm probably, you know, you know, you're looking at the clerk as the primary option right now.

01:23:10 - Brandon Hancock
I, final recommendation, I've heard nothing but amazing feedback on WorkOS.

01:23:17 - Brandon Hancock
And I believe they already have like enterprise SSO set up.

01:23:21 - Brandon Hancock
They also, I assume also have organizations.

01:23:24 - Brandon Hancock
So before you make a pick, I would 100% look at setting that up, like doing a side-by-side.

01:23:32 - Brandon Hancock
It is more expensive.

01:23:33 - Brandon Hancock
It is more enterprise grade.

01:23:36 - Brandon Hancock
I just don't have enough background on the project or the end goal.

01:23:39 - Brandon Hancock
But WorkOS, if you are going to go for the big boys and like, no, I'm supporting this organization, they need to use what SAML and bring in all of their own people.

01:23:49 - Brandon Hancock
WorkOS is probably one of the best options if you're going to go down that path.

01:23:54 - Prem
Yeah.

01:23:55 - Prem
Yeah.

01:23:56 - Prem
Thanks a lot for that.

01:23:57 - Prem
Perfect.

01:23:59 - Prem
And.

01:24:02 - Brandon Hancock
And then if we want to go, Hamal, I saw you had your hand up as well.

01:24:11 - Hemal Shah
Yeah.

01:24:13 - Hemal Shah
There are two screenshots I think you put for the terms, Brandon, one on 605.

01:24:18 - Hemal Shah
I'm there on that screenshot.

01:24:20 - Hemal Shah
think Jaylen had the same mention in the chat.

01:24:22 - Hemal Shah
In the second screenshot, I am not there.

01:24:24 - Hemal Shah
Jaylen is calling it out.

01:24:27 - Hemal Shah
Well, thank you.

01:24:29 - Hemal Shah
Okay, perfect.

01:24:31 - Brandon Hancock
Yeah, well, we can go with the first one.

01:24:33 - Brandon Hancock
It's just sometimes people drop off, so it's hard to tell if they're still on the call.

01:24:37 - Brandon Hancock
But no, okay.

01:24:38 - Brandon Hancock
Yeah, we will.

01:24:39 - Brandon Hancock
Thank you for bringing that up.

01:24:41 - Brandon Hancock
Jaylen, if you're still here, buddy, you can, you're up next.

01:24:44 - Brandon Hancock
Yeah, there you are.

01:24:46 - Brandon Hancock
Are you ready?

01:24:48 - Jaylen.Davis
Of course, dude.

01:24:49 - Brandon Hancock
What's going on?

01:24:50 - Brandon Hancock
Any cool projects?

01:24:51 - Jaylen.Davis
How can we help?

01:24:52 - Jaylen.Davis
Yes, sir.

01:24:53 - Jaylen.Davis
So I spoke with you maybe a month and a half ago.

01:24:56 - Jaylen.Davis
Mitch has sent me a link to the Zoom meeting and I spoke with you.

01:25:00 - Brandon Hancock
I a platform that I was creating that you seem to really like.

01:25:02 - Brandon Hancock
It's called Topic Launch.

01:25:04 - Jaylen.Davis
I actually got it done.

01:25:07 - Jaylen.Davis
Back then I was still coding it, but I got it done and we just started, me and my business partner, we just started creating user-generated content on Instagram.

01:25:18 - Jaylen.Davis
That's was mostly just coming to let you know if you were interested in hopping on the platform.

01:25:23 - Jaylen.Davis
I actually even created an account for you.

01:25:27 - Brandon Hancock
Dude, so how can I, what URL do I go to?

01:25:30 - Jaylen.Davis
Let's look at this.

01:25:31 - Jaylen.Davis
Topiclaunch.com Okay, perfect.

01:25:36 - Brandon Hancock
So, I cannot remember, so was the goal, okay, it was funding, so it was fun topics for your favorite YouTubers.

01:25:43 - Jaylen.Davis
Yeah, so basically, YouTubers monetize their audience by fans funding content ideas for them.

01:25:49 - Jaylen.Davis
So, a fan creates the topic, the community, if the fan doesn't fund the topic to the fullest, the community backs the topic and then you deliver the video.

01:26:00 - Jaylen.Davis
So within 48 hours to receive 90% of the funding while topic launch takes 10%.

01:26:04 - Jaylen.Davis
Very simple and straight to the point.

01:26:07 - Jaylen.Davis
It saves you from running out of ideas and as well as creating videos based off of ideas that you thought were going to pop and they actually flopped.

01:26:14 - Brandon Hancock
Right.

01:26:16 - Brandon Hancock
And you get paid as well.

01:26:18 - Brandon Hancock
No, that is awesome.

01:26:20 - Brandon Hancock
I think this is a, I think this is a very, like I said, I was so pumped when you brought this up last time because like I do think this is, I think this is a very, really idea.

01:26:32 - Brandon Hancock
Um, so, I mean, big things like, I mean, I'll just say it from like the creator standpoint is like, even right now, if I was paid to make a video literally for the next like 25 days, I couldn't.

01:26:44 - Brandon Hancock
Cause

01:26:45 - Brandon Hancock
So mode, but if I was in YouTube mode, like this would be insanely, insanely, um, insanely helpful.

01:26:53 - Brandon Hancock
How, how does it work?

01:26:54 - Brandon Hancock
Just out of curiosity, or, and how can I be helpful?

01:26:57 - Brandon Hancock
Because is it like, um, oh, once a video reads a certain threshold of like 100 bucks, 200 bucks, or how does, I mean, I was just curious, like, what are you thinking for the app?

01:27:07 - Brandon Hancock
Because like, this is a, this is a real world, valid pain point.

01:27:11 - Jaylen.Davis
So basically, uh, you tell your fans, and then your fans go on, well, you create a, you create an account, but in the case of already creating an account, you tell your fans, like, look, um, you guys always want me, want me to make these different kinds of videos, um, so go on this website, if you really want me to make the video, pay for it, put your money where your mouth is, you basically tell them that.

01:27:34 - Jaylen.Davis
They go on the website, they create a topic, and they put in, they put the threshold, so, they would be guessing at how much you'd be willing to do the video for, but, um.

01:27:45 - Jaylen.Davis
It's more so kind of on you to tell them, like, look, I'd be willing to talk about this specific area for $400 or $800, whatever the case might be.

01:27:53 - Jaylen.Davis
And then they go on the website, they create the topic, they set it to your threshold, and they put in at least 10%.

01:27:59 - Jaylen.Davis
They can fund it all the way through if they want to, but at least 10% for it to go live for the community to come in and fund it to the threshold.

01:28:06 - Jaylen.Davis
Once it's funded, you're notified via email, and then you have 48 hours to create the video, and then you receive 90% of the funding.

01:28:13 - Brandon Hancock
Yeah, it's like Kickstarter, but for actual, like, YouTube content.

01:28:17 - Brandon Hancock
It's kind of like if I was to, like, say it in a nutshell.

01:28:20 - Brandon Hancock
No, this is, I absolutely love the idea.

01:28:22 - Brandon Hancock
I mean, I mean, like, main qualms and, like, main things that I would suggest is, like, the timeline part of, like, like, for, like, for example, like, the Django video.

01:28:34 - Brandon Hancock
Like, earlier it was just asked, like, do I do stuff on Django?

01:28:36 - Brandon Hancock
Like, it would be hard if I was asked, like, hey, for $400, make a Django video.

01:28:41 - Brandon Hancock
Like, that would take me...

01:28:45 - Brandon Hancock
Like, forever to spin back up on Django, then do it, so it's like, so I, like, serious feedback, because, like, if you don't do this, I would love to do this.

01:28:54 - Brandon Hancock
Dude, let me, as the creator, just pay 30 bucks a month, 40 bucks a month, whatever the number is, and just allow me to put idea topics out there, and community thumbs up, thumbs down, or community suggest their own videos and thumbs up, thumbs down.

01:29:09 - Brandon Hancock
Like, that is so much more valuable, because, like, there's some times where, like, even if I have a sponsorship deal or whatever, like, well, okay, for the next week, I'm busy working on that video.

01:29:20 - Brandon Hancock
Like, I legitimately could not take on another video, just with how time, timelines work, so, like, but just allowing the community to let me see, like, signal versus noise would be super helpful.

01:29:35 - Brandon Hancock
So, if you are, like, right now, I could not, like, I just couldn't, in good faith, sign up for the current one, just because, like, I, I wouldn't want to take people's money knowing I could not, most of the time, deliver on the

01:29:46 - Brandon Hancock
And I would hate to set false expectations of like, oh yeah, I'll make a video on anything.

01:29:50 - Brandon Hancock
Because that's the other thing, like, a lot of times people ask like, hey, can you make a video on this topic?

01:29:55 - Brandon Hancock
Hey, that's actually like my channel umbrella.

01:29:58 - Brandon Hancock
I don't really cover that topic.

01:29:59 - Brandon Hancock
So just being, you know, you're kind of forced to go in a direction you might not want.

01:30:04 - Brandon Hancock
So just letting it be pure thumbs up, thumbs down would be insanely helpful.

01:30:09 - Brandon Hancock
Um, and that, you know, you know, a creator $30 a month, you know, that's, that easily would pay for that.

01:30:17 - Brandon Hancock
Um, so hopefully, hopefully that makes, makes sense for feedback.

01:30:22 - Brandon Hancock
And, and hopefully the, the concerns also make sense too, um, just as a creator.

01:30:28 - Jaylen.Davis
So if, let's say I just so happen to eventually pivot to, to that, uh, basically the way of the, the website.

01:30:37 - Jaylen.Davis
Is there something that you would sign up for?

01:30:41 - Brandon Hancock
dude, give you 30 bucks right now.

01:30:42 - Brandon Hancock
Yeah.

01:30:43 - Brandon Hancock
Um, and then like also.

01:30:45 - Brandon Hancock
So seriously, A, obviously I'm going to pitch Shipkit, but for the landing page and everything, dude, Shipkit, cannot recommend it enough for, literally, you would just pass in the UI prompt, your landing page, between the UI prompt and the generate landing page prompt, this would be completely redone in two minutes, so if you're looking to just build faster, I really would recommend Shipkit, because, like, you have an idea, you have a very valuable idea, too, so now it's just building it out as fast as possible, so, like, really would look at, you know, I am going to pitch it for myself, but really would recommend to check it out, because, like, you have an idea, like, let's just make it look beautiful, let's get it out to the world fast, and go forth, so, yeah, would definitely recommend that.

01:31:39 - Brandon Hancock
Shipkit.ai, yeah.

01:31:41 - Jaylen.Davis
Shipkit.ai.

01:31:41 - Jaylen.Davis
Shipkit Shipkit Shipkit.ai.

01:31:44 - Brandon Hancock
Shipkit

01:31:46 - Jaylen.Davis
But yeah, seriously, I absolutely love this idea.

01:31:49 - Brandon Hancock
I could not say enough how helpful this would be because like right now, like internal dialogue, because, you know, we will, we're going to hop on to another second.

01:31:57 - Brandon Hancock
It's like, does the community right now, do they want a land graph video?

01:32:00 - Brandon Hancock
Do they want an ADK video?

01:32:02 - Brandon Hancock
Do they want to see a deeper dive into ADK?

01:32:05 - Brandon Hancock
Like as a developer or as a creator right now, like I have to guess, you know?

01:32:09 - Brandon Hancock
So like you literally take the guesswork out of content creation, which is beautiful, you know?

01:32:13 - Brandon Hancock
So, cause like right now I have to look at comments, then I have to, you know, there's so much work that goes into like getting a sense for what direction people want to go.

01:32:22 - Brandon Hancock
And this would just be like, no, I literally just look at the top two and I'm like, cool, I'm making video one today.

01:32:26 - Brandon Hancock
So yeah, hopefully, hopefully that makes sense.

01:32:29 - Jaylen.Davis
Yeah, that makes a lot of sense.

01:32:31 - Jaylen.Davis
Thank you.

01:32:32 - Brandon Hancock
All right, perfect, dude.

01:32:32 - Brandon Hancock
Well, keep, keep going.

01:32:33 - Brandon Hancock
This is, this is looking awesome.

01:32:35 - Brandon Hancock
I'm excited to see it, uh, come to, uh, come to life, man.

01:32:39 - Brandon Hancock
Um, perfect.

01:32:41 - Brandon Hancock
Um, and then, yeah, we're going to go back to the original order of the.

01:32:45 - Brandon Hancock
Yeah, so it looks like, let make sure I'm missing anybody, it looks like Jake was next, I think.

01:32:57 - Jake Maymar
Excellent, excellent.

01:32:59 - Jake Maymar
So first of all, the Shipkit is amazing.

01:33:03 - Jake Maymar
That is totally amazing.

01:33:05 - Jake Maymar
Like, I've already written so many things using it, it's insane.

01:33:11 - Jake Maymar
And I've also altered the prompts, because it's like such a good starting place.

01:33:18 - Jake Maymar
And I'm like, okay, I need to just tweak this, I need to tweak this.

01:33:21 - Jake Maymar
And I can't wait to really fully dive in, but yeah, it's fantastic.

01:33:26 - Jake Maymar
Yeah, and doing the one that does the website, it's insane.

01:33:30 - Jake Maymar
Ah, on that question, and this is, you know, I'm revisiting my website, which is, I have a love-hate relationship, and it's WordPress.

01:33:44 - Jake Maymar
You're so impressed.

01:33:45 - Jake Maymar
You.

01:33:45 - Jake Maymar
And I finally just decided I'm done, I'm just done with WordPress completely, switching completely to Next.js.

01:33:53 - Jake Maymar
I actually really like building things in it.

01:33:56 - Jake Maymar
And so I'm curious, what should I host?

01:33:59 - Jake Maymar
Because I've been looking at like Netify or Netlify.

01:34:07 - Jake Maymar
And I'm using SiteGround right now, but they don't really host Next.js.

01:34:15 - Jake Maymar
So I'm just kind of curious about the hosting side.

01:34:18 - Jake Maymar
I keep hearing about Hostinger.

01:34:20 - Jake Maymar
But yeah, is there any one you would recommend?

01:34:22 - Brandon Hancock
I mean, the easiest one, especially if you're hosting a single project, mean, Vercel, like you literally just say, deploy app, you point to your GitHub project and it's done.

01:34:33 - Brandon Hancock
Like it is insanely easy, how well it works.

01:34:36 - Brandon Hancock
And it, it actually does like the full process of like, distributing the application, because it understands, okay, this is Next.js code.

01:34:45 - Brandon Hancock
So.

01:34:45 - Brandon Hancock
Like, I can actually server-side render a lot of this stuff to make the static pages look better.

01:34:49 - Brandon Hancock
Like, there's so many benefits of using it.

01:34:51 - Brandon Hancock
So, big fan of Vercel.

01:34:53 - Brandon Hancock
And even if you went pro to get, like, a lot more of the additional features, it's $20 a month.

01:35:00 - Brandon Hancock
But if this is your first app, I mean, on the hobby tier, which is completely for free, you're gonna get everything that was just mentioned.

01:35:09 - Brandon Hancock
So, that's what I would use.

01:35:11 - Jake Maymar
But how do you do, like, cause I have, um, I have my own, like, uh, domain and email address and all that.

01:35:18 - Jake Maymar
That's not tied to Vercel.

01:35:20 - Jake Maymar
That would be just, that's, that's a different thing.

01:35:23 - Jake Maymar
Right?

01:35:23 - Brandon Hancock
And so I just have to show you real fast.

01:35:25 - Brandon Hancock
Um, so yeah, when it comes to, like, setting up your own domain, I'll just show you real fast.

01:35:29 - Brandon Hancock
Um, let make sure I'm not gonna accidentally do something that's gonna bite me.

01:35:35 - Brandon Hancock
Um, yeah, so like, this is as easy as it is to like, like, here was my default I ship kit application.

01:35:44 - Brandon Hancock
I added in.

01:35:45 - Brandon Hancock
.

01:35:45 - Brandon Hancock
.

01:35:45 - Brandon Hancock
.

01:35:46 - Brandon Hancock
And then it gave me a few commands to pass over to Namecheap where I bought the domain and then boom, like you're now using your own URL.

01:35:55 - Brandon Hancock
So like it was so easy to add that now on the side of like mail and stuff like that.

01:36:01 - Brandon Hancock
Yeah.

01:36:01 - Brandon Hancock
Like at that point, you're probably going to, if you already had the domain, you know, you could easily just with, you know, you'll create a Google business account and like set that up.

01:36:09 - Brandon Hancock
Um, I think it's like seven, $8 a month to get that business email.

01:36:13 - Brandon Hancock
So it's not bad either.

01:36:16 - Brandon Hancock
Um, and then if you want to get some automated emails sent out, Mailgun would be my default recommendation.

01:36:23 - Brandon Hancock
Very like it's been around forever.

01:36:25 - Brandon Hancock
Super standard, very reliable.

01:36:27 - Brandon Hancock
Obviously, if anyone else has any suggestions to all ears, cause I think this is a cool, a cool conversation.

01:36:31 - Brandon Hancock
But, um, yeah, does anyone else have any ideas or suggestions?

01:36:34 - Brandon Hancock
Just cause like this is the, this is the cool part and the hard part.

01:36:37 - Brandon Hancock
There's a thousand things you could do.

01:36:40 - Brandon Hancock
Yeah.

01:36:41 - Brandon Hancock
If anyone has any other strong opinions to, you know, I think the more the merrier.

01:36:44 - Brandon Hancock
And then.

01:36:45 - Jake Maymar
I have, I have, if there's any opinions, please, please let me know, but I have, I have another question about, okay, so I'm really excited about how this, these projects are going, and one of the things that I want to do, so I'm already using OAuth, I'm already, you're already signed in with LinkedIn, so it's, it's already there, I have your name, but the problem is, is LinkedIn LinkedIn doesn't, doesn't give you access to much, so if you're just using the default setting where you don't have, like, higher level permissions, you get name, and the, the title, and the image, that's it, that's all you get, and so what I want to do is, I actually want to get the profile information, and so I've been thinking about using, like, Serper, but it has to be GDPR, and so it has to only be public profile.

01:37:44 - Jake Maymar
profile.

01:37:45 - Jake Maymar
I'm just curious if you're, you know, because I'm not trying to get like a ton of scraped information, I just need to get enough that you would see a public, whatever you're going to put on a public profile, that's the information I need, and it's actually not like the user themselves is the one that's saying, yes, this is the data I want to bring in.

01:38:09 - Jake Maymar
I'm just saving time for them, essentially.

01:38:12 - Brandon Hancock
Let me look it up, because, yeah, I mean, one of the hardest parts, LinkedIn, I mean, just any site where you want to like scrape anything from like a Twitter or a LinkedIn or anything like that is a huge pain.

01:38:24 - Brandon Hancock
There's a, I'm drawing a blank for the name, but there's a specific, if anyone else knows it off the top of their head, feel free to shout it out.

01:38:35 - Brandon Hancock
So there's, there's a couple I can throw out.

01:38:38 - Jake Maymar
So there's Appify, which is like, okay, but I'm worried about the compliance issues.

01:38:44 - Jake Maymar
Yeah.

01:38:45 - Jake Maymar
Um, uh, there's, there's a whole bunch of scrapers I could use, um, just basically, you know, scraping the web, um, and, you know, like, Make and N8N and all that have those integrations.

01:39:02 - Jake Maymar
Um, so yeah, I'm just, I'm trying to find something that's, you know, going to be fairly okay with GDPR.

01:39:12 - Brandon Hancock
I, yeah, I'm trying to look at the top of my head.

01:39:15 - Brandon Hancock
I, I, I know what it looks like.

01:39:17 - Brandon Hancock
I just cannot remember it off the top of my head of which one, but for the GDPR side of things.

01:39:23 - Brandon Hancock
Yeah.

01:39:24 - Brandon Hancock
I mean, I don't know why Appify wouldn't work.

01:39:27 - Brandon Hancock
I guess that's my big question.

01:39:30 - Brandon Hancock
Maybe it is Appify the one I'm thinking of.

01:39:32 - Brandon Hancock
I don't know why that one wouldn't work.

01:39:34 - Brandon Hancock
It looks like it should work, right?

01:39:37 - Jake Maymar
I mean, that's the thing.

01:39:38 - Jake Maymar
It looks like you should work.

01:39:39 - Jake Maymar
And, and if it's only basically, um, scraping public data, that's fine.

01:39:46 - Jake Maymar
Yeah.

01:39:47 - Brandon Hancock
Okay.

01:39:47 - Brandon Hancock
I'm looking at it right now and it's like...

01:39:55 - Jake Maymar
The weird thing is it's like Curious George is one integration and this other one is another.

01:40:01 - Jake Maymar
Oh, I want to just use the API.

01:40:04 - Jake Maymar
I just want to basically use the API.

01:40:06 - Jake Maymar
don't want to set up something else.

01:40:09 - Brandon Hancock
Dude, the LinkedIn API is a beast.

01:40:12 - Brandon Hancock
I've had to use it before for different companies and like it's so...

01:40:16 - Brandon Hancock
It works very well when you're just trying to do your own post or your own profile.

01:40:19 - Brandon Hancock
It's the second you want to start doing other people's stuff that...

01:40:22 - Brandon Hancock
I remember I had a ton of issues back like a little bit ago.

01:40:27 - Jake Maymar
Yeah, that's kind of what I'm running into too.

01:40:29 - Jake Maymar
That's why I was kind of looking for...

01:40:31 - Jake Maymar
Oh.

01:40:33 - Jake Maymar
Yeah, the Curious Coder.

01:40:34 - Jake Maymar
So that's the one I was looking at.

01:40:36 - Jake Maymar
But the problem is I don't know who this person is.

01:40:39 - Jake Maymar
And, you know, that's the problem.

01:40:42 - Jake Maymar
Like, that's that sort of thing.

01:40:45 - Jake Maymar
I'm to figure out.

01:40:46 - Brandon Hancock
I mean, yeah, I mean, I think GDPR is just, like, what data do you store about our users?

01:40:53 - Brandon Hancock
And like, in your case, it's like, even if I, like, all I'm storing about them is their name.

01:40:58 - Brandon Hancock
Like, yes, this one other service that is not mine is getting this much data, but I'm grabbing that, that and that, that are public facing.

01:41:06 - Brandon Hancock
Yeah, I'm not, I would be curious if you did like a deep research on it, like a CHGPT deep research, if you would, what it would say.

01:41:14 - Brandon Hancock
Okay.

01:41:15 - Jake Maymar
That's what I'll do.

01:41:16 - Jake Maymar
Yeah.

01:41:16 - Jake Maymar
Cause it, you know, this is a, it seems like all I do is just do the hardest thing, Brandon.

01:41:22 - Brandon Hancock
Hard mode.

01:41:23 - Brandon Hancock
We call it doing life on hard mode.

01:41:25 - Brandon Hancock
Oh, it's insane.

01:41:26 - Jake Maymar
Um, yeah.

01:41:28 - Jake Maymar
And then, and then the last question is, I know I'm asking a lot of questions.

01:41:31 - Jake Maymar
The last question is, um, is there a way to make, uh, MCPs compliant?

01:41:38 - Jake Maymar
Like I know you were talking to A2A was sort of a compliance, but the art.

01:41:43 - Jake Maymar
Because MCPs are definitely like.

01:41:45 - Jake Maymar
Like Wild Wild West, but then there, you know, there's ones, you know, the ones I use are the ones on the Anthropix site, but how secure is an MVP?

01:41:56 - Brandon Hancock
So what do you, so when you say to make it compliant, what, specifically to what?

01:42:03 - Jake Maymar
I guess the same thing, GDPR, like make it, like it doesn't have to be like super secure.

01:42:08 - Jake Maymar
I'm not trying to do like SOC 1, SOC 2, or HIPAA or anything like that.

01:42:11 - Jake Maymar
It just needed to be fairly secure.

01:42:16 - Jake Maymar
But I guess the question is, is it seems like every MCP is an MCP, so you have to kind of look at it and figure out what its vulnerability is and all that.

01:42:28 - Jake Maymar
There doesn't seem to be like a standard, I guess.

01:42:32 - Brandon Hancock
I mean, at the end of the day, a MCP is nothing more than a function call that has been wrapped to be accessible to agents.

01:42:41 - Brandon Hancock
Like that, the end of the day, like, so the real question is, is your underlying...

01:42:47 - Brandon Hancock
So I would strip back the phrase MCP and just look at it as like, all right, what I'm doing here is I am on, I'm going to perform this task.

01:42:57 - Brandon Hancock
Whether that's scrape data, whatever that task is, we just want to make sure whatever you're storing is okay.

01:43:04 - Brandon Hancock
Like that's the, and it's okay with the logs that are generated.

01:43:08 - Brandon Hancock
Like everything that gets generated, we have to make sure that it is, you know, proper and compliant.

01:43:15 - Brandon Hancock
And from my understanding too, with GDPR, one of the big requirements is to be able to delete data too.

01:43:20 - Brandon Hancock
Like if you get an email, you have so many days to delete data.

01:43:24 - Brandon Hancock
So you also just need to be able to have control over your logs to make sure that you can delete them.

01:43:31 - Brandon Hancock
That's the main, yeah, I think that's mostly, I think that's mostly it.

01:43:35 - Brandon Hancock
Okay, that's great.

01:43:36 - Jake Maymar
I mean, that's actually really, really helpful.

01:43:39 - Jake Maymar
Because yeah, I was just trying to get my head around it and understand that a little bit more.

01:43:43 - Jake Maymar
it.

01:43:43 - Jake Maymar
doing iveling.

01:43:44 - Brandon Hancock
Yeah.

01:43:45 - Brandon Hancock
Oh, then, you know, where's your Cursor shirt?

01:43:47 - Jake Maymar
I mean, you know, Google and Cursor, I totally see you getting sponsored.

01:43:50 - Brandon Hancock
No problem.

01:43:51 - Brandon Hancock
I, I, so I did like two weeks ago go out to that Google, Google Cloud, uh, competition.

01:43:57 - Brandon Hancock
I'll get to talk more about it as soon as they release the video.

01:43:59 - Brandon Hancock
All I wanted was a shirt.

01:44:01 - Brandon Hancock
I wanted a shirt or a hoodie.

01:44:03 - Brandon Hancock
And I didn't get one.

01:44:05 - Brandon Hancock
I was so sad.

01:44:07 - Brandon Hancock
I like, obviously I had a great time there, but I wanted swag, you know?

01:44:11 - Brandon Hancock
Oh, they should, yeah, they should give that.

01:44:14 - Jake Maymar
mean, that's kind of crazy.

01:44:15 - Jake Maymar
They should definitely give you a hoodie.

01:44:17 - Brandon Hancock
It was, yeah, it was off site.

01:44:20 - Brandon Hancock
So I think if I stayed an extra day, went to the office, I could have, but I just had to get back home.

01:44:25 - Brandon Hancock
But yeah, so I, I, uh, the second I get one though, I'm never taking it off.

01:44:29 - Brandon Hancock
So I will send you a picture whenever I get one.

01:44:32 - Jake Maymar
Excellent.

01:44:33 - Brandon Hancock
Thanks, Jake.

01:44:34 - Brandon Hancock
Yeah.

01:44:35 - Brandon Hancock
All right.

01:44:36 - Brandon Hancock
I think Lewis, you're up next.

01:44:37 - Brandon Hancock
I apologize, guys.

01:44:38 - Brandon Hancock
The order's all out of whack right now.

01:44:39 - Brandon Hancock
But, uh, I think Lewis, Alex, Alex, Andrew, Adam.

01:44:43 - Brandon Hancock
Oh, uh.

01:44:45 - Never2Nervous
Hello, everyone.

01:44:45 - Never2Nervous
Hey, Brandon.

01:44:46 - Brandon Hancock
Hey, how's it going, man?

01:44:48 - Never2Nervous
Good.

01:44:48 - Never2Nervous
Big fan.

01:44:49 - Never2Nervous
I love all your stuff.

01:44:52 - Never2Nervous
Thank you.

01:44:53 - Never2Nervous
So this is my first call, and I've been having some trouble with the application I'm trying to deploy.

01:45:00 - Never2Nervous
Thought I'd get some advice here.

01:45:03 - Never2Nervous
Background is in data science, so I'm a complete novice when it comes to, like, front-end application consumer products.

01:45:12 - Never2Nervous
Okay.

01:45:12 - Never2Nervous
Happy to help.

01:45:14 - Never2Nervous
Hey, don't be ashamed.

01:45:16 - Brandon Hancock
Lean into it, man.

01:45:16 - Brandon Hancock
Lean in.

01:45:17 - Never2Nervous
So the application I'm building is a SaaS factory.

01:45:23 - Brandon Hancock
Okay.

01:45:24 - Never2Nervous
And pretty much the idea behind it is I was thinking, okay, some of these large corporations, they have the funds and the resources to throw a bunch of ideas against the wall and see what sticks and then scale that idea.

01:45:39 - Never2Nervous
And the good ideas are usually what wins out.

01:45:42 - Brandon Hancock
Yeah.

01:45:42 - Never2Nervous
So I thought, okay, what if I could template- What if time,

01:45:45 - Never2Nervous
That process and automate it, so give people the ability to submit ideas, have it production ready and deployed, and then they can also, and I also have some agentic workflows that handles like automated marketing to get the idea out there into the world.

01:46:07 - Brandon Hancock
Okay.

01:46:08 - Never2Nervous
So base 44 is pretty much my direct competitor.

01:46:12 - Never2Nervous
Okay.

01:46:13 - Never2Nervous
So I don't know if you've heard of them.

01:46:16 - Brandon Hancock
Yeah.

01:46:16 - Brandon Hancock
I get, I get ads.

01:46:17 - Brandon Hancock
Oh, okay.

01:46:18 - Never2Nervous
Yeah.

01:46:19 - Never2Nervous
So they're like my direct competitor.

01:46:21 - Never2Nervous
Um, I've been having some trouble.

01:46:23 - Never2Nervous
Like I typically, um, have ChatGPT's agent mode do some user journey testing for me and then it comes back, give me a report of everything's wrong and I'll fix that.

01:46:36 - Never2Nervous
Um, but I've been having this issue with authentication.

01:46:41 - Never2Nervous
Um, and I've just been going in loops with it for like three weeks.

01:46:45 - Brandon Hancock
I Thank

01:46:47 - Never2Nervous
And the templates you put out recently on how to structure prompts to do tasks and things like that, that's been helpful in resolving things concisely, but this authentication issue has been persistent for me, and I'm not a front-end guy and I can't fix it.

01:47:08 - Never2Nervous
Okay, so let me do Google Authenticator and GitHub Authenticator for those two options.

01:47:15 - Never2Nervous
Okay.

01:47:16 - Never2Nervous
It seems to be like a routing issue.

01:47:18 - Never2Nervous
So once you log in, it doesn't route you back to the page for some reason.

01:47:22 - Brandon Hancock
I'm not sure.

01:47:24 - Brandon Hancock
Are you using, so give me a quick tech stack.

01:47:27 - Brandon Hancock
Are we doing Supabase?

01:47:28 - Brandon Hancock
Are we doing just clerk?

01:47:30 - Brandon Hancock
What are we doing to handle authentication?

01:47:33 - Brandon Hancock
Or are you just like directly working with the...

01:47:36 - Never2Nervous
Working with Google Cloud resources in the back-end.

01:47:41 - Brandon Hancock
Okay.

01:47:42 - Brandon Hancock
So I would...

01:47:44 - Brandon Hancock
Okay, and then just a

01:47:45 - Brandon Hancock
A other questions.

01:47:46 - Brandon Hancock
So what does full tech stack look like?

01:47:48 - Brandon Hancock
I think Next.js, if I had to guess.

01:47:51 - Never2Nervous
Yes.

01:47:52 - Brandon Hancock
Okay.

01:47:53 - Never2Nervous
Next Google for the database.

01:47:58 - Brandon Hancock
When you say Google for the database, are we in Firebase?

01:48:02 - Brandon Hancock
Are we using Firebase, or are we actually spun up a database in Google Cloud Platform?

01:48:08 - Never2Nervous
Yeah, I spun up a database in Google Cloud Platform.

01:48:12 - Brandon Hancock
Okay.

01:48:12 - Brandon Hancock
Yeah.

01:48:12 - Brandon Hancock
I think those resources are going to start costing me next month.

01:48:16 - Never2Nervous
Okay.

01:48:18 - Never2Nervous
But yeah.

01:48:19 - Never2Nervous
Yeah.

01:48:20 - Brandon Hancock
So, I big, so just high level first, before we dive into the actual problem, I think you were developing your first project, or you know, on hard mode, like this, like you, I would stay away from raw Google Cloud, unless you have to actually use it.

01:48:41 - Brandon Hancock
Uh, and, and not just, not that there's anything wrong with Google

01:48:45 - Brandon Hancock
I Cloud or AWS, but it's like there are simpler solutions that are like basically free.

01:48:50 - Brandon Hancock
So like, you know, today we've talked a ton about Supabase.

01:48:54 - Brandon Hancock
Like if you wanted to have a very simple app that had authentication, a database, a blob store, Supabase is awesome.

01:49:02 - Brandon Hancock
If you're like, I don't like Supabase, I want to go other options, you could pick and choose.

01:49:08 - Brandon Hancock
You could use Neon for your database, super generous free tier.

01:49:12 - Brandon Hancock
You could use Clerk, like Prim has talked about for today.

01:49:15 - Brandon Hancock
For a blob store, there's a thousand options of them.

01:49:19 - Brandon Hancock
Upload thing, great choice for a blob store.

01:49:22 - Brandon Hancock
Yeah, there's a thousand options you could pick.

01:49:25 - Brandon Hancock
I think the current tech stack is automatically going to make everything harder.

01:49:31 - Brandon Hancock
So, yeah.

01:49:34 - Brandon Hancock
And just cause like, I can just show you really fast how easy it is over here.

01:49:38 - Brandon Hancock
One second, I'll pull up a screen of like what it looks like in Supabase.

01:49:44 - Brandon Hancock
I just I gonna make sure I don't .

01:49:45 - Brandon Hancock
Will something again on accident?

01:49:47 - Brandon Hancock
One second.

01:49:52 - Brandon Hancock
Okay.

01:49:53 - Brandon Hancock
Authentication.

01:49:56 - Brandon Hancock
Yeah, because here's what it looks like.

01:49:58 - Brandon Hancock
I hope I don't share something I'm not supposed to.

01:49:59 - Brandon Hancock
One second.

01:50:00 - Brandon Hancock
I just need to click a button first.

01:50:02 - Brandon Hancock
Don't want to accidentally.

01:50:03 - Brandon Hancock
Okay.

01:50:06 - Brandon Hancock
Okay, I will share some stuff.

01:50:09 - Brandon Hancock
So, like, oh, wait, shoot.

01:50:11 - Brandon Hancock
Wrong thing.

01:50:12 - Brandon Hancock
Oh, God.

01:50:12 - Brandon Hancock
Sorry, guys.

01:50:13 - Brandon Hancock
Oh, God.

01:50:14 - Brandon Hancock
Wrong thing.

01:50:15 - Brandon Hancock
I'll delete that.

01:50:17 - Brandon Hancock
It swapped screens on me.

01:50:20 - Brandon Hancock
Okay.

01:50:20 - Brandon Hancock
One second.

01:50:21 - Brandon Hancock
Sign-in providers.

01:50:22 - Brandon Hancock
Here we go.

01:50:25 - Brandon Hancock
Desktop three.

01:50:26 - Brandon Hancock
Okay.

01:50:27 - Brandon Hancock
Now we're good.

01:50:28 - Brandon Hancock
So now you can see in Supabase, you can set up providers.

01:50:33 - Brandon Hancock
And it is so easy to say, like, I want to enable GitHub.

01:50:37 - Brandon Hancock
So you just click GitHub or Google.

01:50:40 - Brandon Hancock
It gives you a client ID and a client secret.

01:50:42 - Brandon Hancock
Career it.

01:50:43 - Brandon Hancock
And then all you have to.

01:50:45 - Brandon Hancock
to.

01:50:45 - Brandon Hancock
So to do is then if you wanted to allow Google, you hop over to Google, like you've already done, you've already done the hard part, and you're going to create, you're going to set up the OAuth consent screen and create the like web credentials, and you're done.

01:50:58 - Brandon Hancock
And you just paste those credentials back into Supabase, and things are great.

01:51:03 - Brandon Hancock
I think, let me stop sharing again, I want to make sure I don't click something I'm not supposed to.

01:51:07 - Brandon Hancock
But you just set up, yeah, then you just set up your redirect URLs, like this, to where, hey, I want to allow people to hit this endpoint, or these endpoints.

01:51:23 - Brandon Hancock
These are the only available endpoints.

01:51:26 - Brandon Hancock
If not, something went wrong.

01:51:28 - Brandon Hancock
So that's, like, Supabase makes it so easy.

01:51:31 - Brandon Hancock
So I would just recommend going with that.

01:51:34 - Brandon Hancock
If you're trying to just, first app, and you want it all to be, work pretty straightforward.

01:51:41 - Brandon Hancock
Yeah.

01:51:42 - Brandon Hancock
So I know I threw a lot at you.

01:51:43 - Brandon Hancock
Questions?

01:51:44 - Brandon Hancock
Questions?

01:51:44 - Brandon Hancock
.

01:51:45 - Never2Nervous
Yeah, I think I've gotten that far where I got into the end point where it redirects you to the other URLs, but it just doesn't work.

01:51:57 - Never2Nervous
But I can try swapping everything out for Superbase, so I'll do that.

01:52:03 - Brandon Hancock
And I'll just, and I'm sorry, just to dive in, like, I think the issue, like, what's actually happening is when you actually get the credentials from Google, what it's doing is in the header of the response, it's including, like, all the client, like, token, it's including so much information in the return, like, in the request URL and the header, where it has the user's token, it has the user's, it actually has a page to redirect to afterwards, like, it has all the information set up, but if your middleware is not properly set up to handle that, it's not going to take action on all the information you get back.

01:52:38 - Brandon Hancock
So then you end up in a loop where nothing actually is happening.

01:52:42 - Brandon Hancock
And the reason why I keep recommending Superbase, it's because, like, it...

01:52:45 - Brandon Hancock
It comes with middleware that is set up to consume all that information and properly log you in.

01:52:52 - Brandon Hancock
So if I had to guess, I think that's probably where issues are at right now.

01:52:56 - Never2Nervous
Okay, I'll give that a look-see.

01:52:58 - Never2Nervous
Thank you.

01:52:59 - Never2Nervous
Okay, dude, good luck.

01:53:01 - Brandon Hancock
The hardest part about coding is running your head into a wall on issues like this when you're like, dang it, why don't you just work?

01:53:08 - Brandon Hancock
So, dude, keep sticking to it.

01:53:11 - Brandon Hancock
Because the second you figure it out once, you're good for the rest of time.

01:53:14 - Brandon Hancock
So you just have to figure it out once.

01:53:16 - Brandon Hancock
And also, I mean, seriously, I would just check out full-stack application videos with Auth.

01:53:25 - Brandon Hancock
Because people have solved these videos or problems in the past.

01:53:28 - Brandon Hancock
So it's like, we don't have to do something insanely custom.

01:53:32 - Brandon Hancock
This is the beginning steps of like, cool, I have an application.

01:53:38 - Brandon Hancock
Next step, I want people to log in.

01:53:40 - Brandon Hancock
Like this is the second step all applications have.

01:53:42 - Brandon Hancock
So I would definitely...

01:53:44 - Brandon Hancock
...

01:53:44 - Brandon Hancock
...

01:53:45 - Brandon Hancock
I can see if I can actually find a quick resource for you.

01:53:47 - Brandon Hancock
Let me see if there's any good videos, I'd recommend Supabase, Next.js, Login, um, let's see, yeah, like, I would watch, here's a playlist that literally walks through Next.js plus Supabase, I actually need to make a video to compete against him, but, like, that is, like, I think it's, like, video three in that series has the exact, like, step.

01:54:15 - Brandon Hancock
That you need to, to follow.

01:54:17 - Brandon Hancock
So, I would just check out that.

01:54:18 - Brandon Hancock
You said the video of Next.js with Supabase.

01:54:21 - Never2Nervous
Uh, Prem, I saw you had your hand up, buddy.

01:54:24 - Prem
Yeah, I think most of the thing you're talking about, uh, you I was kind of struggling when I initially saw, uh, you know, to kind of build a SaaS.

01:54:30 - Prem
I think your course, like, on the, the AA full stack marketing platform, that kind of solved a lot of problems for me.

01:54:37 - Prem
So, again, I don't know whether Brandon is not kind of self-bragging here about his course.

01:54:41 - Prem
So, and, uh, you know, that goes to to kind of.

01:54:46 - Prem
You know, it kind of solved all the, you know, the full stack, you know, end to end for the needs for the SaaS I was building.

01:54:53 - Prem
So I just want to throw it out there.

01:54:55 - Brandon Hancock
Thank you, Prem.

01:54:55 - Brandon Hancock
I appreciate it.

01:54:56 - Brandon Hancock
And hey, if you can wait 25 days, dude, all this will be built for you automatically.

01:55:03 - Brandon Hancock
So you don't have to do this.

01:55:05 - Brandon Hancock
So these problems are already solved in ShipKit.

01:55:08 - Brandon Hancock
But yeah, would, key thing, I would just simplify.

01:55:11 - Brandon Hancock
I think that's the biggest thing.

01:55:12 - Brandon Hancock
I think right now you're using very big boy tools made for enterprise.

01:55:16 - Brandon Hancock
If we could just bring it back down to stuff made for more like solo developers where it's not a team.

01:55:22 - Brandon Hancock
Yeah.

01:55:22 - Brandon Hancock
So I would look at Supabase.

01:55:24 - Brandon Hancock
Yeah.

01:55:25 - Brandon Hancock
So, okay, cool.

01:55:26 - Brandon Hancock
Thank you.

01:55:26 - Brandon Hancock
All right, dude, good luck.

01:55:28 - Brandon Hancock
Keep us posted on your journey.

01:55:29 - Brandon Hancock
Okay.

01:55:29 - Never2Nervous
Will do.

01:55:30 - Never2Nervous
All right, Alex, you're up next, man.

01:55:34 - Alex Wilson
How's it going?

01:55:35 - Brandon Hancock
Hey, pretty good.

01:55:36 - Brandon Hancock
What fun projects we working on?

01:55:38 - Brandon Hancock
What's going on in Alex land?

01:55:40 - Alex Wilson
So, still looking for work, which is no fun.

01:55:44 - Brandon Hancock
The,

01:55:45 - Brandon Hancock
Dude, so walk me through the journey, where are we at, where are we going, how's, and how are you feeling, most importantly?

01:55:54 - Alex Wilson
I don't I feel all right.

01:55:56 - Alex Wilson
I am still going the standard, not trying to create my own work, but like, you know, find a nine to five, that type of stuff.

01:56:03 - Brandon Hancock
Yeah.

01:56:04 - Alex Wilson
So it's not fun, but it's, it's happening.

01:56:09 - Brandon Hancock
Curiosity, is it mostly, are we on LinkedIn?

01:56:12 - Brandon Hancock
Are we, is that where most of it's at?

01:56:14 - Alex Wilson
Okay.

01:56:15 - Alex Wilson
Yeah, LinkedIn, I, uh, because I was let go, I'm having LHH for my, um, account with my previous employer, so they're guiding and, you know, looking over my resume, all that good stuff.

01:56:30 - Alex Wilson
Okay.

01:56:32 - Brandon Hancock
And I took some time, I took a couple months.

01:56:34 - Alex Wilson
Yeah, definitely.

01:56:35 - Alex Wilson
But, um, ShipKit.

01:56:38 - Brandon Hancock
Hit me.

01:56:39 - Alex Wilson
I did it right away, and tested it out, and was surprised that I actually was was able to

01:56:45 - Alex Wilson
I up an app within, I think, about three days, and it actually worked.

01:56:49 - Alex Wilson
did run into problems with the authentication, so I'm looking forward to actually having access to the repository.

01:56:55 - Alex Wilson
I think it would have made it a lot easier.

01:56:58 - Brandon Hancock
The thing I want to show you, too, because these prompts, I'll actually be dropping them later, like a second round of updated prompts, but these prep templates have made a huge improvement.

01:57:11 - Brandon Hancock
So, like, I'm not sure, out of curiosity, did you go through prep templates, or how did you go about creating the app?

01:57:18 - Alex Wilson
I did, I started from one and went all the way through nine to create the project.

01:57:21 - Alex Wilson
I didn't actually read a lot of the stuff that it was building, I was just testing it.

01:57:25 - Alex Wilson
So, but it actually completely did it.

01:57:30 - Alex Wilson
Hell yeah, dude, I love it, I love it.

01:57:31 - Brandon Hancock
The thing that I think you're going to like so much better, this is the biggest one that I just added in, but what it does is it makes a roadmap, because, like, going from, like, a rough idea, which is here...

01:57:44 - Brandon Hancock
.

01:57:44 - Brandon Hancock
.

01:57:45 - Brandon Hancock
Like, you know, getting all the core ideas out of your head and into a system, what this does is it takes everything that you just thought of and turns it into a roadmap, so like I'll literally share this in the next day or so, I'll send you guys an email, but what it does is it actually turns, like, phase two, authentication, the thing we've been talking about, but it walks you through it, but the part that's cool is you literally, going forward to build apps, is you just copy and paste, like, alright, cool, I'm on phase three, paste, and then now it's like, make a task template to do this, so like, it actually lays out the next steps too, so making big improvements on that, just so it literally feels like the entire way something's walking you through the process, so, but, dude, that makes my heart so happy to hear that you're already making progress, and the full thing's not even there yet, that makes me happy, so.

01:58:43 - Alex Wilson
Thanks for making my day, Alex.

01:58:45 - Alex Wilson
No problem.

01:58:46 - Alex Wilson
Thank you.

01:58:47 - Alex Wilson
I'm really looking forward to it.

01:58:49 - Brandon Hancock
Awesome.

01:58:50 - Brandon Hancock
And real quick, going back to, I do want to focus more on job stuff because I just want to see how we can help community-wise.

01:58:59 - Brandon Hancock
Lewis just mentioned they're always hiring too.

01:59:02 - Brandon Hancock
So, hey, it's cool to be in a network of developers.

01:59:08 - Brandon Hancock
I can't remember.

01:59:09 - Brandon Hancock
I know we talked about it last week.

01:59:11 - Brandon Hancock
What was the specific type of work you were looking for?

01:59:17 - Alex Wilson
I think you want to move.

01:59:18 - Alex Wilson
So, I was a fraud analyst in my last career.

01:59:24 - Alex Wilson
So, financial analyst.

01:59:28 - Alex Wilson
I don't want to stick with banking and whatnot.

01:59:30 - Alex Wilson
And obviously, I'm interested in AI and that kind of stuff.

01:59:33 - Alex Wilson
So, I'd kind of like to find a small company that, you know, were founders and whatnot and just kind of watch it grow.

01:59:40 - Brandon Hancock
That would be ideal.

01:59:41 - Brandon Hancock
Yeah.

01:59:43 - Alex Wilson
Most of the people that-

01:59:45 - Alex Wilson
I've networked with and I know and whatnot are kind of big companies.

01:59:48 - Alex Wilson
It was one of the top three banks.

01:59:50 - Alex Wilson
So those are my peers.

01:59:54 - Brandon Hancock
I got you.

01:59:54 - Brandon Hancock
Where do you live?

01:59:55 - Brandon Hancock
You don't have to give me your actual address, but like what state?

01:59:58 - Alex Wilson
Colorado, Colorado Springs, out of Denver.

02:00:02 - Alex Wilson
Okay.

02:00:02 - Brandon Hancock
Well, I was gonna say, I mean, there's a pretty good amount of tech companies, I think, like compared to like, at least where I'm at.

02:00:10 - Brandon Hancock
There's zero where I live.

02:00:12 - Brandon Hancock
have to go to Atlanta.

02:00:14 - Brandon Hancock
Yeah.

02:00:14 - Brandon Hancock
Things.

02:00:14 - Brandon Hancock
I things I was.

02:00:15 - Brandon Hancock
I H the.

02:00:16 - Brandon Hancock
there so I'm I..

02:00:19 - Brandon Hancock
an.., I'm, first.

02:00:20 - Brandon Hancock
the like, the kick and though is like, I mean work-wise, like every startup I've worked at it has always been over 40 hours.

02:00:28 - Brandon Hancock
That's the only problem that I like, yes, on paper, it's always 40 hours, but it always ends up being more.

02:00:33 - Brandon Hancock
It's never been less.

02:00:35 - Brandon Hancock
I will say that it's never gone down.

02:00:38 - Brandon Hancock
Um, the other option.

02:00:40 - Brandon Hancock
Um, so my wife, she's, she's a consultant consulting firms.

02:00:45 - Brandon Hancock
I do this like a weird place to look at.

02:00:47 - Brandon Hancock
They always need developers because they always get work and they always need extra help.

02:00:51 - Brandon Hancock
So it's called UHY.

02:00:53 - Brandon Hancock
I can see if they have anything.

02:00:55 - Brandon Hancock
I'll talk to her after we get off the call, but see if they have any stuff too.

02:00:59 - Brandon Hancock
But I would just check out also like consulting firms because most developers are always like, I want a tech company, but with your background, you're kind of versatile, you know?

02:01:09 - Brandon Hancock
Like it's not just I'm this box, you know?

02:01:13 - Brandon Hancock
It's like, oh, I actually have a wider array of skills, which would work a lot, really well in a consulting company.

02:01:20 - Brandon Hancock
Um, and there's so many of those.

02:01:21 - Brandon Hancock
So I can, I can ask right after this, um, if, she knows anything, but yeah, dude, we got to get you, uh, got to get you hired and making that, making the dollars.

02:01:29 - Brandon Hancock
Um, so yeah.

02:01:32 - Brandon Hancock
Um, so the good news is I am on severance, so I am good until next year.

02:01:36 - Brandon Hancock
So I'm not like hurting or anything.

02:01:39 - Alex Wilson
I just, it'll be nice to double dip for a while.

02:01:43 - Alex Wilson
So, you know, Hey, no, I,

02:01:45 - Alex Wilson
I Got to get that over-employed, man.

02:01:48 - Brandon Hancock
I will say real fast, just on the topic of money, no money, I'll just give you guys background real fast.

02:01:57 - Brandon Hancock
So obviously, jobs my entire life until leaving Crew AI, and then at that point, it was like, okay, it's like eat what you kill kind of thing.

02:02:06 - Brandon Hancock
Unless I do something valuable to the world, no money comes in.

02:02:10 - Brandon Hancock
So launching courses and doing stuff and freelancing work, your stress, yes, you can make more, but I'll just be honest with you guys, it is stressful.

02:02:20 - Brandon Hancock
I feel like a lot of developers don't talk about it enough.

02:02:23 - Brandon Hancock
They're just like, oh yeah, it's so easy, it's so fun.

02:02:26 - Brandon Hancock
No, it's free.

02:02:27 - Brandon Hancock
I told my wife all the time, was like, I'm going to have so many gray hairs by the time I actually turn 30 here in a few months.

02:02:33 - Brandon Hancock
And I was like, I'm going to look so old, because there's so much extra stress that goes to it.

02:02:38 - Brandon Hancock
I wouldn't trade it for the world.

02:02:39 - Brandon Hancock
I absolutely love it.

02:02:40 - Brandon Hancock
But just being honest, when money's not coming in, and you see your credit card bills going, credit going up.

02:02:45 - Brandon Hancock
It's like, you just gotta live.

02:02:46 - Brandon Hancock
It's very stressful.

02:02:47 - Brandon Hancock
So my friends keep asking to hang out right now.

02:02:50 - Brandon Hancock
And I tell them every day, I'm like, guys, I'm a broke .

02:02:53 - Brandon Hancock
Like I have to do this course or else I have nothing coming in, you know?

02:02:59 - Brandon Hancock
So, and I have to go, you know, freelance work and figure things out.

02:03:02 - Brandon Hancock
But yeah, so yeah, definitely want get you an extra job.

02:03:06 - Brandon Hancock
It's nice that Severance is coming in.

02:03:09 - Brandon Hancock
But yeah, it would be very nice to double dip.

02:03:11 - Brandon Hancock
Yeah, you're double dipping.

02:03:13 - Brandon Hancock
I'm trying to go from zero to one.

02:03:18 - Brandon Hancock
So, but yeah, I will ping her.

02:03:22 - Brandon Hancock
She's hanging out with her friends after yoga right now.

02:03:25 - Brandon Hancock
But I will ping her as soon as she gets home to see if she knows anything.

02:03:30 - Alex Wilson
Excellent, thank you.

02:03:31 - Brandon Hancock
Yeah, of course, Alex.

02:03:33 - Never2Nervous
Alex, I also work for a consulting firm, one of the big fours.

02:03:37 - Never2Nervous
And I can definitely get your resume in front of a human and not a robot, especially interested.ак sicken� savings Okay.

02:03:45 - Never2Nervous
I will hitch up.

02:03:46 - Never2Nervous
Yeah.

02:03:47 - Brandon Hancock
Do you, do you, what would be the best way for y'all to connect just inside of school?

02:03:53 - Brandon Hancock
You just, Lewis, which you might have to look up his last name, because that's, Lewis, what's your last name?

02:03:58 - Brandon Hancock
Just because like that's.

02:04:00 - Never2Nervous
Lewis, Lewisius, L-O-U-I-S-I-U-S.

02:04:09 - Brandon Hancock
Cool.

02:04:09 - Brandon Hancock
I just know I tried to connect with people sometimes in school and I'm like, oh my God, there's 30 of them, you know?

02:04:14 - Brandon Hancock
So it's like, that's like the hard part.

02:04:17 - Brandon Hancock
So thank you for sharing that.

02:04:18 - Never2Nervous
Yeah.

02:04:19 - Never2Nervous
Go team.

02:04:19 - Brandon Hancock
Go team.

02:04:20 - Brandon Hancock
No developers left behind.

02:04:21 - Brandon Hancock
I love it.

02:04:22 - Brandon Hancock
All right.

02:04:23 - Brandon Hancock
Adam, you're up next, man.

02:04:25 - Brandon Hancock
What is going on?

02:04:26 - Brandon Hancock
Any cool projects?

02:04:27 - Brandon Hancock
Anything we can help with?

02:04:29 - Adam
Well, if Alex is looking to work for free, I'm hiring.

02:04:36 - Adam
Alex, I mean, the work is there.

02:04:40 - Brandon Hancock
That's funny.

02:04:43 - Adam
So, Brandon, I was going through your.

02:04:45 - Adam
Yeah.

02:04:45 - Adam
I ADOA tutorial, and I noticed the tutorial calls for preview versions of some of the Gemini models, and apparently they're no longer available, so I sent you a pull request.

02:04:59 - Brandon Hancock
Oh, okay.

02:05:01 - Brandon Hancock
Awesome.

02:05:03 - Adam
So today I just had coffee with a guy, he actually lives in my same town as me, found me on the internet.

02:05:11 - Adam
He's a headhunter for hedge funds.

02:05:16 - Adam
Oh, that's cool.

02:05:19 - Adam
And his current process is he has a bunch of documents, and he copy-paste prompts and documents into ChatGPT, gets the results and does whatever with them.

02:05:32 - Adam
And I'm like, oh yeah, that's my perfect client, right, because I can just automate all of that.

02:05:38 - Brandon Hancock
Yeah, that's awesome.

02:05:39 - Brandon Hancock
So did y'all get to talk numbers, deals?

02:05:42 - Adam
Did y'all get to get into that?

02:05:43 - Adam
Um, right now

02:05:45 - Adam
He's going to send me what his long-term AI goal is and then like a list of low-hanging fruit.

02:05:52 - Adam
I'm a little nervous because I'm thinking if I just slam dunk this project, he can introduce me to all his hedge fund buddies, which you know, I figure there's some money there to be made.

02:06:04 - Brandon Hancock
No, that's awesome.

02:06:05 - Brandon Hancock
I mean, this sounds like an insanely cool opportunity.

02:06:08 - Brandon Hancock
And I'll go ahead and say it, the doing some of your first or like, you know, bigger projects that could lead to bigger things.

02:06:16 - Brandon Hancock
Hey, dude, totally no one will be stressed out.

02:06:18 - Brandon Hancock
Uh, but dude, we gotta, we gotta bet on ourselves, man.

02:06:21 - Brandon Hancock
So I, uh, dude, rooting for you and you got a bunch of developers too, to, to help out too, if you, uh, if you run into issues.

02:06:27 - Brandon Hancock
So, um, yeah.

02:06:29 - Brandon Hancock
So out of curiosity, have you guys got to like dive into like what would be actually automated?

02:06:35 - Brandon Hancock
Um, like, did y'all get into details or, you know, there anything that's like stressing you out?

02:06:39 - Adam
main thing is, um, well, not main thing.

02:06:42 - Adam
One thing he's worried about is if he puts all his stuff, uses.

02:06:45 - Adam
ChadGPT, someone's going to hack GPT and get all this data.

02:06:49 - Adam
So he's a little worried about that.

02:06:52 - Adam
So he wants to use open source stuff, which is fine by me, right?

02:06:58 - Brandon Hancock
Yeah.

02:06:58 - Brandon Hancock
I mean, it's so funny.

02:07:01 - Brandon Hancock
I agree with the concern, but if someone hacked ChadGPT, the amount of social security numbers they would have, the amount of credit card numbers they would have, it would take a very deliberate actor to be like, no, this guy, I'm copying his stuff.

02:07:16 - Brandon Hancock
Like, you know, they would probably steal Sam Altman's messages before they stole his, you know?

02:07:22 - Brandon Hancock
Right.

02:07:23 - Adam
But totally valid concern.

02:07:26 - Brandon Hancock
So it sounds like he wants to use local models.

02:07:32 - Adam
I think we're going to do models hosted in like Vertex or something like that.

02:07:39 - Brandon Hancock
Yeah.

02:07:40 - Brandon Hancock
Okay.

02:07:40 - Brandon Hancock
Okay.

02:07:41 - Brandon Hancock
Oh yeah.

02:07:41 - Brandon Hancock
So in that case, yeah.

02:07:42 - Brandon Hancock
I mean that you could easily.

02:07:44 - Brandon Hancock
Which is even easier.

02:07:45 - Adam
Yeah.

02:07:46 - Adam
Yeah.

02:07:47 - Brandon Hancock
Yeah.

02:07:47 - Brandon Hancock
So any other big areas he has a concern or you have a concern?

02:07:51 - Brandon Hancock
Cause like one of like, I think what stresses me out the most about new stuff is like, I hate vague, you know?

02:07:58 - Brandon Hancock
Oh.

02:07:58 - Brandon Hancock
like, I always like to be like, what am I concerned about?

02:08:02 - Brandon Hancock
And I list it out and then I just try and get answers as quickly as possible to all of those.

02:08:06 - Brandon Hancock
So is there anything else that's stressful or anything?

02:08:10 - Adam
Well, not related to this, but, uh, I've been, I guess, I don't know, collaborating or planning stuff with, there's, a person she has got, I guess she's calling it a fractional business development agency, which is, I found out is basically like outsourcing your sales to her.

02:08:30 - Brandon Hancock
Oh yeah.

02:08:31 - Adam
And she's going to give me a discount if I help her with her website.

02:08:36 - Adam
And, um, I was going to use react and flask, but now I'm thinking, hearing all the stuff.

02:08:45 - Adam
I should go with the Supa-based Node.js route instead.

02:08:52 - Brandon Hancock
So, quick questions on her website.

02:08:56 - Brandon Hancock
Is it a static website?

02:08:59 - Brandon Hancock
Is there- No, it's just an app, but not a very complex, just a CRUD app, basically.

02:09:05 - Brandon Hancock
Oh, okay.

02:09:05 - Brandon Hancock
Yeah.

02:09:06 - Brandon Hancock
So, I mean, big, and is there a front-end, sorry, is there a static website as well for people to like- sign up or see it on the web, or is it strictly internal?

02:09:19 - Adam
Um, yeah, it would be a, um, an external-facing website, yeah, with like a landing page and signing up and all that stuff.

02:09:30 - Brandon Hancock
Yeah.

02:09:31 - Brandon Hancock
So, big, big recommendation I have is strictly, like, why I love Next.js and Vercel so much together, is because of all of the, like, when you're creating pages, a lot of the time you

02:09:45 - Brandon Hancock
have static pages and for better SEO optimization to help rank better, like Next.js coupled with Vercel knows how to actually serve certain aspects of your page so that when like Google is crawling everything, it can actually see your static pages because one of the big issues when you're using like just a normal React app and you're not using Next.js is everything is rendered through JavaScript.

02:10:13 - Brandon Hancock
Right.

02:10:14 - Brandon Hancock
when something comes to check out your site, it's like, dude, I actually can't tell what's going on.

02:10:19 - Brandon Hancock
Like nothing about this makes sense until I load and use like something to render the JavaScript.

02:10:24 - Brandon Hancock
So I big, big, big, big, big of what Next.js is doing because you can make, you can easily add the SEO tab.

02:10:32 - Adam
Well, right if someone goes on their phone, right?

02:10:34 - Adam
Those little tiny, you know, cell phone processor in the JavaScript.

02:10:39 - Adam
Yeah.

02:10:39 - Brandon Hancock
Yeah.

02:10:39 - Brandon Hancock
yeah.

02:10:40 - Brandon Hancock
Yeah.

02:10:41 - Brandon Hancock
Big, like my main recommendation, Next.js.

02:10:44 - Brandon Hancock
I mean, this.

02:10:45 - Brandon Hancock
The second you use it, it is very hard to go back.

02:10:48 - Brandon Hancock
Once it clicks, once it clicks, it's just so hard to go back.

02:10:54 - Brandon Hancock
So, yeah, you'll have to keep us posted.

02:10:59 - Brandon Hancock
I'd love if you're allowed to share anything about the website as you build it or maybe just have a cool deal.

02:11:03 - Adam
No, she's already had me sign an NDA on it, so, yeah.

02:11:07 - Adam
Okay, never mind, don't share.

02:11:10 - Brandon Hancock
I can't get you fired.

02:11:13 - Brandon Hancock
All right, perfect.

02:11:14 - Brandon Hancock
Any final things, Adam?

02:11:15 - Brandon Hancock
just want to make sure.

02:11:15 - Brandon Hancock
No, that's it for me.

02:11:18 - Brandon Hancock
Okay, perfect.

02:11:19 - Brandon Hancock
Well, hey, thank you guys so much for hopping on.

02:11:22 - Brandon Hancock
Always love, oh, real fast.

02:11:23 - Brandon Hancock
Is there anyone else on the call that wants to go?

02:11:25 - Brandon Hancock
I know, if so, if you just want to put your camera on.

02:11:30 - Brandon Hancock
Hamal, I didn't know if you want to.

02:11:32 - Brandon Hancock
Okay, perfect.

02:11:32 - Brandon Hancock
I just pulled up the list.

02:11:35 - Hemal Shah
Yeah, I'll be quick.

02:11:36 - Hemal Shah
I know it's already two hours in.

02:11:38 - Hemal Shah
So, I continued working on my kind of interactive chat application, if you may.

02:11:44 - Hemal Shah
So, it's your...

02:11:45 - Hemal Shah
So just plain text, request response, there are rich content media on your chatbot, you can have rich HTML elements, dropdown, calendar picker to get the missing information.

02:11:57 - Hemal Shah
So user is requesting something, I want to book a travel or something and whatever, if user is not part of all the requested information, the assistant can extract the user's intent, identify what are the missing information, check for completeness, and then return back with some structure with, hey, give me this, give me dates, give me, if you want to travel somewhere, here is only pre-selected list of items that you can choose from.

02:12:25 - Hemal Shah
So some type of drop and all those type of things.

02:12:28 - Hemal Shah
So looking into it, working with the ADK that you created, and I second what Ola said earlier, that if you had not created that video, I would not have learned it from Google's documentation.

02:12:39 - Brandon Hancock
I would have left it from maybe left it from Google's or something else.

02:12:45 - Hemal Shah
I find a little bit more user-friendly, but no, that documentation is helping a lot, and ADK-Web is amazing, I can proof, I can test the agent, I must be multi-agent because there are multiple steps involved, like completeness check before I hit the trigger and all that, but there were certain, I went into issue, I'm learning a lot, but run into issue where I want a routing type of workflow, where I know I went to sequential, parallel agent, but there's a condition, if completeness, if completeness check is good, then you move for the execution, if it is not, if they are missing information, then I need to add more metadata around it, I was able to figure that out using some custom agent, so yeah, that was another thing, I went to your crash course to see if there's a custom agent example, but then I created it going through that awful documentation on Google's website, but yeah, I it, I did it, it,

02:13:46 - Hemal Shah
I complain to them too.

02:13:48 - Brandon Hancock
It's wild that they can't get documentation right.

02:13:52 - Brandon Hancock
So here's what I was going to, I'm going to drop this in the chat real fast.

02:13:56 - Brandon Hancock
So they have a ton of examples.

02:13:58 - Brandon Hancock
You just have to know where to dig for them.

02:14:01 - Brandon Hancock
But the main, I'm trying to figure out which one of these would be a good, maybe it's this one.

02:14:08 - Brandon Hancock
There's one or two, sorry, let me share my screen.

02:14:11 - Brandon Hancock
There's one or two that would be really helpful.

02:14:15 - Brandon Hancock
I just want to see if I can find one.

02:14:17 - Brandon Hancock
Can you guys, I think it's sharing the right screen.

02:14:21 - Brandon Hancock
But their prompts, let's see if they have this phase.

02:14:25 - Brandon Hancock
No, let me, let me go back out.

02:14:29 - Brandon Hancock
Let's go to Python.

02:14:30 - Brandon Hancock
So here's, let's do this.

02:14:33 - Brandon Hancock
They usually have like phase.

02:14:36 - Brandon Hancock
So they usually, let's do search in this repository.

02:14:43 - Brandon Hancock
No.

02:14:44 - Brandon Hancock
No.

02:14:45 - Brandon Hancock
They have some examples and what they do is they actually have an orchestrator.

02:14:50 - Brandon Hancock
The orchestrator has phases.

02:14:52 - Brandon Hancock
it's like phase one, gather information.

02:14:55 - Brandon Hancock
When you're gathering information, you can direct to agent one, two or three.

02:15:00 - Brandon Hancock
Fantastic.

02:15:01 - Brandon Hancock
Once you have completed phase one, move to phase two.

02:15:04 - Brandon Hancock
When you're in phase two, you can route to these three agents.

02:15:07 - Brandon Hancock
So they specifically call out how to, at multiple steps or how to route to the necessary, to the necessary different people.

02:15:18 - Brandon Hancock
I think it could be, they had one where they did a, I just want to find it for you so you can actually see it, or maybe it was on YouTube.

02:15:28 - Brandon Hancock
They had a really good one that did, it was with a browser agent.

02:15:32 - Brandon Hancock
Let me find this real fast.

02:15:33 - Brandon Hancock
I, YouTube ADK browser agent.

02:15:40 - Brandon Hancock
Perfect.

02:15:40 - Brandon Hancock
Okay.

02:15:40 - Brandon Hancock
I found it.

02:15:41 - Brandon Hancock
Let me.

02:15:46 - Brandon Hancock
Point it to you.

02:15:47 - Brandon Hancock
Okay.

02:15:48 - Brandon Hancock
All right, cool.

02:15:48 - Brandon Hancock
Let me share one more time.

02:15:50 - Brandon Hancock
I'll share the repository with you as well.

02:15:54 - Brandon Hancock
But yeah, so I think this is the prompt.

02:15:58 - Brandon Hancock
Yeah.

02:16:00 - Brandon Hancock
So they do a pretty good job of like calling it out in steps.

02:16:06 - Brandon Hancock
And they call it out.

02:16:07 - Brandon Hancock
like, imagine like, in your case, it's like step one, gather all information.

02:16:12 - Brandon Hancock
This agent is going to be the one who handles it.

02:16:14 - Brandon Hancock
Once that agent is done, we come back up here, then the main agent does something.

02:16:19 - Brandon Hancock
So I will share this with you.

02:16:21 - Brandon Hancock
But this is probably one of the better examples of like how you can actually push ADK to its limits to actually, you know, do some more fancy stuff.

02:16:31 - Brandon Hancock
So you can see like in that prompt to start off, they have gather brand information.

02:16:36 - Brandon Hancock
So in your case, it could be gather travel information.

02:16:40 - Brandon Hancock
Then they go into further steps.

02:16:42 - Brandon Hancock
So I would 100% recommend check.

02:16:45 - Brandon Hancock
Checking that out, and quick cheat code, what I always do is when I'm working on stuff is I always have, like when I'm working on another project, I always make a ref folder, and then in here I would clone in this project that I just showed you and say, hey, I'm trying to make something like this.

02:17:06 - Brandon Hancock
Can you help me update my prompt to look like this reference project?

02:17:10 - Brandon Hancock
And this is a really quick way you could dump in three or four projects that you like, heck, you could dump in any YouTube videos that I've made, just dump them in there and say, I'm trying to steal this from Brandon's code, this from Google's code, and this from another project.

02:17:23 - Brandon Hancock
Can you please help me make this prompt work well?

02:17:26 - Brandon Hancock
Perfect.

02:17:27 - Hemal Shah
Thank you.

02:17:28 - Brandon Hancock
Yeah.

02:17:28 - Brandon Hancock
This is great.

02:17:29 - Hemal Shah
I think transferring back to main agent, I did not have thought about that.

02:17:33 - Hemal Shah
That's great.

02:17:34 - Hemal Shah
Then we can, then sky's the limit.

02:17:35 - Hemal Shah
Now you can mix and match however you want.

02:17:38 - Hemal Shah
I have two more quick follow up questions, if I may.

02:17:41 - Brandon Hancock
Of course.

02:17:41 - Brandon Hancock
Yeah.

02:17:42 - Brandon Hancock
Oh, Well, want Tom, if you have a quick question and then.

02:17:45 - Brandon Hancock
Hemal, can go right back.

02:17:47 - Tom Welsh
No, no, I'll let him finish.

02:17:48 - Tom Welsh
Mine comes afterwards.

02:17:50 - Brandon Hancock
Oh, okay.

02:17:50 - Brandon Hancock
Perfect.

02:17:51 - Brandon Hancock
All right.

02:17:51 - Brandon Hancock
Back to you, buddy.

02:17:53 - Hemal Shah
So ADK will take care of all these things, but then there is a chat UI in front of it and then chat API, which is fast API.

02:18:02 - Hemal Shah
So the request response model between UI and API, chat request, chat response.

02:18:09 - Hemal Shah
I think it's very standard.

02:18:10 - Hemal Shah
There are so many applications out there.

02:18:11 - Hemal Shah
I'm wondering if there is any standard JSON model that most of people are using when we send a request to API and then when the response comes back.

02:18:22 - Hemal Shah
The JSON structure that I can build on top of it.

02:18:26 - Hemal Shah
I'm wondering if there is a combination there.

02:18:28 - Brandon Hancock
And you're talking about specifically with ADK, correct?

02:18:31 - Hemal Shah
I mean, in general, whenever we are making this type of AI based chat bot, when you ask questions that could be follow up, that could be some responses like the JSON structure to communicate.

02:18:45 - Hemal Shah
Thank you.

02:18:45 - Hemal Shah
Between UI and API.

02:18:47 - Brandon Hancock
So at least in ADK land and Gemini land, they do it through parts.

02:18:54 - Brandon Hancock
So a part can be a type string, and that's like a message contains parts, parts contain text, like images, like, yeah.

02:19:04 - Brandon Hancock
So here is, I think, the best course or example application they've created.

02:19:12 - Brandon Hancock
It has a front end and a back end, and what you'll notice is in the front end, I'll share my screen in a second, um, URL, um, shoot, um, let's actually go back a page, no, they don't have it.

02:19:30 - Brandon Hancock
But long story short, whenever you run ADK, you can literally do ADK serve API, and what that will do is actually expose endpoints to your ADK application.

02:19:41 - Brandon Hancock
So, let me show you the code for that.

02:19:44 - Brandon Hancock
So, agent.

02:19:44 - Brandon Hancock
Agent.

02:19:45 - Brandon Hancock
Agent.

02:19:45 - Brandon Hancock
Development Kit, Serve, API.

02:19:50 - Brandon Hancock
Yeah, what it automatically does is it converts your agent, like, technically when you do ADK Web, what's happening behind the scenes is it spins up ADK using a fast API, and you have access to sessions, you can trigger runs, like it opens up an entire fast API around ADK, and it's also at the same time spinning up a UI.

02:20:11 - Brandon Hancock
So when you're doing ADK Web, you get both, you know?

02:20:16 - Brandon Hancock
So we're trying to serve API.

02:20:18 - Brandon Hancock
Why is it not showing it?

02:20:22 - Brandon Hancock
Agent Element Kit.

02:20:24 - Hemal Shah
Brandon, what I'm doing is something like embedding the whole ADK into my fast API backend, because before ADK, I'm doing some security checks, you I want to do some extra processing.

02:20:38 - Hemal Shah
So, and I also kind of want to decouple ADK from my chat application.

02:20:45 - Hemal Shah
Bye.

02:20:45 - Hemal Shah
Maybe I replace ADK with crew AI in future or some other better versions.

02:20:49 - Hemal Shah
I'm creating that layers and that's what I'm kind of focusing on chat UI and chat API.

02:20:56 - Hemal Shah
then chat API is communicating with ADK.

02:20:59 - Hemal Shah
Right now it is embedded in within that one container, but maybe I can do API, but that communication is what I was focusing on between UI to API.

02:21:10 - Hemal Shah
Agnostic of Google ADK because I can change ADK in future if they're a better version.

02:21:17 - Brandon Hancock
So usually what you want to do is have some sort of like in your whatever wrapper for your agents, you usually either want to have like a run or we'll just call it run.

02:21:27 - Brandon Hancock
That's usually what it usually is.

02:21:28 - Brandon Hancock
Run, kick off, depending on what framework.

02:21:31 - Brandon Hancock
Those are typical languages that you use.

02:21:33 - Brandon Hancock
Then when it comes to response types, mean, the hard part about this is the, or not the hard part, the two most common return types are SSE, server-side events, which are going to stream back.

02:21:45 - Brandon Hancock
Small chunks where it's gonna say content and author, and it usually, that's how you can get back a stream of data and start to build out that response.

02:21:55 - Brandon Hancock
That's the most common one for streaming, SSE.

02:21:59 - Brandon Hancock
The other one is just a straight up JSON object, which just has content and author and, you know, whatever else you want to add to it.

02:22:08 - Brandon Hancock
But yeah, usually, and I mean, you can see this in, like, if you dive into ADK docs, like the actual source code, you can see how they handle server-side events and JSON events.

02:22:21 - Brandon Hancock
Like, and you could use, steal some inspiration from that.

02:22:24 - Brandon Hancock
Heck, you could literally copy the agent development kit library as a reference and say, hey, I like how they make it to where their models can return server-side events or JSON fragments.

02:22:34 - Brandon Hancock
I would like to do that in my own app.

02:22:37 - Brandon Hancock
And you could, no, no reason to reinvent the wheel.

02:22:40 - Brandon Hancock
Let the agents, as long as they have access to the code, they can recreate it, you know?

02:22:44 - Brandon Hancock
of Open Let's Open Open you.

02:22:45 - Hemal Shah
Okay, perfect.

02:22:46 - Hemal Shah
And my second quick question, this is going to be long.

02:22:50 - Hemal Shah
I went through your ADK voice tutorial as well.

02:22:54 - Hemal Shah
And that is another thing I'm dabbling with, playing with.

02:22:58 - Hemal Shah
And my question is, if you want to create a voice assistant for customer support, which taps into your businesses, ERP, CRM, you know, it can really help.

02:23:10 - Hemal Shah
Yeah.

02:23:11 - Hemal Shah
There are many 11 labs, mean, voice flow, there are many tools out there.

02:23:16 - Hemal Shah
My question is, is there a, have anybody, any recommendation like this is better than other or, or full blown voice assistant?

02:23:26 - Brandon Hancock
Um, I mean, at this point for recommendations, I mean, I, I would actually, cause in that tutorial, it was voice with ADK.

02:23:35 - Brandon Hancock
What I would actually recommend after building that out is just using the straight up Gemini live.

02:23:40 - Brandon Hancock
Library instead, just because at the end of the day, when you.

02:23:45 - Brandon Hancock
You start to do agent calls to function calls.

02:23:47 - Brandon Hancock
It starts to get really weird.

02:23:49 - Brandon Hancock
So I would actually, after making that video, I would just use the straight up Gemini Live library instead, if you're trying to use Google stuff.

02:23:57 - Brandon Hancock
If you're looking for no code tools, I like Bland.

02:24:00 - Brandon Hancock
They do a really cool one.

02:24:02 - Brandon Hancock
Bastion found a really cool voice.

02:24:05 - Brandon Hancock
Bastion and Maxim actually used one recently.

02:24:08 - Brandon Hancock
I think it's called LiveKit.

02:24:10 - Brandon Hancock
Yeah.

02:24:10 - Brandon Hancock
I think this is one you would like.

02:24:13 - Brandon Hancock
Oh, shoot, wrong thing.

02:24:15 - Brandon Hancock
So we found this out when we were going to try and do some work for a potential client, but it's called LiveKit.

02:24:22 - Brandon Hancock
So you get to do some code, like, you get the best of both worlds.

02:24:26 - Brandon Hancock
Like, it's already a pre-created library.

02:24:28 - Brandon Hancock
It works well.

02:24:29 - Brandon Hancock
You can host it.

02:24:30 - Brandon Hancock
You can hook it up to phones.

02:24:33 - Brandon Hancock
So yeah, I would actually, I would take all that back.

02:24:35 - Brandon Hancock
I would just use what these guys are doing.

02:24:37 - Brandon Hancock
You can build your own agents.

02:24:39 - Brandon Hancock
It's a really awesome platform, what they've set up.

02:24:43 - Hemal Shah
Yeah, thank you very much.

02:24:44 - Hemal Shah
you.

02:24:45 - Hemal Shah
All right, perfect.

02:24:46 - Brandon Hancock
All right, Tom, final question, and then I got to go run.

02:24:50 - Tom Welsh
Those are ship kits, it's all about you now.

02:24:53 - Tom Welsh
Obviously, I didn't go to bed, I started coding, so I'm just going to get pushed, I just pushed all my rules to get.

02:25:00 - Tom Welsh
That's a violation of your license, isn't it?

02:25:03 - Brandon Hancock
No.

02:25:04 - Brandon Hancock
No.

02:25:05 - Brandon Hancock
No, I mean, I think the only one, because I was going to update the license stuff, is like, the main rule is like, don't publish ship kit to like, a blank repo, a public repo, like that was the only, the only one, but like, doing your own stuff was totally, I mean, it's the whole point, it's a, it is the boilerplate code for you to take it and go make your own applications.

02:25:28 - Brandon Hancock
So yeah, you're, you, you were sued, then you're unsued, you know, so you're good.

02:25:33 - Tom Welsh
Excellent.

02:25:34 - Tom Welsh
Got to clear that up.

02:25:36 - Brandon Hancock
All right, perfect.

02:25:38 - Brandon Hancock
All right, thank you, Tom.

02:25:40 - Tom Welsh
Sorry, bye.

02:25:42 - Brandon Hancock
All right, perfect.

02:25:43 - Brandon Hancock
All right, guys, wait, I gotta.

02:25:45 - Brandon Hancock
I gotta hop off, but it was awesome getting to see all of you.

02:25:47 - Brandon Hancock
Good luck, keep me posted on all of your awesome projects and look forward to seeing you guys next week.

02:25:53 - Brandon Hancock
All right, you have a great one guys, see ya.

